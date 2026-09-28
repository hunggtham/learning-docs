# Thống kê mô tả và suy luận: từ mẫu (sample / 표본) tới bất định (uncertainty / 불확실성) về population

> **Mạch đọc:** Đọc **Thống kê mô tả và suy luận: từ mẫu (sample / 표본) tới bất định (uncertainty / 불확실성) về population** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Population, mẫu (sample / 표본), parameter và statistic** sang **2. Descriptive statistics chỉ mô tả dữ liệu (data / 데이터) đã thấy**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Thống kê (statistics / 통계학) bắt đầu từ một bất cân xứng rất thực tế: ta muốn biết điều gì đó về một population hoặc tiến trình (process / 프로세스) lớn, nhưng chỉ quan sát được một mẫu (sample / 표본) hữu hạn, noisy và có thể biased.

Xác suất (probability / 확률) thường đi theo hướng

```text
model → consequences
```

còn statistical suy luận (inference / 추론) thường đi ngược:

```text
data → plausible statements về model / parameter / future data
```

Vì vậy statistics không chỉ là “tính mean, variance và p-value”. Nó là lập luận (reasoning / 추론) dưới bất định (uncertainty / 불확실성), và mọi conclusion chỉ có ý nghĩa khi gắn với **sampling cơ chế (mechanism / 메커니즘), các giả định (assumptions / 가정들) và mục tiêu (target / 대상) question**.

## 1. Population, mẫu (sample / 표본), parameter và statistic

Population không nhất thiết là “toàn bộ con người”. Nó có thể là:

- tất cả transactions tương lai của một hệ thống (system / 시스템);
- tiến trình (process / 프로세스) sản xuất tạo measurements;
- phân phối (distribution / 분포) của returns;
- người dùng (user / 사용자) population mà sản phẩm (product / 제품) nhóm (team / 팀) quan tâm.

Parameter là quantity mô tả population/mô hình (model / 모델), ví dụ population mean `\mu` hoặc variance `\sigma^2`.

Statistic là hàm (function / 함수) của observed mẫu (sample / 표본), ví dụ

```math
\bar x=\frac1n\sum_{i=1}^n x_i.
```

Trong frequentist khung phần mềm (framework / 프레임워크), parameter được xem fixed but unknown; statistic là random trước khi mẫu (sample / 표본) được quan sát vì mẫu (sample / 표본) itself random.

## 2. Descriptive statistics chỉ mô tả dữ liệu (data / 데이터) đã thấy

Descriptive statistics trả lời:

> mẫu (sample / 표본) hiện có trông như thế nào?

Inferential statistics hỏi thêm:

> mẫu (sample / 표본) này cho phép nói gì về tiến trình (process / 프로세스) rộng hơn?

Hai tầng không được trộn lẫn.

Một histogram đẹp của mẫu (sample / 표본) không guarantee population có same shape. Một mẫu (sample / 표본) mean chính xác đến nhiều decimal places cũng không guarantee estimator unbiased hoặc representative.

## 3. Center: mean, median và chế độ (mode / 모드) trả lời câu hỏi khác nhau

### Mean

```math
\bar x=\frac1n\sum_i x_i.
```

Mean là balancing điểm (point / 지점) và tối ưu squared-error mất mát (loss / 손실):

```math
\bar x
=
\arg\min_a\sum_i(x_i-a)^2.
```

Đây là lý do mean gắn tự nhiên với least squares.

### Median

Median minimises absolute deviation:

```math
\operatorname{median}(x_i)
\in
\arg\min_a\sum_i|x_i-a|.
```

Nó robust hơn trước outliers.

### Chế độ (mode / 모드)

Chế độ (mode / 모드) là most frequent giá trị (value / 값)/category, hữu ích với discrete/categorical dữ liệu (data / 데이터) nhưng có thể unstable trong continuous settings nếu phụ thuộc binning/density estimation.

Không có một “center đúng” universal; choice phụ thuộc mất mát (loss / 손실), phân phối (distribution / 분포) và question.

## 4. Spread: bất định (uncertainty / 불확실성) nội tại của mẫu (sample / 표본)

Variance đo squared deviation quanh mean:

```math
s^2=
\frac{1}{n-1}
\sum_{i=1}^{n}(x_i-\bar x)^2.
```

Tại sao denominator thường là `n-1` trong mẫu (sample / 표본) variance? Vì mẫu (sample / 표본) mean đã được estimated từ dữ liệu (data / 데이터), làm mất một degree of freedom. Bessel correction làm estimator unbiased cho population variance dưới tiêu chuẩn (standard / 표준) iid các giả định (assumptions / 가정들).

