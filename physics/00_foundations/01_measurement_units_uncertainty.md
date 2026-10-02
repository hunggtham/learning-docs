# Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**. Route đi từ quantity/unit → dimensional analysis → measurement chain → uncertainty propagation → model-data comparison, để con số luôn đi kèm giới hạn tin cậy.

## Phép đo là cầu nối giữa mô hình và thế giới

Vật lý không chỉ xây phương trình; nó phải nối phương trình với đại lượng có thể đo. Một đại lượng vật lý (physical quantity / 물리량) là thuộc tính được định nghĩa đủ rõ để so sánh định lượng, chẳng hạn chiều dài, thời gian, khối lượng, điện tích và nhiệt độ.

Một kết quả đo không chỉ là một con số. Nó phải đi cùng:

- đại lượng đang đo;
- đơn vị;
- quy trình hoặc mô hình đo;
- độ bất định;
- điều kiện đo khi cần.

Viết `5` gần như không có ý nghĩa vật lý. Viết `5.00 ± 0.03 m` đã mang nhiều thông tin hơn: giá trị ước lượng, đơn vị và mức bất định.

> **Chuyển mạch:** Trong **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, **Hệ SI và đại lượng dẫn xuất** tiếp nhận điểm tựa từ **Phép đo là cầu nối giữa mô hình và thế giới** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thứ nguyên: hệ kiểu của phương trình vật lý** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hệ SI và đại lượng dẫn xuất

Hệ SI (International System of Units / 국제단위계) có bảy đơn vị cơ bản:

```text
m, s, kg, A, K, mol, cd
```

Các đơn vị khác được xây từ chúng.

Ví dụ lực có đơn vị

```math
1\,N=1\,kg\cdot m/s^2.
```

Năng lượng có đơn vị

```math
1\,J=1\,N\cdot m
=1\,kg\cdot m^2/s^2.
```

Viết đơn vị dưới dạng cơ bản giúp kiểm tra công thức và hiểu cấu trúc của đại lượng.

> **Chuyển mạch:** Ở chặng này của **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, **Thứ nguyên: hệ kiểu của phương trình vật lý** tiếp nhận điểm tựa từ **Hệ SI và đại lượng dẫn xuất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nguyên tắc đồng nhất thứ nguyên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thứ nguyên: hệ kiểu của phương trình vật lý

Thứ nguyên (dimension / 차원) không phụ thuộc việc ta dùng mét hay centimet.

Ta ký hiệu

```math
[x]=L,
```

```math
[t]=T,
```

```math
[m]=M.
```

Vận tốc có

```math
[v]=LT^{-1},
```

và gia tốc có

```math
[a]=LT^{-2}.
```

Nếu viết

```math
x=v+at,
```

vế trái có thứ nguyên chiều dài, còn cả hai hạng bên phải có thứ nguyên vận tốc. Phương trình chắc chắn sai trước khi ta thay bất kỳ con số nào.

Có thể xem phân tích thứ nguyên giống hệ kiểu (type system / 타입 시스템) trong lập trình: nó không chứng minh thuật toán đúng, nhưng loại được cả một lớp lỗi cấu trúc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, **Nguyên tắc đồng nhất thứ nguyên** tiếp nhận điểm tựa từ **Thứ nguyên: hệ kiểu của phương trình vật lý** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân tích thứ nguyên có thể dự đoán dạng công thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nguyên tắc đồng nhất thứ nguyên

Trong một phương trình vật lý hợp lệ:

1. hai vế phải cùng thứ nguyên;
2. các hạng được cộng hoặc trừ phải cùng thứ nguyên;
3. đối số của `sin`, `cos`, `exp`, `log` phải vô thứ nguyên.

Ví dụ biểu thức

```math
e^{-t/\tau}
```

hợp lệ vì `t/\tau` vô thứ nguyên.

Biểu thức

```math
e^{-3t}
```

chỉ có ý nghĩa nếu hệ số `3` thực ra mang đơn vị nghịch đảo thời gian.

> **Chuyển mạch:** Trong **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, **Phân tích thứ nguyên có thể dự đoán dạng công thức** tiếp nhận điểm tựa từ **Nguyên tắc đồng nhất thứ nguyên** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Accuracy, precision và resolution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân tích thứ nguyên có thể dự đoán dạng công thức

Xét chu kỳ con lắc nhỏ phụ thuộc chiều dài `L` và gia tốc `g`.

Giả sử

```math
T\propto L^ag^b.
```

Thứ nguyên cho

