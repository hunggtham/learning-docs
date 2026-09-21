# Information, bit, encoding và representation

Computer không nhận trực tiếp “chữ A”, “màu đỏ”, “số tiền 10000 won” hay “ảnh một con mèo”. Nó nhận các physical states mà hardware có thể phân biệt, rồi software gán quy ước để những state đó đại diện cho information (thông tin / 정보). Vì vậy trước khi học data structure hay network packet, cần hiểu một nguyên tắc: **mọi dữ liệu số đều là representation theo một encoding nào đó**.

## Tại sao bit trở thành đơn vị nền tảng?

Ở mức vật lý, hệ thống số cần phân biệt các trạng thái đủ ổn định trước noise. Hai trạng thái là lựa chọn đơn giản và robust: high/low voltage, charged/not charged, magnetic orientation A/B. Ta trừu tượng hóa chúng thành binary digit — **bit** (비트), nhận giá trị 0 hoặc 1.

Một bit chỉ phân biệt hai khả năng. Với `n` bit, ta có tối đa `2^n` patterns. Đây không phải công thức để học thuộc mà là hệ quả của multiplication principle: mỗi vị trí có 2 lựa chọn độc lập, nên số tổ hợp là `2 × 2 × ... × 2 = 2^n`.

Tám bit thường được nhóm thành một **byte** (바이트). Byte trở thành đơn vị addressable phổ biến trong memory và storage, nhưng byte không mang nghĩa cố định. `01000001` có thể là integer 65 hay ký tự ASCII `A`.

## Encoding là agreement giữa bit pattern và meaning

Encoding (mã hóa biểu diễn / 인코딩) là quy tắc mapping giữa concept ở tầng cao và bit patterns. Nếu sender dùng UTF-8 nhưng receiver diễn giải bytes như EUC-KR, cùng một byte sequence có thể thành ký tự sai. Đây không phải “data bị đổi”; interpretation bị mismatch.

Mental model hữu ích là:

```text
meaning
  ↓ encode
symbol/value
  ↓ representation
bits/bytes
  ↓ physical realization
voltage / charge / magnetic state
```

Khi đọc ngược, hardware/software decode representation để tái tạo symbol/value rồi application gán semantic meaning.

## Text: từ ASCII tới Unicode và UTF-8

ASCII ban đầu gán 7-bit codes cho 128 symbols, đủ cho English letters, digits và control characters. Ví dụ `A = 65 = 0x41`. Khi computer trở thành hệ thống toàn cầu, mỗi khu vực tạo code page riêng; cùng byte có thể mang ký tự khác nhau, gây incompatibility.

Unicode giải quyết ở tầng concept bằng cách gán **code point** cho ký tự. `U+AC00` đại diện `가`, `U+0041` đại diện `A`. Nhưng code point vẫn chưa phải bytes. UTF-8, UTF-16 và UTF-32 là các encoding schemes chuyển code points thành bytes/code units.

UTF-8 có tính chất quan trọng: ASCII giữ nguyên một byte, còn code point khác dùng nhiều byte. Vì vậy `length` của string có thể mơ hồ. Java `String.length()` đếm UTF-16 code units; JavaScript cũng dựa UTF-16; Python 3 thường expose Unicode code points ở tầng language nhưng internal representation có thể tối ưu. Một emoji có thể gồm nhiều code points vì variation selector hoặc zero-width joiner. Do đó “số bytes”, “số code units”, “số code points” và “số grapheme clusters người dùng nhìn thấy” không luôn giống nhau.

Đây là ví dụ điển hình cho abstraction leak: UI muốn cắt “10 ký tự” nhưng nếu implementation cắt tùy tiện theo byte có thể phá encoding.

## Image và audio: sampling + quantization

Một ảnh raster là lưới samples. Mỗi pixel chứa values như RGB. Nếu mỗi channel dùng 8 bit, một pixel RGB thường cần 24 bit trước compression. Nhưng màu thực tế liên tục hơn nhiều; digital image phải **quantize** (양자화 / lượng tử hóa) thành số mức hữu hạn.

Audio cũng tương tự. Microphone tạo signal liên tục; analog-to-digital conversion lấy samples theo thời gian và quantize amplitude. Sample rate quyết định tần suất đo; bit depth quyết định số mức amplitude có thể biểu diễn.

