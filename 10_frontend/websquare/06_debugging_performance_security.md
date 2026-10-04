# 06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)

> **Mạch đọc:** [README](../README.md) là owner của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**; đặt chapter sau WebSquare fundamentals và trước case vận hành. Từ **1. môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론) bắt đầu bằng bằng chứng (evidence / 증거)** chuyển sang DevTools, performance profiling, security checks và incident recovery; mỗi bước phải truy được từ user action đến server evidence.

## 1. môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론) bắt đầu bằng bằng chứng (evidence / 증거)

WebSquare screen có nhiều lớp lớp trừu tượng (abstraction / 추상화), vì vậy gỡ lỗi (debug / 디버그) bằng cách thêm `alert()` ngẫu nhiên rất nhanh đạt giới hạn. Một sự cố (incident / 인시던트) nên được phân tích như chuỗi xử lý (pipeline / 파이프라인) có bằng chứng (evidence / 증거):

```text
user action
→ event handler
→ page state/DataCollection
→ Submission/request
→ server
→ response
→ target mapping
→ component rendering
```

Mỗi mũi tên là một ranh giới (boundary / 경계) có thể đo hoặc inspect. Khi biết ranh giới (boundary / 경계) nào sai, tìm kiếm (search / 검색) không gian (space / 공간) giảm mạnh.

> **Nối mạch:** Trong **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **1. môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론) bắt đầu bằng bằng chứng (evidence / 증거)** đặt vấn đề; **2. DevTools là công cụ chính, không phải last resort** đối chiếu bằng chứng, rồi **3. gỡ lỗi (debug / 디버그) theo tìm kiếm nhị phân (binary search / 이진 탐색) trên chuỗi xử lý (pipeline / 파이프라인)** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. DevTools là công cụ chính, không phải last resort

Trình duyệt (browser / 브라우저) DevTools vẫn là nền tảng dù khung phần mềm (framework / 프레임워크) dùng nhiều lớp trừu tượng (abstraction / 추상화).

**Console** dùng để inspect `scwin`, thành phần (component / 컴포넌트) đối tượng (object / 객체), DataMap/DataList và exception.

**Sources** dùng breakpoint, ngăn xếp lời gọi (call stack / 호출 스택), phạm vi (scope / 범위) variable và bản đồ mã nguồn (source map / 소스 맵) nếu dự án (project / 프로젝트) có.

**mạng (network / 네트워크)** xác nhận yêu cầu (request / 요청) URL, timing, payload, header, status, phản hồi (response / 응답) body và duplicate yêu cầu (request / 요청).

**hiệu năng (performance / 성능)** xác định long tác vụ (task / 작업), scripting/bố cục (layout / 레이아웃)/rendering chi phí (cost / 비용).

**bộ nhớ (memory / 메모리)** giúp tìm detached đối tượng (object / 객체), vùng nhớ động (heap / 힙) growth và tham chiếu (reference / 참조) leak.

Khung phần mềm (framework / 프레임워크) Studio debugger hữu ích, nhưng bằng chứng vận hành (production evidence / 운영 증거) trong trình duyệt (browser / 브라우저) mới phản ánh môi trường thật.

> **Nối mạch:** Ở chặng này của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **2. DevTools là công cụ chính, không phải last resort** đặt đầu vào cho **3. gỡ lỗi (debug / 디버그) theo tìm kiếm nhị phân (binary search / 이진 탐색) trên chuỗi xử lý (pipeline / 파이프라인)**, rồi **4. phạm vi (scope / 범위) debugging** mở rộng hệ quả hoặc giới hạn liên quan.

## 3. gỡ lỗi (debug / 디버그) theo tìm kiếm nhị phân (binary search / 이진 탐색) trên chuỗi xử lý (pipeline / 파이프라인)

Ví dụ “tìm kiếm (search / 검색) không ra kết quả”. Đừng đọc toàn bộ mã (code / 코드) trước.

Bước 1: mạng (network / 네트워크) có yêu cầu (request / 요청) không?

Nếu **không**, lỗi nằm trước mạng (network / 네트워크): sự kiện (event / 이벤트), kiểm tra hợp lệ (validation / 검증), phạm vi (scope / 범위) hoặc Submission thực thi (execution / 실행).

Nếu **có**, phản hồi (response / 응답) có dữ liệu (data / 데이터) không?

Nếu **không**, xem máy chủ (server / 서버)/yêu cầu (request / 요청) điều kiện (condition / 조건).

Nếu **có**, DataList mục tiêu (target / 대상) có dữ liệu (data / 데이터) không?

