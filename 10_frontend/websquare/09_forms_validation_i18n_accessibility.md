# 09 — Forms, Validation, Internationalization & Accessibility

Màn hình WebSquare enterprise thường xoay quanh form nhập liệu, search condition, popup chọn dữ liệu và Grid edit. Vì vậy chất lượng của input/validation không chỉ là UX detail. Nó quyết định dữ liệu đi vào DataCollection có đáng tin đến mức nào, lỗi được phát hiện ở đâu, người dùng có hiểu được lỗi không, và màn hình có còn sử dụng được khi đổi ngôn ngữ, dùng bàn phím hoặc công cụ hỗ trợ hay không.

Chapter này tập trung vào một mental model quan trọng: **input control, validation, business invariant, internationalization và accessibility là các lớp khác nhau**. Một property UI không thể thay thế server validation; một regex không thể thay thế domain rule; một label dịch được không tự làm màn hình accessible.

## 1. Pipeline của dữ liệu nhập

Khi user nhập dữ liệu, đừng hình dung chỉ có một bước “Input nhận value”. Một flow thực tế thường gồm:

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

Ví dụ `allowChar="0-9"` có thể ngăn nhiều ký tự không phải số được gõ vào Input, nhưng nó không chứng minh giá trị là một employee number hợp lệ. `dataType="number"` có thể giúp parsing và format, nhưng không chứng minh số nằm trong business range. Server vẫn phải kiểm tra.

## 2. Input filtering không phải validation hoàn chỉnh

WebSquare hỗ trợ các property kiểm soát input như `allowChar`, `ignoreChar`, `dataType` tùy component/build. Đây là guard ở mức interaction.

Ví dụ:

```xml
<xf:input id="inputAge" dataType="number" />
```

hoặc một Input text chỉ cho phép pattern ký tự nhất định.

Nhưng input có thể đến từ nhiều nguồn ngoài keypress:

```text
paste
programmatic setValue
binding từ DataMap
response server
restore state
browser/autofill tùy environment
```

Vì vậy không nên suy luận “user không gõ được ký tự X” đồng nghĩa model không bao giờ có X.

## 3. Parsing, representation và domain value

Một field ngày tháng có ít nhất ba representation:

```text
user display: 2026.09.22
client canonical: 20260922 hoặc 2026-09-22
server/domain: LocalDate / DB DATE
```

Nếu không xác định canonical representation, code sẽ có nhiều nơi tự replace `.` hoặc `-`, tạo lỗi locale và edge case.

Rule tốt là chọn một representation ổn định cho boundary data rồi format ở UI layer.

Tương tự money:

```text
display: 1,234,567 원
canonical client payload: 1234567
server numeric type: decimal/integer theo domain
```

Không gửi display string nếu server contract thực sự cần numeric value.

## 4. Validation có nhiều cấp

Một field `amount` có thể đi qua các cấp:

**Syntactic validation**: có parse thành số không?

**Field validation**: amount có lớn hơn 0 không?

**Cross-field validation**: startDate <= endDate?

**Business validation**: amount có vượt hạn mức của user không?

**Authorization validation**: user có quyền thực hiện transaction này không?

**Persistence invariant**: unique key hoặc foreign key còn đúng tại thời điểm commit không?

UI chỉ có đủ context cho một phần trong số này.

## 5. Client validation phục vụ feedback nhanh

Client validation có giá trị lớn: user không phải gửi request mới biết field bắt buộc đang rỗng. Nhưng vai trò chính là **feedback và giảm request vô nghĩa**, không phải trust boundary.

Một pattern save:

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

Server vẫn validate payload lại độc lập.

## 6. Required không đồng nghĩa meaningful

Một field có value không có nghĩa value hợp lệ.

Ví dụ:

```text
" "
"000000"
"N/A"
```

có thể vượt qua kiểm tra non-empty nhưng vô nghĩa theo domain.

Do đó validator nên nói bằng domain language: `isValidEmployeeId`, `isValidDateRange`, `canSubmitApproval`, thay vì chỉ `notEmpty` ở mọi nơi.

