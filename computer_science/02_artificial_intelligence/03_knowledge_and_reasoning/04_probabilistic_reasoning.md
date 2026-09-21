# Suy luận xác suất trong Trí tuệ nhân tạo

Logic cổ điển thường hỏi một mệnh đề có được suy ra hay không. Nhưng AI trong thế giới thực hiếm khi làm việc với sự chắc chắn tuyệt đối: cảm biến có nhiễu, chẩn đoán có thể mơ hồ, ý định người dùng không rõ ràng và tri thức luôn thiếu hụt. **Suy luận xác suất (Probabilistic Reasoning / 확률적 추론)** mở rộng quá trình suy luận bằng cách biểu diễn và cập nhật mức độ tin tưởng dựa trên một mô hình xác suất.

Câu hỏi cốt lõi chuyển từ:

> Giả thuyết H có được suy ra về mặt logic không?

thành:

> Khi đã quan sát bằng chứng E, mức tin tưởng `P(H|E)` nên thay đổi như thế nào?

Xem trước: [Xác suất cho AI](../01_mathematical_foundations/02_probability_for_ai.md) và [Suy luận và lập luận](./03_inference_and_reasoning.md).

## Bất định không chỉ đến từ thiếu hiểu biết

Bất định có thể xuất phát từ nhiều nguồn khác nhau: ngẫu nhiên vốn có của quá trình, nhiễu đo lường, biến ẩn, tri thức chưa đầy đủ, dữ liệu hạn chế hoặc mô hình chỉ xấp xỉ thực tế.

Một con số xác suất duy nhất có thể trộn lẫn nhiều nguồn bất định. Thiết kế hệ thống tốt cần cố phân biệt phần nào có thể giảm khi thu thập thêm thông tin và phần nào là nhiễu không thể loại bỏ hoàn toàn.

## Cập nhật Bayes

Định lý Bayes:

\[
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}
\]

có thể đọc theo trực giác:

```text
niềm tin ban đầu (prior)
        ×
mức phù hợp của bằng chứng với giả thuyết (likelihood)
        ↓
niềm tin sau khi quan sát bằng chứng (posterior)
```

`P(E)` đóng vai trò chuẩn hóa để phân phối hậu nghiệm vẫn có tổng xác suất bằng 1.

## Dạng odds của Bayes

Bayes cũng có thể viết theo tỷ số odds:

\[
\frac{P(H\mid E)}{P(\neg H\mid E)}
=
\frac{P(H)}{P(\neg H)}
\times
\frac{P(E\mid H)}{P(E\mid\neg H)}
\]

Tỷ số likelihood cho biết bằng chứng làm thay đổi odds mạnh tới mức nào. Dạng này đặc biệt hữu ích trong kiểm định y khoa hoặc quá trình tích lũy nhiều mảnh bằng chứng.

## Tỷ lệ nền rất quan trọng

Các bài toán phát hiện sự kiện hiếm thường mắc lỗi bỏ qua **tỷ lệ nền (base rate)**.

Ngay cả một bộ kiểm tra có sensitivity và specificity cao vẫn có thể tạo rất nhiều dương tính giả nếu sự kiện thật sự cực hiếm.

Gian lận, phát hiện bất thường và cảnh báo an ninh đều phải tính tới tỷ lệ nền; nếu không, số false positive có thể áp đảo toàn bộ hệ thống.

## Kết hợp nhiều bằng chứng

Nếu `E1` và `E2` độc lập có điều kiện khi biết `H`:

\[
P(E_1,E_2\mid H)=P(E_1\mid H)P(E_2\mid H)
\]

thì có thể nhân các likelihood với nhau.

Tuy nhiên, giả định độc lập ngây thơ có thể làm bằng chứng bị đếm hai lần. Ví dụ hai tín hiệu gian lận cùng xuất phát từ một nguồn reputation IP thực chất có tương quan mạnh dù được lưu thành hai feature khác nhau.

## Naive Bayes

Naive Bayes giả định các đặc trưng độc lập có điều kiện khi đã biết lớp:

\[
P(x_1,...,x_d\mid y)=\prod_i P(x_i\mid y)
\]

Do đó:

\[
P(y\mid x)\propto P(y)\prod_i P(x_i\mid y)
\]

