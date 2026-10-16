# 정렬 알고리즘과 시간 복잡도 (Thuật toán sắp xếp và độ phức tạp)

## 학습 목표
- Nắm vững 3 ký pháp tiệm cận toán học: Big-$O$ (`최악 / Upper Bound`), Big-$\Omega$ (`최선 / Lower Bound`), và Big-$\Theta$ (`평균 / Tight Bound`), cùng chuỗi thứ bậc tăng trưởng thời gian từ $O(1)$ đến $O(n!)$.
- Phân biệt 4 kỹ thuật thiết kế giải thuật nền tảng: Chia để trị (`분할 정복`), Quy hoạch động (`동적 계획법`), Thuật toán tham lam (`탐욕법`), và Quay lui (`백트래킹`).
- Làm chủ bảng ma trận độ phức tạp thời gian (Tốt nhất, Trung bình, Xấu nhất) và tính ổn định (`안정 정렬 / Stable Sort` vs `불안정 정렬 / Unstable Sort`) của 8 thuật toán sắp xếp kinh điển: Bubble, Selection, Insertion, Shell, Quick, Heap, Merge, Radix.
- Hiểu rõ cơ chế phân rã pivot của Quick Sort, nguyên nhân thoái hóa xuống $O(n^2)$ khi mảng đã sắp xếp sẵn, và các thuật toán luôn bảo đảm $O(n \log n)$ trong mọi trường hợp (Heap Sort, Merge Sort).
- Thực hiện chuẩn xác bài toán trace mảng dữ liệu sau vòng lặp 1 (`1회전`) và vòng lặp 2 (`2회전`) của Bubble Sort, Selection Sort, Insertion Sort.

## 핵심 키워드
- 시간 복잡도 (Độ phức tạp thời gian / Time Complexity / Big-O, Big-$\Omega$, Big-$\Theta$)
- 알고리즘 설계 기법 (Chia để trị Divide & Conquer, Quy hoạch động DP, Tham lam Greedy, Quay lui Backtracking)
- 내부 정렬 vs 외부 정렬 (Internal Sort RAM vs External Sort Disk)
- 안정 정렬 vs 불안정 정렬 (Stable Sort vs Unstable Sort)
- 8대 정렬 알고리즘 (Bubble, Selection, Insertion, Shell, Quick, Heap, Merge, Radix)
- 퀵 정렬 (Quick Sort / 피벗 Pivot / 분할 정복 / 최악 $O(n^2)$ / 평균 $O(n \log n)$)
- 힙 정렬 & 병합 정렬 (Heap Sort & Merge Sort / mọi trường hợp $O(n \log n)$)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [04-do-thi-va-bieu-dien-do-thi.md](04-do-thi-va-bieu-dien-do-thi.md), chúng ta đã khảo sát các giải thuật duyệt đồ thị DFS và BFS.
- **Đang giải quyết gì (Current Problem):** Bài học này cung cấp khung lý thuyết toán học đo lường hiệu năng thuật toán, phân loại cơ chế sắp xếp mảng dữ liệu và nhận diện các thuật toán tối ưu cho từng tình huống thực tế.
- **Dùng đi đâu (Forward Handoff):** Sau khi dữ liệu đã được sắp xếp trật tự, bài học tiếp theo [06-thuat-toan-tim-kiem-va-bang-bam.md](06-thuat-toan-tim-kiem-va-bang-bam.md) sẽ chuyển sang các giải thuật tra cứu dữ liệu tốc độ cao: Tìm kiếm nhị phân và Cấu trúc Bảng băm.

## 읽는 방법
- Đọc TẦNG A để thuộc lòng bảng ma trận độ phức tạp 8 thuật toán sắp xếp, chuỗi tăng trưởng Big-O, và các bẫy đề thi trắc nghiệm kinh điển.
- Đọc TẦNG B để hiểu sâu 4 kỹ thuật thiết kế giải thuật, phân biệt Stable vs Unstable Sort và các bài tập trace mảng sau vòng 1.

