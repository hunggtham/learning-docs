# 운영체제의 목적 및 구성 (Mục đích & Cấu trúc của Hệ điều hành)

## 학습 목표 (Mục tiêu)
- Nắm vững 4 chỉ số hiệu năng đánh giá mục tiêu của hệ điều hành: Thông lượng (처리 능력 - Throughput), Thời gian phản hồi (반환 시간 - Turnaround Time), Tính sẵn sàng (사용 가능도 - Availability), và Độ tin cậy (신뢰도 - Reliability).
- Phân biệt cấu trúc phân loại hai nhóm chương trình trong hệ điều hành: Chương trình điều khiển (제어 프로그램) và Chương trình xử lý (처리 프로그램).
- Hiểu rõ vai trò trung tâm của chương trình giám sát (감시 프로그램 - Supervisor) trong việc điều phối tài nguyên và quản lý CPU.

## 핵심 키워드 (Từ khóa)
- **운영체제 4대 목적 (4 Metrics)**: 처리 능력 향상 (Tăng Throughput), 반환 시간 단축 (Giảm Turnaround Time), 사용 가능도 증대 (Tăng Availability), 신뢰도 향상 (Tăng Reliability).
- **제어 프로그램 (Control Programs)**: 감시 프로그램 (Supervisor - cốt lõi nhất), 작업 관리 (Job Management), 데이터 관리 (Data Management).
- **처리 프로그램 (Processing Programs)**: 언어 번역 프로그램 (Language Translators - Compiler, Assembler), 서비스/유틸리티 프로그램 (Service Programs).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [57-bai-hoc.md](57-bai-hoc.md) (Đặc trưng của Windows và UNIX).
- Liên kết với [58-bai-hoc.md](58-bai-hoc.md) (Kiến trúc Kernel, Shell và Utility trong UNIX).
- Liên kết với [62-bai-hoc.md](62-bai-hoc.md) (Quản lý tiến trình và PCB).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý hướng biến thiên của 4 chỉ số đánh giá mục đích hệ điều hành:
  - Chỉ có **반환 시간 (Turnaround Time)** là càng **thấp/ngắn** càng tốt!
  - Ba chỉ số còn lại: **처리 능력 (Thông lượng)**, **사용 가능도 (Sẵn sàng)**, **신뢰도 (Tin cậy)** đều càng **cao/lớn** càng tốt.
  - "Chương trình cốt lõi quan trọng nhất trong nhóm 제어 프로그램 là gì?" $\rightarrow$ Chọn ngay **감시 프로그램 (Supervisor)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bốn chỉ số mục tiêu đánh giá Hệ điều hành
| Chỉ số đánh giá (KR / EN) | Định nghĩa kỹ thuật | Xu hướng tối ưu mong muốn |
| :--- | :--- | :--- |
| **처리 능력 (Throughput)** | Khối lượng công việc mà hệ thống có thể xử lý hoàn thành trong một đơn vị thời gian | **Tối đa hóa (Càng cao càng tốt)** |
| **반환 시간 (Turnaround Time)** | Tổng thời gian tính từ lúc người dùng nộp yêu cầu/công việc vào hệ thống cho đến khi nhận được kết quả hoàn tất | **Tối thiểu hóa (Càng ngắn/thấp càng tốt)** |
| **사용 가능도 (Availability)** | Tỷ lệ thời gian hoặc mức độ mà hệ thống luôn sẵn sàng phục vụ tức thì khi người dùng cần sử dụng | **Tối đa hóa (Càng cao càng tốt)** |
| **신뢰도 (Reliability)** | Khả năng hệ thống thực thi các tác vụ một cách chính xác, không gặp lỗi hỏng trong suốt quá trình xử lý | **Tối đa hóa (Càng cao càng tốt)** |

#### 2. Cấu trúc hai khối chương trình của Hệ điều hành
- **제어 프로그램 (Chương trình điều khiển - Control Programs)**:
  - **감시 프로그램 (Supervisor Program)**: Thành phần hạt nhân cốt lõi nhất của OS, thường trực trên RAM để điều phối mọi hoạt động phần cứng, quản lý ngắt, cấp phát bộ nhớ và chuyển đổi tác vụ CPU.
  - **작업 관리 프로그램 (Job Management Program)**: Quản lý trình tự nạp, lập lịch thực thi và kết thúc công việc (Job) của người dùng một cách tuần tự hoặc đa nhiệm.
  - **데이터 관리 프로그램 (Data/File Management Program)**: Quản lý việc đọc, ghi, tìm kiếm và phân phối các tệp tin dữ liệu giữa bộ nhớ chính và các thiết bị ngoại vi lưu trữ.
- **처리 프로그램 (Chương trình xử lý - Processing Programs)**:
  - **언어 번역 프로그램 (Language Translators)**: Chuyển đổi mã nguồn của lập trình viên thành mã máy (ví dụ: Trình biên dịch Compiler, Trình hợp dịch Assembler, Trình thông dịch Interpreter).
  - **서비스 프로그램 (Service Programs / Utility)**: Các công cụ tiện ích hỗ trợ người dùng và hệ thống như chương trình chẩn đoán, dọn dẹp đĩa, sao lưu, trình liên kết (Linker) và nạp (Loader).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ phân cấp cấu trúc Hệ điều hành
```
                     ┌──────────────────────────────────────────────┐
                     │            HỆ ĐIỀU HÀNH (OS)                 │
                     ├──────────────────────┬───────────────────────┤
                     │   제어 프로그램      │    처리 프로그램      │
                     │  (Control Programs)  │ (Processing Programs) │
                     ├──────────────────────┼───────────────────────┤
                     │ - 감시 (Supervisor)  │ - 언어 번역 (Compiler)│
                     │ - 작업 (Job Mgmt)    │ - 서비스 (Service)    │
                     │ - 데이터 (Data Mgmt) │ - 사용자 프로그램     │
                     └──────────────────────┴───────────────────────┘
```

#### 2. Thành phần chi tiết của Turnaround Time (Thời gian phản hồi)
- Thời gian phản hồi hoàn chỉnh của một công việc bao gồm 4 giai đoạn cộng dồn:
  $$\text{Turnaround Time} = \text{Thời gian chờ trong hàng đợi} + \text{Thời gian cấp phát tài nguyên} + \text{Thời gian thực thi CPU} + \text{Thời gian xuất kết quả (I/O)}$$
- Việc tối ưu hệ điều hành nhằm giảm thiểu thời gian chờ đợi lãng phí trong hàng đợi (Waiting Time) chứ không chỉ đơn thuần là tăng xung nhịp CPU.

---

### 복습 체크리스트
- [ ] Trong 4 chỉ số đánh giá mục đích của hệ điều hành, chỉ số duy nhất cần giảm thiểu (càng nhỏ càng tốt) là gì?
- [ ] Chương trình giám sát (감시 프로그램 - Supervisor) thuộc nhóm chương trình điều khiển hay chương trình xử lý?
- [ ] Kể tên 3 chương trình con cấu thành nên nhóm 제어 프로그램 (Chương trình điều khiển)?
- [ ] Trình biên dịch (Compiler) thuộc nhóm chương trình nào trong hệ điều hành?
