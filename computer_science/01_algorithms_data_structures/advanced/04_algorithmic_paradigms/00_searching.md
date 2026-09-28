# Searching

> **Mạch đọc:** Đọc **Searching** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **tìm kiếm tuyến tính và cận dưới trực giác** sang **tìm kiếm nhị phân cần monotonic thông tin**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

**Tìm kiếm (Searching / 탐색)**

Searching là quá trình thu hẹp **ứng viên không gian (space / 공간) / 후보 공간** cho tới khi xác định được đích, ranh giới hoặc chứng minh answer không tồn tại. Điểm phân biệt giữa các tìm kiếm (search / 검색) các thuật toán không phải cú pháp (syntax / 문법) vòng lặp (loop / 루프) mà là **thông tin nào cho phép loại một vùng các ứng viên**.

Nếu không có cấu trúc (structure / 구조) hỗ trợ, tuyến tính (linear / 선형) quét có thể là optimal practical choice. Nếu dữ liệu sorted, phép so sánh cho phép loại nửa không gian (space / 공간). Nếu có chỉ mục băm, định danh (identity / 식별자) tra cứu gần-direct. Nếu không gian trạng thái là đồ thị, BFS/DFS/Dijkstra tổ chức frontier khác nhau. Nếu answer không gian (space / 공간) có monotonic predicate, tìm kiếm nhị phân có thể hoạt động ngay cả khi không tồn tại một mảng cụ thể.

Mô hình tư duy quan trọng nhất là:

> tìm kiếm (search / 검색) nhanh khi mỗi observation loại được một vùng các ứng viên lớn mà không bỏ mất answer.

## tìm kiếm tuyến tính và cận dưới trực giác

Nếu mảng chưa được sắp xếp, không có băm hoặc chỉ mục và cần tìm một giá trị bất kỳ, trường hợp xấu nhất có thể phải xem mọi phần tử.

```c
int linear_search(const int *a, int n, int target) {
    for (int i = 0; i < n; ++i) {
        if (a[i] == target) return i;
    }
    return -1;
}
```

trường hợp xấu nhất `O(n)`.

Không nên coi tìm kiếm tuyến tính là “thuật toán kém”. Nếu dataset nhỏ, chỉ tìm kiếm (search / 검색) một lần hoặc tiền xử lý/lập chỉ mục đắt hơn truy vấn, tuyến tính (linear / 선형) quét có thể là lựa chọn tốt nhất.

Ví dụ với 20 các phần tử, xây dựng bảng băm (hash table / 해시 테이블) rồi tra cứu một lần thường không có giá trị thực tế.

## tìm kiếm nhị phân cần monotonic thông tin

tìm kiếm nhị phân hoạt động vì thứ tự đã sắp xếp tạo một predicate monotonic.

Ví dụ tìm đích trong sorted ascending mảng:

```text
values < target | maybe target | values > target
```

Midpoint phép so sánh cho phép chứng minh một nửa các ứng viên không thể chứa đích.

```java
int binarySearch(int[] a, int target) {
    int lo = 0, hi = a.length - 1;

    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;

        if (a[mid] == target) return mid;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }

    return -1;
}
```

`lo + (hi-lo)/2` tránh tràn số mà `(lo+hi)/2` có thể gây trong độ rộng cố định integer lĩnh vực (domain / 도메인).

## bất biến vòng lặp quan trọng hơn template

Một tìm kiếm nhị phân đúng nên có bất biến (invariant / 불변식) rõ ràng.

Ví dụ lower-bound dùng khoảng nửa mở `[lo, hi)`:

```java
int lowerBound(int[] a, int target) {
    int lo = 0, hi = a.length;

    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;

        if (a[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }

    return lo;
}
```

bất biến có thể viết:

```text
mọi index < lo có value < target
mọi index >= hi có value >= target
answer boundary nằm trong [lo, hi]
```

Khi `lo == hi`, ứng viên interval co lại thành ranh giới answer.

Nếu hiểu bất biến này, ta không cần học thuộc hàng chục mẫu tìm lần xuất hiện đầu tiên/cuối cùng khác nhau.

