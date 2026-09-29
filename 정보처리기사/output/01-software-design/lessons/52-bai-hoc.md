# 5. Fan-In / Fan-Out (팬인 / 팬아웃)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **5. Fan-In / Fan-Out (팬인 / 팬아웃)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **5. Fan-In / Fan-Out (팬인 / 팬아웃)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **6. N-S 차트 (Nassi-Schneiderman Chart)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

Fan-In, Fan-Out

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **4. 응집도 (Cohesion - Độ gắn kết)**에서 만든 기준을 이어받아 **5. Fan-In / Fan-Out (팬인 / 팬아웃)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 5. Fan-In / Fan-Out (팬인 / 팬아웃)

Ở bước 52/55, **5. Fan-In / Fan-Out (팬인 / 팬아웃)** xuất hiện như phần tiếp nối của **4. 응집도 (Cohesion - Độ gắn kết)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **5. Fan-In / Fan-Out (팬인 / 팬아웃)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 모듈 간의 호출 관계를 나타내는 지표 (Chỉ số thể hiện mức độ gọi lẫn nhau giữa các module).

*   **Fan-In (들어옴 / Đi vào):**
    *   **Korean:** 나를 호출하는 모듈 수. **높게(High)** 설계하는 것이 재사용성 측면에서 좋음. (단, 단일 장애점 주의)
    *   **VI (Vietnamese) (Tiếng Việt):** Số lượng module gọi đến module hiện tại. Fan-In CAO là tốt vì chứng tỏ module được tái sử dụng nhiều, nhưng cần cẩn thận vì nó là trung tâm (Single Point of Failure).
*   **Fan-Out (나감 / Đi ra):**
    *   **Korean:** 내가 호출하는 모듈 수. **낮게(Low)** 설계하여 단순화해야 함.
    *   **VI (Vietnamese) (Tiếng Việt):** Số lượng module mà module hiện tại gọi. Fan-Out THẤP là tốt, tránh việc module phụ thuộc vào quá nhiều nơi khác.

💡 **Mẹo ghi nhớ:** Fan-In = Gọi VÀO tôi (High is good) / Fan-Out = Tôi gọi RA (Low is good).

---

Như vậy, **5. Fan-In / Fan-Out (팬인 / 팬아웃)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **6. N-S 차트 (Nassi-Schneiderman Chart)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.