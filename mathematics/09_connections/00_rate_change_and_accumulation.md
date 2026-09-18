# Knowledge Connection — Rate, Change và Accumulation

Một trong những patterns quan trọng nhất xuyên suốt toán, khoa học và engineering là cặp **rate of change ↔ accumulation**. Nhiều thuật ngữ khác nhau thực chất là các biến thể của cùng mental model.

## Difference: thay đổi hữu hạn

Nếu quantity từ `x_1` thành `x_2`, change:

```math
\Delta x=x_2-x_1
```

Nếu muốn rate trung bình so với time:

```math
\frac{\Delta x}{\Delta t}
```

Đây là finite difference.

Trong database metrics, requests tăng từ 1000 lên 1200 trong 10 phút cho average increase 20 requests/minute. Nhưng average không nói path giữa hai endpoints.

## Derivative: local rate

Khi interval thu nhỏ bằng limit:

```math
\frac{dx}{dt}=\lim_{\Delta t\to0}\frac{\Delta x}{\Delta t}
```

Ta có instantaneous rate.

Trong physics:

```math
v=\frac{dx}{dt},\qquad a=\frac{dv}{dt}
```

Trong economics, marginal cost `C'(q)` là local cost change theo quantity. Trong ML, gradient là vector local rates theo parameters.

## Accumulation: cộng contributions

Nếu rate constant `r`, accumulated amount trên time `T` là `rT`. Nếu rate thay đổi:

```math
\text{total}=\int r(t)dt
```

Trong physics, integrate velocity để lấy displacement. Trong finance, accumulate continuously varying cash-flow rate. Trong probability, integrate density để lấy probability mass.

## Fundamental theorem as inverse relationship

Nếu accumulation

```math
A(x)=\int_a^x f(t)dt
```

thì

```math
A'(x)=f(x)
```

Rate của accumulated total chính là local contribution rate. Ngược lại integrate derivative reconstruct net change:

```math
f(b)-f(a)=\int_a^b f'(x)dx
```

## Discrete analogue

Difference và summation là discrete counterparts.

Nếu

```math
\Delta a_n=a_{n+1}-a_n
```

thì telescoping sum:

```math
\sum_{n=m}^{N-1}\Delta a_n=a_N-a_m
```

Đây là discrete fundamental theorem: summing local increments gives global change.

Version control commits cũng có mental analogy: mỗi diff là local change; applying sequence of diffs reconstructs new state.

## Gradient and optimization

Gradient components là partial rates:

```math
\nabla L=\left[\frac{\partial L}{\partial\theta_1},\ldots\right]
```

Update accumulates many small parameter changes over iterations. Training trajectory là result của integrating/iterating local update rules.

## Differential equations

Nếu biết rate law:

```math
x'=F(x,t)
```

solving ODE reconstructs state trajectory. Đây là same rate→accumulation idea nhưng rate itself depends on state.

## Mental Model

> “Change” có hai scales. Difference hỏi thay đổi trên một khoảng hữu hạn; derivative zoom vào rate local. Sum/integral làm chiều ngược lại: cộng các local changes để reconstruct total. Khi gặp một domain mới, hãy tìm cặp rate và accumulated state của nó.

## Một bảng nhận diện cùng mental model

| Domain | State / accumulated quantity | Local rate |
|---|---|---|
| Vật lý | Position `x(t)` | Velocity `dx/dt` |
| Vật lý | Velocity `v(t)` | Acceleration `dv/dt` |
| Finance | Account balance | Interest/cash-flow rate |
| Data systems | Stored bytes | Ingestion throughput |
| Probability | CDF `F(x)` | Density `f(x)` |
| Economics | Total cost `C(q)` | Marginal cost `C'(q)` |
| ML | Loss value | Gradient w.r.t. parameters |

Bảng không nói các domains giống hệt nhau; nó cho pattern để đặt câu hỏi đúng. Nếu có accumulated state, hỏi derivative/rate của nó. Nếu có rate/density, hỏi integral/sum tạo total nào.

## Khi continuous model không phù hợp

Transactions, packets và people là discrete counts. Có thể dùng differences và sums thay derivatives/integrals. Continuous calculus đôi khi vẫn là useful approximation khi scale lớn, nhưng cần biết mình đã smooth discrete process. Đây là một recurring modeling choice: exact discrete structure vs continuous approximation dễ phân tích hơn.

## Common Misconceptions

Rate không phải total: velocity và displacement có units khác nhau; marginal cost và total cost cũng vậy. Derivative nhỏ tại một point không nói accumulated change trên interval nhỏ nếu interval lớn hoặc rate thay đổi mạnh. Integral của một rate có dấu có thể cancel, nên total geometric amount đôi khi cần absolute value hoặc một quantity khác.

