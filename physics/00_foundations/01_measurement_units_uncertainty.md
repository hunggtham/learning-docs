# Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường

## Phép đo là cầu nối giữa mô hình và thế giới

Vật lý không chỉ xây phương trình; nó phải nối phương trình với đại lượng có thể đo. Một đại lượng vật lý (physical quantity / 물리량) là thuộc tính được định nghĩa đủ rõ để so sánh định lượng, chẳng hạn chiều dài, thời gian, khối lượng, điện tích và nhiệt độ.

Một kết quả đo không chỉ là một con số. Nó phải đi cùng:

- đại lượng đang đo;
- đơn vị;
- quy trình hoặc mô hình đo;
- độ bất định;
- điều kiện đo khi cần.

Viết `5` gần như không có ý nghĩa vật lý. Viết `5.00 ± 0.03 m` đã mang nhiều thông tin hơn: giá trị ước lượng, đơn vị và mức bất định.

## Hệ SI và đại lượng dẫn xuất

Hệ SI (International System of Units / 국제단위계) có bảy đơn vị cơ bản:

```text
m, s, kg, A, K, mol, cd
```

Các đơn vị khác được xây từ chúng.

Ví dụ lực có đơn vị

```math
1\,N=1\,kg\cdot m/s^2.
```

Năng lượng có đơn vị

```math
1\,J=1\,N\cdot m
=1\,kg\cdot m^2/s^2.
```

Viết đơn vị dưới dạng cơ bản giúp kiểm tra công thức và hiểu cấu trúc của đại lượng.

## Thứ nguyên: hệ kiểu của phương trình vật lý

Thứ nguyên (dimension / 차원) không phụ thuộc việc ta dùng mét hay centimet.

Ta ký hiệu

```math
[x]=L,
```

```math
[t]=T,
```

```math
[m]=M.
```

Vận tốc có

```math
[v]=LT^{-1},
```

và gia tốc có

```math
[a]=LT^{-2}.
```

Nếu viết

```math
x=v+at,
```

vế trái có thứ nguyên chiều dài, còn cả hai hạng bên phải có thứ nguyên vận tốc. Phương trình chắc chắn sai trước khi ta thay bất kỳ con số nào.

Có thể xem phân tích thứ nguyên giống type system trong lập trình: nó không chứng minh thuật toán đúng, nhưng loại được cả một lớp lỗi cấu trúc.

## Nguyên tắc đồng nhất thứ nguyên

Trong một phương trình vật lý hợp lệ:

1. hai vế phải cùng thứ nguyên;
2. các hạng được cộng hoặc trừ phải cùng thứ nguyên;
3. đối số của `sin`, `cos`, `exp`, `log` phải vô thứ nguyên.

Ví dụ biểu thức

```math
e^{-t/\tau}
```

hợp lệ vì `t/\tau` vô thứ nguyên.

Biểu thức

```math
e^{-3t}
```

chỉ có ý nghĩa nếu hệ số `3` thực ra mang đơn vị nghịch đảo thời gian.

## Phân tích thứ nguyên có thể dự đoán dạng công thức

Xét chu kỳ con lắc nhỏ phụ thuộc chiều dài `L` và gia tốc `g`.

Giả sử

```math
T\propto L^ag^b.
```

Thứ nguyên cho

```math
[T]=[L]^a[LT^{-2}]^b
=L^{a+b}T^{-2b}.
```

So sánh số mũ:

```math
-2b=1,
```

```math
a+b=0.
```

suy ra

```math
b=-\frac12,
\qquad
a=\frac12.
```

Do đó

```math
T\propto\sqrt{\frac{L}{g}}.
```

Phân tích thứ nguyên không tìm được hệ số `2\pi`, nhưng loại bỏ rất nhiều dạng sai và cho cấu trúc scaling trước khi giải chi tiết.

## Accuracy, precision và resolution

Ba khái niệm này khác nhau.

**Độ đúng (accuracy / 정확도)** mô tả kết quả gần giá trị tham chiếu đúng đến đâu.

**Độ chụm (precision / 정밀도)** mô tả các phép đo lặp lại gần nhau đến đâu.

**Độ phân giải (resolution)** là thay đổi nhỏ nhất thiết bị có thể phân biệt hoặc hiển thị.

