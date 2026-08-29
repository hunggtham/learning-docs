# Môn 2 — 소프트웨어 개발 (Software Development) (Phát triển phần mềm)

## 학습 목표 (Mục tiêu học tập)

- 시험에서 사용하는 한국어 용어를 영어와 베트남어 뜻까지 함께 인식한다.
- 각 개념을 정의 → 구성요소/절차 → 비교 포인트 → 예시 순서로 설명할 수 있다.
- 앞에서 배운 개념과 뒤의 심화 개념을 연결하여 문제의 조건을 빠르게 해석한다.

## 권장 학습 순서 (Lộ trình đề xuất)

1. 먼저 이 문서의 각 `##` 단원을 순서대로 읽는다.
2. 단원마다 **핵심 키워드**를 소리 내어 읽고, 한국어 원문과 베트남어 설명을 함께 확인한다.
3. 마지막에 `복습 체크리스트`를 점검한 뒤, 세부 lesson 파일에서 헷갈리는 부분을 다시 본다.

> **Nguồn:** tổng hợp từ các Markdown đã generate trong `raw_md/final`, được đối chiếu với các nguồn `raw` và `raw_md` cùng môn. Nội dung gốc được giữ lại; chỉ chuẩn hoá cấu trúc bài học.

> **Quy ước đọc:** thuật ngữ được ưu tiên theo mẫu `한국어 (English) (Tiếng Việt)`. Mỗi ý tiếng Hàn có phần giải thích Việt ngữ liền kề hoặc ngay sau đó; khi gặp từ kỹ thuật trong ngoặc, hãy xem đó là nghĩa cần nhớ khi làm đề.

> **Cách học:** học theo thứ tự các mục; với mỗi mục, xác định khái niệm → cơ chế/quy tắc → ví dụ → mẹo nhớ. Các mục lặp lại ở phần “심화” (nâng cao) dùng để nối kiến thức trước đó với dạng câu hỏi sâu hơn.

---

## 1. 자료 구조의 분류 (Classification of Data Structures)
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

---

## 2. 스택 (Stack) 및 응용 (Applications)
* 리스트의 한쪽 끝으로만 자료의 삽입, 삭제 작업이 이루어지는 자료 구조.
* 가장 나중에 삽입된 자료가 가장 먼저 삭제되는 후입선출(**LIFO**, Last-In First-Out) 방식.
* **응용 분야 (Applications)**: 인터럽트 처리 (Interrupt handling), 수식 계산 및 표기법 (Expression evaluation), 서브루틴 호출 및 복귀 주소 저장 (Subroutine calls).
* **삽입/삭제 (Push/Pop)**: `PUSH`는 자료 입력, `POP`은 자료 출력.
* **VI (Vietnamese) (Tiếng Việt):**
  * Stack là cấu trúc dữ liệu LIFO, thêm/xóa dữ liệu ở một đầu.
  * Ứng dụng: Xử lý ngắt, tính toán biểu thức, lưu địa chỉ khi gọi hàm.
* **Example**: 브라우저의 '뒤로 가기' 버튼은 스택 구조를 사용합니다. (Nút "Back" trên trình duyệt sử dụng cấu trúc stack).
* 💡 **Mẹo ghi nhớ**: LIFO - Vào sau ra trước, giống như xếp đĩa, lấy đĩa trên cùng ra trước.

---

## 29. 큐 (Queue)
* 삽입은 한쪽 끝에서, 삭제는 반대쪽 끝에서 이루어지는 자료 구조.
* 선입선출(**FIFO**, First-In First-Out) 방식.
* 시작과 끝을 표시하는 두 개의 포인터(Front, Rear)가 있음.
* **VI (Vietnamese) (Tiếng Việt):** Hàng đợi FIFO (Vào trước ra trước). Dùng 2 con trỏ chỉ vị trí đầu và cuối.
* **Example**: 프린터의 인쇄 대기열이나 매표소 줄서기와 같습니다.
* 💡 **Mẹo ghi nhớ**: Queue = Xếp hàng.

---

## 3. 트리 (Tree)
* 정점(Node)과 선분(Branch)을 이용하여 사이클을 이루지 않도록 구성한 그래프의 특수한 형태.
* **디그리 (Degree, 차수)**: 각 노드에서 뻗어 나온 가지의 수.
* **단말 노드 (Terminal Node) = 잎 노드 (Leaf Node)**: 자식이 하나도 없는 노드, 즉 디그리가 0인 노드.
* **VI (Vietnamese) (Tiếng Việt):**
  * Cây là đồ thị đặc biệt không có chu trình.
  * Bậc (Degree): Số nhánh của một nút con.
  * Nút lá (Leaf): Nút không có con (bậc = 0).
* **Example**: 폴더 구조에서 하위 폴더가 없는 폴더가 단말 노드입니다. (Trong cấu trúc thư mục, thư mục không chứa thư mục con là nút lá).
* 💡 **Mẹo ghi nhớ**: Degree là số con trực tiếp. Leaf là chiếc lá ở cuối cành không mọc thêm được nữa.

---

## 4. 이진 트리의 운행법 (Binary Tree Traversal)
* **Preorder (전위)**: Root → Left → Right
* **Inorder (중위)**: Left → Root → Right
* **Postorder (후위)**: Left → Right → Root
* **VI (Vietnamese) (Tiếng Việt):**
  * Preorder: Gốc -> Trái -> Phải.
  * Inorder: Trái -> Gốc -> Phải.
  * Postorder: Trái -> Phải -> Gốc.
* **Example**: 수식 `A + B`를 전위 표기하면 `+ A B`, 중위 표기하면 `A + B`, 후위 표기하면 `A B +`가 됩니다.
* 💡 **Mẹo ghi nhớ**: Tiền/Trung/Hậu tố chỉ vị trí của Root (Gốc) so với Trái/Phải.

---

## 30. 트리 구조 추가 용어 (Tree Terminology Additional)
* **자식 노드 (Son Node)**: 어떤 노드에 연결된 다음 레벨의 노드들.
* **부모 노드 (Parent Node)**: 어떤 노드에 연결된 이전 레벨의 노드.
* **형제 노드 (Sibling / Brother Node)**: 동일한 부모를 갖는 노드들.
* **트리의 디그리 (Degree of a Tree)**: 전체 노드들의 디그리(자식 수) 중에서 가장 큰 값.
* **VI (Vietnamese) (Tiếng Việt):**
  * Son Node: Nút con.
  * Parent Node: Nút cha.
  * Sibling: Nút anh em (cùng cha).
  * Degree of Tree: Bậc lớn nhất trong tất cả các nút của cây.

---

## 025: 트리 (Tree / Cây)

| 용어 (Thuật ngữ) | 설명 (Giải thích) | 예시 (Ví dụ) |
|---|---|---|
| 루트 노드 (Root Node) | Nút gốc, không có cha. Chỉ có 1 gốc. | A |
| 단말 노드 (Leaf/Terminal Node) | Nút lá, ở cuối cùng, không có con. | D, E, H, I, G |
| 레벨 (Level) | Độ sâu từ gốc tới nút. | E có Level là 3. |
| 깊이 (Depth) | Độ sâu lớn nhất của cây (Max Level - 1 hoặc tùy cách tính). | Depth = 3. |
| 차수 (Degree of Node) | Bậc của một nút: Số lượng con của nút đó. | B có 3 con => Degree = 3. |
| 트리의 차수 (Degree of Tree) | Bậc của cây: Bậc lớn nhất trong tất cả các nút. | Cả cây có nút max là 3 => Degree của cây = 3. |

### 트리 순회 (Tree Traversal - Duyệt cây)
- **전위 순회 (Preorder):** Root -> Left -> Right.
- **중위 순회 (Inorder):** Left -> Root -> Right.
- **후위 순회 (Postorder):** Left -> Right -> Root.

- **Vietnamese Explanation:** Cách tính Bậc của cây rất hay thi: Tìm cái nút nào đẻ nhiều con nhất, số con đó chính là Bậc của toàn bộ cây. Khi duyệt cây, chữ "Pre/In/Post" (Trước/Giữa/Sau) dùng để chỉ vị trí của Root. Root đứng trước là Pre, ở giữa là In, ở cuối là Post.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 단말 (Đoạn mạt = Cuối) = Leaf (Lá). Degree = Bậc = Số con. Pre/In/Post = Vị trí của Gốc (Root).

---

---

## 026: 그래프 (Graph / Đồ thị)

- **방향 그래프 (Directed Graph):** Có hướng. Tối đa `n(n-1)` cạnh (n là số đỉnh).
- **무방향 그래프 (Undirected Graph):** Vô hướng. Tối đa `n(n-1)/2` cạnh.

### 탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)
- **DFS (Depth-First Search - Tìm kiếm theo chiều sâu):** Đi sâu nhất có thể, hết đường mới lui lại (Dùng Stack).
- **BFS (Breadth-First Search - Tìm kiếm theo chiều rộng):** Loang ra xung quanh, tầng nào xong mới xuống tầng sau (Dùng Queue).

- 💡 **Mẹo ghi nhớ (Mnemonics):** DFS = Sâu = Stack (D/S). BFS = Rộng = Queue (B/Q). Vô hướng chia 2 vì AB và BA là một.

---

---

## 5. 수식의 표기법 변환 (Expression Notation Conversion)
* **Infix → Prefix**: 연산자를 피연산자 두 개의 **앞(왼쪽)**으로 이동.
* **Infix → Postfix**: 연산자를 피연산자 두 개의 **뒤(오른쪽)**로 이동.
* **Postfix → Infix**: 연산자를 피연산자 두 개의 **가운데**로 이동.
* **VI (Vietnamese) (Tiếng Việt):** Chuyển đổi biểu thức Infix sang Prefix (đưa toán tử ra trước) và Postfix (đưa toán tử ra sau).
* **Example**: Infix `A/B` -> Postfix `A B /` -> Prefix `/ A B`.
* 💡 **Mẹo ghi nhớ**: Prefix (Pre = trước), Postfix (Post = sau).

---

## 6. 정렬 알고리즘 (Sorting Algorithms)
* **삽입 정렬 (Insertion Sort)**: 두 번째 값부터 시작해 앞의 값들과 비교하여 알맞은 위치에 삽입.
* **선택 정렬 (Selection Sort)**: 가장 작은 값을 선택해 첫 번째와 교환, 그 다음 작은 값을 두 번째와 교환하는 방식.
* **버블 정렬 (Bubble Sort)**: 인접한 두 값을 비교하여 큰 값을 뒤로 보내는 과정을 반복.
* **VI (Vietnamese) (Tiếng Việt):**
  * Insertion: Chèn phần tử vào đúng vị trí của dãy đã sắp xếp.
  * Selection: Chọn phần tử nhỏ nhất đưa lên đầu.
  * Bubble: Nổi bọt, so sánh 2 phần tử kề nhau, lớn hơn thì đổi chỗ.
* **Example**: `8, 5, 6` 버블 정렬 1회전: 5, 8, 6 -> 5, 6, 8. (Bubble sort đổi chỗ 8 và 5, rồi 8 và 6).
* 💡 **Mẹo ghi nhớ**: Insertion: bốc bài và chèn. Selection: tìm người lùn nhất xếp hàng. Bubble: bong bóng lớn nổi lên cuối cùng.

---

## 31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)
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

---

## 028: 정렬 (Sorting / Thuật toán sắp xếp)

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

---

## 7. 이분 검색 (Binary Search)
* 검색할 데이터가 정렬되어 있어야 함.
* 비교 횟수를 거듭할 때마다 검색 대상이 반(절반)으로 줄어듦.
* 탐색 효율이 좋고 시간이 적게 소요됨. 중간 레코드 번호(M) = (F+L)/2.
* **VI (Vietnamese) (Tiếng Việt):** Tìm kiếm nhị phân. Dữ liệu phải được sắp xếp trước. Mỗi lần chia đôi không gian tìm kiếm.
* **Example**: 사전에서 단어를 찾을 때 책을 반으로 계속 쪼개며 찾는 방식입니다.
* 💡 **Mẹo ghi nhớ**: Binary = chia đôi (phải sắp xếp trước!).

