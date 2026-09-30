# Môn 2 — 소프트웨어 개발 (Software Development) (Phát triển phần mềm)

## 학습 목표 (Mục tiêu học tập)

Phần này đặt mục tiêu của bài, để người mới biết mình cần giải thích được điều gì trước khi đi vào thuật ngữ và ví dụ.

- 시험에서 사용하는 한국어 용어를 영어와 베트남어 뜻까지 함께 인식한다.
- 각 개념을 정의 → 구성요소/절차 → 비교 포인트 → 예시 순서로 설명할 수 있다.
- 앞에서 배운 개념과 뒤의 심화 개념을 연결하여 문제의 조건을 빠르게 해석한다.

> **Câu hỏi trung tâm:** Khi học môn này, người học không chỉ cần nhận ra thuật ngữ Hàn mà còn phải giải thích khái niệm đang giải quyết vấn đề nào, dựa trên điều kiện nào và được dùng để nối sang phần kiến thức nào tiếp theo.

## 권장 학습 순서 (Lộ trình đề xuất)

Phần này là đường đi của bài giảng: đọc theo thứ tự để mỗi mục sau dùng lại hoặc mở rộng tiêu chí của mục trước.

1. 먼저 이 문서의 각 `##` 단원을 순서대로 읽는다.
2. 단원마다 **핵심 키워드**를 소리 내어 읽고, 한국어 원문과 베트남어 설명을 함께 확인한다.
3. 마지막에 `복습 체크리스트`를 점검한 뒤, 세부 lesson 파일에서 헷갈리는 부분을 다시 본다.

> **Nguồn:** tổng hợp từ các Markdown đã generate trong `raw_md/final`, được đối chiếu với các nguồn `raw` và `raw_md` cùng môn. Nội dung gốc được giữ lại; chỉ chuẩn hoá cấu trúc bài học.

> **Quy ước ngôn ngữ:** phần giải thích ưu tiên tiếng Việt; ở mọi lần xuất hiện, thuật ngữ đề thi dùng dạng `nghĩa Việt (English / 한국어)` để không phải quay lại tìm nghĩa.

> **Cách học:** học theo thứ tự các mục; với mỗi mục, xác định khái niệm → cơ chế/quy tắc → ví dụ → mẹo nhớ. Các mục lặp lại ở phần “심화” (nâng cao) dùng để nối kiến thức trước đó với dạng câu hỏi sâu hơn.

> **Mạch giảng:** mỗi mục mở bằng vị trí và mục đích học, đi qua phần giải thích của nguồn, rồi chốt bằng một câu bàn giao sang mục kế tiếp. Hãy đọc các câu nối như một phần của bài giảng: chúng cho biết vì sao kiến thức hiện tại cần thiết trước khi chuyển sang kiến thức sau.

---

## 1. 자료 구조의 분류 (Classification of Data Structures)

Chúng ta bắt đầu mạch học bằng **1. 자료 구조의 분류 (Classification of Data Structures)**. Trước khi đi vào từng thuật ngữ, hãy giữ câu hỏi trung tâm: phần kiến thức này giải quyết vấn đề gì và vì sao các khái niệm sau phải được đọc trong cùng một bối cảnh? Mục đích của mục 1/101 là tạo điểm tựa để những phần tiếp theo được hiểu theo quan hệ, không chỉ được ghi nhớ như danh sách.

Để đọc **1. 자료 구조의 분류 (Classification of Data Structures)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **선형 구조 (Linear Structure)**, **비선형 구조 (Non-linear Structure)**, **방향/무방향 그래프의 최대 간선 수 (Maximum edges in graphs)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “1. 자료 구조의 분류 (Classification of Data Structures)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **선형 구조 (Linear Structure)**: 배열(Array), 선형 리스트(Linear List), 스택(Stack), 큐(Queue), 데크(Deque)
* **비선형 구조 (Non-linear Structure)**: 트리(Tree), 그래프(Graph)
* **방향/무방향 그래프의 최대 간선 수 (Maximum edges in graphs)**:
  * 무방향 그래프 (Undirected Graph): n(n-1)/2
  * 방향 그래프 (Directed Graph): n(n-1)
* **VI (Vietnamese) (Tiếng Việt):**
  * Cấu trúc tuyến tính: Mảng, danh sách tuyến tính, ngăn xếp, hàng đợi, hàng đợi hai đầu.
  * Cấu trúc phi tuyến: Cây, Đồ thị.
  * Số cạnh tối đa: Đồ thị vô hướng là n(n-1)/2, có hướng là n(n-1).
* **Example**: 노드가 4개인 무방향 그래프의 최대 간선 수는 4(4-1)/2 = 6개입니다. (Với đồ thị vô hướng có 4 đỉnh, số cạnh tối đa là 6).
* 💡 **Mẹo ghi nhớ**: Tuyến tính (Linear) là một đường thẳng (Mảng, Stack, Queue). Phi tuyến là rẽ nhánh (Cây, Đồ thị).

Như vậy, **1. 자료 구조의 분류 (Classification of Data Structures)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **2. 스택 (Stack) 및 응용 (Applications)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 2. 스택 (Stack) 및 응용 (Applications)

Sau khi đã đặt nền bằng **1. 자료 구조의 분류 (Classification of Data Structures)**, ta chuyển sang **2. 스택 (Stack) 및 응용 (Applications)**. Đây là mắt xích 2/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **2. 스택 (Stack) 및 응용 (Applications)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **응용 분야 (Applications)**, **삽입/삭제 (Push/Pop)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “2. 스택 (Stack) 및 응용 (Applications)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 리스트의 한쪽 끝으로만 자료의 삽입, 삭제 작업이 이루어지는 자료 구조.
* 가장 나중에 삽입된 자료가 가장 먼저 삭제되는 후입선출(**LIFO**, Last-In First-Out) 방식.
* **응용 분야 (Applications)**: 인터럽트 처리 (Interrupt handling), 수식 계산 및 표기법 (Expression evaluation), 서브루틴 호출 및 복귀 주소 저장 (Subroutine calls).
* **삽입/삭제 (Push/Pop)**: `PUSH`는 자료 입력, `POP`은 자료 출력.
* **VI (Vietnamese) (Tiếng Việt):**
  * Stack là cấu trúc dữ liệu LIFO, thêm/xóa dữ liệu ở một đầu.
  * Ứng dụng: Xử lý ngắt, tính toán biểu thức, lưu địa chỉ khi gọi hàm.
* **Example**: 브라우저의 '뒤로 가기' 버튼은 스택 구조를 사용합니다. (Nút "Back" trên trình duyệt sử dụng cấu trúc stack).
* 💡 **Mẹo ghi nhớ**: LIFO - Vào sau ra trước, giống như xếp đĩa, lấy đĩa trên cùng ra trước.

Ta có thể khép mục **2. 스택 (Stack) 및 응용 (Applications)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)

Từ **2. 스택 (Stack) 및 응용 (Applications)**, ta đã có điểm tựa để bước vào **075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 3/101 trước khi đi vào chi tiết.

Để đọc **075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **스택 (Stack)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 스택 (Stack)

Các ý ngay dưới **스택 (Stack)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “스택 (Stack)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **LIFO (Last-In-First-Out / 후입선출):** Vào sau ra trước.
- **Con trỏ:** `Top` (Điểm vào/ra), `Bottom` (Đáy).
- **Lỗi:** Overflow (Đầy mà cố nhét), Underflow (Rỗng mà cố lấy).
- **Ứng dụng:** 재귀 호출 (Đệ quy), 후위 표기법 (Postfix).

Các bullet của **스택 (Stack)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **스택 (Stack)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **큐 (Queue)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **큐 (Queue)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 큐 (Queue)

Bây giờ ta đi vào nội dung của **큐 (Queue)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “큐 (Queue)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **FIFO (First-In-First-Out / 선입선출):** Vào trước ra trước.
- **Con trỏ:** `Rear` (Chỗ đưa vào), `Front` (Chỗ lấy ra).
- **Ứng dụng:** 작업 스케줄링 (Lập lịch OS - Xếp hàng chờ xử lý).

Các bullet của **큐 (Queue)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **큐 (Queue)**, đừng bắt đầu lại từ số không. **데크 (Deque - Double Ended Queue)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **데크 (Deque - Double Ended Queue)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 데크 (Deque - Double Ended Queue)

Phần nguồn của **데크 (Deque - Double Ended Queue)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “데크 (Deque - Double Ended Queue)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 양쪽 끝에서 모두 입출력 가능. (Vào/Ra ở cả 2 đầu).
- **Scroll (스크롤):** 입력 제한 (Hạn chế Đầu vào - Vào 1 bên, Ra 2 bên).
- **Shelf (셸프):** 출력 제한 (Hạn chế Đầu ra - Vào 2 bên, Ra 1 bên).

- 💡 **Mẹo ghi nhớ (Mnemonics):**
  - Stack = LIFO = Đệ quy.
  - Queue = FIFO = Lập lịch.
  - Scroll (Cuộn) = Chỉ cuộn vào 1 hướng (Hạn chế Input).
  - Shelf (Cái giá đỡ) = Đẩy đồ vào từ 2 bên nhưng chỉ lấy ra được 1 mặt (Hạn chế Output).

---

Với **데크 (Deque - Double Ended Queue)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Như vậy, **데크 (Deque - Double Ended Queue)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **29. 큐 (Queue)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 29. 큐 (Queue)

Ở bước 4/101, **29. 큐 (Queue)** xuất hiện như phần tiếp nối của **075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **29. 큐 (Queue)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “29. 큐 (Queue)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 삽입은 한쪽 끝에서, 삭제는 반대쪽 끝에서 이루어지는 자료 구조.
* 선입선출(**FIFO**, First-In First-Out) 방식.
* 시작과 끝을 표시하는 두 개의 포인터(Front, Rear)가 있음.
* **VI (Vietnamese) (Tiếng Việt):** Hàng đợi FIFO (Vào trước ra trước). Dùng 2 con trỏ chỉ vị trí đầu và cuối.
* **Example**: 프린터의 인쇄 대기열이나 매표소 줄서기와 같습니다.
* 💡 **Mẹo ghi nhớ**: Queue = Xếp hàng.

Như vậy, **29. 큐 (Queue)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **3. 트리 (Tree)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 3. 트리 (Tree)

Sau khi đã đặt nền bằng **29. 큐 (Queue)**, ta chuyển sang **3. 트리 (Tree)**. Đây là mắt xích 5/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **3. 트리 (Tree)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **디그리 (Degree, 차수)**, **단말 노드 (Terminal Node) = 잎 노드 (Leaf Node)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “3. 트리 (Tree)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 정점(Node)과 선분(Branch)을 이용하여 사이클을 이루지 않도록 구성한 그래프의 특수한 형태.
* **디그리 (Degree, 차수)**: 각 노드에서 뻗어 나온 가지의 수.
* **단말 노드 (Terminal Node) = 잎 노드 (Leaf Node)**: 자식이 하나도 없는 노드, 즉 디그리가 0인 노드.
* **VI (Vietnamese) (Tiếng Việt):**
  * Cây là đồ thị đặc biệt không có chu trình.
  * Bậc (Degree): Số nhánh của một nút con.
  * Nút lá (Leaf): Nút không có con (bậc = 0).
* **Example**: 폴더 구조에서 하위 폴더가 없는 폴더가 단말 노드입니다. (Trong cấu trúc thư mục, thư mục không chứa thư mục con là nút lá).
* 💡 **Mẹo ghi nhớ**: Degree là số con trực tiếp. Leaf là chiếc lá ở cuối cành không mọc thêm được nữa.

Ta có thể khép mục **3. 트리 (Tree)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **4. 이진 트리의 운행법 (Binary Tree Traversal)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 4. 이진 트리의 운행법 (Binary Tree Traversal)

Từ **3. 트리 (Tree)**, ta đã có điểm tựa để bước vào **4. 이진 트리의 운행법 (Binary Tree Traversal)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 6/101 trước khi đi vào chi tiết.

Để đọc **4. 이진 트리의 운행법 (Binary Tree Traversal)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **Preorder (전위)**, **Inorder (중위)**, **Postorder (후위)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “4. 이진 트리의 운행법 (Binary Tree Traversal)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **Preorder (전위)**: Root → Left → Right
* **Inorder (중위)**: Left → Root → Right
* **Postorder (후위)**: Left → Right → Root
* **VI (Vietnamese) (Tiếng Việt):**
  * Preorder: Gốc -> Trái -> Phải.
  * Inorder: Trái -> Gốc -> Phải.
  * Postorder: Trái -> Phải -> Gốc.
* **Example**: 수식 `A + B`를 전위 표기하면 `+ A B`, 중위 표기하면 `A + B`, 후위 표기하면 `A B +`가 됩니다.
* 💡 **Mẹo ghi nhớ**: Tiền/Trung/Hậu tố chỉ vị trí của Root (Gốc) so với Trái/Phải.

Điểm chốt của **4. 이진 트리의 운행법 (Binary Tree Traversal)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **30. 트리 구조 추가 용어 (Tree Terminology Additional)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 30. 트리 구조 추가 용어 (Tree Terminology Additional)

Ở bước 7/101, **30. 트리 구조 추가 용어 (Tree Terminology Additional)** xuất hiện như phần tiếp nối của **4. 이진 트리의 운행법 (Binary Tree Traversal)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **30. 트리 구조 추가 용어 (Tree Terminology Additional)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **자식 노드 (Son Node)**, **부모 노드 (Parent Node)**, **형제 노드 (Sibling / Brother Node)**, **트리의 디그리 (Degree of a Tree)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “30. 트리 구조 추가 용어 (Tree Terminology Additional)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **자식 노드 (Son Node)**: 어떤 노드에 연결된 다음 레벨의 노드들.
* **부모 노드 (Parent Node)**: 어떤 노드에 연결된 이전 레벨의 노드.
* **형제 노드 (Sibling / Brother Node)**: 동일한 부모를 갖는 노드들.
* **트리의 디그리 (Degree of a Tree)**: 전체 노드들의 디그리(자식 수) 중에서 가장 큰 값.
* **VI (Vietnamese) (Tiếng Việt):**
  * Son Node: Nút con.
  * Parent Node: Nút cha.
  * Sibling: Nút anh em (cùng cha).
  * Degree of Tree: Bậc lớn nhất trong tất cả các nút của cây.

Như vậy, **30. 트리 구조 추가 용어 (Tree Terminology Additional)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **025: 트리 (Tree / Cây)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 025: 트리 (Tree / Cây)

Sau khi đã đặt nền bằng **30. 트리 구조 추가 용어 (Tree Terminology Additional)**, ta chuyển sang **025: 트리 (Tree / Cây)**. Đây là mắt xích 8/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **025: 트리 (Tree / Cây)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “025: 트리 (Tree / Cây)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 용어 (Thuật ngữ) | 설명 (Giải thích) | 예시 (Ví dụ) |
|---|---|---|
| 루트 노드 (Root Node) | Nút gốc, không có cha. Chỉ có 1 gốc. | A |
| 단말 노드 (Leaf/Terminal Node) | Nút lá, ở cuối cùng, không có con. | D, E, H, I, G |
| 레벨 (Level) | Độ sâu từ gốc tới nút. | E có Level là 3. |
| 깊이 (Depth) | Độ sâu lớn nhất của cây (Max Level - 1 hoặc tùy cách tính). | Depth = 3. |
| 차수 (Degree of Node) | Bậc của một nút: Số lượng con của nút đó. | B có 3 con => Degree = 3. |
| 트리의 차수 (Degree of Tree) | Bậc của cây: Bậc lớn nhất trong tất cả các nút. | Cả cây có nút max là 3 => Degree của cây = 3. |

Ta bắt đầu phần nội dung bằng **트리 순회 (Tree Traversal - Duyệt cây)**. Hãy xác định **트리 순회 (Tree Traversal - Duyệt cây)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 트리 순회 (Tree Traversal - Duyệt cây)

Phần nguồn của **트리 순회 (Tree Traversal - Duyệt cây)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “트리 순회 (Tree Traversal - Duyệt cây)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **전위 순회 (Preorder):** Root -> Left -> Right.
- **중위 순회 (Inorder):** Left -> Root -> Right.
- **후위 순회 (Postorder):** Left -> Right -> Root.

- **Vietnamese Explanation:** Cách tính Bậc của cây rất hay thi: Tìm cái nút nào đẻ nhiều con nhất, số con đó chính là Bậc của toàn bộ cây. Khi duyệt cây, chữ "Pre/In/Post" (Trước/Giữa/Sau) dùng để chỉ vị trí của Root. Root đứng trước là Pre, ở giữa là In, ở cuối là Post.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 단말 (Đoạn mạt = Cuối) = Leaf (Lá). Degree = Bậc = Số con. Pre/In/Post = Vị trí của Gốc (Root).

---

Với **트리 순회 (Tree Traversal - Duyệt cây)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **트리 순회 (Tree Traversal - Duyệt cây)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **025: 트리 (Tree / Cây)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 078 & 079: 트리 및 운행법 (Tree & Tree Traversal)

Từ **025: 트리 (Tree / Cây)**, ta đã có điểm tựa để bước vào **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 9/101 trước khi đi vào chi tiết.

Để đọc **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **트리 (Tree - Cây)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 트리 (Tree - Cây)

Các ý ngay dưới **트리 (Tree - Cây)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “트리 (Tree - Cây)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **사이클(Cycle)이 없는 그래프.** (Đồ thị không có vòng lặp / chu trình).
- **단말 노드 (Leaf Node):** Nút lá (Không có con / Degree = 0).
- **차수 (Degree):** Số nút con của một nút.
- **트리의 차수 (Tree's Degree):** Degree lớn nhất trong toàn bộ cây.
- **깊이 (Depth):** Số tầng (Level) tối đa của cây.

Với **트리 (Tree - Cây)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **트리 (Tree - Cây)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **트리의 운행법 (Tree Traversal - Duyệt cây)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **트리의 운행법 (Tree Traversal - Duyệt cây)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 트리의 운행법 (Tree Traversal - Duyệt cây)

Bây giờ ta đi vào nội dung của **트리의 운행법 (Tree Traversal - Duyệt cây)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “트리의 운행법 (Tree Traversal - Duyệt cây)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Theo vị trí của **Root (Gốc)**:
  - **Preorder (전위):** **Root** -> Left -> Right.
  - **Inorder (중위):** Left -> **Root** -> Right.
  - **Postorder (후위):** Left -> Right -> **Root**.

- **Ví dụ (Example):** Cây có Gốc A, Trái B, Phải C. Pre = ABC, In = BAC, Post = BCA.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Pre (Trước) = Root đi đầu. In (Giữa) = Root ở giữa. Post (Sau) = Root đi chót.

---

Với **트리의 운행법 (Tree Traversal - Duyệt cây)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **트리의 운행법 (Tree Traversal - Duyệt cây)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **026: 그래프 (Graph / Đồ thị)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 026: 그래프 (Graph / Đồ thị)

Ở bước 10/101, **026: 그래프 (Graph / Đồ thị)** xuất hiện như phần tiếp nối của **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **026: 그래프 (Graph / Đồ thị)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “026: 그래프 (Graph / Đồ thị)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **방향 그래프 (Directed Graph):** Có hướng. Tối đa `n(n-1)` cạnh (n là số đỉnh).
- **무방향 그래프 (Undirected Graph):** Vô hướng. Tối đa `n(n-1)/2` cạnh.

Trước hết, ta đặt **탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)

Bây giờ ta đi vào nội dung của **탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **DFS (Depth-First Search - Tìm kiếm theo chiều sâu):** Đi sâu nhất có thể, hết đường mới lui lại (Dùng Stack).
- **BFS (Breadth-First Search - Tìm kiếm theo chiều rộng):** Loang ra xung quanh, tầng nào xong mới xuống tầng sau (Dùng Queue).

- 💡 **Mẹo ghi nhớ (Mnemonics):** DFS = Sâu = Stack (D/S). BFS = Rộng = Queue (B/Q). Vô hướng chia 2 vì AB và BA là một.

---

Với **탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **026: 그래프 (Graph / Đồ thị)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)

Sau khi đã đặt nền bằng **026: 그래프 (Graph / Đồ thị)**, ta chuyển sang **077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)**. Đây là mắt xích 11/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **최대 간선 수 (Số Cạnh Tối Đa)**. Hãy xác định **최대 간선 수 (Số Cạnh Tối Đa)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 최대 간선 수 (Số Cạnh Tối Đa)

Phần nguồn của **최대 간선 수 (Số Cạnh Tối Đa)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “최대 간선 수 (Số Cạnh Tối Đa)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **무방향 그래프 (Vô hướng):** `n(n-1)/2`.
- **방향 그래프 (Có hướng):** `n(n-1)`. (Gấp đôi vô hướng).
*(n là số đỉnh / Vertex)*

Các bullet của **최대 간선 수 (Số Cạnh Tối Đa)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **최대 간선 수 (Số Cạnh Tối Đa)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **인접 행렬 (Adjacency Matrix - Ma trận kề)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **인접 행렬 (Adjacency Matrix - Ma trận kề)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 인접 행렬 (Adjacency Matrix - Ma trận kề)

Các ý ngay dưới **인접 행렬 (Adjacency Matrix - Ma trận kề)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “인접 행렬 (Adjacency Matrix - Ma trận kề)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Biểu diễn đồ thị bằng ma trận `N x N`. (Có đường đi = 1, Không có = 0).
- **방향 그래프:** Không đối xứng. Hàng (Row) là đi Ra (Out), Cột (Column) là đi Vào (In).
- **무방향 그래프:** Đối xứng qua đường chéo (Symmetric).

- **Vietnamese Explanation:** Nếu đồ thị ít cạnh (thưa) thì dùng Ma trận kề sẽ rất tốn RAM vì toàn số 0. Số cạnh của Đồ thị vô hướng luôn bằng một nửa Đồ thị có hướng vì cạnh A-B và B-A được tính là 1.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Vô hướng / 2 (Vì không phân biệt đi/về). Ma trận vô hướng = Đối xứng.

---

Với **인접 행렬 (Adjacency Matrix - Ma trận kề)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **인접 행렬 (Adjacency Matrix - Ma trận kề)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **5. 수식의 표기법 변환 (Expression Notation Conversion)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 5. 수식의 표기법 변환 (Expression Notation Conversion)

Từ **077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)**, ta đã có điểm tựa để bước vào **5. 수식의 표기법 변환 (Expression Notation Conversion)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 12/101 trước khi đi vào chi tiết.

Để đọc **5. 수식의 표기법 변환 (Expression Notation Conversion)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **Infix → Prefix**, **Infix → Postfix**, **Postfix → Infix**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “5. 수식의 표기법 변환 (Expression Notation Conversion)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **Infix → Prefix**: 연산자를 피연산자 두 개의 **앞(왼쪽)**으로 이동.
* **Infix → Postfix**: 연산자를 피연산자 두 개의 **뒤(오른쪽)**로 이동.
* **Postfix → Infix**: 연산자를 피연산자 두 개의 **가운데**로 이동.
* **VI (Vietnamese) (Tiếng Việt):** Chuyển đổi biểu thức Infix sang Prefix (đưa toán tử ra trước) và Postfix (đưa toán tử ra sau).
* **Example**: Infix `A/B` -> Postfix `A B /` -> Prefix `/ A B`.
* 💡 **Mẹo ghi nhớ**: Prefix (Pre = trước), Postfix (Post = sau).

Điểm chốt của **5. 수식의 표기법 변환 (Expression Notation Conversion)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **080: 수식의 표기법 (Expression Notation)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 080: 수식의 표기법 (Expression Notation)

Ở bước 13/101, **080: 수식의 표기법 (Expression Notation)** xuất hiện như phần tiếp nối của **5. 수식의 표기법 변환 (Expression Notation Conversion)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **080: 수식의 표기법 (Expression Notation)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Chuyển đổi biểu thức toán học tương ứng với duyệt cây.
- **Infix (Trung tố):** `A + B` (Giống Inorder).
- **Prefix (Tiền tố):** `+ A B` (Giống Preorder).
- **Postfix (Hậu tố):** `A B +` (Giống Postorder - Máy tính rất thích kiểu này vì dùng Stack tính cực dễ).

Trước hết, ta đặt **Cách chuyển đổi Infix sang Postfix** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **Cách chuyển đổi Infix sang Postfix** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### Cách chuyển đổi Infix sang Postfix

Bây giờ ta đi vào nội dung của **Cách chuyển đổi Infix sang Postfix**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

1. Đóng ngoặc toàn bộ theo thứ tự ưu tiên: `A / B * (C + D)` -> `((A / B) * (C + D))`
2. Kéo Dấu toán tử ra phía **SAU** dấu ngoặc của nó: `((A B /) (C D +) *)`
3. Xóa ngoặc: `A B / C D + *`

- **Vietnamese Explanation:** Máy tính không hiểu `A+B*C` vì nó không biết cái nào ưu tiên trước. Nó dùng Postfix `A B C * +` ném vào Stack để tính một lèo không cần ngoặc.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Postfix = Dấu nằm ở cuối cụm. Prefix = Dấu nằm ở đầu cụm.

---

Với **Cách chuyển đổi Infix sang Postfix**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **Cách chuyển đổi Infix sang Postfix**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **080: 수식의 표기법 (Expression Notation)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **6. 정렬 알고리즘 (Sorting Algorithms)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 6. 정렬 알고리즘 (Sorting Algorithms)

Sau khi đã đặt nền bằng **080: 수식의 표기법 (Expression Notation)**, ta chuyển sang **6. 정렬 알고리즘 (Sorting Algorithms)**. Đây là mắt xích 14/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **6. 정렬 알고리즘 (Sorting Algorithms)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **삽입 정렬 (Insertion Sort)**, **선택 정렬 (Selection Sort)**, **버블 정렬 (Bubble Sort)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “6. 정렬 알고리즘 (Sorting Algorithms)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **삽입 정렬 (Insertion Sort)**: 두 번째 값부터 시작해 앞의 값들과 비교하여 알맞은 위치에 삽입.
* **선택 정렬 (Selection Sort)**: 가장 작은 값을 선택해 첫 번째와 교환, 그 다음 작은 값을 두 번째와 교환하는 방식.
* **버블 정렬 (Bubble Sort)**: 인접한 두 값을 비교하여 큰 값을 뒤로 보내는 과정을 반복.
* **VI (Vietnamese) (Tiếng Việt):**
  * Insertion: Chèn phần tử vào đúng vị trí của dãy đã sắp xếp.
  * Selection: Chọn phần tử nhỏ nhất đưa lên đầu.
  * Bubble: Nổi bọt, so sánh 2 phần tử kề nhau, lớn hơn thì đổi chỗ.
* **Example**: `8, 5, 6` 버블 정렬 1회전: 5, 8, 6 -> 5, 6, 8. (Bubble sort đổi chỗ 8 và 5, rồi 8 và 6).
* 💡 **Mẹo ghi nhớ**: Insertion: bốc bài và chèn. Selection: tìm người lùn nhất xếp hàng. Bubble: bong bóng lớn nổi lên cuối cùng.

