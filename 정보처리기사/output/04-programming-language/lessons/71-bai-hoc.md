# 226 - 227. 데이터베이스 접속 기술 (Database Connectivity)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **226 - 227. 데이터베이스 접속 기술 (Database Connectivity)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

데이터베이스, 접속, 기술

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 226 - 227. 데이터베이스 접속 기술 (Database Connectivity)
- **JDBC (Java DataBase Connectivity)**: **자바(Java)** 프로그램 내에서 데이터베이스(DBMS)에 접속하여 SQL 문을 실행하기 위한 표준 API. 운영체제에 독립적.
- **ODBC (Open DataBase Connectivity)**: 프로그래밍 **언어에 관계없이** (C, C++, VB 등) 다양한 DBMS에 접근할 수 있게 마이크로소프트가 만든 개방형 표준 API.

**Giải thích (Vietnamese):**
- JDBC: Dành riêng cho ngôn ngữ Java.
- ODBC: Mở (Open) cho mọi ngôn ngữ khác, dùng chung thông qua một "người quản lý tài xế" (Driver Manager) để dịch lệnh SQL gửi xuống Database.
