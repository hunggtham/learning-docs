# Theo dõi Thí nghiệm và Khả năng Tái lập

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Experiment tracking và reproducibility**. Route đi từ code/data/config snapshot → metrics/artifacts → run lineage → deterministic versus statistical repeatability → promotion evidence, để kết quả có thể được truy nguyên và tái kiểm.

Quá trình phát triển Machine học tập (learning / 학습) là quá trình thử nhiều giả thuyết: họ mô hình (model family), đặc trưng (feature), tốc độ học (learning rate), snapshot dữ liệu, augmentation, prompt, chunking, retriever hoặc chính sách đánh giá. Nếu thí nghiệm không được theo dõi có cấu trúc, nhóm rất nhanh rơi vào tình trạng “mô hình tốt nhất là tệp (file / 파일) nào?” hoặc “vì sao chỉ số tháng trước cao hơn?”.

**Theo dõi thí nghiệm (experiment tracking / 실험 추적)** tạo một dấu vết kiểm toán (audit trail) cho mỗi lần chạy.

## Một thí nghiệm cần lưu gì?

Ít nhất:

```text
run ID
commit SHA của mã nguồn
phiên bản / truy vấn / snapshot dữ liệu
phiên bản đặc trưng hoặc tiền xử lý
kiến trúc mô hình
siêu tham số
random seed
môi trường / dependency
phần cứng
thời gian huấn luyện
chỉ số
artifact
ghi chú / người phụ trách
```

Với ứng dụng LLM còn cần:

```text
mô hình nền / phiên bản API
system prompt
prompt template
mô hình embedding
cấu hình retriever / reranker
cấu hình chunking
schema của tool
graph của agent
phiên bản bộ đánh giá
```

> **Chuyển mạch:** Trong **Theo dõi Thí nghiệm và Khả năng Tái lập**, **Khả năng tái lập không đồng nghĩa tính xác định từng bit** tiếp nhận điểm tựa từ **Một thí nghiệm cần lưu gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Experiment, Trial và Run** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khả năng tái lập không đồng nghĩa tính xác định từng bit

Kernel phân tán, phần cứng và thứ tự phép toán số có thể tạo tính không xác định. Mục tiêu thực dụng là **khả năng tái lập khoa học (scientific reproducibility)**: có đủ đầu vào và cấu hình để chạy lại và giải thích vì sao kết quả khác.

Nếu cần mức tái lập nghiêm ngặt hơn, có thể:

- cố định seed;
- dùng toán tử xác định khi có thể;
- cố định phiên bản phụ thuộc (dependency / 의존성);
- ghi lại ảnh bộ chứa (container image / 컨테이너 이미지);
- phiên bản (version / 버전) hóa dữ liệu;
- ghi lại phần cứng và thời gian chạy (runtime / 런타임).

> **Chuyển mạch:** Ở chặng này của **Theo dõi Thí nghiệm và Khả năng Tái lập**, **Experiment, Trial và Run** tiếp nhận điểm tựa từ **Khả năng tái lập không đồng nghĩa tính xác định từng bit** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ghi lại chỉ số** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Experiment, Trial và Run

Có thể phân biệt:

```text
Experiment = câu hỏi hoặc giả thuyết
Trial      = một cấu hình được thử
Run        = một lần thực thi cụ thể
```

Ví dụ, thí nghiệm là “dropout có giảm overfit không?”, trial là dropout 0.0/0.1/0.2, và mỗi trial có thể có nhiều run để ước lượng phương sai.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Theo dõi Thí nghiệm và Khả năng Tái lập**, **Ghi lại chỉ số** tiếp nhận điểm tựa từ **Experiment, Trial và Run** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Theo dõi sản phẩm tạo ra (artifact / 산출물)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ghi lại chỉ số

Không nên chỉ lưu chỉ số cuối cùng. Đường cong học (learning curve) cho biết động lực của quá trình tối ưu:

```text
train loss theo step
validation loss
learning rate
throughput
GPU memory
```

Hai mô hình có chỉ số cuối giống nhau nhưng một mô hình huấn luyện không ổn định có rủi ro vận hành khác.

> **Chuyển mạch:** Trong **Theo dõi Thí nghiệm và Khả năng Tái lập**, **Theo dõi sản phẩm tạo ra (artifact / 산출물)** tiếp nhận điểm tựa từ **Ghi lại chỉ số** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Baseline và khả năng so sánh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Theo dõi sản phẩm tạo ra (artifact / 산출물)

Sản phẩm tạo ra (artifact / 산출물) gồm checkpoint, tokenizer, ma trận nhầm lẫn (confusion matrix), báo cáo đánh giá, đầu ra (output / 출력) mẫu và biểu đồ calibration.

Sản phẩm tạo ra (artifact / 산출물) phải gắn với siêu dữ liệu (metadata / 메타데이터) của run thay vì bị lưu rời rạc trong một thư mục dùng chung.

> **Chuyển mạch:** Ở chặng này của **Theo dõi Thí nghiệm và Khả năng Tái lập**, **Theo dõi sản phẩm tạo ra (artifact / 산출물)** đã nêu tiêu chí phân biệt, còn **Baseline và khả năng so sánh** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Bất định thống kê** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Baseline và khả năng so sánh

Thí nghiệm chỉ có ý nghĩa khi điều kiện có thể so sánh. Nếu tập dữ liệu hoặc cách chia dữ liệu thay đổi, chênh lệch chỉ số không thể được quy đơn giản cho thay đổi kiến trúc.

