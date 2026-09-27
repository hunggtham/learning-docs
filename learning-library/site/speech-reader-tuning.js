(() => {
  'use strict';

  const ENGLISH_TERMS = [
    'machine learning', 'deep learning', 'artificial intelligence', 'market crash',
    'house bubble', 'housing bubble', 'supply and demand', 'operating system',
    'data structure', 'design pattern', 'dependency injection', 'garbage collection',
    'event loop', 'memory leak', 'race condition', 'thread pool', 'load balancer',
    'pull request', 'code review', 'unit test', 'integration test', 'access token',
    'refresh token', 'local storage', 'session storage', 'service worker',
    'frontend', 'backend', 'framework', 'runtime', 'database', 'server', 'client',
    'repository', 'branch', 'commit', 'merge', 'cache', 'query', 'thread', 'process',
    'function', 'method', 'object', 'class', 'interface', 'network', 'software',
    'hardware', 'cloud', 'container', 'docker', 'kubernetes', 'browser', 'storage',
    'authentication', 'authorization', 'token', 'session', 'market', 'bubble',
    'inflation', 'deflation', 'recession', 'portfolio', 'investment', 'forex'
  ].sort((a, b) => b.length - a.length);

  const TERM_RE = new RegExp(`\\b(${ENGLISH_TERMS.map(term => term.replace(/[.*+?^${}()|[\\]\\]/g, '\\$&')).join('|')})\\b`, 'gi');
  const ACRONYM_RE = /\\b(?:API|CPU|GPU|RAM|SQL|HTML|CSS|HTTP|HTTPS|JSON|XML|DOM|URL|URI|JWT|OAuth|REST|GraphQL|TTS|AI|IT)\\b/g;
  const SKIP = new Set(['CODE', 'PRE', 'KBD', 'SAMP', 'SCRIPT', 'STYLE', 'A', 'TEXTAREA', 'SELECT', 'OPTION']);

  function wrapMatches(textNode, regex) {
    const text = textNode.nodeValue || '';
    regex.lastIndex = 0;
    if (!regex.test(text)) return false;
    regex.lastIndex = 0;

    const fragment = document.createDocumentFragment();
    let cursor = 0;
    let match;
    while ((match = regex.exec(text))) {
      if (match.index > cursor) fragment.append(document.createTextNode(text.slice(cursor, match.index)));
      const span = document.createElement('span');
      span.lang = 'en';
      span.dataset.speechLang = 'en';
      span.textContent = match[0];
      fragment.append(span);
      cursor = match.index + match[0].length;
    }
    if (cursor < text.length) fragment.append(document.createTextNode(text.slice(cursor)));
    textNode.replaceWith(fragment);
    return true;
  }

  function annotateEnglish(content) {
    if (!content || content.dataset.speechLanguageTuned === 'true') return;
    const walker = document.createTreeWalker(content, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        const parent = node.parentElement;
        if (!parent || SKIP.has(parent.tagName) || parent.closest('[lang],pre,code,kbd,samp,a,.los-related')) return NodeFilter.FILTER_REJECT;
        if (!/[A-Za-z]/.test(node.nodeValue || '')) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });

    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    for (const node of nodes) {
      if (wrapMatches(node, TERM_RE)) continue;
      wrapMatches(node, ACRONYM_RE);
    }
    content.dataset.speechLanguageTuned = 'true';
  }

  function hideAdvancedVoiceUi() {
    const details = document.querySelector('.los-speech-v2-voices');
    const summary = details?.querySelector(':scope > summary');
    if (!details || !summary || details.dataset.compact === 'true') return;
    details.dataset.compact = 'true';
    summary.textContent = '⋯';
    summary.setAttribute('aria-label', 'Tùy chỉnh giọng đọc nâng cao');
    summary.title = 'Tùy chỉnh giọng đọc nâng cao';
  }

  function ensureStyles() {
    if (document.querySelector('#speech-reader-tuning-style')) return;
    const style = document.createElement('style');
    style.id = 'speech-reader-tuning-style';
    style.textContent = `
      .los-speech-v2-voices[data-compact="true"]{margin-left:auto}
      .los-speech-v2-voices[data-compact="true"]>summary{
        width:34px!important;height:34px!important;min-height:34px!important;padding:0!important;
        display:grid!important;place-items:center!important;border:0!important;border-radius:50%!important;
        background:transparent!important;color:var(--muted)!important;font-size:1.05rem!important;opacity:.45
      }
      .los-speech-v2-voices[data-compact="true"]>summary:hover,
      .los-speech-v2-voices[data-compact="true"]>summary:focus-visible,
      .los-speech-v2-voices[data-compact="true"][open]>summary{
        opacity:1;background:var(--accent-soft)!important;color:var(--accent)!important;outline:0
      }
      [data-speech-lang="en"]{font:inherit;color:inherit;background:inherit}
      @media(max-width:760px){.los-speech-v2-voices[data-compact="true"]{flex:0 0 auto;margin-left:0}}
    `;
    document.head.append(style);
  }

  function enhance() {
    ensureStyles();
    annotateEnglish(document.querySelector('.markdown'));
    hideAdvancedVoiceUi();
  }

  let queued = false;
  const schedule = () => {
    if (queued) return;
    queued = true;
    requestAnimationFrame(() => { queued = false; enhance(); });
  };

  new MutationObserver(schedule).observe(document.documentElement, { childList: true, subtree: true });
  addEventListener('hashchange', schedule);
  schedule();
})();
