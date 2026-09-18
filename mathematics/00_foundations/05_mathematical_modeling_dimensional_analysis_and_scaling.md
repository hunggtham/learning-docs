# Mô hình toán học, phân tích thứ nguyên và scaling

Toán học trở nên hữu ích khi ta biến một vấn đề trong thế giới thật thành một cấu trúc có thể suy luận. Quá trình đó gọi là **mô hình hóa toán học (Mathematical Modeling / 수학적 모델링)**. Một mô hình không phải bản sao hoàn hảo của thực tế. Nó là một lựa chọn có chủ đích: giữ lại những đại lượng và quan hệ quan trọng cho câu hỏi đang hỏi, đồng thời bỏ qua những chi tiết chưa cần thiết.

Nếu hỏi “một chiếc xe mất bao lâu để đi 120 km?”, ta có thể bắt đầu với mô hình cực đơn giản `distance = speed × time`. Nhưng nếu tốc độ thay đổi, đường có đèn đỏ, xe dừng nghỉ hoặc GPS đo sai, mô hình đó không còn đủ. Điều quan trọng không phải tìm một công thức “đúng tuyệt đối”, mà là biết assumption nào khiến mô hình hợp lý và khi nào cần thay mô hình.

## Từ hiện tượng đến biến số

Bước đầu tiên của modeling là xác định **biến (Variable / 변수)**, **tham số (Parameter / 매개변수)** và **ràng buộc (Constraint / 제약조건)**. Biến là đại lượng có thể thay đổi trong bài toán. Tham số thường được xem như cố định trong một lần chạy mô hình nhưng có thể thay đổi giữa các trường hợp. Constraint xác định những trạng thái được phép.

Ví dụ với quãng đường `d`, vận tốc `v` và thời gian `t`, quan hệ lý tưởng là

```math
d=vt.
```

Nếu `v` được xem là tốc độ trung bình đã biết, `t` là unknown cần tìm và `d` là dữ liệu đầu vào, thì `v` đang đóng vai trò parameter. Nhưng trong mô hình khác, `v(t)` lại là một function thay đổi theo thời gian. Cùng một ký hiệu không quyết định vai trò; câu hỏi và mô hình quyết định.

## Đơn vị là một phần của toán học, không phải nhãn trang trí

**Thứ nguyên (Dimension / 차원)** mô tả loại đại lượng vật lý: chiều dài `[L]`, thời gian `[T]`, khối lượng `[M]` và các combination của chúng. **Đơn vị (Unit / 단위)** là cách cụ thể để đo thứ nguyên đó: mét, kilomet, giây, giờ, kilogram.

Vận tốc có dimension

```math
[L][T]^{-1}
```

vì nó là distance chia cho time. Gia tốc có dimension

```math
[L][T]^{-2}.
```

Một phương trình vật lý hợp lệ phải **đồng nhất thứ nguyên (Dimensionally Consistent / 차원 일관성)**. Chẳng hạn

```math
d=vt
```

có vế phải mang dimension

```math
[L][T]^{-1}[T]=[L],
```

khớp với distance. Nếu ai đó viết `d=v+t`, biểu thức đó đã đáng nghi trước khi cần thay số, vì không thể cộng một velocity với một time như hai đại lượng cùng loại.

> Dimensional analysis là một type checker cho các mô hình định lượng. Nó không chứng minh công thức đúng, nhưng có thể loại bỏ rất nhiều công thức sai ngay lập tức.

Trong programming, mental model này gần với type systems. Cộng `LocalDate` với `BigDecimal` vô nghĩa không phải vì compiler “khó tính”, mà vì hai object biểu diễn hai loại quantity khác nhau. Các thư viện units-of-measure cố đưa chính tư tưởng dimensional consistency vào code.

## Dimensionless quantity và vì sao ratio mạnh đến vậy

Một đại lượng **không thứ nguyên (Dimensionless Quantity / 무차원량)** xuất hiện khi units triệt tiêu. Ví dụ strain trong mechanics là `ΔL/L`; probability là ratio; percentage là ratio nhân 100; cosine là ratio giữa lengths trong tam giác đồng dạng.

Dimensionless quantities đặc biệt quan trọng vì chúng dễ so sánh giữa systems có scale khác nhau. Một chiếc mô hình dài 10 cm và một cây cầu dài 100 m có thể chia sẻ một số dimensionless ratios dù kích thước tuyệt đối khác nhau. Engineering thường dùng các dimensionless numbers để xác định khi hai hệ thống có behavior tương tự.

## Scaling: nếu kích thước tăng gấp đôi thì điều gì thực sự thay đổi?

**Scaling / 스케일링** nghiên cứu cách một quantity thay đổi khi characteristic size thay đổi. Với một hình vuông cạnh `s`, perimeter tăng theo `s`, còn area tăng theo `s^2`:

```math
P=4s,
\qquad
A=s^2.
```

Nếu cạnh tăng gấp 2, perimeter tăng gấp 2 nhưng area tăng gấp 4. Với vật thể ba chiều, volume thường scale như `s^3`.

Điều này giải thích nhiều hiện tượng đời sống. Một animal lớn hơn không chỉ là animal nhỏ “phóng to”. Surface area và volume tăng theo powers khác nhau, nên heat loss, structural stress và metabolic constraints thay đổi. Trong software, scaling cũng xuất hiện theo cách tương tự: nếu một algorithm so sánh mọi pair trong `n` records, work scale gần `n^2`; doubling input có thể làm work tăng khoảng bốn lần.

