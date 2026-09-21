# Case 12 — Camera, Media, Location, Bluetooth, Files và Device Integration

Một app Android production thường không chỉ hiển thị API data. Nó phải chụp ảnh, phát media, ghi âm, đọc file, chia sẻ document, lấy vị trí, kết nối thiết bị BLE, nhận notification hoặc mở WebView. Đây là vùng dễ tạo bug vì mỗi capability có lifecycle, permission, resource ownership và failure mode riêng.

Chapter này không biến thành manual cho từng SDK. Mục tiêu là xây pattern dùng chung để bạn có thể đọc API mới và đặt nó vào đúng mental model.

# 1. Pattern chung cho mọi device capability

Bất kể camera, microphone, Bluetooth hay location, hãy tách năm lớp:

```text
Capability availability
→ Permission / policy
→ Resource acquisition
→ Active session / stream
→ Release / recovery
```

Nếu code bỏ qua một lớp, bug thường xuất hiện ở lifecycle transition hoặc error recovery.

Ví dụ camera không chỉ là `CAMERA` permission. Device có thể không có camera, permission có thể denied, camera có thể đang busy, Activity có thể stop, hoặc capture session có thể fail.

# Camera

## 2. CameraX trước khi Camera2

Đối với đa số app cần preview, image capture, video capture hoặc image analysis, CameraX là abstraction ưu tiên vì nó chuẩn hóa nhiều khác biệt device và tích hợp lifecycle tốt hơn.

Camera2 phù hợp khi cần control low-level mà CameraX không đáp ứng. Senior decision là chọn abstraction thấp nhất **chỉ khi requirement buộc phải dùng**.

## 3. Camera use case

CameraX tổ chức theo use case như preview, image capture và analysis. Những use case này bind vào lifecycle owner.

Conceptual flow:

```text
check capability
→ permission
→ get camera provider
→ bind Preview/ImageCapture/ImageAnalysis
→ lifecycle start/stop
→ unbind/release
```

## 4. Image analysis và backpressure

Frame analysis có thể nhanh hơn processor của app. Nếu xử lý ML/QR quá chậm, queue frame vô hạn sẽ tăng latency/memory.

Thay vì cố xử lý mọi frame, nhiều use case nên giữ frame mới nhất và drop frame cũ. Đây là cùng tư duy backpressure đã học ở Flow.

## 5. Camera rotation và coordinate transform

Image analysis coordinate không tự động giống preview coordinate. Nếu vẽ bounding box lên preview, cần hiểu rotation, crop, scale và mirror camera trước.

Bug “box lệch khỏi object” thường là coordinate-space bug chứ không phải ML model sai.

# Media playback

## 6. Media3 / ExoPlayer

Media playback hiện đại thường xây trên Jetpack Media3/ExoPlayer. Player có lifecycle riêng, buffering state, track state, audio focus, network retry và decoder resource.

Không tạo player mới mỗi recomposition.

```text
UI composition lifetime
≠ player session lifetime
```

Player thường được owner ở screen/service level phù hợp rồi UI observe state.

## 7. Media session

Nếu playback cần background/control từ notification, Bluetooth headset, Auto hoặc lock screen, MediaSession trở thành system contract quan trọng.

Media notification không nên tự chế thành một collection button rời khỏi playback state; MediaSession giúp system hiểu playback semantics.

## 8. Audio focus

App phát âm thanh không tồn tại một mình. Music player, navigation, call và voice assistant có thể cạnh tranh audio focus.

Playback layer phải xử lý focus gain/loss/duck theo use case thay vì luôn set volume 100%.

Android 17 siết background audio interaction hơn; khi nâng target/platform, review media behavior changes thay vì dựa vào logic cũ.

# Recording và microphone

## 9. Microphone là high-trust resource

Chỉ bắt đầu record sau user intent rõ. Dừng capture khi flow kết thúc hoặc lifecycle không còn hợp lệ.

Nếu app cần long-running recording, foreground execution và notification phải tuân policy/system contract phù hợp.

## 10. Audio format

Sample rate, channel count, codec và container là những layer khác nhau. Đừng gọi mọi file audio là “MP3”. Nếu feature upload voice note, backend contract phải ghi rõ format/codec/content type.

