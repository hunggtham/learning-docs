# Luồng mạng và ghép cặp hai phía

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Luồng mạng và ghép cặp hai phía**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Định nghĩa một luồng (flow / 흐름) hợp lệ** cho thấy đối tượng vận hành qua những bước nào và tạo ra hệ quả gì; sau đó sang **2. Max luồng (flow / 흐름)** để giải thích cách điều kiện hoặc mục tiêu đó vận hành. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**mạng (network / 네트워크) luồng (flow / 흐름) & Bipartite Matching / 네트워크 플로우와 이분 매칭**

Luồng mạng mô hình hóa việc phân phối một đại lượng qua các tuyến có giới hạn. “Đại lượng” có thể là hàng hóa, lưu lượng mạng, job được gán cho worker, đơn vị hàng hóa đi qua chuỗi cung ứng hoặc chỉ là một đại lượng toán học giúp biến một bài toán tổ hợp thành bài toán luồng.

Sức mạnh của mô hình luồng (flow / 흐름) không nằm ở ẩn dụ chất lỏng, mà ở việc nhiều bài toán “phân phối dưới ràng buộc” có thể được biểu diễn thống nhất bằng:

```text
đỉnh
cạnh
sức chứa
nguồn / đích
bảo toàn
```

Một khi mô hình đúng, cùng một bộ định lý và thuật toán có thể giải matching, cut, đường đi rời nhau, phân công, circulation và nhiều bài toán chọn tập có cấu trúc.

## 1. Định nghĩa một luồng (flow / 흐름) hợp lệ

Ta có đồ thị có hướng, nguồn `s`, đích `t` và sức chứa `c(u,v) >= 0`.

Luồng (flow / 흐름) `f(u,v)` phải thỏa:

\[
0\le f(u,v)\le c(u,v)
\]

và tại mọi đỉnh trung gian:

\[
\sum_x f(x,v)=\sum_y f(v,y)
\]

Điều kiện thứ hai là **bảo toàn luồng (flow conservation)**: đỉnh trung gian không tự sinh hoặc làm mất tài nguyên.

Giá trị luồng bằng tổng luồng rời nguồn, đồng thời bằng tổng luồng đi vào đích nếu bảo toàn đúng.

> **Chuyển mạch:** Trong **Luồng mạng và ghép cặp hai phía**, **1. Định nghĩa một luồng (flow / 흐름) hợp lệ** xác định đầu vào; **2. Max luồng (flow / 흐름)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **3. Đồ thị dư là không gian các thay đổi còn có thể thực hiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Max luồng (flow / 흐름)

Bài toán **luồng cực đại (maximum flow)** tìm giá trị luồng (flow / 흐름) lớn nhất có thể gửi từ `s` tới `t` mà không vượt sức chứa.

Một chiến lược tham lam ngây thơ “chọn đường rồi khóa luôn quyết định” có thể thất bại vì đường chọn sớm có thể chiếm sức chứa (capacity / 용량) cần cho lời giải tốt hơn.

Ý tưởng giải quyết vấn đề này là **đồ thị dư (residual graph)**.

> **Chuyển mạch:** Ở chặng này của **Luồng mạng và ghép cặp hai phía**, **2. Max luồng (flow / 흐름)** xác định đầu vào; **3. Đồ thị dư là không gian các thay đổi còn có thể thực hiện** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **4. Đường tăng và bottleneck** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Đồ thị dư là không gian các thay đổi còn có thể thực hiện

Nếu cạnh `u -> v` có sức chứa (capacity / 용량) 10 và hiện đang mang luồng (flow / 흐름) 6:

```text
forward residual capacity = 4
reverse residual capacity = 6
```

Cạnh ngược không nhất thiết tồn tại trong mạng vật lý. Nó biểu diễn khả năng **rút lại** một phần quyết định cũ để chuyển luồng sang đường khác.

Mô hình tư duy quan trọng nhất:

> Residual đồ thị (graph / 그래프) không mô tả mạng gốc; nó mô tả **không gian những chỉnh sửa khả thi trên lời giải hiện tại**.

Đây là lý do augmenting-path thuật toán (algorithm / 알고리즘) có thể sửa sai lựa chọn trước đó thay vì bị kẹt bởi quyết định greedy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Luồng mạng và ghép cặp hai phía**, **4. Đường tăng và bottleneck** tiếp nhận điểm tựa từ **3. Đồ thị dư là không gian các thay đổi còn có thể thực hiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Ford–Fulkerson là một khung thuật toán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Đường tăng và bottleneck

