# 116 & 117: 형상 관리 도구 (SVN vs Git)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **116 & 117: 형상 관리 도구 (SVN vs Git)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **116 & 117: 형상 관리 도구 (SVN vs Git)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

형상, 관리, 도구

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)**에서 만든 기준을 이어받아 **116 & 117: 형상 관리 도구 (SVN vs Git)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 116 & 117: 형상 관리 도구 (SVN vs Git)

Sau khi đã đặt nền bằng **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)**, ta chuyển sang **116 & 117: 형상 관리 도구 (SVN vs Git)**. Đây là mắt xích 26/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **116 & 117: 형상 관리 도구 (SVN vs Git)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **Subversion (SVN)**. Hãy xác định **Subversion (SVN)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### Subversion (SVN)

Phần nguồn của **Subversion (SVN)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 클라이언트/서버 구조 (Cấu trúc Client/Server tập trung).
- **Trunk:** Thư mục chính (Main).
- **Branches:** Th nhánh để làm tính năng riêng.
- **Revision:** Mỗi lần Commit thành công, số Revision tăng lên 1.

Các bullet của **Subversion (SVN)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **Subversion (SVN)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **Git (깃)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **Git (깃)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### Git (깃)

Các ý ngay dưới **Git (깃)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 분산 저장소 방식 (Lưu trữ phân tán). Phát minh bởi Linus Torvalds.
- **Snapshot (스냅샷):** Lưu lại toàn bộ trạng thái file tại một thời điểm rất nhanh chóng.
- **로컬 저장소 (Local Repo) vs 원격 저장소 (Remote Repo):** Internet đứt vẫn làm việc bình thường ở Local.

- 💡 **Mẹo ghi nhớ (Mnemonics):** SVN = Trunk (Thân cây), Revision tăng dần. Git = Snapshot, Phân tán (Phân tán (Distributed)).

---

Với **Git (깃)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **Git (깃)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **116 & 117: 형상 관리 도구 (SVN vs Git)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.