# 071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

보안, 취약성, 식별

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)
- **버퍼 오버플로 (Buffer Overflow)**: 메모리를 다루는 데 오류 발생시켜 덮어쓰는 공격.
- **허상 포인터 (Dangling Pointer)**: 삭제된 객체를 가리키고 있는 포인터 (메모리 보안 위반).
- **FTP 바운스 공격**: FTP 프로토콜 구조 허점 이용.
- **SQL 삽입 (SQL Injection)**: 웹 입력창에 SQL 문법 삽입해 DB 데이터 유출/조작.
- **디렉토리 접근 공격 (Directory Traversal)**: 웹 루트 외 디렉토리 접근 (`../` 문자 사용).
- **포맷 스트링 버그**: `printf()` 등에서 검사되지 않은 입력 통한 공격.
- **코드 인젝션 (Code Injection)**: 유효하지 않은 실행 코드 주입.

**Giải thích (Vietnamese):**
- SQL Injection: Kẻ gian gõ `1' OR '1'='1` vào ô đăng nhập để lừa hệ thống cho phép truy cập.
- Buffer Overflow: Kẻ gian cố tình nhập 100 ký tự vào ô chỉ cho phép 10 ký tự, làm tràn bộ nhớ và sập chương trình.

---
