const app = document.querySelector('#app');
const state = { docs: [], query: '', filter: 'all', format: 'all', folder: '' };
let disposeReader = () => {};

const escapeHtml = value => String(value).replace(/[&<>'"]/g, char => ({ '&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;' })[char]);
const fileUrl = path => `./library/files/${path.split('/').map(encodeURIComponent).join('/')}`;
const titleOf = doc => doc.title || doc.path.split('/').pop().replace(/\.[^.]+$/, '');
const legacyBookmarkKey = doc => `study-shelf-bookmark:${doc.path}`;
const progressKey = doc => `study-shelf-progress:${doc.path}`;
const sectionBookmarksKey = doc => `study-shelf-section-bookmarks:${doc.path}`;
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
function readJson(key, fallback = null) {
  try { return JSON.parse(storageGet(key) || 'null') ?? fallback; }
  catch { return fallback; }
}
function progressStatus(saved) {
  if (!saved) return persistentStorage ? 'Tự động lưu vị trí đọc trên trình duyệt này.' : 'Trình duyệt đang chặn lưu lâu dài; tiến độ chỉ giữ trong phiên hiện tại.';
  return `${persistentStorage ? 'Tự lưu' : 'Lưu tạm'} ${new Date(saved.savedAt).toLocaleString()}`;
}
function readProgress(doc) {
  const current = readJson(progressKey(doc));
  if (current) return current;
  const legacy = readJson(legacyBookmarkKey(doc));
  if (legacy) {
    storageSet(progressKey(doc), JSON.stringify(legacy));
    return legacy;
  }
  return null;
}
function readSectionBookmarks(doc) {
  const value = readJson(sectionBookmarksKey(doc), []);
  return Array.isArray(value) ? value : [];
}
function writeSectionBookmarks(doc, bookmarks) {
  return storageSet(sectionBookmarksKey(doc), JSON.stringify(bookmarks));
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

function writeRouteSection(path, sectionId) {
  const suffix = sectionId ? `?section=${encodeURIComponent(sectionId)}` : '';
  history.replaceState(null, '', `#/read/${encodeURIComponent(path)}${suffix}`);
}
function scrollToHeading(id, behavior = 'smooth') {
  const heading = document.getElementById(id);
  if (!heading) return false;
  window.scrollTo({ top: Math.max(0, heading.getBoundingClientRect().top + window.scrollY - 96), behavior });
  return true;
}

async function renderReader(path, sectionId = '') {
  disposeReader();
  const doc = state.docs.find(item => item.path === path);
  if (!doc) { location.hash = '#/'; return; }

  app.innerHTML = `<div class="reader-shell">
    <div class="reader-layout">
      <aside id="reader-aside" class="reader-aside" aria-label="Điều hướng tài liệu">
        <div class="reader-aside-top">
          <a class="back-link" href="#/">← 서재로 돌아가기</a>
          <button id="toc-close" class="aside-close" type="button" aria-label="Đóng mục lục">×</button>
        </div>
        <section class="progress-card" aria-live="polite">
          <p class="aside-kicker">READING PROGRESS</p>
          <strong id="current-section-label">Đầu tài liệu</strong>
          <span id="progress-status">${escapeHtml(progressStatus(readProgress(doc)))}</span>
        </section>
        <section class="aside-section">
          <div class="aside-title-row"><span>Mục lục</span><span id="toc-count" class="aside-count"></span></div>
          <nav id="toc" class="toc" aria-label="Mục lục tài liệu"></nav>
        </section>
        <section class="aside-section bookmarks-panel">
          <div class="aside-title-row"><span>Bookmarks</span><span id="bookmark-count" class="aside-count"></span></div>
          <div id="bookmark-list" class="bookmark-list"></div>
        </section>
      </aside>
      <article class="reader">
        <header class="reader-header">
          <p class="eyebrow">${doc.type} · ${escapeHtml(doc.category)}</p>
          <h1>${escapeHtml(titleOf(doc))}</h1>
          <p class="muted">${escapeHtml(doc.displayPath || doc.path)} · ${formatSize(doc.size)}</p>
          <div id="reader-toolbar" class="reader-toolbar"></div>
        </header>
        <div id="content"></div>
      </article>
    </div>
    <button id="reader-overlay" class="reader-overlay" type="button" aria-label="Đóng mục lục"></button>
    <div class="reader-edge-actions" aria-label="Reader shortcuts">
      <button id="toc-toggle" class="edge-button edge-toc" type="button" aria-label="Mở mục lục" title="Mục lục">☰</button>
      <button id="edge-bookmark" class="edge-button" type="button" aria-label="Bookmark section hiện tại" title="Bookmark section hiện tại">☆</button>
      <button id="edge-restore" class="edge-button" type="button" aria-label="Về vị trí đọc gần nhất" title="Về vị trí đọc gần nhất">↩</button>
    </div>
    <div class="reading-progress-rail" aria-hidden="true"><span id="reading-progress-bar"></span></div>
  </div>`;

  const content = document.querySelector('#content');
  const aside = document.querySelector('#reader-aside');
  const overlay = document.querySelector('#reader-overlay');
  const setDrawer = open => {
    aside.classList.toggle('open', open);
    overlay.classList.toggle('open', open);
    document.body.classList.toggle('reader-drawer-open', open);
  };
  document.querySelector('#toc-toggle').onclick = () => setDrawer(true);
  document.querySelector('#toc-close').onclick = () => setDrawer(false);
  overlay.onclick = () => setDrawer(false);

  if (doc.type === 'PDF') {
    document.querySelector('#toc').innerHTML = '<p class="toc-empty">Mục lục theo section hiện hỗ trợ tài liệu Markdown.</p>';
    document.querySelector('#bookmark-list').innerHTML = '<p class="bookmark-empty">PDF dùng bookmark của trình đọc PDF hoặc mở ở tab mới.</p>';
    document.querySelector('.reader-edge-actions').hidden = true;
    document.querySelector('.progress-card').hidden = true;
    content.innerHTML = `<iframe class="pdf-frame" title="${escapeHtml(titleOf(doc))}" src="${fileUrl(doc.path)}#view=FitH"></iframe><div class="reader-actions"><a class="open-file" href="${fileUrl(doc.path)}" target="_blank" rel="noreferrer">Mở PDF ở tab mới ↗</a><a class="open-file" href="${fileUrl(doc.path)}" download>Tải PDF xuống ↓</a></div>`;
    disposeReader = () => { setDrawer(false); };
    return;
  }

  try {
    const response = await fetch(fileUrl(doc.path));
    if (!response.ok) throw new Error();
    const markdown = await response.text();
    content.className = 'markdown';
    content.innerHTML = markdownToHtml(markdown);
    const headings = [...content.querySelectorAll('h1,h2,h3')];
    const headingById = new Map(headings.map(heading => [heading.id, heading]));
    const toc = document.querySelector('#toc');
    document.querySelector('#toc-count').textContent = `${headings.length}`;
    toc.innerHTML = headings.length ? headings.map(heading => `<div class="toc-item toc-level-${heading.tagName.slice(1)}" data-toc-row="${heading.id}"><a href="#${heading.id}" data-toc-id="${heading.id}">${escapeHtml(heading.textContent)}</a><button class="toc-bookmark-toggle" type="button" data-bookmark-id="${heading.id}" aria-label="Bookmark ${escapeHtml(heading.textContent)}" title="Bookmark section">☆</button></div>`).join('') : '<p class="toc-empty">Tài liệu này chưa có heading để tạo mục lục.</p>';
    content.insertAdjacentHTML('beforeend', `<a class="open-file" href="${fileUrl(doc.path)}" target="_blank" rel="noreferrer">Mở Markdown gốc ↗</a>`);

    let bookmarks = readSectionBookmarks(doc).filter(item => item && headingById.has(item.headingId));
    if (bookmarks.length !== readSectionBookmarks(doc).length) writeSectionBookmarks(doc, bookmarks);
    let activeId = headings[0]?.id || '';
    let progressTimer = 0;
    let scrollTicking = false;
    const status = document.querySelector('#progress-status');
    const currentLabel = document.querySelector('#current-section-label');
    const bookmarkList = document.querySelector('#bookmark-list');
    const toolbar = document.querySelector('#reader-toolbar');
    const edgeBookmark = document.querySelector('#edge-bookmark');
    const edgeRestore = document.querySelector('#edge-restore');
    const progressBar = document.querySelector('#reading-progress-bar');

    toolbar.innerHTML = `<button id="toggle-current-bookmark" class="bookmark-button" type="button">☆ Bookmark section</button><button id="restore-progress" class="bookmark-button" type="button">↩ Về vị trí đọc gần nhất</button><button id="clear-progress" class="bookmark-button secondary" type="button">Xóa vị trí đã lưu</button><span class="bookmark-status">Auto-save bật · lưu theo section và vị trí scroll</span>`;

    const findBookmarkIndex = id => bookmarks.findIndex(item => item.headingId === id);
    const isBookmarked = id => findBookmarkIndex(id) >= 0;
    const updateBookmarkButtons = () => {
      const currentBookmarked = activeId && isBookmarked(activeId);
      const currentButton = document.querySelector('#toggle-current-bookmark');
      if (currentButton) currentButton.textContent = currentBookmarked ? '★ Bỏ bookmark section' : '☆ Bookmark section';
      edgeBookmark.textContent = currentBookmarked ? '★' : '☆';
      edgeBookmark.classList.toggle('active', Boolean(currentBookmarked));
      toc.querySelectorAll('[data-bookmark-id]').forEach(button => {
        const bookmarked = isBookmarked(button.dataset.bookmarkId);
        button.textContent = bookmarked ? '★' : '☆';
        button.classList.toggle('active', bookmarked);
        button.setAttribute('aria-pressed', String(bookmarked));
      });
    };
    const renderBookmarkList = () => {
      document.querySelector('#bookmark-count').textContent = `${bookmarks.length}`;
      bookmarkList.innerHTML = bookmarks.length ? bookmarks.map(item => `<div class="bookmark-row"><button class="bookmark-jump" type="button" data-bookmark-jump="${item.headingId}">${escapeHtml(item.title)}</button><button class="bookmark-remove" type="button" data-bookmark-remove="${item.headingId}" aria-label="Xóa bookmark ${escapeHtml(item.title)}" title="Xóa bookmark">×</button></div>`).join('') : '<p class="bookmark-empty">Bấm ☆ cạnh một section để lưu.</p>';
      bookmarkList.querySelectorAll('[data-bookmark-jump]').forEach(button => button.onclick = () => {
        const id = button.dataset.bookmarkJump;
        if (scrollToHeading(id)) {
          writeRouteSection(doc.path, id);
          if (window.innerWidth <= 900) setDrawer(false);
        }
      });
      bookmarkList.querySelectorAll('[data-bookmark-remove]').forEach(button => button.onclick = () => toggleBookmark(button.dataset.bookmarkRemove, false));
      updateBookmarkButtons();
    };
    const toggleBookmark = (id, force) => {
      const heading = headingById.get(id);
      if (!heading) return;
      const index = findBookmarkIndex(id);
      const shouldAdd = typeof force === 'boolean' ? force : index < 0;
      if (shouldAdd && index < 0) bookmarks.push({ headingId: id, title: heading.textContent.trim(), savedAt: new Date().toISOString() });
      if (!shouldAdd && index >= 0) bookmarks.splice(index, 1);
      writeSectionBookmarks(doc, bookmarks);
      renderBookmarkList();
    };

    const saveProgressNow = id => {
      const heading = id ? headingById.get(id) : null;
      const progress = { headingId: heading?.id || '', headingTitle: heading?.textContent.trim() || '', scrollY: Math.round(window.scrollY), savedAt: new Date().toISOString() };
      storageSet(progressKey(doc), JSON.stringify(progress));
      status.textContent = progressStatus(progress);
      return progress;
    };
    const scheduleProgressSave = id => {
      window.clearTimeout(progressTimer);
      progressTimer = window.setTimeout(() => saveProgressNow(id), 280);
    };
    const updateReadPercent = () => {
      const available = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
      const percent = Math.max(0, Math.min(100, (window.scrollY / available) * 100));
      progressBar.style.height = `${percent}%`;
    };
    const setActiveSection = (id, { syncUrl = true, save = true } = {}) => {
      if (!id || !headingById.has(id)) return;
      activeId = id;
      const heading = headingById.get(id);
      toc.querySelectorAll('[data-toc-row]').forEach(row => row.classList.toggle('active', row.dataset.tocRow === id));
      currentLabel.textContent = heading.textContent.trim();
      updateBookmarkButtons();
      if (syncUrl) writeRouteSection(doc.path, id);
      if (save) scheduleProgressSave(id);
    };
    const activeFromScroll = () => {
      if (!headings.length) return '';
      const cutoff = Math.min(190, Math.max(120, window.innerHeight * 0.23));
      let active = headings[0];
      for (const heading of headings) {
        if (heading.getBoundingClientRect().top <= cutoff) active = heading;
        else break;
      }
      return active.id;
    };
    const onScroll = () => {
      if (scrollTicking) return;
      scrollTicking = true;
      requestAnimationFrame(() => {
        scrollTicking = false;
        const next = activeFromScroll();
        if (next && next !== activeId) setActiveSection(next);
        else if (next) scheduleProgressSave(next);
        updateReadPercent();
      });
    };
    const restoreProgress = (behavior = 'smooth') => {
      const saved = readProgress(doc);
      if (!saved) return false;
      if (saved.headingId && scrollToHeading(saved.headingId, behavior)) {
        setActiveSection(saved.headingId, { syncUrl: true, save: false });
        return true;
      }
      window.scrollTo({ top: saved.scrollY || 0, behavior });
      return true;
    };
    const clearProgress = () => {
      storageRemove(progressKey(doc));
      storageRemove(legacyBookmarkKey(doc));
      status.textContent = 'Đã xóa vị trí đã lưu. Auto-save sẽ tạo lại khi bạn tiếp tục đọc.';
    };

    document.querySelector('#toggle-current-bookmark').onclick = () => activeId && toggleBookmark(activeId);
    edgeBookmark.onclick = () => activeId && toggleBookmark(activeId);
    document.querySelector('#restore-progress').onclick = () => restoreProgress();
    edgeRestore.onclick = () => restoreProgress();
    document.querySelector('#clear-progress').onclick = clearProgress;

    toc.querySelectorAll('[data-toc-id]').forEach(link => link.onclick = event => {
      event.preventDefault();
      const id = link.dataset.tocId;
      if (scrollToHeading(id)) {
        setActiveSection(id);
        if (window.innerWidth <= 900) setDrawer(false);
      }
    });
    toc.querySelectorAll('[data-bookmark-id]').forEach(button => button.onclick = event => {
      event.preventDefault();
      event.stopPropagation();
      toggleBookmark(button.dataset.bookmarkId);
    });

    renderBookmarkList();
    const onPageHide = () => saveProgressNow(activeFromScroll() || activeId);
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('pagehide', onPageHide);
    updateReadPercent();

    requestAnimationFrame(() => {
      const saved = readProgress(doc);
      if (sectionId && headingById.has(sectionId)) {
        scrollToHeading(sectionId, 'auto');
        setActiveSection(sectionId, { syncUrl: false });
      } else if (saved) {
        restoreProgress('auto');
      } else if (headings[0]) {
        setActiveSection(headings[0].id, { syncUrl: false, save: false });
      }
      updateReadPercent();
    });

    disposeReader = () => {
      window.removeEventListener('scroll', onScroll);
      window.removeEventListener('pagehide', onPageHide);
      window.clearTimeout(progressTimer);
      document.body.classList.remove('reader-drawer-open');
      if (activeId) saveProgressNow(activeFromScroll() || activeId);
    };
  } catch {
    content.innerHTML = '<p class="empty">Không thể tải tài liệu. Hãy chạy lại build và kiểm tra đường dẫn trong library.config.json.</p>';
  }
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