```math
[T]=[L]^a[LT^{-2}]^b
=L^{a+b}T^{-2b}.
```

So sánh số mũ:

```math
-2b=1,
```

```math
a+b=0.
```

suy ra

```math
b=-\frac12,
\qquad
a=\frac12.
```

Do đó

```math
T\propto\sqrt{\frac{L}{g}}.
```

Phân tích thứ nguyên không tìm được hệ số `2\pi`, nhưng loại bỏ rất nhiều dạng sai và cho cấu trúc scaling trước khi giải chi tiết.

> **Chuyển mạch:** Ở chặng này của **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, **Accuracy, precision và resolution** tiếp nhận điểm tựa từ **Phân tích thứ nguyên có thể dự đoán dạng công thức** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sai số ngẫu nhiên và sai số hệ thống** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Accuracy, precision và resolution

Ba khái niệm này khác nhau.

**Độ đúng (accuracy / 정확도)** mô tả kết quả gần giá trị tham chiếu đúng đến đâu.

**Độ chụm (precision / 정밀도)** mô tả các phép đo lặp lại gần nhau đến đâu.

**Độ phân giải (resolution)** là thay đổi nhỏ nhất thiết bị có thể phân biệt hoặc hiển thị.

Một cân có thể hiển thị tới `0.001 kg` nhưng bị lệch chuẩn `0.2 kg`. Khi đó độ phân giải tốt nhưng accuracy kém.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, **Sai số ngẫu nhiên và sai số hệ thống** tiếp nhận điểm tựa từ **Accuracy, precision và resolution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ bất định không phải “sai số đã biết”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sai số ngẫu nhiên và sai số hệ thống

Sai số ngẫu nhiên làm kết quả dao động giữa các lần đo. Lặp phép đo và lấy trung bình có thể giảm bất định (uncertainty / 불확실성) của giá trị trung bình nếu các mẫu đủ độc lập.

Sai số hệ thống làm kết quả bị lệch theo một hướng, ví dụ:

- zero offset;
- quy mô (scale / 규모) factor sai;
- cảm biến phụ thuộc nhiệt độ nhưng không được hiệu chỉnh;
- phương pháp đo bỏ qua một hiệu ứng vật lý.

Lặp lại cùng một phép đo rất nhiều lần không tự loại bỏ systematic độ lệch (bias / 편향).

> **Chuyển mạch:** Trong **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, **Độ bất định không phải “sai số đã biết”** tiếp nhận điểm tựa từ **Sai số ngẫu nhiên và sai số hệ thống** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trung bình và tiêu chuẩn (standard / 표준) lỗi (error / 오류)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ bất định không phải “sai số đã biết”

Ta thường viết

```math
x=\hat x\pm u_x,
```

trong đó `\hat x` là estimate và `u_x` mô tả bất định (uncertainty / 불확실성) theo một quy ước xác định.

Ta thường không biết “giá trị thật” để tính sai số thật sự. bất định (uncertainty / 불확실성) là đánh giá định lượng về phạm vi các giá trị còn phù hợp với dữ liệu, thiết bị và mô hình đo.

Vì vậy báo bất định (uncertainty / 불확실성) luôn cần nói rõ nó là:

- tiêu chuẩn (standard / 표준) bất định (uncertainty / 불확실성);
- tiêu chuẩn (standard / 표준) deviation;
- tiêu chuẩn (standard / 표준) lỗi (error / 오류);
- confidence interval;
- credible interval;
- expanded bất định (uncertainty / 불확실성).

Các khái niệm này không thể thay thế tùy ý cho nhau.

> **Chuyển mạch:** Ở chặng này của **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, **Trung bình và tiêu chuẩn (standard / 표준) lỗi (error / 오류)** tiếp nhận điểm tựa từ **Độ bất định không phải “sai số đã biết”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Truyền độ bất định qua một hàm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trung bình và tiêu chuẩn (standard / 표준) lỗi (error / 오류)

Với `N` phép đo độc lập có tiêu chuẩn (standard / 표준) deviation mẫu `s`, độ bất định thống kê của trung bình thường giảm gần

```math
u_{\bar x}\approx\frac{s}{\sqrt N}.
```

Điều này giải thích tại sao tăng số mẫu giảm noise ngẫu nhiên chậm theo `1/\sqrt N`.

Muốn bất định (uncertainty / 불확실성) thống kê giảm 10 lần thường cần khoảng 100 lần số mẫu, nếu các giả định độc lập và phân bố phù hợp còn đúng.

