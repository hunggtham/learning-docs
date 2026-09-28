# Machine học tập (learning / 학습) là gì?

> **Mạch đọc:** Đặt **Machine học tập (learning / 학습) là gì?** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Từ tường minh (explicit / 명시적) rules tới learned ánh xạ (mapping / 매핑)** sang **Một formal học tập (learning / 학습) bài toán (problem / 문제)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Machine học tập (learning / 학습)** nghiên cứu cách xây dựng các hệ thống (systems / 시스템들) cải thiện hiệu năng (performance / 성능) trên một tác vụ (task / 작업) bằng dữ liệu (data / 데이터) hoặc experience thay vì nhà phát triển (developer / 개발자) phải encode toàn bộ hành vi (behavior / 동작) bằng rules cố định.

Điểm cốt lõi không phải “máy tự học như con người”. Một ML hệ thống (system / 시스템) thường có một mô hình (model / 모델) family, parameters, mục tiêu (objective / 목표), dữ liệu (data / 데이터) và tối ưu hóa (optimization / 최적화) procedure. huấn luyện (training / 학습) thay đổi parameters để mô hình (model / 모델) fit statistical cấu trúc (structure / 구조) trong dữ liệu (data / 데이터); triển khai (deployment / 배포) dùng learned parameters để tạo prediction hoặc biểu diễn (representation / 표현) cho examples mới.

Machine học tập (learning / 학습) là một major approach bên trong Artificial Intelligence, không phải synonym của AI. tìm kiếm (search / 검색), lô-gic (logic / 논리), planning và ràng buộc (constraint / 제약조건) solving vẫn là AI dù không nhất thiết học parameters từ dữ liệu (data / 데이터).

Xem trước: [AI vs ML vs DL vs Generative AI](../00_foundations/05_ai_vs_ml_vs_dl_vs_generative_ai.md).

## Từ tường minh (explicit / 명시적) rules tới learned ánh xạ (mapping / 매핑)

Traditional programming thường có dạng:

```text
Rules + Input → Output
```

Supervised ML:

```text
Training Inputs + Desired Outputs
            ↓
        Learning Algorithm
            ↓
        Learned Model
            ↓
New Input → Prediction
```

Ví dụ spam filter. Viết quy tắc (rule / 규칙) `contains "free" → spam` rất brittle. Một classifier có thể học mẫu (pattern / 패턴) kết hợp từ sender, đơn vị từ (token / 토큰) phân phối (distribution / 분포), links, siêu dữ liệu (metadata / 메타데이터) và lịch sử (history / 이력).

Nhưng learned mô hình (model / 모델) vẫn là software. nhà phát triển (developer / 개발자) vẫn quyết định dữ liệu (data / 데이터) collection, mục tiêu (target / 대상), features/biểu diễn (representation / 표현), mô hình (model / 모델) lớp (class / 클래스), mục tiêu (objective / 목표), evaluation và triển khai (deployment / 배포) chính sách (policy / 정책).

## Một formal học tập (learning / 학습) bài toán (problem / 문제)

Supervised setting có dataset:

\[
D=\{(x_i,y_i)\}_{i=1}^{n}
\]

Mô hình (model / 모델):

\[
f_\theta:X\rightarrow Y
\]

Prediction:

\[
\hat y=f_\theta(x)
\]

Huấn luyện (training / 학습) tìm parameters:

\[
\theta^*=\arg\min_\theta \hat R(\theta)
\]

với empirical rủi ro (risk / 위험):

\[
\hat R(\theta)=\frac{1}{n}\sum_i L(f_\theta(x_i),y_i)
\]

Nhưng mục tiêu (objective / 목표) thật không phải memorize huấn luyện (training / 학습) set. Ta muốn low expected rủi ro (risk / 위험) trên future dữ liệu (data / 데이터):

\[
R(\theta)=\mathbb{E}_{(X,Y)\sim P_{mục tiêu (target / 대상)}}[L(f_\theta(X),Y)]
\]

Gap giữa empirical hiệu năng (performance / 성능) và future hiệu năng (performance / 성능) là heart of **generalization**.

## Tác vụ (task / 작업), Experience, hiệu năng (performance / 성능)

Một classical definition framing nói program learns from experience `E` with respect to tác vụ (task / 작업) `T` and hiệu năng (performance / 성능) measure `P` nếu hiệu năng (performance / 성능) tại T, measured by P, improves with E.

