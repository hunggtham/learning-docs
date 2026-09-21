# Statistics cho Artificial Intelligence

Statistics (통계학 / thống kê) giải quyết một tension nằm ở trung tâm của Machine Learning: ta chỉ quan sát một **finite sample**, nhưng muốn model hoạt động tốt trên những data chưa từng thấy. Training set không phải world. Nó chỉ là một sample được thu thập theo một process cụ thể, trong một khoảng thời gian cụ thể, với measurement error, selection bias và missing information.

Vì vậy Statistics trong AI không chỉ là “mean, median, chart”. Nó cung cấp framework để hỏi: data đến từ đâu, estimate đáng tin đến mức nào, model có generalize không, metric chênh nhau có meaningful không, và khi deployment distribution thay đổi thì conclusion cũ còn valid không.

Xem trước: [Probability for AI](./02_probability_for_ai.md).

## Population, sample và data-generating process

**Population (모집단)** là tập hoặc process mà ta thực sự quan tâm. **Sample (표본)** là data quan sát được.

Trong ML, cách nhìn mạnh hơn là tưởng tượng có một unknown data-generating distribution:

\[
(X,Y)\sim P_{data}
\]

Ta chỉ thấy dataset:

\[
D=\{(x_i,y_i)\}_{i=1}^{n}
\]

Nếu samples thực sự independent và identically distributed (i.i.d.) từ `P_data`, nhiều statistical tools hoạt động cleanly. Nhưng production data thường vi phạm assumptions này: user events theo thời gian correlated, recommendation policy ảnh hưởng data được thu thập, fraudsters thích nghi với detector, hoặc logs chỉ chứa users đã vượt qua một filter trước đó.

Do đó trước mọi statistical inference phải hỏi: **sampling process là gì?**

## Descriptive statistics: mô tả data trước khi modeling

Mean:

\[
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
\]

là center theo arithmetic average, nhưng sensitive với outlier.

Median là quantile 50%, robust hơn với extreme values.

Sample variance:

\[
s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2
\]

đo spread. `n-1` thay vì `n` xuất hiện để tạo unbiased estimator của population variance dưới standard assumptions.

Quantiles giúp hiểu tails. Trong latency monitoring, p50, p95 và p99 thường informative hơn mean vì user experience có thể bị dominated bởi tail latency.

Descriptive statistics không kết luận causality hay future performance; nó chỉ mô tả observed sample.

## Estimator và estimate

Một **estimator (추정량)** là rule/function dùng sample để estimate unknown population quantity. Kết quả cụ thể từ dataset là **estimate (추정값)**.

Ví dụ sample mean `\bar X` là estimator của population mean `μ`.

Ta đánh giá estimator bằng nhiều properties:

**Bias**:

\[
Bias(\hat\theta)=\mathbb{E}[\hat\theta]-\theta
\]

**Variance**:

\[
Var(\hat\theta)
\]

**Mean Squared Error**:

\[
MSE(\hat\theta)=Bias(\hat\theta)^2+Var(\hat\theta)
\]

Trade-off bias–variance ở estimator level liên hệ trực tiếp tới bias–variance trong Machine Learning.

## Law of Large Numbers

Law of Large Numbers nói, dưới conditions phù hợp, sample average hội tụ về expected value khi sample size tăng.

Đây là lý do nhiều empirical estimates trở nên stable hơn với nhiều data.

Nhưng “nhiều data” không tự chữa sampling bias. Nếu sample selection sai, một tỷ records biased vẫn estimate sai population target rất chính xác.

> More data reduces random error; it does not automatically remove systematic bias.

## Central Limit Theorem

Central Limit Theorem (CLT / 중심극한정리) giải thích vì sao distribution của normalized sample mean thường tiến gần Gaussian khi sample size lớn dưới conditions phù hợp, dù individual observations không Gaussian.

Điều này tạo foundation cho standard errors và nhiều confidence intervals.

Tuy nhiên CLT không phải license để assume mọi distribution trong ML là Gaussian. Heavy tails, strong dependency hoặc small sample có thể làm approximation kém.

## Standard error

