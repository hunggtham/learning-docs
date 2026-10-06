# Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**. Route đi từ feature requirement → hardware/software capability → manifest/uses-feature → runtime permission và special access → user intent, fallback, revocation và version behavior.

Android permission thường bị học như một danh sách `Manifest.permission.*`, nhưng môi trường vận hành (production / 운영 환경) bug hiếm khi đến từ việc “không nhớ tên permission”. Vấn đề thật thường là app nhầm **permission với năng lực (capability / 역량)**, yêu cầu (request / 요청) quá sớm, giữ permission như điều kiện tồn tại của tính năng (feature / 기능), không xử lý denial/revocation, hoặc không hiểu rằng hành vi (behavior / 동작) phụ thuộc cả OS phiên bản (version / 버전) lẫn `targetSdk`.

Chapter này xây mô hình tư duy (mental model / 사고 모델) theo thứ tự: tính năng (feature / 기능) yêu cầu (requirement / 요구사항) → hardware/software năng lực (capability / 역량) → manifest declaration → thời gian chạy (runtime / 런타임) permission → special truy cập (access / 접근) → người dùng (user / 사용자) intent → fallback → vòng đời (lifecycle / 생명주기)/revocation → phiên bản (version / 버전) hành vi (behavior / 동작).

## 1. Permission không đồng nghĩa năng lực (capability / 역량)

Thiết bị có thể không có camera, Bluetooth, GPS, telephony hoặc NFC. Ngược lại, thiết bị (device / 장치) có năng lực (capability / 역량) nhưng người dùng (user / 사용자) không grant permission. Vì vậy hai câu hỏi phải tách riêng:

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

Sau đó mới xét thời gian chạy (runtime / 런타임) permission nếu use trường hợp (case / 사례) cần trực tiếp truy cập camera.

> **Nối mạch:** Permission cấp quyền runtime, còn `<uses-feature>` mô tả capability và có thể ảnh hưởng install filtering; request permission nên gắn với user action cụ thể.

## 2. `<uses-feature>` ảnh hưởng khả năng cài app

Khai báo hardware tính năng (feature / 기능) với `android:required="true"` có thể khiến Google Play lọc thiết bị không có tính năng (feature / 기능) đó. Nếu camera chỉ là optional enhancement, nên khai báo `required="false"` và cung cấp fallback.

Ví dụ:

```xml
<uses-feature
    android:name="android.hardware.camera.any"
    android:required="false" />
```

Điều này rất quan trọng với tablet, Chromebook, foldable, bên ngoài (external / 외부) camera và form factor khác. môi trường vận hành (production / 운영 환경) app không nên vô tình giảm thiết bị (device / 장치) availability chỉ vì manifest declaration quá mạnh.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **3. Permission nên gắn với người dùng (user / 사용자) hành động (action / 동작)** nối từ **2. <uses-feature> ảnh hưởng khả năng cài app** sang **4. thời gian chạy (runtime / 런타임) permission là trạng thái (state / 상태) có thể thay đổi**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Permission nên gắn với người dùng (user / 사용자) hành động (action / 동작)

Yêu cầu (request / 요청) permission ngay khi mở app làm người dùng (user / 사용자) khó hiểu tại sao app cần quyền. luồng (flow / 흐름) tốt hơn là người dùng (user / 사용자) bấm “Scan QR”, app giải thích use trường hợp (case / 사례) nếu cần rồi yêu cầu (request / 요청) camera.

```text
User intent
→ check capability
→ check permission
→ explain if needed
→ request
→ execute feature
→ fallback nếu denied
```

Permission UX là một phần sản phẩm (product / 제품) kiến trúc (architecture / 아키텍처), không chỉ technical API.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **4. thời gian chạy (runtime / 런타임) permission là trạng thái (state / 상태) có thể thay đổi** nối từ **3. Permission nên gắn với người dùng (user / 사용자) hành động (action / 동작)** sang **5. Activity kết quả (result / 결과) API cho permission**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. thời gian chạy (runtime / 런타임) permission là trạng thái (state / 상태) có thể thay đổi

Đừng bộ nhớ đệm (cache / 캐시) `permissionGranted = true` vĩnh viễn. người dùng (user / 사용자) có thể revoke permission trong Settings, chính sách (policy / 정책) có thể thay đổi, permission có thể auto-reset sau thời gian dài không dùng app.

