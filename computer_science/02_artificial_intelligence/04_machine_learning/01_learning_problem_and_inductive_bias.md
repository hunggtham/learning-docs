# Học tập (learning / 학습) bài toán (problem / 문제) và Inductive độ lệch (bias / 편향)

> **Mạch đọc:** Đặt **học tập (learning / 학습) bài toán (problem / 문제) và Inductive độ lệch (bias / 편향)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **From dữ liệu (data / 데이터) to hypothesis** sang **Why finite dữ liệu (data / 데이터) cannot determine everything**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Machine học tập (learning / 학습) chỉ có finite observations nhưng phải predict beyond observations. Đây là một logical gap: vô số functions có thể fit cùng finite huấn luyện (training / 학습) set nhưng hành vi (behavior / 동작) hoàn toàn khác ở unseen points. Vì vậy **học tập (learning / 학습) luôn cần inductive độ lệch (bias / 편향)** — các giả định (assumptions / 가정들) khiến thuật toán (algorithm / 알고리즘) ưu tiên một số hypotheses hơn số khác.

Inductive độ lệch (bias / 편향) không phải “độ lệch (bias / 편향) xấu” như unfairness. Nó là điều kiện cần để generalize. Câu hỏi đúng không phải “làm sao loại bỏ mọi độ lệch (bias / 편향)?” mà là “độ lệch (bias / 편향) nào phù hợp cấu trúc (structure / 구조) của bài toán (problem / 문제) và triển khai (deployment / 배포) môi trường (environment / 환경)?”.

## From dữ liệu (data / 데이터) to hypothesis

Dataset:

\[
D=\{(x_i,y_i)\}_{i=1}^{n}
\]

Hypothesis không gian (space / 공간):

\[
\mathcal H=\{f:X\to Y\}
\]

Học tập (learning / 학습) thuật toán (algorithm / 알고리즘) maps dataset thành hypothesis:

\[
A(D)=\hat f\in\mathcal H
\]

Nếu nhiều hypotheses đều zero huấn luyện (training / 학습) lỗi (error / 오류), thuật toán (algorithm / 알고리즘) vẫn phải chọn một.

Selection comes from kiến trúc (architecture / 아키텍처), mục tiêu (objective / 목표), regularization, tối ưu hóa (optimization / 최적화), initialization and dữ liệu (data / 데이터) biểu diễn (representation / 표현).

## Why finite dữ liệu (data / 데이터) cannot determine everything

Suppose huấn luyện (training / 학습) points:

```text
x: 1 2 3
 y: 2 4 6
```

Natural hypothesis:

\[
y=2x
\]

But infinitely many functions pass exactly through those three points and differ elsewhere.

For example polynomial with extra term that is zero at x=1,2,3:

\[
y=2x+c(x-1)(x-2)(x-3)
\]

Every `c` fits dữ liệu huấn luyện (training data / 학습 데이터) perfectly.

Choosing simple tuyến tính (linear / 선형) quan hệ (relation / 관계) is an inductive preference.

## Hypothesis không gian (space / 공간) as a structural prior

Tuyến tính (linear / 선형) regression:

\[
f(x)=w^Tx+b
\]

assumes mục tiêu (target / 대상) can be approximated by affine cấu trúc (structure / 구조) in chosen features.

Cây quyết định (decision tree / 의사결정 트리) assumes useful rules can be built from axis-aligned splits.

CNN assumes locality and translation-related cấu trúc (structure / 구조).

Transformer assumes chuỗi (sequence / 시퀀스) can be modeled through learned đơn vị từ (token / 토큰) interactions with dùng chung (shared / 공유) layers/attention.

Kiến trúc (architecture / 아키텍처) is not neutral bộ chứa (container / 컨테이너); it encodes what patterns are easy to represent/learn.

## Occam's Razor

A dùng chung (common / 공통) principle prefers simpler explanation among equally good fits.

