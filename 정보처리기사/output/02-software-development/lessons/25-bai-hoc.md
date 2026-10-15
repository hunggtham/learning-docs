# 7. 이분 검색 (Binary Search)

## 학습 목표 (Mục tiêu)
- Định nghĩa thuật toán Tìm kiếm nhị phân (이분 검색 - Binary Search) và điều kiện tiên quyết bắt buộc: **Tập dữ liệu phải được sắp xếp có thứ tự từ trước (정렬된 데이터)**.
- Nắm vững công thức tính chỉ số phần tử đứng giữa (Middle Index: $M = \lfloor (F + L) / 2 \rfloor$) và cơ chế thu hẹp không gian tìm kiếm đi một nửa sau mỗi lần so sánh.
- Thuộc nằm lòng độ phức tạp thời gian $O(\log n)$ và công thức tính số lần so sánh tối đa $\lfloor \log_2 n \rfloor + 1$ cho một tập dữ liệu kích thước $n$.

## 핵심 키워드 (Từ khóa)
- 이분 검색 / 이진 탐색 (Binary Search)
- 정렬된 데이터 전제조건 (Sorted Data Prerequisite)
- 중간 레코드 (Middle Record: $M = (F + L) / 2$)
- 탐색 범위 반감 (Halving search space)
- 시간 복잡도 $O(\log n)$
- 최대 비교 횟수 ($\lfloor \log_2 n \rfloor + 1$)

## 선행·연결 개념 (Kiến thức liên kết)
- [16-bai-hoc.md](16-bai-hoc.md): Các thuật toán sắp xếp (tiền đề tạo mảng có thứ tự cho Binary Search).
- [26-bai-hoc.md](26-bai-hoc.md): So sánh Tìm kiếm tuần tự (Sequential) vs Tìm kiếm nhị phân (Binary) vs Băm (Hashing).
- [27-bai-hoc.md](27-bai-hoc.md): Phân tích chi tiết các bài toán truy vết chỉ số và số bước tìm kiếm nhị phân.

## 읽는 방법 (Cách đọc)
- Cứ thấy đề thi hỏi: **"이분 검색(Binary Search)을 적용하기 위한 필수 전제 조건은?"** (Điều kiện tiên quyết để áp dụng tìm kiếm nhị phân) $\rightarrow$ Khoanh ngay đáp án: **자료가 미리 정렬되어 있어야 한다** (Dữ liệu bắt buộc phải được sắp xếp sẵn).
- Khi tính số lần so sánh: Mỗi lần so sánh loại bỏ 50% số phần tử còn lại $\rightarrow$ Tốc độ tìm kiếm cực kỳ vượt trội ($1.000$ phần tử chỉ cần tối đa $10$ lần so sánh, $1.000.000$ phần tử chỉ cần tối đa $20$ lần so sánh).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Cơ chế hoạt động của Binary Search:**
  - **Điều kiện tiên quyết:** Dãy dữ liệu $A[1 \dots n]$ đã được sắp xếp tăng dần.
  - Khởi tạo hai con trỏ biên: Con trỏ đầu $\text{First } (F) = 1$, con trỏ cuối $\text{Last } (L) = n$.
  - Trong khi $F \le L$:
    1. Tính chỉ số phần tử ở giữa:
       $$M = \left\lfloor \frac{F + L}{2} \right\rfloor$$
    2. So sánh giá trị cần tìm ($K$) với giá trị tại vị trí giữa ($A[M]$):
       - Nếu $K == A[M]$: **Tìm thấy thành công!** Trả về vị trí $M$.
       - Nếu $K < A[M]$: Giá trị cần tìm nằm ở nửa bên trái $\rightarrow$ Thu hẹp phạm vi: $L = M - 1$.
       - Nếu $K > A[M]$: Giá trị cần tìm nằm ở nửa bên phải $\rightarrow$ Thu hẹp phạm vi: $F = M + 1$.
    3. Nếu $F > L$: Tập dữ liệu không chứa khóa $K$ (Tìm kiếm thất bại).
- **Độ phức tạp thời gian và Số lần so sánh tối đa:**
  - **Thời gian tốt nhất (Best Case):** $O(1)$ (Khi phần tử cần tìm nằm ngay đúng vị trí giữa $M$ ở lần thử đầu tiên).
  - **Thời gian trung bình và xấu nhất (Average & Worst):** $\mathbf{O(\log n)}$.
  - **Công thức tính số lần so sánh tối đa trong trường hợp xấu nhất:**
    $$\text{Max Comparisons} = \lfloor \log_2 n \rfloor + 1$$
    - *Ví dụ 1:* Với $n = 15$ phần tử: $\lfloor \log_2 15 \rfloor + 1 = 3 + 1 = \mathbf{4}$ lần so sánh tối đa.
    - *Ví dụ 2:* Với $n = 100$ phần tử: $\lfloor \log_2 100 \rfloor + 1 = 6 + 1 = \mathbf{7}$ lần so sánh tối đa.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh trực quan Sequential Search vs Binary Search:**
  - Với danh sách 1 triệu bản ghi ($n = 1.000.000$):
    - **순차 검색 (Sequential Search):** Nếu phần tử nằm ở cuối hoặc không tồn tại, phải duyệt qua đủ $1.000.000$ lần so sánh.
    - **이분 검색 (Binary Search):** Chỉ cần tối đa $\lfloor \log_2 1.000.000 \rfloor + 1 = 19 + 1 = \mathbf{20}$ lần so sánh! Tiết kiệm hơn $50.000$ lần thời gian tính toán của CPU.

### 복습 체크리스트
- [ ] Nhớ điều kiện tiên quyết duy nhất: Dữ liệu bắt buộc phải được sắp xếp trước.
- [ ] Tính đúng chỉ số giữa: $M = \lfloor (F + L) / 2 \rfloor$.
- [ ] Ghi nhớ thời gian trung bình và xấu nhất là $O(\log n)$.
- [ ] Áp dụng chuẩn xác công thức số lần so sánh tối đa $\lfloor \log_2 n \rfloor + 1$.
