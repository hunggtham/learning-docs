# Quyền chọn, bề mặt biến động, Greeks và phòng vệ

> **Mạch đọc:** [README](./README.md) là owner của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**; giữ file trong tuyến derivatives trước khi đi vào hedging. Từ **1. Giá giao ngay và giá kỳ hạn** nối qua cost of carry, forward, implied volatility, surface, Greeks, vega/gamma và thanh khoản, rồi kết thúc ở hedge P/L; mỗi lớp giải thích một thành phần của giá quyền chọn thay vì chỉ đọc hướng thị trường.

> Quyền chọn không chỉ là công cụ “đoán tăng hay giảm”. Giá quyền chọn phản ánh phân phối xác suất, thời gian, biến động và trạng thái thị trường. Chương này giải thích bằng tiếng Việt cách đọc quyền chọn theo sáu lớp: hướng giá, biến động, thời gian, độ lồi, thanh khoản và ký quỹ. Các thuật ngữ tiếng Anh được giữ trong ngoặc hoặc dưới dạng tên chuẩn như Delta, Gamma, Vega để tiện tra cứu.

# Phần I — Từ giá giao ngay tới giá kỳ hạn

## 1. Giá giao ngay và giá kỳ hạn

Giá quyền chọn không chỉ liên quan **giá giao ngay (spot)** mà còn liên quan **giá kỳ hạn (forward)** của tài sản cơ sở.

Giá kỳ hạn chịu ảnh hưởng bởi:

- lãi suất;
- cổ tức;
- chi phí vay tài sản;
- chi phí lưu kho hoặc lợi ích nắm giữ tùy loại tài sản.

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **2. Lợi ích hoặc chi phí nắm giữ** tiếp nhận điểm tựa từ **1. Giá giao ngay và giá kỳ hạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Độ gần tiền theo giá kỳ hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Lợi ích hoặc chi phí nắm giữ

Trước khi đọc option price, cần tách hướng giá khỏi lợi ích/chi phí của việc giữ exposure theo thời gian. Carry có thể làm payoff thực tế khác với biểu đồ spot đơn giản.

**Carry** là lợi ích hoặc chi phí kinh tế phát sinh khi giữ mức phơi nhiễm qua thời gian.

Với chỉ số cổ phiếu, lãi suất và cổ tức ảnh hưởng giá kỳ hạn. Với hàng hóa, chi phí lưu kho và **lợi ích tiện ích (convenience yield)** cũng quan trọng.

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **3. Độ gần tiền theo giá kỳ hạn** tiếp nhận điểm tựa từ **2. Lợi ích hoặc chi phí nắm giữ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Quyền chọn là khoản chi trả phụ thuộc trạng thái** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Độ gần tiền theo giá kỳ hạn

Khi phân tích chuyên sâu, trạng thái **gần tiền (moneyness)** nên được nhìn so với giá kỳ hạn trong nhiều trường hợp, không chỉ so giá thực hiện với giá giao ngay.

# Phần II — Giá quyền chọn và phân phối xác suất

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **4. Quyền chọn là khoản chi trả phụ thuộc trạng thái** tiếp nhận điểm tựa từ **3. Độ gần tiền theo giá kỳ hạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Biến động hàm ý** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Quyền chọn là khoản chi trả phụ thuộc trạng thái

Quyền chọn tạo khoản chi trả khác nhau tùy giá tài sản tại thời điểm đáo hạn.

```text
Call = max(S - K, 0)
Put  = max(K - S, 0)
```

Tính phi tuyến này tạo **độ lồi (convexity)**.

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **5. Biến động hàm ý** tiếp nhận điểm tựa từ **4. Quyền chọn là khoản chi trả phụ thuộc trạng thái** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Biến động thực hiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Biến động hàm ý

IV là biến được suy ra từ giá option, không phải một dự báo chắc chắn. Hãy đọc nó như giá thị trường của bất định và risk premium, rồi so với realized volatility cùng kỳ vọng sự kiện.

**Biến động hàm ý (implied volatility, IV)** là mức biến động khiến mô hình định giá khớp với giá quyền chọn trên thị trường.

IV không phải dự báo chắc chắn về biến động tương lai; nó là một đầu vào ngược suy ra từ giá.

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **6. Biến động thực hiện** tiếp nhận điểm tựa từ **5. Biến động hàm ý** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Phần bù rủi ro biến động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Biến động thực hiện

