# 093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

단위, 모듈, 명세서

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 031: 모듈 구현 (Module Implementation)**에서 만든 기준을 이어받아 **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)** và nối nó với **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)

Từ **핵심 031: 모듈 구현 (Module Implementation)**, ta đã có điểm tựa để bước vào **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 33/101 trước khi đi vào chi tiết.

Để đọc **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **단위 모듈 (Unit Module)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 단위 모듈 (Unit Module)

Các ý ngay dưới **단위 모듈 (Unit Module)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “단위 모듈 (Unit Module)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 프로그램의 단위 기능을 구현하는 독립적인 최소 소프트웨어 단위. (Đơn vị phần mềm nhỏ nhất, độc lập, thực hiện 1 chức năng duy nhất).

Các bullet của **단위 모듈 (Unit Module)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **단위 모듈 (Unit Module)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)

Bây giờ ta đi vào nội dung của **단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **추상화 (Abstraction):** 복잡한 시스템을 단순하게 구현. (Trừu tượng hóa - ẩn đi sự phức tạp).
- **구조화 (Structuring):** 대형 시스템을 분해하여 단위 기능별로 구분, 계층적으로 구성. (Cấu trúc hóa - chia nhỏ thành sơ đồ hình cây).
- **정보 은닉 (Information Hiding):** 한 모듈 내의 정보가 다른 모듈에 영향을 주지 않도록 숨김. (Che giấu thông tin - dùng biến private để tránh đụng độ).

Các bullet của **단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)**, đừng bắt đầu lại từ số không. **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)

Phần nguồn của **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **입·출력 구현:** Nhận Input, trả Output. Chú ý liên kết giao diện (CLI/GUI) hoặc dùng Open Source API để kết nối mạng.
- **알고리즘 구현:** Viết code xử lý logic bên trong (Process) sau khi đã có I/O.

---

Các bullet của **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.