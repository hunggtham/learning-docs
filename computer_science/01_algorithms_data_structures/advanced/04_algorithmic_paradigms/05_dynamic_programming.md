# quy hoạch động (dynamic programming)
**Quy hoạch động (Dynamic Programming, DP / 동적 계획법)**

quy hoạch động không phải một bộ công thức `dp[i][j]`. Bản chất của DP là **trạng thái (state) compression + reuse**: nếu nhiều histories khác nhau dẫn đến cùng một trạng thái mà từ trạng thái đó tương lai hành vi giống nhau, ta chỉ cần giải trạng thái một lần rồi tái sử dụng kết quả.

Một cách nói chặt hơn:

> trạng thái DP đại diện cho một **equivalence class của histories**. Những quá khứ khác nhau được gom thành cùng trạng thái vì mọi quyết định tương lai chỉ cần một dữ liệu tóm lược nhỏ của quá khứ.

Đây là mental mô hình quan trọng hơn việc học thuộc công thức truy hồi.

## Từ recursion tới DP

Hãy bắt đầu bằng recursive problem definition tự nhiên.

Fibonacci naive:

```text
F(n) = F(n-1) + F(n-2)
```

tạo cây lời gọi với nhiều lần tính lại `F(k)`. Nếu bộ nhớ đệm theo `n`, mỗi trạng thái chỉ tính một lần.

```java
long fib(int n, long[] memo) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    return memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
}
```

Nhưng Fibonacci quá đơn giản. Phần khó thật của DP là trả lời:

```text
state cần lưu information gì để future được xác định?
```

## Optimal substructure và overlapping subproblems

Hai concepts thường xuất hiện cùng nhau nhưng không giống nhau.

**Optimal substructure**: lời giải tối ưu của problem lớn có thể xây từ optimal các lời giải của subproblems phù hợp.

**Overlapping subproblems**: cùng subproblem/trạng thái xuất hiện lặp lại từ nhiều histories.

DP đặc biệt hữu ích khi cả hai cùng có mặt.

Nếu subproblems độc lập không overlap nhiều, divide-and-conquer có thể phù hợp hơn.

## trạng thái design: tương lai cần biết gì?

0/1 Knapsack có trạng thái phổ biến:

```text
dp[i][w] = giá trị tối đa khi xét first i items và capacity w
```

Tại sao full lịch sử items đã chọn không cần giữ? Vì tương lai chỉ quan tâm:

```text
đã đi tới index nào
capacity còn/đã dùng bao nhiêu
```

Hai histories khác nhau nhưng có cùng `(i,w)` là future-equivalent.

Đây là một cách thiết kế trạng thái có hệ thống: **xóa mọi thông tin của quá khứ không ảnh hưởng tương lai choices**.

## trạng thái quá nhỏ và trạng thái quá lớn

trạng thái quá nhỏ → merge những histories thực ra có tương lai khác nhau → answer sai.

trạng thái quá lớn → đúng nhưng không gian trạng thái explosion, bộ nhớ/time lãng phí.

Ví dụ grid có các khóa/doors:

```text
(row,col)
```

có thể quá nhỏ; cần `(row,col,keysMask)`.

Ngược lại lưu toàn bộ đường đi tới cell là quá lớn nếu tương lai chỉ cần khóa set.

trạng thái design của DP và visited-trạng thái design của đồ thị search là cùng một problem.

## Transition từ “hành động cuối”

Một technique rất mạnh là phân loại lời giải tối ưu theo **last action**.

Edit khoảng cách:

```text
dp[i][j] = minimum edits biến A[0..i) thành B[0..j)
```

thao tác cuối chỉ có thể là:

```text
insert B[j-1]
delete A[i-1]
replace/match A[i-1] với B[j-1]
```

Từ đó công thức truy hồi xuất hiện tự nhiên.

Nếu chars bằng:

\[
dp[i][j] = dp[i-1][j-1]
\]

