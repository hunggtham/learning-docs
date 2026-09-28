# 01 — kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) từ nguyên lý nền tảng (first principles / 제일 원리)

> **Mạch đọc:** Đặt **01 — kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) từ nguyên lý nền tảng (first principles / 제일 원리)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Vấn đề thật sự không phải là "có dữ liệu"** sang **2. OLTP và OLAP là hai pressure khác nhau**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## 1. Vấn đề thật sự không phải là "có dữ liệu"

Một ứng dụng có thể lưu hàng triệu giao dịch mà doanh nghiệp vẫn chưa có một hệ thống dữ liệu đáng tin cậy. Dữ liệu vận hành thường được sinh ra để phục vụ yêu cầu (request / 요청) hiện tại: tạo đơn hàng, xác nhận thanh toán, cập nhật tài khoản. Trong khi đó câu hỏi phân tích thường cần ghép lịch sử từ nhiều hệ thống, giữ lại thay đổi theo thời gian và đọc một lượng dữ liệu lớn theo cách hoàn toàn khác.

Đây là khoảng cách mà kỹ thuật dữ liệu (Data Engineering / 데이터 엔지니어링) giải quyết. Công việc cốt lõi không phải "di chuyển dữ liệu", mà là duy trì ý nghĩa và tính đúng đắn của dữ liệu khi nó đi qua nhiều hệ thống, thời điểm và biểu diễn khác nhau.

Hãy tưởng tượng `orders` lưu trạng thái hiện tại của đơn hàng. Nếu một bản ghi (record / 레코드) hôm qua là `PENDING`, hôm nay thành `PAID`, cơ sở dữ liệu (database / 데이터베이스) vận hành có thể chỉ cần giá trị mới nhất. Nhưng câu hỏi "mỗi đơn hàng mất bao lâu để chuyển từ PENDING sang PAID trong sáu tháng qua?" cần lịch sử thay đổi. Một hệ thống tối ưu cho giao dịch (transaction / 트랜잭션) hiện tại không tự động trở thành hệ thống tối ưu cho historical analytics.

## 2. OLTP và OLAP là hai pressure khác nhau

Xử lý giao dịch trực tuyến (Online Transaction Processing, OLTP / 온라인 트랜잭션 처리) ưu tiên nhiều thao tác nhỏ, độ trễ (latency / 지연 시간) thấp và tính đúng đắn (correctness / 정확성) của giao dịch (transaction / 트랜잭션). Một yêu cầu (request / 요청) thường chạm rất ít row nhưng có thể yêu cầu locking, ràng buộc (constraint / 제약조건) và durability chặt chẽ.

Xử lý phân tích trực tuyến (Online Analytical Processing, OLAP / 온라인 분석 처리) thường đọc rất nhiều row, chỉ cần một phần column, thực hiện scan, aggregation và phép nối (join / 조인) lớn. Ở đây thông lượng (throughput / 처리량), compression, column pruning, partition pruning và parallelism quan trọng hơn độ trễ (latency / 지연 시간) của một cập nhật (update / 업데이트) đơn lẻ.

Sự khác biệt này giải thích vì sao "chỉ truy vấn (query / 쿼리) môi trường vận hành (production / 운영 환경) cơ sở dữ liệu (database / 데이터베이스)" thường không quy mô (scale / 규모) thành dữ liệu (data / 데이터) nền tảng (platform / 플랫폼). truy vấn (query / 쿼리) phân tích dài có thể tranh CPU, bộ nhớ (memory / 메모리), bộ nhớ đệm (cache / 캐시) và I/O với tải công việc (workload / 워크로드) phục vụ người dùng. Đồng thời lược đồ (schema / 스키마) chuẩn hóa cho giao dịch (transaction / 트랜잭션) không nhất thiết là hình dạng thuận tiện nhất cho analytics.

## 3. dữ liệu (data / 데이터) vòng đời (lifecycle / 생명주기)

Một cách nhìn hữu ích là theo vòng đời dữ liệu (data lifecycle / 데이터 수명 주기). Dữ liệu được sinh ra ở nguồn (source / 소스), được capture, vận chuyển, lưu, biến đổi, kiểm tra, publish cho bên tiêu thụ (consumer / 소비자), quan sát trong môi trường vận hành (production / 운영 환경) và cuối cùng archive hoặc xóa theo chính sách (policy / 정책).

