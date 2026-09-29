# 5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **네트워크 구조 및 기술 (Network Structures & Technologies)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

네트워크, 통신망, 주소, 체계

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)**에서 만든 기준을 이어받아 **5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)** và nối nó với **네트워크 구조 및 기술 (Network Structures & Technologies)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)

Ở bước 19/61, **5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)** xuất hiện như phần tiếp nối của **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **5.1 LAN 및 매체 접근 제어 (LAN & MAC)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **5.1 LAN 및 매체 접근 제어 (LAN & MAC)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 5.1 LAN 및 매체 접근 제어 (LAN & MAC)

Bây giờ ta đi vào nội dung của **5.1 LAN 및 매체 접근 제어 (LAN & MAC)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **LAN (Local Area Network):** 단일 기관 소유, 고속 전송, 오류율 낮음.
- **IEEE 802 주요 규격:**
  - `802.1` (전체 구성), `802.2` (LLC), `802.3` (CSMA/CD), `802.4` (토큰 버스), `802.5` (토큰 링), `802.11` (무선 LAN).
- **CSMA/CD (Carrier Sense Multiple Access/Collision Detection):** 채널 사용권 경쟁. 충돌 감지.
  - 규격 명칭 (예: `10 BASE T` - 10Mbps, 베이스밴드, 꼬임선).
  - **이더넷 (Ethernet):** CSMA/CD 방식을 사용하는 LAN.
- **Tiếng Việt:** Mạng LAN cục bộ. IEEE 802.3 là tiêu chuẩn CSMA/CD (Ethernet - phát hiện xung đột).

Các bullet của **5.1 LAN 및 매체 접근 제어 (LAN & MAC)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **5.1 LAN 및 매체 접근 제어 (LAN & MAC)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **5.2 기타 통신망 (VAN, ISDN)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **5.2 기타 통신망 (VAN, ISDN)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 5.2 기타 통신망 (VAN, ISDN)

Phần nguồn của **5.2 기타 통신망 (VAN, ISDN)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **VAN (부가 가치 통신망):** 공중 통신망을 임대해 정보 가공/변환 등 부가 가치를 첨가해 서비스 제공.
- **ISDN (종합 정보 통신망):** 음성/문자/영상을 디지털 방식으로 종합 제공.
- **Tiếng Việt:**
  - VAN: Mạng giá trị gia tăng (thuê đường truyền, thêm dịch vụ).
  - ISDN: Mạng số đa dịch vụ tích hợp.

Các bullet của **5.2 기타 통신망 (VAN, ISDN)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **5.2 기타 통신망 (VAN, ISDN)**, đừng bắt đầu lại từ số không. **5.3 인터넷 주소 체계 (IP Addresses)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **5.3 인터넷 주소 체계 (IP Addresses)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 5.3 인터넷 주소 체계 (IP Addresses)

Các ý ngay dưới **5.3 인터넷 주소 체계 (IP Addresses)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **IPv4:** 32비트 (8비트 × 4부분). 클래스 A~E (A: 대형 ~ C: 소규모망, D: 멀티캐스트).
- **IPv6:** 128비트 (16비트 × 8부분, 16진수, 콜론 `:` 구분)로 주소 공간을 확장한다. 기본 헤더는 단순화되고 브로드캐스트 대신 멀티캐스트·애니캐스트를 사용한다.
- **IPv4 → IPv6 전환 전략:** 듀얼 스택(Dual Stack), 터널링(Tunneling), 헤더/전송/응용 게이트웨이 변환(Translation).
- **DNS (Domain Name System):** 문자 도메인 네임을 IP 주소로 변환.
- **Tiếng Việt:** IPv4 (32 bit, Class A-E). IPv6 (128 bit, giải quyết cạn kiệt IP). DNS dịch tên miền sang IP.
- 💡 **Mẹo ghi nhớ:** Chuyển đổi IPv4/IPv6: "Dual - Tunnel - Translate".

Các bullet của **5.3 인터넷 주소 체계 (IP Addresses)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**5.3 인터넷 주소 체계 (IP Addresses)** vừa cho ta cách đặt câu hỏi. Bây giờ **5.4 네트워크 관련 장비 (Network Devices)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **5.4 네트워크 관련 장비 (Network Devices)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 5.4 네트워크 관련 장비 (Network Devices)

Bây giờ ta đi vào nội dung của **5.4 네트워크 관련 장비 (Network Devices)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **허브 (Hub):** 물리 계층, 포트 통합 관리 및 리피터 역할.
- **리피터 (Repeater):** 물리 계층, 신호 재생 및 증폭.
- **브리지 (Bridge):** 데이터 링크 계층, LAN-LAN 연결.
- **라우터 (Router):** 네트워크 계층, 경로 선택(Routing) 및 서로 다른 망 연결.
- **게이트웨이 (Gateway):** 전 계층(주로 상위), 프로토콜이 전혀 다른 네트워크 연결.
- **Tiếng Việt:**
  - L1: Hub, Repeater (Khuếch đại tín hiệu).
  - L2: Bridge (Nối LAN).
  - L3: Router (Định tuyến).
  - L4-L7: Gateway (Nối mạng khác giao thức).

Các bullet của **5.4 네트워크 관련 장비 (Network Devices)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **5.4 네트워크 관련 장비 (Network Devices)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **네트워크 구조 및 기술 (Network Structures & Technologies)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.