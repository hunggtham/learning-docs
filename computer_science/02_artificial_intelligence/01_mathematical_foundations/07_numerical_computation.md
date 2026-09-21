# Tính toán số cho Trí tuệ nhân tạo

Toán học trên giấy thường giả định số thực có độ chính xác vô hạn. Máy tính thì không. AI chạy trên bộ nhớ hữu hạn, độ chính xác hữu hạn và các kernel phần cứng cụ thể. Vì vậy một công thức đúng về toán vẫn có thể bị **tràn số (overflow)**, **hụt số (underflow)**, mất độ chính xác hoặc tạo `NaN` khi triển khai.

**Tính toán số (Numerical Computation / 수치 계산)** nghiên cứu cách biến mô hình toán thành phép tính ổn định và hiệu quả. Với học sâu hiện đại, đây không phải chủ đề phụ: độ chính xác hỗn hợp, softmax ổn định, mức điều kiện của ma trận, lượng tử hóa và phép cộng dồn phân tán đều ảnh hưởng trực tiếp đến khả năng huấn luyện và triển khai mô hình.

Xem trước: [Đại số tuyến tính cho AI](./01_linear_algebra_for_ai.md) và [Tối ưu hóa](./06_optimization.md).

## Số dấu phẩy động không phải số thực lý tưởng

Máy tính thường dùng chuẩn IEEE-754 cho **số dấu phẩy động (floating-point number)**. Một số được biểu diễn gần dạng:

\[
(-1)^s\times m\times2^e
\]

với bit dấu, phần định trị và số mũ.

Chỉ có một tập hữu hạn các số có thể biểu diễn chính xác. Nhiều số thập phân như `0.1` không có biểu diễn nhị phân hữu hạn chính xác.

Vì vậy:

```python
0.1 + 0.2 == 0.3
```

có thể cho kết quả `False` trong nhiều ngôn ngữ lập trình.

Trong phần mềm thông thường, sai số này thường rất nhỏ. Nhưng khi cộng dồn hàng triệu phép tính hoặc dùng công thức kém ổn định, sai số nhỏ có thể bị khuếch đại.

## Các định dạng độ chính xác trong AI

### FP32

FP32 dùng 32 bit và có độ chính xác phần định trị đủ cho nhiều phép tính học máy. Trong thời gian dài đây là định dạng mặc định cho huấn luyện.

### FP16

FP16 dùng ít bộ nhớ hơn và có thể tăng thông lượng trên bộ tăng tốc, nhưng miền số mũ và độ chính xác nhỏ hơn nên dễ tràn hoặc hụt số hơn.

### BF16

BFloat16 giữ miền số mũ gần FP32 nhưng phần định trị ngắn hơn. Nó đánh đổi độ chính xác để giữ **miền động (dynamic range)** rộng, phù hợp với nhiều khối lượng công việc học sâu.

### FP8 và độ chính xác thấp hơn

Các bộ tăng tốc hiện đại hỗ trợ định dạng kiểu FP8 trong một số đường huấn luyện hoặc suy luận. Độ chính xác thấp hơn có thể tăng thông lượng và giảm bộ nhớ nhưng đòi hỏi cơ chế co giãn, hiệu chuẩn và kernel phù hợp.

### Lượng tử hóa số nguyên

Các định dạng như INT8 hoặc INT4 thường dùng cho suy luận để giảm bộ nhớ và băng thông. **Lượng tử hóa (quantization)** không chỉ là đổi kiểu dữ liệu; nó cần ánh xạ giá trị thực vào một tập mức rời rạc.

## Epsilon máy

**Epsilon máy (machine epsilon)** mô tả khoảng cách tương đối nhỏ quanh 1 mà định dạng dấu phẩy động còn phân biệt được theo một quy ước nhất định.

Trực giác quan trọng: khi độ lớn của số tăng, khoảng cách giữa các số có thể biểu diễn cũng tăng. Độ chính xác mang tính tương đối, không đồng đều tuyệt đối trên toàn miền.

