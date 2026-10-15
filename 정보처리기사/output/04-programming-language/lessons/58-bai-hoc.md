# 195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm pha cài đặt (구현 / Coding) và triết lý cốt lõi của phương pháp lập trình có cấu trúc (구조적 프로그래밍 - Structured Programming do Edsger Dijkstra đề xuất).
- Hiểu cấu trúc đồ thị dòng điều khiển (제어 흐름도 - Control Flow Graph / CFG) với các khái niệm Node, Edge, và Predicate Node.
- Thuộc lòng và vận dụng thành thạo công thức tính độ phức tạp chu trình McCabe (순환 복잡도 - Cyclomatic Complexity) để xác định số lượng đường dẫn thực thi độc lập (Basis Paths) cần thiết trong kiểm thử.

## 핵심 키워드 (Từ khóa)
- 구조적 프로그래밍 (Structured Programming - Dijkstra)
- 3대 기본 구조 (순차, 선택, 반복 / Sequence, Selection, Iteration)
- 제어 흐름도 (Control Flow Graph - CFG)
- 순환 복잡도 (Cyclomatic Complexity - McCabe Metric)
- $V(G) = E - N + 2$
- $V(G) = P + 1$ (Predicate Node)
- 닫힌 영역의 수 + 1 (Regions)
- 기본 경로 테스트 (Basis Path Testing)

## 선행·연결 개념 (Kiến thức liên kết)
- [57-bai-hoc.md](57-bai-hoc.md): Thiết kế module hóa hiệu quả và biểu đồ N-S.
- [59-bai-hoc.md](59-bai-hoc.md): Kiểm thử hộp trắng (White Box Testing) và kỹ thuật kiểm thử đường dẫn cơ bản.
- [60-bai-hoc.md](60-bai-hoc.md): Kiểm thử hộp đen (Black Box Testing).

## 읽는 방법 (Cách đọc)
- Trong phần thi tính toán của môn 4, bài toán tính độ phức tạp McCabe xuất hiện với tần suất cực kỳ cao:
  - Hãy nhớ kỹ 3 cách tính tương đương:
    1. Theo Cạnh và Node: $V(G) = E - N + 2$ ($E$: số cạnh/mũi tên, $N$: số nút).
    2. Theo nút điều kiện rẽ nhánh: $V(G) = P + 1$ ($P$: số nút có $\ge 2$ mũi tên đi ra).
    3. Theo số miền đóng: $V(G) = R$ ($R$ là tổng số vùng khép kín cộng thêm 1 vùng mở bên ngoài).
  - Giá trị $V(G)$ chính là **số lượng ca kiểm thử (Test Cases) tối thiểu** cần chuẩn bị để bao phủ toàn bộ các đường chạy độc lập của hàm.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Triết lý lập trình có cấu trúc (Structured Programming):**
  - Do nhà khoa học máy tính Edsger W. Dijkstra đề xướng nhằm giải quyết cuộc khủng hoảng phần mềm (Software Crisis).
  - Chỉ cho phép sử dụng duy nhất **3 cấu trúc điều khiển chuẩn mực**:
    1. **순차 (Sequence):** Thực thi lệnh tuần tự từ trên xuống dưới.
    2. **선택 (Selection):** Rẽ nhánh theo điều kiện (`if-else`, `switch-case`).
    3. **반복 (Iteration):** Lặp khối lệnh theo điều kiện (`for`, `while`, `do-while`).
  - **Cấm hoàn toàn việc sử dụng lệnh nhảy tùy tiện `GOTO`** để tránh tạo ra mã nguồn mạng nhện (Spaghetti Code).

- **2. Các công thức tính độ phức tạp chu trình McCabe (순환 복잡도):**

$$\mathbf{V(G) = E - N + 2}$$
$$\mathbf{V(G) = P + 1}$$
$$\mathbf{V(G) = \text{Số vùng khép kín (Closed Regions)} + 1}$$

| Ký hiệu | Ý nghĩa trong đồ thị dòng điều khiển (CFG) |
| :--- | :--- |
| **$E$ (Edges)** | Tổng số cung / mũi tên chuyển luồng thực thi giữa các nút. |
| **$N$ (Nodes)** | Tổng số nút biểu diễn các khối lệnh hoặc điểm giao tiếp luồng. |
| **$P$ (Predicate Nodes)** | Số lượng nút điều kiện (nút có từ 2 mũi tên rẽ nhánh đi ra, ví dụ điểm kiểm tra `if` hoặc `while`). |
| **$V(G)$** | Độ phức tạp Cyclomatic (tương đương số đường đi độc lập tuyến tính). |

- **Bài toán ví dụ điển hình trong đề thi:**
  - *Đề bài:* Cho một đoạn chương trình có đồ thị luồng gồm $N = 6$ nút và $E = 8$ cạnh. Tính độ phức tạp chu trình McCabe?
  - *Giải:* Áp dụng công thức:
    $$V(G) = E - N + 2 = 8 - 6 + 2 = 4$$
  - *Ý nghĩa kết quả:* Lập trình viên cần thiết kế ít nhất **4 test case** độc lập để kiểm thử phủ hết mọi nhánh thực thi của thuật toán.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ngưỡng kiểm soát chất lượng phần mềm theo McCabe:**
  - $V(G) \le 10$: Chương trình có cấu trúc đơn giản, trong sáng, nguy cơ lỗi rất thấp, dễ bảo trì.
  - $11 \le V(G) \le 20$: Độ phức tạp trung bình, cần chú ý kiểm thử kỹ lưỡng.
  - $21 \le V(G) \le 50$: Cấu trúc phức tạp cao, khó hiểu, tiềm ẩn nhiều lỗi ngầm.
  - $V(G) > 50$: Cực kỳ nguy hiểm, không thể kiểm thử đầy đủ, bắt buộc phải tái cấu trúc (Refactoring) chia nhỏ hàm thành các module con.

### 복습 체크리스트
- [ ] Ghi nhớ 3 cấu trúc chuẩn của lập trình có cấu trúc: 순차 (Sequence), 선택 (Selection), 반복 (Iteration).
- [ ] Thuộc lòng công thức vàng: $V(G) = E - N + 2$.
- [ ] Nhớ công thức tính nhanh theo nút điều kiện: $V(G) = P + 1$.
- [ ] Hiểu rõ ý nghĩa thực tiễn: $V(G)$ biểu thị số ca kiểm thử tối thiểu cần có để phủ kín các đường dẫn cơ bản.
