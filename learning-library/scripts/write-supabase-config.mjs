import { writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const siteRoot = path.resolve(scriptDirectory, '../site');
const studyPlannerProjectUrl = 'https://suvknhgjcgeudjqmgzwt.supabase.co';
const url = process.env.VITE_SUPABASE_URL || process.env.SUPABASE_URL || studyPlannerProjectUrl;
const anonKey = process.env.VITE_SUPABASE_ANON_KEY || process.env.SUPABASE_ANON_KEY || '';

await writeFile(
  path.join(siteRoot, 'supabase-config.js'),
  `window.__LEARNING_SUPABASE_CONFIG__ = ${JSON.stringify({ url, anonKey })};\n`,
  'utf8'
);

console.log(anonKey ? 'Study Planner Supabase client config generated.' : 'Study Planner Supabase project selected; anon key missing, so Study Shelf will run local-only.');
