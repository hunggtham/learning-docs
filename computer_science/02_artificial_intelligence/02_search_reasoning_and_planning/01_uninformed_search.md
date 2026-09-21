# Tìm kiếm không dùng heuristic: BFS, DFS, UCS và các chiến lược nền tảng

**Tìm kiếm không dùng heuristic (Uninformed Search / 무정보 탐색)** giải bài toán chỉ dựa trên đặc tả bài toán: trạng thái ban đầu, hành động, phép chuyển, mục tiêu và chi phí đường đi. Thuật toán không có ước lượng theo miền để biết trạng thái nào “gần mục tiêu hơn”.

Điều này không làm nhóm thuật toán này trở nên lỗi thời. Chúng là đường cơ sở giúp hiểu rõ đánh đổi giữa tính đầy đủ, tính tối ưu, thời gian và bộ nhớ. Các thuật toán có heuristic như A* chỉ thực sự dễ hiểu khi ta thấy điều gì xảy ra nếu hoàn toàn không có heuristic.

Xem trước: [Không gian trạng thái và tìm kiếm](./00_state_space_and_search.md).

## Một phép trừu tượng chung

Mọi chiến lược đều có biên tìm kiếm, nhưng khác cách lấy nút tiếp theo:

```text
BFS → hàng đợi FIFO
DFS → ngăn xếp LIFO
UCS → hàng đợi ưu tiên theo g(n)
Tìm kiếm giới hạn độ sâu → DFS + giới hạn độ sâu
Đào sâu lặp → lặp lại DFS có giới hạn độ sâu
Tìm kiếm hai chiều → hai phía tìm và gặp nhau
```

Các thuộc tính của thuật toán phụ thuộc vào giả định về hệ số phân nhánh, độ sâu mục tiêu và chi phí cạnh.

## Tìm kiếm theo chiều rộng

**Tìm kiếm theo chiều rộng (Breadth-First Search - BFS / 너비 우선 탐색)** mở rộng nút theo độ sâu tăng dần.

Nếu biên là hàng đợi FIFO:

```pseudo
hàng_đợi ← [bắt_đầu]
đã_thăm ← {bắt_đầu}

while hàng_đợi không rỗng:
    n ← lấy_đầu(hàng_đợi)
    if mục_tiêu(n): return đường_đi(n)

    for s in các_nút_kế(n):
        if s chưa có trong đã_thăm:
            đã_thăm.add(s)
            hàng_đợi.thêm_cuối(s)
```

BFS khám phá toàn bộ trạng thái ở độ sâu 0, sau đó độ sâu 1, độ sâu 2 và tiếp tục như vậy.

### Khi nào BFS tối ưu?

Nếu mọi bước có cùng chi phí, đường có ít bước nhất cũng là đường có chi phí thấp nhất. Khi đó BFS tối ưu.

Nếu chi phí cạnh khác nhau, đường nông hơn có thể đắt hơn đường sâu hơn. Lúc đó BFS không bảo đảm tối ưu theo chi phí.

### Độ phức tạp

Với hệ số phân nhánh `b` và độ sâu của mục tiêu nông nhất `d`, thời gian và bộ nhớ trong trường hợp xấu thường tăng theo cấp số nhân:

\[
O(b^d)
\]

Điểm yếu lớn của BFS là bộ nhớ vì phải giữ gần như toàn bộ biên của một tầng.

## Tìm kiếm theo chiều sâu

**Tìm kiếm theo chiều sâu (Depth-First Search - DFS / 깊이 우선 탐색)** đi sâu vào một nhánh trước khi quay lui.

Có thể triển khai bằng ngăn xếp hoặc đệ quy:

```pseudo
ngăn_xếp ← [bắt_đầu]
đã_thăm ← tập_rỗng()

while ngăn_xếp không rỗng:
    n ← pop(ngăn_xếp)
    if n in đã_thăm: continue
    đã_thăm.add(n)

    if mục_tiêu(n): return đường_đi(n)

    push(các_nút_kế(n))
```

### Điểm mạnh

DFS thường dùng ít bộ nhớ hơn BFS. Nếu độ sâu tối đa là `m`, độ phức tạp không gian thường gần:

\[
O(bm)
\]

trong cách lưu cây tìm kiếm thông thường.

### Điểm yếu

DFS có thể lao rất sâu vào một nhánh sai hoặc vô hạn nếu không kiểm soát chu trình và độ sâu.

