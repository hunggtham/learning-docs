# 08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Bài toán thật sự của reuse** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Các mức lớp trừu tượng (abstraction / 추상화) nên phân biệt** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

WebSquare enterprise dự án (project / 프로젝트) thường không thất bại vì thiếu một API để set giá trị (value / 값). Nó thất bại khi hàng trăm màn hình cùng giải quyết một vấn đề theo hàng trăm cách khác nhau: mỗi màn hình tự tạo popup, tự validate, tự format date, tự dựng tìm kiếm (search / 검색) điều kiện (condition / 조건), tự gọi Submission, tự xử lý Grid và tự truy cập page khác. Vì vậy lớp trừu tượng (abstraction / 추상화) và reusable kiến trúc (architecture / 아키텍처) là phần bắt buộc nếu muốn đọc hoặc duy trì codebase lớn.

Chapter này không dạy “cách tạo UDC” theo kiểu thao tác Studio. Mục tiêu là hiểu **khi nào một thứ nên trở thành UDC, dùng chung (common / 공통) hàm (function / 함수), page template, bố cục (layout / 레이아웃), snippet hay page riêng**, công khai (public / 공개) đặc tả hợp đồng (contract / 계약) của lớp trừu tượng (abstraction / 추상화) nên có hình dạng nào, và dạng thất bại (failure mode / 실패 모드) nào xuất hiện khi tái sử dụng sai ranh giới (boundary / 경계).

## 1. Bài toán thật sự của reuse

Reuse không có nghĩa là càng gom nhiều mã (code / 코드) vào dùng chung (common / 공통) càng tốt. Hai đoạn mã (code / 코드) giống nhau về chữ chưa chắc đại diện cùng một concept. Ngược lại, hai màn hình nhìn khác nhau có thể cùng tuân theo một bất biến (invariant / 불변식) và nên dùng chung lớp trừu tượng (abstraction / 추상화).

Ví dụ ba màn hình đều có nút tìm nhân viên. Nếu chỉ giống nhau ở việc mở popup nhưng mỗi nghiệp vụ dùng popup khác nhau, ép chúng vào một helper khổng lồ có thể làm coupling tăng. Nhưng nếu cả ba thực sự cùng cần đặc tả hợp đồng (contract / 계약):

```text
input: employeeId?, departmentId?, selectableStatus
output: { employeeId, employeeName, departmentId }
```

thì đây là một reusable nghiệp vụ (business / 비즈니스) tương tác (interaction / 상호작용) hợp lý.

Mô hình tư duy (mental model / 사고 모델) quan trọng là:

```text
reuse tốt = shared invariant + stable contract
reuse xấu = shared syntax + hidden branching
```

Một helper có 12 boolean flag thường là dấu hiệu nhiều concept khác nhau đã bị ép vào cùng hàm (function / 함수).

> **Chuyển mạch:** Reuse bắt đầu từ failure mode và ownership, không từ việc copy include; abstraction levels tiếp theo phân biệt shared primitive, UDC contract và common module boundary.

## 2. Các mức lớp trừu tượng (abstraction / 추상화) nên phân biệt

Trong WebSquare dự án (project / 프로젝트), có nhiều cơ chế (mechanism / 메커니즘) tái sử dụng nhưng chúng giải quyết vấn đề khác nhau.

**dùng chung (common / 공통) JavaScript mô-đun (module / 모듈)** phù hợp cho lô-gic (logic / 논리) không cần sở hữu UI vòng đời (lifecycle / 생명주기), chẳng hạn normalize dữ liệu, format lĩnh vực (domain / 도메인) giá trị (value / 값), tạo yêu cầu (request / 요청) siêu dữ liệu (metadata / 메타데이터) hoặc kiểm tra một quy tắc (rule / 규칙) thuần.

**Snippet** phù hợp cho scaffolding hoặc mẫu (pattern / 패턴) mã (code / 코드) lặp khi tạo nguồn (source / 소스), nhưng không tạo thời gian chạy (runtime / 런타임) lớp trừu tượng (abstraction / 추상화). Sau khi chèn snippet, các bản sao có thể tiến hóa riêng.

**Page template/bố cục (layout / 레이아웃) template** chuẩn hóa cấu trúc màn hình ban đầu. Nó giúp consistency khi tạo page nhưng không đồng nghĩa mọi instance dùng chung thời gian chạy (runtime / 런타임) đối tượng (object / 객체).

