# 189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)

## 학습 목표 (Mục tiêu)
- Nắm vững các nguyên lý cơ bản của thiết kế phần mềm có cấu trúc (구조적 설계의 기본 원리): Tính mô-đun hóa (모듈화), Tính trừu tượng hóa (추상화), và Che giấu thông tin (정보 은닉) theo thần chú **모·추·정**.
- Phân biệt 3 cấp độ trừu tượng hóa trong thiết kế: Trừu tượng hóa chức năng (기능 추상화), Trừu tượng hóa điều khiển (제어 추상화), và Trừu tượng hóa dữ liệu (자료 추상화).
- Hiểu sâu khái niệm cấu trúc cây điều khiển: Độ quạt vào (공유도 / Fan-In) và Độ quạt ra (제어도 / Fan-Out), cùng các nguyên tắc thiết kế tối ưu hệ thống (Fan-In cao, Fan-Out thấp).

## 핵심 키워드 (Từ khóa)
- 구조적 설계 기본 원리 (Structured Design Principles)
- 모추정 (Mnemonic: 모듈화, 추상화, 정보 은닉)
- 모듈화 (Modularity / 독립적인 기능 단위 분할)
- 추상화 3유형 (기능, 제어, 자료 추상화)
- 정보 은닉 (Information Hiding / Parnas 원리 / 부수 효과 최소화)
- 팬인 vs 팬아웃 (Fan-In vs Fan-Out / 공유도 vs 제어도)

## 선행·연결 개념 (Kiến thức liên kết)
- [46-bai-hoc.md](46-bai-hoc.md): Các giao thức tầng mạng và ứng dụng OSI.
- [48-bai-hoc.md](48-bai-hoc.md): Các nguyên lý lập trình hướng đối tượng (OOP).
- [정보처리기사/output/01-software-design/lessons/33-bai-hoc.md](../../01-software-design/lessons/33-bai-hoc.md): Thiết kế kiến trúc mô-đun và độ kết dính (Cohesion).

## 읽는 방법 (Cách đọc)
- Học theo thần chú 3 nguyên lý thiết kế: **모·추·정**
  - **모 (Mô - 모듈화 / Modularity):** Chia nhỏ hệ thống phần mềm phức tạp thành các khối mô-đun độc lập, có chức năng chuyên biệt để dễ phát triển và bảo trì.
  - **추 (Trừu - 추상화 / Abstraction):** Thiết kế từ tổng thể khái quát xuống chi tiết cụ thể; bỏ qua các tiểu tiết kỹ thuật ở tầng cao.
  - **정 (Thông - 정보 은닉 / Information Hiding):** Giấu kín cấu trúc dữ liệu và thuật toán nội bộ bên trong mô-đun; các mô-đun khác chỉ được tương tác qua giao diện (Interface) công khai định sẵn.
- Quy tắc Fan-In và Fan-Out trong cấu trúc cây:
  - **Fan-In (Đi vào):** Số lượng mô-đun cấp trên gọi đến mình $\rightarrow$ **CÀNG CAO CÀNG TỐT** (chứng tỏ mô-đun này được tái sử dụng nhiều lần).
  - **Fan-Out (Đi ra):** Số lượng mô-đun cấp dưới mà mình trực tiếp gọi $\rightarrow$ **NÊN GIỮ VỪA PHẢI ($\le 7$)**; Fan-Out quá cao chứng tỏ mô-đun đó quá phức tạp, ôm đồm nhiều việc.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng 3 nguyên lý cốt lõi của Thiết kế có cấu trúc (모추정):**

| Nguyên lý | Tên tiếng Hàn & Anh | Mục tiêu và định hướng thiết kế | Lợi ích đạt được |
| :--- | :--- | :--- | :--- |
| **모듈화** | **Modularity (Mô-đun hóa)** | Phân rã bài toán lớn thành các đơn vị chức năng nhỏ hơn có tính độc lập cao (**높은 독립성**) | Giảm độ phức tạp, phân công làm việc nhóm song song dễ dàng |
| **추상화** | **Abstraction (Trừu tượng hóa)** | Nêu bật các đặc trưng bản chất của hệ thống mà không cần đi sâu vào chi tiết triển khai cụ thể | Phác thảo khung kiến trúc từ trên xuống dưới (Top-down) |
| **정보 은닉** | **Information Hiding (Che giấu thông tin)** | Đóng kín các chi tiết dữ liệu nội bộ; thay đổi bên trong **không làm ảnh hưởng (No Side Effect)** tới mô-đun khác | Dễ dàng sửa đổi và bảo trì mã nguồn mà không sợ làm sập hệ thống |

- **Bảng so sánh chi tiết: 팬인 (Fan-In) vs 팬아웃 (Fan-Out):**

| Khái niệm | Tên gọi học thuật | Định nghĩa hình học cây | Đánh giá thiết kế tối ưu |
| :--- | :--- | :--- | :--- |
| **Fan-In** | **공유도 (Độ chia sẻ dùng chung)** | Số lượng các mô-đun cấp trên **trực tiếp gọi đến (gọi vào)** mô-đun hiện tại | **Càng cao càng tốt (증가 권장)**; phản ánh mức độ tái sử dụng cao của mô-đun tiện ích |
| **Fan-Out** | **제어도 (Độ điều khiển)** | Số lượng các mô-đun cấp dưới do mô-đun hiện tại **trực tiếp gọi thực thi (gọi ra)** | **Nên giữ thấp hoặc vừa phải (감소 권장)**; nếu quá lớn (ví dụ $> 10$) cần tách thêm mô-đun trung gian |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **3 dạng thức Trừu tượng hóa (Abstraction Types):**
  1. **기능 추상화 (Trừu tượng chức năng):** Biểu diễn một chuỗi các hành vi xử lý bằng một tên gọi tổng quát (ví dụ: hàm `make_payment()`).
  2. **제어 추상화 (Trừu tượng điều khiển):** Trừu tượng hóa các cơ chế điều khiển luồng lệnh (ví dụ: câu lệnh lặp `for-each`, xử lý luồng sự kiện).
  3. **자료 추상화 (Trừu tượng dữ liệu):** Định nghĩa kiểu dữ liệu trừu tượng (ADT) bao gồm cấu trúc dữ liệu và tập hợp các phép toán hợp lệ trên kiểu đó mà không để lộ cách biểu diễn bộ nhớ.

### 복습 체크리스트
- [ ] Học thuộc lòng 3 nguyên lý thiết kế: 모추정 (모듈화, 추상화, 정보 은닉).
- [ ] Nhớ nguyên lý Information Hiding do David Parnas khởi xướng nhằm loại bỏ Side Effect.
- [ ] Phân biệt được Fan-In (số module gọi mình) và Fan-Out (số module mình gọi).
- [ ] Nhớ quy tắc thiết kế hệ thống tốt: Fan-In cao (tái sử dụng cao) và Fan-Out thấp (đơn giản, dễ kiểm soát).
