# Danh sách liên kết

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Danh sách liên kết**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. danh sách liên kết đơn** chỉ đường quay lại owner và tài liệu chuẩn khi cần đào sâu; sau đó sang **2. Insert O(1) chỉ đúng khi đã biết vị trí cục bộ** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối linked lists với pointer, node và locality, để thao tác chèn/xóa được đặt cạnh chi phí cache.

**danh sách liên kết / 연결 리스트**

danh sách liên kết tách **thứ tự lô-gic (logic / 논리)** khỏi **vị trí vật lý trong bộ nhớ**. mảng nói “phần tử thứ `i` nằm ở offset tính được”; danh sách liên kết nói “phần tử tiếp theo nằm ở nơi `next` chỉ tới”. Chính lựa chọn cách biểu diễn (representation / 표현) này tạo ra toàn bộ sự đánh đổi (trade-off / 트레이드오프): cục bộ rewiring rẻ, nhưng truy cập ngẫu nhiên và tính cục bộ (locality) kém.

## 1. danh sách liên kết đơn

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

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

Muốn tới nút thứ `i` phải follow `i` links, nên truy cập (access / 접근) theo chỉ mục (index / 인덱스) là `O(n)`. Không tồn tại phép tính địa chỉ trực tiếp như mảng.

> **Nối mạch:** **2. Insert O(1) chỉ đúng khi đã biết vị trí cục bộ** nối từ **1. danh sách liên kết đơn** sang **3. Tail con trỏ thay đổi append chi phí**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Một lỗi lập luận (reasoning / 추론) phổ biến là nói “danh sách liên kết insert O(1)” mà bỏ qua chi phí tìm vị trí. độ phức tạp (complexity / 복잡도) phải tính **toàn bộ thao tác đặc tả hợp đồng (contract / 계약)**, không chỉ con trỏ cập nhật cuối.

> **Nối mạch:** **3. Tail con trỏ thay đổi append chi phí** nối từ **2. Insert O(1) chỉ đúng khi đã biết vị trí cục bộ** sang **4. Delete và predecessor bài toán (problem / 문제)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Tail con trỏ thay đổi append chi phí

Nếu danh sách (list / 목록) chỉ giữ `head`, append cuối cần traverse `O(n)`. Nếu giữ thêm `tail`, append có thể `O(1)`:

```text
head -> ... -> tail
```

Nhưng thêm `tail` tạo thêm bất biến (invariant / 불변식) phải duy trì:

```text
empty => head == null && tail == null
non-empty => tail.next == null
```

siêu dữ liệu giúp thao tác nhanh hơn nhưng tăng burden tính đúng đắn.

> **Nối mạch:** **4. Delete và predecessor bài toán (problem / 문제)** nối từ **3. Tail con trỏ thay đổi append chi phí** sang **5. danh sách liên kết đôi (Doubly Linked List)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Delete và predecessor bài toán (problem / 문제)

Trong danh sách liên kết đơn, để xóa `cur`, ta thường cần `prev`:

```text
prev.next = cur.next
```

Nếu chỉ có con trỏ tới `cur`, không có cách tổng quát đi lùi về predecessor trong `O(1)`.

Một trick khi được phép thay đổi giá trị là bản sao (copy / 복사) dữ liệu (data / 데이터) từ `cur.next` vào `cur` rồi bỏ nút sau, nhưng không hoạt động cho tail và phá định danh nút. Nó là problem-specific hack chứ không thay đổi limitation cơ bản của singly danh sách (list / 목록).

> **Nối mạch:** sau nội dung của **4. Delete và predecessor bài toán (problem / 문제)**, **5. danh sách liên kết đôi (Doubly Linked List)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu; **6. Sentinel các nút làm bất biến đơn giản hơn** mở rộng hệ quả hoặc giới hạn của cơ chế này.

## 5. danh sách liên kết đôi (Doubly Linked List)

Doubly danh sách (list / 목록) lưu cả `prev` và `next`:

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

> **Nối mạch:** **6. Sentinel các nút làm bất biến đơn giản hơn** nối từ **5. danh sách liên kết đôi (Doubly Linked List)** sang **7. Circular danh sách liên kết**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Sentinel các nút làm bất biến đơn giản hơn