Một cân có thể hiển thị tới `0.001 kg` nhưng bị lệch chuẩn `0.2 kg`. Khi đó độ phân giải tốt nhưng accuracy kém.

## Sai số ngẫu nhiên và sai số hệ thống

Sai số ngẫu nhiên làm kết quả dao động giữa các lần đo. Lặp phép đo và lấy trung bình có thể giảm uncertainty của giá trị trung bình nếu các mẫu đủ độc lập.

Sai số hệ thống làm kết quả bị lệch theo một hướng, ví dụ:

- zero offset;
- scale factor sai;
- cảm biến phụ thuộc nhiệt độ nhưng không được hiệu chỉnh;
- phương pháp đo bỏ qua một hiệu ứng vật lý.

Lặp lại cùng một phép đo rất nhiều lần không tự loại bỏ systematic bias.

## Độ bất định không phải “sai số đã biết”

Ta thường viết

```math
x=\hat x\pm u_x,
```

trong đó `\hat x` là estimate và `u_x` mô tả uncertainty theo một quy ước xác định.

Ta thường không biết “giá trị thật” để tính sai số thật sự. Uncertainty là đánh giá định lượng về phạm vi các giá trị còn phù hợp với dữ liệu, thiết bị và mô hình đo.

Vì vậy báo uncertainty luôn cần nói rõ nó là:

- standard uncertainty;
- standard deviation;
- standard error;
- confidence interval;
- credible interval;
- expanded uncertainty.

Các khái niệm này không thể thay thế tùy ý cho nhau.

## Trung bình và standard error

Với `N` phép đo độc lập có standard deviation mẫu `s`, độ bất định thống kê của trung bình thường giảm gần

```math
u_{\bar x}\approx\frac{s}{\sqrt N}.
```

Điều này giải thích tại sao tăng số mẫu giảm noise ngẫu nhiên chậm theo `1/\sqrt N`.

Muốn uncertainty thống kê giảm 10 lần thường cần khoảng 100 lần số mẫu, nếu các giả định độc lập và phân bố phù hợp còn đúng.

Nếu các mẫu có tương quan theo thời gian, số mẫu hiệu dụng nhỏ hơn `N`; công thức trên không được dùng máy móc.

## Truyền độ bất định qua một hàm

Nếu

```math
y=f(x_1,x_2,\ldots,x_n),
```

và uncertainty nhỏ, khai triển Taylor bậc nhất cho

```math
\delta y
\approx
\sum_i
\frac{\partial f}{\partial x_i}\delta x_i.
```

Nếu các biến độc lập,

```math
u_y^2
\approx
\sum_i
\left(
\frac{\partial f}{\partial x_i}
\right)^2u_i^2.
```

Nếu có tương quan, phải thêm covariance:

```math
u_y^2
\approx
\sum_i\sum_j
\frac{\partial f}{\partial x_i}
\frac{\partial f}{\partial x_j}
\operatorname{Cov}(x_i,x_j).
```

Đây là lý do covariance quan trọng trong thí nghiệm chính xác và fitting nhiều tham số.

## Ví dụ truyền uncertainty

Giả sử diện tích hình chữ nhật

```math
A=LW.
```

Với `L,W` độc lập,

```math
\left(\frac{u_A}{A}\right)^2
\approx
\left(\frac{u_L}{L}\right)^2
+
\left(\frac{u_W}{W}\right)^2.
```

Nếu cùng một thước bị scale error dùng đo cả `L` và `W`, hai sai số có thể tương quan; bỏ covariance sẽ đánh giá uncertainty sai.

## Chữ số có nghĩa và rounding

Không nên báo nhiều chữ số hơn mức dữ liệu hỗ trợ.

Ví dụ, nếu

```text
x = 12.347891 ± 0.3 m
```

thì các chữ số rất sâu sau dấu phẩy không có ý nghĩa thực nghiệm.

Thông thường uncertainty được làm tròn tới một hoặc hai chữ số có nghĩa rồi giá trị estimate được làm tròn tới cùng vị trí thập phân.

Quy tắc cụ thể có thể khác giữa phòng thí nghiệm, nhưng nguyên tắc là không tạo **false precision**.

