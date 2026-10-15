# 11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)

## 학습 목표 (Mục tiêu)
- Nắm vững vai trò và danh sách các sản phẩm máy chủ ứng dụng web (`WAS - Web Application Server`) tiêu biểu trong xử lý dữ liệu động.
- Phân biệt sự khác nhau về ký hiệu Sơ đồ luồng dữ liệu (`DFD`) giữa hai trường phái kinh điển: Yourdon & DeMarco và Gane & Sarson.
- Thuộc nằm lòng 3 khoang cấu trúc của một Lớp trong Class Diagram và phân biệt bản chất giữa Quan hệ tập hợp rỗng (`집합/집약 - Aggregation`) và Quan hệ hợp thành đặc (`포함/합성 - Composition`).
- Nắm vững các thành phần chi tiết của Biểu đồ tuần tự: Đường sinh mệnh (`생명선`) và Hộp thực thi (`실행 상자`).

## 핵심 키워드 (Từ khóa)
- WAS (Web Application Server: Tomcat, WebLogic, JEUS, JBoss)
- DFD 표기법 (Yourdon/DeMarco vs Gane/Sarson)
- 클래스 다이어그램 구획 (Class 3 Compartments: Name, Attributes, Operations)
- 집약 vs 합성 (Aggregation vs Composition: hình thoi rỗng vs hình thoi đặc)
- 스테레오 타입 심화 (`<<include>>`, `<<extend>>`, `<<interface>>`)
- 생명선 / 실행 상자 (Lifeline / Active Box trong Sequence Diagram)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([3. 모델링 및 UML](14-bai-hoc.md)):** Sau khi có bức tranh tổng thể về 13 loại biểu đồ UML, bài này đi sâu vào chi tiết kỹ thuật của các biểu đồ cốt lõi nhất thường xuất hiện trong đề thi thực tế.
- **Tiếp nối sang bài sau ([4. UML](16-bai-hoc.md)):** Khái quát hóa và hệ thống hóa toàn diện 6 mối quan hệ trong UML (Liên kết, Tập hợp, Hợp thành, Kế thừa, Phụ thuộc, Hiện thực hóa) với đầy đủ ký hiệu đường vẽ.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ chắc chắn: Hình thoi rỗng là Aggregation (tồn tại độc lập); Hình thoi đặc là Composition (vòng đời phụ thuộc).
- Đọc TẦNG B để hiểu cơ chế hủy đối tượng con trong Composition và cơ chế xử lý luồng động trong kiến trúc 3 tầng với WAS.

---

## 11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Web Application Server (WAS - Máy chủ ứng dụng web):**
  - **Bản chất:** Là phần mềm trung gian (Middleware) chuyên trách thực thi các logic ứng dụng nghiệp vụ và tạo ra nội dung động (`동적인 콘텐츠 처리`), giao tiếp giữa Web Server (chuyên nội dung tĩnh HTML/CSS) và Cơ sở dữ liệu (DBMS).
  - **Các sản phẩm WAS tiêu biểu trong đề thi:** **Tomcat, JEUS (TmaxSoft), WebLogic (Oracle), WebSphere (IBM), JBoss (RedHat), Jetty, Resin, GlassFish**.
- **2. So sánh ký hiệu DFD giữa 2 trường phái:**
  - `Yourdon & DeMarco`: Ký hiệu Tiến trình (`프로세스 - Process`) bằng **Hình tròn (원형 - Circle)**.
  - `Gane & Sarson`: Ký hiệu Tiến trình bằng **Hình chữ nhật bo tròn góc (둥근 사각형 - Rounded Rectangle)** có vạch kẻ ngang chia phần trên và dưới.
- **3. Cấu trúc 3 khoang của Lớp trong Class Diagram:**
  - Khoang 1 (Trên cùng): **Tên lớp (클래스 이름 - Class Name)**.
  - Khoang 2 (Ở giữa): **Thuộc tính (속성 - Attributes)** mô tả dữ liệu trạng thái.
  - Khoang 3 (Dưới cùng): **Phương thức / Thao tác (오퍼레이션 / 연산 - Operations/Methods)** mô tả hành vi chức năng.
