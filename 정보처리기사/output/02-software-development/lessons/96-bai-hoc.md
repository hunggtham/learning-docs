# 091-1: 절차형 SQL (Procedural SQL)

## 091-1: 절차형 SQL (Procedural SQL)

C, JAVA처럼 분기/반복 (If/For)이 가능한 SQL (SQL có thêm logic lập trình - PL/SQL). Bọc trong khối `BEGIN ~ END`.

| 종류 (Loại) | 특징 (Đặc điểm) | ví dụ (Ví dụ sử dụng) |
|---|---|---|
| **프로시저 (Procedure)** | Gọi thủ công (`CALL`). Thực thi một chuỗi nghiệp vụ (Insert/Update nhiều bảng). KHÔNG có `RETURN`. | Chuyển tiền (Trừ A, Cộng B). |
| **트리거 (Trigger)** | Tự động chạy khi có sự kiện (Insert/Update/Delete). KHÔNG thể gọi thủ công. | Tự động ghi log khi có người xóa dữ liệu, tự trừ số lượng kho khi có đơn hàng. |
| **사용자 정의 함수 (User Defined Function)** | Dùng trong câu `SELECT`. BẮT BUỘC có `RETURN` 1 giá trị. | Hàm tính thuế VAT 10% từ giá gốc. |

- **Vietnamese Explanation:** SQL bình thường rất phèn, chỉ biết lấy dữ liệu ra. Procedural SQL thông minh hơn. Procedure như một cuốn kịch bản bạn bắt nó diễn. Trigger như cái bẫy chuột, có chuột (sự kiện) là tự sập. Function giống hệt hàm trong Toán học, đưa X trả về Y.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Procedure = Gọi mới chạy. Trigger = Tự động (Event). Function = Trả về giá trị (Return).

### 절차형 SQL의 테스트와 디버깅 (Testing & Debugging Procedural SQL)
Phần “절차형 SQL의 테스트와 디버깅 (Testing & Debugging Procedural SQL)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 절차형 SQL은 DBMS 내부에서 직접 실행되므로, 애플리케이션과 DB 사이의 데이터 전송량을 줄일 수 있어 효율적임. (Chạy trực tiếp trong DBMS nên giảm nghẽn mạng).
- **Quy trình Test & Debug:** `CREATE` (Biên dịch) -> Sửa lỗi cú pháp -> Comment các lệnh `INSERT/UPDATE/DELETE` (Tránh làm hỏng DB thật) -> Dùng `DBMS_OUTPUT` in giá trị ra màn hình để kiểm tra -> `EXEC / CALL` -> Xác nhận kết quả.

---
