#!/usr/bin/env node

import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';

const API_BASE = 'https://api.clickup.com/api/v3';

function printUsage() {
  console.log(`Usage:
  node scripts/clickup-doc-to-md.mjs <clickup_doc_url> [output.md]
  node scripts/clickup-doc-to-md.mjs <clickup_doc_url_1> <clickup_doc_url_2> ...
  node scripts/clickup-doc-to-md.mjs --input ./clickup-links.txt [--out-dir ./exports]

Environment:
  CLICKUP_API_TOKEN=your_clickup_token

Examples:
  CLICKUP_API_TOKEN=xxx node scripts/clickup-doc-to-md.mjs "https://app.clickup.com/37003623/docs/1398b7-57978/1398b7-133878"
  CLICKUP_API_TOKEN=xxx node scripts/clickup-doc-to-md.mjs "https://app.clickup.com/37003623/docs/1398b7-57978" "./exports/doc.md"
  CLICKUP_API_TOKEN=xxx node scripts/clickup-doc-to-md.mjs "https://app.clickup.com/.../docs/a/b" "https://app.clickup.com/.../docs/c/d"
  CLICKUP_API_TOKEN=xxx node scripts/clickup-doc-to-md.mjs --input ./clickup-links.txt --out-dir ./exports/clickup
`);
}

function fail(message, error) {
  console.error(message);
  if (error) {
    console.error(error instanceof Error ? error.message : String(error));
  }
  process.exit(1);
}

