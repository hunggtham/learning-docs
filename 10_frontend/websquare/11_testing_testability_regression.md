# 11 — Testing, Testability & Regression kỹ thuật (engineering / 엔지니어링)

> **Mạch đọc:** Đặt **11 — Testing, Testability & Regression kỹ thuật (engineering / 엔지니어링)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. kiểm thử (test / 테스트) không phải là “click được”** sang **2. Testing portfolio theo ranh giới (boundary / 경계)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


WebSquare ứng dụng (application / 애플리케이션) thường được kiểm thử bằng cách mở màn hình, nhập dữ liệu rồi quan sát kết quả. Cách đó cần thiết nhưng không đủ cho một hệ thống enterprise lớn. Khi số page, WFrame, Submission, UDC và Grid tăng lên, kiểm thử thủ công không còn trả lời được câu hỏi quan trọng nhất: **thay đổi này đã phá đặc tả hợp đồng (contract / 계약) nào, ở tầng (layer / 계층) nào, và bằng chứng nào cho thấy hành vi (behavior / 동작) vẫn đúng?**

Chapter này không cố ép WebSquare vào một testing khung phần mềm (framework / 프레임워크) cụ thể. mô hình tư duy (mental model / 사고 모델) quan trọng hơn công cụ (tool / 도구): tách nghiệp vụ (business / 비즈니스) lập luận (reasoning / 추론) khỏi khung phần mềm (framework / 프레임워크) side tác động (effect / 효과), xác định observable đặc tả hợp đồng (contract / 계약), kiểm soát async/vòng đời (lifecycle / 생명주기) và xây regression suite theo rủi ro (risk / 위험). Playwright, Selenium hay một runner nội bộ chỉ là phương tiện thực thi những đặc tả hợp đồng (contract / 계약) đó.

> Prerequisite: [03 — DataCollection & Submission](03_data_collection_submission.md), [04 — Scope, WFrame, Popup & SPA](04_scope_wframe_popup_spa.md), [08 — Reusable Architecture](08_reusable_architecture_udc_common_modules.md) và [10 — Rendering, Lazy Loading & Resource Lifetime](10_rendering_lazy_loading_lifetime.md).

## 1. kiểm thử (test / 테스트) không phải là “click được”

Một màn hình có thể click được nhưng vẫn sai nghiệp vụ (business / 비즈니스) trạng thái (state / 상태). tìm kiếm (search / 검색) button có thể gửi yêu cầu (request / 요청) nhưng gửi điều kiện (condition / 조건) cũ. Save có thể hiện success message nhưng máy chủ (server / 서버) đã reject một phần dữ liệu. Popup có thể mở được nhưng giữ listener sau khi đóng. Grid có thể hiển thị đúng 20 row đầu nhưng selected row định danh (identity / 식별자) bị sai sau sort.

Vì vậy một kiểm thử (test / 테스트) tốt phải phát biểu **bất biến (invariant / 불변식) có thể quan sát**. Ví dụ:

```text
Khi user sửa NAME của row có USER_ID=U100
→ canonical DataList row U100 mang value mới
→ row status chuyển sang trạng thái changed phù hợp
→ Save gửi đúng business identity và field được phép sửa
→ success response làm model trở về trạng thái sau-save theo contract
```

Kiểm thử (test / 테스트) không nên chỉ phát biểu “click Save rồi thấy popup thành công”. UI message là một observation, không phải toàn bộ tính đúng đắn (correctness / 정확성).

## 2. Testing portfolio theo ranh giới (boundary / 경계)

Không có một loại kiểm thử (test / 테스트) nào phù hợp cho mọi dạng thất bại (failure mode / 실패 모드). WebSquare screen nên được kiểm thử ở nhiều ranh giới (boundary / 경계) khác nhau.

**lô-gic (logic / 논리) kiểm thử (test / 테스트)** kiểm tra hàm (function / 함수) gần thuần như normalize đầu vào (input / 입력), bản dựng (build / 빌드) yêu cầu (request / 요청) đối tượng (object / 객체), validate cross-field quy tắc (rule / 규칙), map máy chủ (server / 서버) lỗi (error / 오류) và quyết định enable/disable hành động (action / 동작). Đây là kiểm thử (test / 테스트) rẻ, nhanh và dễ chạy nhiều trường hợp (case / 사례).

**Page orchestration kiểm thử (test / 테스트)** kiểm tra `scwin` hàm (function / 함수) điều phối DataCollection, Submission và chuyển tiếp trạng thái (state transition / 상태 전이). Mục tiêu không phải giả lập toàn bộ trình duyệt (browser / 브라우저) mà là chứng minh page lô-gic (logic / 논리) gọi đúng phụ thuộc (dependency / 의존성) và xử lý đúng kết quả (result / 결과).

