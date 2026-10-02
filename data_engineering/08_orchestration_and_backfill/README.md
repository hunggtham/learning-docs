# 08 — Orchestration và backfill tính đúng đắn (correctness / 정확성)

> **Mạch đọc:** README này là owner của **08 — Orchestration và backfill tính đúng đắn (correctness / 정확성)**. Route đi từ DAG/dependency graph → task semantics → schedule, retry, state và ownership → backfill, idempotency và data correctness → observability/recovery, để orchestration không bị nhầm với processing engine.

Orchestration là quản lý phụ thuộc (dependency / 의존성), schedule, thử lại (retry / 재시도), trạng thái (state / 상태) và quyền sở hữu (ownership / 소유권) của workflow. Nó không thay thế processing engine và cũng không chứng minh nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터) đúng.

## 1. DAG là phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)

Một tác vụ (task / 작업) chỉ nên chạy khi upstream dữ liệu (data / 데이터) và đặc tả hợp đồng (contract / 계약) đã đạt điều kiện cần. phụ thuộc (dependency / 의존성) không chỉ là “job A chạy trước job B”; có thể là partition D đã complete, lược đồ (schema / 스키마) phiên bản (version / 버전) tương thích, cổng chất lượng (quality gate / 품질 게이트) pass hoặc bên ngoài (external / 외부) snapshot đã immutable.

