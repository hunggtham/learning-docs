# Information Theory cho Artificial Intelligence

Information Theory (정보이론 / lý thuyết thông tin) cung cấp một language để định lượng **uncertainty, surprise và information**. Trong AI, nó giải thích vì sao log-probability xuất hiện trong loss functions, vì sao cross-entropy là objective tự nhiên cho classification và language modeling, vì sao KL divergence đo discrepancy giữa distributions, và vì sao compression có relationship sâu với learning.

Điểm khởi đầu không phải công thức entropy. Ta bắt đầu từ câu hỏi: nếu một event rất predictable xảy ra, ta học được ít điều mới; nếu một event rất bất ngờ xảy ra, ta nhận được nhiều information hơn. Information Theory biến trực giác này thành mathematics.

Xem trước: [Probability for AI](./02_probability_for_ai.md).

## Self-information: event càng hiếm càng informative

Với event có probability `p(x)`, self-information hoặc surprisal:

\[
I(x)=-\log p(x)
\]

Nếu `p(x)=1`, event chắc chắn và:

\[
I(x)=0
\]

Nếu event hiếm, `p(x)` nhỏ và `-log p(x)` lớn.

Logarithm không phải lựa chọn arbitrary. Nó biến probability của independent events thành additive information:

\[
I(x,y)=-\log[p(x)p(y)]=I(x)+I(y)
\]

Base của log quyết định unit:

- base 2 → bits;
- base `e` → nats.

Trong ML optimization, natural log thường convenient.

## Entropy: expected surprise

Entropy (엔트로피):

\[
H(X)=-\sum_x p(x)\log p(x)
\]

là expected self-information:

\[
H(X)=\mathbb{E}[-\log p(X)]
\]

Nếu distribution deterministic, entropy bằng 0. Nếu `K` outcomes equally likely:

\[
H(X)=\log K
\]

và đây là maximum entropy trên `K` discrete outcomes.

Entropy không phải “độ hỗn loạn” theo nghĩa vague. Nó định lượng uncertainty của random variable under a distribution.

## Ví dụ: coin

Fair coin:

\[
P(H)=P(T)=0.5
\]

Entropy base 2:

\[
H(X)=1\text{ bit}
\]

Nếu coin gần như luôn head:

\[
P(H)=0.99,\quad P(T)=0.01
\]

entropy nhỏ hơn nhiều vì outcome dễ predict.

Một source predictable hơn có thể compress tốt hơn trung bình. Đây là connection fundamental giữa entropy và coding.

## Entropy và compression

Information Theory cho biết entropy là lower-bound-like quantity cho average code length dưới ideal coding assumptions.

Nếu token rất common, ta muốn code ngắn. Token rare có thể dùng code dài. Huffman coding và arithmetic coding hiện thực idea này theo các cách khác nhau.

Modern language model không chỉ là compressor, nhưng ability assign high probability cho observed sequence liên quan chặt với compression: model predict tốt thì negative log-likelihood thấp và sequence có thể được encoded hiệu quả hơn theo model distribution.

## Cross-entropy

Giả sử true distribution là `p`, model distribution là `q`.

Cross-entropy:

\[
H(p,q)=-\sum_x p(x)\log q(x)
\]

Nó là expected number of nats/bits cần nếu data thực đến từ `p` nhưng ta encode/predict bằng `q`.

Nếu target là one-hot class `y`, cross-entropy loss reduce thành:

\[
L=-\log q(y)
\]

Model bị penalty mạnh nếu assign probability thấp cho correct class.

## Cross-entropy trong classification

Với logits `z`, softmax tạo distribution:

\[
q_k=\frac{e^{z_k}}{\sum_j e^{z_j}}
\]

One-hot target `y`:

\[
L=-\sum_k y_k\log q_k
\]

chỉ giữ term correct class:

\[
L=-\log q_{true}
\]

Nếu model assign 0.9, loss khoảng `0.105`; nếu assign 0.01, loss khoảng `4.605` theo natural log.

Cross-entropy vì vậy không chỉ check đúng/sai. Nó quan tâm probability confidence của correct outcome.

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

Cross-entropy loss trong classification là một form của negative log-likelihood.

## KL divergence

Kullback–Leibler divergence:

\[
D_{KL}(p\|q)=\sum_x p(x)\log\frac{p(x)}{q(x)}
\]

Có identity:

\[
H(p,q)=H(p)+D_{KL}(p\|q)
\]

Vì `H(p)` không phụ thuộc model `q`, minimizing cross-entropy theo `q` tương đương minimizing KL `D_KL(p||q)`.

KL luôn non-negative và bằng 0 khi distributions giống nhau almost everywhere dưới conditions phù hợp.

Nhưng KL **không phải distance metric**:

\[
D_{KL}(p\|q)\neq D_{KL}(q\|p)
\]

