(() => {
  const LOS = {
    docs: [],
    metaSearch: null,
    searchIndex: null,
    graph: null,
    installPrompt: null,
    readerPath: '',
    readerCleanup: () => {},
    selectionTranslatorInstalled: false,
    enhanceQueued: false
  };

  const esc = value => String(value ?? '').replace(/[&<>'"]/g, char => ({ '&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;' })[char]);
  const norm = value => String(value ?? '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().trim();
  const fileUrl = path => `./library/files/${path.split('/').map(encodeURIComponent).join('/')}`;
  const docStateKey = path => `study-shelf-doc-state:${path}`;
  const progressKey = path => `study-shelf-progress:${path}`;
  const bookmarksKey = path => `study-shelf-section-bookmarks:${path}`;
  const readLaterKey = 'study-shelf-read-later';
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
  function readLaterItems() {
    const value = readJson(readLaterKey, []);
    return Array.isArray(value) ? value.filter(item => item && typeof item.path === 'string') : [];
  }
  function isReadLater(path) {
    return readLaterItems().some(item => item.path === path);
  }
  function readLaterDocuments() {
    return readLaterItems()
      .map(item => ({ item, doc: docByPath(item.path) }))
      .filter(entry => entry.doc)
      .sort((a, b) => new Date(b.item.savedAt || 0) - new Date(a.item.savedAt || 0));
  }
  function setReadLater(path, force) {
    const items = readLaterItems();
    const index = items.findIndex(item => item.path === path);
    const shouldAdd = typeof force === 'boolean' ? force : index < 0;
    if (shouldAdd && index < 0) items.unshift({ path, savedAt: new Date().toISOString() });
    if (!shouldAdd && index >= 0) items.splice(index, 1);
    writeJson(readLaterKey, items);
    window.dispatchEvent(new CustomEvent('study-shelf-read-later-change', { detail: { path, saved: shouldAdd } }));
    return shouldAdd;
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

  function installSelectionTranslator() {
    if (LOS.selectionTranslatorInstalled) return;
    LOS.selectionTranslatorInstalled = true;

    const popup = document.createElement('div');
    popup.id = 'los-translation-popup';
    popup.className = 'los-translation-popup';
    popup.setAttribute('role', 'dialog');
    popup.setAttribute('aria-label', 'Dịch nhanh sang tiếng Việt');
    popup.setAttribute('aria-hidden', 'true');
    document.body.append(popup);

    const cache = new Map();
    let selectionTimer = 0;
    let requestController = null;
    let requestId = 0;
    let currentText = '';
    let currentRect = null;

    const clearPopup = () => {
      clearTimeout(selectionTimer);
      requestController?.abort();
      requestController = null;
      currentText = '';
      currentRect = null;
      popup.classList.remove('open');
      popup.setAttribute('aria-hidden', 'true');
    };

    const googleTranslateUrl = text => `https://translate.google.com/?sl=auto&tl=vi&text=${encodeURIComponent(text)}&op=translate`;
    const detectSelectionLanguage = text => {
      const korean = (text.match(/[가-힣]/g) || []).length;
      const latin = (text.match(/[A-Za-z]/g) || []).length;
      if (korean && korean >= latin) return 'ko';
      if (latin) return 'en';
      return 'auto';
    };
    const translationTargets = language => language === 'ko'
      ? [['vi', 'Tiếng Việt'], ['en', 'English']]
      : language === 'en'
        ? [['vi', 'Tiếng Việt'], ['ko', '한국어']]
        : [['vi', 'Tiếng Việt']];
    const selectedReaderText = selection => {
      if (!selection || selection.isCollapsed || !selection.rangeCount) return null;
      const anchor = selection.anchorNode?.parentElement?.closest('.markdown');
      const focus = selection.focusNode?.parentElement?.closest('.markdown');
      if (!anchor || anchor !== focus) return null;
      const range = selection.getRangeAt(0);
      if (!anchor.contains(range.commonAncestorContainer)) return null;
      if (range.commonAncestorContainer.nodeType === Node.ELEMENT_NODE && range.commonAncestorContainer.closest('pre')) return null;
      const text = selection.toString().replace(/\s+/g, ' ').trim();
      if (!text || text.length > 240 || !/[A-Za-zÀ-ỹ가-힣]/.test(text)) return null;
      return { text, rect: range.getBoundingClientRect() };
    };
    const positionPopup = rect => {
      if (!rect) return;
      const width = popup.offsetWidth || Math.min(320, innerWidth - 24);
      const left = Math.max(12, Math.min(innerWidth - width - 12, rect.left + (rect.width / 2) - (width / 2)));
      const above = rect.top - popup.offsetHeight - 10;
      const top = above >= 12 ? above : Math.min(innerHeight - popup.offsetHeight - 12, rect.bottom + 10);
      popup.style.left = `${Math.round(left)}px`;
      popup.style.top = `${Math.max(12, Math.round(top))}px`;
    };
    const renderPopup = ({ text, translations = [], loading = false }) => {
      popup.replaceChildren();
      const head = document.createElement('div');
      head.className = 'los-translation-head';
      const label = document.createElement('span');
      label.textContent = 'Dịch nhanh';
      const close = document.createElement('button');
      close.type = 'button';
      close.className = 'los-translation-close';
      close.setAttribute('aria-label', 'Đóng bản dịch');
      close.textContent = '×';
      close.onclick = clearPopup;
      head.append(label, close);

      const source = document.createElement('div');
      source.className = 'los-translation-source';
      source.textContent = text;
      const results = document.createElement('div');
      results.className = 'los-translation-results';
      results.setAttribute('aria-live', 'polite');
      if (loading) {
        const result = document.createElement('div');
        result.className = 'los-translation-result';
        result.textContent = 'Đang dịch…';
        results.append(result);
      } else {
        translations.forEach(({ label, value, error }) => {
          const row = document.createElement('div');
          row.className = 'los-translation-row';
          const rowLabel = document.createElement('span');
          rowLabel.className = 'los-translation-label';
          rowLabel.textContent = label;
          const rowValue = document.createElement('span');
          rowValue.className = `los-translation-value${error ? ' error' : ''}`;
          rowValue.textContent = value || 'Không có bản dịch.';
          row.append(rowLabel, rowValue);
          results.append(row);
        });
      }

      const footer = document.createElement('div');
      footer.className = 'los-translation-footer';
      const note = document.createElement('span');
      note.textContent = 'Dịch máy';
      const fallback = document.createElement('a');
      fallback.href = googleTranslateUrl(text);
      fallback.target = '_blank';
      fallback.rel = 'noreferrer';
      fallback.textContent = 'Mở Google Translate ↗';
      footer.append(note, fallback);
      popup.append(head, source, results, footer);
      popup.classList.add('open');
      popup.setAttribute('aria-hidden', 'false');
      requestAnimationFrame(() => positionPopup(currentRect));
    };
    const translate = async text => {
      const language = detectSelectionLanguage(text);
      const targets = translationTargets(language);
      const cacheKey = (target, source) => `${source}:${target}:${text}`;
      const cached = targets.map(([target, label]) => ({ label, value: cache.get(cacheKey(target, language)), target })).filter(item => item.value);
      if (cached.length === targets.length) {
        renderPopup({ text, translations: cached });
        return;
      }
      requestController?.abort();
      requestController = new AbortController();
      const thisRequest = ++requestId;
      let results;
      try {
        results = await Promise.all(targets.map(async ([target, label]) => {
          const key = cacheKey(target, language);
          const existing = cache.get(key);
          if (existing) return { label, value: existing, target };
          try {
            const url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=${language}&tl=${target}&dt=t&q=${encodeURIComponent(text)}`;
            const response = await fetch(url, { signal: requestController.signal, credentials: 'omit' });
            if (!response.ok) throw new Error('translation unavailable');
            const payload = await response.json();
            const value = Array.isArray(payload?.[0]) ? payload[0].map(part => part?.[0] || '').join('').trim() : '';
            if (!value) throw new Error('empty translation');
            cache.set(key, value);
            return { label, value, target };
          } catch (error) {
            if (error?.name === 'AbortError') throw error;
            return { label, value: 'Không thể dịch lúc này.', target, error: true };
          }
        }));
      } catch (error) {
        if (error?.name === 'AbortError') return;
        throw error;
      }
      if (thisRequest !== requestId || text !== currentText || requestController.signal.aborted) return;
      renderPopup({ text, translations: results });
    };
    const showSelection = () => {
      const selected = selectedReaderText(window.getSelection());
      if (!selected) {
        clearPopup();
        return;
      }
      currentText = selected.text;
      currentRect = selected.rect;
      renderPopup({ text: selected.text, loading: true });
      translate(selected.text);
    };
    const scheduleSelection = () => {
      clearTimeout(selectionTimer);
      selectionTimer = setTimeout(showSelection, 120);
    };
    const onPointerDown = event => {
      if (!popup.contains(event.target)) clearPopup();
    };
    const onSelectionChange = () => {
      if (window.getSelection()?.isCollapsed) clearPopup();
      else scheduleSelection();
    };
    const onScroll = () => { if (popup.classList.contains('open')) clearPopup(); };
    document.addEventListener('mousedown', onPointerDown);
    document.addEventListener('selectionchange', onSelectionChange);
    window.addEventListener('scroll', onScroll, { passive: true });
    LOS.selectionTranslatorCleanup = () => {
      clearPopup();
      popup.remove();
      document.removeEventListener('mousedown', onPointerDown);
      document.removeEventListener('selectionchange', onSelectionChange);
      window.removeEventListener('scroll', onScroll);
    };
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
      if (card.querySelector('.los-card-meta')) {
        const shell = card.closest('.doc-card-shell');
        const path = shell?.dataset.path;
        const button = shell?.querySelector('.los-card-read-later');
        if (path && button) updateReadLaterButton(button, path);
        return;
      }
      const match = card.getAttribute('href')?.match(/^#\/read\/([^?]+)/);
      if (!match) return;
      const path = decodeURIComponent(match[1]);
      const state = readDocState(path);
      const pct = percentFor(path);
      const shell = document.createElement('div');
      shell.className = 'doc-card-shell';
      shell.dataset.path = path;
      card.replaceWith(shell);
      shell.append(card);
      const meta = document.createElement('div');
      meta.className = 'los-card-meta';
      meta.innerHTML = `<span class="los-status-chip">${esc(statusLabels[state.status] || statusLabels.unread)}</span>${pct ? `<span class="los-card-progress">${Math.round(pct)}%</span>` : ''}`;
      card.append(meta);
      const later = document.createElement('button');
      later.type = 'button';
      later.className = 'los-card-read-later';
      later.dataset.path = path;
      later.onclick = event => {
        event.preventDefault();
        event.stopPropagation();
        setReadLater(path);
      };
      shell.append(later);
      updateReadLaterButton(later, path);
    });
  }

  function updateReadLaterButton(button, path) {
    const saved = isReadLater(path);
    button.textContent = saved ? '★ Đã lưu đọc sau' : '☆ Đọc sau';
    button.setAttribute('aria-pressed', String(saved));
    button.classList.toggle('active', saved);
    button.setAttribute('aria-label', saved ? 'Bỏ khỏi danh sách đọc sau' : 'Lưu vào danh sách đọc sau');
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
    const readLater = readLaterDocuments();
    const recentBody = recent.length ? `<div class="los-list">${recent.map(({ doc, pct, state }) => `<a class="los-item" href="${hrefFor(doc.path)}"><strong>${esc(doc.title)}</strong><span>${esc(statusLabels[state.status] || '')} · ${Math.round(pct)}%</span><div class="los-progress"><i style="width:${pct}%"></i></div></a>`).join('')}</div>` : '<p class="los-empty">Chưa có lịch sử đọc.</p>';
    const bookmarkBody = bookmarks.length ? `<div class="los-list">${bookmarks.map(item => docMiniItem(docByPath(item.path), item.title || 'Bookmark', item.headingId || '')).join('')}</div>` : '<p class="los-empty">Chưa có bookmark.</p>';
    const reviewBody = review.length ? `<div class="los-list">${review.map(doc => docMiniItem(doc, 'Cần ôn lại')).join('')}</div>` : '<p class="los-empty">Review queue đang trống.</p>';
    const readLaterBody = readLater.length ? `<div class="los-list">${readLater.slice(0, 6).map(({ doc, item }) => docMiniItem(doc, `Đã lưu ${new Date(item.savedAt).toLocaleDateString()}`)).join('')}</div>` : '<p class="los-empty">Chưa có tài liệu nào.</p>';
    const section = document.createElement('section');
    section.id = 'los-dashboard';
    section.className = 'los-dashboard';
    section.innerHTML = `<div class="library-heading"><div><p class="eyebrow">LEARNING OS</p><h2>Tiếp tục học</h2></div><button class="los-action" type="button" data-los-open="read-later">Mở Learning OS</button></div><div class="los-dashboard-grid">${dashboardPanel('Continue Reading', recent.length, recentBody)}${dashboardPanel('Đọc sau', readLater.length, readLaterBody)}${dashboardPanel('Global Bookmarks', readAllBookmarks().length, bookmarkBody)}${dashboardPanel('Review Queue', LOS.docs.filter(doc => readDocState(doc.path).status === 'review').length, reviewBody)}</div>`;
    home.before(section);
    section.querySelector('[data-los-open]').onclick = () => openModal('read-later');
  }

  function renderLibrarySummary() {
    const searchBox = document.querySelector('.search-box');
    if (!searchBox || document.querySelector('#los-library-summary')) return;
    const categories = new Set(LOS.docs.map(doc => doc.category).filter(Boolean)).size;
    const folders = new Set(LOS.docs.map(doc => doc.folder).filter(Boolean)).size;
    const summary = document.createElement('div');
    summary.id = 'los-library-summary';
    summary.className = 'los-library-summary';
    summary.innerHTML = `<span><strong>${LOS.docs.length.toLocaleString()}</strong> tài liệu</span><span><strong>${categories}</strong> lĩnh vực</span><span><strong>${folders}</strong> thư mục</span>`;
    searchBox.before(summary);
  }

  let searchTimer = 0;
  let searchRequestId = 0;

  function metadataSearch(query) {
    const q = norm(query);
    const terms = q.split(/\s+/).filter(Boolean);
    if (!LOS.metaSearch) {
      LOS.metaSearch = LOS.docs.map(item => {
        const title = norm(item.title);
        const context = norm(`${item.displayPath || item.path} ${item.category || ''} ${item.language || ''}`);
        return { item, title, context, haystack: `${title} ${context}` };
      });
    }
    return LOS.metaSearch
      .map(entry => {
        if (terms.some(term => !entry.haystack.includes(term))) return null;
        let score = 0;
        terms.forEach(term => {
          if (entry.title.includes(term)) score += 12;
          if (entry.context.includes(term)) score += 4;
        });
        return { item: entry.item, score, snippet: '' };
      })
      .filter(Boolean)
      .sort((a, b) => b.score - a.score || a.item.title.localeCompare(b.item.title));
  }

  function renderSearchResults(target, results, total, label, deepQuery = '') {
    const visible = results.slice(0, 20);
    const list = visible.length ? visible.map(({ item, snippet }) => `<a class="los-search-result" href="${hrefFor(item.path)}"><strong>${esc(item.title)}</strong><small>${esc(item.displayPath || item.path)}</small>${snippet ? `<p>${esc(snippet)}</p>` : ''}</a>`).join('') : '<p class="los-empty los-search-empty">Không tìm thấy tài liệu phù hợp.</p>';
    const deepAction = deepQuery ? `<div class="los-search-footer"><span>Tìm nhanh dùng catalog nhẹ.</span><button class="los-deep-search" type="button">Tìm sâu trong nội dung</button></div>` : '';
    target.innerHTML = `<div class="los-search-head"><span>${esc(label)}</span><span>${visible.length}${total > 20 ? '+' : ''} kết quả</span></div><div class="los-search-list">${list}</div>${deepAction}`;
    if (deepQuery) target.querySelector('.los-deep-search').onclick = () => runDeepSearch(deepQuery, target);
  }

  async function runDeepSearch(query, target) {
    const requestId = ++searchRequestId;
    const q = norm(query);
    if (q.length < 2) return;
    target.innerHTML = '<div class="los-search-head"><span>Đang tải tìm kiếm nội dung…</span><span>chỉ lần này</span></div><p class="los-search-loading">Catalog nhanh vẫn dùng được mà không cần tải index này.</p>';
    try {
      const index = await loadSearchIndex();
      if (requestId !== searchRequestId) return;
      const terms = q.split(/\s+/).filter(Boolean);
      const scored = [];
      for (let position = 0; position < index.length; position += 1) {
        if (position && position % 120 === 0) {
          await new Promise(resolve => requestAnimationFrame(resolve));
          if (requestId !== searchRequestId) return;
        }
        const item = index[position];
        const title = norm(item.title);
        const path = norm(`${item.displayPath || item.path} ${item.category || ''}`);
        const headings = norm((item.headings || []).map(h => h.text).join(' '));
        const text = norm(item.text || '');
        let score = 0;
        let matched = true;
        for (const term of terms) {
          let termScore = 0;
          if (title.includes(term)) termScore += 12;
          if (headings.includes(term)) termScore += 7;
          if (path.includes(term)) termScore += 4;
          if (text.includes(term)) termScore += 1;
          if (!termScore) { matched = false; break; }
          score += termScore;
        }
        if (!matched || !score) continue;
        const rawText = item.text || '';
        const first = terms.map(term => text.indexOf(term)).filter(pos => pos >= 0).sort((a,b) => a-b)[0] ?? 0;
        const start = Math.max(0, first - 90);
        const snippet = rawText.slice(start, start + 260);
        scored.push({ item, score, snippet });
      }
      scored.sort((a, b) => b.score - a.score || a.item.title.localeCompare(b.item.title));
      if (requestId !== searchRequestId) return;
      renderSearchResults(target, scored, scored.length, 'Tìm sâu trong nội dung');
    } catch {
      if (requestId === searchRequestId) target.innerHTML = '<p class="los-empty los-search-empty">Search index chưa sẵn sàng. Tìm nhanh theo tiêu đề vẫn hoạt động.</p>';
    }
  }

  function runGlobalSearch(query, target) {
    const q = norm(query);
    searchRequestId += 1;
    if (q.length < 2) { target.classList.remove('open'); target.innerHTML = ''; return; }
    target.classList.add('open');
    const results = metadataSearch(query);
    renderSearchResults(target, results, results.length, 'Tìm nhanh', query);
  }

  function enhanceSearch() {
    const input = document.querySelector('#search');
    const box = input?.closest('.search-box');
    if (!input || !box || document.querySelector('#los-global-search')) return;
    input.placeholder = `Tìm nhanh trong ${LOS.docs.length.toLocaleString()} tài liệu…`;
    const hint = document.createElement('p');
    hint.className = 'los-search-hint';
    hint.textContent = 'Tìm tiêu đề, đường dẫn và lĩnh vực ngay lập tức; chỉ tải index lớn khi bạn chọn tìm sâu.';
    const target = document.createElement('div');
    target.id = 'los-global-search';
    target.className = 'los-search-results';
    box.after(hint, target);
    input.addEventListener('input', () => {
      searchRequestId += 1;
      clearTimeout(searchTimer);
      searchTimer = setTimeout(() => runGlobalSearch(input.value, target), 180);
    });
    input.addEventListener('keydown', event => { if (event.key === 'Escape') target.classList.remove('open'); });
  }

  function enhanceHome() {
    renderHomeDashboard();
    renderLibrarySummary();
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

  function speechLanguage(doc) {
    const raw = String(doc.language || document.documentElement.lang || 'en').toLowerCase();
    const first = raw.split(/[-_,\s]+/)[0];
    return ['ko', 'vi', 'en', 'ja', 'zh', 'fr', 'de', 'es'].includes(first) ? first : 'en';
  }

  function speechBlocks(content, startAt = 0) {
    const clone = content.cloneNode(true);
    clone.querySelectorAll('pre,.open-file,.los-related').forEach(node => node.remove());
    const blocks = [...clone.querySelectorAll('h1,h2,h3,p,li,blockquote,th,td')]
      .map(node => node.textContent.replace(/\s+/g, ' ').trim())
      .filter(Boolean);
    return (blocks.length ? blocks : [clone.textContent.replace(/\s+/g, ' ').trim()].filter(Boolean)).slice(startAt);
  }

  function visibleSpeechBlock(content) {
    const nodes = [...content.querySelectorAll('h1,h2,h3,p,li,blockquote,th,td')]
      .filter(node => !node.closest('.los-related'))
      .filter(node => node.textContent.replace(/\s+/g, ' ').trim());
    if (!nodes.length) return 0;
    const readingLine = Math.min(180, Math.max(84, window.innerHeight * 0.18));
    const index = nodes.findIndex(node => node.getBoundingClientRect().bottom > readingLine);
    return index < 0 ? nodes.length - 1 : index;
  }

  function speechChunks(blocks, maxLength = 1100) {
    const chunks = [];
    let current = '';
    const flush = () => {
      if (current) chunks.push(current);
      current = '';
    };
    blocks.forEach(block => {
      let rest = block;
      while (rest.length > maxLength) {
        let boundary = rest.lastIndexOf(' ', maxLength);
        if (boundary < Math.floor(maxLength * 0.6)) boundary = maxLength;
        const part = rest.slice(0, boundary).trim();
        if (part) chunks.push(part);
        rest = rest.slice(boundary).trim();
      }
      if (!rest) return;
      const candidate = current ? `${current} ${rest}` : rest;
      if (candidate.length > maxLength) {
        flush();
        current = rest;
      } else {
        current = candidate;
      }
    });
    flush();
    return chunks;
  }

  function enhanceSpeechReader(doc, content, path) {
    const toolbar = document.querySelector('#reader-toolbar');
    if (!toolbar || !content || document.querySelector('#los-speech-controls')) return;
    if (!('speechSynthesis' in window) || !('SpeechSynthesisUtterance' in window)) return;
    const title = document.querySelector('.reader-header h1')?.textContent.replace(/\s+/g, ' ').trim();
    const allBlocks = speechBlocks(content);
    const blocks = allBlocks.slice();
    if (title && blocks[0] !== title) blocks.unshift(title);
    let chunks = speechChunks(blocks);
    if (!chunks.length) return;

    const synth = window.speechSynthesis;
    const language = speechLanguage(doc);
    const controls = document.createElement('div');
    controls.id = 'los-speech-controls';
    controls.className = 'los-speech-controls';
    controls.innerHTML = `<button class="los-action" id="los-speech-start" type="button">🔊 Đọc trang</button><button class="los-action" id="los-speech-pause" type="button" disabled>⏸ Tạm dừng</button><button class="los-action" id="los-speech-stop" type="button" disabled>■ Dừng</button><label class="los-speech-rate"><span>Tốc độ</span><select class="los-select" id="los-speech-rate"><option value="0.8">0,8×</option><option value="1">1×</option><option value="1.2">1,2×</option><option value="1.5">1,5×</option></select></label><span class="los-speech-status" id="los-speech-status" aria-live="polite">Sẵn sàng · ${chunks.length} đoạn</span>`;
    toolbar.append(controls);

    const startButton = controls.querySelector('#los-speech-start');
    const pauseButton = controls.querySelector('#los-speech-pause');
    const stopButton = controls.querySelector('#los-speech-stop');
    const rateSelect = controls.querySelector('#los-speech-rate');
    const status = controls.querySelector('#los-speech-status');
    const edgeActions = document.querySelector('.reader-edge-actions');
    let edgeSpeech = edgeActions?.querySelector('#edge-speech') || null;
    if (edgeActions && !edgeSpeech) {
      edgeSpeech = document.createElement('button');
      edgeSpeech.id = 'edge-speech';
      edgeSpeech.className = 'edge-button';
      edgeSpeech.type = 'button';
      edgeActions.prepend(edgeSpeech);
    }
    const savedRate = Number(readJson('study-shelf-speech-rate', 1));
    if ([0.8, 1, 1.2, 1.5].includes(savedRate)) rateSelect.value = String(savedRate);

    let chunkIndex = 0;
    let active = false;
    let paused = false;
    let runId = 0;

    const setStatus = message => { status.textContent = message; };
    const updateButtons = () => {
      startButton.disabled = active;
      pauseButton.disabled = !active;
      stopButton.disabled = !active;
      pauseButton.textContent = paused ? '▶ Tiếp tục' : '⏸ Tạm dừng';
      if (edgeSpeech) {
        edgeSpeech.textContent = active ? (paused ? '▶' : '⏸') : '🔊';
        edgeSpeech.setAttribute('aria-label', active ? (paused ? 'Tiếp tục đọc' : 'Tạm dừng đọc') : 'Đọc từ vị trí hiện tại');
        edgeSpeech.title = active ? (paused ? 'Tiếp tục đọc' : 'Tạm dừng đọc') : 'Đọc từ vị trí hiện tại';
        edgeSpeech.classList.toggle('active', active);
      }
    };
    const pickVoice = () => {
      const voices = synth.getVoices();
      return voices.find(voice => voice.lang?.toLowerCase() === language)
        || voices.find(voice => voice.lang?.toLowerCase().startsWith(`${language}-`));
    };
    const speakNext = () => {
      if (!active || paused || routePath() !== path) return;
      if (chunkIndex >= chunks.length) {
        active = false;
        paused = false;
        updateButtons();
        setStatus('Đã đọc xong trang.');
        return;
      }
      const currentRun = runId;
      const utterance = new SpeechSynthesisUtterance(chunks[chunkIndex]);
      const voice = pickVoice();
      utterance.lang = voice?.lang || language;
      if (voice) utterance.voice = voice;
      utterance.rate = Number(rateSelect.value) || 1;
      utterance.onstart = () => setStatus(`Đang đọc · ${chunkIndex + 1}/${chunks.length}`);
      utterance.onend = () => {
        if (currentRun !== runId || !active) return;
        chunkIndex += 1;
        speakNext();
      };
      utterance.onerror = event => {
        if (currentRun !== runId || ['canceled', 'interrupted'].includes(event.error)) return;
        active = false;
        paused = false;
        updateButtons();
        setStatus('Không thể đọc trên trình duyệt này.');
      };
      try {
        synth.speak(utterance);
      } catch {
        active = false;
        paused = false;
        updateButtons();
        setStatus('Không thể khởi động đọc chữ.');
      }
    };
    const start = (fromCurrent = false) => {
      const sourceBlocks = fromCurrent ? speechBlocks(content, visibleSpeechBlock(content)) : blocks;
      chunks = speechChunks(sourceBlocks);
      if (!chunks.length) return;
      runId += 1;
      synth.cancel();
      chunkIndex = 0;
      active = true;
      paused = false;
      updateButtons();
      setStatus(`Đang chuẩn bị · ${chunks.length} đoạn`);
      window.setTimeout(speakNext, 0);
    };
    const togglePause = () => {
      if (!active) return;
      if (paused) {
        paused = false;
        if (synth.speaking || synth.pending) synth.resume();
        else speakNext();
        setStatus(`Đang đọc · ${chunkIndex + 1}/${chunks.length}`);
      } else {
        paused = true;
        synth.pause();
        setStatus('Đã tạm dừng.');
      }
      updateButtons();
    };
    const stop = () => {
      runId += 1;
      synth.cancel();
      active = false;
      paused = false;
      updateButtons();
      setStatus('Đã dừng.');
    };

    startButton.textContent = '🔊 Đọc từ đây';
    startButton.onclick = () => start(true);
    pauseButton.onclick = togglePause;
    stopButton.onclick = stop;
    if (edgeSpeech) edgeSpeech.onclick = () => active ? togglePause() : start(true);
    rateSelect.onchange = () => writeJson('study-shelf-speech-rate', Number(rateSelect.value));
    synth.addEventListener?.('voiceschanged', pickVoice);
    updateButtons();

    const previousCleanup = LOS.readerCleanup;
    LOS.readerCleanup = () => {
      previousCleanup();
      stop();
      synth.removeEventListener?.('voiceschanged', pickVoice);
    };
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
      controls.innerHTML = `<label><span class="sr-only">Reading status</span><select id="los-status" class="los-select"><option value="unread">Chưa đọc</option><option value="reading">Đang đọc</option><option value="review">Cần ôn lại</option><option value="completed">Hoàn thành</option></select></label><button id="los-read-later" class="los-action" type="button"></button><button id="los-offline" class="los-action" type="button">↓ Lưu offline</button><button id="los-tools" class="los-action" type="button">Learning OS</button><span class="los-offline-badge">Progress ${Math.round(percentFor(path))}%</span>`;
      header.append(controls);
      const select = controls.querySelector('#los-status');
      select.value = state.status || 'reading';
      select.onchange = () => {
        const patch = { status: select.value, lastOpened: new Date().toISOString() };
        if (select.value === 'completed') patch.progressPct = 100;
        writeDocState(path, patch);
        toast(`Trạng thái: ${statusLabels[select.value]}`);
      };
      const later = controls.querySelector('#los-read-later');
      later.onclick = () => {
        const saved = setReadLater(path);
        updateReadLaterButton(later, path);
        toast(saved ? 'Đã thêm vào danh sách đọc sau.' : 'Đã bỏ khỏi danh sách đọc sau.');
      };
      updateReadLaterButton(later, path);
      controls.querySelector('#los-offline').onclick = () => cacheDocument(doc);
      controls.querySelector('#los-tools').onclick = () => openModal('bookmarks');
    }

    const content = document.querySelector('.markdown');
    if (content) {
      linkifyInternalMarkdown(content, path);
      renderRelated(doc, content);
      enhanceSpeechReader(doc, content, path);
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
    modal.innerHTML = `<button class="los-backdrop" type="button" aria-label="Đóng Learning OS"></button><section class="los-sheet" role="dialog" aria-modal="true" aria-label="Learning OS"><header class="los-sheet-head"><h2>Learning OS</h2><button class="los-close" type="button" aria-label="Đóng">×</button></header><nav class="los-tabs"><button class="los-tab" data-tab="read-later">Đọc sau</button><button class="los-tab" data-tab="bookmarks">Bookmarks</button><button class="los-tab" data-tab="review">Review</button><button class="los-tab" data-tab="graph">Graph</button><button class="los-tab" data-tab="sync">Sync</button><button class="los-tab" data-tab="offline">Offline</button></nav><div id="los-sheet-body" class="los-sheet-body"></div></section>`;
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
    if (tab === 'read-later') {
      const items = readLaterDocuments();
      body.innerHTML = `<section class="los-tool-section"><h3>Đọc sau</h3><p>${items.length} tài liệu đang chờ đọc. Danh sách chỉ lưu trên thiết bị này.</p><div class="los-list">${items.length ? items.map(({ doc, item }) => docMiniItem(doc, `Đã lưu ${new Date(item.savedAt).toLocaleDateString()}`)).join('') : '<p class="los-empty">Chưa có tài liệu nào. Bấm “☆ Đọc sau” khi đang xem tài liệu.</p>'}</div></section>`;
    } else if (tab === 'bookmarks') {
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
    installSelectionTranslator();
    scheduleEnhance();
    const app = document.querySelector('#app');
    if (app) new MutationObserver(scheduleEnhance).observe(app, { childList: true, subtree: true });
    addEventListener('hashchange', scheduleEnhance);
    addEventListener('study-shelf-read-later-change', scheduleEnhance);
    addEventListener('online', () => toast('Đã online trở lại.'));
    addEventListener('offline', () => toast('Đang offline. Tài liệu đã cache vẫn đọc được.'));
    addEventListener('beforeinstallprompt', event => { event.preventDefault(); LOS.installPrompt = event; });
    registerServiceWorker();
  }

  init();
})();
