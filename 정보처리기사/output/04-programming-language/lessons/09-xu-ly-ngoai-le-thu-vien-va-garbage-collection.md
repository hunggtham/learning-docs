# 예외 처리, 라이브러리 및 가비지 컬렉터 (Xử lý ngoại lệ, Thư viện & GC)

## 학습 목표 (Mục tiêu)
- Nắm vững cơ chế xử lý ngoại lệ (예외 처리 - Exception Handling) với cấu trúc `try - catch - finally`; thấu hiểu nguyên lý thực thi bắt buộc của khối `finally` và thứ tự thực thi khi có lệnh `return` ở các khối.
- Phân biệt rạch ròi hai phân loại ngoại lệ kinh điển trong Java: Ngoại lệ kiểm tra (Checked Exception - bắt buộc xử lý tại compile-time) và Ngoại lệ không kiểm tra (Unchecked Exception / RuntimeException).
- Phân biệt sự khác nhau giữa Liên kết tĩnh (정적 링킹 - Static Linking) và Liên kết động (동적 링킹 - Dynamic Linking) trong việc sử dụng thư viện phần mềm.
- Thấu hiểu toàn diện 3 thuật toán và cơ chế Trình thu gom rác (가비지 컬렉터 - Garbage Collector / GC): Reference Counting (vấn đề tham chiếu tròn), Mark-and-Sweep, và Generational GC (Young/Old Generation, Minor vs Major GC).

## 핵심 키워드 (Từ khóa)
- 예외 처리 (Exception Handling) — `try`, `catch`, `finally`, `throw`, `throws`.
- Checked vs Unchecked Exception — Ngoại lệ bắt buộc xử lý khi biên dịch (`IOException`) vs Ngoại lệ runtime (`NullPointerException`).
- finally 블록 (Mandatory Finally Block) — Khối lệnh luôn được thực thi bất chấp ngoại lệ hay lệnh `return`.
- 정적 링킹 vs 동적 링킹 (Static Linking vs Dynamic Linking) — Nhúng mã trực tiếp (`.lib`) vs Chia sẻ thư viện khi chạy (`.dll`, `.so`).
- 가비지 컬렉터 (Garbage Collector - GC) — Tự động thu hồi ô nhớ Heap của đối tượng mất tham chiếu (Unreachable).
- 참조 횟수 계산법 (Reference Counting) — Đếm tham chiếu và hạn chế tham chiếu vòng tròn (Circular Reference).
- 표시 및 소거 (Mark-and-Sweep) — Đánh dấu từ GC Roots và dọn dẹp các đối tượng không thể chạm tới.
- 세대별 GC (Generational GC) — Giả thuyết thế hệ yếu, phân chia Young (Eden, S0, S1 - Minor GC) và Old Generation (Major/Full GC).

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ các đối tượng được cấp phát trên bộ nhớ Heap bằng từ khóa `new` trong bài `08-lap-trinh-huong-doi-tuong-java-oop.md`.
- **Đang giải quyết gì (Current Problem):** Giải quyết hai vấn đề sống còn trong vận hành ứng dụng: Làm sao để chương trình không bị sập đột ngột khi gặp dữ liệu lỗi bất thường (Exception), và làm sao bộ nhớ không bị cạn kiệt sau thời gian dài chạy liên tục (Memory Leak).
- **Dùng đi đâu (Forward Handoff):** Cơ chế quản lý bộ nhớ Heap của ngôn ngữ lập trình là bức tranh thu nhỏ của cơ chế quản lý bộ nhớ vật lý và bộ nhớ ảo của Hệ điều hành trong bài `14-quan-ly-bo-nho-thuc-va-chien-luoc-cap-phat.md` và `15-bo-nho-ao-thuat-toan-thay-the-trang-va-thrashing.md`.

## 읽는 방법 (Cách đọc)
- **Khối `finally`:** Cứ thấy khối `finally` là chắc chắn mọi câu lệnh bên trong nó **bắt buộc phải được chạy**, bất kể trong `try` hay `catch` có lệnh thoát `return`. Nếu trong `finally` cũng có `return`, giá trị của `finally` sẽ ghi đè hoàn toàn giá trị `return` trước đó.
- **Checked vs Unchecked:**
  - Checked: Kế thừa trực tiếp từ `Exception` (trừ con cháu `RuntimeException`), trình biên dịch bắt buộc phải có `try-catch` hoặc `throws`.
  - Unchecked: Kế thừa từ `RuntimeException` (lỗi logic lập trình: chia 0, mảng vượt biên, con trỏ null), không bắt buộc phải khai báo `throws`.
- **Các thuật toán GC:**
  - Reference Counting: Đơn giản nhưng chết vì tham chiếu vòng (A trỏ B, B trỏ A, đếm không bao giờ về 0).
  - Mark-and-Sweep: Duyệt từ GC Roots, đánh dấu đối tượng sống (Mark), quét xóa đối tượng chết (Sweep).
  - Generational GC: Dựa vào "hầu hết đối tượng chết trẻ" để tách thành Young (Minor GC) và Old (Major GC).

---

