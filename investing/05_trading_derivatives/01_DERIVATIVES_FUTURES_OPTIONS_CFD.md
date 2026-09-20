# Phái sinh: hợp đồng tương lai, quyền chọn, hoán đổi và CFD

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

## 3. Giá trị danh nghĩa

**Giá trị danh nghĩa (notional)** là quy mô kinh tế của mức phơi nhiễm.

Với hợp đồng tương lai:

```text
Notional
= Giá hợp đồng tương lai × Hệ số hợp đồng
```

Tiền ký quỹ chỉ là tài sản bảo đảm, không phải giá trị danh nghĩa và cũng không phải mức lỗ tối đa.

# Phần II — Hợp đồng kỳ hạn và hợp đồng tương lai

## 4. Hợp đồng kỳ hạn

**Hợp đồng kỳ hạn (forward)** là thỏa thuận hai bên mua hoặc bán tài sản trong tương lai theo mức giá đã định trước.

Forward thường giao dịch ngoài sở (OTC), vì vậy rủi ro đối tác, tài sản bảo đảm và điều khoản đóng vị thế rất quan trọng.

## 5. Hợp đồng tương lai

**Hợp đồng tương lai (futures)** được chuẩn hóa và thường giao dịch trên sở với cơ chế bù trừ tập trung.

Chuẩn hóa giúp thanh khoản tốt hơn nhưng nhà giao dịch phải tuân thủ hệ số hợp đồng, ngày đáo hạn, ký quỹ và quy tắc thanh toán của từng sản phẩm.

## 6. Ký quỹ ban đầu và ký quỹ duy trì

**Ký quỹ ban đầu (initial margin)** là tài sản bảo đảm cần khi mở vị thế.

**Ký quỹ duy trì (maintenance margin)** là mức tối thiểu phải giữ sau đó.

Nếu giá trị tài khoản giảm dưới ngưỡng, nhà môi giới hoặc thành viên bù trừ có thể yêu cầu bổ sung tiền hoặc đóng vị thế.

## 7. Ký quỹ biến đổi và đánh dấu theo thị trường

Hợp đồng tương lai thường được đánh dấu lại theo giá thị trường định kỳ.

```text
Giá thay đổi
→ lãi/lỗ được ghi nhận
→ tiền mặt dịch chuyển qua hệ thống ký quỹ
```

Vì vậy quản lý thanh khoản rất quan trọng ngay cả khi luận điểm dài hạn vẫn đúng.

## 8. Cơ sở giá

**Cơ sở giá (basis)** là chênh lệch giữa giá hợp đồng tương lai và giá giao ngay theo quy ước của từng thị trường.

Nó chịu ảnh hưởng của:

- lãi suất;
- chi phí lưu kho;
- cổ tức;
- lợi ích tiện ích khi nắm hàng hóa;
- chi phí vay tài sản;
- cung cầu kỹ thuật.

## 9. Hội tụ khi đáo hạn

Gần đáo hạn, giá hợp đồng tương lai và giá giao ngay thường hội tụ nhờ cơ chế thanh toán và chênh lệch giá, tùy sản phẩm.

Nếu không hiểu cơ chế thanh toán, nhà giao dịch có thể vô tình giữ hợp đồng tới giai đoạn không mong muốn.

## 10. Contango và backwardation

**Contango** thường mô tả cấu trúc trong đó giá kỳ hạn xa cao hơn giá gần hoặc giá giao ngay. **Backwardation** mô tả trường hợp ngược lại.

Không nên kết luận tăng hay giảm chỉ từ hai nhãn này. Cần xem chi phí nắm giữ, tồn kho, mức khan hiếm và nhu cầu phòng vệ.

## 11. Chuyển kỳ hạn

Muốn duy trì vị thế sau khi hợp đồng cũ gần đáo hạn, nhà đầu tư phải **chuyển kỳ hạn (roll)** sang hợp đồng mới.

Quá trình này tạo:

- phí giao dịch;
- rủi ro cơ sở;
- lợi suất cuộn kỳ hạn;
- rủi ro thanh khoản.

## 12. Hợp đồng tương lai hàng hóa

Ngoài biến động giá, hàng hóa còn chịu:

- chi phí lưu kho;
- mức tồn kho;
- mùa vụ;
- quy tắc giao hàng vật chất;
- lợi ích tiện ích khi nắm hàng hóa.