Mỗi lần tính năng (feature / 기능) thực sự cần năng lực (capability / 역량), hãy check lại trạng thái (state / 상태) theo đặc tả hợp đồng (contract / 계약) của API.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **5. Activity kết quả (result / 결과) API cho permission** nối từ **4. thời gian chạy (runtime / 런타임) permission là trạng thái (state / 상태) có thể thay đổi** sang **6. shouldShowRequestPermissionRationale() không phải nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) hoàn chỉnh**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Activity kết quả (result / 결과) API cho permission

Mã (code / 코드) hiện đại dùng Activity kết quả (result / 결과) API thay vì override `onRequestPermissionsResult()` thủ công.

```kotlin
val cameraPermission = rememberLauncherForActivityResult(
    ActivityResultContracts.RequestPermission()
) { granted ->
    if (granted) {
        openScanner()
    }
}
```

Trong Compose, launcher nên được tạo ở composition phạm vi (scope / 범위) phù hợp; người dùng (user / 사용자) sự kiện (event / 이벤트) kích hoạt `launch()`.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **6. shouldShowRequestPermissionRationale() không phải nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) hoàn chỉnh** nối từ **5. Activity kết quả (result / 결과) API cho permission** sang **7. Coarse và precise location**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. `shouldShowRequestPermissionRationale()` không phải nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) hoàn chỉnh

API này chỉ cung cấp tín hiệu nền tảng (platform / 플랫폼) để quyết định có nên giải thích thêm hay không. Đừng biến nó thành lô-gic (logic / 논리) “nếu false thì người dùng (user / 사용자) đã chọn Never ask again” tuyệt đối trong mọi phiên bản (version / 버전)/thiết bị (device / 장치).

Thiết kế UI theo kết quả (outcome / 결과): granted, denied nhưng có thể yêu cầu (request / 요청) lại, hoặc tính năng (feature / 기능) hiện cần dẫn người dùng (user / 사용자) tới Settings. Luôn có fallback rõ.

# Location

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **7. Coarse và precise location** nối từ **6. shouldShowRequestPermissionRationale() không phải nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) hoàn chỉnh** sang **8. Foreground và background location là hai mức trust khác nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Coarse và precise location

Android hiện đại cho người dùng (user / 사용자) quyền chia sẻ approximate location thay vì precise. Nếu app chỉ cần thành phố/khu vực, hãy thiết kế để `ACCESS_COARSE_LOCATION` đủ.

Nếu lô-gic nghiệp vụ (business logic / 비즈니스 로직) yêu cầu precise, giải thích rõ lý do tại thời điểm tính năng (feature / 기능) cần.

Không yêu cầu precise chỉ vì API mẫu (sample / 표본) dùng nó.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **8. Foreground và background location là hai mức trust khác nhau** nối từ **7. Coarse và precise location** sang **9. Location unavailable không phải exceptional crash trường hợp (case / 사례)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Foreground và background location là hai mức trust khác nhau

Background location là sensitive năng lực (capability / 역량) cao hơn nhiều. App cần chứng minh use trường hợp (case / 사례) thực sự cần location khi người dùng (user / 사용자) không tương tác trực tiếp.

Các app điều hướng (navigation / 내비게이션), fitness tracking hoặc an toàn (safety / 안전) có thể có lý do; app thương mại thông thường không nên lấy background location chỉ để “analytics tốt hơn”.

Về kiến trúc (architecture / 아키텍처), hãy tách:

```text
feature foreground location
feature background tracking
```

vì permission, chính sách (policy / 정책), battery và foreground-service yêu cầu (requirement / 요구사항) khác nhau.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **8. Foreground và background location là hai mức trust khác nhau** nêu quy tắc; **9. Location unavailable không phải exceptional crash trường hợp (case / 사례)** thử quy tắc trong tình huống, rồi **10. Bluetooth permission thay đổi mạnh từ Android 12** mở rộng hệ quả.

## 9. Location unavailable không phải exceptional crash trường hợp (case / 사례)

