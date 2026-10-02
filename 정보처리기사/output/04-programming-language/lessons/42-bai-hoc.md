# 297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối processes, threads và scheduling với state, queue, context switch và fairness, để CPU được điều phối.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **네트워크 통신 (Network Communication)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

프로세스와, 스레드, 스케줄링

> **Chuyển mạch:** Ở chặng này của **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속**에서 만든 기준을 이어받아 **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**, **읽는 방법 (Cách đọc)** xác định đầu vào; **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)** giải thích bước vận hành tạo ra kết quả kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)

Từ **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속**, ta đã có điểm tựa để bước vào **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 42/91 trước khi đi vào chi tiết.

Để đọc **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **프로세스(Process)**, **상태 전이**, **Dispatch**, **Timeout** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

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

Điểm chốt của **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **네트워크 통신 (Network Communication)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