Nếu **không**, ánh xạ (mapping / 매핑)/mục tiêu (target / 대상) issue.

Nếu **có**, Grid có bind đúng không?

Cách chia đôi chuỗi xử lý (pipeline / 파이프라인) nhanh hơn gỡ lỗi (debug / 디버그) theo tệp (file / 파일).

> **Nối mạch:** Đặt trong câu hỏi lớn của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **3. gỡ lỗi (debug / 디버그) theo tìm kiếm nhị phân (binary search / 이진 탐색) trên chuỗi xử lý (pipeline / 파이프라인)** đặt đầu vào cho **4. phạm vi (scope / 범위) debugging**, rồi **5. Log có ngữ cảnh (context / 맥락), không log chuỗi vô nghĩa** mở rộng hệ quả hoặc giới hạn liên quan.

## 4. phạm vi (scope / 범위) debugging

Khi thấy element trên màn hình nhưng không biết đối tượng (object / 객체) thuộc frame nào, resolve phạm vi (scope / 범위) trước. Một số SP5 bản dựng (build / 빌드) có gỡ lỗi (debug / 디버그) utility như:

```javascript
$p.debug.getScope($0);
$p.debug.getFrame($0);
```

`$0` là DOM element đang được chọn trong DevTools Elements.

Mental workflow:

```text
visual element
→ DOM element
→ WebSquare frame/scope
→ component object
→ scwin/DataCollection
```

Đây là cách đặc biệt hữu ích trong TabControl/WindowContainer nhiều tầng.

> **Nối mạch:** Trong **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **4. phạm vi (scope / 범위) debugging** đặt đầu vào cho **5. Log có ngữ cảnh (context / 맥락), không log chuỗi vô nghĩa**, rồi **6. Correlation ID** mở rộng hệ quả hoặc giới hạn liên quan.

## 5. Log có ngữ cảnh (context / 맥락), không log chuỗi vô nghĩa

Sai:

```javascript
console.log("here1");
console.log("here2");
```

Tốt hơn:

```javascript
console.log("[user-search] execute", {
    condition: dmSearch.getJSON ? dmSearch.getJSON() : null,
    requestId: scwin.requestId
});
```

Trong môi trường vận hành (production / 운영 환경), tránh log PII, đơn vị từ (token / 토큰), password hoặc full phản hồi (response / 응답) nhạy cảm. Logging phải vừa đủ để correlation nhưng không biến console/log máy chủ (server / 서버) thành dữ liệu (data / 데이터) leak.

> **Nối mạch:** Ở chặng này của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **5. Log có ngữ cảnh (context / 맥락), không log chuỗi vô nghĩa** đặt đầu vào cho **6. Correlation ID**, rồi **7. Submission timing** mở rộng hệ quả hoặc giới hạn liên quan.

## 6. Correlation ID

Nếu một người dùng (user / 사용자) hành động (action / 동작) đi qua trình duyệt (browser / 브라우저) → API gateway → ứng dụng (application / 애플리케이션) máy chủ (server / 서버) → DB, correlation ID giúp nối log.

```text
browser request id
→ HTTP header
→ server log
→ downstream log
```

Máy khách (client / 클라이언트) có thể generate/yêu cầu (request / 요청) ID theo convention của hệ thống, nhưng bảo mật (security / 보안)/tracing kiến trúc (architecture / 아키텍처) phải thống nhất server-side. Đừng tự phát minh header nếu gateway đã cung cấp dấu vết (trace / 추적) ID.

> **Nối mạch:** Correlation ID nối một submission với trace/log evidence; submission timing tiếp theo đặt các mốc request, response và commit để phân biệt chậm với sai.

## 7. Submission timing

Khi màn hình chậm, đo các đoạn riêng:

```text
T_click_to_request
T_network_wait
T_response_download
T_mapping
T_render
```

Nếu yêu cầu (request / 요청) bắt đầu 800 ms sau click, máy khách (client / 클라이언트) script/kiểm tra hợp lệ (validation / 검증) đang chậm.

Nếu waiting 4 s, máy chủ (server / 서버)/mạng (network / 네트워크) là nghi phạm chính.

Nếu phản hồi (response / 응답) về nhanh nhưng UI freeze 2 s, DataCollection/Grid rendering là trọng tâm.

> **Nối mạch:** Submission timing cung cấp mốc đo; performance budget tiếp theo biến “chậm” thành số liệu, rồi Grid rendering cost chỉ ra vùng cần tối ưu.

## 8. hiệu năng (performance / 성능) ngân sách (budget / 예산) thay vì “cảm giác chậm”

