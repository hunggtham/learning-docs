# Môn 2 · Bài 07 — Cơ sở dữ liệu và tối ưu hóa truy vấn trong phát triển phần mềm

> **Mạch đọc:** [README](../README.md) là bản đồ chủ đề của **Môn 2 — 소프트웨어 개발 (Software Development)**. Khép lại toàn diện **Chương 1: Cấu trúc dữ liệu, Thuật toán & Tối ưu I/O (데이터 입출력 구현)**, bài học này đưa người học từ không gian bộ nhớ tạm thời (RAM) sang không gian lưu trữ bền vững (Cơ sở dữ liệu). Bài học tập trung vào các kiến thức cơ sở dữ liệu dưới góc nhìn của **Kỹ sư phát triển phần mềm**: kiến trúc 3 tầng lược đồ ANSI/SPARC, tính độc lập dữ liệu, lập trình SQL thủ tục (PL/SQL) và kỹ thuật tối ưu hóa hiệu năng câu lệnh truy vấn (SQL Tuning).

> **Phạm vi nguồn:** Hợp nhất và chuẩn hóa nội dung từ 7 bài học cũ: `68, 71, 81, 93, 94, 95, 96-bai-hoc.md` (tương ứng với các mục 9, 33, 088-2 & 089, 090-1, 091, 091-1, 092-1 trong tài liệu chuẩn gốc). Toàn bộ quy trình gỡ lỗi PL/SQL và nguyên tắc tối ưu Optimizer RBO vs CBO được đối chiếu với chuẩn khảo thí HRDK.

> **Mạch kiến thức:** Khi ứng dụng phần mềm giao tiếp với hệ quản trị CSDL (DBMS), bài toán hiệu năng và toàn vẹn dữ liệu phụ thuộc vào cách viết mã. Bài học này giải quyết ba vấn đề kỹ thuật: (1) Kiến trúc 3 tầng lược đồ (External, Conceptual, Internal) và hai mức độc lập dữ liệu bảo vệ chương trình ứng dụng như thế nào khi cấu trúc bảng thay đổi? (2) Ba đối tượng SQL thủ tục (Procedure, Trigger, Function) khác nhau ra sao về cách kích hoạt, giá trị trả về và các hạn chế giao dịch (TCL)? (3) Quy trình 3 bước tối ưu hóa truy vấn bằng APM và kế hoạch thực thi (Execution Plan) phát hiện và hóa giải các bẫy làm mất Index (gây Full Table Scan) như thế nào?

---

## 1. 스키마 3계층과 데이터 독립성 — Kiến trúc 3 tầng Lược đồ và Tính độc lập dữ liệu

Để giảm thiểu sự phụ thuộc giữa chương trình ứng dụng phần mềm và cấu trúc lưu trữ dữ liệu vật lý trên ổ đĩa, tiêu chuẩn ANSI/SPARC đã thiết lập **Kiến trúc 3 tầng lược đồ (Three-Schema Architecture)**:

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

### 1.1. Bảng phân định 3 tầng lược đồ chuẩn đề thi

| Tầng lược đồ | Tên tiếng Hàn & Anh | Đối tượng sử dụng | Phạm vi và nội dung thể hiện |
| :--- | :--- | :--- | :--- |
| **Tầng Ngoài** | **외부 스키마 (External Schema)** | Người dùng cuối, **Lập trình viên ứng dụng** | Còn gọi là **사용자 뷰 (User View)** hoặc **서브스키마 (Sub-schema)**; chỉ hiển thị phần dữ liệu liên quan đến nghiệp vụ riêng biệt của từng ứng dụng, che giấu dữ liệu của các phòng ban khác |
| **Tầng Quan niệm** | **개념 스키마 (Conceptual Schema)** | Quản trị viên CSDL (DBA), Kiến trúc sư hệ thống | Thể hiện cấu trúc **toàn bộ dữ liệu logic của tổ chức**; định nghĩa các thực thể (Entity), bảng (Table), mối quan hệ (Relationship) và các ràng buộc toàn vẹn |
| **Tầng Trong** | **내부 스키마 (Internal Schema)** | Kỹ sư hệ thống, Nhân DBMS | Cấu trúc **lưu trữ vật lý thực tế trên thiết bị phần cứng**; định nghĩa định dạng bản ghi, dung lượng block, chỉ mục (B-Tree/Hash), phương pháp đánh địa chỉ sector |

