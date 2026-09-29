# 10. môi trường vận hành (production / 운영 환경) backend trường hợp (case / 사례) studies

> **Mạch đọc:** Đặt **10. môi trường vận hành (production / 운영 환경) backend trường hợp (case / 사례) studies** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **trường hợp (case / 사례) 1 — Double charge sau hết thời gian chờ (timeout / 타임아웃)** sang **trường hợp (case / 사례) 2 — người dùng (user / 사용자) thấy dữ liệu tenant khác**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Các trường hợp (case / 사례) dưới đây luyện đường suy luận `symptom → invariant → evidence → design`.
Chúng không thay thế chapter trước và không gắn với một khung phần mềm (framework / 프레임워크) duy nhất.

## Trường hợp (case / 사례) 1 — Double charge sau hết thời gian chờ (timeout / 타임아웃)
Phần “Trường hợp (case / 사례) 1 — Double charge sau hết thời gian chờ (timeout / 타임아웃)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- **Symptom:** máy khách (client / 클라이언트) nhận hết thời gian chờ (timeout / 타임아웃) và bấm lại; có hai charge.
- **bất biến (invariant / 불변식):** một nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) của cùng subject/thứ tự (order / 순서) chỉ được charge
  một lần.
- **bằng chứng (evidence / 증거):** payment provider có một yêu cầu (request / 요청) thành công; ứng dụng (application / 애플리케이션) thử lại (retry / 재시도) có
  yêu cầu (request / 요청) ID khác.
- **thiết kế (design / 설계):** idempotency key theo thứ tự (order / 순서)/attempt, lưu kết quả (result / 결과), truy vấn (query / 쿼리) trạng thái
  trước thử lại (retry / 재시도) và ngân sách thời gian chờ (timeout budget / 타임아웃 예산) rõ ràng.


> **Chuyển mạch:** Từ **trường hợp (case / 사례) 1 — Double charge sau hết thời gian chờ (timeout / 타임아웃)**, ta sang **trường hợp (case / 사례) 2 — người dùng (user / 사용자) thấy dữ liệu tenant khác** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trường hợp (case / 사례) 2 — người dùng (user / 사용자) thấy dữ liệu tenant khác
Phần “Trường hợp (case / 사례) 2 — người dùng (user / 사용자) thấy dữ liệu tenant khác” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- **Symptom:** detail đúng ở bộ nhớ đệm (cache / 캐시) nhưng thuộc tenant khác.
- **bất biến (invariant / 불변식):** mọi read/ghi (write / 쓰기) phải bị giới hạn bởi verified tenant định danh (identity / 식별자).
- **bằng chứng (evidence / 증거):** bộ nhớ đệm (cache / 캐시) key chỉ dùng `resource_id`, thiếu tenant; DB truy vấn (query / 쿼리) chính có
  filter nhưng bộ nhớ đệm (cache / 캐시) hit bypass filter.
- **thiết kế (design / 설계):** key chứa tenant/subject phạm vi (scope / 범위), authorization trước bộ nhớ đệm (cache / 캐시) read, kiểm thử (test / 테스트)
  cross-tenant và không bộ nhớ đệm (cache / 캐시) phản hồi (response / 응답) nhạy cảm nếu chính sách (policy / 정책) chưa rõ.


> **Chuyển mạch:** Từ **trường hợp (case / 사례) 2 — người dùng (user / 사용자) thấy dữ liệu tenant khác**, ta sang **trường hợp (case / 사례) 3 — hàng đợi (queue / 큐) backlog tăng sau deploy** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trường hợp (case / 사례) 3 — hàng đợi (queue / 큐) backlog tăng sau deploy
Phần “Trường hợp (case / 사례) 3 — hàng đợi (queue / 큐) backlog tăng sau deploy” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- **Symptom:** hàng đợi (queue / 큐) age tăng, worker CPU thấp, thử lại (retry / 재시도) count cao.
- **bất biến (invariant / 불변식):** bên tiêu thụ (consumer / 소비자) phải xử lý message trong deadline và không tự nhân tải.
- **bằng chứng (evidence / 증거):** dấu vết (trace / 추적) cho thấy phụ thuộc (dependency / 의존성) hết thời gian chờ (timeout / 타임아웃); mỗi message bị thử lại (retry / 재시도) ở worker
  và máy khách (client / 클라이언트) thư viện (library / 라이브러리), tạo thử lại (retry / 재시도) storm.