Nếu khác:

\[
dp[i][j] = 1 + \min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
\]

Đây là “derive công thức truy hồi”, không phải memorize công thức truy hồi.

## Top-down và bottom-up

**Top-down / memoization**:

```text
viết recursion tự nhiên
cache state đã giải
chỉ tính states reachable
```

**Bottom-up / tabulation**:

```text
xác định dependency order
fill table theo thứ tự đó
không cần recursion stack
```

Không có phương án nào luôn tốt hơn.

Sparse có thể tới không gian trạng thái có thể hợp top-down. Dense regular table thường hợp bottom-up và tính cục bộ bộ nhớ đệm tốt hơn.

## DP như DAG

Xem mỗi trạng thái là đỉnh, mỗi dependency là directed cạnh.

Nếu trạng thái `A` phụ thuộc trạng thái `B`, có cạnh:

```text
B -> A
```

DP computation đồ thị phải acyclic theo dimension/order phù hợp. Bottom-up chỉ đơn giản là evaluate các trạng thái theo một thứ tự tô-pô.

Mental connection:

```text
DP table
≈ DAG of states
≈ reuse repeated subproblems
```

Điều này giúp chuyển đổi giữa đồ thị đường đi ngắn nhất (shortest path) và DP.

## Fibonacci space optimization

Nếu transition chỉ cần hai các trạng thái trước:

```text
F(i) depends on F(i-1), F(i-2)
```

không cần mảng `O(n)`; chỉ giữ rolling variables `O(1)`.

Space optimization xuất phát từ dependency width, không phải trick riêng.

## 0/1 Knapsack và loop direction

2D công thức truy hồi:

\[
dp[i][w]=\max(dp[i-1][w], dp[i-1][w-weight_i]+value_i)
\]

Nếu compress thành 1D:

```java
for (Item item : items) {
    for (int w = capacity; w >= item.weight; --w) {
        dp[w] = Math.max(dp[w], dp[w - item.weight] + item.value);
    }
}
```

Capacity phải iterate giảm. Nếu đi tăng, `dp[w-item.weight]` có thể đã dùng chính item hiện tại và ta vô tình đổi bài thành unbounded knapsack.

Loop direction là part của mathematical ngữ nghĩa (semantics).

## Unbounded knapsack

Nếu mỗi item được dùng unlimited times, capacity loop tăng là đúng:

```text
for item:
    for w = weight .. capacity:
        dp[w] = max(dp[w], dp[w-weight] + value)
```

Hai problems khác nhau chỉ bởi reuse chính sách, nhưng cách triển khai order phản ánh difference đó.

## Coin Change và ngữ nghĩa của “cách”

Có nhiều bài coin change:

```text
có tạo được amount không?
ít coin nhất?
số combinations?
số permutations/orderings?
```

Cùng trạng thái dimension có thể cho giá trị ngữ nghĩa khác.

Đếm combinations thường dùng coins vòng lặp bên ngoài:

```text
for coin:
    for amount increasing:
        ways[x] += ways[x-coin]
```

Nếu amount outer, coin inner, ta có thể đếm ordered sequences.

Loop order chính là cách ta định nghĩa combinatorial đối tượng được đếm.

## Longest Phổ biến Subsequence

trạng thái:

```text
dp[i][j] = LCS length của A[0..i) và B[0..j)
```

Nếu last chars bằng nhau:

\[
dp[i][j]=dp[i-1][j-1]+1
\]

Nếu khác:

\[
dp[i][j]=\max(dp[i-1][j],dp[i][j-1])
\]

trực giác chứng minh: nếu chars cuối khác nhau, một LCS optimal không thể cần dùng cả hai chars đó cùng vị trí matching; ít nhất một bên bị bỏ, nên hai subproblems cover possibilities.

## LCS reconstruction

Bảng giá trị chỉ trả về độ dài. Muốn khôi phục dãy con thực tế, cần lần ngược lại các lựa chọn:

```text
nếu chars equal -> take char, move diagonal
else move về neighbor có dp lớn hơn
```

Nếu đã compress bộ nhớ xuống hai rows, reconstruction khó hơn vì lịch sử bị bỏ. Đây là sự đánh đổi (trade-off) giữa bộ nhớ và thông tin retention.

## Longest Increasing Subsequence

Kinh điển DP:

\[
dp[i]=1+\max(dp[j]) \quad j<i, a[j]<a[i]
\]

Time `O(n^2)`.

thuật toán `O(n log n)` giữ:

```text
tails[len] = smallest possible tail của increasing subsequence length len+1
```

Mỗi giá trị binary-search vị trí trong `tails`.

`tails` không nhất thiết là actual LIS ở mọi thời điểm; nó là **compressed frontier** của possibilities. Đây là một ví dụ sâu về trạng thái compression vượt khỏi table DP truyền thống.

## Grid DP

Grid đường đi problems thường có natural dependency:

```text
dp[r][c] depends on top/left/diagonal
```

Nếu movement chỉ đi xuống/phải, đồ thị trạng thái là DAG theo row+column order.

Nếu movement cho phép chu trình, naive grid DP không còn trực tiếp; có thể cần đồ thị đường đi ngắn nhất hoặc detect another monotonic dimension.

## Interval DP

Interval DP dùng trạng thái:

```text
dp[l][r] = answer cho subarray/subsequence interval [l,r]
```

Transitions thường split interval tại `k` hoặc quyết định endpoints.

Examples:

```text
matrix-chain multiplication
optimal BST
burst balloons
palindrome interval problems
```

Thứ tự tính từ dưới lên thường đi theo độ dài khoảng tăng dần:

```text
for len = 1..n:
    for l:
        r = l + len - 1
```

Vì smaller intervals phải có trước larger intervals.

## Matrix Chain Multiplication

Dimensions `p0,p1,...,pn`. trạng thái:

```text
dp[i][j] = minimum scalar multiplications để nhân matrices i..j
```

Try last split `k`:

\[
dp[i][j] = \min_k dp[i][k] + dp[k+1][j] + p_{i-1}p_kp_j
\]

Đây là classic “choose partition point” interval DP.

## cây DP

Fix nút cha để nút con các cây con độc lập.

Maximum independent set:

```text
dp[u][0] = best nếu không chọn u
dp[u][1] = best nếu chọn u
```

Nếu chọn `u`, các nút con không được chọn.

Nếu không chọn `u`, mỗi nút con chọn tốt nhất giữa two các trạng thái.

cây DP mạnh vì cây itself cung cấp acyclic dependency structure.

## Rerooting DP

Nếu cần answer cho mọi nút khi coi nút đó là nút gốc, tính lại từ đầu là `O(n^2)`.

Rerooting reuse:

```text
child contribution
+ contribution từ phần ngoài child subtree
```

Pass 1 bottom-up, pass 2 top-down.

Đây là message-passing DP trên cây.

## Bitmask DP

Nếu `n` nhỏ, subset có thể encode bằng bitmask.

Travelling Salesman DP:

```text
dp[mask][u] = minimum cost visit set mask và kết thúc tại u
```

Transition add new đỉnh.

Số trạng thái có thể là `O(2^n n)`. Bitmask không làm biến mất độ phức tạp hàm mũ; nó tổ chức không gian tìm kiếm hàm mũ để tái sử dụng các trạng thái chồng lặp.

## Subset DP và SOS DP

Nếu cần tổng hợp trên mọi mặt nạ con hoặc mặt nạ bao, Sum Over Subsets DP (SOS DP) có thể biến các vòng lặp đơn giản `O(3^n)` thành khoảng `O(n2^n)`.

Đây là quy hoạch động trên lattice của subsets.

## Digit DP

Digit DP đếm numbers thỏa ràng buộc trong range bằng trạng thái như:

```text
position
tight?        // prefix có đang bằng bound không
started?      // đã bắt đầu số chưa
additional property: sum/mod/count/etc
```

trạng thái `tight` là ví dụ rõ về future-relevant thông tin: nếu prefix đã nhỏ hơn cận trên (upper bound), tương lai digits không còn bị bound digit hiện tại giới hạn.

## Profile DP

Các bài toán lát bảng hoặc bài toán theo biên có thể mã hóa trạng thái của một “biên” nhỏ bằng bitmask rồi quét qua từng hàng hoặc cột.

Thay vì lưu trạng thái của toàn bộ bảng với kích thước hàm mũ, ta chỉ giữ phần biên cục bộ còn ảnh hưởng đến các bước tiếp theo.

Đây là một form sophisticated của trạng thái compression.

## DP on DAG

Nếu đồ thị là DAG, shortest/longest đường đi có thể giải bằng thứ tự tô-pô.

trạng thái:

```text
dp[v] = best value tới v
```

Relax outgoing các cạnh một lần theo topo order.

Negative cạnh vẫn okay vì không có chu trình.

Đây là bridge trực tiếp giữa các thuật toán đồ thị và DP.

## đường đi ngắn nhất và DP khác nhau ở đâu?

Bellman-Ford có thể được nhìn như lặp lại relaxation DP theo số các cạnh used:

```text
dp[k][v] = shortest path tới v dùng <= k edges
```

Nhưng các thuật toán đồ thị thường khai thác structure/frontier để tránh explicit dimension.

Nhiều distinctions giữa “DP” và “thuật toán đồ thị” là cách triển khai/structure emphasis hơn là mathematical wall.

## DP với monotone queue

Một transition dạng:

\[
dp[i]=\min_{j \in window(i)}(dp[j]+cost)
\]

có thể được optimize bằng deque nếu ứng viên giá trị có monotonic structure.

DP optimization thường là tìm cách tăng tốc transition, không chỉ giảm number các trạng thái.

## Prefix minima/maxima optimization

Nếu transition cần:

```text
min(dp[0..i-1])
```

đừng quét lại mỗi trạng thái; giữ prefix minimum.

Đây là reuse ở tầng transition computation.

## Divide-and-conquer optimization

Một số DP dạng partition:

\[
dp[k][i] = \min_{j<i}(dp[k-1][j]+C(j,i))
\]

có monotonic optimal split các tính chất cho phép divide-and-conquer optimization.

Điều kiện chứng minh không trivial; không áp dụng chỉ vì công thức truy hồi “trông giống”. Nhưng nó cho thấy advanced DP thường dựa vào structure của argmin/transition matrix.

## Knuth optimization

Một số interval DP thỏa quadrangle inequality/monotonicity có thể giảm cubic xuống quadratic.

Không cần học thuộc mọi theorem ngay, nhưng mental mô hình là:

> Sau khi thiết kế đúng trạng thái/transition, bước tiếp theo là khai thác additional structure để giảm transition search.

## Convex Hull Trick

DP transition dạng tuyến tính:

\[
dp[i] = \min_j(m_j x_i + b_j)
\]

có thể được tối ưu bằng cấu trúc dữ liệu giữ lines và truy vấn min/max.

Li Chao Tree hoặc Convex Hull Trick biến bước “duyệt mọi j” thành một truy vấn hình học.

Đây là nơi DP kết nối với computational geometry/các cấu trúc dữ liệu.

## xác suất DP

trạng thái giá trị không nhất thiết min/max/count; có thể là xác suất/kỳ vọng giá trị.

kỳ vọng steps thường dùng law of total expectation:

\[
E[s] = 1 + \sum_t P(s\to t)E[t]
\]

Nhưng nếu transitions chu trình, equations có thể không có đơn giản topological DP; đôi khi cần solve linear các hệ thống hoặc transform các trạng thái.

## DP modulo arithmetic

