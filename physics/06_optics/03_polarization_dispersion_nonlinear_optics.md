# Phân cực, tán sắc và quang học phi tuyến

## Phân cực cho biết điện trường dao động theo hướng nào

Ánh sáng là sóng điện từ. Với sóng phẳng truyền theo trục `z`, điện trường nằm trong mặt phẳng vuông góc hướng truyền.

Phân cực (polarization / 편광) mô tả quỹ đạo của vectơ điện trường `\mathbf E` theo thời gian tại một điểm.

Nếu hai thành phần có cùng pha,

```math
E_x=A_x\cos\omega t,
```

```math
E_y=A_y\cos\omega t,
```

đầu mút của vectơ `\mathbf E` dao động trên một đường thẳng: phân cực tuyến tính.

Nếu hai biên độ bằng nhau và lệch pha `\pi/2`, đầu mút `\mathbf E` quay trên đường tròn: phân cực tròn.

Trường hợp tổng quát tạo phân cực elip.

Phân cực không phải “hướng photon bay”. Nó mô tả cấu trúc ngang của trường điện từ.

## Vector Jones: đại số tuyến tính của ánh sáng kết hợp

Với ánh sáng đơn sắc và kết hợp hoàn toàn, hai biên độ phức có thể viết thành vector Jones:

```math
\mathbf J=
\begin{pmatrix}
E_x\\
E_y
\end{pmatrix}.
```

Các phần tử quang học trở thành phép biến đổi ma trận.

Ví dụ, polarizer lý tưởng theo trục `x` có thể biểu diễn bằng

```math
P_x=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
```

Quarter-wave plate tạo chênh lệch pha giữa hai thành phần trực giao.

Đây là một ví dụ rõ của đại số tuyến tính trong vật lý: ma trận không chỉ là bảng số mà đại diện phép biến đổi trạng thái ánh sáng.

Jones formalism không phù hợp đầy đủ với ánh sáng phân cực một phần hoặc không kết hợp; khi đó nên dùng Stokes parameters và Mueller matrices.

## Định luật Malus

Nếu ánh sáng phân cực tuyến tính có cường độ `I_0` đi qua analyzer lệch góc `\theta`, biên độ điện trường truyền qua là phép chiếu

```math
E=E_0\cos\theta.
```

Vì cường độ tỉ lệ với bình phương biên độ,

```math
I=I_0\cos^2\theta.
```

Hệ số `\cos^2\theta` vì vậy đến từ hai bước: chiếu biên độ theo `\cos\theta`, sau đó tính dòng năng lượng theo bình phương biên độ.

## Lưỡng chiết: chiết suất phụ thuộc hướng phân cực

Trong môi trường đẳng hướng đơn giản,

```math
\mathbf D=\varepsilon\mathbf E.
```

Trong tinh thể dị hướng, hằng số điện môi là tensor:

```math
\mathbf D=\boldsymbol\varepsilon\mathbf E.
```

Các hướng phân cực khác nhau có thể “thấy” chiết suất khác nhau. Đây là hiện tượng lưỡng chiết (birefringence / 복굴절).

Sau khi truyền qua độ dày `L`, hai thành phần tích lũy độ lệch pha

```math
\Delta\phi
=\frac{2\pi}{\lambda}\Delta n\,L.
```

Nếu

```math
\Delta\phi=\frac{\pi}{2},
```

ta có quarter-wave plate; nếu

```math
\Delta\phi=\pi,
```

ta có half-wave plate.

## Tán sắc: chiết suất phụ thuộc tần số

Trong vật liệu thực,

```math
n=n(\omega).
```

Nguyên nhân là các điện tích liên kết trong vật chất không phản ứng giống nhau ở mọi tần số.

Một mô hình cổ điển đơn giản là dao động tử Lorentz:

```math
m\ddot x+m\gamma\dot x+m\omega_0^2x
=qE_0e^{-i\omega t}.
```

Biên độ và pha đáp ứng phụ thuộc `\omega`. Phân cực tập thể của nhiều dao động tử tạo susceptibility `\chi(\omega)` và chiết suất phụ thuộc tần số.

Lăng kính tách ánh sáng trắng vì các bước sóng khác nhau có chiết suất khác nhau.

## Vận tốc pha và vận tốc nhóm

Vận tốc pha là

```math
v_p=\frac{\omega}{k}.
```

Vận tốc nhóm là

```math
v_g=\frac{d\omega}{dk}.
```

Trong môi trường không tán sắc, hai giá trị có thể bằng nhau. Trong môi trường tán sắc, chúng khác nhau.