---

## 정렬 알고리즘과 시간 복잡도

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Chuỗi thứ bậc tăng trưởng thời gian Big-O
$$\mathbf{O(1) \lt O(\log n) \lt O(n) \lt O(n \log n) \lt O(n^2) \lt O(2^n) \lt O(n!)}$$

- $O(1)$: Hằng số (Push/Pop Stack, truy cập mảng `A[i]`).
- $O(\log n)$: Logarit (Tìm kiếm nhị phân Binary Search).
- $O(n)$: Tuyến tính (Tìm kiếm tuần tự).
- $O(n \log n)$: Chuẩn mực tối ưu cho thuật toán sắp xếp so sánh (Merge, Heap, Quick trung bình).
- $O(n^2)$: Bậc hai (Vòng lặp lồng 2 lớp: Bubble, Selection, Insertion).
- $O(2^n), O(n!)$: Bùng nổ tổ hợp (Tháp Hà Nội, Người du lịch TSP).

#### 2. Bảng ma trận độ phức tạp 8 thuật toán sắp xếp chuẩn đề thi
| Thuật toán | Tên tiếng Hàn | Tốt nhất (최선) | Trung bình (평균) | Xấu nhất (최악) | Tính ổn định (Stability) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Selection Sort** | **선택 정렬** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | **Không ổn định (Unstable)** |
| **Bubble Sort** | **버블 정렬** | $O(n)$ (có cờ) | $O(n^2)$ | $O(n^2)$ | **Ổn định (Stable)** |
| **Insertion Sort** | **삽입 정렬** | $O(n)$ (đã xếp) | $O(n^2)$ | $O(n^2)$ | **Ổn định (Stable)** |
| **Shell Sort** | **셸 정렬** | $O(n)$ | $O(n^{1.5})$ | $O(n^2)$ | **Không ổn định (Unstable)** |
| **Quick Sort** | **퀵 정렬** | $O(n \log n)$ | $\mathbf{O(n \log n)}$ | $\mathbf{O(n^2)}$ | **Không ổn định (Unstable)** |
| **Heap Sort** | **힙 정렬** | $\mathbf{O(n \log n)}$ | $\mathbf{O(n \log n)}$ | $\mathbf{O(n \log n)}$ | **Không ổn định (Unstable)** |
| **Merge Sort** | **병합 정렬** | $\mathbf{O(n \log n)}$ | $\mathbf{O(n \log n)}$ | $\mathbf{O(n \log n)}$ | **Ổn định (Stable)** |
| **Radix Sort** | **기수 정렬** | $O(dn)$ | $O(dn)$ | $O(dn)$ | **Ổn định (Stable)** |

#### 3. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Điểm yếu của Quick Sort:**
  - Tốc độ trung bình nhanh nhất: $O(n \log n)$.
  - Nhưng khi mảng **đã được sắp xếp sẵn từ trước** hoặc chọn phải Pivot là phần tử nhỏ nhất/lớn nhất $\rightarrow$ Quick Sort thoái hóa thành **$O(n^2)$**.
- **Bẫy 2: Thuật toán luôn bảo đảm $O(n \log n)$ trong mọi trường hợp:**
  - Chỉ có hai thuật toán: **힙 정렬 (Heap Sort)** và **병합 정렬 (Merge Sort)**.
- **Bẫy 3: Phân biệt Stable vs Unstable Sort:**
  - **안정 정렬 (Stable Sort):** Giữ nguyên thứ tự tương đối ban đầu của các phần tử có cùng giá trị $\rightarrow$ **Bubble, Insertion, Merge, Radix** (Mẹo nhớ: *B-I-M-R*).
  - **불안정 정렬 (Unstable Sort):** Có thể làm xáo trộn thứ tự tương đối $\rightarrow$ **Selection, Quick, Heap, Shell** (Mẹo nhớ: *S-Q-H-S*).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bốn kỹ thuật thiết kế giải thuật nền tảng
