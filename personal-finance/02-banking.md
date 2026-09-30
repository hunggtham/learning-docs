# 02 — Ngân hàng và hệ thống thanh toán (Banking / 은행)

## Định vị

Sau [01 — Money](./01-money.md), ta đã có hai câu hỏi thực tế: tiền cần đủ thanh khoản (liquidity / 유동성) cho các nghĩa vụ gần, nhưng giữ và di chuyển tiền bằng cách nào? Chapter này giải thích tài khoản ngân hàng (bank account / 은행계좌), tiền gửi (deposit / 예금), thanh toán (payment / 결제), phí và rủi ro vận hành. Phần tạo tiền, chính sách tiền tệ và vai trò ngân hàng trong toàn nền kinh tế thuộc [Economics](../economics/README.md); ở đây chỉ giữ góc nhìn của cá nhân/hộ gia đình.

## Tài khoản không phải chiếc hộp tiền

Khi gửi tiền vào ngân hàng, người dùng nhìn thấy một số dư, nhưng về mặt pháp lý và kế toán, số dư thường thể hiện một **khoản ngân hàng nợ người gửi tiền** theo điều khoản của tài khoản. Vì vậy cần phân biệt tiền mặt vật lý với tiền gửi ngân hàng (bank deposit / 은행예금).

Điều này giúp hiểu tại sao một tài khoản có nhiều thuộc tính hơn “có bao nhiêu tiền”: khả năng rút, giới hạn giao dịch, phí, thời gian xử lý, lãi suất, điều kiện bảo vệ tiền gửi và quyền hoàn trả khi giao dịch có vấn đề đều quan trọng.

## Tài khoản giao dịch và tài khoản tiết kiệm

Tài khoản giao dịch (transaction account / 결제계좌) ưu tiên khả năng nhận lương, chuyển khoản, thanh toán hóa đơn, dùng thẻ và rút tiền. Tài khoản tiết kiệm (savings account / 저축예금) thường ưu tiên giữ tiền và có thể trả lãi tốt hơn, nhưng điều kiện truy cập khác nhau theo ngân hàng và quốc gia.

Không nên chọn chỉ bằng lãi suất quảng cáo. Một so sánh đúng cần nhìn:

```text
Lợi ích ròng của tài khoản
= lãi nhận được
− phí duy trì/chuyển/rút
− chi phí do điều kiện số dư
− chi phí do khóa hoặc chậm truy cập tiền
```

Nếu một khoản là quỹ dự phòng (emergency fund / 비상자금), quyền truy cập và độ tin cậy có thể quan trọng hơn một chênh lệch lãi suất nhỏ. Chapter [12 — Emergency Fund](./12-emergency-fund.md) sẽ dùng lại nguyên tắc này.

## Thanh toán là một quá trình, không phải một cú nhấp

Khi quẹt thẻ hoặc chuyển tiền, giao diện tạo cảm giác giao dịch xảy ra ngay. Thực tế thường có nhiều bước: xác thực (authentication / 인증), ủy quyền (authorization / 승인), truyền thông điệp thanh toán, ghi nhận tạm thời và quyết toán (settlement / 결제완료). Tốc độ và khả năng đảo ngược phụ thuộc phương thức.

Vì vậy “số dư khả dụng” và “số dư sổ sách” có thể khác nhau khi giao dịch đang chờ xử lý. Một khoản chuyển cũng có thể không có cùng cơ chế bảo vệ như giao dịch thẻ. Khi thanh toán cho người lạ, cần hiểu liệu phương thức đó cho phép tranh chấp (dispute / 이의제기) hay hoàn trả (chargeback / 지불거절) theo quy định áp dụng hay không.

## Thẻ ghi nợ và thẻ tín dụng

Thẻ ghi nợ (debit card / 체크카드) thường trừ trực tiếp hoặc gần trực tiếp từ tiền trong tài khoản. Thẻ tín dụng (credit card / 신용카드) tạo một khoản tín dụng ngắn hạn và nghĩa vụ thanh toán sau. Hai phương thức có thể giống nhau ở quầy thanh toán nhưng khác hoàn toàn về nguồn tiền, rủi ro dòng tiền và cơ chế tín dụng.

