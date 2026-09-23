# 08 — Orchestration và backfill correctness

Orchestration là quản lý dependency, schedule, retry, state và ownership của workflow. Nó không thay thế processing engine và cũng không chứng minh business data đúng.

## 1. DAG là dependency graph

Một task chỉ nên chạy khi upstream data và contract đã đạt điều kiện cần. Dependency không chỉ là “job A chạy trước job B”; có thể là partition D đã complete, schema version tương thích, quality gate pass hoặc external snapshot đã immutable.

## 2. Task semantics

Mỗi task cần định nghĩa:

- input version/partition;
- output path/table và atomic publish rule;
- retryable vs permanent error;
- idempotency key;
- side effect ngoài data write;
- reconciliation và completion evidence.

Retry an toàn chỉ có thể xảy ra khi chạy lại không phá invariant. Nếu task gửi email, gọi API hoặc cập nhật ticket, side effect phải tách ra hoặc có idempotency key.

## 3. Backfill là một loại deployment

Backfill thay đổi dữ liệu lịch sử bằng code/logic mới, nên phải được review như deployment. Trước khi chạy cần chốt:

```text
input range + source snapshot
→ code/schema version
→ target partitions/version
→ write mode
→ expected counts/reconciliation
→ publish/rollback plan
```

Không chạy backfill trực tiếp lên “latest” nếu chưa tách output namespace hoặc snapshot. Một job thành công có thể overwrite dữ liệu mới bằng kết quả cũ.

## 4. Partition completeness

Partition chỉ nên được đánh dấu complete khi có evidence: source watermark, expected file set, row count/tolerance, checksum hoặc reconciliation với source. “Task không lỗi” không đủ để publish partition.

Manifest/commit marker giúp downstream đọc tập file nhất quán thay vì nhìn thấy output đang ghi dở. Khi partition bị retry, marker cũ phải được thay thế có version hoặc transaction semantics rõ.

## 5. Catchup và schedule drift

Schedule interval không đồng nghĩa data interval. Job chạy lúc 01:00 có thể xử lý ngày D-1, hoặc xử lý source watermark tới 00:45. Nếu scheduler chậm, catchup có thể tạo hàng trăm run cạnh tranh tài nguyên.

Cần giới hạn concurrency, ưu tiên backfill so với freshness, và xác định run nào được phép ghi cùng partition. Một partition có nhiều writer mà không có commit protocol là race condition.

## 6. Recovery

Khi workflow thất bại, phân biệt task chưa bắt đầu, đang chạy, đã ghi output nhưng chưa publish, và đã publish nhưng downstream chưa acknowledge. Resume từ checkpoint khác với rerun toàn DAG.

Run metadata nên lưu input partitions, code commit, schema version, row counts, quality results và output commit. Đó là bằng chứng để quyết định retry hay rollback.

## 7. Tool-independent checklist

1. Dependency có phản ánh data readiness hay chỉ phản ánh process order?
2. Retry/backfill có idempotent không?
3. Output publish có atomic không?
4. Có thể chạy song song hai run trên cùng partition không?
5. Reconciliation nào ngăn job xanh nhưng data sai?
6. External side effect được deduplicate thế nào?

Đọc tiếp: [04 — Reliability](../04_reliability_and_production.md), [07 — Streaming](../07_streaming_systems/README.md), [90 — Case studies](../90_case_studies/README.md).
