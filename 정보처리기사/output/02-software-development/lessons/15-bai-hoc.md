# 31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)

## 학습 목표 (Mục tiêu)
- Nắm vững cơ chế vận hành và nguyên lý thiết kế của các thuật toán sắp xếp nâng cao: Quick Sort (퀵 정렬), Merge Sort (2-Way 합병 정렬) và Heap Sort (힙 정렬).
- Thuộc nằm lòng ma trận độ phức tạp thời gian (Tốt nhất, Trung bình, Xấu nhất) và độ phức tạp không gian bộ nhớ của từng thuật toán.
- Hiểu rõ hiện tượng thoái hóa hiệu năng xuống $O(n^2)$ của Quick Sort khi dữ liệu đã được sắp xếp trước và cách khắc phục.

## 핵심 키워드 (Từ khóa)
- 퀵 정렬 (Quick Sort / 피벗 Pivot / 분할 정복)
- 2-Way 합병 정렬 (Merge Sort / $O(n \log n)$ / 안정 정렬)
- 힙 정렬 (Heap Sort / 완전 이진 트리 Complete Binary Tree)
- 셸 정렬 (Shell Sort / 매개변수 간격 삽입 정렬)
- 기수 정렬 (Radix Sort / 큐 버킷 정렬 / $O(d \cdot n)$)
- 시간 복잡도 비교 (Time Complexity Matrix)

## 선행·연결 개념 (Kiến thức liên kết)
- [05-bai-hoc.md](05-bai-hoc.md): Cây nhị phân hoàn chỉnh (Complete Binary Tree) nền tảng của Heap Sort.
- [14-bai-hoc.md](14-bai-hoc.md): Các thuật toán sắp xếp cơ bản (Insertion, Selection, Bubble).
- [21-bai-hoc.md](21-bai-hoc.md): Chi tiết thuật toán và giải thuật phân vùng của Quick Sort.
- [23-bai-hoc.md](23-bai-hoc.md): Chi tiết giải thuật trộn của 2-Way Merge Sort.

## 읽는 방법 (Cách đọc)
- Học thuộc ma trận độ phức tạp thời gian trong TẦNG A (đặc biệt các thuật toán đạt $O(n \log n)$).
- Chú ý các từ khóa nhận diện đề thi trắc nghiệm:
  - Cứ thấy **"Pivot (피벗)"**, **"Chia thành 2 mảng con lớn/nhỏ hơn chốt"** $\rightarrow$ **퀵 정렬 (Quick Sort)**.
  - Cứ thấy **"Trộn 2 tệp đã sắp xếp thành 1 tệp"** $\rightarrow$ **합병 정렬 (Merge Sort)**.
  - Cứ thấy **"Cây nhị phân hoàn chỉnh (완전 이진 트리)"** hoặc **"Heap (힙)"** $\rightarrow$ **힙 정렬 (Heap Sort)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp đặc tính các thuật toán sắp xếp nâng cao:**

| Thuật toán (Hàn / Anh) | Nguyên lý hoạt động cốt lõi | Thời gian trung bình | Thời gian xấu nhất | Không gian phụ | Tính ổn định |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **퀵 정렬 (Quick Sort)** | Chọn phần tử chốt (Pivot), phân vùng mảng thành 2 phần: nhỏ hơn chốt sang trái, lớn hơn sang phải (Chia để trị) | $\mathbf{O(n \log n)}$ | $\mathbf{O(n^2)}$ *(Khi mảng đã xếp sẵn)* | $O(\log n)$ | Không ổn định (Unstable) |
| **2-Way 합병 정렬 (Merge Sort)** | Chia đôi mảng cho đến từng phần tử đơn lẻ, sau đó **hòa trộn (Merge) từng cặp tệp con đã sắp xếp** | $\mathbf{O(n \log n)}$ | $\mathbf{O(n \log n)}$ | $O(n)$ *(Tốn thêm mảng phụ)* | **Ổn định (Stable)** |
| **힙 정렬 (Heap Sort)** | Xây dựng cấu trúc **Cây nhị phân hoàn chỉnh (Complete Binary Tree)** thành Max-Heap/Min-Heap rồi liên tục rút đỉnh gốc | $\mathbf{O(n \log n)}$ | $\mathbf{O(n \log n)}$ | $O(1)$ *(In-place)* | Không ổn định (Unstable) |
| **셸 정렬 (Shell Sort)** | Cải tiến từ Insertion Sort: chia mảng thành các nhóm con theo khoảng cách bước nhảy (Gap), thu hẹp Gap dần | $O(n^{1.25}) \sim O(n^{1.5})$ | $O(n^2)$ | $O(1)$ | Không ổn định (Unstable) |
| **기수 정렬 (Radix Sort)** | Không dùng phép so sánh: Dùng các thùng Hàng đợi (Queue/Bucket) để phân loại từng chữ số từ hàng đơn vị lên hàng cao | $O(d \cdot n)$ *(d là số chữ số)* | $O(d \cdot n)$ | $O(n + k)$ | **Ổn định (Stable)** |

- **Bẫy đề thi trắc nghiệm kinh điển:**
  - **Bẫy 1:** *"Thuật toán nào có tốc độ trung bình nhanh nhất nhưng khi gặp mảng đã được sắp xếp tăng dần sẵn thì hiệu năng tụt xuống $O(n^2)$?"* $\rightarrow$ Đáp án: **퀵 정렬 (Quick Sort)**.
  - **Bẫy 2:** *"Thuật toán nào luôn bảo đảm thời gian $O(n \log n)$ trong mọi trường hợp (kể cả xấu nhất) VÀ là thuật toán sắp xếp ổn định (Stable)?"* $\rightarrow$ Đáp án: **합병 정렬 (Merge Sort)**.
  - **Bẫy 3:** *"Thuật toán Heap Sort sử dụng cấu trúc dữ liệu nào?"* $\rightarrow$ Đáp án: **완전 이진 트리 (Complete Binary Tree)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh Merge Sort vs Quick Sort:**
  - Cả hai đều cùng áp dụng triết lý thiết kế giải thuật **Chia để trị (Divide and Conquer)**:
    - Quick Sort: Công đoạn nặng nhọc nằm ở bước **Chia (Partitioning)**; bước gộp kết quả là tức thì $O(1)$.
    - Merge Sort: Bước chia là chia đôi đơn giản ở giữa $O(1)$; công đoạn nặng nhọc nằm ở bước **Hòa trộn (Merging)** tốn thêm mảng tạm kích thước $O(n)$.
- **Max-Heap và Min-Heap trong Heap Sort:**
  - **Max-Heap:** Giá trị của nút cha luôn lớn hơn hoặc bằng giá trị các nút con. Nút Root luôn chứa giá trị lớn nhất của toàn cây.

### 복습 체크리스트
- [ ] Nhớ bảng độ phức tạp thời gian: Quick ($n \log n \rightarrow n^2$), Merge ($n \log n \rightarrow n \log n$), Heap ($n \log n \rightarrow n \log n$).
- [ ] Nhớ Quick Sort bị thoái hóa thành $O(n^2)$ khi dãy đã có thứ tự sẵn.
- [ ] Phân biệt đặc trưng: Merge Sort tốn bộ nhớ phụ $O(n)$ và là Stable Sort; Heap Sort dùng cây nhị phân hoàn chỉnh.
- [ ] Nhớ Radix Sort sắp xếp dựa trên các hàng chữ số dùng Queue và không cần so sánh khóa.
