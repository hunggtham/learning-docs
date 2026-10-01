# Selection, k-th phần tử và Top-K

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Selection, k-th phần tử và Top-K**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. thống kê thứ tự** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Full Sort là baseline, không phải luôn sai** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Selection các thuật toán, thứ tự (order / 순서) thống kê & Top-K / 선택 알고리즘과 Top-K**

Bài toán chọn (selection) yêu cầu ít thông tin hơn sắp xếp: **không cần biết toàn bộ thứ tự tương đối của mọi phần tử, chỉ cần một hạng hoặc một nhóm nhỏ quanh ranh giới**. Nếu chỉ cần phần tử nhỏ thứ `k`, sắp xếp toàn bộ tạo nhiều thông tin hơn đầu ra yêu cầu.

Đây là một principle rất quan trọng của thuật toán thiết kế (design / 설계):

> Đừng trả chi phí để tính thông tin mà đặc tả hợp đồng (contract / 계약) không cần.

## 1. thống kê thứ tự

Nếu mảng sorted tăng dần:

```text
[2, 4, 7, 9, 13]
```

- smallest = thống kê thứ tự 1;
- median = thống kê thứ tự giữa;
- percentile = thống kê thứ tự ở một rank xác định.

API phải định nghĩa `k` zero-based hay one-based. Nếu mã (code / 코드) dùng zero-based, “phần tử nhỏ thứ k” thường map thành chỉ mục (index / 인덱스) `k-1` theo ngôn ngữ tự nhiên. Đây là nguồn off-by-one phổ biến.

> **Chuyển mạch:** Trong **Selection, k-th phần tử và Top-K**, **2. Full Sort là baseline, không phải luôn sai** tiếp nhận điểm tựa từ **1. thống kê thứ tự** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Partition là thành phần nguyên thủy (primitive / 기본 요소) cốt lõi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Full Sort là baseline, không phải luôn sai

Sort rồi lấy rank:

\[
O(n\log n)
\]

Nếu sau đó còn hàng nghìn các truy vấn có thứ tự, sorting một lần có thể tốt hơn selection riêng lẻ. Nếu chỉ một rank one-shot, có thể làm ít công việc (work / 작업) hơn.

Selection vs sorting là sự đánh đổi (trade-off / 트레이드오프) giữa:

```text
single query, ít information
vs
preprocess toàn order cho nhiều query
```

> **Chuyển mạch:** Ở chặng này của **Selection, k-th phần tử và Top-K**, **3. Partition là thành phần nguyên thủy (primitive / 기본 요소) cốt lõi** tiếp nhận điểm tựa từ **2. Full Sort là baseline, không phải luôn sai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Quickselect** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Partition là thành phần nguyên thủy (primitive / 기본 요소) cốt lõi

Chọn pivot và rearrange dữ liệu (data / 데이터) thành regions:

```text
< pivot | pivot | >= pivot
```

hoặc three-way:

```text
< pivot | == pivot | > pivot
```

Sau partition, nếu pivot/phạm vi (range / 범위) equal nằm đúng vùng hạng, ta đã tìm answer mà không cần sort từng phía.

Partition chính là cơ chế (mechanism / 메커니즘) biến một phép so sánh với pivot thành **toàn cục elimination of các ứng viên**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Selection, k-th phần tử và Top-K**, **4. Quickselect** tiếp nhận điểm tựa từ **3. Partition là thành phần nguyên thủy (primitive / 기본 요소) cốt lõi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. ngẫu nhiên hóa Quickselect** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Quickselect

Quickselect partition như Quicksort nhưng chỉ tiếp tục side chứa rank `k`.

Nếu pivot thường đủ cân bằng:

\[
T(n)=T(n/2)+O(n)=O(n)
\]

vì:

\[
n+n/2+n/4+\cdots=O(n)
\]

trường hợp xấu nhất vẫn `O(n²)` nếu mỗi pivot chỉ loại một phần tử.

