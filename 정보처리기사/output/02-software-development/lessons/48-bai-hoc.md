# 45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

모델

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **46. 애플리케이션 테스트 프로세스 (Test Process)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계** và nối nó với **46. 애플리케이션 테스트 프로세스 (Test Process)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계
개발 단계와 테스트 단계를 짝지어 놓은 모델.
1. **단위 테스트 (Unit Test)** - *구현(Code)* 단계와 짝. 모듈/컴포넌트 초점 (주로 구조 기반/화이트박스).
2. **통합 테스트 (Integration Test)** - *설계(Design)* 단계와 짝. 모듈들을 결합하여 테스트.
   * **하향식 (Top-down)**: 스텁(Stub) 사용. 깊이/넓이 우선. 테스트 초기부터 시스템 구조 파악 가능.
   * **상향식 (Bottom-up)**: 드라이버(Driver)와 클러스터(Cluster) 사용.
3. **시스템 테스트 (System Test)** - *분석(Specification)* 단계와 짝. 실제 환경과 유사하게 구성, 기능적/비기능적 요구사항 점검.
4. **인수 테스트 (Acceptance Test)** - *요구사항(Requirements)* 단계와 짝. 사용자가 직접 테스트. (알파/베타 테스트).
* **VI (Vietnamese) (Tiếng Việt):** Mô hình chữ V (V-Model). mã (code / 코드) <-> đơn vị (unit / 단위), thiết kế (design / 설계) <-> tích hợp (integration / 통합), phân tích (analysis / 분석) <-> hệ thống (system / 시스템), Requirements <-> Acceptance.
* **Example**: 코드 짠 사람이 직접 해보는 건 단위 테스트, 고객이 요구사항대로 됐는지 최종 확인하는 건 인수 테스트입니다.