*Quy tắc số lượng:* Một hệ thống CSDL có thể có **nhiều Lược đồ ngoài** (mỗi nhóm ứng dụng có 1 view riêng), nhưng **chỉ có duy nhất 1 Lược đồ quan niệm** và **chỉ có duy nhất 1 Lược đồ trong**.

---

### 1.2. Hai cấp độ độc lập dữ liệu (데이터 독립성 — Data Independence)
Tính độc lập dữ liệu là khả năng thay đổi cấu trúc dữ liệu ở tầng dưới mà không làm ảnh hưởng hay bắt buộc phải sửa đổi các chương trình ứng dụng ở tầng trên:

1. **논리적 데이터 독립성 (Logical Data Independence — Tính độc lập logic):**
   - Đạt được thông qua lớp ánh xạ **외부 - 개념 사상 (External - Conceptual Mapping)**.
   - Khi cấu trúc logic của cơ sở dữ liệu thay đổi (ví dụ: thêm một cột mới, gộp hai bảng ở tầng Conceptual Schema), các chương trình ứng dụng và Lược đồ ngoài ở tầng trên **hoàn toàn không bị ảnh hưởng, không cần biên dịch hay viết lại mã**.
2. **물리적 데이터 독립성 (Physical Data Independence — Tính độc lập vật lý):**
   - Đạt được thông qua lớp ánh xạ **개념 - 내부 사상 (Conceptual - Internal Mapping)**.
   - Khi cấu trúc lưu trữ vật lý trên đĩa cứng thay đổi (ví dụ: nâng cấp ổ SSD, thay đổi dung lượng block, tái cấu trúc bảng chỉ mục B-Tree ở tầng Internal Schema), Lược đồ quan niệm và các câu truy vấn logic **hoàn toàn không bị xáo trộn**.

---

## 2. 절차형 SQL (Procedural SQL / PL/SQL) — Lập trình SQL thủ tục

Ngôn ngữ SQL tiêu chuẩn vốn là ngôn ngữ phi thủ tục (Non-procedural): người dùng chỉ khai báo muốn lấy dữ liệu gì (`SELECT ... WHERE ...`) mà không thể kiểm soát luồng thực thi tuần tự. 

**절차형 SQL (Procedural SQL)** mở rộng SQL bằng cách bổ sung các cấu trúc điều khiển rẽ nhánh (`IF-THEN-ELSE`) và vòng lặp (`LOOP`, `FOR`, `WHILE`) tương tự ngôn ngữ C hay Java, cho phép lập trình các nghiệp vụ phức tạp chạy trực tiếp ngay trong nhân DBMS.

### Bảng so sánh 3 đối tượng SQL thủ tục cốt lõi

| Tiêu chuẩn so sánh | 프로시저 (Stored Procedure) | 트리거 (Trigger) | 사용자 정의 함수 (User-Defined Function) |
| :--- | :--- | :--- | :--- |
| **Cách thức kích hoạt** | Được gọi **trực tiếp** bằng lệnh `EXECUTE` hoặc `CALL` | Kích hoạt **hoàn toàn tự động** khi sự kiện DML (`INSERT`, `UPDATE`, `DELETE`) xảy ra | Gọi nhúng trực tiếp trong các câu lệnh SQL (như `SELECT func(x) FROM tab`) |
| **Giá trị trả về** | Không có lệnh `RETURN` giá trị; trả về kết quả qua tham số `OUT` | **Hoàn toàn không trả về giá trị (반환값 없음)** | **Bắt buộc phải trả về duy nhất 1 giá trị** qua mệnh đề `RETURN` |
| **Mục đích sử dụng** | Xử lý các luồng nghiệp vụ phức tạp gồm nhiều bước giao dịch tập trung | Tự động ghi nhật ký (Audit Log), duy trì ràng buộc toàn vẹn phức tạp | Tính toán công thức thuế, định dạng chuỗi dữ liệu tái sử dụng |
| **Hạn chế giao dịch (TCL)** | Cho phép sử dụng các lệnh `COMMIT` và `ROLLBACK` | **Tuyệt đối KHÔNG ĐƯỢC CHỨA `COMMIT` hoặc `ROLLBACK`** | Không được phép thay đổi dữ liệu hoặc commit trong hàm gọi từ SELECT |

### ⚠️ Bẫy đề thi cực lớn về Trigger
Đề thi thường xuyên gài bẫy: *"Đối tượng nào sau đây không thể chứa các lệnh điều khiển giao dịch TCL (COMMIT, ROLLBACK)?"* $\rightarrow$ Đáp án chắc chắn là **트리거 (Trigger)**. Lý do kỹ thuật: Trigger chạy chung ngữ cảnh giao dịch với câu lệnh DML vừa kích hoạt nó; nếu Trigger tự ý commit hay rollback, nó sẽ phá hủy tính nguyên tử (Atomicity) của toàn bộ Transaction mẹ.