Giả định này thường không đúng hoàn toàn trong dữ liệu thực tế, nhưng mô hình vẫn có thể hoạt động tốt vì ranh giới quyết định thu được vẫn hữu ích và việc ước lượng tham số tương đối đơn giản.

Đây là một bài học quan trọng: một mô hình có thể sai theo nghĩa mô tả thế giới tuyệt đối nhưng vẫn hữu ích về mặt vận hành nếu các giả định của nó đủ phù hợp với mục tiêu.

## Mô hình sinh và mô hình phân biệt

Một bộ phân loại sinh (generative classifier) mô hình hóa cấu trúc chung:

\[
P(X,Y)=P(Y)P(X\mid Y)
\]

Trong khi mô hình phân biệt (discriminative model) thường mô hình trực tiếp:

\[
P(Y\mid X)
\]

Naive Bayes là mô hình sinh, còn logistic regression là mô hình phân biệt.

Mô hình sinh có khả năng mô tả hoặc sinh dữ liệu đầu vào theo lớp; mô hình phân biệt tập trung trực tiếp vào ranh giới ra quyết định.

## Biến ẩn

**Biến ẩn (latent variable)** là biến không được quan sát trực tiếp nhưng giúp giải thích dữ liệu quan sát.

\[
P(X)=\sum_z P(X,Z)
\]

hoặc trong trường hợp liên tục là một tích phân.

Ví dụ có thể là chủ đề ẩn tạo ra phân phối từ, bệnh ẩn gây ra triệu chứng, hoặc trạng thái ẩn tạo ra dữ liệu cảm biến.

Biến ẩn giúp nén cấu trúc giải thích, nhưng đồng thời làm bài toán suy luận trở nên khó hơn vì ta phải tính đến nhiều cấu hình có thể của biến không quan sát.

## Lấy biên

Khi một biến ẩn chưa biết, ta có thể loại nó ra bằng phép lấy biên (marginalization):

\[
P(X)=\sum_z P(X,Z)
\]

Về trực giác, hệ thống “cộng qua tất cả khả năng có thể xảy ra” của biến ẩn.

Nếu có nhiều biến ẩn, số tổ hợp chung tăng rất nhanh. Đây là một nguyên nhân chính khiến suy luận xác suất trở nên tốn kém.

## Điều kiện hóa

Khi quan sát bằng chứng `E=e`, hệ thống cập nhật thành:

\[
P(X\mid E=e)
\]

Trong mô hình đồ thị, bằng chứng có thể làm thay đổi mức tin tưởng của nhiều biến ở xa thông qua cấu trúc phụ thuộc.

Một hiện tượng quan trọng là **explaining away**: quan sát một kết quả chung có thể làm hai nguyên nhân vốn độc lập trở nên phụ thuộc lẫn nhau.

## Explaining away

Giả sử trộm `B` và động đất `E` đều có thể làm chuông báo động `A` kêu:

```text
B → A ← E
```

Trước khi nghe chuông, `B` và `E` có thể độc lập.

Sau khi biết `A=true`, nếu lại biết `B=true`, nhu cầu giải thích chuông bằng động đất giảm xuống. Vì vậy `B` và `E` trở nên phụ thuộc khi điều kiện hóa theo `A`.

Cấu trúc collider kiểu này rất quan trọng trong cả mô hình xác suất lẫn suy luận nhân quả.

## Độc lập có điều kiện

Ký hiệu:

\[
X\perp Y\mid Z
\]

có nghĩa là `X` và `Y` độc lập khi đã biết `Z`.

Các mô hình đồ thị xác suất sử dụng quan hệ độc lập có điều kiện để phân rã một phân phối chung rất lớn thành các thành phần nhỏ hơn.

Nếu không có cấu trúc này, một phân phối chung trên `n` biến nhị phân cần tới:

\[
2^n
\]

cấu hình xác suất.

## Phân rã phân phối

Thay vì biểu diễn trực tiếp:

\[
P(X_1,...,X_n)
\]

ta có thể dùng tích các factor cục bộ:

\[
\prod_i \phi_i(X_{S_i})
\]

Bayesian Network phân rã thành các phân phối có điều kiện cục bộ; Markov Random Field sử dụng các potential trên đồ thị vô hướng.

