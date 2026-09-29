# Ensemble học tập (learning / 학습): nhiều mô hình (model / 모델) yếu thành một hệ thống mạnh hơn

> **Mạch đọc:** Đặt **Ensemble học tập (learning / 학습): nhiều mô hình (model / 모델) yếu thành một hệ thống mạnh hơn** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Vì sao averaging có thể giảm variance?** sang **Bagging**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Ensemble học tập (learning / 학습) bắt đầu từ một observation: một mô hình (model / 모델) đơn lẻ có thể mắc lỗi do noise, mẫu (sample / 표본) variation hoặc limitation của hàm (function / 함수) lớp (class / 클래스). Nếu kết hợp nhiều các mô hình (models / 모델들) có lỗi không hoàn toàn giống nhau, aggregate prediction có thể ổn định và chính xác hơn.

Hai family quan trọng nhất là **bagging** và **boosting**. Cả hai đều dùng nhiều learners, nhưng cơ chế (mechanism / 메커니즘) gần như đối lập: bagging huấn luyện tương đối độc lập rồi average để giảm variance; boosting xây learners tuần tự, mỗi learner tập trung sửa phần ensemble hiện tại làm chưa tốt.

## Vì sao averaging có thể giảm variance?

Giả sử các estimators có cùng variance `σ²` và pairwise correlation `ρ`. Variance của average `M` các mô hình (models / 모델들) xấp xỉ:

\[
Var(\bar f)\approx \rho\sigma^2+\frac{1-\rho}{M}\sigma^2
\]

Khi `M` tăng, phần independent noise giảm. Nhưng nếu các mô hình (models / 모델들) hoàn toàn correlated (`ρ≈1`), averaging gần như không giúp.

Insight cốt lõi:

> Ensemble cần cả **strength** và **diversity**.

## Bagging

**Bootstrap Aggregating (Bagging / 배깅)** tạo nhiều bootstrap datasets bằng sampling huấn luyện (training / 학습) examples với replacement. Mỗi mô hình (model / 모델) train trên mẫu (sample / 표본) khác nhau; predictions được average/vote.

Cây quyết định (decision tree / 의사결정 트리) đặc biệt phù hợp vì cây (tree / 트리) có high variance: thay dữ liệu (data / 데이터) một chút có thể thay cấu trúc (structure / 구조) mạnh. Averaging nhiều trees giúp ổn định.

## Random Forest

Random Forest thêm một nguồn (source / 소스) randomness nữa: tại mỗi split, cây (tree / 트리) chỉ xem một random subset features.

Điều này giảm correlation giữa trees. Nếu tất cả trees luôn dùng cùng dominant tính năng (feature / 기능) ở gốc (root / 루트), chúng sẽ rất giống nhau; random tính năng (feature / 기능) subsets tăng diversity.

Classification:

\[
\hat y=chế độ (mode / 모드)\{f_1(x),...,f_M(x)\}
\]

Regression:

\[
\hat y=\frac1M\sum_{m=1}^M f_m(x)
\]

Random Forest thường là strong baseline cho tabular dữ liệu (data / 데이터) vì ít preprocessing, robust với nonlinear tương tác (interaction / 상호작용) và không quá nhạy hyperparameter so với boosting.

## Out-of-Bag Evaluation

Mỗi bootstrap mẫu (sample / 표본) không chứa khoảng 36.8% unique huấn luyện (training / 학습) examples. Những points không được dùng train một cây (tree / 트리) gọi là **out-of-bag (OOB)** cho cây (tree / 트리) đó.

Ta có thể aggregate predictions chỉ từ trees mà mẫu (sample / 표본) đó là OOB để ước lượng generalization hiệu năng (performance / 성능) mà không cần separate kiểm tra hợp lệ (validation / 검증) cho một số use trường hợp (case / 사례).

OOB không thay thế mọi kiểm tra hợp lệ (validation / 검증) thiết kế (design / 설계), đặc biệt thời gian (time / 시간)/group leakage vẫn phải xử lý đúng.

## Boosting: sửa lỗi tuần tự

Boosting xây mô hình (model / 모델) dạng additive:

\[
F_M(x)=\sum_{m=1}^{M}\alpha_m h_m(x)
\]

Mỗi weak learner `h_m` được thêm để cải thiện mục tiêu (objective / 목표) của ensemble hiện tại.

### AdaBoost

AdaBoost tăng trọng số các samples bị classify sai để learner sau chú ý chúng hơn.

Conceptually:

```text
Model 1 → tìm lỗi
        ↓
Tăng trọng số examples khó
        ↓
Model 2 → tập trung hơn vào lỗi
        ↓
Weighted vote
```

### Độ dốc (gradient / 기울기) Boosting

Độ dốc (gradient / 기울기) Boosting có interpretation tổng quát hơn: ở mỗi step, train learner mới để approximate negative độ dốc (gradient / 기울기) của mất mát (loss / 손실) theo hiện tại (current / 현재) predictions.

Với squared-error regression, negative độ dốc (gradient / 기울기) chính là residual:

\[
r_i=y_i-F_{m-1}(x_i)
\]

Cây (tree / 트리) mới học residual, sau đó:

\[
F_m(x)=F_{m-1}(x)+\eta h_m(x)
\]

`η` là học tập (learning / 학습) tỷ lệ (rate / 비율)/shrinkage.

Tên “độ dốc (gradient / 기울기) Boosting” vì procedure thực hiện độ dốc (gradient / 기울기) descent trong **hàm (function / 함수) không gian (space / 공간)**, không trực tiếp chỉ parameter không gian (space / 공간) như neural mạng (network / 네트워크).

