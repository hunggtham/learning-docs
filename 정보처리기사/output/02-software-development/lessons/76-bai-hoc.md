# 23. EAI 구축 유형 (Enterprise Application Integration Types)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **23. EAI 구축 유형 (Enterprise Application Integration Types)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **23. EAI 구축 유형 (Enterprise Application Integration Types)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **25. 트립와이어 (tripwire)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

EAI, 구축, 유형

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **22. 정적 분석 도구 (Static Analysis Tools)**에서 만든 기준을 이어받아 **23. EAI 구축 유형 (Enterprise Application Integration Types)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 23. EAI 구축 유형 (Enterprise Application Integration Types)

Ở bước 76/95, **23. EAI 구축 유형 (Enterprise Application Integration Types)** xuất hiện như phần tiếp nối của **22. 정적 분석 도구 (Static Analysis Tools)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **23. EAI 구축 유형 (Enterprise Application Integration Types)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **Point-to-Point**, **Hub & Spoke**, **Message Bus (ESB 방식)**, **Hybrid** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **Point-to-Point**: 애플리케이션을 1:1로 직접 연결.
* **Hub & Spoke**: 단일 접점인 허브 시스템을 통해 데이터를 전송하는 중앙 집중형 방식.
* **Message Bus (ESB 방식)**: 애플리케이션 사이에 미들웨어를 두어 처리하는 방식.
* **Hybrid**: Hub & Spoke와 Message Bus의 혼합 방식.
* **VI (Vietnamese) (Tiếng Việt):** Các kiểu kiến trúc tích hợp hệ thống (EAI).
  * Point-to-Point: Nối 1-1.
  * Hub & Spoke: Tập trung qua 1 Hub trung tâm.
  * Message Bus: Dùng middleware (trục thông điệp).
  * Hybrid: Lai giữa Hub & Spoke và Message Bus.
* **Example**: 여러 부서의 시스템을 가운데 중앙 서버 하나(Hub)를 통해 연결하는 방식이 Hub & Spoke입니다.
* 💡 **Mẹo ghi nhớ**: Hub là cái trục xe đạp (trung tâm), Spoke là nan hoa (tỏa ra xung quanh).

Như vậy, **23. EAI 구축 유형 (Enterprise Application Integration Types)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **25. 트립와이어 (tripwire)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.