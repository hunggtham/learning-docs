# 알고리즘 시간 복잡도와 정렬 기술 (Độ phức tạp thuật toán và kỹ thuật sắp xếp)

## 학습 목표
- Nắm vững 3 ký pháp tiệm cận toán học: Big-O (`최악 / Worst-case`), Big-$\Omega$ (`최선 / Best-case`), Big-$\Theta$ (`평균 / Average-case`) và thuộc lòng chuỗi thứ bậc tăng trưởng thời gian: $O(1) \lt O(\log n) \lt O(n) \lt O(n \log n) \lt O(n^2) \lt O(2^n) \lt O(n!)$.
- Phân biệt 4 kỹ thuật thiết kế giải thuật: Chia để trị (`분할 정복`), Quy hoạch động (`동적 계획법`), Thuật toán tham lam (`탐욕법`), và Quay lui (`백트래킹`).
- Phân biệt sắp xếp nội bộ (`내부 정렬`) vs sắp xếp ngoài (`외부 정렬`), và phân loại triệt để thuật toán ổn định (`안정 정렬`) vs không ổn định (`불안정 정렬`).
- Phân tích chi tiết cơ chế hoạt động, độ phức tạp và vết lặp vòng 1 (`1회전`) của 8 thuật toán kinh điển: Insertion, Selection, Bubble, Shell, Quick, Merge, Heap, Radix Sort.
- Nắm vững các bẫy đề thi: nguyên nhân thoái hóa xuống $O(n^2)$ của Quick Sort khi dữ liệu đã sắp xếp sẵn; hai thuật toán luôn bảo đảm $O(n \log n)$ trong mọi trường hợp (Merge Sort và Heap Sort).

## 핵심 키워드
- 시간 복잡도 (Độ phức tạp thời gian / Time Complexity / Big-O 표기법)
- 알고리즘 설계 (Kỹ thuật thiết kế: 분할 정복, 동적 계획법, 탐욕법, 백트래킹)
- 내부 정렬 vs 외부 정렬 (Internal Sort vs External Sort)
- 안정 정렬 vs 불안정 정렬 (Stable Sort vs Unstable Sort)
- O(n²) 정렬 (삽입 정렬 Insertion, 선택 정렬 Selection, 버블 정렬 Bubble)
- O(n log n) 정렬 (퀵 정렬 Quick, 합병 정렬 Merge, 힙 정렬 Heap)
- 기수 정렬 (Radix Sort / 큐 Bucket 활용 / 비비교 정렬)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở các bài học trước ([01](01-cau-truc-du-lieu-tuyen-tinh.md), [02](02-ky-phap-bieu-thuc-va-stack.md), [03](03-cay-va-duyet-cay-nhi-phan.md), [04](04-do-thi-va-bieu-dien-do-thi.md)), chúng ta đã làm chủ các cấu trúc dữ liệu nền tảng từ tuyến tính đến phi tuyến trong bộ nhớ.
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết bài toán cốt lõi nhất về hiệu năng: đo lường thời gian thực thi bằng ký pháp tiệm cận Big-O và tối ưu hóa việc sắp xếp dữ liệu có thứ tự thông qua 8 thuật toán kinh điển.
- **Dùng đi đâu (Forward Handoff):** Khi mảng dữ liệu đã được sắp xếp trật tự, ta có thể áp dụng thuật toán tìm kiếm nhị phân với thời gian kỷ lục $O(\log n)$, bàn giao trực tiếp sang [06-thuat-toan-tim-kiem-va-bang-bam.md](06-thuat-toan-tim-kiem-va-bang-bam.md).

## 읽는 방법
- Đọc TẦNG A để thuộc lòng bảng ma trận so sánh 8 thuật toán (thời gian, không gian, tính ổn định) và các bẫy trace vòng 1 (Selection chốt min ở đầu, Bubble chốt max ở cuối).
- Đọc TẦNG B để hiểu sâu bản chất toán học của phân vùng Pivot trong Quick Sort, cơ chế Heapify trong Heap Sort và quy tắc nạp Bucket của Radix Sort.

---

