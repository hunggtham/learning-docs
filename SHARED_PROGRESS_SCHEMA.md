# Dùng chung (shared / 공유) học tập (learning / 학습) Progress lược đồ (schema / 스키마)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Dùng chung (shared / 공유) học tập (learning / 학습) Progress lược đồ (schema / 스키마)**. Route đi từ identity và ownership → common columns → state/metadata và forward compatibility → app integrations, để progress schema dùng chung mà không kéo logic riêng của từng ứng dụng vào lõi.

`learning_progress` is the dùng chung (shared / 공유) progress bảng (table / 테이블) for `my-learning`, `languages-docs`, and future học tập (learning / 학습) applications. It is intentionally application-neutral: app-specific dữ liệu (data / 데이터) belongs in `state`, while the dùng chung (common / 공통) columns remain stable across products.

## Định danh (identity / 식별자)

A row is uniquely identified by `user_id + app_id + content_namespace + content_type + content_id`.

`content_id` must be a stable application-level identifier and must not be a URL or tệp (file / 파일) đường dẫn (path / 경로). `content_path` is only the hiện tại (current / 현재) location hint used for display or di chuyển (migration / 마이그레이션). A máy khách (client / 클라이언트) may provide an tường minh (explicit / 명시적) content ID from its catalogue; the Study Library registry keeps this ID when a file moves and stores old paths as aliases. `content_revision` belongs in the application state, not in the identity key, so content updates can be detected without creating a new progress record.

Study thư viện (library / 라이브러리) uses `app_id = "my-learning"`, `content_type = "document"` for documents, and a separate `content_type = "settings"` bản ghi (record / 레코드) for app preferences. `languages-docs` should use its own `app_id` while reusing the same bảng (table / 테이블).

> **Chuyển mạch:** Trong **Dùng chung (shared / 공유) học tập (learning / 학습) Progress lược đồ (schema / 스키마)**, **Columns and forward tính tương thích (compatibility / 호환성)** tiếp nhận điểm tựa từ **Định danh (identity / 식별자)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trình duyệt (browser / 브라우저) API** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Columns and forward tính tương thích (compatibility / 호환성)

The dùng chung (shared / 공유) columns are `id`, `user_id`, `app_id`, `content_namespace`, `content_type`, `content_id`, `content_path`, `status`, `progress_pct`, `current_section`, `completed_sections`, `bookmarks`, `state`, `schema_version`, `last_opened_at`, `created_at`, and `updated_at`.

`state` is the forward-compatible extension điểm (point / 지점). Clients must preserve every unknown key in `state` when they merge or cập nhật (update / 업데이트) a bản ghi (record / 레코드). A Study thư viện (library / 라이브러리) ghi (write / 쓰기) may cập nhật (update / 업데이트) `state.my_learning`; clients retain legacy `state.study_library` during migration and must not discard keys owned by another phiên bản (version / 버전) or tích hợp (integration / 통합).

> **Chuyển mạch:** Ở chặng này của **Dùng chung (shared / 공유) học tập (learning / 학습) Progress lược đồ (schema / 스키마)**, **Trình duyệt (browser / 브라우저) API** tiếp nhận điểm tựa từ **Columns and forward tính tương thích (compatibility / 호환성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Merge rules** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trình duyệt (browser / 브라우저) API

The dùng chung (shared / 공유) trình duyệt (browser / 브라우저) lớp trừu tượng (abstraction / 추상화) exposes `getProgress(appId, contentNamespace, contentType, contentId)`, `upsertProgress(progress)`, `listProgress(appId)`, and `mergeLocalAndRemoteProgress(local, remote)`. `listProgress()` may omit `appId` when a full-account export is needed. RLS always scopes cloud rows to the authenticated người dùng (user / 사용자).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dùng chung (shared / 공유) học tập (learning / 학습) Progress lược đồ (schema / 스키마)**, **Merge rules** tiếp nhận điểm tựa từ **Trình duyệt (browser / 브라우저) API** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Snapshot v2** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Merge rules

The newer `updated_at` bản ghi (record / 레코드) wins for mutable dùng chung (common / 공통) fields such as status, percentage, hiện tại (current / 현재) section, bookmarks, and completed sections. `state` is deep-merged so unknown keys survive. `schema_version` keeps the highest phiên bản (version / 버전) seen, `created_at` keeps the oldest known giá trị (value / 값), and a server-side `id` is preserved when it exists.

Clients should set `updated_at` when user-visible học tập (learning / 학습) trạng thái (state / 상태) changes. `last_opened_at` may thay đổi (change / 변경) without making an older progress payload authoritative. Offline writes remain cục bộ (local / 로컬) and are retried when the trình duyệt (browser / 브라우저) returns online.

> **Chuyển mạch:** Trong **Dùng chung (shared / 공유) học tập (learning / 학습) Progress lược đồ (schema / 스키마)**, **Snapshot v2** tiếp nhận điểm tựa từ **Merge rules** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Supabase bảo mật (security / 보안)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Snapshot v2

Snapshot v2 uses `format = "shared-learning-progress"` and contains a `learning_progress` array. Every exported bản ghi (record / 레코드) keeps `app_id`, `content_namespace`, `content_type`, `content_id`, `schema_version`, the other available dùng chung (common / 공통) fields, and the complete `state` đối tượng (object / 객체).

Import must round-trip records from apps the hiện tại (current / 현재) frontend does not understand. Study thư viện (library / 라이브러리) therefore stores and re-exports `languages-docs` records unchanged and only mutates Study Library-owned trạng thái (state / 상태) when Study thư viện (library / 라이브러리) itself changes its own bản ghi (record / 레코드). The snapshot also carries legacy `study-shelf-*` localStorage values as a khôi phục (recovery / 복구) tầng (layer / 계층). phiên bản (version / 버전) 1 Study Shelf snapshots remain importable and are migrated into the dùng chung (shared / 공유) bản ghi (record / 레코드) format.

> **Chuyển mạch:** Ở chặng này của **Dùng chung (shared / 공유) học tập (learning / 학습) Progress lược đồ (schema / 스키마)**, **Supabase bảo mật (security / 보안)** tiếp nhận điểm tựa từ **Snapshot v2** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Supabase bảo mật (security / 보안)

The di chuyển (migration / 마이그레이션) enables Row mức (level / 수준) bảo mật (security / 보안) and allows authenticated users to select, insert, cập nhật (update / 업데이트), and delete only rows whose `user_id` equals `auth.uid()`. Anonymous bảng (table / 테이블) truy cập (access / 접근) is revoked. The static frontend uses only the Supabase URL and anon key; never expose a service-role key in GitHub Pages.

> **Bàn giao:** Sau **Supabase bảo mật (security / 보안)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
