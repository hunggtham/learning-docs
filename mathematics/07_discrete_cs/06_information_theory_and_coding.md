# Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Self-information: sự kiện (event / 이벤트) hiếm mang nhiều surprise hơn** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Vì sao phải dùng logarithm?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối information theory với entropy, channel capacity và coding, để hiểu giới hạn truyền tin trước khi chọn mã hóa.

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

> **Chuyển mạch:** Trong **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **2. Vì sao phải dùng logarithm?** tiếp nhận điểm tựa từ **1. Self-information: sự kiện (event / 이벤트) hiếm mang nhiều surprise hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Bit nghĩa là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **3. Bit nghĩa là gì?** tiếp nhận điểm tựa từ **2. Vì sao phải dùng logarithm?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Entropy: expected surprise** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **4. Entropy: expected surprise** tiếp nhận điểm tựa từ **3. Bit nghĩa là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Bernoulli entropy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **5. Bernoulli entropy** tiếp nhận điểm tựa từ **4. Entropy: expected surprise** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Entropy khác variance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **6. Entropy khác variance** tiếp nhận điểm tựa từ **5. Bernoulli entropy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. nguồn (source / 소스) coding: frequent symbols nên có mã (code / 코드) ngắn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Entropy khác variance

Variance đo squared numeric spread. Entropy đo bất định (uncertainty / 불확실성) của xác suất (probability / 확률) phân phối (distribution / 분포).

Label values `0` và `1000` có thể thay variance mạnh nhưng nếu probabilities unchanged, Shannon entropy của discrete labels không đổi.

Hai measures trả lời questions khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **6. Entropy khác variance** nêu điều cần giải thích; **7. nguồn (source / 소스) coding: frequent symbols nên có mã (code / 코드) ngắn** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. Prefix mã (code / 코드) và unique decodability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. nguồn (source / 소스) coding: frequent symbols nên có mã (code / 코드) ngắn

Nếu symbols có different frequencies, fixed-length mã (code / 코드) có thể lãng phí.

Lossless coding exploit predictability:

```text
common symbol → short code
rare symbol → long code
```

Average length có lower bound liên hệ entropy.

> **Chuyển mạch:** Trong **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **7. nguồn (source / 소스) coding: frequent symbols nên có mã (code / 코드) ngắn** nêu điều cần giải thích; **8. Prefix mã (code / 코드) và unique decodability** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. Kraft inequality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **9. Kraft inequality** tiếp nhận điểm tựa từ **8. Prefix mã (code / 코드) và unique decodability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Shannon nguồn (source / 소스) coding theorem intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Kraft inequality

Nếu nhị phân (binary / 이진) prefix mã (code / 코드) lengths là `l_i`, cần:

```math
\sum_i2^{-l_i}\le1.
```

Interpretation: codeword length `l` chiếm fraction `2^{-l}` của binary-tree sức chứa (capacity / 용량).

Kraft inequality nối combinatorics của cây (tree / 트리) với coding feasibility.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **9. Kraft inequality** nêu điều cần giải thích; **10. Shannon nguồn (source / 소스) coding theorem intuition** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. Huffman coding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Shannon nguồn (source / 소스) coding theorem intuition

Với long iid nguồn (source / 소스) blocks và suitable coding, average lossless bits/symbol có thể tiến gần entropy nhưng không systematically thấp hơn entropy mà vẫn decode losslessly trong asymptotic mô hình (model / 모델).

Entropy là information-theoretic limit, không phải guaranteed chính xác (exact / 정확한) compressed kích thước (size / 크기) cho every finite tệp (file / 파일).

Headers, khối (block / 블록) length, mô hình (model / 모델) mismatch và hiện thực (implementation / 구현) overhead matter.

> **Chuyển mạch:** Trong **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **10. Shannon nguồn (source / 소스) coding theorem intuition** nêu điều cần giải thích; **11. Huffman coding** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. Arithmetic coding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Huffman coding

Huffman repeatedly merges least probable symbols/subtrees để xây optimal prefix mã (code / 코드) về expected length among nhị phân (binary / 이진) prefix codes under tiêu chuẩn (standard / 표준) các giả định (assumptions / 가정들).

Mã (code / 코드) lengths roughly nhánh học (track / 트랙):

```math
l_i\approx-\log_2p_i.
```

