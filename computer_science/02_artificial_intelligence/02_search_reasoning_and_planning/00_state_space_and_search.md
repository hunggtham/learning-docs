# Không gian trạng thái và tìm kiếm trong Trí tuệ nhân tạo

**Tìm kiếm (search / 탐색)** là một trong những ý tưởng lâu đời và bền vững nhất của Trí tuệ nhân tạo. Trước khi học máy trở thành hướng chủ đạo của AI hiện đại, rất nhiều bài toán trí tuệ đã được nhìn theo cấu trúc: **ta đang ở một trạng thái, có một tập hành động, mỗi hành động dẫn sang trạng thái khác; làm thế nào tìm được chuỗi hành động đưa ta tới mục tiêu?**

Mô hình tư duy này vẫn xuất hiện trong tìm đường, giải câu đố, chơi game, lập kế hoạch, giải ràng buộc, chứng minh định lý, giải mã, truy xuất và hệ thống tác nhân. Tìm kiếm không đối lập với học máy; mô hình đã học có thể cung cấp hàm ước lượng, giá trị trạng thái hoặc gợi ý ứng viên để quá trình tìm kiếm hiệu quả hơn.

Xem nền tảng biểu diễn: [Biểu diễn bài toán](../00_foundations/03_problem_representation.md).

## Từ thế giới thật tới không gian trạng thái

Giả sử cần robot đi từ phòng A tới phòng D. Thế giới thực có vô số chi tiết như nhiệt độ, màu tường, tiếng ồn, pin và đồ nội thất. Thuật toán tìm kiếm không thể xử lý toàn bộ thực tế. Ta cần một **mức trừu tượng (abstraction)** phù hợp.

Một cách đặc tả bài toán thường gồm:

- **trạng thái ban đầu (initial state / 초기 상태)**;
- **không gian trạng thái (state space / 상태 공간)**;
- **hành động hoặc phép toán (actions/operators)**;
- **mô hình chuyển trạng thái (transition model)**;
- **kiểm tra mục tiêu (goal test)**;
- **chi phí đường đi (path cost)** khi các hành động có chi phí khác nhau.

Ví dụ bài toán bản đồ:

```text
trạng thái       = vị trí hiện tại
trạng thái đầu   = Seoul Station
hành động        = chọn một con đường khả dụng
chuyển trạng thái= di chuyển tới vị trí lân cận
mục tiêu         = Gangnam Station
chi phí          = thời gian di chuyển
```

Ngay lập tức có thể thấy cách biểu diễn quyết định bài toán. Nếu chi phí là khoảng cách, lời giải có thể khác khi chi phí là thời gian di chuyển kỳ vọng.

## Trạng thái không nhất thiết bằng quan sát

Trong môi trường quan sát đầy đủ, quan sát hiện tại có thể đủ để xác định trạng thái.

Trong môi trường quan sát một phần, quan sát chỉ cung cấp một phần thông tin. Tác nhân có thể duy trì **trạng thái niềm tin (belief state)**, tức phân phối hoặc tập các trạng thái thế giới có thể xảy ra.

Ví dụ robot không biết chính xác vị trí vì cảm biến có nhiễu. Lúc này tìm kiếm hoặc lập kế hoạch không chỉ diễn ra trên trạng thái vật lý mà có thể diễn ra trên không gian trạng thái niềm tin.

Điều này nối tìm kiếm với xác suất và POMDP.

## Đồ thị và cây

Bài toán không gian trạng thái thường được biểu diễn thành đồ thị:

\[
G=(V,E)
\]

`V` là các trạng thái, `E` là các phép chuyển hoặc hành động.

Thuật toán tìm kiếm thường xây một **cây tìm kiếm (search tree)** bắt đầu từ trạng thái ban đầu. Một trạng thái trong đồ thị thế giới có thể xuất hiện nhiều lần trong cây qua những đường đi khác nhau.

Phân biệt này rất quan trọng:

```text
đồ thị trạng thái của bài toán
    ≠
cây tìm kiếm do thuật toán sinh ra
```

Nếu không phát hiện trạng thái lặp, thuật toán có thể lặp vô hạn trên đồ thị có chu trình.

## Nút tìm kiếm khác trạng thái

Một **trạng thái (state)** mô tả cấu hình của bài toán.

Một **nút tìm kiếm (search node)** thường chứa thêm:

```text
trạng thái
nút cha
hành động dẫn tới nút
chi phí đường đi g(n)
độ sâu
thông tin phụ
```

Hai nút có thể biểu diễn cùng một trạng thái nhưng đạt tới nó bằng những đường khác nhau. Thuật toán tìm kiếm trên đồ thị thường lưu tập đã duyệt hoặc chi phí tốt nhất để tránh mở rộng dư thừa và so sánh các đường đi.

## Biên tìm kiếm

**Biên tìm kiếm (frontier / 프런티어)** là tập các nút đã được phát hiện nhưng chưa được mở rộng.

Các thuật toán tìm kiếm khác nhau chủ yếu ở quy tắc chọn nút tiếp theo từ biên:

```text
BFS    → nút nông nhất trước
DFS    → nút sâu nhất trước
UCS    → chi phí đường đi g(n) nhỏ nhất
Greedy → heuristic h(n) nhỏ nhất
A*     → g(n) + h(n) nhỏ nhất
```

Một khuôn chung:

```pseudo
biên ← {nút ban đầu}
while biên không rỗng:
    nút ← chọn(biên)
    if mục_tiêu(nút.trạng_thái): return lời_giải
    mở_rộng(nút)
    cập_nhật(biên)
return thất_bại
```

Quy tắc `chọn` và cách xử lý trạng thái trùng tạo ra hành vi khác nhau của từng thuật toán.

## Mở rộng nút

Mở rộng một nút nghĩa là áp dụng các hành động khả dụng để sinh các trạng thái kế tiếp.

Nếu **hệ số phân nhánh (branching factor)** trung bình là `b`, và độ sâu lời giải là `d`, số nút có thể tăng khoảng:

\[
1+b+b^2+\cdots+b^d
\]

xấp xỉ:

\[
O(b^d)
\]

Đây là **bùng nổ tổ hợp (combinatorial explosion)**.

Bài toán tìm kiếm trở nên khó không phải vì mỗi hành động riêng lẻ phức tạp, mà vì số chuỗi hành động có thể tăng theo cấp số nhân.

## Hệ số phân nhánh

Hệ số phân nhánh `b` là số trạng thái kế tiếp trung bình của mỗi trạng thái.

Nếu `b=10`:

```text
độ sâu 1:      10
độ sâu 2:     100
độ sâu 3:   1,000
độ sâu 6: 1,000,000
```

Chỉ tăng vài bước đã làm không gian tìm kiếm khổng lồ.

Vì vậy AI cần heuristic, cắt tỉa, trừu tượng hóa và mô hình học để tránh khám phá mọi khả năng.

## Kiểm tra mục tiêu

Kiểm tra mục tiêu xác định một trạng thái có thỏa yêu cầu hay không.

Một lỗi phổ biến là mô tả mục tiêu quá cụ thể. Ví dụ trong lập lịch, mục tiêu có thể chỉ cần “mọi nhiệm vụ được phân công hợp lệ”, không nhất thiết phải đạt đúng một lịch duy nhất.

Tập mục tiêu rộng hơn có thể làm bài toán tìm kiếm dễ hơn.

## Chi phí đường đi

Chi phí đường đi thường có tính cộng:

\[
g(n)=\sum_{e\in path}c(e)
\]

Nhưng mục tiêu thực tế không phải lúc nào cũng cộng đơn giản. Rủi ro, độ trễ lớn nhất, ràng buộc tài nguyên hoặc chi phí đa mục tiêu có thể yêu cầu trạng thái phong phú hơn hoặc thuật toán khác.

