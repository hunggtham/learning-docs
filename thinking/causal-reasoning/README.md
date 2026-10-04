# Causal Reasoning — Từ tương quan đến cơ chế

Causal reasoning (suy luận nhân quả / 인과 추론) giúp trả lời câu hỏi khó hơn “hai thứ có đi cùng nhau không?”: **nếu ta thay đổi X, Y có thay đổi vì X hay không?**

Formal causal inference thuộc [Research Methods](../../research_methods/README.md) và [Economics / Econometrics](../../economics/README.md). Trang này tập trung vào workflow dùng trong đời sống, công việc, đọc nghiên cứu và debugging.

## 1. Association ≠ causation

Nếu X và Y đi cùng nhau, ít nhất bốn khả năng tồn tại:

```text
X → Y
Y → X
Z → X và Z → Y
X ↔ Y do selection / measurement / chance
```

Correlation chỉ thu hẹp hypothesis space; nó không tự chọn một causal story.

## 2. Bắt đầu bằng causal question rõ ràng

Câu hỏi:

> “Người tập thể dục nhiều có khỏe hơn không?”

khác với:

> “Nếu cùng một nhóm người tăng vận động từ mức A lên B, outcome sức khỏe thay đổi thế nào trong khoảng thời gian T?”

Causal question tốt phải nói rõ intervention, population, outcome và time horizon.

## 3. Confounder

Confounder là biến ảnh hưởng cả exposure và outcome.

Ví dụ người ngủ nhiều hơn có thể đồng thời khác về tuổi, stress, work schedule hoặc bệnh nền. Không kiểm soát đúng causal structure có thể khiến association bị diễn giải sai.

Không phải cứ “control càng nhiều biến càng tốt”. Control mediator hoặc collider có thể tạo bias mới. Chi tiết handoff về Research Methods/Econometrics.

## 4. Counterfactual

Causal effect hỏi về sự khác biệt giữa:

```text
Outcome nếu intervention xảy ra
vs
Outcome nếu intervention không xảy ra
```

trên cùng causal unit. Ta không quan sát đồng thời cả hai trạng thái, nên causal inference luôn cần design hoặc assumption để xây comparison hợp lý.

## 5. Mechanism không thay thế identification

Một mechanism hợp lý làm causal claim believable hơn nhưng chưa chứng minh effect đã xảy ra trong population cụ thể.

Ngược lại, một experiment có thể đo effect dù mechanism chưa hiểu hết.

Giữ riêng:

```text
Does it happen?
How large is the effect?
Why does it happen?
When does it generalize?
```

## 6. Natural experiment mindset

Khi không có randomized experiment, hỏi:

- có policy cutoff không?
- có timing shock không?
- có nhóm comparison chịu cùng trend nhưng không chịu intervention không?
- assignment có gần random ở một boundary không?

Đây chỉ là câu hỏi tìm design; không tự biến observational data thành causal evidence.

## 7. Alternative hypotheses và disconfirmation

Một causal story chỉ đáng tin hơn khi nó sống sót qua các explanation cạnh tranh. Viết `H1` cùng ít nhất hai alternative, sau đó ghi evidence mà mỗi hypothesis dự đoán khác nhau. Evidence chỉ xác nhận H1 nhưng cũng dễ xuất hiện khi H2 đúng không có diagnostic value cao.

Khi intervention nguy hiểm hoặc không thể làm, dùng prediction bất đối xứng, negative control, temporal boundary hoặc natural comparison để tìm evidence có thể làm H1 yếu đi. [Red-team, Steelman & Disconfirmation](../practice/07_red_team_steelman_and_disconfirmation.md) luyện cách phản biện causal claim mà không nhầm “chưa chứng minh” với “đã sai”.

## 8. Causal debugging

Trong engineering:

```text
Deploy A
→ error rate tăng
```

chưa đủ kết luận A gây lỗi nếu cùng lúc traffic spike, dependency outage hoặc config khác đổi.

Workflow:

```text
timeline
→ candidate causes
→ isolate variables
→ reproduce / rollback / compare
→ inspect mechanism
→ update confidence
```

## 9. Intervention ladder

Có thể xếp evidence theo khả năng phân biệt hypothesis:

```text
observation
< controlled comparison
< quasi-experiment
< randomized intervention
```

Đây không phải ranking tuyệt đối về chất lượng mọi study; measurement kém hoặc external validity thấp vẫn có thể làm evidence yếu.

## 10. Causal checklist

Trước một claim “X gây Y”, hỏi:

1. X và Y được đo thế nào?
2. Direction có thể ngược không?
3. Confounder lớn nhất là gì?
4. Selection vào sample diễn ra thế nào?
5. Có intervention/comparison group không?
6. Mechanism plausible là gì?
7. Effect size lớn đến đâu?
8. Population nào được nghiên cứu?
9. Claim có generalize quá xa evidence không?

## Connections

- [Statistics for Life](../statistics-for-life/README.md): association, sampling và uncertainty.
- [Critical Thinking](../critical-thinking/README.md): kiểm tra cấu trúc claim.
- [Systems Thinking](../systems-thinking/README.md): nhiều causal path và feedback loop.
- [Research Methods](../../research_methods/README.md): study design và identification.
- [Economics](../../economics/README.md): econometrics và policy effects.
- [Computer Science](../../computer_science/README.md): debugging và experiments.
