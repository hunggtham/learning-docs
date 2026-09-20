# Stack
**Ngăn xếp (Stack / 스택)**

Stack mô hình hóa **LIFO — Last In, First Out / 후입선출**: phần tử hoặc công việc được mở sau cùng phải được hoàn tất trước. Đây là một ADT rất đơn giản về API — `push`, `pop`, `peek`, `isEmpty` — nhưng xuất hiện khắp nơi: call stack, DFS, parser, undo/redo, expression evaluation, backtracking, monotonic structures và nhiều algorithm dùng explicit continuation state.

## 1. Stack là abstraction, không phải một implementation cụ thể

Stack có thể được implement bằng dynamic array hoặc linked list.

Dynamic array:

```text
push -> append cuối
pop  -> giảm size
peek -> a[size-1]
```

Linked stack:

```text
push -> insert head
pop  -> remove head
```

Cả hai cho `push/pop` `O(1)` theo contract thích hợp, nhưng dynamic array thường có locality tốt hơn và ít allocation hơn; linked stack có stable nodes và không cần contiguous growth.

## 2. Stack trong C, Java và JavaScript

Java hiện đại thường dùng `ArrayDeque` thay legacy `Stack`:

```java
Deque<Integer> st = new ArrayDeque<>();
st.push(10);
st.push(20);
int top = st.peek();
int x = st.pop();
```

JavaScript:

```js
const st = [];
st.push(10);
st.push(20);
const x = st.pop();
```

C có thể dùng dynamic array:

```c
typedef struct {
    int *a;
    size_t size;
    size_t cap;
} IntStack;
```

Stack API nên định nghĩa rõ empty behavior: trả boolean + out parameter, sentinel, `null`, exception hay error code.

## 3. Stack invariant

Với array-backed stack:

```text
0 <= size <= capacity
logical elements = a[0 .. size)
top nếu có = a[size-1]
```

Mọi operation phải giữ invariant này. `pop` không cần erase physical bytes nếu semantics không yêu cầu; chỉ giảm logical size. Nhưng nếu stack giữ object references trong GC language/custom container, clear slot cũ đôi khi giúp object trở nên unreachable sớm hơn.

## 4. Parentheses Matching: obligations chưa hoàn tất

Chuỗi bracket hợp lệ vì closing bracket gần nhất phải khớp opening bracket gần nhất chưa đóng.

```js
function validBrackets(s) {
  const st = [];
  const pair = { ')': '(', ']': '[', '}': '{' };

  for (const ch of s) {
    if (ch === '(' || ch === '[' || ch === '{') {
      st.push(ch);
    } else if (ch in pair) {
      if (st.length === 0 || st.pop() !== pair[ch]) return false;
    }
  }

  return st.length === 0;
}
```

Mental model: stack lưu các **obligations đang mở**. Closing token phải giải quyết obligation mới nhất trước.

## 5. Call Stack và Recursion

Khi A gọi B, B gọi C:

```text
A frame
B frame
C frame <- top
```

C phải return trước B, B trước A. Mỗi frame lưu return address, parameters/local state và metadata runtime.

Recursion tự nhiên vì runtime đã cung cấp stack. Nhưng khi depth phụ thuộc input và có thể rất lớn, explicit stack thường an toàn hơn.

## 6. Chuyển recursion thành explicit stack

Recursive DFS:

```java
void dfs(int u) {
    seen[u] = true;
    for (int v : g[u]) {
        if (!seen[v]) dfs(v);
    }
}
```

Iterative preorder-like DFS:

```java
Deque<Integer> st = new ArrayDeque<>();
st.push(start);

while (!st.isEmpty()) {
    int u = st.pop();
    if (seen[u]) continue;
    seen[u] = true;

    for (int i = g[u].size() - 1; i >= 0; --i) {
        int v = g[u].get(i);
        if (!seen[v]) st.push(v);
    }
}
```

Nhưng để mô phỏng **postorder** chính xác, stack entry thường phải giữ thêm phase/index. Recursion không chỉ là “stack chứa node”; frame còn chứa vị trí tiếp tục sau khi child return.

## 7. Explicit continuation state

Một iterative tree postorder có thể lưu:

```text
(node, visitedChildrenFlag)
```

hoặc:

```text
(node, nextChildIndex)
```

Đây là insight quan trọng: call stack là stack của **continuations** — thông tin cần để biết “sau khi subproblem xong thì làm gì tiếp”.

Khi convert recursion sang iterative, hãy xác định continuation state, không chỉ push arguments.

