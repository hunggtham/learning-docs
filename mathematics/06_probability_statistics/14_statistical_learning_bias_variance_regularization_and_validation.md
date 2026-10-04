# Statistical learning: generalization, bias–variance, regularization và validation

> **Mạch đọc:** Chapter này nối [Regression và correlation](./06_regression_and_correlation.md), [Likelihood / MLE / MAP](./10_likelihood_mle_map_and_model_selection.md), [Experimental design](./13_experimental_design_randomization_blocking_and_anova.md) và [Optimization](../08_optimization_numerical/00_optimization.md). Mục tiêu không phải học một catalog thuật toán ML, mà hiểu câu hỏi toán học trung tâm: **vì sao một model fit data đã thấy có thể hoặc không thể hoạt động tốt trên data chưa thấy?**

Trong statistics cổ điển, ta thường bắt đầu với một probabilistic model và hỏi parameter nào phù hợp với data. Trong **statistical learning / 통계적 학습**, ta thêm một vấn đề rất thực tế: model có thể đủ linh hoạt để fit cả signal lẫn noise.

Một model có training error gần bằng zero chưa chắc là model tốt. Nếu mục tiêu là prediction hoặc decision trên tương lai, object cần tối ưu không phải performance trên sample đã dùng để fit mà là **generalization performance** trên data mới từ cùng data-generating process.

## 1. Ba lớp phải tách riêng: reality, sample và model

Hãy phân biệt:

```text
unknown data-generating process
          ↓ generates
finite observed sample
          ↓ used to fit
chosen model / algorithm
```

Ta không quan sát trực tiếp distribution thật `P(X,Y)`. Ta chỉ có sample:

```math
D=\{(x_i,y_i)\}_{i=1}^n.
```

Một learning algorithm nhận `D` và trả model `\hat f_D`.

Do sample hữu hạn, model được fit trên sample này có thể khác model fit trên một sample khác từ cùng population. Đây là nguồn của **sampling variability** và là lý do generalization không thể được đánh giá chỉ bằng training fit.

## 2. Loss function: model sai theo nghĩa nào?

Để so predictions với outcomes, ta cần một **hàm mất mát (loss function / 손실함수)**.

Regression thường dùng squared loss:

```math
L(y,\hat y)=(y-\hat y)^2.
```

Classification có thể dùng 0–1 loss cho final decision hoặc log loss cho probabilistic predictions.

Loss không phải một chi tiết implementation. Nó encode loại error nào bị phạt và với mức độ nào.

Ví dụ squared loss phạt large errors mạnh hơn absolute loss. Trong finance hoặc safety-critical systems, asymmetric costs có thể khiến underprediction và overprediction không tương đương; khi đó một symmetric loss có thể không phản ánh business/physical objective.

## 3. Expected risk và empirical risk

Nếu biết distribution thật, ta muốn minimize **expected risk / 기대 위험**:

```math
R(f)=\mathbb E_{(X,Y)\sim P}[L(Y,f(X))].
```

Nhưng `P` unknown. Ta chỉ có empirical approximation:

```math
\hat R_n(f)=\frac{1}{n}\sum_{i=1}^{n}L(y_i,f(x_i)).
```

**Empirical Risk Minimization (ERM / 경험위험 최소화)** chọn model làm training loss nhỏ.

Vấn đề: nếu function class quá flexible, ta có thể làm `\hat R_n(f)` rất nhỏ bằng cách memorize sample mà không làm `R(f)` nhỏ.

Đây là mathematical core của overfitting:

```text
empirical fit improves
but population/generalization risk does not
```

## 4. Training error là optimistic estimate

Model được chọn **bởi chính training data**. Vì vậy training performance được đo trên data đã ảnh hưởng tới parameter/model selection.

Ngay cả khi labels chứa noise, sufficiently flexible model có thể adapt vào noise cụ thể của sample. Training error do đó biased downward như estimate của future error.

Đây là lý do cần data không tham gia fitting để estimate generalization.

## 5. Train, validation và test có vai trò khác nhau

Một split cơ bản:

```text
training set   → fit parameters
validation set → choose model / hyperparameters
test set       → final unbiased-ish evaluation
```

