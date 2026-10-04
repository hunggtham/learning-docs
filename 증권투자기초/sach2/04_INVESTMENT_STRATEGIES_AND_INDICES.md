# 4. Chiến lược đầu tư và chỉ số thị trường

Bài 3 cho ta các mô tả về giá; bài này hỏi khi nào biến chúng thành quy tắc phân bổ và cách đo kết quả. Một chiến lược không chỉ là tên phương pháp. Nó phải chỉ ra nguồn lợi suất, thời hạn, điều kiện vào–ra, chi phí, rủi ro và benchmark. Source đặt cạnh các chiến lược đơn giản, hiệu ứng quy mô, hiệu ứng danh mục và chỉ số cổ phiếu để người học thấy một kết quả có thể đến từ nhiều cơ chế.

## 1. Buy-and-hold, bình quân giá và dòng cổ tức

Buy-and-hold giữ tài sản qua thời gian, dựa vào tăng trưởng dòng tiền và tái đầu tư thay vì giao dịch thường xuyên. Lợi thế là chi phí thấp và ít phụ thuộc timing; giới hạn là chịu drawdown và không tự loại bỏ doanh nghiệp xấu. Dollar-cost averaging (bình quân giá định kỳ) chia vốn thành các lần mua đều nhau. Nó làm giảm rủi ro bỏ toàn bộ vốn ở một thời điểm, nhưng không bảo đảm lợi suất cao hơn đầu tư một lần khi thị trường tăng.

Cổ tức là phân phối tiền hoặc tài sản cho cổ đông; stock split thay đổi số cổ phiếu và giá danh nghĩa theo tỷ lệ nhưng không tự tạo giá trị kinh tế. Hãy điều chỉnh dữ liệu giá cho split và cổ tức khi tính total return, nếu không sẽ nhầm thay đổi kỹ thuật với lợi nhuận thật.

## 2. Hiệu ứng và quy tắc chiến lược

Source đề cập note, small-firm effect và formula plan. Các hiệu ứng này là quan sát thực nghiệm hoặc quy tắc đơn giản, không phải định luật. Hiệu ứng quy mô có thể biến mất sau phí, thay đổi cấu trúc thị trường hoặc dữ liệu mẫu. Formula plan cố định cách phân bổ theo điều kiện giá hoặc tỷ trọng; ưu điểm là kỷ luật, giới hạn là quy tắc cứng có thể gặp regime chưa từng thấy. Đánh giá chiến lược bằng chuỗi lợi suất, drawdown, turnover và rủi ro thanh khoản, không bằng vài giao dịch đẹp.

## 3. Portfolio effect

Portfolio effect xuất hiện vì tổng rủi ro phụ thuộc tương quan chứ không chỉ từng tài sản. Với hai tài sản, phương sai danh mục gồm phương sai riêng và hạng tử hiệp phương sai; khi tương quan thấp hơn 1, kết hợp có thể giảm biến động. Diversification không loại bỏ rủi ro thị trường, rủi ro thanh khoản hay tương quan tăng trong khủng hoảng. Vì vậy, “nhiều mã” không đồng nghĩa đa dạng hóa: các mã cùng ngành, cùng tiền tệ hoặc cùng factor vẫn có thể là một cược duy nhất.

Phần tính toán danh mục thuộc [Portfolio Risk, Allocation and Behavior](../../investing/01_foundations/02_PORTFOLIO_RISK_ALLOCATION_AND_BEHAVIOR.md). Trong route Sách 2, chỉ cần giữ mental model: chiến lược tạo exposure, danh mục cộng exposure, benchmark dùng để kiểm tra exposure đó có đáng giá không.

## 4. Chỉ số giá cổ phiếu

