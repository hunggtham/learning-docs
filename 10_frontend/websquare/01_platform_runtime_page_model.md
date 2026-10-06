# 01 — nền tảng (platform / 플랫폼), thời gian chạy (runtime / 런타임) & Page mô hình (model / 모델)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **01 — nền tảng (platform / 플랫폼), thời gian chạy (runtime / 런타임) & Page mô hình (model / 모델)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. WebSquare không phải là “JavaScript có thêm vài API”** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Từ nguồn (source / 소스) đến thời gian chạy (runtime / 런타임): XML → W-Pack → Engine → trình duyệt (browser / 브라우저)** để đối chiếu nhận định với dữ liệu và nguồn. Mạch này nối platform runtime với page model và lifecycle, để xác định screen được tạo, giữ state và hủy ở đâu.

## 1. WebSquare không phải là “JavaScript có thêm vài API”

Cách dễ hiểu sai nhất là nhìn một tệp (file / 파일) WebSquare, thấy JavaScript trong `<script>` rồi kết luận rằng đây chỉ là một trang web bình thường có thêm thư viện thành phần (component / 컴포넌트). Cách nhìn đó bỏ qua phần quan trọng nhất: WebSquare cung cấp một **thời gian chạy (runtime / 런타임) quản lý page** (page runtime / 페이지 런타임). thời gian chạy (runtime / 런타임) này tạo thành phần (component / 컴포넌트) đối tượng (object / 객체), quản lý page vòng đời (lifecycle / 생명주기), binding, mô hình dữ liệu (data model / 데이터 모델), communication đối tượng (object / 객체), frame/phạm vi (scope / 범위) và rendering lớp trừu tượng (abstraction / 추상화).

JavaScript vẫn là JavaScript. Closure, `this`, vòng lặp sự kiện (event loop / 이벤트 루프), Promise, exception, đối tượng (object / 객체) tham chiếu (reference / 참조) và garbage collection vẫn tuân theo thời gian chạy (runtime / 런타임) của trình duyệt (browser / 브라우저). Nhưng đối tượng (object / 객체) mà mã (code / 코드) thao tác thường không phải DOM nút (node / 노드) trực tiếp. `input1`, `gridView1`, `dataList1` hay `submission1` là đối tượng (object / 객체) do WebSquare Engine quản lý. Điều này tạo ra hai tầng ngữ nghĩa (semantics / 의미론) chồng lên nhau: ngữ nghĩa (semantics / 의미론) của JavaScript và ngữ nghĩa (semantics / 의미론) của khung phần mềm (framework / 프레임워크).

Nếu một bug nằm ở closure hoặc async thứ tự (ordering / 순서), học thêm API WebSquare không giải quyết được. Ngược lại, nếu bug do page đang ở WFrame khác phạm vi (scope / 범위), chỉ biết JavaScript thuần cũng chưa đủ. cấp cao (senior / 시니어) nhà phát triển (developer / 개발자) phải xác định đúng tầng trước khi sửa.

> **Nối mạch:** Trong **01 — nền tảng (platform / 플랫폼), thời gian chạy (runtime / 런타임) & Page mô hình (model / 모델)**, **1. WebSquare không phải là “JavaScript có thêm vài API”** đặt vấn đề; **2. Từ nguồn (source / 소스) đến thời gian chạy (runtime / 런타임): XML → W-Pack → Engine → trình duyệt (browser / 브라우저)** đối chiếu bằng chứng, rồi **3. Studio và Engine giải quyết hai nhiệm vụ khác nhau** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. Từ nguồn (source / 소스) đến thời gian chạy (runtime / 런타임): XML → W-Pack → Engine → trình duyệt (browser / 브라우저)

WebSquare Studio cho phép author màn hình dưới dạng XML. XML mô tả thành phần (component / 컴포넌트) cây (tree / 트리), DataCollection, Submission, workflow và script. Trong WebSquare5 SP5, W-Pack có thể chuyển page XML thành JavaScript đặt trong `_wpack_`. trình duyệt (browser / 브라우저) gọi page theo URL, nhưng engine có thể thực sự tải sản phẩm tạo ra (artifact / 산출물) JavaScript đã được bản dựng (build / 빌드) để kết xuất (render / 렌더링) nhanh hơn.

Mô hình tư duy (mental model / 사고 모델) nên là:

```text
page.xml
   │
   ├─ component declaration
   ├─ dataCollection
   ├─ submission
   └─ script
   │
   ▼
W-Pack / build transformation
   │
   ▼
page JavaScript artifact
   │
   ▼
WebSquare Engine
   │
   ├─ create component objects
   ├─ create page/scope objects
   ├─ connect bindings
   ├─ install event handlers
   └─ render DOM
   │
   ▼
Browser
```

Điều này giải thích một hiện tượng thường làm người mới bối rối: nguồn (source / 소스) tệp (file / 파일) họ sửa là XML nhưng dấu vết ngăn xếp (stack trace / 스택 트레이스), mạng (network / 네트워크) tab hoặc thời gian chạy (runtime / 런타임) đối tượng (object / 객체) lại cho thấy JavaScript. Đó không phải hai ứng dụng khác nhau. XML là authoring biểu diễn (representation / 표현); JavaScript mới là biểu diễn (representation / 표현) thuận tiện cho thời gian chạy (runtime / 런타임).

Đọc thêm nền XML tại [XML Beginner](../xml/xml_01_beginner_detailed.md). thư viện (library / 라이브러리) này không lặp lại không gian tên (namespace / 네임스페이스), element cây (tree / 트리) hay well-formed XML.

> **Nối mạch:** Ở chặng này của **01 — nền tảng (platform / 플랫폼), thời gian chạy (runtime / 런타임) & Page mô hình (model / 모델)**, **2. Từ nguồn (source / 소스) đến thời gian chạy (runtime / 런타임): XML → W-Pack → Engine → trình duyệt (browser / 브라우저)** đặt vấn đề; **3. Studio và Engine giải quyết hai nhiệm vụ khác nhau** đối chiếu bằng chứng, rồi **4. Page WebSquare gồm những lớp gì?** mở rộng hệ quả hoặc giới hạn liên quan.

## 3. Studio và Engine giải quyết hai nhiệm vụ khác nhau

WebSquare Studio là môi trường phát triển (development environment / 개발 환경). Nó cung cấp thiết kế (design / 설계) view, nguồn (source / 소스) view, palette, thuộc tính (property / 속성) editor, preview, gỡ lỗi (debug / 디버그) hỗ trợ (support / 지원) và tooling để tạo page.

WebSquare Engine là thời gian chạy (runtime / 런타임) chạy ứng dụng. Engine đọc hoặc tải sản phẩm tạo ra (artifact / 산출물) của page, dựng thành phần (component / 컴포넌트), điều phối vòng đời (lifecycle / 생명주기) và cho phép API WebSquare hoạt động trong trình duyệt (browser / 브라우저).

Việc tách hai khái niệm này giúp tránh một lỗi lập luận (reasoning / 추론) phổ biến: “Studio hiển thị đúng” không đồng nghĩa “thời gian chạy (runtime / 런타임) môi trường vận hành (production / 운영 환경) chắc chắn đúng”. Studio có thể dùng cấu hình cục bộ (local / 로컬), tài nguyên (resource / 자원) đường dẫn (path / 경로), engine bản dựng (build / 빌드) hoặc mock khác với môi trường tích hợp. Khi lỗi chỉ xảy ra trên máy chủ (server / 서버), hãy kiểm tra thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거) chứ không suy từ màn hình thiết kế (design / 설계).

> **Nối mạch:** Studio tạo/biên tập artifact còn Engine thực thi runtime; Page gom các lớp đó thành lifecycle và scope rõ. Component object tiếp theo phân biệt WebSquare object model với DOM element.

## 4. Page WebSquare gồm những lớp gì?

Một page thường có thể hình dung thành bốn vùng lô-gic (logic / 논리).

Phần **UI declaration** mô tả thành phần (component / 컴포넌트) như đầu vào (input / 입력), Button, GridView, Group, WFrame. Đây là cấu trúc hiển thị và tương tác (interaction / 상호작용) surface.

Phần **DataCollection** mô tả dữ liệu client-side. `DataMap` phù hợp với một bản ghi hoặc một nhóm key/giá trị (value / 값); `DataList` phù hợp với nhiều dòng; `LinkedDataList` cung cấp view đã filter/sort từ DataList.