Nếu chi phí hành động có thể âm, nhiều giả định của thuật toán đường đi ngắn nhất tiêu chuẩn không còn đúng.

## Lời giải và lời giải tối ưu

Một **lời giải (solution)** là đường đi hoặc chuỗi hành động từ trạng thái ban đầu tới mục tiêu.

Một **lời giải tối ưu (optimal solution)** là lời giải giảm chi phí đường đi theo hàm mục tiêu đã chọn.

Tính tối ưu luôn tương đối với cách biểu diễn và hàm chi phí. “Đường tốt nhất” theo khoảng cách có thể không tốt nhất theo thời gian, phí đường, an toàn hoặc năng lượng.

## Tính đầy đủ

Thuật toán tìm kiếm có **tính đầy đủ (completeness / 완전성)** nếu bảo đảm tìm được lời giải khi lời giải tồn tại dưới những giả định đã nêu.

Đầy đủ về lý thuyết không có nghĩa khả thi trong thực tế. Một thuật toán có thể bảo đảm tìm ra lời giải nhưng cần thời gian hoặc bộ nhớ khổng lồ.

## Tính tối ưu

Thuật toán có **tính tối ưu (optimality / 최적성)** nếu lời giải trả về có chi phí nhỏ nhất dưới các giả định phù hợp.

BFS chỉ tối ưu khi chi phí mỗi bước bằng nhau. Uniform-Cost Search tối ưu với chi phí không âm dưới những điều kiện phù hợp.

## Độ phức tạp thời gian và không gian

Khi đánh giá thuật toán tìm kiếm, thường cần xem:

- tính đầy đủ;
- tính tối ưu;
- độ phức tạp thời gian;
- độ phức tạp không gian.

Bộ nhớ thường là nút thắt lớn. BFS có thể mở rộng số nút vẫn chấp nhận được nhưng phải lưu một biên rất lớn.

DFS dùng ít bộ nhớ hơn nhưng có thể đi sâu rất lâu vào hướng sai.

Đánh đổi này quay lại trong beam search, lập kế hoạch và tìm kiếm cây.

## Tìm kiếm trên cây và tìm kiếm trên đồ thị

Tìm kiếm trên cây không nhớ trạng thái đã ghé, nên có thể sinh lại cùng một trạng thái nhiều lần.

Tìm kiếm trên đồ thị giữ tập đã duyệt hoặc bảng chi phí tốt nhất.

Một mẫu đơn giản:

```pseudo
biên ← hàng_đợi_ưu_tiên(nút_ban_đầu)
chi_phí_tốt_nhất[ban_đầu] ← 0

while biên:
    n ← pop(biên)
    if mục_tiêu(n): return đường_đi(n)

    for kế_tiếp in mở_rộng(n):
        chi_phí_mới ← g(n) + chi_phí_bước
        if kế_tiếp chưa_seen OR chi_phí_mới < chi_phí_tốt_nhất[kế_tiếp]:
            chi_phí_tốt_nhất[kế_tiếp] ← chi_phí_mới
            push_or_update(kế_tiếp)
```

Chi tiết về nút cũ trong hàng đợi hoặc thao tác giảm khóa phụ thuộc cách triển khai.

## Phát hiện trạng thái trùng

Băm và so sánh trạng thái là vấn đề kỹ thuật cốt lõi.

Nếu trạng thái có thể bị thay đổi hoặc phép so sánh sai, tập đã duyệt hoạt động sai.

Trong câu đố, biểu diễn chuẩn hóa giúp phát hiện trùng. Trong lập kế hoạch ký hiệu, trạng thái có thể là tập mệnh đề. Trong trò chơi bàn cờ, **Zobrist hashing** là kỹ thuật phổ biến để băm trạng thái bàn cờ.

## Hướng tìm kiếm

Không phải lúc nào cũng cần tìm từ điểm bắt đầu tới mục tiêu.

**Tìm kiếm ngược (backward search)** bắt đầu từ mục tiêu và tìm các trạng thái tiền nhiệm. Nếu mục tiêu gọn nhưng trạng thái đầu có hệ số phân nhánh lớn, hướng ngược có thể hiệu quả hơn.

