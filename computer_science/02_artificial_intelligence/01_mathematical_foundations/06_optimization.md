# Tối ưu hóa cho Trí tuệ nhân tạo

**Tối ưu hóa (Optimization / 최적화)** là quá trình tìm giá trị của các biến để một **hàm mục tiêu (objective function)** trở nên tốt hơn. Trong học máy, kiến trúc xác định lớp hàm mà mô hình có thể biểu diễn, dữ liệu cung cấp các mẫu quan sát, hàm mất mát định nghĩa hành vi nào được xem là tốt, còn **bộ tối ưu (optimizer)** tìm các tham số phù hợp với mục tiêu đó.

Một hiểu lầm phổ biến là “huấn luyện = hạ gradient”. Chính xác hơn, huấn luyện là một quá trình học rộng hơn; tối ưu hóa là cơ chế tìm tham số; còn các phương pháp dựa trên gradient chỉ là một họ thuật toán. Quan trọng hơn, tối ưu rất tốt một mục tiêu sai vẫn có thể tạo ra hệ thống tệ. Vì vậy tối ưu hóa phải luôn được học cùng **thiết kế mục tiêu, ràng buộc và đánh giá**.

Xem trước: [Giải tích cho AI](./04_calculus_for_ai.md).

## Hàm mục tiêu

Một bài toán tối ưu tổng quát có dạng:

\[
\theta^*=\arg\min_\theta J(\theta)
\]

Trong học có giám sát:

\[
J(\theta)=\frac{1}{n}\sum_{i=1}^{n}L(f_\theta(x_i),y_i)+\lambda\Omega(\theta)
\]

Hạng đầu đo mức độ mô hình khớp dữ liệu. `Ω(θ)` đóng vai trò điều chuẩn tham số hoặc hành vi. `λ` kiểm soát mức đánh đổi giữa các thành phần.

Nếu muốn tối đa hóa phần thưởng `R`, ta có thể tương đương tối thiểu hóa `-R`. `argmin` và `argmax` chỉ vị trí đạt cực trị, không phải chính giá trị cực trị.

## Hàm mất mát, hàm mục tiêu và chỉ số đánh giá khác nhau

**Hàm mất mát (loss function / 손실 함수)** thường là đại lượng khả vi mà bộ tối ưu giảm trên các mẫu dữ liệu.

**Hàm mục tiêu (objective)** có thể gồm hàm mất mát cộng với điều chuẩn, hình phạt hoặc ràng buộc.

**Chỉ số đánh giá (evaluation metric)** là đại lượng ta thực sự báo cáo hoặc quan tâm, ví dụ độ chính xác, F1, doanh thu hoặc tỷ lệ vi phạm an toàn.

Chỉ số đánh giá không nhất thiết khả vi. Ta có thể tối ưu entropy chéo nhưng đánh giá bằng độ chính xác.

Đây là vai trò của **hàm mất mát thay thế (surrogate loss)**: tối ưu một đại lượng dễ xử lý có quan hệ với mục tiêu thực.

Nếu hàm thay thế và mục tiêu thật lệch nhau, hàm mất mát huấn luyện có thể tiếp tục giảm trong khi kết quả sản phẩm không tốt hơn.

## Tối ưu hóa có ràng buộc

Không phải mọi bài toán đều chỉ là tối thiểu hóa một số vô hướng không ràng buộc.

Ví dụ:

\[
\min_\theta L(\theta)
\]

với điều kiện:

\[
C(\theta)\le c
\]

Ràng buộc có thể là độ trễ, bộ nhớ, giới hạn công bằng, ngân sách năng lượng hoặc ngưỡng rủi ro.

AI trong production thường là bài toán đa mục tiêu hoặc có nhiều ràng buộc:

```text
chất lượng ↑
độ trễ ↓
chi phí ↓
rủi ro riêng tư ↓
vi phạm an toàn ↓
```

Không tồn tại một mô hình “tốt nhất” độc lập với bối cảnh; thường chỉ có các phương án đánh đổi trên **biên Pareto (Pareto frontier)**.

## Tính lồi

Một hàm `f` là **lồi (convex)** nếu với `0≤λ≤1`:

\[
f(\lambda x+(1-\lambda)y)
\le
\lambda f(x)+(1-\lambda)f(y)
\]

Tối ưu lồi hấp dẫn vì dưới các điều kiện phù hợp, cực tiểu cục bộ cũng là cực tiểu toàn cục.

Hồi quy tuyến tính với hàm mất mát bình phương là lồi theo tham số. Hồi quy logistic với hàm mất mát lồi chuẩn cũng có tính lồi.

Mạng nơ-ron sâu nói chung không lồi vì phép hợp thành nhiều tầng và tương tác giữa tham số tạo ra bề mặt tối ưu phức tạp.

## Cực tiểu cục bộ, điểm yên ngựa và vùng phẳng

Trong bề mặt không lồi, gradient bằng 0 có thể là:

- cực tiểu cục bộ;
- cực đại cục bộ;
- **điểm yên ngựa (saddle point)**;
- vùng phẳng.

Mạng nơ-ron nhiều chiều có rất nhiều hướng yên ngựa hoặc gần phẳng. Vì vậy không nên hình dung tối ưu hóa chỉ như “quả bóng lăn xuống một cái bát”.

Bề mặt tối ưu còn phụ thuộc vào cách tham số hóa và các đối xứng. Hai bộ tham số khác nhau có thể biểu diễn cùng một hàm.

## Hạ gradient

**Hạ gradient toàn bộ lô (full-batch gradient descent)** cập nhật:

\[
\theta_{t+1}=\theta_t-\eta\nabla J(\theta_t)
\]

trong đó `η` là tốc độ học.

Nếu `η` quá nhỏ, tiến trình chậm. Nếu quá lớn, cập nhật có thể vượt quá vùng tốt hoặc phân kỳ.

Xét hàm bậc hai một chiều:

\[
J(w)=\frac{1}{2}aw^2
\]

Gradient:

\[
J'(w)=aw
\]

Cập nhật:

\[
w_{t+1}=(1-\eta a)w_t
\]

Từ đây có thể thấy độ ổn định của tốc độ học phụ thuộc vào độ cong `a`. Một tốc độ học phù hợp ở hướng phẳng có thể quá lớn ở hướng dốc.

## Hạ gradient ngẫu nhiên

Với tập dữ liệu lớn, tính gradient trên toàn bộ dữ liệu ở mỗi bước rất tốn kém. **Hạ gradient ngẫu nhiên (Stochastic Gradient Descent - SGD)** thường dùng một mẫu hoặc một **lô nhỏ (mini-batch)**:

\[
g_t=\frac{1}{B}\sum_{i\in\mathcal{B}_t}\nabla L_i(\theta_t)
\]

\[
\theta_{t+1}=\theta_t-\eta g_t
\]

`g_t` là một ước lượng có nhiễu của gradient đầy đủ.

Nhiễu không chỉ là nhược điểm. Nó giúp giảm chi phí mỗi lần cập nhật, có thể giúp khám phá bề mặt tối ưu và đôi khi tạo hiệu ứng điều chuẩn ngầm.

Trong thực hành hiện đại, “SGD” thường chỉ mini-batch SGD chứ không nhất thiết đúng một mẫu mỗi bước.

## Đánh đổi của kích thước lô

**Kích thước lô (batch size)** lớn thường:

- tạo ước lượng gradient ít nhiễu hơn;
- tận dụng phần cứng tốt hơn;
- cần nhiều bộ nhớ hơn;
- tạo ít lần cập nhật tham số hơn trong mỗi epoch;
- có thể làm thay đổi động lực huấn luyện và khả năng khái quát hóa.

Lô nhỏ thường:

- tạo gradient nhiều nhiễu hơn;
- có nhiều lần cập nhật hơn;
- dùng ít bộ nhớ hơn;
- có thể làm thông lượng phần cứng kém nếu quá nhỏ.

Không có kích thước lô tối ưu cho mọi trường hợp. Nó tương tác với tốc độ học, bộ tối ưu, mô hình, phần cứng và quy mô dữ liệu.

## Động lượng

SGD cơ bản dễ dao động trong những vùng có độ cong rất khác nhau theo các trục.

**Động lượng (momentum)** duy trì một biến vận tốc:

\[
v_t=\beta v_{t-1}+g_t
\]

\[
\theta_{t+1}=\theta_t-\eta v_t
\]

Mô hình tư duy: các gradient có hướng nhất quán qua nhiều bước được tích lũy, còn dao động đổi dấu qua lại bị triệt tiêu một phần.

Đây chỉ là phép tương tự với động lượng vật lý, không phải mô hình vật lý chính xác.

## Động lượng Nesterov

Các biến thể Nesterov đánh giá gradient ở một điểm đã dịch theo hướng động lượng trong một số cách xây dựng phổ biến. Chúng có lợi thế lý thuyết trong một số bài toán lồi và cũng có các biến thể thực dụng.

Các framework có thể triển khai công thức hơi khác nhau, nên khi tái lập kết quả cần kiểm tra định nghĩa chính xác thay vì chỉ nhìn tên bộ tối ưu.

## Tốc độ học thích nghi

### AdaGrad

AdaGrad tích lũy bình phương gradient:

\[
s_t=s_{t-1}+g_t^2
\]

và chuẩn hóa cập nhật:

\[
\theta\leftarrow\theta-\eta\frac{g_t}{\sqrt{s_t}+\epsilon}
\]

Các tham số từng có gradient lớn sẽ nhận tốc độ học hiệu dụng nhỏ hơn.

AdaGrad hữu ích với đặc trưng thưa, nhưng mẫu số chỉ tăng nên tốc độ học có thể giảm quá mạnh về sau.

### RMSProp

RMSProp dùng trung bình động hàm mũ:

\[
s_t=\beta s_{t-1}+(1-\beta)g_t^2
\]

nhờ đó tránh tích lũy vô hạn như AdaGrad.

### Adam

Adam kết hợp ước lượng moment bậc nhất và bậc hai:

\[
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t
\]

\[
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2
\]

Sau hiệu chỉnh độ chệch:

\[
\hat m_t=\frac{m_t}{1-\beta_1^t},\quad
\hat v_t=\frac{v_t}{1-\beta_2^t}
\]

Cập nhật:

\[
\theta_{t+1}=
\theta_t-\eta\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}
\]

Adam phổ biến vì hoạt động ổn định trong nhiều bài toán, nhưng không tự động là lựa chọn tốt nhất cho mọi trường hợp.

## AdamW và suy giảm trọng số

Điều chuẩn L2 và **suy giảm trọng số (weight decay)** tương đương trong một số thiết lập SGD đơn giản, nhưng với bộ tối ưu thích nghi chúng không nhất thiết tương đương.

AdamW tách suy giảm trọng số khỏi việc chuẩn hóa gradient theo Adam:

\[
\theta\leftarrow (1-\eta\lambda)\theta-\text{AdamUpdate}
\]

Đây là một lý do AdamW phổ biến trong huấn luyện Transformer.

## Lịch tốc độ học

Tốc độ học hiếm khi giữ nguyên từ đầu đến cuối một quá trình huấn luyện lớn.

Một số kiểu lịch thường gặp:

- **giai đoạn tăng dần ban đầu (warmup)**;
- giảm theo bậc;
- giảm theo hàm mũ;
- giảm theo cosine;
- lịch kiểu one-cycle.

Warmup tăng tốc độ học từ nhỏ lên mức mục tiêu trong những bước đầu. Với Transformer, giai đoạn đầu có thể không ổn định khi thống kê moment và mức kích hoạt chưa ổn định.

Lịch cosine:

\[
\eta_t=\eta_{min}+\frac{1}{2}(\eta_{max}-\eta_{min})
\left(1+\cos\frac{\pi t}{T}\right)
\]

Lịch tốc độ học là một phần của thuật toán tối ưu, không chỉ là tùy chọn trang trí.

## Khởi tạo trọng số và tối ưu hóa

Nếu trọng số quá lớn, giá trị kích hoạt và gradient có thể bùng nổ hoặc rơi vào vùng bão hòa. Nếu quá nhỏ, tín hiệu có thể biến mất.

Khởi tạo Xavier/Glorot cân bằng phương sai theo số đầu vào và đầu ra, thường phù hợp với một số hàm kích hoạt.

