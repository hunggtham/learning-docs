# Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD

> **Mạch đọc:** [README](./README.md) là owner của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**; quay lại đó để định vị file trong track trading derivatives. Từ **1. Quyền sở hữu khác mức phơi nhiễm theo hợp đồng** chuyển sang thông số, margin/collateral, payoff, định giá, basis và đối tác, rồi nối sang settlement, hedging và rủi ro đòn bẩy; cấu trúc hợp đồng quyết định mọi kết luận về giá và tổn thất phía sau.

> Phái sinh (derivative) là hợp đồng có giá trị phụ thuộc vào tài sản, chỉ số hoặc biến tham chiếu. Khác với mua cổ phiếu thông thường, phái sinh có thể tạo nghĩa vụ hợp đồng, đòn bẩy, yêu cầu ký quỹ, tài sản bảo đảm và khoản chi trả phi tuyến. Vì vậy phải hiểu cấu trúc hợp đồng trước khi dự đoán hướng giá. Phần giải thích dùng tiếng Việt; thuật ngữ tiếng Anh chỉ giữ trong ngoặc hoặc dưới dạng tên chuẩn.

# Phần I — Phái sinh là gì?

## 1. Quyền sở hữu khác mức phơi nhiễm theo hợp đồng

Mua cổ phiếu thường tạo quyền sở hữu phần còn lại trong doanh nghiệp. Mua hợp đồng tương lai, quyền chọn hoặc CFD thường chỉ tạo **mức phơi nhiễm theo hợp đồng**, không nhất thiết tạo quyền sở hữu tài sản cơ sở.

Cần phân biệt:

```text
Tài sản cơ sở (underlying)
Hợp đồng
Đối tác pháp lý
Cơ chế thanh toán
Tài sản bảo đảm
```

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **2. Thông số hợp đồng** nối từ **1. Quyền sở hữu khác mức phơi nhiễm theo hợp đồng** sang **3. Giá trị danh nghĩa**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Thông số hợp đồng

Trước khi giao dịch một sản phẩm phái sinh cần biết:

- tài sản cơ sở;
- hệ số hợp đồng;
- bước giá tối thiểu;
- giá trị mỗi bước giá;
- ngày đáo hạn;
- cơ chế thanh toán;
- giờ giao dịch;
- yêu cầu ký quỹ;
- đồng tiền thanh toán;
- kiểu thực hiện quyền nếu là quyền chọn.

Tên sản phẩm giống nhau không bảo đảm thông số giống nhau.

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **3. Giá trị danh nghĩa** nối từ **2. Thông số hợp đồng** sang **4. Hợp đồng kỳ hạn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Giá trị danh nghĩa

Trước khi tính margin hay P/L, cần biết vị thế đang kiểm soát bao nhiêu giá trị kinh tế. Notional là quy mô phơi nhiễm, không phải số tiền đã trả hoặc mức lỗ tối đa.

**Giá trị danh nghĩa (notional)** là quy mô kinh tế của mức phơi nhiễm.

Với hợp đồng tương lai:

```text
Notional
= Giá hợp đồng tương lai × Hệ số hợp đồng
```

Tiền ký quỹ chỉ là tài sản bảo đảm, không phải giá trị danh nghĩa và cũng không phải mức lỗ tối đa.

# Phần II — Hợp đồng kỳ hạn và hợp đồng tương lai

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **4. Hợp đồng kỳ hạn** nối từ **3. Giá trị danh nghĩa** sang **5. Hợp đồng tương lai**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Hợp đồng kỳ hạn

Forward bắt đầu từ thỏa thuận song phương và rủi ro đối tác. Hãy đọc giá, ngày giao hàng, tài sản cơ sở và collateral trước khi so nó với futures niêm yết.

**Hợp đồng kỳ hạn (forward)** là thỏa thuận hai bên mua hoặc bán tài sản trong tương lai theo mức giá đã định trước.

Forward thường giao dịch ngoài sở (OTC), vì vậy rủi ro đối tác, tài sản bảo đảm và điều khoản đóng vị thế rất quan trọng.

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **5. Hợp đồng tương lai** nối từ **4. Hợp đồng kỳ hạn** sang **6. Ký quỹ ban đầu và ký quỹ duy trì**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Hợp đồng tương lai

Futures chuẩn hóa các điều khoản và thêm clearing, margin, expiry và settlement. Điều này giảm một số rủi ro đối tác trực tiếp nhưng tạo yêu cầu ký quỹ và roll cần quản lý.

**Hợp đồng tương lai (futures)** được chuẩn hóa và thường giao dịch trên sở với cơ chế bù trừ tập trung.

