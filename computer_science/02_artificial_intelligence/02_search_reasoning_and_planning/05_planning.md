# Lập kế hoạch trong Trí tuệ nhân tạo

Tìm kiếm đặt câu hỏi “từ trạng thái này, hành động nào dẫn tới mục tiêu?”. **Lập kế hoạch (planning / 계획)** làm câu hỏi đó tường minh hơn bằng cách biểu diễn **hành động có điều kiện trước (precondition) và hiệu ứng (effect)**, mục tiêu có cấu trúc, và một kế hoạch là chuỗi hoặc thứ tự một phần của các hành động làm mục tiêu trở thành đúng.

Lập kế hoạch quan trọng vì trí thông minh không chỉ phản ứng với quan sát hiện tại. Nhiều nhiệm vụ cần suy luận về hậu quả tương lai, điều kiện tiên quyết, xung đột tài nguyên và quan hệ phụ thuộc giữa các mục tiêu con. Lập kế hoạch cổ điển cung cấp ngôn ngữ chính xác cho những vấn đề mà khái niệm “AI agent planning” hiện đại thường mô tả khá lỏng.

Xem trước: [Không gian trạng thái và tìm kiếm](./00_state_space_and_search.md) và [Thỏa mãn ràng buộc](./04_constraint_satisfaction.md).

## Hành vi phản ứng và lập kế hoạch khác nhau thế nào?

Chính sách phản ứng:

```text
quan sát → hành động
```

Lập kế hoạch:

```text
trạng thái hiện tại + mục tiêu + mô hình hành động
              ↓
suy luận về các tương lai có thể xảy ra
              ↓
chuỗi hành động / chính sách
```

Hành vi phản ứng nhanh và bền vững khi môi trường quen thuộc. Lập kế hoạch hữu ích khi nhiệm vụ mới, có chân trời dài hoặc hành động có hậu quả đến muộn.

Tác nhân thực tế thường kết hợp cả hai: lập kế hoạch ở mức cao, phản ứng hoặc lập kế hoạch lại ở mức thấp.

## Biểu diễn trạng thái trong lập kế hoạch cổ điển

Một trạng thái có thể được biểu diễn bằng tập các mệnh đề.

Ví dụ kho hàng:

```text
At(robot, A)
BoxAt(box1, B)
HandEmpty(robot)
DoorOpen(B,C)
```

Trong nhiều bộ lập kế hoạch ký hiệu, **giả định thế giới đóng (closed-world assumption)** xem mệnh đề không được liệt kê là sai. Giả định này tiện cho tính toán nhưng không phù hợp với mọi bài toán tri thức ngoài đời thực.

## Hành động: điều kiện trước và hiệu ứng

Ví dụ hành động `Move(A,B)`:

```text
Điều kiện trước:
  At(robot, A)
  Connected(A, B)

Hiệu ứng:
  thêm At(robot, B)
  xóa At(robot, A)
```

Hành động chỉ áp dụng được khi các điều kiện trước đều đúng.

Mô hình chuyển trạng thái được tạo ra từ các hiệu ứng của hành động.

Cách biểu diễn này giàu cấu trúc hơn một hàm sinh trạng thái kế tiếp tổng quát trong tìm kiếm.

## Biểu diễn kiểu STRIPS

Một lược đồ hành động kiểu **STRIPS** thường gồm:

- danh sách điều kiện trước;
- các hiệu ứng thêm;
- các hiệu ứng xóa.

Nếu trạng thái `S` và hành động `a` áp dụng được:

\[
S'=(S\setminus Del(a))\cup Add(a)
\]

Biểu diễn gọn này cho phép bộ lập kế hoạch suy luận ký hiệu mà không cần liệt kê trước mọi phép chuyển trạng thái có thể xảy ra.

## PDDL

**Planning Domain Definition Language (PDDL)** là họ ngôn ngữ chuẩn dùng để mô tả miền lập kế hoạch và bài toán cụ thể.

Ví dụ khái niệm:

