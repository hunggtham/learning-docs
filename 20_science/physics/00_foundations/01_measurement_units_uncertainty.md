# Đại lượng, đơn vị, thứ nguyên và bất định đo lường

## Đại lượng vật lý và phép đo

Đại lượng vật lý (Physical Quantity / 물리량) là một thuộc tính được định nghĩa sao cho có thể so sánh định lượng. Chiều dài, thời gian, khối lượng, điện tích và nhiệt độ là những ví dụ. Một đại lượng không chỉ là con số; nó luôn gắn với đơn vị và quy trình đo.

Viết “5” không nói gì về chiều dài. Viết “5 m” nói rằng độ dài đang xét bằng năm lần đơn vị chuẩn mét. Điều này tưởng như hiển nhiên nhưng cực kỳ quan trọng: phương trình vật lý chỉ có ý nghĩa nếu hai vế tương thích về thứ nguyên.

### Đơn vị SI

Hệ SI (International System of Units / 국제단위계, SI 단위계) chọn bảy đơn vị cơ bản. Phần lớn Vật lý cơ bản dựa nhiều nhất vào mét `m`, giây `s`, kilogram `kg`, ampere `A`, kelvin `K`, mole `mol` và candela `cd`.

Các đơn vị phức tạp được xây từ đơn vị cơ bản. Ví dụ lực có đơn vị newton:

```math
1\,N = 1\,kg\cdot m/s^2
```

Điều này không chỉ là quy ước ký hiệu. Nó cho biết lực có cấu trúc thứ nguyên bằng khối lượng nhân với gia tốc.

## Phân tích thứ nguyên

Thứ nguyên (Dimension / 차원) cho biết loại đại lượng độc lập với đơn vị cụ thể. Chiều dài có thứ nguyên `[L]`, thời gian `[T]`, khối lượng `[M]`.

Ví dụ vận tốc:

```math
[v] = \frac{L}{T}
```

Gia tốc:

```math
[a] = \frac{L}{T^2}
```

Nếu ai đó viết:

```math
x = v + at
```

thì phương trình sai về thứ nguyên: `x` có thứ nguyên chiều dài, còn `v` và `at` đều có thứ nguyên vận tốc. Chỉ cần kiểm tra thứ nguyên đã bắt được lỗi mà chưa cần biết bài toán cụ thể.

Trong Software Engineering, type system ngăn việc cộng `LocalDate` với một `UserId`. Phân tích thứ nguyên đóng vai trò tương tự cho phương trình vật lý: nó là một “type system” cho đại lượng đo.

## Độ chính xác, độ đúng và sai số

Phép đo không bao giờ cho ta một số tuyệt đối hoàn hảo. Độ đúng (Accuracy / 정확도) nói kết quả gần giá trị thực đến đâu. Độ chụm (Precision / 정밀도) nói các phép đo lặp lại gần nhau đến đâu.

Nếu một cân luôn chỉ nặng hơn thực tế 0.5 kg, các lần đo có thể rất chụm nhưng không đúng. Đây là sai số hệ thống (Systematic Error / 계통오차). Nếu mỗi lần cân dao động nhẹ do nhiễu, đó là sai số ngẫu nhiên (Random Error / 우연오차).

Ta thường biểu diễn:

```math
x = x_0 \pm \Delta x
```

trong đó `x_0` là giá trị ước lượng và `\Delta x` biểu diễn độ bất định (Uncertainty / 불확도).

Ý nghĩa sâu hơn là mọi dữ liệu thực nghiệm đều là một phân bố khả dĩ chứ không phải một điểm hoàn hảo. Đây là cầu nối trực tiếp sang Statistics và Data Science: mô hình không chỉ phải khớp với giá trị trung bình mà còn phải tính đến noise, confidence và bias của hệ đo.

## Mental Model

Một con số chỉ trở thành dữ liệu vật lý khi biết nó đo đại lượng gì, theo đơn vị nào và với mức bất định nào. Thứ nguyên là lớp kiểm tra logic đầu tiên: phương trình vật lý có thể sai về hệ số, nhưng không thể đúng nếu hai vế không cùng dimension.

## Common Misconceptions

Số chữ số sau dấu phẩy không tự động làm phép đo “chính xác hơn”. Precision của thiết bị, calibration, systematic error và uncertainty mới quyết định mức tin cậy của kết quả.

## Knowledge Connection

**Nên hiểu trước:** [Tư duy Vật lý](00_physical_thinking.md).

**Liên hệ tiếp:** [Vật lý thực nghiệm](../12_experimental_computational/00_measurement_experiment.md).
