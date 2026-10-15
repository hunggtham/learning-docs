# 202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)

## 학습 목표 (Mục tiêu)
- Nắm vững triết lý và các thành phần cấu tạo cơ bản của lập trình hướng đối tượng (객체지향 기법 - OOP): Đối tượng (객체 / Instance), Lớp (클래스 / Class), Thuộc tính (속성 / Attribute), Phương thức (메소드 / Method), và Thông điệp (메시지 / Message).
- Ghi nhớ sâu sắc 5 nguyên lý cốt lõi của OOP theo thần chú **캡·정·상·추·다**: Tính đóng gói (캡슐화), Che giấu thông tin (정보 은닉), Tính kế thừa (상속성), Tính trừu tượng (추상화), và Tính đa hình (다형성).
- Phân biệt rõ hai cơ chế đa hình: Nạp chồng phương thức (오버로딩 - Method Overloading) và Ghi đè phương thức (오버라이딩 - Method Overriding).

## 핵심 키워드 (Từ khóa)
- 객체지향 프로그래밍 (OOP - Object-Oriented Programming)
- 캡정상추다 (Mnemonic: 캡슐화, 정보 은닉, 상속성, 추상화, 다형성)
- 캡슐화 (Encapsulation / 데이터와 메소드의 결합)
- 정보 은닉 (Information Hiding / private 접근 제어)
- 상속성 (Inheritance / 재사용 및 확장)
- 다형성 (Polymorphism / 동일 메시지 다른 동작)
- 오버로딩 vs 오버라이딩 (Overloading vs Overriding)

## 선행·연결 개념 (Kiến thức liên kết)
- [47-bai-hoc.md](47-bai-hoc.md): Nguyên lý thiết kế phần mềm có cấu trúc (모추정).
- [49-bai-hoc.md](49-bai-hoc.md): Địa chỉ IP, Subnetting và so sánh IPv4 vs IPv6.
- [정보처리기사/output/01-software-design/lessons/07-bai-hoc.md](../../01-software-design/lessons/07-bai-hoc.md): Các nguyên lý thiết kế SOLID trong OOP.

## 읽는 방법 (Cách đọc)
- Học theo thần chú 5 nguyên lý kinh điển của OOP: **캡·정·상·추·다**
  - **캡 (Đóng - 캡슐화 / Encapsulation):** Gom dữ liệu (Attribute) và các hàm xử lý dữ liệu đó (Method) lại thành một thể thống nhất bên trong một Lớp (Class) $\rightarrow$ Tăng tính độc lập, giảm độ kết hợp giữa các module.
  - **정 (Ẩn - 정보 은닉 / Information Hiding):** Dùng các từ khóa bảo vệ (`private`, `protected`) để giấu kín các biến nội bộ, không cho bên ngoài can thiệp tùy tiện; chỉ cho phép truy cập qua các hàm `getter`/`setter`.
  - **상 (Kế - 상속성 / Inheritance):** Lớp con (Subclass) kế thừa lại toàn bộ các thuộc tính và phương thức của lớp cha (Superclass) $\rightarrow$ Tối đa hóa khả năng tái sử dụng mã nguồn.
  - **추 (Trừu - 추상화 / Abstraction):** Lọc bỏ các chi tiết không cần thiết, chỉ mô hình hóa các đặc trưng bản chất của thực thể trong thế giới thực.
  - **다 (Đa - 다형성 / Polymorphism):** Cùng một tên phương thức (cùng một thông điệp) nhưng khi gửi tới các đối tượng khác nhau sẽ thực thi các hành vi hoàn toàn khác nhau.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng 5 nguyên lý cốt lõi của Lập trình Hướng đối tượng (캡정상추다):**

| Nguyên lý | Tên tiếng Hàn & Anh | Mục tiêu kiến trúc phần mềm | Lợi ích trong phát triển |
| :--- | :--- | :--- | :--- |
| **캡슐화** | **Encapsulation (Tính đóng gói)** | Gom thuộc tính và phương thức liên quan thành một khối duy nhất (Class) | Giảm độ kết hợp (Coupling), tăng tính gắn kết (Cohesion) |
| **정보 은닉** | **Information Hiding (Che giấu thông tin)** | Ngăn chặn việc truy cập hoặc sửa đổi trực tiếp dữ liệu nội bộ từ bên ngoài | Tránh tác dụng phụ (Side Effects) ngoài ý muốn khi sửa mã nguồn |
| **상속성** | **Inheritance (Tính kế thừa)** | Cho phép lớp con sử dụng lại mã nguồn của lớp cha và mở rộng thêm tính năng mới | Giảm thiểu việc viết mã trùng lặp, xây dựng phả hệ lớp phân tầng |
| **추상화** | **Abstraction (Tính trừu tượng)** | Mô hình hóa thực thể dựa trên các thuộc tính và hành vi trọng tâm của nghiệp vụ | Đơn giản hóa bài toán phức tạp, tạo khung giao diện (Interface/Abstract Class) |
| **다형성** | **Polymorphism (Tính đa hình)** | Một giao diện chung có thể đại diện cho nhiều hình thái hành vi khác nhau | Cho phép hệ thống mở rộng linh hoạt mà không cần sửa mã điều khiển gốc |

- **Bảng so sánh: Overloading vs Overriding:**

| Tiêu chuẩn so sánh | 메소드 오버로딩 (Method Overloading) | 메소드 오버라이딩 (Method Overriding) |
| :--- | :--- | :--- |
| **Bản chất kỹ thuật** | **Nạp chồng phương thức:** Trong cùng một Class, viết nhiều phương thức có **CÙNG TÊN** | **Ghi đè phương thức:** Lớp con viết lại phương thức đã kế thừa từ lớp cha |
| **Vị trí định nghĩa** | Xảy ra **trong nội bộ một Lớp duy nhất** | Xảy ra giữa **hai lớp có quan hệ kế thừa (Cha - Con)** |
| **Quy tắc chữ ký hàm** | Tên hàm giống nhau; **BẮT BUỘC danh sách tham số (số lượng, kiểu dữ liệu) PHẢI KHÁC NHAU** | Tên hàm, kiểu trả về và danh sách tham số **BẮT BUỘC PHẢI GIỐNG NHAU 100%** |
| **Thời điểm phân giải** | Đa hình tĩnh (Static Polymorphism); quyết định tại thời điểm **Biên dịch (Compile-time)** | Đa hình động (Dynamic Polymorphism); quyết định tại thời điểm **Thực thi (Runtime)** |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mối liên hệ giữa Lớp (Class) và Thể hiện (Instance / Object):**
  - **클래스 (Class):** Là bản vẽ thiết kế trừu tượng (Khuôn đúc bánh). Không chiếm dụng không gian bộ nhớ RAM khi chưa tạo đối tượng.
  - **객체 / 인스턴스 (Object / Instance):** Là sản phẩm thực tế được đúc ra từ Class bằng từ khóa `new` (Chiếc bánh thực tế). Chiếm dụng không gian thực sự trên vùng nhớ Heap của RAM.

### 복습 체크리스트
- [ ] Học thuộc lòng 5 nguyên lý OOP: 캡정상추다 (캡슐화, 정보 은닉, 상속성, 추상화, 다형성).
- [ ] Phân biệt được Overloading (cùng tên, khác tham số, cùng 1 lớp) và Overriding (viết đè lại hàm của lớp cha).
- [ ] Nhớ Overloading là đa hình lúc biên dịch (Compile-time), Overriding là đa hình lúc chạy (Runtime).
- [ ] Phân biệt được Class (khuôn mẫu tĩnh) và Instance (thực thể trên vùng nhớ Heap).
