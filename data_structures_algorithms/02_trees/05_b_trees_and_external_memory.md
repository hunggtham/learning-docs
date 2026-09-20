# B-Tree, B+Tree và cấu trúc dữ liệu cho External Memory  
**B-Tree / B+Tree / B 트리와 외부 메모리 자료구조**

Binary search tree giả định một node access có chi phí gần giống nhau. Trên SSD/HDD hoặc storage page, assumption đó sai: đọc một page có cost lớn hơn nhiều so với vài chục comparisons trong RAM. Vì vậy ta muốn **mỗi I/O mang về thật nhiều useful keys** và giảm số tầng phải đọc.

## Từ binary tree đến multiway tree

Binary tree có fan-out tối đa 2. B-tree node có thể chứa nhiều keys và nhiều children:

```text
[ 10 | 20 | 35 ]
 /     |     |    \
<10 10..20 20..35 >35
```

Nếu một node vừa đúng kích thước một storage page, một page read cho phép chọn trong hàng trăm children. Height vì thế cực nhỏ ngay cả khi index có hàng triệu records.

Nếu branching factor là `B`, height xấp xỉ:

\[
O(\log_B n)
\]

Sự khác biệt giữa `log_2 n` và `log_200 n` có ý nghĩa thực tế lớn khi mỗi level là I/O.

## B-tree invariant

B-tree duy trì sorted keys trong node, bounded number of keys/children và mọi leaves ở cùng depth. Insert có thể làm node overflow; khi đó split node và đẩy separator key lên parent. Delete có thể gây underflow; structure borrow từ sibling hoặc merge nodes để phục hồi occupancy invariant.

Do rebalancing xảy ra theo path root-leaf, search/insert/delete cần số page accesses logarithmic theo fan-out.

## B+Tree

B+Tree tách routing và records rõ hơn. Internal nodes chủ yếu lưu separator keys; records hoặc pointers tới records nằm ở leaves. Leaves thường linked theo thứ tự.

Điều này đặc biệt tốt cho range scan:

```sql
WHERE created_at BETWEEN :from AND :to
```

Engine tìm leaf đầu bằng tree search, sau đó scan linked leaves tuần tự thay vì quay lại root cho từng key.

## Clustered và secondary index — connection tới database

Một database có thể tổ chức table theo clustered index hoặc lưu secondary index từ key tới row locator. Chi tiết khác nhau giữa engines, nhưng DSA idea không đổi: index biến lookup/range selection từ full scan thành traversal qua ordered structure.

Index không miễn phí. Mỗi insert/update/delete có thể cần bảo trì tree, split page, logging và concurrency coordination. Vì vậy tạo index là trade-off giữa read performance, write cost và storage.

## Tại sao không dùng hash table cho mọi index?

Hash index mạnh với equality:

```text
key = X
```

nhưng không giữ order, nên query kiểu:

```text
key >= L AND key <= R
ORDER BY key
MIN/MAX
prefix-like ordered scan
```

không được hỗ trợ tự nhiên như B+Tree.

## Cache-oblivious insight

External-memory algorithms nhắc ta rằng Big-O theo số primitive operations chưa đủ. Có model đo block transfers. Một thuật toán làm nhiều arithmetic nhưng ít cache misses có thể thắng thuật toán có ít operations nhưng memory access rải rác.

Đây nối trực tiếp với [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md).

## Mental Model

> B-tree không cố giảm số comparisons tối đa; nó cố giảm **số lần phải đi tới một tầng storage đắt tiền** bằng cách tăng fan-out của mỗi node.

Khi cost model đổi, data structure tối ưu cũng đổi.
