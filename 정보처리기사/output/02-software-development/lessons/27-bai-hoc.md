# 087: 이분 검색 (Binary Search - Tìm kiếm nhị phân)

## 학습 목표 (Mục tiêu)
- Nắm vững quy trình truy vết thuật toán Tìm kiếm nhị phân (이분 검색 - Binary Search) trên các mảng dữ liệu số thực tế.
- Khẳng định điều kiện bắt buộc tiên quyết: Danh sách dữ liệu phải được **sắp xếp theo thứ tự (순서화 / 정렬 - Ordered)**.
- Rèn luyện kỹ năng xác định chính xác số bước so sánh và giá trị của các con trỏ $F$ (First), $L$ (Last), $M$ (Middle) tại từng bước lặp trong đề thi trắc nghiệm.

## 핵심 키워드 (Từ khóa)
- 이분 검색 (Binary Search)
- 순서화된 파일 (Ordered / Sorted File)
- 중간 레코드 (Middle Record)
- 탐색 구간 축소 (Search Interval Reduction)
- $M = (F + L) / 2$
- $O(\log n)$

## 선행·연결 개념 (Kiến thức liên kết)
- [25-bai-hoc.md](25-bai-hoc.md): Lý thuyết tổng quan về Tìm kiếm nhị phân và công thức số lần so sánh tối đa.
- [26-bai-hoc.md](26-bai-hoc.md): So sánh Binary Search với Sequential Search và Hashing.
- [28-bai-hoc.md](28-bai-hoc.md): Các hàm băm (Hashing Functions) - Giải pháp tìm kiếm $O(1)$ không cần sắp xếp.

## 읽는 방법 (Cách đọc)
- Cứ làm bài thi có mảng số:
  - Bước 1: Viết số thứ tự chỉ mục từ $1$ đến $n$ cho từng phần tử.
  - Bước 2: Tính $M = \lfloor (F + L) / 2 \rfloor$.
  - Bước 3: So sánh khóa cần tìm $K$ với $A[M]$ để quyết định điều chỉnh $F = M + 1$ hoặc $L = M - 1$.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Quy tắc vàng của Binary Search:**
  - **전제조건 (Điều kiện tiên quyết):** **반드시 파일이 사전에 정렬(순서화)되어 있어야 한다.** Không thể áp dụng Binary Search trên một danh sách lộn xộn chưa được sắp xếp.
  - **Công thức tính vị trí giữa:**
    $$M = \left\lfloor \frac{F + L}{2} \right\rfloor$$
    *(Với $F$ là chỉ số đầu, $L$ là chỉ số cuối của khoảng đang xét)*
- **Bài toán truy vết mẫu thực chiến:**
  - Cho mảng đã sắp xếp gồm 10 phần tử:
    - Index: `[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10]`
    - Value: `[12, 25, 33, 47, 56, 68, 71, 84, 92, 99]`
  - Yêu cầu: Tìm kiếm phần tử có giá trị **$K = 84$** bằng thuật toán Binary Search.
    - **Bước 1:** Khởi tạo $F = 1, L = 10$.
      - Tính $M = \lfloor (1 + 10) / 2 \rfloor = 5$.
      - So sánh: $A[5] = 56 < 84 \rightarrow$ Khóa nằm ở nửa bên phải.
      - Cập nhật: $F = M + 1 = 5 + 1 = \mathbf{6}$, giữ nguyên $L = 10$.
    - **Bước 2:** Phạm vi xét từ index 6 đến 10.
      - Tính $M = \lfloor (6 + 10) / 2 \rfloor = 8$.
      - So sánh: $A[8] = 84 == 84 \rightarrow$ **Tìm thấy khóa tại vị trí index 8!**
    - **Kết luận:** Thuật toán chỉ mất đúng **2 lần so sánh** để tìm ra kết quả.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Xử lý phép chia lấy nguyên trong các ngôn ngữ lập trình:**
  - Trong thực tế lập trình C/C++/Java, khi $F$ và $L$ là các số nguyên rất lớn (hàng tỷ), biểu thức $(F + L) / 2$ có thể gây ra lỗi tràn số nguyên (Integer Overflow).
  - Biểu thức tối ưu chuẩn mực để tránh lỗi tràn số là:
    $$M = F + \frac{L - F}{2}$$
  - Phép tìm kiếm nhị phân có độ phức tạp thời gian $O(\log_2 n)$, tương đương với việc duyệt từ gốc xuống lá của một cây nhị phân tìm kiếm cân bằng hoàn hảo.

### 복습 체크리스트
- [ ] Khẳng định điều kiện bắt buộc: Tập dữ liệu phải được sắp xếp trước.
- [ ] Tính nhẩm chuẩn xác vị trí giữa $M = \lfloor (F + L) / 2 \rfloor$.
- [ ] Cập nhật đúng biên: $K > A[M] \rightarrow F = M + 1$; $K < A[M] \rightarrow L = M - 1$.
- [ ] Truy vết chính xác số bước so sánh trên một mảng số cho trước trong vòng 1 phút.