Location có thể unavailable vì permission denied, sensor disabled, indoor môi trường (environment / 환경), thiết bị (device / 장치) không có hardware, chính sách (policy / 정책) hoặc hết thời gian chờ (timeout / 타임아웃). API tầng (layer / 계층) nên mô hình (model / 모델) điều này như trạng thái (state / 상태)/lĩnh vực (domain / 도메인) kết quả (outcome / 결과) thay vì throw một exception chung rồi UI hiện “Unknown lỗi (error / 오류)”.

# Bluetooth và Nearby Devices

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **9. Location unavailable không phải exceptional crash trường hợp (case / 사례)** nêu quy tắc; **10. Bluetooth permission thay đổi mạnh từ Android 12** thử quy tắc trong tình huống, rồi **11. Companion thiết bị (device / 장치) Manager khi app ghép thiết bị companion** mở rộng hệ quả.

## 10. Bluetooth permission thay đổi mạnh từ Android 12

Với mục tiêu (target / 대상) Android 12+, Bluetooth scan/connect/advertise dùng nhóm permission mới như `BLUETOOTH_SCAN`, `BLUETOOTH_CONNECT`, `BLUETOOTH_ADVERTISE` thay vì chỉ dựa vào location permission như các phiên bản (version / 버전) cũ.

Nếu scan không dùng để suy ra vật lý (physical / 물리적) location, manifest có thể dùng `neverForLocation` trong trường hợp phù hợp. Nhưng assertion này phải đúng với sản phẩm (product / 제품) hành vi (behavior / 동작).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **11. Companion thiết bị (device / 장치) Manager khi app ghép thiết bị companion** nối từ **10. Bluetooth permission thay đổi mạnh từ Android 12** sang **12. Bluetooth máy trạng thái (state machine / 상태 머신)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Companion thiết bị (device / 장치) Manager khi app ghép thiết bị companion

Nếu app pair với wearable, accessory hoặc IoT companion, `CompanionDeviceManager` có thể cung cấp system-mediated pairing UX và giảm nhu cầu permission/location ở một số luồng (flow / 흐름).

Cấp cao (senior / 시니어) quyết định (decision / 결정) không phải “luôn scan BLE trực tiếp”, mà là hỏi system-mediated API có phù hợp không.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **12. Bluetooth máy trạng thái (state machine / 상태 머신)** nối từ **11. Companion thiết bị (device / 장치) Manager khi app ghép thiết bị companion** sang **13. ACCESSLOCALNETWORK**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Bluetooth máy trạng thái (state machine / 상태 머신)

BLE mã (code / 코드) môi trường vận hành (production / 운영 환경) nên mô hình (model / 모델) liên kết (connection / 연결) vòng đời (lifecycle / 생명주기):

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

Đừng dùng một boolean `isConnected`. liên kết (connection / 연결) có hết thời gian chờ (timeout / 타임아웃), reconnect, permission revoke, Bluetooth disabled và remote disconnect.

# Android 17 cục bộ (local / 로컬) mạng (network / 네트워크)

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **13. ACCESSLOCALNETWORK** nối từ **12. Bluetooth máy trạng thái (state machine / 상태 머신)** sang **14. Notification permission**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. `ACCESS_LOCAL_NETWORK`

Android 17 bổ sung thời gian chạy (runtime / 런타임) permission cho app mục tiêu (target / 대상) API 37+ khi cần discover/communicate với thiết bị trong LAN trong những luồng (flow / 흐름) áp dụng. Đây là ví dụ điển hình của nền tảng (platform / 플랫폼) evolution: năng lực (capability / 역량) trước đây “tự do” có thể trở thành protected surface vì privacy/fingerprinting rủi ro (risk / 위험).

Nếu app điều khiển smart-home/casting/cục bộ (local / 로컬) máy chủ (server / 서버), phải kiểm tra di chuyển (migration / 마이그레이션) khi nâng mục tiêu (target / 대상) SDK. Một option khác trong một số use trường hợp (case / 사례) là system-mediated picker giúp người dùng (user / 사용자) chọn cục bộ (local / 로컬) thiết bị (device / 장치) mà không cần broad mạng (network / 네트워크) discovery permission.