Ta có thể khép mục **6. 정렬 알고리즘 (Sorting Algorithms)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)

Từ **6. 정렬 알고리즘 (Sorting Algorithms)**, ta đã có điểm tựa để bước vào **31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 15/101 trước khi đi vào chi tiết.

Để đọc **31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **퀵 정렬 (Quick Sort)**, **2-Way 합병 정렬 (Merge Sort)**, **힙 정렬 (Heap Sort)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **퀵 정렬 (Quick Sort)**: 키를 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽 서브파일로 분해시키는 방식. 분할(Divide)과 정복(Conquer)을 통해 자료를 정렬.
  * 평균 시간 복잡도: O(n log n), 최악: O(n^2).
* **2-Way 합병 정렬 (Merge Sort)**: 정렬되어 있는 두 개의 파일을 한 개의 파일로 합병하는 방식. 평균/최악 모두 O(n log n).
* **힙 정렬 (Heap Sort)**: 전이진 트리(Complete Binary Tree)를 이용한 정렬 방식. 평균/최악 모두 O(n log n).
* **VI (Vietnamese) (Tiếng Việt):** Các thuật toán sắp xếp bổ sung:
  * Quick Sort: Chia để trị (Divide & Conquer), dùng chốt (pivot).
  * Merge Sort: Trộn 2 mảng đã sắp xếp.
  * Heap Sort: Dùng cây nhị phân hoàn chỉnh.
* **Example**: 퀵 정렬은 반장(기준)을 뽑아서 키 작은 사람은 왼쪽, 큰 사람은 오른쪽으로 세우는 방식입니다.
* 💡 **Mẹo ghi nhớ**: Quick = Nhanh nhưng rủi ro (worst case O(n^2)). Merge/Heap = Luôn ổn định O(n log n).

Điểm chốt của **31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **028: 정렬 (Sorting / Thuật toán sắp xếp)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 028: 정렬 (Sorting / Thuật toán sắp xếp)

Ở bước 16/101, **028: 정렬 (Sorting / Thuật toán sắp xếp)** xuất hiện như phần tiếp nối của **31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **028: 정렬 (Sorting / Thuật toán sắp xếp)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “028: 정렬 (Sorting / Thuật toán sắp xếp)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 알고리즘 (Thuật toán) | 설명 (Giải thích) | 평균 복잡도 (Average) | 최악 (Worst) |
|---|---|---|---|
| 삽입 정렬 (Insertion Sort) | Lấy phần tử thứ i chèn vào đúng vị trí trong mảng con từ 1 tới i-1 đã sắp xếp. | O(n²) | O(n²) |
| 거품 정렬 (Bubble Sort) | So sánh 2 phần tử kề nhau, sai thì đổi chỗ. Phần tử to nhất sẽ "nổi bọt" về cuối. Cần N-1 Pass (Vòng lặp). | O(n²) | O(n²) |
| 선택 정렬 (Selection Sort) | Tìm phần tử nhỏ nhất rồi đổi chỗ nó về vị trí đầu tiên chưa sắp xếp. | O(n²) | O(n²) |
| 퀵 정렬 (Quick Sort) | Chọn Pivot (Chốt), chia làm 2 nửa: Trái nhỏ hơn, Phải to hơn. Lặp lại (Divide & Conquer). | O(n log n) | **O(n²)** |
| 합병 정렬 (Merge Sort) | Chia đôi mảng cho đến khi còn 1 phần tử, sau đó gộp (Merge) lại theo thứ tự. | O(n log n) | O(n log n) |
| 힙 정렬 (Heap Sort) | Dùng cây Complete Binary Tree (Heap) để tìm min/max rồi đưa ra ngoài, cấu trúc lại Heap. | O(n log n) | O(n log n) |

- **Vietnamese Explanation:** Bubble, Selection, Insertion là 3 thuật toán cơ bản, chạy chậm O(n²). Quick, Merge, Heap là thuật toán xịn, chạy nhanh O(n log n). Nhưng Quick Sort xui xẻo (Worst case) vẫn có thể dính O(n²).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Quick Sort (Nhanh) nhưng Worst là N². Bọt (Bubble), Chọn (Selection), Chèn (Insertion) đều là N².

---

Như vậy, **028: 정렬 (Sorting / Thuật toán sắp xếp)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)

Sau khi đã đặt nền bằng **028: 정렬 (Sorting / Thuật toán sắp xếp)**, ta chuyển sang **081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)**. Đây là mắt xích 17/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **이미 순서화된 파일(앞부분)**에 새로운 레코드를 **순서에 맞게 삽입**시켜 정렬. (Lấy phần tử hiện tại chèn vào đúng vị trí trong phần mảng đã sắp xếp phía trước nó).
- **Thời gian (Time Complexity):** O(n²) cho cả Trung bình và Tệ nhất.
- **Số vòng lặp (Pass):** Mảng có n phần tử thì chạy (n-1) vòng. Bắt đầu xét từ phần tử thứ 2.

- **Ví dụ (Example):** Xếp bài tá lả. Bạn rút một lá bài mới lên, xem trên tay bài đã xếp sẵn, thấy chỗ nào vừa thì "chèn" nó vào đó.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 삽입 (Chèn) = Từ khóa "Đã được sắp xếp sẵn" (Đã sắp xếp sẵn). Luôn O(n²).

Ta có thể khép mục **081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **081-2: 셸 정렬 (Shell Sort)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 081-2: 셸 정렬 (Shell Sort)

Từ **081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)**, ta đã có điểm tựa để bước vào **081-2: 셸 정렬 (Shell Sort)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 18/101 trước khi đi vào chi tiết.

Để đọc **081-2: 셸 정렬 (Shell Sort)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “081-2: 셸 정렬 (Shell Sort)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **삽입 정렬(Insertion Sort)을 보완/확장**한 알고리즘. (Phiên bản nâng cấp của Insertion Sort).
- 입력 파일을 매개변수 **h(간격)** 만큼 떨어진 레코드들끼리 묶어 서브파일을 구성하고, 각 서브파일을 삽입 정렬. (Chia mảng thành các nhóm con cách nhau một khoảng $h$, sắp xếp chèn từng nhóm. Sau đó giảm $h$ dần dần về 1).
- **시간 복잡도:** 평균 O(n^1.5), 최악 O(n²). 부분적으로 정렬되어 있는 경우에 매우 유리. (Nhanh hơn O(n²) thông thường. Rất hiệu quả nếu mảng đã "hơi hơi" có thứ tự).

- **Vietnamese Explanation:** Insertion Sort thường yếu khi số nhỏ nằm tuốt ở cuối mảng (phải nhích từng bước lên đầu). Shell Sort dùng khoảng cách $h$ (ví dụ nhảy 5 bước 1 lần) để đưa số nhỏ về đầu nhanh hơn.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Shell = Vỏ ốc (Xoáy từ rộng vào hẹp). Từ khóa: **h (Khoảng cách nhảy)**, **O(n^1.5)**.

---

Điểm chốt của **081-2: 셸 정렬 (Shell Sort)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **082: 선택 정렬 (Selection Sort)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 082: 선택 정렬 (Selection Sort)

Ở bước 19/101, **082: 선택 정렬 (Selection Sort)** xuất hiện như phần tiếp nối của **081-2: 셸 정렬 (Shell Sort)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **082: 선택 정렬 (Selection Sort)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “082: 선택 정렬 (Selection Sort)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **최소값(Minimum)**을 찾아 첫 번째 위치에 놓고, 남은 것 중 또 최소값을 찾아 두 번째 위치에 놓는 방식. (Tìm phần tử nhỏ nhất đổi chỗ lên đầu, tiếp tục tìm số nhỏ nhì đổi chỗ lên thứ hai...).
- **시간 복잡도:** O(n²) (Luôn luôn).
- **Từ khóa:** "최소값을 찾아..." (Tìm giá trị nhỏ nhất...).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Selection = Đi "chọn" thằng nhỏ nhất mang lên đầu.

---

Như vậy, **082: 선택 정렬 (Selection Sort)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **083: 버블 정렬 (Bubble Sort)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 083: 버블 정렬 (Bubble Sort)

Sau khi đã đặt nền bằng **082: 선택 정렬 (Selection Sort)**, ta chuyển sang **083: 버블 정렬 (Bubble Sort)**. Đây là mắt xích 20/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **083: 버블 정렬 (Bubble Sort)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “083: 버블 정렬 (Bubble Sort)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **인접한 두 개의 레코드** 키 값을 비교하여 크기에 따라 위치 교환(Swap). (So sánh 2 phần tử cạnh nhau, số to đẩy lùi về sau. Số to nhất sẽ "nổi bọt" chìm xuống cuối mảng sau vòng đầu tiên).
- **종료 조건:** 더 이상 교환이 일어나지 않으면 정렬 끝. 플래그 비트(Flag Bit) 사용. (Dùng cờ Flag, nếu chạy hết 1 vòng mà không có ai đổi chỗ nghĩa là đã sắp xếp xong).
- **시간 복잡도:** O(n²).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Bubble (Nổi bọt) = Từ khóa **Hai phần tử kề nhau** (Hai cái kề nhau), **플래그 비트** (Flag bit).

---

Ta có thể khép mục **083: 버블 정렬 (Bubble Sort)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **084: 퀵 정렬 (Quick Sort)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 084: 퀵 정렬 (Quick Sort)

Từ **083: 버블 정렬 (Bubble Sort)**, ta đã có điểm tựa để bước vào **084: 퀵 정렬 (Quick Sort)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 21/101 trước khi đi vào chi tiết.

Để đọc **084: 퀵 정렬 (Quick Sort)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “084: 퀵 정렬 (Quick Sort)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **분할과 정복 (Divide and Conquer):** 파일 나누어 정렬.
- **피벗 (Pivot):** 기준값. Nhỏ hơn Pivot sang trái, lớn hơn Pivot sang phải.
- **스택 (Stack) 필요:** 재귀 (Recursion) 호출을 위해. (Dùng đệ quy nên cần Stack nhớ vị trí).
- **가장 빠른 방식:** Trung bình nhanh nhất.
- **시간 복잡도:** 평균 **O(n log n)**, 최악 **O(n²)** (Khi mảng đã sắp xếp sẵn mà chọn Pivot ngu).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Quick = Pivot, Đệ quy, Stack. Tốt: n log n. Xấu: n².

---

Điểm chốt của **084: 퀵 정렬 (Quick Sort)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **085: 힙 정렬 (Heap Sort)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 085: 힙 정렬 (Heap Sort)

Ở bước 22/101, **085: 힙 정렬 (Heap Sort)** xuất hiện như phần tiếp nối của **084: 퀵 정렬 (Quick Sort)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **085: 힙 정렬 (Heap Sort)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “085: 힙 정렬 (Heap Sort)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **전이진 트리 (Complete Binary Tree)**를 힙 트리로 변환하여 정렬. (Xếp mảng thành Cây nhị phân hoàn chỉnh, tạo Heap max/min, lấy dần gốc ra ngoài).
- **시간 복잡도:** Mọi trường hợp (Tốt, trung bình, xấu) đều là **O(n log n)**. Rất ổn định, ít tốn RAM.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Heap = Cây (Cây (Tree)). Ổn định ở mức O(n log n).

---

Như vậy, **085: 힙 정렬 (Heap Sort)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **086: 2-Way 합병 정렬 (Merge Sort)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 086: 2-Way 합병 정렬 (Merge Sort)

Sau khi đã đặt nền bằng **085: 힙 정렬 (Heap Sort)**, ta chuyển sang **086: 2-Way 합병 정렬 (Merge Sort)**. Đây là mắt xích 23/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **086: 2-Way 합병 정렬 (Merge Sort)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “086: 2-Way 합병 정렬 (Merge Sort)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 이미 정렬된 두 개의 파일을 하나의 파일로 **합치며 (Merge)** 정렬. (Cưa đôi mảng liên tục đến khi còn 1 phần tử, rồi gộp từ từ lại thành 2, 4, 8...).
- **시간 복잡도:** Mọi trường hợp đều **O(n log n)**. 안정 정렬 (Stable Sort).

---

Ta có thể khép mục **086: 2-Way 합병 정렬 (Merge Sort)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **086-1: 기수 정렬 (Radix Sort / Bucket Sort)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 086-1: 기수 정렬 (Radix Sort / Bucket Sort)

Từ **086: 2-Way 합병 정렬 (Merge Sort)**, ta đã có điểm tựa để bước vào **086-1: 기수 정렬 (Radix Sort / Bucket Sort)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 24/101 trước khi đi vào chi tiết.

Để đọc **086-1: 기수 정렬 (Radix Sort / Bucket Sort)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “086-1: 기수 정렬 (Radix Sort / Bucket Sort)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 데이터를 비교하지 않음! **큐(Queue)**를 이용하여 데이터의 **자릿수(Digit)**별로 나누어 담았다가 꺼냄. (Không dùng dấu < hay > để so sánh. Nhìn vào chữ số hàng Đơn vị, phân vào 10 cái Queue (0-9). Xong ráp lại, làm tiếp hàng Chục, Trăm...).
- **시간 복잡도:** **O(d*n)** (Trong đó d là số chữ số dài nhất). Cực kỳ nhanh, vượt qua giới hạn n log n của các thuật toán so sánh thông thường.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Radix (Cơ số) = Chữ số (Hàng đơn vị, chục...) (Chữ số), Queue/Bucket. Siêu tốc O(dn).

---

Điểm chốt của **086-1: 기수 정렬 (Radix Sort / Bucket Sort)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **7. 이분 검색 (Binary Search)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 7. 이분 검색 (Binary Search)

Ở bước 25/101, **7. 이분 검색 (Binary Search)** xuất hiện như phần tiếp nối của **086-1: 기수 정렬 (Radix Sort / Bucket Sort)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **7. 이분 검색 (Binary Search)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “7. 이분 검색 (Binary Search)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 검색할 데이터가 정렬되어 있어야 함.
* 비교 횟수를 거듭할 때마다 검색 대상이 반(절반)으로 줄어듦.
* 탐색 효율이 좋고 시간이 적게 소요됨. 중간 레코드 번호(M) = (F+L)/2.
* **VI (Vietnamese) (Tiếng Việt):** Tìm kiếm nhị phân. Dữ liệu phải được sắp xếp trước. Mỗi lần chia đôi không gian tìm kiếm.
* **Example**: 사전에서 단어를 찾을 때 책을 반으로 계속 쪼개며 찾는 방식입니다.
* 💡 **Mẹo ghi nhớ**: Binary = chia đôi (phải sắp xếp trước!).

Như vậy, **7. 이분 검색 (Binary Search)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)

Sau khi đã đặt nền bằng **7. 이분 검색 (Binary Search)**, ta chuyển sang **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)**. Đây là mắt xích 26/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **검색 (Search - Tìm kiếm)**. Hãy xác định **검색 (Search - Tìm kiếm)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 검색 (Search - Tìm kiếm)

Phần nguồn của **검색 (Search - Tìm kiếm)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “검색 (Search - Tìm kiếm)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **순차 검색 (Sequential/Linear Search):** Tìm tuần tự từ đầu đến cuối. Dùng cho mảng *chưa sắp xếp*. O(n).
- **이진 검색 (Binary Search):** Tìm nhị phân. Chia đôi mảng liên tục. **Bắt buộc mảng phải ĐÃ SẮP XẾP.** O(log n). Rất nhanh.

Các bullet của **검색 (Search - Tìm kiếm)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **검색 (Search - Tìm kiếm)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **해싱 (Hashing - Băm dữ liệu)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **해싱 (Hashing - Băm dữ liệu)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 해싱 (Hashing - Băm dữ liệu)

Các ý ngay dưới **해싱 (Hashing - Băm dữ liệu)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “해싱 (Hashing - Băm dữ liệu)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Dùng hàm băm (Hash Function) tính ra trực tiếp địa chỉ bộ nhớ để lưu hoặc tìm kiếm dữ liệu. Nhanh nhất (O(1)).

- **Vietnamese Explanation:** Tìm tuần tự là lật từng trang sách. Tìm nhị phân là mở giữa cuốn từ điển, xem vần nào rồi gập nửa bỏ đi, tìm tiếp ở nửa kia. Băm (Hashing) là nhìn Mục lục rồi lật thẳng trang đó.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Binary Search = Phải Sắp Xếp (Sắp xếp), Chia đôi (절반). Hashing = O(1) Siêu Tốc.

Với **해싱 (Hashing - Băm dữ liệu)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **해싱 (Hashing - Băm dữ liệu)**, đừng bắt đầu lại từ số không. **해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)

Bây giờ ta đi vào nội dung của **해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 방법 (Phương pháp) | 설명 (Giải thích) |
|---|---|
| **체이닝 (Chaining - Móc xích)** | 버킷 내에 연결리스트(Linked List)를 할당하여 데이터들을 연결하는 방식. (Dùng danh sách liên kết để nối các phần tử bị đụng độ lại với nhau trong cùng 1 bucket.) |
| **개방 주소법 (Open Addressing - Địa chỉ mở)** | 충돌이 일어났을 때 다른 버킷에 데이터를 삽입해 해결하는 방식. (Khi đụng độ, tìm một ô trống khác để nhét vào. Địa chỉ dữ liệu bị thay đổi so với ban đầu.) |
| 선형 탐색 (Linear Probing) | 해시충돌 시 다음 버킷, 혹은 몇 개를 건너뛰어 삽입. (Thử tuyến tính: Tìm ô trống kế tiếp.) |
| 제곱 탐색 (Quadratic Probing) | 해시충돌 시 제곱만큼 건너뛴 버킷에 삽입 (1, 4, 9, 16...). (Thử bậc hai: Nhảy xa dần theo bình phương để tránh tụ tập.) |
| 이중 해시 (Double Hashing) | 해시충돌 시 다른 해싱함수를 한 번 더 적용. (Băm kép: Dùng thêm một hàm băm phụ để tìm khoảng nhảy.) |

- **Vietnamese Explanation:** Khi hai dữ liệu băm ra cùng một địa chỉ (Collision), ta phải giải quyết. Chaining là cho chúng ở chung một nhà nhưng nối đuôi nhau (như xâu chuỗi). Open Addressing là "nhà này có người rồi, mời anh đi tìm nhà khác".
- 💡 **Mẹo ghi nhớ (Mnemonics):** Chaining = Dây xích (Linked List). Open Addressing = Mở cửa đi tìm nhà khác (Linear, Quadratic, Double).

---

Khi đọc **해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)**, hãy tách hai lớp: bảng giúp đối chiếu các loại hoặc tiêu chí, còn công thức cần được đọc theo biến, đơn vị và quan hệ giữa các đại lượng. Cách tách này giúp ta hiểu cơ chế trước khi ghi nhớ ký hiệu.

Như vậy, **해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **087: 이분 검색 (Binary Search - Tìm kiếm nhị phân)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 087: 이분 검색 (Binary Search - Tìm kiếm nhị phân)

Từ **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)**, ta đã có điểm tựa để bước vào **087: 이분 검색 (Binary Search - Tìm kiếm nhị phân)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 27/101 trước khi đi vào chi tiết.

Để đọc **087: 이분 검색 (Binary Search - Tìm kiếm nhị phân)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “087: 이분 검색 (Binary Search - Tìm kiếm nhị phân)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **전제조건 (Bắt buộc):** 파일이 **반드시 순서화(정렬, Ordered)** 되어 있어야 함. (Mảng bắt buộc phải được sắp xếp từ trước).
- **원리:** 찾고자 하는 값을 중간 레코드(Middle, `M = (F+L)/2`)와 비교하여 탐색 범위를 절반씩 줄임.
- **시간 복잡도:** **O(log n)**. (Gấp ngàn lần tìm tuần tự. 1000 phần tử chỉ cần tìm 10 lần).

---

Điểm chốt của **087: 이분 검색 (Binary Search - Tìm kiếm nhị phân)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **8. 주요 해싱 함수 (Hashing Functions)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 8. 주요 해싱 함수 (Hashing Functions)

Ở bước 28/101, **8. 주요 해싱 함수 (Hashing Functions)** xuất hiện như phần tiếp nối của **087: 이분 검색 (Binary Search - Tìm kiếm nhị phân)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **8. 주요 해싱 함수 (Hashing Functions)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **제산법 (Division)**, **제곱법 (Mid-Square)**, **폴딩법 (Folding)**, **숫자 분석법 (Digit Analysis)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “8. 주요 해싱 함수 (Hashing Functions)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **제산법 (Division)**: 키 값을 소수(Prime)로 나눈 나머지를 주소로 사용.
* **제곱법 (Mid-Square)**: 키 값을 제곱한 후 중간 부분의 값을 주소로 사용.
* **폴딩법 (Folding)**: 키 값을 여러 부분으로 나눈 후 더하거나 XOR한 값을 주소로 사용.
* **숫자 분석법 (Digit Analysis)**: 숫자의 분포를 분석해 고른 자리를 주소로 사용.
* **VI (Vietnamese) (Tiếng Việt):** Các hàm băm (Hashing) giúp ánh xạ khóa (key) thành địa chỉ. Division (chia lấy dư), Mid-Square (bình phương lấy giữa), Folding (gấp/cộng các phần), Digit Analysis (phân tích chữ số).
* **Example**: 제산법으로 키 10을 해시 테이블 크기 7(소수)로 나누면 나머지 3이 주소가 됩니다.
* 💡 **Mẹo ghi nhớ**: Division = Chia lấy dư, Square = Bình phương, Fold = Gấp lại.

Như vậy, **8. 주요 해싱 함수 (Hashing Functions)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **32. 추가 해싱 함수 (Additional Hashing Functions)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 32. 추가 해싱 함수 (Additional Hashing Functions)

Sau khi đã đặt nền bằng **8. 주요 해싱 함수 (Hashing Functions)**, ta chuyển sang **32. 추가 해싱 함수 (Additional Hashing Functions)**. Đây là mắt xích 29/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **32. 추가 해싱 함수 (Additional Hashing Functions)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **기수 변환법 (Radix)**, **대수적 코딩법 (Algebraic Coding)**, **무작위법 (Random)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “32. 추가 해싱 함수 (Additional Hashing Functions)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **기수 변환법 (Radix)**: 키 숫자의 진수를 다른 진수로 변환.
* **대수적 코딩법 (Algebraic Coding)**: 다항식의 계수로 간주하여 나눈 나머지 사용.
* **무작위법 (Random)**: 난수를 발생시켜 홈 주소로 사용.
* **VI (Vietnamese) (Tiếng Việt):** Các hàm băm khác: Cơ số (Radix), Đại số (Algebraic), Ngẫu nhiên (Random).

Ta có thể khép mục **32. 추가 해싱 함수 (Additional Hashing Functions)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **088: 해싱 (Hashing) & 088-1: 데이터저장소 (Data Storage)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 088: 해싱 (Hashing) & 088-1: 데이터저장소 (Data Storage)

Từ **32. 추가 해싱 함수 (Additional Hashing Functions)**, ta đã có điểm tựa để bước vào **088: 해싱 (Hashing) & 088-1: 데이터저장소 (Data Storage)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 30/101 trước khi đi vào chi tiết.

Để đọc **088: 해싱 (Hashing) & 088-1: 데이터저장소 (Data Storage)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **해싱 함수 (Hash Function)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 해싱 함수 (Hash Function)

Các ý ngay dưới **해싱 함수 (Hash Function)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “해싱 함수 (Hash Function)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Chuyển `Key` thành `Home Address` trong Hash Table.
- Từ khóa: Bucket (Xô), Slot (Khe), Collision (Đụng độ - 2 Key ra chung 1 Address), Overflow (Tràn - Bucket hết chỗ trống).
- **제산법 (Division):** Phổ biến nhất. Lấy Key chia cho số nguyên tố $Q$ lấy phần dư (Modulus).

Các bullet của **해싱 함수 (Hash Function)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **해싱 함수 (Hash Function)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **데이터저장소 (Data Storage)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **데이터저장소 (Data Storage)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 데이터저장소 (Data Storage)

Bây giờ ta đi vào nội dung của **데이터저장소 (Data Storage)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “데이터저장소 (Data Storage)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **논리 (Logical):** 연관성, 구조 (Cấu trúc, liên kết, bản thiết kế trên giấy).
- **물리 (Physical):** 하드웨어, 저장장치 (Phần cứng thực tế ổ cứng HDD/SSD).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Logic = Bản vẽ. Physical = Tòa nhà thực tế.

---

Với **데이터저장소 (Data Storage)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **데이터저장소 (Data Storage)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **088: 해싱 (Hashing) & 088-1: 데이터저장소 (Data Storage)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)

Ở bước 31/101, **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)** xuất hiện như phần tiếp nối của **088: 해싱 (Hashing) & 088-1: 데이터저장소 (Data Storage)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **단위 모듈 (Unit Module)**, **IPC (프로세스 간 통신)**, **IPC 대표 메소드**, **Shared Memory** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **단위 모듈 (Unit Module)**: 한 가지 동작을 수행하는 기능 모듈 (독립적인 컴파일 가능).
* **IPC (프로세스 간 통신)**: 복수의 프로세스 간 통신을 구현하는 방법.
* **IPC 대표 메소드**:
  * **Shared Memory**: 다수 프로세스가 공유 가능한 메모리 구성.
  * **Socket**: 네트워크 소켓을 이용한 통신.
  * **Semaphores**: 공유 자원에 대한 접근 제어.
  * **Pipes & Named Pipes**: 선입선출(FIFO) 형태의 공유 메모리 사용.
  * **Message Queueing**: 메시지 전달 방식.
* **VI (Vietnamese) (Tiếng Việt):** Giao tiếp giữa các tiến trình (IPC). Các phương thức: Bộ nhớ chia sẻ, Socket (mạng), Cờ hiệu (Semaphore), Ống dẫn (Pipes), Hàng đợi tin nhắn.
* **Example**: 두 개의 프로그램이 채팅을 주고받을 때 Socket이나 Message Queue를 사용합니다.
* 💡 **Mẹo ghi nhớ**: S-S-S-P-M (Shared memory, Socket, Semaphore, Pipe, Message Queue).

Như vậy, **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **핵심 031: 모듈 구현 (Module Implementation)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 핵심 031: 모듈 구현 (Module Implementation)

