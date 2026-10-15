# 196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, mục đích và thời điểm áp dụng của kiểm thử hộp trắng (화이트 박스 테스트 - White Box / Structural / Glass Box Testing) trong vòng đời phát triển phần mềm.
- Phân biệt các kỹ thuật kiểm thử hộp trắng kinh điển: Kiểm thử đường dẫn cơ bản (기초 경로 검사 - Basis Path Testing) và kiểm thử cấu trúc điều khiển (제어 구조 검사: 조건, 루프, 데이터 흐름 검사).
- Nắm vững hệ thống các tiêu chí đo lường độ bao phủ mã nguồn (Code Coverage): Bao phủ câu lệnh (문장), bao phủ nhánh/quyết định (분기/결정), bao phủ điều kiện (조건), và bao phủ đa điều kiện (다중 조건).

## 핵심 키워드 (Từ khóa)
- 화이트 박스 테스트 (White Box / Structural Testing)
- 원시 코드 오픈 (Source Code Visible)
- 기초 경로 검사 (Basis Path Testing - McCabe)
- 제어 구조 검사 (Control Structure Testing)
- 문장 커버리지 (Statement Coverage)
- 분기/결정 커버리지 (Branch / Decision Coverage)
- 조건 커버리지 (Condition Coverage)
- 데이터 흐름 검사 (Data Flow Testing)
- 루프 검사 (Loop Testing)

## 선행·연결 개념 (Kiến thức liên kết)
- [58-bai-hoc.md](58-bai-hoc.md): Lập trình cấu trúc và độ phức tạp chu trình McCabe $V(G)$.
- [60-bai-hoc.md](60-bai-hoc.md): Kiểm thử hộp đen (Black Box Testing: Phân vùng tương đương, Phân tích giá trị biên).
- [61-bai-hoc.md](61-bai-hoc.md): Chiến lược kiểm thử phần mềm (Đơn vị, Tích hợp, Hệ thống, Chấp nhận).

## 읽는 방법 (Cách đọc)
- Trong bài thi kỹ sư CNTT:
  - Khái niệm: Kiểm thử hộp trắng là kiểm thử **biết rõ và nhìn thấy toàn bộ mã nguồn bên trong (Source code open)**, tập trung vào cấu trúc logic, đường chạy của lệnh, vòng lặp. Áp dụng chủ yếu ở **giai đoạn đầu (초기)** – cấp độ Unit Test.
  - Phân loại: Nhớ nhóm từ khóa đại diện cho White Box gồm: **기초 경로 (Basis Path), 문장 (Statement), 분기/결정 (Branch/Decision), 조건 (Condition), 루프 (Loop), 데이터 흐름 (Data Flow)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Đặc điểm kỹ thuật của kiểm thử hộp trắng (White Box Test):**
  - Còn gọi là **Kiểm thử cấu trúc (Structural Testing)** hay Kiểm thử kính trong suốt (Glass-box Test).
  - Người kiểm thử (thường là lập trình viên) trực tiếp khảo sát mã nguồn, biến số, giải thuật và các nhánh rẽ điều khiển.
  - Mục tiêu: Phát hiện các lỗi sai logic, mã chết (Dead Code), rò rỉ bộ nhớ, hoặc các đường chạy điều kiện chưa từng được kích hoạt.
  - Được tiến hành chủ yếu ở **giai đoạn đầu (초기)** của quy trình kiểm thử phần mềm.

- **2. Các kỹ thuật kiểm thử hộp trắng chính:**
  1. **기초 경로 검사 (Basis Path Testing):** Do Tom McCabe đề xuất, dựa trên đồ thị dòng điều khiển (CFG) để tìm tập hợp các đường đi độc lập tuyến tính nhằm đảm bảo mọi câu lệnh được thực thi ít nhất một lần.
  2. **제어 구조 검사 (Control Structure Testing):**
     - **조건 검사 (Condition Testing):** Kiểm tra từng biểu thức logic rẽ nhánh bên trong module.
     - **루프 검사 (Loop Testing):** Kiểm tra độ vững chắc của các vòng lặp (`for`, `while`) tại các giá trị biên (0 lần lặp, 1 lần lặp, 2 lần lặp, $m$ lần lặp điển hình, và $n-1, n, n+1$ lần lặp giới hạn).
     - **데이터 흐름 검사 (Data Flow Testing):** Kiểm tra vòng đời của biến từ khi khai báo/định nghĩa (Definition) đến khi sử dụng (Usage) và giải phóng.

- **3. Các cấp độ bao phủ mã nguồn (Code Coverage Criteria):**

| Cấp độ bao phủ | Tiêu chuẩn đạt 100% Coverage |
| :--- | :--- |
| **문장 커버리지 (Statement Coverage)** | Mọi câu lệnh trong chương trình đều được thực thi ít nhất **1 lần**. |
| **분기 / 결정 커버리지 (Branch / Decision)** | Mọi nhánh rẽ của tất cả các câu lệnh điều kiện (cả nhánh **True** và nhánh **False**) đều được chạy qua ít nhất **1 lần**. |
| **조건 커버리지 (Condition Coverage)** | Mọi điều kiện con đơn lẻ trong biểu thức điều kiện phức hợp đều được thẩm định nhận cả giá trị **True** và **False** ít nhất **1 lần**. |
| **조건 / 결정 커버리지 (Condition/Decision)** | Đạt đồng thời cả yêu cầu của Branch Coverage và Condition Coverage. |
| **다중 조건 커버리지 (Multiple Condition)** | Kiểm tra **tất cả mọi tổ hợp chân trị có thể có** giữa các điều kiện con trong từng biểu thức phức hợp ($2^k$ trường hợp). |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ phân biệt Branch Coverage vs Condition Coverage:**
  - Xét biểu thức điều kiện: `if (A > 0 || B > 0)`
  - *Branch Coverage:* Chỉ cần toàn bộ biểu thức `(A > 0 || B > 0)` trả về True một lần (ví dụ $A=1, B=0$) và False một lần ($A=-1, B=-1$).
  - *Condition Coverage:* Yêu cầu điều kiện con $A > 0$ phải có lúc True lúc False, và $B > 0$ cũng phải có lúc True lúc False độc lập, bất kể kết quả gộp của câu `if` là gì.

### 복습 체크리스트
- [ ] Ghi nhớ kiểm thử hộp trắng thực hiện trên mã nguồn mở (Source Code Open) ở giai đoạn đầu.
- [ ] Kể tên các phương pháp hộp trắng: Basis Path, Condition, Loop, Data Flow testing.
- [ ] Phân biệt được độ bao phủ câu lệnh (Statement: chạy qua mọi dòng) và bao phủ rẽ nhánh (Decision: chạy qua cả nhánh True và False).
- [ ] Hiểu Multiple Condition Coverage là cấp độ khắt khe nhất vì thử toàn bộ tổ hợp chân trị logic.
