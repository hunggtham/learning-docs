# 163-167. 데이터베이스 설계 순서 (Database Design Process)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **163-167. 데이터베이스 설계 순서 (Database Design Process)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **163-167. 데이터베이스 설계 순서 (Database Design Process)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

데이터베이스, 설계, 순서

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **103. 물리적 설계 (Physical Design)**에서 만든 기준을 이어받아 **163-167. 데이터베이스 설계 순서 (Database Design Process)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **163-167. 데이터베이스 설계 순서 (Database Design Process)** và nối nó với **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 163-167. 데이터베이스 설계 순서 (Database Design Process)

Ở bước 4/54, **163-167. 데이터베이스 설계 순서 (Database Design Process)** xuất hiện như phần tiếp nối của **103. 물리적 설계 (Physical Design)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **163-167. 데이터베이스 설계 순서 (Database Design Process)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “163-167. 데이터베이스 설계 순서 (Database Design Process)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **요구 조건 분석 (Requirements Analysis):** 요구 조건 명세서 작성.
- **개념적 설계 (Conceptual Design - 164):** 개념 스키마, E-R 모델, DBMS 독립적.
- **논리적 설계 (Logical Design - 165):** 논리 스키마 설계, 매핑.
- **물리적 설계 (Physical Design - 166):** 물리적 구조 변환, 접근 경로, 저장 레코드 양식 결정.
- **구현 (Implementation):** DDL로 DB 생성.
- **VI (Vietnamese) (Tiếng Việt):** Quy trình thiết kế CSDL.
  - Phân tích yêu cầu -> Thiết kế Khái niệm (E-R) -> Thiết kế Logic (Bảng/Lược đồ logic) -> Thiết kế Vật lý (Lưu trữ) -> Triển khai (Code DDL).
- 💡 **Mẹo ghi nhớ:** Yêu-Khái-Lo-Vật-Cài (Yêu cầu -> Khái niệm -> Logic -> Vật lý -> Cài đặt).

Như vậy, **163-167. 데이터베이스 설계 순서 (Database Design Process)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.