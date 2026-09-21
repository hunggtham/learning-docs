# Đo lường, đơn vị và ước lượng: từ con số đến quantity có ý nghĩa

Khi toán học chạm vào thế giới thật, một con số hiếm khi đủ. `5` có thể là 5 mét, 5 giây, 5%, 5 requests/s hoặc 5 triệu KRW. Những con số này nhìn giống nhau về mặt ký hiệu nhưng thuộc các loại quantity khác nhau, có cách cộng/trừ khác nhau, độ chính xác khác nhau và mức uncertainty khác nhau.

Vì vậy một measurement nên được nghĩ theo ba lớp:

```text
quantity = numerical value × unit
measurement = quantity + uncertainty
model input = measurement + assumptions
```

Đây là bridge từ arithmetic sang science, engineering, statistics và numerical computing.

## 1. Quantity và unit: unit giống như type information

Một đại lượng đo được (measured quantity / 측정량) thường có dạng

```math
Q=q\,[u]
```

trong đó `q` là numerical value và `[u]` là unit.

Ví dụ:

```text
3.2 km
```

không chỉ là number `3.2`; nó là một length.

Đổi unit:

```math
3.2\,km\times\frac{1000\,m}{1\,km}=3200\,m.
```

Conversion factor về physical meaning bằng 1, nên quantity không đổi, chỉ representation đổi.

Mental model hữu ích trong programming là **unit ≈ type**. `5 m + 3 m` hợp lý, còn `5 m + 3 s` không hợp lý vì hai quantities khác loại. Những thư viện units-of-measure trong software cố encode chính rule này vào type system.

## 2. Dimension khác unit

**Thứ nguyên (dimension / 차원)** nói quantity thuộc loại cơ bản nào; **đơn vị (unit / 단위)** nói ta đo loại đó bằng thang nào.

Ví dụ meter và kilometer là hai units của cùng dimension length `[L]`.

Một số base dimensions thường dùng:

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

## 3. Dimensional consistency là type checker, không phải proof

Một physical equation phải có dimensions compatible ở hai vế.

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

không hợp lệ vì velocity và time không thể cộng trực tiếp.

Tuy nhiên dimensional consistency chỉ là **necessary condition**, không phải sufficient condition. Cả

```math
d=vt
```

và

```math
d=2vt
```

đều đúng dimension, nhưng coefficient 2 cần reasoning/evidence khác.

Đây là một pattern quan trọng trong toán ứng dụng:

> Một constraint có thể loại bỏ nhiều answer sai mà chưa đủ để xác định answer đúng.

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

Dimensionless groups thường cho phép so sánh systems khác scale. Đây là trực giác phía sau dimensional similarity trong physics/engineering và nhiều normalized metrics trong data science.

Ta không cần formal Buckingham π theorem ở đây, nhưng nên nhớ idea: nếu model thực sự chỉ phụ thuộc vào một số independent dimensions, có thể tồn tại representation compact hơn bằng dimensionless combinations.

## 5. Precision, accuracy và uncertainty không giống nhau

**Precision** nói measurements lặp lại có gần nhau không hoặc representation có bao nhiêu resolution.

**Accuracy** nói estimate có gần true value không.

Một sensor có thể rất precise nhưng biased: luôn cho `10.00`, `10.01`, `9.99` trong khi true value là `11.2`.

Ngược lại, measurements có thể noisy nhưng average lại gần true value.

Điều này quan trọng trong ML/Statistics:

```text
low variance ≠ low bias
precision ≠ accuracy
```

## 6. Significant figures và false precision

Chữ số có nghĩa (significant figures / 유효숫자) biểu thị mức resolution/precision hợp lý của measurement.

Nếu length được đo là

```text
12.3 cm
```

calculator không thể biến nó thành knowledge chính xác ở mức

```text
12.300000000 cm
```

chỉ bằng arithmetic.

Giả sử area của square side `12.3 cm`:

```math
A=12.3^2=151.29\,cm^2.
```

Con số `151.29` là computational output, nhưng reporting có thể chỉ nên giữ precision tương thích với measurement ban đầu.

Đây là distinction:

```text
computational precision
≠ information precision
```

## 7. Absolute error và relative error trả lời hai câu hỏi khác nhau

Cho true value `x` và approximation `\hat x`.

Absolute error:

```math
E_{abs}=|x-\hat x|.
```

Relative error:

```math
E_{rel}=\frac{|x-\hat x|}{|x|},\qquad x\ne0.
```

Absolute error trả lời “sai bao nhiêu unit?”. Relative error trả lời “sai lớn đến đâu so với scale của quantity?”.

Ví dụ error `1 cm`:

- object 2 cm → 50% error;
- bridge 2 km → gần như negligible.

