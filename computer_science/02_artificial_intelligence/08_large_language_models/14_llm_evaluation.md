# Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Evaluation của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Perplexity không đủ** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Năng lực (capability / 역량) benchmarks** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối LLM evaluation với benchmark, task, metric và contamination, để điểm số phản ánh năng lực nào.

LLM evaluation khó hơn traditional software testing vì đầu ra (output / 출력) không gian (space / 공간) rộng, nhiều answers có thể acceptable và hành vi (behavior / 동작) phụ thuộc prompt/ngữ cảnh (context / 맥락). Một evaluation tốt phải trả lời **mô hình (model / 모델)/hệ thống (system / 시스템) tốt cho tác vụ (task / 작업) nào, trên population nào, với chỉ số (metric / 지표) nào và dưới các ràng buộc (constraints / 제약조건들) nào**.

## Perplexity không đủ

Pretraining thường monitor cross-entropy/perplexity. Perplexity thấp hơn nghĩa mô hình (model / 모델) predict held-out tokens tốt hơn:

\[
PPL=\exp\left(-\frac{1}{N}\sum_i \log P(x_i\mid x_{<i})\right)
\]

Nhưng perplexity không trực tiếp đo instruction following, factuality, coding tính đúng đắn (correctness / 정확성) hay an toàn (safety / 안전).

Mô hình (model / 모델) A có perplexity tốt hơn nhưng ứng dụng (application / 애플리케이션) hiệu năng (performance / 성능) có thể kém hơn mô hình (model / 모델) B do post-training khác.

Perplexity đo một khía cạnh của dự đoán token, còn benchmark capability đặt mô hình vào một tác vụ cụ thể. Trước khi diễn giải điểm benchmark, cần kiểm tra dữ liệu có thể đã xuất hiện trong training hay chưa.

## Năng lực (capability / 역량) benchmarks

Benchmarks đo slices như mathematics, coding, kiến thức (knowledge / 지식), reading comprehension hoặc multilingual tasks. Chúng hữu ích để compare controlled capabilities nhưng dễ bị overinterpreted.

Một benchmark score chỉ valid cho dataset, prompt giao thức (protocol / 프로토콜), evaluator và mô hình (model / 모델) phiên bản (version / 버전) cụ thể.

Contamination có thể làm điểm benchmark cao hơn khả năng khái quát thật, nhất là khi dữ liệu huấn luyện hoặc bản sao gần của đề đã bị lộ. Sau khi xem xét contamination, ta vẫn phải chọn tiêu chí chấm phù hợp với mục tiêu của task.

## Contamination

Nếu benchmark examples hoặc near-duplicates xuất hiện trong dữ liệu huấn luyện (training data / 학습 데이터), score có thể overestimate generalization.

Contamination khó phát hiện hoàn toàn với proprietary huấn luyện (training / 학습) corpora. Vì vậy fresh/private eval sets có giá trị lớn.

Exact match phù hợp với đầu ra có quy tắc rõ, còn semantic quality cần xét nghĩa, lập luận hoặc mức hữu ích. Khi không có một đáp án duy nhất, pairwise evaluation thường cho tín hiệu dễ so sánh hơn.

## Chính xác (exact / 정확한) match vs ngữ nghĩa (semantic / 의미적) chất lượng (quality / 품질)

Structured tasks như classification có thể dùng chính xác (exact / 정확한) match. Open-ended answer cần ngữ nghĩa (semantic / 의미적) grading.

LLM-as-judge có thể score relevance/tính đúng đắn (correctness / 정확성) nhưng evaluator mô hình (model / 모델) cũng có biases, position preference và style độ lệch (bias / 편향).

Human evaluation vẫn quan trọng cho ambiguous/high-value tasks.

Pairwise evaluation yêu cầu người hoặc judge chọn câu trả lời tốt hơn trong cùng một prompt, nhưng kết quả phụ thuộc thứ tự, tiêu chí và cách xử lý tie. Nó chỉ có ý nghĩa khi task cụ thể và rubric được mô tả rõ.

## Pairwise evaluation

