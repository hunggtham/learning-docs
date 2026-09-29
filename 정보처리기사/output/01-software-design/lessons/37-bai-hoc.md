# 16. 디자인 패턴 심화 (Design Patterns chuyên sâu)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **4. 디자인 패턴 (Design Patterns - GoF)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

디자인, 패턴, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **8. 디자인 패턴 (Design Patterns)**에서 만든 기준을 이어받아 **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 16. 디자인 패턴 심화 (Design Patterns chuyên sâu)

Ở bước 37/55, **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)** xuất hiện như phần tiếp nối của **8. 디자인 패턴 (Design Patterns)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)

Bây giờ ta đi vào nội dung của **디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **장점 (Ưu điểm):** 범용적 코딩 스타일(구조 파악 용이), 생산성 향상, 개발 시간/비용 절약, 의사소통 원활, 유연한 대처 가능. (Dễ đọc code, tăng năng suất, tiết kiệm chi phí, dễ giao tiếp, dễ đối phó thay đổi).
- **단점 (Nhược điểm):** 초기 투자 비용 부담, 다른 기반(비객체지향)에는 부적합. (Tốn kém thời gian học ban đầu, không hợp cho mô hình không hướng đối tượng).

Các bullet của **디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)

Phần nguồn của **디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- *(Tham khảo lại Mục 8 để biết tên gọi, dưới đây là các đặc điểm từ khóa thường ra thi)*
- **생성 패턴 (5개):**
  - **Abstract Factory:** 인터페이스를 통해 구체적인 클래스에 의존하지 않고 객체 생성. (Tạo đối tượng qua Interface mà không phụ thuộc Class cụ thể).
  - **Builder:** 생성 과정과 표현 방법을 분리. (Tách rời quá trình tạo và cách biểu diễn).
  - **Factory Method:** 상위 클래스는 인터페이스만 정의, 실제 생성은 서브 클래스가. (Lớp cha định nghĩa Interface, lớp con thực sự tạo).
  - **Prototype:** 비용이 큰 경우 복제하여 생성. (Clone khi chi phí tạo mới quá lớn).
  - **Singleton:** 인스턴스가 하나뿐임을 보장. (Đảm bảo chỉ có 1 instance).
- **구조 패턴 (7개):**
  - **Adapter:** 호환성이 없는 클래스들의 인터페이스 변환. (Chuyển đổi interface không tương thích).
  - **Bridge:** 기능(추상층)과 구현(구현부)을 분리. (Tách rời chức năng và phần thực thi).
  - **Composite:** 트리 구조로 구성. (Cấu trúc cây).
  - **Decorator:** 능동적으로 기능들을 확장(덧붙임). (Chủ động mở rộng/thêm tính năng).
  - **Facade:** 통합 인터페이스 제공(Wrapper 객체). (Cung cấp interface tổng hợp).
  - **Flyweight:** 다수의 유사 객체 공유 (메모리 절약). (Chia sẻ nhiều đối tượng giống nhau để tiết kiệm RAM).
  - **Proxy:** 네트워크 연결, 메모리 대용량 객체 접근 등 (인터페이스 역할). (Làm đại diện kết nối mạng, tải đối tượng lớn).

Các bullet của **디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **4. 디자인 패턴 (Design Patterns - GoF)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.