Người chỉ muốn giao dịch tài chính phải đặc biệt hiểu ngày thông báo giao hàng và điều khoản vật chất.

## 13. Trái phiếu rẻ nhất để giao trong futures trái phiếu

Một số hợp đồng tương lai trái phiếu cho phép bên bán giao nhiều loại trái phiếu đủ điều kiện. Trái phiếu kinh tế nhất để giao được gọi là **cheapest-to-deliver (CTD)**.

Vì vậy phòng vệ bằng futures trái phiếu còn phụ thuộc hệ số chuyển đổi và sự thay đổi của CTD, không chỉ giá futures.

# Phần III — Quyền chọn

## 14. Quyền chọn mua và quyền chọn bán

Khoản chi trả tại đáo hạn:

```text
Call = max(S - K, 0)
Put  = max(K - S, 0)
```

Người mua trả phí để có quyền; người bán nhận phí nhưng gánh nghĩa vụ tương ứng.

## 15. Phí quyền chọn

**Phí quyền chọn (premium)** không chỉ gồm giá trị nội tại. Trước đáo hạn, giá còn phụ thuộc:

- thời gian;
- biến động hàm ý;
- lãi suất;
- cổ tức;
- chi phí vay;
- hình dạng bề mặt biến động.

## 16. Giá trị nội tại và giá trị thời gian

```text
Giá quyền chọn
= Giá trị nội tại
+ Giá trị thời gian
```

Giá trị thời gian thường giảm khi đáo hạn tới gần nhưng tốc độ giảm không tuyến tính.

## 17. Độ gần tiền

**Độ gần tiền (moneyness)** thường được mô tả bằng:

- ITM: đang có giá trị nội tại;
- ATM: gần giá thực hiện;
- OTM: ngoài tiền.

Độ gần tiền ảnh hưởng Delta, Gamma, thanh khoản và hình dạng phân phối khoản chi trả.

# Phần IV — Greeks

## 18. Delta

Delta đo độ nhạy của giá quyền chọn với thay đổi nhỏ của tài sản cơ sở. Delta không cố định; nó thay đổi theo giá, thời gian và biến động.

## 19. Gamma

Gamma đo tốc độ Delta thay đổi khi giá cơ sở thay đổi.

Mua quyền chọn thường Gamma dương; bán quyền chọn thường Gamma âm. Gamma âm có thể làm tổn thất tăng nhanh khi thị trường di chuyển mạnh.

## 20. Theta

Theta mô tả hao mòn giá trị theo thời gian. Người mua quyền chọn thường trả chi phí thời gian; người bán thường thu Theta nhưng đổi lại chịu rủi ro Gamma và rủi ro đuôi.

## 21. Vega

Vega đo độ nhạy với biến động hàm ý. Đúng hướng giá vẫn có thể lỗ nếu IV giảm đủ mạnh.

## 22. Rho

Rho đo độ nhạy với lãi suất. Với quyền chọn ngắn hạn tác động thường nhỏ hơn Delta hoặc Vega, nhưng với kỳ hạn dài có thể đáng kể.

# Phần V — Biến động hàm ý

## 23. IV không phải dự báo chắc chắn

**Biến động hàm ý (implied volatility, IV)** là mức biến động làm mô hình phù hợp với giá quyền chọn đang giao dịch.

Nó phản ánh đồng thời:

- kỳ vọng biến động;
- phần bù rủi ro;
- cung cầu quyền chọn;
- nhu cầu phòng vệ.

## 24. Biến động thực hiện và biến động hàm ý

**Biến động thực hiện (realized volatility)** là biến động thật đã xảy ra. **Biến động hàm ý** là mức được suy ra từ giá quyền chọn.

Nhiều chiến lược quyền chọn thực chất đặt cược vào khoảng cách giữa hai mức này.

## 25. IV giảm mạnh sau sự kiện

Trước sự kiện, IV có thể cao vì bất định. Sau khi thông tin được công bố, IV có thể giảm nhanh, hiện tượng thường gọi là **IV crush**.

Do đó mua quyền chọn trước sự kiện cần đúng không chỉ hướng mà còn độ lớn biến động và mức IV đã trả.

# Phần VI — Các cấu trúc quyền chọn cơ bản

## 26. Quyền chọn bán bảo vệ

