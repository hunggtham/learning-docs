# Tinh chỉnh có giám sát (SFT)

**Tinh chỉnh có giám sát (Supervised Fine-Tuning — SFT / 지도 미세조정)** là giai đoạn tiếp tục huấn luyện một mô hình đã tiền huấn luyện trên tập ví dụ có input và đầu ra mong muốn rõ ràng. Với mô hình chat, một sample có thể gồm system message, yêu cầu của user và phản hồi assistant chuẩn.

Nếu pretraining học phân bố rộng của ngôn ngữ, SFT tập trung gradient vào **phân bố hành vi mong muốn**.

## Hàm mục tiêu

Về mặt toán học, SFT thường vẫn dùng cross-entropy dự đoán token tiếp theo trên phần phản hồi mục tiêu:

\[
\mathcal L_{SFT}=-\sum_{t\in response}\log P_\theta(y_t\mid x,y_{<t})
\]

`x` là chỉ dẫn/context, còn `y` là câu trả lời mong muốn.

Nhiều pipeline **che loss (loss masking)** trên token của user/system và chỉ tối ưu token của assistant. Như vậy mô hình không bị huấn luyện để “dự đoán lại user” mà tập trung bắt chước hành vi phản hồi.

## SFT khác pretraining ở đâu?

Cơ chế optimizer và backpropagation có thể giống nhau, nhưng **phân bố dữ liệu và tín hiệu giám sát** khác.

Pretraining:

```text
corpus thô → dự đoán token tiếp theo ở mọi vị trí phù hợp
```

SFT:

```text
instruction / context → bắt chước phản hồi đã tuyển chọn
```

Vì vậy SFT gần với **bắt chước hành vi (behavior cloning)** hơn so với language modeling thô.

## Chất lượng dữ liệu quyết định chất lượng hành vi

Một dataset SFT nhỏ nhưng được tuyển chọn tốt có thể thay đổi hành vi mạnh vì mô hình đã có năng lực nền. Ngược lại, nếu phản hồi mục tiêu dài dòng, né tránh, quá tự tin hoặc không nhất quán, mô hình cũng học những pattern đó.

Dữ liệu SFT cần bao phủ nhiều chiều:

- độ chính xác;
- mức tuân thủ chỉ dẫn;
- phong cách và độ sâu;
- hành vi từ chối;
- định dạng gọi công cụ;
- bao phủ đa ngôn ngữ;
- xử lý yêu cầu mơ hồ.

## Loss masking và template hội thoại

Chat template quyết định token nào biểu diễn ranh giới vai trò. Nếu template khi huấn luyện và serving không khớp, hành vi mô hình có thể giảm dù trọng số không đổi.

Ví dụ mô hình được huấn luyện với token đặc biệt:

```text
<|system|> ...
<|user|> ...
<|assistant|> ...
```

nhưng inference lại dùng format khác, mô hình có thể không nhận ra ngữ nghĩa vai trò giống lúc huấn luyện.

## Full fine-tuning và tinh chỉnh tiết kiệm tham số

**Tinh chỉnh toàn bộ (full fine-tuning)** cập nhật gần như toàn bộ trọng số. Cách này linh hoạt nhưng tốn memory/compute và có nguy cơ catastrophic forgetting.

**Tinh chỉnh tiết kiệm tham số (Parameter-Efficient Fine-Tuning — PEFT)** chỉ huấn luyện một tập con tham số hoặc adapter. LoRA là ví dụ nổi tiếng:

\[
W' = W + BA
\]

với rank nhỏ `r`, nhờ đó số tham số cần huấn luyện giảm mạnh.

LoRA không “nén toàn bộ mô hình”; nó học một **cập nhật hạng thấp (low-rank update)** cho một số ma trận được chọn.

## Tinh chỉnh theo miền

Nếu tác vụ cần thuật ngữ, format và phong cách phản hồi đặc thù, SFT theo domain có thể rất hữu ích. Ví dụ trợ lý hỗ trợ tài chính cần định dạng phản hồi, tone và logic escalation ổn định.

Tuy nhiên fact thay đổi thường xuyên vẫn nên đến từ database hoặc RAG nếu độ mới và provenance quan trọng.

