# 18. Mã nguồn sạch, Tái cấu trúc và Phân tích tĩnh (Clean Code, Refactoring & Static Analysis)

## 1. Tổng quan về Chất lượng mã nguồn và Clean Code (클린 코드)

Trong kỹ nghệ phần mềm, chi phí dành cho việc đọc hiểu và bảo trì mã nguồn thường chiếm tới hơn 70% tổng chi phí của toàn bộ vòng đời sản phẩm. Một đoạn mã chạy đúng chức năng nhưng lộn xộn, khó hiểu sẽ nhanh chóng trở thành gánh nặng kỹ thuật khổng lồ (**기술 부채 - Technical Debt**).

**클린 코드 (Clean Code - Mã nguồn sạch)** là mã nguồn có cấu trúc rõ ràng, dễ đọc, mạch lạc, dễ kiểm thử và mở rộng, giúp bất kỳ lập trình viên nào trong nhóm cũng có thể nắm bắt ý định thiết kế và bảo trì một cách thuận lợi.

### 1.1. 5 nguyên tắc viết Clean Code chuẩn thi (클린 코드 5대 원칙)

Đề thi Kỹ sư xử lý thông tin luôn yêu cầu ghi nhớ chính xác 5 tiêu chuẩn vàng định hướng việc viết mã sạch:

```
[1. 가독성 (Dễ đọc)] ──────► [2. 단순성 (Đơn giản)] ──────► [3. 의존성 배제 (Giảm phụ thuộc)]
                                                                      │
                      [5. 추상화 (Trừu tượng hóa)] ◄────── [4. 중복 최소화 (Tránh trùng lặp)]
```

