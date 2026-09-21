# Sóng, chồng chập, Fourier và âm thanh

## Từ dao động cục bộ đến sóng

Sóng (Wave / 파동) là một nhiễu động lan truyền trong không gian và thời gian, có thể mang năng lượng và thông tin mà không nhất thiết vận chuyển khối vật chất theo cùng tốc độ với sóng.

Một sóng điều hòa một chiều có thể viết:

```math
\psi(x,t)=A\cos(kx-\omega t+\phi)
```

Trong đó số sóng (wave number / 파수) là:

```math
k=\frac{2\pi}{\lambda}
```

và tần số góc là:

```math
\omega=2\pi f
```

Tốc độ truyền sóng thỏa:

```math
v=\frac{\omega}{k}=f\lambda
```

Quan hệ `v=f\lambda` không có nghĩa tần số tự nó “gây ra” tốc độ truyền. Trong nhiều môi trường, tốc độ sóng chủ yếu do các tính chất của môi trường quyết định. Nếu nguồn thay đổi tần số trong cùng một môi trường, bước sóng thường thay đổi tương ứng.

## Phương trình sóng

Một phương trình sóng (Wave Equation / 파동방정식) cơ bản trong một chiều là:

```math
\frac{\partial^2\psi}{\partial t^2}
=v^2\frac{\partial^2\psi}{\partial x^2}
```

Đạo hàm riêng (Partial Derivative / 편미분) xuất hiện vì trường `\psi` phụ thuộc đồng thời vào vị trí và thời gian.

Phương trình cho biết độ cong theo không gian của trường liên hệ với gia tốc theo thời gian của nó. Trong một môi trường cơ học, biến dạng cục bộ tạo lực lên vùng lân cận; vùng lân cận lại biến dạng và tác động tiếp lên vùng kế tiếp. Cơ chế liên kết cục bộ này khiến nhiễu động lan truyền thành sóng.

## Nguyên lý chồng chập

Nếu phương trình sóng là tuyến tính, tổng của hai nghiệm cũng là một nghiệm:

```math
\psi=\psi_1+\psi_2
```

Nguyên lý chồng chập (Superposition / 중첩) là nền tảng của giao thoa, sóng dừng và phân tích Fourier.

### Giao thoa

Hai sóng cùng pha có thể làm biên độ tổng tăng lên; hai sóng ngược pha có thể triệt tiêu một phần hoặc hoàn toàn tại một vị trí. Trong giao thoa triệt tiêu, năng lượng không biến mất khỏi toàn hệ mà được phân bố lại trong không gian.

## Sóng dừng

Xét hai sóng cùng biên độ và tần số truyền theo hai hướng ngược nhau:

```math
\psi_1=A\cos(kx-\omega t)
```

```math
\psi_2=A\cos(kx+\omega t)
```

Dùng đồng nhất thức lượng giác:

```math
\psi=2A\cos(kx)\cos(\omega t)
```

Ta thu được sóng dừng (Standing Wave / 정상파), với các nút (node / 마디) có biên độ bằng không và các bụng sóng (antinode / 배) có biên độ lớn.

Điều kiện biên chỉ cho phép một số bước sóng hoặc mode nhất định. Đây là một trực giác quan trọng trước khi học lượng tử hóa: ràng buộc hình học và điều kiện biên có thể biến một miền giá trị liên tục thành một phổ mode rời rạc mà chưa cần đến cơ học lượng tử.

## Fourier: biểu diễn tín hiệu phức tạp bằng các mode đơn giản

Phân tích Fourier (Fourier Analysis / 푸리에 해석) cho phép biểu diễn một lớp rất rộng các tín hiệu hoặc trường như tổng của các thành phần sin, cos hoặc số mũ phức có tần số khác nhau.

Đây là một trong những cầu nối mạnh nhất giữa Vật lý và kỹ thuật số. Bộ mã hóa âm thanh, xử lý ảnh, truyền thông, máy phân tích phổ, phép chập, bộ lọc tín hiệu và mô tả hàm sóng lượng tử đều sử dụng tư duy miền tần số.

Biến đổi Fourier rời rạc (Discrete Fourier Transform, DFT) có dạng:

```math
X_k=\sum_{n=0}^{N-1}x_n e^{-i2\pi kn/N}
```

Dạng số mũ phức gọn vì biên độ và pha được mã hóa tự nhiên trong cùng một đại lượng phức.

