# 238. 가비지 콜렉터 (Garbage Collector)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, mục đích và nguyên lý vận hành tự động của trình thu gom rác bộ nhớ (가비지 컬렉터 - Garbage Collector / GC) trong các môi trường máy ảo hiện đại (Java JVM, .NET CLR).
- Phân biệt sự khác nhau giữa cơ chế quản lý bộ nhớ thủ công trong C/C++ (`malloc`/`free`) và cơ chế quản lý bộ nhớ tự động trong Java/Python.
- Thấu hiểu cơ chế phát hiện rác qua đồ thị tham chiếu (Reachability), hiện tượng tạm dừng hệ thống toàn cục (Stop-The-World), và các kỹ thuật GC kinh điển (Mark-and-Sweep, Phân chia thế hệ Generational GC).

## 핵심 키워드 (Từ khóa)
- 가비지 컬렉터 (Garbage Collector - GC)
- 힙 메모리 자동 회수 (Heap Memory Automatic Deallocation)
- 메모리 누수 방지 (Memory Leak Prevention)
- 유효하지 않은 참조 (Unreachable Objects)
- `System.gc()` (Gợi ý thu gom rác)
- Stop-The-World (STW / Tạm dừng ứng dụng)
- Mark-and-Sweep 알고리즘
- 세대별 가비지 컬렉션 (Generational GC: Young & Old Gen)

## 선행·연결 개념 (Kiến thức liên kết)
- [77-bai-hoc.md](77-bai-hoc.md): Kiểu dữ liệu cấu trúc struct và con trỏ trong C.
- [79-bai-hoc.md](79-bai-hoc.md): Xuất dữ liệu chuẩn trong Java (`print`, `println`, `printf`).
- [70-bai-hoc.md](70-bai-hoc.md): Lỗ hổng con trỏ lơ lửng Dangling Pointer và tràn bộ nhớ.

## 읽는 방법 (Cách đọc)
- Trong bài thi kỹ sư CNTT:
  - Khái niệm: GC là tiến trình nền tự động tìm kiếm các đối tượng nằm trên vùng nhớ **Heap** mà **không còn bất kỳ biến tham chiếu (Reference) nào trỏ tới**, sau đó giải phóng vùng nhớ đó trả lại cho hệ điều hành.
  - Tác dụng lớn nhất: **메모리 누수 방지 (Ngăn chặn triệt để hiện tượng rò rỉ bộ nhớ - Memory Leak)** do lập trình viên quên giải phóng.
  - Lệnh gọi trong Java: `System.gc()` chỉ mang tính chất gửi yêu cầu/gợi ý tới JVM chứ không đảm bảo GC sẽ chạy ngay tức khắc.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Đối chiếu quản lý bộ nhớ: Thủ công vs Tự động:**

| Tiêu chuẩn so sánh | Quản lý thủ công (C / C++) | Quản lý tự động (JAVA / Python / C#) |
| :--- | :--- | :--- |
| **Cấp phát bộ nhớ** | Gọi hàm `malloc()`, `calloc()` hoặc toán tử `new`. | Khởi tạo đối tượng bằng toán tử `new` (hoặc cú pháp tự nhiên trong Python). |
| **Giải phóng bộ nhớ** | **Bắt buộc lập trình viên tự gọi `free()` hoặc `delete`.** | **Trình thu gom rác (Garbage Collector) tự động làm hoàn toàn.** |
| **Nguy cơ lỗi phát sinh** | Dễ gặp **Memory Leak** (quên giải phóng) hoặc **Dangling Pointer** (giải phóng sớm nhưng vẫn truy xuất). | Tránh được hầu hết các lỗi quản lý con trỏ; lập trình viên tập trung 100% vào nghiệp vụ. |
| **Độ trễ thực thi** | Không có độ trễ bất ngờ, tốc độ tức thì. | Xuất hiện hiện tượng **Stop-The-World (STW)** khi GC chạy để dọn dẹp bộ nhớ lớn. |

- **2. Nguyên lý hoạt động của thuật toán Mark-and-Sweep:**
  1. **Mark (Đánh dấu):** Bắt đầu từ các gốc tham chiếu (GC Roots: biến cục bộ trên Stack, biến tĩnh Static), GC duyệt qua đồ thị liên kết. Đối tượng nào còn có đường dẫn tới GC Roots thì đánh dấu là **Sống (Reachable)**.
  2. **Sweep (Quét dọn):** Quét qua toàn bộ vùng nhớ Heap, thu hồi tất cả các đối tượng không được đánh dấu (Unreachable Objects) và đưa vùng nhớ trống vào danh sách khả dụng.
  3. **Compact (Dồn nén - tùy chọn):** Di chuyển các đối tượng còn sống dồn về một phía để khử hiện tượng phân mảnh bộ nhớ ngoài (External Fragmentation).

- **3. Mô hình phân chia thế hệ bộ nhớ Heap trong JVM (Generational GC):**
  - **Young Generation (Thế hệ trẻ):** Chứa các đối tượng mới sinh ra. Đa số đối tượng trong lập trình đều có vòng đời rất ngắn ("chết yểu"). Vùng này gồm 1 khoang **Eden** và 2 khoang **Survivor (S0, S1)**. Quá trình dọn rác ở đây gọi là **Minor GC** (diễn ra rất nhanh).
  - **Old Generation (Thế hệ già):** Chứa các đối tượng sống sót qua nhiều đợt Minor GC. Quá trình dọn rác ở đây gọi là **Major GC / Full GC** (tốn nhiều thời gian hơn).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Hiện tượng rò rỉ bộ nhớ trong Java vẫn có thể xảy ra như thế nào?**
  - Dù có GC, Java vẫn có thể bị Memory Leak nếu đối tượng không còn dùng nhưng vẫn bị vô tình neo giữ trong một cấu trúc dữ liệu toàn cục (Static Collection, ví dụ như đưa đối tượng vào `static List` hoặc quên hủy đăng ký Listener/Callback). Khi đó GC vẫn coi đối tượng là Reachable và không bao giờ thu hồi.

### 복습 체크리스트
- [ ] Ghi nhớ chức năng cốt lõi của GC: Tự động thu hồi vùng nhớ Heap của các đối tượng mất tham chiếu.
- [ ] Nắm được lợi ích chính: Ngăn ngừa lỗi rò rỉ bộ nhớ (Memory Leak).
- [ ] Phân biệt được sự đánh đổi: An toàn bộ nhớ đổi lấy hiện tượng tạm dừng Stop-The-World (STW).
- [ ] Hiểu chu trình 2 pha: Mark (đánh dấu còn sống) $\rightarrow$ Sweep (quét dọn phần rác).
