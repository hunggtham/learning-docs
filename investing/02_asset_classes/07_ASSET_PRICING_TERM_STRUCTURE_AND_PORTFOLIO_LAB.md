# Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Mọi tài sản đều là một tập hợp dòng tiền và điều kiện** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Lợi suất kỳ vọng nên được phân rã** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối asset pricing với term structure và portfolio lab, để mô hình giá được kiểm tra qua duration, risk premium và quyết định phân bổ.

> Mục tiêu của tệp (file / 파일) này là nối các nhóm tài sản thành một hệ thống so sánh thống nhất. Thay vì hỏi “cổ phiếu hay trái phiếu tốt hơn?”, người đọc sẽ học cách phân rã **nguồn lợi suất → rủi ro định giá → thanh khoản → cấu trúc kỳ hạn → biến số vĩ mô chi phối → vai trò trong danh mục**.

## 1. Mọi tài sản đều là một tập hợp dòng tiền và điều kiện

Cổ phiếu, trái phiếu, REIT, vàng, hàng hóa hay sản phẩm cấu trúc nhìn bề ngoài rất khác nhau, nhưng về tư duy có thể đưa về ba câu hỏi:

```text
Tôi nhận được dòng tiền hoặc lợi ích kinh tế nào?
Rủi ro nào làm dòng tiền hoặc tỷ lệ chiết khấu thay đổi?
Tôi có thể thoát vị thế với chi phí nào khi cần?
```

Một tài sản có dòng tiền ổn định nhưng quá đắt vẫn có lợi suất kỳ vọng thấp. Một tài sản rẻ nhưng thanh khoản kém hoặc cấu trúc pháp lý yếu vẫn có thể không phù hợp với mục tiêu.

> **Chuyển mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **2. Lợi suất kỳ vọng nên được phân rã** tiếp nhận điểm tựa từ **1. Mọi tài sản đều là một tập hợp dòng tiền và điều kiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Phân biệt lợi suất từ dòng tiền và lợi suất từ định giá** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Lợi suất kỳ vọng nên được phân rã

Thay vì dùng một con số duy nhất, hãy tách:

```text
Lợi suất kỳ vọng
≈ Thu nhập hiện tại
+ Tăng trưởng cơ bản
+ Thay đổi định giá
+ Lợi ích tái cân bằng / cấu trúc
- Chi phí
- Tổn thất kỳ vọng
```

Với cổ phiếu, thu nhập hiện tại có thể là cổ tức và mua lại ròng. Với trái phiếu là coupon và lợi suất nắm giữ. Với bất động sản là tiền thuê. Với hàng hóa, lợi suất hợp đồng tương lai còn phụ thuộc cấu trúc đường cong và tài sản bảo đảm.

> **Chuyển mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **3. Phân biệt lợi suất từ dòng tiền và lợi suất từ định giá** tiếp nhận điểm tựa từ **2. Lợi suất kỳ vọng nên được phân rã** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Duration là một ngôn ngữ chung** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Phân biệt lợi suất từ dòng tiền và lợi suất từ định giá

Một tài sản có thể tăng giá vì hai lý do hoàn toàn khác:

```text
Dòng tiền / lợi nhuận cơ bản tăng
hoặc
nhà đầu tư chấp nhận trả mức định giá cao hơn
```

Nếu giá tăng chủ yếu do hệ số định giá mở rộng, phần lợi suất đó khó lặp lại mãi. Đây là lý do phải tách **tăng trưởng cơ bản** khỏi **mở rộng bội số (multiple expansion)**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **4. Duration là một ngôn ngữ chung** tiếp nhận điểm tựa từ **3. Phân biệt lợi suất từ dòng tiền và lợi suất từ định giá** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Đường cong lợi suất chứa thông tin về giá của thời gian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Duration là một ngôn ngữ chung

Duration không chỉ thuộc trái phiếu. Nó là trực giác về độ xa của dòng tiền.

- trái phiếu dài hạn: duration cao;
- cổ phiếu tăng trưởng có dòng tiền xa: duration kinh tế cao;
- REIT có hợp đồng dài: duration dòng tiền khác tài sản ngắn hạn;
- vàng không có dòng tiền nhưng nhạy với lợi suất thực qua chi phí cơ hội.

