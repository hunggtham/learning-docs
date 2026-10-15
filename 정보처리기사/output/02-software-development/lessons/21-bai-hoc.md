# 084: 퀵 정렬 (Quick Sort)

## 학습 목표 (Mục tiêu)
- Định nghĩa thuật toán Sắp xếp nhanh (퀵 정렬 - Quick Sort) dựa trên mô hình thiết kế giải thuật Chia để trị (분할과 정복 - Divide and Conquer).
- Nắm vững vai trò của phần tử chốt (피벗 - Pivot) trong quá trình phân vùng mảng thành hai nửa: nhỏ hơn chốt sang trái, lớn hơn chốt sang phải.
- Hiểu rõ việc sử dụng cấu trúc dữ liệu Ngăn xếp (Stack) để quản lý các lời gọi hàm đệ quy (Recursion) và nguyên nhân gây thoái hóa hiệu năng xuống $O(n^2)$.

## 핵심 키워드 (Từ khóa)
- 퀵 정렬 (Quick Sort)
- 피벗 (Pivot - 기준값)
- 분할과 정복 (Divide and Conquer)
- 재귀 호출 (Recursive Call) & 스택 (Stack)
- 평균 시간 복잡도 $O(n \log n)$
- 최악의 시간 복잡도 $O(n^2)$
- 불안정 정렬 (Unstable Sort)

## 선행·연결 개념 (Kiến thức liên kết)
- [02-bai-hoc.md](02-bai-hoc.md): 스택 (Stack) và vai trò quản lý bộ nhớ đệ quy (Recursion).
- [15-bai-hoc.md](15-bai-hoc.md): So sánh Quick Sort với Merge Sort và Heap Sort.
- [23-bai-hoc.md](23-bai-hoc.md): 2-Way 합병 정렬 (Merge Sort) - Phương pháp chia để trị bảo đảm tuyệt đối $O(n \log n)$.

## 읽는 방법 (Cách đọc)
- Cứ thấy đề thi nhắc đến các từ khóa: **"피벗 (Pivot)"**, **"분할과 정복 (Divide & Conquer)"**, **"스택(Stack)을 이용한 재귀"** $\rightarrow$ Khẳng định ngay **퀵 정렬 (Quick Sort)**.
- Ghi nhớ con số tương phản: Tốc độ trung bình là số 1 trong các phép so sánh ($n \log n$), nhưng lúc xui xẻo nhất (Worst Case) bị rơi xuống vực thẳm $n^2$.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Cơ chế vận hành của Quick Sort (Hoare đề xuất năm 1960):**
  1. **Chọn Pivot (기준원소):** Chọn một phần tử bất kỳ trong mảng làm chốt (thường chọn phần tử đầu, cuối, hoặc ở giữa).
  2. **Phân vùng (Partitioning):**
     - Sắp xếp lại mảng sao cho tất cả các phần tử nhỏ hơn Pivot được dời sang bên trái của Pivot.
     - Tất cả các phần tử lớn hơn Pivot được dời sang bên phải của Pivot.
     - Lúc này, **Pivot đã nằm chính xác 100% tại vị trí cuối cùng của nó trong mảng đã sắp xếp**.
  3. **Đệ quy (Recursion):** Áp dụng đệ quy lại quy trình trên cho mảng con bên trái và mảng con bên phải một cách độc lập cho đến khi kích thước mảng con bằng 0 hoặc 1.
- **Độ phức tạp thời gian và không gian:**
  - **Thời gian trung bình (Average):** $\mathbf{O(n \log n)}$ (Nhanh nhất trong thực tế nhờ các hằng số ẩn cực nhỏ và khả năng tận dụng Cache bộ nhớ).
  - **Thời gian xấu nhất (Worst Case):** $\mathbf{O(n^2)}$.
    - *Nguyên nhân:* Xảy ra khi mảng đầu vào **đã được sắp xếp tăng dần sẵn hoặc giảm dần sẵn**, đồng thời ta luôn chọn phần tử biên làm Pivot. Khi đó mảng bị chia lệch tối đa thành 1 bên có $0$ phần tử và 1 bên có $n - 1$ phần tử.
  - **Bộ nhớ phụ:** $O(\log n)$ (Dành cho Call Stack quản lý các tầng đệ quy).
  - **Tính ổn định:** **Unstable (Không ổn định)**.

- **Bẫy đề thi trắc nghiệm:**
  - **Bẫy 1:** *"Thuật toán sắp xếp nào cần sử dụng cấu trúc dữ liệu Stack để lưu trữ phạm vi các mảng con trong quá trình đệ quy?"* $\rightarrow$ Đáp án: **퀵 정렬 (Quick Sort)**.
  - **Bẫy 2:** *"Trường hợp nào khiến Quick Sort có hiệu năng tồi tệ nhất $O(n^2)$?"* $\rightarrow$ Đáp án: Dữ liệu đã có thứ tự sẵn (정렬된 자료) hoặc dữ liệu có các phần tử trùng lặp hoàn toàn.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Giải pháp tối ưu hóa ngăn chặn Worst Case trong thực tế:**
  - **Kỹ thuật chọn Pivot trung vị (Median-of-three):** Lấy giá trị trung vị của 3 phần tử (đầu mảng, giữa mảng, cuối mảng) làm Pivot thay vì chọn ngẫu nhiên một đầu.
  - **Dual-pivot Quick Sort:** Thuật toán dùng 2 chốt cùng lúc (được Oracle chọn làm thuật toán sắp xếp mặc định cho các kiểu dữ liệu nguyên thủy trong Java 7+).

### 복습 체크리스트
- [ ] Nhớ mô hình thiết kế: Chia để trị (분할과 정복) xoay quanh phần tử chốt (Pivot).
- [ ] Giải thích tại sao Quick Sort cần dùng đến Stack (quản lý đệ quy).
- [ ] Nhớ độ phức tạp: Trung bình $O(n \log n)$, Xấu nhất thoái hóa xuống $O(n^2)$.
- [ ] Xác định nguyên nhân dẫn tới Worst Case: Dữ liệu đã được sắp xếp sẵn.
