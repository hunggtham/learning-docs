# 4. UML (Unified Modeling Language)

## 학습 목표 (Mục tiêu)
- Nắm trọn vẹn và chuẩn xác 6 mối quan hệ cốt lõi trong UML (`UML 6대 관계`): Liên kết, Tập hợp, Hợp thành, Khái quát hóa, Phụ thuộc và Hiện thực hóa.
- Thuộc nằm lòng các ký hiệu hình học biểu diễn đường nối và đầu mũi tên của từng mối quan hệ để giải quyết câu hỏi nhận diện hình vẽ trong đề thi.
- Phân loại thành thạo các biểu đồ UML thành hai nhóm lớn: Cấu trúc tĩnh (`구조적 다이어그램`) và Hành vi động (`행위적 다이어그램`).

## 핵심 키워드 (Từ khóa)
- 연관 관계 (Quan hệ liên kết / Association / 실선)
- 집약 관계 (Quan hệ tập hợp / Aggregation / 빈 마름모)
- 합성 관계 (Quan hệ hợp thành / Composition / 채워진 마름모)
- 일반화 관계 (Quan hệ khái quát hóa / Generalization / Kế thừa / 빈 삼각 화살표)
- 의존 관계 (Quan hệ phụ thuộc / Dependency / 점선 화살표)
- 실체화 관계 (Quan hệ hiện thực hóa / Realization / Interface / 점선 빈 삼각 화살표)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([11. 모델링 및 다이어그램 심화](15-bai-hoc.md)):** Sau khi xem xét sự khác biệt giữa Aggregation và Composition, bài này mở rộng thành bảng tổng phổ chuẩn hóa 6 mối quan hệ UML.
- **Tiếp nối sang bài sau ([5. UML 구성요소 상세](17-bai-hoc.md)):** Đi sâu vào các ký hiệu truy cập của Class Diagram (`+`, `-`, `#`, `~`) và cấu trúc chi tiết của Use Case cùng Sequence Diagram.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nắm vững bảng đối chiếu đường vẽ (nét liền hay nét đứt, tam giác rỗng hay hình thoi) - đây là câu hỏi hình ảnh ăn điểm trực tiếp trong kỳ thi.
- Đọc TẦNG B để phân biệt sự khác nhau giữa Phụ thuộc (Dependency - ngắn hạn) và Liên kết (Association - dài hạn).

---

## 4. UML (Unified Modeling Language)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp 6 mối quan hệ chuẩn trong UML (UML 6대 관계):**
  1. **연관 관계 (Association - Quan hệ liên kết):**
     - Thể hiện hai hoặc nhiều lớp có mối quan hệ ngữ nghĩa lâu dài với nhau.
     - **Ký hiệu:** Đường **nét liền (실선)**, có thể có mũi tên chỉ hướng đi hoặc không có mũi tên (liên kết hai chiều). Có ghi số lượng tham gia (Multiplicity: `1`, `0..1`, `*`, `1..*`).
  2. **집약 / 집합 관계 (Aggregation - Quan hệ tập hợp):**
     - Mối quan hệ toàn thể - bộ phận ("has-a"), nhưng đối tượng bộ phận có **vòng đời độc lập**.
     - **Ký hiệu:** Đường nét liền có **Hình thoi rỗng (빈 마름모)** gắn ở phía lớp toàn thể.
  3. **합성 / 포함 관계 (Composition - Quan hệ hợp thành):**
     - Mối quan hệ toàn thể - bộ phận chặt chẽ, đối tượng bộ phận có **vòng đời phụ thuộc hoàn toàn** vào lớp toàn thể.
     - **Ký hiệu:** Đường nét liền có **Hình thoi đặc (채워진 마름모)** gắn ở phía lớp toàn thể.
  4. **일반화 관계 (Generalization - Quan hệ khái quát hóa / Kế thừa):**
     - Mối quan hệ "is-a", một lớp con kế thừa toàn bộ thuộc tính và phương thức từ lớp cha tổng quát hơn.
     - **Ký hiệu:** Đường **nét liền (실선)** có **Mũi tên tam giác rỗng (빈 삼각 화살표)** chỉ về phía lớp cha.
  5. **의존 관계 (Dependency - Quan hệ phụ thuộc):**
     - Mối quan hệ ngắn hạn tạm thời; lớp này sử dụng lớp kia làm tham số truyền vào của phương thức hoặc biến cục bộ. Khi lớp được dùng thay đổi, lớp kia bị ảnh hưởng.
     - **Ký hiệu:** Đường **nét đứt (점선)** có **Mũi tên nhọn thông thường (화살표)** chỉ về phía lớp được sử dụng.
  6. **실체화 관계 (Realization - Quan hệ hiện thực hóa):**
     - Mối quan hệ giữa một Interface và một Class cụ thể nhận trách nhiệm cài đặt các phương thức trừu tượng của Interface đó.
     - **Ký hiệu:** Đường **nét đứt (점선)** có **Mũi tên tam giác rỗng (빈 삼각 화살표)** chỉ về phía Interface.
