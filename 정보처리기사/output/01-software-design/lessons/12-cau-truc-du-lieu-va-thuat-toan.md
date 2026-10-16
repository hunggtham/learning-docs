# 자료구조 및 알고리즘 (Cấu trúc dữ liệu và Thuật toán nền tảng)

## 학습 목표 (Mục tiêu)
- Nắm vững phân loại 2 nhóm cấu trúc dữ liệu cốt lõi: Cấu trúc tuyến tính (`선형 구조: 배열, 연결 리스트, 스택, 큐, 데크`) và Cấu trúc phi tuyến tính (`비선형 구조: 트리, 그래프`).
- Phân biệt tuyệt đối giữa Ngăn xếp (`스택 - Stack: LIFO / Push / Pop / Top`) và Hàng đợi (`큐 - Queue: FIFO / Enqueue / Dequeue / Front / Rear`).
- Làm chủ cấu trúc Cây (`트리`) và Cây nhị phân (`이진 트리`); thành thạo 3 phương pháp duyệt cây nhị phân kinh điển: Tiền thứ tự (`전위 순회 - Preorder`), Trung thứ tự (`중위 순회 - Inorder`), và Hậu thứ tự (`후위 순회 - Postorder`).
- Thành thạo thuật toán chuyển đổi và tính toán giá trị biểu thức số học dạng hậu tố (`후위 표기법 - Postfix`) bằng Stack.
- Phân tích và so sánh độ phức tạp thời gian $O(N)$ của các thuật toán sắp xếp kinh điển: `Bubble, Selection, Insertion, Quick, Merge, Heap Sort`.
- Làm chủ kỹ thuật Tìm kiếm nhị phân (`이진 탐색 - O(\log N)`) và Bảng băm (`해싱 - Hashing: O(1)` / Va chạm Collision / Xử lý Chaining & Open Addressing); phân tích 3 tầng chỉ mục của tập tin chỉ mục tuần tự (`ISAM`).

## 핵심 키워드 (Từ khóa)
- 선형 구조 vs 비선형 구조 (Linear vs Non-linear Data Structures)
- 스택 (Stack / LIFO / Top / Push, Pop / 오버플로, 언더플로)
- 큐 (Queue / FIFO / Front - 삭제, Rear - 삽입)
- 데크 (Deque / Double Ended Queue / 양쪽 입출력)
- 이진 트리 운행법 (Tree Traversal: 전위 Root-L-R, 중위 L-Root-R, 후위 L-R-Root)
- 수식 표기법 (Expression: 중위 Infix, 전위 Prefix, 후위 Postfix / 스택 연산)
- 정렬 알고리즘 (Sorting: 버블, 선택, 삽입 $O(N^2)$ / 퀵, 병합, 힙 $O(N \log N)$)
- 이진 검색 (Binary Search / 정렬 필수 / $O(\log N)$)
- 해싱 (Hashing / 해시 함수 / 버킷, 슬롯 / 충돌 - Collision / 체이닝, 개방 주소법)
- ISAM 파일 편성 (Indexed Sequential: 트랙, 실린더, 마스터 색인 / 기본 구역, 오버플로 구역)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Tiếp nối từ chuyên đề cơ sở dữ liệu [11-co-so-du-lieu-va-quan-ly-giao-dich.md](11-co-so-du-lieu-va-quan-ly-giao-dich.md), trong khi CSDL quản lý dữ liệu lưu trữ bền vững trên đĩa cứng, thì các chương trình phần mềm khi thực thi trong bộ nhớ RAM bắt buộc phải tổ chức dữ liệu dưới dạng các cấu trúc mảng, danh sách liên kết, ngăn xếp, hàng đợi hoặc cây để tối ưu hóa tốc độ tính toán.
- **Đang giải quyết gì (Current Problem):** Bài học chuyên đề này hợp nhất 8 bài học cấu trúc dữ liệu và giải thuật từ nguồn tài liệu gốc, cung cấp toàn bộ nền tảng về tổ chức bộ nhớ, phân tích độ phức tạp thuật toán và kỹ thuật tối ưu hóa tìm kiếm/sắp xếp trong khoa học máy tính.
- **Dùng đi đâu (Forward Handoff):** Hoàn tất toàn diện 12 bài học chuyên sâu của Môn 1 (소프트웨어 설계). Đây là hành trang kiến thức nền tảng trực tiếp để người học tự tin bước sang **Môn 2: 소프트웨어 개발 (Phát triển phần mềm)**, nơi cấu trúc dữ liệu và giải thuật sẽ được áp dụng trực tiếp vào khâu lập trình và kiểm thử phần mềm (`데이터 입출력 구현`).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc lòng công thức duyệt 3 loại cây nhị phân (Preorder: Gốc trước; Inorder: Gốc giữa; Postorder: Gốc sau); thuật toán tính Postfix bằng Stack; bảng độ phức tạp Big-O của các thuật toán sắp xếp; và 3 tầng chỉ mục của ISAM.
- Đọc TẦNG B để theo dõi bài toán mẫu giải chi tiết duyệt cây nhị phân và cách lần vết từng bước của thuật toán tính biểu thức hậu tố.

