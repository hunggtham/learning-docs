# 서버 프로그램 구현: 프레임워크, 배치, 보안 취약점 및 DB 연동 (Triển khai Server: Batch, Bảo mật & DB)

## 학습 목표 (Mục tiêu)
- Phân biệt kiến trúc môi trường máy chủ giữa Máy chủ Web (Web Server - xử lý nội dung tĩnh) và Máy chủ ứng dụng Web (WAS - Web Application Server - xử lý logic động và kết nối CSDL).
- Thuộc lòng 5 yếu tố bắt buộc của Chương trình xử lý hàng loạt Batch theo khẩu quyết **대자견안성** (Đại dung lượng, Tự động hóa, Kiên cố, Ổn định, Hiệu năng) và 3 kiểu kích hoạt Batch (Scheduled, Event-driven, On-demand).
- Nhận diện và nêu giải pháp khắc phục cho 4 lỗ hổng bảo mật mã nguồn kinh điển: Tràn bộ đệm (Buffer Overflow), Con trỏ lơ lửng (Dangling Pointer), Tấn công tiêm mã SQL (SQL Injection với `PreparedStatement`) và Chuỗi định dạng (Format String).
- Thấu hiểu cơ chế Hồ kết nối cơ sở dữ liệu (Database Connection Pool - DBCP), phân biệt hai chuẩn kết nối JDBC (Java) vs ODBC (Microsoft), cùng dịch vụ Web Mashup và kiến trúc SOA.

## 핵심 키워드 (Từ khóa)
- 웹 서버 vs WAS (Web Server vs WAS) — Tĩnh (Apache, Nginx) vs Động (Tomcat, WebLogic, Jeus).
- 배치 프로그램 5대 요소 (Batch Program 5 Elements) — 대용량 데이터, 자동화, 견고성, 안정성, 성능 (대자견안성).
- 배치 실행 유형 (Batch Execution Types) — 정기 배치 (Scheduled), 이벤트 배치 (Event-driven), On-demand 배치 (Theo yêu cầu).
- 데이터베이스 커넥션 풀 (DBCP - Connection Pool) — Khởi tạo sẵn hồ kết nối DB, tái sử dụng chống nghẽn handshake.
- 버퍼 오버플로 (Buffer Overflow) — Tràn bộ đệm ghi đè địa chỉ trả về (Return Address); phòng chống bằng `strncpy`, `fgets`.
- 허상 포인터 (Dangling Pointer) — Con trỏ trỏ tới vùng nhớ đã bị giải phóng `free()`; phòng chống bằng gán `NULL`.
- SQL 삽입 (SQL Injection) — Tấn công chèn mã SQL trái phép; phòng chống triệt để bằng `PreparedStatement`.
- DB 연동 기술 (Database Connectivity) — JDBC (Java 표준) vs ODBC (MS 주도).

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Bài học tổng hợp và khép lại toàn bộ chương trình Môn 4, kế thừa toàn bộ kỹ năng lập trình C/Java, bảo mật con trỏ, quản lý bộ nhớ và kết nối mạng từ bài 01 đến bài 21.
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi thực tế khi triển khai phần mềm phía máy chủ (Server-side): Làm sao để ứng dụng vận hành tự động an toàn, phân tách Web Server và WAS ra sao, không bị tin tặc khai thác lỗ hổng bộ nhớ và kết nối dữ liệu hiệu năng cao với Connection Pool.
- **Dùng đi đâu (Forward Handoff):** Kiến thức về bảo mật, kết nối DB và xử lý hàng loạt này sẽ liên kết trực tiếp với Môn 3 (Cơ sở dữ liệu) và Môn 5 (Quản lý hệ thống thông tin) để hoàn thiện toàn bộ năng lực thi đỗ chứng chỉ Kỹ sư xử lý thông tin.

## 읽는 방법 (Cách đọc)
- **Web Server vs WAS:**
  - Web Server: Chỉ phục vụ file tĩnh (HTML, CSS, Ảnh) -> Nginx, Apache HTTP Server.
  - WAS: Chạy logic mã nguồn động (JSP, Servlet, Spring), kết nối CSDL -> Tomcat, WebLogic, Jeus.
- **Khẩu quyết Batch:** Nhớ 5 chữ vàng: **대·자·견·안·성** (대용량 Đại dung lượng -> 자동화 Tự động hóa -> 견고성 Kiên cố không sập -> 안정성 Ổn định tin cậy -> 성능 Hiệu năng trong cửa sổ thời gian).
- **3 Kiểu Batch:** Định kỳ (Scheduled), Sự kiện (Event-driven), Yêu cầu tức thời (On-demand).
- **Lỗ hổng bảo mật:**
  - Tràn bộ đệm (Buffer Overflow) -> Cấm dùng `strcpy`, `gets`; thay bằng `strncpy`, `fgets`.
  - Con trỏ lơ lửng (Dangling Pointer) -> Sau khi `free(p)`, lập tức gán `p = NULL;`.
  - SQL Injection -> Dùng **`PreparedStatement`** (Parameterized Binding), cấm nối chuỗi câu lệnh SQL.
