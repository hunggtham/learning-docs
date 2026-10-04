# 6. Lợi suất, tín dụng, duration và thị trường trái phiếu

Bài 5 đã xác định các dòng tiền hợp đồng. Bài cuối giải quyết câu hỏi vận hành: thị trường quy đổi dòng tiền đó thành lợi suất thế nào, giá nhạy ra sao với lãi suất, và chỉ số/đường cong truyền thông tin gì? Đây là nơi phân biệt coupon, IRR, YTM, credit spread, duration và total return.

## 1. Discount rate, IRR và YTM

Discount rate là suất dùng để quy đổi dòng tiền về hiện tại. IRR (Internal Rate of Return) là nghiệm làm NPV bằng 0 cho một chuỗi dòng tiền. YTM (Yield to Maturity) là IRR của trái phiếu nếu giữ đến đáo hạn và các coupon được tái đầu tư theo cùng lợi suất; đó là quy đổi mô hình, không phải realized return nếu bán sớm, tái đầu tư khác mức hoặc issuer vỡ nợ. Coupon rate chỉ là tỷ lệ trên mệnh giá, không đồng nghĩa YTM.

## 2. Đường cong lợi suất

Yield curve xếp lợi suất theo kỳ hạn. Source trình bày bốn cách giải thích: Expectations Theory coi lợi suất dài hạn phản ánh lãi suất ngắn hạn kỳ vọng; Liquidity Premium Theory cộng phần bù cho việc nắm giữ kỳ hạn dài; Market Segmentation Theory cho rằng cung–cầu mỗi bucket kỳ hạn tương đối tách biệt; Preferred Habitat Theory cho phép nhà đầu tư có kỳ hạn ưa thích nhưng dịch chuyển khi phần bù đủ lớn. Bốn theory là các lăng kính bổ sung, không phải bốn dự báo đồng nhất.

Đường cong dốc lên có thể phản ánh tăng trưởng/lạm phát kỳ vọng hoặc term premium; đường cong đảo có thể phản ánh kỳ vọng hạ lãi suất. Không được đọc hình dạng mà bỏ qua regime, thanh khoản, cung trái phiếu và chính sách. Những kênh vĩ mô rộng hơn thuộc [Monetary System, Liquidity and Crisis Transmission](../../investing/04_economics/04_MONETARY_SYSTEM_LIQUIDITY_AND_CRISIS_TRANSMISSION.md).

## 3. Tín dụng và xếp hạng

Default risk là khả năng issuer không trả đủ hoặc đúng hạn. Credit rating của Moody’s, S&P, Fitch và các tổ chức khác là đánh giá tương đối về credit risk; rating không phải bảo hiểm và có thể chậm hơn thông tin thị trường. Spread so với trái phiếu tham chiếu bù cho default, liquidity, tax và các rủi ro khác. High-yield/junk bond có spread và xác suất tổn thất cao hơn trong textbook, nhưng lợi suất cao không tự bù đủ nếu recovery thấp hoặc thanh khoản biến mất.

## 4. Duration và convexity

Macaulay duration là thời gian bình quân gia quyền theo giá trị hiện tại của các dòng tiền. Modified duration xấp xỉ độ nhạy phần trăm của giá với thay đổi lợi suất:

```text
ΔP / P ≈ −Modified Duration × Δy
```

Duration dài hơn thường nghĩa là giá nhạy hơn với lãi suất; coupon thấp và maturity dài thường làm duration tăng. Convexity bổ sung độ cong của quan hệ giá–lợi suất, giúp approximation tốt hơn khi cú sốc lớn:

```text
ΔP/P ≈ −D_mod·Δy + 1/2·Convexity·(Δy)^2
```

Duration không dự báo default, spread widening hay prepayment. Với callable/MBS, dòng tiền thay đổi theo lãi suất nên duration có thể biến thiên (negative convexity). Đây là boundary cần giữ khi chuyển từ trái phiếu chính phủ sang sản phẩm cấu trúc.

## 5. Benchmark và bond index

Một bond index phải xác định universe, maturity, rating, currency, trọng số và cách xử lý phát hành mới, đáo hạn, coupon và default. Price index chỉ theo giá; coupon index theo coupon; yield index theo lợi suất; total-return index tái đầu tư coupon và phản ánh cả giá lẫn income. Benchmark portfolio source nêu dùng để so sánh, không phải danh mục “tối ưu” cho mọi nhà đầu tư.

Source nhắc các bond index Hàn Quốc, gồm KSDA-BLP Korean Bond Index và các phân nhóm market/bond subindex. Tên mã, thành phần và phương pháp hiện tại cần xác minh lại trước khi sử dụng; route chỉ giữ nguyên tắc construction vì OCR không đủ cho mọi chi tiết.

## 6. Repo và cơ chế thị trường

Repo là giao dịch bán và mua lại, về kinh tế gần khoản vay có tài sản thế chấp. Haircut, margin, collateral quality và haircut change quyết định đòn bẩy và liquidity. Khi giá tài sản giảm hoặc haircut tăng, bên vay có thể phải bổ sung tài sản hoặc bán cưỡng bức. Vì vậy repo nối đường cong lợi suất với funding và stress thị trường; không nên đọc bond market như một bảng giá tĩnh.

## 7. Source-question test

Để giải câu hỏi cuối sách, người học cần: (1) phân biệt coupon với YTM; (2) suy ra giá giảm khi lợi suất tăng; (3) chọn duration/convexity phù hợp; (4) phân biệt price index với total-return index; (5) nhận diện spread và rating là thước đo rủi ro, không phải bảo đảm. Các câu hỏi có số liệu hình/OCR không rõ được đánh `PARTIAL` trong coverage thay vì bịa đáp án.

## Chốt toàn Sách 2

Sách 2 tạo một knowledge graph: chu kỳ và chỉ báo ảnh hưởng dòng tiền; dòng tiền và rủi ro quyết định định giá; giá và khối lượng tạo tín hiệu; chiến lược biến tín hiệu thành exposure; trái phiếu biến thời hạn, tín dụng và funding thành lợi suất. Ranh giới cuối cùng là mô hình textbook không thay thế dữ liệu đúng thời điểm, prospectus hay quy định hiện hành. Để đi từ route này sang quy trình đầu tư hoàn chỉnh, quay lại [Investing README](../../investing/README.md) và [Full Investment Process](../../investing/07_integrated_case_studies/05_FULL_INVESTMENT_PROCESS_FROM_THESIS_TO_REVIEW.md).

