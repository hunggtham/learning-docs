# Dynamic Programming
**Quy hoạch động (Dynamic Programming, DP / 동적 계획법)**

Dynamic Programming không phải một bộ công thức `dp[i][j]`. Bản chất của DP là **state compression + reuse**: nếu nhiều histories khác nhau dẫn đến cùng một state mà từ state đó future behavior giống nhau, ta chỉ cần giải state một lần rồi tái sử dụng kết quả.

Một cách nói chặt hơn:

> State DP đại diện cho một **equivalence class của histories**. Những quá khứ khác nhau được gom thành cùng state vì mọi quyết định tương lai chỉ cần một summary nhỏ của quá khứ.

Đây là mental model quan trọng hơn việc học thuộc recurrence.

## Từ recursion tới DP

Hãy bắt đầu bằng recursive problem definition tự nhiên.

Fibonacci naive:

```text
F(n) = F(n-1) + F(n-2)
```

tạo call tree với nhiều lần tính lại `F(k)`. Nếu cache theo `n`, mỗi state chỉ tính một lần.

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

**Optimal substructure**: optimal solution của problem lớn có thể xây từ optimal solutions của subproblems phù hợp.

**Overlapping subproblems**: cùng subproblem/state xuất hiện lặp lại từ nhiều histories.

DP đặc biệt hữu ích khi cả hai cùng có mặt.

Nếu subproblems độc lập không overlap nhiều, divide-and-conquer có thể phù hợp hơn.

## State design: future cần biết gì?

0/1 Knapsack có state phổ biến:

```text
dp[i][w] = giá trị tối đa khi xét first i items và capacity w
```

Tại sao full history items đã chọn không cần giữ? Vì future chỉ quan tâm:

```text
đã đi tới index nào
capacity còn/đã dùng bao nhiêu
```

Hai histories khác nhau nhưng có cùng `(i,w)` là future-equivalent.

Đây là một cách thiết kế state có hệ thống: **xóa mọi information của quá khứ không ảnh hưởng future choices**.

## State quá nhỏ và state quá lớn

State quá nhỏ → merge những histories thực ra có future khác nhau → answer sai.

State quá lớn → đúng nhưng state space explosion, memory/time lãng phí.

Ví dụ grid có keys/doors:

```text
(row,col)
```

có thể quá nhỏ; cần `(row,col,keysMask)`.

Ngược lại lưu toàn bộ path tới cell là quá lớn nếu future chỉ cần key set.

State design của DP và visited-state design của graph search là cùng một problem.

## Transition từ “hành động cuối”

Một technique rất mạnh là phân loại optimal solution theo **last action**.

Edit distance:

```text
dp[i][j] = minimum edits biến A[0..i) thành B[0..j)
```

Operation cuối chỉ có thể là:

```text
insert B[j-1]
delete A[i-1]
replace/match A[i-1] với B[j-1]
```

Từ đó recurrence xuất hiện tự nhiên.

Nếu chars bằng:

\[
dp[i][j] = dp[i-1][j-1]
\]

Nếu khác:

\[
dp[i][j] = 1 + \min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
\]

Đây là “derive recurrence”, không phải memorize recurrence.

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

Sparse reachable state space có thể hợp top-down. Dense regular table thường hợp bottom-up và cache locality tốt hơn.

## DP như DAG

Xem mỗi state là vertex, mỗi dependency là directed edge.

Nếu state `A` phụ thuộc state `B`, có edge:

```text
B -> A
```

DP computation graph phải acyclic theo dimension/order phù hợp. Bottom-up chỉ đơn giản là evaluate states theo một topological order.

Mental connection:

```text
DP table
≈ DAG of states
≈ reuse repeated subproblems
```

Điều này giúp chuyển đổi giữa graph shortest path và DP.

## Fibonacci space optimization

Nếu transition chỉ cần hai states trước:

```text
F(i) depends on F(i-1), F(i-2)
```

không cần array `O(n)`; chỉ giữ rolling variables `O(1)`.

Space optimization xuất phát từ dependency width, không phải trick riêng.

## 0/1 Knapsack và loop direction

2D recurrence:

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

Loop direction là part của mathematical semantics.

## Unbounded knapsack

Nếu mỗi item được dùng unlimited times, capacity loop tăng là đúng:

```text
for item:
    for w = weight .. capacity:
        dp[w] = max(dp[w], dp[w-weight] + value)
```