Chuẩn hóa giúp thanh khoản tốt hơn nhưng nhà giao dịch phải tuân thủ hệ số hợp đồng, ngày đáo hạn, ký quỹ và quy tắc thanh toán của từng sản phẩm.

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **6. Ký quỹ ban đầu và ký quỹ duy trì** nối từ **5. Hợp đồng tương lai** sang **7. Ký quỹ biến đổi và đánh dấu theo thị trường**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Ký quỹ ban đầu và ký quỹ duy trì

Margin là cơ chế giữ cho hợp đồng có đủ collateral khi giá thay đổi. Phân biệt initial và maintenance margin giúp người mới hiểu vì sao một vị thế có thể bị gọi bổ sung vốn trước khi thesis dài hạn sai.

**Ký quỹ ban đầu (initial margin)** là tài sản bảo đảm cần khi mở vị thế.

**Ký quỹ duy trì (maintenance margin)** là mức tối thiểu phải giữ sau đó.

Nếu giá trị tài khoản giảm dưới ngưỡng, nhà môi giới hoặc thành viên bù trừ có thể yêu cầu bổ sung tiền hoặc đóng vị thế.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **7. Ký quỹ biến đổi và đánh dấu theo thị trường** nối từ **6. Ký quỹ ban đầu và ký quỹ duy trì** sang **8. Cơ sở giá**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Ký quỹ biến đổi và đánh dấu theo thị trường

Hợp đồng tương lai thường được đánh dấu lại theo giá thị trường định kỳ.

```text
Giá thay đổi
→ lãi/lỗ được ghi nhận
→ tiền mặt dịch chuyển qua hệ thống ký quỹ
```

Vì vậy quản lý thanh khoản rất quan trọng ngay cả khi luận điểm dài hạn vẫn đúng.

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **8. Cơ sở giá** nối từ **7. Ký quỹ biến đổi và đánh dấu theo thị trường** sang **9. Hội tụ khi đáo hạn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Cơ sở giá

Basis nối giá futures với giá spot và chi phí/benefit nắm giữ tài sản. Basis thay đổi theo funding, storage, dividend, convenience yield và cung cầu hợp đồng, nên không phải một hằng số.

**Cơ sở giá (basis)** là chênh lệch giữa giá hợp đồng tương lai và giá giao ngay theo quy ước của từng thị trường.

Nó chịu ảnh hưởng của:

- lãi suất;
- chi phí lưu kho;
- cổ tức;
- lợi ích tiện ích khi nắm hàng hóa;
- chi phí vay tài sản;
- cung cầu kỹ thuật.

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **9. Hội tụ khi đáo hạn** nối từ **8. Cơ sở giá** sang **10. Contango và backwardation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Hội tụ khi đáo hạn

Gần đáo hạn, giá hợp đồng tương lai và giá giao ngay thường hội tụ nhờ cơ chế thanh toán và chênh lệch giá, tùy sản phẩm.

Nếu không hiểu cơ chế thanh toán, nhà giao dịch có thể vô tình giữ hợp đồng tới giai đoạn không mong muốn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **10. Contango và backwardation** nối từ **9. Hội tụ khi đáo hạn** sang **11. Chuyển kỳ hạn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Contango và backwardation

Đường cong futures ảnh hưởng lợi suất roll bên cạnh biến động spot. Vì vậy, contango/backwardation cần được đọc như một phần của tổng lợi suất và chi phí chuyển kỳ.

**Contango** thường mô tả cấu trúc trong đó giá kỳ hạn xa cao hơn giá gần hoặc giá giao ngay. **Backwardation** mô tả trường hợp ngược lại.

Không nên kết luận tăng hay giảm chỉ từ hai nhãn này. Cần xem chi phí nắm giữ, tồn kho, mức khan hiếm và nhu cầu phòng vệ.

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **11. Chuyển kỳ hạn** nối từ **10. Contango và backwardation** sang **12. Hợp đồng tương lai hàng hóa**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Chuyển kỳ hạn

Muốn duy trì vị thế sau khi hợp đồng cũ gần đáo hạn, nhà đầu tư phải **chuyển kỳ hạn (roll)** sang hợp đồng mới.

Quá trình này tạo:

- phí giao dịch;
- rủi ro cơ sở;
- lợi suất cuộn kỳ hạn;
- rủi ro thanh khoản.

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **12. Hợp đồng tương lai hàng hóa** nối từ **11. Chuyển kỳ hạn** sang **13. Trái phiếu rẻ nhất để giao trong futures trái phiếu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Hợp đồng tương lai hàng hóa