Khởi tạo He/Kaiming điều chỉnh tốt hơn cho các hàm kiểu ReLU.

Khởi tạo không chỉ là “hạt giống ngẫu nhiên”; nó đặt hình học ban đầu và thang tín hiệu cho quá trình tối ưu.

## Chuẩn hóa và khả năng huấn luyện

BatchNorm, LayerNorm và các biến thể chuẩn hóa giá trị kích hoạt theo những trục khác nhau.

Ngoài tác dụng điều chuẩn, chuẩn hóa còn giúp cải thiện mức điều kiện và ổn định thang tín hiệu.

Transformer thường dùng LayerNorm hoặc RMSNorm vì cấu trúc chuỗi và batch khác CNN.

Vị trí chuẩn hóa, ví dụ **pre-norm** hay **post-norm**, ảnh hưởng trực tiếp tới dòng gradient và độ ổn định của Transformer sâu.

## Mức điều kiện của bài toán

Một bài toán được xem là **điều kiện kém (ill-conditioned)** khi độ cong khác nhau quá mạnh giữa các hướng.

Với bài toán bậc hai có trị riêng Hessian từ `λ_min` tới `λ_max`, **số điều kiện (condition number)**:

\[
\kappa=\frac{\lambda_{max}}{\lambda_{min}}
\]

Nếu `κ` lớn, hạ gradient dễ đi zig-zag và phải dùng tốc độ học thận trọng.

Chuẩn hóa đặc trưng, chuẩn hóa kích hoạt, tiền điều kiện và các phương pháp thích nghi đều cố cải thiện mức điều kiện hiệu dụng.

## Phương pháp tối ưu bậc hai

Cập nhật Newton:

\[
\theta_{t+1}=\theta_t-H^{-1}\nabla J
\]

sử dụng thông tin độ cong từ Hessian.

Nếu hàm mục tiêu gần bậc hai, Newton có thể hội tụ rất nhanh gần nghiệm tối ưu. Tuy nhiên Hessian của mạng nơ-ron lớn quá khổng lồ để lưu và nghịch đảo trực tiếp.

Các phương pháp gần Newton như BFGS và L-BFGS xấp xỉ độ cong và hữu ích ở bài toán nhỏ hơn, nhưng học sâu quy mô lớn chủ yếu dựa trên phương pháp bậc nhất.

## Cắt gradient

**Cắt gradient (gradient clipping)** theo chuẩn toàn cục:

\[
g\leftarrow g\cdot\min\left(1,\frac{c}{\|g\|}\right)
\]

khi chuẩn gradient vượt ngưỡng `c`.

Cắt gradient giúp tránh một lần cập nhật cực lớn, đặc biệt trong mô hình chuỗi. Nhưng nếu việc cắt xảy ra liên tục, đó có thể là dấu hiệu của tốc độ học không phù hợp, chuẩn hóa kém hoặc bất ổn số khác.

## Điều chuẩn và tối ưu hóa không hoàn toàn tách rời

Hình phạt L2 làm thay đổi hàm mục tiêu.

Dropout làm thay đổi động lực huấn luyện ngẫu nhiên.

Dừng sớm giới hạn quỹ đạo tối ưu trước khi mô hình khớp hoàn toàn tập huấn luyện.

Tăng cường dữ liệu làm thay đổi phân phối thực nghiệm mà bộ tối ưu nhìn thấy.

Vì vậy khả năng khái quát hóa là kết quả tương tác giữa hàm mục tiêu, dữ liệu và quỹ đạo tối ưu.

## Dừng sớm

Hàm mất mát xác thực có thể bắt đầu tăng dù hàm mất mát huấn luyện vẫn giảm. **Dừng sớm (early stopping)** chọn checkpoint trước khi quá khớp trở nên nghiêm trọng.

Đây là một dạng điều chuẩn ngầm: ta giới hạn số bước tối ưu.

Tuy nhiên chỉ số xác thực nhiều nhiễu có thể khiến dừng quá sớm; hệ thống thực tế thường dùng khoảng kiên nhẫn (patience), làm mượt và chiến lược checkpoint.

## Siêu tham số như một bài toán tối ưu bên ngoài

