# 12 — chi phí (cost / 비용), hiệu năng (performance / 성능) và sức chứa (capacity / 용량)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **12 — chi phí (cost / 비용), hiệu năng (performance / 성능) và sức chứa (capacity / 용량)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. sức chứa (capacity / 용량) mô hình (model / 모델)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Scan và bố cục (layout / 레이아웃)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối cost, performance và capacity với workload, bottleneck và SLO, để tối ưu dựa trên giới hạn đo được.

Dữ liệu (data / 데이터) nền tảng (platform / 플랫폼) phải tối ưu total chi phí (cost / 비용) of quyền sở hữu (ownership / 소유권) và data-product SLO, không chỉ một truy vấn (query / 쿼리) benchmark. chi phí (cost / 비용) đến từ bytes scanned, shuffle, lưu trữ (storage / 저장소), mạng (network / 네트워크), tệp (file / 파일) operations, idle sức chứa (capacity / 용량), retries, compaction và thời gian kỹ sư.

## 1. sức chứa (capacity / 용량) mô hình (model / 모델)

Bắt đầu từ volume và tính đồng thời (concurrency / 동시성):

```text
daily input × retention × replication
daily compute × peak concurrency × SLA window
shuffle bytes + spill bytes + network egress
```

Peak thường quan trọng hơn average: backfill, month-end close hoặc sự cố (incident / 인시던트) replay có thể cạnh tranh với freshness tải công việc (workload / 워크로드).

> **Chuyển mạch:** **Capacity model** xác định workload và headroom; **Scan và layout** biến mô hình đó thành I/O cost, rồi **Shuffle/skew/spill** giải thích amplification.

## 2. Scan và bố cục (layout / 레이아웃)

Partition pruning, column pruning, predicate pushdown, clustering và tệp (file / 파일) kích thước (size / 크기) giảm bytes đọc. Nhưng partition quá mịn, compaction quá thường xuyên hoặc sort thứ tự (order / 순서) đắt có thể chuyển chi phí (cost / 비용) sang ingestion/maintenance.

Đo end-to-end: files opened, bytes scanned, CPU decode, mạng (network / 네트워크), hàng đợi (queue / 큐) wait, tác vụ (task / 작업) count và đầu ra (output / 출력) freshness.

> **Chuyển mạch:** **Shuffle, skew và spill** cho thấy cost bị nhân lên ở execution; **Small files và compaction budget** đưa cùng vấn đề vào storage maintenance.

## 3. Shuffle, skew và spill

Shuffle bytes thường là predictor tốt hơn row count. Skew tạo long-tail tác vụ (task / 작업); spill tăng disk I/O và merge. Tối ưu có thể là pre-aggregation, salting, broadcast nhỏ, projection sớm hoặc tách heavy hitter—không mặc định là thêm worker.

> **Chuyển mạch:** **Small files và compaction budget** cân write amplification với read efficiency; **Concurrency và isolation** kiểm tra cost khi nhiều job cùng chạm storage.

## 4. Small files và compaction ngân sách (budget / 예산)

Small-file bài toán (problem / 문제) tăng siêu dữ liệu (metadata / 메타데이터)/listing/tác vụ (task / 작업) overhead. Compaction tạo ghi (write / 쓰기) amplification và có thể tranh tài nguyên (resource / 자원) với truy vấn (query / 쿼리). Cần ngân sách (budget / 예산) compaction theo tệp (file / 파일) count, truy vấn (query / 쿼리) độ trễ (latency / 지연 시간) và khôi phục (recovery / 복구) chính sách (policy / 정책), không chạy cron mù quáng.

> **Chuyển mạch:** **Concurrency và isolation** đặt giới hạn lên throughput và contention; **Unit economics** quy đổi giới hạn đó thành cost mỗi query, row hoặc workload.

## 5. tính đồng thời (concurrency / 동시성) và isolation

Một truy vấn (query / 쿼리) nhanh khi chạy một mình có thể làm freshness job trễ khi chạy cùng nhiều dashboard. sức chứa (capacity / 용량) plan cần tải công việc (workload / 워크로드) lớp (class / 클래스), hàng đợi (queue / 큐), priority, admission điều khiển (control / 제어) và isolation. SLO nên nêu cả độ trễ (latency / 지연 시간) và freshness impact.

> **Chuyển mạch:** **Unit economics** làm rõ baseline và denominator; **Experiment loop** kiểm tra tối ưu có cải thiện cost/performance thật hay chỉ chuyển chi phí sang lớp khác.

## 6. đơn vị (unit / 단위) economics

Theo dõi chi phí (cost / 비용) per TB processed, chi phí (cost / 비용) per successful chuỗi xử lý (pipeline / 파이프라인) run, chi phí (cost / 비용) per published dataset hoặc chi phí (cost / 비용) per active bên tiêu thụ (consumer / 소비자). đơn vị (unit / 단위) economics bắt regression sớm hơn tổng invoice, vì tổng invoice có thể tăng đơn giản do volume tăng.

