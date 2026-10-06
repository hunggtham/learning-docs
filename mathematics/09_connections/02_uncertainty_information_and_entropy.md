# Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. xác suất (probability / 확률) không phải thông tin (information / 정보)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Vì sao logarithm xuất hiện?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối uncertainty với information và entropy, để đo không chắc chắn bằng cấu trúc xác suất thay vì cảm giác.

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

> **Nối mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **2. Vì sao logarithm xuất hiện?** nối từ **1. xác suất (probability / 확률) không phải thông tin (information / 정보)** sang **3. Entropy là expected surprise**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **3. Entropy là expected surprise** nối từ **2. Vì sao logarithm xuất hiện?** sang **4. Entropy khác variance**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **4. Entropy khác variance** nối từ **3. Entropy là expected surprise** sang **5. Compression: predictability thành shorter biểu diễn (representation / 표현)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Entropy khác variance

Variance:

```math
\operatorname{Var}(X)
```

phụ thuộc numerical values và quy mô (scale / 규모).

Entropy phụ thuộc probabilities.

Hai distributions có thể cùng entropy nhưng variance rất khác, hoặc ngược lại.

Không nên coi entropy là “một kiểu variance”.

> **Nối mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **5. Compression: predictability thành shorter biểu diễn (representation / 표현)** nối từ **4. Entropy khác variance** sang **6. Prefix codes và Kraft inequality**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **6. Prefix codes và Kraft inequality** nối từ **5. Compression: predictability thành shorter biểu diễn (representation / 표현)** sang **7. Joint entropy và chuỗi (chain / 사슬) quy tắc (rule / 규칙)**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **6. Prefix codes và Kraft inequality** đặt đầu vào cho **7. Joint entropy và chuỗi (chain / 사슬) quy tắc (rule / 규칙)**, rồi **8. Mutual thông tin (information / 정보): biết Y giảm bất định (uncertainty / 불확실성) về X bao nhiêu?** mở rộng hệ quả hoặc giới hạn liên quan.

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

> **Nối mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **7. Joint entropy và chuỗi (chain / 사슬) quy tắc (rule / 규칙)** đặt đầu vào cho **8. Mutual thông tin (information / 정보): biết Y giảm bất định (uncertainty / 불확실성) về X bao nhiêu?**, rồi **9. dữ liệu (data / 데이터) processing inequality** mở rộng hệ quả hoặc giới hạn liên quan.

## 8. Mutual thông tin (information / 정보): biết Y giảm bất định (uncertainty / 불확실성) về X bao nhiêu?

Mutual information đo lượng bất định về X được giảm khi quan sát Y. Nó không yêu cầu quan hệ tuyến tính, nhưng vẫn phụ thuộc cách mô hình hóa phân phối và dữ liệu.

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

> **Nối mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **8. Mutual thông tin (information / 정보): biết Y giảm bất định (uncertainty / 불확실성) về X bao nhiêu?** đặt vấn đề; **9. dữ liệu (data / 데이터) processing inequality** đối chiếu bằng chứng, rồi **10. Cross-entropy là expected log mất mát (loss / 손실)** mở rộng hệ quả hoặc giới hạn liên quan.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **9. dữ liệu (data / 데이터) processing inequality** đặt vấn đề; **10. Cross-entropy là expected log mất mát (loss / 손실)** đối chiếu bằng chứng, rồi **11. KL divergence là extra coding/log-loss chi phí (cost / 비용)** mở rộng hệ quả hoặc giới hạn liên quan.

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

> **Nối mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **11. KL divergence là extra coding/log-loss chi phí (cost / 비용)** nối từ **10. Cross-entropy là expected log mất mát (loss / 손실)** sang **12. Maximum likelihood và cross-entropy**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. KL divergence là extra coding/log-loss chi phí (cost / 비용)

KL divergence có thể đọc như chi phí thêm khi dùng Q thay cho P để mã hóa hoặc dự đoán. Hướng P‖Q rất quan trọng vì đổi hướng sẽ đổi ý nghĩa.

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

> **Nối mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **12. Maximum likelihood và cross-entropy** nối từ **11. KL divergence là extra coding/log-loss chi phí (cost / 비용)** sang **13. Entropy và calibration khác nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **13. Entropy và calibration khác nhau** nối từ **12. Maximum likelihood và cross-entropy** sang **14. Expected mất mát (loss / 손실): xác suất (probability / 확률) chưa đủ cho hành động (action / 동작)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Entropy và calibration khác nhau

Mô hình (model / 모델) có low-entropy prediction có thể rất confident.

Nhưng confidence cao không đảm bảo calibrated.

Calibration hỏi:

```text
among predictions around 0.8,
roughly 80% có đúng không?
```

Entropy đo bất định (uncertainty / 불확실성) của prediction phân phối (distribution / 분포); calibration đo alignment xác suất (probability / 확률) với empirical frequency.

