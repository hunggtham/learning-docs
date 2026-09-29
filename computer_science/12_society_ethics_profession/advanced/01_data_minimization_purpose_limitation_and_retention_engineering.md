# Dữ liệu (data / 데이터) minimization, purpose limitation và retention kỹ thuật (engineering / 엔지니어링)

> **Mạch đọc:** Đặt **dữ liệu (data / 데이터) minimization, purpose limitation và retention kỹ thuật (engineering / 엔지니어링)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **dữ liệu (data / 데이터) minimization** sang **Purpose limitation**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Privacy kỹ thuật (engineering / 엔지니어링) không chỉ là chính sách (policy / 정책) document. Một hệ thống thật sự bảo vệ dữ liệu phải biến nguyên tắc như **dữ liệu (data / 데이터) minimization**, **purpose limitation** và **retention** thành kiến trúc (architecture / 아키텍처), lược đồ (schema / 스키마), kiểm soát truy cập (access control / 접근 제어) và deletion workflow có thể kiểm chứng.

## Dữ liệu (data / 데이터) minimization

Dữ liệu (data / 데이터) minimization hỏi: để cung cấp năng lực (capability / 역량) này, hệ thống thực sự cần thu thập và giữ những fields nào? “Có thể hữu ích sau này” tạo dữ liệu (data / 데이터) liability: breach impact lớn hơn, authorization phức tạp hơn và deletion khó hơn.

Minimization nên diễn ra từ đầu vào (input / 입력) ranh giới (boundary / 경계). Nếu trường dữ liệu (field / 필드) không cần thiết, tốt hơn không thu thập thay vì thu thập rồi hứa không dùng.


> **Chuyển mạch:** Từ **dữ liệu (data / 데이터) minimization**, ta sang **Purpose limitation** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Purpose limitation

Cùng một dữ liệu có thể phù hợp cho mục đích A nhưng không mặc nhiên phù hợp cho B. kỹ thuật (engineering / 엔지니어링) cần gắn luồng dữ liệu (data flow / 데이터 흐름) với declared purpose và authorization ngữ cảnh (context / 맥락) thay vì coi mọi nội bộ (internal / 내부) dữ liệu (data / 데이터) là tài nguyên dùng tự do.

Điều này ảnh hưởng sự kiện (event / 이벤트) bus, analytics lake và tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링): bản sao (copy / 복사) dữ liệu (data / 데이터) sang hệ thống khác tạo thêm processing purpose và retention ranh giới (boundary / 경계) cần quản lý.


> **Chuyển mạch:** Từ **Purpose limitation**, ta sang **Retention là vòng đời (lifecycle / 생명주기)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Retention là vòng đời (lifecycle / 생명주기)

“Giữ 90 ngày” nghe đơn giản nhưng dữ liệu (data / 데이터) có thể tồn tại trong primary DB, replica, bộ nhớ đệm (cache / 캐시), tìm kiếm (search / 검색) chỉ mục (index / 인덱스), đối tượng (object / 객체) lưu trữ (storage / 저장소), log, backup và derived dataset. Retention kỹ thuật (engineering / 엔지니어링) cần inventory các copies và định nghĩa deletion ngữ nghĩa (semantics / 의미론) cho từng tầng (layer / 계층).

Một row bị delete khỏi primary không có nghĩa mọi derived bản sao (copy / 복사) biến mất ngay.


> **Chuyển mạch:** Từ **Retention là vòng đời (lifecycle / 생명주기)**, ta sang **TTL và scheduled deletion** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## TTL và scheduled deletion

TTL ở lưu trữ (storage / 저장소) tầng (layer / 계층) hữu ích nhưng phải hiểu guarantee: deletion có diễn ra đúng thời điểm hay eventual? Backup immutable có chính sách (policy / 정책) expiry riêng không? tìm kiếm (search / 검색) chỉ mục (index / 인덱스) có nhận delete sự kiện (event / 이벤트) không?

Retention SLO có thể định nghĩa khoảng thời gian tối đa từ eligibility tới deletion hoàn tất ở các active các hệ thống (systems / 시스템들).


> **Chuyển mạch:** Từ **TTL và scheduled deletion**, ta sang **Logs là nguồn rò rỉ phổ biến** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Logs là nguồn rò rỉ phổ biến