Nhưng integer lengths khiến Huffman không luôn đạt chính xác (exact / 정확한) entropy.

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **12. Arithmetic coding** tiếp nhận điểm tựa từ **11. Huffman coding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Joint entropy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Arithmetic coding

Arithmetic coding encode whole chuỗi (sequence / 시퀀스) thành subinterval of `[0,1)` dựa trên cumulative probabilities.

Nó không cần assign integer number bits independently cho each symbol, nên có thể approach entropy closer for suitable các mô hình (models / 모델들).

Compression chất lượng (quality / 품질) phụ thuộc xác suất (probability / 확률) mô hình (model / 모델) accuracy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **13. Joint entropy** tiếp nhận điểm tựa từ **12. Arithmetic coding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Conditional entropy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **14. Conditional entropy** tiếp nhận điểm tựa từ **13. Joint entropy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Mutual thông tin (information / 정보)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **15. Mutual thông tin (information / 정보)** tiếp nhận điểm tựa từ **14. Conditional entropy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Mutual thông tin (information / 정보) detect dependence beyond correlation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **16. Mutual thông tin (information / 정보) detect dependence beyond correlation** tiếp nhận điểm tựa từ **15. Mutual thông tin (information / 정보)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. KL divergence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Mutual thông tin (information / 정보) detect dependence beyond correlation

Correlation đo mainly tuyến tính (linear / 선형) quan hệ (relation / 관계).

Mutual thông tin (information / 정보) bằng 0 iff variables independent under tiêu chuẩn (standard / 표준) discrete/continuous definitions with appropriate regularity.

Do đó MI detect nonlinear dependence too.

Nhưng estimating MI từ finite high-dimensional dữ liệu (data / 데이터) có thể khó và biased.

> **Chuyển mạch:** Trong **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **17. KL divergence** tiếp nhận điểm tựa từ **16. Mutual thông tin (information / 정보) detect dependence beyond correlation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Cross-entropy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **18. Cross-entropy** tiếp nhận điểm tựa từ **17. KL divergence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Cross-entropy mất mát (loss / 손실) trong classification** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **19. Cross-entropy mất mát (loss / 손실) trong classification** tiếp nhận điểm tựa từ **18. Cross-entropy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Log-likelihood và coding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Cross-entropy mất mát (loss / 손실) trong classification

One-hot mục tiêu (target / 대상) lớp (class / 클래스) `y`, predicted probabilities `q_k`:

```math
L=-\log q_y.
```

Mô hình (model / 모델) bị penalty mạnh khi assign low xác suất (probability / 확률) cho true label.

Mất mát (loss / 손실) này đến từ negative log-likelihood của categorical mô hình (model / 모델), không phải arbitrary deep-learning convention.

> **Chuyển mạch:** Trong **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **20. Log-likelihood và coding** tiếp nhận điểm tựa từ **19. Cross-entropy mất mát (loss / 손실) trong classification** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. dữ liệu (data / 데이터) processing inequality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Log-likelihood và coding

Dataset iid:

```math
-\log p(D|\theta)
=
-\sum_i\log p(x_i|\theta).
```

Minimize negative log-likelihood tương đương tìm mô hình (model / 모델) cho shortest ideal mã (code / 코드) length under coding interpretation.

Đây là cầu nối (bridge / 브리지) sâu giữa statistics và thông tin (information / 정보) lý thuyết (theory / 이론).

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **20. Log-likelihood và coding** nêu điều cần giải thích; **21. dữ liệu (data / 데이터) processing inequality** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **22. Entropy tỷ lệ (rate / 비율)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **21. dữ liệu (data / 데이터) processing inequality** nêu điều cần giải thích; **22. Entropy tỷ lệ (rate / 비율)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **23. Redundancy và compression** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Entropy tỷ lệ (rate / 비율)

For sequential/stochastic tiến trình (process / 프로세스), per-symbol bất định (uncertainty / 불확실성) may differ from marginal entropy because symbols dependent.

Entropy tỷ lệ (rate / 비율) roughly measures new thông tin (information / 정보) per step after accounting for lịch sử (history / 이력).

Compression gains from exploiting temporal/ngữ cảnh (context / 맥락) dependence.