Ngoài biến động giá, hàng hóa còn chịu:

- chi phí lưu kho;
- mức tồn kho;
- mùa vụ;
- quy tắc giao hàng vật chất;
- lợi ích tiện ích khi nắm hàng hóa.

Người chỉ muốn giao dịch tài chính phải đặc biệt hiểu ngày thông báo giao hàng và điều khoản vật chất.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **13. Trái phiếu rẻ nhất để giao trong futures trái phiếu** nối từ **12. Hợp đồng tương lai hàng hóa** sang **14. Quyền chọn mua và quyền chọn bán**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Trái phiếu rẻ nhất để giao trong futures trái phiếu

Một số hợp đồng tương lai trái phiếu cho phép bên bán giao nhiều loại trái phiếu đủ điều kiện. Trái phiếu kinh tế nhất để giao được gọi là **cheapest-to-deliver (CTD)**.

Vì vậy phòng vệ bằng futures trái phiếu còn phụ thuộc hệ số chuyển đổi và sự thay đổi của CTD, không chỉ giá futures.

# Phần III — Quyền chọn

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **14. Quyền chọn mua và quyền chọn bán** nối từ **13. Trái phiếu rẻ nhất để giao trong futures trái phiếu** sang **15. Phí quyền chọn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Quyền chọn mua và quyền chọn bán

Khoản chi trả tại đáo hạn:

```text
Call = max(S - K, 0)
Put  = max(K - S, 0)
```

Người mua trả phí để có quyền; người bán nhận phí nhưng gánh nghĩa vụ tương ứng.

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **15. Phí quyền chọn** nối từ **14. Quyền chọn mua và quyền chọn bán** sang **16. Giá trị nội tại và giá trị thời gian**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Phí quyền chọn

Premium là giá phải trả cho payoff không đối xứng. Người mua cần tách intrinsic value khỏi time value và hiểu IV, thời gian, lãi suất cùng dividend có thể làm premium thay đổi.

**Phí quyền chọn (premium)** không chỉ gồm giá trị nội tại. Trước đáo hạn, giá còn phụ thuộc:

- thời gian;
- biến động hàm ý;
- lãi suất;
- cổ tức;
- chi phí vay;
- hình dạng bề mặt biến động.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **16. Giá trị nội tại và giá trị thời gian** nối từ **15. Phí quyền chọn** sang **17. Độ gần tiền**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Giá trị nội tại và giá trị thời gian

Phần này tách hai lớp tạo nên premium trước đáo hạn. Intrinsic value nói về trạng thái hiện tại so với strike; time value phản ánh cơ hội và bất định còn lại cho tới expiry.

```text
Giá quyền chọn
= Giá trị nội tại
+ Giá trị thời gian
```

Giá trị thời gian thường giảm khi đáo hạn tới gần nhưng tốc độ giảm không tuyến tính.

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **17. Độ gần tiền** nối từ **16. Giá trị nội tại và giá trị thời gian** sang **18. Delta**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Độ gần tiền

Moneyness đặt option vào quan hệ giữa spot và strike, từ đó quyết định payoff, delta gần đúng và phần premium là intrinsic hay time value.

**Độ gần tiền (moneyness)** thường được mô tả bằng:

- ITM: đang có giá trị nội tại;
- ATM: gần giá thực hiện;
- OTM: ngoài tiền.

Độ gần tiền ảnh hưởng Delta, Gamma, thanh khoản và hình dạng phân phối khoản chi trả.

# Phần IV — Greeks

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **18. Delta** nối từ **17. Độ gần tiền** sang **19. Gamma**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Delta

Delta đo độ nhạy của giá quyền chọn với thay đổi nhỏ của tài sản cơ sở. Delta không cố định; nó thay đổi theo giá, thời gian và biến động.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **19. Gamma** nối từ **18. Delta** sang **20. Theta**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Gamma

Gamma đo tốc độ Delta thay đổi khi giá cơ sở thay đổi.

Mua quyền chọn thường Gamma dương; bán quyền chọn thường Gamma âm. Gamma âm có thể làm tổn thất tăng nhanh khi thị trường di chuyển mạnh.

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **20. Theta** nối từ **19. Gamma** sang **21. Vega**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Theta

Theta mô tả hao mòn giá trị theo thời gian. Người mua quyền chọn thường trả chi phí thời gian; người bán thường thu Theta nhưng đổi lại chịu rủi ro Gamma và rủi ro đuôi.

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **21. Vega** nối từ **20. Theta** sang **22. Rho**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Vega

