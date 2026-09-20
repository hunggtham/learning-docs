# Danh sách liên kết
**Linked List / 연결 리스트**

Linked list tách **thứ tự logic** khỏi **vị trí vật lý trong memory**. Array nói “phần tử tiếp theo nằm ở offset kế tiếp”; linked list nói “phần tử tiếp theo nằm ở nơi `next` chỉ tới”.

## Singly linked list

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

Muốn tới phần tử thứ ba phải follow hai links. Vì vậy random access theo index là `O(n)`.

Insert đầu list có thể `O(1)` vì chỉ rewiring local pointers:

```c
Node *push_front(Node *head, int value) {
    Node *node = malloc(sizeof(Node));
    if (!node) return head;
    node->value = value;
    node->next = head;
    return node;
}
```

## Delete và predecessor problem

Trong singly linked list, xóa node thường cần node đứng trước để gán `prev->next = cur->next`. Nếu chỉ biết value/index, ta phải traverse tìm predecessor nên operation tổng thể có thể `O(n)`.

## Doubly linked list

Doubly linked list thêm `prev`:

```java
class Node {
    int value;
    Node prev;
    Node next;
}
```

Nó tốn thêm memory nhưng cho phép đi hai chiều và xóa một node đã biết trong `O(1)`.

LRU cache kinh điển kết hợp hash map và doubly linked list. Hash map biến key thành node trong expected `O(1)`; list giữ recency order và move-to-front trong `O(1)`.

## Sentinel node

**Sentinel/Dummy Node / 더미 노드** là node đặc biệt không mang data nghiệp vụ nhưng giúp thống nhất edge cases. Khi có dummy head, insert/delete gần đầu list không cần nhiều nhánh riêng cho trường hợp `head == null` hoặc “xóa node đầu tiên”.

## Cycle detection

Nếu list có cycle, traversal thường không dừng. Floyd's tortoise-hare dùng `slow` đi một bước và `fast` đi hai bước. Nếu có cycle, hai pointer cuối cùng gặp nhau. Time `O(n)`, extra space `O(1)`.

## C, Java và JavaScript

Trong C, node allocation và reclamation là trách nhiệm của code:

```c
Node *p = head;
while (p) {
    Node *next = p->next;
    free(p);
    p = next;
}
```

Java/JavaScript dùng GC, nhưng vẫn cần bỏ references không cần thiết nếu object graph lifetime dài.

## Mental Model

> Linked list không lưu “phần tử thứ i ở đâu”; nó lưu “ai đứng sau ai”.

Điểm mạnh là local rewiring. Điểm yếu là không có coordinate system như array và locality kém hơn. Vì vậy trong production Java, `ArrayList` thường phổ biến hơn `LinkedList` trừ khi workload thực sự phù hợp.

## Một implementation đầy đủ hơn trong Java

```java
class SinglyList<E> {
    private static class Node<E> {
        E value;
        Node<E> next;
        Node(E value) { this.value = value; }
    }

    private Node<E> head;
    private Node<E> tail;
    private int size;

    void addFirst(E value) {
        Node<E> n = new Node<>(value);
        n.next = head;
        head = n;
        if (tail == null) tail = n;
        size++;
    }

    void addLast(E value) {
        Node<E> n = new Node<>(value);
        if (tail == null) {
            head = tail = n;
        } else {
            tail.next = n;
            tail = n;
        }
        size++;
    }

    E removeFirst() {
        if (head == null) throw new NoSuchElementException();
        E value = head.value;
        head = head.next;
        if (head == null) tail = null;
        size--;
        return value;
    }
}
```

Điểm dễ sai là `tail`. Nếu xóa phần tử cuối cùng mà chỉ đặt `head = null` nhưng quên `tail = null`, invariant `empty <=> head == null && tail == null` bị phá. Một data structure tốt nên có invariant cụ thể đến mức có thể viết assertion/test cho nó.

## Reverse linked list

Reverse không cần tạo list mới. Ta đổi hướng từng edge:

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

Ba pointers có vai trò khác nhau. `cur` là node đang xử lý, `prev` là head của phần đã reverse, còn `next` bảo vệ đường tới phần chưa xử lý trước khi ta phá `cur->next` cũ.

Loop invariant:

> Trước mỗi iteration, `prev` là reverse đúng của prefix đã đi qua; `cur` là head của suffix chưa xử lý; hai phần cùng chứa đúng toàn bộ nodes ban đầu và không overlap.

Sau khi loop kết thúc, suffix rỗng nên `prev` là toàn bộ list đã reverse.

## Doubly linked list và LRU cache

Doubly linked list thường dùng sentinel head/tail:

```text
HEAD <-> node <-> node <-> TAIL
```

Khi đó move-to-front không cần special-case null boundaries. LRU cache giữ map `key -> node`; mỗi `get` tìm node expected `O(1)` rồi detach/attach node ở đầu `O(1)`. Khi vượt capacity, xóa node ngay trước tail và remove key khỏi map.

Nếu thiếu map, tìm key trong list là `O(n)`. Nếu thiếu list, hash map không biết key nào least recently used. Đây là một ví dụ điển hình của **composition of data structures**: hai structures bù cho điểm yếu của nhau.

## JavaScript implementation và garbage collection

```js
class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

function reverse(head) {
  let prev = null;
  let cur = head;
  while (cur !== null) {
    const next = cur.next;
    cur.next = prev;
    prev = cur;
    cur = next;
  }
  return prev;
}
```

Không có `free`, nhưng nếu application giữ một external reference tới node đã logically remove, node đó vẫn reachable và GC không thể reclaim. GC quản reclamation, không quản semantic ownership thay programmer.

## Linked list trong production

Textbook thường nhấn mạnh insert `O(1)`, nhưng modern CPUs làm array-based structures cạnh tranh rất mạnh. Linked list đáng dùng khi node identity/iterators tồn tại lâu, khi splice/relink là operation chính, hoặc khi structure tự nhiên đã là graph/tree node chain. Nếu chỉ cần một growable sequence, dynamic array thường là baseline tốt hơn.
