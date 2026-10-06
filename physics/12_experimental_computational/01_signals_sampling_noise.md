# Tín hiệu, nhiễu, lấy mẫu, Nyquist và ADC

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Tín hiệu, nhiễu, lấy mẫu, Nyquist và ADC**. Route đi từ signal/noise model → SNR → sampling/aliasing → reconstruction → ADC quantization and limits, để phép đo số giữ được thông tin cần thiết.

## Tỉ số tín hiệu trên nhiễu

Một hệ đo không chỉ nhận tín hiệu mong muốn mà còn nhận các dao động không mong muốn. Tỉ số tín hiệu trên nhiễu (signal-to-noise ratio, SNR / 신호 대 잡음비) so sánh mức của phần tín hiệu hữu ích với mức nhiễu.

Tăng thời gian đo và lấy trung bình có thể cải thiện SNR khi nhiễu gần độc lập giữa các mẫu, chẳng hạn nhiễu trắng (white noise). Tuy nhiên nhiễu `1/f`, độ trôi (drift) và sai số hệ thống có cấu trúc theo thời gian nên không giảm theo cùng quy luật.

Bộ lọc (filter) cũng không tạo ra thông tin từ hư không. Nó chỉ giữ hoặc làm suy giảm các thành phần theo giả định về miền tần số, thời gian hoặc cấu trúc của tín hiệu và nhiễu.

> **Nối mạch:** Trong **Tín hiệu, nhiễu, lấy mẫu, Nyquist và ADC**, **Lấy mẫu và định lý Nyquist** nối từ **Tỉ số tín hiệu trên nhiễu** sang **Vì sao lấy mẫu lại liên quan đến miền tần số?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Lấy mẫu và định lý Nyquist

Một hệ thu nhận số biến tín hiệu liên tục thành dãy mẫu rời rạc theo thời gian. Nếu tần số lấy mẫu là `f_s`, tín hiệu bị giới hạn băng có tần số lớn nhất `f_{max}` chỉ có thể được khôi phục lý tưởng khi

```math
f_s>2f_{max}.
```

Đây là điều kiện Nyquist. Nếu tín hiệu còn thành phần trên tần số Nyquist `f_s/2`, các thành phần đó có thể bị ánh xạ thành tần số thấp giả. Hiện tượng này gọi là chồng phổ do lấy mẫu (aliasing).

Hiệu ứng bánh xe quay ngược trên video, họa tiết moiré trên ảnh số và một số méo âm thanh đều có thể được hiểu từ cùng nguyên lý lấy mẫu.

> **Nối mạch:** Ở chặng này của **Tín hiệu, nhiễu, lấy mẫu, Nyquist và ADC**, **Vì sao lấy mẫu lại liên quan đến miền tần số?** nối từ **Lấy mẫu và định lý Nyquist** sang **Bộ lọc chống chồng phổ**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vì sao lấy mẫu lại liên quan đến miền tần số?

Một tín hiệu có thể được phân tích thành các thành phần tần số bằng biến đổi Fourier (Fourier transform). Lấy mẫu đều trong miền thời gian tạo các bản sao tuần hoàn của phổ trong miền tần số, cách nhau một khoảng `f_s`. Khi các bản sao phổ chồng lên nhau, thông tin của tần số cao trộn với tần số thấp và không thể tách lại chỉ từ dãy mẫu.

Vì bộ lọc thực tế không có biên cắt vô hạn sắc, hệ thống thường lấy mẫu ở tần số cao hơn đáng kể so với `2f_{max}` để dành một vùng chuyển tiếp cho bộ lọc chống chồng phổ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tín hiệu, nhiễu, lấy mẫu, Nyquist và ADC**, **Bộ lọc chống chồng phổ** nối từ **Vì sao lấy mẫu lại liên quan đến miền tần số?** sang **ADC: từ điện áp liên tục thành mã số**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bộ lọc chống chồng phổ

