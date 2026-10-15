# 01 — Tiền trong tài chính cá nhân (Money / 돈)

## Định vị

Chapter này là điểm bắt đầu của `personal-finance/`. Trước khi học ngân hàng (banking / 은행), lãi suất (interest / 이자), tín dụng (credit / 신용) hay đầu tư (investing / 투자), cần tách ba ý thường bị trộn với nhau: **tiền (money / 화폐)** là công cụ trao đổi và đơn vị đo giá trị; **thu nhập (income / 소득)** là dòng giá trị đi vào trong một khoảng thời gian; còn **tài sản ròng (net worth / 순자산)** là giá trị tài sản trừ nghĩa vụ tại một thời điểm.

Một người có thu nhập cao vẫn có thể có tài sản ròng thấp nếu chi tiêu và nợ tăng tương ứng. Ngược lại, một người có tài sản lớn có thể gặp khủng hoảng ngắn hạn nếu tài sản kém thanh khoản (illiquid / 비유동성) nhưng hóa đơn phải trả ngay. Đây là lý do tài chính cá nhân phải nhìn cả **dòng (flow / 흐름)** và **tồn lượng (stock / 저량)**.

## Tiền giải quyết vấn đề gì?

Trong đời sống, tiền (money / 화폐) thực hiện ba chức năng cơ bản: phương tiện trao đổi (medium of exchange / 교환수단), đơn vị tính toán (unit of account / 계산단위) và phương tiện lưu giữ giá trị (store of value / 가치저장수단). Ba chức năng này không có nghĩa sức mua của tiền bất biến. Nếu mức giá chung tăng, cùng một số tiền danh nghĩa mua được ít hàng hóa và dịch vụ hơn; chapter [04 — Inflation](./04-inflation.md) sẽ giải thích cơ chế này.

Đối với tài chính cá nhân, cách hữu ích nhất để nghĩ về tiền là **quyền lựa chọn có tính thanh khoản**. 1 triệu đồng hoặc 100.000 won đang ở tài khoản có thể được dùng cho nhiều nhu cầu gần như ngay lập tức. Khi số tiền đó được đổi thành một tài sản khó bán, tính thanh khoản (liquidity / 유동성) giảm dù giá trị kế toán có thể không đổi.

## Dòng tiền trước ngân sách

Dòng tiền (cash flow / 현금흐름) trong một kỳ có thể viết đơn giản:

```text
Dòng tiền ròng = Tiền vào − Tiền ra
```

Tiền vào thường gồm lương, thu nhập kinh doanh, tiền lãi hoặc các khoản chuyển giao. Tiền ra có thể chia thành nghĩa vụ tương đối cố định như tiền thuê nhà, trả nợ, bảo hiểm; chi phí thiết yếu biến đổi như ăn uống, điện nước; và chi tiêu tùy ý.

Ngân sách (budget / 예산) không phải mục tiêu tự thân. Nó là mô hình dự kiến của dòng tiền để phát hiện ba câu hỏi: tiền đang đi đâu, nghĩa vụ nào khó thay đổi trong ngắn hạn, và còn bao nhiêu khoảng trống để hấp thụ cú sốc. Nếu ngân sách chỉ liệt kê chi tiêu nhưng không phân biệt nghĩa vụ cố định với khoản có thể cắt giảm, nó khó dùng khi thu nhập giảm.

Một mô hình thực hành tốt hơn là:

```text
Thu nhập khả dụng
− chi phí thiết yếu
− nghĩa vụ nợ tối thiểu
− bảo vệ rủi ro cần thiết
= phần linh hoạt cho tiết kiệm, mục tiêu và tiêu dùng tùy ý
```

Không có tỷ lệ phần trăm duy nhất đúng cho mọi người. Chi phí nhà ở, hệ thống thuế, gia đình, công việc và mức ổn định thu nhập làm cấu trúc dòng tiền khác nhau đáng kể.

## Tiết kiệm không đồng nghĩa đầu tư

Tiết kiệm (saving / 저축) là phần thu nhập chưa tiêu dùng. Đầu tư (investing / 투자) là đưa vốn vào tài sản với kỳ vọng nhận dòng tiền hoặc tăng giá, đồng thời chấp nhận một dạng rủi ro. Tiền dành cho hóa đơn ba tháng tới và tiền dành cho mục tiêu 20 năm không có cùng thời hạn (time horizon / 투자기간), nên không nhất thiết được đặt vào cùng loại tài sản.

Đây là ranh giới quan trọng của library: `personal-finance/` quyết định **bao nhiêu tiền thực sự có thể chịu khóa hoặc chịu biến động**; [Investing](../investing/README.md) quyết định **phân bổ phần vốn đầu tư đó như thế nào**.

## Chi phí cơ hội và quyết định bằng tiền

Mỗi đồng tiền chỉ có thể được dùng cho một mục đích tại một thời điểm. Giá trị của lựa chọn tốt nhất bị bỏ qua là chi phí cơ hội (opportunity cost / 기회비용). Nếu dùng toàn bộ khoản dự phòng để trả trước cho một tài sản dài hạn, lợi ích có thể là giảm chi phí vay; chi phí cơ hội là mất thanh khoản khi có thất nghiệp hoặc chi phí y tế bất ngờ.

Chi phí cơ hội không có nghĩa “luôn chọn phương án có lợi suất cao nhất”. Trong tài chính cá nhân, giá trị của thanh khoản, bảo hiểm và sự linh hoạt có thể lớn hơn phần lợi suất chênh lệch, đặc biệt khi một cú sốc buộc phải vay với lãi suất cao hoặc bán tài sản vào thời điểm bất lợi.

## Danh nghĩa và thực

Tiền thường được ghi theo giá trị danh nghĩa (nominal value / 명목가치): 10 triệu vẫn được ghi là 10 triệu. Nhưng quyết định dài hạn cần nghĩ theo giá trị thực (real value / 실질가치), tức sức mua sau biến động mức giá. Nếu thu nhập tăng 3% nhưng chi phí sinh hoạt tăng 5%, thu nhập danh nghĩa tăng nhưng sức mua thực giảm xấp xỉ.

Quan hệ này là cầu nối trực tiếp sang [03 — Interest](./03-interest.md) và [04 — Inflation](./04-inflation.md): lãi suất cho biết giá của việc chuyển sức mua giữa hiện tại và tương lai; lạm phát cho biết đơn vị tiền đó thay đổi sức mua thế nào.

## Kết luận và hướng đọc tiếp

Mô hình cốt lõi của chapter là:

```text
Income là flow
Wealth/net worth là stock
Cash là liquidity
Saving tạo phần dư
Investing chỉ là một cách sử dụng phần dư đó
```

Đừng dùng số dư tài khoản để kết luận một người “giàu” hay dùng thu nhập để kết luận họ “an toàn”. Chapter tiếp theo, [02 — Banking](./02-banking.md), giải thích nơi tiền thường được giữ và di chuyển, các lớp tài khoản/thanh toán và rủi ro phát sinh khi hệ thống tài chính đứng giữa người dùng với tiền của họ.
