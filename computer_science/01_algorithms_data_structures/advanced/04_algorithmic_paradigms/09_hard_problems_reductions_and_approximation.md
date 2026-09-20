# Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation
**Reductions, NP-Completeness & Approximation / 환원, NP-완전, 근사 알고리즘**

DSA không chỉ dạy cách làm một thuật toán nhanh hơn. Một mức trưởng thành quan trọng là nhận ra khi bản chất bài toán đã khó tới mức việc tiếp tục đổi `ArrayList` thành `HashMap`, hoặc tối ưu `O(n²)` thành `O(n log n)`, không còn giải quyết nút thắt chính.

Khi đó câu hỏi chuyển từ:

> “Làm sao tối ưu implementation này?”

sang:

> “Bài toán tổng quát có cấu trúc hardness nào? Có special case dễ hơn không? Parameter nào nhỏ? Có thể dùng exact exponential algorithm thông minh, approximation, heuristic hoặc solver chuyên dụng không?”

Mục tiêu chương này là dùng complexity theory như một **công cụ engineering**, không phải danh sách thuật ngữ để học thuộc.

## Polynomial và exponential khác nhau về bản chất tăng trưởng

`O(n³)` có thể chậm, nhưng vẫn polynomial. `O(2^n)` có tốc độ tăng khác hẳn: tăng `n` thêm 1 có thể gần như nhân đôi số trạng thái.

```text
2^20 ≈ 1 triệu
2^30 ≈ 1 tỷ
2^40 ≈ 1 nghìn tỷ
```

Điều này không có nghĩa exponential luôn vô dụng. Nếu parameter thực tế chỉ 20–30, hoặc pruning rất mạnh, exact exponential algorithm có thể là lựa chọn tốt nhất.

Điều cần nhớ là **input size thực** đôi khi không phải chỉ một biến `n`; độ lớn số được mã hóa bằng bao nhiêu bit cũng quan trọng.

## Input length và giá trị số

Giả sử capacity `W = 1,000,000`. Giá trị `W` cần chỉ khoảng `log₂ W` bit để biểu diễn.

Một algorithm `O(nW)` là polynomial theo **giá trị số** `W`, nhưng không polynomial theo **độ dài encoding** `log W`.

Đây là nguồn gốc khái niệm **giả đa thức (pseudo-polynomial)**.

Phân biệt này giải thích vì sao một bài NP-hard vẫn có DP rất thực dụng khi numeric parameter nhỏ.

## Decision problem và optimization problem

Complexity theory thường mô tả **decision problem** với đầu ra yes/no.

Optimization TSP:

> Tour ngắn nhất dài bao nhiêu?

Decision TSP:

> Có tour đi qua mọi đỉnh với tổng chi phí `<= B` không?

Nếu giải optimization được, decision thường dễ suy ra. Ngược lại, trong nhiều bài, optimization có thể được dựng từ decision qua repeated queries hoặc binary search nếu objective có miền thích hợp.

Việc chuyển sang decision version giúp định nghĩa lớp P/NP và reduction rõ ràng hơn.

## Class P

**P** là lớp decision problems có deterministic polynomial-time algorithm trong mô hình tính toán chuẩn.

Ví dụ quen thuộc:

```text
shortest path
minimum spanning tree
maximum flow
bipartite matching
2-SAT
```

“Polynomial” không đồng nghĩa “luôn nhanh”. `O(n^10)` vẫn polynomial nhưng có thể không practical. P là khái niệm về tốc độ tăng lý thuyết, không phải SLA production.

## Class NP

**NP** là lớp decision problems mà với một instance có đáp án “yes”, tồn tại một **certificate** có thể được verify trong polynomial time.

Ví dụ Hamiltonian Cycle: certificate là một thứ tự các đỉnh. Verification chỉ cần kiểm tra mỗi đỉnh xuất hiện đúng quy tắc và mọi cạnh liên tiếp tồn tại.

NP không có nghĩa “not polynomial” hay “không giải được”. Ta biết:

\[
P\subseteq NP
\]

vì nếu solve được polynomial thì hiển nhiên verify cũng polynomial.

## NP-hard và NP-complete

**NP-hard** nghĩa bài toán ít nhất khó như mọi bài trong NP dưới một notion reduction phù hợp.

**NP-complete** nghĩa:

```text
problem ∈ NP
và
problem là NP-hard
```

