# Danh sách liên kết
**Linked List / 연결 리스트**

Linked list tách **thứ tự logic** khỏi **vị trí vật lý trong memory**. Array nói “phần tử thứ `i` nằm ở offset tính được”; linked list nói “phần tử tiếp theo nằm ở nơi `next` chỉ tới”. Chính lựa chọn representation này tạo ra toàn bộ trade-off: local rewiring rẻ, nhưng random access và locality kém.

## 1. Singly Linked List

```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```

Representation:

```text
head
 ↓
[10|•] -> [20|•] -> [30|null]
```

Muốn tới node thứ `i` phải follow `i` links, nên access theo index là `O(n)`. Không tồn tại phép tính địa chỉ trực tiếp như array.

## 2. Insert O(1) chỉ đúng khi đã biết vị trí local

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

Rewiring chỉ constant work. Nhưng nếu yêu cầu “insert trước phần tử có value X”, ta vẫn phải search X trước, có thể `O(n)`.

Một lỗi reasoning phổ biến là nói “linked list insert O(1)” mà bỏ qua cost tìm vị trí. Complexity phải tính **toàn bộ operation contract**, không chỉ pointer update cuối.

## 3. Tail pointer thay đổi append cost

Nếu list chỉ giữ `head`, append cuối cần traverse `O(n)`. Nếu giữ thêm `tail`, append có thể `O(1)`:

```text
head -> ... -> tail
```

Nhưng thêm `tail` tạo thêm invariant phải duy trì:

```text
empty => head == null && tail == null
non-empty => tail.next == null
```

Metadata giúp operation nhanh hơn nhưng tăng burden correctness.

## 4. Delete và predecessor problem

Trong singly linked list, để xóa `cur`, ta thường cần `prev`:

```text
prev.next = cur.next
```

Nếu chỉ có pointer tới `cur`, không có cách generic đi lùi về predecessor trong `O(1)`.

Một trick khi được phép thay đổi value là copy data từ `cur.next` vào `cur` rồi bỏ node sau, nhưng không hoạt động cho tail và phá node identity. Nó là problem-specific hack chứ không thay đổi limitation cơ bản của singly list.

## 5. Doubly Linked List

Doubly list lưu cả `prev` và `next`:

```java
class Node<E> {
    E value;
    Node<E> prev;
    Node<E> next;
}
```

Nếu đã có reference tới node, detach `O(1)`:

```text
node.prev.next = node.next
node.next.prev = node.prev
```

Đổi lại mỗi node tốn thêm pointer/reference, mutation phải cập nhật nhiều links hơn và corruption có nhiều dạng hơn.

## 6. Sentinel Nodes làm invariant đơn giản hơn

Thay vì `head == null`/`tail == null` và rất nhiều special case, doubly list có thể dùng hai sentinel:

```text
HEAD <-> ... <-> TAIL
```

List rỗng:

```text
HEAD.next == TAIL
TAIL.prev == HEAD
```

Insert/remove giữa hai nodes luôn cùng pattern. Sentinel không làm algorithm asymptotically nhanh hơn; nó làm **state space của edge cases nhỏ hơn**, từ đó correctness dễ hơn.

## 7. Circular Linked List

Trong circular list, tail nối lại head:

```text
A -> B -> C
^         |
|_________|
```

Nó phù hợp round-robin scheduling, cyclic buffers logic, Josephus-like problems hoặc intrusive queues.

Nhưng traversal không thể dùng `while (p != NULL)`. Termination condition phải dựa vào quay lại start hoặc số bước. Representation thay đổi loop invariant.

## 8. Reverse Linked List và loop invariant

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

Invariant hữu ích:

> `prev` là reverse đúng của prefix đã xử lý; `cur` là head của suffix chưa xử lý; hai phần không overlap và hợp lại chứa đúng toàn bộ nodes ban đầu.

`next` phải được lưu trước khi phá `cur->next`; nếu không ta mất đường tới suffix.

## 9. Floyd Cycle Detection

Dùng `slow` đi 1 bước, `fast` đi 2 bước. Nếu có cycle, hai pointer sẽ gặp nhau.

