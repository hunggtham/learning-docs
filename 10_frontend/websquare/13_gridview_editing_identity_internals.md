# 13 — GridView Editing, định danh (identity / 식별자) & View Internals

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **13 — GridView Editing, định danh (identity / 식별자) & View Internals**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Một cell có nhiều trạng thái hơn giá trị bạn nhìn thấy** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Edit vòng đời (lifecycle / 생명주기) là chuyển tiếp trạng thái (state transition / 상태 전이), không chỉ một sự kiện (event / 이벤트)** để giải thích cách điều kiện hoặc mục tiêu đó vận hành. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Chapter 05 đã xây mô hình tư duy (mental model / 사고 모델) `DataList = model`, `GridView = view + interaction`. Chapter này đi sâu hơn vào phần thường gây bug ở dự án (project / 프로젝트) thật: một cell đang edit chưa chắc đã lần ghi nhận (commit / 커밋) vào mô hình (model / 모델), chỉ mục (index / 인덱스) nhìn thấy chưa chắc là định danh (identity / 식별자) thật, sort/filter/group làm thay đổi view topology, selection không phải nghiệp vụ (business / 비즈니스) trạng thái (state / 상태), và một thao tác tưởng là “sửa một ô” có thể kích hoạt nhiều sự kiện (event / 이벤트), binding và redraw.

Mục tiêu không phải thuộc mọi thuộc tính (property / 속성) GridView. Mục tiêu là có thể nhìn một bug Grid và trả lời chính xác: **giá trị hiện nằm ở editor, Grid view hay DataList; row nào đang được nói tới; sự kiện (event / 이벤트) nào đã chạy; mutation đã lần ghi nhận (commit / 커밋) chưa; và thao tác (operation / 연산) tiếp theo đang dùng định danh (identity / 식별자) nào**.

## 1. Một cell có nhiều trạng thái hơn giá trị bạn nhìn thấy

Khi người dùng (user / 사용자) đang gõ trong một cell editable, có thể tồn tại đồng thời ba biểu diễn (representation / 표현):

```text
editor value đang nhập
        ↓ commit/edit lifecycle
GridView cell state
        ↓ binding/data propagation
DataList canonical client value
```

Trong nhiều tình huống ba giá trị nhanh chóng đồng bộ nên nhà phát triển (developer / 개발자) tưởng chúng luôn là một. Nhưng ở ranh giới (boundary / 경계) như Enter/Tab, click sang row khác, kiểm tra hợp lệ (validation / 검증) thất bại (fail / 실패), Save được click khi editor còn active hoặc script đổi giá trị (value / 값), timing trở nên quan trọng.

Vì vậy câu hỏi “Grid đang hiển thị gì?” khác với “DataList sẽ serialize gì nếu Submission chạy ngay bây giờ?”. Save luồng (flow / 흐름) môi trường vận hành (production / 운영 환경) phải đảm bảo edit hiện tại đã đi qua vòng đời (lifecycle / 생명주기) mà dự án (project / 프로젝트) mong đợi trước khi đọc mô hình (model / 모델).

> **Chuyển mạch:** Trong **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **1. Một cell có nhiều trạng thái hơn giá trị bạn nhìn thấy** xác định đầu vào; **2. Edit vòng đời (lifecycle / 생명주기) là chuyển tiếp trạng thái (state transition / 상태 전이), không chỉ một sự kiện (event / 이벤트)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **3. Before-change sự kiện (event / 이벤트) phù hợp để bảo vệ bất biến (invariant / 불변식) cục bộ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Edit vòng đời (lifecycle / 생명주기) là chuyển tiếp trạng thái (state transition / 상태 전이), không chỉ một sự kiện (event / 이벤트)

Một tương tác (interaction / 상호작용) điển hình có thể lập luận (reasoning / 추론) như sau:

```text
focus cell
→ enter edit mode
→ user changes editor value
→ before-change validation
→ model mutation accepted/rejected
→ row/cell status update
→ after-edit/view-change events
→ formatter/render refresh
```

Chính xác (exact / 정확한) sự kiện (event / 이벤트) name và thứ tự phụ thuộc engine bản dựng (build / 빌드), đầu vào (input / 입력) kiểu (type / 타입) và Grid cấu hình (configuration / 구성). SP5 từng bổ sung `viewChangeAfterEdit` để điều khiển quan hệ thứ tự giữa `onviewchange` và `onafteredit`; điều này là bằng chứng rằng sự kiện (event / 이벤트) thứ tự (ordering / 순서) là thời gian chạy (runtime / 런타임) đặc tả hợp đồng (contract / 계약) có phiên bản (version / 버전), không phải thứ nên đoán từ tên sự kiện (event / 이벤트).

