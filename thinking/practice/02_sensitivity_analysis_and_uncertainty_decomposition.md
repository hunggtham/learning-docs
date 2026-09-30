# Sensitivity Analysis & Uncertainty Decomposition — Assumption nào thật sự quan trọng?

Nhiều decision trông phức tạp vì có nhiều con số, nhưng conclusion thường chỉ nhạy với vài assumption. Sensitivity analysis giúp tìm chúng.

Mục tiêu:

```text
model the decision
→ expose assumptions
→ vary them
→ find decision-critical uncertainty
→ spend research effort where it matters
```

Đây là practical layer; formal statistics, optimization và model analysis vẫn nằm ở [Mathematics](../../mathematics/README.md).

## 1. Tách known, estimated và unknown

Trước khi tính toán, phân loại input:

```text
Known / contracted
Estimated from data
Forecasted
Judgment / assumption
Unknown but potentially important
```

Một spreadsheet chính xác đến hai chữ số thập phân không làm forecast input trở nên chính xác.

## 2. One-way sensitivity

Giữ các input khác cố định và thay một input trong plausible range.

Ví dụ một project automation:

```text
implementation cost = 5–8 tuần
hours saved / week = 5–20 giờ
adoption rate = 40–90%
maintenance = 2–8 giờ / tháng
```

Hỏi conclusion “nên làm” có đổi khi từng biến đi từ low → base → high không.

Nếu chỉ adoption rate làm decision đảo chiều, đó là **decision-critical variable**.

## 3. Break-even analysis

Thay vì hỏi “input thật sự là bao nhiêu?”, đôi khi dễ hơn khi hỏi:

```text
input phải đạt bao nhiêu thì decision đổi?
```

Ví dụ:

```text
Nếu tool tiết kiệm ≥ 8 giờ/tuần thì project break even trong 6 tháng.
```

Sau đó research tập trung vào câu hỏi 8 giờ/tuần có realistic không.

## 4. Uncertainty decomposition

Tách uncertainty theo nguồn:

```text
measurement uncertainty
sampling uncertainty
model uncertainty
parameter uncertainty
future-state uncertainty
behavioral / strategic response
implementation uncertainty
```

Các loại này cần cách giảm khác nhau. Thu thập thêm sample không giải quyết model misspecification; model tốt hơn không loại bỏ policy/competitor response.

## 5. Drill A — Assumption table

Với một decision thật, lập bảng:

| Assumption | Base | Plausible range | Evidence quality | Decision sensitivity |
|---|---:|---:|---|---|
| demand | 100 | 60–140 | medium | high |
| unit cost | 20 | 18–24 | high | low |
| delay | 2 months | 1–6 | low | high |

Sau đó chỉ chọn 1–3 uncertainty quan trọng nhất để investigate.

## 6. Tornado thinking không cần chart

Bạn không cần software để dùng intuition của tornado chart. Rank variable theo mức nó làm outcome thay đổi:

```text
variable A: outcome 10 → 100
variable B: outcome 45 → 55
variable C: outcome 48 → 52
```

Research A trước B/C nếu cost of information hợp lý.

Kết nối trực tiếp với [Value of Information](../value-of-information/README.md).

## 7. Interaction effects

One-way sensitivity có thể bỏ sót việc hai input xấu cùng lúc.

Ví dụ:

```text
low demand alone → survivable
high cost alone → survivable
low demand + high cost → cash runway failure
```

Khi variables correlated hoặc interaction mạnh, chuyển sang scenario/stress testing.

## 8. Model sensitivity

Đừng chỉ thay parameter trong cùng model. Hỏi conclusion có đổi nếu dùng một model khác hợp lý không.

Ví dụ tăng user count có thể được model bằng:

- linear growth;
- saturation/logistic growth;
- cohort retention;
- network effects.

Nếu conclusion chỉ đúng trong một model, confidence phải thấp hơn.

Xem [Model Selection](../model-selection/README.md).

## 9. Drill B — Remove false precision

Lấy một calculation bạn đang dùng và thay point estimate bằng range.

Thay:

```text
ROI = 18.4%
```

bằng:

```text
ROI plausible range = -5% → 35%
main driver = adoption
break-even adoption = 62%
```

Bản thứ hai thường hữu ích cho decision hơn dù nhìn “ít chính xác” hơn.

## 10. Failure modes

### Range tùy ý

Range phải có rationale: historical variation, confidence interval, expert bounds, contract limits hoặc explicit judgment.

### Vary mọi thứ vô hạn

Sensitivity analysis tồn tại để ưu tiên uncertainty, không phải tạo một universe combinatorial không thể dùng.

### Chỉ kiểm tra upside/downside đối xứng

Tail risk có thể asymmetric. Một input giảm 20% và tăng 20% không nhất thiết có impact đối xứng.

### Sensitivity ≠ probability

Một scenario làm decision thất bại không nói scenario đó có xác suất cao. Sensitivity và probability là hai câu hỏi khác nhau.

## 11. Template

```text
Decision / claim:
Outcome metric:
Inputs:
For each input:
  base value
  plausible range
  evidence source
  sensitivity
Break-even values:
Important interactions:
Alternative models:
Top 1–3 uncertainties worth researching:
```

## Connections

- [Model Selection](../model-selection/README.md)
- [Value of Information](../value-of-information/README.md)
- [Risk](../risk/README.md)
- [Expected Value](../expected-value/README.md)
- [Scenario Planning & Stress Testing](./03_scenario_planning_and_stress_testing.md)

Sensitivity analysis tốt không làm uncertainty biến mất. Nó chỉ ra **uncertainty nào đáng quan tâm**.