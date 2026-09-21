# Lập luận trong mô hình ngôn ngữ lớn

Khi nói một LLM “lập luận (reasoning)”, cần tách hành vi quan sát được khỏi khẳng định về cơ chế bên trong. Ở góc nhìn engineering, **reasoning** có thể hiểu là khả năng biến một bài toán thành chuỗi biến đổi trung gian làm tăng khả năng tìm được đáp án đúng: phân rã, so sánh, suy diễn, kiểm chứng, tìm kiếm hoặc dùng công cụ.

Không cần giả định mô hình suy nghĩ giống con người để đánh giá năng lực này. Câu hỏi hữu ích hơn là: mô hình giải bài toán nhiều bước ổn định đến đâu, failure mode nào thường xuất hiện và tính toán bên ngoài có cải thiện độ tin cậy không?

## Trả lời trực tiếp và tính toán trung gian

Một prompt có thể yêu cầu mô hình trả lời ngay hoặc tạo các bước trung gian. Với tác vụ nhiều bước, việc dành thêm token cho quá trình giải có thể giúp vì mô hình có thêm vị trí để thực hiện tính toán tuần tự.

Mô hình tư duy:

```text
giải mã một bước
so với
cấp thêm token inference để biến đổi bài toán qua nhiều bước
```

Tuy nhiên văn bản reasoning dài không tự động đúng. Mô hình có thể tạo lời giải thích mạch lạc cho một đáp án sai.

## Phân rã bài toán

Bài toán phức tạp thường dễ xử lý hơn khi tách thành bài toán con:

```text
hiểu mục tiêu
→ trích xuất dữ kiện
→ giải bài toán con A
→ giải bài toán con B
→ kết hợp
→ kiểm chứng
```

Phân rã có thể giảm độ phức tạp tìm kiếm nếu các bài toán con được xác định đúng. Nếu phân rã sai từ đầu, các bước sau vẫn có thể rất nhất quán nhưng cùng đi tới kết luận sai.

## Prompting có bước lập luận

Ví dụ có các bước trung gian đôi khi cải thiện hiệu quả ở toán, symbolic task và tác vụ tổ hợp. Một cách hiểu thực dụng là mô hình được đưa vào phân bố đầu ra nơi lời giải được trải qua nhiều token thay vì ép toàn bộ phép tính vào một token đáp án ngắn.

Nhưng phần reasoning hiển thị không nên được coi là bản ghi trung thực bắt buộc của computation bên trong. Bản thân lời giải thích cũng là văn bản được sinh.

## Self-consistency

Một chiến lược là sinh nhiều đường giải khác nhau rồi tổng hợp đáp án cuối. Nếu mỗi đường có xác suất đúng đủ cao và lỗi không hoàn toàn tương quan, bỏ phiếu có thể tăng accuracy.

Chi phí tăng gần theo số sample. Nếu mô hình có cùng một misconception hệ thống, self-consistency chỉ tạo nhiều biến thể của cùng lỗi.

## Tìm kiếm trên các đường lập luận

Thay vì chỉ lấy một trajectory, hệ thống có thể phân nhánh các bước ứng viên, chấm điểm, cắt nhánh và tiếp tục. Đây là kết nối trực tiếp với tìm kiếm cổ điển:

```text
state     = lời giải một phần
operator  = đề xuất bước reasoning tiếp theo
heuristic = verifier hoặc value model
search    = chọn nhánh để mở rộng
```

LLM lúc này đóng vai trò mô hình đề xuất (proposal model) bên trong hệ thống search.

## Kiểm chứng

Độ tin cậy tăng mạnh khi kết quả trung gian hoặc cuối có thể được kiểm tra bằng công cụ xác định như:

- máy tính;
- compiler;
- SQL engine;
- theorem prover;
- unit test;
- symbolic algebra.

Một pattern mạnh là:

```text
LLM đề xuất
→ verifier bên ngoài kiểm tra
→ mô hình sửa nếu cần
```

Cách này thường đáng tin hơn việc chỉ yêu cầu mô hình “tự tin hơn” hoặc “kiểm tra lại”.

## Lập luận có công cụ hỗ trợ

LLM không cần tự thực hiện mọi phép toán. Với số học lớn, gọi calculator hợp lý hơn sinh từng chữ số. Với dữ liệu hiện tại, truy vấn API tốt hơn đoán từ trọng số.

Năng lực ở cấp hệ thống đến từ việc chọn đúng công cụ và tích hợp kết quả đúng cách.

## Tính toán ẩn và reasoning hiển thị