Sau khi đã đặt nền bằng **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)**, ta chuyển sang **핵심 031: 모듈 구현 (Module Implementation)**. Đây là mắt xích 32/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **핵심 031: 모듈 구현 (Module Implementation)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “핵심 031: 모듈 구현 (Module Implementation)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **구현 (Implementation):** 설계 명세서가 컴퓨터가 알 수 있는 모습으로 변환되는 과정. 프로그래밍 또는 코딩. (Quá trình chuyển thiết kế thành code.)
- **작업 절차 (Trình tự):** 코딩 계획 (Lập kế hoạch) → 코딩 (Code) → 컴파일 (Compile) → 테스트 (Test).
- **모듈 (Module):** 독립적인 기능을 갖는 단위. 모듈이 모이면 프로그램이 됨. (Một đơn vị độc lập thực hiện một chức năng cụ thể.)
- **컴포넌트 (Component):** 독립적으로 존재할 수 있는 부분, 재사용되는 단위, 인터페이스를 통해서만 접근. (Thành phần có thể tái sử dụng, giao tiếp qua Interface.)

- **Vietnamese Explanation:** Module là một khối code (như một hàm hoặc một class). Component là một khối lớn hơn, đóng gói sẵn và có thể lắp ráp vào nhiều phần mềm khác nhau (như một nút bấm UI, một bộ lịch).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Trình tự: Kế hoạch -> Code -> Dịch (Compile) -> Thử (Test). Module = Ghép lại thành chương trình. Component = Tái sử dụng qua Interface.

---

Ta có thể khép mục **핵심 031: 모듈 구현 (Module Implementation)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)

Từ **핵심 031: 모듈 구현 (Module Implementation)**, ta đã có điểm tựa để bước vào **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 33/101 trước khi đi vào chi tiết.

Để đọc **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **단위 모듈 (Unit Module)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 단위 모듈 (Unit Module)

Các ý ngay dưới **단위 모듈 (Unit Module)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “단위 모듈 (Unit Module)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 프로그램의 단위 기능을 구현하는 독립적인 최소 소프트웨어 단위. (Đơn vị phần mềm nhỏ nhất, độc lập, thực hiện 1 chức năng duy nhất).

Các bullet của **단위 모듈 (Unit Module)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **단위 모듈 (Unit Module)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)

Bây giờ ta đi vào nội dung của **단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **추상화 (Abstraction):** 복잡한 시스템을 단순하게 구현. (Trừu tượng hóa - ẩn đi sự phức tạp).
- **구조화 (Structuring):** 대형 시스템을 분해하여 단위 기능별로 구분, 계층적으로 구성. (Cấu trúc hóa - chia nhỏ thành sơ đồ hình cây).
- **정보 은닉 (Information Hiding):** 한 모듈 내의 정보가 다른 모듈에 영향을 주지 않도록 숨김. (Che giấu thông tin - dùng biến private để tránh đụng độ).

Các bullet của **단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)**, đừng bắt đầu lại từ số không. **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)

Phần nguồn của **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **입·출력 구현:** Nhận Input, trả Output. Chú ý liên kết giao diện (CLI/GUI) hoặc dùng Open Source API để kết nối mạng.
- **알고리즘 구현:** Viết code xử lý logic bên trong (Process) sau khi đã có I/O.

---

Các bullet của **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)

Ở bước 34/101, **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)** xuất hiện như phần tiếp nối của **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)

Bây giờ ta đi vào nội dung của **IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 모듈 간 또는 복수의 프로세스 간 통신을 위한 인터페이스. (Cách các chương trình đang chạy nói chuyện với nhau).
- **Các phương pháp IPC:**
  - **Shared Memory (Bộ nhớ chia sẻ):** Nhanh nhất. Các process dùng chung 1 vùng RAM.
  - **Socket (Ổ cắm):** Giao tiếp qua mạng.
  - **Semaphores (Cờ hiệu):** Đồng bộ hóa, khóa (Locking) tài nguyên dùng chung.
  - **Pipes (Ống dẫn):** Dùng RAM theo kiểu FIFO, tại 1 thời điểm chỉ 1 process được dùng.
  - **Message Queueing (Hàng đợi tin nhắn):** Truyền tin bất đồng bộ.

Các bullet của **IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **알고리즘 구현 모듈 (Các loại Module khi lập trình)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **알고리즘 구현 모듈 (Các loại Module khi lập trình)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 알고리즘 구현 모듈 (Các loại Module khi lập trình)

Phần nguồn của **알고리즘 구현 모듈 (Các loại Module khi lập trình)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “알고리즘 구현 모듈 (Các loại Module khi lập trình)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **디바이스 드라이버 모듈 (Device Driver):** Điều khiển phần cứng ngoại vi (vd: Máy in).
- **네트워크 모듈 (Network):** Truyền thông dữ liệu mạng.
- **파일 모듈 (File):** Truy xuất cấu trúc file trên đĩa cứng.
- **메모리 모듈 (Memory):** Quản lý RAM, cấp phát bộ nhớ ảo, hoặc làm IPC.
- **프로세스 모듈 (Process):** Tạo và quản lý các tiến trình khác.

- 💡 **Mẹo ghi nhớ (Mnemonics):** IPC là gửi thư cho nhau. Shared Memory = Bảng tin chung (Nhanh nhất). Semaphore = Cái khóa cửa nhà vệ sinh (Ai đang dùng thì khóa lại).

---

Với **알고리즘 구현 모듈 (Các loại Module khi lập trình)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **알고리즘 구현 모듈 (Các loại Module khi lập trình)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)

Sau khi đã đặt nền bằng **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)**, ta chuyển sang **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**. Đây là mắt xích 35/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **단위 모듈 테스트 (Unit Module Test)**. Hãy xác định **단위 모듈 테스트 (Unit Module Test)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 단위 모듈 테스트 (Unit Module Test)

Phần nguồn của **단위 모듈 테스트 (Unit Module Test)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “단위 모듈 테스트 (Unit Module Test)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 코딩 직후 최소 단위인 모듈이나 컴포넌트에 초점을 맞춤. (Test ngay sau khi code xong 1 hàm/module).
- Chủ yếu dùng **화이트박스 (White-box test)** để tìm lỗi thuật toán, vòng lặp vô hạn, lỗi công thức toán học.

Với **단위 모듈 테스트 (Unit Module Test)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **단위 모듈 테스트 (Unit Module Test)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **테스트 케이스 (Test Case)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **테스트 케이스 (Test Case)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 테스트 케이스 (Test Case)

Các ý ngay dưới **테스트 케이스 (Test Case)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “테스트 케이스 (Test Case)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 입력 값, 실행 조건, 기대 결과의 명세서. (Tài liệu ghi rõ: Nhập gì, Điều kiện gì, Kết quả mong đợi là gì).
- 테스트 케이스를 미리 작성(사전에 정의)해야 인력과 시간 낭비를 방지. (Phải viết Test Case **trước** khi code hoặc test, để tránh test lung tung tốn thời gian).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Test Case = Input + Condition + Expected Output. Bắt buộc viết trước khi test.

---

Với **테스트 케이스 (Test Case)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **테스트 케이스 (Test Case)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **13. 형상 관리 (SCM - Software Configuration Management)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 13. 형상 관리 (SCM - Software Configuration Management)

Từ **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**, ta đã có điểm tựa để bước vào **13. 형상 관리 (SCM - Software Configuration Management)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 36/101 trước khi đi vào chi tiết.

Để đọc **13. 형상 관리 (SCM - Software Configuration Management)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **도구 (Tools)**, **주요 기능 (Key Functions)**, **Check-Out**, **Check-In** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “13. 형상 관리 (SCM - Software Configuration Management)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 변경 사항을 관리하기 위해 개발된 일련의 활동. 목적: 개발 비용 감소, 방해 요인 최소화.
* **도구 (Tools)**: Git, CVS, Subversion(SVN).
* **주요 기능 (Key Functions)**:
  * **Check-Out**: 저장소에서 파일을 받아옴.
  * **Check-In**: 수정을 완료한 후 저장소에 새로운 버전으로 갱신.
  * **Commit**: 갱신 시 충돌을 알리고 수정한 후 완료함.
* **VI (Vietnamese) (Tiếng Việt):** Quản lý cấu hình phần mềm (quản lý thay đổi/version).
  * Check-out: Lấy file về.
  * Check-in: Lưu file lên.
  * Commit: Lưu thay đổi (xử lý xung đột nếu có).
* **Example**: Git에서 코드를 가져오는 것이 Checkout, 수정 후 서버에 올리는 것이 Commit/Check-in입니다.
* 💡 **Mẹo ghi nhớ**: In = vào kho, Out = ra khỏi kho.

Điểm chốt của **13. 형상 관리 (SCM - Software Configuration Management)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)

Ở bước 37/101, **40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)** xuất hiện như phần tiếp nối của **13. 형상 관리 (SCM - Software Configuration Management)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **형상 관리 (SCM)**, **기능**, **버전 관리 방식 3가지**, **SVN (Subversion)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **형상 관리 (SCM)**: 소프트웨어 개발 과정에서 변경 사항을 관리하는 일련의 활동.
  * **기능**: 형상 식별, 버전 제어, 형상 통제(변경 관리), 형상 감사, 형상 기록.
* **버전 관리 방식 3가지**:
  1. **공유 폴더 방식 (Shared Folder)**: 로컬 공유 폴더에 저장. (SCCS, RCS 등).
  2. **클라이언트/서버 방식 (C/S)**: 중앙 서버에 저장하여 관리. (CVS, SVN 등).
     * **SVN (Subversion)**: `trunk`에서 주로 개발, `branches`에서 추가 작업 후 병합(merge). 커밋 시 리비전(Revision) 1씩 증가.
  3. **분산 저장소 방식 (Distributed)**: 로컬 저장소와 원격 저장소에 함께 저장. (Git 등).
     * **Git**: 로컬에서 버전 관리가 가능해 빠르고 네트워크 문제 시에도 작업 가능. 스냅샷(Snapshot)으로 파일 변화를 저장.
* **주요 기능**: Repository, Import, Check-Out(가져오기), Check-In/Commit(반영), Update(동기화).
* **VI (Vietnamese) (Tiếng Việt):** Quản lý cấu hình (SCM) và các cách quản lý phiên bản.
  * Shared Folder: Lưu ở thư mục chung.
  * C/S: Lưu ở server trung tâm (SVN).
  * Distributed: Lưu phân tán cả local và server (Git). Git dùng Snapshot để lưu thay đổi.
* **Example**: 회사에서 SVN을 쓰면 중앙 서버가 죽었을 때 작업을 올릴 수 없지만, Git을 쓰면 내 PC(Local)에 저장해뒀다가 서버가 복구되면 올릴 수 있습니다.

Như vậy, **40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)

Sau khi đã đặt nền bằng **40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)**, ta chuyển sang **핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)**. Đây là mắt xích 38/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **형상 관리 (Configuration Management)**. Hãy xác định **형상 관리 (Configuration Management)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 형상 관리 (Configuration Management)

Phần nguồn của **형상 관리 (Configuration Management)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “형상 관리 (Configuration Management)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 소프트웨어 개발 과정의 **변경 사항을 관리**하는 것. (Quản lý mọi thay đổi trong vòng đời phần mềm - Version Control).
- 대상 (Đối tượng): 계획, 요구 분석서, 설계서, 소스 코드, 테스트 케이스, 지침서 등. (**개발 비용 - Chi phí phát triển KHÔNG nằm trong này**).
- 절차 (Trình tự): 형상 식별 (Nhận dạng) → 형상 통제 (Kiểm soát bởi CCB) → 형상 감사 (Kiểm toán) → 형상 기록 (Ghi lại).

Các bullet của **형상 관리 (Configuration Management)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **형상 관리 (Configuration Management)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **형상 관리 방식 (Các phương pháp quản lý phiên bản)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **형상 관리 방식 (Các phương pháp quản lý phiên bản)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 형상 관리 방식 (Các phương pháp quản lý phiên bản)

Các ý ngay dưới **형상 관리 방식 (Các phương pháp quản lý phiên bản)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “형상 관리 방식 (Các phương pháp quản lý phiên bản)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **공유 폴더 방식 (Shared Folder):** Lưu vào chung một thư mục trên mạng nội bộ. (Ví dụ: RCS).
- **클라이언트/서버 방식 (Client/Server):** Quản lý tập trung trên một máy chủ. (Ví dụ: CVS, SVN).
- **분산 저장소 방식 (Distributed Repository):** Mỗi máy cá nhân đều chứa một bản copy của kho chứa, commit lên máy cá nhân trước rồi mới push lên server. Rất an toàn. (Ví dụ: **Git**).

Các ý về **형상 관리 방식 (Các phương pháp quản lý phiên bản)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **형상 관리 방식 (Các phương pháp quản lý phiên bản)**, đừng bắt đầu lại từ số không. **형상 관리 도구 기능 (Chức năng công cụ)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **형상 관리 도구 기능 (Chức năng công cụ)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 형상 관리 도구 기능 (Chức năng công cụ)

Bây giờ ta đi vào nội dung của **형상 관리 도구 기능 (Chức năng công cụ)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “형상 관리 도구 기능 (Chức năng công cụ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **Check-In:** Đẩy code lên kho (Upload).
- **Check-Out:** Lấy code mới nhất về (Download).
- **Commit:** Xác nhận lưu sự thay đổi.

Các bullet của **형상 관리 도구 기능 (Chức năng công cụ)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**형상 관리 도구 기능 (Chức năng công cụ)** vừa cho ta cách đặt câu hỏi. Bây giờ **IDE (Integrated Development Environment - Môi trường phát triển tích hợp)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **IDE (Integrated Development Environment - Môi trường phát triển tích hợp)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### IDE (Integrated Development Environment - Môi trường phát triển tích hợp)

Phần nguồn của **IDE (Integrated Development Environment - Môi trường phát triển tích hợp)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “IDE (Integrated Development Environment - Môi trường phát triển tích hợp)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 코딩, 컴파일, 디버깅, 배포 (Coding, Compile, Debug, Deployment) 기능을 하나로 통합. (Tích hợp tất cả công cụ lập trình vào một phần mềm).
- Ví dụ: Eclipse (Java), Visual Studio (C#, C++), Xcode (iOS), Android Studio, IntelliJ IDEA.

- **Vietnamese Explanation:** Quản lý hình thái (Configuration/Version) giống như việc lưu file "Bao_cao_lan1", "Bao_cao_lan2", "Bao_cao_FINAL". Git (Phân tán) là công cụ phổ biến nhất hiện nay. IDE là bộ công cụ tất cả-trong-một của lập trình viên (vừa gõ code, vừa dịch, vừa tìm lỗi).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Trình tự 형상 quản lý: Nhận Kiểm Đánh Ghi (Nhận diện - Kiểm soát - Đánh giá - Ghi chép). Git = Phân tán (분산). IDE 4 bước: CoCoDeDe (Coding - Compile - Debugging - Deployment).

---

Với **IDE (Integrated Development Environment - Môi trường phát triển tích hợp)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **IDE (Integrated Development Environment - Môi trường phát triển tích hợp)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 109 ~ 112: 형상 관리 (SCM - Software Configuration Management)

Từ **핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)**, ta đã có điểm tựa để bước vào **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 39/101 trước khi đi vào chi tiết.

Để đọc **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “109 ~ 112: 형상 관리 (SCM - Software Configuration Management)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **형상 관리 (SCM):** 소프트웨어 변경 사항을 체계적으로 관리. (Quản lý mọi thay đổi của phần mềm: Source code, tài liệu, thiết kế... trong suốt vòng đời).
- **목적:** 가시성 (Tính hiển thị - ai đang làm gì), 추적성 (Tính truy xuất - ai gây ra lỗi này), 무절제한 변경 방지 (Ngăn chặn việc sửa code vô tội vạ).

Để không đọc **형상 관리 5대 기능 (5 Chức năng của SCM)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 형상 관리 5대 기능 (5 Chức năng của SCM)

Các ý ngay dưới **형상 관리 5대 기능 (5 Chức năng của SCM)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

1. **형상 식별 (Identification):** Đặt tên, đánh số phiên bản, phân nhánh (Tree) để dễ quản lý.
2. **버전 제어 (Version Control):** Lưu lại các version cũ/mới.
3. **형상 통제 (Configuration Control):** Yêu cầu đổi code phải được xem xét kỹ trước khi nhập vào bản chính (Baseline).
4. **형상 감사 (Audit):** Kiểm tra lại xem code đã chuẩn chưa.
5. **형상 기록 (Status Reporting):** Ghi chép lịch sử báo cáo.

Phần **형상 관리 5대 기능 (5 Chức năng của SCM)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Ta vừa chốt **형상 관리 5대 기능 (5 Chức năng của SCM)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **버전 관리 용어 (Thuật ngữ Version Control)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **버전 관리 용어 (Thuật ngữ Version Control)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 버전 관리 용어 (Thuật ngữ Version Control)

Bây giờ ta đi vào nội dung của **버전 관리 용어 (Thuật ngữ Version Control)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “버전 관리 용어 (Thuật ngữ Version Control)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **저장소 (Repository):** Kho lưu trữ code.
- **체크아웃 (Check-out):** Lấy code từ Kho về máy mình để sửa.
- **체크인 (Check-in) / 커밋 (Commit):** Lưu code mình vừa sửa vào máy mình (Local) hoặc đưa lên Kho.
- **동기화 (Update):** Lấy code mới nhất của người khác trên Kho về máy mình để đồng bộ.

---

Các bullet của **버전 관리 용어 (Thuật ngữ Version Control)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **버전 관리 용어 (Thuật ngữ Version Control)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **116 & 117: 형상 관리 도구 (SVN vs Git)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 116 & 117: 형상 관리 도구 (SVN vs Git)

Ở bước 40/101, **116 & 117: 형상 관리 도구 (SVN vs Git)** xuất hiện như phần tiếp nối của **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **116 & 117: 형상 관리 도구 (SVN vs Git)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **Subversion (SVN)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **Subversion (SVN)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### Subversion (SVN)

Bây giờ ta đi vào nội dung của **Subversion (SVN)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “Subversion (SVN)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 클라이언트/서버 구조 (Cấu trúc Client/Server tập trung).
- **Trunk:** Thư mục chính (Main).
- **Branches:** Th nhánh để làm tính năng riêng.
- **Revision:** Mỗi lần Commit thành công, số Revision tăng lên 1.

Các bullet của **Subversion (SVN)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **Subversion (SVN)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **Git (깃)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **Git (깃)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### Git (깃)

Phần nguồn của **Git (깃)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “Git (깃)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 분산 저장소 방식 (Lưu trữ phân tán). Phát minh bởi Linus Torvalds.
- **Snapshot (스냅샷):** Lưu lại toàn bộ trạng thái file tại một thời điểm rất nhanh chóng.
- **로컬 저장소 (Local Repo) vs 원격 저장소 (Remote Repo):** Internet đứt vẫn làm việc bình thường ở Local.

- 💡 **Mẹo ghi nhớ (Mnemonics):** SVN = Trunk (Thân cây), Revision tăng dần. Git = Snapshot, Phân tán (Phân tán (Distributed)).

---

Với **Git (깃)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **Git (깃)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **116 & 117: 형상 관리 도구 (SVN vs Git)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)

Sau khi đã đặt nền bằng **116 & 117: 형상 관리 도구 (SVN vs Git)**, ta chuyển sang **12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)**. Đây là mắt xích 41/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **패키징 (Packaging)**, **설치 매뉴얼 (Installation Manual)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **패키징 (Packaging)**: 모듈별 실행 파일들을 묶어 배포용 설치 파일을 만드는 것. 사용자 중심으로 진행하며 보안(암호화, DRM 연동) 고려.
* **설치 매뉴얼 (Installation Manual)**: 사용자를 기준으로 작성. 기본 사항, 소프트웨어 개요, 설치 파일, 프로그램 삭제 등 포함.
* **VI (Vietnamese) (Tiếng Việt):**
  * Packaging: Đóng gói các file thực thi thành file cài đặt (hướng đến người dùng cuối).
  * Manual: Tài liệu hướng dẫn cài đặt viết cho người dùng, bao gồm cách cài và gỡ.
* **Example**: `.exe` 설치 파일을 만들고, "다음, 다음, 완료"를 설명하는 설명서를 작성하는 과정입니다.

Ta có thể khép mục **12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **37. 소프트웨어 패키징 고려사항 추가 (Packaging Considerations)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 37. 소프트웨어 패키징 고려사항 추가 (Packaging Considerations)

Từ **12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)**, ta đã có điểm tựa để bước vào **37. 소프트웨어 패키징 고려사항 추가 (Packaging Considerations)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 42/101 trước khi đi vào chi tiết.

Để đọc **37. 소프트웨어 패키징 고려사항 추가 (Packaging Considerations)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “37. 소프트웨어 패키징 고려사항 추가 (Packaging Considerations)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 사용자의 시스템 최소 환경(OS, CPU, 메모리) 정의.
* UI(시각적 자료) 매뉴얼과 일치.
* 하드웨어와 함께 관리되도록 Managed Service 형태로 제공 고려.
* 제품 종류에 적합한 암호화 알고리즘 및 DRM 연동 고려.
* **VI (Vietnamese) (Tiếng Việt):** Các lưu ý khi đóng gói phần mềm: Yêu cầu hệ thống tối thiểu, Giao diện (UI) khớp với hướng dẫn, Quản lý dịch vụ, Mã hóa/DRM.

Điểm chốt của **37. 소프트웨어 패키징 고려사항 추가 (Packaging Considerations)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **39. DRM 패키징 과정 상세 (DRM Packaging Process)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 39. DRM 패키징 과정 상세 (DRM Packaging Process)

Ở bước 43/101, **39. DRM 패키징 과정 상세 (DRM Packaging Process)** xuất hiện như phần tiếp nối của **37. 소프트웨어 패키징 고려사항 추가 (Packaging Considerations)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **39. DRM 패키징 과정 상세 (DRM Packaging Process)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “39. DRM 패키징 과정 상세 (DRM Packaging Process)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 디지털 콘텐츠 배포 시, 아날로그는 디지털로 변환 후 패키저가 패키징.
* 용량이 작으면 실시간 패키징, 크면 미리 패키징 후 배포.
* 암호화된 저작권자 전자서명 포함, 라이선스는 클리어링 하우스에 등록.
* **VI (Vietnamese) (Tiếng Việt):** Quy trình đóng gói DRM. Nội dung nhỏ thì đóng gói realtime, lớn thì đóng gói trước. Giấy phép lưu tại Clearing House.

Như vậy, **39. DRM 패키징 과정 상세 (DRM Packaging Process)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **099: 소프트웨어 패키징 (Software Packaging)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 099: 소프트웨어 패키징 (Software Packaging)

Sau khi đã đặt nền bằng **39. DRM 패키징 과정 상세 (DRM Packaging Process)**, ta chuyển sang **099: 소프트웨어 패키징 (Software Packaging)**. Đây là mắt xích 44/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **099: 소프트웨어 패키징 (Software Packaging)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “099: 소프트웨어 패키징 (Software Packaging)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 실행 파일들을 묶어 배포용 설치 파일을 만드는 과정. (Gom tất cả file thực thi, file hình, file cấu hình thành 1 file cài đặt (Setup.exe) để tung ra thị trường).
- **Nguyên tắc:**
  - **사용자 중심 (Hướng tới người dùng):** Người dùng cài đặt dễ dàng, không cần biết code.
  - Cần phải 모듈화 (Module hóa) để dễ bảo trì, và tích hợp 보안 (Bảo mật / DRM).

Ta có thể khép mục **099: 소프트웨어 패키징 (Software Packaging)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)

Từ **099: 소프트웨어 패키징 (Software Packaging)**, ta đã có điểm tựa để bước vào **100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 45/101 trước khi đi vào chi tiết.

Để đọc **100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **패키징 시 고려사항** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 패키징 시 고려사항

Các ý ngay dưới **패키징 시 고려사항** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “패키징 시 고려사항” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 최소 환경 정의 (OS/CPU/RAM). (Phải ghi rõ cấu hình tối thiểu để chạy app).
- UI와 매뉴얼 일치. (Hình ảnh UI trong thực tế và trong tài liệu phải giống nhau).
- 보안 및 암호화, DRM 연동 고려. (Bảo mật, mã hóa, tích hợp chống copy).

Các bullet của **패키징 시 고려사항** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **패키징 시 고려사항** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **소프트웨어 패키징 순서 (Trình tự đóng gói)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **소프트웨어 패키징 순서 (Trình tự đóng gói)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 소프트웨어 패키징 순서 (Trình tự đóng gói)

Bây giờ ta đi vào nội dung của **소프트웨어 패키징 순서 (Trình tự đóng gói)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

1. **기능 식별 (Xác định chức năng)**
2. **모듈화 (Module hóa)**
3. **빌드 진행 (Build - Dịch ra file chạy)**
4. **사용자 환경 분석 (Phân tích môi trường người dùng - OS/CPU)**
5. **패키징 및 적용 시험 (Đóng gói & Test thử)**
6. **패키징 변경 개선 (Sửa lỗi nếu có)**
7. **배포 (Deployment - Phát hành)**

- 💡 **Mẹo ghi nhớ (Mnemonics):** Nhận-Mô-Build-Môi-Gói-Cải-Phân (Nhận diện - Module - Build - Môi trường - Đóng gói - Cải tiến - Phân phối).

---

Các bullet của **소프트웨어 패키징 순서 (Trình tự đóng gói)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **소프트웨어 패키징 순서 (Trình tự đóng gói)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **10. 빌드 자동화 도구 (Build Automation Tools)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 10. 빌드 자동화 도구 (Build Automation Tools)

Ở bước 46/101, **10. 빌드 자동화 도구 (Build Automation Tools)** xuất hiện như phần tiếp nối của **100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **10. 빌드 자동화 도구 (Build Automation Tools)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **Ant**, **Maven**, **Jenkins**, **Gradle** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “10. 빌드 자동화 도구 (Build Automation Tools)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **Ant**: 아파치 소프트웨어 재단에서 개발.
* **Maven**: Ant의 대안.
* **Jenkins**: JAVA 기반의 오픈 소스 빌드 자동화 도구.
* **Gradle**: Groovy 기반의 오픈 소스 빌드 자동화 도구.
* **VI (Vietnamese) (Tiếng Việt):** Các công cụ tự động hóa quá trình build phần mềm (biên dịch, đóng gói).
* **Example**: 개발자가 코드를 수정하면 Jenkins가 자동으로 빌드와 테스트를 실행합니다.
* 💡 **Mẹo ghi nhớ**: AMJG (Ant, Maven, Jenkins, Gradle).

Như vậy, **10. 빌드 자동화 도구 (Build Automation Tools)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)

Sau khi đã đặt nền bằng **10. 빌드 자동화 도구 (Build Automation Tools)**, ta chuyển sang **36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)**. Đây là mắt xích 47/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **IDE**, **기능**, **빌드 도구** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **IDE**: 코딩, 디버그, 컴파일, 배포 등 모든 작업을 하나의 프로그램에서 처리.
  * **기능**: 코딩(Coding), 컴파일(Compile), 디버깅(Debugging), 배포(Deployment).
* **빌드 도구**: 소스 코드를 실행 가능한 제품 소프트웨어로 변환(Ant, Maven, Gradle).
* **VI (Vietnamese) (Tiếng Việt):** Môi trường phát triển tích hợp (IDE - như Eclipse, VS Code). Chức năng: Code, Dịch, Gỡ lỗi, Triển khai.

