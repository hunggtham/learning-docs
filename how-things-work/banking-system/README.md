# Banking System — tiền trong tài khoản thực sự di chuyển như thế nào?

Khi ứng dụng ngân hàng hiển thị “10.000.000 VND” hay “1.000.000 KRW”, màn hình không chứa tiền. Nó hiển thị một khoản nợ của ngân hàng đối với người gửi tiền. Để hiểu hệ thống ngân hàng, cần tách ba lớp thường bị trộn vào nhau: **sổ cái của từng ngân hàng (bank ledger / 은행 원장)**, **thanh toán giữa các ngân hàng (interbank payment / 은행간 지급결제)** và **tiền ngân hàng trung ương (central-bank money / 중앙은행 화폐)** dùng để quyết toán cuối cùng giữa các tổ chức.

## 1. Một khoản chuyển tiền nội bộ khác chuyển liên ngân hàng thế nào?

Nếu A và B cùng dùng một ngân hàng, giao dịch có thể chỉ là hai bút toán trên cùng sổ cái:

```text
A account  -100
B account  +100
```

Không cần tiền chạy qua ngân hàng trung ương. Nhưng nếu A ở Bank X và B ở Bank Y, Bank X phải giảm nghĩa vụ với A, Bank Y tăng nghĩa vụ với B, đồng thời hai ngân hàng phải giải quyết nghĩa vụ với nhau qua hạ tầng thanh toán.

```text
Customer A
   ↓ payment instruction
Bank X
   ↓ clearing / payment message
Interbank payment system
   ↓
Bank Y
   ↓
Customer B

Bank X reserves  ─────→  Bank Y reserves
          settlement in central-bank money
```

**Bù trừ (clearing / 청산)** xác định ai nợ ai và bao nhiêu. **Quyết toán (settlement / 결제)** là lúc tài sản thanh toán thực sự được chuyển để nghĩa vụ hoàn tất. Một hệ thống bán lẻ có thể gom hàng triệu giao dịch rồi chỉ quyết toán phần ròng; hệ thống giá trị lớn thường ưu tiên quyết toán theo thời gian thực từng giao dịch để giảm rủi ro.

## 2. Ngân hàng tạo tiền bằng cách nào?

Một ngộ nhận phổ biến là ngân hàng chỉ lấy tiền tiết kiệm của A rồi cho B vay nguyên số đó. Thực tế, khi ngân hàng phê duyệt khoản vay 100 triệu và ghi có tài khoản người vay 100 triệu, nó đồng thời tạo:

```text
Tài sản ngân hàng:   +100 triệu khoản cho vay
Nợ phải trả:         +100 triệu tiền gửi của khách hàng
```

Tiền gửi ngân hàng thương mại (commercial-bank money / 상업은행 화폐) mới được tạo trong hệ thống sổ cái. Nhưng ngân hàng không thể cho vay vô hạn: vốn tự có, rủi ro tín dụng, nhu cầu vay, thanh khoản, quy định an toàn, chi phí vốn và khả năng quyết toán với ngân hàng khác đều tạo ràng buộc.

Nếu người vay chuyển 100 triệu sang ngân hàng khác, ngân hàng cho vay có thể phải chuyển dự trữ hoặc huy động nguồn thanh khoản để hoàn tất settlement. Vì vậy **solvency** và **liquidity** là hai bài toán khác nhau: ngân hàng có tài sản tốt dài hạn vẫn có thể gặp khủng hoảng thanh khoản nếu nhiều nghĩa vụ ngắn hạn đến cùng lúc.

## 3. Ngân hàng trung ương đứng ở đâu?

Ngân hàng trung ương không xử lý từng hóa đơn cà phê của người dân theo kiểu một ngân hàng bán lẻ. Nó cung cấp lớp tiền và thanh toán cốt lõi cho hệ thống tài chính, thực thi chính sách tiền tệ và hỗ trợ ổn định hệ thống theo mandate của từng nước.

### Hàn Quốc

Ngân hàng Trung ương Hàn Quốc (Bank of Korea, BOK / 한국은행) vận hành BOK-Wire+, hệ thống thanh toán giá trị lớn dùng tiền ngân hàng trung ương. Korea Financial Telecommunications & Clearings Institute (KFTC / 금융결제원) vận hành nhiều hạ tầng thanh toán bán lẻ liên ngân hàng. Financial Services Commission (FSC / 금융위원회) phụ trách chính sách và khuôn khổ tài chính; Financial Supervisory Service (FSS / 금융감독원) thực hiện giám sát; Korea Deposit Insurance Corporation (KDIC / 예금보험공사) phụ trách cơ chế bảo hiểm tiền gửi theo phạm vi luật định.

Luồng đơn giản hóa:

```text
Households / firms
      ↓
Commercial & specialized banks
      ↓ retail clearing, transfers
KFTC and other payment infrastructures
      ↓ settlement obligations
BOK-Wire+
      ↓
Central-bank money
```

### Việt Nam