Nếu dùng thẻ tín dụng mà chỉ nhìn “số tiền tối thiểu phải trả”, người dùng có thể bỏ qua chi phí lãi đang tích lũy. Cơ chế này được giải thích ở [05 — Credit](./05-credit.md) và [06 — Loans & Debt](./06-loans-debt.md).

## Bảo vệ tiền gửi không phải bảo hiểm mọi rủi ro

Nhiều quốc gia có cơ chế bảo hiểm hoặc bảo vệ tiền gửi (deposit insurance / 예금자보호) cho các loại tiền gửi đủ điều kiện, nhưng giới hạn, tổ chức được bảo vệ, loại tài khoản và mức chi trả khác nhau theo jurisdiction. Không được áp dụng mức bảo vệ của Mỹ, Hàn Quốc hay Việt Nam cho nhau.

Ngay cả khi tiền gửi được bảo vệ trước một số trường hợp ngân hàng mất khả năng chi trả, điều đó không bảo vệ khỏi mọi rủi ro: lừa đảo do người dùng tự chuyển tiền, mất thông tin đăng nhập, tranh chấp thương mại, biến động ngoại tệ hoặc việc giữ sản phẩm không thuộc phạm vi bảo hiểm có thể có cơ chế khác.

Do đó trước khi gửi số tiền lớn, kiểm tra ba lớp riêng:

```text
Tổ chức có được cấp phép/giám sát không?
→ sản phẩm cụ thể có thuộc chương trình bảo vệ không?
→ giới hạn bảo vệ được tính theo người, tài khoản hay tổ chức như thế nào?
```

## Phí và ma sát tài chính

Phí nhỏ nhưng lặp lại có thể làm giảm đáng kể hiệu quả của hệ thống tiền cá nhân. Các loại thường gặp gồm phí duy trì, phí ATM, phí chuyển tiền, phí ngoại tệ, phí thấu chi (overdraft / 당좌대월) và chênh lệch tỷ giá.

Đừng chỉ hỏi “phí bao nhiêu?”. Hãy hỏi “hành vi nào kích hoạt phí?”. Một tài khoản miễn phí với điều kiện số dư tối thiểu có thể trở thành đắt nếu nó buộc giữ lượng tiền nhàn rỗi lớn; một dịch vụ chuyển tiền có phí thấp nhưng tỷ giá bất lợi vẫn có tổng chi phí cao.

## Thiết kế hệ thống tài khoản

Một cấu trúc đơn giản có thể tách tiền theo chức năng thay vì mở thật nhiều tài khoản:

```text
Tài khoản vận hành: lương + hóa đơn thường xuyên
Tài khoản dự phòng: cú sốc ngắn hạn
Tài khoản mục tiêu: khoản chi có thời hạn xác định
Tài khoản đầu tư: chỉ nhận phần vốn thực sự có thể đầu tư
```

Mục tiêu không phải tạo nhiều “phong bì”, mà giảm khả năng dùng nhầm tiền có nhiệm vụ khác. Khi hệ thống quá phức tạp, chi phí quản lý và nguy cơ quên phí/điều kiện lại tăng.

## Kết luận và hướng đọc tiếp

Ngân hàng (banking / 은행) trong tài chính cá nhân là hạ tầng cho **giữ tiền, chuyển tiền và quản lý thanh khoản**, không phải thước đo tự động về độ an toàn. Sau khi hiểu nơi tiền được giữ, bước tiếp theo là hiểu **giá của việc dùng tiền theo thời gian**. [03 — Interest](./03-interest.md) sẽ giải thích vì sao 1 đơn vị tiền hôm nay không tương đương 1 đơn vị tiền trong tương lai, và cách APR, APY cùng lãi kép thay đổi cả tiết kiệm lẫn nợ.

### Nguồn tham khảo

- CFPB consumer tools: https://www.consumerfinance.gov/consumer-tools/
- Với bảo hiểm tiền gửi, luôn dùng trang chính thức của cơ quan bảo hiểm/giám sát tại quốc gia đang áp dụng thay vì lấy một mức giới hạn chung cho mọi nơi.