**thành phần (component / 컴포넌트)/UDC đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트)** kiểm tra công khai (public / 공개) thuộc tính (property / 속성), phương thức (method / 메서드) và sự kiện (event / 이벤트). bên tiêu thụ (consumer / 소비자) không cần biết nội bộ (internal / 내부) đầu vào (input / 입력)/Grid/DataMap của UDC.

**kiểm thử tích hợp (integration test / 통합 테스트)** chạy page với WebSquare Engine thật hoặc môi trường (environment / 환경) gần thật để kiểm tra phạm vi (scope / 범위), binding, vòng đời (lifecycle / 생명주기), WFrame, Submission ánh xạ (mapping / 매핑) và rendering tích hợp (integration / 통합).

**End-to-end kiểm thử (test / 테스트)** đi qua trình duyệt (browser / 브라우저), HTTP và backend để chứng minh trọng yếu (critical / 중요) người dùng (user / 사용자) journey. Nó có giá trị cao nhưng chậm và dễ flaky hơn, nên không dùng để thay tất cả kiểm thử (test / 테스트) tầng dưới.

Mô hình tư duy (mental model / 사고 모델) là:

```text
pure logic
→ page/component contract
→ WebSquare integration
→ browser + server journey
```

Càng xuống dưới càng gần môi trường vận hành (production / 운영 환경) nhưng chi phí setup, thời gian chạy (runtime / 런타임) và diagnosis càng lớn.

## 3. Testability bắt đầu từ kiến trúc (architecture / 아키텍처)

Nếu một handler 300 dòng vừa đọc thành phần (component / 컴포넌트), validate, bản dựng (build / 빌드) payload, gọi Submission, format message, mở popup và sửa toàn cục (global / 전역) trạng thái (state / 상태), kiểm thử (test / 테스트) sẽ khó vì hành vi (behavior / 동작) không có seam rõ.

Một cấu trúc dễ kiểm thử (test / 테스트) hơn:

```javascript
scwin.normalizeSearchCondition = function (raw) {
    return {
        userId: String(raw.userId || "").trim(),
        activeOnly: raw.activeOnly === true
    };
};

scwin.validateSearchCondition = function (condition) {
    if (condition.userId.length > 30) {
        return { ok: false, code: "USER_ID_TOO_LONG" };
    }
    return { ok: true };
};

scwin.search = function () {
    var condition = scwin.normalizeSearchCondition({
        userId: dmSearch.get("USER_ID"),
        activeOnly: dmSearch.get("ACTIVE_ONLY")
    });

    var result = scwin.validateSearchCondition(condition);
    if (!result.ok) {
        scwin.showValidationError(result);
        return;
    }

    scwin.executeSearch(condition);
};
```

`normalizeSearchCondition()` và `validateSearchCondition()` có thể được kiểm tra mà không cần Grid hay mạng (network / 네트워크). `search()` giữ vai trò orchestration. Đây không phải “viết mã (code / 코드) để kiểm thử (test / 테스트)”; đây là tách responsibility để lập luận (reasoning / 추론) tốt hơn, và testability là hệ quả.

## 4. Không mock WebSquare ở mọi nơi

Mock quá ít làm kiểm thử (test / 테스트) chậm và khó cô lập. Mock quá nhiều làm kiểm thử (test / 테스트) chứng minh hành vi (behavior / 동작) của mock chứ không chứng minh WebSquare tích hợp (integration / 통합).

Quy tắc hữu ích là mock **ranh giới (boundary / 경계) mà kiểm thử (test / 테스트) không nhằm kiểm tra**.

Nếu đang kiểm thử (test / 테스트) validator, không cần engine thật.

Nếu đang kiểm thử (test / 테스트) Submission mục tiêu (target / 대상) ánh xạ (mapping / 매핑), phải có tích hợp (integration / 통합) đủ thật để ánh xạ (mapping / 매핑) chạy.

Nếu đang kiểm thử (test / 테스트) WFrame vòng đời (lifecycle / 생명주기), fake `$p` quá nhiều sẽ che đúng bug cần tìm.

Nếu đang kiểm thử (test / 테스트) nghiệp vụ (business / 비즈니스) phản hồi (response / 응답) ánh xạ (mapping / 매핑), backend thật có thể được thay bằng deterministic kiểm thử (test / 테스트) endpoint hoặc mạng (network / 네트워크) stub, nhưng phản hồi (response / 응답) shape phải giống đặc tả hợp đồng (contract / 계약) môi trường vận hành (production / 운영 환경).

