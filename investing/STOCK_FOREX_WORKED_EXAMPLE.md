# Hồ sơ mẫu đã điền — Cổ phiếu xuất khẩu và Forex

> Đây là hồ sơ học tập với doanh nghiệp và số liệu giả định. Mục tiêu là minh họa cách suy nghĩ, không phải khuyến nghị mua cổ phiếu hay mở vị thế Forex.

Hồ sơ này là bản điền mẫu cho [Mẫu ghi chú nghiên cứu](./STOCK_FOREX_RESEARCH_TEMPLATE.md). Sau khi hiểu cấu trúc, hãy thay toàn bộ số giả định bằng dữ liệu có vintage và nguồn rõ ràng theo [Quy trình dữ liệu và nghiên cứu](./STOCK_FOREX_DATA_RESEARCH_WORKFLOW.md), rồi nâng cấp thành [Case USD funding Hàn Quốc–Việt Nam](./07_integrated_case_studies/07_USD_FUNDING_FX_KOREA_VIETNAM_CROSS_BORDER_CASE.md).

## 1. Câu hỏi quyết định

> Nếu KRW yếu vừa phải, doanh thu USD của HanRiver Components tăng giá trị khi quy đổi sang KRW, trong khi chi phí chủ yếu bằng KRW; tuy nhiên lợi ích chỉ đáng kể nếu nợ USD, chi phí nhập khẩu, hợp đồng phòng vệ và nhu cầu khách hàng không đảo ngược tác động đó.

Luận điểm bị vô hiệu hóa nếu biên lợi nhuận giảm mạnh, volume xuất khẩu giảm, chi phí đầu vào USD tăng hoặc nợ USD tạo tổn thất lớn hơn lợi ích hoạt động.

## 2. Dữ kiện và giả định

Trước khi tính, ta phải tách dữ kiện giả định khỏi kết luận. Bảng này tạo bộ đầu vào tối thiểu; đọc từng dòng cùng với loại dữ liệu để biết con số nào chỉ phục vụ bài tập và con số nào cần nguồn khi áp dụng thật.

| Mục | Giá trị | Loại |
|---|---:|---|
| Doanh thu | 100 triệu USD | Giả định bài tập |
| Chi phí vận hành | 100 tỷ KRW | Giả định bài tập |
| Nợ | 50 triệu USD | Giả định bài tập |
| Cổ phiếu pha loãng | 10 triệu | Giả định bài tập |
| Giá cổ phiếu | 30.000 KRW | Giả định bài tập |
| Tỷ giá cơ sở | 1.300 KRW/USD | Giả định bài tập |
| Lãi suất nợ USD | 3%/năm | Giả định bài tập |
| Thuế suất hiệu dụng | 25% | Giả định bài tập |

Các số liệu trên chưa bao gồm thuế quan, chi phí hedge, vốn lưu động, capex, thay đổi giá bán, thay đổi sản lượng hoặc kế toán điều chỉnh tỷ giá. Đây là giới hạn cố ý để người học nhìn rõ cơ chế đầu tiên.

## 3. Nhánh cổ phiếu

Nhánh cổ phiếu đi theo chuỗi doanh thu quy đổi → lợi nhuận → EPS → định giá. Ta bắt đầu bằng mô hình cơ sở, sau đó thay một biến tỷ giá để thấy cơ chế và cuối cùng liệt kê dữ liệu cần kiểm tra thêm.

### 3.1 Từ doanh thu đến EPS

Phép tính dưới đây cố ý đi từng bước để người mới thấy tỷ giá đi qua doanh thu, lãi vay, thuế và số cổ phiếu như thế nào. Đây là cầu nối từ macro sang con số trên mỗi cổ phiếu.

Ở tỷ giá 1.300:

```text
Doanh thu quy đổi = 100 triệu × 1.300 = 130 tỷ KRW
Lợi nhuận vận hành = 130 - 100 = 30 tỷ KRW
Lãi vay = 50 triệu × 3% × 1.300 = 1,95 tỷ KRW
Lợi nhuận trước thuế = 28,05 tỷ KRW
Lợi nhuận ròng ≈ 28,05 × (1 - 25%) = 21,04 tỷ KRW
EPS ≈ 21,04 tỷ / 10 triệu = 2.104 KRW
P/E tại 30.000 KRW ≈ 14,3 lần
```

### 3.2 Kịch bản KRW yếu

Bây giờ chỉ thay tỷ giá, còn các giả định khác giữ nguyên để cô lập một cơ chế. Sau khi tính xong, không được gọi đó là dự báo; hãy xem nó như một counterfactual cần kiểm tra bằng dữ liệu vận hành.

Giả sử tỷ giá lên 1.430, còn doanh thu USD, chi phí KRW, volume và giá bán không đổi:

```text
Doanh thu quy đổi = 100 triệu × 1.430 = 143 tỷ KRW
Lợi nhuận vận hành = 143 - 100 = 43 tỷ KRW
Lãi vay = 50 triệu × 3% × 1.430 = 2,145 tỷ KRW
Lợi nhuận trước thuế = 40,855 tỷ KRW
Lợi nhuận ròng ≈ 40,855 × (1 - 25%) = 30,64 tỷ KRW
EPS ≈ 30,64 tỷ / 10 triệu = 3.064 KRW
P/E nếu giá vẫn 30.000 KRW ≈ 9,8 lần
```

Kết luận sơ bộ: trong mô hình đơn giản, EPS tăng khoảng 46%, nhưng giá cổ phiếu chưa chắc tăng. Thị trường có thể đã dự đoán KRW yếu; đồng thời nhà đầu tư có thể lo rằng lợi ích này ngắn hạn hoặc bị bù bởi chi phí khác.

