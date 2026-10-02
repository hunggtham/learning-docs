# Trái phiếu, lãi suất và tín dụng

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trái phiếu, lãi suất và tín dụng**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Trái phiếu là hợp đồng cho vay** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Giá trái phiếu là giá trị hiện tại của dòng tiền** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối bonds với rates và credit, để đọc duration, spread và default risk trong cùng một đường truyền giá.

> Trái phiếu thường bị mô tả như “sản phẩm an toàn trả lãi cố định”. Cách hiểu đó quá đơn giản. Trái phiếu là một tập hợp dòng tiền theo hợp đồng chịu đồng thời rủi ro lãi suất, lạm phát, tín dụng, thanh khoản, quyền chọn và đôi khi cả tỷ giá. Chương này xây tư duy từ nguyên lý định giá tới đường cong lợi suất, chênh lệch tín dụng, các cấu trúc chứng khoán hóa và cách triển khai qua quỹ trái phiếu.

## 1. Trái phiếu là hợp đồng cho vay

Người nắm trái phiếu cho tổ chức phát hành vay vốn và nhận dòng tiền theo hợp đồng. Mệnh giá (face/par value) là khoản gốc tham chiếu; coupon là khoản lãi; ngày đáo hạn (maturity) là ngày hoàn trả gốc nếu không vỡ nợ.

Trái chủ khác cổ đông: trái chủ có quyền đòi theo hợp đồng và thường đứng cao hơn trong cấu trúc vốn, nhưng mức tăng giá trị kinh tế thường bị giới hạn hơn cổ phiếu.

> **Chuyển mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **2. Giá trái phiếu là giá trị hiện tại của dòng tiền** tiếp nhận điểm tựa từ **1. Trái phiếu là hợp đồng cho vay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Giá sạch và giá bẩn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Giá trái phiếu là giá trị hiện tại của dòng tiền

Trước khi học duration, spread hay các loại trái phiếu, cần đặt nền bằng câu hỏi: giá hôm nay là bao nhiêu khi các coupon và tiền gốc trong tương lai được chiết khấu về hiện tại? Công thức dưới đây trả lời câu hỏi đó.

```text
Bond Price = Σ Coupon_t / (1 + y)^t + Face Value / (1 + y)^T
```

Khi lợi suất yêu cầu tăng, giá trị hiện tại của dòng tiền cố định giảm; vì vậy giá và lợi suất thường đi ngược chiều.

Một trái phiếu chính phủ có thể giảm giá mạnh dù gần như không có rủi ro vỡ nợ vì lãi suất chiết khấu đã thay đổi.

> **Chuyển mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **3. Giá sạch và giá bẩn** tiếp nhận điểm tựa từ **2. Giá trái phiếu là giá trị hiện tại của dòng tiền** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Coupon, hiện tại (current / 현재) yield và YTM khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Giá sạch và giá bẩn

Giá sạch (clean price) không bao gồm lãi dồn tích. Giá bẩn (dirty price) là số tiền thực tế gần với giá thanh toán:

```text
Dirty Price = Clean Price + Accrued Interest
```

Khi so báo giá và tính lợi suất, phải biết thị trường đang sử dụng loại giá nào.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **4. Coupon, hiện tại (current / 현재) yield và YTM khác nhau** tiếp nhận điểm tựa từ **3. Giá sạch và giá bẩn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Yield to lời gọi (call / 호출) và Yield to Worst** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Coupon, hiện tại (current / 현재) yield và YTM khác nhau

Coupon là lãi theo hợp đồng trên mệnh giá. Lợi suất hiện tại (current yield) gần bằng coupon năm chia giá thị trường. Lợi suất đến đáo hạn (Yield to Maturity, YTM) là tỷ lệ chiết khấu khiến giá trị hiện tại của dòng tiền bằng giá hiện tại với một số giả định.

YTM không phải lợi suất chắc chắn vì nhà đầu tư có thể bán trước đáo hạn, tổ chức phát hành có thể vỡ nợ hoặc dòng tiền phải tái đầu tư ở mức lãi khác.