Tại sao? Sau khi cả hai vào cycle, khoảng cách modulo cycle length thay đổi 1 mỗi iteration, nên cuối cùng bằng 0.

Sau khi gặp, có thể tìm cycle entry bằng cách đưa một pointer về head rồi cho cả hai đi cùng tốc độ; chúng gặp lại ở entry.

Kỹ thuật này khai thác arithmetic trên khoảng cách trong cycle, không cần extra hash set.

## 10. Middle Node và k-th from end bằng relative-speed pointers

Fast/slow không chỉ cho cycle detection. Nếu `fast` đi 2 còn `slow` đi 1, khi fast tới cuối, slow gần middle.

Muốn k-th node từ cuối, giữ hai pointers cách nhau `k` nodes. Khi pointer trước tới cuối, pointer sau chính là answer.

Mental model: linked list không có random index, nhưng **relative distance giữa pointers** có thể encode position information.

## 11. Merge sorted linked lists

Hai sorted lists có thể merge tuyến tính bằng cách luôn lấy head nhỏ hơn. Sentinel dummy head giúp code gọn:

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

Đây là combine primitive của linked-list merge sort.

## 12. Merge Sort trên Linked List

Linked list không có random access tốt, nên Quicksort/index-based strategies kém tự nhiên. Merge Sort lại rất hợp:

1. tìm midpoint bằng slow/fast;
2. split list;
3. recursively sort hai nửa;
4. merge bằng rewiring nodes.

Time `O(n log n)`. Extra array buffer không cần; merge có thể relink nodes. Tuy nhiên recursion stack vẫn tồn tại.

## 13. Splice là thế mạnh thật sự của linked structures

Nếu đã biết boundaries, có thể chuyển cả một đoạn list sang vị trí khác bằng vài pointer updates mà không move từng element.

Đây là operation khó làm hiệu quả trên contiguous array. Intrusive lists, OS kernels và some schedulers dùng node-based structures vì **splice/relink** quan trọng hơn indexed access.

## 14. LRU Cache: composition thay vì một cấu trúc đơn lẻ

LRU cần:

```text
lookup key nhanh
move accessed item lên đầu nhanh
evict least-recent item nhanh
```

Hash map giải lookup, doubly linked list giải recency order.

```text
HashMap<key, Node>
HEAD <-> most recent ... least recent <-> TAIL
```

`get`:

1. map lookup expected `O(1)`;
2. detach node `O(1)`;
3. attach sau HEAD `O(1)`.

Không có map thì search list `O(n)`. Không có list thì map không biết least recently used. Đây là ví dụ quan trọng của **data structure composition**.

## 15. Node identity và stable address

Một lợi thế node-based structure là node có identity riêng. Nếu node allocation không đổi, pointer/reference tới node có thể giữ ổn định qua nhiều insert khác nơi khác.

Dynamic array grow có thể invalid raw pointers/iterators do relocation. Linked list thường không di chuyển các node còn tồn tại.

Nếu API cần stable handles, intrusive references hoặc long-lived iterator semantics, đây có thể là lý do dùng node-based structure dù locality kém.

## 16. C: ownership là phần của data structure

Node chứa value trực tiếp hay pointer?

```text
list owns node, borrows value
list owns node và value
list stores copied value
```

Destructor semantics phải rõ. Nếu value là heap object do list sở hữu, delete node phải gọi destructor/free value. Nếu value borrowed, free nó có thể gây double-free.

Trong C, logical invariant và lifetime invariant phải đúng đồng thời.

## 17. Java/JavaScript: GC không xóa semantic ownership

GC chỉ reclaim object không còn reachable. Nếu application giữ reference tới node đã remove, node và object graph phía sau vẫn sống.

Một bug kiểu:

```text
remove node khỏi list
nhưng giữ nó trong debug/history/global map
```

có thể trở thành logical memory leak dù language có GC.

## 18. Locality: lý do LinkedList thường thua ArrayList trong thực tế

Textbook nhấn mạnh insert/delete `O(1)`, nhưng node-based list có:

```text
pointer/reference overhead
allocator/object overhead
cache misses
poor prefetching
branching
```

Nếu workload chỉ append, iterate và random access, dynamic array thường tốt hơn rõ rệt.