Framing này hữu ích vì buộc ta specify:

```text
Task       → model phải làm gì?
Experience → học từ data/interaction nào?
Performance→ đo tốt/xấu bằng gì?
```

Nếu ba thứ mơ hồ, “dùng ML” chưa phải bài toán (problem / 문제) definition.

## Supervised học tập (learning / 학습)

Dữ liệu (data / 데이터) có mục tiêu (target / 대상) labels.

Regression:

\[
y\in\mathbb{R}
\]

Ví dụ dự đoán price, demand, độ trễ (latency / 지연 시간).

Classification:

\[
y\in\{1,...,K\}
\]

Ví dụ fraud/not-fraud, document category.

Mô hình (model / 모델) learns quan hệ (relation / 관계) between đầu vào (input / 입력) and mục tiêu (target / 대상).

## Unsupervised học tập (learning / 학습)

Không có tường minh (explicit / 명시적) mục tiêu (target / 대상) label theo supervised sense.

Goals include:

- clustering;
- dimensionality reduction;
- density estimation;
- biểu diễn (representation / 표현) học tập (learning / 학습);
- anomaly cấu trúc (structure / 구조) discovery.

“Unsupervised” không nghĩa hệ thống (system / 시스템) không có mục tiêu (objective / 목표); thuật toán (algorithm / 알고리즘) vẫn optimize criterion such as reconstruction lỗi (error / 오류), likelihood or clustering mục tiêu (objective / 목표).

## Self-Supervised học tập (learning / 학습)

Labels được tạo từ dữ liệu (data / 데이터) itself.

Ngôn ngữ (language / 언어) modeling:

```text
context tokens → predict next token
```

Masked modeling:

```text
corrupted input → reconstruct missing content
```

Contrastive học tập (learning / 학습) creates positive/negative pairs from transformations or co-occurrence.

Self-supervision lets mô hình (model / 모델) learn from massive unlabeled raw dữ liệu (data / 데이터). hiện đại (modern / 현대적) foundation các mô hình (models / 모델들) rely heavily on this paradigm.

## Semi-Supervised học tập (learning / 학습)

Có ít labeled dữ liệu (data / 데이터) và nhiều unlabeled dữ liệu (data / 데이터).

Methods may use pseudo-labels, consistency regularization, generative các mô hình (models / 모델들) or biểu diễn (representation / 표현) pretraining.

Goal exploit unlabeled cấu trúc (structure / 구조) without trusting noisy pseudo-labels blindly.

## Reinforcement học tập (learning / 학습)

Tác nhân (agent / 에이전트) interacts with môi trường (environment / 환경) and receives reward, not direct correct label for each hành động (action / 동작).

```text
state → action → transition → reward
```

Challenge includes delayed reward, exploration and policy-dependent dữ liệu (data / 데이터).

RL is học tập (learning / 학습) paradigm distinct from tiêu chuẩn (standard / 표준) supervised học tập (learning / 학습) and will have dedicated folder later.

## Online học tập (learning / 학습)

Mô hình (model / 모델) updates continuously/sequentially as examples arrive.

Useful when phân phối (distribution / 분포) changes or dữ liệu (data / 데이터) stream large.

Need handle:

- concept drift;
- catastrophic adaptation;
- delayed labels;
- phản hồi (feedback / 피드백) loops.

Online học tập (learning / 학습) is not same as online suy luận (inference / 추론). mô hình (model / 모델) can serve requests online while huấn luyện (training / 학습) offline.

## Batch học tập (learning / 학습)

Train on fixed dataset snapshot, deploy mô hình (model / 모델), retrain periodically.

Operationally simpler and reproducible.

Many môi trường vận hành (production / 운영 환경) các hệ thống (systems / 시스템들) use batch retraining even if suy luận (inference / 추론) real-time.

## Instance-Based vs Model-Based học tập (learning / 학습)

**Instance-based** methods keep huấn luyện (training / 학습) examples and compare new đầu vào (input / 입력) to stored instances, e.g. k-NN.

**Model-based** methods fit parameters summarizing dữ liệu (data / 데이터), e.g. tuyến tính (linear / 선형) regression.

Sự đánh đổi (trade-off / 트레이드오프):

