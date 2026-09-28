# Statistics cho Artificial Intelligence

> **Mạch đọc:** Đặt **Statistics cho Artificial Intelligence** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Population, mẫu (sample / 표본) và data-generating tiến trình (process / 프로세스)** sang **Descriptive statistics: mô tả dữ liệu (data / 데이터) trước khi modeling**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Statistics (통계학 / thống kê) giải quyết một tension nằm ở trung tâm của Machine học tập (learning / 학습): ta chỉ quan sát một **finite mẫu (sample / 표본)**, nhưng muốn mô hình (model / 모델) hoạt động tốt trên những dữ liệu (data / 데이터) chưa từng thấy. huấn luyện (training / 학습) set không phải world. Nó chỉ là một mẫu (sample / 표본) được thu thập theo một tiến trình (process / 프로세스) cụ thể, trong một khoảng thời gian cụ thể, với sai số đo lường (measurement error / 측정 오차), selection độ lệch (bias / 편향) và missing thông tin (information / 정보).

Vì vậy Statistics trong AI không chỉ là “mean, median, chart”. Nó cung cấp khung phần mềm (framework / 프레임워크) để hỏi: dữ liệu (data / 데이터) đến từ đâu, estimate đáng tin đến mức nào, mô hình (model / 모델) có generalize không, chỉ số (metric / 지표) chênh nhau có meaningful không, và khi triển khai (deployment / 배포) phân phối (distribution / 분포) thay đổi thì conclusion cũ còn valid không.

Xem trước: [Probability for AI](./02_probability_for_ai.md).

## Population, mẫu (sample / 표본) và data-generating tiến trình (process / 프로세스)

**Population (모집단)** là tập hoặc tiến trình (process / 프로세스) mà ta thực sự quan tâm. **mẫu (sample / 표본)** là dữ liệu (data / 데이터) quan sát được.

Trong ML, cách nhìn mạnh hơn là tưởng tượng có một unknown data-generating phân phối (distribution / 분포):

\[
(X,Y)\sim P_{dữ liệu (data / 데이터)}
\]

Ta chỉ thấy dataset:

\[
D=\{(x_i,y_i)\}_{i=1}^{n}
\]

Nếu samples thực sự independent và identically phân tán (distributed / 분산) (i.i.d.) từ `P_data`, nhiều statistical tools hoạt động cleanly. Nhưng môi trường vận hành (production / 운영 환경) dữ liệu (data / 데이터) thường vi phạm các giả định (assumptions / 가정들) này: người dùng (user / 사용자) events theo thời gian correlated, recommendation chính sách (policy / 정책) ảnh hưởng dữ liệu (data / 데이터) được thu thập, fraudsters thích nghi với detector, hoặc logs chỉ chứa users đã vượt qua một filter trước đó.

Do đó trước mọi statistical suy luận (inference / 추론) phải hỏi: **sampling tiến trình (process / 프로세스) là gì?**

## Descriptive statistics: mô tả dữ liệu (data / 데이터) trước khi modeling

Mean:

\[
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
\]

là center theo arithmetic average, nhưng sensitive với outlier.

Median là quantile 50%, robust hơn với extreme values.

Mẫu (sample / 표본) variance:

\[
s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2
\]

đo spread. `n-1` thay vì `n` xuất hiện để tạo unbiased estimator của population variance dưới tiêu chuẩn (standard / 표준) các giả định (assumptions / 가정들).

Quantiles giúp hiểu tails. Trong độ trễ (latency / 지연 시간) monitoring, p50, p95 và p99 thường informative hơn mean vì người dùng (user / 사용자) experience có thể bị dominated bởi tail độ trễ (latency / 지연 시간).

Descriptive statistics không kết luận causality hay future hiệu năng (performance / 성능); nó chỉ mô tả observed mẫu (sample / 표본).

## Estimator và estimate

Một **estimator (추정량)** là quy tắc (rule / 규칙)/hàm (function / 함수) dùng mẫu (sample / 표본) để estimate unknown population quantity. Kết quả cụ thể từ dataset là **estimate (추정값)**.

Ví dụ mẫu (sample / 표본) mean `\bar X` là estimator của population mean `μ`.

Ta đánh giá estimator bằng nhiều properties:

**độ lệch (bias / 편향)**:

\[
độ lệch (bias / 편향)(\hat\theta)=\mathbb{E}[\hat\theta]-\theta
\]

