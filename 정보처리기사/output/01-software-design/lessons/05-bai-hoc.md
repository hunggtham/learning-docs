# 10. 요구사항 심화 (Yêu cầu chuyên sâu)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **10. 요구사항 심화 (Yêu cầu chuyên sâu)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

요구사항, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

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