Khi `x` gần 0, relative error có thể explode và trở nên không ổn định; lúc đó absolute tolerance hoặc problem-specific scale có thể phù hợp hơn.

## 8. Percentage, percentage point và denominator reasoning

Nếu rate tăng từ 3% lên 4%:

```text
increase = 1 percentage point
```

nhưng relative increase là

```math
\frac{4-3}{3}\approx33.3\%.
```

Hai câu không mâu thuẫn; denominator khác nhau.

Percentage luôn ngầm hỏi:

> Phần trăm của base nào?

Đây là lý do percentage change thường asymmetric. Tăng từ 80 lên 100 là 25%, nhưng giảm từ 100 về 80 là 20%.

## 9. Propagation of uncertainty: output không thể chính xác hơn inputs một cách kỳ diệu

Nếu output

```math
y=f(x_1,\ldots,x_n),
```

small input perturbations có first-order approximation:

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

Đây là connection trực tiếp từ measurement sang multivariable calculus và statistics.

### Worked example: area của rectangle

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

Vì vậy relative uncertainty của product gần bằng tổng relative sensitivities ở first order.

## 10. Order of magnitude là reasoning về scale

Scientific notation:

```math
3.2\times10^6
```

làm scale rõ hơn `3,200,000`.

Order of magnitude không hỏi exact value mà hỏi size regime.

Nếu system A cần `10^3` operations và B cần `10^9`, khác biệt sáu orders of magnitude. Micro-optimization 20% không thể bù chênh lệch factor một triệu.

Đây là lý do order-of-magnitude reasoning cực kỳ hữu ích trong system design và algorithm analysis.

## 11. Fermi estimation: decomposition quan trọng hơn decimal precision

Một Fermi estimate phân rã unknown lớn thành product/sum của quantities dễ estimate.

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

Peak factor, retries và burstiness là assumptions tiếp theo.

## 12. Sanity check bằng upper/lower bounds

Ước lượng tốt nên có bounds thô.

Nếu business có tối đa 1 triệu users, mỗi user không thể tạo hơn 1000 requests/ngày theo product constraints, thì upper bound rough là:

```math
10^6\times10^3=10^9\ requests/day.
```

Nếu một dashboard báo `10^13 requests/day`, trước khi debug code phức tạp ta nên hỏi liệu con số đã vi phạm sanity bound hay unit conversion không.

Bounding là một trong những kỹ thuật reasoning rẻ nhưng mạnh nhất.

## 13. Linear scale vs logarithmic scale

Linear scale bảo toàn differences; log scale bảo toàn ratios.

Trên log10 axis:

```text
1, 10, 100, 1000
```

cách đều vì mỗi step nhân 10.

Log scale hữu ích khi data trải nhiều orders of magnitude: latency tail, wealth distribution, frequency spectrum, pH, decibel, learning curves.

Nhưng log transform thay meaning: difference trên log scale tương ứng ratio trên original scale.

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

loss thường dimensionless hoặc phụ thuộc target scaling; gradient có units output-loss per parameter-unit. Feature scaling thay numerical geometry và do đó ảnh hưởng optimization.

Unit reasoning không chỉ dành cho physics.

## 15. Worked example: phát hiện unit bug

Giả sử travel time được tính bằng:

```text
distance = 120 km
speed = 60 m/s
```

Nếu code làm trực tiếp:

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

Unit algebra tự chỉ ra phép conversion cần thiết.

## 16. Assumptions checklist khi đọc một con số

Trước một metric hoặc estimate, hỏi:

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

## Knowledge Connection

Measurement nối trực tiếp với:

```text
units → dimensional analysis
uncertainty → probability/statistics
sensitivity → derivatives/Jacobian
error propagation → covariance
scale → logarithm/power law
Fermi estimate → modeling/system design
precision → numerical analysis/floating point
```

Trong engineering và data science, nhiều lỗi lớn không đến từ calculus khó mà từ unit mismatch, denominator sai, false precision hoặc assumption scale sai.

## Mental Model

> Một measurement không phải “một number lấy từ thế giới”. Nó là quantity được biểu diễn trong một unit, với finite precision và uncertainty. Good quantitative reasoning luôn giữ bốn lớp cùng lúc: **value, unit, uncertainty, scale**.

## Common Misconceptions

Nhiều decimal places không đồng nghĩa accurate. Dimensionally correct không đồng nghĩa physically correct. Relative error không ổn khi reference gần zero. Log scale không “bóp méo dữ liệu” một cách tùy tiện; nó đổi câu hỏi từ additive difference sang multiplicative ratio. Một estimate thô có assumptions rõ thường hữu ích hơn một con số rất chính xác nhưng không biết denominator, unit hoặc uncertainty.