# Phương trình tốc độ — từ dữ liệu thực nghiệm tới quy luật động học

> **Phương trình tốc độ (rate law / 속도식)** mô tả tốc độ phản ứng phụ thuộc vào trạng thái hiện tại của hệ như thế nào. Nó là cầu nối giữa dữ liệu nồng độ–thời gian và cơ chế vi mô. Các số mũ trong phương trình tốc độ nói chung phải được xác định từ thực nghiệm hoặc suy ra từ một cơ chế đã được kiểm chứng; không thể đọc trực tiếp từ phương trình phản ứng tổng.

Nếu chương trước trả lời “tốc độ là gì?”, chương này trả lời câu hỏi quan trọng hơn: **khi nồng độ thay đổi, tốc độ thay đổi theo quy luật nào?**

## Dạng tổng quát

Một mô hình thực nghiệm đơn giản có thể là:

\[
r=k[A]^m[B]^n
\]

Trong đó:

- \(k\) là **hằng số tốc độ (rate constant / 속도 상수)**;
- \(m\) và \(n\) là **bậc phản ứng (reaction order / 반응 차수)** đối với từng chất;
- \(m+n\) là bậc tổng trong mô hình này.

Bậc phản ứng có thể bằng 0, số nguyên, phân số hoặc thậm chí thay đổi hiệu dụng theo vùng nồng độ nếu cơ chế phức tạp. Vì thế “bậc phản ứng” là một thuộc tính của **mô hình tốc độ dưới điều kiện đang xét**, không phải nhãn cố định gắn vĩnh viễn lên phương trình tổng.

## Vì sao hệ số phương trình tổng không tự cho bậc phản ứng?

Phương trình:

\[
2NO_2+F_2\rightarrow2NO_2F
\]

chỉ nói cân bằng nguyên tử tổng. Nó không cho biết các phân tử gặp nhau qua một bước hay nhiều bước.

Nếu phản ứng thật gồm nhiều bước, tốc độ có thể bị kiểm soát bởi một chất trung gian hoặc một bước không chứa tất cả chất phản ứng. Do đó một phương trình tốc độ kiểu:

\[
r=k[NO_2]^2[F_2]
\]

chỉ được suy trực tiếp từ hệ số khi phương trình đó thực sự là **bước cơ bản (elementary step)** phù hợp với định luật tác dụng khối lượng.

Đây là lý do kinetics cung cấp thông tin cơ chế mà stoichiometry không thể cung cấp.

## Ý nghĩa của bậc phản ứng

Nếu:

\[
r\propto[A]
\]

thì tăng \([A]\) gấp đôi làm tốc độ gần gấp đôi khi các yếu tố khác được giữ cố định.

Nếu:

\[
r\propto[A]^2
\]

thì tăng \([A]\) gấp đôi làm tốc độ gần tăng bốn lần.

Nếu:

\[
r\propto[A]^0
\]

thì trong vùng điều kiện đó, thay đổi \([A]\) không làm tốc độ thay đổi đáng kể.

Bậc 0 không có nghĩa A “không tham gia phản ứng”. Nó có thể nghĩa vị trí xúc tác đã bão hòa, photon là yếu tố giới hạn hoặc một bước khác đang kiểm soát tốc độ.

## Đơn vị của hằng số tốc độ

Tốc độ thường có đơn vị:

\[
mol\,L^{-1}s^{-1}
\]

Nếu bậc tổng là \(p\):

\[
[k]=(concentration)^{1-p}(time)^{-1}
\]

Do đó:

```text
bậc 0: mol L^-1 s^-1
bậc 1: s^-1
bậc 2: L mol^-1 s^-1
```

Đơn vị của \(k\) không phải chi tiết phụ; nó phản ánh cấu trúc toán học của rate law và giúp phát hiện lỗi mô hình.

# Ba cách chính để tìm phương trình tốc độ

## 1. Phương pháp tốc độ ban đầu

Ta thực hiện nhiều thí nghiệm, mỗi lần chỉ thay đổi có kiểm soát một hoặc vài nồng độ ban đầu.

Giả sử:

\[
r=k[A]^m[B]^n
\]

Hai thí nghiệm có cùng \([B]\), nhưng \([A]\) tăng gấp đôi và tốc độ tăng gấp bốn:

\[
\frac{r_2}{r_1}=\left(\frac{[A]_2}{[A]_1}\right)^m
\]

\[
4=2^m\Rightarrow m=2
\]

Nếu \([B]\) tăng gấp đôi nhưng tốc độ giữ gần như không đổi:

\[
2^n\approx1\Rightarrow n\approx0
\]

Ưu điểm của phương pháp tỉ số là \(k\) triệt tiêu. Nhược điểm là cần nhiều thí nghiệm được kiểm soát tốt và tốc độ ban đầu phải đo đáng tin cậy.

## 2. Theo dõi toàn bộ đường nồng độ–thời gian

Thay vì chỉ dùng vài độ dốc ban đầu, có thể fit toàn bộ trajectory vào nghiệm của phương trình vi phân.

Cách này tận dụng nhiều dữ liệu hơn và đặc biệt hữu ích khi nhiễu làm đạo hàm cục bộ không ổn định.

## 3. Dùng cơ chế để suy rate law

Nếu có một cơ chế đề xuất, ta viết tốc độ cho từng bước cơ bản rồi dùng xấp xỉ tiền cân bằng hoặc trạng thái ổn định để loại chất trung gian.

Rate law suy được sau đó phải được so với thực nghiệm. Nếu không khớp, cơ chế hoặc giả định cần được xem lại.

# Động học bậc không

Nếu:

\[
-\frac{d[A]}{dt}=k
\]

thì tích phân cho:

\[
[A]_t=[A]_0-kt
\]

Đường \([A]\) theo \(t\) là đường thẳng với slope \(-k\).

Thời gian bán hủy:

\[
t_{1/2}=\frac{[A]_0}{2k}
\]

phụ thuộc nồng độ ban đầu.

Bậc 0 thường xuất hiện khi một nguồn lực khác đã bão hòa, ví dụ bề mặt xúc tác kín hoặc cường độ ánh sáng giới hạn tốc độ quang hóa.

# Động học bậc nhất

Nếu:

\[
-\frac{d[A]}{dt}=k[A]
\]

chia hai vế cho \([A]\):

\[
\frac{d[A]}{[A]}=-kdt
\]

Tích phân từ \([A]_0\) tới \([A]_t\):

\[
\ln\frac{[A]_t}{[A]_0}=-kt
\]

hay:

\[
[A]_t=[A]_0e^{-kt}
\]

Đây là **suy giảm theo hàm mũ (exponential decay)**.

Thời gian bán hủy:

\[
t_{1/2}=\frac{\ln2}{k}
\]

không phụ thuộc \([A]_0\).

Chính tính chất này làm phân rã phóng xạ trở thành ví dụ rất rõ của động học bậc nhất.

## Vì sao hàm mũ xuất hiện?

Trong bậc nhất, mỗi phân tử có xác suất biến đổi gần như không đổi trên một đơn vị thời gian. Khi quần thể lớn, số phân tử mất đi mỗi giây tỉ lệ với số còn lại. Một quá trình “mất theo tỉ lệ phần trăm” tự nhiên tạo hàm mũ.

Logic tương tự xuất hiện trong phóng xạ, dược động học đơn giản, điện học RC và nhiều hệ thống suy giảm khác.

# Động học bậc hai

Trường hợp đơn giản:

\[
-\frac{d[A]}{dt}=k[A]^2
\]

cho:

\[
\frac1{[A]_t}=\frac1{[A]_0}+kt
\]

và:

\[
t_{1/2}=\frac1{k[A]_0}
\]

Thời gian bán hủy vì vậy phụ thuộc nồng độ ban đầu.

Với phản ứng hai chất khác nhau:

\[
A+B\rightarrow P
\]

\[
r=k[A][B]
\]

nghiệm tích phân có dạng khác nếu \([A]_0\ne[B]_0\). Đây là lời nhắc rằng “bậc hai” không đồng nghĩa chỉ có một công thức tích phân duy nhất.

# Động học giả bậc nhất

Giả sử:

\[
r=k[A][B]
\]

nhưng B được dùng dư rất lớn, nên trong khoảng thí nghiệm:

\[
[B]\approx[B]_0=constant
\]

Khi đó:

\[
r=k[B]_0[A]=k'[A]
\]

với:

\[
k'=k[B]_0
\]

