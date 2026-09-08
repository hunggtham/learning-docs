import { cp, mkdir, readdir, rm, stat, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { auditEntries, contentRoot, loadConfig, normalizeEntry, projectRoot } from './audit-library.mjs';

const outRoot = path.join(projectRoot, 'site/library');
const config = await loadConfig();
const audit = await auditEntries(config);
if (audit.errors.length) {
  for (const error of audit.errors) console.error(`ERROR ${error}`);
  throw new Error(`Publication audit failed with ${audit.errors.length} error(s).`);
}
const allowedDocuments = new Map(config.allowedDocuments.map(normalizeEntry).filter(Boolean).map(entry => [entry.path.replaceAll('\\', '/'), entry]));
const excluded = new Set(['.git', 'node_modules', '.DS_Store', 'dist', 'learning-library']);
const allowed = new Set(['.md', '.pdf']);
const documents = [];

async function walk(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    if (excluded.has(entry.name)) continue;
    const absolute = path.join(directory, entry.name);
    if (entry.isDirectory()) await walk(absolute);
    else if (allowed.has(path.extname(entry.name).toLowerCase())) {
      const relative = path.relative(contentRoot, absolute).split(path.sep).join('/');
      const manifestEntry = allowedDocuments.get(relative);
      if (!manifestEntry) continue;
      const info = await stat(absolute);
      documents.push({
        path: relative,
        title: manifestEntry.title || path.basename(entry.name, path.extname(entry.name)),
        type: path.extname(entry.name).toLowerCase() === '.pdf' ? 'PDF' : 'MD',
        category: manifestEntry.category || relative.split('/')[0],
        language: manifestEntry.language || 'vi',
        rights: manifestEntry.rights || 'author-confirmed',
        size: info.size
      });
      const destination = path.join(outRoot, 'files', relative);
      await mkdir(path.dirname(destination), { recursive: true }); await cp(absolute, destination);
    }
  }
}
await rm(outRoot, { recursive: true, force: true }); await mkdir(outRoot, { recursive: true }); await walk(contentRoot);
documents.sort((a, b) => a.category.localeCompare(b.category) || a.title.localeCompare(b.title));
await writeFile(path.join(outRoot, 'library.json'), JSON.stringify({ generatedAt: new Date().toISOString(), documents }, null, 2));
console.log(`Built library with ${documents.length} documents.`);
