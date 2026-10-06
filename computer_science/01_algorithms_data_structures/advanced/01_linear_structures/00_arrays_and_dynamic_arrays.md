# Mảng và mảng động

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Mảng và mảng động**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. mảng cố định và mảng động khác nhau ở đâu?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Vì sao append có thể amortized O(1)?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối arrays với dynamic arrays, contiguous memory và resize, để truy cập nhanh đi cùng chi phí mở rộng.

**mảng & mảng động / 배열과 동적 배열**

mảng là một trong những cách biểu diễn (representation / 표현) quan trọng nhất của Khoa học máy tính (computer science / 컴퓨터 과학) vì nó ánh xạ **vị trí lô-gic (logic / 논리)** thành **vị trí vật lý** có thể tính được trực tiếp. Nếu phần tử có kích thước cố định `w` byte và vùng dữ liệu bắt đầu tại địa chỉ `B`, phần tử chỉ mục (index / 인덱스) `i` nằm tại:

\[
address(i)=B+i\cdot w
\]

Đây là nguồn gốc của **truy cập ngẫu nhiên (Random Access / 임의 접근)** `O(1)`: không cần lần theo chuỗi (chain / 사슬) hay tìm kiếm (search / 검색) qua các phần tử trước đó. Từ thành phần nguyên thủy (primitive / 기본 요소) này, rất nhiều cấu trúc tưởng như “không phải mảng” thực chất vẫn được xây trên mảng: đống nhị phân, bảng băm (hash table / 해시 테이블) định địa chỉ mở, bộ đệm vòng (ring buffer), cây Fenwick (Fenwick Tree), gọn cây đoạn (Segment Tree), CSR đồ thị, bitmap và nhiều numeric các cấu trúc dữ liệu.

## 1. mảng cố định và mảng động khác nhau ở đâu?

Một mảng cố định có sức chứa (capacity / 용량) cố định sau khi được tạo.

C:

```c
int a[5] = {10, 20, 30, 40, 50};
```

Java:

```java
int[] a = {10, 20, 30, 40, 50};
```

mảng động thêm hai đại lượng:

```text
size      = số phần tử logic đang dùng
capacity  = số slot đã cấp phát
```

Bất biến (invariant / 불변식) cốt lõi:

\[
0 \le kích thước (size / 크기) \le sức chứa (capacity / 용량)
\]

Khi `size == capacity`, append tiếp theo phải grow vùng lưu trữ nền. Một cách triển khai thường cấp khối (block / 블록) mới lớn hơn, bản sao (copy / 복사)/move các phần tử, rồi giải phóng khối (block / 블록) cũ.

> **Nối mạch:** **2. Vì sao append có thể amortized O(1)?** nối từ **1. mảng cố định và mảng động khác nhau ở đâu?** sang **3. Growth factor là sự đánh đổi (trade-off / 트레이드오프) bộ nhớ và resize tần suất**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Vì sao append có thể amortized O(1)?

Nếu mỗi lần đầy chỉ tăng sức chứa (capacity / 용량) thêm 1, chuỗi (sequence / 시퀀스) `n` appends sẽ bản sao (copy / 복사):

\[
1+2+3+\cdots+n=\Theta(n^2)
\]

Nếu tăng theo tỷ lệ, ví dụ nhân đôi:

```text
4 -> 8 -> 16 -> 32 -> ...
```

tổng số các phần tử bị bản sao (copy / 복사) qua toàn chuỗi (sequence / 시퀀스) là geometric series:

\[
4+8+16+\cdots+\frac n2=O(n)
\]

Do đó `n` appends có total `O(n)` và amortized `O(1)` mỗi append.

Nhưng một append riêng lẻ vẫn có thể `O(n)`. Nếu ứng dụng cần độ trễ đuôi ổn định, growth spike có thể quan trọng hơn amortized thông lượng (throughput / 처리량).

> **Nối mạch:** **3. Growth factor là sự đánh đổi (trade-off / 트레이드오프) bộ nhớ và resize tần suất** nối từ **2. Vì sao append có thể amortized O(1)?** sang **4. C cách triển khai và transactional sự thay đổi dữ liệu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Growth factor là sự đánh đổi (trade-off / 트레이드오프) bộ nhớ và resize tần suất

