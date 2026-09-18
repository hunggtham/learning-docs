# Knowledge Connection — Xác suất, thông tin và entropy

Xác suất định lượng uncertainty; information theory hỏi một observation làm uncertainty giảm bao nhiêu và giới hạn của encoding/communication là gì.

## Surprise và logarithm

Một event probability cao không cung cấp nhiều surprise khi xảy ra; event hiếm cung cấp nhiều. Self-information:

```math
I(x)=-\log_2 p(x)
```

Nếu `p=1`, information 0 bits. Nếu `p=1/2`, 1 bit. Nếu `p=1/8`, 3 bits.

Log base 2 tự nhiên vì repeated binary questions halve possibilities.

## Vì sao log?

Nếu independent events A,B có joint probability `p(A)p(B)`, ta muốn information add:

```math
I(A,B)=I(A)+I(B)
```

Negative log biến probability multiplication thành addition.

## Entropy

Entropy của discrete random variable:

```math
H(X)=-\sum_xp(x)\log_2p(x)
```

là expected self-information. Distribution concentrated có entropy thấp; distribution spread đều hơn thường entropy cao.

For fair coin, entropy 1 bit. Biased coin có entropy <1 bit vì outcome predictable hơn.

## Compression

Nếu symbols có unequal probabilities, efficient codes assign shorter codewords to frequent symbols. Shannon entropy là fundamental lower-bound-like quantity cho average lossless coding length under assumptions/theorems.

ZIP/DEFLATE, Huffman coding và arithmetic coding use redundancy/predictability ở các mức khác nhau.

## Cross-entropy

Nếu true distribution `p` nhưng model predicts `q`:

```math
H(p,q)=-\sum_xp(x)\log q(x)
```

Cross-entropy penalizes assigning low probability to events that actually occur. Classification neural networks optimize empirical cross-entropy because maximizing likelihood is mathematically connected.

## KL divergence

```math
D_{KL}(p\|q)=\sum_xp(x)\log\frac{p(x)}{q(x)}
```

measures expected extra log-loss/information when using `q` instead of `p`. It is not symmetric and not a metric.

Relation:

```math
H(p,q)=H(p)+D_{KL}(p\|q)
```

Since `H(p)` fixed wrt model q, minimizing cross-entropy equals minimizing KL divergence from p to q in ideal setting.

## Decision uncertainty

Probability alone không quyết định action; cần loss/utility. An event 1% probability có thể đáng hành động nếu consequence enormous. Expected loss:

```math
E[L]=\sum_xp(x)L(x,a)
```

Decision theory kết hợp uncertainty với cost của actions/outcomes.

## Mental Model

> Probability nói “khả năng”; information nói “mức surprise khi biết outcome”; entropy là average surprise. Logarithm xuất hiện vì independent probabilities multiply nhưng information từ independent observations nên cộng.

## Worked Example: entropy của biased coin

Fair coin:

```math
H=-\frac12\log_2\frac12-\frac12\log_2\frac12=1\text{ bit}
```

Nếu heads probability 0.9:

```math
H=-0.9\log_2(0.9)-0.1\log_2(0.1)\approx0.469
```

Outcome predictable hơn nên average surprise thấp hơn. Nếu probability tiến tới 1/0, entropy tiến về 0.

## Cross-entropy trong classification

Với one-hot true class `y`, cross-entropy loss giảm thành

```math
L=-\log p_{true}
```

Model gán 0.9 cho true class chịu loss nhỏ; gán 0.01 chịu loss lớn. Log loss đặc biệt phạt confident wrong predictions. Đây là lý do probability calibration và numerical handling của very small probabilities quan trọng.

## Entropy không đồng nghĩa “hỗn loạn” theo mọi nghĩa

Trong information theory, entropy có definition cụ thể trên probability distribution. Dùng từ entropy như synonym cho disorder trong mọi context dễ gây lẫn với thermodynamic entropy hoặc colloquial “chaos”. Connection giữa các lĩnh vực là sâu nhưng cần đúng mathematical setup.

Khi chuyển domain, luôn kiểm tra definition cụ thể trước khi dùng analogy từ “entropy” ở lĩnh vực khác.

## Common Misconceptions

Entropy không đồng nghĩa disorder theo nghĩa đời thường trong mọi context. Probability nhỏ tạo self-information lớn nhưng một event hiếm không tự động quan trọng về consequence. Cross-entropy và KL divergence phụ thuộc distributions/model assumptions; KL không symmetric và không phải metric distance.