Định nghĩa ngân sách (budget / 예산) theo screen quan trọng, ví dụ:

```text
search click → request start < 100 ms
API p95 < 1 s
response → interactive grid < 500 ms
main-thread task < 50 ms khi có thể
```

Con số thực tế phụ thuộc hệ thống. Điểm quan trọng là có đo lường (measurement / 측정) mục tiêu (target / 대상). Không có ngân sách (budget / 예산), nhóm (team / 팀) chỉ tranh luận bằng cảm giác.

> **Nối mạch:** Grid cost chiếm một phần budget; synchronous heavy loop trong event handler tiếp theo có thể chặn main thread và phá budget dù network vẫn nhanh.

## 9. Grid rendering chi phí (cost / 비용)

Grid lớn có thể chậm vì:

```text
quá nhiều row trả về
cell formatter nặng
nhiều merged cell/style dynamic
per-cell event
DOM/layout cost
repeated redraw
summary calculation lặp
```

Tối ưu hóa (optimization / 최적화) tốt thường bắt đầu ở dữ liệu (data / 데이터) volume và thuật toán (algorithm / 알고리즘) trước khi micro-optimize từng API.

> **Nối mạch:** Đặt trong câu hỏi lớn của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **10. Tránh synchronous heavy vòng lặp (loop / 루프) trong sự kiện (event / 이벤트) handler** nối từ **9. Grid rendering chi phí (cost / 비용)** sang **11. Debounce và search-as-you-type**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Tránh synchronous heavy vòng lặp (loop / 루프) trong sự kiện (event / 이벤트) handler

JavaScript chạy trên main luồng thực thi (thread / 스레드) cho phần lớn UI công việc (work / 작업). Nếu click handler scan hàng trăm nghìn cell synchronously, trình duyệt (browser / 브라우저) không thể paint/respond trong lúc đó.

Ví dụ O(n²):

```javascript
for (var i = 0; i < count; i++) {
    for (var j = 0; j < count; j++) {
        // duplicate search
    }
}
```

Dùng Set/Map có thể đổi thành gần O(n):

```javascript
var seen = new Set();
for (var i = 0; i < count; i++) {
    var id = dlUser.getCellData(i, "USER_ID");
    if (seen.has(id)) {
        return false;
    }
    seen.add(id);
}
```

Kiến thức độ phức tạp (complexity / 복잡도) nằm ở Khoa học máy tính (computer science / 컴퓨터 과학) chuẩn gốc (canonical / 정본) docs; WebSquare không thay đổi Big-O.

> **Nối mạch:** Trong **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **11. Debounce và search-as-you-type** nối từ **10. Tránh synchronous heavy vòng lặp (loop / 루프) trong sự kiện (event / 이벤트) handler** sang **12. bộ nhớ đệm (cache / 캐시) có vô hiệu hóa (invalidation / 무효화) chi phí (cost / 비용)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Debounce và search-as-you-type

Nếu đầu vào (input / 입력) thay đổi (change / 변경) mỗi ký tự đều gọi Submission, người dùng (user / 사용자) gõ 10 ký tự tạo 10 yêu cầu (request / 요청). Debounce có thể hợp lý cho autocomplete/tìm kiếm (search / 검색) suggestion.

Nhưng debounce không thay abort/stale-response protection. yêu cầu (request / 요청) cũ có thể vẫn về sau yêu cầu (request / 요청) mới.

Tách hai vấn đề:

```text
debounce → giảm số request
cancellation/request identity → bảo vệ ordering
```

> **Nối mạch:** Ở chặng này của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **12. bộ nhớ đệm (cache / 캐시) có vô hiệu hóa (invalidation / 무효화) chi phí (cost / 비용)** nối từ **11. Debounce và search-as-you-type** sang **13. bộ nhớ (memory / 메모리) leak trong SPA**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. bộ nhớ đệm (cache / 캐시) có vô hiệu hóa (invalidation / 무효화) chi phí (cost / 비용)

Dùng chung (common / 공통) mã (code / 코드) đôi khi bộ nhớ đệm (cache / 캐시) mã (code / 코드) danh sách (list / 목록), menu hoặc tham chiếu (reference / 참조) dữ liệu (data / 데이터) để giảm yêu cầu (request / 요청). bộ nhớ đệm (cache / 캐시) chỉ đúng khi biết thời gian tồn tại (lifetime / 수명) và vô hiệu hóa (invalidation / 무효화).

```text
static code list trong session → cache tốt
user permission có thể đổi → cần refresh policy
transaction data → thường không cache global tùy tiện
```

