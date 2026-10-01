# Dữ liệu (data / 데이터) minimization, purpose limitation và retention kỹ thuật (engineering / 엔지니어링)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Dữ liệu (data / 데이터) minimization, purpose limitation và retention kỹ thuật (engineering / 엔지니어링)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Dữ liệu (data / 데이터) minimization** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **Purpose limitation** để mở câu hỏi trung tâm cho phần kế tiếp. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Privacy kỹ thuật (engineering / 엔지니어링) không chỉ là chính sách (policy / 정책) document. Một hệ thống thật sự bảo vệ dữ liệu phải biến nguyên tắc như **dữ liệu (data / 데이터) minimization**, **purpose limitation** và **retention** thành kiến trúc (architecture / 아키텍처), lược đồ (schema / 스키마), kiểm soát truy cập (access control / 접근 제어) và deletion workflow có thể kiểm chứng.

## Dữ liệu (data / 데이터) minimization

Dữ liệu (data / 데이터) minimization hỏi: để cung cấp năng lực (capability / 역량) này, hệ thống thực sự cần thu thập và giữ những fields nào? “Có thể hữu ích sau này” tạo dữ liệu (data / 데이터) liability: breach impact lớn hơn, authorization phức tạp hơn và deletion khó hơn.

Minimization nên diễn ra từ đầu vào (input / 입력) ranh giới (boundary / 경계). Nếu trường dữ liệu (field / 필드) không cần thiết, tốt hơn không thu thập thay vì thu thập rồi hứa không dùng.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) minimization, purpose limitation và retention kỹ thuật (engineering / 엔지니어링)**, **Dữ liệu (data / 데이터) minimization** đã nêu tiêu chí phân biệt, còn **Purpose limitation** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Retention là vòng đời (lifecycle / 생명주기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Purpose limitation

Cùng một dữ liệu có thể phù hợp cho mục đích A nhưng không mặc nhiên phù hợp cho B. kỹ thuật (engineering / 엔지니어링) cần gắn luồng dữ liệu (data flow / 데이터 흐름) với declared purpose và authorization ngữ cảnh (context / 맥락) thay vì coi mọi nội bộ (internal / 내부) dữ liệu (data / 데이터) là tài nguyên dùng tự do.

Điều này ảnh hưởng sự kiện (event / 이벤트) bus, analytics lake và tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링): bản sao (copy / 복사) dữ liệu (data / 데이터) sang hệ thống khác tạo thêm processing purpose và retention ranh giới (boundary / 경계) cần quản lý.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) minimization, purpose limitation và retention kỹ thuật (engineering / 엔지니어링)**, **Purpose limitation** đã nêu tiêu chí phân biệt, còn **Retention là vòng đời (lifecycle / 생명주기)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **TTL và scheduled deletion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Retention là vòng đời (lifecycle / 생명주기)

“Giữ 90 ngày” nghe đơn giản nhưng dữ liệu (data / 데이터) có thể tồn tại trong primary DB, replica, bộ nhớ đệm (cache / 캐시), tìm kiếm (search / 검색) chỉ mục (index / 인덱스), đối tượng (object / 객체) lưu trữ (storage / 저장소), log, backup và derived dataset. Retention kỹ thuật (engineering / 엔지니어링) cần inventory các copies và định nghĩa deletion ngữ nghĩa (semantics / 의미론) cho từng tầng (layer / 계층).

Một row bị delete khỏi primary không có nghĩa mọi derived bản sao (copy / 복사) biến mất ngay.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) minimization, purpose limitation và retention kỹ thuật (engineering / 엔지니어링)**, **Retention là vòng đời (lifecycle / 생명주기)** xác định đầu vào; **TTL và scheduled deletion** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Logs là nguồn rò rỉ phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TTL và scheduled deletion

TTL ở lưu trữ (storage / 저장소) tầng (layer / 계층) hữu ích nhưng phải hiểu guarantee: deletion có diễn ra đúng thời điểm hay eventual? Backup immutable có chính sách (policy / 정책) expiry riêng không? tìm kiếm (search / 검색) chỉ mục (index / 인덱스) có nhận delete sự kiện (event / 이벤트) không?

Retention SLO có thể định nghĩa khoảng thời gian tối đa từ eligibility tới deletion hoàn tất ở các active các hệ thống (systems / 시스템들).

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) minimization, purpose limitation và retention kỹ thuật (engineering / 엔지니어링)**, **TTL và scheduled deletion** nêu điều cần giải thích; **Logs là nguồn rò rỉ phổ biến** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Derived dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Logs là nguồn rò rỉ phổ biến

