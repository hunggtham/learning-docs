# 287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

UNIX, 시스템의, 구성

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **285 & 295. 워킹 셋 (Working Set / Tập làm việc)**에서 만든 기준을 이어받아 **287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)

Từ **285 & 295. 워킹 셋 (Working Set / Tập làm việc)**, ta đã có điểm tựa để bước vào **287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 75/77 trước khi đi vào chi tiết.

Để đọc **287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **개념 (Khái niệm)**, **핵심 키워드 (Từ khóa)**, **시험 포인트 (Điểm thi)**, **커널 (Kernel)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### TẦNG A – NOTE NÉN (ÔN / ĐI THI)

Các ý ngay dưới **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **개념 (Khái niệm)**: 커널(Kernel), 쉘(Shell), 유틸리티(Utility)의 계층적 구조. (Cấu trúc phân tầng gồm Kernel, Shell và Utility.)
- **핵심 키워드 (Từ khóa)**: 커널(Kernel - Hạt nhân), 쉘(Shell - Vỏ), 명령어 해석기 (Trình thông dịch lệnh).
- **시험 포인트 (Điểm thi)**: 커널(핵심 및 상주)과 쉘(명령어 해석기 및 인터페이스)의 역할을 명확히 구분. (Phân biệt vai trò của Kernel và Shell.)

Các bullet của **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **TẦNG B – NOTE 보충 (HIỂU SÂU)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **TẦNG B – NOTE 보충 (HIỂU SÂU)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### TẦNG B – NOTE 보충 (HIỂU SÂU)

Bây giờ ta đi vào nội dung của **TẦNG B – NOTE 보충 (HIỂU SÂU)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **커널 (Kernel)**: 하드웨어를 직접 관리, 프로세스/메모리/파일 관리. 주기억장치에 상주. (Quản lý trực tiếp phần cứng, tiến trình, bộ nhớ. Nằm thường trực trong RAM.)
- **쉘 (Shell)**: 사용자의 명령을 인식하여 수행하는 명령어 해석기 (인터페이스). (Trình biên dịch lệnh, nhận lệnh từ người dùng và gọi chương trình.)
- **유틸리티 (Utility)**: 에디터, 컴파일러 등 응용 프로그램. (Các chương trình ứng dụng như trình soạn thảo, biên dịch.)
- **예시 (Ví dụ)**: 식당에서 사용자가 주문(명령)을 하면 종업원(Shell)이 이를 받아 주방장(Kernel)에게 전달하여 요리(하드웨어 제어)를 하는 구조. (Khách hàng gọi món (Lệnh) -> Phục vụ bàn (Shell) -> Đầu bếp (Kernel) xử lý nấu nướng.)
- 💡 **Mẹo ghi nhớ**: Kernel là **Lõi** (Hardware), Shell là **Vỏ** (Giao tiếp người dùng).

Các ý về **TẦNG B – NOTE 보충 (HIỂU SÂU)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Điểm chốt của **TẦNG B – NOTE 보충 (HIỂU SÂU)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.