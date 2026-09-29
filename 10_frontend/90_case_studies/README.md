# Frontend Trường hợp (case / 사례) Studies — Trình duyệt (browser / 브라우저) Dấu vết (trace / 추적) & Bằng chứng vận hành (production evidence / 운영 증거)

Folder này không thêm một khung phần mềm (framework / 프레임워크) mới. Nó dùng các trường hợp (case / 사례) xuyên nhiều đơn vị sở hữu (owner / 오너) để kiểm tra xem người đọc có thật sự nối được Nền tảng Web (web platform / 웹 플랫폼) thành một hệ thống hay chỉ biết từng chapter riêng lẻ.

Chuẩn gốc (canonical / 정본) lý thuyết (theory / 이론) vẫn nằm ở các nhánh học (track / 트랙) HTML, CSS, JavaScript, React, WebSquare, XML và các lĩnh vực (domain / 도메인) lân cận. Trường hợp (case / 사례) study chỉ có vai trò bắt người đọc đi qua ranh giới (boundary / 경계):

```text
request
→ response
→ parser
→ DOM / CSSOM
→ style
→ layout
→ paint / composite
→ JavaScript scheduling
→ interaction
→ state
→ network
→ artifact / deployment evidence
```

## 00 — Yêu cầu (request / 요청) → Điểm ảnh (pixel / 픽셀) → Tương tác (interaction / 상호작용) Dấu vết (trace / 추적)

[00_REQUEST_TO_PIXEL_AND_INTERACTION_TRACE.md](./00_REQUEST_TO_PIXEL_AND_INTERACTION_TRACE.md)

Trường hợp (case / 사례) này lấy một màn hình web tưởng như đơn giản — mở danh sách, tải dữ liệu, bấm lọc, mở modal — rồi dấu vết (trace / 추적) từ URL cho tới điểm ảnh (pixel / 픽셀) và tương tác (interaction / 상호작용). Trọng tâm không phải thuộc chuỗi xử lý (pipeline / 파이프라인), mà là biết **đơn vị sở hữu (owner / 오너) nào tạo ra trạng thái (state / 상태) nào, công việc (work / 작업) xảy ra lúc nào, bằng chứng (evidence / 증거) nào chứng minh nguyên nhân và thất bại (failure / 실패) có thể nằm ở ranh giới (boundary / 경계) nào**.

## 01 — Rendering Hiệu năng (performance / 성능) Đo lường (measurement / 측정) Lab

[01_RENDERING_PERFORMANCE_MEASUREMENT_LAB.md](./01_RENDERING_PERFORMANCE_MEASUREMENT_LAB.md)

Lab này xử lý gap `paint/composite` trong coverage kiểm tra (audit / 감사). Người học phải tạo baseline, bản ghi (record / 레코드) dấu vết (trace / 추적), phân biệt scripting/style/bố cục (layout / 레이아웃)/paint/composite, xác định vô hiệu hóa (invalidation / 무효화) và thử một thay đổi duy nhất trước khi kết luận. Mục tiêu là thay câu “thuộc tính (property / 속성) này GPU-accelerated nên nhanh” bằng một quy trình đo được và reproducible.

## Cách dùng

Không đọc trường hợp (case / 사례) như lời giải cố định. Trước mỗi phần, hãy tự viết hypothesis và expected bằng chứng (evidence / 증거). Sau đó mới so với luồng (flow / 흐름) trong tài liệu.

Một trường hợp (case / 사례) được xem là hoàn thành khi có thể tạo sản phẩm tạo ra (artifact / 산출물):

```text
request / network timeline
DOM + style ownership map
main-thread / rendering trace
state + async ordering diagram
failure-mode table
before/after measurement
source → build → deployed artifact evidence
```

Nếu chỉ kết luận “React kết xuất (render / 렌더링) nhiều” hoặc “CSS gây reflow” mà không chỉ ra sự kiện (event / 이벤트), vô hiệu hóa (invalidation / 무효화), timing và dấu vết (trace / 추적) tương ứng thì chưa đạt.
