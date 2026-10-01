# Digital lô-gic (logic / 논리), gates và sequential circuits

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Digital lô-gic (logic / 논리), gates và sequential circuits**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ transistor đến lô-gic (logic / 논리) gate** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Combinational lô-gic (logic / 논리)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Một CPU không “hiểu” `if`, đối tượng (object / 객체) hay SQL. Ở tầng thấp, hardware tạo và đo các trạng thái điện rồi tổ chức chúng thành digital lô-gic (logic / 논리). Digital lớp trừu tượng (abstraction / 추상화) biến một continuum voltage thành các mức lô-gic (logic / 논리) 0/1 đủ ổn định để ta lập luận (reasoning / 추론) bằng Boolean algebra thay vì semiconductor physics.

## Từ transistor đến lô-gic (logic / 논리) gate

Transistor có thể hoạt động gần như switch được điều khiển. Nhiều transistors kết hợp tạo NOT, AND, OR, NAND, NOR, XOR gates. Gate thực tế có propagation delay và điện năng tiêu thụ, nhưng ở lô-gic (logic / 논리) mức (level / 수준) ta coi chúng implement Boolean functions.

NAND và NOR là functionally complete: chỉ một loại gate cũng có thể xây mọi Boolean hàm (function / 함수). Đây là ví dụ lớp trừu tượng (abstraction / 추상화) rất mạnh: từ thiết bị (device / 장치) physics → gate → combinational circuit → CPU datapath.

> **Chuyển mạch:** Transistor tạo gate; combinational logic tính đầu ra chỉ từ đầu vào hiện tại, còn sequential logic thêm trạng thái để lưu nhớ và tạo mạch theo thời gian.

## Combinational lô-gic (logic / 논리)

Combinational circuit có đầu ra (output / 출력) phụ thuộc đầu vào (input / 입력) hiện tại, không nhớ lịch sử (history / 이력). Half-adder cộng hai bits, cho sum=`A XOR B`, carry=`A AND B`. Full-adder thêm carry-in; nối nhiều full-adders tạo nhị phân (binary / 이진) adder nhiều bit.

Multiplexer chọn một đầu vào (input / 입력) theo select bits. Decoder biến nhị phân (binary / 이진) mã (code / 코드) thành one-hot lines. Comparator, shifter và ALU đều xây từ những thành phần nguyên thủy (primitive / 기본 요소) như vậy.

Boolean algebra và truth bảng (table / 테이블) cho phép chứng minh two circuits equivalent. Karnaugh map hoặc lô-gic (logic / 논리) synthesis tools tối giản biểu thức để giảm gates/delay/area.

