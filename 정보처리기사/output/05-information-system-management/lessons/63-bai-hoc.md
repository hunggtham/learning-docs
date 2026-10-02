# 주요 스케줄링 알고리즘 (Major Scheduling Algorithms)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối scheduling algorithms với queue, fairness, priority và latency, để CPU allocation được đọc qua workload.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

주요, 스케줄링, 알고리즘

> **Chuyển mạch:** Ở chặng này của **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **프로세스와 스레드 (Process and Thread)**에서 만든 기준을 이어받아 **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**, **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 주요 스케줄링 알고리즘 (Major Scheduling Algorithms)

Từ **프로세스와 스레드 (Process and Thread)**, ta đã có điểm tựa để bước vào **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 63/86 trước khi đi vào chi tiết.

Để đọc **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. FCFS (First Come First Service) / FIFO** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. FCFS (First Come First Service) / FIFO

Các ý ngay dưới **1. FCFS (First Come First Service) / FIFO** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

준비 큐에 도착한 순서대로 CPU를 할당하는 기법 (선입선출). 구현은 가장 간단하나, 긴 작업이 먼저 오면 뒤의 짧은 작업이 오래 기다리게 됨.

Phần **1. FCFS (First Come First Service) / FIFO** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Ta vừa chốt **1. FCFS (First Come First Service) / FIFO** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. SJF (Shortest Job First)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **2. SJF (Shortest Job First)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2. SJF (Shortest Job First)

Bây giờ ta đi vào nội dung của **2. SJF (Shortest Job First)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

실행 시간이 가장 짧은 프로세스에게 먼저 CPU를 할당하는 기법. 가장 적은 평균 대기 시간을 제공하지만, 실행 시간이 긴 프로세스는 무한정 기다릴 수 있음.

Phần **2. SJF (Shortest Job First)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Sau khi đọc **2. SJF (Shortest Job First)**, đừng bắt đầu lại từ số không. **3. HRN (Highest Response-ratio Next)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **3. HRN (Highest Response-ratio Next)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 3. HRN (Highest Response-ratio Next)

Phần nguồn của **3. HRN (Highest Response-ratio Next)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

SJF의 단점(긴 작업 불리)을 보완하여 대기 시간과 실행 시간을 함께 고려함.
- **우선순위 계산식**: `(대기 시간 + 서비스 시간) / 서비스 시간`
- 결과값이 높은 것부터 우선순위를 부여함.

Các bullet của **3. HRN (Highest Response-ratio Next)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3. HRN (Highest Response-ratio Next)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