---

## 029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)

### 검색 (Search - Tìm kiếm)
- **순차 검색 (Sequential/Linear Search):** Tìm tuần tự từ đầu đến cuối. Dùng cho mảng *chưa sắp xếp*. O(n).
- **이진 검색 (Binary Search):** Tìm nhị phân. Chia đôi mảng liên tục. **Bắt buộc mảng phải ĐÃ SẮP XẾP.** O(log n). Rất nhanh.

### 해싱 (Hashing - Băm dữ liệu)
- Dùng hàm băm (Hash Function) tính ra trực tiếp địa chỉ bộ nhớ để lưu hoặc tìm kiếm dữ liệu. Nhanh nhất (O(1)).

- **Vietnamese Explanation:** Tìm tuần tự là lật từng trang sách. Tìm nhị phân là mở giữa cuốn từ điển, xem vần nào rồi gập nửa bỏ đi, tìm tiếp ở nửa kia. Băm (Hashing) là nhìn Mục lục rồi lật thẳng trang đó.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Binary Search = Phải Sắp Xếp (Sắp xếp), Chia đôi (절반). Hashing = O(1) Siêu Tốc.

### 해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)

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

# Chapter 2. 통합 구현 (Integration Implementation)

---

## 8. 주요 해싱 함수 (Hashing Functions)
* **제산법 (Division)**: 키 값을 소수(Prime)로 나눈 나머지를 주소로 사용.
* **제곱법 (Mid-Square)**: 키 값을 제곱한 후 중간 부분의 값을 주소로 사용.
* **폴딩법 (Folding)**: 키 값을 여러 부분으로 나눈 후 더하거나 XOR한 값을 주소로 사용.
* **숫자 분석법 (Digit Analysis)**: 숫자의 분포를 분석해 고른 자리를 주소로 사용.
* **VI (Vietnamese) (Tiếng Việt):** Các hàm băm (Hashing) giúp ánh xạ khóa (key) thành địa chỉ. Division (chia lấy dư), Mid-Square (bình phương lấy giữa), Folding (gấp/cộng các phần), Digit Analysis (phân tích chữ số).
* **Example**: 제산법으로 키 10을 해시 테이블 크기 7(소수)로 나누면 나머지 3이 주소가 됩니다.
* 💡 **Mẹo ghi nhớ**: Division = Chia lấy dư, Square = Bình phương, Fold = Gấp lại.

---

## 32. 추가 해싱 함수 (Additional Hashing Functions)
* **기수 변환법 (Radix)**: 키 숫자의 진수를 다른 진수로 변환.
* **대수적 코딩법 (Algebraic Coding)**: 다항식의 계수로 간주하여 나눈 나머지 사용.
* **무작위법 (Random)**: 난수를 발생시켜 홈 주소로 사용.
* **VI (Vietnamese) (Tiếng Việt):** Các hàm băm khác: Cơ số (Radix), Đại số (Algebraic), Ngẫu nhiên (Random).

---

## 34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)
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

---

## 핵심 031: 모듈 구현 (Module Implementation)

- **구현 (Implementation):** 설계 명세서가 컴퓨터가 알 수 있는 모습으로 변환되는 과정. 프로그래밍 또는 코딩. (Quá trình chuyển thiết kế thành code.)
- **작업 절차 (Trình tự):** 코딩 계획 (Lập kế hoạch) → 코딩 (Code) → 컴파일 (Compile) → 테스트 (Test).
- **모듈 (Module):** 독립적인 기능을 갖는 단위. 모듈이 모이면 프로그램이 됨. (Một đơn vị độc lập thực hiện một chức năng cụ thể.)
- **컴포넌트 (Component):** 독립적으로 존재할 수 있는 부분, 재사용되는 단위, 인터페이스를 통해서만 접근. (Thành phần có thể tái sử dụng, giao tiếp qua Interface.)

- **Vietnamese Explanation:** Module là một khối code (như một hàm hoặc một class). Component là một khối lớn hơn, đóng gói sẵn và có thể lắp ráp vào nhiều phần mềm khác nhau (như một nút bấm UI, một bộ lịch).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Trình tự: Kế hoạch -> Code -> Dịch (Compile) -> Thử (Test). Module = Ghép lại thành chương trình. Component = Tái sử dụng qua Interface.

---

---

## 093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)

### 단위 모듈 (Unit Module)
- 프로그램의 단위 기능을 구현하는 독립적인 최소 소프트웨어 단위. (Đơn vị phần mềm nhỏ nhất, độc lập, thực hiện 1 chức năng duy nhất).

### 단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)
- **추상화 (Abstraction):** 복잡한 시스템을 단순하게 구현. (Trừu tượng hóa - ẩn đi sự phức tạp).
- **구조화 (Structuring):** 대형 시스템을 분해하여 단위 기능별로 구분, 계층적으로 구성. (Cấu trúc hóa - chia nhỏ thành sơ đồ hình cây).
- **정보 은닉 (Information Hiding):** 한 모듈 내의 정보가 다른 모듈에 영향을 주지 않도록 숨김. (Che giấu thông tin - dùng biến private để tránh đụng độ).

### 입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)
- **입·출력 구현:** Nhận Input, trả Output. Chú ý liên kết giao diện (CLI/GUI) hoặc dùng Open Source API để kết nối mạng.
- **알고리즘 구현:** Viết code xử lý logic bên trong (Process) sau khi đã có I/O.

---

---

## 094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)

### IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)
- 모듈 간 또는 복수의 프로세스 간 통신을 위한 인터페이스. (Cách các chương trình đang chạy nói chuyện với nhau).
- **Các phương pháp IPC:**
  - **Shared Memory (Bộ nhớ chia sẻ):** Nhanh nhất. Các process dùng chung 1 vùng RAM.
  - **Socket (Ổ cắm):** Giao tiếp qua mạng.
  - **Semaphores (Cờ hiệu):** Đồng bộ hóa, khóa (Locking) tài nguyên dùng chung.
  - **Pipes (Ống dẫn):** Dùng RAM theo kiểu FIFO, tại 1 thời điểm chỉ 1 process được dùng.
  - **Message Queueing (Hàng đợi tin nhắn):** Truyền tin bất đồng bộ.

### 알고리즘 구현 모듈 (Các loại Module khi lập trình)
- **디바이스 드라이버 모듈 (Device Driver):** Điều khiển phần cứng ngoại vi (vd: Máy in).
- **네트워크 모듈 (Network):** Truyền thông dữ liệu mạng.
- **파일 모듈 (File):** Truy xuất cấu trúc file trên đĩa cứng.
- **메모리 모듈 (Memory):** Quản lý RAM, cấp phát bộ nhớ ảo, hoặc làm IPC.
- **프로세스 모듈 (Process):** Tạo và quản lý các tiến trình khác.

- 💡 **Mẹo ghi nhớ (Mnemonics):** IPC là gửi thư cho nhau. Shared Memory = Bảng tin chung (Nhanh nhất). Semaphore = Cái khóa cửa nhà vệ sinh (Ai đang dùng thì khóa lại).

---

---

## 095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)

### 단위 모듈 테스트 (Unit Module Test)
- 코딩 직후 최소 단위인 모듈이나 컴포넌트에 초점을 맞춤. (Test ngay sau khi code xong 1 hàm/module).
- Chủ yếu dùng **화이트박스 (White-box test)** để tìm lỗi thuật toán, vòng lặp vô hạn, lỗi công thức toán học.

### 테스트 케이스 (Test Case)
- 입력 값, 실행 조건, 기대 결과의 명세서. (Tài liệu ghi rõ: Nhập gì, Điều kiện gì, Kết quả mong đợi là gì).
- 테스트 케이스를 미리 작성(사전에 정의)해야 인력과 시간 낭비를 방지. (Phải viết Test Case **trước** khi code hoặc test, để tránh test lung tung tốn thời gian).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Test Case = Input + Condition + Expected Output. Bắt buộc viết trước khi test.

---

---

## 13. 형상 관리 (SCM - Software Configuration Management)
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

---

## 40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)
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

---

## 핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)

### 형상 관리 (Configuration Management)
- 소프트웨어 개발 과정의 **변경 사항을 관리**하는 것. (Quản lý mọi thay đổi trong vòng đời phần mềm - Version Control).
- 대상 (Đối tượng): 계획, 요구 분석서, 설계서, 소스 코드, 테스트 케이스, 지침서 등. (**개발 비용 - Chi phí phát triển KHÔNG nằm trong này**).
- 절차 (Trình tự): 형상 식별 (Nhận dạng) → 형상 통제 (Kiểm soát bởi CCB) → 형상 감사 (Kiểm toán) → 형상 기록 (Ghi lại).

### 형상 관리 방식 (Các phương pháp quản lý phiên bản)
- **공유 폴더 방식 (Shared Folder):** Lưu vào chung một thư mục trên mạng nội bộ. (Ví dụ: RCS).
- **클라이언트/서버 방식 (Client/Server):** Quản lý tập trung trên một máy chủ. (Ví dụ: CVS, SVN).
- **분산 저장소 방식 (Distributed Repository):** Mỗi máy cá nhân đều chứa một bản copy của kho chứa, commit lên máy cá nhân trước rồi mới push lên server. Rất an toàn. (Ví dụ: **Git**).

### 형상 관리 도구 기능 (Chức năng công cụ)
- **Check-In:** Đẩy code lên kho (Upload).
- **Check-Out:** Lấy code mới nhất về (Download).
- **Commit:** Xác nhận lưu sự thay đổi.

