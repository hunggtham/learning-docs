# Hệ số, integer, floating điểm (point / 지점) và dữ liệu trong bộ nhớ

> **Mạch đọc:** Đặt **Hệ số, integer, floating điểm (point / 지점) và dữ liệu trong bộ nhớ** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Positional notation và vì sao nhị phân (binary / 이진)/hex xuất hiện** sang **Unsigned integer: phạm vi (range / 범위) đến từ số patterns**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Mã nguồn (source code / 소스 코드) cho ta cảm giác `123`, `0.1` hay `true` là những thực thể tự nhiên. Ở machine mức (level / 수준), tất cả đều phải được mã hóa trong một số bit hữu hạn. Sự hữu hạn này tạo ra overflow, rounding, signedness, alignment và endianness — những hiện tượng thường chỉ lộ ra khi hệ thống (system / 시스템) gặp trường hợp biên (edge case / 경계 사례).

## Positional notation và vì sao nhị phân (binary / 이진)/hex xuất hiện

Trong decimal, `472 = 4×10² + 7×10¹ + 2×10⁰`. nhị phân (binary / 이진) dùng cùng nguyên lý nhưng cơ sở (base / 기반) 2: `1011₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 11`.

Hexadecimal (base 16 / 16진수) dùng digits `0–9, A–F`. Một hex digit tương ứng chính xác 4 bits, nên hex là shorthand rất tiện cho bit patterns. `0xFF = 11111111₂ = 255`. Đây là lý do bộ nhớ (memory / 메모리) addresses, bit masks, colors và mã máy (machine code / 기계어) thường hiển thị bằng hex.


> **Chuyển mạch:** Từ **Positional notation và vì sao nhị phân (binary / 이진)/hex xuất hiện**, ta sang **Unsigned integer: phạm vi (range / 범위) đến từ số patterns** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Unsigned integer: phạm vi (range / 범위) đến từ số patterns

Với `n` bits có `2^n` patterns. Nếu dùng tất cả cho non-negative integer, phạm vi (range / 범위) là:

\[
0 \le x \le 2^n - 1
\]

8-bit unsigned integer có 256 values, từ 0 tới 255. Khi cộng 255 + 1 trong arithmetic modulo 256, bit mẫu (pattern / 패턴) quay về 0. Hardware có thể đặt carry flag, còn ngôn ngữ (language / 언어) quyết định đây là wraparound, exception hay undefined hành vi (behavior / 동작).


> **Chuyển mạch:** Từ **Unsigned integer: phạm vi (range / 범위) đến từ số patterns**, ta sang **Signed integer và two's complement** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Signed integer và two's complement

Cần biểu diễn cả âm lẫn dương. Cách phổ biến gần như tuyệt đối trên CPU hiện đại là **two's complement** (2의 보수 / bù hai). Với `n` bits, phạm vi (range / 범위) là:

\[
-2^{n-1} \le x \le 2^{n-1}-1
\]

Điểm bất đối xứng có một số âm nhiều hơn một số dương. Với 8 bit: -128..127.

Two's complement có lợi vì cùng mạch cộng nhị phân (binary / 이진) xử lý cả số âm và dương. Để tạo biểu diễn (representation / 표현) của `-x`, ta invert bits của `x` rồi cộng 1. Ví dụ 8-bit `5 = 00000101`; invert thành `11111010`; cộng 1 thành `11111011`, biểu diễn (representation / 표현) của -5.

Không nên hiểu bit cao nhất đơn giản là “dấu” độc lập với các bit khác như sign-magnitude. Trong two's complement, toàn mẫu (pattern / 패턴) có meaning theo trọng số, với most-significant bit có weight âm `-2^{n-1}`.


> **Chuyển mạch:** Từ **Signed integer và two's complement**, ta sang **Overflow không phải bug của CPU** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Overflow không phải bug của CPU

Một kiểu (type / 타입) hữu hạn không thể biểu diễn mọi integer. Overflow xảy ra khi kết quả toán học nằm ngoài phạm vi (range / 범위) biểu diễn (representation / 표현). Nếu lô-gic nghiệp vụ (business logic / 비즈니스 로직) dùng `int` cho amount quá lớn, vấn đề là mismatch giữa lĩnh vực (domain / 도메인) và biểu diễn (representation / 표현).

