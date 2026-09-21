# Tính đúng đắn và bất biến của thuật toán
**Algorithm Correctness & Invariants / 알고리즘 정확성과 불변식**

Một thuật toán nhanh nhưng sai không có giá trị. Kiểm thử chỉ chứng minh chương trình hoạt động đúng trên những trường hợp đã chạy; nó không tự chứng minh rằng thuật toán đúng với mọi đầu vào hợp lệ. Vì vậy, một năng lực trung tâm của DSA là **lập luận về tính đúng đắn (correctness reasoning)**: biết mình được phép giả định điều gì, điều gì phải luôn đúng trong quá trình chạy, vì sao thuật toán tiến về điểm dừng và vì sao trạng thái cuối bắt buộc thỏa yêu cầu.

Chứng minh không nhất thiết phải là một văn bản toán học dài. Trong thực hành, chỉ cần xác định đúng specification, invariant và progress measure thường đã đủ biến một đoạn code khó tin thành một chuỗi lập luận có thể kiểm tra.

## Trước khi chứng minh phải có specification

Một thuật toán chỉ “đúng” so với một **đặc tả (specification / 명세)** cụ thể.

Specification thường phải nói rõ:

```text
miền đầu vào hợp lệ
điều kiện trước
ngữ nghĩa đầu ra
điều kiện sau
tie-breaking nếu có
hành vi với input không hợp lệ
```

Ví dụ “binary search” có thể có nhiều specification khác nhau:

```text
trả một vị trí bất kỳ chứa target
trả vị trí đầu tiên chứa target
trả lower_bound
trả insertion point nếu không có target
```

Tên thuật toán giống nhau nhưng điều kiện sau khác nhau, nên bất biến và code cũng khác nhau.

## Điều kiện trước và điều kiện sau

**Điều kiện trước (precondition / 사전 조건)** là điều phải đúng trước khi thao tác bắt đầu. **Điều kiện sau (postcondition / 사후 조건)** là điều thao tác cam kết khi kết thúc bình thường.

Ví dụ `merge(left, right)` thường có precondition: hai dãy đầu vào đã được sắp xếp theo cùng comparator. Postcondition cần mạnh hơn câu “đầu ra đã sorted”; nó còn phải bảo toàn đúng đa tập phần tử của hai đầu vào.

```text
sorted(output)
multiset(output) = multiset(left) ∪ multiset(right)
```

Nếu chỉ chứng minh thứ tự mà không chứng minh bảo toàn phần tử, một implementation làm mất hoặc nhân đôi dữ liệu vẫn có thể vượt qua nửa đầu specification.

## Hoare triple: cách viết hợp đồng ngắn gọn

Một cách ký hiệu hữu ích là:

\[
\{P\}\ C\ \{Q\}
\]

Trong đó `P` là precondition, `C` là đoạn chương trình và `Q` là postcondition.

Ví dụ:

```text
{ a đã sorted }
binarySearch(a, x)
{ trả vị trí hợp lệ của x hoặc xác nhận x không tồn tại }
```

Ta không cần formal verification hoàn chỉnh để hưởng lợi từ cách nghĩ này. Nó buộc ta tách rõ “được giả định gì” và “phải bảo đảm gì”.

## Partial correctness và total correctness

**Tính đúng đắn từng phần (partial correctness)** nói rằng: nếu thuật toán kết thúc thì kết quả đúng.

**Tính đúng đắn toàn phần (total correctness)** thêm yêu cầu thuật toán thực sự kết thúc trên mọi input hợp lệ.

Một vòng lặp có thể giữ invariant hoàn hảo nhưng không thu nhỏ không gian tìm kiếm, dẫn tới chạy vô hạn. Vì vậy chứng minh loop thường cần hai phần:

```text
safety: invariant luôn đúng
progress: một đại lượng tiến dần về điểm dừng
```

Đại lượng dùng để chứng minh tiến triển thường gọi là **variant** hoặc **ranking function**.

## Bất biến vòng lặp

**Bất biến vòng lặp (loop invariant / 루프 불변식)** là một mệnh đề đúng tại một vị trí xác định của mọi vòng lặp.

Một mẫu chứng minh chuẩn có ba bước:

```text
Initialization: invariant đúng trước vòng đầu tiên.
Maintenance: nếu invariant đúng trước vòng hiện tại, thân vòng giữ nó đúng cho vòng sau.
Termination: invariant + điều kiện dừng suy ra postcondition.
```

### Ví dụ: binary search

Với đoạn ứng viên `[lo, hi]`, invariant có thể là:

> Nếu target tồn tại thì mọi vị trí còn có khả năng chứa target đều nằm trong `[lo, hi]`.

```c
int binary_search(const int *a, int n, int target) {
    int lo = 0, hi = n - 1;

    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;

        if (a[mid] == target) return mid;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }

    return -1;
}
```

Nếu `a[mid] < target`, tính sorted cho phép loại toàn bộ `[lo, mid]`. Không chỉ một phần tử bị loại; cả một vùng được chứng minh không còn khả năng chứa đáp án.

Progress measure là độ dài đoạn ứng viên. Mỗi vòng không trả kết quả đều làm đoạn ngắn hơn, nên thuật toán kết thúc.

## Invariant phải đủ mạnh nhưng không quá khó duy trì

Một câu kiểu “mảng đang được xử lý đúng” không giúp chứng minh điều gì. Invariant tốt phải đủ mạnh để suy ra postcondition, nhưng đủ đơn giản để chứng minh maintenance.

Insertion Sort có invariant mạnh:

> Trước vòng `i`, đoạn `a[0..i)` đã sorted và chứa đúng đa tập phần tử ban đầu của đoạn đó.

Hai phần đều quan trọng:

```text
order invariant
conservation invariant
```

Nếu thiếu conservation, ta chưa chứng minh thuật toán không làm mất hoặc nhân đôi phần tử.

## Bất biến bảo toàn

Nhiều thuật toán mutate dữ liệu, nên cần theo dõi cái gì phải được bảo toàn.

Sorting bảo toàn đa tập phần tử. Heap giữ toàn bộ phần tử ngoài đúng phần tử vừa chèn/xóa. DSU bảo toàn partition của tập phần tử. Graph traversal phải bảo đảm mọi trạng thái được đánh dấu thực sự reachable từ nguồn theo quy tắc transition.

Một validator tốt hiếm khi chỉ kiểm tra một property.

## Representation invariant của cấu trúc dữ liệu

Cấu trúc dữ liệu thường có **bất biến biểu diễn (representation invariant)** mạnh hơn postcondition của từng thao tác.

Ví dụ Binary Heap:

```text
shape là complete binary tree
size phù hợp vùng hợp lệ của mảng
heap order đúng trên mọi cạnh cha-con
```

Red-Black Tree có thêm các bất biến về màu và black-height. Hash Table phải giữ quan hệ giữa trạng thái slot, số phần tử và quy tắc probing. Doubly Linked List phải giữ `next/prev` đối xứng.

Mỗi thao tác public có thể được xem như:

```text
representation invariant trước thao tác
        ↓
thao tác
        ↓
representation invariant sau thao tác
```

Nếu invariant được phục hồi trước khi API trả về, các thao tác sau có thể tiếp tục dựa trên nó.

## Bất biến cục bộ và bất biến toàn cục

Một số invariant có thể kiểm tra cục bộ. Heap order chỉ cần so mỗi cha với con. Nhưng BST không thể chỉ kiểm tra `left < parent < right` ở mỗi cạnh; một khóa sâu trong cây con trái vẫn phải nhỏ hơn toàn bộ cận trên từ tổ tiên.

Do đó validator BST nên truyền khoảng hợp lệ xuống:

```text
node.key ∈ (lowerBound, upperBound)
```

Đây là bài học tổng quát: **local consistency không luôn suy ra global correctness**.

## Ghost state: thông tin dùng để chứng minh nhưng không cần lưu trong runtime

Khi reasoning, ta có thể dùng thông tin phụ không tồn tại trong implementation. Đây thường được gọi là **ghost state** trong formal methods.

Ví dụ khi chứng minh sorting, ta có thể tưởng tượng một bản sao multiset của input ban đầu để chứng minh conservation, dù code thực tế không lưu bản sao đó.

Trong BFS, ta có thể reasoning bằng “khoảng cách thật ngắn nhất” `δ(s,v)` dù implementation chỉ lưu `dist[v]`.

Ghost state giúp tách “thông tin cần để chứng minh” khỏi “thông tin cần để chạy hiệu quả”.

