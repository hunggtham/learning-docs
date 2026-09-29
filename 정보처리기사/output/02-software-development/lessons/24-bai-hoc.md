# 핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

핵심, 형상, 관리, IDE

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)**에서 만든 기준을 이어받아 **핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)

Từ **40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)**, ta đã có điểm tựa để bước vào **핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 24/95 trước khi đi vào chi tiết.

Để đọc **핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **형상 관리 (Configuration Management)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 형상 관리 (Configuration Management)

Các ý ngay dưới **형상 관리 (Configuration Management)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 소프트웨어 개발 과정의 **변경 사항을 관리**하는 것. (Quản lý mọi thay đổi trong vòng đời phần mềm - Version Control).
- 대상 (Đối tượng): 계획, 요구 분석서, 설계서, 소스 코드, 테스트 케이스, 지침서 등. (**개발 비용 - Chi phí phát triển KHÔNG nằm trong này**).
- 절차 (Trình tự): 형상 식별 (Nhận dạng) → 형상 통제 (Kiểm soát bởi CCB) → 형상 감사 (Kiểm toán) → 형상 기록 (Ghi lại).

Các bullet của **형상 관리 (Configuration Management)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **형상 관리 (Configuration Management)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **형상 관리 방식 (Các phương pháp quản lý phiên bản)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **형상 관리 방식 (Các phương pháp quản lý phiên bản)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 형상 관리 방식 (Các phương pháp quản lý phiên bản)

Bây giờ ta đi vào nội dung của **형상 관리 방식 (Các phương pháp quản lý phiên bản)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **공유 폴더 방식 (Shared Folder):** Lưu vào chung một thư mục trên mạng nội bộ. (Ví dụ: RCS).
- **클라이언트/서버 방식 (Client/Server):** Quản lý tập trung trên một máy chủ. (Ví dụ: CVS, SVN).
- **분산 저장소 방식 (Distributed Repository):** Mỗi máy cá nhân đều chứa một bản copy của kho chứa, commit lên máy cá nhân trước rồi mới push lên server. Rất an toàn. (Ví dụ: **Git**).

Các ý về **형상 관리 방식 (Các phương pháp quản lý phiên bản)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **형상 관리 방식 (Các phương pháp quản lý phiên bản)**, đừng bắt đầu lại từ số không. **형상 관리 도구 기능 (Chức năng công cụ)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **형상 관리 도구 기능 (Chức năng công cụ)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 형상 관리 도구 기능 (Chức năng công cụ)

Phần nguồn của **형상 관리 도구 기능 (Chức năng công cụ)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **Check-In:** Đẩy code lên kho (Upload).
- **Check-Out:** Lấy code mới nhất về (Download).
- **Commit:** Xác nhận lưu sự thay đổi.

Các bullet của **형상 관리 도구 기능 (Chức năng công cụ)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**형상 관리 도구 기능 (Chức năng công cụ)** vừa cho ta cách đặt câu hỏi. Bây giờ **IDE (Integrated Development Environment - Môi trường phát triển tích hợp)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **IDE (Integrated Development Environment - Môi trường phát triển tích hợp)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### IDE (Integrated Development Environment - Môi trường phát triển tích hợp)

Các ý ngay dưới **IDE (Integrated Development Environment - Môi trường phát triển tích hợp)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 코딩, 컴파일, 디버깅, 배포 (Coding, Compile, Debug, Deployment) 기능을 하나로 통합. (Tích hợp tất cả công cụ lập trình vào một phần mềm).
- Ví dụ: Eclipse (Java), Visual Studio (C#, C++), Xcode (iOS), Android Studio, IntelliJ IDEA.

- **Vietnamese Explanation:** Quản lý hình thái (Configuration/Version) giống như việc lưu file "Bao_cao_lan1", "Bao_cao_lan2", "Bao_cao_FINAL". Git (Phân tán) là công cụ phổ biến nhất hiện nay. IDE là bộ công cụ tất cả-trong-một của lập trình viên (vừa gõ code, vừa dịch, vừa tìm lỗi).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Trình tự 형상 quản lý: Nhận Kiểm Đánh Ghi (Nhận diện - Kiểm soát - Đánh giá - Ghi chép). Git = Phân tán (분산). IDE 4 bước: CoCoDeDe (Coding - Compile - Debugging - Deployment).

---

Với **IDE (Integrated Development Environment - Môi trường phát triển tích hợp)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **IDE (Integrated Development Environment - Môi trường phát triển tích hợp)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.