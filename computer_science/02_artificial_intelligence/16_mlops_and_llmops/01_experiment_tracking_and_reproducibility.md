# Theo dõi Thí nghiệm và Khả năng Tái lập

> **Mạch đọc:** Đặt **Theo dõi Thí nghiệm và Khả năng Tái lập** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Một thí nghiệm cần lưu gì?** sang **Khả năng tái lập không đồng nghĩa tính xác định từng bit**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


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

## Khả năng tái lập không đồng nghĩa tính xác định từng bit

Kernel phân tán, phần cứng và thứ tự phép toán số có thể tạo tính không xác định. Mục tiêu thực dụng là **khả năng tái lập khoa học (scientific reproducibility)**: có đủ đầu vào và cấu hình để chạy lại và giải thích vì sao kết quả khác.

Nếu cần mức tái lập nghiêm ngặt hơn, có thể:

- cố định seed;
- dùng toán tử xác định khi có thể;
- cố định phiên bản phụ thuộc (dependency / 의존성);
- ghi lại ảnh bộ chứa (container image / 컨테이너 이미지);
- phiên bản (version / 버전) hóa dữ liệu;
- ghi lại phần cứng và thời gian chạy (runtime / 런타임).

## Experiment, Trial và Run

Có thể phân biệt:

```text
Experiment = câu hỏi hoặc giả thuyết
Trial      = một cấu hình được thử
Run        = một lần thực thi cụ thể
```

Ví dụ, thí nghiệm là “dropout có giảm overfit không?”, trial là dropout 0.0/0.1/0.2, và mỗi trial có thể có nhiều run để ước lượng phương sai.

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

## Theo dõi sản phẩm tạo ra (artifact / 산출물)

Sản phẩm tạo ra (artifact / 산출물) gồm checkpoint, tokenizer, ma trận nhầm lẫn (confusion matrix), báo cáo đánh giá, đầu ra (output / 출력) mẫu và biểu đồ calibration.

Sản phẩm tạo ra (artifact / 산출물) phải gắn với siêu dữ liệu (metadata / 메타데이터) của run thay vì bị lưu rời rạc trong một thư mục dùng chung.

## Baseline và khả năng so sánh

Thí nghiệm chỉ có ý nghĩa khi điều kiện có thể so sánh. Nếu tập dữ liệu hoặc cách chia dữ liệu thay đổi, chênh lệch chỉ số không thể được quy đơn giản cho thay đổi kiến trúc.

Nên lưu run đường cơ sở (baseline) và so sánh trên cùng một phiên bản đánh giá.

## Bất định thống kê

Khác biệt nhỏ có thể chỉ là nhiễu. Với huấn luyện ngẫu nhiên, nên dùng nhiều seed hoặc khoảng tin cậy (confidence interval) khi quyết định quan trọng.

Không nên thăng cấp mô hình chỉ vì tăng 0.1% chỉ số từ một run duy nhất.

## Tìm kiếm siêu tham số

Grid tìm kiếm (search / 검색), random tìm kiếm (search / 검색) hoặc Bayesian tối ưu hóa (optimization / 최적화) tạo nhiều run. Hệ thống theo dõi cần nhóm các run theo study và lưu không gian tìm kiếm (search space).

Điều chỉnh dựa trên kiểm thử (test / 테스트) set lặp đi lặp lại sẽ biến kiểm thử (test / 테스트) set thành kiểm tra hợp lệ (validation / 검증) set không chính thức.

## Thí nghiệm Prompt cho LLM

Thí nghiệm prompt có nhiều biến ẩn:

- phiên bản mô hình (model / 모델)/provider;
- temperature;
- thứ tự ngữ cảnh (context / 맥락);
- công cụ (tool / 도구) được phép dùng;
- trạng thái của retrieval corpus.

Nếu không phiên bản (version / 버전) hóa các yếu tố này thì kết luận “prompt A tốt hơn prompt B” rất khó tái lập.

## Đánh giá của con người

Đánh giá của con người cần rubric, ID hoặc nhóm người đánh giá, độ đồng thuận giữa người đánh giá và các mẫu cụ thể. Chỉ lưu điểm trung bình sẽ làm mất ngữ cảnh quan trọng.

## Từ Notebook sang chuỗi xử lý (pipeline / 파이프라인)

Notebook vẫn hữu ích cho khám phá, nhưng thí nghiệm thắng nên được chuyển thành chuỗi xử lý (pipeline / 파이프라인) bằng script và có phiên bản (version / 버전) trước khi lên môi trường vận hành (production / 운영 환경).

## Anti-Pattern: đặt tên thủ công

Tên tệp (file / 파일) kiểu:

```text
model_final_v2_really_final.pt
```

không phải chiến lược versioning. Danh tính của sản phẩm tạo ra (artifact / 산출물) nên dựa trên run ID/phiên bản (version / 버전) và siêu dữ liệu (metadata / 메타데이터) trong registry.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Theo dõi thí nghiệm = sổ tay khoa học tự động của hệ thống ML
```

Nó trả lời: ta đã thử gì, với dữ liệu/mã nguồn nào, kết quả ra sao và sản phẩm tạo ra (artifact / 산출물) nào được sinh ra.

## Những nhầm lẫn thường gặp

### “Chỉ cần lưu mô hình (model / 모델) checkpoint”

Không. Không thể giải thích checkpoint nếu thiếu dữ liệu, cấu hình và mã nguồn tương ứng.

### “Cố định seed là đủ để tái lập”

Không. Môi trường, thứ tự dữ liệu và kernel phần cứng cũng ảnh hưởng.

### “Chỉ số cao hơn nghĩa giả thuyết đúng”

Không nhất thiết. Cần kiểm soát yếu tố gây nhiễu (confounder) và bất định.

## Liên kết kiến thức

Xem [Data and Model Versioning](./02_data_and_model_versioning.md), [Model Registry](./03_model_registry.md), [Evaluation](../18_evaluation_reliability_interpretability/README.md).
