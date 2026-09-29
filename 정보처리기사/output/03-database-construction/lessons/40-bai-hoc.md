# 198. 암호화 심화 (Encryption Deep Dive)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **198. 암호화 심화 (Encryption Deep Dive)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **198. 암호화 심화 (Encryption Deep Dive)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

암호화, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **201-203. 스토리지 시스템 (Storage Systems)**에서 만든 기준을 이어받아 **198. 암호화 심화 (Encryption Deep Dive)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **198. 암호화 심화 (Encryption Deep Dive)** và nối nó với **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 198. 암호화 심화 (Encryption Deep Dive)

Ở bước 40/56, **198. 암호화 심화 (Encryption Deep Dive)** xuất hiện như phần tiếp nối của **201-203. 스토리지 시스템 (Storage Systems)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **198. 암호화 심화 (Encryption Deep Dive)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **개인키(비밀키) 암호 방식 (Private/Symmetric Key):** 암호화와 복호화 키가 동일. 단일키, 대칭 암호. (예: DES)
- **공개키 암호 방식 (Public/Asymmetric Key):** 암호화 키는 공개(Public), 복호화 키는 비밀(Secret). 비대칭 암호. (예: RSA)
- **VI (Vietnamese) (Tiếng Việt):** Mã hóa dữ liệu.
  - Khóa cá nhân (Đối xứng): Khóa mã hóa và giải mã giống nhau (DES).
  - Khóa công khai (Bất đối xứng): Khóa mã hóa công khai, khóa giải mã bí mật (RSA).

Như vậy, **198. 암호화 심화 (Encryption Deep Dive)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.