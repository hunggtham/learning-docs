# Digital lô-gic (logic / 논리), gates và sequential circuits

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Digital lô-gic (logic / 논리), gates và sequential circuits**. Route đi từ transistor/gate → Boolean và combinational logic → clock, state và sequential circuits → datapath/control, để mạch số được nối với hành vi và trạng thái theo thời gian.

Một CPU không “hiểu” `if`, đối tượng (object / 객체) hay SQL. Ở tầng thấp, hardware tạo và đo các trạng thái điện rồi tổ chức chúng thành digital lô-gic (logic / 논리). Digital lớp trừu tượng (abstraction / 추상화) biến một continuum voltage thành các mức lô-gic (logic / 논리) 0/1 đủ ổn định để ta lập luận (reasoning / 추론) bằng Boolean algebra thay vì semiconductor physics.

## Từ transistor đến lô-gic (logic / 논리) gate

Transistor có thể hoạt động gần như switch được điều khiển. Nhiều transistors kết hợp tạo NOT, AND, OR, NAND, NOR, XOR gates. Gate thực tế có propagation delay và điện năng tiêu thụ, nhưng ở lô-gic (logic / 논리) mức (level / 수준) ta coi chúng implement Boolean functions.

NAND và NOR là functionally complete: chỉ một loại gate cũng có thể xây mọi Boolean hàm (function / 함수). Đây là ví dụ lớp trừu tượng (abstraction / 추상화) rất mạnh: từ thiết bị (device / 장치) physics → gate → combinational circuit → CPU datapath.

Từ các gate này, ta tách hai cách mạch tạo ra kết quả: combinational logic chỉ nhìn đầu vào hiện tại, còn sequential logic giữ trạng thái để hành vi trải dài theo thời gian.

## Combinational lô-gic (logic / 논리)

Combinational circuit có đầu ra (output / 출력) phụ thuộc đầu vào (input / 입력) hiện tại, không nhớ lịch sử (history / 이력). Half-adder cộng hai bits, cho sum=`A XOR B`, carry=`A AND B`. Full-adder thêm carry-in; nối nhiều full-adders tạo nhị phân (binary / 이진) adder nhiều bit.

Multiplexer chọn một đầu vào (input / 입력) theo select bits. Decoder biến nhị phân (binary / 이진) mã (code / 코드) thành one-hot lines. Comparator, shifter và ALU đều xây từ những thành phần nguyên thủy (primitive / 기본 요소) như vậy.

Boolean algebra và truth bảng (table / 테이블) cho phép chứng minh two circuits equivalent. Karnaugh map hoặc lô-gic (logic / 논리) synthesis tools tối giản biểu thức để giảm gates/delay/area.

Combinational circuit không lưu lịch sử. Khi mạch cần nhớ trạng thái giữa hai lần tính, ta phải thêm phần tử lưu trữ và một cơ chế cập nhật. Đó là lý do phần tiếp theo chuyển sang sequential logic.

## Sequential lô-gic (logic / 논리): bộ nhớ (memory / 메모리) xuất hiện

Nếu đầu ra (output / 출력) chỉ phụ thuộc đầu vào (input / 입력) hiện tại, circuit không thể nhớ trạng thái (state / 상태). Sequential circuit thêm phản hồi (feedback / 피드백)/lưu trữ (storage / 저장소) elements như latches và flip-flops. Flip-flop lưu một bit trạng thái (state / 상태) qua clock edges.

Register là nhóm flip-flops lưu một word. Counter cập nhật trạng thái (state / 상태) theo clock. Finite-state controller kết hợp trạng thái hiện tại (current state / 현재 상태) + đầu vào (input / 입력) để quyết định next trạng thái (state / 상태)/đầu ra (output / 출력).

Đây là vật lý (physical / 물리적) realization của [state machine](../00_computation_information/03_logic_state_abstraction_and_invariants.md).

Có trạng thái thôi chưa đủ; mạch còn phải thống nhất thời điểm đọc và ghi trạng thái. Clock, setup/hold và giới hạn timing cung cấp quy ước đó. Khi nhịp đã rõ, ta có thể xem datapath thực hiện phép toán như thế nào.

## Clock và synchronous thiết kế (design / 설계)

Nhiều digital các hệ thống (systems / 시스템들) dùng clock để chia thời gian thành steps. Combinational lô-gic (logic / 논리) phải settle trước next clock edge theo timing các ràng buộc (constraints / 제약조건들). Clock frequency càng cao không tự động càng nhanh: đường găng (critical path / 임계 경로) delay, chuỗi xử lý (pipeline / 파이프라인) độ sâu (depth / 깊이), bộ nhớ (memory / 메모리) stalls và power limit đều quan trọng.

