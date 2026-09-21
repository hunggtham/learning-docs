# Giám sát và Khả năng Quan sát cho Hệ thống AI

AI production cần quan sát đồng thời **hành vi hệ thống (system behavior)** và **hành vi mô hình (model behavior)**. Dịch vụ có thể trả HTTP 200 rất nhanh nhưng chất lượng dự đoán đã hỏng; ngược lại chất lượng mô hình có thể tốt nhưng độ trễ p99 không đạt SLO. Vì vậy giám sát AI phải nối kỹ thuật độ tin cậy với giám sát thống kê.

## Giám sát và Khả năng quan sát khác nhau thế nào?

**Giám sát (monitoring / 모니터링)** theo dõi các chỉ số và cảnh báo đã biết trước. **Khả năng quan sát (observability / 관측 가능성)** giúp suy ra trạng thái nội bộ từ log, metric và trace khi lỗi chưa được dự đoán trước.

## Bốn nhóm tín hiệu chính

```text
1. Hạ tầng / Hệ thống
2. Dữ liệu / Đầu vào
3. Mô hình / Đầu ra
4. Kết quả nghiệp vụ / tác vụ
```

### Chỉ số hệ thống

- tốc độ request;
- tỷ lệ lỗi;
- độ trễ p50/p95/p99;
- thời gian chờ queue;
- mức sử dụng CPU/GPU;
- bộ nhớ/KV cache;
- throughput;
- timeout/retry.

### Chỉ số dữ liệu

- vi phạm schema;
- tỷ lệ null/thiếu;
- tần suất category;
- phân phối đặc trưng;
- độ mới;
- khối lượng dữ liệu;
- lỗi parser.

### Chỉ số mô hình

- phân phối score hoặc prediction;
- confidence/calibration;
- cân bằng class;
- tỷ lệ abstention/fallback;
- độ dài output;
- tính hợp lệ của output có cấu trúc.

### Chỉ số kết quả

- thiệt hại gian lận thực tế;
- conversion;
- tỷ lệ hoàn thành tác vụ;
- tỷ lệ chuyển sang human;
- tỷ lệ người dùng sửa lại;
- tỷ lệ câu trả lời đã được xác minh.

Kết quả thường đến trễ nhưng là tín hiệu quan trọng nhất vì nó gần mục tiêu thực tế nhất.

## Metric, Log và Trace

**Metric** là chuỗi thời gian số đã được tổng hợp.

**Log** giữ chi tiết sự kiện.

**Trace phân tán (distributed trace)** nối một request xuyên qua gateway, retrieval, model, tool và database.

Workflow AI có nhiều giai đoạn nên tracing rất quan trọng để xác định độ trễ hoặc lỗi xuất phát từ component nào.

## Khả năng quan sát cho LLM

Nên theo dõi:

```text
mô hình / phiên bản
số token đầu vào/đầu ra
TTFT
TPOT
ID / score của retrieval
tool call
số bước agent
fallback
kết quả verification
ước tính chi phí
```

Prompt hoặc context có thể chứa dữ liệu nhạy cảm; không nên log nội dung thô theo mặc định. Có thể dùng redaction, hashing hoặc chính sách lấy mẫu phù hợp.

## Đo chất lượng khi chưa có Nhãn ngay lập tức

Nhiều tác vụ production không có ground truth ngay. Có thể dùng tín hiệu thay thế như:

- distribution shift;
- mẫu được human review;
- verifier check;
- kết quả nghiệp vụ;
- delayed label;
- user correction.

Proxy không nên được coi là chỉ số chất lượng thật nếu mối liên hệ với chất lượng chưa được kiểm chứng.

## Cảnh báo

Cảnh báo nên có khả năng hành động. Nếu mỗi thay đổi drift nhỏ đều gửi cảnh báo, nhóm sẽ rơi vào mệt mỏi cảnh báo (alert fatigue).

Ví dụ:

```text
p99 latency > SLO trong 15 phút
tỷ lệ lỗi schema > ngưỡng
retrieval empty-rate tăng đột biến
invalid JSON output tăng đột biến
chi phí/request tăng gấp đôi
```

## Golden Signal cho Model Serving

Có thể bắt đầu bằng:

```text
Traffic
Errors
Latency
Saturation
```

sau đó bổ sung tín hiệu mô hình và tín hiệu dữ liệu.

## Giám sát theo Slice

Chỉ số tổng hợp có thể che lỗi của một subgroup. Nên theo dõi các lát dữ liệu có ý nghĩa như vùng, thiết bị, ngôn ngữ, phân khúc khách hàng hoặc loại tài liệu.

Nhưng quá nhiều slice gây nhiễu và bài toán so sánh nhiều lần; nên chọn slice dựa trên rủi ro và use case.

## Phân phối tham chiếu

Giám sát drift cần một cửa sổ tham chiếu. Tham chiếu có thể là dữ liệu huấn luyện, validation hoặc một giai đoạn production ổn định gần đây. Mỗi lựa chọn trả lời một câu hỏi khác nhau.

## Chất lượng dữ liệu và Chất lượng mô hình

Phân phối đầu vào thay đổi không chứng minh hiệu năng mô hình đã giảm. Nhưng bất thường dữ liệu là tín hiệu chẩn đoán cần được điều tra.

## Vòng phản hồi

Output mô hình có thể làm thay đổi dữ liệu được quan sát về sau. Hệ thống gợi ý chỉ thấy click trên những item nó đã hiển thị. Vì vậy monitoring cần hiểu dữ liệu phụ thuộc policy như thế nào.

## SLO, SLA và Error Budget

SLO là mục tiêu nội bộ, SLA là cam kết với bên ngoài. Ngân sách lỗi (error budget) định lượng mức failure hệ thống chấp nhận được.

Quality SLO của AI khó định nghĩa hơn latency SLO vì nhãn có thể đến trễ hoặc mang tính chủ quan, nhưng vẫn cần contract đo được.

## Khả năng quan sát về Chi phí

Nên quy chi phí theo:

```text
mô hình
feature / workflow
tenant
loại request
agent / tool
```

Nếu chỉ nhìn hóa đơn hàng tháng, rất khó biết phần nào cần tối ưu.

## Khả năng quan sát có nhận thức về Quyền riêng tư

Log cũng là một kho dữ liệu. Cần retention, kiểm soát truy cập, mã hóa và redaction. Prompt hoặc kết quả tool nhạy cảm không nên bị sao chép vô hạn vào trace.

## Ví dụ điều tra Incident

Triệu chứng: chất lượng câu trả lời giảm.

Có thể kiểm tra lần lượt:

```text
phiên bản mô hình có đổi không?
retrieval empty rate có tăng không?
index có bị cũ không?
phiên bản prompt có đổi không?
tool có lỗi không?
phân phối ngôn ngữ đầu vào có shift không?
timeout có khiến hệ thống fallback không?
```

Khả năng quan sát cho phép lần theo chuỗi nguyên nhân thay vì đoán mò.

## Mô hình tư duy

```text
Giám sát cho biết có gì đó đang sai.
Khả năng quan sát giúp giải thích sai ở đâu và vì sao.
```

## Những nhầm lẫn thường gặp

### “HTTP success nghĩa là AI success”

Không. Sức khỏe dịch vụ không đồng nghĩa độ đúng của tác vụ.

### “Log toàn bộ prompt để debug cho dễ”

Không nên mặc định như vậy vì rủi ro quyền riêng tư và bảo mật lớn.

### “Drift metric tăng thì retrain ngay”

Không. Drift cần được diễn giải cùng kết quả và hiệu năng.

## Liên kết kiến thức

Xem [Drift and Retraining](./07_drift_and_retraining.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md), [Latency/Cost](../15_ai_engineering/09_latency_throughput_and_cost.md) và [Evaluation Layer](../18_evaluation_reliability_interpretability/README.md).