Bộ nhớ đệm (cache / 캐시) toàn cục (global / 전역) trong SPA sống lâu; stale trạng thái (state / 상태) có thể kéo dài hàng giờ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **13. bộ nhớ (memory / 메모리) leak trong SPA** nối từ **12. bộ nhớ đệm (cache / 캐시) có vô hiệu hóa (invalidation / 무효화) chi phí (cost / 비용)** sang **14. Timer vòng đời (lifecycle / 생명주기)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. bộ nhớ (memory / 메모리) leak trong SPA

Dấu hiệu:

```text
mở/đóng cùng screen 20 lần → heap tăng liên tục
handler cũ vẫn chạy
request duplicate tăng sau mỗi navigation
```

Nguồn phổ biến:

```text
window/document event listener không remove
timer không clear
global array giữ scope/component
closure giữ DataList lớn
third-party widget không destroy
```

Kiểm thử (test / 테스트) leak bằng repeatable điều hướng (navigation / 내비게이션) scenario và vùng nhớ động (heap / 힙) snapshot, không bằng một lần mở page.

> **Nối mạch:** Trong **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **13. bộ nhớ (memory / 메모리) leak trong SPA** đặt đầu vào cho **14. Timer vòng đời (lifecycle / 생명주기)**, rồi **15. XSS: escape đầu ra (output / 출력) nhưng hiểu ngữ cảnh (context / 맥락)** mở rộng hệ quả hoặc giới hạn liên quan.

## 14. Timer vòng đời (lifecycle / 생명주기)

Nếu page dùng timer:

```javascript
scwin.timerId = setInterval(function () {
    scwin.refreshStatus();
}, 30000);
```

phải xác định cleanup khi page đóng/chuyển. Nếu WebSquare cung cấp timer utility gắn vòng đời (lifecycle / 생명주기), ưu tiên đặc tả hợp đồng (contract / 계약) đó; nếu dùng trình duyệt (browser / 브라우저) timer, tự quản cleanup rõ.

Timer orphan tạo duplicate yêu cầu (request / 요청) và giữ tham chiếu (reference / 참조) vào page.

> **Nối mạch:** Ở chặng này của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **14. Timer vòng đời (lifecycle / 생명주기)** đặt đầu vào cho **15. XSS: escape đầu ra (output / 출력) nhưng hiểu ngữ cảnh (context / 맥락)**, rồi **16. eval và động (dynamic / 동적) hàm (function / 함수) thực thi (execution / 실행)** mở rộng hệ quả hoặc giới hạn liên quan.

## 15. XSS: escape đầu ra (output / 출력) nhưng hiểu ngữ cảnh (context / 맥락)

Cross-site scripting (XSS / 크로스 사이트 스크립팅) xảy ra khi dữ liệu không đáng tin được interpret như mã (code / 코드)/markup.

Một đầu vào (input / 입력)/Grid thuộc tính (property / 속성) có `escape` option ở một số thành phần (component / 컴포넌트)/bản dựng (build / 빌드), nhưng đừng coi một thuộc tính (property / 속성) là lá chắn toàn cục. Escape phải đúng ngữ cảnh (context / 맥락):

```text
HTML text
HTML attribute
JavaScript string
URL
CSS
```

Không dùng `innerHTML`/HTML-rendering chế độ (mode / 모드) cho user-controlled dữ liệu (data / 데이터) trừ khi sanitize bằng cơ chế được phê duyệt.

> **Nối mạch:** Đặt trong câu hỏi lớn của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **16. eval và động (dynamic / 동적) hàm (function / 함수) thực thi (execution / 실행)** nối từ **15. XSS: escape đầu ra (output / 출력) nhưng hiểu ngữ cảnh (context / 맥락)** sang **17. Client-side hidden/readOnly không bảo vệ dữ liệu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. `eval` và động (dynamic / 동적) hàm (function / 함수) thực thi (execution / 실행)

Legacy WebSquare mẫu (pattern / 패턴) đôi khi truyền callback name dạng string và `eval`. `eval` làm mã (code / 코드) khó kiểm tra (audit / 감사) và mở injection rủi ro (risk / 위험) nếu string chịu ảnh hưởng từ bên ngoài (external / 외부) đầu vào (input / 입력).

Quy tắc (rule / 규칙):

```text
Không eval dữ liệu từ user/server.
Nếu legacy callback bắt buộc, dùng allowlist function name nội bộ.
Ưu tiên direct function contract khi có thể.
```

> **Nối mạch:** Trong **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **16. eval và động (dynamic / 동적) hàm (function / 함수) thực thi (execution / 실행)** đặt vấn đề; **17. Client-side hidden/readOnly không bảo vệ dữ liệu** đối chiếu bằng chứng, rồi **18. CSRF, session và authentication** mở rộng hệ quả hoặc giới hạn liên quan.

