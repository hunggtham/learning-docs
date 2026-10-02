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

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **2. Thông số hợp đồng** tiếp nhận điểm tựa từ **1. Quyền sở hữu khác mức phơi nhiễm theo hợp đồng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Giá trị danh nghĩa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **3. Giá trị danh nghĩa** tiếp nhận điểm tựa từ **2. Thông số hợp đồng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Hợp đồng kỳ hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **4. Hợp đồng kỳ hạn** tiếp nhận điểm tựa từ **3. Giá trị danh nghĩa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Hợp đồng tương lai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Hợp đồng kỳ hạn

Forward bắt đầu từ thỏa thuận song phương và rủi ro đối tác. Hãy đọc giá, ngày giao hàng, tài sản cơ sở và collateral trước khi so nó với futures niêm yết.

**Hợp đồng kỳ hạn (forward)** là thỏa thuận hai bên mua hoặc bán tài sản trong tương lai theo mức giá đã định trước.

Forward thường giao dịch ngoài sở (OTC), vì vậy rủi ro đối tác, tài sản bảo đảm và điều khoản đóng vị thế rất quan trọng.

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **5. Hợp đồng tương lai** tiếp nhận điểm tựa từ **4. Hợp đồng kỳ hạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Ký quỹ ban đầu và ký quỹ duy trì** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Hợp đồng tương lai

Futures chuẩn hóa các điều khoản và thêm clearing, margin, expiry và settlement. Điều này giảm một số rủi ro đối tác trực tiếp nhưng tạo yêu cầu ký quỹ và roll cần quản lý.

**Hợp đồng tương lai (futures)** được chuẩn hóa và thường giao dịch trên sở với cơ chế bù trừ tập trung.

Chuẩn hóa giúp thanh khoản tốt hơn nhưng nhà giao dịch phải tuân thủ hệ số hợp đồng, ngày đáo hạn, ký quỹ và quy tắc thanh toán của từng sản phẩm.

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **6. Ký quỹ ban đầu và ký quỹ duy trì** tiếp nhận điểm tựa từ **5. Hợp đồng tương lai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Ký quỹ biến đổi và đánh dấu theo thị trường** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Ký quỹ ban đầu và ký quỹ duy trì

Margin là cơ chế giữ cho hợp đồng có đủ collateral khi giá thay đổi. Phân biệt initial và maintenance margin giúp người mới hiểu vì sao một vị thế có thể bị gọi bổ sung vốn trước khi thesis dài hạn sai.

**Ký quỹ ban đầu (initial margin)** là tài sản bảo đảm cần khi mở vị thế.

**Ký quỹ duy trì (maintenance margin)** là mức tối thiểu phải giữ sau đó.

Nếu giá trị tài khoản giảm dưới ngưỡng, nhà môi giới hoặc thành viên bù trừ có thể yêu cầu bổ sung tiền hoặc đóng vị thế.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **7. Ký quỹ biến đổi và đánh dấu theo thị trường** tiếp nhận điểm tựa từ **6. Ký quỹ ban đầu và ký quỹ duy trì** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Cơ sở giá** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Ký quỹ biến đổi và đánh dấu theo thị trường

Hợp đồng tương lai thường được đánh dấu lại theo giá thị trường định kỳ.

```text
Giá thay đổi
→ lãi/lỗ được ghi nhận
→ tiền mặt dịch chuyển qua hệ thống ký quỹ
```

Vì vậy quản lý thanh khoản rất quan trọng ngay cả khi luận điểm dài hạn vẫn đúng.

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **8. Cơ sở giá** tiếp nhận điểm tựa từ **7. Ký quỹ biến đổi và đánh dấu theo thị trường** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Hội tụ khi đáo hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **9. Hội tụ khi đáo hạn** tiếp nhận điểm tựa từ **8. Cơ sở giá** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Contango và backwardation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Hội tụ khi đáo hạn

Gần đáo hạn, giá hợp đồng tương lai và giá giao ngay thường hội tụ nhờ cơ chế thanh toán và chênh lệch giá, tùy sản phẩm.

Nếu không hiểu cơ chế thanh toán, nhà giao dịch có thể vô tình giữ hợp đồng tới giai đoạn không mong muốn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **10. Contango và backwardation** tiếp nhận điểm tựa từ **9. Hội tụ khi đáo hạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Chuyển kỳ hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Contango và backwardation

