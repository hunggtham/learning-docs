# Case 10 — Permissions, Device Capability và System Contract

Android permission thường bị học như một danh sách `Manifest.permission.*`, nhưng production bug hiếm khi đến từ việc “không nhớ tên permission”. Vấn đề thật thường là app nhầm **permission với capability**, request quá sớm, giữ permission như điều kiện tồn tại của feature, không xử lý denial/revocation, hoặc không hiểu rằng behavior phụ thuộc cả OS version lẫn `targetSdk`.

Chapter này xây mental model theo thứ tự: feature requirement → hardware/software capability → manifest declaration → runtime permission → special access → user intent → fallback → lifecycle/revocation → version behavior.

## 1. Permission không đồng nghĩa capability

Thiết bị có thể không có camera, Bluetooth, GPS, telephony hoặc NFC. Ngược lại, device có capability nhưng user không grant permission. Vì vậy hai câu hỏi phải tách riêng:

```text
Device có khả năng này không?
User/system có cho app sử dụng nó lúc này không?
```

Ví dụ camera:

```kotlin
val hasCamera = context.packageManager.hasSystemFeature(
    PackageManager.FEATURE_CAMERA_ANY
)
```

Sau đó mới xét runtime permission nếu use case cần trực tiếp truy cập camera.

## 2. `<uses-feature>` ảnh hưởng khả năng cài app

Khai báo hardware feature với `android:required="true"` có thể khiến Google Play lọc thiết bị không có feature đó. Nếu camera chỉ là optional enhancement, nên khai báo `required="false"` và cung cấp fallback.

Ví dụ:

```xml
<uses-feature
    android:name="android.hardware.camera.any"
    android:required="false" />
```

Điều này rất quan trọng với tablet, Chromebook, foldable, external camera và form factor khác. Production app không nên vô tình giảm device availability chỉ vì manifest declaration quá mạnh.

## 3. Permission nên gắn với user action

Request permission ngay khi mở app làm user khó hiểu tại sao app cần quyền. Flow tốt hơn là user bấm “Scan QR”, app giải thích use case nếu cần rồi request camera.

```text
User intent
→ check capability
→ check permission
→ explain if needed
→ request
→ execute feature
→ fallback nếu denied
```

Permission UX là một phần product architecture, không chỉ technical API.

## 4. Runtime permission là state có thể thay đổi

Đừng cache `permissionGranted = true` vĩnh viễn. User có thể revoke permission trong Settings, policy có thể thay đổi, permission có thể auto-reset sau thời gian dài không dùng app.

Mỗi lần feature thực sự cần capability, hãy check lại state theo contract của API.

## 5. Activity Result API cho permission

Code hiện đại dùng Activity Result API thay vì override `onRequestPermissionsResult()` thủ công.

```kotlin
val cameraPermission = rememberLauncherForActivityResult(
    ActivityResultContracts.RequestPermission()
) { granted ->
    if (granted) {
        openScanner()
    }
}
```

Trong Compose, launcher nên được tạo ở composition scope phù hợp; user event kích hoạt `launch()`.

## 6. `shouldShowRequestPermissionRationale()` không phải business state hoàn chỉnh

API này chỉ cung cấp tín hiệu platform để quyết định có nên giải thích thêm hay không. Đừng biến nó thành logic “nếu false thì user đã chọn Never ask again” tuyệt đối trong mọi version/device.

Thiết kế UI theo outcome: granted, denied nhưng có thể request lại, hoặc feature hiện cần dẫn user tới Settings. Luôn có fallback rõ.

# Location

## 7. Coarse và precise location

Android hiện đại cho user quyền chia sẻ approximate location thay vì precise. Nếu app chỉ cần thành phố/khu vực, hãy thiết kế để `ACCESS_COARSE_LOCATION` đủ.

Nếu business logic yêu cầu precise, giải thích rõ lý do tại thời điểm feature cần.

Không yêu cầu precise chỉ vì API sample dùng nó.

## 8. Foreground và background location là hai mức trust khác nhau

Background location là sensitive capability cao hơn nhiều. App cần chứng minh use case thực sự cần location khi user không tương tác trực tiếp.

Các app navigation, fitness tracking hoặc safety có thể có lý do; app thương mại thông thường không nên lấy background location chỉ để “analytics tốt hơn”.

Về architecture, hãy tách:

```text
feature foreground location
feature background tracking
```

vì permission, policy, battery và foreground-service requirement khác nhau.

## 9. Location unavailable không phải exceptional crash case

Location có thể unavailable vì permission denied, sensor disabled, indoor environment, device không có hardware, policy hoặc timeout. API layer nên model điều này như state/domain outcome thay vì throw một exception chung rồi UI hiện “Unknown error”.

# Bluetooth và Nearby Devices

## 10. Bluetooth permission thay đổi mạnh từ Android 12

Với target Android 12+, Bluetooth scan/connect/advertise dùng nhóm permission mới như `BLUETOOTH_SCAN`, `BLUETOOTH_CONNECT`, `BLUETOOTH_ADVERTISE` thay vì chỉ dựa vào location permission như các version cũ.

