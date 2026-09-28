# Thông tin (information / 정보) lý thuyết (theory / 이론) cho Artificial Intelligence

> **Mạch đọc:** Đặt **thông tin (information / 정보) lý thuyết (theory / 이론) cho Artificial Intelligence** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Self-information: sự kiện (event / 이벤트) càng hiếm càng informative** sang **Entropy: expected surprise**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Thông tin (information / 정보) lý thuyết (theory / 이론) cung cấp một ngôn ngữ (language / 언어) để định lượng **bất định (uncertainty / 불확실성), surprise và thông tin (information / 정보)**. Trong AI, nó giải thích vì sao log-probability xuất hiện trong mất mát (loss / 손실) functions, vì sao cross-entropy là mục tiêu (objective / 목표) tự nhiên cho classification và ngôn ngữ (language / 언어) modeling, vì sao KL divergence đo discrepancy giữa distributions, và vì sao compression có relationship sâu với học tập (learning / 학습).

Điểm khởi đầu không phải công thức entropy. Ta bắt đầu từ câu hỏi: nếu một sự kiện (event / 이벤트) rất predictable xảy ra, ta học được ít điều mới; nếu một sự kiện (event / 이벤트) rất bất ngờ xảy ra, ta nhận được nhiều thông tin (information / 정보) hơn. thông tin (information / 정보) lý thuyết (theory / 이론) biến trực giác này thành mathematics.

Xem trước: [Probability for AI](./02_probability_for_ai.md).

## Self-information: sự kiện (event / 이벤트) càng hiếm càng informative

Với sự kiện (event / 이벤트) có xác suất (probability / 확률) `p(x)`, self-information hoặc surprisal:

\[
I(x)=-\log p(x)
\]

Nếu `p(x)=1`, sự kiện (event / 이벤트) chắc chắn và:

\[
I(x)=0
\]

Nếu sự kiện (event / 이벤트) hiếm, `p(x)` nhỏ và `-log p(x)` lớn.

Logarithm không phải lựa chọn arbitrary. Nó biến xác suất (probability / 확률) của independent events thành additive thông tin (information / 정보):

\[
I(x,y)=-\log[p(x)p(y)]=I(x)+I(y)
\]

Cơ sở (base / 기반) của log quyết định đơn vị (unit / 단위):

- cơ sở (base / 기반) 2 → bits;
- cơ sở (base / 기반) `e` → nats.

Trong ML tối ưu hóa (optimization / 최적화), natural log thường convenient.

## Entropy: expected surprise

Entropy (엔트로피):

\[
H(X)=-\sum_x p(x)\log p(x)
\]

là expected self-information:

\[
H(X)=\mathbb{E}[-\log p(X)]
\]

Nếu phân phối (distribution / 분포) deterministic, entropy bằng 0. Nếu `K` outcomes equally likely:

\[
H(X)=\log K
\]

và đây là maximum entropy trên `K` discrete outcomes.

Entropy không phải “độ hỗn loạn” theo nghĩa vague. Nó định lượng bất định (uncertainty / 불확실성) của random variable under a phân phối (distribution / 분포).

## Ví dụ: coin

Fair coin:

\[
P(H)=P(T)=0.5
\]

Entropy cơ sở (base / 기반) 2:

\[
H(X)=1\văn bản (text / 텍스트){ bit}
\]

Nếu coin gần như luôn head:

\[
P(H)=0.99,\quad P(T)=0.01
\]

entropy nhỏ hơn nhiều vì kết quả (outcome / 결과) dễ predict.

Một nguồn (source / 소스) predictable hơn có thể compress tốt hơn trung bình. Đây là liên kết (connection / 연결) fundamental giữa entropy và coding.

## Entropy và compression

Thông tin (information / 정보) lý thuyết (theory / 이론) cho biết entropy là lower-bound-like quantity cho average mã (code / 코드) length dưới ideal coding các giả định (assumptions / 가정들).

Nếu đơn vị từ (token / 토큰) rất dùng chung (common / 공통), ta muốn mã (code / 코드) ngắn. đơn vị từ (token / 토큰) rare có thể dùng mã (code / 코드) dài. Huffman coding và arithmetic coding hiện thực idea này theo các cách khác nhau.

Hiện đại (modern / 현대적) ngôn ngữ (language / 언어) mô hình (model / 모델) không chỉ là compressor, nhưng ability assign high xác suất (probability / 확률) cho observed chuỗi (sequence / 시퀀스) liên quan chặt với compression: mô hình (model / 모델) predict tốt thì negative log-likelihood thấp và chuỗi (sequence / 시퀀스) có thể được encoded hiệu quả hơn theo mô hình (model / 모델) phân phối (distribution / 분포).

