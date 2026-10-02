# 086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Hãy nối trạng thái tiến trình, hàng đợi, chuyển ngữ cảnh và tính công bằng với điều kiện tạo ra bế tắc.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

프로세스, 스케줄링과, 교착상태

> **Chuyển mạch:** Ở chặng này của **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **086. 프로세스 스케줄링 (Process Scheduling)**에서 만든 기준을 이어받아 **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속**, **읽는 방법 (Cách đọc)** xác định đầu vào; **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속** giải thích bước vận hành tạo ra kết quả kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속

Sau khi đã đặt nền bằng **086. 프로세스 스케줄링 (Process Scheduling)**, ta chuyển sang **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속**. Đây là mắt xích 41/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **교착상태(Deadlock) 4가지 필요충분조건**, **교착상태 해결 방법 (Handling Deadlocks)**, **예방 (Prevention)**, **회피 (Avoidance)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **교착상태(Deadlock) 4가지 필요충분조건**:
  1. **상호배제 (Mutual Exclusion)**: 한 번에 한 프로세스만 자원 사용.
  2. **점유와 대기 (Hold and Wait)**: 자원을 가진 채로 다른 자원을 기다림.
  3. **비선점 (Non-Preemption)**: 남의 자원을 강제로 뺏을 수 없음.
  4. **환형 대기 (Circular Wait)**: 꼬리에 꼬리를 물고 서로의 자원을 기다림.
- **교착상태 해결 방법 (Handling Deadlocks)**:
  - **예방 (Prevention)**: 4가지 조건 중 하나를 부정 (자원 낭비 심함).
  - **회피 (Avoidance)**: 발생 가능성을 피해 자원 할당 (예: **은행원 알고리즘**, 자원 할당 그래프).
  - **발견 (Detection)**: 발생을 허용하고 나중에 감시하여 발견.
  - **복구 (Recovery)**: 발견 후 프로세스를 종료하여 자원 회복 (기아 상태 주의).

**Giải thích (Vietnamese):**
Deadlock (Bế tắc) giống như kẹt xe ở ngã tư. Ai cũng tiến lên một chút (Chiếm giữ), không ai chịu lùi (Không thể cướp quyền), và chờ người kia nhường đường (Vòng tròn chờ đợi).
- Phòng ngừa (Prevention): Xây cầu vượt để không bao giờ kẹt xe (Tốn kém).
- Né tránh (Avoidance): Xem Google Maps, thấy đường đỏ (nguy cơ kẹt) thì không đi vào (Thuật toán Banker).
- Phục hồi (Recovery): Kẹt rồi thì gọi công an đến cẩu bớt 1 xe đi để thông đường.

**💡 Mẹo ghi nhớ (Mnemonics):**
Điều kiện: **상점비환** (Tương - Chiếm - Phi - Hoàn)
Giải quyết: **예회발복** (Dự - Tị - Phát - Phục).

---

Ta có thể khép mục **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
