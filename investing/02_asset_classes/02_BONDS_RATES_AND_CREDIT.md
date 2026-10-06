# Trái phiếu, lãi suất và tín dụng

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trái phiếu, lãi suất và tín dụng**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Trái phiếu là hợp đồng cho vay** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Giá trái phiếu là giá trị hiện tại của dòng tiền** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối bonds với rates và credit, để đọc duration, spread và default risk trong cùng một đường truyền giá.

> Trái phiếu thường bị mô tả như “sản phẩm an toàn trả lãi cố định”. Cách hiểu đó quá đơn giản. Trái phiếu là một tập hợp dòng tiền theo hợp đồng chịu đồng thời rủi ro lãi suất, lạm phát, tín dụng, thanh khoản, quyền chọn và đôi khi cả tỷ giá. Chương này xây tư duy từ nguyên lý định giá tới đường cong lợi suất, chênh lệch tín dụng, các cấu trúc chứng khoán hóa và cách triển khai qua quỹ trái phiếu.

## 1. Trái phiếu là hợp đồng cho vay

Người nắm trái phiếu cho tổ chức phát hành vay vốn và nhận dòng tiền theo hợp đồng. Mệnh giá (face/par value) là khoản gốc tham chiếu; coupon là khoản lãi; ngày đáo hạn (maturity) là ngày hoàn trả gốc nếu không vỡ nợ.

Trái chủ khác cổ đông: trái chủ có quyền đòi theo hợp đồng và thường đứng cao hơn trong cấu trúc vốn, nhưng mức tăng giá trị kinh tế thường bị giới hạn hơn cổ phiếu.

> **Nối mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **2. Giá trái phiếu là giá trị hiện tại của dòng tiền** nối từ **1. Trái phiếu là hợp đồng cho vay** sang **3. Giá sạch và giá bẩn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Giá trái phiếu là giá trị hiện tại của dòng tiền

Trước khi học duration, spread hay các loại trái phiếu, cần đặt nền bằng câu hỏi: giá hôm nay là bao nhiêu khi các coupon và tiền gốc trong tương lai được chiết khấu về hiện tại? Công thức dưới đây trả lời câu hỏi đó.

```text
Bond Price = Σ Coupon_t / (1 + y)^t + Face Value / (1 + y)^T
```

Khi lợi suất yêu cầu tăng, giá trị hiện tại của dòng tiền cố định giảm; vì vậy giá và lợi suất thường đi ngược chiều.

Một trái phiếu chính phủ có thể giảm giá mạnh dù gần như không có rủi ro vỡ nợ vì lãi suất chiết khấu đã thay đổi.

> **Nối mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **3. Giá sạch và giá bẩn** nối từ **2. Giá trái phiếu là giá trị hiện tại của dòng tiền** sang **4. Coupon, hiện tại (current / 현재) yield và YTM khác nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Giá sạch và giá bẩn

Giá sạch (clean price) không bao gồm lãi dồn tích. Giá bẩn (dirty price) là số tiền thực tế gần với giá thanh toán:

```text
Dirty Price = Clean Price + Accrued Interest
```

Khi so báo giá và tính lợi suất, phải biết thị trường đang sử dụng loại giá nào.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **4. Coupon, hiện tại (current / 현재) yield và YTM khác nhau** nối từ **3. Giá sạch và giá bẩn** sang **5. Yield to lời gọi (call / 호출) và Yield to Worst**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Coupon, hiện tại (current / 현재) yield và YTM khác nhau

Coupon là lãi theo hợp đồng trên mệnh giá. Lợi suất hiện tại (current yield) gần bằng coupon năm chia giá thị trường. Lợi suất đến đáo hạn (Yield to Maturity, YTM) là tỷ lệ chiết khấu khiến giá trị hiện tại của dòng tiền bằng giá hiện tại với một số giả định.

YTM không phải lợi suất chắc chắn vì nhà đầu tư có thể bán trước đáo hạn, tổ chức phát hành có thể vỡ nợ hoặc dòng tiền phải tái đầu tư ở mức lãi khác.

> **Nối mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **5. Yield to lời gọi (call / 호출) và Yield to Worst** nối từ **4. Coupon, hiện tại (current / 현재) yield và YTM khác nhau** sang **6. Duration**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Yield to lời gọi (call / 호출) và Yield to Worst