Nó không bảo đảm tối ưu. Mục tiêu được tìm thấy đầu tiên phụ thuộc mạnh vào thứ tự sinh nút kế tiếp.

### Khi nào DFS hữu ích?

DFS phù hợp khi bộ nhớ hạn chế, lời giải dự kiến sâu, chỉ cần một lời giải bất kỳ, cần duyệt toàn bộ bằng quay lui hoặc xử lý các bài toán đồ thị như phát hiện chu trình.

## Tìm kiếm giới hạn độ sâu

**Tìm kiếm giới hạn độ sâu (Depth-Limited Search - DLS)** là DFS với giới hạn `ℓ`.

Khi đạt độ sâu `ℓ`, nút không được mở rộng thêm.

Cách này tránh đi sâu vô hạn nhưng có thể bỏ lỡ lời giải nằm sâu hơn giới hạn.

Cần phân biệt ba kết quả:

```text
THÀNH_CÔNG
THẤT_BẠI   → không có lời giải trong phần đã khám phá
CẮT_NGANG  → có thể còn lời giải sâu hơn giới hạn
```

Sự phân biệt này đặc biệt quan trọng cho đào sâu lặp.

## DFS đào sâu lặp

**Tìm kiếm đào sâu lặp (Iterative Deepening Depth-First Search - IDDFS)** chạy DLS với các giới hạn:

```text
0, 1, 2, 3, ...
```

Thoạt nhìn có vẻ lãng phí vì các nút ở tầng trên bị mở rộng nhiều lần. Nhưng trong cây tăng theo cấp số nhân, phần lớn nút nằm ở tầng sâu nhất, nên chi phí lặp lại ở các tầng trên tương đối nhỏ.

Với chi phí mỗi bước bằng nhau, IDDFS kết hợp:

- tính đầy đủ của BFS;
- khả năng tìm mục tiêu nông nhất như BFS;
- mức sử dụng bộ nhớ gần DFS.

Thời gian vẫn xấp xỉ:

\[
O(b^d)
\]

và bộ nhớ khoảng:

\[
O(bd)
\]

trong cách phân tích thông thường.

## Tìm kiếm chi phí đồng nhất

**Tìm kiếm chi phí đồng nhất (Uniform-Cost Search - UCS / 균일 비용 탐색)** luôn mở rộng nút có chi phí đường đi thấp nhất:

\[
g(n)
\]

Có thể xem nó gần với thuật toán Dijkstra từ điểm bắt đầu tới mục tiêu trong ngữ cảnh AI.

```pseudo
biên ← PQ((0,bắt_đầu))
tốt_nhất[bắt_đầu] ← 0

while biên:
    g,n ← lấy_chi_phí_thấp_nhất()

    if g != tốt_nhất[n]: continue
    if mục_tiêu(n): return đường_đi

    for cạnh(n,s,c):
        g_mới ← g + c
        if s chưa_thấy OR g_mới < tốt_nhất[s]:
            tốt_nhất[s] ← g_mới
            push(g_mới,s)
```

### Vì sao thường kiểm tra mục tiêu khi lấy nút ra khỏi hàng đợi?

Một trạng thái mục tiêu có thể được sinh ra lần đầu qua một đường đắt, trong khi một đường rẻ hơn chưa được khám phá.

Khi UCS lấy mục tiêu ra như nút có chi phí nhỏ nhất trên biên, với chi phí cạnh không âm, lúc đó mới có bảo đảm tối ưu.

## BFS là trường hợp đặc biệt của UCS

Nếu mọi cạnh có chi phí bằng 1:

\[
g(n)=depth(n)
\]

thì thứ tự của UCS theo chi phí đường đi tương đương BFS theo độ sâu.

Có thể ghi nhớ:

```text
BFS = UCS khi chi phí mỗi bước đồng nhất
```

## Chi phí cạnh âm

Lập luận tối ưu tiêu chuẩn của UCS/Dijkstra yêu cầu chi phí cạnh không âm.

Nếu tồn tại cạnh âm, một nút tưởng như rẻ nhất ở hiện tại vẫn có thể được cải thiện sau qua đường đi chứa cạnh âm.

Các thuật toán như Bellman–Ford xử lý cạnh âm trong bài toán đường đi ngắn nhất; chu trình âm có thể khiến khái niệm đường ngắn nhất không còn hữu hạn.

Trong thiết kế hàm chi phí AI, phần thưởng hoặc chi phí âm cần được mô hình hóa cẩn thận.

## Kiểm tra chu trình

Trong tìm kiếm cây:

```text
A → B → C → A → ...
```

