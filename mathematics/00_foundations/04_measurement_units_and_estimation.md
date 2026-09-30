# Đo lường, đơn vị và ước lượng: từ con số đến quantity có ý nghĩa

> **Mạch đọc:** Đọc **Đo lường, đơn vị và ước lượng: từ con số đến quantity có ý nghĩa** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Quantity và đơn vị (unit / 단위): đơn vị (unit / 단위) giống như kiểu (type / 타입) thông tin (information / 정보)** sang **2. Dimension khác đơn vị (unit / 단위)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi toán học chạm vào thế giới thật, một con số hiếm khi đủ. `5` có thể là 5 mét, 5 giây, 5%, 5 requests/s hoặc 5 triệu KRW. Những con số này nhìn giống nhau về mặt ký hiệu nhưng thuộc các loại quantity khác nhau, có cách cộng/trừ khác nhau, độ chính xác khác nhau và mức bất định (uncertainty / 불확실성) khác nhau.

Vì vậy một đo lường (measurement / 측정) nên được nghĩ theo ba lớp:

```text
quantity = numerical value × unit
measurement = quantity + uncertainty
model input = measurement + assumptions
```

Đây là cầu nối (bridge / 브리지) từ arithmetic sang science, kỹ thuật (engineering / 엔지니어링), statistics và numerical computing.

## 1. Quantity và đơn vị (unit / 단위): đơn vị (unit / 단위) giống như kiểu (type / 타입) thông tin (information / 정보)

Một đại lượng đo được (measured quantity / 측정량) thường có dạng

```math
Q=q\,[u]
```

trong đó `q` là numerical giá trị (value / 값) và `[u]` là đơn vị (unit / 단위).

Ví dụ:

```text
3.2 km
```

không chỉ là number `3.2`; nó là một length.

Đổi đơn vị (unit / 단위):

```math
3.2\,km\times\frac{1000\,m}{1\,km}=3200\,m.
```

Conversion factor về vật lý (physical / 물리적) meaning bằng 1, nên quantity không đổi, chỉ biểu diễn (representation / 표현) đổi.

Mô hình tư duy (mental model / 사고 모델) hữu ích trong programming là **đơn vị (unit / 단위) ≈ kiểu (type / 타입)**. `5 m + 3 m` hợp lý, còn `5 m + 3 s` không hợp lý vì hai quantities khác loại. Những thư viện units-of-measure trong software cố encode chính quy tắc (rule / 규칙) này vào hệ kiểu (type system / 타입 시스템).

## 2. Dimension khác đơn vị (unit / 단위)

**Thứ nguyên (dimension / 차원)** nói quantity thuộc loại cơ bản nào; **đơn vị (unit / 단위)** nói ta đo loại đó bằng thang nào.

Ví dụ meter và kilometer là hai units của cùng dimension length `[L]`.

Một số cơ sở (base / 기반) dimensions thường dùng:

```text
length   [L]
mass     [M]
time     [T]
current  [I]
temperature [Θ]
```

Derived dimensions được tạo bằng multiplication/division.

Velocity:

```math
[v]=LT^{-1}
```

Acceleration:

```math
[a]=LT^{-2}
```

Force:

```math
[F]=MLT^{-2}.
```

## 3. Dimensional consistency là kiểu (type / 타입) checker, không phải proof

Một vật lý (physical / 물리적) equation phải có dimensions compatible ở hai vế.

Ví dụ:

```math
d=vt
```

vì

```math
[L]=[L][T]^{-1}[T].
```

Còn

```math
d=v+t
```

không hợp lệ vì velocity và thời gian (time / 시간) không thể cộng trực tiếp.

Tuy nhiên dimensional consistency chỉ là **necessary điều kiện (condition / 조건)**, không phải sufficient điều kiện (condition / 조건). Cả

```math
d=vt
```

và

```math
d=2vt
```

đều đúng dimension, nhưng coefficient 2 cần lập luận (reasoning / 추론)/bằng chứng (evidence / 증거) khác.

Đây là một mẫu (pattern / 패턴) quan trọng trong toán ứng dụng:

> Một ràng buộc (constraint / 제약조건) có thể loại bỏ nhiều answer sai mà chưa đủ để xác định answer đúng.

