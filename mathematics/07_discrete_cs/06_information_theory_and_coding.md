# Information theory, entropy và coding: xác suất trở thành giới hạn của representation

Information theory (lý thuyết thông tin / 정보이론) hỏi ba câu lớn:

```text
một observation mang bao nhiêu information?
source có thể nén tới mức nào?
channel noisy có thể truyền reliable tới rate nào?
```

Claude Shannon biến các câu hỏi này thành toán bằng cách nối probability với logarithm.

Core chain:

```text
probability
→ surprise
→ entropy
→ compression
→ mutual information
→ channel capacity
→ coding / ML losses
```

## 1. Self-information: event hiếm mang nhiều surprise hơn

Nếu event `x` có probability `p(x)`, self-information:

```math
I(x)=-\log_b p(x).
```

Base 2 cho unit bit.

Nếu `p=1`, event chắc chắn:

```math
I=0.
```

Nếu probability nhỏ, information lớn.

## 2. Vì sao phải dùng logarithm?

Với independent events:

```math
p(x,y)=p(x)p(y).
```

Ta muốn independent pieces of information cộng:

```math
I(x,y)=I(x)+I(y).
```

Logarithm chính xác biến product probability thành sum information:

```math
-\log[p(x)p(y)]
=-\log p(x)-\log p(y).
```

Đây là structural reason, không phải arbitrary convention.

## 3. Bit nghĩa là gì?

Một fair binary choice có:

```math
p=\frac12.
```

Information:

```math
-\log_2\frac12=1\text{ bit}.
```

Một bit là amount of information của một fair yes/no resolution.

Không phải mọi stored binary digit đều mang đúng một bit of *new* information nếu data predictable/redundant.

## 4. Entropy: expected surprise

Với discrete random variable:

```math
H(X)
=-\sum_x p(x)\log_2 p(x).
```

Entropy là average self-information trước khi observation xảy ra.

Nếu variable deterministic:

```math
H(X)=0.
```

Nếu uniform trên `N` outcomes:

```math
H(X)=\log_2N.
```

Uniform maximizes entropy khi support size cố định.

## 5. Bernoulli entropy

Nếu:

```math
X\sim\operatorname{Bernoulli}(p),
```

thì:

```math
H(X)
=-p\log_2p-(1-p)\log_2(1-p).
```

Entropy maximum tại `p=0.5` và giảm về 0 khi `p→0` hoặc `1`.

Uncertainty lớn nhất khi binary outcome khó đoán nhất.

## 6. Entropy khác variance

Variance đo squared numeric spread. Entropy đo uncertainty của probability distribution.

Label values `0` và `1000` có thể thay variance mạnh nhưng nếu probabilities unchanged, Shannon entropy của discrete labels không đổi.

Hai measures trả lời questions khác nhau.

## 7. Source coding: frequent symbols nên có code ngắn

Nếu symbols có different frequencies, fixed-length code có thể lãng phí.

Lossless coding exploit predictability:

```text
common symbol → short code
rare symbol → long code
```

Average length có lower bound liên hệ entropy.

## 8. Prefix code và unique decodability

Prefix code không có codeword nào là prefix của codeword khác.

Ví dụ:

```text
A → 0
B → 10
C → 110
D → 111
```

Sequence decode unambiguously left-to-right.

Prefix structure tương ứng leaves trong binary tree.

## 9. Kraft inequality

Nếu binary prefix code lengths là `l_i`, cần:

```math
\sum_i2^{-l_i}\le1.
```

Interpretation: codeword length `l` chiếm fraction `2^{-l}` của binary-tree capacity.

Kraft inequality nối combinatorics của tree với coding feasibility.

## 10. Shannon source coding theorem intuition

Với long iid source blocks và suitable coding, average lossless bits/symbol có thể tiến gần entropy nhưng không systematically thấp hơn entropy mà vẫn decode losslessly trong asymptotic model.

Entropy là information-theoretic limit, không phải guaranteed exact compressed size cho every finite file.

Headers, block length, model mismatch và implementation overhead matter.

