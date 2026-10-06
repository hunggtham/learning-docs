# Dynamical systems, bifurcations và chaos: khi quy luật đơn giản tạo hành vi phức tạp

> **Mạch đọc:** Chapter này đi sau [Differential equations](./05_differential_equations.md) và [Sequences, recurrence](../02_functions/03_sequences_series_and_recurrence.md). ODE chapter đã giới thiệu equilibrium, phase line, phase plane, linearization và stability. Ở đây ta đi thêm một bước: **system thay đổi qualitative behavior thế nào khi parameter đổi, và deterministic system có thể trở nên khó dự đoán ra sao?**

Một dynamical system không nhất thiết phức tạp vì equation phức tạp. Một rule rất ngắn có thể tạo long-run behavior giàu structure.

Ví dụ discrete map:

```math
x_{n+1}=rx_n(1-x_n).
```

Chỉ một quadratic function, nhưng khi parameter `r` thay đổi, system đi qua:

```text
stable fixed point
→ oscillation
→ period doubling
→ chaos
```

Điều này phá intuition rằng “simple formula ⇒ simple behavior”.

---

## 1. Dynamical system = state + evolution rule

Một system cần hai thứ:

```text
state space
+
evolution rule
```

Discrete time:

```math
x_{n+1}=F(x_n).
```

Continuous time:

```math
\dot x=F(x).
```

State có thể là scalar, vector, population distribution, angle, matrix hoặc point trên manifold.

Câu hỏi chính thường không phải “solve formula exactly” mà là:

- trajectories đi đâu?
- equilibria nào stable?
- có cycle không?
- behavior đổi ra sao khi parameter đổi?
- long-run behavior có predictable không?

Đây là **qualitative analysis**.

---

## 2. Orbit và iteration

Với discrete map `F`, bắt đầu từ `x_0`:

```math
x_1=F(x_0),
```

```math
x_2=F(F(x_0))=F^2(x_0),
```

và general:

```math
x_n=F^n(x_0).
```

Sequence

```math
x_0,x_1,x_2,\ldots
```

là **orbit (궤도)**.

Đừng nhầm `F^n` với numeric power `[F(x)]^n`; ở đây là function composition `n` lần.

---

## 3. Fixed point và local stability trong discrete time

Fixed point `x*` thỏa:

```math
F(x^*)=x^*.
```

Perturb:

```math
x_n=x^*+\delta_n.
```

Linearize:

```math
\delta_{n+1}
\approx F'(x^*)\delta_n.
```

Do đó:

```math
\delta_n
\approx [F'(x^*)]^n\delta_0.
```

Nếu

```math
|F'(x^*)|<1,
```

perturbations shrink: fixed point locally stable.

Nếu

```math
|F'(x^*)|>1,
```

perturbations grow: unstable.

Compare continuous-time condition where sign of real part eigenvalue matters.

Discrete and continuous systems có stability rules tương tự nhưng không identical.

---

## 4. Logistic map

Logistic map:

```math
x_{n+1}=rx_n(1-x_n),
```

thường xét `0≤x≤1`.

Fixed points solve:

```math
x=rx(1-x).
```

Một fixed point:

```math
x^*=0.
```

Nếu `r≠0`, fixed point khác:

```math
x^*=1-\frac1r.
```

Derivative:

```math
F'(x)=r(1-2x).
```

Stability của each fixed point phụ thuộc `r`.

Chỉ việc thay parameter đã có thể đổi qualitative long-run behavior.

---

## 5. Parameter không chỉ đổi number, nó có thể đổi topology của behavior

Trong ordinary formula, đổi parameter thường chỉ làm output lớn/nhỏ hơn.

Trong dynamical system, parameter có thể làm:

```text
one stable equilibrium
→ two equilibria
→ stable cycle
→ unstable cycle
→ chaotic attractor
```

Sự thay đổi qualitative này gọi là **bifurcation (phân nhánh / 분기)**.

Bifurcation analysis hỏi:

> Khi parameter đi qua critical value, structure của phase portrait/orbits đổi thế nào?

---

## 6. Saddle-node bifurcation

Canonical continuous-time form:

```math
\dot x=\mu-x^2.
```

Equilibria solve:

```math
\mu-x^2=0.
```

Nếu `μ<0`: không có real equilibrium.

Nếu `μ=0`: một degenerate equilibrium.

Nếu `μ>0`: hai equilibria:

```math
x=\pm\sqrt\mu.
```

Một pair equilibria được “sinh ra” khi parameter cross threshold.

Đây là saddle-node bifurcation.

---

## 7. Transcritical bifurcation

Canonical form:

```math
\dot x=\mu x-x^2.
```

Equilibria:

```math
x=0,
\qquad
x=\mu.
```

Hai branches tồn tại cả trước/sau critical point nhưng exchange stability tại `μ=0`.

Pattern này xuất hiện khi two competing states cross role.

---

## 8. Pitchfork bifurcation và symmetry

Canonical supercritical pitchfork:

```math
\dot x=\mu x-x^3.
```

System symmetric under:

```math
x\mapsto -x.
```

Khi `μ<0`, origin stable.

Khi `μ>0`, origin unstable và two new stable symmetric equilibria xuất hiện:

```math
x=\pm\sqrt\mu.
```

Bifurcation structure phản ánh symmetry của equation.

Đây là bridge với group/symmetry ideas: symmetry constraints giới hạn kiểu branch nào có thể xuất hiện.

---

## 9. Hopf bifurcation: equilibrium sinh oscillation

Trong continuous systems dimension ≥2, một equilibrium có thể mất stability và stable periodic orbit xuất hiện.

High-level signature: complex-conjugate eigenvalues của Jacobian cross imaginary axis khi parameter thay đổi.

Schematic:

```text
stable equilibrium
   ↓ parameter crosses threshold
small oscillation appears
   ↓
stable limit cycle
```

Hopf bifurcation là mathematical model quan trọng cho onset of oscillation trong circuits, biology, chemistry và control systems.

---

## 10. Limit cycle

Một **limit cycle (극한주기)** là isolated closed trajectory mà nearby trajectories approach hoặc move away from.

Khác simple harmonic oscillator:

- ideal linear oscillator có continuum of closed orbits depending energy;
- nonlinear self-sustained oscillator có thể có one attracting periodic orbit.

Van der Pol oscillator là classic example:

```math
x''-\mu(1-x^2)x'+x=0.
```

Nonlinear damping có thể inject energy khi amplitude nhỏ và dissipate khi amplitude lớn, tạo stable cycle.

---

## 11. Bifurcation diagram

Với logistic map, thay vì plot trajectory theo time cho một `r`, ta có thể:

1. choose many `r` values;
2. iterate long enough bỏ transient;
3. plot long-run `x_n` values against `r`.

Ta thu được **bifurcation diagram (분기도)**.

Diagram cho thấy:

```text
single branch
→ two branches
→ four
→ eight
→ dense chaotic regions
```

Đây là visualization của qualitative state transitions.

---

## 12. Period doubling

Một stable fixed point có thể mất stability và stable period-2 orbit xuất hiện.

Sau đó period-2 mất stability → period-4.

Pattern tiếp tục:

```text
1 → 2 → 4 → 8 → 16 → ...
```

trước khi chaos xuất hiện.

Điều remarkable là ratios giữa parameter intervals approach universal Feigenbaum constants trong large class of maps.

Universal structure xuất hiện từ many different nonlinear systems.

---

## 13. Chaos không có nghĩa “pure randomness”

Một deterministic system có thể chaotic.

Rule hoàn toàn deterministic:

```math
x_{n+1}=F(x_n)
```

nhưng long-run prediction khó vì small initial errors grow rapidly.

Chaos thường gắn với:

- deterministic evolution;
- sensitivity to initial conditions;
- mixing/complex orbit structure;
- positive Lyapunov exponent trong relevant direction;
- topological complexity.

Randomness đến từ stochastic rule; chaos có thể xuất hiện không cần random input.

---

## 14. Sensitivity to initial conditions

Hai nearby initial states:

```math
|x_0-y_0|=\varepsilon
```

có thể separate roughly:

```math
|x_n-y_n|
\approx
\varepsilon e^{\lambda n}
```

trong regime với positive **Lyapunov exponent (리아푸노프 지수)** `λ`.