**Protective put** là nắm tài sản cơ sở và mua quyền chọn bán để giới hạn phần giảm dưới một vùng nhất định. Chi phí là phí quyền chọn lặp lại.

## 27. Covered call

**Covered call** là nắm tài sản cơ sở và bán quyền chọn mua. Nhà đầu tư thu phí nhưng đổi lại giới hạn một phần mức tăng và đang bán độ lồi.

## 28. Chênh lệch dọc

**Vertical spread** dùng hai quyền chọn cùng kỳ hạn nhưng khác giá thực hiện để giới hạn cả chi phí lẫn khoản chi trả.

## 29. Collar

**Collar** kết hợp tài sản cơ sở, quyền chọn bán và quyền chọn mua bán ra để giảm chi phí bảo vệ nhưng giới hạn phần tăng.

## 30. Straddle và strangle

Hai cấu trúc này tập trung nhiều hơn vào độ lớn biến động thay vì chỉ hướng giá. Lãi/lỗ phụ thuộc biến động thực tế so với mức đã được định giá và hao mòn thời gian.

# Phần VII — Rủi ro bán quyền chọn

## 31. Bán quyền chọn không phải thu nhập đều đặn miễn phí

Chiến lược bán biến động có thể thắng nhiều lần nhỏ rồi thua rất lớn trong sự kiện đuôi.

```text
Tỷ lệ thắng cao
≠ rủi ro thấp
```

## 32. Bán quyền chọn mua không có tài sản bảo đảm

**Naked call** có mức lỗ lý thuyết rất lớn khi tài sản cơ sở tăng mạnh.

## 33. Bán quyền chọn bán

**Short put** gần với cam kết mua tài sản ở giá thực hiện khi thị trường giảm. Cần tính yêu cầu ký quỹ và rủi ro nhảy giá.

# Phần VIII — Thực hiện quyền và phân bổ nghĩa vụ

## 34. Kiểu Mỹ và kiểu châu Âu

Quyền chọn kiểu Mỹ có thể được thực hiện trước đáo hạn. Quyền chọn kiểu châu Âu chỉ được thực hiện tại đáo hạn theo điều khoản.

Tên gọi này mô tả kiểu thực hiện quyền, không phải vị trí địa lý của thị trường.

## 35. Phân bổ nghĩa vụ thực hiện

Người bán quyền chọn có thể bị **phân bổ thực hiện (assignment)** theo quy tắc hợp đồng.

Cần hiểu tác động lên vị thế tài sản cơ sở, tiền mặt và ký quỹ.

## 36. Rủi ro pin

Gần đáo hạn, giá cơ sở quanh giá thực hiện có thể làm trạng thái sau đáo hạn không chắc chắn. Đây là rủi ro vận hành chứ không chỉ rủi ro hướng giá.

# Phần IX — Hoán đổi

## 37. Hoán đổi lãi suất

**Hoán đổi lãi suất (interest-rate swap)** thường đổi dòng thanh toán lãi cố định lấy lãi thả nổi hoặc ngược lại.

Nó cho phép thay đổi mức phơi nhiễm lãi suất mà không cần mua bán toàn bộ danh mục trái phiếu.

## 38. OIS

**Hoán đổi chỉ số qua đêm (Overnight Index Swap, OIS)** dùng lãi suất qua đêm làm tham chiếu và thường được dùng để suy ra đường đi lãi suất chính sách kỳ vọng.

## 39. Hoán đổi chéo tiền tệ

**Hoán đổi chéo tiền tệ (cross-currency swap)** trao đổi dòng tiền giữa hai đồng tiền và có thể kèm trao đổi gốc.

Nó liên quan chi phí nguồn vốn và cơ sở hoán đổi tiền tệ.

## 40. Hoán đổi tổng lợi suất

**Hoán đổi tổng lợi suất (Total Return Swap, TRS)** chuyển toàn bộ lợi suất kinh tế của tài sản hoặc chỉ số giữa hai bên mà không cần chuyển quyền sở hữu trực tiếp.

Cấu trúc này tạo rủi ro đối tác và rủi ro tài sản bảo đảm.

# Phần X — Phái sinh tín dụng

## 41. CDS

**Hoán đổi rủi ro tín dụng (Credit Default Swap, CDS)** chuyển rủi ro vỡ nợ theo hợp đồng.

