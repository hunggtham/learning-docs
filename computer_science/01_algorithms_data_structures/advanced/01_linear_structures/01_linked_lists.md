# Danh sách liên kết
**danh sách liên kết / 연결 리스트**

danh sách liên kết tách **thứ tự logic** khỏi **vị trí vật lý trong bộ nhớ**. mảng nói “phần tử thứ `i` nằm ở offset tính được”; danh sách liên kết nói “phần tử tiếp theo nằm ở nơi `next` chỉ tới”. Chính lựa chọn cách biểu diễn (representation) này tạo ra toàn bộ sự đánh đổi (trade-off): cục bộ rewiring rẻ, nhưng truy cập ngẫu nhiên và tính cục bộ (locality) kém.

## 1. danh sách liên kết đơn

```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```

cách biểu diễn:

```text
head
 ↓
[10|•] -> [20|•] -> [30|null]
```

Muốn tới nút thứ `i` phải follow `i` links, nên access theo index là `O(n)`. Không tồn tại phép tính địa chỉ trực tiếp như mảng.

## 2. Insert O(1) chỉ đúng khi đã biết vị trí cục bộ

Push đầu:

```c
Node *push_front(Node *head, int value) {
    Node *node = malloc(sizeof *node);
    if (!node) return head;
    node->value = value;
    node->next = head;
    return node;
}
```

Nối lại con trỏ chỉ cần số thao tác hằng. Nhưng nếu yêu cầu là “chèn trước phần tử có giá trị X”, ta vẫn phải tìm X trước, có thể tốn `O(n)`.

Một lỗi reasoning phổ biến là nói “danh sách liên kết insert O(1)” mà bỏ qua chi phí tìm vị trí. Complexity phải tính **toàn bộ thao tác contract**, không chỉ con trỏ cập nhật cuối.

## 3. Tail con trỏ thay đổi append chi phí

Nếu list chỉ giữ `head`, append cuối cần traverse `O(n)`. Nếu giữ thêm `tail`, append có thể `O(1)`:

```text
head -> ... -> tail
```

Nhưng thêm `tail` tạo thêm bất biến (invariant) phải duy trì:

```text
empty => head == null && tail == null
non-empty => tail.next == null
```

siêu dữ liệu giúp thao tác nhanh hơn nhưng tăng burden tính đúng đắn.

## 4. Delete và predecessor problem

Trong danh sách liên kết đơn, để xóa `cur`, ta thường cần `prev`:

```text
prev.next = cur.next
```

Nếu chỉ có con trỏ tới `cur`, không có cách tổng quát đi lùi về predecessor trong `O(1)`.

Một trick khi được phép thay đổi giá trị là copy data từ `cur.next` vào `cur` rồi bỏ nút sau, nhưng không hoạt động cho tail và phá định danh nút. Nó là problem-specific hack chứ không thay đổi limitation cơ bản của singly list.

## 5. danh sách liên kết đôi (Doubly Linked List)

Doubly list lưu cả `prev` và `next`:

```java
class Node<E> {
    E value;
    Node<E> prev;
    Node<E> next;
}
```

Nếu đã có tham chiếu tới nút, detach `O(1)`:

```text
node.prev.next = node.next
node.next.prev = node.prev
```

Đổi lại mỗi nút tốn thêm con trỏ/tham chiếu, sự thay đổi dữ liệu phải cập nhật nhiều links hơn và corruption có nhiều dạng hơn.

## 6. Sentinel các nút làm bất biến đơn giản hơn

Thay vì `head == null`/`tail == null` và rất nhiều trường hợp đặc biệt, doubly list có thể dùng hai giá trị canh gác (sentinel):

```text
HEAD <-> ... <-> TAIL
```

List rỗng:

```text
HEAD.next == TAIL
TAIL.prev == HEAD
```

Insert/remove giữa hai các nút luôn cùng mẫu. Sentinel không làm thuật toán asymptotically nhanh hơn; nó làm **không gian trạng thái của các trường hợp biên (edge cases) nhỏ hơn**, từ đó tính đúng đắn dễ hơn.

