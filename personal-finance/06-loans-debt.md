# 06 — Khoản vay và nợ (Loans & Debt / 대출과 부채)

## Định vị

[05 — Credit](./05-credit.md) giải thích khả năng sử dụng sức mua trước và thanh toán sau. Chapter này đi xuống cấp hợp đồng: một khoản vay (loan / 대출) tạo ra tiền gốc (principal / 원금), lãi, lịch thanh toán và các quyền/nghĩa vụ cụ thể. Mục tiêu không phải gắn nhãn “nợ tốt/nợ xấu” đơn giản, mà hiểu **nợ thay đổi dòng tiền, bảng cân đối và rủi ro như thế nào**.

## Nợ là nghĩa vụ trên bảng cân đối

Nợ phải trả (liability / 부채) là nghĩa vụ kinh tế với bên khác. Khi vay 100 để mua một tài sản trị giá 100, tài sản tăng 100 nhưng nợ cũng tăng 100; tài sản ròng (net worth / 순자산) chưa tự nhiên tăng chỉ vì sở hữu món đồ.

Điều thay đổi quan trọng là hộ gia đình có thêm nghĩa vụ dòng tiền trong tương lai. Vì vậy mỗi khoản nợ phải được đọc ở hai mặt:

```text
Balance sheet: còn nợ bao nhiêu?
Cash flow: mỗi kỳ phải trả bao nhiêu và trong bao lâu?
```

Một người có tài sản ròng dương vẫn có thể vỡ dòng tiền nếu khoản trả hàng tháng vượt khả năng thanh toán.

## Secured và unsecured debt

Nợ có tài sản bảo đảm (secured debt / 담보부채) gắn với tài sản mà lender có quyền xử lý theo hợp đồng/pháp luật nếu borrower không thực hiện nghĩa vụ, ví dụ nhiều khoản mortgage hoặc auto loan. Nợ không có tài sản bảo đảm (unsecured debt / 무담보부채) không gắn một tài sản cụ thể theo cùng cơ chế, ví dụ nhiều khoản personal loan hoặc credit-card balance.

Secured loan thường có thể rẻ hơn do lender có collateral, nhưng rủi ro đối với borrower bao gồm mất tài sản thiết yếu. Vì vậy lãi suất thấp hơn không có nghĩa rủi ro đời sống thấp hơn.

## Amortization: khoản trả được chia như thế nào

Với khoản vay amortizing có lãi suất cố định và khoản trả đều, mỗi payment thường gồm một phần lãi và một phần giảm gốc. Ban đầu, khi dư nợ cao, phần lãi thường lớn hơn; về sau phần giảm gốc tăng.

Công thức khoản trả đều cho principal `P`, lãi suất mỗi kỳ `r`, tổng số kỳ `n` là:

```text
Payment = P × r(1+r)^n / ((1+r)^n − 1)
```

Không cần học thuộc để quản lý tài chính, nhưng cần hiểu hệ quả: **kéo dài thời hạn giảm payment hàng tháng nhưng thường làm tăng tổng lãi** nếu các điều kiện khác giống nhau.

Khi xem một loan offer, luôn tách:

```text
purchase price
− down payment
= amount financed
+ interest over time
+ fees/insurance/add-ons required by contract
= total economic cost
```

## DTI và khả năng chịu nợ

Tỷ lệ nợ trên thu nhập (debt-to-income ratio / 총부채상환비율) thường so sánh nghĩa vụ nợ định kỳ với thu nhập theo định nghĩa của hệ thống. Công thức khái quát:

```text
DTI = periodic debt payments / periodic income
```

Nhưng lender DTI và household affordability không nhất thiết giống nhau. DTI có thể không phản ánh đầy đủ chi phí trẻ em, hỗ trợ gia đình, thuế, thuê nhà, bảo hiểm hoặc biến động thu nhập. Vì thế nó là chỉ báo, không phải phán quyết cuối.

Một stress test hữu ích hơn là giả định thu nhập giảm hoặc chi phí thiết yếu tăng rồi kiểm tra payment có còn bền vững không.

