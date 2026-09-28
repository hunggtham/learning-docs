# Advanced AI & ML các hệ thống (systems / 시스템들)

> **Mạch đọc:** Đọc **Advanced AI & ML các hệ thống (systems / 시스템들)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **chuẩn gốc (canonical / 정본) chapters** sang **mô hình tư duy (mental models / 사고 모델들) cần đạt**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Phần này giữ AI Foundations trong ranh giới (boundary / 경계) của Khoa học máy tính (computer science / 컴퓨터 과학): mô hình (model / 모델) vòng đời (lifecycle / 생명주기), huấn luyện (training / 학습)/suy luận (inference / 추론) các hệ thống (systems / 시스템들), accelerator utilization, phân tán (distributed / 분산) thực thi (execution / 실행) và môi trường vận hành (production / 운영 환경) evaluation. Không mở chapter chỉ vì một mô hình (model / 모델) family hay khung phần mềm (framework / 프레임워크) đang nổi.

## Chuẩn gốc (canonical / 정본) chapters

1. [Training, inference systems và model lifecycle](./00_training_inference_systems_and_model_lifecycle.md)
2. [Transformer internals, attention, KV cache và inference cost](./01_transformer_attention_kv_cache_and_inference_cost.md)
3. [Distributed training: data, model và pipeline parallelism](./02_distributed_training_data_model_and_pipeline_parallelism.md)


> **Chuyển mạch:** Từ **chuẩn gốc (canonical / 정본) chapters**, ta sang **mô hình tư duy (mental models / 사고 모델들) cần đạt** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

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

Mỗi stage có bất biến (invariant / 불변식) riêng: sản phẩm tạo ra (artifact / 산출물) lineage phải truy được, train/eval phân phối (distribution / 분포) phải được phân biệt, checkpoint phải đủ trạng thái (state / 상태) để resume theo đặc tả hợp đồng (contract / 계약), serving phải tôn trọng độ trễ (latency / 지연 시간)/sức chứa (capacity / 용량) ngân sách (budget / 예산), và online hành vi (behavior / 동작) phải được đánh giá bằng bằng chứng (evidence / 증거) phù hợp chứ không chỉ offline chỉ số (metric / 지표).


> **Chuyển mạch:** Từ **mô hình tư duy (mental models / 사고 모델들) cần đạt**, ta sang **hiệu năng (performance / 성능) pressure** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Hiệu năng (performance / 성능) pressure

AI hiệu năng (performance / 성능) không chỉ là FLOPS. Bottleneck có thể nằm ở đầu vào (input / 입력) chuỗi xử lý (pipeline / 파이프라인), host-device transfer, accelerator bộ nhớ (memory / 메모리), KV bộ nhớ đệm (cache / 캐시), communication collective, batching delay hoặc yêu cầu (request / 요청) hàng đợi (queue / 큐). Vì vậy phải phân biệt compute-bound, memory-bound và communication-bound hành vi (behavior / 동작).

Phân tán (distributed / 분산) huấn luyện (training / 학습) cũng là hệ thống phân tán (distributed system / 분산 시스템): synchronization, straggler, topology và thất bại (failure / 실패) khôi phục (recovery / 복구) quyết định scaling efficiency. suy luận (inference / 추론) serving cũng là software hệ thống (system / 시스템): queueing, admission điều khiển (control / 제어), bộ nhớ đệm (cache / 캐시) thời gian tồn tại (lifetime / 수명) và phiên bản (version / 버전) rollout quyết định tail độ trễ (latency / 지연 시간)/độ tin cậy (reliability / 신뢰성).


> **Chuyển mạch:** Từ **hiệu năng (performance / 성능) pressure**, ta sang **liên kết (connection / 연결) với các lĩnh vực (domain / 도메인) khác** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Liên kết (connection / 연결) với các lĩnh vực (domain / 도메인) khác

Không duplicate nội dung system-level đã có. hàng đợi (queue / 큐)/sức chứa (capacity / 용량) đọc tại [`08_software_systems/advanced`](../../08_software_systems/advanced/README.md), phân tán (distributed / 분산) coordination tại [`06_networks_distributed_systems/advanced`](../../06_networks_distributed_systems/advanced/README.md), triển khai (deployment / 배포)/evolution tại [`09_software_engineering/advanced`](../../09_software_engineering/advanced/README.md), hardware/bộ nhớ đệm (cache / 캐시)/SIMD/GPU tại [`02_computer_architecture/advanced`](../../02_computer_architecture/advanced/README.md).

Retrieval, véc-tơ (vector / 벡터) tìm kiếm (search / 검색), MLOps hay mô hình (model / 모델) bảo mật (security / 보안) chỉ được mở rộng ở đây nếu cần một mô hình tư duy (mental model / 사고 모델) foundational mới; nếu đã thuộc AI specialization riêng thì cross-link thay vì duplicate.


> **Chuyển mạch:** Từ **liên kết (connection / 연결) với các lĩnh vực (domain / 도메인) khác**, ta sang **bằng chứng vận hành (production evidence / 운영 증거)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bằng chứng vận hành (production evidence / 운영 증거)

Bằng chứng (evidence / 증거) cần bao phủ cả mô hình (model / 모델) và hệ thống (system / 시스템): dataset/sản phẩm tạo ra (artifact / 산출물) phiên bản (version / 버전), huấn luyện (training / 학습) thông lượng (throughput / 처리량)/utilization, checkpoint/khôi phục (recovery / 복구) trạng thái (state / 상태), communication stalls, accelerator bộ nhớ (memory / 메모리)/KV-cache pressure, hàng đợi (queue / 큐)/batch wait, độ trễ (latency / 지연 시간) percentile, lỗi (error / 오류)/hết thời gian chờ (timeout / 타임아웃), mô hình (model / 모델) phiên bản (version / 버전)/cohort, drift/data-quality tín hiệu (signal / 신호) và offline-online chỉ số (metric / 지표) gap.

Một mô hình (model / 모델) “accuracy tốt” nhưng không đạt độ trễ (latency / 지연 시간)/chi phí (cost / 비용)/độ tin cậy (reliability / 신뢰성) yêu cầu (requirement / 요구사항) vẫn là môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) không đạt đặc tả hợp đồng (contract / 계약).

> **Bàn giao:** Sau **bằng chứng vận hành (production evidence / 운영 증거)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 training inference systems and model lifecycle](./00_training_inference_systems_and_model_lifecycle.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