## 4. Buckingham-π intuition: vì sao dimensionless groups quan trọng?

Một đại lượng không thứ nguyên (dimensionless quantity / 무차원량) xuất hiện khi units triệt tiêu.

Ví dụ:

```math
\text{strain}=\frac{\Delta L}{L}
```

```math
\text{probability}=\frac{\text{favorable mass}}{\text{total mass}}
```

```math
\text{relative error}=\frac{|x-\hat x|}{|x|}.
```

Dimensionless groups thường cho phép so sánh các hệ thống (systems / 시스템들) khác quy mô (scale / 규모). Đây là trực giác phía sau dimensional similarity trong physics/kỹ thuật (engineering / 엔지니어링) và nhiều normalized metrics trong dữ liệu (data / 데이터) science.

Ta không cần formal Buckingham π theorem ở đây, nhưng nên nhớ idea: nếu mô hình (model / 모델) thực sự chỉ phụ thuộc vào một số independent dimensions, có thể tồn tại biểu diễn (representation / 표현) compact hơn bằng dimensionless combinations.

## 5. Precision, accuracy và bất định (uncertainty / 불확실성) không giống nhau

**Precision** nói measurements lặp lại có gần nhau không hoặc biểu diễn (representation / 표현) có bao nhiêu resolution.

**Accuracy** nói estimate có gần true giá trị (value / 값) không.

Một sensor có thể rất precise nhưng biased: luôn cho `10.00`, `10.01`, `9.99` trong khi true giá trị (value / 값) là `11.2`.

Ngược lại, measurements có thể noisy nhưng average lại gần true giá trị (value / 값).

Điều này quan trọng trong ML/Statistics:

```text
low variance ≠ low bias
precision ≠ accuracy
```

## 6. Significant figures và false precision

Chữ số có nghĩa (significant figures / 유효숫자) biểu thị mức resolution/precision hợp lý của đo lường (measurement / 측정).

Nếu length được đo là

```text
12.3 cm
```

calculator không thể biến nó thành kiến thức (knowledge / 지식) chính xác ở mức

```text
12.300000000 cm
```

chỉ bằng arithmetic.

Giả sử area của square side `12.3 cm`:

```math
A=12.3^2=151.29\,cm^2.
```

Con số `151.29` là computational đầu ra (output / 출력), nhưng reporting có thể chỉ nên giữ precision tương thích với đo lường (measurement / 측정) ban đầu.

Đây là distinction:

```text
computational precision
≠ information precision
```

## 7. Absolute lỗi (error / 오류) và relative lỗi (error / 오류) trả lời hai câu hỏi khác nhau

Cho true giá trị (value / 값) `x` và approximation `\hat x`.

Absolute lỗi (error / 오류):

```math
E_{abs}=|x-\hat x|.
```

Relative lỗi (error / 오류):

```math
E_{rel}=\frac{|x-\hat x|}{|x|},\qquad x\ne0.
```

Absolute lỗi (error / 오류) trả lời “sai bao nhiêu đơn vị (unit / 단위)?”. Relative lỗi (error / 오류) trả lời “sai lớn đến đâu so với quy mô (scale / 규모) của quantity?”.

Ví dụ lỗi (error / 오류) `1 cm`:

- đối tượng (object / 객체) 2 cm → 50% lỗi (error / 오류);
- cầu nối (bridge / 브리지) 2 km → gần như negligible.

Khi `x` gần 0, relative lỗi (error / 오류) có thể explode và trở nên không ổn định; lúc đó absolute tolerance hoặc problem-specific quy mô (scale / 규모) có thể phù hợp hơn.

## 8. Percentage, percentage điểm (point / 지점) và denominator lập luận (reasoning / 추론)

Nếu tỷ lệ (rate / 비율) tăng từ 3% lên 4%:

```text
increase = 1 percentage point
```

nhưng relative increase là

```math
\frac{4-3}{3}\approx33.3\%.
```

Hai câu không mâu thuẫn; denominator khác nhau.

Percentage luôn ngầm hỏi:

> Phần trăm của cơ sở (base / 기반) nào?

Đây là lý do percentage thay đổi (change / 변경) thường asymmetric. Tăng từ 80 lên 100 là 25%, nhưng giảm từ 100 về 80 là 20%.

