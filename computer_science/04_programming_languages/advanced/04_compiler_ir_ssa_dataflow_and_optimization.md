# Compiler IR, SSA, data-flow analysis và optimization

Compiler không tối ưu trực tiếp source code như con người nhìn thấy và cũng không muốn phụ thuộc ngay vào machine instructions. Nó thường chuyển chương trình qua một hoặc nhiều **Intermediate Representations (IR / 중간 표현)** để biến semantics thành cấu trúc thuận lợi cho analysis và transformation.

## Vì sao cần IR

Nếu compiler hỗ trợ nhiều source languages và nhiều CPU targets, viết optimizer riêng cho từng cặp sẽ bùng nổ complexity. IR tạo điểm hội tụ: front-end hạ source semantics xuống IR; optimization passes làm việc trên IR; backend hạ IR xuống target machine.

Một compiler có thể dùng high-level IR giữ type/control structure rồi lower dần sang low-level IR gần machine hơn.

## Control-flow graph

Function được chia thành **basic blocks**: chuỗi instructions có một entry và control chỉ rời ở cuối. Các edges giữa blocks tạo **Control-Flow Graph (CFG)**.

CFG biến `if`, loop, early return thành graph để compiler hỏi: block nào reachable, definition nào có thể tới point này, expression nào invariant trong loop?

## Static Single Assignment

Trong **SSA**, mỗi variable version chỉ được assign một lần. Source:

```text
x = 1
x = x + 2
```

có thể thành `x1 = 1`, `x2 = x1 + 2`. Khi control-flow merge, **phi function** biểu diễn value đến từ predecessor nào.

SSA làm def-use chain rõ ràng. Nếu mỗi value có một definition, constant propagation, dead-code elimination và dependency analysis đơn giản hơn đáng kể.

## Data-flow analysis

Nhiều optimization là fixed-point analysis trên CFG. Ví dụ liveness hỏi value nào còn có thể được dùng trong tương lai; reaching definitions hỏi definitions nào có thể tới program point.

Compiler truyền abstract facts qua graph tới khi không còn thay đổi. Đây là connection trực tiếp với lattice/fixed-point reasoning trong static analysis.

## Optimization phải preserve semantics

Constant folding thay `2 * 3` bằng `6`; common subexpression elimination reuse computation; loop-invariant code motion đưa expression không đổi ra ngoài loop. Nhưng transformation chỉ hợp lệ dưới language semantics.

Floating-point reassociation, overflow, exceptions, volatile memory và concurrency có thể ngăn optimization tưởng như hiển nhiên. “Nhanh hơn” không đủ; compiler phải chứng minh transformation không thay observable behavior theo contract.

## Alias analysis

Nếu compiler không biết hai pointers có trỏ cùng memory hay không, nó phải bảo thủ. Alias analysis tốt mở đường cho reorder/vectorization nhưng analysis chính xác tuyệt đối cho general program là khó hoặc bất khả thi trong nhiều setting.

Đây là nơi computability limits gặp production compiler: optimizer dùng approximation có kiểm soát.

## Lowering và backend

Sau high-level optimization, IR được lower thành operations gần ISA. Backend làm instruction selection, register allocation và scheduling. Physical register hữu hạn khiến SSA virtual values phải được map, đôi khi spill ra stack.

## Debugging optimized code

Optimization phá mapping 1:1 giữa source line và machine execution. Variable có thể bị optimized away, code được inline hoặc reorder. Vì vậy debugging release build khó hơn debug build không chỉ vì thiếu symbols mà vì program representation đã thay đổi.

## Mental Model

> IR là ngôn ngữ reasoning nội bộ của compiler. SSA biến mutation thành explicit value versions; CFG biến control thành graph; data-flow analysis truyền facts trên graph. Optimization là semantics-preserving graph transformation, không phải collection mẹo làm code nhanh.