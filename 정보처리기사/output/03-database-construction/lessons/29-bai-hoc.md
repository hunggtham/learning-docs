# 4. SQL 문법의 종류 (Các loại cú pháp SQL)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **4. SQL 문법의 종류 (Các loại cú pháp SQL)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

SQL, 문법의, 종류

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **4. SQL 문법의 종류 (Các loại cú pháp SQL)** và nối nó với **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 4. SQL 문법의 종류 (Các loại cú pháp SQL)

| 종류 (Loại) | 명령어 (Lệnh) | 설명 & 역할 (Mô tả & Vai trò) | Giải thích (VN) |
|---|---|---|---|
| **DDL** (Data Definition Language) | CREATE, ALTER, DROP, TRUNCATE | 데이터베이스를 **정의**하는 언어, 구조 결정. (Ngôn ngữ định nghĩa dữ liệu - Cấu trúc). | Dùng để Tạo (CREATE), Sửa (ALTER), Xóa hoàn toàn (DROP), hoặc Xóa trắng (TRUNCATE) bảng. Giống như việc xây/đập một ngôi nhà. |
| **DML** (Data Manipulation Language) | SELECT, INSERT, cập nhật (update / 업데이트), DELETE | 저장된 자료를 조회, 삽입, 수정, 삭제. (Ngôn ngữ thao tác dữ liệu - Nội dung). | Dùng để Thêm, Sửa, Xóa, Lấy dữ liệu bên trong bảng. Giống như việc sắp xếp đồ đạc trong nhà. |
| **DCL** (Data Control Language) | GRANT, REVOKE | 데이터 보안과 권한 제어. (Ngôn ngữ điều khiển dữ liệu - Quyền). | Dùng để cấp quyền hoặc thu hồi quyền. |
| **TCL** (Transaction Control Language) | lần ghi nhận (commit / 커밋), quay lui (rollback / 롤백), SAVEPOINT | 트랜잭션의 확정, 취소, 부분 복귀. (Ngôn ngữ điều khiển giao dịch). | Dùng để xác nhận, hoàn tác hoặc đặt điểm khôi phục giao dịch. |

> 💡 **Mẹo ghi nhớ:**
> DDL: **CADT** (Create, Alter, Drop, Truncate - "Cắt" cấu trúc).
> DML: **SUDI** (Select, Update, Delete, Insert - "Sửa đi" dữ liệu).
> DCL: **GR** (Grant, Revoke - "Gác quyền"). TCL: **CRS** (Commit, Rollback, Savepoint - "Chốt/Rút/Save").

---
