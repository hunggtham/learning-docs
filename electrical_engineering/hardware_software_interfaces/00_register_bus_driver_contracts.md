# Register, Bus and Driver Contracts — đặc tả hợp đồng (contract / 계약) phần cứng–phần mềm

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Register, Bus and Driver Contracts — đặc tả hợp đồng (contract / 계약) phần cứng–phần mềm**. Route đi từ register semantics → ordering/visibility và side effects → bus timing → driver/firmware contract → testing, tooling và failure recovery, để register map được đọc như API thấp tầng.

Hardware–software giao diện (interface / 인터페이스) là đặc tả hợp đồng (contract / 계약) có timing, thứ tự (ordering / 순서), side effects và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론). Một register map không chỉ là bảng địa chỉ; nó là API thấp tầng mà firmware, bootloader, driver, kiểm thử (test / 테스트) và tooling cùng phụ thuộc.

## 1. Register ngữ nghĩa (semantics / 의미론)

Mỗi trường dữ liệu (field / 필드) cần mô tả:

    address → width → reset giá trị (value / 값) → truy cập (access / 접근) chế độ (mode / 모드)
    → side tác động (effect / 효과) → timing → lỗi (error / 오류)/status → quyền sở hữu (ownership / 소유권)

Các truy cập (access / 접근) chế độ (mode / 모드) RW, RO, WO, write-one-to-clear và read-to-clear có ngữ nghĩa (semantics / 의미론) khác nhau. Đọc status register hai lần có thể làm mất sự kiện (event / 이벤트) nếu register có side tác động (effect / 효과).

> **Chuyển mạch:** Trong **Register, Bus and Driver Contracts — đặc tả hợp đồng (contract / 계약) phần cứng–phần mềm**, **2. thứ tự (ordering / 순서) và visibility** tiếp nhận điểm tựa từ **1. Register ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Bus giao thức (protocol / 프로토콜)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. thứ tự (ordering / 순서) và visibility

CPU trình biên dịch (compiler / 컴파일러), bộ nhớ đệm (cache / 캐시), bus fabric và peripheral đều có thể reorder hoặc buffer giao dịch (transaction / 트랜잭션). Volatile chỉ nói trình biên dịch (compiler / 컴파일러) không bỏ truy cập (access / 접근); nó không tự tạo atomicity, inter-core thứ tự (ordering / 순서) hay DMA bộ nhớ đệm (cache / 캐시) coherence.

Một driver cần xác định ghi (write / 쓰기) nào phải barrier trước enable, status nào phải đọc sau khi poll, hết thời gian chờ (timeout / 타임아웃) tính từ yêu cầu (request / 요청) hay từ hardware acceptance, và interrupt acknowledge trước hay sau khi clear nguồn (source / 소스).

> **Chuyển mạch:** Ở chặng này của **Register, Bus and Driver Contracts — đặc tả hợp đồng (contract / 계약) phần cứng–phần mềm**, **3. Bus giao thức (protocol / 프로토콜)** tiếp nhận điểm tựa từ **2. thứ tự (ordering / 순서) và visibility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Interrupt và DMA đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Bus giao thức (protocol / 프로토콜)

SPI, I²C, UART, CAN và các bus khác cần phân biệt electrical tầng (layer / 계층) với giao dịch (transaction / 트랜잭션) đặc tả hợp đồng (contract / 계약): voltage/drive/pull-up/termination, framing/addressing/arbitration, maximum clock/setup/hold, NACK/hết thời gian chờ (timeout / 타임아웃)/bus khôi phục (recovery / 복구), duplicate/thử lại (retry / 재시도) và idempotency.

Gửi được byte chưa chứng minh giao thức (protocol / 프로토콜) đúng nếu reset giữa giao dịch (transaction / 트랜잭션) hoặc bus contention chưa được xử lý.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Register, Bus and Driver Contracts — đặc tả hợp đồng (contract / 계약) phần cứng–phần mềm**, **4. Interrupt và DMA đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **3. Bus giao thức (protocol / 프로토콜)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Driver API và lỗi (error / 오류) ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Interrupt và DMA đặc tả hợp đồng (contract / 계약)

Interrupt nguồn (source / 소스) cần máy trạng thái (state machine / 상태 머신) rõ:

    Sự kiện (event / 이벤트) asserted → status observed → nguồn (source / 소스) acknowledged
    → công việc (work / 작업) captured → handler returns → sự kiện (event / 이벤트) cannot be lost/duplicated

DMA descriptor cần quyền sở hữu (ownership / 소유권) bit hoặc hàng đợi (queue / 큐) giao thức (protocol / 프로토콜). bộ nhớ đệm (cache / 캐시) maintenance phải nằm trong đặc tả hợp đồng (contract / 계약) nếu CPU đọc vùng bộ nhớ (memory / 메모리) mà DMA vừa ghi.