Ta có thể khép mục **36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **41. 빌드 자동화 도구 심화: Jenkins vs Gradle**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 41. 빌드 자동화 도구 심화: Jenkins vs Gradle

Từ **36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)**, ta đã có điểm tựa để bước vào **41. 빌드 자동화 도구 심화: Jenkins vs Gradle**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 48/101 trước khi đi vào chi tiết.

Để đọc **41. 빌드 자동화 도구 심화: Jenkins vs Gradle** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **Jenkins**, **Gradle** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “41. 빌드 자동화 도구 심화: Jenkins vs Gradle” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **Jenkins**: JAVA 기반 오픈 소스. 친숙한 Web GUI 제공. 분산 빌드/테스트 가능.
* **Gradle**: Groovy 기반 오픈 소스. 안드로이드 앱 개발 환경에서 주로 사용. DSL을 스크립트 언어로 사용하며 태스크(Task) 단위로 실행. 빌드 캐시(Build Cache)로 속도 향상.
* **VI (Vietnamese) (Tiếng Việt):** Jenkins (dựa trên Java, có Web GUI dễ dùng) và Gradle (dựa trên Groovy, dùng nhiều trong Android, tăng tốc bằng Build Cache).
* 💡 **Mẹo ghi nhớ**: Jenkins = Java, Gradle = Groovy (Android).

Điểm chốt của **41. 빌드 자동화 도구 심화: Jenkins vs Gradle** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)

Ở bước 49/101, **118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)** xuất hiện như phần tiếp nối của **41. 빌드 자동화 도구 심화: Jenkins vs Gradle**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 소스 코드를 실행 파일로 만드는 과정과 배포를 자동화. (Tự động hóa việc dịch code, test và đóng gói phát hành - CI/CD).
- **Jenkins:** Viết bằng Java, chạy trên web (Web GUI). Điểm mạnh là test phân tán trên nhiều máy.
- **Gradle:** Viết bằng Groovy (Ngôn ngữ kịch bản), dùng **DSL**. Điểm mạnh là có **빌드 캐시 (Build Cache)** giúp build lại cực nhanh, thường dùng làm chuẩn cho Android.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Jenkins = Java, Web GUI, Phân tán. Gradle = Groovy, DSL, Cache, Android.

---

Như vậy, **118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **11. DRM (디지털 저작권 관리, Digital Rights Management)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 11. DRM (디지털 저작권 관리, Digital Rights Management)

Sau khi đã đặt nền bằng **118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)**, ta chuyển sang **11. DRM (디지털 저작권 관리, Digital Rights Management)**. Đây là mắt xích 50/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **11. DRM (디지털 저작권 관리, Digital Rights Management)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **구성 요소 (Components)**, **기술 요소 (Technologies)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “11. DRM (디지털 저작권 관리, Digital Rights Management)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **구성 요소 (Components)**: 클리어링 하우스 (Clearing House - 권한/결제 관리), 콘텐츠 제공자 (Contents Provider), 패키저 (Packager - 암호화), 콘텐츠 분배자 (Distributor), DRM 컨트롤러 (Controller - 이용 권한 통제).
* **기술 요소 (Technologies)**: 암호화 및 키 관리, 식별체계 표현, 라이선스 발급, 정책 관리, 크랙 방지.
* **VI (Vietnamese) (Tiếng Việt):** Quản lý bản quyền kỹ thuật số. Clearing House xử lý thanh toán/cấp phép. Packager mã hóa nội dung.
* **Example**: 넷플릭스 영상이 녹화가 안 되거나 불법 복제가 안 되는 것이 DRM 기술 덕분입니다.
* 💡 **Mẹo ghi nhớ**: Clearing House = Ngân hàng/Trung tâm kiểm duyệt. Packager = Người đóng gói/Mã hóa.

Ta có thể khép mục **11. DRM (디지털 저작권 관리, Digital Rights Management)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **100-2 ~ 104: 저작권 및 DRM (Copyright & Digital Rights Management)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 100-2 ~ 104: 저작권 및 DRM (Copyright & Digital Rights Management)

Từ **11. DRM (디지털 저작권 관리, Digital Rights Management)**, ta đã có điểm tựa để bước vào **100-2 ~ 104: 저작권 및 DRM (Copyright & Digital Rights Management)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 51/101 trước khi đi vào chi tiết.

Để đọc **100-2 ~ 104: 저작권 및 DRM (Copyright & Digital Rights Management)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **저작권 (Copyright)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 저작권 (Copyright)

Các ý ngay dưới **저작권 (Copyright)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “저작권 (Copyright)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 창작자가 가지는 **배타적 독점적 권리**. (Quyền độc quyền của tác giả). Phần mềm rất dễ bị copy (`Ctrl+C / Ctrl+V`) nên phải có DRM để bảo vệ.

Các bullet của **저작권 (Copyright)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **저작권 (Copyright)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **DRM의 핵심 구성 요소 (Thành phần chính của DRM)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **DRM의 핵심 구성 요소 (Thành phần chính của DRM)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### DRM의 핵심 구성 요소 (Thành phần chính của DRM)

Bây giờ ta đi vào nội dung của **DRM의 핵심 구성 요소 (Thành phần chính của DRM)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “DRM의 핵심 구성 요소 (Thành phần chính của DRM)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **패키저 (Packager):** 콘텐츠 암호화. (Người/Máy đóng gói và khóa file lại).
  - *실시간 패키징:* File nhỏ (Nhạc, ảnh) -> Khách bấm mua mới đóng gói.
  - *사전 패키징:* File to (Phim) -> Đóng gói sẵn trước khi bán.
- **클리어링 하우스 (Clearing House):** 권한, 라이선스, 결제 관리. (Trạm thu phí: Xác thực bạn đã trả tiền chưa, cấp License cho bạn mở file. Quản lý cả tính tiền theo dung lượng/thời gian - 종량제).
- **콘텐츠 분배자 (Distributor):** Nơi bán/phân phối (App Store).
- **DRM 컨트롤러 (Controller):** Phần mềm trên máy khách hàng kiểm soát việc mở file.
- **보안 컨테이너 (Security Container):** Hộp an toàn chứa file gốc để vận chuyển.

Các bullet của **DRM의 핵심 구성 요소 (Thành phần chính của DRM)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **DRM의 핵심 구성 요소 (Thành phần chính của DRM)**, đừng bắt đầu lại từ số không. **DRM 기술 요소 (Kỹ thuật dùng trong DRM)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **DRM 기술 요소 (Kỹ thuật dùng trong DRM)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### DRM 기술 요소 (Kỹ thuật dùng trong DRM)

Phần nguồn của **DRM 기술 요소 (Kỹ thuật dùng trong DRM)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “DRM 기술 요소 (Kỹ thuật dùng trong DRM)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **암호화 (Encryption):** Mã hóa file.
- **키 관리 (Key Management):** Quản lý khóa để mở mã hóa.
- **식별 기술 (Identification):** Gắn mã định danh (DOI, URI) để biết file nào là file nào.
- **저작권 표현 (Right Expression):** Ghi rõ quyền lợi (Vd: XrML - Chỉ cho xem, cấm in).
- **크랙 방지 (Tamper Resistance):** Chống bẻ khóa, chống hack.
- **인증 (Authentication):** Xác minh danh tính người mua.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Packager (Gói hàng + Khóa), Clearing House (Thu tiền + Đưa chìa).

---

Các bullet của **DRM 기술 요소 (Kỹ thuật dùng trong DRM)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **DRM 기술 요소 (Kỹ thuật dùng trong DRM)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **100-2 ~ 104: 저작권 및 DRM (Copyright & Digital Rights Management)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **15. 화이트박스 vs 블랙박스 테스트 (White-box vs Black-box Testing)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 15. 화이트박스 vs 블랙박스 테스트 (White-box vs Black-box Testing)

Ở bước 52/101, **15. 화이트박스 vs 블랙박스 테스트 (White-box vs Black-box Testing)** xuất hiện như phần tiếp nối của **100-2 ~ 104: 저작권 및 DRM (Copyright & Digital Rights Management)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **15. 화이트박스 vs 블랙박스 테스트 (White-box vs Black-box Testing)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **화이트박스 테스트**, **종류**, **블랙박스 테스트**, **종류** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “15. 화이트박스 vs 블랙박스 테스트 (White-box vs Black-box Testing)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **화이트박스 테스트**: 원시 코드를 오픈시킨 상태에서 논리적 경로(제어 구조)를 테스트.
  * **종류**: 기초 경로 검사 (Base Path), 제어 구조 검사 (조건, 루프, 데이터 흐름).
* **블랙박스 테스트**: 기능이 제대로 작동하는지 외부에서 테스트 (내부 구조 안 봄).
  * **종류**: 동치 분할 (Equivalence Partitioning), 경계값 분석 (Boundary Value), 원인-효과 그래프 (Cause-Effect), 오류 예측 (Error Guessing), 비교 검사 (Comparison).
* **VI (Vietnamese) (Tiếng Việt):**
  * White-box: Nhìn thấy code bên trong (kiểm tra đường dẫn, vòng lặp).
  * Black-box: Không nhìn thấy code, chỉ kiểm tra đầu vào/đầu ra (kiểm tra tính năng).
* **Example**: 화이트박스는 코드의 `if-else` 모든 경로를 실행해보는 것이고, 블랙박스는 로그인 창에 ID/PW를 넣어보는 것입니다.
* 💡 **Mẹo ghi nhớ**: White = Nhìn xuyên thấu (Code). Black = Hộp đen không thấy ruột (Chức năng).

Như vậy, **15. 화이트박스 vs 블랙박스 테스트 (White-box vs Black-box Testing)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **16. 소프트웨어 테스트 단계 (Software Testing Phases)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 16. 소프트웨어 테스트 단계 (Software Testing Phases)

Sau khi đã đặt nền bằng **15. 화이트박스 vs 블랙박스 테스트 (White-box vs Black-box Testing)**, ta chuyển sang **16. 소프트웨어 테스트 단계 (Software Testing Phases)**. Đây là mắt xích 53/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **16. 소프트웨어 테스트 단계 (Software Testing Phases)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **단위 테스트 (Unit Test)**, **통합 테스트 (Integration Test)**, **인수 테스트 (Acceptance Test)**, **알파 테스트** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “16. 소프트웨어 테스트 단계 (Software Testing Phases)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **단위 테스트 (Unit Test)**: 코딩 직후 최소 단위인 모듈/컴포넌트 테스트. (알고리즘 오류, 탈출구 없는 반복문 등 발견).
* **통합 테스트 (Integration Test)**:
  * 하향식 (Top-down): 상위에서 하위로 (스텁/Stub 사용).
  * 상향식 (Bottom-up): 하위에서 상위로 (드라이버/Driver 사용).
* **인수 테스트 (Acceptance Test)**: 사용자가 시스템을 수락하기 전 수행.
  * **알파 테스트**: 개발자 앞에서 사용자가 수행.
  * **베타 테스트 (Field Testing)**: 최종 사용자가 실제 환경에서 여러 사용자 앞에서 수행.
* **VI (Vietnamese) (Tiếng Việt):**
  * Unit Test: Kiểm thử từng module nhỏ (tìm lỗi thuật toán, lặp vô hạn).
  * Integration Test: Kiểm thử tích hợp. Top-down (từ trên xuống), Bottom-up (từ dưới lên).
  * Acceptance Test: Kiểm thử chấp nhận. Alpha (cùng dev), Beta (không có dev, real-world).
* **Example**: 게임 개발 후 회사 내부에서 해보는 것이 알파 테스트, 유저들에게 먼저 공개하는 것이 오픈 베타 테스트입니다.
* 💡 **Mẹo ghi nhớ**: Alpha = có người tạo ra (Dev) giám sát. Beta = thả ra tự nhiên cho User.

Ta có thể khép mục **16. 소프트웨어 테스트 단계 (Software Testing Phases)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)

Từ **16. 소프트웨어 테스트 단계 (Software Testing Phases)**, ta đã có điểm tựa để bước vào **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 54/101 trước khi đi vào chi tiết.

Để đọc **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **테스트 오라클 (Test Oracle)**, **테스트 드라이버 (Test Driver)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **테스트 오라클 (Test Oracle)**: 테스트 결과가 참인지 판단하기 위해 사전에 정의된 참 값을 대입하여 비교. (참, 샘플링, 추정, 일관성 검사 오라클).
* **테스트 드라이버 (Test Driver)**: (상향식 테스트에서) 하위 모듈을 호출하고 매개 변수를 전달하여 결과를 도출하는 도구. (가짜 메인 프로그램).
* **VI (Vietnamese) (Tiếng Việt):**
  * Test Oracle: Cơ chế/Nguồn chân lý để xác định kết quả đúng hay sai.
  * Test Driver: Chương trình giả lập gọi module con (dùng trong Bottom-up).
* **Example**: 테스트 오라클은 정답지 역할을 합니다.
* 💡 **Mẹo ghi nhớ**: Oracle = Nhà tiên tri/Chân lý. Driver = Người lái xe (Gọi cấp dưới).

Điểm chốt của **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **20. 하향식 통합 테스트와 테스트 스텁 (Top-down Integration Test & Test Stub)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 20. 하향식 통합 테스트와 테스트 스텁 (Top-down Integration Test & Test Stub)

Ở bước 55/101, **20. 하향식 통합 테스트와 테스트 스텁 (Top-down Integration Test & Test Stub)** xuất hiện như phần tiếp nối của **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **20. 하향식 통합 테스트와 테스트 스텁 (Top-down Integration Test & Test Stub)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **테스트 스텁 (Test Stub)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “20. 하향식 통합 테스트와 테스트 스텁 (Top-down Integration Test & Test Stub)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **테스트 스텁 (Test Stub)**: 상향식에서 드라이버를 쓰듯, 하향식 통합 테스트에서는 '스텁(Stub)'이라는 가짜 하위 모듈을 사용.
* 의존성 배제 및 중복성 최소화.
* 일시적으로 필요한 조건만을 가지고 있는 시험용 모듈.
* **VI (Vietnamese) (Tiếng Việt):** Test Stub là module giả lập cấp dưới, dùng trong kiểm thử tích hợp từ trên xuống (Top-down).
* **Example**: 로그인 기능을 먼저 테스트하기 위해, DB 연결 모듈 대신 무조건 "성공"을 반환하는 스텁을 만듭니다.
* 💡 **Mẹo ghi nhớ**: Top-down dùng Stub (T-S), Bottom-up dùng Driver (B-D).

Như vậy, **20. 하향식 통합 테스트와 테스트 스텁 (Top-down Integration Test & Test Stub)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **35. 테스트 케이스 (Test Case)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 35. 테스트 케이스 (Test Case)

Sau khi đã đặt nền bằng **20. 하향식 통합 테스트와 테스트 스텁 (Top-down Integration Test & Test Stub)**, ta chuyển sang **35. 테스트 케이스 (Test Case)**. Đây là mắt xích 56/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **35. 테스트 케이스 (Test Case)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **구성 요소 (ISO/IEC/IEEE 29119-3)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “35. 테스트 케이스 (Test Case)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 사용자의 요구사항을 정확하게 준수했는지 확인하기 위해 설계된 테스트 항목에 대한 명세서.
* **구성 요소 (ISO/IEC/IEEE 29119-3)**:
  * 식별자, 테스트 항목, 입력 명세(Input), 출력 명세(Output/예상 결과), 환경 설정, 특수 절차 요구, 의존성 기술.
* **VI (Vietnamese) (Tiếng Việt):** Kịch bản kiểm thử (Test Case). Bao gồm: ID, Môi trường, Đầu vào, Đầu ra mong đợi.
* **Example**: 로그인 기능을 위해 "ID: admin, PW: 1234를 넣었을 때 관리자 페이지로 넘어가는가?"를 문서화한 것입니다.

Ta có thể khép mục **35. 테스트 케이스 (Test Case)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)

Từ **35. 테스트 케이스 (Test Case)**, ta đã có điểm tựa để bước vào **42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 57/101 trước khi đi vào chi tiết.

Để đọc **42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **결함 집중 (Defect Clustering) & 파레토 법칙**, **살충제 패러독스 (Pesticide Paradox)**, **오류-부재의 궤변 (Absence of Errors Fallacy)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **결함 집중 (Defect Clustering) & 파레토 법칙**: 오류의 80%는 20%의 모듈에 집중됨.
* **살충제 패러독스 (Pesticide Paradox)**: 동일한 테스트 케이스로 반복 테스트하면 더 이상 새로운 결함을 찾을 수 없음. 주기적인 테스트 케이스 개선 필요.
* **오류-부재의 궤변 (Absence of Errors Fallacy)**: 결함이 0이더라도 사용자의 요구사항을 만족시키지 못하면 품질이 높다고 할 수 없음.
* **확인 (Validation)** vs **검증 (Verification)**:
  * 확인(Validation): **사용자** 입장에서 요구사항에 맞는지 테스트.
  * 검증(Verification): **개발자** 입장에서 명세서(스펙)에 맞는지 테스트.
* **VI (Vietnamese) (Tiếng Việt):** Nguyên lý kiểm thử:
  * Pesticide Paradox (Nghịch lý thuốc trừ sâu): Dùng mãi 1 kịch bản thì không bắt được lỗi mới.
  * Absence of Errors Fallacy: Không có lỗi không có nghĩa là phần mềm tốt nếu sai yêu cầu của khách hàng.
  * Validation: Đúng yêu cầu người dùng (Build the right product). Verification: Làm đúng kỹ thuật/tài liệu (Build the product right).
* **Example**: 로그인 버튼을 예쁘게 만들었지만(결함 없음), 고객이 원한 건 지문 인식 로그인이라면 이는 '오류-부재의 궤변'입니다.

Điểm chốt của **42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **43. 테스트 분류 방식 (Test Classification)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 43. 테스트 분류 방식 (Test Classification)

Ở bước 58/101, **43. 테스트 분류 방식 (Test Classification)** xuất hiện như phần tiếp nối của **42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **43. 테스트 분류 방식 (Test Classification)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **실행 여부에 따른 분류**, **정적 테스트 (Static)**, **동적 테스트 (Dynamic)**, **기반(Bases)에 따른 분류** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “43. 테스트 분류 방식 (Test Classification)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **실행 여부에 따른 분류**:
  * **정적 테스트 (Static)**: 프로그램 실행 없이 분석. (워크스루, 인스펙션, 코드 검사).
  * **동적 테스트 (Dynamic)**: 프로그램을 직접 실행하며 테스트. (블랙박스, 화이트박스).
* **기반(Bases)에 따른 분류**:
  * **명세 기반 (Specification)**: 요구사항 명세서를 빠짐없이 테스트. (동등 분할, 경계값).
  * **구조 기반 (Structure)**: 내부 논리 흐름(코드)에 따라 테스트. (구문, 결정, 조건 기반).
  * **경험 기반 (Experience)**: 테스터의 경험 직관에 의존. (에러 추정, 탐색적 테스팅).
* **목적에 따른 분류**:
  * **회복 (Recovery)**: 일부러 실패하게 한 후 복구되는지 확인.
  * **안전 (Security)**: 불법 침입으로부터 보호 확인.
  * **강도 (Stress)**: 과부하(Overload) 상태에서 정상 동작하는지.
  * **성능 (Performance)**: 응답 시간, 처리량 등 효율성 진단.
  * **회귀 (Regression)**: 코드를 수정한 후 **새로운 결함**이 발생하지 않았는지 확인.
  * **병행 (Parallel)**: 변경된 시스템과 기존 시스템에 동일 데이터 입력 후 결과 비교.
* **VI (Vietnamese) (Tiếng Việt):** Phân loại kiểm thử.
  * Theo thực thi: Tĩnh (không chạy code - Review) và Động (chạy code).
  * Theo cơ sở: Dựa trên Đặc tả (Spec), Cấu trúc (Code), Kinh nghiệm.
  * Theo mục đích: Phục hồi (Recovery), Áp lực (Stress - quá tải), Hồi quy (Regression - test lại sau khi sửa code), Song song (Parallel).
* **Example**: 버그를 고치고 나서 다른 곳에 문제가 안 생겼는지 다시 테스트하는 것이 '회귀 테스트'입니다. (Kiểm tra lại sau khi sửa lỗi là Regression Test).

Như vậy, **43. 테스트 분류 방식 (Test Classification)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)

Sau khi đã đặt nền bằng **43. 테스트 분류 방식 (Test Classification)**, ta chuyển sang **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)**. Đây là mắt xích 59/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **문장(구문) 검증 기준 (Statement Coverage)**, **결정/분기 검증 기준 (Decision/Branch Coverage)**, **조건 검증 기준 (Condition Coverage)**, **분기/조건 기준 (Branch/Condition Coverage)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **문장(구문) 검증 기준 (Statement Coverage)**: 소스 코드의 **모든 구문**이 한 번 이상 수행되도록 설계.
* **결정/분기 검증 기준 (Decision/Branch Coverage)**: 모든 조건문에 대해 조건이 **True인 경우와 False인 경우**가 한 번 이상 수행되도록 설계.
* **조건 검증 기준 (Condition Coverage)**: 조건문에 포함된 **개별 조건식**의 결과가 T/F 한 번 이상 수행되도록 설계.
* **분기/조건 기준 (Branch/Condition Coverage)**: 위 두 가지를 모두 만족하는 설계.
* **VI (Vietnamese) (Tiếng Việt):** Các tiêu chí độ phủ (Coverage) trong kiểm thử hộp trắng: Bao phủ cú pháp (Statement), Bao phủ nhánh/quyết định (Branch - lệnh IF chạy cả T/F), Bao phủ điều kiện (Condition - từng điều kiện nhỏ chạy cả T/F), Bao phủ nhánh/điều kiện.
* 💡 **Mẹo ghi nhớ**: Statement = Dòng code. Branch = Ngã rẽ (IF). Condition = Điều kiện nhỏ trong IF.

Ta có thể khép mục **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계

Từ **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)**, ta đã có điểm tựa để bước vào **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 60/101 trước khi đi vào chi tiết.

Để đọc **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **하향식 (Top-down)**, **상향식 (Bottom-up)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

개발 단계와 테스트 단계를 짝지어 놓은 모델.
1. **단위 테스트 (Unit Test)** - *구현(Code)* 단계와 짝. 모듈/컴포넌트 초점 (주로 구조 기반/화이트박스).
2. **통합 테스트 (Integration Test)** - *설계(Design)* 단계와 짝. 모듈들을 결합하여 테스트.
   * **하향식 (Top-down)**: 스텁(Stub) 사용. 깊이/넓이 우선. 테스트 초기부터 시스템 구조 파악 가능.
   * **상향식 (Bottom-up)**: 드라이버(Driver)와 클러스터(Cluster) 사용.

---

- **Bandwidth (대역폭/전송률 - Băng thông):** Tốc độ truyền dữ liệu tối đa trong 1 giây (đơn vị bit/s hoặc byte/s). Băng thông càng lớn máy càng nhanh.
- **접근 속도 (Tốc độ tiếp cận Nhanh -> Chậm):** CPU 레지스터 -> Cache -> RAM(Main Memory) -> ROM -> 자기 코어 -> 자기 디스크 (HDD) -> 자기 테이프 (Tape).

Để không đọc **ROM (Read Only Memory - Bộ nhớ chỉ đọc)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### ROM (Read Only Memory - Bộ nhớ chỉ đọc)

Các ý ngay dưới **ROM (Read Only Memory - Bộ nhớ chỉ đọc)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “ROM (Read Only Memory - Bộ nhớ chỉ đọc)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 전원이 꺼져도 내용이 지워지지 않는 비휘발성 (Không bay hơi khi mất điện).
- 주로 기본 입·출력 시스템(BIOS), 자가 진단 프로그램(POST) 저장 (Thường chứa BIOS, POST).
- **ROM 종류 (Các loại ROM):**
  - Mask ROM: Nhà máy làm sẵn, không đổi được.
  - PROM: Ghi được **1번** (1 lần).
  - EPROM: 자외선 (Tia cực tím - UV) để xóa, ghi lại nhiều lần.
  - EEPROM (EAROM): 전기적인 방법 (Phương pháp điện - Electrical) để xóa và ghi. (Ví dụ: USB Flash Drive, SSD).

- **Vietnamese Explanation:** Cycle Time luôn dài hơn Access Time vì bộ nhớ cần thời gian phục hồi lại năng lượng sau khi đọc. ROM giữ lại dữ liệu khi mất điện, có nhiều loại từ cứng nhắc (Mask) đến linh hoạt (EEPROM - dùng điện để xóa).
- **Ví dụ (Example):** EEPROM chính là công nghệ đằng sau cái USB nhỏ xinh bạn hay dùng. EPROM thì giống cái bảng viết phấn, bôi đi bằng tia UV (giẻ lau) rồi viết lại. Mask ROM là bia đá khắc chữ sẵn.
- 💡 **Mẹo ghi nhớ (Mnemonics):** "E" đầu tiên = Erasable (Xóa được). Nhớ: EPROM = UV (Tia cực tím), EEPROM = Điện (Electonic). Cycle Time ≥ Access Time.

Với **ROM (Read Only Memory - Bộ nhớ chỉ đọc)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **ROM (Read Only Memory - Bộ nhớ chỉ đọc)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)

Ở bước 61/101, **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)** xuất hiện như phần tiếp nối của **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**Quy trình 5 bước (5 단계):**
1. **계획 및 제어 (Planning & Control):** Lập kế hoạch, mục tiêu, chi phí.
2. **분석 및 설계 (Analysis & Design):** Viết Kịch bản (Test Scenario) và Ca kiểm thử (**Test Case**).
3. **구현 및 실현 (Implementation & Execution):** Viết Thủ tục test (**Test Procedure** - Trình tự chạy các case) và Thực thi test.
4. **평가 (Evaluation):** Đánh giá kết quả xem đạt chưa.
5. **완료 (Completion):** Lưu trữ hồ sơ, bàn giao.

- **Vietnamese Explanation:** Test Case là danh sách các món ăn cần nấu (Ví dụ: Trứng rán). Test Procedure là công thức nấu (Bước 1 bật bếp, bước 2 đập trứng). Phải có món (Case) rồi mới ghi công thức (Procedure) được.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Kế hoạch -> Phân tích (Ra Test Case) -> Thực hiện (Ra Test Procedure) -> Đánh giá -> Hoàn thành. (Kế Phân Thực Đánh Hoàn (Kế hoạch - Phân tích - Thực hiện - Đánh giá - Hoàn thành)).

---

Như vậy, **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **105: 시각에 따른 테스트 (Verification vs Validation)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 105: 시각에 따른 테스트 (Verification vs Validation)