> **Chuyển mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **5. Yield to lời gọi (call / 호출) và Yield to Worst** tiếp nhận điểm tựa từ **4. Coupon, hiện tại (current / 현재) yield và YTM khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Duration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Yield to lời gọi (call / 호출) và Yield to Worst

Trái phiếu có quyền mua lại trước hạn (callable bond) cho phép tổ chức phát hành hoàn trả sớm theo điều khoản.

Khi lãi suất giảm, doanh nghiệp có động cơ tái cấp vốn rẻ hơn và mua lại trái phiếu coupon cao, làm hạn chế phần tăng giá của nhà đầu tư.

Vì vậy cần xem lợi suất tới ngày gọi lại (yield to call) và lợi suất xấu nhất (yield to worst), không chỉ YTM.

> **Chuyển mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **6. Duration** tiếp nhận điểm tựa từ **5. Yield to lời gọi (call / 호출) và Yield to Worst** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. DV01/PV01** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Duration

Duration đo thời điểm trung bình có trọng số của dòng tiền và độ nhạy của giá với lợi suất.

```text
%ΔPrice ≈ -Modified Duration × ΔYield
```

Trái phiếu kỳ hạn dài, coupon thấp và lợi suất thấp thường có duration cao hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **7. DV01/PV01** tiếp nhận điểm tựa từ **6. Duration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Convexity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. DV01/PV01

DV01/PV01 đo mức thay đổi giá trị khi lợi suất dịch chuyển 1 điểm cơ bản.

Đây là thước đo tiền tệ trực tiếp hơn duration. Một danh mục có DV01 lớn có thể biến động đáng kể chỉ với thay đổi nhỏ của lãi suất.

> **Chuyển mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **8. Convexity** tiếp nhận điểm tựa từ **7. DV01/PV01** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Effective Duration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Convexity

Quan hệ giá–lợi suất là đường cong chứ không phải đường thẳng. Convexity đo độ cong này.

Với trái phiếu thông thường có convexity dương, mức tăng giá khi lợi suất giảm thường lớn hơn mức giảm khi lợi suất tăng cùng một độ lớn so với xấp xỉ tuyến tính.

Khi có quyền chọn nhúng, convexity có thể thay đổi mạnh.

> **Chuyển mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **9. Effective Duration** tiếp nhận điểm tựa từ **8. Convexity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Key-Rate Duration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Effective Duration

Với trái phiếu có dòng tiền thay đổi theo lãi suất, như MBS hoặc callable bond, modified duration cố định có thể không đủ.

Duration hiệu dụng (effective duration) ước lượng độ nhạy sau khi cho phép dòng tiền thay đổi khi lãi suất thay đổi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **10. Key-Rate Duration** tiếp nhận điểm tựa từ **9. Effective Duration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Đường cong lợi suất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Key-Rate Duration

Đường cong lợi suất không luôn dịch chuyển song song. Lợi suất 2Y có thể tăng trong khi 10Y không đổi.

Duration theo điểm kỳ hạn (key-rate duration) phân rã độ nhạy theo các đoạn của đường cong. Hai danh mục cùng tổng duration vẫn có thể chịu rủi ro đường cong rất khác nhau.

> **Chuyển mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **11. Đường cong lợi suất** tiếp nhận điểm tựa từ **10. Key-Rate Duration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Steepening và Flattening** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Đường cong lợi suất

Đường cong nối lợi suất theo kỳ hạn. Đầu ngắn thường nhạy với lãi suất chính sách hiện tại và kỳ vọng. Đầu dài phản ánh đường đi lãi suất tương lai, tăng trưởng, lạm phát, nguồn cung trái phiếu và phần bù kỳ hạn.

```text
Long-term yield ≈ Expected future short rates + Term premium
```

> **Chuyển mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **12. Steepening và Flattening** tiếp nhận điểm tựa từ **11. Đường cong lợi suất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Đường cong đảo ngược** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Steepening và Flattening

Đường cong dốc hơn (steepening) chỉ nói chênh lệch dài–ngắn tăng, không nói nguyên nhân.