## cận dưới và cận trên (upper bound)

**cận dưới** là vị trí đầu tiên có giá trị `>= target`.

**cận trên** là vị trí đầu tiên có giá trị `> target`.

Với mảng đã sắp xếp, số lần đích xuất hiện là:

```text
upperBound(target) - lowerBound(target)
```

Nếu đích không tồn tại, cận dưới vẫn có ý nghĩa: đó là insertion position để giữ thứ tự (order / 순서).

Đây là lý do APIs kiểu `lower_bound` mạnh hơn hàm chỉ trả `found/not found`.

## giá trị đúng đầu tiên / giá trị sai cuối cùng sự trừu tượng (abstraction)

Rất nhiều binary-search problems có thể chuẩn hóa về chuỗi (sequence / 시퀀스):

```text
F F F F T T T T
```

Ta tìm:

```text
first T
hoặc last F
```

Trước khi mã (code / 코드), viết predicate orientation ra giấy:

```text
P(x) = ?
P có monotonic không?
Ta cần first true hay last true?
```

Đây là cách giảm mạnh off-by-one bugs.

## tìm kiếm nhị phân on answer

tìm kiếm nhị phân không cần mảng đã sắp xếp. Nó cần **ordered không gian lời giải + monotonic feasibility predicate**.

Ví dụ tìm ship sức chứa (capacity / 용량) nhỏ nhất để vận chuyển packages trong `D` ngày.

```text
P(C) = có thể ship trong <= D ngày với capacity C không?
```

Nếu sức chứa `C` khả thi thì mọi sức chứa lớn hơn cũng khả thi:

```text
F F F T T T
```

Ta tìm giá trị đúng đầu tiên.

Độ phức tạp (complexity / 복잡도):

```text
O(cost(P) * log(answer range))
```

Điểm quan trọng là feasibility check phải đủ nhanh và monotonic thật sự.

## Cách chứng minh predicate monotonic

Đừng chỉ nhìn bài toán (problem / 문제) và “cảm giác tìm kiếm nhị phân được”. Hãy chứng minh:

```text
P(x) true -> P(y) true với mọi y >= x
```

hoặc orientation ngược lại.

Ví dụ trong bài tìm sức chứa tối thiểu, tăng sức chứa không thể làm lịch khó hơn nên vị từ có tính đơn điệu.

Nhưng nếu parameter ảnh hưởng mục tiêu (objective / 목표) theo non-monotonic way, tìm kiếm nhị phân sẽ sai dù mã (code / 코드) template hoàn hảo.

## Tìm kiếm trên miền đáp án nguyên

Giả sử answer thuộc `[L, R]` inclusive và tìm minimum feasible.

Một robust half-open formulation là tìm kiếm (search / 검색) `[L, R+1)` với upper giá trị canh gác (sentinel) chắc chắn feasible, hoặc dùng inclusive bounds cẩn thận.

Nếu `R+1` có tràn số rủi ro (risk / 위험), cần cách biểu diễn (representation / 표현) khác.

Trong mã dùng trong hệ thống thực tế, ranh giới lĩnh vực (domain / 도메인) quan trọng không kém thuật toán idea.

## tìm kiếm nhị phân trên real numbers

Nếu answer continuous, chính xác equality hiếm có ý nghĩa vì floating-point.

Ta có hai stopping strategies:

```text
fixed iterations
hoặc hi - lo <= epsilon
```

Fixed iterations thường predictable hơn. Với `double`, khoảng 60–100 iterations thường vượt quá precision cần thiết cho nhiều tasks.

Nhưng tính đúng đắn phải định nghĩa lỗi (error / 오류) tolerance theo lĩnh vực (domain / 도메인). `1e-9` không tự động phù hợp với mọi quy mô (scale / 규모).

## Floating-point monotonic caveat

Vị từ toán học có thể đơn điệu, nhưng cách triển khai bằng số dấu phẩy động gần ngưỡng có thể xuất hiện sai số làm tròn.

Nếu predicate dựa vào accumulated floating-point sums, hãy xem xét numerical tính ổn định thay vì giả định chính xác monotonic chuỗi (sequence / 시퀀스) ở machine tầng.