Ứng dụng (application / 애플리케이션) có thể cẩn thận với cơ sở dữ liệu (database / 데이터베이스) nhưng vô tình log đơn vị từ (token / 토큰), email, yêu cầu (request / 요청) body hoặc identifier nhạy cảm. Log thường được replicate sang nhiều khả năng quan sát (observability / 관측 가능성) các hệ thống (systems / 시스템들) và có retention dài.

Structured logging nên có allowlist/redaction chính sách (policy / 정책); “log tất cả rồi filter sau” tạo blast radius lớn.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) minimization, purpose limitation và retention kỹ thuật (engineering / 엔지니어링)**, **Logs là nguồn rò rỉ phổ biến** nêu điều cần giải thích; **Derived dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Kiểm soát truy cập (access control / 접근 제어) theo purpose** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Derived dữ liệu (data / 데이터)

Nếu raw dữ liệu (data / 데이터) bị xóa, aggregate/mô hình (model / 모델) tính năng (feature / 기능) có cần xóa không phụ thuộc khả năng liên kết lại cá nhân và chính sách (policy / 정책)/legal ngữ cảnh (context / 맥락). kỹ thuật (engineering / 엔지니어링) cần lineage để biết sản phẩm tạo ra (artifact / 산출물) nào được tạo từ nguồn nào thay vì tranh luận sau sự cố mà không có bằng chứng (evidence / 증거).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) minimization, purpose limitation và retention kỹ thuật (engineering / 엔지니어링)**, **Derived dữ liệu (data / 데이터)** nêu điều cần giải thích; **Kiểm soát truy cập (access control / 접근 제어) theo purpose** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Deletion workflow phải idempotent** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểm soát truy cập (access control / 접근 제어) theo purpose

RBAC chỉ nói role nào truy cập tài nguyên (resource / 자원); hệ thống phức tạp có thể cần attribute/ngữ cảnh (context / 맥락) để giới hạn theo tenant, workflow hoặc approved purpose. Nhưng chính sách (policy / 정책) càng tinh vi càng cần auditability và kiểm thử (test / 테스트), nếu không cấu hình (configuration / 구성) độ phức tạp (complexity / 복잡도) tự tạo bảo mật (security / 보안) gap.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) minimization, purpose limitation và retention kỹ thuật (engineering / 엔지니어링)**, **Kiểm soát truy cập (access control / 접근 제어) theo purpose** xác định đầu vào; **Deletion workflow phải idempotent** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Privacy và độ tin cậy (reliability / 신뢰성) liên hệ nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deletion workflow phải idempotent

Người dùng (user / 사용자) deletion thường đi qua nhiều services. thử lại (retry / 재시도) là bình thường; vì vậy delete handlers cần idempotent và có trạng thái theo dõi completion. thất bại (failure / 실패) ở một downstream không nên làm toàn workflow im lặng thành công.

Kiểm tra (audit / 감사) bản ghi (record / 레코드) có thể cần chứng minh deletion tiến trình (process / 프로세스) đã chạy mà không giữ lại chính payload đáng lẽ phải xóa.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) minimization, purpose limitation và retention kỹ thuật (engineering / 엔지니어링)**, **Deletion workflow phải idempotent** xác định đầu vào; **Privacy và độ tin cậy (reliability / 신뢰성) liên hệ nhau** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Privacy và độ tin cậy (reliability / 신뢰성) liên hệ nhau

Một deletion hàng đợi (queue / 큐) backlog là privacy sự cố (incident / 인시던트) tiềm năng. Retention job thất bại cần alert/SLO giống môi trường vận hành (production / 운영 환경) chuỗi xử lý (pipeline / 파이프라인) khác. Privacy điều khiển (control / 제어) chỉ tồn tại trên giấy nếu không có monitoring và đơn vị sở hữu (owner / 오너).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) minimization, purpose limitation và retention kỹ thuật (engineering / 엔지니어링)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Privacy và độ tin cậy (reliability / 신뢰성) liên hệ nhau** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Privacy principle phải trở thành dữ liệu (data / 데이터) vòng đời (lifecycle / 생명주기) có thể vận hành: collect ít hơn, bind usage với purpose, biết mọi bản sao (copy / 복사) ở đâu, đặt retention, propagate deletion và đo thất bại (failure / 실패). Privacy kỹ thuật (engineering / 엔지니어링) là hệ thống (system / 시스템) thiết kế (design / 설계) + quản trị (governance / 거버넌스) + khả năng quan sát (observability / 관측 가능성), không phải checkbox cuối dự án.

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
