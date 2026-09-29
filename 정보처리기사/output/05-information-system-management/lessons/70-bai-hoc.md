# DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **교착상태 (Dead Lock)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

회복, 병행, 제어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **CASE (Computer Aided Software Engineering)**에서 만든 기준을 이어받아 **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)** và nối nó với **교착상태 (Dead Lock)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)

Ở bước 70/86, **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)** xuất hiện như phần tiếp nối của **CASE (Computer Aided Software Engineering)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **연기 갱신 (Deferred Update)**, **즉각 갱신 (Immediate Update)**, **그림자 페이지 (Shadow Paging)**, **검사점 (Check Point)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. 회복 기법 (Recovery)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. 회복 기법 (Recovery)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. 회복 기법 (Recovery)

Bây giờ ta đi vào nội dung của **1. 회복 기법 (Recovery)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

장애 발생 시 데이터베이스를 정상 상태로 복구합니다.
- **연기 갱신 (Deferred Update)**: 트랜잭션이 완료될 때까지 DB 갱신을 연기하고 로그(Log)에 보관. 실패 시 무시하면 됨. (Redo만 가능).
- **즉각 갱신 (Immediate Update)**: 즉시 DB에 갱신하고 로그에 보관. 실패 시 취소(Undo)와 재실행(Redo) 모두 사용.
- **그림자 페이지 (Shadow Paging)**: 복사본(그림자) 페이지를 보관해두고, 실패 시 대체하는 방식 (로그 불필요).
- **검사점 (Check Point)**: 특정 단계에 검사점을 찍어 장애 시 그 시점부터 회복(시간 절약).

Các bullet của **1. 회복 기법 (Recovery)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 회복 기법 (Recovery)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 병행 제어 기법 (Concurrency Control)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. 병행 제어 기법 (Concurrency Control)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. 병행 제어 기법 (Concurrency Control)

Phần nguồn của **2. 병행 제어 기법 (Concurrency Control)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

다중 트랜잭션 실행 시 DB의 일관성이 파괴되지 않도록 제어합니다.
- **로킹 (Locking)**: 데이터 엑세스 전에 Lock(잠금)을 요청하는 기법. (로킹 단위: DB, 파일, 레코드 등 한꺼번에 잠그는 크기).
- **타임 스탬프 순서 (Time Stamp Ordering)**: 트랜잭션 실행 전 시간표(Time Stamp)를 부여해 그 순서대로 처리 (교착상태 미발생).
- **다중 버전 기법**: 갱신될 때마다 새로운 버전(Version)을 부여해 관리.

> **Vietnamese Explanation**:
> **Recovery (Phục hồi DB)** có Deferred (chờ xong mới cập nhật - chỉ Redo), Immediate (cập nhật ngay - cần cả Undo và Redo).
> **Concurrency Control (Kiểm soát đồng thời)** dùng Locking (khóa dữ liệu khi đang dùng) hoặc Time Stamp (cấp tem thời gian để xếp hàng trước sau) tránh việc 2 giao dịch cùng sửa 1 dữ liệu gây lỗi.

Các bullet của **2. 병행 제어 기법 (Concurrency Control)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 병행 제어 기법 (Concurrency Control)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **교착상태 (Dead Lock)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.