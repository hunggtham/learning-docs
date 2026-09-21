# Quang sóng: giao thoa, nhiễu xạ, phân cực và giới hạn phân giải

Quang hình học mô tả ánh sáng bằng tia và hoạt động rất tốt khi kích thước đặc trưng của hệ lớn hơn nhiều bước sóng. Khi khẩu độ, khe, chi tiết ảnh hoặc độ chênh đường đi trở nên so sánh được với bước sóng, mô hình tia không còn đủ. Khi đó phải mô tả ánh sáng bằng trường sóng và theo dõi biên độ, pha cùng sự chồng chập.

## Từ Maxwell đến sóng ánh sáng

Trong môi trường đồng nhất, không nguồn và tuyến tính, các phương trình Maxwell dẫn tới phương trình sóng cho điện trường:

```math
\nabla^2\vec E-\frac{1}{v^2}\frac{\partial^2\vec E}{\partial t^2}=0,
```

với

```math
v=\frac{1}{\sqrt{\mu\varepsilon}}.
```

Trong chân không, `v=c`. Một nghiệm phẳng đơn sắc có thể viết dưới dạng phức

```math
\vec E(\mathbf r,t)=\Re\left\{\vec E_0e^{i(\mathbf k\cdot\mathbf r-\omega t)}\right\}.
```

Dùng số phức không làm điện trường “trở thành số phức vật lý”; đây là cách gói biên độ và pha vào cùng một biểu thức. Đại lượng đo được cuối cùng là trường thực hoặc cường độ liên hệ với bình phương biên độ.

## Nguyên lý chồng chập và giao thoa

Trong môi trường tuyến tính, nếu `E_1` và `E_2` đều là nghiệm thì tổng

```math
E=E_1+E_2
```

cũng là nghiệm. Đây là nguyên lý chồng chập (superposition).

Nếu hai sóng cùng tần số có dạng

```math
E_1=E_{01}\cos(\omega t+\phi_1),
```

```math
E_2=E_{02}\cos(\omega t+\phi_2),
```

thì cường độ trung bình của tổng trường có dạng

```math
I=I_1+I_2+2\sqrt{I_1I_2}\cos\Delta\phi,
```

với

```math
\Delta\phi=\phi_2-\phi_1.
```

Hạng cuối là hạng giao thoa. Nó cho thấy cường độ không phải lúc nào cũng chỉ bằng tổng cường độ của từng nguồn; quan hệ pha quyết định hai trường tăng cường hay triệt tiêu nhau.

Nếu hai chùm có cùng cường độ `I_0`, ta được

```math
I=4I_0\cos^2\left(\frac{\Delta\phi}{2}\right).
```

## Độ chênh đường đi và độ lệch pha

Với cùng bước sóng trong cùng môi trường, độ chênh đường đi `\Delta L` tạo độ lệch pha

```math
\Delta\phi=\frac{2\pi}{\lambda}\Delta L.
```

Điều này biến bài toán giao thoa thành bài toán hình học: tìm hai đường đi khác nhau bao nhiêu rồi chuyển phần chênh đó thành pha.

Trong thí nghiệm hai khe Young, ở vùng góc nhỏ, điều kiện cực đại gần là

```math
d\sin\theta=m\lambda,
```

trong đó `d` là khoảng cách hai khe và `m` là số nguyên.

Ở màn cách khe một khoảng `L` với `\theta` nhỏ,

```math
\sin\theta\approx\tan\theta\approx\frac{y}{L},
```

nên vị trí vân sáng xấp xỉ

```math
y_m\approx \frac{m\lambda L}{d}.
```

Do đó khoảng vân

```math
\Delta y\approx\frac{\lambda L}{d}.
```

Các quan hệ này chỉ đúng tốt khi hình học thỏa xấp xỉ góc nhỏ và hai khe đủ hẹp để mỗi khe đóng vai trò nguồn kết hợp thích hợp.

## Độ kết hợp: tại sao không phải hai nguồn bất kỳ đều cho vân ổn định?

Giao thoa quan sát được cần quan hệ pha không bị ngẫu nhiên hóa quá nhanh trong thời gian đo.

Độ kết hợp thời gian (temporal coherence) liên hệ với độ rộng phổ. Một nguồn có độ rộng tần số `\Delta\nu` thường có thời gian kết hợp bậc

```math
\tau_c\sim\frac{1}{\Delta\nu},
```

và độ dài kết hợp

```math
L_c\sim c\tau_c
```

trong chân không.

Độ kết hợp không gian (spatial coherence) mô tả mức tương quan pha giữa các điểm khác nhau trên mặt sóng. Nguồn có kích thước góc lớn thường làm giảm kết hợp không gian tại detector.

Vì vậy laser thường tạo giao thoa ổn định hơn đèn nhiệt không phải đơn giản vì “laser mạnh hơn”, mà vì phổ và cấu trúc không gian của trường có độ kết hợp cao hơn.