## 8. Expression Evaluation và Operator Stack

Expression:

```text
3 + 4 * 2
```

không thể evaluate đơn giản trái sang phải. Shunting-yard hoặc operator-precedence parser dùng stack để trì hoãn operators chưa thể resolve.

Operator stack lưu:

```text
operator đã thấy
nhưng còn chờ precedence/parenthesis/right operand
```

Khi operator mới có precedence thấp hơn, các operators mạnh hơn trên stack được pop/evaluate trước.

## 9. Infix, Postfix và Prefix

Postfix (Reverse Polish Notation) biến precedence thành order tường minh:

```text
3 4 2 * +
```

Evaluation:

1. gặp operand -> push;
2. gặp operator -> pop operands cần thiết;
3. compute;
4. push result.

Stack loại nhu cầu parentheses/precedence trong evaluation phase vì expression đã encode order.

## 10. Backtracking và undo state

Backtracking thường có pattern:

```text
choose
push/apply state
explore
pop/undo state
```

Call stack tự nhiên giữ choice history. Nếu viết iterative, ta cần explicit frame chứa:

```text
state
next choice index
undo information
```

Stack phù hợp vì choice mới nhất phải được undo trước khi quay lại choice cũ.

## 11. Undo/Redo cần hai stacks

Một editor đơn giản có thể giữ:

```text
undoStack
redoStack
```

Action mới:

```text
push undo
clear redo
```

Undo:

```text
pop undo
apply inverse
push redo
```

Redo làm chiều ngược lại. Đây là composition của hai LIFO histories.

Nếu cần branching history/version graph, hai stacks không còn đủ; representation phải tiến lên persistent tree/DAG.

## 12. Monotonic Stack

**Monotonic Stack / 단조 스택** giữ elements/indices theo một order đơn điệu. Ví dụ Next Greater Element:

```js
function nextGreater(a) {
  const ans = Array(a.length).fill(-1);
  const st = []; // indices, values decreasing

  for (let i = 0; i < a.length; i++) {
    while (st.length && a[st[st.length - 1]] < a[i]) {
      ans[st.pop()] = a[i];
    }
    st.push(i);
  }

  return ans;
}
```

Khi `a[i]` lớn hơn stack top, `i` là first greater candidate đã được xác định cho top vì mọi index giữa đã được xử lý mà không đủ lớn.

## 13. Vì sao monotonic stack O(n) dù có nested while?

Mỗi index:

```text
push đúng 1 lần
pop tối đa 1 lần
```

Tổng stack mutations `O(n)`. Đây là amortized analysis điển hình.

Nhìn syntax có `for + while` nhưng không thể kết luận `O(n²)` nếu mỗi element bị loại vĩnh viễn sau một lần pop.

## 14. Largest Rectangle in Histogram

Increasing stack giữ bars có left boundary tiềm năng chưa bị một bar thấp hơn chặn.

Khi gặp height thấp hơn, các bars cao hơn trên stack biết rằng current index là first smaller bên phải. Node mới trên stack sau pop xác định smaller boundary bên trái.

Area:

\[
height \times width
\]

Technique này minh họa monotonic stack như một structure lưu **candidates chưa biết boundary cuối cùng**.

## 15. Min Stack và augmented state

Muốn `getMin()` `O(1)` có thể lưu thêm minima stack:

```java
class MinStack {
    Deque<Integer> values = new ArrayDeque<>();
    Deque<Integer> mins = new ArrayDeque<>();

    void push(int x) {
        values.push(x);
        if (mins.isEmpty() || x <= mins.peek()) mins.push(x);
    }

    int pop() {
        int x = values.pop();
        if (x == mins.peek()) mins.pop();
        return x;
    }

    int min() { return mins.peek(); }
}
```

Ta trả extra memory để duy trì aggregate incremental. Pattern này giống augmented tree: lưu đủ summary để query rẻ hơn.

Một biến thể lưu tại mỗi entry `(value, minSoFar)`; push/pop đơn giản hơn nhưng duplicate metadata nhiều hơn.

## 16. Stack with lazy deletion / two-stack transformations

Nhiều structures có thể được xây từ stacks.

Queue bằng hai stacks:

```text
inStack  nhận enqueue
outStack cung cấp dequeue
```

Khi `outStack` rỗng, chuyển toàn bộ `inStack` sang `outStack`. Mỗi element chuyển tối đa một lần qua lại theo phase, cho amortized `O(1)` queue operations.