## 알고리즘 시간 복잡도와 정렬 기술

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Chuỗi thứ bậc tăng trưởng thời gian Big-O
$$O(1) \lt O(\log n) \lt O(n) \lt O(n \log n) \lt O(n^2) \lt O(n^3) \lt O(2^n) \lt O(n!)$$
- $O(1)$: Thao tác tức thì (Push/Pop Stack, truy cập mảng bằng index).
- $O(\log n)$: Tìm kiếm nhị phân (Binary Search).
- $O(n)$: Tìm kiếm tuần tự, duyệt 1 vòng lặp qua mảng.
- $O(n \log n)$: Chuẩn mực tối ưu sắp xếp so sánh (Merge, Heap, Quick trung bình).
- $O(n^2)$: Vòng lặp lồng 2 lớp (Bubble, Selection, Insertion).
- $O(2^n), O(n!)$: Bùng nổ tổ hợp (Tháp Hà Nội, TSP vét cạn).

#### 2. Bảng ma trận so sánh toàn diện 8 thuật toán sắp xếp
| Thuật toán sắp xếp | Tên tiếng Hàn | Tốt nhất (Best) | Trung bình (Avg) | Xấu nhất (Worst) | Không gian phụ | Tính ổn định |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **선택 정렬 (Selection)** | Sắp xếp chọn | $O(n^2)$ | $O(n^2)$ | $\mathbf{O(n^2)}$ | $O(1)$ | **Không ổn định (Unstable)** |
| **버블 정렬 (Bubble)** | Sắp xếp nổi bọt | $O(n)$ *(dùng cờ)* | $O(n^2)$ | $\mathbf{O(n^2)}$ | $O(1)$ | **Ổn định (Stable)** |
| **삽입 정렬 (Insertion)** | Sắp xếp chèn | $\mathbf{O(n)}$ *(xếp sẵn)* | $O(n^2)$ | $\mathbf{O(n^2)}$ | $O(1)$ | **Ổn định (Stable)** |
| **셸 정렬 (Shell)** | Sắp xếp Shell | $O(n)$ | $O(n^{1.25})$ | $\mathbf{O(n^2)}$ | $O(1)$ | **Không ổn định (Unstable)** |
| **퀵 정렬 (Quick)** | Sắp xếp nhanh | $O(n \log n)$ | $\mathbf{O(n \log n)}$ | $\mathbf{O(n^2)}$ *(thoái hóa)* | $O(\log n)$ | **Không ổn định (Unstable)** |
| **합병 정렬 (Merge)** | Sắp xếp trộn | $\mathbf{O(n \log n)}$ | $\mathbf{O(n \log n)}$ | $\mathbf{O(n \log n)}$ | $\mathbf{O(n)}$ *(mảng phụ)* | **Ổn định (Stable)** |
| **힙 정렬 (Heap)** | Sắp xếp vun đống | $\mathbf{O(n \log n)}$ | $\mathbf{O(n \log n)}$ | $\mathbf{O(n \log n)}$ | $\mathbf{O(1)}$ *(in-place)* | **Không ổn định (Unstable)** |
| **기수 정렬 (Radix)** | Sắp xếp cơ số | $O(d \cdot n)$ | $O(d \cdot n)$ | $\mathbf{O(d \cdot n)}$ | $O(n + k)$ | **Ổn định (Stable)** |

#### 3. Phân biệt tính ổn định (정렬의 안정성)
- **Thuật toán ổn định (Stable Sort):** Giữ nguyên trật tự tương đối ban đầu của các phần tử có giá trị khóa bằng nhau: **삽입 (Insertion), 버블 (Bubble), 합병 (Merge), 기수 (Radix)**.
- **Thuật toán không ổn định (Unstable Sort):** Có thể làm thay đổi trật tự ban đầu của các khóa bằng nhau: **선택 (Selection), 퀵 (Quick), 힙 (Heap), 셸 (Shell)**.

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Hiện tượng thoái hóa của Quick Sort:**
  - Khi mảng đầu vào **đã được sắp xếp sẵn (tăng dần hoặc giảm dần)**, nếu chọn Pivot ở đầu hoặc cuối mảng thì Quick Sort bị thoái hóa xuống **$O(n^2)$**.
- **Bẫy 2: So sánh Merge Sort vs Heap Sort:**
  - Cả hai đều luôn đạt $O(n \log n)$ trong mọi trường hợp.
  - Merge Sort tốn thêm mảng phụ $O(n)$ và là Stable Sort.
  - Heap Sort sắp xếp tại chỗ $O(1)$ (In-place) và là Unstable Sort.
