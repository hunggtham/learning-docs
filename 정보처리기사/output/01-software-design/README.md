# Môn 1 — 소프트웨어 설계 (Software Design) (Thiết kế phần mềm)

## Tài liệu tổng hợp
- [Tài liệu học đầy đủ](01-tai-lieu-hoc-day-du.md)

---

## Danh mục 12 Bài học chuyên sâu theo chuẩn 출제기준 2026

### Chương 1. 요구사항 확인 (Xác nhận yêu cầu)
1. [01. 소프트웨어 생명 주기 및 개발 모형 (Vòng đời phần mềm và Các mô hình phát triển)](lessons/01-sdlc-va-cac-mo-hinh-vong-doi.md)
   - *Phạm vi:* Khung SDLC, Khủng hoảng phần mềm, 4 mô hình kinh điển (Waterfall, Prototype, Spiral Boehm, V-Model), Ma trận lựa chọn mô hình theo rủi ro.
2. [02. 애자일 방법론, 스크럼 및 XP (Phương pháp luận Agile, Khung Scrum và Kỹ thuật XP)](lessons/02-phuong-phap-luan-agile-scrum-xp.md)
   - *Phạm vi:* Tuyên ngôn Agile (4 giá trị, 12 nguyên tắc); Khung Scrum (3 vai trò, 4 sự kiện, 3 tạo phẩm, Burn-down Chart); XP (5 giá trị, 12 thực hành); User Story (INVEST), Planning Poker.
3. [03. 요구공학 및 요구사항 분석·검증 (Kỹ nghệ và Đặc tả yêu cầu phần mềm)](lessons/03-ky-nghe-va-dac-ta-yeu-cau.md)
   - *Phạm vi:* Phân tích hiện trạng & hạ tầng (DAS/NAS/SAN); Kỹ nghệ yêu cầu (Phát triển vs Quản lý RTM); Chức năng vs Phi chức năng; DFD, DD, Mini-spec, CASE, Đặc tả hình thức; Thẩm định FTR (Inspection vs Walkthrough).
