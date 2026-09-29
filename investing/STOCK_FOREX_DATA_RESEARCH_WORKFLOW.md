# Quy trình dữ liệu và nghiên cứu — Cổ phiếu / Forex

> Mục tiêu của quy trình này là biết **mình biết gì, biết từ khi nào và còn thiếu gì**. Một con số chính xác nhưng đã cũ hoặc bị dùng sai thời điểm vẫn có thể dẫn tới quyết định sai.

Đây là checklist nhập môn cho một nghiên cứu cổ phiếu/Forex. Quy trình vận hành chuyên sâu theo thị trường nằm ở [Market Research Workflow](./06_markets_korea_vietnam/04_MARKET_RESEARCH_WORKFLOW_DATA_SOURCES_AND_SECTOR_MAPS.md); phần kiểm soát bias và backtest nằm ở [Systematic Risk, Backtest & Execution](./05_trading_derivatives/02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md).

## 1. Bắt đầu bằng câu hỏi, không bắt đầu bằng mã

Một nghiên cứu tốt bắt đầu bằng câu hỏi có thể bị bác bỏ, không phải bằng ticker hoặc biểu đồ đang gây chú ý. Phần này giúp người mới viết rõ cơ chế cần kiểm tra trước khi gom dữ liệu.

Viết câu hỏi trước khi mở biểu đồ hoặc đọc tin:

```text
Tôi đang muốn kiểm tra cơ chế nào?
Dữ liệu nào có thể xác nhận?
Dữ liệu nào có thể bác bỏ?
Khoảng thời gian nào phù hợp?
```

Ví dụ tốt:

```text
KRW yếu có thực sự cải thiện FCF của doanh nghiệp xuất khẩu này không?
```

Ví dụ quá rộng:

```text
KRW sắp tăng hay giảm?
```

Câu hỏi tốt đã chỉ ra biến, cơ chế và đối tượng; từ đó ta mới chọn được thứ bậc nguồn phù hợp để trả lời.

## 2. Thứ bậc nguồn dữ liệu

Sau khi có câu hỏi, bước kế tiếp là quyết định bằng chứng nào đủ mạnh. Cổ phiếu và Forex có nguồn gốc khác nhau, nhưng cùng một nguyên tắc: nguồn thứ cấp chỉ mở câu hỏi, còn kết luận phải truy ngược về dữ liệu gốc.

### Cổ phiếu

Ưu tiên theo thứ tự:

1. Báo cáo và công bố của cơ quan quản lý hoặc sở giao dịch.
2. Báo cáo tài chính, thuyết minh, tài liệu nhà đầu tư và earnings release của doanh nghiệp.
3. Dữ liệu giá, khối lượng, cổ phiếu lưu hành và corporate action từ nguồn thị trường đáng tin.
4. Transcript, khảo sát ngành và dữ liệu nhà cung cấp để kiểm tra chéo.
5. Báo chí hoặc bình luận thị trường chỉ dùng để phát hiện câu hỏi, không dùng làm bằng chứng duy nhất.

### Forex

Ưu tiên theo thứ tự:

1. Ngân hàng trung ương và cơ quan thống kê chính thức.
2. Lịch công bố, tài liệu chính sách và dữ liệu lãi suất/lợi suất chính thức.
3. Contract specification, spread, financing và margin rule của sản phẩm/broker cụ thể.
4. Dữ liệu giá/forward/volatility từ nguồn có phương pháp rõ ràng.
5. Tin tức và bình luận chỉ dùng để tạo giả thuyết rồi kiểm tra bằng dữ liệu gốc.

Nguồn thứ cấp có thể giúp tìm nhanh, nhưng phải truy ngược về nguồn gốc trước khi đưa số vào mô hình.

Thứ bậc nguồn chưa đủ nếu trộn sai thời điểm. Vì vậy, phần tiếp theo tách năm mốc để tránh look-ahead và revision bias.

## 3. Năm mốc thời gian không được trộn lẫn

Một con số có thể đúng nhưng chưa được thị trường biết tại thời điểm ra quyết định. Năm mốc dưới đây tạo timeline tối thiểu để phân biệt dữ liệu quan sát, ngày công bố, revision và thời điểm khớp lệnh.

```text
Observation time   = dữ liệu mô tả giai đoạn nào?
Publication time    = thị trường biết lúc nào?
Revision time      = số liệu bị sửa lúc nào?
Decision time      = bạn thực sự dùng thông tin lúc nào?
Execution time     = lệnh được khớp lúc nào?
```

Nếu backtest dùng số liệu sau khi đã được sửa, hoặc dùng báo cáo chỉ công bố sau thời điểm vào lệnh, kết quả có thể chứa look-ahead bias.