Standard deviation mô tả spread của observations. **Standard error** mô tả uncertainty của estimator.

Với sample mean và i.i.d. samples:

\[
SE(\bar X)=\frac{s}{\sqrt{n}}
\]

Nếu sample size tăng 4 lần, standard error giảm khoảng 2 lần, không phải 4 lần.

Trong model evaluation, metric trên 100 examples và metric trên 100,000 examples không nên được tin ngang nhau dù point estimate giống hệt.

## Confidence interval

Confidence interval cung cấp range được xây từ một procedure có coverage property.

Approximate 95% interval cho mean trong large-sample setting:

\[
\bar{x}\pm1.96\,SE
\]

Một misunderstanding phổ biến là nói “có 95% probability true mean nằm trong interval đã tính”. Trong classical frequentist interpretation, parameter cố định; procedure tạo intervals có 95% long-run coverage dưới assumptions.

Trong practical AI, điều quan trọng hơn wording philosophical là: report uncertainty thay vì chỉ report point estimate.

## Hypothesis testing

Hypothesis testing bắt đầu từ null hypothesis `H_0`, test statistic và sampling distribution dưới `H_0`.

**p-value** là probability quan sát data ít nhất extreme như hiện tại nếu `H_0` đúng, không phải probability `H_0` đúng.

Small p-value không đo effect size. Với dataset rất lớn, tiny effect có thể statistically significant nhưng practically irrelevant.

Trong A/B testing AI product, cần xem cả:

- effect size;
- confidence interval;
- sample size;
- multiple testing;
- business impact;
- guardrail metrics.

## Multiple comparisons

Nếu test 100 hypotheses với threshold 0.05, ngay cả khi tất cả null đều true, ta vẫn kỳ vọng một số false positives.

Các methods như Bonferroni hoặc False Discovery Rate control giải quyết vấn đề theo cách khác nhau.

Trong ML experimentation, hyperparameter search hoặc benchmark trên nhiều tasks có thể tạo **researcher degrees of freedom**: nếu chỉ report best run mà không account search, result trông stable hơn thực tế.

## Train, validation và test set là statistical separation

Training set dùng để fit parameters.

Validation set dùng để chọn hyperparameters, architecture, threshold hoặc model version.

Test set nên đại diện cho final unbiased-ish estimate sau model selection.

Nếu continuously nhìn test result rồi chỉnh model, test set đã trở thành validation set về mặt statistical function.

Đây là **test-set overfitting**.

Một clean workflow:

```text
training data
    ↓ fit parameters
candidate models
    ↓ choose using validation
selected model
    ↓ evaluate once/few times on held-out test
reported estimate
```

Trong production, temporal holdout thường tốt hơn random split khi future data là target thực.

## Data leakage

**Data leakage (데이터 누수)** xảy ra khi training process có access tới information không hợp lệ tại prediction time hoặc từ validation/test side.

Ví dụ churn prediction dùng feature “account closed date” để dự đoán customer sẽ churn. Model có accuracy cực cao nhưng feature chỉ tồn tại sau event cần predict.

Leakage có thể subtle:

- fit normalization trên toàn dataset trước split;
- duplicate user xuất hiện cả train và test;
- target-derived feature;
- future information trong time series;
- embeddings/preprocessing trained trên held-out labels.

Leakage làm statistical evaluation optimistic giả tạo.

## Empirical risk và expected risk

Ta muốn minimize expected risk:

\[
R(\theta)=\mathbb{E}_{(X,Y)\sim P_{data}}[L(f_\theta(X),Y)]
\]

Nhưng chỉ có empirical risk:

\[
\hat R(\theta)=\frac{1}{n}\sum_{i=1}^{n}L(f_\theta(x_i),y_i)
\]

Nếu model quá flexible, nó có thể giảm `\hat R` bằng cách fit idiosyncrasies của training set mà không giảm true risk. Đây là heart of overfitting.

## Generalization

**Generalization (일반화)** là khả năng performance trên unseen data từ target distribution.

Generalization không đơn giản là “test accuracy cao”. Nếu test distribution khác deployment distribution, test result không đại diện target.

