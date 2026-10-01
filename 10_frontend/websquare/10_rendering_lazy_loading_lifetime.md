# 10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Một page có nhiều mốc sẵn sàng** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. onpageload không có nghĩa toàn nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) đã ready** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

WebSquare screen có thể “tải (load / 로드) xong” theo nhiều nghĩa khác nhau. nguồn (source / 소스) đã tải chưa? Script đã eval chưa? phạm vi (scope / 범위) đã tạo chưa? DataCollection đã tồn tại chưa? thành phần (component / 컴포넌트) đối tượng (object / 객체) đã được tạo chưa? DOM đã kết xuất (render / 렌더링) chưa? `onpageload` đã chạy chưa? Submission đầu tiên đã hoàn thành chưa?

Nếu gom tất cả thành một từ “loaded”, mã (code / 코드) dễ tạo race điều kiện (condition / 조건) và hiệu năng (performance / 성능) regression. Chapter này xây mô hình tư duy (mental model / 사고 모델) chi tiết cho **tải (load / 로드) → instantiate → kết xuất (render / 렌더링) → activate → data-ready → unload**, đặc biệt với WFrame, TabControl, preload, SPA và screen sống lâu.

## 1. Một page có nhiều mốc sẵn sàng

Hãy tách tối thiểu các trạng thái sau:

```text
source available
→ script evaluated
→ scope/data objects created
→ UI component objects created
→ DOM/render complete
→ page lifecycle callback executed
→ initial async data ready
```

Tùy thành phần (component / 컴포넌트)/cấu hình (config / 설정)/bản dựng (build / 빌드), một số bước có thể gần nhau hoặc được tối ưu khác đi. Nhưng distinction vẫn quan trọng.

Một đối tượng (object / 객체) tồn tại không đồng nghĩa UI của nó đã kết xuất (render / 렌더링). Một page kết xuất (render / 렌더링) xong không đồng nghĩa dữ liệu nghiệp vụ đã tải (load / 로드) xong.

> **Chuyển mạch:** Một page có nhiều readiness milestones; onpageload chỉ là một mốc, còn WFrame tiếp theo phân tán lifecycle và cần signal rõ cho từng vùng UI.

## 2. `onpageload` không có nghĩa toàn nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) đã ready

Mẫu (pattern / 패턴) phổ biến:

```javascript
scwin.onpageload = function () {
    scwin.search();
};
```

Nếu `search()` bắt đầu Submission async, `onpageload` có thể return trước khi phản hồi (response / 응답) về.

Do đó parent không nên suy:

```text
child onpageload đã chạy
⇒ child data đã sẵn sàng
```

Nếu parent cần “child ready with initial dữ liệu (data / 데이터)”, child nên có tường minh (explicit / 명시적) readiness đặc tả hợp đồng (contract / 계약) ở sau Submission success.

> **Chuyển mạch:** Ở chặng này của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **2. onpageload không có nghĩa toàn nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) đã ready** xác định đầu vào; **3. WFrame tạo phân tán (distributed / 분산) vòng đời (lifecycle / 생명주기) trong cùng trình duyệt (browser / 브라우저)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **4. setTimeout không phải vòng đời (lifecycle / 생명주기) API** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. WFrame tạo phân tán (distributed / 분산) vòng đời (lifecycle / 생명주기) trong cùng trình duyệt (browser / 브라우저)

Một shell page có thể chứa WFrame A; A chứa TabControl; một tab chứa WFrame B; B gọi Submission. Mỗi tầng (layer / 계층) có vòng đời (lifecycle / 생명주기) riêng.

Nguồn (source / 소스) thứ tự (order / 순서) không mô tả thời gian chạy (runtime / 런타임) thứ tự (ordering / 순서).

```text
shell ready
├─ A source loading
│  ├─ A scope ready
│  └─ tab selected
│     └─ B source loading
│        ├─ B rendered
│        └─ B data request pending
```

Khi bug chỉ xuất hiện “đôi lúc”, hãy vẽ timeline này trước khi thêm `setTimeout`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **3. WFrame tạo phân tán (distributed / 분산) vòng đời (lifecycle / 생명주기) trong cùng trình duyệt (browser / 브라우저)** xác định đầu vào; **4. setTimeout không phải vòng đời (lifecycle / 생명주기) API** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **5. tải (load / 로드), preload và kết xuất (render / 렌더링) là ba chi phí khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. `setTimeout` không phải vòng đời (lifecycle / 생명주기) API

Anti-pattern:

```javascript
wframe1.setSrc("detail.xml");
setTimeout(function () {
    wframe1.getWindow().scwin.initDetail();
}, 500);
```

500 ms chỉ là phỏng đoán dựa trên máy/mạng (network / 네트워크) hiện tại. Ở môi trường vận hành (production / 운영 환경) hoặc trượt bộ nhớ đệm (cache miss / 캐시 미스), tải (load / 로드) có thể lâu hơn; trên máy nhanh, mã (code / 코드) chỉ chậm vô ích.

