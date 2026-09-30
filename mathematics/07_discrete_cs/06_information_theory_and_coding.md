# Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)

> **Mạch đọc:** Đọc **thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Self-information: sự kiện (event / 이벤트) hiếm mang nhiều surprise hơn** sang **2. Vì sao phải dùng logarithm?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Thông tin (information / 정보) lý thuyết (theory / 이론) hỏi ba câu lớn:

```text
một observation mang bao nhiêu information?
source có thể nén tới mức nào?
channel noisy có thể truyền reliable tới rate nào?
```

Claude Shannon biến các câu hỏi này thành toán bằng cách nối xác suất (probability / 확률) với logarithm.

Cốt lõi (core / 핵심) chuỗi (chain / 사슬):

```text
probability
→ surprise
→ entropy
→ compression
→ mutual information
→ channel capacity
→ coding / ML losses
```

## 1. Self-information: sự kiện (event / 이벤트) hiếm mang nhiều surprise hơn

Nếu sự kiện (event / 이벤트) `x` có xác suất (probability / 확률) `p(x)`, self-information:

```math
I(x)=-\log_b p(x).
```

Cơ sở (base / 기반) 2 cho đơn vị (unit / 단위) bit.

Nếu `p=1`, sự kiện (event / 이벤트) chắc chắn:

```math
I=0.
```

Nếu xác suất (probability / 확률) nhỏ, thông tin (information / 정보) lớn.

## 2. Vì sao phải dùng logarithm?

Với independent events:

```math
p(x,y)=p(x)p(y).
```

Ta muốn independent pieces of thông tin (information / 정보) cộng:

```math
I(x,y)=I(x)+I(y).
```

Logarithm chính xác biến sản phẩm (product / 제품) xác suất (probability / 확률) thành sum thông tin (information / 정보):

```math
-\log[p(x)p(y)]
=-\log p(x)-\log p(y).
```

Đây là structural reason, không phải arbitrary convention.

## 3. Bit nghĩa là gì?

Một fair nhị phân (binary / 이진) choice có:

```math
p=\frac12.
```

Thông tin (information / 정보):

```math
-\log_2\frac12=1\text{ bit}.
```

Một bit là amount of thông tin (information / 정보) của một fair yes/no resolution.

Không phải mọi stored nhị phân (binary / 이진) digit đều mang đúng một bit of *new* thông tin (information / 정보) nếu dữ liệu (data / 데이터) predictable/redundant.

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

Uniform maximizes entropy khi hỗ trợ (support / 지원) kích thước (size / 크기) cố định.

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

Bất định (uncertainty / 불확실성) lớn nhất khi nhị phân (binary / 이진) kết quả (outcome / 결과) khó đoán nhất.

## 6. Entropy khác variance

Variance đo squared numeric spread. Entropy đo bất định (uncertainty / 불확실성) của xác suất (probability / 확률) phân phối (distribution / 분포).

Label values `0` và `1000` có thể thay variance mạnh nhưng nếu probabilities unchanged, Shannon entropy của discrete labels không đổi.

Hai measures trả lời questions khác nhau.

## 7. nguồn (source / 소스) coding: frequent symbols nên có mã (code / 코드) ngắn

Nếu symbols có different frequencies, fixed-length mã (code / 코드) có thể lãng phí.

Lossless coding exploit predictability:

```text
common symbol → short code
rare symbol → long code
```

Average length có lower bound liên hệ entropy.

## 8. Prefix mã (code / 코드) và unique decodability

Prefix mã (code / 코드) không có codeword nào là prefix của codeword khác.

Ví dụ:

```text
A → 0
B → 10
C → 110
D → 111
```

Chuỗi (sequence / 시퀀스) decode unambiguously left-to-right.

Prefix cấu trúc (structure / 구조) tương ứng leaves trong nhị phân (binary / 이진) cây (tree / 트리).

## 9. Kraft inequality

Nếu nhị phân (binary / 이진) prefix mã (code / 코드) lengths là `l_i`, cần:

```math
\sum_i2^{-l_i}\le1.
```

Interpretation: codeword length `l` chiếm fraction `2^{-l}` của binary-tree sức chứa (capacity / 용량).

Kraft inequality nối combinatorics của cây (tree / 트리) với coding feasibility.

## 10. Shannon nguồn (source / 소스) coding theorem intuition

Với long iid nguồn (source / 소스) blocks và suitable coding, average lossless bits/symbol có thể tiến gần entropy nhưng không systematically thấp hơn entropy mà vẫn decode losslessly trong asymptotic mô hình (model / 모델).