- **thiết kế (design / 설계):** deadline propagation, một thử lại (retry / 재시도) đơn vị sở hữu (owner / 오너), backoff+jitter, tính đồng thời (concurrency / 동시성)
  cap, DLQ và alert theo hàng đợi (queue / 큐) age.


> **Chuyển mạch:** Từ **trường hợp (case / 사례) 3 — hàng đợi (queue / 큐) backlog tăng sau deploy**, ta sang **trường hợp (case / 사례) 4 — Lost cập nhật (update / 업데이트) khi hai tab cùng sửa** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trường hợp (case / 사례) 4 — Lost cập nhật (update / 업데이트) khi hai tab cùng sửa
Phần “Trường hợp (case / 사례) 4 — Lost cập nhật (update / 업데이트) khi hai tab cùng sửa” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- **Symptom:** thay đổi của tab sau ghi đè tab trước.
- **bất biến (invariant / 불변식):** ghi (write / 쓰기) chỉ áp dụng trên phiên bản (version / 버전) mà máy khách (client / 클라이언트) đã đọc.
- **bằng chứng (evidence / 증거):** hai `UPDATE` đều thành công, không có phiên bản (version / 버전) predicate.
- **thiết kế (design / 설계):** optimistic tính đồng thời (concurrency / 동시성) với `ETag/If-Match` hoặc phiên bản (version / 버전) column;
  trả `409/412`, cho máy khách (client / 클라이언트) merge hoặc reload.


> **Chuyển mạch:** Từ **trường hợp (case / 사례) 4 — Lost cập nhật (update / 업데이트) khi hai tab cùng sửa**, ta sang **trường hợp (case / 사례) 5 — Deploy làm API lỗi ngẫu nhiên** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trường hợp (case / 사례) 5 — Deploy làm API lỗi ngẫu nhiên
Phần “Trường hợp (case / 사례) 5 — Deploy làm API lỗi ngẫu nhiên” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- **Symptom:** rolling deploy có 5xx khi lược đồ (schema / 스키마) mới/chưa mới cùng chạy.
- **bất biến (invariant / 불변식):** mọi mã (code / 코드) phiên bản (version / 버전) đang active phải đọc/ghi lược đồ (schema / 스키마) tương thích.
- **bằng chứng (evidence / 증거):** old instance không hiểu column/enum mới; di chuyển (migration / 마이그레이션) destructive
  chạy trước drain traffic.
- **thiết kế (design / 설계):** expand → deploy compatible readers/writers → backfill → đặc tả hợp đồng (contract / 계약);
  kiểm thử mixed-version và quay lui (rollback / 롤백) plan.


> **Chuyển mạch:** Từ **trường hợp (case / 사례) 5 — Deploy làm API lỗi ngẫu nhiên**, ta sang **Cách dùng trường hợp (case / 사례)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cách dùng trường hợp (case / 사례)

Với sự cố (incident / 인시던트) thật, viết lại symptom bằng phạm vi (scope / 범위)/thời gian (time / 시간) cửa sổ (window / 윈도우), nêu bất biến (invariant / 불변식) bị đe
dọa, thu thập bằng chứng (evidence / 증거) trước khi chọn công cụ (tool / 도구)/khung phần mềm (framework / 프레임워크) fix. Sau mitigation, thêm
kiểm thử (test / 테스트) hoặc chỉ số (metric / 지표) đủ để lần sau phát hiện sớm hơn.


> **Chuyển mạch:** Từ **Cách dùng trường hợp (case / 사례)**, ta sang **trường hợp (case / 사례) 6 — bộ nhớ đệm (cache / 캐시) stampede sau vô hiệu hóa (invalidation / 무효화)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trường hợp (case / 사례) 6 — bộ nhớ đệm (cache / 캐시) stampede sau vô hiệu hóa (invalidation / 무효화)
Phần “Trường hợp (case / 사례) 6 — bộ nhớ đệm (cache / 캐시) stampede sau vô hiệu hóa (invalidation / 무효화)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- **Symptom:** một key hết hạn, origin CPU tăng vọt dù traffic không đổi.
- **bất biến (invariant / 불변식):** hot key không được tạo nhiều rebuild đồng thời vượt ngân sách (budget / 예산).
- **bằng chứng (evidence / 증거):** dấu vết (trace / 추적) cho thấy hàng trăm miss cùng timestamp; không có lease và
  TTL của cả batch được set giống nhau.