- **Phân loại 13 biểu đồ UML (Ghi nhớ nhanh):**
  - **TĨNH (Cấu trúc - 6 loại):** Class, Object, Component, Deployment, Composite Structure, Package.
  - **ĐỘNG (Hành vi - 7 loại):** Use Case, Sequence, Communication, State, Activity, Interaction Overview, Timing.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Quan hệ kế thừa (일반화) và quan hệ hiện thực hóa (실체화) đều dùng mũi tên tam giác rỗng, khác nhau ở điểm nào?"* -> **일반화 dùng đường nét liền (실선), còn 실체화 dùng đường nét đứt (점선)**.
  - **Bẫy 2:** *"Quan hệ phụ thuộc (의존) dùng đường nét liền hay nét đứt?"* -> **Đường nét đứt (점선)**.
  - **Bẫy 3:** *"Khi một phương thức nhận một đối tượng làm đối số (parameter) ngắn hạn, đó là quan hệ gì?"* -> **의존 관계 (Dependency)**, không phải 연관 (Association).
- **한 문장 설명 (Câu chốt ghi nhớ):** "Kế thừa tam giác rỗng nét liền, Hiện thực tam giác rỗng nét đứt; Phụ thuộc nét đứt mũi tên, Thoi rỗng tập hợp, Thoi đặc hợp thành".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh trực quan qua mã nguồn Java:**
  - **Association (Liên kết dài hạn):** Lưu thành trường dữ liệu (field) của Class:
    ```java
    class Professor {
        private Student student; // Liên kết lâu dài
    }
    ```
  - **Dependency (Phụ thuộc ngắn hạn):** Chỉ xuất hiện trong lời gọi hàm:
    ```java
    class Calculator {
        public int add(Data d) { ... } // Data chỉ là tham số tạm thời
    }
    ```
  - **Generalization (Kế thừa):** Dùng từ khóa `extends`:
    ```java
    class Dog extends Animal { ... } // 일반화 (nét liền tam giác rỗng)
    ```
  - **Realization (Hiện thực hóa Interface):** Dùng từ khóa `implements`:
    ```java
    class Circle implements Shape { ... } // 실체화 (nét đứt tam giác rỗng)
    ```

### 복습 체크리스트
- [ ] Vẽ và nhận diện chính xác ký hiệu của cả 6 mối quan hệ trong UML.
- [ ] Phân biệt được sự khác nhau giữa đường vẽ của 일반화 (nét liền) và 실체화 (nét đứt).
- [ ] Phân biệt được tính chất sống còn giữa 집약 (thoi rỗng) và 합성 (thoi đặc).
- [ ] Nhớ 연관 là liên kết dài hạn, 의존 là phụ thuộc tạm thời ngắn hạn.