Phần **Submission** mô tả giao tiếp với máy chủ (server / 서버): endpoint, yêu cầu (request / 요청) tham chiếu (reference / 참조), phản hồi (response / 응답) mục tiêu (target / 대상) và vòng đời (lifecycle / 생명주기) của yêu cầu (request / 요청).

Phần **script** chứa page hành vi (behavior / 동작). Trong page theo phạm vi (scope / 범위) mô hình (model / 모델) hiện đại, hàm (function / 함수) thường nằm dưới `scwin`.

Một ví dụ rút gọn có dạng tư duy như sau:

```xml
<xf:model>
    <w2:dataCollection>
        <!-- dmSearch, dlResult ... -->
    </w2:dataCollection>
    <!-- sbmSearch ... -->
</xf:model>

<script type="text/javascript" lazy="false">
    scwin.btnSearch_onclick = function () {
        scwin.search();
    };
</script>

<!-- UI components -->
```

Đừng học thuộc markup này như template. Điều quan trọng là hiểu phụ thuộc (dependency / 의존성): **UI sự kiện (event / 이벤트) → page hàm (function / 함수) → máy khách (client / 클라이언트) mô hình dữ liệu (data model / 데이터 모델) → Submission → máy chủ (server / 서버) → phản hồi (response / 응답) mục tiêu (target / 대상) → bound UI**.

> **Nối mạch:** Page gồm nhiều lớp runtime; component object vì vậy không đồng nhất với DOM element, và ID tiếp theo phải được hiểu theo ownership của page.

## 5. thành phần (component / 컴포넌트) đối tượng (object / 객체) khác DOM element

Giả sử page có đầu vào (input / 입력) ID `inputName`. mã (code / 코드) có thể gọi:

```javascript
inputName.setValue("Kim");
var value = inputName.getValue();
```

`inputName` ở đây là thành phần (component / 컴포넌트) API đối tượng (object / 객체) do WebSquare expose, không nên mặc định coi nó là raw DOM `<input>`. thành phần (component / 컴포넌트) có thể có format, kiểm tra hợp lệ (validation / 검증), binding, sự kiện (event / 이벤트) mediation và nội bộ (internal / 내부) markup riêng. Một thành phần (component / 컴포넌트) nhìn như một đầu vào (input / 입력) đơn giản có thể kết xuất (render / 렌더링) thành nhiều DOM nút (node / 노드) hoặc thay đổi cấu trúc giữa engine bản dựng (build / 빌드).

Hệ quả là mã (code / 코드) môi trường vận hành (production / 운영 환경) nên ưu tiên **thành phần (component / 컴포넌트) API** thay vì đi xuyên vào DOM nội bộ bằng selector. DOM hacking có ba rủi ro:

Thứ nhất, bạn có thể thay đổi phần hiển thị nhưng không thay đổi khung phần mềm (framework / 프레임워크) trạng thái (state / 상태). UI nhìn đúng nhưng `getValue()` hoặc Submission vẫn lấy dữ liệu cũ.

Thứ hai, nội bộ (internal / 내부) DOM cấu trúc (structure / 구조) không phải công khai (public / 공개) đặc tả hợp đồng (contract / 계약). Engine cập nhật (update / 업데이트) có thể thay lớp (class / 클래스) hoặc nesting.

Thứ ba, sự kiện (event / 이벤트) được khung phần mềm (framework / 프레임워크) quản lý có thể không chạy nếu bạn sửa DOM theo đường tắt.

Chỉ nên thao tác DOM trực tiếp khi API công khai (public API / 공개 API) không đáp ứng yêu cầu và bạn đã xác nhận đặc tả hợp đồng (contract / 계약), kiểm thử (test / 테스트) regression và upgrade rủi ro (risk / 위험).

> **Nối mạch:** Ở chặng này của **01 — nền tảng (platform / 플랫폼), thời gian chạy (runtime / 런타임) & Page mô hình (model / 모델)**, **5. thành phần (component / 컴포넌트) đối tượng (object / 객체) khác DOM element** đặt đầu vào cho **6. ID không chỉ là chuỗi để truy vấn (query / 쿼리) DOM**, rồi **7. scwin: không gian tên (namespace / 네임스페이스) của page hành vi (behavior / 동작)** mở rộng hệ quả hoặc giới hạn liên quan.

## 6. ID không chỉ là chuỗi để truy vấn (query / 쿼리) DOM

