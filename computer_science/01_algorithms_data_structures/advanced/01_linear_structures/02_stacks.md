# Ngăn xếp
**Ngăn xếp (Stack / 스택)**

Ngăn xếp mô hình hóa **vào sau, ra trước (LIFO — Last In, First Out / 후입선출)**: phần tử hoặc công việc được mở sau cùng phải được hoàn tất trước. Đây là một **kiểu dữ liệu trừu tượng (ADT — Abstract Data Type)** có giao diện rất nhỏ — `push`, `pop`, `peek`, `isEmpty` — nhưng xuất hiện ở khắp nơi: ngăn xếp lời gọi (call stack), DFS, bộ phân tích cú pháp (parser), hoàn tác/làm lại (undo/redo), tính biểu thức, quay lui (backtracking), cấu trúc đơn điệu và nhiều thuật toán cần lưu trạng thái để tiếp tục xử lý.

## 1. Ngăn xếp là một abstraction, không phải một implementation cụ thể

Ngăn xếp mô tả **hành vi** chứ không bắt buộc một cách lưu trữ. Nó có thể được cài đặt bằng **mảng động (dynamic array)** hoặc **danh sách liên kết (linked list)**.

Với mảng động:

```text
push -> thêm vào cuối
pop  -> giảm size và lấy phần tử cuối
peek -> a[size-1]
```

Với danh sách liên kết:

```text
push -> chèn ở đầu
pop  -> xóa ở đầu
```

Cả hai có thể cho `push/pop` `O(1)` theo hợp đồng phù hợp. Mảng động thường có **tính cục bộ bộ nhớ (locality)** tốt và ít lần cấp phát hơn. Danh sách liên kết không cần một vùng nhớ liên tục nhưng phải trả thêm chi phí node, con trỏ và cấp phát.

## 2. Ngăn xếp trong C, Java và JavaScript

Java hiện đại thường dùng `ArrayDeque` thay cho lớp `Stack` cũ:

```java
Deque<Integer> st = new ArrayDeque<>();
st.push(10);
st.push(20);
int top = st.peek();
int x = st.pop();
```

JavaScript có thể dùng `Array`:

```js
const st = [];
st.push(10);
st.push(20);
const x = st.pop();
```

C có thể dùng mảng động:

```c
typedef struct {
    int *a;
    size_t size;
    size_t cap;
} IntStack;
```

API cần định nghĩa rõ hành vi khi ngăn xếp rỗng: trả `boolean` kèm tham số đầu ra, giá trị đặc biệt (sentinel), `null`, ngoại lệ (exception) hay mã lỗi (error code).

## 3. Bất biến của ngăn xếp

Với ngăn xếp dựa trên mảng:

```text
0 <= size <= capacity
các phần tử logic = a[0 .. size)
phần tử đỉnh nếu tồn tại = a[size-1]
```

Mọi thao tác phải giữ **bất biến (invariant)** này. `pop` không nhất thiết phải xóa các byte vật lý; về logic chỉ cần giảm `size`. Tuy nhiên, nếu cấu trúc giữ tham chiếu tới object trong ngôn ngữ có GC, xóa tham chiếu ở ô cũ đôi khi giúp object trở thành không còn truy cập được sớm hơn.

## 4. Ghép cặp dấu ngoặc: lưu nghĩa vụ chưa hoàn tất

Một chuỗi dấu ngoặc hợp lệ vì dấu đóng gần nhất phải khớp dấu mở gần nhất chưa được đóng.

```js
function validBrackets(s) {
  const st = [];
  const pair = { ')': '(', ']': '[', '}': '{' };

  for (const ch of s) {
    if (ch === '(' || ch === '[' || ch === '{') st.push(ch);
    else if (ch in pair) {
      if (st.length === 0 || st.pop() !== pair[ch]) return false;
    }
  }
  return st.length === 0;
}
```

**Mô hình tư duy (mental model):** ngăn xếp lưu các **nghĩa vụ đang mở (open obligations)**. Dấu đóng mới phải giải quyết nghĩa vụ được tạo gần nhất trước.

## 5. Ngăn xếp lời gọi và đệ quy

Khi A gọi B và B gọi C:

```text
khung A
khung B
khung C <- đỉnh
```

C phải trả về trước B, B phải trả về trước A. Mỗi **khung lời gọi (stack frame)** lưu địa chỉ quay về, tham số, trạng thái cục bộ và metadata của runtime. Đệ quy (recursion) tự nhiên vì runtime đã cung cấp ngăn xếp. Nếu độ sâu phụ thuộc dữ liệu đầu vào và có thể rất lớn, dùng ngăn xếp tường minh (explicit stack) thường an toàn hơn.

## 6. Chuyển đệ quy thành ngăn xếp tường minh

DFS đệ quy:

```java
void dfs(int u) {
    seen[u] = true;
    for (int v : g[u]) if (!seen[v]) dfs(v);
}
```

DFS lặp:

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

Để mô phỏng **hậu thứ tự (postorder)** chính xác, một mục trong ngăn xếp thường phải giữ thêm giai đoạn hoặc chỉ số đang xử lý. Đệ quy không chỉ là “ngăn xếp chứa node”; mỗi khung còn giữ vị trí cần tiếp tục sau khi lời gọi con kết thúc.

