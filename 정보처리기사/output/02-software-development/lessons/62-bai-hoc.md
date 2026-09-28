# 130 & 131: 블랙박스 테스트 (Black Box Test)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **130 & 131: 블랙박스 테스트 (Black Box Test)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

블랙박스, 테스트

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **127 ~ 129: 화이트박스 테스트 (White Box Test)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **130 & 131: 블랙박스 테스트 (Black Box Test)** và nối nó với **132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 130 & 131: 블랙박스 테스트 (Black Box Test)

- 명세를 기초로 기능 테스트. 내부 구조 무시. (Dựa vào chức năng UI, không thèm nhìn code).
- **종류 (Các kỹ thuật):**
  - **동치 분할 (Equivalence Partitioning):** Chia vùng tương đương (Nhập đại 1 số đại diện).
  - **경계값 분석 (Boundary Value):** kiểm thử (test / 테스트) quanh cái mép (Max, Min, +1, -1). Lỗi hay nằm ở đây.
  - **원인-효과 그래프 (Cause-Effect):** Vẽ biểu đồ nhân quả.
  - **오류 예측 (Error Guessing):** Dựa vào kinh nghiệm (Kinh nghiệm Tester).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Black Box = UI, Chức năng. Các kỹ thuật thường chia theo vùng (Partition) và ranh giới (boundary / 경계).

---
