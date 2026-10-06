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

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **2. Lợi suất kỳ vọng nên được phân rã** nối từ **1. Mọi tài sản đều là một tập hợp dòng tiền và điều kiện** sang **3. Phân biệt lợi suất từ dòng tiền và lợi suất từ định giá**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **3. Phân biệt lợi suất từ dòng tiền và lợi suất từ định giá** nối từ **2. Lợi suất kỳ vọng nên được phân rã** sang **4. Duration là một ngôn ngữ chung**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Phân biệt lợi suất từ dòng tiền và lợi suất từ định giá

Một tài sản có thể tăng giá vì hai lý do hoàn toàn khác:

```text
Dòng tiền / lợi nhuận cơ bản tăng
hoặc
nhà đầu tư chấp nhận trả mức định giá cao hơn
```

Nếu giá tăng chủ yếu do hệ số định giá mở rộng, phần lợi suất đó khó lặp lại mãi. Đây là lý do phải tách **tăng trưởng cơ bản** khỏi **mở rộng bội số (multiple expansion)**.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **4. Duration là một ngôn ngữ chung** nối từ **3. Phân biệt lợi suất từ dòng tiền và lợi suất từ định giá** sang **5. Đường cong lợi suất chứa thông tin về giá của thời gian**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Duration là một ngôn ngữ chung

Duration không chỉ thuộc trái phiếu. Nó là trực giác về độ xa của dòng tiền.

- trái phiếu dài hạn: duration cao;
- cổ phiếu tăng trưởng có dòng tiền xa: duration kinh tế cao;
- REIT có hợp đồng dài: duration dòng tiền khác tài sản ngắn hạn;
- vàng không có dòng tiền nhưng nhạy với lợi suất thực qua chi phí cơ hội.

Nhờ vậy có thể hiểu vì sao nhiều tài sản “khác tên” vẫn cùng giảm khi lợi suất thực tăng mạnh.

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **5. Đường cong lợi suất chứa thông tin về giá của thời gian** nối từ **4. Duration là một ngôn ngữ chung** sang **6. Carry và roll-down phải đọc cùng rủi ro**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **6. Carry và roll-down phải đọc cùng rủi ro** nối từ **5. Đường cong lợi suất chứa thông tin về giá của thời gian** sang **7. Lợi suất trái phiếu là tổng của nhiều thành phần**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **7. Lợi suất trái phiếu là tổng của nhiều thành phần** nối từ **6. Carry và roll-down phải đọc cùng rủi ro** sang **8. Cổ phiếu là tài sản có dòng tiền tăng trưởng nhưng bất định**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **8. Cổ phiếu là tài sản có dòng tiền tăng trưởng nhưng bất định** nối từ **7. Lợi suất trái phiếu là tổng của nhiều thành phần** sang **9. ETF là lớp bao chứ không phải loại tài sản**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Cổ phiếu là tài sản có dòng tiền tăng trưởng nhưng bất định

Một mô hình trực giác:

```text
Lợi suất cổ phiếu
≈ Tăng trưởng EPS/FCF trên mỗi cổ phiếu
+ Lợi suất cổ tức / mua lại
+ Thay đổi bội số định giá
```