## 17. Client-side hidden/readOnly không bảo vệ dữ liệu

Một trường dữ liệu (field / 필드) role `ADMIN` bị hidden vẫn có thể bị sửa bằng DevTools nếu yêu cầu (request / 요청) trust máy khách (client / 클라이언트) payload.

Máy chủ (server / 서버) phải whitelist writable fields:

```text
client sends USER_ID, NAME, ROLE
server knows caller may edit NAME only
→ ignore/reject ROLE change
```

Authorization không được delegate cho WebSquare UI.

> **Nối mạch:** Ở chặng này của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **17. Client-side hidden/readOnly không bảo vệ dữ liệu** đặt vấn đề; **18. CSRF, session và authentication** đối chiếu bằng chứng, rồi **19. Sensitive dữ liệu (data / 데이터) trong DataCollection** mở rộng hệ quả hoặc giới hạn liên quan.

## 18. CSRF, session và authentication

WebSquare Submission vẫn là HTTP yêu cầu (request / 요청). Nếu app dùng cookie session, Cross-Site yêu cầu (request / 요청) Forgery (CSRF / 사이트 간 요청 위조) vẫn là threat tùy kiến trúc (architecture / 아키텍처).

Protection có thể gồm same-site cookie, CSRF đơn vị từ (token / 토큰), origin checks hoặc khung phần mềm (framework / 프레임워크) bảo mật (security / 보안) cơ chế (mechanism / 메커니즘). hiện thực (implementation / 구현) thuộc máy chủ (server / 서버)/bảo mật (security / 보안) ngăn xếp (stack / 스택), không phải “WebSquare tự lo”.

> **Nối mạch:** Đặt trong câu hỏi lớn của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **18. CSRF, session và authentication** đặt vấn đề; **19. Sensitive dữ liệu (data / 데이터) trong DataCollection** đối chiếu bằng chứng, rồi **20. tệp (file / 파일) upload** mở rộng hệ quả hoặc giới hạn liên quan.

## 19. Sensitive dữ liệu (data / 데이터) trong DataCollection

DataCollection ở trình duyệt (browser / 브라우저) có thể inspect. Không đưa secret server-side, private key, cơ sở dữ liệu (database / 데이터베이스) credential hoặc kiểm soát truy cập (access control / 접근 제어) quy tắc (rule / 규칙) nhạy cảm vào máy khách (client / 클라이언트) mô hình (model / 모델).

Đơn vị từ (token / 토큰)/session dữ liệu (data / 데이터) nếu buộc phải ở máy khách (client / 클라이언트) phải theo bảo mật (security / 보안) kiến trúc (architecture / 아키텍처) của hệ thống. `hidden=true` không làm secret.

> **Nối mạch:** Trong **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **19. Sensitive dữ liệu (data / 데이터) trong DataCollection** đặt vấn đề; **20. tệp (file / 파일) upload** đối chiếu bằng chứng, rồi **21. Excel injection** mở rộng hệ quả hoặc giới hạn liên quan.

## 20. tệp (file / 파일) upload

Tệp (file / 파일) upload cần kiểm tra server-side:

```text
size
extension và MIME
magic bytes/content
malware policy
storage path
filename normalization
authorization
```

Máy khách (client / 클라이언트) kiểm tra hợp lệ (validation / 검증) chỉ để UX. Filename do người dùng (user / 사용자) cung cấp không được dùng trực tiếp làm máy chủ (server / 서버) đường dẫn (path / 경로).

> **Nối mạch:** Ở chặng này của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **21. Excel injection** nối từ **20. tệp (file / 파일) upload** sang **22. lỗi (error / 오류) message không nên leak internals**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Excel injection

Nếu export dữ liệu user-controlled sang Excel/CSV, cell bắt đầu bằng `=`, `+`, `-`, `@` có thể được spreadsheet interpret như formula tùy format/ứng dụng (application / 애플리케이션).

Nếu hệ thống xuất tệp (file / 파일) cho người dùng (user / 사용자) khác mở, cần xem xét formula injection chính sách (policy / 정책). Đây là ranh giới bảo mật (security boundary / 보안 경계) thường bị bỏ qua ở enterprise grid export.

> **Nối mạch:** Đặt trong câu hỏi lớn của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **22. lỗi (error / 오류) message không nên leak internals** nối từ **21. Excel injection** sang **23. thử lại (retry / 재시도) chỉ an toàn khi hiểu idempotency**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. lỗi (error / 오류) message không nên leak internals

