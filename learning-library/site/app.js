const app = document.querySelector('#app');
const state = { docs: [], query: '', filter: 'all', format: 'all' };
const escapeHtml = value => String(value).replace(/[&<>'"]/g, char => ({ '&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;' })[char]);
const fileUrl = path => `./library/files/${path.split('/').map(encodeURIComponent).join('/')}`;
const titleOf = doc => doc.title || doc.path.split('/').pop().replace(/\.[^.]+$/, '');

function formatSize(bytes) { return bytes < 1024 * 1024 ? `${Math.ceil(bytes / 1024)} KB` : `${(bytes / 1024 / 1024).toFixed(1)} MB`; }
function renderHome() {
  app.replaceChildren(document.querySelector('#home-template').content.cloneNode(true));
  const search = document.querySelector('#search');
  search.value = state.query;
  search.addEventListener('input', event => { state.query = event.target.value; renderCards(); });
  window.addEventListener('keydown', event => { if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') { event.preventDefault(); search.focus(); } }, { once: true });
  renderFormats(); renderFilters(); renderCards();
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
  const docs = state.docs.filter(doc => (state.filter === 'all' || doc.category === state.filter) && (state.format === 'all' || doc.type === state.format) && (!term || `${titleOf(doc)} ${doc.path} ${doc.category} ${doc.language || ''}`.toLowerCase().includes(term)));
  document.querySelector('#result-count').textContent = `${docs.length}개 자료`;
  document.querySelector('#document-grid').innerHTML = docs.length ? docs.map(doc => `<a class="doc-card" href="#/read/${encodeURIComponent(doc.path)}"><div class="doc-meta"><span class="type-badge">${doc.type}</span><span>${formatSize(doc.size)}</span></div><h3>${escapeHtml(titleOf(doc))}</h3><p class="doc-language">${escapeHtml(doc.language || 'vi')} · ${escapeHtml(doc.rights || 'author-confirmed')}</p><p class="doc-path">${escapeHtml(doc.category)} / ${escapeHtml(doc.path)}</p></a>`).join('') : '<p class="empty">Không có tài liệu phù hợp. Hãy thử đổi bộ lọc hoặc tìm kiếm khác.</p>';
}
function markdownToHtml(markdown) {
  const blocks = escapeHtml(markdown).replace(/\r/g, '').split('\n'); let html = '', inCode = false, code = [], inList = false;
  const inline = text => text.replace(/`([^`]+)`/g, '<code>$1</code>').replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>').replace(/\*([^*]+)\*/g, '<em>$1</em>').replace(/\[([^\]]+)\]\((https?:\/\/[^ )]+)\)/g, '<a href="$2" target="_blank" rel="noreferrer">$1</a>');
  for (const line of blocks) { if (line.startsWith('```')) { if (inCode) html += `<pre><code>${code.join('\n')}</code></pre>`; inCode = !inCode; code = []; continue; } if (inCode) { code.push(line); continue; } const heading = line.match(/^(#{1,3})\s+(.+)/); if (heading) { const text = heading[2]; const id = text.toLowerCase().replace(/[^\w가-힣]+/g, '-'); html += `<h${heading[1].length} id="${id}">${inline(text)}</h${heading[1].length}>`; continue; } if (/^[-*+]\s+/.test(line)) { if (!inList) { html += '<ul>'; inList = true; } html += `<li>${inline(line.replace(/^[-*+]\s+/, ''))}</li>`; continue; } if (inList) { html += '</ul>'; inList = false; } if (line.startsWith('&gt; ')) { html += `<blockquote>${inline(line.slice(5))}</blockquote>`; } else if (line.trim()) { html += `<p>${inline(line)}</p>`; } }
  if (inList) html += '</ul>'; if (inCode) html += `<pre><code>${code.join('\n')}</code></pre>`; return html;
}
async function renderReader(path) {
  const doc = state.docs.find(item => item.path === path); if (!doc) { location.hash = '#/'; return; }
  app.innerHTML = `<div class="reader-layout"><aside class="reader-aside"><a class="back-link" href="#/">← 서재로 돌아가기</a><nav id="toc" class="toc"></nav></aside><article class="reader"><header class="reader-header"><p class="eyebrow">${doc.type} · ${escapeHtml(doc.category)}</p><h1>${escapeHtml(titleOf(doc))}</h1><p class="muted">${escapeHtml(doc.path)} · ${formatSize(doc.size)}</p></header><div id="content"></div></article></div>`;
  const content = document.querySelector('#content');
  if (doc.type === 'PDF') { content.innerHTML = `<iframe class="pdf-frame" title="${escapeHtml(titleOf(doc))}" src="${fileUrl(doc.path)}#view=FitH"></iframe><div class="reader-actions"><a class="open-file" href="${fileUrl(doc.path)}" target="_blank" rel="noreferrer">Mở PDF ở tab mới ↗</a><a class="open-file" href="${fileUrl(doc.path)}" download>Tải PDF xuống ↓</a></div>`; return; }
  try { const response = await fetch(fileUrl(doc.path)); if (!response.ok) throw new Error(); const markdown = await response.text(); content.className = 'markdown'; content.innerHTML = markdownToHtml(markdown); const headings = [...content.querySelectorAll('h1,h2,h3')]; document.querySelector('#toc').innerHTML = headings.map(h => `<a href="#${h.id}">${escapeHtml(h.textContent)}</a>`).join(''); content.insertAdjacentHTML('beforeend', `<a class="open-file" href="${fileUrl(doc.path)}" target="_blank" rel="noreferrer">Mở Markdown gốc ↗</a>`); } catch { content.innerHTML = '<p class="empty">Không thể tải tài liệu. Hãy chạy lại build và kiểm tra đường dẫn trong library.config.json.</p>'; }
}
function route() { const match = location.hash.match(/^#\/read\/(.+)$/); match ? renderReader(decodeURIComponent(match[1])) : renderHome(); }
async function start() { try { const response = await fetch('./library/library.json'); state.docs = (await response.json()).documents; } catch { app.innerHTML = '<p class="empty">자료 목록을 찾을 수 없습니다. <code>npm run build:library</code>를 먼저 실행해 주세요.</p>'; return; } route(); }
document.querySelector('#theme-toggle').onclick = () => { document.documentElement.classList.toggle('dark'); localStorage.setItem('study-shelf-theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light'); };
if (localStorage.getItem('study-shelf-theme') === 'dark') document.documentElement.classList.add('dark');
window.addEventListener('hashchange', route); start();
