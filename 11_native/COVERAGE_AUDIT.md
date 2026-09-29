# Native Mobile Development — Coverage Audit

> **Mạch đọc:** Đặt audit này cạnh [README](./README.md) và [00_INDEX](./00_INDEX.md). README là entrypoint ổn định, `00_INDEX.md` giữ learning map chi tiết; audit này chỉ ghi trạng thái coverage, ranh giới sở hữu và điều kiện cần rà soát lại.

Cập nhật: **2026-09-29**. `main` là nguồn chuẩn (source of truth / 정본) sau khi thay đổi được merge.

## Phạm vi và canonical owner

`11_native/` sở hữu kiến thức phát triển ứng dụng mobile bản địa (native mobile development / 네이티브 모바일 개발) theo hai track:

```text
Native Mobile
├── Swift / iOS
└── Kotlin / Android
```

Mỗi track đi từ ngôn ngữ và platform foundation tới concurrency, persistence, networking, architecture, security, performance, testing, build/release và production engineering.

Các cơ chế tổng quát không được copy lại nếu đã có canonical owner khác: thuật toán/hệ điều hành/mạng/cơ sở dữ liệu thuộc `computer_science/`; API/backend contract thuộc `10_backend/`; CI/CD, observability và platform operations thuộc `devops_platform_engineering/`.

## Trạng thái coverage

| Vùng | Coverage | Trạng thái |
|---|---|---|
| Swift language + iOS foundations | beginner → intermediate → advanced → master | Strong |
| Swift concurrency / ownership / interoperability | structured concurrency, actor/Sendable, Objective-C/C/C++ interop | Strong |
| iOS UI / state / navigation / persistence / networking | SwiftUI, UIKit và production boundaries | Strong |
| iOS production engineering | performance, security, release, observability, offline/sync | Strong |
| Kotlin language + Android foundations | beginner → intermediate → advanced → master | Strong |
| Kotlin coroutine / Flow / Android runtime | concurrency, lifecycle, Compose/runtime reasoning | Strong |
| Android data / networking / background work | Room, DataStore, WorkManager, offline-first | Strong |
| Android production engineering | R8, signing, security, performance, release/rollback | Strong |

## Bất biến cần giữ

Một chapter native chỉ được coi là đủ sâu khi người đọc hiểu được **platform lifecycle**, **state ownership**, **thread/concurrency boundary**, **persistence/network failure**, **security boundary**, **resource/performance cost** và **release/recovery path**. Framework hoặc API cụ thể không thay thế các cơ chế này.

Version/platform claim là dữ liệu thay đổi theo thời gian. Các thông tin như Xcode, Swift, iOS SDK, Kotlin, Android Studio, AGP, Android API level hoặc yêu cầu store phải có **ngày kiểm tra** và khi cập nhật phải đối chiếu nguồn chính thức; không biến version hiện tại thành kiến thức vĩnh viễn.

## Gaps còn lại

Không có gap P0/P1 về learning spine tại lần audit này. Chỉ mở rộng khi có dependency thực, ưu tiên:

1. case end-to-end về offline conflict, sync và recovery giữa client–backend;
2. production incident case về memory/performance/battery/network degradation;
3. platform migration case khi Swift/Kotlin/SDK thay đổi làm xuất hiện cơ chế hoặc failure mode mới;
4. cross-platform awareness chỉ ở mức boundary/comparison, không biến domain native thành catalog framework đa nền tảng.

## Review protocol

Khi sửa domain này:

1. kiểm tra `README.md` và `00_INDEX.md` vẫn trỏ đúng hai track;
2. giữ beginner → master như learning spine nhưng giải thích theo mechanism, không theo danh sách API;
3. với version/store policy, ghi ngày kiểm tra và nguồn chính thức;
4. kiểm tra internal links và handoff sang Computer Science, Backend, DevOps;
5. chỉ đổi trạng thái coverage khi có bằng chứng từ chapter/case cụ thể.

> **Bàn giao:** Bắt đầu học tại [README](./README.md); dùng [00_INDEX](./00_INDEX.md) để chọn Swift/iOS hoặc Kotlin/Android. Audit này chỉ dùng để quyết định nên mở rộng domain ở đâu, không thay thế learning material.