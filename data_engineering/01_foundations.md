# 01 — Data Engineering từ first principles

## 1. Vấn đề thật sự không phải là "có dữ liệu"

Một ứng dụng có thể lưu hàng triệu giao dịch mà doanh nghiệp vẫn chưa có một hệ thống dữ liệu đáng tin cậy. Dữ liệu vận hành thường được sinh ra để phục vụ request hiện tại: tạo đơn hàng, xác nhận thanh toán, cập nhật tài khoản. Trong khi đó câu hỏi phân tích thường cần ghép lịch sử từ nhiều hệ thống, giữ lại thay đổi theo thời gian và đọc một lượng dữ liệu lớn theo cách hoàn toàn khác.

Đây là khoảng cách mà kỹ thuật dữ liệu (Data Engineering / 데이터 엔지니어링) giải quyết. Công việc cốt lõi không phải "di chuyển dữ liệu", mà là duy trì ý nghĩa và tính đúng đắn của dữ liệu khi nó đi qua nhiều hệ thống, thời điểm và biểu diễn khác nhau.

Hãy tưởng tượng `orders` lưu trạng thái hiện tại của đơn hàng. Nếu một record hôm qua là `PENDING`, hôm nay thành `PAID`, database vận hành có thể chỉ cần giá trị mới nhất. Nhưng câu hỏi "mỗi đơn hàng mất bao lâu để chuyển từ PENDING sang PAID trong sáu tháng qua?" cần lịch sử thay đổi. Một hệ thống tối ưu cho transaction hiện tại không tự động trở thành hệ thống tối ưu cho historical analytics.

## 2. OLTP và OLAP là hai pressure khác nhau

Xử lý giao dịch trực tuyến (Online Transaction Processing, OLTP / 온라인 트랜잭션 처리) ưu tiên nhiều thao tác nhỏ, latency thấp và correctness của transaction. Một request thường chạm rất ít row nhưng có thể yêu cầu locking, constraint và durability chặt chẽ.

Xử lý phân tích trực tuyến (Online Analytical Processing, OLAP / 온라인 분석 처리) thường đọc rất nhiều row, chỉ cần một phần column, thực hiện scan, aggregation và join lớn. Ở đây throughput, compression, column pruning, partition pruning và parallelism quan trọng hơn latency của một update đơn lẻ.

Sự khác biệt này giải thích vì sao "chỉ query production database" thường không scale thành data platform. Query phân tích dài có thể tranh CPU, memory, cache và I/O với workload phục vụ người dùng. Đồng thời schema chuẩn hóa cho transaction không nhất thiết là hình dạng thuận tiện nhất cho analytics.

## 3. Data lifecycle

Một cách nhìn hữu ích là theo vòng đời dữ liệu (data lifecycle / 데이터 수명 주기). Dữ liệu được sinh ra ở source, được capture, vận chuyển, lưu, biến đổi, kiểm tra, publish cho consumer, quan sát trong production và cuối cùng archive hoặc xóa theo policy.

Mỗi ranh giới tạo ra một failure mode mới. Source có thể thay schema. Network có thể retry và gửi duplicate. Consumer có thể crash sau khi ghi output nhưng trước khi xác nhận message. Một partition có thể đến muộn. Một transformation có thể chạy thành công nhưng dùng sai timezone. Vì vậy correctness không phải thuộc tính của một file hoặc một job; nó là thuộc tính end-to-end của cả lifecycle.

## 4. Batch và streaming không đơn giản là "chậm" và "nhanh"

Batch processing gom một tập dữ liệu hữu hạn rồi xử lý nó như một đơn vị. Streaming processing coi input là chuỗi sự kiện tiếp tục xuất hiện và hệ thống phải duy trì computation khi dữ liệu mới đến.

Điểm khác biệt quan trọng là trạng thái và thời gian. Với batch của ngày hôm qua, ta biết tương đối rõ tập input cần xử lý. Với stream, tại 10:00 không thể chắc rằng mọi event thuộc 09:55 đã đến. Event có thể bị delay trên thiết bị, broker hoặc network. Vì vậy streaming phải reasoning về event time, processing time, late data, watermark và state retention.

