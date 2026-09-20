# Kotlin + Android Production Casebook

Thư mục này là lớp thực hành kiến trúc nằm sau `04_kotlin_master.md` và các file `deep_dive/`. Bốn file chính của bộ Kotlin + Android giải thích từng khái niệm theo level; `deep_dive/` đào sâu boundary và failure mode; còn **Production Casebook** trả lời câu hỏi khó hơn: khi một ứng dụng thật có nhiều concern cùng lúc thì ta nối chúng như thế nào để hệ thống vẫn đúng, test được, chạy ổn khi process bị kill, mạng chập chờn, schema thay đổi, hardware/permission đổi trạng thái và release gặp sự cố?

Casebook không dùng một “sample app thần thánh” rồi bắt mọi project copy nguyên cấu trúc. Mỗi chương bắt đầu từ requirement, xác định state và source of truth, đặt ownership, thiết kế boundary, sau đó mới chọn API và implementation. Cách đọc này quan trọng vì production Android không thất bại do thiếu một annotation hay quên một method riêng lẻ; nó thường thất bại ở **boundary** giữa UI và state, local và remote, token và request, navigation và process death, schema cũ và schema mới, app và system service, permission và capability, hoặc code mới và legacy code.

## Thứ tự đọc

1. [`01_architecture_end_to_end.md`](01_architecture_end_to_end.md) xây một feature hoàn chỉnh từ UI state tới repository, local database và network, đồng thời giải thích khi nào cần domain layer, module boundary và DI.
2. [`02_auth_session_network_security.md`](02_auth_session_network_security.md) thiết kế sign-in, session, access/refresh token, request authentication, concurrent refresh, logout và Credential Manager theo security boundary đúng.
3. [`03_offline_first_sync_and_database.md`](03_offline_first_sync_and_database.md) đi từ Room source of truth tới sync queue, conflict, retry, tombstone, pagination, migration và data integrity.
4. [`04_navigation_lifecycle_process_death.md`](04_navigation_lifecycle_process_death.md) nối Navigation Compose, type-safe route, deep/App Link, saved state, lifecycle, configuration change và process recreation thành một mental model thống nhất.
5. [`05_testing_performance_release.md`](05_testing_performance_release.md) xây test strategy theo risk, deterministic coroutine test, Room/network/Compose test, profiling, benchmark, CI/CD và release gate.
6. [`06_legacy_migration_and_modularization.md`](06_legacy_migration_and_modularization.md) trình bày cách migrate một codebase XML/Fragment/callback/LiveData/Rx/Java lớn sang coroutine, Flow, Compose và module boundary mà không cần rewrite toàn bộ.
7. [`07_reference_app_blueprint.md`](07_reference_app_blueprint.md) tổng hợp các chương trước thành một blueprint project production: package/module layout, state flow, error model, sync, security, test và release checklist.
8. [`08_kotlin_jvm_compiler_runtime.md`](08_kotlin_jvm_compiler_runtime.md) hạ xuống tầng Kotlin/JVM/K2: suspend state machine, inline/reified, type erasure, boxing/value class, lambda capture, Java interop, annotation target, KSP/KAPT/compiler plugin, R8 và binary compatibility.
9. [`09_android_runtime_process_thread_binder.md`](09_android_runtime_process_thread_binder.md) hạ thêm xuống Android runtime: process/app sandbox, main-thread event loop, Looper/MessageQueue/Handler, Binder IPC, ART/DEX, memory/GC, ANR và process death.
10. [`10_permissions_capabilities_system_contracts.md`](10_permissions_capabilities_system_contracts.md) xây permission/capability model theo Android version: hardware feature, runtime permission, location, Bluetooth/Nearby, local network, storage picker, foreground execution và exported component.
11. [`11_compose_ui_graphics_input_accessibility.md`](11_compose_ui_graphics_input_accessibility.md) đi sâu Compose UI system: composition/layout/draw, constraint/modifier, custom drawing/layout, gestures, focus/IME, animation, semantics/accessibility, edge-to-edge và adaptive UI.
12. [`12_media_camera_location_bluetooth_files.md`](12_media_camera_location_bluetooth_files.md) ghép các device integration thật: CameraX, Media3/audio focus, microphone, files/media picker, location/geofence, BLE/GATT, NFC/sensor, connectivity và WebView.
13. [`13_production_quality_device_matrix.md`](13_production_quality_device_matrix.md) biến knowledge thành release quality: OS/OEM/device matrix, upgrade/rollback, localization/timezone/RTL/font scale, battery/network/thermal, privacy, telemetry, feature flag và production readiness.
14. [`14_system_surfaces_services_receivers_widgets.md`](14_system_surfaces_services_receivers_widgets.md) cover các entry point ngoài Activity: Service, Receiver, Provider, notification/PendingIntent, widget, shortcut, tile, WorkManager coordination và exported-component security.