Ứng dụng (application / 애플리케이션) có thể cẩn thận với cơ sở dữ liệu (database / 데이터베이스) nhưng vô tình log đơn vị từ (token / 토큰), email, yêu cầu (request / 요청) body hoặc identifier nhạy cảm. Log thường được replicate sang nhiều khả năng quan sát (observability / 관측 가능성) các hệ thống (systems / 시스템들) và có retention dài.

Structured logging nên có allowlist/redaction chính sách (policy / 정책); “log tất cả rồi filter sau” tạo blast radius lớn.


> **Chuyển mạch:** Từ **Logs là nguồn rò rỉ phổ biến**, ta sang **Derived dữ liệu (data / 데이터)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Derived dữ liệu (data / 데이터)

Nếu raw dữ liệu (data / 데이터) bị xóa, aggregate/mô hình (model / 모델) tính năng (feature / 기능) có cần xóa không phụ thuộc khả năng liên kết lại cá nhân và chính sách (policy / 정책)/legal ngữ cảnh (context / 맥락). kỹ thuật (engineering / 엔지니어링) cần lineage để biết sản phẩm tạo ra (artifact / 산출물) nào được tạo từ nguồn nào thay vì tranh luận sau sự cố mà không có bằng chứng (evidence / 증거).


> **Chuyển mạch:** Từ **Derived dữ liệu (data / 데이터)**, ta sang **kiểm soát truy cập (access control / 접근 제어) theo purpose** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kiểm soát truy cập (access control / 접근 제어) theo purpose

RBAC chỉ nói role nào truy cập tài nguyên (resource / 자원); hệ thống phức tạp có thể cần attribute/ngữ cảnh (context / 맥락) để giới hạn theo tenant, workflow hoặc approved purpose. Nhưng chính sách (policy / 정책) càng tinh vi càng cần auditability và kiểm thử (test / 테스트), nếu không cấu hình (configuration / 구성) độ phức tạp (complexity / 복잡도) tự tạo bảo mật (security / 보안) gap.


> **Chuyển mạch:** Từ **kiểm soát truy cập (access control / 접근 제어) theo purpose**, ta sang **Deletion workflow phải idempotent** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Deletion workflow phải idempotent

Người dùng (user / 사용자) deletion thường đi qua nhiều services. thử lại (retry / 재시도) là bình thường; vì vậy delete handlers cần idempotent và có trạng thái theo dõi completion. thất bại (failure / 실패) ở một downstream không nên làm toàn workflow im lặng thành công.

Kiểm tra (audit / 감사) bản ghi (record / 레코드) có thể cần chứng minh deletion tiến trình (process / 프로세스) đã chạy mà không giữ lại chính payload đáng lẽ phải xóa.


> **Chuyển mạch:** Từ **Deletion workflow phải idempotent**, ta sang **Privacy và độ tin cậy (reliability / 신뢰성) liên hệ nhau** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Privacy và độ tin cậy (reliability / 신뢰성) liên hệ nhau

Một deletion hàng đợi (queue / 큐) backlog là privacy sự cố (incident / 인시던트) tiềm năng. Retention job thất bại cần alert/SLO giống môi trường vận hành (production / 운영 환경) chuỗi xử lý (pipeline / 파이프라인) khác. Privacy điều khiển (control / 제어) chỉ tồn tại trên giấy nếu không có monitoring và đơn vị sở hữu (owner / 오너).


> **Chuyển mạch:** Từ **Privacy và độ tin cậy (reliability / 신뢰성) liên hệ nhau**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Privacy principle phải trở thành dữ liệu (data / 데이터) vòng đời (lifecycle / 생명주기) có thể vận hành: collect ít hơn, bind usage với purpose, biết mọi bản sao (copy / 복사) ở đâu, đặt retention, propagate deletion và đo thất bại (failure / 실패). Privacy kỹ thuật (engineering / 엔지니어링) là hệ thống (system / 시스템) thiết kế (design / 설계) + quản trị (governance / 거버넌스) + khả năng quan sát (observability / 관측 가능성), không phải checkbox cuối dự án.

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 privacy threat models governance and accountability](./00_privacy_threat_models_governance_and_accountability.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