Đường cong futures ảnh hưởng lợi suất roll bên cạnh biến động spot. Vì vậy, contango/backwardation cần được đọc như một phần của tổng lợi suất và chi phí chuyển kỳ.

**Contango** thường mô tả cấu trúc trong đó giá kỳ hạn xa cao hơn giá gần hoặc giá giao ngay. **Backwardation** mô tả trường hợp ngược lại.

Không nên kết luận tăng hay giảm chỉ từ hai nhãn này. Cần xem chi phí nắm giữ, tồn kho, mức khan hiếm và nhu cầu phòng vệ.

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **11. Chuyển kỳ hạn** tiếp nhận điểm tựa từ **10. Contango và backwardation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Hợp đồng tương lai hàng hóa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Chuyển kỳ hạn

Muốn duy trì vị thế sau khi hợp đồng cũ gần đáo hạn, nhà đầu tư phải **chuyển kỳ hạn (roll)** sang hợp đồng mới.

Quá trình này tạo:

- phí giao dịch;
- rủi ro cơ sở;
- lợi suất cuộn kỳ hạn;
- rủi ro thanh khoản.

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **12. Hợp đồng tương lai hàng hóa** tiếp nhận điểm tựa từ **11. Chuyển kỳ hạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Trái phiếu rẻ nhất để giao trong futures trái phiếu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Hợp đồng tương lai hàng hóa

Ngoài biến động giá, hàng hóa còn chịu:

- chi phí lưu kho;
- mức tồn kho;
- mùa vụ;
- quy tắc giao hàng vật chất;
- lợi ích tiện ích khi nắm hàng hóa.

Người chỉ muốn giao dịch tài chính phải đặc biệt hiểu ngày thông báo giao hàng và điều khoản vật chất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **13. Trái phiếu rẻ nhất để giao trong futures trái phiếu** tiếp nhận điểm tựa từ **12. Hợp đồng tương lai hàng hóa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Quyền chọn mua và quyền chọn bán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Trái phiếu rẻ nhất để giao trong futures trái phiếu

Một số hợp đồng tương lai trái phiếu cho phép bên bán giao nhiều loại trái phiếu đủ điều kiện. Trái phiếu kinh tế nhất để giao được gọi là **cheapest-to-deliver (CTD)**.

Vì vậy phòng vệ bằng futures trái phiếu còn phụ thuộc hệ số chuyển đổi và sự thay đổi của CTD, không chỉ giá futures.

# Phần III — Quyền chọn

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **14. Quyền chọn mua và quyền chọn bán** tiếp nhận điểm tựa từ **13. Trái phiếu rẻ nhất để giao trong futures trái phiếu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Phí quyền chọn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Quyền chọn mua và quyền chọn bán

Khoản chi trả tại đáo hạn:

```text
Call = max(S - K, 0)
Put  = max(K - S, 0)
```

Người mua trả phí để có quyền; người bán nhận phí nhưng gánh nghĩa vụ tương ứng.

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **15. Phí quyền chọn** tiếp nhận điểm tựa từ **14. Quyền chọn mua và quyền chọn bán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Giá trị nội tại và giá trị thời gian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Phí quyền chọn

Premium là giá phải trả cho payoff không đối xứng. Người mua cần tách intrinsic value khỏi time value và hiểu IV, thời gian, lãi suất cùng dividend có thể làm premium thay đổi.

**Phí quyền chọn (premium)** không chỉ gồm giá trị nội tại. Trước đáo hạn, giá còn phụ thuộc:

- thời gian;
- biến động hàm ý;
- lãi suất;
- cổ tức;
- chi phí vay;
- hình dạng bề mặt biến động.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **16. Giá trị nội tại và giá trị thời gian** tiếp nhận điểm tựa từ **15. Phí quyền chọn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Độ gần tiền** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Giá trị nội tại và giá trị thời gian

Phần này tách hai lớp tạo nên premium trước đáo hạn. Intrinsic value nói về trạng thái hiện tại so với strike; time value phản ánh cơ hội và bất định còn lại cho tới expiry.

```text
Giá quyền chọn
= Giá trị nội tại
+ Giá trị thời gian
```

