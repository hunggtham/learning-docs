# 023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

자료구조

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **54. XML 및 데이터 무결성 검사 도구 (XML & Integrity Check Tools)**에서 만든 기준을 이어받아 **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)

Sau khi đã đặt nền bằng **54. XML 및 데이터 무결성 검사 도구 (XML & Integrity Check Tools)**, ta chuyển sang **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**. Đây là mắt xích 86/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

자료구조: 컴퓨터상 자료를 효율적으로 저장하기 위해 만들어진 논리적인 구조 (Cấu trúc logic để lưu trữ dữ liệu hiệu quả).

Ta bắt đầu phần nội dung bằng **선형 구조 (Linear - Nối tiếp nhau)**. Hãy xác định **선형 구조 (Linear - Nối tiếp nhau)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 선형 구조 (Linear - Nối tiếp nhau)

Phần nguồn của **선형 구조 (Linear - Nối tiếp nhau)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **리스트 (List):** 순서에 의해 나열된 구조. (Cấu trúc tuyến tính).
  - **선형 리스트 (Linear List / Array):** Kích thước cố định (고정), lưu liên tục (연속). Tìm kiếm cực nhanh (검색 빠름), nhưng chèn/xóa cực chậm (삽입, 삭제 느림).
  - **연결 리스트 (Linked List):** Kích thước linh hoạt (가변), liên kết bằng Pointer. Chèn/xóa cực nhanh, nhưng tìm kiếm chậm (phải dò từng cái) và tốn không gian lưu Pointer.
- **스택 (Stack):** LIFO (Last-In-First-Out). Vào/Ra ở một đầu. Dùng cho: Gọi hàm (Subroutine), Lưu địa chỉ trở về, Đệ quy (Recursion), Tính biểu thức toán học, DFS (Duyệt sâu).
- **큐 (Queue):** FIFO (First-In-First-Out). Vào một đầu, ra một đầu. Dùng cho: Lập lịch hệ điều hành (Job Scheduling), Hàng đợi in.
- **데크 (Deque):** Kết hợp Stack và Queue, có thể Vào/Ra ở CẢ HAI đầu.

Các bullet của **선형 구조 (Linear - Nối tiếp nhau)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **선형 구조 (Linear - Nối tiếp nhau)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **비선형 구조 (Non-linear - Không nối tiếp)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **비선형 구조 (Non-linear - Không nối tiếp)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 비선형 구조 (Non-linear - Không nối tiếp)

Các ý ngay dưới **비선형 구조 (Non-linear - Không nối tiếp)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

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

Ta có thể khép mục **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.