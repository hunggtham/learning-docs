# Lý thuyết thông tin cho Trí tuệ nhân tạo

**Lý thuyết thông tin (Information Theory / 정보이론)** cung cấp ngôn ngữ để định lượng **sự bất định, mức độ bất ngờ và lượng thông tin**. Trong AI, nó giải thích vì sao log-xác suất xuất hiện trong hàm mất mát, vì sao entropy chéo là mục tiêu tự nhiên cho phân loại và mô hình ngôn ngữ, vì sao độ phân kỳ KL đo mức không khớp giữa các phân phối, và vì sao nén dữ liệu có quan hệ sâu với việc học.

Điểm khởi đầu không phải công thức entropy, mà là một trực giác đơn giản: nếu một sự kiện rất dễ dự đoán xảy ra, ta học được ít điều mới; nếu một sự kiện rất bất ngờ xảy ra, lượng thông tin nhận được lớn hơn. Lý thuyết thông tin biến trực giác này thành toán học.

Xem trước: [Xác suất cho AI](./02_probability_for_ai.md).

## Tự thông tin: sự kiện càng hiếm càng mang nhiều thông tin

Với một sự kiện có xác suất `p(x)`, **tự thông tin (self-information)** hay **độ bất ngờ (surprisal)** là:

\[
I(x)=-\log p(x)
\]

Nếu `p(x)=1`, sự kiện chắc chắn và:

\[
I(x)=0
\]

Nếu sự kiện hiếm, `p(x)` nhỏ và `-log p(x)` lớn.

Logarit không phải lựa chọn tùy ý. Nó biến xác suất của các sự kiện độc lập thành lượng thông tin cộng được:

\[
I(x,y)=-\log[p(x)p(y)]=I(x)+I(y)
\]

Cơ số của log quyết định đơn vị:

- cơ số 2 → bit;
- cơ số `e` → nat.

Trong tối ưu hóa học máy, log tự nhiên thường thuận tiện hơn.

## Entropy: độ bất ngờ kỳ vọng

**Entropy (엔트로피)**:

\[
H(X)=-\sum_x p(x)\log p(x)
\]

là giá trị kỳ vọng của tự thông tin:

\[
H(X)=\mathbb{E}[-\log p(X)]
\]

Nếu phân phối hoàn toàn xác định, entropy bằng 0. Nếu `K` kết quả có xác suất bằng nhau:

\[
H(X)=\log K
\]

và đây là entropy lớn nhất trong số các phân phối rời rạc trên `K` kết quả.

Entropy không phải “độ hỗn loạn” theo nghĩa mơ hồ; nó định lượng mức bất định của biến ngẫu nhiên dưới một phân phối xác suất cụ thể.

## Ví dụ: đồng xu

Với đồng xu cân bằng:

\[
P(H)=P(T)=0.5
\]

Entropy theo cơ số 2 là:

\[
H(X)=1\text{ bit}
\]

Nếu đồng xu gần như luôn ra mặt ngửa:

\[
P(H)=0.99,\quad P(T)=0.01
\]

entropy nhỏ hơn nhiều vì kết quả dễ dự đoán hơn.

Một nguồn dữ liệu dễ dự đoán hơn thường có thể nén hiệu quả hơn. Đây là liên kết nền tảng giữa entropy và mã hóa.

## Entropy và nén dữ liệu

Lý thuyết thông tin cho biết entropy đóng vai trò giống một giới hạn dưới đối với độ dài mã trung bình dưới các giả định mã hóa lý tưởng.

Nếu một token xuất hiện rất thường xuyên, ta muốn dùng mã ngắn. Token hiếm có thể dùng mã dài hơn. Mã Huffman và mã hóa số học hiện thực hóa trực giác này theo các cách khác nhau.

Mô hình ngôn ngữ hiện đại không chỉ là bộ nén, nhưng khả năng gán xác suất cao cho chuỗi quan sát có liên hệ chặt với nén: mô hình dự đoán tốt có âm log-likelihood thấp, và chuỗi có thể được mã hóa hiệu quả hơn nếu dùng phân phối của mô hình.

## Entropy chéo

Giả sử phân phối thật là `p`, còn phân phối của mô hình là `q`.

