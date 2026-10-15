# 183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa toán học và bản chất thực tế của Phụ thuộc hàm (`함수적 종속성 / Functional Dependency`): Mối quan hệ ràng buộc giữa tập thuộc tính quyết định ($X$ - `결정자`) và tập thuộc tính phụ thuộc ($Y$ - `종속자`), ký hiệu $X \rightarrow Y$.
- Phân biệt chi tiết **Phụ thuộc hàm hoàn toàn (`완전 함수 종속`)** và **Phụ thuộc hàm từng phần (`부분 함수 종속`)** để giải quyết bài toán đưa bảng lên Dạng chuẩn 2 (2NF).
- Hiểu sâu cơ chế của **Phụ thuộc hàm bắc cầu (`이행적 함수 종속`)**: Chuỗi quan hệ $A \rightarrow B$ và $B \rightarrow C$ dẫn đến $A \rightarrow C$, và vai trò của việc loại bỏ mối phụ thuộc này để đạt Dạng chuẩn 3 (3NF).

## 핵심 키워드 (Từ khóa)
- 함수적 종속 (Phụ thuộc hàm / Functional Dependency: $X \rightarrow Y$)
- 결정자 (Yếu tố quyết định / Determinant: $X$)
- 종속자 (Yếu tố phụ thuộc / Dependent: $Y$)
- 완전 함수 종속 (Phụ thuộc hàm hoàn toàn / Full Functional Dependency)
- 부분 함수 종속 (Phụ thuộc hàm từng phần / Partial Functional Dependency)
- 이행적 함수 종속 (Phụ thuộc hàm bắc cầu / Transitive Functional Dependency)
- 정규화 연계 (Mối liên hệ với chuẩn hóa: 2NF, 3NF)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([11-bai-hoc.md](11-bai-hoc.md), [17-bai-hoc.md](17-bai-hoc.md), [18-bai-hoc.md](18-bai-hoc.md), [20-bai-hoc.md](20-bai-hoc.md)):** Lý thuyết phụ thuộc hàm chính là nền tảng toán học duy nhất dẫn đường cho toàn bộ tiến trình Chuẩn hóa dữ liệu từ 1NF lên 3NF và BCNF.
- **Tiếp nối sang bài sau ([44-bai-hoc.md](44-bai-hoc.md)):** Các ràng buộc phụ thuộc hàm và cấu trúc khóa của bảng sau khi phân rã sẽ được lưu trữ chính thức trong Hệ thống ca-ta-lô (`시스템 카탈로그`).

## 읽는 방법 (Cách đọc)
- Học thuộc công thức toán học và vai trò chuẩn hóa ở TẦNG A:
  - $X \rightarrow Y$: $X$ là **결정자** (bên trái mũi tên), $Y$ là **종속자** (bên phải mũi tên).
  - Khử **부분 함수 종속 (Phụ thuộc từng phần)** $\rightarrow$ Đạt **2NF**.
  - Khử **이행적 함수 종속 (Phụ thuộc bắc cầu: $A \rightarrow B, B \rightarrow C \implies A \rightarrow C$)** $\rightarrow$ Đạt **3NF**.

---

## 183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Định nghĩa Phụ thuộc hàm (함수적 종속의 개념):**
  - Trong quan hệ $R$, nếu với mỗi giá trị của thuộc tính $X$ luôn tương ứng với duy nhất một giá trị của thuộc tính $Y$, ta nói rằng **$Y$ phụ thuộc hàm vào $X$**, ký hiệu là:
    $$X \longrightarrow Y$$
  - **$X$ gọi là Yếu tố quyết định (`결정자 / Determinant`):** Thuộc tính đóng vai trò làm điều kiện xác định.
  - **$Y$ gọi là Yếu tố phụ thuộc (`종속자 / Dependent`):** Thuộc tính có giá trị được xác định bởi $X$.