Máy chủ (server / 서버) dấu vết ngăn xếp (stack trace / 스택 트레이스), SQL, bảng (table / 테이블) name, filesystem đường dẫn (path / 경로) không nên hiện nguyên cho end người dùng (user / 사용자).

Máy khách (client / 클라이언트) có thể log correlation ID và hiển thị message phù hợp:

```text
“처리 중 오류가 발생했습니다. 문의 시 오류번호 ABC-123을 알려 주세요.”
```

Nhà phát triển (developer / 개발자) tra máy chủ (server / 서버) log bằng ID.

> **Nối mạch:** Trong **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **23. thử lại (retry / 재시도) chỉ an toàn khi hiểu idempotency** nối từ **22. lỗi (error / 오류) message không nên leak internals** sang **24. hết thời gian chờ (timeout / 타임아웃) là sản phẩm (product / 제품) quyết định (decision / 결정)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. thử lại (retry / 재시도) chỉ an toàn khi hiểu idempotency

Tìm kiếm (search / 검색) GET-like thao tác (operation / 연산) thường thử lại (retry / 재시도) dễ hơn Save mutation.

Nếu thử lại (retry / 재시도) Save sau hết thời gian chờ (timeout / 타임아웃), yêu cầu (request / 요청) đầu có thể đã lần ghi nhận (commit / 커밋) nhưng phản hồi (response / 응답) mất. yêu cầu (request / 요청) thứ hai có thể duplicate giao dịch (transaction / 트랜잭션).

Với thao tác (operation / 연산) quan trọng, máy chủ (server / 서버) nên có idempotency chiến lược (strategy / 전략) hoặc giao dịch (transaction / 트랜잭션) key phù hợp. máy khách (client / 클라이언트) không tự động thử lại (retry / 재시도) mutation một cách mù quáng.

> **Nối mạch:** Ở chặng này của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **24. hết thời gian chờ (timeout / 타임아웃) là sản phẩm (product / 제품) quyết định (decision / 결정)** nối từ **23. thử lại (retry / 재시도) chỉ an toàn khi hiểu idempotency** sang **25. cấu hình (config / 설정) và môi trường (environment / 환경) drift**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. hết thời gian chờ (timeout / 타임아웃) là sản phẩm (product / 제품) quyết định (decision / 결정)

Hết thời gian chờ (timeout / 타임아웃) quá ngắn tạo false thất bại (failure / 실패); quá dài làm người dùng (user / 사용자) treo. Chọn dựa endpoint SLO và UX. Khi hết thời gian chờ (timeout / 타임아웃), UI phải cho biết thao tác (operation / 연산) trạng thái (state / 상태) và khả năng thử lại (retry / 재시도).

Nếu trạng thái (state / 상태) máy chủ (server / 서버) không chắc chắn, message “save failed” có thể sai; có thể cần “không xác định kết quả, hãy kiểm tra lại”.

> **Nối mạch:** Đặt trong câu hỏi lớn của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **25. cấu hình (config / 설정) và môi trường (environment / 환경) drift** nối từ **24. hết thời gian chờ (timeout / 타임아웃) là sản phẩm (product / 제품) quyết định (decision / 결정)** sang **26. bộ nhớ đệm (cache / 캐시) busting và stale sản phẩm tạo ra (artifact / 산출물)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. cấu hình (config / 설정) và môi trường (environment / 환경) drift

WebSquare dự án (project / 프로젝트) có máy khách (client / 클라이언트)/máy chủ (server / 서버) cấu hình (config / 설정), tài nguyên (resource / 자원) đường dẫn (path / 경로) và engine setting. cục bộ (local / 로컬), UAT và môi trường vận hành (production / 운영 환경) có thể khác.

Một bug chỉ có môi trường vận hành (production / 운영 환경) nên kiểm tra (audit / 감사):

```text
engine build
config.xml/client config
server config
context root
resource cache/CDN
browser support
security header
reverse proxy path
```

Không giả định mã nguồn (source code / 소스 코드) giống nhau thì hành vi thời gian chạy (runtime behavior / 런타임 동작) giống nhau.

> **Nối mạch:** Trong **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **26. bộ nhớ đệm (cache / 캐시) busting và stale sản phẩm tạo ra (artifact / 산출물)** nối từ **25. cấu hình (config / 설정) và môi trường (environment / 환경) drift** sang **27. bản đồ mã nguồn (source map / 소스 맵) và minification**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. bộ nhớ đệm (cache / 캐시) busting và stale sản phẩm tạo ra (artifact / 산출물)

