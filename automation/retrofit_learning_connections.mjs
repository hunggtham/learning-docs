#!/usr/bin/env node

/**
 * Add a small, topic-aware connection layer to authored learning Markdown that
 * has no visible hand-off between sections.  This is intentionally conservative:
 * raw/imported/generated captures and files already modified by the user are
 * left untouched.  Run from the repository root with --write to apply changes.
 */

import { readFile, readdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const ROOT = process.cwd();
const EXCLUDED_SEGMENTS = new Set([
  '.git',
  'node_modules',
  'raw',
  'raw_md',
  'input',
  'notion',
  'generated_markdown',
  'generated_markdown_translated',
  'workflow-output',
  'output',
  'site'
]);
const EXCLUDED_TOP_LEVEL = new Set(['automation', 'learning-library', 'planner', 'prompt', 'supabase']);
const CONNECTION_RE = /mạch\s*(?:đọc|nối|học)|liên\s*kết|kết\s*nối|tiếp\s*(?:theo|nối)|dựa\s*trên|trước\s*đó|đọc\s*thêm|prerequisite|related|connection|next|previous|builds\s+on|extends/i;
const HEADING_RE = /^(#{1,6})\s+(.+?)\s*$/;
const LINK_RE = /\[[^\]]+\]\(([^)]+)\)/g;

function normalize(value) {
  return value.replaceAll('\\', '/');
}

function cleanHeading(value) {
  return value
    .replace(/[*_`~]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

function isExcluded(relativePath) {
  const parts = normalize(relativePath).split('/');
  return parts.some(part => EXCLUDED_SEGMENTS.has(part.toLowerCase()))
    || EXCLUDED_TOP_LEVEL.has(parts[0]);
}

async function walk(directory, result = []) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const absolute = path.join(directory, entry.name);
    const relative = normalize(path.relative(ROOT, absolute));
    if (EXCLUDED_SEGMENTS.has(entry.name.toLowerCase()) || EXCLUDED_TOP_LEVEL.has(relative.split('/')[0])) continue;
    if (entry.isDirectory()) await walk(absolute, result);
    else if (entry.isFile() && entry.name.toLowerCase().endsWith('.md') && !isExcluded(relative)) result.push(relative);
  }
  return result;
}

function dirtyPaths() {
  const output = execFileSync('git', ['status', '--short'], { cwd: ROOT, encoding: 'utf8' });
  return new Set(output.split('\n').flatMap(line => {
    if (!line.trim()) return [];
    const value = line.slice(3).trim();
    // Rename entries have two paths; protect both sides.
    return value.includes(' -> ') ? value.split(' -> ') : [value];
  }));
}

function extractHeadings(markdown) {
  const headings = [];
  let inFence = false;
  for (const line of markdown.split('\n')) {
    if (/^\s*```/.test(line)) {
      inFence = !inFence;
      continue;
    }
    if (inFence) continue;
    const match = line.match(HEADING_RE);
    if (match) headings.push({ level: match[1].length, text: cleanHeading(match[2]) });
  }
  return headings;
}

function markdownLinks(markdown) {
  return [...markdown.matchAll(LINK_RE)].map(match => match[1]);
}

function relativeLink(from, to) {
  const value = normalize(path.relative(path.dirname(from), to));
  return value.startsWith('.') ? value : `./${value}`;
}

function chooseContext(relativePath, filesByDirectory) {
  const directory = path.posix.dirname(relativePath);
  const siblings = (filesByDirectory.get(directory) || []).filter(file => file !== relativePath);
  const parentReadme = directory === '.' ? null : normalize(path.posix.join(directory, 'README.md'));
  const hasParentReadme = siblings.includes(parentReadme);
  const context = hasParentReadme ? parentReadme : siblings.find(file => path.posix.basename(file).toLowerCase() === 'readme.md') || null;
  const sibling = siblings.find(file => file !== context) || null;
  return { context, sibling };
}

function connectionIntro(relativePath, headings, context, sibling) {
  const title = headings.find(item => item.level === 1)?.text || path.posix.basename(relativePath, '.md');
  const sections = headings.filter(item => item.level >= 2).map(item => item.text);
  const first = sections[0] || title;
  const second = sections[1] || null;
  const contextText = context
    ? `Đặt **${title}** trong bản đồ [${cleanHeading(path.posix.basename(context, '.md'))}](${relativeLink(relativePath, context)}) để thấy owner và vị trí của nó.`
    : `Đọc **${title}** như một mắt xích của learning path hiện tại, không như một ghi chú tách rời.`;
  if (second) {
    return `> **Mạch đọc:** ${contextText} Nội dung đi từ **${first}** sang **${second}**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.`;
  }
  return `> **Mạch đọc:** ${contextText} Hãy xác định đối tượng và câu hỏi trung tâm trước, rồi dùng phần này để đối chiếu với mục liên quan sau khi đã nắm mental model chính.`;
}

