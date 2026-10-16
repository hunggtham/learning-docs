# 데이터 입출력과 쿼리 성능 최적화 (Cơ sở dữ liệu và tối ưu truy vấn)

## 학습 목표
- Nắm vững Kiến trúc 3 tầng lược đồ ANSI/SPARC: Lược đồ ngoài (`외부 스키마`), Lược đồ quan niệm (`개념 스키마`), Lược đồ trong (`내부 스키마`), và 2 cấp độ độc lập dữ liệu: Độc lập logic (`논리적 데이터 독립성`) và Độc lập vật lý (`물리적 데이터 독립성`).
- Phân biệt 3 đối tượng SQL thủ tục (`절차형 SQL / PL/SQL`): Thủ tục lưu trữ (`프로시저 / Stored Procedure`), Trigger (`트리거`), và Hàm do người dùng định nghĩa (`사용자 정의 함수 / User Defined Function`).
- Hiểu rõ quy trình tối ưu hóa truy vấn SQL (SQL Tuning): Giám sát qua APM, phân tích kế hoạch thực thi (`실행 계획 / Execution Plan`), và sự khác biệt giữa Trình tối ưu hóa dựa trên quy tắc (`RBO`) và dựa trên chi phí (`CBO`).
- Nhận diện các bẫy câu lệnh làm vô hiệu hóa chỉ mục Index dẫn đến quét toàn bảng chậm chạp (`Full Table Scan`).

## 핵심 키워드
- 스키마 3계층 (Kiến trúc 3 tầng lược đồ / External, Conceptual, Internal Schema)
- 데이터 독립성 (Tính độc lập dữ liệu / 논리적 독립성 vs 물리적 독립성)
- 절차형 SQL (PL/SQL / 프로시저 Procedure, 트리거 Trigger, 사용자 정의 함수)
- APM & 실행 계획 (Application Performance Monitoring & Execution Plan)
- 옵티마이저 (Optimizer / RBO 규칙 기반 vs CBO 비용 기반)
- 인덱스 무효화 패턴 (Index Invalidation / Full Table Scan 방지)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [06-thuat-toan-tim-kiem-va-bang-bam.md](06-thuat-toan-tim-kiem-va-bang-bam.md), chúng ta đã làm chủ các giải thuật tìm kiếm trong bộ nhớ RAM.
- **Đang giải quyết gì (Current Problem):** Bài học này chuyển dịch sang không gian lưu trữ dữ liệu bền vững (CSDL), giải quyết bài toán độc lập dữ liệu giữa ứng dụng và hệ quản trị CSDL, cùng kỹ thuật tối ưu hóa hiệu năng truy vấn cho kỹ sư phần mềm.
- **Dùng đi đâu (Forward Handoff):** Sau khi hoàn thiện Chương 1, Chương 2 mở màn với [08-hien-thuc-module-va-ipc.md](08-hien-thuc-module-va-ipc.md) để khảo sát thiết kế đơn vị module độc lập và cơ chế giao tiếp liên tiến trình IPC.

## 읽는 방법
- Đọc TẦNG A để nắm bảng phân tích 3 tầng lược đồ, bảng so sánh Procedure vs Trigger vs Function, bảng bẫy tối ưu hóa truy vấn Index và các câu hỏi trắc nghiệm hay gặp.
- Đọc TẦNG B để theo dõi sơ đồ ASCII kiến trúc 3 tầng ANSI/SPARC, cơ chế 2 lớp ánh xạ bảo đảm độc lập dữ liệu và chi tiết cấu trúc PL/SQL.

---

## 데이터 입출력과 쿼리 성능 최적화

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng phân định 3 tầng lược đồ ANSI/SPARC
| Tầng lược đồ | Tên tiếng Hàn & Anh | Đối tượng sử dụng | Phạm vi và nội dung thể hiện |
| :--- | :--- | :--- | :--- |
| **Tầng Ngoài** | **외부 스키마 (External)** | Người dùng, Lập trình viên ứng dụng | Còn gọi là **User View / 서브스키마**; chỉ hiển thị phần dữ liệu riêng của từng ứng dụng |
| **Tầng Quan niệm** | **개념 스키마 (Conceptual)** | DBA, Kiến trúc sư hệ thống | Cấu trúc **toàn bộ dữ liệu logic của tổ chức**; định nghĩa bảng, quan hệ, ràng buộc |
| **Tầng Trong** | **내부 스키마 (Internal)** | Nhân DBMS, Kỹ sư hệ thống | Cấu trúc **lưu trữ vật lý thực tế trên đĩa cứng**; block, index, địa chỉ sector |

*Quy tắc số lượng:* Có **nhiều Lược đồ ngoài**, nhưng **chỉ có duy nhất 1 Lược đồ quan niệm** và **duy nhất 1 Lược đồ trong**.