> **Nối mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **14. Expected mất mát (loss / 손실): xác suất (probability / 확률) chưa đủ cho hành động (action / 동작)** nối từ **13. Entropy và calibration khác nhau** sang **15. Proper scoring rules**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **15. Proper scoring rules** nối từ **14. Expected mất mát (loss / 손실): xác suất (probability / 확률) chưa đủ cho hành động (action / 동작)** sang **16. thông tin (information / 정보) gain trong trees**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Proper scoring rules

Log mất mát (loss / 손실) và Brier score là examples of **proper scoring rules**: expected score incentivizes reporting true probabilities under suitable các giả định (assumptions / 가정들).

Điều này quan trọng vì classification accuracy alone không reward calibrated probabilistic forecasts.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **16. thông tin (information / 정보) gain trong trees** nối từ **15. Proper scoring rules** sang **17. Entropy tỷ lệ (rate / 비율) cho sequences**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. thông tin (information / 정보) gain trong trees

Decision-tree split có thể choose tính năng (feature / 기능) giảm entropy nhiều nhất.

Thông tin (information / 정보) gain:

```math
IG=H(Y)-H(Y|split).
```

Tức split hữu ích nếu biết branch làm label phân phối (distribution / 분포) predictable hơn.

Nhưng greedy cây (tree / 트리) splits không guarantee globally optimal cây (tree / 트리).

> **Nối mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **17. Entropy tỷ lệ (rate / 비율) cho sequences** nối từ **16. thông tin (information / 정보) gain trong trees** sang **18. Channel sức chứa (capacity / 용량)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Entropy tỷ lệ (rate / 비율) cho sequences

Nếu dữ liệu (data / 데이터) có temporal dependence, per-symbol entropy không đủ.

Entropy tỷ lệ (rate / 비율) roughly đo new bất định (uncertainty / 불확실성) per additional symbol khi conditioning on longer past.

Predictable chuỗi (sequence / 시퀀스) có entropy tỷ lệ (rate / 비율) thấp dù marginal symbol phân phối (distribution / 분포) có thể nhìn balanced.

Compression algorithms exploit repeated/conditional cấu trúc (structure / 구조), không chỉ one-symbol frequency.

> **Nối mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **18. Channel sức chứa (capacity / 용량)** nối từ **17. Entropy tỷ lệ (rate / 비율) cho sequences** sang **19. Redundancy có thể tăng độ tin cậy (reliability / 신뢰성)**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **19. Redundancy có thể tăng độ tin cậy (reliability / 신뢰성)** nối từ **18. Channel sức chứa (capacity / 용량)** sang **20. Entropy trong thermodynamics và ML**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Redundancy có thể tăng độ tin cậy (reliability / 신뢰성)

Compression remove redundancy để save bits.

Error-correcting coding add structured redundancy để survive noise.

Hai goals ngược hướng nhưng cùng information-theoretic khung phần mềm (framework / 프레임워크):

```text
source coding → represent efficiently
channel coding → transmit reliably
```

> **Nối mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **20. Entropy trong thermodynamics và ML** nối từ **19. Redundancy có thể tăng độ tin cậy (reliability / 신뢰성)** sang **21. Rare sự kiện (event / 이벤트) không đồng nghĩa important sự kiện (event / 이벤트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Entropy trong thermodynamics và ML

Thermodynamic entropy và Shannon entropy có deep mathematical connections, nhưng không nên translate informal statements trực tiếp giữa domains.

Trong ML, “maximize entropy” có chính xác (exact / 정확한) mục tiêu (objective / 목표) tùy ngữ cảnh (context / 맥락):

```text
maximum entropy modeling
entropy regularization in RL
uncertainty measures
```

Always check definition and phân phối (distribution / 분포).

> **Nối mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **21. Rare sự kiện (event / 이벤트) không đồng nghĩa important sự kiện (event / 이벤트)** nối từ **20. Entropy trong thermodynamics và ML** sang **22. dùng chung (common / 공통) thất bại (failure / 실패) modes**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **22. dùng chung (common / 공통) thất bại (failure / 실패) modes** nối từ **21. Rare sự kiện (event / 이벤트) không đồng nghĩa important sự kiện (event / 이벤트)** sang **Liên kết kiến thức (knowledge connection / 지식 연결)**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** nối từ **22. dùng chung (common / 공통) thất bại (failure / 실패) modes** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Phần kết nối nối entropy, mutual information và KL với machine learning, compression, privacy và decision theory. Hãy phân biệt đo thông tin với tối ưu loss trong từng context.

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

> **Nối mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — bất định (uncertainty / 불확실성), thông tin (information / 정보) và Entropy: từ xác suất (probability / 확률) đến quyết định (decision / 결정)**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Mô hình tư duy (mental model / 사고 모델)

> Probability mô tả uncertainty trước khi biết outcome. Information đo uncertainty giảm khi observation đến. Entropy là average uncertainty/surprise theo distribution. Nhưng action cần thêm loss/utility; information nhiều không đồng nghĩa consequence lớn.

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