function transitionLine(previous, current, next) {
  const nextText = next ? `; từ đó chuyển sang **${next}** để kiểm tra hệ quả hoặc cách dùng` : ' và dùng kết quả đó để khép lại mạch giải thích';
  return `> **Chuyển mạch:** Từ **${previous}**, ta sang **${current}** để mở rộng cùng câu hỏi${nextText}.`;
}

function connectionFooter(relativePath, headings, context, sibling) {
  const sections = headings.filter(item => item.level >= 2).map(item => item.text);
  const last = sections.at(-1) || headings.find(item => item.level === 1)?.text || path.posix.basename(relativePath, '.md');
  const siblingText = sibling
    ? ` Có thể đọc tiếp [${cleanHeading(path.posix.basename(sibling, '.md'))}](${relativeLink(relativePath, sibling)}) để đối chiếu boundary gần nhất.`
    : context
      ? ` Quay lại [${cleanHeading(path.posix.basename(context, '.md'))}](${relativeLink(relativePath, context)}) khi cần định vị lại prerequisite hoặc owner.`
      : '';
  return `> **Bàn giao:** Sau **${last}**, hãy chốt invariant và giới hạn của mục này trước khi nối sang kiến thức kế tiếp.${siblingText}`;
}

function retrofit(relativePath, markdown, context, sibling) {
  if (CONNECTION_RE.test(markdown)) return null;
  const headings = extractHeadings(markdown);
  if (!headings.length) return null;
  const lines = markdown.replace(/\s+$/, '').split('\n');
  const h1Index = lines.findIndex(line => /^#\s+/.test(line));
  const intro = connectionIntro(relativePath, headings, context, sibling);
  let result = lines;
  if (h1Index >= 0) {
    result = [...lines.slice(0, h1Index + 1), '', intro, '', ...lines.slice(h1Index + 1)];
  } else {
    result = [intro, '', ...lines];
  }

  const topSections = headings.filter(item => item.level === 2);
  if (topSections.length >= 2 && topSections.length <= 12) {
    // Add a short, heading-aware bridge before each top-level section after the first.
    // Work from the end so original line indexes remain valid.
    const sectionIndexes = [];
    let inFence = false;
    for (let index = 0; index < result.length; index += 1) {
      if (/^\s*```/.test(result[index])) inFence = !inFence;
      if (!inFence && /^##\s+/.test(result[index])) sectionIndexes.push(index);
    }
    for (let index = sectionIndexes.length - 1; index >= 1; index -= 1) {
      const previous = cleanHeading(result[sectionIndexes[index - 1]].replace(/^##\s+/, ''));
      const current = cleanHeading(result[sectionIndexes[index]].replace(/^##\s+/, ''));
      const next = index + 1 < sectionIndexes.length
        ? cleanHeading(result[sectionIndexes[index + 1]].replace(/^##\s+/, ''))
        : null;
      result.splice(sectionIndexes[index], 0, '', transitionLine(previous, current, next), '');
    }
  }

  result.push('', connectionFooter(relativePath, headings, context, sibling), '');
  return result.join('\n');
}

const writeMode = process.argv.includes('--write');
const files = await walk(ROOT);
const dirty = dirtyPaths();
const filesByDirectory = new Map();
for (const file of files) {
  const directory = path.posix.dirname(file);
  if (!filesByDirectory.has(directory)) filesByDirectory.set(directory, []);
  filesByDirectory.get(directory).push(file);
}
for (const group of filesByDirectory.values()) group.sort();

let candidates = 0;
let changed = 0;
let skippedDirty = 0;
for (const relativePath of files.sort()) {
  if (dirty.has(relativePath)) {
    skippedDirty += 1;
    continue;
  }
  const source = await readFile(path.join(ROOT, relativePath), 'utf8');
  if (CONNECTION_RE.test(source)) continue;
  candidates += 1;
  const { context, sibling } = chooseContext(relativePath, filesByDirectory);
  const updated = retrofit(relativePath, source, context, sibling);
  if (!updated || updated === source) continue;
  changed += 1;
  if (writeMode) await writeFile(path.join(ROOT, relativePath), updated, 'utf8');
  else console.log(relativePath);
}

console.log(`${writeMode ? 'Retrofitted' : 'Would retrofit'} ${changed} file(s); ${candidates} candidate(s), skipped ${skippedDirty} dirty file(s).`);
