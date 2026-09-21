# Quang học Fourier, giới hạn nhiễu xạ và hệ tạo ảnh

Quang hình học mô tả tia sáng và rất hữu ích khi bước sóng nhỏ hơn nhiều kích thước cấu trúc. Nhưng độ phân giải, nhiễu xạ, lọc không gian và chất lượng ảnh không thể hiểu đầy đủ chỉ bằng tia sáng. Ở đây ta cần nhìn trường quang học như một tổng của các thành phần tần số không gian.

Quang học Fourier (Fourier optics / 푸리에 광학) là cầu nối giữa quang học sóng, xử lý tín hiệu và hệ tạo ảnh.

## Tần số không gian là gì?

Một ảnh có vùng sáng tối thay đổi chậm theo vị trí chứa thành phần tần số không gian thấp. Các sọc rất mịn hoặc cạnh sắc chứa thành phần tần số không gian cao.

Một trường một chiều có thể viết dưới dạng

```math
U(x)
=\int \tilde U(k_x)e^{ik_xx}\,dk_x.
```

Mỗi thành phần `k_x` tương ứng với một sóng phẳng có hướng truyền khác nhau. Nhờ đó một ảnh phức tạp được phân rã thành những “mode không gian” đơn giản.

## Nhiễu xạ Fraunhofer và biến đổi Fourier

Trong miền xa hoặc trong mặt phẳng tiêu của thấu kính dưới xấp xỉ thích hợp, biên độ nhiễu xạ gần tỉ lệ với biến đổi Fourier của hàm khẩu độ.

Với khe đơn rộng `a`, cường độ theo góc có dạng

```math
I(\theta)
\propto
\left(\frac{\sin\beta}{\beta}\right)^2,
```

với

```math
\beta=\frac{\pi a\sin\theta}{\lambda}.
```

Khe càng hẹp, vân nhiễu xạ càng rộng. Đây là đánh đổi Fourier: định xứ mạnh trong không gian làm phổ góc hoặc phổ tần số không gian rộng hơn.

## Thấu kính như bộ biến đổi Fourier

Trong xấp xỉ paraxial, một thấu kính hội tụ không chỉ “bẻ tia về tiêu điểm”. Nó ánh xạ các thành phần góc khác nhau của trường tới các vị trí khác nhau trong mặt phẳng tiêu.

Một sóng phẳng có góc truyền khác nhau sẽ hội tụ tại vị trí khác nhau. Vì góc truyền liên hệ với tần số không gian, mặt phẳng tiêu sau của thấu kính có thể được xem gần như một mặt phẳng Fourier.

Điều này cho phép thực hiện **lọc không gian quang học** bằng cách đặt khẩu độ hoặc mặt nạ tại mặt phẳng Fourier.

## Hàm truyền của hệ tạo ảnh

Một hệ tuyến tính bất biến theo dịch chuyển có thể được mô tả bằng **hàm đáp ứng điểm (point-spread function, PSF)** `h(x,y)`.

Nếu vật có phân bố cường độ `o(x,y)`, ảnh lý tưởng hóa là

```math
i(x,y)=o*h,
```

trong đó `*` là phép chập.

Trong miền Fourier,

```math
I(k_x,k_y)
=O(k_x,k_y)H(k_x,k_y).
```

`H` là **hàm truyền quang học (optical transfer function, OTF)**.

Điều này cho thấy hệ tạo ảnh hoạt động giống một bộ lọc: một số tần số không gian được truyền tốt, một số bị suy giảm hoặc mất hoàn toàn.

## MTF và “độ nét”

Môđun của OTF được gọi là **hàm truyền điều biến (modulation transfer function, MTF)**.

MTF cho biết độ tương phản của các mẫu ở tần số không gian khác nhau được bảo toàn đến mức nào. Một hệ có thể tái tạo tốt các cấu trúc lớn nhưng làm mờ các chi tiết nhỏ nếu MTF giảm mạnh ở tần số cao.