Sau khi đã đặt nền bằng **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)**, ta chuyển sang **105: 시각에 따른 테스트 (Verification vs Validation)**. Đây là mắt xích 62/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **105: 시각에 따른 테스트 (Verification vs Validation)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “105: 시각에 따른 테스트 (Verification vs Validation)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **검증 (Verification - Xác minh):** 개발자 시각 (Góc nhìn Dev). "Làm đúng thiết kế/mã code không?". (Are we building the product right?).
- **확인 (Validation - Thẩm định):** 사용자 시각 (Góc nhìn User). "Phần mềm này có đúng cái khách hàng cần không?". (Are we building the right product?).

- 💡 **Mẹo ghi nhớ (Mnemonics):** 검증 (Verification) = Code chuẩn chưa? (Dev). 확인 (Validation) = Khách ưng không? (User).

---

Ta có thể khép mục **105: 시각에 따른 테스트 (Verification vs Validation)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)

Từ **105: 시각에 따른 테스트 (Verification vs Validation)**, ta đã có điểm tựa để bước vào **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 63/101 trước khi đi vào chi tiết.

Để đọc **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **테스트의 기본 원리 (Nguyên lý cơ bản)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 테스트의 기본 원리 (Nguyên lý cơ bản)

Các ý ngay dưới **테스트의 기본 원리 (Nguyên lý cơ bản)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “테스트의 기본 원리 (Nguyên lý cơ bản)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **완벽한 테스트 불가능:** Không thể khẳng định 100% hết bug.
- **파레토 법칙 (Pareto):** 80% bug nằm ở 20% code cốt lõi. (Đám mây lỗi).
- **살충제 패러독스 (Pesticide Paradox):** Test hoài 1 kịch bản sẽ bị "nhờn", phải liên tục thay đổi bộ test.
- **정황 의존 (Context):** Tùy thuộc ngữ cảnh (Web, Game) mà test khác nhau.

Các bullet của **테스트의 기본 원리 (Nguyên lý cơ bản)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **테스트의 기본 원리 (Nguyên lý cơ bản)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **테스트 분류 (Phân loại Test)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **테스트 분류 (Phân loại Test)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 테스트 분류 (Phân loại Test)

Bây giờ ta đi vào nội dung của **테스트 분류 (Phân loại Test)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

1. **실행 여부 (Theo việc có chạy code không):**
   - **정적 테스트 (Static):** Không chạy code. Đọc, review tài liệu (Walkthrough, Inspection).
   - **동적 테스트 (Dynamic):** Chạy code. (White box, Black box).
2. **테스트 기반 (Theo căn cứ Test):**
   - **명세 기반 (Specification):** Dựa vào tài liệu yêu cầu.
   - **구조 기반 (Structure):** Dựa vào luồng logic của code.
   - **경험 기반 (Experience):** Dựa vào kinh nghiệm tester (Đoán lỗi).
3. **목적 (Theo mục đích):**
   - **강도 (Stress):** Ép tải (Dồn dập bắt nó sập).
   - **회귀 (Regression):** Sửa code xong test lại xem có hỏng chỗ cũ không.
   - **회복 (Recovery):** Giả vờ ngắt điện xem app phục hồi data được không.
   - **병행 (Parallel):** Chạy app cũ và app mới cùng lúc để so kết quả.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Inspection (Khám nghiệm) = Tĩnh (Static). Regression (Hồi quy) = Sửa xong test lại.

---

Với **테스트 분류 (Phân loại Test)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **테스트 분류 (Phân loại Test)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **127 ~ 129: 화이트박스 테스트 (White Box Test)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 127 ~ 129: 화이트박스 테스트 (White Box Test)

Ở bước 64/101, **127 ~ 129: 화이트박스 테스트 (White Box Test)** xuất hiện như phần tiếp nối của **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **127 ~ 129: 화이트박스 테스트 (White Box Test)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “127 ~ 129: 화이트박스 테스트 (White Box Test)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 내부 로직과 제어 구조를 직접 관찰. (Test dựa trên mã nguồn (Source Code). Nhìn thấu bên trong).
- **종류 (Các kỹ thuật):** 기초 경로 (Đường dẫn cơ bản), 조건 (Điều kiện), 루프 (Vòng lặp), 데이터 흐름 (Luồng dữ liệu).
- **검증 기준 (Coverage - Mức độ bao phủ):**
  - **문장 검증 (Statement):** Mọi dòng code phải chạy qua 1 lần.
  - **분기/결정 검증 (Branch/Decision):** Mọi nhánh lệnh (If True / False) phải chạy qua 1 lần.
  - **조건 검증 (Condition):** Mọi biểu thức điều kiện con bên trong If phải kiểm tra T/F.

- 💡 **Mẹo ghi nhớ (Mnemonics):** White Box = Code (Câu lệnh, Rẽ nhánh, Vòng lặp). Do Dev tự làm.

---

Như vậy, **127 ~ 129: 화이트박스 테스트 (White Box Test)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **130 & 131: 블랙박스 테스트 (Black Box Test)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 130 & 131: 블랙박스 테스트 (Black Box Test)

Sau khi đã đặt nền bằng **127 ~ 129: 화이트박스 테스트 (White Box Test)**, ta chuyển sang **130 & 131: 블랙박스 테스트 (Black Box Test)**. Đây là mắt xích 65/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **130 & 131: 블랙박스 테스트 (Black Box Test)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “130 & 131: 블랙박스 테스트 (Black Box Test)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 명세를 기초로 기능 테스트. 내부 구조 무시. (Dựa vào chức năng UI, không thèm nhìn code).
- **종류 (Các kỹ thuật):**
  - **동치 분할 (Equivalence Partitioning):** Chia vùng tương đương (Nhập đại 1 số đại diện).
  - **경계값 분석 (Boundary Value):** Test quanh cái mép (Max, Min, +1, -1). Lỗi hay nằm ở đây.
  - **원인-효과 그래프 (Cause-Effect):** Vẽ biểu đồ nhân quả.
  - **오류 예측 (Error Guessing):** Dựa vào kinh nghiệm (Kinh nghiệm Tester).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Black Box = UI, Chức năng. Các kỹ thuật thường chia theo vùng (Partition) và ranh giới (Boundary).

---

Ta có thể khép mục **130 & 131: 블랙박스 테스트 (Black Box Test)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)

Từ **130 & 131: 블랙박스 테스트 (Black Box Test)**, ta đã có điểm tựa để bước vào **132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 66/101 trước khi đi vào chi tiết.

Để đọc **132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Thực hiện theo mô hình V (V-Model), từ nhỏ đến lớn:

1. **단위 테스트 (Unit Test):** Test từng Module con. Thường dùng White Box.
2. **통합 테스트 (Integration Test):** Ghép các module lại. (Có thể test kiểu Big Bang - Gom 1 cục, hoặc dần dần từ trên xuống, từ dưới lên). Tìm lỗi giao tiếp (Interface).
3. **시스템 테스트 (System Test):** Test toàn bộ hệ thống trong môi trường giống thực tế nhất. Đánh giá tính năng + hiệu năng (Bảo mật, tốc độ).
4. **인수 테스트 (Acceptance Test):** Khách hàng test để nghiệm thu.
   - **알파 (Alpha):** Khách hàng test tại văn phòng dev (có dev đứng xem).
   - **베타 (Beta):** Khách hàng tự test ở nhà (Giống Game Open Beta).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Đơn vị (Unit) -> Tích hợp (Integration) -> Hệ thống (System) -> Nghiệm thu (Acceptance). Alpha = Nội bộ, Beta = Ở nhà.

# 136-1. 통합 테스트 (Integration Test - Kiểm thử tích hợp)

Phần **136-1. 통합 테스트 (Integration Test - Kiểm thử tích hợp)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 개념 (Khái niệm):** 단위 테스트가 끝난 모듈을 통합하는 과정에서 발생하는 오류 및 결함을 찾는 테스트 기법.
*(Kiểm thử tích hợp là quá trình kết hợp các module đã qua kiểm thử đơn vị lại với nhau để tìm lỗi và khiếm khuyết phát sinh trong quá trình tương tác.)*

**[2] 핵심 키워드 (Từ khóa chính):**
- 모듈 통합 (Module Integration - Tích hợp module)
- 인터페이스 오류 (Interface Error - Lỗi giao diện/kết nối)
- 비점진적 (Big Bang - Không tăng dần) vs 점진적 (Incremental - Tăng dần)

**[3] 특징 (Đặc điểm):**
- **비점진적 통합 방식 (Non-incremental / Big Bang):**
  - 모든 모듈을 한꺼번에 결합해서 테스트함. *(Gộp tất cả module lại và kiểm thử cùng một lúc.)*
  - **장점 (Ưu điểm):** 규모가 작은 소프트웨어에 유리, 단시간 내 테스트 가능. *(Thích hợp cho phần mềm nhỏ, tốn ít thời gian.)*
  - **단점 (Nhược điểm):** 오류 발견 및 원인 식별이 매우 어려움. *(Khó phát hiện lỗi và xác định nguyên nhân do test một cục lớn.)*
- **점진적 통합 방식 (Incremental):**
  - 모듈 단위로 단계적으로 통합하면서 테스트함. *(Tích hợp từng bước theo từng module để kiểm thử.)*
  - 종류 (Các loại): 하향식(Top-down), 상향식(Bottom-up), 혼합식(Sandwich).
  - **장점 (Ưu điểm):** 오류 수정이 쉽고, 인터페이스와 관련된 오류를 완전히 테스트할 가능성이 높음. *(Dễ sửa lỗi và kiểm tra kỹ được các lỗi kết nối giữa các module.)*

**[4] 예시 (Ví dụ thực tế):**
- **비유 (자동차 조립 - Lắp ráp ô tô):**
  - *Unit Test:* Kiểm tra động cơ, bánh xe, vô lăng riêng biệt. Tất cả đều tốt.
  - *Big Bang:* Lắp ráp toàn bộ rồi mới khởi động. Xe không nổ máy $\rightarrow$ Không biết do động cơ, bình ắc quy hay bugi.
  - *Incremental:* Lắp động cơ vào hộp số rồi test (OK). Lắp thêm bánh xe rồi test (OK) $\rightarrow$ Nếu có lỗi sẽ biết ngay tại bộ phận vừa lắp thêm.

> 💡 **Mẹo ghi nhớ (Mnemonics):**
> - **Big Bang** = "Bùm" một phát gom hết lại, nếu hỏng thì không biết sửa từ đâu.
> - **Incremental** = "Từng bước", thêm một phần tử vào nếu sai thì do phần tử đó.

---

# 137 & 138. 하향식 / 상향식 통합 테스트 (Top Down & Bottom Up Integration Test)

Phần **137 & 138. 하향식 / 상향식 통합 테스트 (Top Down & Bottom Up Integration Test)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 개념 (Khái niệm):**
- **하향식 (Top-down):** 프로그램의 상위 모듈에서 하위 모듈 방향으로 통합하며 테스트. *(Kiểm thử từ module cấp cao nhất (chính) xuống các module cấp thấp (phụ).)*
- **상향식 (Bottom-up):** 프로그램의 하위 모듈에서 상위 모듈 방향으로 통합하며 테스트. *(Kiểm thử từ các module cấp thấp (cơ sở) dần lên module cấp cao.)*

**[2] 핵심 키워드 (Từ khóa chính):**
- **하향식:** 깊이 우선(Depth-first), 넓이 우선(Breadth-first), **스텁(Stub)**.
- **상향식:** 클러스터(Cluster), **테스트 드라이버(Driver)**.

**[3] 차이점 비교 (So sánh chi tiết):**
- **하향식 (Top-Down):**
  - 하위 모듈이 아직 없으므로, 이를 thay thế bằng **Stub** (모듈의 흉내를 내는 가짜 하위 모듈 - module giả lập cấp dưới).
  - 테스트 초기부터 시스템의 전체 구조를 보여주기 유리.
- **상향식 (Bottom-Up):**
  - 하위 모듈들을 클러스터(Cluster)로 묶어서 수행.
  - 상위 모듈이 없으므로, 하위 모듈을 gọi bằng **Driver** (테스트를 제어하는 가짜 상위 모듈 - module giả lập cấp trên điều khiển test).

**[4] 예시 (Ví dụ thực tế):**
- **Top-Down:** Kiểm tra màn hình Đăng nhập (Main). Vì chưa có database, ta tạo một `Stub` (hàm giả) cứ nhận id/pass là trả về "Thành công".
- **Bottom-Up:** Đã viết xong hàm mã hóa mật khẩu (phụ), nhưng chưa có màn hình Đăng nhập. Ta viết một đoạn code ngắn (`Driver`) để gọi hàm mã hóa đó với các chuỗi khác nhau xem nó mã hóa đúng không.

> 💡 **Mẹo ghi nhớ (Mnemonics):**
> - **Top-Down = Stub** (Từ trên xuống gặp tảng đá - S).
> - **Bottom-Up = Driver** (Từ dưới lên cần tài xế lái lên - D).

---

# 139. 테스트 드라이버와 테스트 스텁 (Test Driver vs Test Stub)

Phần **139. 테스트 드라이버와 테스트 스텁 (Test Driver vs Test Stub)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 개념 (Khái niệm):** 결합 테스트 시 미구현된 모듈을 대체하거나 구동하기 위한 가짜(Dummy) 모듈.
*(Module giả lập được dùng thay thế cho các module chưa hoàn thiện trong quá trình kiểm thử tích hợp.)*

**[2] 비교 (So sánh):**
- **드라이버 (Driver):** 상위 모듈 대체. 하위 모듈을 호출하고 매개변수 전달. (Dùng trong Bottom-Up).
- **스텁 (Stub):** 하위 모듈 대체. 상위 모듈의 호출에 단순 응답(결과값)만 제공. (Dùng trong Top-Down).

*(Ví dụ và mẹo nhớ đã tích hợp ở mục 137 & 138 phía trên để tránh lặp lại).*

---

# 140. 회귀 테스팅 (Regression Testing - Kiểm thử hồi quy)

Phần **140. 회귀 테스팅 (Regression Testing - Kiểm thử hồi quy)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 개념 (Khái niệm):** 수정된 모듈이나 컴포넌트가 다른 부분에 영향을 미치는지 확인하기 위해 테스트를 반복하는 것.
*(Kiểm tra lại toàn bộ hoặc một phần hệ thống sau khi đã sửa lỗi hoặc thêm tính năng mới, để đảm bảo việc sửa chữa này không làm hỏng các tính năng cũ đang hoạt động tốt.)*

**[2] 핵심 키워드 (Từ khóa chính):**
- 새로운 오류 확인 (Xác nhận không có lỗi mới)
- 기존 기능 보장 (Đảm bảo chức năng cũ)
- 테스트 케이스 선정 (Lựa chọn test case hiệu quả)

**[3] 예시 (Ví dụ thực tế):**
- Trang web có tính năng Đăng nhập và Thanh toán đang dùng tốt. Bạn vừa sửa tính năng Đăng nhập. Bạn phải chạy lại *Regression Test* để chắc chắn rằng sửa xong Đăng nhập thì nút Thanh toán không tự nhiên bị liệt.

> 💡 **Mẹo ghi nhớ (Mnemonics):**
> - **Regression (Hồi quy)** = Quay trở lại (Hồi) quy trình cũ để test xem có hỏng không.

---

# 140-1 ~ 143-1. 테스트 계획, 프로세스, 케이스 및 시나리오 (Test Process, Case & Scenario)

Phần **140-1 ~ 143-1. 테스트 계획, 프로세스, 케이스 및 시나리오 (Test Process, Case & Scenario)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 테스트 프로세스 (Test Process - Quy trình kiểm thử):**
- 계획(Plan) $\rightarrow$ 분석(Analysis) $\rightarrow$ 설계(Design) $\rightarrow$ 수행(Execution) $\rightarrow$ 평가(Evaluation) $\rightarrow$ 관리(Management).

**[2] 테스트 케이스 (Test Case - Kịch bản kiểm thử chi tiết):**
- **개념:** 요구사항 준수 여부를 확인하기 위한 입력 값, 실행 조건, 기대 결과의 명세서. *(Tài liệu đặc tả bao gồm dữ liệu đầu vào, điều kiện thực thi và kết quả mong muốn để kiểm tra chức năng).*
- **작성 순서 (Thứ tự viết):** 자료 확보 $\rightarrow$ 위험 평가(우선순위 결정) $\rightarrow$ 요구사항 정의 $\rightarrow$ 구조 설계 $\rightarrow$ **케이스 정의 (입력값, 조건, 기대결과)** $\rightarrow$ 타당성 확인.
- **예시:** "Nhập ID 'admin', Pass '1234' (Input) tại trang Login (Condition) $\rightarrow$ Chuyển sang trang chủ (Expected Result)."

**[3] 테스트 시나리오 (Test Scenario - Kịch bản luồng kiểm thử):**
- **개념:** 테스트 케이스를 적용하는 순서에 따라 여러 개의 테스트 케이스들을 묶은 집합 문서. *(Tập hợp nhiều Test Case lại với nhau theo một trình tự để kiểm tra một luồng nghiệp vụ hoàn chỉnh).*
- **유의사항:** 시스템/모듈별로 분리 작성, 유스케이스 간 업무 흐름(Workflow) 검증.
- **예시:** Kịch bản mua hàng: "Đăng nhập (Test Case 1) $\rightarrow$ Tìm kiếm sản phẩm (Test Case 2) $\rightarrow$ Thêm vào giỏ (Test Case 3) $\rightarrow$ Thanh toán (Test Case 4)."

> 💡 **Mẹo ghi nhớ (Mnemonics):**
> - **Test Case** = Từng bước đi độc lập (Kiểm tra 1 hành động).
> - **Test Scenario** = Chuyến hành trình (Nhiều bước nối tiếp nhau tạo thành kịch bản).

---

# 144 & 145. 테스트 오라클과 그 종류 (Test Oracle & Types)

Phần **144 & 145. 테스트 오라클과 그 종류 (Test Oracle & Types)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 개념 (Khái niệm):** 테스트 결과가 올바른지 판단하기 위해 사전에 정의된 참(True) 값을 대입하여 비교하는 기법.
*(Cơ chế so sánh kết quả thực tế của phần mềm với kết quả mong đợi (đáp án chuẩn) để xác định xem phần mềm chạy đúng hay sai).*

**[2] 종류 (Các loại Test Oracle):**
1. **참 오라클 (True Oracle):** 모든 입력에 대해 완벽한 결과를 제공 (Độ bao phủ 100%, chi phí cực cao).
2. **샘플링 오라클 (Sampling Oracle):** 특정 몇몇 입력 값에 대해서만 결과 제공 (Lấy mẫu ngẫu nhiên, chi phí thấp).
3. **추정 오라클 (Heuristic Oracle):** 샘플링 오라클을 개선하여 일부는 참 값을, 나머지는 추정(Heuristic)으로 처리.
4. **일관성 오라클 (Consistent Oracle):** 애플리케이션 변경 시 테스트 전후 결과값이 같은지 확인 (Dùng trong Regression test).

**[3] 예시 (Ví dụ thực tế):**
- Máy tính bỏ túi:
  - *True Oracle:* Tính thử mọi phép tính có thể (Không tưởng).
  - *Sampling Oracle:* Chỉ tính thử $1+1$, $2*3$, $10/2$.
  - *Consistent Oracle:* Bản update mới của app máy tính, lấy kết quả của bản cũ so sánh với bản mới.

> 💡 **Mẹo ghi nhớ (Mnemonics):**
> - **Oracle** = Nhà tiên tri (đưa ra đáp án chuẩn). 4 loại: **T**rue - **S**ampling - **H**euristic - **C**onsistent.

---

# 146 & 146-1. 테스트 자동화 도구 (Test Automation Tools)

Phần **146 & 146-1. 테스트 자동화 도구 (Test Automation Tools)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 개념 (Khái niệm):** 반복적인 테스트 활동을 스크립트나 자동화 소프트웨어로 기계가 대신 수행하게 하는 것.
*(Sử dụng công cụ phần mềm để chạy các bài test một cách tự động, thay vì con người bấm tay).*

**[2] 장점과 단점 (Ưu & Nhược điểm):**
- **장점 (Pros):** 반복 작업(Repetitive) 감소, 일관성(Consistency) 및 객관성 확보, 품질 향상.
- **단점 (Cons):** 초기 구축 비용(비용/노력)이 많이 듦, 도구 학습(교육) 필요.

**[3] 자동화 도구 유형 (Phân loại):**
- **정적 분석 도구 (Static Analysis Tool):** 코드를 실행하지 않고 결함이나 복잡도 분석 (VD: SonarQube).
- **동적 분석 도구 (Dynamic Analysis Tool):** 코드를 직접 실행하여 메모리 누수 등을 파악.

**[4] 고려사항 (Lưu ý khi áp dụng):**
- 재사용(Reusability) 불가능한 1회성 테스트는 자동화에서 제외.
- 프로젝트 초기에 엔지니어 투입 (Early Involvement) để thiết kế cấu trúc test automation.

**[5] 예시 (Ví dụ thực tế):**
- Sử dụng *Selenium* (Công cụ tự động hóa) để code một kịch bản: Tự động mở trình duyệt $\rightarrow$ Điền form $\rightarrow$ Bấm nút "Submit" hàng ngàn lần để test sức chịu đựng (Stress test). Việc này nếu dùng người bấm tay sẽ mất rất nhiều thời gian (손설거지 vs 식기세척기 - Rửa bát bằng tay vs Máy rửa bát).

> 💡 **Mẹo ghi nhớ (Mnemonics):**
> - Tự động hóa = "Máy rửa bát". Đắt tiền mua (초기 비용) nhưng rửa 1000 cái bát rất nhanh (반복 작업 최적화).

---

# 147. 테스트 하네스 (Test Harness)

Phần **147. 테스트 하네스 (Test Harness)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 개념 (Khái niệm):** 시스템이나 모듈을 테스트하기 위해 생성된 코드와 데이터의 집합 (환경).
*(Môi trường bao gồm các đoạn code giả lập, dữ liệu và công cụ để thực thi test).*

**[2] 구성 요소 (Thành phần chính):**
- **Driver / Stub:** (Đã giải thích ở trên).
- **Test Suite (테스트 슈트):** 테스트 케이스들의 집합 (Tập hợp các test case).
- **Test Script (테스트 스크립트):** 자동화된 테스트 실행 절차를 기록한 명세서 (Kịch bản code chạy tự động).
- **Mock Object (목 오브젝트):** 사용자의 예정된 행위를 조건부로 입력해 둔 가짜 객체 (Đối tượng giả lập dữ liệu trả về).

---

# 148. 결함 (Fault / Defect)

Phần **148. 결함 (Fault / Defect)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 개념 (Khái niệm):** 소프트웨어가 개발자의 설계와 다르게 동작하거나 잘못된 결과를 발생시키는 현상 (Bug).
*(Bất kỳ lỗi, thiếu sót nào khiến phần mềm chạy không đúng với tài liệu đặc tả yêu cầu).*

**[2] 예시 (Ví dụ thực tế):**
- Thiết kế: Nút "Hủy" phải có màu Đỏ. Thực tế: Lập trình viên làm nút "Hủy" màu Xanh $\rightarrow$ Đây cũng được tính là một 결함 (Fault) dù không gây crash app.

---

# 149 ~ 151. 성능 분석, 빅오 표기법, 순환 복잡도 (Performance Analysis, Big-O, Cyclomatic Complexity)

Phần **149 ~ 151. 성능 분석, 빅오 표기법, 순환 복잡도 (Performance Analysis, Big-O, Cyclomatic Complexity)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 애플리케이션 성능 지표 (Chỉ số hiệu năng):**
- **처리량 (Throughput):** 일정 시간 동안 처리하는 작업의 양 (Số lượng task xử lý được trong một khoảng thời gian).
- **응답 시간 (Response Time):** 요청부터 응답이 시작될 때까지의 시간 (Thời gian từ lúc click đến lúc app bắt đầu phản hồi).
- **경과 시간 (Turn Around Time):** 요청부터 처리가 완전히 끝날 때까지 걸린 시간 (Thời gian từ lúc click đến lúc hoàn thành 100% công việc).
- **자원 사용률 (Resource Usage):** CPU, 메모리 소비 정도 (Mức độ ngốn RAM, CPU).

**[2] 빅오 표기법 (Big-O Notation - Ký hiệu Big-O):**
- 최악일 때(Worst Case)를 기준으로 알고리즘의 복잡도(실행 시간)를 표기.
- **성능 순서 (Tốc độ từ nhanh $\rightarrow$ chậm):**
  $O(1)$ (Hằng số) $\rightarrow$ $O(log n)$ (Tìm kiếm nhị phân) $\rightarrow$ $O(n)$ (Tuyến tính) $\rightarrow$ $O(n log n)$ (Sắp xếp trộn) $\rightarrow$ $O(n^2)$ (Sắp xếp nổi bọt).

**[3] 순환 복잡도 (Cyclomatic Complexity - Độ phức tạp theo chu trình McCabe):**
- 프로그램의 논리적인 복잡도를 독립적인 경로의 수로 수치화. (Số lượng đường dẫn độc lập trong code).
- **공식 (Công thức):** với một đồ thị luồng liên thông, $V(G) = E - N + 2$ (E: Edge, N: Node); tổng quát là $V(G)=E-N+2P$ với P là số thành phần liên thông. Có thể dùng số vùng kín + 1.

**[4] 예시 (Ví dụ thực tế):**
- **Throughput vs Response Time:** Một quán phở có thể bán 100 bát/giờ (Throughput = 100). Nhưng khách vào gọi món phải chờ 15 phút mới bê ra (Response time = 15m).
- **McCabe $V(G)$:** Nếu vẽ sơ đồ luồng (Flowchart) của hàm If-Else có 4 Node và 4 Edge $\rightarrow$ $V(G) = 4 - 4 + 2 = 2$ (Có 2 đường đi độc lập).

> 💡 **Mẹo ghi nhớ (Mnemonics):**
> - Công thức McCabe: **E**m **N**hớ **+ 2** ($E - N + 2$).

---

# 152 & 153. 소스 코드 최적화 및 품질 분석 (Source Code Optimization & Quality Analysis)

