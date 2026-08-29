# 42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

애플리케이션, 테스트, 원리, 관련, 용어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)
* **결함 집중 (Defect Clustering) & 파레토 법칙**: 오류의 80%는 20%의 모듈에 집중됨.
* **살충제 패러독스 (Pesticide Paradox)**: 동일한 테스트 케이스로 반복 테스트하면 더 이상 새로운 결함을 찾을 수 없음. 주기적인 테스트 케이스 개선 필요.
* **오류-부재의 궤변 (Absence of Errors Fallacy)**: 결함이 0이더라도 사용자의 요구사항을 만족시키지 못하면 품질이 높다고 할 수 없음.
* **확인 (Validation)** vs **검증 (Verification)**:
  * 확인(Validation): **사용자** 입장에서 요구사항에 맞는지 테스트.
  * 검증(Verification): **개발자** 입장에서 명세서(스펙)에 맞는지 테스트.
* **VI (Vietnamese) (Tiếng Việt):** Nguyên lý kiểm thử:
  * Pesticide Paradox (Nghịch lý thuốc trừ sâu): Dùng mãi 1 kịch bản thì không bắt được lỗi mới.
  * Absence of Errors Fallacy: Không có lỗi không có nghĩa là phần mềm tốt nếu sai yêu cầu của khách hàng.
  * Validation: Đúng yêu cầu người dùng (Build the right product). Verification: Làm đúng kỹ thuật/tài liệu (Build the product right).
* **Example**: 로그인 버튼을 예쁘게 만들었지만(결함 없음), 고객이 원한 건 지문 인식 로그인이라면 이는 '오류-부재의 궤변'입니다.
