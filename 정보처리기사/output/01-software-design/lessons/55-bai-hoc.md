# 12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)

## 학습 목표 (Mục tiêu)
- Phân biệt bản chất giữa Sắp xếp nội bộ (`내부 정렬` - trong bộ nhớ RAM) và Sắp xếp ngoại vi (`외부 정렬` - trên đĩa cứng/băng từ bằng kỹ thuật Merge Sort).
- Thuộc nằm lòng cơ chế hoạt động và Độ phức tạp thời gian (`시간 복잡도`) của các thuật toán sắp xếp kinh điển: `삽입`, `선택`, `버블`, `퀵`, `힙`, `병합`, và `기수` 정렬.
- Nhận diện trường hợp xấu nhất $O(N^2)$ của thuật toán Quick Sort và tính ổn định (`안정성 - Stability`) của từng thuật toán.

## 핵심 키워드 (Từ khóa)
- 내부 정렬 vs 외부 정렬 (Internal Sort vs External Sort)
- 삽입 정렬 (Insertion Sort / $O(N^2)$)
- 선택 정렬 (Selection Sort / 항상 $O(N^2)$)
- 버블 정렬 (Bubble Sort / 인접 요소 교환)
- 퀵 정렬 (Quick Sort / Pivot / 평균 $O(N \log N)$, 최악 $O(N^2)$)
- 힙 정렬 (Heap Sort / 완전 이진 트리 / 항상 $O(N \log N)$)
- 병합 정렬 (Merge Sort / 2-Way Merge / 분할 정복 / $O(N \log N)$)
- 정렬 안정성 (Stable Sort vs Unstable Sort)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([11. 수식의 표기법 (Expression Notation)](54-bai-hoc.md)):** Sau khi xem xét biểu diễn biểu thức và Stack, bài này tập trung vào các giải thuật sắp xếp dữ liệu - một chủ đề cốt lõi của khoa học máy tính.
- **Tiếp nối sang bài sau ([13. 검색 및 해싱 (Search & Hashing)](56-bai-hoc.md)):** Khảo sát các giải thuật tìm kiếm dữ liệu (Tìm kiếm tuần tự, Tìm kiếm nhị phân) và kỹ thuật bảng băm Hashing.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc bảng ma trận thời gian: Nhóm $O(N^2)$ gồm Chèn, Chọn, Nổi bọt; Nhóm $O(N \log N)$ gồm Quick (trung bình), Heap (luôn luôn), Merge (luôn luôn); Quick Sort xấu nhất rơi vào $O(N^2)$.
- Đọc TẦNG B để theo dõi bài toán mẫu tính số lượt so sánh trong từng vòng lặp (Pass) của Bubble Sort và Selection Sort.

---

## 12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Phân loại tổng quát:**
  - `내부 정렬 (Internal Sort - Sắp xếp nội bộ)`: Toàn bộ dữ liệu cần sắp xếp được nạp trọn vẹn vào bộ nhớ trong (RAM); tốc độ xử lý nhanh.
  - `외부 정렬 (External Sort - Sắp xếp ngoại vi)`: Dữ liệu có dung lượng khổng lồ vượt quá giới hạn bộ nhớ RAM, phải lưu trữ trên bộ nhớ ngoài (Đĩa từ, Băng từ); sử dụng phương pháp **Trộn 2 đường hoặc đa đường (`2-Way / K-Way Merge Sort`)** để chia nhỏ và sắp xếp từng phần.
- **2. Bảng ma trận độ phức tạp thời gian các thuật toán sắp xếp nội bộ:**
  | Thuật toán sắp xếp | Cơ chế hoạt động cốt lõi | Tốt nhất (Best) | Trung bình (Avg) | Xấu nhất (Worst) | Tính ổn định (Stability) |
  |---|---|---|---|---|---|
  | **삽입 정렬 (Insertion)** | Chèn phần tử vào vị trí thích hợp trong dãy đã xếp | $O(N)$ | $O(N^2)$ | $O(N^2)$ | **Stable (안정)** |
  | **선택 정렬 (Selection)** | Tìm phần tử nhỏ nhất đưa về đầu dãy | $O(N^2)$ | $O(N^2)$ | $O(N^2)$ | Unstable (불안정) |
  | **버블 정렬 (Bubble)** | So sánh và đổi chỗ 2 phần tử kề cận liên tục | $O(N)$ | $O(N^2)$ | $O(N^2)$ | **Stable (안정)** |
  | **퀵 정렬 (Quick)** | Chia để trị dựa trên phần tử chốt (Pivot) | $O(N \log N)$ | $\mathbf{O(N \log N)}$ | $\mathbf{O(N^2)}$ | Unstable (불안정) |
  | **힙 정렬 (Heap)** | Sử dụng cấu trúc cây Complete Binary Heap | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | Unstable (불안정) |
  | **병합 정렬 (Merge)** | Chia đôi dãy, xếp đệ quy rồi trộn (2-Way Merge) | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | **Stable (안정)** |
  | **기수 정렬 (Radix)** | So sánh lần lượt từng chữ số (không cần so sánh khóa) | $O(d \cdot N)$ | $O(d \cdot N)$ | $O(d \cdot N)$ | **Stable (안정)** |
