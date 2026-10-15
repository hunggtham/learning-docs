# 6. 정렬 알고리즘 (Sorting Algorithms)

## 학습 목표 (Mục tiêu)
- Định nghĩa và phân biệt cơ chế vận hành của ba thuật toán sắp xếp cơ bản: Sắp xếp chèn (삽입 정렬 - Insertion Sort), Sắp xếp chọn (선택 정렬 - Selection Sort) và Sắp xếp nổi bọt (버블 정렬 - Bubble Sort).
- Thành thạo kỹ năng mô phỏng từng vòng lặp (1회전, 2회전, 3회전) của từng thuật toán để trả lời chính xác các câu hỏi trạng thái mảng trong đề thi.
- Đánh giá độ phức tạp thời gian trung bình và xấu nhất $O(n^2)$ cùng đặc tính ổn định (Stability) của ba thuật toán sắp xếp cơ bản.

## 핵심 키워드 (Từ khóa)
- 정렬 알고리즘 (Sorting Algorithms)
- 삽입 정렬 (Insertion Sort / Chèn vị trí thích hợp)
- 선택 정렬 (Selection Sort / Chọn min/max đổi chỗ)
- 버블 정렬 (Bubble Sort / So sánh cặp phần tử kề nhau)
- 회전 (Pass / Vòng lặp sắp xếp)
- 시간 복잡도 $O(n^2)$
- 정렬의 안정성 (Stability)

## 선행·연결 개념 (Kiến thức liên kết)
- [01-bai-hoc.md](01-bai-hoc.md): Cấu trúc mảng tuyến tính (Array).
- [15-bai-hoc.md](15-bai-hoc.md): Các thuật toán sắp xếp nâng cao (Quick Sort, Merge Sort, Heap Sort).
- [17-bai-hoc.md](17-bai-hoc.md): Chi tiết thuật toán và biến thể của 삽입 정렬 (Insertion Sort).

## 읽는 방법 (Cách đọc)
- Phân biệt hành vi đặc trưng qua hình ảnh trực quan:
  - **Insertion Sort (Chèn):** Giống như bốc lá bài tây trên tay và chèn vào vị trí thích hợp trong dãy đã xếp. Bắt đầu từ phần tử thứ 2.
  - **Selection Sort (Chọn):** Tìm phần tử nhỏ nhất trong toàn dãy chưa xếp rồi đổi chỗ về đầu hàng.
  - **Bubble Sort (Nổi bọt):** So sánh từng cặp phần tử liền kề nhau (`A[j]` và `A[j+1]`), đẩy số lớn nhất về tận cùng đáy mảng sau mỗi vòng.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh ba thuật toán sắp xếp cơ bản:**

| Thuật toán (Hàn / Anh) | Cơ chế vận hành cốt lõi | Vị trí chốt cố định sau mỗi vòng | Thời gian (TB / Xấu nhất) |
| :--- | :--- | :--- | :--- |
| **삽입 정렬 (Insertion Sort)** | Bắt đầu từ phần tử thứ 2, so sánh ngược về trước để **chèn vào đúng vị trí** trong dãy con đã có thứ tự | Dãy con phía trước ngày càng dài ra và luôn có thứ tự nội bộ | $O(n^2)$ / $O(n^2)$ *(Tốt nhất: $O(n)$ khi mảng gần như đã xếp)* |
| **선택 정렬 (Selection Sort)** | Quét toàn bộ phần chưa xếp, **chọn phần tử nhỏ nhất** rồi hoán đổi với vị trí đầu tiên chưa chốt | **Chốt cố định phần tử nhỏ nhất ở ĐẦU mảng** sau mỗi vòng | $O(n^2)$ / $O(n^2)$ *(Bất kể dữ liệu ban đầu thế nào)* |
| **버블 정렬 (Bubble Sort)** | **So sánh 2 phần tử kề nhau**, nếu nghịch thế thì đổi chỗ, đẩy dần số lớn về sau | **Chốt cố định phần tử lớn nhất ở CUỐI mảng** sau mỗi vòng | $O(n^2)$ / $O(n^2)$ |

- **Mô phỏng truy vết từng vòng (Pass Trace) trên dãy số `[8, 5, 6, 2, 4]`:**
  - **1. 버블 정렬 (Bubble Sort - So sánh kề nhau):**
    - Ban đầu: `[8, 5, 6, 2, 4]`
    - So sánh (8, 5) $\rightarrow$ đổi chỗ: `[5, 8, 6, 2, 4]`
    - So sánh (8, 6) $\rightarrow$ đổi chỗ: `[5, 6, 8, 2, 4]`
    - So sánh (8, 2) $\rightarrow$ đổi chỗ: `[5, 6, 2, 8, 4]`
    - So sánh (8, 4) $\rightarrow$ đổi chỗ: `[5, 6, 2, 4, 8]`
    - **Kết thúc 1 vòng (1회전):** `[5, 6, 2, 4, 8]` (Số 8 to nhất đã chốt ở cuối).
  - **2. 선택 정렬 (Selection Sort - Chọn phần tử bé nhất):**
    - Ban đầu: `[8, 5, 6, 2, 4]`
    - Tìm min trong toàn dãy $\rightarrow$ Min là số `2` (ở vị trí index 3).
    - Đổi chỗ số `2` với số `8` ở vị trí đầu tiên:
    - **Kết thúc 1 vòng (1회전):** `[2, 5, 6, 8, 4]` (Số 2 bé nhất đã chốt ở đầu).
  - **3. 삽입 정렬 (Insertion Sort - Bốc phần tử thứ 2 chèn vào trước):**
    - Ban đầu: `[8, 5, 6, 2, 4]`
    - Lấy phần tử thứ hai là `5`, so với `8` $\rightarrow$ chèn `5` lên trước `8`:
    - **Kết thúc 1 vòng (1회전):** `[5, 8, 6, 2, 4]`.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tính ổn định của thuật toán sắp xếp (Stable Sort):**
  - **Thuật toán ổn định (Stable):** Giữ nguyên thứ tự tương đối ban đầu của các phần tử có giá trị khóa bằng nhau (Insertion Sort, Bubble Sort là Stable).
  - **Thuật toán không ổn định (Unstable):** Có thể làm đảo lộn thứ tự tương đối của các phần tử có cùng giá trị khóa (Selection Sort là Unstable).

### 복습 체크리스트
- [ ] Phân biệt rõ cách thức: Insertion (chèn), Selection (chọn min đổi lên đầu), Bubble (so cặp kề đẩy max về cuối).
- [ ] Viết đúng trạng thái mảng sau vòng 1 (1회전) của từng thuật toán.
- [ ] Nhớ độ phức tạp thời gian trung bình của cả 3 thuật toán là $O(n^2)$.
- [ ] Phân biệt được tính ổn định: Bubble và Insertion là Stable, Selection là Unstable.
