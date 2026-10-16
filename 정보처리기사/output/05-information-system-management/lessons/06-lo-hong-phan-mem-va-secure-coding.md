# 소프트웨어 취약점 방어 및 시큐어 코딩 (Phòng thủ lỗ hổng phần mềm & Lập trình an toàn Secure Coding)

## 학습 목표 (Mục tiêu)
- Nắm vững bản chất cơ chế phát sinh, hậu quả an ninh và các biện pháp phòng vệ hệ thống đối với lỗ hổng tràn bộ đệm bộ nhớ (**메모리 버퍼 오버플로 - Buffer Overflow**): Stack Guard/Canary, ASLR, DEP/NX.
- Thấu hiểu cơ chế tấn công tiêm lệnh hệ điều hành (**운영체제 명령어 삽입 - OS Command Injection**), nhận diện các ký tự phân tách lệnh nguy hiểm và phương pháp lập trình an toàn thay thế.
- Phân biệt sâu sắc giữa tấn công **XSS** và **CSRF (사이트 간 요청 위조)**, làm chủ các kỹ thuật phòng thủ CSRF: Token xác thực, SameSite Cookie và Xác thực lại.
- Hiểu rõ cơ chế gây sập hệ thống (Crash/DoS) của lỗi giải tham chiếu con trỏ rỗng (**널 포인터 역참조 - Null Pointer Dereference**) và rò rỉ tài nguyên (**부적절한 자원 해제 / Use After Free**).
- Thuộc lòng danh sách các API có lỗ hổng cố hữu và các hàm thay thế an toàn chuẩn mực trong C/C++ và Java (`gets` $\rightarrow$ `fgets`, `strcpy` $\rightarrow$ `strncpy`, `sprintf` $\rightarrow$ `snprintf`).

