# 086. 프로세스 스케줄링 (Process Scheduling)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **086. 프로세스 스케줄링 (Process Scheduling)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

프로세스, 스케줄링

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 086. 프로세스 스케줄링 (Process Scheduling)
- **선점형 (Preemptive)**: 운영체제가 CPU를 강제로 뺏을 수 있음. 빠르고 대화식 시스템에 유리하지만 오버헤드 발생. (RR, SRT, MLQ, MLFQ).
- **비선점형 (Non-Preemptive)**: 한 프로세스가 끝나야만 다음 프로세스가 CPU를 씀. 일괄처리에 적합. (FCFS, SJF, HRN).
  - **FCFS**: 먼저 온 놈이 먼저 (First Come First Serve).
  - **SJF**: 짧은 작업 먼저 (Shortest Job First). 긴 작업은 무한 대기(기아 상태) 발생 가능.
  - **HRN**: SJF의 단점(기아 상태) 보완. 우선순위 = (대기시간 + 서비스시간) / 서비스시간. 결과값이 큰 것부터 우선 처리!

**Giải thích (Vietnamese):**
Lập lịch cho CPU:
- Độc quyền (Non-Preemptive): Đang chạy thì không ai được cướp (Giống như đang đi vệ sinh, người khác phải đợi). Ví dụ: FCFS, SJF, HRN.
- Cướp quyền (Preemptive): Đang chạy nhưng có việc khẩn cấp (hoặc hết giờ) thì hệ thống đuổi ra cho người khác vào. Ví dụ: RR, SRT.
- Công thức HRN rất hay thi: `(Thời gian đợi + Thời gian xử lý) / Thời gian xử lý`. Việc đợi càng lâu ưu tiên càng cao.

---
