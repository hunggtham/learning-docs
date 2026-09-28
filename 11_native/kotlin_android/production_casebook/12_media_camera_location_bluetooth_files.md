# Trường hợp (case / 사례) 12 — Camera, Media, Location, Bluetooth, Files và thiết bị (device / 장치) tích hợp (integration / 통합)

> **Mạch đọc:** Đặt **trường hợp (case / 사례) 12 — Camera, Media, Location, Bluetooth, Files và thiết bị (device / 장치) tích hợp (integration / 통합)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **2. CameraX trước khi Camera2** sang **3. Camera use trường hợp (case / 사례)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một app Android môi trường vận hành (production / 운영 환경) thường không chỉ hiển thị API dữ liệu (data / 데이터). Nó phải chụp ảnh, phát media, ghi âm, đọc tệp (file / 파일), chia sẻ document, lấy vị trí, kết nối thiết bị BLE, nhận notification hoặc mở WebView. Đây là vùng dễ tạo bug vì mỗi năng lực (capability / 역량) có vòng đời (lifecycle / 생명주기), permission, tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권) và dạng thất bại (failure mode / 실패 모드) riêng.

Chapter này không biến thành manual cho từng SDK. Mục tiêu là xây mẫu (pattern / 패턴) dùng chung để bạn có thể đọc API mới và đặt nó vào đúng mô hình tư duy (mental model / 사고 모델).

# 1. mẫu (pattern / 패턴) chung cho mọi thiết bị (device / 장치) năng lực (capability / 역량)

Bất kể camera, microphone, Bluetooth hay location, hãy tách năm lớp:

```text
Capability availability
→ Permission / policy
→ Resource acquisition
→ Active session / stream
→ Release / recovery
```

Nếu mã (code / 코드) bỏ qua một lớp, bug thường xuất hiện ở vòng đời (lifecycle / 생명주기) chuyển tiếp (transition / 전이) hoặc lỗi (error / 오류) khôi phục (recovery / 복구).

Ví dụ camera không chỉ là `CAMERA` permission. thiết bị (device / 장치) có thể không có camera, permission có thể denied, camera có thể đang busy, Activity có thể stop, hoặc capture session có thể thất bại (fail / 실패).

# Camera

## 2. CameraX trước khi Camera2

Đối với đa số app cần preview, ảnh (image / 이미지) capture, video capture hoặc ảnh (image / 이미지) phân tích (analysis / 분석), CameraX là lớp trừu tượng (abstraction / 추상화) ưu tiên vì nó chuẩn hóa nhiều khác biệt thiết bị (device / 장치) và tích hợp vòng đời (lifecycle / 생명주기) tốt hơn.

Camera2 phù hợp khi cần điều khiển (control / 제어) low-level mà CameraX không đáp ứng. cấp cao (senior / 시니어) quyết định (decision / 결정) là chọn lớp trừu tượng (abstraction / 추상화) thấp nhất **chỉ khi yêu cầu (requirement / 요구사항) buộc phải dùng**.

## 3. Camera use trường hợp (case / 사례)

CameraX tổ chức theo use trường hợp (case / 사례) như preview, ảnh (image / 이미지) capture và phân tích (analysis / 분석). Những use trường hợp (case / 사례) này bind vào vòng đời (lifecycle / 생명주기) đơn vị sở hữu (owner / 오너).

Conceptual luồng (flow / 흐름):

```text
check capability
→ permission
→ get camera provider
→ bind Preview/ImageCapture/ImageAnalysis
→ lifecycle start/stop
→ unbind/release
```

## 4. ảnh (image / 이미지) phân tích (analysis / 분석) và backpressure

Frame phân tích (analysis / 분석) có thể nhanh hơn processor của app. Nếu xử lý ML/QR quá chậm, hàng đợi (queue / 큐) frame vô hạn sẽ tăng độ trễ (latency / 지연 시간)/bộ nhớ (memory / 메모리).

Thay vì cố xử lý mọi frame, nhiều use trường hợp (case / 사례) nên giữ frame mới nhất và drop frame cũ. Đây là cùng tư duy backpressure đã học ở luồng (flow / 흐름).

## 5. Camera rotation và coordinate transform