## 7. Trạng thái tiếp tục (continuation state)

Một phép duyệt cây hậu thứ tự dạng lặp có thể lưu `(node, visitedChildrenFlag)` hoặc `(node, nextChildIndex)`. Điểm cốt lõi là ngăn xếp lời gọi thực chất lưu các **trạng thái tiếp tục (continuations)** — thông tin cần thiết để biết “sau khi bài toán con xong thì phải làm gì tiếp”. Khi chuyển đệ quy sang vòng lặp, cần xác định trạng thái tiếp tục chứ không chỉ đẩy tham số hàm vào ngăn xếp.

## 8. Tính biểu thức và ngăn xếp toán tử

Biểu thức `3 + 4 * 2` không thể tính đơn giản từ trái sang phải. Thuật toán Shunting-yard hoặc bộ phân tích theo **độ ưu tiên toán tử (operator precedence)** dùng ngăn xếp để trì hoãn các toán tử chưa đủ điều kiện xử lý. Khi toán tử mới có độ ưu tiên thấp hơn, các toán tử mạnh hơn ở đỉnh được lấy ra và xử lý trước.

## 9. Trung tố, hậu tố và tiền tố

Biểu thức hậu tố (postfix / Reverse Polish Notation) biến thứ tự ưu tiên thành thứ tự tường minh:

```text
3 4 2 * +
```

Quy trình: gặp toán hạng thì `push`; gặp toán tử thì lấy các toán hạng cần thiết, tính kết quả rồi `push` lại. Ở giai đoạn tính, hậu tố không cần giải quyết lại dấu ngoặc hay độ ưu tiên vì thứ tự đã được mã hóa trong biểu thức.

## 10. Quay lui và trạng thái hoàn tác

Quay lui (backtracking) thường có mẫu `chọn → áp dụng trạng thái → khám phá → hoàn tác`. Ngăn xếp lời gọi tự nhiên giữ lịch sử lựa chọn. Nếu viết dạng lặp, mỗi khung thường phải chứa trạng thái hiện tại, chỉ số lựa chọn tiếp theo và thông tin cần để hoàn tác. Lựa chọn mới nhất phải được hoàn tác trước khi quay lại lựa chọn cũ hơn.

## 11. Undo/Redo cần hai ngăn xếp

Một trình soạn thảo đơn giản có thể giữ `undoStack` và `redoStack`. Khi có hành động mới, đưa hành động vào `undoStack` và xóa `redoStack`. Khi hoàn tác, lấy hành động gần nhất khỏi `undoStack`, áp dụng thao tác nghịch đảo rồi đưa nó vào `redoStack`. Nếu lịch sử cho phép phân nhánh thành nhiều phiên bản, hai ngăn xếp không còn đủ; cách biểu diễn có thể phải chuyển sang cây bền vững (persistent tree) hoặc DAG.

## 12. Ngăn xếp đơn điệu

**Ngăn xếp đơn điệu (Monotonic Stack / 단조 스택)** giữ phần tử hoặc chỉ số theo một thứ tự đơn điệu. Ví dụ:

```js
function nextGreater(a) {
  const ans = Array(a.length).fill(-1);
  const st = [];
  for (let i = 0; i < a.length; i++) {
    while (st.length && a[st[st.length - 1]] < a[i]) ans[st.pop()] = a[i];
    st.push(i);
  }
  return ans;
}
```

Khi `a[i]` lớn hơn giá trị ở đỉnh, `a[i]` chính là ứng viên lớn hơn đầu tiên đã được xác định cho chỉ số đó, vì mọi vị trí ở giữa đã được xét mà không đủ lớn.

## 13. Vì sao ngăn xếp đơn điệu là O(n)?

Mỗi chỉ số được `push` đúng một lần và bị `pop` tối đa một lần. Tổng số thay đổi là `O(n)`. Đây là **phân tích khấu hao (amortized analysis)**: thấy `for + while` không đủ để kết luận `O(n²)`; cần đếm số lần mỗi phần tử thực sự có thể tham gia thao tác.

## 14. Hình chữ nhật lớn nhất trong histogram

Ngăn xếp tăng dần giữ các cột mà biên phải cuối cùng chưa được xác định. Khi gặp một cột thấp hơn, các cột cao hơn ở đỉnh biết rằng vị trí hiện tại là phần tử thấp hơn đầu tiên bên phải. Phần tử còn lại sau khi `pop` giúp xác định biên phía trái. Ngăn xếp ở đây lưu **các ứng viên chưa biết biên cuối cùng**.

## 15. Min Stack và trạng thái bổ sung

Muốn `getMin()` chạy `O(1)`, có thể lưu thêm ngăn xếp giá trị nhỏ nhất. Ta đổi thêm bộ nhớ để duy trì thông tin tổng hợp tăng dần (incremental aggregate), nhờ đó truy vấn rẻ hơn. Một biến thể khác lưu `(value, minSoFar)` ở mỗi mục; thao tác đơn giản hơn nhưng metadata bị lặp nhiều hơn.