Trái phiếu có quyền mua lại trước hạn (callable bond) cho phép tổ chức phát hành hoàn trả sớm theo điều khoản.

Khi lãi suất giảm, doanh nghiệp có động cơ tái cấp vốn rẻ hơn và mua lại trái phiếu coupon cao, làm hạn chế phần tăng giá của nhà đầu tư.

Vì vậy cần xem lợi suất tới ngày gọi lại (yield to call) và lợi suất xấu nhất (yield to worst), không chỉ YTM.

> **Nối mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **6. Duration** nối từ **5. Yield to lời gọi (call / 호출) và Yield to Worst** sang **7. DV01/PV01**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Duration

Duration đo thời điểm trung bình có trọng số của dòng tiền và độ nhạy của giá với lợi suất.

```text
%ΔPrice ≈ -Modified Duration × ΔYield
```

Trái phiếu kỳ hạn dài, coupon thấp và lợi suất thấp thường có duration cao hơn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **7. DV01/PV01** nối từ **6. Duration** sang **8. Convexity**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. DV01/PV01

DV01/PV01 đo mức thay đổi giá trị khi lợi suất dịch chuyển 1 điểm cơ bản.

Đây là thước đo tiền tệ trực tiếp hơn duration. Một danh mục có DV01 lớn có thể biến động đáng kể chỉ với thay đổi nhỏ của lãi suất.

> **Nối mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **8. Convexity** nối từ **7. DV01/PV01** sang **9. Effective Duration**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Convexity

Quan hệ giá–lợi suất là đường cong chứ không phải đường thẳng. Convexity đo độ cong này.

Với trái phiếu thông thường có convexity dương, mức tăng giá khi lợi suất giảm thường lớn hơn mức giảm khi lợi suất tăng cùng một độ lớn so với xấp xỉ tuyến tính.

Khi có quyền chọn nhúng, convexity có thể thay đổi mạnh.

> **Nối mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **9. Effective Duration** nối từ **8. Convexity** sang **10. Key-Rate Duration**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Effective Duration

Với trái phiếu có dòng tiền thay đổi theo lãi suất, như MBS hoặc callable bond, modified duration cố định có thể không đủ.

Duration hiệu dụng (effective duration) ước lượng độ nhạy sau khi cho phép dòng tiền thay đổi khi lãi suất thay đổi.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **10. Key-Rate Duration** nối từ **9. Effective Duration** sang **11. Đường cong lợi suất**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Key-Rate Duration

Đường cong lợi suất không luôn dịch chuyển song song. Lợi suất 2Y có thể tăng trong khi 10Y không đổi.

Duration theo điểm kỳ hạn (key-rate duration) phân rã độ nhạy theo các đoạn của đường cong. Hai danh mục cùng tổng duration vẫn có thể chịu rủi ro đường cong rất khác nhau.

> **Nối mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **11. Đường cong lợi suất** nối từ **10. Key-Rate Duration** sang **12. Steepening và Flattening**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Đường cong lợi suất

Đường cong nối lợi suất theo kỳ hạn. Đầu ngắn thường nhạy với lãi suất chính sách hiện tại và kỳ vọng. Đầu dài phản ánh đường đi lãi suất tương lai, tăng trưởng, lạm phát, nguồn cung trái phiếu và phần bù kỳ hạn.

```text
Long-term yield ≈ Expected future short rates + Term premium
```

> **Nối mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **12. Steepening và Flattening** nối từ **11. Đường cong lợi suất** sang **13. Đường cong đảo ngược**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Steepening và Flattening

Đường cong dốc hơn (steepening) chỉ nói chênh lệch dài–ngắn tăng, không nói nguyên nhân.

- **Bull steepener**: lợi suất ngắn giảm nhanh hơn dài, thường gắn với kỳ vọng hạ lãi suất hoặc suy thoái.
- **Bear steepener**: lợi suất dài tăng nhanh hơn, có thể do lạm phát, nguồn cung trái phiếu hoặc phần bù kỳ hạn.

