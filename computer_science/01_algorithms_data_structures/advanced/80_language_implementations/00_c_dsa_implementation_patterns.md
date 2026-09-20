# Các mẫu triển khai DSA trong C
**C DSA Implementation Patterns / C 자료구조 구현 패턴**

C là ngôn ngữ rất tốt để học DSA vì nó làm lộ rõ những gì runtime cấp cao thường che đi: bố trí bộ nhớ, số học con trỏ, cấp phát, quyền sở hữu (ownership), vòng đời và xử lý lỗi. Vì vậy một cấu trúc dữ liệu C chỉ thực sự đúng khi đồng thời giữ được **bất biến logic** của thuật toán và **bất biến vòng đời/quyền sở hữu** của bộ nhớ.

Một heap có thể giữ đúng thứ tự nhưng vẫn sai vì ghi vượt bộ đệm. Một danh sách có thể cho kết quả đúng trên ví dụ nhỏ nhưng vẫn chứa con trỏ treo. Học DSA bằng C là học cả thuật toán lẫn cách biểu diễn.

## Quyền sở hữu là một phần của hợp đồng API

Một container lưu con trỏ thường có ba lựa chọn ngữ nghĩa:

```text
sở hữu object
mượn object
sao chép object/giá trị
```

Nếu container sở hữu dữ liệu, nó phải biết cách hủy dữ liệu. Một API tổng quát có thể nhận callback:

```c
typedef void (*destroy_fn)(void *);
```

Nếu quyền sở hữu không rõ, các lỗi thường gặp là double-free, use-after-free, rò rỉ bộ nhớ hoặc giải phóng bằng sai allocator.

Một API tốt phải trả lời: ai tạo/hủy container, ai sở hữu phần tử, con trỏ trả về sống tới khi nào và thao tác nào làm con trỏ/bộ lặp mất hiệu lực.

## Mảng động

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

Nếu mỗi lần đầy chỉ tăng capacity thêm 1, tổng chi phí sao chép của nhiều lần append trở thành bậc hai. Tăng theo cấp số nhân, ví dụ nhân 2 hoặc khoảng 1.5, cho append `O(1)` khấu hao.

Phải kiểm tra overflow trước khi tính kích thước cấp phát:

```c
if (capacity > SIZE_MAX / 2) return false;
if (new_capacity > SIZE_MAX / sizeof *v->data) return false;
```

## realloc và mất hiệu lực của con trỏ

```c
int *new_data = realloc(v->data, new_cap * sizeof *v->data);
if (!new_data) return false;

v->data = new_data;
v->capacity = new_cap;
```

Không nên ghi trực tiếp kết quả `realloc` vào con trỏ cũ nếu muốn giữ vùng cũ khi cấp phát thất bại. `realloc` thành công có thể di chuyển buffer, vì vậy mọi con trỏ tới phần tử cũ có thể mất hiệu lực.

Đây là ví dụ cách biểu diễn bộ nhớ tạo ra ngữ nghĩa API.

## Cập nhật theo kiểu giao dịch

Một thay đổi cấu trúc nên theo mẫu:

```text
chuẩn bị tài nguyên mới
xác nhận thành công
commit thay đổi cấu trúc
sau đó giải phóng trạng thái cũ
```

Ví dụ resize Hash Table: cấp phát bảng mới, rehash thành công, đổi con trỏ/capacity rồi mới giải phóng bảng cũ. Nếu cập nhật nửa chừng rồi cấp phát thất bại, cấu trúc có thể bị hỏng.

## Danh sách liên kết

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

Nút canh gác (sentinel) có thể giảm số trường hợp đặc biệt ở đầu/cuối danh sách và làm logic nối lại đồng đều hơn.

## Stack, queue và bộ đệm vòng

Stack bằng mảng thường có locality tốt và ít cấp phát. Queue có thể dùng **bộ đệm vòng (ring buffer)** để tránh dịch chuyển phần tử.

```c
index = (index + 1) % capacity;
```

Nếu capacity luôn là lũy thừa của 2:

```c
index = (index + 1) & (capacity - 1);
```

Tối ưu bằng bitmask chỉ đúng khi bất biến capacity được duy trì.

Có nhiều quy ước ring buffer như `head + size`, `head/tail + one-empty-slot` hoặc thêm cờ `full`. Phải chọn một mô hình và dùng nhất quán.

## Container tổng quát với void*

```c
typedef int (*compare_fn)(const void *, const void *);
```

`void *` cho phép viết heap, BST hoặc sort tổng quát nhưng đổi lại mất một phần an toàn kiểu tĩnh, cần cast và làm hợp đồng ownership phức tạp hơn.

Macro có thể sinh container theo kiểu cụ thể, giảm cast nhưng làm debug và thông báo lỗi khó hơn. C không có generics native, vì vậy đây là một đánh đổi thiết kế thực sự.

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

`qsort` tiện dụng nhưng gọi comparator qua function pointer và API `void *`. Trong đường chạy số học rất nóng, sort chuyên biệt có thể nhanh hơn, nhưng chỉ nên thay thế sau khi đo.

## Padding, alignment và bố trí dữ liệu

