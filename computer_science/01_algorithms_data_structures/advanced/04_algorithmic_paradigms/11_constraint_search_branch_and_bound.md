# Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa
**Constraint Search & Branch-and-Bound / 제약 탐색과 분기 한정법**

Backtracking cơ bản thử một lựa chọn, đi sâu, rồi hoàn tác. Nhưng trong các bài tổ hợp thực tế, khác biệt giữa một bộ giải chạy được và một bộ giải bất khả thi thường nằm ở **mô hình trạng thái, propagation, thứ tự phân nhánh và cận** chứ không phải ở cú pháp đệ quy.

Chương này tập trung vào cách biến cây tìm kiếm thô thành một hệ thống suy luận có chủ đích.

## 1. Search Tree chỉ là biểu diễn của không gian nghiệm

Mỗi node trong cây tìm kiếm đại diện một **trạng thái từng phần (partial state)**. Mỗi cạnh là một quyết định.

Ví dụ trong Sudoku:

```text
state = các ô đã gán + miền giá trị còn lại của các ô chưa gán
branch = chọn một giá trị cho một ô
```

Trong TSP:

```text
state = đường đi từng phần + thành phố chưa thăm
branch = chọn thành phố tiếp theo
```

Điểm quan trọng là cây tìm kiếm không tồn tại sẵn; nó được sinh từ **cách ta chọn biến trạng thái và quyết định**. Một mô hình khác có thể làm branching factor nhỏ đi rất nhiều.

## 2. Constraint Satisfaction Problem

Một **bài toán thỏa ràng buộc (Constraint Satisfaction Problem – CSP)** thường có:

```text
variables
mỗi variable có domain
constraints giữa các variables
```

Mục tiêu có thể chỉ là tìm một phép gán hợp lệ hoặc tối ưu thêm một objective.

Sudoku, graph coloring, scheduling, n-queens và nhiều configuration problem đều có thể nhìn theo mô hình này.

## 3. Forward Checking

Khi gán một biến, đừng chờ tới khi sâu hơn mới phát hiện xung đột. Hãy cập nhật miền của các biến liên quan ngay lập tức.

Nếu một biến chưa gán bị mất hết domain, branch hiện tại chắc chắn thất bại và có thể quay lui ngay.

Đây là **forward checking**.

Nó biến kiểm tra từ “đến cuối mới biết sai” thành “phát hiện contradiction sớm”.

## 4. Constraint Propagation

Forward checking chỉ là mức đơn giản. **Constraint propagation** lặp lại việc suy ra hậu quả của các domain bị thu hẹp.

Ví dụ nếu một ô Sudoku chỉ còn một ứng viên, ta gán nó; phép gán này lại làm giảm domain của các ô cùng hàng/cột/khối; quá trình tiếp tục cho tới khi không còn suy ra mới.

Search và propagation tạo hai pha:

```text
propagate đến điểm cố định
nếu contradiction -> backtrack
nếu hoàn tất -> solution
nếu chưa -> branch
```

Bộ giải mạnh thường dành nhiều công sức cho propagation để giảm search tree.

## 5. Arc Consistency

Với ràng buộc nhị phân giữa hai biến `X` và `Y`, một giá trị `x` trong domain của `X` có **support** nếu tồn tại ít nhất một `y` trong domain của `Y` sao cho `(x,y)` thỏa constraint.

Nếu không có support, `x` có thể bị loại.

Các thuật toán như AC-3 liên tục xử lý các cung bị ảnh hưởng cho tới khi đạt arc consistency hoặc một domain rỗng.

Propagation mạnh hơn tốn nhiều chi phí mỗi node nhưng có thể giảm mạnh số node phải search. Đây là trade-off giống nhiều cấu trúc DSA khác: trả thêm tiền cục bộ để giảm không gian tương lai.

## 6. MRV: chọn biến khó nhất trước

**Minimum Remaining Values (MRV)** chọn biến có domain nhỏ nhất chưa được gán.

Trực giác là **fail first**: nếu một branch sắp mâu thuẫn, hãy tìm ra càng sớm càng tốt thay vì xây một cây con lớn rồi mới thất bại.

Trong graph coloring, có thể ưu tiên vertex còn ít màu hợp lệ. Trong Sudoku, chọn ô có ít ứng viên nhất.

MRV không thay đổi tập lời giải; nó chỉ đổi shape của cây tìm kiếm.

## 7. Degree Heuristic

