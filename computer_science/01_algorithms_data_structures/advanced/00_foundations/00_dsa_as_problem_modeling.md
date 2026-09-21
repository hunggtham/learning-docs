# DSA như một bài toán mô hình hóa
**Cấu trúc dữ liệu và thuật toán (Data Structures & Algorithms / 자료구조와 알고리즘)**

DSA thường được học bằng tên cấu trúc và tên thuật toán: mảng, danh sách liên kết, bảng băm, cây, đồ thị, BFS, DFS, Dijkstra, quy hoạch động. Cách học này giúp nhận diện mẫu, nhưng chưa đủ để giải bài toán mới. Năng lực cốt lõi hơn là **mô hình hóa (problem modeling)**: biến một vấn đề thực tế thành một mô hình trạng thái có đầu vào, đầu ra, thao tác, bất biến và mô hình chi phí đủ rõ để lựa chọn cách biểu diễn phù hợp.

Một chương trình có thể được nhìn như hai thành phần lớn: **trạng thái (state)** và **phép biến đổi trạng thái (state transition)**. Cấu trúc dữ liệu quyết định trạng thái được biểu diễn và lưu sẵn như thế nào; thuật toán quyết định chuỗi biến đổi dẫn từ trạng thái ban đầu tới kết quả. Hiệu năng và tính đúng đắn không đến từ một thuật toán “mạnh” đứng riêng lẻ, mà từ mức độ phù hợp giữa mô hình, cách biểu diễn, các thao tác và tải công việc thực tế.

## Bắt đầu từ câu hỏi cần trả lời

Giả sử hệ thống có một triệu tài khoản. Nếu thao tác chính là “tìm tài khoản theo id”, quét tuyến tính là mô hình kém phù hợp. Bảng băm có thể đổi thêm bộ nhớ và chi phí băm để có tra cứu kỳ vọng gần `O(1)`. Nếu cần thêm `floor`, `ceiling`, truy vấn theo khoảng hoặc duyệt theo thứ tự, cây tìm kiếm cân bằng có thể phù hợp hơn vì thứ tự được duy trì như một bất biến.

Do đó, câu hỏi đầu tiên không phải “dùng HashMap hay TreeMap?”, mà là:

```text
Hệ thống phải trả lời những truy vấn nào?
Thao tác nào chiếm đa số?
Dữ liệu có thường xuyên thay đổi không?
Cần kết quả chính xác hay có thể xấp xỉ?
Cần worst-case guarantee hay expected guarantee là đủ?
Độ trễ, thông lượng hay bộ nhớ quan trọng hơn?
Dữ liệu có nằm hoàn toàn trong RAM không?
Có nhiều truy vấn hơn cập nhật, hay ngược lại?
```

Đây là **mô hình tải công việc (workload model)**. Cấu trúc dữ liệu chỉ có ý nghĩa khi đặt trong một workload cụ thể.

## Từ yêu cầu nghiệp vụ sang các thao tác nguyên thủy

Một yêu cầu nghiệp vụ nên được phân rã thành các thao tác cụ thể. Ví dụ hệ thống chat có thể cần:

```text
append(message)
getRecent(k)
findById(id)
delete(id)
searchByTime(from, to)
```

Nếu 95% lưu lượng là `append` và `getRecent`, việc tối ưu cực mạnh cho `delete(id)` nhưng làm hai thao tác chính chậm đi có thể là quyết định sai.

Có thể hình dung chi phí trung bình có trọng số:

\[
E[C] = \sum_i p_i C_i
\]

trong đó `p_i` là tần suất tương đối của thao tác `i`, còn `C_i` là chi phí của nó. Không phải lúc nào cũng cần tính chính xác công thức này; giá trị của nó nằm ở việc buộc ta suy nghĩ theo tỷ lệ sử dụng thay vì theo tên cấu trúc dữ liệu.

## Kiểu dữ liệu trừu tượng trước cách triển khai

**Kiểu dữ liệu trừu tượng (Abstract Data Type – ADT / 추상 자료형)** mô tả ngữ nghĩa và hợp đồng thao tác, chưa quyết định biểu diễn vật lý.

Stack cam kết LIFO với `push`, `pop`, `peek`. Nó có thể được cài bằng mảng động, danh sách liên kết hoặc vùng nhớ chuyên dụng. Queue cam kết FIFO nhưng có thể được cài bằng ring buffer, linked list hoặc deque.

Tách ADT khỏi implementation giúp phân biệt hai câu hỏi:

```text
Cấu trúc phải làm gì?
Cấu trúc sẽ làm điều đó bằng cách nào?
```

Hai implementation có thể cùng ngữ nghĩa nhưng rất khác về locality, cấp phát, bộ nhớ, mất hiệu lực của iterator và chi phí theo từng thao tác.

## Cách biểu diễn chính là quyết định “thông tin nào được lưu sẵn”

Mỗi cấu trúc dữ liệu trả một chi phí nào đó để giữ sẵn một loại thông tin, nhờ đó một số truy vấn trở nên rẻ hơn.

Mảng đã sắp xếp giữ toàn bộ thứ tự nên tìm kiếm nhị phân nhanh, nhưng chèn giữa đắt. Hash Table không giữ thứ tự nhưng giữ ánh xạ từ hash tới vị trí tìm kiếm. Heap chỉ giữ đủ quan hệ thứ tự để phần tử cực trị ở gốc. Segment Tree lưu sẵn kết quả tổng hợp của nhiều khoảng chuẩn. Trie lưu cấu trúc tiền tố để tránh so sánh lại phần tiền tố chung.

Có thể xem cấu trúc dữ liệu như một dạng **thông tin được vật chất hóa trước (materialized information)**. Ta bỏ công cập nhật và bộ nhớ để tránh tính lại từ đầu trong tương lai.

## Chuỗi suy luận từ representation tới complexity

Một cách suy nghĩ ổn định là:

```text
representation
    ↓
invariant
    ↓
operation
    ↓
complexity
    ↓
trade-off và failure mode
```

Ví dụ Binary Heap dùng mảng và hình dạng cây complete. Hình dạng đó bảo đảm chiều cao `O(log n)` và cho phép tính parent/child bằng chỉ số. Heap-order invariant làm `peek-min` là `O(1)` và `insert/extract` là `O(log n)`, nhưng không cung cấp tìm kiếm khóa tùy ý nhanh.

Nếu yêu cầu Heap phải trả lời mọi truy vấn mà Balanced BST hỗ trợ, vấn đề không nằm ở code Heap “chưa đủ tốt”; vấn đề là ta đang dùng sai abstraction.

## Mô hình trạng thái: thông tin nào thực sự quyết định tương lai?

Một trạng thái đúng phải chứa đủ thông tin để mọi quyết định tương lai được xác định.

Giả sử đi trên lưới có cửa khóa. Hai lần đứng ở cùng `(row, col)` nhưng có bộ chìa khóa khác nhau không phải cùng một trạng thái, vì các hành động tiếp theo khác nhau. Trạng thái hợp lý có thể là:

```text
(row, col, keyMask)
```

Ngược lại, nếu hai lịch sử khác nhau dẫn tới cùng tập hành động hợp lệ và cùng chi phí tương lai, ta có thể gộp chúng vào một trạng thái.

Đây là một trong những tư tưởng sâu nhất của quy hoạch động:

> Trạng thái không phải là “lịch sử đầy đủ”; trạng thái là lượng thông tin tối thiểu từ lịch sử còn ảnh hưởng tới tương lai.

## Quan hệ tương đương giữa các lịch sử

Có thể formalize trực giác trên bằng cách coi hai lịch sử `h1` và `h2` là tương đương nếu:

```text
mọi hành động tương lai hợp lệ từ h1 cũng hợp lệ từ h2
và
chi phí/kết quả tối ưu từ h1 và h2 là tương đương theo mục tiêu bài toán
```

Khi đó ta không cần lưu toàn bộ lịch sử; chỉ cần lưu lớp tương đương mà lịch sử thuộc về.

Ví dụ trong bài đường đi có tối đa `K` lần phá tường, trạng thái cần số lần phá đã dùng. Trong bài mà chỉ tổng parity của số bước quan trọng, toàn bộ số bước có thể được nén về một bit chẵn/lẻ.

**Nén trạng thái (state compression)** không phải mẹo bitmask đơn thuần; nó là kết quả của việc nhận ra phần nào của lịch sử không còn ảnh hưởng tới tương lai.

## Đồ thị thực thể và đồ thị trạng thái

Không phải mọi đỉnh của đồ thị đều là một “vật thể thật”.

Trong mạng xã hội, đỉnh có thể là người dùng. Trong dependency graph, đỉnh là module. Nhưng trong puzzle hoặc routing có ràng buộc, đỉnh có thể là trạng thái tổng hợp.

