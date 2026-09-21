# Recursion và quay lui (backtracking)
**Đệ quy và quay lui (Recursion & Backtracking / 재귀와 백트래킹)**

Recursion không phải chỉ là “hàm gọi chính nó”. Nó là một cách mô hình hóa problem bằng **một contract nhỏ hơn của cùng loại problem**. quay lui xây trên recursion hoặc explicit stack để explore một không gian lựa chọn, nhưng thêm một ý tưởng quan trọng: sau khi thử một decision, ta có thể **undo** nó để thử decision khác.

Hai khái niệm thường đi cùng nhau nhưng không giống nhau. Duyệt cây có thể dùng đệ quy mà không phải quay lui theo nghĩa thử các lựa chọn. Bộ giải Sudoku thường vừa đệ quy vừa quay lui vì mỗi ứng viên tạo một nhánh có thể phải hoàn tác.

## Mô hình tư duy

> Recursion là “giải subproblem rồi tin vào contract của subproblem”. quay lui là “choose → constrain → explore → undo”, tức DFS trên một trạng thái-space cây ngầm.

Muốn hiểu một recursive thuật toán, đừng đọc bằng cách mô phỏng từng khung ngăn xếp ngay từ đầu. Hãy xác định contract của hàm trước.

## hợp đồng đệ quy

Giả sử hàm:

```text
solve(state)
```

có contract:

> trả lời đúng problem tương ứng với `state`.

Một recursion đúng cần ba yếu tố:

1. **trường hợp cơ sở** giải trực tiếp instance đủ nhỏ.
2. **Recursive reduction** biến hiện tại problem thành một hay nhiều subproblems đúng cùng contract.
3. **Progress measure** phải tiến gần trường hợp cơ sở để đảm bảo termination.

Ví dụ cây nhị phân chiều cao:

\[
chiều cao(node)=1+\max(chiều cao(left),chiều cao(right))
\]

trường hợp cơ sở:

```text
height(null) = 0
```

Progress measure là kích thước cây con/độ sâu giảm khi đi xuống nút con.

## Recursion và quy nạp

Recursion tính đúng đắn thường mirror mathematical quy nạp.

quy nạp nói:

```text
base case đúng
nếu smaller cases đúng -> current case đúng
```

Recursive chứng minh cũng vậy:

```text
base return đúng
assume recursive calls trả đúng theo contract
show current combine logic tạo answer đúng
```

Đây là lý do quy nạp là công cụ chứng minh tự nhiên cho recursive các thuật toán.

## ngăn xếp lời gọi thực sự giữ gì?

Mỗi lời gọi hàm đang hoạt động cần lưu trạng thái để tiếp tục sau khi lời gọi đệ quy trả về: tham số, biến cục bộ, địa chỉ trả về và metadata của môi trường chạy.

Ví dụ:

```java
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

Call `factorial(5)` phải giữ các pending multiplications `5 *`, `4 *`, `3 *`, `2 *` trên stack.

Độ sâu recursion là `O(n)`, nên bộ nhớ stack cũng `O(n)` dù arithmetic work chỉ `O(n)`.

## Tail recursion không phải lúc nào cũng tối ưu được

Tail-hàm đệ quy có lời gọi đệ quy là thao tác cuối cùng. Một số languages/môi trường chạy có thể tối ưu thành loop, nhưng không nên giả định điều đó portable.

Java không đảm bảo tối ưu lời gọi đuôi. JavaScript specification/môi trường chạy hành vi cũng không nên được dựa vào như một optimization phổ biến. C trình biên dịch có thể optimize trong một số case nhưng không phải semantic bảo đảm chung.

Nếu độ sâu có thể rất lớn, explicit loop/stack thường an toàn hơn.

## cây traversal: recursion khớp shape dữ liệu

cây nhị phân vốn có recursive definition:

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

Ở đây recursion không phải trick; cách biểu diễn (representation) của data đã recursive.

## cây đệ quy và complexity

Một hàm đệ quy không thể phân tích chỉ bằng độ sâu. Phải xem hệ số phân nhánh và work mỗi nút.

Ví dụ naive Fibonacci:

```text
fib(n) = fib(n-1) + fib(n-2)
```

tạo cây đệ quy có rất nhiều lặp lại các trạng thái. Complexity exponential không phải vì recursion bản thân chậm, mà vì cùng subproblem được recompute nhiều lần.

Memoization biến trạng thái cây thành trạng thái DAG bằng cách reuse các kết quả.

## quay lui là DFS trên implicit đồ thị trạng thái/cây

Nhiều combinatorial problems không xây dựng đồ thị rõ ràng. Mỗi partial lời giải là một trạng thái; mỗi choice sinh nút con trạng thái.

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

trạng thái cây không được materialize; ngăn xếp đệ quy chính là đường đi hiện tại.

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

`undo` phải đối xứng với sự thay đổi dữ liệu. Nếu `apply()` thay đổi ba structures nhưng `undo()` chỉ restore hai, bug có thể chỉ xuất hiện ở branch sau.

Trong code hệ thống thực tế, có ba strategy để quản trạng thái:

```text
mutable + undo      -> ít allocation, dễ bug rollback
copy-on-recursion   -> đơn giản correctness, tốn memory/time
persistent state    -> structural sharing, implementation phức tạp hơn
```

## Subsets: hệ số phân nhánh 2

Mỗi phần tử có hai choices: lấy hoặc không lấy.

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

Có `2^n` subsets, nên thuật toán đầu ra tất cả subsets không thể tốt hơn `Omega(2^n)` chỉ xét số answers.

Đây là khác biệt quan trọng giữa sự kém hiệu quả của thuật toán và cận dưới do kích thước đầu ra.

## Permutations và factorial growth

Với `n` distinct items, số permutations là:

\[
n!
\]

Dù pruning/check cực nhanh, nếu phải đầu ra tất cả permutations thì complexity ít nhất proportional `n!`.

quay lui không “làm exponential thành polynomial”. Nó giúp không gian search được biểu diễn gọn và cho phép prune branches không cần thiết.

## Pruning: loại cả cây con

Nếu partial trạng thái đã không thể dẫn tới hợp lệ answer, các hậu duệ của nó không cần generate.

Ví dụ N-Queens: nếu queen mới conflict với column hoặc diagonal đã dùng, toàn bộ placements tiếp theo dưới branch đó không hợp lệ.

Thay vì quét board mỗi lần, maintain các ràng buộc:

```text
usedColumn[c]
usedDiag1[r-c]
usedDiag2[r+c]
```

Check từ `O(n)` xuống gần `O(1)`.

Tốc độ tìm kiếm không chỉ phụ thuộc vào số nhánh mà còn phụ thuộc chi phí xác minh mỗi nhánh.

## Bitmask quay lui

Nếu `n` nhỏ, các ràng buộc có thể encode bằng bitmask.

N-Queens có thể giữ:

```text
columns
main diagonals
anti diagonals
```

và compute available positions bằng bit các thao tác. Điều này giảm constant factor rất mạnh và tránh set/hash cấp phát.

Nhưng bitmask không thay đổi trường hợp xấu nhất combinatorial nature; nó chỉ làm trạng thái transition rẻ hơn.

## phần tử trùng control phải gắn với trạng thái ngữ nghĩa (semantics)

Giả sử đầu vào sorted có các phần tử trùng và ta generate combinations/permutations. quy tắc phổ biến:

```text
if (i > start && a[i] == a[i-1]) continue;
```

Điểm quan trọng là **skip phần tử trùng ở cùng recursion độ sâu**, vì hai equal các ứng viên tại cùng choice position tạo cùng cây con semantic.

Nếu skip equal giá trị ở mọi độ sâu, ta có thể loại legitimate các lời giải có nhiều occurrences.

quy tắc chống phần tử trùng phải derive từ câu hỏi:

> Hai branches này có đại diện cùng decision tại trạng thái hiện tại hay không?

## quay lui cho Combination Sum

Nếu các ứng viên positive và có đích còn lại `remain`, ta có pruning monotonic:

```text
candidate > remain -> không cần thử candidate lớn hơn nữa
```

nếu các ứng viên sorted.

Nếu các giá trị có negative numbers, reasoning này vỡ. Một branch đang overshoot có thể quay lại bằng số âm.

Đây là ví dụ các giả định quyết định validity của pruning.

## N-Queens: trạng thái-space reasoning

Thay vì đặt queen ở bất kỳ cell nào, ta có thể mô hình mỗi row đặt đúng một queen. Điều đó giảm branching space ngay từ cách biểu diễn.

trạng thái tối thiểu chỉ cần:

```text
row hiện tại
occupied columns
occupied diagonals
```

Không nhất thiết giữ full board nếu chỉ cần count các lời giải.

Problem mô hình hóa tốt có thể quan trọng hơn micro-optimization trong DFS.

## Sudoku và ràng buộc propagation

Sudoku solver naive thử digits 1..9 cho mọi rỗng cell. Tốt hơn là maintain ứng viên set của từng cell hoặc các mặt nạ hàng/cột/khối.

Một heuristic mạnh là chọn cell có **Minimum Remaining các giá trị (MRV)** — ít các ứng viên nhất.

Tại sao? Nếu branch sắp fail, ta muốn fail sớm để prune cây con lớn.

Đây gọi là **fail-first principle** trong ràng buộc satisfaction.

## thứ tự phân nhánh

Nếu chỉ cần một lời giải, thứ tự các ứng viên ảnh hưởng môi trường chạy mạnh dù trường hợp xấu nhất không đổi.

Các heuristics thường gồm:

```text
most constrained variable first
candidate có khả năng fail sớm
candidate có score tốt trước nếu branch-and-bound
```

Nếu cần enumerate toàn bộ các lời giải, ordering chỉ thay sequence đầu ra, không giảm số hợp lệ các nút lá; pruning vẫn có thể giảm không hợp lệ các trạng thái.

## quay lui và memoization

Nếu tương lai answer chỉ phụ thuộc một canonical trạng thái, nhiều histories có thể merge.

Ví dụ recursive coin change có thể reach cùng trạng thái:

```text
(index, remainingAmount)
```

qua nhiều đường. Nếu solve(state) luôn cho cùng kết quả, memoization tránh recompute.

Lúc đó implicit cây thực chất là đồ thị với lặp lại các nút.

### Dấu hiệu nên nghĩ DP

Nếu bạn thấy cây đệ quy có nhiều calls với cùng parameters hoặc cùng logic trạng thái, hãy hỏi:

> Lịch sử đi tới trạng thái này có còn ảnh hưởng tương lai không?

Nếu không, trạng thái có thể memoize.

## quay lui khác quy hoạch động (dynamic programming) thế nào?

quay lui thường explore choices để tìm feasible/lời giải tối ưu và dựa mạnh vào pruning.

DP xác định các lớp tương đương của histories thành các trạng thái và reuse kết quả.

Một bài toán có thể dùng cả hai: quay lui để khám phá không gian cấu trúc, còn ghi nhớ (memoization) để hợp nhất các trạng thái lặp lại.

Không nên phân loại bằng syntax “có recursion hay không”. Top-down DP cũng recursive.

## nhánh và cận

**nhánh và cận (분기 한정법)** mở rộng quay lui cho optimization. Ngoài feasibility pruning, ta tính optimistic bound của best kết quả có thể đạt từ partial trạng thái.

Nếu bound còn tệ hơn best lời giải đã biết, prune branch.

Ví dụ TSP chính xác solver có thể dùng cận dưới trên remaining route chi phí. Knapsack chính xác search có thể dùng fractional-knapsack cận trên (upper bound).

Mô hình tư duy:

```text
backtracking      -> prune impossible branches
branch-and-bound  -> prune branches không thể beat incumbent
```

## Alpha-Beta như chuyên biệt pruning

Trong minimax game cây, alpha-beta pruning loại branches không thể ảnh hưởng final decision do hiện tại lower/các cận trên.

Nó là một ví dụ domain-specific của general idea: nếu partial thông tin đã chứng minh các hậu duệ không thể thay answer, skip whole cây con.

## Explicit stack thay recursion

Deep đồ thị/cây có thể tràn số ngăn xếp lời gọi. Ta có thể mô phỏng recursion bằng explicit stack.

Nhưng với quay lui, frame cần lưu nhiều trạng thái hơn chỉ nút:

```text
current state
next candidate index
data cần undo
```

Cú pháp đệ quy tự động lưu bộ đếm lệnh và biến cục bộ trong khung lời gọi; phiên bản dạng lặp phải biểu diễn các thông tin này một cách tường minh.

Đây là lý do iterative quay lui đôi khi phức tạp hơn iterative DFS đơn giản.

## C: quyền sở hữu (ownership) và có thể thay đổi trạng thái

Trong C, hàm đệ quy cần rõ ai sở hữu các bộ đệm. Nếu mỗi lời gọi đệ quy `malloc` một trạng thái copy, overhead lớn và dễ leak khi early return.

mẫu có thể thay đổi shared các mảng + explicit undo thường hiệu quả hơn, nhưng cần discipline:

```c
path[depth] = candidate;
used[candidate] = true;
search(depth + 1);
used[candidate] = false;
```

Nếu recursion có multiple exit các đường đi, cleanup phải nhất quán.

## Java: collections và copy chi phí

Trong Java, mẫu:

```java
ans.add(new ArrayList<>(path));
```

ở nút lá là bắt buộc nếu `path` tiếp tục mutate. Nếu thêm chính `path`, mọi các tham chiếu trong `ans` có thể cùng trỏ tới đối tượng đang bị thay đổi.

Đây là một bug bí danh bộ nhớ phổ biến.

## JavaScript: đối tượng sự thay đổi dữ liệu và recursion limit

Trong JavaScript, các mảng/các đối tượng dùng tham chiếu ngữ nghĩa. `ans.push(path)` lưu tham chiếu; thường cần:

```js
ans.push([...path]);
```

cho snapshot.

Deep recursive search còn có call-stack limit phụ thuộc engine. Với đầu vào độ sâu không kiểm soát, explicit stack hoặc iterative design an toàn hơn.

## Complexity của quay lui

Một cách estimate tốt hơn chỉ nói “exponential” là:

\[
O(\text{number of visited states} \times \text{cost per state})
\]

Pruning giảm đã thăm các trạng thái. Better ràng buộc cách biểu diễn giảm chi phí/trạng thái. Memoization merge lặp lại các trạng thái. thứ tự phân nhánh có thể giúp tìm incumbent sớm để prune mạnh hơn.

Đây là decomposition thực dụng khi optimize solver.

## không gian tìm kiếm vs không gian lời giải

Không gian ứng viên có thể lớn hơn rất nhiều số hợp lệ các lời giải. Một good quay lui mô hình cố generate ít không hợp lệ trạng thái nhất có thể.

Ví dụ generate all `n^n` board configurations rồi kiểm N-Queens là vô lý; enforce one queen per row ngay từ mô hình trạng thái giảm không gian tìm kiếm trước cả pruning.

## Phổ biến mistakes

**Quên hoàn tác thay đổi dữ liệu.** Nhánh sau sẽ thừa trạng thái của nhánh trước.

**Undo sai thứ tự.** Nếu mutations phụ thuộc nhau, restore phải đối xứng reverse order.

**trường hợp cơ sở quá sớm/quá muộn.** Có thể miss lời giải hoặc recurse ngoài bounds.

**Pruning không có chứng minh.** Có thể loại hợp lệ các lời giải.

**Copy trạng thái quá nhiều.** Correct nhưng chậm/memory-heavy.

**Dùng toàn cục có thể thay đổi trạng thái nhưng không reset giữa runs.** Test riêng lẻ pass, batch fail.

**Không xử lý các phần tử trùng đúng độ sâu.** Sinh phần tử trùng answers hoặc bỏ mất answers.

**Assume recursion luôn an toàn.** Deep đầu vào có thể stack tràn số.

## kiểm thử quay lui

Với `n` nhỏ, so sánh đầu ra count với known combinatorial các giá trị:

```text
subsets -> 2^n
permutations distinct -> n!
```

Kiểm mỗi đầu ra thỏa các ràng buộc và không phần tử trùng nếu ngữ nghĩa yêu cầu unique.

Một kỹ thuật mạnh là dùng brute-force generator đơn giản làm oracle cho small `n`, rồi so sánh optimized pruning version.

Ngoài final answers, có thể assert trạng thái restored sau mỗi lời gọi đệ quy trong gỡ lỗi xây dựng.

## Mô hình tư duy mở rộng

> Quay lui không phải “thử tất cả một cách mù quáng”. Nó là **thiết kế không gian tìm kiếm (search-space engineering)**: chọn cách biểu diễn trạng thái, thứ tự ứng viên, bất biến và cận sao cho có thể loại bỏ cả cây con càng sớm càng tốt mà vẫn không bỏ sót nghiệm.

Khi một problem có choices lồng nhau, hãy hỏi: trạng thái tối thiểu là gì, branch nào có thể prove impossible sớm, có lặp lại trạng thái để memoize không, và kích thước đầu ra itself có exponential không. Những câu hỏi đó quan trọng hơn việc nhớ một template recursion cụ thể.