## Chương trình học và mixture dữ liệu

Dataset SFT thường là hỗn hợp general instruction, domain task, safety data và tool use. Trọng số mỗi nguồn ảnh hưởng gradient.

Nếu ví dụ safety quá nhiều và quá đơn giản, mô hình có thể từ chối quá mức. Nếu dữ liệu domain chi phối, năng lực tổng quát có thể giảm.

## Loss chỉ trên phản hồi

Trong chat SFT, cách làm phổ biến là tính loss chỉ trên phản hồi assistant. Điều này tránh huấn luyện mô hình tái tạo văn bản người dùng.

Tuy nhiên system prompt vẫn ảnh hưởng trạng thái ẩn vì nó nằm trong context dù không trực tiếp chịu loss.

## Sequence packing

Nhiều sample SFT ngắn có thể được đóng gói vào cùng sequence để tăng mức sử dụng GPU. Attention mask và loss mask phải bảo đảm các sample không rò context sang nhau ngoài semantics đã thiết kế.

## Overfitting trong SFT

Dataset SFT thường nhỏ hơn corpus pretraining rất nhiều. Mô hình lớn có thể nhanh chóng ghi nhớ format hoặc câu trả lời cụ thể.

Validation nên theo dõi:

```text
training loss
validation loss
behavior evaluation
khả năng khái quát ra ngoài template đã thấy
```

Loss SFT thấp không đồng nghĩa trợ lý tốt.

## SFT và trace lập luận

Dataset có thể chứa rationale hoặc lời giải từng bước. Mô hình có thể học pattern giải từng bước, nhưng chất lượng phụ thuộc độ đúng của trace.

Nếu trace trông hợp lý nhưng sai, mô hình cũng có thể bắt chước. Phản hồi dài hơn không tự động nghĩa là reasoning tốt hơn.

## Distillation bằng SFT

Teacher model mạnh có thể sinh phản hồi, sau đó student được huấn luyện bằng SFT. Đây là một dạng **chưng cất tri thức (knowledge distillation)** ở cấp hành vi.

Student học phân bố đầu ra của teacher nhưng không nhất thiết sao chép cơ chế nội bộ.

## SFT cho sử dụng công cụ

Để mô hình gọi tool, dataset có thể chứa:

```text
yêu cầu người dùng
→ JSON gọi công cụ
→ kết quả công cụ
→ câu trả lời cuối
```

SFT giúp mô hình học cú pháp và pattern quyết định. Production vẫn cần validation schema, quyền truy cập và xử lý lỗi runtime.

## SFT và calibration

SFT có thể làm câu trả lời trông tự tin hơn mà không cải thiện calibration về độ đúng tương ứng. Do đó tối ưu phong cách “tự tin và hữu ích” có thể làm overconfidence nặng hơn.

Đánh giá cần tách phong cách khỏi tính đúng.

## Mô hình tư duy

> SFT là **bắt chước hành vi dựa trên năng lực đã học từ pretraining**.

Nó không thay thế tiền huấn luyện, retrieval hay verification ở runtime.

## Những hiểu lầm thường gặp

### “SFT huấn luyện mô hình từ đầu cho tác vụ”

Không. Với LLM, SFT thường là một giai đoạn hậu huấn luyện tương đối nhỏ trên mô hình đã pretrain.

### “LoRA luôn cho kết quả giống full fine-tuning”

Không. Hiệu quả phụ thuộc rank, target module, dữ liệu và mức thay đổi hành vi cần thiết.

### “Dataset SFT càng lớn càng tốt”

Ví dụ xấu hoặc không nhất quán có thể làm hành vi tệ đi. Chất lượng và độ bao phủ quan trọng hơn số lượng thô.

## Liên kết kiến thức

SFT là cầu nối giữa [Instruction Tuning](./06_instruction_tuning.md) và preference optimization. Khi có nhiều câu trả lời chấp nhận được, bắt chước một target duy nhất không đủ để biểu diễn thứ tự ưu tiên. Đây là lý do RLHF và DPO xuất hiện.

Xem tiếp: [RLHF](./08_rlhf.md).