Nhân đôi sức chứa (capacity / 용량) giảm số lần resize nhưng có thể để trống nhiều bộ nhớ. Growth factor nhỏ hơn giảm slack nhưng tăng số lần bản sao (copy / 복사).

Ta đang cân bằng:

```text
ít resize hơn      <->      memory waste nhiều hơn
```

Trong hệ thống thực tế, thư viện (library / 라이브러리) chọn factor dựa trên bộ cấp phát/môi trường chạy (runtime) các giả định chứ không phải có một hằng số “đúng tuyệt đối”.

Shrink cũng cần hysteresis. Nếu grow khi 100% full và shrink ngay khi usage < 100%, khối lượng công việc dao động có thể resize liên tục. Một chính sách thường shrink ở threshold thấp hơn đáng kể để tránh thrashing.

> **Nối mạch:** **3. Growth factor là sự đánh đổi (trade-off / 트레이드오프) bộ nhớ và resize tần suất** đặt vấn đề; **4. C cách triển khai và transactional sự thay đổi dữ liệu** kiểm tra bằng chứng, rồi **5. con trỏ/tham chiếu vô hiệu hóa (invalidation / 무효화)** mở rộng hệ quả.

## 4. C cách triển khai và transactional sự thay đổi dữ liệu

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

```c
typedef struct {
    int *data;
    size_t size;
    size_t capacity;
} IntVector;

bool vector_push(IntVector *v, int x) {
    if (v->size == v->capacity) {
        size_t new_cap = v->capacity == 0 ? 8 : v->capacity * 2;

        if (new_cap > SIZE_MAX / sizeof *v->data) {
            return false;
        }

        int *p = realloc(v->data, new_cap * sizeof *p);
        if (p == NULL) return false;

        v->data = p;
        v->capacity = new_cap;
    }

    v->data[v->size++] = x;
    return true;
}
```

Điểm quan trọng không chỉ là `realloc`. thao tác phải giữ bất biến nếu cấp phát thất bại (fail / 실패). Ta chỉ lần ghi nhận (commit / 커밋) `data/capacity/size` sau khi có tài nguyên (resource / 자원) mới hợp lệ.

mẫu này là **prepare → validate → lần ghi nhận (commit / 커밋)** và xuất hiện trong rất nhiều có thể thay đổi các cấu trúc dữ liệu.

> **Nối mạch:** **4. C cách triển khai và transactional sự thay đổi dữ liệu** đặt vấn đề; **5. con trỏ/tham chiếu vô hiệu hóa (invalidation / 무효화)** kiểm tra bằng chứng, rồi **6. Insert giữa mảng vì sao O(n)?** mở rộng hệ quả.

## 5. con trỏ/tham chiếu vô hiệu hóa (invalidation / 무효화)

Khi mảng động grow, vùng lưu trữ nền có thể đổi địa chỉ. Trong C, mọi con trỏ tới các phần tử cũ có thể không hợp lệ. Trong C++, iterators/các tham chiếu của véc-tơ (vector / 벡터) có vô hiệu hóa (invalidation / 무효화) các quy tắc cụ thể. Trong Java, hàm gọi không thấy raw phần tử address nhưng structural modification vẫn có thể không hợp lệ iterator theo fail-fast ngữ nghĩa (semantics / 의미론) của collection.

Một API giữ con trỏ/tham chiếu lâu dài vào dynamic-array phần tử phải hiểu rõ vòng đời (lifetime) đặc tả hợp đồng (contract / 계약).

Đây là điểm khác với các cấu trúc dựa trên nút: địa chỉ nút của danh sách liên kết có thể ổn định hơn nếu nút không bị xóa, đổi lại tính cục bộ (locality) kém hơn.

> **Nối mạch:** **6. Insert giữa mảng vì sao O(n)?** nối từ **5. con trỏ/tham chiếu vô hiệu hóa (invalidation / 무효화)** sang **7. ổn định deletion và unstable deletion**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Insert giữa mảng vì sao O(n)?

Từ:

```text
[10, 20, 30, 40]
```

chèn `25` trước `30` yêu cầu dịch suffix:

```text
[10, 20, _, 30, 40]
         ↑
        25
```

