# DSA như một bài toán mô hình hóa
**Cấu trúc dữ liệu và thuật toán (Data Structures & Algorithms / 자료구조와 알고리즘)**

Một chương trình có thể nhìn như hai phần: **state** và **transformation**. State là dữ liệu đang tồn tại; transformation là các bước làm state đổi. Data structure quyết định shape của state, còn algorithm quyết định cách state tiến từ input tới output.

Giả sử hệ thống có một triệu tài khoản. Nếu operation chính là “tìm account theo id”, quét list từ đầu tới cuối là representation kém phù hợp. Nếu dùng hash table, ta trả thêm chi phí cho hashing, bucket và memory overhead để đổi lấy lookup trung bình gần hằng số. Nếu ngoài lookup còn cần “liệt kê account trong khoảng id”, balanced tree có thể phù hợp hơn vì nó giữ order.

## ADT trước implementation

**Kiểu dữ liệu trừu tượng (Abstract Data Type, ADT / 추상 자료형)** mô tả hành vi, không khóa implementation. Stack ADT có `push`, `pop`, `peek`, `isEmpty` và invariant LIFO. Nó có thể được implement bằng dynamic array hoặc linked list. Queue ADT có FIFO semantics và có thể implement bằng circular buffer, linked list hoặc deque.

Trong Java, `Deque<E>` là interface/abstraction, còn `ArrayDeque<E>` là implementation. Trong C, ta thường tự định nghĩa `struct` và function contract. Trong JavaScript, `Array` có thể được dùng làm stack qua `push()` và `pop()` dù runtime representation không phải C array thuần túy.

## Từ nghiệp vụ đến operations

Một cách thiết kế tốt là không hỏi “dùng cấu trúc gì?” trước, mà hỏi workload là gì. Ví dụ hệ thống chat cần `append(message)`, `getRecent(k)`, `searchById(id)` và `delete(id)`. Nếu append và recent-read chiếm phần lớn traffic, structure cần tối ưu hai operation đó trước.

Có thể hình dung expected cost:

\[
E[C]=\sum_i p_iC_i
\]

trong đó `p_i` là tần suất tương đối của operation và `C_i` là cost của nó. Đây không phải công thức bắt buộc khi coding, mà là mental model để hiểu rằng performance chỉ có ý nghĩa trong workload.

## Representation, invariant và operation

Mọi data structure hữu ích đều có một **bất biến (Invariant / 불변식)**. Binary Search Tree giữ quy tắc keys ở left subtree nhỏ hơn node và keys ở right subtree lớn hơn node. Min-heap giữ parent không lớn hơn children. Hash table giữ mapping giữa key và bucket theo hash policy.

Ta có chuỗi reasoning:

```text
representation
    ↓
invariant
    ↓
operations có thể thực hiện
    ↓
complexity và trade-off
```

Nếu invariant bị phá, structure có thể vẫn “trông giống” tree hoặc heap nhưng không còn hỗ trợ đúng guarantees.

## DSA và phần cứng

Big-O không kể toàn bộ câu chuyện. Array traversal thường tận dụng cache locality vì elements gần nhau trong memory. Linked list cũng có traversal `O(n)` nhưng pointer chasing có thể gây nhiều cache miss. Hash table lookup expected `O(1)` nhưng constant factor phụ thuộc hash function, load factor và allocation layout.

Vì vậy nên giữ hai tầng suy luận: **asymptotic model** để hiểu growth theo `n`, và **machine/runtime model** để hiểu chi phí thực tế.

## Mental Model

> Data structure là một hợp đồng về shape của state. Algorithm là một hợp đồng về cách state thay đổi. Complexity là giá phải trả để duy trì các hợp đồng đó.

DSA xuất hiện trực tiếp trong production: database index dùng B-tree/B+tree; scheduler dùng priority queue; routing là graph; LRU cache ghép hash map với doubly linked list; autocomplete dùng trie/prefix index; Git commit history có graph structure; dependency resolution dùng topological sorting.

Xem tiếp: [Correctness & Invariants](./01_algorithm_correctness_and_invariants.md), [Complexity](./02_complexity_analysis.md), [Memory Model](./03_memory_models_c_java_javascript.md).
