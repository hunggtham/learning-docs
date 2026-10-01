# Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **CSP gồm những gì?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Ví dụ map coloring** để đem mô hình vào tình huống cụ thể. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Một số bài toán không cần tìm một đường dẫn (path / 경로) cụ thể; ta chỉ cần tìm **một assignment thỏa tất cả các ràng buộc (constraints / 제약조건들)**. Scheduling, Sudoku, map coloring, tài nguyên (resource / 자원) allocation, cấu hình (configuration / 구성) và nhiều planning subproblems có cấu trúc này.

**ràng buộc (constraint / 제약조건) Satisfaction bài toán (problem / 문제)** tách bài toán (problem / 문제) thành variables, domains và các ràng buộc (constraints / 제약조건들). Cách biểu diễn này cho phép dùng suy luận (inference / 추론) để loại bỏ rất nhiều possibilities trước khi tìm kiếm (search / 검색), minh họa một principle quan trọng của AI:

> Một biểu diễn (representation / 표현) tốt có thể làm bài toán dễ hơn nhiều so với brute-force tìm kiếm (search / 검색) trên raw configurations.

Xem trước: [Problem Representation](../00_foundations/03_problem_representation.md) và [State Space and Search](./00_state_space_and_search.md).

## CSP gồm những gì?

Một CSP được mô tả bởi:

\[
(X,D,C)
\]

Trong đó:

- `X={X1,...,Xn}` là variables;
- `D_i` là lĩnh vực (domain / 도메인) của variable `X_i`;
- `C` là set các ràng buộc (constraints / 제약조건들).

Goal là assignment:

\[
X_i=v_i
\]

sao cho mọi ràng buộc (constraint / 제약조건) đều satisfied.

