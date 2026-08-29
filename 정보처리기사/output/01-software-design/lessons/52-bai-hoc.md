# 5. Fan-In / Fan-Out (팬인 / 팬아웃)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **5. Fan-In / Fan-Out (팬인 / 팬아웃)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

Fan-In, Fan-Out

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 5. Fan-In / Fan-Out (팬인 / 팬아웃)
**개념 (Khái niệm):** 모듈 간의 호출 관계를 나타내는 지표 (Chỉ số thể hiện mức độ gọi lẫn nhau giữa các module).

*   **Fan-In (들어옴 / Đi vào):**
    *   **Korean:** 나를 호출하는 모듈 수. **높게(High)** 설계하는 것이 재사용성 측면에서 좋음. (단, 단일 장애점 주의)
    *   **VI (Vietnamese) (Tiếng Việt):** Số lượng module gọi đến module hiện tại. Fan-In CAO là tốt vì chứng tỏ module được tái sử dụng nhiều, nhưng cần cẩn thận vì nó là trung tâm (Single Point of Failure).
*   **Fan-Out (나감 / Đi ra):**
    *   **Korean:** 내가 호출하는 모듈 수. **낮게(Low)** 설계하여 단순화해야 함.
    *   **VI (Vietnamese) (Tiếng Việt):** Số lượng module mà module hiện tại gọi. Fan-Out THẤP là tốt, tránh việc module phụ thuộc vào quá nhiều nơi khác.

💡 **Mẹo ghi nhớ:** Fan-In = Gọi VÀO tôi (High is good) / Fan-Out = Tôi gọi RA (Low is good).

---