- **DBCP:** Mượn kết nối có sẵn trong hồ (Pool), dùng xong trả lại, cấm đóng kết nối vật lý ngắt mạng.

---

## 서버 프로그램 구현: 프레임워크, 배치, 보안 취약점 및 DB 연동

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `웹 서버는 정적 콘텐츠(HTML, 이미지)를 처리하고, WAS는 비즈니스 로직과 DB 연동 등 동적 콘텐츠를 처리한다. 배치 프로그램의 5대 요소는 대용량 데이터, 자동화, 견고성, 안정성, 성능(대자견안성)이며, 실행 유형에는 정기, 이벤트, On-demand 배치가 있다. DBCP는 DB 연결을 미리 생성하여 재사용함으로써 성능을 최적화한다. 버퍼 오버플로는 strncpy로, SQL 삽입은 PreparedStatement로 방지한다.`
  - [Tiếng Việt]: Web Server xử lý nội dung tĩnh (HTML, hình ảnh), còn WAS xử lý logic nghiệp vụ và nội dung động liên kết CSDL. 5 yếu tố cốt lõi của chương trình Batch là Dữ liệu lớn, Tự động hóa, Kiên cố, Ổn định, Hiệu năng (대자견안성), gồm 3 dạng kích hoạt: Định kỳ, Sự kiện, và On-demand. DBCP khởi tạo sẵn kết nối DB để tái sử dụng giúp tối ưu hiệu năng. Tràn bộ đệm được phòng ngừa bằng strncpy, SQL Injection được phòng ngừa bằng PreparedStatement.

- **1. Bảng đối chiếu Máy chủ Web (Web Server) vs Máy chủ ứng dụng Web (WAS):**

| Tiêu chuẩn so sánh | Máy chủ Web (웹 서버 - Web Server) | Máy chủ ứng dụng Web (WAS - Web Application Server) |
| :--- | :--- | :--- |
| **Nhiệm vụ cốt lõi** | Xử lý và phân phối các **tài nguyên tĩnh (Static Content)**: HTML, CSS, JavaScript, hình ảnh. | Thực thi **mã nguồn logic động (Dynamic Logic)**, nghiệp vụ và giao tiếp với CSDL. |
| **Giao thức và công nghệ** | Giao thức HTTP/HTTPS thuần túy. | Servlet Container, JSP Engine, EJB, Spring Framework. |
| **Sản phẩm đại diện** | **Apache HTTP Server, Nginx, Microsoft IIS**. | **Apache Tomcat, Oracle WebLogic, Tmax Jeus, IBM WebSphere, JBoss**. |
| **Mô hình phối hợp** | Đứng ở tầng trước tiếp nhận Request của Client, làm Reverse Proxy và chuyển tiếp request động vào WAS. | Đứng ở tầng sau nhận request từ Web Server, tính toán logic rồi trả kết quả động lại cho Web Server. |

- **2. Bảng 5 yếu tố cốt lõi của Chương trình xử lý hàng loạt (배치 프로그램 5대 요소 - 대자견안성):**

| Yếu tố cốt lõi | Thuật ngữ Hàn / Anh | Nội dung kỹ thuật chuẩn khảo thí HRDK |
| :--- | :--- | :--- |
| **1. Dữ liệu lớn** | **대용량 데이터** (Large Data) | Có khả năng xử lý mượt mà khối lượng dữ liệu khổng lồ trong các chu kỳ định kỳ. |
| **2. Tự động hóa** | **자동화** (Automation) | Vận hành hoàn toàn tự động theo lịch trình đặt trước, **không cần người can thiệp**. |
| **3. Tính kiên cố** | **견고성** (Robustness) | Xử lý ngoại lệ chặt chẽ, **không bị sập hay gián đoạn hệ thống** khi gặp dữ liệu lỗi. |
| **4. Tính ổn định** | **안정성 / 신뢰성** (Reliability) | Đảm bảo toàn vẹn dữ liệu, có cơ chế ghi nhật ký (Logging) và khôi phục khi gặp sự cố. |
| **5. Hiệu năng** | **성능** (Performance) | Hoàn thành toàn bộ khối lượng công việc trong khoảng thời gian cửa sổ cho phép (**Batch Window**). |

- **3. Bảng 3 kiểu kích hoạt xử lý hàng loạt Batch (배치 실행 유형):**

