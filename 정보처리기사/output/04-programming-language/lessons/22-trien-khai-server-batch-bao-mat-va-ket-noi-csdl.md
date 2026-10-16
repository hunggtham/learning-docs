# 서버 프로그램 구현: 프레임워크, 배치, 보안 취약점 및 DB 연동 (Triển khai Server: Batch, Bảo mật & DB)

## 학습 목표 (Mục tiêu)
- Nắm vững 4 đặc trưng cốt lõi của Khung phát triển ứng dụng Server (서버개발 프레임워크: Modularity, Reusability, Extensibility, IoC) và nguyên lý Đảo ngược luồng điều khiển (Inversion of Control - IoC).
- Thuộc lòng 5 yếu tố bắt buộc của Chương trình xử lý hàng loạt Batch theo khẩu quyết **대자견안성** (Đại dung lượng, Tự động hóa, Kiên cố, Ổn định, Hiệu năng).
- Nhận diện và nêu giải pháp khắc phục cho 4 lỗ hổng bảo mật mã nguồn kinh điển: Tràn bộ đệm (Buffer Overflow), Con trỏ lơ lửng (Dangling Pointer), Tấn công tiêm mã SQL (SQL Injection với `PreparedStatement`) và Chuỗi định dạng (Format String).
- Phân biệt công nghệ Web Mashup, kiến trúc hướng dịch vụ SOA và hai chuẩn kết nối cơ sở dữ liệu: JDBC (Java) vs ODBC (Microsoft), cùng vai trò của Connection Pool.

## 핵심 키워드 (Từ khóa)
- 서버개발 프레임워크 (Server Framework) — 모듈화, 재사용성, 확장성, 제어의 역전 (IoC / DI).
- 배치 프로그램 5대 요소 (Batch Program 5 Elements) — 대용량 데이터, 자동화, 견고성, 안정성, 성능 (대자견안성).
- 버퍼 오버플로 (Buffer Overflow) — Tràn bộ đệm ghi đè địa chỉ trả về (Return Address); phòng chống bằng `strncpy`.
- 허상 포인터 (Dangling Pointer) — Con trỏ trỏ tới vùng nhớ đã bị giải phóng `free()`; phòng chống bằng gán `NULL`.
- SQL 삽입 (SQL Injection) — Tấn công chèn mã SQL trái phép; phòng chống triệt để bằng `PreparedStatement`.
- DB 연동 기술 (Database Connectivity) — JDBC (Java 표준) vs ODBC (MS 주도), Connection Pool.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Bài học tổng hợp và khép lại toàn bộ chương trình Môn 4, kế thừa toàn bộ kỹ năng lập trình C/Java, bảo mật con trỏ, quản lý bộ nhớ và kết nối mạng từ bài 01 đến bài 21.
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi thực tế khi triển khai phần mềm phía máy chủ (Server-side): Làm sao để ứng dụng vận hành tự động an toàn, không bị tin tặc khai thác lỗ hổng bộ nhớ và kết nối dữ liệu hiệu năng cao.
- **Dùng đi đâu (Forward Handoff):** Kiến thức về bảo mật, kết nối DB và xử lý hàng loạt này sẽ liên kết trực tiếp với Môn 3 (Cơ sở dữ liệu) và Môn 5 (Quản lý hệ thống thông tin) để hoàn thiện toàn bộ năng lực thi đỗ chứng chỉ Kỹ sư xử lý thông tin.

## 읽는 방법 (Cách đọc)
- **Khẩu quyết Batch:** Nhớ 5 chữ vàng: **대·자·견·안·성** (대용량 Đại dung lượng $\rightarrow$ 자동화 Tự động hóa $\rightarrow$ 견고성 Kiên cố không sập $\rightarrow$ 안정성 Ổn định tin cậy $\rightarrow$ 성능 Hiệu năng).
- **Lỗ hổng bảo mật:**
  - Tràn bộ đệm (Buffer Overflow) $\rightarrow$ Cấm dùng `strcpy`, `gets`; thay bằng `strncpy`, `fgets`.
  - Con trỏ lơ lửng (Dangling Pointer) $\rightarrow$ Sau khi `free(p)`, lập tức gán `p = NULL;`.
  - SQL Injection $\rightarrow$ Dùng **`PreparedStatement`** (Parameterized Binding), cấm nối chuỗi câu lệnh SQL.
- **JDBC vs ODBC:** JDBC là của Java (Sun); ODBC là của Microsoft (đa ngôn ngữ).

---

