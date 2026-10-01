# Thông tin (information / 정보), bit, encoding và biểu diễn (representation / 표현)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Thông tin (information / 정보), bit, encoding và biểu diễn (representation / 표현)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tại sao bit trở thành đơn vị nền tảng?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Encoding là agreement giữa bit mẫu (pattern / 패턴) và meaning** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Computer không nhận trực tiếp “chữ A”, “màu đỏ”, “số tiền 10000 won” hay “ảnh một con mèo”. Nó nhận các vật lý (physical / 물리적) states mà hardware có thể phân biệt, rồi software gán quy ước để những trạng thái (state / 상태) đó đại diện cho thông tin (information / 정보). Vì vậy trước khi học cấu trúc dữ liệu (data structure / 자료구조) hay mạng (network / 네트워크) packet, cần hiểu một nguyên tắc: **mọi dữ liệu số đều là biểu diễn (representation / 표현) theo một encoding nào đó**.

## Tại sao bit trở thành đơn vị nền tảng?

Ở mức vật lý, hệ thống số cần phân biệt các trạng thái đủ ổn định trước noise. Hai trạng thái là lựa chọn đơn giản và robust: high/low voltage, charged/not charged, magnetic orientation A/B. Ta trừu tượng hóa chúng thành nhị phân (binary / 이진) digit — **bit** (비트), nhận giá trị 0 hoặc 1.

Một bit chỉ phân biệt hai khả năng. Với `n` bit, ta có tối đa `2^n` patterns. Đây không phải công thức để học thuộc mà là hệ quả của multiplication principle: mỗi vị trí có 2 lựa chọn độc lập, nên số tổ hợp là `2 × 2 × ... × 2 = 2^n`.

Tám bit thường được nhóm thành một **byte** (바이트). Byte trở thành đơn vị addressable phổ biến trong bộ nhớ (memory / 메모리) và lưu trữ (storage / 저장소), nhưng byte không mang nghĩa cố định. `01000001` có thể là integer 65 hay ký tự ASCII `A`.

> **Chuyển mạch:** Trong **Thông tin (information / 정보), bit, encoding và biểu diễn (representation / 표현)**, **Encoding là agreement giữa bit mẫu (pattern / 패턴) và meaning** tiếp nhận điểm tựa từ **Tại sao bit trở thành đơn vị nền tảng?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Văn bản (text / 텍스트): từ ASCII tới Unicode và UTF-8** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Encoding là agreement giữa bit mẫu (pattern / 패턴) và meaning

Encoding (mã hóa biểu diễn / 인코딩) là quy tắc ánh xạ (mapping / 매핑) giữa concept ở tầng cao và bit patterns. Nếu sender dùng UTF-8 nhưng receiver diễn giải bytes như EUC-KR, cùng một byte chuỗi (sequence / 시퀀스) có thể thành ký tự sai. Đây không phải “dữ liệu (data / 데이터) bị đổi”; interpretation bị mismatch.

Mô hình tư duy (mental model / 사고 모델) hữu ích là:

```text
meaning
  ↓ encode
symbol/value
  ↓ representation
bits/bytes
  ↓ physical realization
voltage / charge / magnetic state
```

Khi đọc ngược, hardware/software decode biểu diễn (representation / 표현) để tái tạo symbol/giá trị (value / 값) rồi ứng dụng (application / 애플리케이션) gán ý nghĩa (semantic meaning / 의미적 뜻).

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보), bit, encoding và biểu diễn (representation / 표현)**, **Văn bản (text / 텍스트): từ ASCII tới Unicode và UTF-8** tiếp nhận điểm tựa từ **Encoding là agreement giữa bit mẫu (pattern / 패턴) và meaning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ảnh (image / 이미지) và audio: sampling + quantization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Văn bản (text / 텍스트): từ ASCII tới Unicode và UTF-8

ASCII ban đầu gán 7-bit codes cho 128 symbols, đủ cho English letters, digits và điều khiển (control / 제어) characters. Ví dụ `A = 65 = 0x41`. Khi computer trở thành hệ thống toàn cầu, mỗi khu vực tạo mã (code / 코드) page riêng; cùng byte có thể mang ký tự khác nhau, gây incompatibility.

Unicode giải quyết ở tầng concept bằng cách gán **mã (code / 코드) điểm (point / 지점)** cho ký tự. `U+AC00` đại diện `가`, `U+0041` đại diện `A`. Nhưng mã (code / 코드) điểm (point / 지점) vẫn chưa phải bytes. UTF-8, UTF-16 và UTF-32 là các encoding schemes chuyển mã (code / 코드) points thành bytes/mã (code / 코드) units.

