# WebSquare Glossary & Coverage Audit

File này có hai vai trò. Phần đầu là glossary để nhận diện thuật ngữ Việt–Anh–Hàn và tên API thường xuất hiện trong codebase. Phần sau là coverage audit để kiểm tra bạn đã hiểu library theo mental model hay chỉ mới nhớ syntax.

## 1. Glossary cốt lõi

| Tiếng Việt | English term | 한국어 용어 | Ý nghĩa trong WebSquare |
|---|---|---|---|
| nền tảng giao diện web doanh nghiệp | enterprise web UI platform | 엔터프라이즈 웹 UI 플랫폼 | Runtime/tooling/component/data abstraction để xây màn hình nghiệp vụ. |
| bộ máy chạy | engine/runtime | 엔진/런타임 | WebSquare Engine tạo page, component, Scope, binding và communication behavior trong browser. |
| trang | page | 화면/페이지 | Đơn vị màn hình WebSquare, thường author bằng XML và chứa script/data/UI. |
| phạm vi hiệu lực | scope | 유효 범위/스코프 | Boundary xác định component/function nào thuộc một page instance. |
| biến phạm vi trang | scope variable | 스코프 변수 | Biến đại diện behavior của page; thường là `scwin`. |
| thành phần giao diện | UI component | UI 컴포넌트 | Input, Button, GridView, WFrame, TabControl... do engine quản lý. |
| mô hình dữ liệu phía client | client data model | 클라이언트 데이터 모델 | DataCollection nằm trong browser memory. |
| đối tượng một bản ghi | DataMap | 데이터맵 | Key/value model cho form, condition hoặc record. |
| đối tượng nhiều dòng | DataList | 데이터리스트 | Table-like client data model có row/column/status. |
| danh sách liên kết | LinkedDataList | 링크드 데이터리스트 | View filter/sort dựa trên DataList. |
| trạng thái dòng | row status | 행 상태 | Metadata như R/U/C/D/V biểu diễn lifecycle thay đổi của row. |
| liên kết dữ liệu | data binding | 데이터 바인딩 | Nối component với DataCollection để đồng bộ value/model. |
| gửi nhận dữ liệu | submission | 서브미션/데이터 통신 | Object mô tả request/response mapping và server communication. |
| dữ liệu gửi | reference | 요청 데이터 참조 | DataCollection/data path được Submission serialize gửi server. |
| dữ liệu nhận | target | 응답 대상 | DataCollection/data path nhận response. |
| khung trang | WFrame | WFrame | Primitive để nhúng page, tạo Scope và hỗ trợ SPA composition. |
| ứng dụng một trang | Single Page Application (SPA) | 단일 페이지 애플리케이션 | Giữ engine shell và thay content page/frame mà không reload toàn ứng dụng. |
| cửa sổ bật lên | popup | 팝업 | Page/window tạm thời với input/output contract riêng. |
| vòng đời | lifecycle | 생명주기 | Trình tự load script, tạo component, render, event, unload/cleanup. |
| trạng thái nguồn chuẩn | source of truth | 단일 진실 공급원 | Nơi canonical state được giữ để tránh duplicate state. |
| bất biến | invariant | 불변 조건 | Điều luôn phải đúng, ví dụ unique key hoặc authorization. |
| điều kiện tranh chấp | race condition | 경쟁 상태 | Kết quả phụ thuộc thứ tự timing của nhiều async operation. |
| tính lũy đẳng | idempotency | 멱등성 | Retry cùng request không tạo thêm side effect ngoài ý muốn. |
| bằng chứng vận hành | production evidence | 운영 증거 | Network trace, log, metric, stack, heap, timing dùng để kiểm chứng giả thuyết. |
| nợ tương thích | compatibility debt | 호환성 부채 | Workaround/API cũ còn tồn tại vì generation/browser/project legacy. |

## 2. Identifier/API cần nhận diện

`scwin` — page/scope namespace thường chứa event handler và function nghiệp vụ của màn hình.

`$p` — WebSquare utility có page/scope context. Các API như `parent()`, `top()`, `main()`, `openPopup()`, `executeSubmission()` thường xuất hiện qua `$p` tùy version/build.

`$w` — utility style xuất hiện nhiều trong code WebSquare cũ/non-Scope. Không blind-replace bằng `$p`; phải hiểu execution context.

`DataMap` — model dạng key/value.

`DataList` — model dạng nhiều row, có API như `getRowCount()`, `getCellData()`, `getRowJSON()`, `getRowStatus()` ở SP5.

