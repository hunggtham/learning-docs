# Bài toán thỏa mãn ràng buộc trong AI

Một số bài toán không cần tìm một đường đi cụ thể; ta chỉ cần tìm **một phép gán thỏa tất cả ràng buộc**. Lập lịch, Sudoku, tô màu bản đồ, phân bổ tài nguyên, cấu hình hệ thống và nhiều bài toán con của lập kế hoạch có cấu trúc này.

**Bài toán thỏa mãn ràng buộc (Constraint Satisfaction Problem - CSP / 제약 만족 문제)** tách bài toán thành biến, miền giá trị và ràng buộc. Cách biểu diễn này cho phép dùng suy luận để loại bỏ rất nhiều khả năng trước khi phải tìm kiếm, minh họa một nguyên lý quan trọng của AI:

> **Biểu diễn tốt có thể làm bài toán dễ hơn rất nhiều so với vét cạn trên mọi cấu hình thô.**

Xem trước: [Biểu diễn bài toán](../00_foundations/03_problem_representation.md) và [Không gian trạng thái và tìm kiếm](./00_state_space_and_search.md).

## Một CSP gồm những gì?

Một CSP được mô tả bằng:

\[
(X,D,C)
\]

trong đó:

- `X={X1,...,Xn}` là tập biến;
- `D_i` là miền giá trị của biến `X_i`;
- `C` là tập ràng buộc.

Mục tiêu là tìm phép gán:

\[
X_i=v_i
\]

sao cho mọi ràng buộc đều được thỏa mãn.

## Ví dụ tô màu bản đồ

Giả sử cần tô các vùng sao cho hai vùng kề nhau có màu khác nhau.

```text
Biến: WA, NT, SA, Q, NSW, V, T
Miền: {Đỏ, Xanh lá, Xanh dương}
Ràng buộc: WA != NT, WA != SA, ...
```

Thứ tự tô màu cuối cùng không quan trọng; điều quan trọng là phép gán cuối cùng hợp lệ.

Đây là khác biệt với tìm đường, nơi chính đường đi cũng có ý nghĩa và chi phí.

## Ràng buộc một biến, hai biến và toàn cục

**Ràng buộc một biến (unary constraint)** chỉ áp dụng lên một biến:

\[
X\neq Red
\]

**Ràng buộc hai biến (binary constraint)** liên hệ hai biến:

\[
X\neq Y
\]

**Ràng buộc toàn cục (global constraint)** liên hệ nhiều biến, ví dụ `AllDifferent(X1,...,Xn)` trong Sudoku hoặc lập lịch.

Ràng buộc toàn cục không chỉ giúp viết ngắn hơn. Thuật toán lan truyền chuyên biệt có thể khai thác cấu trúc của nó mạnh hơn việc tách thành hàng loạt ràng buộc từng cặp.

## Đồ thị ràng buộc

CSP hai biến có thể được biểu diễn bằng đồ thị:

```text
nút = biến
cạnh = ràng buộc giữa hai biến
```

Cấu trúc đồ thị giúp suy luận về tính độc lập, khả năng phân rã và độ phức tạp kiểu treewidth.

Nếu đồ thị tách thành các thành phần không liên thông, từng phần có thể được giải độc lập.

## Liệt kê vét cạn

Nếu có `n` biến và mỗi miền có kích thước `d`, số phép gán có thể là:

\[
d^n
\]

Sudoku có 81 ô với miền 9 chữ số gợi ý tới `9^81` tổ hợp thô, một con số khổng lồ.

Tuy nhiên các ràng buộc loại bỏ ngay phần lớn tổ hợp. Thuật toán CSP tận dụng điều này trước và trong quá trình phân nhánh.

## Tìm kiếm quay lui

**Tìm kiếm quay lui (backtracking search)** gán biến từng bước. Khi phép gán một phần vi phạm ràng buộc, thuật toán quay lui và thử giá trị khác.