Mỗi ranh giới tạo ra một dạng thất bại (failure mode / 실패 모드) mới. nguồn (source / 소스) có thể thay lược đồ (schema / 스키마). mạng (network / 네트워크) có thể thử lại (retry / 재시도) và gửi duplicate. bên tiêu thụ (consumer / 소비자) có thể crash sau khi ghi đầu ra (output / 출력) nhưng trước khi xác nhận message. Một partition có thể đến muộn. Một transformation có thể chạy thành công nhưng dùng sai timezone. Vì vậy tính đúng đắn (correctness / 정확성) không phải thuộc tính của một tệp (file / 파일) hoặc một job; nó là thuộc tính end-to-end của cả vòng đời (lifecycle / 생명주기).

## 4. Batch và streaming không đơn giản là "chậm" và "nhanh"

Batch processing gom một tập dữ liệu hữu hạn rồi xử lý nó như một đơn vị. Streaming processing coi đầu vào (input / 입력) là chuỗi sự kiện tiếp tục xuất hiện và hệ thống phải duy trì computation khi dữ liệu mới đến.

Điểm khác biệt quan trọng là trạng thái và thời gian. Với batch của ngày hôm qua, ta biết tương đối rõ tập đầu vào (input / 입력) cần xử lý. Với stream, tại 10:00 không thể chắc rằng mọi sự kiện (event / 이벤트) thuộc 09:55 đã đến. sự kiện (event / 이벤트) có thể bị delay trên thiết bị, broker hoặc mạng (network / 네트워크). Vì vậy streaming phải lập luận (reasoning / 추론) về sự kiện (event / 이벤트) thời gian (time / 시간), processing thời gian (time / 시간), late dữ liệu (data / 데이터), watermark và trạng thái (state / 상태) retention.

Một chuỗi xử lý (pipeline / 파이프라인) chạy mỗi năm phút vẫn có thể là micro-batch. Ngược lại, việc dùng Kafka không tự động biến toàn bộ kiến trúc (architecture / 아키텍처) thành streaming đúng nghĩa. Cần nhìn vào ngữ nghĩa (semantics / 의미론) của computation thay vì tên sản phẩm.

## 5. tính đúng đắn (correctness / 정확성) trước hiệu năng (performance / 성능)

Giả sử chuỗi xử lý (pipeline / 파이프라인) đọc payment sự kiện (event / 이벤트). bên tiêu thụ (consumer / 소비자) ghi sự kiện (event / 이벤트) vào warehouse rồi crash trước khi lần ghi nhận (commit / 커밋) offset. Sau restart, message được đọc lại. Nếu transformation chỉ `INSERT`, doanh thu có thể bị tính hai lần. Hệ thống rất nhanh nhưng sai.

Đây là lý do tính lũy đẳng (idempotency / 멱등성) là khái niệm trung tâm. Một thao tác (operation / 연산) idempotent có thể được thực hiện lại mà trạng thái cuối vẫn tương đương với việc thực hiện một lần. Trong dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인), điều này thường cần nghiệp vụ (business / 비즈니스) key ổn định, deduplication quy tắc (rule / 규칙), merge/upsert ngữ nghĩa (semantics / 의미론) hoặc giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) thích hợp.

Tính đúng đắn (correctness / 정확성) cũng không đồng nghĩa với "exactly-once" được ghi trên brochure. Exactly-once end-to-end phụ thuộc nguồn (source / 소스), vận chuyển (transport / 전송), processing và sink. Nếu một tầng không tham gia được vào giao dịch (transaction / 트랜잭션) hoặc deduplication giao thức (protocol / 프로토콜), guarantee của engine riêng lẻ không đủ để bảo đảm nghiệp vụ (business / 비즈니스) kết quả (result / 결과) exactly once.

## 6. lược đồ (schema / 스키마) là đặc tả hợp đồng (contract / 계약) về ý nghĩa

Lược đồ (schema / 스키마) không chỉ nói `amount` là `DECIMAL`. bên tiêu thụ (consumer / 소비자) còn cần biết currency là gì, timezone nào áp dụng, `null` nghĩa là unknown hay not-applicable, `customer_id` có stable qua merge account không và một row đại diện cho sự kiện (event / 이벤트) hay trạng thái (state / 상태) hiện tại.

