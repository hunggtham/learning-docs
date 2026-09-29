# 6. 통신 프로토콜 (Giao thức Truyền thông)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **6. 통신 프로토콜 (Giao thức Truyền thông)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **6. 통신 프로토콜 (Giao thức Truyền thông)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **기본 프로토콜 (Basic Protocols)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

통신, 프로토콜

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)**에서 만든 기준을 이어받아 **6. 통신 프로토콜 (Giao thức Truyền thông)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 6. 통신 프로토콜 (Giao thức Truyền thông)

Ở bước 10/18, **6. 통신 프로토콜 (Giao thức Truyền thông)** xuất hiện như phần tiếp nối của **5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **6. 통신 프로토콜 (Giao thức Truyền thông)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **6.1 통신 프로토콜 3요소 (Protocol 3 Elements)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **6.1 통신 프로토콜 3요소 (Protocol 3 Elements)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 6.1 통신 프로토콜 3요소 (Protocol 3 Elements)

Bây giờ ta đi vào nội dung của **6.1 통신 프로토콜 3요소 (Protocol 3 Elements)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **구문 (Syntax):** 데이터 형식, 코딩.
- **의미 (Semantics):** 제어 정보 및 오류 관리.
- **시간 (Timing):** 속도 조절, 동기화.
- **Tiếng Việt:** 3 yếu tố của giao thức: Cú pháp (Syntax), Ngữ nghĩa (Semantics), Thời gian (Timing).

Các bullet của **6.1 통신 프로토콜 3요소 (Protocol 3 Elements)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **6.1 통신 프로토콜 3요소 (Protocol 3 Elements)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **6.2 OSI 7계층 (OSI 7 Layers)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **6.2 OSI 7계층 (OSI 7 Layers)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 6.2 OSI 7계층 (OSI 7 Layers)

Phần nguồn của **6.2 OSI 7계층 (OSI 7 Layers)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

1. **물리 계층 (Physical):** 기계/전기적 특성 (RS-232C, 리피터).
2. **데이터 링크 계층 (Data Link):** 인접 시스템 간 신뢰성 보장, 오류/흐름 제어 (HDLC, LLC).
3. **네트워크 계층 (Network):** 경로 설정(Routing), 데이터 교환 (IP, X.25, 라우터).
4. **전송 계층 (Transport):** 종단 간(End-to-End) 투명한 데이터 전송 (TCP, UDP).
5. **세션 계층 (Session):** 대화 제어 및 동기점(체크점) 관리.
6. **표현 계층 (Presentation):** 데이터 포맷 변환, 암호화, 압축.
7. **응용 계층 (Application):** 사용자에게 네트워크 서비스 제공.
- **Tiếng Việt:** Mô hình OSI 7 lớp: Vật lý -> Liên kết dữ liệu -> Mạng -> Giao vận -> Phiên -> Trình diễn -> Ứng dụng.
- 💡 **Mẹo ghi nhớ:** Vật Liên Mạng Giao Phiên Trình Ứng (Vật lý -> Liên kết dữ liệu -> Mạng -> Giao vận -> Phiên -> Trình diễn -> Ứng dụng).

Các bullet của **6.2 OSI 7계층 (OSI 7 Layers)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **6.2 OSI 7계층 (OSI 7 Layers)**, đừng bắt đầu lại từ số không. **6.3 주요 네트워크 프로토콜** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **6.3 주요 네트워크 프로토콜** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 6.3 주요 네트워크 프로토콜

Các ý ngay dưới **6.3 주요 네트워크 프로토콜** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **X.25:** 패킷 교환망 프로토콜 (물리 - 프레임 - 패킷 계층). LAPB 사용.
- **TCP/IP:**
  - **응용 계층:** FTP, SMTP, HTTP, DNS 등.
  - **전송 계층:** 
    - **TCP:** 연결형, 신뢰성 보장, 순서/흐름 제어, 스트림 전송.
    - **UDP:** 비연결형, 빠른 전송.
  - **인터넷 계층:** 
    - **IP:** 비연결형(데이터그램), 경로 선택(Routing).
    - **ICMP:** IP 오류 처리 및 제어 메시지.
    - **ARP:** IP → MAC / **RARP:** MAC → IP.
  - **네트워크 액세스 계층:** 이더넷, X.25, RS-232C.
- **Tiếng Việt:** 
  - TCP: Tin cậy, hướng kết nối. UDP: Nhanh, không kết nối.
  - IP: Định tuyến. ICMP: Báo lỗi mạng. ARP: Đổi IP sang MAC.

# 정보처리기사 (Information Processing Engineer) - Part 2

Các bullet của **6.3 주요 네트워크 프로토콜** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **6.3 주요 네트워크 프로토콜** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **6. 통신 프로토콜 (Giao thức Truyền thông)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **기본 프로토콜 (Basic Protocols)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.