Hai problems khác nhau chỉ bởi reuse policy, nhưng implementation order phản ánh difference đó.

## Coin Change và semantics của “cách”

Có nhiều bài coin change:

```text
có tạo được amount không?
ít coin nhất?
số combinations?
số permutations/orderings?
```

Cùng state dimension có thể cho value semantics khác.

Đếm combinations thường dùng coins outer loop:

```text
for coin:
    for amount increasing:
        ways[x] += ways[x-coin]
```

Nếu amount outer, coin inner, ta có thể đếm ordered sequences.

Loop order chính là cách ta định nghĩa combinatorial object được đếm.

## Longest Common Subsequence

State:

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

Proof intuition: nếu chars cuối khác nhau, một LCS optimal không thể cần dùng cả hai chars đó cùng vị trí matching; ít nhất một bên bị bỏ, nên hai subproblems cover possibilities.

## LCS reconstruction

Value table chỉ trả length. Muốn actual subsequence, backtrack:

```text
nếu chars equal -> take char, move diagonal
else move về neighbor có dp lớn hơn
```

Nếu đã compress memory xuống hai rows, reconstruction khó hơn vì history bị bỏ. Đây là trade-off giữa memory và information retention.

## Longest Increasing Subsequence

Classic DP:

\[
dp[i]=1+\max(dp[j]) \quad j<i, a[j]<a[i]
\]

Time `O(n^2)`.

Algorithm `O(n log n)` giữ:

```text
tails[len] = smallest possible tail của increasing subsequence length len+1
```

Mỗi value binary-search vị trí trong `tails`.

`tails` không nhất thiết là actual LIS ở mọi thời điểm; nó là **compressed frontier** của possibilities. Đây là một ví dụ sâu về state compression vượt khỏi table DP truyền thống.

## Grid DP

Grid path problems thường có natural dependency:

```text
dp[r][c] depends on top/left/diagonal
```

Nếu movement chỉ đi xuống/phải, state graph là DAG theo row+column order.

Nếu movement cho phép cycle, naive grid DP không còn trực tiếp; có thể cần graph shortest path hoặc detect another monotonic dimension.

## Interval DP

Interval DP dùng state:

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

Bottom-up order thường theo interval length tăng dần:

```text
for len = 1..n:
    for l:
        r = l + len - 1
```

Vì smaller intervals phải có trước larger intervals.

## Matrix Chain Multiplication

Dimensions `p0,p1,...,pn`. State:

```text
dp[i][j] = minimum scalar multiplications để nhân matrices i..j
```

Try last split `k`:

\[
dp[i][j] = \min_k dp[i][k] + dp[k+1][j] + p_{i-1}p_kp_j
\]

Đây là classic “choose partition point” interval DP.

## Tree DP

Fix parent để child subtrees độc lập.

Maximum independent set:

```text
dp[u][0] = best nếu không chọn u
dp[u][1] = best nếu chọn u
```

Nếu chọn `u`, children không được chọn.

Nếu không chọn `u`, mỗi child chọn tốt nhất giữa two states.

Tree DP mạnh vì tree itself cung cấp acyclic dependency structure.

## Rerooting DP

Nếu cần answer cho mọi node khi coi node đó là root, tính lại từ đầu là `O(n^2)`.

Rerooting reuse:

```text
child contribution
+ contribution từ phần ngoài child subtree
```

Pass 1 bottom-up, pass 2 top-down.

Đây là message-passing DP trên tree.

## Bitmask DP

Nếu `n` nhỏ, subset có thể encode bằng bitmask.

Travelling Salesman DP:

```text
dp[mask][u] = minimum cost visit set mask và kết thúc tại u
```

Transition add new vertex.

State count `O(2^n n)`. Bitmask không làm exponential biến mất; nó tổ chức exponential search để reuse overlapping states.

## Subset DP và SOS DP

Nếu cần aggregate over all submasks/supermasks, Sum Over Subsets DP có thể transform `O(3^n)` naive loops thành khoảng `O(n2^n)`.

Đây là dynamic programming trên lattice của subsets.

## Digit DP

Digit DP đếm numbers thỏa constraint trong range bằng state như:

```text
position
tight?        // prefix có đang bằng bound không
started?      // đã bắt đầu số chưa
additional property: sum/mod/count/etc
```