Khi timeline đã rõ, hãy lưu mỗi dữ liệu quan trọng vào một sổ bằng chứng có thể tái lập.

## 4. Sổ bằng chứng tối thiểu

Sổ bằng chứng biến một con số thành một claim có nguồn, thời điểm và vai trò. Bảng dưới đây là cấu trúc tối thiểu để người khác có thể kiểm tra bạn đã dùng fact, input hay assumption nào.

Mỗi dữ liệu quan trọng nên có một dòng:

| Trường | Nội dung cần ghi |
|---|---|
| Tên biến | Ví dụ: diluted shares, CPI core, 2Y yield |
| Giá trị | Con số và đơn vị |
| Observation period | Tháng/quý/ngày nào |
| Publication time | Ngày giờ công bố, nếu có |
| Revision | Có sửa hay không |
| Nguồn gốc | Link, tài liệu, bảng hoặc trang |
| Vai trò | Fact / input / assumption / check |
| Hạn sử dụng | Khi nào cần cập nhật lại |

Một link không có ngày tham chiếu thường chưa đủ để tái lập nghiên cứu.

Từ sổ bằng chứng, ta chọn bộ dữ liệu vừa đủ cho từng loại tài sản thay vì gom mọi thứ có thể tìm được.

## 5. Bộ dữ liệu tối thiểu cho một cổ phiếu

Bộ dữ liệu cổ phiếu đi từ economics của doanh nghiệp tới dòng tiền, bảng cân đối, số cổ phiếu và định giá. Mỗi nhóm phục vụ một câu hỏi khác nhau; thiếu một nhóm có thể làm luận điểm trông đẹp nhưng không kiểm tra được.

```text
Mô hình doanh thu: volume, ASP, mix
Biên lợi nhuận: gross margin, EBIT margin
Dòng tiền: CFO, capex, FCF
Vốn lưu động: receivables, inventory, payables
Bảng cân đối: tiền, nợ, đáo hạn, covenant
Vốn cổ phần: basic shares, diluted shares, SBC
Định giá: price, EPS/FCF, multiple, sensitivity
Exposure: ngành, quốc gia, đồng tiền, factor
```

Không cần có mọi dữ liệu trước khi bắt đầu. Nhưng phải đánh dấu rõ mục nào còn thiếu và mục thiếu đó có thể đảo chiều luận điểm hay không.

Forex có bộ biến khác vì lợi suất là quan hệ giữa hai đồng tiền và chi phí thực thi thay đổi theo sản phẩm.

## 6. Bộ dữ liệu tối thiểu cho một cặp Forex

Với Forex, hãy giữ đồng thời dữ liệu macro tương đối và thông số hợp đồng. Không có hai lớp này, câu chuyện về hướng giá dễ bị tách khỏi pip value, carry, spread và margin.

```text
Spot và cách báo giá
Relative policy path / lãi suất
Real yield và chênh lệch lợi suất
Inflation, labor, growth và surprise so với kỳ vọng
Risk sentiment / funding / dòng vốn
Forward points hoặc carry
Spread, slippage, session và event calendar
Contract size, pip value, margin, financing, stop-out
```

Không gọi một cặp tiền là “tăng vì tin X” nếu chưa kiểm tra tin đó đã khác kỳ vọng bao nhiêu và đồng tiền bên kia phản ứng ra sao.

Phần tiếp theo dùng một ví dụ timeline để cho thấy cùng một con số có thể được dùng hoặc không được dùng tùy ngày quyết định.

## 7. Ví dụ về dữ liệu đúng thời điểm

Ví dụ này nối lý thuyết timestamp với một quyết định cụ thể. Hãy đọc ba mốc như một chuỗi: observation nói dữ liệu mô tả thời gian nào, publication nói thị trường biết khi nào, revision nói phiên bản nào được phép dùng.

Giả sử một chỉ số CPI của tháng 6 được công bố ngày 10 tháng 7 và được sửa ngày 15 tháng 8:

```text
Observation: tháng 6
Known on: ngày 10 tháng 7
Revised on: ngày 15 tháng 8
```

Một quyết định ngày 5 tháng 7 không được dùng số CPI tháng 6 đã công bố ngày 10 tháng 7. Một backtest tại ngày 20 tháng 7 có thể dùng bản công bố ban đầu, nhưng phải ghi rõ có hay không dùng revision ngày 15 tháng 8.

Ví dụ này cho thấy timestamp không phải thủ tục hành chính; nó quyết định bằng chứng nào thật sự có thể dùng tại thời điểm hành động. Sau khi khóa timeline, ta chuyển sang một vòng nghiên cứu bảy bước.