Tiêu chuẩn (standard / 표준) deviation:

```math
s=\sqrt{s^2}
```

trở lại cùng đơn vị (unit / 단위) với dữ liệu (data / 데이터).

IQR:

```math
IQR=Q_3-Q_1
```

robust hơn với heavy tails/outliers.

## 5. Outlier không đồng nghĩa lỗi (error / 오류)

Điểm (point / 지점) xa phần lớn dữ liệu (data / 데이터) có thể là:

- sai số đo lường (measurement error / 측정 오차);
- rare but valid sự kiện (event / 이벤트);
- different subpopulation;
- tail sự kiện (event / 이벤트) quan trọng;
- dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인) bug.

Một quy tắc (rule / 규칙) như `1.5×IQR` chỉ là flagging convention, không phải proof điểm (point / 지점) sai.

Trong finance và độ tin cậy (reliability / 신뢰성), tail observations đôi khi chính là phần cần quan tâm nhất.

## 6. Sampling thiết kế (design / 설계) quan trọng hơn cỡ mẫu (sample size / 표본 크기) đơn thuần

Một mẫu (sample / 표본) lớn nhưng systematically biased có thể cho estimate rất precise của wrong quantity.

Ví dụ survey chỉ thu từ power users có thể estimate sản phẩm (product / 제품) satisfaction của power users cực chính xác nhưng không represent toàn customer cơ sở (base / 기반).

Random sampling giúp giảm selection độ lệch (bias / 편향) theo thiết kế (design / 설계). Stratification, cluster sampling và weighting tồn tại vì real populations hiếm khi mẫu (sample / 표본) đơn giản.

## 7. Estimator có độ lệch (bias / 편향) và variance

Estimator `\hat\theta` có độ lệch (bias / 편향):

```math
\operatorname{Bias}(\hat\theta)
=E[\hat\theta]-\theta.
```

Variance đo estimator fluctuate giữa repeated samples.

Một estimator có thể low độ lệch (bias / 편향) nhưng high variance, hoặc ngược lại.

Mean squared lỗi (error / 오류) decomposition:

```math
E[(\hat\theta-\theta)^2]
=
\operatorname{Var}(\hat\theta)
+\operatorname{Bias}(\hat\theta)^2.
```

Đây là cùng bias-variance sự đánh đổi (trade-off / 트레이드오프) xuất hiện trong machine học tập (learning / 학습).

## 8. Sampling phân phối (distribution / 분포) là cầu nối (bridge / 브리지) tới suy luận (inference / 추론)

Nếu lặp cùng sampling procedure rất nhiều lần và mỗi lần tính statistic, statistic itself có phân phối (distribution / 분포).

Ví dụ mẫu (sample / 표본) mean `\bar X` có

```math
E[\bar X]=\mu
```

và với iid observations variance `\sigma^2`:

```math
\operatorname{Var}(\bar X)=\frac{\sigma^2}{n}.
```

Tiêu chuẩn (standard / 표준) lỗi (error / 오류):

```math
SE(\bar X)=\frac{\sigma}{\sqrt n}
```

hoặc estimate bằng `s/\sqrt n`.

`1/\sqrt n` law giải thích vì sao muốn halve tiêu chuẩn (standard / 표준) lỗi (error / 오류) cần roughly quadruple cỡ mẫu (sample size / 표본 크기).

## 9. Central Limit Theorem: vì sao normal xuất hiện nhiều trong suy luận (inference / 추론)?

Dưới conditions phù hợp, standardized sum/mean của many independent-ish observations tiến tới normal phân phối (distribution / 분포) khi `n` lớn.

Điều này không nói raw dữ liệu (data / 데이터) phải normal. Nó nói **sampling phân phối (distribution / 분포) của aggregate** có thể approximately normal.

Đây là lý do normal-based confidence intervals xuất hiện rộng.

Heavy tails, dependence hoặc small samples có thể làm approximation kém.

## 10. Confidence interval: procedure trước, interval sau

Một 95% confidence procedure được thiết kế sao cho trong repeated sampling, khoảng 95% intervals chứa true parameter dưới các giả định (assumptions / 가정들).

Ví dụ roughly:

```math
\bar x\pm1.96\,SE
```

khi normal approximation phù hợp.

Strict frequentist interpretation không nói “parameter có 95% xác suất (probability / 확률) nằm trong interval này” sau khi dữ liệu (data / 데이터) cố định. Parameter không random trong khung phần mềm (framework / 프레임워크) đó.

