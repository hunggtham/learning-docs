# 교착상태 (Dead Lock)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **교착상태 (Dead Lock)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

교착상태

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **침입 탐지 시스템 (IDS; Intrusion Detection System)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **교착상태 (Dead Lock)** và nối nó với **침입 탐지 시스템 (IDS; Intrusion Detection System)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 교착상태 (Dead Lock)
둘 이상의 프로세스가 자원을 점유한 상태에서 서로 다른 프로세스의 자원을 무한정 기다리는 현상.

### 1. 교착상태 발생의 4가지 필요충분조건
모두 충족해야 교착상태가 발생합니다.
- **상호 배제 (Mutual Exclusion)**: 한 번에 한 프로세스만 자원 사용.
- **점유와 대기 (Hold and Wait)**: 자원을 점유한 채로 다른 자원을 대기.
- **비선점 (Non-preemption)**: 할당된 자원을 강제로 빼앗을 수 없음.
- **환형 대기 (Circular Wait)**: 대기하는 프로세스들이 원형(Cycle)을 이룸.

### 2. 교착상태 해결 방법
- **예방 (Prevention)**: 4가지 조건 중 하나를 제거 (자원 낭비가 가장 심함).
- **회피 (Avoidance)**: 발생 가능성을 인정하고 적절히 피해감 (**은행원 알고리즘 / Banker's Algorithm**).
- **발견 (Detection)**: 발생 여부를 점검 (자원 할당 그래프 등).
- **회복 (Recovery)**: 교착상태에 있는 프로세스를 종료하거나 자원을 선점하여 회복.

> **Vietnamese Explanation**:
> **Deadlock (Bế tắc)** giống như kẹt xe ở ngã tư, ai cũng chờ người kia nhường đường nên không ai đi được. Để giải quyết, phương pháp **Avoidance (Né tránh)** dùng thuật toán Banker (người giữ tiền) để đảm bảo luôn có đủ tài nguyên cấp phát một cách an toàn.