## 7. Circular danh sách liên kết

Trong circular list, tail nối lại head:

```text
A -> B -> C
^         |
|_________|
```

Nó phù hợp lập lịch luân phiên, cyclic các bộ đệm logic, Josephus-like problems hoặc intrusive queues.

Nhưng traversal không thể dùng `while (p != NULL)`. Termination điều kiện phải dựa vào quay lại start hoặc số bước. cách biểu diễn thay đổi bất biến vòng lặp.

## 8. Reverse danh sách liên kết và bất biến vòng lặp

```c
Node *reverse(Node *head) {
    Node *prev = NULL;
    Node *cur = head;

    while (cur != NULL) {
        Node *next = cur->next;
        cur->next = prev;
        prev = cur;
        cur = next;
    }
    return prev;
}
```

bất biến hữu ích:

> `prev` là reverse đúng của prefix đã xử lý; `cur` là head của suffix chưa xử lý; hai phần không overlap và hợp lại chứa đúng toàn bộ các nút ban đầu.

`next` phải được lưu trước khi phá `cur->next`; nếu không ta mất đường tới suffix.

## 9. Floyd phát hiện chu trình

Dùng `slow` đi 1 bước, `fast` đi 2 bước. Nếu có chu trình, hai con trỏ sẽ gặp nhau.

Tại sao? Sau khi cả hai vào chu trình, khoảng cách modulo chu trình length thay đổi 1 mỗi iteration, nên cuối cùng bằng 0.

Sau khi gặp, có thể tìm chu trình mục bằng cách đưa một con trỏ về head rồi cho cả hai đi cùng tốc độ; chúng gặp lại ở mục.

Kỹ thuật này khai thác arithmetic trên khoảng cách trong chu trình, không cần extra hash set.

## 10. nút giữa và k-th from end bằng relative-speed các con trỏ

Fast/slow không chỉ cho phát hiện chu trình. Nếu `fast` đi 2 còn `slow` đi 1, khi fast tới cuối, slow gần middle.

Muốn nút thứ k từ cuối, giữ hai các con trỏ cách nhau `k` các nút. Khi con trỏ trước tới cuối, con trỏ sau chính là answer.

Mô hình tư duy: danh sách liên kết không hỗ trợ truy cập ngẫu nhiên theo chỉ số, nhưng **khoảng cách tương đối giữa các con trỏ** có thể mã hóa thông tin vị trí.

## 11. Merge sorted linked lists

Hai các danh sách đã sắp xếp có thể merge tuyến tính bằng cách luôn lấy head nhỏ hơn. Sentinel nút đầu giả giúp code gọn:

```java
Node dummy = new Node(0);
Node tail = dummy;

while (a != null && b != null) {
    if (a.value <= b.value) {
        tail.next = a;
        a = a.next;
    } else {
        tail.next = b;
        b = b.next;
    }
    tail = tail.next;
}

tail.next = (a != null) ? a : b;
return dummy.next;
```

Đây là kết hợp primitive của linked-list sắp xếp trộn.

## 12. sắp xếp trộn trên danh sách liên kết

danh sách liên kết không có truy cập ngẫu nhiên tốt, nên Quicksort/index-based strategies kém tự nhiên. sắp xếp trộn lại rất hợp:

1. tìm midpoint bằng slow/fast;
2. split list;
3. recursively sort hai nửa;
4. merge bằng rewiring các nút.

Time `O(n log n)`. bộ đệm mảng bổ sung không cần; merge có thể relink các nút. Tuy nhiên ngăn xếp đệ quy vẫn tồn tại.

## 13. Splice là thế mạnh thật sự của linked structures

Nếu đã biết các ranh giới, có thể chuyển cả một đoạn list sang vị trí khác bằng vài con trỏ các cập nhật mà không move từng phần tử.

Đây là thao tác khó thực hiện hiệu quả trên mảng liên tiếp. Danh sách nội tại, nhân hệ điều hành và một số bộ lập lịch dùng cấu trúc dựa trên nút vì **nối lại liên kết** quan trọng hơn truy cập theo chỉ số.

