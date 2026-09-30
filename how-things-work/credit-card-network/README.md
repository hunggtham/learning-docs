# Credit Card Network — từ cú chạm thẻ tới tiền về cửa hàng

Khi terminal báo `APPROVED`, cửa hàng chưa nhất thiết đã nhận tiền. Khoảnh khắc đó chủ yếu xác nhận rằng bên phát hành thẻ chấp nhận giao dịch. Sau đó còn một chuỗi bù trừ (clearing / 청산), quyết toán (settlement / 결제), phí và đối soát. Vì vậy phải tách **authorization** khỏi **clearing/settlement**.

## 1. Những actor chính

- **Chủ thẻ (cardholder / 카드회원)**: người sử dụng thẻ.
- **Đơn vị chấp nhận thẻ (merchant / 가맹점)**: cửa hàng hoặc website bán hàng.
- **Ngân hàng/đơn vị thanh toán cho merchant (acquirer / 매입사)**: kết nối merchant vào hệ thống thẻ và nhận tiền settlement cho merchant.
- **Mạng hoặc tổ chức thẻ (card network/scheme / 카드 네트워크)**: định tuyến message, đặt rule và kết nối issuer với acquirer; ví dụ Visa, Mastercard hoặc mạng nội địa.
- **Tổ chức phát hành (issuer / 발급사)**: ngân hàng/công ty phát hành thẻ cho khách và chịu rủi ro tín dụng của cardholder.
- **POS/VAN/PG**: lớp công nghệ nhận message từ cửa hàng. Hàn Quốc đặc biệt quen với mô hình VAN ở offline và PG ở online; Việt Nam có POS/acquirer/payment gateway và lớp switching của NAPAS trong các giao dịch nội địa phù hợp.

## 2. Authorization: tại sao terminal trả lời trong vài giây?

```text
Card / phone wallet
      ↓
POS terminal
      ↓
Merchant processor / VAN / gateway
      ↓
Acquirer
      ↓
Card network
      ↓
Issuer
      ↓
Risk checks + balance/credit + card status
      ↓
APPROVE / DECLINE
      ↓
Response chạy ngược về POS
```

Issuer kiểm tra nhiều thứ trong thời gian rất ngắn: card có active không, cryptogram/token có hợp lệ không, hạn mức còn đủ không, giao dịch có dấu hiệu fraud không, MCC/địa điểm/country có bị hạn chế không. Một approval thường tạo authorization hold hoặc ghi nhận nghĩa vụ dự kiến; nó chưa phải settlement cuối cùng.

Nếu dùng thẻ contactless hoặc mobile wallet, số thẻ thật có thể được thay bằng token. EMV chip/contactless còn dùng dữ liệu mật mã để làm việc sao chép thẻ khó hơn magnetic stripe truyền thống.

## 3. Clearing và settlement

Cuối ngày hoặc theo batch, merchant/acquirer gửi bản ghi giao dịch vào clearing. Network xác định nghĩa vụ giữa issuer và acquirer, tính interchange/network fees theo rule tương ứng, rồi settlement chuyển tiền giữa các thành viên qua ngân hàng settlement hoặc hạ tầng thanh toán được chỉ định.

```text
AUTHORIZATION
Card → POS → Acquirer → Network → Issuer
                     ← APPROVED ←

CLEARING
Merchant batch → Acquirer → Network → Issuer

SETTLEMENT
Issuer funds
    ↓
Network / settlement banks
    ↓
Acquirer
    ↓
Merchant account
```

Khách hàng thấy một dòng “pending” rồi “posted”; merchant thấy gross sales nhưng nhận net amount sau merchant service fee và adjustments. Đó là lý do số tiền khách trả và số tiền merchant thực nhận không nhất thiết giống nhau.

## 4. Hàn Quốc: issuer, card company, VAN và PG

Hệ sinh thái thẻ Hàn Quốc có tỷ lệ sử dụng thẻ cao và một lớp **mạng giá trị gia tăng (Value Added Network, VAN / 부가가치통신망)** phát triển mạnh. Offline merchant thường kết nối POS tới VAN, VAN định tuyến authorization tới card company/acquirer thích hợp. Online commerce thường thêm **cổng thanh toán (Payment Gateway, PG / 전자지급결제대행)** để tích hợp nhiều phương thức thanh toán cho merchant.

Một giao dịch nội địa vì vậy có thể nhìn như:

```text
Merchant POS
   ↓
VAN
   ↓
Card company / acquirer
   ↓
Issuer-side authorization
   ↓
Clearing + settlement
```

