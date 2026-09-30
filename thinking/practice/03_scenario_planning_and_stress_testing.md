# Scenario Planning & Stress Testing — Khi tương lai không đi theo base case

Forecast thường tạo một “most likely” path. Decision tốt cần hỏi thêm: nếu thế giới đi lệch path đó, plan còn sống được không?

Scenario planning và stress testing khác nhau:

```text
Scenario planning
= nhiều future state hợp lý, có logic nội tại

Stress testing
= cố ý đẩy system vào điều kiện xấu để tìm điểm gãy
```

## 1. Không tạo ba scenario bằng cách ±10%

Một good scenario không chỉ là cùng một thế giới với con số cao/thấp hơn. Nó có thể thay đổi mechanism:

```text
Base: demand tăng đều
Scenario B: competitor giảm giá mạnh
Scenario C: regulation đổi distribution channel
Scenario D: supplier failure làm capacity trở thành bottleneck
```

Mỗi scenario cần một causal story có thể kiểm tra.

## 2. Chọn axes có impact cao và uncertainty cao

Dùng [Sensitivity Analysis](./02_sensitivity_analysis_and_uncertainty_decomposition.md) để tìm variables quan trọng.

Một 2×2 đơn giản có thể dùng hai uncertainty lớn:

```text
Demand: low / high
Funding conditions: loose / tight
```

Từ đó có bốn worlds khác nhau. Không cần luôn dùng 2×2; mục tiêu là tránh scenario tùy hứng.

## 3. Scenario anatomy

Mỗi scenario ghi:

```text
Initial conditions
Key assumptions
Mechanism / causal chain
Actor responses
Leading indicators
Outcome range
Main failure modes
Actions that work in this world
```

Nếu scenario chỉ có outcome mà không có mechanism, nó khó dùng để monitor/update.

## 4. Drill A — Base / adverse / structural-break

Chọn một decision và viết ba scenario:

### Base case

Những assumptions trung tâm tiếp tục tương đối đúng.

### Adverse case

Một số key variables xấu đi nhưng system structure không đổi.

### Structural-break case

Một assumption nền bị phá: technology, regulation, competitor behavior, dependency, health of a critical system, funding regime hoặc user behavior thay đổi.

Sau đó hỏi:

```text
Decision có reversible không?
Cash/time/resource buffer đủ không?
Có early signal nào để switch plan?
```

## 5. Stress test survivability trước optimization

Một plan có expected return cao nhưng fail hoàn toàn trong một plausible stress có thể không phù hợp nếu failure là irrecoverable.

Stress test nên hỏi:

```text
What breaks first?
At what threshold?
Can we recover?
How quickly?
What dependencies fail together?
```

Đây là bridge trực tiếp sang [Risk](../risk/README.md).

## 6. Correlated failure

Stress test từng component riêng có thể bỏ sót common-cause failure.

Ví dụ:

```text
traffic spike
→ database load tăng
→ latency tăng
→ retries tăng
→ traffic hiệu dụng tăng thêm
→ queue saturation
```

Đây là feedback loop, không phải năm independent risks.

Xem [Systems Thinking](../systems-thinking/README.md).

## 7. Reverse stress test

Thay vì chọn shock rồi xem outcome, bắt đầu từ failure:

```text
Điều gì phải xảy ra để system/project/decision thất bại hoàn toàn?
```

Sau đó tìm combinations có thể dẫn đến failure đó.

Reverse stress test rất hữu ích khi ta chưa biết shock nào nên ưu tiên.

## 8. Leading indicators và trigger

Scenario chỉ hữu ích nếu có dấu hiệu để nhận biết world nào đang hình thành.

Ví dụ:

```text
Scenario: demand collapse
Leading indicators:
- conversion giảm trước revenue
- cancellation tăng
- search volume giảm
Trigger:
- nếu 2/3 metric vượt threshold trong 3 tuần → switch plan
```

Trigger nên được viết trước để giảm hindsight và panic reaction.

## 9. Drill B — Pre-commit response

Với mỗi scenario, viết trước:

```text
If X happens,
we will observe Y,
and take action Z,
unless evidence W invalidates the scenario.
```

Cấu trúc này biến scenario planning thành decision rule thay vì story exercise.

## 10. Robust decision

Một decision robust không nhất thiết optimal trong base case. Nó có thể cho outcome “đủ tốt” qua nhiều plausible worlds.

Ví dụ giữ buffer làm giảm return trong normal times nhưng có thể tăng survivability khi adverse scenario xảy ra.

Trade-off này phải explicit, không dùng “robust” như synonym của conservative.

## 11. Failure modes

### Doom scenario không có probability boundary

Extreme story dễ gây attention nhưng không tự đáng ưu tiên. Kết hợp impact với plausibility/probability.

### Scenario explosion

10–20 scenario thường không giúp hơn 3–5 scenario distinct mechanisms.

### Không update

Scenario set phải đổi khi evidence mới làm một world improbable hoặc mở một mechanism mới.

### Stress test nhưng không có action

Biết system gãy ở đâu mà không có mitigation/trigger chỉ tạo information, chưa tạo resilience.

## 12. Template

```text
Decision/system:
Critical assumptions:
Scenario 1:
  mechanism
  indicators
  outcome
  response
Scenario 2:
  ...
Scenario 3:
  ...
Reverse stress condition:
Break thresholds:
Correlated dependencies:
Buffers / options:
Monitoring triggers:
```

## Connections

- [Forecasting](../forecasting/README.md)
- [Risk](../risk/README.md)
- [Systems Thinking](../systems-thinking/README.md)
- [Model Selection](../model-selection/README.md)
- [Decision Making](../decision-making/README.md)

Scenario planning không dự đoán chính xác tương lai. Nó giúp plan **không phụ thuộc hoàn toàn vào một tương lai duy nhất**.