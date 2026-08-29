# 085. 프로세스 및 스레드 (Process & Thread)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **085. 프로세스 및 스레드 (Process & Thread)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

프로세스, 스레드

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 085. 프로세스 및 스레드 (Process & Thread)
- **프로세스 상태 (Process States)**: 생성(Create) -> 준비(Ready) -> 실행(Running) -> 대기(Wait/Block) -> 종료(Exit).
- **상태 전이 (State Transitions)**:
  - **Dispatch**: 준비 -> 실행 (CPU 할당받음, 문맥교환 발생).
  - **Timeout (Timer Runout)**: 실행 -> 준비 (할당된 시간 초과).
  - **Block**: 실행 -> 대기 (I/O 작업 요청).
  - **Wake Up**: 대기 -> 준비 (I/O 작업 완료).
- **PCB (Process Control Block)**: OS가 프로세스를 관리하기 위해 유지하는 정보 블록 (상태, 식별자, 스택 정보 등).
- **문맥 교환 (Context Switch)**: CPU가 프로세스를 바꿀 때 현재 상태를 PCB에 저장하고 새 프로세스 상태를 불러오는 작업.
- **스레드 (Thread)**: 커널 수준(느리지만 안정적), 사용자 수준(빠르지만 불안정).

**Giải thích (Vietnamese):**
Process là một chương trình đang chạy.
Khi Process A đang chạy, hết thời gian (Timeout), OS sẽ cất trạng thái của A vào tờ giấy nhớ gọi là "PCB", sau đó gọi Process B lên chạy. Việc chuyển đổi này gọi là "Context Switch" (Chuyển đổi ngữ cảnh). Chuyển đổi càng nhiều máy càng chậm.

**💡 Mẹo ghi nhớ (Mnemonics):**
**디타블웨** (Dispatch, Timeout, Block, WakeUp): Chu trình chuyển trạng thái của Process.

---