---

## 자료구조 및 알고리즘

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Phân loại Cấu trúc Dữ liệu (Classification of Data Structures)
- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [Hàn/Anh]: `자료구조는 데이터의 논리적 관계와 물리적 배치 방식에 따라 선형 구조(Linear)와 비선형 구조(Non-Linear)로 분류된다.`
  - [Tiếng Việt]: Cấu trúc dữ liệu được chia làm 2 nhánh lớn dựa trên mối quan hệ giữa các phần tử: Cấu trúc tuyến tính (quan hệ 1:1, các phần tử nối tiếp nhau thành một chuỗi) và Cấu trúc phi tuyến tính (quan hệ 1:N hoặc N:M, phân cấp hoặc đa hướng).

- **Bảng phân loại tổng thể:**

| Nhánh cấu trúc | Đặc trưng quan hệ | Các cấu trúc dữ liệu cụ thể |
|:---|:---:|:---|
| **선형 구조 (Linear Data Structures)** | **Quan hệ 1:1** (Tuần tự liên tiếp) | • **배열 (Array)**: Các phần tử cùng kiểu, nằm liền kề trong bộ nhớ, truy cập chỉ mục $O(1)$. • **연결 리스트 (Linked List)**: Các nút nối nhau bằng con trỏ, chèn/xóa $O(1)$, truy cập $O(N)$. • **스택 (Stack)**: Vào sau ra trước (LIFO). • **큐 (Queue)**: Vào trước ra trước (FIFO). • **데크 (Deque)**: Vào/ra ở cả hai đầu. |
| **비선형 구조 (Non-linear Data Structures)** | **Quan hệ 1:N hoặc N:M** (Phân nhánh, mạng lưới) | • **트리 (Tree)**: Cấu trúc phân cấp hình cây (Quan hệ 1:N cha - con). • **그래프 (Graph)**: Cấu trúc mạng lưới đỉnh và cạnh (Quan hệ N:M). |

---

#### 2. Ngăn xếp (Stack), Hàng đợi (Queue) và Hàng đợi hai đầu (Deque)

| Cấu trúc | Nguyên lý hoạt động | Thao tác cốt lõi | Hiện tượng & Ứng dụng thực tế |
|:---|:---:|:---|:---|
| **스택 (Stack)** | **LIFO** (Last In First Out / Vào sau ra trước) | • `Push`: Thêm phần tử vào đỉnh `Top`. • `Pop`: Lấy phần tử ra từ đỉnh `Top`. | • `오버플로 (Overflow)`: Thêm vào khi Stack đã đầy. • `언더플로 (Underflow)`: Lấy ra khi Stack rỗng. • *Ứng dụng:* Ngăn xếp lời gọi hàm đệ quy (Call Stack), Đảo ngược chuỗi, Hoàn tác Undo/Redo, Tính biểu thức hậu tố. |
| **큐 (Queue)** | **FIFO** (First In First Out / Vào trước ra trước) | • `Enqueue`: Thêm phần tử vào đuôi `Rear`. • `Dequeue`: Lấy phần tử ra từ đầu `Front`. | • Thêm và xóa diễn ra ở **hai đầu đối diện nhau**. • *Ứng dụng:* Lập lịch điều phối CPU (FIFO/Round Robin), Hàng đợi in tài liệu, Hàng đợi thông điệp Message Queue (MOM). |
| **데크 (Deque)** | **LIFO + FIFO** (Hai đầu linh hoạt) | Cho phép cả hai thao tác Thêm (`Insert`) và Xóa (`Delete`) ở cả hai đầu `Front` và `Rear`. | • `Scroll`: Hạn chế đầu nhập. • `Shelf`: Hạn chế đầu xuất. |

---

