# Native Mobile Development — Swift/iOS và Kotlin/Android

`11_native/` là canonical root cho phát triển ứng dụng di động bản địa (native mobile development / 네이티브 모바일 개발). Root README này chỉ làm **entrypoint ổn định**; bản đồ học chi tiết vẫn nằm tại [00_INDEX.md](./00_INDEX.md).

## Mạch đọc

Có hai track chính:

- [Swift & iOS](./swift_ios/README.md) — Swift language, SwiftUI/UIKit, concurrency, networking, persistence, architecture, performance, security, release và production engineering.
- [Kotlin & Android](./kotlin_android/README.md) — Kotlin, Android/Compose, coroutine/Flow, persistence, architecture, performance, security, release và production engineering.

Nếu chưa biết nên bắt đầu ở đâu, đọc [Native Mobile Index](./00_INDEX.md) trước để chọn track và level phù hợp.

## Coverage và ranh giới canonical

Trạng thái độ phủ, các gap chỉ nên mở khi có dependency thực và quy tắc kiểm tra version/platform claim nằm tại [COVERAGE_AUDIT.md](./COVERAGE_AUDIT.md).

Các concept chung như operating systems, networking, concurrency, databases, security và distributed systems thuộc [Computer Science](../computer_science/README.md). Backend API/auth/data contracts thuộc [Backend](../10_backend/README.md). `11_native/` tập trung vào cách các cơ chế đó xuất hiện trong runtime, lifecycle, UI framework, device capability và release pipeline của mobile platform.

Không lặp lại generic CS chapter chỉ để làm tài liệu iOS/Android dài hơn; khi cần mechanism sâu, link ngược về canonical owner.

> **Bàn giao:** Sau root entrypoint này, chuyển sang [00_INDEX.md](./00_INDEX.md), sau đó chọn [Swift/iOS](./swift_ios/README.md) hoặc [Kotlin/Android](./kotlin_android/README.md). Dùng [coverage audit](./COVERAGE_AUDIT.md) khi cần quyết định phần nào thực sự còn thiếu.