# Thông tin, bit, mã hóa và biểu diễn

Máy tính không nhận trực tiếp “chữ A”, “màu đỏ”, “số tiền 10000 won” hay “ảnh một con mèo”. Nó nhận các **trạng thái vật lý (physical state)** mà phần cứng có thể phân biệt, sau đó phần mềm áp dụng quy ước để các trạng thái đó đại diện cho thông tin (information / 정보). Vì vậy, trước khi học cấu trúc dữ liệu hay gói tin mạng, cần hiểu một nguyên tắc nền tảng: **mọi dữ liệu số đều là một cách biểu diễn (representation) theo một quy tắc mã hóa (encoding)**.

## Tại sao bit trở thành đơn vị nền tảng?

Ở mức vật lý, hệ thống số cần phân biệt các trạng thái đủ ổn định trước nhiễu (noise). Hai trạng thái là lựa chọn đơn giản và bền vững: điện áp cao/thấp, có điện tích/không có điện tích hoặc hai hướng từ hóa khác nhau. Ta trừu tượng hóa chúng thành **chữ số nhị phân (binary digit)**, gọi tắt là **bit** (비트), nhận giá trị 0 hoặc 1.

Một bit chỉ phân biệt hai khả năng. Với `n` bit, ta có tối đa `2^n` mẫu bit. Đây là hệ quả của nguyên lý nhân: mỗi vị trí có hai lựa chọn độc lập nên số tổ hợp là `2 × 2 × ... × 2 = 2^n`.

Tám bit thường được nhóm thành một **byte** (바이트). Byte là đơn vị địa chỉ hóa phổ biến trong bộ nhớ và lưu trữ, nhưng bản thân byte không có ý nghĩa cố định. Mẫu `01000001` có thể được hiểu là số nguyên 65 hoặc ký tự ASCII `A`, tùy cách diễn giải.

## Mã hóa là quy ước nối mẫu bit với ý nghĩa

**Mã hóa (encoding / 인코딩)** là quy tắc ánh xạ giữa khái niệm ở tầng cao và mẫu bit ở tầng thấp. Nếu bên gửi dùng UTF-8 nhưng bên nhận diễn giải cùng chuỗi byte theo EUC-KR, kết quả có thể trở thành ký tự sai. Dữ liệu vật lý không nhất thiết đã thay đổi; vấn đề nằm ở cách diễn giải không khớp.

Mô hình tư duy hữu ích là:

```text
ý nghĩa
  ↓ mã hóa
ký hiệu / giá trị
  ↓ biểu diễn
bit / byte
  ↓ hiện thực vật lý
điện áp / điện tích / trạng thái từ
```

Khi đọc theo chiều ngược lại, phần cứng và phần mềm giải mã cách biểu diễn để tái tạo ký hiệu hoặc giá trị, sau đó ứng dụng gán ý nghĩa ngữ nghĩa cho chúng.

## Văn bản: từ ASCII tới Unicode và UTF-8

ASCII ban đầu dùng mã 7 bit cho 128 ký hiệu, đủ cho chữ cái tiếng Anh, chữ số và một số ký tự điều khiển. Ví dụ `A = 65 = 0x41`. Khi máy tính được sử dụng toàn cầu, nhiều khu vực tạo bảng mã riêng; cùng một byte có thể mang ký tự khác nhau và gây bất tương thích.

Unicode giải quyết vấn đề ở tầng khái niệm bằng cách gán **điểm mã (code point)** cho ký tự. `U+AC00` đại diện `가`, còn `U+0041` đại diện `A`. Tuy nhiên, điểm mã chưa phải là byte. UTF-8, UTF-16 và UTF-32 là các **cách mã hóa Unicode (Unicode encoding scheme)** chuyển điểm mã thành byte hoặc đơn vị mã (code unit).

UTF-8 giữ nguyên các ký tự ASCII trong một byte, còn nhiều điểm mã khác dùng nhiều byte. Vì vậy khái niệm “độ dài chuỗi” có thể mang nhiều nghĩa. Java `String.length()` đếm đơn vị mã UTF-16; JavaScript cũng dựa trên UTF-16; Python 3 cung cấp cách làm việc với điểm mã Unicode ở tầng ngôn ngữ nhưng có thể tối ưu biểu diễn bên trong. Một emoji còn có thể gồm nhiều điểm mã do bộ chọn biến thể (variation selector) hoặc ký tự nối không độ rộng (zero-width joiner). Vì thế số byte, số đơn vị mã, số điểm mã và số cụm ký tự người dùng nhìn thấy (grapheme cluster) không phải lúc nào cũng bằng nhau.

Đây là ví dụ điển hình của **rò rỉ trừu tượng (abstraction leak)**: giao diện muốn cắt “10 ký tự”, nhưng nếu phần triển khai cắt tùy tiện theo byte thì có thể phá hỏng chuỗi mã hóa.

## Ảnh và âm thanh: lấy mẫu và lượng tử hóa

Ảnh raster là một lưới các mẫu (sample). Mỗi điểm ảnh chứa các giá trị như RGB. Nếu mỗi kênh dùng 8 bit thì một điểm ảnh RGB thường cần 24 bit trước khi nén. Màu trong thế giới thực biến thiên liên tục, vì vậy ảnh số phải **lượng tử hóa (quantization / 양자화)** thành một số mức hữu hạn.

Âm thanh cũng tương tự. Microphone tạo tín hiệu liên tục; quá trình chuyển đổi tương tự–số lấy mẫu theo thời gian rồi lượng tử hóa biên độ. **Tần số lấy mẫu (sample rate)** quyết định tần suất đo, còn **độ sâu bit (bit depth)** quyết định số mức biên độ có thể biểu diễn.