Tăng trưởng doanh thu không đủ. Phải xét pha loãng, biên lợi nhuận, tái đầu tư và ROIC tăng thêm.

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **9. ETF là lớp bao chứ không phải loại tài sản** nối từ **8. Cổ phiếu là tài sản có dòng tiền tăng trưởng nhưng bất định** sang **10. Sai lệch bám chỉ số là kết quả, không chỉ là phí quản lý**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **10. Sai lệch bám chỉ số là kết quả, không chỉ là phí quản lý** nối từ **9. ETF là lớp bao chứ không phải loại tài sản** sang **11. Bất động sản phải tách tài sản và cấu trúc tài trợ**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **11. Bất động sản phải tách tài sản và cấu trúc tài trợ** nối từ **10. Sai lệch bám chỉ số là kết quả, không chỉ là phí quản lý** sang **12. Vàng là tài sản không có dòng tiền**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **12. Vàng là tài sản không có dòng tiền** nối từ **11. Bất động sản phải tách tài sản và cấu trúc tài trợ** sang **13. Hàng hóa là bài toán dòng vật chất**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **13. Hàng hóa là bài toán dòng vật chất** nối từ **12. Vàng là tài sản không có dòng tiền** sang **14. Tài sản tư nhân có vấn đề đo lường riêng**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **13. Hàng hóa là bài toán dòng vật chất** đặt vấn đề; **14. Tài sản tư nhân có vấn đề đo lường riêng** đối chiếu bằng chứng, rồi **15. So sánh IRR với PME** mở rộng hệ quả hoặc giới hạn liên quan.

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

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **14. Tài sản tư nhân có vấn đề đo lường riêng** đặt tiêu chí; **15. So sánh IRR với PME** dùng tiêu chí đó để kiểm tra ranh giới, rồi **16. Sản phẩm cấu trúc phải được giải cấu trúc** mở rộng hệ quả.

## 15. So sánh IRR với PME

IRR có thể cao vì dòng tiền hoàn vốn sớm hoặc dùng subscription line. Để so với thị trường công khai, có thể dùng **tương đương thị trường công khai (public market equivalent, PME)**.

Mục tiêu là hỏi: nếu cùng dòng tiền được đầu tư vào benchmark công khai, kết quả tương đối ra sao?

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **15. So sánh IRR với PME** đặt tiêu chí; **16. Sản phẩm cấu trúc phải được giải cấu trúc** dùng tiêu chí đó để kiểm tra ranh giới, rồi **17. Tương quan không phải đặc tính cố định** mở rộng hệ quả.

## 16. Sản phẩm cấu trúc phải được giải cấu trúc

Một sản phẩm có coupon cao nên được tách thành:

```text
Khoản nợ của nhà phát hành
+ quyền chọn người mua đang bán / mua
+ rủi ro thanh khoản
+ phí cấu trúc
```

Nếu không thể vẽ payoff theo giá tài sản cơ sở, chưa thể đánh giá đúng rủi ro.

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **17. Tương quan không phải đặc tính cố định** nối từ **16. Sản phẩm cấu trúc phải được giải cấu trúc** sang **18. Ma trận tăng trưởng–lạm phát**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Tương quan không phải đặc tính cố định

Cổ phiếu–trái phiếu có thể tương quan âm trong suy thoái giảm phát nhưng tương quan dương trong cú sốc lạm phát.

Vì vậy vai trò của tài sản trong danh mục phải được đánh giá theo **chế độ kinh tế (regime)**.

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **18. Ma trận tăng trưởng–lạm phát** nối từ **17. Tương quan không phải đặc tính cố định** sang **19. Lợi suất kỳ vọng phải được chuẩn hóa theo rủi ro**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Ma trận tăng trưởng–lạm phát

Một ma trận đơn giản:

```text
Tăng trưởng ↑ / Lạm phát ↓  → môi trường thuận lợi cho nhiều tài sản rủi ro
Tăng trưởng ↑ / Lạm phát ↑  → tài sản chu kỳ / hàng hóa có thể nổi bật
Tăng trưởng ↓ / Lạm phát ↓  → trái phiếu chính phủ thường hữu ích hơn
Tăng trưởng ↓ / Lạm phát ↑  → môi trường khó, đa dạng hóa truyền thống suy yếu
```

Đây là điểm xuất phát, không phải quy luật máy móc. Định giá và chính sách ban đầu vẫn quan trọng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **19. Lợi suất kỳ vọng phải được chuẩn hóa theo rủi ro** nối từ **18. Ma trận tăng trưởng–lạm phát** sang **20. Định giá tương đối và tuyệt đối**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **20. Định giá tương đối và tuyệt đối** nối từ **19. Lợi suất kỳ vọng phải được chuẩn hóa theo rủi ro** sang **21. Phần bù rủi ro cổ phiếu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Định giá tương đối và tuyệt đối