**Entropy chéo (cross-entropy)**:

\[
H(p,q)=-\sum_x p(x)\log q(x)
\]

là lượng bit hoặc nat kỳ vọng cần dùng nếu dữ liệu thực đến từ `p` nhưng ta dự đoán hoặc mã hóa bằng `q`.

Nếu mục tiêu là một lớp one-hot `y`, hàm mất mát entropy chéo rút gọn thành:

\[
L=-\log q(y)
\]

Mô hình bị phạt mạnh khi gán xác suất thấp cho lớp đúng.

## Entropy chéo trong phân loại

Với logit `z`, softmax tạo phân phối:

\[
q_k=\frac{e^{z_k}}{\sum_j e^{z_j}}
\]

Với nhãn one-hot `y`:

\[
L=-\sum_k y_k\log q_k
\]

chỉ thành phần của lớp đúng còn lại:

\[
L=-\log q_{true}
\]

Nếu mô hình gán xác suất `0.9`, hàm mất mát khoảng `0.105`; nếu gán `0.01`, mất mát khoảng `4.605` khi dùng log tự nhiên.

Vì vậy entropy chéo không chỉ kiểm tra đúng/sai; nó còn quan tâm mô hình tự tin tới mức nào vào kết quả đúng.

## Âm log-likelihood

Nếu các quan sát độc lập khi đã biết tham số:

\[
p(D\mid\theta)=\prod_i p(y_i\mid x_i,\theta)
\]

Ước lượng hợp lý cực đại muốn:

\[
\max_\theta \prod_i p(y_i\mid x_i,\theta)
\]

Lấy log:

\[
\max_\theta \sum_i \log p(y_i\mid x_i,\theta)
\]

Tương đương tối thiểu hóa **âm log-likelihood (negative log-likelihood)**:

\[
\min_\theta -\sum_i \log p(y_i\mid x_i,\theta)
\]

Hàm mất mát entropy chéo trong phân loại là một dạng của âm log-likelihood.

## Độ phân kỳ KL

**Độ phân kỳ Kullback–Leibler (KL divergence)**:

\[
D_{KL}(p\|q)=\sum_x p(x)\log\frac{p(x)}{q(x)}
\]

có liên hệ:

\[
H(p,q)=H(p)+D_{KL}(p\|q)
\]

Vì `H(p)` không phụ thuộc vào mô hình `q`, tối thiểu hóa entropy chéo theo `q` tương đương tối thiểu hóa `D_KL(p||q)`.

KL luôn không âm và bằng 0 khi hai phân phối giống nhau gần như mọi nơi dưới các điều kiện phù hợp.

Tuy nhiên KL **không phải khoảng cách theo nghĩa metric**:

\[
D_{KL}(p\|q)\neq D_{KL}(q\|p)
\]

nói chung, và nó không thỏa bất đẳng thức tam giác.

## Hướng của KL rất quan trọng

`D_KL(p||q)` phạt rất mạnh khi `p` có khối xác suất ở nơi `q` gần 0; nó thúc đẩy `q` bao phủ những vùng mà `p` coi là có thể xảy ra.

`D_KL(q||p)` có hành vi khác và trong một số bối cảnh có xu hướng tập trung vào một mode thay vì bao phủ nhiều mode.

Trực giác này thường được mô tả bằng “bao phủ mode” và “tìm mode”, nhưng hành vi thực tế còn phụ thuộc vào họ phân phối và bài toán tối ưu hóa, nên không nên xem đây là quy tắc tuyệt đối.

Hướng của KL đặc biệt quan trọng trong suy luận biến phân, chưng cất tri thức và tối ưu hóa chính sách.

## Độ phân kỳ Jensen–Shannon

**Độ phân kỳ Jensen–Shannon (JS divergence)** được xây từ KL và phân phối trộn:

\[
m=\frac{1}{2}(p+q)
\]

\[
JS(p,q)=\frac{1}{2}D_{KL}(p\|m)+\frac{1}{2}D_{KL}(q\|m)
\]

JS đối xứng và bị chặn khi dùng cơ số log phù hợp.

Lý thuyết GAN cổ điển có liên hệ với JS divergence dưới giả định bộ phân biệt lý tưởng, dù động lực huấn luyện GAN thực tế phức tạp hơn nhiều so với biểu thức lý thuyết này.

