# 09 — Forms, kiểm tra hợp lệ (validation / 검증), Internationalization & khả năng tiếp cận (accessibility / 접근성)

> **Mạch đọc:** Đặt **09 — Forms, kiểm tra hợp lệ (validation / 검증), Internationalization & khả năng tiếp cận (accessibility / 접근성)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. chuỗi xử lý (pipeline / 파이프라인) của dữ liệu nhập** sang **2. đầu vào (input / 입력) filtering không phải kiểm tra hợp lệ (validation / 검증) hoàn chỉnh**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Màn hình WebSquare enterprise thường xoay quanh form nhập liệu, tìm kiếm (search / 검색) điều kiện (condition / 조건), popup chọn dữ liệu và Grid edit. Vì vậy chất lượng của đầu vào (input / 입력)/kiểm tra hợp lệ (validation / 검증) không chỉ là UX detail. Nó quyết định dữ liệu đi vào DataCollection có đáng tin đến mức nào, lỗi được phát hiện ở đâu, người dùng có hiểu được lỗi không, và màn hình có còn sử dụng được khi đổi ngôn ngữ, dùng bàn phím hoặc công cụ hỗ trợ hay không.

Chapter này tập trung vào một mô hình tư duy (mental model / 사고 모델) quan trọng: **đầu vào (input / 입력) điều khiển (control / 제어), kiểm tra hợp lệ (validation / 검증), nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식), internationalization và khả năng tiếp cận (accessibility / 접근성) là các lớp khác nhau**. Một thuộc tính (property / 속성) UI không thể thay thế máy chủ (server / 서버) kiểm tra hợp lệ (validation / 검증); một regex không thể thay thế lĩnh vực (domain / 도메인) quy tắc (rule / 규칙); một label dịch được không tự làm màn hình accessible.

## 1. chuỗi xử lý (pipeline / 파이프라인) của dữ liệu nhập

Khi người dùng (user / 사용자) nhập dữ liệu, đừng hình dung chỉ có một bước “đầu vào (input / 입력) nhận giá trị (value / 값)”. Một luồng (flow / 흐름) thực tế thường gồm:

```text
physical keystroke / paste / IME
→ component input filtering
→ component parsing/dataType
→ display formatting
→ binding/model update
→ UI validation
→ request serialization
→ server validation
→ domain invariant/database constraint
```

Mỗi lớp chặn một loại lỗi khác nhau.

Ví dụ `allowChar="0-9"` có thể ngăn nhiều ký tự không phải số được gõ vào đầu vào (input / 입력), nhưng nó không chứng minh giá trị là một employee number hợp lệ. `dataType="number"` có thể giúp parsing và format, nhưng không chứng minh số nằm trong nghiệp vụ (business / 비즈니스) phạm vi (range / 범위). máy chủ (server / 서버) vẫn phải kiểm tra.

## 2. đầu vào (input / 입력) filtering không phải kiểm tra hợp lệ (validation / 검증) hoàn chỉnh

WebSquare hỗ trợ các thuộc tính (property / 속성) kiểm soát đầu vào (input / 입력) như `allowChar`, `ignoreChar`, `dataType` tùy thành phần (component / 컴포넌트)/bản dựng (build / 빌드). Đây là guard ở mức tương tác (interaction / 상호작용).

Ví dụ:

```xml
<xf:input id="inputAge" dataType="number" />
```

hoặc một đầu vào (input / 입력) văn bản (text / 텍스트) chỉ cho phép mẫu (pattern / 패턴) ký tự nhất định.

Nhưng đầu vào (input / 입력) có thể đến từ nhiều nguồn ngoài keypress:

```text
paste
programmatic setValue
binding từ DataMap
response server
restore state
browser/autofill tùy environment
```

Vì vậy không nên suy luận “người dùng (user / 사용자) không gõ được ký tự X” đồng nghĩa mô hình (model / 모델) không bao giờ có X.

## 3. Parsing, biểu diễn (representation / 표현) và lĩnh vực (domain / 도메인) giá trị (value / 값)

Một trường dữ liệu (field / 필드) ngày tháng có ít nhất ba biểu diễn (representation / 표현):

