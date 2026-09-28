# MCU thời gian chạy (runtime / 런타임) and Real-Time lập luận (reasoning / 추론) — MCU, thời gian chạy (runtime / 런타임) và real-time

> **Mạch đọc:** Đặt **MCU thời gian chạy (runtime / 런타임) and Real-Time lập luận (reasoning / 추론) — MCU, thời gian chạy (runtime / 런타임) và real-time** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Boot và quyền sở hữu (ownership / 소유권)** sang **2. Interrupt, DMA và tính đồng thời (concurrency / 동시성)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Embedded hệ thống (system / 시스템) là một closed-loop giữa mã (code / 코드) và vật lý (physical / 물리적) world. tính đúng đắn (correctness / 정확성) có hai chiều: giá trị phải đúng (functional correctness) và phải đến đúng deadline (temporal correctness).

## 1. Boot và quyền sở hữu (ownership / 소유권)

Một MCU thường đi qua:

    reset/véc-tơ (vector / 벡터) → clock/power init → bộ nhớ (memory / 메모리) init
    → peripheral init → scheduler/main vòng lặp (loop / 루프) → ứng dụng (application / 애플리케이션)

Mỗi peripheral cần đơn vị sở hữu (owner / 오너) rõ: ai cấu hình, ai đọc/ghi, ai xử lý lỗi (error / 오류), và trạng thái khi reset/power chuyển tiếp (transition / 전이) là gì. toàn cục (global / 전역) register truy cập (access / 접근) không phải kiến trúc (architecture / 아키텍처).


> **Chuyển mạch:** Từ **1. Boot và quyền sở hữu (ownership / 소유권)**, ta sang **2. Interrupt, DMA và tính đồng thời (concurrency / 동시성)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. Interrupt, DMA và tính đồng thời (concurrency / 동시성)

Interrupt handler nên ngắn: acknowledge nguồn (source / 소스), capture minimal trạng thái (state / 상태), enqueue công việc (work / 작업). lô-gic (logic / 논리) dài trong ISR làm tăng độ trễ (latency / 지연 시간) của interrupt khác và gây jitter.

DMA giảm CPU bản sao (copy / 복사) nhưng tạo quyền sở hữu (ownership / 소유권) bài toán (problem / 문제):

    producer writes buffer → bộ nhớ (memory / 메모리) visibility/bộ nhớ đệm (cache / 캐시) sync
    → bên tiêu thụ (consumer / 소비자) reads → producer reclaims

Buffer descriptor cần trạng thái rõ ràng; không dùng một flag thiếu bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) để đồng bộ giữa CPU/DMA.


> **Chuyển mạch:** Từ **2. Interrupt, DMA và tính đồng thời (concurrency / 동시성)**, ta sang **3. Real-time ngân sách (budget / 예산)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. Real-time ngân sách (budget / 예산)

Với tác vụ (task / 작업) periodic, utilization đơn giản là:

    U = tổng Ci / Ti

Ci là worst-case thực thi (execution / 실행) thời gian (time / 시간), Ti là period. Average thực thi (execution / 실행) thời gian (time / 시간) không đủ cho deadline phân tích (analysis / 분석). Cần cộng interrupt interference, blocking, trượt bộ nhớ đệm (cache miss / 캐시 미스), bus contention và an toàn (safety / 안전) margin.

Jitter có thể làm vòng điều khiển (control loop / 제어 루프) kém ổn định dù average frequency đúng.


> **Chuyển mạch:** Từ **3. Real-time ngân sách (budget / 예산)**, ta sang **4. Timer và timestamp** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. Timer và timestamp

Hardware timer overflow là bình thường. Timestamp nên so sánh theo modulo arithmetic:

    elapsed = now - then

với điều kiện interval nhỏ hơn nửa chu kỳ counter. Không đổi timer ticks sang milliseconds bằng integer division sớm nếu cần precision.


> **Chuyển mạch:** Từ **4. Timer và timestamp**, ta sang **5. an toàn (safety / 안전) và degraded chế độ (mode / 모드)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. an toàn (safety / 안전) và degraded chế độ (mode / 모드)

Watchdog không sửa được mọi lỗi; nó chỉ reset khi software không kick đúng đặc tả hợp đồng (contract / 계약). Thiết kế cần xác định reset có làm actuator về trạng thái (state / 상태) an toàn không, brownout có thể ghi dở persistent trạng thái (state / 상태) không, sensor invalid có được phát hiện bằng phạm vi (range / 범위)/tỷ lệ (rate / 비율)/plausibility checks không, firmware cập nhật (update / 업데이트) thất bại (fail / 실패) giữa chừng có quay lui (rollback / 롤백) không.


> **Chuyển mạch:** Từ **5. an toàn (safety / 안전) và degraded chế độ (mode / 모드)**, ta sang **6. Worked lập luận (reasoning / 추론): sampling sensor 1 kHz** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 6. Worked lập luận (reasoning / 추론): sampling sensor 1 kHz

Nếu sensor cần mẫu (sample / 표본) mỗi 1 ms, tác vụ (task / 작업) period là 1 ms. Nhưng deadline thực tế bao gồm ADC acquisition, DMA completion, filter, điều khiển (control / 제어) calculation và đầu ra (output / 출력) cập nhật (update / 업데이트). Nếu worst-case là 0.7 ms, utilization riêng tác vụ (task / 작업) là 70%; thêm ISR và communication có thể vượt ngân sách (budget / 예산). Tăng average CPU speed không chứng minh worst-case pass nếu bus contention chưa đo.


> **Chuyển mạch:** Từ **6. Worked lập luận (reasoning / 추론): sampling sensor 1 kHz**, ta sang **7. Bring-up và bằng chứng (evidence / 증거)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 7. Bring-up và bằng chứng (evidence / 증거)

Trình tự bring-up nên cô lập miền lỗi (failure domain / 장애 도메인):

    power rails → clock/reset → gỡ lỗi (debug / 디버그) link → GPIO heartbeat
    → one peripheral → sensor đường dẫn (path / 경로) → actuator guarded → full ứng dụng (application / 애플리케이션)

Mỗi bước cần waveform/register/log bằng chứng (evidence / 증거). Nếu chỉ “board chạy”, ta không biết timing margin hoặc khôi phục (recovery / 복구) hành vi (behavior / 동작).


> **Chuyển mạch:** Từ **7. Bring-up và bằng chứng (evidence / 증거)**, ta sang **thất bại (failure / 실패) modes** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Thất bại (failure / 실패) modes

- priority inversion làm tác vụ (task / 작업) quan trọng miss deadline;
- ISR và main vòng lặp (loop / 루프) cùng sửa buffer không có quyền sở hữu (ownership / 소유권);
- trình biên dịch (compiler / 컴파일러) tối ưu hóa (optimization / 최적화) làm register truy cập (access / 접근) sai vì thiếu volatile/barrier;
- watchdog reset nhưng không lưu fault cause;
- firmware cập nhật (update / 업데이트) đổi register đặc tả hợp đồng (contract / 계약) mà driver cũ vẫn chạy.


> **Chuyển mạch:** Từ **thất bại (failure / 실패) modes**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [hardware–software interfaces](../hardware_software_interfaces/00_register_bus_driver_contracts.md), [digital electronics](../digital_electronics/00_logic_timing_state.md) và Khoa học máy tính (computer science / 컴퓨터 과학) về tính đồng thời (concurrency / 동시성)/kiến trúc (architecture / 아키텍처).

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 rtos scheduling verification](./01_rtos_scheduling_verification.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
