# 023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối data structures với access pattern, memory và complexity, để lựa chọn cấu trúc bắt đầu từ thao tác.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

자료구조

> **Chuyển mạch:** Ở chặng này của **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)**에서 만든 기준을 이어받아 **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**, **읽는 방법 (Cách đọc)** nêu điều cần giải thích; **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

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

> **Bàn giao:** Sau **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