Vega đo độ nhạy với biến động hàm ý. Đúng hướng giá vẫn có thể lỗ nếu IV giảm đủ mạnh.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **22. Rho** nối từ **21. Vega** sang **23. IV không phải dự báo chắc chắn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Rho

Rho đo độ nhạy với lãi suất. Với quyền chọn ngắn hạn tác động thường nhỏ hơn Delta hoặc Vega, nhưng với kỳ hạn dài có thể đáng kể.

# Phần V — Biến động hàm ý

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **23. IV không phải dự báo chắc chắn** nối từ **22. Rho** sang **24. Biến động thực hiện và biến động hàm ý**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. IV không phải dự báo chắc chắn

IV là mức biến động được suy ra từ giá option hiện tại, không phải lời tiên tri về realized volatility. Hãy đọc nó cùng risk premium, skew, term structure và thanh khoản.

**Biến động hàm ý (implied volatility, IV)** là mức biến động làm mô hình phù hợp với giá quyền chọn đang giao dịch.

Nó phản ánh đồng thời:

- kỳ vọng biến động;
- phần bù rủi ro;
- cung cầu quyền chọn;
- nhu cầu phòng vệ.

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **24. Biến động thực hiện và biến động hàm ý** nối từ **23. IV không phải dự báo chắc chắn** sang **25. IV giảm mạnh sau sự kiện**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Biến động thực hiện và biến động hàm ý

So sánh realized với implied giúp kiểm tra option đang đắt/rẻ tương đối theo một giả định, nhưng cần cẩn thận với horizon, sampling và thay đổi regime.

**Biến động thực hiện (realized volatility)** là biến động thật đã xảy ra. **Biến động hàm ý** là mức được suy ra từ giá quyền chọn.

Nhiều chiến lược quyền chọn thực chất đặt cược vào khoảng cách giữa hai mức này.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **25. IV giảm mạnh sau sự kiện** nối từ **24. Biến động thực hiện và biến động hàm ý** sang **26. Quyền chọn bán bảo vệ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. IV giảm mạnh sau sự kiện

Trước sự kiện, IV có thể cao vì bất định. Sau khi thông tin được công bố, IV có thể giảm nhanh, hiện tượng thường gọi là **IV crush**.

Do đó mua quyền chọn trước sự kiện cần đúng không chỉ hướng mà còn độ lớn biến động và mức IV đã trả.

# Phần VI — Các cấu trúc quyền chọn cơ bản

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **26. Quyền chọn bán bảo vệ** nối từ **25. IV giảm mạnh sau sự kiện** sang **27. Covered lời gọi (call / 호출)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Quyền chọn bán bảo vệ

Protective put đổi một phần premium lấy giới hạn rủi ro giảm. Câu hỏi đúng là chi phí bảo hiểm có phù hợp với mục tiêu, thời hạn và khả năng chịu drawdown của danh mục không.

**Protective put** là nắm tài sản cơ sở và mua quyền chọn bán để giới hạn phần giảm dưới một vùng nhất định. Chi phí là phí quyền chọn lặp lại.

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **27. Covered lời gọi (call / 호출)** nối từ **26. Quyền chọn bán bảo vệ** sang **28. Chênh lệch dọc**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Covered lời gọi (call / 호출)

Covered call tạo thu nhập premium bằng cách bán một phần upside và convexity. Nó phù hợp với một số mục tiêu income nhưng không phải hedge giảm hoàn chỉnh.

**Covered call** là nắm tài sản cơ sở và bán quyền chọn mua. Nhà đầu tư thu phí nhưng đổi lại giới hạn một phần mức tăng và đang bán độ lồi.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **28. Chênh lệch dọc** nối từ **27. Covered lời gọi (call / 호출)** sang **29. Collar**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Chênh lệch dọc

Vertical spread dùng hai strike để đổi giới hạn chi phí lấy giới hạn payoff. Phần này cần được đọc như một bài toán trade-off giữa premium, xác suất và mức chi trả tối đa.

**Vertical spread** dùng hai quyền chọn cùng kỳ hạn nhưng khác giá thực hiện để giới hạn cả chi phí lẫn khoản chi trả.

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **29. Collar** nối từ **28. Chênh lệch dọc** sang **30. Straddle và strangle**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Collar

Collar kết hợp bảo vệ downside với việc bán upside để giảm chi phí. Thiết kế tốt phải nói rõ vùng bảo vệ, vùng bị giới hạn và điều kiện thoát.

