# Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Perplexity không đủ** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Năng lực (capability / 역량) benchmarks** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

LLM evaluation khó hơn traditional software testing vì đầu ra (output / 출력) không gian (space / 공간) rộng, nhiều answers có thể acceptable và hành vi (behavior / 동작) phụ thuộc prompt/ngữ cảnh (context / 맥락). Một evaluation tốt phải trả lời **mô hình (model / 모델)/hệ thống (system / 시스템) tốt cho tác vụ (task / 작업) nào, trên population nào, với chỉ số (metric / 지표) nào và dưới các ràng buộc (constraints / 제약조건들) nào**.

## Perplexity không đủ

Pretraining thường monitor cross-entropy/perplexity. Perplexity thấp hơn nghĩa mô hình (model / 모델) predict held-out tokens tốt hơn:

\[
PPL=\exp\left(-\frac{1}{N}\sum_i \log P(x_i\mid x_{<i})\right)
\]

Nhưng perplexity không trực tiếp đo instruction following, factuality, coding tính đúng đắn (correctness / 정확성) hay an toàn (safety / 안전).

Mô hình (model / 모델) A có perplexity tốt hơn nhưng ứng dụng (application / 애플리케이션) hiệu năng (performance / 성능) có thể kém hơn mô hình (model / 모델) B do post-training khác.

> **Chuyển mạch:** Trong **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Năng lực (capability / 역량) benchmarks** tiếp nhận điểm tựa từ **Perplexity không đủ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Contamination** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Năng lực (capability / 역량) benchmarks

Benchmarks đo slices như mathematics, coding, kiến thức (knowledge / 지식), reading comprehension hoặc multilingual tasks. Chúng hữu ích để compare controlled capabilities nhưng dễ bị overinterpreted.

Một benchmark score chỉ valid cho dataset, prompt giao thức (protocol / 프로토콜), evaluator và mô hình (model / 모델) phiên bản (version / 버전) cụ thể.

> **Chuyển mạch:** Ở chặng này của **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Contamination** tiếp nhận điểm tựa từ **Năng lực (capability / 역량) benchmarks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chính xác (exact / 정확한) match vs ngữ nghĩa (semantic / 의미적) chất lượng (quality / 품질)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Contamination

Nếu benchmark examples hoặc near-duplicates xuất hiện trong dữ liệu huấn luyện (training data / 학습 데이터), score có thể overestimate generalization.

Contamination khó phát hiện hoàn toàn với proprietary huấn luyện (training / 학습) corpora. Vì vậy fresh/private eval sets có giá trị lớn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Chính xác (exact / 정확한) match vs ngữ nghĩa (semantic / 의미적) chất lượng (quality / 품질)** tiếp nhận điểm tựa từ **Contamination** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pairwise evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chính xác (exact / 정확한) match vs ngữ nghĩa (semantic / 의미적) chất lượng (quality / 품질)

Structured tasks như classification có thể dùng chính xác (exact / 정확한) match. Open-ended answer cần ngữ nghĩa (semantic / 의미적) grading.

LLM-as-judge có thể score relevance/tính đúng đắn (correctness / 정확성) nhưng evaluator mô hình (model / 모델) cũng có biases, position preference và style độ lệch (bias / 편향).

Human evaluation vẫn quan trọng cho ambiguous/high-value tasks.

> **Chuyển mạch:** Trong **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Pairwise evaluation** tiếp nhận điểm tựa từ **Chính xác (exact / 정확한) match vs ngữ nghĩa (semantic / 의미적) chất lượng (quality / 품질)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Task-specific evals** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pairwise evaluation

Thay vì chấm absolute score, evaluator chọn phản hồi (response / 응답) A hay B tốt hơn. Pairwise comparison thường dễ và consistent hơn rubric 1–10.

Nhưng thứ tự (ordering / 순서) độ lệch (bias / 편향) và tie handling cần điều khiển (control / 제어).

