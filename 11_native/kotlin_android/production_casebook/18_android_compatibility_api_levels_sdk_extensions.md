# Case 18 — Android Compatibility Engineering: API Level, targetSdk, SDK Extensions và Platform Migration

Android compatibility không đơn giản là “code chạy trên API 26 tới API 37”. Một app phải đồng thời xử lý nhiều trục: OS version của device, `minSdk`, `compileSdk`, `targetSdk`, Jetpack/library version, hardware capability, OEM behavior và các platform behavior changes có thể áp dụng cho tất cả app hoặc chỉ app target version mới.

Chapter này xây quy trình nâng Android platform có chủ đích: hiểu loại thay đổi nào đang tác động, test bằng compatibility framework, guard API đúng, tránh non-SDK dependency và thiết kế release sao cho user update OS trước hay app trước đều không làm hệ thống vỡ.

## 1. API level là versioned platform contract

Mỗi Android platform release có API level. API level giúp compile-time/runtime code biết API nào tồn tại.

Nhưng chỉ biết `Build.VERSION.SDK_INT` không đủ. Behavior của cùng một API có thể thay đổi theo OS version và target SDK. Một permission, background rule hoặc UI behavior có thể tồn tại lâu nhưng semantics thay đổi qua nhiều release.

Compatibility engineering vì thế là quản lý **behavior contract**, không chỉ method availability.

## 2. Bốn version axis thường bị trộn lẫn

### `minSdk`

OS thấp nhất được support để cài app.

### `compileSdk`

API surface dùng để compile source.

### `targetSdk`

Version behavior contract app tuyên bố đã tương thích.

### Device OS/API level

Platform thực tế app đang chạy.

Ví dụ app có thể compile SDK 37, target 36, min 26 và chạy trên device API 37. Mỗi con số trả lời câu hỏi khác nhau.

## 3. Hai nhóm platform behavior changes

Android compatibility guidance phân biệt quan trọng:

**Changes affecting all apps**: behavior thay đổi khi app chạy trên OS mới dù targetSdk chưa tăng.

**Targeted changes**: chỉ bật khi app target API level tương ứng hoặc cao hơn.

Điều này dẫn tới hai workstream khác nhau:

```text
OS compatibility testing
= chạy current production app trên OS mới

Target SDK migration
= build app target mới và test targeted changes
```

Chỉ làm workstream thứ hai là quá muộn vì user có thể upgrade OS trước khi team tăng target.

## 4. Compatibility calendar nên bắt đầu từ preview/beta

Team production không nên đợi Play deadline mới tăng target. Một cadence tốt:

1. OS preview/beta xuất hiện → chạy smoke/critical flows với current app.
2. Inventory behavior changes for all apps.
3. Inventory targeted behavior changes.
4. Upgrade compileSdk/libraries nếu cần.
5. Fix all-app regressions trước.
6. Tạo branch/flag targetSdk migration.
7. Enable targeted changes dần bằng compat framework.
8. Test device/OEM matrix.
9. Rollout target upgrade trước policy deadline đủ xa.

Mục tiêu là tách platform migration khỏi business release pressure.

## 5. Compatibility framework giúp test change riêng lẻ

Android cung cấp compatibility framework cho nhiều behavior changes. Developer có thể bật/tắt một change bằng Developer Options hoặc ADB trên supported versions mà không luôn phải đổi target/recompile ngay.

Điều này rất hữu ích để isolate regression:

```text
current app
+ new OS
+ enable one compat change
→ test critical flow
```

Thay vì tăng target rồi gặp 15 behavior changes cùng lúc.

ADB command cụ thể thay đổi theo platform/change ID; luôn lấy ID và command từ Android behavior-changes documentation của version đang test.

## 6. API availability guard