```pseudo
quay_lui(phép_gán):
    if đã_hoàn_chỉnh: return phép_gán

    X ← chọn_biến_chưa_gán()
    for v in thứ_tự_giá_trị(X):
        if nhất_quán(X=v, phép_gán):
            gán X=v
            kết_quả ← quay_lui(phép_gán)
            if thành_công: return kết_quả
            hủy_gán X

    return thất_bại
```

Về bản chất đây là DFS trên không gian phép gán, nhưng suy luận chuyên biệt cho CSP khiến nó mạnh hơn DFS ngây thơ.

## Thứ tự biến: MRV

**Giá trị còn lại ít nhất (Minimum Remaining Values - MRV)** chọn biến có ít giá trị hợp lệ nhất.

Trực giác:

> **Phát hiện thất bại càng sớm càng tốt.**

Nếu một biến gần như không thể gán, xử lý nó trước giúp phát hiện mâu thuẫn sớm thay vì lãng phí tìm kiếm trên các nhánh khác.

MRV còn được gọi là chọn “biến bị ràng buộc nhiều nhất”.

## Heuristic bậc của biến

Nếu nhiều biến hòa nhau theo MRV, có thể chọn biến tham gia nhiều ràng buộc nhất với các biến chưa gán.

Ý tưởng là chọn biến có ảnh hưởng lớn để lan truyền hạn chế sớm.

MRV nhìn số giá trị còn lại; heuristic bậc nhìn mức liên kết trong đồ thị.

## Thứ tự giá trị: giá trị ít hạn chế nhất

Sau khi chọn biến, **giá trị ít hạn chế nhất (Least Constraining Value - LCV)** ưu tiên giá trị loại bỏ ít lựa chọn của các biến lân cận nhất.

Heuristic chọn biến thường theo tinh thần “thất bại sớm”; heuristic chọn giá trị thường cố “để lại nhiều linh hoạt”. Hai ý tưởng không mâu thuẫn: chọn biến khó trước nhưng chọn giá trị ít phá lựa chọn tương lai.

## Kiểm tra trước

Khi gán `X=v`, **kiểm tra trước (forward checking)** loại các giá trị không tương thích khỏi miền của các biến lân cận.

Nếu miền của biến lân cận trở thành rỗng, thất bại được phát hiện ngay.

Ví dụ:

```text
X có miền {R,G}
Y có miền {R,G}
ràng buộc X != Y

gán X=R
→ loại R khỏi Y
→ Y={G}
```

Forward checking phát hiện hệ quả cục bộ trước một bước.

## Lan truyền ràng buộc

Mạnh hơn forward checking, **lan truyền ràng buộc (constraint propagation)** lặp lại việc áp dụng các quy tắc nhất quán cho tới khi không thể thu hẹp miền thêm nữa.

Ví dụ:

```text
X=R
→ Y không thể R
→ Y=G
→ Z không thể G
→ Z=B
```

Một phép gán có thể gây hiệu ứng dây chuyền trên toàn mạng ràng buộc.

## Tính nhất quán cung

Với ràng buộc hai biến giữa `X` và `Y`, cung `X→Y` có **tính nhất quán cung (arc consistency)** nếu mỗi giá trị trong `D_X` đều có ít nhất một giá trị hỗ trợ trong `D_Y` thỏa ràng buộc.

Nếu giá trị `x` không có bất kỳ hỗ trợ nào ở `Y`, nó được loại khỏi miền của `X`.

Thuật toán **AC-3** liên tục xem lại các cung cho tới khi ổn định hoặc một miền trở thành rỗng.

```pseudo
hàng_đợi ← tất_cả_các_cung
while hàng_đợi:
    (Xi,Xj) ← pop
    if sửa_miền(Xi,Xj):
        if miền(Xi) rỗng: thất_bại
        for Xk là_láng_giềng_của Xi, Xk != Xj:
            thêm (Xk,Xi)
```

## Nhất quán cục bộ không bảo đảm có lời giải toàn cục

Một CSP có thể nhất quán theo từng cung nhưng vẫn không có lời giải toàn cục.