## Entropy có điều kiện

**Entropy có điều kiện (conditional entropy)**:

\[
H(Y\mid X)
\]

đo lượng bất định còn lại về `Y` sau khi đã biết `X`.

Nếu `X` xác định hoàn toàn `Y`, entropy có điều kiện bằng 0.

Trong học có giám sát, một biểu diễn tốt lý tưởng sẽ giữ lại thông tin liên quan tới mục tiêu và làm giảm bất định về `Y`:

```text
đầu vào thô
   ↓ biểu diễn
giữ thông tin liên quan tới nhiệm vụ
   ↓
dự đoán mục tiêu với ít bất định hơn
```

Đồng thời, biểu diễn có thể loại bỏ chi tiết gây nhiễu không cần cho nhiệm vụ.

## Thông tin tương hỗ

**Thông tin tương hỗ (mutual information / 상호정보량)**:

\[
I(X;Y)=\sum_{x,y}p(x,y)\log\frac{p(x,y)}{p(x)p(y)}
\]

Có các dạng tương đương:

\[
I(X;Y)=H(X)-H(X\mid Y)
\]

\[
I(X;Y)=H(Y)-H(Y\mid X)
\]

Nó đo mức độ việc biết một biến làm giảm bất định về biến còn lại.

Nếu `X` và `Y` độc lập:

\[
I(X;Y)=0
\]

Thông tin tương hỗ có thể nắm bắt phụ thuộc phi tuyến, khác với tương quan vốn chủ yếu đo quan hệ tuyến tính.

## Thông tin tương hỗ và học biểu diễn

Ta có thể muốn biểu diễn `Z` giữ thông tin liên quan về mục tiêu `Y` nhưng bỏ bớt chi tiết gây nhiễu từ `X`:

\[
X\rightarrow Z\rightarrow Y
\]

Ý tưởng **Nút thắt thông tin (Information Bottleneck)** cân bằng giữa:

\[
I(X;Z)
\]

và:

\[
I(Z;Y)
\]

Tuy nhiên, ước lượng thông tin tương hỗ trong biểu diễn nơ-ron liên tục nhiều chiều là bài toán khó. Information Bottleneck hữu ích như một cách nhìn khái niệm; không nên mặc định rằng mọi mạng sâu thực tế đang tối ưu chính xác đại lượng này.

## Bất đẳng thức xử lý dữ liệu

Nếu có chuỗi Markov:

\[
X\rightarrow Z\rightarrow Y
\]

thì việc xử lý `X` qua `Z` không thể tự tạo thêm thông tin về `Y` từ hư không:

\[
I(X;Y)\ge I(Z;Y)
\]

khi các giả định Markov phù hợp được thỏa mãn.

Liên hệ với học biểu diễn: phép biến đổi có thể tổ chức lại thông tin để nhiệm vụ phía sau sử dụng dễ hơn, nhưng xử lý xác định không thể tự bổ sung tri thức hoàn toàn vắng mặt ở đầu vào.

Công cụ hoặc truy xuất bên ngoài có thể bổ sung thông tin mới vì chúng đưa thêm nguồn đầu vào vào hệ thống.

## Mô hình ngôn ngữ và entropy chéo

Mô hình ngôn ngữ tự hồi quy phân rã:

\[
p(x_{1:T})=\prod_{t=1}^{T}p(x_t\mid x_{<t})
\]

Âm log-likelihood:

\[
-\log p(x_{1:T})=-\sum_t\log p(x_t\mid x_{<t})
\]

Entropy chéo trung bình trên token đo mức bất ngờ trung bình mà mô hình gán cho token thực tế tiếp theo.

Huấn luyện dự đoán token tiếp theo chính là giảm độ bất ngờ trung bình trên phân phối huấn luyện.

## Perplexity

**Perplexity** thường được định nghĩa:

\[
PP=\exp(H)
\]

nếu entropy chéo dùng log tự nhiên.

Nếu entropy chéo trung bình là `H`, perplexity có thể được hiểu gần đúng như số nhánh lựa chọn hiệu dụng mà mô hình đang “phân vân”.