- **분할 정복 (Divide and Conquer — Chia để trị):** Chia bài toán lớn thành các bài toán con độc lập cùng dạng, giải quyết đệ quy từng bài toán con rồi gộp kết quả lại (Quick Sort, Merge Sort, Binary Search).
- **동적 계획법 (Dynamic Programming — Quy hoạch động):** Áp dụng cho các bài toán có tính chất gối nhau; lưu kết quả bài toán con vào bảng ghi nhớ (**메모이제이션 — Memoization**) để tái sử dụng mà không phải tính lại (Dãy Fibonacci, Floyd-Warshall, Knapsack 0/1).
- **탐욕법 (Greedy Algorithm — Thuật toán tham lam):** Luôn chọn phương án tối ưu cục bộ tốt nhất trước mắt với hy vọng dẫn đến lời giải tối ưu toàn cục (Cây khung Kruskal, Prim, Tìm đường Dijkstra).
- **백트래킹 (Backtracking — Quay lui):** Thử từng phương án theo chiều sâu (DFS), nếu gặp ngõ cụt thì quay lui lại bước trước (Bài toán 8 quân hậu N-Queens, Mê cung).

#### 2. Cơ chế trace mảng sau vòng 1 (1회전 Trace)
Cho mảng ban đầu: `[8, 5, 2, 6, 3]`
- **Bubble Sort (버블 정렬):** So sánh từng cặp liền kề từ trái sang phải, đổi chỗ nếu đứng trước lớn hơn đứng sau. Phần tử lớn nhất sẽ "nổi bọt" về cuối mảng:
  - $(8, 5) \rightarrow [5, 8, 2, 6, 3] \rightarrow (8, 2) \rightarrow [5, 2, 8, 6, 3] \rightarrow (8, 6) \rightarrow [5, 2, 6, 8, 3] \rightarrow (8, 3) \rightarrow [5, 2, 6, 3, 8]$
  - Kết quả sau 1회전: **`[5, 2, 6, 3, 8]`** (Số 8 cố định ở vị trí cuối).
- **Selection Sort (선택 정렬):** Tìm phần tử nhỏ nhất trong toàn bộ mảng và đổi chỗ về vị trí đầu tiên:
  - Phần tử nhỏ nhất là `2` $\rightarrow$ Đổi chỗ `8` và `2`.
  - Kết quả sau 1회전: **`[2, 5, 8, 6, 3]`** (Số 2 cố định ở vị trí đầu).
- **Insertion Sort (삽입 정렬):** Lấy phần tử thứ hai chèn vào vị trí thích hợp trong dãy con đã sắp xếp phía trước:
  - Dãy con đã sắp xếp ban đầu là `[8]`, lấy phần tử thứ hai `5` chèn vào trước `8`.
  - Kết quả sau 1회전: **`[5, 8, 2, 6, 3]`**.

---

### 복습 체크리스트
- [ ] Thuộc lòng chuỗi tăng trưởng thời gian: $O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(2^n) < O(n!)$.
- [ ] Phân biệt 4 kỹ thuật thiết kế giải thuật: Chia để trị, Quy hoạch động, Tham lam, Quay lui.
- [ ] Nhớ thời gian xấu nhất của Quick Sort là $O(n^2)$ khi mảng đã sắp xếp sẵn.
- [ ] Kể tên 2 thuật toán luôn bảo đảm $O(n \log n)$ trong mọi trường hợp: Heap Sort và Merge Sort.
- [ ] Phân biệt các thuật toán Stable (Bubble, Insertion, Merge, Radix) và Unstable (Selection, Quick, Heap, Shell).
- [ ] Trace chuẩn xác kết quả sau vòng 1 của Bubble Sort, Selection Sort và Insertion Sort.