- **Bull steepener**: lợi suất ngắn giảm nhanh hơn dài, thường gắn với kỳ vọng hạ lãi suất hoặc suy thoái.
- **Bear steepener**: lợi suất dài tăng nhanh hơn, có thể do lạm phát, nguồn cung trái phiếu hoặc phần bù kỳ hạn.

Flattening cũng có phiên bản do lợi suất tăng hoặc giảm. Không nên học thuộc “steepening tốt, inversion xấu” mà không nhìn nguyên nhân.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **13. Đường cong đảo ngược** tiếp nhận điểm tựa từ **12. Steepening và Flattening** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Lợi suất danh nghĩa, lợi suất thực và kỳ vọng lạm phát hòa vốn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Đường cong đảo ngược

Đường cong đảo ngược xảy ra khi lợi suất ngắn cao hơn lợi suất dài ở một số kỳ hạn. Nó thường phản ánh chính sách hiện tại chặt trong khi thị trường kỳ vọng lãi suất thấp hơn trong tương lai.

Đảo ngược có thông tin về chu kỳ nhưng không cho thời điểm chính xác. Đường cong có thể dốc trở lại vì hạ lãi suất trong suy thoái hoặc vì đầu dài tăng do lạm phát/tài khóa; hai trường hợp có tác động rất khác.

> **Chuyển mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **14. Lợi suất danh nghĩa, lợi suất thực và kỳ vọng lạm phát hòa vốn** tiếp nhận điểm tựa từ **13. Đường cong đảo ngược** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Carry** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Lợi suất danh nghĩa, lợi suất thực và kỳ vọng lạm phát hòa vốn

Lợi suất danh nghĩa có thể được hiểu gần đúng là lợi suất thực cộng kỳ vọng lạm phát và các phần bù rủi ro.

Chênh lệch giữa Treasury danh nghĩa và TIPS cùng kỳ hạn thường được dùng làm kỳ vọng lạm phát hòa vốn (breakeven inflation), nhưng còn chứa phần bù rủi ro lạm phát và khác biệt thanh khoản.

Lợi suất thực đặc biệt quan trọng với vàng và cổ phiếu duration dài.

> **Chuyển mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **15. Carry** tiếp nhận điểm tựa từ **14. Lợi suất danh nghĩa, lợi suất thực và kỳ vọng lạm phát hòa vốn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Roll-Down** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Carry

Lợi suất nắm giữ (carry) là thu nhập mà vị thế tạo ra nếu các điều kiện khác không thay đổi, ví dụ coupon và ảnh hưởng của tài trợ.

Carry không phải lợi suất chắc chắn. Một khoản carry nhỏ có thể bị xóa bởi thay đổi lãi suất hoặc spread lớn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **16. Roll-Down** tiếp nhận điểm tựa từ **15. Carry** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Trái phiếu chính phủ, doanh nghiệp và thứ tự ưu tiên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Roll-Down

Nếu đường cong dốc và hình dạng không đổi, trái phiếu khi tiến gần đáo hạn có thể “trượt” xuống điểm có lợi suất thấp hơn, tạo lợi nhuận giá. Đây là lợi suất trượt theo đường cong (roll-down).

```text
Expected fixed-income return
≈ Carry + Roll-down + Rate move + Spread move + Default/Recovery + FX
```

> **Chuyển mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **17. Trái phiếu chính phủ, doanh nghiệp và thứ tự ưu tiên** tiếp nhận điểm tựa từ **16. Roll-Down** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Chênh lệch tín dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Trái phiếu chính phủ, doanh nghiệp và thứ tự ưu tiên

Nợ chính phủ thường là mốc tham chiếu lãi suất trong đồng tiền tương ứng, nhưng rủi ro chính phủ vẫn phụ thuộc cấu trúc tài khóa/tiền tệ.

Nợ doanh nghiệp thêm rủi ro kinh doanh và vỡ nợ. Nợ có bảo đảm đứng cao hơn nợ không bảo đảm; nợ cao cấp đứng trên nợ thứ cấp.

Không so hai trái phiếu chỉ bằng lợi suất nếu thứ tự ưu tiên, tài sản bảo đảm, kỳ hạn và quyền chọn khác nhau.

