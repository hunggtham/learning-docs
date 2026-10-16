# Môn 2 · Bài 15 — Kiểm thử hộp trắng và độ bao phủ kiểm thử

> **Mạch đọc:** [README](../README.md) là bản đồ chủ đề của **Môn 2 — 소프트웨어 개발 (Software Development)**. Tiếp nối [Bài 14: Nguyên lý, phân loại và quy trình kiểm thử](14-nguyen-ly-va-phan-loai-kiem-thu.md), nơi ta đã phân loại kiểm thử theo cơ sở thiết kế (Đặc tả, Cấu trúc, Kinh nghiệm), bài học này đào sâu vào nhánh **구조 기반 테스트 (Kiểm thử dựa trên cấu trúc)**, tức **화이트박스 테스트 (White-Box Testing)**. Bài học trang bị toàn bộ kỹ thuật phân tích luồng điều khiển mã nguồn, công thức tính độ phức tạp chu trình McCabe và 5 cấp độ bao phủ logic kiểm thử thường xuyên xuất hiện trong đề thi.

> **Phạm vi nguồn:** Hợp nhất và chuẩn hóa nội dung từ các bài học cũ `52-bai-hoc.md` (phần White-box), `59-bai-hoc.md`, `64-bai-hoc.md` và `67-bai-hoc.md` (tương ứng với các mục 15, 44, 127 ~ 129 và chuyên đề A+ Deep Dive trong tài liệu chuẩn gốc). Toàn bộ công thức toán học và tiêu chuẩn bao phủ được đối chiếu chính xác với chuẩn ISTQB và chuẩn khảo thí HRDK.

> **Mạch kiến thức:** Khi lập trình viên viết xong một đoạn mã, làm sao để biết đã kiểm tra hết mọi ngóc ngách logic? Bài học này giải quyết ba câu hỏi kỹ thuật: (1) Làm thế nào để xác định số lượng đường dẫn độc lập tối thiểu cần kiểm tra bằng công thức McCabe $V(G)$? (2) Kiểm tra cấu trúc vòng lặp và luồng dữ liệu cần chú ý những giá trị biên nào? (3) Năm cấp độ bao phủ mã nguồn (từ Statement đến Multiple Condition Coverage) khác nhau ra sao và điểm mù của từng cấp độ là gì?

---

## 1. 화이트박스 테스트의 개념과 특징 — Khái niệm và đặc điểm kiểm thử hộp trắng

**화이트박스 테스트는 원시 코드의 논리적인 모든 경로를 테스트하여 테스트 케이스를 설계하는 방법이다.**

Kiểm thử hộp trắng (White-Box Testing, còn gọi là Structural Testing — Kiểm thử cấu trúc, Glass-Box hay Clear-Box Testing) là phương pháp mà kiểm thử viên (thường là lập trình viên) trực tiếp quan sát và phân tích toàn bộ cấu trúc mã nguồn, giải thuật và luồng điều khiển bên trong của phần mềm để thiết kế các ca kiểm thử.

### Đặc trưng bản chất
- **Đối tượng kiểm tra:** Mã nguồn (Source Code), cấu trúc điều khiển rẽ nhánh, vòng lặp và trạng thái biến dữ liệu.
- **Thời điểm áp dụng:** Được áp dụng chủ yếu ở cấp độ **단위 테스트 (Unit Test — Kiểm thử đơn vị)** khi các hàm và module vừa được lập trình xong.
- **Mục tiêu chính:** Phát hiện các lỗi thuật toán nội bộ, vòng lặp vô hạn, nhánh lệnh chết (Dead Code), biến dùng sai kiểu hoặc chưa được khởi tạo, và bảo đảm tính đúng đắn của logic tính toán.

### So sánh đối đầu nhanh White-Box vs Black-Box

| Tiêu chí | 화이트박스 테스트 (White-Box Testing) | 블랙박스 테스트 (Black-Box Testing) |
| :--- | :--- | :--- |
| **Bản chất** | Kiểm thử cấu trúc logic nội bộ mã nguồn | Kiểm thử chức năng theo đặc tả yêu cầu bên ngoài |
| **Tầm nhìn** | **Nhìn thấy toàn bộ code (Glass-box)** | **Không cần nhìn code (Opaque-box)** |
| **Góc nhìn** | Nhà phát triển (Developer) | Người dùng (User) hoặc Kiểm thử viên độc lập (Tester) |
| **Cấp độ chính** | **단위 테스트 (Unit Test)** | **통합 / 시스템 / 인수 테스트** |
| **Dấu hiệu đề thi** | Từ khóa: *원시 코드 (mã nguồn), 내부 논리 (logic nội bộ), 제어 흐름 (luồng điều khiển), 경로 (đường dẫn)* | Từ khóa: *요구사항 명세서 (đặc tả yêu cầu), 입출력 (vào/ra), 기능 검증 (chức năng)* |

