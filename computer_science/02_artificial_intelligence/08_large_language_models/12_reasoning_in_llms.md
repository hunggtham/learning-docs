# Reasoning trong Large Language Models

Khi nói một LLM “reasoning”, ta cần tách behavior quan sát được khỏi claim về cơ chế bên trong. Ở mức engineering, **reasoning** có thể hiểu là khả năng biến một problem thành chuỗi intermediate transformations giúp tăng xác suất tìm được answer đúng: decomposition, comparison, derivation, verification, search hoặc tool use.

Không cần giả định model suy nghĩ giống con người để đánh giá capability này. Câu hỏi hữu ích hơn là: model có thể giải bài toán nhiều bước ổn định đến đâu, failure mode nào xuất hiện, và external computation có cải thiện reliability không?

## Direct answer vs intermediate computation

Một prompt có thể yêu cầu model trả lời trực tiếp hoặc tạo intermediate steps. Với tasks nhiều bước, việc tạo scratch reasoning có thể giúp vì model có thêm token positions để thực hiện computation tuần tự.

Mental model:

```text
single-step decoding
vs
allocate more inference tokens to transform the problem
```

Tuy nhiên reasoning text dài không tự động đúng. Model có thể tạo một explanation coherent cho answer sai.

## Decomposition

Complex problem thường dễ hơn khi tách thành subproblems:

```text
understand goal
→ extract known facts
→ solve subproblem A
→ solve subproblem B
→ combine
→ verify
```

Decomposition giảm effective search complexity nếu subproblems đúng. Nếu decomposition sai từ đầu, downstream steps có thể consistent nhưng wrong.

## Chain-of-thought-like prompting

Demonstrations có intermediate steps đôi khi cải thiện performance trên arithmetic, symbolic và compositional tasks. Lý do thực dụng là model được dẫn vào distribution nơi solution unfolds qua nhiều tokens thay vì ép compress computation vào next-token answer ngắn.

Nhưng visible reasoning không nên được xem là guaranteed faithful transcript của internal computation. Output explanation itself là generated text.

## Self-consistency

Một strategy là sample multiple reasoning paths rồi aggregate final answers. Nếu independent paths có chance đúng lớn hơn random và errors không perfectly correlated, voting có thể cải thiện accuracy.

Cost tăng gần theo số samples. Nếu model có systematic misconception, self-consistency chỉ tạo nhiều phiên bản cùng một lỗi.

## Search over reasoning paths

Thay vì sample một trajectory, system có thể branch candidate steps, score, prune và continue. Đây là connection trực tiếp với classical search.

```text
state = partial solution
operator = propose next reasoning step
heuristic = verifier/value model
search = choose paths to expand
```

LLM trở thành proposal model bên trong search system.

## Verification

Reasoning reliability tăng mạnh khi intermediate/final result có thể kiểm tra bằng deterministic tool:

- calculator;
- compiler;
- SQL engine;
- theorem prover;
- unit tests;
- symbolic algebra.

Pattern mạnh:

```text
LLM proposes
→ external verifier checks
→ model revises if needed
```

Đây thường đáng tin hơn “model tự tin hơn”.

## Tool-augmented reasoning

Một LLM không cần internalize mọi operation. Với arithmetic lớn, gọi calculator hợp lý hơn sinh phép tính token-by-token. Với current data, query API tốt hơn đoán.

Intelligence system-level đến từ việc chọn đúng tool và integrate result đúng cách.

## Reasoning và latent computation

Một phần computation xảy ra trong hidden states trước mỗi token. Visible rationale chỉ là một projection thành language. Vì vậy absence of long rationale không đồng nghĩa absence of computation, và presence of rationale không guarantee fidelity.

Engineering evaluation nên đo task success, verification và robustness, không đo “trông có vẻ suy nghĩ”.

## Test-time compute

Cho model thêm inference tokens, multiple samples, search hoặc verifier calls là một cách tăng **test-time compute**. Đây là axis khác model scale.

Trade-off:

```text
more compute → potentially better reliability
but → higher latency/cost
```

Application cần chọn budget theo task risk.

## Planning vs reasoning

Reasoning thường biến information thành conclusion. Planning chọn sequence of actions để đạt goal trong environment.

LLM agent có thể dùng reasoning để tạo plan, nhưng plan quality còn phụ thuộc state tracking, action effects và environment feedback.

Xem: [Planning](../02_search_reasoning_and_planning/05_planning.md).

## Arithmetic failure

LLM language modeling không đảm bảo exact arithmetic. Digit-level carry operations là brittle khi sequence dài.

Calculator tool giải problem theo deterministic algorithm. Đây là example rõ rằng stronger system không nhất thiết cần model tự làm mọi computation.

## Logic failure

LLM có thể produce valid-sounding syllogism nhưng fail negation, quantifier hoặc adversarial wording. Formal solver có explicit semantics và proof rules.

Hybrid approach: model parse natural language → formal representation → solver verifies.

## Reasoning under uncertainty

Không phải problem nào có one exact answer. Bayesian/decision reasoning cần represent uncertainty và utility. LLM-generated certainty language không phải calibrated probability.

Nếu decision high stakes, explicit probabilistic model hoặc domain policy cần bổ sung.

## Faithfulness problem

Generated rationale có thể là post-hoc explanation. Model có thể arrive at answer through features khác với explanation nó viết.

Do đó không nên dùng chain-of-thought text làm sole audit trail cho regulated decisions.

## Hidden scratchpad vs user-facing explanation

Một system có thể separate internal computational process khỏi concise user explanation. User thường cần reasons/evidence có thể kiểm chứng hơn raw token-by-token scratch work.

Good explanation should cite premises, sources, calculations và uncertainty relevant.

## Reasoning benchmarks

Benchmarks như math/code/logical tasks đo slices của reasoning. High score không nghĩa universal reasoning competence.

Contamination, prompt sensitivity và verifier differences cũng ảnh hưởng score.

## Mental Model

> LLM reasoning đáng tin nhất khi được xem như **probabilistic proposal + structured decomposition + external verification/search**, không phải một oracle suy luận hoàn hảo.

## Common Misconceptions

### “Model viết reasoning dài nghĩa là reasoning sâu”

Length không guarantee correctness.

### “Nếu model reasoning tốt thì không cần tools”

Tools thường làm exact tasks đáng tin và rẻ hơn.

### “Reasoning là một capability đơn nhất”

Math, code, causal, planning và commonsense reasoning có failure modes khác nhau.

## Knowledge Connection

Reasoning nối Transformer/ICL với [Search](../02_search_reasoning_and_planning/00_state_space_and_search.md), [Logic](../03_knowledge_and_reasoning/03_inference_and_reasoning.md), Agents và tool use.

Xem tiếp: [Hallucination and Grounding](./13_hallucination_and_grounding.md).