Đúng hướng là dùng sự kiện (event / 이벤트)/callback/readiness đặc tả hợp đồng (contract / 계약) mà thành phần (component / 컴포넌트)/bản dựng (build / 빌드) hỗ trợ.

> **Chuyển mạch:** Trong **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **4. setTimeout không phải vòng đời (lifecycle / 생명주기) API** xác định đầu vào; **5. tải (load / 로드), preload và kết xuất (render / 렌더링) là ba chi phí khác nhau** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6. TabControl alwaysDraw** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. tải (load / 로드), preload và kết xuất (render / 렌더링) là ba chi phí khác nhau

Một page có thể tải nguồn (source / 소스)/script trước nhưng chưa kết xuất (render / 렌더링) UI. Điều này tạo ba nhóm chi phí (cost / 비용):

```text
network/resource load
JavaScript parse/eval/object creation
DOM/layout/paint/render
```

Tối ưu phải biết bottleneck nằm ở nhóm nào.

Nếu mạng (network / 네트워크) chậm, lazy kết xuất (render / 렌더링) không sửa bandwidth. Nếu DOM quá lớn, preload nguồn (source / 소스) không giải quyết kết xuất (render / 렌더링) chi phí (cost / 비용).

> **Chuyển mạch:** Load, preload và render là ba chi phí riêng; TabControl `alwaysDraw` quyết định vùng nào trả chi phí render sớm thay vì lazy.

## 6. TabControl `alwaysDraw`

Official SP5 guide giải thích `alwaysDraw` quyết định nội dung tab có được kết xuất (render / 렌더링) tất cả ngay ban đầu hay chỉ kết xuất (render / 렌더링) khi tab được chọn.

Mô hình tư duy (mental model / 사고 모델):

```text
alwaysDraw=true
→ startup cost cao hơn
→ child UI sẵn sàng sớm hơn

alwaysDraw=false
→ startup nhẹ hơn
→ first-open cost chuyển sang thời điểm user chọn tab
```

Không có giá trị “luôn đúng”. Quyết định phụ thuộc số tab, thành phần (component / 컴포넌트) độ phức tạp (complexity / 복잡도), initial dữ liệu (data / 데이터) và tương tác (interaction / 상호작용) xác suất (probability / 확률).

> **Chuyển mạch:** `alwaysDraw` quyết định eager rendering ở host; `frameMode="wframe"` tiếp theo tách page content và lifecycle để lazy-load có boundary rõ.

## 7. `frameMode="wframe"` và lazy page content

Với tab content dùng WFrame và `alwaysDraw=false`, page của tab chưa chọn có thể chưa được tải/kết xuất (render / 렌더링) cho đến khi người dùng (user / 사용자) mở tab.

Hệ quả kiến trúc (architecture / 아키텍처):

```text
Không được gọi component trong tab chưa activate như thể nó đã tồn tại.
Không nên load data cho tab user có thể không bao giờ mở.
Không nên đặt business dependency bắt buộc vào side effect của tab lazy chưa chạy.
```

Nếu main page cần dữ liệu chung, dữ liệu đó không nên được khởi tạo tình cờ trong một tab optional.

> **Chuyển mạch:** Trong **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **8. frameMode="wframePreload" tạo trạng thái trung gian rất quan trọng** tiếp nhận điểm tựa từ **7. frameMode="wframe" và lazy page content** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Thiết kế hàm (function / 함수) theo readiness yêu cầu (requirement / 요구사항)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. `frameMode="wframePreload"` tạo trạng thái trung gian rất quan trọng

Official guide mô tả `wframePreload` có thể tải script và tạo đối tượng (object / 객체) trước khi tab được kết xuất (render / 렌더링). DataCollection và `scwin` có thể truy cập được, nhưng mã (code / 코드) đụng trực tiếp UI thành phần (component / 컴포넌트) có thể lỗi vì thành phần (component / 컴포넌트) chưa kết xuất (render / 렌더링) hoàn chỉnh; `onpageload` của tab chưa nhất thiết chạy ở preload stage.

Đây là ví dụ hoàn hảo cho distinction:

```text
object-ready ≠ render-ready
```

Nếu hàm (function / 함수) có thể được gọi ở preload stage, hàm (function / 함수) đó nên tách pure/dữ liệu (data / 데이터) lô-gic (logic / 논리) khỏi UI manipulation.

