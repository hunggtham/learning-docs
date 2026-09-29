# 10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **정보 보안 및 하드웨어 신기술 (Security & HW Tech)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

해킹, 보안, 위협

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)**에서 만든 기준을 이어받아 **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)** và nối nó với **정보 보안 및 하드웨어 신기술 (Security & HW Tech)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)

Ở bước 28/61, **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)** xuất hiện như phần tiếp nối của **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **10.1 웹 및 애플리케이션 취약점** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **10.1 웹 및 애플리케이션 취약점** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 10.1 웹 및 애플리케이션 취약점

Bây giờ ta đi vào nội dung của **10.1 웹 및 애플리케이션 취약점**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **SQL 삽입 (SQL Injection):** SQL을 삽입하여 DB 유출/변조 및 인증 우회.
- **크로스사이트 스크립팅 (XSS):** 악의적인 스크립트를 삽입하여 방문자 정보 탈취.
- **경로 조작 및 자원 삽입:** 데이터 입출력 경로 조작으로 자원 삭제/수정.
- **메모리 버퍼 오버플로:** 메모리 범위를 넘어선 위치에서 쓰기 시도. 방어 기술로 **스택 가드(Stack Guard)** 사용.
- **하드코드된 비밀번호:** 소스코드 내부에 비밀번호를 직접 입력하는 취약점.
- **Tiếng Việt:** Các lỗ hổng web: SQL Injection (chèn lệnh SQL), XSS (chèn script độc hại), Buffer Overflow (tràn bộ đệm - phòng bằng Stack Guard).

Các bullet của **10.1 웹 및 애플리케이션 취약점** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **10.1 웹 및 애플리케이션 취약점** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **10.2 네트워크 및 분산 서비스 거부 공격 (DoS/DDoS)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **10.2 네트워크 및 분산 서비스 거부 공격 (DoS/DDoS)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 10.2 네트워크 및 분산 서비스 거부 공격 (DoS/DDoS)

Phần nguồn của **10.2 네트워크 및 분산 서비스 거부 공격 (DoS/DDoS)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **세션 하이재킹 (Session Hijacking):** 클라이언트의 세션 정보를 가로채는 공격.
- **DDoS 공격:** 여러 분산된 지점에서 한 곳을 공격. (툴: Trin00, TFN, TFN2K, Stacheldraht).
- **Ping of Death:** 허용 범위 이상의 큰 ICMP 패킷을 전송해 마비시킴.
- **Ping Flood:** 많은 ICMP 메시지를 보내 응답으로 자원 고갈시킴.
- **스머핑 (SMURFING):** IP/ICMP 특성을 악용해 한 사이트에 집중적으로 데이터 보냄.
- **DPI (Deep Packet Inspection):** 전 계층의 프로토콜과 패킷 내부를 파악해 침입 탐지.
- **Tiếng Việt:**
  - DDoS: Tấn công từ chối dịch vụ phân tán.
  - Ping of Death: Gửi gói ICMP quá lớn.
  - SMURFING: Gửi lượng lớn dữ liệu tập trung.

Các bullet của **10.2 네트워크 및 분산 서비스 거부 공격 (DoS/DDoS)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **10.2 네트워크 및 분산 서비스 거부 공격 (DoS/DDoS)**, đừng bắt đầu lại từ số không. **10.3 시스템 해킹 및 악성코드** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **10.3 시스템 해킹 및 악성코드** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 10.3 시스템 해킹 및 악성코드

Các ý ngay dưới **10.3 시스템 해킹 및 악성코드** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **백도어 (Back Door):** 보안을 제거하고 만들어 놓은 비밀 통로 (탐지: 무결성 검사, 열린 포트 등).
- **키로거 공격 (Key Logger):** 키보드 움직임을 탐지해 개인정보 탈취.
- **랜섬웨어 (Ransomware):** 문서 암호화 후 돈(Ransom)을 요구.
- **웜 (Worm):** 네트워크를 통해 스스로 전파·복제되는 악성 코드로, 숙주 파일에 기생해야 하는 바이러스와 구분한다.
- **허니팟 (Honeypot):** 비정상 접근 탐지를 위해 의도적으로 설치한 시스템 (미끼).
- **피싱 (Phishing):** 공공/금융 기관을 사칭해 개인정보 탈취.
- **Tiếng Việt:** Backdoor (Cửa hậu), Key Logger (Ghi thao tác bàn phím), Ransomware (Mã độc tống tiền), Worm (Giun máy tính - tự nhân bản), Honeypot (Hệ thống mồi nhử).

Các bullet của **10.3 시스템 해킹 및 악성코드** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**10.3 시스템 해킹 및 악성코드** vừa cho ta cách đặt câu hỏi. Bây giờ **10.4 기타 네트워크 공격** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **10.4 기타 네트워크 공격**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 10.4 기타 네트워크 공격

Bây giờ ta đi vào nội dung của **10.4 기타 네트워크 공격**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **스위치 재밍 (Switch Jamming):** 위조된 MAC 주소를 흘려보내 스위치를 더미 허브로 작동하게 만듦.
- **블루투스 관련 공격:**
  - **블루버그 (BlueBug):** 취약한 연결 관리 악용.
  - **블루스나프 (BlueSnarf):** 취약점 활용해 파일 접근.
  - **블루프린팅 (BluePrinting):** 공격 대상 장비 검색.
  - **블루재킹 (BlueJacking):** 익명으로 스팸 메시지 퍼뜨림.
- **Tiếng Việt:** Tấn công Switch Jamming (biến Switch thành Hub) và các tấn công Bluetooth (BlueBug, BlueSnarf, BlueJacking).
- 💡 **Mẹo ghi nhớ:** Blue**Jacking** = **Spam message**. Blue**Snarf** = **Snatch files** (cướp file).

Với **10.4 기타 네트워크 공격**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **10.4 기타 네트워크 공격**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **정보 보안 및 하드웨어 신기술 (Security & HW Tech)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.