Nếu có polynomial-time algorithm cho một NP-complete problem, thì suy ra mọi problem trong NP có polynomial-time algorithm.

Điểm engineering quan trọng không phải tranh luận lý thuyết, mà là: khi nhận ra bài toán tương đương một NP-hard core quen thuộc, ta phải đổi chiến lược giải.

## NP-complete không có nghĩa mọi instance đều khó

Hardness là phát biểu về lớp input tổng quát và worst-case.

Instance thực tế có thể dễ vì:

```text
n nhỏ
parameter nhỏ
graph sparse
constraint rất chặt
cấu trúc gần cây
treewidth nhỏ
numeric range nhỏ
dữ liệu có geometry đặc biệt
solver heuristic rất phù hợp
```

Vì vậy “bài này NP-hard” không phải điểm kết thúc. Nó là tín hiệu để hỏi: **structure nào của instance thực tế có thể khai thác?**

## Reduction: ngôn ngữ để so sánh độ khó

Một polynomial-time reduction từ `A` sang `B` biến instance `x` của A thành `f(x)` của B sao cho:

\[
x\in A \iff f(x)\in B
\]

và `f` tính được trong polynomial time.

Ký hiệu:

\[
A\le_p B
\]

Nếu A đã biết hard và `A <=p B`, thì B ít nhất hard như A.

### Direction rất dễ nhầm

Muốn chứng minh `B` hard, phải biến **bài đã biết hard A thành B**.

```text
known hard A  ->  target B
```

Nếu chỉ biết cách biến B thành A, điều đó cho thấy có thể dùng solver A để giải B; nó không chứng minh B hard.

## Reduction cần chứng minh hai chiều semantics

Một reduction đúng thường cần:

```text
A yes -> B yes
B yes -> A yes
```

Nếu chỉ chứng minh một chiều, transformation có thể tạo thêm lời giải giả hoặc làm mất lời giải hợp lệ.

Ngoài ra cần chứng minh transformation chạy polynomial và kích thước instance mới không phình exponential.

## Reduction không chỉ dùng để chứng minh hardness

Trong algorithm design, reduction là kỹ năng cực kỳ tích cực:

```text
assignment                 -> bipartite matching
2-SAT                      -> implication graph + SCC
subtree query              -> Euler Tour + range query
difference constraints     -> shortest path
circulation                -> flow
interval overlap           -> sweep line
```

Khi reduce được bài mới về một primitive đã hiểu, ta tái sử dụng cả algorithm, proof và implementation pattern.

## SAT như ngôn ngữ ràng buộc

SAT hỏi liệu có assignment Boolean làm công thức đúng hay không.

CNF là conjunction của nhiều clause; mỗi clause là disjunction của literals.

Ví dụ:

\[
(x\lor \neg y\lor z)\land(\neg x\lor y)
\]

SAT quan trọng vì rất nhiều bài combinatorial có thể encode thành Boolean constraints.

Modern SAT solver dùng nhiều kỹ thuật mạnh như propagation, clause learning và branching heuristics, nên nhiều instance lớn có thể giải rất nhanh dù worst-case vẫn exponential.

## 3-SAT và 2-SAT: thay một chi tiết, landscape thay đổi

3-SAT vẫn NP-complete.

2-SAT lại giải được polynomial bằng implication graph.

Clause:

\[
(a\lor b)
\]

suy ra:

```text
¬a -> b
¬b -> a
```

Formula satisfiable khi không biến nào nằm cùng SCC với phủ định của chính nó.

Bài học cực kỳ quan trọng:

> Một restriction nhỏ của problem có thể biến bài tổng quát hard thành special case dễ.

Do đó luôn tìm cấu trúc đặc biệt trước khi áp một solver tổng quát.

## Clique, Independent Set và Vertex Cover

Trong đồ thị vô hướng:

\[
S\text{ là independent set}\iff V\setminus S\text{ là vertex cover}
\]

Và `S` là clique trong `G` khi và chỉ khi `S` là independent set trong complement graph `\bar G`.

Ba bài tưởng khác nhau nhưng liên kết chặt qua complement và set complement.

Những quan hệ này giúp rèn khả năng nhìn “cùng một ràng buộc dưới biểu diễn khác”.

## Knapsack và pseudo-polynomial DP

0/1 Knapsack có DP dạng:

```text
dp[capacity]
```