function sanitizeFileName(value) {
  return value
    .trim()
    .replace(/[<>:"/\\|?*\u0000-\u001f]/g, '-')
    .replace(/\s+/g, ' ')
    .slice(0, 120) || 'clickup-export';
}

function ensureMarkdownExtension(filePath) {
  return filePath.toLowerCase().endsWith('.md') ? filePath : `${filePath}.md`;
}

async function loadDotEnvIfPresent(filePath = '.env') {
  try {
    const raw = await readFile(path.resolve(filePath), 'utf8');

    for (const line of raw.split(/\r?\n/)) {
      const trimmed = line.trim();

      if (!trimmed || trimmed.startsWith('#') || !trimmed.includes('=')) {
        continue;
      }

      const [key, ...rest] = trimmed.split('=');
      const value = rest.join('=').trim().replace(/^['"]|['"]$/g, '');

      if (key && !(key in process.env)) {
        process.env[key.trim()] = value;
      }
    }
  } catch (error) {
    if (error && typeof error === 'object' && 'code' in error && error.code === 'ENOENT') {
      return;
    }

    throw error;
  }
}

function parseClickUpDocUrl(rawUrl) {
  const url = new URL(rawUrl);
  const patterns = [
    /^\/(\d+)\/docs\/([^/]+)(?:\/([^/?#]+))?/,
    /^\/(\d+)\/v\/dc\/([^/]+)(?:\/([^/?#]+))?/,
  ];
  const match = patterns.map((pattern) => url.pathname.match(pattern)).find(Boolean);

  if (!match) {
    throw new Error(
      '지원하는 ClickUp Doc 링크 형식이 아닙니다. 예: https://app.clickup.com/<workspace_id>/docs/<doc_id>/<page_id> 또는 https://app.clickup.com/<workspace_id>/v/dc/<doc_id>/<page_id>'
    );
  }

  return {
    workspaceId: match[1],
    docId: decodeURIComponent(match[2]),
    pageId: match[3] ? decodeURIComponent(match[3]) : null,
  };
}

function parseCliArgs(args) {
  const urls = [];
  let outputPath = null;
  let outDir = './exports';
  let inputPath = null;

  for (let index = 0; index < args.length; index += 1) {
    const arg = args[index];

    if (arg === '--help' || arg === '-h') {
      return { help: true };
    }

    if (arg === '--input') {
      if (!args[index + 1] || args[index + 1].startsWith('--')) {
        throw new Error('--input 다음에 파일 경로가 필요합니다.');
      }
      inputPath = args[index + 1];
      index += 1;
      continue;
    }

    if (arg === '--out-dir') {
      if (!args[index + 1] || args[index + 1].startsWith('--')) {
        throw new Error('--out-dir 다음에 디렉터리 경로가 필요합니다.');
      }
      outDir = args[index + 1];
      index += 1;
      continue;
    }

    if (arg === '--output') {
      if (!args[index + 1] || args[index + 1].startsWith('--')) {
        throw new Error('--output 다음에 파일 경로가 필요합니다.');
      }
      outputPath = args[index + 1];
      index += 1;
      continue;
    }

    urls.push(arg);
  }

  return {
    help: false,
    urls,
    outputPath,
    outDir,
    inputPath,
  };
}

async function loadUrlsFromFile(filePath) {
  const raw = await readFile(path.resolve(filePath), 'utf8');

  return raw
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter((line) => line && !line.startsWith('#'));
}

async function apiGet(endpoint, token) {
  const response = await fetch(`${API_BASE}${endpoint}`, {
    headers: {
      Authorization: token,
      Accept: 'application/json',
    },
  });

  if (!response.ok) {
    const body = await response.text();
    throw new Error(`ClickUp API ${response.status} ${response.statusText}\n${body}`);
  }

  return response.json();
}

function pickFirstString(candidates) {
  for (const value of candidates) {
    if (typeof value === 'string' && value.trim()) {
      return value;
    }
  }
  return null;
}

function extractTitle(payload) {
  if (!payload || typeof payload !== 'object') {
    return null;
  }

  return pickFirstString([
    payload.title,
    payload.name,
    payload.page_title,
    payload.page?.title,
    payload.page?.name,
    payload.data?.title,
    payload.data?.name,
  ]);
}

function extractMarkdown(payload) {
  if (!payload || typeof payload !== 'object') {
    return null;
  }

  const direct = pickFirstString([
    payload.markdown_content,
    payload.content_markdown,
    payload.content,
    payload.body,
    payload.text_content,
    payload.page?.markdown_content,
    payload.page?.content_markdown,
    payload.page?.content,
    payload.page?.body,
    payload.data?.markdown_content,
    payload.data?.content_markdown,
    payload.data?.content,
    payload.data?.body,
  ]);

  if (direct) {
    return direct;
  }

  const visited = new Set();

  function walk(value) {
    if (!value || typeof value !== 'object' || visited.has(value)) {
      return null;
    }

    visited.add(value);

    if (Array.isArray(value)) {
      for (const item of value) {
        const found = walk(item);
        if (found) {
          return found;
        }
      }
      return null;
    }

    for (const [key, child] of Object.entries(value)) {
      if (
        /markdown|content|body|text/i.test(key) &&
        typeof child === 'string' &&
        child.trim()
      ) {
        return child;
      }
    }

    for (const child of Object.values(value)) {
      const found = walk(child);
      if (found) {
        return found;
      }
    }

    return null;
  }

  return walk(payload);
}

function collectPageNodes(tree) {
  const pages = [];
  const seen = new Set();

  function walk(value, depth) {
    if (!value || typeof value !== 'object') {
      return;
    }

    if (Array.isArray(value)) {
      for (const item of value) {
        walk(item, depth);
      }
      return;
    }

    const pageId = pickFirstString([value.page_id, value.pageId, value.id]);
    const title = pickFirstString([value.title, value.name]);

    if (pageId && title && !seen.has(pageId)) {
      seen.add(pageId);
      pages.push({ id: pageId, title, depth });
    }

    for (const [key, child] of Object.entries(value)) {
      const nextDepth = /children|child|subpages|pages|items/i.test(key) ? depth + 1 : depth;
      walk(child, nextDepth);
    }
  }

  walk(tree, 0);
  return pages;
}

function findPageSubtree(tree, targetPageId) {
  function walk(value) {
    if (!value || typeof value !== 'object') {
      return null;
    }

    if (Array.isArray(value)) {
      for (const item of value) {
        const found = walk(item);
        if (found) {
          return found;
        }
      }
      return null;
    }

    const pageId = pickFirstString([value.page_id, value.pageId, value.id]);
    if (pageId === targetPageId) {
      return value;
    }

    for (const child of Object.values(value)) {
      const found = walk(child);
      if (found) {
        return found;
      }
    }

    return null;
  }

  return walk(tree);
}

function buildSectionHeading(title, depth) {
  const level = Math.max(1, Math.min(depth + 1, 6));
  return `${'#'.repeat(level)} ${title}`;
}

async function writeMarkdown(outputPath, markdown) {
  const fullPath = path.resolve(ensureMarkdownExtension(outputPath));
  await mkdir(path.dirname(fullPath), { recursive: true });
  await writeFile(fullPath, markdown, 'utf8');
  return fullPath;
}

async function buildMarkdownSections({ workspaceId, docId, token, pages }) {
  const parts = [];

  for (const page of pages) {
    const pageDetail = await apiGet(
      `/workspaces/${workspaceId}/docs/${docId}/pages/${page.id}`,
      token
    );
    const pageTitle = extractTitle(pageDetail) || page.title || `Page ${page.id}`;
    const markdown = extractMarkdown(pageDetail);

    if (!markdown) {
      continue;
    }

    parts.push(buildSectionHeading(pageTitle, page.depth));
    parts.push('');
    parts.push(markdown.trim());
    parts.push('');
  }

  return parts;
}

async function exportPageTree({ workspaceId, docId, pageId, token, outputPath, outDir, sourceUrl }) {
  const [pageDetail, pageListing] = await Promise.all([
    apiGet(`/workspaces/${workspaceId}/docs/${docId}/pages/${pageId}`, token),
    apiGet(`/workspaces/${workspaceId}/docs/${docId}/page_listing`, token),
  ]);

  const subtree = findPageSubtree(pageListing, pageId);
  const childPages = subtree ? collectPageNodes(subtree) : [];
  const rootTitle = extractTitle(pageDetail) || `clickup-page-${pageId}`;
  const rootMarkdown = extractMarkdown(pageDetail);

  if (!rootMarkdown && childPages.length === 0) {
    throw new Error('페이지 본문과 하위 페이지를 찾지 못했습니다. 응답 스키마를 확인해 주세요.');
  }

  const dedupedChildPages = childPages.filter((page) => page.id !== pageId);
  const childParts = await buildMarkdownSections({
    workspaceId,
    docId,
    token,
    pages: dedupedChildPages,
  });

  const content = [
    `# ${rootTitle}`,
    '',
    `Source: ${sourceUrl}`,
    '',
  ];

  if (rootMarkdown) {
    content.push(rootMarkdown.trim());
    content.push('');
  }

  content.push(...childParts);

  const finalOutput = outputPath || buildDefaultOutputPath(outDir, rootTitle);
  const savedPath = await writeMarkdown(finalOutput, content.join('\n'));
  return { savedPath, title: rootTitle };
}

async function exportWholeDoc({ workspaceId, docId, token, outputPath, outDir, sourceUrl }) {
  const [doc, pageListing] = await Promise.all([
    apiGet(`/workspaces/${workspaceId}/docs/${docId}`, token),
    apiGet(`/workspaces/${workspaceId}/docs/${docId}/page_listing`, token),
  ]);

  let pages = collectPageNodes(pageListing);

  if (pages.length === 0) {
    const fallbackPages = await apiGet(`/workspaces/${workspaceId}/docs/${docId}/pages`, token);
    pages = collectPageNodes(fallbackPages);
  }

  if (pages.length === 0) {
    throw new Error('문서 페이지 목록을 찾지 못했습니다.');
  }

  const parts = [];
  const docTitle = extractTitle(doc) || `clickup-doc-${docId}`;

  parts.push(`# ${docTitle}`);
  parts.push('');
  parts.push(`Source: ${sourceUrl}`);
  parts.push('');
  parts.push(
    ...(await buildMarkdownSections({
      workspaceId,
      docId,
      token,
      pages,
    }))
  );

  const finalOutput = outputPath || buildDefaultOutputPath(outDir, docTitle);
  const savedPath = await writeMarkdown(finalOutput, parts.join('\n'));
  return { savedPath, title: docTitle };
}

function buildDefaultOutputPath(outDir, title) {
  return path.join(outDir, `${sanitizeFileName(title)}.md`);
}

async function exportOne(rawUrl, { token, outputPath, outDir }) {
  const ids = parseClickUpDocUrl(rawUrl);

  if (ids.pageId) {
    return exportPageTree({
      ...ids,
      token,
      outputPath,
      outDir,
      sourceUrl: rawUrl,
    });
  }

  return exportWholeDoc({
    ...ids,
    token,
    outputPath,
    outDir,
    sourceUrl: rawUrl,
  });
}

async function main() {
  const [, , ...args] = process.argv;
  const parsedArgs = parseCliArgs(args);

  if (args.length === 0 || parsedArgs.help) {
    printUsage();
    process.exit(args.length === 0 ? 1 : 0);
  }

  await loadDotEnvIfPresent();
  const token =
    process.env.CLICKUP_API_TOKEN ||
    process.env.CLICKUP_API_KEY ||
    process.env.ClickUP_API_KEY;

  if (!token) {
    fail('환경 변수 CLICKUP_API_TOKEN 또는 CLICKUP_API_KEY 가 필요합니다.');
  }

  const fileUrls = parsedArgs.inputPath ? await loadUrlsFromFile(parsedArgs.inputPath) : [];
  const urls = [...parsedArgs.urls, ...fileUrls];

  if (urls.length === 0) {
    fail('변환할 ClickUp Doc URL 이 없습니다.');
  }

  if (urls.length > 1 && parsedArgs.outputPath) {
    fail('여러 링크를 일괄 변환할 때는 단일 output 파일을 지정할 수 없습니다. --out-dir 을 사용해 주세요.');
  }

  const results = [];

  for (const rawUrl of urls) {
    const result = await exportOne(rawUrl, {
      token,
      outputPath: parsedArgs.outputPath,
      outDir: parsedArgs.outDir,
    });

    results.push({ url: rawUrl, ...result });
    console.log(`Saved "${result.title}" -> ${result.savedPath}`);
  }

  if (results.length > 1) {
    console.log(`Completed ${results.length} exports.`);
  }
}

main().catch((error) => fail('ClickUp Doc Markdown export failed.', error));
