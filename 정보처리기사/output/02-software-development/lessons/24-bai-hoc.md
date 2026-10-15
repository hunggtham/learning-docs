# 086-1: 기수 정렬 (Radix Sort / Bucket Sort)

## 학습 목표 (Mục tiêu)
- Định nghĩa thuật toán Sắp xếp theo cơ số (기수 정렬 - Radix Sort / Bucket Sort) và hiểu rõ nguyên lý đột phá: **Hoàn toàn không sử dụng phép so sánh trực tiếp giữa các khóa dữ liệu**.
- Nắm vững việc sử dụng các thùng chứa Hàng đợi (큐 - Queue / 버킷 - Bucket) để phân loại dữ liệu theo từng hàng chữ số (Digit) từ thấp đến cao (LSD) hoặc từ cao xuống thấp (MSD).
- Ghi nhớ độ phức tạp thời gian tuyến tính $O(d \cdot n)$ vượt qua giới hạn lý thuyết $O(n \log n)$ của các thuật toán so sánh, cùng đặc tính sắp xếp ổn định (Stable Sort).

## 핵심 키워드 (Từ khóa)
- 기수 정렬 (Radix Sort)
- 버킷 정렬 (Bucket Sort)
- 비교 연산 미수행 (No Comparison)
- 큐 (Queue / FIFO)
- 자릿수 (Digit / Radix)
- LSD (Least Significant Digit) & MSD (Most Significant Digit)
- 시간 복잡도 $O(d \cdot n)$
- 안정 정렬 (Stable Sort)

## 선행·연결 개념 (Kiến thức liên kết)
- [04-bai-hoc.md](04-bai-hoc.md): Cấu trúc dữ liệu Hàng đợi (큐 - Queue) vận hành các Bucket trong Radix Sort.
- [16-bai-hoc.md](16-bai-hoc.md): Ma trận tổng hợp phân loại thuật toán sắp xếp (Radix thuộc nhóm Stable).
- [23-bai-hoc.md](23-bai-hoc.md): 2-Way 합병 정렬 (Merge Sort) - So sánh các thuật toán Stable.

## 읽는 방법 (Cách đọc)
- Cứ thấy đề thi có từ khóa: **"데이터를 비교하지 않음"** (Không so sánh dữ liệu) hoặc **"큐(Queue)나 버킷(Bucket)을 이용"** hoặc **"자릿수(Digit)별로 정렬"** $\rightarrow$ Khẳng định ngay **기수 정렬 (Radix Sort)**.
- Ghi nhớ công thức thời gian siêu tốc: **$O(d \cdot n)$** (với $d$ là số chữ số tối đa, $n$ là số phần tử).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Cơ chế vận hành của Radix Sort:**
  - Không hề dùng các toán tử so sánh lớn hơn (`>`), nhỏ hơn (`<`) giữa hai số.
  - Chuẩn bị sẵn 10 cấu trúc Hàng đợi (Queue), đánh số từ `0` đến `9` tương ứng với cơ số 10 (Radix = 10).
  - **Phương pháp LSD (Least Significant Digit - Phổ biến nhất):**
    1. **Vòng 1 (Hàng đơn vị):** Quét từng số trong mảng, nhìn vào chữ số hàng đơn vị và đẩy (`Enqueue`) số đó vào Queue tương ứng (0~9). Sau đó rút lần lượt (`Dequeue`) từ Queue 0 đến 9 nối lại thành mảng.
    2. **Vòng 2 (Hàng chục):** Lấy mảng vừa thu được, nhìn vào chữ số hàng chục và phân loại lại vào các Queue 0~9. Dequeue ra nối lại.
    3. **Vòng $d$ (Hàng cao nhất):** Lặp lại quy trình trên cho đến chữ số có trọng số lớn nhất. Sau $d$ vòng, toàn bộ mảng được sắp xếp tăng dần hoàn hảo!
- **Độ phức tạp thời gian và không gian:**
  - **Thời gian trong mọi trường hợp (Best, Avg, Worst):** Luôn là $\mathbf{O(d \cdot n)}$ (với $n$ là số lượng phần tử, $d$ là độ dài chữ số lớn nhất).
    - Nếu $d$ là một hằng số nhỏ cố định, độ phức tạp đạt tiệm cận tuyến tính $\mathbf{O(n)}$, nhanh hơn cả Quick Sort và Merge Sort.
  - **Bộ nhớ phụ:** Cần thêm bộ nhớ cho các hàng đợi Bucket $O(n + k)$ (với $k$ là cơ số hệ đếm).
  - **Tính ổn định:** **Stable (Ổn định)** - Nhờ tính chất FIFO (Vào trước ra trước) của Queue giữ nguyên thứ tự của các số có cùng chữ số.

- **Ví dụ minh họa sắp xếp số `[170, 045, 075, 090, 002]`:**
  - *Vòng 1 (Hàng đơn vị):*
    - Đơn vị là 0: `170`, `090` (Queue 0)
    - Đơn vị là 2: `002` (Queue 2)
    - Đơn vị là 5: `045`, `075` (Queue 5)
    - Rút ra: `[170, 090, 002, 045, 075]`
  - *Vòng 2 (Hàng chục):* Phân loại theo 7, 9, 0, 4, 7 $\rightarrow$ Rút ra: `[002, 045, 170, 075, 090]`
  - *Vòng 3 (Hàng trăm):* Phân loại theo 0, 0, 1, 0, 0 $\rightarrow$ Rút ra: `[002, 045, 075, 090, 170]`. Hoàn tất!

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Hạn chế thực tế của Radix Sort:**
  - Chỉ áp dụng được khi dữ liệu có thể biểu diễn dưới dạng các chữ số hoặc chuỗi ký tự có độ dài hữu hạn (như số nguyên, mã bưu điện, chuỗi ký tự cố định).
  - Không thể áp dụng trực tiếp cho các kiểu dữ liệu số thực dấu phẩy động (Floating point) hoặc các đối tượng dữ liệu phức hợp không có cơ số cố định.

### 복습 체크리스트
- [ ] Ghi nhớ đặc điểm độc nhất: Hoàn toàn không dùng phép so sánh trực tiếp.
- [ ] Nhớ cấu trúc dữ liệu bổ trợ: Dùng Hàng đợi (Queue) làm Bucket.
- [ ] Nhớ công thức thời gian: $O(d \cdot n)$ với $d$ là số chữ số.
- [ ] Khẳng định Radix Sort là thuật toán sắp xếp ổn định (Stable).