Thay vì chấm absolute score, evaluator chọn phản hồi (response / 응답) A hay B tốt hơn. Pairwise comparison thường dễ và consistent hơn rubric 1–10.

Nhưng thứ tự (ordering / 순서) độ lệch (bias / 편향) và tie handling cần điều khiển (control / 제어).

Task-specific evals mô phỏng chính các quyết định mà sản phẩm cần hỗ trợ, vì vậy thường hữu ích hơn một điểm tổng quát. Để giữ chuẩn đánh giá ổn định qua các lần sửa, nhóm cần một golden set được quản lý như tài sản kiểm thử.

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

Golden set giúp so sánh các phiên bản trên những trường hợp đại diện đã được xem xét kỹ, nhưng không nên bị dùng đi dùng lại để tune đến mức mất tính độc lập. Khi phát hiện điểm yếu, cần phân loại lỗi thay vì chỉ nhìn một con số tổng.

## Golden set

Một curated **golden set** gồm representative cases, edge cases và known failures. Nó nên versioned và chạy regression khi đổi mô hình (model / 모델), prompt, RAG hoặc công cụ (tool / 도구) mã (code / 코드).

Không nên tune liên tục trên same golden set rồi vẫn gọi nó unbiased kiểm thử (test / 테스트).

Error taxonomy biến các failure thành nhóm có thể hành động, chẳng hạn factuality, instruction following, safety hoặc tool use. Những nhóm này tạo thành các lớp của evaluation stack từ dữ liệu đến hành vi sản phẩm.

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

Evaluation stack có thể gồm unit/model checks, task suites, safety tests, system integration và production outcomes. Không có lớp nào thay thế hoàn toàn lớp khác, nên cần nối offline với online evaluation.

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

Offline evaluation cho phép lặp nhanh trên dữ liệu cố định; online evaluation đo hành vi trong traffic thật nhưng chịu nhiễu và rủi ro sản phẩm. LLM-as-judge có thể mở rộng chấm điểm, miễn là được hiệu chuẩn với human labels.

## Offline và online evaluation

Offline eval reproducible và safe. Online eval phản ánh real traffic nhưng chịu confounding và rủi ro (risk / 위험).

A/B testing đo sản phẩm (product / 제품) kết quả (outcome / 결과) nhưng cần cỡ mẫu (sample size / 표본 크기), guardrails và careful interpretation.

LLM-as-judge tiết kiệm công sức khi so sánh nhiều đầu ra, nhưng có thể thiên vị phong cách, verbosity hoặc model family. Cần kiểm tra judge trên một tập nhãn người trước khi dùng nó để đánh giá factuality.

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

Factuality evaluation phải kiểm tra claim với bằng chứng hoặc nguồn chuẩn, thay vì chỉ hỏi câu trả lời có nghe thuyết phục không. Với agent, factuality còn phụ thuộc việc công cụ được gọi đúng và kết quả công cụ được dùng đúng.

## Factuality eval

Nếu answer phải grounded, evaluator nên check claims against nguồn (source / 소스). Có thể decompose phản hồi (response / 응답) thành atomic claims rồi verify entailment.

Một overall “looks correct” score thường quá coarse.

Tool-use evaluation nên đo task success, lựa chọn công cụ, tham số, thứ tự gọi và cách xử lý lỗi, chứ không chỉ đếm cú pháp tool call. Những hành vi đó cũng cần được đặt trong safety evaluation.

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

Safety evaluation bao gồm cả khả năng từ chối đúng và tránh over-refusal trên tác vụ lành tính. Một hệ thống an toàn cũng cần giữ hiệu năng khi prompt, context hoặc nguồn dữ liệu bị thay đổi.

## An toàn (safety / 안전) evaluation

An toàn (safety / 안전) eval cần benign + adversarial prompts, multilingual variants và transformations. Chỉ kiểm thử (test / 테스트) obvious harmful phrase không đủ.

Đồng thời phải đo over-refusal trên benign tasks.

