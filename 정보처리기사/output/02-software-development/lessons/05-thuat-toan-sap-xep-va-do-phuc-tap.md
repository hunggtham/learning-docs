# Môn 2 · Bài 05 — Độ phức tạp thuật toán và kỹ thuật sắp xếp

> **Mạch đọc:** [README](../README.md) là bản đồ chủ đề của **Môn 2 — 소프트웨어 개발 (Software Development)**. Sau khi đã làm chủ các cấu trúc dữ liệu từ tuyến tính ([Bài 01](01-cau-truc-du-lieu-tuyen-tinh.md), [Bài 02](02-ky-phap-bieu-thuc-va-stack.md)) đến phi tuyến ([Bài 03](03-cay-va-duyet-cay-nhi-phan.md), [Bài 04](04-do-thi-va-bieu-dien-do-thi.md)), bài học này bước sang trọng tâm tính toán lớn nhất của Chương 1: **Thời gian thực thi và Thuật toán sắp xếp dữ liệu (정렬 알고리즘 — Sorting Algorithms)**. Bài học trang bị toàn diện lý thuyết độ phức tạp Big-O, 4 kỹ thuật thiết kế giải thuật và phân tích chi tiết 8 thuật toán sắp xếp kinh điển luôn xuất hiện trong các bài toán truy vết (Trace) của đề thi trắc nghiệm.

> **Phạm vi nguồn:** Hợp nhất và chuẩn hóa nội dung từ 13 bài học cũ: `14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 73, 91-bai-hoc.md` (tương ứng với các mục 6, 18, 31, 027, 028, 081 ~ 086-1 trong tài liệu chuẩn gốc). Toàn bộ bảng ma trận độ phức tạp và các bài toán trace vòng lặp (1회전, 2회전) được chuẩn hóa theo chuẩn khảo thí HRDK.

> **Mạch kiến thức:** Bài học giải quyết ba bài toán cốt lõi trong tối ưu hóa hiệu năng phần mềm: (1) Ký pháp tiệm cận Big-O, $\Omega$, $\Theta$ đánh giá thời gian chạy của chương trình như thế nào và chuỗi tăng trưởng thời gian được sắp xếp ra sao? (2) Tám thuật toán sắp xếp (Bubble, Selection, Insertion, Shell, Quick, Heap, Merge, Radix) vận hành theo cơ chế nào và kết quả mảng sau vòng 1 (1회전) được xác định ra sao? (3) Tại sao Quick Sort có tốc độ trung bình nhanh nhất nhưng lại thoái hóa xuống $O(n^2)$ khi mảng đã sắp xếp sẵn, và những thuật toán nào luôn bảo đảm $O(n \log n)$ trong mọi trường hợp?

---

## 1. 알고리즘 시간 복잡도와 설계 기법 — Độ phức tạp và Kỹ thuật thiết kế thuật toán

**알고리즘의 효율성은 시간 복잡도(Time Complexity)와 공간 복잡도(Space Complexity)로 측정되며, 주로 입력 크기 $n$에 대한 실행 시간의 증가율을 나타내는 빅오(Big-O) 표기법을 사용한다.**

### 1.1. Ba ký pháp tiệm cận toán học
1. **빅오 표기법 (Big-O Notation — $O$):** Biểu diễn **cận trên (Upper Bound)** của thời gian chạy, tức là thời gian thực thi trong **trường hợp xấu nhất (최악 — Worst Case)**. Đây là thước đo tiêu chuẩn được sử dụng rộng rãi nhất trong kỹ nghệ phần mềm để đảm bảo hệ thống không bị vượt quá giới hạn thời gian cho phép.
2. **빅오메가 표기법 (Big-$\Omega$ Notation — $\Omega$):** Biểu diễn **cận dưới (Lower Bound)**, tức là thời gian trong **trường hợp tốt nhất (최선 — Best Case)**.
3. **빅세타 표기법 (Big-$\Theta$ Notation — $\Theta$):** Biểu diễn **cận chặt (Tight Bound)**, tức là thuật toán có cận trên và cận dưới tiệm cận cùng một bậc hàm số (trường hợp trung bình).

### 1.2. Chuỗi thứ bậc tăng trưởng thời gian Big-O
Khi kích thước dữ liệu đầu vào $n$ tăng dần đến vô cùng, tốc độ tiêu tốn thời gian của các thuật toán bùng nổ theo thứ tự tăng dần sau:

$$O(1) \lt O(\log n) \lt O(n) \lt O(n \log n) \lt O(n^2) \lt O(n^3) \lt O(2^n) \lt O(n!)$$

