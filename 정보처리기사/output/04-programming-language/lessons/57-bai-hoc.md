# 071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **078. 사용자 정의 함수와 클래스 (User Defined Functions & Classes)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

보안, 취약성, 식별

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **소프트웨어 공학 (Software Engineering)**에서 만든 기준을 이어받아 **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)** và nối nó với **078. 사용자 정의 함수와 클래스 (User Defined Functions & Classes)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)

Từ **소프트웨어 공학 (Software Engineering)**, ta đã có điểm tựa để bước vào **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 57/78 trước khi đi vào chi tiết.

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

Điểm chốt của **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **078. 사용자 정의 함수와 클래스 (User Defined Functions & Classes)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.