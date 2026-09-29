# 핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 044: 테스트 자동화 도구 (Test Automation Tools)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

핵심, 단위, 통합, 시스템, 인수, 테스트

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)**에서 만든 기준을 이어받아 **핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)

Sau khi đã đặt nền bằng **핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)**, ta chuyển sang **핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)**. Đây là mắt xích 56/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Thứ tự Test từ nhỏ đến lớn: **단위 (Unit) → 통합 (Integration) → 시스템 (System) → 인수 (Acceptance)**.

| 단계 (Giai đoạn) | 설명 (Giải thích) | 방식 / 기법 (Cách thức) |
|---|---|---|
| **단위 (Unit Test)** | Test từng Module, hàm độc lập. | White-box, Black-box, Test cấu trúc dữ liệu. |
| **통합 (Integration)** | Nối các module lại và test sự giao tiếp giữa chúng. | - **빅뱅 (Big Bang):** Gom tất cả test 1 lần (dễ bị rối).
- **상향식 (Bottom-Up):** Dưới lên. Cần **Driver** (Trình điều khiển giả).
- **하향식 (Top-Down):** Trên xuống. Cần **Stub** (Mô đun con giả mạo). |
| **시스템 (System)** | Test toàn bộ hệ thống xem có đúng yêu cầu (Chức năng + Hiệu năng). | Yêu cầu chức năng và phi chức năng. |
| **인수 (Acceptance)** | Khách hàng/Người dùng cuối tự test để nghiệm thu. | - **알파 (Alpha):** Khách hàng test tại cty lập trình viên, có dev đứng ngó.
- **베타 (Beta):** Tung ra cho nhiều người dùng tự test ở nhà (Field Test), tự do. |

- **Vietnamese Explanation:** Tích hợp (Integration) rất hay ra thi. Nếu ráp từ dưới lên (Bottom-up) thì module con xong rồi, nhưng thiếu thằng gọi nó => Cần viết cục **Driver** giả để gọi. Nếu ráp từ trên xuống (Top-down), module chính có rồi nhưng chưa viết xong module con => Cần viết cục **Stub** (Cục gạch giả) để thế chỗ. Alpha test là test "nội bộ" có kiểm soát, Beta test là "open beta" như game.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Từ trên xuống (Top-Down) = Stub (Top-Stub / T-S). 상향식 (Bottom-Up) = Driver (Bottom-Driver / B-D). Alpha = Ở cty Dev. Beta = Ở nhà.

---

Ta có thể khép mục **핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **핵심 044: 테스트 자동화 도구 (Test Automation Tools)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.