Ví dụ chuyến bay giới hạn tối đa `K` chặng:

```text
(airport, flightsUsed)
```

Nếu giá vé phụ thuộc thời điểm:

```text
(airport, timeSlot)
```

Nếu còn phụ thuộc loại vé:

```text
(airport, timeSlot, ticketType)
```

Đây là **đồ thị không gian trạng thái (state-space graph)**. Một thuật toán shortest path hoàn hảo trên mô hình trạng thái sai vẫn trả kết quả sai cho bài toán thật.

## Product graph: ghép nhiều chiều trạng thái

Nhiều bài có thể được xem là tích của hai hoặc nhiều không gian trạng thái.

Ví dụ robot di chuyển trên grid và có hướng nhìn:

```text
(position) × (direction)
```

Một ô `(r,c)` không phải một trạng thái duy nhất; `(r,c,north)` và `(r,c,east)` có thể có tập thao tác khác nhau.

Tư duy **đồ thị tích (product graph)** giúp giải thích vì sao việc “thêm một dimension vào state” thường làm số trạng thái tăng theo tích kích thước của các chiều.

Nếu grid có `R*C` ô và `M` trạng thái phụ, tổng trạng thái có thể là `O(R*C*M)`. Điều này phải được tính trước khi chọn BFS/DP.

## Ràng buộc là dữ liệu đầu vào cho việc chọn thuật toán

Cùng một câu hỏi nhưng constraints khác nhau có thể cần thuật toán hoàn toàn khác.

Shortest path:

```text
không trọng số            -> BFS
trọng số chỉ 0/1          -> 0–1 BFS
trọng số không âm         -> Dijkstra
DAG                       -> relaxation theo topological order
có trọng số âm            -> cần mô hình/thuật toán khác
negative cycle đạt tới    -> có thể không tồn tại minimum hữu hạn
```

Subset problem với `n = 20` có thể duyệt `2^n`; với `n ≈ 40–50` có thể nghĩ tới meet-in-the-middle; với `n = 200000` thì exponential search thường không còn khả thi và phải khai thác thêm cấu trúc.

Constraints không phải phần phụ cuối đề bài; chúng là một phần của định nghĩa bài toán.

## Trước tiên phải xác định objective

Một mô hình có thể đúng về trạng thái nhưng vẫn sai vì objective không rõ.

Các objective thường gặp:

```text
minimize cost
maximize value
count number of solutions
check existence
return lexicographically smallest solution
return any valid solution
minimize worst-case latency
minimize memory under latency bound
```

Hai bài có cùng trạng thái và transition nhưng objective khác nhau có thể cần cấu trúc dữ liệu hoặc thuật toán khác nhau.

Ví dụ “có đường đi hay không” có thể dùng BFS/DFS đơn giản; “đường đi ngắn nhất” cần thêm metric; “đường đi ngắn nhất rồi nhỏ nhất từ điển” còn cần tie-breaking và thứ tự duyệt phù hợp.

## Tách feasibility khỏi optimization

Một kỹ thuật mô hình hóa quan trọng là tách:

```text
Có tồn tại lời giải thỏa điều kiện không?
Giữa các lời giải hợp lệ, lời giải nào tối ưu?
```

Nhiều bài “tối ưu hóa trên đáp án” dùng binary search vì ta có một predicate đơn điệu:

```text
feasible(x) = có thể đạt mục tiêu với ngưỡng x hay không?
```

Khi `feasible(x)` chuyển từ false sang true theo một chiều, bài tối ưu có thể biến thành chuỗi bài kiểm tra khả thi.

Điều này cho thấy thuật toán tìm kiếm không nhất thiết tìm trực tiếp đáp án; đôi khi ta mô hình hóa bài tối ưu thành một quyết định Boolean dễ hơn.

## Bài toán tĩnh, động, trực tuyến và ngoại tuyến

Bốn thuộc tính này thay đổi hoàn toàn không gian lựa chọn.

**Tĩnh (static)**: dữ liệu gần như không đổi. Có thể tiền xử lý mạnh, ví dụ Prefix Sum, Sparse Table, Suffix Array.

**Động (dynamic)**: cập nhật xảy ra thường xuyên. Cần Fenwick Tree, Segment Tree, balanced tree hoặc cấu trúc động khác tùy bài.

**Trực tuyến (online)**: phải trả lời khi dữ liệu tới, không biết tương lai.