```lisp
(:action move
 :parameters (?r ?from ?to)
 :precondition (and (at ?r ?from) (connected ?from ?to))
 :effect (and
   (not (at ?r ?from))
   (at ?r ?to)))
```

PDDL tách quy tắc của miền khỏi trường hợp bài toán cụ thể.

Trong hệ thống LLM, việc chuyển yêu cầu ngôn ngữ tự nhiên thành biểu diễn PDDL hoặc mô hình bộ giải có thể là một thiết kế lai hữu ích.

## Biểu diễn mục tiêu

Mục tiêu có thể là phép hội:

```text
At(box1, Storage)
AND
At(robot, ChargingStation)
```

Bộ lập kế hoạch không cần tạo đúng một trạng thái đích đầy đủ; các mệnh đề không liên quan có thể thay đổi tự do.

Trừu tượng hóa mục tiêu giúp tránh thêm ràng buộc không cần thiết.

## Lập kế hoạch tiến

**Lập kế hoạch tiến (forward state-space planning)** bắt đầu từ trạng thái ban đầu, áp dụng các hành động khả dụng cho tới khi đạt mục tiêu.

```text
S0
 ├─ a1 → S1
 ├─ a2 → S2
 ...
```

Có thể dùng BFS, UCS hoặc A* cùng heuristic chuyên cho bài toán lập kế hoạch.

Điểm yếu là rất nhiều hành động khả dụng có thể hoàn toàn không liên quan tới mục tiêu, làm hệ số phân nhánh lớn.

## Lập kế hoạch lùi

**Lập kế hoạch lùi hoặc hồi quy (backward/regression planning)** bắt đầu từ điều kiện mục tiêu và suy luận hành động nào có thể tạo ra chúng.

Nếu mục tiêu cần `At(box,Storage)`, bộ lập kế hoạch xem những hành động nào có hiệu ứng thêm mệnh đề này, sau đó thay mục tiêu bằng các điều kiện trước của hành động.

Cách này tập trung hơn vào hành động liên quan tới mục tiêu nhưng việc hồi quy qua nhiều tương tác vẫn có thể phức tạp.

## Lập kế hoạch thứ tự một phần

Kế hoạch tuần tự áp đặt một thứ tự toàn phần:

```text
A → B → C → D
```

Nhưng nhiều hành động độc lập. **Lập kế hoạch thứ tự một phần (partial-order planning)** chỉ đặt những quan hệ thứ tự thật sự cần thiết:

```text
A trước C
B trước D
A và B có thể đổi thứ tự hoặc chạy song song
```

Nguyên lý **cam kết tối thiểu (least commitment)** tránh quyết định thứ tự sớm hơn mức cần thiết.

Điều này làm lộ khả năng song song và giữ kế hoạch linh hoạt hơn.

## Liên kết nhân quả

Nếu hành động `A` tạo ra điều kiện `p` mà `B` cần, ta có **liên kết nhân quả (causal link)**:

\[
A \xrightarrow{p} B
\]

Một hành động `C` xóa `p` nếu chen giữa A và B sẽ đe dọa liên kết này.

Bộ lập kế hoạch phải xử lý bằng cách đặt C trước A, sau B hoặc thêm ràng buộc phù hợp.

Nhờ vậy quan hệ phụ thuộc giữa các bước trở nên tường minh.

## Đồ thị lập kế hoạch

Đồ thị kiểu GraphPlan xen kẽ tầng mệnh đề và tầng hành động:

```text
P0 → A0 → P1 → A1 → P2 ...
```

Nó cũng theo dõi quan hệ **loại trừ lẫn nhau (mutex / mutual exclusion)**.

Đồ thị lập kế hoạch cung cấp thông tin về khả năng đạt tới và heuristic mà không phải liệt kê mọi tổ hợp trạng thái.

## Nới lỏng hiệu ứng xóa

Nhiều heuristic lập kế hoạch bỏ qua hiệu ứng xóa: một khi một sự kiện trở thành đúng, tạm giả định nó sẽ đúng mãi.

