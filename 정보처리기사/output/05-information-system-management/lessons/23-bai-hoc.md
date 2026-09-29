# 6. 통신 프로토콜 (Giao thức Truyền thông)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **6. 통신 프로토콜 (Giao thức Truyền thông)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **6. 통신 프로토콜 (Giao thức Truyền thông)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **기본 프로토콜 (Basic Protocols)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

통신, 프로토콜

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **네트워크 보안 기술 (Network Security Tech)**에서 만든 기준을 이어받아 **6. 통신 프로토콜 (Giao thức Truyền thông)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **6. 통신 프로토콜 (Giao thức Truyền thông)** và nối nó với **기본 프로토콜 (Basic Protocols)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 6. 통신 프로토콜 (Giao thức Truyền thông)

Sau khi đã đặt nền bằng **네트워크 보안 기술 (Network Security Tech)**, ta chuyển sang **6. 통신 프로토콜 (Giao thức Truyền thông)**. Đây là mắt xích 23/61 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **6. 통신 프로토콜 (Giao thức Truyền thông)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **6.1 통신 프로토콜 3요소 (Protocol 3 Elements)**. Hãy xác định **6.1 통신 프로토콜 3요소 (Protocol 3 Elements)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 6.1 통신 프로토콜 3요소 (Protocol 3 Elements)

Phần nguồn của **6.1 통신 프로토콜 3요소 (Protocol 3 Elements)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **구문 (Syntax):** 데이터 형식, 코딩.
- **의미 (Semantics):** 제어 정보 및 오류 관리.
- **시간 (Timing):** 속도 조절, 동기화.
- **Tiếng Việt:** 3 yếu tố của giao thức: Cú pháp (Syntax), Ngữ nghĩa (Semantics), Thời gian (Timing).

Các bullet của **6.1 통신 프로토콜 3요소 (Protocol 3 Elements)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **6.1 통신 프로토콜 3요소 (Protocol 3 Elements)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **6.2 OSI 7계층 (OSI 7 Layers)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **6.2 OSI 7계층 (OSI 7 Layers)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 6.2 OSI 7계층 (OSI 7 Layers)

Các ý ngay dưới **6.2 OSI 7계층 (OSI 7 Layers)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

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
Ở đoạn **6.3 주요 네트워크 프로토콜**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 6.3 주요 네트워크 프로토콜

Bây giờ ta đi vào nội dung của **6.3 주요 네트워크 프로토콜**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

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

Các bullet của **6.3 주요 네트워크 프로토콜** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **6.3 주요 네트워크 프로토콜** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **6. 통신 프로토콜 (Giao thức Truyền thông)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **기본 프로토콜 (Basic Protocols)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.