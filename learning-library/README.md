# Study Shelf

A lightweight GitHub Pages reader for the Markdown and PDF files stored in this workspace. The site remains a static frontend: local reading works without an account, while optional Supabase Auth + PostgreSQL adds multi-device progress sync.

## What it does

The library builds a searchable catalogue, renders Markdown with TOC/bookmarks, opens PDFs, tracks reading position/status/progress, supports review/offline/PWA features, and keeps manual JSON export/import as a backup. All existing `study-shelf-*` localStorage data remains supported.

## Local preview

```bash
cd learning-library
npm run build:library
npm run serve
```

Without Supabase environment variables, the generated client config is empty and the UI shows `Local only`. The site still stores everything in localStorage.

To test cloud sync locally:

```bash
cp .env.example .env
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

## Shared Supabase progress

Apply `supabase/migrations/20260924111500_create_learning_progress.sql` to the same Supabase project already used by the learning apps. Do not create a new project unless the existing project cannot be reused. The shared table is `public.learning_progress`; it is intentionally generic so `study-library`, `languages-docs`, and future apps can share it.

Study Library uses `app_id = "study-library"`. Document records use a namespace derived from the document category and `content_type = "document"`. If the catalogue provides an explicit `contentId`, it is used directly; otherwise Study Library derives a deterministic ID from stable document metadata, not from the URL/path. `content_path` is stored only as a migration/display hint.

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

Unknown `state` keys are deep-preserved during merge. Records from another app such as `languages-docs` are cached and re-exported unchanged; Study Library only writes its own `state.study_library` keys. If the user is signed in, imported records are marked dirty and uploaded to the shared table. Old version-1 Study Shelf snapshot files remain importable.

See `/SHARED_PROGRESS_SCHEMA.md` for the shared contract.

## Supabase Auth / RLS setup

Enable the authentication method already used by Study Planner. This frontend supports both magic-link email auth and email/password sign-in. For magic links, add the GitHub Pages URL and the local preview URL to Supabase Auth redirect URLs.

The migration enables RLS and grants authenticated users access only when `user_id = auth.uid()`. Anonymous table access is revoked. The static site must use only the project URL and anon key; never expose a service-role key.

## GitHub Pages Secrets

Create these repository/environment Secrets:

- `VITE_SUPABASE_URL`
- `VITE_SUPABASE_ANON_KEY`

The Pages workflow injects them only while generating `site/supabase-config.js`. That generated file is ignored by git. If either Secret is absent, deployment still succeeds in local-only mode.

## Publication safety

Only files under reviewed prefixes or explicit paths in `library.config.json` are copied into the published site. Confirm ownership, redistribution permission, or a compatible open licence/public-domain status before allowing a document. Run `npm run audit:library` before publishing.

See [PUBLISHING.md](PUBLISHING.md) for the current publication scope.
