# 204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)

## 204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)
Phần “204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **객체지향 분석**: 사용자의 요구사항을 분석하여 클래스(객체), 속성, 연산, 관계 등을 정의하는 작업.
- **분석 방법론**:
  - **Booch**: 미시적/거시적 개발 프로세스 모두 사용.
  - **Jacobson**: Use Case 강조.
  - **Coad/Yourdon**: E-R 다이어그램 사용.
  - **Wirfs-Brock**: 분석과 설계 간 구분 없음.
- **🌟 럼바우(Rumbaugh)의 분석 기법 (객체 모델링 기법, OMT)**:
  - 분석 순서: **객동기** (객체 -> 동적 -> 기능).
  1. **객체 모델링 (Object Modeling)**: 객체 식별, 구조 및 관계 규정 (객체 다이어그램 / 정보 모델링).
  2. **동적 모델링 (Dynamic Modeling)**: 시간 흐름에 따른 상태 변화, 제어 흐름 표현 (상태도).
  3. **기능 모델링 (Functional Modeling)**: 데이터 흐름을 중심으로 처리 과정 표현 (자료 흐름도, DFD).

**Giải thích (Vietnamese):**
Phương pháp phân tích của Rumbaugh là kinh điển nhất trong thi. Gồm 3 bước:
1. Object (Khách hàng, Tài khoản).
2. Dynamic (Tài khoản từ Đang mở -> Bị khóa khi nhập sai pass 3 lần).
3. Functional (Dữ liệu tiền chạy từ hệ thống ra ATM như thế nào).

**💡 Mẹo ghi nhớ (Mnemonics):**
**객동기** (Khách - Động - Cơ): **객**체(Object) -> **동**적(Dynamic) -> **기**능(Functional).

---
