# Constraint Satisfaction Problems trong AI

Một số bài toán không cần tìm một path cụ thể; ta chỉ cần tìm **một assignment thỏa tất cả constraints**. Scheduling, Sudoku, map coloring, resource allocation, configuration và nhiều planning subproblems có cấu trúc này.

**Constraint Satisfaction Problem (CSP / 제약 만족 문제)** tách problem thành variables, domains và constraints. Cách biểu diễn này cho phép dùng inference để loại bỏ rất nhiều possibilities trước khi search, minh họa một principle quan trọng của AI:

> Một representation tốt có thể làm bài toán dễ hơn nhiều so với brute-force search trên raw configurations.

Xem trước: [Problem Representation](../00_foundations/03_problem_representation.md) và [State Space and Search](./00_state_space_and_search.md).

## CSP gồm những gì?

Một CSP được mô tả bởi:

\[
(X,D,C)
\]

Trong đó:

- `X={X1,...,Xn}` là variables;
- `D_i` là domain của variable `X_i`;
- `C` là set constraints.

Goal là assignment:

\[
X_i=v_i
\]

sao cho mọi constraint đều satisfied.

## Ví dụ map coloring

Giả sử cần tô màu regions sao cho adjacent regions khác màu.

```text
Variables: WA, NT, SA, Q, NSW, V, T
Domain: {Red, Green, Blue}
Constraint: WA != NT, WA != SA, ...
```

Không cần care order tô màu cuối cùng. Chỉ final assignment matter.

Đây là khác biệt với route search, nơi path itself has meaning/cost.

## Unary, binary và global constraints

**Unary constraint** áp dụng một variable:

\[
X\neq Red
\]

**Binary constraint** giữa hai variables:

\[
X\neq Y
\]

**Global constraint** involve many variables, ví dụ `AllDifferent(X1,...,Xn)` trong Sudoku/scheduling.

Global constraint không chỉ syntax convenience. Specialized propagation algorithm có thể exploit structure mạnh hơn decomposing thành pairwise constraints.

## Constraint graph

Binary CSP có thể represented bằng graph:

```text
node = variable
edge = constraint giữa variables
```

Graph structure giúp reason về independence, decomposition và treewidth-like complexity.

Nếu graph split thành disconnected components, solve independently.

## Naive enumeration

Nếu `n` variables, mỗi domain size `d`, brute force có:

\[
d^n
\]

assignments.

Sudoku 81 cells với domain 9 gợi ý `9^81`, enormous.

Nhưng constraints immediately eliminate most combinations. CSP algorithms exploit this before/during branching.

## Backtracking Search

Backtracking assign variables one by one. Khi partial assignment violates constraint, undo and try alternative.

```pseudo
backtrack(assignment):
    if complete: return assignment

    X ← choose_unassigned_variable()
    for v in order_values(X):
        if consistent(X=v, assignment):
            assign X=v
            result ← backtrack(assignment)
            if success: return result
            unassign X

    return failure
```

Backtracking là DFS trong assignment space, nhưng CSP-specific reasoning làm nó mạnh hơn naive DFS.

## Variable ordering: MRV

**Minimum Remaining Values (MRV)** chọn variable có ít legal values nhất.

Intuition:

> Fail fast.

Nếu một variable gần như impossible, giải nó trước để discover contradiction early thay vì waste search ở branches khác.

MRV còn gọi “most constrained variable”.

## Degree heuristic

Nếu tie MRV, chọn variable participating in most constraints với unassigned variables.

Idea: chọn variable có influence lớn để propagate restriction sớm.

MRV nhìn domain size hiện tại; degree nhìn connectivity.

## Value ordering: Least Constraining Value

Sau khi chọn variable, **Least Constraining Value (LCV)** thử value loại ít options của neighbors nhất.

Variable heuristic thường “fail first”, value heuristic thường “leave flexibility”.

Hai ideas không contradiction: ta chọn hard variable nhưng chọn value ít phá future choices.

## Forward checking

