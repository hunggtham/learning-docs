# 6. 객체지향 (Hướng Đối Tượng - OOP)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **6. 객체지향 (Hướng Đối Tượng - OOP)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **6. 객체지향 (Hướng Đối Tượng - OOP)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **14. 객체지향 심화 (OOP chuyên sâu)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

객체지향

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **1. 소프트웨어 아키텍처 (Software Architecture)**에서 만든 기준을 이어받아 **6. 객체지향 (Hướng Đối Tượng - OOP)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **6. 객체지향 (Hướng Đối Tượng - OOP)** và nối nó với **14. 객체지향 심화 (OOP chuyên sâu)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 6. 객체지향 (Hướng Đối Tượng - OOP)

Từ **1. 소프트웨어 아키텍처 (Software Architecture)**, ta đã có điểm tựa để bước vào **6. 객체지향 (Hướng Đối Tượng - OOP)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 27/57 trước khi đi vào chi tiết.

Để đọc **6. 객체지향 (Hướng Đối Tượng - OOP)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **031. 메시지 (Message)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 031. 메시지 (Message)

Các ý ngay dưới **031. 메시지 (Message)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 객체에게 어떤 행위를 하도록 지시하는 명령 또는 요구사항이다. (Là lệnh hoặc yêu cầu chỉ thị cho đối tượng thực hiện một hành vi nào đó.)
- 객체들 간에 상호 작용을 하는 데 사용되는 수단이다. (Là phương tiện dùng để tương tác giữa các đối tượng.)

Các bullet của **031. 메시지 (Message)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **031. 메시지 (Message)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **032. 클래스 (Class)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **032. 클래스 (Class)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 032. 클래스 (Class)

Bây giờ ta đi vào nội dung của **032. 클래스 (Class)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 공통된 속성과 연산(행위)을 갖는 객체의 집합이다. (Là tập hợp các đối tượng có chung thuộc tính và phép toán (hành vi).)
- 클래스에 속한 각각의 객체를 인스턴스(Instance)라 한다. (Mỗi đối tượng thuộc một class được gọi là Thực thể - Instance).
- 객체지향 프로그램에서 데이터를 추상화하는 단위이다. (Là đơn vị trừu tượng hóa dữ liệu trong lập trình OOP.)

Các bullet của **032. 클래스 (Class)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **032. 클래스 (Class)**, đừng bắt đầu lại từ số không. **033. 캡슐화 (Encapsulation / Đóng gói)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **033. 캡슐화 (Encapsulation / Đóng gói)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 033. 캡슐화 (Encapsulation / Đóng gói)

Phần nguồn của **033. 캡슐화 (Encapsulation / Đóng gói)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 데이터와 데이터를 처리하는 함수를 하나로 묶는 것을 의미한다. (Việc bó buộc dữ liệu và hàm xử lý dữ liệu đó thành một khối.)
- 외부 모듈의 변경으로 인한 파급 효과가 적다. (Giảm thiểu hiệu ứng lan truyền khi module bên ngoài thay đổi.)
- 인터페이스가 단순화된다. (Giao diện trở nên đơn giản.)
- 재사용이 용이하다. (Dễ dàng tái sử dụng.)
- **Ví dụ (Example):** Một viên thuốc nhộng (capsule) chứa nhiều bột thuốc bên trong, người dùng chỉ việc uống viên nhộng mà không cần biết tỷ lệ bột bên trong.

Các ý về **033. 캡슐화 (Encapsulation / Đóng gói)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

**033. 캡슐화 (Encapsulation / Đóng gói)** vừa cho ta cách đặt câu hỏi. Bây giờ **034. 상속 (Inheritance / Kế thừa)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **034. 상속 (Inheritance / Kế thừa)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 034. 상속 (Inheritance / Kế thừa)

Các ý ngay dưới **034. 상속 (Inheritance / Kế thừa)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 상위 클래스(부모 클래스)의 모든 속성과 연산을 하위 클래스(자식 클래스)가 물려받는 것이다. (Lớp con kế thừa toàn bộ thuộc tính và phương thức của lớp cha.)

Các bullet của **034. 상속 (Inheritance / Kế thừa)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **034. 상속 (Inheritance / Kế thừa)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **035. 다형성 (Polymorphism / Đa hình)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **035. 다형성 (Polymorphism / Đa hình)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 035. 다형성 (Polymorphism / Đa hình)

Bây giờ ta đi vào nội dung của **035. 다형성 (Polymorphism / Đa hình)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 오버로딩 (Overloading - Nạp chồng): 메소드의 이름은 같지만 인수를 받는 자료형과 개수를 달리하여 여러 기능을 정의할 수 있음. (Cùng tên hàm nhưng khác kiểu/số lượng tham số -> Định nghĩa nhiều chức năng).
- 오버라이딩 (Overriding - Ghi đè): 메소드의 이름은 같지만 메소드 안의 실행 코드를 달리하여 자식 클래스에서 재정의해서 사용할 수 있음. (Cùng tên hàm, định nghĩa lại nội dung code ở lớp con).
- **Ví dụ (Example):** Hàm `add(int a, int b)` và `add(float a, float b)` là Overloading. Lớp Mèo `speak()` kêu Meo, lớp Chó `speak()` kêu Gâu là Overriding.