Ảnh (image / 이미지) phân tích (analysis / 분석) coordinate không tự động giống preview coordinate. Nếu vẽ bounding box lên preview, cần hiểu rotation, crop, quy mô (scale / 규모) và mirror camera trước.

Bug “box lệch khỏi đối tượng (object / 객체)” thường là coordinate-space bug chứ không phải ML mô hình (model / 모델) sai.

# Media playback

## 6. Media3 / ExoPlayer

Media playback hiện đại thường xây trên Jetpack Media3/ExoPlayer. Player có vòng đời (lifecycle / 생명주기) riêng, buffering trạng thái (state / 상태), nhánh học (track / 트랙) trạng thái (state / 상태), audio focus, mạng (network / 네트워크) thử lại (retry / 재시도) và decoder tài nguyên (resource / 자원).

Không tạo player mới mỗi recomposition.

```text
UI composition lifetime
≠ player session lifetime
```

Player thường được đơn vị sở hữu (owner / 오너) ở screen/dịch vụ (service / 서비스) mức (level / 수준) phù hợp rồi UI observe trạng thái (state / 상태).

## 7. Media session

Nếu playback cần background/điều khiển (control / 제어) từ notification, Bluetooth headset, Auto hoặc khóa (lock / 잠금) screen, MediaSession trở thành hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약) quan trọng.

Media notification không nên tự chế thành một collection button rời khỏi playback trạng thái (state / 상태); MediaSession giúp hệ thống (system / 시스템) hiểu playback ngữ nghĩa (semantics / 의미론).

## 8. Audio focus

App phát âm thanh không tồn tại một mình. Music player, điều hướng (navigation / 내비게이션), lời gọi (call / 호출) và voice assistant có thể cạnh tranh audio focus.

Playback tầng (layer / 계층) phải xử lý focus gain/mất mát (loss / 손실)/duck theo use trường hợp (case / 사례) thay vì luôn set volume 100%.

Android 17 siết background audio tương tác (interaction / 상호작용) hơn; khi nâng mục tiêu (target / 대상)/nền tảng (platform / 플랫폼), rà soát (review / 검토) media hành vi (behavior / 동작) changes thay vì dựa vào lô-gic (logic / 논리) cũ.

# Recording và microphone

## 9. Microphone là high-trust tài nguyên (resource / 자원)

Chỉ bắt đầu bản ghi (record / 레코드) sau người dùng (user / 사용자) intent rõ. Dừng capture khi luồng (flow / 흐름) kết thúc hoặc vòng đời (lifecycle / 생명주기) không còn hợp lệ.

Nếu app cần long-running recording, foreground thực thi (execution / 실행) và notification phải tuân chính sách (policy / 정책)/hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약) phù hợp.

## 10. Audio format

Mẫu (sample / 표본) tỷ lệ (rate / 비율), channel count, codec và bộ chứa (container / 컨테이너) là những tầng (layer / 계층) khác nhau. Đừng gọi mọi tệp (file / 파일) audio là “MP3”. Nếu tính năng (feature / 기능) upload voice ghi chú (note / 노트), backend đặc tả hợp đồng (contract / 계약) phải ghi rõ format/codec/content kiểu (type / 타입).

# Files và documents

## 11. App-private tệp (file / 파일)

Dữ liệu chỉ app dùng nên ưu tiên nội bộ (internal / 내부)/app-specific lưu trữ (storage / 저장소). Không cần expose ra dùng chung (shared / 공유) lưu trữ (storage / 저장소).

Ví dụ bộ nhớ đệm (cache / 캐시) download tạm nên ở bộ nhớ đệm (cache / 캐시) directory thay vì xin broad lưu trữ (storage / 저장소) truy cập (access / 접근).

## 12. lưu trữ (storage / 저장소) truy cập (access / 접근) khung phần mềm (framework / 프레임워크)

Khi người dùng (user / 사용자) muốn chọn một document bất kỳ, SAF cung cấp hệ thống (system / 시스템) picker và trả `content://` URI.

```kotlin
val launcher = rememberLauncherForActivityResult(
    ActivityResultContracts.OpenDocument()
) { uri ->
    // read via ContentResolver
}
```

App không nên chuyển URI thành filesystem đường dẫn (path / 경로) bằng hack `_data` column. Scoped lưu trữ (storage / 저장소) và provider lớp trừu tượng (abstraction / 추상화) tồn tại để tài nguyên (resource / 자원) có thể không phải tệp (file / 파일) cục bộ (local / 로컬) truyền thống.

