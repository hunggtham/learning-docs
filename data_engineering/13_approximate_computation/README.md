# 13 — Approximate computation và lỗi (error / 오류) bounds

> **Mạch đọc:** Đọc **13 — Approximate computation và lỗi (error / 오류) bounds** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. chính xác (exact / 정확한) không phải lúc nào cũng là mục tiêu tối ưu** sang **2. Sketch phải merge được**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Approximate computation là cách đổi một phần exactness lấy độ trễ (latency / 지연 시간), bộ nhớ (memory / 메모리) hoặc chi phí (cost / 비용) có giới hạn. Nó chỉ đúng khi lỗi (error / 오류) được định nghĩa, đo được và phù hợp với quyết định của bên tiêu thụ (consumer / 소비자).

## 1. chính xác (exact / 정확한) không phải lúc nào cũng là mục tiêu tối ưu

`COUNT(DISTINCT user_id)` trên hàng tỷ row có thể cần trạng thái (state / 상태) lớn hoặc shuffle lớn. Một estimate nhanh với sai số ±1% có thể đủ cho sức chứa (capacity / 용량) planning nhưng không đủ cho billing. đặc tả hợp đồng (contract / 계약) phải nêu rõ chỉ số (metric / 지표) này là estimate hay nguồn chuẩn (source of truth / 정본).


> **Chuyển mạch:** Từ **1. chính xác (exact / 정확한) không phải lúc nào cũng là mục tiêu tối ưu**, ta sang **2. Sketch phải merge được** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. Sketch phải merge được

Trong hệ thống phân tán (distributed system / 분산 시스템), mỗi worker tạo partial sketch rồi merge:

```text
input → local sketch_1 ... sketch_n → merge → estimate + bound
```

Merge thao tác (operation / 연산) cần associative/commutative để thử lại (retry / 재시도) và partition thứ tự (order / 순서) không thay đổi kết quả ngoài bound. Sketch trạng thái (state / 상태) phải có phiên bản (version / 버전), parameter và băm (hash / 해시) hàm (function / 함수) ổn định; đổi chúng giữa run làm estimate không comparable.


> **Chuyển mạch:** Từ **2. Sketch phải merge được**, ta sang **3. Cardinality và quantile** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. Cardinality và quantile

Distinct sketch như HyperLogLog lưu register thay vì mọi định danh (identity / 식별자). Sai số phụ thuộc số register, độ lệch (bias / 편향) correction và băm (hash / 해시) phân phối (distribution / 분포). Quantile sketch phải phân biệt rank lỗi (error / 오류) với giá trị (value / 값) lỗi (error / 오류): ±1% percentile rank không đồng nghĩa giá trị nằm trong ±1%.

Không dùng average của percentile từ từng partition để suy ra percentile toàn cục. Cần merge sketch hoặc giữ weighted phân phối (distribution / 분포) phù hợp.


> **Chuyển mạch:** Từ **3. Cardinality và quantile**, ta sang **4. Sampling** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. Sampling

Random mẫu (sample / 표본) đơn giản nhưng dễ độ lệch (bias / 편향) nếu sampling theo partition, tenant hoặc thời gian. Stratified sampling bảo vệ nhóm nhỏ nhưng cần allocation và weight đúng. Mọi estimate phải lưu sampling frame, seed, tỷ lệ (rate / 비율) và confidence interval.


> **Chuyển mạch:** Từ **4. Sampling**, ta sang **5. lỗi (error / 오류) đặc tả hợp đồng (contract / 계약)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. lỗi (error / 오류) đặc tả hợp đồng (contract / 계약)

Một approximate chỉ số (metric / 지표) cần siêu dữ liệu (metadata / 메타데이터):

```text
estimate + error definition + confidence/bound
→ method/version + input scope + freshness
```

Không ghi một số estimate vào cột `count` như thể chính xác (exact / 정확한). Serving tầng (layer / 계층) nên hiển thị bất định (uncertainty / 불확실성) khi quyết định có thể bị ảnh hưởng bởi bound.


> **Chuyển mạch:** Từ **5. lỗi (error / 오류) đặc tả hợp đồng (contract / 계약)**, ta sang **6. thất bại (failure / 실패) và bằng chứng (evidence / 증거)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 6. thất bại (failure / 실패) và bằng chứng (evidence / 증거)
Phần “6. thất bại (failure / 실패) và bằng chứng (evidence / 증거)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- băm (hash / 해시) collision hoặc đầu vào (input / 입력) phân phối (distribution / 분포) bất thường;
- sketch phiên bản (version / 버전) đổi làm số liệu nhảy;
- merge thiếu một partition nhưng job vẫn xanh;
- mẫu (sample / 표본) bỏ sót heavy hitter;
- estimate bị bộ nhớ đệm (cache / 캐시) lâu hơn freshness đặc tả hợp đồng (contract / 계약).

Bằng chứng (evidence / 증거) cần có chính xác (exact / 정확한) mẫu (sample / 표본) đối chiếu, lỗi (error / 오류) phân phối (distribution / 분포) theo segment, canary run, sketch siêu dữ liệu (metadata / 메타데이터) và reconciliation khi có thể.


> **Chuyển mạch:** Từ **6. thất bại (failure / 실패) và bằng chứng (evidence / 증거)**, ta sang **7. Khi nào không được approximate** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 7. Khi nào không được approximate

Billing, entitlement, compliance count, deletion kiểm tra (audit / 감사) và financial ledger thường cần chính xác (exact / 정확한) hoặc quy trình correction rõ. Approximation có thể dùng cho monitoring/triage nhưng không được âm thầm thay nguồn chuẩn (source of truth / 정본).

Đọc tiếp: [06 — Distributed processing](../06_distributed_processing/README.md), [10 — Serving](../10_serving_semantic_layer/README.md), [12 — Cost](../12_cost_performance_capacity/README.md).

> **Bàn giao:** Sau **7. Khi nào không được approximate**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp.
