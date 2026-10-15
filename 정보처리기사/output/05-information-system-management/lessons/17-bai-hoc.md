# 2. 자원 처리 오류 (Resource Handling Errors)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cơ chế phát sinh và các kịch bản tấn công khai thác của nhóm lỗi quản lý tài nguyên hệ thống (**자원 처리 오류 - Resource Handling Errors**).
- Phân biệt sự khác nhau giữa Giải phóng tài nguyên không thỏa đáng (**부적절한 자원 해제 - Improper Resource Release**) gây cạn kiệt tài nguyên (Resource Exhaustion) và Sử dụng tài nguyên sau giải phóng (**해제된 자원 사용 - Use After Free / UAF**).
- Hiểu các hiểm họa của con trỏ lơ lửng (허상 포인터 - Dangling Pointer), lỗi giải phóng trùng lặp (Double Free), và các giải pháp chuẩn mực để dọn dẹp tài nguyên an toàn (`try-with-resources`, gán con trỏ về `NULL`).

## 핵심 키워드 (Từ khóa)
- 자원 처리 오류 (Resource Handling Vulnerabilities)
- 부적절한 자원 해제 (Improper Resource Release / Resource Leak)
- 해제된 자원 사용 (Use-After-Free - UAF)
- 허상 포인터 (Dangling Pointer)
- 이중 해제 (Double Free Vulnerability)
- 자원 고갈 (Resource Exhaustion / DoS)
- `try-with-resources` & `AutoCloseable`
- `free()` 후 `NULL` 초기화

## 선행·연결 개념 (Kiến thức liên kết)
- [16-bai-hoc.md](16-bai-hoc.md): Lỗi mã nguồn phần mềm và lạm dụng API không an toàn.
- [18-bai-hoc.md](18-bai-hoc.md): Công nghệ hạ tầng mạng ảo hóa (SDN, SDDC, Cloud).
- [78-bai-hoc.md](78-bai-hoc.md): Trình thu gom rác tự động Garbage Collector và phòng ngừa rò rỉ bộ nhớ.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh trong các câu hỏi đề thi:
  - Khi hỏi: "Lỗi không đóng tệp tin (`close`), không ngắt kết nối cơ sở dữ liệu (`Connection`), hoặc không giải phóng bộ nhớ sau khi dùng xong dẫn đến **cạn kiệt tài nguyên hệ thống (자원 고갈)** là gì?" $\rightarrow$ Chọn ngay **부적절한 자원 해제 (Improper Resource Release)**.
  - Khi hỏi: "Lỗi chương trình vẫn tiếp tục tham chiếu, đọc ghi vào vùng nhớ **đã được giải phóng trước đó (반환된 메모리를 다시 참조)** khiến kẻ tấn công có thể thực thi mã độc là gì?" $\rightarrow$ Chọn ngay **해제된 자원 사용 (Use After Free / UAF)**.
  - Khắc phục UAF: Luôn gán con trỏ về `NULL` ngay sau khi giải phóng: `free(ptr); ptr = NULL;`.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu các lỗ hổng quản lý tài nguyên điển hình:**

