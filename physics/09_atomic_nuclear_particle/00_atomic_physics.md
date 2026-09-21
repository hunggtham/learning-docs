# Vật lý nguyên tử: hydro, số lượng tử, cấu trúc tinh tế và quang phổ học

## Nguyên tử không phải “hệ Mặt Trời tí hon”

Mô hình hành tinh của nguyên tử có giá trị lịch sử nhưng không phải mô tả đúng theo cơ học lượng tử. Electron không chạy trên một quỹ đạo cổ điển xác định quanh hạt nhân. Trạng thái electron được mô tả bằng hàm sóng hoặc vectơ trạng thái trong không gian Hilbert.

Các mức năng lượng rời rạc, orbital, spin và quy tắc chọn đều xuất hiện từ cấu trúc lượng tử của Hamiltonian và đối xứng của hệ.

## Nguyên tử hydro

Hydro gồm một proton và một electron tương tác qua thế Coulomb:

```math
V(r)=-\frac{e^2}{4\pi\varepsilon_0r}.
```

Sau khi tách chuyển động tâm khối, bài toán tương đối dùng khối lượng rút gọn

```math
\mu=\frac{m_em_p}{m_e+m_p}.
```

Các mức năng lượng liên kết gần

```math
E_n=-\frac{13.6\,eV}{n^2},
```

với `n=1,2,...`.

Chính xác hơn, hệ số `13.6 eV` đã chứa khối lượng rút gọn thay vì xem proton hoàn toàn bất động.

## Vì sao nguyên tử có kích thước hữu hạn?

Nếu electron bị định xứ trong vùng kích thước `r`, nguyên lý bất định gợi ý

```math
p\sim\frac{\hbar}{r}.
```

Động năng có bậc

```math
K\sim\frac{\hbar^2}{2mr^2},
```

còn thế Coulomb có bậc

```math
V\sim-\frac{e^2}{4\pi\varepsilon_0r}.
```

Khi `r` giảm, thế năng hút giảm theo `1/r`, nhưng chi phí động năng tăng nhanh hơn theo `1/r^2`. Cực tiểu của tổng năng lượng tạo một thang chiều dài tự nhiên là bán kính Bohr:

```math
a_0=\frac{4\pi\varepsilon_0\hbar^2}{\mu e^2}.
```

Do đó nguyên tử ổn định không phải vì electron “quay đủ nhanh để không rơi vào hạt nhân”. Nó ổn định vì trạng thái cơ bản của bài toán lượng tử có năng lượng hữu hạn và kích thước hữu hạn.

## Hàm sóng hydro và các số lượng tử

Do thế Coulomb đối xứng cầu, nghiệm tách thành phần bán kính và góc:

```math
\psi_{nlm}(r,\theta,\phi)
=R_{nl}(r)Y_l^m(\theta,\phi).
```

Các số lượng tử có ý nghĩa:

- `n`: số lượng tử chính, liên hệ thang năng lượng và kích thước orbital;
- `l`: mômen động lượng orbital;
- `m_l`: hình chiếu của mômen động lượng orbital;
- `m_s`: hình chiếu spin electron.

Các orbital `s,p,d,f` tương ứng `l=0,1,2,3`.

Hình dạng orbital là cấu trúc không gian của hàm sóng, không phải đường đi của electron.

## Nút của hàm sóng

Các nút là nơi hàm sóng bằng không. Với hydro, số nút tổng liên hệ với `n`, còn nút góc liên hệ với `l`.

Nút xuất hiện do tính chất sóng và điều kiện biên. Electron không bị một “lực đẩy” ra khỏi mặt nút; xác suất đơn giản bằng không tại đó trong trạng thái đang xét.

## Xác suất theo bán kính

Không thể chỉ nhìn `|\psi|^2` tại một điểm để kết luận bán kính nào có xác suất lớn nhất. Xác suất tìm electron trong lớp cầu dày `dr` là

```math
P(r)dr=4\pi r^2|R_{nl}(r)|^2dr
```

cho trạng thái `s` thích hợp. Hệ số `r^2` đến từ thể tích hình học tăng theo bán kính.

## Phổ hydro và công thức Rydberg

Khi nguyên tử chuyển từ mức `n_i` xuống `n_f`, photon có năng lượng

```math
hf=E_{n_i}-E_{n_f}.
```

Do `E_n\propto-1/n^2`, ta thu được công thức Rydberg:

```math
\frac1\lambda
=R_H\left(\frac1{n_f^2}-\frac1{n_i^2}\right).
```

Các dãy phổ như Lyman, Balmer và Paschen tương ứng với những `n_f` khác nhau.

## Nguyên tử nhiều electron

