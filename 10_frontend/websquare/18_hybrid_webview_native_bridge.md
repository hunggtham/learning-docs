# 18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Hybrid WebSquare không chỉ là website đặt trong app** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. trình duyệt (browser / 브라우저) năng lực (capability / 역량) và bản địa (native / 네이티브) năng lực (capability / 역량) phải được tách** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối WebView với native bridge và capability của từng phía, để thiết kế biên giao tiếp có kiểm soát thay vì coi app như một website.

## 1. Hybrid WebSquare không chỉ là website đặt trong app

Một hybrid ứng dụng (application / 애플리케이션) thường dùng bản địa (native / 네이티브) shell để chứa WebView, còn phần lớn UI/nghiệp vụ (business / 비즈니스) screen chạy bằng WebSquare/JavaScript. Nhưng khi cần camera, biometrics, push notification, tệp (file / 파일) hệ thống (system / 시스템), app-to-app launch hoặc secure lưu trữ (storage / 저장소), JavaScript phải đi qua bản địa (native / 네이티브) năng lực (capability / 역량).

Mô hình tư duy (mental model / 사고 모델):

```text
WebSquare page
    ↓
JavaScript runtime
    ↓
WebView boundary
    ↓
native bridge / Cordova-style plugin / app-defined plugin
    ↓
iOS / Android capability
```

Đây là một phân tán (distributed / 분산) ranh giới (boundary / 경계) nằm trong cùng thiết bị. Hai bên có vòng đời (lifecycle / 생명주기), lỗi (error / 오류) mô hình (model / 모델) và bảo mật (security / 보안) mô hình (model / 모델) khác nhau.

> **Chuyển mạch:** Hybrid WebSquare có hai capability surface: browser và native. WebSquare.hybridApp chỉ báo hiệu môi trường; bridge architecture tiếp theo phải định nghĩa contract rõ.

## 2. trình duyệt (browser / 브라우저) năng lực (capability / 역량) và bản địa (native / 네이티브) năng lực (capability / 역량) phải được tách

Một screen có thể chạy trong desktop Chrome, mobile trình duyệt (browser / 브라우저) và hybrid WebView. Không nên giả định mọi môi trường có cùng API.

Ví dụ conceptual:

```javascript
if (isHybridRuntime()) {
    return nativeCamera.capture();
}
return webCameraFallback();
```

Điểm quan trọng không phải tên helper. Điều quan trọng là năng lực (capability / 역량) detection phải nằm ở một lớp trừu tượng (abstraction / 추상화) ranh giới (boundary / 경계) thay vì rải `if (Android)`/`if (iPhone)` trong từng screen.

> **Chuyển mạch:** Browser/native capability đã được tách; `WebSquare.hybridApp` chỉ là environment signal, còn bridge tiếp theo phải được thiết kế như local RPC contract.

## 3. `WebSquare.hybridApp` là môi trường (environment / 환경) tín hiệu (signal / 신호), không phải kiến trúc (architecture / 아키텍처)

Tài liệu WebSquare có những luồng (flow / 흐름) dùng `WebSquare.hybridApp` để phân biệt trình duyệt (browser / 브라우저) với hybrid thời gian chạy (runtime / 런타임), ví dụ tệp (file / 파일) download trên mobile. tín hiệu (signal / 신호) này hữu ích để chọn đường đi mã (code path / 코드 경로).

Nhưng kiến trúc vận hành (production architecture / 운영 아키텍처) vẫn nên có adapter:

```text
screen
  ↓
platformService.download(...)
  ├─ browser adapter
  └─ hybrid adapter
```

Screen không nên biết Cordova đường dẫn (path / 경로), Android intent hay iOS temporary directory.

> **Chuyển mạch:** Bridge là RPC cục bộ với payload có version; không truyền runtime object qua bridge, chỉ truyền dữ liệu serializable và lỗi có mã rõ.

## 4. bản địa (native / 네이티브) cầu nối (bridge / 브리지) là RPC cục bộ

Khi JavaScript gọi plugin bản địa (native / 네이티브), hãy lập luận (reasoning / 추론) như remote procedure lời gọi (call / 호출) (RPC), dù hai bên ở cùng tiến trình (process / 프로세스)/app.

```text
JS creates request
→ serialize arguments
→ bridge dispatch
→ native executes
→ native serializes result/error
→ JS callback/promise resumes
```

Từ mô hình tư duy (mental model / 사고 모델) này suy ra ngay các vấn đề: serialization, hết thời gian chờ (timeout / 타임아웃), duplicate callback, vòng đời (lifecycle / 생명주기) cancellation, phiên bản (version / 버전) mismatch và lỗi (error / 오류) translation.

