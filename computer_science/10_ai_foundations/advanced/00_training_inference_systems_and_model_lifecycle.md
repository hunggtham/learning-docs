# Training, inference systems và model lifecycle

Foundation ML thường tập trung model, loss và generalization. Production AI cần thêm mental model: **data và model đi qua một lifecycle**, và mỗi stage có artifact, state, version, resource bottleneck và failure mode riêng.

## Training system là dataflow + optimization state

Một training step không chỉ là `loss.backward()`. Pipeline thường gồm storage → decode/preprocess → shuffle/batch → host memory → accelerator transfer → forward → loss → backward → optimizer update → checkpoint/metrics.

Nếu GPU utilization thấp, nguyên nhân có thể là input pipeline hoặc synchronization chứ không phải model compute. Performance tuning vì vậy cần profile toàn pipeline.

## Checkpoint không chỉ lưu weights

Để resume training tương đương, thường cần model parameters, optimizer state, scheduler state, gradient scaler nếu mixed precision, random state và progress metadata. Chỉ lưu weights có thể resume “một model” nhưng không resume cùng optimization trajectory.

Distributed setup còn cần mapping/sharding state tương thích topology hoặc conversion logic.

## Distributed training có communication cost

Data parallelism replicate model và chia batch; gradients cần aggregate. Khi model/optimizer không fit một device, model/tensor/pipeline parallelism chia computation/state theo dimensions khác.

Speedup không tuyến tính vô hạn. Communication, synchronization bubbles, load imbalance và small batch per device có thể trở thành bottleneck. Chọn parallel strategy dựa memory footprint, compute/communication ratio và interconnect.

## Inference có objective khác training

Training tối ưu samples/tokens processed per unit cost trong khi inference thường quan tâm latency percentile, throughput, memory per request và availability.

Dynamic batching tăng accelerator utilization nhưng request phải chờ batch formation, tạo latency trade-off. Continuous batching trong autoregressive serving cố tái sử dụng slots khi sequences hoàn tất khác thời điểm.

## KV cache và memory-bound serving

Transformer autoregressive inference lưu key/value states của prior tokens để không recompute toàn prefix mỗi token. KV cache giảm compute nhưng tiêu memory tỷ lệ sequence length × layers × dimensions × concurrent sequences.

Do đó context length dài có thể giảm concurrency dù weights không đổi. Quantization/cache layout/paged allocation trở thành systems problem.

## Quantization và precision

FP16/BF16/INT8/low-bit formats trade numerical fidelity, memory bandwidth, hardware support và calibration complexity. Quantization không đơn giản “giảm bit = nhanh hơn”; kernel availability, dequant overhead và memory bottleneck quyết định speed thực.

Accuracy cần evaluate trên deployment distribution, không chỉ benchmark chung.

## Model registry và artifact identity

Production cần biết chính xác model version nào đang serve, trained từ dataset/code/config nào, evaluation nào đã pass và rollback artifact ở đâu.

Hash/version cho weights mà không version tokenizer/preprocessing/schema vẫn có thể tạo incompatibility. “Model” thực tế là bundle gồm representation pipeline + parameters + runtime assumptions.

## Offline metric và online outcome khác nhau

Model A tốt hơn validation metric chưa chắc tốt hơn user/business outcome do latency, threshold, population shift hoặc feedback loop. Deployment cần shadow/canary/A-B tùy risk và ability to observe outcomes.

Khi labels đến chậm, monitoring phải kết hợp input distribution, confidence/score distribution, data quality và system metrics thay vì giả vờ biết accuracy real-time.

## Retraining là policy, không phải cron job mặc định

Retrain hàng ngày không tự động tốt. Data window, label delay, concept drift, cost và regression risk cần policy. Mỗi retrain tạo candidate cần evaluate, approve và deploy; nếu pipeline tự động hoàn toàn, guardrails phải mạnh tương ứng.

## Mental Model

> Production AI là **versioned dataflow + optimization state + serving system + evaluation feedback loop**. Model weights chỉ là một artifact trong hệ thống đó.

## Kết nối

Ôn [ML foundation](../../basic/10_ai_foundations/02_machine_learning_foundations.md), [neural networks](../../basic/10_ai_foundations/03_neural_networks_and_representation_learning.md), [performance/capacity](../../basic/08_software_systems/02_performance_capacity_and_scalability.md) và [data governance](../../basic/12_society_ethics_profession/01_data_governance_bias_and_algorithmic_impact.md).