Realized volatility đo những gì đã xảy ra trong đường giá. So sánh nó với IV giúp đánh giá premium tương đối, nhưng cần giữ nhất quán horizon, sampling và regime.

**Biến động thực hiện (realized volatility)** là biến động thật xảy ra trong đường giá.

Một chiến lược biến động thường đặt cược vào quan hệ:

```text
Biến động hàm ý
so với
Biến động thực hiện trong tương lai
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **7. Phần bù rủi ro biến động** tiếp nhận điểm tựa từ **6. Biến động thực hiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Delta** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Phần bù rủi ro biến động

Trong nhiều thị trường, người mua bảo hiểm sẵn sàng trả phí cao để bảo vệ rủi ro đuôi. Vì vậy IV trung bình có thể cao hơn biến động thực hiện trung bình.

Khoảng này thường được gọi là **phần bù rủi ro biến động (volatility risk premium)**.

Nó không phải “tiền miễn phí”; người bán nhận phí để chịu rủi ro trong trạng thái xấu.

# Phần III — Greeks bậc một

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **8. Delta** tiếp nhận điểm tựa từ **7. Phần bù rủi ro biến động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Gamma** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Delta

Delta đo mức giá quyền chọn thay đổi khi giá tài sản cơ sở thay đổi một lượng nhỏ.

Delta cũng thường được dùng như xấp xỉ cho mức phơi nhiễm theo hướng giá, nhưng Delta thay đổi theo giá, thời gian và IV.

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **9. Gamma** tiếp nhận điểm tựa từ **8. Delta** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Theta** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Gamma

Gamma đo mức Delta thay đổi khi giá tài sản cơ sở thay đổi.

```text
Mua quyền chọn → thường Gamma dương
Bán quyền chọn → thường Gamma âm
```

Gamma dương hưởng lợi khi giá di chuyển mạnh hơn kỳ vọng nếu phòng vệ Delta phù hợp. Gamma âm chịu rủi ro khi thị trường chạy mạnh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **10. Theta** tiếp nhận điểm tựa từ **9. Gamma** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Vega** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Theta

Theta đo tốc độ mất giá trị theo thời gian nếu các yếu tố khác không đổi.

Người mua quyền chọn thường chịu hao mòn giá trị thời gian. Người bán thường thu Theta nhưng đổi lại chịu Gamma và rủi ro đuôi.

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **11. Vega** tiếp nhận điểm tựa từ **10. Theta** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Rho** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Vega

Vega đo độ nhạy với thay đổi IV.

Vega dương hưởng lợi khi IV tăng; Vega âm ngược lại.

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **12. Rho** tiếp nhận điểm tựa từ **11. Vega** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Vanna** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Rho

Rho đo độ nhạy với lãi suất. Với quyền chọn ngắn hạn tác động thường nhỏ hơn Delta hoặc Vega, nhưng với kỳ hạn dài có thể đáng kể.

# Phần IV — Greeks bậc cao

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **13. Vanna** tiếp nhận điểm tựa từ **12. Rho** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Vomma / Volga** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Vanna

Vanna mô tả tương tác giữa Delta và biến động, giúp hiểu mức phơi nhiễm theo hướng giá thay đổi khi IV thay đổi.

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **14. Vomma / Volga** tiếp nhận điểm tựa từ **13. Vanna** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Charm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Vomma / Volga

Vomma hoặc Volga đo độ cong của giá quyền chọn theo biến động, tức Vega thay đổi ra sao khi IV thay đổi.

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **15. Charm** tiếp nhận điểm tựa từ **14. Vomma / Volga** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Không dùng một Greek riêng lẻ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Charm

Charm mô tả Delta thay đổi theo thời gian khi giá cơ sở giữ nguyên. Gần đáo hạn, hiệu ứng thời gian có thể tăng mạnh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **16. Không dùng một Greek riêng lẻ** tiếp nhận điểm tựa từ **15. Charm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. IV không giống nhau ở mọi giá thực hiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Không dùng một Greek riêng lẻ

Greeks là các độ nhạy cục bộ quanh trạng thái hiện tại. Khi thị trường nhảy giá lớn, cần dùng lưới kịch bản thay vì chỉ lấy Greek nhân với mức biến động.

# Phần V — Nụ cười và độ lệch biến động

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **17. IV không giống nhau ở mọi giá thực hiện** tiếp nhận điểm tựa từ **16. Không dùng một Greek riêng lẻ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Độ lệch ở chỉ số cổ phiếu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. IV không giống nhau ở mọi giá thực hiện

Trong thị trường thật, quyền chọn bán phía dưới và quyền chọn mua phía trên thường có IV khác nhau.

Đường IV theo giá thực hiện tạo **nụ cười biến động (volatility smile)** hoặc **độ lệch biến động (volatility skew)**.

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **18. Độ lệch ở chỉ số cổ phiếu** tiếp nhận điểm tựa từ **17. IV không giống nhau ở mọi giá thực hiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Chênh lệch biến động mua–bán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Độ lệch ở chỉ số cổ phiếu

Chỉ số cổ phiếu thường có IV của quyền chọn bán ngoài tiền cao hơn vùng gần tiền vì nhu cầu bảo hiểm và rủi ro sụp giảm.

Đây thường được gọi là **độ lệch âm (negative skew)**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **19. Chênh lệch biến động mua–bán** tiếp nhận điểm tựa từ **18. Độ lệch ở chỉ số cổ phiếu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Độ cong cánh quyền chọn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Chênh lệch biến động mua–bán

Risk reversal đặt IV của call và put tương ứng cạnh nhau để đọc skew theo hướng bảo hiểm hoặc đầu cơ. Chênh lệch này phản ánh nhu cầu một phía, không phải xác suất trực tiếp của một mức giá.

**Risk reversal** so sánh IV của quyền chọn mua và quyền chọn bán có độ gần tiền tương ứng.

Chỉ số này giúp đọc sự bất đối xứng trong nhu cầu và nhận thức về rủi ro đuôi.

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **20. Độ cong cánh quyền chọn** tiếp nhận điểm tựa từ **19. Chênh lệch biến động mua–bán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Biến động theo thời gian đáo hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Độ cong cánh quyền chọn

Curvature/butterfly cho biết bề mặt IV cong thế nào quanh vùng near-the-money và hai cánh. Nó giúp phát hiện nhu cầu tail insurance hoặc pricing bất thường mà một risk reversal không cho thấy.

**Độ cong (curvature/butterfly)** cho biết các quyền chọn rất xa tiền đắt hay rẻ so với vùng gần tiền, qua đó phản ánh nhu cầu bảo hiểm đuôi và hình dạng phân phối mà thị trường đang định giá.

# Phần VI — Cấu trúc biến động theo kỳ hạn

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **21. Biến động theo thời gian đáo hạn** tiếp nhận điểm tựa từ **20. Độ cong cánh quyền chọn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Biến động sự kiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Biến động theo thời gian đáo hạn

IV khác nhau giữa các kỳ hạn tạo **cấu trúc kỳ hạn biến động (volatility term structure)**.

Một sự kiện gần có thể làm kỳ hạn ngắn tăng mạnh trong khi kỳ hạn dài ít thay đổi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **22. Biến động sự kiện** tiếp nhận điểm tựa từ **21. Biến động theo thời gian đáo hạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Chênh lệch lịch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Biến động sự kiện

Báo cáo lợi nhuận, CPI, FOMC hoặc phán quyết pháp lý có thể tập trung bất định vào một thời điểm cụ thể.

Sau sự kiện, phần IV liên quan bất định đó thường giảm nhanh.

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **23. Chênh lệch lịch** tiếp nhận điểm tựa từ **22. Biến động sự kiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Bề mặt biến động là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Chênh lệch lịch

Calendar spread tách rủi ro kỳ hạn bằng cách mua/bán option có expiry khác nhau. Nó nhạy với term structure, event timing và thay đổi IV chứ không chỉ với hướng giá.

**Chênh lệch lịch (calendar spread)** dùng quyền chọn cùng hoặc gần cùng giá thực hiện nhưng khác kỳ hạn.

Lãi/lỗ phụ thuộc cấu trúc kỳ hạn, đường đi của giá và tương quan Vega/Theta giữa hai chân.

# Phần VII — Bề mặt biến động

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **24. Bề mặt biến động là gì?** tiếp nhận điểm tựa từ **23. Chênh lệch lịch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Hai cách mô tả chuyển động bề mặt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Bề mặt biến động là gì?

Volatility surface là bản đồ IV theo strike/moneyness và expiry. Đọc toàn bề mặt giúp tránh dùng một IV ATM như thể mọi strike và kỳ hạn có cùng risk premium.

**Bề mặt biến động (volatility surface)** mô tả IV theo hai chiều chính:

```text
Giá thực hiện / độ gần tiền
×
Kỳ hạn
```

Bề mặt thay đổi liên tục khi giá, dòng lệnh và nhận thức rủi ro thay đổi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **25. Hai cách mô tả chuyển động bề mặt** tiếp nhận điểm tựa từ **24. Bề mặt biến động là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Biến động của chính biến động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Hai cách mô tả chuyển động bề mặt

Sticky strike và sticky delta là hai xấp xỉ để dự báo surface di chuyển khi spot đổi. Không cách nào đúng trong mọi regime, nên hedge và scenario phải kiểm tra cả hai giả định.

**Bám giá thực hiện (sticky strike)** và **bám Delta (sticky delta)** là hai cách gần đúng để mô tả IV thay đổi khi giá cơ sở di chuyển.

Đây chỉ là mô hình gần đúng; hành vi thật có thể thay đổi theo chế độ.

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **26. Biến động của chính biến động** tiếp nhận điểm tựa từ **25. Hai cách mô tả chuyển động bề mặt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Ý tưởng cơ bản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Biến động của chính biến động

Vol-of-vol đo độ bất ổn của chính IV. Nó quan trọng với option dài hạn, tail hedge và các vị thế short convexity vì IV có thể tăng cùng lúc với giá cơ sở giảm.

**Biến động của biến động (vol-of-vol)** đo mức IV bản thân nó biến động mạnh tới đâu.

Trong khủng hoảng, cả biến động giá và biến động của IV có thể cùng tăng.

# Phần VIII — Giao dịch Gamma có phòng vệ

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **27. Ý tưởng cơ bản** tiếp nhận điểm tựa từ **26. Biến động của chính biến động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Không phải chênh lệch giá miễn phí** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Ý tưởng cơ bản

Người nắm Gamma dương có thể điều chỉnh Delta nhiều lần khi giá di chuyển.

Một mô tả đơn giản:

```text
Gamma dương
→ giá tăng → Delta tăng → bán bớt tài sản cơ sở để phòng vệ
→ giá giảm → Delta giảm → mua lại tài sản cơ sở để phòng vệ
```

Nếu biến động thực hiện đủ lớn so với phí quyền chọn và chi phí giao dịch, quá trình **giao dịch Gamma (gamma scalping)** có thể bù một phần hao mòn thời gian.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **28. Không phải chênh lệch giá miễn phí** tiếp nhận điểm tựa từ **27. Ý tưởng cơ bản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Delta gần 0 không đồng nghĩa không rủi ro** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Không phải chênh lệch giá miễn phí

Kết quả phụ thuộc:

- biến động thực hiện;
- IV đã trả;
- tần suất phòng vệ;
- chênh lệch mua–bán;
- trượt giá;
- rủi ro nhảy giá.

# Phần IX — Phòng vệ Delta

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **29. Delta gần 0 không đồng nghĩa không rủi ro** tiếp nhận điểm tựa từ **28. Không phải chênh lệch giá miễn phí** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Phòng vệ động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Delta gần 0 không đồng nghĩa không rủi ro

Một vị thế Delta gần 0 vẫn có thể chịu:

- Gamma;
- Vega;
- Theta;
- độ lệch bề mặt;
- rủi ro nhảy giá.

Vì vậy “trung hòa Delta” chỉ mô tả một lớp rủi ro tại thời điểm hiện tại.

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **30. Phòng vệ động** tiếp nhận điểm tựa từ **29. Delta gần 0 không đồng nghĩa không rủi ro** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Thực hiện quyền sớm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Phòng vệ động

Khi Delta thay đổi, vị thế phòng vệ phải được điều chỉnh. Phòng vệ quá thường làm chi phí tăng; phòng vệ quá ít làm rủi ro theo hướng giá tăng.

# Phần X — Thực hiện quyền, đáo hạn và rủi ro quanh giá thực hiện

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **31. Thực hiện quyền sớm** tiếp nhận điểm tựa từ **30. Phòng vệ động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Rủi ro pin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Thực hiện quyền sớm

Quyền chọn kiểu Mỹ có thể bị thực hiện trước đáo hạn, đặc biệt quanh ngày cổ tức hoặc khi giá trị thời gian còn rất thấp.

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **32. Rủi ro pin** tiếp nhận điểm tựa từ **31. Thực hiện quyền sớm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Khoảng nhảy qua đêm hoặc cuối tuần** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Rủi ro pin

Nếu giá cơ sở ở sát giá thực hiện khi đáo hạn, trạng thái thực hiện quyền cuối cùng có thể không chắc chắn và tạo vị thế tài sản cơ sở ngoài ý muốn. Đây thường được gọi là **rủi ro pin (pin risk)**.

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **33. Khoảng nhảy qua đêm hoặc cuối tuần** tiếp nhận điểm tựa từ **32. Rủi ro pin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Vì sao cần quy đổi?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Khoảng nhảy qua đêm hoặc cuối tuần

Vị thế quyền chọn vẫn chịu rủi ro nhảy giá khi thị trường đóng cửa và không thể tái cân bằng Delta.

# Phần XI — Quy đổi Greeks thành giá trị tiền

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **34. Vì sao cần quy đổi?** tiếp nhận điểm tựa từ **33. Khoảng nhảy qua đêm hoặc cuối tuần** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Hệ số hợp đồng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Vì sao cần quy đổi?

Greek trên mỗi quyền chọn khó tổng hợp nếu danh mục có nhiều hệ số hợp đồng và số lượng khác nhau.

Có thể chuyển thành:

- Delta theo giá trị tiền;
- Gamma theo giá trị tiền;
- Vega theo giá trị tiền;
- DV01 với sản phẩm lãi suất.

Cách này giúp tổng hợp rủi ro danh mục.

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **35. Hệ số hợp đồng** tiếp nhận điểm tựa từ **34. Vì sao cần quy đổi?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Tổng hợp theo trạng thái tương lai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Hệ số hợp đồng

Luôn nhân Greek với đúng hệ số hợp đồng và số lượng. Sai hệ số có thể làm ước lượng rủi ro sai hàng chục hoặc hàng trăm lần.

# Phần XII — Danh mục quyền chọn

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **36. Tổng hợp theo trạng thái tương lai** gom các mảnh từ **35. Hệ số hợp đồng** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **37. Lưới kịch bản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Tổng hợp theo trạng thái tương lai

Không nên chỉ cộng Delta hiện tại. Hãy kiểm thử nhiều trạng thái:

```text
Giá cơ sở: -10%, -5%, 0, +5%, +10%
×
IV: giảm mạnh, không đổi, tăng mạnh
×
Thời gian: hôm nay / sau một tuần / gần đáo hạn
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **37. Lưới kịch bản** gom các mảnh từ **36. Tổng hợp theo trạng thái tương lai** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **38. Rủi ro tương quan** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Lưới kịch bản