Java signed integer overflow wrap theo two's-complement ngữ nghĩa (semantics / 의미론). C/C++ historically có signed overflow undefined hành vi (behavior / 동작). Một số languages hoặc bản dựng (build / 빌드) modes có checked arithmetic. cơ sở dữ liệu (database / 데이터베이스) numeric types cũng khác nhau giữa fixed precision, arbitrary precision và machine integers.

Với tiền, floating điểm (point / 지점) thường không phù hợp nếu cần chính xác (exact / 정확한) decimal accounting; `BigDecimal`, decimal kiểu (type / 타입) hoặc integer nhỏ nhất như cents/won có thể phù hợp hơn tùy lĩnh vực (domain / 도메인).


> **Chuyển mạch:** Từ **Overflow không phải bug của CPU**, ta sang **Floating điểm (point / 지점): phạm vi (range / 범위) lớn bằng scientific notation nhị phân** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Floating điểm (point / 지점): phạm vi (range / 범위) lớn bằng scientific notation nhị phân

Real numbers vô hạn và liên tục, nhưng bộ nhớ (memory / 메모리) hữu hạn. Floating điểm (point / 지점) xấp xỉ bằng ý tưởng scientific notation:

\[
giá trị (value / 값) = (-1)^s \times significand \times cơ sở (base / 기반)^{exponent}
\]

IEEE 754 nhị phân (binary / 이진) floating điểm (point / 지점) thường tách bits thành sign, exponent và fraction/significand. Với `double` 64-bit, ta có phạm vi (range / 범위) rất lớn và khoảng 15–17 decimal significant digits, nhưng không thể biểu diễn chính xác mọi số thực.

`0.1` trong nhị phân (binary / 이진) là repeating fraction, giống `1/3 = 0.333...` trong decimal. Vì vậy phép tính như `0.1 + 0.2` có thể không bằng bit-exact `0.3`.

Điều quan trọng không phải “floating điểm (point / 지점) bị sai” mà là **floating điểm (point / 지점) biểu diễn một tập hữu hạn các số gần real line**. Arithmetic phải round về representable giá trị (value / 값) gần nhất.

### Relative precision và ULP

Khoảng cách giữa các representable floats không đều. Gần 1, spacing rất nhỏ; ở magnitude lớn, spacing lớn hơn. Đây là lý do thêm 1 vào một số floating-point cực lớn có thể không thay đổi giá trị (value / 값).

So sánh floats thường cần tolerance phù hợp với quy mô (scale / 규모) và lĩnh vực (domain / 도메인), nhưng “luôn dùng epsilon = 1e-9” cũng không đúng chung. Numerical phân tích (analysis / 분석) quan tâm conditioning và accumulated lỗi (error / 오류); xem [Numerical Methods](../../mathematics/08_optimization_numerical/02_numerical_methods_and_error.md).


> **Chuyển mạch:** Từ **Floating điểm (point / 지점): phạm vi (range / 범위) lớn bằng scientific notation nhị phân**, ta sang **NaN, infinity và signed zero** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## NaN, infinity và signed zero

IEEE 754 còn có special values. `+∞`/`-∞` cho overflow hoặc division theo một số ngữ nghĩa (semantics / 의미론). `NaN` (Not a Number) biểu diễn invalid/undefined numeric kết quả (result / 결과) như `0/0` trong floating điểm (point / 지점). `+0.0` và `-0.0` có thể so sánh bằng nhau nhưng giữ sign để một số limit-oriented operations có ngữ nghĩa (semantics / 의미론) tốt hơn.

NaN có thuộc tính (property / 속성) đáng chú ý: thường `NaN != NaN`. Vì vậy mã (code / 코드) kiểm tra `x == NaN` là sai; cần API như `isNaN`.


> **Chuyển mạch:** Từ **NaN, infinity và signed zero**, ta sang **Endianness: thứ tự byte trong multi-byte giá trị (value / 값)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Endianness: thứ tự byte trong multi-byte giá trị (value / 값)

Giá trị `0x12345678` cần 4 bytes. Little-endian lưu least significant byte trước ở address thấp: `78 56 34 12`. Big-endian lưu `12 34 56 78`.