Trong WebSquare, ID là cách thời gian chạy (runtime / 런타임) định danh thành phần (component / 컴포넌트) trong phạm vi (scope / 범위). Khi phạm vi (scope / 범위)/WFrame được dùng, engine có thể thay đổi ID vật lý ở DOM để tránh collision, trong khi script vẫn truy cập bằng logical ID đã khai báo.

Do đó một CSS quy tắc (rule / 규칙) dựa vào raw `#id` có thể dễ vỡ hơn class-based styling trong môi trường WFrame. Nếu cùng một page được mở hai lần ở hai frame, logical thành phần (component / 컴포넌트) ID có thể giống nhau nhưng mỗi phạm vi (scope / 범위) vẫn tách biệt.

Đây là lý do phải tách ba khái niệm:

```text
logical component ID
        ≠
physical DOM id
        ≠
page Scope identity
```

Nếu không phân biệt ba lớp này, nhà phát triển (developer / 개발자) rất dễ gặp bug “console tìm thấy hai id”, “CSS không ăn trong popup”, hoặc “gọi thành phần (component / 컴포넌트) cùng tên nhưng ra màn hình khác”.

> **Nối mạch:** Đặt trong câu hỏi lớn của **01 — nền tảng (platform / 플랫폼), thời gian chạy (runtime / 런타임) & Page mô hình (model / 모델)**, **6. ID không chỉ là chuỗi để truy vấn (query / 쿼리) DOM** đặt đầu vào cho **7. scwin: không gian tên (namespace / 네임스페이스) của page hành vi (behavior / 동작)**, rồi **8. $p: utility hiểu page phạm vi (scope / 범위)** mở rộng hệ quả hoặc giới hạn liên quan.

## 7. `scwin`: không gian tên (namespace / 네임스페이스) của page hành vi (behavior / 동작)

Trong Scope-based page, WebSquare thường dùng `scwin` làm phạm vi (scope / 범위) variable. Thay vì tạo hàm (function / 함수) toàn cục (global / 전역):

```javascript
function search() {
    // ...
}
```

page viết:

```javascript
scwin.search = function () {
    // ...
};
```

Về mặt lập luận (reasoning / 추론), `scwin` giống một không gian tên (namespace / 네임스페이스) đại diện cho hành vi (behavior / 동작) của page hiện tại. Nó giảm collision giữa nhiều page cùng được mount trong một shell hoặc WFrame cấu trúc (structure / 구조).

Một mẫu (pattern / 패턴) tốt:

```javascript
scwin.btnSearch_onclick = function () {
    scwin.search();
};

scwin.search = function () {
    if (!scwin.validateSearchCondition()) {
        return;
    }

    $p.executeSubmission(sbmSearch);
};

scwin.validateSearchCondition = function () {
    return inputKeyword.getValue().trim().length >= 2;
};
```

Handler chỉ đóng vai trò adapter từ UI sự kiện (event / 이벤트) sang page hành vi (behavior / 동작). kiểm tra hợp lệ (validation / 검증) và orchestration có tên riêng, có thể đọc và kiểm thử (test / 테스트) lập luận (reasoning / 추론) dễ hơn.

Anti-pattern thường thấy là dồn hàng trăm dòng vào `onclick`, vừa đọc giá trị, sửa 10 thành phần (component / 컴포넌트), duyệt grid, gọi nhiều submission và xử lý popup. mã (code / 코드) kiểu đó biến sự kiện (event / 이벤트) thành một “god hàm (function / 함수)”.

> **Nối mạch:** `scwin` giữ page behavior local; `$p` cung cấp utility theo scope, nên lifecycle tiếp theo phải xét đúng page boundary thay vì gọi code trong vacuum.

## 8. `$p`: utility hiểu page phạm vi (scope / 범위)

WebSquare có họ utility trước đây thường gắn với `$w`; trong phạm vi (scope / 범위) mô hình (model / 모델), các utility page-aware được expose qua `$p`. mô hình tư duy (mental model / 사고 모델) thực dụng là: `$p` đại diện cho các WebSquare thao tác (operation / 연산) cần biết **page hiện tại đang ở phạm vi (scope / 범위) nào**.

Ví dụ:

```javascript
$p.executeSubmission(sbmSearch);
$p.openPopup("/user/detail.xml", options);
var parentScope = $p.parent();
var topScope = $p.top();
```

