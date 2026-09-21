# Bài toán học và thiên lệch quy nạp

Machine Learning chỉ quan sát một lượng dữ liệu hữu hạn nhưng lại phải dự đoán ngoài những quan sát đó. Đây là một khoảng trống logic rất quan trọng: vô số hàm có thể khớp hoàn toàn cùng một tập huấn luyện nhưng cho hành vi rất khác trên những điểm chưa từng thấy. Vì vậy **học luôn cần thiên lệch quy nạp (inductive bias / 귀납 편향)** — tức các giả định khiến thuật toán ưu tiên một số giả thuyết hơn các giả thuyết khác.

Thiên lệch quy nạp không phải “bias xấu” theo nghĩa bất công. Nó là điều kiện cần để mô hình có thể khái quát hóa. Câu hỏi đúng không phải “làm sao loại bỏ toàn bộ bias?”, mà là “bias nào phù hợp với cấu trúc của bài toán và môi trường triển khai?”.

## Từ dữ liệu tới giả thuyết

Tập dữ liệu:

\[
D=\{(x_i,y_i)\}_{i=1}^{n}
\]

Không gian giả thuyết:

\[
\mathcal H=\{f:X\to Y\}
\]

Thuật toán học ánh xạ tập dữ liệu thành một giả thuyết:

\[
A(D)=\hat f\in\mathcal H
\]

Nếu nhiều giả thuyết cùng có lỗi huấn luyện bằng 0, thuật toán vẫn phải chọn một trong số chúng.

Lựa chọn đó đến từ kiến trúc, hàm mục tiêu, regularization, optimizer, initialization và cách biểu diễn dữ liệu.

## Vì sao dữ liệu hữu hạn không thể xác định mọi thứ?

Giả sử có ba điểm huấn luyện:

```text
x: 1 2 3
y: 2 4 6
```

Giả thuyết tự nhiên là:

\[
y=2x
\]

Nhưng có vô số hàm khác cũng đi qua chính xác ba điểm đó rồi khác hoàn toàn ở bên ngoài.

Ví dụ:

\[
y=2x+c(x-1)(x-2)(x-3)
\]

Với mọi giá trị `c`, biểu thức vẫn khớp hoàn toàn ba điểm huấn luyện vì phần tích thêm bằng 0 tại `x=1,2,3`.

Việc ưu tiên quan hệ tuyến tính đơn giản `y=2x` chính là một thiên lệch quy nạp.

## Không gian giả thuyết là một prior về cấu trúc

Linear regression giả định:

\[
f(x)=w^Tx+b
\]

nghĩa là target có thể được xấp xỉ tốt bởi cấu trúc affine trên feature đã chọn.

Decision tree giả định những quy tắc hữu ích có thể được xây từ các phép chia ngưỡng theo từng trục feature.

CNN đưa vào giả định về tính cục bộ và cấu trúc dịch chuyển trong ảnh.

Transformer giả định chuỗi có thể được mô hình hóa bằng tương tác giữa token với các layer dùng chung và attention.

Kiến trúc vì vậy không phải một “vỏ chứa trung lập”; nó quyết định loại pattern nào dễ biểu diễn và dễ học.

## Nguyên lý Occam

Một nguyên lý quen thuộc là ưu tiên lời giải đơn giản hơn khi nhiều mô hình khớp dữ liệu tương đương nhau.

Nhưng “đơn giản” phụ thuộc vào cách biểu diễn.

Một hàm sin có thể rất đơn giản trong biểu diễn Fourier nhưng trở nên rất phức tạp nếu cố xấp xỉ bằng đa thức bậc cao. Convolution rất tự nhiên khi giả định locality trong ảnh.

Vì vậy Occam's Razor chỉ có ý nghĩa sau khi ta xác định ngôn ngữ mô hình hoặc cách mô tả độ phức tạp.

## Regularization như một ưu tiên tường minh

Hàm mục tiêu:

\[
J(\theta)=\hat R(\theta)+\lambda\Omega(\theta)
\]

Với L2:

\[
\Omega(\theta)=\|\theta\|_2^2
\]

