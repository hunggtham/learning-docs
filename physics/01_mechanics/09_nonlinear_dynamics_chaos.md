# Động lực học phi tuyến, độ ổn định và hỗn loạn

## Tuyến tính là xấp xỉ hữu ích, không phải luật phổ quát

Nhiều bài vật lý ban đầu dẫn tới phương trình tuyến tính vì ta xét nhiễu nhỏ quanh cân bằng. Ví dụ con lắc thật thỏa

```math
\ddot\theta+\frac{g}{\ell}\sin\theta=0,
```

chỉ trở thành

```math
\ddot\theta+\frac{g}{\ell}\theta=0
```

khi `|\theta|\ll1`.

Hệ tuyến tính có nguyên lý chồng chập. Hệ phi tuyến nói chung không có. Chính việc mất tính chồng chập cho phép xuất hiện nhiều hành vi mới:

- nhiều trạng thái cân bằng;
- phân nhánh;
- dao động tự duy trì;
- khóa pha;
- pattern formation;
- hỗn loạn tất định.

## Hệ động lực và không gian trạng thái

Một hệ autonomous có thể viết

```math
\dot{\mathbf x}=\mathbf f(\mathbf x;\mu),
```

trong đó `\mathbf x` là vector trạng thái và `\mu` là tham số điều khiển.

Mỗi điều kiện ban đầu xác định một quỹ đạo trong không gian trạng thái. Thay vì chỉ hỏi `x(t)` bằng bao nhiêu, động lực học phi tuyến thường hỏi cấu trúc toàn cục của các quỹ đạo:

- chúng tiến tới đâu;
- trạng thái nào ổn định;
- boundary giữa các basin ở đâu;
- cấu trúc thay đổi thế nào khi `\mu` đổi.

## Điểm cố định và tuyến tính hóa

Điểm cố định `\mathbf x^*` thỏa

```math
\mathbf f(\mathbf x^*)=0.
```

Đặt

```math
\mathbf x=\mathbf x^*+\delta\mathbf x.
```

Với nhiễu nhỏ,

```math
\dot{\delta\mathbf x}
\approx J(\mathbf x^*)\delta\mathbf x,
```

trong đó Jacobian là

```math
J_{ij}
=\frac{\partial f_i}{\partial x_j}.
```

Các trị riêng `\lambda_i` của `J` quyết định độ ổn định cục bộ:

- `Re(\lambda_i)<0` cho mọi mode: nhiễu tắt dần;
- có `Re(\lambda_i)>0`: ít nhất một mode tăng;
- trị riêng có phần ảo: xuất hiện quay hoặc dao động cục bộ.

Đây là cầu nối trực tiếp giữa đại số tuyến tính và ổn định động lực học.

## Ví dụ một chiều: phương trình logistic liên tục

Xét

```math
\dot x=rx\left(1-\frac{x}{K}\right).
```

Hai điểm cố định là

```math
x^*=0,
\qquad
x^*=K.
```

Đạo hàm

```math
f'(x)=r\left(1-\frac{2x}{K}\right).
```

Với `r>0`:

```math
f'(0)=r>0,
```

nên `x=0` bất ổn;

```math
f'(K)=-r<0,
```

nên `x=K` ổn định.

Một phép tính đạo hàm đơn giản đã cho cấu trúc ổn định mà chưa cần giải nghiệm đầy đủ.

## Phân nhánh: khi cấu trúc nghiệm thay đổi

Phân nhánh (bifurcation / 분기) xảy ra khi thay đổi tham số làm số lượng hoặc độ ổn định của nghiệm thay đổi định tính.

Ví dụ normal form của pitchfork là

```math
\dot x=\mu x-x^3.
```

Điểm cố định thỏa

```math
x(\mu-x^2)=0.
```

Nếu `\mu<0`, chỉ có `x=0` ổn định.

Nếu `\mu>0`, `x=0` mất ổn định và hai nghiệm mới

```math
x=\pm\sqrt\mu
```

xuất hiện.

Đây là mô hình tối giản của phá vỡ đối xứng tự phát: phương trình đối xứng dưới `x\to-x`, nhưng hệ chọn một trong hai nhánh ổn định.

## Saddle-node và threshold

Một normal form khác là

```math
\dot x=\mu-x^2.
```

Với `\mu>0`, có hai fixed point

