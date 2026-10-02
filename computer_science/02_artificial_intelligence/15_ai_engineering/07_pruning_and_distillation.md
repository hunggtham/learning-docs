# Pruning và kiến thức (knowledge / 지식) Distillation

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Pruning và knowledge distillation**. Route đi từ redundant parameters → structured/unstructured pruning → teacher logits/features → student training → hardware sparsity and quality checks, để compression nối model change với runtime gain.

**Cắt tỉa (pruning / 가지치기)** và **chưng cất tri thức (knowledge distillation / 지식 증류)** đều nhằm tạo mô hình hiệu quả hơn, nhưng cơ chế khác nhau. Pruning loại bỏ một phần cấu trúc (structure / 구조) hoặc weights của mô hình hiện có. Distillation huấn luyện một **mô hình học viên (student)** học hành vi từ **mô hình giáo viên (teacher)**.

## Pruning

Neural mạng (network / 네트워크) thường có mức dư thừa (redundancy) đáng kể. Nếu một nhóm parameter đóng góp ít, ta có thể loại bỏ chúng để giảm compute hoặc bộ nhớ (memory / 메모리).

### Unstructured Pruning

Đặt từng weight riêng lẻ về 0 dựa trên magnitude hoặc một tiêu chí khác.

```text
|w| nhỏ → prune
```

Ưu điểm: có thể đạt sparsity cao.

Nhược điểm: sparse mẫu (pattern / 패턴) không đều, hardware phổ thông có thể không tận dụng tốt. Vì vậy số non-zero parameter giảm mạnh nhưng độ trễ (latency / 지연 시간) không nhất thiết giảm tương ứng.

### Structured Pruning

Loại bỏ toàn bộ channel, attention head, neuron hoặc khối (block / 블록).

Shape sau khi pruning vẫn có cấu trúc đều nên dễ map lên dense hardware hơn.

Ví dụ: cắt một số attention head hoặc giảm dimension của MLP.

> **Chuyển mạch:** Trong **Pruning và kiến thức (knowledge / 지식) Distillation**, **Sparsity** tiếp nhận điểm tựa từ **Pruning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Prune rồi Fine-Tune** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sparsity

Nếu 70% weights bằng 0 thì sparsity bằng 70%. Tuy nhiên mức tiết kiệm lưu trữ (storage / 저장소) và thời gian chạy (runtime / 런타임) phụ thuộc sparse format và kernel hỗ trợ (support / 지원).

Sparsity không đồng nghĩa speedup.

> **Chuyển mạch:** Ở chặng này của **Pruning và kiến thức (knowledge / 지식) Distillation**, **Prune rồi Fine-Tune** tiếp nhận điểm tựa từ **Sparsity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiến thức (knowledge / 지식) Distillation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Prune rồi Fine-Tune

Một workflow phổ biến:

```text
mô hình đã train
→ ước lượng importance
→ prune
→ fine-tune để phục hồi
→ evaluate
```

Pruning quá mạnh có thể phá những năng lực (capability / 역량) hiếm nhưng quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Pruning và kiến thức (knowledge / 지식) Distillation**, **Kiến thức (knowledge / 지식) Distillation** tiếp nhận điểm tựa từ **Prune rồi Fine-Tune** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Temperature** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiến thức (knowledge / 지식) Distillation

Phân phối (distribution / 분포) của teacher chứa nhiều thông tin hơn một hard label đơn lẻ.

Teacher tạo xác suất:

\[
p_T(y|x)
\]

Student tối ưu để tiến gần teacher:

\[
L=\alpha L_{tác vụ (task / 작업)}+(1-\alpha)L_{distill}
\]

`L_distill` thường dùng KL divergence hoặc cross-entropy giữa các phân phối (distribution / 분포) đã được làm mềm.

> **Chuyển mạch:** Trong **Pruning và kiến thức (knowledge / 지식) Distillation**, **Temperature** tiếp nhận điểm tựa từ **Kiến thức (knowledge / 지식) Distillation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phản hồi (response / 응답) Distillation và tính năng (feature / 기능) Distillation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Temperature

Softmax với temperature `T`:

\[
p_i=\frac{e^{z_i/T}}{\sum_j e^{z_j/T}}
\]

Khi `T>1`, phân phối (distribution / 분포) trở nên mềm hơn, giúp student học cả relative preference giữa các lớp (class / 클래스) hoặc đơn vị từ (token / 토큰) thay vì chỉ học argmax.

> **Chuyển mạch:** Ở chặng này của **Pruning và kiến thức (knowledge / 지식) Distillation**, **Phản hồi (response / 응답) Distillation và tính năng (feature / 기능) Distillation** tiếp nhận điểm tựa từ **Temperature** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Distillation cho LLM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phản hồi (response / 응답) Distillation và tính năng (feature / 기능) Distillation

**phản hồi (response / 응답) distillation** khớp final đầu ra (output / 출력) hoặc logits.

**tính năng (feature / 기능) distillation** khớp hidden biểu diễn (representation / 표현) hoặc attention mẫu (pattern / 패턴).

Tính năng (feature / 기능) distillation có thể truyền nhiều tín hiệu (signal / 신호) hơn nhưng thường yêu cầu kiến trúc (architecture / 아키텍처) tương thích hoặc có ánh xạ (mapping / 매핑) giữa teacher và student.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Pruning và kiến thức (knowledge / 지식) Distillation**, **Distillation cho LLM** tiếp nhận điểm tựa từ **Phản hồi (response / 응답) Distillation và tính năng (feature / 기능) Distillation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sequence-Level Distillation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Distillation cho LLM