> **Chuyển mạch:** Trong **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **CSP gồm những gì?** cho ta quy tắc; **Ví dụ map coloring** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Unary, nhị phân (binary / 이진) và toàn cục (global / 전역) các ràng buộc (constraints / 제약조건들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ map coloring

Giả sử cần tô màu regions sao cho adjacent regions khác màu.

```text
Variables: WA, NT, SA, Q, NSW, V, T
Domain: {Red, Green, Blue}
Constraint: WA != NT, WA != SA, ...
```

Không cần care thứ tự (order / 순서) tô màu cuối cùng. Chỉ final assignment matter.

Đây là khác biệt với tuyến (route / 경로) tìm kiếm (search / 검색), nơi đường dẫn (path / 경로) itself has meaning/chi phí (cost / 비용).

> **Chuyển mạch:** Ở chặng này của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Ví dụ map coloring** cho ta quy tắc; **Unary, nhị phân (binary / 이진) và toàn cục (global / 전역) các ràng buộc (constraints / 제약조건들)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Ràng buộc (constraint / 제약조건) đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Unary, nhị phân (binary / 이진) và toàn cục (global / 전역) các ràng buộc (constraints / 제약조건들)

**Unary ràng buộc (constraint / 제약조건)** áp dụng một variable:

\[
X\neq Red
\]

**nhị phân (binary / 이진) ràng buộc (constraint / 제약조건)** giữa hai variables:

\[
X\neq Y
\]

**toàn cục (global / 전역) ràng buộc (constraint / 제약조건)** involve many variables, ví dụ `AllDifferent(X1,...,Xn)` trong Sudoku/scheduling.

Toàn cục (global / 전역) ràng buộc (constraint / 제약조건) không chỉ cú pháp (syntax / 문법) convenience. Specialized propagation thuật toán (algorithm / 알고리즘) có thể exploit cấu trúc (structure / 구조) mạnh hơn decomposing thành pairwise các ràng buộc (constraints / 제약조건들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Ràng buộc (constraint / 제약조건) đồ thị (graph / 그래프)** tiếp nhận điểm tựa từ **Unary, nhị phân (binary / 이진) và toàn cục (global / 전역) các ràng buộc (constraints / 제약조건들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Naive enumeration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ràng buộc (constraint / 제약조건) đồ thị (graph / 그래프)

Nhị phân (binary / 이진) CSP có thể represented bằng đồ thị (graph / 그래프):

```text
node = variable
edge = constraint giữa variables
```

Đồ thị (graph / 그래프) cấu trúc (structure / 구조) giúp reason về independence, decomposition và treewidth-like độ phức tạp (complexity / 복잡도).

Nếu đồ thị (graph / 그래프) split thành disconnected components, solve independently.

> **Chuyển mạch:** Trong **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Naive enumeration** tiếp nhận điểm tựa từ **Ràng buộc (constraint / 제약조건) đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Backtracking tìm kiếm (search / 검색)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Naive enumeration

Nếu `n` variables, mỗi lĩnh vực (domain / 도메인) kích thước (size / 크기) `d`, brute force có:

\[
d^n
\]

assignments.

Sudoku 81 cells với lĩnh vực (domain / 도메인) 9 gợi ý `9^81`, enormous.

Nhưng các ràng buộc (constraints / 제약조건들) immediately eliminate most combinations. CSP algorithms exploit this before/during branching.

> **Chuyển mạch:** Ở chặng này của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Backtracking tìm kiếm (search / 검색)** tiếp nhận điểm tựa từ **Naive enumeration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Variable thứ tự (ordering / 순서): MRV** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backtracking tìm kiếm (search / 검색)

Backtracking assign variables one by one. Khi partial assignment violates ràng buộc (constraint / 제약조건), undo and try alternative.

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

Backtracking là DFS trong assignment không gian (space / 공간), nhưng CSP-specific lập luận (reasoning / 추론) làm nó mạnh hơn naive DFS.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Variable thứ tự (ordering / 순서): MRV** tiếp nhận điểm tựa từ **Backtracking tìm kiếm (search / 검색)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Degree heuristic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Variable thứ tự (ordering / 순서): MRV

**Minimum Remaining Values (MRV)** chọn variable có ít legal values nhất.

Intuition:

> thất bại (fail / 실패) fast.

Nếu một variable gần như impossible, giải nó trước để discover contradiction early thay vì waste tìm kiếm (search / 검색) ở branches khác.

MRV còn gọi “most constrained variable”.

> **Chuyển mạch:** Trong **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Degree heuristic** tiếp nhận điểm tựa từ **Variable thứ tự (ordering / 순서): MRV** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Giá trị (value / 값) thứ tự (ordering / 순서): Least Constraining giá trị (value / 값)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Degree heuristic

Nếu tie MRV, chọn variable participating in most các ràng buộc (constraints / 제약조건들) với unassigned variables.

Idea: chọn variable có influence lớn để propagate restriction sớm.

MRV nhìn lĩnh vực (domain / 도메인) kích thước (size / 크기) hiện tại; degree nhìn connectivity.

> **Chuyển mạch:** Ở chặng này của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Giá trị (value / 값) thứ tự (ordering / 순서): Least Constraining giá trị (value / 값)** tiếp nhận điểm tựa từ **Degree heuristic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Forward checking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Giá trị (value / 값) thứ tự (ordering / 순서): Least Constraining giá trị (value / 값)

Sau khi chọn variable, **Least Constraining giá trị (value / 값) (LCV)** thử giá trị (value / 값) loại ít options của neighbors nhất.

Variable heuristic thường “thất bại (fail / 실패) first”, giá trị (value / 값) heuristic thường “leave flexibility”.

Hai ideas không contradiction: ta chọn hard variable nhưng chọn giá trị (value / 값) ít phá future choices.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Forward checking** tiếp nhận điểm tựa từ **Giá trị (value / 값) thứ tự (ordering / 순서): Least Constraining giá trị (value / 값)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ràng buộc (constraint / 제약조건) propagation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Forward checking

Khi assign `X=v`, forward checking remove incompatible values khỏi domains neighbors.

Nếu neighbor lĩnh vực (domain / 도메인) empty, thất bại (fail / 실패) immediately.

Example:

```text
X domain {R,G}
Y domain {R,G}
constraint X != Y

assign X=R
→ remove R from Y
→ Y={G}
```

Forward checking detects cục bộ (local / 로컬) consequence one step ahead.

> **Chuyển mạch:** Trong **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Ràng buộc (constraint / 제약조건) propagation** tiếp nhận điểm tựa từ **Forward checking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Arc consistency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ràng buộc (constraint / 제약조건) propagation

Stronger than forward checking, propagation repeatedly enforce cục bộ (local / 로컬) consistency until no more reduction.

Example chuỗi (chain / 사슬):

```text
X=R
→ Y cannot R
→ Y=G
→ Z cannot G
→ Z=B
```

One assignment can cascade across mạng (network / 네트워크).

> **Chuyển mạch:** Ở chặng này của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Arc consistency** tiếp nhận điểm tựa từ **Ràng buộc (constraint / 제약조건) propagation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cục bộ (local / 로컬) consistency không guarantee toàn cục (global / 전역) solution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Arc consistency

For nhị phân (binary / 이진) ràng buộc (constraint / 제약조건) between `X` and `Y`, arc `X→Y` is consistent if every giá trị (value / 값) in `D_X` has at least one supporting giá trị (value / 값) in `D_Y` satisfying ràng buộc (constraint / 제약조건).

If giá trị (value / 값) `x` has no hỗ trợ (support / 지원) in `Y`, remove it.

**AC-3** thuật toán (algorithm / 알고리즘) repeatedly revises arcs until stable or lĩnh vực (domain / 도메인) empty.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Cục bộ (local / 로컬) consistency không guarantee toàn cục (global / 전역) solution** tiếp nhận điểm tựa từ **Arc consistency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Maintaining Arc Consistency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cục bộ (local / 로컬) consistency không guarantee toàn cục (global / 전역) solution

Arc-consistent CSP can still have no solution. cục bộ (local / 로컬) checks only ensure pairwise hỗ trợ (support / 지원), not toàn cục (global / 전역) tính tương thích (compatibility / 호환성).

This distinction important:

```text
constraint propagation reduces search
but usually does not eliminate need for search
```

> **Chuyển mạch:** Trong **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Maintaining Arc Consistency** tiếp nhận điểm tựa từ **Cục bộ (local / 로컬) consistency không guarantee toàn cục (global / 전역) solution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sudoku as CSP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Maintaining Arc Consistency

MAC runs arc consistency after each assignment during backtracking.

More propagation chi phí (cost / 비용) per nút (node / 노드) but fewer tìm kiếm (search / 검색) nodes.

Sự đánh đổi (trade-off / 트레이드오프):

```text
more inference per node
vs
less branching
```

Optimal balance depends bài toán (problem / 문제) cấu trúc (structure / 구조).

> **Chuyển mạch:** Ở chặng này của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Sudoku as CSP** tiếp nhận điểm tựa từ **Maintaining Arc Consistency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Scheduling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sudoku as CSP

Variables = 81 cells.

Lĩnh vực (domain / 도메인) = digits 1..9 for empty cells.

Các ràng buộc (constraints / 제약조건들):

- each row AllDifferent;
- each column AllDifferent;
- each 3×3 khối (block / 블록) AllDifferent.

Human techniques like “only possible giá trị (value / 값)” are forms of ràng buộc (constraint / 제약조건) propagation.

Guess-and-backtrack happens only when propagation insufficient.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Scheduling** tiếp nhận điểm tựa từ **Sudoku as CSP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hard vs soft các ràng buộc (constraints / 제약조건들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Scheduling

Variables can be tasks.

Lĩnh vực (domain / 도메인) = possible times/resources.

Các ràng buộc (constraints / 제약조건들):

```text
Task A before B
A and C cannot use same machine simultaneously
employee E available only certain hours
max weekly capacity
```

Real scheduling often becomes richer **ràng buộc (constraint / 제약조건) Programming (CP)** or mixed-integer tối ưu hóa (optimization / 최적화) rather than simple finite-domain CSP.

> **Chuyển mạch:** Trong **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Hard vs soft các ràng buộc (constraints / 제약조건들)** tiếp nhận điểm tựa từ **Scheduling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SAT as ràng buộc (constraint / 제약조건) bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hard vs soft các ràng buộc (constraints / 제약조건들)

Classical CSP treats ràng buộc (constraint / 제약조건) as must satisfy.

Real bài toán (problem / 문제) often has soft preferences:

```text
hard: two meetings cannot occupy same room/time
soft: prefer morning
soft: minimize employee overtime
```

Weighted CSP / Max-CSP / tối ưu hóa (optimization / 최적화) formulations assign penalty/chi phí (cost / 비용) to violations.

This connects CSP with Operations Research.

> **Chuyển mạch:** Ở chặng này của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **SAT as ràng buộc (constraint / 제약조건) bài toán (problem / 문제)** tiếp nhận điểm tựa từ **Hard vs soft các ràng buộc (constraints / 제약조건들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đơn vị (unit / 단위) propagation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SAT as ràng buộc (constraint / 제약조건) bài toán (problem / 문제)

Boolean Satisfiability (SAT) asks whether Boolean formula has assignment making it true.

Variables are Boolean, các ràng buộc (constraints / 제약조건들) are clauses.

Example CNF:

\[
(A\lor \neg B)\land(B\lor C)
\]

SAT is NP-complete but hiện đại (modern / 현대적) SAT solvers are extremely effective on many structured instances using:

- đơn vị (unit / 단위) propagation;
- conflict-driven clause học tập (learning / 학습) (CDCL);
- variable heuristics;
- restarts.

“NP-complete” does not mean every real instance is impossible.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Đơn vị (unit / 단위) propagation** tiếp nhận điểm tựa từ **SAT as ràng buộc (constraint / 제약조건) bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Conflict-Driven Clause học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đơn vị (unit / 단위) propagation

If clause:

\[
(A\lor B)
\]

and `A=false`, then `B` must true.

This is ràng buộc (constraint / 제약조건) propagation over Boolean formula.

CSP and SAT share deep idea: suy luận (inference / 추론) shrinks domains before tìm kiếm (search / 검색) branches.

> **Chuyển mạch:** Trong **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Conflict-Driven Clause học tập (learning / 학습)** tiếp nhận điểm tựa từ **Đơn vị (unit / 단위) propagation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cục bộ (local / 로컬) tìm kiếm (search / 검색) for CSP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Conflict-Driven Clause học tập (learning / 학습)

When SAT solver reaches contradiction, it analyzes xung đột (conflict / 충돌) to derive new clause preventing same lớp (class / 클래스) of bad assignments.

This is tìm kiếm (search / 검색) that **learns from thất bại (failure / 실패)**.

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

This mẫu (pattern / 패턴) resembles hiện đại (modern / 현대적) lập luận (reasoning / 추론) các hệ thống (systems / 시스템들) with bộ nhớ (memory / 메모리)/xác minh (verification / 확인), though CDCL has formal Boolean ngữ nghĩa (semantics / 의미론) and stronger guarantees.

> **Chuyển mạch:** Ở chặng này của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Cục bộ (local / 로컬) tìm kiếm (search / 검색) for CSP** tiếp nhận điểm tựa từ **Conflict-Driven Clause học tập (learning / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **N-Queens** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cục bộ (local / 로컬) tìm kiếm (search / 검색) for CSP

Instead of building partial consistent assignment, start with complete possibly-invalid assignment and iteratively reduce conflicts.

**Min-conflicts** chooses conflicted variable and assigns giá trị (value / 값) minimizing violations.

It works surprisingly well for large N-Queens.

Cục bộ (local / 로컬) tìm kiếm (search / 검색) uses little bộ nhớ (memory / 메모리) but may get stuck and is not complete without additional chiến lược (strategy / 전략).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **N-Queens** tiếp nhận điểm tựa từ **Cục bộ (local / 로컬) tìm kiếm (search / 검색) for CSP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Symmetry breaking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## N-Queens

Place `N` queens on `N×N` board so no two attack each other.

Variables: one queen per column.

Lĩnh vực (domain / 도메인): row number.

Các ràng buộc (constraints / 제약조건들):

\[
Q_i\neq Q_j
\]

and:

\[
|Q_i-Q_j|\neq|i-j|
\]

CSP biểu diễn (representation / 표현) already eliminates same-column xung đột (conflict / 충돌) by construction. Good biểu diễn (representation / 표현) reduces các ràng buộc (constraints / 제약조건들) before thuật toán (algorithm / 알고리즘) starts.

> **Chuyển mạch:** Trong **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Symmetry breaking** tiếp nhận điểm tựa từ **N-Queens** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Decomposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Symmetry breaking

Many CSPs have symmetric equivalent solutions. tìm kiếm (search / 검색) wastes thời gian (time / 시간) rediscovering permutations.

Example coloring: swapping names Red/Green across entire valid solution produces equivalent solution.

Add symmetry-breaking các ràng buộc (constraints / 제약조건들) to choose chuẩn gốc (canonical / 정본) representative.

Again, biểu diễn (representation / 표현)/các ràng buộc (constraints / 제약조건들) can shrink tìm kiếm (search / 검색) không gian (space / 공간) dramatically.

> **Chuyển mạch:** Ở chặng này của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Decomposition** tiếp nhận điểm tựa từ **Symmetry breaking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CSP vs tối ưu hóa (optimization / 최적화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Decomposition

If ràng buộc (constraint / 제약조건) đồ thị (graph / 그래프) has independent components, solve each separately.

More generally, tree-structured CSPs can be solved efficiently compared with arbitrary cyclic graphs.

Đồ thị (graph / 그래프) **treewidth** measures roughly how far đồ thị (graph / 그래프) from tree-like; many algorithms exponential in treewidth rather than raw number variables.

This connects CSP to Graphical các mô hình (models / 모델들) and probabilistic suy luận (inference / 추론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **CSP vs tối ưu hóa (optimization / 최적화)** tiếp nhận điểm tựa từ **Decomposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ràng buộc (constraint / 제약조건) Programming** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CSP vs tối ưu hóa (optimization / 최적화)

CSP asks:

> Is there any assignment satisfying các ràng buộc (constraints / 제약조건들)?

Tối ưu hóa (optimization / 최적화) asks:

> Which feasible assignment has best mục tiêu (objective / 목표)?

Real các hệ thống (systems / 시스템들) often combine:

\[
\min_x f(x)\quad\văn bản (text / 텍스트){s.t. các ràng buộc (constraints / 제약조건들)}
\]

Scheduling, routing and tài nguyên (resource / 자원) allocation frequently use Mixed Integer Programming, CP-SAT or specialized solvers.

AI, Operations Research and tối ưu hóa (optimization / 최적화) overlap strongly here.

> **Chuyển mạch:** Trong **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Ràng buộc (constraint / 제약조건) Programming** tiếp nhận điểm tựa từ **CSP vs tối ưu hóa (optimization / 최적화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Learned heuristics for CSP/SAT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ràng buộc (constraint / 제약조건) Programming

Ràng buộc (constraint / 제약조건) Programming lets nhà phát triển (developer / 개발자) declare variables/các ràng buộc (constraints / 제약조건들) while solver handles propagation + tìm kiếm (search / 검색).

Example conceptual API:

```python
start_A < start_B
no_overlap(tasks_on_machine_1)
all_different(room_assignments)
```

This separates **what must be true** from chính xác (exact / 정확한) tìm kiếm (search / 검색) procedure.

Declarative modeling is similar spirit to lô-gic (logic / 논리) programming.

> **Chuyển mạch:** Ở chặng này của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Learned heuristics for CSP/SAT** tiếp nhận điểm tựa từ **Ràng buộc (constraint / 제약조건) Programming** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LLM + các ràng buộc (constraints / 제약조건들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Learned heuristics for CSP/SAT

Variable/giá trị (value / 값) thứ tự (ordering / 순서) dramatically affects thời gian chạy (runtime / 런타임). ML can learn branching heuristics from solved instances.

But solver tính đúng đắn (correctness / 정확성) can remain symbolic: learned thành phần (component / 컴포넌트) only chooses where tìm kiếm (search / 검색) first; ràng buộc (constraint / 제약조건) checker/proof machinery preserves validity.

This hybrid thiết kế (design / 설계) is attractive because học tập (learning / 학습) improves speed without trusting neural mô hình (model / 모델) for final tính đúng đắn (correctness / 정확성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **LLM + các ràng buộc (constraints / 제약조건들)** tiếp nhận điểm tựa từ **Learned heuristics for CSP/SAT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Structured đầu ra (output / 출력) kiểm tra hợp lệ (validation / 검증)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LLM + các ràng buộc (constraints / 제약조건들)

LLM can propose candidate schedule/cấu hình (configuration / 구성), but văn bản (text / 텍스트) generation does not guarantee hard các ràng buộc (constraints / 제약조건들).

Reliable kiến trúc (architecture / 아키텍처):

```text
LLM interprets natural-language requirements
        ↓
structured CSP/solver model
        ↓
constraint solver finds/verifies assignment
        ↓
LLM explains result
```

This is stronger than asking LLM to “remember all các ràng buộc (constraints / 제약조건들)” in free-form generation.

> **Chuyển mạch:** Trong **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Structured đầu ra (output / 출력) kiểm tra hợp lệ (validation / 검증)** tiếp nhận điểm tựa từ **LLM + các ràng buộc (constraints / 제약조건들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Structured đầu ra (output / 출력) kiểm tra hợp lệ (validation / 검증)

JSON lược đồ (schema / 스키마)/kiểu (type / 타입) các ràng buộc (constraints / 제약조건들) are simpler cousin of CSP. Decoder or post-validator ensures đầu ra (output / 출력) belongs to valid structural lĩnh vực (domain / 도메인).

Grammar-constrained decoding reduces invalid cú pháp (syntax / 문법), but ngữ nghĩa (semantic / 의미적) các ràng buộc (constraints / 제약조건들) like “end date after start date” need richer kiểm tra hợp lệ (validation / 검증)/solver lô-gic (logic / 논리).

> **Chuyển mạch:** Ở chặng này của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Structured đầu ra (output / 출력) kiểm tra hợp lệ (validation / 검증)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Variable   = thing we must choose
Domain     = options available
Constraint = combinations forbidden/required
Propagation = remove impossible values without guessing
Search      = branch when inference alone insufficient
Heuristic   = choose branching variable/value intelligently
Learning    = optionally improve heuristic, not necessarily correctness rule
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “CSP là brute force assignment”

Good CSP solvers use propagation, heuristics, học tập (learning / 학습) and decomposition to avoid most combinations.

### “Arc consistency means solved”

Cục bộ (local / 로컬) consistency can hold while no toàn cục (global / 전역) solution exists.

### “LLM can replace ràng buộc (constraint / 제약조건) solver nếu mô hình (model / 모델) đủ lớn”

LLM may propose solutions, but hard guarantees require tường minh (explicit / 명시적) kiểm tra hợp lệ (validation / 검증)/tìm kiếm (search / 검색)/formal cơ chế (mechanism / 메커니즘) when tính đúng đắn (correctness / 정확성) matters.

### “NP-complete nghĩa practical solver vô dụng”

Worst-case độ phức tạp (complexity / 복잡도) does not predict all structured instances. SAT/CP solvers solve many large real problems effectively.

> **Chuyển mạch:** Trong **Ràng buộc (constraint / 제약조건) Satisfaction Problems trong AI**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

CSP sits at intersection of tìm kiếm (search / 검색), lô-gic (logic / 논리), Graphs and tối ưu hóa (optimization / 최적화). It teaches a recurring AI lesson: **reason before branching**. ràng buộc (constraint / 제약조건) propagation converts kiến thức (knowledge / 지식) into lĩnh vực (domain / 도메인) reduction, just as heuristics convert kiến thức (knowledge / 지식) into tìm kiếm (search / 검색) priority.

Xem tiếp: [Planning](./05_planning.md), nơi actions có preconditions/effects và goal thường cần một sequence thay vì chỉ final assignment.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