Nếu nhiều biến có cùng MRV, có thể ưu tiên biến liên quan tới nhiều constraint chưa giải quyết nhất.

Biến “ảnh hưởng rộng” có khả năng tạo propagation mạnh hơn.

Một heuristic chọn biến tốt thường cân bằng:

```text
constrained nhất hiện tại
và
có khả năng ràng buộc phần còn lại nhiều nhất
```

## 8. Least Constraining Value

Sau khi chọn biến, thứ tự thử giá trị cũng quan trọng.

**Least Constraining Value (LCV)** thử giá trị loại ít lựa chọn của các biến khác nhất trước. Ý tưởng là giữ tương lai linh hoạt nếu đang tìm một nghiệm.

Tuy nhiên, nếu mục tiêu là chứng minh không có nghiệm, đôi khi giá trị gây contradiction sớm có thể hữu ích hơn. Heuristic phải phù hợp objective.

## 9. Symmetry Breaking

Nhiều cây tìm kiếm chứa các branch khác nhau về biểu diễn nhưng tương đương về ngữ nghĩa.

Ví dụ graph coloring với màu `{red, green, blue}`: đổi tên toàn bộ màu có thể tạo một nghiệm tương đương.

Nếu không phá đối xứng, solver có thể tìm cùng cấu trúc nghiệm nhiều lần dưới các nhãn khác nhau.

Có thể thêm constraint như:

```text
vertex đầu tiên luôn dùng màu 0
màu mới chỉ được mở theo thứ tự 0,1,2,...
```

Symmetry breaking không loại nghiệm theo lớp tương đương; nó chọn một đại diện canonical cho mỗi lớp.

## 10. Canonical State và Memoization

Nếu hai lịch sử khác nhau dẫn đến trạng thái tương đương cho tương lai, có thể memoize theo một dạng canonical.

Ví dụ trong game search, trạng thái bàn cờ có thể canonicalize dưới các phép quay/đối xứng nếu luật chơi đối xứng.

Nhưng canonicalization bản thân có chi phí. Chỉ đáng dùng khi giảm đủ nhiều trạng thái trùng lặp.

## 11. Branch-and-Bound khác Backtracking thuần túy

Backtracking thường cắt branch khi **không còn khả thi**.

Branch-and-Bound còn cắt khi branch **vẫn khả thi nhưng không thể đánh bại nghiệm tốt nhất đã biết**.

Ta duy trì:

```text
incumbent = nghiệm tốt nhất đã tìm thấy
bound(state) = cận tốt nhất có thể đạt từ state
```

Nếu bài maximize và:

```text
bound(state) <= incumbent
```

thì không cần mở rộng state.

## 12. Cận phải optimistic

Một cận dùng để prune phải “lạc quan” theo đúng hướng.

Với bài maximize, upper bound phải ít nhất bằng mọi kết quả thật có thể đạt từ branch. Nếu bound đánh giá thấp, ta có thể cắt nhầm branch chứa optimum.

Với bài minimize, cần lower bound không lớn hơn optimum còn có thể đạt.

Độ chặt của bound quyết định sức mạnh pruning; tính hợp lệ của bound quyết định correctness.

## 13. Knapsack Branch-and-Bound

Trong 0/1 Knapsack, một upper bound phổ biến là cho phép lấy phân số các vật còn lại giống Fractional Knapsack.

Vì phiên bản fractional nới lỏng constraint 0/1, giá trị của nó không nhỏ hơn optimum 0/1 thật. Do đó nó là upper bound hợp lệ cho bài maximize.

Nếu upper bound này đã không vượt incumbent, toàn bộ branch có thể bỏ.

Đây là pattern rất quan trọng:

> **Giải một bài toán nới lỏng dễ hơn để tạo cận cho bài toán khó hơn.**

## 14. Relaxation

Một **relaxation** bỏ bớt một số constraint để tạo bài dễ hơn.

Ví dụ:

```text
0/1 variable -> cho phép liên tục [0,1]
integer program -> linear programming relaxation
TSP -> minimum spanning tree / 1-tree lower bound
```

Vì feasible region của bài nới lỏng lớn hơn, optimum của relaxation tạo cận cho bài gốc theo hướng phù hợp.

Relaxation là cầu nối giữa Branch-and-Bound, LP/ILP và approximation.

## 15. Best-First Branch-and-Bound

