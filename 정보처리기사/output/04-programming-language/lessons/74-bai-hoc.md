# 교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)

## 교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)
Phần “교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **교착상태(Deadlock)**: 두 프로세스가 서로의 자원을 기다리며 멈춰버린 현상.
- **상호배제 알고리즘 (Mutual Exclusion)**: 한 번에 하나의 프로세스만 자원을 쓰게 함.
  - Dekker: 두 프로세스 간 Flag와 Turn 변수 사용.
  - Peterson: 두 프로세스 간 상대방에게 양보.
  - Lamport: 고유 번호(티켓) 부여, 번호순 진입.
  - Semaphore: 정수 변수(P연산, V연산)를 이용해 접근 통제.