> **Chuyển mạch:** Trong **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **5. Không truyền đối tượng (object / 객체) thời gian chạy (runtime / 런타임) qua cầu nối (bridge / 브리지)** tiếp nhận điểm tựa từ **4. bản địa (native / 네이티브) cầu nối (bridge / 브리지) là RPC cục bộ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Callback đặc tả hợp đồng (contract / 계약) phải có exactly-once ngữ nghĩa (semantics / 의미론) ở mức ứng dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Không truyền đối tượng (object / 객체) thời gian chạy (runtime / 런타임) qua cầu nối (bridge / 브리지)

Thành phần (component / 컴포넌트) instance, DOM nút (node / 노드), `scwin`, DataList đối tượng (object / 객체) hay hàm (function / 함수) không phải payload cầu nối (bridge / 브리지) tốt.

Cầu nối (bridge / 브리지) đặc tả hợp đồng (contract / 계약) nên dùng thành phần nguyên thủy (primitive / 기본 요소)/plain dữ liệu (data / 데이터):

```javascript
{
    requestId: "REQ-123",
    documentType: "ID_CARD",
    options: {
        allowGallery: false,
        quality: 0.85
    }
}
```

Bản địa (native / 네이티브) trả về dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약):

```javascript
{
    requestId: "REQ-123",
    status: "SUCCESS",
    fileToken: "..."
}
```

Không để bản địa (native / 네이티브) biết GridView ID hoặc WebSquare phạm vi (scope / 범위) topology.

> **Chuyển mạch:** Ở chặng này của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **6. Callback đặc tả hợp đồng (contract / 계약) phải có exactly-once ngữ nghĩa (semantics / 의미론) ở mức ứng dụng** tiếp nhận điểm tựa từ **5. Không truyền đối tượng (object / 객체) thời gian chạy (runtime / 런타임) qua cầu nối (bridge / 브리지)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Page thời gian tồn tại (lifetime / 수명) và bản địa (native / 네이티브) thao tác (operation / 연산) thời gian tồn tại (lifetime / 수명) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Callback đặc tả hợp đồng (contract / 계약) phải có exactly-once ngữ nghĩa (semantics / 의미론) ở mức ứng dụng

Một plugin bug có thể callback hai lần, hoặc callback success sau khi screen đã đóng. Screen mã (code / 코드) không nên mutate trạng thái (state / 상태) vô điều kiện.

Có thể guard bằng yêu cầu (request / 요청) trạng thái (state / 상태):

```text
PENDING
  ├─ SUCCESS → terminal
  ├─ ERROR   → terminal
  └─ CANCEL  → terminal
```

Sau terminal trạng thái (state / 상태), callback cùng yêu cầu (request / 요청) ID phải bị ignore hoặc log anomaly.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **7. Page thời gian tồn tại (lifetime / 수명) và bản địa (native / 네이티브) thao tác (operation / 연산) thời gian tồn tại (lifetime / 수명) khác nhau** tiếp nhận điểm tựa từ **6. Callback đặc tả hợp đồng (contract / 계약) phải có exactly-once ngữ nghĩa (semantics / 의미론) ở mức ứng dụng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. App background/foreground là vòng đời (lifecycle / 생명주기) sự kiện (event / 이벤트) thật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Page thời gian tồn tại (lifetime / 수명) và bản địa (native / 네이티브) thao tác (operation / 연산) thời gian tồn tại (lifetime / 수명) khác nhau

Người dùng (user / 사용자) mở eKYC camera từ page A, rồi app background hoặc người dùng (user / 사용자) đóng tab/page. bản địa (native / 네이티브) camera có thể vẫn đang chạy.

Khi bản địa (native / 네이티브) callback về, page phạm vi (scope / 범위) cũ có thể đã bị destroy.

Sai giả định (assumption / 가정):

```text
operation started by page A
→ page A chắc chắn còn tồn tại khi operation kết thúc
```

Đúng lập luận (reasoning / 추론):

```text
operation lifetime độc lập
→ callback phải kiểm tra owner/session/page validity
```

Đây là stale callback bài toán (problem / 문제) tương tự stale Submission phản hồi (response / 응답), nhưng crossing bản địa (native / 네이티브) ranh giới (boundary / 경계).

> **Chuyển mạch:** Trong **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **7. Page thời gian tồn tại (lifetime / 수명) và bản địa (native / 네이티브) thao tác (operation / 연산) thời gian tồn tại (lifetime / 수명) khác nhau** xác định đầu vào; **8. App background/foreground là vòng đời (lifecycle / 생명주기) sự kiện (event / 이벤트) thật** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **9. bản địa (native / 네이티브) permission là máy trạng thái (state machine / 상태 머신)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. App background/foreground là vòng đời (lifecycle / 생명주기) sự kiện (event / 이벤트) thật

