# 10 — Tài chính xe và tổng chi phí sở hữu (Car Finance / 자동차 금융)

## Định vị

[09 — Housing](./09-housing.md) cho thấy giá mua không bằng tổng chi phí sở hữu. Xe ô tô làm nguyên tắc đó rõ hơn vì phần lớn xe tiêu dùng là tài sản giảm giá (depreciating asset / 감가자산) nhưng vẫn có thể tạo khoản vay dài hạn. Chapter này tập trung vào **giá trị dịch vụ di chuyển**, depreciation, financing, insurance, maintenance và khả năng đổi xe.

## Giá niêm yết không phải giá kinh tế

Khi mua xe, cần tách ít nhất:

```text
vehicle price
+ taxes/registration
+ dealer or delivery fees
+ financing cost
+ insurance
+ fuel/charging
+ parking/tolls
+ maintenance/tires/repairs
− resale value
= approximate total cost of ownership
```

Một chiếc xe có purchase price thấp nhưng depreciation mạnh, insurance đắt hoặc maintenance cao có thể tốn hơn trong thời gian sở hữu.

## Depreciation là chi phí dù không thấy hóa đơn

Khấu hao kinh tế (depreciation / 감가상각) là phần giá trị thị trường xe giảm theo thời gian và sử dụng. Không có ai gửi hóa đơn “depreciation” hàng tháng, nên người mua dễ bỏ qua nó.

Nếu mua xe 30 và bán sau vài năm được 18, 12 đơn vị giá trị đã mất trước khi tính financing, maintenance hay tax. Đây thường là một trong các cost lớn nhất của ownership.

Không nên dùng một tỷ lệ depreciation cố định cho mọi xe. Model, tuổi, mileage, accident history, supply, technology shift và local market có thể làm resale value khác nhiều.

## Monthly payment có thể đánh lạc hướng

Dealer financing thường trình bày “mỗi tháng chỉ X”. Nhưng payment có thể giảm bằng cách:

- tăng down payment;
- kéo dài loan term;
- thêm balloon payment ở cuối;
- dùng promotional rate có điều kiện;
- thay đổi trade-in value.

Vì vậy hãy quay lại decomposition:

```text
amount financed
interest rate / APR-equivalent disclosure
term
total of payments
fees/add-ons
prepayment rules
```

Một khoản vay 84 tháng có thể làm xe trông “affordable” theo tháng nhưng kéo dài nghĩa vụ đến lúc xe đã cũ và repair cost tăng.

## Negative equity

Vốn chủ âm (negative equity / 마이너스 에쿼티) xảy ra khi giá trị thị trường của xe thấp hơn loan balance. Ví dụ xe trị giá 15 nhưng còn nợ 20.

Nếu đổi xe lúc này và dealer “rolls” 5 còn thiếu vào loan mới, người mua bắt đầu xe mới với debt lớn hơn giá trị xe mới tương ứng. Lặp lại chu kỳ có thể tạo debt rất khó thoát.

Trước khi trade-in, luôn tách:

```text
market value of current car
− loan payoff amount
= equity (positive or negative)
```

Đừng để dealer chỉ nói “payment mới”.

## Down payment: giảm debt nhưng giảm liquidity

Down payment lớn làm amount financed và interest nhỏ hơn, đồng thời giảm nguy cơ negative equity. Nhưng down payment lấy cash ra khỏi balance sheet.

Nếu dùng hết emergency fund để giảm car loan, một repair hoặc job loss có thể buộc dùng high-cost credit. Quyết định tối ưu cần cân giữa lãi tiết kiệm và liquidity còn lại, giống nguyên tắc ở [06 — Loans & Debt](./06-loans-debt.md).

## Insurance và deductible

Auto insurance có thể gồm liability, collision, comprehensive và các coverages khác tùy jurisdiction. Lender có thể yêu cầu coverage nhất định khi xe còn financing.

Khi so xe, insurance quote nên được lấy **trước khi mua** nếu có thể. Hai xe cùng price có premium khác nhau do repair cost, theft risk, driver profile hoặc rating rules.

Deductible cao có thể giảm premium nhưng yêu cầu emergency fund đủ để tự trả phần deductible khi có claim.

## Maintenance và consumables

Maintenance không chỉ là dầu máy. Tire, brake, battery, fluid, inspection, scheduled service và repair ngoài bảo hành cần được tính. Với EV, cấu trúc maintenance khác ICE nhưng battery condition, charging access, tire wear và resale risk vẫn quan trọng.

Một mô hình hữu ích là annualize các cost không xảy ra hàng tháng:

```text
annual expected tires + maintenance + registration + insurance
/ 12
= monthly reserve
```

Khoản reserve này cho thấy “true monthly cost” rõ hơn loan payment.

## New vs used không có winner tuyệt đối

Xe mới thường có warranty, ít repair uncertainty và financing tốt hơn trong một số thị trường, nhưng depreciation ban đầu thường lớn. Xe cũ giảm purchase price nhưng tăng uncertainty về condition, repair và history.

Quyết định nên dựa vào **cost per useful year** và reliability requirement thay vì chỉ giá mua. Một người cần xe để đi làm hằng ngày có thể định giá downtime rất cao; người ít dùng xe có bài toán khác.

## Lease và ownership

Thuê dài hạn/lease (vehicle lease / 자동차 리스) thường đổi payment thấp hơn và chu kỳ xe mới lấy việc không tích lũy full ownership, mileage/condition constraints và các fee cuối hợp đồng. Accounting cụ thể khác nhau nhưng câu hỏi kinh tế là:

```text
Tôi đang trả bao nhiêu để sử dụng xe trong N năm?
Tôi chịu residual-value risk hay lessor chịu?
Mileage/termination constraints đáng giá bao nhiêu?
```

Lease không tự động xấu hay tốt; nó là một cấu trúc mua dịch vụ sử dụng khác.

## Car affordability nên bắt đầu từ transport need

Trước khi chọn loan, hỏi liệu ownership có phải phương án giao thông hợp lý. Public transport, car sharing, taxi/ride-hailing, bicycle hoặc thuê xe theo nhu cầu có thể rẻ hơn ở nơi parking/insurance cao và mileage thấp.

Đây là personal finance: mục tiêu không phải tối đa hóa “chất lượng xe” mà tối ưu utility của mobility dưới budget và risk constraints.

## Kết luận và hướng đọc tiếp

Một chiếc xe là **dịch vụ di chuyển được cung cấp bởi một tài sản thường mất giá**, có financing và operating costs đi kèm. Monthly payment chỉ là một dòng trong total cost of ownership.

Sau các quyết định lớn hiện tại như housing và car, ta chuyển sang nghĩa vụ dài nhất: tài trợ cho giai đoạn không còn hoặc giảm thu nhập lao động. [11 — Retirement](./11-retirement.md) xây mental model về pension, contribution, compounding, longevity và sequence risk.
