# 4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

오류, 제어, 교환, 방식

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)**에서 만든 기준을 이어받아 **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)

Ở bước 7/18, **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)** xuất hiện như phần tiếp nối của **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **4.1 오류 발생 원인 및 제어 (Error Causes & Control)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **4.1 오류 발생 원인 및 제어 (Error Causes & Control)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 4.1 오류 발생 원인 및 제어 (Error Causes & Control)

Bây giờ ta đi vào nội dung của **4.1 오류 발생 원인 및 제어 (Error Causes & Control)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **원인:** 감쇠, 지연 왜곡, 상호 변조, 누화 잡음, 충격성 잡음(디지털 통신 주요인).
- **FEC (순방향 오류 수정):** 수신 측에서 스스로 수정 (해밍 코드 등). 오버헤드 큼, 역채널 불필요.
- **BEC (역방향 오류 수정):** 오류 시 재전송(ARQ) 요구 (패리티, CRC 등).
- **Tiếng Việt:** 
  - FEC: Tự sửa lỗi (vd: Hamming Code). 
  - BEC: Yêu cầu gửi lại (vd: CRC, Parity).

Các bullet của **4.1 오류 발생 원인 및 제어 (Error Causes & Control)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **4.1 오류 발생 원인 및 제어 (Error Causes & Control)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **4.2 ARQ (자동 반복 요청) 및 오류 검출 방식** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **4.2 ARQ (자동 반복 요청) 및 오류 검출 방식**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 4.2 ARQ (자동 반복 요청) 및 오류 검출 방식

Phần nguồn của **4.2 ARQ (자동 반복 요청) 및 오류 검출 방식** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **ARQ 종류:**
  - **Stop-and-Wait:** 한 블록 보내고 기다림.
  - **Go-Back-N:** 오류 발생 지점부터 *모두* 재전송.
  - **Selective Repeat:** 오류 발생 블록*만* 재전송 (버퍼 필요, 복잡).
  - **Adaptive:** 채널 상태에 따라 동적 변경.
- **오류 검출 및 수정:**
  - **패리티 (Parity):** 1비트 검출, 짝수오류 검출 불가.
  - **CRC:** 다항식 기반, 집단 오류 검출 특화 (HDLC 사용).
  - **해밍 코드 (Hamming Code):** 1비트 *수정* 가능. `2^n` 번째 자리에 비트 삽입.
- **Tiếng Việt:** 
  - Go-Back-N: Gửi lại từ lỗi. Selective Repeat: Chỉ gửi lại gói lỗi. 
  - CRC: Kiểm tra đa thức (phổ biến nhất). Hamming Code: Sửa được lỗi 1 bit.

Các bullet của **4.2 ARQ (자동 반복 요청) 및 오류 검출 방식** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **4.2 ARQ (자동 반복 요청) 및 오류 검출 방식**, đừng bắt đầu lại từ số không. **4.3 교환 방식 (Switching Methods)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **4.3 교환 방식 (Switching Methods)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 4.3 교환 방식 (Switching Methods)

Các ý ngay dưới **4.3 교환 방식 (Switching Methods)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **회선 교환 (Circuit Switching):** 물리적 전용선 할당. 고정 대역, 연속적 데이터 전송. (접속 지연 O, 전송 지연 X). 전화망.
- **축적 교환 (Store-and-Forward):** 데이터를 저장했다가 경로를 찾아 전송.
  - **메시지 교환 (Message Switching):** 전체 메시지 전송. 지연 매우 긺.
  - **패킷 교환 (Packet Switching):** 패킷 단위로 잘라서 전송 (다음 파트에서 상세 서술).
- **Tiếng Việt:** 
  - Circuit Switching (Chuyển mạch kênh): Tạo đường truyền vật lý (Điện thoại).
  - Message Switching (Chuyển mạch thông điệp): Lưu rồi chuyển toàn bộ.

EOF

Các bullet của **4.3 교환 방식 (Switching Methods)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**4.3 교환 방식 (Switching Methods)** vừa cho ta cách đặt câu hỏi. Bây giờ **4.4 패킷 교환 방식 및 네트워크 기능 (Packet Switching & Network Functions)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **4.4 패킷 교환 방식 및 네트워크 기능 (Packet Switching & Network Functions)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 4.4 패킷 교환 방식 및 네트워크 기능 (Packet Switching & Network Functions)

Bây giờ ta đi vào nội dung của **4.4 패킷 교환 방식 및 네트워크 기능 (Packet Switching & Network Functions)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **가상 회선 (Virtual Circuit):** 패킷 교환 전에 논리적인 가상 회선을 설정. 전송 순서가 보장되며 신뢰성이 높음. (호 설정 → 데이터 전송 → 호 해제).
- **데이터그램 (Datagram):** 연결 경로 설정 없이 각 패킷이 독립적으로 운반됨. 패킷마다 경로가 다르고 순서가 다를 수 있음. 짧은 데이터 전송에 적합.
- **패킷 교환망의 기능:** 패킷 다중화, 논리 채널 설정, 경로 제어, 순서 제어, 트래픽 제어, 오류 제어.
- **Tiếng Việt:** 
  - Virtual Circuit: Tạo đường dẫn ảo trước khi truyền (thứ tự được đảm bảo). 
  - Datagram: Truyền độc lập không cần tạo đường dẫn (thứ tự có thể thay đổi).

Các bullet của **4.4 패킷 교환 방식 및 네트워크 기능 (Packet Switching & Network Functions)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **4.4 패킷 교환 방식 및 네트워크 기능 (Packet Switching & Network Functions)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **4.5 트래픽 제어 및 라우팅 심화 (Traffic Control & Routing)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **4.5 트래픽 제어 및 라우팅 심화 (Traffic Control & Routing)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 4.5 트래픽 제어 및 라우팅 심화 (Traffic Control & Routing)

Phần nguồn của **4.5 트래픽 제어 및 라우팅 심화 (Traffic Control & Routing)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **경로 설정 방식 (Routing Strategies):**
  - **고정 경로 (Static):** 미리 정해진 경로 사용.
  - **적응 경로 (Adaptive):** 트래픽 상황에 따라 동적 변경.
  - **범람 (Flooding):** 모든 경로로 패킷 복사 전송 (네트워크 정보 불필요).
  - **임의 경로 (Random):** 인접 교환기 중 임의 선택.
- **폭주(혼잡) 제어 (Congestion Control):** 오버플로를 방지하기 위해 네트워크 내 패킷 수 조절.
- **Tiếng Việt:** Routing có Static (Tĩnh), Adaptive (Động), Flooding (Tràn ngập). Congestion Control giúp chống quá tải mạng.

Các bullet của **4.5 트래픽 제어 및 라우팅 심화 (Traffic Control & Routing)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **4.5 트래픽 제어 및 라우팅 심화 (Traffic Control & Routing)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.