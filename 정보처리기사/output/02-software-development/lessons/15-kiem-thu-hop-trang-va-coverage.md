# 화이트박스 테스트와 테스트 커버리지 (Kiểm thử hộp trắng và độ bao phủ)

## 학습 목표
- Nắm vững định nghĩa và đặc trưng của Kiểm thử hộp trắng (`화이트박스 테스트 / White-Box Testing`): dựa trên cấu trúc mã nguồn, giải thuật và luồng điều khiển bên trong, chủ yếu áp dụng ở cấp độ kiểm thử đơn vị (`단위 테스트`).
- Áp dụng thành thạo 3 công thức tính Độ phức tạp chu trình McCabe (`순환 복잡도 / Cyclomatic Complexity: V(G)`): $V(G) = E - N + 2 = P + 1 = \text{Số vùng kín Regions}$.
- Nắm vững 3 kỹ thuật kiểm tra cấu trúc điều khiển: Kiểm tra điều kiện (`조건 검사`), Kiểm tra vòng lặp (`루프 검사` - 7 giá trị biên), và Kiểm tra luồng dữ liệu (`데이터 흐름 검사` - chu trình DUK: Define, Use, Kill).
- Phân tích chi tiết định nghĩa và điểm mù của 5 cấp độ bao phủ mã nguồn: Bao phủ câu lệnh (`구문`), Bao phủ nhánh/quyết định (`결정/분기`), Bao phủ điều kiện (`조건`), Bao phủ điều kiện/nhánh (`조건/분기`), và Bao phủ đa điều kiện (`다중 조건`).
- Hiểu rõ tiêu chuẩn an toàn hàng không MC/DC (Modified Condition/Decision Coverage) tối ưu hóa số ca kiểm thử xuống bậc tuyến tính $n + 1$.

## 핵심 키워드
- 화이트박스 테스트 (Kiểm thử hộp trắng / White-Box / 구조 기반 / 단위 테스트)
- 제어 흐름 그래프 (Đồ thị luồng điều khiển / Control Flow Graph / CFG)
- 맥케이브 순환 복잡도 (Độ phức tạp McCabe / Cyclomatic Complexity / V(G) = E - N + 2 = P + 1)
- 제어 구조 검사 (조건 검사, 루프 검사 Loop Testing 7개 경계, 데이터 흐름 DUK)
- 테스트 커버리지 (Độ bao phủ / 구문 Statement, 결정/분기 Branch, 조건 Condition, 다중 조건 Multiple Condition)
- MC/DC (Modified Condition/Decision Coverage / n + 1개 테스트 케이스)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [14-nguyen-ly-va-phan-loai-kiem-thu.md](14-nguyen-ly-va-phan-loai-kiem-thu.md), chúng ta đã khảo sát các nguyên lý nền tảng và phân loại kiểm thử dựa trên cấu trúc (Structure-based).
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết việc đo lường độ bao phủ logic bên trong mã nguồn, tính toán số lượng đường dẫn độc lập tối thiểu cần test qua công thức McCabe và nhận diện các điểm mù nguy hiểm trong kiểm thử nhánh rẽ.
- **Dùng đi đâu (Forward Handoff):** Kiểm thử hộp trắng chỉ nhìn thấy code bên trong mà không phát hiện được tính năng bị bỏ sót theo yêu cầu khách hàng, bàn giao trực tiếp sang [16-kiem-thu-hop-den-va-test-case.md](16-kiem-thu-hop-den-va-test-case.md) để khảo sát kỹ thuật Kiểm thử hộp đen.

## 읽는 방법
- Đọc TẦNG A để nắm chắc 2 công thức tính McCabe ($E - N + 2$ và $P + 1$), bảng 5 cấp độ Code Coverage, và điểm mù kinh điển của Condition Coverage (đạt 100% nhưng nhánh True không bao giờ chạy).
- Đọc TẦNG B để hiểu sâu ví dụ mã logic boolean, chu trình DUK trong luồng dữ liệu và 7 giá trị biên trong kiểm tra vòng lặp.

---

