# Nền tảng Tính toán cho Trí tuệ Nhân tạo

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Nền tảng Tính toán cho Trí tuệ Nhân tạo**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Năng lực tính toán không chỉ là FLOPs** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Huấn luyện và Suy luận** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

AI hiện đại tồn tại ở giao điểm giữa thuật toán và tính toán vật lý. Một mô hình có thể đúng về mặt toán học nhưng không thực tế nếu bộ nhớ không đủ, băng thông quá thấp hoặc giao tiếp giữa các thiết bị chiếm phần lớn thời gian. Vì vậy hiểu **tính toán AI (AI compute / AI 연산)** giúp nối Đại số tuyến tính, Deep học tập (learning / 학습) và môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링) với phần cứng thực tế.

## Năng lực tính toán không chỉ là FLOPs

Một tải công việc (workload / 워크로드) AI tiêu tốn:

```text
phép toán số học
dung lượng bộ nhớ
băng thông bộ nhớ
giao tiếp giữa thiết bị
I/O lưu trữ
I/O mạng
năng lượng
```

Hai mô hình có FLOPs gần nhau vẫn có thời gian chạy (runtime / 런타임) rất khác nếu mẫu (pattern / 패턴) truy cập bộ nhớ hoặc cách song song hóa khác.

> **Chuyển mạch:** Trong **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Huấn luyện và Suy luận** tiếp nhận điểm tựa từ **Năng lực tính toán không chỉ là FLOPs** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cường độ số học** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Huấn luyện và Suy luận

Huấn luyện cần:

```text
forward pass
backward pass
gradient
trạng thái optimizer
lưu activation
```

Suy luận chủ yếu chạy forward pass, nhưng quá trình sinh nội dung của LLM còn cần KV bộ nhớ đệm (cache / 캐시) và decode tự hồi quy.

Huấn luyện thường tốn compute và bộ nhớ nhiều hơn trên mỗi đơn vị từ (token / 토큰); serving lại nhạy hơn với độ trễ, tính đồng thời (concurrency / 동시성) và khả năng giữ dữ liệu trong bộ nhớ.

> **Chuyển mạch:** Ở chặng này của **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Cường độ số học** tiếp nhận điểm tựa từ **Huấn luyện và Suy luận** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **FLOPs và FLOP/s** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cường độ số học

Một kernel có **cường độ số học (arithmetic intensity)** cao nếu thực hiện nhiều phép toán trên mỗi byte dữ liệu được tải. Phép nhân ma trận thường tận dụng accelerator tốt vì cùng dữ liệu được tái sử dụng nhiều lần.

Phép toán có ít tính toán nhưng phải di chuyển nhiều dữ liệu thường bị **giới hạn bởi bộ nhớ (memory-bound)**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **FLOPs và FLOP/s** tiếp nhận điểm tựa từ **Cường độ số học** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Precision** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## FLOPs và FLOP/s

FLOPs là số lượng phép toán dấu chấm động. FLOP/s là tốc độ phần cứng thực hiện các phép toán đó.

Peak FLOP/s lý thuyết không đồng nghĩa thông lượng (throughput / 처리량) thực tế. Hiệu năng thật còn phụ thuộc mức sử dụng tài nguyên, precision, hình dạng kernel, bộ nhớ và giao tiếp.

> **Chuyển mạch:** Trong **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Precision** tiếp nhận điểm tựa từ **FLOPs và FLOP/s** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dung lượng bộ nhớ cần thiết** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Precision thấp hơn giúp giảm bộ nhớ/băng thông và có thể tăng thông lượng (throughput / 처리량) của accelerator, nhưng độ ổn định số và chất lượng phải được kiểm soát.

