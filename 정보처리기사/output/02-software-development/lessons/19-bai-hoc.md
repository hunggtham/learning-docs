# 082: 선택 정렬 (Selection Sort)

## 학습 목표 (Mục tiêu)
- Định nghĩa chính xác thuật toán Sắp xếp chọn (선택 정렬 - Selection Sort) và cơ chế tìm giá trị nhỏ nhất (Minimum) để hoán đổi về đầu mảng.
- Hiểu rõ tại sao độ phức tạp thời gian của Selection Sort luôn cố định ở mức $O(n^2)$ trong mọi trường hợp (Tốt nhất, Trung bình, Xấu nhất).
- Thành thạo kỹ năng truy vết từng vòng lặp (1회전, 2회전, ...) và giải thích nguyên nhân Selection Sort là thuật toán không ổn định (Unstable).

## 핵심 키워드 (Từ khóa)
- 선택 정렬 (Selection Sort)
- 최소값 탐색 (Search for Minimum value)
- 교환 (Swap)
- 항상 $O(n^2)$ (Always $O(n^2)$)
- $n - 1$ 회전 (Total $n - 1$ passes)
- 불안정 정렬 (Unstable Sort)

## 선행·연결 개념 (Kiến thức liên kết)
- [14-bai-hoc.md](14-bai-hoc.md): So sánh Selection Sort với Insertion Sort và Bubble Sort.
- [16-bai-hoc.md](16-bai-hoc.md): Phân loại ổn định (Selection thuộc nhóm Unstable).
- [20-bai-hoc.md](20-bai-hoc.md): 버블 정렬 (Bubble Sort) - Đẩy giá trị lớn nhất về cuối mảng.

## 읽는 방법 (Cách đọc)
- Cứ thấy đề thi nhắc đến câu: **"최소값을 찾아 첫 번째 위치에 놓고, 남은 것 중 또 최소값을 찾아..."** (Tìm giá trị nhỏ nhất đưa về vị trí đầu tiên...) $\rightarrow$ Khoanh ngay **선택 정렬 (Selection Sort)**.
- Ghi nhớ đặc điểm "vững như bàn thạch": Dù mảng có xếp sẵn hay lộn xộn thì Selection Sort vẫn phải quét đủ $\frac{n(n-1)}{2}$ phép so sánh $\rightarrow$ Luôn là $O(n^2)$.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Cơ chế hoạt động của Selection Sort:**
  - Với mảng có $n$ phần tử, thuật toán thực hiện đúng $n - 1$ vòng lặp (Passes):
    - **Vòng 1 (1회전):** Quét từ vị trí 1 đến $n$, tìm phần tử có giá trị nhỏ nhất (Minimum), rồi hoán đổi với vị trí 1. Lúc này phần tử nhỏ nhất toàn mảng đã được chốt ở vị trí đầu.
    - **Vòng 2 (2회전):** Quét từ vị trí 2 đến $n$, tìm phần tử nhỏ nhất trong đoạn còn lại, rồi hoán đổi với vị trí 2.
    - **Vòng $i$ ($i$회전):** Tìm min từ vị trí $i$ đến $n$, hoán đổi với vị trí $i$.
- **Độ phức tạp và đặc tính:**
  - **Thời gian trong mọi trường hợp (Best, Avg, Worst):** Luôn là $\mathbf{O(n^2)}$.
    $$\text{Số phép so sánh cố định} = \sum_{i=1}^{n-1} (n - i) = \frac{n(n - 1)}{2}$$
  - **Số phép hoán đổi (Swaps):** Tối đa $n - 1$ lần (rất ít hoán đổi so với Bubble Sort).
  - **Bộ nhớ phụ:** $O(1)$ (Tại chỗ In-place).
  - **Tính ổn định:** **Unstable (Không ổn định)**.

- **Ví dụ mô phỏng truy vết mảng `[9, 6, 7, 3, 5]`:**
  - Ban đầu: `[9, 6, 7, 3, 5]`
  - **1회전 (Vòng 1):** Tìm min từ index 0 đến 4 $\rightarrow$ Min là số `3` (tại index 3). Đổi chỗ `3` với `9`:
    - Kết quả vòng 1: `[3, 6, 7, 9, 5]` *(Số 3 chốt ở đầu)*.
  - **2회전 (Vòng 2):** Tìm min trong phần còn lại `[6, 7, 9, 5]` $\rightarrow$ Min là số `5` (tại index 4). Đổi chỗ `5` với `6`:
    - Kết quả vòng 2: `[3, 5, 7, 9, 6]` *(Số 5 chốt ở vị trí 2)*.
  - **3회전 (Vòng 3):** Tìm min trong `[7, 9, 6]` $\rightarrow$ Min là `6`. Đổi chỗ `6` với `7`:
    - Kết quả vòng 3: `[3, 5, 6, 9, 7]`.
  - **4회전 (Vòng 4):** Tìm min trong `[9, 7]` $\rightarrow$ Min là `7`. Đổi chỗ `7` với `9`:
    - Kết quả vòng 4: `[3, 5, 6, 7, 9]`. Hoàn tất mảng!

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tại sao Selection Sort lại không ổn định (Unstable)?**
  - Xét mảng: $[5_A, 5_B, 2]$.
  - Ở vòng 1, số nhỏ nhất là $2$ được đổi chỗ với phần tử đầu tiên là $5_A$:
  - Mảng thành: $[2, 5_B, 5_A]$.
  - Ta thấy $5_A$ ban đầu đứng trước $5_B$, nhưng sau khi sắp xếp lại bị nhảy ra sau $5_B$. Thứ tự tương đối ban đầu đã bị đảo lộn $\rightarrow$ Đây chính là bản chất của Unstable Sort.

### 복습 체크리스트
- [ ] Nhớ cơ chế: Quét tìm giá trị nhỏ nhất (Minimum) đưa về đầu mảng sau mỗi vòng.
- [ ] Ghi nhớ thời gian của Selection Sort luôn luôn là $O(n^2)$ trong mọi trường hợp.
- [ ] Tính đúng số vòng lặp: Mảng $n$ phần tử cần chạy $n - 1$ vòng lặp.
- [ ] Giải thích được nguyên nhân Selection Sort là thuật toán không ổn định (Unstable).