Thay vì `head == null`/`tail == null` và rất nhiều trường hợp đặc biệt, doubly danh sách (list / 목록) có thể dùng hai giá trị canh gác (sentinel):

```text
HEAD <-> ... <-> TAIL
```

Danh sách (list / 목록) rỗng:

```text
HEAD.next == TAIL
TAIL.prev == HEAD
```

Insert/remove giữa hai các nút luôn cùng mẫu. Sentinel không làm thuật toán asymptotically nhanh hơn; nó làm **không gian trạng thái của các trường hợp biên (edge cases) nhỏ hơn**, từ đó tính đúng đắn dễ hơn.

> **Nối mạch:** **7. Circular danh sách liên kết** nối từ **6. Sentinel các nút làm bất biến đơn giản hơn** sang **8. Reverse danh sách liên kết và bất biến vòng lặp**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Circular danh sách liên kết

Trong circular danh sách (list / 목록), tail nối lại head:

```text
A -> B -> C
^         |
|_________|
```

Nó phù hợp lập lịch luân phiên, cyclic các bộ đệm lô-gic (logic / 논리), Josephus-like problems hoặc intrusive queues.

Nhưng traversal không thể dùng `while (p != NULL)`. Termination điều kiện phải dựa vào quay lại start hoặc số bước. cách biểu diễn thay đổi bất biến vòng lặp.

> **Nối mạch:** **8. Reverse danh sách liên kết và bất biến vòng lặp** nối từ **7. Circular danh sách liên kết** sang **9. Floyd phát hiện chu trình**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Reverse danh sách liên kết và bất biến vòng lặp

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

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

> **Nối mạch:** **9. Floyd phát hiện chu trình** nối từ **8. Reverse danh sách liên kết và bất biến vòng lặp** sang **10. nút giữa và k-th from end bằng relative-speed các con trỏ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Floyd phát hiện chu trình

Dùng `slow` đi 1 bước, `fast` đi 2 bước. Nếu có chu trình, hai con trỏ sẽ gặp nhau.

Tại sao? Sau khi cả hai vào chu trình, khoảng cách modulo chu trình length thay đổi 1 mỗi iteration, nên cuối cùng bằng 0.

Sau khi gặp, có thể tìm chu trình mục bằng cách đưa một con trỏ về head rồi cho cả hai đi cùng tốc độ; chúng gặp lại ở mục.

Kỹ thuật này khai thác arithmetic trên khoảng cách trong chu trình, không cần extra băm (hash / 해시) set.

> **Nối mạch:** **10. nút giữa và k-th from end bằng relative-speed các con trỏ** nối từ **9. Floyd phát hiện chu trình** sang **11. Merge sorted linked lists**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. nút giữa và k-th from end bằng relative-speed các con trỏ

Fast/slow không chỉ cho phát hiện chu trình. Nếu `fast` đi 2 còn `slow` đi 1, khi fast tới cuối, slow gần middle.

Muốn nút thứ k từ cuối, giữ hai các con trỏ cách nhau `k` các nút. Khi con trỏ trước tới cuối, con trỏ sau chính là answer.

Mô hình tư duy: danh sách liên kết không hỗ trợ truy cập ngẫu nhiên theo chỉ số, nhưng **khoảng cách tương đối giữa các con trỏ** có thể mã hóa thông tin vị trí.

> **Nối mạch:** **11. Merge sorted linked lists** nối từ **10. nút giữa và k-th from end bằng relative-speed các con trỏ** sang **12. sắp xếp trộn trên danh sách liên kết**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Merge sorted linked lists

Hai các danh sách đã sắp xếp có thể merge tuyến tính bằng cách luôn lấy head nhỏ hơn. Sentinel nút đầu giả giúp mã (code / 코드) gọn:

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

Đây là kết hợp thành phần nguyên thủy (primitive / 기본 요소) của linked-list sắp xếp trộn.

> **Nối mạch:** sau nội dung của **11. Merge sorted linked lists**, **12. sắp xếp trộn trên danh sách liên kết** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu; **13. Splice là thế mạnh thật sự của linked structures** mở rộng hệ quả hoặc giới hạn của cơ chế này.

## 12. sắp xếp trộn trên danh sách liên kết

