# Model Selection — Chọn mô hình phù hợp với câu hỏi

Model selection (lựa chọn mô hình / 모델 선택) trong `thinking/` không chỉ nói về statistical model. Nó là kỹ năng chọn **cách biểu diễn vấn đề** đủ tốt để hỗ trợ reasoning mà không thêm complexity không cần thiết.

Một model hữu ích luôn là simplification. Câu hỏi không phải “model này có đúng hoàn toàn không?” mà là **nó bỏ qua điều gì, và phần bị bỏ qua có quan trọng đối với decision hiện tại không?**

## 1. Bắt đầu từ question, không từ tool yêu thích

Sai lầm phổ biến:

```text
I know regression → mọi vấn đề thành regression
I know first principles → bỏ qua base rate
I know game theory → mọi interaction thành strategic game
I know systems thinking → vẽ feedback loop nhưng không đo gì
```

Workflow tốt hơn:

```text
question
→ target / outcome
→ constraints
→ available evidence
→ causal or predictive need
→ simplest adequate model
```

## 2. Description, prediction và causation là ba task khác nhau

Một model có thể mô tả dữ liệu rất tốt nhưng prediction kém ngoài sample. Một predictive model có thể dự báo tốt mà không xác định causal effect.

Luôn ghi rõ task:

```text
Describe?
Predict?
Explain mechanism?
Estimate intervention effect?
Optimize action?
```

Task khác nhau cần tiêu chuẩn đánh giá khác nhau.

## 3. Simplest adequate model

Đơn giản không có nghĩa sơ sài. Nó có nghĩa không thêm detail nếu detail đó không thay đổi inference hoặc decision đáng kể.

Ví dụ:

- tính tip: arithmetic model đủ;
- portfolio risk: cần probability/dependence;
- organizational policy: có thể cần incentives và strategic response;
- ecosystem hoặc distributed system: có thể cần systems thinking.

## 4. Assumptions là một phần của model

Không chỉ ghi formula; ghi assumptions khiến formula có ý nghĩa.

```text
Model
Assumptions
Inputs
Output
Valid domain
Failure modes
```

Một model chính xác trong domain A có thể sai nghiêm trọng khi extrapolate sang domain B.

## 5. Compare models bằng discriminating evidence

Nếu hai model đều giải thích observation hiện tại, hỏi:

> Chúng dự đoán khác nhau ở đâu?

Evidence hữu ích nhất thường là evidence làm hai explanations cho prediction khác nhau.

Đây là nơi [Value of Information](../value-of-information/README.md) trở thành công cụ chọn experiment/test tiếp theo.

## 6. Ensemble mindset

Nhiều decision thực tế cần nhiều lens:

```text
Probability → uncertainty
Economics → constraints / incentives
Psychology → behavior / bias
Systems → feedback / delay
Game theory → strategic response
Causal reasoning → intervention effect
```

Các lens không được cộng cơ học. Mỗi lens phải trả lời phần khác nhau của problem.

## 7. Model risk

Model risk xuất hiện khi decision phụ thuộc mạnh vào assumptions hoặc simplification sai.

Check:

- input nào nhạy nhất?
- có regime change không?
- correlation có stable không?
- actor có adapt khi model được dùng không?
- output có bị false precision không?

Trong finance, forecasting, policy hoặc engineering, model uncertainty có thể lớn hơn parameter uncertainty.

## 8. Stress test

Thay input hoặc assumption quan trọng:

```text
base case
→ optimistic case
→ adverse case
→ structural break case
```

Nếu action thay đổi hoàn toàn bởi một assumption yếu, decision cần thêm margin of safety hoặc information.

## 9. Stop rule

Model đủ dùng khi thêm complexity không thay đổi materially:

- ranking options;
- main risk;
- expected action;
- confidence level.

Không tối ưu model vì elegance nếu decision không hưởng lợi.

## Connections

- [Problem Framing](../problem-framing/README.md): xác định question trước model.
- [First Principles](../first-principles/README.md): build model từ mechanism khi cần.
- [Statistics for Life](../statistics-for-life/README.md): statistical model và uncertainty.
- [Causal Reasoning](../causal-reasoning/README.md): causal model vs predictive model.
- [Systems Thinking](../systems-thinking/README.md): dynamic feedback models.
- [Mathematics](../../mathematics/README.md): formal modeling.
- [Economics](../../economics/README.md): models, assumptions và comparative statics.