**Ngoại tuyến (offline)**: có toàn bộ truy vấn trước và có thể đổi thứ tự xử lý. Khi đó có thể dùng Mo’s Algorithm, sort queries, DSU offline hoặc nhiều kỹ thuật sweep.

Cùng một bộ truy vấn, quyền biết trước tương lai có thể làm bài toán dễ hơn đáng kể.

## Exact, approximate và probabilistic

Không phải mọi hệ thống đều cần kết quả chính xác tuyệt đối.

Bloom Filter chấp nhận false positive để giảm bộ nhớ. HyperLogLog ước lượng số phần tử phân biệt với sai số thống kê. Count-Min Sketch ước lượng tần suất với sai số một phía.

Vấn đề thiết kế là **ngân sách sai số (error budget)**:

```text
Sai số nào được phép?
Xác suất sai tối đa là bao nhiêu?
Sai theo hướng nào?
Sai có ảnh hưởng tính an toàn hay tiền bạc không?
```

Một Bloom Filter có thể hợp cho “có lẽ đã thấy URL này”, nhưng không phù hợp nếu false positive có thể từ chối quyền truy cập hợp lệ hoặc làm sai số dư tài chính.

## Deterministic guarantee và expected guarantee

Balanced BST có chiều cao worst-case `O(log n)`. Skip List có hiệu năng kỳ vọng `O(log n)` dưới mô hình ngẫu nhiên phù hợp. Hash Table thường có tra cứu kỳ vọng gần `O(1)` nhưng có thể suy giảm trong trường hợp xấu.

Không có loại guarantee “luôn tốt hơn” độc lập bối cảnh. Với hệ thống latency cực nhạy hoặc đối mặt input đối kháng, worst-case bound có thể quan trọng. Với workload bình thường, expected performance có thể cho implementation đơn giản và nhanh hơn.

## Input ngẫu nhiên, input trung bình và input đối kháng

Một phân tích “trung bình” chỉ có ý nghĩa nếu distribution đầu vào được mô tả. Trong thực tế, dữ liệu thường không ngẫu nhiên đều.

ID có thể tăng dần. Timestamps gần như đã sắp xếp. Khóa hash có thể do người dùng kiểm soát. Đồ thị mạng xã hội thường có degree distribution rất lệch.

Do đó nên phân biệt:

```text
average-case theo distribution giả định
expected-case do randomness của thuật toán
worst-case trên mọi input hợp lệ
adversarial-case khi input cố tình phá assumption
```

Hai thuật toán có cùng Big-O trung bình nhưng hành vi khác hẳn dưới dữ liệu có cấu trúc hoặc input độc hại.

## Tiền xử lý là đổi chi phí theo thời gian

Giả sử có `Q` truy vấn. Tổng chi phí có thể được mô hình hóa:

\[
C_{total} = C_{build} + Q\cdot C_{query}
\]

Nếu `Q` rất lớn, tiền xử lý đắt có thể đáng giá. Nếu chỉ một truy vấn, quét tuyến tính có thể tốt hơn xây một chỉ mục phức tạp.

Đây là nguyên lý đứng sau database index, Prefix Sum, Sparse Table, Suffix Array và nhiều cấu trúc tìm kiếm.

## Output-sensitive algorithms

Không phải mọi độ phức tạp chỉ phụ thuộc kích thước input. Một số thuật toán phụ thuộc cả kích thước output.

Ví dụ truy vấn khoảng trong balanced BST có thể có chi phí gần:

\[
O(\log n + k)
\]

với `k` là số phần tử thực sự phải trả ra.

Nếu kết quả chứa một triệu phần tử thì không thuật toán nào có thể “trả” chúng với chi phí thấp hơn việc ít nhất xử lý một triệu output theo mô hình thông thường.

Tư duy **output-sensitive** giúp tránh yêu cầu phi thực tế kiểu “trả tất cả kết quả trong O(log n)”.

## Lower bound: có việc không thể tránh khỏi

Trước khi cố tối ưu, nên hỏi liệu tồn tại cận dưới tự nhiên nào không.

Nếu cần đọc toàn bộ input để biết có phần tử âm hay không, chi phí `Ω(n)` là không tránh khỏi trong mô hình truy cập thông thường. Comparison sort cần phân biệt `n!` thứ tự có thể có nên có cận dưới `Ω(n log n)` trong mô hình chỉ dùng so sánh.

Lower bound giúp phân biệt hai tình huống:

```text
implementation chưa tốt
vs
mô hình bài toán tự nó đòi lượng công việc đó
```

