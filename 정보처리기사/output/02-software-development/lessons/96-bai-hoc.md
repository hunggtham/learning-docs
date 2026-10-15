# 091-1: 절차형 SQL (Procedural SQL)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm và vai trò của SQL thủ tục (절차형 SQL - Procedural SQL): mở rộng ngôn ngữ SQL tiêu chuẩn bằng cách bổ sung các cấu trúc rẽ nhánh (`IF`) và vòng lặp (`LOOP`, `FOR`, `WHILE`) như các ngôn ngữ lập trình C/Java.
- Phân biệt chính xác đặc tính vận hành và cú pháp của 3 đối tượng SQL thủ tục cốt lõi trong đề thi: Thủ tục lưu trữ (프로시저 - Stored Procedure), Bộ kích hoạt (트리거 - Trigger), và Hàm do người dùng định nghĩa (사용자 정의 함수 - User-Defined Function).
- Nắm vững quy trình kiểm thử và gỡ lỗi (Debugging) mã SQL thủ tục trực tiếp bên trong DBMS bằng công cụ `DBMS_OUTPUT`.

## 핵심 키워드 (Từ khóa)
- 절차형 SQL (Procedural SQL / PL/SQL)
- 프로시저 (Stored Procedure / EXEC, CALL / 매개변수 IN, OUT)
- 트리거 (Trigger / 이벤트 감지 / 자동 실행 / DML 감시)
- 사용자 정의 함수 (User-Defined Function / RETURN 단일값)
- 제어문 (Control Flow / IF-THEN-ELSE, LOOP)
- 디버깅 (Debugging / DBMS_OUTPUT.PUT_LINE)
- 트랜잭션 제한 (Trigger Transaction Limitation / COMMIT, ROLLBACK 불가)

## 선행·연결 개념 (Kiến thức liên kết)
- [95-bai-hoc.md](95-bai-hoc.md): Lược đồ cơ sở dữ liệu (Schema).
- [97-bai-hoc.md](97-bai-hoc.md): Môi trường phát triển tích hợp (IDE).
- [정보처리기사/output/03-database-construction/lessons/44-bai-hoc.md](../../03-database-construction/lessons/44-bai-hoc.md): Lập trình PL/SQL nâng cao và xử lý Transaction.

## 읽는 방법 (Cách đọc)
- Phân biệt 3 loại mã SQL thủ tục theo cách kích hoạt và kết quả trả về:
  - **프로시저 (Procedure):** Được người dùng hoặc ứng dụng chủ động gọi bằng lệnh `EXEC` hoặc `CALL`. Có thể nhận tham số đầu vào (`IN`) và trả kết quả ra qua tham số (`OUT`), nhưng không bắt buộc trả về một giá trị duy nhất.
  - **트리거 (Trigger):** Hoạt động hoàn toàn tự động, **không thể gọi thủ công bằng lệnh**. Tự động kích hoạt khi có sự kiện bảng dữ liệu (`INSERT`, `UPDATE`, `DELETE`) trước hoặc sau khi xảy ra. Tuyệt đối **không được chứa lệnh `COMMIT` hoặc `ROLLBACK`** vì chạy chung Transaction với câu lệnh gốc.
  - **사용자 정의 함수 (User-Defined Function):** Tương tự Procedure nhưng **bắt buộc phải có mệnh đề `RETURN`** để trả về một giá trị duy nhất; có thể nhúng trực tiếp vào biểu thức câu lệnh `SELECT`.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh 3 đối tượng SQL thủ tục kinh điển:**

| Tiêu chuẩn so sánh | 프로시저 (Procedure) | 트리거 (Trigger) | 사용자 정의 함수 (Function) |
| :--- | :--- | :--- | :--- |
| **Cách thức kích hoạt** | Gọi thực thi **trực tiếp** bằng lệnh `EXECUTE` hoặc `CALL` | Kích hoạt **tự động** khi sự kiện DML (`INSERT`, `UPDATE`, `DELETE`) xảy ra | Gọi nhúng trực tiếp trong các câu lệnh SQL (như `SELECT func(x) FROM tab`) |
| **Giá trị trả về** | Không có lệnh `RETURN` giá trị; trả về kết quả qua tham số `OUT` | **Hoàn toàn không trả về giá trị (반환값 없음)** | **Bắt buộc phải trả về duy nhất 1 giá trị** qua lệnh `RETURN` |
| **Mục đích sử dụng** | Xử lý hàng loạt logic nghiệp vụ phức tạp tập trung trên máy chủ DB | Tự động ghi nhật ký (Audit Log), duy trì ràng buộc toàn vẹn phức tạp | Tính toán công thức, định dạng chuỗi dữ liệu lặp lại nhiều lần |
| **Hạn chế giao dịch (TCL)** | Cho phép sử dụng các lệnh điều khiển giao dịch `COMMIT`, `ROLLBACK` | **Tuyệt đối KHÔNG được chứa `COMMIT` hoặc `ROLLBACK`** (Bẫy đề thi) | Không cho phép thay đổi dữ liệu hoặc commit trong hàm gọi từ SELECT |

- **Quy trình kiểm thử và gỡ lỗi SQL thủ tục (Testing & Debugging):**
  1. **컴파일 (Biên dịch):** Chạy lệnh `CREATE OR REPLACE` để kiểm tra lỗi cú pháp biên dịch.
  2. **DML 주석 처리 (Comment DML):** Khi test thử nghiệm, tạm thời comment các dòng lệnh `INSERT/UPDATE/DELETE` nguy hiểm để tránh làm hỏng dữ liệu thật.
  3. **디버깅 출력 (In log gỡ lỗi):** Chèn lệnh `DBMS_OUTPUT.PUT_LINE(biến);` để theo dõi giá trị trung gian của các biến logic.
  4. **실행 및 검증 (Thực thi và đối soát):** Bật cờ `SET SERVEROUTPUT ON`, chạy thủ tục và so sánh kết quả in ra với kết quả mong đợi.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ưu điểm về hiệu năng của Procedural SQL:**
  - Do toàn bộ khối lệnh logic nằm tập trung và chạy trực tiếp ngay trong nhân DBMS, hệ thống không phải gửi qua lại hàng trăm câu lệnh SQL rời rạc qua mạng mạng LAN/WAN.
  - Điều này giúp giảm thiểu tối đa băng thông đường truyền (Network Traffic) và nâng cao hiệu năng xử lý các giao dịch quy mô lớn.

### 복습 체크리스트
- [ ] Phân biệt rõ cách chạy: Procedure (gọi bằng EXEC/CALL), Trigger (tự động khi có sự kiện), Function (nhúng trong SELECT).
- [ ] Nhớ Trigger KHÔNG BAO GIỜ được dùng COMMIT hay ROLLBACK.
- [ ] Nhớ Function bắt buộc phải có RETURN trả về giá trị.
- [ ] Nhớ công cụ in log gỡ lỗi trong PL/SQL là DBMS_OUTPUT.PUT_LINE.
