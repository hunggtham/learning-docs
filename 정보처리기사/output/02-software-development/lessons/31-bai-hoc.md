# 34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối unit module với IPC, boundary, message và synchronization, để các tiến trình phối hợp qua hợp đồng rõ.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 031: 모듈 구현 (Module Implementation)** khi chuyển sang phần tiếp theo.

Mục tiêu phân biệt unit module với IPC theo ranh giới, dữ liệu và cách phối hợp; từ khóa khoanh vùng interface và process boundary.

## 핵심 키워드 (Từ khóa)

단위, 모듈과, IPC

Kiến thức liên kết đặt module và IPC trên nền data flow từ storage; cách đọc tiếp theo giúp theo dõi nơi trạng thái được trao đổi.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **088: 해싱 (Hashing) & 088-1: 데이터저장소 (Data Storage)**에서 만든 기준을 이어받아 **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Cách đọc đã đặt khung đối tượng–điều kiện–hệ quả; phần module/IPC dùng khung đó để nối interface với cơ chế truyền dữ liệu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Phần này khép lại bằng trade-off giữa gọi trong module và giao tiếp liên tiến trình; khi sang module implementation, hãy giữ lại contract của interface.

## 34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)

Ở bước 31/101, **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)** xuất hiện như phần tiếp nối của **088: 해싱 (Hashing) & 088-1: 데이터저장소 (Data Storage)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **단위 모듈 (Unit Module)**, **IPC (프로세스 간 통신)**, **IPC 대표 메소드**, **Shared Memory** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **단위 모듈 (Unit Module)**: 한 가지 동작을 수행하는 기능 모듈 (독립적인 컴파일 가능).
* **IPC (프로세스 간 통신)**: 복수의 프로세스 간 통신을 구현하는 방법.
* **IPC 대표 메소드**:
  * **Shared Memory**: 다수 프로세스가 공유 가능한 메모리 구성.
  * **Socket**: 네트워크 소켓을 이용한 통신.
  * **Semaphores**: 공유 자원에 대한 접근 제어.
  * **Pipes & Named Pipes**: 선입선출(FIFO) 형태의 공유 메모리 사용.
  * **Message Queueing**: 메시지 전달 방식.
* **VI (Vietnamese) (Tiếng Việt):** Giao tiếp giữa các tiến trình (IPC). Các phương thức: Bộ nhớ chia sẻ, Socket (mạng), Cờ hiệu (Semaphore), Ống dẫn (Pipes), Hàng đợi tin nhắn.
* **Example**: 두 개의 프로그램이 채팅을 주고받을 때 Socket이나 Message Queue를 사용합니다.
* 💡 **Mẹo ghi nhớ**: S-S-S-P-M (Shared memory, Socket, Semaphore, Pipe, Message Queue).

Như vậy, **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **핵심 031: 모듈 구현 (Module Implementation)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
