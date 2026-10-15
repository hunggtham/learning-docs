# ⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cơ chế phát sinh và biện pháp phòng chống các lỗ hổng mã nguồn và lạm dụng giao diện lập trình (**코드 오류 및 API 오용 - Code Errors & API Misuse**) theo tiêu chuẩn bảo mật phần mềm (SW 보안 약점 진단 가이드).
- Hiểu sâu sắc cơ chế gây lỗi và sập hệ thống của hiện tượng giải tham chiếu con trỏ rỗng (**널 포인터 역참조 - Null Pointer Dereference**), tràn số nguyên (**정수 오버플로 - Integer Overflow**), và ép sai kiểu dữ liệu (**부적절한 형변환**).
- Nhận diện các bẫy sử dụng sai API bảo mật: Sử dụng hàm tạo số ngẫu nhiên không an toàn (`rand()`), thuật toán mã hóa lỗi thời (DES, MD5), và sử dụng tra cứu DNS để ra quyết định bảo mật (**보안 결정에 허용되지 않는 DNS 조회**).

## 핵심 키워드 (Từ khóa)
- 코드 오류 (Code Implementation Errors)
- 널 포인터 역참조 (Null Pointer Dereference - DoS 공격)
- 정수 오버플로 (Integer Overflow - 경계값 초과)
- 부적절한 형변환 (Improper Type Casting / Type Confusion)
- API 오용 (API Misuse Vulnerabilities)
- 취약한 난수 생성 (Insecure Randomness - `java.util.Random` vs `SecureRandom`)
- 보안 결정에 허용되지 않는 DNS 조회 (DNS Spoofing Risk)
- 취약한 암호 알고리즘 사용 (Deprecated Crypto: DES, MD5, SHA-1)

## 선행·연결 개념 (Kiến thức liên kết)
- [15-bai-hoc.md](15-bai-hoc.md): Kỹ thuật kiểm soát lỗi đường truyền và các phương thức chuyển mạch.
- [17-bai-hoc.md](17-bai-hoc.md): Lỗi quản lý tài nguyên (Improper Resource Release, Use After Free).
- [70-bai-hoc.md](70-bai-hoc.md): Nhận diện các lỗ hổng bảo mật máy chủ (Buffer Overflow, SQL Injection).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh các lỗi mã nguồn và API trong đề thi:
  - Khi hỏi về **널 포인터 역참조 (Null Pointer Dereference):** Con trỏ hoặc biến đối tượng mang giá trị `null` nhưng chương trình lại cố tình truy xuất trường hoặc gọi hàm của nó (`ptr->member` hoặc `obj.method()`) $\rightarrow$ Dẫn đến **sập ứng dụng (Crash)** hoặc bị kẻ tấn công khai thác gây **từ chối dịch vụ (DoS)**. Khắc phục bằng cách kiểm tra điều kiện `if (obj != null)` trước khi dùng.
  - Khi hỏi về **API 오용 (Lạm dụng API):**
    - Sử dụng hàm tạo số ngẫu nhiên đơn giản (`rand()`, `Math.random()`) để tạo khóa bảo mật $\rightarrow$ Dễ bị hacker đoán trước. Bắt buộc phải dùng **`SecureRandom`**.
    - Sử dụng địa chỉ IP tra cứu từ DNS để phân quyền $\rightarrow$ Kẻ tấn công làm giả DNS (DNS Cache Poisoning) để vượt mặt hệ thống kiểm tra.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu các lỗi cài đặt mã nguồn (Code Errors) điển hình:**

