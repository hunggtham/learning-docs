# 204-219. SQL 명령어 심화 (SQL Commands Detail)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **204-219. SQL 명령어 심화 (SQL Commands Detail)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **204-219. SQL 명령어 심화 (SQL Commands Detail)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

SQL, 명령어, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **143-145. SQL 분류 (SQL Categories)**에서 만든 기준을 이어받아 **204-219. SQL 명령어 심화 (SQL Commands Detail)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 204-219. SQL 명령어 심화 (SQL Commands Detail)

Từ **143-145. SQL 분류 (SQL Categories)**, ta đã có điểm tựa để bước vào **204-219. SQL 명령어 심화 (SQL Commands Detail)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 27/55 trước khi đi vào chi tiết.

Để đọc **204-219. SQL 명령어 심화 (SQL Commands Detail)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **DDL (204, 207-209):** , , .
  -  옵션:  (참조하는 모든 개체 연쇄 제거),  (참조 중이면 제거 취소).
- **DML (205, 214-218):** , , , .
  - : 중복 튜플 제거.
  - : 정렬 (오름차순/내림차순).
- **DCL (206, 210-213):** , , , .
  - : 권한 부여. (옵션: 남에게 권한 부여 가능).
  - : 권한 회수.
  - : 변경 내용을 DB에 영구 반영.
  - : 변경 취소, 이전 상태로 복구.
- **VI (Vietnamese) (Tiếng Việt):** Chi tiết các lệnh SQL.
  - : Xóa dây chuyền các phần phụ thuộc. : Không cho xóa nếu đang bị phụ thuộc.
  - : Cấp quyền và cho phép người đó cấp quyền tiếp cho người khác.
  - : Xác nhận lưu thay đổi. : Hoàn tác.

Điểm chốt của **204-219. SQL 명령어 심화 (SQL Commands Detail)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.