Endianness không thay đổi giá trị abstract; nó thay bộ nhớ (memory / 메모리) biểu diễn (representation / 표현). mạng (network / 네트워크) byte thứ tự (order / 순서) truyền thống là big-endian. Khi serialize nhị phân (binary / 이진) dữ liệu (data / 데이터) giữa heterogeneous các hệ thống (systems / 시스템들), giao thức (protocol / 프로토콜) phải quy định byte thứ tự (order / 순서).


> **Chuyển mạch:** Từ **Endianness: thứ tự byte trong multi-byte giá trị (value / 값)**, ta sang **Alignment và padding** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Alignment và padding

CPU thường truy cập dữ liệu hiệu quả hơn khi address phù hợp alignment ranh giới (boundary / 경계). Struct/đối tượng (object / 객체) bố cục (layout / 레이아웃) có thể thêm padding để fields thẳng hàng. Vì vậy tổng kích thước (size / 크기) struct không nhất thiết bằng tổng kích thước (size / 크기) fields.

Ví dụ conceptual:

```text
char  a;   // 1 byte
int32 b;   // 4 bytes
```

Hiện thực (implementation / 구현) có thể chèn 3 padding bytes trước `b` để `b` bắt đầu tại address chia hết cho 4. Đây là cầu nối (bridge / 브리지) trực tiếp từ language-level types sang hardware bộ nhớ (memory / 메모리) truy cập (access / 접근).


> **Chuyển mạch:** Từ **Alignment và padding**, ta sang **Bitwise operations và masks** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bitwise operations và masks

AND, OR, XOR, NOT và shifts cho phép thao tác từng bit. Bitmask compactly biểu diễn flags. Nếu permission bits là read=`001`, ghi (write / 쓰기)=`010`, execute=`100`, thì `read | write = 011` bật hai quyền. `flags & write != 0` kiểm tra ghi (write / 쓰기) bit.

Bitwise operations xuất hiện trong protocols, graphics, cryptography, low-level thiết bị (device / 장치) điều khiển (control / 제어) và performance-sensitive representations.


> **Chuyển mạch:** Từ **Bitwise operations và masks**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> **kiểu (type / 타입) ở mã nguồn (source code / 소스 코드) là một đặc tả hợp đồng (contract / 계약) trên tập bit patterns hữu hạn.** phạm vi (range / 범위), precision, signedness, byte thứ tự (order / 순서) và bố cục (layout / 레이아웃) là phần của đặc tả hợp đồng (contract / 계약) hoặc hiện thực (implementation / 구현). Khi gặp trường hợp biên (edge case / 경계 사례) số học, hãy quay về câu hỏi: “bit mẫu (pattern / 패턴) nào đang tồn tại và quy tắc (rule / 규칙) diễn giải nó là gì?”


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“float chỉ là số thực ít chữ số hơn.”** Floating điểm (point / 지점) có spacing phụ thuộc magnitude, special values và rounding rules; hành vi (behavior / 동작) khác decimal fixed-point.

**“int overflow hiếm nên có thể bỏ qua.”** Counter, timestamp, tệp (file / 파일) kích thước (size / 크기), ID, multiplication trung gian và attacker-controlled đầu vào (input / 입력) đều có thể chạm overflow.

**“Endian là thứ tự bit.”** Thông thường thuật ngữ đề cập thứ tự bytes của multi-byte giá trị (value / 값) trong bộ nhớ (memory / 메모리)/giao thức (protocol / 프로토콜), không phải cách ta viết từng bit trong byte.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Biểu diễn (representation / 표현) ở đây là nền cho [CPU và ISA](../02_computer_architecture/01_cpu_isa_and_instruction_cycle.md), [assembly/ABI](../02_computer_architecture/04_machine_code_assembly_and_abi.md), [types và memory management](../04_programming_languages/01_types_values_references_and_memory.md), [serialization](../08_software_systems/04_time_serialization_and_idempotency.md) và các memory-safety bugs trong [software vulnerabilities](../07_security_reliability/03_software_vulnerabilities.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 what computer science studies](./00_what_computer_science_studies.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