Điểm quan trọng không phải nhớ `$p` có bao nhiêu phương thức (method / 메서드). Điểm quan trọng là khi một utility cần resolve thành phần (component / 컴포넌트)/page relative to hiện tại (current / 현재) phạm vi (scope / 범위), `$p` giúp khung phần mềm (framework / 프레임워크) giữ ngữ cảnh (context / 맥락) đó.

Chapter [04 — Scope, WFrame, Popup & SPA](04_scope_wframe_popup_spa.md) sẽ đào sâu `$p.parent()`, `$p.main()`, `$p.top()`, `$p.getWindow()` và dạng thất bại (failure mode / 실패 모드) khi đi sai phạm vi (scope / 범위).

> **Nối mạch:** Ở chặng này của **01 — nền tảng (platform / 플랫폼), thời gian chạy (runtime / 런타임) & Page mô hình (model / 모델)**, **8. $p: utility hiểu page phạm vi (scope / 범위)** đặt đầu vào cho **9. Page vòng đời (lifecycle / 생명주기): mã (code / 코드) không chạy trong vacuum**, rồi **10. sự kiện (event / 이벤트) trong WebSquare vẫn dựa trên event-driven programming** mở rộng hệ quả hoặc giới hạn liên quan.

## 9. Page vòng đời (lifecycle / 생명주기): mã (code / 코드) không chạy trong vacuum

Một page phải trải qua tải (load / 로드), script initialization, thành phần (component / 컴포넌트) creation/kết xuất (render / 렌더링), dữ liệu (data / 데이터) binding và page events. WebSquare có các cấu hình liên quan đến thứ tự script như `scriptPrecedence`, `postDrawMode` và JavaScript `lazy` hành vi (behavior / 동작). Chính vì vậy mã (code / 코드) chạy “sớm quá” có thể không nhìn thấy thành phần (component / 컴포넌트), còn mã (code / 코드) chạy “muộn quá” có thể gây flash hoặc duplicate yêu cầu (request / 요청).

Đừng giải quyết vòng đời (lifecycle / 생명주기) bug bằng `setTimeout(..., 100)` trừ khi hết thời gian chờ (timeout / 타임아웃) chính là nghiệp vụ (business / 비즈니스) yêu cầu (requirement / 요구사항). hết thời gian chờ (timeout / 타임아웃) chỉ che race điều kiện (condition / 조건). Câu hỏi đúng là:

```text
Object này được tạo ở lifecycle phase nào?
Code của tôi chạy ở phase nào?
Có event/callback chính thức nào biểu diễn readiness không?
```

Nếu cần delay vì page con chưa tải (load / 로드), hãy dùng sự kiện (event / 이벤트)/tải (load / 로드) đặc tả hợp đồng (contract / 계약) của WFrame/Tab/Popup tương ứng thay vì đoán thời gian.

> **Nối mạch:** Đặt trong câu hỏi lớn của **01 — nền tảng (platform / 플랫폼), thời gian chạy (runtime / 런타임) & Page mô hình (model / 모델)**, **9. Page vòng đời (lifecycle / 생명주기): mã (code / 코드) không chạy trong vacuum** đặt đầu vào cho **10. sự kiện (event / 이벤트) trong WebSquare vẫn dựa trên event-driven programming**, rồi **11. trạng thái (state / 상태) nằm ở đâu?** mở rộng hệ quả hoặc giới hạn liên quan.

## 10. sự kiện (event / 이벤트) trong WebSquare vẫn dựa trên event-driven programming

Button click, đầu vào (input / 입력) thay đổi (change / 변경), DataList cell thay đổi (change / 변경), Submission done hay WFrame tải (load / 로드) đều là sự kiện (event / 이벤트). khung phần mềm (framework / 프레임워크) đăng ký callback và gọi nó khi điều kiện xảy ra.

Mô hình tư duy (mental model / 사고 모델) từ JavaScript vẫn áp dụng:

```text
user action/network result
        │
        ▼
event emitted
        │
        ▼
handler runs on JS execution context
        │
        ├─ read state
        ├─ mutate framework state
        ├─ schedule async work
        └─ return
```

Nếu handler gọi Submission asynchronous, handler không “đứng chờ” máy chủ (server / 서버). phản hồi (response / 응답) callback chạy sau. Vì vậy đoạn mã (code / 코드) đặt ngay sau `executeSubmission()` không được giả định rằng phản hồi (response / 응답) đã có.