## Exponential tìm kiếm (search / 검색) khi chưa biết cận trên

Nếu answer position không có known finite cận trên, ta có thể grow bound theo các lũy thừa của hai:

```text
1, 2, 4, 8, 16, ...
```

cho tới khi predicate true hoặc vượt đích, sau đó tìm kiếm nhị phân interval vừa tìm được.

chi phí logarithmic theo answer magnitude.

mẫu này hữu ích cho:

```text
unbounded sorted stream/API
unknown array length abstraction
first failure position trong infinite-like domain
```

## Ternary tìm kiếm (search / 검색) không phải tìm kiếm nhị phân phiên bản “chia ba nhanh hơn”

Ternary tìm kiếm (search / 검색) thường dùng trên **unimodal hàm** — tăng rồi giảm hoặc giảm rồi tăng — để tìm cực trị.

Nó không thay tìm kiếm nhị phân trên sorted/monotonic predicate. Chia ba không tự động giảm độ phức tạp (complexity / 복잡도) tốt hơn về constant/lô-gic (logic / 논리); tính chất của hàm quyết định thuật toán.

## Interpolation tìm kiếm (search / 검색)

Nếu các giá trị số đã sắp xếp và phân bố gần đồng đều, Interpolation tìm kiếm (search / 검색) ước lượng vị trí từ chính giá trị thay vì luôn lấy điểm giữa.

Hiệu năng kỳ vọng có thể tốt trên phân phối lý tưởng, nhưng trường hợp xấu nhất vẫn có thể là `O(n)`. Điều này cho thấy chiến lược tìm kiếm có thể khai thác cả đặc điểm phân phối chứ không chỉ thứ tự.

Trong general-purpose mã (code / 코드), tìm kiếm nhị phân predictable hơn.

## Băm (hash / 해시) tra cứu

bảng băm dùng hàm băm để map khóa vào ngăn băm/chỉ mục (index / 인덱스) cấu trúc (structure / 구조).

kỳ vọng tra cứu thường `O(1)` nhưng phụ thuộc collision handling và băm (hash / 해시) phân phối.

Tìm kiếm bằng băm không duy trì thứ tự, nên các truy vấn như:

```text
floor/ceiling
range
predecessor/successor
```

không tự nhiên.

BST hoặc `TreeMap` chậm hơn về mặt tiệm cận đối với tra cứu bằng nhau, nhưng đổi lại cung cấp ngữ nghĩa tìm kiếm có thứ tự (ordered search semantics).

## cây tìm kiếm (search / 검색)

BST tìm kiếm (search / 검색) loại cây con dựa trên bất biến thứ tự. độ phức tạp (complexity / 복잡도) `O(h)` chứ không tự động `O(log n)`.

Balanced BST giữ `h = O(log n)`.

B/B+cây (tree / 트리) mở rộng cùng idea cho bên ngoài bộ nhớ bằng fan-out lớn.

Searching vì thế nối trực tiếp với cách biểu diễn.

## Trie tìm kiếm (search / 검색)

Trie không so sánh toàn khóa theo thứ tự toàn phần. Nó consume khóa từng symbol/prefix.

tra cứu length `L` thường khoảng `O(L)` dưới nút con tra cứu các giả định.

Trie phù hợp khi nội bộ cấu trúc (structure / 구조) của khóa — prefix — có ngữ nghĩa quan trọng.

## đồ thị tìm kiếm (search / 검색)

BFS, DFS, Dijkstra, A* đều là searching trên đồ thị trạng thái.

Khác nhau ở frontier chính sách:

```text
DFS       -> stack
BFS       -> FIFO queue
Dijkstra  -> min priority by distance
A*        -> min priority by g + heuristic
```

Một mô hình tư duy thống nhất rất hữu ích là: thuật toán tìm kiếm = không gian trạng thái + thứ tự của biên tìm kiếm + chính sách đã thăm/giá trị tốt nhất đã biết.

## trạng thái-space tìm kiếm (search / 검색) và phần tử trùng detection