## Reduction: biến bài toán lạ thành bài toán đã hiểu

Một kỹ năng mô hình hóa mạnh là **quy giảm (reduction)**: biến một bài toán thành bài khác sao cho lời giải của bài mới cho lời giải của bài cũ.

Ví dụ:

```text
subtree query -> Euler Tour -> range query
LCA -> Euler Tour/RMQ hoặc Binary Lifting
minimum spanning connectivity -> sort edges + DSU
path with state constraints -> state-space shortest path
interval overlap -> sweep line
```

Reduction giúp tái sử dụng cấu trúc dữ liệu và chứng minh đã biết.

Điểm quan trọng là phải chứng minh mapping bảo toàn ngữ nghĩa. Nếu quá trình biến đổi làm mất một ràng buộc, thuật toán mới có thể giải một bài khác với bài gốc.

## Từ miền bài toán sang miền khóa

Nhiều lựa chọn cấu trúc phụ thuộc trực tiếp miền khóa.

Nếu khóa là số nguyên dày đặc `0..n-1`, một mảng có thể thay HashMap. Nếu khóa là chuỗi có prefix semantics, Trie có thể phù hợp. Nếu khóa có thứ tự toàn phần và cần predecessor/successor, ordered tree phù hợp. Nếu khóa là tập con nhỏ, bitmask có thể biến cả state thành một số nguyên.

Câu hỏi “khóa trông như thế nào?” thường quan trọng ngang “có bao nhiêu phần tử?”.

## Mô hình dữ liệu thưa và dày đặc

Một ma trận `n x n` có thể lưu trực tiếp nếu phần lớn ô có dữ liệu. Nhưng nếu chỉ có `m << n²` cạnh, adjacency list hoặc CSR tiết kiệm hơn adjacency matrix.

Tương tự, DP có thể dùng array nếu state space dày đặc và có chỉ số tự nhiên; dùng HashMap nếu phần lớn trạng thái lý thuyết không bao giờ xuất hiện.

**Mật độ trạng thái (state density)** là một tín hiệu để chọn representation.

## Dominance: loại trạng thái chắc chắn không còn hữu ích

Trong nhiều bài, một trạng thái có thể bị một trạng thái khác **chi phối (dominate)**.

Ví dụ hai trạng thái ở cùng vị trí:

```text
A: cost = 10, fuel = 5
B: cost = 12, fuel = 3
```

Nếu càng ít cost và càng nhiều fuel luôn tốt hơn, `B` không thể dẫn tới lời giải tốt hơn `A`. Ta có thể bỏ `B`.

Dominance pruning là một dạng nén trạng thái dựa trên quan hệ thứ tự từng phần. Nó xuất hiện trong DP, shortest path nhiều tiêu chí, branch-and-bound và search trên Pareto frontier.

## Cấu trúc dữ liệu ghép và bất biến liên cấu trúc

Hệ thống thực tế thường ghép nhiều cấu trúc.

LRU Cache thường dùng Hash Map + Doubly Linked List. Dijkstra dùng adjacency representation + distance array/map + Priority Queue. Autocomplete có thể dùng prefix index + ranking structure.

Khi ghép, ngoài bất biến của từng cấu trúc còn có **bất biến liên cấu trúc (cross-structure invariant)**.

Ví dụ LRU:

```text
mỗi key trong map trỏ đúng node trong list
mỗi node trong list tương ứng đúng một key trong map
head/tail phản ánh recency order
size(map) == size(list)
```

Nhiều bug production không phá bất biến của một cấu trúc đơn lẻ mà phá quan hệ giữa hai cấu trúc.

## Big-O chỉ là một mô hình chi phí

Hai thuật toán cùng `O(n)` có thể khác đáng kể do cache, cấp phát, branch prediction, GC hoặc I/O.

Nên suy nghĩ ít nhất ở hai tầng:

```text
mô hình tiệm cận: chi phí tăng thế nào khi input lớn dần
mô hình máy thật: dữ liệu được di chuyển và cấp phát ra sao
```

Trong database, page I/O có thể quan trọng hơn số phép so sánh. Trong hệ thống phân tán, một network round-trip có thể đắt hơn hàng nghìn phép toán CPU. Trong Java, object-heavy representation có thể làm GC và cache trở thành chi phí chính.

## Bộ nhớ cũng cần mô hình thật

Hai cấu trúc cùng `O(n)` space không nhất thiết tiêu tốn bộ nhớ gần nhau.