với runtime `O(nW)`.

Nếu `W` nhỏ, đây là cách cực kỳ thực dụng. Nếu `W` được biểu diễn bằng nhiều bit và rất lớn, `O(nW)` có thể exponential theo input encoding length.

Đây là lý do Knapsack vừa có hardness theory vừa có DP nổi tiếng mà không mâu thuẫn.

## Weakly và strongly NP-hard: trực giác

Một số problem hard chủ yếu vì numeric values có thể rất lớn và có pseudo-polynomial algorithm. Đây là kiểu hardness yếu hơn về mặt cấu trúc.

Strongly NP-hard problems vẫn hard ngay cả khi numeric values được giới hạn polynomial theo input size, nên pseudo-polynomial strategy không giải quyết bản chất tương tự.

Không cần nhớ toàn bộ taxonomy; điều cần học là **numeric magnitude có thể là một parameter ẩn của complexity**.

## Exact exponential algorithm vẫn rất có giá trị

Toolbox exact gồm:

```text
backtracking
branch and bound
bitmask DP
meet-in-the-middle
subset DP
SAT/SMT/ILP/CP-SAT
parameterized algorithm
```

Nếu `n=25`, một `2^n` algorithm tốt có thể hoàn toàn hợp lý. Nếu business yêu cầu exact result, approximation có thể không chấp nhận được.

## Meet-in-the-middle

Tách `n` phần tử thành hai nửa.

Thay vì duyệt:

\[
2^n
\]

ta duyệt khoảng:

\[
2^{n/2}+2^{n/2}
\]

rồi kết hợp bằng sort, hash hoặc binary search.

Subset Sum với `n≈40` là ví dụ kinh điển.

Meet-in-the-middle đổi thêm memory để giảm exponent của time.

## Bitmask DP

TSP Held–Karp:

```text
dp[mask][v] = chi phí nhỏ nhất đi qua tập mask và kết thúc tại v
```

Số state:

\[
O(n2^n)
\]

và transition thường dẫn tới:

\[
O(n^2 2^n)
\]

Nó vẫn exponential, nhưng tốt hơn `n!` brute force rất nhiều.

Điểm sâu hơn là state compression: nhiều thứ tự lịch sử khác nhau được gộp nếu chúng có cùng `(mask,v)` và tương lai chỉ phụ thuộc hai thông tin đó.

## Branch and Bound

Backtracking loại nhánh khi biết nó infeasible. **Branch and Bound** còn dùng một bound lạc quan về objective tốt nhất có thể đạt từ nhánh.

Với minimization:

```text
if lowerBound(state) >= bestKnown:
    prune
```

Bound phải **an toàn**. Nếu bound quá lạc quan, prune ít. Nếu bound sai theo hướng quá mạnh, có thể cắt mất optimum và phá correctness.

Thiết kế bound thường là phần khó nhất.

## Search ordering và incumbent

Branch-and-bound vẫn đúng nếu duyệt nhánh theo thứ tự bất kỳ, nhưng tìm được một lời giải tốt sớm sẽ làm `bestKnown` mạnh hơn và prune được nhiều hơn.

Do đó heuristic ordering có thể thay runtime thực tế hàng bậc độ lớn mà không thay worst-case complexity.

Đây là khác biệt giữa:

```text
correctness guarantee
và
practical search engineering
```

## Constraint propagation

Trong CSP/SAT, trước khi branch có thể suy ra các hậu quả bắt buộc.

Nếu một biến chỉ còn một giá trị hợp lệ, gán nó ngay. Nếu assignment khiến clause/unit/constraint khác bị ép, tiếp tục propagate.

Propagation giúp phát hiện contradiction sớm, làm cây search nhỏ hơn rất nhiều.

Backtracking “thô” và solver hiện đại khác nhau chủ yếu ở lượng thông tin được suy ra trước khi phải đoán tiếp.

## Memoization trong search khó

Hai nhánh search khác nhau có thể dẫn tới cùng state logic. Nếu tương lai chỉ phụ thuộc state, có thể memoize để tránh giải lại.

Đây là cầu nối giữa backtracking và DP.

Một cách nhìn:

```text
backtracking = duyệt cây lịch sử
DP/memoization = gom các lịch sử tương đương thành cùng node trạng thái
```

Nếu số state duy nhất nhỏ hơn rất nhiều số đường đi lịch sử, memoization tạo khác biệt lớn.