Nhờ vậy có thể hiểu vì sao nhiều tài sản “khác tên” vẫn cùng giảm khi lợi suất thực tăng mạnh.

> **Chuyển mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **5. Đường cong lợi suất chứa thông tin về giá của thời gian** tiếp nhận điểm tựa từ **4. Duration là một ngôn ngữ chung** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Carry và roll-down phải đọc cùng rủi ro** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Đường cong lợi suất chứa thông tin về giá của thời gian

Đường cong lợi suất không chỉ là danh sách lãi suất. Nó phản ánh:

```text
Kỳ vọng lãi suất ngắn hạn tương lai
+ phần bù kỳ hạn
+ cung cầu trái phiếu
+ thanh khoản
+ rủi ro lạm phát
```

Hai trái phiếu cùng YTM nhưng khác vị trí trên đường cong có thể có triển vọng khác nếu một trái phiếu được hưởng lợi từ trượt theo đường cong (roll-down) còn trái phiếu kia không.

> **Chuyển mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **6. Carry và roll-down phải đọc cùng rủi ro** tiếp nhận điểm tựa từ **5. Đường cong lợi suất chứa thông tin về giá của thời gian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Lợi suất trái phiếu là tổng của nhiều thành phần** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Carry và roll-down phải đọc cùng rủi ro

Lợi suất nắm giữ (carry) cao không tự động tốt. Nó có thể là phần bù cho rủi ro thật.

Ví dụ:

```text
High-yield spread cao
→ carry hấp dẫn
NHƯNG
→ xác suất vỡ nợ / suy giảm tín dụng cao hơn
```

Một chiến lược “ăn carry” chỉ hợp lý nếu phần bù nhận được đủ lớn so với tổn thất trong các trạng thái xấu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **7. Lợi suất trái phiếu là tổng của nhiều thành phần** tiếp nhận điểm tựa từ **6. Carry và roll-down phải đọc cùng rủi ro** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Cổ phiếu là tài sản có dòng tiền tăng trưởng nhưng bất định** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Lợi suất trái phiếu là tổng của nhiều thành phần

Một khung thực hành:

```text
Lợi suất trái phiếu kỳ vọng
≈ Coupon / carry
+ Roll-down
+ Biến động lợi suất phi rủi ro
+ Biến động chênh lệch tín dụng
+ Tổn thất vỡ nợ / thu hồi
+ FX nếu có
```

Phân rã này giúp tránh sai lầm kiểu “lãi suất giảm thì mọi trái phiếu đều tăng”. Nếu chênh lệch tín dụng mở rộng mạnh, trái phiếu doanh nghiệp vẫn có thể giảm.

> **Chuyển mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **8. Cổ phiếu là tài sản có dòng tiền tăng trưởng nhưng bất định** tiếp nhận điểm tựa từ **7. Lợi suất trái phiếu là tổng của nhiều thành phần** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. ETF là lớp bao chứ không phải loại tài sản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Cổ phiếu là tài sản có dòng tiền tăng trưởng nhưng bất định

Một mô hình trực giác:

```text
Lợi suất cổ phiếu
≈ Tăng trưởng EPS/FCF trên mỗi cổ phiếu
+ Lợi suất cổ tức / mua lại
+ Thay đổi bội số định giá
```

Tăng trưởng doanh thu không đủ. Phải xét pha loãng, biên lợi nhuận, tái đầu tư và ROIC tăng thêm.

> **Chuyển mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **9. ETF là lớp bao chứ không phải loại tài sản** tiếp nhận điểm tựa từ **8. Cổ phiếu là tài sản có dòng tiền tăng trưởng nhưng bất định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Sai lệch bám chỉ số là kết quả, không chỉ là phí quản lý** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. ETF là lớp bao chứ không phải loại tài sản

ETF chỉ là cấu trúc sở hữu. Một ETF có thể chứa:

```text
Cổ phiếu
Trái phiếu
Hàng hóa
Hợp đồng tương lai
Hoán đổi
Chiến lược quyền chọn
```

Vì vậy phân tích phải nhìn xuyên qua lớp bao (look-through) tới tài sản và rủi ro cơ sở.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **10. Sai lệch bám chỉ số là kết quả, không chỉ là phí quản lý** tiếp nhận điểm tựa từ **9. ETF là lớp bao chứ không phải loại tài sản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Bất động sản phải tách tài sản và cấu trúc tài trợ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Sai lệch bám chỉ số là kết quả, không chỉ là phí quản lý