Linked list đáng dùng khi **relinking hoặc stable node identity** thật sự là operation cốt lõi.

## 19. Intrusive Linked List

Trong intrusive list, link fields nằm trực tiếp trong object domain:

```c
struct Task {
    int id;
    struct Task *prev;
    struct Task *next;
};
```

Không cần allocate wrapper node riêng, giảm indirection/allocation. Nhưng object chỉ có thể thuộc một list cho mỗi bộ link fields, coupling representation mạnh hơn.

Kernel/system code thường dùng intrusive structures vì kiểm soát layout/lifetime tốt.

## 20. XOR Linked List: kỹ thuật thú vị nhưng ít thực dụng

XOR list encode `prev XOR next` trong một field để giảm một pointer, nhưng code khó debug, không hợp GC/moving collectors, khó integrate tooling và thường không đáng trade-off trên modern systems.

Bài học không phải học XOR list để dùng, mà là hiểu rằng **giảm metadata có thể làm semantics/maintainability phức tạp hơn nhiều**.

## 21. Persistent Linked List

Singly linked list immutable có persistence rất tự nhiên. Thêm đầu:

```text
newHead -> oldHead -> ...
```

không cần copy tail; version mới share suffix với version cũ. `cons` là `O(1)`.

Functional lists khai thác property này rất mạnh. Ngược lại random access vẫn tuyến tính.

Representation node-based có thể kém cho mutable cache locality nhưng rất hợp structural sharing.

## 22. ABA và concurrent linked structures

Lock-free stack/list nghe đơn giản vì CAS pointer, nhưng memory reclamation rất khó. Một node có thể bị remove, free, rồi allocator reuse cùng address; thread khác thấy pointer “giống cũ” và CAS sai logic — hiện tượng ABA.

Hazard pointers, epoch-based reclamation hoặc tagged pointers là các kỹ thuật giải một phần vấn đề. Vì vậy “chỉ vài pointer writes” không có nghĩa concurrent list đơn giản.

## 23. Iterator invalidation và modification

Nếu iteration đang chạy mà list bị mutate, semantics cần được định nghĩa:

```text
iterator có còn hợp lệ không?
insert trước/sau current có được nhìn thấy không?
remove current bằng iterator có safe không?
```

Java collections có fail-fast behavior ở nhiều iterator, nhưng đó không phải synchronization guarantee. Custom C/JS structure phải tự định nghĩa contract.

## 24. Validation của doubly linked list

Một validator có thể kiểm tra:

```text
head.prev == null hoặc sentinel invariant
for every node: node.next.prev == node
for every node: node.prev.next == node
counted nodes == size
last reachable node == tail
no unintended cycle
```

Trong debug/test, validator `O(n)` sau random mutation sequence có giá trị rất lớn để bắt corruption gần nơi xảy ra.

## 25. Differential Testing

Custom list có thể được so với reference `ArrayList`/JS Array cho behavior sequence:

```text
addFirst
addLast
removeFirst
removeLast
insertAt
removeAt
```

Array reference có thể chậm nhưng đơn giản, rất phù hợp làm oracle cho input nhỏ.

## 26. Khi nào nên chọn Linked List?

Dùng linked structure khi workload thật sự cần một hoặc nhiều yếu tố:

```text
stable node identity
known-node O(1) detach/attach
frequent splice/relink
persistent sharing của suffix
intrusive scheduling/list membership
```

Không chọn chỉ vì “insert O(1)”. Nếu phải search trước insert, locality và footprint có thể khiến dynamic array tốt hơn.

## Mental Model

> Linked list lưu **quan hệ kế tiếp**, không lưu tọa độ. Nó tối ưu việc thay đổi topology cục bộ bằng pointer/reference rewiring, và trả giá bằng traversal, locality và metadata.

Khi hiểu representation này, mọi trade-off — predecessor problem, sentinel, stable node identity, LRU composition, persistence, concurrency — đều trở thành hệ quả tự nhiên.

Xem thêm: [Arrays](./00_arrays_and_dynamic_arrays.md), [Stacks](./02_stacks.md), [Queues/Deque](./03_queues_deques_and_priority_queues.md), [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md).