Scenario grid đặt giá, IV, thời gian và các biến liên quan vào cùng một bảng để lộ payoff phi tuyến. Nó giúp kiểm tra các tổ hợp mà một Greek tại một điểm không thể mô tả.

**Lưới kịch bản (scenario grid)** cho thấy tính phi tuyến rõ hơn một Greek duy nhất.

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **38. Rủi ro tương quan** tiếp nhận điểm tựa từ **37. Lưới kịch bản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Mục tiêu của phòng vệ đuôi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Rủi ro tương quan

Danh mục quyền chọn nhiều tài sản còn chịu rủi ro tương quan giữa các tài sản cơ sở. Sản phẩm “tệ nhất trong rổ” đặc biệt nhạy với tương quan.

# Phần XIII — Phòng vệ rủi ro đuôi

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **39. Mục tiêu của phòng vệ đuôi** tiếp nhận điểm tựa từ **38. Rủi ro tương quan** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Chi phí bảo hiểm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Mục tiêu của phòng vệ đuôi

Tail hedge được thiết kế để giảm phân phối lỗ cực đoan và nguy cơ bán cưỡng bức. Chi phí carry thường xuyên cần được đánh giá cùng lợi ích bảo vệ trong nhiều năm và nhiều regime.

**Phòng vệ đuôi (tail hedge)** nhằm giảm tổn thất trong trạng thái cực đoan, không nhất thiết tạo lợi nhuận mỗi tháng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **40. Chi phí bảo hiểm** tiếp nhận điểm tựa từ **39. Mục tiêu của phòng vệ đuôi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Ngân sách phòng vệ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Chi phí bảo hiểm

