# Electricity Grid — từ nhà máy điện đến ổ cắm

Điện có một tính chất làm hệ thống của nó khác hàng hóa thông thường: trong lưới xoay chiều, cung và cầu phải được cân bằng gần như liên tục. Không thể để toàn bộ điện dư vào một “kho trung tâm” rồi lấy ra sau như gạo hay container. Pin và thủy điện tích năng giúp lưu trữ một phần, nhưng vận hành hệ thống điện vẫn là bài toán cân bằng thời gian thực.

## 1. Luồng vật lý

```text
Power plant
   ↓  step-up transformer
High-voltage transmission
   ↓
Transmission substation
   ↓
Medium-voltage distribution
   ↓
Local transformer
   ↓
Low-voltage distribution
   ↓
Meter
   ↓
Home / factory
```

Máy phát điện tạo điện xoay chiều. Máy biến áp tăng áp để giảm dòng điện với cùng công suất, nhờ đó giảm tổn hao `I²R` trên đường truyền. Gần nơi tiêu thụ, các trạm biến áp hạ điện áp từng bước xuống mức phân phối và sử dụng.

Hàn Quốc dùng hệ thống điện xoay chiều 60 Hz; Việt Nam dùng 50 Hz. Tần số không chỉ là con số trên nhãn thiết bị: nó phản ánh tốc độ cân bằng giữa công suất cơ đưa vào máy phát và tải điện lấy ra khỏi lưới. Khi cung–cầu lệch, tần số bắt đầu lệch và hệ thống điều độ phải phản ứng.

## 2. Ai quyết định nhà máy nào phát?

Đây là chỗ cần tách **dòng điện vật lý** khỏi **giao dịch thị trường**. Electron không mang nhãn “điện của nhà máy A”. Hệ thống điều độ quyết định tổ máy nào chạy dựa trên nhu cầu, khả năng phát, chi phí, giới hạn truyền tải, dự phòng và an ninh hệ thống. Sau đó hệ thống đo đếm và thanh toán xác định ai được trả bao nhiêu.

### Hàn Quốc

Korea Power Exchange (KPX / 전력거래소) vận hành thị trường điện và điều độ hệ thống. Mô hình hiện hành về cốt lõi là cost-based pool: nhà máy cung cấp khả năng phát, KPX lập lịch và xác định System Marginal Price (SMP / 계통한계가격) theo quy tắc thị trường, còn KEPCO giữ vai trò người mua điện chủ yếu và là trung tâm lớn của truyền tải/phân phối/bán lẻ. KPX cũng thực hiện metering, settlement và vận hành Energy Management System.

Luồng khái niệm:

```text
Generators
   ↓ bids / availability / cost data
KPX market + dispatch
   ↓ physical electricity
Transmission grid
   ↓
KEPCO distribution / retail
   ↓
Consumers

KPX metering + settlement
   ↑                     ↓
Generators ← payment ← market settlement
```

### Việt Nam

Việt Nam vận hành thị trường bán buôn điện cạnh tranh với đơn vị vận hành hệ thống và thị trường điện, các đơn vị phát điện, đơn vị truyền tải, đơn vị bán buôn, EVN và các khách hàng lớn theo phạm vi quy định. Thông tư 29/2026/TT-BCT có hiệu lực từ 20/07/2026 tiếp tục quy định đăng ký thị trường, chào giá, lập lịch huy động, đo đếm, xác định giá và thanh toán; cơ chế mua bán điện trực tiếp cho khách hàng lớn cũng nằm trong quá trình mở rộng thị trường.

Điểm cần nắm là Việt Nam đang chuyển từ cấu trúc tích hợp mạnh sang nhiều lớp thị trường hơn, nhưng EVN và các đơn vị liên quan vẫn giữ vai trò rất lớn trong hạ tầng và cung ứng điện.

## 3. So sánh Hàn Quốc ↔ Việt Nam

| Câu hỏi | Hàn Quốc | Việt Nam |
|---|---|---|
| Đơn vị điều phối/market operator | KPX | NSMO và khuôn khổ thị trường điện theo Bộ Công Thương |
| Doanh nghiệp hạ tầng trung tâm | KEPCO cùng các công ty phát điện và đơn vị liên quan | EVN cùng các tổng công ty/đơn vị phát điện, truyền tải, phân phối |
| Cơ chế wholesale | Cost-based pool, SMP và settlement do KPX vận hành | Competitive wholesale market đang tiếp tục hoàn thiện; chào giá, huy động, giá và settlement theo quy định thị trường |
| Tần số | 60 Hz | 50 Hz |
| Áp lực hệ thống nổi bật | Mật độ tải công nghiệp/đô thị cao, nhập nhiên liệu, tích hợp renewable | Tăng nhu cầu nhanh, mở rộng truyền tải, phân bố nguồn–tải và tích hợp renewable |

Không nên suy ra giá điện hộ gia đình trực tiếp từ wholesale price. Hóa đơn cuối cùng còn chịu tariff design, chi phí mạng, thuế/phí, chính sách và phân bổ chi phí giữa nhóm khách hàng.

## 4. Vì sao renewable làm bài toán khó hơn?

Năng lượng gió và mặt trời có chi phí biên thấp nhưng biến thiên theo thời tiết. Khi tỷ trọng tăng, hệ thống cần forecast tốt hơn, transmission đủ mạnh, nguồn linh hoạt, storage, demand response và ancillary services. Một vùng có nhiều solar nhưng ít đường dây truyền tải có thể phải curtail dù tổng quốc gia vẫn cần điện ở nơi khác.

Đây là ví dụ điển hình cho khác biệt giữa **năng lượng (energy / 에너지)** và **công suất đúng thời điểm đúng vị trí (capacity / 용량)**. Có đủ kWh cả năm không có nghĩa là hệ thống luôn đủ MW vào giờ cao điểm tại node cần thiết.

## 5. Khi mất điện, lỗi có thể lan như thế nào?

Một đường dây trip làm công suất chuyển sang tuyến khác. Tuyến còn lại quá tải có thể trip tiếp. Nếu tần số hoặc điện áp vượt giới hạn, bảo vệ sẽ tách thiết bị để tránh hư hỏng. Vì vậy blackout lớn không nhất thiết bắt đầu từ việc “thiếu điện”; nó có thể bắt đầu từ sự cố truyền tải, protection hoặc mất đồng bộ rồi cascade.

Sau chapter này, [`../../electrical_engineering/`](../../electrical_engineering/README.md) là nơi đi sâu mạch điện, máy điện và hệ thống công suất; còn `how-things-work` giữ mental model vận hành thị trường–lưới end-to-end.

## Nguồn chính thức tham chiếu

- KPX — Electricity Market Trading Process: https://www.kpx.or.kr/menu.es?mid=a20201000000
- KPX — Market Price Determination: https://kpx.or.kr/menu.es?mid=a20203000000
- KPX — Settlement Process: https://www.kpx.or.kr/menu.es?mid=a20204000000
- Bộ Công Thương Việt Nam — Thông tư 29/2026/TT-BCT về thị trường bán buôn điện cạnh tranh: https://moit.gov.vn/tin-tuc/bo-cong-thuong-ban-hanh-thong-tu-moi-quy-dinh-chi-tiet-van-hanh-thi-truong-dien.html
