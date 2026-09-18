# Information theory, entropy và coding

Information theory (Lý thuyết thông tin / 정보이론) hỏi một câu tưởng như trừu tượng: **một observation mang bao nhiêu information?** Claude Shannon biến câu hỏi đó thành toán bằng cách liên hệ information với probability.

## Surprise và self-information

Nếu một event rất chắc chắn xảy ra, việc quan sát nó cho ít thông tin mới. Nếu event rất hiếm xảy ra, observation đó surprising hơn.

Một measure phù hợp là

```math
I(x)=-\log_b P(x).
```

Nếu dùng base 2, unit là bit.

Tại sao logarithm? Vì independent events có probabilities nhân:

```math
P(x,y)=P(x)P(y).
```

Ta muốn information cộng:

```math
I(x,y)=I(x)+I(y).
```

Log biến multiplication thành addition.

## Entropy là expected surprise

Với discrete random variable `X`:

```math
H(X)=-\sum_x p(x)\log_2 p(x).
```

Đây là expected number of bits of surprise theo distribution.

Nếu `X` chắc chắn chỉ nhận một value, entropy bằng 0. Nếu `X` uniform trên `N` outcomes:

```math
H(X)=\log_2N.
```

Uniform maximizes entropy khi support cố định vì uncertainty phân tán đều nhất.

## Coding interpretation

Giả sử symbols xuất hiện với probabilities khác nhau. Nếu dùng fixed-length code, mỗi symbol cần cùng số bits. Nhưng nếu common symbols có code ngắn và rare symbols code dài, average length có thể giảm.

Shannon's source coding theorem nói entropy là lower bound nền tảng cho average lossless code length trong asymptotic setting, và practical codes có thể tiến gần bound này.

Huffman coding xây prefix code dựa trên frequencies. Arithmetic coding encode cả sequence bằng interval refinement và có thể tiến gần entropy hơn trong nhiều settings.

## Prefix code và Kraft inequality

Prefix code không cho codeword nào là prefix của codeword khác, nhờ đó sequence có thể decode unambiguously mà không cần separator.

Nếu codeword lengths là `l_i`, Kraft inequality cho binary prefix codes:

```math
\sum_i 2^{-l_i}\le1.
```

Đây là geometric capacity constraint của binary tree: codewords tương ứng leaves và một chosen leaf chặn descendants khỏi được dùng.

## Joint entropy và conditional entropy

Joint entropy:

```math
H(X,Y)
```

đo uncertainty của pair. Conditional entropy:

```math
H(Y\mid X)
```

đo uncertainty còn lại về `Y` sau khi biết `X`.

Chain rule:

```math
H(X,Y)=H(X)+H(Y\mid X).
```

Nó phản ánh accounting: uncertainty về pair = uncertainty của X + phần uncertainty thêm về Y sau khi X đã biết.

## Mutual information

Mutual information:

```math
I(X;Y)=H(X)-H(X\mid Y)
```

cũng bằng

```math
I(X;Y)=H(X)+H(Y)-H(X,Y).
```

Nó đo amount of uncertainty về X được giảm khi biết Y.

Nếu independent, knowing Y không giúp gì nên

```math
I(X;Y)=0.
```

Mutual information detect general statistical dependence, không chỉ linear dependence như correlation.

## Cross-entropy và KL divergence

Nếu true distribution là `p` nhưng model dùng `q`, cross-entropy:

```math
H(p,q)=-\sum_x p(x)\log q(x).
```

KL divergence:

```math
D_{KL}(p\|q)=\sum_x p(x)\log\frac{p(x)}{q(x)}.
```

Relationship:

```math
H(p,q)=H(p)+D_{KL}(p\|q).
```

Vì `H(p)` không phụ thuộc model `q`, minimizing cross-entropy tương đương minimizing KL divergence từ true distribution tới model trong setup phù hợp.

Đây là lý do cross-entropy loss xuất hiện tự nhiên trong classification, không phải chỉ vì “deep learning dùng nó”.

## Error-correcting codes

Communication channel có thể flip hoặc erase bits. Error-correcting code thêm redundancy có cấu trúc để receiver detect/correct errors.

Hamming distance giữa codewords là số positions khác nhau. Nếu minimum distance là `d`, code có thể detect tới `d-1` errors và correct tới

```math
\left\lfloor\frac{d-1}{2}\right\rfloor
```

errors trong simple adversarial bit-flip model.

Redundancy không đối lập efficiency; nó mua reliability dưới noise.

## Channel capacity

Shannon channel coding theorem đặt một boundary sâu: dưới channel capacity, tồn tại coding schemes cho error probability arbitrarily small với block length đủ lớn; vượt capacity thì reliable communication không thể đạt theo asymptotic model.

Capacity không nói một code cụ thể đơn giản thế nào; nó nói limit information-theoretic của channel.

## Knowledge Connection

Entropy nối logarithm, probability và coding. Mutual information nối statistics với feature selection. Cross-entropy nối maximum likelihood với ML losses. Hamming distance nối discrete geometry với coding. Compression và communication đều là bài toán representation dưới resource constraints.

## Mental Model

> Information là mức surprise được định lượng bằng log probability. Entropy là average surprise trước khi quan sát. Coding cố biến frequent patterns thành representations ngắn; communication thêm redundancy đúng chỗ để chống noise.

## Common Misconceptions

Entropy cao không tự động là “tốt” hay “xấu”; nó chỉ đo uncertainty theo model. KL divergence không symmetric nên không phải metric distance. Cross-entropy loss không phải một công thức arbitrary. Compression không thể losslessly nén mọi possible input thành shorter output vì pigeonhole principle.
