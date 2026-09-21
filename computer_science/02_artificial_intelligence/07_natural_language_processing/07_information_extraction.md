# Information Extraction: biến văn bản tự do thành cấu trúc có thể sử dụng

**Trích xuất thông tin (Information Extraction — IE / 정보 추출)** chuyển văn bản phi cấu trúc thành span, thực thể, quan hệ, sự kiện hoặc trường dữ liệu có cấu trúc. Đây là cầu nối trực tiếp giữa NLP với cơ sở dữ liệu, Knowledge Graph và quy trình nghiệp vụ.

Thay vì hỏi mơ hồ “mô hình có hiểu câu không?”, IE định nghĩa schema đầu ra rõ ràng: thực thể nào xuất hiện, thuộc loại gì, có quan hệ nào giữa chúng, sự kiện nào xảy ra và trường nào cần điền.

## Named Entity Recognition

**Nhận dạng thực thể có tên (Named Entity Recognition — NER)** gán loại cho các span:

```text
Shinhan Bank opened an office in Seoul.
[Shinhan Bank]ORG ... [Seoul]LOC
```

Gán nhãn token cổ điển thường dùng BIO:

```text
Shinhan B-ORG
Bank    I-ORG
opened  O
...
Seoul   B-LOC
```

Subword tokenization làm việc căn chỉnh nhãn phức tạp hơn. Vì vậy đánh giá nên ưu tiên cấp span/thực thể thay vì chỉ dùng accuracy trên token.

## Loại thực thể phụ thuộc Domain

NER tổng quát thường có PERSON, ORG, LOCATION.

Trong tài chính có thể cần ACCOUNT, PRODUCT, TRANSACTION, AMOUNT. Trong y tế có thể cần DISEASE, DRUG, DOSAGE.

Schema quyết định “trích xuất đúng” nghĩa là gì. Schema quá rộng mất giá trị sử dụng; quá chi tiết lại làm annotator khó thống nhất.

## Gán nhãn chuỗi

Transformer encoder tạo `h_i`; classifier dự đoán nhãn cho từng token.

Nếu dùng softmax độc lập theo token, mô hình có thể tạo chuỗi nhãn không hợp lệ như `I-PER` xuất hiện mà không có `B-PER`. **Conditional Random Field (CRF)** có thể mô hình hóa ràng buộc chuyển nhãn giữa các vị trí.

Encoder lớn hiện đại thường hoạt động tốt ngay cả khi không có CRF, nhưng structured decoding vẫn có ích trong một số bài toán nhỏ hoặc chuyên domain.

## Trích xuất quan hệ

Sau khi xác định thực thể, mô hình có thể dự đoán quan hệ giữa chúng:

```text
[Company A] acquired [Company B]
```

Schema có thể tạo cạnh `ACQUIRED` hoặc `ACQUIRED_BY` tùy hướng đã quy ước.

Các hướng triển khai gồm phân loại cặp thực thể bằng contextual representation, chấm điểm cặp span, trích xuất entity+relation đồng thời hoặc sinh structured output.

Hướng của quan hệ phải được định nghĩa rõ; đảo subject/object có thể tạo một fact hoàn toàn khác.

## Trích xuất sự kiện

Một sự kiện thường có **trigger** và các đối số có vai trò riêng.

Ví dụ:

```text
Samsung acquired X for $2B in 2025.
```

có thể được chuẩn hóa thành:

```json
{
  "type": "Acquisition",
  "buyer": "Samsung",
  "target": "X",
  "amount": "$2B",
  "date": "2025"
}
```

Event extraction vì vậy không chỉ nhận thực thể mà còn phải gán đúng vai trò và đôi khi cần ngữ cảnh xuyên nhiều câu.

## Coreference Resolution

```text
Alice joined Acme. She became CTO.
```

`She` tham chiếu tới Alice.

**Giải đồng tham chiếu (coreference resolution)** gom nhiều mention cùng chỉ một thực thể thành một cụm. Điều này đặc biệt quan trọng với trích xuất tri thức ở cấp tài liệu.

LLM có thể xử lý nhiều trường hợp nhờ context lớn, nhưng đánh giá coreference tường minh vẫn cần thiết nếu đây là yêu cầu hệ thống.

## Slot Filling

Tài liệu nghiệp vụ thường cần trích các trường cụ thể:

```text
invoice_number
seller
buyer
total_amount
due_date
```

Đây là dạng **điền trường (slot filling)** có ràng buộc. Với tài liệu scan, hệ thống có thể cần OCR, layout và NLP cùng lúc.

Trong production, schema đúng và validation thường quan trọng hơn khả năng tạo câu trả lời tự do.

## Trích xuất Extractive và Generative

Mô hình extractive chọn span trực tiếp từ nguồn, nhờ đó dễ grounding và giữ nguyên văn bản gốc.

Mô hình generative có thể tạo JSON hoặc giá trị đã chuẩn hóa linh hoạt hơn nhưng có nguy cơ sinh giá trị không có trong nguồn.

Một pipeline an toàn hơn cho dữ liệu quan trọng thường là:

```text
LLM đề xuất structured extraction
→ kiểm tra schema
→ đối chiếu evidence/span nguồn
→ áp dụng business rule xác định
→ human review nếu cần
```

## Entity Linking

NER có thể phát hiện mention `Apple`; **liên kết thực thể (entity linking)** ánh xạ mention đó tới thực thể chuẩn:

```text
Apple → Apple Inc. (company)
không phải apple (fruit)
```

Quá trình này thường gồm tạo candidate và phân giải mơ hồ dựa trên context hoặc knowledge base.

Canonical ID giúp fact được trích xuất có thể join với cơ sở dữ liệu hoặc Knowledge Graph.

## Chuẩn hóa giá trị

Chuỗi được trích thường cần chuyển thành dạng chuẩn:

```text
"Sep 20, 2026" → 2026-09-20
"₩1.2 million" → {currency: KRW, amount: 1200000}
```

Khi có thể, bước chuẩn hóa nên dùng logic xác định và vẫn giữ chuỗi gốc cùng provenance để kiểm tra lại.

## Bố cục tài liệu

Hợp đồng, hóa đơn và biểu mẫu mang ý nghĩa trong vị trí ô bảng, header và tọa độ. OCR thuần văn bản có thể làm mất quan hệ này.

Mô hình **layout-aware** kết hợp văn bản với bounding box hoặc đặc trưng hình ảnh. Document AI vì vậy thường là bài toán đa phương thức thay vì NLP thuần túy.

## Weak Supervision

Gán nhãn IE thủ công rất tốn chi phí. **Weak supervision** dùng rule, heuristic, knowledge base hoặc mô hình ngoài để tạo nhãn nhiễu ở quy mô lớn.

Huấn luyện phải tính đến label noise và vẫn cần một tập gold sạch để đánh giá thực sự.

## Distant Supervision

Nếu knowledge base có fact `(CompanyA, acquired, CompanyB)`, hệ thống có thể coi những câu chứa cả hai thực thể là ví dụ dương cho quan hệ mua lại.

Nhưng một câu chứa hai thực thể chưa chắc thật sự biểu đạt quan hệ đó. Distant supervision đánh đổi chi phí gán nhãn lấy nhiễu có hệ thống.

## Precision và Recall trong trích xuất

Nếu fact sau trích xuất được ghi tự động vào database, hệ thống thường cần precision cao. Nếu con người sẽ review toàn bộ candidate, recall cao có thể quan trọng hơn.

Ngưỡng và workflow phải phản ánh chi phí downstream chứ không chỉ tối ưu F1 chung.

## Đánh giá

Precision/Recall/F1 ở cấp entity span:

\[
Precision=\frac{correct\ predicted\ spans}{predicted\ spans}
\]

\[
Recall=\frac{correct\ predicted\ spans}{gold\ spans}
\]

Span chồng một phần có thể được phân tích riêng nhưng không nên tự động tính là exact match.

Đánh giá relation/event còn yêu cầu thực thể, loại, quan hệ và vai trò cùng đúng; lỗi ở bước trước có thể lan sang bước sau.

## Xây Knowledge Graph

Pipeline điển hình:

```text
Tài liệu
→ trích xuất thực thể
→ entity linking
→ trích xuất quan hệ / sự kiện
→ chuẩn hóa
→ gắn provenance
→ Knowledge Graph
```

Mỗi cạnh lý tưởng nên giữ nguồn bằng chứng, thời gian và mức tin cậy thay vì chỉ lưu triple trần.

## Structured Extraction bằng LLM

LLM cho phép few-shot extraction cho schema mới rất nhanh. Nhưng production đáng tin cậy cần thêm:

- constrained decoding theo JSON/schema;
- quy ước rõ cho null/unknown;
- evidence span hoặc trích dẫn nguồn;
- đánh giá theo từng field;
- phòng prompt injection trong tài liệu không tin cậy;
- validation xác định.

“JSON hợp lệ” chỉ chứng minh cú pháp đúng, không chứng minh dữ liệu trích xuất đúng.

## Mô hình tư duy

> Information Extraction biến ngôn ngữ thành các claim có kiểu và gắn chúng với bằng chứng nguồn. Provenance là một phần của dữ liệu, không phải metadata tùy chọn.

## Những hiểu lầm thường gặp

### “NER chỉ là tìm danh từ riêng”

Không. Schema có thể bao gồm ngày, số tiền, sản phẩm, bệnh, mã hợp đồng và nhiều loại khác.

### “LLM tạo field trông hợp lý nghĩa là extraction thành công”

Không. Giá trị có thể bị bịa; extraction cần đối chiếu nguồn.

### “Token accuracy đủ cho NER”

Không. Nhãn `O` thường chiếm đa số; entity-span F1 có ý nghĩa hơn.

### “Có thể xây Knowledge Graph bằng cách lưu mọi triple LLM trích ra”

Không. Còn cần entity resolution, thời gian, provenance, confidence và xử lý mâu thuẫn.

## Liên kết kiến thức

Information Extraction nối [Knowledge Graphs](../03_knowledge_and_reasoning/06_knowledge_graphs.md), [Transformer NLP](./06_transformer_nlp.md), Database/Data Engineering và các workflow RAG/Agent về sau.