DFS branch-and-bound dùng ít bộ nhớ và nhanh tìm một nghiệm sâu. Nhưng có thể mở rộng node theo cận tốt nhất trước bằng priority queue.

```text
frontier ordered by bound
pop state có triển vọng nhất
```

Cách này gần A*: frontier là các partial solutions và key phản ánh tiềm năng tối ưu.

Đổi lại, bộ nhớ có thể rất lớn vì giữ nhiều node đang chờ.

## 16. DFS, BFS hay Best-First?

Không có chiến lược mở rộng duy nhất tốt nhất.

```text
DFS        -> ít memory, incumbent có thể tìm sớm nếu order tốt
BFS        -> hiếm khi phù hợp search tổ hợp lớn
Best-first -> ưu tiên bound tốt, memory cao
```

Nếu incumbent tốt rất quan trọng để prune, ta thường muốn heuristic branch order giúp tìm nghiệm chất lượng cao sớm.

## 17. Incumbent Quality

Branch-and-bound mạnh khi có nghiệm khả thi tốt từ sớm. Một heuristic greedy có thể tạo incumbent ban đầu rất nhanh.

Sau đó exact search dùng incumbent đó để cắt branch.

Đây là composition hữu ích:

```text
heuristic nhanh -> upper/lower feasible solution
exact search    -> chứng minh không còn nghiệm tốt hơn
```

Heuristic và exact algorithm không đối lập; chúng có thể hỗ trợ nhau.

## 18. TSP: lower bound bằng MST

Trong một partial tour, phần còn lại vẫn phải nối các thành phố chưa thăm. Một lower bound đơn giản có thể gồm:

```text
cost đã đi
+ MST của các node chưa thăm
+ chi phí kết nối hiện tại vào phần còn lại
+ chi phí quay về đích
```

Bound càng chặt, search càng ít. Nhưng tính MST ở mọi node cũng đắt.

Ta phải tối ưu cả **bound quality** lẫn **bound evaluation cost**.

## 19. Alpha-Beta Pruning

Trong minimax game tree, alpha-beta pruning dùng cận từ các lựa chọn đã xem để loại branch không thể ảnh hưởng kết quả cuối.

`alpha` là giá trị tốt nhất phía maximizing đã bảo đảm; `beta` là giá trị tốt nhất phía minimizing đã bảo đảm.

Khi:

```text
alpha >= beta
```

branch hiện tại không thể thay đổi quyết định của tổ tiên tương ứng.

Đây là branch-and-bound trong game search dưới dạng hai phía đối kháng.

## 20. Move Ordering trong Alpha-Beta

Alpha-beta cho cùng kết quả minimax bất kể thứ tự move, nhưng hiệu năng phụ thuộc mạnh vào thứ tự.

Nếu xét move tốt trước, alpha/beta chặt sớm và prune nhiều hơn. Iterative deepening, killer move, history heuristic hoặc transposition table giúp cải thiện ordering.

Đây là ví dụ correctness không đổi nhưng traversal order thay đổi complexity thực tế rất lớn.

## 21. Transposition Table

Trong game tree, nhiều sequence move khác nhau có thể dẫn tới cùng board state. Nếu coi cấu trúc là tree, ta tính lại state nhiều lần; thực ra không gian là graph.

**Transposition table** dùng hash table lưu kết quả/cận đã biết cho state.

Entry thường cần:

```text
hash key
depth
evaluation
bound type: exact/lower/upper
best move
```

Không nên cache một evaluation nông rồi dùng như kết quả chính xác cho search sâu hơn.

## 22. Zobrist Hashing

Board state lớn cần hash cập nhật nhanh. Zobrist hashing gán số ngẫu nhiên cho mỗi `(piece, position)` và XOR các giá trị đang hiện diện.

Khi move một quân, hash có thể cập nhật bằng vài phép XOR thay vì băm lại toàn board.

Đây là một ví dụ tuyệt vời của **incremental representation**: state thay đổi ít thì fingerprint cũng cập nhật ít.

Collision vẫn có xác suất; hệ thống yêu cầu tuyệt đối có thể lưu thêm verification data.

## 23. SAT: Search + Propagation ở quy mô công nghiệp

SAT solver hiện đại không chỉ là thử True/False đơn giản. Các kỹ thuật quan trọng gồm:

```text
unit propagation
conflict analysis
clause learning
non-chronological backtracking
variable activity heuristic
restart
```

Điểm đáng học cho DSA là search mạnh thường biến failure thành **kiến thức mới** để tránh lặp lại cùng vùng sai.

