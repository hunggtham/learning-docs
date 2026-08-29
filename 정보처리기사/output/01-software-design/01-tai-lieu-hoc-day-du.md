# Môn 1 — 소프트웨어 설계 (Software Design) (Thiết kế phần mềm)

## 학습 목표 (Mục tiêu học tập)

- 시험에서 사용하는 한국어 용어를 영어와 베트남어 뜻까지 함께 인식한다.
- 각 개념을 정의 → 구성요소/절차 → 비교 포인트 → 예시 순서로 설명할 수 있다.
- 앞에서 배운 개념과 뒤의 심화 개념을 연결하여 문제의 조건을 빠르게 해석한다.

## 권장 학습 순서 (Lộ trình đề xuất)

1. 먼저 이 문서의 각 `##` 단원을 순서대로 읽는다.
2. 단원마다 **핵심 키워드**를 소리 내어 읽고, 한국어 원문과 베트남어 설명을 함께 확인한다.
3. 마지막에 `복습 체크리스트`를 점검한 뒤, 세부 lesson 파일에서 헷갈리는 부분을 다시 본다.

> **Nguồn:** tổng hợp từ các Markdown đã generate trong `raw_md/final`, được đối chiếu với các nguồn `raw` và `raw_md` cùng môn. Nội dung gốc được giữ lại; chỉ chuẩn hoá cấu trúc bài học.

> **Quy ước đọc:** thuật ngữ được ưu tiên theo mẫu `한국어 (English) (Tiếng Việt)`. Mỗi ý tiếng Hàn có phần giải thích Việt ngữ liền kề hoặc ngay sau đó; khi gặp từ kỹ thuật trong ngoặc, hãy xem đó là nghĩa cần nhớ khi làm đề.

> **Cách học:** học theo thứ tự các mục; với mỗi mục, xác định khái niệm → cơ chế/quy tắc → ví dụ → mẹo nhớ. Các mục lặp lại ở phần “심화” (nâng cao) dùng để nối kiến thức trước đó với dạng câu hỏi sâu hơn.

---

## 1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)
- **개념**: Toàn bộ quá trình phát triển (Yêu cầu -> Thiết kế -> Code -> Test -> Bảo trì). Là tiêu chuẩn để quản lý dự án, chi phí, nhân lực.
- **폭포수 모형 (Waterfall Model)**: 
  - Tuần tự (선형 순차적). Xong bước này mới qua bước khác. Không quay lại được.
  - Phù hợp dự án có yêu cầu rõ ràng, hệ thống nhà nước/ngân hàng. Tài liệu là trọng tâm.
- **나선형 모형 (Spiral Model)**:
  - Do Boehm đề xuất. Trọng tâm: Phân tích rủi ro (위험 분석).
  - Chu trình: Kế hoạch (계획) -> Phân tích rủi ro (위험) -> Phát triển (개발) -> Đánh giá (평가). 
  - Phù hợp dự án lớn, rủi ro cao.
- **프로토타입 모형 (Prototype Model)**:
  - Làm bản nháp (시제품) trước khi phát triển thật. Phù hợp khi yêu cầu chưa rõ ràng.
- **V-모형 (V-Model)**:
  - Mỗi bước phát triển tương ứng với một bước Test (Ánh xạ Dev-Test). Yêu cầu chất lượng cực cao (Y tế, Hàng không).

---

## 1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)

### 001. 소프트웨어 공학의 기본 원칙 (Nguyên tắc cơ bản của kỹ nghệ phần mềm)
- 현대적인 프로그래밍 기술을 계속적으로 적용해야 한다. (Phải liên tục áp dụng các kỹ thuật lập trình hiện đại.)
- 개발된 소프트웨어의 품질이 유지되도록 지속적으로 검증해야 한다. (Phải liên tục xác minh để duy trì chất lượng phần mềm đã phát triển.)
- 소프트웨어 개발 관련 사항 및 결과에 대한 명확한 기록을 유지해야 한다. (Phải lưu giữ hồ sơ rõ ràng về các vấn đề và kết quả liên quan đến phát triển phần mềm.)
- **Ví dụ (Example):** Áp dụng CI/CD (Continuous Integration/Continuous Deployment) để liên tục kiểm thử (검증) phần mềm mỗi khi có code mới.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **HKK** (Hiện - Kiểm - Ký): **Hãy Kiểm Kê** (Kỹ thuật hiện đại - Kiểm chứng - Ghi chép).

### 002. 폭포수 모형 (Waterfall Model / Mô hình thác nước)
- 이전 단계로 돌아갈 수 없다는 전제하에 각 단계를 확실히 매듭짓고 다음 단계를 진행하는 개발 방법론이다. (Là phương pháp phát triển với tiền đề không thể quay lại giai đoạn trước, hoàn thành dứt điểm từng giai đoạn rồi mới tiến sang giai đoạn tiếp theo.)
- 보헴이 제시한 고전적 생명 주기 모형이다. (Là mô hình vòng đời cổ điển do Boehm đề xuất.)
- 요구사항을 반영하기 어렵다. (Khó phản ánh/thay đổi yêu cầu.)
- **Ví dụ (Example):** Xây dựng một ngôi nhà, bạn không thể xây mái nhà khi chưa làm xong móng. (Phải theo tuần tự).
- 💡 **Mẹo ghi nhớ (Mnemonic):** Nước chảy từ trên xuống, không chảy ngược lại (이전 단계로 돌아갈 수 없음).

### 003. 나선형 모형 (Spiral Model / Mô hình xoắn ốc)
- 나선을 따라 돌듯이 점진적으로 완벽한 최종 소프트웨어를 개발하는 것이다. (Phát triển phần mềm cuối cùng hoàn hảo một cách tuần tự giống như quay theo hình xoắn ốc.)
- '계획 수립 → 위험 분석 → 개발 및 검증 → 고객 평가' 과정이 반복적으로 수행된다. (Quá trình 'Lập kế hoạch → Phân tích rủi ro → Phát triển & Kiểm chứng → Khách hàng đánh giá' được lặp đi lặp lại.)
- **Ví dụ (Example):** Phát triển một game lớn, ban đầu làm bản demo (1 vòng xoắn), đánh giá rủi ro, rồi mới phát triển thêm tính năng (vòng xoắn tiếp theo).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KNKK** (Kế - Nguy - Khai - Khách): **Kế Nguy Khách Khóc** (Lập KH - Rủi ro - Phát triển - Khách hàng).

