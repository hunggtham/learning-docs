# Xác suất có điều kiện và định lý Bayes

Xác suất có điều kiện (Conditional probability / 조건부 확률) formalizes việc probability thay đổi khi ta biết thêm information.

## Conditional probability

Nếu `P(B)>0`:

```math
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
```

Khi biết B xảy ra, sample space hiệu dụng thu hẹp vào B. Ta hỏi phần của B cũng thuộc A.

Từ definition:

```math
P(A\cap B)=P(A\mid B)P(B)
```

và symmetric:

```math
P(A\cap B)=P(B\mid A)P(A)
```

## Bayes theorem

Equate hai expressions:

```math
P(A\mid B)P(B)=P(B\mid A)P(A)
```

nên

```math
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}
```

Bayes theorem đảo direction của conditioning bằng cách weight likelihood với prior.

## Medical-test example

Giả sử disease prevalence 1%:

```math
P(D)=0.01
```

Test sensitivity 99%:

```math
P(+\mid D)=0.99
```

false-positive rate 5%:

```math
P(+\mid D^c)=0.05
```

Total positive probability:

```math
P(+)=0.99(0.01)+0.05(0.99)=0.0594
```

Posterior probability disease given positive:

```math
P(D\mid +)=\frac{0.99\cdot0.01}{0.0594}\approx0.1667
```

Dù test “99% sensitive”, positive result không nghĩa 99% chance disease. Low base rate và false positives matter.

## Base-rate neglect

Con người thường chú ý `P(evidence|cause)` nhưng nhầm nó với `P(cause|evidence)`. Bayes theorem cho thấy prior/base rate là thành phần không thể bỏ.

Trong fraud detection, một classifier có high accuracy vẫn có thể tạo nhiều false positives nếu fraud extremely rare.

## Law of total probability

Nếu `B_1,...,B_n` partition sample space:

```math
P(A)=\sum_iP(A\mid B_i)P(B_i)
```

Bayes denominator thường tính bằng rule này.

## Odds form

Bayes có thể viết:

```math
\text{posterior odds}=\text{prior odds}\times\text{likelihood ratio}
```

Cách này làm update evidence theo multiplicative factors rõ ràng. Log-odds biến multiplications thành additions.

## Bayesian updating

Nếu observations conditionally independent given hypothesis, successive evidence updates có thể apply sequentially. Posterior sau evidence trước trở thành prior cho evidence tiếp theo.

Nhưng independence assumptions phải kiểm tra; double-count correlated evidence sẽ overstate certainty.

## Mental Model

> Conditional probability thu hẹp universe theo thông tin đã biết. Bayes theorem đổi câu hỏi từ “nếu hypothesis đúng thì evidence dễ xuất hiện đến đâu?” sang “sau khi thấy evidence, hypothesis đáng tin đến đâu?”, đồng thời bắt buộc tính base rate.

## Common Misconceptions

`P(A|B)` và `P(B|A)` không giống nhau. Sensitivity không phải positive predictive value. Bayes không tự tạo prior đúng; posterior vẫn phụ thuộc model, prior và likelihood assumptions.

## Worked Example: spam classifier và base rate

Giả sử 2% emails là spam. Classifier catches 95% spam và false-positive 1% ham.

```math
P(S)=0.02,
\quad P(+|S)=0.95,
\quad P(+|S^c)=0.01
```

Total flagged:

```math
P(+)=0.95(0.02)+0.01(0.98)=0.0288
```

Probability một flagged email thật sự spam:

```math
P(S|+)=\frac{0.95\cdot0.02}{0.0288}\approx0.66
```

Dù sensitivity 95% và false positive chỉ 1%, positive predictive value khoảng 66% vì spam base rate thấp.

## Likelihood khác probability của hypothesis

Trong Bayesian language, `P(data|θ)` là likelihood viewed as function of parameter `θ` cho fixed data. Nó không tự normalize thành probability distribution trên θ. Để có posterior cần prior:

```math
p(\theta|D)\propto p(D|\theta)p(\theta)
```

Phân biệt này quan trọng khi đọc ML/statistics literature.

## Practical checklist khi đọc một conditional probability

Luôn đọc cả hai phía của dấu `|`: event bên phải là information đã được condition. Sau đó hỏi base rate của hypothesis, false-positive/false-negative structure và liệu evidence pieces có thật sự conditionally independent hay không. Chỉ một thay đổi nhỏ ở denominator có thể đảo intuition.