FFT (Fast Fourier Transform) là nhóm thuật toán tính DFT hiệu quả, thường giảm độ phức tạp từ khoảng `O(N^2)` của phép tính trực tiếp xuống `O(N\log N)`.

## Âm thanh

Âm thanh (Sound / 음파) trong không khí chủ yếu là sóng áp suất dọc (longitudinal pressure wave / 종파). Các phân tử không bay từ loa đến tai người nghe; chúng dao động quanh vị trí cân bằng và truyền nhiễu động cho các phân tử lân cận thông qua lực tương tác và chênh lệch áp suất.

Tốc độ âm thanh phụ thuộc môi trường và trạng thái nhiệt động của môi trường. Trong không khí gần nhiệt độ phòng, giá trị điển hình vào khoảng `343 m/s`.

Cao độ (pitch) liên hệ chủ yếu với tần số. Độ to cảm nhận (loudness) liên hệ với cường độ nhưng còn phụ thuộc đáp ứng của tai người. Âm sắc (timbre) phụ thuộc phổ họa âm, pha và sự biến thiên theo thời gian của bao tín hiệu.

## Decibel và thang logarit

Mức cường độ âm có thể viết:

```math
L=10\log_{10}\left(\frac{I}{I_0}\right)\,dB
```

Thang logarit hữu ích vì cường độ âm trong thực tế trải rộng qua nhiều bậc độ lớn, đồng thời cảm nhận của con người không tuyến tính với cường độ vật lý. Tăng `10 dB` tương ứng cường độ tăng 10 lần, chứ không phải chỉ tăng thêm “10 đơn vị tuyến tính”.

## Hiệu ứng Doppler

Hiệu ứng Doppler (Doppler Effect / 도플러 효과) là sự thay đổi tần số quan sát khi nguồn và người quan sát chuyển động tương đối với nhau.

Đối với âm thanh, môi trường truyền sóng cung cấp một hệ quy chiếu vật lý quan trọng, nên chuyển động của nguồn và chuyển động của người quan sát không hoàn toàn đối xứng trong công thức cổ điển. Đối với ánh sáng trong chân không, hiệu ứng Doppler phải được mô tả bằng thuyết tương đối hẹp.

Radar, siêu âm y khoa và thiên văn học đều khai thác dịch chuyển Doppler để suy ra thành phần vận tốc dọc theo phương quan sát.

## Vận tốc pha và vận tốc nhóm

Trong môi trường tán sắc (dispersive medium / 분산 매질), các thành phần tần số khác nhau có thể truyền với vận tốc pha khác nhau.

Vận tốc pha:

```math
v_p=\frac{\omega}{k}
```

Vận tốc nhóm:

```math
v_g=\frac{d\omega}{dk}
```

Vận tốc nhóm thường mô tả tốc độ lan truyền của bao sóng và, trong nhiều điều kiện thông thường, liên hệ với sự truyền năng lượng hoặc thông tin. Tuy nhiên trong các môi trường tán sắc mạnh hoặc bất thường, không nên đồng nhất máy móc vận tốc nhóm với tốc độ truyền tín hiệu nhân quả.

## Mô hình tư duy (Mental Model)

> Dao động mô tả chuyển động quanh một trạng thái cân bằng. Sóng xuất hiện khi nhiều bậc tự do được liên kết với nhau, khiến nhiễu động ở một nơi tạo thay đổi ở nơi lân cận và tiếp tục lan truyền. Fourier bổ sung một góc nhìn khác: thay vì xem một dạng sóng phức tạp như một hình duy nhất, ta đổi cơ sở và phân tích nó thành tổ hợp của các mode đơn giản.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Sóng luôn mang vật chất từ nguồn tới đích”

Không. Âm thanh, sóng trên dây và nhiều loại sóng nước truyền năng lượng và thông tin chủ yếu nhờ dao động cục bộ của môi trường. Chuyển động thuần của vật chất có thể nhỏ hơn rất nhiều so với quãng đường mà nhiễu động sóng lan truyền.

### “Cộng hưởng chỉ xảy ra khi tần số kích thích đúng tuyệt đối bằng tần số riêng”

Không. Trong một hệ có tắt dần, đáp ứng cộng hưởng có độ rộng hữu hạn. Vị trí đỉnh, biên độ và băng thông phụ thuộc vào mức tắt dần và cách hệ ghép với nguồn kích thích.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Dao động](00_oscillations_resonance.md).

**Liên hệ tiếp:** [Sóng điện từ](../05_electromagnetism/04_maxwell_em_waves.md), [Quang học sóng](../06_optics/01_wave_optics.md).
