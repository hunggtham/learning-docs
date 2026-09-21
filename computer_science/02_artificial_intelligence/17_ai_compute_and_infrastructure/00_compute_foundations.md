# Nền tảng Tính toán cho Trí tuệ Nhân tạo

AI hiện đại tồn tại ở giao điểm giữa thuật toán và tính toán vật lý. Một mô hình có thể đúng về mặt toán học nhưng không thực tế nếu bộ nhớ không đủ, băng thông quá thấp hoặc giao tiếp giữa các thiết bị chiếm phần lớn thời gian. Vì vậy hiểu **tính toán AI (AI compute / AI 연산)** giúp nối Đại số tuyến tính, Deep Learning và Production Engineering với phần cứng thực tế.

## Năng lực tính toán không chỉ là FLOPs

Một workload AI tiêu tốn:

```text
phép toán số học
dung lượng bộ nhớ
băng thông bộ nhớ
giao tiếp giữa thiết bị
I/O lưu trữ
I/O mạng
năng lượng
```

Hai mô hình có FLOPs gần nhau vẫn có runtime rất khác nếu pattern truy cập bộ nhớ hoặc cách song song hóa khác.

## Huấn luyện và Suy luận

Huấn luyện cần:

```text
forward pass
backward pass
gradient
trạng thái optimizer
lưu activation
```

Suy luận chủ yếu chạy forward pass, nhưng quá trình sinh nội dung của LLM còn cần KV cache và decode tự hồi quy.

Huấn luyện thường tốn compute và bộ nhớ nhiều hơn trên mỗi token; serving lại nhạy hơn với độ trễ, concurrency và khả năng giữ dữ liệu trong bộ nhớ.

## Cường độ số học

Một kernel có **cường độ số học (arithmetic intensity)** cao nếu thực hiện nhiều phép toán trên mỗi byte dữ liệu được tải. Phép nhân ma trận thường tận dụng accelerator tốt vì cùng dữ liệu được tái sử dụng nhiều lần.

Phép toán có ít tính toán nhưng phải di chuyển nhiều dữ liệu thường bị **giới hạn bởi bộ nhớ (memory-bound)**.

## FLOPs và FLOP/s

FLOPs là số lượng phép toán dấu chấm động. FLOP/s là tốc độ phần cứng thực hiện các phép toán đó.

Peak FLOP/s lý thuyết không đồng nghĩa throughput thực tế. Hiệu năng thật còn phụ thuộc mức sử dụng tài nguyên, precision, hình dạng kernel, bộ nhớ và giao tiếp.

## Precision

AI thường dùng:

```text
FP32
TF32
FP16
BF16
FP8
INT8 / INT4
```

Precision thấp hơn giúp giảm bộ nhớ/băng thông và có thể tăng throughput của accelerator, nhưng độ ổn định số và chất lượng phải được kiểm soát.

## Dung lượng bộ nhớ cần thiết

Bộ nhớ cho huấn luyện không chỉ gồm trọng số:

```text
trọng số
gradient
trạng thái optimizer
activation
buffer tạm
```

Adam có trạng thái optimizer khiến bộ nhớ trên mỗi tham số cao hơn rất nhiều so với chỉ lưu trọng số.

Suy luận LLM còn thêm KV cache, tăng theo độ dài context và concurrency.

## Đồ thị tính toán

Việc thực thi neural network có thể được xem như một graph các phép toán tensor. Runtime hoặc framework cố gắng fuse, lên lịch và ánh xạ các phép toán này thành kernel phần cứng phù hợp.

Tối ưu ở cấp graph đôi khi quan trọng ngang kiến trúc mô hình.

## Kernel

Kernel là implementation mức thấp của một phép toán trên accelerator. Một attention kernel được tối ưu có thể giảm lượng truy cập bộ nhớ dù kết quả toán học tương đương implementation ngây thơ.

Điều này giải thích vì sao cùng kiến trúc Transformer nhưng tốc độ runtime có thể khác rất lớn.

## Phân cấp Bộ nhớ

Dữ liệu có thể nằm ở:

```text
register / cache
on-chip SRAM / shared memory
HBM / VRAM
RAM của host
NVMe / storage
network / object storage
```

