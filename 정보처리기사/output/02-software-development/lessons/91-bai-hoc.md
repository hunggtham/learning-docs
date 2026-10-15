# 027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)

## 학습 목표 (Mục tiêu)
- Nắm vững 4 kỹ thuật thiết kế giải thuật kinh điển: Chia để trị (분할과 정복 - Divide & Conquer), Quy hoạch động (동적계획법 - Dynamic Programming), Thuật toán tham lam (탐욕법 - Greedy), và Quay lui (백트래킹 - Backtracking).
- Phân biệt rõ sự khác nhau giữa Chia để trị (bài toán con độc lập) và Quy hoạch động (bài toán con gối nhau, lưu trữ kết quả trung gian - Memoization).
- Hiểu ý nghĩa của độ phức tạp thời gian (시간 복잡도) và chuỗi thứ tự tăng trưởng tiệm cận: $O(1) \lt O(\log n) \lt O(n) \lt O(n \log n) \lt O(n^2) \lt O(2^n)$.

## 핵심 키워드 (Từ khóa)
- 알고리즘 설계 기법 (Algorithm Design Techniques)
- 분할 정복 (Divide & Conquer / 퀵 정렬, 병합 정렬)
- 동적계획법 (Dynamic Programming / 메모이제이션 Memoization)
- 탐욕법 (Greedy Algorithm / 크루스칼, 다익스트라)
- 백트래킹 (Backtracking / 상태 공간 트리, 유망성 가지치기 Pruning)
- 시간 복잡도 (Time Complexity / Big-O Notation)

## 선행·연결 개념 (Kiến thức liên kết)
- [90-bai-hoc.md](90-bai-hoc.md): Phân loại cấu trúc dữ liệu tuyến tính và phi tuyến tính.
- [92-bai-hoc.md](92-bai-hoc.md): Kỹ thuật tái sử dụng phần mềm (Software Reuse).
- [73-bai-hoc.md](73-bai-hoc.md): Độ phức tạp thời gian trong trường hợp xấu nhất.

## 읽는 방법 (Cách đọc)
- Phân biệt 4 triết lý thiết kế giải thuật:
  - **분할 정복 (Divide & Conquer):** Chia nhỏ bài toán gốc thành các bài toán con có cùng cấu trúc nhưng kích thước nhỏ hơn, giải quyết độc lập rồi gộp nghiệm lại (ví dụ: Merge Sort, Quick Sort).
  - **동적계획법 (Dynamic Programming):** Chia bài toán con nhưng các bài toán con bị lặp lại nhiều lần. Lưu kết quả của bài toán con vào bảng nhớ tạm (Memoization / Tabulation) để tái sử dụng ngay khi gặp lại mà không phải tính lại (ví dụ: Dãy Fibonacci, bài toán cái balo 0/1).
  - **탐욕법 (Greedy):** Tại mỗi bước đưa ra quyết định, luôn chọn phương án tối ưu cục bộ tốt nhất ngay tại thời điểm đó mà không quan tâm tương lai (ví dụ: Cây khung nhỏ nhất Kruskal/Prim, Dijkstra).
  - **백트래킹 (Backtracking):** Duyệt cây không gian trạng thái; nếu phát hiện nhánh đi vào ngõ cụt (không triển vọng - Non-promising) thì cắt tỉa cành (Pruning) và lùi lại nút cha để tìm hướng khác (ví dụ: Bài toán 8 Quân hậu N-Queens).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh 4 kỹ thuật thiết kế thuật toán cốt lõi:**

| Kỹ thuật giải thuật | Tư tưởng thiết kế trọng tâm | Xử lý bài toán con | Giải thuật tiêu biểu |
| :--- | :--- | :--- | :--- |
| **분할 정복 (Divide & Conquer)** | Chia bài toán lớn thành các phần nhỏ đến mức giải trực tiếp được, sau đó gộp lại | Các bài toán con **hoàn toàn độc lập** với nhau | **병합 정렬 (Merge Sort)**, **퀵 정렬 (Quick Sort)**, Tìm kiếm nhị phân |
| **동적계획법 (Dynamic Programming)** | Giải các bài toán nhỏ trước, lưu kết quả vào bộ nhớ để giải bài toán lớn | Các bài toán con **bị trùng lặp gối đầu (Overlapping)** | **피보나치 수열 (Fibonacci)**, Chuỗi con chung dài nhất (LCS), Floyd-Warshall |
| **탐욕법 (Greedy)** | Luôn chọn giải pháp tối ưu nhất trước mắt (Local Optimal) với hy vọng đạt tối ưu toàn cục | Không quay lui, đưa ra lựa chọn tức thì | **크루스칼 (Kruskal)**, **프림 (Prim)**, **다익스트라 (Dijkstra)**, Mã hóa Huffman |
| **백트래킹 (Backtracking)** | Thử đi theo một nhánh; nếu thấy không thỏa điều kiện thì quay lại nút cha | Duyệt cây trạng thái có **cắt tỉa cành (가지치기 - Pruning)** | **N-Queen 문제**, Bài toán Mã đi tuần, Mê cung (Maze Solving) |

- **Chuỗi thứ tự độ phức tạp thời gian Big-O (Nhanh $\rightarrow$ Chậm):**
  $$O(1) \lt O(\log n) \lt O(n) \lt O(n \log n) \lt O(n^2) \lt O(n^3) \lt O(2^n) \lt O(n!)$$
  - $O(1)$: Thời gian không đổi bất kể kích thước $n$ (ví dụ: tra cứu mảng theo chỉ số).
  - $O(\log n)$: Cực nhanh, giảm một nửa không gian mỗi bước (ví dụ: Binary Search).
  - $O(n \log n)$: Tối ưu cho sắp xếp so sánh (Heap Sort, Merge Sort).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Sự khác biệt giữa Cận trên và Trường hợp xấu nhất:**
  - $O$ (Big-O) là cận trên toán học của hàm số: $f(n) \le c \cdot g(n)$.
  - $\Omega$ (Big-Omega) là cận dưới toán học: $f(n) \ge c \cdot g(n)$.
  - $\Theta$ (Big-Theta) là cận chặt đồng thời cả trên và dưới.
  - Cần phân biệt rõ: Big-O là công cụ toán học, còn "Worst-case" là một kịch bản dữ liệu đầu vào.

### 복습 체크리스트
- [ ] Phân biệt được Divide & Conquer (bài toán con độc lập) và Dynamic Programming (bài toán con gối nhau có Memoization).
- [ ] Nhớ tư tưởng cốt lõi của Greedy: Chọn tối ưu cục bộ trước mắt.
- [ ] Nhớ kỹ thuật của Backtracking: Duyệt không gian trạng thái kết hợp tỉa cành (Pruning).
- [ ] Viết đúng chuỗi độ phức tạp Big-O từ $O(1)$ đến $O(n!)$.
