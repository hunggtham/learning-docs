# 245. 연산자 우선순위 (Operator Precedence)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **245. 연산자 우선순위 (Operator Precedence)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

연산자, 우선순위

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **244. 조건(삼항) 연산자 (Ternary Operator)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **입출력 (Input/Output)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **245. 연산자 우선순위 (Operator Precedence)** và nối nó với **입출력 (Input/Output)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 245. 연산자 우선순위 (Operator Precedence)
- 하나의 수식에 여러 연산자가 있을 때 계산되는 순서.
- 순위: **단항**(`!`, `++`, `~`) > **산술**(`*`, `/` > `+`, `-`) > **관계**(`>`, `==`) > **논리**(`&&` > `||`) > **대입**(`=`, `+=`).
- 괄호 `()`가 가장 우선.

**Giải thích (Vietnamese):**
Thứ tự ưu tiên tính toán: Ngoặc () -> Đơn nguyên (phủ định, tăng giảm) -> Nhân chia cộng trừ -> So sánh -> lô-gic (logic / 논리) (AND trước OR sau) -> Gán.

**💡 Mẹo ghi nhớ (Mnemonics):**
**단산관논대** (Đơn - Toán - Quan - Luận - Gán): 단항 -> 산술 -> 관계 -> 논리 -> 대입.

---