Tham số `θ` được bộ tối ưu học từ dữ liệu huấn luyện. **Siêu tham số (hyperparameter)** như `λ`, tốc độ học, độ sâu kiến trúc hoặc kích thước lô thường được chọn bằng tập xác thực.

Có thể nhìn thành hai vòng:

```text
vòng trong: học θ
vòng ngoài: chọn siêu tham số h
```

Tìm kiếm lưới, tìm kiếm ngẫu nhiên, tối ưu Bayes và phương pháp dựa trên quần thể là các chiến lược cho vòng ngoài.

Nếu tinh chỉnh quá nhiều trên cùng tập xác thực, quá khớp tập xác thực cũng có thể xảy ra.

## Tối ưu đa mục tiêu

Giả sử hệ thống cần tăng chất lượng `Q` và giảm độ trễ `C`:

\[
\max Q(\theta),\quad \min C(\theta)
\]

Có thể gộp thành:

\[
J=-Q+\lambda C
\]

nhưng việc chọn `λ` phản ánh yêu cầu sản phẩm hoặc đánh đổi giá trị, không phải điều toán học tự quyết định.

**Biên Pareto (Pareto frontier)** chứa các nghiệm mà không thể cải thiện một mục tiêu mà không làm xấu ít nhất một mục tiêu khác.

Hệ thống AI thực tế thường chọn một điểm trên biên này theo ràng buộc sản phẩm.

## Tối ưu có ràng buộc và hàm Lagrange

Bài toán:

\[
\min_x f(x)\quad \text{s.t.}\quad g(x)\le0
\]

Hàm Lagrange:

\[
\mathcal{L}(x,\lambda)=f(x)+\lambda g(x)
\]

với `λ≥0` cho ràng buộc bất đẳng thức.

Hệ số Lagrange có thể được diễn giải như “giá bóng” của ràng buộc: chi phí biên của việc siết ràng buộc thêm một chút.

Ý tưởng này xuất hiện trong ràng buộc công bằng, phân bổ tài nguyên và học tăng cường có ràng buộc.

## Tối ưu hóa trong học tăng cường

Học tăng cường tối ưu tổng phần thưởng kỳ vọng:

\[
J(\theta)=\mathbb{E}_{\tau\sim\pi_\theta}[R(\tau)]
\]

Gradient khó hơn học có giám sát vì hành động được lấy mẫu ảnh hưởng trạng thái và phần thưởng tương lai.

Định lý policy gradient dẫn tới ước lượng:

\[
\nabla_\theta J
=\mathbb{E}[R\nabla_\theta\log\pi_\theta(a\mid s)]
\]

Phương sai thường lớn, từ đó dẫn tới baseline, actor-critic và nhiều phương pháp tối ưu nâng cao.

## Tối ưu hóa trong tiền huấn luyện LLM

Hàm mục tiêu tiền huấn luyện LLM thường là entropy chéo dự đoán token tiếp theo trên tập văn bản cực lớn.

Quy mô tạo thêm nhiều thách thức:

- tổng hợp gradient phân tán;
- băng thông bộ nhớ;
- độ chính xác hỗn hợp;
- bộ nhớ trạng thái của optimizer;
- lịch tốc độ học;
- cắt gradient;
- checkpoint;
- thứ tự dữ liệu.

Vì vậy tối ưu hóa ở quy mô lớn không chỉ là phương trình toán; nó còn là bài toán hệ thống phân tán.

## Tối ưu hóa trong căn chỉnh mô hình

Tinh chỉnh theo chỉ dẫn vẫn là tối ưu có giám sát trên câu trả lời đã được tuyển chọn.

Tối ưu theo sở thích dùng dữ liệu ưu tiên từ con người hoặc mô hình. RLHF, PPO và DPO tương ứng với những cách xây dựng hàm mục tiêu khác nhau.

Điểm quan trọng là bộ tối ưu không hiểu “hữu ích” hay “an toàn” theo nghĩa con người. Nó chỉ nhìn thấy hàm toán học được xây từ dữ liệu, phần thưởng và sở thích.

> **Bộ tối ưu rất giỏi tìm thứ mà hàm mục tiêu thưởng, chứ không tự hiểu ý định mơ hồ của người thiết kế.**