Robustness tests các biến thể như typo, context dài, distraction và bằng chứng mâu thuẫn để xem kết luận có thay đổi bất thường không. Vì mỗi phép đo vẫn có nhiễu, cần lượng hóa bất định thống kê khi so sánh model.

## Robustness

Paraphrase cùng yêu cầu (request / 요청) nhiều cách. Nếu score biến động lớn, mô hình (model / 모델) hành vi (behavior / 동작) brittle.

Perturbation tests gồm typo, long ngữ cảnh (context / 맥락), irrelevant distraction và conflicting bằng chứng (evidence / 증거).

Confidence interval, bootstrap hoặc repeated runs giúp phân biệt cải thiện thật với dao động lấy mẫu. Khi đã biết độ bất định, ta có thể đặt chất lượng cạnh chi phí và độ trễ để chọn operating point.

## Statistical bất định (uncertainty / 불확실성)

Benchmark score là estimate từ finite samples. Difference nhỏ có thể không statistically meaningful.

Confidence interval hoặc bootstrap hữu ích khi compare các mô hình (models / 모델들).

Cost-quality frontier biểu diễn các lựa chọn đánh đổi giữa chất lượng, latency và chi phí, thay vì giả định model lớn nhất luôn tốt nhất. Những phép đo này trở nên hữu ích nhất khi được đưa vào vòng lặp phát triển hằng ngày.

## Cost-quality frontier

Môi trường vận hành (production / 운영 환경) mô hình (model / 모델) selection thường là multi-objective:

\[
chất lượng (quality / 품질), độ trễ (latency / 지연 시간), chi phí (cost / 비용), độ tin cậy (reliability / 신뢰성)
\]

Mô hình (model / 모델) tốt nhất về benchmark có thể không tốt nhất về nghiệp vụ (business / 비즈니스) hệ thống (system / 시스템).

Plot chất lượng (quality / 품질) vs chi phí (cost / 비용)/độ trễ (latency / 지연 시간) giúp chọn Pareto frontier.

Eval-driven development biến failure đã quan sát thành test hồi quy, rồi dùng kết quả test để hướng dẫn thay đổi tiếp theo. Mô hình tư duy sau đây tóm tắt cách đọc một con số evaluation mà không tách nó khỏi giao thức và bối cảnh.

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

Mental model đúng là: chọn task và population, cố định protocol, đo nhiều lớp, xem bất định, rồi nối điểm đo với quyết định sản phẩm. Các ngộ nhận sau đây thường phá vỡ một trong những bước đó.

## Mô hình tư duy (mental model / 사고 모델)

> Một mô hình (model / 모델) không có “chất lượng” tuyệt đối. Chất lượng luôn là **hiệu năng (performance / 성능) phân phối (distribution / 분포) trên một tác vụ (task / 작업)/population under a giao thức (protocol / 프로토콜)**.

Không có benchmark duy nhất đại diện cho “chất lượng tổng thể”, và một score không thể tách khỏi dataset, prompt, evaluator và phiên bản model. Phần cuối nối các lớp đánh giá này với tài liệu rộng hơn về LLM engineering.

## Dùng chung (common / 공통) Misconceptions

### “Benchmark cao hơn = mô hình (model / 모델) tốt hơn mọi mặt”

Không. Benchmarks đo slices.

### “LLM judge thay thế human hoàn toàn”

Không. Judge cần calibration và kiểm tra (audit / 감사).

### “Một kiểm thử (test / 테스트) set dùng mãi vẫn unbiased”

Nếu nhóm (team / 팀) tune theo nó, nó trở thành development tín hiệu (signal / 신호).

Các liên kết dưới đây đặt evaluation vào mạch rộng hơn của prompting, grounding, safety và MLOps. Người học có thể lần theo chúng để biến một phép đo thành quyết định có thể kiểm chứng trong hệ thống.

## Liên kết kiến thức (knowledge connection / 지식 연결)

LLM evaluation nối [Machine Learning Evaluation](../04_machine_learning/15_model_evaluation.md), RAG evaluation, tác nhân (agent / 에이전트) evaluation và LLMOps monitoring.

Xem tiếp: [LLM Limitations](./15_llm_limitations.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