Mua quyền chọn bán lặp lại tạo chi phí nắm giữ âm. Đánh giá phòng vệ cần theo nhiều năm và ở cấp toàn danh mục.

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **41. Ngân sách phòng vệ** tiếp nhận điểm tựa từ **40. Chi phí bảo hiểm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. Chênh lệch quyền chọn bán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Ngân sách phòng vệ

Có thể định trước tỷ lệ phí quyền chọn hằng năm dành cho bảo vệ. Điều này tránh mua bảo hiểm quá nhiều sau khi IV đã tăng mạnh.

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **42. Chênh lệch quyền chọn bán** tiếp nhận điểm tựa từ **41. Ngân sách phòng vệ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Collar** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. Chênh lệch quyền chọn bán

Put spread đổi một phần vùng bảo vệ sâu lấy premium thấp hơn. Người dùng phải ghi rõ strike bảo vệ, strike bán và mức lỗ còn lại dưới vùng đó.

**Put spread** giảm phí bằng cách bán một quyền chọn bán có giá thực hiện thấp hơn, nhưng mức bảo vệ bị giới hạn khi thị trường giảm cực sâu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **43. Collar** tiếp nhận điểm tựa từ **42. Chênh lệch quyền chọn bán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. Biến động giá hàm ý quanh sự kiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Collar