## Nhiễu xạ từ nguyên lý Huygens–Fresnel

Nhiễu xạ (diffraction / 회절) xuất hiện khi trường sóng đi qua khẩu độ hoặc gặp vật cản có kích thước không lớn hơn nhiều bước sóng. Có thể hình dung mỗi phần tử nhỏ trên mặt sóng như một nguồn thứ cấp; trường tại điểm quan sát là tổng kết hợp của mọi đóng góp, mỗi đóng góp có pha khác nhau do đường đi khác nhau.

Do đó nhiễu xạ không nên được hiểu như “tia sáng va vào cạnh rồi bị bẻ cong”. Nó là hệ quả tự nhiên của chồng chập sóng trên một miền hữu hạn.

## Nhiễu xạ một khe

Với khe rộng `a`, trong giới hạn Fraunhofer, biên độ trường theo góc có dạng

```math
E(\theta)\propto
\frac{\sin\beta}{\beta},
```

với

```math
\beta=\frac{\pi a\sin\theta}{\lambda}.
```

Do đó cường độ

```math
I(\theta)=I_0\left(\frac{\sin\beta}{\beta}\right)^2.
```

Các cực tiểu xảy ra khi

```math
a\sin\theta=m\lambda,
\qquad m=\pm1,\pm2,\ldots
```

Khi `a` nhỏ hơn, cực tiểu đầu tiên xuất hiện ở góc lớn hơn; chùm nhiễu xạ rộng hơn. Đây là ví dụ trực quan của quan hệ Fourier: trường càng bị giới hạn hẹp trong không gian thì phổ số sóng ngang càng trải rộng.

## Fresnel và Fraunhofer: hai chế độ nhiễu xạ

Trong nhiễu xạ Fresnel, khoảng cách truyền chưa đủ lớn để bỏ qua độ cong pha; hình học nguồn–khẩu độ–màn vẫn ảnh hưởng mạnh đến trường.

Trong nhiễu xạ Fraunhofer, có thể dùng xấp xỉ trường xa (far field), và mẫu nhiễu xạ gần với biến đổi Fourier của hàm khẩu độ.

Một số hệ dùng thấu kính để tạo điều kiện Fraunhofer ngay tại mặt phẳng tiêu cự. Đây là cầu nối trực tiếp sang quang học Fourier và xử lý ảnh.

## Khẩu độ tròn và giới hạn phân giải

Khẩu độ tròn tạo mẫu Airy. Góc tới cực tiểu đầu tiên xấp xỉ

```math
\theta_{min}\approx1.22\frac{\lambda}{D},
```

với `D` là đường kính khẩu độ.

Theo tiêu chuẩn Rayleigh, hai nguồn điểm được xem là vừa phân giải khi cực đại trung tâm của một mẫu gần trùng cực tiểu đầu tiên của mẫu kia. Đây không phải một định luật cơ bản tuyệt đối, mà là tiêu chuẩn thực dụng dựa trên cấu trúc PSF của hệ.

Telescope tăng `D` để cải thiện phân giải góc. Kính hiển vi tăng khẩu độ số (numerical aperture, NA) và dùng bước sóng ngắn để cải thiện phân giải không gian.

Một công thức điển hình là

```math
d\sim\frac{\lambda}{2\,NA},
```

với

```math
NA=n\sin\theta.
```

Tăng độ phóng đại không tự làm tăng độ phân giải. Nếu hệ quang học không truyền được các tần số không gian cao thì phóng lớn ảnh chỉ làm lớn phần mờ đã có.

## PSF, OTF và tần số không gian

Hệ tạo ảnh tuyến tính và bất biến theo dịch chuyển có thể được mô tả bằng hàm đáp ứng điểm (point spread function, PSF):

```math
I_{obs}(x,y)=I_{obj}(x,y)*PSF(x,y).
```

Dấu `*` là phép chập (convolution).

Trong miền Fourier,

```math
\widetilde I_{obs}(k_x,k_y)
=
\widetilde I_{obj}(k_x,k_y)\,OTF(k_x,k_y),
```

trong đó OTF là hàm truyền quang học (optical transfer function). Môđun của OTF được gọi là MTF và cho biết độ tương phản của các cấu trúc ở từng tần số không gian được truyền tốt đến mức nào.

Điều này giải thích tại sao khử mờ bằng phần mềm (deconvolution) không thể phục hồi tùy ý mọi chi tiết: nếu một vùng tần số đã bị hệ quang làm mất hoàn toàn hoặc bị noise lấn át, bài toán nghịch đảo trở nên không xác định hoặc rất nhạy với nhiễu.

## Phân cực từ bản chất ngang của sóng điện từ

Trong sóng điện từ phẳng trong môi trường đẳng hướng, `\vec E`, `\vec B` và hướng truyền vuông góc nhau. Hướng dao động của `\vec E` tạo trạng thái phân cực.