W-Pack tạo JavaScript sản phẩm tạo ra (artifact / 산출물). Nếu deploy XML/nguồn (source / 소스) mới nhưng trình duyệt (browser / 브라우저)/CDN vẫn giữ JS sản phẩm tạo ra (artifact / 산출물) cũ, người dùng (user / 사용자) có thể chạy mã (code / 코드) khác nguồn (source / 소스) bạn đang đọc.

Khi bug “máy tôi sửa rồi nhưng người dùng (user / 사용자) vẫn thấy cũ”, kiểm tra:

```text
artifact thực deploy
response cache headers
service worker nếu có
CDN/proxy cache
browser cache
versioned resource URL
```

> **Nối mạch:** Ở chặng này của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **26. bộ nhớ đệm (cache / 캐시) busting và stale sản phẩm tạo ra (artifact / 산출물)** đặt vấn đề; **27. bản đồ mã nguồn (source map / 소스 맵) và minification** đối chiếu bằng chứng, rồi **28. trình duyệt (browser / 브라우저) tính tương thích (compatibility / 호환성)** mở rộng hệ quả hoặc giới hạn liên quan.

## 27. bản đồ mã nguồn (source map / 소스 맵) và minification

Môi trường vận hành (production / 운영 환경) sản phẩm tạo ra (artifact / 산출물) có thể minify/obfuscate. bản đồ mã nguồn (source map / 소스 맵) giúp dấu vết ngăn xếp (stack trace / 스택 트레이스) quay về nguồn (source / 소스) dễ hơn nhưng có bảo mật (security / 보안)/triển khai (deployment / 배포) sự đánh đổi (trade-off / 트레이드오프). Có thể giữ bản đồ mã nguồn (source map / 소스 맵) private cho khả năng quan sát (observability / 관측 가능성) thay vì công khai (public / 공개) nếu chính sách (policy / 정책) yêu cầu.

Đừng gỡ lỗi (debug / 디버그) môi trường vận hành (production / 운영 환경) minified ngăn xếp (stack / 스택) bằng cách đoán nếu bản dựng (build / 빌드) chuỗi xử lý (pipeline / 파이프라인) có thể cung cấp ánh xạ (mapping / 매핑).

> **Nối mạch:** Đặt trong câu hỏi lớn của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **27. bản đồ mã nguồn (source map / 소스 맵) và minification** đặt vấn đề; **28. trình duyệt (browser / 브라우저) tính tương thích (compatibility / 호환성)** đối chiếu bằng chứng, rồi **29. khả năng tiếp cận (accessibility / 접근성)** mở rộng hệ quả hoặc giới hạn liên quan.

## 28. trình duyệt (browser / 브라우저) tính tương thích (compatibility / 호환성)

WebSquare engine hỗ trợ trình duyệt (browser / 브라우저) ma trận (matrix / 행렬) theo phiên bản (version / 버전). dự án (project / 프로젝트) legacy có thể còn IE-specific mã (code / 코드); hiện đại (modern / 현대적) triển khai (deployment / 배포) thường evergreen trình duyệt (browser / 브라우저).

Đừng giữ polyfill/workaround chỉ vì “WebSquare cũ từng cần”. Xác định mức hỗ trợ trình duyệt (browser support / 브라우저 지원) chính sách (policy / 정책) hiện tại rồi loại dead tính tương thích (compatibility / 호환성) mã (code / 코드) có kiểm soát.

> **Nối mạch:** Trong **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **29. khả năng tiếp cận (accessibility / 접근성)** nối từ **28. trình duyệt (browser / 브라우저) tính tương thích (compatibility / 호환성)** sang **30. khả năng quan sát (observability / 관측 가능성) của page quan trọng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. khả năng tiếp cận (accessibility / 접근성)

Enterprise app vẫn cần khả năng tiếp cận (accessibility / 접근성). Grid, form, popup và keyboard luồng (flow / 흐름) phải dùng ngữ nghĩa (semantic / 의미적) label/tab thứ tự (order / 순서)/focus management phù hợp.

Thành phần (component / 컴포넌트) thuộc tính (property / 속성) hỗ trợ khả năng tiếp cận (accessibility / 접근성) nhưng ứng dụng (application / 애플리케이션) lô-gic (logic / 논리) vẫn phải đảm bảo:

```text
focus sau popup mở/đóng
keyboard navigation
error announcement
label association
contrast
no keyboard trap
```

> **Nối mạch:** Ở chặng này của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **30. khả năng quan sát (observability / 관측 가능성) của page quan trọng** nối từ **29. khả năng tiếp cận (accessibility / 접근성)** sang **31. sự cố (incident / 인시던트) example: Save bị duplicate ngẫu nhiên**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. khả năng quan sát (observability / 관측 가능성) của page quan trọng

