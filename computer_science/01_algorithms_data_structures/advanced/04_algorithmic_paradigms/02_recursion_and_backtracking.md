# Recursion và quay lui (backtracking)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Recursion và quay lui (backtracking)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Mô hình tư duy** gom các mảnh thành mental model có thể mang sang nhánh khác; sau đó sang **hợp đồng đệ quy** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Đệ quy và quay lui (Recursion & Backtracking / 재귀와 백트래킹)**

Recursion không phải chỉ là “hàm gọi chính nó”. Nó là một cách mô hình hóa bài toán (problem / 문제) bằng **một đặc tả hợp đồng (contract / 계약) nhỏ hơn của cùng loại bài toán (problem / 문제)**. quay lui xây trên recursion hoặc tường minh (explicit / 명시적) ngăn xếp (stack / 스택) để explore một không gian lựa chọn, nhưng thêm một ý tưởng quan trọng: sau khi thử một quyết định (decision / 결정), ta có thể **undo** nó để thử quyết định (decision / 결정) khác.

Hai khái niệm thường đi cùng nhau nhưng không giống nhau. Duyệt cây có thể dùng đệ quy mà không phải quay lui theo nghĩa thử các lựa chọn. Bộ giải Sudoku thường vừa đệ quy vừa quay lui vì mỗi ứng viên tạo một nhánh có thể phải hoàn tác.

## Mô hình tư duy

> Recursion là “giải subproblem rồi tin vào đặc tả hợp đồng (contract / 계약) của subproblem”. quay lui là “choose → constrain → explore → undo”, tức DFS trên một trạng thái-space cây ngầm.

Muốn hiểu một recursive thuật toán, đừng đọc bằng cách mô phỏng từng khung ngăn xếp ngay từ đầu. Hãy xác định đặc tả hợp đồng (contract / 계약) của hàm trước.

> **Chuyển mạch:** Trong **Recursion và quay lui (backtracking)**, **hợp đồng đệ quy** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Recursion và quy nạp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## hợp đồng đệ quy

Giả sử hàm:

```text
solve(state)
```

có đặc tả hợp đồng (contract / 계약):

> trả lời đúng bài toán (problem / 문제) tương ứng với `state`.

Một recursion đúng cần ba yếu tố:

1. **trường hợp cơ sở** giải trực tiếp instance đủ nhỏ.
2. **Recursive reduction** biến hiện tại bài toán (problem / 문제) thành một hay nhiều subproblems đúng cùng đặc tả hợp đồng (contract / 계약).
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

> **Chuyển mạch:** Ở chặng này của **Recursion và quay lui (backtracking)**, **Recursion và quy nạp** tiếp nhận điểm tựa từ **hợp đồng đệ quy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ngăn xếp lời gọi thực sự giữ gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Recursion và quay lui (backtracking)**, **ngăn xếp lời gọi thực sự giữ gì?** tiếp nhận điểm tựa từ **Recursion và quy nạp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tail recursion không phải lúc nào cũng tối ưu được** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ngăn xếp lời gọi thực sự giữ gì?

Mỗi lời gọi hàm đang hoạt động cần lưu trạng thái để tiếp tục sau khi lời gọi đệ quy trả về: tham số, biến cục bộ, địa chỉ trả về và siêu dữ liệu (metadata / 메타데이터) của môi trường chạy.

Ví dụ:

```java
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

Lời gọi (call / 호출) `factorial(5)` phải giữ các pending multiplications `5 *`, `4 *`, `3 *`, `2 *` trên ngăn xếp (stack / 스택).

Độ sâu recursion là `O(n)`, nên bộ nhớ ngăn xếp (stack / 스택) cũng `O(n)` dù arithmetic công việc (work / 작업) chỉ `O(n)`.

> **Chuyển mạch:** Trong **Recursion và quay lui (backtracking)**, **Tail recursion không phải lúc nào cũng tối ưu được** tiếp nhận điểm tựa từ **ngăn xếp lời gọi thực sự giữ gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **cây traversal: recursion khớp shape dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tail recursion không phải lúc nào cũng tối ưu được

Tail-hàm đệ quy có lời gọi đệ quy là thao tác cuối cùng. Một số languages/môi trường chạy có thể tối ưu thành vòng lặp (loop / 루프), nhưng không nên giả định điều đó portable.

Java không đảm bảo tối ưu lời gọi đuôi. JavaScript specification/môi trường chạy hành vi cũng không nên được dựa vào như một tối ưu hóa (optimization / 최적화) phổ biến. C trình biên dịch có thể optimize trong một số trường hợp (case / 사례) nhưng không phải ngữ nghĩa (semantic / 의미적) bảo đảm chung.

Nếu độ sâu có thể rất lớn, tường minh (explicit / 명시적) vòng lặp (loop / 루프)/ngăn xếp (stack / 스택) thường an toàn hơn.

> **Chuyển mạch:** Ở chặng này của **Recursion và quay lui (backtracking)**, **Tail recursion không phải lúc nào cũng tối ưu được** nêu điều cần giải thích; **cây traversal: recursion khớp shape dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **cây đệ quy và độ phức tạp (complexity / 복잡도)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cây traversal: recursion khớp shape dữ liệu

cây nhị phân vốn có recursive definition:

```text
Tree = empty
    hoặc Node(left Tree, value, right Tree)