Bài toán nới lỏng dễ hơn và lạc quan hơn.

Từ đó có các heuristic như:

- `h_max`;
- `h_add`;
- heuristic kế hoạch nới lỏng `h_FF` trong họ Fast Forward.

Đây cùng nguyên lý với heuristic search: giải một bài toán dễ hơn để ước lượng bài toán thật.

## Vì sao hiệu ứng xóa quan trọng?

Bỏ hiệu ứng xóa có thể quá lạc quan khi hành động hoặc tài nguyên xung đột nhau.

Ví dụ một xe tải không thể đồng thời ở hai thành phố, nhưng bài toán nới lỏng có thể hành xử như cả hai sự kiện đều cùng tồn tại.

Heuristic vẫn hữu ích dù mô hình nới lỏng không thực tế, vì nó nắm cấu trúc mục tiêu với chi phí thấp.

## Lập kế hoạch với tài nguyên

Lập kế hoạch mệnh đề cổ điển thường bỏ qua tài nguyên liên tục và thời gian. Bài toán thực tế có thể cần:

- nhiên liệu;
- pin;
- tiền;
- công suất máy;
- thời hạn;
- thời lượng hành động.

Lập kế hoạch số và thời gian mở rộng mô hình hành động để xử lý các đại lượng này.

Khi đó lập kế hoạch giao nhau mạnh với lập lịch, lập trình ràng buộc và Nghiên cứu vận hành.

## Lập kế hoạch thời gian

Hành động có thể có thời lượng:

```text
Sạc(robot): 30 phút
Di chuyển(A,B): 10 phút
Kiểm tra: 5 phút
```

Một số hành động có thể chạy đồng thời nếu không tranh chấp tài nguyên hoặc vi phạm ràng buộc.

Mục tiêu lúc này không chỉ là khả thi mà còn có thể là giảm **thời gian hoàn thành toàn bộ (makespan)**.

Lập kế hoạch thời gian cần suy luận trên khoảng thời gian và tính đồng thời.

## Mạng nhiệm vụ phân cấp

**Hierarchical Task Network (HTN)** biểu diễn nhiệm vụ cấp cao và cách phân rã chúng thành các nhiệm vụ con.

Ví dụ:

```text
GiaoHàng
  ↓
NhậnHàng
LậpĐườngĐi
VậnChuyển
BànGiao
```

Tri thức miền giới hạn những cách phân rã được phép.

HTN có thể giảm mạnh không gian tìm kiếm vì đã mã hóa cấu trúc thủ tục, đổi lại nó ít tổng quát theo miền hơn lập kế hoạch không ràng buộc.

Cấu trúc này rất gần với phân rã nhiệm vụ trong luồng công việc phần mềm và tác nhân LLM.

## Phân rã mục tiêu

Nếu mục tiêu là `G1 ∧ G2`, chỉ có thể giải hai mục tiêu độc lập khi hành động giữa chúng không can thiệp.

Trong thực tế, các mục tiêu con thường tương tác.

Ví dụ kinh điển trong Blocks World: đạt một mục tiêu trước có thể phá mục tiêu khác nếu thứ tự không phù hợp.

Vì vậy “chia nhiệm vụ thành các nhiệm vụ con” chưa đủ; cần theo dõi phụ thuộc và tác dụng phụ.

## Phân tích phương tiện–mục đích

**Phân tích phương tiện–mục đích (Means–Ends Analysis)** so sánh trạng thái hiện tại với mục tiêu, chọn một khác biệt, chọn hành động làm giảm khác biệt đó, rồi tạo các mục tiêu con từ điều kiện trước của hành động.

Ý tưởng này từng ảnh hưởng mạnh tới General Problem Solver.

Lời nhắc cho tác nhân hiện đại đôi khi tái tạo cùng mẫu tư duy bằng ngôn ngữ tự nhiên, nhưng biểu diễn ký hiệu làm các giả định rõ hơn.