Khi có nhiều electron, Hamiltonian chứa cả tương tác electron–electron:

```math
H=\sum_i\left(\frac{p_i^2}{2m}+V_{nuc}(r_i)\right)
+\sum_{i<j}\frac{e^2}{4\pi\varepsilon_0r_{ij}}.
```

Hạng `1/r_{ij}` làm bài toán không còn tách thành các bài một electron độc lập.

Vì vậy ta thường dùng xấp xỉ trường trung bình, Hartree–Fock hoặc các phương pháp số nhiều hạt.

## Che chắn và điện tích hạt nhân hiệu dụng

Electron lớp trong che chắn một phần điện tích hạt nhân đối với electron lớp ngoài. Electron ở orbital xuyên sâu gần hạt nhân nhiều hơn có thể cảm nhận điện tích hiệu dụng lớn hơn.

Sự khác nhau về độ xuyên sâu làm năng lượng `s,p,d,f` trong nguyên tử nhiều electron không còn suy biến đơn giản theo `n` như hydro.

## Nguyên lý Pauli và bảng tuần hoàn

Electron là fermion nên hàm sóng toàn phần phải phản đối xứng khi trao đổi hai electron giống nhau. Hệ quả là không thể có hai electron trong cùng nguyên tử có cùng toàn bộ bộ số lượng tử.

Kết hợp Pauli, năng lượng orbital, tương tác Coulomb và trao đổi giải thích cấu trúc lớp vỏ và tính tuần hoàn hóa học.

Quy tắc Hund không phải một định luật tách biệt khỏi lượng tử; nó là mô tả gần đúng cho cách hệ giảm năng lượng trong nhiều cấu hình electron cạnh tranh.

## Mômen động lượng toàn phần

Electron có mômen orbital `\vec L` và spin `\vec S`. Trong nhiều nguyên tử nhẹ, chúng ghép thành

```math
\vec J=\vec L+\vec S.
```

Với nhiều electron, ta có thể ghép các `l_i` thành `L`, các `s_i` thành `S`, rồi tạo `J`. Đây là sơ đồ ghép `LS` hoặc Russell–Saunders.

Ở nguyên tử nặng, tương tác spin–orbit mạnh hơn và sơ đồ `jj` có thể phù hợp hơn.

## Cấu trúc tinh tế

Mức hydro lý tưởng chỉ phụ thuộc `n`, nhưng tương đối tính và tương tác spin–orbit tạo cấu trúc tinh tế (fine structure).

Một hạng spin–orbit có dạng định tính

```math
H_{SO}\propto \vec L\cdot\vec S.
```

Nó làm mức năng lượng phụ thuộc `j`, từ đó tách các vạch phổ vốn trùng nhau trong mô hình phi tương đối tính đơn giản.

## Cấu trúc siêu tinh tế

Spin hạt nhân và mômen từ hạt nhân tương tác với electron, tạo cấu trúc siêu tinh tế (hyperfine structure).

Chuyển mức hyperfine nổi tiếng của hydro trung hòa tạo photon bước sóng khoảng `21 cm`. Vạch này là công cụ cực kỳ quan trọng trong thiên văn vô tuyến để lập bản đồ hydro trong thiên hà.

Đây là một cầu nối trực tiếp từ vật lý nguyên tử sang thiên văn quan sát.

## Zeeman và Stark

Trong từ trường ngoài, mức năng lượng tách do tương tác mômen từ với `\vec B`:

```math
\Delta E\sim \mu_B g m_J B.
```

Đây là hiệu ứng Zeeman.

Trong điện trường ngoài, mức năng lượng dịch hoặc tách do hiệu ứng Stark. Cả hai hiệu ứng cung cấp cách đo trường điện/từ và kiểm tra cấu trúc lượng tử của nguyên tử.

## Từ phần tử ma trận tới quy tắc chọn

Xác suất chuyển mức không chỉ phụ thuộc chênh lệch năng lượng. Với tương tác lưỡng cực điện, biên độ chuyển mức liên hệ phần tử ma trận

```math
\langle f|\hat{\vec d}\cdot\vec E|i\rangle.
```

Nếu tích phân này bằng không do đối xứng, chuyển mức lưỡng cực điện bị cấm ở bậc thấp nhất.

Các quy tắc chọn quen thuộc cho lưỡng cực điện gồm gần đúng:

```math
\Delta l=\pm1,
```

```math
\Delta m=0,\pm1.
```

Với spin trong xấp xỉ không relativistic đơn giản,

```math
\Delta S=0.
```

Các quy tắc này không phải “mệnh lệnh tuyệt đối”. Chúng nói rằng một cơ chế cụ thể có phần tử ma trận bằng không. Chuyển mức có thể vẫn xảy ra qua lưỡng cực từ, tứ cực điện hoặc các cơ chế bậc cao hơn nhưng yếu hơn.