```text
user display: 2026.09.22
client canonical: 20260922 hoặc 2026-09-22
server/domain: LocalDate / DB DATE
```

Nếu không xác định chuẩn gốc (canonical / 정본) biểu diễn (representation / 표현), mã (code / 코드) sẽ có nhiều nơi tự replace `.` hoặc `-`, tạo lỗi locale và trường hợp biên (edge case / 경계 사례).

Quy tắc (rule / 규칙) tốt là chọn một biểu diễn (representation / 표현) ổn định cho ranh giới (boundary / 경계) dữ liệu (data / 데이터) rồi format ở UI tầng (layer / 계층).

Tương tự money:

```text
display: 1,234,567 원
canonical client payload: 1234567
server numeric type: decimal/integer theo domain
```

Không gửi display string nếu máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약) thực sự cần numeric giá trị (value / 값).

## 4. kiểm tra hợp lệ (validation / 검증) có nhiều cấp

Một trường dữ liệu (field / 필드) `amount` có thể đi qua các cấp:

**Syntactic kiểm tra hợp lệ (validation / 검증)**: có parse thành số không?

**trường dữ liệu (field / 필드) kiểm tra hợp lệ (validation / 검증)**: amount có lớn hơn 0 không?

**Cross-field kiểm tra hợp lệ (validation / 검증)**: startDate <= endDate?

**nghiệp vụ (business / 비즈니스) kiểm tra hợp lệ (validation / 검증)**: amount có vượt hạn mức của người dùng (user / 사용자) không?

**Authorization kiểm tra hợp lệ (validation / 검증)**: người dùng (user / 사용자) có quyền thực hiện giao dịch (transaction / 트랜잭션) này không?

**Persistence bất biến (invariant / 불변식)**: unique key hoặc foreign key còn đúng tại thời điểm lần ghi nhận (commit / 커밋) không?

UI chỉ có đủ ngữ cảnh (context / 맥락) cho một phần trong số này.

## 5. máy khách (client / 클라이언트) kiểm tra hợp lệ (validation / 검증) phục vụ phản hồi (feedback / 피드백) nhanh

Máy khách (client / 클라이언트) kiểm tra hợp lệ (validation / 검증) có giá trị lớn: người dùng (user / 사용자) không phải gửi yêu cầu (request / 요청) mới biết trường dữ liệu (field / 필드) bắt buộc đang rỗng. Nhưng vai trò chính là **phản hồi (feedback / 피드백) và giảm yêu cầu (request / 요청) vô nghĩa**, không phải trust ranh giới (boundary / 경계).

Một mẫu (pattern / 패턴) save:

```javascript
scwin.save = function () {
    if (!scwin.validateForm()) {
        return;
    }

    if (scwin.saving) {
        return;
    }

    scwin.saving = true;
    $p.executeSubmission("sbmSave");
};
```

Máy chủ (server / 서버) vẫn validate payload lại độc lập.

## 6. Required không đồng nghĩa meaningful

Một trường dữ liệu (field / 필드) có giá trị (value / 값) không có nghĩa giá trị (value / 값) hợp lệ.

Ví dụ:

```text
" "
"000000"
"N/A"
```

có thể vượt qua kiểm tra non-empty nhưng vô nghĩa theo lĩnh vực (domain / 도메인).

Do đó validator nên nói bằng lĩnh vực (domain / 도메인) ngôn ngữ (language / 언어): `isValidEmployeeId`, `isValidDateRange`, `canSubmitApproval`, thay vì chỉ `notEmpty` ở mọi nơi.

## 7. Cross-field quy tắc (rule / 규칙) nên có một đơn vị sở hữu (owner / 오너) rõ

Ví dụ:

```text
fromDate <= toDate
```

Nếu quy tắc (rule / 규칙) này được bản sao (copy / 복사) vào `onchange` của hai đầu vào (input / 입력), `onclick` tìm kiếm (search / 검색) và `beforeSubmission`, bốn bản có thể drift.

Tốt hơn là một hàm (function / 함수) domain-level phía page:

```javascript
scwin.validateSearchPeriod = function () {
    var from = dmSearch.get("fromDate");
    var to = dmSearch.get("toDate");
    return !from || !to || from <= to;
};
```