> **Chuyển mạch:** Ở chặng này của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **9. Thiết kế hàm (function / 함수) theo readiness yêu cầu (requirement / 요구사항)** tiếp nhận điểm tựa từ **8. frameMode="wframePreload" tạo trạng thái trung gian rất quan trọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Lazy loading thay đổi vị trí độ trễ (latency / 지연 시간), không xóa độ trễ (latency / 지연 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Thiết kế hàm (function / 함수) theo readiness yêu cầu (requirement / 요구사항)

Thay vì một `init()` làm mọi thứ:

```javascript
scwin.init = function () {
    dmSearch.set(...);
    inputName.setValue(...);
    grid1.redraw();
    scwin.search();
};
```

có thể tách:

```javascript
scwin.initModel = function () {
    // chỉ cần data objects
};

scwin.initView = function () {
    // cần component đã render
};

scwin.loadInitialData = function () {
    // async boundary
};
```

Tên hàm (function / 함수) biểu diễn prerequisite, giảm việc gọi sai vòng đời (lifecycle / 생명주기) stage.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **10. Lazy loading thay đổi vị trí độ trễ (latency / 지연 시간), không xóa độ trễ (latency / 지연 시간)** tiếp nhận điểm tựa từ **9. Thiết kế hàm (function / 함수) theo readiness yêu cầu (requirement / 요구사항)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Preload là speculation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Lazy loading thay đổi vị trí độ trễ (latency / 지연 시간), không xóa độ trễ (latency / 지연 시간)

Nếu một tab nặng mất 800 ms để tải (load / 로드)/kết xuất (render / 렌더링), lazy loading có thể làm initial page nhanh hơn nhưng người dùng (user / 사용자) chịu 800 ms khi mở tab lần đầu.

Vì vậy cần quyết định UX:

```text
startup latency hay first-use latency quan trọng hơn?
user có khả năng mở tab này bao nhiêu?
resource có thể preload khi browser idle không?
```

Không nên gọi mọi lazy chiến lược (strategy / 전략) là “hiệu năng (performance / 성능) improvement” nếu chỉ di chuyển chi phí (cost / 비용) đến tương tác (interaction / 상호작용) đường găng (critical path / 임계 경로).

> **Chuyển mạch:** Trong **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **11. Preload là speculation** tiếp nhận điểm tựa từ **10. Lazy loading thay đổi vị trí độ trễ (latency / 지연 시간), không xóa độ trễ (latency / 지연 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Rendering chi phí (cost / 비용) tăng theo số đối tượng (object / 객체)/DOM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Preload là speculation

Preload có lợi khi xác suất người dùng (user / 사용자) dùng tài nguyên (resource / 자원) cao và chi phí (cost / 비용) mạng (network / 네트워크) đáng kể. Nó lãng phí khi preload nhiều tab người dùng (user / 사용자) không dùng.

Mô hình tư duy (mental model / 사고 모델):

```text
expected benefit ≈ probability of use × saved latency - preload cost
```

Không cần tính chính xác bằng công thức; chỉ cần lập luận (reasoning / 추론) theo xác suất và chi phí (cost / 비용) thay vì bật preload mặc định.

> **Chuyển mạch:** Ở chặng này của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **12. Rendering chi phí (cost / 비용) tăng theo số đối tượng (object / 객체)/DOM** tiếp nhận điểm tựa từ **11. Preload là speculation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Grid virtual/bản địa (native / 네이티브) và visibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Rendering chi phí (cost / 비용) tăng theo số đối tượng (object / 객체)/DOM

Grid, repeated thành phần (component / 컴포넌트), nested WFrame và complex UDC tạo đối tượng (object / 객체)/DOM lớn. Official hiệu năng (performance / 성능) guide nhấn mạnh số cell/DOM đối tượng (object / 객체), đặc biệt Grid hiển thị nhiều row, ảnh hưởng bộ nhớ (memory / 메모리) và rendering thời gian (time / 시간).

Khi screen lag, đo:

```text
row count
visible DOM count
render duration
script duration
heap retained size
```

Đừng chỉ đo HTTP phản hồi (response / 응답).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **13. Grid virtual/bản địa (native / 네이티브) và visibility** tiếp nhận điểm tựa từ **12. Rendering chi phí (cost / 비용) tăng theo số đối tượng (object / 객체)/DOM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. khả năng tiếp cận (accessibility / 접근성) có thể tăng kết xuất (render / 렌더링) footprint** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Grid virtual/bản địa (native / 네이티브) và visibility

Grid renderer có thể tối ưu bằng chỉ kết xuất (render / 렌더링) phần visible hoặc dùng chế độ (mode / 모드) khác tùy bản dựng (build / 빌드)/thuộc tính (property / 속성). sự đánh đổi (trade-off / 트레이드오프) thường là:

```text
ít DOM → memory/render tốt hơn
nhưng lifecycle/scroll/render behavior phức tạp hơn
```

Mã (code / 코드) không nên dựa vào giả định mọi row luôn tồn tại thành DOM nút (node / 노드). Hãy thao tác bằng DataList/Grid API công khai (public API / 공개 API).

> **Chuyển mạch:** Trong **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **14. khả năng tiếp cận (accessibility / 접근성) có thể tăng kết xuất (render / 렌더링) footprint** tiếp nhận điểm tựa từ **13. Grid virtual/bản địa (native / 네이티브) và visibility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. phạm vi (scope / 범위) giúp cleanup nhưng không cứu được tham chiếu (reference / 참조) toàn cục (global / 전역)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. khả năng tiếp cận (accessibility / 접근성) có thể tăng kết xuất (render / 렌더링) footprint

Một số khả năng tiếp cận (accessibility / 접근성) chế độ (mode / 모드) cần nhiều ngữ nghĩa (semantic / 의미적) DOM hơn. Nếu đồng thời cấu hình `visibleRowNum="all"` với hàng nghìn row, chi phí (cost / 비용) có thể tăng đáng kể.

Fix đúng không phải mặc định tắt khả năng tiếp cận (accessibility / 접근성); hãy giảm dataset/kết xuất (render / 렌더링) footprint và đo.

Xem [09 — Forms, Validation, Internationalization & Accessibility](09_forms_validation_i18n_accessibility.md).

> **Chuyển mạch:** Ở chặng này của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, sau nội dung của **14. khả năng tiếp cận (accessibility / 접근성) có thể tăng kết xuất (render / 렌더링) footprint**, **15. phạm vi (scope / 범위) giúp cleanup nhưng không cứu được tham chiếu (reference / 참조) toàn cục (global / 전역)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **16. tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) phải có đơn vị sở hữu (owner / 오너)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. phạm vi (scope / 범위) giúp cleanup nhưng không cứu được tham chiếu (reference / 참조) toàn cục (global / 전역)

Official hiệu năng (performance / 성능) guidance khuyến nghị đặt hàm (function / 함수)/giá trị (value / 값) nghiệp vụ (business / 비즈니스) screen vào đối tượng (object / 객체)/phạm vi (scope / 범위) thay vì top-level toàn cục (global / 전역) để engine có thể dọn khi screen unload.

Nhưng nếu một toàn cục (global / 전역) bộ nhớ đệm (cache / 캐시) giữ tham chiếu (reference / 참조) tới child phạm vi (scope / 범위):

```javascript
window.lastDetailScope = $p.getWindow("detailFrame");
```

thì page unload không đảm bảo đối tượng (object / 객체) đồ thị (graph / 그래프) được garbage collect vì vẫn còn reachable từ toàn cục (global / 전역) gốc (root / 루트).

Garbage collection tuân theo reachability, không theo ý định nhà phát triển (developer / 개발자).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **15. phạm vi (scope / 범위) giúp cleanup nhưng không cứu được tham chiếu (reference / 참조) toàn cục (global / 전역)** nêu điều cần giải thích; **16. tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) phải có đơn vị sở hữu (owner / 오너)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **17. Timer leak trong SPA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) phải có đơn vị sở hữu (owner / 오너)