Điểm chung là biểu diễn số không sao chép thế giới thực một cách hoàn hảo. Hệ thống chọn độ phân giải và miền giá trị phù hợp với mục đích, qua đó đánh đổi dung lượng lưu trữ và băng thông lấy độ trung thực (fidelity).

## Dữ liệu có cấu trúc cần định dạng ngoài mã hóa ký tự

Giả sử ta có các byte `31 30 30`. Nếu diễn giải theo ASCII hoặc UTF-8 thì đó là chuỗi `100`; nếu muốn số nguyên 100 thì chương trình còn phải phân tích chuỗi thành số. Nếu tệp chứa nhiều trường, ta cần biết thêm ranh giới, kiểu và thứ tự của từng trường. Đây là vai trò của **định dạng tuần tự hóa (serialization format)** như JSON, Protocol Buffers, MessagePack hoặc giao thức nhị phân riêng.

JSON biểu diễn số, văn bản và đối tượng bằng cú pháp văn bản dễ đọc nhưng có chi phí phụ. Định dạng nhị phân có thể gọn hơn và giữ kiểu dữ liệu chặt hơn nhưng khó kiểm tra thủ công. Giao thức mạng và định dạng lưu trữ đều phải cân bằng những đặc tính này.

## Nén: loại bỏ dư thừa chứ không tạo phép màu

**Nén (compression / 압축)** khai thác cấu trúc và phần thông tin dư thừa. **Nén không mất dữ liệu (lossless compression)** cho phép khôi phục chính xác dữ liệu gốc và thường được dùng cho mã nguồn, trang cơ sở dữ liệu hoặc tệp thực thi. **Nén mất dữ liệu (lossy compression)** chấp nhận loại bỏ một phần thông tin ít quan trọng đối với mục đích cảm nhận, như JPEG hoặc AAC.

Không phải dữ liệu nào cũng nén được nhiều. Một chuỗi gần ngẫu nhiên có ít dư thừa để khai thác. Trong lý thuyết thông tin, entropy đặt giới hạn cho độ dài mã trung bình của nén không mất dữ liệu dưới một mô hình xác suất nhất định.

Xem thêm: [Lý thuyết thông tin](../../../mathematics/07_discrete_cs/06_information_theory_and_coding.md).

## Phát hiện và sửa lỗi

Lưu trữ và mạng không tuyệt đối hoàn hảo: bit có thể bị lật. Hệ thống có thể thêm phần dư thừa có chủ đích để **phát hiện lỗi (error detection)** hoặc **sửa lỗi (error correction)**. Bit chẵn lẻ (parity bit) là ví dụ đơn giản. CRC mạnh hơn trong việc phát hiện nhiều kiểu lỗi theo cụm khi truyền dữ liệu. Bộ nhớ ECC dùng mã sửa lỗi để sửa một số lỗi bit.

Điều đáng chú ý là phần dư thừa đôi khi bị loại bỏ để nén, nhưng trong trường hợp khác lại được thêm vào để tăng độ tin cậy. Mục tiêu khác nhau dẫn đến thiết kế khác nhau.

## Đơn vị KB, KiB và sự nhầm lẫn thường gặp

Theo SI, `1 kB = 1000 bytes` và `1 MB = 10^6 bytes`. Tiền tố nhị phân dùng `1 KiB = 1024 bytes`, `1 MiB = 2^20 bytes`. Dung lượng bộ nhớ và công cụ hệ điều hành có thể dùng cách hiển thị khác nhau, nên cùng một ổ đĩa có thể trông “nhỏ hơn” sau khi định dạng dù phần chênh lệch chủ yếu đến từ quy ước đơn vị và chi phí của hệ thống tệp.

Băng thông thường được quảng cáo bằng bit/giây, còn kích thước tệp thường tính bằng byte. Đường truyền 100 Mbps không có nghĩa tải được 100 MB mỗi giây; giới hạn lý thuyết trước chi phí giao thức chỉ khoảng 12,5 MB/s.

## Mô hình tư duy

> **Bit không có ý nghĩa cố định. Ý nghĩa xuất hiện khi một tầng áp dụng quy tắc mã hóa, lược đồ hoặc giao thức lên các mẫu bit.** Khi dữ liệu “bị sai”, hãy kiểm tra xem sự không khớp nằm ở cách biểu diễn, ranh giới dữ liệu, kiểu dữ liệu, thứ tự byte, mã hóa ký tự hay cách diễn giải ngữ nghĩa.

## Những hiểu lầm thường gặp

**“Unicode = UTF-8.”** Unicode định nghĩa điểm mã và nhiều quy tắc xử lý văn bản; UTF-8 là một cách mã hóa Unicode.

**“Một ký tự luôn là một byte.”** Điều này chỉ đúng với một số tập ký tự và cách mã hóa. UTF-8 dùng từ 1 đến 4 byte cho một giá trị Unicode; một ký tự mà người dùng nhìn thấy còn có thể gồm nhiều điểm mã.

**“Nhị phân chính xác hơn thập phân.”** Nhị phân chỉ là một cơ số biểu diễn. Độ chính xác phụ thuộc kiểu dữ liệu và số bit. Số dấu phẩy động nhị phân còn không thể biểu diễn chính xác nhiều phân số thập phân như 0,1.

## Kết nối

Biểu diễn bằng bit dẫn trực tiếp đến [biểu diễn số nguyên và số dấu phẩy động](./02_numbers_and_machine_representation.md), [mạch số](../02_computer_architecture/00_digital_logic_and_circuits.md), [tuần tự hóa](../08_software_systems/04_time_serialization_and_idempotency.md), [gói tin mạng](../06_networks_distributed_systems/00_network_layers_packets_and_encapsulation.md) và [bộ máy lưu trữ](../05_data_databases/04_storage_logs_recovery_and_durability.md).