Cấp cao (senior / 시니어) quy tắc (rule / 규칙): nếu lô-gic nghiệp vụ (business logic / 비즈니스 로직) phụ thuộc “sự kiện (event / 이벤트) A chắc chắn chạy trước sự kiện (event / 이벤트) B”, hãy kiểm chứng bằng tham chiếu (reference / 참조)/bản phát hành (release / 릴리스) ghi chú (note / 노트) đúng engine bản dựng (build / 빌드) và viết regression kiểm thử (test / 테스트) cho giả định (assumption / 가정) đó.

> **Chuyển mạch:** Ở chặng này của **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **2. Edit vòng đời (lifecycle / 생명주기) là chuyển tiếp trạng thái (state transition / 상태 전이), không chỉ một sự kiện (event / 이벤트)** xác định đầu vào; **3. Before-change sự kiện (event / 이벤트) phù hợp để bảo vệ bất biến (invariant / 불변식) cục bộ** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **4. Row position là tương tác (interaction / 상호작용) cursor, không phải định danh (identity / 식별자)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Before-change sự kiện (event / 이벤트) phù hợp để bảo vệ bất biến (invariant / 불변식) cục bộ

DataList có vòng đời (lifecycle / 생명주기) trước cell mutation, ví dụ `onbeforecelldatachange` trong SP5. Handler có thể từ chối thay đổi trong các scenario được hỗ trợ.

```javascript
scwin.dlOrder_onbeforecelldatachange = function (info) {
    if (info.colID === "QTY" && Number(info.newValue) < 0) {
        return false;
    }
};
```

Đây là nơi tốt cho bất biến (invariant / 불변식) rẻ, synchronous và hoàn toàn dựa vào máy khách (client / 클라이언트) trạng thái (state / 상태) hiện có. Nó không phải nơi tốt để gọi máy chủ (server / 서버) rồi chờ kết quả như một synchronous validator.

Nếu kiểm tra hợp lệ (validation / 검증) cần API, hãy tách thành workflow rõ: cho phép edit vào mô hình (model / 모델), đánh dấu trạng thái cần kiểm tra, chạy async kiểm tra hợp lệ (validation / 검증), rồi quyết định UX khi kết quả (result / 결과) về. Cố biến mạng (network / 네트워크) thành before-change synchronous đường dẫn (path / 경로) thường làm UI khó lập luận (reasoning / 추론).

> **Chuyển mạch:** Before-change event bảo vệ invariant trước khi commit; row position chỉ là cursor, vì vậy view index và model index tiếp theo phải có tên và mapping riêng.

## 4. Row position là tương tác (interaction / 상호작용) cursor, không phải định danh (identity / 식별자)

`rowPosition` trả lời “row nào đang active trong mô hình (model / 모델)/view ngữ cảnh (context / 맥락) hiện tại”. Nó hữu ích cho thao tác ngay tại thời điểm sự kiện (event / 이벤트), nhưng không phải khóa bền vững.

Một nghiệp vụ (business / 비즈니스) thực thể (entity / 엔터티) cần định danh (identity / 식별자) như:

```text
EMPLOYEE_ID
ORDER_ID
ACCOUNT_NO + EFFECTIVE_DATE
```

Nếu callback async giữ `rowIndex = 7`, rồi người dùng (user / 사용자) sort/filter/insert trước khi phản hồi (response / 응답) về, row 7 có thể đã là thực thể (entity / 엔터티) khác.

Mẫu (pattern / 패턴) an toàn hơn:

```javascript
var row = dlOrder.getRowPosition();
var orderId = dlOrder.getCellData(row, "ORDER_ID");

scwin.validateOrderAsync(orderId);
```

Khi phản hồi (response / 응답) về, resolve thực thể (entity / 엔터티) bằng nghiệp vụ (business / 비즈니스) key hoặc yêu cầu (request / 요청) định danh (identity / 식별자) thay vì tin chỉ mục (index / 인덱스) cũ.

> **Chuyển mạch:** Row position chỉ là cursor; tách view index khỏi model index để sort có thể đổi thứ tự hiển thị mà không đổi business identity.

