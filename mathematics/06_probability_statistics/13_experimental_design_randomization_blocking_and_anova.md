# Experimental design: randomization, blocking, factorial designs và ANOVA

> **Mạch đọc:** Chapter này nối [Sampling, estimation, confidence và hypothesis testing](./07_sampling_estimation_confidence_and_hypothesis_testing.md) với causal reasoning và statistical modeling. Statistics không chỉ hỏi “sau khi có data thì tính gì?”; một phần quan trọng hơn là **data được tạo ra bằng cơ chế nào**.

Một analysis rất tinh vi không thể cứu một experiment được thiết kế tệ. Nếu treatment và control khác nhau ngay từ đầu, hoặc measurement process confounded với treatment assignment, model phía sau có thể cho p-value rất chính xác cho một câu hỏi sai.

Vì vậy **thiết kế thí nghiệm (experimental design / 실험 설계)** bắt đầu trước khi thu dữ liệu.

## 1. Ba object phải phân biệt

Một experiment có ít nhất ba loại object:

- **đơn vị thí nghiệm (experimental unit / 실험 단위):** object nhận treatment;
- **treatment / 처치:** intervention hoặc condition ta muốn so sánh;
- **response / 반응변수:** outcome được đo sau đó.

Ví dụ A/B test cho checkout page:

```text
experimental unit = user
treatment A       = old checkout
treatment B       = new checkout
response          = purchase / conversion value
```

Nếu treatment được gán theo device nhưng response lại phân tích theo page view, unit of assignment và unit of analysis khác nhau; standard errors có thể sai vì observations không độc lập theo cách model giả định.

## 2. Observational study khác randomized experiment ở đâu?

Trong **nghiên cứu quan sát (observational study / 관찰 연구)**, researcher quan sát exposure/treatment đã xảy ra. Trong **thí nghiệm ngẫu nhiên (randomized experiment / 무작위 실험)**, assignment được controlled và randomized.

Randomization tạo một mechanism giúp treatment groups comparable **in expectation**. Nó không bảo đảm mọi covariate cân bằng hoàn hảo trong một sample hữu hạn, nhưng nó phá systematic relationship giữa treatment assignment và pre-treatment characteristics.

Đây là lý do randomized experiments có causal interpretation mạnh hơn ordinary correlation studies.

## 3. Randomization giải quyết selection bias bằng design

Giả sử ta muốn estimate average treatment effect:

```math
\tau=\mathbb E[Y(1)-Y(0)].
```

Với mỗi unit, `Y(1)` là potential outcome nếu nhận treatment và `Y(0)` nếu control. Ta chỉ quan sát một trong hai; đây là **fundamental problem of causal inference**.

Random assignment tạo independence giữa treatment indicator `T` và potential outcomes theo design:

```math
T \perp (Y(0),Y(1)).
```

Do đó difference in group means có thể estimate treatment effect mà không cần model selection mechanism phức tạp như trong observational data.

Randomization không phải “làm mọi thứ random”. Nó là deliberate mechanism để biến unknown confounders thành noise thay vì systematic bias.

## 4. Replication: tách signal khỏi random variation

**Lặp lại (replication / 반복)** nghĩa treatment được áp dụng cho nhiều independent experimental units.

Nếu chỉ quan sát mỗi treatment một lần, ta không biết difference đến từ treatment hay natural unit-to-unit variation.

Với more replication, standard error thường giảm gần theo scale

```math
SE \propto \frac{1}{\sqrt n}
```

trong những settings đơn giản.

Nhưng cần phân biệt **biological/experimental replication** với repeated measurements trên cùng unit. Đo một người 100 lần không tạo 100 independent people.

## 5. Blocking: loại known nuisance variation trước khi randomize

Nếu ta biết một factor ảnh hưởng response nhưng không phải object chính cần nghiên cứu, ta có thể dùng **khối (blocking / 블로킹)**.