Entropy là information-theoretic limit, không phải guaranteed chính xác (exact / 정확한) compressed kích thước (size / 크기) cho every finite tệp (file / 파일).

Headers, khối (block / 블록) length, mô hình (model / 모델) mismatch và hiện thực (implementation / 구현) overhead matter.

## 11. Huffman coding

Huffman repeatedly merges least probable symbols/subtrees để xây optimal prefix mã (code / 코드) về expected length among nhị phân (binary / 이진) prefix codes under tiêu chuẩn (standard / 표준) các giả định (assumptions / 가정들).

Mã (code / 코드) lengths roughly nhánh học (track / 트랙):

```math
l_i\approx-\log_2p_i.
```

Nhưng integer lengths khiến Huffman không luôn đạt chính xác (exact / 정확한) entropy.

## 12. Arithmetic coding

Arithmetic coding encode whole chuỗi (sequence / 시퀀스) thành subinterval of `[0,1)` dựa trên cumulative probabilities.

Nó không cần assign integer number bits independently cho each symbol, nên có thể approach entropy closer for suitable các mô hình (models / 모델들).

Compression chất lượng (quality / 품질) phụ thuộc xác suất (probability / 확률) mô hình (model / 모델) accuracy.

## 13. Joint entropy

Joint entropy đo bất định của cặp biến cùng lúc, làm nền để tách phần bất định riêng và phần phụ thuộc. Đây là bước trước khi định nghĩa conditional entropy và mutual information.

```math
H(X,Y)
```

measures bất định (uncertainty / 불확실성) của pair.

Chuỗi (chain / 사슬) quy tắc (rule / 규칙):

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

Conditional entropy hỏi còn bao nhiêu bất định của X sau khi đã biết Y. Nó biến ý tưởng “thông tin làm giảm bất định” thành đại lượng có thể tính.

```math
H(Y|X)
```

là average bất định (uncertainty / 불확실성) còn lại về `Y` sau khi observe `X`.

If `Y` deterministic hàm (function / 함수) of `X`:

```math
H(Y|X)=0.
```

If independent:

```math
H(Y|X)=H(Y).
```

## 15. Mutual thông tin (information / 정보)

Mutual information đo lượng bất định về một biến được giảm khi quan sát biến kia. Nó bằng 0 khi độc lập trong điều kiện phù hợp và không yêu cầu quan hệ tuyến tính.

```math
I(X;Y)
=H(X)-H(X|Y).
```

Equivalent:

```math
I(X;Y)=H(X)+H(Y)-H(X,Y).
```

Nó đo reduction in bất định (uncertainty / 불확실성) about one variable gained from the other.

Mutual thông tin (information / 정보) symmetric:

```math
I(X;Y)=I(Y;X).
```

## 16. Mutual thông tin (information / 정보) detect dependence beyond correlation

Correlation đo mainly tuyến tính (linear / 선형) quan hệ (relation / 관계).

Mutual thông tin (information / 정보) bằng 0 iff variables independent under tiêu chuẩn (standard / 표준) discrete/continuous definitions with appropriate regularity.

Do đó MI detect nonlinear dependence too.

Nhưng estimating MI từ finite high-dimensional dữ liệu (data / 데이터) có thể khó và biased.

## 17. KL divergence

KL divergence đo chi phí khi dùng phân phối Q để mã hóa dữ liệu sinh từ P. Nó không đối xứng, nên phải giữ rõ hướng so sánh và không gọi nó là khoảng cách metric thông thường.

```math
D_{KL}(p\|q)
=
\sum_x p(x)\log\frac{p(x)}{q(x)}.
```

Interpretation: extra expected log-loss/mã (code / 코드) chi phí (cost / 비용) khi dữ liệu (data / 데이터) thực theo `p` nhưng ta mô hình (model / 모델) bằng `q`.

Properties:

```text
D_KL ≥ 0
D_KL(p||q)=0 iff p=q almost everywhere
not symmetric
not triangle inequality
```

Do đó KL không phải chỉ số (metric / 지표) distance.

## 18. Cross-entropy

Cross-entropy là loss phổ biến khi phân phối thật gặp dự đoán xác suất. Tách phần entropy cố định khỏi KL giúp hiểu vì sao tối ưu cross-entropy hướng tới phân phối đúng.

```math
H(p,q)
=-\sum_xp(x)\log q(x).
```

Relationship:

```math
H(p,q)=H(p)+D_{KL}(p\|q).
```

