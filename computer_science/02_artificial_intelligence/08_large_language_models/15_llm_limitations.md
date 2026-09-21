# Giới hạn của mô hình ngôn ngữ lớn

LLM mạnh vì học các quy luật thống kê rộng từ lượng dữ liệu và compute lớn, nhưng kiến trúc và objective của chúng tạo ra những giới hạn mang tính cấu trúc. Hiểu các giới hạn này giúp chọn đúng kiến trúc hệ thống thay vì cố “prompt mạnh hơn” cho mọi vấn đề.

## Tri thức không có provenance tự nhiên

Trọng số không lưu citation của source theo dạng cơ sở dữ liệu. Mô hình có thể sinh một fact nhưng không tự biết tài liệu chính xác nào hỗ trợ fact đó.

Nếu provenance là yêu cầu, cần retrieval và source tracking bên ngoài.

## Tri thức có mốc thời gian và có thể lỗi thời

Pretraining xảy ra tại một giai đoạn cụ thể. Fact xuất hiện sau mốc dữ liệu hoặc trạng thái thay đổi liên tục không tự nằm trong trọng số nếu không có continued training/update.

Dữ liệu hiện tại nên đến từ tool, API, database hoặc RAG.

## Hallucination

Objective tự hồi quy yêu cầu mô hình tiếp tục chuỗi chứ không bảo đảm sự thật. Mô hình có thể tạo câu sai với phong cách rất tự tin.

Xem: [Hallucination and Grounding](./13_hallucination_and_grounding.md).

## Cửa sổ ngữ cảnh hữu hạn

Mô hình chỉ condition trên token nằm trong context window hiện tại. Hội thoại dài cần cắt bớt, tóm tắt hoặc retrieval từ memory ngoài.

Ngay cả khi toàn bộ token vẫn vừa cửa sổ, **mức sử dụng hiệu quả** của thông tin ở đầu, giữa và cuối context có thể không đồng đều.

## Reasoning không được bảo đảm

LLM có thể giải nhiều bài toán lập luận nhưng vẫn thất bại ở biến thể logic đơn giản, đặc biệt với prompt đối kháng hoặc distribution shift.

Khi độ chính xác tuyệt đối quan trọng, nên bổ sung external verification.

## Tính toán chính xác yếu hơn công cụ thuật toán

Số học với số lớn, exhaustive search, tổng hợp database và formal proof thường phù hợp hơn với công cụ chuyên dụng thay vì token generation.

Hệ thống tốt phân công phép toán cho đúng nền tảng tính toán.

## Calibration còn hạn chế

Câu chữ thể hiện sự tự tin không phải xác suất đúng. Các từ như “chắc chắn” có thể chỉ là phong cách đã học.

Quyết định nhạy rủi ro cần score đã calibration hoặc kiểm tra ngoài mô hình.

## Nhạy với prompt

Thay đổi nhỏ trong cách diễn đạt có thể làm đầu ra khác. Hậu huấn luyện giảm nhưng không loại bỏ hoàn toàn hiện tượng này.

Prompt production cần regression test và versioning.

## Dễ chịu ảnh hưởng của prompt injection

Mô hình vốn được huấn luyện để làm theo pattern và instruction trong context. Khi document không đáng tin nằm cùng context với chỉ dẫn có quyền cao, attacker có thể cố điều hướng mô hình.

Security cần ranh giới quyền bên ngoài model.

## Tính không xác định

Sampling làm đầu ra thay đổi giữa các lần chạy. Ngay cả deterministic decoding cũng có thể thay đổi khi model/provider version, kernel hoặc hệ thống serving thay đổi.

Nếu ứng dụng cần khả năng tái lập nghiêm ngặt, nên tách các thành phần xác định và ghi lại model version, config và môi trường thực thi.

## Bias từ dữ liệu

Corpus huấn luyện phản ánh mất cân bằng xã hội, ngôn ngữ và địa lý. Mô hình có thể yếu hơn ở low-resource language/domain hoặc tái tạo stereotype.

Đánh giá phải bao phủ population mục tiêu thay vì chỉ nhìn benchmark trung bình.

## Lỗi đuôi dài

Mô hình có thể đúng 99% ở case phổ biến nhưng thất bại khó đoán ở edge case hiếm. Với triển khai quy mô lớn, 1% vẫn có thể tạo rất nhiều sự cố.

