# 인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **284 & 294. 구역성 (Locality / Tính cục bộ)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

인터프리터, 언어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **226 - 227. 데이터베이스 접속 기술 (Database Connectivity)**에서 만든 기준을 이어받아 **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)** và nối nó với **284 & 294. 구역성 (Locality / Tính cục bộ)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)

Ở bước 73/78, **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)** xuất hiện như phần tiếp nối của **226 - 227. 데이터베이스 접속 기술 (Database Connectivity)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **개념 (Khái niệm)**, **핵심 키워드 (Từ khóa)**, **시험 포인트 (Điểm thi)**, **한 문장 설명 (Tóm tắt)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### TẦNG A – NOTE NÉN (ÔN / ĐI THI)

Bây giờ ta đi vào nội dung của **TẦNG A – NOTE NÉN (ÔN / ĐI THI)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **개념 (Khái niệm)**: 소스 코드를 컴파일하지 않고 인터프리터(Interpreter)가 한 줄씩 즉시 해석하여 실행하는 프로그래밍 언어. (Ngôn ngữ lập trình dịch và thực thi từng dòng mã nguồn trực tiếp mà không cần biên dịch toàn bộ.)
- **핵심 키워드 (Từ khóa)**: 자바 스크립트 (JavaScript), PHP, 파이썬 (Python), 쉘 스크립트 (Shell script).
- **시험 포인트 (Điểm thi)**: 클라이언트용(Client-side: JS)과 서버용(Server-side: ASP, JSP, PHP) 스크립트 언어를 구분하는 것이 단골 문제. (Phân biệt ngôn ngữ cho Client và Server là câu hỏi thường gặp.)
- **한 문장 설명 (Tóm tắt)**: 컴파일 과정이 없어 수정과 실행 시작이 편리하지만, 반복 실행 성능은 일반적으로 컴파일 방식보다 느릴 수 있다. (Dễ sửa và bắt đầu chạy vì không cần biên dịch trước, nhưng hiệu năng chạy lặp thường có thể chậm hơn kiểu biên dịch.)

Các bullet của **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **TẦNG B – NOTE 보충 (HIỂU SÂU)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **TẦNG B – NOTE 보충 (HIỂU SÂU)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### TẦNG B – NOTE 보충 (HIỂU SÂU)

Phần nguồn của **TẦNG B – NOTE 보충 (HIỂU SÂU)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **자바 스크립트 (JavaScript)**: 웹 브라우저 내에서 동작하며 입력 사항 확인 등 클라이언트 측 제어에 사용. (Chạy trên trình duyệt, kiểm soát phía client như xác thực đầu vào.)
- **PHP**: 서버용 스크립트로 C, Java와 문법이 유사. (Script cho server, cú pháp giống C/Java.)
- **파이썬 (Python)**: 객체지향 지원, 문법이 간단하여 배우기 쉽고 플랫폼 독립적인 대화형 언어. (Hỗ trợ OOP, cú pháp đơn giản, độc lập nền tảng, có tính tương tác.)
- **쉘 스크립트 (Shell Script)**: 유닉스/리눅스의 쉘 명령어를 조합한 관리용. (Kết hợp lệnh shell Linux/Unix để quản trị.)
- **ASP / JSP**: 서버 측 동적 페이지 생성 언어 (ASP의 마이크로소프트, JSP의 자바 기반). (ASP của MS, JSP của Java.)
- **예시 (Ví dụ)**: 브라우저에서 버튼을 누르면 즉시 알림창이 뜨는 JS 코드는 컴파일 없이 바로 실행됨. (Mã JS hiển thị thông báo khi bấm nút trên trình duyệt chạy ngay mà không cần biên dịch.)
- 💡 **Mẹo ghi nhớ**: JS là Client, còn lại PPP (PHP, JSP, ASP) đa số là Server.

Các ý về **TẦNG B – NOTE 보충 (HIỂU SÂU)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Điểm chốt của **TẦNG B – NOTE 보충 (HIỂU SÂU)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **284 & 294. 구역성 (Locality / Tính cục bộ)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.