Trình duyệt (browser / 브라우저) desktop thường giữ page active tương đối ổn định. Mobile OS có thể pause WebView, reclaim bộ nhớ (memory / 메모리) hoặc kill tiến trình (process / 프로세스) khi background.

Vì vậy trạng thái (state / 상태) quan trọng không nên chỉ tồn tại trong một closure.

Phân loại trạng thái (state / 상태):

```text
ephemeral UI state → có thể mất
recoverable workflow state → cần persist/checkpoint
security-sensitive secret → dùng storage phù hợp, không localStorage tùy tiện
```

Một eKYC luồng (flow / 흐름) 5 bước cần biết sau resume người dùng (user / 사용자) đang ở bước nào và máy chủ (server / 서버) đã ghi nhận gì.

> **Chuyển mạch:** Ở chặng này của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **8. App background/foreground là vòng đời (lifecycle / 생명주기) sự kiện (event / 이벤트) thật** xác định đầu vào; **9. bản địa (native / 네이티브) permission là máy trạng thái (state machine / 상태 머신)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **10. Permission success không đồng nghĩa thao tác (operation / 연산) success** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. bản địa (native / 네이티브) permission là máy trạng thái (state machine / 상태 머신)

Camera/location/lưu trữ (storage / 저장소) permission không phải boolean cố định. Có thể là:

```text
not requested
allowed
rejected
rejected permanently / don't ask again
restricted by policy
```

