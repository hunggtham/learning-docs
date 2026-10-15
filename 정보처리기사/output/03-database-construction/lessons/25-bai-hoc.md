# 10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và mục tiêu sống còn của Kiểm soát đồng thời (`병행제어 / Concurrency Control`): Đảm bảo tính khả tuần tự (`직렬성 / Serializability`) và ngăn chặn 4 thảm họa khi nhiều giao dịch chạy song song (Mất cập nhật, Mâu thuẫn dữ liệu, Hoàn tác dây chuyền, Đọc dữ liệu rác).
- Phân tích chi tiết 4 kỹ thuật kiểm soát đồng thời: **Khóa tài nguyên (`로킹 / Locking`)**, **Gắn mốc thời gian (`타임스탬프 / Time Stamping`)**, **Kiểm soát đồng thời đa phiên bản (`MVCC`)**, và **Kiểm soát lạc quan (`낙관적 병행제어`)**.
- Nắm chắc quy luật đánh đổi của Đơn vị khóa (`로킹 단위 / Locking Granularity`): Đơn vị khóa càng lớn thì chi phí quản lý càng nhỏ nhưng tính đồng thời càng giảm, và ngược lại.
- Hiểu rõ bản chất của Hệ thống ca-ta-lô / Từ điển dữ liệu (`시스템 카탈로그 / 데이터 사전`): DBMS tự động quản lý, người dùng chỉ có quyền tra cứu (`SELECT`).

## 핵심 키워드 (Từ khóa)
- 병행제어 (Kiểm soát đồng thời / Concurrency Control)
- 직렬화 (Tính khả tuần tự / Serializability)
- 갱신 분실 (Mất cập nhật / Lost Update)
- 모순성 (Tính mâu thuẫn không nhất quán / Inconsistency)
- 연쇄 복귀 (Hoàn tác dây chuyền / Cascading Rollback)
- 로킹 (Cơ chế khóa / Locking)
- 로킹 단위 (Đơn vị khóa / Locking Granularity)
- 2단계 로킹 규약 (Giao thức khóa 2 pha / 2PL)
- 시스템 카탈로그 (Hệ thống ca-ta-lô / System Catalog / Data Dictionary)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([22-bai-hoc.md](22-bai-hoc.md), [23-bai-hoc.md](23-bai-hoc.md), [24-bai-hoc.md](24-bai-hoc.md)):** Để duy trì đặc tính Cô lập (Isolation) và Nhất quán (Consistency) của ACID trong môi trường đa người dùng, hệ CSDL bắt buộc phải áp dụng các kỹ thuật kiểm soát đồng thời.
- **Tiếp nối sang các bài sau ([26-bai-hoc.md](26-bai-hoc.md), [27-bai-hoc.md](27-bai-hoc.md)):** Các lệnh điều khiển giao dịch TCL (`COMMIT`, `ROLLBACK`) và phân quyền DCL (`GRANT`, `REVOKE`) trong SQL chính là công cụ lập trình trực tiếp tương tác với hệ thống quản trị giao dịch và ca-ta-lô.

## 읽는 방법 (Cách đọc)
- Học thuộc quy luật đánh đổi Đơn vị khóa ở TẦNG A: **Đơn vị khóa TO $\rightarrow$ ít Lock, chi phí nhẹ, tính đồng thời KÉM; Đơn vị khóa NHỎ $\rightarrow$ nhiều Lock, chi phí nặng, tính đồng thời CAO**.
- Nhớ 4 lỗi khi không kiểm soát đồng thời: Mất cập nhật (`갱신 분실`), Mâu thuẫn (`모순성`), Hoàn tác dây chuyền (`연쇄 복귀`), Đọc rác (`비완료 의존성 / Dirty Read`).
- Nhớ đặc điểm của Ca-ta-lô: DBMS tự cập nhật, người dùng **CHỈ ĐƯỢC XEM (SELECT)**, cấm INSERT/UPDATE/DELETE thủ công.

---

## 10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bốn sự cố nghiêm trọng khi không kiểm soát đồng thời (병행제어 미수행 시 문제점):**
  | Tên sự cố | Thuật ngữ Hàn - Anh | Bản chất lỗi kỹ thuật |
  |---|---|---|
  | **Mất cập nhật** | `갱신 분실` (Lost Update) | Hai giao dịch cùng cập nhật một dữ liệu, giao dịch ghi sau ghi đè làm mất hoàn toàn kết quả của giao dịch trước. |
  | **Tính mâu thuẫn** | `모순성 / 불일치` (Inconsistency) | Hai giao dịch chạy song song, một giao dịch đọc dữ liệu trong khi giao dịch kia đang sửa đổi dở dang, dẫn đến kết quả đọc bị lệch lạc, mâu thuẫn. |
  | **Hoàn tác dây chuyền** | `연쇄 복귀` (Cascading Rollback) | Giao dịch A thay đổi dữ liệu, giao dịch B đọc dữ liệu đó; sau đó giao dịch A bị lỗi Rollback, khiến giao dịch B cũng buộc phải bị Rollback theo hàng loạt. |
  | **Đọc dữ liệu chưa hoàn tất** | `비완료 의존성` (Dirty Read) | Đọc phải dữ liệu trung gian do một giao dịch khác vừa sửa nhưng chưa thực hiện COMMIT (và sau đó giao dịch đó có thể bị Rollback). |