Collar kết hợp long put với short call để tài trợ hedge, vì vậy nó giới hạn cả downside và upside. Thiết kế cần khớp với mục tiêu, thời hạn và mức giá chấp nhận bỏ qua.

**Collar** bán quyền chọn mua để tài trợ một phần quyền chọn bán, đổi lại giới hạn mức tăng giá phía trên.

# Phần XIV — Quyền chọn quanh sự kiện

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **44. Biến động giá hàm ý quanh sự kiện** tiếp nhận điểm tựa từ **43. Collar** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. Sụt IV sau sự kiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Biến động giá hàm ý quanh sự kiện

Thị trường quyền chọn có thể được dùng để ước lượng mức biến động giá mà thị trường đang định giá quanh một sự kiện.

Nếu biến động thực tế nhỏ hơn mức đã được định giá, người mua quyền chọn vẫn có thể lỗ dù đoán đúng hướng.

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **45. Sụt IV sau sự kiện** tiếp nhận điểm tựa từ **44. Biến động giá hàm ý quanh sự kiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **46. Quyền chọn quanh báo cáo lợi nhuận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. Sụt IV sau sự kiện

Sau khi bất định biến mất, IV có thể giảm mạnh. Hiện tượng này thường được gọi là **IV crush**.

Lãi/lỗ của quyền chọn mua có thể được nhìn như:

```text
Lợi ích từ hướng giá
+/- ảnh hưởng Vega
- hao mòn Theta
- chi phí thực thi
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **46. Quyền chọn quanh báo cáo lợi nhuận** tiếp nhận điểm tựa từ **45. Sụt IV sau sự kiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **47. Độ lệch không chỉ là cược hướng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. Quyền chọn quanh báo cáo lợi nhuận

Báo cáo lợi nhuận tạo rủi ro nhảy giá và bất cân xứng thông tin. Kiểm thử chỉ dùng giá đóng cửa ngày trước–sau dễ đánh giá sai giá khớp và động học IV.

# Phần XV — Giao dịch độ lệch biến động

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **47. Độ lệch không chỉ là cược hướng** tiếp nhận điểm tựa từ **46. Quyền chọn quanh báo cáo lợi nhuận** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **48. Độ lệch có thể dốc hơn khi căng thẳng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. Độ lệch không chỉ là cược hướng

Mua quyền chọn bán đắt và bán quyền chọn mua rẻ có thể là cược vào bất đối xứng phân phối chứ không chỉ quan điểm giảm giá.

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **48. Độ lệch có thể dốc hơn khi căng thẳng** tiếp nhận điểm tựa từ **47. Độ lệch không chỉ là cược hướng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **49. Thu Theta và chịu tổn thất đuôi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 48. Độ lệch có thể dốc hơn khi căng thẳng

Khi nhu cầu bảo hiểm giảm giá tăng, IV của quyền chọn bán ngoài tiền có thể tăng nhanh hơn IV gần tiền. Khi đó lãi/lỗ của quyền chọn bán hưởng cả Delta và thay đổi độ lệch.

# Phần XVI — Rủi ro bán biến động

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **49. Thu Theta và chịu tổn thất đuôi** tiếp nhận điểm tựa từ **48. Độ lệch có thể dốc hơn khi căng thẳng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **50. Ký quỹ tăng trong khủng hoảng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 49. Thu Theta và chịu tổn thất đuôi

Vị thế bán quyền chọn thường có cấu trúc:

```text
Nhiều khoản lãi nhỏ
+ thỉnh thoảng một khoản lỗ rất lớn
```

Cần kiểm thử các biến động lớn hơn dữ liệu hằng ngày thông thường.

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **50. Ký quỹ tăng trong khủng hoảng** tiếp nhận điểm tựa từ **49. Thu Theta và chịu tổn thất đuôi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **51. Dữ liệu quyền chọn phức tạp hơn dữ liệu giao ngay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 50. Ký quỹ tăng trong khủng hoảng

Khi biến động tăng, nhà môi giới hoặc tổ chức bù trừ có thể tăng yêu cầu ký quỹ đúng lúc vị thế bán quyền chọn đang lỗ.

Rủi ro lãi/lỗ và rủi ro thanh khoản vì vậy xuất hiện đồng thời.

# Phần XVII — Dữ liệu và kiểm thử quyền chọn

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **50. Ký quỹ tăng trong khủng hoảng** nêu điều cần giải thích; **51. Dữ liệu quyền chọn phức tạp hơn dữ liệu giao ngay** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **52. Thiên lệch dùng giá giữa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 51. Dữ liệu quyền chọn phức tạp hơn dữ liệu giao ngay

Cần xử lý:

- giá thực hiện;
- kỳ hạn;
- giá mua/bán;
- báo giá cũ;
- hành động doanh nghiệp;
- thực hiện quyền sớm;
- hệ số hợp đồng;
- nội suy bề mặt biến động.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **51. Dữ liệu quyền chọn phức tạp hơn dữ liệu giao ngay** nêu điều cần giải thích; **52. Thiên lệch dùng giá giữa** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **53. Chuỗi hợp đồng thay đổi liên tục** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 52. Thiên lệch dùng giá giữa

Kiểm thử dùng điểm giữa bid–ask cho mọi lệnh thường quá lạc quan, đặc biệt với quyền chọn ngoài tiền hoặc ít thanh khoản.

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **52. Thiên lệch dùng giá giữa** xác định đầu vào; **53. Chuỗi hợp đồng thay đổi liên tục** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **54. Ước lượng IV** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 53. Chuỗi hợp đồng thay đổi liên tục

Chuỗi quyền chọn thay đổi theo ngày. Kiểm thử phải dùng đúng những hợp đồng thực sự tồn tại ở thời điểm lịch sử đó.

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **53. Chuỗi hợp đồng thay đổi liên tục** xác định đầu vào; **54. Ước lượng IV** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **55. Phòng vệ đúng nhân tố** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 54. Ước lượng IV

Báo giá lỗi có thể tạo IV vô lý. Cần lọc dữ liệu và kiểm tra tính nhất quán với điều kiện không chênh lệch giá.

# Phần XVIII — Phòng vệ thực tế

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **55. Phòng vệ đúng nhân tố** tiếp nhận điểm tựa từ **54. Ước lượng IV** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **56. Rủi ro cơ sở** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 55. Phòng vệ đúng nhân tố

Hedge đúng nhân tố nghĩa là công cụ giảm đúng beta, duration, FX, credit, volatility hoặc liquidity risk đang gây tổn thất. Sơ đồ này giúp tránh hedge một exposure dễ đo nhưng bỏ qua nguồn rủi ro chính.

```text
Beta cổ phiếu
→ futures chỉ số / quyền chọn bán