Flattening cũng có phiên bản do lợi suất tăng hoặc giảm. Không nên học thuộc “steepening tốt, inversion xấu” mà không nhìn nguyên nhân.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **13. Đường cong đảo ngược** nối từ **12. Steepening và Flattening** sang **14. Lợi suất danh nghĩa, lợi suất thực và kỳ vọng lạm phát hòa vốn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Đường cong đảo ngược

Đường cong đảo ngược xảy ra khi lợi suất ngắn cao hơn lợi suất dài ở một số kỳ hạn. Nó thường phản ánh chính sách hiện tại chặt trong khi thị trường kỳ vọng lãi suất thấp hơn trong tương lai.

Đảo ngược có thông tin về chu kỳ nhưng không cho thời điểm chính xác. Đường cong có thể dốc trở lại vì hạ lãi suất trong suy thoái hoặc vì đầu dài tăng do lạm phát/tài khóa; hai trường hợp có tác động rất khác.

> **Nối mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **14. Lợi suất danh nghĩa, lợi suất thực và kỳ vọng lạm phát hòa vốn** nối từ **13. Đường cong đảo ngược** sang **15. Carry**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Lợi suất danh nghĩa, lợi suất thực và kỳ vọng lạm phát hòa vốn

Lợi suất danh nghĩa có thể được hiểu gần đúng là lợi suất thực cộng kỳ vọng lạm phát và các phần bù rủi ro.

Chênh lệch giữa Treasury danh nghĩa và TIPS cùng kỳ hạn thường được dùng làm kỳ vọng lạm phát hòa vốn (breakeven inflation), nhưng còn chứa phần bù rủi ro lạm phát và khác biệt thanh khoản.

Lợi suất thực đặc biệt quan trọng với vàng và cổ phiếu duration dài.

> **Nối mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **15. Carry** nối từ **14. Lợi suất danh nghĩa, lợi suất thực và kỳ vọng lạm phát hòa vốn** sang **16. Roll-Down**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Carry

Lợi suất nắm giữ (carry) là thu nhập mà vị thế tạo ra nếu các điều kiện khác không thay đổi, ví dụ coupon và ảnh hưởng của tài trợ.

Carry không phải lợi suất chắc chắn. Một khoản carry nhỏ có thể bị xóa bởi thay đổi lãi suất hoặc spread lớn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **16. Roll-Down** nối từ **15. Carry** sang **17. Trái phiếu chính phủ, doanh nghiệp và thứ tự ưu tiên**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Roll-Down

Nếu đường cong dốc và hình dạng không đổi, trái phiếu khi tiến gần đáo hạn có thể “trượt” xuống điểm có lợi suất thấp hơn, tạo lợi nhuận giá. Đây là lợi suất trượt theo đường cong (roll-down).

```text
Expected fixed-income return
≈ Carry + Roll-down + Rate move + Spread move + Default/Recovery + FX
```

> **Nối mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **17. Trái phiếu chính phủ, doanh nghiệp và thứ tự ưu tiên** nối từ **16. Roll-Down** sang **18. Chênh lệch tín dụng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Trái phiếu chính phủ, doanh nghiệp và thứ tự ưu tiên

Nợ chính phủ thường là mốc tham chiếu lãi suất trong đồng tiền tương ứng, nhưng rủi ro chính phủ vẫn phụ thuộc cấu trúc tài khóa/tiền tệ.

Nợ doanh nghiệp thêm rủi ro kinh doanh và vỡ nợ. Nợ có bảo đảm đứng cao hơn nợ không bảo đảm; nợ cao cấp đứng trên nợ thứ cấp.

Không so hai trái phiếu chỉ bằng lợi suất nếu thứ tự ưu tiên, tài sản bảo đảm, kỳ hạn và quyền chọn khác nhau.

> **Nối mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **18. Chênh lệch tín dụng** nối từ **17. Trái phiếu chính phủ, doanh nghiệp và thứ tự ưu tiên** sang **19. Z-Spread và OAS**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **19. Z-Spread và OAS** nối từ **18. Chênh lệch tín dụng** sang **20. Spread Duration**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Z-Spread và OAS

Z-spread là mức chênh lệch cố định cộng vào toàn bộ đường cong chuẩn để chiết khấu dòng tiền hợp đồng về đúng giá.

