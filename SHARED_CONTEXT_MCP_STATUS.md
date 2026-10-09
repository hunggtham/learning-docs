# Shared Context MCP — trạng thái và cách kiểm tra

Snapshot được ghi lúc **2026-10-09 16:45 KST**.

## Phạm vi cài đặt

- Repository: `/Users/mac/00.my-learning`
- Branch hiện tại: `main`
- HEAD tại lúc snapshot: `7123c1a0 chore: update review progress count for kiip level5 01_영주용_기본`
- MCP workspace config: `.agents/mcp_config.json`
- MCP endpoint: `http://localhost:3721/mcp`
- Context dùng chung: `my-learning`
- Server source/install: `/Users/mac/.local/share/mcp-agent-bridge`
- Server revision: `e0f39f2 first commit`

## Trạng thái live đã kiểm tra

- macOS `launchd`: `com.mcp-agent-bridge` đang `running`
- Node process: `/opt/homebrew/bin/node`
- Working directory: `/Users/mac/.local/share/mcp-agent-bridge`
- Listener: `127.0.0.1:3721` (chỉ localhost; không mở ra LAN)
- Health endpoint trả `status: ok`, version `3.0.0`
- Antigravity đang kết nối trong context `my-learning`
- Artifact handoff hiện có: `setup-handoff-2026-10-09`
- Context hiện chưa có task, memory key hoặc session đang chạy

## Trạng thái Git tại snapshot

- `main` đang **ahead 2** so với `origin/main`
- Worktree có **46 file đã sửa** (chủ yếu tài liệu KIIP) và **1 path untracked** (`.agents/` tại thời điểm kiểm tra)
- Không reset, checkout, clean hoặc stage các thay đổi hiện có khi kiểm tra MCP.

## Lệnh kiểm tra nhanh

```bash
cd /Users/mac/00.my-learning
git status --short --branch
curl -fsS http://127.0.0.1:3721/health
lsof -nP -iTCP:3721 -sTCP:LISTEN
launchctl print "gui/$(id -u)/com.mcp-agent-bridge" \
  | rg -n "state =|program =|working directory|pid =|last exit code"
```

Kết quả mong đợi: health `status: ok`, listener `127.0.0.1:3721`, và launchd `state = running`.

## Khởi động lại daemon nếu cần

```bash
launchctl kickstart -k "gui/$(id -u)/com.mcp-agent-bridge"
curl -fsS http://127.0.0.1:3721/health
```

LaunchAgent nằm tại:
`/Users/mac/Library/LaunchAgents/com.mcp-agent-bridge.plist`.

## Khi tiếp tục docs bằng Antigravity

1. Mở workspace `/Users/mac/00.my-learning`.
2. Kiểm tra MCP server `shared-context` trong MCP Servers hoặc `/mcp`.
3. Xác nhận agent vào context `my-learning`.
4. Đọc artifact `setup-handoff-2026-10-09`.
5. Kiểm tra `git status` và chọn một batch docs giới hạn trước khi sửa.

## Lưu ý an toàn

- Server bridge không có authentication; việc bind vào `127.0.0.1` là chủ ý.
- Dữ liệu context/runtime nằm ngoài repo trong `/Users/mac/.local/share/mcp-agent-bridge/data/`.
- Không đưa token hoặc credential vào `.agents/mcp_config.json`.
- Không dùng `git reset --hard`, `git clean` hoặc checkout để “dọn” trạng thái hiện tại nếu chưa có chỉ dẫn rõ ràng.
- Dependency upstream từng báo cảnh báo `npm audit`; chưa tự động chạy `npm audit fix` để tránh thay đổi ngoài phạm vi setup.
