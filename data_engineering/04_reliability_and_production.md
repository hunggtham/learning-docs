# 04 — độ tin cậy (reliability / 신뢰성), dữ liệu (data / 데이터) chất lượng (quality / 품질) và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **04 — độ tin cậy (reliability / 신뢰성), dữ liệu (data / 데이터) chất lượng (quality / 품질) và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론)**. Route đi từ pipeline success và data success → quality invariants → freshness/completeness/correctness → retries, backfills, incidents và observability → production ownership, để đầu ra đúng nghiệp vụ chứ không chỉ exit code 0.

## 1. chuỗi xử lý (pipeline / 파이프라인) success khác dữ liệu (data / 데이터) success

Một tiến trình (process / 프로세스) exit mã (code / 코드) `0` chỉ chứng minh mã (code / 코드) không báo lỗi theo đặc tả hợp đồng (contract / 계약) của tiến trình (process / 프로세스). Nó không chứng minh đầu ra (output / 출력) đầy đủ, đúng nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) hoặc fresh.

Ví dụ nguồn (source / 소스) trả về HTTP 200 nhưng chỉ có 20% records vì pagination bug. chuỗi xử lý (pipeline / 파이프라인) có thể xanh từ đầu đến cuối. Vì vậy môi trường vận hành (production / 운영 환경) kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) cần quan sát cả hệ thống (system / 시스템) metrics lẫn dữ liệu (data / 데이터) metrics.

> **Chuyển mạch:** Trong **04 — độ tin cậy (reliability / 신뢰성), dữ liệu (data / 데이터) chất lượng (quality / 품질) và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론)**, **1. chuỗi xử lý (pipeline / 파이프라인) success khác dữ liệu (data / 데이터) success** nêu điều cần giải thích; **2. dữ liệu (data / 데이터) chất lượng (quality / 품질) theo bất biến (invariant / 불변식)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. Freshness, completeness và tính đúng đắn (correctness / 정확성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. dữ liệu (data / 데이터) chất lượng (quality / 품질) theo bất biến (invariant / 불변식)

Quy tắc (rule / 규칙) chất lượng (quality / 품질) tốt xuất phát từ bất biến (invariant / 불변식) thay vì danh sách check chung chung. `NOT NULL` hữu ích nếu null thực sự bất hợp lệ. `row_count > 0` không đủ nếu bình thường dataset có mười triệu row nhưng hôm nay chỉ còn một nghìn.

Các bất biến (invariant / 불변식) có thể nằm ở nhiều tầng: lược đồ (schema / 스키마) bất biến (invariant / 불변식), uniqueness, referential integrity, accepted lĩnh vực (domain / 도메인), volume phân phối (distribution / 분포), reconciliation với nguồn (source / 소스) và nghiệp vụ (business / 비즈니스) equation.

Ví dụ payment hệ thống (system / 시스템) có thể kiểm tra tổng captured amount theo nguồn (source / 소스) ledger và warehouse trong tolerance xác định. Reconciliation như vậy mạnh hơn chỉ kiểm tra column kiểu (type / 타입).

> **Chuyển mạch:** Ở chặng này của **04 — độ tin cậy (reliability / 신뢰성), dữ liệu (data / 데이터) chất lượng (quality / 품질) và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론)**, **2. dữ liệu (data / 데이터) chất lượng (quality / 품질) theo bất biến (invariant / 불변식)** nêu điều cần giải thích; **3. Freshness, completeness và tính đúng đắn (correctness / 정확성)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Freshness, completeness và tính đúng đắn (correctness / 정확성)

Freshness hỏi dữ liệu mới đến mức nào. Completeness hỏi dữ liệu cần có đã đến đủ chưa. tính đúng đắn (correctness / 정확성) hỏi giá trị có đúng theo ngữ nghĩa (semantics / 의미론) không.

Ba khái niệm không thay thế nhau. Dataset có thể fresh vì vừa cập nhật (update / 업데이트) nhưng thiếu 30% partition. Nó có thể complete nhưng dùng sai exchange tỷ lệ (rate / 비율). Dashboard có timestamp mới không chứng minh nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터) đáng tin.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — độ tin cậy (reliability / 신뢰성), dữ liệu (data / 데이터) chất lượng (quality / 품질) và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론)**, **3. Freshness, completeness và tính đúng đắn (correctness / 정확성)** nêu điều cần giải thích; **4. dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **5. Lineage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약)

Dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약) làm expectation giữa producer và bên tiêu thụ (consumer / 소비자) trở nên tường minh (explicit / 명시적): lược đồ (schema / 스키마), ngữ nghĩa (semantics / 의미론), quyền sở hữu (ownership / 소유권), tính tương thích (compatibility / 호환성), chất lượng (quality / 품질) và đôi khi SLO.

Đặc tả hợp đồng (contract / 계약) không nhất thiết là một khung phần mềm (framework / 프레임워크). Giá trị của nó nằm ở việc breaking thay đổi (change / 변경) không còn là surprise. Producer biết bên tiêu thụ (consumer / 소비자) phụ thuộc vào điều gì; bên tiêu thụ (consumer / 소비자) biết dataset được hứa những guarantee nào.

Đặc tả hợp đồng (contract / 계약) quá cứng cũng có sự đánh đổi (trade-off / 트레이드오프): nó có thể làm evolution chậm. Vì vậy cần phân biệt trường dữ liệu (field / 필드) công khai (public / 공개)/stable với hiện thực (implementation / 구현) detail và có versioning/deprecation tiến trình (process / 프로세스).

> **Chuyển mạch:** Trong **04 — độ tin cậy (reliability / 신뢰성), dữ liệu (data / 데이터) chất lượng (quality / 품질) và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론)**, **4. dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약)** nêu điều cần giải thích; **5. Lineage** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6. khả năng quan sát (observability / 관측 가능성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Lineage

Lineage trả lời dataset này đến từ đâu và downstream nào phụ thuộc vào nó. Khi nguồn (source / 소스) column thay đổi, lineage giúp xác định blast radius.

Lineage chỉ từ static SQL parsing có thể thiếu động (dynamic / 동적) job, UDF hoặc bên ngoài (external / 외부) tiến trình (process / 프로세스). thời gian chạy (runtime / 런타임) lineage chính xác hơn ở một số trường hợp nhưng tốn instrumentation. môi trường vận hành (production / 운영 환경) nền tảng (platform / 플랫폼) thường cần kết hợp siêu dữ liệu (metadata / 메타데이터) từ orchestration, danh mục (catalog / 카탈로그), truy vấn (query / 쿼리) engine và triển khai (deployment / 배포) hệ thống (system / 시스템).

Lineage không tự tạo trust. Nó là bằng chứng (evidence / 증거) đồ thị (graph / 그래프); chất lượng (quality / 품질) và quyền sở hữu (ownership / 소유권) vẫn phải được duy trì.

> **Chuyển mạch:** Ở chặng này của **04 — độ tin cậy (reliability / 신뢰성), dữ liệu (data / 데이터) chất lượng (quality / 품질) và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론)**, **6. khả năng quan sát (observability / 관측 가능성)** tiếp nhận điểm tựa từ **5. Lineage** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. thử lại (retry / 재시도) và poison dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. khả năng quan sát (observability / 관측 가능성)

Hệ thống (system / 시스템) khả năng quan sát (observability / 관측 가능성) theo dõi CPU, bộ nhớ (memory / 메모리), độ trễ (latency / 지연 시간), lỗi (error / 오류) tỷ lệ (rate / 비율), hàng đợi (queue / 큐) lag và tài nguyên (resource / 자원) saturation. dữ liệu (data / 데이터) khả năng quan sát (observability / 관측 가능성) bổ sung freshness, volume, lược đồ (schema / 스키마) drift, phân phối (distribution / 분포) và lineage-aware impact.

Một alert tốt phải actionable. "row count changed" không đủ nếu không có baseline, severity, dataset đơn vị sở hữu (owner / 오너) và runbook. Alert quá nhạy gây fatigue; alert quá lỏng phát hiện sự cố (incident / 인시던트) sau bên tiêu thụ (consumer / 소비자).

Cấp cao (senior / 시니어) ghi chú (note / 노트): monitoring nên bám vào user-visible/data-product SLO trước rồi drill down tới thành phần (component / 컴포넌트) metrics. Nếu chỉ monitor từng tác vụ (task / 작업), có thể tất cả tác vụ (task / 작업) đều xanh trong khi dữ liệu (data / 데이터) sản phẩm (product / 제품) đã vi phạm freshness SLO.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — độ tin cậy (reliability / 신뢰성), dữ liệu (data / 데이터) chất lượng (quality / 품질) và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론)**, **6. khả năng quan sát (observability / 관측 가능성)** nêu điều cần giải thích; **7. thử lại (retry / 재시도) và poison dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. khôi phục (recovery / 복구) và disaster thinking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. thử lại (retry / 재시도) và poison dữ liệu (data / 데이터)