OAS (Option-Adjusted Spread) điều chỉnh thêm giá trị quyền chọn nhúng. Với trái phiếu callable hoặc MBS, OAS thường hữu ích hơn spread đơn giản vì tách một phần tác động của quyền chọn.

> **Nối mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **20. Spread Duration** nối từ **19. Z-Spread và OAS** sang **21. Rating không thay thế phân tích tín dụng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Spread Duration

Trái phiếu doanh nghiệp chịu cả duration lãi suất và duration chênh lệch tín dụng.

Treasury yield có thể giảm 100bp nhưng credit spread tăng 200bp, khiến trái phiếu doanh nghiệp vẫn giảm.

Đây là lý do high yield thường có hành vi gần cổ phiếu hơn trái phiếu chính phủ trong suy thoái.

> **Nối mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **21. Rating không thay thế phân tích tín dụng** nối từ **20. Spread Duration** sang **22. Thanh khoản của doanh nghiệp đi vay**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Rating không thay thế phân tích tín dụng

Xếp hạng tín dụng là đánh giá hữu ích nhưng có thể chậm hơn thị trường. Chênh lệch tín dụng thường phản ứng trước khi xếp hạng thay đổi.

Cần xem đòn bẩy, khả năng trả lãi, dòng tiền tự do, tính chu kỳ, giá trị tài sản, lịch đáo hạn và khả năng tiếp cận vốn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **22. Thanh khoản của doanh nghiệp đi vay** nối từ **21. Rating không thay thế phân tích tín dụng** sang **23. Bức tường đáo hạn**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **23. Bức tường đáo hạn** nối từ **22. Thanh khoản của doanh nghiệp đi vay** sang **24. Chu kỳ tín dụng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Bức tường đáo hạn

Nếu lượng lớn nợ đáo hạn tập trung trong 12–24 tháng, chi phí tái cấp vốn có thể tăng đột ngột ngay cả khi tỷ lệ nợ/EBITDA hiện tại chưa xấu.

Phải xem nợ cố định/thả nổi, có bảo đảm/không bảo đảm và lịch đáo hạn theo từng năm.

> **Nối mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **24. Chu kỳ tín dụng** nối từ **23. Bức tường đáo hạn** sang **25. Fallen Angels và Rising Stars**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **25. Fallen Angels và Rising Stars** nối từ **24. Chu kỳ tín dụng** sang **26. Khoản vay lãi suất thả nổi**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Fallen Angels và Rising Stars

Xếp hạng tín dụng thay đổi có thể tạo dòng lệnh kỹ thuật từ quỹ và chỉ số, đồng thời phản ánh thay đổi trong rủi ro tín dụng. Phần này nối sự kiện rating với giá, spread và thanh khoản chứ không chỉ với nhãn investment grade/high yield.

**Fallen angel** là tổ chức phát hành bị hạ từ investment grade xuống high yield. Việc bị loại khỏi chỉ số/quỹ có giới hạn xếp hạng có thể tạo bán kỹ thuật.

**Rising star** là tổ chức được nâng từ high yield lên investment grade. Dòng vốn kỹ thuật có thể đi hướng ngược lại.

Phân tích phải tách thay đổi chất lượng tín dụng thật khỏi dòng vốn do quy tắc chỉ số.

> **Nối mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **26. Khoản vay lãi suất thả nổi** nối từ **25. Fallen Angels và Rising Stars** sang **27. Leveraged Loans và Covenant**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Khoản vay lãi suất thả nổi

Công cụ lãi suất thả nổi có duration lãi suất thấp hơn nhưng người vay chịu chi phí lãi tăng nhanh khi benchmark tăng.

Nhà đầu tư giảm rủi ro giá do lãi suất nhưng có thể tăng rủi ro tín dụng gián tiếp vì khả năng trả lãi của người vay xấu đi.

> **Nối mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **27. Leveraged Loans và Covenant** nối từ **26. Khoản vay lãi suất thả nổi** sang **28. Trái phiếu liên kết lạm phát**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Leveraged Loans và Covenant

Khoản vay đòn bẩy (leveraged loan) thường cho doanh nghiệp có đòn bẩy cao. Điều khoản bảo vệ (covenant) có thể yêu cầu duy trì tỷ lệ tài chính hoặc giới hạn hành động.

