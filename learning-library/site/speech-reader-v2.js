(() => {
  'use strict';

  const STORAGE_RATE = 'study-shelf-speech-rate';
  const STORAGE_VOICE_PREFIX = 'study-shelf-speech-voice:';
  const RATE_OPTIONS = [0.8, 1, 1.2, 1.5, 1.75, 2, 2.5, 3, 3.5, 4];
  const SUPPORTED_LANGS = ['vi', 'en', 'ko'];
  const VOICE_LOCALES = {
    vi: ['vi-VN', 'vi'],
    en: ['en-US', 'en-GB', 'en'],
    ko: ['ko-KR', 'ko']
  };
  const VOICE_NAME_PREFERENCES = {
    vi: ['linh', 'vietnam', 'google', 'microsoft', 'natural', 'premium', 'enhanced', 'neural'],
    en: ['samantha', 'ava', 'alex', 'google us english', 'microsoft', 'natural', 'premium', 'enhanced', 'neural'],
    ko: ['yuna', 'korean', 'google 한국의', 'microsoft', 'natural', 'premium', 'enhanced', 'neural']
  };
  const HANGUL_RE = /[\u1100-\u11ff\u3130-\u318f\uac00-\ud7af]/;
  const VIETNAMESE_RE = /[ăâđêôơưĂÂĐÊÔƠƯàáảãạằắẳẵặầấẩẫậèéẻẽẹềếểễệìíỉĩịòóỏõọồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ]/i;
  const ASCII_WORD_RE = /[A-Za-z]{2,}/;
  const ENGLISH_HINT_RE = /\b(the|and|or|of|to|in|for|with|from|by|as|is|are|be|this|that|model|system|data|value|cost|market|network|software|hardware|memory|process|thread|class|object|function|method|server|client|database|query|cache|event|state|type|pattern|framework|runtime|learning|reader|speech|voice)\b/i;

  const state = {
    path: '',
    content: null,
    controls: null,
    float: null,
    edgeButton: null,
    rateSelect: null,
    floatRateSelect: null,
    status: null,
    pauseButton: null,
    stopButton: null,
    startButton: null,
    voiceDetails: null,
    voiceSelects: new Map(),
    blocks: [],
    segments: [],
    index: 0,
    active: false,
    paused: false,
    runId: 0,
    highlighted: null,
    defaultLanguage: 'vi',
    docsPromise: null
  };

  const synth = window.speechSynthesis;

  function readJson(key, fallback = null) {
    try {
      return JSON.parse(localStorage.getItem(key) || 'null') ?? fallback;
    } catch {
      return fallback;
    }
  }

  function writeJson(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch {}
  }

  function routePath() {
    const match = location.hash.match(/^#\/read\/([^?]+)/);
    return match ? decodeURIComponent(match[1]) : '';
  }

  function normalizeLanguage(raw, fallback = 'vi') {
    const base = String(raw || '').toLowerCase().split(/[-_,\s]+/)[0];
    return SUPPORTED_LANGS.includes(base) ? base : fallback;
  }

  function loadDocs() {
    if (!state.docsPromise) {
      state.docsPromise = fetch('./library/library.json')
        .then(response => response.ok ? response.json() : { documents: [] })
        .then(data => data.documents || [])
        .catch(() => []);
    }
    return state.docsPromise;
  }

  async function languageForPath(path) {
    const docs = await loadDocs();
    const doc = docs.find(item => item.path === path);
    if (doc?.language) return normalizeLanguage(doc.language);

    const sample = state.content?.textContent?.slice(0, 5000) || '';
    const hangulCount = [...sample].filter(char => HANGUL_RE.test(char)).length;
    const vietnameseCount = [...sample].filter(char => VIETNAMESE_RE.test(char)).length;
    if (hangulCount > Math.max(8, vietnameseCount * 1.4)) return 'ko';
    if (vietnameseCount > 0) return 'vi';
    return 'en';
  }

  function speechNodes(content) {
    return [...content.querySelectorAll('h1,h2,h3,p,li,blockquote,th,td')]
      .filter(node => !node.closest('.los-related'))
      .filter(node => !node.closest('pre'))
      .filter(node => node.textContent.replace(/\s+/g, ' ').trim());
  }

  function visibleBlockIndex(blocks) {
    if (!blocks.length) return 0;

    const topbarBottom = document.querySelector('.topbar')?.getBoundingClientRect().bottom || 0;
    const viewportTop = Math.min(window.innerHeight - 1, topbarBottom + 10);
    const viewportBottom = Math.max(viewportTop + 1, window.innerHeight - 12);
    const readingLine = Math.min(
      viewportBottom - 1,
      viewportTop + Math.max(48, Math.min(150, (viewportBottom - viewportTop) * 0.22))
    );

    const visible = blocks
      .map((node, index) => ({ node, index, rect: node.getBoundingClientRect() }))
      .filter(item => item.rect.bottom > viewportTop && item.rect.top < viewportBottom);

    if (visible.length) {
      const crossing = visible.find(item => item.rect.top <= readingLine && item.rect.bottom > readingLine);
      if (crossing) return crossing.index;

      const below = visible.find(item => item.rect.top >= readingLine);
      if (below) return below.index;

      return visible[0].index;
    }

    const belowViewport = blocks.findIndex(node => node.getBoundingClientRect().bottom > viewportTop);
    return belowViewport >= 0 ? belowViewport : blocks.length - 1;
  }

  function cleanText(text) {
    return String(text || '').replace(/\s+/g, ' ').trim();
  }

  function pushPiece(out, text, language) {
    const value = cleanText(text);
    if (!value) return;
    const lang = normalizeLanguage(language);
    const previous = out[out.length - 1];
    if (previous && previous.lang === lang) {
      previous.text = cleanText(`${previous.text} ${value}`);
    } else {
      out.push({ text: value, lang });
    }
  }

  function splitHangulRuns(text, fallbackLanguage) {
    const tokens = String(text || '').match(/[\u1100-\u11ff\u3130-\u318f\uac00-\ud7af]+|[^\u1100-\u11ff\u3130-\u318f\uac00-\ud7af]+/g) || [];
    const out = [];

    for (const token of tokens) {
      const language = HANGUL_RE.test(token) ? 'ko' : fallbackLanguage;
      pushPiece(out, token, language);
    }
    return out;
  }

  function looksEnglishAscii(text) {
    const value = cleanText(text);
    if (!ASCII_WORD_RE.test(value) || VIETNAMESE_RE.test(value) || HANGUL_RE.test(value)) return false;
    if (/^[A-Z][A-Z0-9.+#/-]{1,11}$/.test(value)) return true;
    if (ENGLISH_HINT_RE.test(value)) return true;

    const words = value.match(/[A-Za-z]+/g) || [];
    return words.length >= 2 && words.some(word => word.length >= 6);
  }

  function splitTextLanguages(text, fallbackLanguage) {
    const value = String(text || '');
    if (!value.trim()) return [];

    const out = [];
    const parenPattern = /\(([^()]{1,140})\)/g;
    let cursor = 0;
    let match;

    const pushDefault = part => {
      splitHangulRuns(part, fallbackLanguage).forEach(piece => pushPiece(out, piece.text, piece.lang));
    };

    while ((match = parenPattern.exec(value))) {
      pushDefault(value.slice(cursor, match.index));
      const inner = match[1];
      if (looksEnglishAscii(inner)) pushPiece(out, inner, 'en');
      else pushDefault(match[0]);
      cursor = match.index + match[0].length;
    }

    pushDefault(value.slice(cursor));
    return out;
  }

  function elementLanguageOverride(element, fallbackLanguage) {
    const explicit = element.getAttribute?.('lang');
    if (explicit) return normalizeLanguage(explicit, fallbackLanguage);

    const tag = element.tagName;
    if (['CODE', 'KBD', 'SAMP'].includes(tag) && looksEnglishAscii(element.textContent)) return 'en';
    if (['STRONG', 'EM'].includes(tag) && fallbackLanguage === 'vi' && looksEnglishAscii(element.textContent)) return 'en';
    return fallbackLanguage;
  }

  function inlinePieces(node, fallbackLanguage) {
    const out = [];

    const walk = (current, language) => {
      if (current.nodeType === Node.TEXT_NODE) {
        splitTextLanguages(current.nodeValue, language).forEach(piece => pushPiece(out, piece.text, piece.lang));
        return;
      }
      if (current.nodeType !== Node.ELEMENT_NODE) return;

      const nextLanguage = elementLanguageOverride(current, language);
      if (nextLanguage !== language && ['CODE', 'KBD', 'SAMP', 'STRONG', 'EM'].includes(current.tagName)) {
        pushPiece(out, current.textContent, nextLanguage);
        return;
      }

      current.childNodes.forEach(child => walk(child, nextLanguage));
    };

    walk(node, fallbackLanguage);

    if (!out.length) {
      splitTextLanguages(node.textContent, fallbackLanguage).forEach(piece => pushPiece(out, piece.text, piece.lang));
    }
    return out;
  }

  function splitForTts(text, maxLength = 360) {
    const value = cleanText(text);
    if (!value) return [];
    if (value.length <= maxLength) return [value];

    const chunks = [];
    let rest = value;

    while (rest.length > maxLength) {
      const windowText = rest.slice(0, maxLength + 1);
      let boundary = Math.max(
        windowText.lastIndexOf('. '),
        windowText.lastIndexOf('! '),
        windowText.lastIndexOf('? '),
        windowText.lastIndexOf('; '),
        windowText.lastIndexOf(', ')
      );
      if (boundary < Math.floor(maxLength * 0.55)) boundary = windowText.lastIndexOf(' ', maxLength);
      if (boundary < Math.floor(maxLength * 0.45)) boundary = maxLength;
      else boundary += 1;

      const part = cleanText(rest.slice(0, boundary));
      if (part) chunks.push(part);
      rest = cleanText(rest.slice(boundary));
    }

    if (rest) chunks.push(rest);
    return chunks;
  }

  function buildSegments(blocks, startIndex, defaultLanguage) {
    const result = [];

    blocks.slice(startIndex).forEach(node => {
      const blockFallback = (
        defaultLanguage === 'vi'
        && /^H[1-3]$/.test(node.tagName)
        && looksEnglishAscii(node.textContent)
      ) ? 'en' : defaultLanguage;

      inlinePieces(node, blockFallback).forEach(piece => {
        splitForTts(piece.text).forEach(text => {
          result.push({ text, lang: piece.lang, node });
        });
      });
    });

    return result;
  }

  function voiceCandidates(language) {
    const base = normalizeLanguage(language);
    return synth.getVoices().filter(voice => normalizeLanguage(voice.lang, '') === base);
  }

  function voiceScore(voice, language) {
    const lang = normalizeLanguage(language);
    const lowerLang = String(voice.lang || '').toLowerCase();
    const lowerName = String(voice.name || '').toLowerCase();
    let score = 0;

    const localeIndex = VOICE_LOCALES[lang].findIndex(locale => lowerLang === locale.toLowerCase());
    if (localeIndex >= 0) score += 120 - localeIndex * 12;
    else if (lowerLang.startsWith(`${lang}-`) || lowerLang === lang) score += 80;

    const preferred = VOICE_NAME_PREFERENCES[lang] || [];
    preferred.forEach((hint, index) => {
      if (lowerName.includes(hint)) score += 35 - Math.min(index, 10);
    });

    if (voice.default) score += 8;
    if (voice.localService) score += 3;
    return score;
  }

  function selectedVoiceName(language) {
    return readJson(`${STORAGE_VOICE_PREFIX}${normalizeLanguage(language)}`, '');
  }

  function pickVoice(language) {
    const lang = normalizeLanguage(language);
    const candidates = voiceCandidates(lang);
    if (!candidates.length) return null;

    const preferredName = selectedVoiceName(lang);
    if (preferredName) {
      const exact = candidates.find(voice => voice.name === preferredName);
      if (exact) return exact;
    }

    return [...candidates].sort((a, b) => voiceScore(b, lang) - voiceScore(a, lang))[0] || null;
  }

  function rateValue() {
    const raw = Number(state.rateSelect?.value || readJson(STORAGE_RATE, 1));
    return RATE_OPTIONS.includes(raw) ? raw : 1;
  }

  function rateOptionsHtml(selected = 1) {
    return RATE_OPTIONS.map(rate => {
      const label = Number.isInteger(rate) ? `${rate}×` : `${String(rate).replace('.', ',')}×`;
      return `<option value="${rate}" ${rate === selected ? 'selected' : ''}>${label}</option>`;
    }).join('');
  }

  function ensureStyles() {
    if (document.querySelector('#los-speech-v2-style')) return;
    const style = document.createElement('style');
    style.id = 'los-speech-v2-style';
    style.textContent = `
      #los-speech-controls[data-reader-v2="true"]{position:relative;gap:8px}
      .los-speech-v2-voices{position:relative}
      .los-speech-v2-voices>summary{min-height:38px;display:inline-flex;align-items:center;padding:7px 10px;border:1px solid var(--line);border-radius:8px;background:var(--panel);color:var(--ink);cursor:pointer;list-style:none}
      .los-speech-v2-voices>summary::-webkit-details-marker{display:none}
      .los-speech-v2-voices[open]>summary{border-color:var(--accent);color:var(--accent)}
      .los-speech-v2-voice-panel{position:absolute;z-index:55;top:calc(100% + 7px);right:0;width:min(420px,calc(100vw - 36px));display:grid;gap:8px;padding:12px;border:1px solid var(--line);border-radius:12px;background:var(--panel);box-shadow:var(--shadow)}
      .los-speech-v2-voice-row{display:grid;grid-template-columns:72px minmax(0,1fr);align-items:center;gap:8px;color:var(--muted);font-size:.76rem}
      .los-speech-v2-voice-row .los-select{width:100%;min-width:0}
      .los-speech-v2-note{margin:0;color:var(--muted);font-size:.7rem;line-height:1.45}
      .los-speech-float{position:fixed;z-index:95;right:max(68px,calc(env(safe-area-inset-right) + 68px));top:50%;display:none;align-items:center;gap:6px;transform:translateY(-50%);padding:6px;border:1px solid color-mix(in srgb,var(--accent) 32%,var(--line));border-radius:999px;background:color-mix(in srgb,var(--panel) 94%,transparent);box-shadow:0 16px 46px #0003;backdrop-filter:blur(16px)}
      .los-speech-float.visible{display:flex}
      .los-speech-float button{width:38px;height:38px;padding:0;border:1px solid var(--line);border-radius:50%;background:var(--panel);color:var(--ink);cursor:pointer}
      .los-speech-float button:hover,.los-speech-float button:focus-visible{border-color:var(--accent);color:var(--accent)}
      .los-speech-float select{min-width:68px;height:38px;padding:0 7px;border:1px solid var(--line);border-radius:999px;background:var(--panel);color:var(--ink)}
      .los-speech-float-label{min-width:46px;padding:0 4px;color:var(--muted);font-size:.7rem;font-weight:800;text-align:center}
      .los-speaking-block{border-radius:7px;background:color-mix(in srgb,var(--accent-soft) 38%,transparent);box-shadow:0 0 0 4px color-mix(in srgb,var(--accent-soft) 38%,transparent)}
      @media(max-width:900px){
        .los-speech-float{top:auto;right:max(72px,calc(env(safe-area-inset-right) + 72px));bottom:calc(20px + env(safe-area-inset-bottom));transform:none}
      }
      @media(max-width:760px){
        .los-speech-v2-voices{flex:1 1 100%}
        .los-speech-v2-voices>summary{width:100%;justify-content:center}
        .los-speech-v2-voice-panel{position:fixed;left:12px;right:12px;bottom:calc(84px + env(safe-area-inset-bottom));top:auto;width:auto}
        .los-speech-float-label{display:none}
        .los-speech-float{right:max(68px,calc(env(safe-area-inset-right) + 68px));padding:5px}
        .los-speech-float button{width:42px;height:42px}
        .los-speech-float select{height:42px;min-width:64px}
      }
    `;
    document.head.append(style);
  }

  function ensureFloat() {
    if (state.float?.isConnected) return state.float;

    const selectedRate = rateValue();
    const node = document.createElement('div');
    node.id = 'los-speech-float';
    node.className = 'los-speech-float';
    node.setAttribute('role', 'group');
    node.setAttribute('aria-label', 'Điều khiển đọc nổi');
    node.innerHTML = `
      <span class="los-speech-float-label" id="los-speech-float-label">TTS</span>
      <button type="button" id="los-speech-float-pause" aria-label="Tạm dừng đọc" title="Tạm dừng đọc">⏸</button>
      <button type="button" id="los-speech-float-stop" aria-label="Dừng đọc" title="Dừng đọc">■</button>
      <select id="los-speech-float-rate" aria-label="Tốc độ đọc">${rateOptionsHtml(selectedRate)}</select>
    `;
    document.body.append(node);

    state.float = node;
    state.floatRateSelect = node.querySelector('#los-speech-float-rate');
    node.querySelector('#los-speech-float-pause').onclick = () => togglePause();
    node.querySelector('#los-speech-float-stop').onclick = () => stop('Đã dừng.');
    state.floatRateSelect.onchange = () => setRate(Number(state.floatRateSelect.value), true);
    return node;
  }

  function populateVoiceSelects() {
    if (!state.controls?.isConnected) return;

    const labels = { vi: 'Tiếng Việt', en: 'English', ko: '한국어' };
    for (const lang of SUPPORTED_LANGS) {
      const select = state.voiceSelects.get(lang);
      if (!select) continue;

      const candidates = voiceCandidates(lang).sort((a, b) => voiceScore(b, lang) - voiceScore(a, lang));
      const selected = selectedVoiceName(lang);
      select.innerHTML = `<option value="">Auto — voice tốt nhất</option>` + candidates
        .map(voice => `<option value="${escapeHtml(voice.name)}">${escapeHtml(voice.name)} · ${escapeHtml(voice.lang)}</option>`)
        .join('');
      if (selected && candidates.some(voice => voice.name === selected)) select.value = selected;
      else select.value = '';
      select.disabled = candidates.length === 0;
      select.setAttribute('aria-label', `Giọng ${labels[lang]}`);
    }
  }

  function escapeHtml(value) {
    return String(value ?? '').replace(/[&<>'"]/g, char => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;'
    })[char]);
  }

  function updateHighlight(node) {
    if (state.highlighted && state.highlighted !== node) state.highlighted.classList.remove('los-speaking-block');
    state.highlighted = node || null;
    state.highlighted?.classList.add('los-speaking-block');
  }

  function clearHighlight() {
    state.highlighted?.classList.remove('los-speaking-block');
    state.highlighted = null;
  }

  function statusText(message) {
    if (state.status) state.status.textContent = message;
  }

  function currentSegment() {
    return state.segments[state.index] || null;
  }

  function updateUi() {
    const active = state.active;
    const paused = state.paused;
    if (state.startButton) state.startButton.disabled = active;
    if (state.pauseButton) {
      state.pauseButton.disabled = !active;
      state.pauseButton.textContent = paused ? '▶ Tiếp tục' : '⏸ Tạm dừng';
    }
    if (state.stopButton) state.stopButton.disabled = !active;

    if (state.edgeButton) {
      state.edgeButton.textContent = active ? (paused ? '▶' : '⏸') : '🔊';
      state.edgeButton.classList.toggle('active', active);
      state.edgeButton.setAttribute('aria-label', active ? (paused ? 'Tiếp tục đọc' : 'Tạm dừng đọc') : 'Đọc từ màn hình hiện tại');
      state.edgeButton.title = active ? (paused ? 'Tiếp tục đọc' : 'Tạm dừng đọc') : 'Đọc từ màn hình hiện tại';
    }

    if (state.float) {
      state.float.classList.toggle('visible', active);
      const pause = state.float.querySelector('#los-speech-float-pause');
      if (pause) {
        pause.textContent = paused ? '▶' : '⏸';
        pause.setAttribute('aria-label', paused ? 'Tiếp tục đọc' : 'Tạm dừng đọc');
        pause.title = paused ? 'Tiếp tục đọc' : 'Tạm dừng đọc';
      }
      const segment = currentSegment();
      const label = state.float.querySelector('#los-speech-float-label');
      if (label) label.textContent = segment ? segment.lang.toUpperCase() : 'TTS';
    }
  }

  function finish(message = 'Đã đọc xong từ vị trí hiện tại.') {
    state.active = false;
    state.paused = false;
    clearHighlight();
    updateUi();
    statusText(message);
  }

  function speakCurrent() {
    if (!state.active || state.paused || routePath() !== state.path) return;

    if (state.index >= state.segments.length) {
      finish();
      return;
    }

    const segment = currentSegment();
    if (!segment?.text) {
      state.index += 1;
      speakCurrent();
      return;
    }

    const currentRun = state.runId;
    const utterance = new SpeechSynthesisUtterance(segment.text);
    const voice = pickVoice(segment.lang);
    utterance.lang = voice?.lang || VOICE_LOCALES[segment.lang]?.[0] || segment.lang;
    if (voice) utterance.voice = voice;
    utterance.rate = rateValue();

    utterance.onstart = () => {
      if (currentRun !== state.runId || !state.active) return;
      updateHighlight(segment.node);
      updateUi();
      statusText(`Đang đọc ${segment.lang.toUpperCase()} · ${state.index + 1}/${state.segments.length} · ${rateValue()}×`);
    };

    utterance.onend = () => {
      if (currentRun !== state.runId || !state.active) return;
      state.index += 1;
      window.setTimeout(speakCurrent, 0);
    };

    utterance.onerror = event => {
      if (currentRun !== state.runId || ['canceled', 'interrupted'].includes(event.error)) return;
      finish('Không thể đọc đoạn hiện tại bằng voice của trình duyệt.');
    };

    try {
      synth.speak(utterance);
    } catch {
      finish('Không thể khởi động đọc chữ trên trình duyệt này.');
    }
  }

  async function startFromViewport() {
    if (!state.content?.isConnected) return;

    state.defaultLanguage = await languageForPath(state.path);
    state.blocks = speechNodes(state.content);
    const startIndex = visibleBlockIndex(state.blocks);
    state.segments = buildSegments(state.blocks, startIndex, state.defaultLanguage);

    if (!state.segments.length) {
      statusText('Không tìm thấy nội dung để đọc từ màn hình hiện tại.');
      return;
    }

    state.runId += 1;
    synth.cancel();
    state.index = 0;
    state.active = true;
    state.paused = false;
    updateUi();
    statusText(`Bắt đầu từ nội dung đang hiển thị · ${state.segments.length} đoạn`);
    window.setTimeout(speakCurrent, 30);
  }

  function togglePause() {
    if (!state.active) return;

    if (state.paused) {
      state.paused = false;
      try { synth.resume(); } catch {}
      if (!synth.speaking && !synth.pending) window.setTimeout(speakCurrent, 0);
      statusText(`Đang đọc · ${state.index + 1}/${state.segments.length}`);
    } else {
      state.paused = true;
      try { synth.pause(); } catch {}
      statusText('Đã tạm dừng.');
    }
    updateUi();
  }

  function stop(message = 'Đã dừng.') {
    state.runId += 1;
    try { synth.cancel(); } catch {}
    state.active = false;
    state.paused = false;
    clearHighlight();
    updateUi();
    statusText(message);
  }

  function restartCurrentSegment() {
    if (!state.active) return;
    state.runId += 1;
    try { synth.cancel(); } catch {}
    if (!state.paused) window.setTimeout(speakCurrent, 35);
  }

  function setRate(rate, restart = false) {
    const value = RATE_OPTIONS.includes(Number(rate)) ? Number(rate) : 1;
    if (state.rateSelect) state.rateSelect.value = String(value);
    if (state.floatRateSelect) state.floatRateSelect.value = String(value);
    writeJson(STORAGE_RATE, value);
    if (restart) restartCurrentSegment();
  }

  function bindVoiceSelect(select, language) {
    state.voiceSelects.set(language, select);
    select.onchange = () => {
      writeJson(`${STORAGE_VOICE_PREFIX}${language}`, select.value || '');
      restartCurrentSegment();
    };
  }

  function installControls(existing, content, path) {
    if (!existing || existing.dataset.readerV2 === 'true') return;

    ensureStyles();
    state.path = path;
    state.content = content;
    state.controls = existing;
    existing.dataset.readerV2 = 'true';

    const selectedRate = Number(readJson(STORAGE_RATE, 1));
    const safeRate = RATE_OPTIONS.includes(selectedRate) ? selectedRate : 1;

    existing.innerHTML = `
      <button class="los-action" id="los-speech-start" type="button">🔊 Đọc từ màn hình hiện tại</button>
      <button class="los-action" id="los-speech-pause" type="button" disabled>⏸ Tạm dừng</button>
      <button class="los-action" id="los-speech-stop" type="button" disabled>■ Dừng</button>
      <label class="los-speech-rate"><span>Tốc độ</span><select class="los-select" id="los-speech-rate">${rateOptionsHtml(safeRate)}</select></label>
      <details class="los-speech-v2-voices">
        <summary>🎙 Voice VI / EN / KO</summary>
        <div class="los-speech-v2-voice-panel">
          <label class="los-speech-v2-voice-row"><span>Việt</span><select class="los-select" data-speech-voice="vi"></select></label>
          <label class="los-speech-v2-voice-row"><span>English</span><select class="los-select" data-speech-voice="en"></select></label>
          <label class="los-speech-v2-voice-row"><span>한국어</span><select class="los-select" data-speech-voice="ko"></select></label>
          <p class="los-speech-v2-note">Auto ưu tiên voice theo đúng ngôn ngữ. Với tài liệu tiếng Việt có thuật ngữ English/Korean, Reader sẽ tự đổi voice giữa các đoạn.</p>
        </div>
      </details>
      <span class="los-speech-status" id="los-speech-status" aria-live="polite">Sẵn sàng · đọc từ viewport hiện tại</span>
    `;

    state.startButton = existing.querySelector('#los-speech-start');
    state.pauseButton = existing.querySelector('#los-speech-pause');
    state.stopButton = existing.querySelector('#los-speech-stop');
    state.rateSelect = existing.querySelector('#los-speech-rate');
    state.status = existing.querySelector('#los-speech-status');
    state.voiceDetails = existing.querySelector('.los-speech-v2-voices');

    state.voiceSelects.clear();
    existing.querySelectorAll('[data-speech-voice]').forEach(select => bindVoiceSelect(select, select.dataset.speechVoice));

    state.startButton.onclick = startFromViewport;
    state.pauseButton.onclick = togglePause;
    state.stopButton.onclick = () => stop('Đã dừng.');
    state.rateSelect.onchange = () => setRate(Number(state.rateSelect.value), true);

    const edgeActions = document.querySelector('.reader-edge-actions');
    state.edgeButton = edgeActions?.querySelector('#edge-speech') || null;
    if (edgeActions && !state.edgeButton) {
      state.edgeButton = document.createElement('button');
      state.edgeButton.id = 'edge-speech';
      state.edgeButton.className = 'edge-button';
      state.edgeButton.type = 'button';
      edgeActions.prepend(state.edgeButton);
    }
    if (state.edgeButton) state.edgeButton.onclick = () => state.active ? togglePause() : startFromViewport();

    ensureFloat();
    setRate(safeRate, false);
    populateVoiceSelects();
    updateUi();
  }

  function cleanupForRoute(nextPath) {
    if (nextPath === state.path) return;
    if (state.active) stop('');
    state.controls = null;
    state.content = null;
    state.path = nextPath;
    state.blocks = [];
    state.segments = [];
    state.index = 0;
    state.voiceSelects.clear();
    state.float?.remove();
    state.float = null;
    state.floatRateSelect = null;
    state.edgeButton = null;
  }

  function enhance() {
    if (!('speechSynthesis' in window) || !('SpeechSynthesisUtterance' in window)) return;

    const path = routePath();
    cleanupForRoute(path);
    if (!path) return;

    const content = document.querySelector('.markdown');
    const controls = document.querySelector('#los-speech-controls');
    if (!content || !controls) return;

    if (controls.dataset.readerV2 !== 'true' || state.content !== content || state.path !== path) {
      if (state.active) stop('');
      state.path = path;
      installControls(controls, content, path);
    } else {
      const edge = document.querySelector('#edge-speech');
      if (edge && edge !== state.edgeButton) {
        state.edgeButton = edge;
        edge.onclick = () => state.active ? togglePause() : startFromViewport();
        updateUi();
      }
    }
  }

  let queued = false;
  function scheduleEnhance() {
    if (queued) return;
    queued = true;
    requestAnimationFrame(() => {
      queued = false;
      enhance();
    });
  }

  if ('speechSynthesis' in window) {
    synth.addEventListener?.('voiceschanged', () => {
      populateVoiceSelects();
    });
  }

  const observer = new MutationObserver(scheduleEnhance);
  observer.observe(document.documentElement, { childList: true, subtree: true });

  addEventListener('hashchange', () => {
    cleanupForRoute(routePath());
    scheduleEnhance();
  });
  addEventListener('pagehide', () => stop(''));

  scheduleEnhance();
})();