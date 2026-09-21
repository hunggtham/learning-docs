# Tư duy Vật lý và tư duy từ nguyên lý đầu tiên (First-Principles Thinking)

Vật lý không bắt đầu từ việc nhớ công thức. Nó bắt đầu bằng việc quyết định **điều gì trong hiện tượng cần được giữ lại để tạo thành một mô hình có thể đo, tính và kiểm chứng**.

Một người học có thể biết rất nhiều công thức nhưng vẫn gặp khó khi bài toán thay đổi hình thức. Ngược lại, nếu hiểu cách chọn hệ, chọn biến, nhận ra thang chi phối, kiểm tra giới hạn và đánh giá giả định, ta có thể xây lại nhiều công thức từ những nguyên lý đơn giản hơn.

## Vật lý thực sự nghiên cứu điều gì?

Vật lý (Physics / 물리학) nghiên cứu các quy luật tổng quát chi phối vật chất, năng lượng, không gian, thời gian và tương tác. Điểm đặc trưng không nằm ở danh sách đối tượng, mà ở cách đặt câu hỏi: ta tìm một tập nhỏ các đại lượng có thể đo, xây dựng quan hệ toán học giữa chúng, rồi dùng quan hệ đó để dự đoán hiện tượng chưa được đo trực tiếp.

Nếu một quả bóng rơi, ta có thể mô tả màu sắc, vật liệu, âm thanh khi va đất, lịch sử người ném hoặc chuyển động của từng phân tử trong bóng. Nhưng nếu câu hỏi là “bao lâu thì bóng chạm đất?”, phần lớn thông tin đó không cần thiết. Chiều cao ban đầu, vận tốc ban đầu và trường hấp dẫn mới là các đại lượng chi phối ở mô hình đơn giản nhất.

Quá trình loại bỏ chi tiết không liên quan được gọi là **mô hình hóa (modeling / 모델링)**.

## Mô hình không phải hiện thực

Mô hình (model / 모형) là một biểu diễn có chủ đích của hiện thực. Khi nói “coi vật là chất điểm”, ta không tuyên bố vật thật không có kích thước. Ta chỉ nói rằng kích thước không ảnh hưởng đáng kể đến câu hỏi đang xét.

Tương tự, khi dùng các giả định như

```text
bỏ qua lực cản không khí
mặt phẳng không ma sát
dây không dãn
vật rắn tuyệt đối
khí lý tưởng
trường điện đều
ánh sáng là tia
```

ta đang xây một lớp mô hình đơn giản hơn để cô lập cơ chế chính.

Cùng một hệ vật lý có thể cần nhiều mô hình khác nhau. Một chiếc ô tô có thể là chất điểm trong bài đường đi, vật rắn có tâm khối trong bài lật xe, vật thể có hình học bề mặt trong khí động học và hệ nhiệt–cơ phức tạp trong bài động cơ.

> Một phương trình vật lý có thể được xem như một “hợp đồng”: nó cho dự đoán chính xác trong một miền điều kiện nhất định, đổi lại ta phải tôn trọng các giả định tạo nên nó.

## Bước đầu tiên: xác định hệ và ranh giới

Trước khi viết phương trình, hãy xác định **hệ (system / 계)** là gì và ranh giới của hệ nằm ở đâu.

Ví dụ với một viên bi rơi:

```text
hệ = viên bi
```

thì trọng lực là ngoại lực.

Nếu chọn

```text
hệ = viên bi + Trái Đất
```

thì tương tác hấp dẫn nằm bên trong hệ và có thể được mô tả bằng thế năng hấp dẫn.

Hai cách chọn đều hợp lệ, nhưng chúng dẫn tới cách viết phương trình và định luật bảo toàn khác nhau.

Đây là lý do các câu như “động lượng có bảo toàn không?” hoặc “năng lượng có bảo toàn không?” không thể trả lời chính xác nếu chưa biết ranh giới hệ và những gì đi qua ranh giới đó.

## Chọn biến trạng thái và bậc tự do

Sau khi chọn hệ, cần xác định những biến nào thực sự cần để mô tả trạng thái.

Một chất điểm trong không gian ba chiều có thể cần

```math
\mathbf r(t),\qquad \mathbf v(t).
```

Một con lắc đơn lý tưởng chỉ cần một góc

```math
\theta(t).
```

Một lượng khí cân bằng có thể được mô tả bằng

```math
P,\quad V,\quad T,\quad N.
```

Một trường nhiệt độ cần một hàm

```math
T(\mathbf r,t).
```

Số lượng biến độc lập cần thiết được liên hệ với **bậc tự do (degrees of freedom / 자유도)**.