Phần **152 & 153. 소스 코드 최적화 및 품질 분석 (Source Code Optimization & Quality Analysis)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 최적화 개념 (Khái niệm tối ưu hóa):**
- 나쁜 코드(Bad Code / Spaghetti Code / Alien Code)를 배제하고, **클린 코드(Clean Code)**로 작성하여 가독성(Readability)과 유지보수성 향상.
*(Viết code sạch sẽ, rõ ràng, dễ hiểu, tránh viết code rối như tơ vò (Spaghetti) hoặc code không ai hiểu được (Alien).*

**[2] 소스 코드 품질 분석 도구 (Công cụ phân tích chất lượng code):**
- **정적 분석 도구 (Static Analysis):** 코드를 실행하지 않고 패턴 분석 (VD: pmd, cppcheck, SonarQube).
- **동적 분석 도구 (Dynamic Analysis):** 소스 코드를 실행하여 메모리 누수(Memory Leak) 분석 (VD: Valgrind, Avalanche).

**[3] 예시 (Ví dụ thực tế):**
- **Alien Code (Code người ngoài hành tinh):** Code từ chục năm trước, tài liệu bị mất, người viết code đã nghỉ việc, sếp bảo bạn sửa code đó $\rightarrow$ Không thể sửa nổi!

---

# 154 & 155. 시스템 연계: EAI와 ESB (System Integration: EAI & ESB)

Phần **154 & 155. 시스템 연계: EAI와 ESB (System Integration: EAI & ESB)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] EAI (Enterprise Application Integration):**
- 기업 내 각종 애플리케이션 및 플랫폼 간의 정보 전달을 위한 통합 솔루션. *(Giải pháp tích hợp các ứng dụng trong doanh nghiệp để chúng có thể chia sẻ dữ liệu với nhau).*
- **유형 (4 loại):**
  - **Point-to-Point:** 1:1 직접 연결 (Nối trực tiếp A-B, nhiều kết nối sẽ rối).
  - **Hub & Spoke:** 중앙 허브를 통한 연결 (Có một Hub ở giữa điều phối, dễ quản lý).
  - **Message Bus:** 미들웨어 버스를 통한 연계 (Gắn tất cả vào 1 trục bus chung, mở rộng tốt).
  - **Hybrid:** Hub & Spoke + Message Bus.

**[2] ESB (Enterprise Service Bus):**
- 표준 기반의 **서비스 중심 통합 (SOA - Service Oriented Architecture)**.
- 애플리케이션 간 **약한 결합 (Loosely Coupled)**을 유지하여 유연성을 극대화.
*(Cũng giống EAI nhưng ESB dựa trên các dịch vụ web tiêu chuẩn, các hệ thống kết nối lỏng lẻo (ít phụ thuộc nhau), phù hợp hệ thống cực lớn).*

> 💡 **Mẹo ghi nhớ (Mnemonics):**
> - **EAI** = Tích hợp hệ thống ứng dụng cục bộ.
> - **ESB** = Tích hợp "Dịch vụ" (Service) theo SOA.

---

# 156. JSON (JavaScript Object Notation)

Phần **156. JSON (JavaScript Object Notation)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 개념 (Khái niệm):** 속성-값 쌍(Attribute-Value)으로 이루어진 데이터 객체를 전달하는 텍스트 포맷.
*(Định dạng trao đổi dữ liệu dạng văn bản nhẹ, bao gồm các cặp Thuộc tính - Giá trị).*

**[2] 핵심 (Đặc điểm chính):**
- 비동기 통신(AJAX)에서 XML을 대체하여 널리 쓰임.
- 구문이 간결하고 데이터 파싱 속도가 빠름.
*(Dùng rất phổ biến trong lập trình Web/Mobile hiện đại để gửi nhận dữ liệu thay cho XML vì nó nhẹ và dễ đọc).*

**[3] 예시 (Ví dụ thực tế):**
```json
{
  "name": "Nguyen Van A",
  "age": 25,
  "role": "Developer"
}
```
*(Đây là định dạng JSON, cực kỳ dễ đọc đối với cả người và máy).*

---

# 157. XML (eXtensible Markup Language)

Phần **157. XML (eXtensible Markup Language)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 개념 (Khái niệm):** 특수한 목적을 갖는 마크업 언어를 만드는 데 사용되는 다목적 마크업 언어.
*(Ngôn ngữ đánh dấu đa mục đích, được sử dụng để tạo ra các ngôn ngữ đánh dấu khác phục vụ mục đích đặc thù).*

**[2] 핵심 키워드 (Từ khóa chính):** HTML 단점 보완 (Khắc phục nhược điểm HTML), 사용자 정의 태그 (Thẻ tự định nghĩa).

**[3] 특징 (Đặc điểm):**
- HTML chỉ có các thẻ cố định (`<h1>`, `<b>`), còn XML cho phép người dùng tự tạo thẻ mới (`<student>`, `<name>`).
- Tách biệt giữa nội dung (Content)와 cách hiển thị (Style).

**[4] 예시 (Ví dụ thực tế):**
```xml
<person>
  <name>Nguyen Van A</name>
  <age>25</age>
</person>
```

---

# 158. AJAX (Asynchronous JavaScript and XML)

Phần **158. AJAX (Asynchronous JavaScript and XML)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 개념 (Khái niệm):** 자바스크립트를 이용해 클라이언트와 서버 간에 데이터를 주고받는 비동기 통신 기술.
*(Công nghệ giao tiếp bất đồng bộ giữa Client và Server sử dụng JavaScript).*

**[2] 핵심 키워드 (Từ khóa chính):** 비동기 통신 (Bất đồng bộ), 새로고침 없음 (Không tải lại trang).

**[3] 특징 (Đặc điểm):**
- Trang web không cần tải lại toàn bộ (Refresh), chỉ cập nhật một phần dữ liệu mong muốn.
- Ngày nay, AJAX thường dùng JSON thay vì XML để truyền dữ liệu vì JSON nhẹ và nhanh hơn.

**[4] 예시 (Ví dụ thực tế):**
- Khi lướt Facebook hoặc đọc bình luận Youtube, bấm "Tải thêm bình luận", các bình luận mới sẽ hiện ra ngay bên dưới mà trình duyệt không hề chớp màn hình tải lại nguyên trang web.

---

# 159. 인터페이스 보안 기능 적용 (Interface Security Application)

Phần **159. 인터페이스 보안 기능 적용 (Interface Security Application)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 개념 (Khái niệm):** 인터페이스 송·수신 시 데이터 탈취 및 변조를 방지하기 위해 각 영역에 보안 설정을 적용하는 활동.
*(Áp dụng các biện pháp bảo mật vào các khu vực khác nhau để ngăn chặn đánh cắp hoặc thay đổi dữ liệu trong quá trình truyền tải).*

**[2] 영역별 보안 (Bảo mật theo khu vực):**
- **네트워크 영역 (Network):** IPsec, SSL, S-HTTP 등 암호화 (Mã hóa đường truyền).
- **애플리케이션 영역 (Application):** 소프트웨어 개발 보안 가이드 적용 (Lập trình an toàn).
- **데이터베이스 영역 (Database):** 스키마, 엔티티 접근 권한 설정 (Thiết lập quyền truy cập DB).

**[3] 예시 (Ví dụ thực tế):**
- **Sniffing (Nghe lén):** Hacker dùng phần mềm bắt gói tin trên mạng Wi-Fi quán cà phê. Nếu bạn dùng SSL (https), hacker chỉ thấy chuỗi ký tự mã hóa vô nghĩa.

---

# 160. 데이터 무결성 검사 도구 (Data Integrity Check Tools)

Phần **160. 데이터 무결성 검사 도구 (Data Integrity Check Tools)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 개념 (Khái niệm):** 시스템 파일의 변경 유무를 확인하고 파일 변동 시 관리자에게 알려주는 보안 도구.
*(Công cụ bảo mật kiểm tra xem tệp hệ thống có bị thay đổi trái phép không và cảnh báo cho quản trị viên).*

**[2] 핵심 키워드 (Từ khóa chính):** 해시(Hash) 함수, 백도어(Backdoor) 감지.
- **도구 종류 (Các công cụ phổ biến):** Tripwire, AIDE, Samhain, Claymore, Fcheck.

**[3] 예시 (Ví dụ thực tế):**
- Hacker cài **Backdoor (Cửa hậu)** vào file `login.php`. Công cụ Tripwire sử dụng hàm băm (Hash) và phát hiện ra mã băm của `login.php` hôm nay khác với hôm qua $
ightarrow$ Phát chuông cảnh báo.

---

# 161. 인터페이스 구현 검증 도구 (Interface Implementation Verification Tools)

Phần **161. 인터페이스 구현 검증 도구 (Interface Implementation Verification Tools)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 개념 (Khái niệm):** 구현된 인터페이스가 정상적으로 작동하는지 확인하기 위해 사용되는 테스트 자동화 프레임워크.
*(Khung tự động hóa kiểm thử để xác minh giao diện kết nối hoạt động bình thường).*

**[2] 도구 종류 (Các công cụ):**
- **FitNesse:** 웹 기반 테스트 (Kiểm thử trên nền Web).
- **Selenium:** 웹 브라우저 검증 (Hỗ trợ đa trình duyệt, cực kỳ phổ biến).
- **watir:** Ruby 기반 프레임워크 (Dùng ngôn ngữ Ruby).
- **NTAF:** FitNesse + STAF (Công cụ nội bộ do Naver phát triển).

---

# 162. APM (Application Performance Management)
Phần “162. APM (Application Performance Management)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

*(Gộp chung hai nội dung lặp ở bản gốc)*

**[1] 개념 (Khái niệm):** 애플리케이션의 성능 관리를 위해 접속자, 자원 현황, 트랜잭션 수행 내역 등을 모니터링하는 도구.
*(Công cụ giám sát hiệu năng ứng dụng, theo dõi lượng người truy cập, tài nguyên và giao dịch theo thời gian thực).*

**[2] 유형 (Phân loại):**
- **리소스 방식 (Resource - Theo tài nguyên):** Giám sát phần cứng như CPU, RAM (VD: Nagios, Zabbix).
- **엔드투엔드 방식 (End-to-End - Toàn trình):** Giám sát từ lúc User click đến khi kết thúc giao dịch (VD: Jennifer, VisualVM, Scouter).

**[3] 예시 (Ví dụ thực tế):**
- Ngày Black Friday, hệ thống bán hàng bị chậm. Nhìn vào màn hình **Jennifer (APM)**, quản trị viên thấy biểu đồ "Database connection" đang đỏ chót $
ightarrow$ Lập tức biết lỗi do kẹt DB chứ không phải do thiếu RAM.

---

# 💡 통합 비유 (Mẹo ghi nhớ tổng hợp)
Phần “💡 통합 비유 (Mẹo ghi nhớ tổng hợp)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **알고리즘 비유 (Thuật toán):**
  - **빅오(Big-O):** Mua balo, luôn nghĩ tới lúc đựng nặng nhất xem có rách không (Worst case).
  - **순환 복잡도(McCabe):** Tính xem tòa nhà có bao nhiêu ngã rẽ để khi cháy bảo vệ phải đi kiểm tra từng ngóc ngách ít nhất bao nhiêu lần.
- **인터페이스 통신 비유 (Giao tiếp & Bảo mật):**
  - **XML / JSON:** Là các "thùng container" có quy chuẩn để chứa hàng (dữ liệu).
  - **AJAX:** Hệ thống "dỡ hàng bất đồng bộ" - Tàu không cần dừng hẳn, băng chuyền cứ lấy đồ ra từ từ mà hành khách không bị gián đoạn.
  - **인터페이스 보안 (Security):** Ổ khóa khóa chặt cửa container lại.
  - **무결성 검사 (Integrity):** Hải quan kiểm tra "Tem niêm phong", xem tem có bị rách hay thay tem giả không (Tripwire).
  - **APM:** Camera giám sát toàn bộ hoạt động cảng biển xem xe nào kẹt, kho nào đầy (Jennifer).

---

# 115. 분산 저장소 방식 (Distributed Repository System)

Phần **115. 분산 저장소 방식 (Distributed Repository System)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

**[1] 개념 (Khái niệm):** 버전 관리 자료가 하나의 원격 저장소와 분산된 개발자 PC의 로컬 저장소에 함께 저장되어 관리되는 방식.
*(Hệ thống quản lý phiên bản mã nguồn, trong đó dữ liệu được lưu ở cả Server từ xa và máy tính cá nhân của mỗi lập trình viên).*

**[2] 핵심 키워드 (Từ khóa chính):** 로컬 저장소 (Local Repo), 원격 저장소 (Remote Repo), Git.

**[3] 특징 (Đặc điểm):**
- 개발자는 원격 저장소의 자료를 복제(Clone)하여 오프라인에서도 작업 가능.
- Server (Remote) bị sập thì vẫn còn dữ liệu nguyên vẹn ở Local Repo의 개발자.
- **대표 도구 (Công cụ tiêu biểu):** Git, Mercurial.

**[4] 예시 (Ví dụ thực tế):**
- Bạn dùng **Git**. Khi cúp mạng internet, bạn vẫn có thể `git commit` để lưu lại phiên bản code trên máy mình. Khi có mạng lại, bạn mới `git push` để đẩy lên Server.

> 💡 **Mẹo ghi nhớ (Mnemonics):**
> - **Phân tán (Distributed) = Git:** Không có mạng vẫn lưu code được. Trái ngược với SVN (Tập trung) rớt mạng là khỏi lưu.

Điểm chốt của **132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **A+ Deep Dive: 알고리즘 trace와 테스트 판정**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## A+ Deep Dive: 알고리즘 trace와 테스트 판정

Ở bước 67/101, **A+ Deep Dive: 알고리즘 trace와 테스트 판정** xuất hiện như phần tiếp nối của **132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **A+ Deep Dive: 알고리즘 trace와 테스트 판정** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận. Trong khối này, **테스트 케이스**, **테스트 오라클**, **회귀 테스트**, **스텁/드라이버** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. 이분 검색 trace** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. 이분 검색 trace** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. 이분 검색 trace

Bây giờ ta đi vào nội dung của **1. 이분 검색 trace**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

정렬된 배열 `A = [2, 5, 8, 12, 16]`에서 `target = 12`를 찾는다.

| 단계 | 탐색 구간 | 중간값 | 판정 |
|---|---|---:|---|
| 1 | 0..4 | `A[2]=8` | 12가 더 크므로 오른쪽 구간 |
| 2 | 3..4 | `A[3]=12` | 발견 |

- 반복마다 탐색 범위가 절반으로 줄어 `O(log n)`이다.
- 배열이 정렬되지 않았다면 이 알고리즘의 전제조건이 깨진다.
- `O(log n)`은 실행 시간의 증가율이며, 실제 초 단위 시간이 항상 빠르다는 보장은 아니다.

Khi đọc **1. 이분 검색 trace**, hãy tách hai lớp: bảng giúp đối chiếu các loại hoặc tiêu chí, còn công thức cần được đọc theo biến, đơn vị và quan hệ giữa các đại lượng. Cách tách này giúp ta hiểu cơ chế trước khi ghi nhớ ký hiệu.

Ta vừa chốt **1. 이분 검색 trace** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 테스트 용어를 답으로 연결하기** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. 테스트 용어를 답으로 연결하기**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. 테스트 용어를 답으로 연결하기

Phần nguồn của **2. 테스트 용어를 답으로 연결하기** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “2. 테스트 용어를 답으로 연결하기” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **테스트 케이스**: 입력·실행 조건·기대 결과의 묶음.
- **테스트 오라클**: 결과가 옳은지 판정하는 기준 또는 메커니즘.
- **회귀 테스트**: 수정 후 기존 기능이 깨지지 않았는지 재확인.
- **스텁/드라이버**: 하향식 통합에서는 스텁, 상향식 통합에서는 드라이버를 사용한다.

> **시험 함정:** 테스트 케이스는 입력 시나리오이고, 오라클은 정답 판정 기준이다. 둘을 같은 뜻으로 쓰지 않는다.

Các bullet của **2. 테스트 용어를 답으로 연결하기** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. 테스트 용어를 답으로 연결하기**, đừng bắt đầu lại từ số không. **자주 혼동하는 판별 포인트** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **자주 혼동하는 판별 포인트** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 자주 혼동하는 판별 포인트

Các ý ngay dưới **자주 혼동하는 판별 포인트** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “자주 혼동하는 판별 포인트” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **정적 분석**은 프로그램을 실행하지 않고 규칙·복잡도·잠재 오류를 분석한다. 실행 중 메모리 상태를 관찰하는 도구는 동적 분석으로 분류한다.
- 선택 정렬은 매 회전마다 남은 구간의 최솟값을 앞에 둔다. 정렬 trace에서는 “한 번의 비교”가 아니라 “한 회전의 교환 결과”를 기록한다.
- **Jenkins**는 CI/CD 자동화 서버이고, Gradle은 task 기반 빌드 자동화 도구다. 둘은 대체 관계가 아니라 연동할 수 있다.
- 함수 호출 복귀·수식 계산·괄호 검사처럼 후입선출이 필요한 문제는 **스택**, 도착 순서대로 처리하는 작업은 **큐**를 우선 떠올린다.

Các bullet của **자주 혼동하는 판별 포인트** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **자주 혼동하는 판별 포인트** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **A+ Deep Dive: 알고리즘 trace와 테스트 판정** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **092-1: 쿼리 성능 최적화 (Query Performance Optimization)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 092-1: 쿼리 성능 최적화 (Query Performance Optimization)

Sau khi đã đặt nền bằng **A+ Deep Dive: 알고리즘 trace와 테스트 판정**, ta chuyển sang **092-1: 쿼리 성능 최적화 (Query Performance Optimization)**. Đây là mắt xích 68/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **092-1: 쿼리 성능 최적화 (Query Performance Optimization)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “092-1: 쿼리 성능 최적화 (Query Performance Optimization)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 데이터 입·출력 애플리케이션의 성능 향상을 위해 **SQL 코드를 최적화**하는 작업. (Tối ưu hóa mã SQL để tăng tốc độ truy xuất).
- **최적화 절차 (Trình tự tối ưu hóa):**
  1. **대상 선정:** **APM (Application Performance Monitoring)** 등 성능 측정 도구를 사용하여 느린 쿼리를 찾아냄. (Dùng APM tìm câu SQL chạy chậm).
  2. **계획 검토:** **옵티마이저 (Optimizer)**가 수립한 **실행 계획 (Execution Plan)**을 분석. (Xem bản đồ đường đi do bộ Tối ưu hóa lập ra xem có bị đi lòng vòng không).
  3. **재구성 (튜닝):** SQL 코드를 수정하거나 **인덱스 (Index)**를 재구성. (Sửa lại code hoặc tạo Index để tăng tốc).

- 💡 **Mẹo ghi nhớ (Mnemonics):** APM (Tìm bệnh) -> Optimizer/Execution Plan (Khám bệnh / Xem phim X-quang) -> Tuning (Chữa bệnh / Tạo Index).

---

Ta có thể khép mục **092-1: 쿼리 성능 최적화 (Query Performance Optimization)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **24. 인터페이스 보안 - 네트워크 영역 (Interface Security - Network Area)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 24. 인터페이스 보안 - 네트워크 영역 (Interface Security - Network Area)

Từ **092-1: 쿼리 성능 최적화 (Query Performance Optimization)**, ta đã có điểm tựa để bước vào **24. 인터페이스 보안 - 네트워크 영역 (Interface Security - Network Area)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 69/101 trước khi đi vào chi tiết.

Để đọc **24. 인터페이스 보안 - 네트워크 영역 (Interface Security - Network Area)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **방식**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “24. 인터페이스 보안 - 네트워크 영역 (Interface Security - Network Area)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 네트워크 트래픽에 대한 암호화 설정.
* **방식**: IPSec, SSL, S-HTTP 등.
* **VI (Vietnamese) (Tiếng Việt):** Bảo mật giao diện vùng mạng (mã hóa lưu lượng). Dùng IPSec, SSL, S-HTTP.
* **Example**: 웹사이트 주소가 `https://`로 시작하면 SSL이 적용된 것입니다.

Điểm chốt của **24. 인터페이스 보안 - 네트워크 영역 (Interface Security - Network Area)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **26. 인터페이스 구현 검증 도구 (Interface Verification Tools)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 26. 인터페이스 구현 검증 도구 (Interface Verification Tools)

Ở bước 70/101, **26. 인터페이스 구현 검증 도구 (Interface Verification Tools)** xuất hiện như phần tiếp nối của **24. 인터페이스 보안 - 네트워크 영역 (Interface Security - Network Area)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **26. 인터페이스 구현 검증 도구 (Interface Verification Tools)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **xUnit**, **STAF**, **FitNesse**, **NTAF** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “26. 인터페이스 구현 검증 도구 (Interface Verification Tools)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **xUnit**: 다양한 언어에 적용되는 단위 테스트 프레임워크 (JUnit, CppUnit, NUnit).
* **STAF**: 서비스 호출 및 컴포넌트 재사용 등 다양한 환경 지원.
* **FitNesse**: 웹 기반 테스트 케이스 설계, 실행, 결과 확인.
* **NTAF**: FitNesse와 STAF의 장점을 통합한 NHN(Naver)의 테스트 자동화 프레임워크.
* **watir**: Ruby 기반 웹 애플리케이션 테스트 프레임워크.
* **VI (Vietnamese) (Tiếng Việt):** Các công cụ kiểm thử giao diện. xUnit (kiểm thử đơn vị), STAF, FitNesse (Web), NTAF (Naver), watir (Ruby).
* 💡 **Mẹo ghi nhớ**: xUnit là phổ biến nhất cho Unit Test. NTAF có chữ N (Naver).

Như vậy, **26. 인터페이스 구현 검증 도구 (Interface Verification Tools)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **9. 스키마 3계층 (Three-Schema Architecture)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 9. 스키마 3계층 (Three-Schema Architecture)

Sau khi đã đặt nền bằng **26. 인터페이스 구현 검증 도구 (Interface Verification Tools)**, ta chuyển sang **9. 스키마 3계층 (Three-Schema Architecture)**. Đây là mắt xích 71/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **9. 스키마 3계층 (Three-Schema Architecture)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **외부 스키마 (External Schema)**, **개념 스키마 (Conceptual Schema)**, **내부 스키마 (Internal Schema)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “9. 스키마 3계층 (Three-Schema Architecture)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **외부 스키마 (External Schema)**: 사용자나 프로그래머 입장에서 필요한 논리적 구조.
* **개념 스키마 (Conceptual Schema)**: 전체적인 논리적 구조, 개체 간 관계/제약조건, 보안/무결성 규칙.
* **내부 스키마 (Internal Schema)**: 물리적 저장장치 입장에서 본 구조 (레코드 형식, 물리적 순서).
* **VI (Vietnamese) (Tiếng Việt):**
  * External: Góc nhìn của người dùng (User view).
  * Conceptual: Cấu trúc logic tổng thể, quan hệ, bảo mật.
  * Internal: Cấu trúc lưu trữ vật lý.
* **Example**: DB의 전체 테이블 구조는 개념 스키마, 사용자가 보는 뷰(View)는 외부 스키마, 파일 저장 방식은 내부 스키마.
* 💡 **Mẹo ghi nhớ**: Ngoài (Người dùng) - Giữa/Khái niệm (Tổng thể logic) - Trong (Lưu trữ vật lý).

Ta có thể khép mục **9. 스키마 3계층 (Three-Schema Architecture)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **14. 파레토 법칙 (Pareto Principle)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 14. 파레토 법칙 (Pareto Principle)

Từ **9. 스키마 3계층 (Three-Schema Architecture)**, ta đã có điểm tựa để bước vào **14. 파레토 법칙 (Pareto Principle)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 72/101 trước khi đi vào chi tiết.

Để đọc **14. 파레토 법칙 (Pareto Principle)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “14. 파레토 법칙 (Pareto Principle)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 소프트웨어 테스트에서 오류의 80%는 전체 모듈의 20% 내에서 발견된다는 법칙.
* **VI (Vietnamese) (Tiếng Việt):** Nguyên lý 80/20. 80% lỗi nằm trong 20% module cốt lõi.
* **Example**: 시스템에 10개의 모듈이 있다면, 대부분의 버그는 핵심 모듈 2개에 몰려있습니다.
* 💡 **Mẹo ghi nhớ**: Pareto = 80/20.

Điểm chốt của **14. 파레토 법칙 (Pareto Principle)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **18. 최악의 시간 복잡도 (Worst-case Time Complexity)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 18. 최악의 시간 복잡도 (Worst-case Time Complexity)

Ở bước 73/101, **18. 최악의 시간 복잡도 (Worst-case Time Complexity)** xuất hiện như phần tiếp nối của **14. 파레토 법칙 (Pareto Principle)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **18. 최악의 시간 복잡도 (Worst-case Time Complexity)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **O(1)**, **O(n log n)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “18. 최악의 시간 복잡도 (Worst-case Time Complexity)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **O(1)**: 입력값 크기에 관계 없이 일정. (스택 삽입/삭제).
* **O(n log n)**: n log n번 수행. (힙 정렬, 병합 정렬).
* **VI (Vietnamese) (Tiếng Việt):** Độ phức tạp thời gian. O(1) là hằng số, O(n log n) cho Heap/Merge sort.
* **Example**: 데이터가 아무리 많아도 스택의 최상단에 값을 넣는 것은 1번의 연산만 필요하므로 O(1)입니다.

Như vậy, **18. 최악의 시간 복잡도 (Worst-case Time Complexity)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **19. 클린 코드 작성 원칙 (Clean Code Principles)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 19. 클린 코드 작성 원칙 (Clean Code Principles)

Sau khi đã đặt nền bằng **18. 최악의 시간 복잡도 (Worst-case Time Complexity)**, ta chuyển sang **19. 클린 코드 작성 원칙 (Clean Code Principles)**. Đây là mắt xích 74/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **19. 클린 코드 작성 원칙 (Clean Code Principles)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **가독성 (Readability)**, **단순성 (Simplicity)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “19. 클린 코드 작성 원칙 (Clean Code Principles)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **가독성 (Readability)**: 누구든지 코드를 쉽게 읽을 수 있도록 작성.
* **단순성 (Simplicity)**: 코드를 간단하게 작성.
* **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc viết code sạch. Dễ đọc, đơn giản.
* **Example**: 변수 이름을 `a` 대신 `userCount`로 짓는 것이 가독성을 높이는 것입니다.

Ta có thể khép mục **19. 클린 코드 작성 원칙 (Clean Code Principles)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **21. 외계인 코드 (Alien Code)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 21. 외계인 코드 (Alien Code)

Từ **19. 클린 코드 작성 원칙 (Clean Code Principles)**, ta đã có điểm tựa để bước vào **21. 외계인 코드 (Alien Code)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 75/101 trước khi đi vào chi tiết.

Để đọc **21. 외계인 코드 (Alien Code)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “21. 외계인 코드 (Alien Code)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 아주 오래되거나 참고문서/개발자가 없어 유지보수 작업이 어려운 코드.
* **VI (Vietnamese) (Tiếng Việt):** Alien Code là mã nguồn quá cũ, không có tài liệu hoặc người phát triển gốc, rất khó bảo trì.
* **Example**: 20년 전에 퇴사한 직원이 주석 없이 짠 코드가 외계인 코드입니다.
* 💡 **Mẹo ghi nhớ**: Alien = Người ngoài hành tinh, đọc không hiểu gì cả.

Điểm chốt của **21. 외계인 코드 (Alien Code)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **22. 정적 분석 도구 (Static Analysis Tools)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 22. 정적 분석 도구 (Static Analysis Tools)

