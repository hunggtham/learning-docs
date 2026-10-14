# 주요 스케줄링 알고리즘 (Major Scheduling Algorithms)

## 주요 스케줄링 알고리즘 (Major Scheduling Algorithms)

### 1. FCFS (First Come First Service) / FIFO
준비 큐에 도착한 순서대로 CPU를 할당하는 기법 (선입선출). 구현은 가장 간단하나, 긴 작업이 먼저 오면 뒤의 짧은 작업이 오래 기다리게 됨.

### 2. SJF (Shortest Job First)
실행 시간이 가장 짧은 프로세스에게 먼저 CPU를 할당하는 기법. 가장 적은 평균 대기 시간을 제공하지만, 실행 시간이 긴 프로세스는 무한정 기다릴 수 있음.

### 3. HRN (Highest Response-ratio Next)
SJF의 단점(긴 작업 불리)을 보완하여 대기 시간과 실행 시간을 함께 고려함.
- **우선순위 계산식**: `(대기 시간 + 서비스 시간) / 서비스 시간`
- 결과값이 높은 것부터 우선순위를 부여함.