Trước bộ chuyển đổi tương tự–số, một bộ lọc chống chồng phổ (anti-alias filter) thường giới hạn các thành phần tần số cao hơn miền cần đo. Việc này phải thực hiện trước khi lấy mẫu. Sau khi aliasing đã xảy ra, bộ lọc số không thể biết một thành phần tần số thấp quan sát được là tín hiệu thật hay là ảnh giả của một thành phần tần số cao.

> **Nối mạch:** Trong **Tín hiệu, nhiễu, lấy mẫu, Nyquist và ADC**, **ADC: từ điện áp liên tục thành mã số** nối từ **Bộ lọc chống chồng phổ** sang **Nhiễu lượng tử hóa và ENOB**, vì cơ chế trước tạo đầu vào cho bước sau.

## ADC: từ điện áp liên tục thành mã số

Bộ chuyển đổi tương tự–số (analog-to-digital converter, ADC) ánh xạ một khoảng điện áp liên tục thành các mã rời rạc. ADC lý tưởng `N` bit có `2^N` mức mã. Bước lượng tử hóa xấp xỉ

```math
\Delta V\approx\frac{V_{range}}{2^N}.
```

Số bit danh định không đồng nghĩa với số bit thông tin thực sự hữu ích. Nhiễu nhiệt, độ phi tuyến, sai lệch độ lợi, độ ổn định điện áp tham chiếu và độ rung thời gian của xung nhịp đều có thể làm độ phân giải hiệu dụng thấp hơn.

> **Nối mạch:** Ở chặng này của **Tín hiệu, nhiễu, lấy mẫu, Nyquist và ADC**, **Nhiễu lượng tử hóa và ENOB** nối từ **ADC: từ điện áp liên tục thành mã số** sang **Độ rung thời gian của xung lấy mẫu**, vì cơ chế trước tạo đầu vào cho bước sau.

## Nhiễu lượng tử hóa và ENOB

Sai số do làm tròn biên độ về các mức ADC được gọi là sai số lượng tử hóa (quantization error). Trong một số điều kiện, nó có thể được xấp xỉ như nhiễu. Tuy nhiên với tín hiệu tuần hoàn nhỏ hoặc có cấu trúc đặc biệt, sai số lượng tử hóa có thể tương quan với chính tín hiệu.

Số bit hiệu dụng (effective number of bits, ENOB) là một cách mô tả chất lượng thực tế của ADC sau khi tính tới nhiễu và méo. Một ADC 16 bit không nhất thiết cung cấp đủ 16 bit thông tin có ý nghĩa trong mọi điều kiện vận hành.

Đôi khi người ta chủ động thêm một lượng nhiễu nhỏ gọi là dither để phá tương quan giữa tín hiệu và sai số lượng tử hóa. Cách này có thể cải thiện tính tuyến tính thống kê, đổi lại mức nền nhiễu tăng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tín hiệu, nhiễu, lấy mẫu, Nyquist và ADC**, **Độ rung thời gian của xung lấy mẫu** nối từ **Nhiễu lượng tử hóa và ENOB** sang **Decibel và SNR**, vì cơ chế trước tạo đầu vào cho bước sau.

## Độ rung thời gian của xung lấy mẫu

Nếu thời điểm lấy mẫu có độ bất định `\delta t`, sai số điện áp gần đúng là

```math
\delta V\approx\frac{dV}{dt}\delta t.
```

Tín hiệu tần số cao thường có độ dốc lớn hơn, nên cùng một độ rung thời gian (timing jitter) sẽ tạo sai số biên độ lớn hơn. Đây là lý do chất lượng xung nhịp trở thành giới hạn vật lý quan trọng trong các bộ chuyển đổi dữ liệu tốc độ cao.

> **Nối mạch:** Trong **Tín hiệu, nhiễu, lấy mẫu, Nyquist và ADC**, **Decibel và SNR** nối từ **Độ rung thời gian của xung lấy mẫu** sang **Cửa sổ quan sát và rò rỉ phổ**, vì cơ chế trước tạo đầu vào cho bước sau.

## Decibel và SNR

Với tỉ số công suất,

```math
\mathrm{SNR_{dB}}=10\log_{10}\frac{P_s}{P_n}.
```

