# 기본 프로토콜 (Basic Protocols)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **기본 프로토콜 (Basic Protocols)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **기본 프로토콜 (Basic Protocols)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

기본, 프로토콜

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **6. 통신 프로토콜 (Giao thức Truyền thông)**에서 만든 기준을 이어받아 **기본 프로토콜 (Basic Protocols)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **기본 프로토콜 (Basic Protocols)** và nối nó với **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 기본 프로토콜 (Basic Protocols)

Từ **6. 통신 프로토콜 (Giao thức Truyền thông)**, ta đã có điểm tựa để bước vào **기본 프로토콜 (Basic Protocols)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 24/61 trước khi đi vào chi tiết.

Để đọc **기본 프로토콜 (Basic Protocols)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **ARP**, **RARP**, **RTCP**, **WAP** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **ARP**: 호스트의 IP 주소(논리 주소)를 호스트와 연결된 네트워크 접속장치의 물리적 주소(MAC Address)로 변환함.
  * *Tiếng Việt*: Chuyển đổi địa chỉ IP (địa chỉ logic) của máy chủ thành địa chỉ vật lý (MAC Address) của thiết bị kết nối mạng.
  * *Ví dụ (Example)*: 컴퓨터가 IP 192.168.1.5의 MAC 주소를 찾을 때 ARP를 사용합니다. (Máy tính sử dụng ARP để tìm địa chỉ MAC của IP 192.168.1.5)
  * 💡 *Mnemonic*: **A**ddress **R**esolution (IP -> MAC)
* **RARP**: 물리적 주소를 IP 주소(논리 주소)로 변환함.
  * *Tiếng Việt*: Chuyển đổi địa chỉ vật lý thành địa chỉ IP (địa chỉ logic).
  * 💡 *Mnemonic*: **R**everse ARP (MAC -> IP)
* **RTCP**: 실시간 전송 프로토콜(RTP)이 안정되게 기능을 유지하도록 데이터 전송을 모니터링하고 최소한의 제어와 인증 기능을 제공함.
  * *Tiếng Việt*: Giám sát truyền dữ liệu và cung cấp chức năng điều khiển, xác thực tối thiểu để duy trì ổn định RTP.
* **WAP**: 이동 단말이나 PDA 등 소형 무선 단말기에서 인터넷을 이용할 수 있도록 해주는 프로토콜.
  * *Tiếng Việt*: Giao thức cho phép sử dụng internet trên các thiết bị không dây nhỏ như điện thoại di động, PDA.
* **PPP**: 주로 두 개의 라우터를 접속할 때 사용되며, 오류 검출 기능만 제공됨.
  * *Tiếng Việt*: Chủ yếu dùng để kết nối 2 router, chỉ cung cấp chức năng phát hiện lỗi (không phục hồi/điều khiển luồng).
* **UDP (User Datagram Protocol)**: 데이터 전송 전에는 연결을 설정하지 않는 비연결형 서비스. 오버헤드가 적고 실시간 전송에 유리.
  * *Tiếng Việt*: Dịch vụ không kết nối (không thiết lập kết nối trước khi truyền). Ít overhead, thuận lợi cho truyền thời gian thực (tốc độ quan trọng hơn độ tin cậy).
  * *Ví dụ*: 실시간 스트리밍(Video streaming)에 주로 사용됩니다. (Thường dùng cho phát video trực tiếp).

---

Điểm chốt của **기본 프로토콜 (Basic Protocols)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.