**Variance**:

\[
Var(\hat\theta)
\]

**Mean Squared lỗi (error / 오류)**:

\[
MSE(\hat\theta)=độ lệch (bias / 편향)(\hat\theta)^2+Var(\hat\theta)
\]

Sự đánh đổi (trade-off / 트레이드오프) độ lệch (bias / 편향)–variance ở estimator mức (level / 수준) liên hệ trực tiếp tới độ lệch (bias / 편향)–variance trong Machine học tập (learning / 학습).

## Law of Large Numbers

Law of Large Numbers nói, dưới conditions phù hợp, mẫu (sample / 표본) average hội tụ về expected giá trị (value / 값) khi cỡ mẫu (sample size / 표본 크기) tăng.

Đây là lý do nhiều empirical estimates trở nên stable hơn với nhiều dữ liệu (data / 데이터).

Nhưng “nhiều dữ liệu (data / 데이터)” không tự chữa sampling độ lệch (bias / 편향). Nếu mẫu (sample / 표본) selection sai, một tỷ records biased vẫn estimate sai population mục tiêu (target / 대상) rất chính xác.

> More dữ liệu (data / 데이터) reduces random lỗi (error / 오류); it does not automatically remove systematic độ lệch (bias / 편향).

## Central Limit Theorem

Central Limit Theorem (CLT / 중심극한정리) giải thích vì sao phân phối (distribution / 분포) của normalized mẫu (sample / 표본) mean thường tiến gần Gaussian khi cỡ mẫu (sample size / 표본 크기) lớn dưới conditions phù hợp, dù individual observations không Gaussian.

Điều này tạo foundation cho tiêu chuẩn (standard / 표준) errors và nhiều confidence intervals.

Tuy nhiên CLT không phải license để assume mọi phân phối (distribution / 분포) trong ML là Gaussian. Heavy tails, strong phụ thuộc (dependency / 의존성) hoặc small mẫu (sample / 표본) có thể làm approximation kém.

## Tiêu chuẩn (standard / 표준) lỗi (error / 오류)

Tiêu chuẩn (standard / 표준) deviation mô tả spread của observations. **tiêu chuẩn (standard / 표준) lỗi (error / 오류)** mô tả bất định (uncertainty / 불확실성) của estimator.

Với mẫu (sample / 표본) mean và i.i.d. samples:

\[
SE(\bar X)=\frac{s}{\sqrt{n}}
\]

Nếu cỡ mẫu (sample size / 표본 크기) tăng 4 lần, tiêu chuẩn (standard / 표준) lỗi (error / 오류) giảm khoảng 2 lần, không phải 4 lần.

Trong mô hình (model / 모델) evaluation, chỉ số (metric / 지표) trên 100 examples và chỉ số (metric / 지표) trên 100,000 examples không nên được tin ngang nhau dù điểm (point / 지점) estimate giống hệt.

## Confidence interval

Confidence interval cung cấp phạm vi (range / 범위) được xây từ một procedure có coverage thuộc tính (property / 속성).

Approximate 95% interval cho mean trong large-sample setting:

\[
\bar{x}\pm1.96\,SE
\]

Một misunderstanding phổ biến là nói “có 95% xác suất (probability / 확률) true mean nằm trong interval đã tính”. Trong classical frequentist interpretation, parameter cố định; procedure tạo intervals có 95% long-run coverage dưới các giả định (assumptions / 가정들).

Trong practical AI, điều quan trọng hơn wording philosophical là: report bất định (uncertainty / 불확실성) thay vì chỉ report điểm (point / 지점) estimate.

## Hypothesis testing

Hypothesis testing bắt đầu từ null hypothesis `H_0`, kiểm thử (test / 테스트) statistic và sampling phân phối (distribution / 분포) dưới `H_0`.

**p-value** là xác suất (probability / 확률) quan sát dữ liệu (data / 데이터) ít nhất extreme như hiện tại nếu `H_0` đúng, không phải xác suất (probability / 확률) `H_0` đúng.

Small p-value không đo tác động (effect / 효과) kích thước (size / 크기). Với dataset rất lớn, tiny tác động (effect / 효과) có thể statistically significant nhưng practically irrelevant.

Trong A/B testing AI sản phẩm (product / 제품), cần xem cả:

- tác động (effect / 효과) kích thước (size / 크기);
- confidence interval;
- cỡ mẫu (sample size / 표본 크기);
- multiple testing;
- nghiệp vụ (business / 비즈니스) impact;
- guardrail metrics.

## Multiple comparisons

Nếu kiểm thử (test / 테스트) 100 hypotheses với threshold 0.05, ngay cả khi tất cả null đều true, ta vẫn kỳ vọng một số false positives.

Các methods như Bonferroni hoặc False Discovery tỷ lệ (rate / 비율) điều khiển (control / 제어) giải quyết vấn đề theo cách khác nhau.

Trong ML experimentation, hyperparameter tìm kiếm (search / 검색) hoặc benchmark trên nhiều tasks có thể tạo **researcher degrees of freedom**: nếu chỉ report best run mà không account tìm kiếm (search / 검색), kết quả (result / 결과) trông stable hơn thực tế.

## Train, kiểm tra hợp lệ (validation / 검증) và kiểm thử (test / 테스트) set là statistical separation

Huấn luyện (training / 학습) set dùng để fit parameters.

Kiểm tra hợp lệ (validation / 검증) set dùng để chọn hyperparameters, kiến trúc (architecture / 아키텍처), threshold hoặc mô hình (model / 모델) phiên bản (version / 버전).

Kiểm thử (test / 테스트) set nên đại diện cho final unbiased-ish estimate sau mô hình (model / 모델) selection.

Nếu continuously nhìn kiểm thử (test / 테스트) kết quả (result / 결과) rồi chỉnh mô hình (model / 모델), kiểm thử (test / 테스트) set đã trở thành kiểm tra hợp lệ (validation / 검증) set về mặt statistical hàm (function / 함수).

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

Trong môi trường vận hành (production / 운영 환경), temporal holdout thường tốt hơn random split khi future dữ liệu (data / 데이터) là mục tiêu (target / 대상) thực.

## Dữ liệu (data / 데이터) leakage

**dữ liệu (data / 데이터) leakage (데이터 누수)** xảy ra khi huấn luyện (training / 학습) tiến trình (process / 프로세스) có truy cập (access / 접근) tới thông tin (information / 정보) không hợp lệ tại prediction thời gian (time / 시간) hoặc từ kiểm tra hợp lệ (validation / 검증)/kiểm thử (test / 테스트) side.

Ví dụ churn prediction dùng tính năng (feature / 기능) “account closed date” để dự đoán customer sẽ churn. mô hình (model / 모델) có accuracy cực cao nhưng tính năng (feature / 기능) chỉ tồn tại sau sự kiện (event / 이벤트) cần predict.

Leakage có thể subtle:

- fit normalization trên toàn dataset trước split;
- duplicate người dùng (user / 사용자) xuất hiện cả train và kiểm thử (test / 테스트);
- target-derived tính năng (feature / 기능);
- future thông tin (information / 정보) trong thời gian (time / 시간) series;
- embeddings/preprocessing trained trên held-out labels.

Leakage làm statistical evaluation optimistic giả tạo.

## Empirical rủi ro (risk / 위험) và expected rủi ro (risk / 위험)

Ta muốn minimize expected rủi ro (risk / 위험):

\[
R(\theta)=\mathbb{E}_{(X,Y)\sim P_{dữ liệu (data / 데이터)}}[L(f_\theta(X),Y)]
\]

Nhưng chỉ có empirical rủi ro (risk / 위험):

\[
\hat R(\theta)=\frac{1}{n}\sum_{i=1}^{n}L(f_\theta(x_i),y_i)
\]

Nếu mô hình (model / 모델) quá flexible, nó có thể giảm `\hat R` bằng cách fit idiosyncrasies của huấn luyện (training / 학습) set mà không giảm true rủi ro (risk / 위험). Đây là heart of overfitting.

## Generalization

**Generalization (일반화)** là khả năng hiệu năng (performance / 성능) trên unseen dữ liệu (data / 데이터) từ mục tiêu (target / 대상) phân phối (distribution / 분포).

Generalization không đơn giản là “kiểm thử (test / 테스트) accuracy cao”. Nếu kiểm thử (test / 테스트) phân phối (distribution / 분포) khác triển khai (deployment / 배포) phân phối (distribution / 분포), kiểm thử (test / 테스트) kết quả (result / 결과) không đại diện mục tiêu (target / 대상).