| Kiểu kích hoạt | Thuật ngữ Hàn / Anh | Thời điểm và điều kiện chạy | Ví dụ thực tế |
| :--- | :--- | :--- | :--- |
| **Định kỳ** | **정기 배치** (Scheduled Batch) | Chạy tự động tại các thời điểm cố định đã được lập lịch sẵn. | Chạy lúc 00:00 hàng ngày để tổng kết doanh thu, sao lưu dữ liệu cuối tuần. |
| **Sự kiện** | **이벤트 배치** (Event-driven Batch) | Tự động kích hoạt ngay khi một điều kiện nghiệp vụ xác định phát sinh. | Hệ thống nhận được file đối soát tài khoản từ ngân hàng thì kích hoạt xử lý ngay. |
| **Theo yêu cầu** | **On-demand 배치** (On-demand Batch) | Được kích hoạt thủ công trực tiếp bởi người dùng hoặc quản trị viên hệ thống. | Kế toán viên bấm nút yêu cầu xuất bảng quyết toán thuế đột xuất. |

- **4. Bảng nhận diện lỗ hổng bảo mật mã nguồn và biện pháp khắc phục:**

| Lỗ hổng bảo mật | Cơ chế tấn công của tin tặc | Hàm gây lỗi nguy hiểm | Biện pháp khắc phục chuẩn thi |
| :--- | :--- | :--- | :--- |
| **Tràn bộ đệm (버퍼 오버플로)** | Ghi dữ liệu vượt kích thước mảng trong Stack, ghi đè lên địa chỉ trả về (Return Address) để chiếm quyền CPU. | `strcpy()`, `gets()`, `scanf("%s")`, `strcat()` | Thay thế bằng các hàm có giới hạn độ dài an toàn: `strncpy()`, `fgets()`, `snprintf()`. |
| **Con trỏ lơ lửng (허상 포인터)** | Vùng nhớ đã giải phóng bằng `free()` nhưng con trỏ vẫn trỏ tới; nếu truy cập lại sẽ gây lỗi bộ nhớ nghiêm trọng. | Gọi hàm `free(ptr)` nhưng không xóa con trỏ. | **Gán ngay con trỏ về giá trị rỗng sau khi giải phóng: `ptr = NULL;`**. |
| **Tiêm mã SQL (SQL 삽입)** | Chèn các chuỗi truy vấn độc hại (`' OR '1'='1`) qua ô nhập liệu để đọc trộm hoặc xóa sạch CSDL. | Nối chuỗi SQL động: `"SELECT * FROM u WHERE id='" + input + "'"` | **Sử dụng đối tượng `PreparedStatement`** để truyền tham số an toàn (Parameter Binding). |
| **Chuỗi định dạng (포맷 스트링)** | Truyền trực tiếp chuỗi người dùng vào vị trí định dạng để xem trộm hoặc ghi đè Stack. | Viết trực tiếp: `printf(user_input);` | Luôn chỉ định rõ ký tự định dạng: `printf("%s", user_input);`. |

- **주의/함정 (Bẫy đề thi):**
  - **Khắc phục SQL Injection:** Đề thi hỏi phương án khắc phục triệt để SQL Injection -> Đáp án đúng bắt buộc là **`PreparedStatement` (또는 매개변수화된 쿼리 - Parameterized Query)**, chọn nối chuỗi hoặc mã hóa mật khẩu là sai.
  - **5 yếu tố Batch Program:** Đề thi thường đưa vào các từ lạ như "Tính tương tác (상호작용성)" hoặc "Giao diện người dùng (UI)" -> Đây là các phương án SAI; chương trình Batch **hoàn toàn chạy tự động ngầm, không có tương tác người dùng**.
  - **Phân biệt Web Server vs WAS:** Nginx và Apache HTTP Server là Web Server (không chạy được code Java JSP/Servlet trực tiếp); Tomcat và WebLogic là WAS.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Web Server tĩnh, WAS động; 대자견안성 5 chuẩn mực Batch; Buffer Overflow sửa bằng strncpy, SQL Injection chặn đứng bằng PreparedStatement; DBCP tái dùng kết nối."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ kiến trúc phân tầng kết hợp Web Server và WAS:
```text
[ Client Trình duyệt ]
        |
        v HTTP Request (Port 80 / 443)
+-------------------------------------------------------+
| Web Server (Nginx / Apache HTTP Server)               |
|  - Phục vụ trực tiếp tài nguyên tĩnh: HTML, CSS, PNG  |
|  - Cân bằng tải (Load Balancing) & SSL Termination    |
+-------------------------------------------------------+
        | Chuyển tiếp Request động (Reverse Proxy)
        v
+-------------------------------------------------------+
| WAS (Apache Tomcat / WebLogic / Jeus)                 |
|  - Chạy Servlet / JSP / Spring Boot Business Logic     |
|  - Quản lý Transaction, Session người dùng            |
+-------------------------------------------------------+
        | Mượn kết nối từ Database Connection Pool (DBCP)
        v
+-------------------------------------------------------+
| Database Server (Oracle / MySQL / PostgreSQL)         |
+-------------------------------------------------------+
```

#### 2. Sơ đồ cơ chế hoạt động của Database Connection Pool (DBCP):
```text
Khởi động hệ thống:
DBCP tạo sẵn 10 kết nối TCP đến CSDL và giữ ở trạng thái rảnh rỗi (Idle).

Khi có Request từ người dùng:
1. Luồng ứng dụng yêu cầu kết nối: DataSource.getConnection()
   -> DBCP cấp phát ngay 1 kết nối Idle (không tốn thời gian 3-way handshake và xác thực DB).
2. Thực thi câu lệnh SQL an toàn qua PreparedStatement.
3. Khi gọi connection.close():
   -> Kết nối KHÔNG bị ngắt vật lý, mà được trả về hồ bơi ở trạng thái Idle để luồng khác dùng lại.
```

#### 3. Minh họa phòng chống lỗ hổng bảo mật tràn bộ đệm trong C:
```c
#include <stdio.h>
#include <string.h>

void vulnerable_function(char *str) {
    char buffer[10];
    // LỖ HỔNG NGUY HIỂM: strcpy không kiểm tra độ dài, nếu str dài hơn 10 ký tự sẽ tràn Stack!
    // strcpy(buffer, str);

    // GIẢI PHÁP AN TOÀN: Dùng strncpy chỉ copy tối đa kích thước đệm trừ 1 byte cho ký tự \0
    strncpy(buffer, str, sizeof(buffer) - 1);
    buffer[sizeof(buffer) - 1] = '\0'; // Đảm bảo luôn có ký tự kết thúc null

    printf("Buffer an toan: %s\n", buffer);
}

int main() {
    char malicious_input[] = "ChuoiKyTuNayQuaDaiSoVoiBoDem10Bytes";
    vulnerable_function(malicious_input);
    return 0;
}
```

#### 4. Minh họa phòng chống SQL Injection bằng `PreparedStatement` trong Java:
```java
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class SecurityDemo {
    public static void secureLogin(Connection conn, String username, String password) throws Exception {
        // LỖ HỔNG NGUY HIỂM (Nối chuỗi SQL):
        // String sql = "SELECT * FROM users WHERE user='" + username + "' AND pass='" + password + "'";
        // Nếu username nhập: admin' -- thì toàn bộ mật khẩu bị vô hiệu hóa!

        // GIẢI PHÁP AN TOÀN: Sử dụng dấu hỏi chấm (?) và PreparedStatement
        String safeSql = "SELECT * FROM users WHERE user = ? AND pass = ?";
        PreparedStatement pstmt = conn.prepareStatement(safeSql);

        // Nạp tham số an toàn (Parameter Binding): Trình điều khiển CSDL tự động thoát mọi ký tự nguy hiểm
        pstmt.setString(1, username);
        pstmt.setString(2, password);

        ResultSet rs = pstmt.executeQuery();
        if (rs.next()) {
            System.out.println("Dang nhap thanh cong an toan!");
        }
    }
}
```

---

### 복습 체크리스트
- [ ] Phân biệt được: Web Server xử lý nội dung tĩnh (Apache, Nginx), WAS xử lý logic nghiệp vụ động và DB (Tomcat, WebLogic).
- [ ] Thuộc lòng 5 yếu tố cốt lõi của Batch: **대자견안성** (대용량, 자동화, 견고성, 안정성, 성능).
- [ ] Phân biệt 3 kiểu thực thi Batch: 정기 배치 (Scheduled), 이벤트 배치 (Event-driven), On-demand 배치.
- [ ] Hiểu rõ lợi ích của DBCP: Tái sử dụng kết nối mở sẵn, tránh chi phí thiết lập kết nối liên tục.
- [ ] Nắm chắc giải pháp chống Buffer Overflow: Dùng hàm có giới hạn độ dài `strncpy`, `fgets`.
- [ ] Nắm chắc giải pháp chống SQL Injection: Bắt buộc dùng `PreparedStatement` (Parameterized Query).
- [ ] Hiểu rõ Dangling Pointer: Gán con trỏ bằng `NULL` ngay sau khi giải phóng bằng `free()`.
- [ ] Phân biệt được: JDBC (Java chuẩn), ODBC (Microsoft đa ngôn ngữ).
