# 핵심 262: 포인터와 포인터 변수 (Pointer)

## 핵심 262: 포인터와 포인터 변수 (Pointer)
Phần “핵심 262: 포인터와 포인터 변수 (Pointer)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 변수의 **메모리 주소**를 저장하는 변수. 동적 메모리(Heap) 접근 시 활용. (Con trỏ: Biến lưu trữ địa chỉ bộ nhớ).
- **기호**:
  - `*`: 포인터 선언 시 사용 (예: `int *p;`). 또는 포인터가 가리키는 주소의 **값(Value)**을 참조할 때 사용 (`*p = 10;`). (Dùng để khai báo con trỏ, hoặc lấy giá trị tại địa chỉ đó).
  - `&`: 특정 변수의 **주소(Address)**를 가져올 때 사용. (Dùng để lấy địa chỉ của biến).
- **Example (KR/VN)**:
  - `int a = 50;` (변수 a 생성 및 50 저장 / Tạo biến a, gán 50).
  - `int *p = &a;` (포인터 p에 a의 주소 저장 / Con trỏ p lưu địa chỉ của a).
  - `*p = 70;` (p가 가리키는 곳(a)의 값을 70으로 변경 / Đổi giá trị tại địa chỉ p trỏ đến thành 70. Lúc này a = 70).
- 💡 **Mẹo ghi nhớ**: `&`(And)는 주소(Address), `*`(Star)는 값(Value)을 가리킨다고 기억하세요.
