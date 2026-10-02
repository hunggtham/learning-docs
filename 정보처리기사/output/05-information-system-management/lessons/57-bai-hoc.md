# Windows와 UNIX 운영체제 (Windows & UNIX)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Windows와 UNIX 운영체제 (Windows & UNIX)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Hãy đặt kernel, shell, hệ thống tệp và tiến trình cạnh nhau để nhận ra khác biệt vận hành giữa Windows và UNIX.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **Windows와 UNIX 운영체제 (Windows & UNIX)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **Windows와 UNIX 운영체제 (Windows & UNIX)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **UNIX 주요 구성요소 (UNIX Components)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **Windows와 UNIX 운영체제 (Windows & UNIX)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

UNIX, 운영체제

> **Chuyển mạch:** Ở chặng này của **Windows와 UNIX 운영체제 (Windows & UNIX)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **운영체제 (OS: Operating System) 기초**에서 만든 기준을 이어받아 **Windows와 UNIX 운영체제 (Windows & UNIX)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Windows와 UNIX 운영체제 (Windows & UNIX)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Windows와 UNIX 운영체제 (Windows & UNIX)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **Windows와 UNIX 운영체제 (Windows & UNIX)**, **Windows와 UNIX 운영체제 (Windows & UNIX)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Windows와 UNIX 운영체제 (Windows & UNIX)

Từ **운영체제 (OS: Operating System) 기초**, ta đã có điểm tựa để bước vào **Windows와 UNIX 운영체제 (Windows & UNIX)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 57/86 trước khi đi vào chi tiết.

Để đọc **Windows와 UNIX 운영체제 (Windows & UNIX)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **GUI (Graphic User Interface)**, **선점형 멀티태스킹 (Preemptive Multi-Tasking)**, **PnP (Plug and Play)**, **OLE (Object Linking and Embedding)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. Windows 주요 특징** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. Windows 주요 특징

Các ý ngay dưới **1. Windows 주요 특징** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “1. Windows 주요 특징” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **GUI (Graphic User Interface)**: 마우스 기반 그래픽 환경.
- **선점형 멀티태스킹 (Preemptive Multi-Tasking)**: 응용 프로그램 문제 시 OS가 강제 종료시켜 자원 반환.
- **PnP (Plug and Play)**: 하드웨어 설치 시 OS가 자동 감지 및 환경 구성.
- **OLE (Object Linking and Embedding)**: 문자/그림 개체를 다른 문서에 연결하거나 삽입.
- **긴 파일명**: 최대 255자 지정 가능 (VFAT 이용).

Các bullet của **1. Windows 주요 특징** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. Windows 주요 특징** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. UNIX 주요 특징** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **2. UNIX 주요 특징**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2. UNIX 주요 특징

Bây giờ ta đi vào nội dung của **2. UNIX 주요 특징**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “2. UNIX 주요 특징” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 대화식 시분할 시스템 (Time Sharing System) 및 개방형 시스템 (Open System).
- 주로 **C언어**로 작성되어 이식성이 높고 파일 시스템은 트리(Tree) 구조를 가짐.
- **다중 사용자 (Multi-User)** 및 **다중 작업 (Multi-Tasking)** 지원.

Các bullet của **2. UNIX 주요 특징** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. UNIX 주요 특징**, đừng bắt đầu lại từ số không. **3. 파일 디스크립터 (File Descriptor)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **3. 파일 디스크립터 (File Descriptor)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 3. 파일 디스크립터 (File Descriptor)

Phần nguồn của **3. 파일 디스크립터 (File Descriptor)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “3. 파일 디스크립터 (File Descriptor)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 파일 제어 블록(FCB; File Control Block)이라고도 하며, 시스템(OS)이 필요로 하는 파일에 대한 정보를 가진 제어 블록.
- 파일마다 독립적으로 존재하며 보통 보조기억장치에 있다가 파일이 열릴(Open) 때 주기억장치로 옮겨집니다.

Các bullet của **3. 파일 디스크립터 (File Descriptor)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**3. 파일 디스크립터 (File Descriptor)** vừa cho ta cách đặt câu hỏi. Bây giờ **4. UNIX 시스템 구조: 커널 (Kernel)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **4. UNIX 시스템 구조: 커널 (Kernel)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 4. UNIX 시스템 구조: 커널 (Kernel)

Các ý ngay dưới **4. UNIX 시스템 구조: 커널 (Kernel)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “4. UNIX 시스템 구조: 커널 (Kernel)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- UNIX의 가장 **핵심적인 부분**. 프로그램과 하드웨어 간의 인터페이스 역할을 담당하며 프로세스, 메모리, 입출력 관리 등을 수행합니다.

> **Vietnamese Explanation**:
> Windows nổi bật với giao diện chuột GUI, Plug and Play (cắm là chạy). UNIX là hệ điều hành mã nguồn mở, đa nhiệm, đa người dùng, chủ yếu viết bằng C. Trong UNIX, Kernel (nhân) là phần cốt lõi quản lý phần cứng và giao tiếp với phần mềm. File Descriptor lưu giữ thông tin quan trọng về các file đang được hệ thống quản lý.

Các bullet của **4. UNIX 시스템 구조: 커널 (Kernel)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **4. UNIX 시스템 구조: 커널 (Kernel)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **Windows와 UNIX 운영체제 (Windows & UNIX)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **UNIX 주요 구성요소 (UNIX Components)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **Windows와 UNIX 운영체제 (Windows & UNIX)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