**Collar** kết hợp tài sản cơ sở, quyền chọn bán và quyền chọn mua bán ra để giảm chi phí bảo vệ nhưng giới hạn phần tăng.

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **30. Straddle và strangle** nối từ **29. Collar** sang **31. Bán quyền chọn không phải thu nhập đều đặn miễn phí**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. Straddle và strangle

Hai cấu trúc này tập trung nhiều hơn vào độ lớn biến động thay vì chỉ hướng giá. Lãi/lỗ phụ thuộc biến động thực tế so với mức đã được định giá và hao mòn thời gian.

# Phần VII — Rủi ro bán quyền chọn

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **31. Bán quyền chọn không phải thu nhập đều đặn miễn phí** nối từ **30. Straddle và strangle** sang **32. Bán quyền chọn mua không có tài sản bảo đảm**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. Bán quyền chọn không phải thu nhập đều đặn miễn phí

Chiến lược bán biến động có thể thắng nhiều lần nhỏ rồi thua rất lớn trong sự kiện đuôi.

```text
Tỷ lệ thắng cao
≠ rủi ro thấp
```

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **32. Bán quyền chọn mua không có tài sản bảo đảm** nối từ **31. Bán quyền chọn không phải thu nhập đều đặn miễn phí** sang **33. Bán quyền chọn bán**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. Bán quyền chọn mua không có tài sản bảo đảm

Naked call tạo exposure short convexity với rủi ro tăng rất lớn. Trước khi nhìn premium nhận được, hãy stress giá cơ sở, margin và gap.

**Naked call** có mức lỗ lý thuyết rất lớn khi tài sản cơ sở tăng mạnh.

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **33. Bán quyền chọn bán** nối từ **32. Bán quyền chọn mua không có tài sản bảo đảm** sang **34. Kiểu Mỹ và kiểu châu Âu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. Bán quyền chọn bán

Short put gần với cam kết mua tài sản ở strike nếu giá giảm. Premium không xóa rủi ro tail; cần tính collateral, assignment và khả năng thanh toán khi thị trường gap.

**Short put** gần với cam kết mua tài sản ở giá thực hiện khi thị trường giảm. Cần tính yêu cầu ký quỹ và rủi ro nhảy giá.

# Phần VIII — Thực hiện quyền và phân bổ nghĩa vụ

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **34. Kiểu Mỹ và kiểu châu Âu** nối từ **33. Bán quyền chọn bán** sang **35. Phân bổ nghĩa vụ thực hiện**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Kiểu Mỹ và kiểu châu Âu

Quyền chọn kiểu Mỹ có thể được thực hiện trước đáo hạn. Quyền chọn kiểu châu Âu chỉ được thực hiện tại đáo hạn theo điều khoản.

Tên gọi này mô tả kiểu thực hiện quyền, không phải vị trí địa lý của thị trường.

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **35. Phân bổ nghĩa vụ thực hiện** nối từ **34. Kiểu Mỹ và kiểu châu Âu** sang **36. Rủi ro pin**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. Phân bổ nghĩa vụ thực hiện

Người bán quyền chọn có thể bị **phân bổ thực hiện (assignment)** theo quy tắc hợp đồng.

Cần hiểu tác động lên vị thế tài sản cơ sở, tiền mặt và ký quỹ.

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **36. Rủi ro pin** nối từ **35. Phân bổ nghĩa vụ thực hiện** sang **37. Hoán đổi lãi suất**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. Rủi ro pin

Gần đáo hạn, giá cơ sở quanh giá thực hiện có thể làm trạng thái sau đáo hạn không chắc chắn. Đây là rủi ro vận hành chứ không chỉ rủi ro hướng giá.

# Phần IX — Hoán đổi

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **37. Hoán đổi lãi suất** nối từ **36. Rủi ro pin** sang **38. OIS**, vì cơ chế trước tạo đầu vào cho bước sau.

## 37. Hoán đổi lãi suất

Interest-rate swap tách rủi ro lãi suất khỏi tài sản cơ sở bằng cách đổi dòng fixed/floating. Hãy xác định notional, reset dates, curve tham chiếu và collateral trước khi đánh giá hedge.

**Hoán đổi lãi suất (interest-rate swap)** thường đổi dòng thanh toán lãi cố định lấy lãi thả nổi hoặc ngược lại.

Nó cho phép thay đổi mức phơi nhiễm lãi suất mà không cần mua bán toàn bộ danh mục trái phiếu.

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **38. OIS** nối từ **37. Hoán đổi lãi suất** sang **39. Hoán đổi chéo tiền tệ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 38. OIS

OIS dùng lãi suất qua đêm để phản ánh đường đi policy và discounting trong nhiều thị trường. Nó là cầu nối giữa kỳ vọng lãi suất ngắn hạn và định giá hợp đồng.

