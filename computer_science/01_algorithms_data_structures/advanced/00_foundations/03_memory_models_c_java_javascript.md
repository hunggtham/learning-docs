# Mô hình bộ nhớ trong C, Java và JavaScript

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Mô hình bộ nhớ trong C, Java và JavaScript**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Ngăn xếp và vùng nhớ động (heap / 힙): mô hình tư duy thực dụng** gom các mảnh thành mental model có thể mang sang nhánh khác; sau đó sang **2. C: con trỏ và địa chỉ bộ nhớ** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối memory models của C, Java và JavaScript với allocation, reference và lifetime, để hiểu cùng một thao tác qua runtime khác nhau.

**bộ nhớ (memory / 메모리) mô hình (model / 모델), tham chiếu (reference / 참조) & quyền sở hữu (ownership / 소유권) / 메모리 모델, 참조와 소유권**

Cấu trúc dữ liệu cuối cùng phải tồn tại trong bộ nhớ thật. Một danh sách liên kết trên giấy chỉ là các nút nối nhau bằng mũi tên; trong chương trình, mỗi nút phải có vị trí lưu trữ, vòng đời, siêu dữ liệu và cách truy cập cụ thể. Một mảng trên giấy chỉ là dãy phần tử; trong máy, việc các phần tử nằm gần nhau cho phép CPU tận dụng bộ nhớ đệm và tính địa chỉ rất khác với việc lần theo con trỏ.

Vì vậy, **cách biểu diễn (representation / 표현)** không chỉ quyết định Big-O. Nó còn ảnh hưởng chi phí cấp phát, tính cục bộ bộ nhớ (locality), áp lực lên bộ thu gom rác, phân mảnh, chi phí con trỏ/tham chiếu và rủi ro về vòng đời dữ liệu.

## 1. Ngăn xếp và vùng nhớ động (heap / 힙): mô hình tư duy thực dụng

Ở mức DSA, có thể dùng một mô hình đơn giản. **ngăn xếp lời gọi (call stack / 호출 스택)** chứa các khung lời gọi hàm: tham số, biến cục bộ, địa chỉ quay về và thông tin quản lý. Mỗi lời gọi đệ quy thường tạo thêm một khung, vì vậy độ sâu đệ quy quá lớn có thể gây **tràn ngăn xếp (stack overflow)**.

**vùng nhớ động (heap / 힙)** chứa các vùng cấp phát động hoặc các đối tượng có vòng đời linh hoạt hơn một khung hàm. Nút của danh sách liên kết, cây, mảng nền của bảng băm và nhiều đối tượng (object / 객체) Java/JavaScript thường được mô hình hóa là sống trên vùng nhớ động (heap / 힙).

Môi trường chạy thực tế có thể tối ưu bằng **phân tích thoát (escape analysis)**, thay thế vô hướng (scalar replacement), các thế hệ GC hoặc các kỹ thuật khác. Tuy nhiên, mô hình ngăn xếp (stack / 스택)–vùng nhớ động (heap / 힙) vẫn rất hữu ích để hiểu đệ quy, cấp phát và vòng đời.

> **Chuyển mạch:** Trong **Mô hình bộ nhớ trong C, Java và JavaScript**, **2. C: con trỏ và địa chỉ bộ nhớ** gom các mảnh từ **1. Ngăn xếp và vùng nhớ động (heap / 힙): mô hình tư duy thực dụng** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **3. Quyền sở hữu trong cấu trúc liên kết bằng C** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. C: con trỏ và địa chỉ bộ nhớ

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```c
int *a = malloc(100 * sizeof(int));
if (!a) return 1;

a[0] = 42;
free(a);
```

`a` giữ địa chỉ của vùng nhớ được cấp phát. Lập trình viên phải bảo đảm vùng đó còn hợp lệ khi giải tham chiếu và được giải phóng đúng lúc.

Sau `free(a)`, giá trị con trỏ có thể vẫn còn nhưng vùng nhớ không còn thuộc một đối tượng hợp lệ. Truy cập qua con trỏ đó là **hành vi không xác định (undefined behavior)**.

C cho quyền kiểm soát cách biểu diễn rất trực tiếp, nhưng đổi lại việc quản lý **quyền sở hữu (ownership / 소유권)** và vòng đời phải được thiết kế rõ ràng.

> **Chuyển mạch:** Ở chặng này của **Mô hình bộ nhớ trong C, Java và JavaScript**, sau nội dung của **2. C: con trỏ và địa chỉ bộ nhớ**, **3. Quyền sở hữu trong cấu trúc liên kết bằng C** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **4. Bí danh bộ nhớ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Quyền sở hữu trong cấu trúc liên kết bằng C

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```c
struct Node {
    int value;
    struct Node *next;
};
```

