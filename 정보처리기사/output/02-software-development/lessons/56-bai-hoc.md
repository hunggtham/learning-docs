# 핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

핵심, 단위, 통합, 시스템, 인수, 테스트

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **핵심 044: 테스트 자동화 도구 (Test Automation Tools)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)** và nối nó với **핵심 044: 테스트 자동화 도구 (Test Automation Tools)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)

Thứ tự kiểm thử (test / 테스트) từ nhỏ đến lớn: **단위 (Unit) → 통합 (Integration) → 시스템 (System) → 인수 (Acceptance)**.

| 단계 (Giai đoạn) | 설명 (Giải thích) | 방식 / 기법 (Cách thức) |
|---|---|---|
| **단위 (Unit Test)** | kiểm thử (test / 테스트) từng mô-đun (module / 모듈), hàm độc lập. | White-box, Black-box, kiểm thử (test / 테스트) cấu trúc dữ liệu. |
| **통합 (Integration)** | Nối các mô-đun (module / 모듈) lại và kiểm thử (test / 테스트) sự giao tiếp giữa chúng. | - **빅뱅 (Big Bang):** Gom tất cả kiểm thử (test / 테스트) 1 lần (dễ bị rối).<br>- **상향식 (Bottom-Up):** Dưới lên. Cần **Driver** (Trình điều khiển giả).<br>- **하향식 (Top-Down):** Trên xuống. Cần **Stub** (Mô đun con giả mạo). |
| **시스템 (System)** | kiểm thử (test / 테스트) toàn bộ hệ thống xem có đúng yêu cầu (Chức năng + Hiệu năng). | Yêu cầu chức năng và phi chức năng. |
| **인수 (Acceptance)** | Khách hàng/Người dùng cuối tự kiểm thử (test / 테스트) để nghiệm thu. | - **알파 (Alpha):** Khách hàng kiểm thử (test / 테스트) tại cty lập trình viên, có dev đứng ngó.<br>- **베타 (Beta):** Tung ra cho nhiều người dùng tự kiểm thử (test / 테스트) ở nhà (Field Test), tự do. |

- **Vietnamese Explanation:** tích hợp (integration / 통합) rất hay ra thi. Nếu ráp từ dưới lên (Bottom-up) thì mô-đun (module / 모듈) con xong rồi, nhưng thiếu thằng gọi nó => Cần viết cục **Driver** giả để gọi. Nếu ráp từ trên xuống (Top-down), mô-đun (module / 모듈) chính có rồi nhưng chưa viết xong mô-đun (module / 모듈) con => Cần viết cục **Stub** (Cục gạch giả) để thế chỗ. Alpha kiểm thử (test / 테스트) là kiểm thử (test / 테스트) "nội bộ" có kiểm soát, Beta kiểm thử (test / 테스트) là "open beta" như game.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Từ trên xuống (Top-Down) = Stub (Top-Stub / T-S). 상향식 (Bottom-Up) = Driver (Bottom-Driver / B-D). Alpha = Ở cty Dev. Beta = Ở nhà.

---