```

Vì vậy traversal recursive gần như trực tiếp từ cấu trúc (structure / 구조):

```java
void inorder(Node x) {
    if (x == null) return;
    inorder(x.left);
    visit(x);
    inorder(x.right);
}
```

Ở đây recursion không phải trick; cách biểu diễn (representation / 표현) của dữ liệu (data / 데이터) đã recursive.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Recursion và quay lui (backtracking)**, **cây traversal: recursion khớp shape dữ liệu** nêu điều cần giải thích; **cây đệ quy và độ phức tạp (complexity / 복잡도)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **quay lui là DFS trên implicit đồ thị trạng thái/cây** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cây đệ quy và độ phức tạp (complexity / 복잡도)

Một hàm đệ quy không thể phân tích chỉ bằng độ sâu. Phải xem hệ số phân nhánh và công việc (work / 작업) mỗi nút.

Ví dụ naive Fibonacci:

```text
fib(n) = fib(n-1) + fib(n-2)
```

tạo cây đệ quy có rất nhiều lặp lại các trạng thái. độ phức tạp (complexity / 복잡도) exponential không phải vì recursion bản thân chậm, mà vì cùng subproblem được recompute nhiều lần.

Memoization biến trạng thái cây thành trạng thái DAG bằng cách reuse các kết quả.

> **Chuyển mạch:** Trong **Recursion và quay lui (backtracking)**, **quay lui là DFS trên implicit đồ thị trạng thái/cây** tiếp nhận điểm tựa từ **cây đệ quy và độ phức tạp (complexity / 복잡도)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Choose → Constrain → Explore → Undo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Recursion và quay lui (backtracking)**, **Choose → Constrain → Explore → Undo** tiếp nhận điểm tựa từ **quay lui là DFS trên implicit đồ thị trạng thái/cây** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Subsets: hệ số phân nhánh 2** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Trong mã (code / 코드) hệ thống thực tế, có ba chiến lược (strategy / 전략) để quản trạng thái:

```text
mutable + undo      -> ít allocation, dễ bug rollback
copy-on-recursion   -> đơn giản correctness, tốn memory/time
persistent state    -> structural sharing, implementation phức tạp hơn
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Recursion và quay lui (backtracking)**, **Subsets: hệ số phân nhánh 2** tiếp nhận điểm tựa từ **Choose → Constrain → Explore → Undo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Permutations và factorial growth** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Recursion và quay lui (backtracking)**, **Permutations và factorial growth** tiếp nhận điểm tựa từ **Subsets: hệ số phân nhánh 2** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pruning: loại cả cây con** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Permutations và factorial growth

Với `n` distinct items, số permutations là:

\[
n!
\]

Dù pruning/check cực nhanh, nếu phải đầu ra tất cả permutations thì độ phức tạp (complexity / 복잡도) ít nhất proportional `n!`.

quay lui không “làm exponential thành polynomial”. Nó giúp không gian tìm kiếm (search / 검색) được biểu diễn gọn và cho phép prune branches không cần thiết.

> **Chuyển mạch:** Ở chặng này của **Recursion và quay lui (backtracking)**, **Pruning: loại cả cây con** tiếp nhận điểm tựa từ **Permutations và factorial growth** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bitmask quay lui** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pruning: loại cả cây con

Nếu partial trạng thái đã không thể dẫn tới hợp lệ answer, các hậu duệ của nó không cần generate.

