# 028: 정렬 (Sorting / Thuật toán sắp xếp)

## 학습 목표 (Mục tiêu)
- Nắm vững bức tranh toàn cảnh và phân loại hai nhóm giải thuật sắp xếp: Sắp xếp nội bộ (내부 정렬 - Internal Sort trong bộ nhớ chính) và Sắp xếp ngoại vi (외부 정렬 - External Sort trên bộ nhớ phụ).
- Phân biệt rõ tính ổn định (안정성 - Stability): Nhận diện các thuật toán sắp xếp ổn định (Stable Sort) và không ổn định (Unstable Sort).
- Thuộc nằm lòng bảng ma trận độ phức tạp thời gian (Tốt nhất, Trung bình, Xấu nhất) và không gian bộ nhớ của toàn bộ 8 thuật toán sắp xếp kinh điển.

## 핵심 키워드 (Từ khóa)
- 내부 정렬 (Internal Sort) & 외부 정렬 (External Sort)
- 안정 정렬 (Stable Sort) & 불안정 정렬 (Unstable Sort)
- 시간 복잡도 (Time Complexity: $O(n^2)$, $O(n \log n)$, $O(dn)$)
- 공간 복잡도 (Space Complexity)
- 정렬 알고리즘 비교 (Sorting Algorithms Matrix)

## 선행·연결 개념 (Kiến thức liên kết)
- [14-bai-hoc.md](14-bai-hoc.md): Các thuật toán sắp xếp cơ bản (Insertion, Selection, Bubble).
- [15-bai-hoc.md](15-bai-hoc.md): Các thuật toán sắp xếp nâng cao (Quick, Merge, Heap).
- [17-bai-hoc.md](17-bai-hoc.md): Đi sâu chi tiết cơ chế hoạt động của Sắp xếp chèn (Insertion Sort).

## 읽는 방법 (Cách đọc)
- Học thuộc hai nhóm phân loại ổn định:
  - **Ổn định (Stable):** **삽-버-병-기** (Chèn - Bọt - Hợp nhất - Cơ số / Insertion, Bubble, Merge, Radix).
  - **Không ổn định (Unstable):** **선-셸-퀵-힙** (Chọn - Shell - Quick - Heap / Selection, Shell, Quick, Heap).
- Thuộc làu nhóm hiệu năng cao $O(n \log n)$: **Quick, Merge, Heap**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp ma trận 8 thuật toán sắp xếp nội bộ kinh điển:**

| Thuật toán (Hàn / Anh) | Tốt nhất (Best) | Trung bình (Avg) | Xấu nhất (Worst) | Bộ nhớ phụ | Tính ổn định |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **삽입 정렬 (Insertion Sort)** | $O(n)$ | $\mathbf{O(n^2)}$ | $O(n^2)$ | $O(1)$ | **Stable (Ổn định)** |
| **선택 정렬 (Selection Sort)** | $O(n^2)$ | $\mathbf{O(n^2)}$ | $O(n^2)$ | $O(1)$ | Unstable (Không ổn định) |
| **버블 정렬 (Bubble Sort)** | $O(n)$ *(dùng cờ Flag)* | $\mathbf{O(n^2)}$ | $O(n^2)$ | $O(1)$ | **Stable (Ổn định)** |
| **셸 정렬 (Shell Sort)** | $O(n)$ | $\mathbf{O(n^{1.25}) \sim O(n^{1.5})}$ | $O(n^2)$ | $O(1)$ | Unstable (Không ổn định) |
| **퀵 정렬 (Quick Sort)** | $O(n \log n)$ | $\mathbf{O(n \log n)}$ | $\mathbf{O(n^2)}$ | $O(\log n)$ | Unstable (Không ổn định) |
| **2-Way 합병 정렬 (Merge Sort)** | $O(n \log n)$ | $\mathbf{O(n \log n)}$ | $\mathbf{O(n \log n)}$ | $O(n)$ | **Stable (Ổn định)** |
| **힙 정렬 (Heap Sort)** | $O(n \log n)$ | $\mathbf{O(n \log n)}$ | $\mathbf{O(n \log n)}$ | $O(1)$ | Unstable (Không ổn định) |
| **기수 정렬 (Radix Sort)** | $O(dn)$ | $\mathbf{O(dn)}$ | $O(dn)$ | $O(n + k)$ | **Stable (Ổn định)** |

- **Phân loại Nội bộ vs Ngoại vi:**
  - **내부 정렬 (Internal Sort):** Toàn bộ dữ liệu nằm gọn trong RAM (Bộ nhớ chính). Tốc độ cực nhanh. Bao gồm cả 8 thuật toán trong bảng trên.
  - **외부 정렬 (External Sort):** Khối lượng dữ liệu quá lớn không thể nạp hết vào RAM, phải lưu trữ trên thiết bị ngoại vi (Ổ đĩa, Băng từ). Áp dụng các thuật toán hòa trộn: **2-Way Merge Sort, Multi-way Merge Sort, Polyphase Merge, Cascade Merge**.

- **Bẫy đề thi trắc nghiệm:**
  - **Bẫy 1:** *"Thuật toán nào sau đây KHÔNG PHẢI là thuật toán sắp xếp ổn định (Stable)?"* $\rightarrow$ Tra cứu thần chú "선-셸-퀵-힙" $\rightarrow$ Chọn một trong các đáp án Selection, Shell, Quick, Heap.
  - **Bẫy 2:** *"Sắp xếp nào vượt qua giới hạn $O(n \log n)$ mà không cần so sánh các cặp khóa?"* $\rightarrow$ Đáp án: **기수 정렬 (Radix Sort)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ý nghĩa thực tế của Tính ổn định (Stability):**
  - Giả sử có danh sách sinh viên đã được sắp xếp tăng dần theo Tên. Nay ta muốn sắp xếp tiếp theo Điểm số:
    - Nếu dùng thuật toán **Stable**: Các sinh viên có cùng điểm số vẫn sẽ giữ nguyên thứ tự sắp xếp theo Tên ban đầu.
    - Nếu dùng thuật toán **Unstable**: Thứ tự theo Tên của các sinh viên cùng điểm số có thể bị đảo lộn ngẫu nhiên.

### 복습 체크리스트
- [ ] Nhớ tên 4 thuật toán Stable (삽-버-병-기: Insertion, Bubble, Merge, Radix).
- [ ] Nhớ tên 4 thuật toán Unstable (선-셸-퀵-힙: Selection, Shell, Quick, Heap).
- [ ] Xác định 3 thuật toán đạt chuẩn $O(n \log n)$: Quick, Merge, Heap.
- [ ] Phân biệt được Internal Sort (trong RAM) và External Sort (ngoại vi ổ đĩa).
