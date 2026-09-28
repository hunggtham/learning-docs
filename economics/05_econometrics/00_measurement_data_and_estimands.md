# Đo lường (measurement / 측정), Dữ liệu (data / 데이터) & Estimands — Trước regression phải biết mình đang đo gì

Econometrics không bắt đầu bằng việc chọn một mô hình (model / 모델). Nó bắt đầu bằng câu hỏi: **economic concept nào cần đo, population nào đang được nói tới, kết quả (outcome / 결과)/treatment là gì, và quantity nào thật sự cần estimate?** Nếu đo lường (measurement / 측정) hoặc estimand sai, một regression chạy hoàn hảo về kỹ thuật vẫn trả lời sai câu hỏi.

## 1. Dữ liệu (data / 데이터) không phải reality nguyên bản

Một dataset là kết quả của đo lường (measurement / 측정) tiến trình (process / 프로세스): definitions, sampling frame, reporting incentives, missing dữ liệu (data / 데이터), timing, revisions và transformations.

Ví dụ “income” có thể là gross labor income, disposable household income, taxable income hoặc total economic resources. “Employment” có thể là payroll job, person employed, hours worked hoặc self-reported labor status.

Trước khi mô hình (model / 모델) hóa, phải viết operational definition.

## 2. Đơn vị (unit / 단위) of observation

Đơn vị (unit / 단위) có thể là:

```text
person
household
firm
product
county
country
year
person-year
firm-quarter
```

Nếu kết quả (outcome / 결과) ở firm mức (level / 수준) nhưng treatment ở region mức (level / 수준), tiêu chuẩn (standard / 표준) lỗi (error / 오류) và interpretation phải phản ánh assignment/clustering mức (level / 수준).

## 3. Cross-section, thời gian (time / 시간) series và panel

Cross-sectional dữ liệu (data / 데이터) quan sát nhiều units tại một thời điểm hoặc cửa sổ (window / 윈도우) ngắn.

Time-series dữ liệu (data / 데이터) theo dõi một aggregate/đơn vị (unit / 단위) qua thời gian.

Panel/longitudinal dữ liệu (data / 데이터) theo dõi cùng units qua nhiều periods.

Cấu trúc dữ liệu (data / 데이터) quyết định variation nào có thể dùng để identify tác động (effect / 효과). Panel không tự động nhân quả (causal / 인과적); nó chỉ mở thêm within-unit variation.

## 4. Population, mẫu (sample / 표본) và sampling frame

Population là tập đối tượng mục tiêu (target / 대상) của suy luận (inference / 추론). Mẫu (sample / 표본) là phần thực sự quan sát. Sampling frame là danh sách/tiến trình (process / 프로세스) từ đó mẫu (sample / 표본) được lấy.

Một random mẫu (sample / 표본) từ wrong frame vẫn không đại diện mục tiêu (target / 대상) population.

Ví dụ survey online tự nguyện có thể overrepresent người quan tâm topic dù cỡ mẫu (sample size / 표본 크기) rất lớn.

## 5. Selection into mẫu (sample / 표본)

Selection độ lệch (bias / 편향) xuất hiện khi xác suất (probability / 확률) được quan sát liên quan tới variables quan trọng cho question.

Examples:

- wage dữ liệu (data / 데이터) chỉ có cho employed workers;
- hospital kết quả (outcome / 결과) chỉ có cho patients who seek care;
- app usage dữ liệu (data / 데이터) chỉ có users who adopt app;
- firm survival dữ liệu (data / 데이터) bỏ firms đã exit.

Cần hỏi missingness/selection xảy ra trước hay sau treatment/kết quả (outcome / 결과).

## 6. Missing dữ liệu (data / 데이터) mechanisms

Một taxonomy thường dùng:

- **MCAR**: missingness độc lập với observed/unobserved values;
- **MAR**: conditional on observed variables, missingness không còn phụ thuộc missing giá trị (value / 값);
- **MNAR**: missingness vẫn phụ thuộc unobserved giá trị (value / 값).