#### 2. Hai cấp độ độc lập dữ liệu (데이터 독립성)
- **논리적 데이터 독립성 (Độc lập logic):** Thông qua ánh xạ **외부 - 개념 사상**. Khi cấu trúc bảng ở tầng Conceptual thay đổi (thêm cột, sửa bảng), ứng dụng ở tầng External **không bị ảnh hưởng, không cần viết lại mã**.
- **물리적 데이터 독립성 (Độc lập vật lý):** Thông qua ánh xạ **개념 - 내부 사상**. Khi nâng cấp ổ đĩa, đổi block ở tầng Internal, tầng Conceptual và các câu truy vấn **hoàn toàn không bị xáo trộn**.

#### 3. Bảng so sánh 3 đối tượng SQL thủ tục (PL/SQL)
| Tiêu chí | 프로시저 (Stored Procedure) | 트리거 (Trigger) | 사용자 정의 함수 (User Function) |
| :--- | :--- | :--- | :--- |
| **Cách kích hoạt** | Gọi thực thi tường minh (`EXECUTE`) | **Tự động kích hoạt** khi có sự kiện (INSERT, UPDATE, DELETE) | Gọi bên trong biểu thức hoặc mệnh đề `SELECT` |
| **Giá trị trả về** | Không bắt buộc (hoặc trả qua tham số `OUT`) | **Không bao giờ trả về giá trị** | **Bắt buộc phải có lệnh `RETURN`** trả về 1 giá trị |
| **Lệnh TCL (COMMIT)** | Cho phép sử dụng COMMIT / ROLLBACK | **Tuyệt đối cấm dùng COMMIT / ROLLBACK** | Không dùng các lệnh thay đổi dữ liệu DML/TCL |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Số lượng lược đồ:** Hệ thống có thể có vô số 외부 스키마, nhưng **chỉ có duy nhất 1 개념 스키마 và 1 내부 스키마**.
- **Bẫy 2: Lệnh cấm trong Trigger:** Trong khối lệnh của 트리거 (Trigger), **tuyệt đối không được sử dụng các lệnh điều khiển giao dịch TCL (COMMIT, ROLLBACK)** vì nó gắn liền với giao dịch của câu lệnh kích hoạt.
- **Bẫy 3: Các mẫu truy vấn làm vô hiệu hóa Index (gây Full Table Scan):**
  - Dùng hàm biến đổi trên cột Index: `WHERE SUBSTR(id, 1, 3) = 'ABC'` $\rightarrow$ Không dùng được Index; phải sửa thành `WHERE id LIKE 'ABC%'`.
  - Phép toán số học trên cột: `WHERE salary * 12 > 50000000` $\rightarrow$ Mất Index; phải sửa thành `WHERE salary > 50000000 / 12`.
  - Dùng toán tử phủ định: `WHERE status != 'ACTIVE'` hoặc `WHERE status NOT IN (...)` $\rightarrow$ Dễ gây quét toàn bảng.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ kiến trúc 3 tầng lược đồ ANSI/SPARC
```
[ Lập trình viên A ]       [ Lập trình viên B ]       [ Người dùng cuối ]
  (외부 스키마 1)            (외부 스키마 2)            (외부 스키마 3)
         \                         |                         /
          \=== [ 외부-개념 사상: Độc lập dữ liệu Logic ] ===/
                                   |
                         [ 개념 스키마 (Conceptual) ]
                         (Toàn thể cấu trúc logic DB)
                                   |
          /=== [ 개념-내부 사상: Độc lập dữ liệu Vật lý ] ===\
         /                         |                         \
                         [ 내부 스키마 (Internal) ]
                         (Bố trí đĩa, Index, Block)
```

#### 2. Trình tối ưu hóa truy vấn: RBO vs CBO
- **RBO (규칙 기반 옵티마이저 — Rule-Based Optimizer):** Quyết định đường dẫn truy cập dựa trên thứ bậc quy tắc ưu tiên cố định được định sẵn (ví dụ: dùng khóa chính trước, rồi đến chỉ mục đơn, cuối cùng mới đến quét toàn bảng). Không quan tâm đến số lượng bản ghi thực tế.
- **CBO (비용 기반 옵티마이저 — Cost-Based Optimizer):** Phân tích thống kê dữ liệu thực tế (số dòng, số block đĩa, phân bố giá trị) để tính toán chi phí tài nguyên (CPU, I/O) và chọn phương án có tổng chi phí nhỏ nhất. Là chuẩn mực trong mọi RDBMS hiện đại.

---

### 복습 체크리스트
- [ ] Phân biệt rõ phạm vi của 3 tầng: 외부 스키마 (User View), 개념 스키마 (toàn bộ logic), 내부 스키마 (lưu trữ đĩa).
- [ ] Phân biệt 논리적 독립성 (ánh xạ ngoài-khái niệm) và 물리적 독립성 (ánh xạ khái niệm-trong).
- [ ] Phân biệt 3 đối tượng PL/SQL: Procedure (gọi lệnh), Trigger (tự động, cấm COMMIT), User Function (phải RETURN).
- [ ] Nhớ quy tắc cấm COMMIT/ROLLBACK trong Trigger.
- [ ] Phân biệt RBO (dựa trên thứ bậc quy tắc) và CBO (dựa trên chi phí thống kê).
- [ ] Liệt kê 3 dạng câu lệnh làm mất hiệu lực chỉ mục Index gây Full Table Scan.
