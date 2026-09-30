# Stock Market — bấm Buy rồi điều gì thực sự xảy ra?

Ứng dụng chứng khoán thường làm một thị trường cực kỳ phức tạp trông giống nút `BUY`. Nhưng lệnh phải đi qua broker, kiểm tra risk, vào venue giao dịch, được khớp với lệnh đối ứng, rồi còn bù trừ (clearing / 청산), quyết toán (settlement / 결제), lưu ký (depository / 예탁) và cập nhật quyền sở hữu. Chapter này tập trung vào plumbing của thị trường, không vào việc chọn cổ phiếu.

## 1. Execution không phải settlement

```text
Investor
   ↓ order
Broker / securities company
   ↓ validation + routing
Exchange matching engine
   ↓
Trade executed
   ↓
Clearing / CCP
   ↓ obligations calculated
Settlement system + depository
   ↓ cash ↔ securities
Investor position finalized
```

**Khớp lệnh (execution / 체결)** là lúc buyer và seller đạt giao dịch theo rule của exchange. **Bù trừ (clearing / 청산)** tính nghĩa vụ phải giao chứng khoán và tiền. **Quyết toán (settlement / 결제)** hoàn tất giao tài sản đối ứng. Vì các bước không nhất thiết xảy ra cùng một thời điểm, hệ thống phải quản trị rủi ro một bên vỡ nợ trong khoảng giữa trade và settlement.

## 2. Order book hoạt động ra sao?

Trong thị trường sổ lệnh giới hạn (limit order book / 지정가 주문장), buy orders xếp theo giá cao trước rồi time priority; sell orders xếp giá thấp trước. Matching engine không “định giá công ty”; nó áp rule để ghép các lệnh tương thích.

```text
SELL
101.0   300 shares
100.5   500 shares   ← best ask
-------------------
100.0   400 shares   ← best bid
 99.5   800 shares
BUY
```

Market order ưu tiên thực hiện nhưng chấp nhận giá đang có; limit order kiểm soát giá nhưng có thể không khớp. Spread giữa best bid và best ask là một phần của chi phí giao dịch và phản ánh liquidity tức thời.

## 3. Korea: KRX, KSD và securities companies

Korea Exchange (KRX / 한국거래소) vận hành các thị trường gồm KOSPI, KOSDAQ và các market/segments liên quan. Công ty chứng khoán nhận lệnh từ investor và kết nối vào exchange. Sau execution, KRX thực hiện chức năng clearing/central counterparty trong các thị trường thuộc phạm vi; Korea Securities Depository (KSD / 한국예탁결제원) là hạ tầng lưu ký/chứng khoán và tham gia chuỗi settlement tương ứng.

```text
Korean investor
   ↓
Securities company
   ↓
KRX KOSPI / KOSDAQ matching
   ↓
KRX clearing / CCP
   ↓
Cash settlement + KSD securities settlement
   ↓
Custody / investor account records
```

CCP đứng giữa buyer và seller bằng cơ chế novation theo rule phù hợp: buyer đối mặt CCP thay vì trực tiếp với seller, giúp tập trung quản trị counterparty risk nhưng đồng thời đòi hỏi margin, default fund và risk controls chặt chẽ.

## 4. Việt Nam: VNX, HOSE, HNX và VSDC

Sở Giao dịch Chứng khoán Việt Nam (Vietnam Exchange, VNX) là công ty mẹ của HOSE và HNX. HOSE là venue chủ yếu cho cổ phiếu niêm yết quy mô lớn; HNX vận hành thị trường cổ phiếu niêm yết của mình, UPCoM và các phân khúc/sản phẩm được giao. Tổng công ty Lưu ký và Bù trừ Chứng khoán Việt Nam (VSDC) thực hiện đăng ký, lưu ký, bù trừ và quyết toán theo khuôn khổ thị trường.

```text
Vietnamese investor
   ↓
Securities company
   ↓
HOSE / HNX trading system
   ↓
Trade result
   ↓
VSDC clearing / settlement infrastructure
   ↓
Cash ↔ securities
   ↓
Investor custody position
```