#### 3. Cấu trúc Cây (Tree) và 3 Phép duyệt Cây nhị phân (Binary Tree Traversal)
- **Thuật ngữ cấu trúc cây:**
  - `루트 노드 (Root Node)`: Nút gốc nằm ở tầng cao nhất của cây (không có nút cha).
  - `단말 노드 / 잎 노드 (Leaf Node)`: Nút lá ở đáy cây, **có Bậc bằng 0 (차수 = 0, không có nút con nào)**.
  - `차수 (Degree - Bậc của nút)`: **Số lượng nút con trực tiếp** của một nút.
  - `트리의 차수 (Degree of Tree - Bậc của cây)`: **Giá trị bậc lớn nhất** trong tất cả các nút của cây.
- **Cây nhị phân (이진 트리 - Binary Tree):** Cây mà mỗi nút có **tối đa 2 nút con (Degree $\le 2$)**.
- **Các công thức toán học cây nhị phân kinh điển trong đề thi:**
  1. Số nút tối đa ở tầng $i$ (Level $i$, gốc là tầng 1): **$\text{Max Nodes at Level } i = 2^{i-1}$**.
  2. Số nút tối đa của cây nhị phân có độ cao $h$: **$\text{Max Nodes} = 2^h - 1$**.
  3. Mối quan hệ giữa nút lá $n_0$ (bậc 0) và nút có 2 con $n_2$ (bậc 2): **$n_0 = n_2 + 1$** (Số nút lá luôn bằng số nút 2 con cộng 1).
- **3 Phép duyệt cây nhị phân kinh điển (BẮT BUỘC THUỘC ĐỂ GIẢI ĐỀ THI):**
  1. `전위 순회 (Preorder Traversal)`: **Root $\rightarrow$ Left $\rightarrow$ Right** (Thăm nút Gốc trước).
  2. `중위 순회 (Inorder Traversal)`: **Left $\rightarrow$ Root $\rightarrow$ Right** (Thăm nút Gốc ở giữa).
  3. `후위 순회 (Postorder Traversal)`: **Left $\rightarrow$ Right $\rightarrow$ Root** (Thăm nút Gốc sau cùng).

---

#### 4. Ký pháp Biểu thức số học (Expression Notation) và Thuật toán Stack
- **3 Dạng biểu diễn biểu thức:**
  - `중위 표기법 (Infix Notation)`: Toán tử nằm giữa 2 toán hạng $\rightarrow$ Ví dụ: $A + B$
  - `전위 표기법 (Prefix / Polish)`: Toán tử nằm trước 2 toán hạng $\rightarrow$ Ví dụ: $+ A B$
  - `후위 표기법 (Postfix / Reverse Polish)`: Toán tử nằm sau 2 toán hạng $\rightarrow$ Ví dụ: $A B +$
- **Thuật toán tính giá trị biểu thức hậu tố (Postfix Evaluation) bằng Stack:**
  1. Quét biểu thức từ trái sang phải.
  2. Nếu gặp **Toán hạng (Con số)**: Đẩy (`Push`) vào Stack.
  3. Nếu gặp **Toán tử (+, -, *, /)**:
     - Lấy (`Pop`) 2 toán hạng trên đỉnh Stack ra (Toán hạng lấy ra trước là $B$, toán hạng lấy ra sau là $A$).
     - Thực hiện phép toán: $A \text{ [toán tử] } B$.
     - Đẩy kết quả tính toán ngược lại (`Push`) vào Stack.
  4. Khi quét hết biểu thức, kết quả cuối cùng nằm duy nhất trên đỉnh Stack.

---

#### 5. Bảng ma trận Độ phức tạp các Thuật toán Sắp xếp (Sorting Algorithms)

| Thuật toán sắp xếp | Cơ chế hoạt động cốt lõi | Độ phức tạp thời gian (Tốt nhất) | Độ phức tạp (Trung bình) | Độ phức tạp (Xấu nhất) |
|:---|:---|:---:|:---:|:---:|
| **버블 정렬 (Bubble Sort)** | So sánh và đổi chỗ 2 phần tử kề nhau, phần tử lớn nổi dần về cuối | $O(N)$ (nếu tối ưu) | $O(N^2)$ | $O(N^2)$ |
| **선택 정렬 (Selection Sort)** | Mỗi vòng tìm Min trong phần chưa sắp đặt vào vị trí đầu | $O(N^2)$ | $O(N^2)$ | $O(N^2)$ |
| **삽입 정렬 (Insertion Sort)** | Chèn phần tử mới vào đúng vị trí trong dãy con đã sắp | $O(N)$ (đã sắp sẵn) | $O(N^2)$ | $O(N^2)$ |
| **퀵 정렬 (Quick Sort)** | Chọn Pivot, phân hoạch 2 bên, đệ quy chia để trị | $O(N \log N)$ | **$O(N \log N)$ (Rất nhanh)** | **$O(N^2)$ (khi đã sắp)** |
| **병합 정렬 (Merge Sort)** | Chia đôi dãy, sắp xếp đệ quy, trộn lại (cần bộ nhớ phụ) | $O(N \log N)$ | **$O(N \log N)$ (Ổn định)** | **$O(N \log N)$** |
| **힙 정렬 (Heap Sort)** | Xây dựng cây nhị phân hoàn chỉnh Heap, rút gốc Min/Max | $O(N \log N)$ | **$O(N \log N)$** | **$O(N \log N)$** |