Vì vậy độ nét không nên chỉ mô tả bằng “số megapixel”. Cảm biến, thấu kính, nhiễu xạ, rung, lấy mẫu và xử lý số cùng quyết định thông tin thực sự được giữ lại.

## Đĩa Airy và giới hạn nhiễu xạ

Khẩu độ tròn không tạo ảnh của một điểm thành một điểm toán học. Nó tạo **mẫu Airy (Airy pattern)**.

Góc tới cực tiểu đầu tiên gần

```math
\theta\approx1.22\frac{\lambda}{D},
```

trong đó `D` là đường kính khẩu độ.

Khẩu độ lớn hơn làm mẫu Airy hẹp hơn và tăng khả năng phân giải góc. Đây là lý do kính thiên văn đường kính lớn có thể phân biệt các nguồn gần nhau tốt hơn.

## Tiêu chuẩn Rayleigh

Hai nguồn điểm thường được coi là vừa phân giải được theo tiêu chuẩn Rayleigh khi cực đại của một mẫu Airy gần với cực tiểu đầu tiên của mẫu kia.

Khoảng phân giải góc gần

```math
\theta_R\approx1.22\frac{\lambda}{D}.
```

Đây không phải một biên tuyệt đối của thông tin trong mọi bài toán. Với mô hình nguồn, SNR cao và thuật toán suy luận phù hợp, ta có thể ước lượng vị trí nguồn với độ chính xác tốt hơn độ rộng PSF. Nhưng khả năng tái tạo cấu trúc tùy ý vẫn bị giới hạn mạnh bởi băng thông quang học và nhiễu.

## Kính hiển vi và khẩu độ số

Trong kính hiển vi, độ phân giải Abbe có bậc

```math
d\approx\frac{\lambda}{2NA},
```

với

```math
NA=n\sin\theta_{max}.
```

Tăng `NA` cho phép thu các thành phần góc lớn hơn, tương ứng giữ được tần số không gian cao hơn.

Dầu nhúng có chiết suất lớn giúp tăng `NA`, vì vậy có thể cải thiện độ phân giải mà không chỉ dựa vào tăng độ phóng đại.

## Phóng đại không đồng nghĩa với phân giải

Nếu ảnh quang học đã mất các tần số không gian cao do nhiễu xạ, phóng to ảnh sau đó không thể tự tạo lại thông tin đó.

Đây là phân biệt quan trọng:

```text
magnification = làm ảnh lớn hơn
resolution = phân biệt được chi tiết gần nhau đến đâu
```

“Zoom số” chủ yếu nội suy điểm ảnh; nó không tương đương việc tăng khẩu độ hoặc thu thêm thông tin quang học.

## Sampling của cảm biến ảnh

Sau khi quang học tạo ảnh trên sensor, ảnh liên tục được lấy mẫu bởi pixel. Khoảng cách pixel `p` đặt ra tần số Nyquist không gian gần

```math
f_N\sim\frac{1}{2p}.
```

Nếu hệ quang truyền tần số cao hơn mức cảm biến có thể lấy mẫu, aliasing và moiré có thể xuất hiện.

Do đó thiết kế camera phải ghép hợp lý MTF của thấu kính, kích thước pixel và bộ lọc chống aliasing nếu cần.

## Deconvolution

Nếu biết PSF `h`, ta có thể cố khôi phục vật `o` từ ảnh quan sát `i`.

Trong miền Fourier, ý tưởng đơn giản là

```math
O\approx\frac{I}{H}.
```

Nhưng nếu `H` rất nhỏ ở một tần số, phép chia khuếch đại nhiễu mạnh. Vì vậy deconvolution thực tế cần regularization, mô hình nhiễu hoặc phương pháp Bayes.

Đây là ví dụ điển hình của bài toán ngược: khôi phục nguồn từ dữ liệu đã bị hệ đo làm mờ và thêm nhiễu.

## Aberration và phase

