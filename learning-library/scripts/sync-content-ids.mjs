import { createHash } from 'node:crypto';
import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';

const exec = promisify(execFile);
const projectRoot = path.resolve(new URL('..', import.meta.url).pathname);
const registryPath = path.join(projectRoot, 'content-ids.json');
const cataloguePath = path.join(projectRoot, 'site/library/library.json');

function deriveContentId(doc) {
  const base = `my-learning-registry\u001f${doc.path.normalize('NFC')}`;
  return `doc_${createHash('sha256').update(base).digest('hex').slice(0, 40)}`;
}

async function renameMap() {
  try {
    const { stdout } = await exec('git', ['diff', '--name-status', '--find-renames=50%', 'HEAD', '--']);
    const map = new Map();
    for (const line of stdout.split('\n')) {
      const match = line.match(/^R\d+\s+(.+)\s+(.+)$/);
      if (match) map.set(match[2], match[1]);
    }
    return map;
  } catch {
    return new Map();
  }
}

const catalogue = JSON.parse(await readFile(cataloguePath, 'utf8'));
let registry = { version: 1, documents: [] };
try { registry = JSON.parse(await readFile(registryPath, 'utf8')); } catch {}
const entries = Array.isArray(registry.documents) ? registry.documents : [];
const byPath = new Map(entries.filter(entry => entry?.path).map(entry => [entry.path, entry]));
const byAlias = new Map(entries.flatMap(entry => (Array.isArray(entry?.aliases) ? entry.aliases : []).map(alias => [alias, entry])));
const byContentId = new Map(entries.filter(entry => entry?.contentId).map(entry => [entry.contentId, entry]));
const byRevision = new Map(entries.filter(entry => entry?.revision).map(entry => [entry.revision, entry]));
const renames = await renameMap();
const used = new Set();
const next = [];

for (const doc of catalogue.documents || []) {
  const oldPath = renames.get(doc.path);
  const entry = byPath.get(doc.path) || byAlias.get(doc.path) || byContentId.get(doc.contentId) || byRevision.get(doc.contentRevision) || (oldPath ? byPath.get(oldPath) || byAlias.get(oldPath) : null);
  const current = entry || { contentId: doc.contentId || deriveContentId(doc), aliases: [] };
  const aliases = [...new Set([
    ...(Array.isArray(current.aliases) ? current.aliases : []),
    current.path && current.path !== doc.path ? current.path : null,
    oldPath && oldPath !== doc.path ? oldPath : null,
    ...(Array.isArray(doc.contentAliases) ? doc.contentAliases : [])
  ].filter(alias => typeof alias === 'string' && alias !== doc.path))];
  next.push({ path: doc.path, contentId: current.contentId, revision: doc.contentRevision, aliases });
  used.add(current.contentId);
}

for (const entry of entries) {
  if (entry?.contentId && !used.has(entry.contentId)) next.push(entry);
}

next.sort((a, b) => a.path.localeCompare(b.path));
await writeFile(registryPath, `${JSON.stringify({ version: 1, documents: next }, null, 2)}\n`, 'utf8');
console.log(`Synced ${next.length} stable content IDs (${(catalogue.documents || []).length} current documents).`);