Một phần computation diễn ra trong hidden state trước mỗi token. Rationale hiển thị chỉ là một cách chiếu quá trình đó thành ngôn ngữ.

Vì vậy không có lời giải thích dài không có nghĩa không có computation; ngược lại có rationale dài cũng không bảo đảm rationale phản ánh đúng cơ chế tạo đáp án.

Đánh giá engineering nên đo kết quả tác vụ, verification và robustness thay vì chỉ đo “trông có vẻ đang suy nghĩ”.

## Compute lúc kiểm thử

Cho mô hình thêm token suy luận, nhiều sample, search hoặc verifier call là cách tăng **compute lúc kiểm thử (test-time compute)**. Đây là một trục khác với tăng kích thước mô hình.

Đánh đổi:

```text
nhiều compute hơn
→ có thể đáng tin hơn
nhưng
→ độ trễ và chi phí cao hơn
```

Ứng dụng nên cấp ngân sách theo mức rủi ro của tác vụ.

## Lập kế hoạch và lập luận

Reasoning thường biến thông tin thành kết luận. **Lập kế hoạch (planning)** chọn chuỗi hành động để đạt mục tiêu trong môi trường.

LLM agent có thể dùng reasoning để tạo plan, nhưng chất lượng plan còn phụ thuộc theo dõi state, mô hình hóa hiệu ứng hành động và feedback từ environment.

Xem: [Planning](../02_search_reasoning_and_planning/05_planning.md).

## Thất bại ở số học

Language modeling không bảo đảm số học chính xác. Các phép carry theo chữ số có thể mong manh khi chuỗi dài.

Calculator giải bài toán bằng thuật toán xác định. Đây là ví dụ rõ rằng hệ thống mạnh hơn không nhất thiết cần mô hình tự thực hiện mọi computation.

## Thất bại ở logic

LLM có thể tạo syllogism nghe hợp lý nhưng sai ở phủ định, lượng từ hoặc cách diễn đạt đối kháng. Formal solver có semantics và quy tắc chứng minh tường minh.

Một kiến trúc lai có thể dùng mô hình để chuyển natural language thành biểu diễn formal rồi để solver kiểm chứng.

## Lập luận dưới bất định

Không phải bài toán nào cũng có một đáp án chính xác duy nhất. Bayesian reasoning hoặc decision reasoning cần biểu diễn uncertainty và utility. Câu văn thể hiện sự chắc chắn do LLM sinh không phải xác suất đã được calibration.

Với quyết định rủi ro cao, mô hình xác suất tường minh hoặc policy domain nên bổ sung.

## Vấn đề tính trung thực của rationale

Rationale được sinh có thể là lời giải thích hậu nghiệm (post-hoc explanation). Mô hình có thể đi đến đáp án nhờ feature khác với điều nó mô tả trong lời giải thích.

Do đó không nên dùng chain-of-thought text làm audit trail duy nhất cho quyết định được quản lý chặt.

## Scratchpad nội bộ và giải thích cho người dùng

Hệ thống có thể tách computation nội bộ khỏi phần giải thích ngắn gọn cho user. Người dùng thường cần lý do và bằng chứng có thể kiểm chứng hơn là toàn bộ scratch work theo token.

Giải thích tốt nên nêu premise, source, phép tính và uncertainty liên quan.

## Benchmark reasoning

Benchmark toán, code hoặc logic chỉ đo từng lát cắt của reasoning. Điểm cao không đồng nghĩa năng lực suy luận phổ quát.

Nhiễm dữ liệu, độ nhạy prompt và cách verifier chấm cũng ảnh hưởng score.

## Mô hình tư duy

> Lập luận bằng LLM đáng tin nhất khi được xem như **đề xuất xác suất + phân rã có cấu trúc + search/verification bên ngoài**, chứ không phải một oracle suy luận hoàn hảo.

## Những hiểu lầm thường gặp

### “Mô hình viết reasoning dài nghĩa là reasoning sâu”

Độ dài không bảo đảm tính đúng.

### “Nếu model reasoning tốt thì không cần tool”

Tool thường xử lý tác vụ chính xác đáng tin và rẻ hơn.

### “Reasoning là một năng lực đơn nhất”

Toán, code, causal reasoning, planning và commonsense reasoning có failure mode khác nhau.

## Liên kết kiến thức

Reasoning nối Transformer và ICL với [Search](../02_search_reasoning_and_planning/00_state_space_and_search.md), [Logic](../03_knowledge_and_reasoning/03_inference_and_reasoning.md), Agent và tool use.

Xem tiếp: [Hallucination and Grounding](./13_hallucination_and_grounding.md).