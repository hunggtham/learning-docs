# 093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

단위, 모듈, 명세서

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 031: 모듈 구현 (Module Implementation)**에서 만든 기준을 이어받아 **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)

Ở bước 19/95, **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)** xuất hiện như phần tiếp nối của **핵심 031: 모듈 구현 (Module Implementation)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **단위 모듈 (Unit Module)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **단위 모듈 (Unit Module)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 단위 모듈 (Unit Module)

Bây giờ ta đi vào nội dung của **단위 모듈 (Unit Module)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 프로그램의 단위 기능을 구현하는 독립적인 최소 소프트웨어 단위. (Đơn vị phần mềm nhỏ nhất, độc lập, thực hiện 1 chức năng duy nhất).

Các bullet của **단위 모듈 (Unit Module)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **단위 모듈 (Unit Module)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)

Phần nguồn của **단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **추상화 (Abstraction):** 복잡한 시스템을 단순하게 구현. (Trừu tượng hóa - ẩn đi sự phức tạp).
- **구조화 (Structuring):** 대형 시스템을 분해하여 단위 기능별로 구분, 계층적으로 구성. (Cấu trúc hóa - chia nhỏ thành sơ đồ hình cây).
- **정보 은닉 (Information Hiding):** 한 모듈 내의 정보가 다른 모듈에 영향을 주지 않도록 숨김. (Che giấu thông tin - dùng biến private để tránh đụng độ).

Các bullet của **단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)**, đừng bắt đầu lại từ số không. **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)

Các ý ngay dưới **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **입·출력 구현:** Nhận Input, trả Output. Chú ý liên kết giao diện (CLI/GUI) hoặc dùng Open Source API để kết nối mạng.
- **알고리즘 구현:** Viết code xử lý logic bên trong (Process) sau khi đã có I/O.

---

Các bullet của **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.