Teacher LLM có thể sinh demonstration, rationale hoặc preference dữ liệu (data / 데이터) để huấn luyện student nhỏ hơn.

Nhưng synthetic teacher dữ liệu (data / 데이터) có các rủi ro:

- lỗi của teacher được sao chép;
- đầu ra (output / 출력) diversity thấp;
- ràng buộc pháp lý hoặc provenance;
- student overfit vào style của teacher.

Distillation không tự tạo ra sự thật.

> **Chuyển mạch:** Trong **Pruning và kiến thức (knowledge / 지식) Distillation**, **Sequence-Level Distillation** tiếp nhận điểm tựa từ **Distillation cho LLM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Distillation và Fine-Tuning khác nhau thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sequence-Level Distillation

Trong generation, teacher sinh chuỗi (sequence / 시퀀스) mục tiêu (target / 대상) rồi student được supervised huấn luyện (training / 학습) trên chuỗi (sequence / 시퀀스) đó.

Cách này thực dụng nhưng làm mất phần bất định (uncertainty / 불확실성) phân phối (distribution / 분포) ở token-level nếu chỉ giữ một đầu ra (output / 출력) duy nhất.

> **Chuyển mạch:** Ở chặng này của **Pruning và kiến thức (knowledge / 지식) Distillation**, **Distillation và Fine-Tuning khác nhau thế nào?** tiếp nhận điểm tựa từ **Sequence-Level Distillation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kết hợp Pruning và Distillation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Distillation và Fine-Tuning khác nhau thế nào?

Fine-tuning điều chỉnh một mô hình cho tác vụ (task / 작업) hoặc lĩnh vực (domain / 도메인) mới. Distillation truyền hành vi từ một mô hình khác sang student, thường để student nhỏ hơn hoặc chuyên biệt hơn.

Hai kỹ thuật có thể kết hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Pruning và kiến thức (knowledge / 지식) Distillation**, **Kết hợp Pruning và Distillation** tiếp nhận điểm tựa từ **Distillation và Fine-Tuning khác nhau thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bảo toàn năng lực (capability / 역량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kết hợp Pruning và Distillation

Một triển khai (deployment / 배포) chuỗi xử lý (pipeline / 파이프라인) có thể là:

```text
large teacher
→ distill student nhỏ hơn
→ structured prune
→ quantize
→ deploy
```

Tuy nhiên các bước compression có thể tương tác với nhau; cần evaluate sau từng bước và cả end-to-end.

> **Chuyển mạch:** Trong **Pruning và kiến thức (knowledge / 지식) Distillation**, **Bảo toàn năng lực (capability / 역량)** tiếp nhận điểm tựa từ **Kết hợp Pruning và Distillation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khi nào Pruning phù hợp?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảo toàn năng lực (capability / 역량)

Average benchmark không đủ. Cần năng lực (capability / 역량) suite bao gồm rare lớp (class / 클래스), long-tail đầu vào (input / 입력), calibration, robustness và an toàn (safety / 안전) hành vi (behavior / 동작).

> **Chuyển mạch:** Ở chặng này của **Pruning và kiến thức (knowledge / 지식) Distillation**, **Khi nào Pruning phù hợp?** tiếp nhận điểm tựa từ **Bảo toàn năng lực (capability / 역량)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khi nào Pruning phù hợp?

Pruning phù hợp khi mô hình overparameterized và thời gian chạy (runtime / 런타임) có sparse hoặc structured-kernel hỗ trợ (support / 지원). Distillation phù hợp khi có teacher mạnh nhưng triển khai (deployment / 배포) ngân sách (budget / 예산) nhỏ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Pruning và kiến thức (knowledge / 지식) Distillation**, **Mô hình tư duy** gom các mảnh từ **Khi nào Pruning phù hợp?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Pruning      → loại bỏ capacity ít cần thiết
Distillation → huấn luyện mô hình nhỏ bắt chước hành vi hữu ích của mô hình lớn
```

> **Chuyển mạch:** Trong **Pruning và kiến thức (knowledge / 지식) Distillation**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Weight gần 0 luôn không quan trọng”

Không. Importance phụ thuộc tương tác giữa các parameter; magnitude chỉ là heuristic.

### “Student luôn đạt chất lượng ngang teacher”

Không. sức chứa (capacity / 용량) của student, độ phủ của dữ liệu và mục tiêu (objective / 목표) giới hạn mức transfer.

### “Distillation là bản sao (copy / 복사) kiến thức (knowledge / 지식) hoàn hảo”

Không. Student học hành vi trên distillation phân phối (distribution / 분포), không sao chép toàn bộ nội bộ (internal / 내부) kiến thức (knowledge / 지식) và năng lực (capability / 역량) của teacher.

> **Chuyển mạch:** Ở chặng này của **Pruning và kiến thức (knowledge / 지식) Distillation**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Quantization](./06_quantization.md), [Model Compression](./08_model_compression.md), [Information Theory](../01_mathematical_foundations/05_information_theory.md) và [Supervised Fine-Tuning](../08_large_language_models/07_supervised_fine_tuning.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
