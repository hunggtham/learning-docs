# Hạt đồng nhất và thống kê lượng tử: fermion, boson, Pauli và many-body các trạng thái (states)

## “Hai electron giống nhau” có nghĩa sâu hơn giống hai viên bi giống nhau

Trong cơ học cổ điển (classical mechanics), nếu ta có hai quả bóng hoàn toàn giống về khối lượng (mass) và hình dạng (shape), vẫn có thể tưởng tượng gắn nhãn A và B rồi theo dõi quỹ đạo (trajectory) của từng quả. Trong cơ học lượng tử (quantum mechanics), **hạt đồng nhất (Identical Particles / 동일 입자)** mạnh hơn nhiều: không tồn tại phép đo (measurement) vật lý nào cho phép phân biệt hai electron chỉ bằng “danh tính (identity) cá nhân” của chúng. Khi hoán đổi labels của các hạt đồng nhất (identical particles), đại lượng quan sát (observable) physics không được thay đổi.

Điều này buộc many-hạt (particle) hàm sóng (wavefunction) có đối xứng (symmetry) đặc biệt dưới hạt trao đổi (exchange).

Với hai các hạt (particles) có coordinates `1` và `2`, trao đổi toán tử (operator) `P_{12}` đổi chúng cho nhau. Vì exchanging hai lần phải trả lại trạng thái (state) ban đầu,

```math
P_{12}^2=1.
```

Eigenvalue của trao đổi vì thế là `+1` hoặc `-1`.

Trong tự nhiên, các hạt với integer spin là **bosons (Boson / 보손)** và many-body trạng thái symmetric:

```math
\Psi(1,2)=+\Psi(2,1).
```

các hạt với half-integer spin là **fermions (Fermion / 페르미온)** và trạng thái antisymmetric:

```math
\Psi(1,2)=-\Psi(2,1).
```

liên hệ (Connection) giữa spin và thống kê (statistics) là spin–thống kê theorem của tương đối tính (relativistic) lượng tử (quantum) trường (field) lý thuyết (theory); nonrelativistic cơ học lượng tử thường lấy rule này làm input.

## Pauli exclusion nguyên lý (principle) xuất hiện từ antisymmetry

Nếu hai identical fermions cố ở cùng single-hạt trạng thái `\phi`, antisymmetric combination là

```math
\Psi(1,2)=\frac{1}{\sqrt2}
[\phi(1)\phi(2)-\phi(2)\phi(1)]=0.
```

hàm sóng bằng không (zero) nghĩa cấu hình (configuration) đó không tồn tại. Đây là **nguyên lý loại trừ Pauli (Pauli Exclusion Principle / 파울리 배타 원리)**: hai identical fermions không thể chiếm cùng lượng tử trạng thái đầy đủ.

Pauli nguyên lý không phải một lực đẩy mới giữa electron. Nó là ràng buộc (constraint) về cấu trúc (structure) của allowed many-fermion các trạng thái. Hệ quả vĩ mô (macroscopic) của ràng buộc này lại cực lớn: electron shell cấu trúc của nguyên tử (atom), tuần hoàn (periodic) table, độ ổn định (stability) và kích thước của vật chất (matter), electron suy biến (degeneracy) áp suất (pressure) trong white dwarf, và Fermi bề mặt (surface) của các kim loại (metals).

## Spin giúp nhiều electron ở cùng không gian (spatial) orbital như thế nào?

Một electron trạng thái gồm cả không gian part và spin part. Hai electron trong cùng atomic không gian orbital có thể tồn tại nếu spin trạng thái tổng thể khiến full hàm sóng antisymmetric. Ground trạng thái của heli (helium), chẳng hạn, có không gian part symmetric và spin singlet antisymmetric.

Điều này giải thích vì sao nói “một orbital chứa tối đa hai electron có opposite spin” chỉ là simplified rule của cấu trúc nguyên tử (atomic structure). Rule sâu hơn là tổng (total) fermionic trạng thái phải antisymmetric khi trao đổi bất kỳ hai electron.

## Slater determinant