Đây là tương đương xác suất của nguyên tắc quen thuộc trong AI: khai thác cấu trúc thay vì liệt kê toàn bộ mọi khả năng.

## Suy luận chính xác

Các phương pháp suy luận chính xác (exact inference) có thể tính hậu nghiệm đúng theo mô hình, ví dụ:

- loại biến (variable elimination);
- lan truyền niềm tin (belief propagation) trên cây hoặc polytree;
- junction tree.

Độ phức tạp phụ thuộc rất nhiều vào cấu trúc đồ thị và treewidth, không chỉ số lượng biến.

Một mạng phụ thuộc dày đặc có thể khiến suy luận chính xác tăng theo hàm mũ.

## Loại biến

Giả sử muốn tính:

\[
P(A\mid E=e)
\]

Hệ thống có thể nhân các factor liên quan và lần lượt cộng bỏ các biến ẩn.

Thứ tự loại biến ảnh hưởng mạnh tới kích thước các factor trung gian.

Điểm này rất giống tối ưu hóa thứ tự join trong cơ sở dữ liệu: kết quả toán học giống nhau nhưng chi phí tính toán có thể khác nhau rất lớn.

## Suy luận xấp xỉ

Khi suy luận chính xác quá đắt, ta dùng phương pháp xấp xỉ, chẳng hạn Monte Carlo, importance sampling, MCMC, variational inference hoặc loopy belief propagation.

Đây là sự đánh đổi giữa tính chính xác tuyệt đối và khả năng tính toán.

Việc một thuật toán trả về một con số không có nghĩa con số đó đã hội tụ tốt hoặc gần hậu nghiệm thật; cần đánh giá sai số và chất lượng hội tụ.

## Monte Carlo

Ta lấy mẫu:

\[
z^{(1)},...,z^{(N)}\sim P
\]

và ước lượng kỳ vọng:

\[
\mathbb{E}[f(Z)]\approx\frac1N\sum_i f(z^{(i)})
\]

Với các giả định chuẩn và mẫu độc lập, sai số thường giảm cỡ `O(1/√N)`. Điều đó có nghĩa tăng độ chính xác gấp đôi có thể cần nhiều hơn đáng kể số mẫu.

## Importance sampling

Nếu khó lấy mẫu trực tiếp từ phân phối đích `p` nhưng dễ lấy mẫu từ phân phối đề xuất `q`, ta có thể dùng:

\[
\mathbb{E}_p[f(X)]
=
\mathbb{E}_q\left[f(X)\frac{p(X)}{q(X)}\right]
\]

Nếu `q` không bao phủ tốt vùng mà `p` có nhiều khối lượng xác suất, trọng số importance có thể rất lớn và phương sai của ước lượng tăng mạnh.

Ý tưởng này xuất hiện lại trong đánh giá off-policy của Reinforcement Learning.

## Markov Chain Monte Carlo

MCMC tạo một chuỗi Markov có phân phối dừng là phân phối mục tiêu.

Các phương pháp nổi tiếng gồm Metropolis–Hastings và Gibbs Sampling.

Các mẫu liên tiếp không độc lập, vì vậy phải quan tâm tới burn-in, tốc độ trộn (mixing) và chẩn đoán hội tụ. Trong không gian nhiều chiều hoặc nhiều mode, chuỗi có thể trộn rất chậm.

## Variational inference

Variational inference chọn một họ phân phối dễ xử lý `q_φ(z)` để xấp xỉ hậu nghiệm `p(z|x)` bằng bài toán tối ưu hóa.

Một mục tiêu thường gặp là:

\[
D_{KL}(q_\phi(z)\|p(z\mid x))
\]

Tương đương với tối đa hóa ELBO:

\[
\log p(x)\ge
\mathbb{E}_{q}[\log p(x,z)-\log q(z)]
\]

Cách tiếp cận này biến suy luận thành tối ưu hóa. Nó thường nhanh hơn sampling nặng, nhưng phải chấp nhận sai lệch do họ phân phối xấp xỉ.

## Maximum Likelihood và Bayes

Ước lượng hợp lý cực đại (Maximum Likelihood Estimation - MLE) chọn một điểm tham số:

\[
\theta_{MLE}=\arg\max_\theta P(D\mid\theta)
\]

