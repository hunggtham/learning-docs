# 05 — GridView, CRUD & Enterprise Screen Patterns

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **05 — GridView, CRUD & Enterprise Screen Patterns**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. GridView là view; DataList mới là dữ liệu nghiệp vụ phía máy khách (client / 클라이언트)** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **2. tìm kiếm (search / 검색) screen điển hình** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối GridView với CRUD patterns, identity và validation, để mỗi thao tác thêm/sửa/xóa có trạng thái và lỗi được truy nguyên.

## 1. GridView là view; DataList mới là dữ liệu nghiệp vụ phía máy khách (client / 클라이언트)

GridView là một trong những thành phần (component / 컴포넌트) quan trọng nhất của WebSquare vì nhiều ứng dụng doanh nghiệp xoay quanh bảng tra cứu, chỉnh sửa hàng loạt và CRUD. Tuy nhiên mô hình tư duy (mental model / 사고 모델) sai phổ biến nhất là coi GridView như “cơ sở dữ liệu (database / 데이터베이스) trên màn hình”.

Nếu GridView bind với `dlUser`, hãy nghĩ:

```text
DataList = model
GridView = view + interaction layer
```

DataList giữ row, column giá trị (value / 값) và row status. GridView chịu trách nhiệm hiển thị, selection, edit UI, formatting, sort/filter/display hành vi (behavior / 동작) và các sự kiện (event / 이벤트) liên quan tương tác (interaction / 상호작용).

Khi cần gửi dữ liệu máy chủ (server / 서버), dirty check hoặc phân tích trạng thái (state / 상태), ưu tiên mô hình (model / 모델). Khi cần thay cách trình bày, ưu tiên GridView.

