# Knowledge Connection — Uncertainty, Information và Entropy: từ probability đến decision

Xác suất định lượng uncertainty. Information theory hỏi một observation giảm uncertainty bao nhiêu, representation nào encode uncertainty hiệu quả, và channel nào truyền được bao nhiêu information.

Mental flow:

```text
uncertainty
→ probability
→ surprise
→ entropy
→ compression
→ mutual information
→ decision / loss
```

Điểm quan trọng là probability, information và decision là ba tầng khác nhau.

## 1. Probability không phải information

Một event có probability `p`.

Self-information:

```math
I(x)=-\log_2 p(x).
```

Event chắc chắn:

```math
p=1
→ I=0
```

Event probability `1/8`:

```math
I=3\text{ bits}.
```

Rare event tạo surprise lớn hơn khi xảy ra.

## 2. Vì sao logarithm xuất hiện?

Với independent events:

```math
P(A,B)=P(A)P(B).
```

Ta muốn information cộng:

```math
I(A,B)=I(A)+I(B).
```

Logarithm biến multiplication thành addition.

Base 2 cho unit bits; base `e` cho nats.

## 3. Entropy là expected surprise

Với discrete random variable:

```math
H(X)=-\sum_xp(x)\log_2p(x).
```

Entropy không đo magnitude của values. Nó đo uncertainty của probability distribution.

Fair coin:

```math
H(X)=1\text{ bit}.
```

Biased coin `p=0.9`:

```math
H(X)\approx0.469\text{ bits}.
```

Outcome predictable hơn nên entropy thấp hơn.

## 4. Entropy khác variance

Variance:

```math
\operatorname{Var}(X)
```

phụ thuộc numerical values và scale.

Entropy phụ thuộc probabilities.

Hai distributions có thể cùng entropy nhưng variance rất khác, hoặc ngược lại.

Không nên coi entropy là “một kiểu variance”.

## 5. Compression: predictability thành shorter representation

Nếu symbols không equally likely, fixed-length code waste bits.

Idea:

```text
frequent symbol → short code
rare symbol     → longer code
```

Entropy cho lower-bound-like quantity cho expected lossless code length trong suitable asymptotic setup.

Huffman coding tạo prefix code gần optimal theo symbol frequencies.

Arithmetic coding encode entire sequence theo probability intervals và có thể approach entropy closer.

## 6. Prefix codes và Kraft inequality

Nếu codeword lengths `l_i`:

```math
\sum_i2^{-l_i}\le1
```

là capacity condition cho binary prefix code.

Tree viewpoint:

```text
short codeword = leaf gần root
```

Chọn leaf sớm block toàn bộ descendants, nên short codes consume more code-tree capacity.

Combinatorics và tree structure gặp information theory ở đây.

## 7. Joint entropy và chain rule

Joint entropy:

```math
H(X,Y)
```

đo uncertainty của pair.

Conditional entropy:

```math
H(Y|X)
```

đo uncertainty còn lại về `Y` sau khi biết `X`.

Chain rule:

```math
H(X,Y)=H(X)+H(Y|X).
```

Đây là uncertainty accounting.

## 8. Mutual information: biết Y giảm uncertainty về X bao nhiêu?

```math
I(X;Y)=H(X)-H(X|Y).
```

Tương đương:

```math
I(X;Y)=H(X)+H(Y)-H(X,Y).
```

Nếu independent:

```math
I(X;Y)=0.
```

Khác correlation, mutual information có thể detect nonlinear statistical dependence.

Nhưng estimate MI từ finite high-dimensional data không trivial.

## 9. Data processing inequality

Nếu:

```text
X → Y → Z
```

là Markov chain, processing `Y` thành `Z` không thể tạo thêm information về original `X`:

```math
I(X;Z)\le I(X;Y).
```

Mental model:

> deterministic/noisy processing có thể giữ hoặc mất relevant information, không thể magic tạo information về source mà input không chứa.

Đây là important principle trong feature extraction và representation learning.

## 10. Cross-entropy là expected log loss

Nếu true distribution `p` và model predicts `q`:

```math
H(p,q)=-\sum_xp(x)\log q(x).
```

Nếu one-hot classification target:

```math
L=-\log q(y_{true}).
```

Confident wrong predictions bị phạt mạnh vì `-log q` tăng lớn khi `q→0`.

## 11. KL divergence là extra coding/log-loss cost

```math
D_{KL}(p\|q)
=\sum_xp(x)\log\frac{p(x)}{q(x)}.
```

Relationship:

```math
H(p,q)=H(p)+D_{KL}(p\|q).
```

Vì `H(p)` không phụ thuộc `q`, minimizing cross-entropy tương đương minimizing forward KL trong idealized setup.