Số các phần tử phải move phụ thuộc khoảng cách từ insertion điểm (point / 지점) tới cuối, trường hợp xấu nhất `O(n)`.

mảng mua `O(1)` truy cập ngẫu nhiên bằng bố trí liên tiếp theo thứ tự; đổi lại structural edit ở giữa đắt.

> **Nối mạch:** **7. ổn định deletion và unstable deletion** nối từ **6. Insert giữa mảng vì sao O(n)?** sang **8. mảng như một coordinate hệ thống**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. ổn định deletion và unstable deletion

Nếu xóa `a[i]` và phải giữ thứ tự, suffix phải shift trái: `O(n)`.

Nếu **không cần giữ thứ tự (order / 순서)**, ta có thể:

```text
swap(a[i], a[size-1])
size--
```

và xóa `O(1)`.

yêu cầu “giữ thứ tự (order / 순서)” tưởng nhỏ nhưng đổi độ phức tạp (complexity / 복잡도). Đây là bài học quan trọng khi thiết kế API: ngữ nghĩa quyết định cấu trúc (structure / 구조), cấu trúc (structure / 구조) quyết định chi phí.

> **Nối mạch:** **8. mảng như một coordinate hệ thống** nối từ **7. ổn định deletion và unstable deletion** sang **9. tính cục bộ bộ nhớ đệm và prefetch**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. mảng như một coordinate hệ thống

Chỉ mục (index / 인덱스) tạo một hệ tọa độ. Nhờ đó ta có thể biểu diễn nhiều cấu trúc (structure / 구조) bằng arithmetic thay vì con trỏ.

đống nhị phân:

```text
parent(i) = (i - 1) / 2
left(i)   = 2i + 1
right(i)  = 2i + 2
```

Ma trận (matrix / 행렬) theo thứ tự hàng:

\[
chỉ mục (index / 인덱스)(r,c)=r\cdot cols+c
\]

Fenwick cây (tree / 트리) dùng phép toán bit trên chỉ số. Segment cây (tree / 트리) dạng lặp dùng các vùng chỉ số riêng cho nút lá và nút nội bộ.

mảng mạnh không phải vì “đơn giản”, mà vì chỉ mục (index / 인덱스) arithmetic loại nhiều con trỏ siêu dữ liệu.

> **Nối mạch:** **9. tính cục bộ bộ nhớ đệm và prefetch** nối từ **8. mảng như một coordinate hệ thống** sang **10. AoS và SoA**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. tính cục bộ bộ nhớ đệm và prefetch

CPU tải bộ nhớ theo dòng bộ nhớ đệm. Sequential mảng quét có spatial tính cục bộ: khi đọc `a[i]`, các phần tử kế tiếp thường đã nằm gần trong dòng bộ nhớ đệm. bộ nạp trước của phần cứng cũng dễ dự đoán mẫu tuyến tính.

danh sách liên kết traversal có cùng `O(n)` nhưng mỗi `next` có thể trỏ tới cấp phát xa, gây trượt bộ nhớ đệm.

Vì vậy trong hệ thống thực tế, cấu trúc dựa trên mảng thường thắng cấu trúc dựa trên nút ngay cả khi Big-O giống nhau.

> **Nối mạch:** **10. AoS và SoA** nối từ **9. tính cục bộ bộ nhớ đệm và prefetch** sang **11. Dense, sparse và holey các mảng trong JavaScript**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. AoS và SoA

**mảng of Structs (AoS)**:

```c
typedef struct {
    float x, y, z;
    int id;
} Point;

Point points[n];
```

**Struct of các mảng (SoA)**:

```c
float x[n], y[n], z[n];
int id[n];
```

Nếu thuật toán luôn dùng toàn bản ghi (record / 레코드), AoS tự nhiên. Nếu vòng lặp nóng chỉ đọc `x`, SoA tránh kéo các trường không cần vào bộ nhớ đệm và có thể thuận lợi hơn cho SIMD.

Data-oriented thiết kế (design / 설계) thường bắt đầu từ câu hỏi: **hot thao tác thực sự đọc những byte nào?**