> **Chuyển mạch:** Trong **Register, Bus and Driver Contracts — đặc tả hợp đồng (contract / 계약) phần cứng–phần mềm**, **5. Driver API và lỗi (error / 오류) ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **4. Interrupt và DMA đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Worked lập luận (reasoning / 추론): write-enable chuỗi (sequence / 시퀀스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Driver API và lỗi (error / 오류) ngữ nghĩa (semantics / 의미론)

Driver không nên trả một mã lỗi cho mọi lỗi. Cần phân biệt invalid argument, thiết bị (device / 장치) not ready, transient hết thời gian chờ (timeout / 타임아웃), permanent hardware fault, dữ liệu (data / 데이터) integrity thất bại (failure / 실패) và cancellation/reset in progress.

Thử lại (retry / 재시도) chỉ an toàn khi thao tác (operation / 연산) idempotent hoặc có giao dịch (transaction / 트랜잭션) định danh (identity / 식별자). thử lại (retry / 재시도) ghi (write / 쓰기) register có side tác động (effect / 효과) có thể tạo hành động lặp.

> **Chuyển mạch:** Ở chặng này của **Register, Bus and Driver Contracts — đặc tả hợp đồng (contract / 계약) phần cứng–phần mềm**, **5. Driver API và lỗi (error / 오류) ngữ nghĩa (semantics / 의미론)** cho ta quy tắc; **6. Worked lập luận (reasoning / 추론): write-enable chuỗi (sequence / 시퀀스)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **7. Boot, cập nhật (update / 업데이트) và tính tương thích (compatibility / 호환성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Worked lập luận (reasoning / 추론): write-enable chuỗi (sequence / 시퀀스)

Giả sử peripheral yêu cầu ghi cấu hình (config / 설정), chờ READY, rồi set ENABLE. Nếu firmware set ENABLE trước khi READY, hardware có thể bỏ yêu cầu (request / 요청) hoặc vào fault trạng thái (state / 상태). đặc tả hợp đồng (contract / 계약) đúng cần:

    reset deasserted
    → clock enabled
    → cấu hình (config / 설정) ghi (write / 쓰기) posted
    → read-back/barrier
    → READY observed within deadline
    → ENABLE set
    → ACTIVE observed

Kiểm thử (test / 테스트) phải inject READY hết thời gian chờ (timeout / 타임아웃), bus lỗi (error / 오류) và reset giữa các bước; happy đường dẫn (path / 경로) không đủ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Register, Bus and Driver Contracts — đặc tả hợp đồng (contract / 계약) phần cứng–phần mềm**, **6. Worked lập luận (reasoning / 추론): write-enable chuỗi (sequence / 시퀀스)** cho ta quy tắc; **7. Boot, cập nhật (update / 업데이트) và tính tương thích (compatibility / 호환성)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Boot, cập nhật (update / 업데이트) và tính tương thích (compatibility / 호환성)

Firmware phiên bản (version / 버전) phải tương thích với hardware revision và register lược đồ (schema / 스키마). Bootloader cần xác định ảnh (image / 이미지) validity, power mất mát (loss / 손실) giữa cập nhật (update / 업데이트), quay lui (rollback / 롤백) và monotonic phiên bản (version / 버전) để tránh downgrade không mong muốn.

> **Chuyển mạch:** Trong **Register, Bus and Driver Contracts — đặc tả hợp đồng (contract / 계약) phần cứng–phần mềm**, **Thất bại (failure / 실패) modes** tiếp nhận điểm tựa từ **7. Boot, cập nhật (update / 업데이트) và tính tương thích (compatibility / 호환성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thất bại (failure / 실패) modes

- register header đúng tên nhưng sai endianness/bitfield packing;
- clear-on-read làm mất interrupt khi gỡ lỗi (debug / 디버그);
- driver hết thời gian chờ (timeout / 타임아웃) nhưng hardware vẫn đang chạy, tạo duplicate command;
- DMA ghi vào buffer trước khi CPU invalidate bộ nhớ đệm (cache / 캐시);
- firmware cập nhật (update / 업데이트) thành công nhưng calibration/lược đồ (schema / 스키마) cũ không tương thích.

> **Chuyển mạch:** Ở chặng này của **Register, Bus and Driver Contracts — đặc tả hợp đồng (contract / 계약) phần cứng–phần mềm**, **Cầu nối (bridge / 브리지)** tiếp nhận điểm tựa từ **Thất bại (failure / 실패) modes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đọc cùng [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md), [digital electronics](../digital_electronics/00_logic_timing_state.md) và Computer kiến trúc (architecture / 아키텍처) về I/O, interrupt, DMA, ABI và bộ nhớ (memory / 메모리) thứ tự (ordering / 순서).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
