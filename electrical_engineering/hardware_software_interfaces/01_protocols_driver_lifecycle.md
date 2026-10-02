# Protocols and Driver vòng đời (lifecycle / 생명주기) — giao thức (protocol / 프로토콜) và vòng đời driver

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Protocols and Driver vòng đời (lifecycle / 생명주기) — giao thức (protocol / 프로토콜) và vòng đời driver**. Route đi từ protocol semantics → driver state machine → discovery/init/active/error recovery → suspend/resume, update và removal → testing/hotplug/failure, để giao thức được nối với toàn bộ vòng đời thiết bị.

Register đặc tả hợp đồng (contract / 계약) cần được đặt vào vòng đời (lifecycle / 생명주기): discovery, init, active thao tác (operation / 연산), lỗi (error / 오류) khôi phục (recovery / 복구), suspend/resume, cập nhật (update / 업데이트) và removal.

## 1. giao thức (protocol / 프로토콜) ngữ nghĩa (semantics / 의미론)

SPI thường không có framing/lỗi (error / 오류) ngữ nghĩa (semantics / 의미론) built-in như CAN; I²C có arbitration và ACK nhưng cần bus khôi phục (recovery / 복구); UART không tự bảo đảm packet ranh giới (boundary / 경계); CAN có arbitration và fault confinement. Chọn bus theo thất bại (failure / 실패) mô hình (model / 모델), không chỉ theo tốc độ danh nghĩa.

> **Chuyển mạch:** Trong **Protocols and Driver vòng đời (lifecycle / 생명주기) — giao thức (protocol / 프로토콜) và vòng đời driver**, **2. máy trạng thái (state machine / 상태 머신) của driver** tiếp nhận điểm tựa từ **1. giao thức (protocol / 프로토콜) ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. ABI, lược đồ (schema / 스키마) và tính tương thích (compatibility / 호환성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. máy trạng thái (state machine / 상태 머신) của driver

Driver nên có trạng thái (state / 상태) rõ:

    RESET → PROBING → READY → RUNNING → DEGRADED → RECOVERING → OFFLINE

Mỗi chuyển tiếp (transition / 전이) cần trigger, hết thời gian chờ (timeout / 타임아웃), side tác động (effect / 효과) và observable bằng chứng (evidence / 증거). Một hết thời gian chờ (timeout / 타임아웃) không được tự động thử lại (retry / 재시도) nếu hardware chưa xác nhận command đã dừng.

> **Chuyển mạch:** Ở chặng này của **Protocols and Driver vòng đời (lifecycle / 생명주기) — giao thức (protocol / 프로토콜) và vòng đời driver**, **3. ABI, lược đồ (schema / 스키마) và tính tương thích (compatibility / 호환성)** tiếp nhận điểm tựa từ **2. máy trạng thái (state machine / 상태 머신) của driver** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Worked lập luận (reasoning / 추론): I²C stuck bus** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. ABI, lược đồ (schema / 스키마) và tính tương thích (compatibility / 호환성)

Header/ABI, register lược đồ (schema / 스키마), firmware phiên bản (version / 버전) và calibration dữ liệu (data / 데이터) đều là tính tương thích (compatibility / 호환성) surface. Thay đổi trường dữ liệu (field / 필드) reserved, alignment hoặc endian có thể phá bên tiêu thụ (consumer / 소비자) dù hàm (function / 함수) name không đổi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Protocols and Driver vòng đời (lifecycle / 생명주기) — giao thức (protocol / 프로토콜) và vòng đời driver**, **3. ABI, lược đồ (schema / 스키마) và tính tương thích (compatibility / 호환성)** cho ta quy tắc; **4. Worked lập luận (reasoning / 추론): I²C stuck bus** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **5. khả năng quan sát (observability / 관측 가능성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Worked lập luận (reasoning / 추론): I²C stuck bus

Nếu slave giữ SDA low sau reset giữa byte, controller không thể gửi command mới. khôi phục (recovery / 복구) có thể toggle SCL hữu hạn lần, phát STOP, reset peripheral và re-probe. Nếu vẫn thất bại (fail / 실패), driver phải chuyển OFFLINE và báo rõ nguyên nhân thay vì vòng lặp (loop / 루프) thử lại (retry / 재시도) vô hạn.

> **Chuyển mạch:** Trong **Protocols and Driver vòng đời (lifecycle / 생명주기) — giao thức (protocol / 프로토콜) và vòng đời driver**, **4. Worked lập luận (reasoning / 추론): I²C stuck bus** cho ta quy tắc; **5. khả năng quan sát (observability / 관측 가능성)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. khả năng quan sát (observability / 관측 가능성)

Telemetry nên ghi giao dịch (transaction / 트랜잭션) id, bus lỗi (error / 오류), thử lại (retry / 재시도) count, reset cause, firmware/hardware revision và timing. Log một “read failed” không đủ để tái hiện race hoặc power fault.

> **Chuyển mạch:** Ở chặng này của **Protocols and Driver vòng đời (lifecycle / 생명주기) — giao thức (protocol / 프로토콜) và vòng đời driver**, **Cầu nối (bridge / 브리지)** tiếp nhận điểm tựa từ **5. khả năng quan sát (observability / 관측 가능성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [embedded systems](../embedded_systems/01_rtos_scheduling_verification.md) cho scheduling/quyền sở hữu (ownership / 소유권) và Khoa học máy tính (computer science / 컴퓨터 과학) về API evolution, tính đồng thời (concurrency / 동시성) và fault khôi phục (recovery / 복구).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