Nếu scan không dùng để suy ra physical location, manifest có thể dùng `neverForLocation` trong trường hợp phù hợp. Nhưng assertion này phải đúng với product behavior.

## 11. Companion Device Manager khi app ghép thiết bị companion

Nếu app pair với wearable, accessory hoặc IoT companion, `CompanionDeviceManager` có thể cung cấp system-mediated pairing UX và giảm nhu cầu permission/location ở một số flow.

Senior decision không phải “luôn scan BLE trực tiếp”, mà là hỏi system-mediated API có phù hợp không.

## 12. Bluetooth state machine

BLE code production nên model connection lifecycle:

```text
Idle
→ Scanning
→ DeviceFound
→ Connecting
→ DiscoveringServices
→ Ready
→ Disconnecting
→ Disconnected / Error
```

Đừng dùng một boolean `isConnected`. Connection có timeout, reconnect, permission revoke, Bluetooth disabled và remote disconnect.

# Android 17 Local Network

## 13. `ACCESS_LOCAL_NETWORK`

Android 17 bổ sung runtime permission cho app target API 37+ khi cần discover/communicate với thiết bị trong LAN trong những flow áp dụng. Đây là ví dụ điển hình của platform evolution: capability trước đây “tự do” có thể trở thành protected surface vì privacy/fingerprinting risk.

Nếu app điều khiển smart-home/casting/local server, phải kiểm tra migration khi nâng target SDK. Một option khác trong một số use case là system-mediated picker giúp user chọn local device mà không cần broad network discovery permission.

Target SDK migration vì vậy phải có **capability audit**, không chỉ tăng con số trong Gradle.

# Notifications

## 14. Notification permission

Trên Android hiện đại, app không được giả định notification luôn hiển thị. User có thể deny permission hoặc disable channel.

Business flow quan trọng không được phụ thuộc notification như kênh duy nhất để đảm bảo data correctness. Notification là delivery surface, không phải durable job queue.

Ví dụ sync background vẫn phải persist state; notification chỉ báo outcome.

## 15. Notification channel là user-controlled contract

Sau khi channel được tạo, user có quyền chỉnh importance/sound. App không nên liên tục tạo channel mới để né setting của user.

Thiết kế channel theo semantic ổn định như:

```text
messages
orders
security_alerts
background_progress
```

thay vì theo từng campaign/version.

## 16. PendingIntent mutability

Khi tạo `PendingIntent`, cần chọn immutable/mutable đúng contract. Mặc định nên immutable nếu receiver không cần system/other process fill thêm extras theo use case hợp lệ.

Security principle: capability token càng hẹp càng tốt.

# Camera và Microphone

## 17. Permission indicator và user expectation

Camera/microphone là high-trust capability. Hệ thống có privacy indicators và user controls. App nên bắt đầu capture rõ ràng sau user intent, dừng capture đúng lifecycle và không giữ resource ở background không cần thiết.

## 18. Camera permission không có nghĩa camera đang usable

Camera có thể đang được app khác sử dụng, lifecycle chưa ready hoặc hardware error. Camera layer phải model open/close/error thay vì chỉ check permission.

CameraX thường giảm complexity so với Camera2 cho app phổ biến, nhưng vẫn phải bind use case vào lifecycle đúng cách.

# Storage, media và file access

## 19. Không xin storage permission nếu system picker đủ dùng

Nếu user chọn ảnh/video, Photo Picker thường là surface tốt hơn broad media permission. Nếu user chọn document/file, Storage Access Framework cho phép user grant URI access cụ thể.

Principle:

```text
request narrow user-selected access
trước khi
request broad library access
```

Điều này giảm privacy surface và permission rejection.

## 20. URI permission

Khi nhận `content://` URI, app không nên assume có filesystem path thật. Dùng `ContentResolver` để mở stream/file descriptor.

```kotlin
context.contentResolver.openInputStream(uri)?.use { input ->
    // consume stream
}
```

Nếu cần access lâu dài cho document từ SAF, có thể cần persist URI permission theo contract của picker.

## 21. `FileProvider` cho share file

Không expose raw `file://` path. Dùng `FileProvider`/content URI với temporary grant.

Intent sharing phải grant permission đúng scope và không expose file private ngoài ý muốn.

# Foreground Service và background execution

## 22. Permission không thể tách khỏi execution policy

Một app có location permission chưa chắc được phép chạy tracking vô hạn ở background. Android áp foreground-service type, background start restriction và battery policy.

Khi feature cần user-visible long-running work, foreground service có thể đúng. Khi work durable nhưng không cần exact-time/user-visible, WorkManager thường phù hợp hơn.

Đừng dùng foreground service như cách “giữ app sống”.

## 23. Exact alarm là special capability

Exact alarm ảnh hưởng battery và bị platform/policy quản lý. Chỉ use case thật sự exact-time như alarm clock/calendar-critical event mới nên dựa vào nó.

Periodic sync nên dùng WorkManager/flexible scheduling hơn.

# Intents, exported component và external input

## 24. `android:exported`