Nếu mỗi nút được `malloc` riêng, khi hủy danh sách ta phải lưu `next`, giải phóng nút hiện tại rồi chuyển sang nút tiếp theo. Nếu một con trỏ khác vẫn trỏ tới nút đã giải phóng, ta có **con trỏ treo (dangling pointer)**. Nếu mất mọi con trỏ tới một vùng cấp phát mà chưa `free`, ta có rò rỉ bộ nhớ.

Do đó API C nên ghi rõ ai sở hữu vùng nhớ và ai chịu trách nhiệm giải phóng. Hợp đồng quyền sở hữu là một phần của tính đúng đắn, không phải chi tiết phụ của thuật toán.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình bộ nhớ trong C, Java và JavaScript**, **4. Bí danh bộ nhớ** tiếp nhận điểm tựa từ **3. Quyền sở hữu trong cấu trúc liên kết bằng C** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Cấp phát liên tiếp trong C** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Bí danh bộ nhớ

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```c
int x = 10;
int *p = &x;
int *q = &x;
*q = 20;
printf("%d", *p); // 20
```

`p` và `q` cùng trỏ tới `x`. Đây là **bí danh (aliasing)**. Thay đổi dữ liệu qua một bí danh có thể được quan sát qua bí danh khác.

Aliasing làm việc suy luận khó hơn vì một hàm có thể thay đổi vùng nhớ mà nơi gọi vẫn giữ tham chiếu tới đó. Trong cấu trúc dữ liệu, chia sẻ nút giữa nhiều cấu trúc mà không có mô hình quyền sở hữu rõ ràng dễ gây lỗi thay đổi ngoài ý muốn hoặc giải phóng hai lần.

> **Chuyển mạch:** Trong **Mô hình bộ nhớ trong C, Java và JavaScript**, **5. Cấp phát liên tiếp trong C** tiếp nhận điểm tựa từ **4. Bí danh bộ nhớ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Phần đệm và căn chỉnh của struct** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Cấp phát liên tiếp trong C

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```c
int *a = malloc(n * sizeof *a);
```

Các phần tử của mảng nằm liên tiếp trong vùng cấp phát. Địa chỉ `a + i` được tính trực tiếp từ địa chỉ cơ sở và kích thước phần tử, vì vậy truy cập theo chỉ số có chi phí hằng số.

Duyệt tuần tự còn có tính cục bộ tốt vì nhiều phần tử lân cận có thể nằm trên cùng một **dòng bộ nhớ đệm (cache line)**.

```c
struct Point { float x, y; };
struct Point points[n];
```

Mảng struct như trên có hành vi bộ nhớ khác đáng kể so với mảng con trỏ tới các `Point` được cấp phát rời rạc. Hai cách có thể cùng Big-O nhưng khác hiệu năng thực tế.

> **Chuyển mạch:** Ở chặng này của **Mô hình bộ nhớ trong C, Java và JavaScript**, **6. Phần đệm và căn chỉnh của struct** tiếp nhận điểm tựa từ **5. Cấp phát liên tiếp trong C** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Java: tham chiếu và thu gom rác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Phần đệm và căn chỉnh của struct

Trình biên dịch C có thể chèn **phần đệm (padding)** giữa các trường để đáp ứng yêu cầu **căn chỉnh (alignment)**.

```c
struct X {
    char flag;
    long value;
};
```

`sizeof(struct X)` có thể lớn hơn tổng kích thước lô-gic (logic / 논리) của hai trường. Với hàng triệu nút, vài byte phần đệm trên mỗi nút có thể trở thành nhiều megabyte.