---

#### 6. Thuật toán Tìm kiếm (Search), Bảng băm (Hashing) và Tập tin ISAM

##### A. Tìm kiếm nhị phân (이진 검색 - Binary Search)
- **ĐIỀU KIỆN TIÊN QUYẾT BẮT BUỘC:** **Dữ liệu trong mảng bắt buộc phải được SẮP XẾP TRƯỚC (정렬 필수)**.
- Mỗi bước so sánh chia đôi không gian tìm kiếm $\rightarrow$ Độ phức tạp cực nhanh: **$O(\log N)$**.

##### B. Bảng băm (해싱 - Hashing)
- Sử dụng hàm băm $h(\text{key})$ để ánh xạ trực tiếp từ khóa tìm kiếm thành địa chỉ ô nhớ trong bảng băm $\rightarrow$ Thời gian tìm kiếm lý tưởng là **$O(1)$**.
- **Hiện tượng xung đột (`충돌 - Collision`):** Khi 2 khóa khác nhau được hàm băm tính ra cùng 1 địa chỉ ô nhớ (Bucket).
- **2 Phương pháp xử lý va chạm chính:**
  - `체이닝 (Chaining)`: Dùng danh sách liên kết bên ngoài để móc nối các phần tử trùng vị trí vào cùng một bucket.
  - `개방 주소법 (Open Addressing)`: Dò tìm ô nhớ trống lân cận bên trong bảng băm (Dò tuyến tính Linear Probing, Băm kép Double Hashing).

##### C. Tập tin chỉ mục tuần tự (ISAM - Indexed Sequential Access Method)
- Cấu trúc gồm 3 vùng dữ liệu trên đĩa:
  1. `기본 구역 (Prime Area)`: Chứa các bản ghi dữ liệu thực tế được sắp xếp theo thứ tự khóa.
  2. `오버플로 구역 (Overflow Area)`: Chứa các bản ghi tràn khi vùng cơ bản bị đầy (Track Overflow, Cylinder Overflow).
  3. `색인 구역 (Index Area - 3 tầng chỉ mục)`:
     - **트랙 색인 (Track Index):** Chỉ mục cấp thấp nhất, định vị bản ghi trên từng Track của đĩa.
     - **실린더 색인 (Cylinder Index):** Chỉ mục cấp trung, định vị Cylinder.
     - **마스터 색인 (Master Index):** Chỉ mục cấp cao nhất, định vị khi Cylinder Index quá lớn.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán mẫu duyệt Cây nhị phân và Trace chi tiết từng bước
Cho cây nhị phân mẫu sau:
```text
            [A] (Root)
           /   \
        [B]     [C]
       /   \       \
     [D]   [E]     [F]
```

- **A. Duyệt Tiền thứ tự (Preorder Traversal: Root $\rightarrow$ Left $\rightarrow$ Right):**
  - Bước 1: Thăm gốc `A`.
  - Bước 2: Đi sang cây con trái của `A` (gốc là `B`) $\rightarrow$ Thăm `B`.
  - Bước 3: Đi sang cây con trái của `B` (gốc là `D`, lá) $\rightarrow$ Thăm `D`.
  - Bước 4: Đi sang cây con phải của `B` (gốc là `E`, lá) $\rightarrow$ Thăm `E`.
  - Bước 5: Quay lại gốc `A`, đi sang cây con phải của `A` (gốc là `C`) $\rightarrow$ Thăm `C`.
  - Bước 6: Đi sang cây con phải của `C` (gốc là `F`, lá) $\rightarrow$ Thăm `F`.
  - **Chuỗi kết quả Preorder:** $\mathbf{A \rightarrow B \rightarrow D \rightarrow E \rightarrow C \rightarrow F}$.

