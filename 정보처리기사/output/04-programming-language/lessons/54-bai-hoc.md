# 190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)

## 학습 목표 (Mục tiêu)
- Nắm vững các tiêu chuẩn cốt lõi định hình một thiết kế phần mềm tốt, chất lượng cao trong kỹ nghệ phần mềm.
- Thấu hiểu và ghi nhớ nguyên tắc vàng: **Độ phụ thuộc giữa các module phải yếu nhất có thể (Low Coupling / 결합도는 약하게)** và **Độ gắn kết nội tại bên trong từng module phải mạnh nhất có thể (High Cohesion / 응집도는 강하게)**.
- Hiểu các tiêu chí cấu trúc bổ trợ: Kích thước module phù hợp, tính độc lập chức năng, cấu trúc luồng một ngõ vào một ngõ ra (Single Entry, Single Exit) và kiểm soát ảnh hưởng lề (Side Effects).

## 핵심 키워드 (Từ khóa)
- 바람직한 설계 (Good Software Design)
- 약한 결합도 (Low / Loose Coupling)
- 강한 응집도 (High Cohesion)
- 모듈의 독립성 (Module Independence)
- 단일 진입·단일 진출 (Single Entry, Single Exit)
- 유지보수성 (Maintainability) & 재사용성 (Reusability)
- 부작용 제어 (Side Effect Prevention)

## 선행·연결 개념 (Kiến thức liên kết)
- [53-bai-hoc.md](53-bai-hoc.md): Đặc điểm các ngôn ngữ lập trình hướng thủ tục.
- [55-bai-hoc.md](55-bai-hoc.md): Chi tiết 6 cấp độ kết hợp (Coupling) từ tốt đến xấu.
- [56-bai-hoc.md](56-bai-hoc.md): Chi tiết 7 cấp độ gắn kết (Cohesion) từ xấu đến tốt.

## 읽는 방법 (Cách đọc)
- Trong mọi kỳ thi chứng chỉ CNTT, câu hỏi "Đặc điểm nào sau đây KHÔNG PHẢI là thiết kế phần mềm tốt?" luôn xuất hiện thường trực:
  - Khẳng định ĐÚNG: "결합도는 약하게, 응집도는 강하게" (Coupling yếu, Cohesion mạnh).
  - Bẫy SAI thường gặp: Đảo ngược thành "결합도를 강하게" (Coupling mạnh) hoặc "응집도를 약하게" (Cohesion yếu) $\rightarrow$ Tuyệt đối không chọn.
  - Thiết kế module có **1 cổng vào và 1 cổng ra** giúp luồng điều khiển trong sáng, dễ kiểm thử đơn vị và ngăn chặn rò rỉ trạng thái.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Các đặc trưng cốt lõi của một thiết kế phần mềm tối ưu:**

| Tiêu chuẩn thiết kế | Yêu cầu kỹ thuật chi tiết |
| :--- | :--- |
| **Độ phụ thuộc (Coupling)** | **Càng yếu càng tốt (Low Coupling).** Các module giao tiếp qua tham số dữ liệu tối thiểu, không can thiệp biến nội bộ của nhau. |
| **Độ gắn kết (Cohesion)** | **Càng mạnh càng tốt (High Cohesion).** Tất cả các câu lệnh bên trong một module phải cùng tập trung hoàn thành một nhiệm vụ duy nhất. |
| **Tính độc lập (Independence)** | Module có tính tự chủ cao, thay đổi bên trong module này không gây hiệu ứng dây chuyền làm sụp đổ các module khác. |
| **Kích thước module** | Giữ quy mô vừa phải; module quá lớn gây khó hiểu, module quá nhỏ làm bùng nổ chi phí giao tiếp và overhead gọi hàm. |
| **Cấu trúc điều khiển** | Đảm bảo **Single Entry - Single Exit** (Một lối vào, một lối ra), tránh lệnh nhảy tùy tiện (`goto`). |
| **Phạm vi ảnh hưởng** | Phạm vi ảnh hưởng của một quyết định (Scope of Effect) phải nằm gọn bên trong phạm vi kiểm soát (Scope of Control) của module đó. |
| **Tính bảo trì & Tái sử dụng** | Giảm thiểu tối đa chi phí sửa lỗi, thích ứng nhanh với yêu cầu mới và dễ dàng tái sử dụng trong các hệ thống khác. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mối quan hệ giữa Scope of Control (Phạm vi kiểm soát) và Scope of Effect (Phạm vi ảnh hưởng):**
  - *Scope of Control (제어 영역):* Gồm chính module đó và toàn bộ các module con cấp dưới mà nó gọi trực tiếp hoặc gián tiếp.
  - *Scope of Effect (영향 영역):* Là tập hợp tất cả các module có hành vi bị thay đổi dựa trên kết quả quyết định rẽ nhánh logic đưa ra bởi module đó.
  - *Quy tắc thiết kế chuẩn:* **Scope of Effect $\subseteq$ Scope of Control**. Nếu một quyết định logic ở module con lại làm thay đổi hành vi của một module bên ngoài nhánh cây phân cấp (ngoài Scope of Control), thiết kế đó bị coi là vi phạm tính đóng gói và có độ phụ thuộc xấu.

### 복습 체크리스트
- [ ] Khắc sâu nguyên tắc vàng: **결합도는 약하게(낮게), 응집도는 강하게(높게)**.
- [ ] Hiểu rõ tại sao module độc lập cao lại giúp việc bảo trì và kiểm thử trở nên dễ dàng.
- [ ] Nhớ nguyên tắc một ngõ vào một ngõ ra (Single Entry, Single Exit).
- [ ] Nắm vững mối quan hệ Scope of Effect phải nằm bên trong Scope of Control.
