# 202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)

## 202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)
Phần “202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 현실 세계의 개체(Entity)를 기계 부품(Object)처럼 만들어 조립식으로 소프트웨어 개발. 재사용/확장 용이.
- **구성 요소**:
  - **데이터 (Data/Attribute)**: 객체가 가진 정보 (속성, 상태).
  - **연산/메소드 (Method/Operation)**: 데이터를 처리하는 알고리즘/함수.
  - **클래스 (Class)**: 공통 속성/연산을 갖는 객체들의 집합 (틀, Type). 객체를 '인스턴스(Instance)'라고 함.
  - **메시지 (Message)**: 객체 간 상호작용 수단 (명령).
- **주요 기본 원칙**:
  1. **캡슐화 (Encapsulation)**: 데이터와 함수를 하나로 묶음. 재사용 용이, 결합도 낮아짐.
  2. **정보 은닉 (Information Hiding)**: 내부 정보를 숨기고 연산만을 통해 접근 허용 (Side Effect 최소화).
  3. **상속성 (Inheritance)**: 상위 클래스의 속성/연산을 하위 클래스가 물려받음. (다중 상속도 있음).
  4. **추상화 (Abstraction)**: 불필요한 부분 생략, 중요한 부분만 모델화.
  5. **다형성 (Polymorphism)**: 동일한 메시지(메소드명)에 대해 객체마다 다른 응답(기능)을 함.

**Giải thích (Vietnamese):**
OOP (Lập trình hướng đối tượng) giống như trò chơi xếp hình Lego.
- Class: Bản vẽ thiết kế chiếc xe.
- Object (Instance): Chiếc xe thật được lắp ráp.
- Tính đóng gói (Encapsulation): Gói gọn các bộ phận động cơ vào trong vỏ xe.
- Tính đa hình (Polymorphism): Cùng là lệnh "Kêu", con chó kêu "Gâu", con mèo kêu "Meo".

**💡 Mẹo ghi nhớ (Mnemonics):**
**캡정상추다** (Đóng - Ẩn - Kế - Trừu - Đa): 캡슐화, 정보 은닉, 상속성, 추상화, 다형성.

---