## 11. Huffman coding

Huffman repeatedly merges least probable symbols/subtrees để xây optimal prefix code về expected length among binary prefix codes under standard assumptions.

Code lengths roughly track:

```math
l_i\approx-\log_2p_i.
```

Nhưng integer lengths khiến Huffman không luôn đạt exact entropy.

## 12. Arithmetic coding

Arithmetic coding encode whole sequence thành subinterval of `[0,1)` dựa trên cumulative probabilities.

Nó không cần assign integer number bits independently cho each symbol, nên có thể approach entropy closer for suitable models.

Compression quality phụ thuộc probability model accuracy.

## 13. Joint entropy

```math
H(X,Y)
```

measures uncertainty của pair.

Chain rule:

```math
H(X,Y)=H(X)+H(Y|X).
```

Interpretation:

```text
uncertainty of pair
= uncertainty of first variable
+ remaining uncertainty of second after first known
```

## 14. Conditional entropy

```math
H(Y|X)
```

là average uncertainty còn lại về `Y` sau khi observe `X`.

If `Y` deterministic function of `X`:

```math
H(Y|X)=0.
```

If independent:

```math
H(Y|X)=H(Y).
```

## 15. Mutual information

```math
I(X;Y)
=H(X)-H(X|Y).
```

Equivalent:

```math
I(X;Y)=H(X)+H(Y)-H(X,Y).
```

Nó đo reduction in uncertainty about one variable gained from the other.

Mutual information symmetric:

```math
I(X;Y)=I(Y;X).
```

## 16. Mutual information detect dependence beyond correlation

Correlation đo mainly linear relation.

Mutual information bằng 0 iff variables independent under standard discrete/continuous definitions with appropriate regularity.

Do đó MI detect nonlinear dependence too.

Nhưng estimating MI từ finite high-dimensional data có thể khó và biased.

## 17. KL divergence

```math
D_{KL}(p\|q)
=
\sum_x p(x)\log\frac{p(x)}{q(x)}.
```

Interpretation: extra expected log-loss/code cost khi data thực theo `p` nhưng ta model bằng `q`.

Properties:

```text
D_KL ≥ 0
D_KL(p||q)=0 iff p=q almost everywhere
not symmetric
not triangle inequality
```

Do đó KL không phải metric distance.

## 18. Cross-entropy

```math
H(p,q)
=-\sum_xp(x)\log q(x).
```

Relationship:

```math
H(p,q)=H(p)+D_{KL}(p\|q).
```

Nếu `p` fixed, minimizing cross-entropy over model `q` equivalent to minimizing KL from `p` to `q`.

## 19. Cross-entropy loss trong classification

One-hot target class `y`, predicted probabilities `q_k`:

```math
L=-\log q_y.
```

Model bị penalty mạnh khi assign low probability cho true label.

Loss này đến từ negative log-likelihood của categorical model, không phải arbitrary deep-learning convention.

## 20. Log-likelihood và coding

Dataset iid:

```math
-\log p(D|\theta)
=
-\sum_i\log p(x_i|\theta).
```

Minimize negative log-likelihood tương đương tìm model cho shortest ideal code length under coding interpretation.

Đây là bridge sâu giữa statistics và information theory.

## 21. Data processing inequality

Nếu Markov chain:

```text
X → Y → Z
```

thì processing `Y` thành `Z` không thể tạo thêm information về `X`:

```math
I(X;Z)\le I(X;Y).
```

Interpretation: deterministic/noisy post-processing cannot magically recover information already lost.

Connection mạnh với representation learning và sufficient statistics.

## 22. Entropy rate

For sequential/stochastic process, per-symbol uncertainty may differ from marginal entropy because symbols dependent.

Entropy rate roughly measures new information per step after accounting for history.

Compression gains from exploiting temporal/context dependence.

## 23. Redundancy và compression

If source predictable, entropy thấp hơn raw fixed-width representation.

Natural language, logs, images và source code có redundancy. Compression models exploit regularities.

No compressor can losslessly shorten every possible input: pigeonhole principle forbids mapping all `n`-bit strings injectively into fewer than `n` bits.

