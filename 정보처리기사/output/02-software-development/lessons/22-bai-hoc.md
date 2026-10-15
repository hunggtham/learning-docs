# 085: 힙 정렬 (Heap Sort)

## 학습 목표 (Mục tiêu)
- Định nghĩa thuật toán Sắp xếp vun đống (힙 정렬 - Heap Sort) dựa trên cấu trúc Cây nhị phân hoàn chỉnh (완전 이진 트리 - Complete Binary Tree).
- Phân biệt hai loại cây Đống: Max-Heap (최대 힙 - Nút cha luôn lớn hơn hoặc bằng các nút con) và Min-Heap (최소 힙 - Nút cha luôn nhỏ hơn hoặc bằng các nút con).
- Nắm vững ưu điểm tuyệt đối về hiệu năng: Bảo đảm thời gian $O(n \log n)$ trong mọi trường hợp (kể cả xấu nhất) mà chỉ tốn bộ nhớ phụ tại chỗ $O(1)$.

## 핵심 키워드 (Từ khóa)
- 힙 정렬 (Heap Sort)
- 완전 이진 트리 (Complete Binary Tree)
- 최대 힙 (Max-Heap) & 최소 힙 (Min-Heap)
- 힙 생성 과정 (Heapify)
- 항상 $O(n \log n)$ (Always $O(n \log n)$)
- 제자리 정렬 (In-place Sort / $O(1)$)
- 불안정 정렬 (Unstable Sort)

## 선행·연결 개념 (Kiến thức liên kết)
- [05-bai-hoc.md](05-bai-hoc.md): Định nghĩa Cây (Tree) và các chỉ số hình học.
- [08-bai-hoc.md](08-bai-hoc.md): Cây nhị phân và các tính chất cấu trúc nút.
- [21-bai-hoc.md](21-bai-hoc.md): 퀵 정렬 (Quick Sort) - So sánh với Heap Sort về độ ổn định Worst Case.
- [23-bai-hoc.md](23-bai-hoc.md): 2-Way 합병 정렬 (Merge Sort) - So sánh về mức sử dụng bộ nhớ phụ.

## 읽는 방법 (Cách đọc)
- Cứ thấy đề thi có từ khóa: **"완전 이진 트리 (Complete Binary Tree)"** hoặc **"전이진 트리"** hoặc **"최대 힙 / 최소 힙"** $\rightarrow$ Khẳng định 100% đáp án là **힙 정렬 (Heap Sort)**.
- Ghi nhớ bộ ba bất biến: Best, Average, Worst của Heap Sort đều là **$O(n \log n)$**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Cơ chế hoạt động của Heap Sort (J. W. J. Williams đề xuất năm 1964):**
  1. **Tạo Đống ban đầu (Build Heap / Heapify):**
     - Biểu diễn mảng 1 chiều $n$ phần tử dưới dạng một Cây nhị phân hoàn chỉnh (với nút cha ở chỉ số $i$, con trái ở $2i$, con phải ở $2i + 1$).
     - Hiệu chỉnh cây từ dưới lên trên để thỏa mãn tính chất **최대 힙 (Max-Heap)**: Giá trị của mọi nút cha đều phải lớn hơn hoặc bằng các nút con của nó ($\text{Parent} \ge \text{Child}$).
     - Sau bước này, **nút gốc (Root) luôn luôn chứa phần tử lớn nhất của toàn bộ mảng**.
  2. **Trích xuất và Tái cấu trúc đống (Extract & Reheapify):**
     - Đổi chỗ phần tử ở Root (lớn nhất) với phần tử cuối cùng của mảng chưa xếp.
     - Thu hẹp kích thước đống đi 1 phần tử (vì phần tử lớn nhất đã được chốt ở cuối mảng).
     - Tiến hành vun lại đống (Heapify) cho nút gốc mới để đưa phần tử lớn nhì lên Root.
     - Lặp lại thao tác này $n - 1$ lần cho đến khi đống chỉ còn 1 phần tử.
- **Độ phức tạp thời gian và không gian:**
  - **Thời gian trong mọi trường hợp (Best, Avg, Worst):** Luôn là $\mathbf{O(n \log n)}$.
    - Giai đoạn tạo đống ban đầu tốn $O(n)$.
    - Mỗi lần trích xuất và vun lại đống tốn $O(\log n)$, làm $n$ lần tốn $O(n \log n)$.
  - **Bộ nhớ phụ:** $\mathbf{O(1)}$ (Sắp xếp tại chỗ In-place trực tiếp trên mảng, không cần mảng tạm).
  - **Tính ổn định:** **Unstable (Không ổn định)**.

- **Bẫy đề thi trắc nghiệm:**
  - **Bẫy 1:** *"Thuật toán sắp xếp nào sử dụng cấu trúc cây nhị phân hoàn chỉnh?"* $\rightarrow$ Đáp án: **힙 정렬 (Heap Sort)**.
  - **Bẫy 2:** *"So sánh Heap Sort và Merge Sort về mức độ tiêu tốn bộ nhớ?"* $\rightarrow$ Heap Sort vượt trội hơn vì là In-place ($O(1)$), trong khi Merge Sort tốn thêm mảng phụ $O(n)$.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ứng dụng thực tế của Heap trong hệ điều hành:**
  - Cấu trúc dữ liệu Đống (Heap) là nền tảng cốt lõi để triển khai **Hàng đợi ưu tiên (Priority Queue)** trong hệ điều hành:
    - Lập lịch tiến trình theo độ ưu tiên cao nhất (Highest Priority First).
    - Thuật toán tìm đường đi ngắn nhất Dijkstra và thuật toán cây khung nhỏ nhất Prim.

### 복습 체크리스트
- [ ] Nhớ cấu trúc dữ liệu nền tảng: 완전 이진 트리 (Complete Binary Tree).
- [ ] Định nghĩa Max-Heap (Cha $\ge$ Con, Root là số lớn nhất) và Min-Heap (Cha $\le$ Con, Root là số nhỏ nhất).
- [ ] Ghi nhớ thời gian của Heap Sort luôn cố định $O(n \log n)$ trong mọi trường hợp.
- [ ] Nêu được ưu điểm của Heap Sort so với Merge Sort: Bộ nhớ phụ chỉ tốn $O(1)$.
