# Argument & Evidence Mapping — Biến một claim thành cấu trúc có thể kiểm tra

Evidence mapping là bài luyện cho lúc một claim nghe hợp lý nhưng đường từ nguồn đến kết luận còn bị giấu. Nó không thay logic, causal inference hay study design; nó tạo artifact trung gian để biết bước nào là fact, bước nào là inference và bước nào cần update. Canonical theory đi về [Philosophy](../../philosophy/README.md) và [Research Methods](../../research_methods/README.md).

## 1. Viết claim ở dạng có thể bị phản bác

Đổi “sản phẩm này tốt”, “policy này hiệu quả” hoặc “AI trả lời đúng” thành claim có subject, outcome, population, thời gian và điều kiện. Nếu claim không thể nói bằng một câu mà evidence có thể làm yếu đi, chưa nên lập map.

Ví dụ:

```text
Trong workflow X, dưới điều kiện Y, intervention A giảm failure Z so với baseline B trong 30 ngày.
```

## 2. Tách sáu lớp của argument

Map tối thiểu phải có:

```text
claim
├── evidence for
├── evidence against
├── assumptions
├── inference
├── alternative explanations
├── confidence
└── evidence that would change conclusion
```

Evidence không tự nối vào claim; `inference` nói vì sao evidence được xem là liên quan. Assumption nói điều gì phải đúng để inference đứng vững. Nhờ tách hai lớp này, ta không gọi một khoảng trống logic là “thiếu data”.

## 3. Truy provenance trước khi chấm chất lượng

Ghi source gần claim nhất, source gốc mà nó dẫn lại, ngày/phiên bản, population và phương pháp. Một bài báo tóm tắt press release khác với study; ba bài copy cùng dataset không phải ba bằng chứng độc lập.

Nếu nguồn không truy được, đánh dấu `unknown provenance` thay vì tự cho điểm thấp hay cao. Với claim pháp lý, y tế, tài chính hoặc policy, chuyển sang canonical owner và nguồn chính thức trước khi dùng map để hành động.

## 4. Phân biệt loại evidence và độ mạnh của claim

Đọc evidence theo câu hỏi nó trả lời:

| Evidence | Hỗ trợ tốt hơn cho | Không tự chứng minh |
|---|---|---|
| Observation / anecdote | hiện tượng có thể xảy ra | prevalence hoặc causality |
| Descriptive data | quy mô/mô tả trong sample | intervention effect |
| Controlled comparison | khác biệt giữa nhóm/điều kiện | mọi population |
| Experiment / intervention | effect trong điều kiện thiết kế | mechanism và external validity đầy đủ |
| Synthesis | pattern giữa nhiều nghiên cứu | chất lượng nếu input yếu |

Bảng này là cách đọc, không phải thứ hạng tuyệt đối. Sau khi xếp loại, viết một câu boundary: “Evidence này cho phép nói X trong Y, chưa cho phép nói Z”.

## 5. Drill A — Ba claim khác context

Lập một map cho:

1. **News/statistic:** một headline nói X làm Y tăng.
2. **Product/workflow:** một vendor claim công cụ giảm thời gian hoặc lỗi.
3. **Research/health:** một study nói intervention thay đổi outcome.

Mỗi map phải có ít nhất một evidence against hoặc missing evidence, một alternative explanation và một điều kiện làm confidence đổi. Không dùng cùng một tiêu chuẩn “nguồn uy tín” cho cả ba context.

## 6. Scoring và feedback loop

Chấm từng map 0–2 điểm:

```text
claim cụ thể và có boundary
provenance truy được
inference được viết ra
assumption / alternative được nêu
evidence for và against cân bằng
update trigger cụ thể
```

Review sau một tuần hoặc sau khi có evidence mới: claim có đổi không, map có dự đoán đúng chỗ yếu không, và phần nào bị nhầm fact với inference. Nếu map thiếu evidence có khả năng đổi action, nối sang [Value of Information](../value-of-information/README.md).

## 7. Failure modes

- **Source count fallacy:** nhiều link nhưng cùng một provenance.
- **Authority substitution:** nguồn chính thức cho biết rule, nhưng không tự trả lời causal effect.
- **Evidence dumping:** gom tài liệu mà không viết inference.
- **Symmetry giả:** cho hai phía số link ngang nhau dù quality và relevance khác nhau.
- **Confidence không update:** map trở thành hồ sơ biện hộ cho conclusion cũ.

## Template tái sử dụng

```text
Exact claim:
Scope / population / time:
Source provenance:
Evidence for:
Evidence against:
Inference connecting evidence to claim:
Assumptions:
Alternative explanations:
Current confidence:
What would change conclusion:
Canonical owner / next source:
Review date:
```

Evidence map tốt không biến claim thành chân lý; nó cho người khác thấy phải kiểm tra khối nào trước và kết luận đang đứng trên điều kiện nào.

## Connections

- [Critical Thinking](../critical-thinking/README.md): claim, inference và steelman.
- [Causal Reasoning](../causal-reasoning/README.md): alternative explanations và counterfactual.
- [Statistics for Life](../statistics-for-life/README.md): denominator, sample và effect size.
- [Research Methods](../../research_methods/README.md): design, measurement và synthesis.