MCAR rất mạnh. Imputation không “chữa” MNAR nếu cơ chế (mechanism / 메커니즘) không được mô hình (model / 모델) hoặc bounded.

## 7. Sai số đo lường (measurement error / 측정 오차)

Observed variable có thể viết:

```text
X_observed = X_true + measurement error
```

Classical sai số đo lường (measurement error / 측정 오차) trong regressor thường attenuate slope toward zero trong simple regression, nhưng non-classical lỗi (error / 오류) có thể độ lệch (bias / 편향) bất kỳ hướng nào.

Kết quả (outcome / 결과) sai số đo lường (measurement error / 측정 오차) thường tăng noise nếu independent, nhưng differential reporting theo treatment có thể tạo độ lệch (bias / 편향).

## 8. Construct validity

Economic constructs như productivity, thị trường (market / 시장) power, trust, financial stress hoặc skill không quan sát trực tiếp hoàn hảo.

Proxy có construct validity khi nó thật sự capture concept cần nghiên cứu, không chỉ correlate thuận tiện.

Ví dụ kiểm thử (test / 테스트) score đo một phần academic skill nhưng không đồng nhất toàn bộ human capital.

## 9. Độ tin cậy (reliability / 신뢰성) khác validity

Đo lường (measurement / 측정) reliable nghĩa lặp lại cho kết quả ổn định. Valid nghĩa đo đúng construct.

Một quy mô (scale / 규모) có thể rất reliable nhưng consistently đo sai thing.

## 10. Nominal, real và chỉ mục (index / 인덱스) construction

Economic dữ liệu (data / 데이터) cần normalization. Nominal revenue tăng có thể do price hoặc quantity. Real variables cần deflator phù hợp.

Chỉ mục (index / 인덱스) numbers phụ thuộc basket, weights, rebasing và chất lượng (quality / 품질) adjustment. Không coi chỉ mục (index / 인덱스) là vật lý (physical / 물리적) đơn vị (unit / 단위) trực tiếp.

## 11. Log transformation

Logs thường dùng vì:

```text
log differences ≈ percentage changes
```

và biến multiplicative quan hệ (relation / 관계) thành additive.

Nhưng log không defined cho zero/negative values; cách thêm constant tùy tiện có thể đổi interpretation.

## 12. Tỷ lệ (rate / 비율), ratio và denominator bài toán (problem / 문제)

Một tỷ lệ (rate / 비율) thay đổi có thể do numerator hoặc denominator.

Unemployment tỷ lệ (rate / 비율) giảm vì employed tăng khác hoàn toàn labor force shrink. Debt/GDP giảm có thể do debt repayment, nominal GDP growth hoặc inflation.

Luôn decomposed denominator trước khi kể nhân quả (causal / 인과적) story.

## 13. Stock, luồng (flow / 흐름) và timing alignment

Một stock tại cuối năm không nên tùy tiện regress với luồng (flow / 흐름) của period khác mà không xác định timing.

Treatment phải xảy ra trước kết quả (outcome / 결과) nếu nhân quả (causal / 인과적) direction yêu cầu như vậy. Dữ liệu (data / 데이터) annual có thể che intra-year thứ tự (ordering / 순서).

## 14. Data-generating tiến trình (process / 프로세스)

Data-generating tiến trình (process / 프로세스) (DGP) là conceptual cơ chế (mechanism / 메커니즘) tạo observed dữ liệu (data / 데이터).

Một mô hình (model / 모델) không cần replicate toàn bộ reality; nó phải capture phần DGP cần cho estimand.

Econometric lập luận (reasoning / 추론) hỏi:

```text
What variation generated X?
Why did Y move?
Which common causes generated both?
```

## 15. Descriptive parameter vs nhân quả (causal / 인과적) estimand

Descriptive mục tiêu (target / 대상) có thể là:

```text
mean income
median wage
correlation
forecast error
conditional expectation
```

Nhân quả (causal / 인과적) mục tiêu (target / 대상) có thể là average treatment tác động (effect / 효과).

Không mọi useful question đều nhân quả (causal / 인과적). Forecasting tomorrow’s demand có thể cần prediction, không cần treatment tác động (effect / 효과).

