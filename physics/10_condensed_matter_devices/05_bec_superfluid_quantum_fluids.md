# Ngưng tụ Bose–Einstein, siêu chảy và chất lưu lượng tử

## Khi bước sóng lượng tử trở nên so sánh với khoảng cách giữa các hạt

Bước sóng de Broglie nhiệt có thang

```math
\lambda_{th}
\sim\frac{h}{\sqrt{2\pi mk_BT}}.
```

Ở nhiệt độ cao hoặc mật độ thấp, `\lambda_{th}` nhỏ hơn nhiều khoảng cách trung bình giữa các hạt. Gói sóng của các hạt ít chồng lấn và thống kê Maxwell–Boltzmann cổ điển có thể là xấp xỉ tốt.

Khi nhiệt độ giảm hoặc mật độ tăng, các gói sóng bắt đầu chồng lấn. Với boson, nhiều hạt có thể cùng chiếm một trạng thái lượng tử, mở đường cho **ngưng tụ Bose–Einstein (Bose–Einstein condensation, BEC / 보스-아인슈타인 응축)**.

Đây không phải hiện tượng các hạt “hút nhau rồi tụ thành một cục” trong không gian thực. Nó là hiện tượng thống kê lượng tử trong không gian trạng thái.

## Mật độ pha tới hạn

Với khí Bose lý tưởng đồng nhất 3D, đại lượng

```math
n\lambda_{th}^3
```

đo mức độ suy biến lượng tử.

Khi đại lượng này đạt giá trị bậc 1, chính xác hơn liên hệ với `\zeta(3/2)` trong mô hình khí lý tưởng, các trạng thái kích thích không còn đủ khả năng chứa toàn bộ số hạt theo phân bố Bose–Einstein. Phần hạt dư tích tụ vĩ mô vào trạng thái năng lượng thấp nhất.

Điều kiện này cho thấy vì sao BEC dễ quan sát hơn với hạt nhẹ, nhiệt độ cực thấp và mật độ đủ cao.

## Tham số trật tự vĩ mô

Một condensate yếu tương tác có thể được mô tả bằng hàm sóng vĩ mô

```math
\Psi(\mathbf r)
=\sqrt{n(\mathbf r)}e^{i\phi(\mathbf r)}.
```

Biên độ xác định mật độ, còn pha `\phi` trở thành bậc tự do tập thể.

Vận tốc siêu chảy liên hệ với gradient pha:

```math
\mathbf v_s
=\frac{\hbar}{m}\nabla\phi.
```

Vì curl của gradient bằng 0, dòng siêu chảy lý tưởng là không xoáy cục bộ, ngoại trừ tại các singularity nơi mật độ giảm về 0 và vortex lượng tử có thể tồn tại.

## Phương trình Gross–Pitaevskii

Với khí Bose loãng, lạnh và tương tác yếu, động lực mean-field thường được mô tả bằng

```math
i\hbar\frac{\partial\Psi}{\partial t}
=
\left[
-\frac{\hbar^2}{2m}\nabla^2
+V_{ext}
+g|\Psi|^2
\right]\Psi.
```

Hạng `g|\Psi|^2` mô tả tương tác mean-field giữa các hạt.

Đây là phương trình Schrödinger phi tuyến, nối cơ học lượng tử với:

- sóng phi tuyến;
- hydrodynamics;
- vortex;
- soliton;
- mode tập thể.

Phương trình này không phải lý thuyết chính xác cho mọi chất lưu lượng tử. Nó phù hợp nhất với condensate Bose loãng và tương tác yếu.

## BEC và siêu chảy không phải một khái niệm

Siêu chảy (superfluidity / 초유동) là khả năng tạo dòng có tiêu tán cực thấp cùng các hiện tượng như lượng tử hóa circulation và vortex lượng tử trong điều kiện thích hợp.

BEC và siêu chảy liên hệ chặt nhưng không đồng nhất.

Helium-4 là chất siêu chảy tương tác mạnh và condensate fraction không gần 100%. Trong hệ 2D, trật tự pha có thể tồn tại theo dạng quasi-long-range mà không có BEC 3D thông thường.

Do đó không nên định nghĩa siêu chảy đơn giản là “BEC có độ nhớt bằng 0”.

## Tiêu chuẩn Landau

Một vật chuyển động qua chất siêu chảy chỉ có thể tiêu tán năng lượng bằng cách tạo excitation nếu đồng thời thỏa bảo toàn năng lượng và động lượng.

Từ lập luận này, vận tốc tới hạn lý tưởng là

```math
v_c
=\min_p\frac{\epsilon(p)}{p}.
```

Nếu tốc độ dòng thấp hơn ngưỡng này, một số kênh tạo excitation bị cấm về động học.