## 5. View chỉ mục (index / 인덱스) và mô hình (model / 모델) chỉ mục (index / 인덱스) phải được phân biệt bằng tên biến

Trong Grid có sort/filter/group/paging, từ `index` một mình là quá mơ hồ. rà soát mã (code review / 코드 리뷰) nên yêu cầu tên thể hiện ngữ nghĩa (semantic / 의미적):

```text
viewRowIndex
modelRowIndex
realRowIndex
pageRowIndex
selectedViewIndex
```

Tên API chính xác (exact / 정확한) để convert giữa các loại chỉ mục (index / 인덱스) phụ thuộc Grid/DataList bản dựng (build / 빌드) và tính năng (feature / 기능) đang dùng. Điều quan trọng hơn là không truyền một integer qua nhiều hàm (function / 함수) mà mất siêu dữ liệu (metadata / 메타데이터) “integer này thuộc coordinate hệ thống (system / 시스템) nào”.

Đây giống bài toán coordinate hệ thống (system / 시스템) trong graphics: cùng số `5` nhưng `x=5` ở cục bộ (local / 로컬) coordinate không đồng nghĩa `x=5` ở world coordinate.

> **Chuyển mạch:** Sort chỉ đổi order của view; filter tiếp theo tạo subset view và phải giữ source data cùng identity mapping nguyên vẹn.

## 6. Sort thay đổi thứ tự (order / 순서), không thay nghiệp vụ (business / 비즈니스) định danh (identity / 식별자)

Khi người dùng (user / 사용자) sort theo `USER_NAME`, vị trí row đổi nhưng `USER_ID` không đổi. Nếu ứng dụng (application / 애플리케이션) giữ selection bằng nghiệp vụ (business / 비즈니스) key, nó có thể tái xác định thực thể (entity / 엔터티). Nếu giữ bằng chỉ mục (index / 인덱스), selection lô-gic (logic / 논리) có thể silently chuyển sang row khác.

Mô hình tư duy (mental model / 사고 모델):

```text
model entities: A B C
sort by name:  C A B

identity A vẫn là A
position của A đã đổi
```

Bất kỳ lô-gic (logic / 논리) dài-lived nào liên quan save kết quả (result / 결과), popup kết quả (result / 결과), async kiểm tra hợp lệ (validation / 검증) hoặc cross-page communication nên ưu tiên định danh (identity / 식별자) hơn position.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **6. Sort thay đổi thứ tự (order / 순서), không thay nghiệp vụ (business / 비즈니스) định danh (identity / 식별자)** nêu điều cần giải thích; **7. Filter tạo một view con, không xóa nguồn (source / 소스) dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. Grouping tạo presentation hierarchy, không tự tạo lĩnh vực (domain / 도메인) hierarchy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Filter tạo một view con, không xóa nguồn (source / 소스) dữ liệu (data / 데이터)

Filter thường làm một số row không còn visible nhưng nguồn (source / 소스) DataList vẫn có thể chứa chúng. Vì vậy:

```text
visible row count
≠ source row count
≠ changed row count
≠ server total count
```

Một nút “Save all changes” thường phải quan tâm changed rows trong mô hình (model / 모델), kể cả row hiện bị filter ẩn. Một nút “Export hiện tại (current / 현재) view” có thể lại cần visible rows. Hai thao tác (operation / 연산) có ngữ nghĩa (semantics / 의미론) khác nhau dù cùng nhìn một Grid.

Trước khi dùng count/chỉ mục (index / 인덱스) API, viết câu tiếng Việt trước: “Tôi muốn đếm/tác động tập row nào?”. Sau đó mới chọn API.

> **Chuyển mạch:** Trong **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **7. Filter tạo một view con, không xóa nguồn (source / 소스) dữ liệu (data / 데이터)** nêu điều cần giải thích; **8. Grouping tạo presentation hierarchy, không tự tạo lĩnh vực (domain / 도메인) hierarchy** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. Selection, check và focus là ba loại tương tác (interaction / 상호작용) trạng thái (state / 상태) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Grouping tạo presentation hierarchy, không tự tạo lĩnh vực (domain / 도메인) hierarchy

Grid grouping có thể hiển thị row theo phòng ban, trạng thái hoặc category. Group header/subtotal là presentation cấu trúc (structure / 구조). Đừng mặc định chúng là nghiệp vụ (business / 비즈니스) thực thể (entity / 엔터티) mới trong DataList.

