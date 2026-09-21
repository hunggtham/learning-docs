# Hệ thống tiền tệ, thanh khoản và cơ chế truyền dẫn khủng hoảng

> Chương này giải thích “đường ống” của hệ thống tài chính bằng tiếng Việt. Các thuật ngữ tiếng Anh chỉ được giữ như từ khóa tra cứu ở lần xuất hiện cần thiết. Mục tiêu là phân biệt rõ tiền, tín dụng, thanh khoản, vốn, tài sản bảo đảm, nguồn vốn và khả năng thanh toán để hiểu vì sao một cú sốc nhỏ có thể bị khuếch đại thành khủng hoảng.

# Phần I — Các lớp tiền khác nhau

## 1. Tiền mặt, tiền gửi và dự trữ ngân hàng

Ba khái niệm này không giống nhau.

**Tiền mặt (cash/banknotes)** là tiền giấy và tiền xu do cơ quan tiền tệ phát hành.

**Tiền gửi ngân hàng (bank deposits)** là nghĩa vụ của ngân hàng thương mại đối với khách hàng. Phần lớn giao dịch hằng ngày trong nền kinh tế hiện đại sử dụng lớp tiền này.

**Dự trữ ngân hàng (bank reserves)** là tài sản của ngân hàng thương mại tại ngân hàng trung ương, chủ yếu dùng cho thanh toán liên ngân hàng và vận hành hệ thống tiền tệ. Nhà đầu tư cá nhân không trực tiếp sở hữu dự trữ ngân hàng.

## 2. Khi ngân hàng cấp tín dụng

Khi ngân hàng cấp một khoản vay, bảng cân đối thường đồng thời xuất hiện:

```text
Tài sản: khoản cho vay
Nợ phải trả: tiền gửi của khách hàng
```

Vì vậy tín dụng ngân hàng có thể mở rộng sức mua mà không cần lượng tiền giấy vật lý tăng tương ứng. Đây là lý do khi phân tích “cung tiền” phải phân biệt tiền mặt, tiền gửi, tín dụng và dự trữ.

## 3. Bảng cân đối ngân hàng trung ương

Một bảng cân đối đơn giản có thể gồm:

```text
Tài sản:
Trái phiếu chính phủ
Khoản cho vay / chương trình hỗ trợ
Dự trữ ngoại hối

Nợ phải trả:
Dự trữ của ngân hàng thương mại
Tiền mặt lưu hành
Tiền gửi của chính phủ
```

Nới lỏng định lượng (Quantitative Easing, QE), thắt chặt định lượng (Quantitative Tightening, QT) và các chương trình cho vay khẩn cấp làm thay đổi bảng cân đối theo các cơ chế khác nhau.

# Phần II — Hệ thống lãi suất ngắn hạn

## 4. Lãi suất chính sách không phải mọi lãi suất trong nền kinh tế

Ngân hàng trung ương trực tiếp kiểm soát hoặc định hướng một lãi suất ngắn hạn. Từ đó tác động được truyền qua:

```text
Lãi suất chính sách
→ lãi suất thị trường tiền tệ
→ chi phí nguồn vốn ngân hàng
→ lợi suất trái phiếu
→ lãi vay doanh nghiệp / thế chấp
→ tiêu dùng và đầu tư
```

Cùng một mức lãi suất chính sách có thể tạo điều kiện tài chính rất khác nếu chênh lệch tín dụng, tỷ giá hoặc tiêu chuẩn cho vay thay đổi.

## 5. Hệ thống sàn và hệ thống hành lang

Trong **hệ thống sàn (floor system)**, dự trữ thường tương đối dồi dào và lãi trả trên dự trữ giúp tạo mức sàn cho lãi suất ngắn hạn.

Trong **hệ thống hành lang (corridor system)**, lãi suất cho vay và lãi suất nhận tiền gửi tại ngân hàng trung ương tạo một vùng để lãi suất thị trường dao động bên trong.

Điểm cần hiểu là cách ngân hàng trung ương truyền tín hiệu chính sách tới giá của nguồn vốn ngắn hạn, không phải học thuộc tên từng chương trình.

# Phần III — Giao dịch mua lại và tài sản bảo đảm

## 6. Giao dịch mua lại — repo

Giao dịch mua lại (repurchase agreement, repo) về bản chất kinh tế gần với khoản vay có tài sản bảo đảm.