Rủi ro lãi suất
→ futures lãi suất / hoán đổi

Rủi ro FX
→ hợp đồng kỳ hạn / quyền chọn

Rủi ro biến động
→ quyền chọn / công cụ biến động
```

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **56. Rủi ro cơ sở** tiếp nhận điểm tựa từ **55. Phòng vệ đúng nhân tố** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **57. Phòng vệ quá mức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 56. Rủi ro cơ sở

Basis risk xuất hiện khi công cụ hedge và tài sản cần bảo vệ không di chuyển giống nhau. Nó phải được stress theo regime, maturity, liquidity và event thay vì giả định correlation cố định.

**Rủi ro cơ sở (basis risk)** xuất hiện khi công cụ phòng vệ không trùng hoàn toàn với tài sản cần bảo vệ.

Ví dụ phòng vệ cổ phiếu bán dẫn Hàn Quốc bằng Nasdaq futures chỉ giảm một phần beta công nghệ toàn cầu, không loại rủi ro riêng của công ty hoặc Hàn Quốc.

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **57. Phòng vệ quá mức** tiếp nhận điểm tựa từ **56. Rủi ro cơ sở** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **58. Tái cân bằng phòng vệ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 57. Phòng vệ quá mức

Phòng vệ quá lớn có thể biến danh mục thành vị thế ngược chiều thay vì chỉ giảm rủi ro.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **58. Tái cân bằng phòng vệ** tiếp nhận điểm tựa từ **57. Phòng vệ quá mức** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **59. Lãi/lỗ quyền chọn nên được phân rã** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 58. Tái cân bằng phòng vệ

Delta hoặc beta thay đổi theo thị trường, vì vậy tỷ lệ phòng vệ phải được đánh giá lại định kỳ hoặc khi trạng thái thay đổi đủ lớn.

# Phần XIX — Phân rã lãi/lỗ

> **Chuyển mạch:** Trong **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **59. Lãi/lỗ quyền chọn nên được phân rã** tiếp nhận điểm tựa từ **58. Tái cân bằng phòng vệ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **60. Đúng hướng nhưng sai công cụ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 59. Lãi/lỗ quyền chọn nên được phân rã

Một khung thực tế:

```text
Ảnh hưởng Delta
Ảnh hưởng Gamma
Theta
Vega / thay đổi IV
Độ lệch / bề mặt
Lãi suất / carry
Chi phí thực thi
Phần còn lại
```

> **Chuyển mạch:** Ở chặng này của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **60. Đúng hướng nhưng sai công cụ** tiếp nhận điểm tựa từ **59. Lãi/lỗ quyền chọn nên được phân rã** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kết luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 60. Đúng hướng nhưng sai công cụ

Nhà đầu tư có thể đoán đúng hướng giá nhưng vẫn lỗ vì trả IV quá cao, chịu hao mòn thời gian hoặc độ lệch biến động di chuyển bất lợi.

Đây là lý do “đúng thị trường” không đồng nghĩa “đúng giao dịch quyền chọn”.

# Phần XX — Quy trình quản trị vị thế quyền chọn

Trước khi mở vị thế, cần trả lời:

```text
Mình đang cược vào hướng giá, biến động hay cả hai?
IV hiện tại cao hay thấp so với lịch sử và sự kiện?
Rủi ro Gamma/Vega/Theta lớn nhất ở đâu?
Có thể bị thực hiện quyền sớm không?
Yêu cầu ký quỹ có thể tăng tới đâu?
Thanh khoản của hợp đồng thế nào?
Nếu giá nhảy mạnh, lưới kịch bản cho thấy gì?
Điều kiện vô hiệu hóa là gì?
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền chọn, bề mặt biến động, Greeks và phòng vệ**, **Kết luận** gom các mảnh từ **60. Đúng hướng nhưng sai công cụ** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết luận

Quyền chọn là công cụ nhiều chiều. Một vị thế phải được hiểu đồng thời qua:

```text
Hướng giá
→ biến động
→ thời gian
→ độ lồi
→ bề mặt biến động
→ thanh khoản
→ ký quỹ
→ chi phí phòng vệ
```

Khi các lớp này được tách rõ, những thuật ngữ như Delta, Gamma, Vega hay skew trở thành nhãn kỹ thuật cho cơ chế đã hiểu, thay vì là từ tiếng Anh phải ghi nhớ riêng lẻ.

> **Bàn giao:** Sau **Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
