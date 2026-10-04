# Reading Specs, Labels & Units — Một con số trên nhãn thực sự nói gì?

Một specification (thông số kỹ thuật / 사양) hữu ích khi nó đo một property liên quan đến use case. Nhưng trong đời sống, spec thường bị đọc như quality score: số lớn hơn = tốt hơn. Đây là lỗi đầu tiên Consumer Literacy cần sửa.

Mục tiêu chapter này là xây một habit: **trước khi so hai con số, phải biết chúng đo cùng đại lượng, cùng điều kiện và cùng mục tiêu hay không**.

## 1. Spec là measurement, không phải judgment

Ví dụ:

```text
300 horsepower
500 Wh battery capacity
46% ABV
60 IBU
1200 nits brightness
10 kg rated load
```

Các số trên đều có meaning cụ thể, nhưng không số nào tự nói “sản phẩm tốt”. Chúng chỉ nói một property dưới definition hoặc test condition nào đó.

Vì vậy trước mọi comparison, hỏi bốn câu:

```text
What is measured?
In what unit?
Under what conditions?
Why does this property matter for my use case?
```

Nếu chưa trả lời được câu cuối, spec có thể chỉ là distraction.

## 2. Unit là một phần của meaning

Số không có unit rất dễ tạo hiểu nhầm.

Ví dụ `500` có thể là:

```text
500 W
500 Wh
500 mAh
500 km
500 g
```

Trong battery context, `W` là power, `Wh` là energy. Hai đại lượng liên quan nhưng không thể thay thế nhau. Một battery có energy capacity lớn không tự động cho biết nó có thể deliver power cao trong mọi điều kiện.

Đây là lý do dimensional reasoning quan trọng. Nếu một calculation cuối cùng có unit không phù hợp với câu hỏi, model có lỗi dù arithmetic đúng.

Khi cần kiểm tra denominator, baseline hoặc cách đọc một quantity, handoff sang [`../../thinking/statistics-for-life/`](../../thinking/statistics-for-life/README.md). Estimation drill chi tiết chỉ nên được link sau khi file đó tồn tại trên canonical `main`.

## 3. Test condition quyết định khả năng so sánh

Hai sản phẩm có thể công bố cùng type metric nhưng đo theo protocol khác nhau.

Ví dụ range, battery life, noise, brightness, fuel economy hoặc load rating đều phụ thuộc điều kiện test.

Câu hỏi cần đọc cùng spec:

```text
temperature?
load?
speed?
measurement distance?
standard/protocol?
peak or sustained?
new condition or aged condition?
```

Nếu protocol khác nhau, ranking trực tiếp có thể sai.

## 4. Peak, nominal, average và sustained không giống nhau

Marketing thường thích peak value vì số đẹp.

Nhưng use thực tế nhiều khi bị quyết định bởi sustained performance.

Ví dụ:

```text
peak charging power
vs
average charging power across session

peak CPU frequency
vs
sustained performance under thermal load

peak audio power
vs
continuous rated output
```

Không phải peak vô dụng. Nó chỉ trả lời câu hỏi khác.

Rule:

> Luôn xác định spec đang nói **capacity tối đa**, **mức danh định**, **trung bình**, hay **khả năng duy trì**.

## 5. Rating không phải raw measurement duy nhất

Một số label là rating/classification được xây từ test protocol, không phải raw property.

Ví dụ water resistance, safety class, efficiency grade hoặc durability class có thể encode nhiều điều kiện trong một nhãn.

Do đó cần biết:

```text
rating body / standard
what tests are included
pass/fail threshold
scope and exclusions
```

Không diễn giải label rộng hơn standard cho phép.

## 6. Percentage cần denominator

Các claim như:

```text
30% faster
50% more efficient
2× stronger
```

không đủ nếu thiếu baseline.

Hỏi:

```text
compared with what?
under what workload?
absolute difference?
which denominator?
```

`50% improvement` từ 2 lên 3 khác hoàn toàn từ 200 lên 300 về impact thực tế.

## 7. Spec có predictive validity tới đâu?

Một spec tốt phải có relationship đủ mạnh với outcome bạn quan tâm.

Ví dụ horsepower có liên quan performance nhưng acceleration còn phụ thuộc:

```text
mass
gearing
traction
power curve
response
```

IBU liên quan bitterness compounds nhưng perceived bitterness còn bị ảnh hưởng bởi malt sweetness, alcohol và sensory context.