> **Chuyển mạch:** Trong **Selection, k-th phần tử và Top-K**, **5. ngẫu nhiên hóa Quickselect** tiếp nhận điểm tựa từ **4. Quickselect** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Three-way partition cho các phần tử trùng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. ngẫu nhiên hóa Quickselect

ngẫu nhiên pivot làm đầu vào cố định khó ép thuật toán liên tục chọn cực trị.

```js
function quickselect(a, k) {
  let lo = 0, hi = a.length - 1;

  while (lo <= hi) {
    const p0 = lo + Math.floor(Math.random() * (hi - lo + 1));
    [a[p0], a[hi]] = [a[hi], a[p0]];
    const pivot = a[hi];

    let p = lo;
    for (let i = lo; i < hi; i++) {
      if (a[i] < pivot) {
        [a[i], a[p]] = [a[p], a[i]];
        p++;
      }
    }

    [a[p], a[hi]] = [a[hi], a[p]];

    if (p === k) return a[p];
    if (k < p) hi = p - 1;
    else lo = p + 1;
  }

  throw new RangeError("k out of range");
}
```

hàm này mutate đầu vào. Nếu API phải bất biến sau khi tạo, bản sao (copy / 복사) trước tạo thêm `O(n)` bộ nhớ/thời gian (time / 시간).

> **Chuyển mạch:** Ở chặng này của **Selection, k-th phần tử và Top-K**, **6. Three-way partition cho các phần tử trùng** tiếp nhận điểm tựa từ **5. ngẫu nhiên hóa Quickselect** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Median of Medians: xác định trường hợp xấu nhất O(n)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Three-way partition cho các phần tử trùng

Nếu nhiều các giá trị bằng pivot, two-way partition có thể recurse trên vùng equal lớn một cách vô ích.

Three-way partition cho interval `[lt, gt]` chứa tất cả các giá trị bằng chốt. Nếu đích `k` nằm trong interval này, return ngay.

có nhiều phần tử trùng dữ liệu (data / 데이터) là trường hợp (case / 사례) mà three-way partition không chỉ là tối ưu hóa (optimization / 최적화) nhỏ; nó có thể thay đổi shape recursion rõ rệt.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Selection, k-th phần tử và Top-K**, **7. Median of Medians: xác định trường hợp xấu nhất O(n)** tiếp nhận điểm tựa từ **6. Three-way partition cho các phần tử trùng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. thông tin cận dưới của selection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Median of Medians: xác định trường hợp xấu nhất O(n)

Median-of-medians chia dữ liệu thành các nhóm nhỏ, lấy trung vị của mỗi nhóm, đệ quy tìm trung vị của các trung vị rồi dùng giá trị đó làm chốt.

Phân tích (analysis / 분석) bảo đảm pivot loại một fraction đủ lớn ở cả hai phía:

\[
T(n) \le T(n/5)+T(7n/10)+O(n)=O(n)
\]

Ý nghĩa lý thuyết rất lớn: comparison-based selection không có cận dưới `Ω(n log n)` như full sorting.

Nhưng constant factor và cách triển khai độ phức tạp (complexity / 복잡도) khiến ngẫu nhiên hóa Quickselect thường thực dụng hơn trong general mã (code / 코드).

> **Chuyển mạch:** Trong **Selection, k-th phần tử và Top-K**, **8. thông tin cận dưới của selection** tiếp nhận điểm tựa từ **7. Median of Medians: xác định trường hợp xấu nhất O(n)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Median và robust thống kê** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. thông tin cận dưới của selection

Để tìm minimum, mọi phần tử trừ winner phải “thua” ít nhất một phép so sánh, nên cần ít nhất `n-1` các phép so sánh.

Selection của arbitrary rank cũng có tuyến tính (linear / 선형) cận dưới vì ít nhất phải inspect đủ đầu vào để không bỏ sót ứng viên.

Vì vậy kỳ vọng/trường hợp xấu nhất `O(n)` selection là asymptotically optimal.