Bayesian credible interval có interpretation khác vì posterior treats parameter bất định (uncertainty / 불확실성) probabilistically.

## 11. Hypothesis testing là mô hình (model / 모델) checking có controlled lỗi (error / 오류) rates

Null hypothesis `H_0` định nghĩa tham chiếu (reference / 참조) mô hình (model / 모델).

Ta chọn kiểm thử (test / 테스트) statistic `T` đo discrepancy giữa dữ liệu (data / 데이터) và null.

p-value:

```math
P(
T\text{ at least as extreme as observed}
\mid H_0,
\text{model assumptions}
).
```

Nó **không phải**

```text
P(H0 true | data).
```

Đây là một trong những misconceptions phổ biến nhất.

## 12. kiểu (type / 타입) I, kiểu (type / 타입) II và power

Kiểu (type / 타입) I lỗi (error / 오류): reject true null.

```math
P(\text{Type I})=\alpha
```

khi kiểm thử (test / 테스트) calibrated đúng.

Kiểu (type / 타입) II lỗi (error / 오류): thất bại (fail / 실패) to reject false null.

Power:

```math
1-\beta.
```

Power phụ thuộc:

- tác động (effect / 효과) kích thước (size / 크기);
- cỡ mẫu (sample size / 표본 크기);
- noise;
- significance threshold;
- kiểm thử (test / 테스트)/mô hình (model / 모델) cấu trúc (structure / 구조).

Không thể nói một kiểm thử (test / 테스트) “80% power” nếu không specify alternative/tác động (effect / 효과) các giả định (assumptions / 가정들).

## 13. tác động (effect / 효과) kích thước (size / 크기) quan trọng hơn chỉ p-value

Với huge mẫu (sample / 표본), tác động (effect / 효과) rất nhỏ có thể statistically significant.

Ví dụ conversion tăng từ 10.000% lên 10.010% có thể p-value rất nhỏ nếu `n` cực lớn, nhưng nghiệp vụ (business / 비즈니스) impact có thể negligible.

Ngược lại, tác động (effect / 효과) economically important có thể không significant nếu mẫu (sample / 표본) quá nhỏ.

Suy luận (inference / 추론) tốt cần report bất định (uncertainty / 불확실성) + tác động (effect / 효과) magnitude + lĩnh vực (domain / 도메인) relevance.

## 14. Multiple testing và false discoveries

Nếu chạy 100 independent tests ở `\alpha=0.05` khi tất cả null true, expected false rejections khoảng 5.

Bonferroni điều khiển (control / 제어) family-wise lỗi (error / 오류) rất conservative.

False Discovery tỷ lệ (rate / 비율) procedures như Benjamini–Hochberg mục tiêu (target / 대상) expected proportion false discoveries trong rejected set.

Choice phương thức (method / 메서드) phụ thuộc chi phí (cost / 비용) của false positives và phân tích (analysis / 분석) goal.

## 15. Bootstrap: approximate sampling bất định (uncertainty / 불확실성) bằng resampling

Khi analytic sampling phân phối (distribution / 분포) khó derive, bootstrap resamples observed dữ liệu (data / 데이터) with replacement, tính statistic nhiều lần và dùng empirical phân phối (distribution / 분포) của bootstrap statistics.

Nó hữu ích nhưng không magic: nếu original mẫu (sample / 표본) biased hoặc dependence cấu trúc (structure / 구조) ignored, bootstrap không sửa thiết kế (design / 설계) bài toán (problem / 문제).

Thời gian (time / 시간) series cần khối (block / 블록)/bootstrap variants để preserve dependence.

## 16. Causality khác prediction và association

Correlation/regression mô tả association hoặc conditional expectation cấu trúc (structure / 구조). nhân quả (causal / 인과적) question hỏi:

> kết quả (outcome / 결과) sẽ thay đổi thế nào nếu ta intervene và thay treatment/exposure?

Confounders, selection độ lệch (bias / 편향), collider độ lệch (bias / 편향) và reverse causality có thể làm observational association khác nhân quả (causal / 인과적) tác động (effect / 효과).

Randomized experiments giúp vì treatment assignment independent of potential outcomes in expectation dưới proper hiện thực (implementation / 구현).

## 17. Worked example: A/B kiểm thử (test / 테스트) không chỉ là p-value

Giả sử:

```text
Control:   1000 users, 100 conversions
Treatment: 1000 users, 120 conversions
```

Observed rates:

```math
\hat p_C=0.10,
\qquad
\hat p_T=0.12.
```

Absolute lift:

```math
0.12-0.10=0.02
```