Chọn quá nhiều biến làm mô hình nặng mà không tăng khả năng dự đoán. Chọn quá ít biến có thể làm mất cơ chế quan trọng. Mô hình hóa tốt là tìm mức mô tả vừa đủ cho câu hỏi.

## Từ hiện tượng đến câu hỏi đo được

Một câu hỏi đời thường thường quá mơ hồ để trở thành bài toán vật lý.

Ví dụ:

```text
“Chiếc xe này nhanh không?”
```

có thể được chuyển thành các câu hỏi định lượng hơn:

```text
vận tốc cực đại là bao nhiêu?
0 → 100 km/h mất bao lâu?
gia tốc cực đại là bao nhiêu?
quãng đường phanh từ 100 km/h là bao nhiêu?
```

Mỗi câu hỏi dẫn tới một mô hình khác.

Một quy trình hữu ích là

```text
hiện tượng
→ câu hỏi có thể kiểm chứng
→ hệ và ranh giới
→ biến trạng thái
→ giả định
→ định luật chi phối
→ dự đoán
→ phép đo
→ so sánh
```

Nếu dự đoán không phù hợp dữ liệu, cần kiểm tra cả ba lớp:

```text
phép tính
mô hình
phép đo
```

Không nên mặc định mọi sai khác đều do tính toán sai.

## Từ nguyên lý đầu tiên nghĩa là gì?

Tư duy từ nguyên lý đầu tiên (first-principles thinking) không có nghĩa là lúc nào cũng phải bắt đầu từ lý thuyết cơ bản nhất của tự nhiên như Mô hình Chuẩn.

Trong một bài cơ học, “nguyên lý đầu tiên” thích hợp có thể là

```math
\sum \mathbf F=\frac{d\mathbf p}{dt}.
```

Trong bài nhiệt động lực học, có thể là bảo toàn năng lượng và entropy.

Trong điện từ học, có thể là các phương trình Maxwell.

Trong lượng tử không tương đối tính, có thể là cấu trúc trạng thái cùng phương trình Schrödinger.

Điểm cốt lõi là: thay vì nhớ một công thức chuyên biệt cho mỗi tình huống, ta cố truy nó về một tập nguyên lý tổng quát hơn và các giả định đã dùng để suy ra công thức đó.

## Định luật vật lý và quan hệ nhân quả

Định luật vật lý (physical law / 물리 법칙) là quan hệ tổng quát đã được kiểm chứng thực nghiệm trong một miền áp dụng.

“Định luật” không có nghĩa là một chân lý siêu hình không thể được thay thế. Cơ học Newton cực kỳ chính xác khi

```math
v\ll c
```

và các hiệu ứng lượng tử không quan trọng. Khi ra ngoài miền đó, thuyết tương đối hoặc cơ học lượng tử trở nên cần thiết.

Lý thuyết mới thường không xóa hoàn toàn lý thuyết cũ. Nó phải khôi phục lý thuyết cũ trong giới hạn thích hợp. Đây gọi là **nguyên lý tương ứng (correspondence principle)** theo nghĩa rộng.

Ví dụ:

```text
thuyết tương đối → cơ học Newton khi v/c → 0
quang học sóng → quang hình học khi λ/L → 0
cơ học lượng tử → hành vi cổ điển trong các giới hạn thích hợp
```

Kiểm tra giới hạn là một trong những công cụ mạnh nhất để phát hiện công thức sai.

## Phân biệt mô tả với giải thích cơ chế

Một phương trình có thể mô tả dữ liệu rất tốt mà chưa chắc đã cho cơ chế cơ bản nhất.

Ví dụ định luật Hooke

```math
F=-kx
```

mô tả rất tốt nhiều vật đàn hồi gần cân bằng. Nhưng nó không nói chi tiết liên kết nguyên tử nào tạo ra độ cứng `k`.

Ở cấp sâu hơn, cơ học vật liệu và vật lý chất rắn giải thích nguồn gốc vi mô của đáp ứng đàn hồi.

Vì vậy nên phân biệt:

```text
mô hình hiện tượng (phenomenological model)
```

và

```text
mô hình cơ chế (mechanistic model)
```

Cả hai đều hữu ích. Mức mô tả nào cần dùng phụ thuộc câu hỏi.

## Phân tích thang đo trước khi giải

Mỗi bài toán có các thang đặc trưng về chiều dài, thời gian, năng lượng hoặc vận tốc.

Ví dụ:

```math
L,\qquad \tau,\qquad E,\qquad v.
```

So sánh chúng với các thang đặc trưng khác thường cho biết mô hình nào phù hợp.

