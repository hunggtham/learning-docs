# Lô-gic (logic / 논리), Timing and trạng thái (state / 상태) — lô-gic (logic / 논리), timing và trạng thái

> **Mạch đọc:** Đặt **lô-gic (logic / 논리), Timing and trạng thái (state / 상태) — lô-gic (logic / 논리), timing và trạng thái** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Từ voltage đến Boolean** sang **2. Combinational và sequential**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Digital electronics dùng các vùng điện áp để biểu diễn lô-gic (logic / 논리), nhưng hệ thống số thật vẫn chịu delay, noise, loading, clock skew, metastability và power. Thiết kế số là thiết kế trạng thái (state / 상태) transitions có timing đặc tả hợp đồng (contract / 계약).

## 1. Từ voltage đến Boolean

Một cổng lô-gic (logic / 논리) không nhận “0/1” trừu tượng; nó nhận khoảng điện áp. VIL, VIH, VOL, VOH tạo noise margin:

    NMH = VOH(min) - VIH(min)
    NML = VIL(max) - VOL(max)

Nếu đầu ra (output / 출력) của driver không đủ margin cho đầu vào (input / 입력) kế tiếp, Boolean simulation vẫn đúng nhưng hardware có thể thất bại (fail / 실패) theo nhiệt độ hoặc nhiễu.


> **Chuyển mạch:** Từ **1. Từ voltage đến Boolean**, ta sang **2. Combinational và sequential** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. Combinational và sequential

Combinational circuit có đầu ra (output / 출력) là hàm của đầu vào (input / 입력) hiện tại. Sequential circuit có trạng thái (state / 상태) q:

    q_next = F(q, x)
    y = G(q, x)

Flip-flop chụp đầu vào (input / 입력) quanh clock edge. Timing đặc tả hợp đồng (contract / 계약) cơ bản:

    t_clk_period ≥ t_clk_to_q + t_comb + t_setup + skew + margin

Hold ràng buộc (constraint / 제약조건) kiểm tra dữ liệu mới không đến quá sớm sau clock edge.


> **Chuyển mạch:** Từ **2. Combinational và sequential**, ta sang **3. Metastability** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. Metastability

Nếu đầu vào (input / 입력) đổi gần sampling edge, flip-flop có thể tạm thời không settle về 0 hoặc 1. Đây là giới hạn analog của bistable circuit. Với tín hiệu asynchronous, dùng synchronizer nhiều tầng và chấp nhận xác suất lỗi giảm theo thời gian settle.

Không dùng một synchronizer cho bus nhiều bit rồi giả định cả bus nhất quán. Dùng handshake, Gray mã (code / 코드) hoặc asynchronous FIFO tùy ngữ nghĩa (semantics / 의미론).


> **Chuyển mạch:** Từ **3. Metastability**, ta sang **4. FSM và bất biến (invariant / 불변식)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. FSM và bất biến (invariant / 불변식)

Một finite-state machine nên xác định rõ:

    Trạng thái (state / 상태) set → đầu vào (input / 입력) sự kiện (event / 이벤트) → next-state → đầu ra (output / 출력) → illegal-state khôi phục (recovery / 복구)

Ví dụ giao thức (protocol / 프로토콜) receiver không chỉ có IDLE → dữ liệu (data / 데이터) → DONE; cần xử lý hết thời gian chờ (timeout / 타임아웃), framing lỗi (error / 오류), reset giữa packet và đầu vào (input / 입력) đến khi buffer đầy. bất biến (invariant / 불변식) như “không phát DONE trước khi checksum pass” nên xuất hiện trong simulation/assertion.


> **Chuyển mạch:** Từ **4. FSM và bất biến (invariant / 불변식)**, ta sang **5. Clock, reset và power** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. Clock, reset và power

Clock lĩnh vực (domain / 도메인) crossing cần giao thức (protocol / 프로토콜); không giải quyết bằng cách “đọc hai lần” một cách mơ hồ. Reset cũng có ngữ nghĩa (semantics / 의미론): synchronous hay asynchronous, reset bản phát hành (release / 릴리스) có đồng bộ không, trạng thái sau brownout có an toàn không, bộ nhớ (memory / 메모리)/peripheral reset có cùng thời điểm không.

Clock gating giảm động (dynamic / 동적) power nhưng tạo clock-domain và wake-up độ phức tạp (complexity / 복잡도). Power intent phải được xem cùng lô-gic (logic / 논리) tính đúng đắn (correctness / 정확성).


> **Chuyển mạch:** Từ **5. Clock, reset và power**, ta sang **6. Worked lập luận (reasoning / 추론): counter 100 MHz** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 6. Worked lập luận (reasoning / 추론): counter 100 MHz

Một counter 32-bit chạy ở 100 MHz overflow sau khoảng 42.95 s. Nếu firmware dùng counter để hết thời gian chờ (timeout / 타임아웃) 60 s mà không xử lý wrap-around, so sánh tuyệt đối sẽ thất bại (fail / 실패). Cách đúng là dùng unsigned elapsed-time arithmetic modulo 2^32, miễn hết thời gian chờ (timeout / 타임아웃) nhỏ hơn nửa chu kỳ wrap.

Đây là ví dụ hardware trạng thái (state / 상태) nối trực tiếp với software thời gian (time / 시간) ngữ nghĩa (semantics / 의미론).


> **Chuyển mạch:** Từ **6. Worked lập luận (reasoning / 추론): counter 100 MHz**, ta sang **7. xác minh (verification / 확인)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 7. xác minh (verification / 확인)
Phần “7. xác minh (verification / 확인)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- truth bảng (table / 테이블) và Boolean simplification cho combinational lô-gic (logic / 논리);
- waveform với clock/reset/lỗi (error / 오류) cases;
- assertion cho an toàn (safety / 안전) bất biến (invariant / 불변식) và giao thức (protocol / 프로토콜) thứ tự (ordering / 순서);
- static timing phân tích (analysis / 분석) cho setup/hold;
- CDC phân tích (analysis / 분석) và metastability các giả định (assumptions / 가정들);
- FPGA/board kiểm thử (test / 테스트) với clock, voltage và temperature corners.


> **Chuyển mạch:** Từ **7. xác minh (verification / 확인)**, ta sang **thất bại (failure / 실패) modes** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Thất bại (failure / 실패) modes
Phần “Thất bại (failure / 실패) modes” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- glitch combinational đi vào clock/reset;
- inferred latch do thiếu assignment;
- simulation dùng ideal zero-delay nhưng silicon có race;
- reset bản phát hành (release / 릴리스) khác lĩnh vực (domain / 도메인) tạo trạng thái (state / 상태) không xác định;
- bus width/endianness mismatch ở hardware–software ranh giới (boundary / 경계).


> **Chuyển mạch:** Từ **thất bại (failure / 실패) modes**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md) để chạy máy trạng thái (state machine / 상태 머신) trong MCU/SoC, hoặc [hardware–software interfaces](../hardware_software_interfaces/00_register_bus_driver_contracts.md) để định nghĩa register/bus đặc tả hợp đồng (contract / 계약). Computer kiến trúc (architecture / 아키텍처) mở rộng phần này sang CPU, ISA và bộ nhớ (memory / 메모리) hierarchy.

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 memory buses hdl verification](./01_memory_buses_hdl_verification.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