## 24. Channel model

Communication channel maps input `X` to output `Y` probabilistically.

Noise means receiver observes uncertain version.

A code adds structured redundancy so messages remain distinguishable despite channel errors.

## 25. Channel capacity

Capacity:

```math
C=\max_{p(x)} I(X;Y)
```

for memoryless channel under standard setup.

It is maximum reliable information rate supported by channel model.

Shannon coding theorem says rates below capacity can be made arbitrarily reliable with sufficiently long codes in asymptotic setting; above capacity reliable communication is impossible.

## 26. Binary symmetric channel intuition

Bit flips with probability `p`.

Capacity:

```math
C=1-H_2(p)
```

bits/use, where `H_2` is binary entropy.

If `p=0`, capacity 1 bit/use.
If `p=0.5`, output independent of input and capacity 0.

## 27. Hamming distance

For binary strings, Hamming distance = number positions different.

Code with minimum distance `d_min` can:

```text
detect up to d_min-1 adversarial bit errors
correct up to floor((d_min-1)/2)
```

because correction regions around codewords must not overlap.

This is discrete geometry in Hamming space.

## 28. Repetition code example

Encode:

```text
0 → 000
1 → 111
```

Minimum distance 3, so can correct one bit flip by majority vote.

Rate only `1/3`; reliability purchased bằng redundancy.

Coding theory studies better trade-offs among rate, distance, complexity.

## 29. Linear codes

A binary linear code is subspace of `GF(2)^n`.

Generator matrix maps message bits to codeword.
Parity-check matrix detects whether received word satisfies code constraints.

This connects Boolean/XOR algebra, finite fields và linear algebra.

## 30. Entropy và thermodynamics: caution

Information entropy has mathematical resemblance to statistical-mechanics entropy, but units/interpretation/context differ.

There are deep connections, yet one should not casually equate “high Shannon entropy” with thermodynamic disorder without model details.

## 31. Mutual information trong feature selection

A feature `X` with high `I(X;Y)` contains predictive information about target `Y`.

But pairwise MI alone does not solve redundancy/synergy among multiple features.

Feature selection needs joint structure and finite-sample estimation caution.

## 32. Information bottleneck intuition

Representation `Z` may seek:

```text
retain information relevant to Y
compress information about raw X
```

This creates trade-off involving `I(Z;Y)` and `I(Z;X)`.

It offers an information-theoretic lens on representation learning, though practical neural training is more nuanced than the ideal formalism.

## 33. Perplexity connection

For language modeling, average cross-entropy in bits/token `H` gives perplexity:

```math
\operatorname{PPL}=2^H.
```

Perplexity can be interpreted as effective branching uncertainty under model/log base conventions.

Comparisons require same tokenization/data protocol.

## 34. Worked example: biased coin entropy

If `p=0.9`:

```math
H_2(0.9)
=-0.9\log_2 0.9-0.1\log_2 0.1
\approx0.469\text{ bits}.
```

Even though one raw observation stored naively may use one bit, average uncertainty is <1 bit because outcomes highly predictable.

## Knowledge Connection

```text
logarithm
→ probability surprise
→ entropy
→ coding length
→ KL / cross-entropy
→ likelihood / ML
→ mutual information
→ channel capacity
```

Combinatorics supplies counting limits. Probability supplies source/channel models. Linear algebra over finite fields supplies error-correcting codes. AI uses cross-entropy, KL and mutual-information concepts throughout probabilistic modeling.

## Mental Model

> Information theory treats probability as a resource accounting system. Rare events cost more bits to describe; entropy is average description uncertainty; compression removes predictable redundancy; channel coding spends redundancy to preserve information through noise.

## Common Misconceptions

Entropy cao không inherently good/bad. KL không symmetric và không phải metric. Cross-entropy is not an arbitrary loss. Mutual information high does not imply causality. Compression cannot shorten every possible input losslessly. Channel capacity is an asymptotic limit under a specified channel model, not guaranteed throughput of a real implementation.