Nên lưu run đường cơ sở (baseline) và so sánh trên cùng một phiên bản đánh giá.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Theo dõi Thí nghiệm và Khả năng Tái lập**, **Baseline và khả năng so sánh** đã nêu tiêu chí phân biệt, còn **Bất định thống kê** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Tìm kiếm siêu tham số** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bất định thống kê

Khác biệt nhỏ có thể chỉ là nhiễu. Với huấn luyện ngẫu nhiên, nên dùng nhiều seed hoặc khoảng tin cậy (confidence interval) khi quyết định quan trọng.

Không nên thăng cấp mô hình chỉ vì tăng 0.1% chỉ số từ một run duy nhất.

> **Chuyển mạch:** Trong **Theo dõi Thí nghiệm và Khả năng Tái lập**, **Tìm kiếm siêu tham số** tiếp nhận điểm tựa từ **Bất định thống kê** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thí nghiệm Prompt cho LLM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tìm kiếm siêu tham số

Grid tìm kiếm (search / 검색), random tìm kiếm (search / 검색) hoặc Bayesian tối ưu hóa (optimization / 최적화) tạo nhiều run. Hệ thống theo dõi cần nhóm các run theo study và lưu không gian tìm kiếm (search space).

Điều chỉnh dựa trên kiểm thử (test / 테스트) set lặp đi lặp lại sẽ biến kiểm thử (test / 테스트) set thành kiểm tra hợp lệ (validation / 검증) set không chính thức.

> **Chuyển mạch:** Ở chặng này của **Theo dõi Thí nghiệm và Khả năng Tái lập**, **Thí nghiệm Prompt cho LLM** tiếp nhận điểm tựa từ **Tìm kiếm siêu tham số** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đánh giá của con người** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thí nghiệm Prompt cho LLM

Thí nghiệm prompt có nhiều biến ẩn:

- phiên bản mô hình (model / 모델)/provider;
- temperature;
- thứ tự ngữ cảnh (context / 맥락);
- công cụ (tool / 도구) được phép dùng;
- trạng thái của retrieval corpus.

Nếu không phiên bản (version / 버전) hóa các yếu tố này thì kết luận “prompt A tốt hơn prompt B” rất khó tái lập.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Theo dõi Thí nghiệm và Khả năng Tái lập**, **Đánh giá của con người** tiếp nhận điểm tựa từ **Thí nghiệm Prompt cho LLM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Từ Notebook sang chuỗi xử lý (pipeline / 파이프라인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đánh giá của con người

Đánh giá của con người cần rubric, ID hoặc nhóm người đánh giá, độ đồng thuận giữa người đánh giá và các mẫu cụ thể. Chỉ lưu điểm trung bình sẽ làm mất ngữ cảnh quan trọng.

> **Chuyển mạch:** Trong **Theo dõi Thí nghiệm và Khả năng Tái lập**, **Đánh giá của con người** xác định đầu vào; **Từ Notebook sang chuỗi xử lý (pipeline / 파이프라인)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Anti-Pattern: đặt tên thủ công** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ Notebook sang chuỗi xử lý (pipeline / 파이프라인)

Notebook vẫn hữu ích cho khám phá, nhưng thí nghiệm thắng nên được chuyển thành chuỗi xử lý (pipeline / 파이프라인) bằng script và có phiên bản (version / 버전) trước khi lên môi trường vận hành (production / 운영 환경).

> **Chuyển mạch:** Ở chặng này của **Theo dõi Thí nghiệm và Khả năng Tái lập**, **Từ Notebook sang chuỗi xử lý (pipeline / 파이프라인)** xác định đầu vào; **Anti-Pattern: đặt tên thủ công** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Anti-Pattern: đặt tên thủ công

Tên tệp (file / 파일) kiểu:

```text
model_final_v2_really_final.pt
```

không phải chiến lược versioning. Danh tính của sản phẩm tạo ra (artifact / 산출물) nên dựa trên run ID/phiên bản (version / 버전) và siêu dữ liệu (metadata / 메타데이터) trong registry.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Theo dõi Thí nghiệm và Khả năng Tái lập**, **Mô hình tư duy** gom các mảnh từ **Anti-Pattern: đặt tên thủ công** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Theo dõi thí nghiệm = sổ tay khoa học tự động của hệ thống ML
```

Nó trả lời: ta đã thử gì, với dữ liệu/mã nguồn nào, kết quả ra sao và sản phẩm tạo ra (artifact / 산출물) nào được sinh ra.

> **Chuyển mạch:** Trong **Theo dõi Thí nghiệm và Khả năng Tái lập**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Chỉ cần lưu mô hình (model / 모델) checkpoint”

Không. Không thể giải thích checkpoint nếu thiếu dữ liệu, cấu hình và mã nguồn tương ứng.

### “Cố định seed là đủ để tái lập”

Không. Môi trường, thứ tự dữ liệu và kernel phần cứng cũng ảnh hưởng.

### “Chỉ số cao hơn nghĩa giả thuyết đúng”

Không nhất thiết. Cần kiểm soát yếu tố gây nhiễu (confounder) và bất định.

> **Chuyển mạch:** Ở chặng này của **Theo dõi Thí nghiệm và Khả năng Tái lập**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Data and Model Versioning](./02_data_and_model_versioning.md), [Model Registry](./03_model_registry.md), [Evaluation](../18_evaluation_reliability_interpretability/README.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