## Calibration: nối tín hiệu cảm biến với đại lượng vật lý

Cảm biến thường không đo trực tiếp đại lượng cần báo. Nó tạo tín hiệu `s`, rồi dùng mô hình calibration

```math
x=f(s;\theta_{cal}).
```

Các tham số calibration `\theta_{cal}` cũng có uncertainty.

Ví dụ thermistor tạo điện trở, ADC tạo code số, rồi phần mềm chuyển code thành nhiệt độ. Uncertainty cuối cùng gồm cả:

- sensor noise;
- ADC quantization;
- calibration fit;
- drift;
- model conversion.

Đây là cầu nối trực tiếp giữa Vật lý, electronics và software/data pipeline.

## Measurement model quan trọng ngang thiết bị

Một phép đo luôn dựa trên một mô hình.

Ví dụ cân đo lực pháp tuyến rồi chuyển thành “khối lượng” dưới giả định gia tốc trọng trường đã biết và vật không gia tốc theo phương thẳng đứng.

Một camera đo photon qua optics, sensor response và image processing; pixel value không phải trực tiếp “độ sáng thật của vật”.

Do đó systematic error thường không chỉ đến từ phần cứng mà còn từ assumption của measurement model.

## Signal-to-noise ratio và averaging

Một tín hiệu nhỏ có thể không nhìn rõ trong một mẫu nhưng xuất hiện khi trung bình nhiều lần nếu:

- tín hiệu được đồng bộ;
- nhiễu gần độc lập;
- hệ không drift đáng kể.

Nếu noise có thành phần `1/f`, drift hoặc correlation dài, averaging lâu hơn không nhất thiết tiếp tục cải thiện theo `\sqrt N`.

Đây là lý do cần xem power spectral density và stability theo thời gian chứ không chỉ standard deviation ngắn hạn.

## Đơn vị trong phần mềm và dữ liệu

Một bug đơn vị có thể tồn tại dù mọi phép tính số học đều hợp lệ.

Các chiến lược kỹ thuật tốt gồm:

- lưu đơn vị cùng metadata;
- dùng SI nội bộ nhất quán;
- đặt tên biến thể hiện đại lượng;
- validation ở API boundary;
- unit-aware library nếu phù hợp;
- test bằng phân tích thứ nguyên.

Một giá trị floating-point không mang ý nghĩa vật lý đầy đủ nếu thiếu đơn vị và quy ước.

## Mô hình tư duy (Mental Model)

Một kết quả đo đáng tin cần cả chuỗi:

```text
physical quantity
→ measurement principle
→ sensor/instrument
→ calibration
→ recorded signal
→ uncertainty model
→ reported value + unit + uncertainty
```

Thứ nguyên kiểm tra logic của phương trình; uncertainty kiểm tra mức độ dữ liệu thật sự ràng buộc giá trị.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Nhiều chữ số thập phân nghĩa là đo chính xác”

Không. Display resolution không quyết định accuracy hay uncertainty tổng.

### “Đo nhiều lần sẽ loại hết sai số”

Không. Averaging chủ yếu giảm phần ngẫu nhiên; systematic bias có thể còn nguyên.

### “Uncertainty là khoảng chắc chắn chứa giá trị thật”

Ý nghĩa phụ thuộc phương pháp thống kê và quy ước. Confidence interval và credible interval có diễn giải khác nhau.

### “Hai đại lượng uncertainty độc lập có thể cộng thẳng”

Không nói chung. Với propagation tuyến tính độc lập, variance thường cộng theo bình phương; nếu tương quan phải thêm covariance.

### “Đơn vị chỉ là nhãn để đổi sau cùng”

Không. Đơn vị là một phần của cấu trúc mô hình và có thể dùng như kiểm tra logic ngay từ đầu.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Tư duy Vật lý](00_physical_thinking.md), [Ngôn ngữ Toán học](03_mathematical_language.md).

**Liên hệ tiếp:** [Vật lý thực nghiệm](../12_experimental_computational/00_measurement_experiment.md), [Tín hiệu, nhiễu và lấy mẫu](../12_experimental_computational/01_signals_sampling_noise.md), [Suy luận dữ liệu và bài toán ngược](../12_experimental_computational/03_data_inference_inverse_problems.md).