State `tight` là ví dụ rõ về future-relevant information: nếu prefix đã nhỏ hơn upper bound, future digits không còn bị bound digit hiện tại giới hạn.

## Profile DP

Board tiling hoặc frontier problems có thể encode trạng thái của một “biên” nhỏ bằng bitmask, rồi sweep qua rows/columns.

Thay vì state toàn board exponential, ta giữ only local boundary that affects future.

Đây là một form sophisticated của state compression.

## DP on DAG

Nếu graph là DAG, shortest/longest path có thể giải bằng topological order.

State:

```text
dp[v] = best value tới v
```

Relax outgoing edges một lần theo topo order.

Negative edge vẫn okay vì không có cycle.

Đây là bridge trực tiếp giữa graph algorithms và DP.

## Shortest path và DP khác nhau ở đâu?

Bellman-Ford có thể được nhìn như repeated relaxation DP theo số edges used:

```text
dp[k][v] = shortest path tới v dùng <= k edges
```

Nhưng graph algorithms thường khai thác structure/frontier để tránh explicit dimension.

Nhiều distinctions giữa “DP” và “graph algorithm” là implementation/structure emphasis hơn là mathematical wall.

## DP với monotone queue

Một transition dạng:

\[
dp[i]=\min_{j \in window(i)}(dp[j]+cost)
\]

có thể được optimize bằng deque nếu candidate value có monotonic structure.

DP optimization thường là tìm cách tăng tốc transition, không chỉ giảm number states.

## Prefix minima/maxima optimization

Nếu transition cần:

```text
min(dp[0..i-1])
```

đừng scan lại mỗi state; giữ prefix minimum.

Đây là reuse ở level transition computation.

## Divide-and-conquer optimization

Một số DP dạng partition:

\[
dp[k][i] = \min_{j<i}(dp[k-1][j]+C(j,i))
\]

có monotonic optimal split properties cho phép divide-and-conquer optimization.

Điều kiện proof không trivial; không áp dụng chỉ vì recurrence “trông giống”. Nhưng nó cho thấy advanced DP thường dựa vào structure của argmin/transition matrix.

## Knuth optimization

Một số interval DP thỏa quadrangle inequality/monotonicity có thể giảm cubic xuống quadratic.

Không cần học thuộc mọi theorem ngay, nhưng mental model là:

> Sau khi thiết kế đúng state/transition, bước tiếp theo là khai thác additional structure để giảm transition search.

## Convex Hull Trick

DP transition dạng tuyến tính:

\[
dp[i] = \min_j(m_j x_i + b_j)
\]

có thể được tối ưu bằng data structure giữ lines và query min/max.

Li Chao Tree hoặc convex hull trick biến “iterate all j” thành query geometry.

Đây là nơi DP kết nối với computational geometry/data structures.

## Probability DP

State value không nhất thiết min/max/count; có thể là probability/expected value.

Expected steps thường dùng law of total expectation:

\[
E[s] = 1 + \sum_t P(s\to t)E[t]
\]

Nhưng nếu transitions cycle, equations có thể không có simple topological DP; đôi khi cần solve linear systems hoặc transform states.

## DP modulo arithmetic

Combinatorial count có thể rất lớn. Problems thường yêu cầu mod `M`.

Cần chú ý overflow trước modulo trong C/Java, và Number safe range trong JavaScript.

Modulo changes numeric representation, không thay combinatorial recurrence.

## Infinity sentinel và overflow

Minimum DP thường initialize `INF`.

Đừng dùng maximum integer rồi cộng cost:

```text
INF + cost -> overflow
```

Use sufficiently safe sentinel hoặc guard:

```java
if (dp[prev] < INF) {
    dp[cur] = Math.min(dp[cur], dp[prev] + cost);
}
```

## Memo key design

Top-down DP với compound state cần canonical key.

Java có thể dùng arrays indexed dimensions hoặc immutable record.

JavaScript `Map` object keys dùng identity, nên `{i:1,j:2}` mới mỗi lần không match previous object. Cần encode key string/int hoặc nested maps.

C phải quản hash table/array ownership rõ.

## Sparse state DP

Nếu theoretical state space rất lớn nhưng reachable states ít, hash-map memoization có thể tốt hơn dense array.

Examples:

```text
DP theo large coordinate values
state machine với many impossible combinations
search + memo hybrid
```

Trade-off: hash overhead vs skipping unreachable states.

## DP và memory locality