Sự kiện (event / 이벤트) handler có thể gọi nó để phản hồi (feedback / 피드백) sớm; save/tìm kiếm (search / 검색) orchestration cũng gọi cùng quy tắc (rule / 규칙) trước yêu cầu (request / 요청).

## 8. lỗi (error / 오류) message phải gắn với hành động sửa được

Thông báo:

```text
Invalid input.
```

ít giá trị hơn:

```text
Ngày bắt đầu phải nhỏ hơn hoặc bằng ngày kết thúc.
```

Một lỗi (error / 오류) message tốt trả lời:

```text
Cái gì sai?
Ở đâu?
User sửa thế nào?
```

Không nên lộ dấu vết ngăn xếp (stack trace / 스택 트레이스), endpoint nội bộ hoặc raw máy chủ (server / 서버) exception cho người dùng (user / 사용자).

## 9. Focus management sau kiểm tra hợp lệ (validation / 검증)

Khi form dài, chỉ alert lỗi nhưng không đưa focus về trường dữ liệu (field / 필드) sai làm người dùng (user / 사용자) mất thời gian tìm.

Luồng (flow / 흐름) tốt thường là:

```text
collect validation result
→ show message/inline marker
→ focus first actionable invalid field
```

Nhưng focus phải tôn trọng thành phần (component / 컴포넌트) vòng đời (lifecycle / 생명주기). Nếu trường dữ liệu (field / 필드) nằm trong tab chưa kết xuất (render / 렌더링), cố focus ngay có thể thất bại (fail / 실패). Khi đó cần activate/kết xuất (render / 렌더링) bộ chứa (container / 컨테이너) trước rồi focus.

## 10. Tab thứ tự (order / 순서) là một phần tương tác (interaction / 상호작용) kiến trúc (architecture / 아키텍처)

Keyboard người dùng (user / 사용자) dựa vào thứ tự focus. Khi screen được sinh từ nhiều Group/WFrame/UDC, visual thứ tự (order / 순서) và tab thứ tự (order / 순서) có thể lệch nhau.

Không nên chỉ kiểm thử (test / 테스트) bằng mouse. Một form môi trường vận hành (production / 운영 환경) nên thử:

```text
Tab từ đầu đến cuối
Shift+Tab quay lại
Enter/Space trên control phù hợp
Popup open/close có trả focus hợp lý không
Disabled/hidden component có bị focus nhầm không
```

## 11. readOnly, disabled, hidden có ngữ nghĩa (semantics / 의미론) khác nhau

Các trạng thái UI này không nên được xem là synonym.

`readOnly` thường nghĩa người dùng (user / 사용자) thấy giá trị (value / 값) nhưng không edit trực tiếp.

`disabled` thường nghĩa điều khiển (control / 제어) không interactive và hành vi (behavior / 동작) submit/focus có thể khác tùy thành phần (component / 컴포넌트).

`hidden` nghĩa không hiển thị nhưng giá trị (value / 값)/mô hình (model / 모델) vẫn có thể tồn tại.

Không thuộc tính (property / 속성) nào trong ba thuộc tính (property / 속성) này tạo authorization ranh giới (boundary / 경계). người dùng (user / 사용자) có thể sửa yêu cầu (request / 요청) hoặc chạy script máy khách (client / 클라이언트).

## 12. Permission phải thay đổi năng lực (capability / 역량), không chỉ decoration

UI có thể ẩn nút Delete nếu người dùng (user / 사용자) không có permission để giảm confusion. Nhưng máy chủ (server / 서버) endpoint Delete vẫn phải kiểm tra permission.

Mô hình tư duy (mental model / 사고 모델):

```text
client permission = presentation/interaction policy
server permission = security enforcement
```

Một hidden button không bảo vệ API.

## 13. Internationalization không chỉ là dịch label

Đa ngôn ngữ (internationalization / i18n / 국제화) bao gồm:

```text
text translation
date/time format
number/currency format
name/address format
text expansion
font/glyph support
sort/collation
message grammar
```