## Quy nạp và đệ quy

Thuật toán đệ quy thường được chứng minh bằng **quy nạp (induction / 수학적 귀납법)**.

Merge Sort:

```text
base: n <= 1 đã sorted
hypothesis: mọi lời gọi trên kích thước nhỏ hơn trả đúng
step: hai nửa được sort đúng + merge đúng => toàn bộ đúng
```

Với cây, **quy nạp cấu trúc (structural induction)** còn tự nhiên hơn. Nếu hàm trên nút chỉ phụ thuộc các cây con, ta giả sử các cây con trả đúng rồi chứng minh phép kết hợp ở nút cha đúng.

## Quy nạp mạnh

Dynamic Programming thường cần **quy nạp mạnh (strong induction)** vì trạng thái hiện tại có thể phụ thuộc nhiều trạng thái nhỏ hơn, không chỉ đúng một trạng thái `n-1`.

Bottom-up DP về bản chất thực thi đúng thứ tự chứng minh: mọi prerequisite được tính trước khi transition hiện tại dùng tới chúng.

## Hợp đồng của hàm đệ quy

Khi debug recursion, thay vì mô phỏng toàn bộ call tree, hãy viết contract cho một lời gọi.

Ví dụ:

```text
solve(state) trả giá trị tối ưu đạt được từ state trở đi,
và khi trả về thì global mutable state đã được phục hồi như trước lời gọi.
```

Trong backtracking, phần “phục hồi state” là cực kỳ quan trọng. Nếu `choose -> recurse -> unchoose` không đối xứng, lời gọi anh em có thể nhìn thấy trạng thái rác.

## Chứng minh termination cho đệ quy

Có base case chưa đủ. Đối số đệ quy phải tiến gần base case theo một well-founded order.

Ví dụ:

```text
n giảm dần
số phần tử chưa xử lý giảm dần
chiều sâu còn lại giảm dần
kích thước cây con nhỏ hơn cây cha
```

Nếu recursion có thể quay lại trạng thái cũ mà không có visited/memoization hoặc progress metric, termination chưa được chứng minh.

## Greedy và exchange argument

Greedy khóa lựa chọn cục bộ và không quay lại, vì vậy phải chứng minh lựa chọn đó an toàn.

Mẫu **exchange argument**:

```text
1. Lấy một lời giải tối ưu O.
2. Nếu O đã chứa lựa chọn greedy g, xong bước này.
3. Nếu chưa, thay một phần của O bằng g.
4. Chứng minh lời giải mới vẫn hợp lệ và không tệ hơn O.
5. Suy ra tồn tại lời giải tối ưu bắt đầu bằng g.
6. Lặp lại cho phần còn lại.
```

Trong interval scheduling, chọn interval kết thúc sớm nhất là an toàn vì thay interval đầu của một optimum bằng interval kết thúc sớm hơn không làm mất thêm không gian thời gian ở phía sau.

“Có vẻ hợp lý” không phải chứng minh greedy.

## Cut property và cycle property

Minimum Spanning Tree có các mẫu chứng minh riêng nhưng rất tái sử dụng.

**Cut property** nói rằng dưới điều kiện phù hợp, cạnh nhẹ nhất cắt qua một cut là cạnh an toàn để thêm vào một MST.

**Cycle property** cho góc nhìn đối ngược: trong một cycle, một cạnh nặng nhất thích hợp có thể bị loại khỏi một MST nào đó.

Kruskal và Prim có implementation khác nhau nhưng đều dựa vào cấu trúc chứng minh này.

## Proof by contradiction

Chứng minh phản chứng hữu ích khi thuật toán “finalize” một quyết định.

Dijkstra với cạnh không âm là ví dụ. Khi đỉnh `u` có tentative distance nhỏ nhất được lấy ra, giả sử vẫn có một đường ngắn hơn tới `u`. Trên đường đó phải tồn tại điểm đầu tiên đi từ vùng đã finalize sang vùng chưa finalize. Tính không âm của trọng số tạo một candidate không thể lớn hơn `dist[u]`, mâu thuẫn với việc `u` là candidate nhỏ nhất.

Lập luận này đồng thời chỉ ra vì sao cạnh âm phá điều kiện cốt lõi của Dijkstra.

## Chứng minh bằng cực trị