- **$O(1)$ (상수형 — Hằng số):** Thao tác tức thì không phụ thuộc vào $n$ (Push/Pop Stack, truy cập mảng bằng chỉ số `A[i]`).
- **$O(\log n)$ (로그형 — Logarit):** Tìm kiếm nhị phân (Binary Search). Cứ mỗi bước thì không gian tìm kiếm giảm đi một nửa.
- **$O(n)$ (선형 — Tuyến tính):** Tìm kiếm tuần tự, duyệt một vòng lặp qua mảng.
- **$O(n \log n)$ (선형로그형):** Chuẩn mực tối ưu cho các thuật toán sắp xếp so sánh (Merge Sort, Heap Sort, Quick Sort trung bình).
- **$O(n^2)$ (2차형 — Bậc hai):** Vòng lặp lồng 2 lớp (Bubble, Selection, Insertion Sort).
- **$O(2^n)$ & $O(n!)$ (지수 및 팩토리얼 — Hàm mũ và Giai thừa):** Bùng nổ tổ hợp khủng khiếp, không khả thi trong thực tế khi $n$ lớn (Bài toán Tháp Hà Nội, Người du lịch TSP vét cạn).

### 1.3. Bốn kỹ thuật thiết kế giải thuật nền tảng
- **분할 정복 (Divide and Conquer — Chia để trị):** Chia bài toán lớn thành các bài toán con độc lập cùng dạng, giải quyết đệ quy từng bài toán con rồi gộp kết quả lại (Quick Sort, Merge Sort, Binary Search).
- **동적 계획법 (Dynamic Programming — Quy hoạch động):** Áp dụng cho các bài toán có tính chất gối nhau (Overlapping Subproblems); lưu trữ kết quả của các bài toán con vào bảng ghi nhớ (**메모이제이션 — Memoization**) để tái sử dụng mà không phải tính lại (Dãy Fibonacci, Floyd-Warshall, Knapsack 0/1).
- **탐욕법 (Greedy Algorithm — Thuật toán tham lam):** Tại mỗi bước quyết định, luôn chọn phương án tối ưu cục bộ tốt nhất trước mắt với hy vọng dẫn đến lời giải tối ưu toàn cục (Thuật toán tìm cây khung Kruskal, Prim, Tìm đường đi ngắn nhất Dijkstra).
- **백트래킹 (Backtracking — Quay lui):** Thử từng phương án theo chiều sâu (DFS), nếu gặp ngõ cụt vi phạm điều kiện ràng buộc thì quay lui lại bước trước để thử nhánh khác (Bài toán 8 quân hậu N-Queens, Giải mê cung).

---

## 2. 정렬 알고리즘의 분류 — Phân loại thuật toán sắp xếp

Thuật toán sắp xếp (Sorting Algorithms) đưa một tập hợp các phần tử về một trật tự xác định (tăng dần hoặc giảm dần).

### Phân loại theo không gian lưu trữ:
- **내부 정렬 (Internal Sort — Sắp xếp nội bộ):** Toàn bộ dữ liệu được nạp vào bộ nhớ chính (RAM) để sắp xếp. Tốc độ rất nhanh nhưng bị giới hạn bởi dung lượng RAM (gồm cả 8 thuật toán dưới đây).
- **외부 정렬 (External Sort — Sắp xếp ngoài):** Dữ liệu quá khổng lồ không thể nạp hết vào RAM, phải lưu trữ trên đĩa cứng/băng từ và nạp từng phần vào RAM để hòa trộn (ví dụ: 2-Way Merge Sort, K-Way Merge Sort).

### Phân loại theo tính ổn định (정렬의 안정성 — Stability):
- **안정 정렬 (Stable Sort — Sắp xếp ổn định):** Bảo tồn nguyên vẹn thứ tự tương đối ban đầu của các phần tử có giá trị khóa bằng nhau (Gồm: **삽입 정렬, 버블 정렬, 합병 정렬, 기수 정렬**).
- **불안정 정렬 (Unstable Sort — Sắp xếp không ổn định):** Có thể làm xáo trộn thứ tự tương đối của các phần tử có cùng giá trị khóa (Gồm: **선택 정렬, 퀵 정렬, 힙 정렬, 셸 정렬**).

---

## 3. Nhóm thuật toán sắp xếp cơ bản $O(n^2)$

Nhóm này sử dụng hai vòng lặp lồng nhau, thao tác đơn giản nhưng hiệu năng kém khi số lượng phần tử $n$ lớn.

