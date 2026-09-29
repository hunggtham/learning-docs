# 50. 애플리케이션 성능 측정 지표 (Performance Metrics)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **50. 애플리케이션 성능 측정 지표 (Performance Metrics)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **50. 애플리케이션 성능 측정 지표 (Performance Metrics)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **55. APM (애플리케이션 성능 관리/모니터링)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

애플리케이션, 성능, 측정, 지표

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)**에서 만든 기준을 이어받아 **50. 애플리케이션 성능 측정 지표 (Performance Metrics)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 50. 애플리케이션 성능 측정 지표 (Performance Metrics)

Ở bước 64/95, **50. 애플리케이션 성능 측정 지표 (Performance Metrics)** xuất hiện như phần tiếp nối của **132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **50. 애플리케이션 성능 측정 지표 (Performance Metrics)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **처리량 (Throughput)**, **응답 시간 (Response Time)**, **경과 시간 (Turn Around Time)**, **자원 사용률 (Resource Usage)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **처리량 (Throughput)**: 일정 시간 내 처리하는 일의 양.
* **응답 시간 (Response Time)**: 요청을 전달한 후 '응답이 도착할 때'까지 걸린 시간.
* **경과 시간 (Turn Around Time)**: 작업을 의뢰한 후 '처리가 완료될 때'까지 걸린 시간.
* **자원 사용률 (Resource Usage)**: CPU, 메모리, 네트워크 등의 자원 사용량.
* **VI (Vietnamese) (Tiếng Việt):** Các chỉ số hiệu năng: Thông lượng (Throughput), Thời gian phản hồi (Response), Thời gian hoàn thành (Turn Around), Mức sử dụng tài nguyên (Resource Usage).
* **Example**: 식당에서 주문하고 물이 나오는 시간(응답 시간), 음식을 다 먹고 나오는 시간(경과 시간).
* 💡 **Mẹo ghi nhớ**: Response = Phản hồi đầu tiên. Turn Around = Hoàn thành toàn bộ.

Như vậy, **50. 애플리케이션 성능 측정 지표 (Performance Metrics)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **55. APM (애플리케이션 성능 관리/모니터링)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.