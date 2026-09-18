import { cp, mkdir, readdir, rm, stat, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { auditEntries, auditFile, contentRoot, loadConfig, normalizeEntry, projectRoot } from './audit-library.mjs';

const outRoot = path.join(projectRoot, 'site/library');
const config = await loadConfig();
const audit = await auditEntries(config);
if (audit.errors.length) {
  for (const error of audit.errors) console.error(`ERROR ${error}`);
  throw new Error(`Publication audit failed with ${audit.errors.length} error(s).`);
}
const allowedDocuments = new Map(config.allowedDocuments.map(normalizeEntry).filter(Boolean).map(entry => [entry.path.replaceAll('\\', '/'), entry]));
const allowedPrefixes = (config.allowedPrefixes || []).map(normalizeEntry).filter(Boolean);
const excluded = new Set(['.git', 'node_modules', '.DS_Store', 'dist', 'learning-library', ...(config.ignoredSegments || [])]);
const allowed = new Set(['.md', '.pdf']);
const documents = [];
const seen = new Set();

function manifestFor(relative) {
  const explicit = allowedDocuments.get(relative);
  if (explicit) return explicit;
  return allowedPrefixes.find(entry => relative === entry.path || relative.startsWith(`${entry.path}/`));
}

function displayPath(relative) {
  return relative.split('/').filter(segment => segment.toLowerCase() !== 'output').join('/');
}

async function walk(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    if (excluded.has(entry.name) || entry.name.toLowerCase() === 'raw' || entry.name.toLowerCase() === 'raw_md') continue;
    const absolute = path.join(directory, entry.name);
    if (entry.isDirectory()) await walk(absolute);
    else if (allowed.has(path.extname(entry.name).toLowerCase())) {
      const relative = path.relative(contentRoot, absolute).split(path.sep).join('/');
      const manifestEntry = manifestFor(relative);
      if (!manifestEntry) continue;
      // PDFs stay opt-in per-file. This prevents a newly added local PDF from
      // becoming public merely because its parent Markdown folder is allowed.
      if (!allowedDocuments.has(relative) && path.extname(entry.name).toLowerCase() === '.pdf') continue;
      if (seen.has(relative)) continue;
      const fileAudit = await auditFile(relative, manifestEntry);
      if (fileAudit.errors.length) {
        for (const error of fileAudit.errors) console.error(`ERROR ${error}`);
        throw new Error(`Publication audit failed for ${relative}.`);
      }
      const info = await stat(absolute);
      const visiblePath = displayPath(relative);
      documents.push({
        path: relative,
        displayPath: visiblePath,
        folder: path.posix.dirname(visiblePath) === '.' ? '' : path.posix.dirname(visiblePath),
        title: manifestEntry.title || path.basename(entry.name, path.extname(entry.name)),
        type: path.extname(entry.name).toLowerCase() === '.pdf' ? 'PDF' : 'MD',
        category: manifestEntry.category || relative.split('/')[0],
        language: manifestEntry.language || 'vi',
        rights: manifestEntry.rights || 'author-confirmed',
        size: info.size
      });
      seen.add(relative);
      const destination = path.join(outRoot, 'files', relative);
      await mkdir(path.dirname(destination), { recursive: true }); await cp(absolute, destination);
    }
  }
}
await rm(outRoot, { recursive: true, force: true }); await mkdir(outRoot, { recursive: true }); await walk(contentRoot);
documents.sort((a, b) => a.displayPath.localeCompare(b.displayPath));
const folderSet = new Set();
for (const document of documents) {
  if (!document.folder) continue;
  const parts = document.folder.split('/');
  for (let index = 1; index <= parts.length; index += 1) folderSet.add(parts.slice(0, index).join('/'));
}
const folders = [...folderSet].sort();
await writeFile(path.join(outRoot, 'library.json'), JSON.stringify({ generatedAt: new Date().toISOString(), folders, documents }, null, 2));
console.log(`Built library with ${documents.length} documents.`);
