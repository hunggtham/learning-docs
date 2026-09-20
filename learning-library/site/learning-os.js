(() => {
  const LOS = {
    docs: [],
    searchIndex: null,
    graph: null,
    installPrompt: null,
    readerPath: '',
    readerCleanup: () => {},
    enhanceQueued: false
  };

  const esc = value => String(value ?? '').replace(/[&<>'"]/g, char => ({ '&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;' })[char]);
  const norm = value => String(value ?? '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().trim();
  const fileUrl = path => `./library/files/${path.split('/').map(encodeURIComponent).join('/')}`;
  const docStateKey = path => `study-shelf-doc-state:${path}`;
  const progressKey = path => `study-shelf-progress:${path}`;
  const bookmarksKey = path => `study-shelf-section-bookmarks:${path}`;
  const statusLabels = { unread: 'Chưa đọc', reading: 'Đang đọc', review: 'Cần ôn lại', completed: 'Hoàn thành' };

  function readJson(key, fallback = null) {
    try { return JSON.parse(localStorage.getItem(key) || 'null') ?? fallback; }
    catch { return fallback; }
  }
  function writeJson(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); return true; }
    catch { return false; }
  }
  function readDocState(path) {
    return readJson(docStateKey(path), { status: 'unread', progressPct: 0, lastOpened: null, updatedAt: null });
  }
  function writeDocState(path, patch) {
    const next = { ...readDocState(path), ...patch, updatedAt: new Date().toISOString() };
    writeJson(docStateKey(path), next);
    return next;
  }
  function routePath() {
    const match = location.hash.match(/^#\/read\/([^?]+)/);
    return match ? decodeURIComponent(match[1]) : '';
  }
  function docByPath(path) { return LOS.docs.find(doc => doc.path === path); }
  function progressFor(path) { return readJson(progressKey(path), null); }
  function bookmarksFor(path) {
    const value = readJson(bookmarksKey(path), []);
    return Array.isArray(value) ? value : [];
  }
  function percentFor(path) {
    const state = readDocState(path);
    return Math.max(0, Math.min(100, Number(state.progressPct) || 0));
  }
  function lastOpenedFor(path) {
    const state = readDocState(path);
    const progress = progressFor(path);
    return state.lastOpened || progress?.savedAt || null;
  }
  function readAllBookmarks() {
    return LOS.docs.flatMap(doc => bookmarksFor(doc.path).map(item => ({ ...item, path: doc.path, docTitle: doc.title, category: doc.category })));
  }
  function slugifyHeading(text) {
    return String(text).toLowerCase().replace(/&[^;]+;/g, ' ').replace(/[^\w가-힣]+/g, '-').replace(/^-+|-+$/g, '') || 'section';
  }
  function normalizeRelativePath(fromPath, target) {
    const raw = decodeURIComponent(target.split('#')[0]).replaceAll('\\', '/');
    if (!raw) return '';
    const parts = (raw.startsWith('/') ? raw.slice(1) : `${fromPath.split('/').slice(0, -1).join('/')}/${raw}`).split('/');
    const out = [];
    for (const part of parts) {
      if (!part || part === '.') continue;
      if (part === '..') out.pop(); else out.push(part);
    }
    return out.join('/');
  }
  function resolveInternalTarget(fromPath, rawTarget) {
    const target = rawTarget.trim();
    if (!target || /^(https?:|mailto:|tel:|#)/i.test(target)) return null;
    const hash = target.includes('#') ? target.slice(target.indexOf('#') + 1) : '';
    const base = target.split('#')[0];
    if (/\.md$/i.test(base)) {
      const resolved = normalizeRelativePath(fromPath, base);
      const direct = docByPath(resolved);
      if (direct) return { doc: direct, section: hash ? slugifyHeading(hash) : '' };
    }
    const key = norm(base.replace(/\.md$/i, ''));
    const found = LOS.docs.find(doc => doc.type === 'MD' && [doc.title, doc.path.replace(/\.md$/i, ''), doc.displayPath?.replace(/\.md$/i, ''), doc.path.split('/').pop().replace(/\.md$/i, '')].some(alias => norm(alias) === key));
    return found ? { doc: found, section: hash ? slugifyHeading(hash) : '' } : null;
  }
  function hrefFor(path, section = '') {
    return `#/read/${encodeURIComponent(path)}${section ? `?section=${encodeURIComponent(section)}` : ''}`;
  }

  function toast(message) {
    let node = document.querySelector('#los-toast');
    if (!node) {
      node = document.createElement('div');
      node.id = 'los-toast';
      node.className = 'los-toast';
      document.body.append(node);
    }
    node.textContent = message;
    node.classList.add('show');
    clearTimeout(node._timer);
    node._timer = setTimeout(() => node.classList.remove('show'), 2200);
  }

  async function loadSearchIndex() {
    if (LOS.searchIndex) return LOS.searchIndex;
    const response = await fetch('./library/search-index.json');
    if (!response.ok) throw new Error('search index unavailable');
    LOS.searchIndex = (await response.json()).documents || [];
    return LOS.searchIndex;
  }
  async function loadGraph() {
    if (LOS.graph) return LOS.graph;
    const response = await fetch('./library/graph.json');
    if (!response.ok) throw new Error('graph unavailable');
    LOS.graph = await response.json();
    return LOS.graph;
  }

  function decorateCards() {
    document.querySelectorAll('.doc-card').forEach(card => {
      if (card.querySelector('.los-card-meta')) return;
      const match = card.getAttribute('href')?.match(/^#\/read\/([^?]+)/);
      if (!match) return;
      const path = decodeURIComponent(match[1]);
      const state = readDocState(path);
      const pct = percentFor(path);
      const meta = document.createElement('div');
      meta.className = 'los-card-meta';
      meta.innerHTML = `<span class="los-status-chip">${esc(statusLabels[state.status] || statusLabels.unread)}</span>${pct ? `<span class="los-card-progress">${Math.round(pct)}%</span>` : ''}`;
      card.append(meta);
    });
  }

  function recentDocuments() {
    return LOS.docs.map(doc => ({ doc, opened: lastOpenedFor(doc.path), pct: percentFor(doc.path), state: readDocState(doc.path) }))
      .filter(item => item.opened)
      .sort((a, b) => new Date(b.opened) - new Date(a.opened))
      .slice(0, 6);
  }

  function dashboardPanel(title, count, body) {
    return `<section class="los-panel"><div class="los-panel-head"><h3>${esc(title)}</h3><span class="los-count">${count}</span></div>${body}</section>`;
  }
  function docMiniItem(doc, extra = '', section = '') {
    return `<a class="los-item" href="${hrefFor(doc.path, section)}"><strong>${esc(doc.title)}</strong><span>${esc(extra || doc.displayPath || doc.path)}</span></a>`;
  }

  function renderHomeDashboard() {
    const home = document.querySelector('.library-section');
    if (!home || document.querySelector('#los-dashboard')) return;
    const recent = recentDocuments();
    const bookmarks = readAllBookmarks().sort((a, b) => new Date(b.savedAt || 0) - new Date(a.savedAt || 0)).slice(0, 6);
    const review = LOS.docs.filter(doc => readDocState(doc.path).status === 'review').slice(0, 6);
    const recentBody = recent.length ? `<div class="los-list">${recent.map(({ doc, pct, state }) => `<a class="los-item" href="${hrefFor(doc.path)}"><strong>${esc(doc.title)}</strong><span>${esc(statusLabels[state.status] || '')} · ${Math.round(pct)}%</span><div class="los-progress"><i style="width:${pct}%"></i></div></a>`).join('')}</div>` : '<p class="los-empty">Chưa có lịch sử đọc.</p>';
    const bookmarkBody = bookmarks.length ? `<div class="los-list">${bookmarks.map(item => docMiniItem(docByPath(item.path), item.title || 'Bookmark', item.headingId || '')).join('')}</div>` : '<p class="los-empty">Chưa có bookmark.</p>';
    const reviewBody = review.length ? `<div class="los-list">${review.map(doc => docMiniItem(doc, 'Cần ôn lại')).join('')}</div>` : '<p class="los-empty">Review queue đang trống.</p>';
    const section = document.createElement('section');
    section.id = 'los-dashboard';
    section.className = 'los-dashboard';
    section.innerHTML = `<div class="library-heading"><div><p class="eyebrow">LEARNING OS</p><h2>Tiếp tục học</h2></div><button class="los-action" type="button" data-los-open="review">Mở Learning OS</button></div><div class="los-dashboard-grid">${dashboardPanel('Continue Reading', recent.length, recentBody)}${dashboardPanel('Global Bookmarks', readAllBookmarks().length, bookmarkBody)}${dashboardPanel('Review Queue', LOS.docs.filter(doc => readDocState(doc.path).status === 'review').length, reviewBody)}</div>`;
    home.before(section);
    section.querySelector('[data-los-open]').onclick = () => openModal('review');
  }

  let searchTimer = 0;
  async function runGlobalSearch(query, target) {
    const q = norm(query);
    if (q.length < 2) { target.classList.remove('open'); target.innerHTML = ''; return; }
    target.classList.add('open');
    target.innerHTML = '<div class="los-search-head"><span>Đang tìm trong toàn bộ library…</span></div>';
    try {
      const index = await loadSearchIndex();
      const terms = q.split(/\s+/).filter(Boolean);
      const scored = [];
      for (const item of index) {
        const title = norm(item.title);
        const path = norm(`${item.displayPath || item.path} ${item.category || ''}`);
        const headings = norm((item.headings || []).map(h => h.text).join(' '));
        const text = norm(item.text || '');
        let score = 0;
        for (const term of terms) {
          if (title.includes(term)) score += 12;
          if (headings.includes(term)) score += 7;
          if (path.includes(term)) score += 4;
          if (text.includes(term)) score += 1;
        }
        if (!score || terms.some(term => !`${title} ${headings} ${path} ${text}`.includes(term))) continue;
        const rawText = item.text || '';
        const first = terms.map(term => norm(rawText).indexOf(term)).filter(pos => pos >= 0).sort((a,b) => a-b)[0] ?? 0;
        const start = Math.max(0, first - 90);
        const snippet = rawText.slice(start, start + 260);
        scored.push({ item, score, snippet });
      }
      scored.sort((a, b) => b.score - a.score || a.item.title.localeCompare(b.item.title));
      const results = scored.slice(0, 20);
      target.innerHTML = `<div class="los-search-head"><span>Global Search</span><span>${results.length}${scored.length > 20 ? '+' : ''} kết quả</span></div><div class="los-search-list">${results.length ? results.map(({ item, snippet }) => `<a class="los-search-result" href="${hrefFor(item.path)}"><strong>${esc(item.title)}</strong><small>${esc(item.displayPath || item.path)}</small>${snippet ? `<p>${esc(snippet)}</p>` : ''}</a>`).join('') : '<p class="los-empty" style="padding:14px">Không tìm thấy nội dung phù hợp.</p>'}</div>`;
    } catch {
      target.innerHTML = '<p class="los-empty" style="padding:14px">Search index chưa sẵn sàng. Hãy deploy lại site.</p>';
    }
  }

  function enhanceSearch() {
    const input = document.querySelector('#search');
    const box = input?.closest('.search-box');
    if (!input || !box || document.querySelector('#los-global-search')) return;
    input.placeholder = 'Tìm tiêu đề, nội dung, heading trên toàn bộ library…';
    const target = document.createElement('div');
    target.id = 'los-global-search';
    target.className = 'los-search-results';
    box.after(target);
    input.addEventListener('input', () => {
      clearTimeout(searchTimer);
      searchTimer = setTimeout(() => runGlobalSearch(input.value, target), 180);
    });
    input.addEventListener('keydown', event => { if (event.key === 'Escape') target.classList.remove('open'); });
  }

  function enhanceHome() {
    renderHomeDashboard();
    enhanceSearch();
    decorateCards();
  }

  function linkifyInternalMarkdown(content, currentPath) {
    if (!content || content.dataset.losLinked === '1') return;
    const walker = document.createTreeWalker(content, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        if (!node.nodeValue || !/(\[\[[^\]]+\]\]|\[[^\]]+\]\([^)]*\.md[^)]*\))/.test(node.nodeValue)) return NodeFilter.FILTER_REJECT;
        if (node.parentElement?.closest('a,code,pre,script,style')) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    const pattern = /\[([^\]]+)\]\(([^)]+\.md(?:#[^)]+)?)\)|\[\[([^\]|#]+)(?:#([^\]|]+))?(?:\|([^\]]+))?\]\]/g;
    for (const node of nodes) {
      const text = node.nodeValue;
      pattern.lastIndex = 0;
      let match, last = 0;
      const fragment = document.createDocumentFragment();
      let changed = false;
      while ((match = pattern.exec(text))) {
        const rawTarget = match[2] || `${match[3]}${match[4] ? `#${match[4]}` : ''}`;
        const resolved = resolveInternalTarget(currentPath, rawTarget);
        if (!resolved) continue;
        fragment.append(document.createTextNode(text.slice(last, match.index)));
        const anchor = document.createElement('a');
        anchor.className = 'los-internal-link';
        anchor.href = hrefFor(resolved.doc.path, resolved.section);
        anchor.textContent = match[1] || match[5] || match[3];
        fragment.append(anchor);
        last = match.index + match[0].length;
        changed = true;
      }
      if (changed) {
        fragment.append(document.createTextNode(text.slice(last)));
        node.replaceWith(fragment);
      }
    }
    content.dataset.losLinked = '1';
  }

  async function cacheDocument(doc) {
    const url = fileUrl(doc.path);
    try {
      if ('caches' in window) {
        const cache = await caches.open('study-shelf-user-v1');
        await cache.add(url);
        toast('Đã lưu tài liệu để đọc offline.');
        return;
      }
      navigator.serviceWorker?.controller?.postMessage({ type: 'CACHE_URL', url });
      toast('Đã gửi yêu cầu lưu offline.');
    } catch { toast('Không thể lưu offline trên trình duyệt này.'); }
  }

  async function renderRelated(doc, host) {
    if (!host || host.querySelector('.los-related') || host.dataset.losRelatedLoading === '1') return;
    host.dataset.losRelatedLoading = '1';
    try {
      const graph = await loadGraph();
      const linked = new Set();
      graph.edges.forEach(edge => {
        if (edge.source === doc.path) linked.add(edge.target);
        if (edge.target === doc.path) linked.add(edge.source);
      });
      const related = [...linked].map(docByPath).filter(Boolean).slice(0, 6);
      if (!related.length) LOS.docs.filter(item => item.path !== doc.path && item.category === doc.category && item.type === 'MD').slice(0, 4).forEach(item => related.push(item));
      if (!related.length || !host.isConnected || routePath() !== doc.path || host.querySelector('.los-related')) return;
      const section = document.createElement('section');
      section.className = 'los-related';
      section.innerHTML = `<h3>Knowledge links</h3><div class="los-related-grid">${related.map(item => docMiniItem(item, item.category)).join('')}</div>`;
      host.append(section);
    } catch {}
    finally { delete host.dataset.losRelatedLoading; }
  }

  function enhanceReader(path) {
    const doc = docByPath(path);
    const header = document.querySelector('.reader-header');
    if (!doc || !header) return;

    if (LOS.readerPath !== path) {
      LOS.readerCleanup();
      LOS.readerPath = path;
      const current = readDocState(path);
      writeDocState(path, { status: current.status === 'unread' ? 'reading' : current.status, lastOpened: new Date().toISOString() });
      let timer = 0;
      const onScroll = () => {
        clearTimeout(timer);
        timer = setTimeout(() => {
          if (routePath() !== path) return;
          const state = readDocState(path);
          const total = Math.max(1, document.documentElement.scrollHeight - innerHeight);
          const measuredPct = Math.max(0, Math.min(100, scrollY / total * 100));
          const pct = state.status === 'completed' ? 100 : measuredPct;
          const progress = progressFor(path);
          writeDocState(path, { progressPct: pct, lastOpened: new Date().toISOString(), currentSection: progress?.headingId || state.currentSection || '' });
        }, 350);
      };
      addEventListener('scroll', onScroll, { passive: true });
      LOS.readerCleanup = () => { removeEventListener('scroll', onScroll); clearTimeout(timer); };
    }

    if (!header.querySelector('#los-reader-controls')) {
      const state = readDocState(path);
      const controls = document.createElement('div');
      controls.id = 'los-reader-controls';
      controls.className = 'los-reader-controls';
      controls.innerHTML = `<label><span class="sr-only">Reading status</span><select id="los-status" class="los-select"><option value="unread">Chưa đọc</option><option value="reading">Đang đọc</option><option value="review">Cần ôn lại</option><option value="completed">Hoàn thành</option></select></label><button id="los-offline" class="los-action" type="button">↓ Lưu offline</button><button id="los-tools" class="los-action" type="button">Learning OS</button><span class="los-offline-badge">Progress ${Math.round(percentFor(path))}%</span>`;
      header.append(controls);
      const select = controls.querySelector('#los-status');
      select.value = state.status || 'reading';
      select.onchange = () => {
        const patch = { status: select.value, lastOpened: new Date().toISOString() };
        if (select.value === 'completed') patch.progressPct = 100;
        writeDocState(path, patch);
        toast(`Trạng thái: ${statusLabels[select.value]}`);
      };
      controls.querySelector('#los-offline').onclick = () => cacheDocument(doc);
      controls.querySelector('#los-tools').onclick = () => openModal('bookmarks');
    }

    const content = document.querySelector('.markdown');
    if (content) {
      linkifyInternalMarkdown(content, path);
      renderRelated(doc, content);
    }
  }

  function exportSnapshot() {
    const data = { version: 1, exportedAt: new Date().toISOString(), origin: location.origin, data: {} };
    try {
      for (let i = 0; i < localStorage.length; i += 1) {
        const key = localStorage.key(i);
        if (key?.startsWith('study-shelf-')) data.data[key] = localStorage.getItem(key);
      }
    } catch {}
    return data;
  }
  function importSnapshot(snapshot) {
    if (!snapshot || snapshot.version !== 1 || typeof snapshot.data !== 'object') throw new Error('invalid snapshot');
    let count = 0;
    for (const [key, value] of Object.entries(snapshot.data)) {
      if (!key.startsWith('study-shelf-') || typeof value !== 'string') continue;
      localStorage.setItem(key, value);
      count += 1;
    }
    localStorage.setItem('study-shelf-last-sync', new Date().toISOString());
    return count;
  }
  function downloadSnapshot() {
    const blob = new Blob([JSON.stringify(exportSnapshot(), null, 2)], { type: 'application/json' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `study-shelf-sync-${new Date().toISOString().slice(0,10)}.json`;
    link.click();
    setTimeout(() => URL.revokeObjectURL(link.href), 1000);
  }

  function ensureModal() {
    let modal = document.querySelector('#los-modal');
    if (modal) return modal;
    modal = document.createElement('div');
    modal.id = 'los-modal';
    modal.className = 'los-modal';
    modal.innerHTML = `<button class="los-backdrop" type="button" aria-label="Đóng Learning OS"></button><section class="los-sheet" role="dialog" aria-modal="true" aria-label="Learning OS"><header class="los-sheet-head"><h2>Learning OS</h2><button class="los-close" type="button" aria-label="Đóng">×</button></header><nav class="los-tabs"><button class="los-tab" data-tab="bookmarks">Bookmarks</button><button class="los-tab" data-tab="review">Review</button><button class="los-tab" data-tab="graph">Graph</button><button class="los-tab" data-tab="sync">Sync</button><button class="los-tab" data-tab="offline">Offline</button></nav><div id="los-sheet-body" class="los-sheet-body"></div></section>`;
    document.body.append(modal);
    modal.querySelector('.los-backdrop').onclick = closeModal;
    modal.querySelector('.los-close').onclick = closeModal;
    modal.querySelectorAll('[data-tab]').forEach(button => button.onclick = () => renderModalTab(button.dataset.tab));
    return modal;
  }
  function closeModal() { document.querySelector('#los-modal')?.classList.remove('open'); }
  function openModal(tab = 'bookmarks') {
    ensureModal().classList.add('open');
    renderModalTab(tab);
  }

  async function renderModalTab(tab) {
    const modal = ensureModal();
    modal.querySelectorAll('[data-tab]').forEach(button => button.classList.toggle('active', button.dataset.tab === tab));
    const body = modal.querySelector('#los-sheet-body');
    if (tab === 'bookmarks') {
      const items = readAllBookmarks().sort((a,b) => new Date(b.savedAt || 0) - new Date(a.savedAt || 0));
      body.innerHTML = `<section class="los-tool-section"><h3>Global Bookmarks</h3><p>${items.length} section đã lưu trên toàn library.</p><div class="los-list">${items.length ? items.map(item => docMiniItem(docByPath(item.path), `${item.title || 'Bookmark'} · ${item.category || ''}`, item.headingId || '')).join('') : '<p class="los-empty">Chưa có bookmark.</p>'}</div></section>`;
    } else if (tab === 'review') {
      const items = LOS.docs.filter(doc => readDocState(doc.path).status === 'review');
      body.innerHTML = `<section class="los-tool-section"><h3>Review Queue</h3><p>Đánh dấu tài liệu là “Cần ôn lại” trong reader để đưa vào hàng đợi.</p><div class="los-list">${items.length ? items.map(doc => docMiniItem(doc, `${Math.round(percentFor(doc.path))}% · ${doc.category}`)).join('') : '<p class="los-empty">Không có tài liệu cần ôn lại.</p>'}</div></section>`;
    } else if (tab === 'graph') {
      body.innerHTML = '<section class="los-tool-section"><h3>Knowledge Graph</h3><p>Đang tải quan hệ giữa các tài liệu…</p></section>';
      try {
        const graph = await loadGraph();
        const degree = new Map(graph.nodes.map(node => [node.path, 0]));
        graph.edges.forEach(edge => { degree.set(edge.source, (degree.get(edge.source) || 0) + 1); degree.set(edge.target, (degree.get(edge.target) || 0) + 1); });
        const nodes = [...graph.nodes].sort((a,b) => (degree.get(b.path) || 0) - (degree.get(a.path) || 0));
        body.innerHTML = `<section class="los-tool-section"><h3>Knowledge Graph</h3><p>${graph.nodes.length} nodes · ${graph.edges.length} internal links. Click tài liệu để mở; số bên phải là số connection.</p><input id="los-graph-search" class="los-graph-search" type="search" placeholder="Lọc node theo tên, folder, category…"><div id="los-graph-list" class="los-graph-list"></div></section>`;
        const input = body.querySelector('#los-graph-search');
        const list = body.querySelector('#los-graph-list');
        const render = () => {
          const q = norm(input.value);
          const filtered = nodes.filter(node => !q || norm(`${node.title} ${node.folder} ${node.category}`).includes(q)).slice(0, 120);
          list.innerHTML = filtered.map(node => `<div class="los-graph-node"><a href="${hrefFor(node.path)}">${esc(node.title)}</a><span>${degree.get(node.path) || 0} links</span></div>`).join('');
        };
        input.oninput = render; render();
      } catch { body.innerHTML = '<p class="los-empty">Graph index chưa sẵn sàng.</p>'; }
    } else if (tab === 'sync') {
      const lastSync = localStorage.getItem('study-shelf-last-sync');
      body.innerHTML = `<section class="los-tool-section"><h3>Sync đa thiết bị</h3><p>Site hiện là GitHub Pages tĩnh nên chưa có account/cloud database. Sync này dùng snapshot portable: export trên thiết bị A rồi import trên thiết bị B. Dữ liệu gồm progress, status, bookmarks và settings.</p><p>${lastSync ? `Lần import gần nhất: ${esc(new Date(lastSync).toLocaleString())}` : 'Chưa import snapshot trên thiết bị này.'}</p><div class="los-toolbar"><button id="los-export" class="los-action" type="button">Export sync file</button><label class="los-action">Import sync file<input id="los-import-file" type="file" accept="application/json" hidden></label><button id="los-copy-sync" class="los-action" type="button">Copy sync package</button></div><textarea id="los-sync-text" class="los-textarea" placeholder="Paste sync package JSON từ thiết bị khác vào đây…"></textarea><button id="los-import-text" class="los-action" type="button">Import pasted package</button></section>`;
      body.querySelector('#los-export').onclick = downloadSnapshot;
      body.querySelector('#los-copy-sync').onclick = async () => { const text = JSON.stringify(exportSnapshot()); body.querySelector('#los-sync-text').value = text; try { await navigator.clipboard.writeText(text); toast('Đã copy sync package.'); } catch { toast('Sync package đã hiển thị để copy.'); } };
      body.querySelector('#los-import-file').onchange = async event => { try { const text = await event.target.files[0].text(); const count = importSnapshot(JSON.parse(text)); toast(`Đã import ${count} mục dữ liệu.`); setTimeout(() => location.reload(), 500); } catch { toast('Sync file không hợp lệ.'); } };
      body.querySelector('#los-import-text').onclick = () => { try { const count = importSnapshot(JSON.parse(body.querySelector('#los-sync-text').value)); toast(`Đã import ${count} mục dữ liệu.`); setTimeout(() => location.reload(), 500); } catch { toast('Sync package không hợp lệ.'); } };
    } else if (tab === 'offline') {
      body.innerHTML = `<section class="los-tool-section"><h3>PWA / Offline</h3><p>App shell được cache tự động. Markdown/PDF đã mở sẽ được service worker cache để đọc lại khi mất mạng; bạn cũng có thể bấm “Lưu offline” trong reader.</p><div class="los-toolbar"><button id="los-install-app" class="los-action los-install ${LOS.installPrompt ? 'visible' : ''}" type="button">Cài Study Shelf</button><button id="los-cache-indexes" class="los-action" type="button">Cache search & graph</button></div><p id="los-online-state">${navigator.onLine ? 'Online' : 'Offline'} · service worker ${'serviceWorker' in navigator ? 'được hỗ trợ' : 'không được hỗ trợ'}.</p></section>`;
      const install = body.querySelector('#los-install-app');
      install.onclick = async () => { if (!LOS.installPrompt) return; LOS.installPrompt.prompt(); await LOS.installPrompt.userChoice; LOS.installPrompt = null; install.classList.remove('visible'); };
      body.querySelector('#los-cache-indexes').onclick = async () => { try { const cache = await caches.open('study-shelf-user-v1'); await cache.addAll(['./library/search-index.json','./library/graph.json','./library/library.json']); toast('Đã cache index cho offline.'); } catch { toast('Không thể cache index.'); } };
    }
  }

  function installTopbar() {
    const actions = document.querySelector('.topbar-actions');
    if (!actions || document.querySelector('#los-open')) return;
    const button = document.createElement('button');
    button.id = 'los-open';
    button.className = 'los-topbar-button';
    button.type = 'button';
    button.textContent = 'Learning OS';
    button.onclick = () => openModal('bookmarks');
    actions.prepend(button);
  }

  function scheduleEnhance() {
    if (LOS.enhanceQueued) return;
    LOS.enhanceQueued = true;
    requestAnimationFrame(() => {
      LOS.enhanceQueued = false;
      installTopbar();
      const path = routePath();
      if (!path && LOS.readerPath) {
        LOS.readerCleanup();
        LOS.readerCleanup = () => {};
        LOS.readerPath = '';
      }
      if (document.querySelector('#search')) enhanceHome();
      if (path) enhanceReader(path);
    });
  }

  async function registerServiceWorker() {
    if (!('serviceWorker' in navigator)) return;
    try { await navigator.serviceWorker.register('./sw.js', { scope: './' }); }
    catch {}
  }

  async function init() {
    try {
      const response = await fetch('./library/library.json');
      LOS.docs = (await response.json()).documents || [];
    } catch { return; }
    installTopbar();
    scheduleEnhance();
    const app = document.querySelector('#app');
    if (app) new MutationObserver(scheduleEnhance).observe(app, { childList: true, subtree: true });
    addEventListener('hashchange', scheduleEnhance);
    addEventListener('online', () => toast('Đã online trở lại.'));
    addEventListener('offline', () => toast('Đang offline. Tài liệu đã cache vẫn đọc được.'));
    addEventListener('beforeinstallprompt', event => { event.preventDefault(); LOS.installPrompt = event; });
    registerServiceWorker();
  }

  init();
})();