# Files và documents

## 11. App-private file

Dữ liệu chỉ app dùng nên ưu tiên internal/app-specific storage. Không cần expose ra shared storage.

Ví dụ cache download tạm nên ở cache directory thay vì xin broad storage access.

## 12. Storage Access Framework

Khi user muốn chọn một document bất kỳ, SAF cung cấp system picker và trả `content://` URI.

```kotlin
val launcher = rememberLauncherForActivityResult(
    ActivityResultContracts.OpenDocument()
) { uri ->
    // read via ContentResolver
}
```

App không nên chuyển URI thành filesystem path bằng hack `_data` column. Scoped storage và provider abstraction tồn tại để resource có thể không phải file local truyền thống.

## 13. Photo Picker

Nếu user chọn ảnh/video, Photo Picker thường giảm permission surface so với broad media access.

Nếu chỉ cần user chọn một ảnh avatar, xin quyền đọc toàn bộ gallery là over-permission.

## 14. MediaStore

Khi app tạo media cần xuất hiện trong shared media library, MediaStore là API phù hợp. Metadata, pending write và collection URI giúp app publish media theo system contract.

## 15. MIME type

File extension không đủ để quyết định content. Khi share/open document, dùng MIME type đúng và validate input ở boundary.

# Sharing

## 16. Sharesheet

Dùng system Sharesheet cho `ACTION_SEND`/`ACTION_SEND_MULTIPLE` thay vì xây danh sách app share riêng.

System có ranking, target filtering và privacy behavior tốt hơn custom chooser.

## 17. URI grant

Khi share content URI, grant read permission đúng scope. Không làm file world-readable.

# Location

## 18. Current location và continuous tracking khác nhau

Một màn hình weather cần location một lần khác hoàn toàn workout tracking liên tục.

Use case một lần nên dùng API current location phù hợp thay vì giữ listener lâu sống.

Continuous tracking cần lifecycle, battery, foreground/background policy và rate strategy.

## 19. Accuracy và battery

High-accuracy location tốn pin hơn. Nếu feature chỉ cần nearby city, đừng yêu cầu update 1 giây với GPS chính xác cao.

Model request theo business SLA:

```text
accuracy
freshness
latency
battery cost
background need
```

## 20. Location timeout

Location request có thể không trả kết quả nhanh. Domain layer nên có timeout/fallback: last-known location, manual selection hoặc user retry.

## 21. Geofencing

Geofence phù hợp event “enter/exit area” hơn polling location liên tục. Nhưng delivery không phải hard real-time guarantee. Business không nên dùng geofence như transaction clock chính xác từng giây.

# Bluetooth Low Energy

## 22. BLE khác classic Bluetooth

BLE thường dùng GATT service/characteristic model. Scan tìm device; connect tạo GATT connection; service discovery xác định capability; characteristic read/write/notify truyền data.

Mental model:

```text
scan
→ identify device
→ connect
→ discover services
→ subscribe/read/write
→ handle disconnect
→ reconnect policy
```

## 23. GATT operation serialization

Nhiều BLE stack/device không thích nhiều GATT operation bắn đồng thời. Production client thường cần queue/serialize read-write operation theo contract device.

## 24. Reconnect

Reconnect không nên infinite tight loop. Dùng backoff, app foreground/background awareness và user expectation.

Nếu thiết bị bị unpaired hoặc Bluetooth off, state machine phải chuyển thành actionable error thay vì spinner mãi mãi.

## 25. Protocol framing

BLE characteristic thường có payload nhỏ. Nếu domain message lớn, bạn cần framing/chunking/checksum/versioning riêng. Đây là network protocol design thu nhỏ.

# NFC

## 26. NFC capability

NFC không có trên mọi device. Nếu app đọc tag, hãy model unsupported/disabled/tag-lost như normal state.

Tag interaction thường ngắn; đừng giữ reference/tag handle lâu quá lifecycle của discovery event.

# Sensors

## 27. Sensor rate

Accelerometer/gyroscope có thể phát event tần suất cao. Sensor callback không nên làm heavy work trực tiếp.

