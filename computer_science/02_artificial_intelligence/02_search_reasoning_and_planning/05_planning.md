# Planning trong Artificial Intelligence

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Planning trong AI**. Route đi từ reactive behavior → state/action/goal representation → classical planning operators → partial order/heuristic planning → execution monitoring, để plan được nối với môi trường và failure.

Tìm kiếm (search / 검색) hỏi “từ trạng thái (state / 상태) này, hành động (action / 동작) nào dẫn tới goal?”. **Planning (계획 / lập kế hoạch)** làm câu hỏi đó tường minh (explicit / 명시적) hơn bằng cách biểu diễn **actions có preconditions và effects**, goal có cấu trúc (structure / 구조), và một plan là chuỗi (sequence / 시퀀스) hoặc partial thứ tự (order / 순서) actions làm goal trở thành true.

Planning quan trọng vì intelligence không chỉ phản ứng với observation hiện tại. Nhiều tác vụ (task / 작업) cần reason về future consequences, prerequisites, tài nguyên (resource / 자원) conflicts và phụ thuộc (dependency / 의존성) giữa subgoals. Classical planning cung cấp vocabulary chính xác cho những vấn đề mà hiện đại (modern / 현대적) “AI tác nhân (agent / 에이전트) planning” thường mô tả rất loosely.

Xem trước: [State Space and Search](./00_state_space_and_search.md) và [Constraint Satisfaction](./04_constraint_satisfaction.md).

## Reactive hành vi (behavior / 동작) và planning khác nhau thế nào?

Reactive chính sách (policy / 정책):

```text
observation → action
```

Planning:

```text
current state + goal + model of actions
              ↓
reason about possible futures
              ↓
action sequence / policy
```

Reactive hành vi (behavior / 동작) nhanh và robust khi môi trường (environment / 환경) familiar. Planning hữu ích khi tác vụ (task / 작업) novel, long-horizon hoặc actions có delayed consequences.

Real agents thường combine both: plan high-level, react/replan low-level.

> **Chuyển mạch:** Trong **Planning trong Artificial Intelligence**, **Trạng thái (state / 상태) biểu diễn (representation / 표현) trong classical planning** tiếp nhận điểm tựa từ **Reactive hành vi (behavior / 동작) và planning khác nhau thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Actions: preconditions và effects** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trạng thái (state / 상태) biểu diễn (representation / 표현) trong classical planning

Một trạng thái (state / 상태) có thể represented bằng set propositions.

Example warehouse:

```text
At(robot, A)
BoxAt(box1, B)
HandEmpty(robot)
DoorOpen(B,C)
```

Closed-world giả định (assumption / 가정) trong many symbolic planners: proposition không listed được coi false. giả định (assumption / 가정) này convenient nhưng không phù hợp mọi real-world kiến thức (knowledge / 지식) setting.

> **Chuyển mạch:** Ở chặng này của **Planning trong Artificial Intelligence**, **Actions: preconditions và effects** tiếp nhận điểm tựa từ **Trạng thái (state / 상태) biểu diễn (representation / 표현) trong classical planning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **STRIPS-style biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Actions: preconditions và effects

Hành động (action / 동작) `Move(A,B)`:

```text
Preconditions:
  At(robot, A)
  Connected(A, B)

Effects:
  add At(robot, B)
  delete At(robot, A)
```

Hành động (action / 동작) applicable chỉ khi preconditions true.

Chuyển tiếp (transition / 전이) mô hình (model / 모델) được bản dựng (build / 빌드) từ effects.

This is more structured than generic successor hàm (function / 함수) in tìm kiếm (search / 검색).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Planning trong Artificial Intelligence**, **STRIPS-style biểu diễn (representation / 표현)** tiếp nhận điểm tựa từ **Actions: preconditions và effects** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **PDDL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## STRIPS-style biểu diễn (representation / 표현)

STRIPS-like hành động (action / 동작) lược đồ (schema / 스키마) thường có:

- precondition danh sách (list / 목록);
- add effects;
- delete effects.

If trạng thái (state / 상태) `S` and hành động (action / 동작) `a` applicable:

\[
S'=(S\setminus Del(a))\cup Add(a)
\]

This compact biểu diễn (representation / 표현) lets planner reason symbolically instead of enumerate all transitions ahead of thời gian (time / 시간).

> **Chuyển mạch:** Trong **Planning trong Artificial Intelligence**, **PDDL** tiếp nhận điểm tựa từ **STRIPS-style biểu diễn (representation / 표현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Goal biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## PDDL

Planning lĩnh vực (domain / 도메인) Definition ngôn ngữ (language / 언어) (PDDL) là standard-like ngôn ngữ (language / 언어) family để describe planning domains/problems.

Conceptual example:

```lisp
(:action move
 :parameters (?r ?from ?to)
 :precondition (and (at ?r ?from) (connected ?from ?to))
 :effect (and
   (not (at ?r ?from))
   (at ?r ?to)))
```

PDDL separates lĩnh vực (domain / 도메인) rules from specific bài toán (problem / 문제) instance.

Khi LLM các hệ thống (systems / 시스템들) generate structured plans, compiling natural ngôn ngữ (language / 언어) into PDDL/solver biểu diễn (representation / 표현) là một possible hybrid thiết kế (design / 설계).

> **Chuyển mạch:** Ở chặng này của **Planning trong Artificial Intelligence**, **Goal biểu diễn (representation / 표현)** tiếp nhận điểm tựa từ **PDDL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Forward state-space planning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Goal biểu diễn (representation / 표현)

Goal có thể là conjunction:

```text
At(box1, Storage)
AND
At(robot, ChargingStation)
```

Planner không cần reproduce chính xác (exact / 정확한) mục tiêu (target / 대상) trạng thái (state / 상태); unrelated propositions có thể vary.

Goal lớp trừu tượng (abstraction / 추상화) giảm unnecessary các ràng buộc (constraints / 제약조건들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Planning trong Artificial Intelligence**, **Forward state-space planning** tiếp nhận điểm tựa từ **Goal biểu diễn (representation / 표현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Backward / regression planning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Forward state-space planning

Start từ initial trạng thái (state / 상태), apply applicable actions forward tới goal.

```text
S0
 ├─ a1 → S1
 ├─ a2 → S2
 ...
```

Có thể dùng BFS/UCS/A* với planning-specific heuristics.

Weakness: many applicable actions irrelevant to goal generate huge branching.

> **Chuyển mạch:** Trong **Planning trong Artificial Intelligence**, **Backward / regression planning** tiếp nhận điểm tựa từ **Forward state-space planning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Partial-order planning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backward / regression planning

Start từ goal conditions và reason actions nào có thể achieve them.

If goal requires `At(box,Storage)`, consider hành động (action / 동작) whose tác động (effect / 효과) adds that proposition, then replace goal by its preconditions.

This focuses on goal-relevant actions but regression through interactions can be complex.

> **Chuyển mạch:** Ở chặng này của **Planning trong Artificial Intelligence**, **Partial-order planning** tiếp nhận điểm tựa từ **Backward / regression planning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhân quả (causal / 인과적) links** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Partial-order planning

A sequential plan imposes total thứ tự (order / 순서):

```text
A → B → C → D
```

Nhưng nhiều actions independent. Partial-order plan chỉ constrain necessary thứ tự (ordering / 순서):

```text
A before C
B before D
A and B may run in either order / parallel
```

Principle of **least commitment**: avoid deciding thứ tự (order / 순서) before necessary.

This helps expose parallelism and flexibility.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Planning trong Artificial Intelligence**, **Nhân quả (causal / 인과적) links** tiếp nhận điểm tựa từ **Partial-order planning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Planning đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhân quả (causal / 인과적) links

If hành động (action / 동작) `A` establishes điều kiện (condition / 조건) `p` needed by `B`, nhân quả (causal / 인과적) link:

\[
A \xrightarrow{p} B
\]

Another hành động (action / 동작) `C` that deletes `p` between A and B threatens link.

Planner must resolve threat by thứ tự (ordering / 순서) C before A or after B, or other các ràng buộc (constraints / 제약조건들).

This makes plan phụ thuộc (dependency / 의존성) tường minh (explicit / 명시적).

> **Chuyển mạch:** Trong **Planning trong Artificial Intelligence**, **Planning đồ thị (graph / 그래프)** tiếp nhận điểm tựa từ **Nhân quả (causal / 인과적) links** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Delete relaxation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Planning đồ thị (graph / 그래프)

GraphPlan-style planning đồ thị (graph / 그래프) alternates proposition levels and hành động (action / 동작) levels:

```text
P0 → A0 → P1 → A1 → P2 ...
```

It also tracks mutex (mutual exclusion) relationships.

Planning đồ thị (graph / 그래프) can provide reachability thông tin (information / 정보) and heuristics without enumerating every trạng thái (state / 상태) combination.

> **Chuyển mạch:** Ở chặng này của **Planning trong Artificial Intelligence**, **Delete relaxation** tiếp nhận điểm tựa từ **Planning đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Why delete effects matter** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Delete relaxation

Many planning heuristics ignore delete effects: once fact becomes true, pretend it remains true.

Relaxed bài toán (problem / 문제) is easier and optimistic.

This yields heuristics like:

- `h_max`;
- `h_add`;
- relaxed-plan heuristic `h_FF` in Fast Forward planner family.

Delete relaxation is same broader principle as heuristic tìm kiếm (search / 검색): solve an easier bài toán (problem / 문제) to estimate original.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Planning trong Artificial Intelligence**, **Why delete effects matter** tiếp nhận điểm tựa từ **Delete relaxation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tài nguyên (resource / 자원) planning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Why delete effects matter

Ignoring delete effects can be wildly optimistic when resources/actions interfere.

Example one truck cannot be simultaneously at two cities. Relaxed planner may act as if visiting both facts can coexist.

Heuristic useful despite unrealistic relaxation because it captures goal cấu trúc (structure / 구조) cheaply.

> **Chuyển mạch:** Trong **Planning trong Artificial Intelligence**, **Why delete effects matter** nêu điều cần giải thích; **Tài nguyên (resource / 자원) planning** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Temporal planning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tài nguyên (resource / 자원) planning

Classical propositional planning often ignores continuous resources/thời gian (time / 시간). Real planning may involve:

- fuel;
- battery;
- money;
- machine sức chứa (capacity / 용량);
- deadlines;
- durations.

Temporal/numeric planning extends hành động (action / 동작) các mô hình (models / 모델들).

Planning increasingly overlaps scheduling, ràng buộc (constraint / 제약조건) programming and operations research.

> **Chuyển mạch:** Ở chặng này của **Planning trong Artificial Intelligence**, **Tài nguyên (resource / 자원) planning** nêu điều cần giải thích; **Temporal planning** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Hierarchical tác vụ (task / 작업) mạng (network / 네트워크)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Temporal planning

Actions can have duration:

```text
Charge(robot): 30 minutes
Move(A,B): 10 minutes
Inspect: 5 minutes
```

Some actions overlap if no tài nguyên (resource / 자원)/xung đột (conflict / 충돌).

Goal becomes not just feasibility but makespan/minimum total thời gian (time / 시간).

Temporal planning needs reason about intervals and tính đồng thời (concurrency / 동시성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Planning trong Artificial Intelligence**, **Hierarchical tác vụ (task / 작업) mạng (network / 네트워크)** tiếp nhận điểm tựa từ **Temporal planning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Goal decomposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hierarchical tác vụ (task / 작업) mạng (network / 네트워크)

HTN planning represents high-level tasks decomposed into subtasks via methods.

Example:

```text
DeliverPackage
  ↓
PickUp
PlanRoute
Transport
DropOff
```

Lĩnh vực (domain / 도메인) kiến thức (knowledge / 지식) constrains allowed decompositions.

HTN can reduce tìm kiếm (search / 검색) không gian (space / 공간) greatly because it encodes procedural cấu trúc (structure / 구조), but less domain-general than unconstrained planning.

This closely resembles tác vụ (task / 작업) decomposition in software workflows and LLM agents.

> **Chuyển mạch:** Trong **Planning trong Artificial Intelligence**, **Goal decomposition** tiếp nhận điểm tựa từ **Hierarchical tác vụ (task / 작업) mạng (network / 네트워크)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Means–Ends phân tích (analysis / 분석)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Goal decomposition

If goal has subgoals `G1 ∧ G2`, solve independently only if actions do not interfere.

In real planning, subgoals interact.

Classic example: Blocks World goals may undo each other if achieved in wrong thứ tự (order / 순서).

Thus “break tác vụ (task / 작업) into subtasks” is not enough; planner must nhánh học (track / 트랙) dependencies and side effects.

> **Chuyển mạch:** Ở chặng này của **Planning trong Artificial Intelligence**, **Means–Ends phân tích (analysis / 분석)** tiếp nhận điểm tựa từ **Goal decomposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Plan validity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Means–Ends phân tích (analysis / 분석)

Means–Ends phân tích (analysis / 분석) compares trạng thái hiện tại (current state / 현재 상태) to goal, chooses difference, selects hành động (action / 동작) reducing difference, then creates subgoals for hành động (action / 동작) preconditions.

This was historically influential in General bài toán (problem / 문제) Solver.

Hiện đại (modern / 현대적) tác nhân (agent / 에이전트) prompts often rediscover similar mẫu (pattern / 패턴) in natural ngôn ngữ (language / 언어), but symbolic formulation makes các giả định (assumptions / 가정들) tường minh (explicit / 명시적).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Planning trong Artificial Intelligence**, **Plan validity** tiếp nhận điểm tựa từ **Means–Ends phân tích (analysis / 분석)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Planning vs scheduling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Plan validity

A proposed hành động (action / 동작) danh sách (list / 목록) is valid only if each hành động (action / 동작)’s preconditions hold at its thực thi (execution / 실행) điểm (point / 지점) and final trạng thái (state / 상태) satisfies goal.

Validator can independently check plan.

This separation is powerful:

```text
generator may be heuristic/learned
        ↓
formal validator checks exact constraints
```

Same kiến trúc (architecture / 아키텍처) useful for LLM agents: mô hình (model / 모델) proposes, deterministic tools verify.

> **Chuyển mạch:** Trong **Planning trong Artificial Intelligence**, **Planning vs scheduling** tiếp nhận điểm tựa từ **Plan validity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deterministic vs stochastic planning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Planning vs scheduling

Planning chooses **what actions and dependencies** achieve goal.

Scheduling chooses **when/resources** execute known tasks.

Real problems combine both.

Example manufacturing:

```text
Planning: which processing steps are needed?
Scheduling: which machine/time slot handles each step?
```

Conflating them hides different các ràng buộc (constraints / 제약조건들).

> **Chuyển mạch:** Ở chặng này của **Planning trong Artificial Intelligence**, **Deterministic vs stochastic planning** tiếp nhận điểm tựa từ **Planning vs scheduling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Offline planning vs online replanning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deterministic vs stochastic planning

Classical planning often assumes hành động (action / 동작) tác động (effect / 효과) deterministic.

Real hành động (action / 동작) can thất bại (fail / 실패):

\[
P(s'\mid s,a)
\]

Then plan as fixed chuỗi (sequence / 시퀀스) may be insufficient. Need **chính sách (policy / 정책)** ánh xạ (mapping / 매핑) states/beliefs to actions, leading toward MDP/POMDP.

This chuyển tiếp (transition / 전이) is covered in [Decision Making Under Uncertainty](./06_decision_making_under_uncertainty.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Planning trong Artificial Intelligence**, **Offline planning vs online replanning** tiếp nhận điểm tựa từ **Deterministic vs stochastic planning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Plan thực thi (execution / 실행) monitoring** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Offline planning vs online replanning

Offline planner computes full plan before thực thi (execution / 실행).

Online/receding-horizon tác nhân (agent / 에이전트):

```text
observe
  ↓
plan next horizon
  ↓
act
  ↓
observe actual result
  ↓
replan
```

Replanning handles động (dynamic / 동적) môi trường (environment / 환경) and mô hình (model / 모델) mismatch.

Robotics often uses mô hình (model / 모델) Predictive Control-like rolling horizon ideas in continuous điều khiển (control / 제어) ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Trong **Planning trong Artificial Intelligence**, **Plan thực thi (execution / 실행) monitoring** tiếp nhận điểm tựa từ **Offline planning vs online replanning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Contingency planning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Plan thực thi (execution / 실행) monitoring

Plan can thất bại (fail / 실패) because world changes or hành động (action / 동작) kết quả (outcome / 결과) differs.

Thực thi (execution / 실행) hệ thống (system / 시스템) must detect:

- precondition no longer true;
- công cụ (tool / 도구)/API lỗi (error / 오류);
- tài nguyên (resource / 자원) unavailable;
- observation contradicts mô hình (model / 모델);
- goal already achieved early.

Reliable tác nhân (agent / 에이전트) kiến trúc (architecture / 아키텍처) separates planner from thực thi (execution / 실행) monitor.

> **Chuyển mạch:** Ở chặng này của **Planning trong Artificial Intelligence**, **Contingency planning** tiếp nhận điểm tựa từ **Plan thực thi (execution / 실행) monitoring** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Planning and tìm kiếm (search / 검색)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Contingency planning

If specific uncertainties known, plan can branch:

```text
Try payment
 ├─ success → ship
 └─ failure → request another method
```

This is a conditional plan, not single chuỗi (sequence / 시퀀스).

As bất định (uncertainty / 불확실성) grows, tường minh (explicit / 명시적) contingency cây (tree / 트리) explodes; policies/MDPs provide more scalable formalism.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Planning trong Artificial Intelligence**, **Planning and tìm kiếm (search / 검색)** tiếp nhận điểm tựa từ **Contingency planning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Planning and CSP/SAT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Planning and tìm kiếm (search / 검색)

Planning can compile to tìm kiếm (search / 검색):

```text
state = set of facts
action = operator
successor = apply effects
goal test = goal propositions satisfied
```

But structured hành động (action / 동작) biểu diễn (representation / 표현) enables specialized heuristics and lập luận (reasoning / 추론) unavailable to generic đồ thị (graph / 그래프) tìm kiếm (search / 검색).

This illustrates mẫu (pattern / 패턴):

> Same bài toán (problem / 문제) may become tractable when thuật toán (algorithm / 알고리즘) understands biểu diễn (representation / 표현) cấu trúc (structure / 구조).

> **Chuyển mạch:** Trong **Planning trong Artificial Intelligence**, **Planning and CSP/SAT** tiếp nhận điểm tựa từ **Planning and tìm kiếm (search / 검색)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Planning and integer programming** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Planning and CSP/SAT

Bounded planning can be encoded as SAT.

For horizon `T`, create Boolean variables representing facts/actions at each timestep and các ràng buộc (constraints / 제약조건들) for transitions/goals.

Then ask SAT solver if plan exists of length `T`.

Increase `T` until satisfiable.

This is another example of reducing one AI bài toán (problem / 문제) to another mature solver lĩnh vực (domain / 도메인).

> **Chuyển mạch:** Ở chặng này của **Planning trong Artificial Intelligence**, **Planning and integer programming** tiếp nhận điểm tựa từ **Planning and CSP/SAT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Classical tác nhân (agent / 에이전트) vs LLM tác nhân (agent / 에이전트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Planning and integer programming

Scheduling/tài nguyên (resource / 자원) planning can be encoded as MILP:

- nhị phân (binary / 이진) variables for hành động (action / 동작) selection;
- continuous/integer times;
- tuyến tính (linear / 선형) sức chứa (capacity / 용량) các ràng buộc (constraints / 제약조건들);
- mục tiêu (objective / 목표) minimize chi phí (cost / 비용)/makespan.

Solver choice depends cấu trúc (structure / 구조); “AI planning thuật toán (algorithm / 알고리즘)” is not always best practical công cụ (tool / 도구).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Planning trong Artificial Intelligence**, **Classical tác nhân (agent / 에이전트) vs LLM tác nhân (agent / 에이전트)** tiếp nhận điểm tựa từ **Planning and integer programming** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Công cụ (tool / 도구) use as hành động (action / 동작) mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Classical tác nhân (agent / 에이전트) vs LLM tác nhân (agent / 에이전트)

Classical tác nhân (agent / 에이전트) planning has tường minh (explicit / 명시적):

```text
state
actions
preconditions
effects
goal
transition model
```

LLM agents often have fuzzy natural-language trạng thái (state / 상태) and công cụ (tool / 도구) descriptions.

This flexibility helps open-world tasks but weakens guarantees.

A robust kiến trúc (architecture / 아키텍처) can recover cấu trúc (structure / 구조):

```text
Natural-language goal
        ↓
structured task state
        ↓
planner / LLM proposes tool action
        ↓
validator checks preconditions/schema
        ↓
execute tool
        ↓
record actual observation
        ↓
replan
```

> **Chuyển mạch:** Trong **Planning trong Artificial Intelligence**, **Công cụ (tool / 도구) use as hành động (action / 동작) mô hình (model / 모델)** tiếp nhận điểm tựa từ **Classical tác nhân (agent / 에이전트) vs LLM tác nhân (agent / 에이전트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Long-horizon planning and lỗi (error / 오류) accumulation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Công cụ (tool / 도구) use as hành động (action / 동작) mô hình (model / 모델)

API/công cụ (tool / 도구) has:

- inputs → parameters;
- preconditions → authentication/trạng thái (state / 상태) requirements;
- effects → changed bên ngoài (external / 외부) trạng thái (state / 상태);
- observation → công cụ (tool / 도구) kết quả (result / 결과)/lỗi (error / 오류).

This maps naturally to planning vocabulary.

Example `send_email` should not be treated as văn bản (text / 텍스트) generation only; it has irreversible bên ngoài (external / 외부) tác động (effect / 효과), so kiểm tra hợp lệ (validation / 검증)/confirmation may be required.

> **Chuyển mạch:** Ở chặng này của **Planning trong Artificial Intelligence**, **Long-horizon planning and lỗi (error / 오류) accumulation** tiếp nhận điểm tựa từ **Công cụ (tool / 도구) use as hành động (action / 동작) mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Planning with learned world các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Long-horizon planning and lỗi (error / 오류) accumulation

If each planned hành động (action / 동작) has independent success xác suất (probability / 확률) `p`, crude chuỗi (sequence / 시퀀스) success:

\[
p^T
\]

falls quickly with horizon `T`.

Real các hệ thống (systems / 시스템들) not independent, but intuition motivates:

- short planning horizons;
- checkpoints;
- xác minh (verification / 확인);
- replanning;
- idempotent actions;
- quay lui (rollback / 롤백)/compensation.

Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) becomes part of tác nhân (agent / 에이전트) planning độ tin cậy (reliability / 신뢰성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Planning trong Artificial Intelligence**, **Planning with learned world các mô hình (models / 모델들)** tiếp nhận điểm tựa từ **Long-horizon planning and lỗi (error / 오류) accumulation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình (model / 모델) Predictive điều khiển (control / 제어) liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Planning with learned world các mô hình (models / 모델들)

If chuyển tiếp (transition / 전이) mô hình (model / 모델) unknown, neural mạng (network / 네트워크) can learn:

\[
\hat T(s,a)\rightarrow s'
\]

Planner searches imagined trajectories in learned mô hình (model / 모델).

Rủi ro (risk / 위험): mô hình (model / 모델) lỗi (error / 오류) compounds outside huấn luyện (training / 학습) phân phối (distribution / 분포). Planner may exploit mô hình (model / 모델) inaccuracies, finding trajectories that look good in simulation but thất bại (fail / 실패) reality.

This is known issue in model-based RL/world các mô hình (models / 모델들).

> **Chuyển mạch:** Trong **Planning trong Artificial Intelligence**, sau nội dung của **Planning with learned world các mô hình (models / 모델들)**, **Mô hình (model / 모델) Predictive điều khiển (control / 제어) liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Planning and lập luận (reasoning / 추론) tokens** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình (model / 모델) Predictive điều khiển (control / 제어) liên kết (connection / 연결)

MPC repeatedly optimize finite horizon, execute first hành động (action / 동작), then re-optimize with new observation.

```text
optimize H steps
execute 1 step
observe
shift horizon
repeat
```

This is control-theory analogue of online replanning and reduces long-horizon model-error accumulation.

> **Chuyển mạch:** Ở chặng này của **Planning trong Artificial Intelligence**, **Planning and lập luận (reasoning / 추론) tokens** tiếp nhận điểm tựa từ **Mô hình (model / 모델) Predictive điều khiển (control / 제어) liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Planning and lập luận (reasoning / 추론) tokens

LLM “plan first, answer later” prompts can improve organization, but natural-language plan is not necessarily executable formal plan.

A useful distinction:

```text
linguistic outline
vs
validated action plan
```

For công cụ (tool / 도구) agents, plan chất lượng (quality / 품질) should be evaluated by feasibility, phụ thuộc (dependency / 의존성) tính đúng đắn (correctness / 정확성) and actual thực thi (execution / 실행) success, not how convincing prose sounds.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Planning trong Artificial Intelligence**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Planning and lập luận (reasoning / 추론) tokens** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Search   = explore possible states
Planning = exploit action semantics to construct goal-achieving behavior

State        = facts true now
Action       = preconditions + effects
Plan         = ordered/partially ordered actions
Validator    = check plan semantics
Executor     = interact with real environment
Replanner    = update when reality differs from model
```

> **Chuyển mạch:** Trong **Planning trong Artificial Intelligence**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Planning chỉ là viết todo danh sách (list / 목록)”

AI planning reasons about preconditions, effects, conflicts, resources and reachability. A danh sách (list / 목록) without validity mô hình (model / 모델) is only an outline.

### “Nếu plan đúng thì thực thi (execution / 실행) sẽ thành công”

Only under accurate deterministic mô hình (model / 모델). Real environments require monitoring and replanning.

### “LLM có thể tự plan vì nó viết được các bước hợp lý”

Plausible steps may violate hidden các ràng buộc (constraints / 제약조건들) or công cụ (tool / 도구) trạng thái (state / 상태). Reliable các hệ thống (systems / 시스템들) need trạng thái (state / 상태) tracking and kiểm tra hợp lệ (validation / 검증).

### “More detailed plan is always better”

Overplanning fragile under bất định (uncertainty / 불확실성). Receding-horizon planning intentionally keeps future decisions flexible.

> **Chuyển mạch:** Ở chặng này của **Planning trong Artificial Intelligence**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Planning sits between tìm kiếm (search / 검색), CSP, lô-gic (logic / 논리) and quyết định (decision / 결정) lý thuyết (theory / 이론). It gives precise ngôn ngữ (language / 언어) for hiện đại (modern / 현대적) Agents: goal, trạng thái (state / 상태), hành động (action / 동작), precondition, tác động (effect / 효과), monitor and replan. Later `10_agents_and_ai_systems/` will reuse these concepts instead of redefining tác nhân (agent / 에이전트) planning from scratch.

Xem tiếp: [Decision Making Under Uncertainty](./06_decision_making_under_uncertainty.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