Guardrail, fallback và human review nên tập trung vào những tail failure có chi phí cao.

## Distribution shift

Hành vi người dùng thay đổi, thuật ngữ mới xuất hiện và chiến lược tấn công tiến hóa. Offline eval tĩnh sẽ mất giá trị theo thời gian.

Monitoring và continual evaluation là cần thiết.

## Lỗi công cụ có thể khuếch đại

Agentic LLM có thể gọi tool, nhưng tham số sai có thể thay đổi trạng thái bên ngoài. Năng lực ngôn ngữ của mô hình không bảo đảm an toàn giao dịch.

Cần quyền tối thiểu, idempotency, validation, bước xác nhận và audit log.

## Bộ nhớ không giống con người

“Bộ nhớ hội thoại” thường đến từ context, retrieval hoặc database của ứng dụng. LLM không tự duy trì episodic memory bền vững qua nhiều phiên nếu hệ thống không cung cấp cơ chế đó.

## Khả năng giải thích còn chưa đầy đủ

Attention weight hoặc rationale do mô hình sinh không cung cấp lời giải thích đầy đủ về computation nội bộ. **Mechanistic interpretability** có thể khám phá một số circuit và pattern nhưng chưa làm quyết định của mô hình lớn hoàn toàn minh bạch.

## Bất định về dữ liệu huấn luyện

Với nhiều mô hình, thành phần corpus chính xác có thể không được công khai đầy đủ. Điều này làm phân tích copyright, contamination và provenance khó hơn.

## Hiểu ngôn ngữ và tương tác thế giới là hai việc khác nhau

Mô hình chỉ-text học pattern của thế giới thông qua văn bản. Grounding vật lý, cảm biến và hành động thời gian thực cần giao diện đa phương thức, robot hoặc tool.

Năng lực ngôn ngữ không nên bị đồng nhất với trải nghiệm embodied trực tiếp.

## Lệch giữa objective và mục tiêu thật

Pretraining tối ưu token prediction; post-training tối ưu preference hoặc policy signal. Mục tiêu thật của người dùng có thể khác proxy đó.

Đây là vấn đề kiểu **Goodhart**: proxy được tối ưu rất tốt nhưng mục tiêu thật có thể bị tổn hại.

## Giới hạn của model và giới hạn của system

Nhiều “giới hạn LLM” có thể được giảm ở cấp hệ thống:

```text
tri thức cũ   → RAG / API
số học        → calculator
factuality    → grounding / verifier
workflow dài  → agent state + tools
định dạng     → constrained decoding / schema
bảo mật       → permission / sandbox
```

Tuy nhiên mỗi lớp bổ sung cũng tạo độ phức tạp và failure mode mới.

## Khi LLM là công cụ không phù hợp

Nếu bài toán có quy tắc xác định chính xác, ít mơ hồ và yêu cầu verification cao, phần mềm truyền thống có thể tốt hơn.

Ví dụ:

```text
tính lãi
kiểm tra quyền
schema validation
sinh ID duy nhất
xác minh mật mã
```

LLM có thể giải thích hoặc làm giao diện quanh rule engine nhưng không nên thay deterministic core.

## Mô hình tư duy

> LLM là **động cơ xác suất cho ngôn ngữ và biểu diễn**, không phải database, calculator, theorem prover, policy engine hay operating system. Hệ thống AI mạnh bằng cách kết hợp LLM với đúng thành phần khác.

## Những hiểu lầm thường gặp

### “Thế hệ model sau sẽ làm mọi giới hạn biến mất”

Một số hạn chế có thể giảm, nhưng bảo đảm sự thật, provenance, authorization và thực thi xác định vẫn là vấn đề cấp hệ thống.

### “Nếu prompt đủ tốt thì không cần kiến trúc khác”

Prompt không thay được tri thức bên ngoài, tool hoặc validation.

### “LLM có failure nghĩa AI không hữu ích”

Không. Giá trị đến từ việc ghép đúng năng lực với đúng tác vụ và engineering quanh failure mode.

## Liên kết kiến thức

Các giới hạn này dẫn trực tiếp tới những layer tiếp theo: [Retrieval & RAG](../09_retrieval_and_rag/00_information_retrieval_foundations.md), Agents, Evaluation, Safety và AI Engineering.