Người mua bảo vệ trả phí; người bán bảo vệ bồi thường nếu sự kiện tín dụng được định nghĩa xảy ra.

Chênh lệch CDS không phải xác suất vỡ nợ thuần túy vì còn phản ánh giả định thu hồi, thanh khoản và phần bù rủi ro.

## 42. Chỉ số tín dụng

CDX, iTraxx và chỉ số tương tự gom nhiều tên tín dụng để giao dịch mức phơi nhiễm rộng hơn.

# Phần XI — Phái sinh biến động

## 43. Hoán đổi phương sai

**Hoán đổi phương sai (variance swap)** tạo mức phơi nhiễm trực tiếp hơn với phương sai thực hiện so với quyền chọn thông thường.

Điểm cần hiểu là biến động cũng có thể được giao dịch như một dạng rủi ro kinh tế riêng.

# Phần XII — CFD

## 44. CFD là gì?

**Hợp đồng chênh lệch (Contract for Difference, CFD)** là hợp đồng song phương với nhà môi giới dựa trên thay đổi giá của tài sản cơ sở.

Nhà giao dịch thường không sở hữu tài sản cơ sở.

## 45. Chi phí tài trợ

Vị thế CFD giữ qua đêm có thể chịu phí tài trợ. Chi phí này có thể làm chiến lược dài hạn kém hiệu quả dù hướng giá đúng.

## 46. Rủi ro đối tác với nhà môi giới

Cần hiểu:

- pháp nhân ký hợp đồng;
- cơ quan quản lý;
- quy tắc tách tiền khách hàng;
- mô hình thực thi;
- mức đóng cưỡng bức;
- bảo vệ số dư âm nếu có.

## 47. CFD và futures trên sở không giống nhau

Futures có hợp đồng chuẩn và bù trừ tập trung. CFD thường là hợp đồng song phương với nhà môi giới.

Hai sản phẩm cùng theo vàng có thể có rủi ro pháp lý và cấu trúc chi phí rất khác.

# Phần XIII — Tài sản bảo đảm và rủi ro đối tác

## 48. Tài sản bảo đảm

Phái sinh có thể yêu cầu tiền mặt hoặc chứng khoán làm **tài sản bảo đảm (collateral)**.

Yêu cầu tài sản bảo đảm tăng trong căng thẳng có thể buộc nhà đầu tư bán tài sản khác để lấy tiền.

## 49. Bù trừ nghĩa vụ

**Bù trừ pháp lý (netting)** cho phép bù các mức phơi nhiễm giữa nhiều giao dịch cùng đối tác theo điều kiện hợp đồng.

Khả năng giảm rủi ro phụ thuộc hiệu lực pháp lý của thỏa thuận.

## 50. Rủi ro sai chiều đối tác

**Rủi ro sai chiều (wrong-way risk)** xảy ra khi đối tác yếu đi đúng lúc mức phơi nhiễm với họ tăng.

Ví dụ dùng một đối tác có sức khỏe phụ thuộc cùng loại tín dụng để phòng vệ chính rủi ro đó.

# Phần XIV — Tỷ lệ phòng vệ

## 51. Công cụ phòng vệ phải khớp loại rủi ro

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

## 52. Không phòng vệ chỉ theo giá trị danh nghĩa

Hai trái phiếu cùng giá trị danh nghĩa nhưng duration khác nhau có rủi ro lãi suất khác nhau.

Tỷ lệ phòng vệ nên dựa trên độ nhạy phù hợp như DV01, beta, Delta hoặc mức phơi nhiễm tiền tệ.

# Phần XV — Quản lý đáo hạn và chuyển kỳ hạn

## 53. Lịch hợp đồng

Nhà giao dịch phái sinh phải theo dõi:

- ngày giao dịch cuối;
- ngày thông báo đầu tiên nếu có;
- ngày thanh toán;
- ngày đáo hạn quyền chọn;
- thời điểm thanh khoản chuyển sang hợp đồng kế tiếp.

## 54. Dịch chuyển thanh khoản

Khối lượng thường chuyển từ hợp đồng gần sang hợp đồng kế tiếp trước đáo hạn. Giữ hợp đồng cũ quá lâu có thể làm chênh lệch và trượt giá tăng.

# Phần XVI — Rủi ro tổng hợp ở cấp danh mục

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