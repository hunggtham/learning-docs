# Study Shelf

A lightweight GitHub Pages reader for the Markdown and PDF files stored in this workspace. The site remains a static frontend: local reading works without an account, while optional Supabase Auth + PostgreSQL adds multi-device progress sync.

> **Mạch vận hành:** Nội dung đi theo chuỗi `canonical Markdown/PDF → publication manifest → audit → build/index → reader → progress sync`. Khi debug hoặc thay đổi một lớp, quay lại lớp trước để xác định source of truth và đi tiếp tới evidence của lớp sau.

## What it does

Phần này định vị Study Library trước khi đi vào chi tiết: trình đọc lấy tài liệu đã kiểm tra, tạo chỉ mục tìm kiếm và giữ đường dẫn để người học quay lại bài giảng gốc.

- Builds a searchable document catalogue from safe folder prefixes plus explicit `.md`/`.pdf` entries.
- Renders Markdown in a clean reading layout with a table of contents.
- Opens PDFs in the browser's native PDF reader.
- Lets readers filter by Markdown/PDF and open or download the original file.
- Shows subfolders and files; `raw`/`raw_md` are hidden, and `output` is flattened in the displayed path.
- Runs a fail-closed publication audit before copying anything into the Pages artifact.
- Works as a static site: no account, database, or server is required.

## Local preview
Phần “Local preview” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```bash
cd learning-library
npm run build:library
npm run serve
```

Để build và mở trang local trong trình duyệt bằng một lệnh:

```bash
npm run open:local
```

Lệnh này tạo lại `site/library`, chạy server tại `http://localhost:4173/` và tự mở trình duyệt. Có thể đổi cổng bằng `PORT=5173 npm run open:local`.

Study Library uses the shared learning Supabase project (project ref `suvknhgjcgeudjqmgzwt`). The project URL therefore defaults to `https://suvknhgjcgeudjqmgzwt.supabase.co`. Without a publishable/anon client key, the UI stays `Local only` and continues using localStorage.

To test cloud sync locally:

```bash
cp .env.example .env
# put the Supabase publishable key in .env
set -a
source .env
set +a
npm run build:library
npm run serve
```

Run checks with:

```bash
npm run check:sync
npm run audit:library
npm run build:library
```

Stable document identity is kept in `content-ids.json`, not in the Markdown filenames. Run `npm run sync:content-ids` after adding or moving published files; it preserves known IDs, records detected aliases, and rebuilds the catalogue. The generated catalogue carries both `contentId` and a SHA-256 `contentRevision`. A moved document keeps its progress through the alias path; an edited document keeps its existing percentage but is marked as updated so the reader can reset it deliberately.

## Shared Supabase progress

Apply `supabase/migrations/20260924111500_create_learning_progress.sql` to the same Supabase project used by Study Planner. The equivalent migration is also stored in `hunggtham/my-study-planner` as `supabase/migrations/20260924_shared_learning_progress.sql`, so it is part of the linked Planner project's migration chain. Do not create a separate Supabase project.

The shared table is `public.learning_progress`; it is intentionally generic so `my-learning`, `languages-docs`, and future apps can share it.

Study Library uses `app_id = "my-learning"`. Document records use a namespace derived from the document category and `content_type = "document"`. Each published document receives a stable `contentId` from `content-ids.json`; explicit `contentId`/`contentAliases` values in `library.config.json` can seed a new registry entry when needed. The app-id migration preserves the existing content-ID seed so existing progress rows continue to match. `content_path` is stored only as a migration/display hint, while `contentRevision` detects content changes without changing identity.

The browser abstraction in `site/progress-sync.js` exposes:

```text
getProgress(appId, contentNamespace, contentType, contentId)
upsertProgress(progress)
listProgress(appId)
mergeLocalAndRemoteProgress(local, remote)
```

On startup, localStorage is read first. When an authenticated session is available, cloud rows are fetched and merged by `updated_at`; local changes are written immediately and cloud upserts are debounced. Offline changes stay dirty locally and are retried after reconnect. Returning to a visible tab also triggers a refresh.

Legacy localStorage is migrated automatically after the document catalogue loads. Existing progress is never deleted. A cloud-newer row is written back into the legacy `study-shelf-*` keys so the current reader continues to work without a rewrite.

## Snapshot export/import

Snapshot v2 uses `format = "shared-learning-progress"` and exports generic `learning_progress` records plus the legacy `study-shelf-*` values. It preserves `app_id`, `content_namespace`, `content_type`, `content_id`, `schema_version`, every common schema field present, and the complete `state` object.

Unknown `state` keys are deep-preserved during merge. Records from another app such as `languages-docs` are cached and re-exported unchanged; Study Library writes its own `state.my_learning` keys and reads legacy `state.study_library` keys during migration. If the user is signed in, imported records are marked dirty and uploaded to the shared table. Old version-1 Study Shelf snapshot files remain importable.

See `/SHARED_PROGRESS_SCHEMA.md` for the shared contract.

## Supabase Auth / RLS setup

Study Library follows Study Planner's current authentication convention: email/password sign-in plus account registration with `supabase.auth.signInWithPassword()` and `supabase.auth.signUp()`. Sessions persist through the Supabase JS client, so the same account can be used on MacBook, phone, and other devices.

The migration enables RLS and grants authenticated users access only when `user_id = auth.uid()`. Anonymous table access is revoked. The static site uses only the project URL and anon/publishable key; never expose a service-role key.

## GitHub Pages configuration

The shared project URL is already used as the safe fallback. Add the Supabase publishable client key as a GitHub Actions Secret:

- `VITE_SUPABASE_PUBLISHABLE_KEY` — preferred client key for cloud auth/sync
- `VITE_SUPABASE_ANON_KEY` — legacy fallback for existing deployments
- `VITE_SUPABASE_URL` — optional override; when absent the Planner project URL above is used

The Pages workflow injects environment values only while generating `site/supabase-config.js`. That generated file is ignored by git. If the client key is absent, deployment still succeeds in local-only mode.

## Publication safety

Only files under reviewed prefixes or explicit paths in `library.config.json` are copied into the published site. Confirm ownership, redistribution permission, or a compatible open licence/public-domain status before allowing a document. Run `npm run audit:library` before publishing.

See [PUBLISHING.md](PUBLISHING.md) for the current publication scope.

> **Bàn giao:** Sau khi publication audit và build pass, kiểm tra reader/search/progress ở môi trường đích; lỗi hiển thị cần được trace ngược về source, manifest hoặc generated artifact thay vì sửa trực tiếp bản site.