Đây là cùng một vấn đề async thứ tự (ordering / 순서) được giải thích sâu ở [JavaScript Intermediate](../javascript/javascript_intermediate.md), chỉ khác đối tượng (object / 객체) phát sự kiện (event / 이벤트) là WebSquare thời gian chạy (runtime / 런타임).

> **Nối mạch:** Event-driven programming giải thích tín hiệu đi vào Page; **11** truy tìm state được giữ ở đâu, rồi **12. Binding** cho thấy dữ liệu đổi lập luận và cập nhật giao diện như thế nào.

## 11. trạng thái (state / 상태) nằm ở đâu?

Một màn hình enterprise có thể có ít nhất bốn loại trạng thái (state / 상태):

**thành phần (component / 컴포넌트) trạng thái (state / 상태)**: giá trị (value / 값), selected chỉ mục (index / 인덱스), disabled/readOnly, visible trạng thái (state / 상태) của UI thành phần (component / 컴포넌트).

**DataCollection trạng thái (state / 상태)**: dữ liệu nghiệp vụ (business / 비즈니스) phía máy khách (client / 클라이언트), ví dụ tìm kiếm (search / 검색) điều kiện (condition / 조건), danh sách người dùng (user / 사용자), row status.

**Page trạng thái (state / 상태)**: biến trong `scwin`, flag loading, hiện tại (current / 현재) chế độ (mode / 모드), temporary ngữ cảnh (context / 맥락).

**máy chủ (server / 서버) trạng thái (state / 상태)**: cơ sở dữ liệu (database / 데이터베이스), session, workflow status thật.

Bug thường xuất hiện khi một giá trị tồn tại ở nhiều nơi nhưng không có nguồn chuẩn (source of truth / 정본) rõ ràng. Ví dụ nhà phát triển (developer / 개발자) giữ `selectedUserId` trong `scwin`, đồng thời trong hidden đầu vào (input / 입력) và trong DataMap. Ba bản sao có thể lệch nhau.

Nguyên tắc môi trường vận hành (production / 운영 환경): chọn nguồn chuẩn (source of truth / 정본) theo mục đích. Dữ liệu cần submit nên sống trong DataCollection phù hợp. UI thành phần (component / 컴포넌트) nên phản ánh mô hình (model / 모델) qua binding khi có thể. Biến `scwin` phù hợp cho transient orchestration trạng thái (state / 상태), không nên biến thành một cơ sở dữ liệu (database / 데이터베이스) thu nhỏ.

> **Nối mạch:** Khi đã xác định state và binding, **13. Error taxonomy** phân loại lỗi theo lớp dữ liệu, event hay runtime trước khi chọn cách sửa.

## 12. Binding thay đổi cách lập luận (reasoning / 추론)

Nếu đầu vào (input / 입력) được bind với DataMap, gọi `inputName.setValue(...)` có thể dẫn đến mô hình (model / 모델) cập nhật (update / 업데이트) theo binding đặc tả hợp đồng (contract / 계약), và mô hình (model / 모델) cập nhật (update / 업데이트) cũng có thể phản ánh ngược ra UI. Vì vậy khi gỡ lỗi (debug / 디버그), không chỉ nhìn thành phần (component / 컴포넌트).

Hãy hỏi:

```text
Input này có bind DataMap không?
Grid này bind DataList nào?
Thay đổi đang xảy ra ở UI, model hay cả hai?
Event nào được phát khi binding cập nhật?
```

Chapter 02 đi sâu vấn đề này.

> **Nối mạch:** Phân loại lỗi làm lộ nơi abstraction của binding bị rò; **14** dùng các điểm rò đó để chọn mức can thiệp phù hợp thay vì vá ngẫu nhiên.

## 13. lỗi (error / 오류) taxonomy: phân loại trước khi sửa

Một lỗi “bấm tìm kiếm (search / 검색) không ra dữ liệu” có thể thuộc nhiều nhóm hoàn toàn khác nhau:

```text
UI event không fire
→ handler sai tên / disabled / overlay

handler fire nhưng validation return
→ page logic

Submission không chạy
→ object/scope/config

request đi nhưng 4xx/5xx
→ endpoint/auth/server

response 200 nhưng target rỗng
→ response schema/mapping

DataList có data nhưng Grid rỗng
→ binding/grid rendering/filter
```