- **Đặc điểm trọng tâm các thuật toán hay thi:**
  - **퀵 정렬 (Quick Sort):** Là thuật toán sắp xếp nội bộ có **tốc độ trung bình nhanh nhất trong thực tế (`평균 수행 속도가 가장 빠름`)**. Tuy nhiên, khi mảng đã được sắp xếp sẵn (tăng dần hoặc giảm dần) mà chọn trúng phần tử đầu/cuối làm Pivot thì hiệu năng bị thoái hóa rơi xuống **trường hợp xấu nhất là $O(N^2)$**.
  - **힙 정렬 (Heap Sort):** Tận dụng cây nhị phân hoàn chỉnh (Complete Binary Tree), đảm bảo thời gian chạy luôn là $O(N \log N)$ trong mọi tình huống xấu nhất.
  - **병합 정렬 (Merge Sort):** Luôn đảm bảo $O(N \log N)$ và có tính ổn định (Stable), là thuật toán nền tảng của Sắp xếp ngoại vi (External Sort), nhưng nhược điểm là tốn thêm mảng phụ dung lượng $O(N)$.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Thuật toán Quick Sort luôn chạy với thời gian $O(N \log N)$ trong mọi trường hợp?"* -> **Sai**. Trong trường hợp xấu nhất (Worst case), Quick Sort tốn **$O(N^2)$**.
  - **Bẫy 2:** *"Sắp xếp ngoại vi (External Sort) sử dụng phương pháp nào chủ đạo?"* -> **병합 (Merge Sort / 2-Way Merge)**.
  - **Bẫy 3:** *"Thuật toán nào sau đây không có tính ổn định (Unstable)?"* -> Nhớ nhóm không ổn định gồm: **Quick, Selection, Heap, Shell**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Nội bộ trong RAM, Ngoại vi đĩa cứng dùng Merge; Quick trung bình nhanh nhất xấu nhất $N^2$; Heap và Merge luôn $N \log N$; Chèn, Nổi bọt, Merge giữ tính ổn định".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa 1 vòng lặp (Pass 1) của Bubble Sort:**
  - Cho mảng: `[8, 5, 2, 6, 3]`
  - So sánh cặp 1: $8 > 5 \rightarrow$ Đổi chỗ: `[5, 8, 2, 6, 3]`
  - So sánh cặp 2: $8 > 2 \rightarrow$ Đổi chỗ: `[5, 2, 8, 6, 3]`
  - So sánh cặp 3: $8 > 6 \rightarrow$ Đổi chỗ: `[5, 2, 6, 8, 3]`
  - So sánh cặp 4: $8 > 3 \rightarrow$ Đổi chỗ: `[5, 2, 6, 3, 8]`
  - $\Longrightarrow$ Kết thúc Pass 1: Phần tử lớn nhất ($8$) đã "nổi bọt" chìm xuống vị trí cuối cùng của mảng.

### 복습 체크리스트
- [ ] Phân biệt được 내부 정렬 (trong RAM) và 외부 정렬 (dùng đĩa, kỹ thuật Merge).
- [ ] Nhớ độ phức tạp trung bình và xấu nhất của Quick Sort ($O(N \log N)$ vs $O(N^2)$).
- [ ] Kể tên 2 thuật toán luôn đảm bảo $O(N \log N)$ trong mọi trường hợp: Heap Sort và Merge Sort.
- [ ] Phân biệt được thuật toán Stable (Bubble, Insertion, Merge) và Unstable (Quick, Selection, Heap).