## 서버 프로그램 구현: 프레임워크, 배치, 보안 취약점 및 DB 연동

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `배치 프로그램의 5대 필수 요소는 대용량 데이터, 자동화, 견고성, 안정성, 성능(대자견안성)이다. 버퍼 오버플로는 복귀 주소를 덮어쓰는 취약점으로 strncpy로 방지하고, SQL 삽입은 PreparedStatement로 방지한다. JDBC는 Java 전용, ODBC는 MS가 개발한 DB 접속 표준이다.`
  - [Tiếng Việt]: 5 yếu tố bắt buộc của chương trình Batch là Dữ liệu lớn, Tự động hóa, Kiên cố, Ổn định, Hiệu năng (대자견안성). Tràn bộ đệm là lỗ hổng ghi đè địa chỉ trả về được phòng chống bằng strncpy, còn SQL Injection được phòng chống bằng PreparedStatement. JDBC dành riêng cho Java, còn ODBC là chuẩn kết nối DB do Microsoft phát triển.

- **1. Bảng 5 yếu tố cốt lõi của Chương trình xử lý hàng loạt (배치 프로그램 5대 요소 - 대자견안성):**

| Yếu tố cốt lõi | Thuật ngữ Hàn / Anh | Nội dung kỹ thuật chuẩn khảo thí HRDK |
| :--- | :--- | :--- |
| **1. Dữ liệu lớn** | **대용량 데이터** (Large Data) | Có khả năng xử lý mượt mà khối lượng dữ liệu khổng lồ trong các chu kỳ định kỳ. |
| **2. Tự động hóa** | **자동화** (Automation) | Vận hành hoàn toàn tự động theo lịch trình đặt trước, **không cần người can thiệp**. |
| **3. Tính kiên cố** | **견고성** (Robustness) | Xử lý ngoại lệ chặt chẽ, **không bị sập hay gián đoạn hệ thống** khi gặp dữ liệu lỗi. |
| **4. Tính ổn định** | **안정성 / 신뢰성** (Reliability) | Đảm bảo toàn vẹn dữ liệu, có cơ chế ghi nhật ký (Logging) và khôi phục khi gặp sự cố. |
| **5. Hiệu năng** | **성능** (Performance) | Hoàn thành toàn bộ khối lượng công việc trong khoảng thời gian cửa sổ cho phép (**Batch Window**). |

- **2. Bảng nhận diện lỗ hổng bảo mật mã nguồn và biện pháp khắc phục:**

| Lỗ hổng bảo mật | Cơ chế tấn công của tin tặc | Hàm gây lỗi nguy hiểm | Biện pháp khắc phục chuẩn thi |
| :--- | :--- | :--- | :--- |
| **Tràn bộ đệm**<br>(버퍼 오버플로 - Buffer Overflow) | Ghi dữ liệu vượt quá kích thước mảng trong Stack, **ghi đè lên địa chỉ trả về (Return Address)** để chiếm quyền điều khiển CPU. | `strcpy()`, `gets()`, `scanf("%s")`, `strcat()` | Thay thế bằng các hàm có giới hạn độ dài an toàn: **`strncpy()`, `fgets()`, `snprintf()`**. |
| **Con trỏ lơ lửng**<br>(허상 포인터 - Dangling Pointer) | Vùng nhớ đã được giải phóng bằng `free()` nhưng con trỏ vẫn còn trỏ tới; nếu truy cập lại sẽ gây lỗi bộ nhớ hoặc bị khai thác. | Gọi hàm `free(ptr)` nhưng không xóa con trỏ. | **Gán ngay con trỏ về giá trị rỗng sau khi giải phóng: `ptr = NULL;`**. |
| **Tiêm mã SQL**<br>(SQL 삽입 - SQL Injection) | Chèn các chuỗi truy vấn độc hại (ví dụ `' OR '1'='1`) qua ô nhập liệu để đọc trộm hoặc xóa sạch CSDL. | Nối chuỗi SQL động: `query = "SELECT * FROM users WHERE id='" + input + "'";` | **Sử dụng đối tượng `PreparedStatement`** để truyền tham số an toàn (Parameter Binding). |
| **Chuỗi định dạng**<br>(포맷 스트링 - Format String) | Truyền trực tiếp chuỗi người dùng vào vị trí định dạng để xem trộm hoặc ghi đè Stack. | Viết trực tiếp: `printf(user_input);` | Luôn chỉ định rõ ký tự định dạng: **`printf("%s", user_input);`**. |

- **3. Bảng đối chiếu công nghệ kết nối CSDL: JDBC vs ODBC:**