Đối với nhiều fermions, antisymmetry được tổ chức gọn bằng **Slater determinant (슬레이터 행렬식)**:

```math
\Psi(x_1,\ldots,x_N)=\frac{1}{\sqrt{N!}}
\begin{vmatrix}
\phi_1(x_1)&\phi_2(x_1)&\cdots&\phi_N(x_1)\\
\phi_1(x_2)&\phi_2(x_2)&\cdots&\phi_N(x_2)\\
\vdots&\vdots&\ddots&\vdots\\
\phi_1(x_N)&\phi_2(x_N)&\cdots&\phi_N(x_N)
\end{vmatrix}.
```

Nếu hai single-hạt các trạng thái giống nhau, hai columns giống nhau và determinant bằng không — Pauli nguyên lý xuất hiện tự động. Hartree–Fock và nhiều phương pháp điện tử (electronic)-cấu trúc bắt đầu từ cấu trúc này rồi thêm các tương quan (correlations) vượt beyond một determinant duy nhất.

## Fermions ở hữu hạn (finite) nhiệt độ (temperature): Fermi–Dirac phân bố (distribution)

Ở cân bằng nhiệt (thermal equilibrium), trung bình (average) occupation của single-hạt năng lượng (energy) mức (level) `E` cho noninteracting fermions là

```math
f(E)=\frac{1}{e^{(E-\mu)/(k_B T)}+1}.
```

Dấu `+1` ở denominator phản ánh exclusion: occupation của một lượng tử trạng thái không thể tăng vô hạn. `\mu` là hóa học (chemical) thế (potential).

Ở `T=0`, các trạng thái được lấp đến **Fermi năng lượng (페르미 에너지)** `E_F`; phía dưới gần như occupied, phía trên empty. Trong kim loại (metal) ở room nhiệt độ, `k_BT` thường nhỏ hơn đáng kể so với `E_F`, nên chỉ electron gần Fermi bề mặt mới dễ thay đổi occupation và đóng vai trò mạnh trong vận chuyển (transport), nhiệt dung (heat capacity) và đáp ứng (response).

Đây là lý do mô hình (model) “tất cả electron dẫn (conduction) cùng nhận nhiệt (thermal) năng lượng `k_BT` như cổ điển (classical) chất khí (gas)” thất bại.

## Bosons: nhiều hạt có thể cùng chiếm một trạng thái

Với bosons, symmetric hàm sóng không cấm nhiều các hạt cùng single-hạt trạng thái. Bose–Einstein occupation là

```math
n(E)=\frac{1}{e^{(E-\mu)/(k_B T)}-1}.
```

Dấu `-1` làm occupation có thể rất lớn khi denominator nhỏ. Điều này mở đường cho tập thể (collective) occupation như Bose–Einstein condensation (BEC / 보스-아인슈타인 응축) trong một số hệ bosonic ở low nhiệt độ.

Photon cũng là boson. Vì photon number không được bảo toàn trong cân bằng nhiệt theo cách hạt number của nguyên tử được bảo toàn, hóa học thế của photon chất khí bằng không. Planck blackbody phổ (spectrum) là direct consequence của quantized điện từ (electromagnetic) các mode (modes) + Bose thống kê.

## giới hạn cổ điển (Classical limit): tại sao đôi khi Maxwell–Boltzmann vẫn đúng?

Khi occupation của mỗi lượng tử trạng thái rất nhỏ, tức chất khí dilute và nhiệt bước sóng (wavelength) ngắn so với interparticle spacing, cả Fermi–Dirac và Bose–Einstein distributions tiến gần Maxwell–Boltzmann form. thống kê lượng tử (Quantum statistics) không “biến mất”; hiệu ứng (effect) trao đổi trở nên negligible ở chế độ (regime) đó.

nhiệt de Broglie bước sóng cho khối lượng `m` có thang (scale)

```math
\lambda_{th}\sim\frac{h}{\sqrt{2\pi m k_B T}}.
```

Khi `n\lambda_{th}^3\ll1`, chất khí thường gần cổ điển. Khi quantity này approach hoặc vượt order one, wavefunctions overlap đáng kể và thống kê lượng tử trở thành thiết yếu.