```text
Bên vay giao tài sản bảo đảm
→ nhận tiền mặt
→ cam kết mua lại tài sản sau một khoảng thời gian
```

Chênh lệch giữa giá bán và giá mua lại phản ánh chi phí vốn của giao dịch.

## 7. Tài sản bảo đảm

**Tài sản bảo đảm (collateral)** không chỉ giảm rủi ro tín dụng mà còn quyết định khả năng vay vốn. Tài sản có chất lượng cao, dễ định giá và dễ bán thường cho phép vay nhiều hơn.

Trong hệ thống tài chính, chất lượng của tài sản bảo đảm có thể quan trọng gần ngang lượng tiền mặt vì nhiều giao dịch tài trợ phụ thuộc vào nó.

## 8. Tỷ lệ chiết trừ tài sản bảo đảm

**Tỷ lệ chiết trừ (haircut)** là phần giá trị của tài sản bảo đảm không được tính vào khả năng vay.

Ví dụ:

```text
Giá trị tài sản bảo đảm = 100
Haircut = 10%
Khả năng vay ≈ 90
```

Nếu tỷ lệ này tăng lên 20%, khả năng vay giảm xuống khoảng 80 ngay cả khi giá tài sản chưa đổi.

## 9. Vòng xoáy tăng haircut

Trong giai đoạn căng thẳng:

```text
Biến động ↑
→ Haircut ↑
→ nhu cầu tiền mặt / tài sản bảo đảm ↑
→ bán cưỡng bức ↑
→ giá tài sản ↓
→ Haircut tiếp tục ↑
```

Đây là một trong các cơ chế khiến cú sốc tài chính tự khuếch đại.

# Phần IV — Nhà tạo lập và khả năng trung gian thị trường

## 10. Bảng cân đối nhà tạo lập

Nhà tạo lập hoặc trung gian giao dịch (dealer) kết nối người mua và người bán, tạm thời giữ tài sản và cung cấp thanh khoản. Nhưng khả năng này bị giới hạn bởi:

- vốn;
- nguồn tài trợ;
- đòn bẩy;
- giới hạn rủi ro;
- quy định.

Khi khả năng sử dụng bảng cân đối giảm, độ sâu thị trường có thể giảm dù tài sản đã trở nên “rẻ”.

## 11. Thanh khoản thị trường thay đổi theo trạng thái hệ thống

Thanh khoản không phải đặc tính cố định. Một tài sản bình thường dễ giao dịch có thể trở nên khó bán khi:

- biến động tăng;
- các trung gian giảm tồn kho;
- nhiều người cùng muốn bán;
- giá trị tài sản bảo đảm giảm;
- nguồn vốn trở nên khan hiếm.

Vì vậy phải phân biệt **thanh khoản của tài sản** với **thanh khoản của hệ thống tài chính**.

# Phần V — Quỹ thị trường tiền tệ và quản lý tiền mặt

## 12. Quỹ thị trường tiền tệ

Quỹ thị trường tiền tệ (Money Market Fund, MMF) đầu tư vào tài sản ngắn hạn như tín phiếu kho bạc, giao dịch repo và giấy tờ có độ an toàn tương đối cao.

Dòng tiền chuyển giữa tiền gửi ngân hàng, MMF, tín phiếu kho bạc và các công cụ repo có thể làm thay đổi phân bố thanh khoản trong hệ thống.

## 13. Tài khoản tiền của chính phủ

Tại Mỹ, tài khoản tiền của Bộ Tài chính tại ngân hàng trung ương thường được gọi là **Treasury General Account (TGA)**.

Nếu chính phủ tăng mạnh số dư tại đây, dự trữ của hệ thống ngân hàng có thể giảm nếu các yếu tố khác giữ nguyên. Khi chính phủ chi tiêu từ tài khoản, dự trữ có thể quay lại hệ thống.

## 14. Công cụ repo đảo chiều

Công cụ repo đảo chiều (reverse repo facility) cho phép các tổ chức đủ điều kiện gửi tiền mặt đổi lấy tài sản bảo đảm.

Dòng tiền giữa MMF, công cụ repo đảo chiều, tín phiếu kho bạc và tiền gửi có thể thay đổi mạnh mà không có nghĩa nền kinh tế “thiếu tiền” theo nghĩa đơn giản.

