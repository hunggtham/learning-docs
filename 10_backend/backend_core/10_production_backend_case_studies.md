# 10. môi trường vận hành (production / 운영 환경) backend trường hợp (case / 사례) studies

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **10. môi trường vận hành (production / 운영 환경) backend trường hợp (case / 사례) studies**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Trường hợp (case / 사례) 1 — Double charge sau hết thời gian chờ (timeout / 타임아웃)** đưa mô hình vào một trường hợp đủ cụ thể để quan sát; sau đó sang **Trường hợp (case / 사례) 2 — người dùng (user / 사용자) thấy dữ liệu tenant khác** để đối chiếu nhận định với dữ liệu và nguồn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Các trường hợp (case / 사례) dưới đây luyện đường suy luận `symptom → invariant → evidence → design`.
Chúng không thay thế chapter trước và không gắn với một khung phần mềm (framework / 프레임워크) duy nhất.

## Trường hợp (case / 사례) 1 — Double charge sau hết thời gian chờ (timeout / 타임아웃)

- **Symptom:** máy khách (client / 클라이언트) nhận hết thời gian chờ (timeout / 타임아웃) và bấm lại; có hai charge.
- **bất biến (invariant / 불변식):** một nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) của cùng subject/thứ tự (order / 순서) chỉ được charge
  một lần.
- **bằng chứng (evidence / 증거):** payment provider có một yêu cầu (request / 요청) thành công; ứng dụng (application / 애플리케이션) thử lại (retry / 재시도) có
  yêu cầu (request / 요청) ID khác.
- **thiết kế (design / 설계):** idempotency key theo thứ tự (order / 순서)/attempt, lưu kết quả (result / 결과), truy vấn (query / 쿼리) trạng thái
  trước thử lại (retry / 재시도) và ngân sách thời gian chờ (timeout budget / 타임아웃 예산) rõ ràng.

> **Chuyển mạch:** Trong **10. môi trường vận hành (production / 운영 환경) backend trường hợp (case / 사례) studies**, **Trường hợp (case / 사례) 1 — Double charge sau hết thời gian chờ (timeout / 타임아웃)** cho ta quy tắc; **Trường hợp (case / 사례) 2 — người dùng (user / 사용자) thấy dữ liệu tenant khác** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례) 3 — hàng đợi (queue / 큐) backlog tăng sau deploy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 2 — người dùng (user / 사용자) thấy dữ liệu tenant khác

- **Symptom:** detail đúng ở bộ nhớ đệm (cache / 캐시) nhưng thuộc tenant khác.
- **bất biến (invariant / 불변식):** mọi read/ghi (write / 쓰기) phải bị giới hạn bởi verified tenant định danh (identity / 식별자).
- **bằng chứng (evidence / 증거):** bộ nhớ đệm (cache / 캐시) key chỉ dùng `resource_id`, thiếu tenant; DB truy vấn (query / 쿼리) chính có
  filter nhưng bộ nhớ đệm (cache / 캐시) hit bypass filter.
- **thiết kế (design / 설계):** key chứa tenant/subject phạm vi (scope / 범위), authorization trước bộ nhớ đệm (cache / 캐시) read, kiểm thử (test / 테스트)
  cross-tenant và không bộ nhớ đệm (cache / 캐시) phản hồi (response / 응답) nhạy cảm nếu chính sách (policy / 정책) chưa rõ.

> **Chuyển mạch:** Ở chặng này của **10. môi trường vận hành (production / 운영 환경) backend trường hợp (case / 사례) studies**, **Trường hợp (case / 사례) 2 — người dùng (user / 사용자) thấy dữ liệu tenant khác** cho ta quy tắc; **Trường hợp (case / 사례) 3 — hàng đợi (queue / 큐) backlog tăng sau deploy** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례) 4 — Lost cập nhật (update / 업데이트) khi hai tab cùng sửa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 3 — hàng đợi (queue / 큐) backlog tăng sau deploy

- **Symptom:** hàng đợi (queue / 큐) age tăng, worker CPU thấp, thử lại (retry / 재시도) count cao.
- **bất biến (invariant / 불변식):** bên tiêu thụ (consumer / 소비자) phải xử lý message trong deadline và không tự nhân tải.
- **bằng chứng (evidence / 증거):** dấu vết (trace / 추적) cho thấy phụ thuộc (dependency / 의존성) hết thời gian chờ (timeout / 타임아웃); mỗi message bị thử lại (retry / 재시도) ở worker
  và máy khách (client / 클라이언트) thư viện (library / 라이브러리), tạo thử lại (retry / 재시도) storm.
