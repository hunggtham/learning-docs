# 087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

환경변수와, 스크립트, 명령어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)
- **환경변수 명령어**:
  - `printenv`: 단일 변수 반환.
  - `env`: 환경 변수 출력/설정.
  - `set` / `setenv`: 변수 추가/업데이트.
  - `export`: 변수를 전역(Global) 변수로 변경 (export 안하면 현재 쉘에만 국한됨).
- **운영체제별 주요 명령어 (Windows / Unix(Linux))**:
  - 목록 보기: `dir` / `ls`
  - 복사: `copy` / `cp`
  - 삭제: `del` / `rm`
  - 이름 변경/이동: `ren`, `move` / `mv`
  - 폴더 생성: `md` / `mkdir`
  - 기타 Unix 명령어:
    - `chmod`: 권한 변경. / `chown`: 소유자 변경.
    - `cat`: 파일 내용 출력.
    - `grep`: 문자열(패턴) 검색 (Windows의 `find`).
    - `ps`: 프로세스 상태. / `kill`: 프로세스 종료.
    - `tar`: 파일 묶기/풀기. / `crontab`: 스케줄링.

**Giải thích (Vietnamese):**
- Lệnh `export` rất hay dùng trong Linux để set biến môi trường (Ví dụ: `export PATH=...`) để các chương trình khác cũng đọc được biến đó.
- Các lệnh Linux kinh điển: `ls` (list - liệt kê), `cp` (copy), `rm` (remove), `mv` (move), `mkdir` (make directory), `grep` (tìm text).

---
