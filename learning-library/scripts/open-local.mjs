import { spawn, spawnSync } from 'node:child_process';
import process from 'node:process';

const port = Number.parseInt(process.env.PORT || '4173', 10);
const host = process.env.HOST || 'localhost';
const url = `http://${host}:${port}/`;

if (!Number.isInteger(port) || port < 1 || port > 65535) {
  console.error('PORT phải là số nguyên trong khoảng 1–65535.');
  process.exit(1);
}

function runBuild(script) {
  const result = spawnSync(process.execPath, [script], { stdio: 'inherit' });
  if (result.error) throw result.error;
  if (result.status !== 0) process.exit(result.status ?? 1);
}

function openBrowser(target) {
  const command = process.platform === 'darwin' ? 'open'
    : process.platform === 'win32' ? 'cmd'
      : 'xdg-open';
  const args = process.platform === 'win32' ? ['/c', 'start', '', target] : [target];
  const opener = spawn(command, args, { detached: true, stdio: 'ignore' });
  opener.on('error', () => {
    console.log(`Không tự mở được trình duyệt. Hãy mở thủ công: ${target}`);
  });
  opener.unref();
}

try {
  console.log('Đang tạo library artifact trước khi chạy local…');
  runBuild('scripts/build-library.mjs');
  runBuild('scripts/write-supabase-config.mjs');
} catch (error) {
  console.error(`Không thể build library: ${error.message}`);
  process.exit(1);
}

const server = spawn('python3', ['-m', 'http.server', String(port), '--bind', host, '--directory', 'site'], {
  stdio: 'inherit',
});

server.on('error', error => {
  console.error(`Không thể khởi động local server: ${error.message}`);
  process.exit(1);
});

server.on('exit', (code, signal) => {
  if (signal) console.log(`Local server đã dừng (${signal}).`);
  else if (code) {
    console.error(`Local server dừng với mã ${code}. Cổng ${port} có thể đang được sử dụng.`);
    process.exit(code);
  }
});

const shutdown = signal => {
  if (!server.killed) server.kill(signal);
  process.exit(signal === 'SIGINT' ? 130 : 143);
};
process.once('SIGINT', () => shutdown('SIGINT'));
process.once('SIGTERM', () => shutdown('SIGTERM'));

console.log(`Local preview đang chạy tại ${url}`);
console.log('Nhấn Ctrl+C để dừng server.');
setTimeout(() => openBrowser(url), 350);
