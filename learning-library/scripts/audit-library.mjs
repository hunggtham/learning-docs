import { readFile, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
export const projectRoot = path.resolve(scriptDirectory, '..');
export const contentRoot = path.resolve(projectRoot, '..');
export const configPath = path.join(projectRoot, 'library.config.json');

// These directories normally contain source captures, OCR output, or imported
// material. They are never safe publication defaults, even when a file is
// accidentally added to the manifest.
const blockedSegments = new Set([
  'raw',
  'raw_md',
  'input',
  'notion',
  'generated_markdown',
  'generated_markdown_translated',
  'workflow-output'
]);

const blockedContentPatterns = [
  /all rights reserved/i,
  /copyright\s*(?:©|\(c\)|\d{4})/i,
  /no part of this book may be reproduced/i,
  /nguồn\s+bám\s+sát\s*:.*(?:pdf|sách|book)/i,
  /source\s*:\s*(?:pdf|book)/i
];

export async function loadConfig() {
  const config = JSON.parse(await readFile(configPath, 'utf8'));
  if (!Array.isArray(config.allowedDocuments)) {
    throw new Error('library.config.json: allowedDocuments must be an array');
  }
  return config;
}

export function normalizeEntry(entry) {
  if (typeof entry === 'string') return { path: entry };
  if (entry && typeof entry.path === 'string') return entry;
  return null;
}

function pathProblem(relativePath) {
  const segments = relativePath.split('/');
  if (segments.some(segment => blockedSegments.has(segment.toLowerCase()))) {
    return 'path nằm trong thư mục raw/imported bị chặn';
  }
  if (/(?:murphy|collins|cambridge|feuerstein|meri[_ -]?williams|22000[_ -]?tu[_ -]?vung)/i.test(relativePath)) {
    return 'tên file khớp nguồn sách/giáo trình đã nhập';
  }
  return null;
}

export async function auditEntries(config) {
  const errors = [];
  const warnings = [];
  const seen = new Set();

  for (const rawEntry of config.allowedDocuments) {
    const entry = normalizeEntry(rawEntry);
    if (!entry) {
      errors.push('mỗi mục allowedDocuments phải là chuỗi path hoặc object có field path');
      continue;
    }

    if (!['author-confirmed', 'permission-confirmed', 'open-license'].includes(entry.rights)) {
      errors.push(`${entry.path || '(missing path)'}: rights phải là author-confirmed, permission-confirmed hoặc open-license`);
    }

    const relativePath = entry.path.replaceAll('\\', '/');
    if (seen.has(relativePath)) {
      errors.push(`${relativePath}: bị khai báo trùng`);
      continue;
    }
    seen.add(relativePath);

    if (relativePath.startsWith('/') || relativePath.includes('..')) {
      errors.push(`${relativePath}: path phải tương đối và không được chứa ..`);
      continue;
    }
    if (!/\.(md|pdf)$/i.test(relativePath)) {
      errors.push(`${relativePath}: chỉ cho phép .md hoặc .pdf`);
      continue;
    }
    const blockedReason = pathProblem(relativePath);
    if (blockedReason) {
      errors.push(`${relativePath}: ${blockedReason}`);
      continue;
    }

    const absolutePath = path.resolve(contentRoot, relativePath);
    if (!absolutePath.startsWith(`${contentRoot}${path.sep}`)) {
      errors.push(`${relativePath}: path thoát khỏi content root`);
      continue;
    }
    try {
      const info = await stat(absolutePath);
      if (!info.isFile()) errors.push(`${relativePath}: không phải file`);
      if (info.size === 0) warnings.push(`${relativePath}: file rỗng`);
      if (/\.md$/i.test(relativePath)) {
        const content = await readFile(absolutePath, 'utf8');
        for (const pattern of blockedContentPatterns) {
          if (pattern.test(content)) {
            errors.push(`${relativePath}: nội dung khớp mẫu bản quyền (${pattern})`);
            break;
          }
        }
      }
    } catch {
      errors.push(`${relativePath}: file không tồn tại`);
    }
  }

  return { errors, warnings, count: seen.size };
}

export async function runAudit({ quiet = false } = {}) {
  const config = await loadConfig();
  const result = await auditEntries(config);
  if (!quiet) {
    for (const warning of result.warnings) console.warn(`WARN ${warning}`);
    for (const error of result.errors) console.error(`ERROR ${error}`);
    console.log(`Audited ${result.count} allow-listed documents.`);
  }
  if (result.errors.length) {
    throw new Error(`Publication audit failed with ${result.errors.length} error(s).`);
  }
  return { config, ...result };
}

if (process.argv[1] && path.resolve(process.argv[1]) === path.resolve(fileURLToPath(import.meta.url))) {
  try {
    await runAudit();
  } catch (error) {
    console.error(error.message);
    process.exitCode = 1;
  }
}