danh sách liên kết không có truy cập ngẫu nhiên tốt, nên Quicksort/index-based strategies kém tự nhiên. sắp xếp trộn lại rất hợp:

1. tìm midpoint bằng slow/fast;
2. split danh sách (list / 목록);
3. recursively sort hai nửa;
4. merge bằng rewiring các nút.

Thời gian (time / 시간) `O(n log n)`. bộ đệm mảng bổ sung không cần; merge có thể relink các nút. Tuy nhiên ngăn xếp đệ quy vẫn tồn tại.

> **Nối mạch:** **13. Splice là thế mạnh thật sự của linked structures** nối từ **12. sắp xếp trộn trên danh sách liên kết** sang **14. LRU bộ nhớ đệm: composition thay vì một cấu trúc đơn lẻ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Splice là thế mạnh thật sự của linked structures

Nếu đã biết các ranh giới, có thể chuyển cả một đoạn danh sách (list / 목록) sang vị trí khác bằng vài con trỏ các cập nhật mà không move từng phần tử.

Đây là thao tác khó thực hiện hiệu quả trên mảng liên tiếp. Danh sách nội tại, nhân hệ điều hành và một số bộ lập lịch dùng cấu trúc dựa trên nút vì **nối lại liên kết** quan trọng hơn truy cập theo chỉ số.

> **Nối mạch:** **14. LRU bộ nhớ đệm: composition thay vì một cấu trúc đơn lẻ** nối từ **13. Splice là thế mạnh thật sự của linked structures** sang **15. định danh nút và ổn định address**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. LRU bộ nhớ đệm: composition thay vì một cấu trúc đơn lẻ

LRU cần:

```text
lookup key nhanh
move accessed item lên đầu nhanh
evict least-recent item nhanh
```

bảng ánh xạ băm giải tra cứu, danh sách liên kết đôi giải recency thứ tự (order / 순서).

```text
HashMap<key, Node>
HEAD <-> most recent ... least recent <-> TAIL
```

`get`:

1. map tra cứu kỳ vọng `O(1)`;
2. detach nút `O(1)`;
3. attach sau HEAD `O(1)`.

Không có ánh xạ thì tìm trong danh sách tốn `O(n)`. Không có danh sách thì ánh xạ không biết phần tử nào ít được sử dụng gần đây nhất. Đây là ví dụ quan trọng của **phối hợp nhiều cấu trúc dữ liệu (data-structure composition)**.

> **Nối mạch:** **15. định danh nút và ổn định address** nối từ **14. LRU bộ nhớ đệm: composition thay vì một cấu trúc đơn lẻ** sang **16. C: quyền sở hữu (ownership / 소유권) là phần của cấu trúc dữ liệu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. định danh nút và ổn định address

Một lợi thế cấu trúc dựa trên nút là nút có định danh (identity / 식별자) riêng. Nếu nút cấp phát không đổi, con trỏ/tham chiếu tới nút có thể giữ ổn định qua nhiều insert khác nơi khác.

mảng động grow có thể không hợp lệ raw các con trỏ/iterators do relocation. danh sách liên kết thường không di chuyển các nút còn tồn tại.

Nếu API cần ổn định handles, intrusive các tham chiếu hoặc long-lived iterator ngữ nghĩa (semantics / 의미론), đây có thể là lý do dùng cấu trúc dựa trên nút dù tính cục bộ kém.

> **Nối mạch:** **15. định danh nút và ổn định address** đặt vấn đề; **16. C: quyền sở hữu (ownership / 소유권) là phần của cấu trúc dữ liệu** kiểm tra bằng chứng, rồi **17. Java/JavaScript: GC không xóa ngữ nghĩa (semantic / 의미적) quyền sở hữu** mở rộng hệ quả.

## 16. C: quyền sở hữu (ownership / 소유권) là phần của cấu trúc dữ liệu

nút chứa giá trị trực tiếp hay con trỏ?

```text
list owns node, borrows value
list owns node và value
list stores copied value
```

Ngữ nghĩa của hàm hủy phải rõ ràng. Nếu giá trị là đối tượng trên vùng nhớ động (heap / 힙) do danh sách sở hữu, khi xóa nút phải gọi hàm hủy hoặc giải phóng giá trị. Nếu giá trị chỉ được mượn, giải phóng nó có thể gây lỗi giải phóng hai lần (double-free).

