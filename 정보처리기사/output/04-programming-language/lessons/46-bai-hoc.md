# 309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

OSI, 계층과, 네트워크, 프로토콜

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어**에서 만든 기준을 이어받아 **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)** và nối nó với **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)

Ở bước 46/91, **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)** xuất hiện như phần tiếp nối của **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **응용 계층 (Application, 7계층)**, **전송 계층 (Transport, 4계층)**, **TCP**, **UDP** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **응용 계층 (Application, 7계층)**: HTTP(웹), FTP(파일), SMTP(메일), DNS(도메인->IP 변환), SNMP(네트워크 관리).
- **전송 계층 (Transport, 4계층)**:
  - **TCP**: 연결형, 신뢰성 보장, 양방향. 흐름 제어.
  - **UDP**: 비연결형, 신뢰성 낮음. 속도가 빨라 스트리밍에 유리.
- **인터넷/네트워크 계층 (Network, 3계층)**: 라우터 사용.
  - **IP**: 경로 설정.
  - **ICMP**: 오류 보고 및 제어.
  - **ARP**: IP 주소 -> MAC 주소 변환. (**RARP**는 반대).
- **데이터 링크/네트워크 액세스 계층 (Data Link, 2계층)**: Ethernet(CSMA/CD 방식), HDLC.

**Giải thích (Vietnamese):**
- **ARP**: Khi biết địa chỉ IP, dùng ARP để hỏi xem "Máy nào có IP này, cho xin địa chỉ MAC của card mạng (phần cứng)".
- **ICMP**: Lệnh `ping` hay dùng trên máy tính chính là chạy giao thức ICMP để kiểm tra mạng có thông không.

---

Như vậy, **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.