**Hoán đổi chỉ số qua đêm (Overnight Index Swap, OIS)** dùng lãi suất qua đêm làm tham chiếu và thường được dùng để suy ra đường đi lãi suất chính sách kỳ vọng.

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **39. Hoán đổi chéo tiền tệ** nối từ **38. OIS** sang **40. Hoán đổi tổng lợi suất**, vì cơ chế trước tạo đầu vào cho bước sau.

## 39. Hoán đổi chéo tiền tệ

Cross-currency swap kết hợp rủi ro lãi suất với rủi ro FX và funding. Việc trao đổi gốc và dòng coupon tạo exposure khác với một forward đơn lẻ.

**Hoán đổi chéo tiền tệ (cross-currency swap)** trao đổi dòng tiền giữa hai đồng tiền và có thể kèm trao đổi gốc.

Nó liên quan chi phí nguồn vốn và cơ sở hoán đổi tiền tệ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **40. Hoán đổi tổng lợi suất** nối từ **39. Hoán đổi chéo tiền tệ** sang **41. CDS**, vì cơ chế trước tạo đầu vào cho bước sau.

## 40. Hoán đổi tổng lợi suất

TRS chuyển lợi suất kinh tế của asset hoặc index mà không nhất thiết chuyển quyền sở hữu trực tiếp. Người dùng phải đọc cùng collateral, counterparty và financing.

**Hoán đổi tổng lợi suất (Total Return Swap, TRS)** chuyển toàn bộ lợi suất kinh tế của tài sản hoặc chỉ số giữa hai bên mà không cần chuyển quyền sở hữu trực tiếp.

Cấu trúc này tạo rủi ro đối tác và rủi ro tài sản bảo đảm.

# Phần X — Phái sinh tín dụng

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **41. CDS** nối từ **40. Hoán đổi tổng lợi suất** sang **42. Chỉ số tín dụng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 41. CDS

CDS chuyển một phần rủi ro credit theo hợp đồng premium–protection. Spread CDS phản ánh xác suất, recovery, liquidity và risk premium chứ không phải xác suất default thuần.

**Hoán đổi rủi ro tín dụng (Credit Default Swap, CDS)** chuyển rủi ro vỡ nợ theo hợp đồng.

Người mua bảo vệ trả phí; người bán bảo vệ bồi thường nếu sự kiện tín dụng được định nghĩa xảy ra.

Chênh lệch CDS không phải xác suất vỡ nợ thuần túy vì còn phản ánh giả định thu hồi, thanh khoản và phần bù rủi ro.

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **42. Chỉ số tín dụng** nối từ **41. CDS** sang **43. Hoán đổi phương sai**, vì cơ chế trước tạo đầu vào cho bước sau.

## 42. Chỉ số tín dụng

CDX, iTraxx và chỉ số tương tự gom nhiều tên tín dụng để giao dịch mức phơi nhiễm rộng hơn.

# Phần XI — Phái sinh biến động

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **43. Hoán đổi phương sai** nối từ **42. Chỉ số tín dụng** sang **44. CFD là gì?**, vì cơ chế trước tạo đầu vào cho bước sau.

## 43. Hoán đổi phương sai

Variance swap tạo exposure trực tiếp với realized variance, nên payoff khác option thông thường và nhạy với jump, sampling, corridor và settlement.

**Hoán đổi phương sai (variance swap)** tạo mức phơi nhiễm trực tiếp hơn với phương sai thực hiện so với quyền chọn thông thường.

Điểm cần hiểu là biến động cũng có thể được giao dịch như một dạng rủi ro kinh tế riêng.

# Phần XII — CFD

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **44. CFD là gì?** nối từ **43. Hoán đổi phương sai** sang **45. Chi phí tài trợ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 44. CFD là gì?

CFD là hợp đồng song phương nên kết quả phụ thuộc giá cơ sở, spread, financing, margin, stop-out và pháp nhân broker. Không nên đồng nhất CFD với quyền sở hữu tài sản cơ sở.

**Hợp đồng chênh lệch (Contract for Difference, CFD)** là hợp đồng song phương với nhà môi giới dựa trên thay đổi giá của tài sản cơ sở.

Nhà giao dịch thường không sở hữu tài sản cơ sở.

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **45. Chi phí tài trợ** nối từ **44. CFD là gì?** sang **46. Rủi ro đối tác với nhà môi giới**, vì cơ chế trước tạo đầu vào cho bước sau.

## 45. Chi phí tài trợ