Ngân hàng Nhà nước Việt Nam (State Bank of Vietnam, SBV / 베트남 국가은행) là ngân hàng trung ương và cơ quan quản lý tiền tệ – ngân hàng. Hệ thống thanh toán điện tử liên ngân hàng và các hạ tầng do SBV quản lý tạo lớp quyết toán quan trọng; NAPAS cung cấp chuyển mạch, bù trừ và kết nối thanh toán bán lẻ giữa nhiều ngân hàng và trung gian. Bảo hiểm Tiền gửi Việt Nam (Deposit Insurance of Vietnam) phụ trách bảo hiểm tiền gửi theo phạm vi pháp luật.

```text
Households / firms
      ↓
Commercial banks
      ↓ transfers / cards / QR
NAPAS + bank payment rails
      ↓ interbank obligations
SBV payment / settlement infrastructure
      ↓
Central-bank money
```

## 4. Hàn Quốc ↔ Việt Nam: chức năng giống, cấu trúc khác

| Câu hỏi | Hàn Quốc | Việt Nam |
|---|---|---|
| Ngân hàng trung ương | BOK | SBV |
| Hạ tầng retail interbank nổi bật | KFTC và các hệ thống thanh toán tư nhân/chuyên ngành | NAPAS và hệ thống ngân hàng/thanh toán do SBV quản lý |
| Large-value settlement | BOK-Wire+ | Hạ tầng thanh toán liên ngân hàng của SBV |
| Cấu trúc ngân hàng | Ngân hàng thương mại, ngân hàng chuyên biệt, internet-only banks và tổ chức tài chính phi ngân hàng phát triển sâu | Ngân hàng thương mại nhà nước/cổ phần, ngân hàng nước ngoài và hệ sinh thái fintech đang mở rộng nhanh |
| Điểm trải nghiệm người dùng | Chuyển khoản tức thời, hệ sinh thái tài khoản/thẻ số hóa rất sâu | Mobile banking, QR và chuyển khoản nhanh phát triển mạnh; NAPAS tạo interoperability quan trọng |

Sự khác nhau ở giao diện không thay đổi nguyên lý: cuối cùng mỗi giao dịch phải được ghi trên các ledger nhất quán và nghĩa vụ liên ngân hàng phải được settlement bằng một tài sản mà hai bên cùng chấp nhận.

## 5. Tại sao một ngân hàng có thể “thiếu tiền” dù tài sản lớn hơn nợ?

Giả sử ngân hàng có khoản vay mua nhà kỳ hạn 20 năm nhưng khách hàng gửi tiền có thể rút ngay. Đây là **chuyển đổi kỳ hạn (maturity transformation / 만기 변환)**. Bình thường, tiền gửi vào–ra phân tán và ngân hàng quản trị thanh khoản bằng dự trữ, thị trường liên ngân hàng, tài sản thanh khoản và nguồn vốn khác. Khi rất nhiều người muốn rút cùng lúc, tài sản dài hạn không thể lập tức biến thành cash mà không bán hoặc thế chấp.

Đó là lý do ngân hàng trung ương, bảo hiểm tiền gửi, quy định vốn và liquidity regulation cùng tồn tại nhưng giải quyết các failure mode khác nhau.

## 6. Lãi suất chính sách truyền tới bạn bằng con đường nào?

Một thay đổi lãi suất chính sách không trực tiếp sửa con số trên mọi hợp đồng vay. Nó đi qua chuỗi:

```text
Central-bank policy
      ↓
Short-term money-market rates
      ↓
Banks' funding cost + liquidity
      ↓
Deposit / loan pricing
      ↓
Household & company borrowing
      ↓
Spending / investment / asset prices
      ↓
Inflation and economic activity
```

Mức truyền dẫn khác nhau giữa Hàn Quốc và Việt Nam vì cấu trúc funding, tỷ lệ lãi suất cố định/thả nổi, vai trò ngân hàng trong nền kinh tế, thị trường trái phiếu và cách điều hành chính sách khác nhau.

## 7. Boundary với economics và investing

Chapter này chỉ trả lời “hệ thống ngân hàng chạy bằng ledger, clearing, settlement và liquidity như thế nào”. Cơ chế chính sách tiền tệ tổng quát thuộc [`../../economics/`](../../economics/README.md); phân tích ngân hàng như một doanh nghiệp, NIM, NPL, capital adequacy và tác động lên danh mục đầu tư thuộc [`../../investing/`](../../investing/README.md).

Tiếp theo, [credit-card-network](../credit-card-network/README.md) phóng to một trường hợp cụ thể: một cú chạm thẻ tạo ra hai chuỗi khác nhau — authorization trong vài giây và settlement sau đó.

## Nguồn chính thức tham chiếu

- Bank of Korea — Payment and Settlement Systems in Korea: https://www.bok.or.kr/eng/main/contents.do?menuNo=400349
- Bank of Korea — Financial System in Korea: https://www.bok.or.kr/eng/main/contents.do?menuNo=400084
- State Bank of Vietnam — Functions and responsibilities: https://www.sbv.gov.vn/
- NAPAS — Services and payment infrastructure: https://napas.com.vn/