Không nên tối ưu vi mô khi chưa cần, nhưng khi đánh giá bộ nhớ phải dùng kích thước thực tế của cấu trúc thay vì chỉ cộng kích thước các trường.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình bộ nhớ trong C, Java và JavaScript**, sau nội dung của **6. Phần đệm và căn chỉnh của struct**, **7. Java: tham chiếu và thu gom rác** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **8. Java vẫn có rò rỉ bộ nhớ ở cấp lô-gic (logic / 논리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Java: tham chiếu và thu gom rác

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

```java
Node a = new Node(10);
Node b = a;
b.value = 20;
System.out.println(a.value); // 20
```

`a` và `b` tham chiếu cùng một đối tượng. Phép gán `b = a` không sao chép đối tượng.

Bộ thu gom rác (Garbage Collector – GC) có thể thu hồi đối tượng khi nó không còn có thể đạt tới từ các **gốc GC (GC roots)**. Lập trình viên không gọi `free` như trong C.

GC loại bỏ nhiều lỗi use-after-free và double-free, nhưng quản lý bộ nhớ không trở thành miễn phí. Cấp phát, đánh dấu, sao chép, nén vùng nhớ động (heap / 힙) và các khoảng dừng GC đều có chi phí.

> **Chuyển mạch:** Trong **Mô hình bộ nhớ trong C, Java và JavaScript**, **8. Java vẫn có rò rỉ bộ nhớ ở cấp lô-gic (logic / 논리)** tiếp nhận điểm tựa từ **7. Java: tham chiếu và thu gom rác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Chi phí của đối tượng (object / 객체) Java** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Java vẫn có rò rỉ bộ nhớ ở cấp lô-gic (logic / 논리)

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

```java
static final Map<String, Object> CACHE = new HashMap<>();
```

Nếu bộ nhớ đệm (cache / 캐시) trên tăng mãi mà không có chính sách loại bỏ, các đối tượng (object / 객체) vẫn có thể đạt tới nên GC không thể thu hồi chúng. Đây là **giữ tham chiếu ngoài ý muốn (unintended retention)**.

Trong ngôn ngữ có GC, rò rỉ bộ nhớ thường không phải “quên free” mà là giữ một đường tham chiếu sống lâu hơn cần thiết.

> **Chuyển mạch:** Ở chặng này của **Mô hình bộ nhớ trong C, Java và JavaScript**, **9. Chi phí của đối tượng (object / 객체) Java** tiếp nhận điểm tựa từ **8. Java vẫn có rò rỉ bộ nhớ ở cấp lô-gic (logic / 논리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Mảng Java và đồ thị đối tượng (object / 객체)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Chi phí của đối tượng (object / 객체) Java

Một `Node` Java không chỉ chứa các trường lô-gic (logic / 논리). đối tượng (object / 객체) thường có phần đầu (object header), căn chỉnh và các tham chiếu (reference / 참조) có kích thước phụ thuộc cấu hình thời gian chạy (runtime / 런타임).

Vì vậy, danh sách liên kết chứa `Integer` có thể tốn nhiều bộ nhớ hơn đáng kể so với `int[]`. `ArrayList<Integer>` cũng phải lưu tham chiếu (reference / 참조) tới các đối tượng (object / 객체) `Integer`, thay vì lưu trực tiếp các giá trị `int` như một mảng thành phần nguyên thủy (primitive / 기본 요소).

Với DSA số học quy mô lớn, `int[]`, `long[]` hoặc các cấu trúc thành phần nguyên thủy (primitive / 기본 요소) chuyên dụng thường gọn và thân thiện với bộ nhớ đệm (cache / 캐시) hơn collection chứa đối tượng (object / 객체) đóng hộp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình bộ nhớ trong C, Java và JavaScript**, **10. Mảng Java và đồ thị đối tượng (object / 객체)** tiếp nhận điểm tựa từ **9. Chi phí của đối tượng (object / 객체) Java** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. JavaScript và định danh đối tượng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Mảng Java và đồ thị đối tượng (object / 객체)

`int[]` lưu các giá trị thành phần nguyên thủy (primitive / 기본 요소) trong một vùng mảng. `Node[]` lưu các tham chiếu (reference / 참조) liên tiếp, nhưng các đối tượng (object / 객체) mà chúng trỏ tới có thể nằm rải rác trên vùng nhớ động (heap / 힙).

Một cây biểu diễn bằng các mảng song song:

```text
value[]
left[]
right[]
```

có thể có tính cục bộ tốt hơn cách mỗi nút là một đối tượng (object / 객체) độc lập. Đây là một ví dụ của **thiết kế hướng dữ liệu (data-oriented design)**: cách bố trí được chọn theo mẫu truy cập thay vì chỉ theo mô hình đối tượng (object / 객체).

> **Chuyển mạch:** Trong **Mô hình bộ nhớ trong C, Java và JavaScript**, **11. JavaScript và định danh đối tượng** tiếp nhận điểm tựa từ **10. Mảng Java và đồ thị đối tượng (object / 객체)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Giá trị nguyên thủy và đối tượng (object / 객체) trong JavaScript** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. JavaScript và định danh đối tượng

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

```js
const a = { value: 10 };
const b = a;
b.value = 20;
console.log(a.value); // 20
```

Phép gán không sao chép sâu đối tượng (object / 객체). `a` và `b` cùng chỉ tới một định danh đối tượng.

Array, `Map`, `Set` và đối tượng (object / 객체) thông thường đều được thời gian chạy (runtime / 런타임) quản lý. Engine có thể thay đổi cách biểu diễn vật lý dựa trên kiểu dữ liệu và hình dạng đối tượng (object / 객체) quan sát được. Lập trình viên không kiểm soát bố trí trực tiếp như C, nhưng mẫu cấp phát và việc giữ tham chiếu (reference / 참조) vẫn ảnh hưởng bộ nhớ và hiệu năng.

> **Chuyển mạch:** Ở chặng này của **Mô hình bộ nhớ trong C, Java và JavaScript**, **12. Giá trị nguyên thủy và đối tượng (object / 객체) trong JavaScript** tiếp nhận điểm tựa từ **11. JavaScript và định danh đối tượng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Closure và việc giữ dữ liệu trong JavaScript** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Giá trị nguyên thủy và đối tượng (object / 객체) trong JavaScript

Các giá trị như `number`, `boolean`, `bigint` và `string` có ngữ nghĩa giá trị. đối tượng (object / 객체) có định danh riêng.

```js
const x = { a: 1 };
const y = { a: 1 };
console.log(x === y); // false
```

Hai đối tượng (object / 객체) có nội dung giống nhau vẫn không phải cùng một đối tượng (object / 객체). Điều này đặc biệt quan trọng khi dùng đối tượng (object / 객체) làm khóa của `Map` hoặc phần tử của `Set`: phép so sánh dựa trên định danh, không tự động so sánh sâu cấu trúc bên trong.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình bộ nhớ trong C, Java và JavaScript**, **12. Giá trị nguyên thủy và đối tượng (object / 객체) trong JavaScript** nêu điều cần giải thích; **13. Closure và việc giữ dữ liệu trong JavaScript** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **14. Đồ thị khả năng đạt tới là mô hình tư duy của GC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Closure và việc giữ dữ liệu trong JavaScript

Closure có thể giữ các biến sống lâu hơn thời gian thực thi của hàm tạo ra nó. Nếu một listener hoặc callback bắt giữ một đối tượng (object / 객체) lớn và listener không được tháo bỏ, đối tượng (object / 객체) đó có thể tiếp tục đạt tới được và không được GC thu hồi.

Bộ nhớ đệm (cache / 캐시), biến toàn cục, timer và tham chiếu DOM cũng có thể tạo ra tình trạng giữ dữ liệu ngoài ý muốn.

Vì vậy, dùng ngôn ngữ có GC vẫn cần hiểu đồ thị khả năng đạt tới của các đối tượng (object / 객체).

> **Chuyển mạch:** Trong **Mô hình bộ nhớ trong C, Java và JavaScript**, các dấu vết trong **13. Closure và việc giữ dữ liệu trong JavaScript** được đọc cùng nhau ở **14. Đồ thị khả năng đạt tới là mô hình tư duy của GC** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **15. Tính cục bộ bộ nhớ đệm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Đồ thị khả năng đạt tới là mô hình tư duy của GC

Có thể hình dung vùng nhớ động (heap / 힙) như một đồ thị: đối tượng (object / 객체) là đỉnh, tham chiếu (reference / 참조) là cạnh và GC roots là các điểm bắt đầu. Những đối tượng (object / 객체) có thể đạt tới từ roots được xem là còn sống.

Nếu `A` trỏ tới `B` và `B` trỏ lại `A`, nhưng không đối tượng (object / 객체) nào trong chu trình có thể đạt tới từ gốc (root / 루트), một tracing GC vẫn có thể thu hồi cả chu trình. Đây là khác biệt quan trọng so với cơ chế đếm tham chiếu đơn giản.

Mô hình này liên hệ trực tiếp với thuật toán đồ thị: giai đoạn đánh dấu của GC về bản chất là một bài toán tìm các đỉnh có thể đạt tới.

> **Chuyển mạch:** Ở chặng này của **Mô hình bộ nhớ trong C, Java và JavaScript**, **15. Tính cục bộ bộ nhớ đệm** gom các mảnh từ **14. Đồ thị khả năng đạt tới là mô hình tư duy của GC** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **16. Lần theo con trỏ và song song ở cấp bộ nhớ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Tính cục bộ bộ nhớ đệm

CPU không truy cập mọi byte bộ nhớ với chi phí đồng nhất. Dữ liệu thường được chuyển qua bộ nhớ đệm (cache / 캐시) theo từng dòng.

```text
mảng:       a[0], a[1], a[2], ...
danh sách:  node -> next -> next -> ...
```

Duyệt mảng có **tính cục bộ không gian (spatial locality)** mạnh. Danh sách liên kết có thể nhảy giữa nhiều vùng vùng nhớ động (heap / 힙) và gây nhiều trượt bộ nhớ đệm (cache miss / 캐시 미스) hơn.

Do đó hai thuật toán cùng `O(n)` vẫn có thể khác nhau lớn về thời gian chạy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình bộ nhớ trong C, Java và JavaScript**, **16. Lần theo con trỏ và song song ở cấp bộ nhớ** tiếp nhận điểm tựa từ **15. Tính cục bộ bộ nhớ đệm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Chi phí cấp phát** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Lần theo con trỏ và song song ở cấp bộ nhớ

Danh sách liên kết tạo chuỗi phụ thuộc: phải đọc nút hiện tại mới biết địa chỉ nút kế tiếp. CPU khó nạp trước nhiều bước nếu địa chỉ không dự đoán được.

Chỉ số mảng dễ dự đoán hơn, giúp cơ chế prefetch và nhiều truy cập bộ nhớ được xử lý hiệu quả hơn. Đây là một lý do mảng hoặc véc-tơ (vector / 벡터) thường được ưu tiên trong mã hiệu năng cao dù một số thao tác chèn giữa có Big-O kém hơn danh sách liên kết.

> **Chuyển mạch:** Trong **Mô hình bộ nhớ trong C, Java và JavaScript**, **17. Chi phí cấp phát** tiếp nhận điểm tựa từ **16. Lần theo con trỏ và song song ở cấp bộ nhớ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Phân mảnh bộ nhớ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Chi phí cấp phát

Cấu trúc “mỗi nút một đối tượng (object / 객체)” cần nhiều lần cấp phát. Chi phí có thể đến từ siêu dữ liệu của allocator, phân mảnh, tranh chấp hoặc áp lực GC.

Trong C/C++, **arena/pool allocator** hoặc mảng cấp phát trước có thể giảm chi phí khi nhiều đối tượng (object / 객체) có vòng đời giống nhau. Trong Java/JavaScript, giảm số đối tượng (object / 객체) tạm thời trên đường chạy nóng có thể giảm tốc độ cấp phát và khối lượng công việc của GC.

Tuy nhiên, tối ưu phải dựa trên profiling; không nên làm thiết kế khó hiểu chỉ để tránh một vài cấp phát chưa được chứng minh là nút thắt.

> **Chuyển mạch:** Ở chặng này của **Mô hình bộ nhớ trong C, Java và JavaScript**, **18. Phân mảnh bộ nhớ** tiếp nhận điểm tựa từ **17. Chi phí cấp phát** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Thay đổi dữ liệu qua tham chiếu trong ba ngôn ngữ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Phân mảnh bộ nhớ

**Phân mảnh bên ngoài (external fragmentation)** xảy ra khi tổng bộ nhớ trống có thể lớn nhưng bị chia thành nhiều vùng rời rạc không phù hợp với một yêu cầu cấp phát lớn liên tiếp.

**Phân mảnh bên trong (internal fragmentation)** là phần không gian bị lãng phí bên trong khối đã cấp phát vì khối lớn hơn nhu cầu thật.

Nhiều cấp phát nhỏ với kích thước khác nhau có hành vi khác với slab, pool hoặc arena dùng các khối đồng nhất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình bộ nhớ trong C, Java và JavaScript**, **18. Phân mảnh bộ nhớ** nêu điều cần giải thích; **19. Thay đổi dữ liệu qua tham chiếu trong ba ngôn ngữ** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. Sao chép nông và sao chép sâu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Thay đổi dữ liệu qua tham chiếu trong ba ngôn ngữ

C:

```c
void set_first(int *a) {
    a[0] = 99;
}
```

Java:

```java
void setFirst(int[] a) {
    a[0] = 99;
}
```

JavaScript:

```js
function setFirst(a) {
  a[0] = 99;
}
```

Trong cả ba ví dụ, nơi gọi quan sát được thay đổi của vùng dữ liệu. Nhưng cơ chế ngôn ngữ và bảo đảm vòng đời khác nhau.

C truyền giá trị con trỏ. Java luôn truyền tham số theo giá trị; với đối tượng (object / 객체) hoặc array, giá trị được truyền là một tham chiếu (reference / 참조). JavaScript cũng truyền giá trị; với đối tượng (object / 객체), giá trị đó dẫn tới cùng một định danh đối tượng (object / 객체).

Vì vậy, cách nói “pass by tham chiếu (reference / 참조)” dễ gây hiểu sai nếu không phân biệt cơ chế truyền tham số với việc nhiều biến cùng truy cập một đối tượng (object / 객체).

> **Chuyển mạch:** Trong **Mô hình bộ nhớ trong C, Java và JavaScript**, **19. Thay đổi dữ liệu qua tham chiếu trong ba ngôn ngữ** nêu điều cần giải thích; **20. Sao chép nông và sao chép sâu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **21. Độ sâu đệ quy và ngăn xếp tường minh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Sao chép nông và sao chép sâu

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```js
const a = [{ x: 1 }];
const b = [...a];
b[0].x = 9;
console.log(a[0].x); // 9
```

`a` và `b` là hai mảng ngoài khác nhau, nhưng phần tử bên trong vẫn là cùng một đối tượng (object / 객체). Đây là **sao chép nông (shallow copy)**.

Trong Java, constructor sao chép hoặc `clone()` cũng có thể chỉ sao chép tham chiếu (reference / 참조). Trong C, `memcpy` một struct chứa con trỏ chỉ sao chép giá trị con trỏ chứ không tự sao chép vùng dữ liệu được trỏ tới.

Các cấu trúc dữ liệu bất biến hoặc persistent có thể chủ động dùng **chia sẻ cấu trúc (structural sharing)**; ngược lại, với cấu trúc có thể thay đổi, chia sẻ ngoài ý muốn dễ gây lỗi aliasing.

> **Chuyển mạch:** Ở chặng này của **Mô hình bộ nhớ trong C, Java và JavaScript**, **21. Độ sâu đệ quy và ngăn xếp tường minh** tiếp nhận điểm tựa từ **20. Sao chép nông và sao chép sâu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Không nên mặc định có tối ưu lời gọi đuôi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Độ sâu đệ quy và ngăn xếp tường minh

Mỗi lời gọi đệ quy thường dùng thêm một khung ngăn xếp. DFS trên cây cân bằng có độ sâu `O(log n)`, trong khi cây lệch hoặc đồ thị dạng đường có thể đạt `O(n)`.

Một DFS trên đường dài `10^5` đỉnh có thể vượt giới hạn ngăn xếp (stack / 스택) trong C, Java hoặc JavaScript tùy môi trường.

Chuyển sang ngăn xếp tường minh:

```text
call stack  -> container do chương trình quản lý
```

không thay đổi bản chất DFS; nó chỉ thay đổi cách lưu trạng thái điều khiển và giúp ta kiểm soát bộ nhớ tốt hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình bộ nhớ trong C, Java và JavaScript**, **22. Không nên mặc định có tối ưu lời gọi đuôi** tiếp nhận điểm tựa từ **21. Độ sâu đệ quy và ngăn xếp tường minh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Biểu diễn số cũng là vấn đề bộ nhớ và tính đúng đắn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Không nên mặc định có tối ưu lời gọi đuôi

Một số ngôn ngữ hoặc thời gian chạy (runtime / 런타임) có thể tối ưu **lời gọi đuôi (tail call)** trong điều kiện nhất định, nhưng Java không bảo đảm loại bỏ lời gọi đuôi tổng quát. Với JavaScript, không nên giả định mọi engine và môi trường triển khai đều biến đệ quy đuôi thành cách thực thi có độ sâu ngăn xếp (stack / 스택) hằng số.

Nếu độ sâu có thể lớn, thiết kế lặp với ngăn xếp (stack / 스택) tường minh thường an toàn và dễ dự đoán hơn.

> **Chuyển mạch:** Trong **Mô hình bộ nhớ trong C, Java và JavaScript**, **23. Biểu diễn số cũng là vấn đề bộ nhớ và tính đúng đắn** tiếp nhận điểm tựa từ **22. Không nên mặc định có tối ưu lời gọi đuôi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Chia sẻ giả và trực giác về xử lý đồng thời** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Biểu diễn số cũng là vấn đề bộ nhớ và tính đúng đắn

Trong C, độ rộng số nguyên phụ thuộc kiểu và các ràng buộc của nền tảng; tràn số nguyên có dấu dẫn tới hành vi không xác định trong nhiều trường hợp theo chuẩn C.

Trong Java, `int` là số nguyên có dấu 32 bit và `long` là 64 bit; phép toán tràn theo ngữ nghĩa bù hai của ngôn ngữ.

JavaScript `Number` dùng IEEE-754 double và chỉ bảo đảm biểu diễn chính xác số nguyên đến:

\[
2^{53}-1
\]

`BigInt` hỗ trợ số nguyên có độ lớn tùy ý nhưng không thể trộn trực tiếp với phép toán `Number`.

Khoảng cách, số đếm, prefix sum hoặc chi phí của thuật toán có thể sai hoàn toàn nếu kiểu số được chọn không đủ miền giá trị.

> **Chuyển mạch:** Ở chặng này của **Mô hình bộ nhớ trong C, Java và JavaScript**, **24. Chia sẻ giả và trực giác về xử lý đồng thời** tiếp nhận điểm tựa từ **23. Biểu diễn số cũng là vấn đề bộ nhớ và tính đúng đắn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Array of Structures và cấu trúc (structure / 구조) of Arrays** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Chia sẻ giả và trực giác về xử lý đồng thời

Trong chương trình đa luồng, hai luồng có thể cập nhật hai biến lô-gic (logic / 논리) độc lập nhưng nằm trên cùng một bộ nhớ đệm (cache / 캐시) line. Cơ chế nhất quán bộ nhớ đệm (cache / 캐시) khi đó có thể khiến dòng bộ nhớ đệm (cache / 캐시) liên tục chuyển quyền sở hữu giữa các lõi. Hiện tượng này gọi là **chia sẻ giả (false sharing)**.

Đây là ví dụ cho thấy bố trí bộ nhớ ảnh hưởng hiệu năng song song dù giữa hai biến không có phụ thuộc dữ liệu ở cấp thuật toán.

Với hàng đợi đồng thời, bộ đếm hoặc thuật toán đồ thị song song, cần nhìn xa hơn Big-O và xét cả tranh chấp cùng hành vi cache-coherence.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình bộ nhớ trong C, Java và JavaScript**, **25. Array of Structures và cấu trúc (structure / 구조) of Arrays** tiếp nhận điểm tựa từ **24. Chia sẻ giả và trực giác về xử lý đồng thời** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Khi dữ liệu vượt khỏi RAM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Array of Structures và cấu trúc (structure / 구조) of Arrays

**Mảng các cấu trúc (Array of Structures – AoS):**

```text
[{x,y,z}, {x,y,z}, ...]
```

**Cấu trúc các mảng (structure of Arrays – SoA):**

```text
x[]
y[]
z[]
```

Nếu phép tính chỉ quét `x`, SoA có thể tận dụng bộ nhớ đệm (cache / 캐시) và vectorization tốt hơn vì không cần tải `y` và `z`. Nếu thường xuyên cần toàn bộ bản ghi cùng lúc, AoS có thể tự nhiên hơn.

Cách triển khai DSA trong hệ thống thực tế đôi khi phải chọn bố trí vật lý theo mẫu truy cập chứ không chỉ theo kiểu dữ liệu trừu tượng.

> **Chuyển mạch:** Trong **Mô hình bộ nhớ trong C, Java và JavaScript**, **25. Array of Structures và cấu trúc (structure / 구조) of Arrays** nêu điều cần giải thích; **26. Khi dữ liệu vượt khỏi RAM** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **27. Độ phức tạp bộ nhớ phải tính cả hệ số thực tế** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Khi dữ liệu vượt khỏi RAM

Khi dữ liệu không vừa bộ nhớ chính, chi phí quan trọng có thể chuyển từ lệnh CPU sang I/O theo trang hoặc khối.

B+cây (tree / 트리) tăng hệ số phân nhánh để giảm chiều cao và số lần đọc trang. **Sắp xếp trộn ngoài (external merge sort)** ưu tiên đọc/ghi tuần tự các run thay vì truy cập ngẫu nhiên. Bộ đệm và kích thước trang trở thành thành phần trung tâm của thiết kế.

Điều này cho thấy mô hình độ phức tạp phải phù hợp với tầng phần cứng. `O(log n)` trong mô hình RAM chưa nói hết chi phí nếu mỗi bước có thể là một lần I/O đĩa.

> **Chuyển mạch:** Ở chặng này của **Mô hình bộ nhớ trong C, Java và JavaScript**, **26. Khi dữ liệu vượt khỏi RAM** nêu điều cần giải thích; **27. Độ phức tạp bộ nhớ phải tính cả hệ số thực tế** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **28. Cấu trúc persistent và bất biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Độ phức tạp bộ nhớ phải tính cả hệ số thực tế

Nói bảng băm (hash table / 해시 테이블) và cây (tree / 트리) đều dùng `O(n)` bộ nhớ là đúng về tiệm cận nhưng chưa đủ để lập kế hoạch dung lượng.

Bảng băm (hash table / 해시 테이블) có dung lượng dự phòng theo hệ số tải. cây (tree / 트리) có tham chiếu (reference / 참조)/con trỏ, siêu dữ liệu (metadata / 메타데이터) cân bằng và đối tượng (object / 객체) header. Trie có thể dành nhiều ô cho cạnh con. Danh sách kề của đồ thị có thể có chi phí trên từng cạnh.

Khi `n` lớn, các hệ số hằng này có thể quyết định cấu trúc có khả thi hay không.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình bộ nhớ trong C, Java và JavaScript**, **28. Cấu trúc persistent và bất biến** tiếp nhận điểm tựa từ **27. Độ phức tạp bộ nhớ phải tính cả hệ số thực tế** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Benchmark có ý thức về bộ nhớ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Cấu trúc persistent và bất biến

**Cấu trúc dữ liệu persistent** không phá hủy phiên bản cũ khi cập nhật. Thay vào đó, nó tạo các nút mới và chia sẻ những phần không đổi.

Ví dụ, cập nhật một cây persistent cân bằng có thể chỉ sao chép `O(log n)` nút trên đường từ gốc tới vị trí cập nhật thay vì sao chép toàn bộ cây.

Structural sharing giúp duy trì nhiều phiên bản hiệu quả nhưng làm tăng số lần cấp phát và đòi hỏi mô hình vòng đời phù hợp. Đây là một đánh đổi khác giữa bộ nhớ, tính bất biến và khả năng chia sẻ.

> **Chuyển mạch:** Trong **Mô hình bộ nhớ trong C, Java và JavaScript**, **29. Benchmark có ý thức về bộ nhớ** tiếp nhận điểm tựa từ **28. Cấu trúc persistent và bất biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Benchmark có ý thức về bộ nhớ

Nếu hai cấu trúc có cùng Big-O, benchmark vẫn nên đo lượng cấp phát, bộ nhớ cực đại, locality và hành vi GC.

Danh sách liên kết có thể thua mảng khi duyệt tuần tự. Đồ thị gồm nhiều đối tượng (object / 객체) nhỏ có thể tốn bộ nhớ hơn CSR bằng mảng phẳng. băm (hash / 해시) Map chứa khóa đóng hộp có thể lớn hơn nhiều so với map thành phần nguyên thủy (primitive / 기본 요소) chuyên dụng.

Một tuyên bố về hiệu năng chỉ đáng tin khi khối lượng công việc, cách biểu diễn và môi trường chạy được mô tả cụ thể.

> **Chuyển mạch:** Ở chặng này của **Mô hình bộ nhớ trong C, Java và JavaScript**, **Mô hình tư duy** gom các mảnh từ **29. Benchmark có ý thức về bộ nhớ** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Cấu trúc dữ liệu trong máy thật là **thuật toán + cách biểu diễn vật lý + mô hình vòng đời**.

Mảng mạnh không chỉ vì lập chỉ mục `O(1)` mà còn nhờ tính cục bộ. Cấu trúc liên kết linh hoạt không chỉ vì có thể nối lại con trỏ mà còn phải trả chi phí cấp phát và lần theo con trỏ. GC loại bỏ việc `free` thủ công nhưng không loại bỏ chi phí cấp phát hoặc việc giữ đối tượng (object / 객체) quá lâu. C cho quyền kiểm soát quyền sở hữu (ownership / 소유권) trực tiếp; Java và JavaScript quản lý vòng đời theo khả năng đạt tới nhưng vẫn cần hiểu định danh (identity / 식별자), aliasing và áp lực bộ nhớ.

Khi chọn cấu trúc, hãy hỏi đồng thời: **độ phức tạp thao tác là gì, dữ liệu được bố trí thế nào, mỗi đối tượng (object / 객체) sống bao lâu, và thời gian chạy (runtime / 런타임)/phần cứng sẽ truy cập cách biểu diễn đó ra sao?**

Xem thêm: [Arrays & Dynamic Arrays](../01_linear_structures/00_arrays_and_dynamic_arrays.md), [Linked Lists](../01_linear_structures/01_linked_lists.md), [C Implementation Patterns](../80_language_implementations/00_c_dsa_implementation_patterns.md), [JavaScript Runtime Patterns](../80_language_implementations/02_javascript_dsa_runtime_patterns.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