Cấp cao (senior / 시니어) ghi chú (note / 노트): mock phải bảo toàn ngữ nghĩa (semantics / 의미론) quan trọng của ranh giới (boundary / 경계). Một fake Submission gọi callback synchronously có thể làm kiểm thử (test / 테스트) xanh trong khi môi trường vận hành (production / 운영 환경) callback asynchronous và có race điều kiện (condition / 조건).

## 5. Fixture cho DataMap và DataList

DataCollection là nơi rất phù hợp để tạo fixture có chủ đích. Đừng dùng một dump môi trường vận hành (production / 운영 환경) khổng lồ cho mọi kiểm thử (test / 테스트). Fixture nên nhỏ nhưng chứa trường hợp (case / 사례) có ý nghĩa.

Ví dụ một DataList kiểm thử (test / 테스트) có thể cần:

```text
U100 — row bình thường
U101 — row có null/empty field
U102 — row sẽ bị update
U103 — row sẽ bị delete
```

Sau thao tác (operation / 연산), assert theo **nghiệp vụ (business / 비즈니스) key** thay vì row chỉ mục (index / 인덱스). Sort/filter có thể đổi chỉ mục (index / 인덱스) nhưng không đổi định danh (identity / 식별자).

Nếu kiểm thử (test / 테스트) CRUD, cần quan sát cả giá trị (value / 값) lẫn row status. Chỉ assert `NAME === "Kim"` có thể bỏ sót việc row vẫn ở status không phù hợp để Save serialize.

## 6. Row status là một máy trạng thái (state machine / 상태 머신) cần kiểm thử (test / 테스트) chuyển tiếp (transition / 전이)

CRUD kiểm thử (test / 테스트) nên xem row status như máy trạng thái (state machine / 상태 머신), không như ký tự bí mật.

Ví dụ các chuyển tiếp (transition / 전이) cần kiểm chứng tùy đặc tả hợp đồng (contract / 계약)/bản dựng (build / 빌드):

```text
loaded row
→ edit
→ changed row

new row
→ edit
→ still new/insert candidate

loaded row
→ delete
→ deletion candidate retained/marked theo model semantics

save success
→ refreshed/committed state theo application policy
```

Không hard-code giả định (assumption / 가정) về ký tự status nếu dự án (project / 프로젝트) wrapper đã abstract nó. kiểm thử (test / 테스트) nghiệp vụ (business / 비즈니스) chuyển tiếp (transition / 전이) mà ứng dụng (application / 애플리케이션) dựa vào, rồi kiểm tra chính xác (exact / 정확한) API/status theo engine bản dựng (build / 빌드).

## 7. Submission kiểm thử (test / 테스트) phải kiểm tra bốn lớp

Một Submission regression thường có bốn lớp tính đúng đắn (correctness / 정확성):

```text
request trigger
→ request serialization
→ response classification
→ target/state update
```

Kiểm thử (test / 테스트) chỉ thấy HTTP 200 mới chứng minh vận chuyển (transport / 전송). Một kiểm thử (test / 테스트) đầy đủ hơn cần xác nhận điều kiện (condition / 조건) đúng được serialize, lỗi (error / 오류) phản hồi (response / 응답) không đi vào success luồng (flow / 흐름), mục tiêu (target / 대상) DataCollection nhận đúng shape và stale phản hồi (response / 응답) không overwrite intent mới.

Nếu save mutation có duplicate protection, kiểm thử (test / 테스트) double-click hoặc repeated trigger phải chứng minh chỉ một logical thao tác (operation / 연산) được lần ghi nhận (commit / 커밋) hoặc máy chủ (server / 서버) idempotency xử lý đúng.

## 8. Async kiểm thử (test / 테스트) không dùng sleep làm synchronization chính

Đây là anti-pattern phổ biến:

```javascript
clickSearch();
await sleep(1000);
expect(gridRowCount()).toBe(10);
```

Kiểm thử (test / 테스트) này giả định mạng (network / 네트워크)/kết xuất (render / 렌더링) hoàn tất trong một giây. Máy CI chậm hơn sẽ flaky; máy nhanh hơn thì lãng phí thời gian.

Hãy chờ một observable điều kiện (condition / 조건):

```text
request cụ thể hoàn thành
DataList đạt expected state
page phát ready signal
loading indicator biến mất sau đúng operation
business result xuất hiện
```

`waitForTimeout` chỉ nên dùng khi chính timing là thứ đang kiểm thử (test / 테스트), không phải cách che thiếu vòng đời (lifecycle / 생명주기) đặc tả hợp đồng (contract / 계약).

