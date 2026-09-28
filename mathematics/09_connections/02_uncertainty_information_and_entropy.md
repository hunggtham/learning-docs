# Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)

> **Mạch đọc:** Đọc **liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. xác suất (probability / 확률) không phải thông tin (information / 정보)** sang **2. Vì sao logarithm xuất hiện?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Xác suất định lượng bất định (uncertainty / 불확실성). thông tin (information / 정보) lý thuyết (theory / 이론) hỏi một observation giảm bất định (uncertainty / 불확실성) bao nhiêu, biểu diễn (representation / 표현) nào encode bất định (uncertainty / 불확실성) hiệu quả, và channel nào truyền được bao nhiêu thông tin (information / 정보).

Mental luồng (flow / 흐름):

```text
uncertainty
→ probability
→ surprise
→ entropy
→ compression
→ mutual information
→ decision / loss
```

Điểm quan trọng là xác suất (probability / 확률), thông tin (information / 정보) và quyết định (decision / 결정) là ba tầng khác nhau.

## 1. xác suất (probability / 확률) không phải thông tin (information / 정보)

Một sự kiện (event / 이벤트) có xác suất (probability / 확률) `p`.

Self-information:

```math
I(x)=-\log_2 p(x).
```

Sự kiện (event / 이벤트) chắc chắn:

```math
p=1
→ I=0
```

Sự kiện (event / 이벤트) xác suất (probability / 확률) `1/8`:

```math
I=3\text{ bits}.
```

Rare sự kiện (event / 이벤트) tạo surprise lớn hơn khi xảy ra.

## 2. Vì sao logarithm xuất hiện?

Với independent events:

```math
P(A,B)=P(A)P(B).
```

Ta muốn thông tin (information / 정보) cộng:

```math
I(A,B)=I(A)+I(B).
```

Logarithm biến multiplication thành addition.

Cơ sở (base / 기반) 2 cho đơn vị (unit / 단위) bits; cơ sở (base / 기반) `e` cho nats.

## 3. Entropy là expected surprise

Với discrete random variable:

```math
H(X)=-\sum_xp(x)\log_2p(x).
```

Entropy không đo magnitude của values. Nó đo bất định (uncertainty / 불확실성) của xác suất (probability / 확률) phân phối (distribution / 분포).

Fair coin:

```math
H(X)=1\text{ bit}.
```

Biased coin `p=0.9`:

```math
H(X)\approx0.469\text{ bits}.
```

Kết quả (outcome / 결과) predictable hơn nên entropy thấp hơn.

## 4. Entropy khác variance

Variance:

```math
\operatorname{Var}(X)
```

phụ thuộc numerical values và quy mô (scale / 규모).

Entropy phụ thuộc probabilities.

Hai distributions có thể cùng entropy nhưng variance rất khác, hoặc ngược lại.

Không nên coi entropy là “một kiểu variance”.

## 5. Compression: predictability thành shorter biểu diễn (representation / 표현)

Nếu symbols không equally likely, fixed-length mã (code / 코드) waste bits.

Idea:

```text
frequent symbol → short code
rare symbol     → longer code
```

Entropy cho lower-bound-like quantity cho expected lossless mã (code / 코드) length trong suitable asymptotic setup.

Huffman coding tạo prefix mã (code / 코드) gần optimal theo symbol frequencies.

Arithmetic coding encode entire chuỗi (sequence / 시퀀스) theo xác suất (probability / 확률) intervals và có thể approach entropy closer.

## 6. Prefix codes và Kraft inequality

Nếu codeword lengths `l_i`:

```math
\sum_i2^{-l_i}\le1
```

là sức chứa (capacity / 용량) điều kiện (condition / 조건) cho nhị phân (binary / 이진) prefix mã (code / 코드).

Cây (tree / 트리) viewpoint:

```text
short codeword = leaf gần root
```

Chọn leaf sớm khối (block / 블록) toàn bộ descendants, nên short codes consume more code-tree sức chứa (capacity / 용량).

Combinatorics và cây (tree / 트리) cấu trúc (structure / 구조) gặp thông tin (information / 정보) lý thuyết (theory / 이론) ở đây.

## 7. Joint entropy và chuỗi (chain / 사슬) quy tắc (rule / 규칙)