Điểm quan trọng là:

```text
lan truyền ràng buộc giúp giảm không gian tìm kiếm
nhưng thường không loại bỏ hoàn toàn nhu cầu phân nhánh tìm kiếm
```

## Duy trì tính nhất quán cung

**Maintaining Arc Consistency (MAC)** chạy kiểm tra nhất quán cung sau mỗi phép gán trong quá trình quay lui.

Cách này tốn nhiều suy luận hơn ở mỗi nút nhưng có thể giảm mạnh số nút phải tìm.

Đánh đổi:

```text
nhiều suy luận hơn trên mỗi nút
↔
ít phân nhánh hơn
```

Điểm cân bằng tốt phụ thuộc cấu trúc bài toán.

## Sudoku như một CSP

Biến = 81 ô.

Miền = các chữ số 1..9 cho ô trống.

Ràng buộc:

- mỗi hàng `AllDifferent`;
- mỗi cột `AllDifferent`;
- mỗi khối 3×3 `AllDifferent`.

Các kỹ thuật con người như “ô này chỉ còn một số có thể điền” chính là dạng lan truyền ràng buộc.

Đoán và quay lui chỉ cần khi suy luận chưa đủ.

## Lập lịch

Biến có thể là các nhiệm vụ.

Miền là các thời điểm hoặc tài nguyên có thể sử dụng.

Ràng buộc ví dụ:

```text
Nhiệm vụ A phải trước B
A và C không được dùng cùng máy cùng lúc
nhân viên E chỉ rảnh ở một số khung giờ
tổng công suất mỗi tuần có giới hạn
```

Lập lịch thực tế thường dẫn tới **lập trình ràng buộc (Constraint Programming - CP)** hoặc tối ưu số nguyên hỗn hợp thay vì CSP hữu hạn đơn giản.

## Ràng buộc cứng và mềm

CSP cổ điển xem ràng buộc là điều bắt buộc phải thỏa.

Bài toán thực tế thường có cả sở thích mềm:

```text
cứng: hai cuộc họp không được cùng phòng và cùng giờ
mềm: ưu tiên buổi sáng
mềm: giảm làm thêm giờ
```

Weighted CSP, Max-CSP hoặc mô hình tối ưu gán chi phí cho việc vi phạm sở thích mềm.

Đây là điểm giao với Nghiên cứu vận hành (Operations Research).

## SAT như một bài toán ràng buộc

**Bài toán thỏa mãn Boolean (Boolean Satisfiability - SAT)** hỏi liệu có phép gán đúng/sai cho các biến để công thức Boolean trở thành đúng hay không.

Các biến là Boolean, còn ràng buộc là các mệnh đề.

Ví dụ dạng chuẩn hội (CNF):

\[
(A\lor \neg B)\land(B\lor C)
\]

SAT là NP-complete nhưng bộ giải SAT hiện đại rất hiệu quả trên nhiều bài toán có cấu trúc nhờ:

- lan truyền đơn vị;
- học mệnh đề từ xung đột (CDCL);
- heuristic chọn biến;
- khởi động lại.

“NP-complete” không có nghĩa mọi trường hợp thực tế đều bất khả thi.

## Lan truyền đơn vị

Nếu có mệnh đề:

\[
(A\lor B)
\]

và `A=false`, thì `B` buộc phải đúng.

Đây là một dạng lan truyền ràng buộc trên công thức Boolean.

CSP và SAT chia sẻ cùng một ý tưởng sâu: **dùng suy luận để thu hẹp miền trước khi buộc phải phân nhánh**.

## Học mệnh đề từ xung đột

Khi bộ giải SAT đi tới mâu thuẫn, nó phân tích nguyên nhân để suy ra mệnh đề mới ngăn cùng kiểu phép gán sai lặp lại. Cơ chế này gọi là **Conflict-Driven Clause Learning (CDCL)**.

Về khái niệm:

```text
phân nhánh
 ↓
mâu thuẫn
 ↓
phân tích nguyên nhân
 ↓
học thêm ràng buộc
 ↓
tránh lặp lại sai lầm
```