## 화이트박스 테스트와 테스트 커버리지

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Đối chiếu nhanh White-Box vs Black-Box
| Tiêu chí | 화이트박스 테스트 (White-Box) | 블랙박스 테스트 (Black-Box) |
| :--- | :--- | :--- |
| **Bản chất** | Kiểm thử cấu trúc logic nội bộ mã nguồn | Kiểm thử chức năng theo đặc tả yêu cầu bên ngoài |
| **Tầm nhìn** | **Nhìn thấy toàn bộ code (Glass-box)** | **Không cần nhìn code (Opaque-box)** |
| **Góc nhìn** | Nhà phát triển (Developer) | Người dùng (User) hoặc Tester độc lập |
| **Cấp độ chính** | **단위 테스트 (Unit Test)** | **통합 / 시스템 / 인수 테스트** |
| **Dấu hiệu đề thi** | Từ khóa: *원시 코드 (mã nguồn), 내부 논리, 제어 흐름, 경로* | Từ khóa: *요구사항 명세서 (đặc tả), 입출력, 기능 검증* |

#### 2. Công thức tính Độ phức tạp chu trình McCabe ($V(G)$)
$$\mathbf{V(G) = E - N + 2 = P + 1 = \text{Số vùng khép kín (Regions)}}$$
- **$E$ (Edges):** Số cạnh / nhánh nối trong đồ thị luồng điều khiển.
- **$N$ (Nodes):** Số nút / khối lệnh.
- **$P$ (Predicate Nodes):** Số nút điều kiện rẽ nhánh (số câu lệnh `if`, `while`).
- *Ý nghĩa:* Biểu thị **số lượng đường đi độc lập tuyến tính tối thiểu** cần kiểm tra.

#### 3. Bảng 5 cấp độ bao phủ mã nguồn (Code Coverage Criteria)

```text
  [PHÂN CẤP ĐỘ PHỦ MÃ NGUỒN - TỪ YẾU ĐẾN MẠNH]
  ▲  [MẠNH NHẤT] 5. 다중 조건 검증 (Multiple Condition Coverage - 2^n tổ hợp bảng chân trị)
  │              4. MC/DC 검증 (Modified Condition/Decision - Tuyến tính n + 1 ca test)
  │              3. 조건 / 결정 검증 (Condition / Decision Coverage - Thỏa mãn cả 2)
  │              2. 결정 / 분기 검증 (Decision / Branch Coverage - Toàn bộ nhánh T/F)
  ▼  [YẾU NHẤT]  1. 구문 검증 (Statement Coverage - Mọi dòng lệnh chạy ít nhất 1 lần)
```

| Tiêu chuẩn độ phủ | Tên tiếng Hàn & Anh | Định nghĩa kỹ thuật chuẩn đề thi | Đánh giá độ mạnh |
|:---|:---|:---|:---|
| **Bao phủ câu lệnh** | **구문 검증 (Statement Coverage)** | Mọi câu lệnh trong mã nguồn đều được thực thi ít nhất 1 lần | Yếu nhất, dễ đạt nhất |
| **Bao phủ quyết định / nhánh** | **결정 / 분기 검증 (Decision / Branch)** | Toàn bộ biểu thức điều kiện đều nhận cả giá trị `True` và `False` ít nhất 1 lần | Mạnh hơn Statement Coverage |
| **Bao phủ điều kiện** | **조건 검증 (Condition Coverage)** | Từng điều kiện con đơn lẻ bên trong đều phải nhận cả `True` và `False` ít nhất 1 lần | Không bảo đảm Decision Coverage |
| **Bao phủ điều kiện / nhánh** | **조건 / 분기 검증 (Condition/Branch)** | Thỏa mãn đồng thời cả hai: Toàn bộ nhánh nhận đủ T/F và từng điều kiện con nhận đủ T/F | Khá mạnh |
| **Bao phủ đa điều kiện** | **다중 조건 검증 (Multiple Condition)** | Kiểm tra **tất cả mọi tổ hợp giá trị chân lý** có thể có giữa các điều kiện con ($2^n$ tổ hợp) | Mạnh nhất, tốn kém nhất |