> **Chuyển mạch:** **Experiment loop** tạo evidence trước/sau; **Queueing và saturation** giải thích khi thay đổi đó chạm giới hạn capacity.

## 7. Experiment vòng lặp (loop / 루프)

1. Chọn tải công việc (workload / 워크로드) và tính đúng đắn (correctness / 정확성) baseline.
2. Đo bytes/CPU/mạng (network / 네트워크)/hàng đợi (queue / 큐)/spill trước thay đổi.
3. Thay một bố cục (layout / 레이아웃)/partition/phép nối (join / 조인) chiến lược (strategy / 전략).
4. Chạy cùng đầu vào (input / 입력) và mã (code / 코드) phiên bản (version / 버전).
5. So sánh chi phí (cost / 비용), độ trễ (latency / 지연 시간), freshness và dữ liệu (data / 데이터) reconciliation.

Không chấp nhận hiệu năng (performance / 성능) gain nếu làm mất late sự kiện (event / 이벤트), duplicate, lịch sử (history / 이력) hoặc kiểm tra (audit / 감사) bằng chứng (evidence / 증거).

Đọc tiếp: [06 — Distributed processing](../06_distributed_processing/README.md), [09 — Warehouse/lakehouse](../09_warehouse_lake_lakehouse/README.md), [04 — Reliability](../04_reliability_and_production.md).

> **Chuyển mạch:** **Queueing và saturation** nối latency với resource headroom; **Cost attribution** phân bổ tác động đó về team, query hoặc product owner.

## 8. Queueing và saturation

Sức chứa (capacity / 용량) không chỉ là tổng CPU. Khi arrival tỷ lệ (rate / 비율) tiến gần dịch vụ (service / 서비스) tỷ lệ (rate / 비율), queueing delay tăng phi tuyến. Một mô hình (model / 모델) đơn giản:

```text
utilization ρ = arrival rate / service rate
```

Khi `ρ` gần 1, một burst nhỏ có thể làm freshness trễ hàng giờ. Cần reserve headroom cho thử lại (retry / 재시도), compaction, backfill và sự cố (incident / 인시던트) replay; chạy môi trường vận hành (production / 운영 환경) ở 100% average utilization là thiết kế không có khôi phục (recovery / 복구) sức chứa (capacity / 용량).

> **Chuyển mạch:** **Cost attribution** cho biết ai chịu tác động của saturation; **Optimization không phá semantics** chỉ chấp nhận thay đổi khi correctness và owner vẫn giữ nguyên.

## 9. chi phí (cost / 비용) attribution

Chi phí (cost / 비용) cần gắn với lĩnh vực (domain / 도메인)/dataset/bên tiêu thụ (consumer / 소비자) bằng tags, truy vấn (query / 쿼리) labels, run siêu dữ liệu (metadata / 메타데이터) hoặc allocation quy tắc (rule / 규칙). dùng chung (shared / 공유) cluster không có attribution làm đơn vị sở hữu (owner / 오너) không thấy regression và nền tảng (platform / 플랫폼) nhóm (team / 팀) phải gánh “mystery chi phí (cost / 비용)”.

Một đơn vị (unit / 단위) economics tốt ghi rõ denominator: chi phí (cost / 비용) per TB đầu vào (input / 입력), per published partition, per successful run, per dashboard refresh hoặc per tính năng (feature / 기능) computation. Denominator thay đổi phải được phiên bản (version / 버전) trong report.

> **Chuyển mạch:** **Optimization không phá semantics** khép README bằng evidence, capacity guardrail và cost owner; chi tiết engine quay về canonical performance chapter.

## 10. tối ưu hóa (optimization / 최적화) không phá ngữ nghĩa (semantics / 의미론)

Mỗi tối ưu hóa (optimization / 최적화) cần tính đúng đắn (correctness / 정확성) guardrail: golden chỉ số (metric / 지표), row/key reconciliation, late-event mẫu (sample / 표본), lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) và quay lui (rollback / 롤백). Broadcast phép nối (join / 조인) có thể giảm shuffle nhưng thất bại (fail / 실패) khi dimension phình; approximate distinct giảm chi phí (cost / 비용) nhưng thay guarantee; caching giảm độ trễ (latency / 지연 시간) nhưng tăng staleness.

Hiệu năng (performance / 성능) rà soát (review / 검토) nên ghi rõ ngữ nghĩa (semantic / 의미적) sự đánh đổi (trade-off / 트레이드오프), không chỉ benchmark trước/sau.

> **Bàn giao:** Sau **10. tối ưu hóa (optimization / 최적화) không phá ngữ nghĩa (semantics / 의미론)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
