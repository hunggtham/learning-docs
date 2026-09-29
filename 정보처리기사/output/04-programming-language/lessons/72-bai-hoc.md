# 226 - 227. 데이터베이스 접속 기술 (Database Connectivity)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **226 - 227. 데이터베이스 접속 기술 (Database Connectivity)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **226 - 227. 데이터베이스 접속 기술 (Database Connectivity)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

데이터베이스, 접속, 기술

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **281. 매시업과 SOA (SW Related Terms: Mashup & SOA)**에서 만든 기준을 이어받아 **226 - 227. 데이터베이스 접속 기술 (Database Connectivity)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **226 - 227. 데이터베이스 접속 기술 (Database Connectivity)** và nối nó với **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 226 - 227. 데이터베이스 접속 기술 (Database Connectivity)

Từ **281. 매시업과 SOA (SW Related Terms: Mashup & SOA)**, ta đã có điểm tựa để bước vào **226 - 227. 데이터베이스 접속 기술 (Database Connectivity)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 72/78 trước khi đi vào chi tiết.

Để đọc **226 - 227. 데이터베이스 접속 기술 (Database Connectivity)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **JDBC (Java DataBase Connectivity)**, **ODBC (Open DataBase Connectivity)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **JDBC (Java DataBase Connectivity)**: **자바(Java)** 프로그램 내에서 데이터베이스(DBMS)에 접속하여 SQL 문을 실행하기 위한 표준 API. 운영체제에 독립적.
- **ODBC (Open DataBase Connectivity)**: 프로그래밍 **언어에 관계없이** (C, C++, VB 등) 다양한 DBMS에 접근할 수 있게 마이크로소프트가 만든 개방형 표준 API.

**Giải thích (Vietnamese):**
- JDBC: Dành riêng cho ngôn ngữ Java.
- ODBC: Mở (Open) cho mọi ngôn ngữ khác, dùng chung thông qua một "người quản lý tài xế" (Driver Manager) để dịch lệnh SQL gửi xuống Database.

Điểm chốt của **226 - 227. 데이터베이스 접속 기술 (Database Connectivity)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.