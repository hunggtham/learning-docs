# Planning trong Artificial Intelligence

Search hỏi “từ state này, action nào dẫn tới goal?”. **Planning (계획 / lập kế hoạch)** làm câu hỏi đó explicit hơn bằng cách biểu diễn **actions có preconditions và effects**, goal có structure, và một plan là sequence hoặc partial order actions làm goal trở thành true.

Planning quan trọng vì intelligence không chỉ phản ứng với observation hiện tại. Nhiều task cần reason về future consequences, prerequisites, resource conflicts và dependency giữa subgoals. Classical planning cung cấp vocabulary chính xác cho những vấn đề mà modern “AI agent planning” thường mô tả rất loosely.

Xem trước: [State Space and Search](./00_state_space_and_search.md) và [Constraint Satisfaction](./04_constraint_satisfaction.md).

## Reactive behavior và planning khác nhau thế nào?

Reactive policy:

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

Reactive behavior nhanh và robust khi environment familiar. Planning hữu ích khi task novel, long-horizon hoặc actions có delayed consequences.

Real agents thường combine both: plan high-level, react/replan low-level.

## State representation trong classical planning

Một state có thể represented bằng set propositions.

Example warehouse:

```text
At(robot, A)
BoxAt(box1, B)
HandEmpty(robot)
DoorOpen(B,C)
```

Closed-world assumption trong many symbolic planners: proposition không listed được coi false. Assumption này convenient nhưng không phù hợp mọi real-world knowledge setting.

## Actions: preconditions và effects

Action `Move(A,B)`:

```text
Preconditions:
  At(robot, A)
  Connected(A, B)

Effects:
  add At(robot, B)
  delete At(robot, A)
```

Action applicable chỉ khi preconditions true.

Transition model được build từ effects.

This is more structured than generic successor function in search.

## STRIPS-style representation

STRIPS-like action schema thường có:

- precondition list;
- add effects;
- delete effects.

If state `S` and action `a` applicable:

\[
S'=(S\setminus Del(a))\cup Add(a)
\]

This compact representation lets planner reason symbolically instead of enumerate all transitions ahead of time.

## PDDL

Planning Domain Definition Language (PDDL) là standard-like language family để describe planning domains/problems.

Conceptual example:

```lisp
(:action move
 :parameters (?r ?from ?to)
 :precondition (and (at ?r ?from) (connected ?from ?to))
 :effect (and
   (not (at ?r ?from))
   (at ?r ?to)))
```

PDDL separates domain rules from specific problem instance.

Khi LLM systems generate structured plans, compiling natural language into PDDL/solver representation là một possible hybrid design.

## Goal representation

Goal có thể là conjunction:

```text
At(box1, Storage)
AND
At(robot, ChargingStation)
```

Planner không cần reproduce exact target state; unrelated propositions có thể vary.

Goal abstraction giảm unnecessary constraints.

## Forward state-space planning

Start từ initial state, apply applicable actions forward tới goal.

```text
S0
 ├─ a1 → S1
 ├─ a2 → S2
 ...
```

Có thể dùng BFS/UCS/A* với planning-specific heuristics.

Weakness: many applicable actions irrelevant to goal generate huge branching.

## Backward / regression planning

Start từ goal conditions và reason actions nào có thể achieve them.

If goal requires `At(box,Storage)`, consider action whose effect adds that proposition, then replace goal by its preconditions.

This focuses on goal-relevant actions but regression through interactions can be complex.

## Partial-order planning

A sequential plan imposes total order:

```text
A → B → C → D
```

Nhưng nhiều actions independent. Partial-order plan chỉ constrain necessary ordering:

```text
A before C
B before D
A and B may run in either order / parallel
```

Principle of **least commitment**: avoid deciding order before necessary.

This helps expose parallelism and flexibility.

## Causal links

If action `A` establishes condition `p` needed by `B`, causal link:

\[
A \xrightarrow{p} B
\]

Another action `C` that deletes `p` between A and B threatens link.

Planner must resolve threat by ordering C before A or after B, or other constraints.

