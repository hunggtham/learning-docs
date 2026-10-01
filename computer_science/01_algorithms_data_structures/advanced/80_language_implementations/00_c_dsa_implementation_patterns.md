# Các mẫu triển khai DSA trong C

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Các mẫu triển khai DSA trong C**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Quyền sở hữu là một phần của hợp đồng API** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Mảng động** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**C DSA hiện thực (implementation / 구현) Patterns / C 자료구조 구현 패턴**

C là ngôn ngữ rất tốt để học DSA vì nó làm lộ rõ những gì thời gian chạy (runtime / 런타임) cấp cao thường che đi: bố trí bộ nhớ, số học con trỏ, cấp phát, quyền sở hữu (ownership / 소유권), vòng đời và xử lý lỗi. Vì vậy một cấu trúc dữ liệu C chỉ thực sự đúng khi đồng thời giữ được **bất biến lô-gic (logic / 논리)** của thuật toán và **bất biến vòng đời/quyền sở hữu** của bộ nhớ.

Một vùng nhớ động (heap / 힙) có thể giữ đúng thứ tự nhưng vẫn sai vì ghi vượt bộ đệm. Một danh sách có thể cho kết quả đúng trên ví dụ nhỏ nhưng vẫn chứa con trỏ treo. Học DSA bằng C là học cả thuật toán lẫn cách biểu diễn.

## Quyền sở hữu là một phần của hợp đồng API

Một bộ chứa (container / 컨테이너) lưu con trỏ thường có ba lựa chọn ngữ nghĩa:

```text
sở hữu object
mượn object
sao chép object/giá trị
```

Nếu bộ chứa (container / 컨테이너) sở hữu dữ liệu, nó phải biết cách hủy dữ liệu. Một API tổng quát có thể nhận callback:

```c
typedef void (*destroy_fn)(void *);
```

Nếu quyền sở hữu không rõ, các lỗi thường gặp là double-free, use-after-free, rò rỉ bộ nhớ hoặc giải phóng bằng sai allocator.

Một API tốt phải trả lời: ai tạo/hủy bộ chứa (container / 컨테이너), ai sở hữu phần tử, con trỏ trả về sống tới khi nào và thao tác nào làm con trỏ/bộ lặp mất hiệu lực.

> **Chuyển mạch:** C API phải làm rõ ownership; dynamic array minh họa capacity/length, còn `realloc` có thể move storage và invalidate pointers nên contract phải nói rõ lifetime.

## Mảng động

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```c
typedef struct {
    int *data;
    size_t size;
    size_t capacity;
} IntVector;
```

Bất biến chính:

```text
0 <= size <= capacity
các phần tử hợp lệ nằm trong [0, size)
vùng cấp phát đủ chứa capacity phần tử
```

Nếu mỗi lần đầy chỉ tăng sức chứa (capacity / 용량) thêm 1, tổng chi phí sao chép của nhiều lần append trở thành bậc hai. Tăng theo cấp số nhân, ví dụ nhân 2 hoặc khoảng 1.5, cho append `O(1)` khấu hao.

Phải kiểm tra overflow trước khi tính kích thước cấp phát:

```c
if (capacity > SIZE_MAX / 2) return false;
if (new_capacity > SIZE_MAX / sizeof *v->data) return false;
```

> **Chuyển mạch:** Ở chặng này của **Các mẫu triển khai DSA trong C**, **realloc và mất hiệu lực của con trỏ** tiếp nhận điểm tựa từ **Mảng động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cập nhật theo kiểu giao dịch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## realloc và mất hiệu lực của con trỏ

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```c
int *new_data = realloc(v->data, new_cap * sizeof *v->data);
if (!new_data) return false;

v->data = new_data;
v->capacity = new_cap;
```

Không nên ghi trực tiếp kết quả `realloc` vào con trỏ cũ nếu muốn giữ vùng cũ khi cấp phát thất bại. `realloc` thành công có thể di chuyển buffer, vì vậy mọi con trỏ tới phần tử cũ có thể mất hiệu lực.