Một pipeline chạy mỗi năm phút vẫn có thể là micro-batch. Ngược lại, việc dùng Kafka không tự động biến toàn bộ architecture thành streaming đúng nghĩa. Cần nhìn vào semantics của computation thay vì tên sản phẩm.

## 5. Correctness trước performance

Giả sử pipeline đọc payment event. Consumer ghi event vào warehouse rồi crash trước khi commit offset. Sau restart, message được đọc lại. Nếu transformation chỉ `INSERT`, doanh thu có thể bị tính hai lần. Hệ thống rất nhanh nhưng sai.

Đây là lý do tính lũy đẳng (idempotency / 멱등성) là khái niệm trung tâm. Một operation idempotent có thể được thực hiện lại mà trạng thái cuối vẫn tương đương với việc thực hiện một lần. Trong data pipeline, điều này thường cần business key ổn định, deduplication rule, merge/upsert semantics hoặc transaction boundary thích hợp.

Correctness cũng không đồng nghĩa với "exactly-once" được ghi trên brochure. Exactly-once end-to-end phụ thuộc source, transport, processing và sink. Nếu một tầng không tham gia được vào transaction hoặc deduplication protocol, guarantee của engine riêng lẻ không đủ để bảo đảm business result exactly once.

## 6. Schema là contract về ý nghĩa

Schema không chỉ nói `amount` là `DECIMAL`. Consumer còn cần biết currency là gì, timezone nào áp dụng, `null` nghĩa là unknown hay not-applicable, `customer_id` có stable qua merge account không và một row đại diện cho event hay state hiện tại.

Đó là lý do thay đổi schema có thể syntactically compatible nhưng semantically breaking. Thêm column nullable thường ít nguy hiểm về mặt parser, nhưng thay ý nghĩa của `status='CANCELLED'` có thể phá dashboard mà không tạo exception nào.

Senior reasoning vì vậy luôn tách schema compatibility khỏi semantic compatibility.

## 7. Data model bắt đầu từ grain

Trước khi thiết kế table phân tích, phải trả lời grain: một row đại diện cho cái gì? Một order, một order item, một payment attempt hay một snapshot mỗi ngày?

Nếu grain không rõ, join rất dễ tạo fan-out. Ví dụ một order có ba item và hai payment attempt. Join trực tiếp ba bảng rồi `SUM(order_amount)` có thể nhân giá trị thành sáu bản sao. SQL vẫn hợp lệ và query vẫn chạy xanh nhưng metric sai.

Đây là connection quan trọng giữa Data Engineering và SQL: học SQL không chỉ là nhớ cú pháp `JOIN`; phải hiểu cardinality, grain và invariant của data model.

## 8. Từ pipeline sang data product

Pipeline chỉ mô tả đường xử lý. Data product nhấn mạnh rằng output có consumer, owner, contract, SLO và lifecycle. Dataset quan trọng nên có câu trả lời cho các câu hỏi: ai chịu trách nhiệm, freshness mong đợi là bao lâu, source nào tạo ra nó, schema thay đổi theo quy trình nào, và consumer phải làm gì khi data quality fail.

Mental model này giúp tránh data swamp: rất nhiều table tồn tại nhưng không ai biết table nào đáng tin, được tạo ra thế nào hoặc còn được sử dụng hay không.

## 9. Invariant là công cụ reasoning mạnh nhất

Khi gặp một architecture mới, đừng bắt đầu bằng tên công cụ. Hãy viết invariant. Ví dụ: mỗi `payment_id` chỉ đóng góp doanh thu một lần; tổng item amount phải khớp order amount theo rule đã định; event không được publish trước khi transaction nguồn commit; partition của ngày D chỉ được coi complete khi điều kiện completeness được thỏa mãn.

Sau đó hỏi từng component duy trì invariant bằng cơ chế nào và evidence nào chứng minh điều đó trong production. Đây là cách đi từ sơ đồ architecture đẹp sang engineering có thể vận hành.