> **Chuyển mạch:** Trong **05 — GridView, CRUD & Enterprise Screen Patterns**, **1. GridView là view; DataList mới là dữ liệu nghiệp vụ phía máy khách (client / 클라이언트)** nêu điều cần giải thích; **2. tìm kiếm (search / 검색) screen điển hình** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. Row định danh (identity / 식별자) quan trọng hơn row chỉ mục (index / 인덱스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. tìm kiếm (search / 검색) screen điển hình

Một màn hình tìm kiếm enterprise thường có luồng (flow / 흐름):

```text
Search condition Inputs
        ⇅ binding
dmSearch
        │ reference
        ▼
sbmSearch
        │
        ▼
server query
        │
        ▼
dlUser target
        ⇅ binding
GridView
```

Luồng (flow / 흐름) này tốt vì mỗi tầng (layer / 계층) có trách nhiệm rõ. Nếu GridView rỗng, bạn có thể inspect `dlUser`. Nếu `dlUser` rỗng, inspect Submission phản hồi (response / 응답). Nếu phản hồi (response / 응답) rỗng, inspect máy chủ (server / 서버) truy vấn (query / 쿼리).

> **Chuyển mạch:** Search screen tạo input/query state; row identity giữ stable mapping khi DataList sort/filter/update. CRUD row status tiếp theo biến mapping đó thành transition contract.

## 3. Row định danh (identity / 식별자) quan trọng hơn row chỉ mục (index / 인덱스)

Row chỉ mục (index / 인덱스) là vị trí hiện tại trong danh sách (list / 목록), không phải định danh (identity / 식별자) nghiệp vụ (business / 비즈니스) ổn định. Sort, filter, insert, delete hoặc paging có thể làm chỉ mục (index / 인덱스) thay đổi.

Sai mẫu (pattern / 패턴):

```javascript
scwin.selectedRowIndex = 5;
// vài thao tác sau
var id = dlUser.getCellData(scwin.selectedRowIndex, "USER_ID");
```

Nếu danh sách (list / 목록) đã sort hoặc filter, row 5 có thể là người dùng (user / 사용자) khác.

Tốt hơn là giữ nghiệp vụ (business / 비즈니스) key khi cần tham chiếu (reference / 참조) dài hơn một sự kiện (event / 이벤트):

```javascript
var row = dlUser.getRowPosition();
scwin.selectedUserId = dlUser.getCellData(row, "USER_ID");
```

Sau đó nếu cần, tìm lại row bằng key theo API phù hợp.

> **Chuyển mạch:** Stable row identity làm CRUD mapping không phụ thuộc index; row status tiếp theo quyết định insert mới mang default nào và do owner nào khởi tạo.

## 4. CRUD row status và ý nghĩa thật

Grid edit làm DataList row chuyển trạng thái (state / 상태). Một vòng đời (lifecycle / 생명주기) thường là:

```text
server result → R
user edit → U
insert new row → C
delete existing row → D
insert rồi delete → V
```

Đây là thông tin quan trọng để save chỉ phần thay đổi.

```javascript
var count = dlUser.getRowCount();
for (var i = 0; i < count; i++) {
    var status = dlUser.getRowStatus(i);
    if (status !== "R") {
        console.log(i, status, dlUser.getRowJSON(i));
    }
}
```

Đừng reset row status chỉ để UI “trông sạch” trước khi máy chủ (server / 서버) lần ghi nhận (commit / 커밋). Bạn sẽ mất bằng chứng (evidence / 증거) về unsaved changes.

> **Chuyển mạch:** Insert default phải phản ánh business invariant; delete/remove tiếp theo tách thay đổi persistence khỏi việc chỉ bỏ row khỏi current view.

## 5. Insert row nên khởi tạo default có chủ đích

Khi người dùng (user / 사용자) thêm row mới, đừng để mỗi cell tự có default rời rạc nếu chúng đại diện một nghiệp vụ (business / 비즈니스) đối tượng (object / 객체).

```javascript
scwin.addUser = function () {
    var rowIndex = dlUser.insertRow();

    dlUser.setCellData(rowIndex, "ACTIVE_YN", "Y");
    dlUser.setCellData(rowIndex, "COUNTRY_CD", "KR");
};
```

Tên API có thể khác theo generation/bản dựng (build / 빌드), nhưng mẫu (pattern / 패턴) là: **create row → initialize lĩnh vực (domain / 도메인) defaults → move focus/selection**.

Nếu default đến máy chủ (server / 서버)/cấu hình (config / 설정), tránh hard-code rải rác nhiều screen.

> **Chuyển mạch:** Ở chặng này của **05 — GridView, CRUD & Enterprise Screen Patterns**, **6. Delete và remove khác nghiệp vụ (business / 비즈니스) meaning** tiếp nhận điểm tựa từ **5. Insert row nên khởi tạo default có chủ đích** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. GridView có thể ẩn row deleted nhưng DataList vẫn giữ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Delete và remove khác nghiệp vụ (business / 비즈니스) meaning

Khi xóa row đã tồn tại trên máy chủ (server / 서버), máy khách (client / 클라이언트) thường cần giữ delete intent để save. Nếu chỉ remove row khỏi DataList mà không giữ status/delete payload, máy chủ (server / 서버) không biết phải xóa gì.

Ngược lại, row mới `C` chưa từng tồn tại máy chủ (server / 서버) nếu người dùng (user / 사용자) bỏ đi có thể chỉ cần remove client-side.

Vì vậy trước khi chọn API, xác định chuyển tiếp trạng thái (state transition / 상태 전이):

```text
existing row → marked delete → server DELETE
new unsaved row → discard locally
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **05 — GridView, CRUD & Enterprise Screen Patterns**, **7. GridView có thể ẩn row deleted nhưng DataList vẫn giữ** tiếp nhận điểm tựa từ **6. Delete và remove khác nghiệp vụ (business / 비즈니스) meaning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Cell giá trị (value / 값) và display giá trị (value / 값)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. GridView có thể ẩn row deleted nhưng DataList vẫn giữ

Thuộc tính (property / 속성) như `hideDeletedRow` cho phép UI không hiển thị row `D`. Đây là presentation choice, không phải mô hình (model / 모델) deletion.

Hệ quả: count trên Grid và count trên DataList có thể khác ngữ nghĩa (semantics / 의미론). Khi hiển thị “총 10건”, hãy quyết định đang đếm visible records, máy chủ (server / 서버) records hay all máy khách (client / 클라이언트) rows including deleted.

> **Chuyển mạch:** Trong **05 — GridView, CRUD & Enterprise Screen Patterns**, **8. Cell giá trị (value / 값) và display giá trị (value / 값)** tiếp nhận điểm tựa từ **7. GridView có thể ẩn row deleted nhưng DataList vẫn giữ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. kiểm tra hợp lệ (validation / 검증) theo row trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Cell giá trị (value / 값) và display giá trị (value / 값)

Một cell có thể hiển thị label nhưng lưu mã (code / 코드).

```text
model value: "01"
display value: "서울"
```

Hoặc date/number format tương tự đầu vào (input / 입력). Khi bản dựng (build / 빌드) payload hoặc compare nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터), dùng mô hình (model / 모델) giá trị (value / 값). Khi export “những gì người dùng (user / 사용자) nhìn thấy”, display giá trị (value / 값) có thể phù hợp hơn.

Đừng compare display string nếu nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) dựa mã (code / 코드).

> **Chuyển mạch:** Ở chặng này của **05 — GridView, CRUD & Enterprise Screen Patterns**, **9. kiểm tra hợp lệ (validation / 검증) theo row trạng thái (state / 상태)** tiếp nhận điểm tựa từ **8. Cell giá trị (value / 값) và display giá trị (value / 값)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Cross-row bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. kiểm tra hợp lệ (validation / 검증) theo row trạng thái (state / 상태)

Một Grid 5.000 row nhưng chỉ 3 row thay đổi. kiểm tra hợp lệ (validation / 검증) hiệu quả nên tập trung changed rows.

```javascript
scwin.validateChangedRows = function () {
    var count = dlUser.getRowCount();

    for (var i = 0; i < count; i++) {
        var status = dlUser.getRowStatus(i);

        if (status === "C" || status === "U") {
            if (!scwin.validateUserRow(i)) {
                return false;
            }
        }
    }

    return true;
};
```

Nếu quy tắc (rule / 규칙) liên quan uniqueness toàn dataset, vẫn có thể cần scan nhiều row. Optimize theo ngữ nghĩa (semantics / 의미론), không theo công thức “chỉ changed rows”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **05 — GridView, CRUD & Enterprise Screen Patterns**, **10. Cross-row bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **9. kiểm tra hợp lệ (validation / 검증) theo row trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Before-change sự kiện (event / 이벤트) để chặn invalid chuyển tiếp (transition / 전이)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Cross-row bất biến (invariant / 불변식)

Một số quy tắc (rule / 규칙) không thuộc riêng một cell:

```text
không trùng USER_ID
chỉ một row được PRIMARY=Y
sum(weight) = 100
fromDate <= toDate trong mọi row
```

Những quy tắc (rule / 규칙) này nên có hàm (function / 함수) tên rõ:

```javascript
scwin.validatePrimaryRow = function () { ... };
scwin.validateDuplicateUserId = function () { ... };
```

Không nhét lô-gic (logic / 논리) vào `onchange` của từng cell nếu quy tắc (rule / 규칙) cần toàn dataset, vì nó dễ bị bypass khi dữ liệu (data / 데이터) tải (load / 로드) bằng API.

> **Chuyển mạch:** Trong **05 — GridView, CRUD & Enterprise Screen Patterns**, **11. Before-change sự kiện (event / 이벤트) để chặn invalid chuyển tiếp (transition / 전이)** tiếp nhận điểm tựa từ **10. Cross-row bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Selection trạng thái (state / 상태) không nên bị nhầm với dữ liệu (data / 데이터) trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Before-change sự kiện (event / 이벤트) để chặn invalid chuyển tiếp (transition / 전이)

DataList có sự kiện (event / 이벤트) trước cell thay đổi (change / 변경) cho phép trả `false` để từ chối mutation trong một số bản dựng (build / 빌드).

Conceptual:

```javascript
scwin.dlUser_onbeforecelldatachange = function (info) {
    if (info.colID === "AGE" && Number(info.newValue) < 0) {
        return false;
    }
};
```

Đây phù hợp cho cục bộ (local / 로컬) bất biến (invariant / 불변식) rẻ và rõ. quy tắc (rule / 규칙) cần máy chủ (server / 서버) dữ liệu (data / 데이터) hoặc async check không nên khối (block / 블록) theo cách giả định synchronous.

> **Chuyển mạch:** Ở chặng này của **05 — GridView, CRUD & Enterprise Screen Patterns**, **11. Before-change sự kiện (event / 이벤트) để chặn invalid chuyển tiếp (transition / 전이)** đã nêu tiêu chí phân biệt, còn **12. Selection trạng thái (state / 상태) không nên bị nhầm với dữ liệu (data / 데이터) trạng thái (state / 상태)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **13. tìm kiếm (search / 검색) lại sau save hay cập nhật (update / 업데이트) cục bộ (local / 로컬)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Selection trạng thái (state / 상태) không nên bị nhầm với dữ liệu (data / 데이터) trạng thái (state / 상태)

Grid có hiện tại (current / 현재) row, selected rows, checked rows hoặc focus cell. Đây là tương tác (interaction / 상호작용) trạng thái (state / 상태), không phải nghiệp vụ (business / 비즈니스) trạng thái (state / 상태).

Nếu người dùng (user / 사용자) tick checkbox để chọn row gửi batch thao tác (operation / 연산), hãy phân biệt:

```text
selection checkbox do UI quản lý
vs.
BUSINESS_SELECTED_YN field thực sự cần persist
```

Không nên persist UI selection chỉ vì nó tiện.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **05 — GridView, CRUD & Enterprise Screen Patterns**, **12. Selection trạng thái (state / 상태) không nên bị nhầm với dữ liệu (data / 데이터) trạng thái (state / 상태)** đã nêu tiêu chí phân biệt, còn **13. tìm kiếm (search / 검색) lại sau save hay cập nhật (update / 업데이트) cục bộ (local / 로컬)?** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **14. Optimistic locking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. tìm kiếm (search / 검색) lại sau save hay cập nhật (update / 업데이트) cục bộ (local / 로컬)?

Sau save thành công, lựa chọn thường là:

**Re-query**: máy chủ (server / 서버) trả chuẩn gốc (canonical / 정본) trạng thái (state / 상태) bằng truy vấn (query / 쿼리) mới.

**cục bộ (local / 로컬) cập nhật (update / 업데이트)**: giữ DataList, cập nhật (update / 업데이트) server-generated trường dữ liệu (field / 필드) rồi reset dirty trạng thái (state / 상태).

Re-query phù hợp khi máy chủ (server / 서버) có chuỗi (sequence / 시퀀스), timestamp, calculated trường dữ liệu (field / 필드), trigger hoặc normalization. cục bộ (local / 로컬) cập nhật (update / 업데이트) phù hợp khi độ trễ (latency / 지연 시간) quan trọng và máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약) trả đầy đủ chuẩn gốc (canonical / 정본) kết quả (result / 결과).

Không có lựa chọn luôn đúng. Hãy cân tính đúng đắn (correctness / 정확성), độ trễ (latency / 지연 시간) và độ phức tạp (complexity / 복잡도).

> **Chuyển mạch:** Trong **05 — GridView, CRUD & Enterprise Screen Patterns**, **14. Optimistic locking** tiếp nhận điểm tựa từ **13. tìm kiếm (search / 검색) lại sau save hay cập nhật (update / 업데이트) cục bộ (local / 로컬)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Paging: client-side và server-side khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Optimistic locking

Nếu hai người dùng (user / 사용자) cùng sửa một row, row status phía máy khách (client / 클라이언트) không giải quyết xung đột (conflict / 충돌). máy chủ (server / 서버) cần tính đồng thời (concurrency / 동시성) điều khiển (control / 제어), ví dụ phiên bản (version / 버전) column hoặc last-updated timestamp.

Máy khách (client / 클라이언트) gửi:

```text
USER_ID = U1001
VERSION = 7
new NAME = ...
```

Máy chủ (server / 서버) cập nhật (update / 업데이트) với điều kiện (condition / 조건) `VERSION = 7`. Nếu affected rows = 0, có thể đã bị người khác sửa.

WebSquare chỉ là nơi vận chuyển (transport / 전송)/display xung đột (conflict / 충돌); bất biến (invariant / 불변식) tính đồng thời (concurrency / 동시성) thuộc máy chủ (server / 서버)/cơ sở dữ liệu (database / 데이터베이스).

> **Chuyển mạch:** Ở chặng này của **05 — GridView, CRUD & Enterprise Screen Patterns**, **15. Paging: client-side và server-side khác nhau** tiếp nhận điểm tựa từ **14. Optimistic locking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Large dataset và rendering ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Paging: client-side và server-side khác nhau

Nếu máy chủ (server / 서버) trả 20 row mỗi page, Grid chỉ biết page hiện tại. Sort/filter client-side chỉ áp dụng dataset hiện có trừ khi khung phần mềm (framework / 프레임워크)/mẫu (pattern / 패턴) trigger máy chủ (server / 서버) truy vấn (query / 쿼리).

Nếu nghiệp vụ (business / 비즈니스) yêu cầu sort toàn bộ 1 triệu row, máy chủ (server / 서버) phải tham gia.

Mô hình tư duy (mental model / 사고 모델):

```text
client paging → full dataset ở browser, view chia page
server paging → browser chỉ có một slice
```

Đừng viết lô-gic (logic / 논리) “đếm toàn bộ” dựa trên `getRowCount()` nếu máy chủ (server / 서버) paging đang bật.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **05 — GridView, CRUD & Enterprise Screen Patterns**, **16. Large dataset và rendering ngân sách (budget / 예산)** tiếp nhận điểm tựa từ **15. Paging: client-side và server-side khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. N+1 Submission ở từng row là anti-pattern** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Large dataset và rendering ngân sách (budget / 예산)

GridView hỗ trợ nhiều tính năng cho dữ liệu lớn, nhưng không có thành phần (component / 컴포넌트) nào miễn phí. chi phí (cost / 비용) có thể đến từ:

```text
JSON parse
DataList creation
binding propagation
cell formatting
renderer creation
layout/reflow
custom event per cell
DOM nodes
```

Trước khi tối ưu, đo:

```text
response size
request duration
DataList row count
time từ response đến UI usable
main-thread long tasks
memory before/after load
```

Nếu 50 MB JSON được trả về, virtual scroll không làm mạng (network / 네트워크) và parse chi phí (cost / 비용) biến mất.

> **Chuyển mạch:** Trong **05 — GridView, CRUD & Enterprise Screen Patterns**, **17. N+1 Submission ở từng row là anti-pattern** tiếp nhận điểm tựa từ **16. Large dataset và rendering ngân sách (budget / 예산)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Custom formatting không nên chứa heavy lô-gic nghiệp vụ (business logic / 비즈니스 로직)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. N+1 Submission ở từng row là anti-pattern

Một màn hình tải (load / 로드) 100 row rồi gọi thêm một Submission cho mỗi row tạo N+1 mạng (network / 네트워크) bài toán (problem / 문제).

```text
1 query list
+ 100 query detail
= 101 request
```

Nếu máy chủ (server / 서버) có thể phép nối (join / 조인)/batch, ưu tiên batch đặc tả hợp đồng (contract / 계약). Nếu detail thật sự lazy, chỉ tải (load / 로드) khi người dùng (user / 사용자) mở row cần thiết.

> **Chuyển mạch:** Ở chặng này của **05 — GridView, CRUD & Enterprise Screen Patterns**, **18. Custom formatting không nên chứa heavy lô-gic nghiệp vụ (business logic / 비즈니스 로직)** tiếp nhận điểm tựa từ **17. N+1 Submission ở từng row là anti-pattern** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Excel upload/download là dữ liệu (data / 데이터) ranh giới (boundary / 경계) nguy hiểm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Custom formatting không nên chứa heavy lô-gic nghiệp vụ (business logic / 비즈니스 로직)

Cell formatter/kết xuất (render / 렌더링) callback có thể chạy rất nhiều lần. Nếu nó parse JSON lớn, gọi synchronous utility nặng hoặc truy vấn (query / 쿼리) DOM, scrolling sẽ lag.

Formatter nên gần pure hàm (function / 함수):

```text
input value → display representation
```

Nghiệp vụ (business / 비즈니스) computation nên chuẩn bị trước ở mô hình (model / 모델)/máy chủ (server / 서버) nếu phức tạp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **05 — GridView, CRUD & Enterprise Screen Patterns**, **18. Custom formatting không nên chứa heavy lô-gic nghiệp vụ (business logic / 비즈니스 로직)** đã nêu tiêu chí phân biệt, còn **19. Excel upload/download là dữ liệu (data / 데이터) ranh giới (boundary / 경계) nguy hiểm** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **20. Batch save và partial thất bại (failure / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Excel upload/download là dữ liệu (data / 데이터) ranh giới (boundary / 경계) nguy hiểm

WebSquare hỗ trợ Grid/Excel tích hợp (integration / 통합) ở nhiều bản dựng (build / 빌드). Đây là tính năng (feature / 기능) tiện nhưng upload Excel đưa một khối dữ liệu không đáng tin vào máy khách (client / 클라이언트)/máy chủ (server / 서버).

Phải nghĩ đến:

```text
file size limit
column mapping
formula/cell type
invalid date/number
duplicate row
malicious content
server validation
transaction size
partial failure reporting
```

Upload thành Grid không đồng nghĩa dữ liệu (data / 데이터) hợp lệ để persist.

> **Chuyển mạch:** Trong **05 — GridView, CRUD & Enterprise Screen Patterns**, **19. Excel upload/download là dữ liệu (data / 데이터) ranh giới (boundary / 경계) nguy hiểm** đã nêu tiêu chí phân biệt, còn **20. Batch save và partial thất bại (failure / 실패)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **21. lỗi (error / 오류) ánh xạ (mapping / 매핑) về row/cell** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Batch save và partial thất bại (failure / 실패)

Giả sử 100 row được save. máy chủ (server / 서버) có hai chiến lược (strategy / 전략):

**all-or-nothing giao dịch (transaction / 트랜잭션)**: một row lỗi thì quay lui (rollback / 롤백) tất cả.

**partial success**: row hợp lệ lần ghi nhận (commit / 커밋), row lỗi trả lỗi (error / 오류) riêng.

Máy khách (client / 클라이언트) UX phải phù hợp. Với partial success, DataList cần biết row nào đã lần ghi nhận (commit / 커밋) và row nào còn dirty/lỗi (error / 오류). Đây là giao thức (protocol / 프로토콜) thiết kế (design / 설계), không chỉ Grid sự kiện (event / 이벤트).

> **Chuyển mạch:** Ở chặng này của **05 — GridView, CRUD & Enterprise Screen Patterns**, **21. lỗi (error / 오류) ánh xạ (mapping / 매핑) về row/cell** tiếp nhận điểm tựa từ **20. Batch save và partial thất bại (failure / 실패)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. truy vấn (query / 쿼리) điều kiện (condition / 조건) trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. lỗi (error / 오류) ánh xạ (mapping / 매핑) về row/cell

Máy chủ (server / 서버) kiểm tra hợp lệ (validation / 검증) tốt nên trả stable identifier, ví dụ nghiệp vụ (business / 비즈니스) key và trường dữ liệu (field / 필드) name, thay vì chỉ row chỉ mục (index / 인덱스).

```json
{
  "errors": [
    {
      "userId": "U1001",
      "field": "EMAIL",
      "code": "INVALID_EMAIL"
    }
  ]
}
```

Row chỉ mục (index / 인덱스) trên máy khách (client / 클라이언트) có thể thay đổi do sort/filter. nghiệp vụ (business / 비즈니스) key giúp map lỗi (error / 오류) ổn định hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **05 — GridView, CRUD & Enterprise Screen Patterns**, **22. truy vấn (query / 쿼리) điều kiện (condition / 조건) trạng thái (state / 상태)** tiếp nhận điểm tựa từ **21. lỗi (error / 오류) ánh xạ (mapping / 매핑) về row/cell** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. UI chế độ (mode / 모드): truy vấn (query / 쿼리) / EDIT / SAVE** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. truy vấn (query / 쿼리) điều kiện (condition / 조건) trạng thái (state / 상태)

Một bug UX phổ biến: người dùng (user / 사용자) tìm kiếm (search / 검색) A, sửa điều kiện thành B nhưng chưa tìm kiếm (search / 검색), rồi export Grid. Export nên dùng dữ liệu (data / 데이터) kết quả (result / 결과) A, nhưng title/filter label lại đọc hiện tại (current / 현재) đầu vào (input / 입력) B.

Có thể tách:

```text
editing search condition
last executed search condition
current result dataset
```

Nếu report/export cần biết truy vấn (query / 쿼리) đã chạy, snapshot điều kiện (condition / 조건) khi execute Submission.

> **Chuyển mạch:** Trong **05 — GridView, CRUD & Enterprise Screen Patterns**, **23. UI chế độ (mode / 모드): truy vấn (query / 쿼리) / EDIT / SAVE** tiếp nhận điểm tựa từ **22. truy vấn (query / 쿼리) điều kiện (condition / 조건) trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Unsaved-change guard** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. UI chế độ (mode / 모드): truy vấn (query / 쿼리) / EDIT / SAVE

Màn hình CRUD phức tạp nên tường minh (explicit / 명시적) chế độ (mode / 모드).

```javascript
scwin.setMode = function (mode) {
    scwin.mode = mode;

    var editing = mode === "EDIT" || mode === "CREATE";
    btnSave.setDisabled(!editing);
    btnAdd.setDisabled(mode === "SAVING");
};
```

Chế độ (mode / 모드) giúp thống nhất enable/readOnly trạng thái (state / 상태) của nhiều thành phần (component / 컴포넌트) thay vì rải thuộc tính (property / 속성) mutation khắp handlers.

> **Chuyển mạch:** Ở chặng này của **05 — GridView, CRUD & Enterprise Screen Patterns**, **24. Unsaved-change guard** tiếp nhận điểm tựa từ **23. UI chế độ (mode / 모드): truy vấn (query / 쿼리) / EDIT / SAVE** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Grid sự kiện (event / 이벤트) storm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Unsaved-change guard

Trước khi chuyển tab/page hoặc đóng popup, nếu DataList còn dirty, ứng dụng (application / 애플리케이션) nên quyết định có prompt người dùng (user / 사용자) không.

Dirty check phải dựa mô hình (model / 모델) trạng thái (state / 상태), không dựa “người dùng (user / 사용자) đã click Edit”. người dùng (user / 사용자) có thể click Edit nhưng không thay gì, hoặc dữ liệu (data / 데이터) có thể bị script thay dù người dùng (user / 사용자) không click Edit.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **05 — GridView, CRUD & Enterprise Screen Patterns**, **25. Grid sự kiện (event / 이벤트) storm** tiếp nhận điểm tựa từ **24. Unsaved-change guard** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Readability của grid mã (code / 코드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Grid sự kiện (event / 이벤트) storm

Một bulk cập nhật (update / 업데이트) có thể trigger rất nhiều sự kiện (event / 이벤트). Nếu mỗi sự kiện (event / 이벤트) tính lại summary toàn dataset, độ phức tạp (complexity / 복잡도) có thể từ O(n) thành O(n²).

Ví dụ 10.000 cell changes × scan 10.000 rows là 100 triệu thao tác (operation / 연산).

Khi bulk cập nhật (update / 업데이트), xem bản dựng (build / 빌드) có cơ chế suspend sự kiện (event / 이벤트)/redraw hay không; nếu không, thiết kế hàm (function / 함수) tổng hợp để chỉ recalculate một lần sau batch.

> **Chuyển mạch:** Trong **05 — GridView, CRUD & Enterprise Screen Patterns**, **26. Readability của grid mã (code / 코드)** tiếp nhận điểm tựa từ **25. Grid sự kiện (event / 이벤트) storm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Example: search-edit-save hoàn chỉnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Readability của grid mã (code / 코드)

Thay vì magic string rải rác:

```javascript
dlUser.getCellData(i, "USR_NM");
dlUser.getCellData(i, "USR_STS_CD");
```

Dự án (project / 프로젝트) có thể dùng constant ánh xạ (mapping / 매핑) nếu convention cho phép:

```javascript
var USER_COL = {
    ID: "USER_ID",
    NAME: "USER_NAME",
    STATUS: "STATUS_CD"
};
```

Tuy nhiên đừng lớp trừu tượng (abstraction / 추상화) quá mức khiến dev phải nhảy 5 tệp (file / 파일) mới biết column ID. Mục tiêu là giảm typo và giữ lĩnh vực (domain / 도메인) vocabulary rõ.

> **Chuyển mạch:** Ở chặng này của **05 — GridView, CRUD & Enterprise Screen Patterns**, **26. Readability của grid mã (code / 코드)** cho ta quy tắc; **27. Example: search-edit-save hoàn chỉnh** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **28. cấp cao (senior / 시니어) code-review checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Example: search-edit-save hoàn chỉnh

```javascript
scwin.btnSearch_onclick = function () {
    scwin.search();
};

scwin.search = function () {
    if (scwin.hasUnsavedChanges()) {
        // confirm trước khi mất changes nếu UX yêu cầu
    }

    scwin.lastSearchCondition = dmSearch.getJSON();
    $p.executeSubmission(sbmSearchUser);
};

scwin.btnAdd_onclick = function () {
    scwin.addUser();
};

scwin.btnSave_onclick = function () {
    scwin.saveUsers();
};

scwin.saveUsers = function () {
    if (!scwin.hasUnsavedChanges()) {
        return;
    }

    if (!scwin.validateChangedRows()) {
        return;
    }

    if (scwin.isSaving) {
        return;
    }

    scwin.isSaving = true;
    $p.executeSubmission(sbmSaveUser);
};
```

Tên API DataMap như `getJSON()` phải được đối chiếu bản dựng (build / 빌드) nếu dùng thực tế; ví dụ này nhấn mạnh orchestration cấu trúc (structure / 구조) hơn là tham chiếu (reference / 참조) API tuyệt đối.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **05 — GridView, CRUD & Enterprise Screen Patterns**, **27. Example: search-edit-save hoàn chỉnh** cho ta quy tắc; **28. cấp cao (senior / 시니어) code-review checklist** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **29. Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. cấp cao (senior / 시니어) code-review checklist

Khi rà soát (review / 검토) Grid screen, hỏi:

“mã (code / 코드) đang thao tác mô hình (model / 모델) hay DOM/Grid internals?”

“Row chỉ mục (index / 인덱스) có bị giữ quá lâu thay vì nghiệp vụ (business / 비즈니스) key?”

“Delete ngữ nghĩa (semantics / 의미론) có đúng với máy chủ (server / 서버) thao tác (operation / 연산) không?”

“Dirty check dựa row trạng thái (state / 상태) thật hay flag thủ công?”

“kiểm tra hợp lệ (validation / 검증) có scan toàn bộ grid không cần thiết?”

“Có N+1 Submission không?”

“máy chủ (server / 서버) paging nhưng mã (code / 코드) lại giả định full dataset không?”

“Batch save có giao thức (protocol / 프로토콜) partial thất bại (failure / 실패) rõ không?”

“Sau save máy khách (client / 클라이언트) lấy chuẩn gốc (canonical / 정본) trạng thái (state / 상태) từ đâu?”

> **Chuyển mạch:** Trong **05 — GridView, CRUD & Enterprise Screen Patterns**, **29. Kết nối** tiếp nhận điểm tựa từ **28. cấp cao (senior / 시니어) code-review checklist** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 29. Kết nối

Một Grid screen đúng lô-gic (logic / 논리) vẫn có thể chậm, leak bộ nhớ (memory / 메모리) hoặc tạo bảo mật (security / 보안) issue. Tiếp theo: [06 — Debugging, Performance, Security & Production](06_debugging_performance_security.md).

> **Bàn giao:** Sau **29. Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