But “simple” depends biểu diễn (representation / 표현).

A sinusoid is simple in Fourier biểu diễn (representation / 표현) but complex as high-degree polynomial; a convolution is simple under spatial locality.

Therefore Occam's Razor becomes meaningful only after defining description/mô hình (model / 모델) ngôn ngữ (language / 언어).

## Regularization as tường minh (explicit / 명시적) preference

Mục tiêu (objective / 목표):

\[
J(\theta)=\hat R(\theta)+\lambda\Omega(\theta)
\]

L2 penalty:

\[
\Omega(\theta)=\|\theta\|_2^2
\]

prefers smaller parameter magnitude.

L1:

\[
\Omega(\theta)=\|\theta\|_1
\]

encourages sparsity in many settings.

Regularization says multiple functions fit; prefer one satisfying extra structural preference.

## Implicit regularization

No tường minh (explicit / 명시적) penalty does not mean no regularization/độ lệch (bias / 편향).

Độ dốc (gradient / 기울기) descent trajectory, initialization, batch noise, early stopping and parameterization can favor certain solutions.

In overparameterized neural networks, optimizer often finds particular interpolating solutions rather than arbitrary zero-training-loss solution.

This implicit độ lệch (bias / 편향) is active research topic.

## Dữ liệu (data / 데이터) augmentation as invariance độ lệch (bias / 편향)

Suppose ảnh (image / 이미지) label should not thay đổi (change / 변경) under small translation/flip.

Huấn luyện (training / 학습) on transformed samples encodes:

\[
f(x)\approx f(T(x))
\]

for transformations `T` believed label-preserving.

Augmentation is lĩnh vực (domain / 도메인) giả định (assumption / 가정), not free improvement. Horizontal flip is fine for cats, but can be invalid for văn bản (text / 텍스트), traffic signs or medical laterality.

## Equivariance vs invariance

Bất biến (invariant / 불변식):

\[
f(Tx)=f(x)
\]

Đầu ra (output / 출력) unchanged.

Equivariant:

\[
f(Tx)=T'f(x)
\]

Đầu ra (output / 출력) transforms predictably.

Ảnh (image / 이미지) classification may desire translation invariance; segmentation requires đầu ra (output / 출력) mask shift with ảnh (image / 이미지), an equivariant relationship.

Kiến trúc (architecture / 아키텍처) can encode these biases.

## Prior kiến thức (knowledge / 지식) in Bayesian học tập (learning / 학습)

Bayesian prior:

\[
p(\theta)
\]

explicitly encodes preference before dữ liệu (data / 데이터).

Posterior:

\[
p(\theta\mid D)\propto p(D\mid\theta)p(\theta)
\]

Regularization often corresponds to MAP prior interpretation. L2 is related to Gaussian prior in dùng chung (common / 공통) formulations; L1 to Laplace prior.

This liên kết (connection / 연결) shows “độ lệch (bias / 편향)” can be written as xác suất (probability / 확률) or penalty.

## Empirical rủi ro (risk / 위험) Minimization

ERM chooses:

\[
\hat f=\arg\min_{f\in\mathcal H}
\frac{1}{n}\sum_i L(f(x_i),y_i)
\]

Huấn luyện (training / 학습) rủi ro (risk / 위험) is observable. Population rủi ro (risk / 위험) is not.

Generalization lý thuyết (theory / 이론) asks when low empirical rủi ro (risk / 위험) implies low expected rủi ro (risk / 위험).

Answer depends sức chứa (capacity / 용량), dữ liệu (data / 데이터) kích thước (size / 크기)/phân phối (distribution / 분포), regularization and algorithmic cấu trúc (structure / 구조).

## Structural rủi ro (risk / 위험) Minimization

Instead of one huge hypothesis lớp (class / 클래스), consider nested classes:

\[
\mathcal H_1\subset\mathcal H_2\subset\cdots
\]