Hệ biểu hiện **động học giả bậc nhất (pseudo-first-order kinetics)**.

Đây không phải “thay đổi bản chất” của bước phản ứng; nó là cách thiết kế thí nghiệm để biến một biến số gần như thành hằng số, giúp phân tích đơn giản hơn.

## Ví dụ hóa sinh

Nếu substrate dư rất lớn so với một chất phản ứng khác, một quá trình hai thành phần có thể biểu hiện gần bậc nhất theo thành phần đang được theo dõi. Logic tương tự xuất hiện trong nhiều assay và phản ứng thủy phân trong dung môi nước dư khổng lồ.

# Half-life như dấu vân tay động học

Sự phụ thuộc của \(t_{1/2}\) vào \([A]_0\) có thể giúp phân biệt mô hình:

```text
bậc 0: t1/2 ∝ [A]0
bậc 1: t1/2 không phụ thuộc [A]0
bậc 2: t1/2 ∝ 1/[A]0
```

Nhưng trong dữ liệu thật, cần nhiều nồng độ ban đầu và sai số đủ nhỏ để kết luận đáng tin cậy.

# Linearization — tiện nhưng có thể gây hiểu sai

Giáo trình thường kiểm tra:

```text
[A] vs t          → bậc 0
ln[A] vs t        → bậc 1
1/[A] vs t        → bậc 2
```

và chọn đồ thị “thẳng nhất”. Cách này hữu ích để học nhưng có hạn chế.

Biến đổi logarithm hoặc nghịch đảo làm thay đổi phân bố sai số. Ví dụ sai số đo nồng độ đồng đều trên thang gốc không còn đồng đều sau phép \(1/[A]\). Vì thế hồi quy tuyến tính trên dữ liệu đã biến đổi có thể tạo parameter bias.

Trong phân tích hiện đại, thường nên fit trực tiếp mô hình phi tuyến lên dữ liệu gốc và xem residuals.

# Không chọn mô hình chỉ bằng R²

Một đường có \(R^2\) cao không tự chứng minh đúng bậc phản ứng.

Cần hỏi:

- phần dư có cấu trúc hay không;
- parameter có ổn định qua nhiều nồng độ ban đầu không;
- mô hình dự đoán được dữ liệu mới không;
- cơ chế hóa học có hợp lý không;
- có thay đổi cơ chế theo conversion hay nhiệt độ không.

Đây là điểm giao giữa động học và **thẩm định mô hình (model validation)**.

# Khi bậc phản ứng không phải số nguyên

Bậc phân số có thể xuất hiện từ cơ chế nhiều bước, adsorption equilibrium hoặc steady-state intermediates.

Ví dụ nếu concentration của một intermediate tỉ lệ gần \([A]^{1/2}\), tốc độ phụ thuộc intermediate đó có thể dẫn tới bậc phân số theo A.

Do đó số mũ không nguyên là dấu hiệu rằng phương trình tốc độ đang “nén” nhiều bước vi mô thành một quan hệ hiệu dụng.

# Bậc âm

Một chất thậm chí có thể có bậc hiệu dụng âm nếu tăng nó làm tốc độ giảm.

Ví dụ một species có thể chiếm bề mặt xúc tác nhưng không phản ứng, cạnh tranh với reactant chính. Khi nồng độ species ức chế tăng, số vị trí hoạt động giảm và tốc độ có thể giảm.

Bậc âm vì thế không vi phạm vật lý; nó chỉ cho biết ảnh hưởng thực nghiệm của thành phần đó lên mạng cơ chế.

# Rate law và hoạt độ

Ở dung dịch loãng, thường dùng concentration:

\[
r=k[A]^m
\]

Nhưng về nguyên tắc, phản ứng phụ thuộc **hoạt độ (activity)** và chemical potential. Khi dung dịch đậm đặc hoặc ionic strength cao, concentration-based rate constant có thể thay đổi theo môi trường.

Điều này đặc biệt quan trọng với phản ứng ion vì tương tác điện tĩnh thay đổi khả năng hai ion tiếp cận trạng thái chuyển tiếp.

# Nhiệt độ phải được kiểm soát khi xác định rate law

Hằng số \(k\) phụ thuộc mạnh nhiệt độ. Nếu hai thí nghiệm “chỉ khác nồng độ” nhưng nhiệt độ thực khác vài độ, phần thay đổi tốc độ có thể bị gán nhầm cho reaction order.

