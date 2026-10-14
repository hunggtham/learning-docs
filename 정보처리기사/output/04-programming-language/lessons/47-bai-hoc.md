# 189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)

## 189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)
Phần “189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **모듈화 (Modularity)**: 시스템을 모듈 단위로 나눔.
- **추상화 (Abstraction)**: 포괄적 개념 먼저 설계 후 세분화 (기능, 제어, 자료 추상화).
- **정보 은닉 (Information Hiding)**: 모듈 내부의 세부 정보를 감추어 다른 모듈이 변경하지 못하게 함 (유지보수 용이).
- **프로그램 구조 (Program Structure)**: 제어 계층 구조 (트리 형태).
  - 공유도(Fan-In): 나를 호출하는 상위 모듈 수.
  - 제어도(Fan-Out): 내가 호출하는 하위 모듈 수.

**Giải thích (Vietnamese):**
Khi thiết kế phần mềm, ta chia nhỏ thành các hàm/chức năng (Modularity). Dùng "Che giấu thông tin" (Information Hiding) như tính đóng gói (Encapsulation) trong OOP để các hàm không can thiệp sai vào dữ liệu của nhau.
- Fan-In (Đi vào): Có bao nhiêu hàm gọi đến mình. Fan-In cao là tốt vì tính tái sử dụng cao.
- Fan-Out (Đi ra): Mình gọi bao nhiêu hàm khác. Fan-Out cao nghĩa là hàm này quá phức tạp.

**💡 Mẹo ghi nhớ (Mnemonics):**
**모추정** (Mô - Trừu - Thông): **모**듈화(Modularity), **추**상화(Abstraction), **정**보 은닉(Information Hiding).

---