Joint entropy:

```math
H(X,Y)
```

đo bất định (uncertainty / 불확실성) của pair.

Conditional entropy:

```math
H(Y|X)
```

đo bất định (uncertainty / 불확실성) còn lại về `Y` sau khi biết `X`.

Chuỗi (chain / 사슬) quy tắc (rule / 규칙):

```math
H(X,Y)=H(X)+H(Y|X).
```

Đây là bất định (uncertainty / 불확실성) accounting.

## 8. Mutual thông tin (information / 정보): biết Y giảm bất định (uncertainty / 불확실성) về X bao nhiêu?

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

Khác correlation, mutual thông tin (information / 정보) có thể detect nonlinear statistical dependence.

Nhưng estimate MI từ finite high-dimensional dữ liệu (data / 데이터) không trivial.

## 9. dữ liệu (data / 데이터) processing inequality

Nếu:

```text
X → Y → Z
```

là Markov chuỗi (chain / 사슬), processing `Y` thành `Z` không thể tạo thêm thông tin (information / 정보) về original `X`:

```math
I(X;Z)\le I(X;Y).
```

Mô hình tư duy (mental model / 사고 모델):

> deterministic/noisy processing có thể giữ hoặc mất relevant thông tin (information / 정보), không thể magic tạo thông tin (information / 정보) về nguồn (source / 소스) mà đầu vào (input / 입력) không chứa.

Đây là important principle trong tính năng (feature / 기능) extraction và biểu diễn (representation / 표현) học tập (learning / 학습).

## 10. Cross-entropy là expected log mất mát (loss / 손실)

Nếu true phân phối (distribution / 분포) `p` và mô hình (model / 모델) predicts `q`:

```math
H(p,q)=-\sum_xp(x)\log q(x).
```

Nếu one-hot classification mục tiêu (target / 대상):

```math
L=-\log q(y_{true}).
```

Confident wrong predictions bị phạt mạnh vì `-log q` tăng lớn khi `q→0`.

## 11. KL divergence là extra coding/log-loss chi phí (cost / 비용)

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

nên không phải ordinary chỉ số (metric / 지표).

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

với categorical đầu ra (output / 출력) chính là empirical cross-entropy up to normalization.

Hàm mất mát (loss function / 손실 함수) vì vậy xuất phát từ probabilistic mô hình (model / 모델), không phải arbitrary choice.

## 13. Entropy và calibration khác nhau

Mô hình (model / 모델) có low-entropy prediction có thể rất confident.

Nhưng confidence cao không đảm bảo calibrated.

Calibration hỏi:

```text
among predictions around 0.8,
roughly 80% có đúng không?
```

Entropy đo bất định (uncertainty / 불확실성) của prediction phân phối (distribution / 분포); calibration đo alignment xác suất (probability / 확률) với empirical frequency.

## 14. Expected mất mát (loss / 손실): xác suất (probability / 확률) chưa đủ cho hành động (action / 동작)

Quyết định (decision / 결정) `a` với kết quả (outcome / 결과) `x` có mất mát (loss / 손실):

```math
L(x,a).
```

Expected mất mát (loss / 손실):

```math
R(a)=E[L(X,a)].
```

Optimal quyết định (decision / 결정):

```math
a^*=\arg\min_aR(a).
```

Một sự kiện (event / 이벤트) xác suất (probability / 확률) 1% có thể demand hành động (action / 동작) nếu consequence rất lớn.

Xác suất (probability / 확률) answer:

```text
khả năng bao nhiêu?
```

Quyết định (decision / 결정) lý thuyết (theory / 이론) answer:

```text
nên làm gì với uncertainty đó?
```

## 15. Proper scoring rules

Log mất mát (loss / 손실) và Brier score là examples of **proper scoring rules**: expected score incentivizes reporting true probabilities under suitable các giả định (assumptions / 가정들).

Điều này quan trọng vì classification accuracy alone không reward calibrated probabilistic forecasts.

## 16. thông tin (information / 정보) gain trong trees

Decision-tree split có thể choose tính năng (feature / 기능) giảm entropy nhiều nhất.

Thông tin (information / 정보) gain:

```math
IG=H(Y)-H(Y|split).
```

