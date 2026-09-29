# 7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **데이터베이스 신기술 (DB New Technologies)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

데이터베이스, 핵심, 기술

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **계층별 주요 프로토콜 (Major Protocols by Layer)**에서 만든 기준을 이어받아 **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)** và nối nó với **데이터베이스 신기술 (DB New Technologies)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)

Từ **계층별 주요 프로토콜 (Major Protocols by Layer)**, ta đã có điểm tựa để bước vào **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 24/86 trước khi đi vào chi tiết.

Để đọc **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **7.1 회복 및 동시성 제어 (Recovery & Concurrency)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 7.1 회복 및 동시성 제어 (Recovery & Concurrency)

Các ý ngay dưới **7.1 회복 및 동시성 제어 (Recovery & Concurrency)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “7.1 회복 및 동시성 제어 (Recovery & Concurrency)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **회복 (Recovery):** 장애 발생 시 손상 이전의 정상 상태로 복구.
- **즉각 갱신 기법 (Immediate Update):** 트랜잭션 부분 완료 전이라도 즉시 DB에 반영. 갱신 내용은 **Log에 보관**하여 회복에 대비.
- **로킹 단위 (Locking Granularity):** 병행제어에서 한꺼번에 로킹하는 객체 크기.
  - **단위가 크면:** 로크 수가 작아 관리하기 쉽지만 병행성 저하.
  - **단위가 작으면:** 로크 수가 많아 관리 복잡/오버헤드 증가, 하지만 병행성 상승.
- **타임 스탬프 순서 (Time Stamp Ordering):** 직렬성 순서를 결정하기 위해 트랜잭션 처리 순서를 미리 선택.
- **Tiếng Việt:**
  - Immediate Update: Cập nhật ngay lập tức (dùng Log để phục hồi).
  - Locking Granularity: Kích thước khóa. Khóa lớn -> dễ quản lý, đồng thời thấp. Khóa nhỏ -> khó quản lý, đồng thời cao.

Các bullet của **7.1 회복 및 동시성 제어 (Recovery & Concurrency)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **7.1 회복 및 동시성 제어 (Recovery & Concurrency)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **7.2 교착상태 (Deadlock)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **7.2 교착상태 (Deadlock)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 7.2 교착상태 (Deadlock)

Bây giờ ta đi vào nội dung của **7.2 교착상태 (Deadlock)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “7.2 교착상태 (Deadlock)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **발생 4가지 조건:** 상호 배제(Mutual Exclusion), 점유와 대기(Hold and Wait), 비선점(Non-preemption), 환형 대기(Circular Wait).
- **회피 기법 (Avoidance):** 교착상태 가능성을 피해 나가는 방법. 주로 **은행원 알고리즘 (Banker's Algorithm, E. J. Dijkstra)** 사용.
- **Tiếng Việt:** 4 điều kiện Deadlock: Loại trừ lẫn nhau, Giữ & Chờ, Không trưng dụng, Chờ vòng tròn. Tránh Deadlock dùng Thuật toán Nhà băng.
- 💡 **Mẹo ghi nhớ:** Điều kiện Deadlock: Độc Giữ Không Vòng (Độc quyền, Giữ và chờ, Không ưu tiên, Vòng tròn).

Các bullet của **7.2 교착상태 (Deadlock)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **7.2 교착상태 (Deadlock)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **데이터베이스 신기술 (DB New Technologies)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.