This makes plan dependency explicit.

## Planning graph

GraphPlan-style planning graph alternates proposition levels and action levels:

```text
P0 → A0 → P1 → A1 → P2 ...
```

It also tracks mutex (mutual exclusion) relationships.

Planning graph can provide reachability information and heuristics without enumerating every state combination.

## Delete relaxation

Many planning heuristics ignore delete effects: once fact becomes true, pretend it remains true.

Relaxed problem is easier and optimistic.

This yields heuristics like:

- `h_max`;
- `h_add`;
- relaxed-plan heuristic `h_FF` in Fast Forward planner family.

Delete relaxation is same broader principle as heuristic search: solve an easier problem to estimate original.

## Why delete effects matter

Ignoring delete effects can be wildly optimistic when resources/actions interfere.

Example one truck cannot be simultaneously at two cities. Relaxed planner may act as if visiting both facts can coexist.

Heuristic useful despite unrealistic relaxation because it captures goal structure cheaply.

## Resource planning

Classical propositional planning often ignores continuous resources/time. Real planning may involve:

- fuel;
- battery;
- money;
- machine capacity;
- deadlines;
- durations.

Temporal/numeric planning extends action models.

Planning increasingly overlaps scheduling, constraint programming and operations research.

## Temporal planning

Actions can have duration:

```text
Charge(robot): 30 minutes
Move(A,B): 10 minutes
Inspect: 5 minutes
```

Some actions overlap if no resource/conflict.

Goal becomes not just feasibility but makespan/minimum total time.

Temporal planning needs reason about intervals and concurrency.

## Hierarchical Task Network

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

Domain knowledge constrains allowed decompositions.

HTN can reduce search space greatly because it encodes procedural structure, but less domain-general than unconstrained planning.

This closely resembles task decomposition in software workflows and LLM agents.

## Goal decomposition

If goal has subgoals `G1 ∧ G2`, solve independently only if actions do not interfere.

In real planning, subgoals interact.

Classic example: Blocks World goals may undo each other if achieved in wrong order.

Thus “break task into subtasks” is not enough; planner must track dependencies and side effects.

## Means–Ends Analysis

Means–Ends Analysis compares current state to goal, chooses difference, selects action reducing difference, then creates subgoals for action preconditions.

This was historically influential in General Problem Solver.

Modern agent prompts often rediscover similar pattern in natural language, but symbolic formulation makes assumptions explicit.

## Plan validity

A proposed action list is valid only if each action’s preconditions hold at its execution point and final state satisfies goal.

Validator can independently check plan.

This separation is powerful:

```text
generator may be heuristic/learned
        ↓
formal validator checks exact constraints
```

Same architecture useful for LLM agents: model proposes, deterministic tools verify.

## Planning vs scheduling

Planning chooses **what actions and dependencies** achieve goal.

Scheduling chooses **when/resources** execute known tasks.

Real problems combine both.

Example manufacturing:

```text
Planning: which processing steps are needed?
Scheduling: which machine/time slot handles each step?
```

Conflating them hides different constraints.

## Deterministic vs stochastic planning

Classical planning often assumes action effect deterministic.

Real action can fail:

\[
P(s'\mid s,a)
\]

Then plan as fixed sequence may be insufficient. Need **policy** mapping states/beliefs to actions, leading toward MDP/POMDP.

This transition is covered in [Decision Making Under Uncertainty](./06_decision_making_under_uncertainty.md).

## Offline planning vs online replanning

Offline planner computes full plan before execution.

Online/receding-horizon agent:

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

Replanning handles dynamic environment and model mismatch.

Robotics often uses Model Predictive Control-like rolling horizon ideas in continuous control context.

## Plan execution monitoring

Plan can fail because world changes or action outcome differs.

Execution system must detect:

- precondition no longer true;
- tool/API error;
- resource unavailable;
- observation contradicts model;
- goal already achieved early.

Reliable agent architecture separates planner from execution monitor.

## Contingency planning

If specific uncertainties known, plan can branch:

```text
Try payment
 ├─ success → ship
 └─ failure → request another method
```

This is a conditional plan, not single sequence.

As uncertainty grows, explicit contingency tree explodes; policies/MDPs provide more scalable formalism.

## Planning and search

Planning can compile to search:

```text
state = set of facts
action = operator
successor = apply effects
goal test = goal propositions satisfied
```

But structured action representation enables specialized heuristics and reasoning unavailable to generic graph search.

This illustrates pattern:

> Same problem may become tractable when algorithm understands representation structure.

## Planning and CSP/SAT

Bounded planning can be encoded as SAT.

For horizon `T`, create Boolean variables representing facts/actions at each timestep and constraints for transitions/goals.

Then ask SAT solver if plan exists of length `T`.

Increase `T` until satisfiable.

This is another example of reducing one AI problem to another mature solver domain.

## Planning and integer programming

Scheduling/resource planning can be encoded as MILP:

- binary variables for action selection;
- continuous/integer times;
- linear capacity constraints;
- objective minimize cost/makespan.

Solver choice depends structure; “AI planning algorithm” is not always best practical tool.

## Classical agent vs LLM agent

Classical agent planning has explicit:

```text
state
actions
preconditions
effects
goal
transition model
```

LLM agents often have fuzzy natural-language state and tool descriptions.

This flexibility helps open-world tasks but weakens guarantees.

A robust architecture can recover structure:

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

## Tool use as action model

API/tool has:

- inputs → parameters;
- preconditions → authentication/state requirements;
- effects → changed external state;
- observation → tool result/error.

This maps naturally to planning vocabulary.

Example `send_email` should not be treated as text generation only; it has irreversible external effect, so validation/confirmation may be required.

## Long-horizon planning and error accumulation

If each planned action has independent success probability `p`, crude sequence success:

\[
p^T
\]

falls quickly with horizon `T`.

Real systems not independent, but intuition motivates:

- short planning horizons;
- checkpoints;
- verification;
- replanning;
- idempotent actions;
- rollback/compensation.

Software Engineering becomes part of agent planning reliability.

## Planning with learned world models

If transition model unknown, neural network can learn:

\[
\hat T(s,a)\rightarrow s'
\]

Planner searches imagined trajectories in learned model.

Risk: model error compounds outside training distribution. Planner may exploit model inaccuracies, finding trajectories that look good in simulation but fail reality.

This is known issue in model-based RL/world models.

## Model Predictive Control connection

MPC repeatedly optimize finite horizon, execute first action, then re-optimize with new observation.

```text
optimize H steps
execute 1 step
observe
shift horizon
repeat
```

This is control-theory analogue of online replanning and reduces long-horizon model-error accumulation.

## Planning and reasoning tokens

LLM “plan first, answer later” prompts can improve organization, but natural-language plan is not necessarily executable formal plan.

A useful distinction:

```text
linguistic outline
vs
validated action plan
```

For tool agents, plan quality should be evaluated by feasibility, dependency correctness and actual execution success, not how convincing prose sounds.

## Mental Model

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

## Common Misconceptions

### “Planning chỉ là viết todo list”

AI planning reasons about preconditions, effects, conflicts, resources and reachability. A list without validity model is only an outline.

### “Nếu plan đúng thì execution sẽ thành công”

Only under accurate deterministic model. Real environments require monitoring and replanning.

### “LLM có thể tự plan vì nó viết được các bước hợp lý”

Plausible steps may violate hidden constraints or tool state. Reliable systems need state tracking and validation.

### “More detailed plan is always better”

Overplanning fragile under uncertainty. Receding-horizon planning intentionally keeps future decisions flexible.

## Knowledge Connection

Planning sits between Search, CSP, Logic and Decision Theory. It gives precise language for modern Agents: goal, state, action, precondition, effect, monitor and replan. Later `10_agents_and_ai_systems/` will reuse these concepts instead of redefining agent planning from scratch.

Xem tiếp: [Decision Making Under Uncertainty](./06_decision_making_under_uncertainty.md).