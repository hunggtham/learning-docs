# 198. 암호화 심화 (Encryption Deep Dive)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **198. 암호화 심화 (Encryption Deep Dive)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **198. 암호화 심화 (Encryption Deep Dive)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

암호화, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **201-203. 스토리지 시스템 (Storage Systems)**에서 만든 기준을 이어받아 **198. 암호화 심화 (Encryption Deep Dive)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 198. 암호화 심화 (Encryption Deep Dive)

Từ **201-203. 스토리지 시스템 (Storage Systems)**, ta đã có điểm tựa để bước vào **198. 암호화 심화 (Encryption Deep Dive)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 39/55 trước khi đi vào chi tiết.

Để đọc **198. 암호화 심화 (Encryption Deep Dive)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **개인키(비밀키) 암호 방식 (Private/Symmetric Key):** 암호화와 복호화 키가 동일. 단일키, 대칭 암호. (예: DES)
- **공개키 암호 방식 (Public/Asymmetric Key):** 암호화 키는 공개(Public), 복호화 키는 비밀(Secret). 비대칭 암호. (예: RSA)
- **VI (Vietnamese) (Tiếng Việt):** Mã hóa dữ liệu.
  - Khóa cá nhân (Đối xứng): Khóa mã hóa và giải mã giống nhau (DES).
  - Khóa công khai (Bất đối xứng): Khóa mã hóa công khai, khóa giải mã bí mật (RSA).

Điểm chốt của **198. 암호화 심화 (Encryption Deep Dive)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.