Giá trị thời gian thường giảm khi đáo hạn tới gần nhưng tốc độ giảm không tuyến tính.

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **17. Độ gần tiền** tiếp nhận điểm tựa từ **16. Giá trị nội tại và giá trị thời gian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Delta** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Độ gần tiền

Moneyness đặt option vào quan hệ giữa spot và strike, từ đó quyết định payoff, delta gần đúng và phần premium là intrinsic hay time value.

**Độ gần tiền (moneyness)** thường được mô tả bằng:

- ITM: đang có giá trị nội tại;
- ATM: gần giá thực hiện;
- OTM: ngoài tiền.

Độ gần tiền ảnh hưởng Delta, Gamma, thanh khoản và hình dạng phân phối khoản chi trả.

# Phần IV — Greeks

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **18. Delta** tiếp nhận điểm tựa từ **17. Độ gần tiền** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Gamma** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Delta

Delta đo độ nhạy của giá quyền chọn với thay đổi nhỏ của tài sản cơ sở. Delta không cố định; nó thay đổi theo giá, thời gian và biến động.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **19. Gamma** tiếp nhận điểm tựa từ **18. Delta** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Theta** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Gamma

Gamma đo tốc độ Delta thay đổi khi giá cơ sở thay đổi.

Mua quyền chọn thường Gamma dương; bán quyền chọn thường Gamma âm. Gamma âm có thể làm tổn thất tăng nhanh khi thị trường di chuyển mạnh.

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **20. Theta** tiếp nhận điểm tựa từ **19. Gamma** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Vega** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Theta

Theta mô tả hao mòn giá trị theo thời gian. Người mua quyền chọn thường trả chi phí thời gian; người bán thường thu Theta nhưng đổi lại chịu rủi ro Gamma và rủi ro đuôi.

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **21. Vega** tiếp nhận điểm tựa từ **20. Theta** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Rho** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Vega

Vega đo độ nhạy với biến động hàm ý. Đúng hướng giá vẫn có thể lỗ nếu IV giảm đủ mạnh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **22. Rho** tiếp nhận điểm tựa từ **21. Vega** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. IV không phải dự báo chắc chắn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Rho

Rho đo độ nhạy với lãi suất. Với quyền chọn ngắn hạn tác động thường nhỏ hơn Delta hoặc Vega, nhưng với kỳ hạn dài có thể đáng kể.

# Phần V — Biến động hàm ý

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **23. IV không phải dự báo chắc chắn** tiếp nhận điểm tựa từ **22. Rho** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Biến động thực hiện và biến động hàm ý** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. IV không phải dự báo chắc chắn

IV là mức biến động được suy ra từ giá option hiện tại, không phải lời tiên tri về realized volatility. Hãy đọc nó cùng risk premium, skew, term structure và thanh khoản.

**Biến động hàm ý (implied volatility, IV)** là mức biến động làm mô hình phù hợp với giá quyền chọn đang giao dịch.

Nó phản ánh đồng thời:

- kỳ vọng biến động;
- phần bù rủi ro;
- cung cầu quyền chọn;
- nhu cầu phòng vệ.

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **24. Biến động thực hiện và biến động hàm ý** tiếp nhận điểm tựa từ **23. IV không phải dự báo chắc chắn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. IV giảm mạnh sau sự kiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Biến động thực hiện và biến động hàm ý

So sánh realized với implied giúp kiểm tra option đang đắt/rẻ tương đối theo một giả định, nhưng cần cẩn thận với horizon, sampling và thay đổi regime.

**Biến động thực hiện (realized volatility)** là biến động thật đã xảy ra. **Biến động hàm ý** là mức được suy ra từ giá quyền chọn.

Nhiều chiến lược quyền chọn thực chất đặt cược vào khoảng cách giữa hai mức này.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **25. IV giảm mạnh sau sự kiện** tiếp nhận điểm tựa từ **24. Biến động thực hiện và biến động hàm ý** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Quyền chọn bán bảo vệ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. IV giảm mạnh sau sự kiện

Trước sự kiện, IV có thể cao vì bất định. Sau khi thông tin được công bố, IV có thể giảm nhanh, hiện tượng thường gọi là **IV crush**.

Do đó mua quyền chọn trước sự kiện cần đúng không chỉ hướng mà còn độ lớn biến động và mức IV đã trả.

