# 283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

운영체제, 구성, UNIX, 시스템

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **282. 운영체제의 정의 및 목적 (Definition & Purpose of OS)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)** và nối nó với **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)
- **운영체제 구성**:
  - **제어 프로그램**: 감시(Supervisor, 핵심), 작업 제어, 데이터 관리.
  - **처리 프로그램**: 언어 번역(컴파일러), 서비스(유틸리티).
- **UNIX의 특징**: 대화식 운영체제, **C언어로 작성**되어 이식성이 높음. 트리(Tree) 구조의 파일 시스템.
  - **커널(Kernel)**: UNIX의 핵심. 하드웨어/메모리/프로세스 관리.
  - **쉘(Shell)**: 사용자의 명령어를 해석하여 커널에 전달하는 인터페이스.
- **파일 디스크립터 (File Descriptor)**: 프로세스가 열린 파일을 참조할 때 사용하는 정수 핸들이다. 파일 속성을 담는 FCB/inode와 동일한 제어 블록이 아니다.
- **UNIX 환경 변수**: `$HOME`(홈 디렉터리), `$PATH`(명령어 검색 경로), `$PWD`(현재 작업 폴더).
- **UNIX 명령어**: `chmod`(권한 변경), `fork`(프로세스 복제).

**Giải thích (Vietnamese):**
- Kernel là não bộ, Shell là lớp vỏ giao tiếp với người dùng.
- Lệnh `fork` trong Unix dùng để nhân bản một tiến trình (process / 프로세스) đang chạy thành một tiến trình (process / 프로세스) con mới.

---