UI phải map từng trạng thái (state / 상태) sang hành động (action / 동작) phù hợp. Nếu permission bị deny vĩnh viễn, gọi yêu cầu (request / 요청) lại vô hạn chỉ tạo UX vòng lặp (loop / 루프); có thể cần hướng người dùng (user / 사용자) tới hệ thống (system / 시스템) settings.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **10. Permission success không đồng nghĩa thao tác (operation / 연산) success** tiếp nhận điểm tựa từ **9. bản địa (native / 네이티브) permission là máy trạng thái (state machine / 상태 머신)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Deep link là bên ngoài (external / 외부) đầu vào (input / 입력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Permission success không đồng nghĩa thao tác (operation / 연산) success

Camera permission được cấp nhưng camera có thể unavailable, người dùng (user / 사용자) cancel, thiết bị (device / 장치) lưu trữ (storage / 저장소) full hoặc bản địa (native / 네이티브) SDK thất bại (fail / 실패).

Tách:

```text
permission result
capability availability
operation result
business result
```

Không collapse tất cả thành `false`.

> **Chuyển mạch:** Trong **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **11. Deep link là bên ngoài (external / 외부) đầu vào (input / 입력)** tiếp nhận điểm tựa từ **10. Permission success không đồng nghĩa thao tác (operation / 연산) success** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Deep link routing và WebSquare điều hướng (navigation / 내비게이션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Deep link là bên ngoài (external / 외부) đầu vào (input / 입력)

Một hybrid app có thể được mở bằng custom scheme hoặc universal/app link.

Ví dụ conceptual:

```text
myapp://ekyc/result?token=...
```

Deep-link payload là untrusted đầu vào (input / 입력) giống URL từ web. Không dùng nó trực tiếp để quyết định privileged hành động (action / 동작).

Server-side đơn vị từ (token / 토큰) kiểm tra hợp lệ (validation / 검증), expiry, nonce/trạng thái (state / 상태) correlation và allowlisted tuyến (route / 경로) là những điều khiển (control / 제어) thường cần.

> **Chuyển mạch:** Ở chặng này của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **12. Deep link routing và WebSquare điều hướng (navigation / 내비게이션)** tiếp nhận điểm tựa từ **11. Deep link là bên ngoài (external / 외부) đầu vào (input / 입력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. bản địa (native / 네이티브) → Web callback phải đi qua một gateway** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Deep link routing và WebSquare điều hướng (navigation / 내비게이션)

Bản địa (native / 네이티브) shell nhận deep link trước, sau đó cần tuyến (route / 경로) vào WebSquare page/screen. Có hai timing trường hợp (case / 사례):

```text
app already running
→ WebView/page shell ready
→ dispatch route immediately

cold start
→ native receives link
→ WebView chưa ready
→ store pending route
→ engine/shell ready
→ dispatch route
```

Nếu không có pending-route trạng thái (state / 상태), deep link cold start sẽ thỉnh thoảng “mất”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **13. bản địa (native / 네이티브) → Web callback phải đi qua một gateway** tiếp nhận điểm tựa từ **12. Deep link routing và WebSquare điều hướng (navigation / 내비게이션)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. sự kiện (event / 이벤트) envelope** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. bản địa (native / 네이티브) → Web callback phải đi qua một gateway

Đừng để bản địa (native / 네이티브) tầng (layer / 계층) gọi ngẫu nhiên `scwin.someFunction()` của screen hiện tại bằng string.

Tốt hơn:

```text
native event
→ bridge gateway
→ validate event envelope
→ route by event type/requestId
→ application service
→ current page reacts
```

Gateway làm versioning, logging và bảo mật (security / 보안) dễ hơn.

> **Chuyển mạch:** Trong **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **14. sự kiện (event / 이벤트) envelope** tiếp nhận điểm tựa từ **13. bản địa (native / 네이티브) → Web callback phải đi qua một gateway** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. cầu nối (bridge / 브리지) versioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. sự kiện (event / 이벤트) envelope

Một sự kiện (event / 이벤트) đặc tả hợp đồng (contract / 계약) tốt có thể gồm:

```javascript
{
    version: 1,
    type: "EKYC_COMPLETED",
    requestId: "REQ-123",
    timestamp: 1780000000000,
    payload: {
        sessionId: "..."
    }
}
```

`type` cho routing, `version` cho tính tương thích (compatibility / 호환성), `requestId` cho correlation. Payload chỉ chứa dữ liệu (data / 데이터) cần thiết.

> **Chuyển mạch:** Ở chặng này của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **15. cầu nối (bridge / 브리지) versioning** tiếp nhận điểm tựa từ **14. sự kiện (event / 이벤트) envelope** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Backward tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. cầu nối (bridge / 브리지) versioning

Web bundle và bản địa (native / 네이티브) app không phải lúc nào deploy cùng lúc. người dùng (user / 사용자) có thể chạy bản địa (native / 네이티브) app phiên bản (version / 버전) cũ nhưng tải WebSquare tài nguyên (resource / 자원) mới từ máy chủ (server / 서버).

Đây là tính tương thích (compatibility / 호환성) bài toán (problem / 문제) quan trọng:

```text
Web vNext expects nativePlugin.fooV2()
Native app old only has fooV1()
→ runtime failure
```

Cần năng lực (capability / 역량)/phiên bản (version / 버전) handshake.

```text
web asks native capabilities
→ native returns appVersion + pluginVersion/features
→ web selects compatible path
```

Đừng chỉ check người dùng (user / 사용자) tác nhân (agent / 에이전트).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **16. Backward tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **15. cầu nối (bridge / 브리지) versioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Authentication trong WebView** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Backward tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)

Một bản phát hành (release / 릴리스) nên biết các cặp được hỗ trợ (support / 지원):

```text
web build A ↔ app 5.2+
web build B ↔ app 5.4+
```

Nếu web deploy độc lập, máy chủ (server / 서버)/CDN có thể cần serve compatible bundle theo app phiên bản (version / 버전) hoặc web phải degrade gracefully.

Hybrid môi trường vận hành (production / 운영 환경) thất bại (failure / 실패) rất hay xuất hiện khi nhóm (team / 팀) web và mobile bản phát hành (release / 릴리스) theo cadence khác nhau.

> **Chuyển mạch:** Trong **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **17. Authentication trong WebView** tiếp nhận điểm tựa từ **16. Backward tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Không nhét long-lived secret vào JavaScript toàn cục (global / 전역)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Authentication trong WebView

Hybrid app có thể dùng cookie session, truy cập (access / 접근) đơn vị từ (token / 토큰) hoặc native-managed credential. Dù cơ chế nào, ranh giới (boundary / 경계) phải rõ:

```text
native auth state
↕
WebView auth state
↕
backend session/token state
```

Nếu bản địa (native / 네이티브) refresh đơn vị từ (token / 토큰) nhưng WebView vẫn giữ cookie/đơn vị từ (token / 토큰) cũ, người dùng (user / 사용자) có thể thấy app “đã login” nhưng WebSquare yêu cầu (request / 요청) nhận 401.

Auth synchronization phải là tường minh (explicit / 명시적) giao thức (protocol / 프로토콜).

> **Chuyển mạch:** Ở chặng này của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **18. Không nhét long-lived secret vào JavaScript toàn cục (global / 전역)** tiếp nhận điểm tựa từ **17. Authentication trong WebView** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. XSS trong hybrid có thể nguy hiểm hơn web thường** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Không nhét long-lived secret vào JavaScript toàn cục (global / 전역)

WebView JavaScript có thể bị inspect/gỡ lỗi (debug / 디버그) ở môi trường development và chịu XSS rủi ro (risk / 위험) như web. Long-lived refresh đơn vị từ (token / 토큰)/private credential không nên được đặt vào `window`, `scwin` hoặc DataCollection nếu bản địa (native / 네이티브) secure lưu trữ (storage / 저장소) có thể giữ chúng.

Web tầng (layer / 계층) nên nhận năng lực (capability / 역량)/đơn vị từ (token / 토큰) có thời gian tồn tại (lifetime / 수명) và phạm vi (scope / 범위) tối thiểu cần thiết.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **19. XSS trong hybrid có thể nguy hiểm hơn web thường** tiếp nhận điểm tựa từ **18. Không nhét long-lived secret vào JavaScript toàn cục (global / 전역)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. cầu nối (bridge / 브리지) allowlist thay vì generic execute(command, args)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. XSS trong hybrid có thể nguy hiểm hơn web thường

Nếu injected JavaScript có quyền gọi bản địa (native / 네이티브) cầu nối (bridge / 브리지) mạnh, XSS có thể trở thành bản địa (native / 네이티브) năng lực (capability / 역량) abuse.

Ví dụ cầu nối (bridge / 브리지) cung cấp:

```text
readFile(path)
openExternalApp(...)
getDeviceId()
```

thì attacker script có thể gọi chúng nếu cầu nối (bridge / 브리지) không kiểm soát origin/caller/hành động (action / 동작).

Cầu nối (bridge / 브리지) phải expose API tối thiểu, validate argument và áp dụng authorization/chính sách (policy / 정책) ở bản địa (native / 네이티브) side khi cần.

> **Chuyển mạch:** Trong **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **20. cầu nối (bridge / 브리지) allowlist thay vì generic execute(command, args)** tiếp nhận điểm tựa từ **19. XSS trong hybrid có thể nguy hiểm hơn web thường** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. tệp (file / 파일) download trên hybrid** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. cầu nối (bridge / 브리지) allowlist thay vì generic `execute(command, args)`

Một generic cầu nối (bridge / 브리지) cho phép string command bất kỳ rất linh hoạt nhưng khó kiểm tra (audit / 감사).

Prefer đặc tả hợp đồng (contract / 계약) rõ:

```text
camera.capture
file.download
biometric.authenticate
app.openSettings
```

thay vì:

```text
native.execute("some arbitrary class/method", args)
```

Surface nhỏ hơn giúp giảm attack surface và di chuyển (migration / 마이그레이션) rủi ro (risk / 위험).

> **Chuyển mạch:** Ở chặng này của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **21. tệp (file / 파일) download trên hybrid** tiếp nhận điểm tựa từ **20. cầu nối (bridge / 브리지) allowlist thay vì generic execute(command, args)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Popup/trình duyệt (browser / 브라우저) launch trong hybrid** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. tệp (file / 파일) download trên hybrid

Tài liệu WebSquare có ví dụ mobile download dùng Cordova `FileTransfer`, chọn directory khác nhau giữa iOS và Android rồi mở tệp (file / 파일) bằng bản địa (native / 네이티브)/hệ thống (system / 시스템) mục tiêu (target / 대상).

Đừng bản sao (copy / 복사) đường dẫn (path / 경로) literal từ mẫu (sample / 표본) vào môi trường vận hành (production / 운영 환경) mà không kiểm tra plugin/nền tảng (platform / 플랫폼) phiên bản (version / 버전). Filesystem permission mô hình (model / 모델) thay đổi theo Android/iOS phiên bản (version / 버전).

Lớp trừu tượng (abstraction / 추상화) nên là:

```javascript
platformService.downloadFile({ url, fileName, mimeType })
```

và bản địa (native / 네이티브) adapter chịu trách nhiệm đường dẫn (path / 경로)/permission/open hành vi (behavior / 동작).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **22. Popup/trình duyệt (browser / 브라우저) launch trong hybrid** tiếp nhận điểm tựa từ **21. tệp (file / 파일) download trên hybrid** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. bên ngoài (external / 외부) app launch và fallback** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Popup/trình duyệt (browser / 브라우저) launch trong hybrid

`window.open()` trong WebView có thể không giống desktop trình duyệt (browser / 브라우저). mục tiêu (target / 대상) `_blank`, `_system`, embedded trình duyệt (browser / 브라우저) plugin hoặc OS trình duyệt (browser / 브라우저) có ngữ nghĩa (semantics / 의미론) khác nhau tùy shell/plugin.

Trước khi dùng, quyết định intent:

```text
mở nội bộ trong WebView?
mở browser ngoài app?
mở native app khác?
```

Rồi map intent sang nền tảng (platform / 플랫폼) adapter.

> **Chuyển mạch:** Trong **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **23. bên ngoài (external / 외부) app launch và fallback** tiếp nhận điểm tựa từ **22. Popup/trình duyệt (browser / 브라우저) launch trong hybrid** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. eKYC như một phân tán (distributed / 분산) workflow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. bên ngoài (external / 외부) app launch và fallback

Nếu cần mở banking/eKYC/định danh (identity / 식별자) app khác:

```text
check capability / attempt launch
        ↓
success → wait for callback/deep link
        ↓
fail → store/app-store/web fallback
```

Không giả định app đích đã cài.

Callback phải correlate với yêu cầu (request / 요청)/session ban đầu để tránh nhận kết quả (result / 결과) của luồng (flow / 흐름) cũ.

> **Chuyển mạch:** Ở chặng này của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **23. bên ngoài (external / 외부) app launch và fallback** xác định đầu vào; **24. eKYC như một phân tán (distributed / 분산) workflow** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **25. yêu cầu (request / 요청) ID xuyên các tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. eKYC như một phân tán (distributed / 분산) workflow

Một eKYC luồng (flow / 흐름) có thể đi qua:

```text
WebSquare screen
→ native camera/SDK
→ vendor SDK/server
→ app callback
→ WebSquare
→ project backend
```

Không tầng (layer / 계층) nào một mình sở hữu toàn bộ giao dịch (transaction / 트랜잭션).

Cần workflow trạng thái (state / 상태) tường minh (explicit / 명시적):

```text
CREATED
CAPTURE_STARTED
CAPTURE_COMPLETED
SUBMITTED
VERIFIED
REJECTED
EXPIRED
```

UI chỉ kết xuất (render / 렌더링) workflow trạng thái (state / 상태); không nên suy trạng thái chỉ từ việc popup/camera đã đóng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **24. eKYC như một phân tán (distributed / 분산) workflow** xác định đầu vào; **25. yêu cầu (request / 요청) ID xuyên các tầng (layer / 계층)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **26. Offline và flaky mạng (network / 네트워크)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. yêu cầu (request / 요청) ID xuyên các tầng (layer / 계층)

Một yêu cầu (request / 요청) ID duy nhất giúp dấu vết (trace / 추적):

```text
WebSquare log
native log
vendor callback
backend log
```

Nếu mỗi tầng (layer / 계층) tự sinh ID mà không map, sự cố (incident / 인시던트) “camera thành công nhưng UI không cập nhật (update / 업데이트)” sẽ rất khó điều tra.

> **Chuyển mạch:** Trong **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **26. Offline và flaky mạng (network / 네트워크)** tiếp nhận điểm tựa từ **25. yêu cầu (request / 요청) ID xuyên các tầng (layer / 계층)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. thử lại (retry / 재시도) phải dựa trên thao tác (operation / 연산) ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Offline và flaky mạng (network / 네트워크)

Hybrid app thường chạy trên cellular mạng (network / 네트워크). mạng (network / 네트워크) có thể chuyển Wi-Fi ↔ LTE, mất vài giây hoặc app background giữa yêu cầu (request / 요청).

Read thao tác (operation / 연산) có thể thử lại (retry / 재시도) với backoff nếu idempotent. Mutation phải có idempotency ngữ nghĩa (semantics / 의미론).

Bản địa (native / 네이티브) thao tác (operation / 연산) success nhưng máy chủ (server / 서버) submit thất bại (fail / 실패) là một trạng thái (state / 상태) riêng; đừng bắt người dùng (user / 사용자) chụp lại ảnh nếu sản phẩm tạo ra (artifact / 산출물)/session vẫn còn hợp lệ.

> **Chuyển mạch:** Ở chặng này của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **27. thử lại (retry / 재시도) phải dựa trên thao tác (operation / 연산) ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **26. Offline và flaky mạng (network / 네트워크)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. ngân sách thời gian chờ (timeout budget / 타임아웃 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. thử lại (retry / 재시도) phải dựa trên thao tác (operation / 연산) ngữ nghĩa (semantics / 의미론)

```text
GET status → thường retry được
upload chunk → có thể retry nếu protocol hỗ trợ
create payment → cần idempotency key
launch camera → retry nghĩa là user action mới, không auto-loop
```

Một helper `retryAll()` cho mọi cầu nối (bridge / 브리지)/mạng (network / 네트워크) lời gọi (call / 호출) là anti-pattern.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **28. ngân sách thời gian chờ (timeout budget / 타임아웃 예산)** tiếp nhận điểm tựa từ **27. thử lại (retry / 재시도) phải dựa trên thao tác (operation / 연산) ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Cancellation đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. ngân sách thời gian chờ (timeout budget / 타임아웃 예산)

Một luồng (flow / 흐름) qua nhiều tầng (layer / 계층) cần ngân sách thời gian chờ (timeout budget / 타임아웃 예산):

```text
Web UI timeout
native plugin timeout
vendor SDK timeout
backend timeout
```

Nếu UI hết thời gian chờ (timeout / 타임아웃) 10s nhưng bản địa (native / 네이티브) SDK hợp lệ mất 30s, UI sẽ báo thất bại (fail / 실패) trong khi thao tác (operation / 연산) vẫn tiếp tục.

Hết thời gian chờ (timeout / 타임아웃) phải phản ánh quyền sở hữu (ownership / 소유권): hết thời gian chờ (timeout / 타임아웃) có cancel thao tác (operation / 연산) thật không, hay chỉ ngừng chờ?

> **Chuyển mạch:** Trong **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **29. Cancellation đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **28. ngân sách thời gian chờ (timeout budget / 타임아웃 예산)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. WebView bộ nhớ đệm (cache / 캐시) và stale tài nguyên (resource / 자원)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Cancellation đặc tả hợp đồng (contract / 계약)

Người dùng (user / 사용자) bấm Cancel trong UI. Có ba khả năng:

```text
cancel chỉ UI waiting
cancel native operation
cancel cả server/vendor session
```

Đặc tả hợp đồng (contract / 계약) phải tường minh (explicit / 명시적). Nếu bản địa (native / 네이티브) không cancel được, mark yêu cầu (request / 요청) abandoned và ignore late callback.

> **Chuyển mạch:** Ở chặng này của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **29. Cancellation đặc tả hợp đồng (contract / 계약)** nêu điều cần giải thích; **30. WebView bộ nhớ đệm (cache / 캐시) và stale tài nguyên (resource / 자원)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **31. Remote debugging và môi trường vận hành (production / 운영 환경) privacy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. WebView bộ nhớ đệm (cache / 캐시) và stale tài nguyên (resource / 자원)

Bản địa (native / 네이티브) app upgrade nhưng WebView bộ nhớ đệm (cache / 캐시) vẫn giữ JS/W-Pack cũ, hoặc ngược lại. Hybrid sự cố (incident / 인시던트) vì vậy phải bản ghi (record / 레코드) cả:

```text
native app version
OS version
WebView version
WebSquare engine build
web artifact/build ID
config version
```

Chỉ hỏi “app phiên bản (version / 버전) bao nhiêu?” là chưa đủ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **30. WebView bộ nhớ đệm (cache / 캐시) và stale tài nguyên (resource / 자원)** nêu điều cần giải thích; **31. Remote debugging và môi trường vận hành (production / 운영 환경) privacy** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **32. Crash vs JavaScript lỗi (error / 오류)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Remote debugging và môi trường vận hành (production / 운영 환경) privacy

Development có thể bật WebView remote debugging, console và WebSquare gỡ lỗi (debug / 디버그) facilities. môi trường vận hành (production / 운영 환경) phải cân bằng khả năng quan sát (observability / 관측 가능성) với exposure.

Không log truy cập (access / 접근) đơn vị từ (token / 토큰), citizen ID, raw eKYC ảnh (image / 이미지), biometric kết quả (result / 결과) chi tiết hoặc full deep-link secret.

Gỡ lỗi (debug / 디버그) bản dựng (build / 빌드) và môi trường vận hành (production / 운영 환경) bản dựng (build / 빌드) cần chính sách (policy / 정책) khác nhau.

> **Chuyển mạch:** Trong **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **32. Crash vs JavaScript lỗi (error / 오류)** tiếp nhận điểm tựa từ **31. Remote debugging và môi trường vận hành (production / 운영 환경) privacy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Testing ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Crash vs JavaScript lỗi (error / 오류)

Hybrid có ít nhất ba miền lỗi (failure domain / 장애 도메인):

```text
JavaScript/WebSquare error
WebView/process error
native app/plugin crash
```

JavaScript `try/catch` không bắt bản địa (native / 네이티브) crash. bản địa (native / 네이티브) crash reporter không tự chứa WebSquare trạng thái (state / 상태) trước crash.

Sự cố (incident / 인시던트) correlation cần telemetry ở cả hai phía.

> **Chuyển mạch:** Ở chặng này của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **33. Testing ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **32. Crash vs JavaScript lỗi (error / 오류)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) cho cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Testing ma trận (matrix / 행렬)

Hybrid tính năng (feature / 기능) không thể chỉ kiểm thử (test / 테스트) Chrome desktop.

Minimum lập luận (reasoning / 추론) ma trận (matrix / 행렬):

```text
Android + supported WebView
Android permission denied/allowed
Android background/resume

iOS + supported WKWebView
iOS permission denied/allowed
iOS background/resume

old supported app + new web
new app + current web
slow/offline network
cold-start deep link
warm deep link
```

Không nhất thiết mọi lần ghi nhận (commit / 커밋) chạy toàn ma trận (matrix / 행렬), nhưng bản phát hành (release / 릴리스) rủi ro (risk / 위험) phải được cover có chủ đích.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **34. đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) cho cầu nối (bridge / 브리지)** tiếp nhận điểm tựa từ **33. Testing ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. môi trường vận hành (production / 운영 환경) checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) cho cầu nối (bridge / 브리지)

