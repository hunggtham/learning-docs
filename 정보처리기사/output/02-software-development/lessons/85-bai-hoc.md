# 핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 115 & 116: 연관 기억장치 및 메모리 인터리빙 (Associative Memory & Memory Interleaving)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

핵심, 보조기억장치, 디스크, 접근, 시간

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)**에서 만든 기준을 이어받아 **핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)** và nối nó với **핵심 115 & 116: 연관 기억장치 및 메모리 인터리빙 (Associative Memory & Memory Interleaving)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)

Ở bước 85/101, **핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)** xuất hiện như phần tiếp nối của **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **보조기억장치 (Bộ nhớ phụ)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **보조기억장치 (Bộ nhớ phụ)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 보조기억장치 (Bộ nhớ phụ)

Bây giờ ta đi vào nội dung của **보조기억장치 (Bộ nhớ phụ)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “보조기억장치 (Bộ nhớ phụ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 주기억장치에 비해 속도는 느리지만 저장 용량이 크다. 전원이 차단되어도 내용이 그대로 유지된다. (Chậm hơn RAM nhưng dung lượng lớn, lưu trữ vĩnh viễn.)
- **자기 테이프 (Magnetic Tape - Băng từ):**
  - 순차처리(SASD)만 할 수 있는 대용량 저장매체. (Chỉ truy cập tuần tự, không nhảy cóc được.)
  - 자료의 백업용으로 많이 사용함. (Thường dùng để Backup.)
- **자기 디스크 (Magnetic Disk - Đĩa từ / HDD):**
  - 순차, 비순차(직접) 처리가 모두 가능한 DASD 방식. (Có thể truy cập trực tiếp ngẫu nhiên.)
  - **Track (Rãnh):** Vòng tròn đồng tâm.
  - **Sector (Cung):** Track chia nhỏ, là đơn vị lưu trữ cơ bản.
  - **Cylinder (Trụ):** Tập hợp các track cùng vị trí trên các mặt đĩa.

Các bullet của **보조기억장치 (Bộ nhớ phụ)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **보조기억장치 (Bộ nhớ phụ)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **디스크의 Access Time (Thời gian truy cập đĩa)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **디스크의 Access Time (Thời gian truy cập đĩa)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 디스크의 Access Time (Thời gian truy cập đĩa)

Phần nguồn của **디스크의 Access Time (Thời gian truy cập đĩa)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “디스크의 Access Time (Thời gian truy cập đĩa)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `Access Time = Seek Time + Latency Time (Rotational Delay) + Transmission Time`
- **Seek Time (Thời gian tìm rãnh):** Đầu đọc di chuyển đến đúng Track.
- **Latency Time (Thời gian chờ xoay):** Đợi đĩa xoay đúng đến Sector cần đọc.
- **Transmission Time (Thời gian truyền):** Đọc Sector và truyền vào RAM.

- **Vietnamese Explanation:** Tape giống như băng cassette (muốn nghe bài 5 phải tua qua bài 1,2,3,4). Disk giống như đĩa CD hoặc đĩa than, bạn có thể đặt kim đọc vào bất kỳ bài nào (DASD).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Công thức tìm ổ cứng: SLT. **S**eek (Tìm Track) -> **L**atency (Đợi Sector xoay tới) -> **T**ransmission (Truyền đi).

---

Với **디스크의 Access Time (Thời gian truy cập đĩa)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **디스크의 Access Time (Thời gian truy cập đĩa)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **핵심 115 & 116: 연관 기억장치 및 메모리 인터리빙 (Associative Memory & Memory Interleaving)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.