có thể tạo mở rộng vô hạn.

Kiểm tra chu trình theo đường hiện tại ngăn một trạng thái lặp lại trên cùng đường.

Tập đã duyệt toàn cục mạnh hơn, nhưng với bài toán có trọng số cần lưu chi phí tốt nhất: “đã từng thấy trạng thái” chưa đủ nếu sau đó xuất hiện đường rẻ hơn.

## Trạng thái trùng trong biên

Có hai kiểu triển khai thường gặp:

1. cập nhật trực tiếp phần tử trong hàng đợi ưu tiên;
2. thêm ứng viên mới tốt hơn và bỏ ứng viên cũ khi nó được lấy ra.

Kiểu thứ hai thường đơn giản hơn với thư viện heap thông thường:

```python
if popped_cost != best[state]:
    continue
```

Mô hình tư duy: bảng `best` là nguồn sự thật; heap có thể chứa ứng viên đã cũ.

## Tìm kiếm hai chiều

Nếu trạng thái bắt đầu `S` và mục tiêu chính xác `G` đều đã biết, có thể tìm xuôi từ `S` và ngược từ `G`.

Số nút lý tưởng có thể giảm từ:

\[
O(b^d)
\]

xuống gần:

\[
O(b^{d/2}) + O(b^{d/2})
\]

### Điều kiện thực tế

Tìm kiếm hai chiều cần:

- sinh được trạng thái tiền nhiệm hoặc cạnh ngược;
- kiểm tra giao nhau hiệu quả;
- điều kiện dừng cẩn thận khi có trọng số;
- khả năng giữ hai biên trong bộ nhớ.

Nếu mục tiêu là một điều kiện rộng như “bất kỳ lịch hợp lệ nào”, tìm ngược có thể không đơn giản.

## Thứ tự tìm và quy tắc phá hòa

Ngay cả cùng BFS hoặc UCS, thứ tự sinh nút kế tiếp vẫn ảnh hưởng đường được trả về khi tồn tại nhiều lời giải tối ưu.

A* cũng chịu ảnh hưởng bởi **quy tắc phá hòa (tie-breaking)** khi nhiều nút có cùng điểm ưu tiên.

Nếu đường đi cụ thể cần tái lập, nên dùng thứ tự sinh nút xác định.

## Độ phức tạp theo cây và theo đồ thị

Giáo trình AI thường diễn đạt độ phức tạp bằng `b,d,m`, trong khi lý thuyết đồ thị dùng `|V|,|E|`.

Duyệt BFS trên đồ thị hữu hạn có thể đạt:

\[
O(|V|+|E|)
\]

nếu mỗi đỉnh và cạnh chỉ được xử lý một số lần hằng định.

Thuật toán đường đi ngắn nhất dùng hàng đợi ưu tiên thường có độ phức tạp liên quan tới `|E| log |V|`, tùy cấu trúc heap.

Hai cách ký hiệu tương ứng với hai góc nhìn:

```text
góc nhìn cây tìm kiếm AI → phân nhánh / độ sâu
góc nhìn thuật toán đồ thị → đỉnh / cạnh
```

## Ví dụ: đường đi có trọng số

Giả sử:

```text
S --1--> A --100--> G
 \                    
  --10--> B --10--> C --10--> G
```

BFS thấy `S-A-G` ở độ sâu 2 và trả đường chi phí 101.

UCS mở rộng theo chi phí tích lũy và tìm `S-B-C-G` với chi phí 30.

Vì vậy “ít bước hơn” không đồng nghĩa “rẻ hơn”.

## Bộ nhớ là một tài nguyên thuật toán

BFS thường hết RAM trước khi hết CPU.

Giả sử biên có 10 triệu nút, mỗi nút cần 100 byte thông tin:

```text
≈ 1 GB
```

Trong thực tế chi phí đối tượng có thể còn lớn hơn.

Mã hóa trạng thái gọn, cách lưu nút cha, tìm kiếm trên bộ nhớ ngoài hoặc đào sâu lặp có thể quan trọng hơn việc tối ưu vi mô thao tác mở rộng.

## Đào sâu lặp và các hệ thống suy luận hiện đại

Ý tưởng cấp dần ngân sách độ sâu có dạng tương tự trong hệ thống hiện đại:

```text
thử suy luận nông / đơn giản
nếu chưa đủ → cho phép tìm sâu hơn
```

Không nên gọi mọi “mức suy luận” là IDDFS theo nghĩa thuật toán chính xác, nhưng việc tăng dần ngân sách tính toán là một mẫu thiết kế lặp lại nhiều lần.

