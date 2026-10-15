# Giám sát và Khả năng Quan sát cho Hệ thống AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Monitoring và observability cho hệ thống AI**. Route đi từ service/quality/feature signals → traces and logs → dashboards/alerts → slice and cohort analysis → actionable response, để quan sát nối tín hiệu với quyết định vận hành.

AI môi trường vận hành (production / 운영 환경) cần quan sát đồng thời **hành vi hệ thống (system behavior)** và **hành vi mô hình (model behavior)**. Dịch vụ có thể trả HTTP 200 rất nhanh nhưng chất lượng dự đoán đã hỏng; ngược lại chất lượng mô hình có thể tốt nhưng độ trễ p99 không đạt SLO. Vì vậy giám sát AI phải nối kỹ thuật độ tin cậy với giám sát thống kê.

## Giám sát và Khả năng quan sát khác nhau thế nào?

**Giám sát (monitoring / 모니터링)** theo dõi các chỉ số và cảnh báo đã biết trước. **khả năng quan sát (observability / 관측 가능성)** giúp suy ra trạng thái nội bộ từ log, chỉ số (metric / 지표) và dấu vết (trace / 추적) khi lỗi chưa được dự đoán trước.

Bốn nhóm tín hiệu trên tạo thành khung để đọc hệ thống từ hạ tầng đến kết quả nghiệp vụ. Phần kế tiếp đi vào cách thu thập và nối các tín hiệu đó.

