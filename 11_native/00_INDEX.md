# Phát triển di động bản địa (native mobile development / 네이티브 모바일 개발) — chỉ mục (index / 인덱스)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Phát triển di động bản địa (native mobile development / 네이티브 모바일 개발) — chỉ mục (index / 인덱스)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Swift & iOS** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Kotlin & Android** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Thư mục `11_native` chứa các bộ tài liệu bản địa (native / 네이티브) mobile theo hệ sinh thái. Mỗi bộ được tổ chức theo lộ trình từ nền tảng đến môi trường vận hành (production / 운영 환경)/master, đồng thời giữ các công nghệ legacy quan trọng để có thể đọc và maintain codebase thực tế.

## Swift & iOS

Bộ Swift/iOS được đặt riêng trong [`swift_ios/`](swift_ios/README.md), sử dụng baseline hiện hành **Xcode 27 + Swift 6.4 + iOS 27 SDK** và vẫn giữ phần di chuyển (migration / 마이그레이션)/legacy để đọc codebase Swift 5.x, UIKit, Combine, cốt lõi (core / 핵심) dữ liệu (data / 데이터) và Objective-C interop.

1. [Beginner](swift_ios/01_swift_ios_beginner.md): Swift cốt lõi (core / 핵심) từ số 0, Xcode, Foundation, SwiftUI/UIKit nhập môn, trạng thái (state / 상태)/điều hướng (navigation / 내비게이션), networking, persistence, SPM, tệp (file / 파일) hệ thống (system / 시스템), form/focus, animation/gesture, testing và signing.
2. [Intermediate](swift_ios/02_swift_ios_intermediate.md): generics/existentials, structured tính đồng thời (concurrency / 동시성), actor/Sendable/AsyncSequence, luồng dữ liệu (data flow / 데이터 흐름), networking tầng (layer / 계층), SwiftData/cốt lõi (core / 핵심) dữ liệu (data / 데이터), kiến trúc (architecture / 아키텍처), background thực thi (execution / 실행), mô-đun (module / 모듈) boundaries, sanitizers và deterministic testing.
3. [Advanced / Senior](swift_ios/03_swift_ios_advanced_senior.md): quyền sở hữu (ownership / 소유권), actor reentrancy, hiệu năng (performance / 성능), modularization, Instruments, resilient networking, cơ sở dữ liệu (database / 데이터베이스) tính đồng thời (concurrency / 동시성), bảo mật (security / 보안), CI/CD, Objective-C/C/C++ interop, môi trường vận hành (production / 운영 환경) thiết kế (design / 설계) và sự cố (incident / 인시던트) mindset.
4. [Master](swift_ios/04_swift_ios_master.md): Swift 5→6.x di chuyển (migration / 마이그레이션), Swift 6.4, ABI/thư viện (library / 라이브러리) evolution, macros, memory-safe các hệ thống (systems / 시스템들) APIs, offline sync, khả năng quan sát (observability / 관측 가능성), App Extensions, StoreKit, CloudKit, bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링) và production-readiness kiểm tra (audit / 감사).

> **Chuyển mạch:** Index đặt Kotlin/Android và Swift/iOS cạnh nhau để so sánh runtime, UI và lifecycle; trước khi chọn track, hãy chốt version baseline vì nó quyết định API, tooling và migration evidence.

## Kotlin & Android

Bộ Kotlin được đặt riêng trong [`kotlin_android/`](kotlin_android/README.md) để không trộn tệp (file / 파일) Android với iOS.

1. [Beginner](kotlin_android/01_kotlin_beginner.md): Kotlin từ số 0, Android Studio/Gradle, OOP, null-safety, collection/lambda, Android components, Compose, XML/View, tài nguyên (resource / 자원), permission và Activity kết quả (result / 결과) API.
2. [Intermediate](kotlin_android/02_kotlin_intermediate.md): Kotlin idioms/generics, coroutine/luồng (flow / 흐름), ViewModel, repository, Room, mạng (network / 네트워크), DI, WorkManager, DataStore, serialization, lưu trữ (storage / 저장소), deep link và testing.
3. [Advanced / Senior](kotlin_android/03_kotlin_advanced_senior.md): coroutine/luồng (flow / 흐름) internals, Compose thời gian chạy (runtime / 런타임), modularization, offline-first, hiệu năng (performance / 성능), R8, bảo mật (security / 보안), signing/bản phát hành (release / 릴리스), API tính tương thích (compatibility / 호환성) và môi trường vận hành (production / 운영 환경) thiết kế (design / 설계).
4. [Master](kotlin_android/04_kotlin_master.md): Kotlin 1.x→2.x/K2, JVM/bản dựng (build / 빌드) internals, large-scale kiến trúc (architecture / 아키텍처), tính tương thích (compatibility / 호환성), độ tin cậy (reliability / 신뢰성), khả năng quan sát (observability / 관측 가능성), hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링), bản phát hành (release / 릴리스)/quay lui (rollback / 롤백) và KMP awareness.

> **Chuyển mạch:** Ở chặng này của **Phát triển di động bản địa (native mobile development / 네이티브 모바일 개발) — chỉ mục (index / 인덱스)**, **Phiên bản (version / 버전) baseline của Kotlin/Android** tiếp nhận điểm tựa từ **Kotlin & Android** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Phiên bản (version / 버전) baseline của Kotlin/Android

Tại lần cập nhật 2026-09-20, bộ Kotlin dùng Kotlin 2.4.20; Android Studio Quail 4 / 2026.1.4 Patch 1; Android Gradle Plugin 9.4.1. Android 17 tương ứng API 37. Với Google Play, app mới và app cập nhật (update / 업데이트) Android thông thường từ 2026-08-31 phải mục tiêu (target / 대상) Android 16 / API 36 trở lên.

> **Bàn giao:** Sau **Phiên bản (version / 버전) baseline của Kotlin/Android**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