Ở bước 76/101, **22. 정적 분석 도구 (Static Analysis Tools)** xuất hiện như phần tiếp nối của **21. 외계인 코드 (Alien Code)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **22. 정적 분석 도구 (Static Analysis Tools)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **종류**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “22. 정적 분석 도구 (Static Analysis Tools)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 코드를 실행하지 않고(하드웨어/소프트웨어적으로) 소스 코드 품질을 분석하는 도구.
* **종류**: pmd, checkstyle, cppcheck 등.
* **VI (Vietnamese) (Tiếng Việt):** Công cụ phân tích tĩnh, phân tích source code mà không cần chạy chương trình.
* **Example**: 코딩 표준을 잘 지켰는지 검사하는 Checkstyle.

Như vậy, **22. 정적 분석 도구 (Static Analysis Tools)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **23. EAI 구축 유형 (Enterprise Application Integration Types)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 23. EAI 구축 유형 (Enterprise Application Integration Types)

Sau khi đã đặt nền bằng **22. 정적 분석 도구 (Static Analysis Tools)**, ta chuyển sang **23. EAI 구축 유형 (Enterprise Application Integration Types)**. Đây là mắt xích 77/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **23. EAI 구축 유형 (Enterprise Application Integration Types)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **Point-to-Point**, **Hub & Spoke**, **Message Bus (ESB 방식)**, **Hybrid** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “23. EAI 구축 유형 (Enterprise Application Integration Types)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **Point-to-Point**: 애플리케이션을 1:1로 직접 연결.
* **Hub & Spoke**: 단일 접점인 허브 시스템을 통해 데이터를 전송하는 중앙 집중형 방식.
* **Message Bus (ESB 방식)**: 애플리케이션 사이에 미들웨어를 두어 처리하는 방식.
* **Hybrid**: Hub & Spoke와 Message Bus의 혼합 방식.
* **VI (Vietnamese) (Tiếng Việt):** Các kiểu kiến trúc tích hợp hệ thống (EAI).
  * Point-to-Point: Nối 1-1.
  * Hub & Spoke: Tập trung qua 1 Hub trung tâm.
  * Message Bus: Dùng middleware (trục thông điệp).
  * Hybrid: Lai giữa Hub & Spoke và Message Bus.
* **Example**: 여러 부서의 시스템을 가운데 중앙 서버 하나(Hub)를 통해 연결하는 방식이 Hub & Spoke입니다.
* 💡 **Mẹo ghi nhớ**: Hub là cái trục xe đạp (trung tâm), Spoke là nan hoa (tỏa ra xung quanh).

Ta có thể khép mục **23. EAI 구축 유형 (Enterprise Application Integration Types)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **25. 트립와이어 (tripwire)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 25. 트립와이어 (tripwire)

Từ **23. EAI 구축 유형 (Enterprise Application Integration Types)**, ta đã có điểm tựa để bước vào **25. 트립와이어 (tripwire)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 78/101 trước khi đi vào chi tiết.

Để đọc **25. 트립와이어 (tripwire)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “25. 트립와이어 (tripwire)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 크래커가 침입하여 백도어를 만들어 놓거나, 설정 파일을 변경했을 때 분석하는 데이터 무결성 검사 도구.
* **VI (Vietnamese) (Tiếng Việt):** Công cụ kiểm tra tính toàn vẹn dữ liệu, phát hiện backdoor hoặc thay đổi file cấu hình.
* 💡 **Mẹo ghi nhớ**: Tripwire = Dây bẫy, chạm vào là báo động.

Điểm chốt của **25. 트립와이어 (tripwire)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **27. JSON 및 AJAX (JSON & AJAX)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 27. JSON 및 AJAX (JSON & AJAX)

Ở bước 79/101, **27. JSON 및 AJAX (JSON & AJAX)** xuất hiện như phần tiếp nối của **25. 트립와이어 (tripwire)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **27. JSON 및 AJAX (JSON & AJAX)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **JSON (JavaScript Object Notation)**, **AJAX (Asynchronous JavaScript and XML)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “27. JSON 및 AJAX (JSON & AJAX)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **JSON (JavaScript Object Notation)**: 속성-값 쌍(Attribute-Value Pairs)으로 이루어진 데이터 객체를 전달하기 위한 개방형 표준 포맷. 사람이 읽기 쉬움.
* **AJAX (Asynchronous JavaScript and XML)**: 자바스크립트를 이용한 비동기 통신 기술. 클라이언트-서버 간 XML(또는 JSON) 데이터를 교환 및 제어.
* **VI (Vietnamese) (Tiếng Việt):**
  * JSON: Định dạng dữ liệu dạng Key-Value dễ đọc.
  * AJAX: Công nghệ giao tiếp bất đồng bộ, tải dữ liệu mà không cần tải lại toàn bộ trang.
* **Example**: 좋아요 버튼을 눌렀을 때 페이지 이동 없이 하트가 채워지는 것이 AJAX 기술입니다.

Như vậy, **27. JSON 및 AJAX (JSON & AJAX)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)

Sau khi đã đặt nền bằng **27. JSON 및 AJAX (JSON & AJAX)**, ta chuyển sang **28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)**. Đây là mắt xích 80/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **연속 리스트 (Contiguous List - 예: 배열)**, **연결 리스트 (Linked List)**, **오버플로/언더플로 (Overflow/Underflow)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 앞서 배운 선형 리스트는 두 가지로 나뉩니다.
* **연속 리스트 (Contiguous List - 예: 배열)**:
  * 연속되는 기억장소에 저장. 기억장소 이용 효율 밀도가 1(가장 좋음).
  * 중간에 데이터를 삽입/삭제 시 자료의 이동이 필요(오버헤드 발생).
* **연결 리스트 (Linked List)**:
  * 임의의 기억공간에 저장하며, 포인터(링크)를 이용해 서로 연결.
  * 노드의 삽입/삭제가 용이. 순차 리스트에 비해 기억 공간 이용 효율은 낮고, 포인터를 찾는 시간 때문에 접근 속도가 느림.
  * 중간 노드가 끊어지면 다음 노드를 찾기 힘듦.
* **오버플로/언더플로 (Overflow/Underflow)**: 스택/리스트가 꽉 찬 상태에서 삽입하면 Overflow, 빈 상태에서 삭제하면 Underflow 발생.
* **VI (Vietnamese) (Tiếng Việt):**
  * Contiguous List (Mảng): Dữ liệu lưu liên tiếp. Chèn/Xóa chậm do phải dịch chuyển dữ liệu. Mật độ = 1.
  * Linked List (Danh sách liên kết): Dữ liệu lưu rải rác, nối bằng pointer. Chèn/Xóa nhanh, nhưng truy cập chậm.
* 💡 **Mẹo ghi nhớ**: Array = Nhà chung cư sát vách. Linked List = Các nhà rải rác nhưng có bản đồ chỉ đường đến nhà tiếp theo.

Ta có thể khép mục **28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **33. DBMS (데이터베이스 관리 시스템)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 33. DBMS (데이터베이스 관리 시스템)

Từ **28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)**, ta đã có điểm tựa để bước vào **33. DBMS (데이터베이스 관리 시스템)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 81/101 trước khi đi vào chi tiết.

Để đọc **33. DBMS (데이터베이스 관리 시스템)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **필수 기능 3가지**, **정의 기능 (Definition)**, **조작 기능 (Manipulation)**, **제어 기능 (Control)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “33. DBMS (데이터베이스 관리 시스템)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 사용자와 데이터베이스 사이에서 정보를 생성하고 데이터베이스를 관리해 주는 소프트웨어.
* **필수 기능 3가지**:
  * **정의 기능 (Definition)**: 데이터 형, 구조, 제약조건 등 명시.
  * **조작 기능 (Manipulation)**: 데이터 검색, 갱신, 삽입, 삭제(인터페이스 제공).
  * **제어 기능 (Control)**: 데이터 무결성 유지, 보안, 정확성 제어.
* **장점**: 데이터 중복 최소화, 독립성 보장, 일관성/무결성/보안 유지, 실시간 처리.
* **단점**: 전문가 부족, 전산화 비용 증가, 과부하 발생 시 백업/회복 어려움, 시스템 복잡.
* **VI (Vietnamese) (Tiếng Việt):** Hệ quản trị CSDL.
  * 3 chức năng: Định nghĩa (Cấu trúc), Thao tác (Thêm/Sửa/Xóa/Tìm), Điều khiển (Bảo mật, toàn vẹn).
  * Ưu điểm: Giảm trùng lặp, nhất quán. Nhược điểm: Tốn kém, phức tạp.
* **Example**: Oracle, MySQL 등이 대표적인 DBMS입니다.
* 💡 **Mẹo ghi nhớ**: Đ-T-Đ (Định nghĩa, Thao tác, Điều khiển) = D-M-C (Define, Manipulate, Control).

Điểm chốt của **33. DBMS (데이터베이스 관리 시스템)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **38. 릴리즈 노트 (Release Note)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 38. 릴리즈 노트 (Release Note)

Ở bước 82/101, **38. 릴리즈 노트 (Release Note)** xuất hiện như phần tiếp nối của **33. DBMS (데이터베이스 관리 시스템)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **38. 릴리즈 노트 (Release Note)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **항목**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “38. 릴리즈 노트 (Release Note)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 소프트웨어 배포(릴리즈) 정보를 최종 사용자와 공유하기 위한 문서 (초기/추가 배포 시 제공).
* 개발팀에서 직접 현재 시제로 정확한 완전한 정보를 기반으로 작성.
* **항목**: 머릿말(Header), 개요, 목적, 문제 요약, 재현 항목, 수정/개선 내용, 사용자 영향도, SW 지원 영향도, 면책 조항 등.
* **VI (Vietnamese) (Tiếng Việt):** Ghi chú phát hành. Chia sẻ thông tin cập nhật, lỗi đã sửa cho người dùng.
* **Example**: 앱스토어에서 앱 업데이트 시 적혀있는 "새로운 기능 및 버그 수정" 목록이 릴리즈 노트입니다.
* 💡 **Mẹo ghi nhớ**: Release Note = Nhật ký cập nhật phần mềm.

Như vậy, **38. 릴리즈 노트 (Release Note)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **핵심 110: RAM (Random Access Memory)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 핵심 110: RAM (Random Access Memory)

Sau khi đã đặt nền bằng **38. 릴리즈 노트 (Release Note)**, ta chuyển sang **핵심 110: RAM (Random Access Memory)**. Đây là mắt xích 83/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **핵심 110: RAM (Random Access Memory)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “핵심 110: RAM (Random Access Memory)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 자유롭게 읽고 쓸 수 있는 기억장치로, RWM(Read Write Memory)이라고도 한다. (Bộ nhớ có thể đọc và ghi tự do.)
- RAM에는 현재 사용중인 프로그램이나 데이터가 저장되어 있다. (Lưu trữ chương trình và dữ liệu đang được sử dụng hiện tại.)
- 전원이 꺼지면 기억된 내용이 모두 사라지는 휘발성 메모리이다. (Bộ nhớ dễ bay hơi, mất dữ liệu khi tắt nguồn.)
- 일반적으로 ‘주기억장치’ 또는 ‘메모리’라고 하면 램을 의미한다. (Thường được gọi là bộ nhớ chính hoặc đơn giản là 'bộ nhớ'.)

| 구분 (Phân loại) | DRAM (Dynamic RAM - RAM động) | SRAM (Static RAM - RAM tĩnh) |
|---|---|---|
| 구성소자 (Thành phần) | 콘덴서 (Tụ điện) | 플립플롭 (Flip-Flop) |
| 특징 (Đặc điểm) | 전하가 방전되므로 주기적인 재충전(Refresh)이 필요함 (Cần làm mới định kỳ do tụ điện bị phóng điện) | 전원이 공급되는 동안에는 기억 내용이 유지 (Giữ nội dung miễn là có nguồn) |
| 전력소모 (Tiêu thụ điện) | 적음 (Ít) | 많음 (Nhiều) |
| 접근속도 (Tốc độ) | 느림 (Chậm) | 빠름 (Nhanh) |
| 집적도 (Mật độ) | 높음 (Cao - dung lượng lớn) | 낮음 (Thấp - dung lượng nhỏ) |
| 가격 (Giá) | 저가 (Rẻ) | 고가 (Đắt) |
| 용도 (Sử dụng cho) | 일반적인 주기억장치 (Bộ nhớ chính thông thường) | 캐시 메모리 (Bộ nhớ đệm / Cache) |

- **Vietnamese Explanation:** RAM là bộ nhớ làm việc của máy tính. DRAM rẻ, dung lượng cao nhưng chậm và hay quên (phải refresh liên tục), thường dùng làm thanh RAM máy tính. SRAM đắt, dung lượng nhỏ nhưng cực nhanh, không cần refresh, dùng làm Cache trong CPU.
- **Ví dụ (Example):** SRAM giống như bộ nhớ ngắn hạn của bạn khi tính nhẩm (nhanh nhưng nhớ được ít số). DRAM giống như cuốn sổ nháp (nhớ được nhiều nhưng phải tra cứu chậm hơn, và chốc chốc phải tô lại chữ mờ - refresh).
- 💡 **Mẹo ghi nhớ (Mnemonics):** **S**RAM = **S**iêu tốc (Flip-Flop, Cache). **D**RAM = **D**ump (Đổ liên tục - Refresh, Tụ điện, RAM thường).

---

Ta có thể khép mục **핵심 110: RAM (Random Access Memory)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)

Từ **핵심 110: RAM (Random Access Memory)**, ta đã có điểm tựa để bước vào **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 84/101 trước khi đi vào chi tiết.

Để đọc **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **RAM/ROM의 용량 계산 (Tính dung lượng RAM/ROM)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### RAM/ROM의 용량 계산 (Tính dung lượng RAM/ROM)

Các ý ngay dưới **RAM/ROM의 용량 계산 (Tính dung lượng RAM/ROM)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “RAM/ROM의 용량 계산 (Tính dung lượng RAM/ROM)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 주소선 (Address Bus) số lượng quyết định số Word: Nếu có n đường thì có 2^n Word. (Liên quan đến MAR và PC).
- 데이터 버스 (Data Bus) số lượng quyết định kích thước mỗi Word. (Liên quan đến MBR và IR).
- `Dung lượng = Số Word × Kích thước Word`. Ví dụ: 7 Address lines, 8 Data lines => 2^7 × 8 Bit = 128 × 8 Bit.

Với **RAM/ROM의 용량 계산 (Tính dung lượng RAM/ROM)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **RAM/ROM의 용량 계산 (Tính dung lượng RAM/ROM)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **자기 코어 (Magnetic Core - Lõi từ)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **자기 코어 (Magnetic Core - Lõi từ)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 자기 코어 (Magnetic Core - Lõi từ)

Bây giờ ta đi vào nội dung của **자기 코어 (Magnetic Core - Lõi từ)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “자기 코어 (Magnetic Core - Lõi từ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 부피에 비해 용량이 작고 가격이 비싸 현재는 거의 사용하지 않는다. (Dung lượng nhỏ, giá đắt, ít dùng hiện nay.)
- 데이터를 읽으면 읽은 내용이 지워지는 파괴 메모리(DRO Memory)이므로, 재저장(Restoration Time) 시간이 필요하다. (Đọc xong là mất dữ liệu (Phá hủy), nên cần thời gian ghi lại.)
- Cấu tạo: 구동선(X, Y) 2개 (2 dây chọn địa chỉ), 센스 선 1개 (1 dây cảm biến trạng thái), 금지선 1개 (1 dây cấm).

- **Vietnamese Explanation:** Kích thước bộ nhớ phụ thuộc vào Address Bus (chiều dài) và Data Bus (chiều rộng). Lõi từ là công nghệ cổ, đọc xong bị mất dữ liệu nên phải tốn thời gian khôi phục, hiện không còn dùng.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 자기 코어 (Magnetic Core) = Đọc là Mất (DRO), Cần ghi lại. 4 dây = 2 X/Y + 1 Sense + 1 Inhibit.

---

Với **자기 코어 (Magnetic Core - Lõi từ)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **자기 코어 (Magnetic Core - Lõi từ)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)

Ở bước 85/101, **핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)** xuất hiện như phần tiếp nối của **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **보조기억장치 (Bộ nhớ phụ)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **보조기억장치 (Bộ nhớ phụ)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 보조기억장치 (Bộ nhớ phụ)

Bây giờ ta đi vào nội dung của **보조기억장치 (Bộ nhớ phụ)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “보조기억장치 (Bộ nhớ phụ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 주기억장치에 비해 속도는 느리지만 저장 용량이 크다. 전원이 차단되어도 내용이 그대로 유지된다. (Chậm hơn RAM nhưng dung lượng lớn, lưu trữ vĩnh viễn.)
- **자기 테이프 (Magnetic Tape - Băng từ):**
  - 순차처리(SASD)만 할 수 있는 대용량 저장매체. (Chỉ truy cập tuần tự, không nhảy cóc được.)
  - 자료의 백업용으로 많이 사용함. (Thường dùng để Backup.)
- **자기 디스크 (Magnetic Disk - Đĩa từ / HDD):**
  - 순차, 비순차(직접) 처리가 모두 가능한 DASD 방식. (Có thể truy cập trực tiếp ngẫu nhiên.)
  - **Track (Rãnh):** Vòng tròn đồng tâm.
  - **Sector (Cung):** Track chia nhỏ, là đơn vị lưu trữ cơ bản.
  - **Cylinder (Trụ):** Tập hợp các track cùng vị trí trên các mặt đĩa.

Các bullet của **보조기억장치 (Bộ nhớ phụ)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **보조기억장치 (Bộ nhớ phụ)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **디스크의 Access Time (Thời gian truy cập đĩa)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **디스크의 Access Time (Thời gian truy cập đĩa)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 디스크의 Access Time (Thời gian truy cập đĩa)

Phần nguồn của **디스크의 Access Time (Thời gian truy cập đĩa)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “디스크의 Access Time (Thời gian truy cập đĩa)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `Access Time = Seek Time + Latency Time (Rotational Delay) + Transmission Time`
- **Seek Time (Thời gian tìm rãnh):** Đầu đọc di chuyển đến đúng Track.
- **Latency Time (Thời gian chờ xoay):** Đợi đĩa xoay đúng đến Sector cần đọc.
- **Transmission Time (Thời gian truyền):** Đọc Sector và truyền vào RAM.

- **Vietnamese Explanation:** Tape giống như băng cassette (muốn nghe bài 5 phải tua qua bài 1,2,3,4). Disk giống như đĩa CD hoặc đĩa than, bạn có thể đặt kim đọc vào bất kỳ bài nào (DASD).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Công thức tìm ổ cứng: SLT. **S**eek (Tìm Track) -> **L**atency (Đợi Sector xoay tới) -> **T**ransmission (Truyền đi).

---

Với **디스크의 Access Time (Thời gian truy cập đĩa)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **디스크의 Access Time (Thời gian truy cập đĩa)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **핵심 115 & 116: 연관 기억장치 및 메모리 인터리빙 (Associative Memory & Memory Interleaving)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 핵심 115 & 116: 연관 기억장치 및 메모리 인터리빙 (Associative Memory & Memory Interleaving)

Sau khi đã đặt nền bằng **핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)**, ta chuyển sang **핵심 115 & 116: 연관 기억장치 및 메모리 인터리빙 (Associative Memory & Memory Interleaving)**. Đây là mắt xích 86/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **핵심 115 & 116: 연관 기억장치 및 메모리 인터리빙 (Associative Memory & Memory Interleaving)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **연관 기억장치 (Associative Memory / CAM)**. Hãy xác định **연관 기억장치 (Associative Memory / CAM)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 연관 기억장치 (Associative Memory / CAM)

Phần nguồn của **연관 기억장치 (Associative Memory / CAM)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “연관 기억장치 (Associative Memory / CAM)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 주소에 의해 접근하지 않고, 기억된 내용의 일부를 이용하여 접근할 수 있는 기억장치. (Không tìm bằng Địa chỉ, mà tìm bằng Nội dung - Content Addressable Memory.)
- 정보 검색이 신속하다. (Tìm kiếm thông tin cực nhanh.)
- 캐시 메모리나 가상 메모리 매핑 테이블에 사용된다. (Dùng trong Cache hoặc Bảng ánh xạ bộ nhớ ảo.)
- 하드웨어 비용이 증가한다. (Tốn kém phần cứng vì cần mạch so sánh song song.)

Các bullet của **연관 기억장치 (Associative Memory / CAM)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **연관 기억장치 (Associative Memory / CAM)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **메모리 인터리빙 (Memory Interleaving)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **메모리 인터리빙 (Memory Interleaving)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 메모리 인터리빙 (Memory Interleaving)

Các ý ngay dưới **메모리 인터리빙 (Memory Interleaving)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “메모리 인터리빙 (Memory Interleaving)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- CPU가 각 모듈로 전송할 주소를 교대로 분산 배치한 후 차례대로 전송하여 여러 모듈을 병행 접근하는 기법. (Kỹ thuật phân tán địa chỉ bộ nhớ thành nhiều module độc lập để CPU truy cập song song cùng lúc.)
- 캐시 기억장치, 고속 DMA 전송 등에서 많이 사용된다. (Dùng trong Cache và DMA tốc độ cao.)

- **Vietnamese Explanation:** Associative Memory giống như việc bạn gọi "Ai tên Nam đứng lên!" thay vì hỏi "Học sinh số báo danh 10 tên gì?". Nhanh nhưng tốn kém (ai cũng phải tự vểnh tai nghe). Interleaving giống như có 4 làn thu phí thay vì 1 làn, xe cộ (dữ liệu) sẽ phân tán đi qua 4 làn cùng lúc, giảm tắc nghẽn.
- 💡 **Mẹo ghi nhớ (Mnemonics):** CAM (Content) = Tìm bằng Nội dung. Interleaving (Xen kẽ) = Đa Module, Truy cập song song.

---

Với **메모리 인터리빙 (Memory Interleaving)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **메모리 인터리빙 (Memory Interleaving)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **핵심 115 & 116: 연관 기억장치 및 메모리 인터리빙 (Associative Memory & Memory Interleaving)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **핵심 117: 캐시 메모리 (Cache Memory)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 핵심 117: 캐시 메모리 (Cache Memory)

Từ **핵심 115 & 116: 연관 기억장치 및 메모리 인터리빙 (Associative Memory & Memory Interleaving)**, ta đã có điểm tựa để bước vào **핵심 117: 캐시 메모리 (Cache Memory)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 87/101 trước khi đi vào chi tiết.

Để đọc **핵심 117: 캐시 메모리 (Cache Memory)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “핵심 117: 캐시 메모리 (Cache Memory)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- CPU의 속도와 메모리의 속도 차이를 줄이기 위해 사용하는 고속 Buffer Memory. (Bộ đệm tốc độ cao giảm chênh lệch tốc độ giữa CPU và RAM.)
- 캐시 메모리는 메모리 계층 구조에서 가장 빠른 소자 (Nhanh nhất trong hệ thống phân cấp bên ngoài register, dùng SRAM.)
- `적중률 (Hit Ratio) = 적중 횟수(Hits) / 총 접근 횟수 (Total Accesses)`

Để không đọc **매핑 프로세스 (Mapping Process)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 매핑 프로세스 (Mapping Process)

Các ý ngay dưới **매핑 프로세스 (Mapping Process)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “매핑 프로세스 (Mapping Process)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 주기억장치로부터 캐시 메모리로 데이터를 전송하는 방법 (Cách ánh xạ RAM vào Cache.)
- 종류: 직접(Direct) 매핑, 어소시에이티브(Associative) 매핑, 세트-어소시에이티브(Set-Associative) 매핑.

Các bullet của **매핑 프로세스 (Mapping Process)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **매핑 프로세스 (Mapping Process)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **쓰기 정책 (Write Policy)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **쓰기 정책 (Write Policy)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 쓰기 정책 (Write Policy)

Bây giờ ta đi vào nội dung của **쓰기 정책 (Write Policy)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “쓰기 정책 (Write Policy)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 캐시에 저장되어 있는 데이터에 수정이 발생했을 때 주기억장치에 갱신하는 시기와 방법. (Khi Cache bị thay đổi, khi nào thì ghi lại vào RAM?)
- **Write-Through:** 쓰기 동작이 이루어질 때마다 캐시와 주기억장치를 동시에 갱신. (Ghi đồng thời cả 2, an toàn nhưng chậm.)
- **Write-Back:** 캐시로부터 제거될 때 주기억장치에 복사. (Chỉ ghi vào RAM khi bị đuổi khỏi Cache, nhanh nhưng rủi ro nếu mất điện.)

- **Vietnamese Explanation:** Cache giống như cái ví tiền lẻ (SRAM) bạn để túi quần. RAM là két sắt (DRAM) ở nhà. Lấy tiền lẻ nhanh hơn về nhà mở két.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Write-Through (Xuyên qua) = Ghi luôn vào RAM (Chậm, Chắc). Write-Back (Ghi lại sau) = Khi nào dọn Cache mới ghi (Nhanh, Nguy hiểm).

---

Với **쓰기 정책 (Write Policy)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **쓰기 정책 (Write Policy)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **핵심 117: 캐시 메모리 (Cache Memory)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **핵심 118: 가상 기억장치 (Virtual Memory)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 핵심 118: 가상 기억장치 (Virtual Memory)

Ở bước 88/101, **핵심 118: 가상 기억장치 (Virtual Memory)** xuất hiện như phần tiếp nối của **핵심 117: 캐시 메모리 (Cache Memory)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **핵심 118: 가상 기억장치 (Virtual Memory)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “핵심 118: 가상 기억장치 (Virtual Memory)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 기억 용량이 작은 주기억장치를 마치 큰 용량을 가진 것처럼 사용할 수 있도록 하는 운영체제의 메모리 운영 기법. (Lấy một phần ổ cứng ảo hóa thành RAM, giúp máy tính chạy được các chương trình nặng hơn dung lượng RAM thực tế.)
- 보조기억장치는 디스크 같은 DASD 장치이어야 한다. (Bắt buộc dùng đĩa từ / HDD / SSD - DASD, không dùng băng từ được.)
- **주소의 사용 (Địa chỉ):**
  - **가상 주소 (Virtual Address):** Địa chỉ ảo trên ổ cứng. Đơn vị thay thế là Page (Trang).
  - **실기억 주소 (Physical Address):** Địa chỉ thực trên RAM. Đơn vị thay thế là Block / Frame.
- **페이지 부재 (Page Fault):** 가상 페이지가 주기억장치에 없는 경우. 프로그램 수행이 중단된다. (Khi dữ liệu cần tìm không có trong RAM mà nằm trên đĩa, CPU phải tạm dừng để lấy vào.)
- **주소 매핑 (Address Mapping):** 가상주소를 실기억주소로 변환하는 작업이다. 사상함수가 사용된다. (Đổi địa chỉ Ảo thành địa chỉ Thực qua hàm ánh xạ.)