Mục tiêu (target / 대상) SDK di chuyển (migration / 마이그레이션) vì vậy phải có **năng lực (capability / 역량) kiểm tra (audit / 감사)**, không chỉ tăng con số trong Gradle.

# Notifications

> **Nối mạch:** Trong **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **14. Notification permission** nối từ **13. ACCESSLOCALNETWORK** sang **15. Notification channel là user-controlled đặc tả hợp đồng (contract / 계약)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Notification permission

Trên Android hiện đại, app không được giả định notification luôn hiển thị. người dùng (user / 사용자) có thể deny permission hoặc disable channel.

Nghiệp vụ (business / 비즈니스) luồng (flow / 흐름) quan trọng không được phụ thuộc notification như kênh duy nhất để đảm bảo dữ liệu (data / 데이터) tính đúng đắn (correctness / 정확성). Notification là delivery surface, không phải durable job hàng đợi (queue / 큐).

Ví dụ sync background vẫn phải persist trạng thái (state / 상태); notification chỉ báo kết quả (outcome / 결과).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **15. Notification channel là user-controlled đặc tả hợp đồng (contract / 계약)** nối từ **14. Notification permission** sang **16. PendingIntent mutability**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Notification channel là user-controlled đặc tả hợp đồng (contract / 계약)

Sau khi channel được tạo, người dùng (user / 사용자) có quyền chỉnh importance/sound. App không nên liên tục tạo channel mới để né setting của người dùng (user / 사용자).

Thiết kế channel theo ngữ nghĩa (semantic / 의미적) ổn định như:

```text
messages
orders
security_alerts
background_progress
```

thay vì theo từng campaign/phiên bản (version / 버전).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **16. PendingIntent mutability** nối từ **15. Notification channel là user-controlled đặc tả hợp đồng (contract / 계약)** sang **17. Permission indicator và người dùng (user / 사용자) expectation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. PendingIntent mutability

Khi tạo `PendingIntent`, cần chọn immutable/mutable đúng đặc tả hợp đồng (contract / 계약). Mặc định nên immutable nếu receiver không cần hệ thống (system / 시스템)/other tiến trình (process / 프로세스) fill thêm extras theo use trường hợp (case / 사례) hợp lệ.

Bảo mật (security / 보안) principle: năng lực (capability / 역량) đơn vị từ (token / 토큰) càng hẹp càng tốt.

# Camera và Microphone

> **Nối mạch:** Trong **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **17. Permission indicator và người dùng (user / 사용자) expectation** nối từ **16. PendingIntent mutability** sang **18. Camera permission không có nghĩa camera đang usable**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Permission indicator và người dùng (user / 사용자) expectation

Camera/microphone là high-trust năng lực (capability / 역량). Hệ thống có privacy indicators và người dùng (user / 사용자) controls. App nên bắt đầu capture rõ ràng sau người dùng (user / 사용자) intent, dừng capture đúng vòng đời (lifecycle / 생명주기) và không giữ tài nguyên (resource / 자원) ở background không cần thiết.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **18. Camera permission không có nghĩa camera đang usable** nối từ **17. Permission indicator và người dùng (user / 사용자) expectation** sang **19. Không xin lưu trữ (storage / 저장소) permission nếu hệ thống (system / 시스템) picker đủ dùng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Camera permission không có nghĩa camera đang usable

Camera có thể đang được app khác sử dụng, vòng đời (lifecycle / 생명주기) chưa ready hoặc hardware lỗi (error / 오류). Camera tầng (layer / 계층) phải mô hình (model / 모델) open/close/lỗi (error / 오류) thay vì chỉ check permission.

CameraX thường giảm độ phức tạp (complexity / 복잡도) so với Camera2 cho app phổ biến, nhưng vẫn phải bind use trường hợp (case / 사례) vào vòng đời (lifecycle / 생명주기) đúng cách.

# Lưu trữ (storage / 저장소), media và truy cập tệp (file access / 파일 접근)

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **19. Không xin lưu trữ (storage / 저장소) permission nếu hệ thống (system / 시스템) picker đủ dùng** nối từ **18. Camera permission không có nghĩa camera đang usable** sang **20. URI permission**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Không xin lưu trữ (storage / 저장소) permission nếu hệ thống (system / 시스템) picker đủ dùng

