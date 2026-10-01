# Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Đầu vào (input / 입력) phải bất biến** xác định điều kiện hoặc ranh giới mà các cơ chế sau phải tôn trọng; sau đó sang **Cấu hình** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Để huấn luyện mô hình có khả năng tái lập, chỉ gọi `model.fit()` là chưa đủ. **chuỗi xử lý (pipeline / 파이프라인) huấn luyện (training pipeline / 학습 파이프라인)** điều phối snapshot dữ liệu, tiền xử lý, cấu hình, phân tán (distributed / 분산) job, checkpoint, đánh giá và đăng ký sản phẩm tạo ra (artifact / 산출물).

```text
dữ liệu đã version hóa
→ kiểm tra
→ biến đổi
→ huấn luyện
→ checkpoint
→ đánh giá
→ đóng gói artifact
→ đăng ký
```

## Đầu vào (input / 입력) phải bất biến

Một huấn luyện (training / 학습) run nên trỏ tới dataset/phiên bản (version / 버전) chính xác, không nên dùng một tệp (file / 파일) mutable kiểu `latest.csv`. đầu vào (input / 입력) thay đổi làm mất khả năng tái lập.

Cần ghi lại:

```text
data manifest / hash
commit của feature code
label schema
model config
seed
runtime image
```

> **Chuyển mạch:** Trong **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Cấu hình** tiếp nhận điểm tựa từ **Đầu vào (input / 입력) phải bất biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiểm tra dữ liệu trước khi dùng compute đắt tiền** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấu hình

Nên tách cấu hình khỏi mã (code / 코드):

```text
learning_rate
batch_size
architecture
optimizer
data paths
augmentation
precision
checkpoint interval
```

Bản thân cấu hình (config / 설정) cũng phải được phiên bản (version / 버전) hóa và lưu cùng huấn luyện (training / 학습) run.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Cấu hình** nêu điều cần giải thích; **Kiểm tra dữ liệu trước khi dùng compute đắt tiền** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Shuffling và Sampling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểm tra dữ liệu trước khi dùng compute đắt tiền

Trước khi cấp GPU, cần kiểm tra lược đồ (schema / 스키마), số lượng mẫu, null, phân phối lớp (class / 클래스), các leakage gate và tính toàn vẹn của tệp (file / 파일). Phát hiện lỗi sớm giúp tiết kiệm chi phí lớn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Kiểm tra dữ liệu trước khi dùng compute đắt tiền** nêu điều cần giải thích; **Shuffling và Sampling** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Tính xác định** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Shuffling và Sampling

Phân tán (distributed / 분산) huấn luyện (training / 학습) cần chia shard và lấy mẫu đúng cách, đồng thời đủ ổn định để có thể tái lập ở mức hợp lý. Class-balanced sampler thay đổi phân phối huấn luyện (training / 학습) thực tế nên phải được ghi lại rõ ràng.

> **Chuyển mạch:** Trong **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Tính xác định** tiếp nhận điểm tựa từ **Shuffling và Sampling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Checkpoint** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính xác định

Khả năng tái lập hoàn toàn trên GPU có thể khó do kernel không xác định và parallel reduction. Cần phân biệt:

- tái lập được cấu hình;
- tái lập được kết quả theo nghĩa thống kê;
- kết quả bitwise giống hệt.

Không nên hứa bitwise equality nếu toàn bộ ngăn xếp (stack / 스택) không hỗ trợ.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Checkpoint** tiếp nhận điểm tựa từ **Tính xác định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tần suất Checkpoint** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Checkpoint

Checkpoint thường lưu:

```text
model weights
optimizer state
scheduler state
step / epoch
random states khi cần
mixed-precision scaler
```