Nếu các mẫu có tương quan theo thời gian, số mẫu hiệu dụng nhỏ hơn `N`; công thức trên không được dùng máy móc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, **Truyền độ bất định qua một hàm** tiếp nhận điểm tựa từ **Trung bình và tiêu chuẩn (standard / 표준) lỗi (error / 오류)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ví dụ truyền bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Truyền độ bất định qua một hàm

Nếu

```math
y=f(x_1,x_2,\ldots,x_n),
```

và bất định (uncertainty / 불확실성) nhỏ, khai triển Taylor bậc nhất cho

```math
\delta y
\approx
\sum_i
\frac{\partial f}{\partial x_i}\delta x_i.
```

Nếu các biến độc lập,

```math
u_y^2
\approx
\sum_i
\left(
\frac{\partial f}{\partial x_i}
\right)^2u_i^2.
```

Nếu có tương quan, phải thêm covariance:

```math
u_y^2
\approx
\sum_i\sum_j
\frac{\partial f}{\partial x_i}
\frac{\partial f}{\partial x_j}
\operatorname{Cov}(x_i,x_j).
```

Đây là lý do covariance quan trọng trong thí nghiệm chính xác và fitting nhiều tham số.

> **Chuyển mạch:** Trong **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, **Truyền độ bất định qua một hàm** cho ta quy tắc; **Ví dụ truyền bất định (uncertainty / 불확실성)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Chữ số có nghĩa và rounding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ truyền bất định (uncertainty / 불확실성)

Giả sử diện tích hình chữ nhật

```math
A=LW.
```

Với `L,W` độc lập,

```math
\left(\frac{u_A}{A}\right)^2
\approx
\left(\frac{u_L}{L}\right)^2
+
\left(\frac{u_W}{W}\right)^2.
```

Nếu cùng một thước bị quy mô (scale / 규모) lỗi (error / 오류) dùng đo cả `L` và `W`, hai sai số có thể tương quan; bỏ covariance sẽ đánh giá bất định (uncertainty / 불확실성) sai.

> **Chuyển mạch:** Ở chặng này của **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, **Ví dụ truyền bất định (uncertainty / 불확실성)** cho ta quy tắc; **Chữ số có nghĩa và rounding** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Calibration: nối tín hiệu cảm biến với đại lượng vật lý** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chữ số có nghĩa và rounding

Không nên báo nhiều chữ số hơn mức dữ liệu hỗ trợ.

Ví dụ, nếu

```text
x = 12.347891 ± 0.3 m
```

thì các chữ số rất sâu sau dấu phẩy không có ý nghĩa thực nghiệm.

Thông thường bất định (uncertainty / 불확실성) được làm tròn tới một hoặc hai chữ số có nghĩa rồi giá trị estimate được làm tròn tới cùng vị trí thập phân.

Quy tắc cụ thể có thể khác giữa phòng thí nghiệm, nhưng nguyên tắc là không tạo **false precision**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, **Calibration: nối tín hiệu cảm biến với đại lượng vật lý** tiếp nhận điểm tựa từ **Chữ số có nghĩa và rounding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đo lường (measurement / 측정) mô hình (model / 모델) quan trọng ngang thiết bị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Calibration: nối tín hiệu cảm biến với đại lượng vật lý

Cảm biến thường không đo trực tiếp đại lượng cần báo. Nó tạo tín hiệu `s`, rồi dùng mô hình calibration

```math
x=f(s;\theta_{cal}).
```

Các tham số calibration `\theta_{cal}` cũng có bất định (uncertainty / 불확실성).

Ví dụ thermistor tạo điện trở, ADC tạo mã (code / 코드) số, rồi phần mềm chuyển mã (code / 코드) thành nhiệt độ. bất định (uncertainty / 불확실성) cuối cùng gồm cả:

- sensor noise;
- ADC quantization;
- calibration fit;
- drift;
- mô hình (model / 모델) conversion.

Đây là cầu nối trực tiếp giữa Vật lý, electronics và software/dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인).

> **Chuyển mạch:** Trong **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, **Calibration: nối tín hiệu cảm biến với đại lượng vật lý** nêu điều cần giải thích; **Đo lường (measurement / 측정) mô hình (model / 모델) quan trọng ngang thiết bị** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Signal-to-noise ratio và averaging** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đo lường (measurement / 측정) mô hình (model / 모델) quan trọng ngang thiết bị

Một phép đo luôn dựa trên một mô hình.

Ví dụ cân đo lực pháp tuyến rồi chuyển thành “khối lượng” dưới giả định gia tốc trọng trường đã biết và vật không gia tốc theo phương thẳng đứng.