mô hình ưu tiên tham số có độ lớn nhỏ hơn.

Với L1:

\[
\Omega(\theta)=\|\theta\|_1
\]

mô hình thường có xu hướng tạo nghiệm thưa (sparsity) hơn trong nhiều bài toán.

Regularization nói một cách trực tiếp: nếu nhiều hàm cùng khớp dữ liệu, hãy ưu tiên hàm thỏa thêm một tiêu chí cấu trúc.

## Regularization ngầm

Không có penalty tường minh không có nghĩa hệ thống không có bias.

Quỹ đạo gradient descent, initialization, nhiễu mini-batch, early stopping và cách tham số hóa đều có thể ưu tiên một số nghiệm hơn các nghiệm khác.

Trong neural network dư tham số, optimizer thường tìm một loại nghiệm nội suy cụ thể chứ không chọn ngẫu nhiên trong toàn bộ các nghiệm có training loss bằng 0.

Đây được gọi là **thiên lệch ngầm (implicit bias)** và vẫn là một chủ đề nghiên cứu quan trọng.

## Data augmentation như một giả định bất biến

Giả sử nhãn ảnh không nên thay đổi khi dịch nhẹ hoặc lật ảnh phù hợp.

Huấn luyện trên các phiên bản biến đổi mã hóa giả định:

\[
f(x)\approx f(T(x))
\]

với `T` là phép biến đổi được tin rằng không làm thay đổi nhãn.

Data augmentation không phải một “mẹo miễn phí”. Lật ngang có thể hợp lý với ảnh mèo nhưng có thể sai với chữ viết, biển giao thông hoặc ảnh y khoa có phân biệt trái/phải.

## Bất biến và đồng biến

Một hàm **bất biến (invariant)** thỏa:

\[
f(Tx)=f(x)
\]

nghĩa là đầu ra không đổi khi đầu vào bị biến đổi theo `T`.

Một hàm **đồng biến (equivariant)** thỏa:

\[
f(Tx)=T'f(x)
\]

nghĩa là đầu ra thay đổi theo một quy luật tương ứng.

Phân loại ảnh có thể cần bất biến với dịch chuyển nhỏ; segmentation lại cần mask dịch chuyển theo ảnh, tức quan hệ đồng biến.

Kiến trúc có thể mã hóa trực tiếp những giả định như vậy.

## Prior trong học Bayes

Trong cách nhìn Bayes, prior:

\[
p(\theta)
\]

mã hóa ưu tiên trước khi quan sát dữ liệu.

Posterior:

\[
p(\theta\mid D)\propto p(D\mid\theta)p(\theta)
\]

Nhiều dạng regularization có thể được diễn giải như MAP với prior tương ứng. L2 thường liên hệ với Gaussian prior, còn L1 liên hệ với Laplace prior trong các mô hình chuẩn.

Điều này cho thấy “bias” có thể được biểu diễn dưới dạng xác suất hoặc penalty toán học.

## Empirical Risk Minimization

ERM chọn:

\[
\hat f=\arg\min_{f\in\mathcal H}
\frac{1}{n}\sum_i L(f(x_i),y_i)
\]

Rủi ro thực nghiệm là thứ ta đo được trực tiếp. Rủi ro trên toàn population thì không thể quan sát đầy đủ.

Lý thuyết generalization hỏi: trong điều kiện nào rủi ro thực nghiệm thấp có thể cho ta niềm tin rằng rủi ro kỳ vọng cũng thấp?

Câu trả lời phụ thuộc vào độ phức tạp mô hình, kích thước và phân phối dữ liệu, regularization và cấu trúc thuật toán.

## Structural Risk Minimization

Thay vì dùng một không gian giả thuyết rất lớn, ta có thể xét một chuỗi lớp lồng nhau:

\[
\mathcal H_1\subset\mathcal H_2\subset\cdots
\]

Mục tiêu là cân bằng giữa mức khớp dữ liệu và độ phức tạp.

Trực giác:

```text
fit đủ tốt
nhưng không dùng nhiều capacity hơn mức cần thiết
```