> **Nối mạch:** **11. Dense, sparse và holey các mảng trong JavaScript** nối từ **10. AoS và SoA** sang **12. Java các mảng kiểu nguyên thủy và các tập hợp dữ liệu dùng kiểu đóng hộp**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Dense, sparse và holey các mảng trong JavaScript

JavaScript `Array` không phải C mảng. Engine có thể tối ưu dense packed các mảng rất tốt, nhưng nếu tạo holes, gán chỉ mục (index / 인덱스) rất lớn hoặc trộn phần tử kinds, cách biểu diễn có thể đổi.

```js
const a = [];
a[1_000_000] = 1;
```

`length` trở thành lớn nhưng số các phần tử thực tế rất ít. Đây không phải cách tạo sparse numeric cấu trúc (structure / 구조) hiệu quả một cách tự động.

Với dữ liệu số có kích thước cố định, `Int32Array`, `Uint32Array`, `Float64Array` cho cách biểu diễn dễ dự đoán hơn, nhưng ngữ nghĩa về miền giá trị và ép kiểu phải phù hợp.

> **Nối mạch:** **11. Dense, sparse và holey các mảng trong JavaScript** đặt vấn đề; **12. Java các mảng kiểu nguyên thủy và các tập hợp dữ liệu dùng kiểu đóng hộp** kiểm tra bằng chứng, rồi **13. Multidimensional các mảng và bố trí** mở rộng hệ quả.

## 12. Java các mảng kiểu nguyên thủy và các tập hợp dữ liệu dùng kiểu đóng hộp

`int[]` lưu thành phần nguyên thủy (primitive / 기본 요소) các giá trị. `Integer[]` hoặc `ArrayList<Integer>` lưu các tham chiếu tới đóng hộp các đối tượng hoặc đóng hộp các giá trị tùy môi trường chạy tối ưu hóa (optimization / 최적화), tạo footprint/GC khác.

Nếu Dijkstra, DP hoặc DSU có hàng triệu integers, `int[]`, `long[]`, `boolean[]` thường có mô hình chi phí tốt hơn tổng quát các tập hợp dữ liệu dùng kiểu đóng hộp.

sự trừu tượng (abstraction) tiện lợi không xóa cách biểu diễn chi phí.

> **Nối mạch:** **12. Java các mảng kiểu nguyên thủy và các tập hợp dữ liệu dùng kiểu đóng hộp** đặt vấn đề; **13. Multidimensional các mảng và bố trí** kiểm tra bằng chứng, rồi **14. tổng tiền tố: tiền xử lý đổi truy vấn chi phí** mở rộng hệ quả.

## 13. Multidimensional các mảng và bố trí

Trong C, một rectangular mảng thường theo thứ tự hàng. Trong Java, `int[][]` là mảng của các tham chiếu mảng, nên rows có thể là các đối tượng riêng và thậm chí ragged.

JavaScript các mảng lồng nhau cũng là đồ thị đối tượng, không phải một ma trận phẳng bắt buộc.

Nếu cần numeric ma trận (matrix / 행렬) lớn/thân thiện với bộ nhớ đệm, mảng phẳng + manual lập chỉ mục thường cho bố trí predictable hơn:

```java
int idx = r * cols + c;
```

> **Nối mạch:** **14. tổng tiền tố: tiền xử lý đổi truy vấn chi phí** nối từ **13. Multidimensional các mảng và bố trí** sang **15. mảng hiệu: đảo chiều khối lượng công việc**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. tổng tiền tố: tiền xử lý đổi truy vấn chi phí

Với tĩnh mảng, tổng tiền tố:

\[
P[i]=a_0+a_1+\cdots+a_{i-1}
\]

cho phạm vi (range / 범위) sum:

\[
sum(L,R)=P[R+1]-P[L]
\]

Preprocess `O(n)`, mỗi truy vấn `O(1)`.

Đây là một mẫu lớn: **trả chi phí trước để truy vấn về sau rẻ hơn**.

> **Nối mạch:** **15. mảng hiệu: đảo chiều khối lượng công việc** nối từ **14. tổng tiền tố: tiền xử lý đổi truy vấn chi phí** sang **16. hai con trỏ (two pointers) và thứ tự (order / 순서) thông tin**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. mảng hiệu: đảo chiều khối lượng công việc