Tuy nhiên perplexity chỉ so sánh được khi tokenization, tập dữ liệu và giao thức đánh giá tương thích. Hai mô hình dùng tokenizer khác nhau có thể cho số perplexity không thể so trực tiếp.

Perplexity thấp cũng không bảo đảm tính đúng sự thật, tính hữu ích hoặc độ an toàn tốt hơn.

## Entropy của đầu ra mô hình

Với phân phối token tiếp theo, entropy cao nghĩa khối xác suất trải trên nhiều lựa chọn. Entropy thấp nghĩa phân phối tập trung vào ít lựa chọn hơn.

Entropy cao có thể đến từ sự mơ hồ thật sự, thiếu ngữ cảnh hoặc việc mô hình không chắc chắn; không thể suy ra nguyên nhân chỉ từ entropy.

Temperature thay đổi logit và do đó thay đổi entropy đầu ra:

\[
p_i(T)=softmax(z_i/T)
\]

Temperature cao hơn thường làm entropy tăng và đầu ra đa dạng hơn.

## KL trong chưng cất tri thức

Mô hình giáo viên tạo phân phối `p_T`, mô hình học viên tạo `p_S`.

Chưng cất tri thức có thể tối thiểu hóa:

\[
D_{KL}(p_T\|p_S)
\]

hoặc entropy chéo tương đương.

Phân phối mềm của mô hình giáo viên chứa thêm quan hệ giữa các lớp mà nhãn cứng không có. Ví dụ:

```text
chó   0.80
sói   0.12
cáo   0.05
xe    0.001
```

Mô hình học viên học cả cấu trúc này thay vì chỉ nhận nhãn `chó=1`.

## KL trong Variational Autoencoder

Hàm mục tiêu của VAE gồm thành phần tái tạo và điều chuẩn KL:

\[
\mathcal{L}_{VAE}
=\mathbb{E}_{q(z\mid x)}[\log p(x\mid z)]
-D_{KL}(q(z\mid x)\|p(z))
\]

KL kéo phân phối hậu nghiệm xấp xỉ về gần phân phối tiên nghiệm, giúp tạo không gian tiềm ẩn có cấu trúc, trong khi thành phần tái tạo giữ thông tin cần thiết để tái tạo dữ liệu.

Đây là ví dụ cụ thể của đánh đổi giữa biểu diễn và điều chuẩn.

## KL trong căn chỉnh LLM kiểu RLHF/PPO

Khi tối ưu chính sách cho LLM, thường cần tránh để mô hình trôi quá xa khỏi chính sách tham chiếu. Một thành phần phạt KL có thể xuất hiện:

\[
Reward'=Reward-\beta D_{KL}(\pi_\theta\|\pi_{ref})
\]

Ý tưởng là cải thiện phần thưởng theo sở thích nhưng vẫn giữ chính sách tương đối gần hành vi tham chiếu.

Cách triển khai chính xác khác nhau giữa các thuật toán; mô hình tư duy là KL đóng vai trò một ràng buộc tương tự vùng tin cậy.

## Entropy chéo và làm mềm nhãn

Nhãn one-hot cứng giả định lớp mục tiêu có xác suất 1 và mọi lớp khác bằng 0. **Làm mềm nhãn (label smoothing)** dùng mục tiêu:

\[
y'_k=(1-\epsilon)y_k+\epsilon/K
\]

Trong một số bài toán, nó có thể giảm tình trạng quá tự tin và đóng vai trò điều chuẩn.

Tuy nhiên làm mềm nhãn cũng thay đổi cách diễn giải hiệu chuẩn và không phải lúc nào cũng cải thiện mọi nhiệm vụ.

## Nguyên lý entropy cực đại

Nếu chỉ biết một số ràng buộc, **Nguyên lý Entropy Cực đại (Maximum Entropy Principle)** chọn phân phối có entropy lớn nhất trong số các phân phối thỏa các ràng buộc, nhằm tránh đưa thêm giả định không được bằng chứng hỗ trợ.

Ví dụ, nếu chỉ biết trung bình và phương sai trên trục số thực dưới những điều kiện phù hợp, phân phối Gaussian xuất hiện như phân phối entropy cực đại.