Nếu `λ>0`, errors grow exponentially on average.

Predictability horizon roughly scales như:

```math
T
\sim
\frac1\lambda
\log\frac{\text{allowed error}}{\text{initial error}}.
```

Improving measurement precision only increases forecast horizon logarithmically.

Đây là deep reason weather-like chaotic systems có finite practical predictability even with deterministic equations.

---

## 15. Lyapunov exponent cho 1D maps

For orbit `x_n`:

```math
\lambda
=
\lim_{N\to\infty}
\frac1N
\sum_{n=0}^{N-1}
\log|F'(x_n)|
```

nếu limit phù hợp tồn tại.

Interpretation:

```text
λ < 0 → nearby perturbations shrink on average
λ > 0 → nearby perturbations grow on average
```

Local derivative products become average exponential growth rate.

Đây là same logarithm/product-to-sum idea xuất hiện trong compound growth và information theory.

---

## 16. Attractor

Một **attractor (끌개)** là invariant set mà nearby trajectories tend toward in appropriate sense.

Types:

```text
fixed-point attractor
limit-cycle attractor
quasiperiodic attractor
strange attractor
```

A **strange attractor** có complex/fractal-like geometry và chaotic dynamics.

Attractor is about long-run state-set, không phải single trajectory formula.

---

## 17. Basin of attraction

**Basin of attraction (끌림 영역)** là set initial conditions whose trajectories approach same attractor.

Một system có thể có multiple attractors; outcome phụ thuộc starting state.

Boundary giữa basins có thể rất complex.

Điều này quan trọng trong optimization: different initializations có thể converge tới different local minima/attractors.

---

## 18. Conjugacy: same dynamics dưới different coordinates

Hai systems `F` và `G` có thể considered dynamically equivalent nếu tồn tại invertible map `h` sao cho:

```math
h\circ F=G\circ h.
```

Khi đó:

```math
G=h\circ F\circ h^{-1}.
```

Đây là **conjugacy (켤레관계)**.

Idea giống change of basis trong linear algebra:

> Representation đổi nhưng underlying behavior pattern có thể giữ nguyên.

Classification của dynamical systems thường tìm invariants dưới coordinate transformations.

---

## 19. Symbolic dynamics

Continuous-looking chaotic orbit có thể encode bằng symbol sequences.

Ví dụ partition state space thành regions `L,R`, rồi record orbit:

```text
L R R L L R ...
```

Ta convert geometric dynamics thành shift dynamics trên sequences.

Bridge:

```text
continuous/nonlinear system
→ symbolic sequence
→ combinatorics/information theory
```

Topological entropy đo growth rate của distinguishable orbit patterns.

---

## 20. Entropy và dynamical complexity

Roughly, if number of distinguishable orbit patterns length `n` grows like

```math
N(n)\approx e^{hn},
```

then `h` acts like entropy rate.

Higher entropy means system produces more new orbit information per unit time/step.

Đây là mathematical bridge giữa dynamical systems và [Information theory](../07_discrete_cs/06_information_theory_and_coding.md).

---

## 21. Poincaré section

Continuous flow trong 3D có thể khó visualize.

Chọn a lower-dimensional surface và record mỗi lần trajectory cross it.

Ta tạo **Poincaré map (푸앵카레 사상)**:

```text
continuous-time flow
→ discrete return map
```

Periodic orbit của flow trở thành fixed point của Poincaré map.

Stability có thể analyze bằng discrete-map tools.

Đây là powerful reduction giữa continuous và discrete dynamics.

---

## 22. Lotka–Volterra và nonlinear interaction

Predator-prey model:

```math
\dot x=ax-bxy,
```

```math
\dot y=-cy+dxy.
```

Interaction terms `xy` tạo nonlinearity.

Phase portrait cho information mà closed-form time solution không nhất thiết cho trực tiếp:

- equilibria;
- invariant trajectories;
- cycles/near-cycles;
- response to parameter changes.

Dynamical thinking ưu tiên geometry của trajectories hơn symbolic solving.

---

## 23. Newton's method cũng là dynamical system

Newton iteration:

```math
x_{n+1}
=x_n-
\frac{f(x_n)}{f'(x_n)}
```

là discrete dynamical system.