## suy biến áp suất: áp suất không cần chuyển động nhiệt (thermal motion)

Fermion chất khí ở `T=0` vẫn có nonzero động lượng (momentum) phân bố vì Pauli nguyên lý buộc các hạt lấp nhiều các trạng thái đến Fermi động lượng. Vì vậy có **suy biến áp suất (축퇴압)** ngay cả không có nhiệt áp suất cổ điển.

Trong white dwarf, electron suy biến áp suất chống hấp dẫn (gravity). Trong sao neutron (neutron star), neutron suy biến và các tương tác hạt nhân (nuclear interactions) đóng vai trò. Khi relativity trở nên quan trọng, phương trình (equation) of trạng thái thay đổi; đây là liên hệ trực tiếp giữa thống kê lượng tử, thuyết tương đối hẹp (special relativity) và vật lý thiên văn (astrophysics).

## trao đổi tương tác (interaction) và từ tính (magnetism)

Antisymmetry cũng làm không gian tương quan (correlation) phụ thuộc spin cấu hình. Khi Coulomb tương tác có mặt, trao đổi cấu trúc ảnh hưởng năng lượng dù không có một “trao đổi lực (force)” cổ điển riêng. Trong các nguyên tử (atoms) nó góp vào Hund's rules; trong các chất rắn (solids) nó là phần nền của ferromagnetic/antiferromagnetic ordering và many-body các mô hình (models).

## rối lượng tử (Entanglement) vì các hạt đồng nhất cần đọc cẩn thận

Symmetrization/antisymmetrization tạo các tương quan do indistinguishability, nhưng không phải mọi trao đổi tương quan đều tương đương operational rối lượng tử dùng trong lượng tử thông tin (information). Khi nói rối lượng tử giữa các hạt đồng nhất, cần chỉ rõ các mode, accessible các đại lượng quan sát (observables) và partition của hệ (system).

## Mô hình tư duy (Mental Model)

> thống kê lượng tử không phải là cách “đếm hạt” được thêm sau cơ học lượng tử. Nó là ràng buộc trực tiếp lên hình học (geometry) của many-hạt Hilbert không gian (space). Bosons và fermions có allowed không gian trạng thái (state space) khác nhau, nên từ cùng những lực cơ bản có thể sinh ra vĩ mô vật chất rất khác.

Pauli nguyên lý giải thích vì sao vật chất không sụp đổ (collapse) thành một orbital duy nhất; Bose thống kê giải thích vì sao nhiều quanta có thể hành xử collectively trong cùng mode (mode). Đây là một trong những cầu nối mạnh nhất từ vi mô (microscopic) lượng tử rules đến properties của vật chất hàng ngày.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Pauli exclusion là lực đẩy giữa hai electron”

Không. Electron vẫn có Coulomb lực đẩy (repulsion), nhưng Pauli exclusion là antisymmetry ràng buộc của trạng thái, không phải lực term trong Hamiltonian.

### “Fermion luôn tránh xa nhau trong không gian”

Không tuyệt đối. Rule cấm cùng complete one-hạt trạng thái; không gian xác suất (probability) còn phụ thuộc spin và các tương tác (interactions). Hai electron opposite spin có thể có mật độ (density) overlap lớn trong cùng orbital.

### “Boson thì không tương tác”

Sai. Boson/fermion classification nói về trao đổi đối xứng, không nói tương tác bằng không. Bosons có thể tương tác mạnh.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Quantum foundations](00_quantum_foundations.md), [Angular momentum & spin](02_angular_momentum_spin.md), [Statistical mechanics](../04_thermal_statistical/01_entropy_statistical_mechanics.md).

**Liên hệ tiếp:** [Atomic Physics](../09_atomic_nuclear_particle/00_atomic_physics.md), [Crystals & bands](../10_condensed_matter_devices/00_crystals_bands.md), [Magnetism & superconductivity](../10_condensed_matter_devices/02_transport_magnetism_superconductivity.md), [Stars & compact objects](../11_astrophysics_cosmology/00_stars_compact_objects.md).
