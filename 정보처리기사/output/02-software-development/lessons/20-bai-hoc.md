# 083: 버블 정렬 (Bubble Sort)

## 학습 목표 (Mục tiêu)
- Định nghĩa chính xác thuật toán Sắp xếp nổi bọt (버블 정렬 - Bubble Sort) dựa trên cơ chế so sánh liên tiếp các cặp phần tử kề nhau (Adjacent pairs).
- Nắm vững đặc điểm sau mỗi vòng lặp (Pass): Phần tử có giá trị lớn nhất sẽ "nổi bọt" và chốt cố định ở vị trí cuối cùng của mảng.
- Hiểu rõ kỹ thuật tối ưu hóa bằng cờ hiệu (플래그 비트 - Flag Bit) giúp thuật toán kết thúc sớm khi mảng đã có thứ tự hoàn hảo, đạt hiệu năng tốt nhất $O(n)$.

## 핵심 키워드 (Từ khóa)
- 버블 정렬 (Bubble Sort)
- 인접한 두 레코드 비교 (Compare adjacent elements)
- 위치 교환 (Swap)
- 플래그 비트 (Flag Bit)
- 조기 종료 조건 (Early termination)
- 시간 복잡도: 최선 $O(n)$, 평균/최악 $O(n^2)$
- 안정 정렬 (Stable Sort)

## 선행·연결 개념 (Kiến thức liên kết)
- [14-bai-hoc.md](14-bai-hoc.md): So sánh tổng quan Bubble, Selection, Insertion Sort.
- [19-bai-hoc.md](19-bai-hoc.md): 선택 정렬 (Selection Sort) - Đưa số nhỏ nhất lên đầu.
- [21-bai-hoc.md](21-bai-hoc.md): 퀵 정렬 (Quick Sort) - Phiên bản nâng cấp nhảy vọt chia để trị.

## 읽는 방법 (Cách đọc)
- Nhận diện đề thi bằng từ khóa: **"인접한 두 개의 레코드 키 값을 비교"** (So sánh giá trị khóa của 2 bản ghi liền kề nhau) $\rightarrow$ Khẳng định ngay **버블 정렬 (Bubble Sort)**.
- Khi truy vết đề thi: Vòng 1 chốt số lớn nhất ở cuối mảng, vòng 2 chốt số lớn nhì ở vị trí áp chót.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Cơ chế hoạt động của Bubble Sort:**
  - Quét từ đầu đến cuối mảng, xét từng cặp hai phần tử đứng cạnh nhau ($A[j]$ và $A[j+1]$):
    - Nếu $A[j] > A[j+1]$: Tiến hành hoán đổi vị trí (Swap) giữa hai phần tử.
    - Tiếp tục dịch sang cặp kế tiếp.
  - Sau vòng 1 (1회전): Phần tử có giá trị **lớn nhất toàn mảng** đã bị đẩy xuống vị trí cuối cùng ($A[n]$).
  - Vòng 2 (2회전): Chỉ cần duyệt đến vị trí $n - 1$, phần tử lớn thứ nhì sẽ chốt ở vị trí áp chót.
  - Tổng số vòng lặp tối đa là **$n - 1$ vòng**.
- **Kỹ thuật tối ưu hóa Flag Bit (Cờ hiệu dừng sớm):**
  - Khởi tạo biến `flag = false` trước mỗi vòng lặp.
  - Nếu có bất kỳ phép hoán đổi nào xảy ra trong vòng lặp đó $\rightarrow$ Đặt `flag = true`.
  - Kết thúc vòng, nếu `flag` vẫn là `false` (nghĩa là không có cặp nào bị ngược chiều) $\rightarrow$ **Dừng thuật toán ngay lập tức**.
- **Độ phức tạp thời gian:**
  - **Tốt nhất (Best Case):** $\mathbf{O(n)}$ (khi mảng đã được sắp xếp sẵn và áp dụng cờ Flag Bit).
  - **Trung bình (Average):** $\mathbf{O(n^2)}$.
  - **Xấu nhất (Worst Case):** $\mathbf{O(n^2)}$ (khi mảng xếp ngược chiều hoàn toàn).
  - **Tính ổn định:** **Stable (Ổn định)**.

- **Ví dụ truy vết mảng `[7, 3, 5, 2, 8]`:**
  - Ban đầu: `[7, 3, 5, 2, 8]`
  - **1회전 (Vòng 1):**
    - So sánh (7, 3) $\rightarrow$ đổi chỗ: `[3, 7, 5, 2, 8]`
    - So sánh (7, 5) $\rightarrow$ đổi chỗ: `[3, 5, 7, 2, 8]`
    - So sánh (7, 2) $\rightarrow$ đổi chỗ: `[3, 5, 2, 7, 8]`
    - So sánh (7, 8) $\rightarrow$ giữ nguyên: `[3, 5, 2, 7, 8]`
    - **Kết thúc vòng 1:** `[3, 5, 2, 7, 8]` *(Số 8 lớn nhất chốt ở cuối)*.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh số phép hoán đổi giữa Bubble Sort và Selection Sort:**
  - Dù cả hai cùng có độ phức tạp thời gian $O(n^2)$, nhưng **Bubble Sort tốn rất nhiều thao tác hoán đổi ghi bộ nhớ (Swap)** trong từng vòng (lên đến $O(n^2)$ lần swap). Trong khi đó Selection Sort chỉ thực hiện tối đa 1 lần swap cho mỗi vòng ($O(n)$ lần swap).

### 복습 체크리스트
- [ ] Nhớ từ khóa cốt lõi: So sánh 2 phần tử kề nhau và hoán đổi vị trí.
- [ ] Nhớ hiện tượng: Phần tử lớn nhất chốt ở vị trí cuối cùng sau vòng 1.
- [ ] Hiểu vai trò của cờ hiệu 플래그 비트 (Flag Bit) giúp dừng sớm đạt thời gian $O(n)$.
- [ ] Khẳng định Bubble Sort là thuật toán sắp xếp ổn định (Stable).
