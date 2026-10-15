# 190. CRUD 분석

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa của Phân tích CRUD (`CRUD 분석 / CRUD Analysis`): Kỹ thuật lập ma trận đối chiếu giữa các Tiến trình nghiệp vụ ứng dụng (`프로세스 / Process`) và các Bảng dữ liệu (`테이블 / Entity`) nhằm kiểm tra sự phù hợp của mô hình dữ liệu.
- Hiểu rõ 4 thao tác cơ bản cấu thành CRUD và câu lệnh SQL tương ứng: **Create (`생성 - INSERT`)**, **Read (`읽기 - SELECT`)**, **Update (`갱신 - UPDATE`)**, và **Delete (`삭제 - DELETE`)**.
- Nắm vững các ứng dụng quan trọng của Ma trận CRUD: Nắm bắt tần suất phát sinh giao dịch theo chu kỳ (`주기별 발생 횟수 파악`), Ước lượng dung lượng dữ liệu (`데이터의 양 유추`), và Phát hiện các khiếm khuyết trong thiết kế hệ thống.

## 핵심 키워드 (Từ khóa)
- CRUD 분석 (Phân tích CRUD / CRUD Analysis)
- CRUD 매트릭스 (Ma trận CRUD / CRUD Matrix)
- 생성 (Create / INSERT)
- 읽기 (Read / SELECT)
- 갱신 (Update / UPDATE)
- 삭제 (Delete / DELETE)
- 트랜잭션 발생 횟수 (Tần suất phát sinh giao dịch)
- 데이터 용량 산정 (Ước lượng dung lượng dữ liệu)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([22-bai-hoc.md](22-bai-hoc.md), [26-bai-hoc.md](26-bai-hoc.md), [44-bai-hoc.md](44-bai-hoc.md)):** Sau khi định nghĩa các bảng trong ca-ta-lô và hiểu bản chất các lệnh DML, kỹ sư tiến hành phân tích CRUD để liên kết giữa phần mềm ứng dụng và hệ CSDL.
- **Tiếp nối sang các bài sau ([46-bai-hoc.md](46-bai-hoc.md), [47-bai-hoc.md](47-bai-hoc.md)):** Các bảng có tần suất Create/Update quá cao trong ma trận CRUD sẽ là đối tượng ưu tiên hàng đầu để tiến hành phân vùng (`파티션`) và tối ưu hóa chỉ mục.

## 읽는 방법 (Cách đọc)
- Học thuộc 4 chữ cái CRUD và câu lệnh SQL tương ứng ở TẦNG A:
  - **C $\rightarrow$ Create (생성 / INSERT)**.
  - **R $\rightarrow$ Read (읽기 / SELECT)**.
  - **U $\rightarrow$ Update (갱신 / UPDATE)**.
  - **D $\rightarrow$ Delete (삭제 / DELETE)**.
- Nhớ câu hỏi đề thi: **Phân tích CRUD dùng để làm gì? $\rightarrow$ Nắm bắt tần suất giao dịch (트랜잭션 주기별 발생 횟수) và Ước lượng dung lượng dữ liệu (데이터의 양 유추)**.
- Nhớ quy tắc kiểm tra: Mọi bảng bắt buộc phải có ít nhất một chữ **C** (có nơi tạo ra) và ít nhất một chữ **R** (có nơi sử dụng).

---

## 190. CRUD 분석

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Khái niệm Phân tích CRUD (CRUD 분석의 정의):**
  - Là phương pháp phân tích sự tương tác giữa các **Tiến trình nghiệp vụ (Process)** của hệ thống ứng dụng và các **Thực thể dữ liệu (Entity / Table)** của CSDL thông qua một bảng ma trận hai chiều gọi là **Ma trận CRUD (`CRUD 매트릭스`)**.
  - **Bốn thao tác cơ bản và ánh xạ SQL:**
    | Chữ cái | Thao tác tiếng Anh | Thuật ngữ tiếng Hàn | Câu lệnh SQL tương ứng | Ý nghĩa nghiệp vụ |
    |:---:|---|---|:---:|---|
    | **C** | **Create** | `생성` | `INSERT` | Tạo mới và ghi bản ghi vào bảng |
    | **R** | **Read** | `읽기` | `SELECT` | Đọc và tra cứu thông tin từ bảng |
    | **U** | **Update** | `갱신` | `UPDATE` | Chỉnh sửa nội dung thuộc tính đã có |
    | **D** | **Delete** | `삭제` | `DELETE` | Xóa bỏ bản ghi ra khỏi bảng |