```text
store/compute at inference
vs
compress structure into parameters during training
```

## Parametric vs Non-Parametric

Parametric mô hình (model / 모델) has fixed-dimensional parameterization independent of dataset kích thước (size / 크기), e.g. tuyến tính (linear / 선형) regression.

Non-parametric methods can grow effective độ phức tạp (complexity / 복잡도) with dữ liệu (data / 데이터), e.g. k-NN, some kernel methods.

“Non-parametric” does not mean “has no parameters”. It means mô hình (model / 모델) độ phức tạp (complexity / 복잡도) is not fixed by a finite parameter véc-tơ (vector / 벡터) in the same way.

## Generative vs Discriminative

Discriminative mô hình (model / 모델) learns:

\[
P(Y\mid X)
\]

or direct quyết định (decision / 결정) ranh giới (boundary / 경계).

Generative mô hình (model / 모델) learns joint/dữ liệu (data / 데이터) phân phối (distribution / 분포):

\[
P(X,Y)
\]

or `P(X)`.

Generative modeling can mẫu (sample / 표본) dữ liệu (data / 데이터) and handle missing/latent cấu trúc (structure / 구조), but may solve a harder bài toán (problem / 문제) than classification needs.

Hiện đại (modern / 현대적) generative AI is broader than old “generative classifier” terminology.

## Biểu diễn (representation / 표현) is part of học tập (learning / 학습)

Raw world must become biểu diễn (representation / 표현).

Traditional ML:

```text
raw data → hand-engineered features → model
```

Deep học tập (learning / 학습):

```text
raw-ish data → learned representations → prediction
```

Tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링) has not disappeared; hệ thống (system / 시스템) still makes biểu diễn (representation / 표현) choices in tokenization, normalization, aggregation, siêu dữ liệu (metadata / 메타데이터) and kiến trúc (architecture / 아키텍처).

## Parameters và Hyperparameters

Parameters learned from dữ liệu huấn luyện (training data / 학습 데이터):

```text
weights, coefficients, tree split values...
```

Hyperparameters configured outside inner fitting:

```text
learning rate
regularization strength
tree depth
number of neighbors
architecture choices
```

Hyperparameters may be tuned using kiểm tra hợp lệ (validation / 검증) dữ liệu (data / 데이터). If repeatedly tune against kiểm thử (test / 테스트) set, kiểm thử (test / 테스트) becomes contaminated.

## Hypothesis không gian (space / 공간)

Mô hình (model / 모델) family defines set of functions thuật toán (algorithm / 알고리즘) can choose:

\[
\mathcal H=\{f_\theta:\theta\in\Theta\}
\]

Mô hình tuyến tính (linear model / 선형 모델) chooses from tuyến tính (linear / 선형)/affine quyết định (decision / 결정) surfaces. Deep mạng (network / 네트워크) defines much richer hàm (function / 함수) lớp (class / 클래스).

Học tập (learning / 학습) thuật toán (algorithm / 알고리즘) does not tìm kiếm (search / 검색) “all possible intelligence”; it searches within mô hình (model / 모델)/parameterization and tối ưu hóa (optimization / 최적화) biases.

## Inductive độ lệch (bias / 편향)

Finite dữ liệu (data / 데이터) can be explained by many hypotheses. To generalize, learner must prefer some solutions.

**Inductive độ lệch (bias / 편향)** includes:

- mô hình (model / 모델) kiến trúc (architecture / 아키텍처);
- regularization;
- tối ưu hóa (optimization / 최적화);
- dữ liệu (data / 데이터) augmentation;
- tính năng (feature / 기능) biểu diễn (representation / 표현);
- pretraining.

There is no học tập (learning / 학습) without các giả định (assumptions / 가정들). More detail: [Learning Problem and Inductive Bias](./01_learning_problem_and_inductive_bias.md).

## Generalization

Huấn luyện (training / 학습) hiệu năng (performance / 성능) can be perfect while future hiệu năng (performance / 성능) poor.

Overfitting occurs when mô hình (model / 모델) captures sample-specific noise/idiosyncrasies instead of reusable cấu trúc (structure / 구조).

Underfitting occurs when mô hình (model / 모델)/tối ưu hóa (optimization / 최적화) cannot capture relevant cấu trúc (structure / 구조).