---

## 2. 기초 경로 검사 및 맥케이브 순환 복잡도 — Basis Path Testing & McCabe Complexity

Trong một đoạn mã có nhiều nhánh `if`, `switch` và vòng lặp `for`, `while`, số lượng đường dẫn thực thi có thể bùng nổ hàm mũ. Tom McCabe đã đề xuất phương pháp **기초 경로 검사 (Basis Path Testing — Kiểm tra đường dẫn cơ sở)** để giải quyết bài toán này.

### 2.1. Đồ thị luồng điều khiển (Control Flow Graph - CFG)
Mã nguồn được chuyển hóa thành đồ thị định hướng:
- **Nút (정점 / Node - ký hiệu $N$):** Đại diện cho một hoặc nhiều câu lệnh thực thi tuần tự hoặc một mệnh đề điều kiện rẽ nhánh.
- **Cạnh (간선 / Edge - ký hiệu $E$):** Mũi tên định hướng luồng chuyển tiếp điều khiển giữa các nút.
- **Vùng kín (영역 / Region):** Vùng không gian hình học được bao khép kín bởi các cạnh và nút (cộng thêm 1 vùng mở bên ngoài đồ thị).
- **Nút điều kiện (조건 노드 / Predicate Node - ký hiệu $P$):** Nút chứa biểu thức logic rẽ ra từ 2 nhánh trở lên (ví dụ: `if`, `while`).

### 2.2. Công thức tính Độ phức tạp chu trình (순환 복잡도 - Cyclomatic Complexity: $V(G)$)

Độ phức tạp chu trình $V(G)$ biểu thị **số lượng đường đi độc lập tuyến tính tối thiểu** trong đồ thị. Đây chính là số lượng ca kiểm thử tối thiểu cần thiết để bảo đảm mỗi câu lệnh và mỗi nhánh rẽ đều được thực thi ít nhất một lần.

$$V(G) = E - N + 2 = P + 1 = \text{Số vùng khép kín (Regions)}$$

- **Công thức 1 (Theo cạnh và nút):** $V(G) = E - N + 2$
  - $E$: Số cạnh (Edges).
  - $N$: Số nút (Nodes).
- **Công thức 2 (Theo nút điều kiện):** $V(G) = P + 1$
  - $P$: Số nút điều kiện rẽ nhánh (Predicate Nodes).
- **Công thức 3 (Theo hình học):** $V(G) = \text{Số vùng bị bao kín} + 1$ (tính cả vùng bên ngoài).

### Ví dụ tính toán thực chiến trong đề thi
- **Bài toán mẫu 1:** Đồ thị luồng điều khiển của một hàm có $E = 11$ cạnh và $N = 9$ nút. Tính số ca kiểm thử đường dẫn cơ sở tối thiểu cần thiết.
  - Áp dụng công thức: $V(G) = 11 - 9 + 2 = \mathbf{4}$.
  - Kết luận: Cần tối thiểu **4 Test Cases** độc lập.
- **Bài toán mẫu 2:** Một đoạn code có 3 câu lệnh `if` độc lập tuần tự (mỗi lệnh rẽ làm 2 nhánh True/False). Số nút điều kiện là $P = 3$.
  - Áp dụng công thức: $V(G) = 3 + 1 = \mathbf{4}$.

---

## 3. 제어 구조 검사 — Các kỹ thuật kiểm tra cấu trúc điều khiển

Bên cạnh việc kiểm tra đường dẫn cơ sở, kiểm thử hộp trắng sử dụng ba kỹ thuật chuyên sâu để kiểm soát cấu trúc điều khiển:

### 3.1. 조건 검사 (Condition Testing — Kiểm tra điều kiện)
- Tập trung kiểm tra các biểu thức điều kiện logic boolean độc lập bên trong câu lệnh rẽ nhánh.
- Thiết kế dữ liệu đầu vào để từng toán tử quan hệ (`<`, `>`, `==`) và toán tử logic (`AND`, `OR`, `NOT`) được kích hoạt đầy đủ ở cả hai trạng thái True và False.

### 3.2. 루프 검사 (Loop Testing — Kiểm tra vòng lặp)
Vòng lặp là nơi tập trung rất nhiều lỗi vượt biên mảng và treo vô hạn (vòng lặp chết). Kỹ thuật kiểm tra vòng lặp được chia theo cấu trúc:

1. **Vòng lặp đơn giản (Simple Loop):** Giả sử số lần lặp tối đa cho phép là $n$. Bộ kiểm thử chuẩn phải kích hoạt 7 trường hợp biên:
   - Bỏ qua vòng lặp hoàn toàn ($0$ lần lặp).
   - Đúng $1$ lần lặp.
   - Đúng $2$ lần lặp.
   - Lặp $m$ lần thông thường (với $m < n$).
   - Lặp $n - 1$ lần (sát ngưỡng trên).
   - Lặp đúng $n$ lần (ngưỡng tối đa).
   - Lặp $n + 1$ lần (vượt biên kiểm tra lỗi ngoại lệ).
2. **Vòng lặp lồng nhau (Nested Loops):** Cần cố định các vòng lặp ngoài ở giá trị tối thiểu, kiểm tra vòng lặp trong cùng trước, sau đó mới mở rộng dần ra ngoài.
3. **Vòng lặp nối tiếp (Concatenated Loops):** Nếu các vòng lặp độc lập thì kiểm tra như các vòng lặp đơn lẻ; nếu phụ thuộc dữ liệu thì đối xử như vòng lặp lồng nhau.

### 3.3. 데이터 흐름 검사 (Data Flow Testing — Kiểm tra luồng dữ liệu)
- Theo dõi toàn bộ vòng đời của các biến số trong chương trình theo chu trình **DUK**:
  - **D (Define / Định nghĩa):** Khởi tạo hoặc gán giá trị cho biến.
  - **U (Use / Sử dụng):** Đọc giá trị biến để tính toán (Computation Use - c-use) hoặc để làm điều kiện rẽ nhánh (Predicate Use - p-use).
  - **K (Kill / Hủy):** Giải phóng bộ nhớ hoặc biến hết phạm vi sử dụng.
- Mục tiêu: Phát hiện các lỗi nghiêm trọng như biến bị đọc trước khi được gán giá trị (Use before Define) hoặc biến được gán hai lần liên tiếp mà không hề được dùng ở giữa (Define-Define Anomaly).

---

## 4. 화이트박스 테스트 검증 기준 — 5 cấp độ bao phủ mã nguồn (Code Coverage)

Độ bao phủ mã nguồn (Code Coverage Criteria) là thước đo định lượng thể hiện mức độ mã nguồn được thực thi bởi bộ ca kiểm thử. Đề thi trắc nghiệm Kỹ sư Xử lý Thông tin thường xuyên yêu cầu phân biệt định nghĩa và điểm mù của 5 tiêu chuẩn sau:

### Bảng tổng hợp 5 tiêu chí độ phủ kiểm thử hộp trắng

| Tiêu chuẩn độ phủ | Tên Hàn & Anh | Định nghĩa kỹ thuật chuẩn đề thi | Đánh giá độ mạnh |
| :--- | :--- | :--- | :--- |
| **Bao phủ câu lệnh** | **구문 검증 기준 (Statement Coverage)** | Bộ ca kiểm thử bảo đảm **mọi câu lệnh (mọi dòng lệnh) trong mã nguồn đều được chạy ít nhất một lần** | Yếu nhất, dễ đạt nhất |
| **Bao phủ quyết định / nhánh** | **결정 / 분기 검증 기준 (Decision / Branch Coverage)** | Bộ ca kiểm thử bảo đảm **toàn bộ biểu thức điều kiện rẽ nhánh (câu lệnh `if`) đều nhận cả giá trị `True` và `False` ít nhất một lần** | Mạnh hơn Statement Coverage |
| **Bao phủ điều kiện** | **조건 검증 기준 (Condition Coverage)** | Tập trung vào bên trong biểu thức: **Từng điều kiện con đơn lẻ đều phải nhận cả giá trị `True` và `False` ít nhất một lần** | Không bảo đảm Decision Coverage |
| **Bao phủ điều kiện / nhánh** | **조건 / 분기 검증 기준 (Condition / Branch Coverage)** | Thỏa mãn đồng thời cả hai: Vừa bảo đảm toàn bộ nhánh rẽ nhận đủ T/F, vừa bảo đảm từng điều kiện con nhận đủ T/F | Khá mạnh |
| **Bao phủ đa điều kiện** | **다중 조건 검증 기준 (Multiple Condition Coverage)** | Kiểm tra **tất cả mọi tổ hợp giá trị chân lý có thể có giữa các điều kiện con** (tương đương phủ 100% bảng chân trị $2^n$ tổ hợp) | Mạnh nhất, tốn kém nhất |

### Phân tích ví dụ logic cụ thể và điểm mù
Xét đoạn mã nguồn sau:
```java
if (A > 0 && B > 0) {
    executeAction();
}
```
Trong đó:
- `(A > 0 && B > 0)` là **Biểu thức quyết định toàn cục (Decision)**.
- `A > 0` là **Điều kiện con 1 ($C_1$)**.
- `B > 0` là **Điều kiện con 2 ($C_2$)**.

