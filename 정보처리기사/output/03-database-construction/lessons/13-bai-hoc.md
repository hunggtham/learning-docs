# 5. 스키마 (Schema - Lược đồ)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa của Lược đồ (`스키마 / Schema`): Cấu trúc tổng thể và các ràng buộc của cơ sở dữ liệu.
- Phân biệt chính xác kiến trúc 3 tầng của lược đồ theo tiêu chuẩn ANSI/SPARC: Lược đồ ngoại (`외부 스키마`), Lược đồ khái niệm (`개념 스키마`), và Lược đồ nội (`내부 스키마`).
- Hiểu rõ cơ chế và ý nghĩa của hai tính độc lập dữ liệu: **Tính độc lập dữ liệu logic (`논리적 데이터 독립성`)** và **Tính độc lập dữ liệu vật lý (`물리적 데이터 독립성`)**.

## 핵심 키워드 (Từ khóa)
- 스키마 (Lược đồ / Schema)
- 외부 스키마 (Lược đồ ngoại / External Schema / Subschema)
- 개념 스키마 (Lược đồ khái niệm / Conceptual Schema)
- 내부 스키마 (Lược đồ nội / Internal Schema / Storage Schema)
- 데이터 독립성 (Tính độc lập dữ liệu / Data Independence)
- 논리적 데이터 독립성 (Tính độc lập dữ liệu logic)
- 물리적 데이터 독립성 (Tính độc lập dữ liệu vật lý)
- 사상 / 매핑 (Ánh xạ / Mapping)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([01-bai-hoc.md](01-bai-hoc.md), [02-bai-hoc.md](02-bai-hoc.md), [03-bai-hoc.md](03-bai-hoc.md)):** 3 tầng kiến trúc Schema tương ứng mật thiết với 3 giai đoạn thiết kế CSDL: Thiết kế khái niệm $\rightarrow$ Lược đồ khái niệm; Thiết kế logic $\rightarrow$ Lược đồ logic/ngoại; Thiết kế vật lý $\rightarrow$ Lược đồ nội.
- **Tiếp nối sang các bài sau ([14-bai-hoc.md](14-bai-hoc.md), [15-bai-hoc.md](15-bai-hoc.md)):** Ràng buộc toàn vẹn dữ liệu được đặc tả tại tầng Lược đồ khái niệm (`개념 스키마`) để áp dụng xuyên suốt toàn bộ hệ thống cơ sở dữ liệu.

## 읽는 방법 (Cách đọc)
- Học thuộc câu thần chú thứ tự tầng: **Ngoại - Khái - Nội (외부 $\rightarrow$ 개념 $\rightarrow$ 내부)**.
- Ghi nhớ số lượng: **외부 스키마 có nhiều cái (nhiều góc nhìn)**, còn **개념 스키마 và 내부 스키마 chỉ có DUY NHẤT 1 cái**.
- Nắm chắc ánh xạ độc lập dữ liệu:
  - Logic thay đổi mà Ngoại không đổi $\rightarrow$ **Độc lập dữ liệu logic**.
  - Lưu trữ vật lý thay đổi mà Khái niệm không đổi $\rightarrow$ **Độc lập dữ liệu vật lý**.

---

## 5. 스키마 (Schema - Lược đồ)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Định nghĩa lược đồ (스키마의 정의):**
  - Là bản thiết kế hoặc cấu trúc mô tả cơ sở dữ liệu, bao gồm các đối tượng dữ liệu (thực thể, thuộc tính, mối quan hệ) và các quy tắc ràng buộc toàn vẹn cần tuân thủ.
  - Được lưu trữ trong Từ điển dữ liệu (`데이터 사전 / Data Dictionary`) dưới dạng Siêu dữ liệu (`메타데이터 / Metadata`).
- **2. Kiến trúc 3 tầng Lược đồ ANSI/SPARC (스키마 3계층):**
  | Tầng lược đồ | Thuật ngữ Hàn - Anh | Góc nhìn / Phạm vi | Số lượng | Đặc điểm thi trắc nghiệm |
  |---|---|---|:---:|---|
  | **Lược đồ ngoại** | `외부 스키마` (External Schema / Subschema) | Góc nhìn của người dùng cuối hoặc lập trình viên ứng dụng | **Nhiều (여러 개)** | Chỉ thể hiện phần dữ liệu mà một nhóm người dùng quan tâm. Một CSDL có thể có nhiều lược đồ ngoại khác nhau. |
  | **Lược đồ khái niệm** | `개념 스키마` (Conceptual Schema) | Góc nhìn logic toàn cục của toàn bộ tổ chức doanh nghiệp | **Duy nhất 1 (단 하나)** | Mô tả toàn bộ thực thể, quan hệ, quyền bảo mật và quy tắc toàn vẹn. Là trung tâm của toàn bộ hệ CSDL. |
  | **Lược đồ nội** | `내부 스키마` (Internal / Storage Schema) | Góc nhìn lưu trữ vật lý trên thiết bị phần cứng (ổ đĩa) | **Duy nhất 1 (단 하나)** | Định nghĩa cấu trúc bản ghi lưu trữ, phương pháp lập chỉ mục (index), đường dẫn truy cập và bố trí bộ nhớ. |