### IDE (Integrated Development Environment - Môi trường phát triển tích hợp)
- 코딩, 컴파일, 디버깅, 배포 (Coding, Compile, Debug, Deployment) 기능을 하나로 통합. (Tích hợp tất cả công cụ lập trình vào một phần mềm).
- Ví dụ: Eclipse (Java), Visual Studio (C#, C++), Xcode (iOS), Android Studio, IntelliJ IDEA.

- **Vietnamese Explanation:** Quản lý hình thái (Configuration/Version) giống như việc lưu file "Bao_cao_lan1", "Bao_cao_lan2", "Bao_cao_FINAL". Git (Phân tán) là công cụ phổ biến nhất hiện nay. IDE là bộ công cụ tất cả-trong-một của lập trình viên (vừa gõ code, vừa dịch, vừa tìm lỗi).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Trình tự 형상 quản lý: Nhận Kiểm Đánh Ghi (Nhận diện - Kiểm soát - Đánh giá - Ghi chép). Git = Phân tán (분산). IDE 4 bước: CoCoDeDe (Coding - Compile - Debugging - Deployment).

---

---

## 109 ~ 112: 형상 관리 (SCM - Software Configuration Management)

- **형상 관리 (SCM):** 소프트웨어 변경 사항을 체계적으로 관리. (Quản lý mọi thay đổi của phần mềm: Source code, tài liệu, thiết kế... trong suốt vòng đời).
- **목적:** 가시성 (Tính hiển thị - ai đang làm gì), 추적성 (Tính truy xuất - ai gây ra lỗi này), 무절제한 변경 방지 (Ngăn chặn việc sửa code vô tội vạ).

### 형상 관리 5대 기능 (5 Chức năng của SCM)
1. **형상 식별 (Identification):** Đặt tên, đánh số phiên bản, phân nhánh (Tree) để dễ quản lý.
2. **버전 제어 (Version Control):** Lưu lại các version cũ/mới.
3. **형상 통제 (Configuration Control):** Yêu cầu đổi code phải được xem xét kỹ trước khi nhập vào bản chính (Baseline).
4. **형상 감사 (Audit):** Kiểm tra lại xem code đã chuẩn chưa.
5. **형상 기록 (Status Reporting):** Ghi chép lịch sử báo cáo.

### 버전 관리 용어 (Thuật ngữ Version Control)
- **저장소 (Repository):** Kho lưu trữ code.
- **체크아웃 (Check-out):** Lấy code từ Kho về máy mình để sửa.
- **체크인 (Check-in) / 커밋 (Commit):** Lưu code mình vừa sửa vào máy mình (Local) hoặc đưa lên Kho.
- **동기화 (Update):** Lấy code mới nhất của người khác trên Kho về máy mình để đồng bộ.

---

---

## 116 & 117: 형상 관리 도구 (SVN vs Git)

### Subversion (SVN)
- 클라이언트/서버 구조 (Cấu trúc Client/Server tập trung).
- **Trunk:** Thư mục chính (Main).
- **Branches:** Th nhánh để làm tính năng riêng.
- **Revision:** Mỗi lần Commit thành công, số Revision tăng lên 1.

### Git (깃)
- 분산 저장소 방식 (Lưu trữ phân tán). Phát minh bởi Linus Torvalds.
- **Snapshot (스냅샷):** Lưu lại toàn bộ trạng thái file tại một thời điểm rất nhanh chóng.
- **로컬 저장소 (Local Repo) vs 원격 저장소 (Remote Repo):** Internet đứt vẫn làm việc bình thường ở Local.

- 💡 **Mẹo ghi nhớ (Mnemonics):** SVN = Trunk (Thân cây), Revision tăng dần. Git = Snapshot, Phân tán (Phân tán (Distributed)).

---

---

## 12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)
* **패키징 (Packaging)**: 모듈별 실행 파일들을 묶어 배포용 설치 파일을 만드는 것. 사용자 중심으로 진행하며 보안(암호화, DRM 연동) 고려.
* **설치 매뉴얼 (Installation Manual)**: 사용자를 기준으로 작성. 기본 사항, 소프트웨어 개요, 설치 파일, 프로그램 삭제 등 포함.
* **VI (Vietnamese) (Tiếng Việt):**
  * Packaging: Đóng gói các file thực thi thành file cài đặt (hướng đến người dùng cuối).
  * Manual: Tài liệu hướng dẫn cài đặt viết cho người dùng, bao gồm cách cài và gỡ.
* **Example**: `.exe` 설치 파일을 만들고, "다음, 다음, 완료"를 설명하는 설명서를 작성하는 과정입니다.

---

## 37. 소프트웨어 패키징 고려사항 추가 (Packaging Considerations)
* 사용자의 시스템 최소 환경(OS, CPU, 메모리) 정의.
* UI(시각적 자료) 매뉴얼과 일치.
* 하드웨어와 함께 관리되도록 Managed Service 형태로 제공 고려.
* 제품 종류에 적합한 암호화 알고리즘 및 DRM 연동 고려.
* **VI (Vietnamese) (Tiếng Việt):** Các lưu ý khi đóng gói phần mềm: Yêu cầu hệ thống tối thiểu, Giao diện (UI) khớp với hướng dẫn, Quản lý dịch vụ, Mã hóa/DRM.

---

## 39. DRM 패키징 과정 상세 (DRM Packaging Process)
* 디지털 콘텐츠 배포 시, 아날로그는 디지털로 변환 후 패키저가 패키징.
* 용량이 작으면 실시간 패키징, 크면 미리 패키징 후 배포.
* 암호화된 저작권자 전자서명 포함, 라이선스는 클리어링 하우스에 등록.
* **VI (Vietnamese) (Tiếng Việt):** Quy trình đóng gói DRM. Nội dung nhỏ thì đóng gói realtime, lớn thì đóng gói trước. Giấy phép lưu tại Clearing House.

---

## 핵심 035 & 036: 소프트웨어 패키징 및 DRM (Software Packaging & DRM)

### 패키징 고려사항 (Lưu ý khi đóng gói)
- **사용자를 중심**으로 진행. (Phải hướng tới người dùng, không phải lập trình viên).
- 보안, 이기종 연동, 복잡성 및 비효율성 문제 고려, 적합한 암호화 알고리즘 적용. (Bảo mật, liên kết đa nền tảng, dễ dùng, mã hóa).

### DRM (Digital Rights Management - Quản lý bản quyền kỹ thuật số)
- 허가된 권한 범위 내에서 콘텐츠의 이용이 가능하도록 통제하는 기술. (Kỹ thuật mã hóa, chống copy lậu, giới hạn số lần mở/in/sao chép nội dung kỹ thuật số).
- **Thành phần (Cấu trúc DRM):**
  - **Contents Provider (Người cung cấp):** Tác giả, người tạo nội dung.
  - **Contents Distributor (Người phân phối):** Nơi bán/phân phối (App Store, Melon...).
  - **Clearing House (Trung tâm thanh toán / Quản lý):** Quản lý Key (khóa), cấp phép License và tính tiền.
  - **Packager (Bộ đóng gói):** Đóng gói nội dung + Meta data + Mã hóa.
  - **DRM Controller (Bộ điều khiển):** Kiểm soát quyền sử dụng trên máy người dùng.

- **Vietnamese Explanation:** DRM là công nghệ chống vi phạm bản quyền (ví dụ: nhạc tải trên Spotify không thể copy ra máy MP3 thường nghe được). Clearing House là trọng tài ở giữa giữ chìa khóa và thu tiền.
- 💡 **Mẹo ghi nhớ (Mnemonics):** DRM = Chống copy lậu. **Clearing House** = Trạm kiểm soát và cấp phép (Rất hay thi). Firewall (Tường lửa) KHÔNG phải là công nghệ của DRM.

---

---

## 099: 소프트웨어 패키징 (Software Packaging)

- 실행 파일들을 묶어 배포용 설치 파일을 만드는 과정. (Gom tất cả file thực thi, file hình, file cấu hình thành 1 file cài đặt (Setup.exe) để tung ra thị trường).
- **Nguyên tắc:** 
  - **사용자 중심 (Hướng tới người dùng):** Người dùng cài đặt dễ dàng, không cần biết code.
  - Cần phải 모듈화 (Module hóa) để dễ bảo trì, và tích hợp 보안 (Bảo mật / DRM).

---

## 100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)

### 패키징 시 고려사항
- 최소 환경 정의 (OS/CPU/RAM). (Phải ghi rõ cấu hình tối thiểu để chạy app).
- UI와 매뉴얼 일치. (Hình ảnh UI trong thực tế và trong tài liệu phải giống nhau).
- 보안 및 암호화, DRM 연동 고려. (Bảo mật, mã hóa, tích hợp chống copy).

### 소프트웨어 패키징 순서 (Trình tự đóng gói)
1. **기능 식별 (Xác định chức năng)**
2. **모듈화 (Module hóa)**
3. **빌드 진행 (Build - Dịch ra file chạy)**
4. **사용자 환경 분석 (Phân tích môi trường người dùng - OS/CPU)**
5. **패키징 및 적용 시험 (Đóng gói & Test thử)**
6. **패키징 변경 개선 (Sửa lỗi nếu có)**
7. **배포 (Deployment - Phát hành)**

- 💡 **Mẹo ghi nhớ (Mnemonics):** Nhận-Mô-Build-Môi-Gói-Cải-Phân (Nhận diện - Module - Build - Môi trường - Đóng gói - Cải tiến - Phân phối).

---

---

## 10. 빌드 자동화 도구 (Build Automation Tools)
* **Ant**: 아파치 소프트웨어 재단에서 개발.
* **Maven**: Ant의 대안.
* **Jenkins**: JAVA 기반의 오픈 소스 빌드 자동화 도구.
* **Gradle**: Groovy 기반의 오픈 소스 빌드 자동화 도구.
* **VI (Vietnamese) (Tiếng Việt):** Các công cụ tự động hóa quá trình build phần mềm (biên dịch, đóng gói).
* **Example**: 개발자가 코드를 수정하면 Jenkins가 자동으로 빌드와 테스트를 실행합니다.
* 💡 **Mẹo ghi nhớ**: AMJG (Ant, Maven, Jenkins, Gradle).

---

## 36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)
* **IDE**: 코딩, 디버그, 컴파일, 배포 등 모든 작업을 하나의 프로그램에서 처리.
  * **기능**: 코딩(Coding), 컴파일(Compile), 디버깅(Debugging), 배포(Deployment).
* **빌드 도구**: 소스 코드를 실행 가능한 제품 소프트웨어로 변환(Ant, Maven, Gradle).
* **VI (Vietnamese) (Tiếng Việt):** Môi trường phát triển tích hợp (IDE - như Eclipse, VS Code). Chức năng: Code, Dịch, Gỡ lỗi, Triển khai.

---

## 41. 빌드 자동화 도구 심화: Jenkins vs Gradle
* **Jenkins**: JAVA 기반 오픈 소스. 친숙한 Web GUI 제공. 분산 빌드/테스트 가능.
* **Gradle**: Groovy 기반 오픈 소스. 안드로이드 앱 개발 환경에서 주로 사용. DSL을 스크립트 언어로 사용하며 태스크(Task) 단위로 실행. 빌드 캐시(Build Cache)로 속도 향상.
* **VI (Vietnamese) (Tiếng Việt):** Jenkins (dựa trên Java, có Web GUI dễ dùng) và Gradle (dựa trên Groovy, dùng nhiều trong Android, tăng tốc bằng Build Cache).
* 💡 **Mẹo ghi nhớ**: Jenkins = Java, Gradle = Groovy (Android).

---

## 핵심 037 & 038: 매뉴얼 및 빌드/배포 도구 (Manuals & Build/Deploy Tools)

### 제품 소프트웨어 매뉴얼 (Tài liệu hướng dẫn)
- **설치 매뉴얼 (Installation Manual):** Hướng dẫn cài đặt. (Lưu ý cách cài, cấu hình hệ thống, cách xóa cài đặt - Uninstall).
- **사용자 매뉴얼 (User Manual):** Hướng dẫn sử dụng. (Giao diện UI, cấu hình tối thiểu, cách dùng tính năng).
- Cả hai đều phải viết theo góc nhìn của **사용자 (Người dùng)**.

### 빌드 및 모니터링 도구 (Công cụ Build & Monitoring)
- **빌드 자동화 도구 (Build Automation):** Biến source code thành file chạy một cách tự động. Ví dụ: Ant, Maven, Gradle, **Jenkins**.
- **버전 관리 도구 (Version Control):** Git, SVN.
- **정적 분석 도구 (Static Analysis):** Phân tích code tìm lỗi mà **KHÔNG CHẠY** chương trình. Ví dụ: PMD, Cppcheck, SonarQube.
- **동적 분석 도구 (Dynamic Analysis):** Vừa **CHẠY** chương trình vừa tìm lỗi (tràn bộ nhớ, v.v.). Ví dụ: Avalanche, Valgrind.

- **Vietnamese Explanation:** "Tĩnh" (Static) nghĩa là code nằm im trên giấy, dùng tool soi từng dòng xem có viết sai cú pháp hay không. "Động" (Dynamic) là bấm nút chạy phần mềm rồi xem nó có bị sập hay tốn RAM không.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Tĩnh (Static) = PMD, SonarQube (Soi code). Động (Dynamic) = Valgrind (Chạy thử). Build = Jenkins (Ông quản gia tự động).

---

---

## 118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)

- 소스 코드를 실행 파일로 만드는 과정과 배포를 자동화. (Tự động hóa việc dịch code, test và đóng gói phát hành - CI/CD).
- **Jenkins:** Viết bằng Java, chạy trên web (Web GUI). Điểm mạnh là test phân tán trên nhiều máy.
- **Gradle:** Viết bằng Groovy (Ngôn ngữ kịch bản), dùng **DSL**. Điểm mạnh là có **빌드 캐시 (Build Cache)** giúp build lại cực nhanh, thường dùng làm chuẩn cho Android.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Jenkins = Java, Web GUI, Phân tán. Gradle = Groovy, DSL, Cache, Android.

---

---

## 11. DRM (디지털 저작권 관리, Digital Rights Management)
* **구성 요소 (Components)**: 클리어링 하우스 (Clearing House - 권한/결제 관리), 콘텐츠 제공자 (Contents Provider), 패키저 (Packager - 암호화), 콘텐츠 분배자 (Distributor), DRM 컨트롤러 (Controller - 이용 권한 통제).
* **기술 요소 (Technologies)**: 암호화 및 키 관리, 식별체계 표현, 라이선스 발급, 정책 관리, 크랙 방지.
* **VI (Vietnamese) (Tiếng Việt):** Quản lý bản quyền kỹ thuật số. Clearing House xử lý thanh toán/cấp phép. Packager mã hóa nội dung.
* **Example**: 넷플릭스 영상이 녹화가 안 되거나 불법 복제가 안 되는 것이 DRM 기술 덕분입니다.
* 💡 **Mẹo ghi nhớ**: Clearing House = Ngân hàng/Trung tâm kiểm duyệt. Packager = Người đóng gói/Mã hóa.

---

## 100-2 ~ 104: 저작권 및 DRM (Copyright & Digital Rights Management)

### 저작권 (Copyright)
- 창작자가 가지는 **배타적 독점적 권리**. (Quyền độc quyền của tác giả). Phần mềm rất dễ bị copy (`Ctrl+C / Ctrl+V`) nên phải có DRM để bảo vệ.

### DRM의 핵심 구성 요소 (Thành phần chính của DRM)
- **패키저 (Packager):** 콘텐츠 암호화. (Người/Máy đóng gói và khóa file lại).
  - *실시간 패키징:* File nhỏ (Nhạc, ảnh) -> Khách bấm mua mới đóng gói.
  - *사전 패키징:* File to (Phim) -> Đóng gói sẵn trước khi bán.
- **클리어링 하우스 (Clearing House):** 권한, 라이선스, 결제 관리. (Trạm thu phí: Xác thực bạn đã trả tiền chưa, cấp License cho bạn mở file. Quản lý cả tính tiền theo dung lượng/thời gian - 종량제).
- **콘텐츠 분배자 (Distributor):** Nơi bán/phân phối (App Store).
- **DRM 컨트롤러 (Controller):** Phần mềm trên máy khách hàng kiểm soát việc mở file.
- **보안 컨테이너 (Security Container):** Hộp an toàn chứa file gốc để vận chuyển.

### DRM 기술 요소 (Kỹ thuật dùng trong DRM)
- **암호화 (Encryption):** Mã hóa file.
- **키 관리 (Key Management):** Quản lý khóa để mở mã hóa.
- **식별 기술 (Identification):** Gắn mã định danh (DOI, URI) để biết file nào là file nào.
- **저작권 표현 (Right Expression):** Ghi rõ quyền lợi (Vd: XrML - Chỉ cho xem, cấm in).
- **크랙 방지 (Tamper Resistance):** Chống bẻ khóa, chống hack.
- **인증 (Authentication):** Xác minh danh tính người mua.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Packager (Gói hàng + Khóa), Clearing House (Thu tiền + Đưa chìa).

---

---

## 15. 화이트박스 vs 블랙박스 테스트 (White-box vs Black-box Testing)
* **화이트박스 테스트**: 원시 코드를 오픈시킨 상태에서 논리적 경로(제어 구조)를 테스트.
  * **종류**: 기초 경로 검사 (Base Path), 제어 구조 검사 (조건, 루프, 데이터 흐름).
* **블랙박스 테스트**: 기능이 제대로 작동하는지 외부에서 테스트 (내부 구조 안 봄).
  * **종류**: 동치 분할 (Equivalence Partitioning), 경계값 분석 (Boundary Value), 원인-효과 그래프 (Cause-Effect), 오류 예측 (Error Guessing), 비교 검사 (Comparison).
* **VI (Vietnamese) (Tiếng Việt):**
  * White-box: Nhìn thấy code bên trong (kiểm tra đường dẫn, vòng lặp).
  * Black-box: Không nhìn thấy code, chỉ kiểm tra đầu vào/đầu ra (kiểm tra tính năng).
* **Example**: 화이트박스는 코드의 `if-else` 모든 경로를 실행해보는 것이고, 블랙박스는 로그인 창에 ID/PW를 넣어보는 것입니다.
* 💡 **Mẹo ghi nhớ**: White = Nhìn xuyên thấu (Code). Black = Hộp đen không thấy ruột (Chức năng).

---

## 16. 소프트웨어 테스트 단계 (Software Testing Phases)
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

---

## 17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)
* **테스트 오라클 (Test Oracle)**: 테스트 결과가 참인지 판단하기 위해 사전에 정의된 참 값을 대입하여 비교. (참, 샘플링, 추정, 일관성 검사 오라클).
* **테스트 드라이버 (Test Driver)**: (상향식 테스트에서) 하위 모듈을 호출하고 매개 변수를 전달하여 결과를 도출하는 도구. (가짜 메인 프로그램).
* **VI (Vietnamese) (Tiếng Việt):**
  * Test Oracle: Cơ chế/Nguồn chân lý để xác định kết quả đúng hay sai.
  * Test Driver: Chương trình giả lập gọi module con (dùng trong Bottom-up).
* **Example**: 테스트 오라클은 정답지 역할을 합니다.
* 💡 **Mẹo ghi nhớ**: Oracle = Nhà tiên tri/Chân lý. Driver = Người lái xe (Gọi cấp dưới).

---

## 20. 하향식 통합 테스트와 테스트 스텁 (Top-down Integration Test & Test Stub)
* **테스트 스텁 (Test Stub)**: 상향식에서 드라이버를 쓰듯, 하향식 통합 테스트에서는 '스텁(Stub)'이라는 가짜 하위 모듈을 사용.
* 의존성 배제 및 중복성 최소화.
* 일시적으로 필요한 조건만을 가지고 있는 시험용 모듈.
* **VI (Vietnamese) (Tiếng Việt):** Test Stub là module giả lập cấp dưới, dùng trong kiểm thử tích hợp từ trên xuống (Top-down).
* **Example**: 로그인 기능을 먼저 테스트하기 위해, DB 연결 모듈 대신 무조건 "성공"을 반환하는 스텁을 만듭니다.
* 💡 **Mẹo ghi nhớ**: Top-down dùng Stub (T-S), Bottom-up dùng Driver (B-D).

---

## 35. 테스트 케이스 (Test Case)
* 사용자의 요구사항을 정확하게 준수했는지 확인하기 위해 설계된 테스트 항목에 대한 명세서.
* **구성 요소 (ISO/IEC/IEEE 29119-3)**: 
  * 식별자, 테스트 항목, 입력 명세(Input), 출력 명세(Output/예상 결과), 환경 설정, 특수 절차 요구, 의존성 기술.
* **VI (Vietnamese) (Tiếng Việt):** Kịch bản kiểm thử (Test Case). Bao gồm: ID, Môi trường, Đầu vào, Đầu ra mong đợi.
* **Example**: 로그인 기능을 위해 "ID: admin, PW: 1234를 넣었을 때 관리자 페이지로 넘어가는가?"를 문서화한 것입니다.

---

## 42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)
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

---

## 43. 테스트 분류 방식 (Test Classification)
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

---

## 44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)
* **문장(구문) 검증 기준 (Statement Coverage)**: 소스 코드의 **모든 구문**이 한 번 이상 수행되도록 설계.
* **결정/분기 검증 기준 (Decision/Branch Coverage)**: 모든 조건문에 대해 조건이 **True인 경우와 False인 경우**가 한 번 이상 수행되도록 설계.
* **조건 검증 기준 (Condition Coverage)**: 조건문에 포함된 **개별 조건식**의 결과가 T/F 한 번 이상 수행되도록 설계.
* **분기/조건 기준 (Branch/Condition Coverage)**: 위 두 가지를 모두 만족하는 설계.
* **VI (Vietnamese) (Tiếng Việt):** Các tiêu chí độ phủ (Coverage) trong kiểm thử hộp trắng: Bao phủ cú pháp (Statement), Bao phủ nhánh/quyết định (Branch - lệnh IF chạy cả T/F), Bao phủ điều kiện (Condition - từng điều kiện nhỏ chạy cả T/F), Bao phủ nhánh/điều kiện.
* 💡 **Mẹo ghi nhớ**: Statement = Dòng code. Branch = Ngã rẽ (IF). Condition = Điều kiện nhỏ trong IF.

---

## 45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계
개발 단계와 테스트 단계를 짝지어 놓은 모델.
1. **단위 테스트 (Unit Test)** - *구현(Code)* 단계와 짝. 모듈/컴포넌트 초점 (주로 구조 기반/화이트박스).
2. **통합 테스트 (Integration Test)** - *설계(Design)* 단계와 짝. 모듈들을 결합하여 테스트.
   * **하향식 (Top-down)**: 스텁(Stub) 사용. 깊이/넓이 우선. 테스트 초기부터 시스템 구조 파악 가능.
   * **상향식 (Bottom-up)**: 드라이버(Driver)와 클러스터(Cluster) 사용.
3. **시스템 테스트 (System Test)** - *분석(Specification)* 단계와 짝. 실제 환경과 유사하게 구성, 기능적/비기능적 요구사항 점검.
4. **인수 테스트 (Acceptance Test)** - *요구사항(Requirements)* 단계와 짝. 사용자가 직접 테스트. (알파/베타 테스트).
* **VI (Vietnamese) (Tiếng Việt):** Mô hình chữ V (V-Model). Code <-> Unit, Design <-> Integration, Analysis <-> System, Requirements <-> Acceptance.
* **Example**: 코드 짠 사람이 직접 해보는 건 단위 테스트, 고객이 요구사항대로 됐는지 최종 확인하는 건 인수 테스트입니다.

---

## 46. 애플리케이션 테스트 프로세스 (Test Process)
* **순서**: 계획(Plan) → 분석 및 디자인(Analysis & Design) → 케이스 및 시나리오 작성 → 수행(Execution) → 결과 평가 및 리포팅 → 결함 추적 및 관리.
* **결함 (Fault/Defect)**: 설계와 다르게 동작하거나 예상 결과와 일치하지 않는 부분.
* **VI (Vietnamese) (Tiếng Việt):** Quy trình kiểm thử: Lập kế hoạch -> Phân tích -> Viết kịch bản -> Chạy -> Đánh giá -> Theo dõi lỗi (Defect Tracking). Lỗi (Defect) là sự sai lệch giữa kết quả thực tế và mong đợi.

---

## 47. 테스트 오라클의 종류 (Types of Test Oracles)
* **참(True) 오라클**: 모든 입력값에 대해 결과를 제공 (모든 오류 검출).
* **샘플링(Sampling) 오라클**: 특정한 몇몇 입력값에 대해서만 결과 제공.
* **추정(Heuristic) 오라클**: 샘플링 + 나머지 값들은 추정(직관)으로 처리.
* **일관성 검사(Consistent) 오라클**: 변경 전후의 결과값이 동일한지 확인.
* **VI (Vietnamese) (Tiếng Việt):** Các loại Test Oracle: Chân lý (True - biết hết kết quả), Lấy mẫu (Sampling - biết vài cái), Ước lượng (Heuristic - kết hợp lấy mẫu và đoán), Nhất quán (Consistent - trước sau như một).

---

## 48. 테스트 자동화 도구 (Test Automation Tools)
* **정적 분석 도구**: 실행 없이 코드 표준/스타일/복잡도 검사.
* **테스트 케이스 생성 도구**: 자료 흐름도, 기능 테스트, 도메인 분석, 랜덤 등으로 TC 자동 생성.
* **테스트 실행 도구**: 데이터 주도(Data-driven) 및 키워드 주도(Keyword-driven) 스크립트 실행.
* **성능 테스트 도구**: 가상의 사용자를 만들어 부하를 줌.
* **테스트 통제 도구**: 테스트 계획, 형상 관리, 결함 관리.
* **테스트 하네스 도구**: 테스트 환경 시뮬레이션.
* **VI (Vietnamese) (Tiếng Việt):** Các công cụ tự động hóa kiểm thử: Phân tích tĩnh, Tạo TC, Chạy TC, Đo hiệu năng, Quản lý, Test Harness (Môi trường giả lập).

---

## 49. 테스트 하네스 구성 요소 (Test Harness Components)
* **드라이버(Driver)**: 하위 모듈 호출 (상향식).
* **스텁(Stub)**: 가짜 하위 모듈 (하향식).
* **슈트(Suites)**: 테스트 케이스의 집합.
* **케이스(Case)**: 입력 값, 실행 조건, 기대 결과 명세.
* **스크립트(Script)**: 테스트 실행 절차 명세(자동화).
* **목 오브젝트(Mock Object)**: 조건부 입력에 따라 상황에 맞는 행위를 수행하는 가짜 객체.
* **VI (Vietnamese) (Tiếng Việt):** Thành phần của Test Harness: Driver (gọi cấp dưới), Stub (giả cấp dưới), Suites (tập hợp TC), Case (kịch bản), Script (mã chạy tự động), Mock Object (đối tượng giả).

---

## 핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)

### 테스트의 기본 원리 (Các nguyên lý cơ bản)
- **완벽한 테스팅은 불가능:** Không bao giờ test ra 100% không còn lỗi.
- **결함 집중 (Defect Clustering):** Lỗi thường tập trung ở 20% các module cốt lõi (Quy tắc Pareto 80/20).
- **살충제 패러독스 (Pesticide Paradox):** Nghịch lý thuốc trừ sâu. Dùng mãi một bài test thì không tìm ra lỗi mới. Cần liên tục thay đổi bộ test.
- **정황 의존성 (Context Dependency):** Tùy bối cảnh (web, app, game) mà cách test phải khác nhau.
- **오류-부재의 궤변 (Absence of Errors Fallacy):** App không có lỗi nhưng không đúng ý khách hàng thì vẫn là rác.

### 정적 테스트 vs 동적 테스트 (Static vs Dynamic Test)
- **정적 테스트 (Static):** Không chạy code. Đọc và review code/tài liệu. (Walkthrough, Inspection, Review). Phát hiện lỗi sớm, tiết kiệm tiền.
- **동적 테스트 (Dynamic):** Phải chạy chương trình. Gồm Black Box và White Box testing.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Thuốc trừ sâu (Pesticide) = Cần thay mới bộ Test. Đám mây lỗi (Clustering) = 20% code gây ra 80% lỗi.

---

---

## 핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)

- **테스트 케이스 (Test Case):** Một bộ gồm: Dữ liệu đầu vào, Điều kiện chạy, Kết quả mong đợi.
- **테스트 시나리오 (Test Scenario):** Kịch bản gồm nhiều Test Case nối tiếp nhau.
- **테스트 오라클 (Test Oracle):** Tiêu chuẩn/Cơ chế để tự động đánh giá kết quả test là Đúng hay Sai (True/False).
  - **참 (True):** Kiểm tra 100% mọi trường hợp (Dùng cho máy bay, y tế).
  - **샘플링 (Sampling):** Lấy mẫu ngẫu nhiên vài test case.
  - **추정 (Heuristic):** Lấy mẫu vài cái chắc chắn, còn lại thì dùng logic ước lượng (Heuristic).
  - **일관성 검사 (Consistent):** Kiểm tra xem code cũ và mới có cho kết quả giống nhau không khi bị thay đổi (Hồi quy).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Oracle (Nhà tiên tri) = Cái để phán xét đúng/sai. True = 100%. Heuristic = Đoán.

---

---

## 핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)

Cả hai đều là **Dynamic Test** (Phải chạy code).

### 블랙박스 테스트 (Black-box / Hộp đen / Dựa trên Chức năng)
- Không quan tâm bên trong code viết gì, chỉ quan tâm Đầu vào -> Đầu ra. (Dựa trên 명세 - Đặc tả).
- **Kỹ thuật (Các loại):**
  - **동등 분할 (Equivalence Partitioning):** Chia vùng tương đương (Vd: Nhập từ 1-100, thì test số 50 là đủ diện cho vùng đúng).
  - **경곗값 분석 (Boundary Value):** Phân tích giá trị biên (Lỗi hay xảy ra ở ranh giới, vd test số 0, 1, 100, 101).
  - **원인-효과 그래프 (Cause-Effect Graph):** Bảng đồ nhân quả.
  - **오류 예측 (Error Guessing):** Dựa vào kinh nghiệm của tester để đoán lỗi.

### 화이트박스 테스트 (White-box / Hộp trắng / Dựa trên Cấu trúc Code)
- Soi thấu bên trong code. Đảm bảo mọi dòng lệnh (Statement), mọi nhánh (Branch/Decision) đều được chạy ít nhất 1 lần.
- **Kỹ thuật (Các loại):**
  - **기본 경로 검사 (Base Path):** Đi qua tất cả các con đường code.
  - **구문 커버리지 (Statement Coverage):** Bao phủ dòng lệnh (Dễ nhất).
  - **결정 커버리지 (Decision/Branch):** Bao phủ nhánh (If True / If False).
  - **조건 커버리지 (Condition):** Bao phủ mọi điều kiện con trong If.
  - **루프 검사 (Loop Testing):** Test các vòng lặp for, while.

- **Vietnamese Explanation:** Black-box giống như lái xe ô tô: đạp ga là chạy, không cần biết động cơ nổ ra sao. White-box giống như thợ máy: tháo tung động cơ ra kiểm tra từng con ốc, từng pít-tông.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 
  - Black-box (Chức năng): Vùng (Partition), Biên (Boundary), Nhờ kinh nghiệm (Guessing).
  - White-box (Cấu trúc code): Dòng lệnh (Statement), Nhánh (Branch), Điều kiện (Condition), Vòng lặp (Loop).

---

---

## 핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)

Thứ tự Test từ nhỏ đến lớn: **단위 (Unit) → 통합 (Integration) → 시스템 (System) → 인수 (Acceptance)**.

| 단계 (Giai đoạn) | 설명 (Giải thích) | 방식 / 기법 (Cách thức) |
|---|---|---|
| **단위 (Unit Test)** | Test từng Module, hàm độc lập. | White-box, Black-box, Test cấu trúc dữ liệu. |
| **통합 (Integration)** | Nối các module lại và test sự giao tiếp giữa chúng. | - **빅뱅 (Big Bang):** Gom tất cả test 1 lần (dễ bị rối).<br>- **상향식 (Bottom-Up):** Dưới lên. Cần **Driver** (Trình điều khiển giả).<br>- **하향식 (Top-Down):** Trên xuống. Cần **Stub** (Mô đun con giả mạo). |
| **시스템 (System)** | Test toàn bộ hệ thống xem có đúng yêu cầu (Chức năng + Hiệu năng). | Yêu cầu chức năng và phi chức năng. |
| **인수 (Acceptance)** | Khách hàng/Người dùng cuối tự test để nghiệm thu. | - **알파 (Alpha):** Khách hàng test tại cty lập trình viên, có dev đứng ngó.<br>- **베타 (Beta):** Tung ra cho nhiều người dùng tự test ở nhà (Field Test), tự do. |

- **Vietnamese Explanation:** Tích hợp (Integration) rất hay ra thi. Nếu ráp từ dưới lên (Bottom-up) thì module con xong rồi, nhưng thiếu thằng gọi nó => Cần viết cục **Driver** giả để gọi. Nếu ráp từ trên xuống (Top-down), module chính có rồi nhưng chưa viết xong module con => Cần viết cục **Stub** (Cục gạch giả) để thế chỗ. Alpha test là test "nội bộ" có kiểm soát, Beta test là "open beta" như game.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Từ trên xuống (Top-Down) = Stub (Top-Stub / T-S). 상향식 (Bottom-Up) = Driver (Bottom-Driver / B-D). Alpha = Ở cty Dev. Beta = Ở nhà.

---

---

## 핵심 044: 테스트 자동화 도구 (Test Automation Tools)

- **정적 분석 도구 (Static Analysis):** Phân tích không cần chạy code.
- **성능 테스트 도구 (Performance Test):** Tạo ra người dùng ảo (Virtual Users) để ép tải, đo đạc băng thông, thời gian phản hồi (Load/Stress testing).
- **테스트 드라이버 (Test Driver):** Dùng trong Bottom-up. Gọi module con, truyền tham số.
- **테스트 스텁 (Test Stub):** Dùng trong Top-down. Module giả mạo, làm hình nộm trả về kết quả ảo cho module trên.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Driver (Tài xế) = Kẻ điều khiển từ trên. Stub (Gốc cây/Khúc gỗ) = Đứng ở dưới chịu đòn giả.

---

## 097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)

**Quy trình 5 bước (5 단계):**
1. **계획 및 제어 (Planning & Control):** Lập kế hoạch, mục tiêu, chi phí.
2. **분석 및 설계 (Analysis & Design):** Viết Kịch bản (Test Scenario) và Ca kiểm thử (**Test Case**).
3. **구현 및 실현 (Implementation & Execution):** Viết Thủ tục test (**Test Procedure** - Trình tự chạy các case) và Thực thi test.
4. **평가 (Evaluation):** Đánh giá kết quả xem đạt chưa.
5. **완료 (Completion):** Lưu trữ hồ sơ, bàn giao.

- **Vietnamese Explanation:** Test Case là danh sách các món ăn cần nấu (Ví dụ: Trứng rán). Test Procedure là công thức nấu (Bước 1 bật bếp, bước 2 đập trứng). Phải có món (Case) rồi mới ghi công thức (Procedure) được.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Kế hoạch -> Phân tích (Ra Test Case) -> Thực hiện (Ra Test Procedure) -> Đánh giá -> Hoàn thành. (Kế Phân Thực Đánh Hoàn (Kế hoạch - Phân tích - Thực hiện - Đánh giá - Hoàn thành)).

---

---

## 105: 시각에 따른 테스트 (Verification vs Validation)

- **검증 (Verification - Xác minh):** 개발자 시각 (Góc nhìn Dev). "Làm đúng thiết kế/mã code không?". (Are we building the product right?).
- **확인 (Validation - Thẩm định):** 사용자 시각 (Góc nhìn User). "Phần mềm này có đúng cái khách hàng cần không?". (Are we building the right product?).

- 💡 **Mẹo ghi nhớ (Mnemonics):** 검증 (Verification) = Code chuẩn chưa? (Dev). 확인 (Validation) = Khách ưng không? (User).

---

---

## 120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)

### 테스트의 기본 원리 (Nguyên lý cơ bản)
- **완벽한 테스트 불가능:** Không thể khẳng định 100% hết bug.
- **파레토 법칙 (Pareto):** 80% bug nằm ở 20% code cốt lõi. (Đám mây lỗi).
- **살충제 패러독스 (Pesticide Paradox):** Test hoài 1 kịch bản sẽ bị "nhờn", phải liên tục thay đổi bộ test.
- **정황 의존 (Context):** Tùy thuộc ngữ cảnh (Web, Game) mà test khác nhau.

### 테스트 분류 (Phân loại Test)
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

---

## 127 ~ 129: 화이트박스 테스트 (White Box Test)

- 내부 로직과 제어 구조를 직접 관찰. (Test dựa trên mã nguồn (Source Code). Nhìn thấu bên trong).
- **종류 (Các kỹ thuật):** 기초 경로 (Đường dẫn cơ bản), 조건 (Điều kiện), 루프 (Vòng lặp), 데이터 흐름 (Luồng dữ liệu).
- **검증 기준 (Coverage - Mức độ bao phủ):**
  - **문장 검증 (Statement):** Mọi dòng code phải chạy qua 1 lần.
  - **분기/결정 검증 (Branch/Decision):** Mọi nhánh lệnh (If True / False) phải chạy qua 1 lần.
  - **조건 검증 (Condition):** Mọi biểu thức điều kiện con bên trong If phải kiểm tra T/F.

- 💡 **Mẹo ghi nhớ (Mnemonics):** White Box = Code (Câu lệnh, Rẽ nhánh, Vòng lặp). Do Dev tự làm.

---

---

## 130 & 131: 블랙박스 테스트 (Black Box Test)

- 명세를 기초로 기능 테스트. 내부 구조 무시. (Dựa vào chức năng UI, không thèm nhìn code).
- **종류 (Các kỹ thuật):**
  - **동치 분할 (Equivalence Partitioning):** Chia vùng tương đương (Nhập đại 1 số đại diện).
  - **경계값 분석 (Boundary Value):** Test quanh cái mép (Max, Min, +1, -1). Lỗi hay nằm ở đây.
  - **원인-효과 그래프 (Cause-Effect):** Vẽ biểu đồ nhân quả.
  - **오류 예측 (Error Guessing):** Dựa vào kinh nghiệm (Kinh nghiệm Tester).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Black Box = UI, Chức năng. Các kỹ thuật thường chia theo vùng (Partition) và ranh giới (Boundary).

---

---

## 132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)

Thực hiện theo mô hình V (V-Model), từ nhỏ đến lớn:

1. **단위 테스트 (Unit Test):** Test từng Module con. Thường dùng White Box.
2. **통합 테스트 (Integration Test):** Ghép các module lại. (Có thể test kiểu Big Bang - Gom 1 cục, hoặc dần dần từ trên xuống, từ dưới lên). Tìm lỗi giao tiếp (Interface).
3. **시스템 테스트 (System Test):** Test toàn bộ hệ thống trong môi trường giống thực tế nhất. Đánh giá tính năng + hiệu năng (Bảo mật, tốc độ).
4. **인수 테스트 (Acceptance Test):** Khách hàng test để nghiệm thu.
   - **알파 (Alpha):** Khách hàng test tại văn phòng dev (có dev đứng xem).
   - **베타 (Beta):** Khách hàng tự test ở nhà (Giống Game Open Beta).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Đơn vị (Unit) -> Tích hợp (Integration) -> Hệ thống (System) -> Nghiệm thu (Acceptance). Alpha = Nội bộ, Beta = Ở nhà.

# 136-1. 통합 테스트 (Integration Test - Kiểm thử tích hợp)

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

**[1] 개념 (Khái niệm):** 결합 테스트 시 미구현된 모듈을 대체하거나 구동하기 위한 가짜(Dummy) 모듈.
*(Module giả lập được dùng thay thế cho các module chưa hoàn thiện trong quá trình kiểm thử tích hợp.)*

**[2] 비교 (So sánh):**
- **드라이버 (Driver):** 상위 모듈 대체. 하위 모듈을 호출하고 매개변수 전달. (Dùng trong Bottom-Up).
- **스텁 (Stub):** 하위 모듈 대체. 상위 모듈의 호출에 단순 응답(결과값)만 제공. (Dùng trong Top-Down).

*(Ví dụ và mẹo nhớ đã tích hợp ở mục 137 & 138 phía trên để tránh lặp lại).*

---

# 140. 회귀 테스팅 (Regression Testing - Kiểm thử hồi quy)

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

**[1] 개념 (Khái niệm):** 시스템이나 모듈을 테스트하기 위해 생성된 코드와 데이터의 집합 (환경).
*(Môi trường bao gồm các đoạn code giả lập, dữ liệu và công cụ để thực thi test).*

**[2] 구성 요소 (Thành phần chính):**
- **Driver / Stub:** (Đã giải thích ở trên).
- **Test Suite (테스트 슈트):** 테스트 케이스들의 집합 (Tập hợp các test case).
- **Test Script (테스트 스크립트):** 자동화된 테스트 실행 절차를 기록한 명세서 (Kịch bản code chạy tự động).
- **Mock Object (목 오브젝트):** 사용자의 예정된 행위를 조건부로 입력해 둔 가짜 객체 (Đối tượng giả lập dữ liệu trả về).

---

# 148. 결함 (Fault / Defect)

**[1] 개념 (Khái niệm):** 소프트웨어가 개발자의 설계와 다르게 동작하거나 잘못된 결과를 발생시키는 현상 (Bug).
*(Bất kỳ lỗi, thiếu sót nào khiến phần mềm chạy không đúng với tài liệu đặc tả yêu cầu).*

**[2] 예시 (Ví dụ thực tế):** 
- Thiết kế: Nút "Hủy" phải có màu Đỏ. Thực tế: Lập trình viên làm nút "Hủy" màu Xanh $\rightarrow$ Đây cũng được tính là một 결함 (Fault) dù không gây crash app.

---

# 149 ~ 151. 성능 분석, 빅오 표기법, 순환 복잡도 (Performance Analysis, Big-O, Cyclomatic Complexity)

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
- **공식 (Công thức):** $V(G) = E - N + 2$ 
  *(E: Edge - số mũi tên, N: Node - số nút).*

**[4] 예시 (Ví dụ thực tế):**
- **Throughput vs Response Time:** Một quán phở có thể bán 100 bát/giờ (Throughput = 100). Nhưng khách vào gọi món phải chờ 15 phút mới bê ra (Response time = 15m).
- **McCabe $V(G)$:** Nếu vẽ sơ đồ luồng (Flowchart) của hàm If-Else có 4 Node và 4 Edge $\rightarrow$ $V(G) = 4 - 4 + 2 = 2$ (Có 2 đường đi độc lập).

> 💡 **Mẹo ghi nhớ (Mnemonics):** 
> - Công thức McCabe: **E**m **N**hớ **+ 2** ($E - N + 2$).

---

# 152 & 153. 소스 코드 최적화 및 품질 분석 (Source Code Optimization & Quality Analysis)

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

**[1] 개념 (Khái niệm):** 시스템 파일의 변경 유무를 확인하고 파일 변동 시 관리자에게 알려주는 보안 도구.
*(Công cụ bảo mật kiểm tra xem tệp hệ thống có bị thay đổi trái phép không và cảnh báo cho quản trị viên).*

**[2] 핵심 키워드 (Từ khóa chính):** 해시(Hash) 함수, 백도어(Backdoor) 감지.
- **도구 종류 (Các công cụ phổ biến):** Tripwire, AIDE, Samhain, Claymore, Fcheck.

**[3] 예시 (Ví dụ thực tế):**
- Hacker cài **Backdoor (Cửa hậu)** vào file `login.php`. Công cụ Tripwire sử dụng hàm băm (Hash) và phát hiện ra mã băm của `login.php` hôm nay khác với hôm qua $
ightarrow$ Phát chuông cảnh báo.

---

# 161. 인터페이스 구현 검증 도구 (Interface Implementation Verification Tools)

**[1] 개념 (Khái niệm):** 구현된 인터페이스가 정상적으로 작동하는지 확인하기 위해 사용되는 테스트 자동화 프레임워크.
*(Khung tự động hóa kiểm thử để xác minh giao diện kết nối hoạt động bình thường).*

**[2] 도구 종류 (Các công cụ):**
- **FitNesse:** 웹 기반 테스트 (Kiểm thử trên nền Web).
- **Selenium:** 웹 브라우저 검증 (Hỗ trợ đa trình duyệt, cực kỳ phổ biến).
- **watir:** Ruby 기반 프레임워크 (Dùng ngôn ngữ Ruby).
- **NTAF:** FitNesse + STAF (Công cụ nội bộ do Naver phát triển).

---

# 162. APM (Application Performance Management)

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

---

## 50. 애플리케이션 성능 측정 지표 (Performance Metrics)
* **처리량 (Throughput)**: 일정 시간 내 처리하는 일의 양.
* **응답 시간 (Response Time)**: 요청을 전달한 후 '응답이 도착할 때'까지 걸린 시간.
* **경과 시간 (Turn Around Time)**: 작업을 의뢰한 후 '처리가 완료될 때'까지 걸린 시간.
* **자원 사용률 (Resource Usage)**: CPU, 메모리, 네트워크 등의 자원 사용량.
* **VI (Vietnamese) (Tiếng Việt):** Các chỉ số hiệu năng: Thông lượng (Throughput), Thời gian phản hồi (Response), Thời gian hoàn thành (Turn Around), Mức sử dụng tài nguyên (Resource Usage).
* **Example**: 식당에서 주문하고 물이 나오는 시간(응답 시간), 음식을 다 먹고 나오는 시간(경과 시간).
* 💡 **Mẹo ghi nhớ**: Response = Phản hồi đầu tiên. Turn Around = Hoàn thành toàn bộ.

---

## 55. APM (애플리케이션 성능 관리/모니터링)
* 애플리케이션의 성능 관리를 위해 자원 현황, 트랜잭션 등을 모니터링.
* **리소스 방식**: Nagios, Zabbix, Cacti.
* **엔드투엔드(End-to-End) 방식**: VisualVM, 제니퍼(Jennifer), 스카우터(Scouter).
* **VI (Vietnamese) (Tiếng Việt):** Công cụ giám sát hiệu năng (APM). Có 2 loại: Theo dõi tài nguyên (Nagios) và Từ đầu đến cuối (VisualVM, Scouter).

---
*(이하 전자계산기 구조 파트 - Computer Architecture)*

---

---

## 24. 인터페이스 보안 - 네트워크 영역 (Interface Security - Network Area)
* 네트워크 트래픽에 대한 암호화 설정.
* **방식**: IPSec, SSL, S-HTTP 등.
* **VI (Vietnamese) (Tiếng Việt):** Bảo mật giao diện vùng mạng (mã hóa lưu lượng). Dùng IPSec, SSL, S-HTTP.
* **Example**: 웹사이트 주소가 `https://`로 시작하면 SSL이 적용된 것입니다.

---

## 26. 인터페이스 구현 검증 도구 (Interface Verification Tools)
* **xUnit**: 다양한 언어에 적용되는 단위 테스트 프레임워크 (JUnit, CppUnit, NUnit).
* **STAF**: 서비스 호출 및 컴포넌트 재사용 등 다양한 환경 지원.
* **FitNesse**: 웹 기반 테스트 케이스 설계, 실행, 결과 확인.
* **NTAF**: FitNesse와 STAF의 장점을 통합한 NHN(Naver)의 테스트 자동화 프레임워크.
* **watir**: Ruby 기반 웹 애플리케이션 테스트 프레임워크.
* **VI (Vietnamese) (Tiếng Việt):** Các công cụ kiểm thử giao diện. xUnit (kiểm thử đơn vị), STAF, FitNesse (Web), NTAF (Naver), watir (Ruby).
* 💡 **Mẹo ghi nhớ**: xUnit là phổ biến nhất cho Unit Test. NTAF có chữ N (Naver).

---

## 핵심 046: 인터페이스 설계 확인 (EAI 구축 유형 - EAI Integration Types)

- **EAI (Enterprise Application Integration):** Doanh nghiệp có nhiều phần mềm (Kế toán, Nhân sự, Kho...), EAI giúp chúng nói chuyện được với nhau.

| 유형 (Kiểu) | 기능 (Chức năng) |
|---|---|
| **Point-to-Point** | 1:1로 연결 (Nối trực tiếp 1-1). Không có Middleware ở giữa. Khó thay đổi. |
| **Hub & Spoke** | 단일 접점인 허브 시스템을 통해 데이터를 전송하는 중앙 집중형. (Nối kiểu nan hoa xe đạp. Tập trung vào cái Hub ở giữa. Hub sập là chết hết.) |
| **Message Bus** | 미들웨어(버스)를 두어 처리하는 방식. 확장성이 뛰어나며 대용량 처리가 가능. (Dùng một trục xe bus (Middleware) ở giữa. Rất dễ mở rộng và xử lý lượng lớn.) |
| **Hybrid** | 그룹 내에서는 Hub & Spoke, 그룹 간에는 Message Bus. (Lai tạp: Trong nhóm thì dùng Hub, giữa các nhóm thì dùng Bus.) |

- 💡 **Mẹo ghi nhớ (Mnemonics):** Hub & Spoke = Nan hoa (Có tâm Hub, sập tâm là chết). Message Bus = Xe buýt (Chở được nhiều, dễ mở rộng).

---

---

## 핵심 047: 인터페이스 보안, 기능 구현 및 검증 (Interface Security, Implementation, Verification)

### 네트워크 보안 기술 (Kỹ thuật bảo mật mạng)
- **IPSec (IP Security):** 네트워크 계층 (Network Layer). Chống giả mạo, ẩn giấu gói tin IP.
- **SSL (Secure Socket Layer):** TCP/IP ~ 애플리케이션 계층 사이. Chứng thực, mã hóa (thường dùng cho HTTPS).
- **S-HTTP:** 애플리케이션 계층 (Application Layer). Mã hóa mọi tin nhắn giữa Client và Server.

### 인터페이스 데이터 포맷 (Định dạng dữ liệu giao tiếp)
- **AJAX:** Bất đồng bộ (Asynchronous), dùng JS và XML để cập nhật một phần trang web mà không cần tải lại toàn bộ trang.
- **JSON:** Cặp "Key-Value", định dạng nhẹ, dễ đọc (Thay thế cho XML rất nhiều).
- **XML:** Thẻ Markup đa mục đích (như HTML nhưng tự tạo thẻ được).
- **YAML:** "YAML Ain't Markup Language". Định dạng dữ liệu tuần tự hóa, rất dễ đọc cho con người (hay dùng làm file config).

### 인터페이스 구현 검증 도구 (Công cụ kiểm chứng Test Interface)
- **xUnit:** Test từng "Đơn vị" (Unit) - jUnit, cppUnit.
- **STAF:** Test trong "Môi trường phân tán" (Distributed environment).
- **FitNesse:** Framework test nền web (Điền bảng là tự chạy test).
- **NTAF:** Kết hợp FitNesse + STAF (Do Naver làm).

- **Vietnamese Explanation:** Khi gửi dữ liệu giữa các máy, JSON đang là vua vì nhẹ và dễ nhìn. YAML thì thường dùng để cấu hình server. Khi test xem các máy tính nói chuyện với nhau ổn không, người ta dùng xUnit (Test từng hàm) hoặc STAF (Test qua nhiều máy).
- 💡 **Mẹo ghi nhớ (Mnemonics):** IPSec = Tầng Mạng (IP). SSL = Tầng giữa (Socket). JSON = Key-Value. STAF = Phân tán (Phân tán (Distributed)).

---

# [복습 / 심화 노트 - Revision & Deep Dive Notes]

---

---

## 9. 스키마 3계층 (Three-Schema Architecture)
* **외부 스키마 (External Schema)**: 사용자나 프로그래머 입장에서 필요한 논리적 구조.
* **개념 스키마 (Conceptual Schema)**: 전체적인 논리적 구조, 개체 간 관계/제약조건, 보안/무결성 규칙.
* **내부 스키마 (Internal Schema)**: 물리적 저장장치 입장에서 본 구조 (레코드 형식, 물리적 순서).
* **VI (Vietnamese) (Tiếng Việt):**
  * External: Góc nhìn của người dùng (User view).
  * Conceptual: Cấu trúc logic tổng thể, quan hệ, bảo mật.
  * Internal: Cấu trúc lưu trữ vật lý.
* **Example**: DB의 전체 테이블 구조는 개념 스키마, 사용자가 보는 뷰(View)는 외부 스키마, 파일 저장 방식은 내부 스키마.
* 💡 **Mẹo ghi nhớ**: Ngoài (Người dùng) - Giữa/Khái niệm (Tổng thể logic) - Trong (Lưu trữ vật lý).

---

## 14. 파레토 법칙 (Pareto Principle)
* 소프트웨어 테스트에서 오류의 80%는 전체 모듈의 20% 내에서 발견된다는 법칙.
* **VI (Vietnamese) (Tiếng Việt):** Nguyên lý 80/20. 80% lỗi nằm trong 20% module cốt lõi.
* **Example**: 시스템에 10개의 모듈이 있다면, 대부분의 버그는 핵심 모듈 2개에 몰려있습니다.
* 💡 **Mẹo ghi nhớ**: Pareto = 80/20.

---

## 18. 최악의 시간 복잡도 (Worst-case Time Complexity)
* **O(1)**: 입력값 크기에 관계 없이 일정. (스택 삽입/삭제).
* **O(n log n)**: n log n번 수행. (힙 정렬, 병합 정렬).
* **VI (Vietnamese) (Tiếng Việt):** Độ phức tạp thời gian. O(1) là hằng số, O(n log n) cho Heap/Merge sort.
* **Example**: 데이터가 아무리 많아도 스택의 최상단에 값을 넣는 것은 1번의 연산만 필요하므로 O(1)입니다.

---

## 19. 클린 코드 작성 원칙 (Clean Code Principles)
* **가독성 (Readability)**: 누구든지 코드를 쉽게 읽을 수 있도록 작성.
* **단순성 (Simplicity)**: 코드를 간단하게 작성.
* **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc viết code sạch. Dễ đọc, đơn giản.
* **Example**: 변수 이름을 `a` 대신 `userCount`로 짓는 것이 가독성을 높이는 것입니다.

---

## 21. 외계인 코드 (Alien Code)
* 아주 오래되거나 참고문서/개발자가 없어 유지보수 작업이 어려운 코드.
* **VI (Vietnamese) (Tiếng Việt):** Alien Code là mã nguồn quá cũ, không có tài liệu hoặc người phát triển gốc, rất khó bảo trì.
* **Example**: 20년 전에 퇴사한 직원이 주석 없이 짠 코드가 외계인 코드입니다.
* 💡 **Mẹo ghi nhớ**: Alien = Người ngoài hành tinh, đọc không hiểu gì cả.

---

## 22. 정적 분석 도구 (Static Analysis Tools)
* 코드를 실행하지 않고(하드웨어/소프트웨어적으로) 소스 코드 품질을 분석하는 도구.
* **종류**: pmd, checkstyle, cppcheck 등.
* **VI (Vietnamese) (Tiếng Việt):** Công cụ phân tích tĩnh, phân tích source code mà không cần chạy chương trình.
* **Example**: 코딩 표준을 잘 지켰는지 검사하는 Checkstyle.

---

## 23. EAI 구축 유형 (Enterprise Application Integration Types)
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

---

## 25. 트립와이어 (tripwire)
* 크래커가 침입하여 백도어를 만들어 놓거나, 설정 파일을 변경했을 때 분석하는 데이터 무결성 검사 도구.
* **VI (Vietnamese) (Tiếng Việt):** Công cụ kiểm tra tính toàn vẹn dữ liệu, phát hiện backdoor hoặc thay đổi file cấu hình.
* 💡 **Mẹo ghi nhớ**: Tripwire = Dây bẫy, chạm vào là báo động.

---

## 27. JSON 및 AJAX (JSON & AJAX)
* **JSON (JavaScript Object Notation)**: 속성-값 쌍(Attribute-Value Pairs)으로 이루어진 데이터 객체를 전달하기 위한 개방형 표준 포맷. 사람이 읽기 쉬움.
* **AJAX (Asynchronous JavaScript and XML)**: 자바스크립트를 이용한 비동기 통신 기술. 클라이언트-서버 간 XML(또는 JSON) 데이터를 교환 및 제어.
* **VI (Vietnamese) (Tiếng Việt):**
  * JSON: Định dạng dữ liệu dạng Key-Value dễ đọc.
  * AJAX: Công nghệ giao tiếp bất đồng bộ, tải dữ liệu mà không cần tải lại toàn bộ trang.
* **Example**: 좋아요 버튼을 눌렀을 때 페이지 이동 없이 하트가 채워지는 것이 AJAX 기술입니다.

---

## 28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)
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

---

## 33. DBMS (데이터베이스 관리 시스템)
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

---

## 38. 릴리즈 노트 (Release Note)
* 소프트웨어 배포(릴리즈) 정보를 최종 사용자와 공유하기 위한 문서 (초기/추가 배포 시 제공).
* 개발팀에서 직접 현재 시제로 정확한 완전한 정보를 기반으로 작성.
* **항목**: 머릿말(Header), 개요, 목적, 문제 요약, 재현 항목, 수정/개선 내용, 사용자 영향도, SW 지원 영향도, 면책 조항 등.
* **VI (Vietnamese) (Tiếng Việt):** Ghi chú phát hành. Chia sẻ thông tin cập nhật, lỗi đã sửa cho người dùng.
* **Example**: 앱스토어에서 앱 업데이트 시 적혀있는 "새로운 기능 및 버그 수정" 목록이 릴리즈 노트입니다.
* 💡 **Mẹo ghi nhớ**: Release Note = Nhật ký cập nhật phần mềm.

---

## 51. 빅오 표기법 (Big-O Notation) 심화
* **O(1)**: 스택 삽입/삭제.
* **O(log_2 n)**: 이진 트리, 이진 검색 (단계가 절반씩 줄어듦).
* **O(n)**: 1중 for문.
* **O(n log_2 n)**: 힙 정렬, 2-Way 합병 정렬.
* **O(n^2)**: 삽입, 선택, 버블, 퀵 정렬(최악). 2중 for문.
* **O(2^n)**: 피보나치 수열.
* **VI (Vietnamese) (Tiếng Việt):** Độ phức tạp thuật toán Big-O. O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n).