Thử lại (retry / 재시도) hữu ích cho transient thất bại (failure / 실패) như mạng (network / 네트워크) hết thời gian chờ (timeout / 타임아웃) nhưng có thể làm tình hình tệ hơn với deterministic thất bại (failure / 실패). Một malformed bản ghi (record / 레코드) thử lại (retry / 재시도) 100 lần vẫn malformed và có thể khối (block / 블록) partition.

Cần phân biệt transient, permanent và unknown thất bại (failure / 실패). Dead-letter/quarantine đường dẫn (path / 경로) cho phép tách poison dữ liệu (data / 데이터) khỏi main luồng (flow / 흐름), nhưng không được biến thành nơi âm thầm bỏ dữ liệu. Quarantine phải có đơn vị sở hữu (owner / 오너), chỉ số (metric / 지표), retention và replay procedure.

Exponential backoff và jitter giúp tránh hàng nghìn worker thử lại (retry / 재시도) đồng thời sau outage, gây thundering herd lên phụ thuộc (dependency / 의존성) vừa phục hồi.

> **Chuyển mạch:** Trong **04 — độ tin cậy (reliability / 신뢰성), dữ liệu (data / 데이터) chất lượng (quality / 품질) và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론)**, **7. thử lại (retry / 재시도) và poison dữ liệu (data / 데이터)** nêu điều cần giải thích; **8. khôi phục (recovery / 복구) và disaster thinking** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. bảo mật (security / 보안) và quản trị (governance / 거버넌스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. khôi phục (recovery / 복구) và disaster thinking

Backup chỉ có giá trị nếu restore được. Tương tự, sự kiện (event / 이벤트) retention chỉ có giá trị nếu đủ để replay trong khôi phục (recovery / 복구) cửa sổ (window / 윈도우).

Khôi phục (recovery / 복구) thiết kế (design / 설계) cần biết khôi phục (recovery / 복구) điểm (point / 지점) mục tiêu (objective / 목표) (RPO) — chấp nhận mất tối đa bao nhiêu dữ liệu — và khôi phục (recovery / 복구) thời gian (time / 시간) mục tiêu (objective / 목표) (RTO) — chấp nhận mất bao lâu để phục hồi dịch vụ (service / 서비스)/dữ liệu (data / 데이터) sản phẩm (product / 제품).

Một chuỗi xử lý (pipeline / 파이프라인) có thể rebuild từ immutable raw log có khôi phục (recovery / 복구) mô hình (model / 모델) khác chuỗi xử lý (pipeline / 파이프라인) chỉ giữ transformed latest trạng thái (state / 상태). Khả năng recompute là một tài sản kiến trúc, nhưng phải cân bằng với lưu trữ (storage / 저장소) chi phí (cost / 비용) và retention/privacy chính sách (policy / 정책).

> **Chuyển mạch:** Ở chặng này của **04 — độ tin cậy (reliability / 신뢰성), dữ liệu (data / 데이터) chất lượng (quality / 품질) và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론)**, **9. bảo mật (security / 보안) và quản trị (governance / 거버넌스)** tiếp nhận điểm tựa từ **8. khôi phục (recovery / 복구) và disaster thinking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. hiệu năng (performance / 성능) và chi phí (cost / 비용) trong môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. bảo mật (security / 보안) và quản trị (governance / 거버넌스)

Dữ liệu (data / 데이터) nền tảng (platform / 플랫폼) thường tập trung dữ liệu từ nhiều nguồn (source / 소스) nên blast radius của quyền truy cập rất lớn. Principle of least privilege cần áp dụng cho dịch vụ (service / 서비스) account, engineer và bên tiêu thụ (consumer / 소비자).

Encryption at rest/in transit là nền tảng nhưng không thay thế authorization. Sensitive trường dữ liệu (field / 필드) có thể cần masking/tokenization, row/column-level truy cập (access / 접근) và nhật ký kiểm tra (audit log / 감사 로그). Development môi trường (environment / 환경) không nên mặc định bản sao (copy / 복사) môi trường vận hành (production / 운영 환경) PII nguyên vẹn.