Vì vậy cộng một số rất nhỏ vào một số cực lớn có thể không làm thay đổi kết quả lưu trữ:

\[
large + tiny \approx large
\]

## Sai số làm tròn

Phép cộng chính xác `a+b` có thể được lưu thành số dấu phẩy động gần nhất:

\[
fl(a+b)=(a+b)(1+\delta)
\]

với `δ` nhỏ dưới các giả định phù hợp.

Sai số của một phép tính có thể rất nhỏ, nhưng thuật toán gồm hàng triệu phép tính vẫn cần xét cách sai số tích lũy và mức điều kiện của bài toán.

## Triệt tiêu nghiêm trọng

Khi trừ hai số lớn gần bằng nhau:

\[
x-y
\]

các chữ số có nghĩa đầu có thể triệt tiêu, khiến sai số tương đối của kết quả tăng mạnh. Hiện tượng này gọi là **triệt tiêu nghiêm trọng (catastrophic cancellation)**.

Ví dụ tính phương sai theo:

\[
E[X^2]-E[X]^2
\]

có thể kém ổn định khi hai hạng rất gần nhau.

Các thuật toán ổn định hơn như phương pháp Welford cập nhật trung bình và phương sai từng bước để giảm vấn đề triệt tiêu.

## Tràn số và hụt số

**Tràn số (overflow)** xảy ra khi độ lớn vượt giá trị lớn nhất có thể biểu diễn, thường dẫn tới `Inf` hoặc hành vi lỗi.

**Hụt số (underflow)** xảy ra khi độ lớn quá nhỏ, trở thành số dưới chuẩn hoặc 0.

Các phép mũ và tích nhiều xác suất nhỏ đặc biệt dễ gặp hai vấn đề này.

## Softmax ổn định

Softmax trực tiếp:

\[
softmax(z_i)=\frac{e^{z_i}}{\sum_j e^{z_j}}
\]

Nếu `z=[1000,1001]`, `e^{1001}` có thể tràn trong nhiều định dạng.

Softmax không đổi khi trừ cùng một hằng số khỏi mọi logit:

\[
softmax(z_i)=\frac{e^{z_i-c}}{\sum_j e^{z_j-c}}
\]

Chọn:

\[
c=\max_j z_j
\]

làm số mũ lớn nhất thành `e^0=1`, nhờ đó tránh tràn số.

Đây là ví dụ kinh điển của **ổn định số (numerical stability)**: hai công thức tương đương về toán có thể có hành vi tính toán hoàn toàn khác nhau.

## Mẹo log-sum-exp

Ta thường cần tính:

\[
\log\sum_i e^{x_i}
\]

Dạng ổn định hơn là:

\[
\log\sum_i e^{x_i}=m+\log\sum_i e^{x_i-m}
\]

với:

\[
m=\max_i x_i
\]

**Log-sum-exp** xuất hiện trong likelihood, softmax, CRF và nhiều mô hình xác suất.

Framework thường cung cấp phép toán nguyên thủy ổn định; nên dùng chúng thay vì tự ghép `log(sum(exp(x)))`.

## Tính xác suất trong miền log

Tích của nhiều xác suất nhỏ:

\[
\prod_i p_i
\]

có thể hụt về 0.

Lấy log:

\[
\log\prod_i p_i=\sum_i\log p_i
\]

biến phép nhân thành phép cộng và ổn định hơn.

Đây là lý do likelihood của chuỗi thường được tính dưới dạng tổng log-xác suất.

## Mức điều kiện khác với độ ổn định số

**Mức điều kiện (conditioning)** là thuộc tính của bài toán toán học: nhiễu nhỏ ở đầu vào có thể làm đầu ra thay đổi bao nhiêu.

**Độ ổn định số (numerical stability)** là thuộc tính của thuật toán: cách tính có làm tăng sai số quá mức cần thiết hay không.

Một bài toán vốn điều kiện kém không thể được “sửa hoàn toàn” chỉ bằng thuật toán tốt; thuật toán ổn định chủ yếu tránh tạo thêm sai số không cần thiết.