> **Chuyển mạch:** Ở chặng này của **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Task-specific evals** tiếp nhận điểm tựa từ **Pairwise evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Golden set** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Task-specific evals

Môi trường vận hành (production / 운영 환경) eval nên reflect actual người dùng (user / 사용자) tải công việc (workload / 워크로드). Ví dụ hỗ trợ (support / 지원) assistant cần đo:

```text
correct resolution
policy adherence
citation support
escalation accuracy
latency
cost
```

Generic benchmark không thay thế tác vụ (task / 작업) eval.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Golden set** tiếp nhận điểm tựa từ **Task-specific evals** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lỗi (error / 오류) taxonomy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Golden set

Một curated **golden set** gồm representative cases, edge cases và known failures. Nó nên versioned và chạy regression khi đổi mô hình (model / 모델), prompt, RAG hoặc công cụ (tool / 도구) mã (code / 코드).

Không nên tune liên tục trên same golden set rồi vẫn gọi nó unbiased kiểm thử (test / 테스트).

> **Chuyển mạch:** Trong **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Lỗi (error / 오류) taxonomy** tiếp nhận điểm tựa từ **Golden set** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Evaluation ngăn xếp (stack / 스택)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lỗi (error / 오류) taxonomy

Aggregate score che thất bại (failure / 실패) modes. Nên categorize errors:

- factual lỗi (error / 오류);
- instruction miss;
- lập luận (reasoning / 추론) lỗi (error / 오류);
- retrieval miss;
- citation mismatch;
- formatting lỗi (error / 오류);
- unsafe hành vi (behavior / 동작);
- công cụ (tool / 도구) misuse.

Taxonomy giúp biết tầng (layer / 계층) nào cần fix.

> **Chuyển mạch:** Ở chặng này của **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Evaluation ngăn xếp (stack / 스택)** tiếp nhận điểm tựa từ **Lỗi (error / 오류) taxonomy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Offline và online evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Evaluation ngăn xếp (stack / 스택)

Một AI ứng dụng (application / 애플리케이션) nên có nhiều tầng:

```text
unit tests for deterministic code
retrieval tests
model response evals
end-to-end workflow evals
online monitoring
human review
```

Không có một benchmark duy nhất cover tất cả.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Offline và online evaluation** tiếp nhận điểm tựa từ **Evaluation ngăn xếp (stack / 스택)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LLM-as-judge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Offline và online evaluation

Offline eval reproducible và safe. Online eval phản ánh real traffic nhưng chịu confounding và rủi ro (risk / 위험).

A/B testing đo sản phẩm (product / 제품) kết quả (outcome / 결과) nhưng cần cỡ mẫu (sample size / 표본 크기), guardrails và careful interpretation.

> **Chuyển mạch:** Trong **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **LLM-as-judge** tiếp nhận điểm tựa từ **Offline và online evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Factuality eval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LLM-as-judge

Judge mô hình (model / 모델) có thể quy mô (scale / 규모) evaluation cho open-ended văn bản (text / 텍스트). Rubric phải tường minh (explicit / 명시적) và ideally judge should receive tham chiếu (reference / 참조)/bằng chứng (evidence / 증거) when relevant.

Risks:

```text
self-preference
verbosity bias
position bias
shared model blind spots
prompt sensitivity
```

Calibration với human labels giúp biết judge đáng tin ở đâu.

> **Chuyển mạch:** Ở chặng này của **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Factuality eval** tiếp nhận điểm tựa từ **LLM-as-judge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tool-use eval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Factuality eval

Nếu answer phải grounded, evaluator nên check claims against nguồn (source / 소스). Có thể decompose phản hồi (response / 응답) thành atomic claims rồi verify entailment.

Một overall “looks correct” score thường quá coarse.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Tool-use eval** tiếp nhận điểm tựa từ **Factuality eval** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **An toàn (safety / 안전) evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tool-use eval

Tác nhân (agent / 에이전트)/công cụ (tool / 도구) mô hình (model / 모델) cần evaluate:

```text
tool selection
argument correctness
schema validity
recovery from tool error
unnecessary tool calls
final answer based on result
```

Tác vụ (task / 작업) success quan trọng hơn tool-call cú pháp (syntax / 문법) đơn thuần.

> **Chuyển mạch:** Trong **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **An toàn (safety / 안전) evaluation** tiếp nhận điểm tựa từ **Tool-use eval** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Robustness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## An toàn (safety / 안전) evaluation

An toàn (safety / 안전) eval cần benign + adversarial prompts, multilingual variants và transformations. Chỉ kiểm thử (test / 테스트) obvious harmful phrase không đủ.

Đồng thời phải đo over-refusal trên benign tasks.

> **Chuyển mạch:** Ở chặng này của **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Robustness** tiếp nhận điểm tựa từ **An toàn (safety / 안전) evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Statistical bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Robustness

Paraphrase cùng yêu cầu (request / 요청) nhiều cách. Nếu score biến động lớn, mô hình (model / 모델) hành vi (behavior / 동작) brittle.

Perturbation tests gồm typo, long ngữ cảnh (context / 맥락), irrelevant distraction và conflicting bằng chứng (evidence / 증거).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Statistical bất định (uncertainty / 불확실성)** tiếp nhận điểm tựa từ **Robustness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cost-quality frontier** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Statistical bất định (uncertainty / 불확실성)

Benchmark score là estimate từ finite samples. Difference nhỏ có thể không statistically meaningful.

Confidence interval hoặc bootstrap hữu ích khi compare các mô hình (models / 모델들).

> **Chuyển mạch:** Trong **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Cost-quality frontier** tiếp nhận điểm tựa từ **Statistical bất định (uncertainty / 불확실성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Eval-driven development** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cost-quality frontier

Môi trường vận hành (production / 운영 환경) mô hình (model / 모델) selection thường là multi-objective:

\[
chất lượng (quality / 품질), độ trễ (latency / 지연 시간), chi phí (cost / 비용), độ tin cậy (reliability / 신뢰성)
\]

Mô hình (model / 모델) tốt nhất về benchmark có thể không tốt nhất về nghiệp vụ (business / 비즈니스) hệ thống (system / 시스템).

Plot chất lượng (quality / 품질) vs chi phí (cost / 비용)/độ trễ (latency / 지연 시간) giúp chọn Pareto frontier.

> **Chuyển mạch:** Ở chặng này của **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Eval-driven development** tiếp nhận điểm tựa từ **Cost-quality frontier** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Eval-driven development

Workflow tốt:

```text
collect failures
→ convert to regression evals
→ change prompt/model/system
→ rerun eval suite
→ deploy guarded
→ monitor new failures
```

Evaluation không phải final stage; nó là vòng phản hồi (feedback loop / 피드백 루프) của AI kỹ thuật (engineering / 엔지니어링).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Eval-driven development** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Một mô hình (model / 모델) không có “chất lượng” tuyệt đối. Chất lượng luôn là **hiệu năng (performance / 성능) phân phối (distribution / 분포) trên một tác vụ (task / 작업)/population under a giao thức (protocol / 프로토콜)**.

> **Chuyển mạch:** Trong **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Benchmark cao hơn = mô hình (model / 모델) tốt hơn mọi mặt”

Không. Benchmarks đo slices.

### “LLM judge thay thế human hoàn toàn”

Không. Judge cần calibration và kiểm tra (audit / 감사).

### “Một kiểm thử (test / 테스트) set dùng mãi vẫn unbiased”

Nếu nhóm (team / 팀) tune theo nó, nó trở thành development tín hiệu (signal / 신호).

> **Chuyển mạch:** Ở chặng này của **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

LLM evaluation nối [Machine Learning Evaluation](../04_machine_learning/15_model_evaluation.md), RAG evaluation, tác nhân (agent / 에이전트) evaluation và LLMOps monitoring.

Xem tiếp: [LLM Limitations](./15_llm_limitations.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
