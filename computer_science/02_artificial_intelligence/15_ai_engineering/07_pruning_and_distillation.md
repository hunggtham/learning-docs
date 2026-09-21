# Pruning và Knowledge Distillation

**Cắt tỉa (pruning / 가지치기)** và **chưng cất tri thức (knowledge distillation / 지식 증류)** đều nhằm tạo mô hình hiệu quả hơn, nhưng cơ chế khác nhau. Pruning loại bỏ một phần structure hoặc weights của mô hình hiện có. Distillation huấn luyện một **mô hình học viên (student)** học hành vi từ **mô hình giáo viên (teacher)**.

## Pruning

Neural network thường có mức dư thừa (redundancy) đáng kể. Nếu một nhóm parameter đóng góp ít, ta có thể loại bỏ chúng để giảm compute hoặc memory.

### Unstructured Pruning

Đặt từng weight riêng lẻ về 0 dựa trên magnitude hoặc một tiêu chí khác.

```text
|w| nhỏ → prune
```

Ưu điểm: có thể đạt sparsity cao.

Nhược điểm: sparse pattern không đều, hardware phổ thông có thể không tận dụng tốt. Vì vậy số non-zero parameter giảm mạnh nhưng latency không nhất thiết giảm tương ứng.

### Structured Pruning

Loại bỏ toàn bộ channel, attention head, neuron hoặc block.

Shape sau khi pruning vẫn có cấu trúc đều nên dễ map lên dense hardware hơn.

Ví dụ: cắt một số attention head hoặc giảm dimension của MLP.

## Sparsity

Nếu 70% weights bằng 0 thì sparsity bằng 70%. Tuy nhiên mức tiết kiệm storage và runtime phụ thuộc sparse format và kernel support.

Sparsity không đồng nghĩa speedup.

## Prune rồi Fine-Tune

Một workflow phổ biến:

```text
mô hình đã train
→ ước lượng importance
→ prune
→ fine-tune để phục hồi
→ evaluate
```

Pruning quá mạnh có thể phá những capability hiếm nhưng quan trọng.

## Knowledge Distillation

Distribution của teacher chứa nhiều thông tin hơn một hard label đơn lẻ.

Teacher tạo xác suất:

\[
p_T(y|x)
\]

Student tối ưu để tiến gần teacher:

\[
L=\alpha L_{task}+(1-\alpha)L_{distill}
\]

`L_distill` thường dùng KL divergence hoặc cross-entropy giữa các distribution đã được làm mềm.

## Temperature

Softmax với temperature `T`:

\[
p_i=\frac{e^{z_i/T}}{\sum_j e^{z_j/T}}
\]

Khi `T>1`, distribution trở nên mềm hơn, giúp student học cả relative preference giữa các class hoặc token thay vì chỉ học argmax.

## Response Distillation và Feature Distillation

**Response distillation** khớp final output hoặc logits.

**Feature distillation** khớp hidden representation hoặc attention pattern.

Feature distillation có thể truyền nhiều signal hơn nhưng thường yêu cầu architecture tương thích hoặc có mapping giữa teacher và student.

## Distillation cho LLM

Teacher LLM có thể sinh demonstration, rationale hoặc preference data để huấn luyện student nhỏ hơn.

Nhưng synthetic teacher data có các rủi ro:

- lỗi của teacher được sao chép;
- output diversity thấp;
- ràng buộc pháp lý hoặc provenance;
- student overfit vào style của teacher.

Distillation không tự tạo ra sự thật.

## Sequence-Level Distillation

Trong generation, teacher sinh sequence target rồi student được supervised training trên sequence đó.

Cách này thực dụng nhưng làm mất phần uncertainty distribution ở token-level nếu chỉ giữ một output duy nhất.

## Distillation và Fine-Tuning khác nhau thế nào?

Fine-tuning điều chỉnh một mô hình cho task hoặc domain mới. Distillation truyền hành vi từ một mô hình khác sang student, thường để student nhỏ hơn hoặc chuyên biệt hơn.

Hai kỹ thuật có thể kết hợp.

## Kết hợp Pruning và Distillation

Một deployment pipeline có thể là:

```text
large teacher
→ distill student nhỏ hơn
→ structured prune
→ quantize
→ deploy
```

Tuy nhiên các bước compression có thể tương tác với nhau; cần evaluate sau từng bước và cả end-to-end.

## Bảo toàn Capability

Average benchmark không đủ. Cần capability suite bao gồm rare class, long-tail input, calibration, robustness và safety behavior.

## Khi nào Pruning phù hợp?

Pruning phù hợp khi mô hình overparameterized và runtime có sparse hoặc structured-kernel support. Distillation phù hợp khi có teacher mạnh nhưng deployment budget nhỏ.

## Mô hình tư duy

```text
Pruning      → loại bỏ capacity ít cần thiết
Distillation → huấn luyện mô hình nhỏ bắt chước hành vi hữu ích của mô hình lớn
```

## Những nhầm lẫn thường gặp

### “Weight gần 0 luôn không quan trọng”

Không. Importance phụ thuộc tương tác giữa các parameter; magnitude chỉ là heuristic.

### “Student luôn đạt chất lượng ngang teacher”

Không. Capacity của student, độ phủ của dữ liệu và objective giới hạn mức transfer.

### “Distillation là copy knowledge hoàn hảo”

Không. Student học hành vi trên distillation distribution, không sao chép toàn bộ internal knowledge và capability của teacher.

## Liên kết kiến thức

Xem [Quantization](./06_quantization.md), [Model Compression](./08_model_compression.md), [Information Theory](../01_mathematical_foundations/05_information_theory.md) và [Supervised Fine-Tuning](../08_large_language_models/07_supervised_fine_tuning.md).