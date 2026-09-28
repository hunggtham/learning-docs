# 127 ~ 129: 화이트박스 테스트 (White Box Test)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **127 ~ 129: 화이트박스 테스트 (White Box Test)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

화이트박스, 테스트

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **130 & 131: 블랙박스 테스트 (Black Box Test)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **127 ~ 129: 화이트박스 테스트 (White Box Test)** và nối nó với **130 & 131: 블랙박스 테스트 (Black Box Test)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 127 ~ 129: 화이트박스 테스트 (White Box Test)

- 내부 로직과 제어 구조를 직접 관찰. (Test dựa trên source code. Nhìn thấu bên trong).
- **종류 (Các kỹ thuật):** 기초 경로 (Đường dẫn cơ bản), 조건 (Điều kiện), 루프 (Vòng lặp), 데이터 흐름 (Luồng dữ liệu).
- **검증 기준 (Coverage - Mức độ bao phủ):**
  - **문장 검증 (Statement):** Mọi dòng mã (code / 코드) phải chạy qua 1 lần.
  - **분기/결정 검증 (Branch/Decision):** Mọi nhánh lệnh (If True / False) phải chạy qua 1 lần.
  - **조건 검증 (Condition):** Mọi biểu thức điều kiện con bên trong If phải kiểm tra T/F.

- 💡 **Mẹo ghi nhớ (Mnemonics):** White Box = mã (code / 코드) (Câu lệnh, Rẽ nhánh, Vòng lặp). Do Dev tự làm.

---