Bất kỳ tài nguyên (resource / 자원) nào sống qua thời gian đều cần đơn vị sở hữu (owner / 오너):

```text
timer
interval
event listener
observer
cached scope
pending request
large DataList
popup/window reference
```

Hỏi hai câu:

```text
Ai tạo nó?
Ai giải phóng/hủy nó?
```

Nếu câu thứ hai không có đáp án, leak rủi ro (risk / 위험) cao.

> **Chuyển mạch:** Trong **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **16. tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) phải có đơn vị sở hữu (owner / 오너)** nêu điều cần giải thích; **17. Timer leak trong SPA** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **18. sự kiện (event / 이벤트) listener leak** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Timer leak trong SPA

Ví dụ:

```javascript
scwin.timer = setInterval(scwin.refresh, 30000);
```

Nếu page đóng mà interval không clear, callback vẫn có thể giữ `scwin`, DataCollection và closure reachable.

Cleanup:

```javascript
clearInterval(scwin.timer);
scwin.timer = null;
```

Tên vòng đời (lifecycle / 생명주기) callback unload cụ thể phải kiểm tra theo dự án (project / 프로젝트)/bản dựng (build / 빌드). mô hình tư duy (mental model / 사고 모델) là cleanup cùng quyền sở hữu (ownership / 소유권) ranh giới (boundary / 경계).

> **Chuyển mạch:** Ở chặng này của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **18. sự kiện (event / 이벤트) listener leak** tiếp nhận điểm tựa từ **17. Timer leak trong SPA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Pending Submission khi page đóng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. sự kiện (event / 이벤트) listener leak

Listener gắn trực tiếp lên đối tượng (object / 객체) sống lâu như `window`/`document` đặc biệt nguy hiểm.

```javascript
window.addEventListener("resize", scwin.onResize);
```

Page đóng nhưng `window` vẫn sống. Nếu không remove listener, hàm (function / 함수) tham chiếu (reference / 참조) giữ page trạng thái (state / 상태).

Ưu tiên sự kiện (event / 이벤트) API/thành phần (component / 컴포넌트) vòng đời (lifecycle / 생명주기) của WebSquare khi có thể; nếu tự đăng ký trình duyệt (browser / 브라우저) sự kiện (event / 이벤트), tự unregister.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **19. Pending Submission khi page đóng** tiếp nhận điểm tựa từ **18. sự kiện (event / 이벤트) listener leak** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. yêu cầu (request / 요청) generation/đơn vị từ (token / 토큰)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Pending Submission khi page đóng

Một yêu cầu (request / 요청) có thể còn đang chạy khi người dùng (user / 사용자) đổi tab/đóng popup. Khi phản hồi (response / 응답) về, callback có thể cố cập nhật (update / 업데이트) page không còn active.

Có ba chiến lược (strategy / 전략) tùy nghiệp vụ (business / 비즈니스):

```text
abort request nếu không còn giá trị
ignore stale result bằng token/version
apply result vào shared owner nếu owner vẫn sống
```

