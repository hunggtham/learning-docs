# 2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

소프트웨어, 공학, 기법

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)

### 2.1 소프트웨어 재사용 (Software Reuse)
- **이점 (Benefits):** 개발 시간과 비용 단축, 품질 향상, 생산성 향상, 시스템 명세/설계/코드 등 문서 공유.
- **방법 (Methods):**
  - **합성 중심 (Composition-based):** 전자 칩 같은 소프트웨어 부품(모듈)을 만들어 끼워 맞추는 방법.
  - **생성 중심 (Generation-based):** 추상화 형태로 쓰여진 명세를 구체화하여 프로그램을 만드는 방법.
- **Tiếng Việt:** Tái sử dụng phần mềm giúp giảm thời gian/chi phí, tăng chất lượng. 
  - Tổng hợp: lắp ráp các module (như chip).
  - Khởi tạo: tạo chương trình từ đặc tả trừu tượng.
- **Example:**
  - *KR:* 이전에 만든 로그인 모듈을 새 프로젝트에 그대로 재사용.
  - *VN:* Tái sử dụng nguyên bản module đăng nhập đã làm trước đó cho dự án mới.

### 2.2 소프트웨어 재공학 (Software Reengineering)
- 기존 소프트웨어의 데이터와 기능을 변경 및 개선하여 유지보수성과 품질을 높이는 기법.
- **이점 (Benefits):** 위험 부담 감소, 개발 시간/비용 단축, 시스템 명세 오류 억제.
- **주요 활동 (Activities):**
  - **분석 (Analysis):** 명세서 확인 및 재공학 대상 선정.
  - **재구성 (Restructuring):** 코드 재구성하여 구조 향상.
  - **역공학 (Reverse Engineering):** 기존 소프트웨어를 분석하여 설계 정보를 재발견하는 활동.
  - **이식 (Migration):** 다른 운영체제나 하드웨어 환경으로 변환.
- **Tiếng Việt:** Tái thiết kế phần mềm cũ để dễ bảo trì. Các hoạt động chính: Phân tích, Tái cấu trúc, Dịch ngược (Reverse Engineering), và Di chuyển (Migration).
- 💡 **Mẹo ghi nhớ:** Các bước Reengineering: "Phân Tích -> Tái Cấu Trúc -> Dịch Ngược -> Di Chuyển".

### 2.3 CASE (Computer Aided Software Engineering)
- 소프트웨어 개발 과정 전체 또는 일부를 자동화하는 전용 도구.
- **원천 기술 (Core Technologies):** 구조적 기법, 프로토타이핑, 자동 프로그래밍, 정보 저장소, 분산처리.
- **주요 기능 (Major Functions):** 생명 주기 전 단계 연결, 다양한 모델 지원, 그래픽 지원, 자료 흐름도 작성, 모순 검사 등.
- **Tiếng Việt:** Công cụ tự động hóa toàn bộ hoặc một phần quá trình phát triển phần mềm. Hỗ trợ đồ họa, vẽ sơ đồ, kiểm tra lỗi.
- **Example:**
  - *KR:* UML 설계 도구를 사용하여 코드를 자동 생성.
  - *VN:* Sử dụng công cụ thiết kế UML để tự động sinh code.