```math
x=\pm\sqrt\mu.
```

Khi `\mu\to0`, chúng gặp nhau rồi biến mất.

Cấu trúc saddle-node xuất hiện trong switching, buckling, laser threshold và nhiều hệ có hiện tượng “đột ngột không còn trạng thái cân bằng cũ”.

## Hopf bifurcation và dao động tự duy trì

Trong hệ ít nhất hai chiều, một trạng thái cố định có thể mất ổn định khi cặp trị riêng phức đi qua trục ảo.

Khi đó một limit cycle có thể xuất hiện: hệ dao động tự duy trì dù không có lực cưỡng bức tuần hoàn bên ngoài.

Các ví dụ bao gồm:

- oscillator điện tử;
- chemical oscillator;
- nhịp sinh học;
- một số instability khí động.

Điểm này phân biệt dao động tự sinh với dao động cưỡng bức của một hệ tuyến tính.

## Không gian pha và attractor

Với dao động tử một chiều, phase space có thể dùng `(x,v)`.

Quỹ đạo có thể tiến tới:

- fixed point;
- limit cycle;
- torus;
- strange attractor.

Attractor không phải một lực hút vật lý. Nó là tập trạng thái mà một họ điều kiện ban đầu tiến gần về lâu dài.

Basin of attraction là tập các điều kiện ban đầu dẫn tới cùng attractor.

Trong hệ đa ổn định, boundary giữa các basin quyết định hệ cuối cùng rơi vào trạng thái nào.

## Lyapunov exponent và độ nhạy điều kiện ban đầu

Hai quỹ đạo bắt đầu cách nhau `\delta_0` có thể tách nhau gần

```math
\delta(t)
\sim\delta_0e^{\lambda t}.
```

Nếu số mũ Lyapunov lớn nhất `\lambda>0`, sai lệch nhỏ tăng theo hàm mũ trong miền phù hợp.

Vì điều kiện ban đầu luôn được đo với uncertainty hữu hạn, thời gian dự báo chi tiết bị giới hạn gần bởi

```math
T_{pred}
\sim\frac{1}{\lambda}
\ln\frac{\Delta_{tol}}{\delta_0},
```

trong đó `\Delta_{tol}` là sai số tối đa chấp nhận được.

Hệ có thể hoàn toàn tất định nhưng vẫn không thể dự báo chi tiết tùy ý xa trong tương lai.

## Hỗn loạn không đồng nghĩa với ngẫu nhiên

Hệ hỗn loạn có thể tuân phương trình deterministic không chứa noise.

Ngẫu nhiên thống kê và chaos là hai khái niệm khác nhau:

- stochastic system có biến ngẫu nhiên trong mô hình;
- chaotic deterministic system có luật xác định nhưng nhạy điều kiện đầu.

Trong hệ thực, cả hai có thể cùng tồn tại.

Dự báo thời tiết là ví dụ: phương trình khí quyển gần deterministic trong mô hình continuum, nhưng uncertainty ban đầu, model error và chaos giới hạn forecast horizon.

## Logistic map

Một mô hình rời rạc tối giản là

```math
x_{n+1}=rx_n(1-x_n).
```

Dù chỉ có một biến và một tham số, khi `r` tăng nó có thể trải qua:

```text
fixed point
→ period-2
→ period-4
→ period-8
→ ...
→ chaos
```

Đây là chuỗi period-doubling.

Logistic map cho thấy độ phức tạp không nhất thiết cần hàng triệu thành phần; feedback phi tuyến đơn giản đã đủ tạo bifurcation và chaos.

## Poincaré section

Với hệ liên tục tuần hoàn theo thời gian, theo dõi quỹ đạo đầy đủ có thể khó.

Ta có thể lấy mẫu hệ mỗi chu kỳ của lực cưỡng bức. Poincaré section biến quỹ đạo liên tục thành map rời rạc:

- limit cycle cho một số điểm hữu hạn;
- quasiperiodic motion cho đường cong;
- chaos có thể cho tập fractal phức tạp.

Đây là kỹ thuật giảm chiều rất mạnh để nhìn cấu trúc động lực.

## Con lắc cưỡng bức tắt dần

Một mô hình kinh điển là

```math
\ddot\theta
+\gamma\dot\theta
+\frac{g}{\ell}\sin\theta
=A\cos\omega t.
```

Hệ chứa:

- phi tuyến `\sin\theta`;
- damping;
- forcing ngoài.

Tùy `A,\omega,\gamma`, hệ có thể khóa vào dao động tuần hoàn, period-doubling hoặc chaos.

Nếu thay `\sin\theta` bằng `\theta`, ta mất nhiều hành vi phi tuyến quan trọng. Đây là ví dụ rõ rằng tuyến tính hóa có miền hiệu lực hữu hạn.

## Bảo toàn và chaos Hamilton

Một hệ Hamilton kín vẫn có thể chaotic dù không có attractor tiêu tán.

Trong phase space, quỹ đạo có thể chứa vùng regular xen kẽ vùng chaotic. KAM theory mô tả cách một số torus của hệ tích phân được sống sót dưới nhiễu loạn nhỏ, còn các resonance có thể tạo transport phức tạp.

Vì vậy chaos không đồng nghĩa với tiêu tán hoặc strange attractor; đó chỉ là một trường hợp phổ biến trong hệ dissipative.

## Mô phỏng số của hệ hỗn loạn

Sai số rounding và sai số bước thời gian cũng bị động lực chaotic khuếch đại.

Hai trajectory từ hai solver có thể tách nhau sau thời gian dài dù cả hai solver đều đúng trong sense numerical convergence ngắn hạn.

Do đó validation cho chaos không nên chỉ hỏi “trajectory có trùng từng điểm mãi không?”. Cần kiểm tra:

- convergence theo timestep ở horizon hữu hạn;
- phân bố thống kê;
- Lyapunov exponent;
- attractor geometry;
- invariant hoặc conservation law khi phù hợp.

## Liên hệ với Control và Engineering

Hệ điều khiển thường được thiết kế quanh operating point bằng linearization.

Nhưng nếu gain, tải hoặc state đi xa operating point, nonlinear effect có thể gây:

- saturation;
- limit cycle;
- bifurcation;
- loss of stability.

Vì vậy linear controller tốt trong một vùng không đảm bảo global stability.

Trong robotics, power electronics và flight dynamics, phase portrait, Lyapunov function và bifurcation analysis giúp đánh giá điều mà eigenvalue cục bộ không nói hết.

## Miền áp dụng và giới hạn

Linear stability chỉ cho thông tin gần fixed point. Nó không quyết định đầy đủ global behavior.

Một Lyapunov exponent dương là dấu hiệu mạnh của chaos nhưng việc ước lượng từ dữ liệu hữu hạn cần cẩn thận với noise và sampling.

Fractal-looking plot cũng không tự chứng minh chaos; cần kiểm tra động lực và sensitivity có định lượng.

## Mô hình tư duy (Mental Model)

Tuyến tính hóa hỏi “gần trạng thái này, nhiễu nhỏ tăng hay giảm?”. Bifurcation hỏi “khi tham số thay đổi, cấu trúc trạng thái đổi ra sao?”. Chaos hỏi “luật deterministic có thể khuếch đại uncertainty nhanh đến mức nào?”.

```text
nonlinear equations
→ fixed points
→ local stability
→ bifurcations
→ phase-space structure
→ Lyapunov growth
→ predictability horizon
```

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Phi tuyến nghĩa ngẫu nhiên”

Không. Hệ phi tuyến có thể hoàn toàn deterministic.

### “Chaos nghĩa không có quy luật”

Không. Chaos có thể sinh từ phương trình xác định rất đơn giản.

### “Tuyến tính hóa ổn định nghĩa hệ ổn định cho mọi điều kiện đầu”

Không. Linearization chỉ là kết luận cục bộ quanh operating point.

### “Hai mô phỏng chaotic tách nhau nghĩa một solver chắc chắn sai”

Không. Cần đánh giá convergence hữu hạn thời gian và đại lượng thống kê thay vì đòi trajectory dài hạn trùng tuyệt đối.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Cơ học giải tích](08_analytical_mechanics.md), [Ngôn ngữ Toán học](../00_foundations/03_mathematical_language.md), [Dao động](../02_oscillations_waves/00_oscillations_resonance.md).

**Liên hệ tiếp:** [Hamilton nâng cao](10_canonical_transformations_hamilton_jacobi.md), [Vật lý tính toán](../12_experimental_computational/02_computational_physics.md), [Dòng rối](../03_continuum/03_turbulence_rheology_soft_matter.md).