Càng xa đơn vị tính toán thì độ trễ thường cao hơn và băng thông thấp hơn. AI hiệu năng cao cố giữ và tái sử dụng dữ liệu ở tầng gần compute nhất có thể.

## Giao tiếp

Một thiết bị đơn lẻ bị giới hạn bởi dung lượng. Huấn luyện hoặc suy luận phân tán cần truyền tensor hoặc gradient giữa nhiều thiết bị.

Nếu thời gian giao tiếp lớn hơn lượng compute tiết kiệm được nhờ chia tải, thêm GPU sẽ không còn scale tốt.

## Hiệu quả mở rộng

Nếu 1 GPU mất `T1`, lý tưởng N GPU sẽ mất `T1/N`. Thực tế:

\[
Efficiency=\frac{T_1}{NT_N}
\]

Hiệu quả nhỏ hơn 1 do giao tiếp, đồng bộ, mất cân bằng tải và overhead.

## Trực giác từ Amdahl's Law

Nếu một phần công việc mang tính tuần tự và không thể song song hóa, tổng speedup sẽ bị giới hạn. Dù 99% compute chạy song song, 1% nút thắt tuần tự vẫn tạo trần hiệu năng.

## Mức sử dụng tài nguyên

Một chỉ số GPU utilization duy nhất chưa đủ. Thiết bị có thể trông “bận” nhưng đang chạy kernel kém hiệu quả hoặc bị dừng chờ bộ nhớ.

Cần profile:

- mức sử dụng compute;
- băng thông bộ nhớ;
- mức lấp đầy kernel (kernel occupancy);
- giao tiếp;
- khoảng thời gian rỗi.

## Kinh tế học của Token Huấn luyện

Chi phí pretraining quy mô lớn xấp xỉ phụ thuộc:

```text
kích thước mô hình × số token huấn luyện × số phép toán/token
```

Nhưng hiệu quả dữ liệu, kiến trúc và optimizer quyết định cùng một lượng compute tạo ra bao nhiêu chất lượng.

## Kinh tế học của Suy luận

Chi phí serving phụ thuộc độ dài prompt, độ dài output, batch/concurrency, KV cache và cách đặt mô hình trên phần cứng.

Decode tự hồi quy khiến suy luận LLM khác image classifier: hệ thống phải chạy nhiều bước token nối tiếp nhau.

## Kiến trúc có nhận thức về Compute

Kiến trúc không độc lập với phần cứng. CNN tận dụng kernel convolution dày đặc. Transformer scale tốt trên accelerator cho ma trận và huấn luyện song song. Mixture-of-Experts giảm active compute trên mỗi token nhưng tăng độ phức tạp của routing và giao tiếp.

## Mô hình Roofline

Hiệu năng bị giới hạn bởi compute peak hoặc băng thông bộ nhớ. Nếu phép toán đang memory-bound, tăng peak FLOPs sẽ không giúp nhiều nếu băng thông không đổi.

## Profile trước khi tối ưu

Không nên đoán bottleneck. Cần profile end-to-end và ở cấp kernel trước khi quyết định quantize, shard hoặc viết lại.

## Mô hình tư duy

```text
Tính toán AI = số học bị ràng buộc bởi di chuyển dữ liệu, dung lượng bộ nhớ và giao tiếp
```

## Những nhầm lẫn thường gặp

### “GPU nhanh hơn CPU vì clock cao hơn”

Không. GPU mạnh ở khả năng xử lý song song quy mô lớn, không đơn giản vì clock.

### “Peak TFLOPS quyết định mô hình chạy nhanh”

Không. Bộ nhớ, giao tiếp và hiệu quả kernel có thể mới là nút thắt.

### “Thêm GPU luôn scale tuyến tính”

Không. Overhead phân tán làm hiệu quả mở rộng giảm.

## Liên kết kiến thức

Xem [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [Numerical Computation](../01_mathematical_foundations/07_numerical_computation.md), [AI Engineering](../15_ai_engineering/README.md) và các chapter tiếp theo về accelerator, bộ nhớ, tính toán song song và hệ thống phân tán.