# 150-155. 데이터 조작어 (DML) 확장 및 조건 연산자

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **193. 뷰 (View)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

데이터, 조작어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**에서 만든 기준을 이어받아 **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자** và nối nó với **193. 뷰 (View)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 150-155. 데이터 조작어 (DML) 확장 및 조건 연산자

Từ **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**, ta đã có điểm tựa để bước vào **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 30/54 trước khi đi vào chi tiết.

Để đọc **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “150-155. 데이터 조작어 (DML) 확장 및 조건 연산자” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **DELETE (150):** 튜플을 삭제. `DELETE FROM 테이블명 [WHERE 조건];`
- **UPDATE (151):** 튜플 내용 변경. `UPDATE 테이블명 SET 속성명 = 데이터 [WHERE 조건];`
- **SELECT (152, 153):** 데이터 검색. `SELECT [DISTINCT] 속성명 FROM 테이블명 [WHERE] [GROUP BY] [HAVING] [ORDER BY ASC|DESC];`
- **LIKE (154):** 문자 패턴 일치 검색.
  - `%`: 모든 문자
  - `_`: 문자 하나
  - `#`: 숫자 하나
- **BETWEEN (155):** 두 숫자 사이의 값 검색.
- **VI (Vietnamese) (Tiếng Việt):** Mở rộng DML và toán tử điều kiện.
  - DELETE: Xóa dữ liệu (hàng).
  - UPDATE: Cập nhật dữ liệu.
  - SELECT: Truy vấn dữ liệu (DISTINCT: Loại bỏ trùng lặp).
  - LIKE: Tìm kiếm theo mẫu ký tự. `%` đại diện cho chuỗi, `_` đại diện 1 ký tự, `#` đại diện 1 số.
  - BETWEEN: Trong khoảng giá trị.
- **Example:** `SELECT * FROM 학생 WHERE 이름 LIKE '김%';` / Tìm tất cả sinh viên có tên bắt đầu bằng họ 'Kim' (김).

Điểm chốt của **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **193. 뷰 (View)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.