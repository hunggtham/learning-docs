# Tác nhân (agent / 에이전트) Evaluation

> **Mạch đọc:** Đặt **tác nhân (agent / 에이전트) Evaluation** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **End-to-End tác vụ (task / 작업) Success** sang **Step-Level Evaluation**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Đánh giá tác nhân (agent / 에이전트) khó hơn đánh giá single mô hình (model / 모델) phản hồi (response / 응답) vì tác nhân (agent / 에이전트) tạo **trajectory** gồm nhiều decisions, công cụ (tool / 도구) calls và trạng thái (state / 상태) transitions. Một final answer đúng có thể đến từ trajectory nguy hiểm; một tác vụ (task / 작업) thất bại (fail / 실패) có thể do công cụ (tool / 도구) outage chứ không phải mô hình (model / 모델) lập luận (reasoning / 추론).

Do đó evaluation cần nhiều mức (level / 수준):

```text
step-level
trajectory-level
end-to-end task-level
system-level
```

## End-to-End tác vụ (task / 작업) Success

Chỉ số (metric / 지표) quan trọng nhất là tác vụ (task / 작업) có đạt acceptance criteria thật không.

Ví dụ coding tác vụ (task / 작업):

```text
required tests pass
no regression
requested behavior implemented
scope constraints respected
```

Không dùng self-reported “done” của mô hình (model / 모델) làm ground truth.

## Step-Level Evaluation

Mỗi quyết định (decision / 결정) có thể score:

- chọn đúng công cụ (tool / 도구)?
- arguments đúng?
- có dùng unnecessary công cụ (tool / 도구)?
- observation được interpret đúng?
- thử lại (retry / 재시도) appropriate?
- dangerous hành động (action / 동작) bị chặn?

Step metrics giúp localize thất bại (failure / 실패).

## Trajectory Evaluation

Hai agents đều hoàn thành tác vụ (task / 작업) nhưng trajectory khác:

```text
A: 5 steps, 1 retry, verified
B: 27 steps, repeated searches, accidental write then rollback
```

Final success alone không capture efficiency/rủi ro (risk / 위험).

Trajectory metrics:

```text
step count
tool calls
repeated-action rate
cost
latency
rollback count
approval count
unnecessary mutation count
```

## Efficiency

Có thể define normalized efficiency:

\[
E = \frac{utility}{chi phí (cost / 비용) + \lambda độ trễ (latency / 지연 시간) + \mu steps}
\]

Không có universal formula; mục đích là make sự đánh đổi (trade-off / 트레이드오프) tường minh (explicit / 명시적).

## Tool-Use Accuracy

Create kiểm thử (test / 테스트) cases mà correct công cụ (tool / 도구)/arguments known. Measure:

- công cụ (tool / 도구) selection accuracy;
- argument validity;
- ngữ nghĩa (semantic / 의미적) tính đúng đắn (correctness / 정확성);
- permission compliance.

## Retrieval/Research Agents

Ngoài answer chất lượng (quality / 품질) cần:

- nguồn (source / 소스) recall;
- citation tính đúng đắn (correctness / 정확성);
- nguồn (source / 소스) authority;
- claim–bằng chứng (evidence / 증거) alignment;
- unsupported claim tỷ lệ (rate / 비율).

## Agentic Coding

Metrics có thể:

- tests passed;
- patch tính đúng đắn (correctness / 정확성);
- regression tỷ lệ (rate / 비율);
- files changed beyond phạm vi (scope / 범위);
- compile/lint;
- bảo mật (security / 보안)/static-analysis issues;
- number of failed attempts.

## Planning Evaluation

Plan score theo:

```text
coverage of required subtasks
dependency correctness
executability
risk ordering
verification coverage
adaptability after failure
```

Một plan prose đẹp nhưng chứa non-existent công cụ (tool / 도구) là thất bại (fail / 실패).

## Bộ nhớ (memory / 메모리) Evaluation

Measure:

- relevant bộ nhớ (memory / 메모리) retrieval recall;
- stale fact usage;
- contradiction;
- unauthorized bộ nhớ (memory / 메모리) truy cập (access / 접근);
- bộ nhớ (memory / 메모리) ghi (write / 쓰기) precision;
- harmful persistence.

## An toàn (safety / 안전) Evaluation

Scenario suites phải kiểm thử (test / 테스트):

- direct prompt injection;
- indirect injection qua documents/web;
- privilege escalation;
- destructive hành động (action / 동작) yêu cầu (request / 요청);
- exfiltration attempt;
- ambiguous approval;
- conflicting instructions.

An toàn (safety / 안전) kiểm thử (test / 테스트) cần verify thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계), không chỉ mô hình (model / 모델) refusal văn bản (text / 텍스트).

## Deterministic kiểm thử (test / 테스트) môi trường (environment / 환경)

Công cụ (tool / 도구)/môi trường (environment / 환경) nên có simulator/sandbox để repeat trajectories.

Ví dụ fake email máy chủ (server / 서버), kiểm thử (test / 테스트) cơ sở dữ liệu (database / 데이터베이스), mock filesystem. Nếu mỗi evaluation run tác động môi trường vận hành (production / 운영 환경) trạng thái (state / 상태), kiểm thử (test / 테스트) không reproducible và nguy hiểm.

