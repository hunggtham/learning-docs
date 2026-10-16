# 예외 처리, 라이브러리 및 가비지 컬렉터 (Xử lý ngoại lệ, Thư viện & GC)

## 학습 목표 (Mục tiêu)
- Nắm vững cơ chế xử lý ngoại lệ (예외 처리 - Exception Handling) với cấu trúc `try - catch - finally`; thấu hiểu nguyên lý thực thi bắt buộc của khối `finally` ngay cả khi có lệnh `return`.
- Phân biệt sự khác nhau giữa Liên kết tĩnh (정적 링킹 - Static Linking) và Liên kết động (동적 링킹 - Dynamic Linking) trong việc sử dụng thư viện phần mềm.
- Thấu hiểu cơ chế quản lý bộ nhớ tự động của Trình thu gom rác (가비지 컬렉터 - Garbage Collector / GC) trong JVM: thuật toán Mark-and-Sweep, hiện tượng Stop-The-World (STW), phân chia thế hệ Young/Old Generation và cách ngăn ngừa rò rỉ bộ nhớ (Memory Leak).

## 핵심 키워드 (Từ khóa)
- 예외 처리 (Exception Handling) — `try`, `catch`, `finally`, `throw`, `throws`.
- finally 블록 (Mandatory Finally Block) — Khối lệnh luôn được thực thi bất chấp ngoại lệ hay lệnh `return`.
- 정적 링킹 vs 동적 링킹 (Static Linking vs Dynamic Linking) — Nhúng mã trực tiếp (`.lib`) vs Chia sẻ thư viện khi chạy (`.dll`, `.so`).
- 가비지 컬렉터 (Garbage Collector - GC) — Tự động thu hồi ô nhớ Heap của đối tượng mất tham chiếu (Unreachable).
- Stop-The-World (STW) — Tạm dừng toàn bộ các luồng ứng dụng để thực hiện dọn dẹp rác bộ nhớ.
- 세대별 GC (Generational GC) — Young Generation (Eden, Survivor - Minor GC) & Old Generation (Major/Full GC).

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ các đối tượng được cấp phát trên bộ nhớ Heap bằng từ khóa `new` trong bài `08-lap-trinh-huong-doi-tuong-java-oop.md`.
- **Đang giải quyết gì (Current Problem):** Giải quyết hai vấn đề sống còn trong vận hành ứng dụng: Làm sao để chương trình không bị sập đột ngột khi gặp dữ liệu lỗi bất thường (Exception), và làm sao bộ nhớ không bị cạn kiệt sau thời gian dài chạy liên tục (Memory Leak).
- **Dùng đi đâu (Forward Handoff):** Cơ chế quản lý bộ nhớ Heap của ngôn ngữ lập trình là bức tranh thu nhỏ của cơ chế quản lý bộ nhớ vật lý và bộ nhớ ảo của Hệ điều hành trong bài `14-quan-ly-bo-nho-thuc-va-chien-luoc-cap-phat.md` và `15-bo-nho-ao-thuat-toan-thay-the-trang-va-thrashing.md`.

## 읽는 방법 (Cách đọc)
- **Khối `finally`:** Cứ thấy khối `finally` là chắc chắn mọi câu lệnh bên trong nó **bắt buộc phải được chạy**, bất kể trong `try` hay `catch` có lệnh thoát `return`.
- **Static vs Dynamic Linking:**
  - Static: Gói hết vào một cục file chạy `.exe` $\rightarrow$ Nặng, chạy độc lập không cần file ngoài.
  - Dynamic: Để thư viện ở file ngoài (`.dll`, `.so`) $\rightarrow$ File `.exe` nhẹ, nhiều tiến trình dùng chung 1 bản sao trên RAM.
- **Garbage Collector:** Nhớ từ khóa **Stop-The-World (STW)** và **Young Gen (Minor GC)** vs **Old Gen (Major/Full GC)**.

---

## 예외 처리, 라이브러리 및 가비지 컬렉터

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `try-catch-finally 구문에서 finally 블록은 예외 발생 여부 및 return문 실행과 관계없이 반드시 실행된다. 가비지 컬렉터(GC)는 유효한 참조가 없는 힙(Heap) 메모리 객체를 자동 회수하여 메모리 누수를 방지하며, STW(Stop-The-World) 현상이 수반된다.`
  - [Tiếng Việt]: Trong cấu trúc try-catch-finally, khối finally luôn luôn bắt buộc phải thực thi bất kể có ngoại lệ hay có lệnh return. Garbage Collector (GC) tự động thu hồi các đối tượng trên bộ nhớ Heap không còn tham chiếu hợp lệ để chống rò rỉ bộ nhớ, đi kèm hiện tượng tạm dừng ứng dụng Stop-The-World.