nói chung, và không thỏa triangle inequality.

## Direction của KL matters

`D_KL(p||q)` penalty rất mạnh khi `p` có mass nơi `q` gần zero. Nó thúc `q` cover support của `p`.

`D_KL(q||p)` có behavior khác: nếu `q` tránh regions nơi `p` low, nó có thể tập trung vào một mode.

Đây là intuition “mode covering” vs “mode seeking”, nhưng thực tế phụ thuộc family distributions và optimization context, nên không nên biến thành rule tuyệt đối.

Direction KL xuất hiện quan trọng trong variational inference, distillation và policy optimization.

## Jensen–Shannon divergence

Jensen–Shannon divergence xây từ KL với mixture:

\[
m=\frac{1}{2}(p+q)
\]

\[
JS(p,q)=\frac{1}{2}D_{KL}(p\|m)+\frac{1}{2}D_{KL}(q\|m)
\]

Nó symmetric và bounded với log base phù hợp.

GAN theory cổ điển có connection với JS divergence dưới ideal discriminator assumptions, dù practical GAN training dynamics phức tạp hơn expression lý thuyết này.

## Conditional entropy

Conditional entropy:

\[
H(Y\mid X)
\]

đo uncertainty còn lại về `Y` khi đã biết `X`.

Nếu `X` fully determines `Y`, conditional entropy bằng 0.

Trong supervised learning, một representation tốt ideally giảm uncertainty về target:

```text
raw input
   ↓ representation
retain task-relevant information
   ↓
predict target with lower uncertainty
```

Nhưng representation có thể discard nuisance information không cần cho task.

## Mutual information

Mutual information (상호정보량):

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

Nó đo mức knowing one variable giảm uncertainty về variable kia.

Nếu `X` và `Y` independent:

\[
I(X;Y)=0
\]

Mutual information capture nonlinear dependency, unlike correlation which is primarily linear measure.

## Mutual information và representation learning

Ta có thể muốn representation `Z` giữ information relevant về target `Y` nhưng bỏ nuisance details từ `X`.

Conceptually:

\[
X\rightarrow Z\rightarrow Y
\]

Information Bottleneck idea cân bằng:

\[
I(X;Z)
\]

và:

\[
I(Z;Y)
\]

Tuy nhiên estimating mutual information trong high-dimensional continuous neural representations là difficult. Information Bottleneck hữu ích như conceptual lens, không nên assume mọi practical deep network explicit optimize exact quantity này.

## Data Processing Inequality

Nếu Markov chain:

\[
X\rightarrow Z\rightarrow Y
\]

thì processing `X` qua `Z` không thể tạo information về `Y` từ nothing:

\[
I(X;Y)\ge I(Z;Y)
\]

under the Markov assumptions.

Connection với representation: transformation có thể reorganize information cho downstream task dễ use hơn, nhưng deterministic processing không magically add knowledge absent from input.

External tools/retrieval có thể add new information vì chúng introduce additional input source.

## Language modeling và cross-entropy

Autoregressive language model factorizes:

\[
p(x_{1:T})=\prod_{t=1}^{T}p(x_t\mid x_{<t})
\]

Negative log-likelihood:

\[
-\log p(x_{1:T})=-\sum_t\log p(x_t\mid x_{<t})
\]

Average token cross-entropy đo expected surprise model assign cho actual next tokens.

Training next-token prediction chính là giảm average surprisal trên training distribution.

## Perplexity

Perplexity thường defined:

\[
PP=\exp(H)
\]

nếu cross-entropy dùng natural log.

Nếu average cross-entropy là `H`, perplexity có thể interpret roughly như effective branching factor: model “bối rối” tương đương lựa chọn giữa bao nhiêu equally likely options.

Nhưng perplexity chỉ comparable khi tokenization, dataset và evaluation protocol tương thích. Hai models với tokenizers khác nhau có perplexity numbers không directly comparable.

Perplexity thấp cũng không guarantee better factuality, helpfulness hay safety.

## Entropy của model output

Với next-token distribution, entropy cao nghĩa probability mass spread trên nhiều alternatives. Entropy thấp nghĩa model distribution concentrated.

High entropy có thể do genuine ambiguity, insufficient context hoặc model uncertainty; không thể infer cause chỉ từ entropy.

Generation temperature thay logits và do đó output entropy:

\[
p_i(T)=softmax(z_i/T)
\]

Higher temperature thường tăng entropy, tạo diversity hơn.

## KL trong knowledge distillation

Teacher model tạo distribution `p_T`, student tạo `p_S`.

Distillation có thể minimize:

\[
D_{KL}(p_T\|p_S)
\]

hoặc cross-entropy tương đương theo context.

Soft teacher distribution chứa “dark knowledge”: relation giữa non-target classes mà hard label không chứa.