**Parameter / 매개변수** được fit trực tiếp từ training objective, ví dụ regression coefficients hoặc neural-network weights.

**Hyperparameter / 하이퍼파라미터** điều khiển learning procedure/model class, ví dụ regularization strength `\lambda`, tree depth hoặc number of basis functions.

Nếu nhìn test performance rồi chỉnh model, test set đã trở thành validation set. Repeated human iteration trên cùng benchmark cũng là một dạng information leakage.

## 6. Data leakage: model được phép biết điều gì tại prediction time?

**Data leakage / 데이터 누수** xảy ra khi training pipeline sử dụng information không thực sự available khi model được deployed hoặc sử dụng information từ validation/test theo cách làm evaluation optimistic.

Ví dụ:

- normalize toàn dataset trước khi split;
- impute missing values dùng statistics từ test set;
- feature chứa outcome future;
- chọn features bằng toàn data rồi mới cross-validation;
- time-series prediction dùng random split khiến future observations rơi vào training.

Nguyên tắc:

> Mọi transformation có học từ data phải được fit **bên trong training partition** tương ứng.

Pipeline đúng trong cross-validation là:

```text
fold training data
  → fit preprocessing
  → fit model
  → apply frozen preprocessing/model to fold validation data
```

## 7. Underfitting và overfitting

**Underfitting / 과소적합**: model class quá restricted hoặc optimization chưa đủ, nên cả training và validation errors cao.

**Overfitting / 과적합**: model adapts quá mạnh vào sample-specific noise; training error thấp nhưng validation/test error cao hơn đáng kể.

Một typical complexity curve:

```text
model complexity ↑
training error   ↓ monotonically-ish
validation error ↓ then ↑
```

Điểm tối ưu không phải necessarily model đơn giản nhất, mà là complexity level cho generalization tốt nhất với sample size/noise hiện có.

## 8. Bias–variance decomposition

Trong squared-error regression, giả sử

```math
Y=f(x)+\varepsilon,
\qquad
\mathbb E[\varepsilon]=0,
\qquad
\operatorname{Var}(\varepsilon)=\sigma^2.
```

Prediction `\hat f_D(x)` phụ thuộc random training dataset `D`.

Expected squared prediction error tại `x` có decomposition:

```math
\mathbb E_D[(Y-\hat f_D(x))^2]
=
\sigma^2
+
\operatorname{Bias}(\hat f(x))^2
+
\operatorname{Var}(\hat f_D(x)).
```

Trong đó

```math
\operatorname{Bias}(\hat f(x))
=
\mathbb E_D[\hat f_D(x)]-f(x).
```

**Bias** đo systematic misspecification trung bình qua hypothetical repeated datasets.

**Variance** đo model prediction thay đổi mạnh đến mức nào khi training sample thay đổi.

`\sigma^2` là irreducible noise theo model assumptions.

## 9. Vì sao flexibility thường giảm bias nhưng tăng variance?

Một rigid linear model không thể biểu diễn highly nonlinear truth: high bias, thường lower variance.

Một very flexible model có thể follow many shapes và giảm approximation bias, nhưng small changes trong sample có thể làm fitted shape thay đổi đáng kể: higher variance.

Trade-off không phải universal law theo mọi parameterization, nhưng là một mental model mạnh:

```text
more flexibility
  → more capacity to capture signal
  → more capacity to capture sample noise
```

Good learning procedure tìm cách giữ useful flexibility nhưng control unstable directions.

## 10. Regularization: thêm preference vào optimization

Thay vì minimize pure training loss:

```math
\min_\beta \sum_i (y_i-x_i^T\beta)^2,
```

**regularization / 정규화** thêm penalty:

```math
\min_\beta
\left[
\sum_i (y_i-x_i^T\beta)^2
+
\lambda\,\Omega(\beta)
\right].
```

`\lambda` điều khiển trade-off giữa fit và model complexity theo penalty chosen.

Regularization không chỉ “làm coefficients nhỏ”. Nó encode prior preference rằng trong nhiều nearly-equivalent fits, ta ưu tiên một class solutions có cấu trúc mong muốn.

## 11. Ridge / L2 regularization

Ridge dùng

