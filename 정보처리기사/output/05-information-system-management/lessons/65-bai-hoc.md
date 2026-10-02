# IP 주소 및 서브네팅 (IP Address & Subnetting)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **IP 주소 및 서브네팅 (IP Address & Subnetting)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối IP address với subnetting, prefix, routing và host range, để địa chỉ đi cùng topology.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **IP 주소 및 서브네팅 (IP Address & Subnetting)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **IP 주소 및 서브네팅 (IP Address & Subnetting)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **IP 주소 및 서브네팅 (IP Address & Subnetting)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

주소, 서브네팅

> **Chuyển mạch:** Ở chặng này của **IP 주소 및 서브네팅 (IP Address & Subnetting)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)**에서 만든 기준을 이어받아 **IP 주소 및 서브네팅 (IP Address & Subnetting)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **IP 주소 및 서브네팅 (IP Address & Subnetting)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **IP 주소 및 서브네팅 (IP Address & Subnetting)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **IP 주소 및 서브네팅 (IP Address & Subnetting)**, **IP 주소 및 서브네팅 (IP Address & Subnetting)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## IP 주소 및 서브네팅 (IP Address & Subnetting)

Sau khi đã đặt nền bằng **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)**, ta chuyển sang **IP 주소 및 서브네팅 (IP Address & Subnetting)**. Đây là mắt xích 65/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **IP 주소 및 서브네팅 (IP Address & Subnetting)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **A Class**, **B Class**, **C Class**, **D Class** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. IPv4 주소 (Internet Protocol version 4)**. Hãy xác định **1. IPv4 주소 (Internet Protocol version 4)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. IPv4 주소 (Internet Protocol version 4)

Phần nguồn của **1. IPv4 주소 (Internet Protocol version 4)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. IPv4 주소 (Internet Protocol version 4)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 8비트씩 4부분, 총 **32비트**로 구성됩니다.
- 네트워크 크기에 따라 A~E 클래스로 나뉩니다.
  - **A Class**: 국가/대형 망 (0~127)
  - **B Class**: 중대형 망 (128~191)
  - **C Class**: 소규모 망 (192~223)
  - **D Class**: 멀티캐스트용 (224~239)
  - **E Class**: 실험적 주소

Các bullet của **1. IPv4 주소 (Internet Protocol version 4)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. IPv4 주소 (Internet Protocol version 4)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 서브네팅 (Subnetting)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 서브네팅 (Subnetting)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 서브네팅 (Subnetting)

Các ý ngay dưới **2. 서브네팅 (Subnetting)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

할당된 네트워크 주소를 다시 여러 개의 작은 네트워크로 나누어 사용하는 기법입니다. (서브넷 마스크 활용).

Phần **2. 서브네팅 (Subnetting)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Sau khi đọc **2. 서브네팅 (Subnetting)**, đừng bắt đầu lại từ số không. **3. IPv6 주소 (Internet Protocol version 6)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **3. IPv6 주소 (Internet Protocol version 6)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 3. IPv6 주소 (Internet Protocol version 6)

Bây giờ ta đi vào nội dung của **3. IPv6 주소 (Internet Protocol version 6)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “3. IPv6 주소 (Internet Protocol version 6)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- IPv4의 주소 부족 문제를 해결하기 위해 개발되었습니다.
- 16비트씩 8부분, 총 **128비트**로 구성되며 콜론(`:`)으로 구분합니다.
- 인증성, 기밀성, 무결성을 지원하여 보안이 뛰어나고, 주소 확장성과 호환성이 좋습니다.
- **주소 체계**:
  - **유니캐스트 (Unicast)**: 1 대 1 통신
  - **멀티캐스트 (Multicast)**: 1 대 다 통신
  - **애니캐스트 (Anycast)**: 1 대 1 통신 (가장 가까운 수신자에게 전송)

💡 **Mẹo ghi nhớ (Mnemonics):**
- **IPv4**: 32-bit (4 x 8).
- **IPv6**: 128-bit (8 x 16), **U.M.A** (Unicast, Multicast, Anycast).

Các bullet của **3. IPv6 주소 (Internet Protocol version 6)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3. IPv6 주소 (Internet Protocol version 6)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **IP 주소 및 서브네팅 (IP Address & Subnetting)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **IP 주소 및 서브네팅 (IP Address & Subnetting)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