**Tìm kiếm hai chiều (bidirectional search)** tìm đồng thời từ hai phía và gặp nhau ở giữa. Với hệ số phân nhánh `b` và độ sâu `d`, trong trường hợp lý tưởng độ phức tạp có thể giảm từ `b^d` xuống khoảng:

\[
2b^{d/2}
\]

nhưng cần phép chuyển ngược hiệu quả và cơ chế phát hiện điểm gặp.

## Trừu tượng hóa

Tìm kiếm trực tiếp trên trạng thái thô có thể quá lớn. Ta có thể xây không gian trạng thái trừu tượng, bỏ bớt chi tiết không liên quan.

Ví dụ lập kế hoạch đường đi:

```text
tìm ở mức từng con phố   → rất nhiều nút
tìm trên đồ thị cao tốc   → ít nút hơn
```

Lập kế hoạch phân cấp có thể tìm lời giải thô trước rồi tinh chỉnh sau.

Trừu tượng hóa là một dạng thiết kế biểu diễn.

## Tìm kiếm và quy hoạch động

Tìm kiếm khám phá trạng thái khi cần. **Quy hoạch động (Dynamic Programming)** thường giải các bài toán con lặp lại bằng cách lưu kết quả và dùng quan hệ truy hồi.

Ghi nhớ kết quả (memoization) biến đệ quy dạng cây thành tính toán gần với đồ thị khi các bài toán con lặp lại.

A* với bảng chi phí tốt nhất, thuật toán đường đi ngắn nhất và phương trình Bellman đều nằm gần ranh giới giữa tìm kiếm và quy hoạch động.

## Tìm kiếm và tối ưu hóa

Tối ưu hóa liên tục tìm trong không gian tham số bằng gradient hoặc các phương pháp khác. Tìm kiếm cổ điển thường hoạt động trên không gian tổ hợp rời rạc.

Liên hệ tư duy:

```text
Tìm kiếm rời rạc      → chọn trạng thái / hành động
Tối ưu hóa liên tục   → tìm giá trị tham số
```

Hệ thống AI lai có thể dùng cả hai: mạng nơ-ron được tối ưu bằng gradient cung cấp heuristic cho tìm kiếm cây.

Các hệ thống kiểu AlphaGo là ví dụ nổi tiếng của việc kết hợp chính sách/giá trị đã học với tìm kiếm cây.

## Tìm kiếm và suy luận

Suy luận xác suất cũng có thể được nhìn như phép cộng hoặc cực đại trên các cấu hình ẩn.

Giải mã Viterbi tìm chuỗi có xác suất cao nhất bằng quy hoạch động.

Beam search xấp xỉ việc tìm kiếm chuỗi trong không gian có hệ số phân nhánh cực lớn.

Giải mã LLM cũng là bài toán tìm kiếm/lấy mẫu trên chuỗi token, dù greedy hay top-p thường không được gọi là tìm kiếm trạng thái cổ điển theo đúng cùng hình thức.

## Tìm kiếm và suy luận bằng LLM

Hệ thống hiện đại có thể sinh nhiều ứng viên suy luận hoặc hành động rồi đánh giá và lựa chọn. Các cách kiểu cây suy nghĩ, lập kế hoạch công cụ và tìm kiếm của tác nhân tái sử dụng một ý tưởng cũ:

```text
trạng thái / ngữ cảnh
    ↓
đề xuất hành động
    ↓
đánh giá ứng viên
    ↓
mở rộng các nhánh hứa hẹn
```

LLM thay thế một số thành phần viết tay bằng mô hình đề xuất hoặc đánh giá đã học, nhưng bài toán bùng nổ tổ hợp vẫn còn nguyên.

## Chân trời tìm kiếm

Nhiệm vụ dài nhiều bước có cả hệ số phân nhánh và độ sâu lớn. Ngay cả mô hình cục bộ mạnh cũng có thể thất bại vì lỗi tích lũy.

