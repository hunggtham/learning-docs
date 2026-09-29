# 071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **078. 사용자 정의 함수와 클래스 (User Defined Functions & Classes)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

보안, 취약성, 식별

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **070. 서버개발 프레임워크 (Server Development Framework)**에서 만든 기준을 이어받아 **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)

Sau khi đã đặt nền bằng **070. 서버개발 프레임워크 (Server Development Framework)**, ta chuyển sang **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)**. Đây là mắt xích 56/77 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **버퍼 오버플로 (Buffer Overflow)**, **허상 포인터 (Dangling Pointer)**, **FTP 바운스 공격**, **SQL 삽입 (SQL Injection)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **버퍼 오버플로 (Buffer Overflow)**: 메모리를 다루는 데 오류 발생시켜 덮어쓰는 공격.
- **허상 포인터 (Dangling Pointer)**: 삭제된 객체를 가리키고 있는 포인터 (메모리 보안 위반).
- **FTP 바운스 공격**: FTP 프로토콜 구조 허점 이용.
- **SQL 삽입 (SQL Injection)**: 웹 입력창에 SQL 문법 삽입해 DB 데이터 유출/조작.
- **디렉토리 접근 공격 (Directory Traversal)**: 웹 루트 외 디렉토리 접근 (`../` 문자 사용).
- **포맷 스트링 버그**: `printf()` 등에서 검사되지 않은 입력 통한 공격.
- **코드 인젝션 (Code Injection)**: 유효하지 않은 실행 코드 주입.

**Giải thích (Vietnamese):**
- SQL Injection: Kẻ gian gõ `1' OR '1'='1` vào ô đăng nhập để lừa hệ thống cho phép truy cập.
- Buffer Overflow: Kẻ gian cố tình nhập 100 ký tự vào ô chỉ cho phép 10 ký tự, làm tràn bộ nhớ và sập chương trình.

---

Ta có thể khép mục **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **078. 사용자 정의 함수와 클래스 (User Defined Functions & Classes)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.