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
| Tiêu chuẩn độ phủ | Tên tiếng Hàn & Anh | Định nghĩa kỹ thuật chuẩn đề thi | Đánh giá độ mạnh |
| :--- | :--- | :--- | :--- |
| **Bao phủ câu lệnh** | **구문 검증 (Statement Coverage)** | Mọi câu lệnh trong mã nguồn đều được thực thi ít nhất 1 lần | Yếu nhất, dễ đạt |
| **Bao phủ quyết định / nhánh** | **결정 / 분기 검증 (Decision / Branch)** | Toàn bộ biểu thức điều kiện đều nhận cả giá trị `True` và `False` ít nhất 1 lần | Mạnh hơn Statement Coverage |
| **Bao phủ điều kiện** | **조건 검증 (Condition Coverage)** | Từng điều kiện con đơn lẻ bên trong đều phải nhận cả `True` và `False` ít nhất 1 lần | Không bảo đảm Decision Coverage |
| **Bao phủ điều kiện / nhánh** | **조건 / 분기 검증 (Condition/Branch)** | Thỏa mãn đồng thời cả hai: Toàn bộ nhánh nhận đủ T/F và từng điều kiện con nhận đủ T/F | Khá mạnh |
| **Bao phủ đa điều kiện** | **다중 조건 검증 (Multiple Condition)** | Kiểm tra **tất cả mọi tổ hợp giá trị chân lý** có thể có giữa các điều kiện con ($2^n$ tổ hợp) | Mạnh nhất, tốn kém nhất |

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

#### 3. Phân tích ví dụ logic cụ thể và điểm mù của Condition Coverage
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
   - Chỉ cần **1 Test Case**: Chọn $A = 1, B = 1 ightarrow$ Điều kiện True $ightarrow$ Lệnh `executeAction()` được thực thi. Đạt 100% Statement Coverage dù nhánh False chưa bao giờ được chạy!
2. **Với 결정/분기 검증 (Decision/Branch Coverage):**
   - Cần **2 Test Cases**:
     - Test Case 1: $A = 1, B = 1 ightarrow$ Decision nhận `True`.
     - Test Case 2: $A = -1, B = 1 ightarrow$ Decision nhận `False`.
3. **Với 조건 검증 (Condition Coverage) và Điểm mù nguy hiểm:**
   - Cần từng điều kiện con nhận đủ True và False:
     - Test Case 1: $A = 1, B = -1 ightarrow C_1 = T, C_2 = F ightarrow$ Decision tổng thể là `False`.
     - Test Case 2: $A = -1, B = 1 ightarrow C_1 = F, C_2 = T ightarrow$ Decision tổng thể là `False`.
   - **Điểm mù:** Cả hai Test Case đều khiến Decision tổng thể mang giá trị `False`! Câu lệnh `executeAction()` bên trong không bao giờ được chạy. Nghĩa là **Condition Coverage đạt 100% nhưng Statement Coverage và Decision Coverage lại không đạt**!
4. **Với 다중 조건 검증 (Multiple Condition Coverage):**
   - Với $n = 2$ điều kiện con, cần kiểm tra đủ $2^2 = 4$ ca kiểm thử bao phủ toàn bộ bảng chân trị: $(T, T), (T, F), (F, T), (F, F)$.

#### 4. Tiêu chuẩn MC/DC (Modified Condition/Decision Coverage)
- Khi một biểu thức phức hợp có $n = 10$ điều kiện con, Multiple Condition đòi hỏi $2^{10} = 1024$ Test Cases, chi phí kiểm thử quá khổng lồ.
- Chuẩn an toàn hàng không (DO-178C Cấp độ A) sử dụng tiêu chuẩn **MC/DC**: Chỉ yêu cầu tuyến tính **$n + 1$ ca kiểm thử** (với $n=10$ chỉ cần 11 ca test).
- **Nguyên lý MC/DC:** Mỗi điều kiện con khi độc lập đổi từ True sang False (trong khi giữ nguyên giá trị của tất cả các điều kiện con khác) phải trực tiếp làm thay đổi kết quả đầu ra của toàn bộ biểu thức quyết định.

---

### 복습 체크리스트
- [ ] Định nghĩa White-Box Testing là phương pháp dựa trên cấu trúc mã nguồn và logic nội bộ.
- [ ] Tính thành thạo độ phức tạp chu trình McCabe: $V(G) = E - N + 2 = P + 1 = \text{Regions}$.
- [ ] Nêu 3 kỹ thuật kiểm tra cấu trúc điều khiển: Điều kiện, Vòng lặp, Luồng dữ liệu (DUK).
- [ ] Nhớ 7 trường hợp biên khi kiểm tra vòng lặp đơn giản: $0, 1, 2, m, n-1, n, n+1$.
- [ ] Phân biệt định nghĩa cốt lõi của 5 cấp độ Code Coverage: Statement, Branch/Decision, Condition, Condition/Branch, Multiple Condition.
- [ ] Giải thích điểm mù của Condition Coverage (có thể đạt 100% Condition nhưng nhánh True không bao giờ chạy).
- [ ] Nhớ tiêu chuẩn MC/DC chỉ cần $n + 1$ ca kiểm thử thay vì $2^n$ trong công nghệ an toàn cao.
