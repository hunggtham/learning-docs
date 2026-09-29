# 53. EAI와 ESB 심화 (EAI vs ESB)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **53. EAI와 ESB 심화 (EAI vs ESB)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **53. EAI와 ESB 심화 (EAI vs ESB)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **54. XML 및 데이터 무결성 검사 도구 (XML & Integrity Check Tools)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

ESB, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)**에서 만든 기준을 이어받아 **53. EAI와 ESB 심화 (EAI vs ESB)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **53. EAI와 ESB 심화 (EAI vs ESB)** và nối nó với **54. XML 및 데이터 무결성 검사 도구 (XML & Integrity Check Tools)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 53. EAI와 ESB 심화 (EAI vs ESB)

Ở bước 85/95, **53. EAI와 ESB 심화 (EAI vs ESB)** xuất hiện như phần tiếp nối của **52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **53. EAI와 ESB 심화 (EAI vs ESB)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **EAI**, **ESB (Enterprise Service Bus)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **EAI**: 기업 내 애플리케이션들을 연동하는 솔루션 (Point-to-Point, Hub&Spoke, Message Bus, Hybrid).
* **ESB (Enterprise Service Bus)**: 애플리케이션 간 표준 기반 인터페이스 제공. 애플리케이션 통합보다는 **서비스 중심 통합** 지향. 결합도(Coupling)를 **약하게(Loosely)** 유지.
* **VI (Vietnamese) (Tiếng Việt):** So sánh EAI và ESB. EAI tập trung tích hợp ứng dụng, ESB tập trung tích hợp dịch vụ (Service-oriented) với độ kết dính lỏng lẻo (Loosely coupled) dùng tiêu chuẩn chung.

Như vậy, **53. EAI와 ESB 심화 (EAI vs ESB)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **54. XML 및 데이터 무결성 검사 도구 (XML & Integrity Check Tools)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.