Trong các bài đố hoặc bài toán quay lui (backtracking), cùng một trạng thái lô-gic (logic / 논리) (state) có thể được đi tới qua nhiều lịch sử khác nhau.

Nếu tương lai possibilities từ trạng thái giống nhau, ta nên canonicalize trạng thái và tránh expand lại.

Đây chính là quan hệ (relation / 관계) giữa tìm kiếm (search / 검색), đồ thị đã thăm và DP memoization.

## nhánh và cận

Tìm kiếm tối ưu có thể giữ lời giải tốt nhất hiện biết cùng cận dưới/cận trên cho các trạng thái chưa hoàn chỉnh. Nếu một nhánh không thể vượt lời giải hiện tại, có thể cắt tỉa nhánh đó.

Đây không phải tìm kiếm nhị phân; nó là search-tree pruning dựa trên mục tiêu (objective / 목표) bound.

Phổ biến mẫu:

```text
if optimistic_bound(state) >= best:
    prune
```

cho minimization.

## A* tìm kiếm (search / 검색)

A* dùng:

\[
f(n)=g(n)+h(n)
\]

trong đó `g` là chi phí đã đi, `h` là heuristic estimate remaining chi phí.

Nếu heuristic chấp nhận được/consistent theo các giả định thích hợp, A* vẫn optimal nhưng explore ít các trạng thái hơn Dijkstra trong nhiều spatial problems.

Heuristic là extra thông tin giúp loại/deprioritize các ứng viên — cùng bản chất với mọi tìm kiếm (search / 검색) tối ưu hóa (optimization / 최적화).

## Chỉ mục tìm kiếm trong cơ sở dữ liệu

cơ sở dữ liệu bảng (table / 테이블) quét là tìm kiếm tuyến tính ở lưu trữ quy mô (scale / 규모).

Chỉ mục B+cây (tree / 트리), chỉ mục băm và chỉ mục đảo đều là các cấu trúc tiền xử lý nhằm giảm số hàng hoặc tài liệu ứng viên cần xét.

Xây dựng và cập nhật chỉ mục đều có chi phí, vì vậy tốc độ tìm kiếm luôn được đánh đổi bằng dung lượng lưu trữ và chi phí bảo trì.

Mô hình tư duy này giúp nối interview DSA với các hệ thống thực tế.

## Inverted chỉ mục (index / 인덱스)

công cụ tìm kiếm văn bản (text / 텍스트) retrieval không quét mọi tài liệu cho mỗi truy vấn. Nó xây ánh xạ:

```text
term -> sorted postings list of document IDs
```

Truy vấn AND lấy giao của các danh sách vị trí xuất hiện, thường bằng hai con trỏ (two pointers) hoặc thông tin nhảy để bỏ qua nhanh.

Đây là một chỉ mục tìm kiếm được thiết kế theo tải công việc: truy vấn dựa trên việc một thuật ngữ có xuất hiện hay không.

## thông tin lý thuyết (theory / 이론) intuition

Nếu cần phân biệt `n` sorted positions bằng nhị phân (binary / 이진) các phép so sánh, mỗi phép so sánh có khoảng hai outcomes và cung cấp cỡ một bit thông tin.

Để distinguish `n` possibilities cần khoảng:

\[
\log_2 n
\]

bits.

Đây là intuition cho logarithmic phép so sánh lower quy mô (scale / 규모) của tìm kiếm nhị phân.

Không phải chứng minh cận dưới đầy đủ cho mọi mô hình, nhưng giúp hiểu vì sao `O(log n)` là tự nhiên.

## tiền xử lý vs truy vấn thời gian (time / 시간)

Một dataset tĩnh với triệu các truy vấn đáng để xây dựng chỉ mục (index / 인덱스)/preprocess.

Một dataset chỉ truy vấn một lần có thể không đáng.

Ví dụ:

```text
sort once O(n log n) + q binary searches O(q log n)
```

so với:

```text
q linear scans O(qn)
```

Break-even phụ thuộc `q`, n và constants.

Searching thiết kế (design / 설계) vì thế cần nhìn **vòng đời (lifecycle / 생명주기) khối lượng công việc**, không chỉ một truy vấn cô lập.

