# Red-team, Steelman & Disconfirmation — Phản biện để cập nhật model

Red-team trong reasoning không phải phản đối mọi đề xuất. Nó là một vòng kiểm tra có điều kiện: diễn đạt argument mạnh nhất, tìm cách làm nó thất bại, rồi cập nhật mức tin tưởng theo evidence. Formal logic, causal inference và domain evidence vẫn thuộc owner tương ứng; drill này luyện kỷ luật không bảo vệ conclusion chỉ vì đã đầu tư vào nó.

## 1. Steelman trước khi tấn công

Viết version mạnh nhất của argument:

```text
goal / claim
mechanism
best evidence
assumptions
boundary
trade-off accepted
```

Người đưa argument phải có thể xác nhận “đúng, đó là phiên bản tôi muốn bảo vệ”. Nếu chưa làm được, red-team đang đánh vào caricature chứ chưa kiểm tra model.

## 2. Chọn điểm yếu có khả năng phân biệt

Không liệt kê mọi objection. Chọn assumption mà nếu sai sẽ làm action, ranking hoặc safety boundary đổi. Câu hỏi tốt là:

```text
Nếu claim đúng, điều gì nên quan sát được?
Nếu claim sai, điều gì sẽ khác?
Test nào phân biệt hai thế giới với chi phí/rủi ro chấp nhận được?
```

Một counterargument chỉ nói “có thể khác” chưa đủ; cần prediction hoặc evidence có thể làm confidence giảm.

## 3. Disconfirmation không đồng nghĩa tìm một ngoại lệ

Một counterexample nhỏ có thể làm claim tuyệt đối sai, nhưng không tự bác bỏ một claim xác suất hoặc claim có boundary. Ghi rõ loại claim trước khi chấm kết quả:

```text
universal → one valid counterexample có thể đủ
probabilistic → cần cập nhật mức độ / base rate
causal → cần kiểm tra design, confounder và alternative
normative → cần tranh luận value criteria, không giả làm fact
```

## 4. Drill A — Ba context

Lặp template trong ba bối cảnh:

1. **Project/engineering:** proposal nói rollout sẽ giảm incident.
2. **Policy/business:** metric tăng được diễn giải là outcome tốt hơn.
3. **AI-generated claim:** câu trả lời trôi chảy được xem là đã xác minh.

Mỗi context phải có một test disconfirming, một evidence không đủ để kết luận và một update rule. Với claim AI, kiểm tra provenance, phiên bản, source gốc và khả năng tái tạo; không chấm độ tự tin dựa trên văn phong.

## 5. Red-team theo tầng rủi ro

Quick pass: hỏi một alternative mạnh nhất và một điều làm đổi ý. Normal pass: chạy test trên data/sample nhỏ và ghi expected result. Deep pass: mời người có incentive hoặc domain khác dựng phản biện, kiểm tra common-cause failure và đặt stop/rollback condition.

Depth phải theo stakes × uncertainty × irreversibility. Red-team một lựa chọn dễ đảo ngược không cần biến thành adversarial review kéo dài; decision không thể đảo ngược cần evidence và boundary nghiêm hơn.

## 6. Score và review

Chấm 0–2 điểm cho mỗi mục:

```text
steelman trung thực
assumption critical đã chọn
test có khả năng phân biệt
evidence provenance rõ
update rule định trước
boundary không bị mở rộng tùy tiện
```

Sau khi test, ghi `đã bác bỏ`, `làm yếu`, `không đổi`, hoặc `tăng confidence`. Nếu test không phân biệt được, đừng gọi nó là disconfirmation; đưa uncertainty sang [Value of Information](../value-of-information/README.md).

## 7. Failure modes

- **Contrarian reflex:** phản đối để thể hiện độc lập, không có prediction.
- **Moving goalposts:** đổi tiêu chuẩn sau khi test bất lợi.
- **Steelman giả:** thêm assumption mà người đưa claim không hề có.
- **Single counterexample overreach:** dùng một ngoại lệ để bác claim có boundary khác.
- **Red-team theater:** tìm flaw nhưng không đổi action, guardrail hoặc confidence.

## Template tái sử dụng

```text
Claim / decision:
Steelman:
Critical assumption:
Strongest alternative:
Disconfirming prediction:
Test and provenance:
Expected result if claim is true:
Expected result if claim is false:
Observed result:
Update: reject / weaken / unchanged / strengthen
Action or guardrail change:
Review date:
```

Red-team tốt không đảm bảo claim sai hay đúng; nó làm cho lý do giữ claim trở nên có điều kiện, truy được và dễ cập nhật hơn.

## Connections

- [Critical Thinking](../critical-thinking/README.md): argument, source và inference.
- [Causal Reasoning](../causal-reasoning/README.md): competing hypotheses và intervention.
- [Model Selection](../model-selection/README.md): discriminating evidence và model mismatch.
- [Cognitive Bias](../cognitive-bias/README.md): confirmation, anchoring và sunk cost.
- [Decision Making](../decision-making/README.md): update rule, reversibility và stop condition.