Đây là liên kết cốt lõi với vấn đề căn chỉnh.

## Khai thác phần thưởng và lách đặc tả

Nếu mục tiêu đại diện không khớp hoàn toàn với kết quả mong muốn, tác nhân hoặc mô hình có thể khai thác kẽ hở. Đây thường được gọi là **khai thác phần thưởng (reward hacking)** hoặc **lách đặc tả (specification gaming)**.

Ví dụ, một tác nhân được thưởng theo “số vật được nhặt” có thể liên tục nhặt rồi thả cùng một vật nếu môi trường cho phép và định nghĩa phần thưởng không ngăn việc đó.

Trong sản phẩm học máy, tối ưu chỉ tỷ lệ nhấp có thể khuyến khích nội dung gây sốc dù mức hài lòng dài hạn của người dùng giảm.

Tối ưu hóa có thể khuếch đại sai lầm trong cách thiết kế chỉ số.

## Trực giác “không có thuật toán tốt nhất cho mọi bài toán”

Không có bộ tối ưu hoặc mô hình nào tốt nhất trên mọi bài toán có thể có. Hiệu năng phụ thuộc vào cấu trúc và thiên kiến quy nạp của lớp nhiệm vụ.

Adam mạnh trong nhiều bài toán học sâu, nhưng không có định lý rằng “Adam luôn tốt nhất”. Giá trị mặc định của siêu tham số cũng chỉ là kiến thức tiên nghiệm theo miền, không phải hằng số phổ quát.

## Mô hình tư duy (mental model)

```text
Kiến trúc mô hình  → những hàm có thể biểu diễn
Hàm mất mát/mục tiêu → hành vi nào được thưởng
Gradient           → tín hiệu hướng cục bộ
Bộ tối ưu          → quy tắc biến tín hiệu thành cập nhật tham số
Lịch học           → độ lớn cập nhật thay đổi theo thời gian
Điều chuẩn         → ưu tiên ngoài việc khớp dữ liệu huấn luyện
Ràng buộc          → giới hạn hệ thống không được vượt
Đánh giá           → mục tiêu toán học có thật sự khớp kết quả mong muốn không
```

## Các hiểu lầm thường gặp

### “Hàm mất mát càng thấp thì mô hình càng tốt”

Chỉ đúng đối với hàm mục tiêu và tập dữ liệu đang tối ưu. Khả năng khái quát hóa, hiệu chuẩn, an toàn và chỉ số sản phẩm có thể khác.

### “Adam luôn tốt hơn SGD vì hiện đại hơn”

Lựa chọn optimizer phụ thuộc vào nhiệm vụ, cách tinh chỉnh và mục tiêu. SGD với momentum vẫn rất mạnh trong nhiều bài toán thị giác; Adam/AdamW phổ biến với Transformer.

### “Luôn phải tìm cực tiểu toàn cục”

Trong học sâu, một nghiệm có khả năng khái quát hóa tốt quan trọng hơn cực tiểu toán học tuyệt đối của hàm mất mát huấn luyện. Nhiều bộ tham số khác nhau có thể đạt mất mát gần 0.

### “Mô hình đủ mạnh thì tối ưu hóa sẽ tự tìm hành vi đúng”

Không. Bộ tối ưu trung thành với tín hiệu được cung cấp; mục tiêu đặc tả sai sẽ khuyến khích hành vi sai lệch.

## Liên kết kiến thức

Tối ưu hóa nối [Giải tích](./04_calculus_for_ai.md) với huấn luyện học máy và nối trực tiếp tới an toàn AI thông qua việc đặc tả mục tiêu. SGD và AdamW sẽ quay lại trong mạng nơ-ron; tối ưu có ràng buộc và tối ưu chính sách sẽ xuất hiện trong học tăng cường; mục tiêu sở thích sẽ xuất hiện trong căn chỉnh LLM.

Khi huấn luyện thất bại, đừng chỉ đổi optimizer. Hãy kiểm tra **hàm mục tiêu, quy mô dữ liệu, chuẩn hóa, thống kê gradient, lịch tốc độ học, kích thước lô, khởi tạo và độ chính xác số như một hệ thống liên kết**.