Stock Price Index tổng hợp nhiều giá cổ phiếu thành một thước đo. Price-weighted index cho trọng số theo giá danh nghĩa; market-cap-weighted index cho trọng số theo giá trị vốn hóa; equal-weighted index cho mỗi thành phần trọng số gần nhau. Cùng một thị trường có thể cho kết quả khác nhau tùy phương pháp. KOSPI, KOSPI200, KOSDAQ, S&P 500 và Nikkei 225 được source nêu như các ví dụ chỉ số; đây là tên thể chế và trạng thái textbook, không phải xác nhận thành phần hiện tại.

Khi đọc một chỉ số, kiểm tra: universe, quy tắc chọn và loại mã, trọng số, điều chỉnh corporate action, tần suất tái cân bằng và liệu chỉ số là price return hay total return. Chỉ số price chỉ phản ánh biến động giá; total-return index tái đầu tư cổ tức. So sánh quỹ với benchmark sai loại sẽ tạo kết luận sai về năng lực.

## 5. Câu hỏi ứng dụng và cách giải

Các câu hỏi cuối khối yêu cầu nhận diện KOSPI/KOSDAQ/S&P 500/Nikkei 225, phân biệt PER–PBR–PSR–EV/EBITDA và hiểu portfolio effect. Cách giải không phải nhớ đáp án: (1) xác định object; (2) viết numerator/denominator hoặc cách index-weight; (3) nêu điều kiện; (4) kiểm tra bẫy như split, cổ tức, đòn bẩy và currency. Các số trong ảnh OCR không đủ chắc để chép lại; nguyên tắc reasoning được giữ, chi tiết số liệu được đánh dấu `SOURCE_AMBIGUITY` trong coverage.

## 6. Worked portfolio and benchmark check

Với hai tài sản có trọng số `w₁`, `w₂`, phương sai danh mục không chỉ là trung bình phương sai riêng:

```text
σ²p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρ₁₂σ₁σ₂
```

Hạng tử tương quan giải thích vì sao hai khoản đầu tư biến động mạnh vẫn có thể làm danh mục ổn định hơn khi chúng không cùng giảm. Nhưng tương quan là biến số theo regime; trong stress, thanh khoản và đòn bẩy có thể làm `ρ` tăng. Vì vậy diversification cần được kiểm tra bằng kịch bản, không chỉ bằng correlation trung bình lịch sử.

Khi so sánh với benchmark, phải đồng nhất ba thứ: cách tính lợi suất (price hay total return), tiền tệ và thời điểm tái cân bằng. Một quỹ nhận cổ tức nhưng benchmark chỉ tính giá sẽ bị đánh giá thấp giả tạo; một danh mục KRW so với benchmark USD sẽ trộn lợi nhuận tài sản với FX. Đây là lý do index construction là một phần của measurement, không chỉ là tên chỉ số.

## 7. Khi chiến lược thất bại

Buy-and-hold thất bại nếu tài sản mất khả năng tạo dòng tiền; DCA thất bại về mục tiêu nếu nhà đầu tư không chịu được drawdown kéo dài; small-firm/formula effect thất bại nếu premium bị phí, thanh khoản hoặc data-mining ăn hết. Mỗi chiến lược cần một kill condition: thay đổi quyền lợi pháp lý, suy giảm chất lượng lợi nhuận, turnover vượt ngân sách hoặc benchmark-adjusted return không còn bù rủi ro. Bài 5 sẽ cho thấy cùng logic này áp dụng vào sản phẩm trái phiếu có payoff phức tạp hơn.

## Chốt và bàn giao

Invariant là “kết quả đầu tư = exposure × cơ chế lợi suất − chi phí và rủi ro”. Benchmark chỉ có ý nghĩa khi cùng định nghĩa lợi suất, tiền tệ và thời hạn. Bài 5 chuyển sang trái phiếu, nơi exposure được trả theo coupon, gốc, quyền chọn và thứ tự ưu tiên thay vì residual claim của cổ phiếu. Xem [Trái phiếu và sản phẩm thu nhập cố định](./05_BONDS_AND_FIXED_INCOME_INSTRUMENTS.md).