- **1. Bảng các từ khóa xử lý ngoại lệ trong Java (예외 처리 키워드):**

| Từ khóa | Bản chất chức năng | Điểm thi cần lưu ý |
| :--- | :--- | :--- |
| **`try`** | Bọc khối lệnh có nguy cơ phát sinh ngoại lệ (lỗi thời gian chạy). | Bắt buộc phải đi kèm với ít nhất một khối `catch` hoặc một khối `finally`. |
| **`catch`** | Bắt và xử lý ngoại lệ cụ thể khi nó phát sinh bên trong `try`. | Khối `catch` con phải đặt trước `catch` cha (ví dụ `ArithmeticException` trước `Exception`). |
| **`finally`**| **Khối dọn dẹp tài nguyên bắt buộc phải chạy.** | Luôn chạy dù có lỗi hay không; thường dùng đóng file, đóng kết nối CSDL. |
| **`throw`** | Chủ động ném ra một đối tượng ngoại lệ cụ thể: `throw new Exception();`. | Dùng bên trong thân hàm khi phát hiện vi phạm quy tắc nghiệp vụ. |
| **`throws`**| Khai báo các ngoại lệ mà hàm có thể ném ra: `void readFile() throws IOException`. | Đặt ở chữ ký hàm (Method Signature) để cảnh báo nơi gọi phải xử lý. |

- **2. Bảng đối chiếu: Liên kết tĩnh vs Liên kết động (정적 링킹 vs 동적 링킹):**

| Tiêu chuẩn so sánh | Liên kết tĩnh (Static Linking) | Liên kết động (Dynamic Linking) |
| :--- | :--- | :--- |
| **Thời điểm liên kết** | **Khi biên dịch / Tạo tệp thực thi (Build-time)**.| **Khi chương trình đang chạy (Runtime)**. |
| **Đuôi tệp thư viện** | `.lib` (Windows), `.a` (Linux / UNIX). | `.dll` (Windows), `.so` (Linux / UNIX). |
| **Dung lượng file `.exe`** | **Rất lớn** do sao chép toàn bộ mã nhúng vào trong. | **Rất nhỏ**, chỉ chứa bảng tham chiếu địa chỉ. |
| **Bộ nhớ RAM sử dụng** | Tốn RAM vì mỗi tiến trình nạp một bản sao riêng. | **Tiết kiệm RAM**, nhiều tiến trình dùng chung 1 bản thư viện. |
| **Khả năng nâng cấp** | Khi thư viện sửa đổi, **phải biên dịch lại toàn bộ**. | Chỉ cần thay file `.dll` mới, không cần build lại mã nguồn. |

- **3. Bảng cơ chế Trình thu gom rác bộ nhớ (Garbage Collector - GC):**

| Tiêu chuẩn | Nội dung kỹ thuật cốt lõi chuẩn khảo thí HRDK |
| :--- | :--- |
| **Vùng nhớ quản lý** | Chỉ quản lý và dọn dẹp vùng nhớ **Heap** (nơi lưu các đối tượng tạo bằng `new`). |
| **Đối tượng bị thu hồi** | **Unreachable Objects:** Các đối tượng không còn bất kỳ biến tham chiếu nào trỏ tới. |
| **Mục đích tối cao** | **메모리 누수 방지 (Ngăn chặn hiện tượng rò rỉ bộ nhớ - Memory Leak)**. |
| **Hiện tượng STW** | **Stop-The-World:** JVM tạm dừng toàn bộ luồng công việc để tiến hành quét và dọn rác. |
| **Thuật toán Mark-Sweep**| 1. **Mark:** Đánh dấu đối tượng còn sống từ GC Roots $\rightarrow$ 2. **Sweep:** Xóa đối tượng chết $\rightarrow$ 3. **Compact:** Dồn nén bộ nhớ. |
| **Young Generation** | Chứa đối tượng mới tạo (Eden, Survivor). Quá trình dọn dẹp gọi là **Minor GC** (rất nhanh). |
| **Old Generation** | Chứa đối tượng sống sót qua nhiều đợt Minor GC. Dọn dẹp gọi là **Major / Full GC** (tốn thời gian). |