Khoản vay covenant-lite cho người cho vay ít quyền can thiệp sớm hơn. Lợi suất cao phải được đọc cùng chất lượng điều khoản.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, sau nội dung của **27. Leveraged Loans và Covenant**, **28. Trái phiếu liên kết lạm phát** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **29. MBS và convexity âm** mở rộng hệ quả hoặc giới hạn liên quan.

## 28. Trái phiếu liên kết lạm phát

TIPS và các trái phiếu liên kết lạm phát điều chỉnh gốc hoặc dòng tiền theo chỉ số giá theo quy tắc.

Chúng bảo vệ sức mua tốt hơn trong một số tình huống nhưng vẫn chịu duration của lợi suất thực. Một năm CPI cao vẫn có thể tạo lỗ nếu lợi suất thực tăng mạnh.

> **Nối mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **29. MBS và convexity âm** nối từ **28. Trái phiếu liên kết lạm phát** sang **30. ABS và phân tầng rủi ro**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. MBS và convexity âm

Chứng khoán bảo đảm bằng khoản vay thế chấp (MBS) nhận dòng tiền từ các khoản vay mua nhà. Người vay có quyền trả trước.

Khi lãi suất giảm, tái cấp vốn tăng và nhà đầu tư nhận lại tiền sớm đúng lúc muốn giữ coupon cao. Khi lãi suất tăng, trả trước chậm và duration kéo dài.

Đây là trực giác của convexity âm.

> **Nối mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **30. ABS và phân tầng rủi ro** nối từ **29. MBS và convexity âm** sang **31. Trái phiếu chính phủ nội tệ và ngoại tệ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. ABS và phân tầng rủi ro

Chứng khoán bảo đảm bằng tài sản (ABS) gom dòng tiền từ các khoản vay/tài sản rồi chia thành các tầng (tranche) có thứ tự nhận tiền và chịu lỗ khác nhau.

Một pool tài sản tương đối ổn định vẫn có thể tạo tranche rủi ro cao nếu cấu trúc phân bổ lỗ phức tạp. Cần hiểu waterfall, credit enhancement và trigger.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **31. Trái phiếu chính phủ nội tệ và ngoại tệ** nối từ **30. ABS và phân tầng rủi ro** sang **32. ETF trái phiếu không giống trái phiếu riêng lẻ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. Trái phiếu chính phủ nội tệ và ngoại tệ

Chính phủ vay bằng đồng tiền mình kiểm soát có rủi ro khác chính phủ vay bằng ngoại tệ.

Nợ nội tệ có thể giảm rủi ro vỡ nợ danh nghĩa nhưng vẫn có rủi ro lạm phát và mất giá tiền tệ. Nợ ngoại tệ phụ thuộc dự trữ ngoại hối, cán cân thanh toán và khả năng tiếp cận thị trường quốc tế.

> **Nối mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **32. ETF trái phiếu không giống trái phiếu riêng lẻ** nối từ **31. Trái phiếu chính phủ nội tệ và ngoại tệ** sang **33. Thanh khoản ETF trái phiếu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. ETF trái phiếu không giống trái phiếu riêng lẻ

Trái phiếu riêng lẻ giữ tới đáo hạn có kỳ hạn còn lại giảm dần. ETF trái phiếu thông thường liên tục thay trái phiếu để duy trì vùng kỳ hạn mục tiêu.

Vì vậy “giữ ETF trái phiếu tới đáo hạn” thường là mô hình sai, trừ các quỹ mục tiêu đáo hạn có cấu trúc đặc biệt.

> **Nối mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **33. Thanh khoản ETF trái phiếu** nối từ **32. ETF trái phiếu không giống trái phiếu riêng lẻ** sang **34. Thang đáo hạn, bullet và barbell**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. Thanh khoản ETF trái phiếu

ETF có thể giao dịch thường xuyên dù trái phiếu cơ sở OTC và ít thanh khoản. Trong khủng hoảng, giá ETF có thể lệch NAV do NAV dùng báo giá cũ trong khi ETF đang khám phá giá nhanh hơn.

Cần xem spread, AUM, chất lượng tài sản, duration và thanh khoản tài sản cơ sở.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **34. Thang đáo hạn, bullet và barbell** nối từ **33. Thanh khoản ETF trái phiếu** sang **35. Immunization và liability matching**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Thang đáo hạn, bullet và barbell

