# Greedy nâng cao: Matroid, Primal–Dual và Xấp xỉ

> **Mạch đọc:** Đọc **Greedy nâng cao: Matroid, Primal–Dual và Xấp xỉ** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Greedy đúng không phải vì lựa chọn cục bộ trông tốt** sang **2. Hệ độc lập**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

**Advanced Greedy tối ưu hóa (optimization / 최적화) / 고급 그리디 최적화**

Các ví dụ greedy cơ bản như lập lịch khoảng, Kruskal hay Huffman cho thấy một lựa chọn cục bộ đôi khi có thể khóa vĩnh viễn mà vẫn giữ tối ưu toàn cục. Nhưng để hiểu greedy sâu hơn, cần trả lời câu hỏi cấu trúc:

> **Điều gì trong không gian nghiệm khiến một lựa chọn cục bộ có thể được chứng minh là an toàn?**

Chương này đi xa hơn các “mẫu chọn sớm nhất/nhẹ nhất”, tập trung vào cấu trúc trao đổi, matroid, primal–dual, submodularity và greedy xấp xỉ.

## 1. Greedy đúng không phải vì lựa chọn cục bộ trông tốt

Một thuật toán greedy chỉ có ý nghĩa khi ta có một trong các dạng chứng minh:

```text
exchange argument
cut/cycle property
stays-ahead argument
matroid exchange property
primal-dual certificate
submodular diminishing returns
```

Nếu không có cấu trúc chứng minh, greedy chỉ là heuristic.

## 2. Hệ độc lập

Nhiều bài toán có thể mô tả bằng một tập phần tử nền `E` và một họ các tập hợp “hợp lệ” `I`.

Ví dụ với đồ thị:

```text
E = tập cạnh
I = các tập cạnh không tạo chu trình
```

Ta muốn chọn một tập hợp hợp lệ có trọng số tốt nhất.

Điểm quan trọng là tách hai lớp:

```text
feasibility -> một tập có hợp lệ không?
objective   -> tập hợp lệ nào có giá trị tốt nhất?
```

Greedy thường thành công khi family của tập hợp hợp lệ có cấu trúc trao đổi đủ mạnh.

## 3. Matroid

Một **matroid** gồm tập nền `E` và họ các tập độc lập `I` thỏa hai tính chất chính.

**Tính di truyền (hereditary):**

```text
A thuộc I và B ⊆ A => B thuộc I
```

Nếu một tập hợp hợp lệ, bỏ bớt phần tử vẫn hợp lệ.

**Tính trao đổi (exchange):** nếu `A` và `B` đều độc lập và `|A| < |B|`, tồn tại phần tử `x` trong `B \ A` sao cho `A ∪ {x}` vẫn độc lập.

Tính trao đổi nói rằng một tập độc lập nhỏ hơn luôn có thể “học” thêm ít nhất một phần tử từ tập lớn hơn mà không phá tính hợp lệ.

## 4. Vì sao matroid làm greedy đúng?

Giả sử mỗi phần tử có trọng số và ta muốn chọn một tập độc lập có tổng trọng số lớn nhất.

Greedy:

1. sắp xếp phần tử theo trọng số giảm dần;
2. duyệt theo thứ tự;
3. thêm phần tử nếu tập vẫn độc lập.

Trong matroid, exchange thuộc tính (property / 속성) cho phép biến đổi một nghiệm tối ưu thành nghiệm chứa dần các lựa chọn greedy mà không giảm tổng trọng số.

Đây là một định lý rất mạnh: greedy không đúng “do may mắn” cho từng bài riêng; nó đúng cho **cả một lớp cấu trúc**.

## 5. Graphic Matroid và Kruskal

Với đồ thị, tập cạnh không tạo chu trình là independent set. Đây là **graphic matroid**.

Kruskal sắp cạnh theo trọng số tăng dần và thêm cạnh nếu không tạo chu trình. Nếu đổi dấu trọng số hoặc nhìn theo maximum spanning forest, đây chính là greedy trên graphic matroid.

DSU chỉ là công cụ kiểm tra independence nhanh; tính đúng đắn (correctness / 정확성) đến từ cấu trúc matroid/cut thuộc tính (property / 속성).

Điều này giúp phân biệt:

```text
DSU -> implementation mechanism
matroid/cut property -> correctness structure
```

## 6. Partition Matroid

Giả sử phần tử được chia thành các nhóm và mỗi nhóm chỉ được chọn tối đa `k_i` phần tử.

Ví dụ:

```text
mỗi department chọn tối đa 2 người
mỗi category lấy tối đa 1 sản phẩm
```

Các tập thỏa ràng buộc này tạo một partition matroid.

Greedy theo trọng số giảm dần và chỉ thêm phần tử khi quota nhóm chưa vượt thường là tối ưu cho một matroid duy nhất.