Một kỹ thuật khác là chọn “phản ví dụ nhỏ nhất”, “đỉnh đầu tiên vi phạm” hoặc “thời điểm đầu tiên invariant bị phá”.

Giả sử một property đúng ban đầu nhưng cuối cùng sai. Xét bước đầu tiên nó trở thành sai. Ngay trước bước đó property còn đúng, nên ta chỉ cần phân tích thao tác vừa thực hiện.

Đây là cách rất mạnh để chứng minh invariant của cấu trúc động.

## Monotonicity và binary search on answer

Nếu predicate `P(x)` có dạng:

```text
false false false ... true true true
```

ta có thể tìm điểm chuyển bằng binary search.

Nhưng trước khi viết code phải chứng minh **tính đơn điệu (monotonicity)**. Nếu `P(x)` có thể true rồi false trở lại, binary search on answer không có cơ sở đúng đắn.

Một lỗi phổ biến là thấy “đáp án là một số” rồi áp binary search mà chưa chứng minh predicate có cấu trúc đơn điệu.

## BFS: invariant theo tầng

BFS có một invariant quan trọng:

> Khi một đỉnh được lấy ra theo BFS chuẩn trên đồ thị không trọng số, `dist[v]` là độ dài đường đi ngắn nhất từ nguồn tới `v`.

Lý do queue xử lý đỉnh theo lớp khoảng cách không giảm. Mọi cạnh thêm đúng 1 bước. Một đường ngắn hơn tới `v` nếu tồn tại phải đi qua một lớp nhỏ hơn và đã được khám phá trước.

Điều này giải thích vì sao đánh dấu khi enqueue thường quan trọng: nó ngăn cùng một state được đưa vào queue nhiều lần và giữ rõ nghĩa “đã phát hiện khoảng cách ngắn nhất”.

## DFS: invariant của call stack

Trong DFS đệ quy, call stack biểu diễn đường đi hiện tại trong cây DFS. Với đồ thị có hướng dùng ba màu:

```text
WHITE = chưa thăm
GRAY  = đang nằm trên recursion stack
BLACK = đã hoàn tất
```

Một cạnh tới `GRAY` cho thấy có chu trình có hướng vì ta quay lại một tổ tiên đang hoạt động. Nếu chỉ dùng `visited` Boolean, thông tin “đang hoạt động” bị mất và không đủ cho chứng minh kiểu này.

## DSU: invariant của đại diện

Disjoint Set Union giữ một forest các parent pointer. Invariant ngữ nghĩa không phải “cây đẹp”, mà là:

```text
find(x) trả cùng representative khi và chỉ khi x thuộc cùng component theo các union đã áp dụng
```

Path compression thay đổi hình dạng cây mạnh nhưng không đổi partition logic. Đây là ví dụ một optimization thay representation nhưng giữ semantics.

Nếu có `size[root]` hoặc `rank[root]`, metadata chỉ có ý nghĩa ở root và phải được cập nhật theo đúng union rule.

## Heap: repair local, preserve global

Khi chèn vào Binary Heap, shape invariant được giữ bằng cách thêm ở cuối mảng. Chỉ heap-order trên đường từ node mới tới root có thể bị phá.

Sift-up sửa đúng vùng có khả năng sai. Các cạnh ngoài đường đó không thay đổi nên invariant vẫn đúng ở đó.

Đây là mẫu chứng minh cực kỳ phổ biến:

```text
một mutation chỉ có thể phá invariant trong một vùng nhỏ
=> sửa vùng đó
=> phần còn lại không cần kiểm tra lại
```

AVL/Red-Black rotation, Segment Tree update và nhiều cấu trúc tăng cường đều dựa trên tư duy này.

## Segment Tree: invariant theo đoạn

Mỗi node Segment Tree đại diện một đoạn và lưu aggregate của chính đoạn đó.

Invariant:

```text
tree[node] = combine(value của mọi phần tử trong interval(node))
```

Khi cập nhật một điểm, chỉ các node trên đường từ leaf đó tới root có interval chứa điểm cập nhật. Do đó chỉ cần recompute đường này.

Tính đúng đắn đến từ việc các node không chứa vị trí cập nhật giữ nguyên giá trị đúng, còn các node có chứa nó được tính lại từ hai child đã đúng.

## Shortest path relaxation

Relaxation thường có dạng:

\[
dist[v] \leftarrow \min(dist[v], dist[u] + w(u,v))
\]

Một invariant nền tảng là `dist[v]` luôn là chi phí của một đường đi thực sự đã biết tới `v` hoặc `∞`. Vì vậy nó là một **upper bound** trên shortest-path distance thật.

Các thuật toán shortest path khác nhau chủ yếu khác ở quy tắc chọn thứ tự relaxation và điều kiện cho phép ta kết luận bound đã trở thành chính xác.

## Invariant giữa nhiều cấu trúc

LRU Cache dùng Hash Map + Doubly Linked List. Mỗi cấu trúc có thể tự hợp lệ nhưng hệ thống vẫn sai nếu map và list không nhất quán.

Cần invariant liên cấu trúc:

```text
map và list chứa cùng tập key
mỗi map entry trỏ đúng node trong list
size nhất quán
thứ tự list đúng recency semantics
```

Trong code production, đây thường là nơi bug khó xuất hiện nhất vì validator riêng lẻ của từng container vẫn pass.

## Atomicity của thao tác phức hợp

Một operation có thể gồm nhiều bước nội bộ. Nếu failure xảy ra giữa chừng, cấu trúc cần hoặc:

```text
rollback về trạng thái cũ
hoặc
đạt một trạng thái mới vẫn hợp lệ theo contract
```

Trong C, resize Hash Table nên hoàn thành allocation/rehash bảng mới trước khi thay pointer chính. Đây là reasoning gần với transaction: không để public state ở trạng thái nửa cũ nửa mới.

## Concurrency và linearizability

Trong môi trường nhiều luồng, invariant có thể bị phá giữa hai dòng code dù từng dòng riêng lẻ đúng.

Ví dụ:

```text
if key absent:
    insert key
```

Hai thread có thể cùng thấy “absent” rồi cùng insert.

Một mô hình correctness quan trọng là **tính tuyến tính hóa (linearizability / 선형화 가능성)**: mỗi operation concurrent phải có thể được xem như xảy ra tại một thời điểm nguyên tử nào đó giữa lúc gọi và lúc trả về.

Lock-free structures còn cần memory ordering và memory reclamation reasoning. “Dùng atomic pointer” tự nó chưa chứng minh thuật toán đúng.

## Arithmetic correctness

Một proof toán học có thể giả sử số nguyên vô hạn, nhưng code chạy với kiểu hữu hạn.

Ví dụ:

```java
long candidate = dist[u] + weight;
```

Nếu `dist[u]` là sentinel gần `Long.MAX_VALUE`, phép cộng có thể overflow. Trong C, signed overflow có thể dẫn tới undefined behavior. Trong JavaScript, `Number` mất tính chính xác số nguyên sau `2^53 - 1`.

Do đó proof của implementation phải bao gồm miền giá trị của kiểu số.

## Floating-point correctness

Số thực máy có sai số làm tròn. So sánh equality, predicate đơn điệu hoặc comparator dựa trên epsilon tùy tiện có thể không còn bắc cầu.

Nếu comparator vi phạm transitivity, sort hoặc balanced tree có thể có hành vi không đúng contract.

Với geometry và numerical algorithms, representation số là một phần của specification, không phải chi tiết implementation.

## Validator cho cấu trúc dữ liệu

Cấu trúc phức tạp nên có `validate()` trong test/debug.

```text
BST        -> kiểm tra cận toàn cây, không chỉ cha-con
Red-Black  -> màu, root, red-red, black-height
Heap       -> shape và heap-order
Hash Table -> trạng thái slot, count, lookup mọi entry
DSU        -> parent hợp lệ, metadata ở root
LinkedList -> size và prev/next đối xứng
```

Validator không thay proof nhưng giúp phát hiện implementation phá proof ở đâu.

## Differential testing

Một implementation chậm nhưng rõ có thể làm **oracle** cho input nhỏ.

```text
range query     -> so với quét tuyến tính
shortest path   -> so với Floyd–Warshall trên graph nhỏ
Top-K           -> so với sort toàn bộ
custom BST      -> so với TreeMap/TreeSet
custom heap     -> so chuỗi pop với mảng đã sort
```

Differential testing rất hiệu quả vì nó kiểm tra hàng nghìn chuỗi thao tác mà ta khó viết tay.

