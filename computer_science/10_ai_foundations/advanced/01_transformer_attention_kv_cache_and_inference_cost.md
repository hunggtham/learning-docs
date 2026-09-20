# Transformer internals, attention, KV cache và inference cost

Transformer trở nên quan trọng không chỉ vì model quality mà vì architecture của nó ánh xạ tốt lên parallel hardware trong training. Tuy nhiên training và autoregressive inference có cost profile khác nhau. Hiểu attention, KV cache và memory bandwidth giúp giải thích vì sao cùng một model có throughput/latency rất khác tùy batch, context length và hardware.

## Token representation và layer flow

Input tokens được ánh xạ thành vectors. Mỗi transformer block thường kết hợp attention với feed-forward network, residual connections và normalization. Attention cho mỗi position khả năng tổng hợp information từ các positions khác thay vì chỉ truyền state tuần tự như recurrent network cổ điển.

## Query, Key, Value

Mỗi token representation được project thành **Q, K, V**. Similarity giữa query hiện tại và keys tạo weights; weighted combination của values tạo output attention.

Multi-head attention thực hiện nhiều projections để model học nhiều relation subspaces. Đây là mechanism; “head này luôn đại diện grammar” không phải guarantee kiến trúc.

## Vì sao self-attention có quadratic component?

Với sequence length `n`, full attention tạo relation giữa nhiều cặp positions, dẫn tới attention matrix cỡ `n × n`. Training long context vì thế có memory/compute pressure tăng nhanh, dù implementation tối ưu như tiled/flash attention có thể giảm memory traffic đáng kể mà không thay mathematical result.

## Autoregressive inference khác training

Khi generate token từng bước, model không cần tính lại key/value của toàn prefix nếu lưu chúng. **KV cache** giữ K/V của các tokens trước cho mỗi layer. Token mới chỉ tính projection mới rồi attend vào cache.

Điều này giảm recomputation nhưng KV cache tăng gần tuyến tính theo context length, batch/concurrent sequences, number of layers và KV dimensions.

## Memory bandwidth trở thành bottleneck

Decode một token thường phải đọc lượng lớn model weights và KV cache để thực hiện tương đối ít work cho một sequence. Vì vậy inference có thể memory-bandwidth-bound thay vì pure compute-bound.

Batching cho phép reuse weight reads cho nhiều sequences và tăng hardware utilization, nhưng batch lớn tăng queueing latency. Serving system phải cân throughput với time-to-first-token và inter-token latency.

## Prefill và decode là hai phases

**Prefill** xử lý prompt ban đầu, có nhiều tokens có thể parallelize và thường compute-heavy hơn. **Decode** sinh từng token sequential theo dependency autoregressive và thường nhạy memory bandwidth/latency.

Tách hai phases trong metrics giúp tránh average che giấu bottleneck.

## Quantization

Giảm precision của weights/activations/KV có thể giảm memory footprint và bandwidth, đôi khi tăng throughput. Nhưng quality loss và kernel/hardware support phụ thuộc quantization scheme. “4-bit” không tự động nhanh hơn nếu dequantization hoặc kernel path không phù hợp.

## Context length không miễn phí

Context dài làm KV cache lớn, attention work tăng và giảm số concurrent requests fit GPU memory. Product cho phép context cực lớn nhưng workload thường dùng ngắn cần capacity planning theo distribution thực tế, không chỉ maximum advertised context.

## Serving scheduler

Continuous batching có thể đưa requests mới vào batch động thay vì chờ batch cố định kết thúc. Paged KV-cache management giảm fragmentation bằng cách quản lý cache theo blocks/pages. Những kỹ thuật này cho thấy AI serving là bài toán operating/system scheduling chứ không chỉ model code.

## Mental model

> Transformer inference là interaction giữa model math và memory system. Attention quyết định dependency structure; KV cache đổi recomputation lấy memory; batching đổi latency lấy throughput; quantization đổi precision lấy footprint/bandwidth. Muốn tối ưu serving phải đo prefill, decode, cache memory và hardware utilization riêng.