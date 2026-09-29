# 106-107. 튜플(Tuple)과 속성(Attribute)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **106-107. 튜플(Tuple)과 속성(Attribute)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **106-107. 튜플(Tuple)과 속성(Attribute)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **108. 도메인 (Domain)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

튜플

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**에서 만든 기준을 이어받아 **106-107. 튜플(Tuple)과 속성(Attribute)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **106-107. 튜플(Tuple)과 속성(Attribute)** và nối nó với **108. 도메인 (Domain)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 106-107. 튜플(Tuple)과 속성(Attribute)

Ở bước 43/56, **106-107. 튜플(Tuple)과 속성(Attribute)** xuất hiện như phần tiếp nối của **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **106-107. 튜플(Tuple)과 속성(Attribute)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **튜플 (Tuple):** 릴레이션을 구성하는 행(Row). 튜플의 수 = 카디널리티 (Cardinality).
- **속성 (Attribute):** 데이터베이스를 구성하는 가장 작은 논리적 단위. 열(Column). 속성의 수 = 디그리 (Degree).
- **VI (Vietnamese) (Tiếng Việt):** Tuple (Hàng) và Attribute (Cột).
  - Tuple: Hàng. Số hàng = Cardinality.
  - Attribute: Cột, đơn vị logic nhỏ nhất. Số cột = Degree.
- **Example:** 학생 테이블의 '홍길동' 데이터 한 줄이 튜플, '이름', '학번' 열이 속성. / Một dòng dữ liệu 'Hong Gil-dong' là Tuple, các cột 'Tên', 'Mã SV' là Attribute.
- 💡 **Mẹo ghi nhớ:** Tu-Car (Tuple = Cardinality), At-De (Attribute = Degree).

Như vậy, **106-107. 튜플(Tuple)과 속성(Attribute)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **108. 도메인 (Domain)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.