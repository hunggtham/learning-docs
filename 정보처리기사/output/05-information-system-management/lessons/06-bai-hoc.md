# 3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, mục tiêu chiến lược và 3 yếu tố nền tảng của quản lý dự án phần mềm (**3P: People - Con người, Problem - Vấn đề, Process - Quy trình**).
- Thuộc lòng và vận dụng thành thạo các công thức tính toán ước lượng dự án theo phương pháp dòng mã nguồn (**LOC - Lines of Code**): Công số nỗ lực nhân tháng (Man-Month / Person-Month), Thời gian phát triển dự án, Chi phí phát triển, và Năng suất lao động.
- Giải quyết chính xác các bài toán định lượng tính toán chi phí dự án trong đề thi trắc nghiệm và thực hành.

## 핵심 키워드 (Từ khóa)
- 프로젝트 관리 3대 요소 (3P: People, Problem, Process)
- LOC 기법 (Lines of Code)
- 노력 / 인월 계산 (Man-Month / Person-Month - MM)
- 개발 기간 및 투입 인원 산정 (Development Duration & Staffing)
- 개발 비용 산출 (Total Development Cost)
- 생산성 (Productivity = LOC / MM)

## 선행·연결 개념 (Kiến thức liên kết)
- [05-bai-hoc.md](05-bai-hoc.md): Đặc tính của Framework và các điểm phân biệt trọng điểm.
- [07-bai-hoc.md](07-bai-hoc.md): Quản lý tiến độ dự án bằng sơ đồ mạng PERT/CPM và đường găng Critical Path.
- [08-bai-hoc.md](08-bai-hoc.md): Chi tiết các mô hình toán học ước tính chi phí phần mềm (COCOMO, Putnam, FP).

## 읽는 방법 (Cách đọc)
- Trong bài thi kỹ sư CNTT, câu hỏi tính toán về LOC luôn tuân theo các công thức cơ sở:
  $$\mathbf{\text{Nỗ lực (Man-Month)} = \text{Thời gian phát triển (tháng)} \times \text{Số lượng nhân sự}}$$
  $$\mathbf{\text{Nỗ lực (Man-Month)} = \frac{\text{Tổng số dòng code LOC}}{\text{Năng suất 1 người tạo ra trong 1 tháng}}}$$
  $$\mathbf{\text{Chi phí dự án} = \text{Nỗ lực (Man-Month)} \times \text{Đơn giá nhân công 1 tháng}}$$
  $$\mathbf{\text{Thời gian phát triển} = \frac{\text{Nỗ lực (Man-Month)}}{\text{Số lượng nhân sự}}}$$
- Nhớ thứ tự quan trọng trong 3P: **People (Con người)** luôn là nhân tố quyết định thành bại hàng đầu của dự án.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Tam giác quản trị 3P trong dự án phần mềm:**
  - **People (인적 자원 - Con người):** Là yếu tố **quan trọng nhất**; bao gồm người quản lý dự án (PM), kỹ sư phân tích, lập trình viên, kiểm thử viên và khách hàng.
  - **Problem (문제 / 과업 - Vấn đề):** Xác định phạm vi công việc, mục tiêu nghiệp vụ của khách hàng, và các ràng buộc kỹ thuật.
  - **Process (프로세스 - Quy trình):** Khung quy trình và các giai đoạn thực thi (SDLC), phương pháp luận phát triển được áp dụng.

- **2. Bảng hệ thống công thức tính toán LOC và Man-Month:**

| Chỉ số cần tính | Công thức toán học chuẩn | Đơn vị đo |
| :--- | :--- | :---: |
| **Nỗ lực (Man-Month)** | $\text{MM} = \text{Thời gian phát triển (tháng)} \times \text{Số nhân lực}$ | Người - Tháng (MM) |
| **Nỗ lực theo LOC** | $\text{MM} = \frac{\text{Tổng LOC dự kiến}}{\text{Năng suất 1 người trong 1 tháng}}$ | Người - Tháng (MM) |
| **Chi phí phát triển** | $\text{Chi phí} = \text{Nỗ lực (MM)} \times \text{Đơn giá nhân công 1 người/tháng}$ | Tiền tệ (VND / KRW / USD) |
| **Thời gian bàn giao** | $\text{Thời gian (tháng)} = \frac{\text{Nỗ lực (MM)}}{\text{Số nhân lực thực tế}}$ | Tháng |
| **Năng suất bình quân** | $\text{Năng suất} = \frac{\text{Tổng LOC}}{\text{Nỗ lực (MM)}}$ | Dòng code / Người-Tháng |

- **3. Bài toán mẫu điển hình trong đề thi:**
  - *Đề bài:* Một dự án phần mềm có quy mô ước tính là $30.000$ dòng code (LOC). Một lập trình viên trung bình viết được $500$ dòng code trong một tháng. Nếu công ty bố trí $10$ lập trình viên cùng tham gia dự án với mức lương $3.000.000$ KRW/người/tháng, hãy tính:
    1. Tổng nỗ lực dự án (Man-Month)?
    2. Thời gian hoàn thành dự án (tháng)?
    3. Tổng chi phí nhân công của dự án?
  - *Lời giải:*
    1. $\text{Nỗ lực (MM)} = \frac{30.000}{500} = 60 \text{ Man-Month}$.
    2. $\text{Thời gian phát triển} = \frac{\text{Nỗ lực}}{\text{Số người}} = \frac{60}{10} = 6 \text{ tháng}$.
    3. $\text{Tổng chi phí} = 60 \times 3.000.000 = 180.000.000 \text{ KRW}$.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Định luật Brooks (Brooks' Law) trong quản trị nhân sự:**
  - *"Thêm người vào một dự án phần mềm đang bị trễ hạn chỉ làm cho nó càng trễ hạn hơn"* (Adding manpower to a late software project makes it later).
  - Lý do: Người mới vào cần thời gian đào tạo từ người cũ, đồng thời số lượng kênh giao tiếp giữa các thành viên tăng theo cấp số nhân $\frac{N(N-1)}{2}$, làm phát sinh chi phí họp hành, giải thích và đồng bộ hóa khổng lồ.

### 복습 체크리스트
- [ ] Ghi nhớ 3 yếu tố quản lý dự án (3P): People (quan trọng nhất), Problem, Process.
- [ ] Thuộc lòng công thức tính Man-Month: $\text{MM} = \text{Thời gian} \times \text{Số người} = \frac{\text{LOC}}{\text{Năng suất}}$.
- [ ] Biết cách tính thời gian phát triển: $\text{Thời gian} = \frac{\text{Man-Month}}{\text{Số người}}$.
- [ ] Nhớ Định luật Brooks: Bổ sung thêm nhân lực vào dự án đang trễ sẽ làm dự án càng trễ thêm.