> **Chuyển mạch:** Trong **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **23. Redundancy và compression** tiếp nhận điểm tựa từ **22. Entropy tỷ lệ (rate / 비율)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Channel mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Redundancy và compression

If nguồn (source / 소스) predictable, entropy thấp hơn raw fixed-width biểu diễn (representation / 표현).

Natural ngôn ngữ (language / 언어), logs, images và mã nguồn (source code / 소스 코드) có redundancy. Compression các mô hình (models / 모델들) exploit regularities.

No compressor can losslessly shorten every possible đầu vào (input / 입력): pigeonhole principle forbids ánh xạ (mapping / 매핑) all `n`-bit strings injectively into fewer than `n` bits.

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **24. Channel mô hình (model / 모델)** tiếp nhận điểm tựa từ **23. Redundancy và compression** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Channel sức chứa (capacity / 용량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Channel mô hình (model / 모델)

Communication channel maps đầu vào (input / 입력) `X` to đầu ra (output / 출력) `Y` probabilistically.

Noise means receiver observes uncertain phiên bản (version / 버전).

A mã (code / 코드) adds structured redundancy so messages remain distinguishable despite channel errors.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **25. Channel sức chứa (capacity / 용량)** tiếp nhận điểm tựa từ **24. Channel mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. nhị phân (binary / 이진) symmetric channel intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Channel sức chứa (capacity / 용량)

Sức chứa (capacity / 용량):

```math
C=\max_{p(x)} I(X;Y)
```

for memoryless channel under tiêu chuẩn (standard / 표준) setup.

It is maximum reliable thông tin (information / 정보) tỷ lệ (rate / 비율) supported by channel mô hình (model / 모델).

Shannon coding theorem says rates below sức chứa (capacity / 용량) can be made arbitrarily reliable with sufficiently long codes in asymptotic setting; above sức chứa (capacity / 용량) reliable communication is impossible.

> **Chuyển mạch:** Trong **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **26. nhị phân (binary / 이진) symmetric channel intuition** tiếp nhận điểm tựa từ **25. Channel sức chứa (capacity / 용량)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Hamming distance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. nhị phân (binary / 이진) symmetric channel intuition

Bit flips with xác suất (probability / 확률) `p`.

Sức chứa (capacity / 용량):

```math
C=1-H_2(p)
```

bits/use, where `H_2` is nhị phân (binary / 이진) entropy.

If `p=0`, sức chứa (capacity / 용량) 1 bit/use.
If `p=0.5`, đầu ra (output / 출력) independent of đầu vào (input / 입력) and sức chứa (capacity / 용량) 0.

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **27. Hamming distance** tiếp nhận điểm tựa từ **26. nhị phân (binary / 이진) symmetric channel intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Repetition mã (code / 코드) example** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Hamming distance

For nhị phân (binary / 이진) strings, Hamming distance = number positions different.

Mã (code / 코드) with minimum distance `d_min` can:

```text
detect up to d_min-1 adversarial bit errors
correct up to floor((d_min-1)/2)
```

because correction regions around codewords must not overlap.

This is discrete hình học (geometry / 기하학) in Hamming không gian (space / 공간).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **27. Hamming distance** cho ta quy tắc; **28. Repetition mã (code / 코드) example** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **29. tuyến tính (linear / 선형) codes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Repetition mã (code / 코드) example

Encode:

```text
0 → 000
1 → 111
```

Minimum distance 3, so can correct one bit flip by majority vote.

Tỷ lệ (rate / 비율) only `1/3`; độ tin cậy (reliability / 신뢰성) purchased bằng redundancy.

Coding lý thuyết (theory / 이론) studies better trade-offs among tỷ lệ (rate / 비율), distance, độ phức tạp (complexity / 복잡도).

> **Chuyển mạch:** Trong **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **28. Repetition mã (code / 코드) example** cho ta quy tắc; **29. tuyến tính (linear / 선형) codes** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **30. Entropy và thermodynamics: caution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. tuyến tính (linear / 선형) codes

A nhị phân (binary / 이진) tuyến tính (linear / 선형) mã (code / 코드) is subspace of `GF(2)^n`.

Generator ma trận (matrix / 행렬) maps message bits to codeword.
Parity-check ma trận (matrix / 행렬) detects whether received word satisfies mã (code / 코드) các ràng buộc (constraints / 제약조건들).

This connects Boolean/XOR algebra, finite fields và tuyến tính (linear / 선형) algebra.

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **30. Entropy và thermodynamics: caution** tiếp nhận điểm tựa từ **29. tuyến tính (linear / 선형) codes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Mutual thông tin (information / 정보) trong tính năng (feature / 기능) selection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Entropy và thermodynamics: caution

Thông tin (information / 정보) entropy has mathematical resemblance to statistical-mechanics entropy, but units/interpretation/ngữ cảnh (context / 맥락) differ.

There are deep connections, yet one should not casually equate “high Shannon entropy” with thermodynamic disorder without mô hình (model / 모델) details.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **31. Mutual thông tin (information / 정보) trong tính năng (feature / 기능) selection** tiếp nhận điểm tựa từ **30. Entropy và thermodynamics: caution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. thông tin (information / 정보) bottleneck intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Mutual thông tin (information / 정보) trong tính năng (feature / 기능) selection

A tính năng (feature / 기능) `X` with high `I(X;Y)` contains predictive thông tin (information / 정보) about mục tiêu (target / 대상) `Y`.

But pairwise MI alone does not solve redundancy/synergy among multiple features.

Tính năng (feature / 기능) selection needs joint cấu trúc (structure / 구조) and finite-sample estimation caution.

> **Chuyển mạch:** Trong **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **32. thông tin (information / 정보) bottleneck intuition** tiếp nhận điểm tựa từ **31. Mutual thông tin (information / 정보) trong tính năng (feature / 기능) selection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Perplexity liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. thông tin (information / 정보) bottleneck intuition

Biểu diễn (representation / 표현) `Z` may seek:

```text
retain information relevant to Y
compress information about raw X
```

This creates sự đánh đổi (trade-off / 트레이드오프) involving `I(Z;Y)` and `I(Z;X)`.

It offers an information-theoretic lens on biểu diễn (representation / 표현) học tập (learning / 학습), though practical neural huấn luyện (training / 학습) is more nuanced than the ideal formalism.

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, sau nội dung của **32. thông tin (information / 정보) bottleneck intuition**, **33. Perplexity liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **34. Worked example: biased coin entropy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Perplexity liên kết (connection / 연결)

For ngôn ngữ (language / 언어) modeling, average cross-entropy in bits/đơn vị từ (token / 토큰) `H` gives perplexity:

```math
\operatorname{PPL}=2^H.
```

Perplexity can be interpreted as effective branching bất định (uncertainty / 불확실성) under mô hình (model / 모델)/log cơ sở (base / 기반) conventions.

Comparisons require same tokenization/dữ liệu (data / 데이터) giao thức (protocol / 프로토콜).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **33. Perplexity liên kết (connection / 연결)** cho ta quy tắc; **34. Worked example: biased coin entropy** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Worked example: biased coin entropy

If `p=0.9`:

```math
H_2(0.9)
=-0.9\log_2 0.9-0.1\log_2 0.1
\approx0.469\text{ bits}.
```

Even though one raw observation stored naively may use one bit, average bất định (uncertainty / 불확실성) is <1 bit because outcomes highly predictable.

> **Chuyển mạch:** Trong **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **34. Worked example: biased coin entropy** cho ta quy tắc; **Liên kết kiến thức (knowledge connection / 지식 연결)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> thông tin (information / 정보) lý thuyết (theory / 이론) treats xác suất (probability / 확률) as a tài nguyên (resource / 자원) accounting hệ thống (system / 시스템). Rare events chi phí (cost / 비용) more bits to describe; entropy is average description bất định (uncertainty / 불확실성); compression removes predictable redundancy; channel coding spends redundancy to preserve thông tin (information / 정보) through noise.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) lý thuyết (theory / 이론), entropy và coding: xác suất trở thành giới hạn của biểu diễn (representation / 표현)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

Entropy cao không inherently good/bad. KL không symmetric và không phải chỉ số (metric / 지표). Cross-entropy is not an arbitrary mất mát (loss / 손실). Mutual thông tin (information / 정보) high does not imply causality. Compression cannot shorten every possible đầu vào (input / 입력) losslessly. Channel sức chứa (capacity / 용량) is an asymptotic limit under a specified channel mô hình (model / 모델), not guaranteed thông lượng (throughput / 처리량) of a real hiện thực (implementation / 구현).

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