### Quy trình kiểm thử và gỡ lỗi (Debugging) mã PL/SQL
1. **Biên dịch (Compile):** Dùng lệnh `CREATE OR REPLACE` để kiểm tra lỗi cú pháp biên dịch của máy chủ.
2. **Comment mã DML nguy hiểm:** Khi chạy thử nghiệm kiểm tra logic, tạm thời chú thích (comment out) các dòng lệnh `INSERT/UPDATE/DELETE` để tránh làm sai lệch dữ liệu thực tế.
3. **In log theo dõi biến:** Sử dụng gói thư viện chuẩn:
   $$\mathbf{DBMS\_OUTPUT.PUT\_LINE(bi\acute{e}n);}$$
4. **Bật ngõ ra và thực thi:** Trên cửa sổ lệnh (SQL*Plus / Tool), gõ `SET SERVEROUTPUT ON;` trước khi gọi thủ tục để màn hình hiển thị toàn bộ giá trị log trung gian.

---

## 3. 쿼리 성능 최적화 (Query Performance Optimization) — Tối ưu hóa truy vấn

Trong hệ thống I/O dữ liệu, một câu truy vấn viết cẩu thả có thể kéo sập toàn bộ máy chủ cơ sở dữ liệu do chiếm dụng 100% CPU và tràn bộ nhớ đệm Buffer Pool.

### 3.1. Quy trình tối ưu hóa truy vấn 3 bước tiêu chuẩn
1. **1단계: 대상 선정 (Xác định mục tiêu):**
   - Sử dụng công cụ **APM (Application Performance Monitoring — ví dụ: Scouter, Jennifer, Pinpoint)** để giám sát ứng dụng theo thời gian thực.
   - Lọc ra danh sách các câu lệnh SQL có thời gian đáp ứng vượt ngưỡng (Slow Query) hoặc có tần suất thực thi cao đột biến (High I/O Query).
2. **2단계: 계획 검토 (Phân tích kế hoạch thực thi):**
   - Sử dụng lệnh `EXPLAIN PLAN` hoặc công cụ đồ họa của DBMS để phân tích **실행 계획 (Execution Plan)** do Bộ tối ưu hóa (Optimizer) thiết lập.
   - Kiểm tra xem câu truy vấn đang sử dụng phương thức quét nào: Quét theo dải chỉ mục (**Index Range Scan**) hay bị tụt xuống quét toàn bộ bảng (**풀 테이블 스캔 — Full Table Scan / FTS**).
3. **3단계: 재구성 및 튜닝 (Tái cấu trúc mã và tinh chỉnh Index):**
   - Sửa lại cú pháp mệnh đề `WHERE`, loại bỏ các biểu thức làm vô hiệu hóa Index, tái cấu trúc bảng chỉ mục hoặc bổ sung gợi ý điều khiển (**옵티마이저 힌트 — Optimizer Hint**).

---

### 3.2. Bộ tối ưu hóa: RBO vs CBO

Bộ tối ưu hóa (**옵티마이저 — Optimizer**) là trái tim của DBMS, chịu trách nhiệm phân tích câu lệnh SQL và lựa chọn con đường thực thi tốn ít tài nguyên nhất:

| Tiêu chuẩn | RBO (Rule-Based Optimizer — Dựa trên quy tắc) | CBO (Cost-Based Optimizer — Dựa trên chi phí) |
| :--- | :--- | :--- |
| **Cơ sở quyết định** | Áp dụng cứng nhắc theo thứ tự 15 quy tắc ưu tiên định sẵn | Tính toán **chi phí ước lượng nhỏ nhất (최소 비용)** dựa trên bảng thống kê dữ liệu thực tế |
| **Dữ liệu thống kê** | Không cần dữ liệu thống kê số lượng bản ghi | **Bắt buộc phải thu thập và định kỳ cập nhật thống kê (Analyze / Statistics)** |
| **Khả năng thích ứng** | Cứng nhắc, không phân biệt bảng có 10 dòng hay 10 triệu dòng | Rất thông minh và thích ứng linh hoạt theo kích thước dữ liệu thực tế |

---

### 3.3. Các lỗi bẫy làm mất Index gây Full Table Scan trong đề thi

