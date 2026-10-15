# 070. 서버개발 프레임워크 (Server Development Framework)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, vai trò và kiến trúc hoạt động của các bộ khung phát triển ứng dụng máy chủ (서버개발 프레임워크 - Server Development Framework).
- Thấu hiểu và thuộc lòng 4 đặc trưng kiến trúc nền tảng của một Framework: Tính module hóa (모듈화), Khả năng tái sử dụng (재사용성), Tính mở rộng (확장성), và Đảo ngược quyền điều khiển (제어의 역전 - Inversion of Control / IoC).
- Phân biệt sự khác biệt bản chất kỹ thuật giữa Framework (Khung phần mềm) và Library (Thư viện thông thường).

## 핵심 키워드 (Từ khóa)
- 서버개발 프레임워크 (Server Development Framework)
- 모듈화 (Modularity - 캡슐화)
- 재사용성 (Reusability)
- 확장성 (Extensibility - 다형성)
- 제어의 역전 (IoC - Inversion of Control)
- 프레임워크 vs 라이브러리 (Framework vs Library)
- 스프링 프레임워크 (Spring Framework & DI)

## 선행·연결 개념 (Kiến thức liên kết)
- [68-bai-hoc.md](68-bai-hoc.md): Công cụ tự động hóa kỹ nghệ phần mềm CASE.
- [70-bai-hoc.md](70-bai-hoc.md): Nhận diện các lỗ hổng bảo mật trong mã nguồn máy chủ.
- [71-bai-hoc.md](71-bai-hoc.md): Hàm do người dùng định nghĩa và hướng đối tượng nâng cao.

## 읽는 방법 (Cách đọc)
- Trong bài thi kỹ sư CNTT, câu hỏi về đặc tính của Server Framework tập trung vào:
  - **제어의 역전 (Inversion of Control - IoC):** "Nếu trong lập trình truyền thống lập trình viên tự gọi các hàm của thư viện, thì trong Framework, **chính Framework là người nắm giữ luồng điều khiển và tự động gọi mã nguồn do lập trình viên viết**" (Hollywood Principle: *Don't call us, we'll call you*).
  - 4 đặc trưng trụ cột: **모듈화 (Modularity), 재사용성 (Reusability), 확장성 (Extensibility), 제어 반전 (IoC)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. 4 đặc tính cốt lõi của Framework phát triển máy chủ:**

| Đặc tính kiến trúc | Bản chất kỹ thuật & Ý nghĩa thiết kế |
| :--- | :--- |
| **모듈화 (Modularity)** | Ứng dụng nguyên lý đóng gói (Encapsulation) để phân chia hệ thống thành các module độc lập. Thay đổi bên trong một module không gây tác động tiêu cực đến các module khác, tối ưu hóa chi phí bảo trì. |
| **재사용성 (Reusability)** | Cung cấp sẵn các module chuẩn hóa cho các tác vụ phổ quát (kết nối cơ sở dữ liệu, quản lý phiên làm việc Session, bảo mật, gửi email), giúp rút ngắn thời gian phát triển và nâng cao chất lượng mã nguồn. |
| **확장성 (Extensibility)** | Cho phép lập trình viên tùy biến và bổ sung thêm các tính năng nghiệp vụ riêng biệt thông qua việc kế thừa (Inheritance) và cài đặt các giao diện trừu tượng (**Interface & Polymorphism**) mà không cần sửa đổi mã nguồn gốc của Framework. |
| **제어의 역전 (IoC)** | **Đảo ngược luồng điều khiển chương trình.** Vòng đời của các đối tượng (khởi tạo, cấu hình, hủy bỏ) do Container của Framework quản lý hoàn toàn; Framework sẽ tự động triệu gọi mã nguồn ứng dụng khi có sự kiện thích hợp. |

- **2. Bảng phân biệt sâu sắc: Framework vs Thư viện (Library):**

| Tiêu chí | Thư viện (Library) | Khung phần mềm (Framework) |
| :--- | :--- | :--- |
| **Quyền kiểm soát luồng** | **Lập trình viên (Developer)** chủ động quyết định khi nào gọi hàm của thư viện. | **Framework** nắm giữ luồng thực thi chính và tự động gọi code của Developer (IoC). |
| **Hình tượng thực tế** | Như bộ dụng cụ cơ khí (cờ lê, mỏ lết) mang ra dùng khi cần. | Như bộ khung nhà bê tông có sẵn các phòng, lập trình viên chỉ vào trang trí nội thất. |
| **Khả năng thay thế** | Dễ dàng thay thế thư viện này bằng thư viện khác có hàm tương tự. | Rất khó thay thế vì toàn bộ ứng dụng được xây dựng neo chặt theo kiến trúc của Framework. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế Tiêm phụ thuộc (Dependency Injection - DI) trong Spring Framework:**
  - DI là hình thức cụ thể hóa phổ biến nhất của IoC. Thay vì một đối tượng tự dùng toán tử `new` để tạo ra đối tượng phụ thuộc (gây kết hợp chặt chẽ), Framework sẽ tự động "tiêm" (Inject) đối tượng phụ thuộc vào thông qua Constructor hoặc Setter, giúp mã nguồn đạt được trạng thái Low Coupling lý tưởng.

### 복습 체크리스트
- [ ] Kể tên đầy đủ 4 đặc trưng của Server Framework: 모듈화, 재사용성, 확장성, 제어의 역전.
- [ ] Giải thích được bản chất của IoC (Inversion of Control): Framework nắm quyền điều khiển và gọi code của ta.
- [ ] Phân biệt được sự khác biệt cốt lõi về quyền kiểm soát luồng giữa Library và Framework.
- [ ] Hiểu được tính mở rộng (Extensibility) đạt được nhờ cơ chế đa hình (Polymorphism) và Interface.
