# 2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

대칭, 비대칭

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)**에서 만든 기준을 이어받아 **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)** và nối nó với **108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)

Ở bước 82/86, **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)** xuất hiện như phần tiếp nối của **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **대칭 키 (Symmetric Key)**, **비대칭 키 (Asymmetric Key)**, **Backdoor (백도어)**, **Key Logger (키로거)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **대칭 키 (Symmetric Key)**: 암호화 키 = 복호화 키 (비밀 키).
  - 속도가 빠름, 키 관리가 어려움 (Nhanh nhưng khó quản lý phân phối key).
  - 종류 (Các loại): DES, AES, SEED, ARIA, IDEA (Block); RC4, LFSR (Stream).
- **비대칭 키 (Asymmetric Key)**: 암호화 키(공개 키) ≠ 복호화 키(개인 키).
  - 속도가 느림, 키 분배 및 관리가 쉬움 (Chậm nhưng dễ phân phối key, an toàn).
  - 종류 (Các loại): RSA, ECC, Diffie-Hellman.
- 💡 **Mẹo ghi nhớ**:
  - 대칭 (Đại xưng) = 비밀 (Bí mật chung) -> AES, DES.
  - 비대칭 (Bất đại xưng) = 공개 (Công khai 1 nửa) -> RSA.

---

# 107 서비스 공격 기법 (Service Attack Techniques / Kỹ thuật tấn công dịch vụ)
Phần “107 서비스 공격 기법 (Service Attack Techniques / Kỹ thuật tấn công dịch vụ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **Backdoor (백도어)**: 시스템 인증 절차를 우회하여 몰래 접속하는 경로 (Cửa sau, lách xác thực).
- **Key Logger (키로거)**: 키보드 입력 움직임을 탐지하여 비밀번호 등을 탈취 (Ghi lại thao tác bàn phím).
- **Rootkit (루트킷)**: 시스템 침입 사실을 숨기고 관리자 권한을 유지하는 도구 모음 (Bộ công cụ che giấu xâm nhập và giữ quyền admin).
- **Phishing, Smishing, Qshing (피싱, 스미싱, 큐싱)**: 이메일(Phishing), 문자(Smishing), QR코드(Qshing)로 개인정보 탈취 (Lừa đảo lấy thông tin qua mail, SMS, mã QR).
- **Zombie PC & Botnet (좀비 PC & 봇넷)**: 악성 봇에 감염되어 해커(C&C서버)의 명령에 따라 DDoS 공격 등을 수행하는 PC 무리 (Máy tính bị nhiễm bot, bị điều khiển hàng loạt).
- **Ransomware (랜섬웨어)**: 파일을 암호화하고 돈을 요구하는 악성 프로그램 (Mã độc tống tiền).
- **Zero Day Attack (제로데이 공격)**: 취약점이 공표되기도 전에 이루어지는 공격 (Tấn công ngay khi lỗ hổng vừa được phát hiện, chưa có bản vá).
- **Sniffing (스니핑)**: 네트워크 패킷을 몰래 엿보며 정보 수집 (Nghe lén gói tin trên mạng).
- **Spoofing (스푸핑 - IP, ARP)**: 위조된 IP나 MAC 주소로 속여 인증을 통과하거나 패킷을 가로챔 (Giả mạo địa chỉ IP hoặc MAC).
- **Session Hijacking (세션 하이재킹)**: 이미 로그인된 세션 정보를 가로채어 권한 획득 (Cướp phiên đăng nhập).
- 💡 **Mẹo ghi nhớ**: Spoof = 속이다 (Fake/Giả mạo), Sniff = 킁킁거리다 (Nghe lén/Trộm xem).

---

Như vậy, **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.