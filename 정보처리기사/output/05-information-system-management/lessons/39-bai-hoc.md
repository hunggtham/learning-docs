# 11. 보충 및 심화 내용 (Bổ sung & Nâng cao)

## 학습 목표 (Mục tiêu)
- Nắm vững 4 đặc tính kiến trúc cốt lõi của Software Framework (모듈화, 재사용성, 확장성, 제어의 역흐름 - IoC).
- Phân biệt các hệ khung phần mềm phổ biến trong thực tế và đề thi: Spring Framework, eGovFrame, Microsoft .NET.
- Phân tích chi tiết ưu nhược điểm của các cấu trúc tô pô mạng (Star, Ring, Bus, Tree, Mesh) và công thức số đường truyền $n(n-1)/2$.
- Nhớ chuẩn các số hiệu tiêu chuẩn mạng quốc tế IEEE 802 (802.3, 802.11, 802.15).

## 핵심 키워드 (Từ khóa)
- **프레임워크 4대 특성 (Framework Characteristics)**: 모듈화 (Modularity), 재사용성 (Reusability), 확장성 (Extensibility), 제어의 역흐름 (Inversion of Control - IoC).
- **주요 프레임워크 (Frameworks)**: Spring (Java IoC/DI, AOP), 전자정부 표준 프레임워크 (eGovFrame), .NET (Microsoft CLR).
- **네트워크 토폴로지 (Topologies)**: 성형 (Star - Hub trung tâm), 링형 (Ring - vòng tròn khép kín), 버스형 (Bus - dây cáp chung có Terminator), 트리형 (Tree - phân cấp), 망형 (Mesh - $n(n-1)/2$).
- **IEEE 802 표준**: IEEE 802.3 (Ethernet - CSMA/CD), IEEE 802.11 (Wireless LAN - CSMA/CA), IEEE 802.15 (WPAN - Bluetooth).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [02-bai-hoc.md](02-bai-hoc.md) (방법론 테일러링 및 프레임워크 - Đặc tính khung phần mềm).
- Liên kết với [20-bai-hoc.md](20-bai-hoc.md) (네트워크 토폴로지 및 IEEE 표준 - Cấu trúc mạng cơ bản).
- Liên kết với [04-programming-language/69-bai-hoc.md](../../04-programming-language/lessons/69-bai-hoc.md) (Kiến trúc Spring và nguyên lý IoC).

## 읽는 방법 (Cách đọc)
- Phân biệt đặc tính Framework:
  - "Lập trình viên không trực tiếp gọi luồng xử lý mà Framework sẽ điều khiển và gọi lại mã của lập trình viên" $\rightarrow$ **제어의 역흐름 (Inversion of Control - IoC)**.
  - "Hai đầu dây cáp của cấu trúc mạng bus phải gắn linh kiện gì để tránh phản xạ tín hiệu?" $\rightarrow$ **Terminator (종단 저항)**.
  - "Mạng kết nối Star có điểm yếu lớn nhất là gì?" $\rightarrow$ **Nút trung tâm (Hub/Switch) bị hỏng sẽ làm tê liệt toàn mạng (Single Point of Failure)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bốn đặc tính kiến trúc của Software Framework
| Đặc tính (KR / EN) | Khái niệm kỹ thuật | Giá trị mang lại |
| :--- | :--- | :--- |
| **모듈화 (Modularity)** | Đóng gói các chức năng thành các module độc lập thông qua kỹ thuật trừu tượng hóa và che giấu thông tin | Giảm thiểu tối đa tác động lan truyền khi có sự thay đổi mã nguồn, tăng chất lượng phần mềm |
| **재사용성 (Reusability)** | Cung cấp sẵn các thành phần kiến trúc và hàm tiện ích chuẩn hóa dùng chung cho nhiều ứng dụng | Tăng năng suất phát triển, tiết kiệm chi phí và chuẩn hóa cách thức triển khai dự án |
| **확장성 (Extensibility)** | Cho phép lập trình viên kế thừa (Inheritance) và áp dụng đa hình (Polymorphism) để mở rộng chức năng | Cho phép tùy biến linh hoạt giải pháp nghiệp vụ mà không cần chỉnh sửa mã nguồn gốc của Framework |
| **제어의 역흐름 / (Inversion of Control - IoC)** | Quyền kiểm soát luồng thực thi của chương trình được chuyển giao cho Framework thay vì người lập trình chủ động gọi | Giảm sự phụ thuộc chặt chẽ giữa các thành phần (Loose Coupling), dễ dàng kiểm thử đơn vị |