Trong khi suy luận Bayes giữ cả phân phối hậu nghiệm:

\[
P(\theta\mid D)
\]

Giữ toàn bộ posterior giúp biểu diễn bất định của tham số tốt hơn, nhưng thường rất đắt với neural network lớn.

Các kỹ thuật Deep Learning theo hướng Bayes thường dùng ensemble, variational approximation hoặc các phương pháp xấp xỉ khác.

## Phân phối dự đoán

Dự đoán theo Bayes tích phân qua các tham số có thể xảy ra:

\[
P(y\mid x,D)=\int P(y\mid x,\theta)P(\theta\mid D)d\theta
\]

Thay vì cam kết vào một `θ` duy nhất, hệ thống lấy trung bình dự đoán theo mức độ hợp lý hậu nghiệm của từng tham số.

Deep ensemble tiếp cận bất định theo hướng khác bằng cách huấn luyện nhiều mô hình độc lập hoặc bán độc lập.

## Hiệu chuẩn xác suất

Một hệ suy luận xác suất không chỉ cần xếp hạng đúng mà còn cần xác suất phản ánh tần suất thực tế khi ứng dụng yêu cầu cách diễn giải đó.

Hiệu chuẩn (calibration) có thể suy giảm khi phân phối dữ liệu thay đổi.

Một mô hình được calibration tốt trên khách hàng Mỹ chưa chắc giữ nguyên chất lượng trên khách hàng Hàn Quốc nếu quan hệ điều kiện giữa các biến thay đổi.

## Bằng chứng và likelihood phụ thuộc vào mô hình

Định lý Bayes luôn đúng về mặt toán học, nhưng posterior chỉ đáng tin khi prior, likelihood và cấu trúc mô hình đủ phù hợp.

Nếu mô hình sai, Bayes vẫn tính đúng hậu nghiệm của **mô hình sai đó**.

Điều này tương tự logic hình thức: suy luận có thể hoàn toàn hợp lệ từ các tiền đề sai nhưng kết luận ngoài thực tế vẫn sai.

## Độ nhạy với prior

Khi dữ liệu ít, prior có thể ảnh hưởng rất mạnh tới posterior. Khi có nhiều dữ liệu giàu thông tin, likelihood thường chiếm ưu thế hơn trong các điều kiện thông thường.

Trong mô hình nhiều chiều, không tồn tại một khái niệm “prior hoàn toàn không mang thông tin” theo cách đơn giản; cách tham số hóa cũng ảnh hưởng.

Prior chính là một dạng thiên lệch quy nạp (inductive bias), không phải thứ cần che giấu.

## Lý thuyết quyết định Bayes

Posterior chưa phải là hành động. Để quyết định, ta kết hợp posterior với hàm mất mát hoặc utility:

\[
a^*=\arg\min_a\mathbb{E}_{\theta\mid D}[L(a,\theta)]
\]

Điểm này nối suy luận xác suất với [Ra quyết định dưới bất định](../02_search_reasoning_and_planning/06_decision_making_under_uncertainty.md).

## Mô hình đồ thị xác suất

Ba dạng quan trọng:

**Bayesian Network** dùng đồ thị có hướng không chu trình (DAG) và các phân phối điều kiện cục bộ.

**Markov Random Field** dùng đồ thị vô hướng và các potential.

**Factor Graph** tách rõ node biến và node factor.

Các biểu diễn này phơi bày cấu trúc phụ thuộc để phục vụ suy luận hiệu quả hơn.

## Hidden Markov Model

HMM có chuỗi trạng thái ẩn:

```text
Z1 → Z2 → Z3 → ...
↓    ↓    ↓
X1   X2   X3
```

Một giả định Markov phổ biến là:

\[
P(Z_t\mid Z_{<t})=P(Z_t\mid Z_{t-1})
\]

và quan sát tại thời điểm `t` phụ thuộc có điều kiện vào trạng thái ẩn hiện tại.

Các thuật toán kinh điển gồm Forward algorithm để tính likelihood hoặc filtering, Viterbi để tìm chuỗi trạng thái có xác suất cao nhất và Forward–Backward để tính posterior biên.

HMM từng là nền tảng quan trọng của speech và NLP trước thời Deep Learning.

## Kalman Filter

