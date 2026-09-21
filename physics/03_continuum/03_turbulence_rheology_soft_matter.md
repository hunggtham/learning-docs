# Turbulence, rheology và soft vật chất (matter): khi liên tục (continuum) trở nên phi tuyến và nhiều thang đo

## Tại sao Navier–Stokes chưa phải là “đã giải xong chất lưu”?

Biết governing phương trình (equation) không đồng nghĩa biết solution. Navier–Stokes kết hợp bảo toàn (conservation) of khối lượng (mass), động lượng (momentum) và constitutive giả định (assumption) cho viscous ứng suất (stress). Nhưng phi tuyến (nonlinear) term

```math
(\vec v\cdot\nabla)\vec v
```

làm vận tốc (velocity) trường (field) tự advect chính nó. Ở số Reynolds (Reynolds number) lớn, small disturbances có thể tương tác qua nhiều các thang (scales) và tạo **turbulence (난류)**. Đây là ví dụ điển hình của physics: định luật (law) cục bộ (local) khá gọn nhưng tập thể (collective) hành vi (behavior) cực kỳ phức tạp.

## số Reynolds như tỷ số cạnh tranh giữa inertia và độ nhớt (viscosity)

thang (Scale) analysis cho incompressible dòng chảy (flow) với characteristic tốc độ (speed) `U`, độ dài (length) `L`, kinematic độ nhớt `\nu`:

```math
Re=\frac{UL}{\nu}.
```

`Re` không phải “ngưỡng turbulence tuyệt đối”. Nó đo relative importance của inertial vận chuyển (transport) so với viscous động lượng khuếch tán (diffusion). chuyển mức (Transition) còn phụ thuộc hình học (geometry), nhiễu động (disturbance) và các điều kiện biên (boundary conditions). Pipe dòng chảy, lớp biên (boundary layer) và dòng chảy quanh vật thể (object) có critical hành vi khác nhau.

## năng lượng (Energy) cascade

Một mô hình tư duy (mental model) quan trọng của 3D turbulence là năng lượng injected ở thang lớn được phi tuyến các tương tác (interactions) chuyển qua intermediate eddies rồi dissipate bởi độ nhớt ở thang nhỏ. Trong inertial range, Kolmogorov lý thuyết (theory) dự đoán năng lượng phổ (spectrum) thu nhỏ quy mô (scaling) gần

```math
E(k)\propto \varepsilon^{2/3}k^{-5/3},
```

với `k` wavenumber và `\varepsilon` năng lượng dissipation tốc độ biến thiên (rate) per khối lượng.

Đây không phải universal chính xác (exact) định luật cho mọi turbulent dòng chảy, nhưng cho thấy cách phân tích thứ nguyên (dimensional analysis) + thang locality có thể tạo dự đoán (prediction) mạnh khi vi mô (microscopic) details không cần biết đầy đủ.

## Boundary các lớp (layers) và lực cản (drag) crisis

Gần no-slip wall, vận tốc phải chuyển từ không (zero) ở bề mặt (surface) đến tự do (free)-stream value. Region gradient lớn này là lớp biên. Khi lớp biên tách khỏi bề mặt, wake và áp suất (pressure) lực cản có thể tăng mạnh. Golf ball dimples khai thác chuyển mức của lớp biên để delay separation trong một range vận tốc, làm giảm áp suất lực cản dù skin ma sát (friction) có thể tăng.

Vì vậy “bề mặt nhẵn luôn ít cản hơn” không phải rule tuyệt đối.

## Rheology: khi ứng suất không tỷ lệ đơn giản với biến dạng tương đối (strain) tốc độ biến thiên

Newtonian chất lưu (fluid) obey gần

```math
\tau=\eta\dot\gamma,
```

với ứng suất cắt (shear stress) `\tau`, độ nhớt `\eta` và shear tốc độ biến thiên `\dot\gamma`. Nhưng nhiều vật liệu đời sống không Newtonian.

Ketchup và blood có thể shear-thinning: hiệu dụng (effective) độ nhớt giảm khi shear tốc độ biến thiên tăng. Cornstarch suspension có thể shear-thicken trong chế độ (regime) nhất định. Toothpaste và some gels có yield-ứng suất hành vi: dưới ứng suất threshold chúng gần chất rắn (solid)-like, trên threshold mới dòng chảy đáng kể.

Rheology (Rheology / 유변학) vì thế hỏi quan hệ (relation) giữa ứng suất, biến dạng (deformation) và time. Polymer melts có memory vì chain cấu hình (configuration) cần thời gian relax; viscoelasticity kết hợp spring-like storage và dashpot-like dissipation.

## Maxwell và Kelvin–Voigt các mô hình (models)