## XGBoost, LightGBM, CatBoost

Các hiện thực (implementation / 구현) hiện đại bổ sung regularization, efficient histogram splitting, parallelization, missing-value handling và categorical strategies.

- **XGBoost** nổi tiếng với regularized mục tiêu (objective / 목표) và kỹ thuật (engineering / 엔지니어링) hiệu quả.
- **LightGBM** dùng histogram/leaf-wise growth để quy mô (scale / 규모) tốt trên large tabular dữ liệu (data / 데이터).
- **CatBoost** có techniques mạnh cho categorical features và giảm mục tiêu (target / 대상) leakage trong mục tiêu (target / 대상) statistics.

Không nên học chúng chỉ như ba thư viện (library / 라이브러리) APIs. Chúng đều nằm trong gradient-boosted decision-tree family nhưng khác tối ưu hóa (optimization / 최적화)/hệ thống (system / 시스템) thiết kế (design / 설계).

## Học tập (learning / 학습) tỷ lệ (rate / 비율) và number of trees

Small học tập (learning / 학습) tỷ lệ (rate / 비율) thường cần nhiều trees hơn. Đây là sự đánh đổi (trade-off / 트레이드오프) giữa từng step cập nhật (update / 업데이트) nhỏ và ensemble độ sâu (depth / 깊이) theo iteration.

Quá nhiều boosting rounds có thể overfit, dù cây (tree / 트리) boosting thường overfit chậm hơn single deep cây (tree / 트리). Early stopping trên kiểm tra hợp lệ (validation / 검증) set là practice quan trọng.

## Bagging vs Boosting

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

| Aspect | Bagging | Boosting |
|---|---|---|
| Primary goal | giảm variance | giảm độ lệch (bias / 편향), tiếp tục sửa lỗi (error / 오류) |
| huấn luyện (training / 학습) | có thể parallel | chủ yếu sequential |
| Typical mô hình (model / 모델) | Random Forest | GBDT/XGBoost/LightGBM |
| Noise sensitivity | thường robust hơn | có thể nhạy hơn với mislabeled/outlier |
| cốt lõi (core / 핵심) cơ chế (mechanism / 메커니즘) | average diverse learners | additive corrective learners |

## Stacking

**Stacking** dùng predictions của cơ sở (base / 기반) các mô hình (models / 모델들) làm đầu vào (input / 입력) cho meta-model.

Ví dụ:

```text
Linear model ─┐
Tree model   ─┼→ out-of-fold predictions → Meta model
Neural model ─┘
```

Trọng yếu (critical / 중요): meta-model phải train trên **out-of-fold** predictions. Nếu dùng in-sample predictions, leakage xảy ra vì cơ sở (base / 기반) các mô hình (models / 모델들) đã thấy targets.

## Ensemble và bất định (uncertainty / 불확실성)

Disagreement giữa ensemble members đôi khi cung cấp tín hiệu (signal / 신호) về epistemic bất định (uncertainty / 불확실성). Deep ensembles dùng nhiều neural networks với initialization/dữ liệu (data / 데이터) thứ tự (order / 순서) khác nhau và thường cho bất định (uncertainty / 불확실성) estimate thực dụng tốt.

Nhưng disagreement không tự động là calibrated bất định (uncertainty / 불확실성), nhất là khi all các mô hình (models / 모델들) share same blind spots.

## Tabular ML và Deep học tập (learning / 학습)

Trên nhiều structured/tabular tasks với dataset vừa phải, độ dốc (gradient / 기울기) Boosted Trees vẫn rất competitive hoặc tốt hơn generic neural networks. Điều này cho thấy “mô hình (model / 모델) mới hơn” không đồng nghĩa “phù hợp hơn mọi dữ liệu (data / 데이터) modality”.

Inductive độ lệch (bias / 편향) của trees rất hợp threshold, heterogeneous quy mô (scale / 규모) và tính năng (feature / 기능) tương tác (interaction / 상호작용) trong tabular dữ liệu (data / 데이터).

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Bagging  = nhiều góc nhìn độc lập + average → ổn định hơn
Boosting = model sau sửa lỗi model trước → function mạnh dần
Stacking = model cấp trên học cách phối hợp các model cấp dưới
```

## Dùng chung (common / 공통) Misconceptions

### “Nhiều mô hình (model / 모델) luôn tốt hơn một mô hình (model / 모델)”

Nếu các mô hình (models / 모델들) correlated hoặc cùng độ lệch (bias / 편향), ensemble gain có thể nhỏ.

### “Random Forest chỉ là nhiều cây (tree / 트리) bình thường”

Random tính năng (feature / 기능) selection là thành phần (component / 컴포넌트) quan trọng để decorrelate trees.

### “độ dốc (gradient / 기울기) Boosting train từng cây (tree / 트리) trên mục tiêu (target / 대상) gốc”

Learners sau được fit để cải thiện hiện tại (current / 현재) mục tiêu (objective / 목표), thường qua residual/negative độ dốc (gradient / 기울기).

### “Stacking chỉ cần lấy prediction rồi train mô hình (model / 모델) mới”

Nếu không dùng out-of-fold thiết kế (design / 설계), leakage làm meta-model đánh giá giả.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Ensemble học tập (learning / 학습) là ứng dụng (application / 애플리케이션) trực tiếp của [Bias–Variance and Generalization](./14_bias_variance_and_generalization.md) và [Optimization](../01_mathematical_foundations/06_optimization.md).

Xem tiếp: [Support Vector Machines](./10_support_vector_machines.md) để chuyển sang một family có inductive bias hình học rất khác.
