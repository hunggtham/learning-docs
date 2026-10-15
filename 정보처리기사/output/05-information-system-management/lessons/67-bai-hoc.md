# 5과목 정보시스템 구축 관리 (Quản trị Xây dựng Hệ thống Thông tin)

## 학습 목표 (Mục tiêu)
- Nắm vững bức tranh tổng quan của Môn 5 (Quản trị Xây dựng Hệ thống Thông tin) trong kỳ thi Kỹ sư xử lý thông tin.
- Phân biệt bản chất và trọng tâm của 5 phương pháp luận phát triển phần mềm kinh điển: Cấu trúc (구조적), Kỹ nghệ thông tin (정보공학), Hướng đối tượng (객체지향), Dựa trên linh kiện (CBD), và Linh hoạt (애자일 - Agile).
- Hiểu rõ sự kết nối chiến lược giữa Tái sử dụng phần mềm (Software Reuse) và Tái kỹ nghệ phần mềm (Software Reengineering) trong việc tối ưu hóa chi phí vòng đời hệ thống.

## 핵심 키워드 (Từ khóa)
- **구조적 방법론 (Structured)**: Lấy tiến trình xử lý (Process) làm trung tâm, chia để trị (Divide and Conquer), DFD/DD.
- **정보공학 방법론 (Information Engineering)**: Lấy dữ liệu (Data) làm trung tâm, lập kế hoạch chiến lược thông tin toàn doanh nghiệp, ERD/CRUD.
- **CBD 방법론 (Component-Based Development)**: Lắp ghép các linh kiện phần mềm có sẵn, tái sử dụng tối đa, mở rộng linh hoạt.
- **애자일 (Agile)**: Thích ứng nhanh với thay đổi, chu kỳ ngắn (Sprint), Scrum, XP (eXtreme Programming).
- **재사용 & 재공학**: Tái sử dụng linh kiện đã kiểm chứng và cải tạo mã nguồn hệ thống cũ để kéo dài tuổi thọ.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [01-bai-hoc.md](01-bai-hoc.md) (Phương pháp luận phát triển phần mềm chi tiết).
- Liên kết với [68-bai-hoc.md](68-bai-hoc.md) (Hoạt động tái sử dụng và tái kỹ nghệ chi tiết).
- Liên kết với [69-bai-hoc.md](69-bai-hoc.md) (Công cụ tự động hóa công nghệ phần mềm CASE).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh trọng tâm của các phương pháp luận:
  - Cứ thấy "처리(Process) 중심", "Top-Down", "DFD" $\rightarrow$ Chọn **구조적 방법론 (Structured)**.
  - Cứ thấy "자료(Data) 중심", "Doanh nghiệp quy mô lớn", "ERD/CRUD" $\rightarrow$ Chọn **정보공학 방법론 (Information Engineering)**.
  - Cứ thấy "소프트웨어 부품(블록) 조합", "독립적 컴포넌트" $\rightarrow$ Chọn **CBD 방법론**.
  - Cứ thấy "스프린트", "변화에 민첩한 대응", "고객 소통" $\rightarrow$ Chọn **애자일 (Agile)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng so sánh 5 Phương pháp luận Phát triển Phần mềm
| Phương pháp luận (KR / EN) | Trọng tâm thiết kế | Nguyên lý cốt lõi | Công cụ mô hình hóa tiêu biểu |
| :--- | :--- | :--- | :--- |
| **구조적 방법론 / (Structured)** | **Xử lý / Tiến trình (Process)** | Chia nhỏ bài toán từ trên xuống dưới theo nguyên lý "Chia để trị" (Divide and Conquer) | Biểu đồ luồng dữ liệu (DFD), Từ điển dữ liệu (DD), Mini-spec |
| **정보공학 방법론 / (Information Engineering)** | **Dữ liệu (Data)** | Mô hình hóa cấu trúc dữ liệu toàn diện của doanh nghiệp trước khi phát triển các hàm xử lý | Sơ đồ quan hệ thực thể (ERD), Ma trận CRUD |
| **객체지향 방법론 / (Object-Oriented)** | **Đối tượng (Object)** | Đóng gói thực thể gồm dữ liệu (Thuộc tính) và hàm xử lý (Phương thức) thành các lớp | Ngôn ngữ mô hình hóa thống nhất (UML: Use Case, Class, Sequence) |
| **컴포넌트 기반 방법론 / (CBD - Component-Based)** | **Linh kiện (Component)** | Lắp ghép và phối hợp các linh kiện phần mềm độc lập đã được kiểm chứng chất lượng | Kiến trúc phần mềm (Software Architecture), Giao diện Interface |
| **애자일 방법론 / (Agile)** | **Con người & Sự thích ứng** | Phát triển lặp đi lặp lại theo chu kỳ ngắn, liên tục giao tiếp với khách hàng và chào đón sự thay đổi | Bảng Kanban, Biểu đồ Burndown, User Stories |

#### 2. Chiến lược Tái sử dụng và Tái kỹ nghệ phần mềm
- **소프트웨어 재사용 (Software Reuse)**:
  - Tận dụng lại các module, thư viện, kiến trúc thiết kế đã thành công từ các dự án trước.
  - Mang lại lợi ích giảm thiểu rủi ro, rút ngắn từ 30% đến 50% thời gian phát triển và nâng cao độ tin cậy của phần mềm mới.
- **소프트웨어 재공학 (Software Reengineering)**:
  - Cải tiến và tái cấu trúc hệ thống phần mềm cũ (Legacy) để nâng cao khả năng bảo trì và khả năng tương thích với hạ tầng mới.
  - Phân định rõ: Tái kỹ nghệ **không phải là việc thêm mới chức năng kinh doanh**, mà là nâng cấp "sức khỏe" nội tại của mã nguồn để giảm chi phí bảo trì hàng năm.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sự chuyển dịch mô hình phát triển phần mềm qua các thời kỳ
```
[Thập niên 70: Cấu trúc (Structured)] ──► "Tôi muốn chương trình thực hiện bước 1, 2, 3..."
                   │
                   ▼
[Thập niên 80: Thông tin (Information)] ──► "Tôi muốn thiết kế toàn bộ cơ sở dữ liệu doanh nghiệp..."
                   │
                   ▼
[Thập niên 90: Hướng đối tượng (OOP)] ──► "Tôi muốn tạo các đối tượng tự quản lý dữ liệu của chính mình..."
                   │
                   ▼
[Thập niên 2000: Linh kiện (CBD)] ──► "Tôi muốn lắp ráp các mảnh ghép đã hoàn thiện sẵn..."
                   │
                   ▼
[Hiện đại: Linh hoạt (Agile & DevOps)] ──► "Tôi muốn giao sản phẩm nhỏ nhanh chóng và cập nhật liên tục!"
```

---

### 복습 체크리스트
- [ ] Sự khác biệt trọng tâm giữa phương pháp luận Cấu trúc (Structured) và Kỹ nghệ thông tin (Information Engineering) là gì?
- [ ] Phương pháp luận CBD (Component-Based Development) mang lại lợi ích gì nổi trội nhất trong quá trình bảo trì hệ thống?
- [ ] Bốn giá trị cốt lõi của Tuyên ngôn Agile (Agile Manifesto) ưu tiên những yếu tố nào hơn quy trình truyền thống?
- [ ] Mục tiêu chính của hoạt động Tái kỹ nghệ phần mềm (Software Reengineering) là gì?