Generalization depends on much more than parameter count: dữ liệu (data / 데이터) quy mô (scale / 규모)/diversity, inductive độ lệch (bias / 편향), tối ưu hóa (optimization / 최적화), regularization and phân phối (distribution / 분포) match all matter.

## Phân phối (distribution / 분포) matters

Huấn luyện (training / 학습) examples typically assumed sampled from phân phối (distribution / 분포) `P_train`. triển khai (deployment / 배포) mục tiêu (target / 대상) `P_deploy` may differ.

If:

\[
P_{train}\neq P_{deploy}
\]

evaluation can break.

Mô hình (model / 모델) “accuracy” is never universal; it is hiệu năng (performance / 성능) over a specified population/thời gian (time / 시간)/lĩnh vực (domain / 도메인).

## Dữ liệu (data / 데이터) is generated by các hệ thống (systems / 시스템들)

Dataset is not neutral snapshot of reality. It reflects collection chính sách (policy / 정책).

Examples:

- only approved loans have repayment labels;
- recommender only sees phản hồi (feedback / 피드백) on shown items;
- fraud labels depend investigation tiến trình (process / 프로세스);
- medical dữ liệu (data / 데이터) reflects who seeks care.

This creates selection độ lệch (bias / 편향) and phản hồi (feedback / 피드백) loops.

## Mất mát (loss / 손실) is not the real-world goal

Huấn luyện (training / 학습) needs tractable mathematical tín hiệu (signal / 신호) such as cross-entropy.

Nghiệp vụ (business / 비즈니스) goal may be:

```text
reduce fraud loss
while preserving customer experience
```

Mất mát (loss / 손실), chỉ số (metric / 지표) and quyết định (decision / 결정) chính sách (policy / 정책) must be connected carefully.

A classifier xác suất (probability / 확률) mô hình (model / 모델) may be good while chosen threshold makes sản phẩm (product / 제품) bad.

## Prediction vs quyết định (decision / 결정)

Mô hình (model / 모델) đầu ra (output / 출력):

\[
P(fraud\mid x)=0.72
\]

Quyết định (decision / 결정) tầng (layer / 계층) chooses:

```text
approve
manual review
block
```

based on costs, sức chứa (capacity / 용량) and chính sách (policy / 정책).

Do not encode all lô-gic nghiệp vụ (business logic / 비즈니스 로직) implicitly inside mô hình (model / 모델) if tường minh (explicit / 명시적) chính sách (policy / 정책) is clearer/auditable.

## Correlation vs Causation

ML predicts associations in observed dữ liệu (data / 데이터). A tính năng (feature / 기능) predictive of kết quả (outcome / 결과) does not mean intervening on tính năng (feature / 기능) changes kết quả (outcome / 결과).

If goal is quyết định (decision / 결정) chính sách (policy / 정책) that changes world, lập luận nhân quả (causal reasoning / 인과적 추론) may be needed.

Example users who contact hỗ trợ (support / 지원) may churn more; forcing users to contact hỗ trợ (support / 지원) does not imply churn increases.

## Leakage

Mô hình (model / 모델) may accidentally truy cập (access / 접근) future/mục tiêu (target / 대상) thông tin (information / 정보).

Then huấn luyện (training / 학습)/kiểm thử (test / 테스트) metrics look excellent but triển khai (deployment / 배포) fails.

Leakage is often more dangerous than choosing “wrong thuật toán (algorithm / 알고리즘)”.

See [Data, Features and Labels](./02_data_features_and_labels.md).

## Evaluation is part of mô hình (model / 모델) definition in practice

A hệ thống (system / 시스템) is not “good” without specified chỉ số (metric / 지표) and kiểm thử (test / 테스트) population.

For imbalanced fraud:

```text
99.9% accuracy
```

could mean trivial always-negative mô hình (model / 모델).

Precision, recall, PR-AUC, expected chi phí (cost / 비용) and calibration may matter more.

## Baseline

Before sophisticated mô hình (model / 모델), create simple baseline:

- majority lớp (class / 클래스);
- mean predictor;
- simple quy tắc (rule / 규칙);
- tuyến tính (linear / 선형)/logistic regression.

If complex hệ thống (system / 시스템) barely beats baseline, added độ phức tạp (complexity / 복잡도) may not justify operational chi phí (cost / 비용).