Điểm chung là digital representation không “sao chép thế giới thật hoàn hảo”; nó chọn resolution và range đủ cho mục đích, đánh đổi storage/bandwidth với fidelity.

## Structured data cần format ngoài encoding

Giả sử có bytes `31 30 30`. Nếu diễn giải ASCII/UTF-8, đó là chuỗi `100`; nếu muốn integer 100, ta cần parse. Nếu file chứa nhiều fields, ta còn phải biết boundary, type và order. Đây là vai trò của serialization format như JSON, Protocol Buffers, MessagePack hoặc custom binary protocols.

JSON biểu diễn number/text/object bằng text syntax dễ đọc nhưng có overhead. Binary format có thể compact hơn và giữ type chặt hơn, nhưng khó inspect thủ công. Network protocol và storage format luôn phải quyết định cùng loại trade-off.

## Compression: bỏ redundancy chứ không tạo phép màu

Compression (nén / 압축) tận dụng structure và redundancy. Lossless compression cho phép khôi phục chính xác dữ liệu gốc; lossless thường dùng trong source code, database pages hoặc executable. Lossy compression chấp nhận mất một số information ít quan trọng cho mục đích perception, như JPEG hay AAC.

Không phải mọi dữ liệu đều nén được nhiều. Nếu một chuỗi đã gần random, nó có ít redundancy để khai thác. Về information theory, entropy đặt ra giới hạn cho average code length của lossless compression dưới một model xác suất.

Xem thêm: [Information Theory](../../mathematics/07_discrete_cs/06_information_theory_and_coding.md).

## Error detection và correction

Storage và network không tuyệt đối hoàn hảo: bit có thể flip. Ta có thể thêm redundancy có chủ đích để detect/correct lỗi. Parity bit là ví dụ đơn giản: thêm một bit sao cho tổng số 1 theo quy ước là chẵn/lẻ. CRC mạnh hơn cho burst errors trong transmission. ECC memory dùng error-correcting codes để sửa một số lỗi bit.

Điều thú vị là redundancy đôi khi bị loại bỏ để compression, nhưng đôi khi lại được thêm vào để reliability. Mục tiêu khác nhau tạo ra design khác nhau.

## Units: KB, KiB và sự nhầm lẫn thường gặp

Trong SI, `1 kB = 1000 bytes`, `1 MB = 10^6 bytes`. Binary prefixes dùng `1 KiB = 1024 bytes`, `1 MiB = 2^20 bytes`. Memory capacity và OS tools đôi khi dùng cách hiển thị khác nhau, nên cùng ổ đĩa có thể thấy “nhỏ hơn” sau khi format mà thực ra chỉ khác unit convention và filesystem overhead.

Bandwidth thường được quảng cáo bằng bit/s, trong khi file size bằng byte. Link 100 Mbps không có nghĩa tải 100 MB mỗi giây; upper bound trước protocol overhead là khoảng 12.5 MB/s.

## Mental Model

> **Bits không có meaning cố định. Meaning xuất hiện khi một layer áp encoding/schema/protocol lên bit patterns.** Khi dữ liệu “bị sai”, hãy hỏi mismatch nằm ở representation, boundary, type, byte order, character encoding hay semantic interpretation.

## Common Misconceptions

**“Unicode = UTF-8.”** Unicode định nghĩa code points và nhiều quy tắc text; UTF-8 là một encoding của Unicode.

**“Một ký tự luôn là một byte.”** Chỉ đúng với một subset và một số encoding. UTF-8 dùng 1–4 bytes cho một Unicode scalar value; grapheme người dùng thấy còn có thể gồm nhiều code points.

**“Binary chính xác hơn decimal.”** Binary chỉ là base representation. Độ chính xác phụ thuộc type và số bit. Floating-point binary còn không biểu diễn chính xác nhiều decimal fractions như 0.1.

## Kết nối

Bit representation dẫn trực tiếp đến [integer và floating-point representation](./02_numbers_and_machine_representation.md), [digital circuits](../02_computer_architecture/00_digital_logic_and_circuits.md), [serialization](../08_software_systems/04_time_serialization_and_idempotency.md), [network packets](../06_networks_distributed_systems/00_network_layers_packets_and_encapsulation.md) và [storage engines](../05_data_databases/04_storage_logs_recovery_and_durability.md).
