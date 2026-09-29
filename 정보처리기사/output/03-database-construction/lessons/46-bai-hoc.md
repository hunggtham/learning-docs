# 186. 시스템 카탈로그 (System Catalog)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **186. 시스템 카탈로그 (System Catalog)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **186. 시스템 카탈로그 (System Catalog)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **190. CRUD 분석** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

시스템, 카탈로그

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)**에서 만든 기준을 이어받아 **186. 시스템 카탈로그 (System Catalog)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 186. 시스템 카탈로그 (System Catalog)

Ở bước 46/55, **186. 시스템 카탈로그 (System Catalog)** xuất hiện như phần tiếp nối của **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **186. 시스템 카탈로그 (System Catalog)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- DBMS의 객체(테이블, 뷰 등) 정보를 포함하는 시스템 데이터베이스. (데이터 사전, 메타 데이터)
- 사용자가 조회는 가능하나 직접 갱신(INSERT/UPDATE/DELETE)은 불가 (시스템 자동 갱신).
- **VI (Vietnamese) (Tiếng Việt):** Danh mục hệ thống (System Catalog / Data Dictionary).
  - Chứa thông tin (metadata) về các đối tượng trong DB.
  - Người dùng có thể xem (SELECT) nhưng KHÔNG thể sửa đổi trực tiếp.

Như vậy, **186. 시스템 카탈로그 (System Catalog)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **190. CRUD 분석**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.