UTF-8 có tính chất quan trọng: ASCII giữ nguyên một byte, còn mã (code / 코드) điểm (point / 지점) khác dùng nhiều byte. Vì vậy `length` của string có thể mơ hồ. Java `String.length()` đếm UTF-16 mã (code / 코드) units; JavaScript cũng dựa UTF-16; Python 3 thường expose Unicode mã (code / 코드) points ở tầng ngôn ngữ (language / 언어) nhưng nội bộ (internal / 내부) biểu diễn (representation / 표현) có thể tối ưu. Một emoji có thể gồm nhiều mã (code / 코드) points vì variation selector hoặc zero-width joiner. Do đó “số bytes”, “số mã (code / 코드) units”, “số mã (code / 코드) points” và “số grapheme clusters người dùng nhìn thấy” không luôn giống nhau.

Đây là ví dụ điển hình cho lớp trừu tượng (abstraction / 추상화) leak: UI muốn cắt “10 ký tự” nhưng nếu hiện thực (implementation / 구현) cắt tùy tiện theo byte có thể phá encoding.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보), bit, encoding và biểu diễn (representation / 표현)**, **Ảnh (image / 이미지) và audio: sampling + quantization** tiếp nhận điểm tựa từ **Văn bản (text / 텍스트): từ ASCII tới Unicode và UTF-8** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Structured dữ liệu (data / 데이터) cần format ngoài encoding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ảnh (image / 이미지) và audio: sampling + quantization

Một ảnh raster là lưới samples. Mỗi điểm ảnh (pixel / 픽셀) chứa values như RGB. Nếu mỗi channel dùng 8 bit, một điểm ảnh (pixel / 픽셀) RGB thường cần 24 bit trước compression. Nhưng màu thực tế liên tục hơn nhiều; digital ảnh (image / 이미지) phải **quantize** (양자화 / lượng tử hóa) thành số mức hữu hạn.

Audio cũng tương tự. Microphone tạo tín hiệu (signal / 신호) liên tục; analog-to-digital conversion lấy samples theo thời gian và quantize amplitude. mẫu (sample / 표본) tỷ lệ (rate / 비율) quyết định tần suất đo; bit độ sâu (depth / 깊이) quyết định số mức amplitude có thể biểu diễn.

Điểm chung là digital biểu diễn (representation / 표현) không “sao chép thế giới thật hoàn hảo”; nó chọn resolution và phạm vi (range / 범위) đủ cho mục đích, đánh đổi lưu trữ (storage / 저장소)/bandwidth với fidelity.

> **Chuyển mạch:** Trong **Thông tin (information / 정보), bit, encoding và biểu diễn (representation / 표현)**, **Ảnh (image / 이미지) và audio: sampling + quantization** nêu điều cần giải thích; **Structured dữ liệu (data / 데이터) cần format ngoài encoding** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Compression: bỏ redundancy chứ không tạo phép màu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Structured dữ liệu (data / 데이터) cần format ngoài encoding

Giả sử có bytes `31 30 30`. Nếu diễn giải ASCII/UTF-8, đó là chuỗi `100`; nếu muốn integer 100, ta cần parse. Nếu tệp (file / 파일) chứa nhiều fields, ta còn phải biết ranh giới (boundary / 경계), kiểu (type / 타입) và thứ tự (order / 순서). Đây là vai trò của serialization format như JSON, giao thức (protocol / 프로토콜) Buffers, MessagePack hoặc custom nhị phân (binary / 이진) protocols.

JSON biểu diễn number/văn bản (text / 텍스트)/đối tượng (object / 객체) bằng văn bản (text / 텍스트) cú pháp (syntax / 문법) dễ đọc nhưng có overhead. nhị phân (binary / 이진) format có thể compact hơn và giữ kiểu (type / 타입) chặt hơn, nhưng khó inspect thủ công. mạng (network / 네트워크) giao thức (protocol / 프로토콜) và lưu trữ (storage / 저장소) format luôn phải quyết định cùng loại sự đánh đổi (trade-off / 트레이드오프).

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보), bit, encoding và biểu diễn (representation / 표현)**, **Structured dữ liệu (data / 데이터) cần format ngoài encoding** nêu điều cần giải thích; **Compression: bỏ redundancy chứ không tạo phép màu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Lỗi (error / 오류) detection và correction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Compression: bỏ redundancy chứ không tạo phép màu

Compression (nén / 압축) tận dụng cấu trúc (structure / 구조) và redundancy. Lossless compression cho phép khôi phục chính xác dữ liệu gốc; lossless thường dùng trong mã nguồn (source code / 소스 코드), cơ sở dữ liệu (database / 데이터베이스) pages hoặc executable. Lossy compression chấp nhận mất một số thông tin (information / 정보) ít quan trọng cho mục đích perception, như JPEG hay AAC.