- **B. Duyệt Trung thứ tự (Inorder Traversal: Left $\rightarrow$ Root $\rightarrow$ Right):**
  - Bước 1: Đi hết về phía trái nhất $\rightarrow$ Thăm `D`.
  - Bước 2: Lùi về nút cha của `D` $\rightarrow$ Thăm `B`.
  - Bước 3: Đi sang con phải của `B` $\rightarrow$ Thăm `E`.
  - Bước 4: Lùi về nút gốc toàn cây $\rightarrow$ Thăm `A`.
  - Bước 5: Đi sang cây con phải của `A`, thăm nút `C` (vì `C` không có con trái).
  - Bước 6: Đi sang con phải của `C` $\rightarrow$ Thăm `F`.
  - **Chuỗi kết quả Inorder:** $\mathbf{D \rightarrow B \rightarrow E \rightarrow A \rightarrow C \rightarrow F}$.

- **C. Duyệt Hậu thứ tự (Postorder Traversal: Left $\rightarrow$ Right $\rightarrow$ Root):**
  - Bước 1: Đi hết về con trái nhất $\rightarrow$ Thăm `D`.
  - Bước 2: Đi sang con phải của `B` $\rightarrow$ Thăm `E`.
  - Bước 3: Sau khi duyệt xong 2 con, thăm cha `B`.
  - Bước 4: Chuyển sang cây con phải của `A`, đi đến lá `F`.
  - Bước 5: Thăm cha `C` (sau khi con phải `F` xong).
  - Bước 6: Thăm gốc toàn cây `A` sau cùng.
  - **Chuỗi kết quả Postorder:** $\mathbf{D \rightarrow E \rightarrow B \rightarrow F \rightarrow C \rightarrow A}$.

#### 2. Bài toán mẫu tính toán Biểu thức hậu tố bằng Stack
- Cho biểu thức hậu tố: `3 4 2 * + 5 -`
- **Quá trình lần vết từng bước qua Stack:**
  1. Đọc `3` $\rightarrow$ Push vào Stack: `[3]`
  2. Đọc `4` $\rightarrow$ Push vào Stack: `[3, 4]`
  3. Đọc `2` $\rightarrow$ Push vào Stack: `[3, 4, 2]`
  4. Đọc `*` (Nhân) $\rightarrow$ Pop 2 và Pop 4 ra, tính: $4 \times 2 = 8$, Push 8 vào Stack: `[3, 8]`
  5. Đọc `+` (Cộng) $\rightarrow$ Pop 8 và Pop 3 ra, tính: $3 + 8 = 11$, Push 11 vào Stack: `[11]`
  6. Đọc `5` $\rightarrow$ Push vào Stack: `[11, 5]`
  7. Đọc `-` (Trừ) $\rightarrow$ Pop 5 và Pop 11 ra, tính: $11 - 5 = 6$, Push 6 vào Stack: `[6]`
- **Kết quả tính toán cuối cùng:** $\mathbf{6}$.

---

### 복습 체크리스트
- [ ] Phân loại được các cấu trúc dữ liệu tuyến tính (Array, List, Stack, Queue, Deque) và phi tuyến tính (Tree, Graph).
- [ ] Định nghĩa được Stack (LIFO, thao tác tại Top) và Queue (FIFO, thêm Rear, lấy Front).
- [ ] Phân biệt được Bậc của nút (số nút con) và Bậc của cây (bậc lớn nhất của nút trong cây); nhớ nút lá có Bậc bằng 0.
- [ ] Thuộc lòng quy tắc 3 phép duyệt cây nhị phân: Preorder (Root-L-R), Inorder (L-Root-R), Postorder (L-R-Root).
- [ ] Giải thành thạo bài toán tính toán biểu thức hậu tố Postfix bằng Stack.
- [ ] Nhớ độ phức tạp thời gian của Quick Sort ($O(N \log N)$, xấu nhất $O(N^2)$), Merge Sort và Heap Sort (luôn $O(N \log N)$).
- [ ] Nhớ điều kiện tiên quyết của Binary Search là dữ liệu bắt buộc phải được sắp xếp trước.
- [ ] Định nghĩa được hiện tượng xung đột (Collision) trong Hashing và nhớ 2 cách xử lý: Chaining và Open Addressing.
- [ ] Nhớ thứ tự 3 tầng chỉ mục của ISAM: Master Index $\rightarrow$ Cylinder Index $\rightarrow$ Track Index.