Khi assign `X=v`, forward checking remove incompatible values khỏi domains neighbors.

Nếu neighbor domain empty, fail immediately.

Example:

```text
X domain {R,G}
Y domain {R,G}
constraint X != Y

assign X=R
→ remove R from Y
→ Y={G}
```

Forward checking detects local consequence one step ahead.

## Constraint propagation

Stronger than forward checking, propagation repeatedly enforce local consistency until no more reduction.

Example chain:

```text
X=R
→ Y cannot R
→ Y=G
→ Z cannot G
→ Z=B
```

One assignment can cascade across network.

## Arc consistency

For binary constraint between `X` and `Y`, arc `X→Y` is consistent if every value in `D_X` has at least one supporting value in `D_Y` satisfying constraint.

If value `x` has no support in `Y`, remove it.

**AC-3** algorithm repeatedly revises arcs until stable or domain empty.

Simplified:

```pseudo
queue ← all arcs
while queue:
    (Xi,Xj) ← pop
    if revise(Xi,Xj):
        if domain(Xi) empty: failure
        for Xk neighbor of Xi except Xj:
            add (Xk,Xi)
```

## Local consistency không guarantee global solution

Arc-consistent CSP can still have no solution. Local checks only ensure pairwise support, not global compatibility.

This distinction important:

```text
constraint propagation reduces search
but usually does not eliminate need for search
```

## Maintaining Arc Consistency

MAC runs arc consistency after each assignment during backtracking.

More propagation cost per node but fewer search nodes.

Trade-off:

```text
more inference per node
vs
less branching
```

Optimal balance depends problem structure.

## Sudoku as CSP

Variables = 81 cells.

Domain = digits 1..9 for empty cells.

Constraints:

- each row AllDifferent;
- each column AllDifferent;
- each 3×3 block AllDifferent.

Human techniques like “only possible value” are forms of constraint propagation.

Guess-and-backtrack happens only when propagation insufficient.

## Scheduling

Variables can be tasks.

Domain = possible times/resources.

Constraints:

```text
Task A before B
A and C cannot use same machine simultaneously
employee E available only certain hours
max weekly capacity
```

Real scheduling often becomes richer **Constraint Programming (CP)** or mixed-integer optimization rather than simple finite-domain CSP.

## Hard vs soft constraints

Classical CSP treats constraint as must satisfy.

Real problem often has soft preferences:

```text
hard: two meetings cannot occupy same room/time
soft: prefer morning
soft: minimize employee overtime
```

Weighted CSP / Max-CSP / optimization formulations assign penalty/cost to violations.

This connects CSP with Operations Research.

## SAT as constraint problem

Boolean Satisfiability (SAT) asks whether Boolean formula has assignment making it true.

Variables are Boolean, constraints are clauses.

Example CNF:

\[
(A\lor \neg B)\land(B\lor C)
\]

SAT is NP-complete but modern SAT solvers are extremely effective on many structured instances using:

- unit propagation;
- conflict-driven clause learning (CDCL);
- variable heuristics;
- restarts.

“NP-complete” does not mean every real instance is impossible.

## Unit propagation

If clause:

\[
(A\lor B)
\]

and `A=false`, then `B` must true.

This is constraint propagation over Boolean formula.

CSP and SAT share deep idea: inference shrinks domains before search branches.

## Conflict-Driven Clause Learning

When SAT solver reaches contradiction, it analyzes conflict to derive new clause preventing same class of bad assignments.

This is search that **learns from failure**.

Conceptually:

```text
branch
 ↓
contradiction
 ↓
analyze reason
 ↓
learn constraint
 ↓
avoid repeated mistake
```

This pattern resembles modern reasoning systems with memory/verification, though CDCL has formal Boolean semantics and stronger guarantees.

## Local search for CSP

Instead of building partial consistent assignment, start with complete possibly-invalid assignment and iteratively reduce conflicts.

**Min-conflicts** chooses conflicted variable and assigns value minimizing violations.

It works surprisingly well for large N-Queens.