## 7. Cross-field rule nên có một owner rõ

Ví dụ:

```text
fromDate <= toDate
```

Nếu rule này được copy vào `onchange` của hai Input, `onclick` Search và `beforeSubmission`, bốn bản có thể drift.

Tốt hơn là một function domain-level phía page:

```javascript
scwin.validateSearchPeriod = function () {
    var from = dmSearch.get("fromDate");
    var to = dmSearch.get("toDate");
    return !from || !to || from <= to;
};
```

Event handler có thể gọi nó để feedback sớm; save/search orchestration cũng gọi cùng rule trước request.

## 8. Error message phải gắn với hành động sửa được

Thông báo:

```text
Invalid input.
```

ít giá trị hơn:

```text
Ngày bắt đầu phải nhỏ hơn hoặc bằng ngày kết thúc.
```

Một error message tốt trả lời:

```text
Cái gì sai?
Ở đâu?
User sửa thế nào?
```

Không nên lộ stack trace, endpoint nội bộ hoặc raw server exception cho user.

## 9. Focus management sau validation

Khi form dài, chỉ alert lỗi nhưng không đưa focus về field sai làm user mất thời gian tìm.

Flow tốt thường là:

```text
collect validation result
→ show message/inline marker
→ focus first actionable invalid field
```

Nhưng focus phải tôn trọng component lifecycle. Nếu field nằm trong tab chưa render, cố focus ngay có thể fail. Khi đó cần activate/render container trước rồi focus.

## 10. Tab order là một phần interaction architecture

Keyboard user dựa vào thứ tự focus. Khi screen được sinh từ nhiều Group/WFrame/UDC, visual order và tab order có thể lệch nhau.

Không nên chỉ test bằng mouse. Một form production nên thử:

```text
Tab từ đầu đến cuối
Shift+Tab quay lại
Enter/Space trên control phù hợp
Popup open/close có trả focus hợp lý không
Disabled/hidden component có bị focus nhầm không
```

## 11. readOnly, disabled, hidden có semantics khác nhau

Các trạng thái UI này không nên được xem là synonym.

`readOnly` thường nghĩa user thấy value nhưng không edit trực tiếp.

`disabled` thường nghĩa control không interactive và behavior submit/focus có thể khác tùy component.

`hidden` nghĩa không hiển thị nhưng value/model vẫn có thể tồn tại.

Không property nào trong ba property này tạo authorization boundary. User có thể sửa request hoặc chạy script client.

## 12. Permission phải thay đổi capability, không chỉ decoration

UI có thể ẩn nút Delete nếu user không có permission để giảm confusion. Nhưng server endpoint Delete vẫn phải kiểm tra permission.

Mental model:

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

WebSquare5 hỗ trợ language pack và các property như `useLocale`, `localeRef` ở những component tương ứng. Đây là mechanism mapping key → localized text, nhưng domain design vẫn phải dùng stable semantic keys.

## 14. Stable locale key

Không nên dùng raw Korean sentence làm key:

```text
"저장하시겠습니까?"
```

rồi map sang English. Khi Korean wording đổi, key identity cũng đổi.

Tốt hơn:

```text
confirm.save
validation.required.employeeName
button.search
```

Key mô tả meaning, translation file mô tả wording.

## 15. `useLanguagePack` và runtime configuration

Theo SP5 official guide, client configuration có thể bật language pack và map language code tới file resource. Component hỗ trợ locale có thể dùng `localeRef` để lấy text.

Điểm cần reasoning không phải thuộc tên mọi property mà là hiểu pipeline:

```text
runtime language decision
→ load language resource
→ resolve locale key
→ component displays localized value
```

Nếu text không đổi khi switch language, debug theo pipeline này thay vì sửa component ngẫu nhiên.

## 16. Missing translation là data-quality problem

Khi locale key không tồn tại, behavior fallback phụ thuộc config/component/build. Production nên phát hiện missing key sớm hơn user.

Có thể audit bằng:

```text
collect keys từ source
compare với language files
report missing/unused keys
```