Nếu có nhiều các cập nhật khoảng rồi cuối cùng mới materialize các giá trị, mảng hiệu giúp mỗi cập nhật `O(1)`:

```text
diff[L] += delta
diff[R+1] -= delta
```

tổng tiền tố cuối cùng phục hồi tác động (effect / 효과) của mọi các cập nhật.

tổng tiền tố tối ưu nhiều truy vấn trên dữ liệu (data / 데이터) tĩnh. mảng hiệu tối ưu nhiều batch các cập nhật trước reconstruction. Cùng mảng nhưng cách biểu diễn được chọn theo khối lượng công việc.

> **Nối mạch:** **16. hai con trỏ (two pointers) và thứ tự (order / 순서) thông tin** nối từ **15. mảng hiệu: đảo chiều khối lượng công việc** sang **17. cửa sổ trượt và trạng thái (state / 상태) reuse**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. hai con trỏ (two pointers) và thứ tự (order / 순서) thông tin

mảng đã sắp xếp cung cấp thông tin cho phép loại ứng viên.

```js
function twoSumSorted(a, target) {
  let l = 0, r = a.length - 1;
  while (l < r) {
    const s = a[l] + a[r];
    if (s === target) return [l, r];
    if (s < target) l++;
    else r--;
  }
  return null;
}
```

Nếu sum quá nhỏ, giữ `l` và giảm `r` chỉ làm sum nhỏ hơn hoặc bằng, nên không thể giải quyết vấn đề. Vì vậy tăng `l` là an toàn.

Technique này dựa trên bất biến thứ tự chứ không phải chỉ “hai biến chỉ mục (index / 인덱스)”.

> **Nối mạch:** **17. cửa sổ trượt và trạng thái (state / 상태) reuse** nối từ **16. hai con trỏ (two pointers) và thứ tự (order / 순서) thông tin** sang **18. Circular mảng và bộ đệm vòng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. cửa sổ trượt và trạng thái (state / 상태) reuse

Cửa sổ (window / 윈도우) sum length `k`:

\[
S_{i+1}=S_i-a_i+a_{i+k}
\]

Mỗi chuyển tiếp (transition / 전이) chỉ cập nhật contribution rời/đến, thay vì tính lại cả cửa sổ (window / 윈도우). Tổng từ `O(nk)` về `O(n)`.

General lesson: nếu hai subproblems liên tiếp overlap mạnh, hãy hỏi trạng thái nào có thể reuse.

> **Nối mạch:** **18. Circular mảng và bộ đệm vòng** nối từ **17. cửa sổ trượt và trạng thái (state / 상태) reuse** sang **19. Gap bộ đệm, Piece bảng (table / 테이블) và Rope: khi insert giữa là khối lượng công việc chính**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Circular mảng và bộ đệm vòng

Nếu dãy lô-gic (logic / 논리) quay vòng, chỉ số modulo cho phép reuse fixed lưu trữ:

\[
vật lý=(head+logicalIndex)\bmod sức chứa (capacity / 용량)
\]

bộ đệm vòng dùng mảng nhưng ngữ nghĩa giống hàng đợi (queue / 큐). Nó tránh shift và cho bộ nhớ bounded, rất phù hợp audio/mạng/telemetry các bộ đệm.

Nếu sức chứa (capacity / 용량) là lũy thừa của hai, cách triển khai thấp tầng đôi khi dùng mặt nạ bit thay modulo:

```text
index & (capacity - 1)
```

nhưng chỉ đúng khi các giả định được giữ.

> **Nối mạch:** **19. Gap bộ đệm, Piece bảng (table / 테이블) và Rope: khi insert giữa là khối lượng công việc chính** nối từ **18. Circular mảng và bộ đệm vòng** sang **20. Small véc-tơ (vector / 벡터) tối ưu hóa (optimization / 최적화) và inline lưu trữ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Gap bộ đệm, Piece bảng (table / 테이블) và Rope: khi insert giữa là khối lượng công việc chính

Văn bản (text / 텍스트) editor không nên luôn dùng một contiguous mảng và shift hàng megabytes cho mỗi keystroke. **Gap bộ đệm** giữ một vùng trống quanh cursor để cục bộ insert nhanh. Piece bảng (table / 테이블)/rope dùng cách biểu diễn khác để hỗ trợ edit lớn hơn.

