# 소프트웨어 취약점 방어 및 시큐어 코딩 (Phòng thủ lỗ hổng phần mềm & Lập trình an toàn Secure Coding)

## 학습 목표 (Mục tiêu)
- Nắm vững bản chất cơ chế phát sinh, kịch bản tấn công và giải pháp lập trình an toàn cho 5 lỗ hổng mã nguồn nguy hiểm hàng đầu theo OWASP Top 10 và KISA Secure Coding: **SQL Injection**, **XSS**, **CSRF**, **Buffer Overflow**, và **Race Condition (TOCTOU)**.
- Phân biệt cơ chế phòng vệ SQL Injection bằng câu truy vấn tham số hóa (**매개변수화된 쿼리 - `PreparedStatement`**) so với việc nối chuỗi truy vấn động.
- So sánh toàn diện 3 biến thể XSS: **Stored XSS (저장형)**, **Reflected XSS (반사형)**, và **DOM-based XSS (DOM 기반)** cùng kỹ thuật mã hóa thực thể HTML (**HTML Entity Encoding**).
- Phân biệt cơ chế bảo vệ vùng nhớ Stack/Heap chống tràn bộ đệm: **Stack Guard/Canary**, **ASLR**, **DEP/NX** và cách sử dụng chuẩn mực hàm `strncpy` thay cho `strcpy`.
- Hiểu rõ bản chất lỗi điều kiện tương tranh **Race Condition** và cơ chế lỗ hổng kiểm tra - sử dụng (**TOCTOU - Time of Check to Time of Use**).
- Thuộc lòng danh sách các API có lỗ hổng cố hữu và các hàm thay thế an toàn chuẩn mực trong C/C++ và Java.