Combinatorial count có thể rất lớn. Problems thường yêu cầu mod `M`.

Cần chú ý tràn số trước modulo trong C/Java, và Number an toàn range trong JavaScript.

Modulo changes numeric cách biểu diễn (representation), không thay combinatorial công thức truy hồi.

## Infinity giá trị canh gác (sentinel) và tràn số

Minimum DP thường initialize `INF`.

Đừng dùng maximum integer rồi cộng chi phí:

```text
INF + cost -> overflow
```

Use sufficiently an toàn giá trị canh gác (sentinel) hoặc guard:

```java
if (dp[prev] < INF) {
    dp[cur] = Math.min(dp[cur], dp[prev] + cost);
}
```

## Memo khóa design

Top-down DP với compound trạng thái cần canonical khóa.

Java có thể dùng các mảng indexed dimensions hoặc bất biến sau khi tạo record.

JavaScript `Map` đối tượng các khóa dùng identity, nên `{i:1,j:2}` mới mỗi lần không match trước đó đối tượng. Cần encode khóa string/int hoặc nested maps.

C phải quản bảng băm (Hash Table)/mảng quyền sở hữu (ownership) rõ.

## Sparse trạng thái DP

Nếu theoretical không gian trạng thái rất lớn nhưng có thể tới các trạng thái ít, hash-map memoization có thể tốt hơn dense mảng.

Examples:

```text
DP theo large coordinate values
state machine với many impossible combinations
search + memo hybrid
```

sự đánh đổi: hash overhead vs skipping unreachable các trạng thái.

## DP và bộ nhớ tính cục bộ (locality)

2D `dp[i][j]` theo thứ tự hàng traversal thường thân thiện với bộ nhớ đệm nếu vòng lặp bên trong đi contiguous.

Changing loop order có thể ảnh hưởng môi trường chạy (runtime) rất mạnh dù Big-O giống nhau.

Rolling mảng vừa giảm bộ nhớ vừa cải thiện bộ nhớ đệm, nhưng có thể làm reconstruction khó hơn.

## Reconstruction strategies

Có ba cách phổ biến:

```text
1. store parent/choice trực tiếp
2. backtrack bằng cách so dp values
3. recompute một phần nếu memory optimized
```

Store choices tăng bộ nhớ nhưng đơn giản.

Recomputation tiết kiệm bộ nhớ nhưng tăng CPU.

Design phụ thuộc đầu ra yêu cầu.

## Counting vs optimizing

Một công thức truy hồi có thể cần:

```text
best value
number of best ways
lexicographically smallest optimal solution
```

Nếu tie ngữ nghĩa quan trọng, trạng thái giá trị có thể phải lưu tuple hoặc extra siêu dữ liệu.

“DP đúng giá trị” chưa chắc đủ cho requested đầu ra.

## trạng thái explosion

Nếu trạng thái dimensions:

```text
n * capacity * mask * last * flag
```

product có thể quá lớn.

Trước khi code, estimate:

```text
#states * transition cost * bytes/state
```

DP feasibility là engineering calculation, không chỉ asymptotic label.

## Meet-in-the-middle vs DP

Subset problems với `n≈40` có thể quá lớn cho `2^n`, nhưng split thành hai halves khoảng `2^(n/2)` rồi kết hợp có thể hiệu quả.

Nếu numeric sum dimension nhỏ, giả đa thức DP có thể tốt hơn.

thuật toán choice phụ thuộc both `n` và giá trị ranges.

## giả đa thức complexity

Knapsack `O(nW)` là đa thức theo giá trị số `W`, nhưng không phải đa thức theo độ dài biểu diễn đầu vào `log W`.

Đây gọi là giả đa thức.

Hiểu distinction này quan trọng khi nối DSA với computational complexity.

## DP vs Greedy

Greedy giữ một frontier nhỏ vì prove cục bộ choice an toàn.

DP giữ nhiều các trạng thái vì chưa thể loại alternatives sớm.