Trong C, lô-gic (logic / 논리) bất biến và vòng đời (lifetime) bất biến phải đúng đồng thời.

> **Nối mạch:** **16. C: quyền sở hữu (ownership / 소유권) là phần của cấu trúc dữ liệu** đặt vấn đề; **17. Java/JavaScript: GC không xóa ngữ nghĩa (semantic / 의미적) quyền sở hữu** kiểm tra bằng chứng, rồi **18. tính cục bộ: lý do LinkedList thường thua ArrayList trong thực tế** mở rộng hệ quả.

## 17. Java/JavaScript: GC không xóa ngữ nghĩa (semantic / 의미적) quyền sở hữu

GC chỉ thu hồi đối tượng không còn có thể tới. Nếu ứng dụng giữ tham chiếu tới nút đã remove, nút và đồ thị đối tượng phía sau vẫn sống.

Một bug kiểu:

```text
remove node khỏi list
nhưng giữ nó trong debug/history/global map
```

có thể trở thành lô-gic (logic / 논리) rò rỉ bộ nhớ dù ngôn ngữ (language / 언어) có GC.

> **Nối mạch:** **18. tính cục bộ: lý do LinkedList thường thua ArrayList trong thực tế** nối từ **17. Java/JavaScript: GC không xóa ngữ nghĩa (semantic / 의미적) quyền sở hữu** sang **19. Intrusive danh sách liên kết**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** sau nội dung của **18. tính cục bộ: lý do LinkedList thường thua ArrayList trong thực tế**, **19. Intrusive danh sách liên kết** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu; **20. XOR danh sách liên kết: kỹ thuật thú vị nhưng ít thực dụng** mở rộng hệ quả hoặc giới hạn của cơ chế này.

## 19. Intrusive danh sách liên kết

Trong intrusive danh sách (list / 목록), link các trường nằm trực tiếp trong đối tượng lĩnh vực (domain / 도메인):

```c
struct Task {
    int id;
    struct Task *prev;
    struct Task *next;
};
```

Không cần cấp phát wrapper nút riêng, giảm indirection/cấp phát. Nhưng đối tượng chỉ có thể thuộc một danh sách (list / 목록) cho mỗi bộ link các trường, coupling cách biểu diễn mạnh hơn.

Kernel/hệ thống mã (code / 코드) thường dùng intrusive structures vì kiểm soát bố trí/vòng đời tốt.

> **Nối mạch:** **20. XOR danh sách liên kết: kỹ thuật thú vị nhưng ít thực dụng** nối từ **19. Intrusive danh sách liên kết** sang **21. Persistent danh sách liên kết**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. XOR danh sách liên kết: kỹ thuật thú vị nhưng ít thực dụng

XOR danh sách (list / 목록) encode `prev XOR next` trong một trường để giảm một con trỏ, nhưng mã (code / 코드) khó gỡ lỗi, không hợp GC/moving collectors, khó integrate tooling và thường không đáng sự đánh đổi trên hiện đại (modern / 현대적) các hệ thống.

Bài học không phải học XOR danh sách (list / 목록) để dùng, mà là hiểu rằng **giảm siêu dữ liệu có thể làm ngữ nghĩa/maintainability phức tạp hơn nhiều**.

> **Nối mạch:** **21. Persistent danh sách liên kết** nối từ **20. XOR danh sách liên kết: kỹ thuật thú vị nhưng ít thực dụng** sang **22. ABA và concurrent linked structures**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Persistent danh sách liên kết

danh sách liên kết đơn bất biến sau khi tạo có persistence rất tự nhiên. Thêm đầu:

```text
newHead -> oldHead -> ...
```

không cần bản sao (copy / 복사) tail; phiên bản (version / 버전) mới share suffix với phiên bản (version / 버전) cũ. `cons` là `O(1)`.

Functional lists khai thác tính chất này rất mạnh. Ngược lại truy cập ngẫu nhiên vẫn tuyến tính.

cách biểu diễn node-based có thể kém cho có thể thay đổi tính cục bộ bộ nhớ đệm nhưng rất hợp chia sẻ cấu trúc.

> **Nối mạch:** **22. ABA và concurrent linked structures** nối từ **21. Persistent danh sách liên kết** sang **23. mất hiệu lực của bộ lặp và modification**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. ABA và concurrent linked structures