---

## 52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)
* **소스 코드 최적화**: 배제해야 할 '나쁜 코드(Bad Code - 스파게티 코드, 외계인 코드)'와 작성해야 할 '클린 코드(Clean Code - 가독성, 단순성, 의존성 배제, 중복성 최소화, 추상화)'가 있음.
* **순환 복잡도 (McCabe's Cyclomatic Complexity)**: 프로그램 논리의 복잡도를 측정.
  * 계산 방법: `V(G) = 화살표 수(E) - 노드 수(N) + 2` 또는 제어 흐름도의 닫힌 영역 수 + 1.
* **소스 코드 품질 분석 도구 심화**:
  * **정적 분석 도구**: pmd, cppcheck, SonarQube, checkstyle, ccm.
  * **동적 분석 도구**: Avalanche, Valgrind (메모리 누수, 스레드 결함 발견).
* **VI (Vietnamese) (Tiếng Việt):** Tối ưu mã nguồn & Độ phức tạp Cyclomatic (McCabe). 
  * Clean code > Bad code (Spaghetti/Alien).
  * V(G) = Cạnh(E) - Đỉnh(N) + 2. Số V(G) chính là số lượng test case cơ bản cần thiết.
  * Công cụ tĩnh (không chạy code): SonarQube. Động (chạy code tìm rò rỉ bộ nhớ): Valgrind.

---

## 53. EAI와 ESB 심화 (EAI vs ESB)
* **EAI**: 기업 내 애플리케이션들을 연동하는 솔루션 (Point-to-Point, Hub&Spoke, Message Bus, Hybrid).
* **ESB (Enterprise Service Bus)**: 애플리케이션 간 표준 기반 인터페이스 제공. 애플리케이션 통합보다는 **서비스 중심 통합** 지향. 결합도(Coupling)를 **약하게(Loosely)** 유지.
* **VI (Vietnamese) (Tiếng Việt):** So sánh EAI và ESB. EAI tập trung tích hợp ứng dụng, ESB tập trung tích hợp dịch vụ (Service-oriented) với độ kết dính lỏng lẻo (Loosely coupled) dùng tiêu chuẩn chung.

---

## 54. XML 및 데이터 무결성 검사 도구 (XML & Integrity Check Tools)
* **XML (eXtensible Markup Language)**: HTML의 비호환성과 SGML의 복잡성을 해결하기 위해 만든 다목적 마크업 언어.
* **인터페이스 보안 - 네트워크 영역 (IPSec)**: 네트워크 계층에서 IP 패킷 단위의 데이터 변조 방지 (양방향 암호화 지원).
* **데이터 무결성 검사 도구**: 시스템 파일 변경 유무 확인 (해시 함수 이용). 백도어 탐지.
  * **종류**: Tripwire, AIDE, Samhain, Claymore, Slipwire, Fcheck.
* **VI (Vietnamese) (Tiếng Việt):** XML khắc phục nhược điểm của HTML/SGML. Công cụ kiểm tra tính toàn vẹn dữ liệu (phát hiện backdoor/thay đổi file) dùng hàm Hash: Tripwire, AIDE.

---

## 023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)

자료구조: 컴퓨터상 자료를 효율적으로 저장하기 위해 만들어진 논리적인 구조 (Cấu trúc logic để lưu trữ dữ liệu hiệu quả).

### 선형 구조 (Linear - Nối tiếp nhau)
- **리스트 (List):** 순서에 의해 나열된 구조. (Cấu trúc tuyến tính).
  - **선형 리스트 (Linear List / Array):** Kích thước cố định (고정), lưu liên tục (연속). Tìm kiếm cực nhanh (검색 빠름), nhưng chèn/xóa cực chậm (삽입, 삭제 느림).
  - **연결 리스트 (Linked List):** Kích thước linh hoạt (가변), liên kết bằng Pointer. Chèn/xóa cực nhanh, nhưng tìm kiếm chậm (phải dò từng cái) và tốn không gian lưu Pointer.
- **스택 (Stack):** LIFO (Last-In-First-Out). Vào/Ra ở một đầu. Dùng cho: Gọi hàm (Subroutine), Lưu địa chỉ trở về, Đệ quy (Recursion), Tính biểu thức toán học, DFS (Duyệt sâu).
- **큐 (Queue):** FIFO (First-In-First-Out). Vào một đầu, ra một đầu. Dùng cho: Lập lịch hệ điều hành (Job Scheduling), Hàng đợi in.
- **데크 (Deque):** Kết hợp Stack và Queue, có thể Vào/Ra ở CẢ HAI đầu.

### 비선형 구조 (Non-linear - Không nối tiếp)
- **트리 (Tree):** Cây. Có Node (Đỉnh) và Branch (Nhánh). **Không có chu trình (Cycle).**
- **그래프 (Graph):** Đồ thị. Có Đỉnh (Vertex) và Cạnh (Edge). Có thể có hướng hoặc vô hướng. (Cây là một dạng Đồ thị không có chu trình).

- **Vietnamese Explanation:** Cấu trúc dữ liệu là cách sắp xếp thông tin. 
  - Linear List như dãy ghế đá (tìm số ghế thì nhanh, nhưng muốn chen vào giữa phải bắt mọi người xích ra). 
  - Linked List như trò chơi nắm tay nhau (muốn chen vào giữa chỉ cần thả tay và nắm người mới, rất dễ, nhưng tìm người thứ 10 thì phải đếm từ đầu).
  - Stack như hộp bóng bàn (LIFO - vứt vào sau thì lấy ra trước). Queue như xếp hàng mua vé (FIFO - ai đến trước mua trước).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Stack = LIFO (Gọi Hàm, Đệ quy). Queue = FIFO (Lập lịch). Liên kết (Linked) = Nhanh chèn/xóa, Chậm tìm kiếm.

---

---

## 027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)

### 알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)
- **분할과 정복 (Divide & Conquer):** Chia để trị. Chia nhỏ vấn đề đến khi không chia được nữa rồi gộp lại. (VD: Merge Sort, Quick Sort).
- **동적계획법 (Dynamic Programming - Quy hoạch động):** Chia bài toán, nhưng CÓ lưu lại kết quả (bộ nhớ) để tận dụng cho lần sau. (VD: Fibonacci).
- **탐욕법 (Greedy):** Tham lam. Chọn cái tốt nhất ở *ngay thời điểm hiện tại*, không cần biết tương lai.
- **백트래킹 (Backtracking):** Quay lui. Đi thử, nếu thấy bế tắc (không triển vọng - promising) thì quay lại nút cha.

### 시간 복잡도 (Time Complexity - Độ phức tạp thời gian)
- Đếm số lần thực thi các phép toán (không phải tính thời gian bằng giây).
- Biểu diễn: Big-O (최악 - Tệ nhất), Theta (평균 - Trung bình), Omega (최상 - Tốt nhất).
- **Thứ tự (Nhanh -> Chậm):** O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
- O(1) nghĩa là: Dữ liệu lớn đến đâu thời gian vẫn không đổi.

- **Vietnamese Explanation:** Greedy giống như đi nhặt tiền: cứ thấy tờ to nhất trước mặt là nhặt, bất chấp sau đó dẫn vào ngõ cụt. Dynamic Programming giống như làm toán: kết quả bài 1 lưu ra nháp để dùng cho bài 2.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Divide = Cắt nhỏ. Dynamic = Nhớ bài cũ. Greedy = Tham bát bỏ mâm. Backtrack = Đi lùi. O(1) là nhanh nhất.

---

---

## 핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)

- **재사용 (Reuse):** 이미 개발되어 인정받았던 소프트웨어의 전체 또는 일부분을 다시 사용하는 기법. (Sử dụng lại code/phần mềm cũ đã được kiểm chứng để tiết kiệm thời gian, chi phí và giảm lỗi.)
- **Phân loại theo kỹ thuật:**
  - **분석 (Analysis):** Hiểu code cũ để chọn cái cần tái sử dụng.
  - **재구조 (Restructuring):** Đổi cấu trúc, không đổi chức năng.
  - **역공학 (Reverse Engineering):** Dịch ngược từ code ra bản thiết kế.
  - **이식 (Migration):** Chuyển sang môi trường / phần cứng mới.
  - **재개발 (Re-Development):** Đập đi xây lại có tham khảo cái cũ.
- **Phân loại theo phạm vi:**
  - Hàm & Đối tượng (Function/Class), Component, Ứng dụng (Application).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Reverse Engineering (Dịch ngược) = Từ Code -> Bản thiết kế. Migration = Chuyển nhà (môi trường).

---

# Chapter 3. 제품 소프트웨어 패키징 (Product Software Packaging)

---

## 핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)

- **ISO/IEC 9126:** Đánh giá chất lượng phần mềm gồm 6 đặc tính: **기신사효유이**
  - **기**능성 (Functionality): Đáp ứng đúng yêu cầu.
  - **신**뢰성 (Reliability): Chạy ổn định, không lỗi, chịu lỗi tốt.
  - **사**용성 (Usability): Dễ hiểu, dễ học, dễ dùng.
  - **효**율성 (Efficiency): Tốn ít tài nguyên, chạy nhanh.
  - **유**지 보수성 (Maintainability): Dễ sửa chữa, bảo trì, phân tích.
  - **이**식성 (Portability): Dễ cài đặt, dễ chuyển sang môi trường/máy khác.
- **ISO/IEC 14598:** Tiêu chuẩn đánh giá quá trình mua/phát triển.
- **ISO/IEC 12119:** Tiêu chuẩn cho gói phần mềm thương mại.
- **ISO/IEC 25000 (SQuaRE):** Tích hợp tất cả các tiêu chuẩn 9126, 14598, 12119.

- **Vietnamese Explanation:** ISO 9126 là kinh điển nhất, bạn phải nhớ 6 chữ cái đầu của 6 đặc tính. Nếu phần mềm khó dùng => Kém "Sử dụng tính". Nếu đổi máy tính mà không chạy được => Kém "Di thực tính" (Portability).
- 💡 **Mẹo ghi nhớ (Mnemonics):** 6 Đặc tính của 9126: "Chức Tín Dùng Hiệu Bảo Di" (Chức năng - Đáng tin - Dễ dùng - Hiệu quả - Bảo trì - Di động). ISO 25000 = Chuẩn xịn nhất tổng hợp tất cả.

---

# Chapter 4. 애플리케이션 테스트 관리 (Application Test Management)

---

## 핵심 클린 코드 작성 원칙 (Clean Code Principles)

- **클린 코드 (Clean Code):** 누구나 쉽게 이해하고 수정 및 추가할 수 있는 단순 명료한 코드. (Code sạch: Dễ hiểu, dễ sửa, dễ thêm tính năng.)
- **배드 코드 (Bad code):** 프로그램의 로직이 복잡하고 이해하기 어려운 코드. (Code rác: Lộn xộn, logic phức tạp.)
- **외계인 코드 (Alien Code):** 매우 오래되거나 참고 문서 또는 개발자가 없어 유지보수 작업이 매우 어려운 코드. (Code "người ngoài hành tinh": Code cổ đại, người viết đã nghỉ việc, không có tài liệu, đụng vào là hỏng.)

| 작성 원칙 (Nguyên tắc) | 설명 (Giải thích) |
|---|---|
| **가독성 (Readability)** | 누구든지 코드를 쉽게 읽을 수 있도록 작성. 이해하기 쉬운 용어, 들여쓰기. (Dễ đọc: Tên biến rõ ràng, thụt lề chuẩn.) |
| **단순성 (Simplicity)** | 한 번에 한 가지를 처리하도록 작성, 최소 단위로 분리. (Đơn giản: Mỗi hàm chỉ làm 1 việc duy nhất.) |
| **의존성 배제 (Independence)** | 다른 모듈에 미치는 영향을 최소화. (Độc lập: Đổi chỗ này không làm sập chỗ khác.) |
| **중복성 최소화 (Minimizing Duplication)** | 코드의 중복을 최소화, 공통된 코드 사용. (DRY - Don't Repeat Yourself: Không copy-paste code.) |
| **추상화 (Abstraction)** | 상위 수준에선 간략하게, 상세 내용은 하위에서 구현. (Trừu tượng hóa: Cái chung ở trên, cái chi tiết ở dưới.) |

- **Vietnamese Explanation:** Clean Code là "đạo đức" của lập trình viên. Đừng viết Alien Code (code không ai hiểu nổi trừ người viết ban đầu). 
- 💡 **Mẹo ghi nhớ (Mnemonics):** 5 nguyên tắc: Đọc - Đơn - Độc - Lặp - Trừu. (Đọc Đơn Độc Lặp Trừu (Đọc hiểu - Đơn giản - Độc lập - Không lặp - Trừu tượng)).

---

# Chapter 5. 인터페이스 구현 (Interface Implementation)

---

## 097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)

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

---

## 098 & 기타 협업 도구 (Build Tools & Collaboration Tools)

### 빌드 도구 (Build Tool)
- 소스 코드를 실행할 수 있는 제품으로 변환(빌드)하는 과정을 자동화. (Công cụ tự động biên dịch và gom file code lại thành file chạy `.exe`, `.apk`...).
- **Ant:** Cổ điển, dùng cho Java, của Apache.
- **Maven:** Nâng cấp của Ant, quản lý thư viện (Dependencies) tự động.
- **Gradle:** Hiện đại nhất, lai giữa Ant và Maven, dùng nhiều cho Android.

### 기타 협업 도구 (Groupware / Collaboration Tools)
- **프로젝트 및 일정 관리 (Quản lý dự án):** Jira (지라), Trello, Google Calendar.
- **메신저 (Giao tiếp):** Slack, Jandi.
- **디자인 (Thiết kế UI -> Code):** Zeplin, Sketch.
- **기타:** Evernote (Ghi chú), Swagger (Tài liệu API tự động), GitHub (Lưu source code).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Jira = Quản lý công việc (Ticket). Slack = Chat. Zeplin = Thiết kế. Swagger = Viết Document cho API. Gradle = Build Android.

---

---

## 104-1 ~ 108: 소프트웨어 매뉴얼 (Software Manuals)

### 설치 매뉴얼 (Installation Manual - Hướng dẫn cài đặt)
- **사용자 기준 (Góc nhìn người dùng):** Viết cho khách hàng, không phải cho Dev.
- **순서대로 (Theo trình tự):** Từ lúc bấm Next đến lúc Finish.
- **예외 상황 / 오류 메시지:** Phải có cách xử lý khi cài đặt bị lỗi.
- **Uninstall (Xóa cài đặt):** Bắt buộc phải hướng dẫn cách gỡ cài đặt sạch sẽ.
- **서문 (Lời nói đầu) bao gồm:** 
  - 문서 이력 (Lịch sử chỉnh sửa v1.0, v1.1).
  - 주석 (Chú ý/Tham khảo).
  - 설치 환경 체크 (Kiểm tra OS, tắt app khác trước khi cài).

### 사용자 매뉴얼 (User Manual - Hướng dẫn sử dụng)
- **컴포넌트 단위 (Theo từng Component):** Chia nhỏ theo từng tính năng (Ví dụ: Hướng dẫn riêng cho Word, Excel).
- **버전 관리 (Quản lý phiên bản):** App update tính năng thì Manual cũng phải update theo.
- **시각 자료 (Hình ảnh):** Bắt buộc phải có hình chụp màn hình UI để dễ hiểu.

---

---

## 113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)

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

---

## 120-1: 소프트웨어의 분류 (Software Classification)

- **상용 소프트웨어 (Commercial):** Bán lấy tiền (Product). VD: Windows, Office, Game.
- **서비스 제공 소프트웨어 (Service Provision / SI):** Làm theo đơn đặt hàng của 1 tổ chức (Dự án nội bộ). VD: Hệ thống ngân hàng.

---
