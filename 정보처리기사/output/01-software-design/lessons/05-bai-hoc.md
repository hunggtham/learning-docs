# 9. 요구사항 및 시스템 파악 (Yêu cầu & Phân tích Hệ thống)

## 학습 목표 (Mục tiêu)
- Phân biệt rõ ràng 3 phương pháp rà soát và kiểm tra tài liệu yêu cầu: Đánh giá đồng cấp (`동료검토`), Rà soát từng bước (`워크스루`), và Thanh tra chính thức (`인스펙션`).
- Nắm vững khái niệm, vai trò của Phần mềm trung gian (`미들웨어`) và các chủng loại tiêu biểu (RPC, MOM, TP-Monitor, ORB, WAS).
- Hiểu sâu vai trò và công cụ của Scrum (PO, SM, Sprint, Burn-down Chart) cùng các kỹ thuật thực hành cốt lõi của XP (Pair Programming, TDD, Refactoring, CI).
- Ghi nhớ 3 bước phân tích hiện trạng hệ thống (`현행 시스템 파악 3단계`) và tiêu chuẩn lựa chọn OS/DBMS.

## 핵심 키워드 (Từ khóa)
- 요구사항 검증 (Thẩm định yêu cầu: 동료검토, 워크스루, 인스펙션)
- 미들웨어 (Phần mềm trung gian / Middleware: RPC, MOM, TP-Monitor, WAS)
- 스크럼 (Scrum: PO, SM, 스프린트, 소멸 차트 / Burn-down Chart)
- XP 실천 방법 (Kỹ thuật thực hành XP: 짝 프로그래밍, TDD, 리팩토링, 계속적 통합)
- 현행 시스템 파악 (Phân tích hệ thống hiện tại / 3단계 절차)
- 가용성·성능·구축 비용 (Tính sẵn sàng, hiệu năng, chi phí xây dựng)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([2. 요구사항 개발](04-bai-hoc.md)):** Sau khi xây dựng tài liệu yêu cầu bằng DFD, DD và SRS, bước tiếp theo là kiểm chứng tính chính xác của tài liệu và đánh giá môi trường kỹ thuật hiện tại mà hệ thống sẽ tích hợp.
- **Tiếp nối sang bài sau ([10. 요구사항 심화](06-bai-hoc.md)):** Đi sâu vào các kỹ thuật đặc tả hình thức (Formal Specification) và các công cụ CASE tự động hóa phân tích yêu cầu chuyên sâu.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ mức độ khắt khe của 3 kỹ thuật Review: Inspection là chính thức (`공식적`), có chuyên gia độc lập; Walkthrough và Peer Review là phi chính thức.
- Đọc TẦNG B để hiểu rõ kiến trúc phân lớp của Middleware trong các hệ thống phân tán và cơ chế họp đánh giá Sprint trong mô hình Agile.

---

## 9. 요구사항 및 시스템 파악 (Yêu cầu & Phân tích Hệ thống)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **3 phương pháp rà soát thẩm định yêu cầu bằng thủ công:**
  1. **동료검토 (Peer Review - Đánh giá đồng cấp):**
     - Tác giả trực tiếp giải thích nội dung tài liệu đặc tả cho các đồng nghiệp, cùng nhau thảo luận để phát hiện lỗi khiếm khuyết. Mang tính phi chính thức (`비공식적`).
  2. **워크스루 (Walkthrough - Rà soát từng bước):**
     - Tài liệu được gửi trước cho các thành viên xem qua; sau đó tổ chức buổi họp ngắn để tác giả dẫn dắt rà soát từng kịch bản, tìm kiếm lỗi sớm. Mang tính phi chính thức (`비공식적`).
  3. **인스펙션 (Inspection - Thanh tra chuyên gia):**
     - **Chính thức và khắt khe nhất (`공식적인 검토 검사`)**. Người viết tài liệu không tham gia dẫn dắt; một nhóm chuyên gia thẩm định độc lập tiến hành soi xét tài liệu theo danh sách tiêu chí kiểm tra (Checklist) để vạch ra các lỗi kỹ thuật và độ lệch chuẩn.
- **미들웨어 (Middleware - Phần mềm trung gian):**
  - **Khái niệm:** Là phần mềm nằm giữa Hệ điều hành (`OS`) và Ứng dụng (`응용 프로그램`), cung cấp môi trường kết nối các hệ thống phần cứng/phần mềm không đồng nhất trong môi trường điện toán phân tán, đảm bảo tính trong suốt vị trí (`위치 투명성`).
  - **Các loại Middleware chủ chốt:**
    - `RPC (Remote Procedure Call)`: Gọi hàm/thủ tục từ xa qua mạng như trên máy cục bộ.
    - `MOM (Message-Oriented Middleware)`: Truyền thông điệp bất đồng bộ qua hàng đợi (Message Queue).
    - `TP-Monitor (Transaction Processing Monitor)`: Giám sát và quản lý giao dịch lớn, phân tải chịu lỗi cao (ngân hàng, hàng không).
    - `ORB (Object Request Broker)`: Kết nối đối tượng phân tán theo chuẩn CORBA.
    - `WAS (Web Application Server)`: Môi trường chạy logic nghiệp vụ phía web (Tomcat, WebLogic, Jeus).
