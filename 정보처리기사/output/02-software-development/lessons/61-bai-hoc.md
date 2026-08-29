# 127 ~ 129: 화이트박스 테스트 (White Box Test)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **127 ~ 129: 화이트박스 테스트 (White Box Test)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

화이트박스, 테스트

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 127 ~ 129: 화이트박스 테스트 (White Box Test)

- 내부 로직과 제어 구조를 직접 관찰. (Test dựa trên mã nguồn (Source Code). Nhìn thấu bên trong).
- **종류 (Các kỹ thuật):** 기초 경로 (Đường dẫn cơ bản), 조건 (Điều kiện), 루프 (Vòng lặp), 데이터 흐름 (Luồng dữ liệu).
- **검증 기준 (Coverage - Mức độ bao phủ):**
  - **문장 검증 (Statement):** Mọi dòng code phải chạy qua 1 lần.
  - **분기/결정 검증 (Branch/Decision):** Mọi nhánh lệnh (If True / False) phải chạy qua 1 lần.
  - **조건 검증 (Condition):** Mọi biểu thức điều kiện con bên trong If phải kiểm tra T/F.

- 💡 **Mẹo ghi nhớ (Mnemonics):** White Box = Code (Câu lệnh, Rẽ nhánh, Vòng lặp). Do Dev tự làm.

---
