# Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Ratio là quantity không phụ thuộc quy mô (scale / 규모) chung** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Ratio, tỷ lệ (rate / 비율) và fraction khác nhau thế nào?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối ratio, proportion và percentage với scale, rate và baseline, để không nhầm thay đổi tuyệt đối với thay đổi tương đối.

Tỉ số (ratio / 비) là một trong những ideas arithmetic quan trọng nhất vì rất nhiều quantities trong đời sống không có ý nghĩa khi nhìn bằng absolute difference alone. “Hơn 10” và “gấp đôi” trả lời hai câu hỏi khác nhau.

Nếu máy chủ (server / 서버) A xử lý 200 requests/s và máy chủ (server / 서버) B xử lý 100 requests/s, difference là 100 requests/s nhưng ratio là

```math
\frac{200}{100}=2.
```

Difference là additive comparison; ratio là multiplicative comparison.

## Ratio là quantity không phụ thuộc quy mô (scale / 규모) chung

Nếu `a:b=2:3`, quy mô (scale / 규모) cả hai bởi cùng positive factor `k`:

```math
ka:kb=2:3.
```

Ratio không đổi. Đây là reason ratios phù hợp mô tả shape, composition và relative allocation.

Recipe 2 parts water : 1 part concentrate vẫn giữ taste nếu quy mô (scale / 규모) từ cups sang liters, miễn cùng ratio.

> **Nối mạch:** Trong **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Ratio, tỷ lệ (rate / 비율) và fraction khác nhau thế nào?** nối từ **Ratio là quantity không phụ thuộc quy mô (scale / 규모) chung** sang **Proportion: equality của ratios**, vì cơ chế trước tạo đầu vào cho bước sau.

## Ratio, tỷ lệ (rate / 비율) và fraction khác nhau thế nào?

Ratio có thể so quantities cùng loại hoặc khác loại.

Nếu same đơn vị (unit / 단위), ratio thường dimensionless:

```math
\frac{10\text{ kg}}{5\text{ kg}}=2.
```

Nếu khác units, ratio trở thành tỷ lệ (rate / 비율):

```math
\frac{120\text{ km}}{2\text{ h}}=60\text{ km/h}.
```

Tỷ lệ (rate / 비율) có đơn vị (unit / 단위) và thường mô tả “per one đơn vị (unit / 단위)” của denominator quantity.

Fraction như `3/5` có thể represent ratio, xác suất (probability / 확률), operator “divide 3 by 5” hoặc part-whole quan hệ (relation / 관계) tùy ngữ cảnh (context / 맥락). Không nên đồng nhất notation với meaning.

> **Nối mạch:** Ở chặng này của **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Proportion: equality của ratios** nối từ **Ratio, tỷ lệ (rate / 비율) và fraction khác nhau thế nào?** sang **Direct proportionality: constant ratio**, vì cơ chế trước tạo đầu vào cho bước sau.

## Proportion: equality của ratios

Tỉ lệ thức (proportion / 비례식):

```math
\frac ab=\frac cd,
```

với denominators nonzero.

Cross multiplication

```math
ad=bc
```

không phải quy tắc (rule / 규칙) riêng cần học thuộc. Multiply both sides bởi `bd`:

```math
bd\frac ab=bd\frac cd,
```

rồi cancel denominators.

Understanding này giúp tránh dùng cross multiplication trong expressions nơi denominator có thể zero hoặc equation không thực sự là equality of ratios.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Direct proportionality: constant ratio** nối từ **Proportion: equality của ratios** sang **Inverse proportionality: constant sản phẩm (product / 제품)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Direct proportionality: constant ratio

Nếu `y` tỷ lệ thuận với `x`:

```math
y=kx.
```

Then

```math
\frac yx=k
```

constant khi `x\neq0`.

Đồ thị (graph / 그래프) đi qua origin vì nếu đầu vào (input / 입력) zero thì đầu ra (output / 출력) zero trong mô hình (model / 모델).

Ví dụ đơn vị (unit / 단위) price fixed `p`:

```math
C=pq.
```

Nếu quantity double, total chi phí (cost / 비용) double.

Nếu đồ thị (graph / 그래프) tuyến tính (linear / 선형) nhưng có intercept:

```math
C=b+pq,
```

thì chi phí (cost / 비용) không proportional với quantity dù vẫn affine/linear-looking. Fixed fee `b` phá constant ratio.

> **Nối mạch:** Trong **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Inverse proportionality: constant sản phẩm (product / 제품)** nối từ **Direct proportionality: constant ratio** sang **Percentage chỉ là ratio trên cơ sở (base / 기반) 100**, vì cơ chế trước tạo đầu vào cho bước sau.

## Inverse proportionality: constant sản phẩm (product / 제품)

Nếu

```math
y=\frac{k}{x},
```

thì

```math
xy=k.
```

Một variable tăng factor `c` thì other giảm factor `c`.

Ideal công việc (work / 작업) mô hình (model / 모델): fixed tải công việc (workload / 워크로드) `W`, identical workers `n`, no coordination overhead:

```math
T=\frac W{rn}.
```

Thời gian (time / 시간) inverse-proportional với workers. Real teams violate các giả định (assumptions / 가정들) vì communication, dependencies và uneven tasks. Đây là example quan trọng: proportionality is a mô hình (model / 모델), not a law by notation alone.

> **Nối mạch:** Ở chặng này của **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Percentage chỉ là ratio trên cơ sở (base / 기반) 100** nối từ **Inverse proportionality: constant sản phẩm (product / 제품)** sang **Percentage thay đổi (change / 변경): denominator là tham chiếu (reference / 참조) trạng thái (state / 상태)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Percentage chỉ là ratio trên cơ sở (base / 기반) 100

Phần trăm là một ratio có mẫu chuẩn bằng 100. Đọc nó theo base giúp phân biệt phần trăm, percentage point và thay đổi tương đối trong các bài toán thực tế.

```math
15\%=\frac{15}{100}=0.15.
```

`p%` của `x`:

```math
\frac p{100}x.
```

Ví dụ:

```math
20\%\text{ of }300
=0.2\times300
=60.
```

Điểm quan trọng là luôn xác định **cơ sở (base / 기반)**. “20% increase” nghĩa 20% của old giá trị (value / 값), không phải new giá trị (value / 값).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, sau nội dung của **Percentage chỉ là ratio trên cơ sở (base / 기반) 100**, **Percentage thay đổi (change / 변경): denominator là tham chiếu (reference / 참조) trạng thái (state / 상태)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Vì sao +10% rồi -10% không cancel?** mở rộng hệ quả hoặc giới hạn liên quan.

## Percentage thay đổi (change / 변경): denominator là tham chiếu (reference / 참조) trạng thái (state / 상태)

Từ old `x` sang new `y`:

```math
\text{relative change}
=
\frac{y-x}{x}.
```

Percentage thay đổi (change / 변경):

```math
\frac{y-x}{x}\times100\%.
```

Từ 80 lên 100:

```math
\frac{20}{80}=25\%.
```

Từ 100 xuống 80:

```math
\frac{-20}{100}=-20\%.
```

Hai percentages khác nhau vì denominator/cơ sở (base / 기반) khác.

> **Nối mạch:** Trong **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Vì sao +10% rồi -10% không cancel?** nối từ **Percentage thay đổi (change / 변경): denominator là tham chiếu (reference / 참조) trạng thái (state / 상태)** sang **Percentage điểm (point / 지점) khác percentage thay đổi (change / 변경)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vì sao +10% rồi -10% không cancel?

Repeated percentage changes multiply growth factors.

Increase 10%:

```math
\times1.10.
```

Decrease 10%:

```math
\times0.90.
```

Combined:

```math
1.10\times0.90=0.99.
```

Net -1%.

Percentage operations live naturally in multiplicative không gian (space / 공간), không additive không gian (space / 공간).

> **Nối mạch:** Ở chặng này của **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Percentage điểm (point / 지점) khác percentage thay đổi (change / 변경)** nối từ **Vì sao +10% rồi -10% không cancel?** sang **Repeated rates dẫn tới exponential growth**, vì cơ chế trước tạo đầu vào cho bước sau.

## Percentage điểm (point / 지점) khác percentage thay đổi (change / 변경)