Nếu máy chủ (server / 서버) cần hierarchy thật, đặc tả hợp đồng (contract / 계약) phải biểu diễn hierarchy rõ. Nếu chỉ Grid group theo `DEPT_CD`, save vẫn nên dựa nguồn (source / 소스) row định danh (identity / 식별자)/status chứ không dựa group header position.

> **Chuyển mạch:** Ở chặng này của **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **9. Selection, check và focus là ba loại tương tác (interaction / 상호작용) trạng thái (state / 상태) khác nhau** tiếp nhận điểm tựa từ **8. Grouping tạo presentation hierarchy, không tự tạo lĩnh vực (domain / 도메인) hierarchy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Programmatic thay đổi (change / 변경) và người dùng (user / 사용자) thay đổi (change / 변경) không nhất thiết phát cùng sự kiện (event / 이벤트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Selection, check và focus là ba loại tương tác (interaction / 상호작용) trạng thái (state / 상태) khác nhau

Một Grid có thể có focused cell, hiện tại (current / 현재) row, selected rows và checkbox selection. Chúng phục vụ UX khác nhau.

```text
focus → keyboard/edit cursor
current row → active record context
selection → user chọn một hoặc nhiều row
check column → có thể chỉ là UI selection hoặc business field
```

Bug phổ biến là dùng checkbox UI để persist `SELECTED_YN` dù nghiệp vụ (business / 비즈니스) không hề có khái niệm selected. Ngược lại, nếu checkbox thật sự là trường dữ liệu (field / 필드) nghiệp vụ như `APPROVED_YN`, nó phải nằm trong DataList và tham gia kiểm tra hợp lệ (validation / 검증)/save như dữ liệu (data / 데이터).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **10. Programmatic thay đổi (change / 변경) và người dùng (user / 사용자) thay đổi (change / 변경) không nhất thiết phát cùng sự kiện (event / 이벤트)** tiếp nhận điểm tựa từ **9. Selection, check và focus là ba loại tương tác (interaction / 상호작용) trạng thái (state / 상태) khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Bulk mutation cần một transaction-like máy khách (client / 클라이언트) ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Programmatic thay đổi (change / 변경) và người dùng (user / 사용자) thay đổi (change / 변경) không nhất thiết phát cùng sự kiện (event / 이벤트)

Một số thành phần (component / 컴포넌트)/sự kiện (event / 이벤트) chỉ phát khi người dùng (user / 사용자) tương tác (interaction / 상호작용) xảy ra, trong khi `setCellData()` hoặc binding cập nhật (update / 업데이트) bằng script có thể đi đường khác. Vì vậy nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) quan trọng không nên chỉ sống trong handler “người dùng (user / 사용자) changed cell”.

Ví dụ total phải luôn đúng sau cả Excel upload, API tải (load / 로드), bulk script cập nhật (update / 업데이트) và người dùng (user / 사용자) edit. Nếu total lô-gic (logic / 논리) chỉ nằm ở `onviewchange`, các đường dẫn (path / 경로) khác có thể bypass.

Tốt hơn là có hàm (function / 함수) lĩnh vực (domain / 도메인) rõ:

```javascript
scwin.recalculateTotal = function () {
    // đọc canonical DataList và tính lại
};
```

Các sự kiện (event / 이벤트)/đường dẫn (path / 경로) cần thiết gọi hàm (function / 함수) đó, hoặc máy chủ (server / 서버) trả chuẩn gốc (canonical / 정본) total nếu đó là đơn vị sở hữu (owner / 오너) phù hợp.

> **Chuyển mạch:** Trong **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **10. Programmatic thay đổi (change / 변경) và người dùng (user / 사용자) thay đổi (change / 변경) không nhất thiết phát cùng sự kiện (event / 이벤트)** đã nêu tiêu chí phân biệt, còn **11. Bulk mutation cần một transaction-like máy khách (client / 클라이언트) ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **12. Formatter là pure projection càng nhiều càng tốt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Bulk mutation cần một transaction-like máy khách (client / 클라이언트) ranh giới (boundary / 경계)

Giả sử người dùng (user / 사용자) chọn 2.000 row và bấm “Set ACTIVE=Y”. Nếu mỗi `setCellData()` kích hoạt formatter, summary, kiểm tra hợp lệ (validation / 검증) và redraw toàn Grid, chi phí có thể tăng rất lớn.

Lập luận (reasoning / 추론) đúng:

```text
begin bulk intent
→ mutate model rows
→ suppress/defer expensive derived work nếu build hỗ trợ
→ recalculate derived state một lần
→ redraw/refresh một lần
→ validate result
```

Tên API suspend/redraw cụ thể phụ thuộc bản dựng (build / 빌드). Đừng bản sao (copy / 복사) một private engine trick từ dự án (project / 프로젝트) khác. Hãy tìm API công khai (public API / 공개 API)/cấu hình (config / 설정) của Grid/DataList đang dùng và đo trước/sau bằng hiệu năng (performance / 성능) dấu vết (trace / 추적).

> **Chuyển mạch:** Ở chặng này của **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **11. Bulk mutation cần một transaction-like máy khách (client / 클라이언트) ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **12. Formatter là pure projection càng nhiều càng tốt** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **13. Expression, subtotal và summary có computational ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Formatter là pure projection càng nhiều càng tốt

Formatter tốt nhận giá trị (value / 값)/ngữ cảnh (context / 맥락) và trả biểu diễn (representation / 표현). Nó không nên âm thầm mutate DataList, gọi Submission hoặc truy vấn (query / 쿼리) DOM lớn.

```text
model value
→ formatter
→ display text/style
```

Nếu formatter có side tác động (effect / 효과), redraw có thể vô tình chạy lô-gic nghiệp vụ (business logic / 비즈니스 로직) nhiều lần. Đây là loại bug rất khó thấy vì cùng một người dùng (user / 사용자) hành động (action / 동작) có thể dẫn đến nhiều kết xuất (render / 렌더링) pass.

Cấp cao (senior / 시니어) ghi chú (note / 노트): kết xuất (render / 렌더링) callback phải được xem như đường xử lý nóng (hot path / 핫 패스). Một hàm (function / 함수) 0.1 ms chạy 100.000 lần vẫn thành 10 giây CPU.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **13. Expression, subtotal và summary có computational ngân sách (budget / 예산)** gom các mảnh từ **12. Formatter là pure projection càng nhiều càng tốt** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **14. Infinite scroll không biến full payload thành nhỏ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Expression, subtotal và summary có computational ngân sách (budget / 예산)

Grid hỗ trợ expression, subtotal/footer và nhiều dạng derived display. Chúng hữu ích nhưng mỗi derived giá trị (value / 값) đều có chi phí (cost / 비용) và vô hiệu hóa (invalidation / 무효화) quy tắc (rule / 규칙).

Nếu một cell thay đổi khiến toàn bộ summary scan lại 50.000 row, rồi bulk cập nhật (update / 업데이트) 5.000 cell, độ phức tạp (complexity / 복잡도) có thể bùng nổ. Khi hiệu năng (performance / 성능) giảm, đo số lần hàm (function / 함수) chạy và dataset kích thước (size / 크기) trước khi tối ưu micro-code.

Một số calculation nên chuyển máy chủ (server / 서버) nếu nó thuộc nghiệp vụ (business / 비즈니스) truth hoặc cần full dataset mà trình duyệt (browser / 브라우저) chỉ có một page.

> **Chuyển mạch:** Trong **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **14. Infinite scroll không biến full payload thành nhỏ** gom các mảnh từ **13. Expression, subtotal và summary có computational ngân sách (budget / 예산)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **15. máy chủ (server / 서버) paging làm selection xuyên trang trở thành lĩnh vực (domain / 도메인) bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Infinite scroll không biến full payload thành nhỏ

Grid có thể kết xuất (render / 렌더링) tuần tự hoặc hỗ trợ large-data display tốt hơn, nhưng phải tách ba vấn đề:

```text
network volume
client model volume
rendered DOM/view volume
```

Virtual/infinite rendering chủ yếu giảm view/DOM chi phí (cost / 비용). Nếu máy chủ (server / 서버) vẫn gửi 500.000 row một lần, mạng (network / 네트워크), JSON parse và DataList bộ nhớ (memory / 메모리) vẫn tồn tại.

Nếu dataset lớn thật, server-side paging/truy vấn (query / 쿼리) thường là kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계) quan trọng hơn Grid rendering option.

> **Chuyển mạch:** Ở chặng này của **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **15. máy chủ (server / 서버) paging làm selection xuyên trang trở thành lĩnh vực (domain / 도메인) bài toán (problem / 문제)** tiếp nhận điểm tựa từ **14. Infinite scroll không biến full payload thành nhỏ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Save trong khi editor còn active phải có chính sách (policy / 정책) rõ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. máy chủ (server / 서버) paging làm selection xuyên trang trở thành lĩnh vực (domain / 도메인) bài toán (problem / 문제)