Vị thế CFD giữ qua đêm có thể chịu phí tài trợ. Chi phí này có thể làm chiến lược dài hạn kém hiệu quả dù hướng giá đúng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **46. Rủi ro đối tác với nhà môi giới** nối từ **45. Chi phí tài trợ** sang **47. CFD và futures trên sở không giống nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## 46. Rủi ro đối tác với nhà môi giới

Cần hiểu:

- pháp nhân ký hợp đồng;
- cơ quan quản lý;
- quy tắc tách tiền khách hàng;
- mô hình thực thi;
- mức đóng cưỡng bức;
- bảo vệ số dư âm nếu có.

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **47. CFD và futures trên sở không giống nhau** nối từ **46. Rủi ro đối tác với nhà môi giới** sang **48. Tài sản bảo đảm**, vì cơ chế trước tạo đầu vào cho bước sau.

## 47. CFD và futures trên sở không giống nhau

Futures có hợp đồng chuẩn và bù trừ tập trung. CFD thường là hợp đồng song phương với nhà môi giới.

Hai sản phẩm cùng theo vàng có thể có rủi ro pháp lý và cấu trúc chi phí rất khác.

# Phần XIII — Tài sản bảo đảm và rủi ro đối tác

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **48. Tài sản bảo đảm** nối từ **47. CFD và futures trên sở không giống nhau** sang **49. Bù trừ nghĩa vụ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 48. Tài sản bảo đảm

Phái sinh có thể yêu cầu tiền mặt hoặc chứng khoán làm **tài sản bảo đảm (collateral)**.

Yêu cầu tài sản bảo đảm tăng trong căng thẳng có thể buộc nhà đầu tư bán tài sản khác để lấy tiền.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **49. Bù trừ nghĩa vụ** nối từ **48. Tài sản bảo đảm** sang **50. Rủi ro sai chiều đối tác**, vì cơ chế trước tạo đầu vào cho bước sau.

## 49. Bù trừ nghĩa vụ

Netting giảm gross exposure giữa nhiều giao dịch khi điều khoản pháp lý cho phép. Giá trị của nó phụ thuộc enforceability, close-out và cấu trúc đối tác, không chỉ vào phép cộng số dư.

**Bù trừ pháp lý (netting)** cho phép bù các mức phơi nhiễm giữa nhiều giao dịch cùng đối tác theo điều kiện hợp đồng.

Khả năng giảm rủi ro phụ thuộc hiệu lực pháp lý của thỏa thuận.

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **50. Rủi ro sai chiều đối tác** nối từ **49. Bù trừ nghĩa vụ** sang **51. Công cụ phòng vệ phải khớp loại rủi ro**, vì cơ chế trước tạo đầu vào cho bước sau.

## 50. Rủi ro sai chiều đối tác

Wrong-way risk xảy ra khi đối tác yếu đi đúng lúc exposure với họ tăng. Đây là rủi ro kết hợp giữa chất lượng đối tác và trạng thái thị trường, nên cần stress chung thay vì tách riêng.

**Rủi ro sai chiều (wrong-way risk)** xảy ra khi đối tác yếu đi đúng lúc mức phơi nhiễm với họ tăng.

Ví dụ dùng một đối tác có sức khỏe phụ thuộc cùng loại tín dụng để phòng vệ chính rủi ro đó.

# Phần XIV — Tỷ lệ phòng vệ

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **51. Công cụ phòng vệ phải khớp loại rủi ro** nối từ **50. Rủi ro sai chiều đối tác** sang **52. Không phòng vệ chỉ theo giá trị danh nghĩa**, vì cơ chế trước tạo đầu vào cho bước sau.

## 51. Công cụ phòng vệ phải khớp loại rủi ro

Trước khi chọn công cụ, hãy xác định rủi ro cần giảm là delta, duration, FX, credit, volatility, liquidity hay funding. Sơ đồ này là điểm chốt để tránh dùng một hedge đúng tên nhưng sai exposure.

```text
Rủi ro lãi suất
→ DV01 / futures lãi suất / hoán đổi

Beta cổ phiếu
→ futures chỉ số

Rủi ro tỷ giá
→ hợp đồng kỳ hạn / futures

Rủi ro đuôi
→ quyền chọn
```

Chọn công cụ không khớp tạo **rủi ro cơ sở (basis risk)**.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **52. Không phòng vệ chỉ theo giá trị danh nghĩa** nối từ **51. Công cụ phòng vệ phải khớp loại rủi ro** sang **53. Lịch hợp đồng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 52. Không phòng vệ chỉ theo giá trị danh nghĩa