Nếu

```math
\frac{v}{c}\ll1,
```

ta thường chưa cần tương đối tính.

Nếu bước sóng `\lambda` rất nhỏ so với kích thước hình học `L`,

```math
\frac{\lambda}{L}\ll1,
```

quang hình học có thể đủ tốt.

Trong chất lưu, số Reynolds

```math
Re=\frac{\rho vL}{\mu}
```

so sánh quán tính với độ nhớt.

Tư duy theo **tỉ số vô thứ nguyên (dimensionless ratio)** tốt hơn các nhận xét mơ hồ như “vận tốc khá nhỏ” hoặc “vật khá lớn”.

## Ước lượng bậc độ lớn

Trước khi làm phép tính chính xác, nên ước lượng kết quả ở bậc độ lớn (order of magnitude).

Nếu tính vận tốc của ô tô và nhận được

```math
10^6\;m/s,
```

thì sai lệch không còn là vấn đề làm tròn số. Hoặc mô hình, hoặc đơn vị, hoặc phép biến đổi đại số đã có vấn đề.

Ước lượng kiểu Fermi chia một câu hỏi khó thành các yếu tố dễ ước lượng hơn. Trong khoa học và kỹ thuật, khả năng nhận ra “kết quả này không thể đúng về mặt quy mô” rất quan trọng.

## Phân tích thứ nguyên như một bộ kiểm tra logic

Một phương trình vật lý phải nhất quán về thứ nguyên.

Nếu

```math
x=v_0t+\frac12at^2,
```

thì cả ba hạng đều phải có đơn vị chiều dài.

Phân tích thứ nguyên không chứng minh một phương trình đúng, nhưng có thể chứng minh nhiều phương trình là sai.

Nó còn có thể gợi ý dạng của kết quả. Nếu chu kỳ con lắc chỉ phụ thuộc chiều dài `L` và gia tốc `g`, tổ hợp có thứ nguyên thời gian là

```math
\sqrt{\frac{L}{g}}.
```

Do đó trước khi giải chi tiết, ta đã biết

```math
T\propto\sqrt{\frac{L}{g}}.
```

Hệ số `2\pi` cần mô hình động lực học để xác định.

## Xấp xỉ phải có tham số kiểm soát

Một xấp xỉ tốt không nên chỉ dựa vào cảm giác.

Ví dụ

```math
\sin\theta\approx\theta
```

được kiểm soát bởi điều kiện

```math
|\theta|\ll1
```

khi `\theta` đo bằng radian.

Khai triển Taylor cho

```math
\sin\theta=\theta-\frac{\theta^3}{6}+\cdots
```

cho ta biết luôn hạng sai số đầu tiên bị bỏ qua.

Do đó khi dùng xấp xỉ, hãy hỏi:

```text
tham số nhỏ là gì?
sai số đầu tiên có bậc nào?
nghiệm cuối có còn nằm trong miền xấp xỉ ban đầu không?
```

Câu hỏi cuối rất quan trọng. Một phép giải có thể bắt đầu với giả định “góc nhỏ” nhưng cho nghiệm góc lớn; khi đó mô hình tự mâu thuẫn.

## Điều kiện đầu và điều kiện biên là một phần của mô hình

Phương trình chi phối thường chưa đủ để xác định nghiệm.

Ví dụ phương trình dao động

```math
\ddot x+\omega^2x=0
```

có vô số nghiệm. Muốn xác định quỹ đạo cụ thể cần các điều kiện đầu như

```math
x(0),\qquad \dot x(0).
```

Với phương trình trường, điều kiện biên (boundary conditions / 경계조건) có thể quyết định cấu trúc nghiệm.

Cùng phương trình Laplace có thể tạo các điện thế hoàn toàn khác nhau tùy điện thế hoặc điện tích đặt trên biên.

Do đó một bài toán vật lý đầy đủ thường gồm

```text
phương trình chi phối
+ điều kiện đầu
+ điều kiện biên
+ tham số vật liệu
+ hình học
```

## Bài toán thuận và bài toán ngược

Bài toán thuận (forward problem) đi từ mô hình tới dự đoán:

```text
tham số
→ phương trình
→ nghiệm
→ đại lượng quan sát được
```

Bài toán ngược (inverse problem) đi từ dữ liệu trở lại tham số:

```text
dữ liệu đo
→ suy ra tham số hoặc cấu trúc nguồn
```

Ví dụ, từ quang phổ của sao ta suy ra nhiệt độ, thành phần hóa học và vận tốc. Từ tín hiệu detector ta suy ra thuộc tính của hệ đã tạo tín hiệu.

