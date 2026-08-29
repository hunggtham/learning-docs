# 44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

화이트박스, 테스트, 검증, 기준

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)
* **문장(구문) 검증 기준 (Statement Coverage)**: 소스 코드의 **모든 구문**이 한 번 이상 수행되도록 설계.
* **결정/분기 검증 기준 (Decision/Branch Coverage)**: 모든 조건문에 대해 조건이 **True인 경우와 False인 경우**가 한 번 이상 수행되도록 설계.
* **조건 검증 기준 (Condition Coverage)**: 조건문에 포함된 **개별 조건식**의 결과가 T/F 한 번 이상 수행되도록 설계.
* **분기/조건 기준 (Branch/Condition Coverage)**: 위 두 가지를 모두 만족하는 설계.
* **VI (Vietnamese) (Tiếng Việt):** Các tiêu chí độ phủ (Coverage) trong kiểm thử hộp trắng: Bao phủ cú pháp (Statement), Bao phủ nhánh/quyết định (Branch - lệnh IF chạy cả T/F), Bao phủ điều kiện (Condition - từng điều kiện nhỏ chạy cả T/F), Bao phủ nhánh/điều kiện.
* 💡 **Mẹo ghi nhớ**: Statement = Dòng code. Branch = Ngã rẽ (IF). Condition = Điều kiện nhỏ trong IF.