Tuy nhiên, vận tốc tới hạn thực nghiệm còn bị giới hạn bởi:

- vortex nucleation;
- biên vật chứa;
- impurity;
- nhiệt độ hữu hạn;
- hình học dòng.

Vì vậy `v_c` của Landau là tiêu chuẩn nền tảng, không phải con số duy nhất cho mọi setup.

## Lượng tử hóa circulation và vortex

Hàm sóng phải đơn trị sau một vòng kín, nên pha phải thay đổi một bội nguyên của `2\pi`:

```math
\oint\nabla\phi\cdot d\mathbf l=2\pi n.
```

Do đó

```math
\oint\mathbf v_s\cdot d\mathbf l
=n\frac{h}{m}.
```

Circulation bị lượng tử hóa.

Vortex lượng tử có lõi nơi mật độ condensate giảm mạnh để pha có thể singular mà hàm sóng vẫn vật lý.

Khi chất siêu chảy quay, nó không tạo phân bố vorticity liên tục như chất lưu cổ điển lý tưởng; nhiều vortex lượng tử có thể sắp thành mạng vortex.

## Helium-4 và chuyển pha lambda

Helium-4 trở thành siêu chảy dưới khoảng `2.17 K` ở áp suất hơi bão hòa.

Nhiệt dung gần chuyển pha có dạng dị thường giống chữ lambda, nên nhiệt độ này thường gọi là lambda point.

Nguyên tử helium-4 là boson, nhưng tương tác giữa chúng mạnh. Vì vậy khí Bose lý tưởng chỉ cung cấp trực giác ban đầu, không phải mô hình định lượng đầy đủ của helium lỏng.

## Mô hình hai chất lưu

Dưới lambda transition, helium-4 thường được mô hình hóa hiện tượng luận bằng hai thành phần:

- thành phần siêu chảy;
- thành phần bình thường mang entropy.

Đây không phải hai chất hóa học khác nhau. Nó là cách phân rã đáp ứng tập thể của cùng chất lỏng.

Dòng ngược giữa hai thành phần tạo các cơ chế truyền nhiệt rất khác chất lưu cổ điển thông thường.

## Helium-3: fermion cũng có thể siêu chảy

Nguyên tử helium-3 là fermion nên không thể đơn giản ngưng tụ từng hạt vào cùng trạng thái như boson.

Ở nhiệt độ thấp hơn nhiều, các fermion có thể bắt cặp thành bậc tự do composite có tính boson rồi tạo pha siêu chảy.

Cấu trúc này có họ hàng khái niệm với cặp Cooper trong siêu dẫn.

Vì vậy nguyên lý Pauli không cấm fermion tham gia một trạng thái siêu chảy; nó thay đổi cơ chế tạo trạng thái tập thể.

## So sánh siêu chảy và siêu dẫn

Chất siêu chảy trung hòa vận chuyển khối lượng. Siêu dẫn vận chuyển điện tích bằng các cặp electron kết hợp.

Cả hai có thể có:

- pha lượng tử vĩ mô;
- lượng tử hóa circulation hoặc từ thông;
- hiệu ứng Josephson;
- excitation tập thể.

Siêu dẫn còn ghép trực tiếp với điện từ trường và thể hiện hiệu ứng Meissner.

Từ thông lượng tử trong siêu dẫn cặp Cooper là

```math
\Phi_0=\frac{h}{2e}.
```

## Hiệu ứng Josephson

Hai condensate kết hợp yếu qua một barrier có dòng phụ thuộc độ lệch pha:

```math
I=I_c\sin\Delta\phi.
```

Trong junction siêu dẫn, điện áp làm pha tiến hóa theo

```math
\frac{d\Delta\phi}{dt}
=\frac{2eV}{\hbar}.
```

Josephson junction là nền tảng của SQUID, chuẩn điện áp và nhiều qubit siêu dẫn.

Hệ nguyên tử trung hòa cũng có hiệu ứng Josephson tương tự về cấu trúc pha.

## Khí nguyên tử siêu lạnh như quantum simulator

Laser cooling, bẫy quang/từ và làm lạnh bay hơi có thể tạo khí nguyên tử siêu lạnh.

Optical lattice tạo thế tuần hoàn có tham số điều chỉnh bằng laser. Nhờ đó thực nghiệm có thể hiện thực các mô hình như Bose–Hubbard và quan sát chuyển pha superfluid–Mott insulator.

Đây là ví dụ mạnh của quantum simulation: thay vì mô phỏng một Hamiltonian khó chỉ bằng máy tính cổ điển, ta xây một hệ lượng tử có Hamiltonian gần tương đương rồi đo trực tiếp hành vi của nó.

## BEC trong bẫy điều hòa

Trong phòng thí nghiệm, nguyên tử thường nằm trong bẫy gần điều hòa thay vì hộp đồng nhất.