Roots là fixed points.

Different initial values có thể converge tới different roots.

Trong complex plane, basins of attraction của Newton map có fractal boundaries.

Numerical algorithm và chaos theory gặp nhau ở đây.

---

## 24. Stability không đồng nghĩa robustness toàn cục

Linearization nói local behavior gần hyperbolic equilibrium.

Nó không đảm bảo:

- global convergence;
- absence of another attractor;
- resilience to large perturbation;
- behavior far from equilibrium.

Một locally stable equilibrium có basin rất nhỏ.

Engineering judgment cần phân biệt:

```text
local stability
vs
global stability
vs
robustness under model/parameter uncertainty
```

---

## 25. Lyapunov function

Một **Lyapunov function (리아푸노프 함수)** `V(x)` giống generalized energy.

Nếu:

```math
V(x)\ge0,
```

và along trajectories:

```math
\dot V(x)\le0,
```

thì `V` không tăng.

Nếu strict decrease away from equilibrium dưới suitable conditions, ta có strong stability conclusions.

Điểm mạnh: không cần solve ODE explicitly.

Đây là qualitative certificate giống objective decrease trong optimization.

---

## 26. Connection với optimization

Gradient descent:

```math
x_{k+1}=x_k-\eta\nabla f(x_k)
```

là discrete dynamical system.

Questions:

- fixed points là gì?
- stable fixed point có correspond minima không?
- step size làm bifurcation/oscillation không?
- momentum tạo higher-dimensional dynamics thế nào?

Optimization algorithm không chỉ là formula update; nó là designed dynamical system.

Learning rate quá lớn có thể chuyển từ convergence sang oscillation/divergence.

---

## 27. Connection với control

Control adds input:

```math
\dot x=F(x,u).
```

Goal không chỉ observe dynamics mà shape nó.

Feedback:

```math
u=K(x)
```

thay closed-loop dynamics thành:

```math
\dot x=F(x,K(x)).
```

Control design có thể xem như thiết kế vector field để desired state/trajectory trở thành stable attractor.

---

## 28. Common misconceptions

**“Chaos = random.”** Chaotic system có thể deterministic.

**“Nếu equation deterministic thì prediction lâu dài luôn chính xác khi computer đủ mạnh.”** Measurement/model error có thể amplify exponentially.

**“Stable equilibrium nghĩa mọi initial condition converge tới nó.”** Stability thường local; basin matters.

**“Linearization mô tả toàn system.”** Nó chỉ reliable near relevant equilibrium và under conditions.

**“Bifurcation chỉ là curve split trên graph.”** Nó là qualitative change của invariant structures/stability.

**“Period doubling tự động nghĩa chaos.”** Nó là một route toward chaos trong certain families, không universal diagnostic duy nhất.

---

## 29. Mental model

> Dynamical systems nghiên cứu evolution geometry thay vì chỉ closed-form solutions. Fixed points/cycles là invariant structures; stability nói perturbation đi đâu; bifurcation nói structure đổi khi parameter đổi; chaos nói deterministic evolution có thể amplify uncertainty exponentially. Một update rule, ODE, optimization algorithm hay feedback controller đều có thể được nhìn bằng cùng language của state, orbit, attractor và stability.

---

## 30. Mạch học tiếp

```text
ODE / recurrence
→ equilibrium & linearization
→ phase portrait
→ bifurcation
→ periodic orbits
→ chaos / Lyapunov exponents
→ symbolic dynamics / entropy
```

Applied route:

```text
Dynamical systems
→ Control
→ Optimization algorithms
→ Complex systems / networks
```

Đọc tiếp:

- [Differential equations](./05_differential_equations.md)
- [Laplace/Z-transform and dynamic systems](../09_connections/06_laplace_z_transform_and_dynamic_systems.md)
- [Dynamic programming and optimal control](../08_optimization_numerical/06_dynamic_programming_bellman_and_optimal_control.md)
- [Information theory](../07_discrete_cs/06_information_theory_and_coding.md)

## Further reading

- Shlomo Sternberg — *Dynamical Systems*, Harvard lecture-note lineage; especially iteration, bifurcations, conjugacy, hyperbolicity, Lotka–Volterra and symbolic dynamics.
