# 프로세스와 스레드 (Process and Thread)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **프로세스와 스레드 (Process and Thread)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **프로세스와 스레드 (Process and Thread)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

프로세스와, 스레드

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)**에서 만든 기준을 이어받아 **프로세스와 스레드 (Process and Thread)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **프로세스와 스레드 (Process and Thread)** và nối nó với **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 프로세스와 스레드 (Process and Thread)

Sau khi đã đặt nền bằng **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)**, ta chuyển sang **프로세스와 스레드 (Process and Thread)**. Đây là mắt xích 62/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **프로세스와 스레드 (Process and Thread)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **PCB(Process Control Block)**, **주요 용어**, **Dispatch (디스패치)**, **Wake Up (웨이크 업)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 프로세스 (Process)**. Hãy xác định **1. 프로세스 (Process)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 프로세스 (Process)

Phần nguồn của **1. 프로세스 (Process)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. 프로세스 (Process)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- CPU에 의해 처리되는 실행 중인 프로그램 (작업/Job, 태스크/Task).
- **PCB(Process Control Block)**: 운영체제가 프로세스에 대한 중요한 정보를 저장하는 곳. (현재 상태, 포인터, 고유 식별자, 스케줄링 우선순위 등). 프로세스 생성 시 만들어지고 완료 시 제거됨.

Các bullet của **1. 프로세스 (Process)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 프로세스 (Process)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 프로세스 상태 전이 (Process State Transition)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 프로세스 상태 전이 (Process State Transition)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 프로세스 상태 전이 (Process State Transition)

Các ý ngay dưới **2. 프로세스 상태 전이 (Process State Transition)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “2. 프로세스 상태 전이 (Process State Transition)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **제출(Submit) -> 접수(Hold) -> 준비(Ready) -> 실행(Run) -> 대기(Wait/Block) -> 종료(Exit)**
- **주요 용어**:
  - **Dispatch (디스패치)**: 준비 상태 -> 실행 상태로 전이 (CPU 할당).
  - **Wake Up (웨이크 업)**: 입·출력 완료 후 대기 상태 -> 준비 상태로 전이.
  - **Spooling (스풀링)**: 디스크를 버퍼처럼 활용해 느린 입출력 장치와 CPU 간 속도 차이를 보완.

Các bullet của **2. 프로세스 상태 전이 (Process State Transition)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. 프로세스 상태 전이 (Process State Transition)**, đừng bắt đầu lại từ số không. **3. 스레드 (Thread)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **3. 스레드 (Thread)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 3. 스레드 (Thread)

Bây giờ ta đi vào nội dung của **3. 스레드 (Thread)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “3. 스레드 (Thread)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 프로세스 내에서의 작업 단위 (경량 프로세스/Light Weight Process).
- 동일 프로세스 환경에서 서로 독립적인 다중 수행이 가능하여 응답 시간을 단축하고 기억장소 낭비를 줄입니다.

> **Vietnamese Explanation**:
> **Process** là một chương trình đang chạy. **Thread** là các luồng xử lý nhỏ nằm bên trong Process. Dùng nhiều thread giúp chương trình chạy nhanh hơn và chia sẻ bộ nhớ tốt hơn (ví dụ nhiều tab trên trình duyệt). **Dispatch** là hành động cấp CPU cho một tiến trình đang xếp hàng chờ.

Các ý về **3. 스레드 (Thread)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Như vậy, **3. 스레드 (Thread)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **프로세스와 스레드 (Process and Thread)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.