Nếu trình duyệt (browser / 브라우저) chỉ giữ page 3 gồm 20 row, “Select all 100.000 records” không thể chỉ là tick 20 checkbox hiện có.

Cần đặc tả hợp đồng (contract / 계약) rõ:

```text
select current page
select loaded rows
select all rows matching last executed query
```

Trường hợp cuối thường nên gửi truy vấn (query / 쿼리) snapshot + exclusion/inclusion keys cho máy chủ (server / 서버) thay vì materialize 100.000 định danh (identity / 식별자) trong trình duyệt (browser / 브라우저).

Đây là ví dụ điển hình cho việc UI wording phải khớp dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **16. Save trong khi editor còn active phải có chính sách (policy / 정책) rõ** tiếp nhận điểm tựa từ **15. máy chủ (server / 서버) paging làm selection xuyên trang trở thành lĩnh vực (domain / 도메인) bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. điều hướng (navigation / 내비게이션) khi cell invalid cần phân biệt “không cho rời cell” và “không cho save”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Save trong khi editor còn active phải có chính sách (policy / 정책) rõ

Một dạng thất bại (failure mode / 실패 모드) thực tế:

```text
user gõ giá trị mới
→ chưa rời cell
→ click Save
→ payload vẫn chứa giá trị trước edit
```

Không nên chữa bằng `setTimeout(100)` vì đó chỉ là timing guess. Hãy xác định công khai (public / 공개) Grid/edit API hoặc vòng đời (lifecycle / 생명주기) convention của dự án (project / 프로젝트) để lần ghi nhận (commit / 커밋)/finish hiện tại (current / 현재) edit trước khi serialize. Sau đó regression kiểm thử (test / 테스트) bằng cách click Save trực tiếp khi editor còn active.

Nếu bản dựng (build / 빌드) tự lần ghi nhận (commit / 커밋) trước click handler thì kiểm thử (test / 테스트) sẽ chứng minh hành vi (behavior / 동작) đó; nếu không, ứng dụng (application / 애플리케이션) phải tường minh (explicit / 명시적).

> **Chuyển mạch:** Trong **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **17. điều hướng (navigation / 내비게이션) khi cell invalid cần phân biệt “không cho rời cell” và “không cho save”** tiếp nhận điểm tựa từ **16. Save trong khi editor còn active phải có chính sách (policy / 정책) rõ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. lỗi (error / 오류) ánh xạ (mapping / 매핑) phải sống qua sort/filter** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. điều hướng (navigation / 내비게이션) khi cell invalid cần phân biệt “không cho rời cell” và “không cho save”

Blocking row/cell điều hướng (navigation / 내비게이션) cho mọi invalid giá trị (value / 값) có thể làm UX bị trap. Một số quy tắc (rule / 규칙) nên ngăn mutation ngay; một số quy tắc (rule / 규칙) nên cho người dùng (user / 사용자) tiếp tục nhập rồi validate ở Save.

Quyết định (decision / 결정) dựa vào loại bất biến (invariant / 불변식):

```text
syntactic impossible value → có thể reject sớm
required field → có thể đánh dấu lỗi và cho di chuyển
cross-row uniqueness → thường validate dataset/save
server-owned rule → validate server
```

Đừng biến mọi kiểm tra hợp lệ (validation / 검증) thành before-navigation khối (block / 블록).