Nếu project không có automation, ít nhất regression test các screen quan trọng ở mọi supported language.

## 17. Text expansion và layout

English, Vietnamese và Korean có độ dài khác nhau. Một button vừa đẹp với `조회` có thể không đủ cho `Search transactions`.

Do đó layout không nên phụ thuộc quá chặt fixed width nếu product cần đa ngôn ngữ.

Kiểm tra:

```text
button label overflow
Grid header width
validation message wrapping
popup title
placeholder
```

I18n là một input cho layout architecture.

## 18. Accessibility là capability của user

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

WebSquare component cung cấp một phần semantics; developer vẫn phải cấu hình và test.

## 19. Grid accessibility có performance trade-off thật

Official WebSquare guide lưu ý các option liên quan Grid accessibility như `senseReader` có thể làm tăng DOM/memory cost, đặc biệt khi đồng thời hiển thị số lượng row lớn. Đây là ví dụ quan trọng: accessibility và performance không nên bị đặt thành hai mục tiêu đối nghịch kiểu “chọn một”.

Thay vào đó phải thiết kế dataset/rendering strategy phù hợp:

```text
server paging
virtual/native rendering khi phù hợp
không render hàng chục nghìn row cùng lúc
đo heap/DOM/render time
```

Không nên tắt accessibility chỉ vì screen được thiết kế với dataset phi thực tế.

## 20. Label và context

Một Input chỉ có placeholder không phải lúc nào cũng cung cấp semantic label ổn định. Placeholder biến mất khi user nhập và có thể khó đọc.

Form quan trọng nên có label/context rõ. Với Grid, header phải diễn đạt meaning của column, không chỉ viết abbreviation nội bộ mà user không hiểu.

## 21. Error accessibility

Nếu validation chỉ đổi border thành đỏ, user không phân biệt màu hoặc screen reader có thể không biết có lỗi.

Tối thiểu error state nên có text message và focus/navigation strategy. Nếu component/build hỗ trợ accessibility attribute tương ứng, dùng theo official API thay vì DOM hack.

## 22. Không chỉnh DOM private để thêm accessibility nếu public API có sẵn

WebSquare component có rendering structure do engine quản lý. Chèn trực tiếp attribute vào internal DOM có thể mất sau re-render hoặc đổi giữa build.

Ưu tiên:

```text
component public property/API
official accessibility option
supported class/style hook
```

DOM manipulation chỉ là last resort có regression evidence.

## 23. Input method và Korean/Vietnamese text

IME (Input Method Editor) làm key event không luôn tương ứng một ký tự hoàn chỉnh. Đặc biệt Korean composition ghép jamo thành syllable, nên filtering dựa quá thấp vào keycode có thể phá input.

Official guide cũng lưu ý pattern Korean cần hiểu range syllable hoàn chỉnh thay vì suy từ English alphabet behavior.

Rule: dùng component-level supported input control và validate final value; đừng tự viết keydown filter naïve nếu không cần.

## 24. Paste và normalization

User có thể paste text có:

```text
full-width characters
non-breaking spaces
Unicode normalization differences
hidden newline
localized punctuation
```

Nếu business key strict, normalize có chủ đích trước validation. Nhưng không nên normalize đến mức thay đổi meaning mà user không biết.

Ví dụ phone có thể strip formatting, nhưng password không được tự trim mù quáng nếu whitespace là hợp lệ.

## 25. Date/time và timezone boundary

Nếu app chỉ xử lý local business date, gửi `YYYY-MM-DD` có thể đủ. Nếu xử lý timestamp, phải xác định timezone/offset.

UI hiển thị `2026-09-22 09:00` không đủ để biết timestamp thật nếu hệ thống có user ở nhiều timezone.

WebSquare chỉ là client layer; timezone contract phải đồng bộ với server/API.

## 26. Number và floating-point

JavaScript number có floating-point semantics. Với tiền tệ, không nên làm business settlement dựa vào phép tính client rồi coi là authoritative.

Client có thể tính preview; server nên dùng numeric/decimal model phù hợp và kiểm tra lại.