# Phần VI — Các cấu trúc quyền chọn cơ bản

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **26. Quyền chọn bán bảo vệ** tiếp nhận điểm tựa từ **25. IV giảm mạnh sau sự kiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Covered lời gọi (call / 호출)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Quyền chọn bán bảo vệ

Protective put đổi một phần premium lấy giới hạn rủi ro giảm. Câu hỏi đúng là chi phí bảo hiểm có phù hợp với mục tiêu, thời hạn và khả năng chịu drawdown của danh mục không.

**Protective put** là nắm tài sản cơ sở và mua quyền chọn bán để giới hạn phần giảm dưới một vùng nhất định. Chi phí là phí quyền chọn lặp lại.

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **27. Covered lời gọi (call / 호출)** tiếp nhận điểm tựa từ **26. Quyền chọn bán bảo vệ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Chênh lệch dọc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Covered lời gọi (call / 호출)

Covered call tạo thu nhập premium bằng cách bán một phần upside và convexity. Nó phù hợp với một số mục tiêu income nhưng không phải hedge giảm hoàn chỉnh.

**Covered call** là nắm tài sản cơ sở và bán quyền chọn mua. Nhà đầu tư thu phí nhưng đổi lại giới hạn một phần mức tăng và đang bán độ lồi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **28. Chênh lệch dọc** tiếp nhận điểm tựa từ **27. Covered lời gọi (call / 호출)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Collar** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Chênh lệch dọc

Vertical spread dùng hai strike để đổi giới hạn chi phí lấy giới hạn payoff. Phần này cần được đọc như một bài toán trade-off giữa premium, xác suất và mức chi trả tối đa.

**Vertical spread** dùng hai quyền chọn cùng kỳ hạn nhưng khác giá thực hiện để giới hạn cả chi phí lẫn khoản chi trả.

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **29. Collar** tiếp nhận điểm tựa từ **28. Chênh lệch dọc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Straddle và strangle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Collar

Collar kết hợp bảo vệ downside với việc bán upside để giảm chi phí. Thiết kế tốt phải nói rõ vùng bảo vệ, vùng bị giới hạn và điều kiện thoát.

**Collar** kết hợp tài sản cơ sở, quyền chọn bán và quyền chọn mua bán ra để giảm chi phí bảo vệ nhưng giới hạn phần tăng.

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **30. Straddle và strangle** tiếp nhận điểm tựa từ **29. Collar** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Bán quyền chọn không phải thu nhập đều đặn miễn phí** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Straddle và strangle

Hai cấu trúc này tập trung nhiều hơn vào độ lớn biến động thay vì chỉ hướng giá. Lãi/lỗ phụ thuộc biến động thực tế so với mức đã được định giá và hao mòn thời gian.

# Phần VII — Rủi ro bán quyền chọn

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **31. Bán quyền chọn không phải thu nhập đều đặn miễn phí** tiếp nhận điểm tựa từ **30. Straddle và strangle** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Bán quyền chọn mua không có tài sản bảo đảm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Bán quyền chọn không phải thu nhập đều đặn miễn phí

Chiến lược bán biến động có thể thắng nhiều lần nhỏ rồi thua rất lớn trong sự kiện đuôi.

```text
Tỷ lệ thắng cao
≠ rủi ro thấp
```

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **32. Bán quyền chọn mua không có tài sản bảo đảm** tiếp nhận điểm tựa từ **31. Bán quyền chọn không phải thu nhập đều đặn miễn phí** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Bán quyền chọn bán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Bán quyền chọn mua không có tài sản bảo đảm

Naked call tạo exposure short convexity với rủi ro tăng rất lớn. Trước khi nhìn premium nhận được, hãy stress giá cơ sở, margin và gap.

**Naked call** có mức lỗ lý thuyết rất lớn khi tài sản cơ sở tăng mạnh.

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **33. Bán quyền chọn bán** tiếp nhận điểm tựa từ **32. Bán quyền chọn mua không có tài sản bảo đảm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Kiểu Mỹ và kiểu châu Âu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Bán quyền chọn bán

Short put gần với cam kết mua tài sản ở strike nếu giá giảm. Premium không xóa rủi ro tail; cần tính collateral, assignment và khả năng thanh toán khi thị trường gap.

