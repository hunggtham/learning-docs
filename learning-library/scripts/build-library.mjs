import { cp, mkdir, readFile, readdir, rm, stat, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const projectRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const contentRoot = path.resolve(projectRoot, '..');
const outRoot = path.join(projectRoot, 'site/library');
const config = JSON.parse(await readFile(path.join(projectRoot, 'library.config.json'), 'utf8'));
const allowedDocuments = new Set(config.allowedDocuments);
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
      if (!allowedDocuments.has(relative)) continue;
      const info = await stat(absolute);
      documents.push({ path: relative, title: path.basename(entry.name, path.extname(entry.name)), type: path.extname(entry.name).toLowerCase() === '.pdf' ? 'PDF' : 'MD', category: relative.split('/')[0], size: info.size });
      const destination = path.join(outRoot, 'files', relative);
      await mkdir(path.dirname(destination), { recursive: true }); await cp(absolute, destination);
    }
  }
}
await rm(outRoot, { recursive: true, force: true }); await mkdir(outRoot, { recursive: true }); await walk(contentRoot);
documents.sort((a, b) => a.category.localeCompare(b.category) || a.title.localeCompare(b.title));
await writeFile(path.join(outRoot, 'library.json'), JSON.stringify({ generatedAt: new Date().toISOString(), documents }, null, 2));
console.log(`Built library with ${documents.length} documents.`);