Component nhận implicit intent hoặc cần external access phải có exported configuration rõ. Component nội bộ nên không exported nếu không cần.

Đừng coi Activity/Service/Receiver exported chỉ là navigation detail; đó là attack surface.

## 25. Intent input phải validate

Deep link như:

```text
myapp://payment/confirm?amount=...
```

không được tin amount/role/userId chỉ vì link mở từ app của bạn. External source có thể craft Intent.

Server-side authorization và domain validation vẫn là nguồn quyết định.

## 26. App Links tốt hơn custom scheme cho web ownership

Verified App Links liên kết HTTP(S) domain với app ownership, giảm hijacking so với custom URI scheme trong nhiều use case.

Navigation layer nên parse thành typed route/domain input rồi validate thay vì truyền URI string đi khắp app.

# Special App Access

## 27. Một số capability không phải runtime permission bình thường

Draw over other apps, manage all files, install unknown apps, exact alarms hoặc accessibility service có system setting/special access flow riêng. Không được request/khuyến khích chỉ vì muốn shortcut kỹ thuật.

Nếu app cần special access, UX phải giải thích benefit cụ thể và feature vẫn degrade hợp lý khi user không cấp.

# Capability architecture

## 28. Tạo abstraction theo capability, không theo permission API

UI không nên biết chi tiết API level branching:

```kotlin
interface CameraCapability {
    suspend fun ensureReady(): CapabilityResult
}
```

Implementation có thể check hardware, permission, policy và lifecycle. UI chỉ render state:

```kotlin
sealed interface CapabilityResult {
    data object Ready : CapabilityResult
    data object Unsupported : CapabilityResult
    data object PermissionRequired : CapabilityResult
    data object DisabledBySystem : CapabilityResult
}
```

Cách này làm test dễ hơn và tránh permission logic rải khắp Composable.

## 29. Permission state không phải domain entitlement

User có camera permission không có nghĩa account được phép dùng feature premium. Ngược lại, subscription entitlement không có nghĩa OS permission đã grant.

Tách:

```text
OS capability/permission
business entitlement
backend authorization
```

ba layer khác nhau.

# Version matrix

## 30. `minSdk`, `targetSdk`, runtime OS

Một app có thể:

```text
minSdk = 26
targetSdk = 37
chạy trên device API 29, 34, 37...
```

Behavior phụ thuộc cả runtime OS và target SDK. Vì vậy code compatibility thường cần xét:

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.X) {
    // API mới
}
```

nhưng target-specific behavior không phải lúc nào cũng chỉ giải bằng `SDK_INT`; phải đọc behavior changes khi nâng target.

## 31. Target SDK migration checklist

Mỗi lần tăng target SDK, review ít nhất: permissions mới/đổi semantics, background execution, foreground-service types, notification, storage/media, intents/exported components, security/network, edge-to-edge/system UI, accessibility/IME, WebView behavior và hardware capability.

Android 17 là ví dụ rõ với local network permission, MessageQueue implementation change, background audio tightening và các behavior khác.

# Testing permission/capability

## 32. Test matrix

Permission feature nên test ít nhất:

| Scenario | Kỳ vọng |
|---|---|
| hardware absent | fallback rõ |
| permission granted | feature chạy |
| denied lần đầu | explain/retry hợp lý |
| denied lâu dài | Settings/fallback |
| revoke khi app background | app recover |
| OS version cũ | compatibility path |
| target-SDK behavior mới | migration path |

## 33. Đừng chỉ test emulator “happy path”

Bluetooth, camera, audio, sensor, foldable posture hoặc OEM permission behavior cần physical-device matrix khi risk cao. Emulator hữu ích nhưng không thay hết hardware integration.

# Senior Notes

## 34. Permission tối thiểu là security và product quality

Ít permission hơn không chỉ giảm risk; nó giảm dialog, denial state, support burden, Play policy surface và code branch.

## 35. System picker thường thắng custom broad access

Photo Picker, document picker, Credential Manager, Companion Device Manager và các system-mediated flow tồn tại để user grant access cụ thể với trust UX nhất quán. Dùng chúng khi phù hợp thay vì tự xây broad-scanning architecture.

## 36. Capability phải có fallback

Nếu app crash hoặc khóa toàn bộ flow chỉ vì camera/Bluetooth/location unavailable, architecture đang coupling feature quá chặt với hardware.

## 37. Permission denial là normal user choice

Đừng dùng dark pattern ép user grant. Product tốt giải thích value và vẫn cho user đường khác nếu possible.

# Checklist kết thúc chapter

Bạn nên có thể giải thích sự khác nhau giữa permission và hardware capability; vì sao `<uses-feature>` có thể ảnh hưởng Play availability; khi nào dùng system picker thay broad permission; vì sao permission có thể bị revoke; Bluetooth permission hiện đại khác legacy thế nào; Android 17 local-network permission ảnh hưởng app LAN ra sao; vì sao URI không phải filesystem path; foreground service khác WorkManager; `android:exported` và PendingIntent liên quan security thế nào; và tại sao target-SDK upgrade phải được xem như platform migration project chứ không phải sửa một số trong Gradle.