## Beam Search: cắt bớt không gian theo điểm số

**Beam Search** thường được học trong phần giải mã chuỗi, nhưng là đối chiếu hữu ích với tìm kiếm đầy đủ.

Ở mỗi độ sâu, chỉ giữ `k` ứng viên có điểm cao nhất:

```text
tất cả khả năng tăng theo cấp số nhân
       ↓ cắt bớt
chỉ giữ beam width = k
```

Beam Search tiết kiệm thời gian và bộ nhớ nhưng không đầy đủ và không bảo đảm tối ưu toàn cục.

Dịch máy và sinh chuỗi từng sử dụng chiến lược này rất rộng rãi.

## Tìm kiếm dưới giới hạn tài nguyên

Hệ thống thực tế có giới hạn:

- thời gian;
- bộ nhớ;
- chi phí API/công cụ;
- ngân sách token.

Một thuật toán tối ưu về lý thuyết có thể hoàn toàn không dùng được trong thực tế.

Thuật toán bị giới hạn tài nguyên chấp nhận đánh đổi chất lượng lời giải để giảm tính toán. Ý tưởng này quay lại trong thuật toán anytime, Beam Search, Monte Carlo Tree Search và lập kế hoạch tác nhân LLM.

## Thuật toán anytime

**Thuật toán anytime** có thể trả lời giải tốt nhất hiện tại nếu bị dừng, và chất lượng tiếp tục cải thiện nếu được cấp thêm thời gian.

Đây là thuộc tính hữu ích khi ngân sách tính toán không chắc chắn.

Weighted A* và nhiều phương pháp cải thiện lặp có các biến thể anytime.

## Chọn chiến lược tìm kiếm không heuristic

| Tình huống | Trực giác lựa chọn |
|---|---|
| Chi phí bằng nhau, lời giải nông | BFS |
| Bộ nhớ hạn chế, chỉ cần một lời giải | DFS / DLS |
| Không biết độ sâu mục tiêu, chi phí bằng nhau | IDDFS |
| Chi phí không âm khác nhau | UCS |
| Biết chính xác đầu và đích, đồ thị đảo được | Tìm kiếm hai chiều |

Bảng này chỉ là điểm khởi đầu. Vẫn cần phân tích kích thước đồ thị, chu trình, ràng buộc và cách biểu diễn bộ nhớ thực tế.

## Mô hình tư duy (mental model)

```text
BFS   = ưu tiên độ sâu nhỏ
DFS   = đi sâu một nhánh, tiết kiệm bộ nhớ
DLS   = DFS có chân trời độ sâu
IDDFS = bảo đảm theo độ sâu kiểu BFS với bộ nhớ gần DFS
UCS   = tối ưu chi phí đường đi tích lũy
Tìm hai chiều = giảm độ sâu hiệu dụng bằng cách gặp ở giữa
```

## Các hiểu lầm thường gặp

### “BFS luôn tìm đường ngắn nhất”

BFS chỉ tối thiểu số cạnh; nó tối ưu theo chi phí khi mọi bước có chi phí bằng nhau.

### “DFS nhanh hơn BFS”

Không có quy luật chung như vậy. DFS có thứ tự khám phá khác và ít tốn bộ nhớ hơn, nhưng có thể đi rất lâu vào nhánh sai.

### “Tập đã thăm chỉ là tối ưu hiệu năng”

Trong đồ thị có chu trình, phát hiện trạng thái trùng có thể quyết định cả khả năng dừng lẫn tính đúng đắn.

### “UCS thấy mục tiêu lần đầu là đủ”

Mục tiêu cần được xác nhận khi được lấy ra theo logic chi phí thấp nhất; việc được sinh ra đầu tiên chưa bảo đảm tối ưu.

## Liên kết kiến thức

Tìm kiếm không dùng heuristic là đường cơ sở để thấy heuristic mang lại điều gì. [Tìm kiếm heuristic](./02_heuristic_search.md) sẽ thêm ước lượng `h(n)` để tập trung mở rộng, còn phần lập kế hoạch sẽ bổ sung điều kiện trước và hiệu ứng của hành động.

Khi chọn thuật toán tìm kiếm, hãy bắt đầu bằng các thuộc tính của đồ thị: **hệ số phân nhánh, độ sâu, chi phí cạnh, chu trình, ngân sách bộ nhớ và việc mục tiêu/phép chuyển ngược có được biết hay không**.