Xem canonical JavaScript docs để hiểu floating-point; WebSquare không thay đổi semantics này.

## 27. Form state sau Submission error

Khi save fail, UX tốt thường giữ user input để sửa/retry. Nếu callback error reset DataMap hoặc reload page vô điều kiện, user mất dữ liệu.

Thiết kế rõ:

```text
transport error → giữ edit state
business validation error → map message về field nếu có thể
success → commit/reset row status theo contract
```

Không gom mọi callback vào `reload()`.

## 28. Double submit và focus feedback

Khi user click Save, disable/guard duplicate request là hợp lý. Nhưng nếu request fail, phải restore capability.

State machine:

```text
idle
→ validating
→ submitting
→ success | failure
→ idle
```

Nếu button bị disabled trước validation rồi validation fail mà không re-enable, screen bị stuck.

## 29. File upload là trust boundary lớn

WebSquare có Upload/MultiUpload và server config cho giới hạn upload. Nhưng file upload security không dừng ở client extension check.

Server phải xem xét:

```text
size limit
allowed content/type
safe generated filename
path traversal
malware scanning theo policy
storage isolation
authorization
```

Client accept/filter chỉ cải thiện UX.

## 30. Excel import/export là data boundary

Grid Excel feature tiện cho enterprise workflow nhưng tạo thêm edge case:

```text
large file memory
column mapping
formula/value distinction
encoding
invalid rows
partial success
permission/sensitive export
```

Nếu import 10.000 row, validation từng cell bằng UI callback không nhất thiết là architecture tốt. Có thể cần server-side batch validation và trả structured error list.

## 31. Localization của server message

Có hai strategy phổ biến.

Server trả localized final message theo locale request.

Hoặc server trả stable error code + parameters, client map sang language pack.

Strategy thứ hai giúp client consistency nhưng cần contract versioning. Strategy đầu đơn giản hơn nhưng server phải biết locale và UI khó format field-specific message nếu payload nghèo.

Điều quan trọng là chọn rõ, không trộn tùy endpoint.

## 32. Senior checklist cho một form production

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

## 33. Case study: form chuyển khoản nội bộ

User nhập account, amount và memo. Input component có thể giới hạn amount theo numeric representation và hiển thị separator. DataMap giữ canonical amount. Client kiểm tra required, amount > 0 và một số limit UX-known. Khi Submit, server xác thực account tồn tại, user được phép chuyển, balance đủ, limit theo policy hiện tại và transaction invariant. Nếu server trả error code `LIMIT_EXCEEDED`, client map sang localized message và focus amount. Nếu success, UI hiển thị reference ID từ server.

Điểm chính: mỗi layer chỉ làm điều nó có đủ authority để chứng minh.

## 34. Connection với library

Component/binding semantics: [02 — Components, Events & Data Binding](02_components_events_binding.md).

Submission và trust boundary: [03 — DataCollection & Submission](03_data_collection_submission.md).

Grid performance/security: [05 — GridView, CRUD & Enterprise Screen Patterns](05_gridview_crud_patterns.md) và [06 — Debugging, Performance, Security & Production](06_debugging_performance_security.md).

JavaScript number, string, Unicode và browser behavior được giữ ở canonical JavaScript track.

## Nguồn chính thức nên đối chiếu

WebSquare5 SP5 — 입출력 제어: `https://docs1.inswave.com/sp5_user_guide/a91097396def6ee2`

WebSquare5 SP5 — 다국어 설정 가이드: `https://docs1.inswave.com/sp5_user_guide/73c59bba42ccbcd4`

WebSquare5 SP5 — client.config.xml: `https://docs1.inswave.com/sp5_user_guide/db5edae0d31101bd`

WebSquare5 SP5 — GridView senseReader guide: `https://docs1.inswave.com/sp5_user_guide/8313cd0f3e625bdf`

WebSquare5 SP5 — 파일 업로드/다운로드 가이드: `https://docs1.inswave.com/sp5_user_guide/2142a003497a4f9a`

Property/API cụ thể có thể thay đổi theo engine build; production phải kiểm tra reference đúng build.