`LinkedDataList` — derived/filter/sort view của DataList.

`Submission` — communication object nối DataCollection với HTTP/server.

`GridView` — view component cho table data, thường bind DataList.

`WFrame` — page composition + Scope primitive.

`WindowContainer`, `TabControl` — container có thể quản lý nhiều page/window/tab và Scope relationship.

`dataObject` — parameter object dùng khi tạo WFrame/popup ở các API tương ứng; nên chứa JSON-serializable plain data.

`setSrc()` — thay source page của WFrame/page container tương ứng; operation có lifecycle, không nên giả định child sẵn sàng ngay sau call.

`getParameter()` — đọc parameter được truyền vào page theo contract tương ứng.

`W-Pack` — cơ chế build/chuyển page source XML sang JavaScript artifact trong WebSquare5.

## 3. Những cặp khái niệm dễ nhầm

### Component object vs DOM element

Component object là public framework abstraction. DOM element là representation bên dưới. Không đồng nhất hai thứ.

### Logical ID vs DOM ID

Logical component ID là ID developer dùng trong Scope. Physical DOM ID có thể được engine biến đổi, đặc biệt khi WFrame/Scope tạo nhiều instance.

### GridView vs DataList

GridView hiển thị và xử lý interaction. DataList giữ dữ liệu và row status.

### UI validation vs server validation

UI validation cải thiện UX. Server validation bảo vệ invariant và trust boundary.

### hidden/readOnly vs authorization

Property UI không tạo security boundary. Authorization phải ở server.

### HTTP success vs business success

HTTP 200 chỉ chứng minh transport/application endpoint trả response. Business operation vẫn có thể fail.

### row index vs business identity

Index là vị trí có thể đổi khi sort/filter. Business key mới là identity ổn định.

### popup/frame input vs shared global state

Parameter/data contract dễ reasoning và reuse hơn global mutable state.

### sync function call vs async business operation

Gọi function giữa scope có thể synchronous, nhưng function có thể bắt đầu network/frame load asynchronous.

### source XML vs runtime JavaScript artifact

XML là authoring source; runtime có thể dùng JS artifact do W-Pack tạo.

## 4. Coverage audit — Foundation

Bạn đã đạt mức Foundation khi có thể giải thích bằng lời của mình, không nhìn note:

WebSquare giải quyết vấn đề gì mà browser + JavaScript thuần không tự chuẩn hóa cho enterprise screen?

Vì sao WebSquare không phải ngôn ngữ lập trình riêng?

Studio khác Engine thế nào?

Vì sao page XML có thể dẫn đến JavaScript runtime artifact?

Vì sao component không nên đồng nhất với DOM element?

`scwin` giải quyết collision gì?

`$p` cần page context để làm gì?

DataMap và DataList khác nhau theo data shape và use case nào?

Submission reference/target biểu diễn gì?

Nếu chưa trả lời rõ được các câu này, quay lại chapter 01–03.

## 5. Coverage audit — Intermediate

Bạn đạt mức Intermediate khi có thể reasoning một màn hình query/edit mà không dò API liên tục:

Khi user sửa Input bind DataMap, state nào thay đổi?

Khi Grid bind DataList, dữ liệu canonical phía client nằm ở đâu?

Row `R/U/C/D/V` biểu diễn state transition gì?

Tại sao deleted row có thể vẫn tồn tại trong model?

Tại sao code ngay sau `executeSubmission()` không được giả định response đã về?

Tại sao HTTP 200 chưa đủ để hiển thị “Save success”?

Tại sao server paging làm `getRowCount()` không đại diện total dataset?

Tại sao giữ selected row index lâu dài có thể sai?

## 6. Coverage audit — Scope & Architecture

Bạn đạt mức này khi có thể mở một app shell nhiều tab và vẽ được topology:

Page nào là parent/child?

Mỗi WFrame có Scope nào?

Hai page có cùng component ID vì sao không collision?

`parent()`, `main()`, `top()` có khác nhau về intent nào?

Khi nào nên dùng `getWindow()` thay vì chain nhiều `parent()`?

`dataObject` nên chứa loại dữ liệu gì và vì sao không nên chứa function/window/component instance?

Popup nên trả result contract thế nào để giảm coupling?

Vì sao `setSrc()` tạo lifecycle race nếu gọi child ngay sau đó?

## 7. Coverage audit — Senior Production

Bạn đạt mức Senior Production khi gặp incident và biết evidence cần lấy trước khi sửa:

Search chậm: bạn đo network, mapping hay rendering ở đâu?

Grid 50.000 row lag: làm sao phân biệt payload cost và renderer cost?

Screen càng mở lâu càng chậm: làm sao chứng minh timer/listener leak?

Save đôi lúc duplicate: evidence nào phân biệt double-click client và retry server?

Response 200 nhưng Grid rỗng: pipeline debug theo thứ tự nào?

Popup đôi lúc không tìm thấy child object: lifecycle hay Scope hypothesis nào cần test?

Tại sao readOnly/hidden field không bảo vệ role/permission?

Tại sao mutation request không nên auto-retry mù quáng?

W-Pack/cache có thể làm production chạy code khác source bạn vừa sửa như thế nào?

## 8. Coverage audit — Legacy & Migration

Bạn đạt mức migration-ready khi có thể phân loại code cũ:

Business invariant nào phải giữ?

IFrame isolation cũ khác WFrame Scope thế nào?

`window.parent` nên migrate sang page contract nào?

`$w` usage nào có thể chuyển `$p`, usage nào cần hiểu context trước?

jQuery/DOM hack nào đã có component API thay thế?

Callback string/eval có thể thay bằng result contract không?

Synchronous Submission migration sang async làm control flow thay đổi ở đâu?

Config/workaround nào là historical debt và evidence nào cho phép remove?

Engine upgrade cần regression areas nào?

## 9. Failure-mode matrix

| Triệu chứng | Hypothesis ưu tiên | Evidence đầu tiên |
|---|---|---|
| Click không làm gì | event/disabled/Scope | breakpoint handler |
| Request không chạy | validation/Submission/Scope | Network + handler log |
| Request 200, model rỗng | target/schema mapping | response body + DataList |
| Model có data, Grid rỗng | binding/filter/render | DataList state + Grid binding |
| Save gửi giá trị cũ | binding/commit timing/duplicate state | request payload + model value |
| Popup không gọi được parent | wrong Scope/topology | resolve parent scope |
| Data đúng nhưng screen lag | rendering/script cost | Performance trace |
| Screen chậm dần | leak/timer/listener | repeat test + heap/request count |
| Duplicate record | duplicate request/idempotency | Network + server trace |
| Chỉ production lỗi | config/build/cache drift | engine/config/artifact diff |

## 10. Internal knowledge connections

JavaScript execution, closure, event loop và Promise: [JavaScript Intermediate](../javascript/javascript_intermediate.md).

Browser/runtime performance, memory và security: [JavaScript Senior](../javascript/javascript_senior.md) và [JavaScript Master](../javascript/javascript_master_supplement_detailed.md).

XML tree, namespace, parsing và schema mindset: [XML track](../xml/xml_01_beginner_detailed.md).

Nếu backend là Java/Spring, transaction, authorization và API correctness không thuộc WebSquare. Hãy cross-reference canonical backend docs trong `10_backend/` thay vì đưa server semantics vào UI library.

## 11. Practical capstone

Library được coi là thực sự “học xong” khi bạn có thể tự dựng và giải thích một flow:

```text
Search form
→ dmSearch
→ sbmSearch
→ dlUser
→ GridView
→ edit rows
→ row status
→ validate changed rows
→ sbmSave
→ server result
→ refresh
→ popup detail trong WFrame/Scope
```

Sau đó phải debug được ba fault injection:

Server response chậm 5 giây.

User double-click Save.

Popup được mở/đóng 30 lần và có timer cố ý không cleanup.

Nếu bạn có thể chỉ ra failure mode, evidence và fix boundary cho cả ba case, kiến thức đã chuyển từ “biết API” sang “reasoning được hệ thống”.

## 12. Coverage status của library

Library hiện bao phủ các trục canonical cần thiết cho WebSquare JavaScript enterprise development: platform/runtime, page model, component API, events, binding, DataCollection, DataMap/DataList/LinkedDataList, row status, Submission, async communication, WFrame, Scope, `scwin`, `$p`, popup, SPA, GridView/CRUD, performance, memory, security, observability, legacy patterns và migration reasoning.

Những thứ cố ý **không** biến thành chapter riêng gồm danh sách toàn bộ property của từng component, exhaustive API reference, mọi option GridView, mọi config tag và mọi build release note. Các nội dung đó thay đổi theo engine build và đã có official reference. Library này ưu tiên mental model giúp bạn đọc reference đúng và áp dụng an toàn.
