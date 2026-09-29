# 네트워크 통신 (Network Communication)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **네트워크 통신 (Network Communication)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **네트워크 통신 (Network Communication)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **네트워크 프로토콜 및 장비 심화 (Network Protocols & Devices - Advanced)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

네트워크, 통신

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**에서 만든 기준을 이어받아 **네트워크 통신 (Network Communication)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **네트워크 통신 (Network Communication)** và nối nó với **네트워크 프로토콜 및 장비 심화 (Network Protocols & Devices - Advanced)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 네트워크 통신 (Network Communication)

Từ **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**, ta đã có điểm tựa để bước vào **네트워크 통신 (Network Communication)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 45/78 trước khi đi vào chi tiết.

Để đọc **네트워크 통신 (Network Communication)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **209. 데이터 링크 계층 (Data Link)**, **210. 네트워크 계층 (Network)**, **211. 전송 계층 (Transport)**, **212. 세션 계층 (Session)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **207. 인터넷 주소 체계 - IPv4 (IPv4 Addressing)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 207. 인터넷 주소 체계 - IPv4 (IPv4 Addressing)

Các ý ngay dưới **207. 인터넷 주소 체계 - IPv4 (IPv4 Addressing)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 8비트씩 4부분, 총 32비트 (4 phần, mỗi phần 8 bit -> 32 bit). A~E 클래스.

Các bullet của **207. 인터넷 주소 체계 - IPv4 (IPv4 Addressing)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **207. 인터넷 주소 체계 - IPv4 (IPv4 Addressing)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **208. 인터넷 주소 체계 - IPv6 (IPv6 Addressing)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **208. 인터넷 주소 체계 - IPv6 (IPv6 Addressing)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 208. 인터넷 주소 체계 - IPv6 (IPv6 Addressing)

Bây giờ ta đi vào nội dung của **208. 인터넷 주소 체계 - IPv6 (IPv6 Addressing)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 16비트씩 8부분, 총 128비트 (8 phần, mỗi phần 16 bit -> 128 bit, dùng hệ Hex).
- 유니캐스트(Unicast), 멀티캐스트(Multicast), 애니캐스트(Anycast).
  - 💡 *Mẹo ghi nhớ*: IPv4 = 32 bit (dấu `.`). IPv6 = 128 bit (dấu `:`).

Với **208. 인터넷 주소 체계 - IPv6 (IPv6 Addressing)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **208. 인터넷 주소 체계 - IPv6 (IPv6 Addressing)**, đừng bắt đầu lại từ số không. **OSI 7계층 (OSI 7 Layers)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **OSI 7계층 (OSI 7 Layers)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### OSI 7계층 (OSI 7 Layers)

Phần nguồn của **OSI 7계층 (OSI 7 Layers)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **209. 데이터 링크 계층 (Data Link)**: 인접 시스템 간 신뢰성 있는 전송. 흐름/오류 제어 (HDLC, PPP). (Truyền tải tin cậy giữa các nút lân cận).
- **210. 네트워크 계층 (Network)**: 경로 설정, 패킷 라우팅. (Định tuyến, chuyển mạch gói).
- **211. 전송 계층 (Transport)**: 종단 간 투명한 데이터 전송. (Truyền tải End-to-End, TCP/UDP).
- **212. 세션 계층 (Session)**: 대화 제어, 동기화 (Quản lý phiên, đồng bộ hóa hội thoại).
  - 💡 *Mẹo ghi nhớ*: Data Link = Frame/MAC. Network = IP/Routing. Transport = TCP/UDP/Port. Session = Dialog/Token.

Với **OSI 7계층 (OSI 7 Layers)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**OSI 7계층 (OSI 7 Layers)** vừa cho ta cách đặt câu hỏi. Bây giờ **213. 네트워크 관련 주요 장비 (Network Devices / Thiết bị mạng)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **213. 네트워크 관련 주요 장비 (Network Devices / Thiết bị mạng)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 213. 네트워크 관련 주요 장비 (Network Devices / Thiết bị mạng)

Các ý ngay dưới **213. 네트워크 관련 주요 장비 (Network Devices / Thiết bị mạng)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **리피터 (Repeater)**: 신호 재생 (Khuếch đại tín hiệu).
- **브리지 (Bridge)**: LAN 연결 (Kết nối mạng LAN cùng loại).
- **라우터 (Router)**: 최적 경로 선택 (Chọn đường đi tối ưu).
- **스위치 (Switch)**: 여러 랜선 연결 (Chuyển mạch mạng LAN).
- **브라우터 (Brouter)**: Bridge + Router.

Các bullet của **213. 네트워크 관련 주요 장비 (Network Devices / Thiết bị mạng)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **213. 네트워크 관련 주요 장비 (Network Devices / Thiết bị mạng)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **TCP/IP 프로토콜 (TCP/IP Protocols)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **TCP/IP 프로토콜 (TCP/IP Protocols)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### TCP/IP 프로토콜 (TCP/IP Protocols)

Bây giờ ta đi vào nội dung của **TCP/IP 프로토콜 (TCP/IP Protocols)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **214. MQTT**: IoT에서 사용하는 발행-구독 메시징 (Giao thức Publish/Subscribe cho IoT).
- **215. TCP**: 신뢰성 있는 양방향 연결형 서비스 (Kết nối hai chiều, đáng tin cậy).
- **216. UDP**: 비연결형, 빠른 속도, 실시간 전송 유리 (Không kết nối, truyền nhanh, hợp với Real-time).
  - 💡 *Mẹo ghi nhớ*: TCP = Cẩn thận, chậm mà chắc. UDP = Nhanh, mất gói cũng không sao (Video call, Game).

Với **TCP/IP 프로토콜 (TCP/IP Protocols)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **TCP/IP 프로토콜 (TCP/IP Protocols)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **네트워크 통신 (Network Communication)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **네트워크 프로토콜 및 장비 심화 (Network Protocols & Devices - Advanced)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.