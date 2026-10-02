# 계층별 주요 프로토콜 (Major Protocols by Layer)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **계층별 주요 프로토콜 (Major Protocols by Layer)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối protocols theo layer với encapsulation, service và failure boundary, để mỗi giao thức có vai trò rõ.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **계층별 주요 프로토콜 (Major Protocols by Layer)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **계층별 주요 프로토콜 (Major Protocols by Layer)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **계층별 주요 프로토콜 (Major Protocols by Layer)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

계층별, 주요, 프로토콜

> **Chuyển mạch:** Ở chặng này của **계층별 주요 프로토콜 (Major Protocols by Layer)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **네트워크 보안 기술 (Network Security Tech)**에서 만든 기준을 이어받아 **계층별 주요 프로토콜 (Major Protocols by Layer)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **계층별 주요 프로토콜 (Major Protocols by Layer)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **계층별 주요 프로토콜 (Major Protocols by Layer)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **계층별 주요 프로토콜 (Major Protocols by Layer)**, **계층별 주요 프로토콜 (Major Protocols by Layer)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 계층별 주요 프로토콜 (Major Protocols by Layer)

Sau khi đã đặt nền bằng **네트워크 보안 기술 (Network Security Tech)**, ta chuyển sang **계층별 주요 프로토콜 (Major Protocols by Layer)**. Đây là mắt xích 23/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **계층별 주요 프로토콜 (Major Protocols by Layer)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **FTP**, **TELNET**, **TCP**, **UDP** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 응용 계층 (Application)**. Hãy xác định **1. 응용 계층 (Application)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 응용 계층 (Application)

Phần nguồn của **1. 응용 계층 (Application)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. 응용 계층 (Application)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **FTP**: 파일 전송 / **SMTP**: 이메일 송신 / **HTTP**: 웹 문서 송수신
- **TELNET**: 원격 접속 가상 터미널 / **DNS**: 도메인 네임을 IP 주소로 변환

Các bullet của **1. 응용 계층 (Application)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 응용 계층 (Application)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 전송 계층 (Transport)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 전송 계층 (Transport)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 전송 계층 (Transport)

Các ý ngay dưới **2. 전송 계층 (Transport)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “2. 전송 계층 (Transport)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **TCP**: 연결 지향, 양방향, 신뢰성 보장, 스트림 위주 전달, 흐름 및 순서 제어 기능 제공.
- **UDP**: 비연결형, 빠른 전송 속도 (실시간 전송 유리, 오버헤드 적음).

Các bullet của **2. 전송 계층 (Transport)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. 전송 계층 (Transport)**, đừng bắt đầu lại từ số không. **3. 인터넷 계층 (Internet / Network)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **3. 인터넷 계층 (Internet / Network)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 3. 인터넷 계층 (Internet / Network)

Bây giờ ta đi vào nội dung của **3. 인터넷 계층 (Internet / Network)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “3. 인터넷 계층 (Internet / Network)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **IP**: 데이터 주소 지정 및 경로 설정.
- **ICMP**: 제어 메시지 및 오류 처리 관리.
- **ARP**: IP 주소 -> MAC 주소 (물리적 주소)로 변환.
- **RARP**: MAC 주소 -> IP 주소로 변환.

Các bullet của **3. 인터넷 계층 (Internet / Network)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**3. 인터넷 계층 (Internet / Network)** vừa cho ta cách đặt câu hỏi. Bây giờ **4. 네트워크 액세스 계층 (Data Link & Physical)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **4. 네트워크 액세스 계층 (Data Link & Physical)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 4. 네트워크 액세스 계층 (Data Link & Physical)

Phần nguồn của **4. 네트워크 액세스 계층 (Data Link & Physical)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “4. 네트워크 액세스 계층 (Data Link & Physical)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **Ethernet (IEEE 802.3)**, **HDLC**, **X.25**, **RS-232C** 등.

Các bullet của **4. 네트워크 액세스 계층 (Data Link & Physical)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **4. 네트워크 액세스 계층 (Data Link & Physical)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **계층별 주요 프로토콜 (Major Protocols by Layer)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **계층별 주요 프로토콜 (Major Protocols by Layer)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