## 9. kiểm thử (test / 테스트) latest-intent và race điều kiện (condition / 조건)

Search-as-you-type hoặc người dùng (user / 사용자) đổi điều kiện (condition / 조건) nhanh tạo scenario:

```text
request A gửi trước
request B gửi sau
response B về trước
response A về sau
```

Expected hành vi (behavior / 동작) thường là UI giữ kết quả (result / 결과) của intent B. Regression kiểm thử (test / 테스트) nên cố tình đảo phản hồi (response / 응답) thứ tự (order / 순서). Nếu chỉ kiểm thử (test / 테스트) mạng (network / 네트워크) trả theo thứ tự gửi, race bug sẽ không bao giờ xuất hiện trong CI nhưng vẫn xảy ra môi trường vận hành (production / 운영 환경).

Tương tự, kiểm thử (test / 테스트) điều hướng (navigation / 내비게이션) race:

```text
page A gửi request
user đóng tab A
page B mở
response A về
```

Phản hồi (response / 응답) cũ không được mutate trạng thái (state / 상태) của page đã disposed hoặc page mới không liên quan.

## 10. WFrame và phạm vi (scope / 범위) kiểm thử (test / 테스트) cần kiểm tra topology

Một page chạy standalone có thể pass nhưng thất bại (fail / 실패) khi nằm trong WFrame tầng hai. Vì vậy trọng yếu (critical / 중요) reusable page nên có ít nhất một kiểm thử (test / 테스트) trong topology thật.

Cần kiểm chứng:

```text
component ID giống nhau ở hai Scope không collision
child nhận đúng parameter
child chỉ gọi public parent contract nếu contract cho phép
popup result quay đúng caller
close/reopen tạo instance sạch
setSrc/navigation không gọi child trước readiness phù hợp
```

Nếu mã (code / 코드) chỉ pass khi page là direct child của main frame, kiểm thử (test / 테스트) nested topology sẽ lộ hidden phụ thuộc (dependency / 의존성) vào `parent().parent()`.

## 11. UDC kiểm thử (test / 테스트) theo công khai (public / 공개) đặc tả hợp đồng (contract / 계약)

UDC tốt có thể kiểm thử (test / 테스트) như một black box tương đối.

Ví dụ `EmployeePicker` có đặc tả hợp đồng (contract / 계약):

```text
property: departmentId
method: setValue(employee)
method: getValue()
event: onChange(employee)
```

Kiểm thử (test / 테스트) không nên truy vấn (query / 쿼리) nội bộ (internal / 내부) `inputEmployeeName` trừ khi đang kiểm thử (test / 테스트) hiện thực (implementation / 구현) riêng. bên tiêu thụ (consumer / 소비자) regression phải chứng minh thuộc tính (property / 속성) được áp dụng, phương thức (method / 메서드) giữ bất biến (invariant / 불변식) và sự kiện (event / 이벤트) trả payload đúng lược đồ (schema / 스키마).

Khi refactor nội bộ (internal / 내부) bố cục (layout / 레이아웃) từ đầu vào (input / 입력) + Button sang AutoComplete, đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) vẫn giữ nguyên. Đây là lợi ích trực tiếp của lớp trừu tượng (abstraction / 추상화) ranh giới (boundary / 경계).

## 12. End-to-end selector phải bền với rendering internals

WebSquare có thể biến đổi vật lý (physical / 물리적) DOM ID theo phạm vi (scope / 범위)/rendering. kiểm thử (test / 테스트) E2E phụ thuộc selector dài kiểu:

```text
#mf_wframe1_udc1_input1_input
```

sẽ dễ vỡ khi bố cục (layout / 레이아웃) thay đổi dù hành vi (behavior / 동작) không đổi.

Ưu tiên selector dựa trên đặc tả hợp đồng (contract / 계약) ổn định: logical kiểm thử (test / 테스트) hook được dự án (project / 프로젝트) quy ước, accessible name/label, role, hoặc wrapper kiểm thử (test / 테스트) API. Không dựa vào private engine DOM cấu trúc (structure / 구조) nếu không bắt buộc.

Nếu cần thêm `data-*` hook cho automation, hook phải ngữ nghĩa (semantic / 의미적) và ổn định, ví dụ `data-testid="employee-search-submit"`, không phải `div-17-child-2`.

## 13. khả năng tiếp cận (accessibility / 접근성) kiểm thử (test / 테스트) là functional kiểm thử (test / 테스트)

Keyboard điều hướng (navigation / 내비게이션), focus return sau popup, label association và lỗi (error / 오류) announcement không phải cosmetic detail.

Một regression scenario nên thử:

```text
Tab qua form theo thứ tự nghiệp vụ
mở popup bằng keyboard
focus chuyển vào popup
đóng popup
focus quay về trigger hợp lý
validation error có thể được nhận biết không chỉ bằng màu
```

Automation có thể hỗ trợ một phần, nhưng keyboard-only exploratory kiểm thử (test / 테스트) và screen-reader xác minh (verification / 확인) vẫn cần cho luồng (flow / 흐름) quan trọng.

## 14. Internationalization kiểm thử (test / 테스트) cần thay đổi dữ liệu, không chỉ locale flag

Một screen “đã hỗ trợ English” chưa được chứng minh chỉ vì locale switch hoạt động.

Kiểm thử (test / 테스트) nên dùng văn bản (text / 텍스트) dài, missing key, ký tự đa byte, date/number format và label có độ dài khác nhau. Korean, Vietnamese và English tạo pressure bố cục (layout / 레이아웃) khác nhau.

Fixture i18n nên có ít nhất:

```text
short label
long translated label
missing key
special character
number/date locale case
```

Mục tiêu là tìm giả định (assumption / 가정) “văn bản (text / 텍스트) luôn ngắn như Korean hiện tại”.

## 15. kiểm tra hợp lệ (validation / 검증) kiểm thử (test / 테스트) theo ranh giới (boundary / 경계)

Máy khách (client / 클라이언트) kiểm tra hợp lệ (validation / 검증) có ba nhóm kiểm thử (test / 테스트) khác nhau.

Đầu vào (input / 입력) tương tác (interaction / 상호작용) kiểm thử (test / 테스트) chứng minh thành phần (component / 컴포넌트) cho phép/chặn character theo UX quy tắc (rule / 규칙).

Ngữ nghĩa (semantic / 의미적) kiểm tra hợp lệ (validation / 검증) kiểm thử (test / 테스트) chứng minh nghiệp vụ (business / 비즈니스) điều kiện (condition / 조건) như `startDate <= endDate`.

Máy chủ (server / 서버) kiểm tra hợp lệ (validation / 검증) kiểm thử tích hợp (integration test / 통합 테스트) chứng minh payload không hợp lệ vẫn bị reject dù máy khách (client / 클라이언트) guard bị bypass.

Nếu chỉ kiểm thử (test / 테스트) máy khách (client / 클라이언트), bạn chưa kiểm thử (test / 테스트) trust ranh giới (boundary / 경계). Nếu chỉ kiểm thử (test / 테스트) máy chủ (server / 서버), UX regression có thể vẫn xảy ra.

## 16. bảo mật (security / 보안) negative kiểm thử (test / 테스트)

Trọng yếu (critical / 중요) screen nên có negative kiểm thử (test / 테스트) cho giả định (assumption / 가정) bảo mật thường gặp:

```text
hidden field bị sửa bằng request manipulation
readOnly field bị gửi giá trị khác
role thấp gọi save endpoint trực tiếp
HTML-like input quay lại Grid/Output
file upload sai loại/kích thước
Excel/CSV cell có formula-like prefix
```

Kết quả đúng phải đến từ máy chủ (server / 서버) chính sách (policy / 정책) và safe rendering, không từ việc button bị ẩn.

## 17. hiệu năng (performance / 성능) regression kiểm thử (test / 테스트) cần ngân sách (budget / 예산)

Không cần biến mọi kiểm thử (test / 테스트) thành benchmark. Chọn luồng (flow / 흐름) có rủi ro (risk / 위험) cao như initial shell, tìm kiếm (search / 검색) Grid lớn, open popup, switch tab và repeated điều hướng (navigation / 내비게이션).

Đo cùng một scenario với dataset kiểm soát:

```text
click → request start
request end → DataList ready
DataList ready → interactive render
heap sau N vòng open/close
request count sau N vòng navigation
```

Regression kiểm thử (test / 테스트) có giá trị khi môi trường (environment / 환경) đủ ổn định và threshold có ý nghĩa. Một threshold 500 ms trên CI noisy có thể tạo false alarm; trend hoặc relative comparison đôi khi phù hợp hơn absolute number.

## 18. bộ nhớ (memory / 메모리) regression cần repeated vòng đời (lifecycle / 생명주기)

Leak hiếm khi lộ sau một lần mở page.

Scenario tốt hơn:

```text
warm up
record baseline
open popup/tab
perform representative action
close
lặp 20–50 lần
force/await GC nếu test environment cho phép
so heap/listener/request behavior
```

