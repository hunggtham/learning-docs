# 라이브러리 및 예외 처리 (Libraries and Exception Handling)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm thư viện phần mềm và chức năng của các tệp tiêu đề thư viện chuẩn trong C (`stdio.h`, `math.h`, `string.h`, `stdlib.h`, `time.h`).
- Phân biệt cơ chế liên kết của Thư viện tĩnh (Static Library) và Thư viện liên kết động (Dynamic Link Library).
- Hiểu rõ bản chất của ngoại lệ (Exception) và luồng xử lý lỗi an toàn thông qua cấu trúc `try - catch/except - finally`.
- Nắm bắt quy tắc thực thi bắt buộc của khối `finally` trong việc dọn dẹp và giải phóng tài nguyên hệ thống.

## 핵심 키워드 (Từ khóa)
- **표준 라이브러리 (Standard Library)**: Tập hợp các hàm viết sẵn (`stdio.h`, `math.h`, `stdlib.h`).
- **정적 라이브러리 vs 동적 라이브러리**: Static Library (`.a`, `.lib` - lúc build) vs DLL (`.so`, `.dll` - lúc runtime).
- **예외 (Exception)**: Sự cố bất thường phát sinh lúc chương trình đang chạy làm gián đoạn luồng lệnh.
- **`try - catch - finally`**: Cấu trúc kiểm soát lỗi trong Java/C++; trong Python là `try - except - finally`.
- **자원 해제 (Resource Cleanup)**: Vai trò cốt lõi của khối `finally` (luôn luôn được thực thi).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [42-bai-hoc.md](42-bai-hoc.md) (Hàm thư viện chuỗi string.h).
- Liên kết với [17-bai-hoc.md](17-bai-hoc.md) (Lỗi tài nguyên và try-with-resources).
- Liên kết với [04-programming-language/70-bai-hoc.md](../../04-programming-language/lessons/70-bai-hoc.md) (Lỗ hổng bảo mật và xử lý lỗi an toàn).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh vai trò các thư viện C:
  - Cần cấp phát bộ nhớ động (`malloc`, `free`) hoặc đổi chuỗi ra số (`atoi`) $\rightarrow$ **`<stdlib.h>`**.
  - Cần tính căn bậc hai (`sqrt`) hay lũy thừa (`pow`) $\rightarrow$ **`<math.h>`**.
- Quy tắc khối `finally`: Kể cả khi khối `try` có lệnh `return` thì khối `finally` **vẫn phải được chạy** trước khi hàm kết thúc thực sự!

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Các thư viện tiêu đề chuẩn trong ngôn ngữ C
| Tên Header File | Chức năng chính | Các hàm tiêu biểu thường gặp trong đề thi |
| :--- | :--- | :--- |
| **`<stdio.h>`** | Standard Input/Output (Nhập xuất chuẩn) | `printf`, `scanf`, `gets`, `puts`, `fopen`, `fclose` |
| **`<math.h>`** | Mathematical Functions (Hàm toán học) | `sqrt` (căn bậc hai), `pow` (lũy thừa), `abs`/`fabs` (trị tuyệt đối), `ceil` (làm tròn lên), `floor` (làm tròn xuống) |
| **`<string.h>`** | String Handling (Xử lý chuỗi ký tự) | `strlen` (đo độ dài), `strcpy` (sao chép), `strcat` (nối chuỗi), `strcmp` (so sánh) |
| **`<stdlib.h>`** | Standard Utility (Tiện ích chuẩn) | `atoi` (đổi chuỗi sang int), `atof` (đổi chuỗi sang float), `malloc` / `free` (cấp phát/giải phóng bộ nhớ Heap), `rand` (sinh số ngẫu nhiên) |
| **`<time.h>`** | Date and Time (Xử lý thời gian) | `time` (lấy thời gian hiện tại), `clock` (đo thời gian CPU) |

#### 2. Phân loại Thư viện: Tĩnh vs Động
- **Thư viện tĩnh (Static Library - `.lib`, `.a`)**:
  - Toàn bộ mã nhị phân của các hàm thư viện được sao chép và nhúng trực tiếp vào tệp thực thi (`.exe`) tại **thời điểm biên dịch/liên kết (Link-time)**.
  - *Ưu điểm*: Tệp thực thi chạy độc lập, không phụ thuộc vào hệ thống bên ngoài.
  - *Nhược điểm*: Kích thước tệp chương trình phình to; khi thư viện có bản vá lỗi phải biên dịch lại toàn bộ phần mềm.
- **Thư viện liên kết động (Dynamic Link Library - DLL / `.so`, `.dll`)**:
  - Mã nhị phân của thư viện được lưu riêng biệt trên ổ đĩa và chỉ được nạp vào bộ nhớ RAM khi chương trình chạy (**Runtime**).
  - *Ưu điểm*: Tiết kiệm dung lượng bộ nhớ RAM (nhiều tiến trình dùng chung một bản nạp trên RAM); dễ dàng nâng cấp cập nhật mà không cần build lại ứng dụng.
  - *Nhược điểm*: Có thể xảy ra lỗi không tìm thấy file DLL (DLL Hell) nếu môi trường thiếu tệp phụ thuộc.

#### 3. Cơ chế Xử lý Ngoại lệ (Exception Handling)
- **Cấu trúc luồng lệnh chuẩn**:
  - **Khối `try`**: Chứa các đoạn mã nghiệp vụ tiềm ẩn rủi ro phát sinh ngoại lệ (ví dụ: mở tệp, kết nối mạng, đọc mảng, chia số).
  - **Khối `catch` (Java) / `except` (Python)**: Chứa logic xử lý khi lỗi xảy ra, ngăn không cho chương trình bị sập đột ngột (Crash).
  - **Khối `finally`**: Luôn luôn được đảm bảo thực thi 100%, kể cả khi có ngoại lệ xảy ra hay không xảy ra, và ngay cả khi có lệnh `return`. Đây là nơi bắt buộc phải đóng kết nối tệp hoặc ngắt kết nối cơ sở dữ liệu.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Luồng thực thi của khối try-catch-finally
```
               [Bắt đầu khối try]
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
   [Không có lỗi]             [Phát sinh ngoại lệ]
          │                         │
          │                         ▼
          │                [Nhảy sang khối catch]
          │                (Xử lý ghi log / khắc phục)
          │                         │
          └────────────┬────────────┘
                       ▼
             [Khối FINALLY] (BẮT BUỘC LUÔN CHẠY)
             (Đóng file, giải phóng tài nguyên)
                       │
                       ▼
             [Lệnh kế tiếp phía sau]
```

#### 2. Bài toán thi Kỹ sư xử lý thông tin về khối finally
```java
public class Test {
    public static int check() {
        try {
            int a = 10 / 2; // a = 5
            return a;       // Chuẩn bị trả về 5
        } catch (Exception e) {
            return -1;
        } finally {
            System.out.print("DONE-"); // VẪN ĐƯỢC IN RA TRƯỚC KHI RETURN!
        }
    }
    public static void main(String[] args) {
        System.out.println(check()); // In ra: DONE-5
    }
}
```

---

### 복습 체크리스트
- [ ] Hàm `atoi` và `malloc` trong ngôn ngữ C nằm trong tệp tiêu đề (header) nào?
- [ ] Thư viện liên kết động (DLL) mang lại lợi ích gì vượt trội so với Thư viện tĩnh (Static Library)?
- [ ] Trong trường hợp khối `try` thực thi câu lệnh `return`, khối `finally` có được chạy hay không?
- [ ] Từ khóa nào được dùng trong Java và Python để ném (throw) một ngoại lệ có chủ đích?