= 2 percentage points.

Relative lift:

```math
\frac{0.12-0.10}{0.10}=20\%.
```

Hai numbers đều đúng nhưng answer different questions.

Một complete phân tích (analysis / 분석) còn cần bất định (uncertainty / 불확실성) interval, kiểm thử (test / 테스트) các giả định (assumptions / 가정들), pre-specified chỉ số (metric / 지표), exposure chất lượng (quality / 품질) và practical giá trị (value / 값) của 2-point lift.

## 18. Simpson's paradox: aggregation có thể đảo conclusion

Một trend có thể xuất hiện trong từng subgroup nhưng đảo khi aggregate vì group composition khác nhau.

Điều này nhắc rằng weighted aggregation và conditioning cấu trúc (structure / 구조) matter.

Statistics không chỉ xử lý numbers; nó xử lý **which comparisons are meaningful**.

## 19. Finance: return phân phối (distribution / 분포) và tail rủi ro (risk / 위험)

Mean return và tiêu chuẩn (standard / 표준) deviation chỉ summarize một phần phân phối (distribution / 분포).

Skewness, kurtosis, drawdowns, serial dependence và tail dependence có thể quan trọng hơn.

Assume normal returns có thể underestimate extreme rủi ro (risk / 위험).

Confidence intervals cũng cần distinguish iid các giả định (assumptions / 가정들) với autocorrelated/heteroskedastic financial thời gian (time / 시간) series.

## 20. AI/dữ liệu (data / 데이터): train/kiểm thử (test / 테스트) statistics và dataset shift

Train metrics estimate hiệu năng (performance / 성능) trên huấn luyện (training / 학습) phân phối (distribution / 분포). kiểm tra hợp lệ (validation / 검증)/kiểm thử (test / 테스트) estimate generalization tới related mẫu (sample / 표본) phân phối (distribution / 분포).

Nếu triển khai (deployment / 배포) phân phối (distribution / 분포) shifts, confidence từ iid kiểm thử (test / 테스트) set không guarantee môi trường vận hành (production / 운영 환경) hành vi (behavior / 동작).

Dataset representativeness là statistical giả định (assumption / 가정), không chỉ MLOps detail.

## 21. dùng chung (common / 공통) thất bại (failure / 실패) modes của statistical lập luận (reasoning / 추론)

### Precision without validity

Very narrow confidence interval từ huge biased mẫu (sample / 표본) vẫn có thể center ở wrong mục tiêu (target / 대상).

### p-value worship

Threshold `0.05` không phân chia truth/falsehood. Nó là quyết định (decision / 결정) convention trong defined testing khung phần mềm (framework / 프레임워크).

### Ignoring denominator

“Errors tăng 50%” vô nghĩa nếu traffic cũng tăng 200%; rates và counts answer different questions.

### Post-selection suy luận (inference / 추론)

Nếu ta thử rất nhiều analyses rồi chỉ report one significant kết quả (result / 결과), nominal p-value không còn reflect full tìm kiếm (search / 검색) tiến trình (process / 프로세스).

## Mô hình tư duy (mental model / 사고 모델)

> Statistics là một chuỗi xử lý (pipeline / 파이프라인): define mục tiêu (target / 대상) → understand data-generating/sampling tiến trình (process / 프로세스) → choose estimator/mô hình (model / 모델) → quantify sampling bất định (uncertainty / 불확실성) → check các giả định (assumptions / 가정들) → interpret tác động (effect / 효과) in lĩnh vực (domain / 도메인) ngữ cảnh (context / 맥락). Một number cuối như mean, p-value hay confidence interval chỉ có meaning bên trong chuỗi xử lý (pipeline / 파이프라인) đó.

## Dùng chung (common / 공통) Misconceptions

**Larger mẫu (sample / 표본) luôn solve bài toán (problem / 문제).** Nó giảm random lỗi (error / 오류) nhưng không tự chữa systematic độ lệch (bias / 편향).

**95% confidence interval nghĩa parameter có 95% xác suất (probability / 확률) nằm trong interval cụ thể.** Không trong strict frequentist interpretation.

**Small p-value nghĩa tác động (effect / 효과) lớn hoặc important.** Không; p-value phụ thuộc cả tác động (effect / 효과) và cỡ mẫu (sample size / 표본 크기)/noise.

**Correlation hoặc regression đủ để nói causality.** Không; nhân quả (causal / 인과적) interpretation cần thiết kế (design / 설계)/identification các giả định (assumptions / 가정들) bổ sung.

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 counting and combinatorics](./00_counting_and_combinatorics.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