Không chỉ nhìn vùng nhớ động (heap / 힙) tổng. Tìm retained phạm vi (scope / 범위)/thành phần (component / 컴포넌트)/listener hoặc duplicate mạng (network / 네트워크) tác động (effect / 효과). Chapter [10](10_rendering_lazy_loading_lifetime.md) giải thích thời gian tồn tại (lifetime / 수명) mô hình (model / 모델) phía sau kiểm thử (test / 테스트) này.

## 19. kiểm thử (test / 테스트) dữ liệu (data / 데이터) phải có quyền sở hữu (ownership / 소유권)

E2E kiểm thử (test / 테스트) dùng chung một account và một bản ghi (record / 레코드) mutable rất dễ flaky. kiểm thử (test / 테스트) A đổi bản ghi (record / 레코드), kiểm thử (test / 테스트) B giả định bản ghi (record / 레코드) cũ.

Có ba chiến lược thường dùng:

```text
immutable reference fixture
per-test generated data
reset/cleanup transaction theo suite
```

Chọn theo backend kiến trúc (architecture / 아키텍처). Điều quan trọng là kiểm thử (test / 테스트) biết ai tạo dữ liệu, ai được sửa và ai cleanup.

Đừng để CI phụ thuộc “cơ sở dữ liệu (database / 데이터베이스) UAT hiện đang có USER_ID=TEST01”. Đó không phải fixture; đó là environmental accident.

## 20. môi trường (environment / 환경) parity và deterministic cấu hình (config / 설정)

Một kiểm thử (test / 테스트) pass cục bộ (local / 로컬) nhưng thất bại (fail / 실패) UAT có thể do engine bản dựng (build / 빌드), cấu hình (config / 설정), ngữ cảnh (context / 맥락) gốc (root / 루트), locale, trình duyệt (browser / 브라우저) hoặc bộ nhớ đệm (cache / 캐시) khác nhau.

Regression report nên ghi ít nhất:

```text
WebSquare engine build
browser/version
application build/artifact id
config profile
backend environment
test data version hoặc seed
```

Đây là provenance của bằng chứng (evidence / 증거). Không có provenance, screenshot “pass” khó tái hiện.

## 21. đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) cho phản hồi (response / 응답) lược đồ (schema / 스키마)

Frontend thường thất bại (fail / 실패) không phải vì UI mã (code / 코드) đổi mà vì backend phản hồi (response / 응답) shape đổi.

Nếu page kỳ vọng:

```json
{
  "users": [
    { "userId": "U100", "name": "Kim" }
  ]
}
```

thì đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) cần bắt các thay đổi như `userId` thành `user_id`, `users` thành `data`, hoặc nullability thay đổi.

TypeScript có thể giúp mô hình (model / 모델) đặc tả hợp đồng (contract / 계약) nếu dự án (project / 프로젝트) dùng TypeScript, nhưng thời gian chạy (runtime / 런타임) phản hồi (response / 응답) vẫn cần kiểm tra hợp lệ (validation / 검증)/đặc tả hợp đồng (contract / 계약) bằng chứng (evidence / 증거). Với JavaScript WebSquare, lược đồ (schema / 스키마) fixture và kiểm thử tích hợp (integration test / 통합 테스트) càng quan trọng.

## 22. lỗi (error / 오류) đường dẫn (path / 경로) phải được kiểm thử (test / 테스트) như first-class hành vi (behavior / 동작)

Happy đường dẫn (path / 경로) thường được kiểm thử (test / 테스트) nhiều nhất, trong khi môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) nằm ở hết thời gian chờ (timeout / 타임아웃), 401/403, 500, malformed payload và partial nghiệp vụ (business / 비즈니스) thất bại (failure / 실패).

Một screen quan trọng nên fault-inject:

```text
network timeout
HTTP error
business error với HTTP 200
malformed/missing field
slow response
response out of order
session expiration
```

Sau mỗi lỗi, assert cả UI trạng thái (state / 상태): loading indicator có tắt không, button có được enable lại không, DataList cũ có bị xóa sai không, người dùng (user / 사용자) có thể thử lại (retry / 재시도) không.

## 23. kiểm thử (test / 테스트) gỡ lỗi (debug / 디버그) menu và thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거) trong exploratory testing

WebSquare5 SP5 có gỡ lỗi (debug / 디버그) ngữ cảnh (context / 맥락) menu cho log, DataCollection, sự kiện (event / 이벤트) và Submission ở các cấu hình (configuration / 구성) tương ứng. Khi exploratory kiểm thử (test / 테스트) phát hiện lỗi, dùng các view này cùng trình duyệt (browser / 브라우저) DevTools để capture trạng thái (state / 상태) trước khi refresh.

Một bug report tốt không chỉ có “tìm kiếm (search / 검색) không chạy”. Nó có thể ghi:

```text
handler đã fire
Submission object tồn tại
Network không có request
DataMap condition = {...}
engine build = ...
console exception = ...
```

Như vậy nhà phát triển (developer / 개발자) bắt đầu từ ranh giới (boundary / 경계) đã khoanh vùng thay vì tái hiện mù.

## 24. CI chuỗi xử lý (pipeline / 파이프라인): thất bại (fail / 실패) càng sớm càng rẻ

Một chuỗi xử lý (pipeline / 파이프라인) hợp lý thường đi từ kiểm tra rẻ đến đắt:

```text
syntax/static checks
→ pure logic tests
→ build/W-Pack validation
→ component/page integration
→ critical E2E smoke
→ broader regression
→ performance/security suites theo lịch hoặc release gate
```

W-Pack có stand-alone mô-đun (module / 모듈) phục vụ CI/server-side batch conversion trong SP5, vì vậy hiện vật bản dựng (build artifact / 빌드 산출물) không nhất thiết phụ thuộc thao tác thủ công trong Studio. Chapter [12](12_build_config_deployment.md) đi sâu source-to-artifact chuỗi xử lý (pipeline / 파이프라인).

## 25. Smoke kiểm thử (test / 테스트) sau deploy

Deploy thành công không đồng nghĩa ứng dụng (application / 애플리케이션) usable. Smoke kiểm thử (test / 테스트) nên đi qua một số đặc tả hợp đồng (contract / 계약) có khả năng phát hiện cấu hình (config / 설정)/sản phẩm tạo ra (artifact / 산출물) lỗi nhanh:

```text
shell load
login/session nếu thuộc scope test
một WFrame child load
một Submission GET/query
một Grid render
một popup open/close
một static/common resource từ _wpack_
```

Nếu bản phát hành (release / 릴리스) có di chuyển (migration / 마이그레이션) lớn, thêm luồng (flow / 흐름) đặc thù như UDC, Excel hoặc multilingual tài nguyên (resource / 자원).

## 26. Regression suite theo rủi ro (risk / 위험), không theo số màn hình

Không cần một E2E kiểm thử (test / 테스트) đầy đủ cho mọi page nếu nhiều page chỉ lặp cùng mẫu (pattern / 패턴). Ưu tiên theo:

```text
business criticality
change frequency
complexity/lifecycle risk
historical defect density
shared component blast radius
security/data sensitivity
```

Một UDC dùng ở 80 screen có thể đáng được kiểm thử (test / 테스트) sâu hơn một page độc lập ít dùng.

## 27. Flaky kiểm thử (test / 테스트) là defect của kiểm thử (test / 테스트) hệ thống (system / 시스템)

Một kiểm thử (test / 테스트) thất bại (fail / 실패) ngẫu nhiên làm nhóm (team / 팀) mất niềm tin. Đừng chỉ thử lại (retry / 재시도) đến xanh.

Nguyên nhân gốc (root cause / 근본 원인) thường là:

```text
sleep-based synchronization
shared mutable test data
selector phụ thuộc DOM internals
network/environment không kiểm soát
animation/render timing
test order dependency
cleanup thiếu
```

Thử lại (retry / 재시도) có thể dùng để thu thập bằng chứng (evidence / 증거) tạm thời, nhưng không được biến nondeterminism thành “pass”.

## 28. Anti-pattern: assert hiện thực (implementation / 구현) detail

Ví dụ kiểm thử (test / 테스트) rằng `scwin.tempFlag === 2` trong khi nghiệp vụ (business / 비즈니스) đặc tả hợp đồng (contract / 계약) chỉ cần Save button disabled. Refactor nội bộ sẽ làm kiểm thử (test / 테스트) vỡ dù hành vi (behavior / 동작) đúng.

Kiểm thử (test / 테스트) nên bám vào công khai (public / 공개) đặc tả hợp đồng (contract / 계약) hoặc bất biến (invariant / 불변식). Implementation-level kiểm thử (test / 테스트) chỉ hợp lý khi hiện thực (implementation / 구현) đó chính là thứ cần bảo vệ, ví dụ row-status chuyển tiếp (transition / 전이) hoặc serialization adapter.

## 29. Anti-pattern: một E2E khổng lồ cho cả ngày làm việc

Một script login → tìm kiếm (search / 검색) → edit → popup → export → logout dài hàng trăm bước có diagnosis kém. Step 87 thất bại (fail / 실패) không biết nguyên nhân gốc (root cause / 근본 원인) nằm ở trạng thái (state / 상태) từ step nào.

Tách journey theo bounded năng lực (capability / 역량), nhưng giữ một số end-to-end đường găng (critical path / 임계 경로) ngắn để chứng minh tích hợp (integration / 통합) xuyên hệ thống.