## Fixed, variable và refinancing

Nợ lãi cố định (fixed-rate debt / 고정금리부채) tạo payment dễ dự báo hơn. Nợ lãi biến đổi (variable-rate debt / 변동금리부채) có thể thay đổi theo benchmark và điều kiện hợp đồng. Khi lãi thị trường tăng, payment hoặc thời hạn có thể thay đổi tùy cấu trúc.

Tái cấp vốn (refinancing / 대환대출) thay một khoản nợ bằng khoản mới. Nó chỉ có lợi kinh tế khi phần giảm chi phí hoặc cải thiện rủi ro lớn hơn phí, penalty, thời gian hoàn vốn và tác động kéo dài debt term. “Lãi suất mới thấp hơn” chưa đủ nếu refinancing reset khoản vay sang thời hạn dài hơn nhiều.

## Trả nợ sớm: toán học và thanh khoản

Nếu không có penalty, trả trước debt có chi phí cao thường tạo một “return” tương đương phần lãi tránh được, gần như chắc chắn so với việc tiếp tục chịu lãi. Nhưng dùng toàn bộ tiền mặt để trả nợ có thể phá hủy quỹ dự phòng (emergency fund / 비상자금), khiến một sự cố nhỏ phải vay lại với chi phí cao hơn.

Do đó quyết định nên xem đồng thời:

```text
interest saved
vs
liquidity lost
vs
alternative uses of cash
vs
prepayment terms
```

Không nên áp dụng “trả hết mọi nợ trước khi giữ cash” hoặc “luôn đầu tư thay vì trả nợ” như quy tắc phổ quát.

## Debt avalanche và debt snowball

Hai chiến lược phổ biến:

- Debt avalanche ưu tiên khoản có lãi suất hiệu dụng cao nhất sau khi trả minimum cho các khoản khác. Nếu thực hiện đúng, nó thường tối thiểu hóa chi phí lãi trong các điều kiện đơn giản.
- Debt snowball ưu tiên khoản có balance nhỏ nhất để tạo các mốc hoàn thành sớm. Nó có thể tạo động lực hành vi dù không luôn tối ưu tiền lãi.

Đây là ví dụ quan trọng về khác biệt giữa tối ưu toán học và khả năng thực thi. Phương án tốt chỉ có giá trị nếu người dùng duy trì được nó. Tuy nhiên với debt có penalty, teaser rate, secured collateral hoặc legal consequences, thứ tự không nên dựa duy nhất vào rate/balance.

## Consolidation không xóa nợ

Hợp nhất nợ (debt consolidation / 부채통합) gom nhiều khoản thành một khoản mới. Nó có thể giảm rate hoặc đơn giản hóa payment, nhưng không làm principal biến mất. Nếu sau consolidation người vay tiếp tục tạo dư nợ mới trên các line cũ, tổng leverage còn tăng.

Cần hỏi:

```text
new effective rate + fees?
new term?
secured or unsecured?
old accounts remain usable?
behavioral cause of debt fixed or not?
```

## Khi vấn đề đã vượt khỏi budgeting

Nếu payment tối thiểu cộng chi phí thiết yếu liên tục vượt thu nhập, hoặc có nguy cơ foreclosure, repossession, collection hay legal action, đây không còn là bài toán “tối ưu lãi suất” thông thường. Quyền của borrower và quy trình xử lý khác theo quốc gia; cần dùng nguồn chính thức hoặc tư vấn có thẩm quyền tại jurisdiction.

## Kết luận và hướng đọc tiếp

Nợ (debt / 부채) là **một chuỗi nghĩa vụ dòng tiền được tạo ra bởi hợp đồng**. Giá của nó gồm lãi, phí, mất linh hoạt và đôi khi cả rủi ro mất collateral. Sau khi đã nhìn rõ những rủi ro có thể tự giữ và những rủi ro quá lớn để tự gánh, [07 — Insurance](./07-insurance.md) sẽ giải thích cơ chế chuyển giao rủi ro qua pooling, premium, deductible và coverage.