## 핵심 키워드 (Từ khóa song ngữ)
- 버퍼 오버플로 (Buffer Overflow — Tràn bộ đệm ghi đè Return Address trên Stack)
- 스택 가드 (Stack Guard / Canary — Giá trị ngẫu nhiên bảo vệ Return Address)
- ASLR (Address Space Layout Randomization — Xáo trộn không gian địa chỉ bộ nhớ)
- DEP / NX (Data Execution Prevention / No-Execute — Ngăn chặn thực thi mã trên Stack/Heap)
- 운영체제 명령어 삽입 (OS Command Injection — Tiêm lệnh Shell qua ký tự phân tách `;`, `|`, `&&`)
- CSRF (Cross-Site Request Forgery / 사이트 간 요청 위조 — Lợi dụng Session hợp lệ của nạn nhân)
- CSRF 토큰 (Anti-CSRF Token — Chuỗi ngẫu nhiên xác thực Form theo phiên làm việc)
- 널 포인터 역참조 (Null Pointer Dereference — Truy xuất địa chỉ rỗng gây Segmentation Fault/DoS)
- 자원 누수 (Resource Leak / Improper Release — Rò rỉ bộ nhớ và tệp mô tả File Descriptor)
- 취약한 API (Vulnerable API — `gets`, `strcpy`, `sprintf` vs `fgets`, `strncpy`, `snprintf`)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Từ khung quy trình bảo mật Secure SDLC đã học ở [05-khung-bao-mat-phan-mem-va-phap-luat.md](05-khung-bao-mat-phan-mem-va-phap-luat.md), các nguy cơ an ninh phải được loại trừ trực tiếp ở cấp độ mã nguồn bằng kỹ thuật lập trình phòng thủ (Defensive Coding).
- **Đang giải quyết gì (Current Problem):** Bài học này đi sâu vào cơ chế nhị phân và kiến trúc bộ nhớ để mổ xẻ các lỗ hổng nguy hiểm nhất (Buffer Overflow, Command Injection, CSRF, Null Pointer, API yếu) và cung cấp các giải pháp vá lỗi triệt để cả ở tầng mã nguồn lẫn tầng hệ điều hành.
- **Dùng đi đâu (Forward Handoff):** Để bảo vệ dữ liệu khỏi bị trích xuất hoặc can thiệp khi các lỗ hổng bị dò quét, hệ thống phải mã hóa dữ liệu nhạy cảm bằng các thuật toán tại [07-thuat-toan-ma-hoa-va-mat-ma-hoc.md](07-thuat-toan-ma-hoa-va-mat-ma-hoc.md) và thiết lập hàng rào kiểm soát truy cập tại [08-xac-thuc-va-kiem-soat-truy-cap.md](08-xac-thuc-va-kiem-soat-truy-cap.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **Tràn bộ đệm (Buffer Overflow):**
  - Cơ chế: Ghi dữ liệu vượt quá kích thước mảng đệm $\rightarrow$ Ghi đè lên **복귀 주소 (Return Address / EIP)** để chuyển hướng CPU sang mã độc.
  - Các kỹ thuật phòng vệ tầng OS/Compiler:
    - **스택 가드 (Canary):** Đặt giá trị kiểm tra trước Return Address.
    - **ASLR:** Xáo trộn địa chỉ nạp Stack, Heap, Libc ngẫu nhiên mỗi lần chạy.
    - **DEP/NX:** Cấm CPU thực thi lệnh trên vùng nhớ Stack/Heap.
- **Tiêm lệnh hệ điều hành (OS Command Injection):**
  - Dấu hiệu nhận diện: Ứng dụng nối chuỗi vào hàm gọi shell (`system()`, `exec()`), kẻ tấn công chèn các ký tự phân tách: **`;` (chấm phẩy)**, **`|` (pipe)**, **`&&` (AND)**, **`||` (OR)**.
  - Giải pháp đúng nhất: **Tuyệt đối không gọi Shell**, truyền mảng đối số tách rời (`ProcessBuilder`).
- **Phân biệt XSS vs CSRF (Bẫy đề thi kinh điển):**
  - **XSS:** Khai thác **sự tin tưởng của người dùng đối với trang web** (chèn mã JavaScript độc hại vào trang web để đánh cắp Cookie trên máy nạn nhân).
  - **CSRF:** Khai thác **sự tin tưởng của máy chủ đối với trình duyệt của người dùng** (lợi dụng việc máy chủ tin tưởng Session Cookie hợp lệ để lừa người dùng gửi lệnh trái phép).
  - Phòng vệ CSRF: Dùng **CSRF Token** ngẫu nhiên trên từng Form, bật cờ **SameSite Cookie** (`Strict` / `Lax`), hoặc yêu cầu **nhập lại mật khẩu (Re-authentication)**.
- **API dễ bị tổn thương (Vulnerable APIs):**
  - Nhìn thấy `gets()` $\rightarrow$ Thay ngay bằng `fgets()`.
  - Nhìn thấy `strcpy()`, `strcat()` $\rightarrow$ Thay ngay bằng `strncpy()`, `strncat()`.
  - Nhìn thấy `sprintf()` $\rightarrow$ Thay ngay bằng `snprintf()`.
  - Nhìn thấy bộ sinh số ngẫu nhiên `rand()` $\rightarrow$ Thay bằng `SecureRandom`.

---

## 소프트웨어 취약점 방어 및 시큐어 코딩

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Lỗ hổng tràn bộ đệm bộ nhớ (Memory Buffer Overflow)
- **개념 (Khái niệm):** Xảy ra trong các ngôn ngữ lập trình bậc thấp (C/C++) khi chương trình sao chép dữ liệu vượt quá dung lượng vùng nhớ đệm (Buffer) được cấp phát trên Stack hoặc Heap, dẫn đến việc ghi đè lên các ô nhớ liền kề.
- **Hậu quả an ninh:** Kẻ tấn công tính toán chính xác số byte cần thiết để ghi đè lên **Địa chỉ quay về (Return Address / RET)** trong Stack Frame của hàm, ép CPU nhảy đến đoạn mã độc (Shellcode) do kẻ tấn công cài cắm để chiếm toàn quyền điều khiển hệ thống.
- **Các cơ chế phòng vệ hệ thống (Compiler & OS Protection):**

| Cơ chế bảo vệ | Tên tiếng Hàn & Anh | Nguyên lý hoạt động phòng vệ |
| :--- | :--- | :--- |
| **Stack Guard / Canary** | **스택 가드 / 카나리** | Trình biên dịch tự động chèn một giá trị ngẫu nhiên (Canary) nằm ngay giữa biến cục bộ và Return Address. Trước khi hàm thoát ra, CPU kiểm tra lại Canary; nếu giá trị bị thay đổi (bị tràn đè lên), chương trình sẽ lập tức bị hủy bỏ (Abort) để ngăn chặn chuyển hướng luồng thực thi. |
| **ASLR** | **ASLR (주소 공간 배치 난수화)** | Hệ điều hành tự động xáo trộn ngẫu nhiên vị trí không gian địa chỉ của Stack, Heap và các thư viện liên kết động (libc) mỗi khi chương trình khởi chạy, khiến kẻ tấn công không thể xác định địa chỉ tĩnh để trỏ Return Address về. |
| **DEP / NX bit** | **DEP (데이터 실행 방지) / NX** | Đánh dấu vùng nhớ ngăn xếp (Stack) và đống (Heap) là vùng nhớ không thể thực thi mã lệnh (No-Execute). Nếu CPU cố tình nhảy vào thực thi lệnh tại vùng nhớ đệm, phần cứng sẽ kích hoạt ngoại lệ ngắt ngay lập tức. |

#### 2. Lỗ hổng tiêm lệnh hệ điều hành (OS Command Injection)
- **개념 (Khái niệm):** Xảy ra khi ứng dụng web nhận dữ liệu đầu vào từ người dùng rồi nối trực tiếp vào chuỗi lệnh để gọi thực thi thông qua shell hệ điều hành (`system()`, `popen()`, `exec()`).
- **Kịch bản khai thác:** Kẻ tấn công lợi dụng các ký tự phân tách lệnh của shell để chèn thêm lệnh độc hại:
  ```bash
  # Đầu vào hợp lệ của ứng dụng: ping 192.168.1.1
  # Đầu vào bị kẻ tấn công tiêm mã: 192.168.1.1; cat /etc/passwd
  # Hệ điều hành sẽ thực thi cả 2 lệnh tuần tự: ping xong sẽ in tệp mật khẩu hệ thống!
  ```
- **Biện pháp lập trình an toàn:**
  - `운영체제 명령어 실행 함수 사용을 원칙적으로 금지한다.` — Hạn chế tối đa việc gọi lệnh shell hệ thống; ưu tiên dùng các hàm thư viện API tích hợp sẵn của ngôn ngữ.
  - Sử dụng mảng đối số tách rời thay vì ghép chuỗi (ví dụ: `ProcessBuilder` trong Java hoặc `subprocess.run(["ping", "-c", "4", ip])` trong Python).
  - Áp dụng danh sách trắng (Allowlist) để lọc nghiêm ngặt ký tự đầu vào, chỉ cho phép chữ cái và chữ số.

#### 3. Giả mạo yêu cầu liên trang (CSRF - Cross-Site Request Forgery)
- **개념 (Khái niệm):** Cuộc tấn công lừa trình duyệt của nạn nhân (người dùng đã được xác thực hợp lệ trên trang web mục tiêu) tự động gửi các yêu cầu HTTP trái phép (như chuyển khoản ngân hàng, đổi email, đổi mật khẩu) tới máy chủ mà người dùng không hề hay biết.
- **Đối chiếu sự khác nhau sống còn giữa XSS và CSRF:**

| Tiêu chí | Tấn công XSS (Cross-Site Scripting) | Tấn công CSRF (Cross-Site Request Forgery) |
| :--- | :--- | :--- |
| **Bản chất khai thác** | Khai thác **sự tin tưởng của người dùng đối với trang web**. | Khai thác **sự tin tưởng của máy chủ đối với trình duyệt của người dùng**. |
| **Vị trí thực thi mã** | Chèn và thực thi mã script độc hại (JavaScript) ngay trong trình duyệt của nạn nhân. | Không thực thi mã script trên trang đích; chỉ mượn phiên làm việc hợp lệ (Cookie/Session) để gửi Request. |
| **Mục tiêu tấn công** | Đánh cắp Cookie phiên làm việc, Token xác thực, ghi lại phím bấm (Keylogger). | Ép người dùng thực hiện một hành động ngoài ý muốn (Chuyển tiền, Xóa tài khoản). |

- **Các biện pháp phòng thủ CSRF chuẩn công nghiệp:**
  1. **Anti-CSRF Token (CSRF 토큰 검증):** Mỗi khi hiển thị Form, máy chủ sinh ra một chuỗi mã ngẫu nhiên bí mật gắn kèm vào Form ẩn. Khi người dùng bấm gửi Form, máy chủ sẽ đối chiếu Token nhận được với Token trong phiên làm việc. Kẻ tấn công trên trang web khác không thể đọc được Token này do bị chặn bởi chính sách cùng nguồn gốc (Same-Origin Policy).
  2. **Thuộc tính SameSite của Cookie:** Đặt cờ `SameSite=Strict` hoặc `SameSite=Lax` trên Cookie xác thực để hướng dẫn trình duyệt không tự động gửi kèm Cookie trong các yêu cầu liên trang (Cross-site Requests).
  3. **Tái xác thực (Re-authentication):** Đối với các tác vụ nhạy cảm (thanh toán giao dịch, thay đổi thông tin cá nhân), bắt buộc người dùng phải nhập lại mật khẩu hoặc mã OTP xác nhận.

#### 4. Lỗi giải tham chiếu con trỏ rỗng (Null Pointer Dereference)
- **개념 (Khái niệm):** Xảy ra khi chương trình cố gắng đọc, ghi hoặc gọi phương thức thông qua một con trỏ đang trỏ tới địa chỉ `NULL` (hoặc `0x00000000`).
- **Hậu quả an ninh:** Bộ quản lý bộ nhớ phần cứng (MMU) phát hiện hành vi truy xuất vùng nhớ cấm và kích hoạt lỗi phân trang bảo vệ (Segmentation Fault / Access Violation), dẫn đến việc ứng dụng bị sập đột ngột (Crash), tạo cơ hội cho kẻ tấn công thực hiện tấn công **Từ chối dịch vụ (DoS)**.
- **Biện pháp lập trình an toàn:** Luôn kiểm tra điều kiện con trỏ khác `NULL` trước khi sử dụng; áp dụng lớp đóng gói an toàn như `Optional<T>` trong Java hoặc con trỏ thông minh (Smart Pointers) trong C++.

#### 5. Nhóm lỗi quản lý tài nguyên hệ thống (Resource Handling Errors)
- **Giải phóng tài nguyên không thỏa đáng (부적절한 자원 해제):**
  - Chương trình mở tệp (File Handle), cấp phát bộ nhớ động (`malloc`), hoặc mở kết nối CSDL (`Connection`) nhưng không đóng lại sau khi sử dụng hoặc khi xảy ra ngoại lệ. Dẫn đến rò rỉ bộ nhớ (Memory Leak) và cạn kiệt tệp mô tả (File Descriptor Exhaustion).
  - *Biện pháp:* Đặt lệnh đóng tài nguyên trong khối `finally` hoặc sử dụng cú pháp tự động giải phóng tài nguyên (`try-with-resources` trong Java, `with` trong Python).
- **Sử dụng tài nguyên sau khi giải phóng (Use After Free - UAF):**
  - Con trỏ vẫn tiếp tục truy cập vùng nhớ sau khi đã gọi hàm `free()`. Vùng nhớ này có thể bị hệ điều hành cấp phát lại cho một đối tượng khác, tạo cơ hội cho kẻ tấn công thực thi mã độc tùy ý.
  - *Biện pháp:* Gán con trỏ bằng `NULL` ngay lập tức sau khi giải phóng (`free(ptr); ptr = NULL;`).

#### 6. Bảng đối chiếu các API có lỗ hổng và hàm thay thế an toàn

| Hàm có lỗ hổng (Vulnerable API) | Nguy cơ bảo mật cố hữu | Hàm thay thế an toàn (Secure Alternative) | Nguyên lý an toàn |
| :--- | :--- | :--- | :--- |
| **`gets()`** | Tuyệt đối không kiểm tra kích thước đệm đầu vào, luôn gây tràn bộ đệm. | **`fgets(buf, sizeof(buf), stdin)`** | Giới hạn số ký tự đọc tối đa bằng kích thước vùng đệm đích. |
| **`strcpy(dest, src)`** | Sao chép toàn bộ chuỗi cho đến khi gặp `\0` mà không quan tâm kích thước `dest`. | **`strncpy(dest, src, sizeof(dest) - 1)`** | Giới hạn số byte sao chép tối đa; bắt buộc gán `dest[sizeof(dest) - 1] = '\0'`. |
| **`sprintf(dest, format, ...)`** | Ghép định dạng chuỗi không kiểm soát độ dài kết quả đầu ra. | **`snprintf(dest, sizeof(dest), format, ...)`** | Chỉ định kích thước bộ đệm tối đa để ngăn tràn số ký tự định dạng. |
| **`strcat(dest, src)`** | Nối chuỗi vào đuôi không kiểm tra dung lượng còn lại của `dest`. | **`strncat(dest, src, max_len)`** | Kiểm soát độ dài tối đa của chuỗi nối thêm. |
| **`rand()`, `srand()`** | Bộ sinh số ngẫu nhiên giả có quy luật tuần hoàn, dễ bị đoán trước khóa bảo mật. | **`SecureRandom`** (Java) / **`/dev/urandom`** (Linux) | Bộ sinh số ngẫu nhiên bảo mật mật mã học (CSPRNG) thu thập độ hỗn loạn từ phần cứng. |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### Bẫy ký tự Null kết thúc chuỗi (`\0`) khi dùng hàm `strncpy`
Rất nhiều lập trình viên mắc sai lầm nghiêm trọng khi sử dụng `strncpy(dest, src, sizeof(dest))`:
- **Cơ chế nguy hiểm:** Nếu độ dài chuỗi nguồn `src` lớn hơn hoặc bằng kích thước vùng đệm đích `sizeof(dest)`, hàm `strncpy` sẽ sao chép đủ số byte nhưng **KHÔNG tự động chèn ký tự Null (`\0`)** vào cuối chuỗi `dest`.
- **Hậu quả:** Khi một hàm khác (như `printf("%s", dest)` hoặc `strlen(dest)`) đọc chuỗi `dest`, nó sẽ tiếp tục đọc tràn qua ranh giới của mảng trên bộ nhớ cho đến khi tình cờ gặp một byte `0x00`, dẫn đến rò rỉ thông tin bộ nhớ ngăn xếp (Stack Information Disclosure).
- **Mẫu mã an toàn bắt buộc:**
  ```c
  strncpy(dest, src, sizeof(dest) - 1);
  dest[sizeof(dest) - 1] = '\0'; // Bắt buộc thủ công gán ký tự kết thúc chuỗi
  ```

---

### 복습 체크리스트
- [ ] Nắm vững cơ chế tràn bộ đệm: Ghi đè lên Return Address trên Stack để chuyển hướng CPU.
- [ ] Nhớ 3 kỹ thuật phòng vệ Buffer Overflow: Stack Guard/Canary (giá trị kiểm tra), ASLR (xáo trộn địa chỉ), DEP/NX (cấm thực thi mã trên Stack/Heap).
- [ ] Nhận diện nguy cơ Command Injection qua các ký tự phân tách lệnh: `;`, `|`, `&&`, `||`.
- [ ] Phân biệt được XSS (lừa máy khách) vs CSRF (lợi dụng sự tin tưởng của máy chủ đối với Session nạn nhân).
- [ ] Nắm được 3 giải pháp phòng vệ CSRF: CSRF Token, SameSite Cookie, Re-authentication.
- [ ] Hiểu lỗi Null Pointer Dereference: Làm sập chương trình (Crash / DoS) do MMU kích hoạt Segmentation Fault.
- [ ] Thuộc lòng các cặp API thay thế an toàn: `gets` $\rightarrow$ `fgets`, `strcpy` $\rightarrow$ `strncpy`, `sprintf` $\rightarrow$ `snprintf`, `rand` $\rightarrow$ `SecureRandom`.
