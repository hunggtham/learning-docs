# Hệ số, integer, floating point và dữ liệu trong bộ nhớ

Source code cho ta cảm giác `123`, `0.1` hay `true` là những thực thể tự nhiên. Ở machine level, tất cả đều phải được mã hóa trong một số bit hữu hạn. Sự hữu hạn này tạo ra overflow, rounding, signedness, alignment và endianness — những hiện tượng thường chỉ lộ ra khi system gặp edge case.

## Positional notation và vì sao binary/hex xuất hiện

Trong decimal, `472 = 4×10² + 7×10¹ + 2×10⁰`. Binary dùng cùng nguyên lý nhưng base 2: `1011₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 11`.

Hexadecimal (base 16 / 16진수) dùng digits `0–9, A–F`. Một hex digit tương ứng chính xác 4 bits, nên hex là shorthand rất tiện cho bit patterns. `0xFF = 11111111₂ = 255`. Đây là lý do memory addresses, bit masks, colors và machine code thường hiển thị bằng hex.

## Unsigned integer: range đến từ số patterns

Với `n` bits có `2^n` patterns. Nếu dùng tất cả cho non-negative integer, range là:

\[
0 \le x \le 2^n - 1
\]

8-bit unsigned integer có 256 values, từ 0 tới 255. Khi cộng 255 + 1 trong arithmetic modulo 256, bit pattern quay về 0. Hardware có thể đặt carry flag, còn language quyết định đây là wraparound, exception hay undefined behavior.

## Signed integer và two's complement

Cần biểu diễn cả âm lẫn dương. Cách phổ biến gần như tuyệt đối trên CPU hiện đại là **two's complement** (2의 보수 / bù hai). Với `n` bits, range là:

\[
-2^{n-1} \le x \le 2^{n-1}-1
\]

Điểm bất đối xứng có một số âm nhiều hơn một số dương. Với 8 bit: -128..127.

Two's complement có lợi vì cùng mạch cộng binary xử lý cả số âm và dương. Để tạo representation của `-x`, ta invert bits của `x` rồi cộng 1. Ví dụ 8-bit `5 = 00000101`; invert thành `11111010`; cộng 1 thành `11111011`, representation của -5.

Không nên hiểu bit cao nhất đơn giản là “dấu” độc lập với các bit khác như sign-magnitude. Trong two's complement, toàn pattern có meaning theo trọng số, với most-significant bit có weight âm `-2^{n-1}`.

## Overflow không phải bug của CPU

Một type hữu hạn không thể biểu diễn mọi integer. Overflow xảy ra khi kết quả toán học nằm ngoài range representation. Nếu business logic dùng `int` cho amount quá lớn, vấn đề là mismatch giữa domain và representation.

Java signed integer overflow wrap theo two's-complement semantics. C/C++ historically có signed overflow undefined behavior. Một số languages hoặc build modes có checked arithmetic. Database numeric types cũng khác nhau giữa fixed precision, arbitrary precision và machine integers.

Với tiền, floating point thường không phù hợp nếu cần exact decimal accounting; `BigDecimal`, decimal type hoặc integer nhỏ nhất như cents/won có thể phù hợp hơn tùy domain.

## Floating point: range lớn bằng scientific notation nhị phân

Real numbers vô hạn và liên tục, nhưng memory hữu hạn. Floating point xấp xỉ bằng ý tưởng scientific notation:

\[
value = (-1)^s \times significand \times base^{exponent}
\]

IEEE 754 binary floating point thường tách bits thành sign, exponent và fraction/significand. Với `double` 64-bit, ta có range rất lớn và khoảng 15–17 decimal significant digits, nhưng không thể biểu diễn chính xác mọi số thực.

`0.1` trong binary là repeating fraction, giống `1/3 = 0.333...` trong decimal. Vì vậy phép tính như `0.1 + 0.2` có thể không bằng bit-exact `0.3`.

Điều quan trọng không phải “floating point bị sai” mà là **floating point biểu diễn một tập hữu hạn các số gần real line**. Arithmetic phải round về representable value gần nhất.