> **Chuyển mạch:** Ở chặng này của **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Dung lượng bộ nhớ cần thiết** tiếp nhận điểm tựa từ **Precision** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đồ thị tính toán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Suy luận LLM còn thêm KV bộ nhớ đệm (cache / 캐시), tăng theo độ dài ngữ cảnh (context / 맥락) và tính đồng thời (concurrency / 동시성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Đồ thị tính toán** tiếp nhận điểm tựa từ **Dung lượng bộ nhớ cần thiết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kernel** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đồ thị tính toán

Việc thực thi neural mạng (network / 네트워크) có thể được xem như một đồ thị (graph / 그래프) các phép toán tensor. thời gian chạy (runtime / 런타임) hoặc khung phần mềm (framework / 프레임워크) cố gắng fuse, lên lịch và ánh xạ các phép toán này thành kernel phần cứng phù hợp.

Tối ưu ở cấp đồ thị (graph / 그래프) đôi khi quan trọng ngang kiến trúc mô hình.

> **Chuyển mạch:** Trong **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Kernel** tiếp nhận điểm tựa từ **Đồ thị tính toán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân cấp Bộ nhớ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kernel

Kernel là hiện thực (implementation / 구현) mức thấp của một phép toán trên accelerator. Một attention kernel được tối ưu có thể giảm lượng truy cập bộ nhớ dù kết quả toán học tương đương hiện thực (implementation / 구현) ngây thơ.

Điều này giải thích vì sao cùng kiến trúc Transformer nhưng tốc độ thời gian chạy (runtime / 런타임) có thể khác rất lớn.

> **Chuyển mạch:** Ở chặng này của **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Phân cấp Bộ nhớ** tiếp nhận điểm tựa từ **Kernel** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Giao tiếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Giao tiếp** tiếp nhận điểm tựa từ **Phân cấp Bộ nhớ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hiệu quả mở rộng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Giao tiếp

Một thiết bị đơn lẻ bị giới hạn bởi dung lượng. Huấn luyện hoặc suy luận phân tán cần truyền tensor hoặc độ dốc (gradient / 기울기) giữa nhiều thiết bị.

Nếu thời gian giao tiếp lớn hơn lượng compute tiết kiệm được nhờ chia tải, thêm GPU sẽ không còn quy mô (scale / 규모) tốt.

> **Chuyển mạch:** Trong **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Hiệu quả mở rộng** tiếp nhận điểm tựa từ **Giao tiếp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trực giác từ Amdahl's Law** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hiệu quả mở rộng

Nếu 1 GPU mất `T1`, lý tưởng N GPU sẽ mất `T1/N`. Thực tế:

\[
Efficiency=\frac{T_1}{NT_N}
\]

Hiệu quả nhỏ hơn 1 do giao tiếp, đồng bộ, mất cân bằng tải và overhead.

> **Chuyển mạch:** Ở chặng này của **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Trực giác từ Amdahl's Law** tiếp nhận điểm tựa từ **Hiệu quả mở rộng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mức sử dụng tài nguyên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trực giác từ Amdahl's Law

Nếu một phần công việc mang tính tuần tự và không thể song song hóa, tổng speedup sẽ bị giới hạn. Dù 99% compute chạy song song, 1% nút thắt tuần tự vẫn tạo trần hiệu năng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Mức sử dụng tài nguyên** tiếp nhận điểm tựa từ **Trực giác từ Amdahl's Law** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kinh tế học của đơn vị từ (token / 토큰) Huấn luyện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mức sử dụng tài nguyên

Một chỉ số GPU utilization duy nhất chưa đủ. Thiết bị có thể trông “bận” nhưng đang chạy kernel kém hiệu quả hoặc bị dừng chờ bộ nhớ.

Cần profile:

- mức sử dụng compute;
- băng thông bộ nhớ;
- mức lấp đầy kernel (kernel occupancy);
- giao tiếp;
- khoảng thời gian rỗi.

> **Chuyển mạch:** Trong **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Kinh tế học của đơn vị từ (token / 토큰) Huấn luyện** tiếp nhận điểm tựa từ **Mức sử dụng tài nguyên** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kinh tế học của Suy luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kinh tế học của đơn vị từ (token / 토큰) Huấn luyện

Chi phí pretraining quy mô lớn xấp xỉ phụ thuộc:

```text
kích thước mô hình × số token huấn luyện × số phép toán/token
```

Nhưng hiệu quả dữ liệu, kiến trúc và optimizer quyết định cùng một lượng compute tạo ra bao nhiêu chất lượng.

> **Chuyển mạch:** Ở chặng này của **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Kinh tế học của Suy luận** tiếp nhận điểm tựa từ **Kinh tế học của đơn vị từ (token / 토큰) Huấn luyện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiến trúc có nhận thức về Compute** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kinh tế học của Suy luận

Chi phí serving phụ thuộc độ dài prompt, độ dài đầu ra (output / 출력), batch/tính đồng thời (concurrency / 동시성), KV bộ nhớ đệm (cache / 캐시) và cách đặt mô hình trên phần cứng.

Decode tự hồi quy khiến suy luận LLM khác ảnh (image / 이미지) classifier: hệ thống phải chạy nhiều bước đơn vị từ (token / 토큰) nối tiếp nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Kiến trúc có nhận thức về Compute** tiếp nhận điểm tựa từ **Kinh tế học của Suy luận** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình Roofline** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiến trúc có nhận thức về Compute

Kiến trúc không độc lập với phần cứng. CNN tận dụng kernel convolution dày đặc. Transformer quy mô (scale / 규모) tốt trên accelerator cho ma trận và huấn luyện song song. Mixture-of-Experts giảm active compute trên mỗi đơn vị từ (token / 토큰) nhưng tăng độ phức tạp của routing và giao tiếp.

> **Chuyển mạch:** Trong **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Mô hình Roofline** tiếp nhận điểm tựa từ **Kiến trúc có nhận thức về Compute** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Profile trước khi tối ưu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình Roofline

Hiệu năng bị giới hạn bởi compute peak hoặc băng thông bộ nhớ. Nếu phép toán đang memory-bound, tăng peak FLOPs sẽ không giúp nhiều nếu băng thông không đổi.

> **Chuyển mạch:** Ở chặng này của **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Profile trước khi tối ưu** tiếp nhận điểm tựa từ **Mô hình Roofline** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Profile trước khi tối ưu

Không nên đoán bottleneck. Cần profile end-to-end và ở cấp kernel trước khi quyết định quantize, shard hoặc viết lại.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Mô hình tư duy** gom các mảnh từ **Profile trước khi tối ưu** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Tính toán AI = số học bị ràng buộc bởi di chuyển dữ liệu, dung lượng bộ nhớ và giao tiếp
```

> **Chuyển mạch:** Trong **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “GPU nhanh hơn CPU vì clock cao hơn”

Không. GPU mạnh ở khả năng xử lý song song quy mô lớn, không đơn giản vì clock.

### “Peak TFLOPS quyết định mô hình chạy nhanh”

Không. Bộ nhớ, giao tiếp và hiệu quả kernel có thể mới là nút thắt.

### “Thêm GPU luôn quy mô (scale / 규모) tuyến tính”

Không. Overhead phân tán làm hiệu quả mở rộng giảm.

> **Chuyển mạch:** Ở chặng này của **Nền tảng Tính toán cho Trí tuệ Nhân tạo**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [Numerical Computation](../01_mathematical_foundations/07_numerical_computation.md), [AI Engineering](../15_ai_engineering/README.md) và các chapter tiếp theo về accelerator, bộ nhớ, tính toán song song và hệ thống phân tán.

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