Nếu interest tỷ lệ (rate / 비율) tăng từ 3% lên 5%:

- increase là 2 **percentage points**;
- relative percentage increase là

```math
\frac{5-3}{3}\approx66.7\%.
```

Hai statements khác nhau mạnh. Reports về polls, rates, margins và thị trường (market / 시장) share thường bị hiểu sai vì trộn hai concepts này.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Repeated rates dẫn tới exponential growth** nối từ **Percentage điểm (point / 지점) khác percentage thay đổi (change / 변경)** sang **Annualized return và geometric mean**, vì cơ chế trước tạo đầu vào cho bước sau.

## Repeated rates dẫn tới exponential growth

Nếu quantity tăng fixed tỷ lệ (rate / 비율) `r` mỗi period:

```math
x_{n+1}=x_n(1+r).
```

Repeated substitution:

```math
x_n=x_0(1+r)^n.
```

Compound interest, population growth, inflation compounding và depreciation đều dùng same multiplicative cấu trúc (structure / 구조).

Arithmetic percentage vì vậy là prerequisite trực tiếp cho exponential functions và finance.

> **Nối mạch:** Trong **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Annualized return và geometric mean** nối từ **Repeated rates dẫn tới exponential growth** sang **Weighted average: denominator tells what is being averaged**, vì cơ chế trước tạo đầu vào cho bước sau.

## Annualized return và geometric mean

Nếu returns nhiều periods là `r_1,...,r_n`, wealth multiplier là

```math
\prod_{i=1}^n(1+r_i).
```

Average arithmetic return

```math
\frac1n\sum r_i
```

không reproduce final wealth generally.

Geometric average growth tỷ lệ (rate / 비율) `g` thỏa

```math
(1+g)^n
=
\prod_{i=1}^n(1+r_i).
```

Đây là reason finance phân biệt arithmetic average và compound growth.

### Worked example

Year 1 +50%, year 2 -50%:

```math
1.5\times0.5=0.75.
```

Total wealth giảm 25%, dù arithmetic average return là 0%.

Multiplicative tiến trình (process / 프로세스) cần multiplicative aggregation.

> **Nối mạch:** Ở chặng này của **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Weighted average: denominator tells what is being averaged** nối từ **Annualized return và geometric mean** sang **Simpson's paradox: aggregated ratios có thể đảo conclusion**, vì cơ chế trước tạo đầu vào cho bước sau.

## Weighted average: denominator tells what is being averaged

Lớp (class / 클래스) A: 10 students average 80. lớp (class / 클래스) B: 30 students average 90.

Overall average:

```math
\frac{10(80)+30(90)}{40}=87.5.
```

Không phải 85.

Each group mean represents different number of observations. Weighted average reconstructs total numerator divided total denominator.

General:

```math
\bar x_w
=
\frac{\sum_iw_ix_i}{\sum_iw_i}.
```

Portfolio return, CPI baskets, grades, phân tán (distributed / 분산) metrics và expected values đều dùng weighted cấu trúc (structure / 구조).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Simpson's paradox: aggregated ratios có thể đảo conclusion** nối từ **Weighted average: denominator tells what is being averaged** sang **Rates và dimensional phân tích (analysis / 분석)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Simpson's paradox: aggregated ratios có thể đảo conclusion

Nếu success rates được aggregate across groups có different sizes/difficulty, overall ratio có thể reverse within-group trends.

Reason: weighted composition differs between groups. Ratio comparison without conditioning can hide confounding.

Đây là cầu nối (bridge / 브리지) từ elementary percentages sang statistics và lập luận nhân quả (causal reasoning / 인과적 추론).

> **Nối mạch:** Trong **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Rates và dimensional phân tích (analysis / 분석)** nối từ **Simpson's paradox: aggregated ratios có thể đảo conclusion** sang **Scaling law và ratio lập luận (reasoning / 추론)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Rates và dimensional phân tích (analysis / 분석)

Speed:

```math
60\frac{\text{km}}{\text{h}}.
```

Travel 2.5 h:

```math
60\frac{\text{km}}{\text{h}}
\times2.5\text{ h}
=150\text{ km}.
```

Units cancel như algebraic factors.

Currency exchange:

```math
100\text{ USD}
\times
\frac{1400\text{ KRW}}{1\text{ USD}}
=140000\text{ KRW}.
```

Writing units makes multiply/divide direction tường minh (explicit / 명시적).

> **Nối mạch:** Ở chặng này của **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Scaling law và ratio lập luận (reasoning / 추론)** nối từ **Rates và dimensional phân tích (analysis / 분석)** sang **AI and dữ liệu (data / 데이터) liên kết (connection / 연결) — normalization and rates**, vì cơ chế trước tạo đầu vào cho bước sau.

## Scaling law và ratio lập luận (reasoning / 추론)

Nếu similar shapes quy mô (scale / 규모) length by `k`, corresponding side ratios constant. Area scales `k^2`, volume `k^3`.

Thus elementary proportion becomes geometric scaling and dimensional phân tích (analysis / 분석).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Scaling law và ratio lập luận (reasoning / 추론)** đặt vấn đề; **AI and dữ liệu (data / 데이터) liên kết (connection / 연결) — normalization and rates** đối chiếu bằng chứng, rồi **Finance liên kết (connection / 연결) — nominal vs real thay đổi (change / 변경)** mở rộng hệ quả hoặc giới hạn liên quan.

## AI and dữ liệu (data / 데이터) liên kết (connection / 연결) — normalization and rates

Metrics like precision, recall, conversion tỷ lệ (rate / 비율), lỗi (error / 오류) tỷ lệ (rate / 비율) đều ratios. Their denominator defines meaning.

For example:

```math
precision
=
\frac{TP}{TP+FP},
```

```math
recall
=
\frac{TP}{TP+FN}.
```

Same numerator `TP`, different denominators → different questions.

Never compare percentages without checking denominator population.

> **Nối mạch:** Trong **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **AI and dữ liệu (data / 데이터) liên kết (connection / 연결) — normalization and rates** đặt vấn đề; **Finance liên kết (connection / 연결) — nominal vs real thay đổi (change / 변경)** đối chiếu bằng chứng, rồi **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** mở rộng hệ quả hoặc giới hạn liên quan.

## Finance liên kết (connection / 연결) — nominal vs real thay đổi (change / 변경)

If nominal wealth grows by `r_n` and prices by inflation `\pi`, chính xác (exact / 정확한) real growth factor is

```math
\frac{1+r_n}{1+\pi}.
```

So real return:

```math
r_{real}
=
\frac{1+r_n}{1+\pi}-1.
```

Approximation

```math
r_{real}\approx r_n-\pi
```

works only for small rates.

This is another example where multiplicative ratios are fundamental and additive shortcuts are approximations.

> **Nối mạch:** Ở chặng này của **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** nối từ **Finance liên kết (connection / 연결) — nominal vs real thay đổi (change / 변경)** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes

Ratios become unstable when denominator near zero. Percentage changes from very small bases can look huge. A 100% increase from 1 to 2 may be operationally tiny; ngữ cảnh (context / 맥락) and absolute magnitude still matter.

Average of ratios may differ from ratio of totals. Weighted aggregation must match desired denominator.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Ratio answers “how many times relative to a tham chiếu (reference / 참조)?” tỷ lệ (rate / 비율) adds units to that comparison. Percentage simply expresses a ratio on a base-100 quy mô (scale / 규모). Repeated percentages multiply, weighted averages reconstruct numerator/denominator cấu trúc (structure / 구조), and many statistical or financial errors come from forgetting which denominator defines the question.

> **Nối mạch:** Trong **Tỉ số, tỉ lệ, tỷ lệ (rate / 비율) và phần trăm: ngôn ngữ của so sánh tương đối**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

**“+10% and -10% cancel.”** They apply to different bases and combine multiplicatively.

**“2 percentage points = 2% increase.”** Not generally; percentage points measure absolute difference between percentages.

**“Average of averages is fine.”** Only when weights/groups are equal or specifically appropriate.

**“A huge percentage thay đổi (change / 변경) always means a huge practical thay đổi (change / 변경).”** Small denominators can create huge percentages.

**“Any straight line means direct proportionality.”** `y=kx+b` is proportional only when `b=0`.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
