# 6. 객체지향 (Hướng Đối Tượng - OOP)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **6. 객체지향 (Hướng Đối Tượng - OOP)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

객체지향

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 6. 객체지향 (Hướng Đối Tượng - OOP)

### 031. 메시지 (Message)
- 객체에게 어떤 행위를 하도록 지시하는 명령 또는 요구사항이다. (Là lệnh hoặc yêu cầu chỉ thị cho đối tượng thực hiện một hành vi nào đó.)
- 객체들 간에 상호 작용을 하는 데 사용되는 수단이다. (Là phương tiện dùng để tương tác giữa các đối tượng.)

### 032. 클래스 (Class)
- 공통된 속성과 연산(행위)을 갖는 객체의 집합이다. (Là tập hợp các đối tượng có chung thuộc tính và phép toán (hành vi).)
- 클래스에 속한 각각의 객체를 인스턴스(Instance)라 한다. (Mỗi đối tượng thuộc một class được gọi là Thực thể - Instance).
- 객체지향 프로그램에서 데이터를 추상화하는 단위이다. (Là đơn vị trừu tượng hóa dữ liệu trong lập trình OOP.)

### 033. 캡슐화 (Encapsulation / Đóng gói)
- 데이터와 데이터를 처리하는 함수를 하나로 묶는 것을 의미한다. (Việc bó buộc dữ liệu và hàm xử lý dữ liệu đó thành một khối.)
- 외부 모듈의 변경으로 인한 파급 효과가 적다. (Giảm thiểu hiệu ứng lan truyền khi module bên ngoài thay đổi.)
- 인터페이스가 단순화된다. (Giao diện trở nên đơn giản.)
- 재사용이 용이하다. (Dễ dàng tái sử dụng.)
- **Ví dụ (Example):** Một viên thuốc nhộng (capsule) chứa nhiều bột thuốc bên trong, người dùng chỉ việc uống viên nhộng mà không cần biết tỷ lệ bột bên trong.

### 034. 상속 (Inheritance / Kế thừa)
- 상위 클래스(부모 클래스)의 모든 속성과 연산을 하위 클래스(자식 클래스)가 물려받는 것이다. (Lớp con kế thừa toàn bộ thuộc tính và phương thức của lớp cha.)

### 035. 다형성 (Polymorphism / Đa hình)
- 오버로딩 (Overloading - Nạp chồng): 메소드의 이름은 같지만 인수를 받는 자료형과 개수를 달리하여 여러 기능을 정의할 수 있음. (Cùng tên hàm nhưng khác kiểu/số lượng tham số -> Định nghĩa nhiều chức năng).
- 오버라이딩 (Overriding - Ghi đè): 메소드의 이름은 같지만 메소드 안의 실행 코드를 달리하여 자식 클래스에서 재정의해서 사용할 수 있음. (Cùng tên hàm, định nghĩa lại nội dung code ở lớp con).
- **Ví dụ (Example):** Hàm `add(int a, int b)` và `add(float a, float b)` là Overloading. Lớp Mèo `speak()` kêu Meo, lớp Chó `speak()` kêu Gâu là Overriding.

### 036. 객체지향 분석 방법론 - Coad와 Yourdon 방법
- E-R 다이어그램을 사용하여 객체의 행위를 모델링 한다. (Sử dụng biểu đồ E-R để mô hình hóa hành vi đối tượng.)
- 객체 식별, 구조 식별, 주제 정의, 속성과 인스턴스 연결 정의, 연산과 메시지 연결 정의 등의 과정으로 구성하는 기법이다. (Quy trình gồm: Nhận diện đối tượng, Nhận diện cấu trúc, Định nghĩa chủ đề, Định nghĩa thuộc tính/liên kết instance, Định nghĩa phép toán/thông điệp).

### 037. 럼바우(Rumbaugh)의 분석 기법 (Kỹ thuật phân tích của Rumbaugh)
- 객체(Object) 모델링: 정보 모델링이라고도 하며, 객체들 간의 관계를 규정하여 객체 다이어그램으로 표시하는 것. (Mô hình hóa đối tượng/thông tin: Xác định mối quan hệ giữa các đối tượng và hiển thị bằng Object Diagram).
- 동적(Dynamic) 모델링: 상태 다이어그램을 이용하여 객체들 간의 동적인 행위를 표현하는 모델링. (Mô hình hóa động: Thể hiện hành vi động giữa các đối tượng bằng State Diagram).
- 기능(Functional) 모델링: 자료 흐름도를 이용하여 자료 흐름을 표현한 모델링. (Mô hình hóa chức năng: Thể hiện luồng dữ liệu bằng DFD - Data Flow Diagram).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KĐC** (Khách - Động - Cơ): **Không Đợi Chờ** (Khách thể - Động lực - Cơ năng). (O-D-F)

### 038. 객체지향 설계 원칙 (SOLID 원칙) (Các nguyên tắc thiết kế OOP)
- 단일 책임 원칙 (SRP - Single Responsibility Principle): 객체는 단 하나의 책임만 가져야 한다는 원칙. (Mỗi đối tượng chỉ có MỘT trách nhiệm duy nhất.)
- 개방-폐쇄 원칙 (OCP - Open-Closed Principle): 기존의 코드를 변경하지 않고 기능을 추가할 수 있도록 설계해야 한다는 원칙. (Mở cho việc mở rộng, Đóng cho việc sửa đổi.)
- 리스코프 치환 원칙 (LSP - Liskov Substitution Principle): 자식 클래스는 최소한 자신의 부모 클래스에서 가능한 행위는 수행할 수 있어야 한다는 설계 원칙. (Lớp con có thể thay thế hoàn toàn lớp cha mà không làm hỏng logic.)
- 인터페이스 분리 원칙 (ISP - Interface Segregation Principle): 자신이 사용하지 않는 인터페이스와 의존 관계를 맺거나 영향을 받지 않아야 한다는 원칙. (Nên tách nhỏ Interface, không ép client implement những phương thức không dùng tới.)
- 의존 역전 원칙 (DIP - Dependency Inversion Principle): 추상성이 낮은 클래스보다 추상성이 높은 클래스와 의존 관계를 맺어야 한다는 원칙. (Module cấp cao không nên phụ thuộc module cấp thấp, cả 2 nên phụ thuộc vào abstraction/interface.)
- 💡 **Mẹo ghi nhớ (Mnemonic):** Tên các chữ cái đầu tiếng Anh tạo thành chữ **S-O-L-I-D**.
