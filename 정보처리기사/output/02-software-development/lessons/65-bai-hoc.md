# 55. APM (애플리케이션 성능 관리/모니터링)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **55. APM (애플리케이션 성능 관리/모니터링)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **55. APM (애플리케이션 성능 관리/모니터링)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **24. 인터페이스 보안 - 네트워크 영역 (Interface Security - Network Area)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

APM

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **50. 애플리케이션 성능 측정 지표 (Performance Metrics)**에서 만든 기준을 이어받아 **55. APM (애플리케이션 성능 관리/모니터링)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 55. APM (애플리케이션 성능 관리/모니터링)

Sau khi đã đặt nền bằng **50. 애플리케이션 성능 측정 지표 (Performance Metrics)**, ta chuyển sang **55. APM (애플리케이션 성능 관리/모니터링)**. Đây là mắt xích 65/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **55. APM (애플리케이션 성능 관리/모니터링)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **리소스 방식**, **엔드투엔드(End-to-End) 방식** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* 애플리케이션의 성능 관리를 위해 자원 현황, 트랜잭션 등을 모니터링.
* **리소스 방식**: Nagios, Zabbix, Cacti.
* **엔드투엔드(End-to-End) 방식**: VisualVM, 제니퍼(Jennifer), 스카우터(Scouter).
* **VI (Vietnamese) (Tiếng Việt):** Công cụ giám sát hiệu năng (APM). Có 2 loại: Theo dõi tài nguyên (Nagios) và Từ đầu đến cuối (VisualVM, Scouter).

---
*(이하 전자계산기 구조 파트 - Computer Architecture)*

---

Ta có thể khép mục **55. APM (애플리케이션 성능 관리/모니터링)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **24. 인터페이스 보안 - 네트워크 영역 (Interface Security - Network Area)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.