### 004. 애자일 모형의 주요 방법론 (Các phương pháp luận chính của mô hình Agile)
- 스크럼 (Scrum
- XP (eXtreme Programming)
- 기능 중심 개발 (FDD; Feature Driven Development)
- 칸반 (Kanban)
- Lean
- **Ví dụ (Example):** Các công ty startup thường dùng Scrum để phát triển nhanh một ứng dụng, chia thành các Sprint ngắn 2 tuần.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **SXFKL** (Scrum, XP, FDD, Kanban, Lean): **Sợ Xấu Phải Kiêng Luôn**.

### 005. 애자일 개발 4가지 핵심 가치 (4 Giá trị cốt lõi của phát triển Agile)
- 프로세스와 도구보다는 개인과 상호작용에 더 가치를 둔다. (Coi trọng cá nhân và sự tương tác hơn là quy trình và công cụ.)
- 방대한 문서보다는 실행되는 SW에 더 가치를 둔다. (Coi trọng phần mềm chạy được hơn là tài liệu đồ sộ.)
- 계약 협상보다는 고객과 협업에 더 가치를 둔다. (Coi trọng sự cộng tác với khách hàng hơn là đàm phán hợp đồng.)
- 계획을 따르기 보다는 변화에 반응하는 것에 더 가치를 둔다. (Coi trọng việc phản hồi với sự thay đổi hơn là bám sát kế hoạch.)
- **Ví dụ (Example):** Thay vì viết tài liệu 100 trang cho khách, nhóm Agile sẽ đưa cho khách một bản demo chạy được (실행되는 SW) để lấy ý kiến ngay.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CTKB** (Cá - Thực - Khách - Biến): **Cá Thực Khó Bắt** (Cá nhân - Thực thi - Khách hàng - Biến đổi).

### 006. XP의 핵심 가치 (Giá trị cốt lõi của XP - eXtreme Programming)
- 의사소통 (Communication - Giao tiếp)
- 단순성 (Simplicity - Sự đơn giản)
- 용기 (Courage - Dũng cảm)
- 존중 (Respect - Tôn trọng)
- 피드백 (Feedback - Phản hồi)
- **Ví dụ (Example):** Developer có 'dũng cảm' (용기) để xóa những đoạn code cũ không cần thiết và viết lại cho 'đơn giản' (단순성).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **YĐDTP** (Ý - Đơn - Dũng - Tôn - Phản): **Ý Định Dũng Tướng Phàm**.

---

## 2. 요구사항 개발 (Phát triển Yêu cầu)

### 007. 주요 비기능 요구사항 (Các yêu cầu phi chức năng chính / Non-functional Requirements)
- 성능 요구사항 (Yêu cầu hiệu năng)
- 보안 요구사항 (Yêu cầu bảo mật)
- 품질 요구사항 (Yêu cầu chất lượng)
- 제약사항 (Ràng buộc)
- 인터페이스 요구사항 (Yêu cầu giao diện)
- **Ví dụ (Example):** Chức năng đăng nhập là yêu cầu chức năng. Nhưng "Đăng nhập phải hoàn tất dưới 1 giây" là yêu cầu phi chức năng (hiệu năng - 성능).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **HBCRG** (Hiệu - Bảo - Chất - Ràng - Giao): **Học Bài Chăm Rồi Giỏi**.

### 008. 요구사항 개발 프로세스 (Quy trình phát triển yêu cầu)
- 도출 (Elicitation - Khám phá/Rút ra) → 분석 (Analysis - Phân tích) → 명세 (Specification - Đặc tả) → 확인 (Validation - Xác nhận)
- **Ví dụ (Example):** Phỏng vấn user (도출), lọc ra các yêu cầu hợp lý (분석), viết tài liệu SRS (명세), nhờ user ký duyệt (확인).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **ĐPMX** (Đồ - Phân - Minh - Xác): **Đi Phượt Một Xe**.

### 009. 요구사항 분석 (Phân tích yêu cầu / Requirements Analysis)
- 개발 대상에 대한 사용자의 요구사항을 이해하고 문서화(명세화)하는 활동을 의미한다. (Hoạt động hiểu và tài liệu hóa (đặc tả) yêu cầu của người dùng về đối tượng cần phát triển.)
- 소프트웨어 개발의 실제적인 첫 단계이다. (Là bước thực tế đầu tiên của phát triển phần mềm.)
- 사용자 요구의 타당성을 조사하고 비용과 일정에 대한 제약을 설정한다. (Khảo sát tính hợp lý của yêu cầu người dùng và thiết lập các ràng buộc về chi phí, lịch trình.)
- 사용자의 요구를 정확하게 추출하여 목표를 정하고, 해결 방식을 결정한다. (Trích xuất chính xác yêu cầu của người dùng để đặt mục tiêu và quyết định cách giải quyết.)
- **Ví dụ (Example):** Khách hàng muốn "App chạy nhanh". Phân tích viên sẽ dịch thành "Thời gian phản hồi < 2s" và xem xét chi phí server có đủ đáp ứng không (비용/일정 제약).

### 010. 자료 흐름도 (DFD - Data Flow Diagram) 의 구성 요소
- 프로세스 (Process - Quy trình): Hình tròn / Hình bầu dục. (Ví dụ: 물품 확인 - Kiểm tra hàng hóa)
- 자료 흐름 (Data Flow - Luồng dữ liệu): Mũi tên. (Ví dụ: 물품 코드 - Mã hàng hóa)
- 자료 저장소 (Data Store - Kho lưu trữ dữ liệu): Hai đường thẳng song song. (Ví dụ: 물품대장 - Sổ hàng hóa)
- 단말 (Terminator - Điểm cuối/Tác nhân ngoài): Hình chữ nhật. (Ví dụ: 공장 - Nhà máy)
- 💡 **Mẹo ghi nhớ (Mnemonic):** **PFST** (Process, Flow, Store, Terminator): **Phải Phạt Sợ Tội**.

### 011. 자료 사전 (Data Dictionary) 의 표기 기호
- `=`: 정의 (Định nghĩa - is composed of)
- `+`: 연결 (Kết nối/Và - and)
- `( )`: 생략 (Có thể bỏ qua/Tùy chọn - optional)
- `[ | ]`: 선택 (Lựa chọn [hoặc] - choose only one)
- `{ }`: 반복 (Lặp lại - iteration)
- `* *`: 설명 (Giải thích/Chú thích - comment)
- **Ví dụ (Example):** `Customer_Name = First_Name + (Middle_Name) + Last_Name`. Middle_Name nằm trong `( )` nghĩa là có thể không có (생략).
- 💡 **Mẹo ghi nhớ (Mnemonic):** `{ }` giống như vòng lặp trong code, nên là lặp lại (반복). `* *` giống comment `/* */` trong code.

### 012. HIPO (Hierarchy plus Input-Process-Output)
- 하향식 소프트웨어 개발을 위한 문서화 도구이다. (Là công cụ tài liệu hóa cho phát triển phần mềm theo hướng từ trên xuống - Top-down.)
- 기호, 도표 등을 사용하므로 보기 쉽고 이해하기도 쉽다. (Sử dụng ký hiệu, biểu đồ nên dễ nhìn và dễ hiểu.)
- 기능과 자료의 의존 관계를 동시에 표현할 수 있다. (Có thể biểu diễn đồng thời mối quan hệ phụ thuộc giữa chức năng và dữ liệu.)
- **Ví dụ (Example):** Vẽ một sơ đồ cây bắt đầu từ Hệ thống chính (Quản lý trường học) rẽ nhánh xuống các chức năng con (Quản lý điểm, Quản lý sinh viên).

---

## 9. 요구사항 및 시스템 파악 (Yêu cầu & Phân tích Hệ thống)

### 요구사항 검증 방법 (Phương pháp xác minh yêu cầu)
- **동료검토 (Peer Review):** 작성자가 명세서 내용을 직접 설명하면서 결함을 발견함. (Tác giả trực tiếp giải thích tài liệu để đồng nghiệp tìm lỗi - Phi chính thức).
- **워크스루 (Walk Through):** 미리 배포한 명세서를 사전 검토한 후 결함을 발견함. (Phát tài liệu trước, sau đó họp để tìm lỗi - Phi chính thức).
- **인스펙션 (Inspection):** 작성자를 제외한 다른 검토 전문가들이 결함을 발견함. (Các chuyên gia khác (không phải tác giả) kiểm tra chặt chẽ để tìm lỗi - **Chính thức**).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **PWI** (Peer - Walk - Inspect): **Phát Web In**. Inspection là khắt khe và chính thức nhất (공식적).

### 미들웨어 (Middleware)
- 분산 컴퓨팅 환경에서 서로 다른 기종 간을 연결한다. (Kết nối các nền tảng khác nhau trong môi trường điện toán phân tán).
- 운영체제와 응용 프로그램 사이에서 다양한 서비스를 제공한다. (Cung cấp các dịch vụ nằm giữa HĐH và Ứng dụng).
- 위치 투명성을 제공한다. (Cung cấp tính trong suốt về vị trí - User không cần biết server nằm đâu).
- 사용자가 미들웨어의 내부 동작을 확인하려면 별도의 응용 소프트웨어를 사용해야 한다.
- **종류 (Phân loại):** DB, RPC (Remote Procedure Call), MOM (Message Oriented Middleware), TP-Monitor (Transaction Processing Monitor), ORB (Object Request Broker), WAS (Web Application Server).

### 스크럼(Scrum) 상세 (Chi tiết về Scrum)
- **제품 책임자 (PO; Product Owner):** 요구사항을 작성하고 우선순위를 결정하는 주체. (Người đại diện khách hàng, tạo và quản lý thứ tự ưu tiên của Product Backlog).
- **스크럼 마스터 (SM; Scrum Master):** 스크럼 회의를 주관하고 장애 요소를 해결하는 가이드. (Người hướng dẫn, giải quyết khó khăn cho team, không phải là sếp quản lý).
- **개발팀 (Development Team):** 디자이너, 테스터 등 개발에 참여하는 모든 인원 (7~8명). (Nhóm đa chức năng trực tiếp làm ra sản phẩm).
- **제품 백로그 (Product Backlog):** 모든 요구사항(User Story) 목록. (Danh sách tổng tổng hợp mọi yêu cầu của sản phẩm).
- **스프린트 (Sprint):** 2~4주 주기의 실제 개발 과정. (Vòng lặp phát triển kéo dài 2-4 tuần).
- **일일 스크럼 (Daily Scrum):** 매일 15분, 서서 진행, 소멸 차트(Burn-down Chart) 사용. (Họp đứng 15 phút mỗi ngày cập nhật tiến độ, dùng Burn-down Chart).
- **스프린트 검토/회고 (Sprint Review/Retrospective):** 검토는 제품 시연, 회고는 프로세스 cải tiến. (Review = Demo sản phẩm; Retrospective = Rút kinh nghiệm quy trình).

### XP 주요 실천 방법 (Các kỹ thuật thực hành của XP)
- **짝 프로그래밍 (Pair Programming):** 2 người cùng code trên 1 máy tính.
- **공동 코드 소유 (Collective Ownership):** Code là của chung, ai cũng có quyền sửa.
- **테스트 주도 개발 (TDD - Test-Driven Development):** Viết Test case trước, viết Code sau.
- **전체 팀 (Whole Team):** Khách hàng và team phát triển làm việc cùng nhau như 1 đội.
- **계속적인 통합 (Continuous Integration):** Tích hợp code liên tục (CI) ngay khi xong 1 task.
- **리팩토링 (Refactoring):** Cải thiện cấu trúc code mà không đổi chức năng bên ngoài.
- **소규모 릴리즈 (Small Releases):** Cập nhật/Phát hành các phiên bản nhỏ liên tục.

### 현행 시스템 파악 (Phân tích hệ thống hiện tại)
- 1단계: 시스템 구성, 기능, 인터페이스 파악. (Bước 1: Nắm bắt Cấu trúc, Chức năng, Interface).
- 2단계: 아키텍처 및 소프트웨어 구성 파악. (Bước 2: Nắm bắt Kiến trúc và Phần mềm).
- 3단계: 하드웨어 및 네트워크 구성 파악. (Bước 3: Nắm bắt Phần cứng và Mạng).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KGI -> AS -> HN** (Kéo Ghế In -> Áo Sơ -> Hát Nhép) -> Giống như quy trình từ phần mềm đến phần cứng.

### 운영체제 (OS - Operating System)
- 컴퓨터 시스템의 자원들을 효율적으로 관리하며, 환경을 제공하는 소프트웨어이다. (Là phần mềm quản lý tài nguyên máy tính hiệu quả và cung cấp môi trường chạy ứng dụng).
- 고려사항 (Các yếu tố cần cân nhắc khi chọn): 가용성 (Tính sẵn sàng), 성능 (Hiệu năng), 기술 지원 (Hỗ trợ kỹ thuật), 주변 기기 (Thiết bị ngoại vi), 구축 비용 (Chi phí).

### 데이터베이스 관리 시스템 (DBMS)
- 사용자와 데이터베이스 사이에서 정보를 생성하고 관리해 주는 소프트웨어이다. (Phần mềm nằm giữa User và Database để quản lý dữ liệu - giải quyết vấn đề trùng lặp và phụ thuộc).
- 고려사항: 가용성, 성능, 기술 지원, 상호 호환성 (Tính tương thích), 구축 비용.

---

## 10. 요구사항 심화 (Yêu cầu chuyên sâu)

### 요구사항의 유형 (Các loại yêu cầu)
- **기능 요구사항 (Functional Requirements):** 시스템이 무엇을 하는지, 어떤 기능을 하는지에 대한 사항. (Hệ thống làm gì, chức năng nào. Ví dụ: Phải có nút Lưu, phải tính toán được thuế).
- **비기능 요구사항 (Non-functional Requirements):** 성능 (Hiệu năng), 인터페이스 (Giao diện), 데이터 (Dữ liệu), 테스트 (Kiểm thử), 보안 (Bảo mật), 품질 (Chất lượng), 제약사항 (Ràng buộc), 프로젝트 관리/지원 (Quản lý dự án/Hỗ trợ). (Là các yêu cầu không trực tiếp là chức năng nhưng quyết định chất lượng hệ thống).
- **Ví dụ (Example):** Chức năng giỏ hàng là "기능" (Chức năng). Nhưng giỏ hàng phải load trong 0.5 giây là "성능" (Hiệu năng - Phi chức năng).

### 요구사항 도출 (Requirement Elicitation / Thu thập yêu cầu)
- 기법 (Kỹ thuật): 청취와 인터뷰 (Lắng nghe & Phỏng vấn), 설문 (Khảo sát), 브레인스토밍 (Brainstorming), 워크샵 (Workshop), 프로토타이핑 (Prototyping), 유스케이스 (Use Case).

### 요구사항 명세 기법 (Kỹ thuật Đặc tả yêu cầu)
- **정형 명세 기법 (Formal Specification):** 수학적 기호, 정형화된 표기법 사용 (Dùng ký hiệu toán học). 정확하고 간결, 일관성 있음, 하지만 표기법이 어려워 사용자가 이해하기 어려움. (Chính xác, nhất quán nhưng khó hiểu với user). 종류: VDM, Z, Petri-net, CSP.
- **비정형 명세 기법 (Informal Specification):** 일반 명사, 동사 등의 자연어를 기반으로 서술 또는 다이어그램 작성. (Dùng ngôn ngữ tự nhiên/biểu đồ). 의사소통이 용이하지만 작성자에 따라 해석이 달라질 수 있음. (Dễ giao tiếp nhưng dễ gây hiểu nhầm). 종류: FSM, Decision Table, ER모델링, State Chart.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CTPT** (Chính-Toán-Phi-Tự) -> **Chăm Toán Phải Tốt** -> 정형 = 수학적 (Chính thức = Toán học), 비정형 = 자연어 (Phi chính thức = Tự nhiên).

### 요구사항 분석을 위한 CASE 도구 (Công cụ CASE tự động hóa phân tích)
- **SADT:** SoftTech사 개발, 구조적 분석 및 설계 도구. (Công cụ phân tích cấu trúc của SoftTech).
- **SREM (RSL/REVS):** TRW사 개발, 실시간 처리 소프트웨어 요구사항 기술. (Công cụ cho hệ thống thời gian thực, dùng RSL và REVS).
- **PSL/PSA:** 미시간 대학 개발. (Phát triển bởi ĐH Michigan).
- **TAGS:** 개발 주기 전 과정에 이용할 수 있는 통합 자동화 도구. (Công cụ tích hợp toàn bộ vòng đời).

---

## 2. 요구사항 정의 (Requirements Definition)
- **기능 요구사항 (Functional)**: Chức năng hệ thống phải có (Ví dụ: Đăng nhập).
- **비기능 요구사항 (Non-Functional)**: Hiệu năng, bảo mật, chất lượng, ràng buộc (Ví dụ: Phản hồi dưới 1s).
- **개발 프로세스 (Development Process)**: 
  1. 도출 (Elicitation) -> 2. 분석 (Analysis) -> 3. 명세 (Specification) -> 4. 확인/검증 (Validation).
- 💡 **Mẹo ghi nhớ**: Đ/P/M/X (Elicitation, Analysis, Spec, Validation) -> **Đi Phượt Một Xe**
- **명세 기법 (Specification Techniques)**:
  - 정형 (Formal): Ký hiệu toán học (Toán học, VDM, Z-schema). Rõ ràng nhưng khó hiểu với user.
  - 비정형 (Informal): Ngôn ngữ tự nhiên (Natural language, FSM, ERD). Dễ hiểu nhưng có thể mơ hồ.

---

## 3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)
- **자료 흐름도 (DFD - Data Flow Diagram)**:
  - 프로세스 (Process - Tròn), 자료 흐름 (Data Flow - Mũi tên), 자료 저장소 (Data Store - Đường thẳng), 단말 (Terminator - Vuông).
- **자료 사전 (DD - Data Dictionary)**: 
  - `=`: Định nghĩa (is composed of)
  - `+`: Kết nối (and)
  - `( )`: Tùy chọn (Optional)
  - `[ | ]`: Lựa chọn (or)
  - `{ }`: Lặp lại (Iteration)
  - `**`: Ghi chú (Comment)
- **CASE 도구 (CASE Tools)**: SADT, SREM, PSL/PSA.
- **HIPO (Hierarchical Input Process Output)**: Phân tích Top-down (가시적 도표, 총체적 도표, 세부적 도표).

---

## 1. 요구사항 개발 기법 (Requirements Elicitation Techniques)
- **도출 (Elicitation) 기법**:
  - **인터뷰 (Interview)**: Phỏng vấn.
  - **브레인스토밍 (Brainstorming)**: Công não ý tưởng (Không chỉ trích).
  - **델파이 기법 (Delphi)**: Hỏi ý kiến chuyên gia ẩn danh.
  - **프로토타이핑 (Prototyping)**: Làm mẫu thử.

---

## 12. 요구사항 (Requirements)
### 요구사항 분석 (Requirements Analysis)
*   **분류 (Phân loại):** 기능적(Functional) / 비기능적(Non-functional)으로 조직화.
*   **절차 (Quy trình 5 bước):** 선별(목록 작성) -> 자료 준비 -> 분류(기능/비기능) -> 분석 및 수정 -> 전달 (Lọc -> Chuẩn bị -> Phân loại -> Phân tích/Sửa -> Truyền đạt).

### 요구사항 검증 (Requirements Verification)
**설계 및 구현 전에 베이스라인(Baseline) 설정** (Xác minh trước khi thiết kế/code để chốt Baseline làm chuẩn).
*   **검증 방법 (Các phương pháp kiểm tra):**
    *   수작업: 동료검토(Peer Review), 워크스루(Walkthrough), 인스펙션(Inspection).
    *   **프로토타이핑 (Prototyping):** 견본 제작 (Làm bản mẫu dùng thử).
    *   **테스트 설계 (Test Design):** 테스트 케이스 생성 (Viết test case trước để xem có test được không).
    *   **CASE 도구:** 자동화 도구로 일관성 분석 (Dùng phần mềm check logic).

### 요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)
1.  **완전성 (Completeness):** 누락 없이 (Đầy đủ).
2.  **일관성 (Consistency):** 충돌 없이 (Nhất quán).
3.  **명확성 (Unambiguity):** 똑같이 이해되게 (Rõ ràng).
4.  **기능성 (Functionality):** '어떻게'보다 '무엇을(What)' (Tập trung vào tính năng "Làm gì" hơn là "Làm như thế nào").
5.  **검증 가능성 (Verifiability):** 테스트 가능 여부 (Có thể kiểm chứng/test được).
6.  **추적 가능성 (Traceability):** 설계서와 연결 (Có thể truy xuất).
7.  **변경 용이성 (Easily Changeable):** 수정 용이 (Dễ thay đổi).

---

---

## 1. 현행 시스템 분석 (Current System Analysis)
- **플랫폼 성능 (Platform Performance)**: 
  - 가용성 (Availability), 경과 시간 (Turnaround Time), 응답 시간 (Response Time), 사용률 (Utilization).
- **운영체제 및 DBMS 고려사항 (OS & DBMS Considerations)**: 
  - 신뢰도 (Reliability), 성능 (Performance), 기술 지원 (Tech Support), 주변 기기 (Peripherals), 구축 비용 (Cost), 상호 호환성 (Compatibility).

---

## 3. 현행 시스템 파악 (Understanding Current System)
- **1단계**: 시스템 구성 (기간 업무/지원 업무), 기능 (계층형), 인터페이스 (Giao thức, loại liên kết).
- **2단계**: 아키텍처 구성 (Kiến trúc), 소프트웨어 구성 (Bản quyền - 라이선스).
- **3단계**: 하드웨어 구성 (Dự phòng - 이중화/Redundancy), 네트워크 구성 (Vị trí vật lý, mạng).

---

## 3. 모델링 및 UML (Mô hình hóa và UML)

### 013. UML (Unified Modeling Language)
- 시스템 개발자와 고객 또는 개발자 상호 간의 의사소통이 원활하게 이루어지도록 표준화한 대표적인 객체지향 모델링 언어이다. (Là ngôn ngữ mô hình hóa hướng đối tượng tiêu biểu được chuẩn hóa để việc giao tiếp giữa nhà phát triển hệ thống và khách hàng, hoặc giữa các nhà phát triển với nhau diễn ra suôn sẻ.)
- 구성 요소 (Components): 사물 (Things - Sự vật), 관계 (Relationships - Mối quan hệ), 다이어그램 (Diagram - Biểu đồ).
- **Ví dụ (Example):** Khi xây nhà cần bản vẽ thiết kế (Blueprint). Khi làm phần mềm, dùng UML làm bản vẽ thiết kế chung để ai cũng hiểu.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **SQĐ** (Sự - Quan - Đa): **Sợ Quá Đi** (Sự vật - Quan hệ - Đa biểu đồ).

### 014. UML의 주요 관계 (Các mối quan hệ chính trong UML)
- 일반화 (Generalization) 관계: 하나의 사물이 다른 사물에 비해 더 일반적인지 구체적인지를 표현. (Thể hiện một sự vật là tổng quát hay cụ thể hơn sự vật khác - kế thừa).
- 의존 (Dependency) 관계: 필요에 의해 서로에게 영향을 주는 짧은 시간 동안만 연관을 유지하는 관계를 표현. (Thể hiện mối quan hệ phụ thuộc ngắn hạn, ảnh hưởng lẫn nhau khi cần thiết).
- 실체화 (Realization) 관계: 사물이 할 수 있거나 해야 하는 기능으로 서로를 그룹화 할 수 있는 관계를 표현. (Thể hiện mối quan hệ hiện thực hóa chức năng mà sự vật có thể/phải làm - interface).
- **Ví dụ (Example):** Động vật -> Chó, Mèo là mối quan hệ '일반화' (Generalization).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **NYT** (Nhất - Ý - Thực): **Như Ý Thật** (Nhất quát - Ý tồn - Thực thể).

### 015. 구조적(Structural) 다이어그램의 종류 (Các loại biểu đồ cấu trúc - Tĩnh)
- 클래스 다이어그램 (Class Diagram)
- 객체 다이어그램 (Object Diagram)
- 컴포넌트 다이어그램 (Component Diagram)
- 배치 다이어그램 (Deployment Diagram)
- 복합체 구조 다이어그램 (Composite Structure Diagram)
- 패키지 다이어그램 (Package Diagram)
- **Ví dụ (Example):** Class Diagram thể hiện cấu trúc tĩnh của hệ thống, giống như sơ đồ tổ chức của một công ty.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **LĐCBPG** (Lớp - Đối - Com - Bố - Phức - Gói): **Làm Được Có Bữa Phải Giỏi**. Các biểu đồ này thể hiện cấu trúc "Tĩnh" (정적).

### 016. 행위(Behavioral) 다이어그램의 종류 (Các loại biểu đồ hành vi - Động)
- 유스케이스 다이어그램 (Use Case Diagram)
- 순차 다이어그램 (Sequence Diagram)
- 커뮤니케이션 다이어그램 (Communication Diagram)
- 상태 다이어그램 (State Diagram)
- 활동 다이어그램 (Activity Diagram)
- 상호작용 개요 다이어그램 (Interaction Overview Diagram)
- 타이밍 다이어그램 (Timing Diagram)
- **Ví dụ (Example):** Sequence Diagram thể hiện trình tự thời gian gửi tin nhắn (메시지) giữa các đối tượng (hành vi động).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **UTCTHTT** (Use - Trình - Com - Trạng - Hoạt - Tương - Time): **Uống Trà Chiều Thấy Hay Thật Tuyệt**. Các biểu đồ này thể hiện đặc tính "Động" (동적).

### 017. 스테레오 타입 (Stereotype)
- UML에서 표현하는 기본 기능 외에 추가적인 기능을 표현하기 위해 사용한다. (Dùng để biểu diễn các chức năng bổ sung ngoài chức năng cơ bản trong UML.)
- 길러멧(Guilemet)이라고 부르는 겹화살괄호(`<< >>`) 사이에 표현할 형태를 기술한다. (Viết hình thái muốn biểu diễn giữa cặp dấu ngoặc nhọn kép `<< >>` gọi là Guilemet.)
- **Ví dụ (Example):** `<<include>>` hoặc `<<extend>>` trong Use Case Diagram.

### 018. 유스케이스 다이어그램 - 액터(Actor) (Biểu đồ Use Case - Tác nhân)
- 시스템과 상호작용을 하는 모든 외부 요소로, 사람이나 외부 시스템을 의미한다. (Là tất cả các yếu tố bên ngoài tương tác với hệ thống, có nghĩa là con người hoặc hệ thống bên ngoài.)
- 주액터 (Primary Actor): 시스템을 사용함으로써 이득을 얻는 대상으로, 주로 사람이 해당함. (Đối tượng nhận được lợi ích khi dùng hệ thống, chủ yếu là con người - ví dụ: Khách hàng.)
- 부액터 (Secondary Actor): 주액터의 목적 달성을 위해 시스템에 서비스를 제공하는 외부 시스템으로, 조직이나 기관 등이 될 수 있음. (Hệ thống bên ngoài cung cấp dịch vụ cho hệ thống để đạt mục đích của Primary Actor - ví dụ: Cổng thanh toán ngân hàng.)

### 019. 순차(Sequence) 다이어그램의 구성 요소 (Thành phần của biểu đồ Sequence)
- 액터 (Actor - Tác nhân)
- 객체 (Object - Đối tượng)
- 생명선 (Lifeline - Đường đời)
- 실행 상자 (Active Box - Hộp thực thi)
- 메시지 (Message - Thông điệp)
- **Ví dụ (Example):** Khi user (Actor) ấn nút mua hàng, một mũi tên (Message) sẽ được gửi đến Giỏ hàng (Object). Đường nét đứt sổ dọc xuống từ Giỏ hàng là 생명선 (Lifeline).

---

## 11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)

### 웹 애플리케이션 서버 (WAS - Web Application Server)
- 동적인 콘텐츠를 처리하기 위해 사용되는 미들웨어. (Middleware xử lý các nội dung web động thay vì web tĩnh).
- 종류: Tomcat, GlassFish, JBoss, Jetty, JEUS, Resin, WebLogic, WebSphere.

### 자료 흐름도 (DFD) 표기법 차이 (Khác biệt ký hiệu DFD)
- **Yourdon/DeMarco:** 프로세스를 원(원형)으로 표시. (Process là hình tròn).
- **Gane/Sarson:** 프로세스를 둥근 사각형으로 표시. (Process là hình chữ nhật bo góc).

### HIPO Chart의 종류 (Các loại biểu đồ HIPO)
- **가시적 도표 (Visual Table of Contents):** 시스템의 전체적인 기능과 흐름을 보여주는 계층(Tree) 구조도. (Cấu trúc cây tổng thể).
- **총체적 도표 (Overview Diagram):** 입력, 처리, 출력에 대한 전반적인 정보를 제공. (Cung cấp thông tin tổng quan I-P-O).
- **세부적 도표 (Detail Diagram):** 기본 요소들을 상세히 기술하는 도표. (Mô tả chi tiết các yếu tố cơ bản).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **GTT** (Gia - Tổng - Tế): **Giữ Trật Tự**.

### 클래스 다이어그램 심화 (Class Diagram chi tiết)
- **클래스 (Class):** 3개의 구획으로 나뉨 (Chia làm 3 phần). 이름 (Tên class), 속성 (Attribute/Biến), 오퍼레이션 (Operation/Hàm, Phương thức).
- **관계 (Relationships) 심화:**
  - **연관 (Association):** 2개 이상의 사물이 서로 관련되어 있음 (Mũi tên ngang).
  - **집합 (Aggregation):** 하나의 사물이 다른 사물에 포함되어 있는 관계 (Hình thoi rỗng). (Ví dụ: Máy tính và Chuột - Mất máy tính chuột vẫn tồn tại).
  - **포함 (Composition):** 집합 관계의 특수한 형태, 포함하는 사물의 변화가 포함되는 사물에게 영향을 미치는 관계 (Hình thoi đặc). (Ví dụ: Tòa nhà và Căn phòng - Phá tòa nhà thì phòng cũng mất).

### 스테레오 타입 (Stereotype) 추가
- `<<include>>`: 연결된 다른 UML 요소에 대해 포함 관계. (Quan hệ Bắt buộc phải có - Bắt buộc thực hiện Use case kia).
- `<<extend>>`: 확장 관계. (Quan hệ Tùy chọn/Mở rộng - Có thể thực hiện hoặc không).
- `<<interface>>`: 인터페이스 정의. (Định nghĩa Interface).
- `<<exception>>`: 예외 정의. (Định nghĩa Ngoại lệ).
- `<<constructor>>`: 생성자 역할. (Đóng vai trò Hàm khởi tạo).

### 순차 다이어그램 심화 (Sequence Diagram chi tiết)
- **생명선 (Lifeline):** 객체가 메모리에 존재하는 기간 (Đường nét đứt sổ dọc xuống).
- **실행 상자 (Active Box):** 객체가 메시지를 주고받으며 구동되고 있음을 표현 (Hình chữ nhật nằm trên đường sinh mệnh).

### 사용자 인터페이스(UI) 특성 (Đặc tính của UI)
- 소프트웨어 영역 중 변경이 가장 많이 발생한다. (Là phần thường xuyên bị thay đổi nhất trong phần mềm).
- 최소한의 노력으로 원하는 결과를 얻을 수 있게 한다. (Giúp user đạt kết quả mong muốn với nỗ lực ít nhất).

---

## 4. UML (Unified Modeling Language)
- **개념**: Ngôn ngữ mô hình hóa hướng đối tượng chuẩn.
- **구성요소**: 사물 (Things), 관계 (Relationships), 다이어그램 (Diagrams).
- **관계 (Relationships)**: 
  - 연관 (Association), 의존 (Dependency), 집합 (Aggregation), 포함 (Composition), 일반화 (Generalization - Kế thừa), 실체화 (Realization - Interface).
- **다이어그램 (Diagrams)**:
  - **구조적/정적 (Structural/Static)**: Class, Object, Component, Deployment, Composite Structure, Package.
  - **행위적/동적 (Behavioral/Dynamic)**: Use Case, Sequence, Communication, State, Activity, Timing.
- 💡 **Mẹo ghi nhớ**: 
  - 정적 다이어그램: 클/객/컴/배/복/패 (Class, Object, Component, Deployment, Composite, Package)
  - 동적 다이어그램: 유/순/커/상/활/타 (Use case, Sequence, Comm, State, Activity, Timing)

---

## 5. UML 구성요소 상세 (UML Components Detail)
- **클래스 다이어그램 (Class Diagram)**: Class Name, Attribute, Operation.
  - 접근 제어자 (Access Modifier): `+` (Public), `-` (Private), `#` (Protected), `~` (Package).
- **유스케이스 다이어그램 (Use Case Diagram)**: System, Use Case, Actor.
  - Quan hệ: `<<include>>` (Bắt buộc), `<<extend>>` (Tùy chọn), Generalization (Kế thừa).
- **순차 다이어그램 (Sequence Diagram)**: Object, Lifeline, Activation, Message, Self-Message.
  - Thể hiện sự tương tác theo thời gian.

---

## 7. UML 심화 (Advanced UML)
- Do OMG chuẩn hóa từ phương pháp của Rumbaugh, Booch, Jacobson.
- **다이어그램 (Diagrams)**:
  - 구조적 (Structural / Tĩnh): Class, Object, Component, Deployment, Composite, Package.
  - 행위적 (Behavioral / Động): Use Case, Sequence, Communication, State, Activity, Timing.
- **스테레오 타입 (Stereotype)**: Mở rộng UML bằng dấu `<< >>` (Guillemet). Ví dụ: `<<include>>`, `<<extend>>`.

---

## 4. 사용자 인터페이스 (Giao diện người dùng - UI)

### 020. 사용자 인터페이스의 특징 (Đặc điểm của giao diện người dùng)
- 사용자의 편리성과 가독성을 높여준다. (Tăng tính tiện lợi và khả năng đọc cho người dùng.)
- 작업 시간을 단축시킨다. (Rút ngắn thời gian làm việc.)
- 업무에 대한 이해도를 높여준다. (Tăng cường sự hiểu biết về công việc.)
- 사용자 중심으로 설계되어 있다. (Được thiết kế lấy người dùng làm trung tâm.)

### 021. 사용자 인터페이스의 구분 (Phân loại giao diện người dùng)
- CLI (Command Line Interface): 명령과 출력이 텍스트 형태로 이뤄지는 인터페이스 (Giao diện mà lệnh và đầu ra đều dưới dạng văn bản - VD: CMD, Terminal).
- GUI (Graphical User Interface): 아이콘이나 메뉴를 마우스로 선택하여 작업을 수행하는 그래픽 환경의 인터페이스 (Giao diện môi trường đồ họa, dùng chuột chọn icon/menu - VD: Windows, MacOS).
- NUI (Natural User Interface): 사용자의 말이나 행동으로 기기를 조작하는 인터페이스 (Giao diện thao tác thiết bị bằng lời nói hoặc hành động của người dùng - VD: Siri, Kinect).

### 022. 사용자 인터페이스의 기본 원칙 (Nguyên tắc cơ bản của UI)
- 직관성 (Tính trực quan): 누구나 쉽게 이해하고 사용할 수 있어야 한다. (Bất kỳ ai cũng có thể dễ dàng hiểu và sử dụng.)
- 유효성 (Tính hữu hiệu): 사용자의 목적을 정확하고 완벽하게 달성해야 한다. (Phải đạt được mục đích của người dùng một cách chính xác và hoàn hảo.)
- 학습성 (Tính học hỏi): 누구나 쉽게 배우고 익힐 수 있어야 한다. (Bất kỳ ai cũng có thể dễ dàng học và làm quen.)
- 유연성 (Tính linh hoạt): 요구사항을 최대한 수용하며, 실수를 방지. (Tính linh hoạt, tối đa hóa việc đáp ứng yêu cầu người dùng).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **THHN** (Trực - Hữu - Học - Nhu): **Trực Học Hằng Ngày**.

### 023. 목업 (Mockup)
- 와이어프레임보다 좀 더 실제 화면과 유사하게 만든 정적인 형태의 모형이다. (Là mô hình dạng tĩnh, được làm giống với màn hình thực tế hơn so với Wireframe.)
- 시각적으로만 구성 요소를 배치하는 것으로 실제로 구현되지는 않는다. (Chỉ bố trí các thành phần về mặt thị giác chứ thực tế không hoạt động/code chưa chạy.)
- **Ví dụ (Example):** Dùng Figma vẽ ra một màn hình app đẹp long lanh, nhưng bấm vào các nút không có phản hồi logic gì, đó là Mockup.

---

## 1. 사용자 인터페이스 (User Interface - UI)
- **UI 유형 (UI Types)**: 
  - CLI (Dòng lệnh), GUI (Đồ họa), NUI (Cử chỉ tự nhiên như chạm, vuốt), OUI (Hữu cơ).
  - **모바일 제스처 (Mobile Gestures)**: Tap (Chạm), Double Tap, Drag (Kéo), Pan (Di chuyển liên tục), Press (Nhấn giữ), Flick (Vuốt nhanh), Pinch (Phóng to/thu nhỏ bằng 2 ngón).
- **UI 기본 원칙 (4 Principles)**:
  - **직관성 (Intuitiveness)**: Dễ hiểu, trực quan.
  - **유효성 (Efficiency)**: Đạt được mục tiêu chính xác.
  - **학습성 (Learnability)**: Dễ học.
  - **유연성 (Flexibility)**: Linh hoạt, giảm thiểu lỗi.
  - 💡 **Mẹo ghi nhớ**: T/H/H/N -> **Trực Học Hằng Ngày**
- **UI 설계 도구 (UI Design Tools)**:
  - **와이어프레임 (Wireframe)**: Khung xương (Tĩnh).
  - **목업 (Mockup)**: Thiết kế tĩnh, giống thật nhất.
  - **스토리보드 (Storyboard)**: Bản hướng dẫn chi tiết, có luồng di chuyển.
  - **프로토타입 (Prototype)**: Mô hình động, có thể tương tác.

---
# Chapter 3. 애플리케이션 설계 (Application Design)

---

## 12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)

### 사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)
- **VUI (Voice User Interface):** 사람의 음성으로 기기를 조작하는 인터페이스. (Giao diện điều khiển bằng giọng nói - VD: Bixby, Alexa).
- **OUI (Organic User Interface):** 모든 사물과 사용자 간의 상호작용을 위한 인터페이스 (사물 인터넷, VR, AR, MR 등). (Giao diện hữu cơ, tương tác vật lý/thực tế ảo).

### 사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)
- **사용자 중심 (User-centric):** 실사용자에 대한 이해가 바탕이 되어야 함. (Dựa trên sự hiểu biết về người dùng thực tế).
- **사용성 (Usability):** 설계 시 가장 우선적으로 고려해야 함. (Ưu tiên hàng đầu khi thiết kế - dễ hiểu, dễ dùng).
- **심미성 (Aesthetics):** 디자인적으로 완성도 높게 그래픽 요소 배치. (Bố trí đồ họa thẩm mỹ cao).
- **오류 발생 해결 (Error Recovery):** 오류 발생 시 쉽게 인지하고 해결할 수 있도록 설계. (Giúp user dễ nhận biết và khắc phục lỗi).

### UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)
- **와이어프레임 (Wireframe):** 개략적인 레이아웃이나 뼈대 설계 (손그림, 스케치). (Khung xương, layout sơ lược).
- **목업 (Mockup):** 실제 화면과 유사하게 만든 정적인 형태의 모형. (Mô hình tĩnh giống thật nhưng không chạy được logic).
- **스토리보드 (Storyboard):** 와이어프레임 + 콘텐츠 설명 + 페이지 이동 흐름. 디자이너/개발자의 최종 참고 문서. (Tài liệu chi tiết nhất gồm wireframe + mô tả nội dung + luồng di chuyển).
- **프로토타입 (Prototype):** 인터랙션을 적용하여 실제 구현된 것처럼 테스트 가능한 동적인 모형. (Mô hình động có tương tác, test thử được).
- **유스케이스 (Use Case):** 사용자 측면의 요구사항 기술. (Mô tả yêu cầu chức năng từ góc nhìn người dùng).

### UI 주요 요소 (Các thành phần UI)
- **체크 박스 (Check Box):** 1개 이상의 값을 선택할 수 있는 버튼. (Chọn nhiều - Multiple choice).
- **라디오 버튼 (Radio Button):** 여러 항목 중 하나만 선택할 수 있는 버튼. (Chọn 1 - Single choice).
- **텍스트 박스 (Text Box):** 데이터를 입력/수정하는 상자. (Hộp nhập văn bản).
- **콤보 상자 (Combo Box):** 목록에서 선택하거나 새로 입력할 수 있는 상자. (Dropdown list có thể gõ thêm text).
- **목록 상자 (List Box):** 목록만 표시하고 새로 입력할 수는 없는 상자. (Chỉ chọn từ list có sẵn, không được gõ).

### 상위 설계와 하위 설계 (Thiết kế bậc cao và Bậc thấp)
- **상위 설계 (High-level Design):** 아키텍처 설계, 예비 설계. 대상: 시스템 전체 구조 (DB, Interface). (Thiết kế tổng thể, kiến trúc).
- **하위 설계 (Low-level Design):** 모듈 설계, 상세 설계. 대상: 시스템 내부 구조, 컴포넌트, 알고리즘. (Thiết kế chi tiết module, thuật toán).

### 소프트웨어 아키텍처 품질 속성 (Thuộc tính chất lượng Kiến trúc)
- **시스템 측면 (Hệ thống):** 성능, 보안, 가용성, 기능성. (Hiệu năng, bảo mật...).
- **비즈니스 측면 (Kinh doanh):** 시장 적시성 (Time-to-market), 비용과 혜택. (Thời điểm tung ra thị trường, chi phí).
- **아키텍처 측면 (Kiến trúc):** 개념적 무결성, 정확성, 완결성. (Tính toàn vẹn, chính xác).

### 협약(Contract)에 의한 설계 (Thiết kế theo hợp đồng)
- 컴포넌트의 정확한 인터페이스를 명세하는 방법. (Đặc tả chính xác interface của component).
- **선행 조건 (Precondition):** 오퍼레이션이 호출되기 전에 참이 되어야 할 조건. (Điều kiện bắt buộc trước khi chạy hàm).
- **결과 조건 (Postcondition):** 오퍼레이션이 수행된 후 만족되어야 할 조건. (Điều kiện phải đạt sau khi chạy hàm).
- **불변 조건 (Invariant):** 오퍼레이션이 실행되는 동안 항상 만족되어야 할 조건. (Điều kiện luôn đúng trong suốt quá trình chạy).

---

## 5. 요구공학 (Requirements Engineering)
- **도출 (Elicitation)**: Lặp đi lặp lại trong suốt vòng đời (SDLC).
- **분석 (Analysis)**: Giải quyết xung đột (중재), dùng DFD, DD.
- **명세 (Specification)**: Viết tài liệu (Mini-Spec), đảm bảo tính truy xuất (추적성).
  - 정형 (Toán học, VDM) vs 비정형 (Ngôn ngữ tự nhiên, ERD).
- **확인 (Validation)**: 
  - 확인 (Validation): Có đúng sản phẩm khách cần không? (Right product).
  - 검증 (Verification): Có làm đúng quy trình không? (Product right).
  - Cần quản lý cấu hình (형상 관리).

---

## 8. UI 및 UX, HCI (UI, UX, HCI)
- **UI 유형**: CLI (Văn bản), GUI (Đồ họa), NUI (Tự nhiên - Giọng nói/Hành động), OUI (Hữu cơ - Gắn với đồ vật vật lý).
- **UI 설계 도구**: Wireframe (Khung xương), Mockup (Mô hình tĩnh giống thật), Storyboard (Kịch bản chi tiết), Prototype (Mô hình động tương tác).
- **HCI (Human Computer Interaction)**: Nghiên cứu tương tác người-máy tính để mang lại trải nghiệm tốt nhất (UX).
- **UX (User Experience - Trải nghiệm người dùng)**:
  - **주관성 (Subjectivity)**: Tính chủ quan.
  - **정황성 (Contextuality)**: Phụ thuộc vào hoàn cảnh (thời gian, địa điểm).
  - **총체성 (Holistic)**: Trải nghiệm tổng thể.
- **감성공학 (Affective Engineering)**: Khoa học kết hợp cảm xúc con người vào thiết kế (Dựa trên -> Thực hiện -> Ứng dụng).

---

## 5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)

### 024. ISO/IEC 9126의 품질 특성 (Đặc tính chất lượng theo ISO/IEC 9126)
- 기능성 (Functionality): 요구사항을 정확하게 만족하는 기능을 제공하는지 여부를 나타냄. (Cung cấp chức năng thỏa mãn chính xác các yêu cầu không.)
- 신뢰성 (Reliability): 요구된 기능을 오류 없이 수행할 수 있는 정도를 나타냄. (Mức độ thực hiện chức năng yêu cầu mà không có lỗi.)
- 사용성 (Usability): 사용자가 쉽게 배우고 사용할 수 있는 정도를 나타냄. (Mức độ người dùng dễ dàng học và sử dụng.)
- 이식성 (Portability): 다른 환경에서도 얼마나 쉽게 적용할 수 있는지 정도를 나타냄. (Mức độ dễ dàng áp dụng trong các môi trường khác nhau.)
- **Ví dụ (Example):** App đang chạy trên Android, mang sang iOS chạy vẫn tốt mà không cần sửa nhiều -> Tính 이식성 (Portability) cao.

### 025. 소프트웨어 아키텍처의 설계 과정 (Quá trình thiết kế Kiến trúc phần mềm)
- 설계 목표 설정 (Thiết lập mục tiêu thiết kế) → 시스템 타입 결정 (Quyết định loại hệ thống) → 아키텍처 패턴 적용 (Áp dụng pattern kiến trúc) → 서브시스템 구체화 (Cụ thể hóa hệ thống con) → 검토 (Xem xét/Đánh giá).

### 026. 모듈화 (Modularization / Mô-đun hóa)
- 기능의 분리가 가능하여 인터페이스가 단순해진다. (Có thể phân tách các chức năng nên giao diện trở nên đơn giản.)
- 프로그램의 효율적인 관리가 가능하다. (Có thể quản lý chương trình một cách hiệu quả.)
- 오류의 파급 효과를 최소화할 수 있다. (Có thể giảm thiểu tác động lan truyền của lỗi.)
- 모듈의 크기를 너무 작게 나누면 개수가 많아져 모듈간의 통합 비용이 많이 들고, 너무 크게 나누면 개수가 적어 통합 비용은 적게 들지만 모듈 하나의 개발 비용이 많이 든다. (Nếu chia module quá nhỏ, số lượng nhiều, chi phí tích hợp sẽ cao. Nếu chia quá lớn, chi phí tích hợp ít nhưng chi phí phát triển 1 module lại cao.)
- **Ví dụ (Example):** Thay vì viết toàn bộ chức năng vào 1 file code, ta chia ra `login.py`, `payment.py`. Lỗi ở payment không làm sập login (giảm thiểu 파급 효과).

### 027. 추상화의 유형 (Các loại trừu tượng hóa)
- 과정 추상화 (Trừu tượng hóa quá trình)
- 데이터(자료) 추상화 (Trừu tượng hóa dữ liệu)
- 제어 추상화 (Trừu tượng hóa điều khiển)

### 028. 정보 은닉 (Information Hiding / Che giấu thông tin)
- 한 모듈 내부에 포함된 절차와 자료들의 정보가 감추어져 다른 모듈이 접근하거나 변경하지 못하도록 하는 기법이다. (Kỹ thuật che giấu thông tin về thủ tục và dữ liệu bên trong một module để các module khác không thể truy cập hoặc sửa đổi.)
- 모듈을 독립적으로 수행할 수 있다. (Có thể thực thi module một cách độc lập.)
- 수정, 시험, 유지보수가 용이하다. (Dễ dàng sửa đổi, kiểm thử, bảo trì.)
- 정보 은닉을 표기할 때 private의 의미는 은닉이다. (Khi ký hiệu che giấu thông tin, 'private' mang ý nghĩa là che giấu.)
- **Ví dụ (Example):** Trong OOP, khai báo các biến là `private` và chỉ cho phép truy cập qua `getter/setter`.

### 029. 파이프 - 필터 패턴 (Pipe-Filter Pattern)
- 시스템의 처리 결과물을 파이프를 통해 전달받아 처리한 후 그 결과물을 다시 파이프를 통해 다음 시스템으로 넘겨주는 패턴이다. (Pattern nhận kết quả xử lý qua Pipe, xử lý (Filter) rồi lại chuyển kết quả đó qua Pipe cho hệ thống tiếp theo.)
- 데이터 변환으로 인한 오버헤드가 발생한다. (Phát sinh overhead do chuyển đổi dữ liệu.)
- **Ví dụ (Example):** Câu lệnh trong Linux: `ls | grep "txt" | sort`. Ký tự `|` chính là Pipe, còn `grep`, `sort` là các Filter.

### 030. MVC (Model-View-Controller) 패턴
- 모델 (Model): 서브시스템의 핵심 기능과 데이터를 보관함. (Lưu trữ chức năng cốt lõi và dữ liệu - Logic nghiệp vụ.)
- 뷰 (View): 사용자에게 정보를 표시함. (Hiển thị thông tin cho người dùng - UI.)
- 컨트롤러 (Controller): 사용자로부터 입력된 변경 요청을 처리하기 위해 모델에게 명령을 보냄. (Xử lý yêu cầu thay đổi từ người dùng và gửi lệnh cho Model.)

### 039. 모듈 (Module)
- 모듈화를 통해 분리된 시스템의 각 기능들이다. (Là các chức năng của hệ thống được tách ra thông qua quá trình module hóa.)
- 단독으로 컴파일이 가능하다. (Có thể biên dịch độc lập.)
- 재사용 할 수 있다. (Có thể tái sử dụng.)
- 다른 모듈에서의 접근이 가능하다. (Các module khác có thể truy cập được.)

### 040 & 041. 결합도 (Coupling) 의 종류와 정도 (Các loại Độ kết dính / Mức độ từ Yếu → Mạnh)
- *Kết dính càng YẾU (약함) càng TỐT, càng MẠNH (강함) càng XẤU.*
- **자료 (Data) 결합도 (Yếu nhất - Tốt nhất):** 모듈 간의 인터페이스가 자료 요소로만 구성될 때. (Chỉ truyền dữ liệu đơn giản giữa các module).
- **스탬프 (Stamp) 결합도:** 배열이나 레코드 등의 자료 구조가 전달될 때. (Truyền cấu trúc dữ liệu như mảng, bản ghi).
- **제어 (Control) 결합도:** 제어 신호를 이용하여 통신하거나 제어 요소를 전달. (Truyền cờ điều khiển - control flag/signal).
- **외부 (External) 결합도:** 데이터(변수)를 외부의 다른 모듈에서 참조할 때. (Tham chiếu biến toàn cục bên ngoài).
- **공통 (Common) 결합도:** 공유되는 공통 데이터 영역을 여러 모듈이 사용할 때. (Nhiều module cùng dùng chung một vùng dữ liệu chung - global data).
- **내용 (Content) 결합도 (Mạnh nhất - Xấu nhất):** 한 모듈이 다른 모듈의 내부 기능 및 그 내부 자료를 직접 참조하거나 수정. (Module này trực tiếp can thiệp nội bộ module kia).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TSCNCN** (Tư - Stamp - Chế - Ngoại - Công - Nội): **Tính Sao Cho Nhẹ Cả Người**. (Từ Tốt nhất -> Xấu nhất).

### 043. 주요 응집도 (Cohesion)
- *Độ gắn kết nội bộ. Gắn kết càng MẠNH càng TỐT.*
- **기능적 (Functional) 응집도 (Mạnh nhất - Tốt nhất):** Tất cả các yếu tố bên trong đều hướng tới giải quyết một chức năng duy nhất.
- **순차적 (Sequential) 응집도:** Kết quả đầu ra của hoạt động này là đầu vào của hoạt động kia.
- **통신적 (Communication) 응집도:** Các hoạt động cùng sử dụng chung một dữ liệu đầu vào/ra.
- **절차적 (Procedural) 응집도:** 모듈 안의 구성 요소들이 그 기능을 순차적으로 수행할 경우. (Thực hiện tuần tự theo quy trình nhưng có thể không cùng dữ liệu).
- **시간적 (Temporal) 응집도:** 특정 시간에 처리되는 몇 개의 기능을 모아 하나의 모듈로 작성. (Nhóm các chức năng cần thực hiện cùng một thời điểm, ví dụ: Module khởi tạo hệ thống).
- **논리적 (Logical) 응집도:** Các chức năng có cùng logic được nhóm lại.
- **우연적 (Coincidental) 응집도 (Yếu nhất - Xấu nhất):** 각 구성 요소들이 서로 관련 없는 요소로만 구성된 경우. (Nhóm các thành phần chẳng liên quan gì với nhau).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KTTTTLN** (Kỳ - Thuận - Thông - Tiết - Thời - Luận - Ngẫu): **Không Thể Tin Thằng Trẻ Làm Ngốc**. (Từ Tốt nhất -> Xấu nhất).

### 044. 팬인(Fan-In) / 팬아웃(Fan-Out)
- 팬인 (Fan-In): 어떤 모듈을 제어(호출)하는 모듈의 수. (Số lượng các module gọi/điều khiển module đó -> Mũi tên TRỎ VÀO nó).
- 팬아웃 (Fan-Out): 어떤 모듈에 의해 제어(호출)되는 모듈의 수. (Số lượng các module mà module đó gọi/điều khiển -> Mũi tên TRỎ RA từ nó).
- **Nguyên tắc thiết kế tốt:** Fan-In phải CAO (được dùng lại nhiều), Fan-Out phải THẤP (ít phụ thuộc vào nhiều thằng khác).

---

## 13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)

### ISO/IEC 9126 하위 품질 특성 (Đặc tính con của ISO/IEC 9126)
- *Đây là phần rất hay thi, cần ghi nhớ chi tiết.*
- **기능성 (Functionality):** 적절성 (Suitability), 정밀성 (Accuracy), 상호 운용성 (Interoperability), 보안성 (Security), 준수성 (Compliance).
- **신뢰성 (Reliability):** 성숙성 (Maturity), 고장 허용성 (Fault Tolerance), 회복성 (Recoverability).
- **사용성 (Usability):** 이해성 (Understandability), 학습성 (Learnability), 운용성 (Operability), 친밀성 (Attractiveness).
- **효율성 (Efficiency):** 시간 효율성 (Time Behaviour), 자원 효율성 (Resource Behaviour).
- **유지 보수성 (Maintainability):** 분석성 (Analyzability), 변경성 (Changeability), 안정성 (Stability), 시험성 (Testability).
- **이식성 (Portability):** 적용성 (Adaptability), 설치성 (Installability), 대체성 (Replaceability), 공존성 (Co-existence).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KTSHDD** (Kỳ - Tín - Sử - Hiệu - Duy - Di): **Không Tin Sẽ Hư Dần Dần** (Tên 6 đặc tính chính).
  - 유지 보수성: **분변안시** (Phân - Biến - An - Thử).

### 관련 품질 표준 (Các tiêu chuẩn ISO khác)
- **ISO/IEC 25010:** 2011년 9126을 개정한 최신 표준. (Bản cập nhật của 9126).
- **ISO/IEC 12119:** 테스트 절차를 포함한 품질 표준. (Bao gồm quy trình test).
- **ISO/IEC 14598:** 평가자별 제품 평가 활동 규정. (Quy định hoạt động đánh giá).

### 기타 아키텍처 패턴 (Các mẫu kiến trúc bổ sung)
- **마스터-슬레이브 패턴 (Master-Slave):** 마스터가 작업을 분할하고 슬레이브가 처리 결과를 돌려주는 패턴 (장애 허용 시스템, 병렬 컴퓨팅). (Master chia việc, Slave làm rồi trả kết quả -> Hệ thống tính toán song song).
- **브로커 패턴 (Broker):** 사용자가 요청하면 브로커가 적합한 컴포넌트를 연결해 줌 (분산 환경). (Môi giới kết nối User với Component phù hợp -> Hệ thống phân tán).
- **피어-투-피어 패턴 (Peer-To-Peer / P2P):** 각 피어가 클라이언트도 되고 서버도 됨. (Mỗi node vừa là Client vừa là Server).
- **이벤트-버스 패턴 (Event-Bus):** 소스가 이벤트를 발행(Publish)하면 리스너가 구독(Subscribe)하여 처리. (Mô hình Pub/Sub).
- **블랙보드 패턴 (Blackboard):** 모든 컴포넌트가 공유 데이터 저장소(블랙보드)에 접근 (음성 인식, 신호 해석). (Bảng đen dùng chung, các AI agents tự do truy cập -> Nhận diện giọng nói, xử lý tín hiệu).

---

## 1. 소프트웨어 아키텍처 (Software Architecture)
- **상위 설계 (High-level)**: 아키텍처 (Architecture), 자료구조 (Data Structure), 인터페이스 (Interface).
- **하위 설계 (Low-level)**: 모듈 (Module), 프로시저 (Procedure).
- **아키텍처 패턴 (Architecture Patterns)**:
  - **레이어 패턴 (Layers)**: Chia thành các tầng (OSI 7 layer).
  - **클라이언트-서버 패턴 (Client-Server)**: Máy khách - Máy chủ.
  - **파이프-필터 패턴 (Pipe-Filter)**: Dữ liệu qua các bộ lọc liên tiếp (Ví dụ: Unix shell).
  - **MVC 패턴**: Model (Dữ liệu), View (Giao diện), Controller (Điều khiển).
  - **브로커 패턴 (Broker)**: Có môi giới ở giữa.
  - **마스터-슬레이브 (Master-Slave)**: Một chủ, nhiều tớ (Hệ thống thời gian thực).

---

## 6. 객체지향 (Hướng Đối Tượng - OOP)

### 031. 메시지 (Message)
- 객체에게 어떤 행위를 하도록 지시하는 명령 또는 요구사항이다. (Là lệnh hoặc yêu cầu chỉ thị cho đối tượng thực hiện một hành vi nào đó.)
- 객체들 간에 상호 작용을 하는 데 사용되는 수단이다. (Là phương tiện dùng để tương tác giữa các đối tượng.)

### 032. 클래스 (Class)
- 공통된 속성과 연산(행위)을 갖는 객체의 집합이다. (Là tập hợp các đối tượng có chung thuộc tính và phép toán (hành vi).)
- 클래스에 속한 각각의 객체를 인스턴스(Instance)라 한다. (Mỗi đối tượng thuộc một class được gọi là Thực thể - Instance).
- 객체지향 프로그램에서 데이터를 추상화하는 단위이다. (Là đơn vị trừu tượng hóa dữ liệu trong lập trình OOP.)

### 033. 캡슐화 (Encapsulation / Đóng gói)
- 데이터와 데이터를 처리하는 함수를 하나로 묶는 것을 의미한다. (Việc bó buộc dữ liệu và hàm xử lý dữ liệu đó thành một khối.)
- 외부 모듈의 변경으로 인한 파급 효과가 적다. (Giảm thiểu hiệu ứng lan truyền khi module bên ngoài thay đổi.)
- 인터페이스가 단순화된다. (Giao diện trở nên đơn giản.)
- 재사용이 용이하다. (Dễ dàng tái sử dụng.)
- **Ví dụ (Example):** Một viên thuốc nhộng (capsule) chứa nhiều bột thuốc bên trong, người dùng chỉ việc uống viên nhộng mà không cần biết tỷ lệ bột bên trong.

### 034. 상속 (Inheritance / Kế thừa)
- 상위 클래스(부모 클래스)의 모든 속성과 연산을 하위 클래스(자식 클래스)가 물려받는 것이다. (Lớp con kế thừa toàn bộ thuộc tính và phương thức của lớp cha.)

### 035. 다형성 (Polymorphism / Đa hình)
- 오버로딩 (Overloading - Nạp chồng): 메소드의 이름은 같지만 인수를 받는 자료형과 개수를 달리하여 여러 기능을 정의할 수 있음. (Cùng tên hàm nhưng khác kiểu/số lượng tham số -> Định nghĩa nhiều chức năng).
- 오버라이딩 (Overriding - Ghi đè): 메소드의 이름은 같지만 메소드 안의 실행 코드를 달리하여 자식 클래스에서 재정의해서 사용할 수 있음. (Cùng tên hàm, định nghĩa lại nội dung code ở lớp con).
- **Ví dụ (Example):** Hàm `add(int a, int b)` và `add(float a, float b)` là Overloading. Lớp Mèo `speak()` kêu Meo, lớp Chó `speak()` kêu Gâu là Overriding.

### 036. 객체지향 분석 방법론 - Coad와 Yourdon 방법
- E-R 다이어그램을 사용하여 객체의 행위를 모델링 한다. (Sử dụng biểu đồ E-R để mô hình hóa hành vi đối tượng.)
- 객체 식별, 구조 식별, 주제 정의, 속성과 인스턴스 연결 정의, 연산과 메시지 연결 정의 등의 과정으로 구성하는 기법이다. (Quy trình gồm: Nhận diện đối tượng, Nhận diện cấu trúc, Định nghĩa chủ đề, Định nghĩa thuộc tính/liên kết instance, Định nghĩa phép toán/thông điệp).

### 037. 럼바우(Rumbaugh)의 분석 기법 (Kỹ thuật phân tích của Rumbaugh)
- 객체(Object) 모델링: 정보 모델링이라고도 하며, 객체들 간의 관계를 규정하여 객체 다이어그램으로 표시하는 것. (Mô hình hóa đối tượng/thông tin: Xác định mối quan hệ giữa các đối tượng và hiển thị bằng Object Diagram).
- 동적(Dynamic) 모델링: 상태 다이어그램을 이용하여 객체들 간의 동적인 행위를 표현하는 모델링. (Mô hình hóa động: Thể hiện hành vi động giữa các đối tượng bằng State Diagram).
- 기능(Functional) 모델링: 자료 흐름도를 이용하여 자료 흐름을 표현한 모델링. (Mô hình hóa chức năng: Thể hiện luồng dữ liệu bằng DFD - Data Flow Diagram).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KĐC** (Khách - Động - Cơ): **Không Đợi Chờ** (Khách thể - Động lực - Cơ năng). (O-D-F)

### 038. 객체지향 설계 원칙 (SOLID 원칙) (Các nguyên tắc thiết kế OOP)
- 단일 책임 원칙 (SRP - Single Responsibility Principle): 객체는 단 하나의 책임만 가져야 한다는 원칙. (Mỗi đối tượng chỉ có MỘT trách nhiệm duy nhất.)
- 개방-폐쇄 원칙 (OCP - Open-Closed Principle): 기존의 코드를 변경하지 않고 기능을 추가할 수 있도록 설계해야 한다는 원칙. (Mở cho việc mở rộng, Đóng cho việc sửa đổi.)
- 리스코프 치환 원칙 (LSP - Liskov Substitution Principle): 자식 클래스는 최소한 자신의 부모 클래스에서 가능한 행위는 수행할 수 있어야 한다는 설계 원칙. (Lớp con có thể thay thế hoàn toàn lớp cha mà không làm hỏng logic.)
- 인터페이스 분리 원칙 (ISP - Interface Segregation Principle): 자신이 사용하지 않는 인터페이스와 의존 관계를 맺거나 영향을 받지 않아야 한다는 원칙. (Nên tách nhỏ Interface, không ép client implement những phương thức không dùng tới.)
- 의존 역전 원칙 (DIP - Dependency Inversion Principle): 추상성이 낮은 클래스보다 추상성이 높은 클래스와 의존 관계를 맺어야 한다는 원칙. (Module cấp cao không nên phụ thuộc module cấp thấp, cả 2 nên phụ thuộc vào abstraction/interface.)
- 💡 **Mẹo ghi nhớ (Mnemonic):** Tên các chữ cái đầu tiếng Anh tạo thành chữ **S-O-L-I-D**.

---

## 14. 객체지향 심화 (OOP chuyên sâu)

### 다형성 (Polymorphism) 추가 설명
- **오버로딩 (Overloading):** 인수를 받는 자료형과 개수를 달리하여 여러 기능을 정의. (Cùng tên hàm, khác tham số).
- **오버라이딩 (Overriding / 메소드 재정의):** 상위 클래스의 메소드 안의 코드를 자식 클래스에서 재정의. (Lớp con định nghĩa lại hàm của lớp cha).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **Over-load** = Chở thêm đồ (Thêm tham số). **Over-ride** = Lái đè lên vết xe cũ (Ghi đè nội dung hàm).

---

## 15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)

### 객체지향 분석 방법론 종류 (Các phương pháp phân tích OOP)
- **Rumbaugh (럼바우):** 객체(Object), 동적(Dynamic), 기능(Functional) 모델로 나누어 분석. (Chia làm 3 mô hình).
- **Booch (부치):** 미시적(Micro) 개발과 거시적(Macro) 개발 프로세스 모두 사용. (Dùng cả quy trình vĩ mô và vi mô).
- **Jacobson (제이콥슨):** Use Case(유스케이스)를 강조. (Nhấn mạnh vào Use Case).
- **Coad와 Yourdon:** E-R 다이어그램 사용. (Dùng sơ đồ ER).
- **Wirfs-Brock:** 분석과 설계 간 구분이 없고 연속적으로 수행. (Không phân biệt rõ phân tích và thiết kế, làm liên tục).
- 💡 **Mẹo ghi nhớ (Mnemonic):** R-O, B-M, J-U, C-E, W-L -> **Ra Ôm Bạn Mới, Giữ Út, Cho Em Vui Lây** (Rumbaugh-Object, Booch-Micro, Jacobson-Use case, Coad-ER, Wirfs-Liên tục).

### 공통 모듈 명세 기법 (Kỹ thuật đặc tả Module chung)
- **정확성 (Correctness):** 기능이 필요하다는 것을 알 수 있도록 정확히 작성. (Chính xác, biết rõ cần thiết).
- **명확성 (Clarity):** 중의적으로 해석되지 않도록 명확하게. (Rõ ràng, không hiểu 2 nghĩa).
- **완전성 (Completeness):** 구현에 필요한 모든 것을 기술. (Đầy đủ mọi thứ cần thiết).
- **일관성 (Consistency):** 기능들 간 상호 충돌이 발생하지 않도록. (Nhất quán, không xung đột).
- **추적성 (Traceability):** 요구사항 출처, 관련 시스템 등 관계 파악. (Có thể truy xuất nguồn gốc).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CMHNT** (Chính - Minh - Hoàn - Nhất - Truy): **Chỉ Mong Học Nhất Trường**.

### 코드(Code)의 주요 기능 (Chức năng chính của Code)
- 식별 기능 (Nhận diện), 분류 기능 (Phân loại), 배열 기능 (Sắp xếp), 표준화 기능 (Chuẩn hóa), 간소화 기능 (Đơn giản hóa).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TPBTG** (Thức - Phân - Bài - Tiêu - Giản): **Thích Phá Bài Thì Giảm**.

### 코드의 종류 심화 (Các loại Code chi tiết)
- **순차 코드 (Sequence Code):** 1, 2, 3... (Theo thứ tự).
- **블록 코드 (Block Code):** 공통성 있는 것끼리 블록으로 구분 (1000~1100: Phòng Nhân sự, 1101~1200: Phòng IT).
- **10진 코드 (Decimal Code):** 0~9 분할 반복 (Ví dụ: Mã phân loại sách thư viện Dewey).
- **그룹 분류 코드 (Group Classification):** 대/중/소 분류 (1-01-001).
- **연상 코드 (Mnemonic Code):** 명칭/약호와 관계있는 문자/숫자 (TV-40). (Gợi nhớ).
- **표의 숫자 코드 (Significant Digit):** 물리적 수치 적용 (120-720).
- **합성 코드 (Combined Code):** 2개 이상 코드 조합 (KE-711).

---

## 2. 객체지향 (OOP - Object Oriented Programming)
- **구성요소**: 클래스 (Class), 객체 (Object), 메서드 (Method), 메시지 (Message), 인스턴스 (Instance), 속성 (Property).
- **객체지향 기법 (OOP Techniques)**:
  - **캡슐화 (Encapsulation)**: Đóng gói dữ liệu và phương thức, giảm kết dính (Coupling).
  - **정보 은닉 (Information Hiding)**: Giấu thông tin chi tiết.
  - **다형성 (Polymorphism)**: Đa hình (Overloading - Cùng tên khác tham số, Overriding - Ghi đè phương thức cha).
- **객체지향 설계 원칙 (SOLID)**:
  - **S (SRP)**: Đơn trách nhiệm (Một lớp một việc).
  - **O (OCP)**: Đóng-Mở (Mở rộng thì dễ, sửa đổi thì cấm).
  - **L (LSP)**: Thay thế Liskov (Lớp con thay thế được lớp cha).
  - **I (ISP)**: Phân tách Interface (Interface nhỏ gọn).
  - **D (DIP)**: Đảo ngược phụ thuộc (Phụ thuộc vào Interface, không phụ thuộc vào triển khai chi tiết).
- **분석 방법론 (OOA Methods)**:
  - **람바우 (Rumbaugh - OMT)**: 객체 모형 (Object) -> 동적 모형 (Dynamic) -> 기능 모형 (Functional - DFD). 
  - 💡 **Mẹo ghi nhớ**: K/Đ/C -> **Không Đợi Chờ**

---

## 1. 객체지향 설계 5대 원칙 (SOLID)
**개념 (Khái niệm):** 시스템의 변경이나 확장에 유연하게 대응하기 위해 지켜야 할 5가지 원칙 (5 nguyên tắc thiết kế hướng đối tượng giúp hệ thống linh hoạt trước các thay đổi và mở rộng).

*   **SRP (Single Responsibility Principle - 단일 책임 원칙):**
    *   **Korean:** 객체는 '단 하나의 책임'만 가져야 함. 클래스를 수정해야 할 이유는 단 하나여야 함.
    *   **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc Đơn trách nhiệm. Một đối tượng (hoặc lớp) chỉ nên có một trách nhiệm duy nhất. Lý do để sửa đổi một lớp chỉ nên có một.
    *   **Example:**
        *   *KR:* 보고서를 생성하는 클래스와 출력하는 클래스를 분리.
        *   *VN:* Tách biệt lớp tạo báo cáo và lớp in báo cáo, không để chung một lớp.
*   **OCP (Open-Closed Principle - 개방-폐쇄 원칙):**
    *   **Korean:** 기능 추가에는 열려(Open) 있어야 하고, 기존 코드 변경에는 닫혀(Closed) 있어야 함. 인터페이스로 캡슐화.
    *   **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc Đóng - Mở. Mở rộng chức năng thì dễ dàng (Open), nhưng không được sửa đổi mã nguồn hiện tại (Closed). Thường dùng Interface để đóng gói.
    *   **Example:**
        *   *KR:* 결제 수단(카드, 페이 등)을 인터페이스로 구현하여 새로운 결제 수단 추가 시 기존 코드 수정 없이 확장.
        *   *VN:* Dùng Interface cho phương thức thanh toán, khi thêm phương thức mới (ví dụ: ví điện tử) thì không cần sửa mã cũ.
*   **LSP (Liskov Substitution Principle - 리스코프 치환 원칙):**
    *   **Korean:** 자식 클래스는 최소한 부모 클래스의 행위를 수행할 수 있어야 함. 부모의 의도를 훼손하지 않고 확장.
    *   **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc Thay thế Liskov. Lớp con phải có thể thay thế lớp cha mà không làm hỏng tính đúng đắn của chương trình. Lớp con chỉ nên mở rộng, không làm sai lệch ý định của lớp cha.
    *   **Example:**
        *   *KR:* 새(Bird) 부모 클래스를 상속받은 펭귄(Penguin)이 날기(fly) 메서드를 가지면 LSP 위반.
        *   *VN:* Chim cánh cụt kế thừa từ lớp Chim, nhưng nếu gọi hàm bay() sẽ bị lỗi, vi phạm LSP. Cần thiết kế lại.
*   **ISP (Interface Segregation Principle - 인터페이스 분리 원칙):**
    *   **Korean:** 사용하지 않는 인터페이스에 의존하지 않도록 분리.
    *   **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc Phân tách Interface. Không nên ép các lớp phụ thuộc vào những interface mà chúng không sử dụng. Hãy chia nhỏ interface khổng lồ thành các interface cụ thể.
    *   **Example:**
        *   *KR:* 복합기 인터페이스를 프린터, 스캐너, 팩스 인터페이스로 분리.
        *   *VN:* Tách interface của máy photocopy đa năng thành các interface riêng: In, Quét, Fax.
*   **DIP (Dependency Inversion Principle - 의존 역전 원칙):**
    *   **Korean:** 구체적인 클래스보다 추상화된 클래스(인터페이스)에 의존해야 함.
    *   **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc Đảo ngược phụ thuộc. Các module cấp cao không nên phụ thuộc vào module cấp thấp, cả hai nên phụ thuộc vào abstractions (interface).
    *   **Example:**
        *   *KR:* 자동차가 스노우타이어(구체) 대신 타이어(추상) 인터페이스에 의존.
        *   *VN:* Lớp xe hơi phụ thuộc vào interface "Lốp xe" nói chung, thay vì phụ thuộc trực tiếp vào "Lốp đi tuyết".

💡 **Mẹo ghi nhớ (Mnemonics):** **SOLID** (S = Single, O = Open, L = Liskov, I = Interface, D = Dependency)

---

---

## 7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)

### NS 차트 (Nassi-Shneiderman Chart)
- 논리의 기술에 중점을 둔 도형을 이용한 표현 방법이다. (Là phương pháp biểu diễn bằng hình khối, trọng tâm vào việc mô tả logic.)
- 연속, 선택 및 다중 선택, 반복 등의 제어 논리 구조를 표현한다. (Thể hiện cấu trúc logic điều khiển như tuần tự, lựa chọn (if-else), đa lựa chọn (switch), lặp lại (while/for).)
- GOTO나 화살표를 사용하지 않는다. (Không sử dụng lệnh GOTO hay mũi tên.)
- 시각적으로 명확히 식별하는 데 적합하다. (Thích hợp để nhận diện rõ ràng về mặt thị giác.)
- 이해하기 쉽고, 코드 변환이 용이하다. (Dễ hiểu và dễ chuyển đổi thành code.)
- **Ví dụ (Example):** Dùng các khối hình chữ nhật xếp chồng lên nhau để biểu diễn một hàm tính toán thay vì dùng sơ đồ khối (Flowchart) có mũi tên rườm rà.

### 재사용 (Reuse / Tái sử dụng)
- 이미 개발된 기능을 새로운 시스템이나 기능 개발에 사용할 수 있는 정도를 의미한다. (Mức độ có thể sử dụng lại các chức năng đã phát triển cho hệ thống hoặc chức năng mới.)
- 재사용 규모에 따른 분류: 함수와 객체, 컴포넌트, 애플리케이션. (Phân loại theo quy mô: Hàm/Đối tượng, Component, Ứng dụng).

### 효과적인 모듈 설계 방안 (Phương án thiết kế module hiệu quả)
- 결합도는 줄이고 응집도는 높인다. (Giảm độ kết dính (Coupling) và tăng độ gắn kết (Cohesion).)
- 복잡도와 중복성을 줄인다. (Giảm độ phức tạp và sự trùng lặp.)
- 일관성을 유지시킨다. (Duy trì tính nhất quán.)
- 모듈의 기능은 지나치게 제한적이어서는 안 된다. (Chức năng của module không nên quá hạn hẹp.)
- 유지보수가 용이해야 한다. (Phải dễ dàng bảo trì.)
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CUTK** (Cao Ứng - Thấp Kết): **Cứ Ứng Thật Kỹ** -> 응집도 높게(Cohesion High), 결합도 낮게(Coupling Low).

### 주요 코드 (Các loại Code cơ bản)
- 순차 코드 (Sequence Code): 일정 기준에 따라서 차례로 일련번호를 부여하는 방법. (Gắn số thứ tự liên tiếp theo một tiêu chuẩn định sẵn - VD: 001, 002, 003).
- 표의 숫자 코드 (Significant Digit Code): 코드화 대상 항목의 중량, 면적, 용량 등의 물리적 수치를 적용시키는 방법. (Sử dụng trực tiếp các chỉ số vật lý như trọng lượng, kích thước vào mã - VD: Tivi 50 inch thì mã là TV-50).

---

## 3. 모듈 (Module)
- **결합도 (Coupling - Độ kết dính giữa các module)**: Càng thấp càng tốt.
  - 자료 (Data - Tốt nhất) < 스탬프 (Stamp) < 제어 (Control) < 외부 (External) < 공통 (Common) < 내용 (Content - Tệ nhất).
  - 💡 **Mẹo ghi nhớ**: T/S/C/N/C/N (Tốt -> Tệ) -> **Tính Sao Cho Nhẹ Cả Người**
- **응집도 (Cohesion - Độ gắn kết trong 1 module)**: Càng cao càng tốt.
  - 기능적 (Functional - Tốt nhất) > 순차적 (Sequential) > 통신적 (Communication) > 절차적 (Procedural) > 시간적 (Temporal) > 논리적 (Logical) > 우연적 (Coincidental - Tệ nhất).
  - 💡 **Mẹo ghi nhớ**: K/T/T/T/T/L/N (Tốt -> Tệ) -> **Không Thể Tin Thằng Trẻ Làm Ngốc**
- **팬인 (Fan-In) / 팬아웃 (Fan-Out)**:
  - Fan-in (Số module gọi nó): Cao thì tốt (tái sử dụng nhiều).
  - Fan-out (Số module nó gọi): Càng thấp càng tốt.

---

## 2. 모듈 (Module) & 독립성 (Independence)
**개념 (Khái niệm):** 시스템의 기능을 분리한 단위. 단독 컴파일과 재사용 가능 (Module là các đơn vị chức năng được phân tách của hệ thống, có thể biên dịch độc lập và tái sử dụng).

*   **기능적 독립성 (Functional Independence - Tính độc lập chức năng):**
    *   **Korean:** 각 모듈이 하나의 기능만을 수행하고 상호작용을 최소화하는 것. 결합도(Coupling)는 약하게(Weak), 응집도(Cohesion)는 강하게(Strong) 해야 함.
    *   **VI (Vietnamese) (Tiếng Việt):** Mỗi module chỉ thực hiện một chức năng và hạn chế tương tác với bên ngoài. Cần Độ phụ thuộc (Coupling) thấp và Độ gắn kết (Cohesion) cao. Kích thước module nên nhỏ gọn.
    *   **Example:**
        *   *KR:* 독립된 로그인 모듈은 다른 모듈 변경 시 영향을 받지 않음.
        *   *VN:* Module đăng nhập đứng độc lập, khi sửa giỏ hàng thì module đăng nhập không bị ảnh hưởng.

---

---

## 7. 공통 모듈 (Common Module)
**개념 (Khái niệm):** 여러 프로그램에서 공통적으로 사용할 수 있는 모듈 (Module dùng chung cho nhiều chương trình, ví dụ: Đăng nhập, tính toán).

*   **명세 기법 5가지 (5 nguyên tắc viết đặc tả module):**
    1.  **정확성 (Correctness):** 정확히 작성 (Chính xác).
    2.  **명확성 (Clarity):** 중의적이지 않게 (Rõ ràng, không mơ hồ).
    3.  **완전성 (Completeness):** 모든 것을 빠짐없이 (Đầy đủ).
    4.  **일관성 (Consistency):** 상호 충돌 없게 (Nhất quán).
    5.  **추적성 (Traceability):** 출처, 관계 추적 가능 (Có thể truy xuất nguồn gốc).
💡 **Mẹo ghi nhớ:** C-M-H-N-T (Chính-Rõ-Đủ-Nhất-Truy) -> **Chỉ Mong Học Nhất Trường**

---

---

## 9. 효과적인 모듈 설계 방안 (Effective Module Design)
*   **Korean:** 결합도↓, 응집도↑. 모듈의 영향 영역(Scope of Effect)이 제어 영역(Scope of Control) 안에 있어야 함. 단일 입구/단일 출구(Single Entry, Single Exit). 복잡도와 중복성 감소.
*   **VI (Vietnamese) (Tiếng Việt):** Coupling thấp, Cohesion cao. **Phạm vi ảnh hưởng (Scope of Effect) phải nằm TRONG Phạm vi kiểm soát (Scope of Control)** của module. Chỉ có 1 đầu vào và 1 đầu ra. Giảm độ phức tạp và dư thừa.
*   **Example:** Một hàm sắp xếp chỉ nên thay đổi mảng truyền vào nó (trong vùng kiểm soát), không nên vô tình thay đổi giao diện UI (vùng ảnh hưởng ngoài kiểm soát).

---

---

## 9. 소프트웨어 품질 특성 (ISO/IEC 9126)
- 6 tiêu chuẩn chất lượng:
  1. **기능성 (Functionality - Chức năng)**: Bảo mật, Tương tác, Chính xác.
  2. **신뢰성 (Reliability - Độ tin cậy)**: Không lỗi, Phục hồi (회복성), Chịu lỗi (고장 허용성).
  3. **사용성 (Usability - Khả năng sử dụng)**: Dễ học, Dễ hiểu, Hấp dẫn.
  4. **효율성 (Efficiency - Hiệu quả)**: Thời gian phản hồi, Tiết kiệm tài nguyên.
  5. **유지 보수성 (Maintainability - Khả năng bảo trì)**: Dễ phân tích, Dễ thay đổi, Ổn định.
  6. **이식성 (Portability - Khả năng thay thế/di chuyển)**: Cài đặt dễ, Tương thích, Thay thế.

---

## 8. 디자인 패턴 (Design Patterns)

### 디자인 패턴 (Design Pattern) 개요
- 세부적인 구현 방안을 설계할 때 참조할 수 있는 전형적인 해결 방식 또는 예제를 의미한다. (Là những phương pháp giải quyết hoặc ví dụ điển hình có thể tham khảo khi thiết계 chi tiết phương án triển khai.)
- 3가지 유형 (3 Loại chính): 생성 패턴 (Creational), 구조 패턴 (Structural), 행위 패턴 (Behavioral).

### 생성 패턴 (Creational Pattern / Mẫu khởi tạo) - 5 loại
- 객체 생성과 관련된 패턴. (Liên quan đến việc tạo đối tượng.)
- **빌더 (Builder):** 작게 분리된 인스턴스를 건축하듯이 조합하여 객체를 생성함. (Tạo đối tượng bằng cách lắp ráp các phần nhỏ như xây nhà.)
- **팩토리 메소드 (Factory Method):** 객체 생성을 서브 클래스에서 처리하도록 분리하여 캡슐화한 패턴으로, 가상 생성자(Virtual Constructor) 패턴이라고도 함. (Giao việc tạo đối tượng cho lớp con, còn gọi là Virtual Constructor).
- **프로토타입 (Prototype):** 원본 객체를 복제하는 방법으로 객체를 생성함. (Tạo đối tượng bằng cách copy/clone từ đối tượng gốc).
- **싱글톤 (Singleton):** 생성된 객체를 여러 프로세스가 동시에 참조할 수는 없음 (하나의 객체만 생성). (Đảm bảo chỉ có 1 instance duy nhất được tạo ra).
- **추상 팩토리 (Abstract Factory):** 서로 연관·의존하는 객체들의 그룹으로 생성하여 추상적으로 표현함. (Tạo ra một nhóm các đối tượng có liên quan với nhau thông qua interface).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **BFPSA** (Build - Fact - Pro - Sing - Ab): **Bạn Phải Phạt Sợ Ai**.

### 구조 패턴 (Structural Pattern / Mẫu cấu trúc) - 7 loại
- 클래스나 객체를 조합해 더 큰 구조를 만드는 패턴. (Kết hợp lớp/đối tượng thành cấu trúc lớn hơn).
- **어댑터 (Adapter):** 인터페이스를 다른 클래스가 재사용할 수 있도록 변환함. (Biến đổi interface để lớp khác dùng được, giống như cục sạc chuyển đổi điện).
- **브리지 (Bridge):** 서로가 독립적으로 확장할 수 있도록 구성함. (Tách phần trừu tượng và phần thực thi để cả 2 có thể phát triển độc lập).
- **컴포지트 (Composite):** 복합 객체와 단일 객체를 구분 없이 다루고자 할 때 사용함. (Xử lý đối tượng đơn lẻ và đối tượng phức hợp (nhóm) theo cùng một cách, cấu trúc cây).
- **데코레이터 (Decorator):** 부가적인 기능을 추가하기 위해 다른 객체들을 덧붙이는 방식으로 구현함. (Gắn thêm tính năng mới vào đối tượng có sẵn giống như trang trí).
- **퍼싸드 (Facade):** 복잡한 서브 클래스들을 피해 더 상위에 인터페이스를 구성함. (Tạo một interface cấp cao đơn giản để che giấu hệ thống con phức tạp bên dưới).
- **플라이웨이트 (Flyweight):** 가능한 한 인스턴스를 공유해서 사용함으로써 메모리를 절약하는 패턴. (Chia sẻ instance để tiết kiệm bộ nhớ, tái sử dụng những gì giống nhau).
- **프록시 (Proxy):** 접근이 어려운 객체와 여기에 연결하려는 객체 사이에서 인터페이스 역할을 수행하는 패턴. (Người đại diện, đứng giữa kiểm soát truy cập vào đối tượng thực).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **ABCDFFP** (Ad - Bri - Com - Dec - Fac - Fly - Pro): **Anh Bán Cơm Đĩa Phải Phạt Phi**.

### 행위 패턴 (Behavioral Pattern / Mẫu hành vi) - 11 loại
- 객체 간의 상호작용이나 책임 분배에 대한 패턴. (Giao tiếp và phân bổ trách nhiệm giữa các đối tượng).
- **책임 연쇄 (Chain of Responsibility):** 요청을 한 객체가 처리하지 못하면 다음 객체로 넘어가는 형태. (Xử lý dây chuyền, ai làm được thì làm, không thì chuyển người tiếp theo).
- **커맨드 (Command):** 재이용하거나 취소할 수 있도록 요청에 필요한 정보를 저장함. (Đóng gói yêu cầu thành đối tượng, dễ dàng undo/redo).
- **인터프리터 (Interpreter):** 언어에 문법 표현을 정의함. (Định nghĩa ngữ pháp cho ngôn ngữ).
- **반복자 (Iterator):** 접근이 잦은 객체에 대해 동일한 인터페이스를 사용하도록 함. (Duyệt qua các phần tử của tập hợp mà không cần biết cấu trúc bên trong).
- **중재자 (Mediator):** 복잡한 상호 작용을 캡슐화하여 객체로 정의함. (Làm trung gian liên lạc giữa các đối tượng để giảm sự phụ thuộc chéo).
- **메멘토 (Memento):** 객체를 해당 시점의 상태로 돌릴 수 있는 기능을 제공, C + Z와 같은 되돌리기 기능을 개발할 때 주로 이용함. (Lưu trạng thái để khôi phục/Undo).
- **옵서버 (Observer):** 객체에 상속되어 있는 다른 객체들에게 변화된 상태를 전달함. (Một đối tượng thay đổi trạng thái, các đối tượng đăng ký theo dõi sẽ được thông báo - VD: Đăng ký kênh YouTube).
- **상태 (State):** 객체의 상태에 따라 동일한 동작을 다르게 처리해야 할 때 사용함. (Thay đổi hành vi khi trạng thái đối tượng thay đổi).
- **전략 (Strategy):** 동일한 계열의 알고리즘들을 상호 교환할 수 있게 정의함. (Đóng gói thuật toán để có thể thay đổi linh hoạt lúc runtime).
- **템플릿 메소드 (Template Method):** 하위 클래스에서 세부 처리를 구체화함. (Lớp cha định nghĩa khung thuật toán, lớp con implement chi tiết).
- **방문자 (Visitor):** 처리 기능을 분리하여 별도의 클래스로 구성함. (Tách logic xử lý khỏi cấu trúc dữ liệu, đối tượng Visitor đi "thăm" các phần tử để xử lý).

---

## 16. 디자인 패턴 심화 (Design Patterns chuyên sâu)

### 디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)
- **장점 (Ưu điểm):** 범용적 코딩 스타일(구조 파악 용이), 생산성 향상, 개발 시간/비용 절약, 의사소통 원활, 유연한 대처 가능. (Dễ đọc code, tăng năng suất, tiết kiệm chi phí, dễ giao tiếp, dễ đối phó thay đổi).
- **단점 (Nhược điểm):** 초기 투자 비용 부담, 다른 기반(비객체지향)에는 부적합. (Tốn kém thời gian học ban đầu, không hợp cho mô hình không hướng đối tượng).

### 디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)
- *(Tham khảo lại Mục 8 để biết tên gọi, dưới đây là các đặc điểm từ khóa thường ra thi)*
- **생성 패턴 (5개):**
  - **Abstract Factory:** 인터페이스를 통해 구체적인 클래스에 의존하지 않고 객체 생성. (Tạo đối tượng qua Interface mà không phụ thuộc Class cụ thể).
  - **Builder:** 생성 과정과 표현 방법을 분리. (Tách rời quá trình tạo và cách biểu diễn).
  - **Factory Method:** 상위 클래스는 인터페이스만 정의, 실제 생성은 서브 클래스가. (Lớp cha định nghĩa Interface, lớp con thực sự tạo).
  - **Prototype:** 비용이 큰 경우 복제하여 생성. (Clone khi chi phí tạo mới quá lớn).
  - **Singleton:** 인스턴스가 하나뿐임을 보장. (Đảm bảo chỉ có 1 instance).
- **구조 패턴 (7개):**
  - **Adapter:** 호환성이 없는 클래스들의 인터페이스 변환. (Chuyển đổi interface không tương thích).
  - **Bridge:** 기능(추상층)과 구현(구현부)을 분리. (Tách rời chức năng và phần thực thi).
  - **Composite:** 트리 구조로 구성. (Cấu trúc cây).
  - **Decorator:** 능동적으로 기능들을 확장(덧붙임). (Chủ động mở rộng/thêm tính năng).
  - **Facade:** 통합 인터페이스 제공(Wrapper 객체). (Cung cấp interface tổng hợp).
  - **Flyweight:** 다수의 유사 객체 공유 (메모리 절약). (Chia sẻ nhiều đối tượng giống nhau để tiết kiệm RAM).
  - **Proxy:** 네트워크 연결, 메모리 대용량 객체 접근 등 (인터페이스 역할). (Làm đại diện kết nối mạng, tải đối tượng lớn).

---

## 4. 디자인 패턴 (Design Patterns - GoF)
- **생성 패턴 (Creational - 5)**: Abstract Factory, Builder, Factory Method, Prototype, Singleton. (Tạo đối tượng)
- **구조 패턴 (Structural - 7)**: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy. (Cấu trúc, ghép nối)
- **행위 패턴 (Behavioral - 11)**: Strategy, Mediator, Command, Observer, State, Iterator, Visitor, Chain of Responsibility, Interpreter, Memento, Template Method. (Hành vi, tương tác)

---
# Chapter 4. 인터페이스 설계 (Interface Design)

---

## 11. 디자인 패턴 (Design Pattern)
**개념 (Khái niệm):** 설계 시 참조할 수 있는 전형적인 해결 방식 (Các mẫu giải pháp tiêu chuẩn dùng tham khảo khi thiết kế phần mềm). GoF (Gang of Four)가 23개로 체계화.
💡 **Mẹo ghi nhớ:** "바퀴를 다시 발명하지 마라 (Don't reinvent the wheel)" - Đừng phát minh lại bánh xe, hãy dùng các mẫu đã được kiểm chứng.

*   **장단점 (Ưu & Nhược điểm):**
    *   장점: 구조 파악 용이, 의사소통 원활, 생산성 향상 (Dễ nắm cấu trúc, giao tiếp tốt, tăng năng suất).
    *   단점: **초기 투자 비용 부담**, 객체지향 전용 (Tốn chi phí/thời gian học ban đầu, chỉ hợp với Hướng đối tượng).

### 11.1 생성 패턴 (Creational - 5개)
객체 생성 캡슐화 (Đóng gói quá trình tạo đối tượng).
1.  **추상 팩토리 (Abstract Factory):** 연관된 객체 그룹 생성 (Tạo nhóm đối tượng liên quan).
2.  **빌더 (Builder):** 생성 과정과 표현 방법 분리 (Tách quá trình xây dựng và biểu diễn).
3.  **팩토리 메소드 (Factory Method):** 객체 생성을 서브 클래스에 위임, 가상 생성자 (Giao việc tạo đối tượng cho lớp con).
4.  **프로토타입 (Prototype):** 원본 객체 복제 (Nhân bản đối tượng nguyên mẫu Clone).
5.  **싱글톤 (Singleton):** 인스턴스가 하나뿐임을 보장 (Đảm bảo chỉ có 1 instance duy nhất).

### 11.2 구조 패턴 (Structural - 7개)
객체 조합으로 더 큰 구조 생성 (Kết hợp đối tượng thành cấu trúc lớn hơn).
1.  **어댑터 (Adapter):** 호환 안 되는 인터페이스 변환 (Chuyển đổi interface không tương thích).
2.  **브리지 (Bridge):** 구현과 추상층 분리 (Tách biệt phần triển khai và phần trừu tượng).
3.  **컴포지트 (Composite):** 트리 구조, 단일/복합 객체 동일하게 다룸 (Cấu trúc cây, xử lý đối tượng đơn và phức như nhau).
4.  **데코레이터 (Decorator):** 동적으로 기능 덧붙임 (Thêm chức năng linh hoạt bằng cách bọc đối tượng).
5.  **퍼싸드 (Facade):** 복잡한 서브 시스템 위에 통합 인터페이스(Wrapper) 제공 (Tạo mặt tiền/giao diện chung đơn giản cho hệ thống phức tạp).
6.  **플라이웨이트 (Flyweight):** 인스턴스 공유로 메모리 절약 (Chia sẻ đối tượng để tiết kiệm bộ nhớ).
7.  **프록시 (Proxy):** 접근 어려운 객체를 대리 수행 (Đại diện/ủy quyền truy cập cho đối tượng khác).

### 11.3 행위 패턴 (Behavioral - 11개)
객체 간 상호작용 및 책임 분배 (Tương tác và phân chia trách nhiệm giữa các đối tượng).
1.  **책임 연쇄 (Chain of Responsibility):** 고리를 따라 책임 넘김 (Truyền yêu cầu theo chuỗi xử lý).
2.  **커맨드 (Command):** 요청을 객체로 캡슐화 (로그, Undo) (Đóng gói yêu cầu thành đối tượng, tiện cho Undo/Log).
3.  **인터프리터 (Interpreter):** 언어 문법 정의 (Định nghĩa cú pháp ngôn ngữ).
4.  **반복자 (Iterator):** 내부 노출 없이 순차 접근 (Truy cập tuần tự không lộ cấu trúc).
5.  **중재자 (Mediator):** 복잡한 상호작용을 통제/지시 (Điều phối viên trung gian để giảm phụ thuộc chéo).
6.  **메멘토 (Memento):** 상태 스냅샷 저장/복원 (Lưu trạng thái để Undo/Khôi phục).
7.  **옵서버 (Observer):** 상태 변화를 구독자에게 전파 (Publish/Subscribe, thông báo khi có thay đổi).
8.  **상태 (State):** 상태에 따라 다른 동작 (Hành vi thay đổi theo trạng thái).
9.  **전략 (Strategy):** 알고리즘 캡슐화하여 교체 가능 (Đóng gói thuật toán, dễ dàng hoán đổi).
10. **템플릿 메소드 (Template Method):** 상위가 골격, 하위가 세부 구현 (Lớp cha tạo khung, lớp con điền chi tiết).
11. **방문자 (Visitor):** 처리 기능을 분리하여 방문 수행 (Tách logic xử lý ra khỏi cấu trúc dữ liệu, đi "thăm" từng phần tử).

---

---

## 2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)
- **정형 기술 검토 (FTR - Formal Technical Review)**:
  - **동료검토 (Peer Review)**: Tác giả tự giải thích tài liệu, đồng nghiệp tìm lỗi.
  - **워크 스루 (Walk Through)**: Gửi tài liệu trước, họp review ngắn để tìm lỗi nhanh.
  - **인스펙션 (Inspection)**: Chuyên gia khác (không phải tác giả) kiểm tra chặt chẽ để tìm lỗi.
  - 💡 **Mẹo ghi nhớ**: 동료(Tự thuyết trình) / 워크스루(Họp ngắn) / 인스펙션(Chuyên gia chém).
- **연계 기술 (Connection Tech)**: 
  - DB Link, API, Socket (Cấp phát cổng), JDBC.
- **미들웨어 (Middleware)**: Phần mềm trung gian kết nối các hệ thống khác biệt.
  - **TP Monitor**: Giám sát Transaction (Giao dịch).
  - **MOM (Message-Oriented)**: Bất đồng bộ (비동기), dùng hàng đợi tin nhắn (메시지 큐).
  - **ORB (Object Request Broker)**: Hướng đối tượng, chuẩn CORBA.
  - **WAS (Web Application Server)**: Xử lý nội dung web động (동적인 콘텐츠).

---
# 소프트웨어 생명 주기 및 개발 방법론 (SDLC & Methodologies)

---

## 13. 시스템 연계 및 인터페이스 (System Interface & Integration)
### 13.1 시스템 연계 기술 (Các công nghệ liên kết hệ thống)
1.  **DB Link:** DB 객체 이용 (Kết nối trực tiếp qua DB Link).
2.  **API/Open API:** 프로그램 인터페이스 (Mở cổng API để ứng dụng khác gọi).
3.  **EAI (연계 솔루션):** 중계 서버/클라이언트 사용 (Dùng máy chủ trung gian Enterprise Application Integration).
4.  **Socket:** 포트 할당하여 연결 (Mở port mạng Socket để truyền dữ liệu).
5.  **Web Service:** WSDL, UDDI, SOAP 프로토콜 사용 (Dịch vụ web dùng giao thức chuẩn XML/SOAP).

### 13.2 인터페이스 통신 & 처리 유형 (Loại giao tiếp & xử lý)
*   **통신 유형 (Loại Giao tiếp):**
    *   **단방향 (Unidirectional):** 응답 없음 (Chỉ gửi, không cần phản hồi).
    *   **동기 (Synchronous):** 응답 대기 (Gửi và đợi phản hồi).
    *   **비동기 (Asynchronous):** 다른 작업 수행 (Gửi xong làm việc khác, trả lời sau).
*   **처리 유형 (Loại Xử lý):**
    *   **실시간 (Real-time):** 즉시 처리 (Xử lý ngay lập tức).
    *   **지연 처리 (Deferred):** 비용 절감을 위해 모아서 처리 (Trì hoãn xử lý để tiết kiệm chi phí).
    *   **배치 (Batch):** 대용량 일괄 처리 (Gom dữ liệu lớn xử lý 1 lần).

### 13.3 명세화 (Specification)
*   **송수신 데이터 명세화:** 데이터 필드명, 타입, 사이즈, **암호화 여부** 정의 (Đặc tả dữ liệu: Tên trường, Kiểu, Kích thước, và có Cần Mã hóa không).
*   **오류 식별 및 처리 방안 명세화:** 오류 코드, 메시지, 해결 방법 정의 (Đặc tả lỗi: Mã lỗi, Thông báo, Cách xử lý để dễ vận hành).

---

---

## 17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)

### 요구사항 검증 방법 추가 (Các phương pháp kiểm chứng yêu cầu bổ sung)
- **요구사항 검토 (Requirements Review):** 동료검토, 워크스루, 인스펙션. (Review thủ công bởi người).
- **프로토타이핑 (Prototyping):** 견본품을 만들어 최종 결과물을 예측. (Làm bản nháp/prototype để dự đoán kết quả).
- **테스트 설계 (Test Design):** 요구사항이 현실적으로 테스트 가능한지 검토 (Test Case 생성). (Tạo Test Case để xem yêu cầu có khả thi không).
- **CASE 도구 활용 (CASE Tools):** 일관성 분석(Consistency Analysis)을 통해 요구사항 변경사항 추적 및 분석. (Dùng tool để phân tích tính nhất quán).

### 시스템 연계 기술 (Các công nghệ liên kết hệ thống)
- **DB Link:** DB에서 제공하는 DB Link 객체를 이용. (Dùng trực tiếp link kết nối của DB).
- **API / Open API:** 송신 시스템의 DB에서 데이터를 읽어와 제공하는 프로그램. (Giao diện lập trình ứng dụng mở).
- **연계 솔루션:** EAI 서버와 송·수신 시스템에 설치되는 클라이언트(Client)를 이용. (Giải pháp dùng EAI Server).
- **Socket:** 통신을 위한 소켓을 생성하여 포트를 할당하고 클라이언트와 연결. (Tạo socket và cấp phát port để giao tiếp mạng).
- **Web Service:** WSDL, UDDI, SOAP 프로토콜을 이용. (Dịch vụ web dùng chuẩn SOAP/WSDL).

### 연계 매커니즘 구성요소 (Thành phần cơ chế liên kết)
- **송신 시스템 (Sender System):** 데이터를 전송 형식에 맞게 변환하여 송신. (Hệ thống gửi, chuyển đổi dữ liệu ra định dạng chuẩn).
- **수신 시스템 (Receiver System):** 수신한 데이터를 시스템에 맞게 변환하여 반영. (Hệ thống nhận, chuyển đổi dữ liệu chuẩn vào DB).
- **연계 서버 (Integration Server):** 송수신 현황을 모니터링. (Server trung gian giám sát quá trình truyền dữ liệu).

### 미들웨어(Middleware) 상세 (Chi tiết Middleware)
- 운영체제와 응용 프로그램 사이에서 다양한 서비스를 제공.
- **DB (DataBase):** 2-Tier 아키텍처에 주로 사용, 클라이언트와 원격 DB를 연결. (Kết nối Client-DB).
- **RPC (Remote Procedure Call):** 원격 프로시저를 로컬 프로시저처럼 호출. (Gọi hàm từ xa như gọi hàm cục bộ).
- **MOM (Message Oriented Middleware):** 비동기형 메시지 전달 (이기종 분산 데이터 시스템). (Truyền tin nhắn bất đồng bộ).
- **TP-Monitor (Transaction Processing Monitor):** 온라인 트랜잭션 처리 및 감시 (항공기/철도 예약). (Quản lý giao dịch online tốc độ cao).
- **ORB (Object Request Broker):** CORBA 표준 스펙을 구현한 객체 지향 미들웨어. (Middleware hướng đối tượng chuẩn CORBA).
- **WAS (Web Application Server):** 동적인 콘텐츠를 처리하는 미들웨어. (Xử lý web động).

---

# 3과목: 데이터베이스 (Phần 3: Cơ sở dữ liệu)
*(Lưu ý: Tùy theo chương trình, Database có thể thuộc Subject 1 hoặc 3. Dưới đây là kiến thức cốt lõi về DB)*

---

---

## 14. 미들웨어 (Middleware)
**개념 (Khái niệm):** 운영체제와 응용 프로그램 사이의 중재자 (Phần mềm trung gian đứng giữa OS và Ứng dụng).
💡 **Mẹo ghi nhớ 미들웨어:** DB, RPC, MOM, TP-Monitor, ORB, WAS

1.  **DB 미들웨어:** 2-Tier 원격 연결 (ODBC, IDAPI, Glue). (Kết nối CSDL 2 lớp).
2.  **RPC (Remote Procedure Call):** 원격을 로컬처럼 호출 (Entera, ONC/RPC). (Gọi hàm từ xa như gọi hàm cục bộ).
3.  **MOM (Message Oriented Middleware):** 비동기 메시지, 데이터 동기 (IBM MQ, JMS). (Truyền tin nhắn bất đồng bộ, đồng bộ dữ liệu hệ thống khác nền tảng).
4.  **TP-Monitor (Transaction Processing):** 항공/철도 예약, 빠른 응답/트랜잭션 감시 (tuxedo, tmax). (Giám sát giao dịch, đảm bảo tốc độ phản hồi nhanh cho đặt vé).
5.  **ORB (Object Request Broker):** 객체 지향, CORBA 표준 (Orbix). (Môi giới yêu cầu đối tượng, chuẩn CORBA).
6.  **WAS (Web Application Server):** 동적 콘텐츠, 웹 환경 핵심(Java/EJB) (WebLogic, WebSphere). (Xử lý nội dung web động, tác vụ doanh nghiệp quan trọng).
    *   *Example:* Apache là Web Server (tĩnh), còn WebLogic/Tomcat là WAS (động).

*   **솔루션 식별 & 명세서 작성:** 아키텍처 구성 정보, 구매 내역 확인 -> 제약사항 확인 (Xác định Middleware dựa trên kiến trúc và hóa đơn mua sắm -> Kiểm tra các hạn chế / constraints).

---

## 6. 애자일 방법론 (Agile Methodology)
- **개념**: Linh hoạt, phản hồi liên tục.
- **4대 핵심 가치 (4 Core Values)**:
  1. Cá nhân và tương tác (개인과의 상호작용) > Quy trình và công cụ.
  2. Phần mềm chạy được (실행되는 소프트웨어) > Tài liệu.
  3. Hợp tác với khách hàng (고객과의 협력) > Đàm phán hợp đồng.
  4. Phản hồi với sự thay đổi (변화에 유연하게 대응) > Tuân thủ kế hoạch.

---

## 7. 스크럼(Scrum) 및 XP(eXtreme Programming)
- **스크럼 (Scrum)**: Quản lý dự án Agile theo nhóm.
  - **용어**: 제품 백로그 (Product Backlog - Yêu cầu tổng), 스프린트 (Sprint - Chu kỳ 2-4 tuần), 속도 (Velocity), 번 다운 차트 (Burn Down Chart - Biểu đồ tiến độ), PO (Product Owner), SM (Scrum Master).
  - **프로세스**: Backlog -> Sprint Planning -> Sprint Execution (Daily Scrum) -> Sprint Review (Đánh giá) -> Sprint Retrospective (Hồi tưởng/Cải tiến).
- **XP (eXtreme Programming)**: Tối ưu hóa phát triển phần mềm cùng khách hàng.
  - **핵심 가치 (5 Core Values)**: 의사소통 (Communication), 단순성 (Simplicity), 용기 (Courage), 존중 (Respect), 피드백 (Feedback). 
  - 💡 **Mẹo ghi nhớ**: Y/Đ/D/T/P -> **Ý Định Dũng Tướng Phàm**
  - **기본 원리 (Principles)**: Pair Programming, CI (Tích hợp liên tục), TDD (Test-Driven Development), Refactoring (Tái cấu trúc mã), 40-Hour Work.

---
# Chapter 2. 화면 설계 (Screen Design)

---

## 2. 스크럼 및 XP 추가 개념 (Advanced Scrum & XP)
- **스크럼 프로세스 (Scrum Process)**:
  - **일일 스크럼 (Daily Scrum)**: Họp đứng 15 phút. Cập nhật tiến độ lên Burn-down Chart (Biểu đồ tiêu hao).
  - **스프린트 검토 (Sprint Review)**: Demo sản phẩm cho khách hàng xem có đúng ý không.
  - **스프린트 회고 (Sprint Retrospective)**: Nội bộ team họp để rút kinh nghiệm, cải tiến quy trình.
- **XP 기법 상세 (XP Details)**:
  - **사용자 스토리 (User Story)**: Kịch bản do khách hàng viết (đơn vị chức năng), có thể chứa Test Case.
  - **릴리즈 계획 (Release Planning)**: Kế hoạch phát hành từng phần sản phẩm (v1.0, v1.1).
  - **스파이크 (Spike)**: Chương trình nhỏ, code thử nghiệm nhanh để kiểm tra tính khả thi của công nghệ nhằm giảm rủi ro (기술적 위험 감소). Code này có thể bị vứt đi sau khi test.

---

## 4. 운영 환경 구축 고려사항 (Operation Environment Considerations)
- **운영체제 (OS)** & **DBMS**: 가용성 (Availability), 성능 (Performance), 기술 지원 (Tech Support), 구축 비용 (Cost). 
  - OS có thêm: 주변 기기 (Thiết bị ngoại vi).
  - DBMS có thêm: 상호 호환성 (Khả năng tương thích - JDBC/ODBC).
- **WAS (Web Application Server)**: Xử lý nội dung động. Có thêm **가비지 컬렉션 (GC - Dọn rác)**.
- **오픈 소스 (Open Source)**: Cần chú ý 라이선스 (Bản quyền), 사용자 수 (Số lượng người dùng), 기술의 지속 가능성 (Khả năng duy trì công nghệ).

---

## 6. 구조적 분석 도구 (Structured Analysis Tools)
- Phân tích Top-down (하향식), dùng biểu đồ (도형).
- **DFD (Biểu đồ luồng dữ liệu)**: Process (Tròn), Flow (Mũi tên), Data Store (Vạch ngang), Terminator (Vuông).
- **DD (Từ điển dữ liệu)**: 
  - `=`: Định nghĩa
  - `+`: Nối
  - `( )`: Tùy chọn (Optional)
  - `[ | ]`: Chọn 1 trong các (Or)
  - `{ }`: Lặp (Iteration)
  - `* *`: Chú thích
- **HIPO**: Biểu đồ phân cấp (가시적, 총체적, 세부적).

---

## 10. 소프트웨어 설계 원리 (Software Design Principles)
- **모듈화 (Modularity)**: 
  - Module quá nhỏ -> Chi phí tích hợp (Integration Cost) tăng.
  - Module quá lớn -> Chi phí phát triển từng module (Development Cost) tăng.
- **추상화 (Abstraction)**: 3 loại (과정 - Quá trình, 데이터 - Dữ liệu, 제어 - Điều khiển).
- **단계적 분해 (Stepwise Refinement)**: Đi từ trên xuống (Top-down).
- **정보 은닉 (Information Hiding)**: Giấu thông tin để giảm phụ thuộc.
- **시스템 타입 (System Types)**:
  - **대화형 (Interactive)**: Tương tác (VD: Web bán hàng).
  - **이벤트 중심 (Event-driven)**: Dựa trên sự kiện (VD: Chuông báo cháy).
  - **변환형 (Transformational)**: Biến đổi dữ liệu (VD: Trình biên dịch - Compiler).
  - **객체 영속형 (Object Persistence)**: Lưu trữ lâu dài (VD: Database Server).

# Subject 1 - Part 3

---

## 3. 결합도 (Coupling - Độ phụ thuộc)
**개념 (Khái niệm):** 모듈 간의 의존성 정도 (Mức độ phụ thuộc giữa các module với nhau). **낮을수록 좋음 (Càng thấp càng tốt).**

순서 (Từ Tốt nhất đến Xấu nhất): **자료(Data) -> 스탬프(Stamp) -> 제어(Control) -> 외부(External) -> 공통(Common) -> 내용(Content)**
💡 **Mẹo ghi nhớ:** T-S-C-N-C-N (Data-Stamp-Control-External-Common-Content) -> **Tính Sao Cho Nhẹ Cả Người**

1.  **자료 결합도 (Data Coupling) - TỐT NHẤT:**
    *   **Korean:** 파라미터(자료 요소)만 전달.
    *   **VI (Vietnamese) (Tiếng Việt):** Chỉ truyền tham số dữ liệu cần thiết.
    *   **Example:** `sum(a, b)` truyền đúng 2 số a, b.
2.  **스탬프 결합도 (Stamp Coupling):**
    *   **Korean:** 배열/레코드 등 자료구조가 전달됨.
    *   **VI (Vietnamese) (Tiếng Việt):** Truyền toàn bộ cấu trúc dữ liệu (mảng, đối tượng) nhưng chỉ dùng 1 phần.
    *   **Example:** Truyền đối tượng `User` nhưng chỉ dùng `User.name`.
3.  **제어 결합도 (Control Coupling):**
    *   **Korean:** 제어 신호(Flag)를 전달하여 모듈 흐름 제어.
    *   **VI (Vietnamese) (Tiếng Việt):** Truyền cờ điều khiển (flag, boolean) can thiệp vào logic của module khác.
    *   **Example:** Truyền `isExpress=true` để quyết định cách xử lý.
4.  **외부 결합도 (External Coupling):**
    *   **Korean:** 외부 변수/데이터 참조.
    *   **VI (Vietnamese) (Tiếng Việt):** Cùng phụ thuộc vào dữ liệu / file / thiết bị bên ngoài.
    *   **Example:** Hai module dùng chung một file `config.txt`.
5.  **공통 결합도 (Common Coupling):**
    *   **Korean:** 공통 데이터 영역(전역 변수) 공유.
    *   **VI (Vietnamese) (Tiếng Việt):** Nhiều module dùng chung biến toàn cục (global variables).
    *   **Example:** Sử dụng `public static int totalCount` chung.
6.  **내용 결합도 (Content Coupling) - XẤU NHẤT:**
    *   **Korean:** 내부 기능/자료 직접 참조. 스파게티 코드.
    *   **VI (Vietnamese) (Tiếng Việt):** Truy cập, sửa đổi trực tiếp dữ liệu/logic nội bộ của module khác.
    *   **Example:** `moduleB.internalValue = 10` từ module A.

---

---

## 4. 응집도 (Cohesion - Độ gắn kết)
**개념 (Khái niệm):** 모듈 내부 요소들이 서로 밀접하게 관련되어 있는 정도 (Mức độ liên quan chặt chẽ của các thành phần BÊN TRONG 1 module). **강할수록 좋음 (Càng cao càng tốt).**

순서 (Từ Tốt nhất đến Xấu nhất): **기능(Functional) -> 순차(Sequential) -> 교환(Communication) -> 절차(Procedural) -> 시간(Temporal) -> 논리(Logical) -> 우연(Coincidental)**
💡 **Mẹo ghi nhớ:** K-S-K-C-S-N-U (Kì-Sun-Kiều-Chul-Shi-Non-U) -> **Không Tin Kiều Chỉ Sợ Người Ù**

1.  **기능적 응집도 (Functional):**
    *   **Korean:** 단일 문제와 연관되어 수행. (Tốt nhất)
    *   **VI (Vietnamese) (Tiếng Việt):** Mọi thành phần trong module cùng giải quyết MỘT bài toán duy nhất.
2.  **순차적 응집도 (Sequential):**
    *   **Korean:** 출력 데이터가 다음 활동의 입력 데이터로 사용됨.
    *   **VI (Vietnamese) (Tiếng Việt):** Đầu ra của bước này là đầu vào của bước kia (trong cùng module).
3.  **교환(통신)적 응집도 (Communication):**
    *   **Korean:** 동일한 입출력을 사용하여 서로 다른 기능 수행.
    *   **VI (Vietnamese) (Tiếng Việt):** Các chức năng khác nhau dùng chung một tập dữ liệu đầu vào / đầu ra.
4.  **절차적 응집도 (Procedural):**
    *   **Korean:** 기능들을 순차적으로 수행.
    *   **VI (Vietnamese) (Tiếng Việt):** Các phần tử được thực hiện theo trình tự thời gian / kịch bản nhất định.
5.  **시간적 응집도 (Temporal):**
    *   **Korean:** 특정 시간에 처리되는 기능들을 모음.
    *   **VI (Vietnamese) (Tiếng Việt):** Gom các tác vụ xảy ra cùng một thời điểm (VD: khối khởi tạo hệ thống Init).
6.  **논리적 응집도 (Logical):**
    *   **Korean:** 유사한 성격/형태로 분류되는 요소들을 모음.
    *   **VI (Vietnamese) (Tiếng Việt):** Gom các hàm có tính chất logic giống nhau (VD: Hàm in các loại báo cáo, mặc dù báo cáo khác nhau).
7.  **우연적 응집도 (Coincidental) - XẤU NHẤT:**
    *   **Korean:** 아무 관련 없이 구성됨.
    *   **VI (Vietnamese) (Tiếng Việt):** Các phần tử gom lại ngẫu nhiên, không liên quan gì nhau.

---

---

## 5. Fan-In / Fan-Out (팬인 / 팬아웃)
**개념 (Khái niệm):** 모듈 간의 호출 관계를 나타내는 지표 (Chỉ số thể hiện mức độ gọi lẫn nhau giữa các module).

*   **Fan-In (들어옴 / Đi vào):**
    *   **Korean:** 나를 호출하는 모듈 수. **높게(High)** 설계하는 것이 재사용성 측면에서 좋음. (단, 단일 장애점 주의)
    *   **VI (Vietnamese) (Tiếng Việt):** Số lượng module gọi đến module hiện tại. Fan-In CAO là tốt vì chứng tỏ module được tái sử dụng nhiều, nhưng cần cẩn thận vì nó là trung tâm (Single Point of Failure).
*   **Fan-Out (나감 / Đi ra):**
    *   **Korean:** 내가 호출하는 모듈 수. **낮게(Low)** 설계하여 단순화해야 함.
    *   **VI (Vietnamese) (Tiếng Việt):** Số lượng module mà module hiện tại gọi. Fan-Out THẤP là tốt, tránh việc module phụ thuộc vào quá nhiều nơi khác.

💡 **Mẹo ghi nhớ:** Fan-In = Gọi VÀO tôi (High is good) / Fan-Out = Tôi gọi RA (Low is good).

---

---

## 6. N-S 차트 (Nassi-Schneiderman Chart)
**개념 (Khái niệm):** 논리 기술 중점의 박스 다이어그램 (Biểu đồ dạng hộp tập trung mô tả logic).

*   **Korean:** GOTO나 화살표를 사용하지 않음. 단일 입구/단일 출구. Box Diagram, Chapin Chart라고도 부름. 순차, 선택, 반복 논리 구조 시각화.
*   **VI (Vietnamese) (Tiếng Việt):** Đặc điểm quan trọng nhất: **KHÔNG DÙNG GOTO và KHÔNG CÓ MŨI TÊN**. Có một lối vào và một lối ra duy nhất. Còn gọi là Box Diagram hoặc Chapin Chart. Gồm 3 cấu trúc: Tuần tự, Lựa chọn (If-else), Lặp (Loop). Dễ chuyển sang code nhưng khó vẽ.

---

---

## 8. 재사용 (Reuse)
**개념 (Khái niệm):** 기존 기능을 최적화하여 다시 쓰는 것 (Tái sử dụng chức năng để tiết kiệm thời gian và chi phí).

*   **Korean:** 결합도는 낮고 응집도는 높아야 함.
*   **VI (Vietnamese) (Tiếng Việt):** Yêu cầu: Độ phụ thuộc (Coupling) THẤP và Độ gắn kết (Cohesion) CAO.
*   **분류 (Phân loại):**
    *   **함수와 객체 (Function & Object):** 소스 코드 단위 (Mức mã nguồn / Class).
    *   **컴포넌트 (Component):** 인터페이스 통신 (Mức Interface, không sửa code gốc).
    *   **애플리케이션 (Application):** 시스템 전체 (Mức ứng dụng hoàn chỉnh).

---

---

## 10. 코드 (Code) 개요 & 종류
**개념 (Khái niệm):** 데이터를 식별, 분류, 배열하기 위해 사용하는 기호 (Ký hiệu dùng để nhận dạng, phân loại và sắp xếp dữ liệu).

*   **기능 (Chức năng):** 식별(Nhận dạng), 분류(Phân loại), 배열(Sắp xếp), 표준화(Chuẩn hóa), 간소화(Đơn giản hóa).
*   **종류 (Các loại Code):**
    1.  **순차 코드 (Sequential):** 발생 순서대로 일련번호 부여 (Đánh số thứ tự 1, 2, 3...).
    2.  **블록 코드 (Block):** 공통성 있는 항목을 블록으로 묶음 (Phân khối theo nhóm chung).
    3.  **10진 코드 (Decimal):** 0~9까지 10진 분할 반복, 도서분류 (Phân loại thập phân như sách thư viện).
    4.  **그룹 분류 코드 (Group Classification):** 대/중/소분류 (Phân nhóm lớn/vừa/nhỏ như 1-01-001).
    5.  **연상 코드 (Mnemonic):** 명칭이나 약호와 관계있는 기호 (Mã gợi nhớ, ví dụ: TV-40 cho Tivi 40 inch).
    6.  **표의 숫자 코드 (Significant Digit):** 물리적 수치를 직접 적용 (Dùng kích thước vật lý làm mã).
    7.  **합성 코드 (Combined):** 2개 이상 조합 (Kết hợp nhiều mã).

*   **코드 부여 체계 (Code Assignment System):**
    *   **Korean:** 이름만으로 개체의 용도와 적용 범위를 알 수 있게 상세 명시 (자릿수, 구분자).
    *   **VI (Vietnamese) (Tiếng Việt):** Hệ thống đánh mã sao cho nhìn vào tên mã là biết ngay công dụng và phạm vi (cần nêu rõ số chữ số, dấu phân cách).
    *   **Example:** 연도(00) + 학과(00) + 개인번호(000) -> 2401001.

---