## 16. Potential outcomes

Nhân quả (causal / 인과적) khung phần mềm (framework / 프레임워크) thường viết mỗi đơn vị (unit / 단위) có hai potential outcomes:

```text
Y_i(1) = outcome if treated
Y_i(0) = outcome if untreated
```

Individual treatment tác động (effect / 효과):

```text
τ_i = Y_i(1) − Y_i(0)
```

Fundamental bài toán (problem / 문제): cùng một đơn vị (unit / 단위) không thể simultaneously quan sát cả hai states tại cùng thời điểm. Nhân quả (causal / 인과적) suy luận (inference / 추론) là bài toán xây credible counterfactual cho potential kết quả (outcome / 결과) bị thiếu.

## 17. ATE, ATT và LATE

Average Treatment Tác động (effect / 효과):

```text
ATE = E[Y(1) − Y(0)]
```

Average Treatment Tác động (effect / 효과) on the Treated:

```text
ATT = E[Y(1) − Y(0) | D=1]
```

Instrumental-variable settings có thể identify Cục bộ (local / 로컬) Average Treatment Tác động (effect / 효과) (LATE) cho compliers dưới các giả định (assumptions / 가정들) cụ thể.

Các estimands không interchangeable. Chính sách (policy / 정책) question phải quyết định population nào quan trọng.

## 18. Treatment phải được định nghĩa rõ

“Education”, “chính sách (policy / 정책)”, “exposure” hoặc “credit” thường quá mơ hồ.

Treatment cần dose, timing, duration và phiên bản (version / 버전). Một year schooling thêm ở primary school có thể khác university. Tax reform có nhiều components cùng lúc.

Nếu treatment có multiple versions, Stable Đơn vị (unit / 단위) Treatment Giá trị (value / 값) Giả định (assumption / 가정) (SUTVA) có thể bị đe dọa.

## 19. Interference và spillovers

Tiêu chuẩn (standard / 표준) potential-outcomes notation thường giả định kết quả (outcome / 결과) của đơn vị (unit / 단위) i không phụ thuộc treatment của đơn vị (unit / 단위) j.

Mạng (network / 네트워크), vaccination, classroom, labor thị trường (market / 시장) và geographic chính sách (policy / 정책) thường có spillovers.

Nếu interference tồn tại, estimand phải mở rộng từ own-treatment tác động (effect / 효과) sang direct/indirect/mạng (network / 네트워크) effects.

## 20. Counterfactual không phải prediction đơn thuần

Prediction hỏi `Y sẽ là bao nhiêu?`. Nhân quả (causal / 인과적) counterfactual hỏi `Y sẽ khác bao nhiêu nếu intervention thay đổi trong khi các điều kiện relevant khác được giữ theo causal structure?`

Một mô hình (model / 모델) forecast tốt không nhất thiết estimate nhân quả (causal / 인과적) tác động (effect / 효과) đúng nếu nó dựa vào variables downstream hoặc proxies của selection.

## 21. DAG intuition

Directed acyclic đồ thị (graph / 그래프) (DAG) là công cụ biểu diễn các giả định (assumptions / 가정들) về nhân quả (causal / 인과적) paths.

Nếu `Z` gây cả treatment `D` và kết quả (outcome / 결과) `Y`, `Z` là confounder:

```text
Z → D
Z → Y
```

Conditioning on confounder có thể khối (block / 블록) backdoor đường dẫn (path / 경로). Nhưng conditioning on collider có thể tạo độ lệch (bias / 편향).

## 22. Collider độ lệch (bias / 편향)

Nếu:

```text
D → C ← U
```

và ta điều kiện (condition / 조건) on `C`, D và U có thể trở nên statistically associated dù ban đầu independent.

Examples thường xuất hiện khi mẫu (sample / 표본) chỉ gồm hired workers, hospitalized patients hoặc selected applicants.

Không phải “điều khiển (control / 제어) càng nhiều càng tốt”.

## 23. Bad controls

Điều khiển (control / 제어) variable nằm sau treatment có thể absorb một phần treatment tác động (effect / 효과) hoặc mở collider đường dẫn (path / 경로).