## Cách sử dụng casebook

Không nên học bằng cách copy nguyên code. Với mỗi chapter, hãy tự trả lời bốn câu trước khi nhìn implementation: state nào phải sống qua recomposition; state nào phải sống qua configuration change; state nào phải sống qua process death; dữ liệu nào phải sống qua uninstall hoặc phải được khôi phục từ server. Chỉ bốn câu này đã giúp phân biệt `remember`, `rememberSaveable`, `ViewModel`, `SavedStateHandle`, Room/DataStore và remote backend.

Sau đó hỏi tiếp: ai là source of truth, ai được quyền mutate state, code đang chạy ở thread/process/lifecycle nào, external system nào có thể fail, permission/capability nào có thể bị mất, operation nào cần idempotency, dữ liệu nào là secret, và nếu version N+1 rollback về N thì schema/data có còn đọc được hay không. Đây là các câu hỏi Senior/Master quan trọng hơn việc thuộc tên API.

Case 08–09 nên được đọc như tầng “under the hood”. Không cần áp dụng bytecode/Binder reasoning vào mọi dòng code; hãy dùng khi abstraction leak: build/plugin incompatibility, Java interop kỳ lạ, coroutine stack khó hiểu, memory/performance hotspot, ANR, reflection/R8 issue, IPC hoặc binary compatibility problem.

Case 10–14 là tầng “Android platform contract”. Chúng giúp trả lời những câu hỏi mà architecture thuần Kotlin không giải thích được: vì sao permission cũ đổi behavior khi target SDK tăng, vì sao camera/BLE phải có state machine riêng, vì sao accessibility nằm trong semantics tree, vì sao notification tap phải hoạt động khi process cold-start, và vì sao widget/service/receiver không được xem như cách giữ app sống.

## Nguyên tắc xuyên suốt

Casebook sử dụng một số quy ước nhất quán. UI render từ immutable `UiState` và gửi event xuống; `ViewModel` điều phối screen state nhưng không trở thành database/network god object; repository sở hữu data contract và giải quyết nhiều data source; local database thường là source of truth cho feature offline-first; network DTO không đi thẳng lên UI; coroutine phải có ownership/lifetime rõ ràng; cancellation không được nuốt; error được phân loại theo transport/protocol/domain thay vì một `Exception` chung; authentication và authorization không bị nhầm lẫn; client không được coi là trusted environment; permission không được nhầm với business entitlement; system component/external Intent được coi là boundary không tin cậy; migration phải được test bằng dữ liệu của schema cũ; release phải có khả năng quan sát và rollback.

Những nguyên tắc này không có nghĩa mọi app phải nhiều module, Clean Architecture đầy đủ hoặc có use case cho từng method. Complexity chỉ được thêm khi nó mua được một lợi ích rõ ràng: boundary dễ test hơn, ownership rõ hơn, build nhanh hơn, feature độc lập hơn, platform failure dễ recover hơn, hoặc migration/risk dễ kiểm soát hơn.