Bài học là: mảng động là baseline, nhưng nếu khối lượng công việc có nhiều middle edits, cách biểu diễn cần thay đổi.

> **Nối mạch:** **20. Small véc-tơ (vector / 벡터) tối ưu hóa (optimization / 최적화) và inline lưu trữ** nối từ **19. Gap bộ đệm, Piece bảng (table / 테이블) và Rope: khi insert giữa là khối lượng công việc chính** sang **21. Persistent/bất biến sau khi tạo các mảng và sao chép khi ghi**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Small véc-tơ (vector / 벡터) tối ưu hóa (optimization / 최적화) và inline lưu trữ

Một số bộ chứa (container / 컨테이너) tối ưu trường hợp kích thước nhỏ bằng cách lưu vài phần tử trực tiếp trong đối tượng, chỉ cấp phát trên vùng nhớ động (heap / 힙) khi vượt ngưỡng. Đây là **tối ưu bộ đệm/véc-tơ (vector / 벡터) nhỏ (small-buffer/small-vector optimization)**.

Nó giảm cấp phát cho dùng chung (common / 공통) small trường hợp (case / 사례) nhưng làm đối tượng lớn hơn và move/bản sao (copy / 복사) ngữ nghĩa phức tạp hơn.

Đây là ví dụ constants/bộ nhớ bố trí thay đổi thiết kế (design / 설계) dù asymptotic độ phức tạp (complexity / 복잡도) giữ nguyên.

> **Nối mạch:** **21. Persistent/bất biến sau khi tạo các mảng và sao chép khi ghi** nối từ **20. Small véc-tơ (vector / 벡터) tối ưu hóa (optimization / 최적화) và inline lưu trữ** sang **22. bí danh bộ nhớ và slice/view ngữ nghĩa**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Persistent/bất biến sau khi tạo các mảng và sao chép khi ghi

có thể thay đổi mảng cho cập nhật chỉ mục (index / 인덱스) `O(1)` nhưng thay trạng thái tại chỗ. Trong bất biến sau khi tạo/persistent hệ thống, cập nhật phải tạo lô-gic (logic / 논리) phiên bản (version / 버전) mới.

Cách đơn giản bản sao (copy / 복사) toàn mảng là `O(n)`. Persistent véc-tơ (vector / 벡터) kiểu tree-of-arrays có thể cập nhật theo đường đi `O(log_B n)` với hệ số phân nhánh lớn. sao chép khi ghi có thể trì hoãn bản sao (copy / 복사) cho tới khi một dùng chung (shared / 공유) bộ đệm cần sự thay đổi dữ liệu.

Khi yêu cầu thêm versioning/immutability, “mảng cập nhật O(1)” không còn tự động đúng.

> **Nối mạch:** **22. bí danh bộ nhớ và slice/view ngữ nghĩa** nối từ **21. Persistent/bất biến sau khi tạo các mảng và sao chép khi ghi** sang **23. chia sẻ giả trong concurrent các mảng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. bí danh bộ nhớ và slice/view ngữ nghĩa

Một slice có thể là bản sao (copy / 복사) hoặc view lên mảng nền. Nếu là view, sự thay đổi dữ liệu vùng lưu trữ nền có thể nhìn thấy qua slice và ngược lại.

C con trỏ + length gần như luôn là view. Java `Arrays.copyOfRange` tạo bản sao (copy / 복사); NIO bộ đệm có view ngữ nghĩa khác. JavaScript `TypedArray.subarray()` tạo view, còn `slice()` thường bản sao (copy / 복사) theo API ngữ nghĩa tương ứng.

API phải nói rõ quyền sở hữu (ownership / 소유권)/bí danh bộ nhớ, nếu không tính đúng đắn bug rất dễ xuất hiện.

> **Nối mạch:** **23. chia sẻ giả trong concurrent các mảng** nối từ **22. bí danh bộ nhớ và slice/view ngữ nghĩa** sang **24. Bounds, tràn số nguyên (integer overflow) và cấp phát an toàn (safety / 안전)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. chia sẻ giả trong concurrent các mảng