- **Công thức tính tỷ lệ phần trăm bao phủ (Coverage Percentage Formula):**
  $$\text{Statement Coverage} = \frac{\text{Số câu lệnh được thực thi}}{\text{Tổng số câu lệnh có trong hàm}} \times 100\%$$
  $$\text{Branch / Decision Coverage} = \frac{\text{Số nhánh True/False đã được rẽ qua}}{\text{Tổng số nhánh quyết định} \times 2} \times 100\%$$
  $$\text{Condition Coverage} = \frac{\text{Số trạng thái True/False của điều kiện con đã đạt}}{\text{Tổng số điều kiện con} \times 2} \times 100\%$$

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Tính McCabe $V(G)$:**
  - Cho $E = 11, N = 9 \rightarrow V(G) = 11 - 9 + 2 = \mathbf{4}$.
  - Cho 3 câu lệnh `if` độc lập ($P = 3$) $\rightarrow V(G) = 3 + 1 = \mathbf{4}$.
- **Bẫy 2: Điểm mù của Condition Coverage:**
  - Xét đoạn mã: `if (A > 0 && B > 0) { action(); }`
  - Test Case 1: $A = 1, B = -1$ ($C_1 = T, C_2 = F \rightarrow$ Decision tổng = `False`).
  - Test Case 2: $A = -1, B = 1$ ($C_1 = F, C_2 = T \rightarrow$ Decision tổng = `False`).
  - Cả 2 Test Case đều khiến nhánh tổng là False, lệnh `action()` không bao giờ được chạy!
  - Kết luận: **Condition Coverage đạt 100% nhưng Statement và Decision Coverage lại KHÔNG ĐẠT!**
- **Bẫy 3: Tiêu chuẩn MC/DC:** Khi có $n$ điều kiện con, Multiple Condition đòi hỏi $2^n$ ca test; chuẩn an toàn cao MC/DC chỉ cần tuyến tính **$n + 1$ ca kiểm thử**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Kiểm tra vòng lặp đơn giản (Loop Testing)
- Giả sử số lần lặp tối đa cho phép là $n$. Bộ kiểm thử chuẩn phải bao phủ 7 trường hợp biên:
  1. $0$ lần (bỏ qua vòng lặp hoàn toàn).
  2. Đúng $1$ lần.
  3. Đúng $2$ lần.
  4. Lặp $m$ lần thông thường ($m < n$).
  5. Lặp $n - 1$ lần (sát ngưỡng tối đa).
  6. Lặp đúng $n$ lần (ngưỡng tối đa).
  7. Lặp $n + 1$ lần (vượt biên để kiểm tra xử lý ngoại lệ).

#### 2. Kiểm tra luồng dữ liệu theo chu trình DUK (Data Flow Testing)
- `D (Define)`: Khởi tạo hoặc gán giá trị cho biến.
- `U (Use)`: Đọc giá trị biến để tính toán (c-use) hoặc làm điều kiện rẽ nhánh (p-use).
- `K (Kill)`: Hủy biến hoặc giải phóng vùng nhớ.
- Mục tiêu: Phát hiện lỗi đọc biến trước khi định nghĩa (Use before Define) hoặc gán 2 lần liên tiếp không dùng.

#### 3. Bảng chân trị thực nghiệm và Phân tích điểm mù Condition Coverage
Xét đoạn mã nguồn thực tế:
```java
if (A > 0 && B > 0) {
    executeAction(); // Dòng lệnh thực thi
}
```
Trong đó:
- `A > 0` là **Điều kiện con 1 ($C_1$)**.
- `B > 0` là **Điều kiện con 2 ($C_2$)**.
- `(A > 0 && B > 0)` là **Biểu thức quyết định tổng thể (Decision $D$)**.

##### Bảng chân trị toàn diện (Truth Table):

| Ca kiểm thử (Test Case) | $C_1: A > 0$ | $C_2: B > 0$ | Decision $D: C_1 \land C_2$ | Lệnh executeAction() | Thuộc tập ca test tối thiểu nào? |
|:---:|:---:|:---:|:---:|:---:|:---|
| **TC1** ($A=1, B=1$) | **True** | **True** | **True** | **Thực thi** | Statement, Decision, MC/DC |
| **TC2** ($A=1, B=-1$) | **True** | **False** | **False** | Bỏ qua | Decision, Condition, MC/DC |
| **TC3** ($A=-1, B=1$) | **False** | **True** | **False** | Bỏ qua | Condition, MC/DC |
| **TC4** ($A=-1, B=-1$) | **False** | **False** | **False** | Bỏ qua | Chỉ cần trong Multiple Condition |