Sai lệch lợi suất so với chỉ số có thể đến từ:

```text
Phí
Thuế
Tiền mặt
Tái cân bằng
Tối ưu hóa mẫu
Cho vay chứng khoán
Chi phí phòng vệ FX
Chênh lệch thời điểm định giá
```

Do đó quỹ có phí thấp hơn chưa chắc có hiệu quả bám chỉ số tốt hơn sau mọi chi phí.

> **Chuyển mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **11. Bất động sản phải tách tài sản và cấu trúc tài trợ** tiếp nhận điểm tựa từ **10. Sai lệch bám chỉ số là kết quả, không chỉ là phí quản lý** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Vàng là tài sản không có dòng tiền** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Bất động sản phải tách tài sản và cấu trúc tài trợ

Một tài sản bất động sản có thể tốt nhưng phần vốn chủ sở hữu vẫn rủi ro nếu dùng quá nhiều nợ.

Khung cơ bản:

```text
Doanh thu thuê
- Chi phí vận hành
= NOI

NOI / Giá trị tài sản
≈ Cap rate
```

Sau đó mới xét:

```text
LTV
DSCR
Lãi vay
Kỳ hạn nợ
Chi phí bảo trì
Capex
```

Đòn bẩy làm vốn chủ sở hữu nhạy hơn nhiều với thay đổi cap tỷ lệ (rate / 비율) và NOI.

> **Chuyển mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **12. Vàng là tài sản không có dòng tiền** tiếp nhận điểm tựa từ **11. Bất động sản phải tách tài sản và cấu trúc tài trợ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Hàng hóa là bài toán dòng vật chất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Vàng là tài sản không có dòng tiền

Do không tạo coupon hay FCF, vàng phải được hiểu qua:

```text
Lợi suất thực
USD
Niềm tin vào tiền tệ / hệ thống
Nhu cầu dự trữ
Địa chính trị
Dòng vốn đầu tư
```

Nếu lợi suất thực tăng mạnh và USD mạnh, chi phí cơ hội giữ vàng thường tăng. Nhưng trong khủng hoảng niềm tin hoặc rủi ro hệ thống, hành vi có thể khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **13. Hàng hóa là bài toán dòng vật chất** tiếp nhận điểm tựa từ **12. Vàng là tài sản không có dòng tiền** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Tài sản tư nhân có vấn đề đo lường riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Hàng hóa là bài toán dòng vật chất

Giá hàng hóa chịu:

```text
Sản lượng
Tồn kho
Công suất dự phòng
Chi phí biên
Nhu cầu cuối
Logistics
Thời tiết / địa chính trị
```

Với hợp đồng tương lai còn phải xét contango/backwardation và lợi suất chuyển kỳ.

Đầu tư vào ETF hàng hóa không đồng nghĩa trực tiếp sở hữu giá giao ngay.

> **Chuyển mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **13. Hàng hóa là bài toán dòng vật chất** nêu điều cần giải thích; **14. Tài sản tư nhân có vấn đề đo lường riêng** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **15. So sánh IRR với PME** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Tài sản tư nhân có vấn đề đo lường riêng

Private equity, private credit hay bất động sản tư nhân thường được định giá không liên tục. NAV ít dao động không có nghĩa rủi ro kinh tế thấp.

Cần điều chỉnh tư duy cho:

```text
Độ trễ định giá
Khó thoát vốn
Cam kết vốn chưa gọi
Đòn bẩy ở cấp quỹ / tài sản
Phí nhiều tầng
IRR nhạy thời điểm dòng tiền
```

> **Chuyển mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **14. Tài sản tư nhân có vấn đề đo lường riêng** đã nêu tiêu chí phân biệt, còn **15. So sánh IRR với PME** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **16. Sản phẩm cấu trúc phải được giải cấu trúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. So sánh IRR với PME

IRR có thể cao vì dòng tiền hoàn vốn sớm hoặc dùng subscription line. Để so với thị trường công khai, có thể dùng **tương đương thị trường công khai (public market equivalent, PME)**.