Một mô hình (model / 모델) có thể generalize tốt within-distribution nhưng thất bại (fail / 실패) khi:

- geography đổi;
- season đổi;
- thiết bị (device / 장치) mix đổi;
- chính sách (policy / 정책) thay đổi;
- người dùng (user / 사용자) hành vi (behavior / 동작) thích nghi;
- đầu vào (input / 입력) ngôn ngữ (language / 언어)/lĩnh vực (domain / 도메인) mới.

Do đó generalization luôn relative to một phân phối (distribution / 분포) family hoặc operating môi trường (environment / 환경).

## Độ lệch (bias / 편향)–variance sự đánh đổi (trade-off / 트레이드오프)

Trong regression với squared lỗi (error / 오류), expected prediction lỗi (error / 오류) có thể conceptually decomposed thành:

\[
lỗi (error / 오류) \approx độ lệch (bias / 편향)^2 + Variance + Irreducible\ Noise
\]

High độ lệch (bias / 편향): mô hình (model / 모델) các giả định (assumptions / 가정들) quá restrictive, underfit mẫu (pattern / 패턴).

High variance: mô hình (model / 모델) sensitive với mẫu (sample / 표본) fluctuations, dễ overfit.

Hiện đại (modern / 현대적) Deep học tập (learning / 학습) phức tạp hơn textbook curve đơn giản; highly overparameterized các mô hình (models / 모델들) vẫn có thể generalize tốt nhờ tối ưu hóa (optimization / 최적화), regularization, dữ liệu (data / 데이터) quy mô (scale / 규모) và implicit biases. Vì vậy độ lệch (bias / 편향)–variance vẫn là useful mô hình tư duy (mental model / 사고 모델), không phải complete lý thuyết (theory / 이론) cho mọi neural mạng (network / 네트워크).

## Regularization như statistical preference

Regularization thêm preference ngoài pure huấn luyện (training / 학습) fit:

\[
J(\theta)=\hat R(\theta)+\lambda\Omega(\theta)
\]

L2 regularization preference smaller parameters. dữ liệu (data / 데이터) augmentation encode invariances. Early stopping giới hạn tối ưu hóa (optimization / 최적화) trajectory. Dropout inject stochastic cấu trúc (structure / 구조).

Từ statistical viewpoint, regularization giảm effective flexibility hoặc encode prior các giả định (assumptions / 가정들) để improve generalization.

## Cross-validation

K-fold cross-validation chia dữ liệu (data / 데이터) thành `K` folds, train trên `K-1` và evaluate fold còn lại, lặp lại.

Nó hữu ích khi dataset nhỏ và muốn dùng dữ liệu (data / 데이터) hiệu quả hơn để estimate hiệu năng (performance / 성능).

Nhưng tiêu chuẩn (standard / 표준) random K-fold không phù hợp mọi tác vụ (task / 작업). Với thời gian (time / 시간) series, cần time-aware split. Với multiple rows per patient/người dùng (user / 사용자), cần group split để tránh thực thể (entity / 엔터티) leakage.

Split chiến lược (strategy / 전략) phải mô phỏng triển khai (deployment / 배포) ranh giới (boundary / 경계).

## Bootstrap

Bootstrap mẫu (sample / 표본) `n` observations **with replacement** từ observed dataset, lặp nhiều lần để approximate sampling phân phối (distribution / 분포) của statistic.

Nó hữu ích để estimate bất định (uncertainty / 불확실성) của chỉ số (metric / 지표) khi analytic formula khó.

Ví dụ muốn confidence interval cho F1 hoặc difference giữa hai các mô hình (models / 모델들), paired bootstrap trên cùng kiểm thử (test / 테스트) examples thường informative.

Bootstrap cũng có các giả định (assumptions / 가정들); strongly dependent dữ liệu (data / 데이터) cần khối (block / 블록)/bootstrap variants hoặc domain-specific treatment.

## Lớp (class / 클래스) imbalance và cơ sở (base / 기반) tỷ lệ (rate / 비율)

Nếu fraud tỷ lệ (rate / 비율) 0.1%, classifier luôn predict “not fraud” có accuracy 99.9% nhưng vô dụng.

Chỉ số (metric / 지표) phải phản ánh quyết định (decision / 결정) need.

Precision:

\[
Precision=\frac{TP}{TP+FP}
\]