## 16. Xây hàng đợi bằng hai ngăn xếp

`inStack` nhận `enqueue`, `outStack` cung cấp `dequeue`. Khi `outStack` rỗng, chuyển toàn bộ phần tử từ `inStack` sang `outStack`. Mỗi phần tử chỉ được chuyển số lần bị chặn nên chi phí khấu hao của thao tác hàng đợi là `O(1)`.

## 17. Ngăn xếp bền vững

Danh sách liên kết đơn bất biến (immutable singly linked list) tạo **tính bền vững phiên bản (persistence)** tự nhiên. `push` tạo node mới trỏ tới phiên bản cũ; `pop` trả về phần đuôi cũ. Các phiên bản chia sẻ cấu trúc (structural sharing) thay vì sao chép toàn bộ.

## 18. Tràn ngăn xếp và độ sâu đệ quy

Độ sâu đệ quy tối đa phụ thuộc kích thước stack của runtime, kích thước mỗi khung, compiler/JIT, biến cục bộ và công cụ gỡ lỗi. Nếu dữ liệu có thể tạo độ sâu `O(n)`, phiên bản lặp thường đáng cân nhắc dù phiên bản đệ quy dễ đọc hơn.

## 19. Đệ quy đuôi không đảm bảo bộ nhớ hằng số

Một số ngôn ngữ hoặc compiler tối ưu **lời gọi đuôi (tail-call optimization)** trong những điều kiện nhất định. Java không đảm bảo loại bỏ lời gọi đuôi như một hợp đồng ngữ nghĩa. Vì vậy không nên kết luận rằng đệ quy đuôi luôn dùng bộ nhớ `O(1)` nếu runtime không đảm bảo.

## 20. Bộ nhớ stack và vòng đời object cục bộ

Trong C, vòng đời object cấp phát trên stack kết thúc khi scope hoặc khung lời gọi kết thúc. Trả con trỏ tới biến cục bộ tạo con trỏ treo (dangling pointer). **Stack ADT** và **call stack của runtime** là hai khái niệm khác nhau dù cùng mang tính LIFO; một Stack ADT hoàn toàn có thể dùng heap.

## 21. Treiber Stack không khóa

Treiber Stack là ngăn xếp đồng thời dùng thao tác nguyên tử **so sánh và hoán đổi (CAS — compare-and-swap)** trên `head`. Phần khó nằm ở thu hồi bộ nhớ và **vấn đề ABA (ABA problem)**. Hazard pointer, epoch hoặc con trỏ gắn phiên bản có thể cần thiết. Tính đúng trong môi trường đồng thời không thể suy trực tiếp từ bất biến LIFO tuần tự.

## 22. Ngăn xếp giới hạn dung lượng

Nếu biết trước độ sâu tối đa, ngăn xếp có dung lượng cố định tránh được cấp phát và thay đổi kích thước. Khi đầy, API phải định nghĩa rõ hành vi. Hệ thống nhúng hoặc thời gian thực thường thích bộ nhớ giới hạn vì mức dùng bộ nhớ và độ trễ dễ dự đoán hơn.

## 23. Ngữ nghĩa lỗi và underflow

`pop` trên ngăn xếp rỗng là **underflow**. API có thể ném ngoại lệ, trả `Optional/null`, trả `boolean` kèm tham số đầu ra hoặc dùng assertion nếu đây là lỗi lập trình nội bộ. Lựa chọn phụ thuộc tầng abstraction và hợp đồng API.

## 24. Kiểm thử ngăn xếp

Cần kiểm tra thứ tự LIFO, `peek` không xóa phần tử, `size` chính xác và hành vi underflow. Có thể dùng **kiểm thử vi sai (differential testing)** để so cấu trúc tự viết với một cấu trúc tham chiếu. Thuật toán ngăn xếp đơn điệu nên được so với lời giải vét cạn `O(n²)` trên nhiều đầu vào nhỏ ngẫu nhiên.

## 25. Khi nào nhận ra một bài cần ngăn xếp?

Các tín hiệu thường gặp là cấu trúc lồng nhau, mở sau phải đóng trước, quay lui, DFS tường minh, phần tử lớn hơn/nhỏ hơn gần nhất, lịch sử undo, mô phỏng postorder và độ ưu tiên toán tử.

Câu hỏi hữu ích:

> “Có những công việc nào đã bắt đầu nhưng chưa hoàn tất, và công việc mới nhất có phải được hoàn tất trước không?”

Nếu có, ngăn xếp thường là mô hình tự nhiên.

## Mô hình tư duy

> Ngăn xếp là **bộ nhớ của những trạng thái tiếp tục hoặc nghĩa vụ chưa hoàn tất**, với quy tắc phần mới nhất được xử lý trước.

Từ ghép dấu ngoặc, đệ quy, parser, ngăn xếp đơn điệu đến undo, cùng một nguyên lý LIFO xuất hiện dưới nhiều hình thức. Ngăn xếp không chỉ giữ dữ liệu; nó còn giữ **trạng thái cần thiết để tiếp tục quá trình tính toán (computation)**.
