# 운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối OS memory/process management với address space, scheduling và lifecycle, để chương trình chạy được đọc qua tài nguyên.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **082. 운영체제 기능 및 종류 (Operating System OS)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

운영체제, 메모리, 프로세스, 관리

> **Nối mạch:** Ở chặng này của **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **스크립트 및 운영체제 (Script Languages & Operating Systems)**에서 만든 기준을 이어받아 **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**, **읽는 방법 (Cách đọc)** đặt đầu vào cho **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**, rồi nối sang phần giải thích tiếp theo.

## 운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)

Từ **스크립트 및 운영체제 (Script Languages & Operating Systems)**, ta đã có điểm tựa để bước vào **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 33/91 trước khi đi vào chi tiết.

Để đọc **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **최초 적합 (First Fit)**, **최적 적합 (Best Fit)**, **최악 적합 (Worst Fit)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **200. 기억장치의 배치 전략 (Memory Placement Strategies / Chiến lược cấp phát bộ nhớ)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 200. 기억장치의 배치 전략 (Memory Placement Strategies / Chiến lược cấp phát bộ nhớ)

Các ý ngay dưới **200. 기억장치의 배치 전략 (Memory Placement Strategies / Chiến lược cấp phát bộ nhớ)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “200. 기억장치의 배치 전략 (Memory Placement Strategies / Chiến lược cấp phát bộ nhớ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **최초 적합 (First Fit)**: 첫 번째 분할 영역에 배치 (Vị trí trống đầu tiên đủ lớn).
- **최적 적합 (Best Fit)**: 단편화가 가장 작은 영역 (Vị trí trống vừa vặn nhất, để lại ít rác nhất).
- **최악 적합 (Worst Fit)**: 단편화가 가장 큰 영역 (Vị trí trống lớn nhất).
  - 💡 *Mẹo ghi nhớ*: First = Nhanh nhất. Best = Tiết kiệm nhất. Worst = Còn lại khoảng trống lớn nhất.

Với **200. 기억장치의 배치 전략 (Memory Placement Strategies / Chiến lược cấp phát bộ nhớ)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **200. 기억장치의 배치 전략 (Memory Placement Strategies / Chiến lược cấp phát bộ nhớ)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **201. 페이지 교체 알고리즘 - FIFO (Page Replacement - FIFO / Thuật toán thay thế trang)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **201. 페이지 교체 알고리즘 - FIFO (Page Replacement - FIFO / Thuật toán thay thế trang)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 201. 페이지 교체 알고리즘 - FIFO (Page Replacement - FIFO / Thuật toán thay thế trang)

Bây giờ ta đi vào nội dung của **201. 페이지 교체 알고리즘 - FIFO (Page Replacement - FIFO / Thuật toán thay thế trang)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “201. 페이지 교체 알고리즘 - FIFO (Page Replacement - FIFO / Thuật toán thay thế trang)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 가장 먼저 들어와서 가장 오래 있었던 페이지를 교체 (Thay thế trang vào bộ nhớ sớm nhất - First In First Out).

Các bullet của **201. 페이지 교체 알고리즘 - FIFO (Page Replacement - FIFO / Thuật toán thay thế trang)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **201. 페이지 교체 알고리즘 - FIFO (Page Replacement - FIFO / Thuật toán thay thế trang)**, đừng bắt đầu lại từ số không. **202. 스래싱 (Thrashing)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **202. 스래싱 (Thrashing)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 202. 스래싱 (Thrashing)

Phần nguồn của **202. 스래싱 (Thrashing)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “202. 스래싱 (Thrashing)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 프로세스 처리 시간보다 페이지 교체 시간이 더 많아지는 현상 (Hiện tượng mất nhiều thời gian cho việc tráo đổi trang bộ nhớ hơn là thực thi tiến trình).
  - 💡 *Mẹo ghi nhớ*: Thrashing = Kẹt xe bộ nhớ (quá tải).

Với **202. 스래싱 (Thrashing)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**202. 스래싱 (Thrashing)** vừa cho ta cách đặt câu hỏi. Bây giờ **203. 프로세스 상태 (Process States / Trạng thái tiến trình)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **203. 프로세스 상태 (Process States / Trạng thái tiến trình)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 203. 프로세스 상태 (Process States / Trạng thái tiến trình)

Các ý ngay dưới **203. 프로세스 상태 (Process States / Trạng thái tiến trình)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “203. 프로세스 상태 (Process States / Trạng thái tiến trình)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 제출(Submit) → 접수(Hold) → 준비(Ready) → 실행(Run) → 대기(Wait/Block) → 종료(Exit).
  - 💡 *Mẹo ghi nhớ*: Nộp -> Nhận -> Chờ chạy -> Chạy -> (Tạm dừng nếu cần) -> Xong.

Các bullet của **203. 프로세스 상태 (Process States / Trạng thái tiến trình)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **203. 프로세스 상태 (Process States / Trạng thái tiến trình)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **204. 스케줄링 - SJF (Shortest Job First / Việc ngắn làm trước)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **204. 스케줄링 - SJF (Shortest Job First / Việc ngắn làm trước)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 204. 스케줄링 - SJF (Shortest Job First / Việc ngắn làm trước)

Bây giờ ta đi vào nội dung của **204. 스케줄링 - SJF (Shortest Job First / Việc ngắn làm trước)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “204. 스케줄링 - SJF (Shortest Job First / Việc ngắn làm trước)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 실행 시간이 가장 짧은 프로세스에게 먼저 CPU 할당 (Ưu tiên tiến trình có thời gian thực thi ngắn nhất).

Các bullet của **204. 스케줄링 - SJF (Shortest Job First / Việc ngắn làm trước)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **204. 스케줄링 - SJF (Shortest Job First / Việc ngắn làm trước)**, đừng bắt đầu lại từ số không. **205. 스케줄링 - HRN (Highest Response-ratio Next)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **205. 스케줄링 - HRN (Highest Response-ratio Next)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 205. 스케줄링 - HRN (Highest Response-ratio Next)

Phần nguồn của **205. 스케줄링 - HRN (Highest Response-ratio Next)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “205. 스케줄링 - HRN (Highest Response-ratio Next)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 우선순위 = `(대기 시간 + 서비스 시간) / 서비스 시간`
- (Priority = (Wait time + Service time) / Service time).
  - *Example / Ví dụ*: Đợi 10, Chạy 5 => `(10+5)/5 = 3`.
  - 💡 *Mẹo ghi nhớ*: Công thức = `(Đợi + Chạy) / Chạy`. Số càng lớn càng ưu tiên. Giải quyết nhược điểm của SJF (tiến trình dài bị bỏ đói).

Với **205. 스케줄링 - HRN (Highest Response-ratio Next)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Như vậy, **205. 스케줄링 - HRN (Highest Response-ratio Next)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **082. 운영체제 기능 및 종류 (Operating System OS)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
