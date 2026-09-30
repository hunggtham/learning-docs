# 09 — Nhà ở và tài chính nhà ở (Housing / 주거 재무)

## Định vị

Nhà ở (housing / 주거) thường là một trong những khoản chi lớn nhất của hộ gia đình và có thể tạo nghĩa vụ kéo dài hàng chục năm. Sau [06 — Loans & Debt](./06-loans-debt.md), [07 — Insurance](./07-insurance.md) và [08 — Taxes](./08-taxes.md), ta đã có đủ công cụ để phân tích thuê hay mua mà không rút gọn thành “thuê là mất tiền” hoặc “mua nhà luôn là đầu tư tốt”.

Housing vừa là nhu cầu tiêu dùng, vừa có thể là tài sản và nguồn leverage. Phần bất động sản như asset class cho portfolio thuộc [Investing](../investing/README.md); chapter này chỉ xem quyết định nơi ở ở cấp cá nhân/hộ gia đình.

## Thuê và mua cung cấp cùng một dịch vụ cơ bản

Cả thuê (renting / 임차) và sở hữu (homeownership / 주택소유) đều mua quyền sử dụng nhà ở theo thời gian. Khác biệt nằm ở cấu trúc chi phí, rủi ro, tính linh hoạt và quyền sở hữu residual value.

Người thuê thường trả rent và một số phí/utilities. Chủ nhà có thể trả mortgage, interest, property tax, insurance, maintenance, repair, association fee và transaction costs. Vì thế so sánh **rent với toàn bộ mortgage payment** vẫn chưa chính xác: một phần mortgage payment giảm principal và xây equity, trong khi nhiều chi phí sở hữu là chi phí thực không tạo equity.

## Down payment và leverage

Khoản trả trước (down payment / 계약금·자기자본) là phần giá mua được tài trợ bằng vốn của người mua. Phần còn lại có thể là mortgage.

Nếu nhà giá 500 và down payment 100, debt 400, initial equity xấp xỉ 100 trước chi phí giao dịch. Đây là leverage:

```text
Asset = 500
Debt = 400
Equity = 100
```

Nếu giá nhà tăng 10% lên 550, equity trước các yếu tố khác tăng từ 100 lên 150, tức 50%. Nếu giá giảm 10% xuống 450, equity còn 50, giảm 50%. Leverage khuếch đại cả upside lẫn downside của vốn chủ.

Điều này giải thích vì sao không thể đánh giá affordability chỉ bằng việc ngân hàng chấp nhận cho vay.

## Mortgage payment không phải toàn bộ housing cost

Khoản trả mortgage (mortgage payment / 주택담보대출 상환액) thường gồm principal và interest, đôi khi kèm escrow cho tax/insurance tùy hệ thống. Nhưng tổng chi phí sở hữu (total cost of ownership / 총소유비용) rộng hơn:

```text
interest
+ taxes
+ insurance
+ maintenance/repairs
+ association/management fees
+ transaction costs
+ opportunity cost of equity/down payment
+ utilities differences
```

Principal reduction không hoàn toàn là “chi phí” vì nó chuyển cash thành home equity, nhưng vẫn là **cash-flow requirement**. Một hộ có thể xây equity nhưng vẫn thiếu cash để sống nếu payment quá cao.

## Chi phí giao dịch và thời gian nắm giữ

Mua/bán nhà thường có môi giới, legal/registration fees, taxes, appraisal, inspection và moving costs tùy jurisdiction. Các chi phí một lần này làm quyết định sở hữu nhạy với thời gian ở.

Nếu dự kiến chuyển việc hoặc quốc gia sớm, flexibility của thuê có thể có giá trị lớn. Nếu ở lâu, chi phí giao dịch được phân bổ trên nhiều năm hơn. Vì vậy rent-vs-buy không có câu trả lời chung mà thiếu **expected holding period**.

## Maintenance không phải biến ngẫu nhiên bằng 0

Nhà xuống cấp. Roof, heating/cooling, plumbing, appliances, waterproofing, common areas và renovation đều có vòng đời. Dùng một tỷ lệ cố định của giá nhà làm maintenance có thể hữu ích cho rough planning nhưng không phải quy luật tự nhiên; loại nhà, tuổi, climate và building management khác nhau.

Mô hình tốt hơn là lập sinking fund theo các hạng mục lớn dự kiến:

```text
Expected future repair cost / years until repair
→ annual reserve contribution
```

Điều này biến một hóa đơn lớn bất ngờ thành chi phí được tích lũy dần.

## Affordability và stress test

Affordability không chỉ là payment tháng hiện tại. Cần thử ít nhất các kịch bản:

```text
thu nhập giảm 20%
lãi suất reset tăng
maintenance lớn xảy ra cùng năm
property tax/management fee tăng
một người trong household tạm nghỉ việc
```

Nếu chỉ cần một cú sốc nhỏ đã buộc dùng credit card hoặc bán tài sản dài hạn, cấu trúc housing có thể quá căng dù DTI ban đầu được lender chấp nhận.

## Rent vs buy: framework thay vì slogan

Có thể chia quyết định thành bốn lớp:

### 1. Nhu cầu sống

Vị trí, diện tích, commute, trường học, ổn định gia đình và quyền sửa đổi không gian. Đây là utility, không nên giả vờ mọi yếu tố đều quy về ROI.

### 2. Dòng tiền

So sánh rent với **chi phí sở hữu không tạo equity** cộng cash-flow burden của principal. Đưa insurance, tax, maintenance và fees vào.

### 3. Bảng cân đối

Down payment làm giảm cash nhưng tăng home equity. Mortgage tăng liability. Kiểm tra sau giao dịch còn bao nhiêu liquid assets.

### 4. Optionality và risk

Khả năng chuyển nơi ở, concentration risk, leverage, rate reset, job mobility và price risk. Nhà ở thường là tài sản lớn, không đa dạng hóa và khó bán nhanh.

## Nhà ở không phải lúc nào cũng là “investment” theo nghĩa portfolio

Primary residence có thể tăng giá và xây equity, nhưng đồng thời cung cấp housing consumption. Return thực sự phải tính transaction costs, financing, maintenance, tax và giá trị dịch vụ nhà ở. So sánh trực tiếp headline house-price growth với stock-market return thường sai vì hai con số không cùng basis.

Nếu mục tiêu là đầu tư real estate thay vì chỗ ở, chuyển sang owner phù hợp trong [Investing](../investing/README.md).

## Kết luận và hướng đọc tiếp

Housing là bài toán kết hợp **consumption + financing + leverage + liquidity + life flexibility**. Mua không tự động tốt hơn thuê, và rent không tự động là “ném tiền đi”.

Sau housing, [10 — Car Finance](./10-car-finance.md) áp dụng cùng mô hình vào một tài sản thường giảm giá: tách purchase price khỏi total cost of ownership, xem financing và depreciation thay vì chỉ hỏi monthly payment.