## 13. Photo Picker

Nếu người dùng (user / 사용자) chọn ảnh/video, Photo Picker thường giảm permission surface so với broad media truy cập (access / 접근).

Nếu chỉ cần người dùng (user / 사용자) chọn một ảnh avatar, xin quyền đọc toàn bộ gallery là over-permission.

## 14. MediaStore

Khi app tạo media cần xuất hiện trong dùng chung (shared / 공유) media thư viện (library / 라이브러리), MediaStore là API phù hợp. siêu dữ liệu (metadata / 메타데이터), pending ghi (write / 쓰기) và collection URI giúp app publish media theo hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약).

## 15. MIME kiểu (type / 타입)

Tệp (file / 파일) extension không đủ để quyết định content. Khi share/open document, dùng MIME kiểu (type / 타입) đúng và validate đầu vào (input / 입력) ở ranh giới (boundary / 경계).

# Sharing

## 16. Sharesheet

Dùng hệ thống (system / 시스템) Sharesheet cho `ACTION_SEND`/`ACTION_SEND_MULTIPLE` thay vì xây danh sách app share riêng.

Hệ thống (system / 시스템) có ranking, mục tiêu (target / 대상) filtering và privacy hành vi (behavior / 동작) tốt hơn custom chooser.

## 17. URI grant

Khi share content URI, grant read permission đúng phạm vi (scope / 범위). Không làm tệp (file / 파일) world-readable.

# Location

## 18. hiện tại (current / 현재) location và continuous tracking khác nhau

Một màn hình weather cần location một lần khác hoàn toàn workout tracking liên tục.

Use trường hợp (case / 사례) một lần nên dùng API hiện tại (current / 현재) location phù hợp thay vì giữ listener lâu sống.

Continuous tracking cần vòng đời (lifecycle / 생명주기), battery, foreground/background chính sách (policy / 정책) và tỷ lệ (rate / 비율) chiến lược (strategy / 전략).

## 19. Accuracy và battery

High-accuracy location tốn pin hơn. Nếu tính năng (feature / 기능) chỉ cần nearby city, đừng yêu cầu cập nhật (update / 업데이트) 1 giây với GPS chính xác cao.

Mô hình (model / 모델) yêu cầu (request / 요청) theo nghiệp vụ (business / 비즈니스) SLA:

```text
accuracy
freshness
latency
battery cost
background need
```

## 20. Location hết thời gian chờ (timeout / 타임아웃)

Location yêu cầu (request / 요청) có thể không trả kết quả nhanh. lĩnh vực (domain / 도메인) tầng (layer / 계층) nên có hết thời gian chờ (timeout / 타임아웃)/fallback: last-known location, manual selection hoặc người dùng (user / 사용자) thử lại (retry / 재시도).

## 21. Geofencing

Geofence phù hợp sự kiện (event / 이벤트) “enter/exit area” hơn polling location liên tục. Nhưng delivery không phải hard real-time guarantee. nghiệp vụ (business / 비즈니스) không nên dùng geofence như giao dịch (transaction / 트랜잭션) clock chính xác từng giây.

# Bluetooth Low năng lượng (energy / 에너지)

## 22. BLE khác classic Bluetooth

BLE thường dùng GATT dịch vụ (service / 서비스)/characteristic mô hình (model / 모델). Scan tìm thiết bị (device / 장치); connect tạo GATT liên kết (connection / 연결); khám phá dịch vụ (service discovery / 서비스 디스커버리) xác định năng lực (capability / 역량); characteristic read/ghi (write / 쓰기)/notify truyền dữ liệu (data / 데이터).

Mô hình tư duy (mental model / 사고 모델):

```text
scan
→ identify device
→ connect
→ discover services
→ subscribe/read/write
→ handle disconnect
→ reconnect policy
```

## 23. GATT thao tác (operation / 연산) serialization

Nhiều BLE ngăn xếp (stack / 스택)/thiết bị (device / 장치) không thích nhiều GATT thao tác (operation / 연산) bắn đồng thời. môi trường vận hành (production / 운영 환경) máy khách (client / 클라이언트) thường cần hàng đợi (queue / 큐)/serialize read-write thao tác (operation / 연산) theo đặc tả hợp đồng (contract / 계약) thiết bị (device / 장치).