Đây là ví dụ cách biểu diễn bộ nhớ tạo ra ngữ nghĩa API.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các mẫu triển khai DSA trong C**, **Cập nhật theo kiểu giao dịch** tiếp nhận điểm tựa từ **realloc và mất hiệu lực của con trỏ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Danh sách liên kết** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cập nhật theo kiểu giao dịch

Một thay đổi cấu trúc nên theo mẫu:

```text
chuẩn bị tài nguyên mới
xác nhận thành công
commit thay đổi cấu trúc
sau đó giải phóng trạng thái cũ
```

Ví dụ resize bảng băm (hash table / 해시 테이블): cấp phát bảng mới, rehash thành công, đổi con trỏ/sức chứa (capacity / 용량) rồi mới giải phóng bảng cũ. Nếu cập nhật nửa chừng rồi cấp phát thất bại, cấu trúc có thể bị hỏng.

> **Chuyển mạch:** Trong **Các mẫu triển khai DSA trong C**, sau nội dung của **Cập nhật theo kiểu giao dịch**, **Danh sách liên kết** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Ngăn xếp (stack / 스택), hàng đợi (queue / 큐) và bộ đệm vòng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Danh sách liên kết

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```

Chèn đầu:

```c
Node *n = malloc(sizeof *n);
if (!n) return false;

