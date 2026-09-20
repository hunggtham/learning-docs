const app = document.querySelector('#app');
const state = { docs: [], query: '', filter: 'all', format: 'all', folder: '' };
let disposeReader = () => {};

const escapeHtml = value => String(value).replace(/[&<>'"]/g, char => ({ '&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;' })[char]);
const fileUrl = path => `./library/files/${path.split('/').map(encodeURIComponent).join('/')}`;
const titleOf = doc => doc.title || doc.path.split('/').pop().replace(/\.[^.]+$/, '');
const bookmarkKey = doc => `study-shelf-bookmark:${doc.path}`;
const memoryStorage = new Map();
let persistentStorage = true;

function storageGet(key) {
  try { return window.localStorage.getItem(key); }
  catch { persistentStorage = false; return memoryStorage.get(key) || null; }
}
function storageSet(key, value) {
  try { window.localStorage.setItem(key, value); return true; }
  catch { persistentStorage = false; memoryStorage.set(key, value); return false; }
}
function storageRemove(key) {
  try { window.localStorage.removeItem(key); }
  catch { persistentStorage = false; memoryStorage.delete(key); }
}
function bookmarkStatus(saved) {
  if (!saved) return persistentStorage ? 'Bookmark lưu trên trình duyệt này.' : 'Safari đang không cho lưu lâu dài; bookmark chỉ giữ trong phiên hiện tại.';
  return `${persistentStorage ? 'Đã lưu' : 'Đã lưu tạm trong phiên'} ${new Date(saved.savedAt).toLocaleString()}`;
}

function formatSize(bytes) { return bytes < 1024 * 1024 ? `${Math.ceil(bytes / 1024)} KB` : `${(bytes / 1024 / 1024).toFixed(1)} MB`; }
function folderLabel(folder) { return folder ? `📁 ${folder}` : 'Tất cả thư mục'; }
function folderCount(folder) { return state.docs.filter(doc => !folder || doc.folder === folder || (doc.folder || '').startsWith(`${folder}/`)).length; }

function renderHome() {
  disposeReader();
  app.replaceChildren(document.querySelector('#home-template').content.cloneNode(true));
  const search = document.querySelector('#search');
  search.value = state.query;
  search.addEventListener('input', event => { state.query = event.target.value; renderCards(); });
  window.addEventListener('keydown', event => { if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') { event.preventDefault(); search.focus(); } }, { once: true });
  renderFolderTree(); renderFormats(); renderFilters(); renderCards();
}

function renderFolderTree() {
  const current = state.folder;
  const prefix = current ? `${current}/` : '';
  const childNames = [...new Set(state.docs.map(doc => doc.folder || '').filter(folder => folder.startsWith(prefix) && folder !== current).map(folder => folder.slice(prefix.length).split('/')[0]).filter(Boolean))].sort();
  const parent = current.includes('/') ? current.split('/').slice(0, -1).join('/') : '';
  const directFiles = state.docs.filter(doc => (doc.folder || '') === current).length;
  const controls = [];
  if (current) controls.push(`<button class="folder-button navigation" data-folder="${escapeHtml(parent)}">↩ Lên một cấp</button>`);
  controls.push(`<button class="folder-button navigation ${current ? '' : 'active'}" data-folder="">⌂ Tất cả thư mục</button>`);
  const folders = childNames.map(name => {
    const value = prefix + name;
    return `<button class="folder-button" data-folder="${escapeHtml(value)}">📁 ${escapeHtml(name)} <span class="folder-count">(${folderCount(value)})</span></button>`;
  });
  const summary = current ? `<span class="folder-summary">${directFiles} file trong folder này</span>` : `<span class="folder-summary">Chọn folder để mở nội dung</span>`;
  document.querySelector('#folder-tree').innerHTML = `${controls.join('')} ${folders.join('')} ${summary}`;
  document.querySelectorAll('[data-folder]').forEach(button => button.onclick = () => { state.folder = button.dataset.folder; renderFolderTree(); renderCards(); });
}

function renderFormats() {
  const formats = ['all', ...new Set(state.docs.map(doc => doc.type))];
  document.querySelector('#format-filters').innerHTML = formats.map(format => `<button class="filter ${state.format === format ? 'active' : ''}" data-format="${escapeHtml(format)}">${format === 'all' ? 'Tất cả định dạng' : format === 'MD' ? 'Markdown' : 'PDF'}</button>`).join('');
  document.querySelectorAll('[data-format]').forEach(button => button.onclick = () => { state.format = button.dataset.format; renderFormats(); renderCards(); });
}

function renderFilters() {
  const groups = ['all', ...new Set(state.docs.map(doc => doc.category))];
  document.querySelector('#filters').innerHTML = groups.map(group => `<button class="filter ${state.filter === group ? 'active' : ''}" data-filter="${escapeHtml(group)}">${group === 'all' ? '전체' : escapeHtml(group)}</button>`).join('');
  document.querySelectorAll('[data-filter]').forEach(button => button.onclick = () => { state.filter = button.dataset.filter; renderFilters(); renderCards(); });
}

function renderCards() {
  const term = state.query.trim().toLowerCase();
  const docs = state.docs.filter(doc => (doc.folder || '') === state.folder && (state.filter === 'all' || doc.category === state.filter) && (state.format === 'all' || doc.type === state.format) && (!term || `${titleOf(doc)} ${doc.displayPath || doc.path} ${doc.category} ${doc.language || ''}`.toLowerCase().includes(term)));
  document.querySelector('#result-count').textContent = state.folder ? `${docs.length} file` : `${state.docs.length} tài liệu`;
  document.querySelector('#result-title').textContent = state.folder ? folderLabel(state.folder) : 'Mọi tài liệu';
  document.querySelector('#document-grid').innerHTML = docs.length ? docs.map(doc => `<a class="doc-card" href="#/read/${encodeURIComponent(doc.path)}"><div class="doc-meta"><span class="type-badge">${doc.type}</span><span>${formatSize(doc.size)}</span></div><h3>${escapeHtml(titleOf(doc))}</h3><p class="doc-language">${escapeHtml(doc.language || 'vi')} · ${escapeHtml(doc.rights || 'author-confirmed')}</p><p class="doc-path">${escapeHtml(doc.displayPath || doc.path)}</p></a>`).join('') : state.folder ? '<p class="empty">Folder này chưa có file trực tiếp. Hãy mở folder con hoặc quay lên một cấp.</p>' : '<p class="empty">Chọn một folder ở trên để xem các file bên trong.</p>';
}

function markdownToHtml(markdown) {
  const blocks = escapeHtml(markdown).replace(/\r/g, '').split('\n');
  let html = '', inCode = false, code = [], inList = false;
  const usedIds = new Map();
  const inline = text => text.replace(/`([^`]+)`/g, '<code>$1</code>').replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>').replace(/\*([^*]+)\*/g, '<em>$1</em>').replace(/\[([^\]]+)\]\((https?:\/\/[^ )]+)\)/g, '<a href="$2" target="_blank" rel="noreferrer">$1</a>');
  const headingId = text => {
    const base = text.toLowerCase().replace(/&[^;]+;/g, ' ').replace(/[^\w가-힣]+/g, '-').replace(/^-+|-+$/g, '') || 'section';
    const next = (usedIds.get(base) || 0) + 1;
    usedIds.set(base, next);
    return next === 1 ? base : `${base}-${next}`;
  };
  for (const line of blocks) {
    if (line.startsWith('```')) { if (inCode) html += `<pre><code>${code.join('\n')}</code></pre>`; inCode = !inCode; code = []; continue; }
    if (inCode) { code.push(line); continue; }
    const heading = line.match(/^(#{1,3})\s+(.+)/);
    if (heading) { const text = heading[2]; const id = headingId(text); html += `<h${heading[1].length} id="${id}">${inline(text)}</h${heading[1].length}>`; continue; }
    if (/^[-*+]\s+/.test(line)) { if (!inList) { html += '<ul>'; inList = true; } html += `<li>${inline(line.replace(/^[-*+]\s+/, ''))}</li>`; continue; }
    if (inList) { html += '</ul>'; inList = false; }
    if (line.startsWith('&gt; ')) html += `<blockquote>${inline(line.slice(5))}</blockquote>`;
    else if (line.trim()) html += `<p>${inline(line)}</p>`;
  }
  if (inList) html += '</ul>';
  if (inCode) html += `<pre><code>${code.join('\n')}</code></pre>`;
  return html;
}

function readBookmark(doc) {
  try { return JSON.parse(storageGet(bookmarkKey(doc)) || 'null'); } catch { return null; }
}
function writeRouteSection(path, sectionId) {
  const suffix = sectionId ? `?section=${encodeURIComponent(sectionId)}` : '';
  history.replaceState(null, '', `#/read/${encodeURIComponent(path)}${suffix}`);
}
function scrollToHeading(id, behavior = 'smooth') {
  const heading = document.getElementById(id);
  if (!heading) return;
  window.scrollTo({ top: Math.max(0, heading.getBoundingClientRect().top + window.scrollY - 96), behavior });
}

async function renderReader(path, sectionId = '') {
  disposeReader();
  const doc = state.docs.find(item => item.path === path);
  if (!doc) { location.hash = '#/'; return; }
  app.innerHTML = `<div class="reader-layout"><aside class="reader-aside"><a class="back-link" href="#/">← 서재로 돌아가기</a><nav id="toc" class="toc" aria-label="Mục lục tài liệu"></nav></aside><article class="reader"><header class="reader-header"><p class="eyebrow">${doc.type} · ${escapeHtml(doc.category)}</p><h1>${escapeHtml(titleOf(doc))}</h1><p class="muted">${escapeHtml(doc.displayPath || doc.path)} · ${formatSize(doc.size)}</p><div id="reader-toolbar" class="reader-toolbar"></div></header><div id="content"></div></article></div>`;
  const content = document.querySelector('#content');
  if (doc.type === 'PDF') {
    content.innerHTML = `<iframe class="pdf-frame" title="${escapeHtml(titleOf(doc))}" src="${fileUrl(doc.path)}#view=FitH"></iframe><div class="reader-actions"><a class="open-file" href="${fileUrl(doc.path)}" target="_blank" rel="noreferrer">Mở PDF ở tab mới ↗</a><a class="open-file" href="${fileUrl(doc.path)}" download>Tải PDF xuống ↓</a></div>`;
    return;
  }
  try {
    const response = await fetch(fileUrl(doc.path));
    if (!response.ok) throw new Error();
    const markdown = await response.text();
    content.className = 'markdown';
    content.innerHTML = markdownToHtml(markdown);
    const headings = [...content.querySelectorAll('h1,h2,h3')];
    const toc = document.querySelector('#toc');
    toc.innerHTML = headings.map(heading => `<a href="#${heading.id}" data-toc-id="${heading.id}" class="toc-level-${heading.tagName.slice(1)}">${escapeHtml(heading.textContent)}</a>`).join('');
    content.insertAdjacentHTML('beforeend', `<a class="open-file" href="${fileUrl(doc.path)}" target="_blank" rel="noreferrer">Mở Markdown gốc ↗</a>`);

    const saved = readBookmark(doc);
    const toolbar = document.querySelector('#reader-toolbar');
    toolbar.innerHTML = `<button id="save-bookmark" class="bookmark-button" type="button">🔖 Lưu vị trí hiện tại</button><button id="restore-bookmark" class="bookmark-button" type="button" ${saved ? '' : 'disabled'}>↩ Khôi phục vị trí${saved ? '' : ' (chưa lưu)'}</button><button id="clear-bookmark" class="bookmark-button secondary" type="button" ${saved ? '' : 'disabled'}>Xóa bookmark</button><span id="bookmark-status" class="bookmark-status">${escapeHtml(bookmarkStatus(saved))}</span>`;
    const save = () => {
      const active = [...headings].reverse().find(heading => heading.getBoundingClientRect().top <= 150) || headings[0];
      const bookmark = { headingId: active?.id || '', scrollY: Math.round(window.scrollY), savedAt: new Date().toISOString() };
      const persisted = storageSet(bookmarkKey(doc), JSON.stringify(bookmark));
      document.querySelector('#restore-bookmark').disabled = false;
      document.querySelector('#clear-bookmark').disabled = false;
      document.querySelector('#bookmark-status').textContent = persisted ? bookmarkStatus(bookmark) : 'Đã lưu tạm trong phiên này; Safari chưa cho lưu lâu dài.';
    };
    const restore = () => { const bookmark = readBookmark(doc); if (!bookmark) return; if (bookmark.headingId) scrollToHeading(bookmark.headingId); else window.scrollTo({ top: bookmark.scrollY, behavior: 'smooth' }); };
    const clear = () => { storageRemove(bookmarkKey(doc)); document.querySelector('#restore-bookmark').disabled = true; document.querySelector('#clear-bookmark').disabled = true; document.querySelector('#bookmark-status').textContent = 'Đã xóa bookmark.'; };
    document.querySelector('#save-bookmark').onclick = save;
    document.querySelector('#restore-bookmark').onclick = restore;
    document.querySelector('#clear-bookmark').onclick = clear;
    toc.querySelectorAll('[data-toc-id]').forEach(link => link.onclick = event => { event.preventDefault(); const id = link.dataset.tocId; scrollToHeading(id); writeRouteSection(doc.path, id); });
    const observer = new IntersectionObserver(() => {
      const active = [...headings].reverse().find(heading => heading.getBoundingClientRect().top <= 150) || headings[0];
      toc.querySelectorAll('[data-toc-id]').forEach(link => link.classList.toggle('active', link.dataset.tocId === active?.id));
    }, { threshold: [0, 1] });
    headings.forEach(heading => observer.observe(heading));
    disposeReader = () => observer.disconnect();
    requestAnimationFrame(() => { if (sectionId) scrollToHeading(sectionId, 'auto'); });
  } catch { content.innerHTML = '<p class="empty">Không thể tải tài liệu. Hãy chạy lại build và kiểm tra đường dẫn trong library.config.json.</p>'; }
}

function route() {
  const match = location.hash.match(/^#\/read\/([^?]+)(?:\?section=(.*))?$/);
  match ? renderReader(decodeURIComponent(match[1]), match[2] ? decodeURIComponent(match[2]) : '') : renderHome();
}
async function start() {
  try { const response = await fetch('./library/library.json'); state.docs = (await response.json()).documents; }
  catch { app.innerHTML = '<p class="empty">Không tìm thấy danh sách tài liệu. Hãy chạy <code>npm run build:library</code> trước.</p>'; return; }
  route();
}
document.querySelector('#theme-toggle').onclick = () => { document.documentElement.classList.toggle('dark'); storageSet('study-shelf-theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light'); };
if (storageGet('study-shelf-theme') === 'dark') document.documentElement.classList.add('dark');
window.addEventListener('hashchange', route);
start();