## 7. Khi giao của hai matroid xuất hiện

Nhiều bài toán khó hơn có thể được diễn tả là phải thỏa đồng thời hai family độc lập. Khi đó greedy đơn giản không còn được bảo đảm.

Ví dụ matching hai phía có thể liên hệ tới intersection của các partition-like các ràng buộc (constraints / 제약조건들): một đỉnh trái và một đỉnh phải đều không được dùng quá một lần.

Matroid intersection là bài toán mạnh hơn greedy đơn giản và cần thuật toán chuyên biệt.

Bài học:

> Chỉ vì từng ràng buộc riêng lẻ “trông greedy được” không có nghĩa giao của chúng vẫn greedy được.

## 8. Greedoid và feasibility phụ thuộc thứ tự

Matroid giả định mọi subset của independent set vẫn độc lập. Nhưng có bài toán nơi tính hợp lệ phụ thuộc cách xây dựng tuần tự.

**Greedoid** là một cấu trúc tổng quát hơn cho một số bài toán dạng khả năng đạt tới hoặc xây dựng từng bước.

Không cần đi sâu hình thức để sử dụng hằng ngày, nhưng khái niệm này nhắc rằng “exchange cấu trúc (structure / 구조)” có nhiều mức độ; matroid không phải khuôn duy nhất.

## 9. Primal–Dual: nhìn greedy qua cặp bài toán

Nhiều bài tối ưu có thể có một bài toán **primal** và một bài toán **dual**. Dual tạo một cận cho primal.

Thuật toán primal–dual thường:

1. bắt đầu với nghiệm dual khả thi;
2. tăng các biến dual tới khi một ràng buộc primal trở nên “tight”;
3. dùng sự kiện tight đó để chọn phần tử cho nghiệm primal;
4. cuối cùng dùng quan hệ giữa hai nghiệm để chứng minh chất lượng.

Đây là một cách nhìn sâu hơn về greedy: thay vì chỉ “chọn phần tử tốt nhất”, ta xây đồng thời một **chứng chỉ cận dưới/cận trên**.

## 10. Set Cover và greedy xấp xỉ

Set Cover:

```text
Universe U
các tập S1, S2, ...
chọn ít tập nhất để phủ toàn bộ U
```

Bài toán là NP-hard. Greedy kinh điển chọn tập phủ được nhiều phần tử chưa phủ nhất ở mỗi bước.

Greedy không luôn tối ưu, nhưng có bảo đảm xấp xỉ logarithmic.

Đây là thay đổi quan trọng trong tư duy:

> Khi tối ưu chính xác quá khó, greedy vẫn có thể rất giá trị nếu ta chứng minh được **approximation ratio**.

## 11. Weighted Set Cover

Nếu mỗi tập có chi phí `c(S)`, một tiêu chí tự nhiên là:

\[
\frac{c(S)}{\văn bản (text / 텍스트){số phần tử mới được phủ}}
\]

chọn tập có chi phí trên mỗi coverage mới thấp nhất.

Bảo đảm xấp xỉ vẫn dựa trên lập luận dạng charging/dual-fitting, không phải vì ratio “có vẻ hợp lý”.

## 12. Vertex Cover và primal–dual intuition

Trong weighted Vertex Cover, có thể tăng giá dual trên các cạnh cho tới khi tổng dual chạm chi phí của một đỉnh, rồi chọn đỉnh đó.

Các cạnh “trả tiền” dần cho các đỉnh. Khi một đỉnh trở nên tight, nó được đưa vào nghiệm.

Cách nhìn này rất khác greedy theo score thuần túy nhưng vẫn mang tinh thần cục bộ (local / 로컬), monotonic và có certificate.

## 13. Diminishing Returns và hàm submodular

Một hàm tập hợp `f(S)` là **submodular** nếu lợi ích biên của việc thêm phần tử giảm khi tập hiện tại lớn hơn.

Trực giác:

```text
A ⊆ B
marginal gain của x khi thêm vào A
>= marginal gain của x khi thêm vào B
```

Đây là nguyên lý **lợi ích giảm dần (diminishing returns)**.

Coverage là ví dụ: khi đã phủ nhiều phần tử, một tập mới thường mang lại ít phần tử chưa phủ hơn.

## 14. Greedy cho Submodular Maximization

Nếu `f` đơn điệu, submodular và ta chỉ được chọn tối đa `k` phần tử, greedy lặp lại chọn phần tử có marginal gain lớn nhất.

Thuật toán không nhất thiết tối ưu nhưng có bảo đảm gần `1 - 1/e` trong mô hình chuẩn.

Kết quả này cực kỳ quan trọng vì nhiều bài:

```text
chọn vị trí cảm biến
chọn seed trong mạng
chọn feature
chọn đại diện/tóm tắt
```

có cấu trúc submodular hoặc gần submodular.

## 15. Lazy Greedy

Tính lại marginal gain của mọi phần tử sau mỗi bước có thể đắt.

Vì submodularity làm marginal gain chỉ giảm, ta có thể giữ một max-heap theo upper bound cũ. Khi một ứng viên lên đầu, tính lại gain hiện tại; nếu nó vẫn lớn nhất, chọn nó, nếu không cập nhật rồi đưa lại vùng nhớ động (heap / 힙).

Đây là **lazy greedy**.

Cấu trúc toán học (marginal gain chỉ giảm) cho phép giảm số lần đánh giá hàm trong thực tế mà không đổi kết quả greedy.

## 16. Greedy và Online Algorithms

Trong bài online, quyết định phải đưa ra trước khi biết tương lai. Một greedy quy tắc (rule / 규칙) có thể hợp lý nhưng không còn được so trực tiếp với optimal offline theo cùng thông tin.

Ta dùng **competitive ratio** để so chi phí online với nghiệm tối ưu biết trước toàn bộ đầu vào (input / 입력).

Ví dụ caching/paging dẫn tới các chính sách như LRU, FIFO và các kết quả cạnh tranh tùy mô hình.

Điểm quan trọng:

```text
greedy offline tối ưu
khác
greedy online có competitive guarantee
```

## 17. Ski Rental: mẫu quyết định online cơ bản

Ta thuê mỗi ngày hoặc mua một lần. Không biết sẽ dùng bao lâu.

Một chiến lược xác định: thuê cho tới khi tổng tiền thuê gần bằng giá mua, sau đó mua.

Chiến lược này không luôn tối ưu cho từng đầu vào (input / 입력), nhưng có competitive ratio bị chặn.

Đây là ví dụ tốt để hiểu rằng khi tương lai bị ẩn, “tối ưu tuyệt đối” không còn là tiêu chuẩn phù hợp.

## 18. Greedy và Streaming

Trong streaming, bộ nhớ hạn chế khiến ta không thể giữ toàn bộ ứng viên. Các thuật toán như Misra–Gries, Space-Saving hoặc một số sampling scheme duy trì tóm lược theo quy tắc (rule / 규칙) cục bộ.

Một lựa chọn cục bộ trong streaming thường phải được đánh giá theo:

```text
memory bound
error guarantee
mergeability
one-pass constraint
```

chứ không chỉ mục tiêu (objective / 목표) combinatorial cổ điển.

## 19. Exchange đồ thị (graph / 그래프)

Trong một số bài tối ưu, ta có thể xây **exchange đồ thị (graph / 그래프)** giữa phần tử đang chọn và chưa chọn. Một đường đi trong exchange đồ thị (graph / 그래프) mô tả chuỗi thay thế giữ feasibility.

Matroid intersection, matching và local-improvement algorithms có thể được hiểu theo cách này.

Đây là cầu nối giữa greedy, augmenting đường dẫn (path / 경로) và tối ưu tổ hợp.

## 20. cục bộ (local / 로컬) tìm kiếm (search / 검색) khác Greedy ở đâu?

Greedy xây nghiệm một chiều và không quay lại. **cục bộ (local / 로컬) tìm kiếm (search / 검색)** bắt đầu từ một nghiệm rồi thực hiện các phép thay đổi cục bộ để cải thiện.

Ví dụ:

```text
1-swap
2-swap
k-exchange
```

Một nghiệm cục bộ (local / 로컬) optimum không nhất thiết toàn cục (global / 전역) optimum. Nhưng với một số bài, cục bộ (local / 로컬) tìm kiếm (search / 검색) có approximation guarantee.

Greedy và cục bộ (local / 로컬) tìm kiếm (search / 검색) đều dùng quyết định cục bộ, nhưng không nên trộn lẫn hai paradigm.

## 21. Greedy + tìm kiếm nhị phân (binary search / 이진 탐색)

Có những bài tối ưu không greedy trực tiếp theo mục tiêu (objective / 목표), nhưng bài **kiểm tra tính khả thi** ở một ngưỡng lại greedy được.

Mẫu:

```text
binary search answer X
    ↓
greedy check: có đạt được X không?
```

Ví dụ chia mảng thành số đoạn giới hạn với maximum sum không vượt `X`, hoặc đặt đối tượng với khoảng cách tối thiểu `X` dưới một số ràng buộc.

Greedy lúc này là oracle feasibility, còn tìm kiếm nhị phân (binary search / 이진 탐색) xử lý không gian mục tiêu (objective / 목표).

## 22. Greedy + vùng nhớ động (heap / 힙)

Một mẫu (pattern / 패턴) mạnh:

1. sắp xếp sự kiện theo deadline/thời gian (time / 시간);
2. thêm ứng viên hiện tại vào vùng nhớ động (heap / 힙);
3. nếu ràng buộc (constraint / 제약조건) bị vi phạm, loại phần tử tệ nhất đang chọn.

Ví dụ chọn nhiều tác vụ (task / 작업) nhất dưới deadline với duration khác nhau: sort theo deadline, thêm duration vào max-heap, nếu tổng thời gian vượt deadline thì bỏ tác vụ (task / 작업) dài nhất.

Bất biến (invariant / 불변식) là sau mỗi prefix deadline, ta giữ một tập tác vụ (task / 작업) khả thi có số lượng tối đa, và trong số đó tổng duration nhỏ nhất theo exchange lập luận (reasoning / 추론).

## 23. Greedy + DSU

Kruskal là ví dụ rõ nhất: greedy quyết định thứ tự cạnh; DSU chỉ bảo vệ feasibility “không tạo chu trình”.

Một mẫu (pattern / 패턴) rộng hơn là:

```text
sort candidates theo score
greedy scan
DSU/bitset/tree kiểm tra constraint nhanh
```

Cấu trúc dữ liệu phụ trợ không tạo tính đúng đắn (correctness / 정확성); nó làm phép kiểm tra greedy nhanh hơn.

## 24. Những tín hiệu greedy có thể đúng

Các dấu hiệu đáng điều tra:

```text
có exchange argument tự nhiên
sau lựa chọn, phần còn lại giữ cùng dạng bài toán
feasibility có tính di truyền
có cut/cycle property
có diminishing returns
có thứ tự làm một lựa chọn trở nên irrevocably safe
```

Nhưng đây chỉ là tín hiệu để tìm chứng minh, không phải giấy phép bỏ qua chứng minh.

## 25. Những tín hiệu greedy dễ sai

Cảnh báo khi:

```text
lựa chọn hiện tại thay đổi mạnh giá trị của lựa chọn tương lai
có complementarity: hai phần tử riêng lẻ kém nhưng đi cùng rất tốt
constraint không có exchange property
phải hy sinh lợi ích ngắn hạn để mở khóa trạng thái tốt hơn
objective phụ thuộc toàn bộ lịch sử
```

0/1 Knapsack và nhiều bài scheduling có trọng số là ví dụ.

## 26. Kiểm thử một ý tưởng Greedy

Trước khi viết chứng minh dài, hãy dùng brute force trên đầu vào (input / 입력) nhỏ để tìm phản ví dụ.

Quy trình:

```text
sinh mọi input nhỏ
chạy greedy candidate
chạy exhaustive search / DP oracle
so sánh objective
```

Nếu tìm phản ví dụ, quy tắc (rule / 규칙) sai. Nếu không tìm thấy, đó vẫn chưa phải chứng minh, nhưng giúp lọc heuristic yếu rất nhanh.

Property-based generation nên tập trung vào trường hợp hòa, giá trị cực đoan và đầu vào (input / 입력) làm các lựa chọn cục bộ cạnh tranh sát nhau.

## 27. Chứng chỉ tối ưu

Một lời giải greedy mạnh đôi khi tạo kèm certificate.

MST có cut/cycle thuộc tính (property / 속성). Primal–dual có dual solution. Scheduling có exchange/stays-ahead argument. Matching có augmenting-path characterization.

Trong môi trường vận hành (production / 운영 환경) tối ưu hóa (optimization / 최적화), certificate hữu ích vì giúp kiểm tra (audit / 감사): không chỉ có answer mà còn có lý do answer đạt một cận đã biết.

## Mô hình tư duy

> Greedy không phải “chọn thứ tốt nhất hiện tại”. Greedy là **khóa một quyết định cục bộ vì cấu trúc toán học chứng minh rằng quyết định đó không làm mất mọi lời giải tối ưu hoặc làm mất quá nhiều chất lượng**.

Khi đánh giá một chiến lược greedy, hãy hỏi:

```text
Feasibility family có exchange structure không?
Có thể biến một optimum thành optimum chứa lựa chọn greedy không?
Nếu exact optimum quá khó, greedy có approximation guarantee không?
Có primal/dual hoặc charging argument để chứng minh chất lượng không?
Có diminishing returns không?
Bài là offline hay online?
```

Xem thêm: [Greedy cơ bản](./04_greedy_algorithms.md), [MST](../03_graphs/03_minimum_spanning_trees.md), [Network Flow & Matching](../03_graphs/08_network_flow_and_matching.md), [Hard Problems & Approximation](./09_hard_problems_reductions_and_approximation.md), [Selection & Top-K](./06_selection_and_top_k.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 searching](./00_searching.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