Setup/hold violations có thể dẫn tới metastability khi tín hiệu (signal / 신호) thay đổi gần sampling edge. Synchronizing signals giữa clock domains là một real hardware bài toán (problem / 문제), cho thấy digital 0/1 chỉ là lớp trừu tượng (abstraction / 추상화) trên analog reality.

ALU cho thấy các gate và đường dữ liệu biến đầu vào thành kết quả có ý nghĩa với CPU. Nhưng kết quả chỉ hữu ích nếu mạch có nơi giữ operands, instructions và trạng thái giữa các chu kỳ. Vì vậy, bước kế tiếp là các ô nhớ và memory hierarchy.

## Arithmetic lô-gic (logic / 논리) đơn vị (unit / 단위)

ALU (Arithmetic Logic Unit / 산술 논리 장치) thực hiện operations như add, subtract, AND, OR, shifts, comparisons. Subtraction có thể reuse adder bằng two's complement. Flags như zero/carry/overflow/sign cung cấp thông tin cho conditional branches trong một số ISAs.

ALU không tự quyết thao tác (operation / 연산); điều khiển (control / 제어) lô-gic (logic / 논리) decode instruction và tuyến (route / 경로) operands/results qua datapath.

Các loại memory khác nhau ở tốc độ, mật độ, giá thành và khả năng giữ dữ liệu khi mất điện. Để biến những đánh đổi ấy thành phần cứng cụ thể, người thiết kế cần một ngôn ngữ mô tả mạch và quan hệ đồng thời giữa các phần tử.

## Bộ nhớ (memory / 메모리) cells và hierarchy

Registers dùng fast circuits gần CPU thực thi (execution / 실행) units. SRAM thường dùng cho caches, nhanh nhưng area lớn. DRAM dùng capacitor-based cells, dense hơn nhưng cần refresh và chậm hơn. lưu trữ (storage / 저장소) flash dùng mechanisms khác và non-volatile.

Hierarchy tồn tại vì không có một technology đồng thời nhanh nhất, rẻ nhất, dense nhất và non-volatile nhất.

HDL gom các mảnh của file vào một mô hình thống nhất: dữ liệu đi qua combinational logic, trạng thái được giữ bởi storage elements, còn clock điều phối thời điểm cập nhật. Mô hình đó giúp ta kiểm tra các ngộ nhận thường gặp trước khi rút ra kết luận.

## Lô-gic (logic / 논리) và HDL

Hardware Description Languages như Verilog/SystemVerilog/VHDL mô tả circuits/tính đồng thời (concurrency / 동시성), không đơn giản là “program chạy tuần tự”. Synthesis công cụ (tool / 도구) biến RTL thành gates; timing/place-and-route nối lô-gic (logic / 논리) với vật lý (physical / 물리적) hiện thực (implementation / 구현).

Điều này khác software compilation: hardware description có thể biểu diễn nhiều operations xảy ra song song thực sự.

## Mô hình tư duy (mental model / 사고 모델)

> Digital computer là **máy trạng thái (state machine / 상태 머신) khổng lồ**: combinational lô-gic (logic / 논리) tính next values, lưu trữ (storage / 저장소) elements giữ trạng thái (state / 상태), clock phối hợp updates. Instructions ở CPU chỉ là một tầng lớp trừu tượng (abstraction / 추상화) trên cấu trúc đó.

## Dùng chung (common / 공통) Misconceptions

**“0 và 1 là đúng 0V và 5V.”** lô-gic (logic / 논리) levels là voltage ranges tùy technology; digital lớp trừu tượng (abstraction / 추상화) chịu noise margins.

**“Clock 5 GHz nghĩa mỗi instruction mất 0.2 ns.”** Instructions có độ trễ (latency / 지연 시간)/thông lượng (throughput / 처리량) khác nhau, chuỗi xử lý (pipeline / 파이프라인), bộ nhớ đệm (cache / 캐시) misses và parallel thực thi (execution / 실행); CPI không cố định 1.

**“Hardware lô-gic (logic / 논리) chạy như mã (code / 코드) từng dòng.”** Nhiều parts của circuit hoạt động đồng thời; HDL ngữ nghĩa (semantics / 의미론) và timing khác imperative software.

Ba ngộ nhận trên đều xuất phát từ việc nhầm lớp trừu tượng với phần cứng bên dưới. Khi đã tách được mức logic, timing và sự đồng thời, ta có thể nối chapter này về các owner cơ chế thay vì coi digital logic là một hộp đen.

## Kết nối

Boolean lô-gic (logic / 논리) nối trực tiếp [logic/invariants](../00_computation_information/03_logic_state_abstraction_and_invariants.md) với [CPU/ISA](./01_cpu_isa_and_instruction_cycle.md). bộ nhớ (memory / 메모리) technologies giải thích vì sao [memory hierarchy/cache](./02_memory_hierarchy_and_cache.md) tồn tại.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
