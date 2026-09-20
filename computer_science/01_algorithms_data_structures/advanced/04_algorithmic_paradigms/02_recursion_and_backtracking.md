# Recursion và Backtracking
**Đệ quy và quay lui (Recursion & Backtracking / 재귀와 백트래킹)**

Recursion không phải chỉ là “function gọi chính nó”. Nó là một cách mô hình hóa problem bằng **một contract nhỏ hơn của cùng loại problem**. Backtracking xây trên recursion hoặc explicit stack để explore một không gian lựa chọn, nhưng thêm một ý tưởng quan trọng: sau khi thử một decision, ta có thể **undo** nó để thử decision khác.

Hai khái niệm thường đi cùng nhau nhưng không giống nhau. Một tree traversal có thể recursive mà không backtrack theo nghĩa search choices. Một Sudoku solver thường vừa recursive vừa backtracking vì mỗi candidate tạo một branch có thể phải hoàn tác.

## Mental Model

> Recursion là “giải subproblem rồi tin vào contract của subproblem”. Backtracking là “choose → constrain → explore → undo”, tức DFS trên một state-space tree ngầm.

Muốn hiểu một recursive algorithm, đừng đọc bằng cách mô phỏng từng stack frame ngay từ đầu. Hãy xác định contract của function trước.

## Recursive contract

Giả sử function:

```text
solve(state)
```

có contract:

> trả lời đúng problem tương ứng với `state`.

Một recursion đúng cần ba yếu tố:

1. **Base case** giải trực tiếp instance đủ nhỏ.
2. **Recursive reduction** biến current problem thành một hay nhiều subproblems đúng cùng contract.
3. **Progress measure** phải tiến gần base case để đảm bảo termination.

Ví dụ binary tree height:

\[
height(node)=1+\max(height(left),height(right))
\]

Base case:

```text
height(null) = 0
```

Progress measure là subtree size/depth giảm khi đi xuống child.

## Recursion và induction

Recursion correctness thường mirror mathematical induction.

Induction nói:

```text
base case đúng
nếu smaller cases đúng -> current case đúng
```

Recursive proof cũng vậy:

```text
base return đúng
assume recursive calls trả đúng theo contract
show current combine logic tạo answer đúng
```

Đây là lý do induction là công cụ proof tự nhiên cho recursive algorithms.

## Call stack thực sự giữ gì?

Mỗi active function call cần lưu state để tiếp tục sau khi recursive call return: parameters, local variables, return address và runtime metadata.

Ví dụ:

```java
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

Call `factorial(5)` phải giữ các pending multiplications `5 *`, `4 *`, `3 *`, `2 *` trên stack.

Độ sâu recursion là `O(n)`, nên memory stack cũng `O(n)` dù arithmetic work chỉ `O(n)`.

## Tail recursion không phải lúc nào cũng tối ưu được

Tail-recursive function có recursive call là operation cuối cùng. Một số languages/runtime có thể tối ưu thành loop, nhưng không nên giả định điều đó portable.

Java không đảm bảo tail-call optimization. JavaScript specification/runtime behavior cũng không nên được dựa vào như một optimization phổ biến. C compiler có thể optimize trong một số case nhưng không phải semantic guarantee chung.

Nếu depth có thể rất lớn, explicit loop/stack thường an toàn hơn.

## Tree traversal: recursion khớp shape dữ liệu

Binary tree vốn có recursive definition:

```text
Tree = empty
    hoặc Node(left Tree, value, right Tree)
