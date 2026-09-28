# 49. 테스트 하네스 구성 요소 (Test Harness Components)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **49. 테스트 하네스 구성 요소 (Test Harness Components)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

테스트, 하네스, 구성, 요소

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **48. 테스트 자동화 도구 (Test Automation Tools)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **49. 테스트 하네스 구성 요소 (Test Harness Components)** và nối nó với **핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 49. 테스트 하네스 구성 요소 (Test Harness Components)
* **드라이버(Driver)**: 하위 모듈 호출 (상향식).
* **스텁(Stub)**: 가짜 하위 모듈 (하향식).
* **슈트(Suites)**: 테스트 케이스의 집합.
* **케이스(Case)**: 입력 값, 실행 조건, 기대 결과 명세.
* **스크립트(Script)**: 테스트 실행 절차 명세(자동화).
* **목 오브젝트(Mock Object)**: 조건부 입력에 따라 상황에 맞는 행위를 수행하는 가짜 객체.
* **VI (Vietnamese) (Tiếng Việt):** Thành phần của kiểm thử (test / 테스트) Harness: Driver (gọi cấp dưới), Stub (giả cấp dưới), Suites (tập hợp TC), trường hợp (case / 사례) (kịch bản), Script (mã chạy tự động), Mock đối tượng (object / 객체).