Không phải mọi dữ liệu đều nén được nhiều. Nếu một chuỗi đã gần random, nó có ít redundancy để khai thác. Về thông tin (information / 정보) lý thuyết (theory / 이론), entropy đặt ra giới hạn cho average mã (code / 코드) length của lossless compression dưới một mô hình (model / 모델) xác suất.

Xem thêm: [Information Theory](../../mathematics/07_discrete_cs/06_information_theory_and_coding.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보), bit, encoding và biểu diễn (representation / 표현)**, **Lỗi (error / 오류) detection và correction** tiếp nhận điểm tựa từ **Compression: bỏ redundancy chứ không tạo phép màu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Units: KB, KiB và sự nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lỗi (error / 오류) detection và correction

Lưu trữ (storage / 저장소) và mạng (network / 네트워크) không tuyệt đối hoàn hảo: bit có thể flip. Ta có thể thêm redundancy có chủ đích để detect/correct lỗi. Parity bit là ví dụ đơn giản: thêm một bit sao cho tổng số 1 theo quy ước là chẵn/lẻ. CRC mạnh hơn cho burst errors trong transmission. ECC bộ nhớ (memory / 메모리) dùng error-correcting codes để sửa một số lỗi bit.

Điều thú vị là redundancy đôi khi bị loại bỏ để compression, nhưng đôi khi lại được thêm vào để độ tin cậy (reliability / 신뢰성). Mục tiêu khác nhau tạo ra thiết kế (design / 설계) khác nhau.

> **Chuyển mạch:** Trong **Thông tin (information / 정보), bit, encoding và biểu diễn (representation / 표현)**, **Lỗi (error / 오류) detection và correction** đã nêu tiêu chí phân biệt, còn **Units: KB, KiB và sự nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Units: KB, KiB và sự nhầm lẫn thường gặp

Trong SI, `1 kB = 1000 bytes`, `1 MB = 10^6 bytes`. nhị phân (binary / 이진) prefixes dùng `1 KiB = 1024 bytes`, `1 MiB = 2^20 bytes`. bộ nhớ (memory / 메모리) sức chứa (capacity / 용량) và OS tools đôi khi dùng cách hiển thị khác nhau, nên cùng ổ đĩa có thể thấy “nhỏ hơn” sau khi format mà thực ra chỉ khác đơn vị (unit / 단위) convention và filesystem overhead.

Bandwidth thường được quảng cáo bằng bit/s, trong khi tệp (file / 파일) kích thước (size / 크기) bằng byte. Link 100 Mbps không có nghĩa tải 100 MB mỗi giây; upper bound trước giao thức (protocol / 프로토콜) overhead là khoảng 12.5 MB/s.

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보), bit, encoding và biểu diễn (representation / 표현)**, **Units: KB, KiB và sự nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Mô hình tư duy (mental model / 사고 모델)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **Bits không có meaning cố định. Meaning xuất hiện khi một tầng (layer / 계층) áp encoding/lược đồ (schema / 스키마)/giao thức (protocol / 프로토콜) lên bit patterns.** Khi dữ liệu “bị sai”, hãy hỏi mismatch nằm ở biểu diễn (representation / 표현), ranh giới (boundary / 경계), kiểu (type / 타입), byte thứ tự (order / 순서), character encoding hay ngữ nghĩa (semantic / 의미적) interpretation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보), bit, encoding và biểu diễn (representation / 표현)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Unicode = UTF-8.”** Unicode định nghĩa mã (code / 코드) points và nhiều quy tắc văn bản (text / 텍스트); UTF-8 là một encoding của Unicode.

**“Một ký tự luôn là một byte.”** Chỉ đúng với một subset và một số encoding. UTF-8 dùng 1–4 bytes cho một Unicode scalar giá trị (value / 값); grapheme người dùng thấy còn có thể gồm nhiều mã (code / 코드) points.

**“nhị phân (binary / 이진) chính xác hơn decimal.”** nhị phân (binary / 이진) chỉ là cơ sở (base / 기반) biểu diễn (representation / 표현). Độ chính xác phụ thuộc kiểu (type / 타입) và số bit. Floating-point nhị phân (binary / 이진) còn không biểu diễn chính xác nhiều decimal fractions như 0.1.

> **Chuyển mạch:** Trong **Thông tin (information / 정보), bit, encoding và biểu diễn (representation / 표현)**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Bit biểu diễn (representation / 표현) dẫn trực tiếp đến [integer và floating-point representation](./02_numbers_and_machine_representation.md), [digital circuits](../02_computer_architecture/00_digital_logic_and_circuits.md), [serialization](../08_software_systems/04_time_serialization_and_idempotency.md), [network packets](../06_networks_distributed_systems/00_network_layers_packets_and_encapsulation.md) và [storage engines](../05_data_databases/04_storage_logs_recovery_and_durability.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