- **주의/함정 (Bẫy đề thi):**
  - **Lệnh `System.gc()`:** Trong Java, gọi `System.gc()` chỉ mang tính chất **gửi yêu cầu gợi ý** cho JVM chứ không đảm bảo GC sẽ được kích hoạt ngay lập tức.
  - **Lệnh `return` trong `try`:** Nếu trong `try` có câu lệnh `return 1;`, khối `finally` vẫn được thực thi trước khi giá trị 1 thực sự được trả về cho hàm gọi.
  - **Thứ tự khối `catch`:** Nếu đặt `catch (Exception e)` lên trước `catch (ArithmeticException e)`, trình biên dịch sẽ báo lỗi cú pháp "Unreachable catch block".

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Finally luôn chạy dù return hay lỗi; GC dọn rác Heap chặn đứng Memory Leak; Young làm Minor còn Old làm Major."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Lần vết luồng thực thi khối `try-catch-finally` có chứa `return`:
```java
public class ExceptionTraceDemo {
    public static int testException() {
        try {
            System.out.println("1. Vao khoi try");
            int result = 10 / 0; // Phat sinh ArithmeticException: chia cho 0
            System.out.println("2. Dong nay khong bao gio chay");
            return result;
        } catch (ArithmeticException e) {
            System.out.println("3. Vao khoi catch xu ly loi chia cho 0");
            return 100; // Gap lenh return tai day!
        } finally {
            // BẪY THI: Du khoi catch da gap return 100, finally BAT BUOC PHAI CHAY truoc!
            System.out.println("4. Vao khoi finally bat buoc");
        }
    }

    public static void main(String[] args) {
        int val = testException();
        System.out.println("5. Gia tri nhan duoc: " + val);
    }
}
```

*Thứ tự in ra màn hình:*
1. `1. Vao khoi try`
2. `3. Vao khoi catch xu ly loi chia cho 0`
3. `4. Vao khoi finally bat buoc`
4. `5. Gia tri nhan duoc: 100`

#### 2. Minh họa các hàm thư viện chuẩn C thường gặp trong đề thi:
```c
#include <stdio.h>
#include <stdlib.h> // Chua atoi, abs, malloc, free
#include <math.h>   // Chua pow, sqrt

int main() {
    // 1. Chuyen chuoi thanh so nguyen: atoi (ASCII to Integer)
    char str[] = "2026";
    int year = atoi(str);
    printf("Nam sau khi atoi: %d\n", year + 1); // In ra: 2027

    // 2. Gia tri tuyet doi: abs
    printf("abs(-15) = %d\n", abs(-15)); // In ra: 15

    // 3. Tinh luy thua va can bac hai
    printf("2^3 = %.0f\n", pow(2, 3));   // In ra: 8
    printf("sqrt(16) = %.0f\n", sqrt(16)); // In ra: 4

    return 0;
}
```

#### 3. Sơ đồ chu kỳ sống đối tượng trong bộ nhớ Heap của JVM:
$$\text{Đối tượng mới tạo} \xrightarrow{\text{Cấp phát}} \mathbf{Eden} \xrightarrow{\text{Minor GC sống sót}} \mathbf{Survivor (S0/S1)} \xrightarrow{\text{Đạt ngưỡng tuổi (Tenuring)}} \mathbf{Old Generation}$$

- Khi vùng Eden đầy: Kích hoạt **Minor GC** chuyển đối tượng còn sống sang khoang Survivor và dọn sạch Eden.
- Khi Old Generation đầy: Kích hoạt **Major GC (Full GC)** với thời gian tạm dừng STW dài hơn đáng kể.

---

### 복습 체크리스트
- [ ] Ghi nhớ bản chất `finally`: Luôn luôn chạy bất chấp có phát sinh ngoại lệ hay có lệnh `return`.
- [ ] Phân biệt được: `throw` dùng để ném ngoại lệ trong thân hàm, `throws` dùng khai báo ở chữ ký hàm.
- [ ] Nắm chắc khác biệt: Static Linking nhúng mã trực tiếp (file to), Dynamic Linking liên kết file `.dll`/`.so` khi chạy (file nhỏ, tiết kiệm RAM).
- [ ] Hiểu rõ Garbage Collector: Chỉ dọn dẹp vùng Heap của các đối tượng không còn tham chiếu (Unreachable).
- [ ] Nắm được mục đích của GC: Ngăn chặn triệt để hiện tượng rò rỉ bộ nhớ (Memory Leak).
- [ ] Phân biệt được 2 cấp độ: Minor GC dọn Young Generation, Major/Full GC dọn Old Generation.