## 14. LRU bộ nhớ đệm: composition thay vì một cấu trúc đơn lẻ

LRU cần:

```text
lookup key nhanh
move accessed item lên đầu nhanh
evict least-recent item nhanh
```

bảng ánh xạ băm giải tra cứu, danh sách liên kết đôi giải recency order.

```text
HashMap<key, Node>
HEAD <-> most recent ... least recent <-> TAIL
```

`get`:

1. map tra cứu kỳ vọng `O(1)`;
2. detach nút `O(1)`;
3. attach sau HEAD `O(1)`.

Không có ánh xạ thì tìm trong danh sách tốn `O(n)`. Không có danh sách thì ánh xạ không biết phần tử nào ít được sử dụng gần đây nhất. Đây là ví dụ quan trọng của **phối hợp nhiều cấu trúc dữ liệu (data-structure composition)**.

## 15. định danh nút và ổn định address

Một lợi thế cấu trúc dựa trên nút là nút có identity riêng. Nếu nút cấp phát không đổi, con trỏ/tham chiếu tới nút có thể giữ ổn định qua nhiều insert khác nơi khác.

mảng động grow có thể không hợp lệ raw các con trỏ/iterators do relocation. danh sách liên kết thường không di chuyển các nút còn tồn tại.

Nếu API cần ổn định handles, intrusive các tham chiếu hoặc long-lived iterator ngữ nghĩa (semantics), đây có thể là lý do dùng cấu trúc dựa trên nút dù tính cục bộ kém.

## 16. C: quyền sở hữu (ownership) là phần của cấu trúc dữ liệu

nút chứa giá trị trực tiếp hay con trỏ?

```text
list owns node, borrows value
list owns node và value
list stores copied value
```

Ngữ nghĩa của hàm hủy phải rõ ràng. Nếu giá trị là đối tượng trên heap do danh sách sở hữu, khi xóa nút phải gọi hàm hủy hoặc giải phóng giá trị. Nếu giá trị chỉ được mượn, giải phóng nó có thể gây lỗi giải phóng hai lần (double-free).

Trong C, logic bất biến và vòng đời (lifetime) bất biến phải đúng đồng thời.

## 17. Java/JavaScript: GC không xóa semantic quyền sở hữu

GC chỉ thu hồi đối tượng không còn có thể tới. Nếu ứng dụng giữ tham chiếu tới nút đã remove, nút và đồ thị đối tượng phía sau vẫn sống.

Một bug kiểu:

```text
remove node khỏi list
nhưng giữ nó trong debug/history/global map
```

có thể trở thành logic rò rỉ bộ nhớ dù language có GC.

## 18. tính cục bộ: lý do LinkedList thường thua ArrayList trong thực tế

Sách giáo khoa thường nhấn mạnh chèn/xóa `O(1)`, nhưng danh sách dựa trên nút còn có các chi phí khác:

```text
pointer/reference overhead
allocator/object overhead
cache misses
poor prefetching
branching
```

Nếu khối lượng công việc chỉ append, iterate và truy cập ngẫu nhiên, mảng động thường tốt hơn rõ rệt.

danh sách liên kết đáng dùng khi **relinking hoặc ổn định định danh nút** thật sự là thao tác cốt lõi.

## 19. Intrusive danh sách liên kết

Trong intrusive list, link các trường nằm trực tiếp trong đối tượng domain:

```c
struct Task {
    int id;
    struct Task *prev;
    struct Task *next;
};
```

Không cần cấp phát wrapper nút riêng, giảm indirection/cấp phát. Nhưng đối tượng chỉ có thể thuộc một list cho mỗi bộ link các trường, coupling cách biểu diễn mạnh hơn.

Kernel/hệ thống code thường dùng intrusive structures vì kiểm soát bố trí/vòng đời tốt.

## 20. XOR danh sách liên kết: kỹ thuật thú vị nhưng ít thực dụng

XOR list encode `prev XOR next` trong một trường để giảm một con trỏ, nhưng code khó gỡ lỗi, không hợp GC/moving collectors, khó integrate tooling và thường không đáng sự đánh đổi trên modern các hệ thống.