Để Index phát huy tác dụng quét nhanh $O(\log n)$, cột được đánh Index phải giữ nguyên giá trị nguyên bản. Các lỗi sau đây sẽ khiến Optimizer buộc phải quét toàn bảng (Full Table Scan):

1. **Sử dụng hàm hoặc phép tính trên cột có Index:**
   - ❌ Sai: `WHERE SUBSTR(EMP_ID, 1, 2) = '10'` (Hàm `SUBSTR` làm mất tác dụng Index).
   - ✅ Đúng: `WHERE EMP_ID LIKE '10%'`.
   - ❌ Sai: `WHERE SALARY * 12 > 50000000` (Phép nhân làm mất Index).
   - ✅ Đúng: `WHERE SALARY > 50000000 / 12`.
2. **Sử dụng ký tự đại diện Wildcard ở đầu chuỗi:**
   - ❌ Sai: `WHERE USER_NAME LIKE '%KIM'` (Bắt buộc phải quét toàn bộ bảng vì không biết chữ cái đầu).
   - ✅ Đúng: `WHERE USER_NAME LIKE 'KIM%'` (Sử dụng được Index Range Scan).
3. **Lạm dụng `SELECT *`:**
   - Luôn chỉ định rõ ràng các cột cần lấy: `SELECT id, name FROM ...` nhằm giảm thiểu I/O đĩa và giải phóng băng thông truyền thông.
4. **Sử dụng Optimizer Hint:**
   - Trong trường hợp CBO tính toán sai do bảng thống kê bị lỗi thời, lập trình viên có thể chèn trực tiếp gợi ý điều khiển vào ngay sau lệnh SELECT:
     `SELECT /*+ INDEX(emp emp_idx_01) */ id, name FROM emp WHERE ...;`

---

## 4. Nối mạch kiến thức sang Chương 2: Thiết kế và Hiện thực Module

Đến đây, chúng ta đã hoàn thành toàn diện **Chương 1: Cấu trúc dữ liệu, Thuật toán & Tối ưu I/O (Bài 01 đến Bài 07)**. Toàn bộ nền tảng về tổ chức bộ nhớ tuyến tính/phi tuyến, độ phức tạp sắp xếp, tìm kiếm bảng băm và tối ưu hóa truy vấn CSDL đã được làm chủ vững chắc.

Tuy nhiên, phần mềm hiện đại không được viết dưới dạng một tệp mã nguồn khổng lồ nguyên khối. Phần mềm bắt buộc phải được chia nhỏ thành các đơn vị chức năng độc lập gọi là **Module**, và các module đó phải có cơ chế giao tiếp liên tiến trình (IPC) với nhau.

Chúng ta chính thức bước sang **Chương 2: Thiết kế & Hiện thực Module, Tích hợp hệ thống (통합 구현)** với **[Bài 08: Hiện thực đơn vị module, IPC và tái sử dụng phần mềm](08-hien-thuc-module-va-ipc.md)**.

---

## 5. 복습 체크리스트 (Checklist ôn tập)

- [ ] Phân biệt được 3 tầng lược đồ: 외부 (User View), 개념 (Toàn thể logic), 내부 (Lưu trữ vật lý).
- [ ] Nhớ hệ thống có nhiều 외부 스키마 nhưng chỉ có 1 개념 스키마 và 1 내부 스키마.
- [ ] Phân biệt 논리적 데이터 독립성 (sửa 개념 không sửa 외부) và 물리적 데이터 독립성 (sửa 내부 không sửa 개념).
- [ ] Phân biệt 3 loại mã SQL thủ tục: Procedure (gọi bằng EXEC/CALL), Trigger (tự động khi có sự kiện), Function (nhúng trong SELECT).
- [ ] Nhớ Trigger TUYỆT ĐỐI KHÔNG ĐƯỢC CHỨA lệnh COMMIT hoặc ROLLBACK.
- [ ] Nhớ User-Defined Function bắt buộc phải có mệnh đề RETURN trả về giá trị đơn lẻ.
- [ ] Nhớ lệnh in log gỡ lỗi trong PL/SQL là DBMS_OUTPUT.PUT_LINE.
- [ ] Nắm rõ 3 bước tối ưu hóa truy vấn: 대상 선정 (APM) $\rightarrow$ 계획 검토 (실행 계획) $\rightarrow$ 재구성 (SQL/Index tuning).
- [ ] Phân biệt RBO (dựa trên quy tắc cố định) và CBO (dựa trên chi phí ước tính từ thống kê).
- [ ] Nhận diện các lỗi gây Full Table Scan: bọc hàm quanh cột Index, viết wildcard '%' ở đầu LIKE.