Nếu `p` fixed, minimizing cross-entropy over mô hình (model / 모델) `q` equivalent to minimizing KL from `p` to `q`.

## 19. Cross-entropy mất mát (loss / 손실) trong classification

One-hot mục tiêu (target / 대상) lớp (class / 클래스) `y`, predicted probabilities `q_k`:

```math
L=-\log q_y.
```

Mô hình (model / 모델) bị penalty mạnh khi assign low xác suất (probability / 확률) cho true label.

Mất mát (loss / 손실) này đến từ negative log-likelihood của categorical mô hình (model / 모델), không phải arbitrary deep-learning convention.

## 20. Log-likelihood và coding

Dataset iid:

```math
-\log p(D|\theta)
=
-\sum_i\log p(x_i|\theta).
```

Minimize negative log-likelihood tương đương tìm mô hình (model / 모델) cho shortest ideal mã (code / 코드) length under coding interpretation.

Đây là cầu nối (bridge / 브리지) sâu giữa statistics và thông tin (information / 정보) lý thuyết (theory / 이론).

## 21. dữ liệu (data / 데이터) processing inequality

Nếu Markov chuỗi (chain / 사슬):

```text
X → Y → Z
```

thì processing `Y` thành `Z` không thể tạo thêm thông tin (information / 정보) về `X`:

```math
I(X;Z)\le I(X;Y).
```

Interpretation: deterministic/noisy post-processing cannot magically recover thông tin (information / 정보) already lost.

Liên kết (connection / 연결) mạnh với biểu diễn (representation / 표현) học tập (learning / 학습) và sufficient statistics.

## 22. Entropy tỷ lệ (rate / 비율)

For sequential/stochastic tiến trình (process / 프로세스), per-symbol bất định (uncertainty / 불확실성) may differ from marginal entropy because symbols dependent.

Entropy tỷ lệ (rate / 비율) roughly measures new thông tin (information / 정보) per step after accounting for lịch sử (history / 이력).

Compression gains from exploiting temporal/ngữ cảnh (context / 맥락) dependence.

## 23. Redundancy và compression

If nguồn (source / 소스) predictable, entropy thấp hơn raw fixed-width biểu diễn (representation / 표현).

Natural ngôn ngữ (language / 언어), logs, images và mã nguồn (source code / 소스 코드) có redundancy. Compression các mô hình (models / 모델들) exploit regularities.

No compressor can losslessly shorten every possible đầu vào (input / 입력): pigeonhole principle forbids ánh xạ (mapping / 매핑) all `n`-bit strings injectively into fewer than `n` bits.

## 24. Channel mô hình (model / 모델)

Communication channel maps đầu vào (input / 입력) `X` to đầu ra (output / 출력) `Y` probabilistically.

Noise means receiver observes uncertain phiên bản (version / 버전).

A mã (code / 코드) adds structured redundancy so messages remain distinguishable despite channel errors.

## 25. Channel sức chứa (capacity / 용량)

Sức chứa (capacity / 용량):

```math
C=\max_{p(x)} I(X;Y)
```

for memoryless channel under tiêu chuẩn (standard / 표준) setup.

It is maximum reliable thông tin (information / 정보) tỷ lệ (rate / 비율) supported by channel mô hình (model / 모델).

Shannon coding theorem says rates below sức chứa (capacity / 용량) can be made arbitrarily reliable with sufficiently long codes in asymptotic setting; above sức chứa (capacity / 용량) reliable communication is impossible.

## 26. nhị phân (binary / 이진) symmetric channel intuition

Bit flips with xác suất (probability / 확률) `p`.

Sức chứa (capacity / 용량):

```math
C=1-H_2(p)
```

bits/use, where `H_2` is nhị phân (binary / 이진) entropy.

If `p=0`, sức chứa (capacity / 용량) 1 bit/use.
If `p=0.5`, đầu ra (output / 출력) independent of đầu vào (input / 입력) and sức chứa (capacity / 용량) 0.

## 27. Hamming distance

For nhị phân (binary / 이진) strings, Hamming distance = number positions different.

Mã (code / 코드) with minimum distance `d_min` can:

```text
detect up to d_min-1 adversarial bit errors
correct up to floor((d_min-1)/2)
```

because correction regions around codewords must not overlap.

This is discrete hình học (geometry / 기하학) in Hamming không gian (space / 공간).

## 28. Repetition mã (code / 코드) example

Encode:

```text
0 → 000
1 → 111
```

Minimum distance 3, so can correct one bit flip by majority vote.