## Cross-entropy

Giả sử true phân phối (distribution / 분포) là `p`, mô hình (model / 모델) phân phối (distribution / 분포) là `q`.

Cross-entropy:

\[
H(p,q)=-\sum_x p(x)\log q(x)
\]

Nó là expected number of nats/bits cần nếu dữ liệu (data / 데이터) thực đến từ `p` nhưng ta encode/predict bằng `q`.

Nếu mục tiêu (target / 대상) là one-hot lớp (class / 클래스) `y`, cross-entropy mất mát (loss / 손실) reduce thành:

\[
L=-\log q(y)
\]

Mô hình (model / 모델) bị penalty mạnh nếu assign xác suất (probability / 확률) thấp cho correct lớp (class / 클래스).

## Cross-entropy trong classification

Với logits `z`, softmax tạo phân phối (distribution / 분포):

\[
q_k=\frac{e^{z_k}}{\sum_j e^{z_j}}
\]

One-hot mục tiêu (target / 대상) `y`:

\[
L=-\sum_k y_k\log q_k
\]

chỉ giữ term correct lớp (class / 클래스):

\[
L=-\log q_{true}
\]

Nếu mô hình (model / 모델) assign 0.9, mất mát (loss / 손실) khoảng `0.105`; nếu assign 0.01, mất mát (loss / 손실) khoảng `4.605` theo natural log.

Cross-entropy vì vậy không chỉ check đúng/sai. Nó quan tâm xác suất (probability / 확률) confidence của correct kết quả (outcome / 결과).

## Negative log-likelihood

Nếu observations independent conditioned on parameters:

\[
p(D\mid\theta)=\prod_i p(y_i\mid x_i,\theta)
\]

Maximum likelihood:

\[
\max_\theta \prod_i p(y_i\mid x_i,\theta)
\]

Taking log:

\[
\max_\theta \sum_i \log p(y_i\mid x_i,\theta)
\]

Tương đương minimize negative log-likelihood:

\[
\min_\theta -\sum_i \log p(y_i\mid x_i,\theta)
\]

Cross-entropy mất mát (loss / 손실) trong classification là một form của negative log-likelihood.

## KL divergence

Kullback–Leibler divergence:

\[
D_{KL}(p\|q)=\sum_x p(x)\log\frac{p(x)}{q(x)}
\]

Có định danh (identity / 식별자):

\[
H(p,q)=H(p)+D_{KL}(p\|q)
\]

Vì `H(p)` không phụ thuộc mô hình (model / 모델) `q`, minimizing cross-entropy theo `q` tương đương minimizing KL `D_KL(p||q)`.

KL luôn non-negative và bằng 0 khi distributions giống nhau almost everywhere dưới conditions phù hợp.

Nhưng KL **không phải distance chỉ số (metric / 지표)**:

\[
D_{KL}(p\|q)\neq D_{KL}(q\|p)
\]

nói chung, và không thỏa triangle inequality.

## Direction của KL matters

`D_KL(p||q)` penalty rất mạnh khi `p` có mass nơi `q` gần zero. Nó thúc `q` cover hỗ trợ (support / 지원) của `p`.

`D_KL(q||p)` có hành vi (behavior / 동작) khác: nếu `q` tránh regions nơi `p` low, nó có thể tập trung vào một chế độ (mode / 모드).

Đây là intuition “chế độ (mode / 모드) covering” vs “chế độ (mode / 모드) seeking”, nhưng thực tế phụ thuộc family distributions và tối ưu hóa (optimization / 최적화) ngữ cảnh (context / 맥락), nên không nên biến thành quy tắc (rule / 규칙) tuyệt đối.

Direction KL xuất hiện quan trọng trong variational suy luận (inference / 추론), distillation và chính sách (policy / 정책) tối ưu hóa (optimization / 최적화).

## Jensen–Shannon divergence

Jensen–Shannon divergence xây từ KL với mixture:

\[
m=\frac{1}{2}(p+q)
\]

\[
JS(p,q)=\frac{1}{2}D_{KL}(p\|m)+\frac{1}{2}D_{KL}(q\|m)
\]

Nó symmetric và bounded với log cơ sở (base / 기반) phù hợp.