Ví dụ image thật là dog, teacher có thể assign:

```text
dog 0.80
wolf 0.12
fox 0.05
car 0.001
```

Student học structure này thay vì chỉ target `dog=1`.

## KL trong Variational Autoencoder

VAE objective gồm reconstruction term và KL regularization:

\[
\mathcal{L}_{VAE}
=\mathbb{E}_{q(z\mid x)}[\log p(x\mid z)]
-D_{KL}(q(z\mid x)\|p(z))
\]

KL kéo approximate posterior về prior, tạo organized latent space, trong khi reconstruction giữ information cần tái tạo data.

Đây là concrete example của trade-off representation vs regularization.

## KL trong RLHF/PPO-style alignment

Policy optimization cho LLM thường cần tránh model drift quá xa reference policy. Một KL penalty có thể xuất hiện:

\[
Reward'=Reward-\beta D_{KL}(\pi_\theta\|\pi_{ref})
\]

Idea: improve preference reward nhưng giữ policy gần pretrained/reference behavior.

Exact implementation khác nhau giữa algorithms; mental model là KL đóng vai trust-region-like constraint.

## Cross-entropy và label smoothing

Hard one-hot targets assume target class probability 1 và others 0. Label smoothing dùng target softened:

\[
y'_k=(1-\epsilon)y_k+\epsilon/K
\]

Nó có thể reduce overconfidence và act as regularization trong một số settings.

Nhưng smoothing cũng thay interpretation calibration và không universally improve every task.

## Maximum entropy principle

Nếu chỉ biết một số constraints, Maximum Entropy Principle chọn distribution có entropy lớn nhất thỏa constraints, tránh inject assumptions không được support.

Ví dụ nếu chỉ biết mean và variance trên real line dưới conditions thích hợp, Gaussian arises as maximum-entropy distribution.

Idea này nối Information Theory với probabilistic modeling: không nên encode certainty nhiều hơn evidence cho phép.

## Entropy và decision making

Entropy đo uncertainty, nhưng không trực tiếp đo expected harm.

Hai distributions có cùng entropy có thể có very different consequences nếu outcomes có utility/cost khác nhau.

AI system cần tách:

```text
uncertainty measure
        +
consequence / utility
        ↓
decision rule
```

Đây là connection với Decision Theory và AI Safety.

## Information gain

Information gain có thể được nhìn như reduction in entropy:

\[
IG=H(Y)-H(Y\mid X)
\]

Decision trees dùng entropy/information gain để chọn split trong một formulation phổ biến.

Active Learning cũng có thể chọn query dự kiến giảm uncertainty/information nhiều nhất, dù practical acquisition functions đa dạng.

## Compression và generalization: connection thận trọng

Có một deep connection giữa compression và learning: pattern cho phép description ngắn hơn, còn model generalize thường capture reusable structure thay vì memorize raw data.

Minimum Description Length (MDL) formalizes một cách nhìn: preferred explanation balances model complexity và data encoding cost.

Nhưng “compress tốt = intelligent” không phải equivalence universal. Compression objective nào, data nào và downstream capability nào đều matter.

## Mental Model

```text
Surprisal          = event hiếm mang nhiều information
Entropy            = expected uncertainty/surprise
Cross-entropy      = cost khi predict data từ p bằng model q
KL divergence      = extra mismatch giữa two distributions
Mutual information = information shared giữa variables
Perplexity         = exponential form của average token uncertainty
Compression        = exploit predictable structure để encode ngắn hơn
```

## Common Misconceptions

### “Entropy cao nghĩa là data xấu”

Không. Entropy chỉ nói uncertainty dưới distribution. Một task intrinsically ambiguous có thể entropy cao nhưng data hoàn toàn valid.

### “KL divergence là distance”

KL không symmetric và không thỏa triangle inequality.

### “Perplexity thấp nghĩa LLM tốt hơn mọi mặt”

Perplexity đo next-token predictive fit trên evaluation corpus, không trực tiếp measure factuality, reasoning, safety hoặc instruction following.

### “Cross-entropy chỉ là công thức loss do framework chọn”

Nó có derivation từ likelihood và Information Theory; understanding này giúp biết khi nào loss phù hợp.

## Knowledge Connection

Information Theory nối [Probability](./02_probability_for_ai.md), [Statistics](./03_statistics_for_ai.md) và [Optimization](./06_optimization.md) với Machine Learning objectives. Sau này entropy, cross-entropy, KL và mutual-information ideas sẽ quay lại trong Decision Trees, Neural Networks, Language Models, VAEs, Distillation và Alignment.

Khi gặp một information-theoretic quantity, hãy hỏi: distribution nào đang được so sánh, expectation dưới distribution nào, log unit gì, và quantity đó có trực tiếp map tới product objective hay chỉ là proxy.