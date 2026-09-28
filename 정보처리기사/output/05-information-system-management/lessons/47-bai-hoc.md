# 침입 탐지 시스템 (IDS; Intrusion Detection System)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **침입 탐지 시스템 (IDS; Intrusion Detection System)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

침입, 탐지, 시스템

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **교착상태 (Dead Lock)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **리눅스의 커널 로그 (Linux Kernel Logs)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **침입 탐지 시스템 (IDS; Intrusion Detection System)** và nối nó với **리눅스의 커널 로그 (Linux Kernel Logs)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 침입 탐지 시스템 (IDS; Intrusion Detection System)
컴퓨터 시스템의 비정상적인 사용, 오용, 남용 등을 실시간으로 탐지하는 시스템.
- **오용 탐지 (Misuse Detection)**: 미리 입력해 둔 공격 패턴 감지 (시그니처 기반).
- **이상 탐지 (Anomaly Detection)**: 평균적인 상태를 기준으로 비정상 행위 감지 (행위 기반).
- **종류**:
  - **HIDS (Host-Based)**: 내부 시스템 감시 (OSSEC 등).
  - **NIDS (Network-Based)**: 외부로부터의 네트워크 트래픽 감시 (Snort 등).