#### 2. Các Framework tiêu chuẩn trong đề thi
- **스프링 프레임워크 (Spring Framework)**: Khung phát triển ứng dụng mã nguồn mở trên nền tảng Java, cung cấp các mẫu thiết kế mạnh mẽ gồm: Dependency Injection (DI), Inversion of Control (IoC), Aspect-Oriented Programming (AOP) và Spring MVC.
- **전자정부 표준 프레임워크 (eGovFrame)**: Khung tiêu chuẩn chính phủ điện tử của Hàn Quốc do Bộ Hành chính An toàn phát triển dựa trên Spring Framework, nhằm chuẩn hóa và nâng cao chất lượng các dự án phần mềm khối công quyền.
- **닷넷 프레임워크 (.NET Framework)**: Môi trường phát triển và thực thi ứng dụng của Microsoft chạy trên nền tảng Windows, hoạt động dựa trên máy ảo CLR (Common Language Runtime) hỗ trợ nhiều ngôn ngữ (C#, VB.NET, F#).

#### 3. Bảng so sánh 5 cấu trúc Tô pô mạng (Network Topologies)
| Dạng hình học (KR / EN) | Cấu trúc vật lý | Ưu điểm cốt lõi | Nhược điểm chí mạng |
| :--- | :--- | :--- | :--- |
| **성형 (Star Topology)** | Tất cả các nút kết nối trực tiếp (Point-to-Point) tới một Hub/Switch trung tâm | Cài đặt và mở rộng dễ dàng, sự cố 1 máy trạm không ảnh hưởng đến các máy khác | Nếu Hub/Switch trung tâm bị hỏng thì **toàn bộ mạng ngừng hoạt động** (Single Point of Failure) |
| **링형 (Ring Topology)** | Mỗi nút kết nối nối tiếp với 2 nút lân cận tạo thành một chu trình vòng khép kín | Tiết kiệm dây cáp hơn Star, không xảy ra xung đột gói tin (Token Ring) | Đứt một đoạn cáp có thể làm tê liệt toàn mạng; khó cô lập vị trí gặp sự cố |
| **버스형 (Bus Topology)** | Tất cả các máy tính cùng chia sẻ chung một trục cáp truyền dẫn chính (Trunk Cable) | Chi phí rẻ nhất, lắp đặt nhanh; hai đầu trục cáp phải gắn **Terminator** để khử sóng dội | Nếu trục cáp chính bị đứt, toàn bộ mạng ngừng hoạt động; lưu lượng lớn dễ gây xung đột (Collision) |
| **트리형 (Tree Topology)** | Các nút kết nối theo cấu trúc phân cấp hình cây (Hub chính nối tới các Hub phụ nhánh) | Dễ dàng quản trị và phân cụm mạng lớn; mở rộng theo tầng bậc linh hoạt | Máy nhánh phụ thuộc hoàn toàn vào các nút phân nhánh cấp trên |
| **망형 (Mesh Topology)** | Các nút mạng được kết nối trực tiếp lẫn nhau qua các liên kết riêng biệt | Độ tin cậy và khả năng chịu lỗi cao nhất; có nhiều đường đi dự phòng | Chi phí thi công cáp và số cổng đắt nhất; số đường cáp kết nối toàn phần là $\frac{n(n-1)}{2}$ |

#### 4. Các chuẩn kết nối IEEE 802
- **IEEE 802.3**: Tiêu chuẩn mạng cục bộ có dây **Ethernet**, sử dụng giao thức truy cập đường truyền **CSMA/CD** (Carrier Sense Multiple Access with Collision Detection).
- **IEEE 802.11**: Tiêu chuẩn mạng cục bộ không dây **Wireless LAN (Wi-Fi)**, sử dụng giao thức **CSMA/CA** (Carrier Sense Multiple Access with Collision Avoidance).
- **IEEE 802.15**: Tiêu chuẩn mạng cá nhân không dây **WPAN (Wireless Personal Area Network)** bao gồm công nghệ Bluetooth (802.15.1) và ZigBee (802.15.4).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ cơ chế IoC (Inversion of Control) trong Spring Framework
```
[Cách truyền thống (Chủ động)]
  Lập trình viên viết mã: OrderService tự khởi tạo `new DatabaseRepository()`
  └── Nhược điểm: Phụ thuộc cứng vào loại Database cụ thể.

[Cách hiện đại với Spring IoC Container (Thụ động)]
  Lập trình viên khai báo: OrderService cần một `IRepository`
  Spring Container tự nạp (Inject) `MySQLRepository` vào lúc chạy thông qua cơ chế DI
  └── Quyền kiểm soát luồng sống của đối tượng thuộc về Framework!
```

#### 2. Kỹ thuật tính số đường cáp trong Mesh Topology
- Đối với mạng Full Mesh gồm $n$ trạm: Mỗi trạm cần có $n - 1$ cổng giao tiếp (Ports).
- Tổng số đường kết nối vật lý trong toàn mạng là:
  $$\text{Số kết nối} = \frac{n(n - 1)}{2}$$
- *Ví dụ*: Một mạng có 8 máy trạm kết nối Full Mesh cần: $\frac{8 \times 7}{2} = 28$ đường truyền cáp riêng biệt.

---

### 복습 체크리스트
- [ ] Bốn đặc tính cốt lõi của Framework gồm những gì và đặc tính nào đảo ngược luồng điều khiển của ứng dụng?
- [ ] Điểm yếu rủi ro cao nhất của mạng cấu trúc Star (성형) là gì?
- [ ] Vai trò của linh kiện Terminator (종단 저항) trong cấu trúc mạng hình Bus (버스형) là gì?
- [ ] Giao thức kiểm soát đường truyền của chuẩn có dây IEEE 802.3 (CSMA/CD) khác gì so với không dây IEEE 802.11 (CSMA/CA)?