Nếu so sánh biên độ trong cùng trở kháng, công suất tỉ lệ với bình phương biên độ nên ta dùng

```math
20\log_{10}\frac{A_s}{A_n}.
```

Đơn vị decibel (dB) hữu ích vì nó nén một dải động rất rộng và biến phép nhân độ lợi thành phép cộng. Vì vậy dB xuất hiện phổ biến trong âm thanh, vô tuyến, viễn thông và đo lường điện tử.

> **Nối mạch:** Ở chặng này của **Tín hiệu, nhiễu, lấy mẫu, Nyquist và ADC**, **Cửa sổ quan sát và rò rỉ phổ** nối từ **Decibel và SNR** sang **Liên hệ với phần mềm và hệ thống số**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cửa sổ quan sát và rò rỉ phổ

Trong thực nghiệm, ta chỉ quan sát tín hiệu trong một khoảng thời gian hữu hạn. Việc cắt tín hiệu tương đương với nhân nó với một hàm cửa sổ (window function / 윈도우 함수). Trong miền tần số, phép nhân này trở thành phép chập và có thể làm năng lượng của một tần số lan sang các ô phổ lân cận, gọi là rò rỉ phổ (spectral leakage).

Các ô của FFT không phải “những tần số duy nhất tồn tại trong tự nhiên”. Chúng là cách biểu diễn phụ thuộc độ dài bản ghi, tần số lấy mẫu và loại cửa sổ được chọn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tín hiệu, nhiễu, lấy mẫu, Nyquist và ADC**, **Liên hệ với phần mềm và hệ thống số** nối từ **Cửa sổ quan sát và rò rỉ phổ** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Liên hệ với phần mềm và hệ thống số

Âm thanh số, cảm biến ảnh, vô tuyến định nghĩa bằng phần mềm (software-defined radio) và lớp vật lý của mạng đều bắt đầu từ các ràng buộc lấy mẫu, băng thông, SNR và đồng bộ thời gian. Một lỗi ở tầng ứng dụng có thể hoàn toàn là vấn đề phần mềm; nhưng nếu bit bị sai do nhiễu, phản xạ đường truyền, jitter hoặc thiếu băng thông thì ranh giới giữa phần mềm và phần cứng trở nên rất cụ thể.

> **Nối mạch:** Trong **Tín hiệu, nhiễu, lấy mẫu, Nyquist và ADC**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Liên hệ với phần mềm và hệ thống số** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

Dữ liệu số không xuất hiện trực tiếp trong tự nhiên. Cảm biến biến đại lượng vật lý thành tín hiệu tương tự; mạch lọc giới hạn băng thông; bộ lấy mẫu chọn các thời điểm; ADC lượng tử hóa biên độ; phần mềm mới nhận các số nguyên. Mỗi bước vừa bảo tồn một phần thông tin vừa có khả năng làm mất hoặc làm méo thông tin.

> **Nối mạch:** Ở chặng này của **Tín hiệu, nhiễu, lấy mẫu, Nyquist và ADC**, **Những ngộ nhận thường gặp (Common Misconceptions)** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** mở rộng hệ quả hoặc giới hạn liên quan.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Lấy mẫu đúng gấp đôi tần số lớn nhất luôn là đủ”

Đó là giới hạn lý tưởng cho tín hiệu giới hạn băng. Hệ thực cần vùng chuyển tiếp cho bộ lọc và còn phải xét nhiễu, jitter, độ phi tuyến và yêu cầu tái tạo.

### “Dữ liệu đã thành số thì không còn nhiễu”

Sai. Nhiễu có thể xuất hiện trước ADC, trong quá trình chuyển đổi hoặc sau đó do đồng bộ và truyền dữ liệu. Số hóa chỉ thay đổi cách biểu diễn tín hiệu.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tín hiệu, nhiễu, lấy mẫu, Nyquist và ADC**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Sóng, Fourier và âm thanh](../02_oscillations_waves/01_waves_fourier_sound.md).

**Liên hệ tiếp:** [Mạch điện một chiều](../05_electromagnetism/01_dc_circuits.md), [Vật lý tính toán](02_computational_physics.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
