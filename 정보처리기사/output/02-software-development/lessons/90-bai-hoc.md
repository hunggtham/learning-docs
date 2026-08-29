# 핵심 클린 코드 작성 원칙 (Clean Code Principles)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 클린 코드 작성 원칙 (Clean Code Principles)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

핵심, 클린, 코드, 작성, 원칙

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 핵심 클린 코드 작성 원칙 (Clean Code Principles)

- **클린 코드 (Clean Code):** 누구나 쉽게 이해하고 수정 및 추가할 수 있는 단순 명료한 코드. (Code sạch: Dễ hiểu, dễ sửa, dễ thêm tính năng.)
- **배드 코드 (Bad code):** 프로그램의 로직이 복잡하고 이해하기 어려운 코드. (Code rác: Lộn xộn, logic phức tạp.)
- **외계인 코드 (Alien Code):** 매우 오래되거나 참고 문서 또는 개발자가 없어 유지보수 작업이 매우 어려운 코드. (Code "người ngoài hành tinh": Code cổ đại, người viết đã nghỉ việc, không có tài liệu, đụng vào là hỏng.)

| 작성 원칙 (Nguyên tắc) | 설명 (Giải thích) |
|---|---|
| **가독성 (Readability)** | 누구든지 코드를 쉽게 읽을 수 있도록 작성. 이해하기 쉬운 용어, 들여쓰기. (Dễ đọc: Tên biến rõ ràng, thụt lề chuẩn.) |
| **단순성 (Simplicity)** | 한 번에 한 가지를 처리하도록 작성, 최소 단위로 분리. (Đơn giản: Mỗi hàm chỉ làm 1 việc duy nhất.) |
| **의존성 배제 (Independence)** | 다른 모듈에 미치는 영향을 최소화. (Độc lập: Đổi chỗ này không làm sập chỗ khác.) |
| **중복성 최소화 (Minimizing Duplication)** | 코드의 중복을 최소화, 공통된 코드 사용. (DRY - Don't Repeat Yourself: Không copy-paste code.) |
| **추상화 (Abstraction)** | 상위 수준에선 간략하게, 상세 내용은 하위에서 구현. (Trừu tượng hóa: Cái chung ở trên, cái chi tiết ở dưới.) |

- **Vietnamese Explanation:** Clean Code là "đạo đức" của lập trình viên. Đừng viết Alien Code (code không ai hiểu nổi trừ người viết ban đầu). 
- 💡 **Mẹo ghi nhớ (Mnemonics):** 5 nguyên tắc: Đọc - Đơn - Độc - Lặp - Trừu. (Đọc Đơn Độc Lặp Trừu (Đọc hiểu - Đơn giản - Độc lập - Không lặp - Trừu tượng)).

---

# Chapter 5. 인터페이스 구현 (Interface Implementation)