### 3.3 Bảng biến số cần kiểm tra thêm

Mô hình đơn giản vừa cho ta hướng tác động, nhưng chưa chứng minh độ lớn. Bảng này chỉ ra từng biến có thể làm kết luận đảo chiều và loại dữ liệu cần tìm để kiểm tra nó.

| Biến số | Vì sao quan trọng | Dữ liệu cần tìm |
|---|---|---|
| Tỷ lệ doanh thu USD | Xác định exposure translation | Thuyết minh doanh thu theo khu vực/tiền tệ |
| Chi phí USD | Có thể bù trừ doanh thu USD | Nguyên liệu, logistics, capex |
| Nợ USD | Làm tăng nghĩa vụ khi KRW yếu | Lịch đáo hạn, lãi suất, covenant |
| Hedge | Giảm cả lãi và lỗ tỷ giá | Notional, kỳ hạn, giá forward |
| Volume/ASP | KRW yếu có thể đi kèm cầu yếu | Đơn hàng, giá bán, tồn kho |
| Pha loãng | Quyết định EPS trên mỗi cổ phiếu | SBC, option, phát hành mới |

## 4. Nhánh Forex

Nhánh Forex tách riêng bài toán sizing vì cùng một luận điểm đúng vẫn có thể tạo trade sai nếu quy mô, spread và financing làm lỗ all-in vượt risk budget.

Để luyện cơ chế sizing riêng, giả sử một paper trade EUR/USD:

```text
Equity: 5.000 USD
Rủi ro tối đa: 0,5% = 25 USD
Vị thế: 10.000 EUR/USD
Giá trị gần đúng: 1 USD/pip
Stop: 25 pip
Spread: 1,2 pip
```

```text
Lỗ tại stop ≈ 25 × 1 = 25 USD
Chi phí spread ≈ 1,2 × 1 = 1,2 USD
Rủi ro trước slippage/financing ≈ 26,2 USD
Tỷ lệ trên equity ≈ 26,2 / 5.000 = 0,524%
```

Vì rủi ro all-in đã vượt 0,5%, có ba lựa chọn hợp lý trong bài tập:

Các lựa chọn dưới đây là cách phản ứng với risk budget, không phải danh sách mẹo vào lệnh. Hãy chọn theo dữ liệu chi phí và event risk đã có, không theo mong muốn giữ nguyên notional.

1. Giảm quy mô vị thế.
2. Tăng khoảng cách stop nhưng giảm quy mô tương ứng.
3. Không giao dịch nếu spread, slippage hoặc event risk không thể ước lượng.

Không được giải quyết vấn đề bằng cách tăng leverage. Leverage chỉ làm yêu cầu margin nhỏ hơn.

## 5. Kịch bản và hành động

Sau hai nhánh tính riêng, bảng này đặt các điều kiện vào cùng một khung quyết định. Mỗi dòng phải trả lời đủ cơ chế, tác động và hành động học tập; nếu thiếu một cột, kịch bản chưa thể dùng để review.

| Kịch bản | Cơ chế | Tác động có thể có | Hành động học tập |
|---|---|---|---|
| Cơ sở | KRW ổn định, volume giữ nguyên | EPS gần mô hình cơ sở | Theo dõi doanh thu, margin, nợ |
| Thuận lợi | KRW yếu, chi phí KRW ổn định, hedge vừa phải | EPS tăng, P/E giảm nếu giá chưa đổi | Kiểm tra thị trường đã pricing chưa |
| Bất lợi | KRW yếu nhưng cầu giảm, chi phí USD tăng | Margin co, lợi ích FX mất | Giảm độ tin cậy luận điểm |
| Stress | Gap tỷ giá, spread tăng, thanh khoản giảm | Hedge/trade khó thoát đúng giá | Không tăng vị thế; dùng kill switch |

## 6. Điều kiện vô hiệu hóa

Đây là phần bảo vệ bài tập khỏi việc biến mô hình thành niềm tin. Các điều kiện dưới đây nói rõ bằng chứng nào khiến ta giảm độ tin cậy hoặc loại bỏ luận điểm, kể cả khi giá vẫn đang đi theo hướng thuận lợi.

```text
1. Doanh thu USD thực tế thấp hơn đáng kể so với giả định.
2. Chi phí USD hoặc giá nguyên liệu tăng gần bằng mức tăng doanh thu quy đổi.
3. Volume hoặc ASP giảm đủ lớn để xóa lợi ích tỷ giá.
4. Nợ USD / hedge tạo lỗ lớn hơn lợi ích hoạt động.
5. EPS tăng nhưng CFO/FCF không tăng.
6. Giá cổ phiếu đã phản ánh toàn bộ lợi ích trước khi dữ liệu xác nhận.
```

## 7. Review sau bài tập

Review khép vòng học bằng cách tách điều đã hiểu, biến còn thiếu và phần chỉ là minh họa. Mục tiêu là biết lần sau phải cải thiện dữ liệu hay cơ chế, không phải làm cho kết quả cũ trông đẹp hơn.

```text
Điều đã hiểu rõ hơn:
Biến số còn thiếu:
Giả định nhạy cảm nhất:
Phần tính toán nào chỉ là minh họa:
Thông tin nào cần nguồn chính thức trước khi dùng thật:
```

### Bài học chính

Một biến vĩ mô như tỷ giá không đi thẳng vào giá cổ phiếu. Nó đi qua doanh thu, chi phí, nợ, hedge, thuế, dòng tiền, EPS, kỳ vọng và định giá. Với Forex, cùng một luận điểm còn phải đi qua quy mô, spread, slippage, financing, margin và khả năng sống sót của tài khoản.