Một tuyến tính (linear) viscoelastic mô hình (model) đơn giản nối spring và dashpot theo series — Maxwell mô hình. Nó mô tả ứng suất hồi phục (relaxation). Kelvin–Voigt mô hình nối song song, hữu ích cho creep hành vi khác. Các mô hình này không phải phân tử (molecular) truth; chúng là reduced constitutive các mô hình giống RC/RL analog trong mạch điện (circuit) lý thuyết.

phức (Complex) modulus dưới oscillatory forcing,

```math
G^*(\omega)=G'(\omega)+iG''(\omega),
```

phân tách storage modulus `G'` và tổn hao (loss) modulus `G''`. tần số (Frequency) sweep vì vậy probe bên trong (internal) hồi phục times của vật liệu (material).

## Soft vật chất: năng lượng các thang gần nhiệt (thermal) năng lượng

**Soft vật chất (연성물질)** gồm polymers, colloids, foams, emulsions, chất lỏng (liquid) các tinh thể (crystals) và biological các vật liệu (materials). Điểm chung không phải “mềm” theo cảm giác, mà nhiều structural năng lượng các thang gần `k_BT`, nên các thăng giáng nhiệt (thermal fluctuations) cạnh tranh trực tiếp với đàn hồi (elastic)/interfacial/electrostatic các lực (forces).

Brownian chuyển động (motion) của colloidal hạt (particle) là kết quả bombardment vi mô và fluctuation. Einstein quan hệ nối hệ số khuếch tán (diffusion coefficient) với độ linh động (mobility):

```math
D=\mu k_BT.
```

Đây là một dạng fluctuation–dissipation liên hệ (connection): ngẫu nhiên (random) các thăng giáng (fluctuations) và dissipative đáp ứng (response) không độc lập mà cùng xuất phát từ nhiệt environment.

## sức căng bề mặt (Surface tension) + soft vật chất = droplets, emulsions và capillary number

Khi dòng chảy deform giọt (droplet), viscous ứng suất cạnh tranh sức căng bề mặt. Capillary number

```math
Ca=\frac{\eta U}{\gamma}
```

so sánh viscous hiệu ứng (effect) với sức căng bề mặt. `Ca` nhỏ: mặt phân cách (interface) giữ hình dạng (shape) mạnh; `Ca` lớn: dòng chảy dễ deform/break giọt.

vi lưu (Microfluidics) dùng chính competition này để tạo droplets đồng đều cho hóa học (chemistry), diagnostics và biological assays.

## động lực học chất lưu tính toán (Computational Fluid Dynamics) và turbulence các mô hình

Direct số (Numerical) mô phỏng (Simulation) giải mọi relevant turbulent các thang nhưng cost tăng cực nhanh với số Reynolds. kỹ thuật (Engineering) thường dùng RANS hoặc LES: thay vì resolve tất cả các thang, mô hình hiệu ứng của unresolved các thăng giáng.

Đây là cùng triết lý mô hình reduction thấy ở physics khác: câu hỏi không phải “mô phỏng có chính xác không?” mà “các thang nào cần resolve để đại lượng quan sát (observable) mình quan tâm có sai số (error) chấp nhận được?”

## Mô hình tư duy (Mental Model)

> liên tục physics không dừng ở phương trình vật liệu “đẹp”. Khi phi tuyến advection, memory, interfaces và các thăng giáng nhiệt cùng xuất hiện, hành vi phụ thuộc competition giữa nhiều timescales và độ dài các thang. các số vô thứ nguyên (Dimensionless numbers) là bản đồ cho biết competition nào đang thống trị.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “số Reynolds lớn nghĩa chắc chắn turbulent”

Không. Nó báo inertia mạnh so với độ nhớt, nhưng chuyển mức phụ thuộc độ ổn định (stability), hình học và disturbances.

### “độ nhớt là một hằng số của mọi chất lưu”

Chỉ đúng cho Newtonian mô hình trong một chế độ. Non-Newtonian các chất lưu (fluids) có hiệu dụng đáp ứng phụ thuộc shear tốc độ biến thiên, lịch sử (history) và tần số.

### “Turbulence chỉ là ngẫu nhiên nhiễu (noise)”

Turbulence có stochastic-looking các thăng giáng nhưng vẫn chứa coherent structures, bảo toàn các ràng buộc (constraints) và statistical thu nhỏ quy mô. Nó không phải white nhiễu tùy ý.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Fluids](00_fluids.md), [Transport phenomena](02_transport_diffusion_heat.md), [Nonlinear dynamics](../01_mechanics/09_nonlinear_dynamics_chaos.md).

**Liên hệ tiếp:** [Statistical mechanics](../04_thermal_statistical/01_entropy_statistical_mechanics.md), [Computational Physics](../12_experimental_computational/02_computational_physics.md), hóa học (chemical) kỹ thuật, biomechanics và vi lưu.
