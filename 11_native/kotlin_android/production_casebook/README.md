# Kotlin + Android Production Casebook

Thư mục này là lớp thực hành kiến trúc nằm sau `04_kotlin_master.md` và các file `deep_dive/`. Bốn file chính của bộ Kotlin + Android giải thích từng khái niệm theo level; `deep_dive/` đào sâu boundary và failure mode; còn **Production Casebook** trả lời câu hỏi khó hơn: khi một ứng dụng thật có nhiều concern cùng lúc thì ta nối chúng như thế nào để hệ thống vẫn đúng, test được, chạy ổn khi process bị kill, mạng chập chờn, schema thay đổi và release gặp sự cố?

Casebook không dùng một “sample app thần thánh” rồi bắt mọi project copy nguyên cấu trúc. Mỗi chương bắt đầu từ requirement, xác định state và source of truth, đặt ownership, thiết kế boundary, sau đó mới chọn API và implementation. Cách đọc này quan trọng vì production Android không thất bại do thiếu một annotation hay quên một method riêng lẻ; nó thường thất bại ở **boundary** giữa UI và state, local và remote, token và request, navigation và process death, schema cũ và schema mới, hoặc code mới và legacy code.

## Thứ tự đọc

1. [`01_architecture_end_to_end.md`](01_architecture_end_to_end.md) xây một feature hoàn chỉnh từ UI state tới repository, local database và network, đồng thời giải thích khi nào cần domain layer, module boundary và DI.
2. [`02_auth_session_network_security.md`](02_auth_session_network_security.md) thiết kế sign-in, session, access/refresh token, request authentication, concurrent refresh, logout và Credential Manager theo security boundary đúng.
3. [`03_offline_first_sync_and_database.md`](03_offline_first_sync_and_database.md) đi từ Room source of truth tới sync queue, conflict, retry, tombstone, pagination, migration và data integrity.
4. [`04_navigation_lifecycle_process_death.md`](04_navigation_lifecycle_process_death.md) nối Navigation Compose, type-safe route, deep/App Link, saved state, lifecycle, configuration change và process recreation thành một mental model thống nhất.
5. [`05_testing_performance_release.md`](05_testing_performance_release.md) xây test strategy theo risk, deterministic coroutine test, Room/network/Compose test, profiling, benchmark, CI/CD và release gate.
6. [`06_legacy_migration_and_modularization.md`](06_legacy_migration_and_modularization.md) trình bày cách migrate một codebase XML/Fragment/callback/LiveData/Rx/Java lớn sang coroutine, Flow, Compose và module boundary mà không cần rewrite toàn bộ.
7. [`07_reference_app_blueprint.md`](07_reference_app_blueprint.md) tổng hợp các chương trước thành một blueprint project production: package/module layout, state flow, error model, sync, security, test và release checklist.
8. [`08_kotlin_jvm_compiler_runtime.md`](08_kotlin_jvm_compiler_runtime.md) hạ xuống tầng Kotlin/JVM/K2: suspend state machine, inline/reified, type erasure, boxing/value class, lambda capture, Java interop, annotation target, KSP/KAPT/compiler plugin, R8 và binary compatibility.

## Cách sử dụng casebook

Không nên học bằng cách copy nguyên code. Với mỗi chapter, hãy tự trả lời bốn câu trước khi nhìn implementation: state nào phải sống qua recomposition; state nào phải sống qua configuration change; state nào phải sống qua process death; dữ liệu nào phải sống qua uninstall hoặc phải được khôi phục từ server. Chỉ bốn câu này đã giúp phân biệt `remember`, `rememberSaveable`, `ViewModel`, `SavedStateHandle`, Room/DataStore và remote backend.

Sau đó hỏi tiếp: ai là source of truth, ai được quyền mutate state, failure nào retry được, operation nào cần idempotency, dữ liệu nào là secret, và nếu version N+1 rollback về N thì schema/data có còn đọc được hay không. Đây là các câu hỏi Senior/Master quan trọng hơn việc thuộc tên API.

Sau Case 07, Case 08 nên được đọc như tầng “under the hood”. Không cần áp dụng bytecode reasoning vào mọi dòng code; hãy dùng nó khi abstraction leak: build/plugin incompatibility, Java interop kỳ lạ, coroutine stack khó hiểu, memory/performance hotspot, reflection/R8 issue hoặc binary compatibility problem.

## Nguyên tắc xuyên suốt

Casebook sử dụng một số quy ước nhất quán. UI render từ immutable `UiState` và gửi event xuống; `ViewModel` điều phối screen state nhưng không trở thành database/network god object; repository sở hữu data contract và giải quyết nhiều data source; local database thường là source of truth cho feature offline-first; network DTO không đi thẳng lên UI; coroutine phải có ownership/lifetime rõ ràng; cancellation không được nuốt; error được phân loại theo transport/protocol/domain thay vì một `Exception` chung; authentication và authorization không bị nhầm lẫn; client không được coi là trusted environment; migration phải được test bằng dữ liệu của schema cũ; release phải có khả năng quan sát và rollback.

Những nguyên tắc này không có nghĩa mọi app phải nhiều module, Clean Architecture đầy đủ hoặc có use case cho từng method. Complexity chỉ được thêm khi nó mua được một lợi ích rõ ràng: boundary dễ test hơn, ownership rõ hơn, build nhanh hơn, feature độc lập hơn, hoặc migration/risk dễ kiểm soát hơn.