Một camera đo photon qua optics, sensor phản hồi (response / 응답) và xử lý ảnh (image processing / 이미지 처리); điểm ảnh (pixel / 픽셀) giá trị (value / 값) không phải trực tiếp “độ sáng thật của vật”.

Do đó systematic lỗi (error / 오류) thường không chỉ đến từ phần cứng mà còn từ giả định (assumption / 가정) của đo lường (measurement / 측정) mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, **Đo lường (measurement / 측정) mô hình (model / 모델) quan trọng ngang thiết bị** nêu điều cần giải thích; **Signal-to-noise ratio và averaging** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Đơn vị trong phần mềm và dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Signal-to-noise ratio và averaging

Một tín hiệu nhỏ có thể không nhìn rõ trong một mẫu nhưng xuất hiện khi trung bình nhiều lần nếu:

- tín hiệu được đồng bộ;
- nhiễu gần độc lập;
- hệ không drift đáng kể.

Nếu noise có thành phần `1/f`, drift hoặc correlation dài, averaging lâu hơn không nhất thiết tiếp tục cải thiện theo `\sqrt N`.

Đây là lý do cần xem power spectral density và stability theo thời gian chứ không chỉ tiêu chuẩn (standard / 표준) deviation ngắn hạn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, **Signal-to-noise ratio và averaging** nêu điều cần giải thích; **Đơn vị trong phần mềm và dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đơn vị trong phần mềm và dữ liệu

Một bug đơn vị có thể tồn tại dù mọi phép tính số học đều hợp lệ.

Các chiến lược kỹ thuật tốt gồm:

- lưu đơn vị cùng siêu dữ liệu (metadata / 메타데이터);
- dùng SI nội bộ nhất quán;
- đặt tên biến thể hiện đại lượng;
- kiểm tra hợp lệ (validation / 검증) ở API ranh giới (boundary / 경계);
- unit-aware thư viện (library / 라이브러리) nếu phù hợp;
- kiểm thử (test / 테스트) bằng phân tích thứ nguyên.

Một giá trị floating-point không mang ý nghĩa vật lý đầy đủ nếu thiếu đơn vị và quy ước.

> **Chuyển mạch:** Trong **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, các dấu vết trong **Đơn vị trong phần mềm và dữ liệu** được đọc cùng nhau ở **Mô hình tư duy (mental model / 사고 모델)** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Một kết quả đo đáng tin cần cả chuỗi:

```text
physical quantity
→ measurement principle
→ sensor/instrument
→ calibration
→ recorded signal
→ uncertainty model
→ reported value + unit + uncertainty
```

Thứ nguyên kiểm tra lô-gic (logic / 논리) của phương trình; bất định (uncertainty / 불확실성) kiểm tra mức độ dữ liệu thật sự ràng buộc giá trị.

> **Chuyển mạch:** Ở chặng này của **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, **Những ngộ nhận thường gặp (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Nhiều chữ số thập phân nghĩa là đo chính xác”

Không. Display resolution không quyết định accuracy hay bất định (uncertainty / 불확실성) tổng.

### “Đo nhiều lần sẽ loại hết sai số”

Không. Averaging chủ yếu giảm phần ngẫu nhiên; systematic độ lệch (bias / 편향) có thể còn nguyên.

### “bất định (uncertainty / 불확실성) là khoảng chắc chắn chứa giá trị thật”

Ý nghĩa phụ thuộc phương pháp thống kê và quy ước. Confidence interval và credible interval có diễn giải khác nhau.

### “Hai đại lượng bất định (uncertainty / 불확실성) độc lập có thể cộng thẳng”

Không nói chung. Với propagation tuyến tính độc lập, variance thường cộng theo bình phương; nếu tương quan phải thêm covariance.

### “Đơn vị chỉ là nhãn để đổi sau cùng”

Không. Đơn vị là một phần của cấu trúc mô hình và có thể dùng như kiểm tra lô-gic (logic / 논리) ngay từ đầu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đại lượng, đơn vị, thứ nguyên và độ bất định đo lường**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Tư duy Vật lý](00_physical_thinking.md), [Ngôn ngữ Toán học](03_mathematical_language.md).

**Liên hệ tiếp:** [Vật lý thực nghiệm](../12_experimental_computational/00_measurement_experiment.md), [Tín hiệu, nhiễu và lấy mẫu](../12_experimental_computational/01_signals_sampling_noise.md), [Suy luận dữ liệu và bài toán ngược](../12_experimental_computational/03_data_inference_inverse_problems.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