- **thiết kế (design / 설계):** single-flight/lease, jitter, stale-while-revalidate, origin
  tính đồng thời (concurrency / 동시성) cap và chỉ số (metric / 지표) `rebuild_in_flight`.


> **Chuyển mạch:** Từ **trường hợp (case / 사례) 6 — bộ nhớ đệm (cache / 캐시) stampede sau vô hiệu hóa (invalidation / 무효화)**, ta sang **trường hợp (case / 사례) 7 — thử lại (retry / 재시도) storm làm phụ thuộc (dependency / 의존성) sập** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trường hợp (case / 사례) 7 — thử lại (retry / 재시도) storm làm phụ thuộc (dependency / 의존성) sập
Phần “Trường hợp (case / 사례) 7 — thử lại (retry / 재시도) storm làm phụ thuộc (dependency / 의존성) sập” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- **Symptom:** provider chậm, số yêu cầu (request / 요청) tăng dù traffic vào ổn định.
- **bất biến (invariant / 불변식):** thử lại (retry / 재시도) không được làm tải lỗi lớn hơn tải gốc ngoài multiplier đã
  định trước.
- **bằng chứng (evidence / 증거):** gateway, dịch vụ (service / 서비스) và SDK cùng thử lại (retry / 재시도); backoff không có jitter.
- **thiết kế (design / 설계):** một thử lại (retry / 재시도) đơn vị sở hữu (owner / 오너), deadline propagation, bounded attempts, circuit
  breaker/bulkhead và alert theo thử lại (retry / 재시도) ratio.


> **Chuyển mạch:** Từ **trường hợp (case / 사례) 7 — thử lại (retry / 재시도) storm làm phụ thuộc (dependency / 의존성) sập**, ta sang **trường hợp (case / 사례) 8 — Authorization đúng ở HTTP nhưng sai ở worker** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trường hợp (case / 사례) 8 — Authorization đúng ở HTTP nhưng sai ở worker
Phần “Trường hợp (case / 사례) 8 — Authorization đúng ở HTTP nhưng sai ở worker” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- **Symptom:** người dùng (user / 사용자) bị revoke nhưng export job vẫn đọc dữ liệu nhạy cảm.
- **bất biến (invariant / 불변식):** chính sách (policy / 정책) của async đường dẫn (path / 경로) phải được định nghĩa như sync đường dẫn (path / 경로).
- **bằng chứng (evidence / 증거):** worker tin snapshot yêu cầu (request / 요청) cũ, không kiểm tra tenant status và
  không có kiểm tra (audit / 감사) actor.
- **thiết kế (design / 설계):** chọn snapshot hoặc just-in-time authorization có chủ ý, lưu actor,
  phạm vi (scope / 범위) và chính sách (policy / 정책) phiên bản (version / 버전), thêm revoke kiểm thử (test / 테스트) và kill switch.


> **Chuyển mạch:** Từ **trường hợp (case / 사례) 8 — Authorization đúng ở HTTP nhưng sai ở worker**, ta sang **Capstone** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Capstone

Chọn một API thật và viết một thiết kế (design / 설계) ghi chú (note / 노트) gồm yêu cầu (request / 요청) máy trạng thái (state machine / 상태 머신), đặc tả hợp đồng (contract / 계약),
định danh (identity / 식별자), giao dịch (transaction / 트랜잭션) ma trận (matrix / 행렬), bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책), async handoff, ngân sách thời gian chờ (timeout budget / 타임아웃 예산), kiểm thử (test / 테스트)
ma trận (matrix / 행렬), telemetry và quay lui (rollback / 롤백). thiết kế (design / 설계) chỉ hoàn tất khi mỗi dạng thất bại (failure mode / 실패 모드) có đơn vị sở hữu (owner / 오너)
và bằng chứng (evidence / 증거) tương ứng.

> **Bàn giao:** Sau **Capstone**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 backend request lifecycle](./00_backend_request_lifecycle.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