Retention cũng là bảo mật (security / 보안) thuộc tính (property / 속성). Giữ dữ liệu vô thời hạn làm tăng attack surface và có thể xung đột chính sách (policy / 정책)/pháp lý. dữ liệu (data / 데이터) vòng đời (lifecycle / 생명주기) phải bao gồm deletion, không chỉ ingestion.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — độ tin cậy (reliability / 신뢰성), dữ liệu (data / 데이터) chất lượng (quality / 품질) và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론)**, **10. hiệu năng (performance / 성능) và chi phí (cost / 비용) trong môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **9. bảo mật (security / 보안) và quản trị (governance / 거버넌스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. hiệu năng (performance / 성능) và chi phí (cost / 비용) trong môi trường vận hành (production / 운영 환경)

Khi chuỗi xử lý (pipeline / 파이프라인) chậm, đừng tối ưu theo cảm giác. Tách thời gian thành nguồn (source / 소스) read, serialization, mạng (network / 네트워크), compute, shuffle, sink ghi (write / 쓰기) và orchestration wait. Xác định bottleneck trước.

Phân tán (distributed / 분산) job có thể chậm vì dữ liệu (data / 데이터) skew: một key chiếm phần lớn records khiến một tác vụ (task / 작업) xử lý lâu hơn tất cả tác vụ (task / 작업) khác. Tăng số worker không nhất thiết giải quyết hotspot. Cần thay partition chiến lược (strategy / 전략), pre-aggregation, salting hoặc xử lý heavy hitter riêng tùy ngữ nghĩa (semantics / 의미론).

Chi phí (cost / 비용) cũng phải nhìn theo đơn vị (unit / 단위) kinh doanh như chi phí (cost / 비용) trên TB processed, chi phí (cost / 비용) trên chuỗi xử lý (pipeline / 파이프라인) run hoặc chi phí (cost / 비용) trên dữ liệu (data / 데이터) sản phẩm (product / 제품), thay vì chỉ tổng hóa đơn. đơn vị (unit / 단위) economics giúp thấy regression khi volume thay đổi.

> **Chuyển mạch:** Trong **04 — độ tin cậy (reliability / 신뢰성), dữ liệu (data / 데이터) chất lượng (quality / 품질) và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론)**, **11. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **10. hiệu năng (performance / 성능) và chi phí (cost / 비용) trong môi trường vận hành (production / 운영 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. độ tin cậy (reliability / 신뢰성) ngân sách (budget / 예산) cho dữ liệu (data / 데이터) sản phẩm (product / 제품)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) lập luận (reasoning / 추론)

Khi chỉ số (metric / 지표) sai, debugging nên đi ngược lineage: bên tiêu thụ (consumer / 소비자) thấy gì → serving bảng (table / 테이블) được publish khi nào → transformation dùng đầu vào (input / 입력) snapshot nào → ingestion có gap/duplicate không → nguồn (source / 소스) có thay ngữ nghĩa (semantics / 의미론) không.

Giữ run siêu dữ liệu (metadata / 메타데이터) như mã (code / 코드) phiên bản (version / 버전), đầu vào (input / 입력) partitions/snapshot, row counts, checkpoint, lược đồ (schema / 스키마) phiên bản (version / 버전) và đầu ra (output / 출력) lần ghi nhận (commit / 커밋) giúp biến debugging từ suy đoán thành điều tra dựa trên bằng chứng (evidence / 증거).

Một hệ thống dữ liệu trưởng thành không phải hệ thống không bao giờ lỗi. Nó là hệ thống phát hiện lỗi sớm, giới hạn blast radius, giải thích được trạng thái, replay/recover có kiểm soát và học được từ sự cố (incident / 인시던트) để bất biến (invariant / 불변식) được bảo vệ tốt hơn ở lần sau.

> **Chuyển mạch:** Ở chặng này của **04 — độ tin cậy (reliability / 신뢰성), dữ liệu (data / 데이터) chất lượng (quality / 품질) và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론)**, **11. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) lập luận (reasoning / 추론)** nêu điều cần giải thích; **12. độ tin cậy (reliability / 신뢰성) ngân sách (budget / 예산) cho dữ liệu (data / 데이터) sản phẩm (product / 제품)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **13. cổng chất lượng (quality gate / 품질 게이트) theo tầng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. độ tin cậy (reliability / 신뢰성) ngân sách (budget / 예산) cho dữ liệu (data / 데이터) sản phẩm (product / 제품)

Dữ liệu (data / 데이터) sản phẩm (product / 제품) nên có SLO riêng thay vì chỉ dùng tác vụ (task / 작업) success tỷ lệ (rate / 비율):

```text
freshness SLO       = thời gian tối đa từ source event đến publish
completeness SLO    = tỷ lệ input cần có đã được xử lý
correctness SLO     = tỷ lệ reconciliation/quality gate đạt
availability SLO    = consumer có đọc được version hợp lệ không
```