Nếu người dùng (user / 사용자) chọn ảnh/video, Photo Picker thường là surface tốt hơn broad media permission. Nếu người dùng (user / 사용자) chọn document/tệp (file / 파일), lưu trữ (storage / 저장소) truy cập (access / 접근) khung phần mềm (framework / 프레임워크) cho phép người dùng (user / 사용자) grant URI truy cập (access / 접근) cụ thể.

Principle:

```text
request narrow user-selected access
trước khi
request broad library access
```

Điều này giảm privacy surface và permission rejection.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **20. URI permission** nối từ **19. Không xin lưu trữ (storage / 저장소) permission nếu hệ thống (system / 시스템) picker đủ dùng** sang **21. FileProvider cho share tệp (file / 파일)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. URI permission

Khi nhận `content://` URI, app không nên assume có filesystem đường dẫn (path / 경로) thật. Dùng `ContentResolver` để mở stream/tệp (file / 파일) descriptor.

```kotlin
context.contentResolver.openInputStream(uri)?.use { input ->
    // consume stream
}
```

Nếu cần truy cập (access / 접근) lâu dài cho document từ SAF, có thể cần persist URI permission theo đặc tả hợp đồng (contract / 계약) của picker.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **21. FileProvider cho share tệp (file / 파일)** nối từ **20. URI permission** sang **22. Permission không thể tách khỏi thực thi (execution / 실행) chính sách (policy / 정책)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. `FileProvider` cho share tệp (file / 파일)

Không expose raw `file://` đường dẫn (path / 경로). Dùng `FileProvider`/content URI với temporary grant.

Intent sharing phải grant permission đúng phạm vi (scope / 범위) và không expose tệp (file / 파일) private ngoài ý muốn.

# Foreground dịch vụ (service / 서비스) và background thực thi (execution / 실행)

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **22. Permission không thể tách khỏi thực thi (execution / 실행) chính sách (policy / 정책)** nối từ **21. FileProvider cho share tệp (file / 파일)** sang **23. chính xác (exact / 정확한) alarm là special năng lực (capability / 역량)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Permission không thể tách khỏi thực thi (execution / 실행) chính sách (policy / 정책)

Một app có location permission chưa chắc được phép chạy tracking vô hạn ở background. Android áp foreground-service kiểu (type / 타입), background start restriction và battery chính sách (policy / 정책).

Khi tính năng (feature / 기능) cần user-visible long-running công việc (work / 작업), foreground dịch vụ (service / 서비스) có thể đúng. Khi công việc (work / 작업) durable nhưng không cần exact-time/user-visible, WorkManager thường phù hợp hơn.

Đừng dùng foreground dịch vụ (service / 서비스) như cách “giữ app sống”.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **23. chính xác (exact / 정확한) alarm là special năng lực (capability / 역량)** nối từ **22. Permission không thể tách khỏi thực thi (execution / 실행) chính sách (policy / 정책)** sang **24. android:exported**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. chính xác (exact / 정확한) alarm là special năng lực (capability / 역량)

Chính xác (exact / 정확한) alarm ảnh hưởng battery và bị nền tảng (platform / 플랫폼)/chính sách (policy / 정책) quản lý. Chỉ use trường hợp (case / 사례) thật sự exact-time như alarm clock/calendar-critical sự kiện (event / 이벤트) mới nên dựa vào nó.

Periodic sync nên dùng WorkManager/flexible scheduling hơn.

# Intents, exported thành phần (component / 컴포넌트) và bên ngoài (external / 외부) đầu vào (input / 입력)

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **24. android:exported** nối từ **23. chính xác (exact / 정확한) alarm là special năng lực (capability / 역량)** sang **25. Intent đầu vào (input / 입력) phải validate**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. `android:exported`

Thành phần (component / 컴포넌트) nhận implicit intent hoặc cần bên ngoài (external / 외부) truy cập (access / 접근) phải có exported cấu hình (configuration / 구성) rõ. thành phần (component / 컴포넌트) nội bộ nên không exported nếu không cần.

Đừng coi Activity/dịch vụ (service / 서비스)/Receiver exported chỉ là điều hướng (navigation / 내비게이션) detail; đó là attack surface.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **25. Intent đầu vào (input / 입력) phải validate** nối từ **24. android:exported** sang **26. App Links tốt hơn custom scheme cho web quyền sở hữu (ownership / 소유권)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Intent đầu vào (input / 입력) phải validate

