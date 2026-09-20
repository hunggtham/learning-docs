# Distributed training: data, model và pipeline parallelism

Modern model có thể quá lớn hoặc training quá chậm cho một accelerator. Distributed training chia computation/state qua nhiều GPUs/nodes, nhưng speedup bị giới hạn bởi communication, synchronization và imbalance chứ không chỉ số thiết bị.

## Data parallelism

Mỗi worker giữ model replica và xử lý mini-batch khác nhau. Sau backward pass, gradients được aggregate, thường qua all-reduce, để replicas cập nhật nhất quán.

Nếu computation mỗi step ít so với gradient communication, thêm GPUs cho diminishing returns. Batch size cũng thường tăng, có thể thay optimization dynamics.

## Model/tensor parallelism

Khi model không vừa một device, tensor/matrix operations được shard. Một layer có thể cần collectives giữa devices trong forward/backward.

High-bandwidth interconnect trở thành critical. Partition tốt phải cân bằng compute và giảm communication volume.

## Pipeline parallelism

Layers được chia thành stages trên devices. Micro-batches chạy như assembly line. Nếu stage chậm hơn, toàn pipeline bị giới hạn bởi bottleneck stage; đầu/cuối schedule có **pipeline bubble** không tận dụng đủ devices.

Scheduling strategy đổi memory footprint, staleness và utilization.

## Optimizer state và sharding

Training không chỉ lưu parameters. Gradients và optimizer states như Adam moments có thể chiếm nhiều lần model size. ZeRO-style sharding phân tán optimizer state, gradients và parameters để giảm memory mỗi worker.

Memory accounting phải tính activations, temporary buffers và communication workspace, không chỉ checkpoint size.

## Collective communication

All-reduce, all-gather, reduce-scatter là primitives chính. Topology-aware algorithms tận dụng NVLink/intra-node bandwidth trước khi đi inter-node network.

Straggler một worker có thể kéo dài synchronous step vì mọi worker chờ collective.

## Fault tolerance

Training nhiều ngày tăng xác suất node failure. Checkpoint cần đủ model/optimizer/scheduler/random state để resume gần đúng trajectory.

Checkpoint quá thường xuyên tốn I/O; quá thưa mất nhiều compute khi failure.

## Scaling efficiency

Nếu 8 GPUs chỉ nhanh gấp 5 lần 1 GPU, efficiency là khoảng 62.5%. Phần mất đi đến từ communication, idle/bubbles, input pipeline và synchronization.

Amdahl's law cung cấp mental model: phần serial/coordination cuối cùng giới hạn speedup.

## Mental Model

> Distributed training là bài toán partition computation, memory và communication. Thêm accelerator chỉ hữu ích khi mỗi device có đủ work và interconnect không biến synchronization thành bottleneck.