Local search uses little memory but may get stuck and is not complete without additional strategy.

## N-Queens

Place `N` queens on `N×N` board so no two attack each other.

Variables: one queen per column.

Domain: row number.

Constraints:

\[
Q_i\neq Q_j
\]

and:

\[
|Q_i-Q_j|\neq|i-j|
\]

CSP representation already eliminates same-column conflict by construction. Good representation reduces constraints before algorithm starts.

## Symmetry breaking

Many CSPs have symmetric equivalent solutions. Search wastes time rediscovering permutations.

Example coloring: swapping names Red/Green across entire valid solution produces equivalent solution.

Add symmetry-breaking constraints to choose canonical representative.

Again, representation/constraints can shrink search space dramatically.

## Decomposition

If constraint graph has independent components, solve each separately.

More generally, tree-structured CSPs can be solved efficiently compared with arbitrary cyclic graphs.

Graph **treewidth** measures roughly how far graph from tree-like; many algorithms exponential in treewidth rather than raw number variables.

This connects CSP to Graphical Models and probabilistic inference.

## CSP vs Optimization

CSP asks:

> Is there any assignment satisfying constraints?

Optimization asks:

> Which feasible assignment has best objective?

Real systems often combine:

\[
\min_x f(x)\quad\text{s.t. constraints}
\]

Scheduling, routing and resource allocation frequently use Mixed Integer Programming, CP-SAT or specialized solvers.

AI, Operations Research and Optimization overlap strongly here.

## Constraint Programming

Constraint Programming lets developer declare variables/constraints while solver handles propagation + search.

Example conceptual API:

```python
start_A < start_B
no_overlap(tasks_on_machine_1)
all_different(room_assignments)
```

This separates **what must be true** from exact search procedure.

Declarative modeling is similar spirit to logic programming.

## Learned heuristics for CSP/SAT

Variable/value ordering dramatically affects runtime. ML can learn branching heuristics from solved instances.

But solver correctness can remain symbolic: learned component only chooses where search first; constraint checker/proof machinery preserves validity.

This hybrid design is attractive because learning improves speed without trusting neural model for final correctness.

## LLM + constraints

LLM can propose candidate schedule/configuration, but text generation does not guarantee hard constraints.

Reliable architecture:

```text
LLM interprets natural-language requirements
        ↓
structured CSP/solver model
        ↓
constraint solver finds/verifies assignment
        ↓
LLM explains result
```

This is stronger than asking LLM to “remember all constraints” in free-form generation.

## Structured output validation

JSON schema/type constraints are simpler cousin of CSP. Decoder or post-validator ensures output belongs to valid structural domain.

Grammar-constrained decoding reduces invalid syntax, but semantic constraints like “end date after start date” need richer validation/solver logic.

## Mental Model

```text
Variable   = thing we must choose
Domain     = options available
Constraint = combinations forbidden/required
Propagation = remove impossible values without guessing
Search      = branch when inference alone insufficient
Heuristic   = choose branching variable/value intelligently
Learning    = optionally improve heuristic, not necessarily correctness rule
```

## Common Misconceptions

### “CSP là brute force assignment”

Good CSP solvers use propagation, heuristics, learning and decomposition to avoid most combinations.

### “Arc consistency means solved”

Local consistency can hold while no global solution exists.

### “LLM can replace constraint solver nếu model đủ lớn”

LLM may propose solutions, but hard guarantees require explicit validation/search/formal mechanism when correctness matters.

### “NP-complete nghĩa practical solver vô dụng”

Worst-case complexity does not predict all structured instances. SAT/CP solvers solve many large real problems effectively.

## Knowledge Connection

CSP sits at intersection of Search, Logic, Graphs and Optimization. It teaches a recurring AI lesson: **reason before branching**. Constraint propagation converts knowledge into domain reduction, just as heuristics convert knowledge into search priority.

Xem tiếp: [Planning](./05_planning.md), nơi actions có preconditions/effects và goal thường cần một sequence thay vì chỉ final assignment.