Đó là lý do thay đổi lược đồ (schema / 스키마) có thể syntactically compatible nhưng semantically breaking. Thêm column nullable thường ít nguy hiểm về mặt parser, nhưng thay ý nghĩa của `status='CANCELLED'` có thể phá dashboard mà không tạo exception nào.

Cấp cao (senior / 시니어) lập luận (reasoning / 추론) vì vậy luôn tách lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) khỏi ngữ nghĩa (semantic / 의미적) tính tương thích (compatibility / 호환성).

## 7. mô hình dữ liệu (data model / 데이터 모델) bắt đầu từ grain

Trước khi thiết kế bảng (table / 테이블) phân tích, phải trả lời grain: một row đại diện cho cái gì? Một thứ tự (order / 순서), một thứ tự (order / 순서) item, một payment attempt hay một snapshot mỗi ngày?

Nếu grain không rõ, phép nối (join / 조인) rất dễ tạo fan-out. Ví dụ một thứ tự (order / 순서) có ba item và hai payment attempt. phép nối (join / 조인) trực tiếp ba bảng rồi `SUM(order_amount)` có thể nhân giá trị thành sáu bản sao. SQL vẫn hợp lệ và truy vấn (query / 쿼리) vẫn chạy xanh nhưng chỉ số (metric / 지표) sai.

Đây là liên kết (connection / 연결) quan trọng giữa kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) và SQL: học SQL không chỉ là nhớ cú pháp `JOIN`; phải hiểu cardinality, grain và bất biến (invariant / 불변식) của mô hình dữ liệu (data model / 데이터 모델).

## 8. Từ chuỗi xử lý (pipeline / 파이프라인) sang dữ liệu (data / 데이터) sản phẩm (product / 제품)

Chuỗi xử lý (pipeline / 파이프라인) chỉ mô tả đường xử lý. dữ liệu (data / 데이터) sản phẩm (product / 제품) nhấn mạnh rằng đầu ra (output / 출력) có bên tiêu thụ (consumer / 소비자), đơn vị sở hữu (owner / 오너), đặc tả hợp đồng (contract / 계약), SLO và vòng đời (lifecycle / 생명주기). Dataset quan trọng nên có câu trả lời cho các câu hỏi: ai chịu trách nhiệm, freshness mong đợi là bao lâu, nguồn (source / 소스) nào tạo ra nó, lược đồ (schema / 스키마) thay đổi theo quy trình nào, và bên tiêu thụ (consumer / 소비자) phải làm gì khi dữ liệu (data / 데이터) chất lượng (quality / 품질) thất bại (fail / 실패).

Mô hình tư duy (mental model / 사고 모델) này giúp tránh dữ liệu (data / 데이터) swamp: rất nhiều bảng (table / 테이블) tồn tại nhưng không ai biết bảng (table / 테이블) nào đáng tin, được tạo ra thế nào hoặc còn được sử dụng hay không.

## 9. bất biến (invariant / 불변식) là công cụ lập luận (reasoning / 추론) mạnh nhất

Khi gặp một kiến trúc (architecture / 아키텍처) mới, đừng bắt đầu bằng tên công cụ. Hãy viết bất biến (invariant / 불변식). Ví dụ: mỗi `payment_id` chỉ đóng góp doanh thu một lần; tổng item amount phải khớp thứ tự (order / 순서) amount theo quy tắc (rule / 규칙) đã định; sự kiện (event / 이벤트) không được publish trước khi giao dịch (transaction / 트랜잭션) nguồn lần ghi nhận (commit / 커밋); partition của ngày D chỉ được coi complete khi điều kiện completeness được thỏa mãn.

Sau đó hỏi từng thành phần (component / 컴포넌트) duy trì bất biến (invariant / 불변식) bằng cơ chế nào và bằng chứng (evidence / 증거) nào chứng minh điều đó trong môi trường vận hành (production / 운영 환경). Đây là cách đi từ sơ đồ kiến trúc (architecture / 아키텍처) đẹp sang kỹ thuật (engineering / 엔지니어링) có thể vận hành.

## 10. Các lớp của tính đúng đắn (correctness / 정확성)

Một dữ liệu (data / 데이터) sản phẩm (product / 제품) hiếm khi có một cờ `correct/incorrect` duy nhất. Nên tách ít nhất năm lớp:

| Lớp | Câu hỏi kiểm chứng |
|---|---|
| vận chuyển (transport / 전송) | bản ghi (record / 레코드) có bị mất, duplicate hoặc reorder ngoài giới hạn không? |
| lược đồ (schema / 스키마) | kiểu (type / 타입), nullability, enum và phiên bản (version / 버전) có tương thích không? |
| mô hình (model / 모델) | grain, key, phép nối (join / 조인) cardinality có đúng không? |
| nghiệp vụ (business / 비즈니스) | chỉ số (metric / 지표) có giữ phương trình/bất biến (invariant / 불변식) của lĩnh vực (domain / 도메인) không? |
| temporal | freshness, completeness và event-time cửa sổ (window / 윈도우) có đúng không? |

Một chuỗi xử lý (pipeline / 파이프라인) có thể pass vận chuyển (transport / 전송) nhưng thất bại (fail / 실패) nghiệp vụ (business / 비즈니스). Ví dụ tất cả message đến đủ nhưng `refund` bị tính như `sale`. cổng chất lượng (quality gate / 품질 게이트) phải chỉ rõ đang bảo vệ lớp nào.

## 11. ranh giới (boundary / 경계) của giao dịch (transaction / 트랜잭션) và publish

Nguồn (source / 소스) giao dịch (transaction / 트랜잭션), vận chuyển (transport / 전송) acknowledgement, processing checkpoint và sink lần ghi nhận (commit / 커밋) thường là bốn máy trạng thái (state machine / 상태 머신) khác nhau. Không được gọi một bản ghi (record / 레코드) là “đã xử lý” nếu chỉ có một trạng thái (state / 상태) trong bốn trạng thái (state / 상태) đã chuyển.

Mẫu lập luận (reasoning / 추론) cơ bản:

```text
source commit
  → durable capture
  → deterministic transform
  → sink commit
  → publish marker / serving pointer
```

Nếu crash giữa hai bước, khôi phục (recovery / 복구) phải biết bước nào đã hoàn tất. Idempotent ghi (write / 쓰기) hoặc giao dịch (transaction / 트랜잭션) coordinator nối các trạng thái (state / 상태) đó; offset riêng lẻ không làm được.

## 12. Worked example: thứ tự (order / 순서) revenue

Giả sử nguồn (source / 소스) có `order_created`, `payment_captured` và `refund_issued`. chỉ số (metric / 지표) doanh thu không phải tổng mọi amount; nó là:

```text
net_revenue = Σ captured_amount − Σ valid_refund_amount
```

Muốn chứng minh chỉ số (metric / 지표) đúng cần định nghĩa `valid_refund`: refund có thể đến sau nhiều ngày, có thể partial, và có thể bị thử lại (retry / 재시도). mô hình (model / 모델) phải lưu sự kiện (event / 이벤트) định danh (identity / 식별자), currency, sự kiện (event / 이벤트) thời gian (time / 시간), nguồn (source / 소스) phiên bản (version / 버전) và trạng thái reconciliation. Chỉ kiểm tra row count sẽ không phát hiện double-capture.

## 13. quyết định (decision / 결정) bản ghi (record / 레코드) tối thiểu

Mỗi ranh giới (boundary / 경계) quan trọng nên ghi lại:

1. bất biến (invariant / 불변식) cần bảo vệ;
2. giả định (assumption / 가정) về thứ tự (ordering / 순서), clock, lược đồ (schema / 스키마) hoặc retention;
3. thất bại (failure / 실패) cửa sổ (window / 윈도우) và hành vi (behavior / 동작) khi thử lại (retry / 재시도);
4. bằng chứng (evidence / 증거)/chỉ số (metric / 지표) chứng minh guarantee;
5. sự đánh đổi (trade-off / 트레이드오프) về độ trễ (latency / 지연 시간), chi phí (cost / 비용), completeness và operational độ phức tạp (complexity / 복잡도).

Quyết định (decision / 결정) bản ghi (record / 레코드) ngắn nhưng giúp phân biệt guarantee thật với khẩu hiệu như “exactly once”, “real thời gian (time / 시간)” hoặc “high chất lượng (quality / 품질)”.

> **Bàn giao:** Sau **13. quyết định (decision / 결정) bản ghi (record / 레코드) tối thiểu**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [02 pipeline architecture](./02_pipeline_architecture.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