## Parameterized complexity

Thay vì chỉ hỏi runtime theo `n`, ta chọn một parameter `k` phản ánh phần khó.

Một algorithm **fixed-parameter tractable (FPT)** có dạng:

\[
f(k)\cdot n^{O(1)}
\]

`f(k)` có thể exponential theo `k`, nhưng nếu `k` nhỏ thì toàn bộ algorithm vẫn practical.

Ví dụ mindset:

```text
n rất lớn
nhưng số vertex cần xóa chỉ k=10
```

thì exponential theo `k` có thể tốt hơn exponential theo `n`.

## Parameter đúng quan trọng hơn label NP-hard

Một problem NP-hard theo `n` vẫn có thể dễ khi parameter thực tế nhỏ.

Các parameter thường có ý nghĩa:

```text
solution size
number of conflicts
treewidth
number of machines
number of colors
edit distance
feedback vertex count
```

Engineering question nên là:

> Hardness nằm ở chiều nào của instance, và chiều đó trong dữ liệu thật có nhỏ không?

## Kernelization

Kernelization là preprocessing polynomial-time biến `(instance,k)` thành một instance nhỏ hơn có kích thước bị chặn theo hàm của `k`, đồng thời bảo toàn đáp án.

Mục tiêu là loại bỏ phần dữ liệu chắc chắn không ảnh hưởng bản chất combinatorial khó.

Có thể xem kernelization như **problem reduction theo parameter** trước khi chạy exact search đắt tiền.

## Treewidth: graph gần cây có thể dễ hơn

Nhiều bài NP-hard trên general graph trở nên dễ hơn trên tree hoặc graph có treewidth nhỏ.

Tree decomposition cho phép DP trên các “bag” kích thước nhỏ, với exponential factor phụ thuộc treewidth thay vì toàn bộ số đỉnh.

Trực giác:

> Nếu graph có thể được ghép từ các phần nhỏ liên kết với nhau qua boundary nhỏ, ta có thể giữ state chỉ trên boundary đó.

Đây là một ví dụ sâu về việc structure của instance quan trọng hơn tên bài toán tổng quát.

## Approximation algorithm

Khi exact optimum quá đắt, có thể chấp nhận solution gần optimum với guarantee định lượng.

Với minimization, một `ρ`-approximation thường bảo đảm:

\[
ALG(I)\le \rho\cdot OPT(I)
\]

Với maximization, convention được viết theo hướng phù hợp để đảm bảo giá trị không quá xa optimum.

Điểm quan trọng là approximation algorithm có **guarantee trên mọi instance thuộc mô hình**, khác với heuristic chỉ “thường chạy tốt”.

## Vertex Cover 2-approximation

Một thuật toán đơn giản:

```text
while còn cạnh chưa cover:
    chọn một cạnh (u,v)
    đưa cả u và v vào cover
    xóa mọi cạnh incident với u hoặc v
```

Các cạnh được chọn tạo một matching. Mọi vertex cover tối ưu phải lấy ít nhất một endpoint của mỗi cạnh matching, nên nếu matching có `k` cạnh thì optimum ít nhất `k` đỉnh.

Algorithm lấy `2k` đỉnh, nên kích thước không quá `2*OPT`.

Ví dụ này cho thấy approximation proof thường cần một **lower bound lên optimum** để so solution của algorithm.

## Set Cover và greedy

Greedy Set Cover liên tục chọn tập cover nhiều phần tử chưa được cover nhất trên mỗi đơn vị chi phí theo variant phù hợp.

Nó có logarithmic approximation guarantee trong mô hình chuẩn.

Điểm cần học không phải chỉ công thức guarantee, mà là kỹ thuật proof: mỗi bước phân bổ “giá” cho các phần tử mới được cover và so tổng charge với optimum.

## Metric TSP và vai trò của triangle inequality

General TSP rất khó approximation tốt, nhưng **metric TSP** có thêm triangle inequality:

\[
d(a,c)\le d(a,b)+d(b,c)
\]

Cấu trúc này cho phép dùng MST như lower bound và xây các approximation có guarantee hằng số.

Một restriction toán học nhỏ có thể thay approximation landscape rất mạnh.

## PTAS và FPTAS