- **2. Bốn kỹ thuật Kiểm soát đồng thời chủ yếu (병행제어 주요 기법):**
  - **로킹 (Locking - Cơ chế khóa):**
    - Giao dịch muốn thao tác trên dữ liệu phải xin quyền khóa (`Lock`). Giao dịch khác muốn truy cập phải chờ đến khi khóa được mở (`Unlock`).
    - **Khóa chia sẻ (Shared Lock - `공유 로킹 / S-Lock`):** Cho phép các giao dịch khác cùng ĐỌC dữ liệu, cấm GHI.
    - **Khóa độc quyền (Exclusive Lock - `전용 로킹 / X-Lock`):** Cho phép ĐỌC và GHI, cấm tuyệt đối mọi giao dịch khác truy cập.
    - **Giao thức 2 pha (2PL - `2단계 로킹 규약`):** Gồm pha mở rộng (chỉ xin Lock, không nhả) và pha thu hẹp (chỉ nhả Lock, không xin thêm); **đảm bảo tính khả tuần tự (직렬성) nhưng vẫn có thể xảy ra Deadlock (교착상태)**.
  - **로킹 단위 (Đơn vị khóa / Locking Granularity) và Quy luật đánh đổi:**
    | Đơn vị khóa | Số lượng khóa (Lock 수) | Chi phí quản lý (오버헤드) | Mức độ đồng thời (병행성) |
    |---|:---:|:---:|:---:|
    | **Lớn (Cả CSDL, Cả Bảng)** | **Ít** | **Nhỏ (đơn giản)** | **Thấp (nhiều giao dịch phải chờ)** |
    | **Nhỏ (Dòng bản ghi, Cột/Trường)** | **Nhiều** | **Lớn (phức tạp)** | **Cao (nhiều giao dịch chạy cùng lúc)** |
  - **타임스탬프 순서 (Time Stamping Order):** Gán nhãn thời gian bắt đầu cho từng giao dịch; sắp xếp thứ tự thực thi theo nhãn thời gian mà không dùng khóa, **hoàn toàn loại trừ nguy cơ Deadlock**.
  - **낙관적 병행제어 (Optimistic Concurrency Control):** Giả định ít khi xảy ra xung đột; cho phép các giao dịch đọc ghi tự do trên vùng đệm, đến cuối pha Kiểm tra hợp lệ (Validation phase) mới kiểm tra xung đột; nếu có xung đột thì Rollback.
  - **MVCC (Multi-Version Concurrency Control):** Tạo ra các bản sao phiên bản cũ của dữ liệu kèm nhãn thời gian, giúp thao tác ĐỌC không bao giờ bị chặn bởi thao tác GHI.
- **3. Hệ thống ca-ta-lô / Từ điển dữ liệu (시스템 카탈로그 / 데이터 사전):**
  - Là cơ sở dữ liệu hệ thống chứa **Siêu dữ liệu (`메타데이터 / Metadata`)** mô tả về tất cả các đối tượng (bảng, chỉ mục, khung nhìn, quyền hạn, người dùng).
  - **Đặc trưng thi trắc nghiệm:**
    - Do DBMS **tự động tạo lập, cập nhật và duy trì** khi người dùng thi hành các câu lệnh DDL.
    - Người dùng thông thường **chỉ có thể tra cứu bằng câu lệnh `SELECT`**.
    - **Nghiêm cấm** người dùng sử dụng các câu lệnh `INSERT`, `UPDATE`, `DELETE` để can thiệp trực tiếp vào ca-ta-lô.
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Đơn vị khóa càng lớn thì tính đồng thời và chi phí thay đổi thế nào?"* $\rightarrow$ **Tính đồng thời GIẢM, chi phí quản lý GIẢM**.
  - Đề hỏi: *"Người dùng có được dùng lệnh UPDATE để sửa Hệ thống ca-ta-lô không?"* $\rightarrow$ **TUYỆT ĐỐI KHÔNG (chỉ được SELECT tra cứu)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa sự cố Mất cập nhật (Lost Update):**
  - Tài khoản có số dư 100 USD.
  - Giao dịch $T_1$ nạp thêm 50 USD (đọc 100, chuẩn bị ghi 150).
  - Cùng lúc đó, giao dịch $T_2$ rút đi 20 USD (cũng đọc 100, chuẩn bị ghi 80).
  - $T_1$ ghi 150. Sau đó 1 giây, $T_2$ ghi 80 đè lên.
  - Kết quả cuối cùng là 80 USD $\rightarrow$ Mất đứt 50 USD nạp vào của $T_1$ do không áp dụng Exclusive Lock!

### 복습 체크리스트
- [ ] Kể tên và giải thích 4 sự cố khi thiếu kiểm soát đồng thời: 갱신 분실, 모순성, 연쇄 복귀, 비완료 의존성.
- [ ] Nắm vững bảng đánh đổi 로킹 단위 (đơn vị to vs đơn vị nhỏ).
- [ ] Phân biệt được Shared Lock (chỉ đọc) và Exclusive Lock (đọc và ghi).
- [ ] Nêu rõ quy tắc bảo mật đối với 시스템 카탈로그 (chỉ DBMS tự cập nhật, người dùng chỉ được SELECT).
