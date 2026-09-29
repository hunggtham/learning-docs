# 077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **5. 수식의 표기법 변환 (Expression Notation Conversion)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

그래프, 인접, 행렬

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **026: 그래프 (Graph / Đồ thị)**에서 만든 기준을 이어받아 **077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)** và nối nó với **5. 수식의 표기법 변환 (Expression Notation Conversion)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

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