WebSquare5 hỗ trợ ngôn ngữ (language / 언어) pack và các thuộc tính (property / 속성) như `useLocale`, `localeRef` ở những thành phần (component / 컴포넌트) tương ứng. Đây là cơ chế (mechanism / 메커니즘) ánh xạ (mapping / 매핑) key → localized văn bản (text / 텍스트), nhưng lĩnh vực (domain / 도메인) thiết kế (design / 설계) vẫn phải dùng stable ngữ nghĩa (semantic / 의미적) keys.

## 14. Stable locale key

Không nên dùng raw Korean sentence làm key:

```text
"저장하시겠습니까?"
```

rồi map sang English. Khi Korean wording đổi, key định danh (identity / 식별자) cũng đổi.

Tốt hơn:

```text
confirm.save
validation.required.employeeName
button.search
```

Key mô tả meaning, translation tệp (file / 파일) mô tả wording.

## 15. `useLanguagePack` và thời gian chạy (runtime / 런타임) cấu hình (configuration / 구성)

Theo SP5 official guide, máy khách (client / 클라이언트) cấu hình (configuration / 구성) có thể bật ngôn ngữ (language / 언어) pack và map ngôn ngữ (language / 언어) mã (code / 코드) tới tệp (file / 파일) tài nguyên (resource / 자원). thành phần (component / 컴포넌트) hỗ trợ locale có thể dùng `localeRef` để lấy văn bản (text / 텍스트).

Điểm cần lập luận (reasoning / 추론) không phải thuộc tên mọi thuộc tính (property / 속성) mà là hiểu chuỗi xử lý (pipeline / 파이프라인):

```text
runtime language decision
→ load language resource
→ resolve locale key
→ component displays localized value
```

Nếu văn bản (text / 텍스트) không đổi khi switch ngôn ngữ (language / 언어), gỡ lỗi (debug / 디버그) theo chuỗi xử lý (pipeline / 파이프라인) này thay vì sửa thành phần (component / 컴포넌트) ngẫu nhiên.

## 16. Missing translation là data-quality bài toán (problem / 문제)

Khi locale key không tồn tại, hành vi (behavior / 동작) fallback phụ thuộc cấu hình (config / 설정)/thành phần (component / 컴포넌트)/bản dựng (build / 빌드). môi trường vận hành (production / 운영 환경) nên phát hiện missing key sớm hơn người dùng (user / 사용자).

Có thể kiểm tra (audit / 감사) bằng:

```text
collect keys từ source
compare với language files
report missing/unused keys
```

Nếu dự án (project / 프로젝트) không có automation, ít nhất regression kiểm thử (test / 테스트) các screen quan trọng ở mọi supported ngôn ngữ (language / 언어).

## 17. văn bản (text / 텍스트) expansion và bố cục (layout / 레이아웃)

English, Vietnamese và Korean có độ dài khác nhau. Một button vừa đẹp với `조회` có thể không đủ cho `Search transactions`.

Do đó bố cục (layout / 레이아웃) không nên phụ thuộc quá chặt fixed width nếu sản phẩm (product / 제품) cần đa ngôn ngữ.

Kiểm tra:

```text
button label overflow
Grid header width
validation message wrapping
popup title
placeholder
```

I18n là một đầu vào (input / 입력) cho bố cục (layout / 레이아웃) kiến trúc (architecture / 아키텍처).

## 18. khả năng tiếp cận (accessibility / 접근성) là năng lực (capability / 역량) của người dùng (user / 사용자)

Khả năng truy cập (accessibility / 접근성) nghĩa người dùng có thể thao tác và hiểu screen bằng nhiều phương thức khác nhau, không chỉ mouse + visual display.

Các trục cơ bản:

```text
keyboard navigation
focus visibility
semantic label
screen reader context
contrast/state distinction
error identification
```

WebSquare thành phần (component / 컴포넌트) cung cấp một phần ngữ nghĩa (semantics / 의미론); nhà phát triển (developer / 개발자) vẫn phải cấu hình và kiểm thử (test / 테스트).

## 19. Grid khả năng tiếp cận (accessibility / 접근성) có hiệu năng (performance / 성능) sự đánh đổi (trade-off / 트레이드오프) thật

