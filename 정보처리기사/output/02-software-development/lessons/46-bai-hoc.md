# 43. 테스트 분류 방식 (Test Classification)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **43. 테스트 분류 방식 (Test Classification)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

테스트, 분류, 방식

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 43. 테스트 분류 방식 (Test Classification)
* **실행 여부에 따른 분류**:
  * **정적 테스트 (Static)**: 프로그램 실행 없이 분석. (워크스루, 인스펙션, 코드 검사).
  * **동적 테스트 (Dynamic)**: 프로그램을 직접 실행하며 테스트. (블랙박스, 화이트박스).
* **기반(Bases)에 따른 분류**:
  * **명세 기반 (Specification)**: 요구사항 명세서를 빠짐없이 테스트. (동등 분할, 경계값).
  * **구조 기반 (Structure)**: 내부 논리 흐름(코드)에 따라 테스트. (구문, 결정, 조건 기반).
  * **경험 기반 (Experience)**: 테스터의 경험 직관에 의존. (에러 추정, 탐색적 테스팅).
* **목적에 따른 분류**:
  * **회복 (Recovery)**: 일부러 실패하게 한 후 복구되는지 확인.
  * **안전 (Security)**: 불법 침입으로부터 보호 확인.
  * **강도 (Stress)**: 과부하(Overload) 상태에서 정상 동작하는지.
  * **성능 (Performance)**: 응답 시간, 처리량 등 효율성 진단.
  * **회귀 (Regression)**: 코드를 수정한 후 **새로운 결함**이 발생하지 않았는지 확인.
  * **병행 (Parallel)**: 변경된 시스템과 기존 시스템에 동일 데이터 입력 후 결과 비교.
* **VI (Vietnamese) (Tiếng Việt):** Phân loại kiểm thử.
  * Theo thực thi: Tĩnh (không chạy code - Review) và Động (chạy code).
  * Theo cơ sở: Dựa trên Đặc tả (Spec), Cấu trúc (Code), Kinh nghiệm.
  * Theo mục đích: Phục hồi (Recovery), Áp lực (Stress - quá tải), Hồi quy (Regression - test lại sau khi sửa code), Song song (Parallel).
* **Example**: 버그를 고치고 나서 다른 곳에 문제가 안 생겼는지 다시 테스트하는 것이 '회귀 테스트'입니다. (Kiểm tra lại sau khi sửa lỗi là Regression Test).