## Order of magnitude và ước lượng Fermi

Trong nhiều tình huống, exact data không có sẵn. **Ước lượng bậc độ lớn (Order-of-Magnitude Estimate / 자릿수 규모 추정)** hỏi quantity nằm khoảng `10^2`, `10^3` hay `10^6`, thay vì đòi decimal chính xác giả tạo.

Một **Fermi estimate / 페르미 추정** phân rã câu hỏi lớn thành các factors dễ ước lượng hơn. Muốn ước lượng bao nhiêu ly cà phê được bán ở một quận mỗi ngày, ta có thể model:

```math
\text{population}
\times
\text{fraction buying coffee}
\times
\text{cups per buyer per day}.
```

Mỗi factor có uncertainty, nhưng product vẫn có thể cho scale đủ tốt để kiểm tra feasibility hoặc detect một con số vô lý.

Đây cũng là kỹ năng quan trọng khi review system design. Nếu một service có 2 triệu users, mỗi user tạo 20 requests/ngày, traffic trung bình là khoảng

```math
\frac{2\times10^6\times20}{86400}
\approx 463\ \text{requests/s}.
```

Peak traffic có thể cao hơn nhiều, nhưng phép tính thô giúp ta biết mình đang nói về vài trăm, vài nghìn hay vài triệu requests/s.

## Sensitivity: kết quả nhạy đến assumption nào?

Một model thường phụ thuộc vào parameters `p_1,p_2,...`. **Phân tích độ nhạy (Sensitivity Analysis / 민감도 분석)** hỏi kết quả thay đổi bao nhiêu khi một parameter thay đổi.

Nếu

```math
R=pq,
```

thì small relative changes gần thỏa

```math
\frac{\Delta R}{R}
\approx
\frac{\Delta p}{p}+\frac{\Delta q}{q}.
```

Điều này cho thấy uncertainty tương đối có xu hướng cộng trong product ở first-order approximation. Trong business model, một forecast revenue có thể phụ thuộc vào traffic, conversion rate và average order value. Nếu conclusion chỉ đúng khi conversion rate chính xác đến 0.01%, model rất fragile.

Sensitivity nối trực tiếp với derivatives: derivative chính là local sensitivity. Với function `y=f(x)`, quantity

```math
\frac{dy}{dx}
```

cho biết output phản ứng local mạnh đến mức nào trước thay đổi input.

## Model validation và residual

Sau khi dựng model, ta phải so sánh prediction với observation. Difference giữa observed value `y_i` và prediction `\hat y_i` thường gọi là **residual / 잔차**:

```math
r_i=y_i-\hat y_i.
```

Residual không chỉ là “error cần giảm”. Pattern trong residual có thể cho thấy assumption sai. Nếu residual tăng dần theo time, model có thể đang thiếu trend. Nếu variance của residual tăng cùng magnitude, noise có thể không homoscedastic. Statistics và machine learning phát triển phần lớn từ chính câu hỏi: làm sao đánh giá model khi data chứa uncertainty?

## Assumption, approximation và domain of validity

Một approximation không phải false statement. Nó là statement đúng trong một regime nhất định. Ví dụ với `x` nhỏ,

```math
\sin x\approx x
```

khi `x` đo bằng radian. Đây là local approximation xuất phát từ Taylor series. Nếu `x=0.01`, approximation rất tốt; nếu `x=2`, nó không còn tốt. Vấn đề không phải “approximation sai”, mà là đã dùng ngoài domain of validity.

Khi đọc bất kỳ model nào, nên hỏi ba câu: what is being ignored, what scale are we operating at, and which variables are treated as independent even though reality may couple them?

## Knowledge Connection

Modeling là nơi nhiều nhánh Toán gặp nhau. Algebra biểu diễn relationships; functions biến inputs thành outputs; calculus đo sensitivity và dynamics; probability biểu diễn uncertainty; statistics kiểm tra model bằng data; optimization chọn parameters; numerical mathematics tính approximation trên máy tính.

Trong machine learning, một neural network là một parameterized function family. Training là optimization; loss là objective; regularization là constraint/penalty; validation kiểm tra khả năng generalize. Trong finance, discounted cash-flow model biến assumptions về future cash flow và discount rate thành present value. Trong physics, differential equations model laws of change. Những trường hợp này khác domain nhưng cùng một mental structure.

## Mental Model

> Một mathematical model là một “máy suy luận có điều kiện”: nếu các assumptions và relationships ta chọn đủ phù hợp với câu hỏi, model cho phép biến dữ liệu đầu vào thành prediction hoặc decision. Dimensional analysis kiểm tra model có nói đúng loại quantity; scaling cho biết điều gì xảy ra khi kích thước thay đổi; sensitivity cho biết assumption nào thực sự chi phối kết quả.

## Common Misconceptions

Mô hình phức tạp hơn không tự động tốt hơn. Complexity chỉ hữu ích nếu nó mô tả structure cần cho câu hỏi và được data hỗ trợ. Một model đơn giản với assumptions rõ có thể đáng tin hơn model rất nhiều parameters nhưng không validate được.

Dimensional consistency cũng không chứng minh công thức đúng. `d=vt` và `d=2vt` đều dimensionally consistent, nhưng coefficient và relationship phải đến từ reasoning hoặc evidence khác.

Cuối cùng, precision không đồng nghĩa accuracy. Viết `12.384729%` từ những assumptions chỉ chính xác khoảng 10% là false precision. Số chữ số phải phản ánh uncertainty của model, không phải khả năng máy tính in nhiều decimal places.