```c
typedef struct {
    char flag;
    int value;
    void *next;
} Node;
```

Compiler có thể chèn padding để căn chỉnh. `sizeof(Node)` mới là chi phí thực tế.

**Array of Structures (AoS)** phù hợp khi thường đọc toàn bản ghi. **Structure of Arrays (SoA)** có thể tốt hơn nếu thuật toán chủ yếu quét một vài trường vì tăng locality và khả năng vectorization.

Cách bố trí nên phù hợp mẫu truy cập.

## Arena và pool allocator

Cấu trúc nhiều nút gọi `malloc` cho từng nút có thể tốn metadata và gây phân mảnh.

Arena cấp phát một khối lớn rồi chia tuần tự thành các nút. Nó nhanh, có locality tốt và rất phù hợp khi nhiều object có cùng vòng đời, nhưng khó giải phóng riêng từng nút.

Pool với free-list phù hợp khi object có kích thước cố định và thường xuyên được tái sử dụng:

```text
free node     -> đưa vào free list
allocate node -> lấy từ free list trước khi xin vùng mới
```

Nếu bên ngoài giữ handle lâu dài, generation counter `(index, generation)` giúp phát hiện handle cũ sau khi slot được tái sử dụng.

## Handle thay cho con trỏ thô

Khi storage có thể di chuyển hoặc compact, public API giữ raw pointer rất rủi ro. Một handle số nguyên có thể ánh xạ tới slot nội bộ. Nếu storage di chuyển, ánh xạ thay đổi nhưng handle vẫn ổn định.

Mẫu này phổ biến trong game engine và ECS.

## Hash Table và cách xử lý va chạm

**Separate chaining** lưu bucket trỏ tới danh sách entry. **Open addressing** lưu entry trực tiếp trong bảng và thường có locality tốt hơn, nhưng probing, hệ số tải và xóa phức tạp hơn.

Khi xóa trong open addressing, không thể luôn đặt slot thành `EMPTY` vì có thể cắt chuỗi probing. Thường cần ba trạng thái:

```text
EMPTY
OCCUPIED
DELETED / TOMBSTONE
```

Quá nhiều tombstone làm probing dài hơn, vì vậy đôi khi phải rehash dù bảng chưa đầy.

Nếu hash dựa vào phép quay vòng số nguyên, nên dùng kiểu unsigned vì unsigned overflow trong C có ngữ nghĩa modulo xác định; signed overflow thì không.

## Độ sâu đệ quy

DFS đệ quy rất dễ đọc nhưng stack hữu hạn. Cây lệch hoặc đồ thị dạng đường hàng trăm nghìn đỉnh có thể gây stack overflow.

Stack tường minh trên heap cho phép kiểm soát dung lượng và xử lý lỗi cấp phát. Thuật toán vẫn là DFS; chỉ thay cách lưu trạng thái điều khiển.

## const, restrict và aliasing

```c
const Node *tree_find(const Tree *tree, int key);
```

`const` thể hiện rằng hàm không được sửa dữ liệu qua con trỏ đó. Nó không chứng minh bất biến sâu nhưng giúp hợp đồng API rõ hơn.

`restrict` có thể cho compiler biết các con trỏ không alias theo hợp đồng và mở thêm cơ hội tối ưu. Dùng sai `restrict` dẫn tới undefined behavior, vì vậy chỉ dùng khi mô hình aliasing được hiểu chắc chắn.

API cấu trúc dữ liệu nên hạn chế để lộ con trỏ nội bộ có thể thay đổi nếu không cần thiết.

## Quy tắc mất hiệu lực

Mảng động resize có thể làm con trỏ phần tử mất hiệu lực. Hash Table rehash làm bucket/con trỏ nội bộ mất hiệu lực. Xóa nút danh sách làm con trỏ tới nút đó mất hiệu lực. Xoay cây có thể giữ địa chỉ nút nhưng thay đổi quan hệ cha–con.

Thư viện C tốt nên ghi rõ các quy tắc này giống cách container C++ mô tả iterator invalidation.

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

Destructor có thể đặt con trỏ về `NULL` và reset metadata sau `free`, nhưng điều đó không làm các alias khác tự biến mất. Dùng object sau khi destroy vẫn là lỗi ngữ nghĩa.

## Sao chép, clone và chuyển quyền sở hữu

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

## Địa chỉ ổn định và lưu trữ gọn

Nút cấp phát riêng có địa chỉ ổn định nhưng locality kém. Nút tham chiếu nhau bằng index trong vector có thể gọn hơn; vector resize có thể đổi địa chỉ cơ sở nhưng index vẫn ổn định nếu thứ tự slot không đổi.

Lựa chọn phụ thuộc việc bên ngoài có giữ reference/handle hay không và mẫu truy cập thực tế.

## Biểu diễn đồ thị

Mỗi cạnh là một object/nút liên kết dễ cài nhưng tốn cấp phát. Với đồ thị tĩnh, CSR gọn hơn:

```c
size_t offsets[n + 1];
int edges[m];
```

Đồ thị động có thể dùng vector cạnh cho từng đỉnh hoặc block adjacency từ pool.