Ví dụ N-Queens: nếu queen mới xung đột (conflict / 충돌) với column hoặc diagonal đã dùng, toàn bộ placements tiếp theo dưới branch đó không hợp lệ.

Thay vì quét board mỗi lần, maintain các ràng buộc:

```text
usedColumn[c]
usedDiag1[r-c]
usedDiag2[r+c]
```

Check từ `O(n)` xuống gần `O(1)`.

Tốc độ tìm kiếm không chỉ phụ thuộc vào số nhánh mà còn phụ thuộc chi phí xác minh mỗi nhánh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Recursion và quay lui (backtracking)**, **Bitmask quay lui** tiếp nhận điểm tựa từ **Pruning: loại cả cây con** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **phần tử trùng điều khiển (control / 제어) phải gắn với trạng thái ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bitmask quay lui

Nếu `n` nhỏ, các ràng buộc có thể encode bằng bitmask.

N-Queens có thể giữ:

```text
columns
main diagonals
anti diagonals
```

và compute available positions bằng bit các thao tác. Điều này giảm constant factor rất mạnh và tránh set/băm (hash / 해시) cấp phát.

Nhưng bitmask không thay đổi trường hợp xấu nhất combinatorial nature; nó chỉ làm trạng thái chuyển tiếp (transition / 전이) rẻ hơn.

> **Chuyển mạch:** Trong **Recursion và quay lui (backtracking)**, **phần tử trùng điều khiển (control / 제어) phải gắn với trạng thái ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **Bitmask quay lui** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **quay lui cho Combination Sum** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## phần tử trùng điều khiển (control / 제어) phải gắn với trạng thái ngữ nghĩa (semantics / 의미론)

Giả sử đầu vào sorted có các phần tử trùng và ta generate combinations/permutations. quy tắc phổ biến:

```text
if (i > start && a[i] == a[i-1]) continue;
```

Điểm quan trọng là **skip phần tử trùng ở cùng recursion độ sâu**, vì hai equal các ứng viên tại cùng choice position tạo cùng cây con ngữ nghĩa (semantic / 의미적).

Nếu skip equal giá trị ở mọi độ sâu, ta có thể loại legitimate các lời giải có nhiều occurrences.

quy tắc chống phần tử trùng phải derive từ câu hỏi:

> Hai branches này có đại diện cùng quyết định (decision / 결정) tại trạng thái hiện tại hay không?

> **Chuyển mạch:** Ở chặng này của **Recursion và quay lui (backtracking)**, **quay lui cho Combination Sum** tiếp nhận điểm tựa từ **phần tử trùng điều khiển (control / 제어) phải gắn với trạng thái ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **N-Queens: trạng thái-space lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## quay lui cho Combination Sum

Nếu các ứng viên positive và có đích còn lại `remain`, ta có pruning monotonic:

```text
candidate > remain -> không cần thử candidate lớn hơn nữa
```

nếu các ứng viên sorted.

Nếu các giá trị có negative numbers, lập luận (reasoning / 추론) này vỡ. Một branch đang overshoot có thể quay lại bằng số âm.

Đây là ví dụ các giả định quyết định validity của pruning.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Recursion và quay lui (backtracking)**, **N-Queens: trạng thái-space lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **quay lui cho Combination Sum** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sudoku và ràng buộc propagation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## N-Queens: trạng thái-space lập luận (reasoning / 추론)

Thay vì đặt queen ở bất kỳ cell nào, ta có thể mô hình mỗi row đặt đúng một queen. Điều đó giảm branching không gian (space / 공간) ngay từ cách biểu diễn.

trạng thái tối thiểu chỉ cần:

```text
row hiện tại
occupied columns
occupied diagonals
```

Không nhất thiết giữ full board nếu chỉ cần count các lời giải.

Bài toán (problem / 문제) mô hình hóa tốt có thể quan trọng hơn micro-optimization trong DFS.