Một screen trọng yếu (critical / 중요) có thể instrument:

```text
screen load duration
search request latency
save success/failure rate
client exception count
large result size
popup load error
```

Không cần log mọi click. Chọn tín hiệu (signal / 신호) giúp vận hành.

> **Nối mạch:** Đặt trong câu hỏi lớn của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **30. khả năng quan sát (observability / 관측 가능성) của page quan trọng** nêu quy tắc; **31. sự cố (incident / 인시던트) example: Save bị duplicate ngẫu nhiên** thử quy tắc trong tình huống, rồi **32. sự cố (incident / 인시던트) example: Screen càng dùng lâu càng chậm** mở rộng hệ quả.

## 31. sự cố (incident / 인시던트) example: Save bị duplicate ngẫu nhiên

Triệu chứng: cơ sở dữ liệu (database / 데이터베이스) đôi lúc có hai bản ghi (record / 레코드).

Đi theo bằng chứng (evidence / 증거):

1. mạng (network / 네트워크) dấu vết (trace / 추적) cho thấy hai yêu cầu (request / 요청) giống nhau cách nhau 80 ms.
2. Click handler log cũng chạy hai lần.
3. Button chưa disable cho đến sau một async kiểm tra hợp lệ (validation / 검증) callback.
4. người dùng (user / 사용자) double-click tạo hai luồng (flow / 흐름) song song.

Máy khách (client / 클라이언트) fix: set in-flight guard ngay khi thao tác (operation / 연산) bắt đầu.

Máy chủ (server / 서버) fix: unique ràng buộc (constraint / 제약조건)/idempotency/giao dịch (transaction / 트랜잭션) bất biến (invariant / 불변식) để duplicate không thể lần ghi nhận (commit / 커밋) nếu nghiệp vụ (business / 비즈니스) không cho phép.

Bài học: máy khách (client / 클라이언트) fix UX, máy chủ (server / 서버) fix tính đúng đắn (correctness / 정확성).

> **Nối mạch:** Trong **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **31. sự cố (incident / 인시던트) example: Save bị duplicate ngẫu nhiên** nêu quy tắc; **32. sự cố (incident / 인시던트) example: Screen càng dùng lâu càng chậm** thử quy tắc trong tình huống, rồi **33. môi trường vận hành (production / 운영 환경) readiness checklist** mở rộng hệ quả.

## 32. sự cố (incident / 인시던트) example: Screen càng dùng lâu càng chậm

Bằng chứng (evidence / 증거):

1. Fresh reload: 1 yêu cầu (request / 요청) mỗi 30 s.
2. Sau 10 lần mở/đóng tab: 10 yêu cầu (request / 요청) mỗi 30 s.
3. vùng nhớ động (heap / 힙) snapshot giữ 10 phạm vi (scope / 범위) instance cũ.
4. Mỗi page start `setInterval` nhưng không clear.

Fix nằm ở vòng đời (lifecycle / 생명주기) cleanup, không ở API máy chủ (server / 서버).

> **Nối mạch:** Ở chặng này của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **32. sự cố (incident / 인시던트) example: Screen càng dùng lâu càng chậm** nêu quy tắc; **33. môi trường vận hành (production / 운영 환경) readiness checklist** thử quy tắc trong tình huống, rồi **34. Kết nối** mở rộng hệ quả.

## 33. môi trường vận hành (production / 운영 환경) readiness checklist

Trước bản phát hành (release / 릴리스) screen quan trọng:

```text
No duplicate submission on double click
All error paths restore UI state
Authorization enforced server-side
Sensitive data not logged
Large dataset tested
SPA open/close leak tested
Network failure tested
Slow server tested
Popup/frame race tested
Browser matrix tested
Accessibility basics checked
Cache/deploy artifact verified
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **06 — Debugging, hiệu năng (performance / 성능), bảo mật (security / 보안) & môi trường vận hành (production / 운영 환경)**, **34. Kết nối** nối từ **33. môi trường vận hành (production / 운영 환경) readiness checklist** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## 34. Kết nối

Môi trường vận hành (production / 운영 환경) mã (code / 코드) thường sống lâu qua nhiều WebSquare generation. Chapter cuối giúp đọc và migrate mã (code / 코드) cũ mà không phá ngữ nghĩa (semantics / 의미론): [07 — Legacy, Modern Evolution & Migration](07_legacy_modern_migration.md).

> **Bàn giao:** Sau **34. Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