> **Chuyển mạch:** Ở chặng này của **Digital lô-gic (logic / 논리), gates và sequential circuits**, **Sequential lô-gic (logic / 논리): bộ nhớ (memory / 메모리) xuất hiện** tiếp nhận điểm tựa từ **Combinational lô-gic (logic / 논리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Clock và synchronous thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sequential lô-gic (logic / 논리): bộ nhớ (memory / 메모리) xuất hiện

Nếu đầu ra (output / 출력) chỉ phụ thuộc đầu vào (input / 입력) hiện tại, circuit không thể nhớ trạng thái (state / 상태). Sequential circuit thêm phản hồi (feedback / 피드백)/lưu trữ (storage / 저장소) elements như latches và flip-flops. Flip-flop lưu một bit trạng thái (state / 상태) qua clock edges.

Register là nhóm flip-flops lưu một word. Counter cập nhật trạng thái (state / 상태) theo clock. Finite-state controller kết hợp trạng thái hiện tại (current state / 현재 상태) + đầu vào (input / 입력) để quyết định next trạng thái (state / 상태)/đầu ra (output / 출력).

Đây là vật lý (physical / 물리적) realization của [state machine](../00_computation_information/03_logic_state_abstraction_and_invariants.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Digital lô-gic (logic / 논리), gates và sequential circuits**, **Clock và synchronous thiết kế (design / 설계)** tiếp nhận điểm tựa từ **Sequential lô-gic (logic / 논리): bộ nhớ (memory / 메모리) xuất hiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Arithmetic lô-gic (logic / 논리) đơn vị (unit / 단위)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Clock và synchronous thiết kế (design / 설계)

Nhiều digital các hệ thống (systems / 시스템들) dùng clock để chia thời gian thành steps. Combinational lô-gic (logic / 논리) phải settle trước next clock edge theo timing các ràng buộc (constraints / 제약조건들). Clock frequency càng cao không tự động càng nhanh: đường găng (critical path / 임계 경로) delay, chuỗi xử lý (pipeline / 파이프라인) độ sâu (depth / 깊이), bộ nhớ (memory / 메모리) stalls và power limit đều quan trọng.

Setup/hold violations có thể dẫn tới metastability khi tín hiệu (signal / 신호) thay đổi gần sampling edge. Synchronizing signals giữa clock domains là một real hardware bài toán (problem / 문제), cho thấy digital 0/1 chỉ là lớp trừu tượng (abstraction / 추상화) trên analog reality.

> **Chuyển mạch:** Trong **Digital lô-gic (logic / 논리), gates và sequential circuits**, **Arithmetic lô-gic (logic / 논리) đơn vị (unit / 단위)** tiếp nhận điểm tựa từ **Clock và synchronous thiết kế (design / 설계)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ (memory / 메모리) cells và hierarchy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Arithmetic lô-gic (logic / 논리) đơn vị (unit / 단위)

ALU (Arithmetic Logic Unit / 산술 논리 장치) thực hiện operations như add, subtract, AND, OR, shifts, comparisons. Subtraction có thể reuse adder bằng two's complement. Flags như zero/carry/overflow/sign cung cấp thông tin cho conditional branches trong một số ISAs.

ALU không tự quyết thao tác (operation / 연산); điều khiển (control / 제어) lô-gic (logic / 논리) decode instruction và tuyến (route / 경로) operands/results qua datapath.

> **Chuyển mạch:** Ở chặng này của **Digital lô-gic (logic / 논리), gates và sequential circuits**, **Bộ nhớ (memory / 메모리) cells và hierarchy** tiếp nhận điểm tựa từ **Arithmetic lô-gic (logic / 논리) đơn vị (unit / 단위)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lô-gic (logic / 논리) và HDL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) cells và hierarchy

Registers dùng fast circuits gần CPU thực thi (execution / 실행) units. SRAM thường dùng cho caches, nhanh nhưng area lớn. DRAM dùng capacitor-based cells, dense hơn nhưng cần refresh và chậm hơn. lưu trữ (storage / 저장소) flash dùng mechanisms khác và non-volatile.

Hierarchy tồn tại vì không có một technology đồng thời nhanh nhất, rẻ nhất, dense nhất và non-volatile nhất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Digital lô-gic (logic / 논리), gates và sequential circuits**, **Lô-gic (logic / 논리) và HDL** tiếp nhận điểm tựa từ **Bộ nhớ (memory / 메모리) cells và hierarchy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lô-gic (logic / 논리) và HDL

Hardware Description Languages như Verilog/SystemVerilog/VHDL mô tả circuits/tính đồng thời (concurrency / 동시성), không đơn giản là “program chạy tuần tự”. Synthesis công cụ (tool / 도구) biến RTL thành gates; timing/place-and-route nối lô-gic (logic / 논리) với vật lý (physical / 물리적) hiện thực (implementation / 구현).

Điều này khác software compilation: hardware description có thể biểu diễn nhiều operations xảy ra song song thực sự.

> **Chuyển mạch:** Trong **Digital lô-gic (logic / 논리), gates và sequential circuits**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Lô-gic (logic / 논리) và HDL** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Digital computer là **máy trạng thái (state machine / 상태 머신) khổng lồ**: combinational lô-gic (logic / 논리) tính next values, lưu trữ (storage / 저장소) elements giữ trạng thái (state / 상태), clock phối hợp updates. Instructions ở CPU chỉ là một tầng lớp trừu tượng (abstraction / 추상화) trên cấu trúc đó.

> **Chuyển mạch:** Ở chặng này của **Digital lô-gic (logic / 논리), gates và sequential circuits**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“0 và 1 là đúng 0V và 5V.”** lô-gic (logic / 논리) levels là voltage ranges tùy technology; digital lớp trừu tượng (abstraction / 추상화) chịu noise margins.

**“Clock 5 GHz nghĩa mỗi instruction mất 0.2 ns.”** Instructions có độ trễ (latency / 지연 시간)/thông lượng (throughput / 처리량) khác nhau, chuỗi xử lý (pipeline / 파이프라인), bộ nhớ đệm (cache / 캐시) misses và parallel thực thi (execution / 실행); CPI không cố định 1.

**“Hardware lô-gic (logic / 논리) chạy như mã (code / 코드) từng dòng.”** Nhiều parts của circuit hoạt động đồng thời; HDL ngữ nghĩa (semantics / 의미론) và timing khác imperative software.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Digital lô-gic (logic / 논리), gates và sequential circuits**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Boolean lô-gic (logic / 논리) nối trực tiếp [logic/invariants](../00_computation_information/03_logic_state_abstraction_and_invariants.md) với [CPU/ISA](./01_cpu_isa_and_instruction_cycle.md). bộ nhớ (memory / 메모리) technologies giải thích vì sao [memory hierarchy/cache](./02_memory_hierarchy_and_cache.md) tồn tại.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