- **2. Bảng phân loại 3 dạng Phụ thuộc hàm cốt lõi:**
  | Dạng phụ thuộc | Thuật ngữ Hàn - Anh | Khái niệm & Cơ chế toán học | Tác động trong Chuẩn hóa |
  |---|---|---|---|
  | **Phụ thuộc hoàn toàn** | `완전 함수 종속` (Full Functional Dependency) | Thuộc tính $Y$ phụ thuộc vào toàn bộ khóa chính $X$, và **không phụ thuộc vào bất kỳ tập con thực sự nào của $X$**. | Điều kiện bắt buộc để đạt **Dạng chuẩn 2 (2NF)**. |
  | **Phụ thuộc từng phần** | `부분 함수 종속` (Partial Functional Dependency) | Thuộc tính $Y$ chỉ phụ thuộc vào **một phần thuộc tính cấu thành khóa chính kết hợp $X$**. | Nguyên nhân gây dị thường ở 1NF; **phải loại bỏ để chuyển từ 1NF lên 2NF**. |
  | **Phụ thuộc bắc cầu** | `이행적 함수 종속` (Transitive Dependency) | Mối quan hệ gián tiếp: Nếu $A \rightarrow B$ và $B \rightarrow C$ (với $B$ không suy ra ngược lại $A$, $C$ không thuộc $B$), dẫn đến $A \rightarrow C$ thông qua trung gian $B$. | Nguyên nhân gây dị thường ở 2NF; **phải loại bỏ để chuyển từ 2NF lên 3NF**. |

- **3. Quy tắc cốt lõi thi trắc nghiệm:**
  - Nếu đề cho chuỗi: $A \rightarrow B$, $B \rightarrow C$, suy ra $A \rightarrow C$ $\rightarrow$ Đây là **이행적 함수 종속 (Phụ thuộc hàm bắc cầu)**.
  - Loại bỏ 부분 함수 종속 để đạt **2NF**.
  - Loại bỏ 이행적 함수 종속 để đạt **3NF**.
  - Loại bỏ 결정자이면서 후보키가 아닌 것 để đạt **BCNF**.
- **주의/함정 (Bẫy đề thi):**
  - Đề hỏi: *"Trong biểu thức $X \rightarrow Y$, $X$ được gọi là gì?"* $\rightarrow$ Đáp án: **결정자 (Yếu tố quyết định / Determinant)**.
  - Đề hỏi: *"Phụ thuộc hàm bắc cầu liên quan trực tiếp đến cấp độ chuẩn hóa nào?"* $\rightarrow$ Đáp án: **제3정규형 (3NF)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa phân biệt trực quan giữa Phụ thuộc hoàn toàn và từng phần:**
  - Xét bảng kết quả học tập có Khóa chính phức hợp gồm 2 cột: `(MaSV, MaMH)`:
    - `(MaSV, MaMH) -> DiemThi`: Điểm thi phụ thuộc vào cả sinh viên và môn học cụ thể $\rightarrow$ **완전 함수 종속 (Phụ thuộc hoàn toàn)**.
    - `MaSV -> TenSV`: Tên sinh viên chỉ cần biết `MaSV` là xác định được, không cần quan tâm đến `MaMH` $\rightarrow$ `TenSV` phụ thuộc vào một phần của khóa $\rightarrow$ **부분 함수 종속 (Phụ thuộc từng phần)**.
- **Minh họa Phụ thuộc bắc cầu:**
  - Bảng nhân viên: `MaNV -> PhongBan` và `PhongBan -> TruongPhong`.
  - Từ mã nhân viên gián tiếp xác định được tên trưởng phòng: `MaNV -> TruongPhong`.
  - Đây là **이행적 함수 종속**. Tách thành 2 bảng để loại bỏ: `NHAN_VIEN (MaNV, PhongBan)` và `PHONG_BAN (PhongBan, TruongPhong)`.

### 복습 체크리스트
- [ ] Phân biệt được vai trò của 결정자 ($X$) và 종속자 ($Y$) trong $X \rightarrow Y$.
- [ ] Định nghĩa chuẩn xác 완전 함수 종속 và 부분 함수 종속.
- [ ] Trình bày được điều kiện của 이행적 함수 종속 ($A \rightarrow B \wedge B \rightarrow C \implies A \rightarrow C$).
- [ ] Nhớ mối liên kết với chuẩn hóa: 2NF khử 부분 종속, 3NF khử 이행 종속.