| Lỗ hổng mã nguồn | Tên tiếng Hàn & Anh | Cơ chế phát sinh & Hậu quả an ninh | Giải pháp phòng chống chuẩn |
| :--- | :--- | :--- | :--- |
| **Giải tham chiếu con trỏ rỗng** | **널 포인터 역참조** (Null Pointer Dereference) | Thực hiện thao tác đọc/ghi trên địa chỉ con trỏ hoặc đối tượng đang mang giá trị `NULL` (chưa được khởi tạo hoặc hàm trước đó trả về thất bại). Gây Exception, sập chương trình đột ngột (DoS). | Luôn kiểm tra tính hợp lệ của con trỏ trước khi gọi (`if (p != NULL) { ... }`). |
| **Tràn số nguyên** | **정수 오버플로** (Integer Overflow / Underflow) | Kết quả của phép tính số học vượt quá giá trị cực đại (`INT_MAX`) hoặc cực tiểu của kiểu dữ liệu, làm giá trị bị cuộn tròn (Wrap-around, ví dụ số dương lớn biến thành số âm). | Kiểm tra cận giới hạn trước khi thực hiện phép tính số học; dùng kiểu số nguyên lớn (`long long`, `BigInteger`). |
| **Ép sai kiểu dữ liệu** | **부적절한 형변환** (Type Confusion / Bad Cast) | Ép kiểu ép buộc giữa các lớp đối tượng hoặc kiểu con trỏ không tương thích trong cây kế thừa; dẫn đến truy xuất sai vùng nhớ thực tế. | Sử dụng toán tử kiểm tra kiểu an toàn (`instanceof` trong Java, `dynamic_cast` trong C++). |
| **Bỏ qua giá trị trả về** | **반환값 미검사** (Unchecked Return Value) | Không kiểm tra giá trị trả về của các hàm hệ thống (như `malloc`, `fread`, hàm kiểm tra quyền), giả định hàm luôn chạy thành công. | Luôn hứng và xử lý ngoại lệ theo đúng mã trạng thái trả về của API. |

- **2. Bảng phân loại các trường hợp lạm dụng API (API Misuse):**

| Hành vi dùng sai API | Nguy cơ bảo mật tiềm ẩn | Giải pháp chuẩn mực quốc tế |
| :--- | :--- | :--- |
| **Tạo số ngẫu nhiên yếu (취약한 난수)** | Sử dụng hàm tạo số ngẫu nhiên tuần tự mang tính dự đoán được như `rand()` trong C hoặc `java.util.Random` trong Java để sinh Token phiên làm việc, Khóa bí mật hay Mã OTP. Kẻ tấn công có thể phân tích hạt giống (Seed) để đoán trước mã bí mật. | Bắt buộc sử dụng các thư viện tạo số ngẫu nhiên an toàn mã hóa chuẩn mật mã: **`SecureRandom`** trong Java, hoặc `/dev/urandom` trong Linux. |
| **Ra quyết định bảo mật bằng DNS (보안 결정에 허용되지 않는 DNS 조회)** | Sử dụng hàm tra cứu tên miền ngược (Reverse DNS Lookup: `gethostbyaddr()`) để kiểm tra xem máy khách có thuộc tên miền tin cậy (ví dụ `trusted.com`) hay không trước khi cấp quyền truy cập. Kẻ tấn công có thể giả mạo bảng phân giải DNS (DNS Spoofing) để đánh lừa máy chủ. | **Tuyệt đối không dùng tên miền DNS để xác thực quyền hạn**; bắt buộc xác thực danh tính qua chữ ký số, chứng chỉ SSL/TLS hoặc khóa bí mật. |
| **Dùng thuật toán mật mã lỗi thời (취약한 암호화)** | Tiếp tục sử dụng các thuật toán mã hóa cổ đã bị toán học giải mã hoặc có độ dài khóa quá ngắn như **DES (56-bit), RC4, MD5, SHA-1**. | Chuyển dịch lên các tiêu chuẩn hiện đại: **AES-256**, **RSA-2048 bit trở lên**, và chuỗi hàm băm an toàn **SHA-256 / SHA-3**. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa lỗ hổng Null Pointer Dereference trong Java:**
  ```java
  public void printUser(User user) {
      // Nguy cơ: Nếu user là null -> Ném NullPointerException làm sập thread
      // Sai: System.out.println(user.getName());

      // Đúng chuẩn phòng thủ:
      if (user != null && user.getName() != null) {
          System.out.println(user.getName());
      } else {
          System.out.println("Default Guest");
      }
  }
  ```

### 복습 체크리스트
- [ ] Nhớ lỗi Null Pointer Dereference phát sinh khi truy xuất con trỏ rỗng và gây sập ứng dụng (DoS).
- [ ] Nhớ Integer Overflow xảy ra khi giá trị vượt quá giới hạn cực đại khiến số dương cuộn thành số âm.
- [ ] Khẳng định không được dùng `rand()` để tạo khóa bảo mật mà phải dùng `SecureRandom`.
- [ ] Nắm được nguy cơ khi dùng DNS Lookup để ra quyết định an ninh: Dễ bị tấn công giả mạo DNS Spoofing.
- [ ] Kể tên các thuật toán mật mã cổ yếu cần loại bỏ: DES, RC4, MD5, SHA-1.