**PTAS**: với mọi `ε>0` cố định, có algorithm polynomial theo `n` cho solution trong factor `(1+ε)` thích hợp, nhưng exponent theo `n` có thể phụ thuộc `1/ε`.

**FPTAS** mạnh hơn: runtime polynomial cả theo `n` và `1/ε`.

Knapsack có FPTAS nổi tiếng dựa trên scaling DP values.

Tư duy engineering: `ε` là một knob đổi runtime lấy chất lượng solution.

## Approximation khác heuristic

**Approximation algorithm** có worst-case quality guarantee.

**Heuristic** có thể rất tốt thực tế nhưng không có guarantee tương tự.

Ví dụ heuristic:

```text
local search
simulated annealing
genetic algorithm
greedy without proof
problem-specific neighborhood search
```

Không nên coi heuristic là “sai”. Chỉ cần gọi đúng bản chất guarantee của nó.

## Local Search

Bắt đầu từ một solution hợp lệ, liên tục chuyển sang solution hàng xóm tốt hơn.

Câu hỏi thiết kế:

```text
neighborhood là gì?
move cost tính nhanh thế nào?
local optimum có tệ không?
làm sao thoát local optimum?
```

2-opt cho TSP là ví dụ kinh điển: thay hai cạnh bằng hai cạnh khác nếu tour ngắn hơn.

Local search thường rất mạnh khi cần good solution nhanh trên instance lớn.

## Randomized heuristic

Random restart hoặc randomized neighborhood giúp tránh bị kẹt cùng local optimum.

Khi dùng randomness, nên đo distribution của solution quality và runtime thay vì chỉ báo một lần chạy tốt.

Trong production, reproducibility có thể cần seed được quản lý rõ.

## ILP/MILP

Nhiều bài optimization có thể encode bằng biến và ràng buộc tuyến tính nguyên.

Ví dụ chọn item:

```text
x_i ∈ {0,1}
```

với objective và constraints tuyến tính.

MILP solver dùng LP relaxation, cutting planes, branch-and-bound/branch-and-cut và nhiều heuristic.

Lợi thế engineering:

```text
mô hình hóa nhanh
solver trưởng thành
có bound và optimality gap
xử lý nhiều constraint business phức tạp
```

Nhược điểm là performance khó dự đoán theo worst-case và cần solver/tooling phù hợp.

## SAT, SMT và CP-SAT

SAT phù hợp Boolean logic. SMT thêm theory như integer arithmetic, bit-vectors hoặc arrays. Constraint Programming/CP-SAT phù hợp scheduling và combinatorial constraints với propagation mạnh.

Thay vì tự viết backtracking khổng lồ, đôi khi encoding problem vào solver là cách engineering tốt hơn.

Câu hỏi là model nào diễn đạt constraint tự nhiên nhất.

## Solver không loại bỏ nhu cầu mô hình hóa

Một model solver tệ vẫn có thể chạy rất chậm.

Các quyết định quan trọng:

```text
biến nào thực sự cần?
constraint nào redundant nhưng giúp propagation?
symmetry có thể phá bớt không?
bound ban đầu có tốt không?
miền biến có thể thu hẹp trước không?
```

Hardness không biến mất khi dùng solver; solver cung cấp một bộ search/pruning engine rất mạnh.

## Symmetry breaking

Nếu nhiều assignment khác nhau thực chất biểu diễn cùng một solution, solver có thể tốn thời gian khám phá các bản sao đối xứng.

Ví dụ gán màu cho graph: hoán đổi tên màu có thể tạo solution logic giống nhau.

Thêm constraint cố định một số lựa chọn đại diện có thể giảm search mà không mất solution thực sự khác biệt.

Đây là một dạng state-space reduction.

## Lower bound, upper bound và optimality gap

Trong minimization:

```text
upper bound = chi phí solution khả thi đã tìm được
lower bound = cận dưới chứng minh optimum không thể thấp hơn
```

Nếu hai bound gặp nhau, optimum được chứng minh.

Nếu chưa gặp, gap cho biết mức độ chưa chắc chắn.

Solver optimization hiện đại thường báo cả incumbent solution và best bound; đây là thông tin rất hữu ích để quyết định dừng sớm.

## Anytime algorithm

Một **anytime algorithm** có thể trả solution hiện tại bất cứ lúc nào và cải thiện dần nếu được cho thêm thời gian.

Branch-and-bound, local search và nhiều solver có thể dùng theo cách này.