Đây là tìm kiếm có khả năng **học từ thất bại**.

Mẫu tư duy này có nét tương đồng với hệ thống suy luận hiện đại có bộ nhớ và xác minh, dù CDCL dựa trên ngữ nghĩa Boolean hình thức và có bảo đảm mạnh hơn.

## Tìm kiếm cục bộ cho CSP

Thay vì xây dần phép gán nhất quán, có thể bắt đầu từ một phép gán đầy đủ nhưng có vi phạm rồi liên tục giảm xung đột.

**Min-conflicts** chọn một biến đang xung đột và gán lại giá trị làm số vi phạm nhỏ nhất.

Phương pháp này hoạt động rất tốt với bài toán N-Queens lớn.

Tìm kiếm cục bộ dùng ít bộ nhớ nhưng có thể mắc kẹt và không đầy đủ nếu không có chiến lược bổ sung.

## Bài toán N quân hậu

Đặt `N` quân hậu lên bàn `N×N` sao cho không quân nào tấn công nhau.

Biến: một quân hậu cho mỗi cột.

Miền: số hàng.

Ràng buộc:

\[
Q_i\neq Q_j
\]

và:

\[
|Q_i-Q_j|\neq|i-j|
\]

Cách biểu diễn “mỗi cột đúng một quân hậu” đã loại bỏ xung đột cùng cột ngay từ cấu trúc bài toán. Đây là ví dụ rõ rằng biểu diễn tốt có thể giảm ràng buộc trước cả khi chạy thuật toán.

## Phá đối xứng

Nhiều CSP có các lời giải tương đương do đối xứng. Tìm kiếm có thể lãng phí thời gian khám phá nhiều hoán vị của cùng một cấu trúc.

Ví dụ trong tô màu, đổi tên toàn bộ Đỏ ↔ Xanh lá có thể tạo một lời giải tương đương.

Có thể thêm **ràng buộc phá đối xứng (symmetry-breaking constraint)** để chỉ giữ một đại diện chuẩn.

Một lần nữa, biểu diễn và ràng buộc giúp thu nhỏ không gian tìm kiếm mạnh mẽ.

## Phân rã bài toán

Nếu đồ thị ràng buộc có các thành phần độc lập, ta có thể giải từng phần riêng.

CSP có cấu trúc cây thường giải hiệu quả hơn nhiều so với đồ thị chu trình tùy ý.

**Treewidth** đo gần đúng mức độ một đồ thị khác cây đến đâu; nhiều thuật toán có độ phức tạp theo cấp số nhân của treewidth thay vì chỉ theo số lượng biến.

Điều này nối CSP với mô hình đồ thị xác suất và suy luận trên đồ thị.

## CSP và tối ưu hóa

CSP hỏi:

> Có phép gán nào thỏa mọi ràng buộc không?

Tối ưu hóa hỏi:

> Trong các phép gán khả thi, phép nào tốt nhất theo hàm mục tiêu?

Hệ thống thực tế thường kết hợp:

\[
\min_x f(x)\quad\text{s.t. các ràng buộc}
\]

Lập lịch, định tuyến và phân bổ tài nguyên thường dùng Mixed Integer Programming, CP-SAT hoặc bộ giải chuyên biệt.

AI, Nghiên cứu vận hành và tối ưu hóa giao nhau rất mạnh ở đây.

## Lập trình ràng buộc

**Lập trình ràng buộc (Constraint Programming)** cho phép lập trình viên khai báo biến và ràng buộc, còn bộ giải chịu trách nhiệm lan truyền và tìm kiếm.

Ví dụ API khái niệm:

```python
start_A < start_B
no_overlap(tasks_on_machine_1)
all_different(room_assignments)
```

Cách này tách **điều gì phải đúng** khỏi **thuật toán cụ thể dùng để tìm lời giải**.

Tinh thần khai báo này gần với lập trình logic.

## Heuristic học được cho CSP và SAT