Deep link như:

```text
myapp://payment/confirm?amount=...
```

không được tin amount/role/userId chỉ vì link mở từ app của bạn. bên ngoài (external / 외부) nguồn (source / 소스) có thể craft Intent.

Server-side authorization và lĩnh vực (domain / 도메인) kiểm tra hợp lệ (validation / 검증) vẫn là nguồn quyết định.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, sau nội dung của **25. Intent đầu vào (input / 입력) phải validate**, **26. App Links tốt hơn custom scheme cho web quyền sở hữu (ownership / 소유권)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **27. Một số năng lực (capability / 역량) không phải thời gian chạy (runtime / 런타임) permission bình thường** mở rộng hệ quả hoặc giới hạn liên quan.

## 26. App Links tốt hơn custom scheme cho web quyền sở hữu (ownership / 소유권)

Verified App Links liên kết HTTP(S) lĩnh vực (domain / 도메인) với app quyền sở hữu (ownership / 소유권), giảm hijacking so với custom URI scheme trong nhiều use trường hợp (case / 사례).

Điều hướng (navigation / 내비게이션) tầng (layer / 계층) nên parse thành typed tuyến (route / 경로)/lĩnh vực (domain / 도메인) đầu vào (input / 입력) rồi validate thay vì truyền URI string đi khắp app.

# Special App truy cập (access / 접근)

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **27. Một số năng lực (capability / 역량) không phải thời gian chạy (runtime / 런타임) permission bình thường** nối từ **26. App Links tốt hơn custom scheme cho web quyền sở hữu (ownership / 소유권)** sang **28. Tạo lớp trừu tượng (abstraction / 추상화) theo năng lực (capability / 역량), không theo permission API**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Một số năng lực (capability / 역량) không phải thời gian chạy (runtime / 런타임) permission bình thường

Draw over other apps, manage all files, install unknown apps, chính xác (exact / 정확한) alarms hoặc khả năng tiếp cận (accessibility / 접근성) dịch vụ (service / 서비스) có hệ thống (system / 시스템) setting/special truy cập (access / 접근) luồng (flow / 흐름) riêng. Không được yêu cầu (request / 요청)/khuyến khích chỉ vì muốn shortcut kỹ thuật.

Nếu app cần special truy cập (access / 접근), UX phải giải thích benefit cụ thể và tính năng (feature / 기능) vẫn degrade hợp lý khi người dùng (user / 사용자) không cấp.

# Năng lực (capability / 역량) kiến trúc (architecture / 아키텍처)

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **28. Tạo lớp trừu tượng (abstraction / 추상화) theo năng lực (capability / 역량), không theo permission API** nối từ **27. Một số năng lực (capability / 역량) không phải thời gian chạy (runtime / 런타임) permission bình thường** sang **29. Permission trạng thái (state / 상태) không phải lĩnh vực (domain / 도메인) entitlement**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Tạo lớp trừu tượng (abstraction / 추상화) theo năng lực (capability / 역량), không theo permission API

UI không nên biết chi tiết API mức (level / 수준) branching:

```kotlin
interface CameraCapability {
    suspend fun ensureReady(): CapabilityResult
}
```

Hiện thực (implementation / 구현) có thể check hardware, permission, chính sách (policy / 정책) và vòng đời (lifecycle / 생명주기). UI chỉ kết xuất (render / 렌더링) trạng thái (state / 상태):

```kotlin
sealed interface CapabilityResult {
    data object Ready : CapabilityResult
    data object Unsupported : CapabilityResult
    data object PermissionRequired : CapabilityResult
    data object DisabledBySystem : CapabilityResult
}
```

Cách này làm kiểm thử (test / 테스트) dễ hơn và tránh permission lô-gic (logic / 논리) rải khắp Composable.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **29. Permission trạng thái (state / 상태) không phải lĩnh vực (domain / 도메인) entitlement** nối từ **28. Tạo lớp trừu tượng (abstraction / 추상화) theo năng lực (capability / 역량), không theo permission API** sang **30. minSdk, targetSdk, thời gian chạy (runtime / 런타임) OS**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Permission trạng thái (state / 상태) không phải lĩnh vực (domain / 도메인) entitlement