```

Vì vậy traversal recursive gần như trực tiếp từ structure:

```java
void inorder(Node x) {
    if (x == null) return;
    inorder(x.left);
    visit(x);
    inorder(x.right);
}
```

Ở đây recursion không phải trick; representation của data đã recursive.

## Recursion tree và complexity

Một recursive function không thể phân tích chỉ bằng depth. Phải xem branching factor và work mỗi node.

Ví dụ naive Fibonacci:

```text
fib(n) = fib(n-1) + fib(n-2)
```

tạo recursion tree có rất nhiều repeated states. Complexity exponential không phải vì recursion bản thân chậm, mà vì cùng subproblem được recompute nhiều lần.

Memoization biến state tree thành state DAG bằng cách reuse results.

## Backtracking là DFS trên implicit state graph/tree

Nhiều combinatorial problems không build graph rõ ràng. Mỗi partial solution là một state; mỗi choice sinh child state.

Ví dụ permutations:

```js
function permutations(nums) {
  const ans = [];
  const path = [];
  const used = Array(nums.length).fill(false);

  function dfs() {
    if (path.length === nums.length) {
      ans.push([...path]);
      return;
    }

    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;

      used[i] = true;      // choose / constrain
      path.push(nums[i]);

      dfs();               // explore

      path.pop();          // undo
      used[i] = false;
    }
  }

  dfs();
  return ans;
}
```

State tree không được materialize; recursion stack chính là path hiện tại.

## Choose → Constrain → Explore → Undo

Một template mạnh:

```text
for candidate in candidates(state):
    if candidate invalid:
        continue

    apply(candidate)
    recurse(nextState)
    undo(candidate)
