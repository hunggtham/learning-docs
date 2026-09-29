# 34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 031: 모듈 구현 (Module Implementation)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

단위, 모듈과, IPC

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **32. 추가 해싱 함수 (Additional Hashing Functions)**에서 만든 기준을 이어받아 **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)

Sau khi đã đặt nền bằng **32. 추가 해싱 함수 (Additional Hashing Functions)**, ta chuyển sang **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)**. Đây là mắt xích 17/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **단위 모듈 (Unit Module)**, **IPC (프로세스 간 통신)**, **IPC 대표 메소드**, **Shared Memory** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

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

Ta có thể khép mục **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **핵심 031: 모듈 구현 (Module Implementation)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.