Mục tiêu là hỏi: nếu cùng dòng tiền được đầu tư vào benchmark công khai, kết quả tương đối ra sao?

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **15. So sánh IRR với PME** đã nêu tiêu chí phân biệt, còn **16. Sản phẩm cấu trúc phải được giải cấu trúc** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **17. Tương quan không phải đặc tính cố định** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Sản phẩm cấu trúc phải được giải cấu trúc

Một sản phẩm có coupon cao nên được tách thành:

```text
Khoản nợ của nhà phát hành
+ quyền chọn người mua đang bán / mua
+ rủi ro thanh khoản
+ phí cấu trúc
```

Nếu không thể vẽ payoff theo giá tài sản cơ sở, chưa thể đánh giá đúng rủi ro.

> **Chuyển mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **17. Tương quan không phải đặc tính cố định** tiếp nhận điểm tựa từ **16. Sản phẩm cấu trúc phải được giải cấu trúc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Ma trận tăng trưởng–lạm phát** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Tương quan không phải đặc tính cố định

Cổ phiếu–trái phiếu có thể tương quan âm trong suy thoái giảm phát nhưng tương quan dương trong cú sốc lạm phát.

Vì vậy vai trò của tài sản trong danh mục phải được đánh giá theo **chế độ kinh tế (regime)**.

> **Chuyển mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **18. Ma trận tăng trưởng–lạm phát** tiếp nhận điểm tựa từ **17. Tương quan không phải đặc tính cố định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Lợi suất kỳ vọng phải được chuẩn hóa theo rủi ro** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Ma trận tăng trưởng–lạm phát

Một ma trận đơn giản:

```text
Tăng trưởng ↑ / Lạm phát ↓  → môi trường thuận lợi cho nhiều tài sản rủi ro
Tăng trưởng ↑ / Lạm phát ↑  → tài sản chu kỳ / hàng hóa có thể nổi bật
Tăng trưởng ↓ / Lạm phát ↓  → trái phiếu chính phủ thường hữu ích hơn
Tăng trưởng ↓ / Lạm phát ↑  → môi trường khó, đa dạng hóa truyền thống suy yếu
```

Đây là điểm xuất phát, không phải quy luật máy móc. Định giá và chính sách ban đầu vẫn quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **19. Lợi suất kỳ vọng phải được chuẩn hóa theo rủi ro** tiếp nhận điểm tựa từ **18. Ma trận tăng trưởng–lạm phát** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Định giá tương đối và tuyệt đối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Lợi suất kỳ vọng phải được chuẩn hóa theo rủi ro

Không nên so 8% của trái phiếu với 10% của cổ phiếu chỉ bằng con số.

Cần hỏi:

```text
Độ biến động?
Mức suy giảm?
Thanh khoản?
Rủi ro đuôi?
Rủi ro tiền tệ?
Khả năng vỡ nợ?
Khả năng tái đầu tư?
```

Một tài sản có lợi suất danh nghĩa cao nhưng xác suất mất vốn lớn có thể có lợi suất điều chỉnh rủi ro kém hơn.

> **Chuyển mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **20. Định giá tương đối và tuyệt đối** tiếp nhận điểm tựa từ **19. Lợi suất kỳ vọng phải được chuẩn hóa theo rủi ro** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Phần bù rủi ro cổ phiếu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Định giá tương đối và tuyệt đối

Sau khi đánh giá lợi suất và rủi ro, ta cần hỏi giá hiện tại đang được so với dòng tiền của chính tài sản hay với cơ hội thay thế. Hai góc nhìn bổ sung cho nhau và giúp đặt earnings yield trong bối cảnh lãi suất thực, tăng trưởng và rủi ro.

**Định giá tuyệt đối** hỏi giá hiện tại so với dòng tiền tương lai của chính tài sản.

**Định giá tương đối** hỏi tài sản rẻ hay đắt so với tài sản thay thế.

Ví dụ cổ phiếu có earnings yield 5% không thể đánh giá tách khỏi lợi suất trái phiếu thực và rủi ro tăng trưởng.

> **Chuyển mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **21. Phần bù rủi ro cổ phiếu** tiếp nhận điểm tựa từ **20. Định giá tương đối và tuyệt đối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Thanh khoản là một phần của định giá** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Phần bù rủi ro cổ phiếu

Một cách trực giác:

```text
Lợi suất kỳ vọng cổ phiếu
- lợi suất tài sản ít rủi ro
= phần bù rủi ro cổ phiếu kỳ vọng
```