Choose sự đánh đổi (trade-off / 트레이드오프) between empirical fit and độ phức tạp (complexity / 복잡도).

This formalizes idea:

```text
fit data enough
but avoid unnecessary capacity
```

Hiện đại (modern / 현대적) Deep học tập (learning / 학습) complicates simple sức chứa (capacity / 용량) story because huge các mô hình (models / 모델들) can generalize despite enough parameters to memorize.

## VC dimension intuition

VC dimension measures ability of hypothesis lớp (class / 클래스) to shatter sets of points in nhị phân (binary / 이진) classification.

Higher VC dimension means richer lớp (class / 클래스).

It supports bounds roughly relating:

```text
sample size
model capacity
generalization gap
```

But VC lý thuyết (theory / 이론) is often too loose to explain practical hành vi (behavior / 동작) of massive neural networks quantitatively. It remains important conceptual foundation.

## Độ lệch (bias / 편향)–variance

A mô hình (model / 모델) lớp (class / 클래스) too rigid may have high độ lệch (bias / 편향); predictions systematically miss cấu trúc (structure / 구조).

A highly flexible learner can have high variance; small dataset changes produce large mô hình (model / 모델) changes.

Classical decomposition under squared-error các giả định (assumptions / 가정들):

\[
ExpectedError=độ lệch (bias / 편향)^2+Variance+Noise
\]

This is a mô hình tư duy (mental model / 사고 모델), not universal full lý thuyết (theory / 이론).

See [Bias, Variance and Generalization](./14_bias_variance_and_generalization.md).

## Underfitting

Symptoms:

```text
training error high
validation error also high
```

Possible causes:

- features missing useful thông tin (information / 정보);
- mô hình (model / 모델) too restrictive;
- excessive regularization;
- tối ưu hóa (optimization / 최적화) not converged.

Adding dữ liệu (data / 데이터) alone often does not solve strong underfitting.

## Overfitting

Typical mẫu (pattern / 패턴):

```text
training error very low
validation error significantly worse
```

Possible causes:

- flexible mô hình (model / 모델) + insufficient dữ liệu (data / 데이터);
- leakage-like artifacts;
- repeated kiểm tra hợp lệ (validation / 검증) tuning;
- spurious correlations;
- weak regularization.

Overfitting is relative to mục tiêu (target / 대상) phân phối (distribution / 분포) and evaluation procedure.

## Memorization vs generalization

Các mô hình (models / 모델들) can memorize rare examples while also generalize elsewhere. These are not mutually exclusive nhị phân (binary / 이진) states.

Large neural networks can interpolate huấn luyện (training / 학습) set but learn useful representations due to dữ liệu (data / 데이터) quy mô (scale / 규모) and inductive biases.

So “parameter count > mẫu (sample / 표본) count ⇒ overfit” is not a reliable hiện đại (modern / 현대적) quy tắc (rule / 규칙).

## Interpolation and extrapolation

Interpolation predicts within region covered by huấn luyện (training / 학습) phân phối (distribution / 분포).

Extrapolation predicts outside observed phạm vi (range / 범위)/cấu trúc (structure / 구조).

Many ML các mô hình (models / 모델들) are much less reliable under extrapolation.

A mô hình (model / 모델) trained on incomes 0–100k may behave strangely at 10 million even if formula returns a number.

Confidence should not be inferred from mere ability to compute đầu ra (output / 출력).

## Spurious correlation

A tính năng (feature / 기능) may correlate with label in huấn luyện (training / 학습) môi trường (environment / 환경) but not causally/reliably.

Example ảnh (image / 이미지) classifier learns hospital watermark instead of disease mẫu (pattern / 패턴) because watermark correlates with labels.

Huấn luyện (training / 학습)/kiểm thử (test / 테스트) random split from same hospitals may not reveal bài toán (problem / 문제). External-site split might.