## 핵심 키워드 (Từ khóa song ngữ)
- SQL 삽입 (SQL Injection — Nối chuỗi truy vấn động, phòng ngừa bằng PreparedStatement)
- XSS (크로스 사이트 스크립팅 — Stored 저장형, Reflected 반사형, DOM 기반, HTML Entity Encoding)
- CSRF (사이트 간 요청 위조 — Lợi dụng phiên xác thực của nạn nhân, Anti-CSRF Token, SameSite Cookie)
- 버퍼 오버플로 (Buffer Overflow — Tràn bộ đệm ghi đè Return Address trên Stack)
- 스택 가드 / 카나리 (Stack Guard / Canary — Giá trị ngẫu nhiên kiểm tra tràn bộ đệm trước RET)
- ASLR (Address Space Layout Randomization — Xáo trộn không gian địa chỉ bộ nhớ)
- DEP / NX (Data Execution Prevention / No-Execute — Ngăn chặn thực thi mã trên Stack/Heap)
- 경쟁 조건 (Race Condition — Điều kiện tương tranh giữa các tiến trình/luồng đồng thời)
- TOCTOU (Time of Check to Time of Use — Lỗ hổng bất đồng bộ giữa thời điểm kiểm tra và sử dụng)
- 취약한 API (Vulnerable API — `gets` $\rightarrow$ `fgets`, `strcpy` $\rightarrow$ `strncpy`, `sprintf` $\rightarrow$ `snprintf`)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Từ khung quy trình bảo mật Secure SDLC đã học ở [05-khung-bao-mat-phan-mem-va-phap-luat.md](05-khung-bao-mat-phan-mem-va-phap-luat.md), các nguy cơ an ninh phải được loại trừ trực tiếp ở cấp độ mã nguồn bằng kỹ thuật lập trình phòng thủ (Defensive Coding).
- **Đang giải quyết gì (Current Problem):** Bài học này đi sâu vào cơ chế nhị phân và kiến trúc mã nguồn để mổ xẻ các lỗ hổng nguy hiểm nhất (SQL Injection, XSS, CSRF, Buffer Overflow, Race Condition) và cung cấp các giải pháp vá lỗi triệt để cả ở tầng mã nguồn lẫn tầng hệ điều hành.
- **Dùng đi đâu (Forward Handoff):** Để bảo vệ dữ liệu khỏi bị trích xuất hoặc can thiệp khi các lỗ hổng bị dò quét, hệ thống phải mã hóa dữ liệu nhạy cảm bằng các thuật toán tại [07-thuat-toan-ma-hoa-va-mat-ma-hoc.md](07-thuat-toan-ma-hoa-va-mat-ma-hoc.md) và thiết lập hàng rào kiểm soát truy cập tại [08-xac-thuc-va-kiem-soat-truy-cap.md](08-xac-thuc-va-kiem-soat-truy-cap.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **SQL Injection (SQL 삽입):**
  - Dấu hiệu nhận diện: Nối chuỗi truy vấn SQL trực tiếp với dữ liệu người dùng (`"SELECT * FROM user WHERE id = '" + id + "'"`).
  - Biện pháp phòng ngừa số 1: Luôn chọn **매개변수화된 쿼리 (Parameterized Query / `PreparedStatement`)**; biến tham số thành literal dữ liệu, không biên dịch lại cú pháp.
- **XSS vs CSRF (Bẫy đề thi kinh điển):**
  - **XSS:** Khai thác **sự tin tưởng của người dùng đối với trang web**; chèn mã JavaScript độc hại vào trang web để đánh cắp Cookie trên trình duyệt nạn nhân.
  - **CSRF:** Khai thác **sự tin tưởng của máy chủ đối với trình duyệt của người dùng**; lợi dụng Session Cookie hợp lệ để ép người dùng gửi yêu cầu trái phép.
  - Phân biệt 3 loại XSS: Lưu trong CSDL $\rightarrow$ **Stored XSS**; Nằm trong URL $\rightarrow$ **Reflected XSS**; Xử lý hoàn toàn ở client $\rightarrow$ **DOM XSS**.
- **Tràn bộ đệm (Buffer Overflow):**
  - Cơ chế: Ghi dữ liệu vượt quá kích thước mảng đệm $\rightarrow$ Ghi đè lên **복귀 주소 (Return Address / RET)** để chuyển hướng CPU sang Shellcode.
  - Các kỹ thuật phòng vệ tầng OS/Compiler:
    - **스택 가드 (Canary):** Đặt giá trị kiểm tra trước Return Address.
    - **ASLR:** Xáo trộn địa chỉ nạp Stack, Heap, Libc ngẫu nhiên mỗi lần chạy.
    - **DEP/NX:** Cấm CPU thực thi lệnh trên vùng nhớ Stack/Heap.
- **Race Condition & TOCTOU:**
  - Nhắc đến **"검사 시점(Check)과 사용 시점(Use) 사이의 시간 차이를 이용"** $\rightarrow$ Chọn ngay **TOCTOU / 경쟁 조건 (Race Condition)**.
- **API dễ bị tổn thương (Vulnerable APIs):**
  - Nhìn thấy `gets()` $\rightarrow$ Thay ngay bằng `fgets()`.
  - Nhìn thấy `strcpy()`, `strcat()` $\rightarrow$ Thay ngay bằng `strncpy()`, `strncat()`.
  - Nhìn thấy `sprintf()` $\rightarrow$ Thay ngay bằng `snprintf()`.
  - Nhìn thấy bộ sinh số ngẫu nhiên `rand()` $\rightarrow$ Thay bằng `SecureRandom`.

---

## 소프트웨어 취약점 방어 및 시큐어 코딩

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Lỗ hổng chèn câu truy vấn SQL (SQL Injection)
- **개념 (Khái niệm):** Xảy ra khi ứng dụng nhận dữ liệu đầu vào từ người dùng rồi nối trực tiếp vào chuỗi câu lệnh SQL để gửi tới hệ quản trị CSDL mà không qua cơ chế kiểm tra tính hợp lệ.
- **Kịch bản tấn công:** Kẻ tấn công nhập các chuỗi ký tự thao túng logic điều kiện (ví dụ: `' OR '1'='1` hoặc `admin' --`), biến đổi mệnh đề `WHERE` luôn trả về giá trị `TRUE`, giúp đăng nhập trái phép vào tài khoản quản trị mà không cần biết mật khẩu.
- **Biện pháp phòng ngừa chuẩn mực:**
  - **Dùng câu truy vấn tham số hóa (`PreparedStatement`):** CSDL biên dịch trước cấu trúc câu truy vấn (Skeleton), các giá trị đầu vào chỉ được truyền vào dưới dạng tham số thuần túy (Data Literal). Dù đầu vào có chứa ký tự `' OR '1'='1` thì hệ thống vẫn coi đó là một chuỗi văn bản thông thường, không thể làm thay đổi cấu trúc cú pháp của lệnh SQL ban đầu.
  - **Sử dụng khung ORM an toàn (MyBatis, JPA):** Sử dụng cú pháp ánh xạ tham số `#` (ví dụ: `#{userId}`) thay vì nối chuỗi trực tiếp bằng `$`.
  - **Lọc ký tự đặc biệt (Input Sanitization):** Loại bỏ hoặc kiểm tra nghiêm ngặt các ký tự nhạy cảm: `'`, `"`, `;`, `--`, `/*`, `*/`.

#### 2. Tấn công chèn mã kịch bản liên trang (XSS - Cross-Site Scripting)
- **개념 (Khái niệm):** Kẻ tấn công chèn các đoạn mã kịch bản độc hại (thường là JavaScript `<script>`) vào ứng dụng web. Khi người dùng hợp lệ duyệt trang web đó, đoạn mã sẽ tự động thực thi trên trình duyệt của nạn nhân để đánh cắp Cookie phiên làm việc, chiếm đoạt tài khoản hoặc chuyển hướng sang trang web giả mạo.
- **Ba biến thể XSS kinh điển:**

| Biến thể XSS | Tên tiếng Hàn & Anh | Cơ chế phát tán & Mức độ đe dọa |
| :--- | :--- | :--- |
| **XSS lưu trữ** | **저장형 XSS (Stored / Persistent)** | Mã script độc hại được lưu trữ vĩnh viễn trực tiếp trong CSDL của máy chủ (qua bài viết diễn đàn, phần bình luận). Mọi người dùng khi truy cập vào bài viết đều bị thực thi mã độc. Mức độ nguy hiểm cao nhất và phạm vi ảnh hưởng rộng nhất. |
| **XSS phản xạ** | **반사형 XSS (Reflected / Non-Persistent)** | Mã script độc hại được chèn trực tiếp trong URL (tham số tìm kiếm hoặc liên kết độc hại). Kẻ tấn công lừa nạn nhân bấm vào liên kết; máy chủ nhận Request và phản hồi lại nội dung kèm mã độc trong trang kết quả để trình duyệt nạn nhân tự thực thi. |
| **XSS dựa trên DOM** | **DOM 기반 XSS (DOM-based XSS)** | Đoạn mã script được xử lý và thực thi hoàn toàn trong môi trường trình duyệt máy khách (Client-side) thông qua việc thao tác trực tiếp trên cây DOM (như `document.location`, `innerHTML`). Dữ liệu độc hại không cần gửi qua máy chủ web. |

- **Biện pháp phòng ngừa chuẩn mực:**
  - **Mã hóa thực thể HTML (HTML Entity Encoding):** Chuyển đổi toàn bộ các ký tự điều khiển HTML thành các thực thể an toàn trước khi in ra màn hình trình duyệt:
    - `<` chuyển thành `&lt;`
    - `>` chuyển thành `&gt;`
    - `&` chuyển thành `&amp;`
    - `"` chuyển thành `&quot;`
    - `'` chuyển thành `&#x27;`
  - **Đặt cờ `HttpOnly` cho Cookie:** Hướng dẫn trình duyệt không cho phép bất kỳ đoạn mã JavaScript nào truy xuất vào Cookie xác thực, vô hiệu hóa hoàn toàn nguy cơ đánh cắp Session Cookie qua XSS.

#### 3. Giả mạo yêu cầu liên trang (CSRF - Cross-Site Request Forgery)
- **개념 (Khái niệm):** Cuộc tấn công lừa trình duyệt của nạn nhân (người dùng đã được xác thực hợp lệ trên trang web mục tiêu) tự động gửi các yêu cầu HTTP trái phép (như chuyển khoản ngân hàng, đổi email, đổi mật khẩu) tới máy chủ mà người dùng không hề hay biết.
- **Đối chiếu sự khác nhau sống còn giữa XSS và CSRF:**

| Tiêu chí | Tấn công XSS (Cross-Site Scripting) | Tấn công CSRF (Cross-Site Request Forgery) |
| :--- | :--- | :--- |
| **Bản chất khai thác** | Khai thác **sự tin tưởng của người dùng đối với trang web**. | Khai thác **sự tin tưởng của máy chủ đối với trình duyệt của người dùng**. |
| **Vị trí thực thi mã** | Chèn và thực thi mã script độc hại (JavaScript) ngay trong trình duyệt của nạn nhân. | Không thực thi mã script trên trang đích; chỉ mượn phiên làm việc hợp lệ (Cookie/Session) để gửi Request. |
| **Mục tiêu tấn công** | Đánh cắp Cookie phiên làm việc, Token xác thực, ghi lại phím bấm (Keylogger). | Ép người dùng thực hiện một hành động ngoài ý muốn (Chuyển tiền, Xóa tài khoản). |

- **Các biện pháp phòng thủ CSRF chuẩn công nghiệp:**
  1. **Anti-CSRF Token (CSRF 토큰 검증):** Mỗi khi hiển thị Form, máy chủ sinh ra một chuỗi mã ngẫu nhiên bí mật gắn kèm vào Form ẩn. Khi người dùng gửi Form, máy chủ sẽ đối chiếu Token nhận được với Token trong phiên làm việc. Kẻ tấn công trên trang web khác không thể đọc được Token này do bị chặn bởi chính sách cùng nguồn gốc (Same-Origin Policy).
  2. **Thuộc tính SameSite của Cookie:** Đặt cờ `SameSite=Strict` hoặc `SameSite=Lax` trên Cookie xác thực để hướng dẫn trình duyệt không tự động gửi kèm Cookie trong các yêu cầu liên trang (Cross-site Requests).
  3. **Tái xác thực (Re-authentication):** Bắt buộc người dùng phải nhập lại mật khẩu hoặc mã OTP xác nhận đối với các tác vụ nhạy cảm.

#### 4. Lỗ hổng tràn bộ đệm bộ nhớ (Memory Buffer Overflow)
- **개념 (Khái niệm):** Xảy ra trong các ngôn ngữ lập trình bậc thấp (C/C++) khi chương trình sao chép dữ liệu vượt quá dung lượng vùng nhớ đệm (Buffer) được cấp phát trên Stack hoặc Heap, dẫn đến việc ghi đè lên các ô nhớ liền kề.
- **Hậu quả an ninh:** Kẻ tấn công tính toán chính xác số byte cần thiết để ghi đè lên **Địa chỉ quay về (Return Address / RET)** trong Stack Frame của hàm, ép CPU nhảy đến đoạn mã độc (Shellcode) do kẻ tấn công cài cắm để chiếm toàn quyền điều khiển hệ thống.
- **Các cơ chế phòng vệ hệ thống (Compiler & OS Protection):**

| Cơ chế bảo vệ | Tên tiếng Hàn & Anh | Nguyên lý hoạt động phòng vệ |
| :--- | :--- | :--- |
| **Stack Guard / Canary** | **스택 가드 / 카나리** | Trình biên dịch tự động chèn một giá trị ngẫu nhiên (Canary) nằm ngay giữa biến cục bộ và Return Address. Trước khi hàm thoát ra, CPU kiểm tra lại Canary; nếu giá trị bị thay đổi (bị tràn đè lên), chương trình sẽ lập tức bị hủy bỏ (Abort) để ngăn chặn chuyển hướng luồng thực thi. |
| **ASLR** | **ASLR (주소 공간 배치 난수화)** | Hệ điều hành tự động xáo trộn ngẫu nhiên vị trí không gian địa chỉ của Stack, Heap và các thư viện liên kết động (libc) mỗi khi chương trình khởi chạy, khiến kẻ tấn công không thể xác định địa chỉ tĩnh để trỏ Return Address về. |
| **DEP / NX bit** | **DEP (데이터 실행 방지) / NX** | Đánh dấu vùng nhớ ngăn xếp (Stack) và đống (Heap) là vùng nhớ không thể thực thi mã lệnh (No-Execute). Nếu CPU cố tình nhảy vào thực thi lệnh tại vùng nhớ đệm, phần cứng sẽ kích hoạt ngoại lệ ngắt ngay lập tức. |

#### 5. Điều kiện tương tranh và Lỗ hổng TOCTOU (Race Condition & TOCTOU)
- **개념 (Khái niệm):** Xảy ra khi hai hay nhiều tiến trình hoặc luồng cùng truy cập và thao tác đồng thời trên một tài nguyên dùng chung (tệp tin, biến bộ nhớ) mà kết quả cuối cùng phụ thuộc vào thứ tự thực thi của các tiến trình đó.
- **Lỗ hổng TOCTOU (Time of Check to Time of Use):**
  - **Bản chất:** Là một dạng lỗ hổng Race Condition kinh điển phát sinh do có một khoảng thời gian trễ giữa **thời điểm kiểm tra quyền hợp lệ (Time of Check)** và **thời điểm thực tế sử dụng tài nguyên (Time of Use)**.
  - **Kịch bản khai thác:** Kẻ tấn công lợi dụng khoảng thời gian trễ này để thay đổi tài nguyên (ví dụ: thay thế một tệp tin bình thường bằng một liên kết tượng trưng Symbolic Link trỏ tới tệp hệ thống tối mật `/etc/shadow`), khiến chương trình sau khi vượt qua bước kiểm tra quyền sẽ vô tình ghi đè lên tệp hệ thống.
  - **Biện pháp phòng ngừa:**
    - Sử dụng các thao tác nguyên tử (**Atomic Operations**) kết hợp kiểm tra và truy cập trong cùng một bước.
    - Áp dụng cơ chế khóa tài nguyên dùng chung (File Locking, Mutex, Semaphore) trong toàn bộ chu trình xử lý.

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

#### Mẫu mã an toàn phòng ngừa SQL Injection với `PreparedStatement`
- **Mã nguồn không an toàn (Vulnerable Code):**
  ```java
  // Ghép chuỗi trực tiếp: Kẻ tấn công nhập id = "' OR '1'='1" -> Vượt qua xác thực!
  String query = "SELECT * FROM member WHERE id = '" + id + "' AND pw = '" + pw + "'";
  Statement stmt = conn.createStatement();
  ResultSet rs = stmt.executeQuery(query);
  ```
- **Mã nguồn lập trình an toàn (Secure Code):**
  ```java
  // Sử dụng PreparedStatement với dấu hỏi ? đại diện cho tham số
  String query = "SELECT * FROM member WHERE id = ? AND pw = ?";
  PreparedStatement pstmt = conn.prepareStatement(query);
  pstmt.setString(1, id); // Dữ liệu id được đối xử như một giá trị hằng số Literal
  pstmt.setString(2, pw);
  ResultSet rs = pstmt.executeQuery();
  ```

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
- [ ] Hiểu rõ cơ chế SQL Injection và giải pháp số 1: Sử dụng câu truy vấn tham số hóa (PreparedStatement).
- [ ] Phân biệt 3 biến thể XSS: Stored XSS (lưu trong CSDL, nguy hiểm nhất), Reflected XSS (nằm trong URL), DOM-based XSS (xử lý ở trình duyệt).
- [ ] Nắm vững kỹ thuật phòng vệ XSS: Mã hóa thực thể HTML (HTML Entity Encoding) và bật cờ HttpOnly cho Cookie.
- [ ] Phân biệt XSS (lừa máy khách) vs CSRF (lợi dụng phiên xác thực của nạn nhân gửi yêu cầu trái phép tới máy chủ).
- [ ] Nhớ 3 giải pháp phòng vệ CSRF: Anti-CSRF Token, SameSite Cookie, Re-authentication.
- [ ] Nắm vững cơ chế tràn bộ đệm: Ghi đè lên Return Address trên Stack để chuyển hướng CPU.
- [ ] Nhớ 3 kỹ thuật phòng vệ Buffer Overflow: Stack Guard/Canary (giá trị kiểm tra), ASLR (xáo trộn địa chỉ), DEP/NX (cấm thực thi mã trên Stack/Heap).
- [ ] Hiểu bản chất Race Condition và lỗ hổng TOCTOU: Lợi dụng khoảng thời gian trễ giữa lúc kiểm tra và lúc sử dụng để hoán đổi tài nguyên.
- [ ] Thuộc lòng các cặp API thay thế an toàn: `gets` $\rightarrow$ `fgets`, `strcpy` $\rightarrow$ `strncpy`, `sprintf` $\rightarrow$ `snprintf`, `rand` $\rightarrow$ `SecureRandom`.