Ví dụ so sánh hai fertilizer trên field có gradient đất Bắc–Nam. Randomize hoàn toàn có thể vô tình để nhiều plot tốt vào treatment A. Thay vào đó:

```text
chia field thành các block tương đối đồng nhất
        ↓
randomize treatments bên trong mỗi block
        ↓
compare treatments after accounting for block
```

Blocking dùng knowledge có trước để giảm noise.

Một simple additive model:

```math
Y_{ij}=\mu+\tau_i+\beta_j+\varepsilon_{ij},
```

trong đó `\tau_i` là treatment effect và `\beta_j` là block effect.

Nếu block giải thích nhiều variation, residual variance nhỏ hơn và treatment comparison chính xác hơn.

## 6. Pairing là blocking với block size nhỏ

**Matched pairs / 대응표본** là trường hợp đặc biệt: mỗi block có hai highly comparable units hoặc cùng một unit được đo trong two conditions theo design phù hợp.

Ví dụ before/after measurement trên cùng subject:

```math
D_i=Y_{i,after}-Y_{i,before}.
```

Thay vì model two noisy levels riêng, ta phân tích within-unit difference. Stable person-specific variation bị cancel một phần.

Nhưng before/after không tự động causal: time trend, learning, regression to the mean hoặc concurrent events vẫn có thể confound nếu không có appropriate control.

## 7. Factor khác treatment level như thế nào?

Một **factor / 요인** là một variable được manipulated hoặc structured trong experiment. Mỗi factor có các **levels / 수준**.

Ví dụ:

```text
Factor A: learning method
  A1 = video
  A2 = text

Factor B: feedback
  B1 = immediate
  B2 = delayed
```

Một **factorial design / 요인설계** chạy combinations của levels:

```text
A1B1  A1B2
A2B1  A2B2
```

Điểm mạnh là không chỉ estimate main effects mà còn interaction.

## 8. Interaction: effect của A phụ thuộc B

Nếu effect của method A thay đổi tùy feedback B, ta có **tương tác (interaction / 상호작용)**.

Simple two-factor model:

```math
Y=\mu+\alpha_i+\beta_j+(\alpha\beta)_{ij}+\varepsilon.
```

Nếu interaction term lớn, câu “A tốt hơn B” có thể quá đơn giản. Đúng hơn có thể là:

```text
A tốt khi feedback immediate,
nhưng không tốt khi feedback delayed.
```

Interaction là lý do factorial experiments hiệu quả hơn việc chạy nhiều one-factor experiments rời nhau: system behavior thường không additive hoàn toàn.

## 9. Confounding: hai explanations không thể tách bằng data hiện có

**Nhiễu lẫn (confounding / 교란)** xảy ra khi effect của treatment bị trộn với effect của variable khác.

Ví dụ:

```text
all control users measured in morning
all treatment users measured in evening
```

Nếu conversion khác, ta không thể biết do treatment hay time-of-day.

Mathematically, design matrix có thể không chứa enough independent variation để separate effects. Đây là design-level identifiability problem, không chỉ là “thiếu một covariate trong regression”.

## 10. Why randomize order?

Trong lab, manufacturing hoặc benchmarks, measurement order có thể tạo drift:

- machine warms up;
- operator gets tired;
- battery depletes;
- network traffic changes;
- model cache becomes warm.

Nếu luôn chạy A trước B, **order** confounds treatment. Randomizing hoặc counterbalancing order phân phối drift across treatments thay vì để nó align systematic với một condition.

## 11. ANOVA không đơn giản là “test nhiều means”

**Phân tích phương sai (Analysis of Variance, ANOVA / 분산분석)** decomposes total variation thành components attributable to structured sources và residual noise.

Trong one-way setting:

```math
Y_{ij}=\mu+\tau_i+\varepsilon_{ij}.
```

Total sum of squares có thể decomposed conceptually:

```math
SS_{Total}=SS_{Treatment}+SS_{Error}.
```