### 3.1. 삽입 정렬 (Insertion Sort — Sắp xếp chèn)
- **Cơ chế:** Bắt đầu từ phần tử thứ 2 ($i = 1$), so sánh ngược về phía trước để tìm vị trí thích hợp và **chèn phần tử đó vào dãy con đã có thứ tự**.
- **Đặc điểm đề thi:**
  - Nếu mảng ban đầu **gần như đã được sắp xếp tăng dần sẵn**, Insertion Sort đạt tốc độ kỷ lục là **$O(n)$** (chỉ tốn 1 lần so sánh cho mỗi phần tử).
  - Là thuật toán **ổn định (Stable)**.
- **Trace vòng 1 (1회전):** Cho dãy `[8, 5, 6, 2, 4]`.
  - Bốc số thứ hai là `5`, so với `8` $\rightarrow$ chèn `5` lên trước `8`.
  - Kết thúc 1 vòng: `[5, 8, 6, 2, 4]`.

### 3.2. 선택 정렬 (Selection Sort — Sắp xếp chọn)
- **Cơ chế:** Quét toàn bộ các phần tử chưa chốt, **tìm ra phần tử có giá trị nhỏ nhất (Min)** rồi hoán đổi vị trí của nó với phần tử đầu tiên của dãy chưa chốt.
- **Đặc điểm đề thi:**
  - **Chốt cố định phần tử nhỏ nhất ở ĐẦU mảng sau mỗi vòng.**
  - Thời gian thực thi luôn là **$O(n^2)$ trong mọi trường hợp** (bất kể mảng ban đầu thế nào vẫn phải quét hết để tìm min).
  - Là thuật toán **không ổn định (Unstable)**.
- **Trace vòng 1 (1회전):** Cho dãy `[8, 5, 6, 2, 4]`.
  - Quét toàn mảng, tìm thấy số nhỏ nhất là `2` (tại index 3).
  - Hoán đổi số `2` với số `8` ở vị trí đầu tiên.
  - Kết thúc 1 vòng: `[2, 5, 6, 8, 4]` (Số 2 chốt cứng ở đầu).

### 3.3. 버블 정렬 (Bubble Sort — Sắp xếp nổi bọt)
- **Cơ chế:** Duyệt từ đầu đến cuối mảng, **so sánh từng cặp phần tử liền kề nhau** (`A[j]` và `A[j+1]`). Nếu phần tử đứng trước lớn hơn phần tử đứng sau thì hoán đổi chỗ, làm cho phần tử lớn nhất dần dần "nổi bọt" trôi về tận cùng đáy mảng.
- **Đặc điểm đề thi:**
  - **Chốt cố định phần tử lớn nhất ở CUỐI mảng sau mỗi vòng.**
  - Là thuật toán **ổn định (Stable)**.
  - Có thể cải tiến bằng cờ hiệu `flag`: nếu qua 1 vòng mà không có phép hoán đổi nào xảy ra thì dừng sớm, đạt $O(n)$.
- **Trace vòng 1 (1회전):** Cho dãy `[8, 5, 6, 2, 4]`.
  - So (8, 5) $\rightarrow$ đổi: `[5, 8, 6, 2, 4]`
  - So (8, 6) $\rightarrow$ đổi: `[5, 6, 8, 2, 4]`
  - So (8, 2) $\rightarrow$ đổi: `[5, 6, 2, 8, 4]`
  - So (8, 4) $\rightarrow$ đổi: `[5, 6, 2, 4, 8]`
  - Kết thúc 1 vòng: `[5, 6, 2, 4, 8]` (Số 8 to nhất chốt cứng ở cuối).

---

## 4. Nhóm thuật toán sắp xếp nâng cao $O(n \log n)$

### 4.1. 셸 정렬 (Shell Sort — Sắp xếp Shell)
- **Cơ chế:** Do Donald Shell đề xuất nhằm khắc phục nhược điểm dịch chuyển từng bước 1 của Insertion Sort. Thuật toán chia danh sách thành các nhóm con gồm các phần tử cách nhau một khoảng bước nhảy (**간격 — Gap**), áp dụng Insertion Sort cho từng nhóm, sau đó giảm dần khoảng cách Gap (thường chia đôi: $h = \lfloor h/2 \rfloor$) cho đến khi $\text{Gap} = 1$.
- **Độ phức tạp:** Trung bình đạt $O(n^{1.25}) \sim O(n^{1.5})$; trường hợp xấu nhất là $O(n^2)$. Là thuật toán **không ổn định (Unstable)**.

