# Pruning và kiến thức (knowledge / 지식) Distillation

> **Mạch đọc:** Đặt **Pruning và kiến thức (knowledge / 지식) Distillation** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Pruning** sang **Unstructured Pruning**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


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

## Sparsity

Nếu 70% weights bằng 0 thì sparsity bằng 70%. Tuy nhiên mức tiết kiệm lưu trữ (storage / 저장소) và thời gian chạy (runtime / 런타임) phụ thuộc sparse format và kernel hỗ trợ (support / 지원).

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

Pruning quá mạnh có thể phá những năng lực (capability / 역량) hiếm nhưng quan trọng.

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

## Temperature

Softmax với temperature `T`:

\[
p_i=\frac{e^{z_i/T}}{\sum_j e^{z_j/T}}
\]

Khi `T>1`, phân phối (distribution / 분포) trở nên mềm hơn, giúp student học cả relative preference giữa các lớp (class / 클래스) hoặc đơn vị từ (token / 토큰) thay vì chỉ học argmax.

## Phản hồi (response / 응답) Distillation và tính năng (feature / 기능) Distillation

**phản hồi (response / 응답) distillation** khớp final đầu ra (output / 출력) hoặc logits.

**tính năng (feature / 기능) distillation** khớp hidden biểu diễn (representation / 표현) hoặc attention mẫu (pattern / 패턴).

Tính năng (feature / 기능) distillation có thể truyền nhiều tín hiệu (signal / 신호) hơn nhưng thường yêu cầu kiến trúc (architecture / 아키텍처) tương thích hoặc có ánh xạ (mapping / 매핑) giữa teacher và student.

## Distillation cho LLM

Teacher LLM có thể sinh demonstration, rationale hoặc preference dữ liệu (data / 데이터) để huấn luyện student nhỏ hơn.

Nhưng synthetic teacher dữ liệu (data / 데이터) có các rủi ro:

- lỗi của teacher được sao chép;
- đầu ra (output / 출력) diversity thấp;
- ràng buộc pháp lý hoặc provenance;
- student overfit vào style của teacher.

Distillation không tự tạo ra sự thật.

## Sequence-Level Distillation

Trong generation, teacher sinh chuỗi (sequence / 시퀀스) mục tiêu (target / 대상) rồi student được supervised huấn luyện (training / 학습) trên chuỗi (sequence / 시퀀스) đó.

Cách này thực dụng nhưng làm mất phần bất định (uncertainty / 불확실성) phân phối (distribution / 분포) ở token-level nếu chỉ giữ một đầu ra (output / 출력) duy nhất.

## Distillation và Fine-Tuning khác nhau thế nào?

Fine-tuning điều chỉnh một mô hình cho tác vụ (task / 작업) hoặc lĩnh vực (domain / 도메인) mới. Distillation truyền hành vi từ một mô hình khác sang student, thường để student nhỏ hơn hoặc chuyên biệt hơn.

Hai kỹ thuật có thể kết hợp.

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

## Bảo toàn năng lực (capability / 역량)

Average benchmark không đủ. Cần năng lực (capability / 역량) suite bao gồm rare lớp (class / 클래스), long-tail đầu vào (input / 입력), calibration, robustness và an toàn (safety / 안전) hành vi (behavior / 동작).

## Khi nào Pruning phù hợp?

Pruning phù hợp khi mô hình overparameterized và thời gian chạy (runtime / 런타임) có sparse hoặc structured-kernel hỗ trợ (support / 지원). Distillation phù hợp khi có teacher mạnh nhưng triển khai (deployment / 배포) ngân sách (budget / 예산) nhỏ.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Pruning      → loại bỏ capacity ít cần thiết
Distillation → huấn luyện mô hình nhỏ bắt chước hành vi hữu ích của mô hình lớn
```

## Những nhầm lẫn thường gặp

### “Weight gần 0 luôn không quan trọng”

Không. Importance phụ thuộc tương tác giữa các parameter; magnitude chỉ là heuristic.

### “Student luôn đạt chất lượng ngang teacher”

Không. sức chứa (capacity / 용량) của student, độ phủ của dữ liệu và mục tiêu (objective / 목표) giới hạn mức transfer.

### “Distillation là bản sao (copy / 복사) kiến thức (knowledge / 지식) hoàn hảo”

Không. Student học hành vi trên distillation phân phối (distribution / 분포), không sao chép toàn bộ nội bộ (internal / 내부) kiến thức (knowledge / 지식) và năng lực (capability / 역량) của teacher.

## Liên kết kiến thức

Xem [Quantization](./06_quantization.md), [Model Compression](./08_model_compression.md), [Information Theory](../01_mathematical_foundations/05_information_theory.md) và [Supervised Fine-Tuning](../08_large_language_models/07_supervised_fine_tuning.md).
