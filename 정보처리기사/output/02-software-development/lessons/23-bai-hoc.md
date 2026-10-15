# 086: 2-Way 합병 정렬 (Merge Sort)

## 학습 목표 (Mục tiêu)
- Định nghĩa thuật toán Sắp xếp hòa trộn 2 đường (2-Way 합병 정렬 - 2-Way Merge Sort) dựa trên nguyên lý Chia để trị (Divide and Conquer).
- Nắm vững quy trình phân tách mảng liên tục cho đến từng phần tử đơn lẻ và hợp nhất tuần tự các tệp con đã có thứ tự lại với nhau ($1 \rightarrow 2 \rightarrow 4 \rightarrow 8 \dots$).
- Hiểu rõ hai đặc tính sống còn của Merge Sort: Luôn duy trì độ phức tạp thời gian $O(n \log n)$ trong mọi hoàn cảnh và là thuật toán sắp xếp ổn định (Stable Sort), cùng nhược điểm tốn thêm bộ nhớ đệm $O(n)$.

## 핵심 키워드 (Từ khóa)
- 2-Way 합병 정렬 (2-Way Merge Sort)
- 분할과 정복 (Divide and Conquer)
- 이미 정렬된 두 개의 서브파일 (Merging two sorted subarrays)
- 항상 $O(n \log n)$ (Always $O(n \log n)$)
- 추가 기억 공간 $O(n)$ (Auxiliary space $O(n)$)
- 안정 정렬 (Stable Sort)
- 외부 정렬의 기본 (Foundation of External Sorting)

## 선행·연결 개념 (Kiến thức liên kết)
- [15-bai-hoc.md](15-bai-hoc.md): So sánh tổng quan các thuật toán sắp xếp nâng cao (Quick, Merge, Heap).
- [21-bai-hoc.md](21-bai-hoc.md): 퀵 정렬 (Quick Sort) - Thuật toán chia để trị đối trọng.
- [24-bai-hoc.md](24-bai-hoc.md): 기수 정렬 (Radix Sort) - Thuật toán sắp xếp ổn định không cần so sánh khóa.

## 읽는 방법 (Cách đọc)
- Cứ thấy đề thi có cụm từ: **"이미 정렬되어 있는 두 개의 파일을 하나의 파일로 합병"** (Hợp nhất hai tệp đã sắp xếp thành một tệp) $\rightarrow$ Khẳng định ngay **2-Way 합병 정렬 (Merge Sort)**.
- Ghi nhớ 2 điểm đặc trưng: Luôn luôn là **$O(n \log n)$** và là thuật toán **Ổn định (Stable)**, nhưng bị điểm trừ là **tốn thêm RAM $O(n)$**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Cơ chế vận hành của 2-Way Merge Sort:**
  - **Giai đoạn 1 (Phân tách - Divide):** Chia đôi mảng liên tục thành 2 nửa bằng nhau cho đến khi mỗi mảng con chỉ còn chứa đúng 1 phần tử (vì mảng 1 phần tử mặc nhiên được coi là đã sắp xếp).
  - **Giai đoạn 2 (Hòa trộn - Merge):**
    - Lấy từng cặp 2 mảng con kề nhau, so sánh các phần tử ở đầu mỗi mảng con để chọn phần tử nhỏ hơn đưa vào mảng đệm kết quả.
    - Cứ thế gộp từ kích thước $1 \rightarrow 2$, từ $2 \rightarrow 4$, từ $4 \rightarrow 8$ cho đến khi toàn bộ mảng được hợp nhất hoàn chỉnh.
- **Độ phức tạp thời gian và không gian:**
  - **Thời gian trong mọi trường hợp (Best, Avg, Worst):** Luôn đạt $\mathbf{O(n \log n)}$ tuyệt đối (Cây phân tách có độ sâu $\log_2 n$, mỗi tầng cây thực hiện phép gộp tốn $O(n)$ thời gian).
  - **Bộ nhớ phụ:** $\mathbf{O(n)}$ (Bắt buộc phải cấp phát một mảng tạm có kích thước bằng mảng gốc để chứa kết quả khi hòa trộn).
  - **Tính ổn định:** **Stable (Ổn định)** - Giữ nguyên tuyệt đối thứ tự ban đầu của các khóa bằng nhau khi gộp.

- **Bẫy đề thi trắc nghiệm:**
  - **Bẫy 1:** *"Thuật toán nào sau đây bảo đảm độ phức tạp thời gian $O(n \log n)$ trong trường hợp xấu nhất VÀ là thuật toán sắp xếp ổn định (Stable)?"* $\rightarrow$ Đáp án: **2-Way 합병 정렬 (Merge Sort)**.
  - **Bẫy 2:** *"Nhược điểm lớn nhất của 2-Way Merge Sort so với Quick Sort và Heap Sort là gì?"* $\rightarrow$ Đáp án: Cần thêm không gian bộ nhớ phụ bằng đúng kích thước dữ liệu ban đầu ($O(n)$).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ứng dụng trong Sắp xếp ngoại vi (External Sorting):**
  - Khi dữ liệu vượt quá dung lượng RAM (hàng chục GB hoặc TB):
    - Dữ liệu được chia thành các phần nhỏ vừa khít RAM để nạp vào và sắp xếp nội bộ bằng Quick Sort/Heap Sort, sau đó ghi ra đĩa thành các Run (tệp con đã sắp xếp).
    - Áp dụng kỹ thuật **Multi-way Merge Sort** để đọc tuần tự các Run từ ổ đĩa và hòa trộn thành tệp kết quả cuối cùng mà không bao giờ làm tràn bộ nhớ RAM.

### 복습 체크리스트
- [ ] Nhớ từ khóa cốt lõi: Hợp nhất hai tệp đã sắp xếp thành một tệp (이미 정렬된 두 개의 파일 합병).
- [ ] Ghi nhớ thời gian trong mọi trường hợp (Best, Avg, Worst) đều là $O(n \log n)$.
- [ ] Khẳng định Merge Sort là thuật toán sắp xếp ổn định (Stable).
- [ ] Nhớ nhược điểm không gian bộ nhớ phụ tốn $O(n)$.
