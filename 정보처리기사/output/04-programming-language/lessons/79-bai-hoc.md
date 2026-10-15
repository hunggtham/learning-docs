# 250. JAVA에서의 표준 출력 (Standard Output in JAVA)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp, nguyên lý hoạt động và sự khác biệt giữa 3 phương thức xuất dữ liệu chuẩn trong Java: `System.out.print()`, `System.out.println()`, và `System.out.printf()`.
- Hiểu sâu sắc cơ chế chuyển đổi kiểu dữ liệu tự động của toán tử cộng (`+`) khi kết hợp giữa chuỗi ký tự (`String`) và các giá trị số học nguyên thủy.
- Phân tích chính xác thứ tự lượng giá biểu thức từ trái sang phải để không bị rơi vào bẫy nối chuỗi trong các câu hỏi tính toán kết quả in ra màn hình.

## 핵심 키워드 (Từ khóa)
- 표준 출력 (Standard Output)
- `System.out.print()` (줄바꿈 없음 / No Newline)
- `System.out.println()` (자동 개행 / With Newline)
- `System.out.printf()` (서식 지정자 / Formatted Output)
- 문자열 연결 연산자 (`+` String Concatenation)
- 좌측 결합 법칙 (Left-to-Right Associativity)
- 형변환 우선순위 (Type Promotion & Conversion)

## 선행·연결 개념 (Kiến thức liên kết)
- [78-bai-hoc.md](78-bai-hoc.md): Trình thu gom rác tự động Garbage Collector trong Java JVM.
- [80-bai-hoc.md](80-bai-hoc.md): Câu lệnh điều khiển rẽ nhánh `if` đơn giản.
- [13-bai-hoc.md](13-bai-hoc.md): Cơ chế xuất nhập dữ liệu cơ bản trong C và Java.

## 읽는 방법 (Cách đọc)
- Trong các câu hỏi thực hành Java của đề thi:
  - Phân biệt nhanh: `print` không xuống dòng, `println` tự động xuống dòng sau khi in xong nội dung.
  - Cực kỳ cảnh giác với toán tử `+`:
    - Nếu chuỗi `String` đứng trước: `"Tổng: " + 3 + 5` $\rightarrow$ Kết quả in ra là **`Tổng: 35`** (vì chuỗi ghép với `3` thành `"Tổng: 3"`, sau đó ghép tiếp với `5` thành `"Tổng: 35"`).
    - Nếu phép tính số đứng trước: `3 + 5 + " là tổng"` $\rightarrow$ Kết quả in ra là **`8 là tổng`** (vì $3+5=8$ tính số học trước, sau đó số `8` mới ghép chuỗi).
    - Nếu có ngoặc tròn: `"Tổng: " + (3 + 5)` $\rightarrow$ Kết quả in ra là **`Tổng: 8`**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu 3 phương thức xuất dữ liệu trong Java:**

| Phương thức xuất | Cú pháp áp dụng | Hành vi xuống dòng (Newline) | Trường hợp sử dụng điển hình |
| :--- | :--- | :---: | :--- |
| **`System.out.print()`** | `System.out.print(giá_trị);` | **Không xuống dòng** | In nhiều dữ liệu liên tục trên cùng một dòng (ví dụ in các phần tử của mảng cạnh nhau). |
| **`System.out.println()`** | `System.out.println(giá_trị);` | **Tự động xuống dòng** sau khi in xong | In dòng hoàn chỉnh; nếu gọi `System.out.println()` không tham số sẽ tương đương in một dòng trống. |
| **`System.out.printf()`** | `System.out.printf("format", args...);` | **Không tự động xuống dòng** (phải tự ghi `%n` hoặc `\n`) | Định dạng số thực làm tròn (`%.2f`), số nguyên canh lề (`%4d`), xuất ký tự hoặc chuỗi có định dạng. |

- **2. Bẫy toán tử nối chuỗi `+` và thứ tự ưu tiên:**

```java
public class OutputDemo {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;

        // Trường hợp 1: Chuỗi đứng đầu -> Toàn bộ biểu thức chuyển thành nối chuỗi
        System.out.println("Result: " + a + b);     // In ra: Result: 1020

        // Trường hợp 2: Biểu thức số học đứng đầu -> Tính cộng số học trước
        System.out.println(a + b + " is sum");       // In ra: 30 is sum

        // Trường hợp 3: Có ngoặc tròn bảo vệ -> Ngoặc tính trước
        System.out.println("Result: " + (a + b));   // In ra: Result: 30

        // Trường hợp 4: Kết hợp dấu nhân (*) có độ ưu tiên cao hơn (+)
        System.out.println("Result: " + a * b);     // In ra: Result: 200 (a * b = 200 trước)
    }
}
```

- **3. Các ký tự định dạng phổ biến trong `printf` của Java:**
  - `%d`: Xuất số nguyên thập phân (Decimal Integer).
  - `%f`: Xuất số thực dấu phẩy động (Floating point).
  - `%s`: Xuất chuỗi ký tự (String).
  - `%c`: Xuất ký tự đơn (Character).
  - `%n`: Ký tự xuống dòng độc lập nền tảng (khuyên dùng trong Java thay cho `\n`).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Hiệu năng của phép nối chuỗi `+` trong vòng lặp:**
  - Vì kiểu `String` trong Java là bất biến (Immutable), mỗi lần dùng toán tử `+` để nối chuỗi bên trong vòng lặp lớn, JVM sẽ phải liên tục khởi tạo đối tượng `StringBuilder` mới và cấp phát mảng ký tự mới trên Heap.
  - Do đó trong các tác vụ ghép chuỗi vòng lặp lớn, chuẩn mực Clean Code yêu cầu sử dụng trực tiếp lớp `StringBuilder` hoặc `StringBuffer` với phương thức `.append()`.

### 복습 체크리스트
- [ ] Phân biệt rõ `print` (không xuống dòng), `println` (xuống dòng tự động), `printf` (định dạng).
- [ ] Nhớ kết quả của `"A" + 1 + 2` là `"A12"`, còn `1 + 2 + "A"` là `"3A"`.
- [ ] Nhớ toán tử nhân `*` có độ ưu tiên cao hơn `+`, nên `"A" + 2 * 3` sẽ in ra `"A6"`.
- [ ] Nắm được ký hiệu `%n` trong `printf` là mã xuống dòng tương thích đa nền tảng của Java.