Deep Learning hiện đại làm câu chuyện capacity đơn giản trở nên phức tạp hơn vì mô hình rất lớn vẫn có thể khái quát hóa tốt dù đủ tham số để ghi nhớ toàn bộ training set.

## Trực giác VC dimension

VC dimension đo khả năng một lớp giả thuyết có thể **shatter** các tập điểm trong bài toán phân loại nhị phân.

VC dimension càng cao thì lớp mô hình càng phong phú.

Nó cung cấp các bound liên hệ giữa:

```text
số lượng mẫu
độ phức tạp lớp mô hình
khoảng cách generalization
```

Tuy nhiên các bound kiểu VC thường quá lỏng để giải thích định lượng hành vi thực tế của neural network rất lớn. Dù vậy, nó vẫn là nền tảng khái niệm quan trọng.

## Bias–variance

Một họ mô hình quá cứng có thể có bias cao: dự đoán sai có hệ thống vì không biểu diễn được cấu trúc thật.

Một mô hình quá linh hoạt có thể có variance cao: chỉ cần thay đổi một ít dữ liệu huấn luyện cũng làm mô hình thay đổi mạnh.

Trong một số giả định với squared error:

\[
ExpectedError=Bias^2+Variance+Noise
\]

Đây là mô hình tư duy hữu ích, không phải một lý thuyết đầy đủ cho mọi neural network hiện đại.

Xem thêm: [Bias, Variance and Generalization](./14_bias_variance_and_generalization.md).

## Underfitting

Dấu hiệu thường gặp:

```text
training error cao
validation error cũng cao
```

Nguyên nhân có thể là feature thiếu thông tin, mô hình quá hạn chế, regularization quá mạnh hoặc quá trình tối ưu chưa hội tụ.

Chỉ thêm nhiều dữ liệu thường không giải quyết được underfitting mạnh nếu bản thân mô hình không đủ khả năng biểu diễn.

## Overfitting

Dấu hiệu thường gặp:

```text
training error rất thấp
validation error cao hơn đáng kể
```

Nguyên nhân có thể gồm mô hình linh hoạt nhưng dữ liệu ít, pattern giả do leakage, điều chỉnh quá nhiều theo validation set, correlation ngẫu nhiên hoặc regularization yếu.

Overfitting luôn phải được hiểu tương đối với phân phối mục tiêu và giao thức đánh giá.

## Ghi nhớ và khái quát hóa có thể cùng tồn tại

Một mô hình có thể ghi nhớ một số ví dụ hiếm nhưng vẫn generalize tốt ở phần còn lại. Hai hành vi này không phải hai trạng thái loại trừ nhau.

Neural network lớn có thể nội suy gần như toàn bộ training set nhưng vẫn học biểu diễn hữu ích nhờ quy mô dữ liệu và inductive bias.

Vì vậy quy tắc “số tham số > số mẫu thì chắc chắn overfit” không còn đáng tin như một nguyên tắc chung.

## Nội suy và ngoại suy

**Nội suy (interpolation)** dự đoán trong vùng đã được training distribution bao phủ.

**Ngoại suy (extrapolation)** dự đoán ra ngoài vùng hoặc cấu trúc đã quan sát.

Nhiều mô hình ML hoạt động kém đáng tin cậy hơn rất nhiều khi phải extrapolate.

Một mô hình huấn luyện trên mức thu nhập từ 0 tới 100k vẫn có thể trả ra số cho mức 10 triệu, nhưng khả năng tính ra đầu ra không có nghĩa đầu ra đó đáng tin.

## Tương quan giả

Một feature có thể tương quan với nhãn trong môi trường huấn luyện nhưng không ổn định hoặc không có ý nghĩa nhân quả.

Ví dụ classifier ảnh y tế học watermark của bệnh viện thay vì pattern bệnh vì watermark vô tình tương quan với nhãn.

Nếu train/test đều chia ngẫu nhiên từ cùng bệnh viện, metric có thể vẫn rất đẹp. Chỉ khi đánh giá ở bệnh viện khác vấn đề mới lộ ra.