1. **Với 구문 검증 (Statement Coverage):**
   - Chỉ cần **1 Test Case**: Chọn $A = 1, B = 1 \rightarrow$ Điều kiện True $\rightarrow$ Lệnh `executeAction()` được thực thi. Đạt 100% Statement Coverage dù nhánh False chưa bao giờ được chạy!
2. **Với 결정/분기 검증 (Decision/Branch Coverage):**
   - Cần **2 Test Cases**:
     - Test Case 1: $A = 1, B = 1 \rightarrow$ Decision nhận `True`.
     - Test Case 2: $A = -1, B = 1 \rightarrow$ Decision nhận `False`.
3. **Với 조건 검증 (Condition Coverage) và Điểm mù nguy hiểm:**
   - Cần từng điều kiện con nhận đủ True và False:
     - Test Case 1: $A = 1, B = -1 \rightarrow C_1 = T, C_2 = F \rightarrow$ Decision tổng thể là `False`.
     - Test Case 2: $A = -1, B = 1 \rightarrow C_1 = F, C_2 = T \rightarrow$ Decision tổng thể là `False`.
   - **Điểm mù:** Cả hai Test Case đều khiến Decision tổng thể mang giá trị `False`! Câu lệnh `executeAction()` bên trong không bao giờ được chạy. Nghĩa là **Condition Coverage đạt 100% nhưng Statement Coverage và Decision Coverage lại không đạt**!
4. **Với 다중 조건 검증 (Multiple Condition Coverage):**
   - Với $n = 2$ điều kiện con, cần kiểm tra đủ $2^2 = 4$ ca kiểm thử bao phủ toàn bộ bảng chân trị: $(T, T), (T, F), (F, T), (F, F)$.

### Mở rộng chuyên sâu: Tiêu chuẩn MC/DC (Modified Condition/Decision Coverage)
- Khi một biểu thức phức hợp có $n = 10$ điều kiện con, Multiple Condition đòi hỏi $2^{10} = 1024$ Test Cases, chi phí kiểm thử quá khổng lồ.
- Chuẩn an toàn hàng không (DO-178C Cấp độ A) sử dụng tiêu chuẩn **MC/DC**: Chỉ yêu cầu tuyến tính **$n + 1$ ca kiểm thử** (với $n=10$ chỉ cần 11 ca test).
- **Nguyên lý MC/DC:** Mỗi điều kiện con khi độc lập đổi từ True sang False (trong khi giữ nguyên giá trị của tất cả các điều kiện con khác) phải trực tiếp làm thay đổi kết quả đầu ra của toàn bộ biểu thức quyết định.

---

## 5. Nối mạch kiến thức sang bài tiếp theo

Từ việc làm chủ toàn bộ kỹ thuật kiểm thử cấu trúc bên trong mã nguồn qua luồng điều khiển, độ phức tạp McCabe và các cấp độ Code Coverage, người học đã có công cụ vững chắc để kiểm định tầng Unit Test.

Tuy nhiên, kiểm thử hộp trắng hoàn toàn bất lực trong việc phát hiện các tính năng bị lập trình viên bỏ sót (omission faults) hoặc giao diện hiển thị sai lệch so với yêu cầu của khách hàng. Để khắc phục điểm mù đó, chúng ta chuyển sang **[Bài 16: Kiểm thử hộp đen và kỹ thuật thiết kế Test Case](16-kiem-thu-hop-den-va-test-case.md)**, nơi sản phẩm được kiểm nghiệm độc lập từ bên ngoài hoàn toàn dựa trên bản đặc tả yêu cầu chức năng.

---

## 6. 복습 체크리스트 (Checklist ôn tập)

- [ ] Định nghĩa White-Box Testing là phương pháp dựa trên mã nguồn và luồng logic nội bộ.
- [ ] Tính thành thạo độ phức tạp chu trình McCabe: $V(G) = E - N + 2 = P + 1$.
- [ ] Nêu 3 kỹ thuật kiểm tra cấu trúc điều khiển: Điều kiện, Vòng lặp, Luồng dữ liệu (DUK).
- [ ] Nhớ 7 trường hợp biên khi kiểm tra vòng lặp đơn giản: $0, 1, 2, m, n-1, n, n+1$.
- [ ] Phân biệt định nghĩa cốt lõi của 5 cấp độ Code Coverage: Statement, Branch/Decision, Condition, Condition/Branch, Multiple Condition.
- [ ] Giải thích điểm mù của Condition Coverage (có thể đạt 100% Condition nhưng nhánh True không bao giờ chạy).
- [ ] Nhớ tiêu chuẩn MC/DC chỉ cần $n + 1$ ca kiểm thử thay vì $2^n$ trong công nghệ an toàn cao.