## Flexible Array Member

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

## Intrusive data structures

```c
typedef struct Task {
    int priority;
    struct Task *next;
} Task;
```

Intrusive list nhúng trường liên kết trực tiếp vào object người dùng nên không cần wrapper node. Đổi lại, object bị gắn với bố trí của cấu trúc; nếu muốn tham gia nhiều list có thể cần nhiều trường liên kết.

## Sentinel và trạng thái tường minh

Không nên dùng `0`, `-1` hoặc một “magic value” làm rỗng nếu miền dữ liệu hợp lệ có thể chứa chính giá trị đó. Nên dùng size, cờ hoặc trạng thái riêng.

Bài học này áp dụng cho tombstone của Hash Table và `INF` trong thuật toán đồ thị.

## Bộ xác minh bất biến

Cấu trúc phức tạp nên có validator dùng trong debug/test.

```text
Heap       -> parent <= child
BST        -> mọi khóa nằm trong khoảng hợp lệ
LinkedList -> size khớp số nút, prev/next đối xứng
Hash Table -> số slot occupied khớp size và lookup tìm được mọi entry
```

Chạy validator sau chuỗi thao tác ngẫu nhiên giúp bắt lỗi cấu trúc ngay tại thời điểm bất biến bị phá.

## Sanitizer và phân tích tĩnh

Các công cụ rất hữu ích gồm:

```text
AddressSanitizer           -> out-of-bounds, use-after-free
UndefinedBehaviorSanitizer -> signed overflow, shift sai, UB khác
LeakSanitizer              -> rò rỉ bộ nhớ tùy nền tảng/toolchain
```

Valgrind, compiler warnings và static analyzer cũng giúp tìm lỗi vòng đời và khởi tạo. Nên biên dịch với cảnh báo mạnh như `-Wall -Wextra -Wconversion` và xử lý cảnh báo nghiêm túc.

Đầu ra đúng trên vài test không chứng minh chương trình an toàn bộ nhớ.

## Fuzzing và kiểm thử đối chiếu

Cấu trúc dữ liệu rất phù hợp với chuỗi thao tác ngẫu nhiên:

```text
insert / delete / find
so sánh với mô hình tham chiếu đơn giản
chạy validator và sanitizer
```

Heap tự cài đặt có thể đối chiếu chuỗi pop với bản sao dữ liệu được `qsort`. Hash Set tự cài đặt có thể đối chiếu với mảng nhỏ xử lý tuyến tính.

Một oracle chậm nhưng đơn giản thường tốt hơn một oracle tối ưu phức tạp.

## Benchmark đúng

Benchmark C nên dùng cờ tối ưu nhất quán như `-O2` hoặc `-O3`, đồng thời bảo đảm compiler không loại bỏ công việc vì kết quả không được quan sát.

Nên thử nhiều hình dạng đầu vào, đo cả cấp phát nếu cấu trúc dùng nhiều nút và phân biệt rõ cache nóng/lạnh khi điều đó quan trọng.

## ABI và kiểu mờ

Nếu public header công khai toàn bộ `struct`, mã người dùng phụ thuộc bố trí dữ liệu. Nếu muốn đóng gói:

```c
typedef struct HashMap HashMap;
```

có thể khai báo kiểu mờ trong header và giữ trường thật trong file `.c`. Khi đó implementation có thể đổi cách biểu diễn mà không thay public API.

## Pool, luồng và atomic

Allocator/pool tùy biến không tự an toàn luồng. Môi trường concurrent cần khóa, pool theo luồng hoặc giao thức đồng bộ phù hợp.

Thêm `_Atomic` vào con trỏ cũng không tự biến danh sách thành lock-free. Các vấn đề như ABA, memory reclamation, hazard pointer và epoch cần thiết kế thuật toán riêng.

## Những hiểu lầm phổ biến

“C luôn nhanh hơn vì gần phần cứng” — không đúng; mã cấp phát dày và locality kém có thể chậm hơn mảng trong managed runtime.

“free xong đặt con trỏ cục bộ thành NULL là hết dangling pointer” — sai nếu alias khác vẫn tồn tại.

“Big-O đúng thì implementation đúng” — sai; UB và lỗi bộ nhớ có thể phá mọi bảo đảm.

“Linked List chèn O(1) nên luôn nhanh hơn vector” — bỏ qua chi phí tìm vị trí, cấp phát và cache locality.

## Checklist triển khai

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

## Mô hình tư duy

> Trong C, cấu trúc dữ liệu tồn tại đồng thời ở hai thế giới: **cấu trúc logic của khóa/nút/cạnh** và **cấu trúc vật lý của byte/vùng cấp phát/con trỏ**. Tính đúng đắn và hiệu năng đều phụ thuộc cả hai.

Một triển khai DSA hoàn chỉnh không chỉ có `push`, `pop`, `find`; nó còn cần `init/destroy`, xử lý lỗi, hợp đồng ownership, validator, kiểm thử đối chiếu ngẫu nhiên và kiểm tra an toàn bộ nhớ.

Xem thêm: [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md), [Cross-language Testing](./03_cross_language_testing_and_benchmarking.md).