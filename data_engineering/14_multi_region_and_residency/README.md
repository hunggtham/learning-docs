# 14 — Multi-region, replication và dữ liệu (data / 데이터) residency

> **Mạch đọc:** Đọc **14 — Multi-region, replication và dữ liệu (data / 데이터) residency** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Topology và authority** sang **2. Replication lag**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Multi-region không chỉ là bản sao (copy / 복사) bảng (table / 테이블) sang hai nơi. Nó là bài toán về độ trễ (latency / 지연 시간), authority, replication lag, xung đột (conflict / 충돌), failover, khôi phục (recovery / 복구) điểm (point / 지점) và nơi dữ liệu được phép tồn tại.

## 1. Topology và authority

Chọn primary/replica, active-passive hay multi-writer phải bắt đầu từ ghi (write / 쓰기) authority. Nếu hai region cùng sửa một customer, cần xung đột (conflict / 충돌) quy tắc (rule / 규칙); eventual convergence không tự bảo toàn nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식).

```text
single writer → replicate → read-local
multi writer  → conflict resolution → converge/compensate
```

Giải quyết xung đột (conflict resolution / 충돌 해결) có thể là last-write-wins, phiên bản (version / 버전) véc-tơ (vector / 벡터), field-level merge hoặc lĩnh vực (domain / 도메인) command. Clock wall-time không đủ đáng tin nếu clock skew có thể đảo thứ tự sự kiện (event / 이벤트).


> **Chuyển mạch:** Từ **1. Topology và authority**, ta sang **2. Replication lag** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. Replication lag

Lag có thể đo theo nguồn (source / 소스) position, sự kiện (event / 이벤트) thời gian (time / 시간) hoặc lần ghi nhận (commit / 커밋) timestamp. Read-after-write guarantee cần biết yêu cầu (request / 요청) đọc ở region nào và replica đã bắt kịp position nào. Dashboard đọc cục bộ (local / 로컬) replica có thể stale dù replication job không báo lỗi.

SLO nên tách p50/p99 lag, maximum staleness và khôi phục (recovery / 복구) catch-up thời gian (time / 시간). Average lag che giấu một partition/tenant bị kẹt.


> **Chuyển mạch:** Từ **2. Replication lag**, ta sang **3. RPO/RTO và failover** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. RPO/RTO và failover

RPO trả lời mất tối đa bao nhiêu dữ liệu; RTO trả lời phục hồi trong bao lâu. Failover chỉ đúng nếu mục tiêu (target / 대상) region có lược đồ (schema / 스키마), secrets, danh mục (catalog / 카탈로그), checkpoints, routing và truy cập (access / 접근) chính sách (policy / 정책) tương ứng—không chỉ có dữ liệu (data / 데이터) files.

Runbook cần fencing primary cũ để tránh split-brain. Sau failover, ghi tiếp vào đâu, replay khoảng nào, và merge/correction đầu ra (output / 출력) thế nào phải được định nghĩa trước.


> **Chuyển mạch:** Từ **3. RPO/RTO và failover**, ta sang **4. Residency và purpose limitation** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. Residency và purpose limitation

Dữ liệu (data / 데이터) residency có thể yêu cầu raw PII ở một quốc gia nhưng aggregate đã anonymize được phục vụ toàn cầu. Replication chính sách (policy / 정책) phải gắn với trường dữ liệu (field / 필드) classification và purpose, không chỉ cơ sở dữ liệu (database / 데이터베이스) name.

Siêu dữ liệu (metadata / 메타데이터), logs, backups, caches và hỗ trợ (support / 지원) exports cũng có thể chứa dữ liệu nhạy cảm. “Không replicate bảng (table / 테이블)” chưa đủ nếu CDC log hoặc khả năng quan sát (observability / 관측 가능성) payload vẫn vượt region ranh giới (boundary / 경계).


> **Chuyển mạch:** Từ **4. Residency và purpose limitation**, ta sang **5. bằng chứng (evidence / 증거) và kiểm thử (test / 테스트)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. bằng chứng (evidence / 증거) và kiểm thử (test / 테스트)

Bằng chứng (evidence / 증거) gồm replication position, lag histogram, failover timestamp, fenced writer, đầu ra (output / 출력) reconciliation và residency kiểm tra (audit / 감사). kiểm thử (test / 테스트) định kỳ phải mô phỏng region mất mạng, stale replica, duplicate replay và clock skew.


> **Chuyển mạch:** Từ **5. bằng chứng (evidence / 증거) và kiểm thử (test / 테스트)**, ta sang **6. sự đánh đổi (trade-off / 트레이드오프)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 6. sự đánh đổi (trade-off / 트레이드오프)

Strong consistency across regions tăng độ trễ (latency / 지연 시간) và coordination chi phí (cost / 비용); eventual consistency giảm độ trễ (latency / 지연 시간) nhưng cần correction/read-your-writes chiến lược (strategy / 전략). Chọn guarantee theo lĩnh vực (domain / 도메인), không theo default của cơ sở dữ liệu (database / 데이터베이스) hoặc cloud dịch vụ (service / 서비스).

Đọc tiếp: [07 — Streaming](../07_streaming_systems/README.md), [09 — Lakehouse](../09_warehouse_lake_lakehouse/README.md), [11 — Governance](../11_governance_lineage_security/README.md).

> **Bàn giao:** Sau **6. sự đánh đổi (trade-off / 트레이드오프)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp.
