# Advanced AI & ML Các hệ thống (systems / 시스템들)

Phần này giữ AI Foundations trong ranh giới (boundary / 경계) của Khoa học máy tính (computer science / 컴퓨터 과학): mô hình (model / 모델) vòng đời (lifecycle / 생명주기), huấn luyện (training / 학습)/suy luận (inference / 추론) các hệ thống (systems / 시스템들), accelerator utilization, phân tán (distributed / 분산) thực thi (execution / 실행) và môi trường vận hành (production / 운영 환경) evaluation. Không mở chapter chỉ vì một mô hình (model / 모델) family hay khung phần mềm (framework / 프레임워크) đang nổi.

## Chuẩn gốc (canonical / 정본) chapters

1. [Training, inference systems và model lifecycle](./00_training_inference_systems_and_model_lifecycle.md)
2. [Transformer internals, attention, KV cache và inference cost](./01_transformer_attention_kv_cache_and_inference_cost.md)
3. [Distributed training: data, model và pipeline parallelism](./02_distributed_training_data_model_and_pipeline_parallelism.md)
4. [Inference disaggregation, prefill/decode và placement của KV cache](./03_inference_disaggregation_prefill_decode_and_kv_cache_placement.md)

## Mô hình tư duy (mental models / 사고 모델들) cần đạt

AI hệ thống (system / 시스템) phải được đọc như một versioned dataflow có trạng thái (state / 상태) và tài nguyên (resource / 자원) các ràng buộc (constraints / 제약조건들):

```text
data/version
→ preprocessing/tokenization
→ training state/checkpoint
→ model artifact
→ serving runtime
→ batching/cache/accelerator memory
→ prediction
→ evaluation/feedback
```

Ở suy luận (inference / 추론), cần thêm trạng thái (state / 상태) đường dẫn (path / 경로):

```text
admission
→ prefill
→ KV state
→ placement / transfer
→ decode loop
→ token stream
→ cancellation / cleanup
```

Mỗi stage có bất biến (invariant / 불변식) riêng: sản phẩm tạo ra (artifact / 산출물) lineage phải truy được, train/eval phân phối (distribution / 분포) phải được phân biệt, checkpoint phải đủ trạng thái (state / 상태) để resume theo đặc tả hợp đồng (contract / 계약), serving phải tôn trọng độ trễ (latency / 지연 시간)/sức chứa (capacity / 용량) ngân sách (budget / 예산), KV trạng thái (state / 상태) phải gắn đúng mô hình (model / 모델)/yêu cầu (request / 요청)/phiên bản (version / 버전) và online hành vi (behavior / 동작) phải được đánh giá bằng bằng chứng (evidence / 증거) phù hợp chứ không chỉ offline chỉ số (metric / 지표).

## Hiệu năng (performance / 성능) pressure

AI hiệu năng (performance / 성능) không chỉ là FLOPS. Bottleneck có thể nằm ở đầu vào (input / 입력) chuỗi xử lý (pipeline / 파이프라인), host-device transfer, accelerator bộ nhớ (memory / 메모리), KV bộ nhớ đệm (cache / 캐시), communication collective, batching delay hoặc yêu cầu (request / 요청) hàng đợi (queue / 큐). Vì vậy phải phân biệt compute-bound, memory-bound và communication-bound hành vi (behavior / 동작).

Prefill và decode cũng không có tài nguyên (resource / 자원) profile giống nhau. Prefill thường có parallel compute lớn hơn; decode lặp theo đơn vị từ (token / 토큰) và dễ bị bộ nhớ (memory / 메모리)/KV/scheduler pressure. Disaggregation chỉ có lợi khi specialization/independent scaling lớn hơn state-transfer chi phí (cost / 비용), extra hàng đợi (queue / 큐) và thất bại (failure / 실패) surface.

Phân tán (distributed / 분산) huấn luyện (training / 학습) là hệ thống phân tán (distributed system / 분산 시스템): synchronization, straggler, topology và thất bại (failure / 실패) khôi phục (recovery / 복구) quyết định scaling efficiency. Suy luận (inference / 추론) serving cũng là software hệ thống (system / 시스템): queueing, admission điều khiển (control / 제어), bộ nhớ đệm (cache / 캐시) thời gian tồn tại (lifetime / 수명), placement, phiên bản (version / 버전) rollout và cancellation quyết định tail độ trễ (latency / 지연 시간)/độ tin cậy (reliability / 신뢰성).

## Liên kết (connection / 연결) với các lĩnh vực (domain / 도메인) khác

Không duplicate nội dung system-level đã có. Hàng đợi (queue / 큐)/sức chứa (capacity / 용량) đọc tại [`08_software_systems/advanced`](../../08_software_systems/advanced/README.md), phân tán (distributed / 분산) coordination tại [`06_networks_distributed_systems/advanced`](../../06_networks_distributed_systems/advanced/README.md), triển khai (deployment / 배포)/evolution tại [`09_software_engineering/advanced`](../../09_software_engineering/advanced/README.md), hardware/bộ nhớ đệm (cache / 캐시)/SIMD/GPU/DVFS tại [`02_computer_architecture/advanced`](../../02_computer_architecture/advanced/README.md).

Retrieval, véc-tơ (vector / 벡터) tìm kiếm (search / 검색), MLOps hay mô hình (model / 모델) bảo mật (security / 보안) chỉ được mở rộng ở đây nếu cần một mô hình tư duy (mental model / 사고 모델) foundational mới; nếu đã thuộc AI specialization riêng thì cross-link thay vì duplicate.

## Bằng chứng vận hành (production evidence / 운영 증거)

Bằng chứng (evidence / 증거) cần bao phủ cả mô hình (model / 모델) và hệ thống (system / 시스템): dataset/sản phẩm tạo ra (artifact / 산출물) phiên bản (version / 버전), huấn luyện (training / 학습) thông lượng (throughput / 처리량)/utilization, checkpoint/khôi phục (recovery / 복구) trạng thái (state / 상태), communication stalls, accelerator bộ nhớ (memory / 메모리)/KV-cache pressure, prefill/decode hàng đợi (queue / 큐) riêng, TTFT, inter-token độ trễ (latency / 지연 시간), KV transfer/placement thời gian (time / 시간), active chuỗi (sequence / 시퀀스)/đơn vị từ (token / 토큰) ngân sách (budget / 예산), độ trễ (latency / 지연 시간) percentile, lỗi (error / 오류)/hết thời gian chờ (timeout / 타임아웃)/cancellation, mô hình (model / 모델) phiên bản (version / 버전)/cohort, drift/data-quality tín hiệu (signal / 신호) và offline-online chỉ số (metric / 지표) gap.

Một mô hình (model / 모델) “accuracy tốt” nhưng không đạt độ trễ (latency / 지연 시간)/chi phí (cost / 비용)/độ tin cậy (reliability / 신뢰성) yêu cầu (requirement / 요구사항) vẫn là môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) không đạt đặc tả hợp đồng (contract / 계약). Một accelerator utilization cao cũng chưa chứng minh hệ thống hiệu quả nếu useful-token thông lượng (throughput / 처리량) thấp hoặc hàng đợi (queue / 큐)/tail độ trễ (latency / 지연 시간) vượt SLO.