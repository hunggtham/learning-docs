# 08 — Thuế trong tài chính cá nhân (Taxes / 세금)

## Định vị

Sau khi xây dòng tiền, nợ và bảo hiểm, một phần quan trọng của “tiền thực sự có thể dùng” là thuế (tax / 세금). Chapter này không dạy luật thuế của một quốc gia cụ thể; mục tiêu là tạo mô hình để đọc payslip, so sánh gross với net, hiểu thuế suất biên và hiệu dụng, timing của thuế và tác động của các tài khoản ưu đãi thuế.

Luật, mức thuế, deduction, credit, reporting và deadline thay đổi theo quốc gia và năm. Mọi con số thực tế phải được kiểm tra từ cơ quan thuế chính thức tại jurisdiction đang áp dụng.

## Gross income và net income

Thu nhập gộp (gross income / 총소득) là thu nhập trước các khoản khấu trừ theo định nghĩa đang dùng. Thu nhập ròng (net income / 순소득) là phần còn lại sau các khoản thuế/khấu trừ tương ứng.

Trong personal finance, cần phân biệt thêm **take-home pay**: số tiền thực tế vào tài khoản sau withholding, social contributions, insurance hoặc các deduction khác từ payroll.

Một ngân sách không nên được xây từ salary headline nếu số tiền thực nhận thấp hơn đáng kể. Dòng tiền phải bắt đầu từ amount có thể chi tiêu thực tế và ghi riêng các khoản deduction mà người dùng có quyền thay đổi hoặc cần theo dõi.

## Thuế suất biên khác thuế suất hiệu dụng

Trong hệ thống thuế lũy tiến, thuế suất biên (marginal tax rate / 한계세율) là rate áp lên đơn vị thu nhập bổ sung trong bracket tương ứng. Nó **không có nghĩa toàn bộ thu nhập bị đánh ở bracket cao nhất**.

Thuế suất hiệu dụng (effective tax rate / 실효세율) có thể được biểu diễn khái quát:

```text
Effective tax rate = total tax / relevant income base
```

Ví dụ minh họa đơn giản, nếu các bracket giả định là:

```text
0–10: 0%
10–30: 10%
trên 30: 20%
```

Với thu nhập 40, phần 0–10 không chịu thuế, phần 10–30 chịu 10%, phần 30–40 chịu 20%. Không phải toàn bộ 40 chịu 20%. Mức thực tế của từng nước có deductions, credits và nhiều loại thuế khác nên phức tạp hơn.

## Deduction và credit

Khoản khấu trừ (tax deduction / 소득공제) thường làm giảm cơ sở tính thuế theo cơ chế luật quy định. Khoản tín dụng thuế (tax credit / 세액공제) thường làm giảm trực tiếp số thuế phải nộp theo điều kiện.

Hai khái niệm không tương đương. Giá trị kinh tế của deduction phụ thuộc marginal rate và luật, trong khi credit có thể có cấu trúc refundable/non-refundable hoặc giới hạn khác nhau.

Vì vậy câu “được trừ thuế” không có nghĩa chi 100 sẽ tiết kiệm 100. Cần hỏi chính xác **trừ khỏi taxable income hay trừ khỏi tax liability, với giới hạn nào**.

## Withholding không phải final tax

Khấu trừ tại nguồn (withholding / 원천징수) là cơ chế thu trước một phần thuế khi income được trả. Số đã withholding có thể cao hơn hoặc thấp hơn final liability sau khi tính cả năm, tùy hệ thống.

Nhận refund lớn không tự động nghĩa là “kiếm thêm tiền”; có thể chỉ là đã nộp thừa trong năm và được hoàn lại. Ngược lại, thiếu withholding có thể tạo khoản phải nộp lớn khi filing.

Trong cash-flow planning, refund hoặc tax bill nên được xem như kết quả của timing và estimation, không phải bonus/mất mát bất ngờ nếu có thể dự đoán.

## Các loại thuế chạm vào đời sống cá nhân

Tùy jurisdiction, người dân có thể gặp thuế thu nhập cá nhân (income tax / 소득세), payroll/social contributions, thuế tiêu dùng như VAT/sales tax, property tax, capital-gains tax, dividend/interest taxation, inheritance/gift tax hoặc vehicle-related taxes.

Library này không sao chép từng luật. Điều cần học là mapping:

```text
Sự kiện kinh tế nào xảy ra?
→ loại tax base nào bị kích hoạt?
→ ai có nghĩa vụ khai/nộp?
→ thời điểm nào?
→ deduction/credit/exemption nào có thể áp dụng?
→ tài liệu nào phải lưu?
```

Khi câu hỏi chuyển thành mức thuế cụ thể tại Hàn Quốc, Việt Nam hoặc quốc gia khác, phải dùng nguồn thuế chính thức tại thời điểm quyết định.

## Tax-deferred và tax-advantaged

Một số tài khoản hưu trí/tiết kiệm có ưu đãi thuế (tax-advantaged account / 세제혜택계좌). Cơ chế thường rơi vào một hoặc nhiều dạng:

- deduction/contribution benefit ở thời điểm nộp tiền;
- tăng trưởng hoãn thuế (tax-deferred growth / 과세이연);
- withdrawal đủ điều kiện được miễn/giảm thuế;
- employer/government contribution theo điều kiện.

Không thể đánh giá chỉ bằng “được giảm thuế hôm nay”. Cần xem contribution limit, lock-up, withdrawal tax, penalty, investment options, phí và tax rate hiện tại so với tương lai.

[11 — Retirement](./11-retirement.md) sẽ sử dụng khung này mà không giả định một hệ thống pension cụ thể.

## Thuế và quyết định đầu tư

Thuế có thể làm return sau thuế khác return trước thuế. Tuy nhiên `personal-finance/` chỉ giữ nguyên tắc “đánh giá sau thuế và sau phí”; tax treatment của securities, portfolio turnover, account location và strategy thuộc [Investing](../investing/README.md) khi mục tiêu là phân bổ vốn.

Một sai lầm phổ biến là để thuế chi phối toàn bộ quyết định: giữ một tài sản xấu chỉ vì sợ tax, vay thêm chỉ để lấy deduction, hoặc mua sản phẩm phức tạp vì nhãn “tax efficient”. Tax optimization là constraint, không thay thế economics cơ bản.

## Hồ sơ và operational discipline

Một hệ thống thuế cá nhân bền vững cần record keeping: payslips, annual statements, receipts đủ điều kiện, transaction records, contribution records và documents chứng minh basis nếu cần. Không đợi đến filing season mới tìm lại dữ liệu.

Một cấu trúc thực hành:

```text
year/
├── income/
├── withholding/
├── deductible-expenses/
├── investments/
├── housing/
└── filed-return-and-notices/
```

Tên folder có thể khác, nhưng mục tiêu là có audit trail rõ.

## Kết luận và hướng đọc tiếp

Thuế (tax / 세금) biến gross income thành net resources và ảnh hưởng timing của nhiều quyết định dài hạn. Ba điểm cần giữ: marginal rate khác effective rate; withholding khác final liability; “tax benefit” chỉ có ý nghĩa khi hiểu toàn bộ điều kiện.

Hai quyết định lớn mà thuế thường chạm tới là nhà và xe. [09 — Housing](./09-housing.md) bắt đầu với housing vì đây thường là khoản chi/nợ lớn nhất, nơi rent-vs-buy dễ bị biến thành khẩu hiệu thay vì phân tích total cost và flexibility.
