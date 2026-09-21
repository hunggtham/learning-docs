# Tìm kiếm heuristic: Greedy Best-First và A*

Tìm kiếm không heuristic biết trạng thái hiện tại, các hành động và chi phí đã đi, nhưng không biết hướng nào có vẻ gần mục tiêu hơn. Khi không gian trạng thái lớn, cách đó quá đắt. **Tìm kiếm heuristic (Heuristic Search / 휴리스틱 탐색)** thêm một hàm ước lượng `h(n)` nhằm trả lời:

> Từ nút `n`, ước tính còn bao nhiêu chi phí nữa để tới mục tiêu?

Heuristic không cần hoàn hảo. Chỉ cần tương quan đủ tốt với độ khó còn lại, nó có thể giảm mạnh số nút phải mở rộng. Nhưng heuristic cũng đưa thêm tri thức hoặc giả định vào quá trình tìm kiếm, nên chất lượng và các bảo đảm tính đúng phụ thuộc vào thuộc tính của `h`.

Xem trước: [Tìm kiếm không dùng heuristic](./01_uninformed_search.md).

## Hàm heuristic

Heuristic có thể viết:

\[
h(n)\approx h^*(n)
\]

trong đó `h*(n)` là chi phí tối ưu thật từ `n` tới mục tiêu.

Ví dụ lập kế hoạch đường đi:

```text
h(n) = khoảng cách đường thẳng từ n tới đích
```

Khoảng cách đường thực tế thường lớn hơn hoặc bằng khoảng cách đường thẳng, nên trong một số mô hình chi phí, đây có thể là cận dưới phù hợp.

Trong câu đố, tổng khoảng cách Manhattan của các ô tới vị trí đích là một heuristic quen thuộc.

Có thể xem heuristic là tri thức miền được nén thành một giá trị vô hướng dùng để hướng dẫn tìm kiếm.

## Greedy Best-First Search

**Greedy Best-First Search** chọn nút có:

\[
f(n)=h(n)
\]

nhỏ nhất.

Nó bỏ qua chi phí đã trả `g(n)`.

Mô hình tư duy:

```text
“trạng thái nào trông gần mục tiêu nhất thì ưu tiên trước”
```

Cách này có thể rất nhanh nếu heuristic tốt nhưng cũng dễ bị đánh lừa.

## Ví dụ Greedy thất bại

Giả sử:

```text
S → A → vùng có chi phí rất lớn → G
 \ 
  → B → C → G
```

Heuristic đánh giá `A` rất gần mục tiêu theo khoảng cách hình học nhưng đường thực tế từ `A` bị chặn hoặc rất đắt.

Greedy vẫn ưu tiên `h` thấp dù chi phí đường đi đang tăng mạnh.

Vì bỏ qua `g(n)`, Greedy không bảo đảm tối ưu và cách triển khai trên đồ thị cũng cần xử lý cẩn thận nếu muốn bảo đảm tính đầy đủ.

## A*: kết hợp chi phí đã trả và ước lượng tương lai

A* dùng:

\[
f(n)=g(n)+h(n)
\]

trong đó:

- `g(n)` = chi phí thật từ trạng thái bắt đầu tới `n`;
- `h(n)` = chi phí còn lại được ước lượng;
- `f(n)` = tổng chi phí lời giải được ước lượng nếu đi qua `n`.

A* cân bằng hai câu hỏi:

```text
đã trả bao nhiêu chi phí?
        +
ước tính còn bao nhiêu chi phí?
```

Nếu `h(n)=0` với mọi nút, A* trở thành Uniform-Cost Search.

Nếu bỏ `g(n)`, hành vi trở nên gần Greedy Best-First Search.

## Heuristic chấp nhận được

Heuristic **chấp nhận được (admissible heuristic / 허용적 휴리스틱)** nếu không bao giờ ước lượng lớn hơn chi phí tối ưu thật còn lại:

\[
0\le h(n)\le h^*(n)
\]

Nó mang tính “lạc quan”.

Vì không thổi phồng chi phí còn lại, A* trên cây có bảo đảm tối ưu dưới các giả định chuẩn.

Thông thường cũng yêu cầu:

\[
h(goal)=0
\]

vì chi phí còn lại tại mục tiêu là 0.

## Heuristic nhất quán

Heuristic **nhất quán (consistent / monotone / 일관적 휴리스틱)** nếu với mọi chuyển trạng thái `n→n'` có chi phí `c`:

\[
h(n)\le c(n,n')+h(n')
\]

Điều này giống bất đẳng thức tam giác.

Từ đó:

\[
g(n)+h(n)\le g(n)+c(n,n')+h(n')
\]

nên:

\[
f(n)\le f(n')
\]

trên một đường đi.

Tính nhất quán làm `f` không giảm dọc đường và giúp A* trên đồ thị chốt nút sạch hơn mà thường không phải mở lại nút.

Dưới các giả định mục tiêu phù hợp, nhất quán suy ra chấp nhận được; chiều ngược lại không luôn đúng.

## Trực giác vì sao A* tối ưu

Giả sử chi phí lời giải tối ưu là `C*`.

Với mọi nút `n` trên đường tối ưu:

\[
f(n)=g(n)+h(n)\le g(n)+h^*(n)=C^*
\]

Một mục tiêu không tối ưu `G'` có:

\[
f(G')=g(G')>C^*
\]

vì `h(goal)=0`.

A* luôn mở rộng nút có `f` nhỏ nhất. Khi vẫn còn nút trên đường tối ưu có `f≤C*`, mục tiêu tệ hơn không thể được ưu tiên trước dưới các giả định chuẩn.

Chứng minh đầy đủ còn phụ thuộc chi tiết tìm kiếm cây hay đồ thị, nhưng đây là trực giác trung tâm.

## Heuristic “tốt hơn” nghĩa là gì?

Nếu `h_2(n)≥h_1(n)` với mọi `n` và cả hai đều chấp nhận được, `h_2` được gọi là **chi phối (dominates)** `h_1`.

Một cận dưới gần chi phí thật hơn thường giúp A* mở rộng ít nút hơn.

Hai trường hợp cực đoan:

```text
h(n)=0        → gần UCS, hầu như không có hướng dẫn
h(n)=h*(n)    → heuristic hoàn hảo
```

Heuristic hoàn hảo biết chính xác chi phí tối ưu còn lại, tức gần như đã giải phần lớn bài toán. Tuy nhiên tính heuristic cũng có chi phí, nên thực tế phải cân bằng:

```text
độ chính xác heuristic ↔ chi phí tính heuristic
```

## Suy ra heuristic bằng bài toán nới lỏng

Một phương pháp mạnh là **nới lỏng ràng buộc (relax constraints)**.

Nếu giải một bài toán dễ hơn mà chi phí tối ưu của nó là cận dưới cho bài toán gốc, kết quả có thể trở thành heuristic chấp nhận được.

Ví dụ 8-puzzle:

- bài toán gốc: một ô chỉ di chuyển vào vị trí trống lân cận;
- bài toán nới lỏng: mỗi ô được di chuyển độc lập;
- từ đó có thể suy ra ước lượng kiểu khoảng cách Manhattan.

Nguyên lý tổng quát:

> **Bỏ bớt ràng buộc → bài toán dễ hơn → cận dưới lạc quan.**

Điều này nối thiết kế heuristic với kỹ thuật nới lỏng trong tối ưu hóa.

## Cơ sở dữ liệu mẫu trạng thái

**Pattern Database (PDB)** tính trước khoảng cách chính xác cho một phần hoặc một phép trừu tượng của không gian trạng thái.

Khi chạy:

\[
h(n)=distance\_in\_abstract\_space(n)
\]

Nếu phép trừu tượng nới lỏng bài toán gốc đúng cách, heuristic vẫn chấp nhận được.

PDB đánh đổi bộ nhớ và chi phí tiền tính toán để tăng tốc quá trình tìm kiếm sau đó.

Có thể xem đây là một ví dụ sớm của việc lưu sẵn ước lượng giá trị trước thời đại heuristic nơ-ron.

## Kết hợp nhiều heuristic

Nếu `h1` và `h2` đều chấp nhận được thì:

\[
h(n)=\max(h_1(n),h_2(n))
\]

vẫn chấp nhận được và ít nhất không yếu hơn từng heuristic riêng lẻ.

Ngược lại, `h1+h2` không tự động chấp nhận được vì có thể đếm hai lần cùng một phần chi phí, trừ khi hai heuristic có tính cộng theo cách phân chia chi phí phù hợp.

## Weighted A*

**Weighted A*** dùng:

\[
f(n)=g(n)+w h(n),\quad w>1
\]

để ưu tiên heuristic mạnh hơn.

Nó thường mở rộng ít nút hơn và chạy nhanh hơn nhưng đánh đổi tính tối ưu chính xác. Dưới một số giả định có thể suy ra giới hạn mức kém tối ưu.

Đây là ví dụ thực tế của đánh đổi giữa chất lượng lời giải và chi phí tính toán.

## Tìm kiếm kiểu anytime

Các biến thể **anytime** cố tìm một lời giải nhanh trước, sau đó dùng thêm thời gian để cải thiện chất lượng hoặc cận tối ưu.

Ví dụ, Anytime Repairing A* (ARA*) có thể giảm dần trọng số heuristic theo thời gian.

Cách này hữu ích trong robotics và lập kế hoạch khi ngân sách tính toán thay đổi.

## Vấn đề bộ nhớ của A*

A* có thể tiết kiệm thời gian nhưng dùng rất nhiều bộ nhớ vì phải giữ biên và tập trạng thái đã khám phá.

Một số biến thể gồm:

- Iterative Deepening A* (IDA*);
- Recursive Best-First Search (RBFS);
- Simplified Memory-Bounded A* (SMA*).

Chúng đánh đổi việc tính lại hoặc một số bảo đảm để giảm bộ nhớ.

## IDA*

IDA* dùng DFS theo các ngưỡng của `f=g+h` thay vì độ sâu.

Chạy DFS với ngưỡng `T`; nếu chưa có lời giải, ngưỡng tiếp theo thường là giá trị `f` nhỏ nhất đã vượt `T`.

Bộ nhớ gần DFS nhưng nhiều nút có thể bị mở rộng lại nhiều lần.

Nó phù hợp khi bộ nhớ là nút thắt và heuristic đủ mạnh.

## Beam Search

**Beam Search** chỉ giữ `k` ứng viên tốt nhất ở mỗi độ sâu hoặc bước theo một điểm số.

Nó không phải A* và nhìn chung:

- không đầy đủ;
- không tối ưu;
- bộ nhớ bị giới hạn gần theo độ rộng beam.

Mô hình chuỗi sử dụng Beam Search vì không gian từ vựng phân nhánh quá lớn và tìm kiếm chính xác là bất khả thi.

Điểm beam thường dựa trên log-xác suất và chuẩn hóa độ dài, không phải `g+h` cùng heuristic chấp nhận được như A* cổ điển.

## Độ chính xác heuristic và hiệu chuẩn

Heuristic không nhất thiết là xác suất; nó ước lượng chi phí hoặc giá trị.

Với các bảo đảm của A*, thuộc tính **cận dưới** quan trọng hơn hiệu chuẩn thống kê.

Heuristic học bằng mạng nơ-ron có thể chính xác trung bình nhưng thỉnh thoảng ước lượng quá cao, từ đó phá vỡ tính chấp nhận được nghiêm ngặt.

Hệ thống tìm kiếm học được trong thực tế thường chấp nhận đánh đổi này để tăng tốc.

## Heuristic đã học

Có thể huấn luyện mô hình:

\[
h_\theta(s)\approx cost\_to\_goal(s)
\]

từ các ví dụ đã được giải.

Lợi ích:

- nắm bắt cấu trúc miền phức tạp;
- suy luận nhanh sau huấn luyện;
- có thể khái quát hóa giữa nhiều trường hợp.

Rủi ro:

- dịch chuyển phân phối;
- không có bảo đảm chấp nhận được;
- ước lượng sai nhưng tự tin;
- chi phí suy luận của chính mô hình.

Một cách lai là giữ riêng một cận dưới an toàn và dùng mô hình học chỉ để hướng dẫn thứ tự tìm kiếm.

## Hướng dẫn bằng chính sách và ước lượng giá trị

Một **chính sách (policy)** dự đoán hành động hứa hẹn:

\[
\pi(a\mid s)
\]

Một **hàm giá trị hoặc heuristic** ước lượng chất lượng trạng thái hoặc chi phí còn lại:

\[
V(s), h(s)
\]

Tìm kiếm có thể dùng cả hai:

```text
chính sách → ưu tiên / chọn hành động
giá trị     → đánh giá trạng thái kết quả
```

Đây là mẫu trung tâm trong tìm kiếm trò chơi được hướng dẫn bằng mạng nơ-ron và nhiều hệ thống lập kế hoạch hiện đại.

## Quan hệ giữa A* và Dijkstra/UCS

Dijkstra hoặc UCS:

\[
f(n)=g(n)
\]

A*:

\[
f(n)=g(n)+h(n)
\]

Heuristic có thể được xem như một thế năng giúp ưu tiên tìm theo hướng mục tiêu.

Khi `h=0`, A* trở về UCS nếu triển khai tương đương.

## Heuristic hình học

Với lưới chỉ cho di chuyển 4 hướng và mỗi bước có chi phí 1, khoảng cách Manhattan:

\[
h=|x-x_g|+|y-y_g|
\]

là heuristic chấp nhận được nếu không tồn tại phép dịch chuyển rẻ hơn như dịch chuyển chéo hay dịch chuyển tức thời.

Nếu cho phép đi chéo với chi phí 1, Manhattan có thể ước lượng quá cao; khoảng cách kiểu Chebyshev có thể phù hợp hơn.

Bài học quan trọng:

> **Heuristic chỉ hợp lệ tương đối với mô hình chuyển trạng thái và mô hình chi phí cụ thể.**

## Heuristic trong môi trường động

Nếu giao thông thay đổi, khoảng cách hình học tĩnh chỉ còn là cận dưới của thời gian di chuyển nếu giả định tốc độ tối đa vẫn hợp lệ.

Các thuật toán như D* hoặc Lifelong Planning A* có thể tái sử dụng kết quả tìm kiếm trước khi chi phí cạnh thay đổi.

Điều này nối heuristic search với định vị và robotics.

## Phân biệt lỗi tìm kiếm và lỗi heuristic

Nếu hệ thống trả đường xấu, cần chẩn đoán toàn bộ chuỗi:

```text
biểu diễn sai?
mô hình chuyển / chi phí sai?
heuristic không hợp lệ?
thuật toán triển khai sai?
ngân sách tính toán đã cắt mất lời giải tốt?
môi trường động nhưng trạng thái đã cũ?
```

Không nên mặc định mọi lỗi đều do heuristic.

## Tìm kiếm heuristic trong chứng minh định lý

Trạng thái chứng minh có thể là tập nghĩa vụ hoặc mệnh đề hiện tại; hành động là quy tắc suy luận; mục tiêu là hoàn tất chứng minh.

Heuristic xếp hạng mệnh đề hoặc mục tiêu con nên mở rộng trước.

Các hệ thống chứng minh định lý dùng nơ-ron hiện đại có thể học cách xếp hạng, trong khi kernel ký hiệu vẫn kiểm chứng tính đúng của chứng minh.

Đây là ví dụ mạnh của **Tìm kiếm + Học + Xác minh hình thức**.

## Tìm kiếm heuristic trong tác nhân LLM

Trạng thái tác nhân có thể gồm tiến độ nhiệm vụ, quan sát và kết quả công cụ. Chuỗi hành động ứng viên phân nhánh rất nhanh.

LLM có thể đề xuất hành động; mô hình hoặc quy tắc khác có thể đánh giá trạng thái. Hệ thống có thể giữ nhiều ứng viên thay vì chỉ một chuỗi tham lam.

Tuy nhiên điểm số của LLM không phải heuristic chấp nhận được. Vì vậy các bảo đảm lý thuyết của A* không tự động chuyển sang hệ thống này.

Cần dùng thuật ngữ chính xác:

```text
Tìm kiếm ưu tiên kiểu A* với điểm học được
≠
A* cổ điển với heuristic chấp nhận được
```

## Tìm kiếm và truy xuất

Hệ thống truy xuất thông tin xếp hạng tài liệu theo điểm liên quan. Về ý tưởng đây cũng là tìm kiếm trên một tập ứng viên, nhưng cấu trúc chỉ mục và thuật toán láng giềng gần nhất khác với tìm đường trong không gian trạng thái.

Hệ thống **láng giềng gần nhất xấp xỉ (Approximate Nearest Neighbor - ANN)** cố ý đánh đổi tính chính xác tuyệt đối để tăng tốc, tương tự nhiều đánh đổi của tìm kiếm giới hạn tài nguyên.

Mẫu tư duy chung là: **tránh liệt kê toàn bộ bằng cách dùng cấu trúc và tín hiệu hướng dẫn**.

## Mô hình tư duy (mental model)

```text
g(n) = chi phí đã trả
h(n) = chi phí còn lại được ước lượng
f(n) = tổng chi phí ước lượng nếu đi qua n

Greedy → chỉ tin h
UCS    → chỉ dùng g
A*     → cân bằng g + h
```

Heuristic chấp nhận được là cận dưới lạc quan. Heuristic nhất quán còn thỏa một ràng buộc cục bộ giống bất đẳng thức tam giác.

## Các hiểu lầm thường gặp

### “A* luôn là thuật toán đường ngắn nhất nhanh nhất”

Không. Hiệu năng phụ thuộc chất lượng heuristic, cấu trúc đồ thị, cách triển khai và bộ nhớ. `h` kém có thể làm A* gần giống UCS.

### “Heuristic phải dự đoán thật chính xác”

Nếu cần bảo đảm tối ưu cổ điển, tính chấp nhận được và nhất quán quan trọng hơn độ chính xác trung bình. Một heuristic kém sát hơn nhưng không ước lượng quá cao đôi khi phù hợp hơn.

### “Heuristic học được tự động giữ A* tối ưu”

Không, nếu nó có thể ước lượng quá cao hoặc vi phạm giả định.

### “Greedy và A* gần như giống nhau”

Greedy bỏ qua chi phí tích lũy `g`; A* giữ cả `g` và `h`. Đây là khác biệt nền tảng.

## Liên kết kiến thức

Tìm kiếm heuristic biến tri thức miền thành tiết kiệm tính toán. Nó nối AI cổ điển với tìm kiếm được hướng dẫn bằng mô hình hiện đại: heuristic viết tay có thể được thay thế hoặc bổ sung bằng ước lượng giá trị đã học, còn cơ chế tìm kiếm vẫn xử lý cấu trúc tổ hợp.

Xem tiếp: [Tìm kiếm đối kháng và trò chơi](./03_adversarial_search_and_games.md), [Bài toán thỏa mãn ràng buộc](./04_constraint_satisfaction.md) và [Lập kế hoạch](./05_planning.md).