Một model có thể generalize tốt within-distribution nhưng fail khi:

- geography đổi;
- season đổi;
- device mix đổi;
- policy thay đổi;
- user behavior thích nghi;
- input language/domain mới.

Do đó generalization luôn relative to một distribution family hoặc operating environment.

## Bias–variance trade-off

Trong regression với squared error, expected prediction error có thể conceptually decomposed thành:

\[
Error \approx Bias^2 + Variance + Irreducible\ Noise
\]

High bias: model assumptions quá restrictive, underfit pattern.

High variance: model sensitive với sample fluctuations, dễ overfit.

Modern Deep Learning phức tạp hơn textbook curve đơn giản; highly overparameterized models vẫn có thể generalize tốt nhờ optimization, regularization, data scale và implicit biases. Vì vậy bias–variance vẫn là useful mental model, không phải complete theory cho mọi neural network.

## Regularization như statistical preference

Regularization thêm preference ngoài pure training fit:

\[
J(\theta)=\hat R(\theta)+\lambda\Omega(\theta)
\]

L2 regularization preference smaller parameters. Data augmentation encode invariances. Early stopping giới hạn optimization trajectory. Dropout inject stochastic structure.

Từ statistical viewpoint, regularization giảm effective flexibility hoặc encode prior assumptions để improve generalization.

## Cross-validation

K-fold cross-validation chia data thành `K` folds, train trên `K-1` và evaluate fold còn lại, lặp lại.

Nó hữu ích khi dataset nhỏ và muốn dùng data hiệu quả hơn để estimate performance.

Nhưng standard random K-fold không phù hợp mọi task. Với time series, cần time-aware split. Với multiple rows per patient/user, cần group split để tránh entity leakage.

Split strategy phải mô phỏng deployment boundary.

## Bootstrap

Bootstrap sample `n` observations **with replacement** từ observed dataset, lặp nhiều lần để approximate sampling distribution của statistic.

Nó hữu ích để estimate uncertainty của metric khi analytic formula khó.

Ví dụ muốn confidence interval cho F1 hoặc difference giữa hai models, paired bootstrap trên cùng test examples thường informative.

Bootstrap cũng có assumptions; strongly dependent data cần block/bootstrap variants hoặc domain-specific treatment.

## Class imbalance và base rate

Nếu fraud rate 0.1%, classifier luôn predict “not fraud” có accuracy 99.9% nhưng vô dụng.

Metric phải phản ánh decision need.

Precision:

\[
Precision=\frac{TP}{TP+FP}
\]

Recall:

\[
Recall=\frac{TP}{TP+FN}
\]

False positive rate:

\[
FPR=\frac{FP}{FP+TN}
\]

Base rate ảnh hưởng precision mạnh. Một model có same sensitivity/specificity có thể có drastically different precision ở population với prevalence khác.

## Threshold là decision parameter, không phải model truth

Binary classifier có score/probability `p`. Threshold `0.5` không phải universal law.

Nếu cost false negative lớn hơn false positive, threshold có thể thấp hơn.

Expected cost:

\[
Risk(t)=C_{FP}P(FP\mid t)+C_{FN}P(FN\mid t)
\]

Threshold nên chọn theo operating objective, capacity và risk constraints.

Model evaluation phải nối metrics với decision economics.

## ROC và Precision–Recall

ROC curve plot TPR vs FPR qua thresholds. ROC-AUC đo ranking ability theo một probability interpretation.

Precision–Recall curve thường informative hơn với rare positive class vì precision phản ánh false positives relative to predicted positives.

Không có metric universal tốt nhất. Metric choice là statement về điều system coi trọng.

## Distribution shift

Training distribution:

\[
P_{train}(X,Y)
\]

Deployment distribution:

\[
P_{deploy}(X,Y)
\]

Nếu hai distributions khác, model assumptions bị thử thách.

Các patterns thường được phân biệt:

**Covariate shift:** `P(X)` đổi, conditional relationship có thể tương đối stable.

**Label/prior shift:** `P(Y)` đổi.

**Concept shift/drift:** `P(Y|X)` đổi.

Real systems có thể kết hợp nhiều loại shift, nên taxonomy chỉ là diagnostic model.

