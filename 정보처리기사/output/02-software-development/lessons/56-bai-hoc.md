# 핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

핵심, 단위, 통합, 시스템, 인수, 테스트

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)

Thứ tự Test từ nhỏ đến lớn: **단위 (Unit) → 통합 (Integration) → 시스템 (System) → 인수 (Acceptance)**.

| 단계 (Giai đoạn) | 설명 (Giải thích) | 방식 / 기법 (Cách thức) |
|---|---|---|
| **단위 (Unit Test)** | Test từng Module, hàm độc lập. | White-box, Black-box, Test cấu trúc dữ liệu. |
| **통합 (Integration)** | Nối các module lại và test sự giao tiếp giữa chúng. | - **빅뱅 (Big Bang):** Gom tất cả test 1 lần (dễ bị rối).<br>- **상향식 (Bottom-Up):** Dưới lên. Cần **Driver** (Trình điều khiển giả).<br>- **하향식 (Top-Down):** Trên xuống. Cần **Stub** (Mô đun con giả mạo). |
| **시스템 (System)** | Test toàn bộ hệ thống xem có đúng yêu cầu (Chức năng + Hiệu năng). | Yêu cầu chức năng và phi chức năng. |
| **인수 (Acceptance)** | Khách hàng/Người dùng cuối tự test để nghiệm thu. | - **알파 (Alpha):** Khách hàng test tại cty lập trình viên, có dev đứng ngó.<br>- **베타 (Beta):** Tung ra cho nhiều người dùng tự test ở nhà (Field Test), tự do. |

- **Vietnamese Explanation:** Tích hợp (Integration) rất hay ra thi. Nếu ráp từ dưới lên (Bottom-up) thì module con xong rồi, nhưng thiếu thằng gọi nó => Cần viết cục **Driver** giả để gọi. Nếu ráp từ trên xuống (Top-down), module chính có rồi nhưng chưa viết xong module con => Cần viết cục **Stub** (Cục gạch giả) để thế chỗ. Alpha test là test "nội bộ" có kiểm soát, Beta test là "open beta" như game.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Từ trên xuống (Top-Down) = Stub (Top-Stub / T-S). 상향식 (Bottom-Up) = Driver (Bottom-Driver / B-D). Alpha = Ở cty Dev. Beta = Ở nhà.

---