Bài học không phải học XOR list để dùng, mà là hiểu rằng **giảm siêu dữ liệu có thể làm ngữ nghĩa/maintainability phức tạp hơn nhiều**.

## 21. Persistent danh sách liên kết

danh sách liên kết đơn bất biến sau khi tạo có persistence rất tự nhiên. Thêm đầu:

```text
newHead -> oldHead -> ...
```

không cần copy tail; version mới share suffix với version cũ. `cons` là `O(1)`.

Functional lists khai thác tính chất này rất mạnh. Ngược lại truy cập ngẫu nhiên vẫn tuyến tính.

cách biểu diễn node-based có thể kém cho có thể thay đổi tính cục bộ bộ nhớ đệm nhưng rất hợp chia sẻ cấu trúc.

## 22. ABA và concurrent linked structures

không khóa (lock-free) stack/list nghe đơn giản vì CAS con trỏ, nhưng thu hồi bộ nhớ (memory reclamation) rất khó. Một nút có thể bị remove, free, rồi bộ cấp phát reuse cùng address; luồng khác thấy con trỏ “giống cũ” và CAS sai logic — hiện tượng ABA.

con trỏ nguy hiểm, epoch-based reclamation hoặc tagged các con trỏ là các kỹ thuật giải một phần vấn đề. Vì vậy “chỉ vài con trỏ writes” không có nghĩa concurrent list đơn giản.

## 23. mất hiệu lực của bộ lặp và modification

Nếu iteration đang chạy mà list bị mutate, ngữ nghĩa cần được định nghĩa:

```text
iterator có còn hợp lệ không?
insert trước/sau current có được nhìn thấy không?
remove current bằng iterator có safe không?
```

Java collections có fail-fast hành vi ở nhiều iterator, nhưng đó không phải synchronization bảo đảm. Custom C/JS structure phải tự định nghĩa contract.

## 24. xác minh của danh sách liên kết đôi

Một bộ xác minh có thể kiểm tra:

```text
head.prev == null hoặc sentinel invariant
for every node: node.next.prev == node
for every node: node.prev.next == node
counted nodes == size
last reachable node == tail
no unintended cycle
```

Trong gỡ lỗi/test, bộ xác minh `O(n)` sau ngẫu nhiên sự thay đổi dữ liệu sequence có giá trị rất lớn để bắt corruption gần nơi xảy ra.

## 25. Differential kiểm thử

Custom list có thể được so với tham chiếu `ArrayList`/JS mảng cho hành vi sequence:

```text
addFirst
addLast
removeFirst
removeLast
insertAt
removeAt
```

mảng tham chiếu có thể chậm nhưng đơn giản, rất phù hợp làm oracle cho đầu vào nhỏ.

## 26. Khi nào nên chọn danh sách liên kết?

Dùng linked structure khi khối lượng công việc thật sự cần một hoặc nhiều yếu tố:

```text
stable node identity
known-node O(1) detach/attach
frequent splice/relink
persistent sharing của suffix
intrusive scheduling/list membership
```

Không nên chọn chỉ vì “chèn là `O(1)`”. Nếu phải tìm kiếm trước khi chèn, tính cục bộ và kích thước bộ nhớ có thể khiến mảng động tốt hơn.

## Mô hình tư duy

> danh sách liên kết lưu **quan hệ kế tiếp**, không lưu tọa độ. Nó tối ưu việc thay đổi topology cục bộ bằng con trỏ/tham chiếu rewiring, và trả giá bằng traversal, tính cục bộ và siêu dữ liệu.

Khi hiểu cách biểu diễn này, mọi sự đánh đổi — predecessor problem, giá trị canh gác (sentinel), ổn định định danh nút, LRU composition, persistence, concurrency — đều trở thành hệ quả tự nhiên.

Xem thêm: [Arrays](./00_arrays_and_dynamic_arrays.md), [Stacks](./02_stacks.md), [Queues/Deque](./03_queues_deques_and_priority_queues.md), [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md).