## 30. Practical kiểm thử (test / 테스트) ma trận (matrix / 행렬) cho màn hình CRUD

Một màn hình truy vấn (query / 쿼리)/edit/save nên có regression ma trận (matrix / 행렬) tối thiểu theo lập luận (reasoning / 추론) sau.

**tìm kiếm (search / 검색)** phải chứng minh điều kiện (condition / 조건) ánh xạ (mapping / 매핑), empty kết quả (result / 결과), large kết quả (result / 결과), máy chủ (server / 서버) lỗi (error / 오류) và stale-response thứ tự (ordering / 순서).

**Edit** phải chứng minh chuẩn gốc (canonical / 정본) DataList thay đổi, row định danh (identity / 식별자) ổn định sau sort/filter và kiểm tra hợp lệ (validation / 검증) không duplicate giữa handler.

**Save** phải chứng minh changed rows được gửi đúng, double-click không tạo duplicate logical giao dịch (transaction / 트랜잭션), nghiệp vụ (business / 비즈니스) lỗi (error / 오류) giữ UI recoverable và success trạng thái (state / 상태) được refresh/lần ghi nhận (commit / 커밋) đúng chính sách (policy / 정책).

**Popup** phải chứng minh parameter/kết quả (result / 결과) đặc tả hợp đồng (contract / 계약), focus return và repeated open/close không leak.

**vòng đời (lifecycle / 생명주기)** phải chứng minh close/navigate khi yêu cầu (request / 요청) pending không gây stale mutation.

Đây là ma trận (matrix / 행렬) theo dạng thất bại (failure mode / 실패 모드), không phải checklist API.

## 31. cấp cao (senior / 시니어) ghi chú (note / 노트): testability là chỉ báo coupling

Nếu muốn kiểm thử (test / 테스트) một quy tắc (rule / 규칙) nhỏ nhưng phải boot toàn bộ app shell, mở ba WFrame và kết nối máy chủ (server / 서버) thật, quy tắc (rule / 규칙) đó đang nằm quá sâu trong khung phần mềm (framework / 프레임워크) coupling.

Nếu muốn kiểm thử (test / 테스트) một UDC nhưng phải biết năm nội bộ (internal / 내부) thành phần (component / 컴포넌트) ID, công khai (public / 공개) đặc tả hợp đồng (contract / 계약) của UDC chưa đủ rõ.

Nếu muốn kiểm thử (test / 테스트) page B nhưng phải tạo toàn cục (global / 전역) trạng thái (state / 상태) từ page A, hai page đang có hidden coupling.

Testing vì vậy không chỉ bắt bug. Nó cho phản hồi (feedback / 피드백) về kiến trúc (architecture / 아키텍처).

## 32. mô hình tư duy (mental model / 사고 모델) cuối chapter

Một regression chiến lược (strategy / 전략) tốt có thể tóm tắt:

```text
business invariant
→ observable contract
→ smallest useful test boundary
→ deterministic fixture
→ controlled async/lifecycle
→ production-like integration ở nơi cần
→ evidence khi fail
```

Khi kiểm thử (test / 테스트) thất bại (fail / 실패), câu hỏi đầu tiên không phải “thử lại (retry / 재시도) có pass không?”. Hãy hỏi đặc tả hợp đồng (contract / 계약) nào vừa bị phá, bằng chứng (evidence / 증거) nằm ở tầng (layer / 계층) nào và kiểm thử (test / 테스트) có đang quan sát đúng nguồn chuẩn (source of truth / 정본) không.

## Nguồn đối chiếu

WebSquare5 SP5 Development Guide mô tả gỡ lỗi (debug / 디버그) ngữ cảnh (context / 맥락) menu, DataCollection/Submission inspection, W-Pack và vòng đời (lifecycle / 생명주기) hành vi (behavior / 동작). Stand-alone W-Pack được tài liệu chính thức mô tả như cơ chế có thể tích hợp CI/máy chủ (server / 서버) batch bản dựng (build / 빌드). Testing khung phần mềm (framework / 프레임워크) cụ thể không phải chuẩn gốc (canonical / 정본) WebSquare API; hãy chọn theo trình duyệt (browser / 브라우저)/toolchain của dự án (project / 프로젝트) và giữ kiểm thử (test / 테스트) dựa trên công khai (public / 공개) WebSquare/đặc tả ứng dụng (application contract / 애플리케이션 계약) thay vì private engine DOM.

> **Bàn giao:** Sau **Nguồn đối chiếu**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 platform runtime page model](./01_platform_runtime_page_model.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
