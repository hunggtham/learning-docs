# 소프트웨어 공학 및 실무 (Software Engineering & Practice)

## 학습 목표 (Mục tiêu)
- Nắm vững chu trình vòng đời quản lý lỗi phần mềm (Defect / Bug Life Cycle) và ý nghĩa nghiệp vụ của các trạng thái lỗi dữ liệu (Error Data States): Open, Assigned, Fixed, Closed, Deferred, Clarified.
- Thuộc lòng 5 đặc tính cốt lõi bắt buộc phải có của chương trình xử lý hàng loạt (배치 프로그램 필수 요소 - Batch Program Elements).
- Ghi nhớ chính xác độ lớn kích thước bộ nhớ (Bytes) của các kiểu dữ liệu mở rộng trong C/C++ (`long long`, `double`, `long double`).

## 핵심 키워드 (Từ khóa)
- 결함 생명주기 (Defect / Bug Life Cycle)
- 오류 데이터 상태 (Open, Assigned, Fixed, Closed, Deferred)
- 배치 프로그램 5대 요소 (대용량 데이터, 자동화, 견고성, 안정성/신뢰성, 성능)
- C/C++ 자료형 크기 (Data Type Sizes: char 1B, int 4B, long long 8B, double 8B)
- 무중단 대용량 처리 (Batch Processing Reliability)

## 선행·연결 개념 (Kiến thức liên kết)
- [51-bai-hoc.md](51-bai-hoc.md): Kiến trúc không gian địa chỉ mạng IPv4 vs IPv6.
- [53-bai-hoc.md](53-bai-hoc.md): Phân loại và đặc trưng các ngôn ngữ lập trình hướng thủ tục.
- [04-bai-hoc.md](04-bai-hoc.md): Kích thước và giới hạn phạm vi kiểu dữ liệu trong C/C++.

## 읽는 방법 (Cách đọc)
- Trong bài thi kỹ sư CNTT Hàn Quốc:
  - Câu hỏi về vòng đời lỗi thường yêu cầu xác định trạng thái khi phát hiện lỗi mới (Open), khi giao việc cho lập trình viên (Assigned), khi dev sửa xong (Fixed), và khi kiểm thử viên xác nhận hoàn tất (Closed).
  - Khẩu quyết 5 yếu tố của Batch Program: **대·자·견·안·성** (Đại - Tự - Kiên - An - Tính): Đại dung lượng, Tự động hóa, Kiên cố (bền bỉ không sập), An định/Tin cậy, và Tính năng (hiệu năng cao).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Chu trình trạng thái vòng đời lỗi phần mềm (Defect Life Cycle):**

| Trạng thái (State) | Ý nghĩa và hành động tương ứng |
| :--- | :--- |
| **Open (Mở lỗi)** | Lỗi mới được phát hiện và ghi nhận vào hệ thống theo dõi (Issue Tracker), chưa xử lý. |
| **Assigned (Giao việc)** | Trưởng nhóm phân tích và bàn giao lỗi cho lập trình viên chịu trách nhiệm sửa chữa. |
| **Fixed (Đã sửa)** | Lập trình viên đã khắc phục xong lỗi và bàn giao lại cho đội kiểm thử xác thực. |
| **Closed (Đóng lỗi)** | Kiểm thử viên (Tester) đã re-test và xác nhận lỗi không còn tái diễn, đóng vé. |
| **Deferred (Hoãn lại)** | Lỗi được xác nhận nhưng độ ưu tiên thấp hoặc dời việc sửa chữa sang phiên bản kế tiếp. |
| **Clarified / Rejected** | Xác nhận báo cáo lỗi không chính xác hoặc hành vi hệ thống hoạt động đúng đặc tả. |
| **Reopened (Mở lại)** | Lỗi sau khi sửa vẫn còn tái phát trong quá trình kiểm thử lại (Regression Testing). |

- **2. 5 yếu tố cốt lõi của chương trình Batch (배치 프로그램 5대 요소):**
  1. **대용량 데이터 (Dữ liệu lớn):** Có khả năng xử lý khối lượng dữ liệu khổng lồ trong các chu kỳ định kỳ.
  2. **자동화 (Tự động hóa):** Vận hành hoàn toàn tự động theo lịch trình đặt trước, không cần sự can thiệp thủ công của người dùng.
  3. **견고성 (Tính kiên cố / Robustness):** Xử lý ngoại lệ chặt chẽ, không bị sập hay gián đoạn hệ thống khi gặp dữ liệu lỗi bất thường.
  4. **안정성 / 신뢰성 (Tính ổn định & Tin cậy):** Đảm bảo tính toán toàn vẹn dữ liệu, có cơ chế ghi log và rollback khi gặp sự cố.
  5. **성능 (Hiệu năng):** Hoàn thành khối lượng công việc lớn trong khoảng thời gian cửa sổ quy định (Batch Window).

- **3. Bảng kích thước kiểu dữ liệu C/C++ cần nhớ:**

| Kiểu dữ liệu | Kích thước (Byte) | Ghi chú thi cử |
| :--- | :--- | :--- |
| `char` | **1 Byte** (8 bit) | Ký tự chuẩn ASCII |
| `short` | **2 Byte** (16 bit) | Số nguyên ngắn |
| `int`, `long` | **4 Byte** (32 bit) | Mặc định số nguyên 32-bit |
| `long long` | **8 Byte** (64 bit) | Số nguyên mở rộng 64-bit |
| `float` | **4 Byte** (32 bit) | Dấu phẩy động độ chính xác đơn |
| `double`, `long double` | **8 Byte** (64 bit) | Dấu phẩy động độ chính xác kép |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Đặc trưng thiết kế hệ thống Batch xử lý ban đêm (Overnight Batch):**
  - Hệ thống Batch thường chạy vào khoảng thời gian hệ thống OLTP (Online Transaction Processing) có lưu lượng truy cập thấp nhất (thường từ 0h đến 5h sáng).
  - Cơ chế phân mảnh công việc (Chunk-based Processing) trong Spring Batch: Đọc dữ liệu theo từng khối (Chunk), xử lý nghiệp vụ, và thực hiện Commit giao dịch theo lô nhằm tối ưu hóa bộ nhớ RAM và giảm thời gian chiếm giữ khóa bảng cơ sở dữ liệu.

### 복습 체크리스트
- [ ] Vẽ được luồng chuyển trạng thái lỗi: Open $\rightarrow$ Assigned $\rightarrow$ Fixed $\rightarrow$ Closed (hoặc Reopened nếu còn lỗi).
- [ ] Phân biệt được trường hợp chuyển sang Deferred (hoãn sửa sang sprint sau) vs Clarified/Rejected (không phải lỗi).
- [ ] Thuộc lòng 5 yếu tố của Batch: Đại dung lượng, Tự động hóa, Kiên cố, Ổn định, Hiệu năng (**대·자·견·안·성**).
- [ ] Ghi nhớ kiểu `long long` và `double` trong C/C++ đều chiếm **8 Byte**.