## Scenario-Based Evaluation

Tác nhân (agent / 에이전트) tasks đa dạng nên xây scenario dataset:

```text
normal success
missing information
transient tool failure
permission denied
conflicting records
stale state
user changes goal mid-task
malicious retrieved content
```

Mỗi scenario có expected invariants.

## Invariants

Thay vì yêu cầu chính xác (exact / 정확한) trajectory, enforce invariants:

```text
must not write before approval
must cite external factual claims
must not exceed budget
must verify after mutation
must preserve user data
```

Tác nhân (agent / 에이전트) có thể tìm different valid paths miễn invariants hold.

## LLM-as-Judge

LLM judge hữu ích cho ngữ nghĩa (semantic / 의미적) dimensions như relevance/style, nhưng không nên là sole evaluator cho factual/công cụ (tool / 도구) tính đúng đắn (correctness / 정확성).

Risks:

- judge độ lệch (bias / 편향);
- self-preference;
- prompt sensitivity;
- poor calibration.

Use deterministic checks và human labels làm anchors.

## Human Evaluation

Cần khi chất lượng (quality / 품질) subjective hoặc high-stakes. Human rubric phải rõ để inter-rater consistency tốt.

## Regression Testing

Mỗi thay đổi prompt/mô hình (model / 모델)/công cụ (tool / 도구) lược đồ (schema / 스키마) có thể đổi hành vi (behavior / 동작). Maintain fixed eval suite và compare before/after.

Không chỉ compare average; inspect trọng yếu (critical / 중요) scenario regressions.

## Online Evaluation

Môi trường vận hành (production / 운영 환경) metrics:

```text
task completion rate
user corrections
human escalation
abort/cancel rate
cost/task
p95 latency
unsafe action blocks
incident rate
```

A/B kiểm thử (test / 테스트) cần guardrail metrics, không chỉ người dùng (user / 사용자) engagement.

## Thất bại (failure / 실패) Taxonomy

Tag failures:

```text
MODEL_REASONING
TOOL_SELECTION
TOOL_EXECUTION
STATE_STALE
RETRIEVAL_MISS
PERMISSION
PLANNING
VERIFICATION_MISS
ORCHESTRATION
USER_AMBIGUITY
```

Taxonomy giúp biết nên fix prompt, công cụ (tool / 도구), dữ liệu (data / 데이터) hay thời gian chạy (runtime / 런타임).

## Credit Assignment

End-to-end thất bại (failure / 실패) qua 20 steps tạo challenge: step nào thực sự gây thất bại (fail / 실패)? dấu vết (trace / 추적) + structured trạng thái (state / 상태) giúp postmortem.

## Benchmark Leakage

Công khai (public / 공개) tác nhân (agent / 에이전트) benchmarks có thể contaminated trong dữ liệu huấn luyện (training data / 학습 데이터). nội bộ (internal / 내부) realistic tasks thường cho tín hiệu (signal / 신호) môi trường vận hành (production / 운영 환경) tốt hơn.

## Độ tin cậy (reliability / 신뢰성) Curve theo Horizon

Đo success theo number of required steps. Nếu hiệu năng (performance / 성능) sụt mạnh khi horizon > 5, thiết kế (design / 설계) cần more decomposition/checkpoints chứ không chỉ average benchmark.

## Cost-aware Evaluation

Mô hình (model / 모델) A success 90% với $1/tác vụ (task / 작업), mô hình (model / 모델) B 92% với $10/tác vụ (task / 작업). “Better” phụ thuộc nghiệp vụ (business / 비즈니스) utility và thất bại (failure / 실패) chi phí (cost / 비용).

## Mô hình tư duy (mental model / 사고 모델)

> **tác nhân (agent / 에이전트) evaluation phải đo kết quả (outcome / 결과), trajectory, an toàn (safety / 안전) và economics cùng lúc.**

Một demo thành công không nói gì về độ tin cậy (reliability / 신뢰성) phân phối (distribution / 분포).

## Dùng chung (common / 공통) Misconceptions

### “Benchmark mô hình (model / 모델) cao thì tác nhân (agent / 에이전트) sẽ cao”

Tác nhân (agent / 에이전트) chất lượng (quality / 품질) phụ thuộc tools, trạng thái (state / 상태), orchestration và môi trường (environment / 환경).

### “Final answer đúng là đủ”

Trajectory có thể vi phạm permission hoặc tạo side tác động (effect / 효과) sai rồi sửa lại.

### “LLM judge thay thế được kiểm thử (test / 테스트)”

Không cho deterministic properties như tệp (file / 파일) existence, giao dịch (transaction / 트랜잭션) trạng thái (state / 상태) hay permission.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Evaluation nối software testing, khả năng quan sát (observability / 관측 가능성), statistics và an toàn (safety / 안전) kỹ thuật (engineering / 엔지니어링). Chapter cuối chuyển các lessons thành thiết kế (design / 설계) principles cho reliable agents.

Xem tiếp: [Reliable Agent Design](./10_reliable_agent_design.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 from llm to agent](./00_from_llm_to_agent.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
