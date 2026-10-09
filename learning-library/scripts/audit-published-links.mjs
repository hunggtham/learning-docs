import { readdir, readFile, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const libraryRoot = path.resolve(scriptDirectory, '..', 'site', 'library');
const filesRoot = path.join(libraryRoot, 'files');
const inlineLinkPattern = /!?\[[^\]\n]*\]\((<[^>]+>|[^)\s]+)(?:\s+(?:"[^"]*"|'[^']*'|\([^)]*\)))?\)/g;
const externalPattern = /^(?:https?:|mailto:|tel:|data:|javascript:|#)/i;

async function markdownFiles(directory) {
  const files = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const absolute = path.join(directory, entry.name);
    if (entry.isDirectory()) files.push(...await markdownFiles(absolute));
    else if (/\.md$/i.test(entry.name)) files.push(absolute);
  }
  return files;
}

function resolveTarget(source, rawTarget) {
  const target = rawTarget.replace(/^<|>$/g, '').trim();
  if (!target || externalPattern.test(target)) return null;
  const withoutHash = decodeURIComponent(target.split('#')[0]).replaceAll('\\', '/');
  if (!withoutHash) return null;
  return path.normalize(path.resolve(path.dirname(source), withoutHash));
}

async function publishedTarget(resolved, rawTarget) {
  try {
    if ((await stat(resolved)).isFile()) return true;
    if (!(await stat(resolved)).isDirectory()) return false;
  } catch {
    return false;
  }
  for (const index of ['README.md', 'index.md']) {
    try {
      if ((await stat(path.join(resolved, index))).isFile()) return true;
    } catch {
      // Try the next conventional directory entrypoint.
    }
  }
  return false;
}

const errors = [];
const sources = await markdownFiles(filesRoot);
for (const source of sources) {
  const text = await readFile(source, 'utf8');
  for (const match of text.matchAll(inlineLinkPattern)) {
    const cleanTarget = match[1].replace(/^<|>$/g, '').trim();
    if (!/\.(?:md|pdf)(?:#.*)?$/i.test(cleanTarget) && !cleanTarget.includes('/')) continue;
    const resolved = resolveTarget(source, match[1]);
    if (!resolved) continue;
    if (!resolved.startsWith(`${filesRoot}${path.sep}`)) {
      errors.push(`${path.relative(libraryRoot, source)}: link escapes published files: ${match[1]}`);
      continue;
    }
    if (!(await publishedTarget(resolved, cleanTarget))) {
      errors.push(`${path.relative(libraryRoot, source)}: missing published target: ${match[1]}`);
    }
  }
}

if (errors.length) {
  for (const error of errors) console.error(`ERROR ${error}`);
  console.error(`Published link audit failed with ${errors.length} error(s).`);
  process.exitCode = 1;
} else {
  console.log(`Published link audit passed for ${sources.length} Markdown files.`);
}