Người dùng (user / 사용자) có camera permission không có nghĩa account được phép dùng tính năng (feature / 기능) premium. Ngược lại, subscription entitlement không có nghĩa OS permission đã grant.

Tách:

```text
OS capability/permission
business entitlement
backend authorization
```

ba tầng (layer / 계층) khác nhau.

# Phiên bản (version / 버전) ma trận (matrix / 행렬)

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **30. minSdk, targetSdk, thời gian chạy (runtime / 런타임) OS** nối từ **29. Permission trạng thái (state / 상태) không phải lĩnh vực (domain / 도메인) entitlement** sang **31. mục tiêu (target / 대상) SDK di chuyển (migration / 마이그레이션) checklist**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. `minSdk`, `targetSdk`, thời gian chạy (runtime / 런타임) OS

Một app có thể:

```text
minSdk = 26
targetSdk = 37
chạy trên device API 29, 34, 37...
```

Hành vi (behavior / 동작) phụ thuộc cả thời gian chạy (runtime / 런타임) OS và mục tiêu (target / 대상) SDK. Vì vậy mã (code / 코드) tính tương thích (compatibility / 호환성) thường cần xét:

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.X) {
    // API mới
}
```

nhưng target-specific hành vi (behavior / 동작) không phải lúc nào cũng chỉ giải bằng `SDK_INT`; phải đọc hành vi (behavior / 동작) changes khi nâng mục tiêu (target / 대상).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **31. mục tiêu (target / 대상) SDK di chuyển (migration / 마이그레이션) checklist** nối từ **30. minSdk, targetSdk, thời gian chạy (runtime / 런타임) OS** sang **32. kiểm thử (test / 테스트) ma trận (matrix / 행렬)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. mục tiêu (target / 대상) SDK di chuyển (migration / 마이그레이션) checklist

Mỗi lần tăng mục tiêu (target / 대상) SDK, rà soát (review / 검토) ít nhất: permissions mới/đổi ngữ nghĩa (semantics / 의미론), background thực thi (execution / 실행), foreground-service types, notification, lưu trữ (storage / 저장소)/media, intents/exported components, bảo mật (security / 보안)/mạng (network / 네트워크), edge-to-edge/hệ thống (system / 시스템) UI, khả năng tiếp cận (accessibility / 접근성)/IME, WebView hành vi (behavior / 동작) và hardware năng lực (capability / 역량).

Android 17 là ví dụ rõ với cục bộ (local / 로컬) mạng (network / 네트워크) permission, MessageQueue hiện thực (implementation / 구현) thay đổi (change / 변경), background audio tightening và các hành vi (behavior / 동작) khác.

# Testing permission/năng lực (capability / 역량)

> **Nối mạch:** Trong **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **32. kiểm thử (test / 테스트) ma trận (matrix / 행렬)** nối từ **31. mục tiêu (target / 대상) SDK di chuyển (migration / 마이그레이션) checklist** sang **33. Đừng chỉ kiểm thử (test / 테스트) emulator “happy đường dẫn (path / 경로)”**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. kiểm thử (test / 테스트) ma trận (matrix / 행렬)

Permission tính năng (feature / 기능) nên kiểm thử (test / 테스트) ít nhất:

| Scenario | Kỳ vọng |
|---|---|
| hardware absent | fallback rõ |
| permission granted | tính năng (feature / 기능) chạy |
| denied lần đầu | explain/thử lại (retry / 재시도) hợp lý |
| denied lâu dài | Settings/fallback |
| revoke khi app background | app recover |
| OS phiên bản (version / 버전) cũ | tính tương thích (compatibility / 호환성) đường dẫn (path / 경로) |
| target-SDK hành vi (behavior / 동작) mới | di chuyển (migration / 마이그레이션) đường dẫn (path / 경로) |

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **32. kiểm thử (test / 테스트) ma trận (matrix / 행렬)** đặt đầu vào cho **33. Đừng chỉ kiểm thử (test / 테스트) emulator “happy đường dẫn (path / 경로)”**, rồi **34. Permission tối thiểu là bảo mật (security / 보안) và sản phẩm (product / 제품) chất lượng (quality / 품질)** mở rộng hệ quả hoặc giới hạn liên quan.

## 33. Đừng chỉ kiểm thử (test / 테스트) emulator “happy đường dẫn (path / 경로)”

Bluetooth, camera, audio, sensor, foldable posture hoặc OEM permission hành vi (behavior / 동작) cần physical-device ma trận (matrix / 행렬) khi rủi ro (risk / 위험) cao. Emulator hữu ích nhưng không thay hết hardware tích hợp (integration / 통합).

# Cấp cao (senior / 시니어) Notes

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **33. Đừng chỉ kiểm thử (test / 테스트) emulator “happy đường dẫn (path / 경로)”** đặt đầu vào cho **34. Permission tối thiểu là bảo mật (security / 보안) và sản phẩm (product / 제품) chất lượng (quality / 품질)**, rồi **35. hệ thống (system / 시스템) picker thường thắng custom broad truy cập (access / 접근)** mở rộng hệ quả hoặc giới hạn liên quan.

## 34. Permission tối thiểu là bảo mật (security / 보안) và sản phẩm (product / 제품) chất lượng (quality / 품질)

Ít permission hơn không chỉ giảm rủi ro (risk / 위험); nó giảm dialog, denial trạng thái (state / 상태), hỗ trợ (support / 지원) burden, Play chính sách (policy / 정책) surface và mã (code / 코드) branch.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **35. hệ thống (system / 시스템) picker thường thắng custom broad truy cập (access / 접근)** nối từ **34. Permission tối thiểu là bảo mật (security / 보안) và sản phẩm (product / 제품) chất lượng (quality / 품질)** sang **36. năng lực (capability / 역량) phải có fallback**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. hệ thống (system / 시스템) picker thường thắng custom broad truy cập (access / 접근)

Photo Picker, document picker, Credential Manager, Companion thiết bị (device / 장치) Manager và các system-mediated luồng (flow / 흐름) tồn tại để người dùng (user / 사용자) grant truy cập (access / 접근) cụ thể với trust UX nhất quán. Dùng chúng khi phù hợp thay vì tự xây broad-scanning kiến trúc (architecture / 아키텍처).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **36. năng lực (capability / 역량) phải có fallback** nối từ **35. hệ thống (system / 시스템) picker thường thắng custom broad truy cập (access / 접근)** sang **37. Permission denial là normal người dùng (user / 사용자) choice**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. năng lực (capability / 역량) phải có fallback

Nếu app crash hoặc khóa toàn bộ luồng (flow / 흐름) chỉ vì camera/Bluetooth/location unavailable, kiến trúc (architecture / 아키텍처) đang coupling tính năng (feature / 기능) quá chặt với hardware.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 10 — Permissions, thiết bị (device / 장치) năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)**, **37. Permission denial là normal người dùng (user / 사용자) choice** nối từ **36. năng lực (capability / 역량) phải có fallback** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## 37. Permission denial là normal người dùng (user / 사용자) choice

Đừng dùng dark mẫu (pattern / 패턴) ép người dùng (user / 사용자) grant. sản phẩm (product / 제품) tốt giải thích giá trị (value / 값) và vẫn cho người dùng (user / 사용자) đường khác nếu possible.

# Checklist kết thúc chapter

Bạn nên có thể giải thích sự khác nhau giữa permission và hardware năng lực (capability / 역량); vì sao `<uses-feature>` có thể ảnh hưởng Play availability; khi nào dùng hệ thống (system / 시스템) picker thay broad permission; vì sao permission có thể bị revoke; Bluetooth permission hiện đại khác legacy thế nào; Android 17 local-network permission ảnh hưởng app LAN ra sao; vì sao URI không phải filesystem đường dẫn (path / 경로); foreground dịch vụ (service / 서비스) khác WorkManager; `android:exported` và PendingIntent liên quan bảo mật (security / 보안) thế nào; và tại sao target-SDK upgrade phải được xem như nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션) dự án (project / 프로젝트) chứ không phải sửa một số trong Gradle.

> **Bàn giao:** Sau **37. Permission denial là normal người dùng (user / 사용자) choice**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