## 예외 처리, 라이브러리 및 가비지 컬렉터

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `try-catch-finally 구문에서 finally 블록은 예외 발생 여부 및 return문 실행과 관계없이 반드시 실행된다. Checked Exception은 컴파일 시점에 처리를 강제하고, Unchecked Exception(RuntimeException)은 강제하지 않는다. 가비지 컬렉터(GC) 알고리즘에는 참조 횟수(순환 참조 한계), Mark-and-Sweep, 세대별 GC(Young-Minor GC / Old-Major GC)가 있다.`
  - [Tiếng Việt]: Trong cấu trúc try-catch-finally, khối finally luôn luôn bắt buộc phải thực thi bất kể có ngoại lệ hay có lệnh return. Checked Exception bắt buộc xử lý ở thời điểm biên dịch, còn Unchecked Exception (RuntimeException) thì không. Các thuật toán GC gồm: Reference Counting (gặp hạn chế tham chiếu vòng tròn), Mark-and-Sweep, và Generational GC (Young - Minor GC / Old - Major GC).

- **1. Bảng đối chiếu Checked Exception vs Unchecked Exception:**

| Tiêu chuẩn so sánh | Checked Exception (체크 예외) | Unchecked Exception (언체크 예외) |
| :--- | :--- | :--- |
| **Lớp cha kế thừa** | Kế thừa từ `java.lang.Exception` (trừ nhóm `RuntimeException`). | Kế thừa từ `java.lang.RuntimeException` (và `Error`). |
| **Thời điểm kiểm tra** | **Thời điểm biên dịch (Compile-time)**. | **Thời điểm thực thi (Runtime)**. |
| **Bắt buộc xử lý?** | **BẮT BUỘC:** Phải bọc trong `try-catch` hoặc khai báo `throws`. | **KHÔNG BẮT BUỘC:** Lập trình viên tự quyết định xử lý hay không. |
| **Nguyên nhân phát sinh**| Do yếu tố môi trường bên ngoài: File không tồn tại, lỗi mạng, lỗi SQL. | Do lỗi tư duy hoặc logic lập trình viên viết sai. |
| **Ví dụ đại diện** | `IOException`, `SQLException`, `ClassNotFoundException`, `FileNotFoundException`.| `NullPointerException`, `ArithmeticException`, `ArrayIndexOutOfBoundsException`. |

- **2. Bảng 3 thuật toán Garbage Collection cốt lõi:**

| Thuật toán GC | Bản chất cơ chế hoạt động | Ưu điểm kỹ thuật | Nhược điểm chí mạng (Bẫy thi) |
| :--- | :--- | :--- | :--- |
| **참조 횟수 계산 (Reference Counting)** | Mỗi đối tượng có một bộ đếm số biến trỏ tới nó. Tăng khi thêm tham chiếu, giảm khi hủy; bằng 0 thì giải phóng. | Thu hồi tức thì ngay khi đối tượng hết dùng, cài đặt đơn giản. | **Bất lực trước tham chiếu vòng tròn (Circular Reference):** Đối tượng tự trỏ nhau không bao giờ về 0. |
| **표시 및 소거 (Mark-and-Sweep)** | Xuất phát từ gốc (**GC Roots**), duyệt theo đồ thị đánh dấu (Mark) đối tượng đến được; sau đó quét dọn (Sweep) đối tượng không được đánh dấu. | Giải quyết triệt để vấn đề tham chiếu vòng tròn. | Gây ngưng trệ ứng dụng (**STW - Stop-The-World**) và gây **phân mảnh bộ nhớ** (cần thêm bước Compact). |
| **세대별 가비지 컬렉션 (Generational GC)** | Dựa trên giả thuyết thế hệ yếu (Weak Generational Hypothesis): Chia bộ nhớ thành **Young Generation** (Eden, S0, S1) và **Old Generation**. | Tối ưu hóa hiệu năng cực cao: phần lớn đối tượng được dọn siêu tốc ở Young Gen qua **Minor GC**. | Khi Old Gen đầy sẽ kích hoạt **Major GC (Full GC)** với thời gian STW kéo dài. |

- **3. Bảng đối chiếu: Liên kết tĩnh vs Liên kết động (정적 링킹 vs 동적 링킹):**

| Tiêu chuẩn so sánh | Liên kết tĩnh (Static Linking) | Liên kết động (Dynamic Linking) |
| :--- | :--- | :--- |
| **Thời điểm liên kết** | **Khi biên dịch / Tạo tệp thực thi (Build-time)**.| **Khi chương trình đang chạy (Runtime)**. |
| **Đuôi tệp thư viện** | `.lib` (Windows), `.a` (Linux / UNIX). | `.dll` (Windows), `.so` (Linux / UNIX). |
| **Dung lượng file `.exe`** | **Rất lớn** do sao chép toàn bộ mã nhúng vào trong. | **Rất nhỏ**, chỉ chứa bảng tham chiếu địa chỉ. |
| **Bộ nhớ RAM sử dụng** | Tốn RAM vì mỗi tiến trình nạp một bản sao riêng. | **Tiết kiệm RAM**, nhiều tiến trình dùng chung 1 bản thư viện. |
| **Khả năng nâng cấp** | Khi thư viện sửa đổi, **phải biên dịch lại toàn bộ**. | Chỉ cần thay file `.dll` mới, không cần build lại mã nguồn. |