## 24. Clause Learning như Memoization của Conflict

Khi một tập quyết định dẫn tới contradiction, solver phân tích conflict và học một clause mới biểu diễn “tổ hợp này không được phép lặp lại”.

Đây là dạng tổng quát hơn của memoizing một trạng thái fail. Thay vì nhớ nguyên state, ta rút ra một constraint có thể prune nhiều state tương lai.

## 25. Non-Chronological Backtracking

Backtracking cổ điển quay lại đúng một mức. Nhưng nếu conflict thực sự do quyết định ở xa hơn, quay từng mức là lãng phí.

Conflict analysis có thể xác định **backjump level** và quay thẳng tới quyết định liên quan.

Điều này cho thấy call-stack order không nhất thiết phải là logic dependency order.

## 26. Restart không có nghĩa là mất toàn bộ công việc

SAT solver có thể restart search định kỳ nhưng giữ lại learned clauses. Restart thay đổi đường exploration trong khi tri thức về các vùng thất bại vẫn được bảo toàn.

Đây là ví dụ search không nhất thiết tiến tuyến tính “đi sâu rồi quay lại”; nó có thể chủ động reset trajectory khi state học được đã thay đổi landscape.

## 27. Iterative Deepening

Nếu solution depth chưa biết, DFS giới hạn độ sâu có thể chạy lần lượt với limit tăng dần.

```text
limit 0
limit 1
limit 2
...
```

Dù các tầng nông được duyệt lại, trong cây có branching factor lớn phần lớn node nằm ở tầng sâu nhất, nên chi phí lặp lại thường chấp nhận được.

Iterative deepening kết hợp memory của DFS với khả năng tìm solution nông giống BFS.

## 28. IDA*

IDA* dùng ngưỡng trên `f = g + h` thay vì depth. Mỗi iteration DFS chỉ đi qua node có `f <= threshold`; ngưỡng sau tăng tới giá trị nhỏ nhất vượt ngưỡng cũ.

Nó giảm memory so với A* nhưng có thể lặp lại nhiều công việc.

Heuristic admissible giữ optimality tương tự A* trong mô hình chuẩn.

## 29. Dominance Pruning

Nếu hai partial states có cùng future-relevant state nhưng một state không tốt hơn state kia về mọi tiêu chí, state bị trội có thể bỏ.

Ví dụ cùng `(position, usedResources)` nhưng một path có cost lớn hơn; state cost lớn hơn không cần tiếp tục.

Đây là nguyên lý **dominance**. DP thường giữ trạng thái tốt nhất; branch-and-bound dùng dominance để prune search trực tiếp.

## 30. Pareto Frontier

Nếu có nhiều objective/resource, không thể chỉ giữ một state tốt nhất bằng scalar.

Ta giữ các state không bị state nào khác trội trên mọi chiều, tạo **Pareto frontier**.

Ví dụ route theo `(time, cost)`: route A nhanh hơn nhưng đắt hơn route B; cả hai có thể cần giữ.

Frontier có thể tăng lớn, vì vậy multi-objective search khó hơn đáng kể.

## 31. Bitmask DP và Search: ranh giới không tuyệt đối

Một bài TSP nhỏ có thể giải bằng Held–Karp DP `O(n^2 2^n)` hoặc branch-and-bound.

DP trả chi phí dự đoán được theo state space. Branch-and-bound có trường hợp xấu rất lớn nhưng có thể chạy nhanh trên instance dễ nhờ pruning.

Lựa chọn phụ thuộc:

```text
n
memory
instance structure
cần worst-case predictability hay average practical speed
```

## 32. Meet-in-the-Middle

Khi brute force có `2^n`, chia biến thành hai nửa có thể tạo khoảng `2^{n/2}` states mỗi phía rồi ghép.

Subset Sum là ví dụ điển hình.

Đây không phải backtracking thuần túy mà là thay shape của không gian tìm kiếm: đổi một cây sâu thành hai tập state vừa phải + bước matching/search.

## 33. Branching Factor và Effective Search Tree

Complexity thô thường viết:

\[
O(b^d)
\]

với branching factor `b`, depth `d`. Nhưng propagation và pruning làm `b` hiệu dụng thay đổi theo tầng.

Một heuristic tốt có thể không thay worst-case asymptotic nhưng giảm số node thực tế hàng triệu lần.

Vì vậy benchmark search nên đo:

```text
nodes expanded
prune ratio
propagation operations
bound evaluations
maximum depth
incumbent improvement timeline
```

không chỉ wall-clock time.

## 34. Kiểm thử Search Solver

Cần tách ba lớp:

```text
feasibility checker đúng không?
search có bỏ sót solution không?
objective có tối ưu đúng không?
```

Với input nhỏ, exhaustive enumeration là oracle rất mạnh.

Có thể sinh random instance nhỏ rồi so:

```text
optimized solver
vs
brute-force solver
```

Nếu solver dùng bound, nên thêm test kiểm tra bound luôn hợp lệ trên state nhỏ bằng cách tính optimum thật của subtree.

## 35. Reversible State

Mutable + undo thường nhanh nhưng dễ bug. Một pattern an toàn là ghi log thay đổi:

```text
checkpoint = changeStack.size()
apply changes and push old values
recurse
rollback until checkpoint
```

Rollback DSU dùng đúng tư duy này. Constraint solver cũng có thể quản domain updates bằng trail stack.

Điểm mạnh là undo không cần viết logic ngược riêng cho từng operation; chỉ restore các giá trị đã ghi.

## 36. Persistent State

Cấu trúc persistent tạo phiên bản mới bằng structural sharing. Nó giảm rủi ro quên undo và phù hợp search phân nhánh, nhưng có thêm allocation và metadata.

Trong functional programming hoặc search cần giữ nhiều frontier states đồng thời, persistent structures có thể rất tự nhiên.

## 37. Parallel Search

Các branch độc lập có thể chạy song song, nhưng cần xử lý:

```text
chia work
cập nhật incumbent dùng chung
hủy branch khi bound mới mạnh hơn
tránh duplicate search
reproducibility
```

Work stealing phù hợp khi kích thước subtree khó dự đoán.

Một incumbent tốt tìm được bởi một worker có thể giúp mọi worker khác prune mạnh hơn, vì vậy communication có giá trị.

## 38. Anytime Algorithm

Một số branch-and-bound có thể trả nghiệm khả thi sớm và tiếp tục cải thiện, đồng thời duy trì gap giữa incumbent và bound tốt nhất còn lại.

Nếu bị dừng giữa chừng, hệ thống vẫn có:

```text
một nghiệm khả thi
và
một chứng nhận khoảng cách tới tối ưu
```

Đây là đặc tính cực hữu ích trong scheduling và optimization production có time budget.

## 39. Khi nào dùng DP, khi nào dùng Search?

DP phù hợp khi state space có thể liệt kê tương đối gọn và nhiều lịch sử hội tụ về cùng state.

Search phù hợp khi:

```text
state space lý thuyết lớn
nhưng constraint/bound có thể prune mạnh
cần một solution sớm
instance thực tế có structure thuận lợi
```

Hybrid rất phổ biến: search bên ngoài, memoization/DP cho subproblem lặp lại bên trong.

## 40. Decision Checklist

Trước một bài tổ hợp khó, hãy hỏi:

```text
State tối thiểu là gì?
Có propagation nào làm domain nhỏ trước khi branch không?
Biến nào nên chọn trước để fail sớm?
Có symmetry để canonicalize không?
Có relaxation tạo bound không?
Có incumbent heuristic tốt không?
Có state dominance/memoization không?
Có cần optimality proof hay chỉ feasible solution tốt?
Có time budget để dùng anytime search không?
```

## Mô hình tư duy

> Search hiệu quả không phải “đệ quy nhanh hơn”. Nó là **quản lý thông tin để càng nhiều nhánh bị chứng minh là không cần mở càng sớm càng tốt**.

Bốn đòn bẩy chính là:

```text
mô hình trạng thái tốt
propagation mạnh
branch ordering tốt
bound/certificate chặt
```

Nếu search tree vẫn quá lớn, đừng chỉ tối ưu code; hãy hỏi thông tin nào chưa được khai thác để loại cả một vùng trạng thái.

Xem thêm: [Recursion & Backtracking](./02_recursion_and_backtracking.md), [Dynamic Programming](./05_dynamic_programming.md), [Hard Problems & Approximation](./09_hard_problems_reductions_and_approximation.md), [Greedy nâng cao](./10_greedy_matroids_primal_dual_and_approximation.md), [Hash Tables](../01_linear_structures/04_hash_tables.md), [Amortized/Randomized Thinking](../05_specialized/03_amortized_randomized_and_probabilistic_thinking.md).