Ví dụ, giải hệ tuyến tính với ma trận gần suy biến vốn đã rất nhạy.

## Số điều kiện

Với ma trận khả nghịch `A`, **số điều kiện (condition number)** theo một chuẩn là:

\[
\kappa(A)=\|A\|\|A^{-1}\|
\]

`κ` lớn nghĩa sai số nhỏ của đầu vào hoặc làm tròn có thể bị khuếch đại mạnh trong nghiệm.

Trong tối ưu hóa, Hessian điều kiện kém làm hạ gradient đi zig-zag và hội tụ chậm.

Co giãn đặc trưng và chuẩn hóa có thể cải thiện mức điều kiện hiệu dụng.

## Không nên tính nghịch đảo khi không cần

Biểu thức:

\[
x=A^{-1}b
\]

đúng về toán, nhưng đại số tuyến tính số thường dùng bộ giải hoặc phép phân rã thay vì tính tường minh `A^{-1}`.

Ví dụ, bài toán bình phương tối thiểu nên dùng QR, SVD hoặc bộ giải tối ưu thay vì trực tiếp tính:

\[
(X^TX)^{-1}X^Ty
\]

vì tạo `X^TX` có thể làm số điều kiện xấu đi đáng kể.

Nguyên tắc thực hành:

> **Hãy giải hệ phương trình; đừng tự động tạo ma trận nghịch đảo nếu không cần.**

## Sai số khi cộng dồn

Tổng hàng triệu số dấu phẩy động có thể phụ thuộc vào thứ tự vì phép cộng dấu phẩy động không có tính kết hợp tuyệt đối:

\[
(a+b)+c\neq a+(b+c)
\]

trên máy tính.

Cộng theo cặp hoặc thuật toán Kahan có thể giảm sai số.

Phép rút gọn song song trên GPU thay đổi thứ tự phép cộng, vì vậy cùng mã nguồn vẫn có thể có sai khác số nhỏ tùy kernel và cách lập lịch.

## Tính xác định và khả năng tái lập

Kết quả học sâu có thể thay đổi do:

- khởi tạo ngẫu nhiên;
- thứ tự các lô dữ liệu;
- dropout;
- thứ tự cộng dồn song song;
- kernel CUDA không hoàn toàn xác định;
- thời điểm truyền thông trong huấn luyện phân tán.

Đặt cùng seed không bảo đảm kết quả giống từng bit nếu kernel bên dưới không xác định.

Để tái lập, cần ghi lại phiên bản phần mềm, phần cứng, seed, cấu hình, phiên bản dữ liệu và các tùy chọn xác định khi cần.

## Huấn luyện độ chính xác hỗn hợp

**Độ chính xác hỗn hợp (mixed precision)** dùng định dạng thấp hơn cho các phép toán cần thông lượng cao nhưng giữ một số đại lượng quan trọng ở độ chính xác cao hơn.

Một mẫu điển hình:

```text
Nhân ma trận FP16/BF16
        ↓
Cộng dồn hoặc trọng số chính ở độ chính xác cao hơn khi cần
        ↓
Cập nhật bộ tối ưu
```

Chi tiết chính xác phụ thuộc phần cứng và framework.

Mục tiêu là giảm bộ nhớ và tăng thông lượng mà không phá hỏng tín hiệu huấn luyện.

## Co giãn hàm mất mát

Với FP16, gradient rất nhỏ có thể hụt về 0. **Co giãn hàm mất mát (loss scaling)** nhân mất mát với hệ số `S`:

\[
L'=SL
\]

Gradient trở thành:

\[
\nabla L'=S\nabla L
\]

Sau lan truyền ngược, chia gradient cho `S` trước khi cập nhật tham số.

Co giãn động điều chỉnh `S` khi phát hiện tràn số.

BF16 có miền số mũ rộng hơn nên thường ít phụ thuộc vào loss scaling hơn FP16.

## Gỡ lỗi gradient tràn và NaN

`NaN` có thể xuất phát từ:

- chia cho 0;
- lấy log của giá trị không hợp lệ hoặc bằng 0;
- căn bậc hai giá trị âm do sai số số;
- giá trị kích hoạt hoặc gradient bùng nổ;
- phép mũ bị tràn;
- thống kê chuẩn hóa không hợp lệ.

Một luồng gỡ lỗi hữu ích:

```text
hàm mất mát còn hữu hạn?
  ↓
giá trị kích hoạt từng tầng còn hữu hạn?
  ↓
gradient còn hữu hạn?
  ↓
trạng thái optimizer còn hữu hạn?
  ↓
kiểm tra tốc độ học / co giãn / dữ liệu đầu vào
```

Cơ chế phát hiện bất thường của framework giúp tìm phép toán đầu tiên sinh giá trị lỗi nhưng thường làm chậm chương trình.

## Chuẩn hóa ổn định

Công thức phương sai:

\[
\sigma^2=E[x^2]-E[x]^2
\]

có thể chịu triệt tiêu số. Triển khai thực tế dùng phép giảm ổn định và thêm epsilon:

\[
\hat x=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}
\]

`ε` không chỉ tránh chia 0; nó còn ảnh hưởng hành vi khi phương sai rất nhỏ.

Các lớp chuẩn hóa khác nhau chọn các trục khác nhau, từ đó thay đổi cả thống kê lẫn hành vi số.

## Lượng tử hóa

**Lượng tử hóa (quantization)** ánh xạ giá trị liên tục hoặc dấu phẩy động thành các mức số nguyên rời rạc.

Ví dụ lượng tử hóa affine đơn giản:

\[
q=round(x/s)+z
\]

với thang `s` và điểm 0 `z`.

Khôi phục gần đúng:

\[
x\approx s(q-z)
\]

Sai số lượng tử hóa là chênh lệch giữa giá trị gốc và giá trị tái tạo.

## Lượng tử hóa đối xứng và bất đối xứng

Lượng tử hóa đối xứng thường đặt điểm 0 gần 0 và miền giá trị đối xứng quanh 0. Nó đơn giản và có thể nhanh hơn trên một số phần cứng.

Lượng tử hóa bất đối xứng dùng điểm 0 để khớp tốt hơn với phân phối không đối xứng.

Lựa chọn phụ thuộc vào phân phối trọng số/kích hoạt và kernel phần cứng.

## Theo tensor và theo kênh

**Lượng tử hóa theo tensor (per-tensor)** dùng một hệ số thang cho toàn tensor.

**Lượng tử hóa theo kênh (per-channel)** dùng thang riêng cho từng kênh, thường giảm sai số khi các kênh có miền giá trị khác nhau nhưng tăng độ phức tạp.

Lượng tử hóa trọng số LLM còn thường dùng nhóm trọng số, tức mỗi nhóm có một hệ số thang riêng.

## PTQ và QAT

**Lượng tử hóa sau huấn luyện (Post-Training Quantization - PTQ)** lượng tử hóa mô hình đã huấn luyện, đôi khi dùng dữ liệu hiệu chuẩn.

**Huấn luyện nhận biết lượng tử hóa (Quantization-Aware Training - QAT)** mô phỏng tác động lượng tử hóa trong quá trình huấn luyện để mô hình thích nghi.

PTQ đơn giản hơn; QAT có thể giữ chất lượng tốt hơn khi giảm bit mạnh nhưng cần thêm chi phí huấn luyện.

## Lượng tử hóa LLM

Tham số LLM chiếm nhiều bộ nhớ. Xấp xỉ bộ nhớ chỉ tính trọng số thô:

\[
Memory\approx N_{params}\times bits/parameter
\]

Ví dụ mô hình 7B tham số:

- FP16 ≈ 14 GB trọng số thô;
- INT8 ≈ 7 GB;
- 4-bit ≈ 3.5 GB.

Bộ nhớ thực tế còn cần metadata, KV cache, kích hoạt, vùng làm việc và chi phí bộ cấp phát.

Mức suy giảm chất lượng phụ thuộc thuật toán lượng tử hóa, cách xử lý ngoại lệ, kích thước nhóm và kiến trúc mô hình.

