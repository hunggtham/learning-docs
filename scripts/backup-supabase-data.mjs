import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';

const baseUrl = String(process.env.SUPABASE_URL || '').replace(/\/$/, '');
const secretKey = process.env.SUPABASE_SECRET_KEY || '';
const outputPath = process.env.BACKUP_OUTPUT || path.resolve('supabase-backup.json');
const pageSize = Math.min(Math.max(Number(process.env.SUPABASE_BACKUP_PAGE_SIZE) || 500, 1), 1000);
const tables = (process.env.SUPABASE_BACKUP_TABLES || 'learning_progress,tasks,goals,public_shares,english_task_progress')
  .split(',')
  .map(value => value.trim())
  .filter(Boolean);

if (!baseUrl) throw new Error('SUPABASE_URL is required.');
if (!secretKey) throw new Error('SUPABASE_SECRET_KEY is required. Use a GitHub Actions secret, never the anon key.');
if (!tables.length) throw new Error('SUPABASE_BACKUP_TABLES must contain at least one table.');
if (tables.some(table => !/^[a-z_][a-z0-9_]*$/i.test(table))) throw new Error('Invalid table name in SUPABASE_BACKUP_TABLES.');

async function fetchTable(table) {
  const rows = [];
  for (let offset = 0; ; offset += pageSize) {
    const url = new URL(`${baseUrl}/rest/v1/${table}`);
    url.searchParams.set('select', '*');
    url.searchParams.set('limit', String(pageSize));
    url.searchParams.set('offset', String(offset));
    const response = await fetch(url, {
      headers: {
        apikey: secretKey,
        Authorization: `Bearer ${secretKey}`,
        Accept: 'application/json',
      },
    });
    if (!response.ok) {
      const detail = (await response.text()).slice(0, 300);
      throw new Error(`${table}: Supabase returned HTTP ${response.status}: ${detail}`);
    }
    const page = await response.json();
    if (!Array.isArray(page)) throw new Error(`${table}: expected a JSON array from PostgREST.`);
    rows.push(...page);
    if (page.length < pageSize) break;
  }
  return rows;
}

const result = {};
for (const table of tables) {
  const rows = await fetchTable(table);
  result[table] = { row_count: rows.length, rows };
  console.log(`${table}: ${rows.length} rows`);
}

const backup = {
  format: 'supabase-public-data-backup',
  schema_version: 1,
  generated_at: new Date().toISOString(),
  project_url: baseUrl,
  tables: result,
};

await mkdir(path.dirname(outputPath), { recursive: true });
await writeFile(outputPath, `${JSON.stringify(backup, null, 2)}\n`, 'utf8');
console.log(`Backup written to ${outputPath}`);
