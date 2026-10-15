# 071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cơ chế khai thác và biện pháp khắc phục các lỗ hổng bảo mật phổ biến trong mã nguồn ứng dụng và hệ thống theo tiêu chuẩn an toàn thông tin.
- Phân biệt các lỗ hổng quản lý bộ nhớ nguy hiểm ở tầng thấp: Tràn bộ đệm (버퍼 오버플로 - Buffer Overflow), Con trỏ lơ lửng (허상 포인터 - Dangling Pointer), và Lỗi chuỗi định dạng (포맷 스트링 버그 - Format String Bug).
- Thấu hiểu cơ chế tấn công ở tầng ứng dụng web: Tấn công tiêm lệnh SQL (SQL Injection), Tấn công duyệt thư mục (디렉토리 접근 공격 - Directory Traversal), và Tấn công bật nảy FTP (FTP 바운스 공격).

## 핵심 키워드 (Từ khóa)
- 보안 취약점 (Security Vulnerability)
- 버퍼 오버플로 (Buffer Overflow - Return Address 변조)
- 허상 포인터 (Dangling Pointer / Use-After-Free)
- SQL 삽입 (SQL Injection - PreparedStatement 대응)
- 디렉토리 접근 공격 (Directory / Path Traversal - `../` 패턴)
- 포맷 스트링 버그 (Format String Bug - `%n`, `%x` 악용)
- FTP 바운스 공격 (FTP Bounce Attack - PORT 명령 악용)

## 선행·연결 개념 (Kiến thức liên kết)
- [69-bai-hoc.md](69-bai-hoc.md): Framework phát triển máy chủ và các cơ chế bảo mật tích hợp.
- [71-bai-hoc.md](71-bai-hoc.md): Hàm do người dùng định nghĩa và quản lý biến cục bộ.
- [14-bai-hoc.md](14-bai-hoc.md): Các đặc tả định dạng xuất nhập dữ liệu (`printf`, `scanf`) trong C.

## 읽는 방법 (Cách đọc)
- Trong bài thi kỹ sư CNTT Hàn Quốc:
  - Khi nhắc đến từ khóa "Dùng chuỗi `../` để đọc tệp tin hệ thống như `/etc/passwd`" $\rightarrow$ Chọn ngay **디렉토리 접근 공격 (Directory Traversal)**.
  - Khi nhắc đến việc "Nhập chuỗi vượt quá kích thước mảng làm ghi đè vùng nhớ ngăn xếp (Stack) và địa chỉ trả về (Return Address)" $\rightarrow$ Chọn ngay **버퍼 오버플로 (Buffer Overflow)**.
  - Khắc phục SQL Injection: Sử dụng câu truy vấn tham số hóa tĩnh **PreparedStatement** (바인딩 변수).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp các lỗ hổng bảo mật kinh điển trong đề thi:**

| Lỗ hổng bảo mật | Bản chất kỹ thuật & Phương thức khai thác | Biện pháp phòng chống chuẩn |
| :--- | :--- | :--- |
| **버퍼 오버플로** (Buffer Overflow) | Nhập dữ liệu có độ dài vượt quá dung lượng bộ đệm được cấp phát trên Stack/Heap, làm tràn và **ghi đè lên địa chỉ trả về (Return Address)** của hàm để chuyển hướng luồng thực thi sang mã độc. | Dùng các hàm an toàn có kiểm soát độ dài (`strncpy`, `snprintf`), bật cờ biên dịch Stack Canary (ASLR, DEP/NX bit). |
| **허상 포인터** (Dangling Pointer) | Con trỏ vẫn tiếp tục trỏ đến một vùng địa chỉ bộ nhớ **đã bị giải phóng (`free`) hoặc đối tượng đã bị hủy**, dẫn đến nguy cơ ghi đè dữ liệu bất hợp pháp (Use-After-Free). | Gán con trỏ về `NULL` ngay lập tức sau khi gọi lệnh giải phóng vùng nhớ (`free(p); p = NULL;`). |
| **SQL 삽입** (SQL Injection) | Kẻ tấn công chèn các ký tự điều khiển cú pháp SQL (như `' OR '1'='1`) vào form nhập liệu nhằm bẻ cong logic câu truy vấn, truy xuất trái phép hoặc xóa sạch cơ sở dữ liệu. | **Sử dụng PreparedStatement (Prepared Parameter Binding)**; tuyệt đối không cộng chuỗi lệnh SQL động với dữ liệu người dùng. |
| **디렉토리 접근** (Directory Traversal) | Sử dụng các ký tự chuyển hướng thư mục như `../` hoặc `%2e%2e%2f` để thoát khỏi thư mục Web Root và đọc trộm các tệp cấu hình hệ thống nhạy cảm (như `/etc/passwd`). | Kiểm tra tính hợp lệ của đường dẫn (Path Normalization / Whitelist), loại bỏ triệt để các ký tự `..`, `/`, `\`. |
| **포맷 스트링 버그** (Format String Bug) | Truyền trực tiếp dữ liệu do người dùng nhập vào tham số đầu tiên của hàm xuất định dạng (ví dụ viết sai cú pháp `printf(user_str)` thay vì `printf("%s", user_str)`). Kẻ tấn công dùng mã `%x` để đọc RAM hoặc `%n` để ghi đè bộ nhớ. | Luôn luôn chỉ định chuỗi định dạng tĩnh rõ ràng ở tham số đầu tiên của hàm (`printf("%s", input)`). |
| **FTP 바운스 공격** (FTP Bounce Attack) | Lợi dụng cơ chế lệnh `PORT` trong giao thức truyền tệp FTP để yêu cầu máy chủ FTP gửi dữ liệu đến một máy thứ ba ngẫu nhiên, giúp kẻ tấn công quét cổng ẩn danh hoặc vượt tường lửa. | Cấu hình máy chủ FTP từ chối lệnh PORT gửi tới cổng hoặc địa chỉ IP khác với địa chỉ kết nối của máy khách (bật chế độ Passive FTP). |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tấn công tiêm mã độc (Code / Command Injection):**
  - Xảy ra khi ứng dụng chuyển trực tiếp chuỗi nhập liệu của người dùng vào các hàm gọi lệnh shell của hệ điều hành (như `system()`, `exec()`, `Runtime.getRuntime().exec()`). Kẻ tấn công có thể ghép dấu chấm phẩy `;` hoặc dấu gạch đứng `|` để thực thi các lệnh nguy hiểm (ví dụ: `input_filename; rm -rf /`).

### 복습 체크리스트
- [ ] Nhận diện Buffer Overflow qua cơ chế ghi đè địa chỉ trả về (Return Address) do không kiểm tra độ dài đầu vào.
- [ ] Hiểu con trỏ lơ lửng (Dangling Pointer) phát sinh khi giải phóng bộ nhớ nhưng không gán con trỏ về `NULL`.
- [ ] Ghi nhớ giải pháp chống SQL Injection triệt để nhất là dùng **PreparedStatement**.
- [ ] Nhận diện Directory Traversal qua chuỗi ký tự điều hướng thư mục `../`.
- [ ] Tránh lỗi Format String bằng cách luôn dùng cú pháp an toàn: `printf("%s", str)`.
