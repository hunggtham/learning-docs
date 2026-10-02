# 네트워크 구조 및 기술 (Network Structures & Technologies)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **네트워크 구조 및 기술 (Network Structures & Technologies)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối network structures với topology, protocol, routing và boundary, để hạ tầng giải thích luồng dữ liệu.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **네트워크 구조 및 기술 (Network Structures & Technologies)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **네트워크 구조 및 기술 (Network Structures & Technologies)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **네트워크 구조 및 기술 (Network Structures & Technologies)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

네트워크, 구조, 기술

> **Chuyển mạch:** Ở chặng này của **네트워크 구조 및 기술 (Network Structures & Technologies)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **네트워크 관련 장비 (Network Equipment)**에서 만든 기준을 이어받아 **네트워크 구조 및 기술 (Network Structures & Technologies)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **네트워크 구조 및 기술 (Network Structures & Technologies)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **네트워크 구조 및 기술 (Network Structures & Technologies)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **네트워크 구조 및 기술 (Network Structures & Technologies)**, **네트워크 구조 및 기술 (Network Structures & Technologies)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 네트워크 구조 및 기술 (Network Structures & Technologies)

Sau khi đã đặt nền bằng **네트워크 관련 장비 (Network Equipment)**, ta chuyển sang **네트워크 구조 및 기술 (Network Structures & Technologies)**. Đây là mắt xích 20/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **네트워크 구조 및 기술 (Network Structures & Technologies)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **성형 (Star, 중앙 집중형)**, **링형 (Ring, 루프형)**, **버스형 (Bus)**, **계층형 (Tree, 분산형)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 네트워크 설치 구조 (Network Topologies)**. Hãy xác định **1. 네트워크 설치 구조 (Network Topologies)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 네트워크 설치 구조 (Network Topologies)

Phần nguồn của **1. 네트워크 설치 구조 (Network Topologies)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. 네트워크 설치 구조 (Network Topologies)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **성형 (Star, 중앙 집중형)**: 중앙 컴퓨터를 중심으로 단말기가 연결 (Point-to-Point).
- **링형 (Ring, 루프형)**: 이웃하는 장치끼리 연결. 단방향 시 하나만 고장나도 전체 마비.
- **버스형 (Bus)**: 한 개의 통신 회선에 여러 장치 연결 (단말기 추가/제거 용이).
- **계층형 (Tree, 분산형)**: 중앙에서 중간 단말장치로 다시 분기되는 형태.
- **망형 (Mesh)**: 모든 지점을 연결. 통신량이 많을 때 유리하며 회선이 가장 많이 필요함 (`n(n-1)/2` 개).

Các bullet của **1. 네트워크 설치 구조 (Network Topologies)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 네트워크 설치 구조 (Network Topologies)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 근거리 통신망 (LAN) 표준 및 기술** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 근거리 통신망 (LAN) 표준 및 기술** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 근거리 통신망 (LAN) 표준 및 기술

Các ý ngay dưới **2. 근거리 통신망 (LAN) 표준 및 기술** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “2. 근거리 통신망 (LAN) 표준 및 기술” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **IEEE 802 규격**: 802.3(CSMA/CD), 802.4(토큰 버스), 802.5(토큰 링), 802.11(무선 LAN).
- **VLAN**: 물리적 배치와 상관없이 논리적으로 분리하는 기술.
- **CSMA/CA**: 무선 LAN(802.11)에서 매체가 비어있음을 확인 후 충돌 회피(Avoidance)를 위해 기다렸다가 전송하는 방식.

Các bullet của **2. 근거리 통신망 (LAN) 표준 및 기술** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. 근거리 통신망 (LAN) 표준 및 기술**, đừng bắt đầu lại từ số không. **3. 경로 제어 (Routing) 및 흐름 제어 (Flow Control)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **3. 경로 제어 (Routing) 및 흐름 제어 (Flow Control)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 3. 경로 제어 (Routing) 및 흐름 제어 (Flow Control)

Bây giờ ta đi vào nội dung của **3. 경로 제어 (Routing) 및 흐름 제어 (Flow Control)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “3. 경로 제어 (Routing) 및 흐름 제어 (Flow Control)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **IGP (내부 게이트웨이 프로토콜)**: AS 내에서 사용. **RIP**(거리 벡터, 최대 15홉 제한)와 **OSPF**(링크 상태, 대규모 망)가 있음.
- **EGP / BGP**: AS(자율 시스템) 간의 라우팅 프로토콜.
- **흐름 제어**: **정지-대기(Stop-and-Wait)** (수신 확인 후 다음 패킷 전송) / **슬라이딩 윈도우(Sliding Window)** (수신 확인 없이 윈도우 크기만큼 연속 전송).

💡 **Mẹo ghi nhớ (Mnemonics):**
- **RIP**: 15 Hops max (Dùng cho mạng nhỏ).
- **OSPF**: Link State (Dùng cho mạng lớn).
- **CSMA/CD**: Mạng LAN có dây (Collision Detection).
- **CSMA/CA**: Mạng không dây (Collision Avoidance).

Các bullet của **3. 경로 제어 (Routing) 및 흐름 제어 (Flow Control)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3. 경로 제어 (Routing) 및 흐름 제어 (Flow Control)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **네트워크 구조 및 기술 (Network Structures & Technologies)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **네트워크 구조 및 기술 (Network Structures & Technologies)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