```

`undo` phải đối xứng với mutation. Nếu `apply()` thay đổi ba structures nhưng `undo()` chỉ restore hai, bug có thể chỉ xuất hiện ở branch sau.

Trong code production, có ba strategy để quản state:

```text
mutable + undo      -> ít allocation, dễ bug rollback
copy-on-recursion   -> đơn giản correctness, tốn memory/time
persistent state    -> structural sharing, implementation phức tạp hơn
```

## Subsets: branching factor 2

Mỗi element có hai choices: lấy hoặc không lấy.

```java
void subsets(int i, int[] a, List<Integer> cur) {
    if (i == a.length) {
        output(cur);
        return;
    }

    subsets(i + 1, a, cur); // exclude

    cur.add(a[i]);
    subsets(i + 1, a, cur); // include
    cur.remove(cur.size() - 1);
}
```

Có `2^n` subsets, nên algorithm output tất cả subsets không thể tốt hơn `Omega(2^n)` chỉ xét số answers.

Đây là distinction quan trọng giữa algorithm inefficiency và output-size lower bound.

## Permutations và factorial growth

Với `n` distinct items, số permutations là:

\[
n!
\]

Dù pruning/check cực nhanh, nếu phải output tất cả permutations thì complexity ít nhất proportional `n!`.

Backtracking không “làm exponential thành polynomial”. Nó giúp không gian search được biểu diễn gọn và cho phép prune branches không cần thiết.

## Pruning: loại cả subtree

Nếu partial state đã không thể dẫn tới valid answer, descendants của nó không cần generate.

Ví dụ N-Queens: nếu queen mới conflict với column hoặc diagonal đã dùng, toàn bộ placements tiếp theo dưới branch đó invalid.

Thay vì scan board mỗi lần, maintain constraints:

```text
usedColumn[c]
usedDiag1[r-c]
usedDiag2[r+c]
```

Check từ `O(n)` xuống gần `O(1)`.

Search speed không chỉ phụ thuộc số branches; còn phụ thuộc cost validate mỗi branch.

## Bitmask backtracking

Nếu `n` nhỏ, constraints có thể encode bằng bitmask.

N-Queens có thể giữ:

```text
columns
main diagonals
anti diagonals
```

và compute available positions bằng bit operations. Điều này giảm constant factor rất mạnh và tránh set/hash allocation.

Nhưng bitmask không thay đổi worst-case combinatorial nature; nó chỉ làm state transition rẻ hơn.

## Duplicate control phải gắn với state semantics

Giả sử input sorted có duplicates và ta generate combinations/permutations. Rule phổ biến:

```text
if (i > start && a[i] == a[i-1]) continue;
```

Điểm quan trọng là **skip duplicate ở cùng recursion depth**, vì hai equal candidates tại cùng choice position tạo cùng subtree semantic.

Nếu skip equal value ở mọi depth, ta có thể loại legitimate solutions có nhiều occurrences.

Rule chống duplicate phải derive từ câu hỏi:

> Hai branches này có đại diện cùng decision tại state hiện tại hay không?

## Backtracking cho Combination Sum

Nếu candidates positive và có target còn lại `remain`, ta có pruning monotonic:

```text
candidate > remain -> không cần thử candidate lớn hơn nữa
```

nếu candidates sorted.

Nếu values có negative numbers, reasoning này vỡ. Một branch đang overshoot có thể quay lại bằng số âm.

Đây là ví dụ assumptions quyết định validity của pruning.

## N-Queens: state-space reasoning

Thay vì đặt queen ở bất kỳ cell nào, ta có thể model mỗi row đặt đúng một queen. Điều đó giảm branching space ngay từ representation.

State tối thiểu chỉ cần:

```text
row hiện tại
occupied columns
occupied diagonals
```

Không nhất thiết giữ full board nếu chỉ cần count solutions.

Problem modeling tốt có thể quan trọng hơn micro-optimization trong DFS.

## Sudoku và constraint propagation

Sudoku solver naive thử digits 1..9 cho mọi empty cell. Tốt hơn là maintain candidate set của từng cell hoặc row/column/box masks.

Một heuristic mạnh là chọn cell có **Minimum Remaining Values (MRV)** — ít candidates nhất.

Tại sao? Nếu branch sắp fail, ta muốn fail sớm để prune subtree lớn.

Đây gọi là **fail-first principle** trong constraint satisfaction.

## Branch ordering

Nếu chỉ cần một solution, thứ tự candidates ảnh hưởng runtime mạnh dù worst-case không đổi.

Các heuristics thường gồm:

```text
most constrained variable first
candidate có khả năng fail sớm
candidate có score tốt trước nếu branch-and-bound
```

Nếu cần enumerate toàn bộ solutions, ordering chỉ thay sequence output, không giảm số valid leaves; pruning vẫn có thể giảm invalid states.

## Backtracking và memoization

Nếu future answer chỉ phụ thuộc một canonical state, nhiều histories có thể merge.

Ví dụ recursive coin change có thể reach cùng state:

```text
(index, remainingAmount)
```

qua nhiều đường. Nếu solve(state) luôn cho cùng result, memoization tránh recompute.

Lúc đó implicit tree thực chất là graph với repeated nodes.

### Dấu hiệu nên nghĩ DP

Nếu bạn thấy recursion tree có nhiều calls với cùng parameters hoặc cùng logical state, hãy hỏi:

> Lịch sử đi tới state này có còn ảnh hưởng future không?

Nếu không, state có thể memoize.

## Backtracking khác Dynamic Programming thế nào?

Backtracking thường explore choices để tìm feasible/optimal solution và dựa mạnh vào pruning.

DP xác định equivalence classes của histories thành states và reuse result.

Một problem có thể dùng cả hai: backtracking để explore structure, memoization để merge repeated states.

Không nên phân loại bằng syntax “có recursion hay không”. Top-down DP cũng recursive.

## Branch and Bound

**Branch and Bound (분기 한정법)** mở rộng backtracking cho optimization. Ngoài feasibility pruning, ta tính optimistic bound của best result có thể đạt từ partial state.

Nếu bound còn tệ hơn best solution đã biết, prune branch.

Ví dụ TSP exact solver có thể dùng lower bound trên remaining route cost. Knapsack exact search có thể dùng fractional-knapsack upper bound.

Mental model:

```text
backtracking      -> prune impossible branches
branch-and-bound  -> prune branches không thể beat incumbent
```

## Alpha-Beta như specialized pruning

Trong minimax game tree, alpha-beta pruning loại branches không thể ảnh hưởng final decision do current lower/upper bounds.

Nó là một ví dụ domain-specific của general idea: nếu partial information đã chứng minh descendants không thể thay answer, skip whole subtree.

## Explicit stack thay recursion

Deep graph/tree có thể overflow call stack. Ta có thể mô phỏng recursion bằng explicit stack.

Nhưng với backtracking, frame cần lưu nhiều state hơn chỉ node:

```text
current state
next candidate index
data cần undo
```

Recursive syntax tự động lưu program counter/local variables trong call frame; iterative version phải encode chúng rõ ràng.

Đây là lý do iterative backtracking đôi khi phức tạp hơn iterative DFS đơn giản.

## C: ownership và mutable state

Trong C, recursive function cần rõ ai sở hữu buffers. Nếu mỗi recursive call `malloc` một state copy, overhead lớn và dễ leak khi early return.

Pattern mutable shared arrays + explicit undo thường hiệu quả hơn, nhưng cần discipline:

```c
path[depth] = candidate;
used[candidate] = true;
search(depth + 1);
used[candidate] = false;
```

Nếu recursion có multiple exit paths, cleanup phải nhất quán.

## Java: collections và copy cost

Trong Java, pattern:

```java
ans.add(new ArrayList<>(path));
```

ở leaf là bắt buộc nếu `path` tiếp tục mutate. Nếu thêm chính `path`, mọi references trong `ans` có thể cùng trỏ tới object đang bị thay đổi.

Đây là một bug aliasing phổ biến.

## JavaScript: object mutation và recursion limit

Trong JavaScript, arrays/objects dùng reference semantics. `ans.push(path)` lưu reference; thường cần:

```js
ans.push([...path]);
```

cho snapshot.

Deep recursive search còn có call-stack limit phụ thuộc engine. Với input depth không kiểm soát, explicit stack hoặc iterative design an toàn hơn.

## Complexity của backtracking

Một cách estimate tốt hơn chỉ nói “exponential” là:

\[
O(\text{number of visited states} \times \text{cost per state})
\]

Pruning giảm visited states. Better constraint representation giảm cost/state. Memoization merge repeated states. Branch ordering có thể giúp tìm incumbent sớm để prune mạnh hơn.

Đây là decomposition thực dụng khi optimize solver.

## Search space vs solution space

Không gian candidate có thể lớn hơn rất nhiều số valid solutions. Một good backtracking model cố generate ít invalid state nhất có thể.

Ví dụ generate all `n^n` board configurations rồi kiểm N-Queens là vô lý; enforce one queen per row ngay từ state model giảm search space trước cả pruning.

## Common mistakes

**Quên undo mutation.** Branch sau thừa state của branch trước.

**Undo sai thứ tự.** Nếu mutations phụ thuộc nhau, restore phải đối xứng reverse order.

**Base case quá sớm/quá muộn.** Có thể miss solution hoặc recurse ngoài bounds.

**Pruning không có proof.** Có thể loại valid solutions.

**Copy state quá nhiều.** Correct nhưng chậm/memory-heavy.

**Dùng global mutable state nhưng không reset giữa runs.** Test riêng lẻ pass, batch fail.

**Không xử lý duplicates đúng depth.** Sinh duplicate answers hoặc bỏ mất answers.

**Assume recursion luôn an toàn.** Deep input có thể stack overflow.

## Testing backtracking

Với `n` nhỏ, compare output count với known combinatorial values:

```text
subsets -> 2^n
permutations distinct -> n!
```

Kiểm mỗi output thỏa constraints và không duplicate nếu semantics yêu cầu unique.

Một kỹ thuật mạnh là dùng brute-force generator đơn giản làm oracle cho small `n`, rồi compare optimized pruning version.

Ngoài final answers, có thể assert state restored sau mỗi recursive call trong debug build.

## Mental Model mở rộng

> Backtracking không phải “thử tất cả một cách mù quáng”. Nó là **search-space engineering**: chọn state representation, candidate order, invariant và bound sao cho cả subtree có thể bị loại càng sớm càng tốt mà vẫn giữ completeness.

Khi một problem có choices lồng nhau, hãy hỏi: state tối thiểu là gì, branch nào có thể prove impossible sớm, có repeated state để memoize không, và output size itself có exponential không. Những câu hỏi đó quan trọng hơn việc nhớ một template recursion cụ thể.