Một job chạy xanh 99.9% nhưng freshness trễ 4 giờ vẫn có thể vi phạm sản phẩm (product / 제품) SLO. lỗi (error / 오류) ngân sách (budget / 예산) nên được dùng để quyết định có ưu tiên tính năng (feature / 기능) mới, backfill hay độ tin cậy (reliability / 신뢰성) công việc (work / 작업).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — độ tin cậy (reliability / 신뢰성), dữ liệu (data / 데이터) chất lượng (quality / 품질) và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론)**, **12. độ tin cậy (reliability / 신뢰성) ngân sách (budget / 예산) cho dữ liệu (data / 데이터) sản phẩm (product / 제품)** nêu điều cần giải thích; **13. cổng chất lượng (quality gate / 품질 게이트) theo tầng** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **14. sự cố (incident / 인시던트) timeline và bằng chứng (evidence / 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. cổng chất lượng (quality gate / 품질 게이트) theo tầng

Chất lượng (quality / 품질) check nên đặt gần thất bại (failure / 실패) ranh giới (boundary / 경계):

1. ingestion: lược đồ (schema / 스키마), checksum, duplicate định danh (identity / 식별자), nguồn (source / 소스) cursor;
2. transformation: grain, uniqueness, referential integrity, accepted lĩnh vực (domain / 도메인);
3. publish: row count, freshness, reconciliation, snapshot completeness;
4. serving: chỉ số (metric / 지표) golden set, point-in-time tính đúng đắn (correctness / 정확성), bên tiêu thụ (consumer / 소비자) đặc tả hợp đồng (contract / 계약).

Check ở tầng cuối không thay thế check ở tầng trước. Nếu chỉ kiểm tra dashboard, rất khó biết mất dữ liệu xảy ra ở nguồn (source / 소스), vận chuyển (transport / 전송) hay phép nối (join / 조인).

> **Chuyển mạch:** Trong **04 — độ tin cậy (reliability / 신뢰성), dữ liệu (data / 데이터) chất lượng (quality / 품질) và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론)**, **13. cổng chất lượng (quality gate / 품질 게이트) theo tầng** nêu điều cần giải thích; **14. sự cố (incident / 인시던트) timeline và bằng chứng (evidence / 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **15. Chaos và khôi phục (recovery / 복구) kiểm thử (test / 테스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. sự cố (incident / 인시던트) timeline và bằng chứng (evidence / 증거)

Một sự cố (incident / 인시던트) report tốt không chỉ có “job failed”. Nó ghi lại nguồn (source / 소스) watermark, đầu vào (input / 입력) partitions, mã (code / 코드)/lược đồ (schema / 스키마) phiên bản (version / 버전), checkpoint, đầu ra (output / 출력) lần ghi nhận (commit / 커밋), chất lượng (quality / 품질) results, bên tiêu thụ (consumer / 소비자) impact và các quyết định quay lui (rollback / 롤백)/replay.

Timeline cần phân biệt:

```text
first bad input → first bad transform → bad publish → first consumer observation
```

Phân biệt bốn mốc này giúp tránh sửa nhầm tầng (layer / 계층) và đo được detection lag.

> **Chuyển mạch:** Ở chặng này của **04 — độ tin cậy (reliability / 신뢰성), dữ liệu (data / 데이터) chất lượng (quality / 품질) và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론)**, **14. sự cố (incident / 인시던트) timeline và bằng chứng (evidence / 증거)** nêu điều cần giải thích; **15. Chaos và khôi phục (recovery / 복구) kiểm thử (test / 테스트)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 15. Chaos và khôi phục (recovery / 복구) kiểm thử (test / 테스트)

Khôi phục (recovery / 복구) claim phải được kiểm chứng bằng thử nghiệm: kill worker trước/sau sink lần ghi nhận (commit / 커밋), làm mất acknowledgement, inject late sự kiện (event / 이벤트), truncate nguồn (source / 소스) retention giả lập, chạy duplicate backfill và restore snapshot. kiểm thử (test / 테스트) cần kiểm tra cả đầu ra (output / 출력) tính đúng đắn (correctness / 정확성) lẫn absence of unwanted side tác động (effect / 효과).

Một runbook chưa từng chạy trong điều kiện gần môi trường vận hành (production / 운영 환경) chỉ là giả thuyết. khôi phục (recovery / 복구) thời gian (time / 시간) phải được đo, không suy ra từ sơ đồ kiến trúc (architecture / 아키텍처).

> **Bàn giao:** Sau **15. Chaos và khôi phục (recovery / 복구) kiểm thử (test / 테스트)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