- **thiết kế (design / 설계):** deadline propagation, một thử lại (retry / 재시도) đơn vị sở hữu (owner / 오너), backoff+jitter, tính đồng thời (concurrency / 동시성)
  cap, DLQ và alert theo hàng đợi (queue / 큐) age.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10. môi trường vận hành (production / 운영 환경) backend trường hợp (case / 사례) studies**, **Trường hợp (case / 사례) 3 — hàng đợi (queue / 큐) backlog tăng sau deploy** cho ta quy tắc; **Trường hợp (case / 사례) 4 — Lost cập nhật (update / 업데이트) khi hai tab cùng sửa** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례) 5 — Deploy làm API lỗi ngẫu nhiên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 4 — Lost cập nhật (update / 업데이트) khi hai tab cùng sửa

- **Symptom:** thay đổi của tab sau ghi đè tab trước.
- **bất biến (invariant / 불변식):** ghi (write / 쓰기) chỉ áp dụng trên phiên bản (version / 버전) mà máy khách (client / 클라이언트) đã đọc.
- **bằng chứng (evidence / 증거):** hai `UPDATE` đều thành công, không có phiên bản (version / 버전) predicate.
- **thiết kế (design / 설계):** optimistic tính đồng thời (concurrency / 동시성) với `ETag/If-Match` hoặc phiên bản (version / 버전) column;
  trả `409/412`, cho máy khách (client / 클라이언트) merge hoặc reload.

> **Chuyển mạch:** Trong **10. môi trường vận hành (production / 운영 환경) backend trường hợp (case / 사례) studies**, **Trường hợp (case / 사례) 4 — Lost cập nhật (update / 업데이트) khi hai tab cùng sửa** cho ta quy tắc; **Trường hợp (case / 사례) 5 — Deploy làm API lỗi ngẫu nhiên** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cách dùng trường hợp (case / 사례)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 5 — Deploy làm API lỗi ngẫu nhiên

- **Symptom:** rolling deploy có 5xx khi lược đồ (schema / 스키마) mới/chưa mới cùng chạy.
- **bất biến (invariant / 불변식):** mọi mã (code / 코드) phiên bản (version / 버전) đang active phải đọc/ghi lược đồ (schema / 스키마) tương thích.
- **bằng chứng (evidence / 증거):** old instance không hiểu column/enum mới; di chuyển (migration / 마이그레이션) destructive
  chạy trước drain traffic.
- **thiết kế (design / 설계):** expand → deploy compatible readers/writers → backfill → đặc tả hợp đồng (contract / 계약);
  kiểm thử mixed-version và quay lui (rollback / 롤백) plan.

> **Chuyển mạch:** Ở chặng này của **10. môi trường vận hành (production / 운영 환경) backend trường hợp (case / 사례) studies**, **Trường hợp (case / 사례) 5 — Deploy làm API lỗi ngẫu nhiên** cho ta quy tắc; **Cách dùng trường hợp (case / 사례)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례) 6 — bộ nhớ đệm (cache / 캐시) stampede sau vô hiệu hóa (invalidation / 무효화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cách dùng trường hợp (case / 사례)

Với sự cố (incident / 인시던트) thật, viết lại symptom bằng phạm vi (scope / 범위)/thời gian (time / 시간) cửa sổ (window / 윈도우), nêu bất biến (invariant / 불변식) bị đe
dọa, thu thập bằng chứng (evidence / 증거) trước khi chọn công cụ (tool / 도구)/khung phần mềm (framework / 프레임워크) fix. Sau mitigation, thêm
kiểm thử (test / 테스트) hoặc chỉ số (metric / 지표) đủ để lần sau phát hiện sớm hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10. môi trường vận hành (production / 운영 환경) backend trường hợp (case / 사례) studies**, **Cách dùng trường hợp (case / 사례)** cho ta quy tắc; **Trường hợp (case / 사례) 6 — bộ nhớ đệm (cache / 캐시) stampede sau vô hiệu hóa (invalidation / 무효화)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례) 7 — thử lại (retry / 재시도) storm làm phụ thuộc (dependency / 의존성) sập** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 6 — bộ nhớ đệm (cache / 캐시) stampede sau vô hiệu hóa (invalidation / 무효화)