GAN lý thuyết (theory / 이론) cổ điển có liên kết (connection / 연결) với JS divergence dưới ideal discriminator các giả định (assumptions / 가정들), dù practical GAN huấn luyện (training / 학습) dynamics phức tạp hơn expression lý thuyết này.

## Conditional entropy

Conditional entropy:

\[
H(Y\mid X)
\]

đo bất định (uncertainty / 불확실성) còn lại về `Y` khi đã biết `X`.

Nếu `X` fully determines `Y`, conditional entropy bằng 0.

Trong supervised học tập (learning / 학습), một biểu diễn (representation / 표현) tốt ideally giảm bất định (uncertainty / 불확실성) về mục tiêu (target / 대상):

```text
raw input
   ↓ representation
retain task-relevant information
   ↓
predict target with lower uncertainty
```

Nhưng biểu diễn (representation / 표현) có thể discard nuisance thông tin (information / 정보) không cần cho tác vụ (task / 작업).

## Mutual thông tin (information / 정보)

Mutual thông tin (information / 정보):

\[
I(X;Y)=\sum_{x,y}p(x,y)\log\frac{p(x,y)}{p(x)p(y)}
\]

Equivalent forms:

\[
I(X;Y)=H(X)-H(X\mid Y)
\]

\[
I(X;Y)=H(Y)-H(Y\mid X)
\]

Nó đo mức knowing one variable giảm bất định (uncertainty / 불확실성) về variable kia.

Nếu `X` và `Y` independent:

\[
I(X;Y)=0
\]

Mutual thông tin (information / 정보) capture nonlinear phụ thuộc (dependency / 의존성), unlike correlation which is primarily tuyến tính (linear / 선형) measure.

## Mutual thông tin (information / 정보) và biểu diễn (representation / 표현) học tập (learning / 학습)

Ta có thể muốn biểu diễn (representation / 표현) `Z` giữ thông tin (information / 정보) relevant về mục tiêu (target / 대상) `Y` nhưng bỏ nuisance details từ `X`.

Conceptually:

\[
X\rightarrow Z\rightarrow Y
\]

Thông tin (information / 정보) Bottleneck idea cân bằng:

\[
I(X;Z)
\]

và:

\[
I(Z;Y)
\]

Tuy nhiên estimating mutual thông tin (information / 정보) trong high-dimensional continuous neural representations là difficult. thông tin (information / 정보) Bottleneck hữu ích như conceptual lens, không nên assume mọi practical deep mạng (network / 네트워크) tường minh (explicit / 명시적) optimize chính xác (exact / 정확한) quantity này.

## Dữ liệu (data / 데이터) Processing Inequality

Nếu Markov chuỗi (chain / 사슬):

\[
X\rightarrow Z\rightarrow Y
\]

thì processing `X` qua `Z` không thể tạo thông tin (information / 정보) về `Y` từ nothing:

\[
I(X;Y)\ge I(Z;Y)
\]

under the Markov các giả định (assumptions / 가정들).

Liên kết (connection / 연결) với biểu diễn (representation / 표현): transformation có thể reorganize thông tin (information / 정보) cho downstream tác vụ (task / 작업) dễ use hơn, nhưng deterministic processing không magically add kiến thức (knowledge / 지식) absent from đầu vào (input / 입력).

Bên ngoài (external / 외부) tools/retrieval có thể add new thông tin (information / 정보) vì chúng introduce additional đầu vào (input / 입력) nguồn (source / 소스).

## Ngôn ngữ (language / 언어) modeling và cross-entropy

Autoregressive ngôn ngữ (language / 언어) mô hình (model / 모델) factorizes:

\[
p(x_{1:T})=\prod_{t=1}^{T}p(x_t\mid x_{<t})
\]

Negative log-likelihood:

\[
-\log p(x_{1:T})=-\sum_t\log p(x_t\mid x_{<t})
\]

Average đơn vị từ (token / 토큰) cross-entropy đo expected surprise mô hình (model / 모델) assign cho actual next tokens.

Huấn luyện (training / 학습) next-token prediction chính là giảm average surprisal trên huấn luyện (training / 학습) phân phối (distribution / 분포).

## Perplexity

Perplexity thường defined:

\[
PP=\exp(H)
\]

nếu cross-entropy dùng natural log.

Nếu average cross-entropy là `H`, perplexity có thể interpret roughly như effective branching factor: mô hình (model / 모델) “bối rối” tương đương lựa chọn giữa bao nhiêu equally likely options.