## 8. Quy trình nghiên cứu 7 bước

Bảy bước là một vòng lặp, không phải checklist làm một lần rồi bỏ. Mỗi bước tạo đầu vào cho bước sau và để lại dấu vết để có thể review khi dữ kiện mới xuất hiện.

1. Viết hypothesis và điều kiện vô hiệu hóa.
2. Chọn biến cần đo, không gom mọi dữ liệu có thể tìm được.
3. Lấy nguồn gốc và ghi observation/publication time.
4. Tách fact, estimate, assumption và interpretation.
5. Tính base/bull/bear hoặc thuận lợi/cơ sở/bất lợi.
6. Kiểm tra chi phí, thanh khoản, exposure trùng lặp và dữ liệu đã pricing.
7. Ghi kết luận, dữ liệu còn thiếu và ngày review tiếp theo.

Nếu bước 3 chưa làm được, chưa nên viết con số với độ chính xác giả tạo.

Ngay cả khi đã làm đủ bảy bước, cần audit các bẫy dữ liệu phổ biến trước khi biến kết luận thành hành động.

## 9. Các bẫy dữ liệu thường gặp

Bảng này là phần đối chiếu lỗi: cột giữa giúp nhận ra dấu hiệu, cột cuối chuyển dấu hiệu thành cách xử lý. Đừng chỉ học tên bias; hãy gắn mỗi bias với một thay đổi cụ thể trong dữ liệu hoặc phương pháp.

| Bẫy | Cách nhận ra | Cách xử lý |
|---|---|---|
| Dữ liệu nhìn trước | Dùng số được sửa sau thời điểm quyết định | Lưu vintage theo ngày công bố |
| Chọn mẫu sống sót | Chỉ nhìn doanh nghiệp/cặp tiền còn tồn tại | Ghi cả mẫu thất bại hoặc thay đổi universe |
| Đổi định nghĩa | KPI cùng tên nhưng cách tính thay đổi | Đọc footnote và giữ định nghĩa theo thời gian |
| Tương quan thành nhân quả | Hai biến đi cùng nhưng không có cơ chế | Viết kênh truyền dẫn và biến phản chứng |
| Chính xác giả tạo | Dự báo nhiều chữ số hơn chất lượng dữ liệu | Dùng khoảng, sensitivity và confidence |
| Tin vào giá đóng cửa | Bỏ qua thanh khoản và giá khớp thực tế | Ghi spread, slippage, time và order type |

Sau khi xử lý bẫy, hãy ghi phiên bản mới của nghiên cứu vào nhật ký cập nhật để biết claim nào đã thay đổi.

## 10. Nhật ký cập nhật

Nhật ký là nơi nối các lần quan sát theo thời gian. Mục tiêu không phải viết dài, mà là giữ lại câu hỏi, dữ kiện mới và thay đổi trong fact/estimate/assumption để không chỉnh câu chuyện sau khi đã biết kết quả.

```text
Ngày:
Câu hỏi đang kiểm tra:
Dữ liệu mới:
Điều gì thay đổi so với lần trước:
Thay đổi ở fact, estimate hay assumption:
Luận điểm mạnh hơn, yếu hơn hay không đổi:
Quy mô / hành động có cần thay đổi không:
Ngày cần kiểm tra lại:
```

Trước khi dùng dữ liệu cho quyết định thật, chạy cổng kiểm tra cuối cùng dưới đây và dừng nếu một lớp nguồn hoặc timestamp còn thiếu.

## 11. Trước khi dùng dữ liệu cho quyết định thật

Checklist cuối cùng xác nhận nghiên cứu đã đủ nguồn, thời điểm, chi phí và điều kiện sai hay chưa. Nó không biến forecast thành sự thật; nó chỉ ngăn những lỗi có thể phát hiện trước khi hành động.

- [ ] Nguồn là nguồn gốc hoặc đã truy ngược được về nguồn gốc.
- [ ] Có ngày quan sát và ngày công bố.
- [ ] Đã kiểm tra revision và thay đổi định nghĩa.
- [ ] Đã tách số liệu lịch sử khỏi forecast.
- [ ] Đã tính chi phí, thanh khoản và độ trễ thực thi.
- [ ] Đã ghi dữ liệu nào có thể làm luận điểm sai.
- [ ] Đã kiểm tra quy định, thuế và thông số sản phẩm hiện hành.

Các quy tắc thị trường, thuế, broker và thông số sản phẩm có thể thay đổi. Trước giao dịch thật, phải xác minh lại từ nguồn chính thức hiện hành.