Với thẻ quốc tế, Visa/Mastercard và các scheme khác có thể nằm trong đường định tuyến tùy sản phẩm và giao dịch.

## 5. Việt Nam: NAPAS, ngân hàng và mạng quốc tế

NAPAS vận hành hạ tầng chuyển mạch và bù trừ cho nhiều giao dịch thanh toán nội địa, kết nối ngân hàng và trung gian. Với thẻ nội địa, NAPAS có thể là lớp switching quan trọng giữa acquirer và issuer. Với thẻ Visa/Mastercard/JCB… đường đi tuân theo scheme quốc tế tương ứng; merchant vẫn cần acquirer/payment gateway để tham gia.

```text
Domestic card example
Card → POS → Acquirer → NAPAS switching → Issuer
                                   ↓
                         clearing / reconciliation
```

Sự phát triển mạnh của chuyển khoản nhanh và QR ở Việt Nam cũng làm “thanh toán tại cửa hàng” không đồng nghĩa “card network”. Nếu người dùng quét VietQR và chuyển khoản tài khoản–tài khoản, dòng tiền đi qua payment rails khác với Visa authorization dù giao diện tại quầy đều là thanh toán không tiền mặt.

## 6. So sánh Hàn Quốc ↔ Việt Nam

| Lớp | Hàn Quốc | Việt Nam |
|---|---|---|
| Offline acceptance | Card rất phổ biến; VAN là lớp kết nối đặc trưng | POS/card cùng tồn tại với QR account-to-account rất mạnh |
| Online acceptance | PG tích hợp card, bank transfer, wallets | Payment gateway tích hợp card, bank account, NAPAS, QR và wallets |
| Domestic switching | Card companies/VAN/KFTC và hạ tầng liên quan tùy rail | NAPAS có vai trò trung tâm ở nhiều rail nội địa |
| International cards | Visa/Mastercard/JCB/Amex… theo từng issuer/acquirer | Visa/Mastercard/JCB… đi qua issuer/acquirer và scheme tương ứng |
| User experience | Tap/card/mobile wallet, recurring billing phổ biến | Card + mobile banking + VietQR tạo hệ sinh thái pha trộn card và account transfer |

Không nên dùng từ “Visa xử lý toàn bộ tiền”. Visa chủ yếu cung cấp network/rules cho giao dịch thuộc scheme; tài khoản khách nằm ở issuer, merchant settlement phụ thuộc acquirer và các settlement arrangements phía dưới.

## 7. Chargeback là gì và vì sao tồn tại?

**Truy thu/hoàn trả giao dịch theo tranh chấp (chargeback / 차지백)** là quy trình đảo nghĩa vụ trong một số trường hợp: fraud, hàng không được giao, duplicate transaction hoặc merchant vi phạm rule. Nó không phải nút “refund miễn phí”. Network đặt evidence và time window; issuer, acquirer và merchant trao đổi dữ liệu theo quy trình dispute.

Chargeback cho thấy card network không chỉ truyền message mà còn là một **rule system** phân bổ rủi ro giữa các bên.

## 8. Nếu một mắt xích lỗi thì sao?

- POS mất mạng: có thể không authorization online được.
- Acquirer/VAN/gateway lỗi: nhiều merchant cùng bị ảnh hưởng dù issuer vẫn bình thường.
- Network/switching lỗi: giao dịch liên ngân hàng hoặc thuộc scheme có thể gián đoạn diện rộng.
- Issuer lỗi/risk engine từ chối: chỉ khách của issuer đó hoặc nhóm giao dịch liên quan bị ảnh hưởng.
- Settlement delay: authorization đã thành công nhưng merchant nhận tiền chậm hơn.

Mental model quan trọng:

```text
Approved ≠ settled
Payment UX ≠ payment rail
Card network ≠ bank account
```

Chapter này dựa trên [banking-system](../banking-system/README.md). Sau khi hiểu card, có thể so với [stock-market](../stock-market/README.md): cả hai đều có execution/message trước, clearing và settlement sau, nhưng tài sản và risk model rất khác.

## Nguồn chính thức tham chiếu

- Bank of Korea — Payment and Settlement Systems in Korea: https://www.bok.or.kr/eng/main/contents.do?menuNo=400349
- NAPAS — Card and switching/payment services: https://napas.com.vn/
- Visa — How VisaNet/payment processing works: https://usa.visa.com/run-your-business/small-business-tools/payment-technology/visa-network.html