Sau khi hiểu duration và đường cong, ta chuyển sang cách sắp xếp các ngày đáo hạn để đáp ứng nghĩa vụ và kiểm soát tái đầu tư. Ba cấu trúc dưới đây khác nhau ở dòng tiền, độ nhạy và rủi ro tập trung thời điểm.

**Bond ladder** trải kỳ hạn để tạo dòng tiền gốc đều.

**Bullet** tập trung kỳ hạn quanh một mốc để khớp nghĩa vụ.

**Barbell** kết hợp kỳ hạn ngắn và dài thay vì tập trung ở giữa.

Hai danh mục có cùng duration tổng nhưng khác cấu trúc đường cong và rủi ro tái đầu tư.

> **Nối mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **35. Immunization và liability matching** nối từ **34. Thang đáo hạn, bullet và barbell** sang **36. Phòng vệ lãi suất**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. Immunization và liability matching

Immunization cố gắng khớp duration/convexity của tài sản với nghĩa vụ để giảm nhạy với thay đổi lãi suất.

Đây là tư duy khác với “mua trái phiếu vì nghĩ lãi suất sẽ giảm”. Mục tiêu là bảo vệ khả năng thanh toán nghĩa vụ.

> **Nối mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **36. Phòng vệ lãi suất** nối từ **35. Immunization và liability matching** sang **37. Phòng vệ tín dụng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. Phòng vệ lãi suất

Có thể dùng futures hoặc swap để điều chỉnh DV01 mà không bán toàn bộ trái phiếu.

Phòng vệ tốt cần khớp độ nhạy theo đường cong, không chỉ giá trị danh nghĩa. Curve twist có thể làm hedge một điểm kỳ hạn không hoàn hảo.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **37. Phòng vệ tín dụng** nối từ **36. Phòng vệ lãi suất** sang **38. Khi long-duration bond đa dạng hóa cổ phiếu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 37. Phòng vệ tín dụng

CDS hoặc chỉ số tín dụng có thể giảm rủi ro spread/default, nhưng thêm rủi ro đối tác, basis và cấu trúc hợp đồng.

Một hedge tín dụng không loại bỏ rủi ro thanh khoản của trái phiếu cơ sở.

> **Nối mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **38. Khi long-duration bond đa dạng hóa cổ phiếu** nối từ **37. Phòng vệ tín dụng** sang **39. Phân rã lợi suất thu nhập cố định**, vì cơ chế trước tạo đầu vào cho bước sau.

## 38. Khi long-duration bond đa dạng hóa cổ phiếu

Trái phiếu chính phủ dài hạn thường hữu ích trong suy thoái do cầu yếu và giảm phát, khi lợi suất có xu hướng giảm.

Trong cú sốc lạm phát, cổ phiếu và trái phiếu dài hạn có thể cùng giảm. Tương quan cổ phiếu–trái phiếu phụ thuộc chế độ kinh tế.

> **Nối mạch:** Ở chặng này của **Trái phiếu, lãi suất và tín dụng**, **39. Phân rã lợi suất thu nhập cố định** nối từ **38. Khi long-duration bond đa dạng hóa cổ phiếu** sang **40. Checklist trái phiếu hoặc ETF trái phiếu**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trái phiếu, lãi suất và tín dụng**, **40. Checklist trái phiếu hoặc ETF trái phiếu** nối từ **39. Phân rã lợi suất thu nhập cố định** sang **Kết luận**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Trái phiếu, lãi suất và tín dụng**, **Kết luận** tổng hợp từ **40. Checklist trái phiếu hoặc ETF trái phiếu** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Kết luận

Lợi suất trái phiếu không thể rút gọn thành “nhận coupon”. Cần tách **thu nhập, lãi suất, đường cong, tín dụng, quyền chọn, thanh khoản, vỡ nợ, thu hồi và tỷ giá**. Chỉ khi hiểu từng thành phần, nhà đầu tư mới biết trái phiếu đang đóng vai trò phòng thủ, tạo thu nhập hay thực chất là một khoản cược vào duration hoặc tín dụng.

> **Bàn giao:** Sau **Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
