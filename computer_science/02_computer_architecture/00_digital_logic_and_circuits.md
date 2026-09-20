# Digital logic, gates và sequential circuits

Một CPU không “hiểu” `if`, object hay SQL. Ở tầng thấp, hardware tạo và đo các trạng thái điện rồi tổ chức chúng thành digital logic (논리 회로 / mạch logic số). Digital abstraction biến một continuum voltage thành các mức logic 0/1 đủ ổn định để ta reasoning bằng Boolean algebra thay vì semiconductor physics.

## Từ transistor đến logic gate

Transistor có thể hoạt động gần như switch được điều khiển. Nhiều transistors kết hợp tạo NOT, AND, OR, NAND, NOR, XOR gates. Gate thực tế có propagation delay và điện năng tiêu thụ, nhưng ở logic level ta coi chúng implement Boolean functions.

NAND và NOR là functionally complete: chỉ một loại gate cũng có thể xây mọi Boolean function. Đây là ví dụ abstraction rất mạnh: từ device physics → gate → combinational circuit → CPU datapath.

## Combinational logic

Combinational circuit có output phụ thuộc input hiện tại, không nhớ history. Half-adder cộng hai bits, cho sum=`A XOR B`, carry=`A AND B`. Full-adder thêm carry-in; nối nhiều full-adders tạo binary adder nhiều bit.

Multiplexer chọn một input theo select bits. Decoder biến binary code thành one-hot lines. Comparator, shifter và ALU đều xây từ những primitive như vậy.

Boolean algebra và truth table cho phép chứng minh two circuits equivalent. Karnaugh map hoặc logic synthesis tools tối giản biểu thức để giảm gates/delay/area.

## Sequential logic: memory xuất hiện

Nếu output chỉ phụ thuộc input hiện tại, circuit không thể nhớ state. Sequential circuit thêm feedback/storage elements như latches và flip-flops. Flip-flop lưu một bit state qua clock edges.

Register là nhóm flip-flops lưu một word. Counter cập nhật state theo clock. Finite-state controller kết hợp current state + input để quyết định next state/output.

Đây là physical realization của [state machine](../00_computation_information/03_logic_state_abstraction_and_invariants.md).

## Clock và synchronous design

Nhiều digital systems dùng clock để chia thời gian thành steps. Combinational logic phải settle trước next clock edge theo timing constraints. Clock frequency càng cao không tự động càng nhanh: critical path delay, pipeline depth, memory stalls và power limit đều quan trọng.

Setup/hold violations có thể dẫn tới metastability khi signal thay đổi gần sampling edge. Synchronizing signals giữa clock domains là một real hardware problem, cho thấy digital 0/1 chỉ là abstraction trên analog reality.

## Arithmetic logic unit

ALU (Arithmetic Logic Unit / 산술 논리 장치) thực hiện operations như add, subtract, AND, OR, shifts, comparisons. Subtraction có thể reuse adder bằng two's complement. Flags như zero/carry/overflow/sign cung cấp thông tin cho conditional branches trong một số ISAs.

ALU không tự quyết operation; control logic decode instruction và route operands/results qua datapath.

## Memory cells và hierarchy

Registers dùng fast circuits gần CPU execution units. SRAM thường dùng cho caches, nhanh nhưng area lớn. DRAM dùng capacitor-based cells, dense hơn nhưng cần refresh và chậm hơn. Storage flash dùng mechanisms khác và non-volatile.

Hierarchy tồn tại vì không có một technology đồng thời nhanh nhất, rẻ nhất, dense nhất và non-volatile nhất.

## Logic và HDL

Hardware Description Languages như Verilog/SystemVerilog/VHDL mô tả circuits/concurrency, không đơn giản là “program chạy tuần tự”. Synthesis tool biến RTL thành gates; timing/place-and-route nối logic với physical implementation.

Điều này khác software compilation: hardware description có thể biểu diễn nhiều operations xảy ra song song thực sự.

## Mental Model

> Digital computer là **state machine khổng lồ**: combinational logic tính next values, storage elements giữ state, clock phối hợp updates. Instructions ở CPU chỉ là một tầng abstraction trên cấu trúc đó.

## Common Misconceptions

**“0 và 1 là đúng 0V và 5V.”** Logic levels là voltage ranges tùy technology; digital abstraction chịu noise margins.

**“Clock 5 GHz nghĩa mỗi instruction mất 0.2 ns.”** Instructions có latency/throughput khác nhau, pipeline, cache misses và parallel execution; CPI không cố định 1.

**“Hardware logic chạy như code từng dòng.”** Nhiều parts của circuit hoạt động đồng thời; HDL semantics và timing khác imperative software.

## Kết nối

Boolean logic nối trực tiếp [logic/invariants](../00_computation_information/03_logic_state_abstraction_and_invariants.md) với [CPU/ISA](./01_cpu_isa_and_instruction_cycle.md). Memory technologies giải thích vì sao [memory hierarchy/cache](./02_memory_hierarchy_and_cache.md) tồn tại.