```math
\Omega(\beta)=\|\beta\|_2^2=\sum_j\beta_j^2.
```

Objective:

```math
\min_\beta
\|y-X\beta\|_2^2+\lambda\|\beta\|_2^2.
```

Closed-form khi conditions phù hợp:

```math
\hat\beta_{ridge}
=(X^TX+\lambda I)^{-1}X^Ty.
```

So với ordinary least squares, term `\lambda I` stabilizes directions nơi `X^TX` gần singular. Vì vậy ridge liên kết trực tiếp với conditioning và numerical stability.

Ridge thường shrink correlated/weakly identified coefficients thay vì để chúng explode để fit small sample fluctuations.

## 12. Lasso / L1 regularization

Lasso dùng

```math
\Omega(\beta)=\|\beta\|_1=\sum_j|\beta_j|.
```

L1 penalty có geometry với “corners” trên coordinate axes. Khi loss contours chạm feasible/penalized region tại corner, một số coefficients trở thành exact zero.

Do đó lasso có thể đồng thời regularize và perform a form of feature selection.

Nhưng “coefficient zero” không nghĩa feature objectively irrelevant. Với correlated predictors, selected variable có thể unstable giữa samples.

## 13. Constraint view và penalty view

Penalty problem

```math
\min_\beta \text{Loss}(\beta)+\lambda\Omega(\beta)
```

liên hệ với constrained problem

```math
\min_\beta \text{Loss}(\beta)
\quad\text{s.t.}\quad
\Omega(\beta)\le t.
```

`\lambda` và `t` là hai cách encode same trade-off family dưới suitable conditions.

Viewpoint này nối regularization với [Constrained optimization, Lagrange và KKT](../08_optimization_numerical/03_constrained_optimization_lagrange_and_kkt.md).

## 14. MAP interpretation: regularization như prior

Trong Bayesian view, Gaussian prior trên coefficients:

```math
\beta_j\sim N(0,\tau^2)
```

kết hợp Gaussian likelihood dẫn tới MAP objective tương ứng với L2 penalty.

Laplace prior dẫn tới L1-like penalty.

Vì vậy regularization có thể được hiểu theo ba languages:

```text
optimization penalty
↔ constrained complexity
↔ probabilistic prior
```

Không nên nói mọi regularizer “thực sự là Bayesian prior”; nhưng mathematical correspondence giúp thấy cùng structure từ nhiều góc.

## 15. Basis expansion: linear model vẫn có thể nonlinear theo input

Ta có thể transform input thành basis functions:

```math
\phi(x)=
(1,x,x^2,x^3,\ldots).
```

Rồi fit

```math
f(x)=\beta^T\phi(x).
```

Model linear theo parameters `\beta` nhưng nonlinear theo raw `x`.

Increasing number of basis functions tăng representational flexibility. Regularization giúp control high-order coefficients và giảm variance.

Spline models, kernels và many feature-engineering approaches đều dùng same pattern: map inputs vào richer representation rồi control effective complexity.

## 16. Cross-validation: simulate repeated out-of-sample prediction

Trong **k-fold cross-validation / k겹 교차검증**, split data thành `k` folds. Với mỗi fold:

1. fit model trên `k-1` folds;
2. evaluate trên held-out fold;
3. repeat để mỗi fold được hold out một lần;
4. average validation losses.

Estimate:

```math
CV_k
=
\frac{1}{k}\sum_{j=1}^{k}\text{Loss on fold }j.
```

Cross-validation dùng data hiệu quả hơn một single validation split, đặc biệt khi sample không lớn.

Nhưng folds phải respect data structure. Random k-fold không appropriate nếu observations clustered, grouped hoặc time-ordered theo cách tạo dependency/leakage.

## 17. Nested cross-validation: đánh giá cả model-selection procedure

Nếu dùng CV để chọn hyperparameters rồi report chính minimum CV score đó như final performance, estimate có thể optimistic vì ta đã search over many candidates.

**Nested CV / 중첩 교차검증** có:

```text
outer loop → estimate generalization
inner loop → choose hyperparameters
```

Outer held-out fold không được dùng để select hyperparameters. Ta đánh giá whole model-selection procedure, không chỉ một fitted model.