Hai các luồng cập nhật hai counters khác nhau nhưng nằm cùng dòng bộ nhớ đệm có thể gây tính nhất quán bộ nhớ đệm lưu lượng dù không tranh cùng lô-gic (logic / 논리) variable. Đây là **chia sẻ giả**.

Một dense mảng rất tốt cho tính cục bộ sequential, nhưng concurrent ghi (write / 쓰기) mẫu có thể cần phần đệm/sharding để giảm cache-line tranh chấp tài nguyên.

cách biểu diễn tối ưu cho single-thread không luôn tối ưu cho multi-thread.

> **Nối mạch:** **23. chia sẻ giả trong concurrent các mảng** đặt đầu vào cho **24. Bounds, tràn số nguyên (integer overflow) và cấp phát an toàn (safety / 안전)**, rồi **25. kiểm thử động các mảng bằng bất biến** mở rộng hệ quả.

## 24. Bounds, tràn số nguyên (integer overflow) và cấp phát an toàn (safety / 안전)

Trong C/hệ thống mã (code / 코드), cấp phát:

```c
malloc(count * sizeof *ptr)
```

có thể tràn số multiplication trước khi bộ cấp phát được gọi. chỉ mục (index / 인덱스) arithmetic `r * cols + c` cũng có thể tràn số nếu dimensions lớn.

Trong Java/JavaScript, out-of-bounds ngữ nghĩa khác C nhưng integer/miền giá trị số vẫn cần lập luận (reasoning / 추론). JavaScript Number mất integer precision sau `2^53-1`; TypedArray có độ rộng cố định wrap/coercion ngữ nghĩa.

> **Nối mạch:** **24. Bounds, tràn số nguyên (integer overflow) và cấp phát an toàn (safety / 안전)** đặt đầu vào cho **25. kiểm thử động các mảng bằng bất biến**, rồi **26. Khi nào mảng là lựa chọn tốt?** mở rộng hệ quả.

## 25. kiểm thử động các mảng bằng bất biến

Sau mỗi sự thay đổi dữ liệu, các bất biến có thể kiểm tra:

```text
0 <= size <= capacity
mọi element logic nằm trong [0, size)
append giữ prefix cũ
remove stable giữ relative order còn lại
reserve không đổi logical contents
resize failure không phá state cũ
```

tính chất kiểm thử (test / 테스트) có thể so custom véc-tơ (vector / 벡터) với tham chiếu danh sách (list / 목록) trên ngẫu nhiên chuỗi thao tác.

> **Nối mạch:** **26. Khi nào mảng là lựa chọn tốt?** nối từ **25. kiểm thử động các mảng bằng bất biến** sang **Mô hình tư duy**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Khi nào mảng là lựa chọn tốt?

mảng/mảng động đặc biệt mạnh khi:

```text
random access quan trọng
append nhiều
iteration nhiều
memory locality quan trọng
size thay đổi nhưng middle insert không phải hot operation
```

Nếu cần định danh nút ổn định và thường xuyên nối/tách hoặc chèn/xóa tại vị trí đã biết, cấu trúc liên kết dựa trên nút có thể phù hợp hơn. Nếu tra cứu có thứ tự hoặc truy vấn khoảng là trọng tâm, cây hoặc chỉ mục có thể phù hợp hơn.

> **Nối mạch:** **Mô hình tư duy** tổng hợp từ **26. Khi nào mảng là lựa chọn tốt?**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Mô hình tư duy

> mảng là một **coordinate hệ thống contiguous cho dữ liệu**. Nó mua truy cập ngẫu nhiên, tính cục bộ và siêu dữ liệu thấp bằng việc ràng buộc thứ tự lô-gic (logic / 논리) vào bố trí vật lý.

Mảng động thêm một lớp phân tích khấu hao để vùng lưu trữ có thể tăng kích thước. Từ đó, các đánh đổi về thay đổi kích thước, mất hiệu lực tham chiếu, chèn/xóa, hành vi bộ nhớ đệm, lát cắt và xử lý đồng thời đều có thể suy ra từ cùng cách biểu diễn này.

Xem thêm: [Linked Lists](./01_linked_lists.md), [Queues/Deque](./03_queues_deques_and_priority_queues.md), [Range Queries](../05_specialized/01_range_queries_fenwick_segment_tree.md), [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
