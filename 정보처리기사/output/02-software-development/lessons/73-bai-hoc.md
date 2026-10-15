# 18. 최악의 시간 복잡도 (Worst-case Time Complexity)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm độ phức tạp thời gian trong trường hợp xấu nhất (최악의 시간 복잡도 - Worst-case Time Complexity) và ký pháp Big-O ($O$).
- Hiểu rõ thứ tự tăng dần của các bậc độ phức tạp thuật toán: $O(1) \lt O(\log n) \lt O(n) \lt O(n \log n) \lt O(n^2) \lt O(n^3) \lt O(2^n) \lt O(n!)$.
- Phân tích và nhận diện chính xác độ phức tạp thời gian của các cấu trúc dữ liệu và giải thuật sắp xếp/tìm kiếm thông dụng trong đề thi.

## 핵심 키워드 (Từ khóa)
- 시간 복잡도 (Time Complexity)
- 최악의 시간 복잡도 (Worst-case Time Complexity / Big-O Notation)
- 상수 시간 (Constant Time - $O(1)$)
- 로그 시간 (Logarithmic Time - $O(\log n)$)
- 선형 시간 (Linear Time - $O(n)$)
- 선형 로그 시간 (Linearithmic Time - $O(n \log n)$)
- 다항 및 지수 시간 (Polynomial vs Exponential Time - $O(n^2)$, $O(2^n)$)

## 선행·연결 개념 (Kiến thức liên kết)
- [72-bai-hoc.md](72-bai-hoc.md): Định luật Pareto và hiện tượng tập trung lỗi trong kiểm thử.
- [74-bai-hoc.md](74-bai-hoc.md): Các nguyên tắc viết mã nguồn sạch (Clean Code).
- [16-bai-hoc.md](16-bai-hoc.md): Bảng tổng hợp độ phức tạp của các thuật toán sắp xếp.

## 읽는 방법 (Cách đọc)
- Ghi nhớ chuỗi so sánh tốc độ tăng trưởng của hàm thời gian:
  - Càng về bên phải, thời gian chạy càng bùng nổ khi kích thước đầu vào $n$ tăng lớn:
  $$O(1) \lt O(\log n) \lt O(n) \lt O(n \log n) \lt O(n^2) \lt O(n^3) \lt O(2^n) \lt O(n!)$$
  - Chú ý trường hợp ngoại lệ: Sắp xếp Quick Sort có trung bình là $O(n \log n)$ nhưng trường hợp xấu nhất là $O(n^2)$, trong khi Heap Sort và Merge Sort luôn giữ vững $O(n \log n)$ ở mọi trường hợp.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng phân loại các bậc thời gian Big-O thông dụng:**

| Ký pháp Big-O | Tên gọi học thuật | Ví dụ thao tác tiêu biểu | Nhận xét hiệu năng |
| :--- | :--- | :--- | :--- |
| **$O(1)$** | **상수형 (Constant)** | Đẩy/rút phần tử ở đỉnh Stack (`Push`/`Pop`), lấy phần tử mảng bằng chỉ số `A[i]` | Tối ưu nhất; thời gian thực thi không phụ thuộc vào kích thước dữ liệu $n$ |
| **$O(\log n)$** | **로그형 (Logarithmic)** | Tìm kiếm nhị phân (Binary Search), tìm kiếm trên cây tìm kiếm nhị phân cân bằng (AVL) | Rất nhanh; mỗi bước kiểm tra giảm đi một nửa không gian tìm kiếm |
| **$O(n)$** | **선형 (Linear)** | Tìm kiếm tuần tự (Sequential Search), duyệt một vòng lặp qua mảng $n$ phần tử | Thời gian tăng tỉ lệ thuận trực tiếp với số lượng phần tử đầu vào |
| **$O(n \log n)$** | **선형로그형 (Linearithmic)** | Sắp xếp vun đống (Heap Sort), Sắp xếp trộn (Merge Sort), Sắp xếp nhanh trung bình (Quick Sort Avg) | Chuẩn mực tối ưu cho các thuật toán sắp xếp dựa trên so sánh |
| **$O(n^2)$** | **2차형 (Quadratic)** | Sắp xếp chèn (Insertion Sort), Sắp xếp chọn (Selection Sort), Sắp xếp nổi bọt (Bubble Sort) | Vòng lặp lồng nhau 2 lớp; hiệu năng kém khi $n$ lớn |
| **$O(2^n)$** | **지수형 (Exponential)** | Bài toán Tháp Hà Nội (Tower of Hanoi), vét cạn tìm tập hợp con (Power Set) | Thời gian tăng theo hàm mũ; không khả thi trong thực tế khi $n$ lớn |
| **$O(n!)$** | **팩토리얼 (Factorial)** | Bài toán Người du lịch vét cạn (Traveling Salesperson Problem - Brute-force) | Bùng nổ tổ hợp khủng khiếp nhất |

- **So sánh độ phức tạp trường hợp xấu nhất của các thuật toán kinh điển:**

| Giải thuật | Trường hợp tốt nhất (Best) | Trường hợp trung bình (Average) | Trường hợp xấu nhất (Worst) |
| :--- | :--- | :--- | :--- |
| **선택 정렬 (Selection Sort)** | $O(n^2)$ | $O(n^2)$ | **$O(n^2)$** |
| **버블 정렬 (Bubble Sort)** | $O(n)$ (có cờ hiệu Flag) | $O(n^2)$ | **$O(n^2)$** |
| **삽입 정렬 (Insertion Sort)** | $O(n)$ (đã có thứ tự sẵn) | $O(n^2)$ | **$O(n^2)$** |
| **퀵 정렬 (Quick Sort)** | $O(n \log n)$ | $O(n \log n)$ | **$O(n^2)$** (khi chọn trúng Pivot max/min) |
| **힙 정렬 (Heap Sort)** | $O(n \log n)$ | $O(n \log n)$ | **$O(n \log n)$** |
| **병합 정렬 (Merge Sort)** | $O(n \log n)$ | $O(n \log n)$ | **$O(n \log n)$** |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ý nghĩa của việc phân tích Worst-case trong kỹ nghệ phần mềm:**
  - Trong các hệ thống thời gian thực (Real-time Systems) như hệ thống phanh xe tự động hoặc điều khiển vệ tinh, phân tích Worst-case là bắt buộc để đảm bảo hệ thống luôn trả về phản hồi trong thời hạn tối đa cho phép (Deadline).
  - Ký pháp Big-O thể hiện cận trên của hàm tăng trưởng thời gian: $f(n) \le c \cdot g(n)$ với mọi $n \ge n_0$.

### 복습 체크리스트
- [ ] Viết đúng chuỗi thứ tự tăng dần từ $O(1)$ đến $O(n!)$.
- [ ] Nhớ Heap Sort và Merge Sort có Worst-case là $O(n \log n)$.
- [ ] Nhớ Quick Sort có Worst-case rơi vào $O(n^2)$.
- [ ] Nhớ thao tác Stack Push/Pop và Queue Enqueue/Dequeue có thời gian $O(1)$.