| Tên lỗ hổng tài nguyên | Tên tiếng Hàn & Anh | Cơ chế phát sinh & Hậu quả an ninh | Biện pháp khắc phục chuẩn |
| :--- | :--- | :--- | :--- |
| **Giải phóng không thỏa đáng** | **부적절한 자원 해제** (Improper Resource Release) | Cấp phát tài nguyên hệ thống (Bộ nhớ Heap, File Handle, Database Connection, Socket mạng) nhưng khi gặp ngoại lệ (Exception) hoặc luồng rẽ nhánh lại thoát mà quên gọi hàm đóng/hủy. Gây rò rỉ tài nguyên (**Resource Leak**) và cạn kiệt tài nguyên hệ thống (**Resource Exhaustion**). | Luôn đưa lệnh giải phóng vào khối `finally` hoặc sử dụng cú pháp tự động đóng **`try-with-resources`** (`AutoCloseable` trong Java, `using` trong C#). |
| **Sử dụng sau khi giải phóng** | **해제된 자원 사용** (Use-After-Free / UAF) | Một khối bộ nhớ động trên Heap đã được giải phóng bằng hàm `free()`, nhưng con trỏ trỏ tới nó vẫn tồn tại và chương trình tiếp tục đọc/ghi vào đó. Kẻ tấn công có thể chiếm quyền cấp phát vùng nhớ này để ghi đè con trỏ hàm (Function Pointer), chuyển hướng luồng thực thi sang shellcode mã độc. | **Gán con trỏ về `NULL` ngay lập tức** sau khi giải phóng: `free(p); p = NULL;`. |
| **Giải phóng hai lần** | **이중 해제** (Double Free) | Gọi hàm `free()` hai lần trên cùng một địa chỉ con trỏ mà không kiểm tra. Thao tác này làm hỏng cấu trúc liên kết nội bộ của trình quản trị Heap (Heap Chunk Metadata), cho phép kẻ tấn công thực thi mã tùy ý. | Đặt biến cờ kiểm soát trạng thái và gán `p = NULL` (hàm `free(NULL)` trong chuẩn C an toàn không làm gì). |
| **Truy xuất bộ nhớ chưa khởi tạo** | **초기화되지 않은 메모리 접근** (Uninitialized Memory Access) | Khai báo biến cục bộ trên Stack hoặc cấp phát bộ nhớ bằng `malloc()` nhưng không gán giá trị khởi tạo mà sử dụng ngay; dẫn đến đọc dữ liệu rác ngẫu nhiên hoặc làm rò rỉ các thông tin nhạy cảm của tiến trình trước. | Luôn khởi tạo giá trị ban đầu rõ ràng (`int a = 0;`), dùng `calloc()` (tự động xóa về 0) hoặc gọi hàm `memset()`. |

- **2. Minh họa chuẩn mực khắc phục lỗi bằng `try-with-resources` trong Java:**

```java
// Cách viết cổ điển dễ bị lỗi rò rỉ tài nguyên nếu có exception xảy ra trước khi kịp gọi close()
// Chuẩn hiện đại an toàn: Tự động đóng tệp tin bất kể thành công hay có exception
try (FileInputStream fis = new FileInputStream("secret.txt");
     BufferedReader br = new BufferedReader(new InputStreamReader(fis))) {
    String line;
    while ((line = br.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    logger.error("Lỗi đọc tệp tin: " + e.getMessage());
}
// Tự động đóng fis và br mà không cần viết khối finally thủ công!
```

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Hiểm họa của Con trỏ lơ lửng (허상 포인터 - Dangling Pointer):**
  - Khi hai con trỏ $P_1$ và $P_2$ cùng trỏ tới một vùng nhớ đối tượng. Nếu lập trình viên gọi `free(P_1)`, vùng nhớ đó bị đánh dấu là khả dụng trên Heap. Lúc này con trỏ $P_2$ vẫn trỏ vào địa chỉ đó và biến thành một **Dangling Pointer**.
  - Nếu sau đó hệ thống cấp phát vùng nhớ này cho một đối tượng nhạy cảm khác, thao tác thông qua $P_2$ sẽ làm hỏng dữ liệu mới hoặc bị lợi dụng để thay đổi bảng phương thức ảo (vtable).

### 복습 체크리스트
- [ ] Phân biệt được: Improper Resource Release gây cạn kiệt tài nguyên (Resource Exhaustion).
- [ ] Nhớ Use-After-Free (UAF) là hành vi truy xuất lại vùng nhớ đã bị giải phóng qua con trỏ lơ lửng (Dangling Pointer).
- [ ] Ghi nhớ cách khắc phục UAF: Luôn gán con trỏ về `NULL` ngay sau khi gọi `free()`.
- [ ] Nhớ cú pháp `try-with-resources` trong Java giúp tự động đóng tệp và socket an toàn.