Recall:

\[
Recall=\frac{TP}{TP+FN}
\]

False positive tỷ lệ (rate / 비율):

\[
FPR=\frac{FP}{FP+TN}
\]

Cơ sở (base / 기반) tỷ lệ (rate / 비율) ảnh hưởng precision mạnh. Một mô hình (model / 모델) có same sensitivity/specificity có thể có drastically different precision ở population với prevalence khác.

## Threshold là quyết định (decision / 결정) parameter, không phải mô hình (model / 모델) truth

Nhị phân (binary / 이진) classifier có score/xác suất (probability / 확률) `p`. Threshold `0.5` không phải universal law.

Nếu chi phí (cost / 비용) false negative lớn hơn false positive, threshold có thể thấp hơn.

Expected chi phí (cost / 비용):

\[
rủi ro (risk / 위험)(t)=C_{FP}P(FP\mid t)+C_{FN}P(FN\mid t)
\]

Threshold nên chọn theo operating mục tiêu (objective / 목표), sức chứa (capacity / 용량) và rủi ro (risk / 위험) các ràng buộc (constraints / 제약조건들).

Mô hình (model / 모델) evaluation phải nối metrics với quyết định (decision / 결정) economics.

## ROC và Precision–Recall

ROC curve plot TPR vs FPR qua thresholds. ROC-AUC đo ranking ability theo một xác suất (probability / 확률) interpretation.

Precision–Recall curve thường informative hơn với rare positive lớp (class / 클래스) vì precision phản ánh false positives relative to predicted positives.

Không có chỉ số (metric / 지표) universal tốt nhất. chỉ số (metric / 지표) choice là statement về điều hệ thống (system / 시스템) coi trọng.

## Phân phối (distribution / 분포) shift

Huấn luyện (training / 학습) phân phối (distribution / 분포):

\[
P_{train}(X,Y)
\]

Triển khai (deployment / 배포) phân phối (distribution / 분포):

\[
P_{deploy}(X,Y)
\]

Nếu hai distributions khác, mô hình (model / 모델) các giả định (assumptions / 가정들) bị thử thách.

Các patterns thường được phân biệt:

**Covariate shift:** `P(X)` đổi, conditional relationship có thể tương đối stable.

**Label/prior shift:** `P(Y)` đổi.

**Concept shift/drift:** `P(Y|X)` đổi.

Real các hệ thống (systems / 시스템들) có thể kết hợp nhiều loại shift, nên taxonomy chỉ là diagnostic mô hình (model / 모델).

## Selection độ lệch (bias / 편향) và phản hồi (feedback / 피드백) loops

Một recommender chỉ quan sát phản hồi (feedback / 피드백) cho items mà nó đã show. dữ liệu (data / 데이터) tương lai bị chính sách (policy / 정책) hiện tại tạo ra.

```mermaid
flowchart LR
    M[Current Model] --> R[Recommendations]
    R --> U[User Exposure]
    U --> F[Observed Feedback]
    F --> D[Training Data]
    D --> M
```

Nếu không account vòng phản hồi (feedback loop / 피드백 루프), mô hình (model / 모델) có thể reinforce popularity hoặc hide alternatives mà nó chưa thử.

Đây là liên kết (connection / 연결) giữa Statistics, nhân quả (causal / 인과적) suy luận (inference / 추론), Bandits và Recommender các hệ thống (systems / 시스템들).

## Correlation và causation

Nếu users dùng tính năng (feature / 기능) A thường retention cao, không có nghĩa forcing A sẽ tăng retention. Có thể engaged users tự chọn A.

Prediction hỏi:

> `Y` có thể được dự đoán từ `X` không?

Nhân quả (causal / 인과적) suy luận (inference / 추론) hỏi:

> Nếu chủ động thay đổi `X`, `Y` sẽ thay đổi thế nào?

Machine học tập (learning / 학습) rất mạnh cho prediction nhưng nhân quả (causal / 인과적) question cần các giả định (assumptions / 가정들), experiments hoặc nhân quả (causal / 인과적) identification chiến lược (strategy / 전략) khác.

## A/B testing

Randomized controlled experiment gán units ngẫu nhiên vào treatment/điều khiển (control / 제어) để break confounding on average.

Trong AI sản phẩm (product / 제품), A/B testing có thể compare recommendation thuật toán (algorithm / 알고리즘), ranking chính sách (policy / 정책) hoặc assistant hành vi (behavior / 동작).

