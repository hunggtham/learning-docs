import { createHash } from 'node:crypto';
import { cp, mkdir, readFile, readdir, rm, stat, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { auditEntries, auditFile, contentRoot, loadConfig, normalizeEntry, projectRoot } from './audit-library.mjs';

const outRoot = path.join(projectRoot, 'site/library');
const config = await loadConfig();
const contentIdsPath = path.join(projectRoot, 'content-ids.json');
const audit = await auditEntries(config);
if (audit.errors.length) {
  for (const error of audit.errors) console.error(`ERROR ${error}`);
  throw new Error(`Publication audit failed with ${audit.errors.length} error(s).`);
}

const normalizePath = value => value.replaceAll('\\', '/').normalize('NFC');
const normalizeManifestEntry = entry => {
  const normalized = normalizeEntry(entry);
  return normalized ? { ...normalized, path: normalizePath(normalized.path) } : null;
};
const allowedDocuments = new Map(config.allowedDocuments.map(normalizeManifestEntry).filter(Boolean).map(entry => [entry.path, entry]));
const allowedPrefixes = (config.allowedPrefixes || []).map(normalizeManifestEntry).filter(Boolean);
let contentIds = { version: 1, documents: [] };
try {
  contentIds = JSON.parse(await readFile(contentIdsPath, 'utf8'));
} catch {}
const contentIdEntries = Array.isArray(contentIds.documents) ? contentIds.documents : [];
const contentIdByPath = new Map();
const contentIdByAlias = new Map();
for (const entry of contentIdEntries) {
  if (!entry || typeof entry.contentId !== 'string') continue;
  if (typeof entry.path === 'string') contentIdByPath.set(entry.path.replaceAll('\\', '/'), entry);
  for (const alias of Array.isArray(entry.aliases) ? entry.aliases : []) {
    if (typeof alias === 'string') contentIdByAlias.set(alias.replaceAll('\\', '/'), entry);
  }
}
const excluded = new Set(['.git', 'node_modules', '.DS_Store', 'dist', 'learning-library', ...(config.ignoredSegments || [])]);
const allowed = new Set(['.md', '.pdf']);
const documents = [];
const seen = new Set();
const markdownSources = new Map();

function normalizeNamespace(value) {
  return String(value || 'general').normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9가-힣]+/g, '-').replace(/^-+|-+$/g, '') || 'general';
}

function derivedContentId(document) {
  const base = `my-learning-registry\u001f${document.path.normalize('NFC')}`;
  return `doc_${createHash('sha256').update(base).digest('hex').slice(0, 40)}`;
}

function contentIdentity(relative, manifestEntry, title, type, category) {
  const registry = contentIdByPath.get(relative) || contentIdByAlias.get(relative);
  const contentId = manifestEntry?.contentId || registry?.contentId || derivedContentId({ path: relative, title, type, category, contentNamespace: manifestEntry?.contentNamespace, contentType: manifestEntry?.contentType });
  const aliases = [...new Set([
    ...(Array.isArray(manifestEntry?.contentAliases) ? manifestEntry.contentAliases : []),
    ...(Array.isArray(registry?.aliases) ? registry.aliases : []),
    registry?.path && registry.path !== relative ? registry.path : null
  ].filter(alias => typeof alias === 'string' && alias !== relative))];
  return { contentId, aliases };
}

function manifestFor(relative) {
  const explicit = allowedDocuments.get(relative);
  if (explicit) return explicit;
  return allowedPrefixes.find(entry => relative === entry.path || relative.startsWith(`${entry.path}/`));
}

function displayPath(relative, manifestEntry) {
  const displayPrefix = manifestEntry?.displayPrefix?.replace(/^\/+|\/+$/g, '');
  const sourcePrefix = manifestEntry?.path?.replace(/^\/+|\/+$/g, '');
  if (displayPrefix && sourcePrefix && (relative === sourcePrefix || relative.startsWith(`${sourcePrefix}/`))) {
    const suffix = relative.slice(sourcePrefix.length).replace(/^\/+/, '');
    return [displayPrefix, suffix].filter(Boolean).join('/');
  }
  return relative.split('/').filter(segment => segment.toLowerCase() !== 'output').join('/');
}

