# 092-1: 쿼리 성능 최적화 (Query Performance Optimization)

## 학습 목표 (Mục tiêu)
- Hiểu rõ khái niệm và mục đích của tối ưu hóa truy vấn dữ liệu (쿼리 성능 최적화): nâng cao tốc độ phản hồi và thông lượng của ứng dụng I/O dữ liệu bằng cách tinh chỉnh mã SQL và cấu trúc lưu trữ.
- Nắm vững quy trình tối ưu hóa 3 bước tiêu chuẩn: Xác định đối tượng chậm bằng công cụ APM $\rightarrow$ Phân tích kế hoạch thực thi (실행 계획) do Bộ tối ưu hóa (Optimizer) thiết lập $\rightarrow$ Tái cấu trúc mã SQL và tinh chỉnh chỉ mục (인덱스 튜닝).
- Phân biệt hai cơ chế vận hành của Optimizer trong RDBMS: Tối ưu dựa trên quy tắc (RBO - Rule-Based Optimizer) và Tối ưu dựa trên chi phí (CBO - Cost-Based Optimizer).

## 핵심 키워드 (Từ khóa)
- 쿼리 성능 최적화 (Query Performance Optimization / SQL Tuning)
- APM (Application Performance Monitoring / Scouter, Jennifer)
- 옵티마이저 (Optimizer / RBO vs CBO)
- 실행 계획 (Execution Plan / EXPLAIN PLAN)
- 인덱스 재구성 (Index Restructuring / B-Tree Index)
- 풀 테이블 스캔 (Full Table Scan / FTS)

## 선행·연결 개념 (Kiến thức liên kết)
- [67-bai-hoc.md](67-bai-hoc.md): Phân tích thuật toán và kiểm thử phần mềm.
- [69-bai-hoc.md](69-bai-hoc.md): Bảo mật giao diện tầng mạng.
- [정보처리기사/output/03-database-construction/lessons/34-bai-hoc.md](../../03-database-construction/lessons/34-bai-hoc.md): Cấu trúc và nguyên lý tạo Index trong CSDL.

## 읽는 방법 (Cách đọc)
- Tập trung vào chu trình 3 bước chuẩn thi:
  1. **대상 선정 (Xác định mục tiêu):** Dùng APM đo đạc để tìm ra các câu lệnh SQL tốn nhiều tài nguyên hoặc chạy vượt ngưỡng thời gian quy định (Slow Query).
  2. **계획 검토 (Kiểm tra kế hoạch):** Đọc đồ thị hoặc cây kế hoạch thực thi (`EXPLAIN`) để xem hệ thống đang dùng Index Scan hay bị Full Table Scan.
  3. **재구성 (Tái cấu trúc / Tinh chỉnh):** Viết lại mệnh đề WHERE, tránh hàm xử lý trên cột đánh chỉ mục, hoặc tạo thêm Composite Index thích hợp.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Quy trình tối ưu hóa truy vấn SQL (최적화 3단계 절차):**

| Giai đoạn | Hành động cụ thể | Công cụ / Thành phần cốt lõi |
| :--- | :--- | :--- |
| **1. 대상 선정 (Chọn đối tượng)** | Giám sát toàn diện hệ thống, phát hiện và lập danh sách các câu lệnh truy vấn có thời gian đáp ứng quá chậm (Slow Query) | **APM (Application Performance Monitoring):** Jennifer, Scouter, Pinpoint |
| **2. 계획 검토 (Phân tích kế hoạch)** | Phân tích đường đi xử lý dữ liệu, kiểm tra thứ tự duyệt bảng, phương thức quét (Full Scan vs Index Range Scan), chi phí ước tính | **옵티마이저 (Optimizer)** & **실행 계획 (Execution Plan - EXPLAIN)** |
| **3. 재구성 및 튜닝 (Tái cấu trúc & Tuning)** | Sửa cú pháp SQL (tránh wildcard `%` ở đầu, tránh hàm bọc cột khóa), tái cấu trúc chỉ mục, cập nhật thống kê (Statistics) | Tái cấu trúc Index, Hint điều khiển Optimizer, Partitioning |

- **So sánh hai trường phái Optimizer (RBO vs CBO):**

| Tiêu chí | RBO (Rule-Based Optimizer - Tối ưu dựa trên quy tắc) | CBO (Cost-Based Optimizer - Tối ưu dựa trên chi phí) |
| :--- | :--- | :--- |
| **Cơ sở quyết định** | Áp dụng cứng nhắc theo thứ hạng quy tắc cố định (15 bậc ưu tiên định sẵn) | Tính toán **chi phí ước lượng nhỏ nhất (최소 비용)** dựa trên bảng thống kê dữ liệu thực tế |
| **Dữ liệu thống kê** | Không cần thông tin thống kê số lượng bản ghi hay phân bố dữ liệu | Bắt buộc phải thu thập và định kỳ cập nhật thông tin thống kê (Analyze / DBMS_STATS) |
| **Độ linh hoạt** | Kém thích ứng khi kích thước dữ liệu biến động lớn | Rất thông minh và thích ứng linh hoạt theo kích thước thực tế của từng bảng |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Các nguyên tắc vàng khi tinh chỉnh SQL (SQL Tuning Best Practices):**
  - **Không áp dụng hàm toán học hoặc chuỗi lên cột có Index:** Ví dụ viết `WHERE SUBSTR(EMP_NO, 1, 2) = '10'` sẽ làm mất tác dụng của Index trên cột `EMP_NO`, khiến hệ thống chuyển sang quét toàn bảng (Full Table Scan). Cần sửa thành `WHERE EMP_NO LIKE '10%'`.
  - **Tránh dùng `SELECT *`:** Chỉ truy vấn đúng các cột cần thiết nhằm giảm tải I/O bộ nhớ và đường truyền mạng.
  - **Sử dụng Index Hint:** Trong trường hợp CBO tính toán sai do thống kê lỗi thời, lập trình viên có thể chèn gợi ý (Hint) như `/*+ INDEX(table index_name) */` để ép Optimizer đi theo con đường mong muốn.

### 복습 체크리스트
- [ ] Nhớ 3 bước tối ưu hóa truy vấn: 대상 선정 (APM) $\rightarrow$ 계획 검토 (실행 계획) $\rightarrow$ 재구성 (SQL/인덱스 튜닝).
- [ ] Phân biệt rõ sự khác nhau giữa RBO (quy tắc cố định) và CBO (chi phí ước tính từ thống kê).
- [ ] Giải thích được tại sao việc viết hàm bọc cột khóa trong mệnh đề WHERE lại gây ra hiện tượng Full Table Scan.