- **Symptom:** một key hết hạn, origin CPU tăng vọt dù traffic không đổi.
- **bất biến (invariant / 불변식):** hot key không được tạo nhiều rebuild đồng thời vượt ngân sách (budget / 예산).
- **bằng chứng (evidence / 증거):** dấu vết (trace / 추적) cho thấy hàng trăm miss cùng timestamp; không có lease và
  TTL của cả batch được set giống nhau.
- **thiết kế (design / 설계):** single-flight/lease, jitter, stale-while-revalidate, origin
  tính đồng thời (concurrency / 동시성) cap và chỉ số (metric / 지표) `rebuild_in_flight`.

> **Chuyển mạch:** Trong **10. môi trường vận hành (production / 운영 환경) backend trường hợp (case / 사례) studies**, **Trường hợp (case / 사례) 6 — bộ nhớ đệm (cache / 캐시) stampede sau vô hiệu hóa (invalidation / 무효화)** cho ta quy tắc; **Trường hợp (case / 사례) 7 — thử lại (retry / 재시도) storm làm phụ thuộc (dependency / 의존성) sập** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례) 8 — Authorization đúng ở HTTP nhưng sai ở worker** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 7 — thử lại (retry / 재시도) storm làm phụ thuộc (dependency / 의존성) sập

- **Symptom:** provider chậm, số yêu cầu (request / 요청) tăng dù traffic vào ổn định.
- **bất biến (invariant / 불변식):** thử lại (retry / 재시도) không được làm tải lỗi lớn hơn tải gốc ngoài multiplier đã
  định trước.
- **bằng chứng (evidence / 증거):** gateway, dịch vụ (service / 서비스) và SDK cùng thử lại (retry / 재시도); backoff không có jitter.
- **thiết kế (design / 설계):** một thử lại (retry / 재시도) đơn vị sở hữu (owner / 오너), deadline propagation, bounded attempts, circuit
  breaker/bulkhead và alert theo thử lại (retry / 재시도) ratio.

> **Chuyển mạch:** Ở chặng này của **10. môi trường vận hành (production / 운영 환경) backend trường hợp (case / 사례) studies**, **Trường hợp (case / 사례) 7 — thử lại (retry / 재시도) storm làm phụ thuộc (dependency / 의존성) sập** cho ta quy tắc; **Trường hợp (case / 사례) 8 — Authorization đúng ở HTTP nhưng sai ở worker** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Capstone** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 8 — Authorization đúng ở HTTP nhưng sai ở worker

- **Symptom:** người dùng (user / 사용자) bị revoke nhưng export job vẫn đọc dữ liệu nhạy cảm.
- **bất biến (invariant / 불변식):** chính sách (policy / 정책) của async đường dẫn (path / 경로) phải được định nghĩa như sync đường dẫn (path / 경로).
- **bằng chứng (evidence / 증거):** worker tin snapshot yêu cầu (request / 요청) cũ, không kiểm tra tenant status và
  không có kiểm tra (audit / 감사) actor.
- **thiết kế (design / 설계):** chọn snapshot hoặc just-in-time authorization có chủ ý, lưu actor,
  phạm vi (scope / 범위) và chính sách (policy / 정책) phiên bản (version / 버전), thêm revoke kiểm thử (test / 테스트) và kill switch.

> **Chuyển mạch:** Case 8 cho thấy authorization phải sống qua cả async boundary, không chỉ ở HTTP handler. **Capstone** gom cùng invariant đó với timeout, transaction, cache, test và telemetry để người học kiểm tra một thiết kế hoàn chỉnh.

## Capstone

Chọn một API thật và viết một thiết kế (design / 설계) ghi chú (note / 노트) gồm yêu cầu (request / 요청) máy trạng thái (state machine / 상태 머신), đặc tả hợp đồng (contract / 계약),
định danh (identity / 식별자), giao dịch (transaction / 트랜잭션) ma trận (matrix / 행렬), bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책), async handoff, ngân sách thời gian chờ (timeout budget / 타임아웃 예산), kiểm thử (test / 테스트)
ma trận (matrix / 행렬), telemetry và quay lui (rollback / 롤백). thiết kế (design / 설계) chỉ hoàn tất khi mỗi dạng thất bại (failure mode / 실패 모드) có đơn vị sở hữu (owner / 오너)
và bằng chứng (evidence / 증거) tương ứng.

> **Bàn giao:** Sau **Capstone**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