không khóa (lock-free) ngăn xếp (stack / 스택)/danh sách (list / 목록) nghe đơn giản vì CAS con trỏ, nhưng thu hồi bộ nhớ (memory reclamation) rất khó. Một nút có thể bị remove, free, rồi bộ cấp phát reuse cùng address; luồng khác thấy con trỏ “giống cũ” và CAS sai lô-gic (logic / 논리) — hiện tượng ABA.

con trỏ nguy hiểm, epoch-based reclamation hoặc tagged các con trỏ là các kỹ thuật giải một phần vấn đề. Vì vậy “chỉ vài con trỏ writes” không có nghĩa concurrent danh sách (list / 목록) đơn giản.

> **Nối mạch:** **23. mất hiệu lực của bộ lặp và modification** nối từ **22. ABA và concurrent linked structures** sang **24. xác minh của danh sách liên kết đôi**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. mất hiệu lực của bộ lặp và modification

Nếu iteration đang chạy mà danh sách (list / 목록) bị mutate, ngữ nghĩa cần được định nghĩa:

```text
iterator có còn hợp lệ không?
insert trước/sau current có được nhìn thấy không?
remove current bằng iterator có safe không?
```

Java collections có fail-fast hành vi ở nhiều iterator, nhưng đó không phải synchronization bảo đảm. Custom C/JS cấu trúc (structure / 구조) phải tự định nghĩa đặc tả hợp đồng (contract / 계약).

> **Nối mạch:** sau nội dung của **23. mất hiệu lực của bộ lặp và modification**, **24. xác minh của danh sách liên kết đôi** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu; **25. Differential kiểm thử** mở rộng hệ quả hoặc giới hạn của cơ chế này.

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

Trong gỡ lỗi/kiểm thử (test / 테스트), bộ xác minh `O(n)` sau ngẫu nhiên sự thay đổi dữ liệu chuỗi (sequence / 시퀀스) có giá trị rất lớn để bắt corruption gần nơi xảy ra.

> **Nối mạch:** **25. Differential kiểm thử** nối từ **24. xác minh của danh sách liên kết đôi** sang **26. Khi nào nên chọn danh sách liên kết?**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Differential kiểm thử

Custom danh sách (list / 목록) có thể được so với tham chiếu `ArrayList`/JS mảng cho hành vi chuỗi (sequence / 시퀀스):

```text
addFirst
addLast
removeFirst
removeLast
insertAt
removeAt
```

mảng tham chiếu có thể chậm nhưng đơn giản, rất phù hợp làm oracle cho đầu vào nhỏ.

> **Nối mạch:** **26. Khi nào nên chọn danh sách liên kết?** nối từ **25. Differential kiểm thử** sang **Mô hình tư duy**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Khi nào nên chọn danh sách liên kết?

Dùng linked cấu trúc (structure / 구조) khi khối lượng công việc thật sự cần một hoặc nhiều yếu tố:

```text
stable node identity
known-node O(1) detach/attach
frequent splice/relink
persistent sharing của suffix
intrusive scheduling/list membership
```

Không nên chọn chỉ vì “chèn là `O(1)`”. Nếu phải tìm kiếm trước khi chèn, tính cục bộ và kích thước bộ nhớ có thể khiến mảng động tốt hơn.

> **Nối mạch:** **Mô hình tư duy** tổng hợp từ **26. Khi nào nên chọn danh sách liên kết?**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Mô hình tư duy

> danh sách liên kết lưu **quan hệ kế tiếp**, không lưu tọa độ. Nó tối ưu việc thay đổi topology cục bộ bằng con trỏ/tham chiếu rewiring, và trả giá bằng traversal, tính cục bộ và siêu dữ liệu.

Khi hiểu cách biểu diễn này, mọi sự đánh đổi — predecessor bài toán (problem / 문제), giá trị canh gác (sentinel), ổn định định danh nút, LRU composition, persistence, tính đồng thời (concurrency / 동시성) — đều trở thành hệ quả tự nhiên.

Xem thêm: [Arrays](./00_arrays_and_dynamic_arrays.md), [Stacks](./02_stacks.md), [Queues/Deque](./03_queues_deques_and_priority_queues.md), [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
