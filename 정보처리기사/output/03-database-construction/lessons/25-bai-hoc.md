# 10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)

> **Mạch đọc:** [README](../README.md) là owner của **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)**; đặt bài trong tuyến transaction trước SQL categories và concurrency details. Từ **학습 목표 (Mục tiêu)** qua **핵심 키워드 (Từ khóa)**, nối transaction boundaries với lock/isolation, commit/rollback, recovery và control techniques, rồi dùng **선행·연결 개념 (Kiến thức liên kết)** để phân biệt TCL/DDL/DML trong một workflow có trạng thái.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **143-145. SQL 분류 (SQL Categories)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

트랜잭션, 관리, 기법, 제어

> **Nối mạch:** Ở chặng này của **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **9. 인덱스와 트랜잭션 (Index và Giao dịch)**에서 만든 기준을 이어받아 **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)**, **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)

Ở bước 25/54, **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)** xuất hiện như phần tiếp nối của **9. 인덱스와 트랜잭션 (Index và Giao dịch)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)

Bây giờ ta đi vào nội dung của **병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **로킹 (Locking):** Khóa tài nguyên để đảm bảo giao dịch chạy tuần tự (직렬화).
  - *Đơn vị khóa (Locking Unit):* Càng lớn (DB, Bảng) -> Ít Lock, Overhead nhỏ, Tính đồng thời giảm. Càng nhỏ (Bản ghi, Trường) -> Nhiều Lock, Overhead lớn, Tính đồng thời cao.
- **타임스탬프 (Time Stamping):** Gắn mốc thời gian để ưu tiên.
- **다중버전 동시제어 (MVCC):** Giữ nhiều phiên bản dữ liệu.
- **낙관적 병행제어 (Optimistic):** Cứ cho chạy đi, kết thúc mới kiểm tra lỗi (thích hợp môi trường ít xung đột).

Các bullet của **병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **트랜잭션 상태 (Trạng thái giao dịch)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **트랜잭션 상태 (Trạng thái giao dịch)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 트랜잭션 상태 (Trạng thái giao dịch)

Phần nguồn của **트랜잭션 상태 (Trạng thái giao dịch)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “트랜잭션 상태 (Trạng thái giao dịch)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **활동 (Active):** Đang chạy.
- **부분 완료 (Partially Committed):** Đã chạy lệnh xong, chuẩn bị COMMIT nhưng chưa ghi lên đĩa.
- **완료 (Committed):** Thành công và lưu vĩnh viễn.
- **실패 (Failed):** Có lỗi xảy ra.
- **철회 (Aborted):** Bị hủy bỏ (Rollback).

Các bullet của **트랜잭션 상태 (Trạng thái giao dịch)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **트랜잭션 상태 (Trạng thái giao dịch)**, đừng bắt đầu lại từ số không. **데이터 사전 (Data Dictionary / System Catalog / Metadata)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **데이터 사전 (Data Dictionary / System Catalog / Metadata)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 데이터 사전 (Data Dictionary / System Catalog / Metadata)

Các ý ngay dưới **데이터 사전 (Data Dictionary / System Catalog / Metadata)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “데이터 사전 (Data Dictionary / System Catalog / Metadata)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Lưu thông tin về các đối tượng (bảng, view, index...).
- DBMS tự động cập nhật, người dùng **chỉ được Read Only (조회만 가능)**.

---

Các bullet của **데이터 사전 (Data Dictionary / System Catalog / Metadata)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **데이터 사전 (Data Dictionary / System Catalog / Metadata)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **143-145. SQL 분류 (SQL Categories)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