- **스크럼 (Scrum) & XP (eXtreme Programming) trọng tâm:**
  - **Scrum:**
    - `제품 책임자 (PO; Product Owner)`: Đại diện tiếng nói khách hàng, xây dựng và quyết định thứ tự ưu tiên trong `제품 백로그 (Product Backlog)`.
    - `스크럼 마스터 (SM; Scrum Master)`: Người điều phối, loại bỏ các trở ngại cản trở team, không phải sếp chỉ đạo.
    - `스프린트 (Sprint)`: Vòng lặp phát triển chạy thử thực tế từ 2 đến 4 tuần.
    - `일일 스크럼 (Daily Scrum)`: Họp đứng 15 phút mỗi sáng, theo dõi tiến độ công việc còn lại bằng **소멸 차트 (Burn-down Chart)**.
  - **XP Core Practices (Kỹ thuật thực hành XP):**
    - `짝 프로그래밍 (Pair Programming)`: 2 lập trình viên cùng ngồi 1 máy tính (1 người code, 1 người review).
    - `테스트 주도 개발 (TDD)`: Viết kiểm thử tự động trước (`테스트 케이스 작성`), viết mã hiện thực sau.
    - `리팩토링 (Refactoring)`: Tối ưu hóa cấu trúc mã nguồn bên trong mà không làm thay đổi hành vi bên ngoài.
    - `계속적인 통합 (CI; Continuous Integration)`: Tích hợp mã nguồn của các thành viên liên tục hàng ngày.
- **현행 시스템 파악 3단계 (3 bước phân tích hiện trạng hệ thống):**
  - Bước 1: Nắm bắt Cấu trúc hệ thống, Chức năng và Giao diện (`시스템 구성, 기능, 인터페이스 파악`).
  - Bước 2: Nắm bắt Kiến trúc phần mềm và Các phân hệ (`아키텍처 및 소프트웨어 구성 파악`).
  - Bước 3: Nắm bắt Phần cứng máy chủ và Hạ tầng mạng (`하드웨어 및 네트워크 구성 파악`).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Phương pháp kiểm tra yêu cầu nào là chính thức nhất do nhóm chuyên gia độc lập thực hiện?"* -> **인스펙션 (Inspection)**, không phải Walkthrough hay Peer Review.
  - **Bẫy 2:** *"Trong Daily Scrum, cuộc họp kéo dài bao lâu và dùng công cụ gì?"* -> **15 phút, đứng họp, sử dụng 소멸 차트 (Burn-down Chart)**.
  - **Bẫy 3:** *"TDD viết code chức năng trước rồi mới viết test case sau?"* -> **Sai hoàn toàn**. TDD là viết Test trước, viết Code sau.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Inspection chính thức nhất; Middleware nối OS với App; Daily Scrum 15 phút Burn-down; TDD viết test trước code sau".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bản chất của Burn-down Chart trong Scrum:**
  - Trục hoành là Thời gian trong Sprint (tính theo ngày), trục tung là Tổng số lượng công việc còn lại (tính theo Giờ hoặc Story Point). Đường đồ thị lý tưởng sẽ dốc dần từ góc trên bên trái xuống số 0 ở góc dưới bên phải vào ngày kết thúc Sprint. Nếu đường thực tế nằm trên đường lý tưởng, tiến độ đang bị chậm trễ.
- **Tại sao cần 3 bước phân tích hiện trạng hệ thống:**
  - Kỹ sư phải khảo sát từ tầng trừu tượng nghiệp vụ và giao diện (Bước 1), sang cấu trúc phân tầng phần mềm và CSDL (Bước 2), rồi mới đến năng lực vật lý của máy chủ, dung lượng RAM, băng thông mạng (Bước 3). Nếu bỏ qua bước này, hệ thống mới xây dựng có thể không tương thích hoặc làm sập hạ tầng phần cứng hiện có.

### 복습 체크리스트
- [ ] Phân biệt được sự khác nhau giữa Peer Review, Walkthrough và Inspection (chính thức, checklist).
- [ ] Kể tên 5 loại Middleware phổ biến: RPC, MOM, TP-Monitor, ORB, WAS.
- [ ] Nắm vững 3 vai trò và chu trình Sprint trong Scrum cùng công cụ 소멸 차트 (Burn-down Chart).
- [ ] Liệt kê 4 kỹ thuật thực hành quan trọng của XP: 짝 프로그래밍, TDD, 리팩토링, CI.
- [ ] Nhớ thứ tự 3 bước của quy trình 현행 시스템 파악 (Cấu trúc/chức năng -> Kiến trúc/SW -> HW/Mạng).