Việc VNX làm công ty mẹ không có nghĩa mọi lệnh đi qua một matching engine tên “VNX”. Cần phân biệt tầng holding/governance với trading venue thực tế là HOSE/HNX.

## 5. Delivery versus Payment

Nguyên tắc **giao chứng khoán đồng thời với nhận tiền (Delivery versus Payment, DvP / 증권대금동시결제)** giảm rủi ro principal: bên bán không muốn giao chứng khoán nếu bên mua chưa trả tiền, và bên mua không muốn trả tiền nếu chứng khoán chưa được giao. Settlement infrastructure phối hợp hai leg để giảm khoảng trống này.

Từng thị trường có settlement cycle và cut-off cụ thể; đây là rule có thể thay đổi, vì vậy chapter này không coi một ký hiệu như `T+2` là chân lý vĩnh viễn. Khi thực hiện giao dịch thật, phải kiểm tra rule hiện hành của KRX/KSD hoặc HOSE/HNX/VSDC và broker.

## 6. Hàn Quốc ↔ Việt Nam

| Lớp | Hàn Quốc | Việt Nam |
|---|---|---|
| Exchange group/venue | KRX trực tiếp vận hành KOSPI, KOSDAQ và các market liên quan | VNX ở tầng công ty mẹ; HOSE và HNX là trading venues |
| Clearing | KRX có CCP/clearing functions cho các market thuộc phạm vi | VSDC đảm nhiệm clearing/settlement functions theo cấu trúc thị trường Việt Nam |
| Depository | KSD | VSDC |
| Broker access | Securities companies thành viên | Công ty chứng khoán thành viên |
| Market maturity | Institutional/derivatives/market infrastructure phát triển sâu | Thị trường đang nâng cấp infrastructure, sản phẩm và cơ chế access |
| Foreign-investor concerns | FX, custody, tax, market rules | Foreign ownership, prefunding/settlement rules theo từng giai đoạn, FX/custody và market-access rules cần kiểm tra hiện hành |

## 7. Giá giảm mạnh không có nghĩa “exchange mất tiền”

Exchange chủ yếu cung cấp venue, rule và market infrastructure. Investor chịu mark-to-market loss trên vị thế; broker chịu exposure nếu cấp margin; CCP/custodian quản lý các loại risk khác. Phân biệt actor giúp tránh câu kiểu “sàn chứng khoán trả tiền cho người bán”. Tiền thực sự chạy qua settlement banks và clearing arrangements, còn exchange/matching engine xác định trade.

## 8. Circuit breaker, price limit và halt giải quyết gì?

Khi biến động cực lớn hoặc hệ thống có vấn đề, market có thể dùng price limits, volatility interruption, trading halt hoặc circuit breaker tùy rule. Mục tiêu không phải bảo đảm giá không giảm mà là tạo thời gian hấp thụ thông tin, hạn chế feedback loop cực đoan hoặc bảo vệ market integrity.

Thiết kế Hàn Quốc và Việt Nam không giống nhau hoàn toàn; các biên độ và trigger là rule time-sensitive, vì vậy nên học **chức năng** trước rồi tra rule hiện hành khi giao dịch.

## 9. Boundary với Investing

[`../../investing/06_markets_korea_vietnam/`](../../investing/06_markets_korea_vietnam/README.md) sở hữu phân tích thị trường Hàn Quốc–Việt Nam cho nhà đầu tư: ngành, FX, access, custody, valuation và portfolio. Chapter hiện tại chỉ sở hữu plumbing từ order tới settlement.

Một connection hữu ích là [credit-card-network](../credit-card-network/README.md): cả card và securities đều có message/execution ở trước, clearing ở giữa và settlement ở sau. Sự khác nhau là chứng khoán cần đồng bộ hai tài sản — cash và security — còn card payment chủ yếu xử lý nghĩa vụ thanh toán merchant/cardholder.

## Nguồn chính thức tham chiếu

- Korea Exchange — Market / clearing information: https://global.krx.co.kr/
- Korea Securities Depository: https://www.ksd.or.kr/
- Vietnam Exchange: https://vnx.vn/
- HOSE: https://www.hsx.vn/
- HNX: https://www.hnx.vn/
- VSDC: https://www.vsd.vn/