Bài toán ngược thường khó hơn vì nhiều mô hình khác nhau có thể tạo dữ liệu gần giống nhau. Vì vậy **identifiability**, uncertainty và prior assumptions trở nên quan trọng.

Đây là cầu nối trực tiếp giữa Vật lý, thống kê, khoa học dữ liệu và Machine Learning.

## Mô hình phải tạo được dự đoán có thể kiểm tra

Một mô hình khoa học mạnh không chỉ giải thích dữ liệu đã biết; nó cần tạo ra hệ quả mà phép đo có thể kiểm tra.

Quy trình lý tưởng là

```text
model
→ prediction
→ measurement
→ residual
→ model revision
```

Nếu ta thay đổi mô hình mỗi lần có dữ liệu mới mà không để lại khả năng bị bác bỏ, mô hình sẽ mất sức mạnh kiểm chứng.

Điều này liên quan tới tính khả kiểm (falsifiability), nhưng trong thực hành khoa học hiện đại cần tinh tế hơn: dữ liệu không bao giờ hoàn hảo, mô hình thường gần đúng và phép đo có uncertainty. Vì vậy ta đánh giá mức phù hợp định lượng, không chỉ hỏi “đúng hay sai tuyệt đối”.

## Sai số mô hình khác sai số đo

Nếu dự đoán khác dữ liệu, ít nhất ba nguồn cần được tách:

```text
measurement uncertainty
numerical error
model discrepancy
```

Độ bất định đo đến từ detector, hiệu chuẩn và sampling.

Sai số số học đến từ rời rạc hóa, finite precision hoặc solver.

Sai lệch mô hình đến từ việc giả định vật lý chưa đủ, chẳng hạn bỏ qua ma sát, dùng khí lý tưởng ngoài miền phù hợp hoặc dùng continuum ở thang quá nhỏ.

Tăng độ chính xác của máy đo không tự sửa một mô hình sai.

## Emergence và coarse-graining

Vật lý hoạt động ở nhiều cấp mô tả.

Một phân tử nước tuân theo cơ học lượng tử, nhưng dòng nước trong đường ống được mô tả tốt bằng các trường

```math
\rho(\mathbf r,t),\qquad \mathbf v(\mathbf r,t),\qquad P(\mathbf r,t).
```

Nhiệt độ không phải thuộc tính đầy đủ của một phân tử đơn lẻ; nó là đại lượng vĩ mô của một tập hợp rất lớn các bậc tự do vi mô.

Việc chuyển từ chi tiết vi mô sang các biến tập thể được gọi là **coarse-graining**. Các quy luật hiệu dụng xuất hiện ở thang lớn hơn được gọi là hiện tượng nổi lên (emergence / 창발).

Điều này liên hệ mạnh với Chemistry, Materials Science và Computer Science: cùng một hệ có thể cần các abstraction khác nhau ở các thang khác nhau.

## Liên hệ với Toán học

Toán học cung cấp cấu trúc biểu diễn cho Vật lý:

```text
đạo hàm → tốc độ biến thiên
integral → cộng dồn
vector → đại lượng có hướng
matrix/eigenvalue → mode tự nhiên
PDE → trường liên tục
probability → hệ có bất định hoặc nhiều trạng thái khả dĩ
```

Nhưng một biểu thức toán học chỉ trở thành phát biểu vật lý khi ta gắn cho biến ý nghĩa, đơn vị, miền áp dụng và quy tắc đo.

Cùng một phương trình vi phân có thể xuất hiện trong nhiều hệ hoàn toàn khác nhau; sự giống nhau nằm ở cấu trúc toán học, không có nghĩa các hệ có cùng bản chất vật lý.

## Liên hệ với Chemistry và Materials Science

Hóa học thường bắt đầu ở cấp nguyên tử–phân tử nơi cơ học lượng tử quyết định orbital, liên kết và phổ năng lượng.

Ở cấp vật liệu, cấu trúc vi mô tạo ra tính chất hiệu dụng như

```text
độ đàn hồi
độ dẫn điện
độ dẫn nhiệt
hằng số điện môi
độ từ thẩm
```

Vì vậy một tham số xuất hiện trong phương trình vĩ mô thường là kết quả nén của rất nhiều physics ở cấp thấp hơn.

## Liên hệ với Engineering

Engineering không chỉ dùng phương trình vật lý; nó còn đặt thêm ràng buộc:

```text
an toàn
chi phí
độ bền
hiệu suất
manufacturability
control
reliability
```

Một mô hình đủ tốt cho nghiên cứu định tính có thể chưa đủ tốt cho thiết kế kỹ thuật nếu sai số nhỏ gây hậu quả lớn.