## Shortcut learning

Neural network thường khai thác tín hiệu dễ dự đoán nhất thay vì khái niệm con người mong đợi.

Nếu màu nền dự đoán được lớp, mô hình có thể bỏ qua hình dạng vật thể.

Đây không phải mô hình “gian lận”; hàm mục tiêu chỉ thưởng dự đoán đúng chứ không thưởng “lý do mà con người muốn”.

Vì vậy dữ liệu và evaluation phải được thiết kế để loại bỏ hoặc thách thức các shortcut.

## Giả định về phân phối

Supervised learning truyền thống thường giả định train và test là i.i.d. từ cùng phân phối.

Trong thực tế:

\[
P_{train}(X,Y)\neq P_{deploy}(X,Y)
\]

Khi distribution shift xảy ra, inductive bias từng hoạt động tốt có thể thất bại.

Do đó validation split và monitoring nên phản ánh các dạng shift có khả năng xuất hiện.

## Domain shift và invariant

Nếu môi trường thay đổi, ta muốn tìm quan hệ ổn định qua nhiều domain.

Ví dụ:

```text
bệnh viện A và B
quốc gia A và B
mùa đông và mùa hè
thiết bị cũ và mới
```

Học cấu trúc ổn định hơn correlation cục bộ là một bài toán khó. Các phương pháp domain generalization cố giải quyết vấn đề này, nhưng bảo đảm của chúng luôn dựa trên giả định cụ thể.

## Biểu diễn feature thay đổi độ khó của bài toán

Một bài toán phi tuyến trong feature gốc có thể trở nên tuyến tính sau một phép biến đổi.

Ví dụ ranh giới hình tròn có thể đơn giản hơn nếu dùng:

\[
r^2=x_1^2+x_2^2
\]

Sau đó chỉ cần threshold theo `r`.

Feature engineering thay đổi độ phức tạp của mô hình phía sau.

Deep Learning tự học nhiều phép biến đổi để biến bài toán thành dạng dễ xử lý hơn ở các layer sau.

## Kernel trick như một thiên lệch biểu diễn

Kernel method ngầm ánh xạ dữ liệu vào không gian feature nhiều chiều:

\[
\phi(x)
\]

nhưng không cần tính trực tiếp tọa độ, chỉ cần:

\[
k(x,x')=\langle\phi(x),\phi(x')\rangle
\]

Việc chọn kernel chính là chọn một giả định về similarity.

RBF kernel ưu tiên giả định rằng các điểm gần nhau trong không gian feature có hành vi tương tự.

## Thiên lệch cục bộ

k-NN giả định các ví dụ gần nhau có khả năng chia sẻ target.

Giả định này chỉ hữu ích khi metric khoảng cách phản ánh đúng sự tương đồng ngữ nghĩa.

Trong không gian nhiều chiều hoặc dữ liệu trộn nhiều scale, Euclidean distance có thể trở nên vô nghĩa.

Vì vậy ngay cả phương pháp “không học tham số rõ ràng” vẫn mang inductive bias rất mạnh.

## Thiên lệch của Decision Tree

Decision tree chia không gian feature bằng các quy tắc ngưỡng theo từng trục.

Nó mô hình hóa interaction và phi tuyến tốt, nhưng có thể kém hiệu quả với ranh giới mượt và nghiêng chéo vì phải dùng nhiều split dạng bậc thang.

Ensemble tree giúp giảm độ bất ổn trong khi vẫn tận dụng ưu điểm của tree với dữ liệu bảng.

## Pretraining như một prior đã học

Mô hình pretrained không bắt đầu từ “không biết gì”; các tham số đã được định hình bởi dữ liệu trước đó.

Fine-tuning trên một tập nhỏ có thể tận dụng:

```text
pattern tổng quát từ pretraining
+ bằng chứng riêng của task mới
```

Điều này cải thiện sample efficiency rất mạnh.

Foundation model có thể được xem như một prior hoặc biểu diễn học được để tái sử dụng trên nhiều nhiệm vụ.

## Giả định của transfer learning

