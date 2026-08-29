# 3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

데이터베이스와, 절차형, SQL

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)

| 종류 (Loại) | 설명 (Mô tả) | Ví dụ & Giải thích (VN) |
|---|---|---|
| **트리거 (Trigger)** | 테이블 이벤트(Insert, Update, Delete)에 반응해 **자동**으로 실행되는 작업. (Thực thi tự động khi có sự kiện). | _Ví dụ:_ Khi xóa 1 nhân viên khỏi bảng NhânViên, một trigger tự động lưu thông tin nhân viên đó vào bảng NhanVien_NghiViec (Audit log). |
| **프로시저 (Procedure)** | 어떤 행동을 수행하기 위한 일련의 작업 순서. (Một chuỗi các thao tác lưu sẵn để thực thi chung). | _Ví dụ:_ Một procedure `Tinh_Luong_Thang` chạy cuối tháng để tính lương cho toàn bộ công ty. |
| **사용자 정의 함수 (User-Defined Function)** | 단일 값으로 반환할 수 있도록 수행. (Hàm do người dùng định nghĩa, trả về một giá trị duy nhất). | _Ví dụ:_ Hàm `GET_AGE(ngay_sinh)` tự động tính và trả về tuổi. |

---