Tức split hữu ích nếu biết branch làm label phân phối (distribution / 분포) predictable hơn.

Nhưng greedy cây (tree / 트리) splits không guarantee globally optimal cây (tree / 트리).

## 17. Entropy tỷ lệ (rate / 비율) cho sequences

Nếu dữ liệu (data / 데이터) có temporal dependence, per-symbol entropy không đủ.

Entropy tỷ lệ (rate / 비율) roughly đo new bất định (uncertainty / 불확실성) per additional symbol khi conditioning on longer past.

Predictable chuỗi (sequence / 시퀀스) có entropy tỷ lệ (rate / 비율) thấp dù marginal symbol phân phối (distribution / 분포) có thể nhìn balanced.

Compression algorithms exploit repeated/conditional cấu trúc (structure / 구조), không chỉ one-symbol frequency.

## 18. Channel sức chứa (capacity / 용량)

Communication channel thêm noise.

Sức chứa (capacity / 용량) hỏi maximum reliable thông tin (information / 정보) tỷ lệ (rate / 비율) dưới specified channel mô hình (model / 모델).

Nhị phân (binary / 이진) symmetric channel crossover xác suất (probability / 확률) `p` có sức chứa (capacity / 용량):

```math
C=1-H_2(p)
```

bits/use, với `H_2` nhị phân (binary / 이진) entropy.

Nếu `p=0`, sức chứa (capacity / 용량) 1 bit/use.
Nếu `p=1/2`, đầu ra (output / 출력) independent nguồn (source / 소스) nên sức chứa (capacity / 용량) 0.

## 19. Redundancy có thể tăng độ tin cậy (reliability / 신뢰성)

Compression remove redundancy để save bits.

Error-correcting coding add structured redundancy để survive noise.

Hai goals ngược hướng nhưng cùng information-theoretic khung phần mềm (framework / 프레임워크):

```text
source coding → represent efficiently
channel coding → transmit reliably
```

## 20. Entropy trong thermodynamics và ML

Thermodynamic entropy và Shannon entropy có deep mathematical connections, nhưng không nên translate informal statements trực tiếp giữa domains.

Trong ML, “maximize entropy” có chính xác (exact / 정확한) mục tiêu (objective / 목표) tùy ngữ cảnh (context / 맥락):

```text
maximum entropy modeling
entropy regularization in RL
uncertainty measures
```

Always check definition and phân phối (distribution / 분포).

## 21. Rare sự kiện (event / 이벤트) không đồng nghĩa important sự kiện (event / 이벤트)

Self-information lớn khi xác suất (probability / 확률) nhỏ.

Nhưng practical importance depends on consequence.

Example:

```text
rare harmless packet retry
vs
rare catastrophic safety failure
```

same xác suất (probability / 확률) lớp (class / 클래스) có very different quyết định (decision / 결정) significance.

Thông tin (information / 정보) và utility phải tách.

## 22. dùng chung (common / 공통) thất bại (failure / 실패) modes

### Equating entropy with disorder colloquially

Mathematical entropy cần specified xác suất (probability / 확률) mô hình (model / 모델).

### Treating cross-entropy as distance

Nó không symmetric theo general distributions.

### Ignoring calibration

Low mất mát (loss / 손실)/accuracy không automatically imply reliable probabilities.

### Estimating MI naively in high dimensions

Finite-sample độ lệch (bias / 편향) có thể lớn.

### Forgetting mô hình (model / 모델) dependence

Entropy depends on chosen random variable/biểu diễn (representation / 표현).

## Liên kết kiến thức (knowledge connection / 지식 연결)

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

## Mô hình tư duy (mental model / 사고 모델)

> xác suất (probability / 확률) mô tả bất định (uncertainty / 불확실성) trước khi biết kết quả (outcome / 결과). thông tin (information / 정보) đo bất định (uncertainty / 불확실성) giảm khi observation đến. Entropy là average bất định (uncertainty / 불확실성)/surprise theo phân phối (distribution / 분포). Nhưng hành động (action / 동작) cần thêm mất mát (loss / 손실)/utility; thông tin (information / 정보) nhiều không đồng nghĩa consequence lớn.

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 rate change and accumulation](./00_rate_change_and_accumulation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