function localTargetPath(fromPath, rawTarget) {
  const target = rawTarget.trim().replace(/^<|>$/g, '');
  if (!target || /^(?:https?:|mailto:|tel:|data:|javascript:|#)/i.test(target)) return null;
  const withoutHash = decodeURIComponent(target.split('#')[0]).replaceAll('\\', '/');
  if (!withoutHash) return null;
  return withoutHash.startsWith('/')
    ? withoutHash.slice(1)
    : path.posix.normalize(path.posix.join(path.posix.dirname(fromPath), withoutHash));
}

function scrubUnpublishedLinks(markdown, fromPath, publishedPaths) {
  let removed = 0;
  const scrub = (match, label, target) => {
    const resolved = localTargetPath(fromPath, target);
    const cleanTarget = target.trim().replace(/^<|>$/g, '');
    const isDocument = /\.(?:md|pdf)(?:#.*)?$/i.test(cleanTarget);
    const isDirectory = cleanTarget.endsWith('/') || cleanTarget.includes('/');
    if (!resolved || (!isDocument && !isDirectory)) return match;
    if (publishedPaths.has(resolved)) return match;
    if (isDirectory) {
      const directoryTarget = cleanTarget.replace(/\/?(?:#.*)?$/, '/README.md');
      const directoryPath = localTargetPath(fromPath, directoryTarget);
      if (directoryPath && publishedPaths.has(directoryPath)) return match.replace(target, directoryTarget);
    }
    removed += 1;
    return label;
  };

  // Keep links to published documents and external URLs; flatten only local
  // Markdown/PDF links whose source is intentionally outside the publication.
  const inline = markdown.replace(/\[([^\]\n]+)\]\(([^)\n]+)\)/g, scrub);
  return { markdown: inline, removed };
}

function stripMarkdown(markdown) {
  return markdown
    .replace(/```[\s\S]*?```/g, ' ')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/!\[[^\]]*\]\([^)]*\)/g, ' ')
    .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
    .replace(/\[\[([^\]|]+)(?:\|[^\]]+)?\]\]/g, '$1')
    .replace(/^#{1,6}\s+/gm, '')
    .replace(/^>\s?/gm, '')
    .replace(/[*_~=-]{2,}/g, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function extractHeadings(markdown) {
  return [...markdown.matchAll(/^(#{1,3})\s+(.+)$/gm)].map(match => ({
    level: match[1].length,
    text: match[2].replace(/[*_`~]/g, '').trim()
  }));
}

async function walk(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    if (excluded.has(entry.name) || entry.name.toLowerCase() === 'raw' || entry.name.toLowerCase() === 'raw_md') continue;
    const absolute = path.join(directory, entry.name);
    if (entry.isDirectory()) await walk(absolute);
    else if (allowed.has(path.extname(entry.name).toLowerCase())) {
      const relative = normalizePath(path.relative(contentRoot, absolute));
      const manifestEntry = manifestFor(relative);
      if (!manifestEntry) continue;
      if (!allowedDocuments.has(relative) && path.extname(entry.name).toLowerCase() === '.pdf') continue;
      if (seen.has(relative)) continue;
      const fileAudit = await auditFile(relative, manifestEntry);
      if (fileAudit.errors.length) {
        for (const error of fileAudit.errors) console.error(`ERROR ${error}`);
        throw new Error(`Publication audit failed for ${relative}.`);
      }
      const info = await stat(absolute);
      const visiblePath = displayPath(relative, manifestEntry);
      const type = path.extname(entry.name).toLowerCase() === '.pdf' ? 'PDF' : 'MD';
      const category = manifestEntry.category || relative.split('/')[0];
      const title = manifestEntry.title || path.basename(entry.name, path.extname(entry.name));
      const identity = contentIdentity(relative, manifestEntry, title, type, category);
      documents.push({
        path: relative,
        displayPath: visiblePath,
        folder: path.posix.dirname(visiblePath) === '.' ? '' : path.posix.dirname(visiblePath),
        title,
        type,
        category,
        language: manifestEntry.language || 'vi',
        rights: manifestEntry.rights || 'author-confirmed',
        size: info.size,
        contentId: identity.contentId,
        contentAliases: identity.aliases,
        contentRevision: createHash('sha256').update(await readFile(absolute)).digest('hex')
      });
      if (type === 'MD') markdownSources.set(relative, await readFile(absolute, 'utf8'));
      seen.add(relative);
      const destination = path.join(outRoot, 'files', relative);
      await mkdir(path.dirname(destination), { recursive: true });
      await cp(absolute, destination);
    }
  }
}

await rm(outRoot, { recursive: true, force: true });
await mkdir(outRoot, { recursive: true });
await walk(contentRoot);
documents.sort((a, b) => a.displayPath.localeCompare(b.displayPath));

const folderSet = new Set();
for (const document of documents) {
  if (!document.folder) continue;
  const parts = document.folder.split('/');
  for (let index = 1; index <= parts.length; index += 1) folderSet.add(parts.slice(0, index).join('/'));
}
const folders = [...folderSet].sort();

const searchIndex = documents.map(document => {
  if (document.type !== 'MD') return { ...document, headings: [], text: '' };
  const source = markdownSources.get(document.path) || '';
  return {
    path: document.path,
    displayPath: document.displayPath,
    folder: document.folder,
    title: document.title,
    type: document.type,
    category: document.category,
    language: document.language,
    headings: extractHeadings(source),
    text: stripMarkdown(source).slice(0, 80000)
  };
});

const markdownDocuments = documents.filter(document => document.type === 'MD');
const pathSet = new Set(documents.map(document => document.path));

let scrubbedLinkCount = 0;
for (const [relative, source] of markdownSources) {
  const scrubbed = scrubUnpublishedLinks(source, relative, pathSet);
  scrubbedLinkCount += scrubbed.removed;
  markdownSources.set(relative, scrubbed.markdown);
  if (scrubbed.markdown !== source) {
    await writeFile(path.join(outRoot, 'files', relative), scrubbed.markdown);
    const document = documents.find(item => item.path === relative);
    if (document) document.contentRevision = createHash('sha256').update(scrubbed.markdown).digest('hex');
  }
}

const aliasMap = new Map();
for (const document of markdownDocuments) {
  const aliases = [
    document.title,
    path.posix.basename(document.path, '.md'),
    document.displayPath.replace(/\.md$/i, ''),
    document.path.replace(/\.md$/i, '')
  ];
  for (const alias of aliases) {
    const key = alias.toLowerCase().trim();
    if (key && !aliasMap.has(key)) aliasMap.set(key, document.path);
  }
}

function resolveLink(fromPath, rawTarget) {
  if (!rawTarget) return null;
  const target = rawTarget.trim().replace(/^<|>$/g, '');
  if (/^(https?:|mailto:|tel:|#)/i.test(target)) return null;
  const withoutHash = decodeURIComponent(target.split('#')[0]).replaceAll('\\', '/');
  if (!withoutHash) return null;
  if (/\.md$/i.test(withoutHash)) {
    const resolved = withoutHash.startsWith('/')
      ? withoutHash.slice(1)
      : path.posix.normalize(path.posix.join(path.posix.dirname(fromPath), withoutHash));
    if (pathSet.has(resolved)) return resolved;
  }
  const alias = withoutHash.replace(/\.md$/i, '').toLowerCase().trim();
  return aliasMap.get(alias) || null;
}

const edges = [];
const edgeKeys = new Set();
for (const document of markdownDocuments) {
  const source = markdownSources.get(document.path) || '';
  const rawTargets = [];
  for (const match of source.matchAll(/\[[^\]]+\]\(([^)]+)\)/g)) rawTargets.push(match[1]);
  for (const match of source.matchAll(/\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]/g)) rawTargets.push(match[1]);
  for (const rawTarget of rawTargets) {
    const target = resolveLink(document.path, rawTarget);
    if (!target || target === document.path) continue;
    const key = `${document.path}→${target}`;
    if (edgeKeys.has(key)) continue;
    edgeKeys.add(key);
    edges.push({ source: document.path, target });
  }
}

const graph = {
  generatedAt: new Date().toISOString(),
  nodes: markdownDocuments.map(document => ({
    path: document.path,
    title: document.title,
    category: document.category,
    folder: document.folder
  })),
  edges
};

const generatedAt = new Date().toISOString();
await writeFile(path.join(outRoot, 'library.json'), JSON.stringify({ generatedAt, folders, documents }, null, 2));
await writeFile(path.join(outRoot, 'search-index.json'), JSON.stringify({ generatedAt, documents: searchIndex }));
await writeFile(path.join(outRoot, 'graph.json'), JSON.stringify(graph));
console.log(`Built library with ${documents.length} documents, ${searchIndex.length} search entries and ${edges.length} knowledge links.`);
if (scrubbedLinkCount) console.log(`Publication boundary: flattened ${scrubbedLinkCount} links to withheld local files.`);