2D `dp[i][j]` row-major traversal thường cache-friendly nếu inner loop đi contiguous.

Changing loop order có thể ảnh hưởng runtime rất mạnh dù Big-O giống nhau.

Rolling array vừa giảm memory vừa cải thiện cache, nhưng có thể làm reconstruction khó hơn.

## Reconstruction strategies

Có ba cách phổ biến:

```text
1. store parent/choice trực tiếp
2. backtrack bằng cách so dp values
3. recompute một phần nếu memory optimized
```

Store choices tăng memory nhưng đơn giản.

Recomputation tiết kiệm memory nhưng tăng CPU.

Design phụ thuộc output requirement.

## Counting vs optimizing

Một recurrence có thể cần:

```text
best value
number of best ways
lexicographically smallest optimal solution
```

Nếu tie semantics quan trọng, state value có thể phải lưu tuple hoặc extra metadata.

“DP đúng value” chưa chắc đủ cho requested output.

## State explosion

Nếu state dimensions:

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

Subset problems với `n≈40` có thể quá lớn cho `2^n`, nhưng split thành hai halves khoảng `2^(n/2)` rồi combine có thể hiệu quả.

Nếu numeric sum dimension nhỏ, pseudo-polynomial DP có thể tốt hơn.

Algorithm choice phụ thuộc both `n` và value ranges.

## Pseudo-polynomial complexity

Knapsack `O(nW)` là polynomial theo numeric value `W`, nhưng không polynomial theo input bit-length `log W`.

Đây gọi là pseudo-polynomial.

Hiểu distinction này quan trọng khi nối DSA với computational complexity.

## DP vs Greedy

Greedy giữ một frontier nhỏ vì prove local choice safe.

DP giữ nhiều states vì chưa thể loại alternatives sớm.

Nếu tìm được dominance/exchange property mạnh, một DP có thể collapse thành greedy.

Ngược lại nếu greedy choice có regret, DP giữ competing possibilities.

## Dominance pruning

Trong some DP/search, state A dominates B nếu A không tệ hơn B trên mọi future-relevant dimension.

Ta có thể discard dominated states.

Ví dụ resource-constrained path giữ Pareto frontier giữa cost/time. Đây là state pruning thay vì exact key equality reuse.

## DP correctness proof template

Một proof tốt thường gồm:

```text
1. định nghĩa state chính xác
2. chứng minh base cases
3. chứng minh transition cover mọi valid solution
4. chứng minh không bỏ candidate optimal
5. chứng minh evaluation order thỏa dependencies
```

Nếu optimization space, còn phải chứng minh overwrite order không làm dùng state mới sai semantics.

## Testing DP

Brute force trên small n là oracle rất mạnh.

Workflow:

```text
generate random small instance
solve brute-force exhaustive
solve DP
compare
```

Đây là cách bắt state/loop-order bugs tốt hơn nhiều examples thủ công.

## Common misconceptions

“Có recursion là DP” — sai. DP cần repeated equivalent states hoặc structured state graph đáng reuse.

“Có `dp[]` array là DP” — naming không quan trọng; state semantics mới quan trọng.

“Bottom-up luôn nhanh hơn” — sparse states có thể hợp memoization.

“Space optimization luôn tốt” — có thể mất reconstruction/debuggability.

“DP complexity = số states” — còn phải nhân transition cost.

“Loop order chỉ là implementation” — nhiều DP, loop order quyết định reuse semantics và correctness.

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

## Mental Model

> DP là nghệ thuật tìm **summary nhỏ nhất của quá khứ mà tương lai cần biết**. Khi summary đúng, nhiều histories collapse thành một state; khi state được reuse, exponential search có thể biến thành polynomial hoặc pseudo-polynomial computation. Sau đó optimization nâng cao tập trung vào giảm số states, giảm transition cost hoặc giảm memory.

Câu hỏi cốt lõi luôn là:

```text
Hai histories nào có future giống nhau?
State tối thiểu để phân biệt future là gì?
Transition cover mọi possibility chưa?
Dependency graph có order nào?
Có dominance/monotonicity/convexity để optimize không?
```

Xem thêm: [Recursion & Backtracking](./02_recursion_and_backtracking.md), [Greedy](./04_greedy_algorithms.md), [DAG/SCC](../03_graphs/04_dag_topological_sort_and_scc.md), [Bit Manipulation](../05_specialized/02_bit_manipulation_and_bitsets.md).