Phân bố mật độ là kết quả cạnh tranh giữa:

- động năng lượng tử;
- năng lượng bẫy;
- tương tác giữa hạt.

Khi tắt bẫy và cho đám mây giãn nở, time-of-flight imaging cung cấp thông tin về phân bố động lượng. Condensate thường tạo peak hẹp đặc trưng.

## Bogoliubov excitation và âm thanh

Trong condensate tương tác yếu, excitation Bogoliubov có dispersion gần tuyến tính ở động lượng thấp:

```math
\epsilon(p)\approx c_sp.
```

Ở thang này, excitation giống phonon âm học.

Ở động lượng lớn hơn, dispersion dần trở về dạng gần hạt tự do.

Đây là ví dụ quasiparticle phụ thuộc thang: cùng hệ có thể được mô tả bằng excitation “giống sóng âm” ở năng lượng thấp và “giống hạt” ở năng lượng cao hơn.

## Chuyển pha BKT trong hai chiều

Trong hệ 2D vô hạn với đối xứng liên tục, dao động nhiệt ngăn trật tự dài hạn thông thường ở nhiệt độ hữu hạn.

Tuy nhiên, chuyển pha Berezinskii–Kosterlitz–Thouless (BKT) có thể tạo quasi-long-range order thông qua cơ chế liên kết và tách cặp vortex–antivortex.

Đây là chuyển pha tô pô: cơ chế cốt lõi nằm ở defect và topology, không chỉ ở một tham số trật tự Landau thông thường.

## Liên hệ với hydrodynamics

Viết

```math
\Psi=\sqrt n e^{i\phi}
```

và tách phương trình Gross–Pitaevskii thành phần biên độ và pha cho các phương trình gần dạng:

- phương trình liên tục cho mật độ;
- phương trình Euler có thêm áp suất lượng tử.

Điều này tạo cầu nối trực tiếp giữa hàm sóng lượng tử và cơ học chất lưu.

Ở thang dài, nhiều hệ lượng tử tập thể có thể được mô tả bằng các biến hydrodynamic hiệu dụng thay vì theo dõi từng hạt.

## Miền áp dụng và giới hạn

Khí Bose lý tưởng giải thích điều kiện BEC nhưng không đủ để mô tả đầy đủ siêu chảy tương tác mạnh.

Gross–Pitaevskii là mean-field theory; nó hoạt động tốt với khí Bose loãng, lạnh và tương tác yếu. Gần criticality, trong 1D/2D hoặc với tương tác mạnh, fluctuation lượng tử và nhiệt có thể làm mean-field thất bại.

Tiêu chuẩn Landau không tự tính được mọi cơ chế vortex nucleation hoặc ảnh hưởng biên thực tế.

## Mô hình tư duy (Mental Model)

Chất lưu lượng tử xuất hiện khi các hạt không thể được xem như những đối tượng phân biệt độc lập và toàn hệ phát triển pha lượng tử tập thể ở thang vĩ mô.

Khi đó dòng không chỉ được mô tả bằng trường vận tốc Newton mà còn bởi:

- pha hàm sóng;
- phổ excitation;
- vortex lượng tử;
- topology của pha.

```text
quantum statistics
→ wavefunction overlap
→ collective phase
→ excitation spectrum
→ superfluid flow / vortices / Josephson phenomena
```

## Những ngộ nhận thường gặp (Common Misconceptions)

### “BEC nghĩa tất cả nguyên tử nằm cùng một điểm”

Không. Chúng cùng chiếm một mode lượng tử; hàm sóng không gian của mode có thể trải rộng trên toàn bẫy.

### “Siêu chảy nghĩa độ nhớt bằng đúng 0 cho mọi quá trình”

Không. Hiện tượng tiêu tán phụ thuộc excitation, vortex, biên và thành phần bình thường ở nhiệt độ hữu hạn.

### “Chất siêu chảy không có tương tác”

Sai. Tương tác thường rất quan trọng cho độ ổn định, âm thanh và động lực tập thể.

### “Fermion không thể tạo siêu chảy”

Sai. Fermion có thể bắt cặp để tạo bậc tự do composite và pha siêu chảy hoặc siêu dẫn.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Thống kê lượng tử](../08_quantum/05_identical_particles_quantum_statistics.md), [Hiện tượng tới hạn](../04_thermal_statistical/05_critical_phenomena_renormalization.md), [Phonon và vật chất tô pô](04_phonons_defects_topological_matter.md).

**Liên hệ tiếp:** [Vận chuyển và siêu dẫn](02_transport_magnetism_superconductivity.md), [Berry phase và Hall lượng tử](06_berry_phase_quantum_hall_topology.md), [Phép đo lượng tử](../08_quantum/03_measurement_entanglement_decoherence.md).
