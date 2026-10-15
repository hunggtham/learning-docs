# 206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm và mục tiêu của thiết kế hướng đối tượng (OOD - Object-Oriented Design): Chuyển hóa mô hình phân tích thành mô hình kiến trúc thực tế, trong đó yếu tố quan trọng nhất là **tính module hóa (모듈화 - Modularity)**.
- Hiểu các nguyên lý thiết kế then chốt: Trừu tượng hóa (추상화), Đóng gói và che giấu thông tin (정보 은닉), Kế thừa (상속), và Đa hình (다형성).
- Ghi nhớ lịch sử phát triển của các ngôn ngữ lập trình hướng đối tượng (OOP): **Simula (ngôn ngữ OOP đầu tiên)**, **Smalltalk (OOP thuần khiết đầu tiên)**, C++, và Java.

## 핵심 키워드 (Từ khóa)
- 객체지향 설계 (Object-Oriented Design - OOD)
- 모듈화 (Modularity - 가장 중요한 요소)
- 객체지향 프로그래밍 (Object-Oriented Programming - OOP)
- 정보 은닉 (Information Hiding)
- Simula 67 (최초의 객체지향 언어)
- Smalltalk (순수 객체지향 언어)
- 재사용성 & 유지보수성 (Reusability & Maintainability)

## 선행·연결 개념 (Kiến thức liên kết)
- [64-bai-hoc.md](64-bai-hoc.md): Phương pháp phân tích hướng đối tượng Rumbaugh (객동기).
- [66-bai-hoc.md](66-bai-hoc.md): Tái sử dụng phần mềm và kiến trúc thành phần (Component).
- [48-bai-hoc.md](48-bai-hoc.md): 5 nguyên lý hướng đối tượng kinh điển (캡정상추다).

## 읽는 방법 (Cách đọc)
- Trong bài thi kỹ sư CNTT:
  - Khi hỏi "Yếu tố quan trọng nhất trong thiết kế hướng đối tượng là gì?" $\rightarrow$ Đáp án chuẩn luôn là **모듈화 (Modularity / Tính module hóa)**.
  - Lịch sử ngôn ngữ: Ngôn ngữ hướng đối tượng **đầu tiên** là **Simula 67** (phát triển tại Na Uy). Ngôn ngữ OOP thuần túy đầu tiên đưa thuật ngữ "Object-Oriented" trở nên phổ biến là **Smalltalk**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Thiết kế hướng đối tượng (OOD - Object-Oriented Design):**
  - Chuyển dịch các mô hình trừu tượng từ OOA thành các cấu trúc phần mềm cụ thể (Data structures, Class definitions, Method signatures).
  - Mục tiêu tối cao: Xây dựng hệ thống có tính độc lập cao, mở rộng linh hoạt mà không làm vỡ kiến trúc cũ.
  - **Yếu tố cốt lõi hàng đầu:** **모듈화 (Modularity)** – Phân rã bài toán lớn thành các module/lớp tự chủ, liên kết với nhau qua các giao diện hợp đồng (Interfaces).

- **2. Lập trình hướng đối tượng (OOP - Object-Oriented Programming):**
  - Phương pháp lập trình xem chương trình là một tập hợp các đối tượng tự chủ có trạng thái (Properties/Attributes) và hành vi (Methods) tương tác trao đổi thông điệp (Messages) với nhau, mô phỏng thế giới thực.
  - Ưu điểm vượt trội: Tái sử dụng mã nguồn cực mạnh (Code Reuse qua kế thừa và thành phần), bảo trì nhanh chóng, giảm thiểu lỗi phụ thuộc chéo.

- **3. Cột mốc lịch sử các ngôn ngữ OOP kinh điển:**

| Ngôn ngữ | Năm ra đời & Tác giả | Vị thế lịch sử & Đặc trưng thi cử |
| :--- | :--- | :--- |
| **Simula 67** | 1967 (Ole-Johan Dahl & Kristen Nygaard) | **Ngôn ngữ lập trình hướng đối tượng ĐẦU TIÊN trên thế giới**; giới thiệu các khái niệm Class, Object, Inheritance, Subclass. |
| **Smalltalk** | Thập niên 1970 (Alan Kay - Xerox PARC) | **Ngôn ngữ OOP thuần khiết (Pure OOP) đầu tiên**; mọi thứ trong Smalltalk đều là đối tượng, kể cả số nguyên hay khối lệnh. |
| **C++** | 1983 (Bjarne Stroustrup) | Ngôn ngữ đa hình thức (Multi-paradigm), mở rộng từ C với Class và cơ chế kiểm tra kiểu tĩnh hiệu năng cao. |
| **Java** | 1995 (James Gosling - Sun Microsystems) | Ngôn ngữ hướng đối tượng phổ biến toàn cầu, độc lập nền tảng nhờ máy ảo Java (JVM - Write Once, Run Anywhere). |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Thiết kế hướng đối tượng vs Thiết kế cấu trúc:**
  - Thiết kế cấu trúc (Structured Design) tách biệt dữ liệu (Data) và hàm xử lý (Process), dẫn đến nguy cơ dữ liệu bị thay đổi tự do từ nhiều nơi.
  - Thiết kế hướng đối tượng (OOD) gom dữ liệu và các thao tác trên dữ liệu đó vào chung một vỏ bọc (Capsule) thông qua tính đóng gói (Encapsulation), bảo vệ toàn vẹn dữ liệu qua cơ chế che giấu thông tin (Information Hiding / `private`, `protected`).

### 복습 체크리스트
- [ ] Ghi nhớ yếu tố quan trọng nhất trong OOD là **모듈화 (Modularity)**.
- [ ] Nhớ **Simula 67** là ngôn ngữ hướng đối tượng đầu tiên của nhân loại.
- [ ] Nhớ **Smalltalk** là ngôn ngữ OOP thuần túy do Alan Kay phát triển.
- [ ] Hiểu rõ lợi ích lớn nhất của OOP là nâng cao tính tái sử dụng (Reusability) và bảo trì (Maintainability).
