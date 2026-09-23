# 9. 효과적인 모듈 설계 방안 (Effective Module Design)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **9. 효과적인 모듈 설계 방안 (Effective Module Design)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

효과적인, 모듈, 설계, 방안

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 9. 효과적인 모듈 설계 방안 (Effective Module Design)
*   **Korean:** 결합도↓, 응집도↑. 모듈의 영향 영역(Scope of Effect)이 제어 영역(Scope of Control) 안에 있어야 함. 단일 입구/단일 출구(Single Entry, Single Exit). 복잡도와 중복성 감소.
*   **VI (Vietnamese) (Tiếng Việt):** Coupling thấp, Cohesion cao. **Phạm vi ảnh hưởng (Scope of Effect) phải nằm TRONG Phạm vi kiểm soát (Scope of Control)** của module. Chỉ có 1 đầu vào và 1 đầu ra. Giảm độ phức tạp và dư thừa.
*   **Example:** Một hàm sắp xếp chỉ nên thay đổi mảng truyền vào nó (trong vùng kiểm soát), không nên vô tình thay đổi giao diện UI (vùng ảnh hưởng ngoài kiểm soát).

---