**Short put** gần với cam kết mua tài sản ở giá thực hiện khi thị trường giảm. Cần tính yêu cầu ký quỹ và rủi ro nhảy giá.

# Phần VIII — Thực hiện quyền và phân bổ nghĩa vụ

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **34. Kiểu Mỹ và kiểu châu Âu** tiếp nhận điểm tựa từ **33. Bán quyền chọn bán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Phân bổ nghĩa vụ thực hiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Kiểu Mỹ và kiểu châu Âu

Quyền chọn kiểu Mỹ có thể được thực hiện trước đáo hạn. Quyền chọn kiểu châu Âu chỉ được thực hiện tại đáo hạn theo điều khoản.

Tên gọi này mô tả kiểu thực hiện quyền, không phải vị trí địa lý của thị trường.

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **35. Phân bổ nghĩa vụ thực hiện** tiếp nhận điểm tựa từ **34. Kiểu Mỹ và kiểu châu Âu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Rủi ro pin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Phân bổ nghĩa vụ thực hiện

Người bán quyền chọn có thể bị **phân bổ thực hiện (assignment)** theo quy tắc hợp đồng.

Cần hiểu tác động lên vị thế tài sản cơ sở, tiền mặt và ký quỹ.

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **36. Rủi ro pin** tiếp nhận điểm tựa từ **35. Phân bổ nghĩa vụ thực hiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Hoán đổi lãi suất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Rủi ro pin

Gần đáo hạn, giá cơ sở quanh giá thực hiện có thể làm trạng thái sau đáo hạn không chắc chắn. Đây là rủi ro vận hành chứ không chỉ rủi ro hướng giá.

# Phần IX — Hoán đổi

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **37. Hoán đổi lãi suất** tiếp nhận điểm tựa từ **36. Rủi ro pin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. OIS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Hoán đổi lãi suất

Interest-rate swap tách rủi ro lãi suất khỏi tài sản cơ sở bằng cách đổi dòng fixed/floating. Hãy xác định notional, reset dates, curve tham chiếu và collateral trước khi đánh giá hedge.

**Hoán đổi lãi suất (interest-rate swap)** thường đổi dòng thanh toán lãi cố định lấy lãi thả nổi hoặc ngược lại.

Nó cho phép thay đổi mức phơi nhiễm lãi suất mà không cần mua bán toàn bộ danh mục trái phiếu.

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **38. OIS** tiếp nhận điểm tựa từ **37. Hoán đổi lãi suất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Hoán đổi chéo tiền tệ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. OIS

OIS dùng lãi suất qua đêm để phản ánh đường đi policy và discounting trong nhiều thị trường. Nó là cầu nối giữa kỳ vọng lãi suất ngắn hạn và định giá hợp đồng.

**Hoán đổi chỉ số qua đêm (Overnight Index Swap, OIS)** dùng lãi suất qua đêm làm tham chiếu và thường được dùng để suy ra đường đi lãi suất chính sách kỳ vọng.

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **39. Hoán đổi chéo tiền tệ** tiếp nhận điểm tựa từ **38. OIS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Hoán đổi tổng lợi suất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Hoán đổi chéo tiền tệ

Cross-currency swap kết hợp rủi ro lãi suất với rủi ro FX và funding. Việc trao đổi gốc và dòng coupon tạo exposure khác với một forward đơn lẻ.

**Hoán đổi chéo tiền tệ (cross-currency swap)** trao đổi dòng tiền giữa hai đồng tiền và có thể kèm trao đổi gốc.

Nó liên quan chi phí nguồn vốn và cơ sở hoán đổi tiền tệ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **40. Hoán đổi tổng lợi suất** tiếp nhận điểm tựa từ **39. Hoán đổi chéo tiền tệ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. CDS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Hoán đổi tổng lợi suất

TRS chuyển lợi suất kinh tế của asset hoặc index mà không nhất thiết chuyển quyền sở hữu trực tiếp. Người dùng phải đọc cùng collateral, counterparty và financing.

**Hoán đổi tổng lợi suất (Total Return Swap, TRS)** chuyển toàn bộ lợi suất kinh tế của tài sản hoặc chỉ số giữa hai bên mà không cần chuyển quyền sở hữu trực tiếp.

Cấu trúc này tạo rủi ro đối tác và rủi ro tài sản bảo đảm.

