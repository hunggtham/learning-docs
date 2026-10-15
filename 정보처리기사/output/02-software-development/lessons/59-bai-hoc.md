# 44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)

## 학습 목표 (Mục tiêu)
- Nắm vững hệ thống các tiêu chuẩn đo lường độ bao phủ mã nguồn (코드 커버리지 - Code Coverage) trong kiểm thử hộp trắng.
- Phân biệt chi tiết 5 cấp độ bao phủ logic: Độ phủ câu lệnh (구문/문장 검증), Độ phủ quyết định/nhánh (결정/분기 검증), Độ phủ điều kiện (조건 검증), Độ phủ điều kiện/nhánh (조건/분기 검증) và Độ phủ đa điều kiện (다중 조건 검증).
- Hiểu rõ mối quan hệ thứ bậc và độ mạnh yếu giữa các tiêu chí độ phủ để tối ưu hóa chi phí thiết kế ca kiểm thử trong các dự án an toàn cao.

## 핵심 키워드 (Từ khóa)
- 화이트박스 테스트 검증 기준 (White-box Coverage Criteria)
- 구문 / 문장 검증 기준 (Statement Coverage / 모든 구문 1회 이상)
- 결정 / 분기 검증 기준 (Decision / Branch Coverage / 전체 T·F 1회 이상)
- 조건 검증 기준 (Condition Coverage / 개별 조건식 T·F 1회 이상)
- 조건 / 분기 검증 기준 (Condition / Branch Coverage)
- 다중 조건 검증 기준 (Multiple Condition Coverage / 모든 진리표 조합)
- MC/DC (Modified Condition / Decision Coverage)

## 선행·연결 개념 (Kiến thức liên kết)
- [52-bai-hoc.md](52-bai-hoc.md): Khái niệm tổng quan về kiểm thử hộp trắng và kiểm tra đường dẫn cơ sở.
- [58-bai-hoc.md](58-bai-hoc.md): Phân loại kiểm thử dựa trên cấu trúc (Structure-based Testing).
- [64-bai-hoc.md](64-bai-hoc.md): Chi tiết chuyên sâu về các bài toán tính toán độ phủ White-box.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh từ khóa trong đề thi trắc nghiệm:
  - Thấy **"모든 구문(문장)이 한 번 이상 수행"** $\rightarrow$ **구문 검증 기준 (Statement)**.
  - Thấy **"전체 조건문이 True와 False를 한 번 이상"** $\rightarrow$ **결정/분기 검증 기준 (Decision / Branch)**.
  - Thấy **"개별 조건식이 True와 False를 한 번 이상"** $\rightarrow$ **조건 검증 기준 (Condition)**.
  - Thấy **"모든 개별 조건식의 가능한 모든 논리 조합 ($2^n$개)"** $\rightarrow$ **다중 조건 검증 기준 (Multiple Condition)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp 5 tiêu chí độ phủ kiểm thử hộp trắng:**

| Tiêu chuẩn độ phủ | Tên tiếng Hàn & Anh | Cơ chế và Định nghĩa kỹ thuật | Mức độ kiểm tra |
| :--- | :--- | :--- | :--- |
| **Bao phủ câu lệnh** | **구문 검증 기준 (Statement Coverage)** | Thiết kế bộ ca kiểm thử sao cho **tất cả các dòng lệnh (mọi câu lệnh) trong mã nguồn đều được thực thi ít nhất một lần** | Yếu nhất, dễ đạt nhất |
| **Bao phủ quyết định / nhánh** | **결정 / 분기 검증 기준 (Decision / Branch Coverage)** | Thiết kế ca kiểm thử sao cho **toàn bộ biểu thức điều kiện rẽ nhánh (lệnh `if`) đều nhận cả giá trị `True` và `False` ít nhất một lần** | Mạnh hơn Statement Coverage |
| **Bao phủ điều kiện** | **조건 검증 기준 (Condition Coverage)** | Tập trung vào bên trong biểu thức phức hợp: **Từng điều kiện con đơn lẻ đều phải nhận cả giá trị `True` và `False` ít nhất một lần** | Không bảo đảm bao phủ được toàn bộ nhánh rẽ |
| **Bao phủ điều kiện / nhánh** | **조건 / 분기 검증 기준 (Condition / Branch Coverage)** | Thỏa mãn đồng thời cả hai tiêu chí trên: Vừa bảo đảm toàn bộ nhánh rẽ nhận đủ T/F, vừa bảo đảm từng điều kiện con nhận đủ T/F | Khá mạnh |
| **Bao phủ đa điều kiện** | **다중 조건 검증 기준 (Multiple Condition Coverage)** | Kiểm tra **tất cả mọi tổ hợp giá trị chân lý có thể xảy ra giữa các điều kiện con** (tương đương với việc phủ $100\%$ bảng chân trị $2^n$ tổ hợp) | Cực kỳ mạnh, tốn kém nhất |

- **Ví dụ phân tích logic cụ thể:**
  - Xét đoạn mã nguồn: `if (A > 0 && B > 0) then Action();`
    - Ở đây, `(A > 0 && B > 0)` là **Biểu thức quyết định toàn cục (Decision)**.
    - `A > 0` là **Điều kiện con 1**, `B > 0` là **Điều kiện con 2**.
    - **Decision Coverage:** Chỉ cần 2 Test Case: 1 ca làm cả cụm thành True (ví dụ $A=1, B=1$), 1 ca làm cả cụm thành False (ví dụ $A=-1, B=1$).
    - **Condition Coverage:** Cần Test Case sao cho $A > 0$ có lúc True lúc False, và $B > 0$ có lúc True lúc False (nhưng có thể cả 2 test case đều cho kết quả nhánh rẽ là False, khiến lệnh `Action()` không bao giờ được chạy $\rightarrow$ Đây là điểm mù của Condition Coverage).
    - **Multiple Condition Coverage:** Bắt buộc phải thử đủ 4 tổ hợp ($2^2 = 4$): (T, T), (T, F), (F, T), (F, F).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tiêu chuẩn MC/DC (Modified Condition / Decision Coverage):**
  - Trong ngành hàng không dân dụng (tiêu chuẩn DO-178C cấp độ A), việc kiểm tra $2^n$ tổ hợp của Multiple Condition Coverage là quá tốn kém nếu một hàm có 10 điều kiện ($2^{10} = 1024$ test cases).
  - Tiêu chuẩn **MC/DC** ra đời để thay thế: Chỉ cần số lượng test case tuyến tính là **$n + 1$ ca kiểm thử**, nhưng vẫn chứng minh được rằng: Mỗi điều kiện con khi độc lập thay đổi giá trị từ True sang False (trong khi giữ nguyên các điều kiện khác) đều làm thay đổi trực tiếp kết quả đầu ra của toàn bộ biểu thức quyết định.

### 복습 체크리스트
- [ ] Định nghĩa Statement Coverage: Tất cả câu lệnh chạy ít nhất 1 lần.
- [ ] Phân biệt Decision Coverage (toàn bộ biểu thức if nhận T/F) và Condition Coverage (từng điều kiện con nhận T/F).
- [ ] Nhớ Multiple Condition Coverage kiểm tra toàn bộ $2^n$ tổ hợp bảng chân trị.
- [ ] Hiểu tiêu chuẩn MC/DC dùng $n + 1$ test cases trong công nghệ an toàn hàng không.