Nếu tìm được dominance/exchange tính chất mạnh, một DP có thể collapse thành greedy.

Ngược lại nếu lựa chọn tham lam có regret, DP giữ competing possibilities.

## Dominance pruning

Trong một số bài quy hoạch động hoặc tìm kiếm, trạng thái A lấn át B nếu A không tệ hơn B trên mọi chiều còn ảnh hưởng tới tương lai.

Ta có thể discard dominated các trạng thái.

Ví dụ resource-constrained đường đi giữ Pareto frontier giữa chi phí/time. Đây là trạng thái pruning thay vì chính xác khóa equality reuse.

## DP tính đúng đắn chứng minh template

Một chứng minh tốt thường gồm:

```text
1. định nghĩa state chính xác
2. chứng minh base cases
3. chứng minh transition cover mọi valid solution
4. chứng minh không bỏ candidate optimal
5. chứng minh evaluation order thỏa dependencies
```

Nếu optimization space, còn phải chứng minh overwrite order không làm dùng trạng thái mới sai ngữ nghĩa.

## kiểm thử DP

Brute force trên small n là oracle rất mạnh.

Workflow:

```text
generate random small instance
solve brute-force exhaustive
solve DP
compare
```

Đây là cách bắt trạng thái/loop-order bugs tốt hơn nhiều examples thủ công.

## Những hiểu lầm phổ biến

“Có recursion là DP” — sai. DP cần lặp lại equivalent các trạng thái hoặc structured đồ thị trạng thái đáng reuse.

“Có `dp[]` mảng là DP” — naming không quan trọng; trạng thái ngữ nghĩa mới quan trọng.

“Bottom-up luôn nhanh hơn” — sparse các trạng thái có thể hợp memoization.

“Space optimization luôn tốt” — có thể mất reconstruction/debuggability.

“DP complexity = số các trạng thái” — còn phải nhân transition chi phí.

“Thứ tự vòng lặp chỉ là chi tiết triển khai” — sai; trong nhiều bài quy hoạch động, thứ tự vòng lặp quyết định ngữ nghĩa tái sử dụng trạng thái và cả tính đúng đắn.

## Một workflow thiết kế DP có thể tái sử dụng

Khi gặp problem:

```text
1. Viết brute-force recursion tự nhiên.
2. Xác định arguments nào quyết định future -> đó là candidate state.
3. Tìm repeated states.
4. Định nghĩa chính xác dp[state] nghĩa gì.
5. Derive transition từ last/first decision.
6. Xác định base cases.
7. Estimate #states và cost/transition.
8. Chọn top-down hay bottom-up.
9. Nếu cần, optimize memory/transition.
10. Thiết kế reconstruction và test với brute force.
```

Nếu bước 4 không thể nói bằng một câu rõ ràng, code DP thường rất dễ sai.

## Mô hình tư duy

> DP là nghệ thuật tìm **dữ liệu tóm lược nhỏ nhất của quá khứ mà tương lai cần biết**. Khi dữ liệu tóm lược đúng, nhiều histories collapse thành một trạng thái; khi trạng thái được reuse, exponential search có thể biến thành polynomial hoặc giả đa thức computation. Sau đó optimization nâng cao tập trung vào giảm số các trạng thái, giảm transition chi phí hoặc giảm bộ nhớ.

Câu hỏi cốt lõi luôn là:

```text
Hai histories nào có future giống nhau?
State tối thiểu để phân biệt future là gì?
Transition cover mọi possibility chưa?
Dependency graph có order nào?
Có dominance/monotonicity/convexity để optimize không?
```

Xem thêm: [Recursion & Backtracking](./02_recursion_and_backtracking.md), [Greedy](./04_greedy_algorithms.md), [DAG/SCC](../03_graphs/04_dag_topological_sort_and_scc.md), [Bit Manipulation](../05_specialized/02_bit_manipulation_and_bitsets.md).