> **Chuyển mạch:** Ở chặng này của **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **18. lỗi (error / 오류) ánh xạ (mapping / 매핑) phải sống qua sort/filter** tiếp nhận điểm tựa từ **17. điều hướng (navigation / 내비게이션) khi cell invalid cần phân biệt “không cho rời cell” và “không cho save”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Excel import là một bulk edit chuỗi xử lý (pipeline / 파이프라인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. lỗi (error / 오류) ánh xạ (mapping / 매핑) phải sống qua sort/filter

Máy chủ (server / 서버) trả `rowIndex=12` là fragile nếu người dùng (user / 사용자) có thể sort/filter trong lúc yêu cầu (request / 요청) pending. Tốt hơn trả nghiệp vụ (business / 비즈니스) định danh (identity / 식별자) + trường dữ liệu (field / 필드)/mã (code / 코드).

```json
{
  "entityKey": "ORD-2026-00123",
  "field": "AMOUNT",
  "code": "LIMIT_EXCEEDED"
}
```

Máy khách (client / 클라이언트) resolve row hiện tại bằng key rồi focus/highlight nếu row visible. Nếu row bị filter ẩn, UX có thể hiển thị summary “1 lỗi nằm ngoài filter hiện tại” thay vì silently bỏ lỗi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **18. lỗi (error / 오류) ánh xạ (mapping / 매핑) phải sống qua sort/filter** xác định đầu vào; **19. Excel import là một bulk edit chuỗi xử lý (pipeline / 파이프라인)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **20. Excel export phải định nghĩa giá trị (value / 값) ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Excel import là một bulk edit chuỗi xử lý (pipeline / 파이프라인)

`advancedExcelUpload()` có thể đưa nhiều row vào Grid, nhưng về kiến trúc (architecture / 아키텍처) nó là một import chuỗi xử lý (pipeline / 파이프라인):

```text
untrusted file
→ parse/convert
→ column mapping
→ client model
→ validation
→ preview/error report
→ server validation
→ transaction/partial result
```

Không nên coi “Excel đã hiện đúng trong Grid” là “dữ liệu đã an toàn để save”. kiểu (type / 타입) conversion, trim, date format, duplicate key và hidden formula/content đều cần chính sách (policy / 정책).

> **Chuyển mạch:** Trong **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **19. Excel import là một bulk edit chuỗi xử lý (pipeline / 파이프라인)** xác định đầu vào; **20. Excel export phải định nghĩa giá trị (value / 값) ngữ nghĩa (semantics / 의미론)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **21. khả năng tiếp cận (accessibility / 접근성) thay đổi tương tác (interaction / 상호작용) các giả định (assumptions / 가정들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Excel export phải định nghĩa giá trị (value / 값) ngữ nghĩa (semantics / 의미론)

Grid có thể hiển thị mã (code / 코드) label khác mô hình (model / 모델) giá trị (value / 값). `advancedExcelDownload()` hỗ trợ nhiều option liên quan giá trị (value / 값)/label, style, dữ liệu (data / 데이터) format, row limit và callback tùy bản dựng (build / 빌드).

Trước khi cấu hình, quyết định report đặc tả hợp đồng (contract / 계약):

```text
Excel dùng code hay label?
Export source dataset hay current grouped/filtered view?
Date là text hay Excel date?
Có export hidden/sensitive column không?
Max row/cell là bao nhiêu?
```

Bảo mật (security / 보안) rà soát (review / 검토) phải bao gồm việc người dùng có thể export dữ liệu mà UI chỉ “ẩn” nhưng DataList vẫn chứa.

> **Chuyển mạch:** Ở chặng này của **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **21. khả năng tiếp cận (accessibility / 접근성) thay đổi tương tác (interaction / 상호작용) các giả định (assumptions / 가정들)** tiếp nhận điểm tựa từ **20. Excel export phải định nghĩa giá trị (value / 값) ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Grid debugging theo bốn coordinate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. khả năng tiếp cận (accessibility / 접근성) thay đổi tương tác (interaction / 상호작용) các giả định (assumptions / 가정들)

Grid khả năng tiếp cận (accessibility / 접근성) chế độ (mode / 모드) có thể thay đổi embedded đầu vào (input / 입력), focus movement, keyboard hành vi (behavior / 동작) và rendering footprint. Vì vậy kiểm thử (test / 테스트) Grid chỉ bằng mouse là chưa đủ.

Regression scenario nên có:

```text
Tab/Shift+Tab
arrow navigation
enter/escape edit
screen-reader relevant label/title
error focus
popup return focus
```

Hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) không được mặc định tắt khả năng tiếp cận (accessibility / 접근성) để giảm DOM. Hãy giảm dữ liệu (data / 데이터)/kết xuất (render / 렌더링) chi phí (cost / 비용) trước.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **22. Grid debugging theo bốn coordinate** tiếp nhận điểm tựa từ **21. khả năng tiếp cận (accessibility / 접근성) thay đổi tương tác (interaction / 상호작용) các giả định (assumptions / 가정들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Master bất biến (invariant / 불변식) cho Grid screen** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Grid debugging theo bốn coordinate

Khi một cell “sai”, ghi lại bốn thứ:

```text
business key của row
model index / view index hiện tại
column ID
value ở editor / Grid / DataList
```

Sau đó mới xem sự kiện (event / 이벤트) dấu vết (trace / 추적). Cách này loại bỏ phần lớn nhầm lẫn do chỉ log `rowIndex=3`.

Một gỡ lỗi (debug / 디버그) bản ghi (record / 레코드) tốt có thể như:

```javascript
console.log("[order-grid] edit", {
    orderId: orderId,
    viewRowIndex: viewRowIndex,
    columnId: info.colID,
    oldValue: info.oldValue,
    newValue: info.newValue
});
```

Không log dữ liệu nhạy cảm nếu môi trường vận hành (production / 운영 환경) chính sách (policy / 정책) không cho phép.

> **Chuyển mạch:** Trong **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **23. Master bất biến (invariant / 불변식) cho Grid screen** tiếp nhận điểm tựa từ **22. Grid debugging theo bốn coordinate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. trường hợp (case / 사례) study: chỉnh giá hàng loạt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Master bất biến (invariant / 불변식) cho Grid screen

Một Grid screen môi trường vận hành (production / 운영 환경) nên giữ các bất biến (invariant / 불변식) sau:

```text
Business identity không phụ thuộc view index.
Submission serialize canonical model, không đọc DOM.
Unsaved change không bị mất khi sort/filter/navigation ngoài ý muốn.
Async result không apply vào entity khác vì index stale.
Bulk operation không tạo event/redraw storm không kiểm soát.
Export/import có contract riêng, không chỉ “copy Grid”.
Accessibility và keyboard path được test như interaction chính thức.
```

Nếu một thiết kế (design / 설계) vi phạm một bất biến (invariant / 불변식), hãy ghi rõ lý do và regression kiểm thử (test / 테스트) cho exception đó.

> **Chuyển mạch:** Ở chặng này của **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **23. Master bất biến (invariant / 불변식) cho Grid screen** cho ta quy tắc; **24. trường hợp (case / 사례) study: chỉnh giá hàng loạt** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **25. Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. trường hợp (case / 사례) study: chỉnh giá hàng loạt

Giả sử màn hình có 20.000 sản phẩm, máy chủ (server / 서버) paging 100 row/page. người dùng (user / 사용자) filter category A, chọn 40 row trên page hiện tại, tăng giá 5%, rồi Save.

Đầu tiên, selection phải được snapshot bằng `PRODUCT_ID`, không bằng row chỉ mục (index / 인덱스). Tiếp theo, bulk mutation cập nhật DataList hiện có và đánh dấu row dirty. Derived display như margin có thể recalculate một lần sau batch. Save gửi changed entities cùng phiên bản (version / 버전) để optimistic locking. máy chủ (server / 서버) trả success/lỗi (error / 오류) theo `PRODUCT_ID`. máy khách (client / 클라이언트) map lỗi (error / 오류) về row hiện tại bằng key; nếu người dùng (user / 사용자) đã sort trong lúc yêu cầu (request / 요청) pending, chỉ mục (index / 인덱스) mới vẫn không làm sai định danh (identity / 식별자).

Nếu sản phẩm (product / 제품) ở page khác không được tải (load / 로드), thao tác (operation / 연산) không được tự hiểu là “tất cả category A”. Nếu sản phẩm (product / 제품) yêu cầu (requirement / 요구사항) muốn “tăng 5% toàn bộ kết quả filter”, đó phải là server-side bulk command dựa trên truy vấn (query / 쿼리) snapshot, không phải vòng lặp (loop / 루프) Grid.

Trường hợp (case / 사례) này gom nhiều nguyên tắc thành một câu: **Grid chỉ là cửa sổ tương tác lên một tập dữ liệu có định danh (identity / 식별자) và quyền sở hữu (ownership / 소유권) rõ; đừng biến vị trí hiển thị thành nghiệp vụ (business / 비즈니스) truth.**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **13 — GridView Editing, định danh (identity / 식별자) & View Internals**, **24. trường hợp (case / 사례) study: chỉnh giá hàng loạt** cho ta quy tắc; **25. Kết nối** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 25. Kết nối

Chapter này mở rộng [05 — GridView, CRUD & Enterprise Screen Patterns](05_gridview_crud_patterns.md) bằng editing/view internals. Khi Grid được đặt trong app shell nhiều tab/cửa sổ (window / 윈도우), định danh (identity / 식별자) của **page instance** cũng quan trọng như định danh (identity / 식별자) của row. Tiếp theo đọc [14 — Application Shell, Navigation & Multi-Screen State](14_application_shell_navigation_state.md).

> **Bàn giao:** Sau **25. Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
