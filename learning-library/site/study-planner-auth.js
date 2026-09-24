(() => {
  'use strict';

  const cfg = window.__LEARNING_SUPABASE_CONFIG__ || {};
  let clientPromise = null;

  async function getClient() {
    if (clientPromise) return clientPromise;
    clientPromise = (async () => {
      if (!cfg.url || !cfg.anonKey) throw new Error('Supabase anon key chưa được cấu hình.');
      if (!window.supabase?.createClient) {
        await new Promise((resolve, reject) => {
          const script = document.createElement('script');
          script.src = 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2';
          script.async = true;
          script.onload = resolve;
          script.onerror = () => reject(new Error('Không tải được Supabase client.'));
          document.head.append(script);
        });
      }
      return window.supabase.createClient(cfg.url, cfg.anonKey, {
        auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true }
      });
    })();
    return clientPromise;
  }

  async function signUp(panel) {
    const errorNode = panel.querySelector('#learning-auth-error');
    const email = panel.querySelector('#learning-auth-email')?.value.trim();
    const password = panel.querySelector('#learning-auth-password')?.value || '';
    errorNode.textContent = '';
    try {
      if (!email || !password) throw new Error('Nhập email và mật khẩu.');
      if (password.length < 6) throw new Error('Mật khẩu cần ít nhất 6 ký tự.');
      const client = await getClient();
      const { data, error } = await client.auth.signUp({ email, password });
      if (error) throw error;
      const state = panel.querySelector('#learning-auth-state');
      if (state) state.textContent = data.session
        ? 'Đăng ký và đăng nhập thành công. Đang tải dữ liệu đồng bộ…'
        : 'Đăng ký thành công. Nếu Supabase yêu cầu xác nhận email, hãy xác nhận rồi đăng nhập.';
      if (data.session) setTimeout(() => location.reload(), 250);
    } catch (error) {
      errorNode.textContent = error.message || String(error);
    }
  }

  function patchPanel(panel) {
    if (!panel || panel.dataset.studyPlannerAuth === '1') return;
    const email = panel.querySelector('#learning-auth-email');
    const password = panel.querySelector('#learning-auth-password');
    const signUpButton = panel.querySelector('#learning-magic');
    const signInButton = panel.querySelector('#learning-password');
    if (!email || !password || !signUpButton || !signInButton) return;

    panel.dataset.studyPlannerAuth = '1';
    password.placeholder = 'Mật khẩu';
    password.required = true;
    signUpButton.textContent = 'Đăng ký';
    signUpButton.onclick = () => signUp(panel);
    signInButton.textContent = 'Đăng nhập';
    signInButton.title = 'Dùng cùng email/password với Study Planner';
  }

  const observer = new MutationObserver(() => patchPanel(document.querySelector('#learning-auth-panel')));
  observer.observe(document.documentElement, { childList: true, subtree: true });
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => patchPanel(document.querySelector('#learning-auth-panel')), { once: true });
  } else {
    patchPanel(document.querySelector('#learning-auth-panel'));
  }
})();