### Relative precision và ULP

Khoảng cách giữa các representable floats không đều. Gần 1, spacing rất nhỏ; ở magnitude lớn, spacing lớn hơn. Đây là lý do thêm 1 vào một số floating-point cực lớn có thể không thay đổi value.

So sánh floats thường cần tolerance phù hợp với scale và domain, nhưng “luôn dùng epsilon = 1e-9” cũng không đúng chung. Numerical analysis quan tâm conditioning và accumulated error; xem [Numerical Methods](../../../mathematics/08_optimization_numerical/02_numerical_methods_and_error.md).

## NaN, infinity và signed zero

IEEE 754 còn có special values. `+∞`/`-∞` cho overflow hoặc division theo một số semantics. `NaN` (Not a Number) biểu diễn invalid/undefined numeric result như `0/0` trong floating point. `+0.0` và `-0.0` có thể so sánh bằng nhau nhưng giữ sign để một số limit-oriented operations có semantics tốt hơn.

NaN có property đáng chú ý: thường `NaN != NaN`. Vì vậy code kiểm tra `x == NaN` là sai; cần API như `isNaN`.

## Endianness: thứ tự byte trong multi-byte value

Giá trị `0x12345678` cần 4 bytes. Little-endian lưu least significant byte trước ở address thấp: `78 56 34 12`. Big-endian lưu `12 34 56 78`.

Endianness không thay đổi giá trị abstract; nó thay memory representation. Network byte order truyền thống là big-endian. Khi serialize binary data giữa heterogeneous systems, protocol phải quy định byte order.

## Alignment và padding

CPU thường truy cập dữ liệu hiệu quả hơn khi address phù hợp alignment boundary. Struct/object layout có thể thêm padding để fields thẳng hàng. Vì vậy tổng size struct không nhất thiết bằng tổng size fields.

Ví dụ conceptual:

```text
char  a;   // 1 byte
int32 b;   // 4 bytes
```

Implementation có thể chèn 3 padding bytes trước `b` để `b` bắt đầu tại address chia hết cho 4. Đây là bridge trực tiếp từ language-level types sang hardware memory access.

## Bitwise operations và masks

AND, OR, XOR, NOT và shifts cho phép thao tác từng bit. Bitmask compactly biểu diễn flags. Nếu permission bits là read=`001`, write=`010`, execute=`100`, thì `read | write = 011` bật hai quyền. `flags & write != 0` kiểm tra write bit.

Bitwise operations xuất hiện trong protocols, graphics, cryptography, low-level device control và performance-sensitive representations.

## Mental Model

> **Type ở source code là một contract trên tập bit patterns hữu hạn.** Range, precision, signedness, byte order và layout là phần của contract hoặc implementation. Khi gặp edge case số học, hãy quay về câu hỏi: “bit pattern nào đang tồn tại và rule diễn giải nó là gì?”

## Common Misconceptions

**“float chỉ là số thực ít chữ số hơn.”** Floating point có spacing phụ thuộc magnitude, special values và rounding rules; behavior khác decimal fixed-point.

**“int overflow hiếm nên có thể bỏ qua.”** Counter, timestamp, file size, ID, multiplication trung gian và attacker-controlled input đều có thể chạm overflow.

**“Endian là thứ tự bit.”** Thông thường thuật ngữ đề cập thứ tự bytes của multi-byte value trong memory/protocol, không phải cách ta viết từng bit trong byte.

## Kết nối

Representation ở đây là nền cho [CPU và ISA](../02_computer_architecture/01_cpu_isa_and_instruction_cycle.md), [assembly/ABI](../02_computer_architecture/04_machine_code_assembly_and_abi.md), [types và memory management](../04_programming_languages/01_types_values_references_and_memory.md), [serialization](../08_software_systems/04_time_serialization_and_idempotency.md) và các memory-safety bugs trong [software vulnerabilities](../07_security_reliability/03_software_vulnerabilities.md).
