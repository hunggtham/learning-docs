# 110-114. 키 (Keys)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **110-114. 키 (Keys)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối keys với candidate key, primary key, foreign key và integrity, để định danh bản ghi cùng các quan hệ mà database phải bảo vệ.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **110-114. 키 (Keys)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **110-114. 키 (Keys)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **110-114. 키 (Keys)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

110-114. 키 (Keys)

> **Nối mạch:** Ở chặng này của **110-114. 키 (Keys)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **105. E-R 다이어그램 (E-R Diagram)**에서 만든 기준을 이어받아 **110-114. 키 (Keys)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **110-114. 키 (Keys)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **110-114. 키 (Keys)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **110-114. 키 (Keys)**, **110-114. 키 (Keys)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 110-114. 키 (Keys)

Sau khi đã đặt nền bằng **105. E-R 다이어그램 (E-R Diagram)**, ta chuyển sang **110-114. 키 (Keys)**. Đây là mắt xích 11/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **110-114. 키 (Keys)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “110-114. 키 (Keys)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **후보키 (Candidate Key):** 튜플을 유일하게 식별하는 속성. 유일성과 최소성 만족.
- **기본키 (Primary Key):** 후보키 중 선정된 주키. 중복과 NULL 불가.
- **대체키 (Alternate Key):** 후보키 중 기본키를 제외한 나머지 (보조키).
- **슈퍼키 (Super Key):** 유일성은 만족하지만 최소성은 만족하지 못하는 속성 집합.
- **외래키 (Foreign Key):** 다른 릴레이션의 기본키를 참조하는 속성.
- **VI (Vietnamese) (Tiếng Việt):** Các loại khóa (Keys).
  - Candidate Key (Khóa ứng viên): Định danh duy nhất, thỏa mãn tính duy nhất và tính tối thiểu.
  - Primary Key (Khóa chính): Chọn từ khóa ứng viên, không trùng lặp, không NULL.
  - Alternate Key (Khóa thay thế): Các khóa ứng viên còn lại.
  - Super Key (Siêu khóa): Thỏa mãn tính duy nhất nhưng không tối thiểu.
  - Foreign Key (Khóa ngoại): Thuộc tính tham chiếu đến khóa chính của bảng khác.

Ta có thể khép mục **110-114. 키 (Keys)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **110-114. 키 (Keys)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
