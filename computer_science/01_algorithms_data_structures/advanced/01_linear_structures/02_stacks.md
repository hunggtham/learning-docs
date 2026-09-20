# Stack
**Ngăn xếp (Stack / 스택)**

Stack mô hình hóa **LIFO — Last In, First Out / 후입선출**. Phần tử được đưa vào sau được lấy ra trước.

Stack là một ADT; implementation có thể bằng array, dynamic array hoặc linked list. API cốt lõi là `push`, `pop`, `peek`, `isEmpty`.

## Stack trong ba ngôn ngữ

Java hiện đại thường dùng `ArrayDeque` thay class `Stack` cũ:

```java
Deque<Integer> st = new ArrayDeque<>();
st.push(10);
st.push(20);
int x = st.pop();
```

JavaScript:

```js
const st = [];
st.push(10);
st.push(20);
const x = st.pop();
```

Trong C, dynamic array với `size` đủ để tạo stack; `push` append cuối, `pop` giảm `size`.

## Parentheses matching

Chuỗi `{[( )]}` hợp lệ vì closing bracket gần nhất phải đóng opening bracket gần nhất chưa được đóng. Đây chính là LIFO semantics.

```js
function validBrackets(s) {
  const st = [];
  const match = { ')': '(', ']': '[', '}': '{' };
  for (const ch of s) {
    if (ch === '(' || ch === '[' || ch === '{') st.push(ch);
    else if (ch in match && st.pop() !== match[ch]) return false;
  }
  return st.length === 0;
}
```

## Call stack và recursion

Runtime call stack cũng là LIFO. Khi function A gọi B rồi B gọi C, C phải return trước B, B return trước A. Vì vậy recursion có thể chuyển sang iterative algorithm bằng **explicit stack**.

## Monotonic stack

**Monotonic Stack / 단조 스택** giữ values hoặc indices theo thứ tự tăng/giảm để giải “nearest greater/smaller”. Với Next Greater Element, khi gặp value mới lớn hơn stack top, value đó chính là next greater cho các elements nhỏ hơn đang chờ.

Mặc dù có `while` bên trong loop, mỗi element chỉ push một lần và pop tối đa một lần, nên tổng work `O(n)`.

## Mental Model

> Stack là bộ nhớ cho những việc đã mở nhưng chưa hoàn tất. Việc mở gần nhất thường phải hoàn tất trước.

Parser, DFS, undo, expression evaluation và call stack đều là cùng một structural idea.

## Expression parsing và operator stack

Một parser toán học cần xử lý precedence. Với expression:

```text
3 + 4 * 2
```

nếu evaluate trái sang phải sẽ sai. Shunting-yard algorithm dùng operator stack để trì hoãn operator chưa được phép thực thi. `*` có precedence cao hơn `+`, nên nó được xử lý trước.

Stack ở đây biểu diễn **các obligations chưa hoàn tất**: operator đã thấy nhưng còn chờ operand/right context.

## Min-stack

Nếu cần `getMin()` trong `O(1)` cùng push/pop, chỉ scan stack khi hỏi min sẽ `O(n)`. Ta có thể lưu thêm stack minima:

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

Ta trả thêm memory để duy trì một aggregate incremental. Pattern này xuất hiện lại trong monotonic structures và augmented trees.

## Monotonic stack và “phần tử nào bị loại vĩnh viễn?”

Trong next greater element, khi gặp `x`, mọi indices trên stack có value `< x` đã tìm thấy câu trả lời. Sau khi pop, chúng không cần xuất hiện nữa. Chính việc mỗi element chỉ bị push một lần và pop một lần tạo `O(n)`.

Ví dụ histogram largest rectangle còn sâu hơn: increasing stack giữ bars có start boundary chưa xác định hoàn toàn; khi gặp bar thấp hơn, bars cao hơn biết right boundary và có thể tính area.

## C stack bằng dynamic array

```c
typedef struct {
    int *a;
    size_t size;
    size_t cap;
} IntStack;

bool push(IntStack *s, int x) {
    if (s->size == s->cap) {
        size_t nc = s->cap ? s->cap * 2 : 8;
        int *p = realloc(s->a, nc * sizeof *p);
        if (!p) return false;
        s->a = p;
        s->cap = nc;
    }
    s->a[s->size++] = x;
    return true;
}
```

Một stack linked-list cũng push/pop `O(1)`, nhưng dynamic array thường có locality và allocation behavior tốt hơn.

## Stack overflow không phải recursion “quá nhiều lần” theo một con số cố định

Maximum recursion depth phụ thuộc stack size và frame size. Một function có local arrays lớn có thể overflow ở depth nhỏ hơn function chỉ có vài scalars. Vì vậy với input-controlled depth, iterative explicit stack thường an toàn hơn.