Phân cực tuyến tính là trường hợp đầu mút của vectơ điện trường dao động trên một đường thẳng. Phân cực tròn và elip xuất hiện khi hai thành phần vuông góc có biên độ và pha tương đối phù hợp.

Qua polarizer lý tưởng, định luật Malus cho

```math
I=I_0\cos^2\theta.
```

Polarizer không “xóa một nửa photon theo cơ học cổ điển”; ở mô tả trường cổ điển, nó chiếu điện trường lên trục truyền. Ở mô tả lượng tử, cùng cấu trúc xuất hiện dưới dạng xác suất phép chiếu trạng thái phân cực.

## Tán sắc và vận tốc pha

Chiết suất thường phụ thuộc tần số:

```math
n=n(\omega).
```

Do đó vận tốc pha

```math
v_p=\frac{c}{n(\omega)}
```

cũng phụ thuộc tần số. Một xung gồm nhiều thành phần tần số có thể bị kéo giãn và biến dạng khi các thành phần tích lũy pha khác nhau.

Vận tốc nhóm

```math
v_g=\frac{d\omega}{dk}
```

mô tả chuyển động của bao xung trong nhiều trường hợp, nhưng không nên đồng nhất máy móc với vận tốc truyền thông tin trong mọi môi trường tán sắc mạnh hoặc hấp thụ mạnh. Nhân quả đầy đủ được quyết định bởi đáp ứng vật liệu và phương trình Maxwell.

## Ví dụ định lượng: độ phân giải của telescope

Giả sử telescope có `D=0.20 m` quan sát tại `\lambda=550 nm`.

Giới hạn Rayleigh xấp xỉ

```math
\theta_{min}
\approx
1.22\frac{550\times10^{-9}}{0.20}
\approx3.4\times10^{-6}\,rad.
```

Đổi sang arcsecond:

```math
1\,rad\approx206265\,arcsec,
```

nên

```math
\theta_{min}\approx0.69\,arcsec.
```

Đây là giới hạn nhiễu xạ lý tưởng. Quan sát thật còn chịu khí quyển, sai lệch quang học, rung, detector sampling và signal-to-noise ratio.

## Điều kiện áp dụng và giới hạn mô hình

Các công thức Fraunhofer giả định trường xa hoặc cấu hình quang học tương đương. Công thức `1.22\lambda/D` giả định khẩu độ tròn lý tưởng và ánh sáng gần đơn sắc. Mô hình PSF tuyến tính giả định hệ không bão hòa và đáp ứng không phụ thuộc mạnh vào vị trí. Trong quang học phi tuyến, các nguyên lý cộng trường tuyến tính không còn đủ.

Ở mức photon rất thấp, detector ghi các sự kiện rời rạc, nhưng phân bố xác suất của nhiều sự kiện vẫn tái tạo cấu trúc giao thoa và nhiễu xạ. Vì vậy mô tả lượng tử không loại bỏ quang sóng cổ điển; nó giải thích vì sao trường cổ điển xuất hiện như giới hạn của rất nhiều lượng tử trường.

## Mô hình tư duy (Mental Model)

Quang sóng có thể được tổ chức quanh ba ý: **pha quyết định giao thoa, khẩu độ hữu hạn tạo nhiễu xạ, và hệ quang là một bộ lọc tần số không gian**. Khi nhìn ảnh mờ hay một mẫu vân, hãy hỏi trường đã tích lũy pha thế nào, phần nào của mặt sóng được truyền qua và tần số không gian nào còn tồn tại ở detector.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Nhiễu xạ chỉ xảy ra ở mép vật cản”

Không. Toàn bộ khẩu độ đóng góp vào trường qua chồng chập. Mép chỉ trở nên nổi bật vì nó giới hạn miền tích phân của trường.

### “Phóng đại lớn hơn luôn cho chi tiết tốt hơn”

Không. Độ phân giải bị giới hạn bởi bước sóng, khẩu độ và đáp ứng hệ. Phóng đại có thể chỉ làm lớn một PSF đã mờ.

### “Giao thoa chứng minh ánh sáng chỉ là sóng cổ điển”

Giao thoa là tính chất của biên độ. Trong thí nghiệm photon đơn, từng sự kiện là rời rạc nhưng phân bố nhiều sự kiện vẫn tạo vân giao thoa. Cơ học lượng tử giữ cấu trúc pha nhưng thay đổi cách diễn giải phép đo.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Sóng và Fourier](../02_oscillations_waves/01_waves_fourier_sound.md), [Maxwell và sóng điện từ](../05_electromagnetism/04_maxwell_em_waves.md).

**Liên hệ tiếp:** [Photon, coherence và laser](02_photons_lasers_coherence.md), [Quang học Fourier và thiết bị](04_fourier_imaging_instrumentation.md).