Official WebSquare guide lưu ý các option liên quan Grid khả năng tiếp cận (accessibility / 접근성) như `senseReader` có thể làm tăng DOM/bộ nhớ (memory / 메모리) chi phí (cost / 비용), đặc biệt khi đồng thời hiển thị số lượng row lớn. Đây là ví dụ quan trọng: khả năng tiếp cận (accessibility / 접근성) và hiệu năng (performance / 성능) không nên bị đặt thành hai mục tiêu đối nghịch kiểu “chọn một”.

Thay vào đó phải thiết kế dataset/rendering chiến lược (strategy / 전략) phù hợp:

```text
server paging
virtual/native rendering khi phù hợp
không render hàng chục nghìn row cùng lúc
đo heap/DOM/render time
```

Không nên tắt khả năng tiếp cận (accessibility / 접근성) chỉ vì screen được thiết kế với dataset phi thực tế.

## 20. Label và ngữ cảnh (context / 맥락)

Một đầu vào (input / 입력) chỉ có placeholder không phải lúc nào cũng cung cấp ngữ nghĩa (semantic / 의미적) label ổn định. Placeholder biến mất khi người dùng (user / 사용자) nhập và có thể khó đọc.

Form quan trọng nên có label/ngữ cảnh (context / 맥락) rõ. Với Grid, header phải diễn đạt meaning của column, không chỉ viết abbreviation nội bộ mà người dùng (user / 사용자) không hiểu.

## 21. lỗi (error / 오류) khả năng tiếp cận (accessibility / 접근성)

Nếu kiểm tra hợp lệ (validation / 검증) chỉ đổi border thành đỏ, người dùng (user / 사용자) không phân biệt màu hoặc screen reader có thể không biết có lỗi.

Tối thiểu lỗi (error / 오류) trạng thái (state / 상태) nên có văn bản (text / 텍스트) message và focus/điều hướng (navigation / 내비게이션) chiến lược (strategy / 전략). Nếu thành phần (component / 컴포넌트)/bản dựng (build / 빌드) hỗ trợ khả năng tiếp cận (accessibility / 접근성) attribute tương ứng, dùng theo official API thay vì DOM hack.

## 22. Không chỉnh DOM private để thêm khả năng tiếp cận (accessibility / 접근성) nếu API công khai (public API / 공개 API) có sẵn

WebSquare thành phần (component / 컴포넌트) có rendering cấu trúc (structure / 구조) do engine quản lý. Chèn trực tiếp attribute vào nội bộ (internal / 내부) DOM có thể mất sau re-render hoặc đổi giữa bản dựng (build / 빌드).

Ưu tiên:

```text
component public property/API
official accessibility option
supported class/style hook
```

DOM manipulation chỉ là last resort có regression bằng chứng (evidence / 증거).

## 23. đầu vào (input / 입력) phương thức (method / 메서드) và Korean/Vietnamese văn bản (text / 텍스트)

IME (Input Method Editor) làm key sự kiện (event / 이벤트) không luôn tương ứng một ký tự hoàn chỉnh. Đặc biệt Korean composition ghép jamo thành syllable, nên filtering dựa quá thấp vào keycode có thể phá đầu vào (input / 입력).

Official guide cũng lưu ý mẫu (pattern / 패턴) Korean cần hiểu phạm vi (range / 범위) syllable hoàn chỉnh thay vì suy từ English alphabet hành vi (behavior / 동작).

Quy tắc (rule / 규칙): dùng component-level supported đầu vào (input / 입력) điều khiển (control / 제어) và validate final giá trị (value / 값); đừng tự viết keydown filter naïve nếu không cần.

## 24. Paste và normalization

Người dùng (user / 사용자) có thể paste văn bản (text / 텍스트) có:

```text
full-width characters
non-breaking spaces
Unicode normalization differences
hidden newline
localized punctuation
```

Nếu nghiệp vụ (business / 비즈니스) key strict, normalize có chủ đích trước kiểm tra hợp lệ (validation / 검증). Nhưng không nên normalize đến mức thay đổi meaning mà người dùng (user / 사용자) không biết.

Ví dụ phone có thể strip formatting, nhưng password không được tự trim mù quáng nếu whitespace là hợp lệ.

## 25. Date/thời gian (time / 시간) và timezone ranh giới (boundary / 경계)