**WFrame/page composition** phù hợp khi một khu vực UI có vòng đời (lifecycle / 생명주기), DataCollection và hành vi (behavior / 동작) riêng, cần được tải (load / 로드) như một page ranh giới (boundary / 경계).

**UDC (User Defined Component / 사용자 정의 컴포넌트)** phù hợp khi muốn tạo một UI thành phần (component / 컴포넌트) có công khai (public / 공개) thuộc tính (property / 속성), phương thức (method / 메서드) và sự kiện (event / 이벤트) riêng, xuất hiện như một thành phần (component / 컴포넌트) có đặc tả hợp đồng (contract / 계약) rõ trong Studio/thời gian chạy (runtime / 런타임).

Không nên chọn cơ chế (mechanism / 메커니즘) dựa trên câu hỏi “cái nào tiện nhất lúc này”. Hãy hỏi đối tượng (object / 객체) mới cần sở hữu điều gì: nguồn (source / 소스) template, pure lô-gic (logic / 논리), UI trạng thái (state / 상태), vòng đời (lifecycle / 생명주기) hay thành phần (component / 컴포넌트) đặc tả hợp đồng (contract / 계약).

> **Chuyển mạch:** Abstraction levels phân biệt primitive, UDC và common module; UDC là contract-bearing component, nên public properties phải là cấu hình ổn định thay vì remote control.

## 3. UDC là thành phần (component / 컴포넌트) đặc tả hợp đồng (contract / 계약), không phải một tệp (file / 파일) include đẹp hơn

Official WebSquare5 guide cho phép UDC khai báo thuộc tính (property / 속성), phương thức (method / 메서드) và sự kiện (event / 이벤트); thuộc tính (property / 속성) được đọc qua `$p.getOptions()` và UDC có thể được đưa vào Palette. Điều này cho thấy UDC nên được hiểu như một **thành phần (component / 컴포넌트) kiểu (type / 타입) do dự án (project / 프로젝트) định nghĩa**, không chỉ là một đoạn XML tái sử dụng.

Nếu một UDC `EmployeeSearch` có thuộc tính (property / 속성):

```text
requiredDepartment
allowInactive
placeholder
```

Phương thức (method / 메서드):

```text
getSelectedEmployee()
clear()
openSearch()
```

và sự kiện (event / 이벤트):

```text
onemployeechange
onsearchopen
```

thì page sử dụng nó không cần biết bên trong UDC dùng đầu vào (input / 입력), Trigger, Popup hay DataMap nào.

Đây là nguyên lý đóng gói (encapsulation / 캡슐화): **bên tiêu thụ (consumer / 소비자) phụ thuộc công khai (public / 공개) đặc tả hợp đồng (contract / 계약), không phụ thuộc nội bộ (internal / 내부) thành phần (component / 컴포넌트) ID**.

> **Chuyển mạch:** Public property giữ configuration contract; method tiếp theo nên biểu diễn command có chủ đích, không expose toàn bộ implementation của UDC.

## 4. công khai (public / 공개) thuộc tính (property / 속성) phải là cấu hình, không phải remote điều khiển (control / 제어)

Thuộc tính (property / 속성) tốt mô tả trạng thái cấu hình tương đối ổn định:

```text
mode="readonly"
required="true"
maxResult="20"
```

Thuộc tính (property / 속성) xấu thường bắt bên tiêu thụ (consumer / 소비자) truyền quá nhiều hiện thực (implementation / 구현) detail:

```text
innerInputId="..."
innerButtonId="..."
parentGridId="..."
parentDataListId="..."
```

Nếu một UDC cần biết ID thành phần (component / 컴포넌트) bên ngoài để hoạt động, ranh giới (boundary / 경계) đã bị đảo ngược. thành phần (component / 컴포넌트) reusable đang điều khiển bên tiêu thụ (consumer / 소비자) thay vì cung cấp năng lực (capability / 역량) cho bên tiêu thụ (consumer / 소비자).

Thay vào đó, expose sự kiện (event / 이벤트)/kết quả (result / 결과) và để page cha quyết định cập nhật mô hình (model / 모델) nào.