4. [04. UML 모델링 및 다이어그램 (Mô hình hóa UML và Hệ thống Biểu đồ)](lessons/04-mo-hinh-hoa-uml-va-bieu-do.md)
   - *Phạm vi:* Chuẩn UML (3 thành tố); 6 mối quan hệ cốt lõi; Quyền truy cập (+,-,#,~); Biểu đồ cấu trúc tĩnh (Class 3 ngăn, Component, Deployment); Biểu đồ hành vi động (Use Case `<<include>>` vs `<<extend>>`, Sequence, State, Activity).

### Chương 2. 화면 설계 (Thiết kế màn hình)
5. [05. 화면 설계 및 UI·UX·HCI (Thiết kế Giao diện người dùng và Tương tác UI/UX/HCI)](lessons/05-thiet-ke-giao-dien-ui-ux.md)
   - *Phạm vi:* 4 dạng UI (CLI, GUI, NUI, OUI); Cử chỉ cảm ứng di động; 4 nguyên tắc vàng UI (직관성, 유효성, 학습성, 유연성); Chuỗi sản phẩm Wireframe $\rightarrow$ Mockup $\rightarrow$ Storyboard $\rightarrow$ Prototype; Mối quan hệ HCI - UX - UI; Chuẩn ISO 9241.

### Chương 3. 애플리케이션 설계 (Thiết kế ứng dụng)
6. [06. 소프트웨어 아키텍처 및 품질 표준 (Thiết kế Kiến trúc phần mềm và Tiêu chuẩn chất lượng ISO)](lessons/06-thiet-ke-kien-truc-va-chat-luong-phan-mem.md)
   - *Phạm vi:* Phân cấp thiết kế (상위 설계 vs 하위 설계); Mô hình 4+1 View (Use Case trung tâm); Architectural Patterns (Layered, Pipe-Filter, MVC, Broker, Blackboard); Nguyên lý Parnas; Chuẩn chất lượng ISO/IEC 9126 (기-신-사-효-유-이) và ISO/IEC 25010.
7. [07. 객체지향 개념 및 SOLID 원칙 (Khái niệm Hướng đối tượng và 5 Nguyên tắc SOLID)](lessons/07-huong-doi-tuong-va-nguyen-ly-solid.md)
   - *Phạm vi:* Khái niệm OOP (Đối tượng, Lớp, Đóng gói, Kế thừa, Đa hình); Overloading vs Overriding; Phương pháp OOA Rumbaugh (객-동-기); 5 nguyên tắc vàng SOLID (SRP, OCP, LSP, ISP, DIP).
8. [08. 모듈 설계, 결합도·응집도 및 설계 도구 (Thiết kế Module, Độ phụ thuộc Coupling, Độ gắn kết Cohesion và Công cụ thiết kế)](lessons/08-thiet-ke-module-coupling-cohesion.md)
   - *Phạm vi:* Độc lập chức năng; 7 cấp độ Cohesion (기-순-교-절-시-논-우); 6 cấp độ Coupling (자-스-제-외-공-내); Fan-In cao / Fan-Out thấp; Đặc tả module dùng chung; N-S Chart (3 quy tắc); Tái sử dụng (합성 vs 생성); Thiết kế hệ thống mã.
9. [09. GoF 23 디자인 패턴 (23 Mẫu thiết kế GoF chuẩn quốc tế)](lessons/09-design-patterns-gof.md)
   - *Phạm vi:* 23 mẫu GoF: 5 Mẫu khởi tạo (Factory Method, Abstract Factory, Singleton, Builder, Prototype); 7 Mẫu cấu trúc (Adapter, Decorator, Facade, Proxy...); 11 Mẫu hành vi (Observer, Strategy, Template Method, State...).

### Chương 4. 인터페이스 설계 (Thiết kế giao diện liên kết)
10. [10. 인터페이스 설계, 미들웨어 및 연계 기술 (Thiết kế Giao diện, Middleware và Kỹ thuật Liên kết Hệ thống)](lessons/10-giao-dien-va-middleware.md)
    - *Phạm vi:* Thẩm định giao diện FTR; Tích hợp EAI (Point-to-Point, Hub & Spoke SPOF, Message Bus, Hybrid) & ESB; Định dạng JSON, XML, REST API, AJAX; Web Services (SOAP, WSDL, UDDI); 6 loại Middleware (RPC, MOM, TP-Monitor, ORB, WAS, DB Middleware).

### Chuyên đề củng cố nền tảng / Liên môn
11. [11. 관계형 데이터베이스 및 트랜잭션 관리 (Cơ sở dữ liệu quan hệ và Quản lý Giao dịch)](lessons/11-co-so-du-lieu-va-quan-ly-giao-dich.md)
    - *Phạm vi:* Bảng quan hệ, Ràng buộc toàn vẹn; 4 phép toán quan hệ thuần túy; Dị thường Anomaly; 6 cấp độ chuẩn hóa (도-부-이-결-다-조); Giao dịch ACID; Trạng thái giao dịch; Phục hồi REDO/UNDO; Kiểm soát đồng thời 2PL; Mật mã đối xứng vs bất đối xứng; 4 tính trong suốt phân tán.
12. [12. 자료구조 및 알고리즘 (Cấu trúc dữ liệu và Thuật toán nền tảng)](lessons/12-cau-truc-du-lieu-va-thuat-toan.md)
    - *Phạm vi:* Tuyến tính (Array, List, Stack LIFO, Queue FIFO, Deque) vs Phi tuyến tính (Tree, Graph); Duyệt cây nhị phân (Pre/In/Postorder); Ký pháp biểu thức hậu tố Stack; Độ phức tạp thuật toán sắp xếp (Bubble, Quick, Merge, Heap); Tìm kiếm nhị phân $O(\log N)$; Bảng băm Hashing $O(1)$; Cấu trúc tập tin ISAM.
