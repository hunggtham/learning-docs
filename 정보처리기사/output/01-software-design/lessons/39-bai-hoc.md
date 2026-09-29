# 16. 디자인 패턴 심화 (Design Patterns chuyên sâu)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **4. 디자인 패턴 (Design Patterns - GoF)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

디자인, 패턴, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **8. 디자인 패턴 (Design Patterns)**에서 만든 기준을 이어받아 **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)** và nối nó với **4. 디자인 패턴 (Design Patterns - GoF)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 16. 디자인 패턴 심화 (Design Patterns chuyên sâu)

Từ **8. 디자인 패턴 (Design Patterns)**, ta đã có điểm tựa để bước vào **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 39/57 trước khi đi vào chi tiết.

Để đọc **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)

Các ý ngay dưới **디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **장점 (Ưu điểm):** 범용적 코딩 스타일(구조 파악 용이), 생산성 향상, 개발 시간/비용 절약, 의사소통 원활, 유연한 대처 가능. (Dễ đọc code, tăng năng suất, tiết kiệm chi phí, dễ giao tiếp, dễ đối phó thay đổi).
- **단점 (Nhược điểm):** 초기 투자 비용 부담, 다른 기반(비객체지향)에는 부적합. (Tốn kém thời gian học ban đầu, không hợp cho mô hình không hướng đối tượng).

Các bullet của **디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)

Bây giờ ta đi vào nội dung của **디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

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

Điểm chốt của **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **4. 디자인 패턴 (Design Patterns - GoF)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.