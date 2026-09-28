# 소프트웨어 보안 (Software Security)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **소프트웨어 보안 (Software Security)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

소프트웨어, 보안

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **정보 보안 및 하드웨어 신기술 (Security & HW Tech)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **인증 및 보안 체계 (Authentication & Security System)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **소프트웨어 보안 (Software Security)** và nối nó với **인증 및 보안 체계 (Authentication & Security System)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 소프트웨어 보안 (Software Security)

### 1. 보안 3대 요소 (CIA Triad)
- **기밀성 (Confidentiality)**: 인가된 사용자만 접근 가능 (암호화).
- **무결성 (Integrity)**: 인가된 사용자만 수정 가능 (변조 방지).
- **가용성 (Availability)**: 인가된 사용자는 언제든 사용 가능.
- 기타: 인증(Authentication), 부인 방지(Non-Repudiation).

### 2. Secure SDLC
보안상 안전한 SW 개발을 위해 SDLC(생명주기)에 보안 활동을 추가한 것.
- **방법론**: CLASP(초기 단계 중심), SDL(MS사 개발), Seven Touchpoints(각 단계별 모범사례 적용).

### 3. 주요 보안 약점 및 방어
- **SQL 삽입 (SQL Injection)**: 입력 폼에 SQL 명령어를 넣어 DB를 조작. (방어: 입력값 필터링 및 매개변수화).
- **XSS (크로스사이트 스크립팅)**: 웹페이지에 악성 스크립트를 삽입해 사용자 정보 탈취. (방어: `<, >, &` 등 특수문자 치환).
- **메모리 버퍼 오버플로**: 할당된 메모리 범위를 넘어서 기록하여 오동작 유발.
  - **스택 가드 (Stack Guard)**: 복귀 주소와 변수 사이에 특정 값을 넣어 오버플로를 탐지하는 기술.
- **접근 지정자 (Access Modifier)**: `Public`(모두 접근), `Protected`(패키지+상속), `Default`(같은 패키지), `Private`(클래스 내부만).

💡 **Mẹo ghi nhớ (Mnemonics):**
- 보안 3요소: **C.I.A** (Confidentiality - Integrity - Availability).
- 접근 한정자: **P.P.D.P** (Public - Protected - Default - Private).