Nhưng perplexity chỉ comparable khi tokenization, dataset và evaluation giao thức (protocol / 프로토콜) tương thích. Hai các mô hình (models / 모델들) với tokenizers khác nhau có perplexity numbers không directly comparable.

Perplexity thấp cũng không guarantee better factuality, helpfulness hay an toàn (safety / 안전).

## Entropy của mô hình (model / 모델) đầu ra (output / 출력)

Với next-token phân phối (distribution / 분포), entropy cao nghĩa xác suất (probability / 확률) mass spread trên nhiều alternatives. Entropy thấp nghĩa mô hình (model / 모델) phân phối (distribution / 분포) concentrated.

High entropy có thể do genuine ambiguity, insufficient ngữ cảnh (context / 맥락) hoặc mô hình (model / 모델) bất định (uncertainty / 불확실성); không thể infer cause chỉ từ entropy.

Generation temperature thay logits và do đó đầu ra (output / 출력) entropy:

\[
p_i(T)=softmax(z_i/T)
\]

Higher temperature thường tăng entropy, tạo diversity hơn.

## KL trong kiến thức (knowledge / 지식) distillation

Teacher mô hình (model / 모델) tạo phân phối (distribution / 분포) `p_T`, student tạo `p_S`.

Distillation có thể minimize:

\[
D_{KL}(p_T\|p_S)
\]

hoặc cross-entropy tương đương theo ngữ cảnh (context / 맥락).

Soft teacher phân phối (distribution / 분포) chứa “dark kiến thức (knowledge / 지식)”: quan hệ (relation / 관계) giữa non-target classes mà hard label không chứa.

Ví dụ ảnh (image / 이미지) thật là dog, teacher có thể assign:

```text
dog 0.80
wolf 0.12
fox 0.05
car 0.001
```

Student học cấu trúc (structure / 구조) này thay vì chỉ mục tiêu (target / 대상) `dog=1`.

## KL trong Variational Autoencoder

VAE mục tiêu (objective / 목표) gồm reconstruction term và KL regularization:

\[
\mathcal{L}_{VAE}
=\mathbb{E}_{q(z\mid x)}[\log p(x\mid z)]
-D_{KL}(q(z\mid x)\|p(z))
\]

KL kéo approximate posterior về prior, tạo organized latent không gian (space / 공간), trong khi reconstruction giữ thông tin (information / 정보) cần tái tạo dữ liệu (data / 데이터).

Đây là concrete example của sự đánh đổi (trade-off / 트레이드오프) biểu diễn (representation / 표현) vs regularization.

## KL trong RLHF/PPO-style alignment

Chính sách (policy / 정책) tối ưu hóa (optimization / 최적화) cho LLM thường cần tránh mô hình (model / 모델) drift quá xa tham chiếu (reference / 참조) chính sách (policy / 정책). Một KL penalty có thể xuất hiện:

\[
Reward'=Reward-\beta D_{KL}(\pi_\theta\|\pi_{ref})
\]

Idea: improve preference reward nhưng giữ chính sách (policy / 정책) gần pretrained/tham chiếu (reference / 참조) hành vi (behavior / 동작).

Chính xác (exact / 정확한) hiện thực (implementation / 구현) khác nhau giữa algorithms; mô hình tư duy (mental model / 사고 모델) là KL đóng vai trust-region-like ràng buộc (constraint / 제약조건).

## Cross-entropy và label smoothing

Hard one-hot targets assume mục tiêu (target / 대상) lớp (class / 클래스) xác suất (probability / 확률) 1 và others 0. Label smoothing dùng mục tiêu (target / 대상) softened:

\[
y'_k=(1-\epsilon)y_k+\epsilon/K
\]

Nó có thể reduce overconfidence và act as regularization trong một số settings.

Nhưng smoothing cũng thay interpretation calibration và không universally improve every tác vụ (task / 작업).

## Maximum entropy principle

Nếu chỉ biết một số các ràng buộc (constraints / 제약조건들), Maximum Entropy Principle chọn phân phối (distribution / 분포) có entropy lớn nhất thỏa các ràng buộc (constraints / 제약조건들), tránh inject các giả định (assumptions / 가정들) không được hỗ trợ (support / 지원).

Ví dụ nếu chỉ biết mean và variance trên real line dưới conditions thích hợp, Gaussian arises as maximum-entropy phân phối (distribution / 분포).

Idea này nối thông tin (information / 정보) lý thuyết (theory / 이론) với probabilistic modeling: không nên encode certainty nhiều hơn bằng chứng (evidence / 증거) cho phép.