Ý tưởng này nối lý thuyết thông tin với mô hình xác suất: không nên mã hóa mức chắc chắn lớn hơn điều bằng chứng cho phép.

## Entropy và ra quyết định

Entropy đo bất định nhưng không trực tiếp đo thiệt hại kỳ vọng.

Hai phân phối có cùng entropy có thể dẫn tới hậu quả rất khác nếu các kết quả có độ hữu dụng hoặc chi phí khác nhau.

Hệ thống AI cần tách:

```text
độ bất định
    +
hậu quả / độ hữu dụng
    ↓
quy tắc ra quyết định
```

Đây là liên kết với lý thuyết quyết định và an toàn AI.

## Độ tăng thông tin

**Độ tăng thông tin (information gain)** có thể hiểu như mức giảm entropy:

\[
IG=H(Y)-H(Y\mid X)
\]

Trong một cách xây dựng phổ biến, cây quyết định dùng entropy hoặc information gain để chọn điểm chia.

Học chủ động (active learning) cũng có thể chọn mẫu dự kiến làm giảm bất định nhiều nhất, dù hàm lựa chọn thực tế có nhiều biến thể.

## Nén và khái quát hóa: một liên kết cần dùng thận trọng

Có một liên hệ sâu giữa nén và học: quy luật giúp mô tả dữ liệu ngắn hơn, còn mô hình khái quát hóa tốt thường nắm bắt cấu trúc có thể tái sử dụng thay vì chỉ ghi nhớ dữ liệu thô.

**Độ dài mô tả tối thiểu (Minimum Description Length - MDL)** chính thức hóa một góc nhìn: lời giải thích tốt cân bằng độ phức tạp của mô hình với chi phí mã hóa dữ liệu.

Tuy nhiên “nén tốt = thông minh” không phải tương đương phổ quát. Mục tiêu nén nào, dữ liệu nào và năng lực phía sau nào đều quan trọng.

## Mô hình tư duy (mental model)

```text
Độ bất ngờ        = sự kiện hiếm mang nhiều thông tin
Entropy            = bất định / độ bất ngờ kỳ vọng
Entropy chéo       = chi phí khi dữ liệu từ p nhưng dự đoán bằng q
KL divergence      = mức không khớp bổ sung giữa hai phân phối
Thông tin tương hỗ = lượng thông tin chia sẻ giữa các biến
Perplexity         = dạng mũ của bất định trung bình trên token
Nén                = khai thác cấu trúc dự đoán được để mã hóa ngắn hơn
```

## Các hiểu lầm thường gặp

### “Entropy cao nghĩa là dữ liệu xấu”

Không. Entropy chỉ nói mức bất định dưới một phân phối. Nhiệm vụ vốn mơ hồ có thể có entropy cao dù dữ liệu hoàn toàn hợp lệ.

### “KL divergence là khoảng cách”

KL không đối xứng và không thỏa bất đẳng thức tam giác.

### “Perplexity thấp nghĩa LLM tốt hơn ở mọi mặt”

Perplexity đo khả năng dự đoán token tiếp theo trên tập đánh giá; nó không trực tiếp đo tính đúng sự thật, khả năng suy luận, độ an toàn hoặc khả năng làm theo chỉ dẫn.

### “Cross-entropy chỉ là công thức loss do framework chọn”

Entropy chéo có thể được suy ra từ likelihood và lý thuyết thông tin. Hiểu nguồn gốc này giúp biết khi nào hàm mất mát phù hợp.

## Liên kết kiến thức

Lý thuyết thông tin nối [Xác suất](./02_probability_for_ai.md), [Thống kê](./03_statistics_for_ai.md) và [Tối ưu hóa](./06_optimization.md) với các hàm mục tiêu trong học máy. Sau này entropy, cross-entropy, KL và thông tin tương hỗ sẽ quay lại trong cây quyết định, mạng nơ-ron, mô hình ngôn ngữ, VAE, chưng cất tri thức và căn chỉnh.

Khi gặp một đại lượng thuộc lý thuyết thông tin, hãy hỏi: **đang so sánh phân phối nào, kỳ vọng lấy theo phân phối nào, log dùng đơn vị gì, và đại lượng đó trực tiếp phản ánh mục tiêu sản phẩm hay chỉ là đại diện thay thế?**