n->value = value;
n->next = list->head;
list->head = n;
list->size++;
```

Khi xóa, phải nối lại các liên kết trước khi giải phóng nút. Nếu bên ngoài còn giữ con trỏ tới nút bị xóa, con trỏ đó trở thành không hợp lệ.

Với danh sách đôi, cần giữ bất biến hai chiều:

```text
n->next != NULL => n->next->prev == n
n->prev != NULL => n->prev->next == n
```

Nút canh gác (sentinel) có thể giảm số trường hợp đặc biệt ở đầu/cuối danh sách và làm lô-gic (logic / 논리) nối lại đồng đều hơn.

> **Chuyển mạch:** Ở chặng này của **Các mẫu triển khai DSA trong C**, **Ngăn xếp (stack / 스택), hàng đợi (queue / 큐) và bộ đệm vòng** tiếp nhận điểm tựa từ **Danh sách liên kết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ chứa (container / 컨테이너) tổng quát với void** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngăn xếp (stack / 스택), hàng đợi (queue / 큐) và bộ đệm vòng

Ngăn xếp (stack / 스택) bằng mảng thường có locality tốt và ít cấp phát. hàng đợi (queue / 큐) có thể dùng **bộ đệm vòng (ring buffer)** để tránh dịch chuyển phần tử.

```c
index = (index + 1) % capacity;
```

Nếu sức chứa (capacity / 용량) luôn là lũy thừa của 2:

```c
index = (index + 1) & (capacity - 1);
```

Tối ưu bằng bitmask chỉ đúng khi bất biến sức chứa (capacity / 용량) được duy trì.

Có nhiều quy ước ring buffer như `head + size`, `head/tail + one-empty-slot` hoặc thêm cờ `full`. Phải chọn một mô hình và dùng nhất quán.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các mẫu triển khai DSA trong C**, **Bộ chứa (container / 컨테이너) tổng quát với void** tiếp nhận điểm tựa từ **Ngăn xếp (stack / 스택), hàng đợi (queue / 큐) và bộ đệm vòng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hợp đồng comparator** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ chứa (container / 컨테이너) tổng quát với void*

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```c
typedef int (*compare_fn)(const void *, const void *);
```

`void *` cho phép viết vùng nhớ động (heap / 힙), BST hoặc sort tổng quát nhưng đổi lại mất một phần an toàn kiểu tĩnh, cần cast và làm hợp đồng quyền sở hữu (ownership / 소유권) phức tạp hơn.

Macro có thể sinh bộ chứa (container / 컨테이너) theo kiểu cụ thể, giảm cast nhưng làm gỡ lỗi (debug / 디버그) và thông báo lỗi khó hơn. C không có generics bản địa (native / 네이티브), vì vậy đây là một đánh đổi thiết kế thực sự.

> **Chuyển mạch:** Trong **Các mẫu triển khai DSA trong C**, **Hợp đồng comparator** tiếp nhận điểm tựa từ **Bộ chứa (container / 컨테이너) tổng quát với void** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Padding, alignment và bố trí dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hợp đồng comparator

Comparator phải nhất quán và có tính bắc cầu. Tránh:

```c
return a - b;
```

vì signed overflow. Với số nguyên:

```c
return (a > b) - (a < b);
```

thường an toàn hơn.

`qsort` tiện dụng nhưng gọi comparator qua hàm (function / 함수) pointer và API `void *`. Trong đường chạy số học rất nóng, sort chuyên biệt có thể nhanh hơn, nhưng chỉ nên thay thế sau khi đo.

> **Chuyển mạch:** Ở chặng này của **Các mẫu triển khai DSA trong C**, **Hợp đồng comparator** nêu điều cần giải thích; **Padding, alignment và bố trí dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Arena và pool allocator** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Padding, alignment và bố trí dữ liệu

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```c
typedef struct {
    char flag;
    int value;
    void *next;
} Node;
```

Trình biên dịch (compiler / 컴파일러) có thể chèn padding để căn chỉnh. `sizeof(Node)` mới là chi phí thực tế.

**Array of Structures (AoS)** phù hợp khi thường đọc toàn bản ghi. **cấu trúc (structure / 구조) of Arrays (SoA)** có thể tốt hơn nếu thuật toán chủ yếu quét một vài trường vì tăng locality và khả năng vectorization.

Cách bố trí nên phù hợp mẫu truy cập.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các mẫu triển khai DSA trong C**, **Padding, alignment và bố trí dữ liệu** nêu điều cần giải thích; **Arena và pool allocator** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Handle thay cho con trỏ thô** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Arena và pool allocator

Cấu trúc nhiều nút gọi `malloc` cho từng nút có thể tốn siêu dữ liệu (metadata / 메타데이터) và gây phân mảnh.

Arena cấp phát một khối lớn rồi chia tuần tự thành các nút. Nó nhanh, có locality tốt và rất phù hợp khi nhiều đối tượng (object / 객체) có cùng vòng đời, nhưng khó giải phóng riêng từng nút.

Pool với free-list phù hợp khi đối tượng (object / 객체) có kích thước cố định và thường xuyên được tái sử dụng:

```text
free node     -> đưa vào free list
allocate node -> lấy từ free list trước khi xin vùng mới
```

Nếu bên ngoài giữ handle lâu dài, generation counter `(index, generation)` giúp phát hiện handle cũ sau khi slot được tái sử dụng.

> **Chuyển mạch:** Trong **Các mẫu triển khai DSA trong C**, **Handle thay cho con trỏ thô** tiếp nhận điểm tựa từ **Arena và pool allocator** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bảng băm (hash table / 해시 테이블) và cách xử lý va chạm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Handle thay cho con trỏ thô

Khi lưu trữ (storage / 저장소) có thể di chuyển hoặc compact, API công khai (public API / 공개 API) giữ raw pointer rất rủi ro. Một handle số nguyên có thể ánh xạ tới slot nội bộ. Nếu lưu trữ (storage / 저장소) di chuyển, ánh xạ thay đổi nhưng handle vẫn ổn định.

Mẫu này phổ biến trong game engine và ECS.

> **Chuyển mạch:** Ở chặng này của **Các mẫu triển khai DSA trong C**, **Bảng băm (hash table / 해시 테이블) và cách xử lý va chạm** tiếp nhận điểm tựa từ **Handle thay cho con trỏ thô** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ sâu đệ quy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảng băm (hash table / 해시 테이블) và cách xử lý va chạm

**Separate chaining** lưu bucket trỏ tới danh sách entry. **Open addressing** lưu entry trực tiếp trong bảng và thường có locality tốt hơn, nhưng probing, hệ số tải và xóa phức tạp hơn.

Khi xóa trong open addressing, không thể luôn đặt slot thành `EMPTY` vì có thể cắt chuỗi probing. Thường cần ba trạng thái:

```text
EMPTY
OCCUPIED
DELETED / TOMBSTONE
```

Quá nhiều tombstone làm probing dài hơn, vì vậy đôi khi phải rehash dù bảng chưa đầy.

Nếu băm (hash / 해시) dựa vào phép quay vòng số nguyên, nên dùng kiểu unsigned vì unsigned overflow trong C có ngữ nghĩa modulo xác định; signed overflow thì không.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các mẫu triển khai DSA trong C**, **Độ sâu đệ quy** tiếp nhận điểm tựa từ **Bảng băm (hash table / 해시 테이블) và cách xử lý va chạm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **const, restrict và aliasing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ sâu đệ quy

DFS đệ quy rất dễ đọc nhưng ngăn xếp (stack / 스택) hữu hạn. Cây lệch hoặc đồ thị dạng đường hàng trăm nghìn đỉnh có thể gây ngăn xếp (stack / 스택) overflow.

Ngăn xếp (stack / 스택) tường minh trên vùng nhớ động (heap / 힙) cho phép kiểm soát dung lượng và xử lý lỗi cấp phát. Thuật toán vẫn là DFS; chỉ thay cách lưu trạng thái điều khiển.

> **Chuyển mạch:** Trong **Các mẫu triển khai DSA trong C**, **const, restrict và aliasing** tiếp nhận điểm tựa từ **Độ sâu đệ quy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quy tắc mất hiệu lực** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## const, restrict và aliasing

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```c
const Node *tree_find(const Tree *tree, int key);
```

`const` thể hiện rằng hàm không được sửa dữ liệu qua con trỏ đó. Nó không chứng minh bất biến sâu nhưng giúp hợp đồng API rõ hơn.

`restrict` có thể cho trình biên dịch (compiler / 컴파일러) biết các con trỏ không alias theo hợp đồng và mở thêm cơ hội tối ưu. Dùng sai `restrict` dẫn tới undefined hành vi (behavior / 동작), vì vậy chỉ dùng khi mô hình aliasing được hiểu chắc chắn.

API cấu trúc dữ liệu nên hạn chế để lộ con trỏ nội bộ có thể thay đổi nếu không cần thiết.

> **Chuyển mạch:** Ở chặng này của **Các mẫu triển khai DSA trong C**, **Quy tắc mất hiệu lực** tiếp nhận điểm tựa từ **const, restrict và aliasing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mã lỗi và cleanup** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quy tắc mất hiệu lực

Mảng động resize có thể làm con trỏ phần tử mất hiệu lực. bảng băm (hash table / 해시 테이블) rehash làm bucket/con trỏ nội bộ mất hiệu lực. Xóa nút danh sách làm con trỏ tới nút đó mất hiệu lực. Xoay cây có thể giữ địa chỉ nút nhưng thay đổi quan hệ cha–con.

Thư viện C tốt nên ghi rõ các quy tắc này giống cách bộ chứa (container / 컨테이너) C++ mô tả iterator vô hiệu hóa (invalidation / 무효화).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các mẫu triển khai DSA trong C**, **Mã lỗi và cleanup** tiếp nhận điểm tựa từ **Quy tắc mất hiệu lực** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sao chép, clone và chuyển quyền sở hữu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mã lỗi và cleanup

`bool` đôi khi không đủ để mô tả lỗi:

```c
typedef enum {
    DS_OK,
    DS_ERR_OOM,
    DS_ERR_NOT_FOUND,
    DS_ERR_INVALID
} DsResult;
```

Hàm khởi tạo nhiều tài nguyên phải cleanup đúng khi một bước giữa thất bại. Mẫu `goto cleanup` trong C có thể làm luồng giải phóng tập trung và dễ kiểm chứng hơn nhiều nhánh lồng nhau.

Destructor có thể đặt con trỏ về `NULL` và reset siêu dữ liệu (metadata / 메타데이터) sau `free`, nhưng điều đó không làm các alias khác tự biến mất. Dùng đối tượng (object / 객체) sau khi destroy vẫn là lỗi ngữ nghĩa.

> **Chuyển mạch:** Trong **Các mẫu triển khai DSA trong C**, **Sao chép, clone và chuyển quyền sở hữu** tiếp nhận điểm tựa từ **Mã lỗi và cleanup** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Địa chỉ ổn định và lưu trữ gọn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sao chép, clone và chuyển quyền sở hữu

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```c
Tree b = a;
```

nếu `Tree` chứa con trỏ thì đây chỉ là sao chép nông. Nếu cả `a` và `b` cùng được destroy, có thể double-free.

API nên tách rõ:

```text
clone/deep_copy
move/transfer ownership
borrow reference
```

Tên hàm và hợp đồng rõ ràng giúp tránh sao chép nông ngoài ý muốn.

> **Chuyển mạch:** Ở chặng này của **Các mẫu triển khai DSA trong C**, **Địa chỉ ổn định và lưu trữ gọn** tiếp nhận điểm tựa từ **Sao chép, clone và chuyển quyền sở hữu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Biểu diễn đồ thị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Địa chỉ ổn định và lưu trữ gọn

Nút cấp phát riêng có địa chỉ ổn định nhưng locality kém. Nút tham chiếu nhau bằng chỉ mục (index / 인덱스) trong véc-tơ (vector / 벡터) có thể gọn hơn; véc-tơ (vector / 벡터) resize có thể đổi địa chỉ cơ sở nhưng chỉ mục (index / 인덱스) vẫn ổn định nếu thứ tự slot không đổi.

Lựa chọn phụ thuộc việc bên ngoài có giữ tham chiếu (reference / 참조)/handle hay không và mẫu truy cập thực tế.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các mẫu triển khai DSA trong C**, **Biểu diễn đồ thị** tiếp nhận điểm tựa từ **Địa chỉ ổn định và lưu trữ gọn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Flexible Array Member** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Biểu diễn đồ thị

Mỗi cạnh là một đối tượng (object / 객체)/nút liên kết dễ cài nhưng tốn cấp phát. Với đồ thị tĩnh, CSR gọn hơn:

```c
size_t offsets[n + 1];
int edges[m];
```

Đồ thị động có thể dùng véc-tơ (vector / 벡터) cạnh cho từng đỉnh hoặc khối (block / 블록) adjacency từ pool.

> **Chuyển mạch:** Trong **Các mẫu triển khai DSA trong C**, **Flexible Array Member** tiếp nhận điểm tựa từ **Biểu diễn đồ thị** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Intrusive dữ liệu (data / 데이터) structures** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Flexible Array Member

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```c
typedef struct {
    size_t len;
    int data[];
} Block;
```

Có thể cấp phát header và dữ liệu trong cùng một khối:

```c
malloc(sizeof(Block) + n * sizeof(int));
```

Cách này giảm một lần gián tiếp qua con trỏ và giảm số cấp phát, nhưng phép tính kích thước phải chống overflow.

> **Chuyển mạch:** Ở chặng này của **Các mẫu triển khai DSA trong C**, **Flexible Array Member** nêu điều cần giải thích; **Intrusive dữ liệu (data / 데이터) structures** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Sentinel và trạng thái tường minh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Intrusive dữ liệu (data / 데이터) structures

Sơ đồ hoặc danh sách này mô tả thứ tự phụ thuộc của các khái niệm. Hãy đọc theo mũi tên để biết phần nào là prerequisite, phần nào là ứng dụng và khi nào cần quay lại nền tảng.

```c
typedef struct Task {
    int priority;
    struct Task *next;
} Task;
```

Intrusive danh sách (list / 목록) nhúng trường liên kết trực tiếp vào đối tượng (object / 객체) người dùng nên không cần wrapper nút (node / 노드). Đổi lại, đối tượng (object / 객체) bị gắn với bố trí của cấu trúc; nếu muốn tham gia nhiều danh sách (list / 목록) có thể cần nhiều trường liên kết.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các mẫu triển khai DSA trong C**, **Intrusive dữ liệu (data / 데이터) structures** nêu điều cần giải thích; **Sentinel và trạng thái tường minh** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Bộ xác minh bất biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sentinel và trạng thái tường minh

Không nên dùng `0`, `-1` hoặc một “magic giá trị (value / 값)” làm rỗng nếu miền dữ liệu hợp lệ có thể chứa chính giá trị đó. Nên dùng kích thước (size / 크기), cờ hoặc trạng thái riêng.

Bài học này áp dụng cho tombstone của bảng băm (hash table / 해시 테이블) và `INF` trong thuật toán đồ thị.

> **Chuyển mạch:** Trong **Các mẫu triển khai DSA trong C**, **Bộ xác minh bất biến** tiếp nhận điểm tựa từ **Sentinel và trạng thái tường minh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sanitizer và phân tích tĩnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ xác minh bất biến

Cấu trúc phức tạp nên có validator dùng trong gỡ lỗi (debug / 디버그)/kiểm thử (test / 테스트).

```text
Heap       -> parent <= child
BST        -> mọi khóa nằm trong khoảng hợp lệ
LinkedList -> size khớp số nút, prev/next đối xứng
Hash Table -> số slot occupied khớp size và lookup tìm được mọi entry
```

Chạy validator sau chuỗi thao tác ngẫu nhiên giúp bắt lỗi cấu trúc ngay tại thời điểm bất biến bị phá.

> **Chuyển mạch:** Ở chặng này của **Các mẫu triển khai DSA trong C**, **Sanitizer và phân tích tĩnh** tiếp nhận điểm tựa từ **Bộ xác minh bất biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fuzzing và kiểm thử đối chiếu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sanitizer và phân tích tĩnh

Các công cụ rất hữu ích gồm:

```text
AddressSanitizer           -> out-of-bounds, use-after-free
UndefinedBehaviorSanitizer -> signed overflow, shift sai, UB khác
LeakSanitizer              -> rò rỉ bộ nhớ tùy nền tảng/toolchain
```

Valgrind, trình biên dịch (compiler / 컴파일러) warnings và static analyzer cũng giúp tìm lỗi vòng đời và khởi tạo. Nên biên dịch với cảnh báo mạnh như `-Wall -Wextra -Wconversion` và xử lý cảnh báo nghiêm túc.

Đầu ra đúng trên vài kiểm thử (test / 테스트) không chứng minh chương trình an toàn bộ nhớ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các mẫu triển khai DSA trong C**, **Sanitizer và phân tích tĩnh** đã nêu tiêu chí phân biệt, còn **Fuzzing và kiểm thử đối chiếu** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Benchmark đúng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fuzzing và kiểm thử đối chiếu

Cấu trúc dữ liệu rất phù hợp với chuỗi thao tác ngẫu nhiên:

```text
insert / delete / find
so sánh với mô hình tham chiếu đơn giản
chạy validator và sanitizer
```

Vùng nhớ vùng nhớ động (heap / 힙) tự cài đặt có thể đối chiếu chuỗi pop với bản sao dữ liệu được `qsort`. băm (hash / 해시) Set tự cài đặt có thể đối chiếu với mảng nhỏ xử lý tuyến tính.

Một oracle chậm nhưng đơn giản thường tốt hơn một oracle tối ưu phức tạp.

> **Chuyển mạch:** Trong **Các mẫu triển khai DSA trong C**, **Fuzzing và kiểm thử đối chiếu** đã nêu tiêu chí phân biệt, còn **Benchmark đúng** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **ABI và kiểu mờ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Benchmark đúng

Benchmark C nên dùng cờ tối ưu nhất quán như `-O2` hoặc `-O3`, đồng thời bảo đảm trình biên dịch (compiler / 컴파일러) không loại bỏ công việc vì kết quả không được quan sát.

Nên thử nhiều hình dạng đầu vào, đo cả cấp phát nếu cấu trúc dùng nhiều nút và phân biệt rõ bộ nhớ đệm (cache / 캐시) nóng/lạnh khi điều đó quan trọng.

> **Chuyển mạch:** Ở chặng này của **Các mẫu triển khai DSA trong C**, **ABI và kiểu mờ** tiếp nhận điểm tựa từ **Benchmark đúng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pool, luồng và atomic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ABI và kiểu mờ

Nếu công khai (public / 공개) header công khai toàn bộ `struct`, mã người dùng phụ thuộc bố trí dữ liệu. Nếu muốn đóng gói:

```c
typedef struct HashMap HashMap;
```

có thể khai báo kiểu mờ trong header và giữ trường thật trong tệp (file / 파일) `.c`. Khi đó hiện thực (implementation / 구현) có thể đổi cách biểu diễn mà không thay API công khai (public API / 공개 API).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các mẫu triển khai DSA trong C**, **Pool, luồng và atomic** tiếp nhận điểm tựa từ **ABI và kiểu mờ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pool, luồng và atomic

Allocator/pool tùy biến không tự an toàn luồng. Môi trường concurrent cần khóa, pool theo luồng hoặc giao thức đồng bộ phù hợp.

Thêm `_Atomic` vào con trỏ cũng không tự biến danh sách thành lock-free. Các vấn đề như ABA, bộ nhớ (memory / 메모리) reclamation, hazard pointer và epoch cần thiết kế thuật toán riêng.

> **Chuyển mạch:** Trong **Các mẫu triển khai DSA trong C**, **Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **Pool, luồng và atomic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Checklist triển khai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

“C luôn nhanh hơn vì gần phần cứng” — không đúng; mã cấp phát dày và locality kém có thể chậm hơn mảng trong managed thời gian chạy (runtime / 런타임).

“free xong đặt con trỏ cục bộ thành NULL là hết dangling pointer” — sai nếu alias khác vẫn tồn tại.

“Big-O đúng thì hiện thực (implementation / 구현) đúng” — sai; UB và lỗi bộ nhớ có thể phá mọi bảo đảm.

“Linked danh sách (list / 목록) chèn O(1) nên luôn nhanh hơn véc-tơ (vector / 벡터)” — bỏ qua chi phí tìm vị trí, cấp phát và bộ nhớ đệm (cache / 캐시) locality.

> **Chuyển mạch:** Ở chặng này của **Các mẫu triển khai DSA trong C**, **Checklist triển khai** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Checklist triển khai

Phần này kiểm tra ranh giới và failure mode của cơ chế vừa học. Hãy dùng nó để biết khi nào mô hình còn đúng, khi nào cần đổi chiến lược và bằng chứng nào phải thu thập.

```text
Bất biến biểu diễn là gì?
Ai sở hữu từng con trỏ và vòng đời của nó?
Allocation failure có rollback an toàn không?
Phép tính kích thước có overflow không?
Con trỏ/bộ lặp mất hiệu lực khi nào?
Độ sâu đệ quy có bị chặn không?
Comparator/hash có đúng hợp đồng không?
Có validator và random differential test chưa?
Sanitizer đã chạy sạch chưa?
Benchmark có phản ánh tải công việc thật không?
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các mẫu triển khai DSA trong C**, **Mô hình tư duy** gom các mảnh từ **Checklist triển khai** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Trong C, cấu trúc dữ liệu tồn tại đồng thời ở hai thế giới: **cấu trúc lô-gic (logic / 논리) của khóa/nút/cạnh** và **cấu trúc vật lý của byte/vùng cấp phát/con trỏ**. Tính đúng đắn và hiệu năng đều phụ thuộc cả hai.

Một triển khai DSA hoàn chỉnh không chỉ có `push`, `pop`, `find`; nó còn cần `init/destroy`, xử lý lỗi, hợp đồng quyền sở hữu (ownership / 소유권), validator, kiểm thử đối chiếu ngẫu nhiên và kiểm tra an toàn bộ nhớ.

Xem thêm: [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md), [Cross-language Testing](./03_cross_language_testing_and_benchmarking.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
