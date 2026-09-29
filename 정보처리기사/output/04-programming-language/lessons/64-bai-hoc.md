# 238. 가비지 콜렉터 (Garbage Collector)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **238. 가비지 콜렉터 (Garbage Collector)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **238. 가비지 콜렉터 (Garbage Collector)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **250. JAVA에서의 표준 출력 (Standard Output in JAVA)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

가비지, 콜렉터

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **234. C언어의 구조체 (struct in C)**에서 만든 기준을 이어받아 **238. 가비지 콜렉터 (Garbage Collector)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 238. 가비지 콜렉터 (Garbage Collector)

Ở bước 64/77, **238. 가비지 콜렉터 (Garbage Collector)** xuất hiện như phần tiếp nối của **234. C언어의 구조체 (struct in C)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **238. 가비지 콜렉터 (Garbage Collector)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 더 이상 사용되지 않고 메모리를 점유하고 있는 변수/객체를 시스템이 **자동으로 해제**하여 자원을 회수하는 모듈.
- 메모리 누수(Memory Leak)를 방지. JAVA 등에서 사용됨.

**Giải thích (Vietnamese):**
"Người dọn rác" tự động. Bạn cứ việc tạo biến dùng, khi không dùng nữa, hệ thống sẽ tự động xoá nó khỏi RAM để giải phóng bộ nhớ. Trong C/C++ bạn phải tự dọn dẹp, nhưng Java/Python có tính năng này.

---

Như vậy, **238. 가비지 콜렉터 (Garbage Collector)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **250. JAVA에서의 표준 출력 (Standard Output in JAVA)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.