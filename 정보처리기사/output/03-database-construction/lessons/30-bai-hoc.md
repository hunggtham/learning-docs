# 150-155. 데이터 조작어 (DML) 확장 및 조건 연산자

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

데이터, 조작어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 150-155. 데이터 조작어 (DML) 확장 및 조건 연산자
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