## Entropy và quyết định (decision / 결정) making

Entropy đo bất định (uncertainty / 불확실성), nhưng không trực tiếp đo expected harm.

Hai distributions có cùng entropy có thể có very different consequences nếu outcomes có utility/chi phí (cost / 비용) khác nhau.

AI hệ thống (system / 시스템) cần tách:

```text
uncertainty measure
        +
consequence / utility
        ↓
decision rule
```

Đây là liên kết (connection / 연결) với quyết định (decision / 결정) lý thuyết (theory / 이론) và AI an toàn (safety / 안전).

## Thông tin (information / 정보) gain

Thông tin (information / 정보) gain có thể được nhìn như reduction in entropy:

\[
IG=H(Y)-H(Y\mid X)
\]

Quyết định (decision / 결정) trees dùng entropy/thông tin (information / 정보) gain để chọn split trong một formulation phổ biến.

Active học tập (learning / 학습) cũng có thể chọn truy vấn (query / 쿼리) dự kiến giảm bất định (uncertainty / 불확실성)/thông tin (information / 정보) nhiều nhất, dù practical acquisition functions đa dạng.

## Compression và generalization: liên kết (connection / 연결) thận trọng

Có một deep liên kết (connection / 연결) giữa compression và học tập (learning / 학습): mẫu (pattern / 패턴) cho phép description ngắn hơn, còn mô hình (model / 모델) generalize thường capture reusable cấu trúc (structure / 구조) thay vì memorize raw dữ liệu (data / 데이터).

Minimum Description Length (MDL) formalizes một cách nhìn: preferred explanation balances mô hình (model / 모델) độ phức tạp (complexity / 복잡도) và dữ liệu (data / 데이터) encoding chi phí (cost / 비용).

Nhưng “compress tốt = intelligent” không phải equivalence universal. Compression mục tiêu (objective / 목표) nào, dữ liệu (data / 데이터) nào và downstream năng lực (capability / 역량) nào đều matter.

## Mô hình tư duy (mental model / 사고 모델)

```text
Surprisal          = event hiếm mang nhiều information
Entropy            = expected uncertainty/surprise
Cross-entropy      = cost khi predict data từ p bằng model q
KL divergence      = extra mismatch giữa two distributions
Mutual information = information shared giữa variables
Perplexity         = exponential form của average token uncertainty
Compression        = exploit predictable structure để encode ngắn hơn
```

## Dùng chung (common / 공통) Misconceptions

### “Entropy cao nghĩa là dữ liệu (data / 데이터) xấu”

Không. Entropy chỉ nói bất định (uncertainty / 불확실성) dưới phân phối (distribution / 분포). Một tác vụ (task / 작업) intrinsically ambiguous có thể entropy cao nhưng dữ liệu (data / 데이터) hoàn toàn valid.

### “KL divergence là distance”

KL không symmetric và không thỏa triangle inequality.

### “Perplexity thấp nghĩa LLM tốt hơn mọi mặt”

Perplexity đo next-token predictive fit trên evaluation corpus, không trực tiếp measure factuality, lập luận (reasoning / 추론), an toàn (safety / 안전) hoặc instruction following.

### “Cross-entropy chỉ là công thức mất mát (loss / 손실) do khung phần mềm (framework / 프레임워크) chọn”

Nó có derivation từ likelihood và thông tin (information / 정보) lý thuyết (theory / 이론); understanding này giúp biết khi nào mất mát (loss / 손실) phù hợp.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Thông tin (information / 정보) lý thuyết (theory / 이론) nối [Probability](./02_probability_for_ai.md), [Statistics](./03_statistics_for_ai.md) và [Optimization](./06_optimization.md) với Machine học tập (learning / 학습) objectives. Sau này entropy, cross-entropy, KL và mutual-information ideas sẽ quay lại trong quyết định (decision / 결정) Trees, Neural Networks, ngôn ngữ (language / 언어) các mô hình (models / 모델들), VAEs, Distillation và Alignment.

Khi gặp một information-theoretic quantity, hãy hỏi: phân phối (distribution / 분포) nào đang được so sánh, expectation dưới phân phối (distribution / 분포) nào, log đơn vị (unit / 단위) gì, và quantity đó có trực tiếp map tới sản phẩm (product / 제품) mục tiêu (objective / 목표) hay chỉ là proxy.

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 mathematics for ai](./00_mathematics_for_ai.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