ANOVA hỏi treatment-explained variation có lớn so với residual variation không.

F-statistic có dạng

```math
F=\frac{MS_{Treatment}}{MS_{Error}}.
```

Nếu null model đúng và assumptions phù hợp, numerator và denominator estimate cùng noise scale theo different degrees of freedom; ratio quá lớn là evidence against equal-means null.

## 12. Degrees of freedom là số hướng variation độc lập

**Bậc tự do (degrees of freedom / 자유도)** không nên học như arbitrary subtraction rule.

Nếu `k` group means bị constraint bởi overall mean, số independent treatment contrasts là `k-1`. Residual degrees of freedom phản ánh số independent directions còn lại sau khi fitted structure đã “dùng” một phần information.

Linear algebra viewpoint:

> ANOVA là projection của response vector vào orthogonal hoặc structured subspaces tương ứng với model terms.

Liên kết này trở nên rõ khi đọc cùng [Projection và inner product](../04_vectors_linear_algebra/06_inner_product_orthogonality_and_projection.md) và [Regression](./06_regression_and_correlation.md).

## 13. Assumptions của classical ANOVA

Trong basic fixed-effects ANOVA, common assumptions thường gồm:

- independent errors theo design;
- mean model được specified hợp lý;
- roughly constant variance trong basic formulation;
- normality của errors nếu dùng exact small-sample F inference theo classical derivation.

Không nên biến checklist này thành ritual. Quan trọng là biết assumption nào đến từ **design** và assumption nào từ **analysis model**.

Randomization-based inference có thể dựa vào assignment mechanism hơn là normal-error model trong nhiều settings.

## 14. Multiple comparisons và family-wise error

Nếu test rất nhiều pairwise differences với threshold `0.05`, chance có ít nhất một false positive tăng.

Ví dụ với `m` independent null tests, probability không có false positive là roughly

```math
(1-\alpha)^m,
```

nên probability có ít nhất một là

```math
1-(1-\alpha)^m.
```

Vì vậy post-hoc comparisons cần procedures phù hợp như Tukey-style family-wise control hoặc false discovery rate methods tùy mục tiêu.

ANOVA significant không tự nói group nào khác group nào.

## 15. Full factorial và fractional factorial

Nếu có `k` binary factors, full factorial cần

```math
2^k
```

combinations. Khi `k` lớn, cost tăng nhanh.

**Fractional factorial designs / 일부요인설계** chỉ chạy một carefully chosen subset của combinations để estimate important effects với fewer runs.

Trade-off là một số effects trở nên **aliased**: design không thể distinguish chúng nếu không thêm assumptions hoặc runs.

Đây là ví dụ rất rõ của information trade-off:

```text
fewer experimental runs
        ↔
less ability to separate all interactions
```

## 16. Power phải được nghĩ trước experiment

**Statistical power / 검정력** là probability reject null khi một specified alternative thật sự đúng.

Power phụ thuộc effect size, noise, sample size và test/design structure.

Planning sample size sau khi experiment đã thất bại không sửa được data đã thu. Trước experiment, cần định nghĩa **smallest effect size of practical interest** thay vì chỉ hỏi “bao nhiêu sample để p<0.05?”.

Một experiment enormous có thể detect effect trivial; một experiment nhỏ có thể miss effect practically important.

## 17. A/B testing thực tế: unit, interference và repeated exposure

Online experiments có thêm complications:

**Unit:** randomize user, session hay device?

**Repeated exposure:** cùng user có thể thấy treatment nhiều lần, làm observations correlated.

**Interference:** treatment của một user có thể ảnh hưởng user khác, ví dụ social network, marketplace hoặc pricing system. Classical assumption that one unit's outcome does not depend on others' treatment có thể hỏng.

**Novelty effect:** response ban đầu khác long-run behavior.

**Sample-ratio mismatch:** observed assignment ratio khác intended ratio có thể signal instrumentation/eligibility bug.