- **4. Phân biệt quan hệ Tập hợp (Aggregation) vs Hợp thành (Composition):**
  - **집합 / 집약 (Aggregation - Quan hệ tập hợp):**
    - Mối quan hệ "has-a", một đối tượng chứa đối tượng khác nhưng **vòng đời của chúng độc lập với nhau (`독립적인 생명주기`)**. Khi đối tượng toàn thể bị hủy, đối tượng thành phần vẫn tiếp tục tồn tại.
    - Ký hiệu: Đường nối có **Hình thoi rỗng (빈 마름모)** ở phía lớp toàn thể.
    - Ví dụ: Máy tính (Computer) và Chuột máy tính (Mouse). Nếu máy tính hỏng, con chuột vẫn có thể cắm sang máy tính khác dùng bình thường.
  - **포함 / 합성 (Composition - Quan hệ hợp thành):**
    - Mối quan hệ tập hợp chặt chẽ, **vòng đời của đối tượng thành phần phụ thuộc hoàn toàn vào đối tượng toàn thể (`종속적인 생명주기`)**. Khi đối tượng toàn thể bị hủy, tất cả đối tượng thành phần bên trong cũng bị hủy theo.
    - Ký hiệu: Đường nối có **Hình thoi đặc (채워진 마름모)** ở phía lớp toàn thể.
    - Ví dụ: Ngôi nhà (House) và Căn phòng (Room). Nếu đập bỏ toàn bộ ngôi nhà, các căn phòng bên trong ngôi nhà đó đương nhiên không còn tồn tại.
- **5. Thành phần chi tiết của Biểu đồ tuần tự (Sequence Diagram):**
  - `객체 (Object)`: Hình chữ nhật ghi tên đối tượng ở trên cùng.
  - `생명선 (Lifeline - Đường sinh mệnh)`: Đường nét đứt sổ thẳng đứng từ đối tượng xuống dưới, biểu thị thời gian tồn tại của đối tượng trong bộ nhớ.
  - `실행 상자 (Active Box / Activation Box - Hộp thực thi)`: Hình chữ nhật hẹp nằm đè lên đường sinh mệnh, biểu thị khoảng thời gian đối tượng đang trực tiếp nắm quyền điều khiển hoặc thực thi phương thức.
  - `메시지 (Message - Thông điệp)`: Mũi tên ngang kết nối giữa các đường sinh mệnh (mũi tên nét liền đầu nhọn là gọi hàm đồng bộ, mũi tên nét đứt là phản hồi kết quả trả về).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Hình thoi rỗng (빈 마름모) biểu diễn quan hệ hợp thành (Composition)?"* -> **Sai hoàn toàn**. Hình thoi rỗng là Aggregation (Tập hợp); Hình thoi đặc mới là Composition (Hợp thành).
  - **Bẫy 2:** *"JEUS và WebLogic là hệ thống quản trị cơ sở dữ liệu DBMS?"* -> **Sai**. Đây là các máy chủ ứng dụng web (WAS - Web Application Server).
  - **Bẫy 3:** *"Trường phái nào dùng hình chữ nhật bo tròn để vẽ tiến trình DFD?"* -> **Gane & Sarson**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "WAS chạy ứng dụng web động; Thoi rỗng tập hợp sống riêng, Thoi đặc hợp thành chết chùm; Sequence có Sinh mệnh nét đứt và Hộp thực thi".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bản chất lập trình của Aggregation vs Composition trong mã nguồn (Java/C++):**
  - Trong **Aggregation**: Đối tượng thành phần được truyền từ ngoài vào qua Constructor (Dependency Injection):
    ```java
    class Computer {
        private Mouse mouse;
        public Computer(Mouse m) { this.mouse = m; } // Mouse được tạo ở ngoài
    }
    ```
  - Trong **Composition**: Đối tượng thành phần được khởi tạo trực tiếp bên trong Constructor của lớp cha:
    ```java
    class House {
        private Room room;
        public House() { this.room = new Room(); } // House chết thì room chết theo
    }
    ```

### 복습 체크리스트
- [ ] Kể tên ít nhất 4 máy chủ ứng dụng web WAS: Tomcat, WebLogic, JEUS, JBoss.
- [ ] Phân biệt được ký hiệu hình vẽ DFD của Yourdon/DeMarco (tròn) và Gane/Sarson (chữ nhật bo tròn).
- [ ] Nhớ thứ tự 3 khoang của Class Diagram (Tên lớp, Thuộc tính, Phương thức).
- [ ] Phân biệt được hình thoi rỗng (집약 - độc lập) và hình thoi đặc (합성 - phụ thuộc vòng đời).
- [ ] Nêu vai trò của 생명선 (Lifeline) và 실행 상자 (Active Box) trong Sequence Diagram.