KL:

```text
không symmetric
không satisfy triangle inequality
```

nên không phải ordinary metric.

## 12. Maximum likelihood và cross-entropy

Dataset iid:

```math
D=\{(x_i,y_i)\}_{i=1}^n.
```

Likelihood:

```math
\prod_i p_\theta(y_i|x_i).
```

Negative log-likelihood:

```math
-\sum_i\log p_\theta(y_i|x_i).
```

với categorical output chính là empirical cross-entropy up to normalization.

Loss function vì vậy xuất phát từ probabilistic model, không phải arbitrary choice.

## 13. Entropy và calibration khác nhau

Model có low-entropy prediction có thể rất confident.

Nhưng confidence cao không đảm bảo calibrated.

Calibration hỏi:

```text
among predictions around 0.8,
roughly 80% có đúng không?
```

Entropy đo uncertainty của prediction distribution; calibration đo alignment probability với empirical frequency.

## 14. Expected loss: probability chưa đủ cho action

Decision `a` với outcome `x` có loss:

```math
L(x,a).
```

Expected loss:

```math
R(a)=E[L(X,a)].
```

Optimal decision:

```math
a^*=\arg\min_aR(a).
```

Một event probability 1% có thể demand action nếu consequence rất lớn.

Probability answer:

```text
khả năng bao nhiêu?
```

Decision theory answer:

```text
nên làm gì với uncertainty đó?
```

## 15. Proper scoring rules

Log loss và Brier score là examples of **proper scoring rules**: expected score incentivizes reporting true probabilities under suitable assumptions.

Điều này quan trọng vì classification accuracy alone không reward calibrated probabilistic forecasts.

## 16. Information gain trong trees

Decision-tree split có thể choose feature giảm entropy nhiều nhất.

Information gain:

```math
IG=H(Y)-H(Y|split).
```

Tức split hữu ích nếu biết branch làm label distribution predictable hơn.

Nhưng greedy tree splits không guarantee globally optimal tree.

## 17. Entropy rate cho sequences

Nếu data có temporal dependence, per-symbol entropy không đủ.

Entropy rate roughly đo new uncertainty per additional symbol khi conditioning on longer past.

Predictable sequence có entropy rate thấp dù marginal symbol distribution có thể nhìn balanced.

Compression algorithms exploit repeated/conditional structure, không chỉ one-symbol frequency.

## 18. Channel capacity

Communication channel thêm noise.

Capacity hỏi maximum reliable information rate dưới specified channel model.

Binary symmetric channel crossover probability `p` có capacity:

```math
C=1-H_2(p)
```

bits/use, với `H_2` binary entropy.

Nếu `p=0`, capacity 1 bit/use.
Nếu `p=1/2`, output independent source nên capacity 0.

## 19. Redundancy có thể tăng reliability

Compression remove redundancy để save bits.

Error-correcting coding add structured redundancy để survive noise.

Hai goals ngược hướng nhưng cùng information-theoretic framework:

```text
source coding → represent efficiently
channel coding → transmit reliably
```

## 20. Entropy trong thermodynamics và ML

Thermodynamic entropy và Shannon entropy có deep mathematical connections, nhưng không nên translate informal statements trực tiếp giữa domains.

Trong ML, “maximize entropy” có exact objective tùy context:

```text
maximum entropy modeling
entropy regularization in RL
uncertainty measures
```

Always check definition and distribution.

## 21. Rare event không đồng nghĩa important event

Self-information lớn khi probability nhỏ.

Nhưng practical importance depends on consequence.

Example:

```text
rare harmless packet retry
vs
rare catastrophic safety failure
```

same probability class có very different decision significance.

Information và utility phải tách.

## 22. Common failure modes

### Equating entropy with disorder colloquially

Mathematical entropy cần specified probability model.

### Treating cross-entropy as distance

Nó không symmetric theo general distributions.

### Ignoring calibration

Low loss/accuracy không automatically imply reliable probabilities.

### Estimating MI naively in high dimensions

Finite-sample bias có thể lớn.

### Forgetting model dependence

Entropy depends on chosen random variable/representation.

## Knowledge Connection

```text
Probability → uncertainty
Logarithm → additive information
Entropy → expected surprise
Trees → prefix coding
Bayes → conditional information
ML → cross-entropy / NLL
Statistics → calibration
Decision theory → expected loss
Communication → capacity / error correction
```

## Mental Model

> Probability mô tả uncertainty trước khi biết outcome. Information đo uncertainty giảm khi observation đến. Entropy là average uncertainty/surprise theo distribution. Nhưng action cần thêm loss/utility; information nhiều không đồng nghĩa consequence lớn.