Hai trái phiếu cùng giá trị danh nghĩa nhưng duration khác nhau có rủi ro lãi suất khác nhau.

Tỷ lệ phòng vệ nên dựa trên độ nhạy phù hợp như DV01, beta, Delta hoặc mức phơi nhiễm tiền tệ.

# Phần XV — Quản lý đáo hạn và chuyển kỳ hạn

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **53. Lịch hợp đồng** nối từ **52. Không phòng vệ chỉ theo giá trị danh nghĩa** sang **54. Dịch chuyển thanh khoản**, vì cơ chế trước tạo đầu vào cho bước sau.

## 53. Lịch hợp đồng

Nhà giao dịch phái sinh phải theo dõi:

- ngày giao dịch cuối;
- ngày thông báo đầu tiên nếu có;
- ngày thanh toán;
- ngày đáo hạn quyền chọn;
- thời điểm thanh khoản chuyển sang hợp đồng kế tiếp.

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **54. Dịch chuyển thanh khoản** nối từ **53. Lịch hợp đồng** sang **55. Không nhìn từng vị thế riêng lẻ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 54. Dịch chuyển thanh khoản

Khối lượng thường chuyển từ hợp đồng gần sang hợp đồng kế tiếp trước đáo hạn. Giữ hợp đồng cũ quá lâu có thể làm chênh lệch và trượt giá tăng.

# Phần XVI — Rủi ro tổng hợp ở cấp danh mục

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **55. Không nhìn từng vị thế riêng lẻ** nối từ **54. Dịch chuyển thanh khoản** sang **56. Lãi/lỗ và ký quỹ phải được kiểm thử cùng nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## 55. Không nhìn từng vị thế riêng lẻ

Một danh mục có thể gồm quyền chọn mua, quyền chọn bán, futures và CFD nhưng tổng rủi ro phải được quy đổi theo:

- Delta;
- Gamma;
- Vega;
- DV01;
- FX;
- giá trị danh nghĩa;
- ký quỹ;
- rủi ro đối tác.

> **Nối mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **56. Lãi/lỗ và ký quỹ phải được kiểm thử cùng nhau** nối từ **55. Không nhìn từng vị thế riêng lẻ** sang **57. Phân rã lãi/lỗ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 56. Lãi/lỗ và ký quỹ phải được kiểm thử cùng nhau

Một kịch bản đúng cần hỏi đồng thời:

```text
Tài sản cơ sở thay đổi bao nhiêu?
Quyền chọn đổi Delta/Gamma/Vega ra sao?
Lãi/lỗ là bao nhiêu?
Yêu cầu ký quỹ mới là bao nhiêu?
Có đủ tiền mặt để duy trì vị thế không?
```

Một vị thế có lợi nhuận kỳ vọng dương vẫn có thể bị đóng cưỡng bức nếu thiếu thanh khoản giữa đường.

> **Nối mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **57. Phân rã lãi/lỗ** nối từ **56. Lãi/lỗ và ký quỹ phải được kiểm thử cùng nhau** sang **Kết luận**, vì cơ chế trước tạo đầu vào cho bước sau.

## 57. Phân rã lãi/lỗ

Lãi/lỗ phái sinh có thể tách theo:

```text
Biến động tài sản cơ sở
Biến động lãi suất / tỷ giá
Carry
Basis
Biến động hàm ý
Hao mòn thời gian
Chi phí chuyển kỳ hạn
Chi phí tài trợ
Chi phí giao dịch
```

Việc phân rã giúp biết luận điểm đúng nhưng triển khai sai ở đâu.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **Kết luận** tổng hợp từ **57. Phân rã lãi/lỗ** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Kết luận

Phái sinh không tạo lợi thế đầu tư chỉ vì cho phép dùng đòn bẩy. Giá trị của chúng nằm ở khả năng chuyển, phòng vệ hoặc định hình rủi ro một cách chính xác hơn.

Trước khi dùng bất kỳ sản phẩm nào, hãy trả lời:

```text
Tài sản cơ sở là gì?
Quyền và nghĩa vụ của hợp đồng là gì?
Giá trị danh nghĩa bao nhiêu?
Tổn thất trong kịch bản xấu là bao nhiêu?
Ký quỹ có thể tăng tới đâu?
Ai là đối tác pháp lý?
Thanh khoản khi căng thẳng ra sao?
Khi nào phải chuyển kỳ hạn hoặc thanh toán?
```

Nếu chưa trả lời được các câu này, chưa nên dùng đòn bẩy chỉ vì mức ký quỹ ban đầu trông nhỏ.

> **Bàn giao:** Sau **Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