# Phần X — Phái sinh tín dụng

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **41. CDS** tiếp nhận điểm tựa từ **40. Hoán đổi tổng lợi suất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. Chỉ số tín dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. CDS

CDS chuyển một phần rủi ro credit theo hợp đồng premium–protection. Spread CDS phản ánh xác suất, recovery, liquidity và risk premium chứ không phải xác suất default thuần.

**Hoán đổi rủi ro tín dụng (Credit Default Swap, CDS)** chuyển rủi ro vỡ nợ theo hợp đồng.

Người mua bảo vệ trả phí; người bán bảo vệ bồi thường nếu sự kiện tín dụng được định nghĩa xảy ra.

Chênh lệch CDS không phải xác suất vỡ nợ thuần túy vì còn phản ánh giả định thu hồi, thanh khoản và phần bù rủi ro.

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **42. Chỉ số tín dụng** tiếp nhận điểm tựa từ **41. CDS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Hoán đổi phương sai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. Chỉ số tín dụng

CDX, iTraxx và chỉ số tương tự gom nhiều tên tín dụng để giao dịch mức phơi nhiễm rộng hơn.

# Phần XI — Phái sinh biến động

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **43. Hoán đổi phương sai** tiếp nhận điểm tựa từ **42. Chỉ số tín dụng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. CFD là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Hoán đổi phương sai

Variance swap tạo exposure trực tiếp với realized variance, nên payoff khác option thông thường và nhạy với jump, sampling, corridor và settlement.

**Hoán đổi phương sai (variance swap)** tạo mức phơi nhiễm trực tiếp hơn với phương sai thực hiện so với quyền chọn thông thường.

Điểm cần hiểu là biến động cũng có thể được giao dịch như một dạng rủi ro kinh tế riêng.

# Phần XII — CFD

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **44. CFD là gì?** tiếp nhận điểm tựa từ **43. Hoán đổi phương sai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. Chi phí tài trợ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. CFD là gì?

CFD là hợp đồng song phương nên kết quả phụ thuộc giá cơ sở, spread, financing, margin, stop-out và pháp nhân broker. Không nên đồng nhất CFD với quyền sở hữu tài sản cơ sở.

**Hợp đồng chênh lệch (Contract for Difference, CFD)** là hợp đồng song phương với nhà môi giới dựa trên thay đổi giá của tài sản cơ sở.

Nhà giao dịch thường không sở hữu tài sản cơ sở.

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **45. Chi phí tài trợ** tiếp nhận điểm tựa từ **44. CFD là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **46. Rủi ro đối tác với nhà môi giới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. Chi phí tài trợ

Vị thế CFD giữ qua đêm có thể chịu phí tài trợ. Chi phí này có thể làm chiến lược dài hạn kém hiệu quả dù hướng giá đúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **46. Rủi ro đối tác với nhà môi giới** tiếp nhận điểm tựa từ **45. Chi phí tài trợ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **47. CFD và futures trên sở không giống nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. Rủi ro đối tác với nhà môi giới

Cần hiểu:

- pháp nhân ký hợp đồng;
- cơ quan quản lý;
- quy tắc tách tiền khách hàng;
- mô hình thực thi;
- mức đóng cưỡng bức;
- bảo vệ số dư âm nếu có.

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **47. CFD và futures trên sở không giống nhau** tiếp nhận điểm tựa từ **46. Rủi ro đối tác với nhà môi giới** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **48. Tài sản bảo đảm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. CFD và futures trên sở không giống nhau

Futures có hợp đồng chuẩn và bù trừ tập trung. CFD thường là hợp đồng song phương với nhà môi giới.

Hai sản phẩm cùng theo vàng có thể có rủi ro pháp lý và cấu trúc chi phí rất khác.

# Phần XIII — Tài sản bảo đảm và rủi ro đối tác

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **48. Tài sản bảo đảm** tiếp nhận điểm tựa từ **47. CFD và futures trên sở không giống nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **49. Bù trừ nghĩa vụ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 48. Tài sản bảo đảm

Phái sinh có thể yêu cầu tiền mặt hoặc chứng khoán làm **tài sản bảo đảm (collateral)**.