## 18. High-dimensional setting: khi p gần hoặc lớn hơn n

Nếu number of features `p` lớn so với sample size `n`, ordinary least squares có thể non-unique hoặc extremely unstable.

Khi `p>n`, design matrix cannot have full column rank. Có infinitely many coefficient vectors producing same training fit trong noiseless linear algebra sense.

Regularization hoặc structural assumptions trở thành essential, không chỉ optional tuning.

High-dimensional learning thường cần assumptions như sparsity, smoothness, low rank hoặc manifold structure để convert finite data thành identifiable prediction problem.

## 19. Effective complexity quan trọng hơn parameter count đơn thuần

Hai models có cùng number of parameters có thể có different effective flexibility do regularization, architecture hoặc constraints.

Ridge với very large `\lambda` có many coefficients nhưng effective degrees of freedom thấp hơn unregularized fit.

Vì vậy “model có bao nhiêu parameters?” là useful but incomplete question. Ta cần hỏi data có thể làm fitted function thay đổi tự do đến mức nào.

## 20. Model selection criteria: AIC/BIC không giống cross-validation

Criteria như AIC/BIC combine fit và complexity penalties từ different theoretical goals.

Cross-validation directly estimates held-out predictive loss under resampling scheme.

AIC, BIC và CV có thể select different models vì mục tiêu/assumptions khác nhau. Không nên dùng chúng như interchangeable magic scores.

Đọc cùng [Likelihood / MLE / MAP và model selection](./10_likelihood_mle_map_and_model_selection.md) để xem likelihood-based viewpoint.

## 21. Classification: accuracy có thể đánh lừa

Nếu positive class chỉ 1%, model luôn predict negative đạt 99% accuracy nhưng vô dụng cho detecting positives.

Metrics phải align với task:

- precision;
- recall/sensitivity;
- specificity;
- ROC-AUC;
- PR-AUC;
- log loss;
- calibration;
- cost-weighted decision metrics.

Không có “best metric” độc lập với decision context.

## 22. Discrimination và calibration là hai properties khác nhau

Một probabilistic model có thể rank high-risk cases tốt nhưng probabilities poorly calibrated.

**Discrimination / 판별력** hỏi model xếp positive cases cao hơn negative cases tốt đến đâu.

**Calibration / 보정** hỏi trong nhóm predictions khoảng `0.7`, outcome có xảy ra khoảng 70% không.

Trong medical risk, credit risk hoặc weather probability, calibration có ý nghĩa decision trực tiếp. AUC tốt không guarantee probabilities có interpretation đúng.

## 23. Distribution shift: generalization cần assumption về tương lai

Train/test logic thường ngầm giả định future data sufficiently similar với data-generating process của training/evaluation.

Nếu distribution đổi:

```math
P_{train}(X,Y)\ne P_{deploy}(X,Y),
```

historical test performance có thể không transfer.

Các dạng shift thường được phân biệt như covariate shift, label/prior shift hoặc concept drift. Naming phụ thuộc assumptions, nhưng central problem là same:

> evaluation chỉ valid cho distribution mà nó represent.

No amount of cross-validation trên old regime chứng minh performance trong a fundamentally different regime.

## 24. Model misspecification và no-free-lunch intuition

Every learning method carries inductive bias: assumptions/preferences quyết định patterns nào được considered plausible.

Linear regression ưu tiên linear structure. Trees ưu tiên piecewise partition structure. Smooth kernels ưu tiên local smoothness. Neural architectures encode invariances/compositional structure theo design.

Không có model universally best trên mọi possible data-generating processes. Success đến từ matching inductive bias, data scale, loss và deployment constraints.

## 25. Why “more data” thường giúp nhưng không chữa mọi thứ

More representative independent data thường giảm sampling variance và cho phép estimate richer models tốt hơn.

Nhưng more data không sửa:

- label leakage;
- systematic measurement bias;
- confounding trong causal question;
- wrong target definition;
- distribution mismatch;
- inappropriate loss/metric;
- duplicated/dependent observations bị coi như independent.

Quantity không thay thế data-generating design.

## 26. Connection với optimization

Learning model thường là optimization:

```math
\hat\theta
=
\arg\min_\theta
\left[
\hat R_n(\theta)+\lambda\Omega(\theta)
\right].
```

Nhưng optimization success và statistical success khác nhau.

Một optimizer có thể tìm training optimum rất chính xác nhưng model generalize tệ. Ngược lại approximate optimization đôi khi acts like implicit regularization.

Tách ba câu hỏi:

```text
Can the model class represent the pattern?
Can the optimizer find a good fitted solution?
Will that solution generalize?
```

## 27. Connection với experimental design

Experimental design controls how data are generated; statistical learning controls how pattern is extracted from finite data.

Nếu assignment randomized tốt, model can focus on heterogeneous treatment effects/prediction with less confounding concern. Nếu data observational, predictive accuracy không tự động imply causal validity.

Một model có thể predict who receives treatment rất tốt mà không answer treatment causes what.

Prediction và causation là different targets.

## 28. A practical workflow

Một disciplined learning workflow:

```text
1. Define deployment target and loss
2. Identify unit of observation and data-generating process
3. Freeze an evaluation protocol
4. Build simple baseline
5. Fit preprocessing only on training data
6. Tune complexity/regularization with validation or CV
7. Diagnose residuals, stability and subgroup behavior
8. Evaluate once on untouched test data
9. Check calibration / uncertainty where relevant
10. Monitor distribution shift after deployment
```

Điểm quan trọng là sequence. Nếu evaluation protocol thay đổi mỗi lần result không đẹp, final score no longer has clean interpretation.

## Mental Model

> Statistical learning là bài toán **ước lượng một rule dùng được ngoài sample**. Training loss nói model giải thích data đã thấy tốt đến đâu; validation/test cố estimate future loss; bias–variance giải thích vì sao flexibility vừa hữu ích vừa nguy hiểm; regularization đặt giới hạn/preference lên những solutions mà optimizer được phép chọn. Generalization không phải thuộc tính của model name mà của cả **model + data + fitting procedure + evaluation protocol + deployment distribution**.

## Common Misconceptions

**“Training accuracy cao nghĩa model tốt.”** Không; model có thể memorize sample.

**“Cross-validation loại bỏ overfitting.”** Không; nó giúp estimate/select, nhưng có thể bị overfit nếu repeatedly tuned against same CV results hoặc pipeline leaks information.

**“Regularization luôn làm model đơn giản hơn theo số parameter.”** Không nhất thiết; nó thường giảm effective flexibility/stability risk mà không xóa parameters.

**“Lasso chọn ra true causal variables.”** Không. Selection phụ thuộc sample, correlations, penalty và predictive objective; causality cần stronger assumptions/design.

**“Test set chỉ là một validation set khác.”** Không nếu muốn unbiased final evaluation; test phải remain untouched cho tới khi procedure đã được fixed.

**“Model tốt trên IID test set chắc chắn tốt khi deploy.”** Không khi deployment distribution khác.

## Nguồn học miễn phí để đi sâu

- Trevor Hastie, Robert Tibshirani, Jerome Friedman, **The Elements of Statistical Learning** — official free PDF: https://hastie.su.domains/ElemStatLearn/main.html . Đây là reference sâu về regression, classification, regularization, model assessment, trees, kernels, boosting và unsupervised learning.
- Marc Peter Deisenroth, A. Aldo Faisal, Cheng Soon Ong, **Mathematics for Machine Learning** — free companion PDF: https://mml-book.github.io/ . Hữu ích để nối linear algebra, calculus, probability và optimization với ML models.
- Abakcus, **Free Math Textbooks from University Mathematicians** — https://abakcus.com/book-lists/free-math-textbooks . Dùng như catalog discovery; source học chính nên ưu tiên trang tác giả/trường đại học.

> **Bàn giao:** Nếu muốn hiểu sâu hơn về prior/regularization, đọc [Bayesian inference và hierarchical models](./12_bayesian_inference_posterior_predictive_and_hierarchical_models.md). Nếu muốn đi theo optimization mechanics, đọc [Gradient descent và convexity](../08_optimization_numerical/01_gradient_descent_and_convexity.md) và [Constrained optimization / KKT](../08_optimization_numerical/03_constrained_optimization_lagrange_and_kkt.md).