Transfer learning chỉ hữu ích khi tri thức từ source domain có liên quan tới target domain.

Nếu hai miền khác quá xa hoặc bias từ pretraining không phù hợp, có thể xảy ra **negative transfer**.

Vì vậy “pretrained luôn tốt hơn” không phải một quy tắc tuyệt đối.

## Multi-task learning

Một mô hình chia sẻ tham số cho nhiều task có thể tối ưu:

\[
L=\sum_t\lambda_t L_t
\]

Nếu các task liên quan, biểu diễn dùng chung có thể giúp regularize và tăng sample efficiency.

Nếu gradient giữa các task xung đột, một task có thể làm task khác tệ đi.

Việc cho rằng các task có liên quan cũng chính là một thiên lệch quy nạp.

## Lựa chọn của con người cũng tạo bias

Bias xuất hiện từ trước cả thuật toán:

```text
bài toán nào được tự động hóa?
ai xuất hiện trong dataset?
label "thành công" nghĩa là gì?
metric nào được tối ưu?
loại lỗi nào được chấp nhận?
```

Bias kỹ thuật của mô hình và bias xã hội hoặc fairness có liên quan nhưng không phải cùng một khái niệm.

## Trực giác No Free Lunch

Nếu lấy trung bình đều trên toàn bộ mọi hàm mục tiêu có thể có, không một learner nào vượt trội mọi learner khác trong các thiết lập No Free Lunch kinh điển.

Ý nghĩa thực dụng:

> Machine Learning hoạt động vì các bài toán thật có cấu trúc, và mô hình của ta mang giả định phù hợp với cấu trúc đó.

Điều này không có nghĩa “mọi thuật toán đều ngang nhau”. Trong một domain cụ thể, có inductive bias phù hợp và có inductive bias rất tệ.

## Chọn họ mô hình

Các câu hỏi cần cân nhắc gồm:

```text
Có bao nhiêu dữ liệu?
Dữ liệu thuộc loại nào?
Mức phi tuyến và interaction dự kiến ra sao?
Có cần interpretability không?
Giới hạn latency / memory thế nào?
Có distribution shift nào đáng lo?
Có ràng buộc vật lý hoặc monotonic cứng không?
```

Lựa chọn mô hình nên đi từ cấu trúc bài toán, không đi từ độ nổi tiếng của thuật toán.

## Mô hình tư duy

```text
Dữ liệu hữu hạn không thể xác định duy nhất hành vi tương lai.
Inductive bias quyết định lời giải nào được ưu tiên.

Architecture      → thiên lệch biểu diễn
Regularization    → ưu tiên tham số / hàm
Optimization      → thiên lệch chọn nghiệm
Data augmentation → giả định bất biến
Pretraining       → prior đã học
Features          → thay đổi hình học và độ đơn giản của bài toán
```

## Các hiểu lầm thường gặp

### “Bias là thứ phải loại bỏ hoàn toàn”

Không. Inductive bias là điều kiện cần để generalization xảy ra. Bias bất công trong xã hội là một vấn đề khác dù có thể tương tác với bias kỹ thuật.

### “Mô hình càng linh hoạt càng tốt”

Không. Flexibility giúp fit dữ liệu nhưng cần dữ liệu, regularization và evaluation phù hợp để khái quát hóa.

### “Mô hình fit toàn bộ training data nghĩa là đã học sự thật”

Không. Vô số hàm có thể nội suy cùng các quan sát hữu hạn.

### “Architecture chỉ ảnh hưởng compute”

Không. Architecture mã hóa giả định mạnh về locality, sequence, invariance và composition.

## Liên kết kiến thức

Thiên lệch quy nạp nối Thống kê, Tối ưu hóa và Kiến trúc mô hình. Mỗi thuật toán ở các chương sau nên được đọc với một câu hỏi xuyên suốt: **phương pháp này đang giả định điều gì về dữ liệu, và giả định đó hữu ích hoặc nguy hiểm trong trường hợp nào?**

Xem tiếp: [Dữ liệu, feature và label](./02_data_features_and_labels.md).