Thứ tự chọn biến và giá trị ảnh hưởng rất mạnh tới thời gian chạy. Học máy có thể học heuristic phân nhánh từ các bài toán đã giải.

Tuy nhiên tính đúng vẫn có thể được giữ bởi bộ giải ký hiệu: thành phần học chỉ quyết định nên tìm ở đâu trước; bộ kiểm tra ràng buộc hoặc cơ chế chứng minh vẫn bảo đảm tính hợp lệ.

Thiết kế lai này hấp dẫn vì học giúp tăng tốc mà không phải tin mô hình nơ-ron cho tính đúng cuối cùng.

## LLM kết hợp bộ giải ràng buộc

LLM có thể đề xuất lịch hoặc cấu hình, nhưng sinh văn bản tự do không bảo đảm ràng buộc cứng.

Một kiến trúc đáng tin hơn:

```text
LLM hiểu yêu cầu bằng ngôn ngữ tự nhiên
        ↓
chuyển thành mô hình CSP có cấu trúc
        ↓
bộ giải tìm và kiểm tra phép gán
        ↓
LLM giải thích kết quả
```

Cách này mạnh hơn việc yêu cầu LLM “ghi nhớ mọi ràng buộc” trong một đoạn sinh tự do.

## Kiểm tra đầu ra có cấu trúc

Lược đồ JSON và ràng buộc kiểu dữ liệu có thể xem là họ hàng đơn giản của CSP. Bộ giải mã hoặc bộ kiểm tra sau sinh bảo đảm đầu ra thuộc một miền cấu trúc hợp lệ.

Giải mã theo ngữ pháp giúp giảm lỗi cú pháp, nhưng ràng buộc ngữ nghĩa như “ngày kết thúc phải sau ngày bắt đầu” vẫn cần kiểm tra hoặc bộ giải giàu biểu đạt hơn.

## Mô hình tư duy (mental model)

```text
Biến        = thứ cần lựa chọn
Miền        = các giá trị có thể chọn
Ràng buộc   = tổ hợp bị cấm hoặc bắt buộc
Lan truyền  = loại giá trị bất khả thi mà chưa cần đoán
Tìm kiếm    = phân nhánh khi suy luận chưa đủ
Heuristic   = chọn biến/giá trị phân nhánh thông minh hơn
Học         = có thể cải thiện heuristic, không nhất thiết quyết định tính đúng
```

## Các hiểu lầm thường gặp

### “CSP chỉ là thử mọi phép gán”

Bộ giải CSP tốt dùng lan truyền, heuristic, học từ xung đột và phân rã để tránh phần lớn tổ hợp.

### “Nhất quán cung nghĩa là đã giải xong”

Nhất quán cục bộ có thể tồn tại trong một bài toán vẫn không có lời giải toàn cục.

### “LLM đủ lớn có thể thay hoàn toàn bộ giải ràng buộc”

LLM có thể đề xuất lời giải, nhưng khi cần bảo đảm cứng phải có cơ chế kiểm tra, tìm kiếm hoặc suy luận hình thức tường minh.

### “NP-complete nghĩa là bộ giải thực tế vô dụng”

Độ phức tạp trường hợp xấu không mô tả mọi bài toán có cấu trúc. Bộ giải SAT/CP có thể xử lý hiệu quả nhiều bài toán lớn trong thực tế.

## Liên kết kiến thức

CSP nằm ở giao điểm của tìm kiếm, logic, đồ thị và tối ưu hóa. Nó dạy một bài học AI lặp lại nhiều lần: **suy luận trước khi phân nhánh**. Lan truyền ràng buộc biến tri thức thành việc thu hẹp miền, giống như heuristic biến tri thức thành thứ tự ưu tiên tìm kiếm.

Xem tiếp: [Lập kế hoạch](./05_planning.md), nơi hành động có điều kiện trước và hiệu ứng, còn mục tiêu thường yêu cầu một chuỗi hành động thay vì chỉ một phép gán cuối cùng.