Sampling rate phải phù hợp use case. UI orientation indicator khác motion-analysis pipeline.

## 28. Sensor fusion

Raw sensor noisy. Nhiều feature cần filtering/fusion thay vì dùng một sample trực tiếp.

Đây là nơi math/signal processing trở nên quan trọng hơn API syntax.

# Connectivity

## 29. Network available không đồng nghĩa Internet usable

`ConnectivityManager` có thể cho biết network capability, nhưng captive portal, DNS failure hoặc backend outage vẫn có thể làm request fail.

Đừng gate toàn bộ request bằng boolean `isNetworkConnected`. Request thật vẫn là source of truth về success/failure.

## 30. Offline UI

UI nên phân biệt:

```text
no cached data + offline
cached data + offline
sync pending
server error
```

Một banner “No internet” không đủ cho app offline-first.

# WebView

## 31. WebView là browser engine trong security boundary app

WebView có cookie/session, JS, file access, navigation, permission và bridge concern. Không coi nó như `TextView` hiển thị HTML.

## 32. JavaScript bridge

`addJavascriptInterface` tạo bridge giữa web content và native code. Chỉ expose API tối thiểu, chỉ load trusted origin và validate input.

Không expose object quyền lực cho arbitrary web content.

## 33. Web permission

Camera/mic/location request bên trong WebView vẫn cần Android permission + web-origin permission handling. Không tự động `request.grant(request.resources)` cho mọi origin.

# Resource ownership trong Compose

## 34. `DisposableEffect`

Listener/resource cần acquire/release cùng composition có thể dùng:

```kotlin
DisposableEffect(sensorManager, listener) {
    sensorManager.registerListener(...)

    onDispose {
        sensorManager.unregisterListener(listener)
    }
}
```

Nhưng long-lived media/camera session thường nên owner ở layer có lifecycle rõ hơn thay vì gắn trực tiếp vào một leaf composable.

# Error model

## 35. Device integration error không nên là string

```kotlin
sealed interface DeviceError {
    data object Unsupported : DeviceError
    data object PermissionDenied : DeviceError
    data object Disabled : DeviceError
    data object Busy : DeviceError
    data object Disconnected : DeviceError
    data object Timeout : DeviceError
    data class Protocol(val code: Int) : DeviceError
}
```

Typed error cho phép UI đưa action đúng: “Open settings”, “Turn on Bluetooth”, “Retry”, “Reconnect”, không chỉ toast `Something went wrong`.

# Testing

## 36. Fake boundary

Hardware API nên được wrap sau interface để business logic test bằng fake state machine.

Ví dụ BLE repository test:

```text
Disconnected
→ Connecting
→ Ready
→ write succeeds
```

và case:

```text
Ready
→ permission revoked
→ PermissionDenied
```

## 37. Instrumentation/hardware test

Fake không thay toàn bộ device behavior. Protocol critical nên có integration test với hardware lab/device matrix nếu business phụ thuộc mạnh.

# Senior Notes

## 38. Device feature là distributed system nhỏ

Camera service, media decoder, Bluetooth peripheral, location provider hoặc WebView đều là component ngoài core business process. Chúng có latency, failure, lifecycle và version riêng. Hãy thiết kế timeout/recovery/state machine giống khi làm network.

## 39. Đừng giữ resource vì sợ reopen cost

Camera/mic/sensor/BLE resource giữ quá lâu gây battery/privacy/conflict. Ownership đúng quan trọng hơn micro-optimization reopen.

## 40. Protocol phải version được

Nếu app nói chuyện với BLE/IoT/backend/media format do công ty kiểm soát, thêm protocol version/compatibility strategy sớm. Mobile app không update đồng thời 100% với firmware/server.

# Checklist kết thúc chapter

Bạn nên giải thích được khi nào dùng CameraX thay Camera2; vì sao image analysis cần backpressure; MediaSession/audio focus liên quan playback thế nào; Photo Picker/SAF/MediaStore khác nhau ra sao; content URI khác path file; current location khác continuous tracking; BLE GATT state machine gồm những bước nào; WebView permission/JS bridge có security risk gì; và vì sao device integration nên được model như stateful external system chứ không phải một lời gọi API đơn lẻ.
