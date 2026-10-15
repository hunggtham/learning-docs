# 081-2: 셸 정렬 (Shell Sort)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và nguyên lý cải tiến của thuật toán Sắp xếp Shell (셸 정렬 - Shell Sort) so với Sắp xếp chèn (Insertion Sort) truyền thống.
- Hiểu rõ cơ chế phân chia mảng thành các nhóm con theo khoảng cách bước nhảy $h$ (매개변수 간격 - Increment / Gap) và thu hẹp dần khoảng cách về 1.
- Ghi nhớ độ phức tạp thời gian trung bình đột phá $O(n^{1.25}) \sim O(n^{1.5})$ và tính chất không ổn định (Unstable) của Shell Sort.

## 핵심 키워드 (Từ khóa)
- 셸 정렬 (Shell Sort)
- 삽입 정렬 보완 / 확장 (Extension of Insertion Sort)
- 매개변수 간격 $h$ (Gap / Increment)
- 서브파일 분할 (Subarray grouping)
- 시간 복잡도: 평균 $O(n^{1.5})$, 최악 $O(n^2)$
- 불안정 정렬 (Unstable Sort)

## 선행·연결 개념 (Kiến thức liên kết)
- [17-bai-hoc.md](17-bai-hoc.md): 삽입 정렬 (Insertion Sort) - Thuật toán nền tảng của Shell Sort.
- [19-bai-hoc.md](19-bai-hoc.md): 선택 정렬 (Selection Sort) - Thuật toán tìm giá trị nhỏ nhất để đổi chỗ.
- [21-bai-hoc.md](21-bai-hoc.md): 퀵 정렬 (Quick Sort) - Thuật toán chia để trị hiệu năng cao.

## 읽는 방법 (Cách đọc)
- Đi thi trắc nghiệm hễ thấy câu hỏi có từ khóa **"삽입 정렬을 보완"** (Cải tiến từ Insertion Sort) hoặc **"매개변수 간격 $h$"** (Sắp xếp theo khoảng cách bước nhảy $h$) $\rightarrow$ Chọn ngay **셸 정렬 (Shell Sort)**.
- Nhớ hình ảnh chiếc vỏ ốc (Shell): Khoảng cách nhảy ban đầu rất rộng, sau mỗi vòng co hẹp dần, đến vòng cuối cùng khoảng cách bằng 1 (lúc này mảng đã gần như có thứ tự nên chạy cực nhanh).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Lý do ra đời và Nguyên lý của Shell Sort:**
  - **Nhược điểm của Insertion Sort:** Nếu một phần tử rất nhỏ nằm ở tận cuối mảng, ta phải dịch chuyển từng ô một qua toàn bộ mảng để đưa nó về đầu $\rightarrow$ Rất tốn kém thời gian.
  - **Giải pháp của Shell Sort:**
    - Do Donald Shell đề xuất năm 1959.
    - Chọn một chuỗi khoảng cách bước nhảy $h$ (ví dụ: $h = 5, 3, 1$).
    - Gom các phần tử cách nhau khoảng cách $h$ thành từng nhóm con (Subfiles) độc lập.
    - Áp dụng Insertion Sort trên từng nhóm con đó để các phần tử nhỏ có thể "nhảy bước dài" về phía đầu mảng.
    - Giảm dần khoảng cách $h$ cho đến khi $h = 1$ (ở bước $h = 1$, toàn bộ mảng được sắp xếp chèn một lần cuối, nhưng lúc này mảng đã rất ngăn nắp nên thời gian chạy tiệm cận $O(n)$).
- **Độ phức tạp thời gian và không gian:**
  - **Thời gian trung bình:** $\mathbf{O(n^{1.25}) \sim O(n^{1.5})}$ (Vượt trội hơn hẳn so với mức $O(n^2)$ của Insertion Sort thông thường).
  - **Thời gian xấu nhất:** $\mathbf{O(n^2)}$.
  - **Bộ nhớ phụ:** $O(1)$ (Sắp xếp tại chỗ In-place).
  - **Tính ổn định:** **Unstable (Không ổn định)** - Do việc nhảy bước xa có thể làm xáo trộn vị trí của các phần tử có cùng giá trị.

- **Bẫy đề thi trắc nghiệm:**
  - **Bẫy 1:** *"Thuật toán nào sau đây chia mảng thành các phần tử cách nhau một khoảng cách xác định $h$ để sắp xếp?"* $\rightarrow$ Đáp án: **셸 정렬 (Shell Sort)**.
  - **Bẫy 2:** *"Độ phức tạp trung bình của Shell Sort là bao nhiêu?"* $\rightarrow$ Khoanh đáp án có dạng **$O(n^{1.5})$** hoặc **$O(n^{1.25})$**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ minh họa bước nhảy khoảng cách:**
  - Cho mảng 8 phần tử: $[80, 30, 60, 40, 20, 10, 50, 70]$
  - Chọn bước nhảy đầu tiên $h = 4$:
    - Nhóm 1: Các phần tử ở vị trí 1 và 5 ($80$ và $20$) $\rightarrow$ Đổi thành $[20, 80]$.
    - Nhóm 2: Các phần tử ở vị trí 2 và 6 ($30$ và $10$) $\rightarrow$ Đổi thành $[10, 30]$.
    - Nhóm 3: Các phần tử ở vị trí 3 và 7 ($60$ và $50$) $\rightarrow$ Đổi thành $[50, 60]$.
    - Nhóm 4: Các phần tử ở vị trí 4 và 8 ($40$ và $70$) $\rightarrow$ Giữ nguyên $[40, 70]$.
  - Sau bước nhảy $h = 4$: Các số nhỏ như `10`, `20` đã bay vèo từ nửa sau về nửa đầu mảng chỉ trong 1 thao tác.

### 복습 체크리스트
- [ ] Khẳng định Shell Sort là thuật toán nâng cấp mở rộng của Insertion Sort.
- [ ] Nhớ từ khóa then chốt: 매개변수 간격 $h$ (Bước nhảy khoảng cách).
- [ ] Ghi nhớ độ phức tạp trung bình $O(n^{1.5})$, nhanh hơn $O(n^2)$.
- [ ] Xác nhận Shell Sort là thuật toán sắp xếp không ổn định (Unstable).