Baseline also catches chuỗi xử lý (pipeline / 파이프라인) bugs: if mô hình (model / 모델) worse than trivial baseline, inspect dữ liệu (data / 데이터) and mục tiêu (target / 대상) first.

## No Free Lunch intuition

No thuật toán (algorithm / 알고리즘) universally best for every possible data-generating tiến trình (process / 프로세스).

Thuật toán (algorithm / 알고리즘) succeeds because its biases match cấu trúc (structure / 구조) of actual tác vụ (task / 작업).

Thus mô hình (model / 모델) selection asks:

> What các giả định (assumptions / 가정들) about dữ liệu (data / 데이터) and quyết định (decision / 결정) ranh giới (boundary / 경계) are reasonable here?

not simply “which thuật toán (algorithm / 알고리즘) is strongest?”.

## ML as compression of experience

Huấn luyện (training / 학습) compresses statistical cấu trúc (structure / 구조) from dataset into parameters/representations.

But compression loses detail and encodes biases. A mô hình (model / 모델) does not store a perfect cơ sở dữ liệu (database / 데이터베이스) of huấn luyện (training / 학습) examples even if memorization can occur.

This mô hình tư duy (mental model / 사고 모델) helps distinguish parameterized kiến thức (knowledge / 지식) from retrieval databases.

## Mô hình (model / 모델) vòng đời (lifecycle / 생명주기)

Môi trường vận hành (production / 운영 환경) ML:

```text
problem definition
→ data collection
→ validation/splitting
→ feature/representation
→ train
→ evaluate
→ decision policy
→ deploy
→ monitor
→ collect feedback
→ retrain/revise
```

Huấn luyện (training / 학습) is one stage, not entire ML hệ thống (system / 시스템).

## When NOT to use ML

Prefer deterministic software when:

- rules are chính xác (exact / 정확한) and stable;
- đầu ra (output / 출력) must be provably correct;
- little/no representative dữ liệu (data / 데이터);
- simple threshold solves tác vụ (task / 작업);
- thất bại (failure / 실패) chi phí (cost / 비용) too high without xác minh (verification / 확인).

Example tax formula should be mã (code / 코드)/rules. ML may predict missing categories or detect anomalies around it, not replace chính xác (exact / 정확한) arithmetic.

## Mô hình tư duy (mental model / 사고 모델)

```text
Data       = observed experience
Model      = family of possible mappings
Parameters = learned state of model
Loss       = training signal
Optimizer  = mechanism adjusting parameters
Bias       = assumptions selecting among possible explanations
Generalization = useful behavior on unseen target data
Evaluation = evidence that system generalizes for intended use
```

## Dùng chung (common / 공통) Misconceptions

### “ML tự tìm quy luật nên không cần lĩnh vực (domain / 도메인) kiến thức (knowledge / 지식)”

Lĩnh vực (domain / 도메인) kiến thức (knowledge / 지식) affects mục tiêu (target / 대상) definition, sampling, features, các ràng buộc (constraints / 제약조건들) and evaluation. Bad bài toán (problem / 문제) formulation cannot be fixed by stronger mô hình (model / 모델) alone.

### “More huấn luyện (training / 학습) accuracy = better mô hình (model / 모델)”

Huấn luyện (training / 학습) fit can improve while generalization worsens.

### “Deep học tập (learning / 학습) thay thế classical ML”

Tabular/small-data/latency-constrained tasks often favor trees, tuyến tính (linear / 선형) các mô hình (models / 모델들) or hybrids.

### “Unsupervised học tập (learning / 학습) has no labels nên mô hình (model / 모델) tự hiểu dữ liệu (data / 데이터)”

Thuật toán (algorithm / 알고리즘) still has mục tiêu (objective / 목표)/inductive độ lệch (bias / 편향) defining what cấu trúc (structure / 구조) counts as useful.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Machine học tập (learning / 학습) is where [Statistics](../01_mathematical_foundations/03_statistics_for_ai.md), [Optimization](../01_mathematical_foundations/06_optimization.md) and biểu diễn (representation / 표현) meet. The next chapters will make the học tập (learning / 학습) bài toán (problem / 문제) precise before introducing specific algorithms.

Xem tiếp: [Learning Problem and Inductive Bias](./01_learning_problem_and_inductive_bias.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 learning problem and inductive bias](./01_learning_problem_and_inductive_bias.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
