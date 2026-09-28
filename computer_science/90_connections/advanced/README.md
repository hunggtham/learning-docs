# Kết nối xuyên tầng nâng cao

> **Mạch đọc:** Đọc **Kết nối xuyên tầng nâng cao** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **chuẩn gốc (canonical / 정본) liên kết (connection / 연결) paths** sang **Connections đã được hấp thụ vào bốn đường dẫn (path / 경로) hiện có**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Các chapter ở đây không lặp lại lĩnh vực (domain / 도메인) content. Chúng bắt đầu từ một thuộc tính end-to-end hoặc symptom môi trường vận hành (production / 운영 환경) rồi đi xuyên các lớp trừu tượng (abstraction / 추상화) để trả lời: bất biến (invariant / 불변식) nào bị vi phạm, lower tầng (layer / 계층) nào quyết định hành vi (behavior / 동작), và bằng chứng (evidence / 증거) nào đủ để chứng minh nhân quả (causal / 인과적) đường dẫn (path / 경로).

## Chuẩn gốc (canonical / 정본) liên kết (connection / 연결) paths

1. [Gỡ lỗi xuyên abstraction layers](./00_debugging_across_abstraction_layers.md)
2. [Request path: DNS → TCP/TLS → proxy/load balancer → runtime → DB/storage](./01_end_to_end_latency_browser_edge_service_db_storage.md)
3. [Correctness path: CPU cache → memory ordering → language memory model → concurrency bug](./02_correctness_path_language_os_cpu_memory_ordering.md)
4. [Durability path: application transaction → MVCC/WAL → filesystem → storage → replication](./03_durability_path_application_commit_wal_filesystem_device.md)


> **Chuyển mạch:** Từ **chuẩn gốc (canonical / 정본) liên kết (connection / 연결) paths**, ta sang **Connections đã được hấp thụ vào bốn đường dẫn (path / 경로) hiện có** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Connections đã được hấp thụ vào bốn đường dẫn (path / 경로) hiện có

Không tạo chapter riêng chỉ để có thêm tên liên kết (connection / 연결).

**thử lại (retry / 재시도) → hết thời gian chờ (timeout / 타임아웃) → overload → hàng đợi (queue / 큐) → backpressure → cascading thất bại (failure / 실패)** nằm trong yêu cầu (request / 요청)/độ trễ (latency / 지연 시간) đường dẫn (path / 경로), vì đây là một vòng phản hồi (feedback loop / 피드백 루프) làm thay đổi arrival tỷ lệ (rate / 비율) và dịch vụ (service / 서비스) thời gian (time / 시간) trên cùng nhân quả (causal / 인과적) đồ thị (graph / 그래프).

**định danh (identity / 식별자) → authorization → secret → TLS → dịch vụ (service / 서비스) ranh giới (boundary / 경계) → sự cố (incident / 인시던트) containment** nằm trong debugging đường dẫn (path / 경로), vì đây là authority đường dẫn (path / 경로) cần được reconstruct khi thất bại (failure / 실패) hoặc compromise lan qua nhiều dịch vụ (service / 서비스) boundaries.

**CPU bộ nhớ đệm (cache / 캐시) → bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) → ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델) → tính đồng thời (concurrency / 동시성) bug** là tính đúng đắn (correctness / 정확성) đường dẫn (path / 경로) và phải luôn phân biệt vật lý (physical / 물리적) visibility với language-level happens-before.

**ứng dụng (application / 애플리케이션) giao dịch (transaction / 트랜잭션) → MVCC/WAL → filesystem → lưu trữ (storage / 저장소) → replication** là durability đường dẫn (path / 경로) và phải phân biệt visibility, cục bộ (local / 로컬) persistence, quorum lần ghi nhận (commit / 커밋) và backup/khôi phục (recovery / 복구).


> **Chuyển mạch:** Từ **Connections đã được hấp thụ vào bốn đường dẫn (path / 경로) hiện có**, ta sang **Cách dùng khi gỡ lỗi (debug / 디버그) môi trường vận hành (production / 운영 환경)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cách dùng khi gỡ lỗi (debug / 디버그) môi trường vận hành (production / 운영 환경)

Bắt đầu từ thuộc tính (property / 속성) người dùng quan sát được: sai dữ liệu, mất dữ liệu, hết thời gian chờ (timeout / 타임아웃), duplicate side tác động (effect / 효과), auth thất bại (failure / 실패) hoặc độ trễ (latency / 지연 시간) tail. Sau đó:

```text
1. Viết invariant bị nghi vi phạm.
2. Dựng timeline/causal graph.
3. Xác định boundary có queue, ownership, authority hoặc representation change.
4. Thu evidence ở tầng hiện tại.
5. Chỉ đi xuống lower layer khi contract hiện tại không giải thích được symptom.
6. Quay lại abstraction sở hữu invariant để đặt fix.
```

Không mặc định nguyên nhân ở tầng (layer / 계층) thấp nhất. CPU/bộ nhớ đệm (cache / 캐시)/kernel chỉ nên xuất hiện khi bằng chứng (evidence / 증거) cho thấy chúng thực sự quyết định hành vi (behavior / 동작).


> **Chuyển mạch:** Từ **Cách dùng khi gỡ lỗi (debug / 디버그) môi trường vận hành (production / 운영 환경)**, ta sang **bằng chứng vận hành (production evidence / 운영 증거)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bằng chứng vận hành (production evidence / 운영 증거)

Cross-layer bằng chứng (evidence / 증거) phải nối được nhiều loại tín hiệu (signal / 신호): dấu vết (trace / 추적)/span, hàng đợi (queue / 큐)/pool wait, thời gian chạy (runtime / 런타임) pause, scheduler pressure, DB wait/plan/WAL, mạng (network / 네트워크) liên kết (connection / 연결)/retransmission, certificate/chính sách (policy / 정책) định danh (identity / 식별자), lưu trữ (storage / 저장소) flush/hàng đợi (queue / 큐), quorum/replica position và hardware counters khi cần.

Một dashboard đơn lẻ thường chỉ cho symptom. Mục tiêu là xây **nhân quả (causal / 인과적) mô hình (model / 모델) có confidence**, dùng nhiều independent signals để phân biệt correlation với cơ chế (mechanism / 메커니즘).


> **Chuyển mạch:** Từ **bằng chứng vận hành (production evidence / 운영 증거)**, ta sang **Quy tắc mở rộng** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Quy tắc mở rộng

Nếu liên kết (connection / 연결) mới có thể được hấp thụ như một section sâu hơn trong bốn chuẩn gốc (canonical / 정본) đường dẫn (path / 경로) hiện tại, không tạo chapter mới. Chỉ thêm tệp (file / 파일) khi có một end-to-end bất biến (invariant / 불변식) độc lập, một thất bại (failure / 실패) propagation mẫu (pattern / 패턴) khác bản chất và đủ nội dung để tạo mô hình tư duy (mental model / 사고 모델) mới.

> **Bàn giao:** Sau **Quy tắc mở rộng**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 debugging across abstraction layers](./00_debugging_across_abstraction_layers.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