Vận tốc nhóm thường mô tả vận tốc bao xung khi xung đủ hẹp phổ và dispersion đủ trơn. Không nên đồng nhất vô điều kiện `v_g` với tốc độ truyền thông tin trong mọi chế độ.

Trong vùng tán sắc dị thường, vận tốc nhóm định nghĩa toán học có thể lớn hơn `c` hoặc âm mà không cho phép mặt trước nhân quả của tín hiệu truyền nhanh hơn ánh sáng.

## Mở rộng xung trong sợi quang

Một xung quang chứa một dải tần số. Nếu vận tốc nhóm phụ thuộc tần số, các thành phần phổ đến đích ở các thời điểm khác nhau, làm xung rộng ra.

Trong truyền thông sợi quang, tán sắc sắc ký giới hạn khoảng cách và tốc độ bit nếu các xung lân cận bắt đầu chồng lên nhau.

Kỹ thuật thực tế dùng kết hợp:

- thiết kế sợi;
- bù tán sắc;
- điều chế phù hợp;
- xử lý tín hiệu số.

Đây là cầu nối trực tiếp từ đáp ứng điện từ của vật liệu tới hạ tầng truyền thông Internet.

## Stokes parameters: khi Jones vector không còn đủ

Ánh sáng thực có thể chỉ phân cực một phần. Khi đó Jones vector không đủ vì nó giả sử một biên độ phức xác định hoàn toàn.

Ta có thể dùng bốn tham số Stokes `S_0,S_1,S_2,S_3`:

- `S_0` biểu diễn tổng cường độ;
- các tham số còn lại mô tả ưu thế giữa các cơ sở phân cực tuyến tính và độ thuận tay tròn.

Polarimeter đo cường độ qua nhiều analyzer để tái dựng vector Stokes.

Jones calculus mô tả biên độ trường kết hợp; Stokes/Mueller formalism mô tả tương quan cường độ và phù hợp với hệ phân cực một phần.

## Phân cực phi tuyến của vật chất

Ở trường yếu, phân cực vật liệu thường gần tuyến tính:

```math
P=\varepsilon_0\chi^{(1)}E.
```

Khi trường đủ mạnh,

```math
P=\varepsilon_0\left[
\chi^{(1)}E+
\chi^{(2)}E^2+
\chi^{(3)}E^3+\cdots
\right].
```

Các susceptibility bậc cao tạo nên quang học phi tuyến (nonlinear optics / 비선형 광학).

Ở trường yếu, hạng `\chi^{(1)}` chi phối. Laser cường độ cao làm các hạng bậc hai, ba và cao hơn có thể đo được.

## Phát họa âm bậc hai

Nếu

```math
E=E_0\cos\omega t,
```

thì

```math
E^2
=\frac{E_0^2}{2}(1+\cos2\omega t).
```

Do đó hạng `\chi^{(2)}E^2` chứa thành phần ở tần số `2\omega`.

Phân cực dao động ở `2\omega` có thể phát ánh sáng với tần số gấp đôi nguồn. Đây là phát họa âm bậc hai (second-harmonic generation), được dùng để chuyển laser hồng ngoại sang bước sóng nhìn thấy trong một số hệ.

## Phase matching

Chỉ có thành phần `2\omega` chưa đủ để chuyển đổi hiệu quả.

Các trường được tạo ở những vị trí khác nhau trong tinh thể phải cộng pha thuận lợi. Nếu chúng lệch pha dần, đóng góp từ vùng này có thể triệt tiêu vùng khác.

Điều kiện phase matching bảo đảm quan hệ vector sóng phù hợp, gần dạng

```math
\Delta k=k_{2\omega}-2k_\omega\approx0.
```

Lưỡng chiết hoặc quasi-phase matching có thể được dùng để đạt điều kiện này.

## Hiệu ứng Kerr và self-phase modulation

Susceptibility `\chi^{(3)}` có thể làm chiết suất phụ thuộc cường độ:

```math
n=n_0+n_2I.
```

Nếu cường độ thay đổi theo thời gian trong một xung, pha tích lũy cũng thay đổi theo thời gian. Điều này tạo self-phase modulation và mở rộng phổ.

Kết hợp phi tuyến Kerr với tán sắc có thể tạo soliton trong sợi quang ở điều kiện phù hợp.

## Four-wave mixing và tổng–hiệu tần số

Các hạng phi tuyến có thể ghép nhiều tần số.

Với `\chi^{(2)}`, có thể xuất hiện sum-frequency hoặc difference-frequency generation.