Nhưng cần chú ý interference: một người dùng (user / 사용자)'s treatment có thể ảnh hưởng người khác, ví dụ marketplace hoặc xã hội (social / 사회적) mạng (network / 네트워크). Khi SUTVA-like các giả định (assumptions / 가정들) thất bại (fail / 실패), tiêu chuẩn (standard / 표준) phân tích (analysis / 분석) có thể misleading.

## Offline evaluation và online evaluation

Offline kiểm thử (test / 테스트) set giúp iterate nhanh và reproducibly. Online experiment đo actual sản phẩm (product / 제품) impact.

Hai thứ có thể disagree vì offline chỉ số (metric / 지표) chỉ proxy for người dùng (user / 사용자)/nghiệp vụ (business / 비즈니스) kết quả (outcome / 결과).

Ví dụ recommender tăng NDCG nhưng làm feed quá homogeneous, giảm long-term discovery. AI hệ thống (system / 시스템) evaluation cần chỉ số (metric / 지표) hierarchy thay vì một score duy nhất.

## Statistical power

Power là xác suất (probability / 확률) detect tác động (effect / 효과) khi tác động (effect / 효과) thật sự tồn tại ở specified kích thước (size / 크기).

Experiment thiếu power dễ tạo inconclusive kết quả (result / 결과). cỡ mẫu (sample size / 표본 크기) planning cần expected variance, minimum detectable tác động (effect / 효과) và significance/power targets.

Không nên “chạy tới khi p<0.05 rồi dừng” nếu stopping quy tắc (rule / 규칙) không accounted, vì optional stopping inflate false positive rủi ro (risk / 위험).

## Reproducibility và random seeds

Huấn luyện (training / 학습) Deep học tập (learning / 학습) có stochasticity từ initialization, dữ liệu (data / 데이터) thứ tự (order / 순서), dropout, nondeterministic kernels.

Một single run có thể không đại diện phương thức (method / 메서드) hiệu năng (performance / 성능).

Khi feasible, report multiple runs, variation và experimental giao thức (protocol / 프로토콜). Seed giúp reproducibility nhưng không biến kết quả (result / 결과) thành universal truth.

## Mô hình tư duy (mental model / 사고 모델)

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

## Dùng chung (common / 공통) Misconceptions

### “Dataset càng lớn thì độ lệch (bias / 편향) càng ít”

Larger `n` giảm sampling variance nhưng systematic selection độ lệch (bias / 편향) có thể giữ nguyên hoặc mạnh hơn.

### “kiểm thử (test / 테스트) accuracy là hiệu năng (performance / 성능) thực tế”

Chỉ khi kiểm thử (test / 테스트) phân phối (distribution / 분포) và evaluation giao thức (protocol / 프로토콜) đại diện triển khai (deployment / 배포) mục tiêu (target / 대상) đủ tốt.

### “p < 0.05 nghĩa là tác động (effect / 효과) quan trọng”

p-value không nói tác động (effect / 효과) kích thước (size / 크기) hay nghiệp vụ (business / 비즈니스) importance.

### “Cross-validation luôn tốt hơn một kiểm thử (test / 테스트) split”

Không. Với time-dependent hoặc grouped dữ liệu (data / 데이터), naive CV có thể leak thông tin (information / 정보). Split thiết kế (design / 설계) phải mirror triển khai (deployment / 배포).

## Liên kết kiến thức (knowledge connection / 지식 연결)

Statistics là cầu nối (bridge / 브리지) giữa [Probability](./02_probability_for_ai.md) và Machine học tập (learning / 학습). Sau này các chapter về generalization, mô hình (model / 모델) evaluation, calibration, dataset độ lệch (bias / 편향) và drift sẽ reuse các ideas ở đây.

Khi nhìn một mô hình (model / 모델) score, đừng chỉ hỏi “bao nhiêu phần trăm?”. Hãy hỏi: trên population nào, mẫu (sample / 표본) được lấy thế nào, bất định (uncertainty / 불확실성) của estimate bao nhiêu, selection đã xảy ra ở đâu, và triển khai (deployment / 배포) phân phối (distribution / 분포) có giống evaluation phân phối (distribution / 분포) không.

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 mathematics for ai](./00_mathematics_for_ai.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
