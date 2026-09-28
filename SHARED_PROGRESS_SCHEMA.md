# Dùng chung (shared / 공유) học tập (learning / 학습) Progress lược đồ (schema / 스키마)

`learning_progress` is the dùng chung (shared / 공유) progress bảng (table / 테이블) for `study-library`, `languages-docs`, and future học tập (learning / 학습) applications. It is intentionally application-neutral: app-specific dữ liệu (data / 데이터) belongs in `state`, while the dùng chung (common / 공통) columns remain stable across products.

> **Mạch đọc:** lược đồ (schema / 스키마) này đi từ định danh (identity / 식별자) → columns/tính tương thích (compatibility / 호환성) → trình duyệt (browser / 브라우저) API → merge rules → snapshot → bảo mật (security / 보안). Mỗi lớp giữ bất biến (invariant / 불변식) cho lớp kế tiếp; khi triển khai, đối chiếu cả đặc tả hợp đồng (contract / 계약) trước đó và hành vi (behavior / 동작) của adapter sau đó.

## Định danh (identity / 식별자)

A row is uniquely identified by `user_id + app_id + content_namespace + content_type + content_id`.

`content_id` must be a stable application-level identifier and must not be a URL or tệp (file / 파일) đường dẫn (path / 경로). `content_path` is only the hiện tại (current / 현재) location hint used for display or di chuyển (migration / 마이그레이션). A máy khách (client / 클라이언트) may provide an tường minh (explicit / 명시적) content ID from its catalogue; otherwise its adapter must derive an ID from stable content siêu dữ liệu (metadata / 메타데이터) rather than a tuyến (route / 경로).

Study thư viện (library / 라이브러리) uses `app_id = "study-library"`, `content_type = "document"` for documents, and a separate `content_type = "settings"` bản ghi (record / 레코드) for app preferences. `languages-docs` should use its own `app_id` while reusing the same bảng (table / 테이블).

## Columns and forward tính tương thích (compatibility / 호환성)

The dùng chung (shared / 공유) columns are `id`, `user_id`, `app_id`, `content_namespace`, `content_type`, `content_id`, `content_path`, `status`, `progress_pct`, `current_section`, `completed_sections`, `bookmarks`, `state`, `schema_version`, `last_opened_at`, `created_at`, and `updated_at`.

`state` is the forward-compatible extension điểm (point / 지점). Clients must preserve every unknown key in `state` when they merge or cập nhật (update / 업데이트) a bản ghi (record / 레코드). A Study thư viện (library / 라이브러리) ghi (write / 쓰기) may cập nhật (update / 업데이트) `state.study_library`, but it must not discard keys owned by another phiên bản (version / 버전) or tích hợp (integration / 통합).

## Trình duyệt (browser / 브라우저) API

The dùng chung (shared / 공유) trình duyệt (browser / 브라우저) lớp trừu tượng (abstraction / 추상화) exposes `getProgress(appId, contentNamespace, contentType, contentId)`, `upsertProgress(progress)`, `listProgress(appId)`, and `mergeLocalAndRemoteProgress(local, remote)`. `listProgress()` may omit `appId` when a full-account export is needed. RLS always scopes cloud rows to the authenticated người dùng (user / 사용자).

## Merge rules

The newer `updated_at` bản ghi (record / 레코드) wins for mutable dùng chung (common / 공통) fields such as status, percentage, hiện tại (current / 현재) section, bookmarks, and completed sections. `state` is deep-merged so unknown keys survive. `schema_version` keeps the highest phiên bản (version / 버전) seen, `created_at` keeps the oldest known giá trị (value / 값), and a server-side `id` is preserved when it exists.

Clients should set `updated_at` when user-visible học tập (learning / 학습) trạng thái (state / 상태) changes. `last_opened_at` may thay đổi (change / 변경) without making an older progress payload authoritative. Offline writes remain cục bộ (local / 로컬) and are retried when the trình duyệt (browser / 브라우저) returns online.

## Snapshot v2

Snapshot v2 uses `format = "shared-learning-progress"` and contains a `learning_progress` array. Every exported bản ghi (record / 레코드) keeps `app_id`, `content_namespace`, `content_type`, `content_id`, `schema_version`, the other available dùng chung (common / 공통) fields, and the complete `state` đối tượng (object / 객체).

Import must round-trip records from apps the hiện tại (current / 현재) frontend does not understand. Study thư viện (library / 라이브러리) therefore stores and re-exports `languages-docs` records unchanged and only mutates Study Library-owned trạng thái (state / 상태) when Study thư viện (library / 라이브러리) itself changes its own bản ghi (record / 레코드). The snapshot also carries legacy `study-shelf-*` localStorage values as a khôi phục (recovery / 복구) tầng (layer / 계층). phiên bản (version / 버전) 1 Study Shelf snapshots remain importable and are migrated into the dùng chung (shared / 공유) bản ghi (record / 레코드) format.

## Supabase bảo mật (security / 보안)

The di chuyển (migration / 마이그레이션) enables Row mức (level / 수준) bảo mật (security / 보안) and allows authenticated users to select, insert, cập nhật (update / 업데이트), and delete only rows whose `user_id` equals `auth.uid()`. Anonymous bảng (table / 테이블) truy cập (access / 접근) is revoked. The static frontend uses only the Supabase URL and anon key; never expose a service-role key in GitHub Pages.

> **Bàn giao:** Sau ranh giới bảo mật (security boundary / 보안 경계), kiểm tra adapter và di chuyển (migration / 마이그레이션) ở Study thư viện (library / 라이브러리)/Planner; nếu hành vi (behavior / 동작) lệch lược đồ (schema / 스키마), sửa đơn vị sở hữu (owner / 오너) tương ứng rồi chạy lại round-trip, merge và RLS bằng chứng (evidence / 증거) thay vì nới đặc tả hợp đồng (contract / 계약) chung tùy tiện.