### 4.2. 퀵 정렬 (Quick Sort — Sắp xếp nhanh)
- **Cơ chế:** Áp dụng chiến lược Chia để trị (Divide and Conquer). Chọn một phần tử làm chốt (**피벗 — Pivot**). Phân vùng mảng sao cho tất cả các phần tử nhỏ hơn Pivot nằm về bên trái, tất cả các phần tử lớn hơn Pivot nằm về bên phải. Sau đó gọi đệ quy sắp xếp hai mảng con độc lập.
- **Ưu điểm lớn nhất:** Có tốc độ thực thi trong trường hợp trung bình **nhanh nhất** trong các thuật toán so sánh: $\mathbf{O(n \log n)}$.
- **⚠️ Bẫy đề thi kinh điển (Hiện tượng thoái hóa):**
  - Khi mảng đầu vào **đã được sắp xếp tăng dần hoặc giảm dần sẵn**, nếu chọn Pivot là phần tử đầu mảng hoặc cuối mảng, mảng sẽ bị phân vùng lệch tuyệt đối ($0$ phần tử và $n-1$ phần tử). Lúc này cây đệ quy bị suy biến thành danh sách liên kết và thời gian chạy **tụt dốc thảm hại xuống mức tồi tệ nhất là $\mathbf{O(n^2)}$**!
  - Khắc phục: Chọn Pivot ngẫu nhiên hoặc chọn trung vị của 3 phần tử (Median-of-three).
- **Tính chất:** Không ổn định (Unstable), không gian ngăn xếp đệ quy $O(\log n)$.

### 4.3. 2-Way 합병 정렬 (Merge Sort — Sắp xếp hòa trộn)
- **Cơ chế:** Áp dụng triết lý Chia để trị: Liên tục chia đôi mảng ra làm 2 nửa cho đến khi thu được các mảng con chỉ chứa 1 phần tử. Sau đó, **hòa trộn (Merge) từng cặp 2 mảng con đã có thứ tự lại với nhau thành 1 mảng lớn hơn** có thứ tự.
- **Ưu điểm lớn nhất chuẩn đề thi:**
  - **Luôn luôn bảo đảm thời gian $\mathbf{O(n \log n)}$ trong mọi trường hợp** (kể cả tốt nhất, trung bình lẫn xấu nhất).
  - Là thuật toán **ổn định (Stable)**.
- **Nhược điểm:** Đòi hỏi phải cấp phát thêm một mảng bộ nhớ phụ có kích thước đúng bằng mảng ban đầu $\mathbf{O(n)}$ để phục vụ việc hòa trộn dữ liệu.

### 4.4. 힙 정렬 (Heap Sort — Sắp xếp vun đống)
- **Cơ chế:** Dựa trên cấu trúc dữ liệu **Cây nhị phân hoàn chỉnh (Complete Binary Tree)**. Xây dựng cây thành **최대 힙 (Max-Heap)** — nơi giá trị nút cha luôn lớn hơn hoặc bằng các nút con (nút Root chứa giá trị lớn nhất). Lần lượt hoán đổi nút Root với nút cuối mảng, thu hẹp kích thước Heap và vun đống lại (**Heapify**).
- **Đặc điểm đề thi:**
  - **Luôn luôn bảo đảm thời gian $\mathbf{O(n \log n)}$ trong mọi trường hợp** giống như Merge Sort.
  - Khắc phục được nhược điểm của Merge Sort: **Không tốn thêm mảng phụ**, sắp xếp trực tiếp trên mảng gốc (**In-place Sort** với không gian phụ $O(1)$).
  - Là thuật toán **không ổn định (Unstable)**.

### 4.5. 기수 정렬 (Radix Sort / Bucket Sort — Sắp xếp theo cơ số)
- **Cơ chế:** Là thuật toán sắp xếp phân phối **hoàn toàn không dùng phép so sánh khóa**. Thuật toán sử dụng 10 thùng Hàng đợi (**큐 — Queue / Bucket**) tương ứng với các chữ số từ `0` đến `9`. Lần lượt phân loại các số vào các thùng theo từng hàng chữ số: bắt đầu từ hàng đơn vị (LSD — Least Significant Digit), rồi hàng chục, hàng trăm...
- **Độ phức tạp:** Thời gian chạy là **$O(d \cdot n)$** (với $d$ là số chữ số lớn nhất). Rất nhanh khi số chữ số $d$ nhỏ, là thuật toán **ổn định (Stable)**.

---

## 5. Bảng ma trận so sánh tổng hợp toàn diện các thuật toán sắp xếp

Đây là bảng kiến thức quyết định để trả lời chính xác mọi câu hỏi trắc nghiệm về độ phức tạp và tính ổn định:

| Thuật toán sắp xếp | Tên tiếng Hàn | Thời gian Tốt nhất (Best) | Thời gian Trung bình (Avg) | Thời gian Xấu nhất (Worst) | Không gian phụ | Tính ổn định (Stability) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **선택 정렬 (Selection)** | Sắp xếp chọn | $O(n^2)$ | $O(n^2)$ | $\mathbf{O(n^2)}$ | $O(1)$ | **Không ổn định (Unstable)** |
| **버블 정렬 (Bubble)** | Sắp xếp nổi bọt | $O(n)$ *(dùng cờ)* | $O(n^2)$ | $\mathbf{O(n^2)}$ | $O(1)$ | **Ổn định (Stable)** |
| **삽입 정렬 (Insertion)** | Sắp xếp chèn | $\mathbf{O(n)}$ *(xếp sẵn)* | $O(n^2)$ | $\mathbf{O(n^2)}$ | $O(1)$ | **Ổn định (Stable)** |
| **셸 정렬 (Shell)** | Sắp xếp Shell | $O(n)$ | $O(n^{1.25})$ | $\mathbf{O(n^2)}$ | $O(1)$ | **Không ổn định (Unstable)** |
| **퀵 정렬 (Quick)** | Sắp xếp nhanh | $O(n \log n)$ | $\mathbf{O(n \log n)}$ | $\mathbf{O(n^2)}$ *(thoái hóa)* | $O(\log n)$ | **Không ổn định (Unstable)** |
| **합병 정렬 (Merge)** | Sắp xếp trộn | $\mathbf{O(n \log n)}$ | $\mathbf{O(n \log n)}$ | $\mathbf{O(n \log n)}$ | $\mathbf{O(n)}$ *(mảng phụ)* | **Ổn định (Stable)** |
| **힙 정렬 (Heap)** | Sắp xếp vun đống | $\mathbf{O(n \log n)}$ | $\mathbf{O(n \log n)}$ | $\mathbf{O(n \log n)}$ | $\mathbf{O(1)}$ *(in-place)* | **Không ổn định (Unstable)** |
| **기수 정렬 (Radix)** | Sắp xếp theo cơ số | $O(d \cdot n)$ | $O(d \cdot n)$ | $\mathbf{O(d \cdot n)}$ | $O(n + k)$ | **Ổn định (Stable)** |

---

## 6. Nối mạch kiến thức sang bài tiếp theo

Khi dữ liệu đã được sắp xếp trật tự bằng các thuật toán tối ưu $O(n \log n)$, một lợi ích kỹ thuật to lớn mở ra: thay vì phải tìm kiếm tuần tự chậm chạp tốn $O(n)$, chúng ta có thể áp dụng thuật toán tìm kiếm nhị phân với thời gian kỷ lục $O(\log n)$.

Chúng ta sẽ chuyển sang **[Bài 06: Thuật toán tìm kiếm và bảng băm](06-thuat-toan-tim-kiem-va-bang-bam.md)** để nghiên cứu thuật toán tìm kiếm nhị phân (Binary Search), cấu trúc lưu trữ bảng băm (Hashing) và các kỹ thuật giải quyết xung đột (Collision Resolution) để đạt tốc độ tra cứu $O(1)$.

---

## 7. 복습 체크리스트 (Checklist ôn tập)

- [ ] Thuộc lòng chuỗi thứ bậc Big-O: $O(1) \lt O(\log n) \lt O(n) \lt O(n \log n) \lt O(n^2) \lt O(2^n) \lt O(n!)$.
- [ ] Phân biệt được 4 kỹ thuật: Chia để trị (Quick/Merge), Quy hoạch động (Fibonacci/DP), Tham lam (Kruskal/Prim), Quay lui (N-Queens).
- [ ] Phân biệt được đặc điểm trace sau vòng 1: Selection chốt min ở đầu, Bubble chốt max ở cuối.
- [ ] Nhớ Insertion Sort đạt $O(n)$ khi mảng ban đầu gần như đã xếp sẵn.
- [ ] Giải thích nguyên nhân Quick Sort bị tụt xuống $O(n^2)$ khi dữ liệu đã có thứ tự sẵn.
- [ ] Nhớ Merge Sort và Heap Sort luôn đạt $O(n \log n)$ trong mọi trường hợp.
- [ ] Phân biệt: Merge Sort tốn bộ nhớ phụ $O(n)$ và là Stable; Heap Sort in-place $O(1)$ và là Unstable.
- [ ] Nhớ Radix Sort dùng hàng đợi Queue để sắp xếp theo chữ số không cần so sánh khóa.
- [ ] Phân loại chính xác danh sách các thuật toán Stable (Insertion, Bubble, Merge, Radix) và Unstable (Selection, Quick, Heap, Shell).