Một **đường tăng (augmenting path)** là đường từ `s` tới `t` trong residual đồ thị (graph / 그래프) mà mọi cạnh đều còn dung lượng dư dương.

Ta có thể tăng luồng một lượng:

\[
\Delta=\min_{e\in đường dẫn (path / 경로)} c_{residual}(e)
\]

Sau đó cập nhật forward/reverse residual capacities.

Nếu không còn augmenting đường dẫn (path / 경로), luồng (flow / 흐름) hiện tại không thể được cải thiện bằng bất kỳ thay đổi hợp lệ nào trong residual đồ thị (graph / 그래프).

> **Chuyển mạch:** Trong **Luồng mạng và ghép cặp hai phía**, **5. Ford–Fulkerson là một khung thuật toán** tiếp nhận điểm tựa từ **4. Đường tăng và bottleneck** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Edmonds–Karp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Ford–Fulkerson là một khung thuật toán

Ford–Fulkerson chỉ nói:

```text
while còn augmenting path:
    tìm một augmenting path
    đẩy bottleneck flow
```

Cách chọn đường dẫn (path / 경로) quyết định độ phức tạp (complexity / 복잡도) thực tế.

Với sức chứa (capacity / 용량) nguyên, mỗi augmentation tăng giá trị luồng (flow / 흐름) ít nhất 1 nên thuật toán kết thúc. Với sức chứa (capacity / 용량) lớn, số augmentation có thể phụ thuộc vào magnitude của sức chứa (capacity / 용량) chứ không chỉ kích thước đồ thị.

Với số thực, các vấn đề hội tụ lý thuyết còn tinh tế hơn. Vì vậy hiện thực (implementation / 구현) DSA thường dùng sức chứa (capacity / 용량) nguyên hoặc kiểu số có ngữ nghĩa rõ ràng.

> **Chuyển mạch:** Ở chặng này của **Luồng mạng và ghép cặp hai phía**, **6. Edmonds–Karp** tiếp nhận điểm tựa từ **5. Ford–Fulkerson là một khung thuật toán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Dinic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Edmonds–Karp

Edmonds–Karp chọn augmenting đường dẫn (path / 경로) ngắn nhất theo số cạnh bằng BFS.

Độ phức tạp (complexity / 복잡도) cổ điển:

\[
O(VE^2)
\]

Điều đáng học không phải chỉ công thức mà là lý do: khoảng cách BFS trong residual đồ thị (graph / 그래프) từ nguồn tới các đỉnh không giảm qua các augmentation phù hợp, và mỗi cạnh chỉ có thể trở thành bottleneck ở một tầng nhất định hữu hạn lần.