Chẩn đoán tốt là đi theo chuỗi xử lý (pipeline / 파이프라인) và thu bằng chứng (evidence / 증거) ở từng ranh giới (boundary / 경계), không sửa ngẫu nhiên từng API.

> **Nối mạch:** Sau khi nhận diện abstraction leak, **15. Bài tập lập luận** buộc người học truy nguyên symptom → state → binding → runtime bằng một case cụ thể.

## 14. cấp cao (senior / 시니어) ghi chú (note / 노트): lớp trừu tượng (abstraction / 추상화) leak là bình thường, nhưng phải biết lúc nào xảy ra

Khung phần mềm (framework / 프레임워크) cố che DOM, AJAX, serialization và frame management để nhà phát triển (developer / 개발자) làm việc ở mức lớp trừu tượng (abstraction / 추상화) cao hơn. Nhưng lớp trừu tượng (abstraction / 추상화) không bao giờ kín hoàn toàn. Khi có hiệu năng (performance / 성능) issue, bảo mật (security / 보안) issue hay browser-specific bug, bạn phải đi xuống tầng thấp hơn.

Một cấp cao (senior / 시니어) WebSquare nhà phát triển (developer / 개발자) cần di chuyển được giữa ba mức:

```text
business screen
↕
WebSquare abstraction
↕
JavaScript / browser / HTTP / DOM
```

Chỉ biết tầng trên thì gỡ lỗi (debug / 디버그) khó. Chỉ biết tầng dưới thì dễ chống lại khung phần mềm (framework / 프레임워크) và tạo mã (code / 코드) fragile. Kỹ năng quan trọng là biết **khi nào nên ở trong công khai (public / 공개) lớp trừu tượng (abstraction / 추상화), khi nào cần quan sát internals, và khi nào tuyệt đối không phụ thuộc internals**.

> **Nối mạch:** Case đã kiểm tra được mental model; **16. Kết nối sang chapter tiếp theo** bàn giao từ Page runtime sang workflow và orchestration, nơi state chịu thêm điều phối.

## 15. Bài tập lập luận (reasoning / 추론)

Giả sử một page có `inputName`, `dmUser`, `sbmSaveUser` và nút Save. `inputName` bind với `dmUser.name`. Khi người dùng nhập tên và bấm Save, máy chủ (server / 서버) đôi lúc nhận tên cũ.

Đừng sửa ngay. Hãy xây giả thuyết theo thứ tự:

1. Giá trị hiển thị của đầu vào (input / 입력) có khác actual giá trị (value / 값) do format/lần ghi nhận (commit / 커밋) timing không?
2. Binding có lần ghi nhận (commit / 커밋) trước sự kiện (event / 이벤트) click không?
3. Submission tham chiếu (reference / 참조) lấy từ đúng DataMap không?
4. Có mã (code / 코드) khác ghi đè `dmUser.name` trước submit không?
5. Có duplicate/racing submission không?
6. yêu cầu (request / 요청) payload trong mạng (network / 네트워크) tab thực tế chứa giá trị nào?

Bước 6 rất quan trọng. Nếu payload đã đúng mà máy chủ (server / 서버) vẫn lưu sai, lỗi không còn nằm ở WebSquare UI. Nếu payload sai, tiếp tục truy ngược mô hình (model / 모델) và sự kiện (event / 이벤트) thứ tự (ordering / 순서). Đây là cách gỡ lỗi (debug / 디버그) theo bằng chứng (evidence / 증거) thay vì theo cảm giác.

> **Nối mạch:** Chapter này khép ở runtime Page; phần kế tiếp mở rộng cùng mental model sang workflow, data state và error architecture của WebSquare.

## 16. Kết nối sang chapter tiếp theo

Sau chapter này, bạn nên giải thích được vì sao XML chỉ là authoring nguồn (source / 소스), vì sao thành phần (component / 컴포넌트) đối tượng (object / 객체) không nên đồng nhất với DOM, `scwin` giải quyết collision gì, `$p` cần phạm vi (scope / 범위) ngữ cảnh (context / 맥락) ra sao, và tại sao trạng thái (state / 상태) duplication là nguồn bug lớn.

Tiếp theo: [02 — Components, Events & Data Binding](02_components_events_binding.md).

> **Bàn giao:** Sau **16. Kết nối sang chapter tiếp theo**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