Nếu lợi suất trái phiếu tăng trong khi định giá cổ phiếu không đổi, phần bù tương đối có thể co lại và áp lực lên bội số tăng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **22. Thanh khoản là một phần của định giá** tiếp nhận điểm tựa từ **21. Phần bù rủi ro cổ phiếu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Kiểm thử vai trò của tài sản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Thanh khoản là một phần của định giá

Hai tài sản có dòng tiền giống nhau nhưng tài sản khó bán thường cần phần bù cao hơn.

Trong bình thường, chênh lệch này có thể nhỏ. Trong căng thẳng, spread và tác động thị trường tăng rất nhanh. Vì vậy thanh khoản phải được đưa vào lợi suất kỳ vọng và quy mô vị thế.

> **Chuyển mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **23. Kiểm thử vai trò của tài sản** tiếp nhận điểm tựa từ **22. Thanh khoản là một phần của định giá** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Bài tập so sánh bốn tài sản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Kiểm thử vai trò của tài sản

Với mỗi tài sản trong danh mục, viết một dòng:

```text
Vai trò chính:
Tăng trưởng / phòng thủ / thanh khoản / lạm phát / đa dạng hóa / chiến thuật
```

Sau đó hỏi:

```text
Trong trạng thái nào vai trò này thất bại?
```

Ví dụ trái phiếu dài hạn là phòng thủ trước suy thoái giảm phát nhưng có thể thất bại trong cú sốc lạm phát.

> **Chuyển mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **23. Kiểm thử vai trò của tài sản** đã nêu tiêu chí phân biệt, còn **24. Bài tập so sánh bốn tài sản** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **25. Liên kết đọc tiếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Bài tập so sánh bốn tài sản

Chọn:

```text
ETF cổ phiếu toàn cầu
ETF trái phiếu chính phủ dài hạn
Vàng
REIT
```

Với mỗi tài sản, ghi:

1. nguồn lợi suất;
2. biến số vĩ mô chi phối;
3. duration kinh tế;
4. rủi ro thanh khoản;
5. rủi ro tiền tệ;
6. trạng thái tốt nhất;
7. trạng thái xấu nhất;
8. vai trò trong danh mục.

Sau đó kiểm tra xem bốn tài sản có thật sự đa dạng hóa hay chỉ cùng phụ thuộc một vài biến.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **24. Bài tập so sánh bốn tài sản** đã nêu tiêu chí phân biệt, còn **25. Liên kết đọc tiếp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Kết luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Liên kết đọc tiếp

Các tài liệu sau mở rộng từng nhóm tài sản và cách chúng kết hợp trong danh mục. Hãy chọn liên kết tương ứng với biến rủi ro còn chưa rõ sau bài lab, rồi quay lại kiểm tra giả định ban đầu.

- [Cổ phiếu, ETF và quỹ](./01_STOCKS_ETF_AND_FUNDS.md)
- [Trái phiếu, lãi suất và tín dụng](./02_BONDS_RATES_AND_CREDIT.md)
- [Tài sản thực và thay thế](./03_REAL_ASSETS_AND_ALTERNATIVES.md)
- [Nhân tố, chỉ số và hành vi đa tài sản](./04_FACTORS_INDEXING_AND_MULTI_ASSET_BEHAVIOR.md)
- [Danh mục đa tài sản và phòng vệ](./05_MULTI_ASSET_HEDGING_CURRENCY_AND_REGIME_ALLOCATION.md)

> **Chuyển mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **Kết luận** gom các mảnh từ **25. Liên kết đọc tiếp** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết luận

Một nhóm tài sản không nên được đánh giá bằng tên sản phẩm hay lợi suất quá khứ. Khung sâu hơn là:

```text
Dòng tiền / lợi ích kinh tế
→ nguồn lợi suất
→ tỷ lệ chiết khấu
→ cấu trúc kỳ hạn
→ thanh khoản
→ chế độ kinh tế
→ tương quan với phần còn lại
→ vai trò trong danh mục
```

Khi dùng chung khung này, người đọc có thể so sánh những tài sản rất khác nhau mà không rơi vào bẫy “tài sản nào tăng nhiều nhất gần đây”.

> **Bàn giao:** Sau **Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