> **Chuyển mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **18. Chênh lệch tín dụng** tiếp nhận điểm tựa từ **17. Trái phiếu chính phủ, doanh nghiệp và thứ tự ưu tiên** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Z-Spread và OAS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Chênh lệch tín dụng

Chênh lệch tín dụng (credit spread) là phần lợi suất cao hơn mốc phi rủi ro tương ứng. Nó bù cho:

```text
Tổn thất vỡ nợ kỳ vọng
Bất định
Thanh khoản
Ác cảm rủi ro
Cung–cầu kỹ thuật
```

Công thức trực giác:

```text
Expected Credit Loss ≈ PD × LGD × Exposure
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **19. Z-Spread và OAS** tiếp nhận điểm tựa từ **18. Chênh lệch tín dụng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Spread Duration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Z-Spread và OAS

Z-spread là mức chênh lệch cố định cộng vào toàn bộ đường cong chuẩn để chiết khấu dòng tiền hợp đồng về đúng giá.

OAS (Option-Adjusted Spread) điều chỉnh thêm giá trị quyền chọn nhúng. Với trái phiếu callable hoặc MBS, OAS thường hữu ích hơn spread đơn giản vì tách một phần tác động của quyền chọn.

> **Chuyển mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **20. Spread Duration** tiếp nhận điểm tựa từ **19. Z-Spread và OAS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Rating không thay thế phân tích tín dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Spread Duration

Trái phiếu doanh nghiệp chịu cả duration lãi suất và duration chênh lệch tín dụng.

Treasury yield có thể giảm 100bp nhưng credit spread tăng 200bp, khiến trái phiếu doanh nghiệp vẫn giảm.

Đây là lý do high yield thường có hành vi gần cổ phiếu hơn trái phiếu chính phủ trong suy thoái.

> **Chuyển mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **21. Rating không thay thế phân tích tín dụng** tiếp nhận điểm tựa từ **20. Spread Duration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Thanh khoản của doanh nghiệp đi vay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Rating không thay thế phân tích tín dụng

Xếp hạng tín dụng là đánh giá hữu ích nhưng có thể chậm hơn thị trường. Chênh lệch tín dụng thường phản ứng trước khi xếp hạng thay đổi.

Cần xem đòn bẩy, khả năng trả lãi, dòng tiền tự do, tính chu kỳ, giá trị tài sản, lịch đáo hạn và khả năng tiếp cận vốn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **22. Thanh khoản của doanh nghiệp đi vay** tiếp nhận điểm tựa từ **21. Rating không thay thế phân tích tín dụng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Bức tường đáo hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Thanh khoản của doanh nghiệp đi vay

Một công ty có tài sản tốt vẫn có thể vỡ nợ nếu không đủ tiền hoặc không tái cấp vốn được trước đáo hạn.

Cần xây “đường chạy thanh khoản” (liquidity runway):

```text
Tiền mặt
+ FCF dự kiến
+ Hạn mức chưa dùng
+ Khả năng bán tài sản
so với
Nợ đáo hạn
+ Lãi vay
+ Capex bắt buộc
+ Nghĩa vụ khác
```

> **Chuyển mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **23. Bức tường đáo hạn** tiếp nhận điểm tựa từ **22. Thanh khoản của doanh nghiệp đi vay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Chu kỳ tín dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Bức tường đáo hạn

Nếu lượng lớn nợ đáo hạn tập trung trong 12–24 tháng, chi phí tái cấp vốn có thể tăng đột ngột ngay cả khi tỷ lệ nợ/EBITDA hiện tại chưa xấu.

Phải xem nợ cố định/thả nổi, có bảo đảm/không bảo đảm và lịch đáo hạn theo từng năm.

> **Chuyển mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **24. Chu kỳ tín dụng** tiếp nhận điểm tựa từ **23. Bức tường đáo hạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Fallen Angels và Rising Stars** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Chu kỳ tín dụng

Một chu kỳ thường có dạng:

```text
Tín dụng dễ
→ Đòn bẩy tích tụ
→ Cú sốc
→ Spread mở rộng
→ Tái cấp vốn khó
→ Vỡ nợ / Giảm đòn bẩy
→ Sửa chữa bảng cân đối
```

Tín dụng khuếch đại chu kỳ kinh doanh vì tiêu chuẩn cho vay thay đổi theo giá tài sản và chất lượng người vay.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **25. Fallen Angels và Rising Stars** tiếp nhận điểm tựa từ **24. Chu kỳ tín dụng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Khoản vay lãi suất thả nổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Fallen Angels và Rising Stars

Xếp hạng tín dụng thay đổi có thể tạo dòng lệnh kỹ thuật từ quỹ và chỉ số, đồng thời phản ánh thay đổi trong rủi ro tín dụng. Phần này nối sự kiện rating với giá, spread và thanh khoản chứ không chỉ với nhãn investment grade/high yield.

**Fallen angel** là tổ chức phát hành bị hạ từ investment grade xuống high yield. Việc bị loại khỏi chỉ số/quỹ có giới hạn xếp hạng có thể tạo bán kỹ thuật.

**Rising star** là tổ chức được nâng từ high yield lên investment grade. Dòng vốn kỹ thuật có thể đi hướng ngược lại.

Phân tích phải tách thay đổi chất lượng tín dụng thật khỏi dòng vốn do quy tắc chỉ số.

> **Chuyển mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **26. Khoản vay lãi suất thả nổi** tiếp nhận điểm tựa từ **25. Fallen Angels và Rising Stars** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Leveraged Loans và Covenant** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Khoản vay lãi suất thả nổi

Công cụ lãi suất thả nổi có duration lãi suất thấp hơn nhưng người vay chịu chi phí lãi tăng nhanh khi benchmark tăng.

Nhà đầu tư giảm rủi ro giá do lãi suất nhưng có thể tăng rủi ro tín dụng gián tiếp vì khả năng trả lãi của người vay xấu đi.

> **Chuyển mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **27. Leveraged Loans và Covenant** tiếp nhận điểm tựa từ **26. Khoản vay lãi suất thả nổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Trái phiếu liên kết lạm phát** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Leveraged Loans và Covenant

Khoản vay đòn bẩy (leveraged loan) thường cho doanh nghiệp có đòn bẩy cao. Điều khoản bảo vệ (covenant) có thể yêu cầu duy trì tỷ lệ tài chính hoặc giới hạn hành động.

Khoản vay covenant-lite cho người cho vay ít quyền can thiệp sớm hơn. Lợi suất cao phải được đọc cùng chất lượng điều khoản.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, sau nội dung của **27. Leveraged Loans và Covenant**, **28. Trái phiếu liên kết lạm phát** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **29. MBS và convexity âm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Trái phiếu liên kết lạm phát

TIPS và các trái phiếu liên kết lạm phát điều chỉnh gốc hoặc dòng tiền theo chỉ số giá theo quy tắc.

Chúng bảo vệ sức mua tốt hơn trong một số tình huống nhưng vẫn chịu duration của lợi suất thực. Một năm CPI cao vẫn có thể tạo lỗ nếu lợi suất thực tăng mạnh.

> **Chuyển mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **29. MBS và convexity âm** tiếp nhận điểm tựa từ **28. Trái phiếu liên kết lạm phát** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. ABS và phân tầng rủi ro** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. MBS và convexity âm

Chứng khoán bảo đảm bằng khoản vay thế chấp (MBS) nhận dòng tiền từ các khoản vay mua nhà. Người vay có quyền trả trước.

Khi lãi suất giảm, tái cấp vốn tăng và nhà đầu tư nhận lại tiền sớm đúng lúc muốn giữ coupon cao. Khi lãi suất tăng, trả trước chậm và duration kéo dài.

Đây là trực giác của convexity âm.

> **Chuyển mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **30. ABS và phân tầng rủi ro** tiếp nhận điểm tựa từ **29. MBS và convexity âm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Trái phiếu chính phủ nội tệ và ngoại tệ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. ABS và phân tầng rủi ro

Chứng khoán bảo đảm bằng tài sản (ABS) gom dòng tiền từ các khoản vay/tài sản rồi chia thành các tầng (tranche) có thứ tự nhận tiền và chịu lỗ khác nhau.

Một pool tài sản tương đối ổn định vẫn có thể tạo tranche rủi ro cao nếu cấu trúc phân bổ lỗ phức tạp. Cần hiểu waterfall, credit enhancement và trigger.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **31. Trái phiếu chính phủ nội tệ và ngoại tệ** tiếp nhận điểm tựa từ **30. ABS và phân tầng rủi ro** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. ETF trái phiếu không giống trái phiếu riêng lẻ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Trái phiếu chính phủ nội tệ và ngoại tệ

Chính phủ vay bằng đồng tiền mình kiểm soát có rủi ro khác chính phủ vay bằng ngoại tệ.

Nợ nội tệ có thể giảm rủi ro vỡ nợ danh nghĩa nhưng vẫn có rủi ro lạm phát và mất giá tiền tệ. Nợ ngoại tệ phụ thuộc dự trữ ngoại hối, cán cân thanh toán và khả năng tiếp cận thị trường quốc tế.

> **Chuyển mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **32. ETF trái phiếu không giống trái phiếu riêng lẻ** tiếp nhận điểm tựa từ **31. Trái phiếu chính phủ nội tệ và ngoại tệ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Thanh khoản ETF trái phiếu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. ETF trái phiếu không giống trái phiếu riêng lẻ

Trái phiếu riêng lẻ giữ tới đáo hạn có kỳ hạn còn lại giảm dần. ETF trái phiếu thông thường liên tục thay trái phiếu để duy trì vùng kỳ hạn mục tiêu.

Vì vậy “giữ ETF trái phiếu tới đáo hạn” thường là mô hình sai, trừ các quỹ mục tiêu đáo hạn có cấu trúc đặc biệt.

> **Chuyển mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **33. Thanh khoản ETF trái phiếu** tiếp nhận điểm tựa từ **32. ETF trái phiếu không giống trái phiếu riêng lẻ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Thang đáo hạn, bullet và barbell** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Thanh khoản ETF trái phiếu

ETF có thể giao dịch thường xuyên dù trái phiếu cơ sở OTC và ít thanh khoản. Trong khủng hoảng, giá ETF có thể lệch NAV do NAV dùng báo giá cũ trong khi ETF đang khám phá giá nhanh hơn.

Cần xem spread, AUM, chất lượng tài sản, duration và thanh khoản tài sản cơ sở.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **34. Thang đáo hạn, bullet và barbell** tiếp nhận điểm tựa từ **33. Thanh khoản ETF trái phiếu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Immunization và liability matching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Thang đáo hạn, bullet và barbell

Sau khi hiểu duration và đường cong, ta chuyển sang cách sắp xếp các ngày đáo hạn để đáp ứng nghĩa vụ và kiểm soát tái đầu tư. Ba cấu trúc dưới đây khác nhau ở dòng tiền, độ nhạy và rủi ro tập trung thời điểm.

**Bond ladder** trải kỳ hạn để tạo dòng tiền gốc đều.

**Bullet** tập trung kỳ hạn quanh một mốc để khớp nghĩa vụ.

**Barbell** kết hợp kỳ hạn ngắn và dài thay vì tập trung ở giữa.

Hai danh mục có cùng duration tổng nhưng khác cấu trúc đường cong và rủi ro tái đầu tư.

> **Chuyển mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **35. Immunization và liability matching** tiếp nhận điểm tựa từ **34. Thang đáo hạn, bullet và barbell** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Phòng vệ lãi suất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Immunization và liability matching

Immunization cố gắng khớp duration/convexity của tài sản với nghĩa vụ để giảm nhạy với thay đổi lãi suất.

Đây là tư duy khác với “mua trái phiếu vì nghĩ lãi suất sẽ giảm”. Mục tiêu là bảo vệ khả năng thanh toán nghĩa vụ.

> **Chuyển mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **36. Phòng vệ lãi suất** tiếp nhận điểm tựa từ **35. Immunization và liability matching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Phòng vệ tín dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Phòng vệ lãi suất

Có thể dùng futures hoặc swap để điều chỉnh DV01 mà không bán toàn bộ trái phiếu.

Phòng vệ tốt cần khớp độ nhạy theo đường cong, không chỉ giá trị danh nghĩa. Curve twist có thể làm hedge một điểm kỳ hạn không hoàn hảo.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **37. Phòng vệ tín dụng** tiếp nhận điểm tựa từ **36. Phòng vệ lãi suất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Khi long-duration bond đa dạng hóa cổ phiếu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Phòng vệ tín dụng

CDS hoặc chỉ số tín dụng có thể giảm rủi ro spread/default, nhưng thêm rủi ro đối tác, basis và cấu trúc hợp đồng.

Một hedge tín dụng không loại bỏ rủi ro thanh khoản của trái phiếu cơ sở.

> **Chuyển mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **38. Khi long-duration bond đa dạng hóa cổ phiếu** tiếp nhận điểm tựa từ **37. Phòng vệ tín dụng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Phân rã lợi suất thu nhập cố định** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Khi long-duration bond đa dạng hóa cổ phiếu

Trái phiếu chính phủ dài hạn thường hữu ích trong suy thoái do cầu yếu và giảm phát, khi lợi suất có xu hướng giảm.

Trong cú sốc lạm phát, cổ phiếu và trái phiếu dài hạn có thể cùng giảm. Tương quan cổ phiếu–trái phiếu phụ thuộc chế độ kinh tế.

> **Chuyển mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **39. Phân rã lợi suất thu nhập cố định** tiếp nhận điểm tựa từ **38. Khi long-duration bond đa dạng hóa cổ phiếu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Checklist trái phiếu hoặc ETF trái phiếu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Phân rã lợi suất thu nhập cố định

Phân rã lợi suất giúp tách coupon/carry, thay đổi yield, credit spread, roll-down, FX, default và chi phí. Mục tiêu là biết phần lợi nhuận nào đến từ exposure chủ động và phần nào chỉ là bù rủi ro đã nhận.

```text
Tổng lợi suất
= Thu nhập / Carry
+ Roll-down
+ Thay đổi lãi suất
+ Thay đổi đường cong
+ Thay đổi spread
+ Quyền chọn
+ Vỡ nợ / Thu hồi
+ FX
- Chi phí
```

Phân rã này giúp biết lợi nhuận đến từ nhận coupon, cược duration hay chấp nhận tín dụng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **40. Checklist trái phiếu hoặc ETF trái phiếu** tiếp nhận điểm tựa từ **39. Phân rã lợi suất thu nhập cố định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kết luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Checklist trái phiếu hoặc ETF trái phiếu

Checklist cuối cùng chuyển toàn bộ chapter thành quy trình trước khi mua. Hãy đi từ dòng tiền và duration tới tín dụng, thanh khoản, ETF mechanics, chi phí và kịch bản stress; nếu thiếu một lớp, kết luận về yield có thể sai.

```text
Tổ chức phát hành
Thứ tự ưu tiên / Tài sản bảo đảm
Kỳ hạn / Call
Coupon cố định hay thả nổi
YTM / YTW
Duration / DV01 / Convexity
Spread / OAS
Xếp hạng và rủi ro ngầm định
Thanh khoản và lịch đáo hạn nợ
Tiền tệ
Khả năng tái cấp vốn
Kịch bản xấu nhất hợp lý
```

Với ETF, thêm chất lượng tín dụng trung bình, cơ cấu holdings, thanh khoản tài sản cơ sở, phí, tracking và phòng vệ FX.

> **Chuyển mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **Kết luận** gom các mảnh từ **40. Checklist trái phiếu hoặc ETF trái phiếu** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết luận

Lợi suất trái phiếu không thể rút gọn thành “nhận coupon”. Cần tách **thu nhập, lãi suất, đường cong, tín dụng, quyền chọn, thanh khoản, vỡ nợ, thu hồi và tỷ giá**. Chỉ khi hiểu từng thành phần, nhà đầu tư mới biết trái phiếu đang đóng vai trò phòng thủ, tạo thu nhập hay thực chất là một khoản cược vào duration hoặc tín dụng.

> **Bàn giao:** Sau **Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