Sau khi đánh giá lợi suất và rủi ro, ta cần hỏi giá hiện tại đang được so với dòng tiền của chính tài sản hay với cơ hội thay thế. Hai góc nhìn bổ sung cho nhau và giúp đặt earnings yield trong bối cảnh lãi suất thực, tăng trưởng và rủi ro.

**Định giá tuyệt đối** hỏi giá hiện tại so với dòng tiền tương lai của chính tài sản.

**Định giá tương đối** hỏi tài sản rẻ hay đắt so với tài sản thay thế.

Ví dụ cổ phiếu có earnings yield 5% không thể đánh giá tách khỏi lợi suất trái phiếu thực và rủi ro tăng trưởng.

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **21. Phần bù rủi ro cổ phiếu** nối từ **20. Định giá tương đối và tuyệt đối** sang **22. Thanh khoản là một phần của định giá**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Phần bù rủi ro cổ phiếu

Một cách trực giác:

```text
Lợi suất kỳ vọng cổ phiếu
- lợi suất tài sản ít rủi ro
= phần bù rủi ro cổ phiếu kỳ vọng
```

Nếu lợi suất trái phiếu tăng trong khi định giá cổ phiếu không đổi, phần bù tương đối có thể co lại và áp lực lên bội số tăng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **22. Thanh khoản là một phần của định giá** nối từ **21. Phần bù rủi ro cổ phiếu** sang **23. Kiểm thử vai trò của tài sản**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Thanh khoản là một phần của định giá

Hai tài sản có dòng tiền giống nhau nhưng tài sản khó bán thường cần phần bù cao hơn.

Trong bình thường, chênh lệch này có thể nhỏ. Trong căng thẳng, spread và tác động thị trường tăng rất nhanh. Vì vậy thanh khoản phải được đưa vào lợi suất kỳ vọng và quy mô vị thế.

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **23. Kiểm thử vai trò của tài sản** nối từ **22. Thanh khoản là một phần của định giá** sang **24. Bài tập so sánh bốn tài sản**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **23. Kiểm thử vai trò của tài sản** đặt tiêu chí; **24. Bài tập so sánh bốn tài sản** dùng tiêu chí đó để kiểm tra ranh giới, rồi **25. Liên kết đọc tiếp** mở rộng hệ quả.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **24. Bài tập so sánh bốn tài sản** đặt tiêu chí; **25. Liên kết đọc tiếp** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Kết luận** mở rộng hệ quả.

## 25. Liên kết đọc tiếp

Các tài liệu sau mở rộng từng nhóm tài sản và cách chúng kết hợp trong danh mục. Hãy chọn liên kết tương ứng với biến rủi ro còn chưa rõ sau bài lab, rồi quay lại kiểm tra giả định ban đầu.

- [Cổ phiếu, ETF và quỹ](./01_STOCKS_ETF_AND_FUNDS.md)
- [Trái phiếu, lãi suất và tín dụng](./02_BONDS_RATES_AND_CREDIT.md)
- [Tài sản thực và thay thế](./03_REAL_ASSETS_AND_ALTERNATIVES.md)
- [Nhân tố, chỉ số và hành vi đa tài sản](./04_FACTORS_INDEXING_AND_MULTI_ASSET_BEHAVIOR.md)
- [Danh mục đa tài sản và phòng vệ](./05_MULTI_ASSET_HEDGING_CURRENCY_AND_REGIME_ALLOCATION.md)

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: định giá tài sản, cấu trúc kỳ hạn và vai trò trong danh mục**, **Kết luận** tổng hợp từ **25. Liên kết đọc tiếp** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

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