# Phần VI — Phát hành nợ chính phủ và phần bù kỳ hạn

## 15. Cơ cấu phát hành nợ

Chính phủ có thể tài trợ bằng tín phiếu ngắn hạn, trái phiếu trung hạn và trái phiếu dài hạn. Cơ cấu kỳ hạn quyết định lượng **rủi ro thời hạn (duration)** mà khu vực tư nhân phải hấp thụ.

## 16. Phần bù kỳ hạn

**Phần bù kỳ hạn (term premium)** là phần lợi suất nhà đầu tư yêu cầu để chịu rủi ro nắm trái phiếu dài hạn ngoài kỳ vọng lãi suất ngắn hạn tương lai.

Một cơ chế có thể là:

```text
Phát hành dài hạn ↑
+ nhu cầu không tăng tương ứng
→ phần bù kỳ hạn ↑
→ lợi suất dài hạn ↑
```

Khi đó điều kiện tài chính có thể thắt chặt dù ngân hàng trung ương không nâng lãi suất chính sách.

# Phần VII — Vốn và thanh khoản ngân hàng

## 17. Vốn và thanh khoản khác nhau

**Vốn (capital)** là lớp hấp thụ tổn thất.

**Thanh khoản (liquidity)** là khả năng đáp ứng nghĩa vụ tiền mặt đúng thời điểm.

Một ngân hàng có vốn kế toán tốt vẫn có thể gặp khủng hoảng nếu dòng tiền rút quá nhanh và tài sản không thể chuyển thành tiền kịp thời.

## 18. Khả năng thanh toán dài hạn

**Khả năng thanh toán dài hạn (solvency)** hỏi liệu giá trị kinh tế của tài sản có đủ lớn so với nghĩa vụ hay không.

Hỗ trợ thanh khoản có thể giải quyết vấn đề thời điểm dòng tiền, nhưng không tự động sửa một bảng cân đối đã mất khả năng thanh toán.

## 19. Dòng tiền gửi rút ra nhanh

Tiền gửi có thể rời ngân hàng vì:

- mất niềm tin;
- khách hàng gửi tiền lớn tập trung;
- sản phẩm khác có lãi suất hấp dẫn hơn;
- tin tức lan nhanh qua ngân hàng số.

Tốc độ rút tiền hiện đại có thể lớn hơn nhiều so với mô hình khủng hoảng ngân hàng truyền thống.

## 20. Rủi ro tập trung nguồn vốn

Ngân hàng có hàng triệu khoản tiền gửi nhỏ khác hẳn ngân hàng phụ thuộc vài khách hàng doanh nghiệp lớn. **Tập trung nguồn vốn (funding concentration)** là một nguồn rủi ro độc lập.

# Phần VIII — Lệch kỳ hạn trên bảng cân đối ngân hàng

## 21. Tài sản dài hạn, nguồn vốn ngắn hạn

Một cấu trúc thường gặp:

```text
Nguồn vốn:
tiền gửi / vay ngắn hạn

Tài sản:
trái phiếu dài hạn / khoản thế chấp dài hạn
```

Khi lãi suất tăng, giá thị trường của tài sản dài hạn giảm. Nếu người gửi tiền ổn định, ngân hàng có thể tiếp tục nắm giữ. Nếu tiền gửi rút nhanh, ngân hàng có thể buộc phải bán và hiện thực hóa lỗ.

## 22. Từ lỗ chưa thực hiện tới lỗ thực hiện

Lỗ đánh dấu theo thị trường chưa nhất thiết làm mất tiền mặt ngay. Nhưng khi tài sản phải bán:

```text
Lỗ chưa thực hiện
→ lỗ thực hiện
→ vốn giảm
```

Đây là cầu nối giữa rủi ro duration, thanh khoản và khả năng thanh toán.

# Phần IX — Tạo tín dụng và cơ chế khuếch đại tài chính

## 23. Tín dụng không chỉ phụ thuộc lãi suất chính sách

Ngân hàng quyết định cho vay dựa trên:

- vốn;
- nguồn vốn;
- tài sản bảo đảm;
- tổn thất kỳ vọng;
- quy định;
- khẩu vị rủi ro.

Do đó giảm lãi suất không bảo đảm tín dụng tăng ngay.

## 24. Cơ chế khuếch đại tài chính

**Cơ chế khuếch đại tài chính (financial accelerator)** mô tả vòng phản hồi:

```text
Giá tài sản ↓
→ giá trị tài sản bảo đảm ↓
→ tiêu chuẩn cho vay chặt hơn
→ tín dụng ↓
→ đầu tư / tiêu dùng ↓
→ lợi nhuận doanh nghiệp ↓
→ chất lượng tín dụng ↓
```

Một cú sốc tài chính vì vậy có thể truyền sang nền kinh tế thực.

# Phần X — Tổ chức tài chính phi ngân hàng

## 25. NBFI

**Tổ chức tài chính phi ngân hàng (Non-Bank Financial Institution, NBFI)** gồm quỹ đầu tư, công ty bảo hiểm, quỹ hưu trí, công ty tài chính và các tổ chức khác ngoài ngân hàng truyền thống.

Rủi ro tín dụng hoặc đòn bẩy có thể chuyển khỏi bảng cân đối ngân hàng sang khu vực này thay vì biến mất.

## 26. Đòn bẩy ẩn

Phái sinh, repo và sản phẩm cấu trúc có thể tạo mức phơi nhiễm lớn hơn số vốn ban đầu. Khi biến động tăng, yêu cầu bổ sung ký quỹ có thể buộc tổ chức bán tài sản khác để lấy tiền mặt.

# Phần XI — Hệ thống nguồn vốn USD toàn cầu

## 27. Nhu cầu USD ngoài nước Mỹ

Doanh nghiệp và ngân hàng ngoài Mỹ có thể vay USD để tài trợ thương mại, đầu tư hoặc tài sản bằng USD.

Khi nguồn vốn USD trở nên khan hiếm:

```text
Chi phí vốn USD ↑
→ chi phí phòng vệ tỷ giá ↑
→ giảm đòn bẩy ↑
→ tín dụng toàn cầu thắt chặt
```

## 28. Cơ sở hoán đổi tiền tệ

**Cơ sở hoán đổi tiền tệ (cross-currency basis)** phản ánh phần chi phí hoặc mất cân bằng khi đổi nguồn vốn giữa hai đồng tiền thông qua hoán đổi.

Mức cơ sở căng bất thường có thể cho thấy nhu cầu USD hoặc giới hạn bảng cân đối của trung gian đang tăng.

# Phần XII — QE và QT

## 29. Nới lỏng định lượng

Nới lỏng định lượng (QE) thường là việc ngân hàng trung ương mua tài sản dài hạn và tạo thêm dự trữ ngân hàng.

Các kênh tác động có thể gồm:

- giảm lượng duration khu vực tư nhân phải nắm;
- giảm phần bù kỳ hạn;
- hỗ trợ khả năng vận hành của thị trường;
- thúc đẩy tái cân bằng danh mục.

QE không đồng nghĩa trực tiếp với việc phát tiền mặt cho hộ gia đình.

## 30. Thắt chặt định lượng

Thắt chặt định lượng (QT) làm bảng cân đối ngân hàng trung ương giảm khi tài sản đáo hạn mà không được tái đầu tư hoặc được bán.

Ảnh hưởng thực tế phụ thuộc tốc độ QT, số dư tiền của chính phủ, dòng tiền khỏi công cụ repo đảo chiều, nhu cầu dự trữ và cơ cấu phát hành nợ.

## 31. Dự trữ dồi dào không bảo đảm mọi thị trường đều thanh khoản

Căng thẳng có thể nằm ở:

- chất lượng tài sản bảo đảm;
- khả năng trung gian của nhà tạo lập;
- một thị trường nguồn vốn cụ thể;
- lo ngại đối tác;
- giới hạn bảng cân đối.

Do đó không nên dùng một chỉ số dự trữ duy nhất để kết luận toàn hệ thống đang “thừa thanh khoản”.

# Phần XIII — Công cụ hỗ trợ khẩn cấp

## 32. Người cho vay cuối cùng

Ngân hàng trung ương có thể đóng vai trò **người cho vay cuối cùng (lender of last resort)** bằng cách cung cấp thanh khoản tạm thời cho tổ chức đủ điều kiện dựa trên tài sản bảo đảm.

Mục tiêu là ngăn thiếu tiền mặt ngắn hạn biến thành bán tháo tài sản không cần thiết.

## 33. Hỗ trợ thanh khoản khác tái cấp vốn chủ sở hữu