## Property-based testing

Thay vì chỉ kiểm tra output cụ thể, có thể kiểm tra property:

```text
sort(output) phải có thứ tự và cùng multiset input
push rồi pop trên stack phải khôi phục state phù hợp
union(a,b) => find(a) == find(b)
heap poll liên tục phải cho dãy không giảm
serialize rồi deserialize phải bảo toàn cấu trúc
```

Đây là cách biến specification thành test tự động.

## Adversarial tests

Random test không thay thế các case biên được thiết kế có chủ đích:

```text
rỗng
một phần tử
tất cả bằng nhau
đã sorted / reverse sorted
nhiều duplicate
cây cực lệch
đồ thị rời rạc
self-loop / parallel edges
giá trị sát giới hạn kiểu số
input gây nhiều hash collision
```

Một proof tốt cho biết case nào nằm trong domain hợp lệ và case nào phải bị từ chối.

## Proof sketch trong code review

Với thuật toán khó, một proof sketch ngắn thường có giá trị hơn comment từng dòng.

Ví dụ Monotonic Queue cho sliding-window maximum:

```text
Invariant 1: deque chỉ chứa index còn nằm trong window.
Invariant 2: value tại các index giảm dần từ front tới back.
Khi thêm i, mọi phần tử ở back có value <= a[i] bị loại vì i mới hơn
và không nhỏ hơn, nên chúng không thể trở thành maximum trong future window.
Front vì vậy luôn là maximum hiện tại.
```

Đây là loại comment giải thích “vì sao đúng”, giúp reviewer đánh giá thay đổi thuật toán.

## Một template chứng minh có thể tái sử dụng

Khi cần chứng minh thuật toán, có thể dùng khung:

```text
1. Specification là gì?
2. Preconditions là gì?
3. State nào đang được duy trì?
4. Invariant là gì?
5. Invariant đúng lúc khởi tạo không?
6. Mỗi transition có giữ invariant không?
7. Progress measure là gì?
8. Vì sao thuật toán phải dừng?
9. Khi dừng, invariant + stop condition suy ra postcondition thế nào?
10. Numeric/runtime assumptions nào proof đang dựa vào?
```

Với greedy, thêm exchange/cut argument. Với recursion, thêm induction. Với concurrent structure, thêm linearization point và memory-order reasoning.

## Những hiểu lầm phổ biến

“Pass sample tests là đã đúng” — sai; sample chỉ là bằng chứng hữu hạn.

“Invariant đúng ở cuối là đủ” — sai; phải đúng sau initialization và được duy trì qua mọi transition.

“Có base case thì recursion sẽ dừng” — sai nếu đối số không tiến gần base case.

“Greedy hợp lý theo trực giác” — không thay exchange argument hoặc structural proof.

“Cấu trúc vẫn trả vài query đúng nên metadata chắc đúng” — sai; invariant có thể đã hỏng và chỉ chưa chạm case lộ lỗi.

“Đã chứng minh thuật toán nên code chắc đúng” — sai; overflow, aliasing, indexing và runtime semantics có thể làm implementation khác mô hình toán học.

## Mô hình tư duy

> Tính đúng đắn là một chuỗi lập luận: **specification** nói phải đạt gì; **precondition** nói được giả định gì; **invariant** nói điều gì luôn được bảo vệ; **progress argument** nói vì sao thuật toán sẽ dừng; trạng thái khi dừng cộng với invariant phải suy ra **postcondition**.

Khi gặp một thuật toán khó, đừng đọc code từng dòng trước. Hãy hỏi: **tập ứng viên hiện tại là gì, invariant nào đang được giữ, mỗi transition loại bỏ hay bảo toàn thông tin nào, phần nào có thể bị phá bởi mutation, và vì sao khi dừng không còn trường hợp nào chưa được xử lý?**

Xem tiếp: [Problem Modeling](./00_dsa_as_problem_modeling.md), [Complexity Analysis](./02_complexity_analysis.md), [Mathematical Toolkit](./04_mathematical_toolkit_for_dsa.md), [Greedy Algorithms](../04_algorithmic_paradigms/04_greedy_algorithms.md), [Dynamic Programming](../04_algorithmic_paradigms/05_dynamic_programming.md) và [Problem Solving Workflow](../90_connections/02_problem_solving_workflow.md).