Edmonds–Karp rất tốt để học tính đúng đắn (correctness / 정확성) và residual mechanics, nhưng thường chậm hơn Dinic trên đồ thị lớn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Luồng mạng và ghép cặp hai phía**, **7. Dinic** tiếp nhận điểm tựa từ **6. Edmonds–Karp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Current-Arc tối ưu hóa (optimization / 최적화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Dinic

Dinic chạy theo các pha:

1. BFS xây **mức (level / 수준) đồ thị (graph / 그래프)**;
2. chỉ giữ residual edge đi từ mức (level / 수준) `d` sang `d+1`;
3. DFS đẩy **blocking luồng (flow / 흐름)** cho đến khi không còn đường `s -> t` trong mức (level / 수준) đồ thị (graph / 그래프) đó;
4. xây mức (level / 수준) đồ thị (graph / 그래프) mới.

Sau mỗi blocking-flow phase, độ dài đường residual ngắn nhất từ `s` tới `t` tăng.

Cận tổng quát thường được trình bày là:

\[
O(V^2E)
\]

nhưng nhiều lớp đồ thị đặc biệt có cận tốt hơn.

Trong thực hành, Dinic thường là lựa chọn cân bằng giữa hiệu năng và độ phức tạp hiện thực (implementation / 구현).

> **Chuyển mạch:** Trong **Luồng mạng và ghép cặp hai phía**, **8. Current-Arc tối ưu hóa (optimization / 최적화)** tiếp nhận điểm tựa từ **7. Dinic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Max-Flow Min-Cut** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Current-Arc tối ưu hóa (optimization / 최적화)

Trong DFS của Dinic, nếu một cạnh đã được thử hết trong phase hiện tại, không nên quét lại từ đầu.

Ta giữ:

```text
ptr[v] = cạnh tiếp theo cần thử của v
```

Tối ưu hóa (optimization / 최적화) này không thay đổi ý tưởng toán học nhưng giảm đáng kể việc quét lặp adjacency danh sách (list / 목록).

Đây là ví dụ DSA quan trọng: cùng một thuật toán lý thuyết nhưng cách tổ chức trạng thái phụ có thể quyết định hiệu năng hiện thực (implementation / 구현).

> **Chuyển mạch:** Ở chặng này của **Luồng mạng và ghép cặp hai phía**, **8. Current-Arc tối ưu hóa (optimization / 최적화)** xác định đầu vào; **9. Max-Flow Min-Cut** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **10. Duality intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Max-Flow Min-Cut

Một cut chia các đỉnh thành `S` và `T`, với `s∈S`, `t∈T`.

Dung lượng cut:

\[
c(S,T)=\sum_{u\in S,v\in T} c(u,v)
\]

Mọi luồng (flow / 흐름) từ `s` sang `t` phải đi qua cut, nên:

\[
|f|\le c(S,T)
\]

Định lý max-flow min-cut nói:

\[
\max luồng (flow / 흐름) = \min cut
\]

Khi residual đồ thị (graph / 그래프) không còn đường từ `s` tới `t`, tập đỉnh còn reachable từ `s` trong residual đồ thị (graph / 그래프) chính là phía `S` của một min-cut tương ứng.

Luồng (flow / 흐름) hiện tại và cut này tạo ra **certificate tối ưu**: cận dưới và cận trên gặp nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Luồng mạng và ghép cặp hai phía**, **9. Max-Flow Min-Cut** xác định đầu vào; **10. Duality intuition** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **11. Bipartite Matching như một bài luồng (flow / 흐름)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Duality intuition

Max-flow hỏi: “đẩy được bao nhiêu?”. Min-cut hỏi: “cần chặn tổng sức chứa nhỏ nhất bao nhiêu để tách nguồn và đích?”.

Hai bài nhìn khác nhau nhưng có cùng giá trị tối ưu.

Đây là một ví dụ trực quan của **đối ngẫu (duality)** trong tối ưu hóa: lời giải primal và một certificate dual có thể xác nhận tính tối ưu lẫn nhau.

> **Chuyển mạch:** Trong **Luồng mạng và ghép cặp hai phía**, **10. Duality intuition** xác định đầu vào; **11. Bipartite Matching như một bài luồng (flow / 흐름)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **12. Integrality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Bipartite Matching như một bài luồng (flow / 흐름)

Với hai phía `L` và `R`:

```text
source -> L        capacity 1
L -> R             capacity 1 nếu có cạnh matching
R -> sink          capacity 1
```

Mỗi đơn vị (unit / 단위) luồng (flow / 흐름) qua một cạnh `L -> R` tương ứng với một cặp được ghép.

Sức chứa (capacity / 용량) 1 ở nguồn và đích đảm bảo một đỉnh không được dùng trong hai cặp.

> **Chuyển mạch:** Ở chặng này của **Luồng mạng và ghép cặp hai phía**, **11. Bipartite Matching như một bài luồng (flow / 흐름)** xác định đầu vào; **12. Integrality** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **13. Augmenting đường dẫn (path / 경로) trong matching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Integrality

Nếu sức chứa (capacity / 용량) đều nguyên, tồn tại max luồng (flow / 흐름) nguyên.

Tính chất này rất quan trọng: luồng (flow / 흐름) equations nhìn giống bài liên tục, nhưng với mạng matching sức chứa (capacity / 용량) nguyên, lời giải tự nhiên cho ra số cặp nguyên thay vì “0.3 worker”.

Tính nguyên của luồng (flow / 흐름) là cầu nối giữa tối ưu liên tục kiểu đại số và bài toán tổ hợp rời rạc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Luồng mạng và ghép cặp hai phía**, **12. Integrality** xác định đầu vào; **13. Augmenting đường dẫn (path / 경로) trong matching** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **14. Hopcroft–Karp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Augmenting đường dẫn (path / 경로) trong matching

Trong matching, augmenting đường dẫn (path / 경로) luân phiên giữa:

```text
cạnh chưa nằm trong matching
cạnh đang nằm trong matching
```

và bắt đầu/kết thúc ở hai đỉnh chưa ghép.

Flip trạng thái của các cạnh trên đường dẫn (path / 경로) làm matching tăng thêm đúng 1 cạnh.

Đây chính là phiên bản matching của residual-path lập luận (reasoning / 추론).

> **Chuyển mạch:** Trong **Luồng mạng và ghép cặp hai phía**, **13. Augmenting đường dẫn (path / 경로) trong matching** xác định đầu vào; **14. Hopcroft–Karp** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **15. Hall’s Theorem** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Hopcroft–Karp

Với maximum bipartite matching không trọng số, Hopcroft–Karp khai thác cấu trúc đặc biệt tốt hơn generic luồng (flow / 흐름).

Độ phức tạp (complexity / 복잡도):

\[
O(E\sqrt V)
\]

BFS tìm tầng của các augmenting đường dẫn (path / 경로) ngắn nhất, rồi DFS tìm nhiều augmenting đường dẫn (path / 경로) vertex-disjoint trong cùng phase.

Ý tưởng gần Dinic nhưng chuyên biệt hơn.

Bài học tổng quát:

> Reduction về bài tổng quát giúp hiểu cấu trúc; nếu miền có thêm bất biến đặc biệt, thuật toán chuyên biệt có thể nhanh hơn.

> **Chuyển mạch:** Ở chặng này của **Luồng mạng và ghép cặp hai phía**, **15. Hall’s Theorem** tiếp nhận điểm tựa từ **14. Hopcroft–Karp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Vertex Cover và Kőnig’s Theorem** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Hall’s Theorem

Với bipartite đồ thị (graph / 그래프) `G=(L,R,E)`, tồn tại matching phủ mọi đỉnh của `L` khi và chỉ khi với mọi tập con `S⊆L`:

\[
|N(S)|\ge |S|
\]

Trực giác: mọi nhóm `S` bên trái phải có ít nhất đủ số hàng xóm bên phải để ghép riêng cho từng phần tử.

Hall’s theorem là characterization mang tính cấu trúc, còn matching thuật toán (algorithm / 알고리즘) là thủ tục xây dựng lời giải.

Đây là một ví dụ đẹp cho mối quan hệ giữa **định lý tồn tại** và **thuật toán xây dựng**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Luồng mạng và ghép cặp hai phía**, **16. Vertex Cover và Kőnig’s Theorem** tiếp nhận điểm tựa từ **15. Hall’s Theorem** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. nút (node / 노드) Splitting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Vertex Cover và Kőnig’s Theorem

Trong bipartite đồ thị (graph / 그래프):

\[
|maximum\ matching| = |minimum\ vertex\ cover|
\]

Đây là Kőnig’s theorem.

Sau khi có maximum matching, có thể xây minimum vertex cover bằng traversal trên alternating đồ thị (graph / 그래프) theo quy tắc phù hợp.

Đây là một ví dụ khác của primal/dual certificate trong bài toán rời rạc.

> **Chuyển mạch:** Trong **Luồng mạng và ghép cặp hai phía**, **17. nút (node / 노드) Splitting** tiếp nhận điểm tựa từ **16. Vertex Cover và Kőnig’s Theorem** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Edge-Disjoint và Vertex-Disjoint Paths** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. nút (node / 노드) Splitting

Nếu sức chứa (capacity / 용량) nằm ở đỉnh thay vì cạnh, tách:

```text
v_in -> v_out  capacity = cap(v)
```

Mọi cạnh vào nối tới `v_in`, mọi cạnh ra xuất phát từ `v_out`.

Kỹ thuật này chuyển vertex ràng buộc (constraint / 제약조건) thành edge ràng buộc (constraint / 제약조건).

Ứng dụng:

```text
vertex-disjoint paths
giới hạn số job qua một server
resource capacity tại nút trung gian
```

> **Chuyển mạch:** Ở chặng này của **Luồng mạng và ghép cặp hai phía**, **17. nút (node / 노드) Splitting** xác định đầu vào; **18. Edge-Disjoint và Vertex-Disjoint Paths** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **19. Nhiều nguồn và nhiều đích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Edge-Disjoint và Vertex-Disjoint Paths

Nếu mỗi cạnh có sức chứa (capacity / 용량) 1, max luồng (flow / 흐름) cho số đường `s-t` không dùng chung cạnh lớn nhất trong mô hình phù hợp.

Nếu cần không dùng chung đỉnh, dùng nút (node / 노드) splitting với sức chứa (capacity / 용량) 1 cho các đỉnh trung gian.

Điều này liên hệ chặt với Menger’s theorem: số đường rời nhau cực đại và kích thước cut tối thiểu phản ánh cùng một cấu trúc kết nối.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Luồng mạng và ghép cặp hai phía**, **18. Edge-Disjoint và Vertex-Disjoint Paths** nêu điều cần giải thích; **19. Nhiều nguồn và nhiều đích** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. Circulation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Nhiều nguồn và nhiều đích

Thêm **super nguồn (source / 소스)** nối tới các nguồn thật và **super sink** nối từ các đích thật.

Sức chứa (capacity / 용량) của cạnh nhân tạo phải đủ lớn hoặc bằng giới hạn cung/cầu tương ứng.

Kỹ thuật này biến nhiều nguồn/đích về đúng dạng single-source single-sink của max-flow chuẩn.

> **Chuyển mạch:** Trong **Luồng mạng và ghép cặp hai phía**, **19. Nhiều nguồn và nhiều đích** nêu điều cần giải thích; **20. Circulation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **21. Lower Bounds trên cạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Circulation

Circulation bỏ yêu cầu nguồn/đích duy nhất và yêu cầu bảo toàn luồng (flow / 흐름) tại mọi đỉnh. Cạnh có thể có lower/upper bounds.

Đây là mô hình tự nhiên cho:

```text
phân phối cung-cầu
quota tối thiểu/tối đa
lịch phân công với ràng buộc
```

Circulation feasibility thường được reduce về max-flow bằng cách điều chỉnh lower bounds và tạo super nguồn (source / 소스)/sink.

> **Chuyển mạch:** Ở chặng này của **Luồng mạng và ghép cặp hai phía**, **21. Lower Bounds trên cạnh** tiếp nhận điểm tựa từ **20. Circulation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Min-Cost luồng (flow / 흐름)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Lower Bounds trên cạnh

Nếu cạnh yêu cầu:

\[
l(u,v)\le f(u,v)\le c(u,v)
\]

ta có thể gửi trước `l(u,v)`, giảm sức chứa (capacity / 용량) còn lại thành `c-l`, rồi điều chỉnh balance của hai endpoint.

Sau đó thêm super nguồn (source / 소스)/sink để bù các nhu cầu dư/thiếu.

Đây là một kỹ thuật reduction mạnh: biến ràng buộc (constraint / 제약조건) “ít nhất” thành preflow cố định và bài feasibility còn lại.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Luồng mạng và ghép cặp hai phía**, **21. Lower Bounds trên cạnh** xác định đầu vào; **22. Min-Cost luồng (flow / 흐름)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **23. Negative chi phí (cost / 비용) và Potential** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Min-Cost luồng (flow / 흐름)

Nếu mỗi đơn vị luồng (flow / 흐름) trên cạnh có chi phí (cost / 비용), ta cần tối ưu tổng chi phí bên cạnh lượng luồng (flow / 흐름).

Một dạng:

```text
maximize flow trước
trong các max-flow, minimize total cost
```

hoặc gửi chính xác `K` đơn vị với chi phí nhỏ nhất.

Min-Cost Max-Flow thường dùng residual đồ thị (graph / 그래프) với **chi phí cạnh ngược âm** để biểu diễn khả năng hoàn tác quyết định cũ.

Shortest augmenting đường dẫn (path / 경로) với potential/reduced chi phí (cost / 비용) là một cách triển khai phổ biến.

> **Chuyển mạch:** Trong **Luồng mạng và ghép cặp hai phía**, **22. Min-Cost luồng (flow / 흐름)** xác định đầu vào; **23. Negative chi phí (cost / 비용) và Potential** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **24. Assignment bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Negative chi phí (cost / 비용) và Potential

Residual reverse edge của một cạnh chi phí (cost / 비용) `w` có chi phí (cost / 비용) `-w`, vì hoàn tác một đơn vị luồng (flow / 흐름) thu lại chi phí đã trả.

Điều này tạo cạnh âm. Ta có thể dùng Bellman–Ford ban đầu hoặc potential để biến reduced chi phí (cost / 비용) thành không âm rồi chạy Dijkstra trong các vòng sau.

Đây là ví dụ luồng (flow / 흐름) kết nối trực tiếp với shortest-path lý thuyết (theory / 이론).

> **Chuyển mạch:** Ở chặng này của **Luồng mạng và ghép cặp hai phía**, **24. Assignment bài toán (problem / 문제)** tiếp nhận điểm tựa từ **23. Negative chi phí (cost / 비용) và Potential** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. B-Matching và sức chứa (capacity / 용량) > 1** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Assignment bài toán (problem / 문제)

Nếu cần ghép mọi worker với job và mỗi cặp có chi phí (cost / 비용), bài toán assignment có thể giải bằng Hungarian thuật toán (algorithm / 알고리즘) hoặc min-cost luồng (flow / 흐름) tùy cấu trúc.

Maximum matching chỉ tối đa hóa số cặp; nó không tự tối ưu tổng lợi ích.

Phải phân biệt mục tiêu (objective / 목표):

```text
maximum cardinality
maximum weight
minimum cost perfect matching
```

Các bài nhìn giống nhau nhưng cần mô hình khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Luồng mạng và ghép cặp hai phía**, **25. B-Matching và sức chứa (capacity / 용량) > 1** tiếp nhận điểm tựa từ **24. Assignment bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. luồng (flow / 흐름) Decomposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. B-Matching và sức chứa (capacity / 용량) > 1

Nếu một worker có thể nhận nhiều job hoặc một tài nguyên (resource / 자원) có quota `b(v)`, matching chuẩn sức chứa (capacity / 용량) 1 không đủ.

Có thể tăng sức chứa (capacity / 용량) trên cạnh nguồn/đích hoặc dùng b-matching formulation phù hợp.

Đây là ví dụ đơn giản cho thấy matching chỉ là một trường hợp đặc biệt của luồng (flow / 흐름) với sức chứa (capacity / 용량) 1.

> **Chuyển mạch:** Trong **Luồng mạng và ghép cặp hai phía**, **25. B-Matching và sức chứa (capacity / 용량) > 1** xác định đầu vào; **26. luồng (flow / 흐름) Decomposition** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **27. sức chứa (capacity / 용량) Scaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. luồng (flow / 흐름) Decomposition

Một integral luồng (flow / 흐름) có thể phân rã thành tập các đường từ nguồn tới đích và chu trình.

Trong nhiều bài ứng dụng (application / 애플리케이션), giá trị max-flow chưa đủ; ta cần chính các assignment/đường dẫn (path / 경로) cụ thể. Khi đó cần duyệt các cạnh có luồng (flow / 흐름) dương để reconstruct.

Nếu API cần tuyến (route / 경로) cụ thể, đầu ra (output / 출력) ngữ nghĩa (semantics / 의미론) phải được thiết kế ngay từ đầu.

> **Chuyển mạch:** Ở chặng này của **Luồng mạng và ghép cặp hai phía**, **26. luồng (flow / 흐름) Decomposition** xác định đầu vào; **27. sức chứa (capacity / 용량) Scaling** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **28. Push–Relabel** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. sức chứa (capacity / 용량) Scaling

Một số thuật toán tăng hiệu năng bằng cách ưu tiên các residual edge có sức chứa (capacity / 용량) lớn trước, rồi giảm ngưỡng theo lũy thừa của 2.

Ý tưởng **scaling** xuất hiện ở nhiều thuật toán tối ưu hóa: giải bài thô trước ở mức giá trị lớn, sau đó tinh chỉnh.

Không phải hiện thực (implementation / 구현) max-flow nào cũng cần scaling, nhưng đây là mẫu (pattern / 패턴) thiết kế đáng nhận diện.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Luồng mạng và ghép cặp hai phía**, **27. sức chứa (capacity / 용량) Scaling** cho ta quy tắc; **28. Push–Relabel** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **29. Min-Cut trong bài chọn tập** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Push–Relabel

Push–Relabel không tìm augmenting đường dẫn (path / 경로) hoàn chỉnh ở mỗi bước. Nó duy trì một **preflow** cho phép đỉnh trung gian tạm thời có excess, cùng nhãn chiều cao `h(v)`.

Thao tác chính:

```text
push      -> đẩy excess qua admissible edge
relabel   -> tăng height khi không còn admissible edge
```

Mô hình tư duy khác hoàn toàn Ford–Fulkerson nhưng vẫn giải cùng max-flow bài toán (problem / 문제).

Trong một số đồ thị (graph / 그래프) lớn/dày, Push–Relabel rất cạnh tranh.

> **Chuyển mạch:** Trong **Luồng mạng và ghép cặp hai phía**, **28. Push–Relabel** cho ta quy tắc; **29. Min-Cut trong bài chọn tập** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **30. Khi luồng (flow / 흐름) là quá nặng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Min-Cut trong bài chọn tập

Một số bài có chi phí (cost / 비용) chọn/bỏ đỉnh và penalty nếu hai lựa chọn không nhất quán có thể reduce về s-t min-cut.

Mẫu thường gặp:

```text
source edge  -> cost của một lựa chọn
sink edge    -> cost của lựa chọn đối lập
pair edge    -> penalty khi tách hai biến
```

Cut chọn một phía cho mỗi nút (node / 노드) và tổng sức chứa (capacity / 용량) bị cắt chính là mục tiêu (objective / 목표).

Đây là nền tảng của nhiều formulation trong computer vision và năng lượng (energy / 에너지) minimization với điều kiện phù hợp.

> **Chuyển mạch:** Ở chặng này của **Luồng mạng và ghép cặp hai phía**, **29. Min-Cut trong bài chọn tập** xác định đầu vào; **30. Khi luồng (flow / 흐름) là quá nặng** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **31. Độ phức tạp phải gắn với lớp đồ thị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Khi luồng (flow / 흐름) là quá nặng

Không nên dùng max-flow chỉ vì “bài có assignment”.

Nếu chỉ cần matching bipartite, Hopcroft–Karp đơn giản và nhanh hơn. Nếu assignment ma trận (matrix / 행렬) có trọng số đặc biệt, Hungarian có thể phù hợp. Nếu chỉ cần connectivity, DSU/DFS rẻ hơn rất nhiều.

Luồng (flow / 흐름) là công cụ tổng quát; sức mạnh tổng quát thường đi cùng hiện thực (implementation / 구현) và constant factor lớn hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Luồng mạng và ghép cặp hai phía**, **30. Khi luồng (flow / 흐름) là quá nặng** xác định đầu vào; **31. Độ phức tạp phải gắn với lớp đồ thị** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **32. Overflow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Độ phức tạp phải gắn với lớp đồ thị

Một độ phức tạp (complexity / 복잡도) formula không nói hết câu chuyện.

Cần xét:

```text
V, E
sparse hay dense
capacity magnitude
unit capacity hay arbitrary capacity
bipartite hay general
integer hay real
số augmentation thực tế
```

Cùng Dinic có thể rất nhanh trên đơn vị (unit / 단위) mạng (network / 네트워크) nhưng kém hơn một lựa chọn khác trên đồ thị (graph / 그래프) dày hoặc ứng dụng (application / 애플리케이션) đặc biệt.

> **Chuyển mạch:** Trong **Luồng mạng và ghép cặp hai phía**, **31. Độ phức tạp phải gắn với lớp đồ thị** xác định đầu vào; **32. Overflow** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **33. Biểu diễn Residual Edge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Overflow

Tổng luồng (flow / 흐름) có thể vượt 32-bit dù từng sức chứa (capacity / 용량) nhỏ. chi phí (cost / 비용) * luồng (flow / 흐름) còn dễ vượt hơn.

Nên chọn kiểu số dựa trên cận toán học, không theo kiểu của đầu vào (input / 입력) riêng lẻ.

Trong Java thường cần `long`; trong C cần kiểu nguyên đủ rộng và kiểm tra overflow khi nhân/cộng chi phí (cost / 비용).

> **Chuyển mạch:** Ở chặng này của **Luồng mạng và ghép cặp hai phía**, **32. Overflow** xác định đầu vào; **33. Biểu diễn Residual Edge** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **34. Validator cho luồng (flow / 흐름)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Biểu diễn Residual Edge

Một mẫu (pattern / 패턴) phổ biến là mỗi edge lưu chỉ mục (index / 인덱스) của reverse edge:

```text
Edge { to, capacity, rev }
```

Khi đẩy `delta`:

```text
forward.cap -= delta
reverse.cap += delta
```

Bất biến cực kỳ quan trọng:

> forward và reverse edge phải luôn tham chiếu đúng cặp của nhau.

Lỗi reverse-index là một trong những bug hiện thực (implementation / 구현) max-flow phổ biến nhất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Luồng mạng và ghép cặp hai phía**, **33. Biểu diễn Residual Edge** xác định đầu vào; **34. Validator cho luồng (flow / 흐름)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **35. Differential Testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Validator cho luồng (flow / 흐름)

Sau khi thuật toán chạy, có thể kiểm tra:

```text
0 <= flow <= capacity
flow conservation ở mọi đỉnh trung gian
value out of source == value into sink
không còn augmenting path nếu dùng augmenting algorithm
```

Để xác minh optimality mạnh hơn, xây min-cut từ residual reachability và kiểm tra:

\[
flowValue = cutCapacity
\]

Đây là validator rất mạnh vì dùng theorem độc lập với đường chạy cụ thể của thuật toán.

> **Chuyển mạch:** Trong **Luồng mạng và ghép cặp hai phía**, **34. Validator cho luồng (flow / 흐름)** xác định đầu vào; **35. Differential Testing** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **36. Những trường hợp biên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Differential Testing

Với đồ thị (graph / 그래프) nhỏ, có thể:

```text
so Dinic với Edmonds–Karp
so matching-flow với brute-force matching
so min-cut với enumerate mọi partition nhỏ
```

Random đồ thị (graph / 그래프) + oracle chậm là cách rất hiệu quả để phát hiện bug reverse edge, mức (level / 수준) đồ thị (graph / 그래프), ptr hoặc sức chứa (capacity / 용량) cập nhật (update / 업데이트).

> **Chuyển mạch:** Ở chặng này của **Luồng mạng và ghép cặp hai phía**, **36. Những trường hợp biên** tiếp nhận điểm tựa từ **35. Differential Testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Mô hình hóa quan trọng hơn chọn thuật toán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Những trường hợp biên

Cần thử:

```text
s == t theo hợp đồng API
không có đường s-t
parallel edges
self-loop
capacity 0
capacity rất lớn
nhiều min-cut khác nhau
nhiều maximum matching khác nhau
graph disconnected
node splitting với source/sink đặc biệt
```

Parallel edge thường hoàn toàn hợp lệ trong luồng (flow / 흐름); hiện thực (implementation / 구현) adjacency phải giữ từng edge riêng hoặc gộp sức chứa (capacity / 용량) có chủ đích.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Luồng mạng và ghép cặp hai phía**, **37. Mô hình hóa quan trọng hơn chọn thuật toán** tiếp nhận điểm tựa từ **36. Những trường hợp biên** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Mô hình hóa quan trọng hơn chọn thuật toán

Nhiều bug luồng (flow / 흐름) không nằm trong Dinic mà nằm trong đồ thị (graph / 그래프) construction:

```text
capacity đặt sai phía
quên capacity 1 trong matching
source/sink nối sai
lower-bound balance sai dấu
node splitting bỏ sót cạnh
```

Một max-flow hiện thực (implementation / 구현) hoàn hảo trên một mạng (network / 네트워크) mô hình (model / 모델) sai vẫn trả lời sai bài toán.

> **Chuyển mạch:** Trong **Luồng mạng và ghép cặp hai phía**, **Mô hình tư duy** gom các mảnh từ **37. Mô hình hóa quan trọng hơn chọn thuật toán** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> mạng (network / 네트워크) luồng (flow / 흐름) là một ngôn ngữ để mô hình hóa **phân phối tài nguyên dưới các ràng buộc**, còn residual đồ thị (graph / 그래프) là ngôn ngữ của **những thay đổi còn có thể thực hiện trên lời giải hiện tại**.

Khi nhận ra một bài có tính chất “mỗi đối tượng có sức chứa (capacity / 용량)/quota, phải phân phối sao cho bảo toàn và tối ưu tổng lượng/chi phí”, hãy thử nghĩ theo luồng (flow / 흐름). Sau đó hỏi: **bài có cấu trúc đặc biệt để dùng matching/Hungarian/DSU thay vì generic luồng (flow / 흐름) không, cần cardinality hay chi phí (cost / 비용), sức chứa (capacity / 용량) nằm ở cạnh hay đỉnh, và có thể tạo certificate min-cut để kiểm chứng tính tối ưu hay không?**

Xem thêm: [Graph Modeling](./00_graph_modeling_and_representation.md), [Shortest Paths](./02_shortest_paths.md), [Union-Find](./05_union_find.md), [Hard Problems & Reductions](../04_algorithmic_paradigms/09_hard_problems_reductions_and_approximation.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