- **주의/함정 (Bẫy đề thi):**
  - **Lệnh `return` trong `finally`:** Nếu trong `try` return 10, trong `catch` return 20, nhưng trong `finally` có `return 30;` -> Kết quả trả về cuối cùng chắc chắn là **`30`** (giá trị trong finally ghi đè tất cả).
  - **Thứ tự khối `catch`:** Khối bắt ngoại lệ chuyên biệt (lớp con như `ArithmeticException`) bắt buộc phải đứng trước khối bắt tổng quát (lớp cha như `Exception`). Nếu đảo ngược sẽ bị lỗi biên dịch.
  - **Tham chiếu vòng trong Reference Counting:** Hai đối tượng $A$ và $B$ nắm giữ con trỏ trỏ lẫn nhau, dù không còn biến nào bên ngoài trỏ tới thì số đếm vẫn bằng 1 -> Gây ra hiện tượng rò rỉ bộ nhớ (Memory Leak) nếu dùng thuật toán Reference Counting.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Finally ghi đè return; Checked bắt buộc try-catch lúc build; Reference Counting chết vì xoay vòng, Generational chia Young dọn nhanh Old dọn kỹ."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Lần vết luồng thực thi khối `try-catch-finally` khi có lệnh `return`:
```java
public class FinallyReturnDemo {
    public static int testException() {
        try {
            System.out.println("1. Vao khoi try");
            int result = 10 / 0; // Phat sinh ArithmeticException: chia cho 0
            return result;
        } catch (ArithmeticException e) {
            System.out.println("2. Vao khoi catch");
            return 100; // Gia tri du kien tra ve: 100
        } finally {
            System.out.println("3. Vao khoi finally bat buoc");
            return 999; // BẪY THI: return trong finally ghi de hoan toan gia tri 100 cua catch!
        }
    }

    public static void main(String[] args) {
        int val = testException();
        System.out.println("4. Gia tri thuc te nhan duoc: " + val); // In ra: 999!
    }
}
```

*Thứ tự in ra màn hình:*
1. `1. Vao khoi try`
2. `2. Vao khoi catch`
3. `3. Vao khoi finally bat buoc`
4. `4. Gia tri thuc te nhan duoc: 999`

#### 2. Sơ đồ minh họa vấn đề tham chiếu vòng tròn (Circular Reference):
```text
Biến tham chiếu cục bộ trong hàm:
[ con_tro_A ] ----> Đối tượng A (Reference count = 1)
                      ^         |
                      |         | A.ref = B (Reference count = 2)
                      |         v
[ con_tro_B ] ----> Đối tượng B (Reference count = 2)
                      |         ^
                      +---------+ B.ref = A

Khi hàm kết thúc, con_tro_A và con_tro_B trên Stack bị hủy:
                   Đối tượng A (Reference count = 1)
                      ^         |
                      |         |
                      v         v
                   Đối tượng B (Reference count = 1)

KẾT QUẢ: Không ai bên ngoài chạm tới được A và B, nhưng bộ đếm không bao giờ
trở về 0 -> Reference Counting KHÔNG THỂ giải phóng 2 đối tượng này!
```

#### 3. Sơ đồ chu kỳ sống đối tượng trong bộ nhớ Heap của JVM (Generational GC):
```text
+------------------------------------+--------------------------+
|          Young Generation          |      Old Generation      |
| +------------+-------------------+ | +----------------------+ |
| |    Eden    | Survivor (S0, S1) | | |                      | |
| | (Mới tạo)  |   (Sống sót)      | | | (Tồn tại lâu năm)    | |
| +------------+-------------------+ | +----------------------+ |
+------------------------------------+--------------------------+
   | (Eden đầy)          | (Đạt max age)
   v                     v
[ Minor GC: Nhanh ]   [ Major / Full GC: Dừng toàn bộ (STW) ]
```

---

### 복습 체크리스트
- [ ] Ghi nhớ bản chất `finally`: Luôn luôn chạy bất chấp có phát sinh ngoại lệ hay có lệnh `return`.
- [ ] Nhớ nếu `finally` chứa lệnh `return`, nó sẽ ghi đè hoàn toàn giá trị trả về của `try` hoặc `catch`.
- [ ] Phân biệt Checked Exception (buộc try-catch khi compile: `IOException`) và Unchecked Exception (runtime: `NullPointerException`).
- [ ] Hiểu rõ điểm yếu chí mạng của Reference Counting: Bất lực trước tham chiếu vòng (Circular Reference).
- [ ] Nắm vững 3 bước của Mark-and-Sweep: Đánh dấu (Mark), Quét dọn (Sweep), Dồn nén (Compact).
- [ ] Phân biệt được 2 cấp độ: Minor GC dọn Young Generation (Eden/Survivor), Major/Full GC dọn Old Generation.
- [ ] Nhớ hiện tượng Stop-The-World (STW): JVM tạm dừng toàn bộ tiến trình để dọn rác bộ nhớ.
