# Multi-Agent các hệ thống (systems / 시스템들)

> **Mạch đọc:** Đặt **Multi-Agent các hệ thống (systems / 시스템들)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Vì sao dùng nhiều tác nhân (agent / 에이전트)?** sang **Role Specialization**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một **multi-agent hệ thống (system / 시스템)** có nhiều agents tương tác để hoàn thành tác vụ (task / 작업). Ý tưởng hấp dẫn vì có thể chia vai trò hoặc chạy subtasks song song, nhưng thêm tác nhân (agent / 에이전트) cũng thêm communication, coordination và thất bại (failure / 실패) modes.

```text
Coordinator
├── Research Agent
├── Coding Agent
├── Verification Agent
└── Domain Reviewer
```

## Vì sao dùng nhiều tác nhân (agent / 에이전트)?

Multi-agent hữu ích khi tác vụ (task / 작업) có decomposition tự nhiên:

- subtasks độc lập có thể parallelize;
- cần specialization/ngữ cảnh (context / 맥락) riêng;
- cần separation of duties;
- một tác nhân (agent / 에이전트) tạo sản phẩm tạo ra (artifact / 산출물) và tác nhân (agent / 에이전트) khác verify;
- cần simulate multiple stakeholders.

Không nên dùng chỉ để “tăng intelligence”.

## Role Specialization

Tác nhân (agent / 에이전트) có thể khác nhau về:

```text
instructions
available tools
permissions
context
model
memory
success criteria
```

Ví dụ verifier tác nhân (agent / 에이전트) chỉ có read/kiểm thử (test / 테스트) tools, không có ghi (write / 쓰기) permission. Separation này tăng độ tin cậy (reliability / 신뢰성) hơn việc prompt cùng mô hình (model / 모델) “hãy tự kiểm tra mình”.

## Coordinator mẫu (pattern / 패턴)

Coordinator phân tác vụ (task / 작업) và aggregate results.

```mermaid
flowchart TD
    C[Coordinator] --> A[Agent A]
    C --> B[Agent B]
    C --> D[Agent C]
    A --> C
    B --> C
    D --> C
```

Coordinator có thể trở thành bottleneck hoặc single điểm (point / 지점) of thất bại (failure / 실패).

## Blackboard mẫu (pattern / 패턴)

Agents đọc/ghi dùng chung (shared / 공유) workspace:

```text
shared task board / artifact store / state store
```

Coordinator nhẹ hơn, nhưng cần giải quyết xung đột (conflict resolution / 충돌 해결) và quyền sở hữu (ownership / 소유권) rules.

## Peer-to-Peer Debate

Agents critique proposals của nhau. Có thể tăng coverage, nhưng dễ tạo redundant đơn vị từ (token / 토큰) usage và false consensus.

Independent diversity chỉ có giá trị nếu agents thật sự có different bằng chứng (evidence / 증거)/roles, không phải clone cùng prompt.

## Producer–Verifier

Một mẫu (pattern / 패턴) mạnh:

```text
Producer creates solution
→ Verifier tests against independent criteria
→ Producer revises if needed
```

Verifier nên có independent bằng chứng (evidence / 증거)/tooling. Nếu verifier chỉ đọc prose của producer, correlated errors vẫn cao.

## Delegation đặc tả hợp đồng (contract / 계약)

Subtask giao cho tác nhân (agent / 에이전트) nên có:

```text
objective
inputs
allowed tools
output schema
completion criteria
budget
deadline
```

“Research this” quá mơ hồ.

## Communication chi phí (cost / 비용)

Nếu `n` agents all-to-all communicate, potential communication edges tăng gần:

\[
O(n^2)
\]

Vì vậy topology quan trọng. Hierarchical/coordinator patterns giảm chatter.

## Trạng thái dùng chung (shared state / 공유 상태) Consistency

Hai agents cùng edit sản phẩm tạo ra (artifact / 산출물) có thể xung đột (conflict / 충돌). Cần:

- locks;
- versioning;
- merge chiến lược (strategy / 전략);
- quyền sở hữu (ownership / 소유권) partition;
- sự kiện (event / 이벤트) thứ tự (ordering / 순서).

