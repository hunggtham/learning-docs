# 15. 화이트박스 vs 블랙박스 테스트 (White-box vs Black-box Testing)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **15. 화이트박스 vs 블랙박스 테스트 (White-box vs Black-box Testing)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

화이트박스, 블랙박스, 테스트

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 15. 화이트박스 vs 블랙박스 테스트 (White-box vs Black-box Testing)
* **화이트박스 테스트**: 원시 코드를 오픈시킨 상태에서 논리적 경로(제어 구조)를 테스트.
  * **종류**: 기초 경로 검사 (Base Path), 제어 구조 검사 (조건, 루프, 데이터 흐름).
* **블랙박스 테스트**: 기능이 제대로 작동하는지 외부에서 테스트 (내부 구조 안 봄).
  * **종류**: 동치 분할 (Equivalence Partitioning), 경계값 분석 (Boundary Value), 원인-효과 그래프 (Cause-Effect), 오류 예측 (Error Guessing), 비교 검사 (Comparison).
* **VI (Vietnamese) (Tiếng Việt):**
  * White-box: Nhìn thấy code bên trong (kiểm tra đường dẫn, vòng lặp).
  * Black-box: Không nhìn thấy code, chỉ kiểm tra đầu vào/đầu ra (kiểm tra tính năng).
* **Example**: 화이트박스는 코드의 `if-else` 모든 경로를 실행해보는 것이고, 블랙박스는 로그인 창에 ID/PW를 넣어보는 것입니다.
* 💡 **Mẹo ghi nhớ**: White = Nhìn xuyên thấu (Code). Black = Hộp đen không thấy ruột (Chức năng).