## Selection bias và feedback loops

Một recommender chỉ quan sát feedback cho items mà nó đã show. Data tương lai bị policy hiện tại tạo ra.

```mermaid
flowchart LR
    M[Current Model] --> R[Recommendations]
    R --> U[User Exposure]
    U --> F[Observed Feedback]
    F --> D[Training Data]
    D --> M
```

Nếu không account feedback loop, model có thể reinforce popularity hoặc hide alternatives mà nó chưa thử.

Đây là connection giữa Statistics, Causal Inference, Bandits và Recommender Systems.

## Correlation và causation

Nếu users dùng feature A thường retention cao, không có nghĩa forcing A sẽ tăng retention. Có thể engaged users tự chọn A.

Prediction hỏi:

> `Y` có thể được dự đoán từ `X` không?

Causal inference hỏi:

> Nếu chủ động thay đổi `X`, `Y` sẽ thay đổi thế nào?

Machine Learning rất mạnh cho prediction nhưng causal question cần assumptions, experiments hoặc causal identification strategy khác.

## A/B testing

Randomized controlled experiment gán units ngẫu nhiên vào treatment/control để break confounding on average.

Trong AI product, A/B testing có thể compare recommendation algorithm, ranking policy hoặc assistant behavior.

Nhưng cần chú ý interference: một user's treatment có thể ảnh hưởng người khác, ví dụ marketplace hoặc social network. Khi SUTVA-like assumptions fail, standard analysis có thể misleading.

## Offline evaluation và online evaluation

Offline test set giúp iterate nhanh và reproducibly. Online experiment đo actual product impact.

Hai thứ có thể disagree vì offline metric chỉ proxy for user/business outcome.

Ví dụ recommender tăng NDCG nhưng làm feed quá homogeneous, giảm long-term discovery. AI system evaluation cần metric hierarchy thay vì một score duy nhất.

## Statistical power

Power là probability detect effect khi effect thật sự tồn tại ở specified size.

Experiment thiếu power dễ tạo inconclusive result. Sample size planning cần expected variance, minimum detectable effect và significance/power targets.

Không nên “chạy tới khi p<0.05 rồi dừng” nếu stopping rule không accounted, vì optional stopping inflate false positive risk.

## Reproducibility và random seeds

Training Deep Learning có stochasticity từ initialization, data order, dropout, nondeterministic kernels.

Một single run có thể không đại diện method performance.

Khi feasible, report multiple runs, variation và experimental protocol. Seed giúp reproducibility nhưng không biến result thành universal truth.

## Mental Model

```text
Probability  → mô hình hóa uncertainty
Statistics   → học điều đáng tin về population từ finite sample
Training set → sample dùng để fit
Validation   → sample dùng để choose
Test         → sample dùng để estimate sau selection
Generalization → performance ngoài sample đã fit
Uncertainty  → mức ta chưa biết về metric/parameter/prediction
Shift        → deployment không còn giống sampling assumptions
```

## Common Misconceptions

### “Dataset càng lớn thì bias càng ít”

Larger `n` giảm sampling variance nhưng systematic selection bias có thể giữ nguyên hoặc mạnh hơn.

### “Test accuracy là performance thực tế”

Chỉ khi test distribution và evaluation protocol đại diện deployment target đủ tốt.

### “p < 0.05 nghĩa là effect quan trọng”

p-value không nói effect size hay business importance.

### “Cross-validation luôn tốt hơn một test split”

Không. Với time-dependent hoặc grouped data, naive CV có thể leak information. Split design phải mirror deployment.

## Knowledge Connection

Statistics là bridge giữa [Probability](./02_probability_for_ai.md) và Machine Learning. Sau này các chapter về generalization, model evaluation, calibration, dataset bias và drift sẽ reuse các ideas ở đây.

Khi nhìn một model score, đừng chỉ hỏi “bao nhiêu phần trăm?”. Hãy hỏi: trên population nào, sample được lấy thế nào, uncertainty của estimate bao nhiêu, selection đã xảy ra ở đâu, và deployment distribution có giống evaluation distribution không.