> **Chuyển mạch:** Trong **Recursion và quay lui (backtracking)**, **Sudoku và ràng buộc propagation** tiếp nhận điểm tựa từ **N-Queens: trạng thái-space lập luận (reasoning / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **thứ tự phân nhánh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sudoku và ràng buộc propagation

Sudoku solver naive thử digits 1..9 cho mọi rỗng cell. Tốt hơn là maintain ứng viên set của từng cell hoặc các mặt nạ hàng/cột/khối.

Một heuristic mạnh là chọn cell có **Minimum Remaining các giá trị (MRV)** — ít các ứng viên nhất.

Tại sao? Nếu branch sắp thất bại (fail / 실패), ta muốn thất bại (fail / 실패) sớm để prune cây con lớn.

Đây gọi là **fail-first principle** trong ràng buộc satisfaction.

> **Chuyển mạch:** Ở chặng này của **Recursion và quay lui (backtracking)**, **thứ tự phân nhánh** tiếp nhận điểm tựa từ **Sudoku và ràng buộc propagation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **quay lui và memoization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## thứ tự phân nhánh

Nếu chỉ cần một lời giải, thứ tự các ứng viên ảnh hưởng môi trường chạy mạnh dù trường hợp xấu nhất không đổi.

Các heuristics thường gồm:

```text
most constrained variable first
candidate có khả năng fail sớm
candidate có score tốt trước nếu branch-and-bound
```

Nếu cần enumerate toàn bộ các lời giải, thứ tự (ordering / 순서) chỉ thay chuỗi (sequence / 시퀀스) đầu ra, không giảm số hợp lệ các nút lá; pruning vẫn có thể giảm không hợp lệ các trạng thái.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Recursion và quay lui (backtracking)**, **quay lui và memoization** tiếp nhận điểm tựa từ **thứ tự phân nhánh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **quay lui khác quy hoạch động (dynamic programming) thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## quay lui và memoization

Nếu tương lai answer chỉ phụ thuộc một chuẩn gốc (canonical / 정본) trạng thái, nhiều histories có thể merge.

Ví dụ recursive coin thay đổi (change / 변경) có thể reach cùng trạng thái:

```text
(index, remainingAmount)
```

qua nhiều đường. Nếu solve(state) luôn cho cùng kết quả, memoization tránh recompute.

Lúc đó implicit cây thực chất là đồ thị với lặp lại các nút.

### Dấu hiệu nên nghĩ DP

Nếu bạn thấy cây đệ quy có nhiều calls với cùng parameters hoặc cùng lô-gic (logic / 논리) trạng thái, hãy hỏi:

> Lịch sử đi tới trạng thái này có còn ảnh hưởng tương lai không?

Nếu không, trạng thái có thể memoize.

> **Chuyển mạch:** Trong **Recursion và quay lui (backtracking)**, **quay lui khác quy hoạch động (dynamic programming) thế nào?** tiếp nhận điểm tựa từ **quay lui và memoization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **nhánh và cận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## quay lui khác quy hoạch động (dynamic programming) thế nào?

quay lui thường explore choices để tìm feasible/lời giải tối ưu và dựa mạnh vào pruning.

DP xác định các lớp tương đương của histories thành các trạng thái và reuse kết quả.

Một bài toán có thể dùng cả hai: quay lui để khám phá không gian cấu trúc, còn ghi nhớ (memoization) để hợp nhất các trạng thái lặp lại.

Không nên phân loại bằng cú pháp (syntax / 문법) “có recursion hay không”. Top-down DP cũng recursive.

> **Chuyển mạch:** Ở chặng này của **Recursion và quay lui (backtracking)**, **nhánh và cận** tiếp nhận điểm tựa từ **quay lui khác quy hoạch động (dynamic programming) thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Alpha-Beta như chuyên biệt pruning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## nhánh và cận

**nhánh và cận (분기 한정법)** mở rộng quay lui cho tối ưu hóa (optimization / 최적화). Ngoài feasibility pruning, ta tính optimistic bound của best kết quả có thể đạt từ partial trạng thái.

Nếu bound còn tệ hơn best lời giải đã biết, prune branch.

Ví dụ TSP chính xác solver có thể dùng cận dưới trên remaining tuyến (route / 경로) chi phí. Knapsack chính xác tìm kiếm (search / 검색) có thể dùng fractional-knapsack cận trên (upper bound).

Mô hình tư duy:

```text
backtracking      -> prune impossible branches
branch-and-bound  -> prune branches không thể beat incumbent
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Recursion và quay lui (backtracking)**, **Alpha-Beta như chuyên biệt pruning** tiếp nhận điểm tựa từ **nhánh và cận** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tường minh (explicit / 명시적) ngăn xếp (stack / 스택) thay recursion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Alpha-Beta như chuyên biệt pruning

Trong minimax game cây, alpha-beta pruning loại branches không thể ảnh hưởng final quyết định (decision / 결정) do hiện tại lower/các cận trên.

Nó là một ví dụ domain-specific của general idea: nếu partial thông tin đã chứng minh các hậu duệ không thể thay answer, skip whole cây con.

> **Chuyển mạch:** Trong **Recursion và quay lui (backtracking)**, **Tường minh (explicit / 명시적) ngăn xếp (stack / 스택) thay recursion** tiếp nhận điểm tựa từ **Alpha-Beta như chuyên biệt pruning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **C: quyền sở hữu (ownership / 소유권) và có thể thay đổi trạng thái** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tường minh (explicit / 명시적) ngăn xếp (stack / 스택) thay recursion

Deep đồ thị/cây có thể tràn số ngăn xếp lời gọi. Ta có thể mô phỏng recursion bằng tường minh (explicit / 명시적) ngăn xếp (stack / 스택).

Nhưng với quay lui, frame cần lưu nhiều trạng thái hơn chỉ nút:

```text
current state
next candidate index
data cần undo
```

Cú pháp đệ quy tự động lưu bộ đếm lệnh và biến cục bộ trong khung lời gọi; phiên bản dạng lặp phải biểu diễn các thông tin này một cách tường minh.

Đây là lý do iterative quay lui đôi khi phức tạp hơn iterative DFS đơn giản.

> **Chuyển mạch:** Ở chặng này của **Recursion và quay lui (backtracking)**, sau nội dung của **Tường minh (explicit / 명시적) ngăn xếp (stack / 스택) thay recursion**, **C: quyền sở hữu (ownership / 소유권) và có thể thay đổi trạng thái** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Java: collections và bản sao (copy / 복사) chi phí** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## C: quyền sở hữu (ownership / 소유권) và có thể thay đổi trạng thái

Trong C, hàm đệ quy cần rõ ai sở hữu các bộ đệm. Nếu mỗi lời gọi đệ quy `malloc` một trạng thái bản sao (copy / 복사), overhead lớn và dễ leak khi early return.

mẫu có thể thay đổi dùng chung (shared / 공유) các mảng + tường minh (explicit / 명시적) undo thường hiệu quả hơn, nhưng cần discipline:

```c
path[depth] = candidate;
used[candidate] = true;
search(depth + 1);
used[candidate] = false;
```

Nếu recursion có multiple exit các đường đi, cleanup phải nhất quán.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Recursion và quay lui (backtracking)**, **Java: collections và bản sao (copy / 복사) chi phí** tiếp nhận điểm tựa từ **C: quyền sở hữu (ownership / 소유권) và có thể thay đổi trạng thái** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **JavaScript: đối tượng sự thay đổi dữ liệu và recursion limit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Java: collections và bản sao (copy / 복사) chi phí

Trong Java, mẫu:

```java
ans.add(new ArrayList<>(path));
```

ở nút lá là bắt buộc nếu `path` tiếp tục mutate. Nếu thêm chính `path`, mọi các tham chiếu trong `ans` có thể cùng trỏ tới đối tượng đang bị thay đổi.

Đây là một bug bí danh bộ nhớ phổ biến.

> **Chuyển mạch:** Trong **Recursion và quay lui (backtracking)**, **Java: collections và bản sao (copy / 복사) chi phí** đã nêu tiêu chí phân biệt, còn **JavaScript: đối tượng sự thay đổi dữ liệu và recursion limit** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Độ phức tạp (complexity / 복잡도) của quay lui** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## JavaScript: đối tượng sự thay đổi dữ liệu và recursion limit

Trong JavaScript, các mảng/các đối tượng dùng tham chiếu ngữ nghĩa. `ans.push(path)` lưu tham chiếu; thường cần:

```js
ans.push([...path]);
```

cho snapshot.

Deep recursive tìm kiếm (search / 검색) còn có call-stack limit phụ thuộc engine. Với đầu vào độ sâu không kiểm soát, tường minh (explicit / 명시적) ngăn xếp (stack / 스택) hoặc iterative thiết kế (design / 설계) an toàn hơn.

> **Chuyển mạch:** Ở chặng này của **Recursion và quay lui (backtracking)**, **JavaScript: đối tượng sự thay đổi dữ liệu và recursion limit** đã nêu tiêu chí phân biệt, còn **Độ phức tạp (complexity / 복잡도) của quay lui** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **không gian tìm kiếm vs không gian lời giải** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ phức tạp (complexity / 복잡도) của quay lui

Một cách estimate tốt hơn chỉ nói “exponential” là:

\[
O(\text{number of visited states} \times \text{cost per state})
\]

Pruning giảm đã thăm các trạng thái. Better ràng buộc cách biểu diễn giảm chi phí/trạng thái. Memoization merge lặp lại các trạng thái. thứ tự phân nhánh có thể giúp tìm incumbent sớm để prune mạnh hơn.

Đây là decomposition thực dụng khi optimize solver.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Recursion và quay lui (backtracking)**, **không gian tìm kiếm vs không gian lời giải** tiếp nhận điểm tựa từ **Độ phức tạp (complexity / 복잡도) của quay lui** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phổ biến mistakes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## không gian tìm kiếm vs không gian lời giải

Không gian ứng viên có thể lớn hơn rất nhiều số hợp lệ các lời giải. Một good quay lui mô hình cố generate ít không hợp lệ trạng thái nhất có thể.

Ví dụ generate all `n^n` board configurations rồi kiểm N-Queens là vô lý; enforce one queen per row ngay từ mô hình trạng thái giảm không gian tìm kiếm trước cả pruning.

> **Chuyển mạch:** Trong **Recursion và quay lui (backtracking)**, **Phổ biến mistakes** tiếp nhận điểm tựa từ **không gian tìm kiếm vs không gian lời giải** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **kiểm thử quay lui** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phổ biến mistakes

**Quên hoàn tác thay đổi dữ liệu.** Nhánh sau sẽ thừa trạng thái của nhánh trước.

**Undo sai thứ tự.** Nếu mutations phụ thuộc nhau, restore phải đối xứng reverse thứ tự (order / 순서).

**trường hợp cơ sở quá sớm/quá muộn.** Có thể miss lời giải hoặc recurse ngoài bounds.

**Pruning không có chứng minh.** Có thể loại hợp lệ các lời giải.

**bản sao (copy / 복사) trạng thái quá nhiều.** Correct nhưng chậm/memory-heavy.

**Dùng toàn cục có thể thay đổi trạng thái nhưng không reset giữa runs.** kiểm thử (test / 테스트) riêng lẻ pass, batch thất bại (fail / 실패).

**Không xử lý các phần tử trùng đúng độ sâu.** Sinh phần tử trùng answers hoặc bỏ mất answers.

**Assume recursion luôn an toàn.** Deep đầu vào có thể ngăn xếp (stack / 스택) tràn số.

> **Chuyển mạch:** Ở chặng này của **Recursion và quay lui (backtracking)**, **kiểm thử quay lui** tiếp nhận điểm tựa từ **Phổ biến mistakes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy mở rộng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## kiểm thử quay lui

Với `n` nhỏ, so sánh đầu ra count với known combinatorial các giá trị:

```text
subsets -> 2^n
permutations distinct -> n!
```

Kiểm mỗi đầu ra thỏa các ràng buộc và không phần tử trùng nếu ngữ nghĩa yêu cầu unique.

Một kỹ thuật mạnh là dùng brute-force generator đơn giản làm oracle cho small `n`, rồi so sánh optimized pruning phiên bản (version / 버전).

Ngoài final answers, có thể assert trạng thái restored sau mỗi lời gọi đệ quy trong gỡ lỗi xây dựng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Recursion và quay lui (backtracking)**, **Mô hình tư duy mở rộng** gom các mảnh từ **kiểm thử quay lui** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy mở rộng

> Quay lui không phải “thử tất cả một cách mù quáng”. Nó là **thiết kế không gian tìm kiếm (search-space engineering)**: chọn cách biểu diễn trạng thái, thứ tự ứng viên, bất biến và cận sao cho có thể loại bỏ cả cây con càng sớm càng tốt mà vẫn không bỏ sót nghiệm.

Khi một bài toán (problem / 문제) có choices lồng nhau, hãy hỏi: trạng thái tối thiểu là gì, branch nào có thể prove impossible sớm, có lặp lại trạng thái để memoize không, và kích thước đầu ra itself có exponential không. Những câu hỏi đó quan trọng hơn việc nhớ một template recursion cụ thể.

> **Bàn giao:** Sau **Mô hình tư duy mở rộng**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