## Bốn nhóm tín hiệu chính

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
1. Hạ tầng / Hệ thống
2. Dữ liệu / Đầu vào
3. Mô hình / Đầu ra
4. Kết quả nghiệp vụ / tác vụ
```

### Chỉ số hệ thống

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

- tốc độ request;
- tỷ lệ lỗi;
- độ trễ p50/p95/p99;
- thời gian chờ hàng đợi (queue / 큐);
- mức sử dụng CPU/GPU;
- bộ nhớ/KV bộ nhớ đệm (cache / 캐시);
- thông lượng (throughput / 처리량);
- hết thời gian chờ (timeout / 타임아웃)/thử lại (retry / 재시도).

### Chỉ số dữ liệu

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

- vi phạm schema;
- tỷ lệ null/thiếu;
- tần suất category;
- phân phối đặc trưng;
- độ mới;
- khối lượng dữ liệu;
- lỗi parser.

### Chỉ số mô hình

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

- phân phối score hoặc prediction;
- confidence/calibration;
- cân bằng lớp (class / 클래스);
- tỷ lệ abstention/fallback;
- độ dài đầu ra (output / 출력);
- tính hợp lệ của đầu ra (output / 출력) có cấu trúc.

### Chỉ số kết quả

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

- thiệt hại gian lận thực tế;
- conversion;
- tỷ lệ hoàn thành tác vụ;
- tỷ lệ chuyển sang human;
- tỷ lệ người dùng sửa lại;
- tỷ lệ câu trả lời đã được xác minh.

Kết quả thường đến trễ nhưng là tín hiệu quan trọng nhất vì nó gần mục tiêu thực tế nhất.

Các tín hiệu này cần được thu thập bằng metric, log và trace để có thể điều tra nguyên nhân thay vì chỉ nhìn triệu chứng.

## Chỉ số (metric / 지표), Log và dấu vết (trace / 추적)

**chỉ số (metric / 지표)** là chuỗi thời gian số đã được tổng hợp.

**Log** giữ chi tiết sự kiện.

**dấu vết (trace / 추적) phân tán (distributed trace)** nối một yêu cầu (request / 요청) xuyên qua gateway, retrieval, mô hình (model / 모델), công cụ (tool / 도구) và cơ sở dữ liệu (database / 데이터베이스).

Workflow AI có nhiều giai đoạn nên tracing rất quan trọng để xác định độ trễ hoặc lỗi xuất phát từ thành phần (component / 컴포넌트) nào.

Với LLM, các tín hiệu kỹ thuật cần thêm ngữ cảnh về token, retrieval và tool call. Khi nhãn chưa đến ngay, ta cần các proxy có giới hạn rõ ràng để theo dõi chất lượng.

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

Prompt hoặc ngữ cảnh (context / 맥락) có thể chứa dữ liệu nhạy cảm; không nên log nội dung thô theo mặc định. Có thể dùng redaction, hashing hoặc chính sách lấy mẫu phù hợp.

Khi nhãn chưa đến ngay, những proxy này chỉ hữu ích nếu được gắn với ngưỡng và hành động cụ thể; đó là vai trò của cảnh báo.

## Đo chất lượng khi chưa có Nhãn ngay lập tức

Nhiều tác vụ môi trường vận hành (production / 운영 환경) không có ground truth ngay. Có thể dùng tín hiệu thay thế như:

- phân phối (distribution / 분포) shift;
- mẫu được human rà soát (review / 검토);
- verifier check;
- kết quả nghiệp vụ;
- delayed label;
- người dùng (user / 사용자) correction.

Proxy không nên được coi là chỉ số chất lượng thật nếu mối liên hệ với chất lượng chưa được kiểm chứng.

Để tránh chỉ nhìn hạ tầng, bộ golden signals cần mở rộng sang tín hiệu mô hình và dữ liệu.

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

Khi các chỉ số tổng hợp che khuất một subgroup, phân tích theo slice giúp phát hiện lỗi cục bộ.

## Golden tín hiệu (signal / 신호) cho mô hình (model / 모델) Serving

Có thể bắt đầu bằng:

```text
Traffic
Errors
Latency
Saturation
```

sau đó bổ sung tín hiệu mô hình và tín hiệu dữ liệu.

Mỗi slice cần được so với một cửa sổ tham chiếu có chủ đích, nếu không kết quả so sánh sẽ khó diễn giải.

## Giám sát theo Slice

Chỉ số tổng hợp có thể che lỗi của một subgroup. Nên theo dõi các lát dữ liệu có ý nghĩa như vùng, thiết bị, ngôn ngữ, phân khúc khách hàng hoặc loại tài liệu.

Nhưng quá nhiều slice gây nhiễu và bài toán so sánh nhiều lần; nên chọn slice dựa trên rủi ro và use trường hợp (case / 사례).

Sau khi chọn slice, cần xác định phân phối tham chiếu để biết sự thay đổi đang được đo so với giai đoạn nào.

## Phân phối tham chiếu

Giám sát drift cần một cửa sổ tham chiếu. Tham chiếu có thể là dữ liệu huấn luyện, kiểm tra hợp lệ (validation / 검증) hoặc một giai đoạn môi trường vận hành (production / 운영 환경) ổn định gần đây. Mỗi lựa chọn trả lời một câu hỏi khác nhau.

So sánh phân phối chỉ là bước chẩn đoán; cần đối chiếu nó với chất lượng dữ liệu và chất lượng mô hình.

## Chất lượng dữ liệu và Chất lượng mô hình

Phân phối đầu vào thay đổi không chứng minh hiệu năng mô hình đã giảm. Nhưng bất thường dữ liệu là tín hiệu chẩn đoán cần được điều tra.

Những bất thường này trở nên dễ hiểu hơn khi xem vòng phản hồi mà hệ thống tạo ra.

## Vòng phản hồi

Đầu ra (output / 출력) mô hình có thể làm thay đổi dữ liệu được quan sát về sau. Hệ thống gợi ý chỉ thấy click trên những item nó đã hiển thị. Vì vậy monitoring cần hiểu dữ liệu phụ thuộc chính sách (policy / 정책) như thế nào.

Từ các tín hiệu đó, SLO, SLA và error budget biến quan sát thành cam kết vận hành.

## SLO, SLA và lỗi (error / 오류) ngân sách (budget / 예산)

SLO là mục tiêu nội bộ, SLA là cam kết với bên ngoài. Ngân sách lỗi (error budget) định lượng mức thất bại (failure / 실패) hệ thống chấp nhận được.

Chất lượng (quality / 품질) SLO của AI khó định nghĩa hơn độ trễ (latency / 지연 시간) SLO vì nhãn có thể đến trễ hoặc mang tính chủ quan, nhưng vẫn cần đặc tả hợp đồng (contract / 계약) đo được.

Chi phí cũng là một tín hiệu vận hành cần được phân bổ đến đúng thành phần, thay vì chỉ xem ở cấp hóa đơn.

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

Việc quan sát chi phí phải đi cùng giới hạn về quyền riêng tư và chính sách lưu giữ dữ liệu.

## Khả năng quan sát có nhận thức về Quyền riêng tư

Log cũng là một kho dữ liệu. Cần retention, kiểm soát truy cập, mã hóa và redaction. Prompt hoặc kết quả công cụ (tool / 도구) nhạy cảm không nên bị sao chép vô hạn vào dấu vết (trace / 추적).

Các nguyên tắc trên có thể kiểm tra qua một ca điều tra sự cố cụ thể.

## Ví dụ điều tra sự cố (incident / 인시던트)

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

Từ ca điều tra này, có thể rút ra một mô hình tư duy dùng lại cho các hệ thống khác.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Giám sát cho biết có gì đó đang sai.
Khả năng quan sát giúp giải thích sai ở đâu và vì sao.
```

Các nhầm lẫn sau đây làm rõ ranh giới của mô hình tư duy đó.

## Những nhầm lẫn thường gặp

### “HTTP success nghĩa là AI success”

Không. Sức khỏe dịch vụ không đồng nghĩa độ đúng của tác vụ.

### “Log toàn bộ prompt để gỡ lỗi (debug / 디버그) cho dễ”

Không nên mặc định như vậy vì rủi ro quyền riêng tư và bảo mật lớn.

### “Drift chỉ số (metric / 지표) tăng thì retrain ngay”

Không. Drift cần được diễn giải cùng kết quả và hiệu năng.

Phần liên kết kiến thức khép lại chủ đề và mở đường sang drift, evaluation và latency.

## Liên kết kiến thức

Xem [Drift and Retraining](./07_drift_and_retraining.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md), [Latency/Cost](../15_ai_engineering/09_latency_throughput_and_cost.md) và [Evaluation Layer](../18_evaluation_reliability_interpretability/README.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