Nếu mỗi bước có xác suất thành công `p`, một xấp xỉ độc lập đơn giản cho `d` bước là:

\[
p^d
\]

cho thấy độ tin cậy giảm nhanh theo chiều dài nhiệm vụ.

Quan hệ thực tế phức tạp hơn, nhưng trực giác này giải thích vì sao lập kế hoạch, xác minh, lập kế hoạch lại và phản hồi công cụ quan trọng trong tác nhân.

## Tìm kiếm trực tuyến

Tìm kiếm cổ điển thường giả định mô hình chuyển trạng thái đã biết trước khi hành động.

Trong môi trường quá lớn hoặc chưa biết đầy đủ, tác nhân có thể xen kẽ tìm kiếm với hành động:

```text
quan sát → lập kế hoạch một phần → hành động → quan sát trạng thái mới → lập kế hoạch lại
```

Robotics, game và tác nhân LLM thường hoạt động theo cách này.

Khi đó hệ thống phải tính cả chi phí khám phá và sự bất định của môi trường.

## Không gian tìm kiếm và không gian lời giải

Chất lượng thuật toán không chỉ phụ thuộc tốc độ. Cách biểu diễn có thể thu nhỏ mạnh không gian cần tìm.

Ví dụ Sudoku với 81 ô, mỗi ô có 9 khả năng gợi ý tới `9^81` cấu hình thô. **Lan truyền ràng buộc (constraint propagation)** có thể loại bỏ phần lớn khả năng trước khi cần phân nhánh.

Do đó “tối ưu tìm kiếm” tốt nhất đôi khi là cải thiện biểu diễn hoặc quy tắc suy luận, chứ không phải tăng tốc hàng đợi.

## Mô hình tư duy (mental model)

```text
Trạng thái     = đủ thông tin để tiếp tục giải
Hành động      = phép biến đổi trạng thái
Chuyển trạng thái = hành động thay đổi thế giới/trạng thái thế nào
Mục tiêu       = điều kiện chấp nhận được
Chi phí        = mục tiêu tích lũy trên đường đi
Biên tìm kiếm  = các khả năng đã phát hiện nhưng chưa mở rộng
Tìm kiếm       = chính sách chọn khả năng nào mở rộng tiếp
Heuristic      = tri thức giúp ưu tiên khả năng hứa hẹn
```

## Các hiểu lầm thường gặp

### “Tìm kiếm trong AI chỉ là tìm văn bản hoặc cơ sở dữ liệu”

Trong AI, tìm kiếm rộng hơn nhiều: tìm đường, chuỗi hành động, phép gán, chứng minh hoặc chiến lược trong không gian khả năng.

### “Trạng thái càng chi tiết càng tốt”

Quá nhiều chi tiết không liên quan làm không gian trạng thái lớn hơn. Trạng thái cần đủ thông tin nhưng không nên dư thừa quá mức.

### “Thuật toán đầy đủ luôn tốt hơn thuật toán không đầy đủ”

Hệ thống thực tế có giới hạn thời gian và bộ nhớ. Beam search cố ý không đầy đủ nhưng rất hữu ích trong không gian lớn.

### “Học máy thay thế tìm kiếm”

Mô hình học thường hướng dẫn tìm kiếm, ước lượng giá trị, sinh ứng viên hoặc cắt nhánh. Tìm kiếm và học bổ sung cho nhau.

## Liên kết kiến thức

Tìm kiếm trên không gian trạng thái nối trực tiếp từ [Tác nhân và môi trường](../00_foundations/02_intelligence_agents_and_environments.md) và [Biểu diễn bài toán](../00_foundations/03_problem_representation.md) sang BFS/DFS/UCS, tìm kiếm heuristic, lập kế hoạch và trò chơi.

Xem tiếp: [Tìm kiếm không dùng heuristic](./01_uninformed_search.md) và [Tìm kiếm heuristic](./02_heuristic_search.md).