Đây là ví dụ stack + amortized analysis tạo ADT khác.

## 17. Persistent Stack

Immutable singly linked stack có persistence gần như miễn phí:

```text
newTop -> oldTop -> ...
```

Push tạo node mới trỏ version cũ; pop trả tail cũ. Các versions share structure.

Trong functional programming, stack/list persistent là primitive quan trọng vì update không phá history.

## 18. Stack overflow và depth không có một con số cố định

Maximum recursion depth phụ thuộc:

```text
native/runtime stack size
frame size
compiler/JIT behavior
local variables
debug instrumentation
```

Một function có large local buffer có thể overflow sớm hơn function nhỏ.

Nếu input adversarial có depth `O(n)`, iterative version thường đáng cân nhắc dù recursion đẹp hơn.

## 19. Tail recursion không phải portable stack guarantee

Một số language/compiler có tail-call optimization trong điều kiện nhất định; Java không đảm bảo tail-call elimination như một semantic contract. JavaScript specification/runtime support cũng không nên được giả định đồng nhất cho production portability.

Vì vậy đừng dựa vào “đây là tail recursion” để kết luận stack usage constant nếu runtime không đảm bảo.

## 20. Stack memory và local object lifetime

Trong C, stack-allocated object lifetime kết thúc khi scope/frame kết thúc. Trả pointer tới local variable là invalid.

```c
int *bad(void) {
    int x = 10;
    return &x; // dangling pointer
}
```

“Stack” data structure và “call stack memory” là hai khái niệm liên quan LIFO nhưng không giống nhau. Một stack ADT có thể được allocate trên heap; call stack là runtime execution structure.

## 21. Lock-free Treiber Stack

Một concurrent stack kinh điển là Treiber stack dùng atomic compare-and-swap trên head pointer. Logical algorithm rất ngắn:

```text
read oldHead
new.next = oldHead
CAS(head, oldHead, new)
retry nếu fail
```

Nhưng memory reclamation và ABA problem làm production correctness khó. Hazard pointers/epochs/tagged pointers có thể cần thiết.

Điều này nhắc rằng concurrent correctness không thể suy từ sequential LIFO invariant một mình.

## 22. Bounded Stack và memory predictability

Nếu max depth biết trước, fixed-capacity stack có thể tránh allocation/resizing:

```text
array[capacity]
size
```

Push khi full phải định nghĩa behavior. Embedded/real-time systems thường thích bounded storage để memory và latency predictable.

## 23. Error semantics và underflow

`pop` trên empty stack là underflow. API có thể:

```text
throw exception
return optional/null
return boolean + out parameter
assert programmer error
```

Không có lựa chọn duy nhất; đúng hay sai phụ thuộc abstraction layer. Internal algorithm stack có thể assert invariant “không bao giờ pop empty”, trong khi public container API cần xử lý input robust hơn.

## 24. Testing Stack

Public behavior:

```text
push a,b,c -> pop c,b,a
peek không remove
size đúng
underflow đúng contract
```

Random differential test có thể so custom stack với reference dynamic array.

Monotonic stack algorithms nên so với `O(n²)` brute force trên random arrays nhỏ. Parser stack nên test malformed nesting, unary operators, empty expressions và precedence ties.

## 25. Khi nào nhận ra một bài cần Stack?

Các tín hiệu mạnh:

```text
nested structure
last-opened-first-closed
need to backtrack
explicit DFS
nearest greater/smaller
undo history
postorder simulation
operator precedence
```

Câu hỏi tốt là:

> “Có những công việc nào đã bắt đầu nhưng chưa hoàn tất, và công việc mới nhất có phải cần hoàn tất trước không?”

Nếu có, stack thường là model tự nhiên.

## Mental Model

> Stack là **bộ nhớ của những continuation/obligation chưa hoàn tất**, với quy tắc phần mới nhất được xử lý trước.

Từ parenthesis matching tới recursion, parser, monotonic stack và undo, cùng một LIFO principle xuất hiện dưới nhiều hình thức. Khi chuyển giữa recursive và iterative reasoning, hãy nghĩ stack không chỉ giữ data — nó giữ cả **trạng thái cần để tiếp tục computation**.

Xem thêm: [Queues/Deque](./03_queues_deques_and_priority_queues.md), [Recursion & Backtracking](../04_algorithmic_paradigms/02_recursion_and_backtracking.md), [Graph Traversal](../03_graphs/01_graph_traversal_bfs_dfs.md).