Yêu cầu tài sản bảo đảm tăng trong căng thẳng có thể buộc nhà đầu tư bán tài sản khác để lấy tiền.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **49. Bù trừ nghĩa vụ** tiếp nhận điểm tựa từ **48. Tài sản bảo đảm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **50. Rủi ro sai chiều đối tác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 49. Bù trừ nghĩa vụ

Netting giảm gross exposure giữa nhiều giao dịch khi điều khoản pháp lý cho phép. Giá trị của nó phụ thuộc enforceability, close-out và cấu trúc đối tác, không chỉ vào phép cộng số dư.

**Bù trừ pháp lý (netting)** cho phép bù các mức phơi nhiễm giữa nhiều giao dịch cùng đối tác theo điều kiện hợp đồng.

Khả năng giảm rủi ro phụ thuộc hiệu lực pháp lý của thỏa thuận.

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **50. Rủi ro sai chiều đối tác** tiếp nhận điểm tựa từ **49. Bù trừ nghĩa vụ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **51. Công cụ phòng vệ phải khớp loại rủi ro** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 50. Rủi ro sai chiều đối tác

Wrong-way risk xảy ra khi đối tác yếu đi đúng lúc exposure với họ tăng. Đây là rủi ro kết hợp giữa chất lượng đối tác và trạng thái thị trường, nên cần stress chung thay vì tách riêng.

**Rủi ro sai chiều (wrong-way risk)** xảy ra khi đối tác yếu đi đúng lúc mức phơi nhiễm với họ tăng.

Ví dụ dùng một đối tác có sức khỏe phụ thuộc cùng loại tín dụng để phòng vệ chính rủi ro đó.

# Phần XIV — Tỷ lệ phòng vệ

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **51. Công cụ phòng vệ phải khớp loại rủi ro** tiếp nhận điểm tựa từ **50. Rủi ro sai chiều đối tác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **52. Không phòng vệ chỉ theo giá trị danh nghĩa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **52. Không phòng vệ chỉ theo giá trị danh nghĩa** tiếp nhận điểm tựa từ **51. Công cụ phòng vệ phải khớp loại rủi ro** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **53. Lịch hợp đồng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 52. Không phòng vệ chỉ theo giá trị danh nghĩa

Hai trái phiếu cùng giá trị danh nghĩa nhưng duration khác nhau có rủi ro lãi suất khác nhau.

Tỷ lệ phòng vệ nên dựa trên độ nhạy phù hợp như DV01, beta, Delta hoặc mức phơi nhiễm tiền tệ.

# Phần XV — Quản lý đáo hạn và chuyển kỳ hạn

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **53. Lịch hợp đồng** tiếp nhận điểm tựa từ **52. Không phòng vệ chỉ theo giá trị danh nghĩa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **54. Dịch chuyển thanh khoản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 53. Lịch hợp đồng

Nhà giao dịch phái sinh phải theo dõi:

- ngày giao dịch cuối;
- ngày thông báo đầu tiên nếu có;
- ngày thanh toán;
- ngày đáo hạn quyền chọn;
- thời điểm thanh khoản chuyển sang hợp đồng kế tiếp.

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **54. Dịch chuyển thanh khoản** tiếp nhận điểm tựa từ **53. Lịch hợp đồng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **55. Không nhìn từng vị thế riêng lẻ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 54. Dịch chuyển thanh khoản

Khối lượng thường chuyển từ hợp đồng gần sang hợp đồng kế tiếp trước đáo hạn. Giữ hợp đồng cũ quá lâu có thể làm chênh lệch và trượt giá tăng.

# Phần XVI — Rủi ro tổng hợp ở cấp danh mục

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **55. Không nhìn từng vị thế riêng lẻ** tiếp nhận điểm tựa từ **54. Dịch chuyển thanh khoản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **56. Lãi/lỗ và ký quỹ phải được kiểm thử cùng nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **56. Lãi/lỗ và ký quỹ phải được kiểm thử cùng nhau** tiếp nhận điểm tựa từ **55. Không nhìn từng vị thế riêng lẻ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **57. Phân rã lãi/lỗ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **57. Phân rã lãi/lỗ** tiếp nhận điểm tựa từ **56. Lãi/lỗ và ký quỹ phải được kiểm thử cùng nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kết luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD**, **Kết luận** gom các mảnh từ **57. Phân rã lãi/lỗ** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

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