```text
Hỗ trợ thanh khoản
→ giải quyết vấn đề thời điểm và nguồn vốn

Tái cấp vốn chủ sở hữu
→ bổ sung lớp vốn hấp thụ tổn thất
```

Không nên gọi mọi hình thức hỗ trợ là QE hoặc “cứu trợ”.

# Phần XIV — Các dạng khủng hoảng

## 34. Khủng hoảng ngân hàng

Có thể bắt đầu từ:

- tổn thất tín dụng;
- tổn thất duration;
- rút tiền gửi;
- gian lận;
- bất động sản giảm mạnh;
- mất niềm tin vào khả năng thanh toán.

## 35. Khủng hoảng tín dụng

Chênh lệch tín dụng mở rộng, thị trường phát hành đóng lại và doanh nghiệp yếu không thể tái cấp vốn. Tác động thường lan qua đầu tư, việc làm và lợi nhuận.

## 36. Khủng hoảng tiền tệ

Một nền kinh tế dễ tổn thương khi có nợ ngoại tệ lớn, dự trữ thấp, thâm hụt đối ngoại và niềm tin chính sách yếu. Đồng tiền mất giá có thể làm gánh nợ ngoại tệ tăng thêm.

## 37. Khủng hoảng chủ quyền

Nợ công mất bền vững có thể kéo lợi suất tăng, làm hệ thống ngân hàng yếu nếu ngân hàng nắm nhiều trái phiếu chính phủ. Đây là cơ chế liên kết giữa nhà nước và ngân hàng.

# Phần XV — Khung phân tích căng thẳng hệ thống

Khi xuất hiện một sự kiện tài chính, hãy đi theo thứ tự:

```text
1. Tổn thất nằm ở tài sản nào?
2. Ai đang nắm tài sản đó?
3. Họ dùng bao nhiêu đòn bẩy?
4. Nguồn vốn của họ có ổn định không?
5. Tài sản bảo đảm có bị giảm giá không?
6. Có yêu cầu bổ sung ký quỹ không?
7. Ai có thể cung cấp thanh khoản?
8. Vấn đề là thiếu thanh khoản hay mất khả năng thanh toán?
9. Cú sốc có truyền sang tín dụng thực không?
10. Chính sách xử lý phần nào của vấn đề?
```

## 38. Bảng theo dõi thanh khoản

Một bảng theo dõi thực tế có thể gồm:

- lãi suất qua đêm và repo;
- chênh lệch tín dụng;
- biến động trái phiếu và cổ phiếu;
- mức cơ sở hoán đổi tiền tệ;
- phát hành nợ chính phủ;
- số dư tiền của chính phủ;
- dòng tiền quỹ thị trường tiền tệ;
- tiêu chuẩn cho vay ngân hàng;
- mức sử dụng công cụ khẩn cấp;
- độ sâu thị trường và chênh lệch giá mua–bán.

Không một chỉ số nào đủ để kết luận “thanh khoản tốt” hay “thanh khoản xấu”.

## 39. Cầu nối sang tài sản đầu tư

```text
Nguồn vốn căng
→ đòn bẩy giảm
→ thanh khoản thị trường giảm
→ chênh lệch tín dụng tăng
→ doanh nghiệp tái cấp vốn khó hơn
→ lợi nhuận / đầu tư giảm
→ định giá tài sản thay đổi
```

Với cổ phiếu, tác động đi qua cả lợi nhuận và hệ số định giá. Với trái phiếu doanh nghiệp, tác động đi trực tiếp qua chênh lệch tín dụng và khả năng tái cấp vốn. Với FX, tác động phụ thuộc nhu cầu tiền tệ an toàn và cấu trúc nợ ngoại tệ.

## 40. Kết luận

Cơ chế truyền dẫn khủng hoảng thường không bắt đầu bằng câu hỏi “cung tiền tăng hay giảm”, mà bằng chuỗi:

```text
Bảng cân đối
→ nguồn vốn
→ tài sản bảo đảm
→ ký quỹ
→ bán cưỡng bức
→ thanh khoản
→ tín dụng
→ kinh tế thực
```

Khi hiểu chuỗi này, các thuật ngữ như repo, haircut, QE, QT hay cơ sở hoán đổi chỉ còn là tên của các mắt xích cụ thể, không phải những từ tiếng Anh phải ghi nhớ mà chưa hiểu bản chất.