Các ý về **035. 다형성 (Polymorphism / Đa hình)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **035. 다형성 (Polymorphism / Đa hình)**, đừng bắt đầu lại từ số không. **036. 객체지향 분석 방법론 - Coad와 Yourdon 방법** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **036. 객체지향 분석 방법론 - Coad와 Yourdon 방법**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 036. 객체지향 분석 방법론 - Coad와 Yourdon 방법

Phần nguồn của **036. 객체지향 분석 방법론 - Coad와 Yourdon 방법** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- E-R 다이어그램을 사용하여 객체의 행위를 모델링 한다. (Sử dụng biểu đồ E-R để mô hình hóa hành vi đối tượng.)
- 객체 식별, 구조 식별, 주제 정의, 속성과 인스턴스 연결 정의, 연산과 메시지 연결 정의 등의 과정으로 구성하는 기법이다. (Quy trình gồm: Nhận diện đối tượng, Nhận diện cấu trúc, Định nghĩa chủ đề, Định nghĩa thuộc tính/liên kết instance, Định nghĩa phép toán/thông điệp).

Các bullet của **036. 객체지향 분석 방법론 - Coad와 Yourdon 방법** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**036. 객체지향 분석 방법론 - Coad와 Yourdon 방법** vừa cho ta cách đặt câu hỏi. Bây giờ **037. 럼바우(Rumbaugh)의 분석 기법 (Kỹ thuật phân tích của Rumbaugh)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **037. 럼바우(Rumbaugh)의 분석 기법 (Kỹ thuật phân tích của Rumbaugh)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 037. 럼바우(Rumbaugh)의 분석 기법 (Kỹ thuật phân tích của Rumbaugh)

Các ý ngay dưới **037. 럼바우(Rumbaugh)의 분석 기법 (Kỹ thuật phân tích của Rumbaugh)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 객체(Object) 모델링: 정보 모델링이라고도 하며, 객체들 간의 관계를 규정하여 객체 다이어그램으로 표시하는 것. (Mô hình hóa đối tượng/thông tin: Xác định mối quan hệ giữa các đối tượng và hiển thị bằng Object Diagram).
- 동적(Dynamic) 모델링: 상태 다이어그램을 이용하여 객체들 간의 동적인 행위를 표현하는 모델링. (Mô hình hóa động: Thể hiện hành vi động giữa các đối tượng bằng State Diagram).
- 기능(Functional) 모델링: 자료 흐름도를 이용하여 자료 흐름을 표현한 모델링. (Mô hình hóa chức năng: Thể hiện luồng dữ liệu bằng DFD - Data Flow Diagram).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KĐC** (Khách - Động - Cơ): **Không Đợi Chờ** (Khách thể - Động lực - Cơ năng). (O-D-F)

Các bullet của **037. 럼바우(Rumbaugh)의 분석 기법 (Kỹ thuật phân tích của Rumbaugh)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **037. 럼바우(Rumbaugh)의 분석 기법 (Kỹ thuật phân tích của Rumbaugh)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **038. 객체지향 설계 원칙 (SOLID 원칙) (Các nguyên tắc thiết kế OOP)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **038. 객체지향 설계 원칙 (SOLID 원칙) (Các nguyên tắc thiết kế OOP)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 038. 객체지향 설계 원칙 (SOLID 원칙) (Các nguyên tắc thiết kế OOP)

Bây giờ ta đi vào nội dung của **038. 객체지향 설계 원칙 (SOLID 원칙) (Các nguyên tắc thiết kế OOP)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 단일 책임 원칙 (SRP - Single Responsibility Principle): 객체는 단 하나의 책임만 가져야 한다는 원칙. (Mỗi đối tượng chỉ có MỘT trách nhiệm duy nhất.)
- 개방-폐쇄 원칙 (OCP - Open-Closed Principle): 기존의 코드를 변경하지 않고 기능을 추가할 수 있도록 설계해야 한다는 원칙. (Mở cho việc mở rộng, Đóng cho việc sửa đổi.)
- 리스코프 치환 원칙 (LSP - Liskov Substitution Principle): 자식 클래스는 최소한 자신의 부모 클래스에서 가능한 행위는 수행할 수 있어야 한다는 설계 원칙. (Lớp con có thể thay thế hoàn toàn lớp cha mà không làm hỏng logic.)
- 인터페이스 분리 원칙 (ISP - Interface Segregation Principle): 자신이 사용하지 않는 인터페이스와 의존 관계를 맺거나 영향을 받지 않아야 한다는 원칙. (Nên tách nhỏ Interface, không ép client implement những phương thức không dùng tới.)
- 의존 역전 원칙 (DIP - Dependency Inversion Principle): 추상성이 낮은 클래스보다 추상성이 높은 클래스와 의존 관계를 맺어야 한다는 원칙. (Module cấp cao không nên phụ thuộc module cấp thấp, cả 2 nên phụ thuộc vào abstraction/interface.)
- 💡 **Mẹo ghi nhớ (Mnemonic):** Tên các chữ cái đầu tiếng Anh tạo thành chữ **S-O-L-I-D**.

Các bullet của **038. 객체지향 설계 원칙 (SOLID 원칙) (Các nguyên tắc thiết kế OOP)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **038. 객체지향 설계 원칙 (SOLID 원칙) (Các nguyên tắc thiết kế OOP)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **6. 객체지향 (Hướng Đối Tượng - OOP)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **14. 객체지향 심화 (OOP chuyên sâu)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.