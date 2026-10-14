# 프로세스와 스레드 (Process and Thread)

## 프로세스와 스레드 (Process and Thread)

### 1. 프로세스 (Process)
Phần “1. 프로세스 (Process)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- CPU에 의해 처리되는 실행 중인 프로그램 (작업/Job, 태스크/Task).
- **PCB(Process Control Block)**: 운영체제가 프로세스에 대한 중요한 정보를 저장하는 곳. (현재 상태, 포인터, 고유 식별자, 스케줄링 우선순위 등). 프로세스 생성 시 만들어지고 완료 시 제거됨.

### 2. 프로세스 상태 전이 (Process State Transition)
Phần “2. 프로세스 상태 전이 (Process State Transition)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **제출(Submit) -> 접수(Hold) -> 준비(Ready) -> 실행(Run) -> 대기(Wait/Block) -> 종료(Exit)**
- **주요 용어**:
  - **Dispatch (디스패치)**: 준비 상태 -> 실행 상태로 전이 (CPU 할당).
  - **Wake Up (웨이크 업)**: 입·출력 완료 후 대기 상태 -> 준비 상태로 전이.
  - **Spooling (스풀링)**: 디스크를 버퍼처럼 활용해 느린 입출력 장치와 CPU 간 속도 차이를 보완.

### 3. 스레드 (Thread)
Phần “3. 스레드 (Thread)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 프로세스 내에서의 작업 단위 (경량 프로세스/Light Weight Process).
- 동일 프로세스 환경에서 서로 독립적인 다중 수행이 가능하여 응답 시간을 단축하고 기억장소 낭비를 줄입니다.

> **Vietnamese Explanation**:
> **Process** là một chương trình đang chạy. **Thread** là các luồng xử lý nhỏ nằm bên trong Process. Dùng nhiều thread giúp chương trình chạy nhanh hơn và chia sẻ bộ nhớ tốt hơn (ví dụ nhiều tab trên trình duyệt). **Dispatch** là hành động cấp CPU cho một tiến trình đang xếp hàng chờ.