## 9. Propagation of bất định (uncertainty / 불확실성): đầu ra (output / 출력) không thể chính xác hơn inputs một cách kỳ diệu

Nếu đầu ra (output / 출력)

```math
y=f(x_1,\ldots,x_n),
```

small đầu vào (input / 입력) perturbations có first-order approximation:

```math
\Delta y\approx
\sum_i\frac{\partial f}{\partial x_i}\Delta x_i.
```

Các partial derivatives đo sensitivity.

Nếu errors ngẫu nhiên, độc lập và small, variance propagation thường dùng approximation:

```math
\operatorname{Var}(y)
\approx
\sum_i
\left(\frac{\partial f}{\partial x_i}\right)^2
\operatorname{Var}(x_i).
```

Đây là liên kết (connection / 연결) trực tiếp từ đo lường (measurement / 측정) sang multivariable calculus và statistics.

### Worked example: area của rectangle

Ví dụ này cho thấy cách chọn đơn vị, ghi precision và truyền uncertainty qua một phép tính đơn giản. Hãy theo từng bước để thấy measurement không chỉ là thay số vào công thức.

```math
A=LW.
```

First-order differential:

```math
dA=W\,dL+L\,dW.
```

Chia cho `A=LW`:

```math
\frac{dA}{A}
\approx
\frac{dL}{L}+\frac{dW}{W}.
```

Vì vậy relative bất định (uncertainty / 불확실성) của sản phẩm (product / 제품) gần bằng tổng relative sensitivities ở first thứ tự (order / 순서).

## 10. thứ tự (order / 순서) of magnitude là lập luận (reasoning / 추론) về quy mô (scale / 규모)

Scientific notation:

```math
3.2\times10^6
```

làm quy mô (scale / 규모) rõ hơn `3,200,000`.

Thứ tự (order / 순서) of magnitude không hỏi chính xác (exact / 정확한) giá trị (value / 값) mà hỏi kích thước (size / 크기) regime.

Nếu hệ thống (system / 시스템) A cần `10^3` operations và B cần `10^9`, khác biệt sáu orders of magnitude. Micro-optimization 20% không thể bù chênh lệch factor một triệu.

Đây là lý do order-of-magnitude lập luận (reasoning / 추론) cực kỳ hữu ích trong hệ thống (system / 시스템) thiết kế (design / 설계) và thuật toán (algorithm / 알고리즘) phân tích (analysis / 분석).

## 11. Fermi estimation: decomposition quan trọng hơn decimal precision

Một Fermi estimate phân rã unknown lớn thành sản phẩm (product / 제품)/sum của quantities dễ estimate.

Ví dụ rough traffic:

```text
users
× sessions/user/day
× requests/session
÷ seconds/day
```

Giả sử:

```text
100,000 users
× 2 sessions/day
× 30 requests/session
= 6,000,000 requests/day
```

Average:

```math
\frac{6,000,000}{86,400}\approx69.4\ requests/s.
```

Câu trả lời quan trọng đầu tiên không phải `69.444...`, mà là:

```text
order of magnitude ≈ 10^2 requests/s average
```

Peak factor, retries và burstiness là các giả định (assumptions / 가정들) tiếp theo.

## 12. Sanity check bằng upper/lower bounds

Ước lượng tốt nên có bounds thô.

Nếu nghiệp vụ (business / 비즈니스) có tối đa 1 triệu users, mỗi người dùng (user / 사용자) không thể tạo hơn 1000 requests/ngày theo sản phẩm (product / 제품) các ràng buộc (constraints / 제약조건들), thì upper bound rough là:

```math
10^6\times10^3=10^9\ requests/day.
```

Nếu một dashboard báo `10^13 requests/day`, trước khi gỡ lỗi (debug / 디버그) mã (code / 코드) phức tạp ta nên hỏi liệu con số đã vi phạm sanity bound hay đơn vị (unit / 단위) conversion không.

Bounding là một trong những kỹ thuật lập luận (reasoning / 추론) rẻ nhưng mạnh nhất.

## 13. tuyến tính (linear / 선형) quy mô (scale / 규모) vs logarithmic quy mô (scale / 규모)