Nếu app chỉ xử lý cục bộ (local / 로컬) nghiệp vụ (business / 비즈니스) date, gửi `YYYY-MM-DD` có thể đủ. Nếu xử lý timestamp, phải xác định timezone/offset.

UI hiển thị `2026-09-22 09:00` không đủ để biết timestamp thật nếu hệ thống có người dùng (user / 사용자) ở nhiều timezone.

WebSquare chỉ là máy khách (client / 클라이언트) tầng (layer / 계층); timezone đặc tả hợp đồng (contract / 계약) phải đồng bộ với máy chủ (server / 서버)/API.

## 26. Number và floating-point

JavaScript number có floating-point ngữ nghĩa (semantics / 의미론). Với tiền tệ, không nên làm nghiệp vụ (business / 비즈니스) settlement dựa vào phép tính máy khách (client / 클라이언트) rồi coi là authoritative.

Máy khách (client / 클라이언트) có thể tính preview; máy chủ (server / 서버) nên dùng numeric/decimal mô hình (model / 모델) phù hợp và kiểm tra lại.

Xem chuẩn gốc (canonical / 정본) JavaScript docs để hiểu floating-point; WebSquare không thay đổi ngữ nghĩa (semantics / 의미론) này.

## 27. Form trạng thái (state / 상태) sau Submission lỗi (error / 오류)

Khi save thất bại (fail / 실패), UX tốt thường giữ người dùng (user / 사용자) đầu vào (input / 입력) để sửa/thử lại (retry / 재시도). Nếu callback lỗi (error / 오류) reset DataMap hoặc reload page vô điều kiện, người dùng (user / 사용자) mất dữ liệu.

Thiết kế rõ:

```text
transport error → giữ edit state
business validation error → map message về field nếu có thể
success → commit/reset row status theo contract
```

Không gom mọi callback vào `reload()`.

## 28. Double submit và focus phản hồi (feedback / 피드백)

Khi người dùng (user / 사용자) click Save, disable/guard duplicate yêu cầu (request / 요청) là hợp lý. Nhưng nếu yêu cầu (request / 요청) thất bại (fail / 실패), phải restore năng lực (capability / 역량).

Máy trạng thái (state machine / 상태 머신):

```text
idle
→ validating
→ submitting
→ success | failure
→ idle
```

Nếu button bị disabled trước kiểm tra hợp lệ (validation / 검증) rồi kiểm tra hợp lệ (validation / 검증) thất bại (fail / 실패) mà không re-enable, screen bị stuck.

## 29. tệp (file / 파일) upload là trust ranh giới (boundary / 경계) lớn

WebSquare có Upload/MultiUpload và máy chủ (server / 서버) cấu hình (config / 설정) cho giới hạn upload. Nhưng tệp (file / 파일) upload bảo mật (security / 보안) không dừng ở máy khách (client / 클라이언트) extension check.

Máy chủ (server / 서버) phải xem xét:

```text
size limit
allowed content/type
safe generated filename
path traversal
malware scanning theo policy
storage isolation
authorization
```

Máy khách (client / 클라이언트) accept/filter chỉ cải thiện UX.

## 30. Excel import/export là dữ liệu (data / 데이터) ranh giới (boundary / 경계)

Grid Excel tính năng (feature / 기능) tiện cho enterprise workflow nhưng tạo thêm trường hợp biên (edge case / 경계 사례):

```text
large file memory
column mapping
formula/value distinction
encoding
invalid rows
partial success
permission/sensitive export
```

Nếu import 10.000 row, kiểm tra hợp lệ (validation / 검증) từng cell bằng UI callback không nhất thiết là kiến trúc (architecture / 아키텍처) tốt. Có thể cần server-side batch kiểm tra hợp lệ (validation / 검증) và trả structured lỗi (error / 오류) danh sách (list / 목록).

## 31. Localization của máy chủ (server / 서버) message

Có hai chiến lược (strategy / 전략) phổ biến.

Máy chủ (server / 서버) trả localized final message theo locale yêu cầu (request / 요청).

Hoặc máy chủ (server / 서버) trả stable lỗi (error / 오류) mã (code / 코드) + parameters, máy khách (client / 클라이언트) map sang ngôn ngữ (language / 언어) pack.