Inductive độ lệch (bias / 편향) includes các giả định (assumptions / 가정들) about which correlations will persist.

## Shortcut học tập (learning / 학습)

Neural các mô hình (models / 모델들) often exploit easiest predictive tín hiệu (signal / 신호) rather than intended concept.

If dataset allows background color to predict lớp (class / 클래스), mô hình (model / 모델) may ignore đối tượng (object / 객체) shape.

This is not mô hình (model / 모델) “cheating”; mục tiêu (objective / 목표) rewards prediction, not human-intended lập luận (reasoning / 추론).

Dataset/evaluation must remove or challenge shortcuts.

## Distributional các giả định (assumptions / 가정들)

Tiêu chuẩn (standard / 표준) supervised học tập (learning / 학습) often assumes train and kiểm thử (test / 테스트) are i.i.d. from same phân phối (distribution / 분포).

Reality:

\[
P_{train}(X,Y)\neq P_{deploy}(X,Y)
\]

Under shift, a độ lệch (bias / 편향) that worked historically may thất bại (fail / 실패).

Robustness requires designing kiểm tra hợp lệ (validation / 검증) splits and monitoring around plausible shifts.

## Lĩnh vực (domain / 도메인) shift and invariants

If environments vary, seek relationships stable across them.

Examples:

```text
hospital A vs B
country A vs B
winter vs summer
old device vs new device
```

Học tập (learning / 학습) bất biến (invariant / 불변식) causal-ish cấu trúc (structure / 구조) is harder than fitting pooled correlations. lĩnh vực (domain / 도메인) generalization methods attempt this, but guarantees require các giả định (assumptions / 가정들).

## Tính năng (feature / 기능) biểu diễn (representation / 표현) changes simplicity

A nonlinear bài toán (problem / 문제) in raw tính năng (feature / 기능) may become tuyến tính (linear / 선형) after transformation.

Example circular ranh giới (boundary / 경계) can be easier using radius:

\[
r^2=x_1^2+x_2^2
\]

Then threshold on `r` suffices.

Tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링) alters hypothesis độ phức tạp (complexity / 복잡도) needed downstream.

Deep học tập (learning / 학습) learns transformations automatically to make mục tiêu (target / 대상) easier for later layers.

## Kernel trick as representational độ lệch (bias / 편향)

Kernel methods implicitly map inputs to high-dimensional tính năng (feature / 기능) không gian (space / 공간):

\[
\phi(x)
\]

without computing coordinates explicitly, using:

\[
k(x,x')=\langle\phi(x),\phi(x')\rangle
\]

Choice of kernel encodes similarity độ lệch (bias / 편향).

RBF kernel assumes nearby points in tính năng (feature / 기능) không gian (space / 공간) should behave similarly.

## Locality độ lệch (bias / 편향)

k-NN assumes nearby examples likely share mục tiêu (target / 대상).

This only works if distance chỉ số (metric / 지표) aligns with ngữ nghĩa (semantic / 의미적) relevance.

In high dimensions/raw mixed-scale dữ liệu (data / 데이터), Euclidean distance may be meaningless.

Thus even “model-free” phương thức (method / 메서드) has strong inductive độ lệch (bias / 편향).

## Cây (tree / 트리) độ lệch (bias / 편향)

Quyết định (decision / 결정) trees partition tính năng (feature / 기능) không gian (space / 공간) using hierarchical threshold rules.

They naturally mô hình (model / 모델) interactions and nonlinearities but axis-aligned partitions can be inefficient for diagonal smooth boundaries.

Ensembles reduce instability while keeping tree-based độ lệch (bias / 편향) useful for tabular dữ liệu (data / 데이터).

## Pretraining as inductive prior

A pretrained mô hình (model / 모델) starts not from random ignorance but parameters shaped by massive prior dữ liệu (data / 데이터).

Fine-tuning with small tác vụ (task / 작업) dataset uses biểu diễn (representation / 표현) prior:

```text
general patterns from pretraining
+ task-specific evidence
```

This changes mẫu (sample / 표본) efficiency dramatically.

Foundation các mô hình (models / 모델들) can be viewed as learned priors/representations reused across tasks.

## Transfer học tập (learning / 학습) các giả định (assumptions / 가정들)

Transfer works when nguồn (source / 소스) pretraining cấu trúc (structure / 구조) useful for mục tiêu (target / 대상).

Negative transfer can occur when domains/tasks differ or inherited biases harmful.

“Pretrained is always better” is not guaranteed.

## Multi-task học tập (learning / 학습)

Dùng chung (shared / 공유) mô hình (model / 모델) learns several tasks:

\[
L=\sum_t\lambda_t L_t
\]

Dùng chung (shared / 공유) representations can regularize/help if tasks related. Conflicting gradients may hurt.

Tác vụ (task / 작업) relatedness is another inductive giả định (assumption / 가정).

## Human choices as hidden độ lệch (bias / 편향)

Độ lệch (bias / 편향) enters before thuật toán (algorithm / 알고리즘):

```text
what problem to automate?
who appears in dataset?
what label means "success"?
which metric optimized?
which errors tolerated?
```

Technical mô hình (model / 모델) độ lệch (bias / 편향) and xã hội (social / 사회적)/fairness độ lệch (bias / 편향) overlap but are not identical concepts.

## No Free Lunch

Averaged uniformly over all possible mục tiêu (target / 대상) functions, no learner dominates all others in classic No Free Lunch settings.

Practical meaning:

> học tập (learning / 학습) works because real-world tasks have cấu trúc (structure / 구조) and our các mô hình (models / 모델들) exploit các giả định (assumptions / 가정들) about that cấu trúc (structure / 구조).

Do not interpret as “all algorithms equal”. On actual domains, some inductive biases match far better.

## Choosing mô hình (model / 모델) family

Ask:

```text
How much data?
What data type?
Expected nonlinearity/interactions?
Need interpretability?
Latency/memory constraints?
Distribution shifts?
Hard monotonic/physical constraints?
```

Mô hình (model / 모델) selection should follow bài toán (problem / 문제) cấu trúc (structure / 구조), not popularity.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Finite data cannot uniquely determine future behavior.
Inductive bias chooses which explanation to prefer.

Architecture     → representational bias
Regularization   → parameter/function preference
Optimization     → solution-selection bias
Data augmentation→ invariance assumptions
Pretraining      → learned prior
Features         → change geometry/simplicity of task
```

## Dùng chung (common / 공통) Misconceptions

### “độ lệch (bias / 편향) là thứ phải loại bỏ”

Inductive độ lệch (bias / 편향) is necessary for generalization. Unfair societal độ lệch (bias / 편향) is a different but related concern.

### “More flexible mô hình (model / 모델) always better”

Flexibility helps fit but needs dữ liệu (data / 데이터)/độ lệch (bias / 편향)/evaluation to generalize.

### “A mô hình (model / 모델) that fits all dữ liệu huấn luyện (training data / 학습 데이터) learned the truth”

Many functions can interpolate same observations.

### “kiến trúc (architecture / 아키텍처) only affects compute”

Kiến trúc (architecture / 아키텍처) encodes strong các giả định (assumptions / 가정들) about locality, chuỗi (sequence / 시퀀스), invariance and composition.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Inductive độ lệch (bias / 편향) connects Statistics, tối ưu hóa (optimization / 최적화) and mô hình (model / 모델) kiến trúc (architecture / 아키텍처). Every thuật toán (algorithm / 알고리즘) chapter later should be read as: **what các giả định (assumptions / 가정들) does this phương thức (method / 메서드) encode, and when are those các giả định (assumptions / 가정들) useful or dangerous?**

Xem tiếp: [Data, Features and Labels](./02_data_features_and_labels.md).