Không nên để callback mù quáng chạm thành phần (component / 컴포넌트) cũ.

> **Chuyển mạch:** Trong **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **20. yêu cầu (request / 요청) generation/đơn vị từ (token / 토큰)** tiếp nhận điểm tựa từ **19. Pending Submission khi page đóng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Debounce và latest-intent** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. yêu cầu (request / 요청) generation/đơn vị từ (token / 토큰)

Một mẫu (pattern / 패턴) chống stale phản hồi (response / 응답):

```javascript
scwin.searchVersion = 0;

scwin.search = function () {
    scwin.searchVersion += 1;
    var myVersion = scwin.searchVersion;
    // execute request; trong callback chỉ apply nếu myVersion còn current
};
```

Với Submission đối tượng (object / 객체) cụ thể, hiện thực (implementation / 구현) callback cần phù hợp API dự án (project / 프로젝트). mô hình tư duy (mental model / 사고 모델) là **kết quả (result / 결과) chỉ hợp lệ với generation đã tạo nó**.

> **Chuyển mạch:** Ở chặng này của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **21. Debounce và latest-intent** tiếp nhận điểm tựa từ **20. yêu cầu (request / 요청) generation/đơn vị từ (token / 토큰)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Lazy script và thực thi (execution / 실행) thứ tự (ordering / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Debounce và latest-intent

Autocomplete/search-as-you-type có thể phát nhiều yêu cầu (request / 요청). Nếu yêu cầu (request / 요청) cũ về sau yêu cầu (request / 요청) mới, UI có thể hiển thị kết quả cũ.

Hai tầng (layer / 계층) giải quyết khác nhau:

```text
debounce → giảm số request
latest-intent guard → ngăn stale response ghi đè state mới
```

Chỉ debounce không loại bỏ race hoàn toàn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **22. Lazy script và thực thi (execution / 실행) thứ tự (ordering / 순서)** tiếp nhận điểm tựa từ **21. Debounce và latest-intent** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. scriptLoading.merge và khả năng quan sát (observability / 관측 가능성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Lazy script và thực thi (execution / 실행) thứ tự (ordering / 순서)

WebSquare/WFrame cấu hình (config / 설정) có các option liên quan lazy script, sync chế độ (mode / 모드) và phạm vi (scope / 범위). Official WFrame guide lưu ý một số cấu hình `mode="sync"`, `scope="true"` để bảo đảm hành vi (behavior / 동작)/thực thi (execution / 실행) thứ tự (order / 순서) trong multi-WFrame kiến trúc (architecture / 아키텍처) của các generation tương ứng.

Không bản sao (copy / 복사) cấu hình (config / 설정) từ dự án (project / 프로젝트) khác mà không hiểu bản dựng (build / 빌드). Một cấu hình (config / 설정) từng là workaround ở SP cũ có thể không còn là recommendation hiện tại.

> **Chuyển mạch:** Trong **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **23. scriptLoading.merge và khả năng quan sát (observability / 관측 가능성)** tiếp nhận điểm tựa từ **22. Lazy script và thực thi (execution / 실행) thứ tự (ordering / 순서)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. W-Pack và bộ nhớ đệm (cache / 캐시) tạo nhiều sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. `scriptLoading.merge` và khả năng quan sát (observability / 관측 가능성)

Máy khách (client / 클라이언트) cấu hình (config / 설정) có option liên quan cách script WFrame/PageInherit được eval/merge. Các tối ưu hóa (optimization / 최적화) kiểu merge có thể thay đổi dấu vết ngăn xếp (stack trace / 스택 트레이스)/nguồn (source / 소스) visibility và timing.

Khi gỡ lỗi (debug / 디버그) issue chỉ môi trường vận hành (production / 운영 환경) xảy ra, hãy so sánh cấu hình (config / 설정) dev/prod trước khi kết luận mã nguồn (source code / 소스 코드) khác.

> **Chuyển mạch:** Ở chặng này của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **24. W-Pack và bộ nhớ đệm (cache / 캐시) tạo nhiều sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자)** tiếp nhận điểm tựa từ **23. scriptLoading.merge và khả năng quan sát (observability / 관측 가능성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Page reload không đồng nghĩa engine reload** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. W-Pack và bộ nhớ đệm (cache / 캐시) tạo nhiều sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자)

Có thể tồn tại:

```text
XML source trong repository
W-Pack generated JS
artifact trong deploy package
browser/CDN cached artifact
runtime object hiện tại
```

Nếu nhà phát triển (developer / 개발자) sửa XML nhưng trình duyệt (browser / 브라우저) vẫn chạy JS cũ, nhìn nguồn (source / 소스) repo không đủ chứng minh thời gian chạy (runtime / 런타임) mã (code / 코드).

Gỡ lỗi (debug / 디버그) môi trường vận hành (production / 운영 환경) phải xác định sản phẩm tạo ra (artifact / 산출물) thật được tải qua mạng (network / 네트워크)/bản đồ mã nguồn (source map / 소스 맵)/băm (hash / 해시)/bản dựng (build / 빌드) siêu dữ liệu (metadata / 메타데이터).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **25. Page reload không đồng nghĩa engine reload** tiếp nhận điểm tựa từ **24. W-Pack và bộ nhớ đệm (cache / 캐시) tạo nhiều sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Tab caching và stale trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Page reload không đồng nghĩa engine reload

Trong SPA, thay WFrame `src` có thể tạo page instance mới trong cùng engine shell. toàn cục (global / 전역) engine/dùng chung (common / 공통) trạng thái (state / 상태) vẫn còn.

Do đó bug “reload page con là hết” có thể khác “reload trình duyệt (browser / 브라우저) là hết”. Đây là clue quan trọng:

```text
Nếu browser reload mới fix → nghi global/common/cache/lifetime state.
Nếu đổi page con fix → nghi page-local state.
```

> **Chuyển mạch:** Trong **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **26. Tab caching và stale trạng thái (state / 상태)** tiếp nhận điểm tựa từ **25. Page reload không đồng nghĩa engine reload** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Warm bộ nhớ đệm (cache / 캐시) che hiệu năng (performance / 성능) bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Tab caching và stale trạng thái (state / 상태)

Một tab đã mở có thể được giữ lại thay vì destroy/recreate tùy bộ chứa (container / 컨테이너)/cấu hình (config / 설정). Khi người dùng (user / 사용자) quay lại, `onpageload` có thể không chạy lại như nhà phát triển (developer / 개발자) tưởng.

Nên phân biệt:

```text
first creation
activation
refresh
re-entry
close/destroy
```

Nếu nghiệp vụ (business / 비즈니스) cần refresh mỗi lần active, gắn vào activation đặc tả hợp đồng (contract / 계약), không dựa vào creation callback.

> **Chuyển mạch:** Ở chặng này của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **27. Warm bộ nhớ đệm (cache / 캐시) che hiệu năng (performance / 성능) bài toán (problem / 문제)** tiếp nhận điểm tựa từ **26. Tab caching và stale trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. bộ nhớ (memory / 메모리) kiểm thử (test / 테스트) cần lặp vòng đời (lifecycle / 생명주기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Warm bộ nhớ đệm (cache / 캐시) che hiệu năng (performance / 성능) bài toán (problem / 문제)

Development thường kiểm thử (test / 테스트) lần thứ hai khi trình duyệt (browser / 브라우저) đã bộ nhớ đệm (cache / 캐시) script và API dữ liệu (data / 데이터) nhỏ. người dùng (user / 사용자) first visit có cold bộ nhớ đệm (cache / 캐시).

Hiệu năng (performance / 성능) kiểm thử (test / 테스트) nên có:

```text
cold load
warm load
slow network simulation khi phù hợp
realistic row count
repeated navigation 20–50 lần
```

Một screen chỉ nhanh ở warm bộ nhớ đệm (cache / 캐시) chưa đủ production-ready.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **27. Warm bộ nhớ đệm (cache / 캐시) che hiệu năng (performance / 성능) bài toán (problem / 문제)** xác định đầu vào; **28. bộ nhớ (memory / 메모리) kiểm thử (test / 테스트) cần lặp vòng đời (lifecycle / 생명주기)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **29. hiệu năng (performance / 성능) ngân sách (budget / 예산) theo screen** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. bộ nhớ (memory / 메모리) kiểm thử (test / 테스트) cần lặp vòng đời (lifecycle / 생명주기)

Vùng nhớ vùng nhớ động (heap / 힙) snapshot một lần khó chứng minh leak. kiểm thử (test / 테스트) tốt:

```text
baseline heap
open screen
perform representative actions
close screen
force/allow GC khi tooling hỗ trợ
repeat N lần
compare retained objects
```

Nếu retained phạm vi (scope / 범위)/listener/count tăng gần tuyến tính theo lần mở, hypothesis leak mạnh hơn.

> **Chuyển mạch:** Trong **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **28. bộ nhớ (memory / 메모리) kiểm thử (test / 테스트) cần lặp vòng đời (lifecycle / 생명주기)** xác định đầu vào; **29. hiệu năng (performance / 성능) ngân sách (budget / 예산) theo screen** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **30. Không optimize bằng private engine API** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. hiệu năng (performance / 성능) ngân sách (budget / 예산) theo screen

Thay vì “màn hình phải nhanh”, đặt ngân sách (budget / 예산) có thể đo:

```text
initial payload
first interactive time
search response + render
maximum practical row count
heap growth after 30 navigation cycles
```

Con số cụ thể phụ thuộc sản phẩm (product / 제품)/thiết bị (device / 장치)/mạng (network / 네트워크). Giá trị của ngân sách (budget / 예산) là tạo regression tín hiệu (signal / 신호).

> **Chuyển mạch:** Ở chặng này của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **30. Không optimize bằng private engine API** tiếp nhận điểm tựa từ **29. hiệu năng (performance / 성능) ngân sách (budget / 예산) theo screen** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. kết xuất (render / 렌더링) storm do sự kiện (event / 이벤트)/binding chuỗi (chain / 사슬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Không optimize bằng private engine API

Official hiệu năng (performance / 성능) guide khuyến nghị dùng công khai (public / 공개) thành phần (component / 컴포넌트) API/sự kiện (event / 이벤트). API nhìn thấy trong DevTools nhưng không có trong docs có thể thay đổi giữa bản dựng (build / 빌드).

Một private phương thức (method / 메서드) nhanh hơn 20% hôm nay có thể tạo upgrade blocker ngày mai.

Tối ưu bền vững ưu tiên:

```text
ít data hơn
ít render hơn
đúng lifecycle
ít duplicate work
public API
```

trước micro-hack internals.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **30. Không optimize bằng private engine API** xác định đầu vào; **31. kết xuất (render / 렌더링) storm do sự kiện (event / 이벤트)/binding chuỗi (chain / 사슬)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **32. Batch mutation khi API hỗ trợ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. kết xuất (render / 렌더링) storm do sự kiện (event / 이벤트)/binding chuỗi (chain / 사슬)

Một người dùng (user / 사용자) hành động (action / 동작) có thể:

```text
set model
→ binding update component
→ onchange handler
→ handler set model khác
→ Grid refresh
→ computed state update
```

Nếu handler viết thiếu guard, sự kiện (event / 이벤트) chuỗi (chain / 사슬) có thể lặp hoặc redraw nhiều lần.

Khi profile thấy scripting/kết xuất (render / 렌더링) spike, vẽ chuỗi nhân quả (causal chain / 인과 사슬) của trạng thái (state / 상태) mutation thay vì tối ưu từng hàm (function / 함수) độc lập.

> **Chuyển mạch:** Trong **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **31. kết xuất (render / 렌더링) storm do sự kiện (event / 이벤트)/binding chuỗi (chain / 사슬)** xác định đầu vào; **32. Batch mutation khi API hỗ trợ** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **33. Hidden UI vẫn có thể có chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Batch mutation khi API hỗ trợ

Nếu cần cập nhật (update / 업데이트) nhiều row/cell, gọi cập nhật (update / 업데이트) + redraw mỗi iteration có thể tốn hơn batch thay đổi (change / 변경) rồi redraw/refresh một lần. API cụ thể phụ thuộc DataList/Grid bản dựng (build / 빌드).

Mô hình tư duy (mental model / 사고 모델):

```text
N mutations × N render notifications
```

thường đắt hơn:

```text
N model mutations + 1 render synchronization
```

Nhưng không dùng undocumented suspend-render hack; kiểm tra API công khai (public API / 공개 API).

> **Chuyển mạch:** Ở chặng này của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **33. Hidden UI vẫn có thể có chi phí (cost / 비용)** tiếp nhận điểm tựa từ **32. Batch mutation khi API hỗ trợ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. trường hợp (case / 사례) study: dashboard 12 tab** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Hidden UI vẫn có thể có chi phí (cost / 비용)

`display:none` hoặc tab chưa visible không nhất thiết nghĩa thành phần (component / 컴포넌트) chưa được instantiate hoặc dữ liệu (data / 데이터) không tải (load / 로드). chi phí (cost / 비용) phụ thuộc vòng đời (lifecycle / 생명주기)/kết xuất (render / 렌더링) chiến lược (strategy / 전략).

Đừng tối ưu bằng cách “ẩn” 20 Grid rồi nghĩ startup nhẹ đi. Đo mạng (network / 네트워크), đối tượng (object / 객체) creation và DOM.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **33. Hidden UI vẫn có thể có chi phí (cost / 비용)** cho ta quy tắc; **34. trường hợp (case / 사례) study: dashboard 12 tab** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **35. trường hợp (case / 사례) study: child đối tượng (object / 객체) tồn tại nhưng phương thức (method / 메서드) lỗi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. trường hợp (case / 사례) study: dashboard 12 tab

Giả sử dashboard có 12 tab, mỗi tab một WFrame và 3 Grid. Với `alwaysDraw=true`, startup có thể tải/kết xuất (render / 렌더링) mọi tab và phát hàng chục yêu cầu (request / 요청). người dùng (user / 사용자) thường chỉ dùng 2–3 tab.

Một kiến trúc (architecture / 아키텍처) tốt hơn có thể:

```text
render tab đầu
lazy load tab khác
preload một tab có xác suất sử dụng cao nếu network latency đáng kể
load tab-specific data khi activation lần đầu
cache data có TTL nếu business cho phép
cleanup listener/timer khi tab destroy
```

Nhưng nếu tab B cung cấp dữ liệu (data / 데이터) bắt buộc cho header chung, dữ liệu (data / 데이터) đó phải chuyển lên đơn vị sở hữu (owner / 오너) chung thay vì trông chờ tab B lazy chạy.

> **Chuyển mạch:** Trong **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **34. trường hợp (case / 사례) study: dashboard 12 tab** cho ta quy tắc; **35. trường hợp (case / 사례) study: child đối tượng (object / 객체) tồn tại nhưng phương thức (method / 메서드) lỗi** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **36. vòng đời (lifecycle / 생명주기) máy trạng thái (state machine / 상태 머신) nên nghĩ thế nào** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. trường hợp (case / 사례) study: child đối tượng (object / 객체) tồn tại nhưng phương thức (method / 메서드) lỗi

Với preload, `scwin` child có thể tồn tại. Parent gọi `child.scwin.calculate()` thành công nếu hàm (function / 함수) chỉ dùng DataMap. Sau đó refactor hàm (function / 함수) thêm `grid1.redraw()` và bắt đầu lỗi trước khi tab kết xuất (render / 렌더링).

Nguyên nhân gốc (root cause / 근본 원인) không phải “Grid API flaky”. đặc tả hợp đồng (contract / 계약) của hàm (function / 함수) đã thay đổi từ data-ready sang render-ready nhưng caller không biết.

Fix tốt là tách hàm (function / 함수) hoặc encode readiness yêu cầu (requirement / 요구사항) rõ.

> **Chuyển mạch:** Ở chặng này của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **35. trường hợp (case / 사례) study: child đối tượng (object / 객체) tồn tại nhưng phương thức (method / 메서드) lỗi** cho ta quy tắc; **36. vòng đời (lifecycle / 생명주기) máy trạng thái (state machine / 상태 머신) nên nghĩ thế nào** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **37. môi trường vận hành (production / 운영 환경) debugging thứ tự (order / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. vòng đời (lifecycle / 생명주기) máy trạng thái (state machine / 상태 머신) nên nghĩ thế nào

Một screen phức tạp có thể lập luận (reasoning / 추론) như máy trạng thái (state machine / 상태 머신):

```text
CREATED
→ MODEL_READY
→ VIEW_READY
→ ACTIVE
→ DATA_LOADING
→ READY
→ CLOSING
→ DISPOSED
```

Không nhất thiết implement enum thật. Nhưng khi bug timing xảy ra, xác định thao tác (operation / 연산) hợp lệ ở trạng thái (state / 상태) nào giúp tìm lỗi nhanh hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **36. vòng đời (lifecycle / 생명주기) máy trạng thái (state machine / 상태 머신) nên nghĩ thế nào** xác định đầu vào; **37. môi trường vận hành (production / 운영 환경) debugging thứ tự (order / 순서)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **38. liên kết (connection / 연결) với chapter khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. môi trường vận hành (production / 운영 환경) debugging thứ tự (order / 순서)

Khi “tab đôi lúc trắng”, kiểm tra theo thứ tự:

```text
content source đã request chưa?
HTTP/resource load có success không?
script exception có xảy ra không?
scope/window có tồn tại không?
component đã render chưa?
onpageload/activation có chạy không?
initial Submission có pending/fail không?
CSS/layout có làm nội dung invisible không?
```

Mỗi bước có bằng chứng (evidence / 증거) khác nhau. Không bắt đầu bằng random `redraw()`.

> **Chuyển mạch:** Trong **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **38. liên kết (connection / 연결) với chapter khác** tiếp nhận điểm tựa từ **37. môi trường vận hành (production / 운영 환경) debugging thứ tự (order / 순서)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nguồn chính thức nên đối chiếu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. liên kết (connection / 연결) với chapter khác

Phạm vi (scope / 범위)/WFrame topology: [04 — Scope, WFrame, Popup & SPA](04_scope_wframe_popup_spa.md).

Grid rendering và large dataset: [05 — GridView, CRUD & Enterprise Screen Patterns](05_gridview_crud_patterns.md).

Bộ nhớ (memory / 메모리)/bằng chứng hiệu năng (performance evidence / 성능 증거): [06 — Debugging, Performance, Security & Production](06_debugging_performance_security.md).

Reusable UDC/động (dynamic / 동적) thành phần (component / 컴포넌트) quyền sở hữu (ownership / 소유권): [08 — Reusable Architecture, UDC & Common Modules](08_reusable_architecture_udc_common_modules.md).

> **Chuyển mạch:** Ở chặng này của **10 — Rendering, Lazy Loading & tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)**, **38. liên kết (connection / 연결) với chapter khác** đã nêu tiêu chí phân biệt, còn **Nguồn chính thức nên đối chiếu** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Nguồn chính thức nên đối chiếu

WebSquare5 SP5 — TabControl tab content rendering guide: `https://docs1.inswave.com/sp5_user_guide/e0b2630fe498ead7`

WebSquare5 SP5 — hiệu năng (performance / 성능) guide: `https://docs1.inswave.com/sp5_user_guide/5f4b3b7ceca5e65b`

WebSquare5 SP5 — WFrame/phạm vi (scope / 범위) guide: `https://docs1.inswave.com/sp5_user_guide/4b5b013547991bdf`

WebSquare5 SP5 — máy khách (client / 클라이언트).cấu hình (config / 설정).xml: `https://docs1.inswave.com/sp5_user_guide/db5edae0d31101bd`

Các hành vi (behavior / 동작) vòng đời (lifecycle / 생명주기)/cấu hình (config / 설정) cụ thể phải được xác minh theo chính xác (exact / 정확한) engine bản dựng (build / 빌드) của dự án (project / 프로젝트).

> **Bàn giao:** Sau **Nguồn chính thức nên đối chiếu**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
