# 082. 운영체제 기능 및 종류 (Operating System OS)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **082. 운영체제 기능 및 종류 (Operating System OS)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

운영체제, 기능, 종류

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 082. 운영체제 기능 및 종류 (Operating System OS)
- **운영체제의 주요 프로그램**:
  - **제어 프로그램 (Control Program)**: 감시(Kernel), 작업 제어, 데이터 관리.
  - **처리 프로그램 (Processing Program)**: 언어 번역(컴파일러), 서비스, 문제 프로그램.
- **쉘(Shell)과 커널(Kernel)**:
  - **쉘 (Shell)**: 사용자의 명령어를 해석하여 커널로 전달 (사용자 인터페이스).
  - **커널 (Kernel)**: 핵심 모듈. 하드웨어/메모리/프로세스를 직접 제어 및 관리.
- **운영체제 종류**:
  - **Windows**: GUI, 선점형 멀티태스킹, PnP(자동 감지) 기능.
  - **Linux / Unix**: 오픈소스 (Linux), 트리 구조 파일 시스템. 시분할 시스템.
  - **Unix 파일 시스템 구조**: 부트 블록 -> 슈퍼 블록 (전체 정보) -> 아이노드(i-node) 블록 (파일 메타데이터) -> 데이터 블록 (실제 파일 내용).

**Giải thích (Vietnamese):**
OS giống như quản gia của máy tính.
- Kernel (Hạt nhân) là bộ não xử lý phần cứng. Shell (Vỏ) là cái dòng lệnh hoặc giao diện để con người nói chuyện với bộ não đó.
- Hệ thống tệp của UNIX chia làm 4 phần: Boot (chứa code khởi động) -> Super (Thông tin tổng quan) -> i-node (Lưu tên file, quyền truy cập...) -> Data (Nội dung file thực tế).

**💡 Mẹo ghi nhớ (Mnemonics):**
**제어 프로그램**: 감작데 (감시, 작업, 데이터). / **처리 프로그램**: 언서문 (언어, 서비스, 문제).

---