## 24. Reconnect

Reconnect không nên infinite tight vòng lặp (loop / 루프). Dùng backoff, app foreground/background awareness và người dùng (user / 사용자) expectation.

Nếu thiết bị bị unpaired hoặc Bluetooth off, máy trạng thái (state machine / 상태 머신) phải chuyển thành actionable lỗi (error / 오류) thay vì spinner mãi mãi.

## 25. giao thức (protocol / 프로토콜) framing

BLE characteristic thường có payload nhỏ. Nếu lĩnh vực (domain / 도메인) message lớn, bạn cần framing/chunking/checksum/versioning riêng. Đây là mạng (network / 네트워크) giao thức (protocol / 프로토콜) thiết kế (design / 설계) thu nhỏ.

# NFC

## 26. NFC năng lực (capability / 역량)

NFC không có trên mọi thiết bị (device / 장치). Nếu app đọc tag, hãy mô hình (model / 모델) unsupported/disabled/tag-lost như normal trạng thái (state / 상태).

Tag tương tác (interaction / 상호작용) thường ngắn; đừng giữ tham chiếu (reference / 참조)/tag handle lâu quá vòng đời (lifecycle / 생명주기) của discovery sự kiện (event / 이벤트).

# Sensors

## 27. Sensor tỷ lệ (rate / 비율)

Accelerometer/gyroscope có thể phát sự kiện (event / 이벤트) tần suất cao. Sensor callback không nên làm heavy công việc (work / 작업) trực tiếp.

Sampling tỷ lệ (rate / 비율) phải phù hợp use trường hợp (case / 사례). UI orientation indicator khác motion-analysis chuỗi xử lý (pipeline / 파이프라인).

## 28. Sensor fusion

Raw sensor noisy. Nhiều tính năng (feature / 기능) cần filtering/fusion thay vì dùng một mẫu (sample / 표본) trực tiếp.

Đây là nơi math/tín hiệu (signal / 신호) processing trở nên quan trọng hơn API cú pháp (syntax / 문법).

# Connectivity

## 29. mạng (network / 네트워크) available không đồng nghĩa Internet usable

`ConnectivityManager` có thể cho biết mạng (network / 네트워크) năng lực (capability / 역량), nhưng captive portal, DNS thất bại (failure / 실패) hoặc backend outage vẫn có thể làm yêu cầu (request / 요청) thất bại (fail / 실패).

Đừng gate toàn bộ yêu cầu (request / 요청) bằng boolean `isNetworkConnected`. yêu cầu (request / 요청) thật vẫn là nguồn chuẩn (source of truth / 정본) về success/thất bại (failure / 실패).

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

## 31. WebView là trình duyệt (browser / 브라우저) engine trong ranh giới bảo mật (security boundary / 보안 경계) app

WebView có cookie/session, JS, truy cập tệp (file access / 파일 접근), điều hướng (navigation / 내비게이션), permission và cầu nối (bridge / 브리지) concern. Không coi nó như `TextView` hiển thị HTML.

## 32. JavaScript cầu nối (bridge / 브리지)

`addJavascriptInterface` tạo cầu nối (bridge / 브리지) giữa web content và bản địa (native / 네이티브) mã (code / 코드). Chỉ expose API tối thiểu, chỉ tải (load / 로드) trusted origin và validate đầu vào (input / 입력).

Không expose đối tượng (object / 객체) quyền lực cho arbitrary web content.

## 33. Web permission

Camera/mic/location yêu cầu (request / 요청) bên trong WebView vẫn cần Android permission + web-origin permission handling. Không tự động `request.grant(request.resources)` cho mọi origin.

# Tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권) trong Compose

## 34. `DisposableEffect`

Listener/tài nguyên (resource / 자원) cần acquire/bản phát hành (release / 릴리스) cùng composition có thể dùng:

```kotlin
DisposableEffect(sensorManager, listener) {
    sensorManager.registerListener(...)

    onDispose {
        sensorManager.unregisterListener(listener)
    }
}
```

Nhưng long-lived media/camera session thường nên đơn vị sở hữu (owner / 오너) ở tầng (layer / 계층) có vòng đời (lifecycle / 생명주기) rõ hơn thay vì gắn trực tiếp vào một leaf composable.

