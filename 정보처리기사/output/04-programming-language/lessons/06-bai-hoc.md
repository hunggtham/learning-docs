# 237. 변수명 작성 규칙 (Variable Naming Rules)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **237. 변수명 작성 규칙 (Variable Naming Rules)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **237. 변수명 작성 규칙 (Variable Naming Rules)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **연산자 (Operators)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

변수명, 작성, 규칙

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)**에서 만든 기준을 이어받아 **237. 변수명 작성 규칙 (Variable Naming Rules)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **237. 변수명 작성 규칙 (Variable Naming Rules)** và nối nó với **연산자 (Operators)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 237. 변수명 작성 규칙 (Variable Naming Rules)

Từ **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)**, ta đã có điểm tựa để bước vào **237. 변수명 작성 규칙 (Variable Naming Rules)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 6/78 trước khi đi vào chi tiết.

Để đọc **237. 변수명 작성 규칙 (Variable Naming Rules)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 영문자, 숫자, 밑줄(`_`)의 조합만 가능.
- **첫 글자는 숫자로 시작할 수 없음** (예: `1a` 안됨).
- 공백이나 특수문자(`+`, `-`, `*`, `/`, `@` 등) 사용 금지.
- 예약어(`if`, `for`, `while` 등) 사용 금지.
- 대소문자 엄격히 구분.

**Giải thích (Vietnamese):**
Quy tắc đặt tên biến: Không được bắt đầu bằng số, không có khoảng trắng, không chứa ký tự đặc biệt (trừ dấu gạch dưới `_`), không dùng từ khoá của ngôn ngữ.

---

Điểm chốt của **237. 변수명 작성 규칙 (Variable Naming Rules)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **연산자 (Operators)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.