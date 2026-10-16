# 데이터베이스와 쿼리 성능 최적화 (Cơ sở dữ liệu và tối ưu hóa truy vấn)

## 학습 목표
- Nắm vững kiến trúc 3 tầng lược đồ ANSI/SPARC: Lược đồ ngoài (`외부 스키마`), Lược đồ quan niệm (`개념 스키마`), Lược đồ trong (`내부 스키마`), và 2 cấp độ độc lập dữ liệu logic và vật lý.
- Phân biệt bản chất, phương thức kích hoạt và giá trị trả về của 3 đối tượng SQL thủ tục: Thủ tục lưu trữ (`저장 프로시저`), Trigger (`트리거`), và Hàm người dùng định nghĩa (`사용자 정의 함수`).
- Nhận diện bẫy cấm tuyệt đối chứa lệnh điều khiển giao dịch `COMMIT` hoặc `ROLLBACK` bên trong Trigger.
- Làm chủ quy trình 3 bước tối ưu hóa hiệu năng truy vấn: Chọn đối tượng (`대상 선정` qua APM) $\rightarrow$ Đánh giá kế hoạch (`계획 검토` qua Execution Plan) $\rightarrow$ Tái cấu trúc và tinh chỉnh (`재구성 및 튜닝`).
- So sánh bộ tối ưu hóa RBO (dựa trên 15 quy tắc cố định) vs CBO (dựa trên chi phí ước tính từ số liệu thống kê) và các bẫy làm vô hiệu hóa Index gây Full Table Scan.

## 핵심 키워드
- 스키마 3계층 (Kiến trúc 3 tầng lược đồ / 외부 External, 개념 Conceptual, 내부 Internal)
- 데이터 독립성 (Độc lập dữ liệu / 논리적 데이터 독립성, 물리적 데이터 독립성)
- 절차형 SQL (PL/SQL / 프로시저 Procedure, 트리거 Trigger, 사용자 정의 함수 Function)
- 트리거 제약 (Trigger / COMMIT, ROLLBACK 사용 불가)
- 쿼리 성능 최적화 (Tối ưu hóa truy vấn / APM, 실행 계획 Execution Plan, Full Table Scan)
- 옵티마이저 (Bộ tối ưu hóa / RBO 규칙기반, CBO 비용기반, 옵티마이저 힌트)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [06-thuat-toan-tim-kiem-va-bang-bam.md](06-thuat-toan-tim-kiem-va-bang-bam.md), chúng ta đã khảo sát các giải thuật tìm kiếm nhị phân và cấu trúc bảng băm tức thời $O(1)$ trên RAM.
- **Đang giải quyết gì (Current Problem):** Bài học này khép lại Chương 1, đưa người học từ RAM sang không gian lưu trữ CSDL bền vững dưới góc nhìn của kỹ sư phần mềm: bảo vệ chương trình qua tính độc lập dữ liệu 3 tầng lược đồ, đóng gói nghiệp vụ qua SQL thủ tục và tối ưu hóa thời gian chạy câu lệnh truy vấn.
- **Dùng đi đâu (Forward Handoff):** Sau khi hoàn tất Chương 1 về dữ liệu và thuật toán, chúng ta chính thức bước sang Chương 2 về tích hợp hệ thống với [08-hien-thuc-module-va-ipc.md](08-hien-thuc-module-va-ipc.md) để khảo sát hiện thực module và giao tiếp liên tiến trình IPC.

## 읽는 방법
- Đọc TẦNG A để nắm chắc bảng nén 3 tầng lược đồ, bảng đối chiếu 3 đối tượng SQL thủ tục (Trigger cấm TCL), và danh sách các lỗi viết SQL làm mất tác dụng Index.
- Đọc TẦNG B để hiểu sâu cơ chế của bộ tối ưu CBO và quy trình debug PL/SQL bằng gói DBMS_OUTPUT.

---