Mảng primitive khá gọn. Linked nodes có pointer/reference và object header. Hash Table cần dung lượng dư theo load factor. Trie có thể có rất nhiều nhánh rỗng nếu representation không phù hợp alphabet.

Dung lượng bộ nhớ còn ảnh hưởng tốc độ qua cache và paging, vì vậy space complexity không tách rời time performance trên máy thật.

## Mutability, ownership và concurrency

Trong C, representation còn phải mô hình hóa ai sở hữu bộ nhớ, ai giải phóng và con trỏ nào chỉ được mượn. Trong Java, `equals/hashCode`, identity và GC reachability ảnh hưởng semantics. Trong JavaScript, object identity, `Map`, `Number` và engine representation tạo thêm ràng buộc.

Concurrency bổ sung một chiều khác: cấu trúc đúng trong single-thread chưa chắc đúng khi nhiều luồng cập nhật. Khi đó cần thêm mô hình atomicity, synchronization và visibility. Lock-free structure còn cần reasoning về ABA, memory ordering và reclamation.

Nói cách khác, “cùng một ADT” không có nghĩa cùng một implementation phù hợp cho mọi runtime và mô hình đồng thời.

## Một quy trình mô hình hóa có thể tái sử dụng

Khi gặp bài toán mới, có thể đi theo thứ tự sau:

```text
1. Viết chính xác input, output và objective.
2. Ghi rõ constraints và error model.
3. Liệt kê queries, updates và tỷ lệ xuất hiện.
4. Xác định static/dynamic, online/offline, exact/approximate.
5. Xác định state tối thiểu nhưng đủ thông tin cho tương lai.
6. Tìm quan hệ tương đương và dominance để nén state.
7. Chọn invariant giúp loại bỏ công việc lặp lại.
8. Chọn representation hiện thực invariant hiệu quả.
9. Chứng minh thao tác giữ invariant và đúng semantics.
10. Phân tích Big-O, memory footprint và machine-level costs.
11. Kiểm thử bằng oracle nhỏ, adversarial input và invariant validator.
12. Chỉ tối ưu tiếp khi profiling cho thấy nút thắt thật.
```

Đây là quy trình tổng quát hơn việc học thuộc “mẫu A dùng HashMap, mẫu B dùng Heap”.

## Những sai lầm tư duy phổ biến

“Cấu trúc có Big-O tốt hơn thì luôn tốt hơn” — sai vì workload, locality, bộ nhớ và hệ số hằng khác nhau.

“Có thể chọn thuật toán trước rồi ép bài toán vào” — dễ dẫn tới state thiếu thông tin hoặc model sai.

“`O(1)` nghĩa là chỉ một lệnh” — sai; nó chỉ nói chi phí không tăng theo `n` trong mô hình phân tích.

“Cấu trúc dữ liệu chỉ là container” — sai; nó là container + invariant + semantics + cost contract.

“Nếu state chứa càng nhiều thông tin thì càng an toàn” — sai; state dư thừa có thể làm không gian tìm kiếm tăng theo tích nhiều chiều và biến bài khả thi thành không khả thi.

“Preprocessing luôn tốt” — sai; nó chỉ đáng khi số truy vấn hoặc yêu cầu latency biện minh cho chi phí build và memory.

## Mô hình tư duy

> Cấu trúc dữ liệu là một hợp đồng về **thông tin nào được giữ sẵn và bất biến nào phải luôn đúng**. Thuật toán là một hợp đồng về **trạng thái biến đổi như thế nào**. Mô hình hóa quyết định thông tin nào thực sự cần tồn tại để tương lai được xác định.

Khi gặp một bài DSA mới, hãy hỏi: **trạng thái thật sự là gì, phần nào của lịch sử còn ảnh hưởng tương lai, truy vấn nào phải rẻ, có thể tiền xử lý hay nén state không, guarantee nào thật sự cần, và invariant nào giúp loại bỏ phần công việc không cần thiết?**

Xem tiếp: [Correctness & Invariants](./01_algorithm_correctness_and_invariants.md), [Complexity Analysis](./02_complexity_analysis.md), [Memory Models](./03_memory_models_c_java_javascript.md), [Mathematical Toolkit](./04_mathematical_toolkit_for_dsa.md), [Dynamic Programming](../04_algorithmic_paradigms/05_dynamic_programming.md) và [Problem Solving Workflow](../90_connections/02_problem_solving_workflow.md).