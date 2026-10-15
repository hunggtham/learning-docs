# Argument & Evidence Mapping — Tách claim, evidence và inference trước khi kết luận

Nhiều tranh luận khó không phải vì thiếu dữ liệu mà vì các bên đang trộn ba tầng khác nhau: **điều được quan sát**, **cách diễn giải observation**, và **kết luận muốn rút ra**. Khi ba tầng này bị viết thành một câu liền mạch, một claim yếu có thể nghe rất chắc chắn.

Chapter này luyện cách dựng một map có thể review được. Formal logic và argument theory tiếp tục thuộc [Philosophy](../../philosophy/README.md); study design và evidence quality thuộc [Research Methods](../../research_methods/README.md). Ở đây ta tập trung vào workflow dùng trong news, report, technical review, policy claim và decision.

## 1. Map bắt đầu từ một claim có thể kiểm tra

Một câu quá rộng như:

> “Remote work làm productivity tốt hơn.”

chưa đủ để map tốt. Ta cần operationalize:

```text
Population: nhóm nào?
Intervention/exposure: remote work ở mức nào?
Outcome: productivity đo bằng gì?
Comparator: so với trạng thái nào?
Time horizon: trong bao lâu?
```

Ví dụ rõ hơn:

> “Trong team software X, chuyển từ 5 ngày office sang hybrid 2 ngày office làm cycle time giảm trong 3 tháng đầu.”

Lúc đó evidence và alternative explanation mới có thể gắn vào một question cụ thể.

## 2. Cấu trúc tối thiểu

Dùng map:

```text
Claim
├── Evidence for
├── Evidence against
├── Assumptions
├── Alternative explanations
├── Confidence
└── Evidence that would change conclusion
```

Map không nhằm biến reasoning thành hình thức cứng nhắc. Nó ép ta trả lời câu quan trọng: **phần nào là data, phần nào là bridge từ data sang conclusion?**

## 3. Evidence không tự nói chuyện

Ví dụ:

```text
Observation:
Revenue tăng 20% sau khi app redesign.
```

Từ observation này có nhiều inference khả dĩ:

```text
redesign caused the increase
seasonality caused it
marketing campaign caused it
pricing changed
customer mix changed
measurement changed
multiple causes acted together
```

Nếu report viết thẳng:

> “Redesign tăng revenue 20%”

thì causal bridge đang bị ẩn.

Handoff sang [Causal Reasoning](../causal-reasoning/README.md) khi claim vượt từ association sang cause.

## 4. Evidence strength phải khớp claim strength

Có thể hình dung ba mức:

```text
Evidence supports description
Evidence supports association
Evidence supports intervention/causality
```

Một survey có thể hỗ trợ claim “người tham gia báo cáo X”, nhưng không tự động hỗ trợ claim “X gây ra Y”. Một experiment tốt có thể mạnh hơn cho causal question nhưng vẫn có giới hạn external validity.

Rule:

> Không nâng cấp claim chỉ vì evidence nghe “khoa học”.

## 5. Assumption ledger

Mọi inference cần assumptions. Ghi chúng ra riêng.

Ví dụ một dashboard cho thấy conversion giảm:

```text
Assumption A: tracking definition không đổi
Assumption B: traffic quality tương đương
Assumption C: attribution window giống nhau
Assumption D: outage/bot filtering không làm metric lệch
```

Nếu assumption A sai, có thể không cần tìm causal explanation ở product behavior nữa.

Assumption ledger giúp tránh một lỗi phổ biến: debug business reality trong khi thực ra measurement pipeline đã đổi.

## 6. Evidence for và evidence against phải cùng tiêu chuẩn

Confirmation bias thường xuất hiện khi evidence ủng hộ được chấp nhận dễ dàng, còn evidence phản bác bị yêu cầu tiêu chuẩn cao hơn.

Khi map, dùng cùng câu hỏi cho cả hai phía:

```text
Source quality?
Measurement validity?
Sample relevance?
Alternative explanation?
Conflict of interest?
Replicability / independent confirmation?
```

Không phải mọi evidence phải có weight ngang nhau; nhưng criteria để đánh giá phải nhất quán.

## 7. Alternative hypotheses

Một map tốt không chỉ có “pro/con”. Nó có competing explanations.

Ví dụ hệ thống latency tăng sau deploy:

```text
H1: new query pattern
H2: cache invalidation
H3: traffic spike
H4: downstream dependency degradation
H5: observability artifact
```

Sau đó hỏi evidence nào có khả năng phân biệt H1–H5 nhanh nhất.

Đây là bridge sang [Value of Information](../value-of-information/README.md): evidence tốt nhất thường là evidence **discriminating**, không phải evidence nhiều nhất.

## 8. Source provenance

Đừng chỉ ghi “có nghiên cứu nói”. Track đường đi:

```text
social post
→ news article
→ press release
→ study
→ dataset / method
```

Mỗi layer có thể thêm interpretation hoặc bỏ caveat.

Với report doanh nghiệp:

```text
executive slide
→ dashboard
→ metric definition
→ event/log source
```

Map provenance giúp phát hiện khi hai nguồn tưởng độc lập thực ra cùng copy một nguồn gốc.

## 9. Confidence không phải nhãn trang trí

Sau mapping, confidence nên phản ánh:

- quality của evidence mạnh nhất;
- consistency giữa sources;
- assumption uncertainty;
- plausible alternatives;
- mức directness của measurement;
- causal identification nếu claim là causal.

Có thể dùng range ngôn ngữ hoặc probability nếu phù hợp, nhưng tránh pseudo-precision.

Ví dụ:

```text
Low confidence
Moderate confidence
High confidence
```

hoặc:

```text
~60–70%
```

chỉ khi bạn có habit calibration và resolution rule phù hợp.

## 10. What would change my mind?

Đây là phần chống reasoning “đóng”.

Viết trước:

```text
Evidence nào nếu xuất hiện sẽ làm confidence giảm?
Evidence nào sẽ làm confidence tăng?
Outcome nào sẽ falsify key mechanism?
```

Nếu câu trả lời là “không có evidence nào”, bạn không còn ở mode inquiry nữa.

## 11. Steelman trước khi phản biện

Trước khi attack một conclusion, viết phiên bản mạnh nhất mà evidence hiện có cho phép.

```text
Weak caricature
→ fair reconstruction
→ strongest supported version
→ critique
```

Steelmanning không có nghĩa đồng ý. Nó làm criticism chính xác hơn và giảm straw man.

## 12. Drill A — News claim

Chọn một headline có causal hoặc policy implication.

Output:

```text
Original headline:
Narrowed claim:
Primary source:
Evidence for:
Evidence against:
Hidden assumptions:
Alternative explanations:
What is descriptive vs causal vs normative:
Current confidence:
What would change my mind:
```

Sau đó so với [News Claims Case](../90_connections/00_news_claims_and_online_information.md).

## 13. Drill B — Engineering root cause

Dùng incident thật hoặc giả lập.

```text
Claim:
“Deployment X caused latency spike.”
```

Map:

```text
timeline evidence
logs/metrics
counterevidence
other changes at same time
rollback result
dependency health
measurement artifacts
```

Sau đó chọn test có information value cao nhất.

Không gọi correlation theo timeline là root cause nếu chưa có discriminating evidence.

## 14. Drill C — Business recommendation

Claim:

```text
“We should increase discount because conversion rose during campaign A.”
```

Map:

```text
Observed:
Inference:
Assumptions:
Alternative mechanisms:
Cannibalization / margin effects:
Customer mix effects:
Long-term effects:
What evidence is missing:
```

Điểm quan trọng là tách:

```text
“campaign correlated with conversion”
```

khỏi:

```text
“more discount maximizes business value”
```

Đó là hai question khác nhau.

## 15. Review score

Mỗi map có thể self-review theo 0/1:

```text
[ ] claim đã đủ specific
[ ] observation tách khỏi inference
[ ] assumptions được viết ra
[ ] có ít nhất 2 alternative explanations khi phù hợp
[ ] evidence for/against dùng cùng quality criteria
[ ] source provenance rõ
[ ] causal claim có causal justification
[ ] confidence có boundary
[ ] có explicit update trigger
```

Theo dõi không phải tổng điểm tuyệt đối mà recurring miss của bạn. Nếu 5 map liên tiếp quên alternative explanation, đó là process defect cần sửa.

## 16. Failure modes

### Map quá lớn

Nếu map có 50 node nhưng không giúp quyết định, scope đang quá rộng. Quay lại [Problem Framing](../problem-framing/README.md).

### False balance

Hai phía không cần số node bằng nhau. Evidence quality quan trọng hơn symmetry.

### “Assumption” như thùng rác

Assumption phải cụ thể và có thể challenge. “Market may change” quá chung; “competitor price remains within ±5%” hữu ích hơn.

### Treating absence of evidence as evidence of absence

Không tìm thấy support không luôn chứng minh claim sai. Hãy phân biệt evidence expected-but-missing với domain chưa được đo đủ.

### Argument map thay thế domain expertise

Map tốt không cứu được factual premises sai. Khi premise thuộc medicine, law, finance, engineering hoặc science, phải handoff sang owner chuyên môn.

## Reusable template

```text
# Claim map — YYYY-MM-DD

Question:
Claim:
Scope/population/time:

## Evidence for
- source:
- observation:
- strength/limits:

## Evidence against
- source:
- observation:
- strength/limits:

## Assumptions
- A1:
- A2:

## Alternative explanations
- H1:
- H2:

## Provenance
original source → intermediaries → current claim

## Judgment
Current confidence:
Strongest reason for:
Strongest reason against:
What would change my mind:
Next evidence with highest information value:
```

## Connections

- [Critical Thinking](../critical-thinking/README.md): claim, source và inference checks.
- [Logical Fallacies](../logical-fallacies/README.md): argument repair thay vì chỉ gắn nhãn lỗi.
- [Causal Reasoning](../causal-reasoning/README.md): causal bridge và alternative mechanisms.
- [Value of Information](../value-of-information/README.md): chọn evidence phân biệt hypotheses.
- [Cognitive Bias](../cognitive-bias/README.md): confirmation và motivated reasoning.
- [Research Methods](../../research_methods/README.md): measurement, study design và evidence quality.
- [Philosophy](../../philosophy/README.md): logic, epistemology và justification.

Argument map tốt không đảm bảo conclusion đúng. Giá trị của nó là làm reasoning **inspectable**: người khác và chính bạn có thể thấy claim dựa vào observation nào, assumption nào đang gánh inference, và evidence nào thực sự có thể khiến kết luận thay đổi.