Nếu API chỉ có từ version mới hơn minSdk:

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
    // call API introduced/required on this level
} else {
    // legacy path
}
```

Đừng chỉ guard để compiler hết warning; legacy path phải có behavior business hợp lệ.

Nếu feature không thể support OS cũ, có thể degrade gracefully thay vì giả lập behavior nguy hiểm.

## 7. `@RequiresApi` và lint

`@RequiresApi` document contract rằng caller phải chạy trên API tối thiểu. Android Lint giúp phát hiện call site không guard.

```kotlin
@RequiresApi(Build.VERSION_CODES.TIRAMISU)
fun useNewApi() { ... }
```

Annotation không tự runtime-check. Nó là static contract. Caller vẫn chịu trách nhiệm guard.

## 8. API-specific implementation bằng class isolation

Đôi khi verifier/class loading hoặc code readability tốt hơn nếu tách implementation theo version:

```kotlin
object NotificationPermissionCompat {
    fun isGranted(context: Context): Boolean {
        return if (Build.VERSION.SDK_INT >= 33) {
            Api33Impl.isGranted(context)
        } else {
            true
        }
    }

    @RequiresApi(33)
    private object Api33Impl {
        fun isGranted(context: Context): Boolean =
            ContextCompat.checkSelfPermission(
                context,
                Manifest.permission.POST_NOTIFICATIONS
            ) == PackageManager.PERMISSION_GRANTED
    }
}
```

Pattern này giữ new API reference trong implementation isolated và làm compatibility intent rõ.

## 9. Jetpack compat abstraction

Không phải mọi API-level difference cần tự viết `if SDK_INT`. Jetpack Core/Activity/Window/Media/Camera... cung cấp compatibility abstraction đã encode nhiều platform differences.

Ưu tiên stable Jetpack API khi nó thực sự giải quyết compatibility concern. Tự build wrapper platform có maintenance cost dài hạn.

Tuy nhiên wrapper không loại bỏ need hiểu underlying behavior khi debugging OEM/platform edge case.

## 10. Desugaring là compile/toolchain compatibility, không phải OS magic

Java language/API desugaring cho phép một số language/API constructs hoạt động trên OS cũ thông qua bytecode transformation/library support.

Core library desugaring có thể backport một số Java APIs, nhưng không backport Android framework API tùy ý.

Không nhìn thấy compile error không có nghĩa method framework mới sẽ chạy trên minSdk cũ.

## 11. `compileSdk` upgrade thường ít risky hơn `targetSdk` upgrade nhưng không risk-free

Tăng compileSdk chủ yếu mở API surface mới, nhưng đi kèm AGP/library/toolchain constraints và có thể expose new lint/resource behavior.

Tăng targetSdk bật behavior contract mới và cần full migration test.

Team nên tách hai change nếu project risk cao, để root cause rõ hơn.

## 12. Platform behavior matrix

Cho mỗi Android upgrade, tạo bảng:

| Change | Affects all apps? | Target-gated? | Feature impacted | Test owner | Mitigation |
|---|---|---|---|---|---|
| background restriction | maybe | yes/no | sync/media | platform team | WorkManager/FGS change |
| permission behavior | maybe | yes | location/notification | feature team | permission state machine |
| edge-to-edge | target-dependent | yes | UI | UI team | insets |
| local network | target-dependent | yes | discovery | device team | permission flow |

Không để knowledge chỉ nằm trong release notes browser tab của một developer.

## 13. Permission changes là compatibility migration điển hình

Permission có thể split thành nhiều permission mới, đổi grant behavior, auto-reset, add one-time/approximate mode hoặc thay background access flow.

Migration phải test:

- fresh install trên OS mới;
- upgrade app trên OS cũ;
- OS upgrade khi app đã cài;
- app upgrade sau OS upgrade;
- permission previously granted/denied;
- user revoke từ Settings;
- enterprise/device policy nếu applicable.

Đây là lý do Case 10 model permission như state machine thay vì boolean.

## 14. Background execution thay đổi qua platform versions

Service/background start restrictions, exact alarm, foreground-service types, JobScheduler/WorkManager behavior và battery policy đã evolve nhiều release.

Code kiểu “Service chạy được trên phone tôi” không đủ. Background architecture phải map requirement sang platform-supported primitive theo target/OS.

Nếu task durable nhưng không exact-time, WorkManager thường phù hợp hơn giữ process/service sống.

## 15. UI compatibility không chỉ screen size

Platform changes có thể ảnh hưởng status/navigation bar, edge-to-edge, predictive back, font, accessibility, gesture navigation và window management.

UI regression test khi target upgrade phải cover system bars/insets, keyboard, back gesture, rotation/resizing, large screen và accessibility—not chỉ screenshot main state.

## 16. Predictive back và system navigation contracts

Back behavior đã evolve từ hardware button mental model sang gesture/system animation contract. Modern navigation nên dùng platform/AndroidX back APIs thay vì intercept key event thủ công.

Nếu app custom back stack, test back callback registration/lifecycle và navigation transitions trên OS mới.

Compatibility principle: integrate system contract ở abstraction level chính thức, tránh hack dựa implementation detail.

## 17. SDK Extensions

Android có **SDK Extensions** để một số API capabilities được cập nhật ngoài traditional annual platform API level trên supported components.

Điều này tạo thêm version axis: device có API level X nhưng extension version Y.

Khi dùng API gated bởi extension, check extension version theo official API guidance thay vì chỉ `SDK_INT`.

Không cần mọi app dùng extension check; chỉ khi API documentation nói capability thuộc extension.

## 18. Extension version check phải gắn API contract

Pseudo-pattern:

```kotlin
val extension = SdkExtensions.getExtensionVersion(/* extension id */)
if (extension >= REQUIRED_VERSION) {
    // safe path documented for extension
}
```

ID/version cụ thể phải lấy từ docs của API. Không hardcode magic number không nguồn.

Test device/emulator cần representative extension state nếu feature phụ thuộc.

## 19. Mainline module và updatable system components

Một số Android components có thể update qua system module mechanism mà không chờ full OS OTA. Vì vậy two devices cùng API level không phải lúc nào có identical component behavior/version.

App nên dựa public capability/version checks thay vì manufacturer build fingerprint assumptions.

## 20. Non-SDK interface là technical debt nguy hiểm

Reflection vào hidden/private Android APIs có thể từng “chạy được” nhưng bị restriction ở release mới.

Non-SDK interface policy ngày càng hạn chế access. Nếu app/library phụ thuộc hidden API:

- inventory ngay;
- tìm public replacement;
- update vendor SDK;
- isolate risk;
- test latest OS preview.

Không xây core feature dựa private framework method chỉ vì StackOverflow có reflection snippet.

## 21. Reflection vào platform internals và R8 là hai risk khác nhau

Reflection app-internal có shrinker/keep-rule concern. Reflection vào Android hidden API có platform compatibility restriction concern. Có thể gặp cả hai nhưng không được nhầm.

Một reflection call fail sau OS update không nhất thiết do R8.

## 22. OEM compatibility

Android Compatibility Definition/Test Suite giảm fragmentation nhưng OEM/device-specific implementation vẫn có khác biệt: camera, BLE, background scheduling, battery manager, WebView version, graphics driver.

Không code theo brand hack ngay từ đầu. Trước tiên xác định:

1. public API contract;
2. bug có reproduce AOSP/reference device không;
3. OEM/version cohort cụ thể;
4. workaround có bounded và observable không.

Feature flag/remote config có thể giúp disable workaround theo cohort, nhưng workaround phải có expiry/cleanup owner.

## 23. WebView là independently evolving runtime

WebView behavior/version có thể update độc lập OS trên nhiều devices. Hybrid app phải log WebView version và test representative channels.

Compatibility issue JavaScript bridge, cookie, TLS, file chooser hoặc rendering không chỉ phụ thuộc API level.

Do đó bug report nên capture OS + device + WebView package/version.

## 24. Library minSdk và transitive constraints

Upgrade một Jetpack/third-party library có thể tăng minSdk hoặc yêu cầu compileSdk/toolchain mới. Dependency upgrade vì thế có thể là platform-support decision.

Before upgrade:

- đọc release notes;
- inspect minSdk/compile requirement;
- check removed/deprecated APIs;
- test binary/source compatibility;
- run minSdk device/emulator suite.

Không merge Renovate/Dependabot-style upgrade chỉ vì compile pass.

## 25. `minSdk` increase là product decision

Tăng minSdk có thể giảm compatibility burden và cho phép API hiện đại hơn, nhưng loại user/device cũ khỏi future updates/install.

Decision cần usage telemetry, security support, engineering cost, market/device cohort và Play policy—not developer preference.

Khi drop old OS, clean compatibility branches/dependencies dần để giảm permanent dead code.

## 26. Target API policy và platform release không cùng timeline

Google Play target API requirement có deadline riêng. Latest OS có thể mới hơn target requirement tại một thời điểm.

Team nên track:

```text
latest stable Android
latest preview/beta Android
current compileSdk
current targetSdk
Play minimum target requirement + deadline
minSdk support floor
```

Đừng chờ console warning mới lập kế hoạch.

## 27. Compatibility testing với ADB toggles

Ngoài compat framework, ADB giúp mô phỏng/revoke permission, force-stop, background state, process death và app ops tùy API.

Test script có thể encode regression scenario, nhưng ADB command là platform-specific tool. Giữ scripts versioned và document API range.

Automation tốt biến migration checklist thành repeatable evidence.

## 28. OS upgrade path khác fresh install

Một app cài trên Android N rồi device upgrade lên N+1 có thể giữ permission/data/state khác fresh install N+1.

Critical feature nên test cả:

```text
fresh N+1
install app on N → configure state → OS upgrade → launch on N+1
```

CI emulator upgrade automation không phải lúc nào đơn giản, nhưng release qualification lab/manual matrix có thể cover representative path.

## 29. App downgrade thường không phải supported rollback path

Android package manager thường không cho normal downgrade versionCode trên production device. Data schema mới cũng có thể không readable bởi old binary.

Vì vậy compatibility phải hướng **forward fix** và **backward-compatible data/backend** hơn là dựa user downgrade.

## 30. Backend version skew

Mobile fleet luôn có nhiều app versions cùng lúc. Backend contract phải support version skew trong window hợp lý.

Khi target SDK migration buộc app flow thay đổi, backend rollout cũng phải xem old clients.

Một server deploy phá old app còn nguy hiểm hơn target SDK bug vì user không update ngay.

## 31. Compatibility telemetry

Crash/ANR/feature failure nên segment theo:

- app version;
- OS/API level;
- target migration cohort nếu staged;
- device model/OEM;
- WebView/library relevant version;
- feature flag state.

Nếu chỉ xem global crash rate, regression chỉ xảy ra API 37 có thể bị che bởi majority API 34–36.

## 32. Migration playbook mẫu

### Phase A — inventory

Liệt kê behavior changes, permissions, background APIs, system UI, storage, hardware integrations, hidden APIs.

### Phase B — current-app compatibility

Chạy production-target app trên OS mới và fix all-app changes.

### Phase C — target-gated enablement

Dùng compat framework/toggle để bật change riêng khi có thể.

### Phase D — target bump

Tăng target, compile release artifact, run full matrix.

### Phase E — staged rollout

Monitor API-level segmented metrics.

### Phase F — cleanup

Xóa compatibility workaround obsolete, update documentation và baseline.

## 33. Senior checklist cho một Android version mới

Hỏi:

- all-app behavior change nào ảnh hưởng ngay;
- target-gated change nào sẽ bật;
- permission/system UI/background/storage có đổi không;
- third-party SDK đã certified chưa;
- non-SDK/reflection nào còn tồn tại;
- native `.so` compatible không;
- minSdk device vẫn chạy sau library/toolchain upgrade không;
- test OS upgrade/fresh install đã có chưa;
- metrics có segment API/OEM không;
- rollback/hotfix path là gì.

## 34. Official references

- App compatibility: https://developer.android.com/guide/app-compatibility
- Platform behavior changes: https://developer.android.com/about/versions
- Test/debug behavior changes: https://developer.android.com/guide/app-compatibility/test-debug
- SDK Extensions: https://developer.android.com/guide/sdk-extensions
- Target API requirements: https://developer.android.com/google/play/requirements/target-sdk

Compatibility documentation là versioned source of truth. Mỗi lần target/OS upgrade phải đọc release-specific pages, không dựa duy nhất vào memory từ release trước.