## KV cache và độ chính xác

Suy luận Transformer tự hồi quy lưu Key/Value của token trước trong **KV cache** để không phải tính lại toàn bộ chuỗi ở mỗi bước.

Bộ nhớ KV cache tăng xấp xỉ theo:

```text
kích thước lô × độ dài chuỗi × số tầng × số KV head × chiều head × số byte
```

Ngữ cảnh dài có thể khiến KV cache chiếm phần lớn bộ nhớ. Lượng tử hóa KV cache hoặc dùng grouped-query/multi-query attention giúp giảm áp lực bộ nhớ nhưng có thể ảnh hưởng chất lượng.

## Độ chính xác cộng dồn trong nhân ma trận

Đầu vào có thể là FP16/BF16 nhưng phép cộng dồn nhiều tích có thể dùng độ chính xác kiểu FP32 tùy phần cứng và kernel.

Với tích vô hướng:

\[
s=\sum_i a_ib_i
\]

nếu toàn bộ phép cộng dồn dùng độ chính xác thấp, sai số làm tròn tăng theo số hạng.

Thiết kế bộ tăng tốc thường tách định dạng đầu vào khỏi định dạng cộng dồn.

## Kernel hợp nhất

Một chuỗi như:

```text
linear → bias → activation
```

nếu thực hiện từng phép riêng sẽ phải ghi và đọc tensor trung gian từ bộ nhớ nhiều lần.

**Hợp nhất kernel (kernel fusion)** gộp các phép toán để giảm lưu lượng bộ nhớ và đôi khi cải thiện hành vi số vì tránh làm tròn ở các trung gian.

FlashAttention là ví dụ sâu hơn: nó tổ chức lại phép tính attention để giảm truy cập HBM mà vẫn tính attention chính xác theo công thức, trong giới hạn số dấu phẩy động, mà không cần vật chất hóa toàn bộ ma trận attention theo cách ngây thơ.

Như vậy, việc viết lại thuật toán có thể đồng thời cải thiện cả hiệu suất phần cứng lẫn độ ổn định.

## Băng thông bộ nhớ và FLOPs

Hiệu năng AI không chỉ phụ thuộc số phép toán dấu phẩy động. Một phép tính có thể bị giới hạn bởi năng lực tính toán hoặc bởi băng thông bộ nhớ.

**Cường độ số học (arithmetic intensity)** xấp xỉ:

\[
\frac{FLOPs}{bytes\ moved}
\]

Nhân ma trận lớn có cường độ số học cao và phù hợp GPU. Phép toán theo từng phần tử thường dễ bị giới hạn bởi bộ nhớ.

Đây là lý do vector hóa và hợp nhất kernel quan trọng, và cũng là lý do kiến trúc AI cùng tiến hóa với phần cứng.

## Tính toán thưa

Nếu tensor có nhiều số 0, biểu diễn thưa có thể tiết kiệm tính toán và bộ nhớ. Tuy nhiên tính thưa chỉ hữu ích nếu phần cứng và phần mềm thực sự khai thác được mẫu thưa đó.

Tính thưa ngẫu nhiên không cấu trúc có thể tốn chi phí lập chỉ mục cao; tính thưa có cấu trúc dễ tăng tốc hơn.

“90% trọng số bằng 0” không tự động nghĩa suy luận nhanh gấp 10 lần.

## Tách lỗi mô hình và lỗi số

Cần phân biệt:

```text
sai số mô hình hóa
+ sai số thống kê
+ sai số tối ưu hóa
+ sai số số học
```

Dự đoán sai có thể do lớp mô hình không phù hợp, dữ liệu thiếu, bộ tối ưu chưa hội tụ hoặc độ chính xác số không đủ.

Không nên đổ lỗi cho dấu phẩy động trước khi kiểm tra các nguồn lỗi lớn hơn, nhưng ở quy mô lớn vấn đề số học là một kiểu thất bại thực tế.

## Sigmoid và binary cross-entropy ổn định

Nếu tính trực tiếp:

\[
\sigma(z)=1/(1+e^{-z})
\]

rồi:

\[
-y\log\sigma(z)-(1-y)\log(1-\sigma(z))
\]

công thức có thể kém ổn định khi logit rất lớn hoặc rất nhỏ.

Framework thường cung cấp hàm kiểu `binary_cross_entropy_with_logits` với công thức hợp nhất ổn định. Nguyên tắc thực hành là **ưu tiên primitive loss ổn định do framework cung cấp thay vì tự ghép qua xác suất nếu không cần**.

## Tích lũy gradient

Nếu GPU không đủ bộ nhớ cho lô lớn, có thể tích lũy gradient qua nhiều lô siêu nhỏ:

```text
microbatch 1 → gradient
microbatch 2 → cộng thêm gradient
...
optimizer.step()
```

Nếu chuẩn hóa và co giãn hàm mất mát đúng, lô hiệu dụng có thể gần tương đương lô lớn.

Tuy nhiên các lớp như BatchNorm hoặc trạng thái ngẫu nhiên có thể khiến ngữ nghĩa khác với một lô lớn thật sự.

## Hành vi số trong huấn luyện phân tán

Huấn luyện phân tán tổng hợp gradient qua các phép như all-reduce. Thứ tự và độ chính xác truyền thông ảnh hưởng đến làm tròn.

Nén gradient, truyền thông độ chính xác thấp và sharding giúp tiết kiệm băng thông hoặc bộ nhớ nhưng tạo thêm đánh đổi.

Ở quy mô lớn, phân tích số và kỹ nghệ hệ thống phân tán hòa vào nhau.

## Mô hình tư duy (mental model)

```text
Công thức số thực       ≠ phép tính dấu phẩy động
Công thức ổn định       = cùng toán học, đường tính an toàn hơn
Mức điều kiện           = bài toán nhạy với sai số đầu vào đến đâu
Độ chính xác            = biểu diễn giá trị chi tiết đến mức nào
Miền động               = biểu diễn được độ lớn/nhỏ tới đâu
Độ chính xác hỗn hợp    = dùng định dạng phù hợp cho từng phép toán
Lượng tử hóa            = đổi độ trung thực số lấy bộ nhớ/thông lượng
Thiết kế kernel         = tổ chức lại phép tính theo phần cứng và độ ổn định
```

## Các hiểu lầm thường gặp

### “FP16 chỉ kém chính xác hơn FP32 một chút”

FP16 vừa có độ chính xác thấp hơn vừa có miền số mũ nhỏ hơn FP32 đáng kể, nên hành vi tràn/hụt số khác nhiều. BF16 lại có một kiểu đánh đổi khác.

### “Lượng tử hóa 4-bit làm mô hình nhỏ và nhanh đúng 4 lần”

Dung lượng trọng số thô có thể giảm gần 4 lần so với FP16, nhưng bộ nhớ chạy còn KV cache, metadata và vùng làm việc; tốc độ còn phụ thuộc kernel và phần cứng.

### “NaN là lỗi framework”

Có thể là lỗi phần mềm, nhưng thường cũng có thể do hàm mục tiêu kém ổn định, tràn số, tốc độ học quá lớn, đầu vào không hợp lệ hoặc co giãn sai.

### “Hai công thức tương đương về toán sẽ chạy giống nhau”

Không đúng trong dấu phẩy động. Softmax ổn định và log-sum-exp là hai ví dụ điển hình.

## Liên kết kiến thức

Tính toán số nối toán học với [Kiến trúc hệ thống AI](../00_foundations/04_ai_system_architecture.md), tối ưu hóa và hạ tầng tính toán. Các khái niệm này sẽ quay lại trong huấn luyện độ chính xác hỗn hợp, lượng tử hóa, kernel Transformer, huấn luyện phân tán và suy luận hiệu quả.

Khi mô hình bất ổn hoặc chi phí triển khai cao, hãy nhìn cả **phương trình, định dạng số, miền giá trị tensor, thứ tự cộng dồn, lưu lượng bộ nhớ và kernel phần cứng**, chứ không chỉ nhìn kiến trúc trên giấy.