Do đó kỹ thuật thường yêu cầu thêm safety factor, tolerance analysis, uncertainty propagation và validation với dữ liệu thực.

## Liên hệ với Computer Science

Mô phỏng vật lý có chuỗi abstraction:

```text
hệ thật
→ mô hình vật lý
→ phương trình toán học
→ rời rạc hóa
→ thuật toán
→ mã nguồn
→ kết quả số
```

Mỗi lớp có thể sinh lỗi riêng.

Một chương trình chạy thành công chỉ chứng minh rằng máy tính đã thực thi thuật toán; nó không tự chứng minh rằng thuật toán giải đúng phương trình hay phương trình mô tả đúng hệ thật.

Đây là lý do version control, testing, reproducibility và numerical validation cũng là một phần của vật lý tính toán hiện đại.

## Quy trình first-principles có thể tái sử dụng

Khi gặp một hiện tượng mới, có thể đi theo chuỗi câu hỏi sau:

1. Hệ là gì và ranh giới ở đâu?
2. Đại lượng nào có thể đo?
3. Bậc tự do nào cần giữ lại?
4. Thang chiều dài, thời gian, năng lượng và vận tốc nào chi phối?
5. Có đối xứng hoặc định luật bảo toàn nào không?
6. Lực, trường hoặc tương tác nào quan trọng?
7. Hiệu ứng nào nhỏ đến mức có thể bỏ qua?
8. Phương trình chi phối là gì?
9. Điều kiện đầu và điều kiện biên là gì?
10. Kết quả có đúng đơn vị và bậc độ lớn không?
11. Khi đưa tham số về giới hạn đơn giản, nghiệm có hợp lý không?
12. Đại lượng nào có thể đo để kiểm tra dự đoán?
13. Nếu dữ liệu không khớp, lỗi nằm ở measurement, numerics hay model?

Đây không phải checklist phải thực hiện máy móc cho mọi bài đơn giản. Nó là khung tư duy để tránh nhảy trực tiếp từ đề bài sang công thức.

## Mô hình tư duy (Mental Model)

Một cách cô đọng để nhìn toàn bộ Vật lý là

```text
hiện thực
→ chọn hệ
→ chọn biến
→ đặt giả định
→ xây mô hình
→ suy ra dự đoán
→ đo
→ so sánh
→ sửa mô hình
```

Mục tiêu không phải tạo mô hình chứa mọi chi tiết. Mục tiêu là tạo **mô hình đơn giản nhất vẫn giữ đúng cơ chế cần thiết cho câu hỏi hiện tại**, đồng thời biết rõ khi nào mô hình đó hết hiệu lực.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Mô hình đơn giản là mô hình sai”

Không. Mô hình đơn giản có thể cực kỳ chính xác trong miền phù hợp. Điều quan trọng là biết giả định nào đã được dùng.

### “Lý thuyết mới làm lý thuyết cũ trở thành vô dụng”

Không. Lý thuyết cũ thường vẫn là xấp xỉ tốt trong miền mà nó được xây dựng.

### “Càng dùng lý thuyết cơ bản hơn thì kết quả càng tốt”

Không nhất thiết. Mô tả một cây cầu bằng QCD là không thực tế và không giúp giải bài cơ học kết cấu. Mô hình đúng thang quan trọng hơn mô hình vi mô nhất.

### “Dữ liệu khớp tốt thì mô hình chắc chắn đúng”

Không. Nhiều mô hình có thể khớp cùng một tập dữ liệu hữu hạn. Cần kiểm tra dự đoán mới, residual, uncertainty và khả năng phân biệt mô hình.

### “Máy tính cho nhiều chữ số nghĩa là kết quả chính xác”

Không. Precision số học khác với accuracy vật lý. Một mô hình sai có thể được tính với mười lăm chữ số.

## Liên kết kiến thức (Knowledge Connection)

**Liên hệ tiếp:** [Phép đo, đơn vị và độ bất định](01_measurement_units_uncertainty.md), [Ngôn ngữ Toán học](03_mathematical_language.md), [Đối xứng, bảo toàn và thang đo](04_symmetry_conservation_scale.md).

**Đi sâu hơn:** [PDE, điều kiện biên, Green function và tensor](05_pde_boundary_green_tensors.md), [Vật lý thực nghiệm](../12_experimental_computational/00_measurement_experiment.md), [Vật lý tính toán](../12_experimental_computational/02_computational_physics.md), [Suy luận dữ liệu và bài toán ngược](../12_experimental_computational/03_data_inference_inverse_problems.md).
