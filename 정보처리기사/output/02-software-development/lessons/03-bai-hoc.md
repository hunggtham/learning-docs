# 075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối stack, queue và deque với LIFO, FIFO, access pattern và scheduling, để chọn cấu trúc theo thứ tự.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **29. 큐 (Queue)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

스택, 데크

> **Chuyển mạch:** Ở chặng này của **075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **2. 스택 (Stack) 및 응용 (Applications)**에서 만든 기준을 이어받아 **075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)**, **075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

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

> **Bàn giao:** Sau **075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