Cầu nối (bridge / 브리지) adapter có thể được kiểm thử (test / 테스트) bằng fake bản địa (native / 네이티브) hiện thực (implementation / 구현):

```javascript
var fakeBridge = {
    capture: function (request) {
        return Promise.resolve({
            requestId: request.requestId,
            status: "SUCCESS",
            fileToken: "TEST_TOKEN"
        });
    }
};
```

Mục tiêu là kiểm thử (test / 테스트) WebSquare workflow mà không cần camera thật. bản địa (native / 네이티브) nhóm (team / 팀) kiểm thử (test / 테스트) đặc tả hợp đồng (contract / 계약) tương tự ở phía bản địa (native / 네이티브).

> **Chuyển mạch:** Trong **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **35. môi trường vận hành (production / 운영 환경) checklist** tiếp nhận điểm tựa từ **34. đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) cho cầu nối (bridge / 브리지)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. cấp cao (senior / 시니어) mẫu (pattern / 패턴): nền tảng (platform / 플랫폼) dịch vụ (service / 서비스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. môi trường vận hành (production / 운영 환경) checklist

Trước khi bản phát hành (release / 릴리스) hybrid tính năng (feature / 기능), trả lời được:

```text
Bridge contract version là gì?
Old app có gọi được web mới không?
Operation có requestId không?
Late callback xử lý thế nào?
Page đóng trước callback thì sao?
Permission denied/permanent denied thì sao?
App background giữa flow thì sao?
Deep link cold start có mất không?
Native capability có allowlist không?
Sensitive data có đi vào JS/log không?
Có test old app/new web compatibility không?
```

> **Chuyển mạch:** Ở chặng này của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **36. cấp cao (senior / 시니어) mẫu (pattern / 패턴): nền tảng (platform / 플랫폼) dịch vụ (service / 서비스)** tiếp nhận điểm tựa từ **35. môi trường vận hành (production / 운영 환경) checklist** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. cấp cao (senior / 시니어) mẫu (pattern / 패턴): nền tảng (platform / 플랫폼) dịch vụ (service / 서비스)

Screen nên phụ thuộc vào intent-level API:

```javascript
platformService.captureIdentityDocument(options)
platformService.downloadFile(file)
platformService.openExternalVerification(session)
platformService.authenticateBiometric(options)
```

Bên dưới mới quyết định trình duyệt (browser / 브라우저), Cordova, Android hoặc iOS hiện thực (implementation / 구현).

Nhờ vậy nghiệp vụ (business / 비즈니스) screen không biến thành collection của nền tảng (platform / 플랫폼) `if/else`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **37. Kết nối** tiếp nhận điểm tựa từ **36. cấp cao (senior / 시니어) mẫu (pattern / 패턴): nền tảng (platform / 플랫폼) dịch vụ (service / 서비스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Mastery checkpoint** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Kết nối

Hybrid chapter dựa trên [04 — Scope, WFrame, Popup & SPA](04_scope_wframe_popup_spa.md) để hiểu page thời gian tồn tại (lifetime / 수명), [10 — Rendering, Lazy Loading & Lifetime](10_rendering_lazy_loading_lifetime.md) để hiểu tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명), [15 — Backend Contract, Transaction & Concurrency](15_backend_contract_transaction_concurrency.md) để hiểu phân tán (distributed / 분산) workflow và [17 — File/Excel Pipeline](17_file_excel_upload_download_pipeline.md) cho mobile download.

Cách dấu vết (trace / 추적) sự cố (incident / 인시던트) xuyên WebSquare/bản địa (native / 네이티브)/backend được tiếp tục ở [19 — Observability & Incident Response](19_observability_incident_response.md).

> **Chuyển mạch:** Trong **18 — Hybrid App, WebView & bản địa (native / 네이티브) cầu nối (bridge / 브리지)**, **38. Mastery checkpoint** tiếp nhận điểm tựa từ **37. Kết nối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 38. Mastery checkpoint

Bạn đã master phần hybrid khi không còn nghĩ “gọi plugin rồi callback”. Bạn phải nhìn thấy một RPC ranh giới (boundary / 경계) có phiên bản (version / 버전), serialization, vòng đời (lifecycle / 생명주기), permission, bảo mật (security / 보안), tính tương thích (compatibility / 호환성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론); đồng thời thiết kế WebSquare screen sao cho trình duyệt (browser / 브라우저) và bản địa (native / 네이티브) hiện thực (implementation / 구현) có thể thay đổi mà nghiệp vụ (business / 비즈니스) workflow vẫn giữ bất biến (invariant / 불변식).

> **Bàn giao:** Sau **38. Mastery checkpoint**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