## Parity và quy tắc chọn

Đối xứng chẵn–lẻ (parity) của trạng thái là công cụ mạnh để biết phần tử ma trận có bằng không hay không.

Toán tử vị trí `\vec r` có parity lẻ. Vì vậy chuyển mức lưỡng cực điện cần trạng thái đầu và cuối có parity khác nhau.

Cách nhìn bằng đối xứng giúp hiểu quy tắc chọn sâu hơn việc ghi nhớ `\Delta l=\pm1`.

## Cường độ vạch phổ

Vị trí vạch cho chênh lệch năng lượng, nhưng cường độ còn phụ thuộc:

- số hạt ở trạng thái ban đầu;
- phần tử ma trận chuyển mức;
- phân cực của ánh sáng;
- độ suy biến của mức;
- điều kiện nhiệt động hoặc pumping của hệ.

Khái niệm oscillator strength nén độ mạnh của chuyển mức thành một đại lượng tiện dùng trong quang phổ học.

## Độ rộng tự nhiên và thời gian sống

Một trạng thái kích thích có thời gian sống hữu hạn `\tau`, nên năng lượng không hoàn toàn sắc nét. Có quan hệ bậc độ lớn

```math
\Delta E\,\tau\sim\hbar.
```

Do đó thời gian sống ngắn tạo vạch tự nhiên rộng hơn.

Ngoài ra còn có:

- Doppler broadening do phân bố vận tốc nhiệt;
- collisional broadening do va chạm;
- instrumental broadening do thiết bị.

Quan sát một vạch phổ vì vậy luôn là phép chập của nhiều cơ chế vật lý và đáp ứng thiết bị.

## Phân bố Boltzmann và cường độ phổ

Ở cân bằng nhiệt, tỉ số số hạt giữa hai mức gần

```math
\frac{N_2}{N_1}
=\frac{g_2}{g_1}
\exp\left[-\frac{E_2-E_1}{k_BT}\right].
```

Do đó phổ không chỉ cho cấu trúc nguyên tử mà còn có thể cho nhiệt độ và trạng thái kích thích của môi trường.

Trong plasma và thiên văn, phải kết hợp thêm cân bằng ion hóa và các quá trình không cân bằng.

## Ví dụ suy luận từ một vạch phổ

Nếu một vạch quan sát bị dịch tương đối

```math
\frac{\Delta\lambda}{\lambda}\ll1,
```

vận tốc xuyên tâm phi tương đối tính gần

```math
v_r\approx c\frac{\Delta\lambda}{\lambda}.
```

Nếu vạch đồng thời rộng hơn dự kiến từ thiết bị, độ rộng bổ sung có thể chứa thông tin về nhiệt độ hoặc turbulence.

Một vạch phổ vì thế không chỉ “cho biết nguyên tố nào”; nó có thể mang đồng thời thông tin về thành phần, vận tốc, nhiệt độ, mật độ và trường từ.

## Mô hình tư duy (Mental Model)

Cấu trúc nguyên tử là bài toán trị riêng của một Hamiltonian có đối xứng. Phổ là cách quan sát **chênh lệch giữa các trị riêng**, còn cường độ chuyển mức cho biết cách toán tử tương tác nối các trạng thái đó.

Do đó quang phổ học nối ba tầng:

```text
Hamiltonian
→ trạng thái và mức năng lượng
→ phần tử ma trận
→ photon quan sát được
```

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Orbital là quỹ đạo electron”

Không. Orbital là trạng thái lượng tử không gian.

### “Mọi chênh lệch năng lượng đều tạo vạch mạnh”

Không. Phần tử ma trận và quy tắc chọn quyết định xác suất chuyển mức.

### “Forbidden transition nghĩa tuyệt đối không thể xảy ra”

Không. Nó thường chỉ bị cấm đối với cơ chế bậc thấp đang xét.

### “Độ rộng vạch chỉ do thiết bị kém”

Không. Nó còn chứa thông tin về lifetime, nhiệt độ, va chạm và động lực học môi trường.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Nền tảng lượng tử](../08_quantum/00_quantum_foundations.md), [Mômen động lượng và spin](../08_quantum/02_angular_momentum_spin.md), [Động lực học lượng tử và tán xạ](../08_quantum/06_time_dependent_scattering.md).

**Liên hệ tiếp:** [Photon và laser](../06_optics/02_photons_lasers_coherence.md), [Vật lý phân tử](04_molecular_physics.md), [Thiên văn quan sát](../11_astrophysics_cosmology/02_observational_astrophysics_radiative_transfer.md).
