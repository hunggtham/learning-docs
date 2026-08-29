# 47. 테스트 오라클의 종류 (Types of Test Oracles)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **47. 테스트 오라클의 종류 (Types of Test Oracles)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

테스트, 오라클의, 종류

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 47. 테스트 오라클의 종류 (Types of Test Oracles)
* **참(True) 오라클**: 모든 입력값에 대해 결과를 제공 (모든 오류 검출).
* **샘플링(Sampling) 오라클**: 특정한 몇몇 입력값에 대해서만 결과 제공.
* **추정(Heuristic) 오라클**: 샘플링 + 나머지 값들은 추정(직관)으로 처리.
* **일관성 검사(Consistent) 오라클**: 변경 전후의 결과값이 동일한지 확인.
* **VI (Vietnamese) (Tiếng Việt):** Các loại Test Oracle: Chân lý (True - biết hết kết quả), Lấy mẫu (Sampling - biết vài cái), Ước lượng (Heuristic - kết hợp lấy mẫu và đoán), Nhất quán (Consistent - trước sau như một).