Trong hệ thống deadline-driven, đôi khi “solution tốt trong 2 giây” có giá trị hơn “optimum sau thời gian không biết trước”.

Đây là trade-off trực tiếp giữa quality và compute budget.

## Khi nào nên bỏ exactness?

Một quy trình thực dụng:

```text
1. Xác định exactness có thật sự là requirement không.
2. Tìm special case polynomial.
3. Tìm parameter nhỏ cho FPT/exponential method.
4. Ước lượng state-space và memory.
5. Thử exact solver nếu instance vừa phải.
6. Nếu quá lớn, tìm approximation guarantee phù hợp.
7. Nếu guarantee vẫn quá đắt, dùng heuristic và đo quality thực tế.
```

Không nên nhảy thẳng sang heuristic chỉ vì thấy từ “NP-hard”.

## Khi nào nên dùng brute force?

Brute force đúng khi:

```text
input rất nhỏ
cần oracle để test algorithm tối ưu hơn
chỉ chạy offline một lần
search space thực tế bị constraint thu nhỏ
implementation đơn giản quan trọng hơn runtime
```

Một brute-force solver nhỏ, rõ và đúng còn là reference model rất tốt cho differential testing.

## Hardness và product requirements

Một product có thể thay specification để làm bài dễ hơn.

Ví dụ:

```text
exact optimal route -> route <= 5% so với optimum
solve 1 triệu item -> solve theo từng region
arbitrary graph -> graph được giới hạn gần tree
real-time answer -> offline preprocessing
```

Thay requirement không phải “né thuật toán”; đôi khi đó là cách duy nhất biến một optimization không khả thi thành hệ thống có SLA rõ.

## Một workflow nhận diện bài khó

Khi gặp combinatorial problem, có thể hỏi:

```text
Có đang chọn subset/permutation/partition không?
Có constraint pairwise hoặc global khiến greedy khó không?
State space là 2^n, n!, k^n hay gì khác?
Có special case graph/tree/interval không?
Numeric parameter có nhỏ không?
Có thể reduce về flow/matching/2-SAT không?
Có parameter k nhỏ cho FPT không?
Có approximation guarantee đã biết theo structure không?
Solver SAT/ILP/CP có phù hợp không?
```

Mục tiêu là nhận ra cấu trúc trước khi lao vào micro-optimization.

## Những hiểu lầm phổ biến

“NP nghĩa là non-polynomial” — sai.

“NP-complete nghĩa là không giải được” — sai; nhiều instance cụ thể giải rất tốt.

“Bài NP-hard thì DP polynomial không thể tồn tại” — pseudo-polynomial hoặc special-case DP vẫn có thể tồn tại.

“Reduction B -> SAT chứng minh SAT hard” — sai direction; nó cho thấy SAT có thể giải B nếu encoding đúng.

“Approximation là heuristic” — không nhất thiết; approximation algorithm có guarantee định lượng.

“Solver tự động giải quyết modeling” — sai; model quality ảnh hưởng search cực mạnh.

“Exponential algorithm luôn tệ” — sai nếu parameter nhỏ hoặc exactness bắt buộc.

## Mô hình tư duy

> Khi một bài toán khó, đừng chỉ hỏi “thuật toán nào nhanh hơn?”. Hãy hỏi **hardness nằm ở dimension nào, structure nào của instance làm bài dễ hơn, exactness có thật sự cần không, và ta có thể đổi thời gian–bộ nhớ–độ chính xác như thế nào?**

Reduction giúp đổi góc nhìn. Parameterization đổi biến mà exponential phụ thuộc. Approximation đổi exactness lấy guarantee. Solver đổi công sức implementation lấy một search engine trưởng thành. Heuristic đổi guarantee lấy tốc độ thực tế.

Đó là toolbox đầy đủ hơn cho những bài toán mà “chọn đúng data structure” vẫn chưa đủ.

Xem tiếp: [Recursion & Backtracking](./02_recursion_and_backtracking.md), [Dynamic Programming](./05_dynamic_programming.md), [Greedy Algorithms](./04_greedy_algorithms.md), [Graph Algorithms](../03_graphs/_index.md), [Probabilistic Thinking](../05_specialized/03_amortized_randomized_and_probabilistic_thinking.md) và [Problem Modeling](../00_foundations/00_dsa_as_problem_modeling.md).