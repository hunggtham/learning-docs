# Shared Learning Progress Schema

`learning_progress` is the shared progress table for `study-library`, `languages-docs`, and future learning applications. It is intentionally application-neutral: app-specific data belongs in `state`, while the common columns remain stable across products.

## Identity

A row is uniquely identified by `user_id + app_id + content_namespace + content_type + content_id`.

`content_id` must be a stable application-level identifier and must not be a URL or file path. `content_path` is only the current location hint used for display or migration. A client may provide an explicit content ID from its catalogue; otherwise its adapter must derive an ID from stable content metadata rather than a route.

Study Library uses `app_id = "study-library"`, `content_type = "document"` for documents, and a separate `content_type = "settings"` record for app preferences. `languages-docs` should use its own `app_id` while reusing the same table.

## Columns and forward compatibility

The shared columns are `id`, `user_id`, `app_id`, `content_namespace`, `content_type`, `content_id`, `content_path`, `status`, `progress_pct`, `current_section`, `completed_sections`, `bookmarks`, `state`, `schema_version`, `last_opened_at`, `created_at`, and `updated_at`.

`state` is the forward-compatible extension point. Clients must preserve every unknown key in `state` when they merge or update a record. A Study Library write may update `state.study_library`, but it must not discard keys owned by another version or integration.

## Browser API

The shared browser abstraction exposes `getProgress(appId, contentNamespace, contentType, contentId)`, `upsertProgress(progress)`, `listProgress(appId)`, and `mergeLocalAndRemoteProgress(local, remote)`. `listProgress()` may omit `appId` when a full-account export is needed. RLS always scopes cloud rows to the authenticated user.

## Merge rules

The newer `updated_at` record wins for mutable common fields such as status, percentage, current section, bookmarks, and completed sections. `state` is deep-merged so unknown keys survive. `schema_version` keeps the highest version seen, `created_at` keeps the oldest known value, and a server-side `id` is preserved when it exists.

Clients should set `updated_at` when user-visible learning state changes. `last_opened_at` may change without making an older progress payload authoritative. Offline writes remain local and are retried when the browser returns online.

## Snapshot v2

Snapshot v2 uses `format = "shared-learning-progress"` and contains a `learning_progress` array. Every exported record keeps `app_id`, `content_namespace`, `content_type`, `content_id`, `schema_version`, the other available common fields, and the complete `state` object.

Import must round-trip records from apps the current frontend does not understand. Study Library therefore stores and re-exports `languages-docs` records unchanged and only mutates Study Library-owned state when Study Library itself changes its own record. The snapshot also carries legacy `study-shelf-*` localStorage values as a recovery layer. Version 1 Study Shelf snapshots remain importable and are migrated into the shared record format.

## Supabase security

The migration enables Row Level Security and allows authenticated users to select, insert, update, and delete only rows whose `user_id` equals `auth.uid()`. Anonymous table access is revoked. The static frontend uses only the Supabase URL and anon key; never expose a service-role key in GitHub Pages.
