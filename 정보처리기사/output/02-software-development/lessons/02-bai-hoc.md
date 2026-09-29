# 073 & 074: 자료 구조의 정의 및 선형 리스트 (Data Structures & Linear List)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **073 & 074: 자료 구조의 정의 및 선형 리스트 (Data Structures & Linear List)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **073 & 074: 자료 구조의 정의 및 선형 리스트 (Data Structures & Linear List)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **2. 스택 (Stack) 및 응용 (Applications)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

자료, 구조의, 정의, 선형, 리스트

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **1. 자료 구조의 분류 (Classification of Data Structures)**에서 만든 기준을 이어받아 **073 & 074: 자료 구조의 정의 및 선형 리스트 (Data Structures & Linear List)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **073 & 074: 자료 구조의 정의 및 선형 리스트 (Data Structures & Linear List)** và nối nó với **2. 스택 (Stack) 및 응용 (Applications)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 073 & 074: 자료 구조의 정의 및 선형 리스트 (Data Structures & Linear List)

Sau khi đã đặt nền bằng **1. 자료 구조의 분류 (Classification of Data Structures)**, ta chuyển sang **073 & 074: 자료 구조의 정의 및 선형 리스트 (Data Structures & Linear List)**. Đây là mắt xích 2/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **073 & 074: 자료 구조의 정의 및 선형 리스트 (Data Structures & Linear List)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **자료 구조의 분류 (Phân loại)**. Hãy xác định **자료 구조의 분류 (Phân loại)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 자료 구조의 분류 (Phân loại)

Phần nguồn của **자료 구조의 분류 (Phân loại)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **선형 구조 (Linear - Tuyến tính):** 배열 (Array), 리스트 (List), 스택 (Stack), 큐 (Queue), 데크 (Deque).
- **비선형 구조 (Non-Linear - Phi tuyến):** 트리 (Tree), 그래프 (Graph).

Các bullet của **자료 구조의 분류 (Phân loại)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **자료 구조의 분류 (Phân loại)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **배열 (Array - Mảng)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **배열 (Array - Mảng)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 배열 (Array - Mảng)

Các ý ngay dưới **배열 (Array - Mảng)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

---

- **구조화 (Structuring):** 대형 시스템을 분해하여 단위 기능별로 구분, 계층적으로 구성. (Cấu trúc hóa - chia nhỏ thành sơ đồ hình cây).
- **정보 은닉 (Information Hiding):** 한 모듈 내의 정보가 다른 모듈에 영향을 주지 않도록 숨김. (Che giấu thông tin - dùng biến private để tránh đụng độ).

Các bullet của **배열 (Array - Mảng)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **배열 (Array - Mảng)**, đừng bắt đầu lại từ số không. **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)

Bây giờ ta đi vào nội dung của **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **입·출력 구현:** Nhận Input, trả Output. Chú ý liên kết giao diện (CLI/GUI) hoặc dùng Open Source API để kết nối mạng.
- **알고리즘 구현:** Viết code xử lý logic bên trong (Process) sau khi đã có I/O.

---

Các bullet của **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **073 & 074: 자료 구조의 정의 및 선형 리스트 (Data Structures & Linear List)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **2. 스택 (Stack) 및 응용 (Applications)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.