Multi-agent các hệ thống (systems / 시스템들) inherits phân tán (distributed / 분산) các hệ thống (systems / 시스템들) problems.

## Duplicate công việc (work / 작업)

Without tác vụ (task / 작업) registry, agents có thể cùng làm một subtask. Coordinator cần idempotent assignment hoặc dùng chung (shared / 공유) tác vụ (task / 작업) status.

## Trust Boundaries

Không phải tác nhân (agent / 에이전트) nào cũng nên có same permissions. Research tác nhân (agent / 에이전트) đọc web; deploy tác nhân (agent / 에이전트) có môi trường vận hành (production / 운영 환경) permission; verifier read-only.

Compromise một tác nhân (agent / 에이전트) không nên grant truy cập (access / 접근) toàn hệ thống (system / 시스템).

## Consensus không đảm bảo truth

Nếu ba agents cùng dùng same mô hình (model / 모델)/dữ liệu huấn luyện (training data / 학습 데이터), errors có thể correlated. Majority vote chỉ hiệu quả khi errors sufficiently independent.

## Multi-Agent vs Parallel công cụ (tool / 도구) Calls

Nhiều tác nhân (agent / 에이전트) không cần thiết nếu chỉ muốn fetch 5 APIs song song. Parallel tools trong một workflow đơn giản hơn.

Dùng multi-agent khi cần distinct lập luận (reasoning / 추론)/trạng thái (state / 상태)/permission boundaries, không chỉ tính đồng thời (concurrency / 동시성).

## Tác nhân (agent / 에이전트) Handoff

Handoff cần tường minh (explicit / 명시적) transfer trạng thái (state / 상태):

```text
what has been done
what evidence exists
what remains
constraints
artifact references
```

Không nên chỉ gửi raw transcript.

## Example: Software thay đổi (change / 변경)

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
Planner → identifies files/tests
Implementer → edits code
Tester → runs test suite
Reviewer → inspects diff against requirements
Coordinator → decides done/revise
```

Điểm mạnh là separation of duties; điểm yếu là độ trễ (latency / 지연 시간)/chi phí (cost / 비용).

## Example: Research

Agents có thể split sources theo region/criterion, sau đó aggregator merge. Citation provenance phải preserved xuyên handoffs.

## Evaluation

Đánh giá:

- end-to-end tác vụ (task / 작업) success;
- per-agent contribution;
- duplicated công việc (work / 작업);
- communication tokens;
- coordination độ trễ (latency / 지연 시간);
- xung đột (conflict / 충돌) tỷ lệ (rate / 비율);
- verifier catch tỷ lệ (rate / 비율).

Nếu multi-agent không tăng success đủ để bù chi phí (cost / 비용), kiến trúc (architecture / 아키텍처) là overengineering.

## Mô hình tư duy (mental model / 사고 모델)

> **Multi-agent là hệ thống phân tán (distributed system / 분산 시스템) của probabilistic workers.**

Điều khó không chỉ là lập luận (reasoning / 추론) từng tác nhân (agent / 에이전트) mà là tác vụ (task / 작업) allocation, communication, consistency và trust.

## Dùng chung (common / 공통) Misconceptions

### “Nhiều tác nhân (agent / 에이전트) sẽ tự nhiên thông minh hơn một tác nhân (agent / 에이전트)”

Không. Coordination overhead và correlated failures có thể làm tệ hơn.

### “tác nhân (agent / 에이전트) roles chỉ cần đổi hệ thống (system / 시스템) prompt”

Role mạnh hơn khi khác permissions, tools, ngữ cảnh (context / 맥락) và evaluation criteria.

### “Debate luôn tăng accuracy”

Debate có thể tạo verbosity hoặc reinforce dùng chung (common / 공통) lỗi (error / 오류) nếu bằng chứng (evidence / 증거) không independent.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Multi-agent các hệ thống (systems / 시스템들) nối phân tán (distributed / 분산) các hệ thống (systems / 시스템들), organizational thiết kế (design / 설계), workflow orchestration và ensemble lập luận (reasoning / 추론).

Xem tiếp: [Agent Orchestration](./08_agent_orchestration.md).