## Phổ biến binary-search bugs

### Midpoint cập nhật không shrink interval

Nếu branch dùng `lo = mid` trong interval nơi `mid == lo`, vòng lặp (loop / 루프) có thể infinite. Phải prove khoảng giảm nghiêm ngặt.

### Wrong first/last orientation

Mã đang tìm giá trị đúng đầu tiên nhưng vị từ thực tế lại có dạng đúng-rồi-sai.

### Closed vs half-open trộn lẫn

`hi = n-1` nhưng vòng lặp (loop / 루프)/các cập nhật viết như `[lo,hi)` tạo off-by-one.

### Predicate không monotonic

Đây là bug conceptual, không phải cú pháp (syntax / 문법).

### tràn số

`(lo+hi)/2`, `R+1` hoặc feasibility arithmetic có thể tràn số.

## kiểm thử tìm kiếm nhị phân bằng các tính chất

Thay vì chỉ vài examples, kiểm thử (test / 테스트):

```text
empty array
one element
target < min
target > max
all values equal
duplicates nhiều
target tại first/last index
```

Với cận dưới, tính chất:

```text
for all i < ans: a[i] < target
for all i >= ans: a[i] >= target
```

Property-based kiểm thử (test / 테스트) này mạnh hơn checking one kỳ vọng chỉ mục (index / 인덱스).

## Tìm kiếm (search / 검색) và tính cục bộ bộ nhớ đệm

tìm kiếm nhị phân trên mảng có `O(log n)` các phép so sánh nhưng mẫu truy cập nhảy. cây tìm kiếm (search / 검색) cũng pointer-chasing.

Với các mảng, tuyến tính (linear / 선형) quét có thể cạnh tranh nhờ contiguous bộ nhớ, vectorization và khả năng dự đoán nhánh.

mô hình tiệm cận không bỏ qua hardware effects.

## tìm kiếm nhảy nhanh trong merge/intersection

Khi lấy giao hai danh sách đã sắp xếp có kích thước rất chênh lệch, thay vì tiến từng phần tử trên danh sách lớn, có thể nhảy theo cấp số nhân rồi dùng tìm kiếm nhị phân để giảm công việc.

Tìm kiếm (search / 검색) techniques thường compose với nhau; không phải mỗi bài toán (problem / 문제) chỉ dùng một named thuật toán.

## Tìm kiếm (search / 검색) as elimination

Một cách gỡ lỗi thiết kế (design / 설계):

```text
Candidate set ban đầu là gì?
Mỗi observation loại candidates nào?
Tại sao loại chúng là safe?
Candidate set có strictly shrink không?
Stopping condition chứng minh điều gì?
```

Nếu không trả lời được, tìm kiếm (search / 검색) lô-gic (logic / 논리) có thể đang dựa vào intuition chưa được chứng minh.

## Mô hình tư duy

> Searching là khoa học của **ứng viên elimination**. dữ liệu (data / 데이터) thứ tự (order / 순서), chỉ mục băm, prefix cấu trúc (structure / 구조), đồ thị khoảng cách, heuristic hay monotonic predicate đều là thông tin dùng để loại hoặc deprioritize các ứng viên. thuật toán tốt không chỉ “tìm nhanh”; nó giải thích rõ vì sao các ứng viên bị bỏ chắc chắn không thể là answer.

Khi gặp một tìm kiếm (search / 검색) bài toán (problem / 문제), hãy hỏi:

```text
Candidate space là gì?
Có order/monotonicity không?
Có thể preprocess/index không?
Search một lần hay rất nhiều lần?
State graph có duplicate states không?
Frontier cần FIFO/LIFO/priority/heuristic?
Need exact answer hay approximate acceptable?
```

Xem thêm: [BST](../02_trees/01_binary_search_trees.md), [BFS/DFS](../03_graphs/01_graph_traversal_bfs_dfs.md), [Shortest Paths](../03_graphs/02_shortest_paths.md), [Trie](../02_trees/04_tries.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 sorting](./01_sorting.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