| Nguyên tắc | Tên tiếng Hàn & Anh | Mục tiêu định hướng kỹ thuật | Biểu hiện vi phạm (Code Smell) |
| :--- | :--- | :--- | :--- |
| **Tính dễ đọc** | **가독성 (Readability)** | Bất kỳ ai đọc vào cũng hiểu ngay mục đích và hành vi của mã; tên biến/hàm phải có ý nghĩa biểu cảm cao, tuân thủ quy tắc thụt lề | Đặt tên tắt tối nghĩa (`int a, b;`), viết nhiều câu lệnh trên một dòng, định dạng lộn xộn |
| **Tính đơn giản** | **단순성 (Simplicity)** | Tuân thủ triết lý K.I.S.S (*Keep It Simple, Stupid*); mỗi hàm chỉ giải quyết duy nhất một công việc (**단일 책임**) | Hàm quá dài hàng trăm dòng, lồng ghép quá nhiều vòng lặp `for`/`if` phức tạp |
| **Loại trừ phụ thuộc** | **의존성 배제 (Loose Coupling)** | Giảm thiểu sự gắn kết cứng giữa các module/lớp; thay đổi ở một lớp không làm ảnh hưởng hoặc làm vỡ logic của lớp khác | Lớp phụ thuộc trực tiếp vào triển khai chi tiết của lớp khác thay vì thông qua Interface |
| **Trùng lặp tối thiểu** | **중복 최소화 (DRY - Don't Repeat)** | Tuyệt đối không sao chép và dán (Copy-Paste) mã logic; gom các đoạn mã lặp lại thành hàm hoặc lớp dùng chung | Cùng một đoạn thuật toán xác thực xuất hiện rải rác ở 5 tệp mã nguồn khác nhau |
| **Tính trừu tượng hóa** | **추상화 (Abstraction)** | Ẩn giấu các chi tiết cài đặt phức tạp đằng sau các giao diện (Interface/API) cấp cao, chỉ phơi bày những gì thực sự cần thiết | Phơi bày toàn bộ cấu trúc dữ liệu nội bộ ra bên ngoài, phá vỡ nguyên lý che giấu thông tin |

---

## 2. Các dạng mã nguồn có vấn đề: Alien Code, Spaghetti Code và Legacy Code

Khi chất lượng mã nguồn bị bỏ bê trong thời gian dài, phần mềm sẽ thoái hóa thành các trạng thái mã bệnh tật sau:

### 2.1. Bảng phân biệt 3 dạng mã nguồn có vấn đề

| Thuật ngữ | Tên tiếng Hàn & Anh | Bản chất nguyên nhân hình thành | Hệ quả trong công tác bảo trì |
| :--- | :--- | :--- | :--- |
| **Mã ngoài hành tinh** | **외계인 코드 (Alien Code)** | Mã nguồn quá cũ kỹ, **tác giả gốc đã nghỉ việc hoặc không thể liên lạc (개발자 부재)** và **hoàn toàn không có tài liệu kỹ thuật (참고 문서 없음)** | Người tiếp quản không thể hiểu nổi logic; việc chỉnh sửa một dòng có thể làm đổ vỡ toàn bộ hệ thống |
| **Mã mì sợi** | **스파게티 코드 (Spaghetti Code)** | Cấu trúc luồng điều khiển cực kỳ rối rắm, lạm dụng các lệnh nhảy tùy tiện (`goto`) hoặc phụ thuộc chéo vòng vèo | Cực kỳ khó gỡ lỗi (Debugging), khó theo dõi luồng thực thi dữ liệu, vi phạm lập trình có cấu trúc |
| **Mã di sản** | **레거시 코드 (Legacy Code)** | Mã nguồn cũ được viết bằng công nghệ lỗi thời nhưng hiện vẫn đang vận hành sinh ra doanh thu cho doanh nghiệp | Thiếu các bộ kiểm thử tự động (Unit Test), tiềm ẩn rủi ro cao khi phải tích hợp công nghệ mới |

> [!IMPORTANT]
> **Dấu hiệu nhận diện Alien Code trong đề thi:**
> Khi câu hỏi đề cập đến tình huống: *"Một đoạn mã nguồn được viết từ rất lâu trong quá khứ, người phát triển ban đầu không còn ở công ty (**개발자 부재**), tài liệu thiết kế hoặc tài liệu tham khảo hoàn toàn không tồn tại (**참고 문서 없음**)"*, đáp án chắc chắn là **외계인 코드 (Alien Code)**.

---

## 3. Tái cấu trúc mã nguồn (리팩토링 - Refactoring)

Để giải quyết nợ kỹ thuật và cải thiện chất lượng mã mà không làm gián đoạn nghiệp vụ của doanh nghiệp, lập trình viên sử dụng kỹ thuật tái cấu trúc mã nguồn.

### 3.1. Định nghĩa chuẩn thi của Refactoring
**리팩토링 (Refactoring)** là quá trình tái cấu trúc lại mã nguồn phần mềm nhằm nâng cao khả năng bảo trì (**유지보수성 향상**), cải thiện tính dễ đọc và loại bỏ các mùi hôi của mã (**Code Smells**), **nhưng tuyệt đối KHÔNG làm thay đổi hành vi bên ngoài của chương trình (외부 동작은 변경하지 않고 내부 구조만 개선)**.

### 3.2. Mục đích và kỹ thuật Refactoring phổ biến
- **Mục đích:**
  - Nâng cao tính dễ hiểu, giảm sự phức tạp của mã nguồn.
  - Tăng tốc độ phát triển các tính năng mới trong tương lai.
  - Hỗ trợ việc phát hiện các lỗi tiềm ẩn dễ dàng hơn.
- **Kỹ thuật tiêu biểu:**
  - *Extract Method (Trích xuất phương thức):* Tách một đoạn mã dài, phức tạp thành một hàm con độc lập có tên gọi rõ nghĩa.
  - *Rename Variable/Method (Đổi tên có ý nghĩa):* Đổi tên biến và hàm cho đúng với trách nhiệm thực tế.
  - *Replace Temp with Query:* Thay thế các biến tạm tính toán trung gian bằng một hàm truy vấn.

---

## 4. Công cụ phân tích tĩnh vs Phân tích động (정적 분석 vs 동적 분석 도구)

Trước khi chuyển giao mã nguồn sang các giai đoạn kiểm thử phức tạp, các công cụ kiểm tra tự động được sử dụng để rà soát chất lượng mã nguồn theo hai hướng tiếp cận:

```
                              ┌──────────────────────────────────────────────┐
                              │     ĐÁNH GIÁ CHẤT LƯỢNG MÃ NGUỒN             │
                              └──────────────────────┬───────────────────────┘
                                                     │
                         ┌───────────────────────────┴───────────────────────────┐
                         ▼                                                       ▼
            ┌───────────────────────────┐                           ┌───────────────────────────┐
            │  정적 분석 (Static)        │                           │  동적 분석 (Dynamic)       │
            │  - KHÔNG CHẠY mã nguồn    │                           │  - BẮT BUỘC CHẠY mã nguồn │
            │  - Tìm vi phạm quy chuẩn, │                           │  - Đo rò rỉ bộ nhớ,       │
            │    biến thừa, AST syntax  │                           │    profiling CPU, coverage│
            └────────────┬──────────────┘                           └────────────┬──────────────┘
                         │                                                       │
                 PMD, Checkstyle, SonarQube                              Valgrind, Profiler
```

### 4.1. Bảng so sánh Phân tích tĩnh vs Phân tích động

| Tiêu chí | 정적 분석 도구 (Static Analysis) | 동적 분석 도구 (Dynamic Analysis) |
| :--- | :--- | :--- |
| **Trạng thái thực thi** | **Không chạy chương trình (코드를 실행하지 않음)** | **Bắt buộc phải chạy chương trình (프로그램 실행 중)** |
| **Đối tượng phân tích** | Tệp mã nguồn (Source Code), cây cú pháp trừu tượng (AST) | Tiến trình thực thi (Process), bộ nhớ RAM, hành vi I/O |
| **Mục tiêu phát hiện** | - Biến khai báo nhưng không dùng (Unused Variables)<br>- Phương thức rỗng hoặc chưa hoàn thiện<br>- Vi phạm chuẩn lập trình (Coding Standard)<br>- Đoán trước nguy cơ tràn bộ đệm (Buffer Overflow) | - **Rò rỉ bộ nhớ (메모리 누수 - Memory Leak)**<br>- Xung đột tuyến trình (Thread Deadlock)<br>- Đo độ bao phủ mã kiểm thử (**Code Coverage**)<br>- Nút thắt cổ chai về thời gian CPU (Profiling) |
| **Thời điểm áp dụng** | Giai đoạn viết mã (Coding) hoặc tiền biên dịch (Pre-commit) | Giai đoạn kiểm thử đơn vị, kiểm thử tích hợp và kiểm thử tải |

### 4.2. Các công cụ phân tích tĩnh tiêu biểu trong đề thi

| Tên công cụ | Nền tảng / Ngôn ngữ | Đặc điểm kỹ thuật nhận diện đề thi |
| :--- | :--- | :--- |
| **PMD** | Java | Quét mã nguồn Java để phát hiện: **biến không sử dụng (미사용 변수)**, khối `catch` rỗng, phương thức chưa hiện thực, đối tượng không cần thiết |
| **Checkstyle** | Java | Kiểm tra việc tuân thủ các quy tắc chuẩn mực viết mã (**코딩 표준 준수 여부**): thụt lề, đặt tên lớp/biến, khoảng trắng, định dạng tệp |
| **Cppcheck** | C / C++ | Phân tích tĩnh chuyên sâu mã C/C++: phát hiện lỗi con trỏ null, tràn bộ đệm ngoài giới hạn mảng, rò rỉ tài nguyên |
| **SonarQube** | Đa ngôn ngữ | Nền tảng quản lý chất lượng mã nguồn tập trung toàn diện: tích hợp CI/CD, theo dõi nợ kỹ thuật, lỗi bảo mật (Vulnerabilities) và độ bao phủ test |

---

## 5. Câu hỏi ôn tập và bẫy đề thi thực tế

1. **Định nghĩa Alien Code:**
   - *Câu hỏi:* Thuật ngữ nào trong kỹ nghệ phần mềm chỉ đoạn mã nguồn đã được phát triển từ lâu, người phát triển ban đầu đã rời đi (**개발자 부재**), và hoàn toàn không có tài liệu kỹ thuật hoặc hướng dẫn bảo trì kèm theo (**참고 문서 없음**)?
   - *Đáp án chuẩn thi:* **외계인 코드 (Alien Code)**.
2. **Bản chất của Refactoring:**
   - *Bẫy đề thi:* "Refactoring là quá trình viết lại mã nguồn nhằm bổ sung thêm các tính năng nghiệp vụ mới cho người dùng." $\rightarrow$ **SAI**. Refactoring chỉ tái cấu trúc nội bộ để tăng khả năng bảo trì (**유지보수성**), **tuyệt đối không làm thay đổi hành vi bên ngoài (외부 동작 불변)** và không thêm tính năng mới.
3. **Phân biệt Static vs Dynamic Analysis:**
   - *Câu hỏi:* Công cụ kiểm tra chất lượng mã nguồn nào hoạt động bằng cách quét cú pháp trực tiếp trên tệp văn bản mã nguồn mà **không cần thực thi chương trình**?
   - *Đáp án chuẩn thi:* **정적 분석 도구 (Static Analysis Tools)**.
4. **Nhận diện công cụ PMD:**
   - *Câu hỏi:* Công cụ phân tích tĩnh nào chuyên dùng cho Java nhằm tìm kiếm các lỗi biến khai báo nhưng không dùng (**미사용 변수**) và các phương thức chưa hoàn thiện?
   - *Đáp án chuẩn thi:* **pmd**.

---

## 6. Liên kết bài học tiếp theo

Bên cạnh các nguyên lý về mã nguồn và công cụ phần mềm, một kỹ sư phát triển phần mềm cần nắm vững bản chất tầng vật lý phần cứng và cơ chế tổ chức bộ nhớ của hệ thống máy tính để tối ưu hóa hiệu năng chương trình. Tiếp tục với **[19-phan-cap-bo-nho-va-phan-cung-lien-ket.md](19-phan-cap-bo-nho-va-phan-cung-lien-ket.md)** để tìm hiểu về phân cấp bộ nhớ, RAM tĩnh vs RAM động, bộ nhớ kết hợp (CAM), bộ nhớ ảo và phân loại kiến trúc máy tính theo Flynn.