| Tiêu chuẩn so sánh | Chuẩn kết nối JDBC | Chuẩn kết nối ODBC |
| :--- | :--- | :--- |
| **Hãng khởi xướng** | **Sun Microsystems** (hiện thuộc Oracle). | **Microsoft**. |
| **Ngôn ngữ hỗ trợ** | **Chuyên biệt và tối ưu riêng cho ngôn ngữ Java**. | **Hỗ trợ đa ngôn ngữ** (C, C++, VB, Python...). |
| **Thành phần điều phối**| `DriverManager` kết hợp với JDBC Driver của từng hãng DB. | `ODBC Driver Manager` của hệ điều hành. |
| **Tính khả chuyển** | Rất cao, chạy độc lập mọi nền tảng hỗ trợ máy ảo JVM. | Phụ thuộc nhiều vào cấu hình Driver trên hệ điều hành. |

- **4. Dịch vụ Web Mashup và Kiến trúc hướng dịch vụ (SOA):**
  - **Mashup (매시업):** Ứng dụng Web được tạo ra bằng cách kết hợp nội dung hoặc dịch vụ từ **nhiều nguồn Open API khác nhau** (ví dụ: lấy API bản đồ Google Maps kết hợp với API bất động sản để tạo trang web tìm nhà trọ trực quan).
  - **SOA (Service-Oriented Architecture - Kiến trúc hướng dịch vụ):** Phong cách thiết kế kiến trúc hệ thống bằng cách đóng gói các chức năng nghiệp vụ thành các **Dịch vụ (Services)** độc lập, có thể tái sử dụng và kết nối lỏng lẻo (Loose Coupling) qua mạng bằng các giao thức chuẩn (SOAP, REST).
  - **Connection Pool (Hồ bơi kết nối):** Cơ chế khởi tạo sẵn một số lượng kết nối CSDL nhất định lưu trữ trong RAM; khi tiến trình cần thao tác CSDL chỉ việc mượn kết nối có sẵn và trả lại hồ bơi sau khi xong, tránh việc mở/đóng kết nối liên tục gây nghẽn máy chủ.

- **주의/함정 (Bẫy đề thi):**
  - **Khắc phục SQL Injection:** Đề thi hỏi phương án khắc phục triệt để SQL Injection $\rightarrow$ Đáp án đúng bắt buộc là **`PreparedStatement` (또는 매개변수화된 쿼리 - Parameterized Query)**, chọn nối chuỗi hoặc mã hóa mật khẩu là sai.
  - **5 yếu tố Batch Program:** Đề thi thường đưa vào các từ lạ như "Tính tương tác (상호작용성)" hoặc "Giao diện người dùng (UI)" $\rightarrow$ Đây là các phương án SAI; chương trình Batch **hoàn toàn chạy tự động ngầm, không có tương tác người dùng**.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"대자견안성 5 chuẩn mực Batch; Buffer Overflow sửa bằng strncpy, SQL Injection chặn đứng bằng PreparedStatement; JDBC của Java, ODBC của MS."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Minh họa phòng chống lỗ hổng bảo mật tràn bộ đệm trong C:
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

#### 2. Minh họa phòng chống SQL Injection bằng `PreparedStatement` trong Java:
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

#### 3. Bảng cơ chế vận hành của Connection Pool trong ứng dụng máy chủ:
$$\begin{array}{ccc}
\mathbf{\text{Client Yêu cầu}} & \longrightarrow & \mathbf{\text{Connection Pool}} \\
\text{Yêu cầu truy vấn CSDL} & \xrightarrow{\text{Mượn kết nối}} & \text{Lấy kết nối đang rảnh rỗi (Idle)} \\
\text{Thực thi câu lệnh SQL} & & | \\
\text{Hoàn tất thao tác} & \xrightarrow{\text{Trả lại kết nối (close)}} & \text{Kết nối quay lại trạng thái Idle để dùng tiếp}
\end{array}$$
- Lợi ích vượt trội: Tiết kiệm chi phí bắt tay 3 bước của mạng và chi phí xác thực tài khoản CSDL, nâng cao năng suất xử lý (Throughput) cho hệ thống máy chủ.

---

### 복습 체크리스트
- [ ] Thuộc lòng 5 yếu tố cốt lõi của Batch: **대자견안성** (대용량, 자동화, 견고성, 안정성, 성능).
- [ ] Nhớ chương trình Batch vận hành tự động định kỳ, không có tương tác người dùng.
- [ ] Nắm chắc giải pháp chống Buffer Overflow: Dùng hàm có giới hạn độ dài `strncpy`, `fgets`.
- [ ] Nắm chắc giải pháp chống SQL Injection: Bắt buộc dùng `PreparedStatement` (Parameterized Query).
- [ ] Hiểu rõ Dangling Pointer: Gán con trỏ bằng `NULL` ngay sau khi giải phóng bằng `free()`.
- [ ] Phân biệt được: JDBC (Java chuẩn), ODBC (Microsoft đa ngôn ngữ), Connection Pool (tái sử dụng kết nối CSDL).
- [ ] Định nghĩa được Web Mashup: Kết hợp nhiều nguồn Open API để tạo ứng dụng mới.