Tuyến tính (linear / 선형) quy mô (scale / 규모) bảo toàn differences; log quy mô (scale / 규모) bảo toàn ratios.

Trên log10 axis:

```text
1, 10, 100, 1000
```

cách đều vì mỗi step nhân 10.

Log quy mô (scale / 규모) hữu ích khi dữ liệu (data / 데이터) trải nhiều orders of magnitude: độ trễ (latency / 지연 시간) tail, wealth phân phối (distribution / 분포), frequency spectrum, pH, decibel, học tập (learning / 학습) curves.

Nhưng log transform thay meaning: difference trên log quy mô (scale / 규모) tương ứng ratio trên original quy mô (scale / 규모).

## 14. Units trong Finance, CS và AI

Trong Finance:

```text
return → dimensionless ratio
volatility → return per sqrt(time) theo convention/model
interest rate → 1/time-ish scale trong continuous model
```

Trong CS:

```text
latency → ms/request
throughput → requests/s
bandwidth → bits/s
storage → bytes
```

Trong AI:

Mất mát (loss / 손실) thường dimensionless hoặc phụ thuộc mục tiêu (target / 대상) scaling; độ dốc (gradient / 기울기) có units output-loss per parameter-unit. tính năng (feature / 기능) scaling thay numerical hình học (geometry / 기하학) và do đó ảnh hưởng tối ưu hóa (optimization / 최적화).

Đơn vị (unit / 단위) lập luận (reasoning / 추론) không chỉ dành cho physics.

## 15. Worked example: phát hiện đơn vị (unit / 단위) bug

Giả sử travel thời gian (time / 시간) được tính bằng:

```text
distance = 120 km
speed = 60 m/s
```

Nếu mã (code / 코드) làm trực tiếp:

```math
t=120/60=2
```

con số `2` vô nghĩa vì units chưa align.

Convert:

```math
120\,km=120000\,m
```

nên

```math
t=\frac{120000\,m}{60\,m/s}=2000\,s\approx33.3\,min.
```

Đơn vị (unit / 단위) algebra tự chỉ ra phép conversion cần thiết.

## 16. các giả định (assumptions / 가정들) checklist khi đọc một con số

Trước một chỉ số (metric / 지표) hoặc estimate, hỏi:

```text
Quantity nào đang được đo?
Unit là gì?
Reference/base là gì?
Precision thực sự đến đâu?
Uncertainty đến từ đâu?
Data có systematic bias không?
Scale linear hay multiplicative?
Có sanity bound nào không?
```

Đây là mathematical hygiene, không phải paperwork.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Đo lường (measurement / 측정) nối trực tiếp với:

```text
units → dimensional analysis
uncertainty → probability/statistics
sensitivity → derivatives/Jacobian
error propagation → covariance
scale → logarithm/power law
Fermi estimate → modeling/system design
precision → numerical analysis/floating point
```

Trong kỹ thuật (engineering / 엔지니어링) và dữ liệu (data / 데이터) science, nhiều lỗi lớn không đến từ calculus khó mà từ đơn vị (unit / 단위) mismatch, denominator sai, false precision hoặc giả định (assumption / 가정) quy mô (scale / 규모) sai.

## Mô hình tư duy (mental model / 사고 모델)

> Một đo lường (measurement / 측정) không phải “một number lấy từ thế giới”. Nó là quantity được biểu diễn trong một đơn vị (unit / 단위), với finite precision và bất định (uncertainty / 불확실성). Good quantitative lập luận (reasoning / 추론) luôn giữ bốn lớp cùng lúc: **giá trị (value / 값), đơn vị (unit / 단위), bất định (uncertainty / 불확실성), quy mô (scale / 규모)**.

## Dùng chung (common / 공통) Misconceptions

Nhiều decimal places không đồng nghĩa accurate. Dimensionally correct không đồng nghĩa physically correct. Relative error không ổn khi reference gần zero. Log scale không “bóp méo dữ liệu” một cách tùy tiện; nó đổi câu hỏi từ additive difference sang multiplicative ratio. Một estimate thô có assumptions rõ thường hữu ích hơn một con số rất chính xác nhưng không biết denominator, unit hoặc uncertainty.