Một thấu kính thật không chỉ làm giảm biên độ tần số cao; nó còn có thể làm sai pha do quang sai như spherical aberration, coma và astigmatism.

Trong ngôn ngữ Fourier, quang sai làm thay đổi hàm pupil phức và từ đó thay đổi PSF cùng OTF.

Điều này cho thấy “hình ảnh bị mờ” có thể đến từ nhiều cơ chế: nhiễu xạ, defocus, quang sai, chuyển động hoặc sampling.

## Coherent và incoherent imaging

Với nguồn kết hợp (coherent), trường phức được cộng trước rồi mới lấy cường độ. Với nguồn không kết hợp (incoherent), cường độ từ các điểm nguồn được cộng.

Hai trường hợp có hàm truyền khác nhau. Vì vậy không thể luôn dùng cùng một công thức PSF/OTF mà bỏ qua tính kết hợp của nguồn.

Laser microscopy và imaging với ánh sáng trắng có thể có hành vi rất khác dù dùng cùng hệ thấu kính.

## Spatial filtering

Tại mặt phẳng Fourier, vùng gần tâm tương ứng tần số không gian thấp; vùng xa hơn tương ứng chi tiết nhỏ và cạnh sắc.

Chặn tần số cao tạo lọc thông thấp và làm ảnh mượt hơn. Chặn tần số thấp có thể nhấn mạnh cạnh và biến thiên nhanh.

Thí nghiệm lọc không gian quang học cho thấy nhiều thao tác quen thuộc trong xử lý ảnh số có thể được thực hiện trực tiếp bằng lan truyền sóng và thấu kính.

## Liên hệ với thị giác máy tính

Trong thị giác máy tính, convolution kernel phát hiện cạnh, làm mờ hoặc lọc tần số. Trong quang học, PSF của hệ cũng thực hiện phép convolution trước khi photon tới sensor.

Do đó pipeline hình ảnh thực tế là

```text
cảnh thật
→ lan truyền ánh sáng
→ thấu kính + khẩu độ + quang sai
→ PSF/OTF
→ cảm biến lấy mẫu
→ nhiễu và ADC
→ xử lý ảnh số
```

Mô hình AI chỉ nhìn thấy dữ liệu ở cuối chuỗi này; hiểu vật lý cảm biến giúp phân biệt đặc trưng của thế giới với artifact của hệ đo.

## Mô hình tư duy (Mental Model)

Một hệ tạo ảnh là một **kênh truyền thông tin không gian**. Khẩu độ và bước sóng giới hạn băng thông; PSF mô tả ảnh của một điểm; OTF/MTF cho biết tần số không gian nào sống sót qua hệ; sensor tiếp tục lấy mẫu và thêm nhiễu.

Độ phân giải vì vậy không phải một con số độc lập của thấu kính hay sensor mà là kết quả của toàn hệ.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Tăng độ phóng đại luôn cho thêm chi tiết”

Không. Nếu hệ đã bị giới hạn bởi nhiễu xạ hoặc lấy mẫu, phóng to chỉ làm chi tiết đã có lớn hơn.

### “Ảnh của một điểm lý tưởng vẫn là một pixel”

Không. Trước khi tới sensor, khẩu độ đã biến nguồn điểm thành PSF có kích thước hữu hạn.

### “Sharpen bằng phần mềm có thể phục hồi mọi chi tiết”

Không. Nếu hàm truyền bằng gần không ở một dải tần số và dữ liệu bị chìm trong nhiễu, thông tin đó không thể được tái tạo duy nhất nếu không thêm giả định hoặc prior.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Quang học sóng](01_wave_optics.md), [Sóng và Fourier](../02_oscillations_waves/01_waves_fourier_sound.md).

**Liên hệ tiếp:** [Tín hiệu, nhiễu và lấy mẫu](../12_experimental_computational/01_signals_sampling_noise.md), [Vật lý tính toán và bài toán ngược](../12_experimental_computational/02_computational_physics.md).