- **Vietnamese Explanation:** Khi RAM 4GB nhưng game nặng 10GB, HĐH dùng ổ cứng làm RAM ảo. RAM ảo chia thành các "Trang" (Page). Khi CPU cần 1 trang mà nó chưa nằm trong RAM thực, nó bị "Page Fault", máy sẽ hơi khựng lại để tải từ ổ cứng lên.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Virtual = Đĩa cứng đóng giả làm RAM. Page Fault (Lỗi trang) = Trang chưa nạp, phải đợi.

---

Như vậy, **핵심 118: 가상 기억장치 (Virtual Memory)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)

Sau khi đã đặt nền bằng **핵심 118: 가상 기억장치 (Virtual Memory)**, ta chuyển sang **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)**. Đây là mắt xích 89/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **플린(Flynn)의 분류 (Phân loại Flynn)**. Hãy xác định **플린(Flynn)의 분류 (Phân loại Flynn)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 플린(Flynn)의 분류 (Phân loại Flynn)

Phần nguồn của **플린(Flynn)의 분류 (Phân loại Flynn)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “플린(Flynn)의 분류 (Phân loại Flynn)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **SISD (Single Instruction, Single Data):** 1 Lệnh xử lý 1 Dữ liệu. (Máy tính truyền thống Von Neumann).
- **SIMD (Single Instruction, Multi Data):** 1 Lệnh xử lý Nhiều Dữ liệu. (Array Processor, xử lý đồng bộ).
- **MISD (Multi Instruction, Single Data):** Nhiều Lệnh, 1 Dữ liệu. (Không dùng trong thực tế).
- **MIMD (Multi Instruction, Multi Data):** Nhiều Lệnh xử lý Nhiều Dữ liệu. (Máy đa nhân hiện đại - Đa xử lý bất đồng bộ). Tightly Coupled (Multiprocessor), Loosely Coupled (Distributed).

Các bullet của **플린(Flynn)의 분류 (Phân loại Flynn)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **플린(Flynn)의 분류 (Phân loại Flynn)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **병렬처리기법 (Kỹ thuật xử lý song song)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **병렬처리기법 (Kỹ thuật xử lý song song)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 병렬처리기법 (Kỹ thuật xử lý song song)

Các ý ngay dưới **병렬처리기법 (Kỹ thuật xử lý song song)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “병렬처리기법 (Kỹ thuật xử lý song song)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **파이프라인 프로세서 (Pipeline):** Chia lệnh thành các Sub-task (như dây chuyền nhà máy). Các bước: Fetch, Decode, Operand, Execute.
- **벡터 프로세서 (Vector Processor):** Xử lý mảng dữ liệu cực nhanh (Systolic algorithm).
- **배열 프로세서 (Array Processor):** Có nhiều bộ ALU (Processing Elements), điều khiển tập trung, tính toán song song theo không gian (SIMD).
- **데이터 흐름 컴퓨터 (Data Flow Computer):** Ngược với Von Neumann (Control-flow). Lệnh không chạy theo thứ tự PC, mà cứ hễ **đủ Dữ liệu là chạy** (Không cần Program Counter).

- **Vietnamese Explanation:** SISD là làm việc một mình. SIMD là 1 ông chủ ra lệnh cho 10 người cùng làm. MIMD là 10 người tự làm 10 việc khác nhau. Data Flow là cách làm việc "không cần quản lý", ai có đủ nguyên liệu thì tự động nấu, không cần chờ sếp hô hào.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Flynn: S = Single (Đơn), M = Multi (Đa), I = Instruction (Lệnh), D = Data (Dữ liệu). Data Flow = Data dẫn dắt, Không cần PC.

---

# [과목 2] 소프트웨어 개발 (Subject 2: Software Development)

Với **병렬처리기법 (Kỹ thuật xử lý song song)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **병렬처리기법 (Kỹ thuật xử lý song song)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)

Từ **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)**, ta đã có điểm tựa để bước vào **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 90/101 trước khi đi vào chi tiết.

Để đọc **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

자료구조: 컴퓨터상 자료를 효율적으로 저장하기 위해 만들어진 논리적인 구조 (Cấu trúc logic để lưu trữ dữ liệu hiệu quả).

Để không đọc **선형 구조 (Linear - Nối tiếp nhau)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 선형 구조 (Linear - Nối tiếp nhau)

Các ý ngay dưới **선형 구조 (Linear - Nối tiếp nhau)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “선형 구조 (Linear - Nối tiếp nhau)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **리스트 (List):** 순서에 의해 나열된 구조. (Cấu trúc tuyến tính).
  - **선형 리스트 (Linear List / Array):** Kích thước cố định (고정), lưu liên tục (연속). Tìm kiếm cực nhanh (검색 빠름), nhưng chèn/xóa cực chậm (삽입, 삭제 느림).
  - **연결 리스트 (Linked List):** Kích thước linh hoạt (가변), liên kết bằng Pointer. Chèn/xóa cực nhanh, nhưng tìm kiếm chậm (phải dò từng cái) và tốn không gian lưu Pointer.
- **스택 (Stack):** LIFO (Last-In-First-Out). Vào/Ra ở một đầu. Dùng cho: Gọi hàm (Subroutine), Lưu địa chỉ trở về, Đệ quy (Recursion), Tính biểu thức toán học, DFS (Duyệt sâu).
- **큐 (Queue):** FIFO (First-In-First-Out). Vào một đầu, ra một đầu. Dùng cho: Lập lịch hệ điều hành (Job Scheduling), Hàng đợi in.
- **데크 (Deque):** Kết hợp Stack và Queue, có thể Vào/Ra ở CẢ HAI đầu.

Các bullet của **선형 구조 (Linear - Nối tiếp nhau)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **선형 구조 (Linear - Nối tiếp nhau)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **비선형 구조 (Non-linear - Không nối tiếp)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **비선형 구조 (Non-linear - Không nối tiếp)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 비선형 구조 (Non-linear - Không nối tiếp)

Bây giờ ta đi vào nội dung của **비선형 구조 (Non-linear - Không nối tiếp)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “비선형 구조 (Non-linear - Không nối tiếp)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **트리 (Tree):** Cây. Có Node (Đỉnh) và Branch (Nhánh). **Không có chu trình (Cycle).**
- **그래프 (Graph):** Đồ thị. Có Đỉnh (Vertex) và Cạnh (Edge). Có thể có hướng hoặc vô hướng. (Cây là một dạng Đồ thị không có chu trình).

- **Vietnamese Explanation:** Cấu trúc dữ liệu là cách sắp xếp thông tin.
  - Linear List như dãy ghế đá (tìm số ghế thì nhanh, nhưng muốn chen vào giữa phải bắt mọi người xích ra).
  - Linked List như trò chơi nắm tay nhau (muốn chen vào giữa chỉ cần thả tay và nắm người mới, rất dễ, nhưng tìm người thứ 10 thì phải đếm từ đầu).
  - Stack như hộp bóng bàn (LIFO - vứt vào sau thì lấy ra trước). Queue như xếp hàng mua vé (FIFO - ai đến trước mua trước).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Stack = LIFO (Gọi Hàm, Đệ quy). Queue = FIFO (Lập lịch). Liên kết (Linked) = Nhanh chèn/xóa, Chậm tìm kiếm.

---

Với **비선형 구조 (Non-linear - Không nối tiếp)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **비선형 구조 (Non-linear - Không nối tiếp)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)

Ở bước 91/101, **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)** xuất hiện như phần tiếp nối của **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)

Bây giờ ta đi vào nội dung của **알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **분할과 정복 (Divide & Conquer):** Chia để trị. Chia nhỏ vấn đề đến khi không chia được nữa rồi gộp lại. (VD: Merge Sort, Quick Sort).
- **동적계획법 (Dynamic Programming - Quy hoạch động):** Chia bài toán, nhưng CÓ lưu lại kết quả (bộ nhớ) để tận dụng cho lần sau. (VD: Fibonacci).
- **탐욕법 (Greedy):** Tham lam. Chọn cái tốt nhất ở *ngay thời điểm hiện tại*, không cần biết tương lai.
- **백트래킹 (Backtracking):** Quay lui. Đi thử, nếu thấy bế tắc (không triển vọng - promising) thì quay lại nút cha.

Các bullet của **알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **시간 복잡도 (Time Complexity - Độ phức tạp thời gian)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **시간 복잡도 (Time Complexity - Độ phức tạp thời gian)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 시간 복잡도 (Time Complexity - Độ phức tạp thời gian)

Phần nguồn của **시간 복잡도 (Time Complexity - Độ phức tạp thời gian)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “시간 복잡도 (Time Complexity - Độ phức tạp thời gian)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Đếm số lần thực thi các phép toán (không phải tính thời gian bằng giây).
- Ký hiệu tiệm cận: Big-O là cận trên, Omega là cận dưới, Theta là cận chặt; chúng không tự động đồng nghĩa với lần lượt 최악/평균/최상. Khi đề bài nói rõ worst/best case thì mới gắn với trường hợp đó.
- **Thứ tự (Nhanh -> Chậm):** O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
- O(1) nghĩa là: Dữ liệu lớn đến đâu thời gian vẫn không đổi.

- **Vietnamese Explanation:** Greedy giống như đi nhặt tiền: cứ thấy tờ to nhất trước mặt là nhặt, bất chấp sau đó dẫn vào ngõ cụt. Dynamic Programming giống như làm toán: kết quả bài 1 lưu ra nháp để dùng cho bài 2.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Divide = Cắt nhỏ. Dynamic = Nhớ bài cũ. Greedy = Tham bát bỏ mâm. Backtrack = Đi lùi. O(1) là nhanh nhất.

---

Với **시간 복잡도 (Time Complexity - Độ phức tạp thời gian)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **시간 복잡도 (Time Complexity - Độ phức tạp thời gian)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)

Sau khi đã đặt nền bằng **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**, ta chuyển sang **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**. Đây là mắt xích 92/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **재사용 (Reuse):** 이미 개발되어 인정받았던 소프트웨어의 전체 또는 일부분을 다시 사용하는 기법. (Sử dụng lại code/phần mềm cũ đã được kiểm chứng để tiết kiệm thời gian, chi phí và giảm lỗi.)
- **Phân loại theo kỹ thuật:**
  - **분석 (Analysis):** Hiểu code cũ để chọn cái cần tái sử dụng.
  - **재구조 (Restructuring):** Đổi cấu trúc, không đổi chức năng.

---

Ta có thể khép mục **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **088-2: 데이터베이스 (Database) & 089: DBMS**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 088-2: 데이터베이스 (Database) & 089: DBMS

Từ **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**, ta đã có điểm tựa để bước vào **088-2: 데이터베이스 (Database) & 089: DBMS**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 93/101 trước khi đi vào chi tiết.

Để đọc **088-2: 데이터베이스 (Database) & 089: DBMS** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **데이터베이스의 4가지 특징 (ISOS - 4 Đặc trưng của DB)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 데이터베이스의 4가지 특징 (ISOS - 4 Đặc trưng của DB)

Các ý ngay dưới **데이터베이스의 4가지 특징 (ISOS - 4 Đặc trưng của DB)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “데이터베이스의 4가지 특징 (ISOS - 4 Đặc trưng của DB)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **통합된 데이터 (Integrated Data):** 중복 배제 (Không trùng lặp).
- **저장된 데이터 (Stored Data):** 저장 매체에 저장 (Lưu trên máy tính).
- **운영 데이터 (Operational Data):** 반드시 필요한 고유 업무 자료 (Dữ liệu bắt buộc phải có để tổ chức hoạt động, không phải rác).
- **공용 데이터 (Shared Data):** 공동으로 소유 (Nhiều người/app dùng chung).

Các bullet của **데이터베이스의 4가지 특징 (ISOS - 4 Đặc trưng của DB)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **데이터베이스의 4가지 특징 (ISOS - 4 Đặc trưng của DB)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **DBMS (Database Management System)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **DBMS (Database Management System)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### DBMS (Database Management System)

Bây giờ ta đi vào nội dung của **DBMS (Database Management System)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “DBMS (Database Management System)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 소프트웨어 (Là phần mềm quản lý DB, ví dụ: MySQL, Oracle).
- **3대 기능 (3 Chức năng chính):**
  - **정의 (Definition / DDL):** Tạo cấu trúc, bảng (Table).
  - **조작 (Manipulation / DML):** Thêm, sửa, xóa, tìm kiếm (CRUD).
  - **제어 (Control / DCL):** Bảo mật, phân quyền, tính toàn vẹn.

- 💡 **Mẹo ghi nhớ (Mnemonics):** ISOS (Integrated, Stored, Operational, Shared) - Nhớ chữ O = Operational (Vận hành/Thiết yếu). DBMS có 3 chữ D-M-C (Định nghĩa, Thao tác, Điều khiển).

---

Với **DBMS (Database Management System)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **DBMS (Database Management System)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **088-2: 데이터베이스 (Database) & 089: DBMS** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **090-1: 데이터의 독립성 (Data Independence)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 090-1: 데이터의 독립성 (Data Independence)

Ở bước 94/101, **090-1: 데이터의 독립성 (Data Independence)** xuất hiện như phần tiếp nối của **088-2: 데이터베이스 (Database) & 089: DBMS**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **090-1: 데이터의 독립성 (Data Independence)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “090-1: 데이터의 독립성 (Data Independence)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **논리적 독립성 (Logical):** Đổi cấu trúc logic (Thêm/xóa cột) nhưng App đang chạy không bị sập.
- **물리적 독립성 (Physical):** Đổi ổ cứng (Sang SSD, đổi server) nhưng App vẫn chạy bình thường.

---

Như vậy, **090-1: 데이터의 독립성 (Data Independence)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **091: 스키마 (Schema)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 091: 스키마 (Schema)

Sau khi đã đặt nền bằng **090-1: 데이터의 독립성 (Data Independence)**, ta chuyển sang **091: 스키마 (Schema)**. Đây là mắt xích 95/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **091: 스키마 (Schema)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

스키마 là bộ khung (Cấu trúc, ràng buộc) của Database. Có 3 góc nhìn:
- **외부 스키마 (External Schema):** User view. (User nhìn thấy gì, vd: Màn hình nhân viên chỉ thấy Lương của mình).
- **개념 스키마 (Conceptual Schema):** DB Admin view. (Toàn bộ logic, cấu trúc của doanh nghiệp. Thường gọi tắt là "Schema").
- **내부 스키마 (Internal Schema):** System view. (Cấu trúc vật lý, lưu trên đĩa như thế nào).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Ngoại (User/App) - Khái niệm (Toàn cục/Admin) - Nội (Máy móc/Ổ cứng).

---

Ta có thể khép mục **091: 스키마 (Schema)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **091-1: 절차형 SQL (Procedural SQL)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 091-1: 절차형 SQL (Procedural SQL)

Từ **091: 스키마 (Schema)**, ta đã có điểm tựa để bước vào **091-1: 절차형 SQL (Procedural SQL)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 96/101 trước khi đi vào chi tiết.

Để đọc **091-1: 절차형 SQL (Procedural SQL)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

C, JAVA처럼 분기/반복 (If/For)이 가능한 SQL (SQL có thêm logic lập trình - PL/SQL). Bọc trong khối `BEGIN ~ END`.

| 종류 (Loại) | 특징 (Đặc điểm) | ví dụ (Ví dụ sử dụng) |
|---|---|---|
| **프로시저 (Procedure)** | Gọi thủ công (`CALL`). Thực thi một chuỗi nghiệp vụ (Insert/Update nhiều bảng). KHÔNG có `RETURN`. | Chuyển tiền (Trừ A, Cộng B). |
| **트리거 (Trigger)** | Tự động chạy khi có sự kiện (Insert/Update/Delete). KHÔNG thể gọi thủ công. | Tự động ghi log khi có người xóa dữ liệu, tự trừ số lượng kho khi có đơn hàng. |
| **사용자 정의 함수 (User Defined Function)** | Dùng trong câu `SELECT`. BẮT BUỘC có `RETURN` 1 giá trị. | Hàm tính thuế VAT 10% từ giá gốc. |

- **Vietnamese Explanation:** SQL bình thường rất phèn, chỉ biết lấy dữ liệu ra. Procedural SQL thông minh hơn. Procedure như một cuốn kịch bản bạn bắt nó diễn. Trigger như cái bẫy chuột, có chuột (sự kiện) là tự sập. Function giống hệt hàm trong Toán học, đưa X trả về Y.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Procedure = Gọi mới chạy. Trigger = Tự động (Event). Function = Trả về giá trị (Return).

Để không đọc **절차형 SQL의 테스트와 디버깅 (Testing & Debugging Procedural SQL)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 절차형 SQL의 테스트와 디버깅 (Testing & Debugging Procedural SQL)

Các ý ngay dưới **절차형 SQL의 테스트와 디버깅 (Testing & Debugging Procedural SQL)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “절차형 SQL의 테스트와 디버깅 (Testing & Debugging Procedural SQL)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 절차형 SQL은 DBMS 내부에서 직접 실행되므로, 애플리케이션과 DB 사이의 데이터 전송량을 줄일 수 있어 효율적임. (Chạy trực tiếp trong DBMS nên giảm nghẽn mạng).
- **Quy trình Test & Debug:** `CREATE` (Biên dịch) -> Sửa lỗi cú pháp -> Comment các lệnh `INSERT/UPDATE/DELETE` (Tránh làm hỏng DB thật) -> Dùng `DBMS_OUTPUT` in giá trị ra màn hình để kiểm tra -> `EXEC / CALL` -> Xác nhận kết quả.

---

Các bullet của **절차형 SQL의 테스트와 디버깅 (Testing & Debugging Procedural SQL)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **절차형 SQL의 테스트와 디버깅 (Testing & Debugging Procedural SQL)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **091-1: 절차형 SQL (Procedural SQL)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)

Ở bước 97/101, **097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)** xuất hiện như phần tiếp nối của **091-1: 절차형 SQL (Procedural SQL)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 코딩, 디버그, 컴파일, 배포 등 모든 작업을 하나의 프로그램에서 처리. (Phần mềm tất-cả-trong-một).
- **4대 기능 (4 Chức năng chính):**
  - 코딩 (Coding): Gõ code.
  - 컴파일 (Compile): Dịch ra mã máy.
  - 디버깅 (Debugging): Tìm và sửa lỗi (Bug).
  - 배포 (Deployment): Đóng gói và giao cho người dùng.
- **대표 도구 (Các IDE tiêu biểu):**
  - **이클립스 (Eclipse):** Của IBM, Đa nền tảng (Cross-platform), chuyên Java.
  - **IntelliJ (IDEA):** Của JetBrains, Đa nền tảng, chuyên Java/Kotlin.
  - **비주얼 스튜디오 (Visual Studio):** Của Microsoft, chuyên Windows, C#/.NET.
  - **엑스 코드 (Xcode):** Của Apple, chuyên MacOS/iOS.
  - **안드로이드 스튜디오 (Android Studio):** Của Google, chuyên Android.

---

Như vậy, **097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **098 & 기타 협업 도구 (Build Tools & Collaboration Tools)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 098 & 기타 협업 도구 (Build Tools & Collaboration Tools)

Sau khi đã đặt nền bằng **097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)**, ta chuyển sang **098 & 기타 협업 도구 (Build Tools & Collaboration Tools)**. Đây là mắt xích 98/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **098 & 기타 협업 도구 (Build Tools & Collaboration Tools)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **빌드 도구 (Build Tool)**. Hãy xác định **빌드 도구 (Build Tool)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 빌드 도구 (Build Tool)

Phần nguồn của **빌드 도구 (Build Tool)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “빌드 도구 (Build Tool)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 소스 코드를 실행할 수 있는 제품으로 변환(빌드)하는 과정을 자동화. (Công cụ tự động biên dịch và gom file code lại thành file chạy `.exe`, `.apk`...).
- **Ant:** Cổ điển, dùng cho Java, của Apache.
- **Maven:** Nâng cấp của Ant, quản lý thư viện (Dependencies) tự động.
- **Gradle:** Hiện đại nhất, lai giữa Ant và Maven, dùng nhiều cho Android.

Các bullet của **빌드 도구 (Build Tool)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **빌드 도구 (Build Tool)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **기타 협업 도구 (Groupware / Collaboration Tools)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **기타 협업 도구 (Groupware / Collaboration Tools)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 기타 협업 도구 (Groupware / Collaboration Tools)

Các ý ngay dưới **기타 협업 도구 (Groupware / Collaboration Tools)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “기타 협업 도구 (Groupware / Collaboration Tools)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **프로젝트 및 일정 관리 (Quản lý dự án):** Jira (지라), Trello, Google Calendar.
- **메신저 (Giao tiếp):** Slack, Jandi.
- **디자인 (Thiết kế UI -> Code):** Zeplin, Sketch.
- **기타:** Evernote (Ghi chú), Swagger (Tài liệu API tự động), GitHub (Lưu source code).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Jira = Quản lý công việc (Ticket). Slack = Chat. Zeplin = Thiết kế. Swagger = Viết Document cho API. Gradle = Build Android.

---

Với **기타 협업 도구 (Groupware / Collaboration Tools)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **기타 협업 도구 (Groupware / Collaboration Tools)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **098 & 기타 협업 도구 (Build Tools & Collaboration Tools)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **104-1 ~ 108: 소프트웨어 매뉴얼 (Software Manuals)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 104-1 ~ 108: 소프트웨어 매뉴얼 (Software Manuals)

Từ **098 & 기타 협업 도구 (Build Tools & Collaboration Tools)**, ta đã có điểm tựa để bước vào **104-1 ~ 108: 소프트웨어 매뉴얼 (Software Manuals)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 99/101 trước khi đi vào chi tiết.

Để đọc **104-1 ~ 108: 소프트웨어 매뉴얼 (Software Manuals)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **설치 매뉴얼 (Installation Manual - Hướng dẫn cài đặt)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 설치 매뉴얼 (Installation Manual - Hướng dẫn cài đặt)

Các ý ngay dưới **설치 매뉴얼 (Installation Manual - Hướng dẫn cài đặt)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “설치 매뉴얼 (Installation Manual - Hướng dẫn cài đặt)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **사용자 기준 (Góc nhìn người dùng):** Viết cho khách hàng, không phải cho Dev.
- **순서대로 (Theo trình tự):** Từ lúc bấm Next đến lúc Finish.
- **예외 상황 / 오류 메시지:** Phải có cách xử lý khi cài đặt bị lỗi.
- **Uninstall (Xóa cài đặt):** Bắt buộc phải hướng dẫn cách gỡ cài đặt sạch sẽ.
- **서문 (Lời nói đầu) bao gồm:**
  - 문서 이력 (Lịch sử chỉnh sửa v1.0, v1.1).
  - 주석 (Chú ý/Tham khảo).
  - 설치 환경 체크 (Kiểm tra OS, tắt app khác trước khi cài).

Các bullet của **설치 매뉴얼 (Installation Manual - Hướng dẫn cài đặt)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **설치 매뉴얼 (Installation Manual - Hướng dẫn cài đặt)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **사용자 매뉴얼 (User Manual - Hướng dẫn sử dụng)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **사용자 매뉴얼 (User Manual - Hướng dẫn sử dụng)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 사용자 매뉴얼 (User Manual - Hướng dẫn sử dụng)

Bây giờ ta đi vào nội dung của **사용자 매뉴얼 (User Manual - Hướng dẫn sử dụng)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “사용자 매뉴얼 (User Manual - Hướng dẫn sử dụng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **컴포넌트 단위 (Theo từng Component):** Chia nhỏ theo từng tính năng (Ví dụ: Hướng dẫn riêng cho Word, Excel).
- **버전 관리 (Quản lý phiên bản):** App update tính năng thì Manual cũng phải update theo.
- **시각 자료 (Hình ảnh):** Bắt buộc phải có hình chụp màn hình UI để dễ hiểu.

---

Các ý về **사용자 매뉴얼 (User Manual - Hướng dẫn sử dụng)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Điểm chốt của **사용자 매뉴얼 (User Manual - Hướng dẫn sử dụng)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **104-1 ~ 108: 소프트웨어 매뉴얼 (Software Manuals)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)

Ở bước 100/101, **113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)** xuất hiện như phần tiếp nối của **104-1 ~ 108: 소프트웨어 매뉴얼 (Software Manuals)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 방식 (Cách thức) | 특징 (Đặc điểm) | 대표 도구 (Công cụ) |
|---|---|---|
| **공유 폴더 (Shared Folder)** | Copy đè file vào 1 folder dùng chung trên mạng Lan. Dễ mất dữ liệu. | SCCS, RCS, PVCS |
| **클라이언트/서버 (Client/Server)** | Có 1 máy Server trung tâm giữ code. Máy cá nhân (Client) lấy về sửa rồi đẩy lên. Server chết là nghỉ làm. | **CVS, SVN** (Subversion), ClearCase |
| **분산 저장소 (Distributed Repo)** | Mỗi máy cá nhân đều là 1 cái Kho thu nhỏ (Local Repo). Copy (Clone) từ Server (Remote Repo) về. Server chết vẫn làm việc bình thường ở máy cá nhân, lúc nào Server sống lại đẩy lên sau (Push). Rất an toàn. | **Git**, Mercurial, Bitkeeper |

- **Vietnamese Explanation:** SVN là kiểu "Đi mượn sách thư viện", mất thư viện là khỏi đọc. Git là kiểu "Photo cuốn sách về nhà", thư viện cháy mình vẫn còn sách đọc, sửa sách thoải mái.
- 💡 **Mẹo ghi nhớ (Mnemonics):**
  - 공유 폴더 (Share folder) = RCS, PVCS.
  - 클라이언트/서버 = CVS, SVN (Server tập trung).
  - 분산 (Phân tán) = Git.

Như vậy, **113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **120-1: 소프트웨어의 분류 (Software Classification)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 120-1: 소프트웨어의 분류 (Software Classification)

Sau khi đã đặt nền bằng **113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)**, ta chuyển sang **120-1: 소프트웨어의 분류 (Software Classification)**. Đây là mắt xích 101/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **120-1: 소프트웨어의 분류 (Software Classification)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “120-1: 소프트웨어의 분류 (Software Classification)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **상용 소프트웨어 (Commercial):** Bán lấy tiền (Product). VD: Windows, Office, Game.
- **서비스 제공 소프트웨어 (Service Provision / SI):** Làm theo đơn đặt hàng của 1 tổ chức (Dự án nội bộ). VD: Hệ thống ngân hàng.

---

Khép lại **120-1: 소프트웨어의 분류 (Software Classification)**, điều cần giữ lại là mối quan hệ giữa mục đích, cơ chế và điểm giới hạn của các khái niệm trong nguồn. Khi ôn lại, hãy tự giải thích chúng bằng một câu hoàn chỉnh rồi đối chiếu với các điểm dễ nhầm trước khi chuyển sang bài tổng hợp của môn.