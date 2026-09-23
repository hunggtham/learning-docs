# 9. 요구사항 및 시스템 파악 (Yêu cầu & Phân tích Hệ thống)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **9. 요구사항 및 시스템 파악 (Yêu cầu & Phân tích Hệ thống)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

요구사항, 시스템, 파악

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

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