Với phản ứng tỏa nhiệt mạnh, nhiệt độ trong mẫu còn có thể cao hơn bath temperature. Vì vậy kinetics tốt cần đo trạng thái thật của hệ, không chỉ setpoint thiết bị.

# Hệ phản ứng ghép và nghiệm số

Với mạng nhiều phản ứng:

\[
\frac{d\mathbf C}{dt}=S\mathbf r(\mathbf C,T,...)
\]

các nồng độ được nối qua hệ ODE phi tuyến. Khi không có nghiệm giải tích, ta dùng bộ giải số.

Mô hình có thể chứa hàng chục tới hàng nghìn species trong combustion, atmospheric chemistry hoặc metabolism. Khi đó “rate law” không còn là một công thức đơn mà là một vector hàm tốc độ.

# Stiff kinetics

Nếu một mạng có phản ứng rất nhanh và rất chậm đồng thời, hệ ODE có thể trở thành **cứng (stiff)**. Bộ giải số explicit thông thường phải dùng bước thời gian cực nhỏ để ổn định, dù ta quan tâm quá trình chậm hơn nhiều.

Các solver implicit như BDF được dùng trong nhiều software kinetics. Đây là ví dụ rất rõ cho việc kiến thức hóa học dẫn trực tiếp tới lựa chọn thuật toán trong khoa học máy tính.

# Parameter fitting và identifiability

Khi fit \(k\) từ dữ liệu, có hai câu hỏi khác nhau:

1. thuật toán có tìm được bộ parameter khớp dữ liệu không?
2. dữ liệu có chứa đủ thông tin để xác định duy nhất parameter đó không?

Nếu nhiều bộ \(k\) cho đường dự đoán gần như giống nhau, parameter có **khả năng nhận dạng kém (poor identifiability)**.

Thêm chữ số cho giá trị fit không giải quyết thiếu thông tin. Cần thiết kế thí nghiệm mới, thay đổi điều kiện hoặc đo thêm species.

# So sánh model bằng dự đoán, không chỉ bằng fit

Một rate law tốt nên giải thích được dữ liệu đã dùng để xây dựng **và** dự đoán được điều kiện mới trong phạm vi hợp lý.

Ví dụ, fit dữ liệu ở một nồng độ ban đầu rồi thử dự đoán trajectory ở nồng độ khác là kiểm tra mạnh hơn việc chỉ báo \(R^2\) trên cùng dataset.

# Những hiểu lầm thường gặp

### “Hệ số stoichiometric chính là reaction order”

Chỉ có thể suy như vậy cho một bước cơ bản phù hợp. Phương trình tổng không đủ thông tin.

### “Bậc nhất nghĩa phản ứng có một reactant”

Không. Bậc mô tả sự phụ thuộc toán học của tốc độ, không đếm số chất trong phương trình.

### “Đồ thị tuyến tính nhất chứng minh bậc phản ứng”

Không. Linearization có thể bóp méo sai số; cần residuals, kiểm chứng ngoài mẫu và logic cơ chế.

### “k là hằng số tuyệt đối của phản ứng”

\(k\) chỉ được xem là hằng trong điều kiện xác định. Nhiệt độ, dung môi, ionic strength và catalyst state có thể làm nó thay đổi.

### “Reaction order phải là số nguyên không âm”

Không. Mạng cơ chế có thể tạo bậc phân số, 0 hoặc âm.

## Mô hình tư duy

Phương trình tốc độ là **hàm chuyển trạng thái hóa học hiện tại thành độ dốc tiếp theo của hệ**:

```text
trạng thái hiện tại C(t)
→ rate law r(C,T,...)
→ dC/dt
→ trạng thái mới C(t+dt)
```

Dạng tích phân chỉ là quỹ đạo sinh ra khi quy tắc cục bộ đó được áp dụng liên tục. Khi cơ chế phức tạp, máy tính thực hiện quá trình tích phân này bằng solver số.

Xem tiếp: [Cơ chế phản ứng](./02_reaction_mechanisms.md) và [Ma trận hóa lượng và mạng phản ứng](../04_chemical_quantities/06_stoichiometric_matrices_and_reaction_networks.md).