> **Chuyển mạch:** Trong **08 — Orchestration và backfill tính đúng đắn (correctness / 정확성)**, **2. tác vụ (task / 작업) ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **1. DAG là phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Backfill là một loại triển khai (deployment / 배포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. tác vụ (task / 작업) ngữ nghĩa (semantics / 의미론)

Mỗi tác vụ (task / 작업) cần định nghĩa:

- đầu vào (input / 입력) phiên bản (version / 버전)/partition;
- đầu ra (output / 출력) đường dẫn (path / 경로)/bảng (table / 테이블) và atomic publish quy tắc (rule / 규칙);
- retryable vs permanent lỗi (error / 오류);
- idempotency key;
- side tác động (effect / 효과) ngoài dữ liệu (data / 데이터) ghi (write / 쓰기);
- reconciliation và completion bằng chứng (evidence / 증거).

Thử lại (retry / 재시도) an toàn chỉ có thể xảy ra khi chạy lại không phá bất biến (invariant / 불변식). Nếu tác vụ (task / 작업) gửi email, gọi API hoặc cập nhật ticket, side tác động (effect / 효과) phải tách ra hoặc có idempotency key.

> **Chuyển mạch:** Ở chặng này của **08 — Orchestration và backfill tính đúng đắn (correctness / 정확성)**, **3. Backfill là một loại triển khai (deployment / 배포)** tiếp nhận điểm tựa từ **2. tác vụ (task / 작업) ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Partition completeness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Backfill là một loại triển khai (deployment / 배포)

Backfill thay đổi dữ liệu lịch sử bằng mã (code / 코드)/lô-gic (logic / 논리) mới, nên phải được rà soát (review / 검토) như triển khai (deployment / 배포). Trước khi chạy cần chốt:

```text
input range + source snapshot
→ code/schema version
→ target partitions/version
→ write mode
→ expected counts/reconciliation
→ publish/rollback plan
```

Không chạy backfill trực tiếp lên “latest” nếu chưa tách đầu ra (output / 출력) không gian tên (namespace / 네임스페이스) hoặc snapshot. Một job thành công có thể overwrite dữ liệu mới bằng kết quả cũ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Orchestration và backfill tính đúng đắn (correctness / 정확성)**, **4. Partition completeness** tiếp nhận điểm tựa từ **3. Backfill là một loại triển khai (deployment / 배포)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Catchup và schedule drift** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Partition completeness

Partition chỉ nên được đánh dấu complete khi có bằng chứng (evidence / 증거): nguồn (source / 소스) watermark, expected tệp (file / 파일) set, row count/tolerance, checksum hoặc reconciliation với nguồn (source / 소스). “tác vụ (task / 작업) không lỗi” không đủ để publish partition.

Manifest/lần ghi nhận (commit / 커밋) marker giúp downstream đọc tập tệp (file / 파일) nhất quán thay vì nhìn thấy đầu ra (output / 출력) đang ghi dở. Khi partition bị thử lại (retry / 재시도), marker cũ phải được thay thế có phiên bản (version / 버전) hoặc giao dịch (transaction / 트랜잭션) ngữ nghĩa (semantics / 의미론) rõ.

> **Chuyển mạch:** Trong **08 — Orchestration và backfill tính đúng đắn (correctness / 정확성)**, **5. Catchup và schedule drift** tiếp nhận điểm tựa từ **4. Partition completeness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. khôi phục (recovery / 복구)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Catchup và schedule drift

Schedule interval không đồng nghĩa dữ liệu (data / 데이터) interval. Job chạy lúc 01:00 có thể xử lý ngày D-1, hoặc xử lý nguồn (source / 소스) watermark tới 00:45. Nếu scheduler chậm, catchup có thể tạo hàng trăm run cạnh tranh tài nguyên.

Cần giới hạn tính đồng thời (concurrency / 동시성), ưu tiên backfill so với freshness, và xác định run nào được phép ghi cùng partition. Một partition có nhiều writer mà không có lần ghi nhận (commit / 커밋) giao thức (protocol / 프로토콜) là race điều kiện (condition / 조건).

> **Chuyển mạch:** Ở chặng này của **08 — Orchestration và backfill tính đúng đắn (correctness / 정확성)**, **6. khôi phục (recovery / 복구)** tiếp nhận điểm tựa từ **5. Catchup và schedule drift** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Tool-independent checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. khôi phục (recovery / 복구)

Khi workflow thất bại, phân biệt tác vụ (task / 작업) chưa bắt đầu, đang chạy, đã ghi đầu ra (output / 출력) nhưng chưa publish, và đã publish nhưng downstream chưa acknowledge. Resume từ checkpoint khác với rerun toàn DAG.

Run siêu dữ liệu (metadata / 메타데이터) nên lưu đầu vào (input / 입력) partitions, mã (code / 코드) lần ghi nhận (commit / 커밋), lược đồ (schema / 스키마) phiên bản (version / 버전), row counts, chất lượng (quality / 품질) results và đầu ra (output / 출력) lần ghi nhận (commit / 커밋). Đó là bằng chứng để quyết định thử lại (retry / 재시도) hay quay lui (rollback / 롤백).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Orchestration và backfill tính đúng đắn (correctness / 정확성)**, **7. Tool-independent checklist** tiếp nhận điểm tựa từ **6. khôi phục (recovery / 복구)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Backfill planner** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Tool-independent checklist

1. phụ thuộc (dependency / 의존성) có phản ánh dữ liệu (data / 데이터) readiness hay chỉ phản ánh tiến trình (process / 프로세스) thứ tự (order / 순서)?
2. thử lại (retry / 재시도)/backfill có idempotent không?
3. đầu ra (output / 출력) publish có atomic không?
4. Có thể chạy song song hai run trên cùng partition không?
5. Reconciliation nào ngăn job xanh nhưng dữ liệu (data / 데이터) sai?
6. bên ngoài (external / 외부) side tác động (effect / 효과) được deduplicate thế nào?

Đọc tiếp: [04 — Reliability](../04_reliability_and_production.md), [07 — Streaming](../07_streaming_systems/README.md), [90 — Case studies](../90_case_studies/README.md).

> **Chuyển mạch:** Trong **08 — Orchestration và backfill tính đúng đắn (correctness / 정확성)**, **8. Backfill planner** tiếp nhận điểm tựa từ **7. Tool-independent checklist** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. tính đồng thời (concurrency / 동시성) trên cùng partition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Backfill planner

Một backfill lớn nên có planner tách khỏi executor. Planner tạo manifest các đầu vào (input / 입력) partition, đầu ra (output / 출력) partition, mã (code / 코드)/lược đồ (schema / 스키마) phiên bản (version / 버전), expected row count và phụ thuộc (dependency / 의존성). Executor chỉ chạy manifest immutable; không tự suy luận mục tiêu (target / 대상) phạm vi (range / 범위) từ “now”.

```text
plan → validate conflicts → execute isolated output → reconcile → publish
```

Nếu plan thay đổi giữa chừng, tạo plan phiên bản (version / 버전) mới thay vì sửa tệp (file / 파일) đang chạy. Điều này giúp quay lui (rollback / 롤백) và forensic phân tích (analysis / 분석) biết run đã dựa trên giả định (assumption / 가정) nào.

> **Chuyển mạch:** Ở chặng này của **08 — Orchestration và backfill tính đúng đắn (correctness / 정확성)**, **9. tính đồng thời (concurrency / 동시성) trên cùng partition** tiếp nhận điểm tựa từ **8. Backfill planner** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. thử lại (retry / 재시도) taxonomy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. tính đồng thời (concurrency / 동시성) trên cùng partition

Cho phép hai run cùng ghi partition là race điều kiện (condition / 조건) nếu không có fencing/lease/lần ghi nhận (commit / 커밋) giao thức (protocol / 프로토콜). Scheduler cần một trong các bất biến (invariant / 불변식):

- một partition chỉ có một writer active;
- writer có epoch/fencing đơn vị từ (token / 토큰), writer cũ bị từ chối;
- đầu ra (output / 출력) phiên bản (version / 버전) riêng, publish pointer tuần tự;
- merge ngữ nghĩa (semantics / 의미론) chứng minh hai ghi (write / 쓰기) giao nhau là an toàn.

Phân tán (distributed / 분산) khóa (lock / 잠금) chỉ giải quyết mutual exclusion trong thời gian khóa (lock / 잠금) còn hiệu lực; nó không thay thế đầu ra (output / 출력) reconciliation và stale-writer fencing.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Orchestration và backfill tính đúng đắn (correctness / 정확성)**, **10. thử lại (retry / 재시도) taxonomy** tiếp nhận điểm tựa từ **9. tính đồng thời (concurrency / 동시성) trên cùng partition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 10. thử lại (retry / 재시도) taxonomy

Thử lại (retry / 재시도) theo lỗi, không theo cảm xúc:

| Lỗi | Hành động |
|---|---|
| hết thời gian chờ (timeout / 타임아웃)/mạng (network / 네트워크) transient | exponential backoff + jitter |
| quota/sức chứa (capacity / 용량) | thử lại (retry / 재시도) có giới hạn hoặc reschedule |
| lược đồ (schema / 스키마)/đặc tả hợp đồng (contract / 계약) breaking | stop, alert đơn vị sở hữu (owner / 오너) |
| malformed bản ghi (record / 레코드) | quarantine + chỉ số (metric / 지표) |
| mã (code / 코드) bug | quay lui (rollback / 롤백)/phiên bản (version / 버전) fix rồi rerun |
| sink partial lần ghi nhận (commit / 커밋) | inspect marker trước khi thử lại (retry / 재시도) |

Thử lại (retry / 재시도) vô hạn biến lỗi deterministic thành sự cố (incident / 인시던트) lớn hơn và che khuất dữ liệu (data / 데이터) mất mát (loss / 손실).

> **Bàn giao:** Sau **10. thử lại (retry / 재시도) taxonomy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