- **2. Ứng dụng thực tế của Ma trận CRUD (CRUD 매트릭스의 활용):**
  - **Đo lường tần suất giao dịch:** Xác định số lần thao tác C, R, U, D phát sinh trên từng bảng theo chu kỳ (ngày, tuần, tháng) để phát hiện điểm nghẽn cổ chai (Bottleneck).
  - **Ước tính dung lượng lưu trữ (`데이터의 양 유추`):** Dựa vào số lượng thao tác Create (Insert) nhân với kích thước trung bình của một bản ghi để dự đoán tốc độ phình to của CSDL.
  - **Kiểm tra tính nhất quán và hoàn thiện:** Phát hiện sự thiếu sót giữa thiết kế phần mềm và thiết kế CSDL trước khi bước vào giai đoạn lập trình.
- **3. Quy tắc thẩm định chất lượng Ma trận CRUD (CRUD 점검 기준):**
  - **Quy tắc đối với Entity (Cột dọc):** Mỗi thực thể (bảng) bắt buộc phải có **ít nhất một chữ `C`** và **ít nhất một chữ `R`**.
    - Nếu không có `C`: Dữ liệu không bao giờ được tạo ra (thực thể vô căn cứ).
    - Nếu không có `R`: Dữ liệu được tạo ra nhưng không ai dùng đến (thực thể rác, thừa thãi).
  - **Quy tắc đối với Process (Hàng ngang):** Mỗi tiến trình nghiệp vụ phải có ít nhất một thao tác C, R, hoặc U trên ít nhất một bảng dữ liệu.
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Phương pháp nào giúp nắm bắt số lần phát sinh giao dịch theo chu kỳ và ước tính dung lượng dữ liệu trên các bảng?"* $\rightarrow$ Đáp án: **CRUD 분석 (Phân tích CRUD)**.
  - Đề hỏi: *"Một thực thể trong ma trận CRUD không có chữ R nào thì biểu thị điều gì?"* $\rightarrow$ Đáp án: **Dữ liệu được tạo ra nhưng không bao giờ được sử dụng (데이터가 활용되지 않음)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa Ma trận CRUD trong hệ thống bán hàng:**
  | Tiến trình nghiệp vụ (Process) | Bảng KHACH_HANG | Bảng SAN_PHAM | Bảng DON_HANG |
  |---|:---:|:---:|:---:|
  | Đăng ký tài khoản mới | **C** | | |
  | Tìm kiếm sản phẩm | | **R** | |
  | Đặt mua hàng | **R** | **R, U** | **C** |
  | Hủy đơn hàng | | **U** | **U, D** |
  | Xem lịch sử mua hàng | **R** | | **R** |
  - Nhận xét:
    - Bảng `DON_HANG` có thao tác `C` (Đặt hàng) và `R` (Xem lịch sử) $\rightarrow$ Thỏa mãn tiêu chuẩn kiểm toán.
    - Cột `SAN_PHAM` bị `Update` số lượng tồn kho liên tục khi đặt mua $\rightarrow$ Bảng này có tải ghi cao, cần xem xét chiến lược khóa và bộ nhớ đệm.

### 복습 체크리스트
- [ ] Phân tích được ý nghĩa 4 chữ cái: Create (INSERT), Read (SELECT), Update (UPDATE), Delete (DELETE).
- [ ] Nêu 2 mục đích lớn của CRUD: 파악 트랜잭션 발생 횟수 (đo tần suất) và 유추 데이터 양 (ước tính dung lượng).
- [ ] Trình bày quy tắc kiểm tra ma trận: mỗi bảng phải có ít nhất một C và một R.
- [ ] Giải thích hậu quả nếu một bảng không có chữ C hoặc không có chữ R.