- **3. Hai mức Độc lập dữ liệu (데이터 독립성 2단계):**
  - **논리적 데이터 독립성 (Tính độc lập dữ liệu logic):**
    - Được đảm bảo bởi ánh xạ **외부/개념 사상 (Ánh xạ Ngoại - Khái niệm)**.
    - Khái niệm: Khi cấu trúc logic của toàn hệ thống (개념 스키마) thay đổi (như thêm thuộc tính mới, thêm bảng mới), các ứng dụng người dùng (외부 스키마) **không cần phải biên dịch hay sửa đổi lại**.
  - **물리적 데이터 독립성 (Tính độc lập dữ liệu vật lý):**
    - Được đảm bảo bởi ánh xạ **개념/내부 사상 (Ánh xạ Khái niệm - Nội)**.
    - Khái niệm: Khi phương thức lưu trữ vật lý (내부 스키마) thay đổi (như chuyển sang ổ đĩa SSD mới, tái cấu trúc file chỉ mục, tăng kích thước block), cấu trúc logic (개념 스키마) và ứng dụng người dùng **hoàn toàn không bị ảnh hưởng**.
- **주의/함정 (Bẫy đề thi hay gặp):**
  - Đề hỏi: *"Lược đồ nào có thể tồn tại nhiều bản trong một hệ thống CSDL?"* $\rightarrow$ Đáp án: **외부 스키마 (External Schema)**.
  - Đề hỏi: *"Lược đồ nào quản lý toàn diện các quy tắc bảo mật và ràng buộc toàn vẹn?"* $\rightarrow$ Đáp án: **개념 스키마 (Conceptual Schema)**.
  - Đề hỏi: *"Khi thêm một trường mới vào bảng CSDL mà ứng dụng cũ không bị lỗi thì đó là loại độc lập nào?"* $\rightarrow$ Đáp án: **논리적 데이터 독립성 (Tính độc lập dữ liệu logic)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Sơ đồ phân cấp 3 tầng Schema và 2 ánh xạ:**
  $$\text{Người dùng A (외부 1)} \quad \text{Lập trình viên (외부 2)} \quad \text{Quản lý (외부 3)}$$
  $$\downarrow \quad \text{[Ánh xạ Ngoại - Khái niệm: Bảo vệ độc lập Logic]} \quad \downarrow$$
  $$\mathbf{개념\ 스키마\ (Lược\ đồ\ khái\ niệm\ toàn\ cục)}$$
  $$\downarrow \quad \text{[Ánh xạ Khái niệm - Nội: Bảo vệ độc lập Vật lý]} \quad \downarrow$$
  $$\mathbf{내부\ 스키마\ (Cấu\ trúc\ lưu\ trữ\ trên\ ổ\ cứng)}$$
- **Ứng dụng thực tế trong quản trị hệ CSDL (DBMS):**
  - Khi DBA tạo một `VIEW` cho phòng kế toán chỉ xem được cột Lương mà không xem được thông tin cá nhân, `VIEW` đó chính là một phần của **외부 스키마**.
  - Lệnh tạo bảng `CREATE TABLE` và thiết lập khóa chính, khóa ngoại đại diện cho **개념 스키마**.
  - Lệnh tạo chỉ mục `CREATE INDEX`, chọn tablespace hoặc phân vùng ổ đĩa (partitioning) đại diện cho **내부 스키마**.

### 복습 체크리스트
- [ ] Kể tên đúng 3 tầng lược đồ: 외부 스키마, 개념 스키마, 내부 스키마.
- [ ] Phân biệt được lược đồ nào có nhiều (외부) và lược đồ nào chỉ có duy nhất một (개념, 내부).
- [ ] Phân biệt rõ hai tính độc lập: 논리적 데이터 독립성 vs 물리적 데이터 독립성.
- [ ] Nắm được vai trò của Ánh xạ (사상 / Mapping) trong việc duy trì tính độc lập dữ liệu.
