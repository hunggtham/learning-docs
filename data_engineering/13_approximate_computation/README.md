# 13 — Approximate computation và lỗi (error / 오류) bounds

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **13 — Approximate computation và lỗi (error / 오류) bounds**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. chính xác (exact / 정확한) không phải lúc nào cũng là mục tiêu tối ưu** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **2. Sketch phải merge được** để mở rộng đối tượng sang phạm vi kế cận. Mạch này dùng README làm bản đồ owner của approximate computation, rồi nối sketching, sampling, error bound và cost.

Approximate computation là cách đổi một phần exactness lấy độ trễ (latency / 지연 시간), bộ nhớ (memory / 메모리) hoặc chi phí (cost / 비용) có giới hạn. Nó chỉ đúng khi lỗi (error / 오류) được định nghĩa, đo được và phù hợp với quyết định của bên tiêu thụ (consumer / 소비자).

## 1. chính xác (exact / 정확한) không phải lúc nào cũng là mục tiêu tối ưu

`COUNT(DISTINCT user_id)` trên hàng tỷ row có thể cần trạng thái (state / 상태) lớn hoặc shuffle lớn. Một estimate nhanh với sai số ±1% có thể đủ cho sức chứa (capacity / 용량) planning nhưng không đủ cho billing. đặc tả hợp đồng (contract / 계약) phải nêu rõ chỉ số (metric / 지표) này là estimate hay nguồn chuẩn (source of truth / 정본).

> **Chuyển mạch:** Khi exact computation vượt ngân sách, **Sketch phải merge được** giữ phép đo phân tán có thể hợp nhất; **Cardinality và quantile** đưa invariant đó vào hai loại ước lượng khác nhau.

## 2. Sketch phải merge được

Trong hệ thống phân tán (distributed system / 분산 시스템), mỗi worker tạo partial sketch rồi merge:

```text
input → local sketch_1 ... sketch_n → merge → estimate + bound
```

Merge thao tác (operation / 연산) cần associative/commutative để thử lại (retry / 재시도) và partition thứ tự (order / 순서) không thay đổi kết quả ngoài bound. Sketch trạng thái (state / 상태) phải có phiên bản (version / 버전), parameter và băm (hash / 해시) hàm (function / 함수) ổn định; đổi chúng giữa run làm estimate không comparable.

> **Chuyển mạch:** **Cardinality và quantile** cho biết merge error biểu hiện ở metric nào; **Sampling** mở rộng câu hỏi sang cách chọn quan sát và bias.

## 3. Cardinality và quantile

Distinct sketch như HyperLogLog lưu register thay vì mọi định danh (identity / 식별자). Sai số phụ thuộc số register, độ lệch (bias / 편향) correction và băm (hash / 해시) phân phối (distribution / 분포). Quantile sketch phải phân biệt rank lỗi (error / 오류) với giá trị (value / 값) lỗi (error / 오류): ±1% percentile rank không đồng nghĩa giá trị nằm trong ±1%.

Không dùng average của percentile từ từng partition để suy ra percentile toàn cục. Cần merge sketch hoặc giữ weighted phân phối (distribution / 분포) phù hợp.

> **Chuyển mạch:** **Sampling** thay đổi population và uncertainty; **Error contract** phải ghi rõ bound, confidence và điều kiện áp dụng trước khi dùng kết quả.

## 4. Sampling

Random mẫu (sample / 표본) đơn giản nhưng dễ độ lệch (bias / 편향) nếu sampling theo partition, tenant hoặc thời gian. Stratified sampling bảo vệ nhóm nhỏ nhưng cần allocation và weight đúng. Mọi estimate phải lưu sampling frame, seed, tỷ lệ (rate / 비율) và confidence interval.

> **Chuyển mạch:** **Error contract** biến uncertainty thành điều kiện kiểm chứng; **Failure và evidence** tìm trường hợp bound không còn đáng tin trong pipeline thật.

## 5. lỗi (error / 오류) đặc tả hợp đồng (contract / 계약)

Một approximate chỉ số (metric / 지표) cần siêu dữ liệu (metadata / 메타데이터):

```text
estimate + error definition + confidence/bound
→ method/version + input scope + freshness
```

Không ghi một số estimate vào cột `count` như thể chính xác (exact / 정확한). Serving tầng (layer / 계층) nên hiển thị bất định (uncertainty / 불확실성) khi quyết định có thể bị ảnh hưởng bởi bound.

> **Chuyển mạch:** Ở chặng này của **13 — Approximate computation và lỗi (error / 오류) bounds**, **5. lỗi (error / 오류) đặc tả hợp đồng (contract / 계약)** nêu điều cần giải thích; **6. thất bại (failure / 실패) và bằng chứng (evidence / 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. Khi nào không được approximate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. thất bại (failure / 실패) và bằng chứng (evidence / 증거)

- băm (hash / 해시) collision hoặc đầu vào (input / 입력) phân phối (distribution / 분포) bất thường;
- sketch phiên bản (version / 버전) đổi làm số liệu nhảy;
- merge thiếu một partition nhưng job vẫn xanh;
- mẫu (sample / 표본) bỏ sót heavy hitter;
- estimate bị bộ nhớ đệm (cache / 캐시) lâu hơn freshness đặc tả hợp đồng (contract / 계약).

Bằng chứng (evidence / 증거) cần có chính xác (exact / 정확한) mẫu (sample / 표본) đối chiếu, lỗi (error / 오류) phân phối (distribution / 분포) theo segment, canary run, sketch siêu dữ liệu (metadata / 메타데이터) và reconciliation khi có thể.

> **Chuyển mạch:** **Failure và evidence** cho thấy approximation đang che rủi ro nào; **Khi nào không được approximate** đặt boundary để quay về phép đo exact hoặc owner domain.

## 7. Khi nào không được approximate

Billing, entitlement, compliance count, deletion kiểm tra (audit / 감사) và financial ledger thường cần chính xác (exact / 정확한) hoặc quy trình correction rõ. Approximation có thể dùng cho monitoring/triage nhưng không được âm thầm thay nguồn chuẩn (source of truth / 정본).

Đọc tiếp: [06 — Distributed processing](../06_distributed_processing/README.md), [10 — Serving](../10_serving_semantic_layer/README.md), [12 — Cost](../12_cost_performance_capacity/README.md).

> **Bàn giao:** Sau **7. Khi nào không được approximate**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