Với `\chi^{(3)}`, four-wave mixing cho phép ba mode quang học ghép để tạo mode thứ tư theo điều kiện bảo toàn năng lượng và phase matching.

Các quá trình này là nền tảng của chuyển đổi tần số, khuếch đại tham số và nhiều nguồn photon lượng tử.

## Đối xứng tinh thể quyết định tensor phi tuyến

Susceptibility bậc cao là tensor. Đối xứng của tinh thể buộc nhiều thành phần tensor bằng 0 hoặc liên hệ với nhau.

Ví dụ, trong môi trường có tâm đối xứng lý tưởng, susceptibility điện bậc hai trong bulk thường triệt tiêu dưới xấp xỉ dipole điện.

Do đó quang học phi tuyến nối trực tiếp với tư duy symmetry: không phải mọi quá trình đều được phép trong mọi vật liệu.

## Phân cực trong màn hình và viễn thám

LCD điều khiển phân cực bằng tinh thể lỏng và polarizer.

Kính râm phân cực giảm chói vì ánh sáng phản xạ từ một số bề mặt ngang có phân cực ưu tiên.

Radar polarimetry và cảm biến vệ tinh dùng đáp ứng phân cực để suy ra hình dạng và hướng của giọt mưa, tinh thể băng, thảm thực vật hoặc bề mặt địa hình.

## Tán sắc, hấp thụ và quan hệ Kramers–Kronig

Gần cộng hưởng vật liệu, dispersion mạnh thường đi cùng hấp thụ đáng kể.

Phần thực và phần ảo của susceptibility không độc lập vì đáp ứng vật liệu phải tuân nhân quả. Chúng liên hệ qua quan hệ Kramers–Kronig.

Điều này giúp giải thích vì sao vùng mà chiết suất thay đổi nhanh theo tần số thường liên hệ với cấu trúc hấp thụ.

## Miền áp dụng và giới hạn

Jones calculus giả sử ánh sáng kết hợp và phân cực hoàn toàn. Với ánh sáng không kết hợp hoặc phân cực một phần phải dùng mô tả thống kê hơn.

Khai triển

```math
P=\varepsilon_0(\chi^{(1)}E+\chi^{(2)}E^2+\cdots)
```

chỉ hữu ích khi đáp ứng có thể biểu diễn bằng chuỗi theo trường. Ở cường độ cực cao, ion hóa, damage, plasma formation hoặc hiệu ứng không nhiễu loạn có thể làm mô hình susceptibility bậc thấp không còn phù hợp.

## Mô hình tư duy (Mental Model)

Phân cực mô tả hình học của vectơ trường. Tán sắc mô tả việc vật liệu phản ứng khác nhau với các tần số khác nhau. Quang học phi tuyến xuất hiện khi trường mạnh đến mức đáp ứng không còn tỉ lệ đơn giản với đầu vào.

Ba chủ đề là ba mặt của một câu hỏi chung:

> vật chất biến đổi biên độ, pha, tần số và phân cực của trường điện từ như thế nào?

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Polarizer là bộ lọc màu”

Không. Polarizer chọn trạng thái phân cực, còn bộ lọc màu chọn dải bước sóng hoặc tần số.

### “Vận tốc nhóm luôn là tốc độ tín hiệu”

Không trong mọi chế độ tán sắc. Nhân quả phải được xét bằng đáp ứng đầy đủ của xung và vật liệu.

### “Quang học phi tuyến nghĩa vật liệu đã bị phá hỏng”

Không. Đáp ứng phi tuyến có thể hoàn toàn thuận nghịch và xuất hiện trước ngưỡng damage.

### “Muốn có second harmonic chỉ cần chiếu laser mạnh”

Không. Hiệu suất còn phụ thuộc tensor `\chi^{(2)}`, đối xứng vật liệu, độ dài tương tác và phase matching.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Sóng Maxwell](../05_electromagnetism/04_maxwell_em_waves.md), [Quang học sóng](01_wave_optics.md), [Trường trong vật chất](../05_electromagnetism/07_fields_in_matter_dielectrics_magnetism.md).

**Liên hệ tiếp:** [Laser và tính kết hợp](02_photons_lasers_coherence.md), [Quang học Fourier](04_fourier_imaging_instrumentation.md), [Đáp ứng tuyến tính và FDT](../04_thermal_statistical/07_linear_response_fluctuation_dissipation.md), [Tín hiệu](../12_experimental_computational/01_signals_sampling_noise.md).