# Lỗi (error / 오류) mô hình (model / 모델)

## 35. thiết bị (device / 장치) tích hợp (integration / 통합) lỗi (error / 오류) không nên là string

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

Typed lỗi (error / 오류) cho phép UI đưa hành động (action / 동작) đúng: “Open settings”, “Turn on Bluetooth”, “thử lại (retry / 재시도)”, “Reconnect”, không chỉ toast `Something went wrong`.

# Testing

## 36. Fake ranh giới (boundary / 경계)

Hardware API nên được wrap sau giao diện (interface / 인터페이스) để lô-gic nghiệp vụ (business logic / 비즈니스 로직) kiểm thử (test / 테스트) bằng fake máy trạng thái (state machine / 상태 머신).

Ví dụ BLE repository kiểm thử (test / 테스트):

```text
Disconnected
→ Connecting
→ Ready
→ write succeeds
```

và trường hợp (case / 사례):

```text
Ready
→ permission revoked
→ PermissionDenied
```

## 37. Instrumentation/hardware kiểm thử (test / 테스트)

Fake không thay toàn bộ thiết bị (device / 장치) hành vi (behavior / 동작). giao thức (protocol / 프로토콜) trọng yếu (critical / 중요) nên có kiểm thử tích hợp (integration test / 통합 테스트) với hardware lab/thiết bị (device / 장치) ma trận (matrix / 행렬) nếu nghiệp vụ (business / 비즈니스) phụ thuộc mạnh.

# Cấp cao (senior / 시니어) Notes

## 38. thiết bị (device / 장치) tính năng (feature / 기능) là hệ thống phân tán (distributed system / 분산 시스템) nhỏ

Camera dịch vụ (service / 서비스), media decoder, Bluetooth peripheral, location provider hoặc WebView đều là thành phần (component / 컴포넌트) ngoài cốt lõi (core / 핵심) nghiệp vụ (business / 비즈니스) tiến trình (process / 프로세스). Chúng có độ trễ (latency / 지연 시간), thất bại (failure / 실패), vòng đời (lifecycle / 생명주기) và phiên bản (version / 버전) riêng. Hãy thiết kế hết thời gian chờ (timeout / 타임아웃)/khôi phục (recovery / 복구)/máy trạng thái (state machine / 상태 머신) giống khi làm mạng (network / 네트워크).

## 39. Đừng giữ tài nguyên (resource / 자원) vì sợ reopen chi phí (cost / 비용)

Camera/mic/sensor/BLE tài nguyên (resource / 자원) giữ quá lâu gây battery/privacy/xung đột (conflict / 충돌). quyền sở hữu (ownership / 소유권) đúng quan trọng hơn micro-optimization reopen.

## 40. giao thức (protocol / 프로토콜) phải phiên bản (version / 버전) được

Nếu app nói chuyện với BLE/IoT/backend/media format do công ty kiểm soát, thêm giao thức (protocol / 프로토콜) phiên bản (version / 버전)/tính tương thích (compatibility / 호환성) chiến lược (strategy / 전략) sớm. Mobile app không cập nhật (update / 업데이트) đồng thời 100% với firmware/máy chủ (server / 서버).

# Checklist kết thúc chapter

Bạn nên giải thích được khi nào dùng CameraX thay Camera2; vì sao ảnh (image / 이미지) phân tích (analysis / 분석) cần backpressure; MediaSession/audio focus liên quan playback thế nào; Photo Picker/SAF/MediaStore khác nhau ra sao; content URI khác đường dẫn (path / 경로) tệp (file / 파일); hiện tại (current / 현재) location khác continuous tracking; BLE GATT máy trạng thái (state machine / 상태 머신) gồm những bước nào; WebView permission/JS cầu nối (bridge / 브리지) có bảo mật (security / 보안) rủi ro (risk / 위험) gì; và vì sao thiết bị (device / 장치) tích hợp (integration / 통합) nên được mô hình (model / 모델) như stateful hệ thống bên ngoài (external system / 외부 시스템) chứ không phải một lời gọi API đơn lẻ.

> **Bàn giao:** Sau **40. giao thức (protocol / 프로토콜) phải phiên bản (version / 버전) được**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 architecture end to end](./01_architecture_end_to_end.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