## 데이터베이스와 쿼리 성능 최적화

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng phân định 3 tầng lược đồ ANSI/SPARC
| Tầng lược đồ | Tên tiếng Hàn & Anh | Đối tượng sử dụng | Phạm vi và nội dung thể hiện |
| :--- | :--- | :--- | :--- |
| **Tầng Ngoài** | **외부 스키마 (External)** | Người dùng cuối, **Lập trình viên** | Còn gọi là **User View / Sub-schema**; chỉ hiển thị phạm vi nghiệp vụ riêng, che giấu dữ liệu khác (có nhiều Lược đồ ngoài) |
| **Tầng Quan niệm** | **개념 스키마 (Conceptual)** | Quản trị viên CSDL (DBA) | Thể hiện cấu trúc **toàn bộ dữ liệu logic của tổ chức**; định nghĩa bảng, quan hệ, ràng buộc toàn vẹn (**duy nhất 1**) |
| **Tầng Trong** | **내부 스키마 (Internal)** | Kỹ sư hệ thống, Nhân DBMS | Cấu trúc **lưu trữ vật lý thực tế trên đĩa cứng**; định nghĩa định dạng record, block, chỉ mục B-Tree (**duy nhất 1**) |

#### 2. Hai cấp độ độc lập dữ liệu (데이터 독립성)
- **논리적 데이터 독립성 (Độc lập logic):** Thông qua ánh xạ `외부 - 개념 사상`. Khi sửa đổi cấu trúc bảng ở tầng Conceptual (thêm cột, gộp bảng), các chương trình ứng dụng ở tầng External **không bị ảnh hưởng, không cần viết lại mã**.
- **물리적 데이터 독립성 (Độc lập vật lý):** Thông qua ánh xạ `개념 - 내부 사상`. Khi thay đổi ổ cứng vật lý, đổi kích thước block hay tạo lại index ở tầng Internal, Lược đồ quan niệm Conceptual **hoàn toàn không bị xáo trộn**.

#### 3. Bảng đối chiếu 3 đối tượng SQL thủ tục
| Tiêu chí | 프로시저 (Stored Procedure) | 트리거 (Trigger) | 사용자 정의 함수 (User Function) |
| :--- | :--- | :--- | :--- |
| **Cách kích hoạt** | Gọi trực tiếp bằng `EXECUTE` hoặc `CALL` | Kích hoạt tự động khi có sự kiện DML (`INSERT`, `UPDATE`, `DELETE`) | Gọi nhúng trực tiếp trong câu lệnh SQL (`SELECT func()`) |
| **Giá trị trả về** | Không có lệnh `RETURN`; trả kết quả qua tham số `OUT` | **Hoàn toàn không trả về giá trị (반환값 없음)** | **Bắt buộc phải trả về 1 giá trị duy nhất** qua lệnh `RETURN` |
| **Lệnh giao dịch TCL** | Cho phép dùng `COMMIT` và `ROLLBACK` | **TUYỆT ĐỐI CẤM dùng `COMMIT` hoặc `ROLLBACK`** | Không được phép thay đổi dữ liệu hoặc commit |

#### 4. Đối chiếu bộ tối ưu hóa: RBO vs CBO
| Tiêu chí | RBO (Rule-Based Optimizer) | CBO (Cost-Based Optimizer) |
| :--- | :--- | :--- |
| **Cơ sở quyết định** | Áp dụng cứng nhắc theo thứ tự 15 quy tắc ưu tiên định sẵn | Tính toán **chi phí ước lượng nhỏ nhất (최소 비용)** |
| **Dữ liệu thống kê** | Không cần dữ liệu thống kê số lượng bản ghi | **Bắt buộc phải có số liệu thống kê thực tế (Analyze/Statistics)** |
| **Khả năng thích ứng**| Cố định, không linh hoạt theo kích thước dữ liệu | Linh hoạt và thông minh theo dữ liệu thực tế |