> **Chuyển mạch:** Ở chặng này của **Selection, k-th phần tử và Top-K**, **9. Median và robust thống kê** tiếp nhận điểm tựa từ **8. thông tin cận dưới của selection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Top-K largest bằng đống nhỏ nhất kích thước (size / 크기) k** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Median và robust thống kê

Median ít nhạy với outlier hơn mean. chính xác median batch có thể dùng selection. Nếu dữ liệu (data / 데이터) quá lớn/xử lý luồng, chính xác rank đòi lưu nhiều trạng thái (state / 상태); lúc đó xấp xỉ quantile sketches như KLL/t-digest family phù hợp hơn.

thuật toán selection phải xét cả statistical ngữ nghĩa (semantics / 의미론) và mô hình bộ nhớ (memory model).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Selection, k-th phần tử và Top-K**, **10. Top-K largest bằng đống nhỏ nhất kích thước (size / 크기) k** tiếp nhận điểm tựa từ **9. Median và robust thống kê** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Vì sao đống nhỏ nhất cho k largest?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Top-K largest bằng đống nhỏ nhất kích thước (size / 크기) k

Duy trì đống nhỏ nhất chứa hiện tại `k` largest:

```text
heap size < k -> push
x <= heap.min -> bỏ
x > heap.min -> replace root
```

Độ phức tạp (complexity / 복잡도):

\[
O(n\log k)
\]

bộ nhớ:

\[
O(k)
\]

Nếu `k << n`, đây là lựa chọn rất mạnh cho xử lý luồng.

> **Chuyển mạch:** Trong **Selection, k-th phần tử và Top-K**, **11. Vì sao đống nhỏ nhất cho k largest?** tiếp nhận điểm tựa từ **10. Top-K largest bằng đống nhỏ nhất kích thước (size / 크기) k** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Quickselect cho batch Top-K** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Vì sao đống nhỏ nhất cho k largest?

Trong nhóm hiện tại Top-K, phần tử quan trọng nhất để quyết định ứng viên mới là **phần tử nhỏ nhất đang giữ**. Nếu ứng viên không thắng ranh giới này, nó không thể vào Top-K.

Do đó đống nhỏ nhất đặt đúng ranh giới phần tử ở nút gốc.

Tương tự k smallest dùng đống lớn nhất kích thước (size / 크기) k.

> **Chuyển mạch:** Ở chặng này của **Selection, k-th phần tử và Top-K**, **12. Quickselect cho batch Top-K** tiếp nhận điểm tựa từ **11. Vì sao đống nhỏ nhất cho k largest?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Heapify toàn bộ rồi pop k lần** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Quickselect cho batch Top-K

Quickselect partition đầu vào để `k` largest/smallest nằm cùng một phía kỳ vọng `O(n)`.

Nếu đầu ra không cần có thứ tự, ta có thể dừng ở đó. Nếu cần Top-K đã được sắp xếp:

\[
O(n)+O(k\log k)
\]

sort riêng selected region.

Vùng nhớ vùng nhớ động (heap / 힙) và Quickselect giải cùng hợp đồng đầu ra dưới khối lượng công việc khác:

```text
stream/bounded memory -> heap
batch/in-memory       -> quickselect
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Selection, k-th phần tử và Top-K**, **13. Heapify toàn bộ rồi pop k lần** tiếp nhận điểm tựa từ **12. Quickselect cho batch Top-K** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. sắp xếp một phần** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Heapify toàn bộ rồi pop k lần

xây dựng đống lớn nhất `O(n)`, pop k lần:

\[
O(n+k\log n)
\]

Giữ toàn dataset `O(n)` nhưng hợp nếu vùng nhớ động (heap / 힙) còn dùng sau đó hoặc k tương đối lớn.

Không có một chiến lược (strategy / 전략) Top-K duy nhất tốt cho mọi `k/n`.

> **Chuyển mạch:** Trong **Selection, k-th phần tử và Top-K**, **14. sắp xếp một phần** tiếp nhận điểm tựa từ **13. Heapify toàn bộ rồi pop k lần** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Multi-selection: cần nhiều ranks nhưng chưa cần full sort** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. sắp xếp một phần

Nếu cần prefix Top-K **đã sorted**, sắp xếp một phần có thể phù hợp hơn full sort.

Conceptual distinction:

```text
nth-element: chỉ cần đúng boundary rank
selection: một rank
unordered top-k: đúng membership
sorted top-k: membership + order trong top-k
full sort: order toàn bộ n
```

Mỗi đặc tả hợp đồng (contract / 계약) chứa lượng thông tin khác nhau.

> **Chuyển mạch:** Ở chặng này của **Selection, k-th phần tử và Top-K**, **15. Multi-selection: cần nhiều ranks nhưng chưa cần full sort** tiếp nhận điểm tựa từ **14. sắp xếp một phần** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. K-way Merge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Multi-selection: cần nhiều ranks nhưng chưa cần full sort

Nếu cần quartiles hoặc một tập ranks `k1,k2,...`, ta có thể reuse partition cây thay vì chạy Quickselect độc lập cho từng rank.

Một partition chia set ranks thành nhóm trái/phải; recurse chỉ nơi có các hạng cần tìm.

Đây là middle ground giữa one-rank selection và full sorting.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Selection, k-th phần tử và Top-K**, **16. K-way Merge** tiếp nhận điểm tựa từ **15. Multi-selection: cần nhiều ranks nhưng chưa cần full sort** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Top-K frequent các phần tử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. K-way Merge

Có `m` các danh sách đã sắp xếp và cần k smallest tổng thể. đống nhỏ nhất chứa hiện tại head mỗi danh sách (list / 목록):

1. pop toàn cục smallest;
2. đưa phần tử tiếp theo từ cùng danh sách vào vùng nhớ động (heap / 힙);
3. lặp k lần.

Độ phức tạp (complexity / 복잡도):

\[
O(k\log m)
\]

Không cần merge toàn bộ dữ liệu (data / 데이터).

mẫu này xuất hiện trong bên ngoài sort, cơ sở dữ liệu merge, tìm kiếm (search / 검색) shards và time-series streams.

> **Chuyển mạch:** Trong **Selection, k-th phần tử và Top-K**, **17. Top-K frequent các phần tử** tiếp nhận điểm tựa từ **16. K-way Merge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. xử lý luồng các phần tử xuất hiện dày đặc khác chính xác Top-K các giá trị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Top-K frequent các phần tử

Bài này gồm hai phases:

```text
frequency counting
selection theo frequency
```

Bảng băm tạo bảng tần suất trong thời gian kỳ vọng `O(n)`. Sau đó dùng vùng nhớ động (heap / 힙) kích thước k trên `u` giá trị phân biệt:

\[
O(n+u\log k)
\]

Nếu các tần suất bounded `0..n`, bucket-by-frequency có thể đạt near-linear.

“Top-K” không tự động đồng nghĩa vùng nhớ động (heap / 힙); khóa lĩnh vực (domain / 도메인) có thể mở alternative.

> **Chuyển mạch:** Ở chặng này của **Selection, k-th phần tử và Top-K**, **18. xử lý luồng các phần tử xuất hiện dày đặc khác chính xác Top-K các giá trị** tiếp nhận điểm tựa từ **17. Top-K frequent các phần tử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Quantile trong các hệ thống phân tán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. xử lý luồng các phần tử xuất hiện dày đặc khác chính xác Top-K các giá trị

Nếu muốn items có tần suất cao nhất trong stream khổng lồ, chính xác map có thể cần bộ nhớ theo số distinct các khóa.

bản phác đếm tối thiểu + ứng viên tracking, Space-Saving hoặc Misra–Gries giảm bộ nhớ đổi lấy bảo đảm khác.

Phân biệt:

```text
top-k by raw score per item
vs
top-k frequent over stream
```

chúng là bài toán (problem / 문제) khác nhau dù tên giống.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Selection, k-th phần tử và Top-K**, **19. Quantile trong các hệ thống phân tán** tiếp nhận điểm tựa từ **18. xử lý luồng các phần tử xuất hiện dày đặc khác chính xác Top-K các giá trị** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. phân tán (distributed / 분산) Top-K: cục bộ reduction rồi toàn cục merge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Quantile trong các hệ thống phân tán

chính xác percentile toàn phân tán (distributed / 분산) dataset có thể cần shuffle/sort lớn. xấp xỉ sketches cho phép mỗi shard giữ dữ liệu tóm lược rồi merge.

Nếu chính xác, một chiến lược (strategy / 전략) có thể dùng phân tán (distributed / 분산) selection/partition rounds, nhưng mạng communication trở thành chi phí chính.

Ở quy mô (scale / 규모) lớn, độ phức tạp truyền thông có thể quan trọng hơn CPU `O(n)` vs `O(n log n)`.

> **Chuyển mạch:** Trong **Selection, k-th phần tử và Top-K**, **20. phân tán (distributed / 분산) Top-K: cục bộ reduction rồi toàn cục merge** tiếp nhận điểm tựa từ **19. Quantile trong các hệ thống phân tán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Threshold các thuật toán cho sorted truy cập (access / 접근)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. phân tán (distributed / 분산) Top-K: cục bộ reduction rồi toàn cục merge

Nếu score mỗi item độc lập và mỗi shard chứa partition disjoint, cục bộ Top-K của mỗi shard là ứng viên superset đủ cho toàn cục Top-K: item không nằm cục bộ Top-K không thể vượt k items cùng shard đã cao hơn nó.

Coordinator chỉ cần merge tối đa `shards * k` các ứng viên.

Đây là một reduction rất mạnh:

```text
huge distributed dataset
-> local top-k
-> much smaller candidate union
-> global top-k
```

Nếu scoring phụ thuộc toàn cục normalization/tương tác (interaction / 상호작용), tính chất này có thể không còn đúng.

> **Chuyển mạch:** Ở chặng này của **Selection, k-th phần tử và Top-K**, **21. Threshold các thuật toán cho sorted truy cập (access / 접근)** tiếp nhận điểm tựa từ **20. phân tán (distributed / 분산) Top-K: cục bộ reduction rồi toàn cục merge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. lựa chọn trên bộ nhớ ngoài** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Threshold các thuật toán cho sorted truy cập (access / 접근)

Trong information-retrieval/cơ sở dữ liệu settings, nếu nhiều attribute lists sorted theo partial scores, threshold các thuật toán có thể dừng sớm khi hiện tại Top-K score đã vượt cận trên (upper bound) của unseen các ứng viên.

Đây là một generalization của ranh giới lập luận (reasoning / 추론): maintain cận dưới của winners và cận trên của unknowns.

Không cần full materialization nếu có stopping certificate.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Selection, k-th phần tử và Top-K**, **22. lựa chọn trên bộ nhớ ngoài** tiếp nhận điểm tựa từ **21. Threshold các thuật toán cho sorted truy cập (access / 접근)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Selection trên linked dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. lựa chọn trên bộ nhớ ngoài

Nếu dữ liệu không vừa RAM, Quickselect tại chỗ trên toàn bộ tập dữ liệu không còn là cách triển khai trực tiếp. Ta có thể partition dữ liệu (data / 데이터) thành files/các ngăn băm theo pivot, count sizes, rồi chỉ recurse ngăn băm chứa rank.

Mục tiêu chuyển từ phép so sánh count sang giảm các lượt I/O và byte read/ghi (write / 쓰기).

Một thuật toán `O(n)` CPU nhưng nhiều ngẫu nhiên I/O có thể thua bên ngoài chiến lược (strategy / 전략) sequential các lần quét.

> **Chuyển mạch:** Trong **Selection, k-th phần tử và Top-K**, **22. lựa chọn trên bộ nhớ ngoài** nêu điều cần giải thích; **23. Selection trên linked dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **24. Selection các cây và Tournament các cây** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Selection trên linked dữ liệu (data / 데이터)

Quickselect cần efficient partition traversal nhưng không nhất thiết truy cập ngẫu nhiên. Tuy nhiên pointer-heavy danh sách (list / 목록) có bộ nhớ đệm chi phí và partition relinking phức tạp.

Nếu dữ liệu (data / 데이터) là linked cấu trúc (structure / 구조) nhưng có thể materialize mảng rẻ, chuyển cách biểu diễn (representation / 표현) đôi khi thực tế hơn cố implement chuyên biệt danh sách (list / 목록) selection.

> **Chuyển mạch:** Ở chặng này của **Selection, k-th phần tử và Top-K**, **23. Selection trên linked dữ liệu (data / 데이터)** nêu điều cần giải thích; **24. Selection các cây và Tournament các cây** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **25. trực tuyến Median bằng hai heaps** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Selection các cây và Tournament các cây

Tournament cây (tree / 트리) lưu kết quả của các cặp so sánh. Tìm phần tử nhỏ nhất cần `n-1` phép so sánh. Nếu muốn phần tử nhỏ thứ hai, chỉ cần xét những phần tử đã trực tiếp thua phần tử nhỏ nhất trên đường đi, khoảng `log n` ứng viên trong cây giải đấu cân bằng.

Đây là insight thông tin reuse: phép so sánh lịch sử chứa thêm cấu trúc (structure / 구조) cho thứ tự (order / 순서) thống kê tiếp theo.

Tournament/loser các cây cũng dùng trong k-way bên ngoài merge.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Selection, k-th phần tử và Top-K**, **25. trực tuyến Median bằng hai heaps** tiếp nhận điểm tựa từ **24. Selection các cây và Tournament các cây** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Top-K với các cập nhật/deletes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. trực tuyến Median bằng hai heaps

Giữ:

```text
max-heap lower half
min-heap upper half
```

Bất biến (invariant / 불변식):

```text
size difference <= 1
max(lower) <= min(upper)
```

Insert `O(log n)`, median `O(1)`.

Đây không phải bài chọn một lần kinh điển mà là thống kê thứ tự động cho luồng chỉ có thao tác chèn.

Nếu cần xóa phần tử tùy ý, mô hình hai vùng nhớ động (heap / 힙) cần xóa lười hoặc lập chỉ mục phức tạp hơn; một cây cân bằng có thống kê thứ tự có thể phù hợp hơn.

> **Chuyển mạch:** Trong **Selection, k-th phần tử và Top-K**, **26. Top-K với các cập nhật/deletes** tiếp nhận điểm tựa từ **25. trực tuyến Median bằng hai heaps** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. quy tắc phân xử khi bằng nhau và determinism** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Top-K với các cập nhật/deletes

Vùng nhớ vùng nhớ động (heap / 힙) kích thước k trong trường hợp tĩnh giả định mỗi phần tử chỉ được xét một lần. Nếu điểm số thay đổi sau khi chèn, vùng nhớ động (heap / 힙) không tự sắp xếp lại chỉ vì trường của đối tượng bị thay đổi.

Java `PriorityQueue` không hỗ trợ arbitrary độ ưu tiên cập nhật. Options:

```text
push new version + skip stale
indexed heap
balanced tree keyed by score
periodic rebuild
```

hợp đồng đầu ra động làm cấu trúc dữ liệu choice thay đổi.

> **Chuyển mạch:** Ở chặng này của **Selection, k-th phần tử và Top-K**, **27. quy tắc phân xử khi bằng nhau và determinism** tiếp nhận điểm tựa từ **26. Top-K với các cập nhật/deletes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Floating-point scores** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. quy tắc phân xử khi bằng nhau và determinism

Nếu nhiều items cùng score, cần secondary thứ tự (order / 순서):

```text
score desc
then timestamp asc
then id asc
```

Bộ so sánh phải mã hóa đầy đủ quy tắc phân xử. Nếu không, vùng nhớ động (heap / 힙) hoặc phép phân hoạch có thể trả thứ tự tùy ý giữa các phần tử hòa nhau, khiến kiểm thử không ổn định và kết quả phân tán không xác định.

Top-K theo **tập phần tử thuộc kết quả** và Top-K theo **danh sách có thứ tự ổn định** là hai hợp đồng khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Selection, k-th phần tử và Top-K**, **28. Floating-point scores** tiếp nhận điểm tựa từ **27. quy tắc phân xử khi bằng nhau và determinism** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Java/C/JavaScript comparator caveats** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Floating-point scores

Ranking với `NaN`, `-0`, infinities hoặc floating rounding cần ngữ nghĩa rõ. Comparator không nên giả định thứ tự toàn phần nếu lĩnh vực (domain / 도메인) có NaN hành vi đặc biệt.

Nếu score được tính từ nhiều floating các thành phần, near-tie các kết quả có thể nhạy với evaluation thứ tự (order / 순서). Trong hệ thống thực tế, ranking thường cần xác định normalization/tie-break khóa.

> **Chuyển mạch:** Trong **Selection, k-th phần tử và Top-K**, **29. Java/C/JavaScript comparator caveats** tiếp nhận điểm tựa từ **28. Floating-point scores** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. sự thay đổi dữ liệu đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Java/C/JavaScript comparator caveats

Java/C comparator dùng subtraction có thể tràn số:

```java
return a.score - b.score;
```

nên dùng `Integer.compare`/`Long.compare`.

Bộ so sánh cho `Number` trong JavaScript phải trả giá trị âm, 0 hoặc dương. Với `BigInt`, không nên trả trực tiếp kết quả số học BigInt nếu API mong dấu dạng Number; hãy dùng các nhánh so sánh quan hệ.

Comparator tính đúng đắn là prerequisite của vùng nhớ động (heap / 힙)/sort/ordered selection.

> **Chuyển mạch:** Ở chặng này của **Selection, k-th phần tử và Top-K**, **29. Java/C/JavaScript comparator caveats** nêu điều cần giải thích; **30. sự thay đổi dữ liệu đặc tả hợp đồng (contract / 계약)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **31. kiểm thử Quickselect** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. sự thay đổi dữ liệu đặc tả hợp đồng (contract / 계약)

Quickselect thường mutate mảng. vùng nhớ động (heap / 힙) xử lý luồng không cần reorder đầu vào. Full sort có thể mutate tùy API.

Nếu bên gọi cần giữ nguyên thứ tự ban đầu, việc sao chép tốn `O(n)` thời gian và bộ nhớ. Đây là một đánh đổi kỹ thuật thực sự, không chỉ là vấn đề phong cách mã.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Selection, k-th phần tử và Top-K**, **30. sự thay đổi dữ liệu đặc tả hợp đồng (contract / 계약)** nêu điều cần giải thích; **31. kiểm thử Quickselect** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **32. tính chất của k-th statistic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. kiểm thử Quickselect

tham chiếu oracle:

```text
copy input
sort copy
expected = copy[k]
```

ngẫu nhiên small các mảng cho differential kiểm thử rất hiệu quả.

Cases:

```text
all equal
many duplicates
sorted
reverse sorted
single element
k = 0
k = n-1
negative/large values
```

Nếu ngẫu nhiên hóa, log seed để reproduce thất bại (failure / 실패).

> **Chuyển mạch:** Trong **Selection, k-th phần tử và Top-K**, **32. tính chất của k-th statistic** tiếp nhận điểm tựa từ **31. kiểm thử Quickselect** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. kiểm thử Top-K** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. tính chất của k-th statistic

Nếu answer `x` cho zero-based rank `k`, phải có đủ số các phần tử `< x` và `<= x` phù hợp phần tử trùng ngữ nghĩa để rank `k` nằm trong equal khối (block / 블록) của `x`.

tính chất này giúp verify kết quả mà không cần chính xác pivot lịch sử.

> **Chuyển mạch:** Ở chặng này của **Selection, k-th phần tử và Top-K**, **33. kiểm thử Top-K** tiếp nhận điểm tựa từ **32. tính chất của k-th statistic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. đối kháng đầu vào và pivot chiến lược (strategy / 전략)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. kiểm thử Top-K

So sánh đa tập đầu ra với k phần tử đầu của kết quả tham chiếu đã sắp xếp hoàn toàn. Nếu hợp đồng đầu ra yêu cầu có thứ tự, so sánh dãy; nếu không yêu cầu thứ tự, so sánh bảng tần suất hoặc đa tập.

quy tắc phân xử khi bằng nhau phải được kiểm thử (test / 테스트) riêng nếu API xác định.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Selection, k-th phần tử và Top-K**, **34. đối kháng đầu vào và pivot chiến lược (strategy / 전략)** tiếp nhận điểm tựa từ **33. kiểm thử Top-K** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. chiến lược (strategy / 전략) ma trận (matrix / 행렬) theo khối lượng công việc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. đối kháng đầu vào và pivot chiến lược (strategy / 전략)

Quickselect xác định pivot đầu/cuối dễ bị sorted/đối kháng đầu vào phá `O(n²)`.

ngẫu nhiên pivot, median-of-three hoặc introspective fallback giúp giảm rủi ro (risk / 위험). công khai (public / 공개) APIs phải cân nhắc đối kháng callers nếu độ trễ (latency / 지연 시간)/bảo mật (security / 보안) quan trọng.

> **Chuyển mạch:** Trong **Selection, k-th phần tử và Top-K**, **35. chiến lược (strategy / 전략) ma trận (matrix / 행렬) theo khối lượng công việc** tiếp nhận điểm tựa từ **34. đối kháng đầu vào và pivot chiến lược (strategy / 전략)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. chiến lược (strategy / 전략) ma trận (matrix / 행렬) theo khối lượng công việc

Một rank, batch, sự thay đổi dữ liệu allowed:

```text
Quickselect
```

Một rank, xác định trường hợp xấu nhất bound bắt buộc:

```text
Median of Medians / deterministic selection
```

Top-K xử lý luồng, k nhỏ:

```text
bounded heap
```

Top-K batch unsorted:

```text
Quickselect
```

Top-K sorted:

```text
selection + sort k
heap
partial sort
```

Nhiều rank các truy vấn:

```text
sort once
order-stat tree
multi-selection
```

xử lý luồng percentile xấp xỉ:

```text
quantile sketch
```

> **Chuyển mạch:** Ở chặng này của **Selection, k-th phần tử và Top-K**, **Mô hình tư duy** gom các mảnh từ **35. chiến lược (strategy / 전략) ma trận (matrix / 행렬) theo khối lượng công việc** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Các thuật toán chọn khai thác việc đầu ra chỉ yêu cầu **một ranh giới trong thứ tự**, không cần toàn bộ thứ tự. Quickselect loại bỏ từng vùng; vùng nhớ động (heap / 힙) duy trì ranh giới; Tournament cây (tree / 트리) tái sử dụng lịch sử so sánh; Top-K phân tán giảm tập ứng viên trước khi gộp.

Trước khi chọn thuật toán, hãy viết chính xác hợp đồng đầu ra: một rank, unordered Top-K, sorted Top-K, động rank, tần suất các phần tử xuất hiện dày đặc hay xấp xỉ percentile. Chỉ một từ “Top-K” chưa đủ xác định bài toán.

Xem thêm: [Heap](../02_trees/03_heaps.md), [Sorting](./01_sorting.md), [Probabilistic Structures](../05_specialized/06_probabilistic_data_structures.md), [Complexity](../00_foundations/02_complexity_analysis.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