- **Bẫy 3: Trace vòng 1 (1회전):**
  - **Selection Sort:** Tìm phần tử nhỏ nhất chốt cứng ở **ĐẦU mảng**.
  - **Bubble Sort:** So sánh cặp liền kề, đẩy phần tử lớn nhất chốt cứng ở **CUỐI mảng**.
  - **Insertion Sort:** Bốc phần tử thứ 2 chèn vào vị trí thích hợp của dãy con đứng trước nó.
- **Bẫy 4: Insertion Sort xếp sẵn:** Khi dữ liệu đã gần như có thứ tự tăng dần sẵn, Insertion Sort chạy cực nhanh với thời gian $O(n)$.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bốn kỹ thuật thiết kế giải thuật nền tảng
- **분할 정복 (Divide and Conquer):** Chia nhỏ bài toán thành các bài toán con độc lập cùng cấu trúc, giải đệ quy rồi hợp nhất kết quả (Merge Sort, Quick Sort, Binary Search).
- **동적 계획법 (Dynamic Programming):** Áp dụng cho bài toán có các bài toán con gối nhau (`Overlapping Subproblems`); lưu kết quả vào bảng nhớ (`Memoization`) để không phải tính lại (Dãy Fibonacci, Knapsack 0/1, Floyd-Warshall).
- **탐욕법 (Greedy Algorithm):** Luôn chọn phương án tối ưu cục bộ trước mắt tại mỗi bước để hướng đến lời giải toàn cục (Kruskal, Prim, Dijkstra).
- **백트래킹 (Backtracking):** Tìm kiếm theo chiều sâu (DFS), khi chạm nhánh cụt vi phạm ràng buộc thì quay lui lại bước trước (Bài toán 8 quân hậu N-Queens, Mê cung).

#### 2. Cơ chế sắp xếp vun đống (Heap Sort)
- Dựa trên cấu trúc Cây nhị phân hoàn chỉnh (Complete Binary Tree).
- Tạo **최대 힙 (Max-Heap)**: Nút cha luôn lớn hơn hoặc bằng các nút con, nút gốc Root chứa giá trị lớn nhất toàn cây.
- Lần lượt hoán đổi nút Root với phần tử cuối cùng của mảng, giảm kích thước heap đi 1 và gọi hàm `Heapify` để tái cân bằng cây trong thời gian $O(\log n)$.

#### 3. Cơ chế sắp xếp cơ số (Radix Sort)
- Không sử dụng phép so sánh khóa trực tiếp.
- Sử dụng 10 thùng Hàng đợi (`큐 / Bucket`) tương ứng với các chữ số từ `0` đến `9`.
- Quét các số theo từng hàng chữ số từ hàng đơn vị (LSD - Least Significant Digit) đến hàng chục, hàng trăm; phân phối vào các Bucket rồi nối lại theo trật tự FIFO.

---

### 복습 체크리스트
- [ ] Thuộc lòng chuỗi thứ bậc Big-O: $O(1) \lt O(\log n) \lt O(n) \lt O(n \log n) \lt O(n^2) \lt O(2^n) \lt O(n!)$.
- [ ] Phân biệt 4 kỹ thuật thiết kế: Chia để trị, Quy hoạch động, Tham lam, Quay lui.
- [ ] Phân biệt đặc điểm trace sau vòng 1: Selection chốt min ở đầu, Bubble chốt max ở cuối.
- [ ] Nhớ Insertion Sort đạt $O(n)$ khi mảng ban đầu gần như đã xếp sẵn.
- [ ] Giải thích nguyên nhân Quick Sort bị thoái hóa xuống $O(n^2)$ khi dữ liệu đã có thứ tự sẵn.
- [ ] Nhớ Merge Sort và Heap Sort luôn bảo đảm $O(n \log n)$ trong mọi trường hợp.
- [ ] Phân biệt: Merge Sort tốn bộ nhớ phụ $O(n)$ và là Stable; Heap Sort in-place $O(1)$ và là Unstable.
- [ ] Nhớ Radix Sort dùng hàng đợi Queue để sắp xếp theo chữ số không cần so sánh khóa.
- [ ] Phân loại chính xác các thuật toán Stable (Insertion, Bubble, Merge, Radix) và Unstable (Selection, Quick, Heap, Shell).