Trong mô hình trạng thái tuyến tính-Gaussian, Kalman Filter cho phép suy luận Bayes đệ quy chính xác với niềm tin dạng Gaussian.

Mỗi bước gồm hai pha: dự đoán trạng thái tiếp theo rồi hiệu chỉnh theo quan sát mới.

Kalman gain cân bằng độ tin cậy giữa mô hình động lực và phép đo. Đây là ví dụ rất thực tế của suy luận xác suất trong định vị, theo dõi và điều khiển.

## Lập trình xác suất

Các hệ sinh thái như Stan hay PyMC cho phép người dùng khai báo mô hình sinh rồi giao quá trình suy luận cho engine MCMC hoặc variational inference.

Cách này tách phần **đặc tả mô hình** khỏi phần **thuật toán suy luận**, tương tự tinh thần khai báo của logic programming.

Tuy nhiên chất lượng và chi phí suy luận vẫn phụ thuộc mạnh vào hình học của mô hình và thuật toán được chọn.

## Bất định trong LLM

Xác suất token tiếp theo của LLM là xác suất có điều kiện của chuỗi ngôn ngữ, không phải trực tiếp là “xác suất câu này đúng ngoài thế giới”.

\[
P(token\mid context)
\neq
P(statement\ is\ true\mid world\ evidence)
\]

Một token hoặc câu có thể có xác suất ngôn ngữ rất cao vì nghe tự nhiên, nhưng nội dung vẫn sai.

Đây là một trong những phân biệt cốt lõi để hiểu hallucination và grounding.

## Confidence do LLM tự báo cáo

Nếu hỏi LLM “Bạn tự tin bao nhiêu phần trăm?”, con số trả về vẫn là một chuỗi token được sinh bởi chính mô hình, không tự động trở thành posterior đã được hiệu chuẩn về độ đúng.

Đánh giá confidence cần quy trình riêng như calibration, ensemble, consistency signals, kiểm chứng bên ngoài hoặc mô hình chuyên biệt cho nhiệm vụ.

## Bất định trong RAG

Một hệ RAG chứa nhiều nguồn bất định:

```text
ý định truy vấn có thể chưa rõ
xếp hạng retriever có thể sai
tài liệu có thể cũ hoặc không đúng
LLM có thể diễn giải bằng chứng sai
```

Điểm retrieval chỉ là tín hiệu xếp hạng, không phải bằng chứng chắc chắn tài liệu đúng hoặc liên quan.

Reranking, citation và kiểm tra nguồn giải quyết những lớp bất định khác nhau trong pipeline.

## Mô hình tư duy

```text
Logic          → điều gì bắt buộc đúng nếu tiền đề đúng
Probability    → niềm tin phân bố thế nào dưới bất định
Bayes          → cập nhật niềm tin bằng bằng chứng
Factorization  → khai thác cấu trúc phụ thuộc
Inference      → tính posterior, marginal hoặc kỳ vọng
Approximation  → đổi một phần độ chính xác lấy khả năng tính toán
Decision       → kết hợp posterior với utility hoặc cost
```

## Các hiểu lầm thường gặp

### “Dùng Bayes thì xác suất luôn đúng”

Không. Posterior phụ thuộc hoàn toàn vào cấu trúc mô hình, prior, likelihood và chất lượng dữ liệu.

### “Xác suất của LLM là confidence về sự thật”

Không. Xác suất token tiếp theo không phải xác suất chân lý đã được calibration.

### “Suy luận chính xác luôn tốt hơn xấp xỉ”

Không nếu chi phí tính toán khiến nó không thể thực hiện. Xấp xỉ thường là lựa chọn duy nhất trong mô hình lớn.

### “Độc lập có điều kiện nghĩa là các biến không liên quan”

Không. Hai biến có thể phụ thuộc khi xét biên nhưng trở nên độc lập khi đã biết một biến thứ ba.

## Liên kết kiến thức

Suy luận xác suất nối Xác suất, Biểu diễn tri thức và Lý thuyết quyết định. [Bayesian Network](./05_bayesian_networks.md) sẽ làm rõ cấu trúc phụ thuộc có điều kiện, còn các chương Machine Learning sau này sẽ giải thích cách các phân phối này được ước lượng từ dữ liệu.