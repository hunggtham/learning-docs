# 297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **네트워크 통신 (Network Communication)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

프로세스와, 스레드, 스케줄링

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속**에서 만든 기준을 이어받아 **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)** và nối nó với **네트워크 통신 (Network Communication)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)

Sau khi đã đặt nền bằng **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속**, ta chuyển sang **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**. Đây là mắt xích 44/78 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **프로세스(Process)**, **상태 전이**, **Dispatch**, **Timeout** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **프로세스(Process)**: **PCB(Process Control Block)를 가진** 실행 중인 프로그램.
- **상태 전이**:
  - **Dispatch**: 준비(Ready) -> 실행(Run) (CPU 할당 받음).
  - **Timeout**: 실행(Run) -> 준비(Ready) (시간 초과).
  - **Wake Up**: 대기(Wait) -> 준비(Ready) (입출력 완료).
- **스레드(Thread)**: 프로세스 내의 독립적인 실행 흐름 (최소 작업 단위). 프로세스의 자원을 공유하여 병행성 증대 및 문맥 교환 오버헤드 감소.
- **비선점 스케줄링 (Non-Preemptive)**:
  - FCFS: 먼저 온 순서대로.
  - SJF: 실행 시간이 가장 짧은 것 먼저.
  - **HRN**: 대기 시간과 서비스 시간을 고려해 기아(Starvation) 현상 해결. 공식: **(대기시간 + 서비스시간) / 서비스시간** (값이 클수록 우선).

---

Ta có thể khép mục **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **네트워크 통신 (Network Communication)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.