> **Chuyển mạch:** Trong **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **5. phương thức (method / 메서드) là command trên lớp trừu tượng (abstraction / 추상화)** tiếp nhận điểm tựa từ **4. công khai (public / 공개) thuộc tính (property / 속성) phải là cấu hình, không phải remote điều khiển (control / 제어)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. sự kiện (event / 이벤트) đảo chiều phụ thuộc (dependency / 의존성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. phương thức (method / 메서드) là command trên lớp trừu tượng (abstraction / 추상화)

Một phương thức (method / 메서드) công khai (public / 공개) nên diễn đạt hành vi theo lĩnh vực (domain / 도메인)/thành phần (component / 컴포넌트) năng lực (capability / 역량):

```javascript
employeePicker.clear();
employeePicker.openSearch();
var employee = employeePicker.getSelectedEmployee();
```

Không nên expose phương thức (method / 메서드) chỉ để mirror toàn bộ internals:

```javascript
employeePicker.getInnerInput().setValue(...);
employeePicker.getInternalDataMap().set(...);
```

Nếu bên tiêu thụ (consumer / 소비자) thường xuyên phải chui vào internals, lớp trừu tượng (abstraction / 추상화) không thực sự đóng gói gì cả.

Cấp cao (senior / 시니어) ghi chú (note / 노트): API công khai (public API / 공개 API) nhỏ thường tốt hơn API công khai (public API / 공개 API) lớn. Mỗi API công khai (public / 공개) là tính tương thích (compatibility / 호환성) promise mà dự án (project / 프로젝트) phải giữ khi UDC được refactor.

> **Chuyển mạch:** Ở chặng này của **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **6. sự kiện (event / 이벤트) đảo chiều phụ thuộc (dependency / 의존성)** tiếp nhận điểm tựa từ **5. phương thức (method / 메서드) là command trên lớp trừu tượng (abstraction / 추상화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. $p.getOptions() và initialization timing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. sự kiện (event / 이벤트) đảo chiều phụ thuộc (dependency / 의존성)

Thành phần (component / 컴포넌트) reusable không nên biết bên tiêu thụ (consumer / 소비자) sẽ làm gì sau khi người dùng (user / 사용자) chọn dữ liệu. Nó phát sự kiện (event / 이벤트) và cung cấp payload.

Conceptual luồng (flow / 흐름):

```text
UDC internal interaction
→ UDC validates internal state
→ UDC emits onemployeechange(payload)
→ consumer decides business consequence
```

Bên tiêu thụ (consumer / 소비자) có thể cập nhật (update / 업데이트) DataMap, refresh Grid hay không làm gì thêm. UDC không cần biết.

Đây là inversion of điều khiển (control / 제어) ở cấp UI. Nó giảm coupling mạnh hơn việc UDC gọi `$p.parent().scwin.someFunction()` bằng tên cố định.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **7. $p.getOptions() và initialization timing** tiếp nhận điểm tựa từ **6. sự kiện (event / 이벤트) đảo chiều phụ thuộc (dependency / 의존성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. UDC quyền sở hữu trạng thái (state ownership / 상태 소유권)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. `$p.getOptions()` và initialization timing

UDC thuộc tính (property / 속성) thường được đưa vào thành phần (component / 컴포넌트) options. Khi đọc option, cần phân biệt **construction-time cấu hình (configuration / 구성)** với **thời gian chạy (runtime / 런타임) mutable trạng thái (state / 상태)**.

Nếu một thuộc tính (property / 속성) được dùng để quyết định cấu trúc thành phần (component / 컴포넌트) khi khởi tạo, thay đổi nó sau kết xuất (render / 렌더링) có thể không tự tái cấu hình internals trừ khi UDC tự cung cấp setter tương ứng.

Do đó đặc tả hợp đồng (contract / 계약) nên nói rõ:

```text
Property nào chỉ đọc khi init?
Property nào có setter runtime?
Setter thay đổi model, style hay re-render?
```

Nếu không có distinction này, bên tiêu thụ (consumer / 소비자) dễ tưởng mọi thuộc tính (property / 속성) là reactive cấu hình (configuration / 구성).

> **Chuyển mạch:** Trong **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, sau nội dung của **7. $p.getOptions() và initialization timing**, **8. UDC quyền sở hữu trạng thái (state ownership / 상태 소유권)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **9. Controlled và uncontrolled mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. UDC quyền sở hữu trạng thái (state ownership / 상태 소유권)

Một UDC có thể có trạng thái (state / 상태) nội bộ, nhưng phải xác định trạng thái (state / 상태) nào thuộc UDC và trạng thái (state / 상태) nào thuộc page.

Ví dụ employee picker có thể sở hữu:

```text
popup opened?
current display label
internal validation message
```

Page nên sở hữu nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) chính:

```text
employeeId used in search condition
selected employee used for save
```

Nếu UDC giữ một bản sao (copy / 복사) employee đối tượng (object / 객체) và page cũng giữ một bản sao (copy / 복사) trong DataMap, hai nguồn sự thật có thể drift. Khi có binding hoặc setter, nên thiết kế một chiều dữ liệu rõ ràng.

> **Chuyển mạch:** Ở chặng này của **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **9. Controlled và uncontrolled mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **8. UDC quyền sở hữu trạng thái (state ownership / 상태 소유권)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **10. dùng chung (common / 공통) mô-đun (module / 모듈) nên thuần khi có thể** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Controlled và uncontrolled mô hình tư duy (mental model / 사고 모델)

Dù WebSquare không dùng thuật ngữ React, distinction này vẫn hữu ích.

Một thành phần (component / 컴포넌트) **self-owned** giữ giá trị (value / 값) nội bộ và bên tiêu thụ (consumer / 소비자) hỏi giá trị (value / 값) khi cần.

Một thành phần (component / 컴포넌트) **model-bound** lấy chuẩn gốc (canonical / 정본) giá trị (value / 값) từ DataCollection/binding và tương tác (interaction / 상호작용) cập nhật mô hình (model / 모델).

Cả hai đều có thể hợp lệ. Vấn đề xuất hiện khi trộn hai mô hình (model / 모델) mà không có precedence quy tắc (rule / 규칙).

Ví dụ UDC vừa bind `dmForm.employeeId`, vừa giữ `scwin.selectedEmployeeId`, lại còn cho parent set trực tiếp đầu vào (input / 입력) giá trị (value / 값). Đây là ba nguồn chuẩn (source of truth / 정본).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **10. dùng chung (common / 공통) mô-đun (module / 모듈) nên thuần khi có thể** gom các mảnh từ **9. Controlled và uncontrolled mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **11. dùng chung (common / 공통) đối tượng (object / 객체) không nên trở thành dịch vụ (service / 서비스) locator toàn ứng dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. dùng chung (common / 공통) mô-đun (module / 모듈) nên thuần khi có thể

Dùng chung (common / 공통) hàm (function / 함수) càng ít phụ thuộc phạm vi (scope / 범위)/thành phần (component / 컴포넌트) càng dễ kiểm thử (test / 테스트) và reuse.

Tốt:

```javascript
common.normalizePhone = function (value) {
    return String(value || "").replace(/[^0-9]/g, "");
};
```

Coupling cao:

```javascript
common.normalizePhone = function () {
    inputPhone.setValue(inputPhone.getValue().replace(...));
};
```

Hàm (function / 함수) thứ hai chỉ chạy nếu đúng page có đúng ID và đúng phạm vi (scope / 범위) ngữ cảnh (context / 맥락).

Quy tắc (rule / 규칙) thực tế:

```text
Nếu logic có thể nhận value và trả value → giữ pure.
Nếu cần thao tác page → để page orchestration gọi pure function rồi update component/model.
```

> **Chuyển mạch:** Trong **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **11. dùng chung (common / 공통) đối tượng (object / 객체) không nên trở thành dịch vụ (service / 서비스) locator toàn ứng dụng** tiếp nhận điểm tựa từ **10. dùng chung (common / 공통) mô-đun (module / 모듈) nên thuần khi có thể** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Wrapper API phải giữ ngữ nghĩa (semantics / 의미론) quan trọng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. dùng chung (common / 공통) đối tượng (object / 객체) không nên trở thành dịch vụ (service / 서비스) locator toàn ứng dụng

Enterprise codebase thường bắt đầu bằng `gcm`, `com`, `common` nhỏ rồi dần thành đối tượng (object / 객체) chứa mọi thứ:

```text
popup
submission
session
permission
format
DOM
Grid
business code
component lookup
navigation
```

Khi đó mọi page phụ thuộc dùng chung (common / 공통) toàn cục (global / 전역) đối tượng (object / 객체) và dùng chung (common / 공통) đối tượng (object / 객체) phụ thuộc mọi page convention. Đây là circular kiến trúc (architecture / 아키텍처).

Nên chia theo năng lực (capability / 역량) ổn định, chẳng hạn:

```text
formatting
navigation contract
submission helper
message/notification
permission adapter
```

nhưng vẫn tránh helper che mất WebSquare ngữ nghĩa (semantics / 의미론). Ví dụ wrapper Submission không nên nuốt hết lỗi (error / 오류) để caller chỉ nhận `true/false`; caller cần đủ bằng chứng (evidence / 증거) để xử lý nghiệp vụ (business / 비즈니스) thất bại (failure / 실패).

> **Chuyển mạch:** Ở chặng này của **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **12. Wrapper API phải giữ ngữ nghĩa (semantics / 의미론) quan trọng** tiếp nhận điểm tựa từ **11. dùng chung (common / 공통) đối tượng (object / 객체) không nên trở thành dịch vụ (service / 서비스) locator toàn ứng dụng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. động (dynamic / 동적) thành phần (component / 컴포넌트) creation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Wrapper API phải giữ ngữ nghĩa (semantics / 의미론) quan trọng

Giả sử dự án (project / 프로젝트) tạo:

```javascript
common.submit("sbmSave");
```

Nếu wrapper này tự disable button, tự hiện loading, tự thử lại (retry / 재시도), tự show success message và tự refresh page, nhà phát triển (developer / 개발자) không còn biết side tác động (effect / 효과) thực tế.

Wrapper tốt thường chuẩn hóa phần boilerplate nhưng vẫn expose vòng đời (lifecycle / 생명주기) rõ:

```text
before request
success transport
business result
error
finally
cancel
```

Lớp trừu tượng (abstraction / 추상화) không được đổi một giao thức (protocol / 프로토콜) nhiều trạng thái thành một boolean nghèo thông tin.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **13. động (dynamic / 동적) thành phần (component / 컴포넌트) creation** tiếp nhận điểm tựa từ **12. Wrapper API phải giữ ngữ nghĩa (semantics / 의미론) quan trọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Generator và repeated UI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. động (dynamic / 동적) thành phần (component / 컴포넌트) creation

WebSquare hỗ trợ tạo thành phần (component / 컴포넌트)/UDC động bằng API như `$p.dynamicCreate()` ở các bản dựng (build / 빌드) tương ứng. động (dynamic / 동적) UI hợp lý khi số lượng hoặc loại thành phần (component / 컴포넌트) thực sự phụ thuộc thời gian chạy (runtime / 런타임) dữ liệu (data / 데이터).

Không nên dùng động (dynamic / 동적) creation chỉ để né XML authoring. động (dynamic / 동적) thành phần (component / 컴포넌트) tăng yêu cầu quản lý:

```text
unique ID
scope ownership
event registration
binding
cleanup
render cost
```

Nếu một cấu trúc UI luôn tồn tại, declarative XML thường dễ inspect và maintain hơn.

> **Chuyển mạch:** Trong **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **14. Generator và repeated UI** tiếp nhận điểm tựa từ **13. động (dynamic / 동적) thành phần (component / 컴포넌트) creation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. động (dynamic / 동적) sự kiện (event / 이벤트) registration và cleanup** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Generator và repeated UI

Generator phù hợp khi cần lặp một UI cấu trúc (structure / 구조) theo collection. mô hình tư duy (mental model / 사고 모델) khác GridView: GridView là specialized tabular tương tác (interaction / 상호작용); Generator là repeated thành phần (component / 컴포넌트) composition linh hoạt hơn.

Khi lựa chọn, hỏi:

```text
Dữ liệu có bản chất bảng không?
Có cần sorting/editing/cell semantics không?
Hay mỗi item là một card/form complex?
```

Nếu ép mọi repeated UI vào Grid chỉ vì quen Grid API, UX và rendering kiến trúc (architecture / 아키텍처) có thể trở nên méo mó.

> **Chuyển mạch:** Ở chặng này của **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **15. động (dynamic / 동적) sự kiện (event / 이벤트) registration và cleanup** tiếp nhận điểm tựa từ **14. Generator và repeated UI** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Page template không phải thời gian chạy (runtime / 런타임) inheritance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. động (dynamic / 동적) sự kiện (event / 이벤트) registration và cleanup

Sự kiện (event / 이벤트) được khai báo trong page XML thường gắn với vòng đời (lifecycle / 생명주기) thành phần (component / 컴포넌트). sự kiện (event / 이벤트) đăng ký động bằng mã (code / 코드) cần có quyền sở hữu (ownership / 소유권) rõ.

Nếu page tạo sự kiện (event / 이벤트) trên `window`, `document` hoặc đối tượng (object / 객체) sống lâu hơn page, unload page không nhất thiết tự hiểu callback nào do nghiệp vụ (business / 비즈니스) mã (code / 코드) đăng ký.

Do đó bất kỳ động (dynamic / 동적) subscription nào cũng nên trả lời được:

```text
Ai đăng ký?
Ai sở hữu listener?
Khi nào unregister?
Nếu page mở 20 lần thì listener có thành 20 bản không?
```

Đây là điểm giao giữa reusable kiến trúc (architecture / 아키텍처) và bộ nhớ (memory / 메모리) leak.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **16. Page template không phải thời gian chạy (runtime / 런타임) inheritance** tiếp nhận điểm tựa từ **15. động (dynamic / 동적) sự kiện (event / 이벤트) registration và cleanup** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. WFrame reuse và UDC reuse khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Page template không phải thời gian chạy (runtime / 런타임) inheritance

Template giúp tạo nhiều page với cấu trúc ban đầu giống nhau, nhưng sau khi sinh nguồn (source / 소스), mỗi page là nguồn (source / 소스) riêng. Nếu muốn thay đổi hành vi (behavior / 동작) dùng chung ở thời gian chạy (runtime / 런타임), sửa template cũ không tự sửa các page đã sinh.

Vì vậy hãy tách:

```text
creation-time consistency → template/snippet
runtime shared behavior → common module/UDC/component contract
```

Không hiểu distinction này thường dẫn đến câu hỏi “tại sao tôi sửa template mà màn hình cũ không đổi?”.

> **Chuyển mạch:** Trong **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **17. WFrame reuse và UDC reuse khác nhau** tiếp nhận điểm tựa từ **16. Page template không phải thời gian chạy (runtime / 런타임) inheritance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Cross-scope phụ thuộc (dependency / 의존성) injection bằng dữ liệu (data / 데이터), không bằng đối tượng (object / 객체) internals** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. WFrame reuse và UDC reuse khác nhau

WFrame page thường là một **screen/ranh giới mô-đun (module boundary / 모듈 경계)**: có DataCollection, Submission, vòng đời (lifecycle / 생명주기), điều hướng (navigation / 내비게이션) ngữ cảnh (context / 맥락).

UDC thường là **thành phần (component / 컴포넌트) ranh giới (boundary / 경계)**: một năng lực (capability / 역량) UI nhỏ hơn với thuộc tính (property / 속성)/phương thức (method / 메서드)/sự kiện (event / 이벤트) đặc tả hợp đồng (contract / 계약).

Nếu một UDC chứa cả tìm kiếm (search / 검색) page, 8 Submission, nghiệp vụ (business / 비즈니스) permission và routing, có thể lớp trừu tượng (abstraction / 추상화) đã quá lớn. Ngược lại nếu một reusable screen được nhét vào UDC chỉ để gọi vài phương thức (method / 메서드), điều hướng (navigation / 내비게이션)/vòng đời (lifecycle / 생명주기) trở nên khó lập luận (reasoning / 추론).

> **Chuyển mạch:** Ở chặng này của **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **17. WFrame reuse và UDC reuse khác nhau** nêu điều cần giải thích; **18. Cross-scope phụ thuộc (dependency / 의존성) injection bằng dữ liệu (data / 데이터), không bằng đối tượng (object / 객체) internals** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **19. Versioning reusable thành phần (component / 컴포넌트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Cross-scope phụ thuộc (dependency / 의존성) injection bằng dữ liệu (data / 데이터), không bằng đối tượng (object / 객체) internals

Khi một reusable page cần ngữ cảnh (context / 맥락), truyền plain dữ liệu (data / 데이터) hoặc công khai (public / 공개) dịch vụ (service / 서비스) đặc tả hợp đồng (contract / 계약) hẹp tốt hơn truyền thành phần (component / 컴포넌트) instance.

Tốt:

```text
{ userId, mode, permissions }
```

Rủi ro:

```text
{ parentGrid, parentDataList, parentWindow, callbackThatTouchesEverything }
```

Plain dữ liệu (data / 데이터) làm ranh giới (boundary / 경계) dễ serialize, log, kiểm thử (test / 테스트) và replay.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **18. Cross-scope phụ thuộc (dependency / 의존성) injection bằng dữ liệu (data / 데이터), không bằng đối tượng (object / 객체) internals** nêu điều cần giải thích; **19. Versioning reusable thành phần (component / 컴포넌트)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. Anti-pattern: lớp trừu tượng (abstraction / 추상화) chỉ chuyển tên API** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Versioning reusable thành phần (component / 컴포넌트)

Một UDC dùng ở 200 page là nội bộ (internal / 내부) nền tảng (platform / 플랫폼) API. Thay đổi nhỏ cũng có blast radius lớn.

Trước khi đổi công khai (public / 공개) thuộc tính (property / 속성)/phương thức (method / 메서드)/sự kiện (event / 이벤트), phân loại:

```text
backward-compatible addition
behavioral change
contract break
visual-only change
performance change
```

Nếu buộc breaking thay đổi (change / 변경), di chuyển (migration / 마이그레이션) nên có tìm kiếm (search / 검색) chiến lược (strategy / 전략) và regression set rõ. Đừng đổi phương thức (method / 메서드) ngữ nghĩa (semantic / 의미적) nhưng giữ nguyên tên khiến old bên tiêu thụ (consumer / 소비자) chạy mà sai âm thầm.

> **Chuyển mạch:** Trong **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **20. Anti-pattern: lớp trừu tượng (abstraction / 추상화) chỉ chuyển tên API** tiếp nhận điểm tựa từ **19. Versioning reusable thành phần (component / 컴포넌트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Testing chiến lược (strategy / 전략) cho reusable tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Anti-pattern: lớp trừu tượng (abstraction / 추상화) chỉ chuyển tên API

Wrapper như:

```javascript
common.setValue = function(component, value) {
    component.setValue(value);
};
```

không tạo mô hình tư duy (mental model / 사고 모델) mới, không chuẩn hóa bất biến (invariant / 불변식), không giảm coupling. Nó chỉ thêm một indirection.

Lớp trừu tượng (abstraction / 추상화) có giá trị khi nó đóng gói chính sách (policy / 정책) hoặc bất biến (invariant / 불변식), ví dụ:

```text
normalize domain value
apply permission consistently
serialize a standard request envelope
open popup with stable result contract
```

> **Chuyển mạch:** Ở chặng này của **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **21. Testing chiến lược (strategy / 전략) cho reusable tầng (layer / 계층)** tiếp nhận điểm tựa từ **20. Anti-pattern: lớp trừu tượng (abstraction / 추상화) chỉ chuyển tên API** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. bằng chứng vận hành (production evidence / 운영 증거) khi reusable lớp trừu tượng (abstraction / 추상화) lỗi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Testing chiến lược (strategy / 전략) cho reusable tầng (layer / 계층)

Pure dùng chung (common / 공통) lô-gic (logic / 논리) có thể kiểm thử (test / 테스트) độc lập khỏi WebSquare thời gian chạy (runtime / 런타임) nếu dự án (project / 프로젝트) toolchain cho phép.

UDC cần đặc tả hợp đồng (contract / 계약) tests theo hành vi (behavior / 동작):

```text
property input → initial state
user action → emitted event payload
method call → observable component state
invalid input → validation behavior
open/close repeatedly → no duplicated listener/timer
```

Không nên kiểm thử (test / 테스트) UDC chỉ bằng DOM snapshot. công khai (public / 공개) hành vi (behavior / 동작) mới là tính tương thích (compatibility / 호환성) surface.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **21. Testing chiến lược (strategy / 전략) cho reusable tầng (layer / 계층)** nêu điều cần giải thích; **22. bằng chứng vận hành (production evidence / 운영 증거) khi reusable lớp trừu tượng (abstraction / 추상화) lỗi** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **23. trường hợp (case / 사례) study: EmployeePicker** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. bằng chứng vận hành (production evidence / 운영 증거) khi reusable lớp trừu tượng (abstraction / 추상화) lỗi

Khi một dùng chung (shared / 공유) UDC lỗi ở 30 màn hình, sửa nhanh trực tiếp UDC có thể có blast radius cực lớn. Trước hết cần phân biệt:

```text
UDC internal defect?
consumer dùng sai contract?
engine build behavior khác?
CSS/theme override?
shared config drift?
```

Bằng chứng (evidence / 증거) nên gồm page instance, UDC phiên bản (version / 버전)/nguồn (source / 소스) băm (hash / 해시), engine bản dựng (build / 빌드), option payload, emitted sự kiện (event / 이벤트) và reproduction tối thiểu.

> **Chuyển mạch:** Trong **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **22. bằng chứng vận hành (production evidence / 운영 증거) khi reusable lớp trừu tượng (abstraction / 추상화) lỗi** cho ta quy tắc; **23. trường hợp (case / 사례) study: EmployeePicker** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **24. Checklist lập luận (reasoning / 추론) trước khi tạo dùng chung (common / 공통) lớp trừu tượng (abstraction / 추상화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. trường hợp (case / 사례) study: EmployeePicker

Giả sử nhiều màn hình cần chọn nhân viên. Thiết kế tốt có thể như sau.

UDC nhận thuộc tính (property / 속성) `allowInactive` và `requiredDepartment`. Nội bộ nó có đầu vào (input / 입력) hiển thị tên, hidden/mô hình (model / 모델) trạng thái (state / 상태) giữ `employeeId`, Trigger mở popup và kiểm tra hợp lệ (validation / 검증) message. Popup nhận filter bằng plain dữ liệu (data / 데이터). Khi người dùng (user / 사용자) chọn, UDC cập nhật trạng thái (state / 상태) và phát `onemployeechange` với payload `{employeeId, employeeName, departmentId}`.

Page bên tiêu thụ (consumer / 소비자) bind kết quả (result / 결과) cần thiết vào `dmForm` trong handler sự kiện (event / 이벤트). Page không biết ID đầu vào (input / 입력) nội bộ của UDC; UDC không biết `dmForm` của page.

Nếu sau này UI đổi từ popup sang autocomplete server-side, bên tiêu thụ (consumer / 소비자) đặc tả hợp đồng (contract / 계약) có thể giữ nguyên. Đó là dấu hiệu lớp trừu tượng (abstraction / 추상화) ranh giới (boundary / 경계) tốt.

> **Chuyển mạch:** Ở chặng này của **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **23. trường hợp (case / 사례) study: EmployeePicker** cho ta quy tắc; **24. Checklist lập luận (reasoning / 추론) trước khi tạo dùng chung (common / 공통) lớp trừu tượng (abstraction / 추상화)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **25. liên kết (connection / 연결) với các chapter khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Checklist lập luận (reasoning / 추론) trước khi tạo dùng chung (common / 공통) lớp trừu tượng (abstraction / 추상화)

Trước khi tạo helper/UDC mới, hãy trả lời:

```text
Shared invariant là gì?
Owner của state là ai?
Public input/output là gì?
Lifecycle bắt đầu/kết thúc ở đâu?
Consumer có cần biết internal ID không?
Có hidden dependency vào parent/top scope không?
Có thể log/test contract độc lập không?
Breaking change sẽ ảnh hưởng bao nhiêu consumer?
```

Nếu chưa trả lời được, lớp trừu tượng (abstraction / 추상화) có thể đang được tạo quá sớm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, sau nội dung của **24. Checklist lập luận (reasoning / 추론) trước khi tạo dùng chung (common / 공통) lớp trừu tượng (abstraction / 추상화)**, **25. liên kết (connection / 연결) với các chapter khác** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Nguồn chính thức nên đối chiếu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. liên kết (connection / 연결) với các chapter khác

Phạm vi (scope / 범위) và WFrame ranh giới (boundary / 경계) được giải thích ở [04 — Scope, WFrame, Popup & SPA](04_scope_wframe_popup_spa.md). dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약) và Submission nằm ở [03 — DataCollection & Submission](03_data_collection_submission.md). bộ nhớ (memory / 메모리) leak do động (dynamic / 동적) listener và long-lived SPA được đào sâu ở [06 — Debugging, Performance, Security & Production](06_debugging_performance_security.md).

JavaScript closure/mô-đun (module / 모듈) ngữ nghĩa (semantics / 의미론) không lặp lại ở đây; xem [JavaScript Intermediate](../javascript/javascript_intermediate.md) và [JavaScript Senior](../javascript/javascript_senior.md).

> **Chuyển mạch:** Trong **08 — Reusable kiến trúc (architecture / 아키텍처), UDC & dùng chung (common / 공통) Modules**, **25. liên kết (connection / 연결) với các chapter khác** đã nêu tiêu chí phân biệt, còn **Nguồn chính thức nên đối chiếu** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Nguồn chính thức nên đối chiếu

WebSquare5 SP5 Development Guide — UDC 생성: `https://docs1.inswave.com/sp5_user_guide/0825289df4df8d45`

WebSquare5 SP5 Development Guide — 화면 그리기 / tài nguyên (resource / 자원) types: `https://docs1.inswave.com/sp5_user_guide/740ba8f1ef906f13`

API và hành vi (behavior / 동작) cụ thể của `$p.dynamicCreate()`, Generator, thuộc tính (property / 속성)/phương thức (method / 메서드)/sự kiện (event / 이벤트) phải được kiểm tra theo engine bản dựng (build / 빌드) dự án (project / 프로젝트) đang chạy.

> **Bàn giao:** Sau **Nguồn chính thức nên đối chiếu**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