Experimental design vì vậy là systems engineering + statistics, không chỉ một test formula.

## 18. Regression và ANOVA là cùng một linear-model language

One-way ANOVA có thể viết thành regression với indicator variables. Ví dụ treatment B indicator `x_i`:

```math
Y_i=\beta_0+\beta_1x_i+\varepsilon_i.
```

Với nhiều groups/factors, design matrix `X` encode group membership, blocks và interactions:

```math
Y=X\beta+\varepsilon.
```

ANOVA tables và regression coefficients là different summaries của cùng geometric model structure.

Điều này quan trọng vì nó nối classical experimental design với generalized linear models, mixed models và modern causal analysis.

## 19. Random effects và hierarchical structure

Nếu blocks, schools, users hoặc machines là sampled từ broader population, ta có thể model group-specific deviations như random effects thay vì fixed coefficients riêng.

Conceptual form:

```math
Y_{ij}=\mu+u_j+\tau_i+\varepsilon_{ij},
```

với

```math
u_j\sim \text{some population distribution}.
```

Hierarchical modeling tách variation between groups và within groups. Đọc tiếp [Bayesian hierarchical models](./12_bayesian_inference_posterior_predictive_and_hierarchical_models.md) để thấy same structure trong probabilistic framework.

## 20. Checklist thiết kế trước khi thu data

Trước experiment, hãy trả lời được:

1. Experimental unit là gì?
2. Treatment assignment mechanism là gì?
3. Response metric định nghĩa trước hay chọn sau khi nhìn data?
4. Có known nuisance factors nên block không?
5. Có repeated measurements hoặc clustered units không?
6. Có interference giữa units không?
7. Có interaction nào practically important?
8. Effect size nào đáng quan tâm về mặt thực tế?
9. Sample size/power đủ không?
10. Missing data và exclusion rules sẽ xử lý thế nào?

Nếu các câu này chưa rõ, việc chọn t-test hay ANOVA thường chưa phải vấn đề cấp bách nhất.

## Mental Model

> Experimental design là cách **engineer information trước khi data tồn tại**. Randomization chống systematic selection, replication estimate noise, blocking loại known nuisance variation, factorial design expose interactions, còn ANOVA/regression decomposes variation theo structure đã được design. Analysis tốt bắt đầu từ assignment mechanism tốt.

## Common Misconceptions

**“Random sample và randomized treatment là một.”** Không. Random sampling liên quan generalization từ sample sang population; randomized treatment liên quan causal comparison giữa treatments.

**“Blocking làm experiment kém random.”** Không; ta randomize *within* sensible blocks để kiểm soát known variation.

**“ANOVA significant nghĩa mọi means khác nhau.”** Không. Nó chỉ evidence rằng equal-means model không đủ trong setting tương ứng.

**“Có nhiều data thì confounding tự biến mất.”** Sai. Systematic confounding không được chữa bằng sample size; càng nhiều data có thể chỉ làm estimate biased trở nên rất precise.

**“Repeated measurements là independent replication.”** Không nếu chúng share cùng experimental unit hoặc common shocks.

## Nguồn học miễn phí để đi sâu

- R. A. Bailey, **Design of Comparative Experiments** — bản PDF được tác giả/Queen Mary University of London cung cấp tại https://webspace.maths.qmul.ac.uk/r.a.bailey/bookbeam.pdf . Nội dung đi sâu blocking, factorial structure, row-column designs, incomplete blocks và fractional factorial designs.
- Abakcus, **Free Math Textbooks from University Mathematicians** — https://abakcus.com/book-lists/free-math-textbooks . Catalog này là nguồn phát hiện textbook trên và các tài liệu statistics/data science liên quan.

> **Bàn giao:** Đọc tiếp [Statistical learning: generalization, bias–variance và regularization](./14_statistical_learning_bias_variance_regularization_and_validation.md) để chuyển từ “design data-generating process” sang “học model từ finite data mà không overfit”.