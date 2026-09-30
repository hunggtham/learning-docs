# 네트워크 및 정보 침해 공격 (Network & Info Security Attacks)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **네트워크 보안 기술 (Network Security Tech)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

네트워크, 정보, 침해, 공격

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **네트워크 구조 및 기술 (Network Structures & Technologies)**에서 만든 기준을 이어받아 **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)** và nối nó với **네트워크 보안 기술 (Network Security Tech)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 네트워크 및 정보 침해 공격 (Network & Info Security Attacks)

Từ **네트워크 구조 및 기술 (Network Structures & Technologies)**, ta đã có điểm tựa để bước vào **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 21/86 trước khi đi vào chi tiết.

Để đọc **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **DDoS (분산 서비스 거부 공격)**, **스머핑 (SMURFING)**, **세션 하이재킹 (Session Hijacking)**, **스위치 재밍 (Switch Jamming)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. 네트워크 공격** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. 네트워크 공격

Các ý ngay dưới **1. 네트워크 공격** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “1. 네트워크 공격” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **DDoS (분산 서비스 거부 공격)**: 여러 대의 PC(Agent/Zombie)를 이용해 특정 서버에 대량의 트래픽을 보내 마비시킴. (툴: Trin00, TFN, TFN2K, Stacheldraht).
- **스머핑 (SMURFING)**: IP/ICMP 특성을 악용해 한 사이트에 엄청난 데이터를 집중시키는 공격.
- **세션 하이재킹 (Session Hijacking)**: 클라이언트 세션을 가로채어 정상적인 사용자인 척하는 공격.
- **스위치 재밍 (Switch Jamming)**: 위조된 MAC 주소를 대량으로 보내 스위치를 더미 허브처럼 작동하게 만듦.

Các bullet của **1. 네트워크 공격** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 네트워크 공격** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 블루투스 공격** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **2. 블루투스 공격**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2. 블루투스 공격

Bây giờ ta đi vào nội dung của **2. 블루투스 공격**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “2. 블루투스 공격” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **블루버그 (BlueBug)**: 원격 조종 및 통화 감청.
- **블루스나프 (BlueSnarf)**: 장비 파일에 접근해 정보 탈취.
- **블루재킹 (BlueJacking)**: 스팸 메시지를 익명으로 퍼뜨림.

Các bullet của **2. 블루투스 공격** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. 블루투스 공격**, đừng bắt đầu lại từ số không. **3. 시스템 및 소프트웨어 공격** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **3. 시스템 및 소프트웨어 공격**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 3. 시스템 및 소프트웨어 공격

Phần nguồn của **3. 시스템 및 소프트웨어 공격** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “3. 시스템 및 소프트웨어 공격” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **제로 데이 공격 (Zero Day Attack)**: 보안 취약점이 공표되기 전, 혹은 패치가 나오기 전에 신속하게 이루어지는 공격.
- **랜섬웨어 (Ransomware)**: 파일을 암호화하고 돈(Ransom)을 요구하는 악성 프로그램.
- **백도어 (Back Door)**: 관리자 편의를 위해 만들어 놓은 비밀 통로를 악용.

💡 **Mẹo ghi nhớ (Mnemonics):**
- **BlueSnarf**: Sniff (Đánh hơi/Trộm thông tin).
- **BlueBug**: Bug (Cài bọ/Nghe lén).
- **BlueJacking**: Hijack (Chặn tin/Gửi tin nhắn rác).

Các bullet của **3. 시스템 및 소프트웨어 공격** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3. 시스템 및 소프트웨어 공격** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **네트워크 보안 기술 (Network Security Tech)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.