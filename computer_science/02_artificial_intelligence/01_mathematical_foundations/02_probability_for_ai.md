# Xác suất cho Trí tuệ nhân tạo

**Xác suất (Probability / 확률)** là ngôn ngữ để suy luận khi thông tin không đầy đủ, kết quả không chắc chắn hoặc quá trình có tính ngẫu nhiên. AI gần như luôn hoạt động trong những điều kiện như vậy: ảnh có thể mơ hồ, cảm biến có nhiễu, hành vi người dùng không hoàn toàn xác định, dữ liệu huấn luyện chỉ là một mẫu của thế giới, và mô hình ngôn ngữ không biết chắc token tiếp theo.

Điểm cốt lõi không phải “mô hình trả 0.8 nên chắc chắn đúng 80%”. Xác suất cần được hiểu như một hệ thống biểu diễn niềm tin, tần suất hoặc sự bất định dưới những giả định cụ thể. Nếu không phân biệt các cách diễn giải này, ta rất dễ đọc sai đầu ra của mô hình.

Xem trước: [Toán học cho AI](./00_mathematics_for_ai.md).

## Tại sao AI cần xác suất?

Giả sử camera nhìn thấy một hình mờ. Không đủ thông tin để khẳng định chắc chắn đó là mèo hay chó. Một quy tắc xác định buộc hệ thống chọn ngay một nhãn sẽ che mất sự bất định. Phân phối xác suất cho phép biểu diễn:

\[
P(cat\mid x)=0.65,\quad P(dog\mid x)=0.30,\quad P(other\mid x)=0.05
\]

Phân phối giữ lại nhiều thông tin hơn một nhãn cứng. Hệ thống phía sau có thể quyết định rằng `0.65` chưa đủ để tự động hành động và cần con người xem xét.

Vì vậy xác suất không chỉ là phần trang trí toán học; nó ảnh hưởng trực tiếp đến thiết kế hệ thống và quản lý rủi ro.

## Không gian mẫu, biến cố và biến ngẫu nhiên

**Không gian mẫu (sample space / 표본공간)** `Ω` là tập các kết quả có thể xảy ra.

Ví dụ tung đồng xu:

\[
\Omega=\{H,T\}
\]

Một **biến cố (event / 사건)** là một tập con của không gian mẫu.

Một **biến ngẫu nhiên (random variable / 확률변수)** ánh xạ kết quả thành một giá trị. Nếu `X` là số lần xuất hiện mặt ngửa trong hai lần tung đồng xu, `X` có thể nhận các giá trị `0,1,2`.

Trong học máy, nhãn `Y`, đặc trưng `X`, nhiễu `ε` hoặc token tiếp theo đều thường được mô hình hóa như biến ngẫu nhiên.

## Phân phối xác suất

Với biến ngẫu nhiên rời rạc `X`, **hàm khối xác suất (probability mass function)**:

\[
P(X=x)
\]

gán xác suất cho từng giá trị.

Với biến ngẫu nhiên liên tục, ta dùng **hàm mật độ xác suất (probability density function)** `p(x)`. Xác suất tại đúng một giá trị thực có thể bằng 0; đại lượng có ý nghĩa là diện tích trên một khoảng:

\[
P(a\le X\le b)=\int_a^b p(x)dx
\]

Phân biệt khối xác suất và mật độ giúp tránh hiểu lầm rằng “mật độ lớn hơn 1 là không thể”. Mật độ có thể lớn hơn 1 miễn tích phân toàn miền bằng 1.

## Xác suất đồng thời, biên và có điều kiện

**Xác suất đồng thời (joint probability)**:

\[
P(X,Y)
\]

mô tả hai biến cùng lúc.

**Xác suất biên (marginal probability)** loại một biến bằng cách cộng hoặc tích phân theo biến còn lại:

\[
P(X)=\sum_y P(X,Y=y)
\]

**Xác suất có điều kiện (conditional probability)**:

\[
P(Y\mid X)=\frac{P(X,Y)}{P(X)}
\]

mô tả phân phối của `Y` khi đã biết `X`.

Học có giám sát thường cố xấp xỉ:

\[
P(Y\mid X=x)
\]

Còn mô hình ngôn ngữ xấp xỉ:

\[
P(x_t\mid x_1,\ldots,x_{t-1})
\]

Xác suất có điều kiện là một trong những cầu nối quan trọng nhất giữa lý thuyết xác suất và học máy.

## Quy tắc nhân và quy tắc chuỗi của xác suất

Từ định nghĩa xác suất có điều kiện:

\[
P(X,Y)=P(X)P(Y\mid X)
\]

Với một chuỗi:

\[
P(x_1,\ldots,x_n)=\prod_{t=1}^{n}P(x_t\mid x_{<t})
\]

Đây là nền tảng của **mô hình ngôn ngữ tự hồi quy (autoregressive language modeling)**. LLM không cần gán xác suất cho cả câu trong một phép tính duy nhất; nó phân rã xác suất chung thành chuỗi xác suất của token tiếp theo có điều kiện trên các token trước.

Ví dụ đơn giản theo mức từ:

```text
P("I love AI")
= P("I")
× P("love" | "I")
× P("AI" | "I love")
```

Tokenization thực tế phức tạp hơn ví dụ này, nhưng cơ chế xác suất vẫn như vậy.

## Tính độc lập

Hai biến cố `A` và `B` **độc lập (independent)** nếu:

\[
P(A,B)=P(A)P(B)
\]

Tương đương:

\[
P(A\mid B)=P(A)
\]

khi xác suất được định nghĩa.

**Độc lập có điều kiện (conditional independence)** đặc biệt hữu ích trong AI. `X` và `Y` có thể phụ thuộc nhau khi nhìn tổng thể nhưng trở nên độc lập nếu đã biết `Z`.

Mạng Bayes khai thác tính độc lập có điều kiện để phân rã phân phối chung hiệu quả.

Một lỗi phổ biến là giả định độc lập chỉ vì tương quan thấp. Tương quan bằng 0 không đồng nghĩa độc lập, ngoại trừ một số phân phối đặc biệt như Gaussian đồng thời.

## Định lý Bayes

Định lý Bayes:

\[
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}
\]

Trong đó:

- `H` là **giả thuyết (hypothesis)**;
- `E` là **bằng chứng (evidence)**;
- `P(H)` là **xác suất tiên nghiệm (prior)**;
- `P(E|H)` là **khả năng xảy ra dữ liệu theo giả thuyết (likelihood)**;
- `P(H|E)` là **xác suất hậu nghiệm (posterior)**.

### Ví dụ xét nghiệm y tế

Giả sử tỷ lệ mắc bệnh trong quần thể là 1%:

\[
P(D)=0.01
\]

Xét nghiệm có độ nhạy 99%:

\[
P(+\mid D)=0.99
\]

và tỷ lệ dương tính giả 5%:

\[
P(+\mid \neg D)=0.05
\]

Ta có:

\[
P(D\mid +)=\frac{0.99\times0.01}{0.99\times0.01+0.05\times0.99}
\]

xấp xỉ `0.167`.

Một xét nghiệm có độ nhạy cao không có nghĩa người nhận kết quả dương tính có 99% khả năng mắc bệnh. **Tỷ lệ nền (base rate)** của bệnh rất quan trọng.

Trong phát hiện bất thường, gian lận và an ninh, bỏ qua tỷ lệ nền là một kiểu sai lầm nghiêm trọng.

## Tiên nghiệm, likelihood và hậu nghiệm trong học máy

Theo góc nhìn Bayes đối với tham số `θ`:

\[
p(\theta\mid D)=\frac{p(D\mid\theta)p(\theta)}{p(D)}
\]

`p(θ)` biểu diễn niềm tin tiên nghiệm. `p(D|θ)` đo mức độ tham số giải thích dữ liệu quan sát tốt đến đâu. Phân phối hậu nghiệm kết hợp cả hai.

**Ước lượng hợp lý cực đại (Maximum Likelihood Estimation - MLE)** chọn:

\[
\theta_{MLE}=\arg\max_\theta p(D\mid\theta)
\]

**Ước lượng hậu nghiệm cực đại (Maximum A Posteriori - MAP)** chọn:

\[
\theta_{MAP}=\arg\max_\theta p(D\mid\theta)p(\theta)
\]

Lấy log biến tích thành tổng:

\[
\theta_{MLE}=\arg\max_\theta \log p(D\mid\theta)
\]

Đây là lý do **âm log-likelihood (negative log-likelihood)** xuất hiện tự nhiên dưới dạng hàm mất mát.

## Kỳ vọng

Giá trị kỳ vọng của biến ngẫu nhiên rời rạc:

\[
\mathbb{E}[X]=\sum_x xP(X=x)
\]

Với biến liên tục:

\[
\mathbb{E}[X]=\int xp(x)dx
\]

Giá trị kỳ vọng không nhất thiết là một kết quả có thể xảy ra. Kỳ vọng của một lần tung xúc xắc là `3.5` dù không thể tung ra `3.5`.

Trong học máy, **rủi ro kỳ vọng (expected risk)**:

\[
R(\theta)=\mathbb{E}_{(X,Y)\sim P}[L(f_\theta(X),Y)]
\]

là mục tiêu lý tưởng trên phân phối dữ liệu thật. Tập huấn luyện chỉ cung cấp một xấp xỉ thực nghiệm.

## Phương sai, hiệp phương sai và tương quan

**Phương sai (variance)**:

\[
Var(X)=\mathbb{E}[(X-\mathbb{E}[X])^2]
\]

đo mức phân tán quanh trung bình.

**Hiệp phương sai (covariance)**:

\[
Cov(X,Y)=\mathbb{E}[(X-\mu_X)(Y-\mu_Y)]
\]

đo xu hướng hai biến thay đổi cùng nhau theo nghĩa tuyến tính.

Ma trận hiệp phương sai:

\[
\Sigma_{ij}=Cov(X_i,X_j)
\]

là đối tượng trung tâm trong thống kê nhiều biến, phân phối Gaussian và PCA.

**Tương quan (correlation)** chuẩn hóa hiệp phương sai:

\[
\rho_{XY}=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}
\]

Tương quan không suy ra quan hệ nhân quả, và tương quan thấp không có nghĩa không tồn tại quan hệ phi tuyến.

## Phân phối Bernoulli và Nhị thức

Biến Bernoulli `X∈{0,1}` với:

\[
P(X=1)=p
\]

có kỳ vọng `p` và phương sai `p(1-p)`.

Mục tiêu phân loại nhị phân thường được mô hình hóa bằng Bernoulli.

Nếu có `n` phép thử Bernoulli độc lập cùng tham số `p`, số lần thành công có **phân phối Nhị thức (Binomial distribution)**:

\[
P(K=k)=\binom{n}{k}p^k(1-p)^{n-k}
\]

## Phân phối phân loại (categorical distribution)

Phân phối categorical mở rộng Bernoulli sang `K` lớp:

\[
P(Y=k)=p_k,\quad \sum_k p_k=1
\]

Đầu ra softmax thường tham số hóa phân phối này:

\[
p_k=\frac{e^{z_k}}{\sum_j e^{z_j}}
\]

Trong mô hình ngôn ngữ, từ vựng có thể gồm hàng chục nghìn token; mỗi bước sinh tạo một phân phối categorical trên toàn bộ từ vựng.

## Phân phối Gaussian

Phân phối chuẩn hay Gaussian:

\[
p(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
\]

xuất hiện nhiều vì thuận tiện về toán và liên hệ với Định lý Giới hạn Trung tâm. Tuy nhiên, không nên mặc định mọi đại lượng thế giới thực đều tuân theo Gaussian.

Gaussian nhiều biến:

\[
\mathbf{x}\sim\mathcal{N}(\boldsymbol\mu,\Sigma)
\]

được xác định bởi vector trung bình và ma trận hiệp phương sai.

Giả định Gaussian xuất hiện trong mô hình tuyến tính, bộ lọc Kalman, mô hình xác suất và các phương pháp biến tiềm ẩn.

## Softmax không phải “máy chuyển đổi thành xác suất” kỳ diệu

Softmax biến logit thành các giá trị dương được chuẩn hóa:

\[
softmax(z_i)=\frac{e^{z_i}}{\sum_j e^{z_j}}
\]

Nếu cộng cùng hằng số `c` vào mọi logit:

\[
softmax(z_i+c)=softmax(z_i)
\]

nên softmax phụ thuộc vào quan hệ tương đối giữa các logit.

Với **nhiệt độ (temperature)** `T`:

\[
p_i=softmax\left(\frac{z_i}{T}\right)
\]

`T<1` làm phân phối sắc hơn, còn `T>1` làm phân phối phẳng hơn.

Trong sinh văn bản bằng LLM, temperature thay đổi phân phối lấy mẫu; nó không trực tiếp “làm mô hình thông minh hơn” hay bảo đảm tăng độ đúng sự thật.

## Odds và log-odds

Với xác suất `p`, **odds** là:

\[
\frac{p}{1-p}
\]

Log-odds hay logit:

\[
\log\frac{p}{1-p}
\]

Hồi quy logistic mô hình hóa log-odds như một hàm tuyến tính:

\[
\log\frac{p}{1-p}=\mathbf{w}^T\mathbf{x}+b
\]

Dùng sigmoid để đổi ngược về xác suất:

\[
p=\sigma(z)=\frac{1}{1+e^{-z}}
\]

Điều này giải thích vì sao sigmoid không phải hàm kích hoạt được chọn tùy ý trong hồi quy logistic; nó xuất hiện tự nhiên từ cách mô hình hóa log-odds.

## Kỳ vọng có điều kiện và ra quyết định

Nếu hành động `a` có độ hữu dụng `U(a,Y)`, quyết định hợp lý dưới bất định có thể chọn hành động tối đa hóa **độ hữu dụng kỳ vọng (expected utility)**:

\[
a^*=\arg\max_a \mathbb{E}[U(a,Y)\mid X]
\]

Mô hình phân loại và quyết định nghiệp vụ là hai thứ khác nhau. Mô hình có thể ước lượng xác suất gian lận, còn hệ thống phải quyết định chặn giao dịch hay yêu cầu xác minh dựa trên chi phí của dương tính giả và âm tính giả.

Vì vậy **mô hình xác suất** và **chính sách ra quyết định (decision policy)** cần được tách rõ.

## Bất định ngẫu nhiên và bất định tri thức

**Bất định ngẫu nhiên (aleatoric uncertainty)** đến từ tính ngẫu nhiên hoặc nhiễu vốn có của quá trình. Ví dụ, trong cùng ngữ cảnh người dùng vẫn có thể chọn nhiều hành động khác nhau.

**Bất định tri thức (epistemic uncertainty)** đến từ việc mô hình hoặc hệ thống thiếu tri thức/dữ liệu, và có thể giảm khi có thêm dữ liệu hữu ích.

Trong thực tế hai loại này không phải lúc nào cũng tách hoàn toàn, nhưng sự phân biệt giúp suy luận về nguyên nhân thất bại.

Một mô hình có entropy đầu ra cao có thể vì đầu vào thực sự mơ hồ hoặc vì mô hình chưa từng thấy miền dữ liệu đó. Hai trường hợp cần cách xử lý khác nhau.

## Hiệu chuẩn (calibration)

Nếu mô hình dự đoán xác suất `0.8` cho 1.000 trường hợp tương tự, một mô hình được hiệu chuẩn tốt lý tưởng sẽ đúng khoảng 80% trong nhóm đó.

Hiệu chuẩn khác với khả năng phân biệt. Một mô hình có AUC hoặc khả năng xếp hạng tốt vẫn có thể cho ước lượng xác suất kém hiệu chuẩn.

Biểu đồ độ tin cậy, Expected Calibration Error và các phương pháp như **temperature scaling** có thể được dùng để đánh giá hoặc cải thiện vấn đề này.

Trong AI rủi ro cao, xác suất không được hiệu chuẩn dễ dẫn tới ngưỡng quyết định sai.

## Lấy mẫu

Nếu phân phối là `p(x)`, **lấy mẫu (sampling)** tạo ra một kết quả ngẫu nhiên theo phân phối đó.

Sinh văn bản bằng LLM có thể sử dụng:

- giải mã tham lam (greedy decoding);
- lấy mẫu theo temperature;
- lấy mẫu top-k;
- lấy mẫu top-p, còn gọi là nucleus sampling.

Chiến lược lấy mẫu thay đổi độ đa dạng và kiểu lỗi mà không thay đổi tham số mô hình.

Giải mã tham lam là xác định, nhưng không nhất thiết tạo ra chuỗi có xác suất toàn cục cao nhất vì lựa chọn tốt nhất ở từng bước không bảo đảm tối ưu toàn cục.

## Ý tưởng Monte Carlo

Khi kỳ vọng khó tính trực tiếp:

\[
\mathbb{E}[f(X)]
\]

ta có thể lấy mẫu:

\[
X_1,\ldots,X_N\sim p(x)
\]

và xấp xỉ:

\[
\mathbb{E}[f(X)]\approx\frac{1}{N}\sum_{i=1}^{N}f(X_i)
\]

Phương pháp Monte Carlo xuất hiện trong suy luận Bayes, học tăng cường, ước lượng bất định và mô phỏng.

## Xác suất trong mô hình tạo sinh

Mô hình tạo sinh cố mô hình hóa phân phối dữ liệu hoặc một phân phối có điều kiện.

Mô hình tự hồi quy:

\[
p(x)=\prod_t p(x_t\mid x_{<t})
\]

Mô hình biến phân dùng biến tiềm ẩn:

\[
p(x)=\int p(x\mid z)p(z)dz
\]

Mô hình khuếch tán học cách đảo ngược một quá trình thêm nhiễu ngẫu nhiên.

Dù cơ chế khác nhau, xác suất vẫn là ngôn ngữ chung để mô tả quá trình sinh.

## Mô hình tư duy (mental model)

```text
Phân phối          = các kết quả có thể xảy ra và mức tin tương đối
Xác suất có điều kiện = niềm tin sau khi biết ngữ cảnh
Bayes              = cập nhật niềm tin bằng bằng chứng
Kỳ vọng            = giá trị trung bình dưới phân phối
Phương sai         = mức phân tán / bất định
Likelihood         = dữ liệu phù hợp tham số đến đâu
Lấy mẫu            = biến phân phối thành một kết quả cụ thể
Hiệu chuẩn         = xác suất đầu ra có khớp tần suất quan sát hay không
```

## Các hiểu lầm thường gặp

### “Xác suất 0.9 nghĩa là mô hình chắc chắn đúng 90%”

Chỉ có thể diễn giải như vậy khi đầu ra được hiệu chuẩn và biến cố được định nghĩa phù hợp. Điểm softmax của mạng nơ-ron có thể quá tự tin.

### “Hai biến không tương quan thì độc lập”

Không đúng nói chung. Tương quan chủ yếu đo quan hệ tuyến tính; quan hệ phi tuyến vẫn có thể tồn tại.

### “Bayes là chủ quan, frequentist là khách quan”

Đây là cách đơn giản hóa quá mức. Hai khung thống kê khác nhau ở cách mô hình hóa bất định và suy luận; cả hai đều cần giả định và lựa chọn mô hình.

### “Lấy mẫu làm mô hình bịa”

Ảo giác mô hình (hallucination) không chỉ do lấy mẫu. Giải mã tham lam vẫn có thể tạo lỗi thực tế nếu phân phối đã học hoặc ngữ cảnh không được đối chiếu với sự thật.

## Liên kết kiến thức

Xác suất là nền trực tiếp cho [Thống kê cho AI](./03_statistics_for_ai.md) và [Lý thuyết thông tin](./05_information_theory.md). Nó cũng quay lại trong phân loại, mô hình tạo sinh, mạng Bayes, học tăng cường, mô hình ngôn ngữ, hiệu chuẩn và các hệ thống nhận biết bất định.

Khi gặp một xác suất trong AI, hãy hỏi: biến ngẫu nhiên là gì, phân phối đang có điều kiện trên thông tin nào, xác suất này là ước lượng của mô hình hay tần suất quan sát, và quyết định phía sau sẽ dùng nó như thế nào.