Chiến lược (strategy / 전략) thứ hai giúp máy khách (client / 클라이언트) consistency nhưng cần đặc tả hợp đồng (contract / 계약) versioning. chiến lược (strategy / 전략) đầu đơn giản hơn nhưng máy chủ (server / 서버) phải biết locale và UI khó format field-specific message nếu payload nghèo.

Điều quan trọng là chọn rõ, không trộn tùy endpoint.

## 32. cấp cao (senior / 시니어) checklist cho một form môi trường vận hành (production / 운영 환경)

Trước khi coi form hoàn tất, kiểm tra:

```text
canonical value format đã rõ chưa?
client validation và server validation có boundary rõ chưa?
cross-field rule có bị duplicate không?
error có actionable không?
keyboard flow có dùng được không?
popup đóng có trả focus hợp lý không?
locale khác có overflow không?
missing translation có detect được không?
readOnly/hidden có bị hiểu nhầm thành security không?
large Grid + accessibility option đã đo performance chưa?
```

## 33. trường hợp (case / 사례) study: form chuyển khoản nội bộ

Người dùng (user / 사용자) nhập account, amount và memo. đầu vào (input / 입력) thành phần (component / 컴포넌트) có thể giới hạn amount theo numeric biểu diễn (representation / 표현) và hiển thị separator. DataMap giữ chuẩn gốc (canonical / 정본) amount. máy khách (client / 클라이언트) kiểm tra required, amount > 0 và một số limit UX-known. Khi Submit, máy chủ (server / 서버) xác thực account tồn tại, người dùng (user / 사용자) được phép chuyển, balance đủ, limit theo chính sách (policy / 정책) hiện tại và giao dịch (transaction / 트랜잭션) bất biến (invariant / 불변식). Nếu máy chủ (server / 서버) trả lỗi (error / 오류) mã (code / 코드) `LIMIT_EXCEEDED`, máy khách (client / 클라이언트) map sang localized message và focus amount. Nếu success, UI hiển thị tham chiếu (reference / 참조) ID từ máy chủ (server / 서버).

Điểm chính: mỗi tầng (layer / 계층) chỉ làm điều nó có đủ authority để chứng minh.

## 34. liên kết (connection / 연결) với thư viện (library / 라이브러리)

Thành phần (component / 컴포넌트)/binding ngữ nghĩa (semantics / 의미론): [02 — Components, Events & Data Binding](02_components_events_binding.md).

Submission và trust ranh giới (boundary / 경계): [03 — DataCollection & Submission](03_data_collection_submission.md).

Grid hiệu năng (performance / 성능)/bảo mật (security / 보안): [05 — GridView, CRUD & Enterprise Screen Patterns](05_gridview_crud_patterns.md) và [06 — Debugging, Performance, Security & Production](06_debugging_performance_security.md).

JavaScript number, string, Unicode và trình duyệt (browser / 브라우저) hành vi (behavior / 동작) được giữ ở chuẩn gốc (canonical / 정본) JavaScript nhánh học (track / 트랙).

## Nguồn chính thức nên đối chiếu

WebSquare5 SP5 — 입출력 제어: `https://docs1.inswave.com/sp5_user_guide/a91097396def6ee2`

WebSquare5 SP5 — 다국어 설정 가이드: `https://docs1.inswave.com/sp5_user_guide/73c59bba42ccbcd4`

WebSquare5 SP5 — máy khách (client / 클라이언트).cấu hình (config / 설정).xml: `https://docs1.inswave.com/sp5_user_guide/db5edae0d31101bd`

WebSquare5 SP5 — GridView senseReader guide: `https://docs1.inswave.com/sp5_user_guide/8313cd0f3e625bdf`

WebSquare5 SP5 — 파일 업로드/다운로드 가이드: `https://docs1.inswave.com/sp5_user_guide/2142a003497a4f9a`

Thuộc tính (property / 속성)/API cụ thể có thể thay đổi theo engine bản dựng (build / 빌드); môi trường vận hành (production / 운영 환경) phải kiểm tra tham chiếu (reference / 참조) đúng bản dựng (build / 빌드).

> **Bàn giao:** Sau **Nguồn chính thức nên đối chiếu**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 platform runtime page model](./01_platform_runtime_page_model.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