#### 5. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Lệnh giao dịch trong Trigger:** Trigger **tuyệt đối không được chứa câu lệnh `COMMIT` hoặc `ROLLBACK`** vì nó chạy chung Transaction với câu lệnh DML kích hoạt.
- **Bẫy 2: Lỗi làm mất Index gây Full Table Scan:**
  - Viết hàm hoặc phép tính trên cột Index: `WHERE SUBSTR(EMP_ID, 1, 2) = '10'` hoặc `WHERE SALARY * 12 > 5000` $\rightarrow$ Mất Index.
  - Viết ký tự đại diện `%` ở đầu chuỗi: `WHERE NAME LIKE '%KIM'` $\rightarrow$ Mất Index. (Viết `WHERE NAME LIKE 'KIM%'` thì dùng được Index).
- **Bẫy 3: Hàm người dùng định nghĩa:** User-Defined Function **bắt buộc phải có mệnh đề `RETURN`** trả về giá trị.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Quy trình tối ưu hóa truy vấn 3 bước tiêu chuẩn
1. **1단계: 대상 선정 (Xác định mục tiêu):** Sử dụng công cụ APM (Scouter, Jennifer, Pinpoint) giám sát ứng dụng để lọc ra các câu lệnh SQL chạy chậm (Slow Query) hoặc tốn nhiều tài nguyên I/O.
2. **2단계: 계획 검토 (Phân tích kế hoạch thực thi):** Dùng lệnh `EXPLAIN PLAN` xem Optimizer lựa chọn Index Range Scan hay bị rơi vào Full Table Scan (quét toàn bộ bảng).
3. **3단계: 재구성 및 튜닝 (Tái cấu trúc và tinh chỉnh):** Sửa lại cú pháp mệnh đề `WHERE`, loại bỏ phép tính quanh cột index hoặc chèn gợi ý điều khiển `/*+ INDEX(...) */` (Optimizer Hint).

#### 2. Quy trình gỡ lỗi PL/SQL
- Sử dụng gói chuẩn của Oracle: `DBMS_OUTPUT.PUT_LINE(biến);`.
- Trên màn hình dòng lệnh, bắt buộc phải bật ngõ ra: `SET SERVEROUTPUT ON;` trước khi gọi thủ tục.
- Chú thích (comment out) các dòng lệnh `INSERT/UPDATE/DELETE` nguy hiểm khi thử nghiệm luồng logic.

---

### 복습 체크리스트
- [ ] Phân biệt 3 tầng lược đồ: 외부 (User View), 개념 (Toàn thể logic), 내부 (Lưu trữ vật lý).
- [ ] Nhớ hệ thống có nhiều 외부 스키마 nhưng chỉ có 1 개념 스키마 và 1 내부 스키마.
- [ ] Phân biệt 논리적 데이터 독립성 (sửa 개념 không sửa 외부) và 물리적 데이터 독립성 (sửa 내부 không sửa 개념).
- [ ] Phân biệt 3 đối tượng SQL thủ tục: Procedure (gọi bằng EXEC/CALL), Trigger (tự động khi có sự kiện), Function (nhúng trong SELECT).
- [ ] Nhớ Trigger TUYỆT ĐỐI KHÔNG ĐƯỢC CHỨA lệnh COMMIT hoặc ROLLBACK.
- [ ] Nhớ User-Defined Function bắt buộc phải có mệnh đề RETURN trả về giá trị đơn lẻ.
- [ ] Nhớ lệnh in log gỡ lỗi trong PL/SQL là DBMS_OUTPUT.PUT_LINE.
- [ ] Nắm rõ 3 bước tối ưu hóa truy vấn: 대상 선정 (APM) $\rightarrow$ 계획 검토 (실행 계획) $\rightarrow$ 재구성 (SQL/Index tuning).
- [ ] Phân biệt RBO (dựa trên quy tắc cố định) và CBO (dựa trên chi phí ước tính từ thống kê).
- [ ] Nhận diện các lỗi gây Full Table Scan: bọc hàm quanh cột Index, viết wildcard '%' ở đầu LIKE.