Do đó một spec có thể **relevant nhưng không sufficient**.

Đây là pattern quan trọng:

```text
property measured
→ contributes to outcome
≠ fully determines outcome
```

## 8. Feature count dễ tạo proxy trap

Sản phẩm A có 20 feature, B có 10 không có nghĩa A tốt gấp đôi.

Feature chỉ tạo value khi:

```text
used
× works reliably
× fits workflow
× does not impose too much complexity/cost
```

Nhiều feature còn tạo maintenance surface, UI complexity và failure points.

Vì vậy đọc feature list phải quay về use case.

## 9. “Pro”, “Premium”, “Ultra” thường không phải engineering definition

Market labels có thể hữu ích để phân segment nhưng thường không phải scientific unit.

Khi gặp adjective:

```text
premium
professional
military-grade
AI-powered
high-performance
natural
```

hãy hỏi label này có:

- standard chính thức;
- test condition;
- measurable criterion;
- hay chỉ là marketing positioning.

Không mặc định tất cả đều vô nghĩa; nhưng weight của claim phụ thuộc evidence.

## 10. Regulatory label và marketing label phải tách nhau

Một certification/regulatory mark có thể có legal definition và conformity process. Marketing badge nội bộ có thể không có.

Với label có tính pháp lý hoặc safety-sensitive:

- kiểm tra jurisdiction;
- kiểm tra issuing authority/standard body;
- kiểm tra snapshot date;
- không copy rule time-sensitive thành truth vĩnh viễn.

Legal detail handoff sang relevant civic/legal domain hoặc official source.

## 11. Comparison worksheet

Khi so hai sản phẩm:

| Property | Product A | Product B | Same protocol? | Relevant to use case? | Caveat |
|---|---:|---:|---|---|---|
| X |  |  |  |  |  |
| Y |  |  |  |  |  |

Bảng không nhằm tạo score tổng. Nó ép ta thấy khi hai con số **không thật sự comparable**.

## 12. Drill — bóc một spec sheet

Chọn một product spec sheet và phân loại từng dòng:

```text
measurement
rating/class
marketing label
configuration option
physical dimension
capacity limit
performance claim
```

Sau đó với mỗi item quan trọng, ghi:

```text
What does it measure?
Unit/protocol?
Why does it matter?
What does it not tell me?
Trade-off?
```

Nếu không trả lời được, đừng dùng spec đó làm tiêu chí ranking chính.

## 13. Common failure modes

### Bigger-is-better

Không phải mọi quantity đều monotonic với utility. Weight, power, capacity, stiffness, brightness hoặc complexity đều có trade-off.

### One-number ranking

Một product hiếm khi có quality scalar duy nhất. Nếu seller cố gói mọi thứ vào một score, cần hiểu score construction.

### Comparing different test regimes

Hai con số giống unit chưa chắc cùng protocol.

### Ignoring tolerance và real-world variance

Manufacturing variation, environment và aging làm actual performance lệch nominal spec.

### Specs replace mechanism

Spec sheet cho biết *what was measured*, không luôn giải thích *why product behaves that way*. Muốn hiểu mechanism phải quay lại product-domain chapter.

## Reusable checklist

```text
Use case:
Spec:
Measured property:
Unit:
Test protocol:
Peak/nominal/average/sustained:
Baseline/denominator:
Relevance to outcome:
What it does NOT predict:
Trade-off:
Need external evidence? yes/no
```

## Connections

- [`../CONCEPTUAL_DEPENDENCIES.md`](../CONCEPTUAL_DEPENDENCIES.md): specs nằm giữa mechanism và trade-offs trong dependency graph.
- [`../../thinking/statistics-for-life/`](../../thinking/statistics-for-life/README.md): denominator, baseline và cách đọc quantitative claim.
- [`../../thinking/critical-thinking/`](../../thinking/critical-thinking/README.md): kiểm tra product claim và source.
- [`../../thinking/causal-reasoning/`](../../thinking/causal-reasoning/README.md): tránh dùng một spec liên quan để suy ra causal conclusion quá rộng.

Điểm cần giữ lại không phải “đừng tin specs”. Ngược lại, **hãy đọc specs chính xác hơn**: biết nó đo gì, điều kiện nào, dự đoán được điều gì và khi nào phải chuyển từ con số sang mechanism, evidence hoặc real-world use.