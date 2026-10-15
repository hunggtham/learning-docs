# 081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và cơ chế hoạt động của thuật toán Sắp xếp chèn (삽입 정렬 - Insertion Sort).
- Hiểu rõ quy tắc bắt đầu từ phần tử thứ 2 ($i = 2$) và so sánh ngược về phía trước để tìm vị trí thích hợp chèn vào mảng con đã được sắp xếp.
- Thành thạo mô phỏng từng vòng lặp (1회전, 2회전, 3회전) và nhận biết trường hợp tốt nhất đạt độ phức tạp tuyến tính $O(n)$.

## 핵심 키워드 (Từ khóa)
- 삽입 정렬 (Insertion Sort)
- 이미 순서화된 부분 (Subarray already sorted)
- 제2 원소부터 시작 (Starts from 2nd element)
- $n - 1$ 회전 (Total $n - 1$ passes)
- 최선의 시간 복잡도 $O(n)$
- 평균/최악의 시간 복잡도 $O(n^2)$
- 안정 정렬 (Stable Sort)

## 선행·연결 개념 (Kiến thức liên kết)
- [14-bai-hoc.md](14-bai-hoc.md): So sánh tổng quan 3 thuật toán sắp xếp cơ bản (Insertion, Selection, Bubble).
- [16-bai-hoc.md](16-bai-hoc.md): Ma trận độ phức tạp và tính ổn định của các thuật toán sắp xếp.
- [18-bai-hoc.md](18-bai-hoc.md): 셸 정렬 (Shell Sort) - Bản nâng cấp vượt bậc của Insertion Sort với bước nhảy khoảng cách $h$.

## 읽는 방법 (Cách đọc)
- Cứ thấy đề thi nhắc đến: **"이미 순서화된 앞부분에 새로운 레코드를 순서에 맞게 삽입"** (Chèn phần tử mới vào đúng vị trí trong phần mảng đã có thứ tự phía trước) $\rightarrow$ Khoanh ngay **삽입 정렬 (Insertion Sort)**.
- Khi làm bài toán theo từng vòng: Vòng 1 cố định 2 phần tử đầu, vòng 2 cố định 3 phần tử đầu...

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Cơ chế hoạt động cốt lõi của Insertion Sort:**
  - Coi phần tử đầu tiên ($A[1]$) là một mảng con đã được sắp xếp có độ dài 1.
  - Bắt đầu duyệt từ phần tử thứ 2 ($A[2]$) đến phần tử cuối cùng ($A[n]$):
    - Lấy giá trị $A[i]$ làm chìa khóa (Key).
    - So sánh ngược về phía trước với các phần tử thuộc mảng con đã sắp xếp ($A[i-1], A[i-2], \dots$).
    - Dịch chuyển các phần tử lớn hơn chìa khóa sang phải một vị trí, sau đó **chèn chìa khóa vào vị trí trống thích hợp vừa tạo ra**.
  - Tổng số vòng lặp cần thực hiện để hoàn tất mảng $n$ phần tử là: **$n - 1$ vòng (Passes)**.
- **Độ phức tạp thời gian:**
  - **Tốt nhất (Best Case):** $\mathbf{O(n)}$ khi dữ liệu đầu vào đã được sắp xếp tăng dần sẵn (mỗi phần tử chỉ cần so sánh 1 lần với phần tử ngay trước nó rồi dừng).
  - **Trung bình (Average):** $\mathbf{O(n^2)}$.
  - **Xấu nhất (Worst Case):** $\mathbf{O(n^2)}$ khi dữ liệu ban đầu bị xếp ngược chiều giảm dần hoàn toàn.

- **Ví dụ truy vết từng vòng (Pass Trace) trên dãy số `[5, 4, 3, 2, 1]`:**
  - Ban đầu: `[5, 4, 3, 2, 1]`
  - **1회전 (Vòng 1 - Xét số 4):** So sánh `4` với `5` $\rightarrow$ chèn `4` trước `5` $\rightarrow$ Dãy thành: `[4, 5, 3, 2, 1]`.
  - **2회전 (Vòng 2 - Xét số 3):** So sánh `3` với `5` và `4` $\rightarrow$ chèn `3` lên đầu $\rightarrow$ Dãy thành: `[3, 4, 5, 2, 1]`.
  - **3회전 (Vòng 3 - Xét số 2):** Chèn `2` lên đầu $\rightarrow$ Dãy thành: `[2, 3, 4, 5, 1]`.
  - **4회전 (Vòng 4 - Xét số 1):** Chèn `1` lên đầu $\rightarrow$ Dãy thành: `[1, 2, 3, 4, 5]`. Hoàn tất!

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ưu điểm thực tế của Insertion Sort:**
  - Cài đặt vô cùng đơn giản, là thuật toán sắp xếp tại chỗ (In-place sort) không tốn bộ nhớ phụ ($O(1)$).
  - Hoạt động cực kỳ hiệu quả đối với các tập dữ liệu có kích thước nhỏ ($n < 50$) hoặc các tập dữ liệu **gần như đã được sắp xếp sẵn (Nearly Sorted Data)**.
  - Đây là lý do nhiều thuật toán lai hiện đại (như Timsort trong Python/Java) sử dụng Insertion Sort cho các mảng con kích thước nhỏ.

### 복습 체크리스트
- [ ] Nhớ từ khóa định danh: Chèn phần tử vào mảng con đã sắp xếp phía trước.
- [ ] Nhớ quy tắc: Bắt đầu từ phần tử thứ 2, tổng cộng chạy $n - 1$ vòng lặp.
- [ ] Ghi nhớ thời gian tốt nhất là $O(n)$ khi mảng đã sắp xếp sẵn.
- [ ] Truy vết thành thạo kết quả của mảng sau vòng 1 và vòng 2.