Tỷ lệ (rate / 비율) only `1/3`; độ tin cậy (reliability / 신뢰성) purchased bằng redundancy.

Coding lý thuyết (theory / 이론) studies better trade-offs among tỷ lệ (rate / 비율), distance, độ phức tạp (complexity / 복잡도).

## 29. tuyến tính (linear / 선형) codes

A nhị phân (binary / 이진) tuyến tính (linear / 선형) mã (code / 코드) is subspace of `GF(2)^n`.

Generator ma trận (matrix / 행렬) maps message bits to codeword.
Parity-check ma trận (matrix / 행렬) detects whether received word satisfies mã (code / 코드) các ràng buộc (constraints / 제약조건들).

This connects Boolean/XOR algebra, finite fields và tuyến tính (linear / 선형) algebra.

## 30. Entropy và thermodynamics: caution

Thông tin (information / 정보) entropy has mathematical resemblance to statistical-mechanics entropy, but units/interpretation/ngữ cảnh (context / 맥락) differ.

There are deep connections, yet one should not casually equate “high Shannon entropy” with thermodynamic disorder without mô hình (model / 모델) details.

## 31. Mutual thông tin (information / 정보) trong tính năng (feature / 기능) selection

A tính năng (feature / 기능) `X` with high `I(X;Y)` contains predictive thông tin (information / 정보) about mục tiêu (target / 대상) `Y`.

But pairwise MI alone does not solve redundancy/synergy among multiple features.

Tính năng (feature / 기능) selection needs joint cấu trúc (structure / 구조) and finite-sample estimation caution.

## 32. thông tin (information / 정보) bottleneck intuition

Biểu diễn (representation / 표현) `Z` may seek:

```text
retain information relevant to Y
compress information about raw X
```

This creates sự đánh đổi (trade-off / 트레이드오프) involving `I(Z;Y)` and `I(Z;X)`.

It offers an information-theoretic lens on biểu diễn (representation / 표현) học tập (learning / 학습), though practical neural huấn luyện (training / 학습) is more nuanced than the ideal formalism.

## 33. Perplexity liên kết (connection / 연결)

For ngôn ngữ (language / 언어) modeling, average cross-entropy in bits/đơn vị từ (token / 토큰) `H` gives perplexity:

```math
\operatorname{PPL}=2^H.
```

Perplexity can be interpreted as effective branching bất định (uncertainty / 불확실성) under mô hình (model / 모델)/log cơ sở (base / 기반) conventions.

Comparisons require same tokenization/dữ liệu (data / 데이터) giao thức (protocol / 프로토콜).

## 34. Worked example: biased coin entropy

If `p=0.9`:

```math
H_2(0.9)
=-0.9\log_2 0.9-0.1\log_2 0.1
\approx0.469\text{ bits}.
```

Even though one raw observation stored naively may use one bit, average bất định (uncertainty / 불확실성) is <1 bit because outcomes highly predictable.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Phần kết nối đưa entropy và coding sang machine learning, compression, privacy và decision theory. Hãy theo dõi xem “thông tin” đang được đo, truyền hay mất ở tầng nào.

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

Combinatorics supplies counting limits. xác suất (probability / 확률) supplies nguồn (source / 소스)/channel các mô hình (models / 모델들). tuyến tính (linear / 선형) algebra over finite fields supplies error-correcting codes. AI uses cross-entropy, KL and mutual-information concepts throughout probabilistic modeling.

## Mô hình tư duy (mental model / 사고 모델)

> thông tin (information / 정보) lý thuyết (theory / 이론) treats xác suất (probability / 확률) as a tài nguyên (resource / 자원) accounting hệ thống (system / 시스템). Rare events chi phí (cost / 비용) more bits to describe; entropy is average description bất định (uncertainty / 불확실성); compression removes predictable redundancy; channel coding spends redundancy to preserve thông tin (information / 정보) through noise.

## Dùng chung (common / 공통) Misconceptions

Entropy cao không inherently good/bad. KL không symmetric và không phải chỉ số (metric / 지표). Cross-entropy is not an arbitrary mất mát (loss / 손실). Mutual thông tin (information / 정보) high does not imply causality. Compression cannot shorten every possible đầu vào (input / 입력) losslessly. Channel sức chứa (capacity / 용량) is an asymptotic limit under a specified channel mô hình (model / 모델), not guaranteed thông lượng (throughput / 처리량) of a real hiện thực (implementation / 구현).

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 graph theory](./00_graph_theory.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