- **Phân tích từng mức độ bao phủ qua bảng chân trị:**
  1. **구문 검증 (Statement Coverage):** Chỉ cần **TC1** vì khi $D = \text{True}$, dòng lệnh `executeAction()` được chạy. Tỷ lệ bao phủ đạt $100\%$ dù nhánh False hoàn toàn bị bỏ sót.
  2. **결정/분기 검증 (Decision/Branch Coverage):** Cần **TC1 ($D = \text{True}$)** và **TC2 ($D = \text{False}$)**. Đạt $100\%$ Branch Coverage vì cả hai nhánh True và False của biểu thức điều kiện đều được chạy.
  3. **조건 검증 (Condition Coverage) và Điểm mù chí tử:**
     - Nếu người kiểm thử chọn cặp **{TC2, TC3}**:
       - Với $C_1$: TC2 mang True, TC3 mang False $\rightarrow C_1$ nhận đủ T/F ($100\%$).
       - Với $C_2$: TC2 mang False, TC3 mang True $\rightarrow C_2$ nhận đủ T/F ($100\%$).
     - $\rightarrow$ **Condition Coverage đạt $100\%$ tuyệt đối!**
     - **Tuy nhiên:** Cả TC2 và TC3 đều làm $D = \text{False}$. Do đó nhánh True không bao giờ chạy và lệnh `executeAction()` không bao giờ được chạm tới $\rightarrow$ **Statement Coverage = 0% và Branch Coverage chỉ đạt 50%**.
  4. **다중 조건 검증 (Multiple Condition Coverage):** Bắt buộc phải chạy **cả 4 ca {TC1, TC2, TC3, TC4}** để quét trọn vẹn $2^2 = 4$ tổ hợp chân trị.

#### 4. Tiêu chuẩn MC/DC (Modified Condition/Decision Coverage)
- Khi một biểu thức phức hợp có $n = 10$ điều kiện con, Multiple Condition đòi hỏi $2^{10} = 1024$ Test Cases, chi phí kiểm thử quá khổng lồ.
- Chuẩn an toàn hàng không (DO-178C Cấp độ A) sử dụng tiêu chuẩn **MC/DC**: Chỉ yêu cầu tuyến tính **$n + 1$ ca kiểm thử** (với $n=10$ chỉ cần 11 ca test).
- **Nguyên lý MC/DC:** Mỗi điều kiện con khi độc lập đổi từ True sang False (trong khi giữ nguyên giá trị của tất cả các điều kiện con khác) phải trực tiếp làm thay đổi kết quả đầu ra của toàn bộ biểu thức quyết định.
- **Minh họa trên bảng chân trị:**
  - Cặp kiểm chứng cho $C_1$: {TC1, TC3} (khi $C_2=\text{True}$ cố định, $C_1$ đổi từ $T \rightarrow F$ làm $D$ đổi từ $T \rightarrow F$).
  - Cặp kiểm chứng cho $C_2$: {TC1, TC2} (khi $C_1=\text{True}$ cố định, $C_2$ đổi từ $T \rightarrow F$ làm $D$ đổi từ $T \rightarrow F$).
  - $\rightarrow$ Bộ ca kiểm thử MC/DC chỉ cần **3 ca: {TC1, TC2, TC3}** (đúng bằng $n + 1 = 2 + 1 = 3$).

---

### 복습 체크리스트
- [ ] Định nghĩa White-Box Testing là phương pháp dựa trên cấu trúc mã nguồn và logic nội bộ.
- [ ] Tính thành thạo độ phức tạp chu trình McCabe: $V(G) = E - N + 2 = P + 1 = \text{Regions}$.
- [ ] Nêu 3 kỹ thuật kiểm tra cấu trúc điều khiển: Điều kiện, Vòng lặp, Luồng dữ liệu (DUK).
- [ ] Nhớ 7 trường hợp biên khi kiểm tra vòng lặp đơn giản: $0, 1, 2, m, n-1, n, n+1$.
- [ ] Phân biệt định nghĩa cốt lõi của 5 cấp độ Code Coverage: Statement, Branch/Decision, Condition, Condition/Branch, Multiple Condition.
- [ ] Giải thích điểm mù của Condition Coverage (chọn {TC2, TC3} đạt 100% Condition nhưng nhánh True không bao giờ chạy).
- [ ] Nhớ tiêu chuẩn MC/DC chỉ cần tuyến tính $n + 1$ ca kiểm thử thay vì $2^n$ trong công nghệ an toàn cao.