## Tính hợp lệ của kế hoạch

Một danh sách hành động chỉ hợp lệ nếu điều kiện trước của từng hành động đúng tại thời điểm thực thi và trạng thái cuối thỏa mục tiêu.

Bộ kiểm tra độc lập có thể xác minh kế hoạch.

Sự tách biệt này rất mạnh:

```text
bộ sinh có thể dùng heuristic hoặc mô hình học
        ↓
bộ kiểm tra hình thức xác minh ràng buộc chính xác
```

Kiến trúc tương tự hữu ích cho tác nhân LLM: mô hình đề xuất, công cụ xác định kiểm tra.

## Lập kế hoạch và lập lịch

Lập kế hoạch chọn **cần những hành động nào và phụ thuộc ra sao** để đạt mục tiêu.

Lập lịch chọn **khi nào và tài nguyên nào** thực hiện các nhiệm vụ đã biết.

Bài toán thực tế thường kết hợp cả hai.

Ví dụ sản xuất:

```text
Lập kế hoạch: cần các bước xử lý nào?
Lập lịch: máy nào và khung giờ nào xử lý từng bước?
```

Trộn hai khái niệm làm mờ những ràng buộc khác nhau của chúng.

## Lập kế hoạch xác định và ngẫu nhiên

Lập kế hoạch cổ điển thường giả định hiệu ứng hành động xác định.

Trong thực tế hành động có thể thất bại:

\[
P(s'\mid s,a)
\]

Lúc này kế hoạch là một chuỗi cố định có thể không đủ. Ta cần **chính sách (policy)** ánh xạ trạng thái hoặc niềm tin sang hành động, dẫn tới MDP/POMDP.

Phần chuyển tiếp này được trình bày trong [Ra quyết định dưới bất định](./06_decision_making_under_uncertainty.md).

## Lập kế hoạch ngoại tuyến và lập kế hoạch lại trực tuyến

Bộ lập kế hoạch ngoại tuyến tính toàn bộ kế hoạch trước khi thực thi.

Tác nhân trực tuyến hoặc theo **chân trời trượt (receding horizon)** hoạt động như:

```text
quan sát
  ↓
lập kế hoạch cho một chân trời ngắn
  ↓
hành động
  ↓
quan sát kết quả thật
  ↓
lập kế hoạch lại
```

Lập kế hoạch lại xử lý môi trường động và sai lệch giữa mô hình với thế giới.

Robotics thường dùng ý tưởng tương tự Model Predictive Control trong điều khiển liên tục.

## Giám sát thực thi kế hoạch

Kế hoạch có thể thất bại vì thế giới thay đổi hoặc hiệu ứng hành động khác dự kiến.

Hệ thống thực thi cần phát hiện:

- điều kiện trước không còn đúng;
- lỗi công cụ hoặc API;
- tài nguyên không còn khả dụng;
- quan sát mới mâu thuẫn mô hình;
- mục tiêu đã đạt sớm.

Kiến trúc tác nhân đáng tin cậy nên tách bộ lập kế hoạch khỏi thành phần giám sát thực thi.

## Lập kế hoạch dự phòng

Nếu một số bất định đã biết, kế hoạch có thể phân nhánh:

```text
Thử thanh toán
 ├─ thành công → giao hàng
 └─ thất bại → yêu cầu phương thức khác
```

Đây là **kế hoạch có điều kiện (conditional plan)** chứ không phải chuỗi duy nhất.

Khi bất định tăng, cây dự phòng tường minh nhanh chóng bùng nổ; chính sách và MDP là hình thức mở rộng dễ quản lý hơn.

## Lập kế hoạch và tìm kiếm

Lập kế hoạch có thể được chuyển về bài toán tìm kiếm:

```text
trạng thái = tập các sự kiện
hành động = toán tử
trạng thái kế = áp dụng hiệu ứng
test mục tiêu = các mệnh đề mục tiêu đều đúng
```

Tuy nhiên biểu diễn hành động có cấu trúc cho phép dùng heuristic và suy luận chuyên biệt mà tìm kiếm đồ thị tổng quát không có.

Bài học:

> **Cùng một bài toán có thể trở nên dễ giải hơn khi thuật toán hiểu cấu trúc của biểu diễn.**

## Lập kế hoạch và CSP/SAT

Lập kế hoạch có chân trời giới hạn có thể được mã hóa thành SAT.

Với chân trời `T`, tạo biến Boolean cho các sự kiện và hành động ở từng thời điểm cùng ràng buộc chuyển trạng thái và mục tiêu.

Sau đó hỏi bộ giải SAT liệu có kế hoạch độ dài `T` hay không, rồi tăng `T` cho tới khi thỏa mãn.

Đây là ví dụ khác của việc chuyển một bài toán AI sang một miền bộ giải trưởng thành hơn.

## Lập kế hoạch và tối ưu số nguyên

Lập lịch hoặc lập kế hoạch tài nguyên có thể được mã hóa thành MILP:

- biến nhị phân cho lựa chọn hành động;
- thời gian dạng số nguyên hoặc liên tục;
- ràng buộc năng lực tuyến tính;
- hàm mục tiêu giảm chi phí hoặc makespan.

Lựa chọn bộ giải phụ thuộc cấu trúc bài toán; “thuật toán AI planning” không phải lúc nào cũng là công cụ thực tế tốt nhất.

## Tác nhân cổ điển và tác nhân LLM

Lập kế hoạch cổ điển có biểu diễn tường minh:

```text
trạng thái
hành động
điều kiện trước
hiệu ứng
mục tiêu
mô hình chuyển trạng thái
```

Tác nhân LLM thường dùng trạng thái ngôn ngữ tự nhiên và mô tả công cụ ít chặt chẽ hơn.

Tính linh hoạt này hữu ích cho nhiệm vụ thế giới mở nhưng làm yếu các bảo đảm.

Kiến trúc bền vững có thể đưa cấu trúc trở lại:

```text
Mục tiêu ngôn ngữ tự nhiên
        ↓
trạng thái nhiệm vụ có cấu trúc
        ↓
bộ lập kế hoạch / LLM đề xuất hành động công cụ
        ↓
bộ kiểm tra xác minh điều kiện trước và schema
        ↓
thực thi công cụ
        ↓
ghi nhận quan sát thật
        ↓
lập kế hoạch lại
```

## Công cụ như mô hình hành động

Một API hoặc công cụ có thể được nhìn như:

- đầu vào → tham số;
- điều kiện trước → yêu cầu xác thực/trạng thái;
- hiệu ứng → thay đổi trạng thái bên ngoài;
- quan sát → kết quả hoặc lỗi công cụ.

Cách nhìn này khớp tự nhiên với ngôn ngữ lập kế hoạch.

Ví dụ `send_email` không nên được xem chỉ là sinh văn bản; nó có tác dụng phụ bên ngoài khó đảo ngược nên có thể cần kiểm tra hoặc xác nhận trước khi thực thi.

## Lập kế hoạch dài hạn và tích lũy lỗi

Nếu mỗi hành động có xác suất thành công độc lập `p`, một xấp xỉ thô cho xác suất thành công của chuỗi `T` bước là:

\[
p^T
\]

và giảm nhanh khi `T` tăng.

Hệ thống thật không độc lập như vậy, nhưng trực giác này giải thích nhu cầu về:

- chân trời lập kế hoạch ngắn;
- checkpoint;
- xác minh;
- lập kế hoạch lại;
- hành động có tính lặp lại an toàn (idempotent);
- rollback hoặc hành động bù trừ.

Kỹ nghệ phần mềm trở thành một phần của độ tin cậy trong lập kế hoạch tác nhân.

## Lập kế hoạch với mô hình thế giới đã học

Nếu mô hình chuyển chưa biết, mạng nơ-ron có thể học:

\[
\hat T(s,a)\rightarrow s'
\]

Bộ lập kế hoạch tìm trên những quỹ đạo được mô phỏng bởi mô hình đã học.

Rủi ro là sai số mô hình tích lũy ngoài phân phối huấn luyện. Bộ lập kế hoạch thậm chí có thể khai thác lỗ hổng của mô hình, tìm quỹ đạo trông rất tốt trong mô phỏng nhưng thất bại ngoài thực tế.

Đây là một vấn đề trung tâm của học tăng cường dựa trên mô hình và world model.

## Liên hệ với Model Predictive Control

**Model Predictive Control (MPC)** liên tục tối ưu một chân trời hữu hạn, thực thi bước đầu, rồi tối ưu lại sau khi có quan sát mới.

```text
tối ưu H bước
thực thi 1 bước
quan sát
trượt chân trời
lặp lại
```

Đây là phiên bản trong lý thuyết điều khiển của lập kế hoạch lại trực tuyến và giúp giảm tích lũy sai số mô hình trên chân trời dài.

## Kế hoạch bằng ngôn ngữ và kế hoạch thực thi

Lời nhắc kiểu “hãy lập kế hoạch trước rồi trả lời” có thể giúp LLM tổ chức công việc, nhưng một kế hoạch ngôn ngữ tự nhiên chưa chắc là kế hoạch hình thức có thể thực thi.

Cần phân biệt:

```text
dàn ý ngôn ngữ
≠
kế hoạch hành động đã được xác minh
```

Với tác nhân dùng công cụ, chất lượng kế hoạch cần được đánh giá bằng tính khả thi, độ đúng phụ thuộc và tỷ lệ thực thi thành công, không phải độ thuyết phục của câu chữ.

## Mô hình tư duy (mental model)

```text
Tìm kiếm     = khám phá trạng thái có thể xảy ra
Lập kế hoạch = khai thác ngữ nghĩa hành động để xây hành vi đạt mục tiêu

Trạng thái   = các sự kiện đang đúng
Hành động    = điều kiện trước + hiệu ứng
Kế hoạch     = hành động có thứ tự toàn phần hoặc một phần
Bộ kiểm tra  = xác minh ngữ nghĩa kế hoạch
Bộ thực thi  = tương tác với môi trường thật
Bộ lập lại   = cập nhật khi thực tế khác mô hình
```

## Các hiểu lầm thường gặp

### “Lập kế hoạch chỉ là viết danh sách việc cần làm”

Lập kế hoạch AI suy luận về điều kiện trước, hiệu ứng, xung đột, tài nguyên và khả năng đạt tới. Một danh sách không có mô hình hợp lệ chỉ là dàn ý.

### “Kế hoạch đúng thì thực thi chắc chắn thành công”

Chỉ đúng dưới mô hình xác định và chính xác. Môi trường thật cần giám sát và lập kế hoạch lại.

### “LLM viết được các bước hợp lý nên tự động lập kế hoạch tốt”

Các bước nghe hợp lý vẫn có thể vi phạm ràng buộc ẩn hoặc trạng thái công cụ. Hệ thống đáng tin cần theo dõi trạng thái và xác minh.

### “Kế hoạch càng chi tiết càng tốt”

Lập kế hoạch quá xa dễ trở nên mong manh khi môi trường bất định. Lập kế hoạch chân trời trượt cố ý giữ quyết định tương lai linh hoạt.

## Liên kết kiến thức

Lập kế hoạch nằm giữa tìm kiếm, CSP, logic và lý thuyết quyết định. Nó cung cấp ngôn ngữ chính xác cho tác nhân hiện đại: **mục tiêu, trạng thái, hành động, điều kiện trước, hiệu ứng, giám sát và lập kế hoạch lại**. Phần `10_agents_and_ai_systems/` sẽ tái sử dụng các khái niệm này thay vì định nghĩa lại từ đầu.

Xem tiếp: [Ra quyết định dưới bất định](./06_decision_making_under_uncertainty.md).