Chỉ lưu weights là không đủ để resume huấn luyện (training / 학습) giống trước, vì momentum và trạng thái (state / 상태) của optimizer đã mất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Tần suất Checkpoint** tiếp nhận điểm tựa từ **Checkpoint** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiểm tra hợp lệ (validation / 검증) trong quá trình huấn luyện (training / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tần suất Checkpoint

Checkpoint quá thưa làm mất nhiều công sức khi job lỗi. Checkpoint quá dày làm tăng overhead về lưu trữ (storage / 저장소) và I/O.

Chu kỳ checkpoint nên dựa trên chi phí của job và xác suất thất bại (failure / 실패).

> **Chuyển mạch:** Trong **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Kiểm tra hợp lệ (validation / 검증) trong quá trình huấn luyện (training / 학습)** tiếp nhận điểm tựa từ **Tần suất Checkpoint** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Early Stopping** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểm tra hợp lệ (validation / 검증) trong quá trình huấn luyện (training / 학습)

Kiểm tra hợp lệ (validation / 검증) định kỳ giúp phát hiện overfitting hoặc divergence. Nhưng kiểm tra hợp lệ (validation / 검증) set lớn cũng có thể trở thành chi phí đáng kể; có thể dùng subset đại diện cho kiểm tra thường xuyên và chạy full evaluation tại các milestone.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Early Stopping** tiếp nhận điểm tựa từ **Kiểm tra hợp lệ (validation / 검증) trong quá trình huấn luyện (training / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mixed Precision** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Early Stopping

Dừng huấn luyện nếu kiểm tra hợp lệ (validation / 검증) chỉ số (metric / 지표) không cải thiện sau một khoảng đủ dài. Cần có `patience` để tránh phản ứng quá mức với nhiễu.

Với foundation mô hình (model / 모델), pretraining thường được lập kế hoạch theo compute/đơn vị từ (token / 토큰) ngân sách (budget / 예산) thay vì kiểm tra hợp lệ (validation / 검증) theo epoch kiểu truyền thống.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Mixed Precision** tiếp nhận điểm tựa từ **Early Stopping** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ dốc (gradient / 기울기) Accumulation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mixed Precision

FP16/BF16 giúp giảm bộ nhớ (memory / 메모리) và tăng thông lượng (throughput / 처리량) trên accelerator. Một số phép toán nhạy số vẫn có thể cần precision cao hơn.

FP16 thường dùng **mất mát (loss / 손실) scaling** để tránh độ dốc (gradient / 기울기) underflow; BF16 có exponent phạm vi (range / 범위) lớn hơn nên giảm nhu cầu này.

> **Chuyển mạch:** Trong **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Độ dốc (gradient / 기울기) Accumulation** tiếp nhận điểm tựa từ **Mixed Precision** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân tán (distributed / 분산) dữ liệu (data / 데이터) Parallel** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ dốc (gradient / 기울기) Accumulation

Nếu batch mong muốn không vừa bộ nhớ (memory / 메모리), có thể cộng dồn độ dốc (gradient / 기울기) qua nhiều microbatch:

```text
zero grad
for k microbatches:
    forward / backward(loss / k)
optimizer step
```

Effective batch tăng mà không cần giữ toàn bộ activation cùng lúc, nhưng độ trễ (latency / 지연 시간) cho mỗi optimizer step cũng tăng.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Độ dốc (gradient / 기울기) Accumulation** nêu điều cần giải thích; **Phân tán (distributed / 분산) dữ liệu (data / 데이터) Parallel** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Hyperparameter tìm kiếm (search / 검색)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân tán (distributed / 분산) dữ liệu (data / 데이터) Parallel

Với **phân tán (distributed / 분산) dữ liệu (data / 데이터) Parallel (DDP)**, mô hình được replicate trên nhiều thiết bị (device / 장치), mỗi thiết bị (device / 장치) xử lý một shard khác nhau rồi đồng bộ độ dốc (gradient / 기울기) bằng all-reduce.

Communication overhead tăng theo số parameter. Các phần sharding và mô hình (model / 모델) parallelism được giải thích sâu hơn ở tầng (layer / 계층) hạ tầng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Phân tán (distributed / 분산) dữ liệu (data / 데이터) Parallel** nêu điều cần giải thích; **Hyperparameter tìm kiếm (search / 검색)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Đóng gói sản phẩm tạo ra (artifact / 산출물)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hyperparameter tìm kiếm (search / 검색)

Grid tìm kiếm (search / 검색), random tìm kiếm (search / 검색) hoặc Bayesian tối ưu hóa (optimization / 최적화) có thể tạo rất nhiều huấn luyện (training / 학습) run. Vì vậy cần experiment tracking và ngân sách (budget / 예산) điều khiển (control / 제어).

Kiểm thử (test / 테스트) set không được biến thành mục tiêu (objective / 목표) của hyperparameter tìm kiếm (search / 검색).

> **Chuyển mạch:** Trong **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Đóng gói sản phẩm tạo ra (artifact / 산출물)** tiếp nhận điểm tựa từ **Hyperparameter tìm kiếm (search / 검색)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bàn giao sang mô hình (model / 모델) Registry** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đóng gói sản phẩm tạo ra (artifact / 산출물)

Huấn luyện (training / 학습) thành công nên tạo ra bundle có thể triển khai:

```text
weights
tokenizer / preprocessor
model config
label map
signature / input schema
metrics
provenance
```

> **Chuyển mạch:** Ở chặng này của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Bàn giao sang mô hình (model / 모델) Registry** tiếp nhận điểm tựa từ **Đóng gói sản phẩm tạo ra (artifact / 산출물)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phục hồi khi lỗi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bàn giao sang mô hình (model / 모델) Registry

Chỉ những mô hình vượt qua evaluation và cổng chất lượng (quality gate / 품질 게이트) mới nên được đưa vào mô hình (model / 모델) registry để xem xét triển khai (deployment / 배포). “huấn luyện (training / 학습) đã chạy xong” không đồng nghĩa “được phép chạy môi trường vận hành (production / 운영 환경)”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Phục hồi khi lỗi** tiếp nhận điểm tựa từ **Bàn giao sang mô hình (model / 모델) Registry** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bottleneck ở dữ liệu (data / 데이터) Loader** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phục hồi khi lỗi

Chuỗi xử lý (pipeline / 파이프라인) nên có khả năng resume từ checkpoint nhất quán gần nhất. Điều này đặc biệt quan trọng khi dùng spot hoặc preemptible instance.

> **Chuyển mạch:** Trong **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Phục hồi khi lỗi** nêu điều cần giải thích; **Bottleneck ở dữ liệu (data / 데이터) Loader** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Huấn luyện (training / 학습) thông lượng (throughput / 처리량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bottleneck ở dữ liệu (data / 데이터) Loader

GPU có thể bị idle nếu CPU decoding, augmentation hoặc lưu trữ (storage / 저장소) quá chậm. Cần theo dõi accelerator utilization và thời gian chờ dữ liệu.

Các cách cải thiện gồm:

- prefetch;
- nhiều worker song song;
- định dạng dữ liệu hiệu quả;
- cục bộ (local / 로컬)/bộ nhớ đệm (cache / 캐시) lưu trữ (storage / 저장소);
- GPU augmentation khi phù hợp.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Bottleneck ở dữ liệu (data / 데이터) Loader** nêu điều cần giải thích; **Huấn luyện (training / 학습) thông lượng (throughput / 처리량)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Siêu dữ liệu (metadata / 메타데이터) của Experiment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Huấn luyện (training / 학습) thông lượng (throughput / 처리량)

Các chỉ số (metric / 지표) phổ biến:

```text
samples / sec
tokens / sec
```

Tuy nhiên thông lượng (throughput / 처리량) cao nhất chưa chắc giúp hội tụ nhanh nhất nếu batch kích thước (size / 크기) hoặc optimizer làm giảm mẫu (sample / 표본) efficiency.

**Time-to-quality** thường có ý nghĩa hơn raw hardware utilization.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Huấn luyện (training / 학습) thông lượng (throughput / 처리량)** nêu điều cần giải thích; **Siêu dữ liệu (metadata / 메타데이터) của Experiment** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Pretraining chuỗi xử lý (pipeline / 파이프라인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Siêu dữ liệu (metadata / 메타데이터) của Experiment

Mỗi run nên trả lời được:

- thay đổi gì?
- dữ liệu (data / 데이터) phiên bản (version / 버전) nào?
- mã (code / 코드)/cấu hình (config / 설정) nào?
- chỉ số (metric / 지표) nào?
- sản phẩm tạo ra (artifact / 산출물) nào?
- cơ sở (base / 기반) mô hình (model / 모델) hoặc parent nào?
- tốn bao nhiêu compute và chi phí?

> **Chuyển mạch:** Trong **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Siêu dữ liệu (metadata / 메타데이터) của Experiment** nêu điều cần giải thích; **Pretraining chuỗi xử lý (pipeline / 파이프라인)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Fine-Tuning chuỗi xử lý (pipeline / 파이프라인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pretraining chuỗi xử lý (pipeline / 파이프라인)

Foundation-model pretraining thường bổ sung:

```text
hỗn hợp dữ liệu rất lớn
streaming shard
dedup / filter
checkpoint ở quy mô lớn
distributed optimizer
fault recovery
đánh giá dài hạn
```

Ở quy mô này, một shard bị lỗi hoặc một nút (node / 노드) chết không được phép làm dừng toàn bộ job.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Pretraining chuỗi xử lý (pipeline / 파이프라인)** xác định đầu vào; **Fine-Tuning chuỗi xử lý (pipeline / 파이프라인)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Bảo mật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fine-Tuning chuỗi xử lý (pipeline / 파이프라인)

Chuỗi xử lý (pipeline / 파이프라인) SFT/LoRA cần ghi rõ base-model phiên bản (version / 버전), adapter cấu hình (config / 설정), prompt/template và tokenizer. Chat template không tương thích có thể gây regression lớn khi serving.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Fine-Tuning chuỗi xử lý (pipeline / 파이프라인)** xác định đầu vào; **Bảo mật** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảo mật

Huấn luyện (training / 학습) job thường truy cập dataset lớn và cloud lưu trữ (storage / 저장소) nhạy cảm. Nên dùng credential có phạm vi (scope / 범위) tối thiểu, worker cô lập và tránh đưa secret trực tiếp vào cấu hình (config / 설정) hoặc checkpoint.

> **Chuyển mạch:** Trong **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Mô hình tư duy** gom các mảnh từ **Bảo mật** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> **huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인) biến một thí nghiệm tối ưu hóa mang tính nghiên cứu thành quy trình sản xuất sản phẩm tạo ra (artifact / 산출물) mô hình có thể tái lập.**

> **Chuyển mạch:** Ở chặng này của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Checkpoint chỉ là weights”

Không. Để resume chính xác còn cần trạng thái (state / 상태) của optimizer, scheduler và các trạng thái (state / 상태) liên quan khác.

### “Cùng seed thì kết quả chắc chắn giống hệt”

Không. phân tán (distributed / 분산) GPU thao tác (operation / 연산) vẫn có thể không xác định.

### “GPU utilization cao nghĩa là chuỗi xử lý (pipeline / 파이프라인) tối ưu”

Không. Time-to-quality và cost-to-quality quan trọng hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인)**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Huấn luyện (training / 학습) chuỗi xử lý (pipeline / 파이프라인) là cầu nối giữa [Data Governance](../14_data_for_ai/08_data_governance.md) và vòng đời experiment/mô hình (model / 모델) trong MLOps.

Xem tiếp: [Inference Pipeline](./02_inference_pipeline.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
