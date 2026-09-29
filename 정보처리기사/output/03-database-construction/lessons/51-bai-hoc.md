# 220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

하위, 질의, 트리거, DBMS, 접속, 데이터, 전환

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)**에서 만든 기준을 이어받아 **220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환** và nối nó với **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환

Từ **199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)**, ta đã có điểm tựa để bước vào **220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 51/56 trước khi đi vào chi tiết.

Để đọc **220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **하위 질의 (Subquery):** 조건절에 주어진 질의를 먼저 수행하여 결과를 피연산자로 사용.
- **트리거 (Trigger):** 데이터의 삽입/갱신/삭제 등 이벤트 발생 시 관련 작업이 자동 수행되는 절차형 SQL. DCL 사용 불가.
- **DBMS 접속 기술:** JDBC(Java 표준 API), ODBC(개방형 표준 API), MyBatis(SQL Mapping 프레임워크), ORM(객체와 DB 매핑).
- **데이터 전환 (Data Migration/ETL):** 기존 시스템에서 데이터를 추출(Extraction), 변환(Transformation), 적재(Loading)하는 과정.
- **VI (Vietnamese) (Tiếng Việt):** Truy vấn con, Trigger, Kết nối DBMS & Chuyển đổi dữ liệu.
  - Subquery: Truy vấn lồng nhau.
  - Trigger: Tự động kích hoạt khi có sự kiện (INSERT/UPDATE/DELETE). Không dùng DCL trong Trigger.
  - Kết nối: JDBC (cho Java), ODBC (chuẩn mở), ORM (Ánh xạ đối tượng - quan hệ).
  - ETL: Trích xuất (E), Chuyển đổi (T), Tải (L) dữ liệu sang hệ thống mới.

---

# 3과목 운영체제 (Operating System - 추가 포함된 내용)

Phần **3과목 운영체제 (Operating System - 추가 포함된 내용)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.

---

Điểm chốt của **220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.