Nếu chính sách (policy / 정책) `D` làm income `M` tăng và income làm health `Y` tăng, controlling for `M` chuyển estimand từ total tác động (effect / 효과) sang something closer to direct tác động (effect / 효과).

Điều khiển (control / 제어) choice phải dựa nhân quả (causal / 인과적) question, không chỉ p-value.

## 24. Sampling bất định (uncertainty / 불확실성) vs identification bất định (uncertainty / 불확실성)

Tiêu chuẩn (standard / 표준) lỗi (error / 오류) đo sampling bất định (uncertainty / 불확실성) conditional on mô hình (model / 모델)/thiết kế (design / 설계). Nó không đo bất định (uncertainty / 불확실성) về omitted confounders, wrong functional form, invalid instrument hay bad đo lường (measurement / 측정).

Một estimate có SE cực nhỏ vẫn có thể causally wrong.

## 25. Nội bộ (internal / 내부) và bên ngoài (external / 외부) validity

Nội bộ (internal / 내부) validity hỏi estimate có credible cho studied mẫu (sample / 표본)/ngữ cảnh (context / 맥락) không.

Bên ngoài (external / 외부) validity hỏi tác động (effect / 효과) có generalize sang population, thời gian (time / 시간), institution hoặc quy mô (scale / 규모) khác không.

Randomization mạnh về nội bộ (internal / 내부) validity nhưng không tự đảm bảo bên ngoài (external / 외부) validity.

## 26. Statistical significance vs economic significance

Large mẫu (sample / 표본) có thể làm tiny tác động (effect / 효과) statistically significant.

Cần report tác động (effect / 효과) kích thước (size / 크기), units, confidence interval và economic magnitude.

Một coefficient `0.002` có thể nhỏ hoặc lớn tùy kết quả (outcome / 결과) quy mô (scale / 규모) và chính sách (policy / 정책) chi phí (cost / 비용).

## 27. Pre-analysis thinking

Trước khi chạy mô hình (model / 모델), nên viết:

```text
Question
Population
Treatment / exposure
Outcome
Estimand
Assignment / source of variation
Main confounders
Measurement risks
Expected mechanism
Falsification / robustness ideas
```

Workflow này ngăn “regression fishing” sau khi nhìn kết quả.

## 28. Thất bại (failure / 실패) modes

Sai lầm thứ nhất là dùng dataset lớn để thay cho representative/credible thiết kế (design / 설계).

Sai lầm thứ hai là gọi coefficient nhân quả (causal / 인과적) trước khi xác định counterfactual.

Sai lầm thứ ba là điều khiển (control / 제어) mọi variable available.

Sai lầm thứ tư là dùng statistical significance thay economic magnitude.

Sai lầm thứ năm là không phân biệt ATE, ATT và cục bộ (local / 로컬) tác động (effect / 효과).

Sai lầm thứ sáu là bỏ timing, missingness và đo lường (measurement / 측정) tiến trình (process / 프로세스).

## 29. Mô hình tư duy (mental model / 사고 모델)

Trước mọi econometric phân tích (analysis / 분석), hãy hỏi:

1. Economic concept chính xác là gì?
2. Đơn vị (unit / 단위), population và sampling frame là gì?
3. Variable được đo thế nào, có lỗi (error / 오류)/selection nào?
4. Question là description, prediction hay causality?
5. Estimand chính xác là gì?
6. Counterfactual nào bị thiếu?
7. Variation trong treatment đến từ đâu?
8. Confounders/colliders/post-treatment variables nằm ở đâu?
9. Tiêu chuẩn (standard / 표준) lỗi (error / 오류) có đang che identification bất định (uncertainty / 불확실성) không?
10. Kết quả (result / 결과) có economic magnitude và bên ngoài (external / 외부) validity ra sao?

Sau khi xác định dữ liệu (data / 데이터) và estimand, regression mới trở thành công cụ hữu ích. Chapter tiếp theo xây regression từ conditional expectation và projection, thay vì học OLS như một nút bấm.
