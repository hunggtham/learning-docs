# Nền tảng an toàn AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Nền tảng an toàn AI**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Kiến thức cần có trước** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Phân biệt an toàn (safety / 안전), bảo mật (security / 보안), Alignment và quản trị (governance / 거버넌스)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**An toàn AI (AI Safety / AI 안전)** nghiên cứu và kỹ nghệ cách xây dựng hệ thống AI sao cho hành vi vẫn nằm trong phạm vi được chấp nhận, có thể giám sát, có thể giới hạn hậu quả và có thể phục hồi khi thất bại. An toàn không đồng nghĩa với bảo mật, căn chỉnh hay quản trị, dù các lĩnh vực này liên kết chặt chẽ.

## Kiến thức cần có trước

Nên đọc [Agent Systems](../10_agents_and_ai_systems/README.md), [AI System Design](../15_ai_engineering/10_ai_system_design.md), [Evaluation & Reliability](../18_evaluation_reliability_interpretability/README.md) và [Incident Response](../16_mlops_and_llmops/09_incident_response_and_lifecycle.md).

> **Chuyển mạch:** Trong **Nền tảng an toàn AI**, **Phân biệt an toàn (safety / 안전), bảo mật (security / 보안), Alignment và quản trị (governance / 거버넌스)** tiếp nhận điểm tựa từ **Kiến thức cần có trước** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Từ lỗi mô hình tới hậu quả thực tế** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân biệt an toàn (safety / 안전), bảo mật (security / 보안), Alignment và quản trị (governance / 거버넌스)

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
An toàn (safety)
→ hệ thống có thể gây hậu quả nguy hiểm bằng cách nào?

Bảo mật (security)
→ attacker có thể khai thác hệ thống bằng cách nào?

Căn chỉnh (alignment)
→ mục tiêu/hành vi có phù hợp ý định và ràng buộc không?

Quản trị (governance)
→ ai chịu trách nhiệm, ai được phê duyệt, quy trình nào kiểm soát vòng đời?
```

Một prompt injection là vấn đề bảo mật nhưng có thể dẫn tới hậu quả an toàn. Một reward sai có thể tạo rủi ro an toàn dù không có attacker.

> **Chuyển mạch:** Ở chặng này của **Nền tảng an toàn AI**, **Từ lỗi mô hình tới hậu quả thực tế** tiếp nhận điểm tựa từ **Phân biệt an toàn (safety / 안전), bảo mật (security / 보안), Alignment và quản trị (governance / 거버넌스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rủi ro (risk / 위험) và residual rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ lỗi mô hình tới hậu quả thực tế

Không phải mọi lỗi dự đoán đều tạo cùng mức rủi ro. Một chuỗi gây hại có thể được mô hình hóa:

```text
lỗi mô hình
→ quyết định sai
→ hành động hoặc thông tin sai
→ người dùng/hệ thống tin và sử dụng
→ hậu quả
```

Ví dụ trợ lý y tế:

```text
failure mode: liều lượng bị hallucination
→ hazard: người dùng tin là thật
→ exposure: không có cảnh báo hoặc review
→ harm: dùng thuốc sai
```

Điều này giải thích vì sao UI, verifier, permission và human rà soát (review / 검토) có thể giảm rủi ro (risk / 위험) ngay cả khi mô hình (model / 모델) lỗi (error / 오류) chưa về 0.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng an toàn AI**, **Rủi ro (risk / 위험) và residual rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **Từ lỗi mô hình tới hậu quả thực tế** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hazard và dạng thất bại (failure mode / 실패 모드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rủi ro (risk / 위험) và residual rủi ro (risk / 위험)

Một trực giác đơn giản:

\[
rủi ro (risk / 위험)\approx P(Harm)\times Severity(Harm)
\]

Nhưng trong hệ thống mở, xác suất thường khó biết chính xác. môi trường vận hành (production / 운영 환경) rủi ro (risk / 위험) assessment nên xem thêm:

- mức phơi nhiễm;
- khả năng phát hiện;
- khả năng đảo ngược;
- phạm vi ảnh hưởng;
- thời gian tồn tại của lỗi;
- khả năng attacker thích nghi;
- độ tin cậy của bằng chứng (evidence / 증거).

Sau khi áp dụng điều khiển (control / 제어) vẫn còn **rủi ro còn lại (residual risk)**. Quyết định deploy phải dựa trên residual rủi ro (risk / 위험), không phải giả định rằng điều khiển (control / 제어) đã loại bỏ toàn bộ rủi ro.

> **Chuyển mạch:** Trong **Nền tảng an toàn AI**, **Hazard và dạng thất bại (failure mode / 실패 모드)** tiếp nhận điểm tựa từ **Rủi ro (risk / 위험) và residual rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **An toàn (safety / 안전) trường hợp (case / 사례)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hazard và dạng thất bại (failure mode / 실패 모드)

**Mối nguy (hazard)** là điều kiện có thể dẫn đến harm. **Kiểu thất bại (failure mode)** là cách hệ thống không đáp ứng đặc tả hợp đồng (contract / 계약).

Một dạng thất bại (failure mode / 실패 모드) có thể không nguy hiểm trong use trường hợp (case / 사례) này nhưng nguy hiểm trong use trường hợp (case / 사례) khác. Ví dụ đầu ra (output / 출력) chậm 3 giây có thể chấp nhận ở công cụ tóm tắt, nhưng nguy hiểm trong hệ thống điều khiển thời gian thực.

> **Chuyển mạch:** Ở chặng này của **Nền tảng an toàn AI**, **Hazard và dạng thất bại (failure mode / 실패 모드)** cho ta quy tắc; **An toàn (safety / 안전) trường hợp (case / 사례)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Năng lực (capability / 역량), autonomy và attack surface** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## An toàn (safety / 안전) trường hợp (case / 사례)

Thay vì tuyên bố “mô hình an toàn”, nên xây một **lập luận an toàn (safety case)**:

```text
claim
→ assumption
→ evidence
→ control
→ monitoring
→ residual risk
```

Ví dụ:

```text
claim: agent không được tự chuyển tiền vượt hạn mức
assumption: mọi giao dịch đi qua payment tool chuẩn
control: backend limit + authorization + approval
validation: integration test + adversarial scenario
monitoring: audit log + alert vượt ngưỡng
residual risk: bug ở payment service hoặc credential compromise
```

An toàn (safety / 안전) là thuộc tính của cả hệ thống dưới những điều kiện xác định, không phải nhãn tuyệt đối của một checkpoint.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng an toàn AI**, **An toàn (safety / 안전) trường hợp (case / 사례)** cho ta quy tắc; **Năng lực (capability / 역량), autonomy và attack surface** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Tính đảo ngược** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Năng lực (capability / 역량), autonomy và attack surface

Khi năng lực (capability / 역량) tăng, bề mặt hậu quả cũng tăng. Một chatbot chỉ trả văn bản khác hoàn toàn tác nhân (agent / 에이전트) có quyền:

- đọc tệp (file / 파일);
- gọi cơ sở dữ liệu (database / 데이터베이스);
- gửi email;
- sửa mã (code / 코드);
- tạo giao dịch;
- lưu bộ nhớ (memory / 메모리) dài hạn.

Mức tự chủ (autonomy) là một lựa chọn kiến trúc. Không nên tăng autonomy chỉ vì mô hình (model / 모델) đủ khả năng; phải tăng đồng thời verifier, permission, trạng thái (state / 상태) management, khả năng quan sát (observability / 관측 가능성) và khôi phục (recovery / 복구).

> **Chuyển mạch:** Trong **Nền tảng an toàn AI**, **Tính đảo ngược** tiếp nhận điểm tựa từ **Năng lực (capability / 역량), autonomy và attack surface** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Specification bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính đảo ngược

Một nguyên tắc môi trường vận hành (production / 운영 환경) mạnh là ưu tiên hành động có thể đảo ngược khi bất định (uncertainty / 불확실성) cao.

```text
nháp email → có thể review
xóa file vĩnh viễn → khó đảo ngược
đề xuất lệnh → có thể kiểm tra
thực thi payment → hậu quả cao
```

Hành động càng khó đảo ngược, điều khiển (control / 제어) trước thực thi (execution / 실행) càng cần mạnh.

> **Chuyển mạch:** Ở chặng này của **Nền tảng an toàn AI**, **Specification bài toán (problem / 문제)** tiếp nhận điểm tựa từ **Tính đảo ngược** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân phối (distribution / 분포) shift** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Specification bài toán (problem / 문제)

Ý định con người thường giàu hơn mục tiêu có thể đo. Nếu hệ thống tối ưu proxy, nó có thể tìm lỗ hổng giữa proxy và mục tiêu thật.

Ví dụ:

```text
mục tiêu thật: người dùng nhận nội dung hữu ích
proxy: watch time tối đa
```

Tối ưu proxy có thể tăng watch thời gian (time / 시간) bằng nội dung gây nghiện. Xem sâu hơn ở [Căn chỉnh AI](./01_alignment_and_objective_specification.md) và [Reward Misspecification](./02_reward_misspecification_and_goal_misgeneralization.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng an toàn AI**, **Phân phối (distribution / 분포) shift** tiếp nhận điểm tựa từ **Specification bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Defense in độ sâu (depth / 깊이)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân phối (distribution / 분포) shift

Điều khiển (control / 제어) được xác minh trên phân phối (distribution / 분포) này có thể thất bại khi:

- ngôn ngữ thay đổi;
- người dùng (user / 사용자) hành vi (behavior / 동작) thay đổi;
- công cụ (tool / 도구) mới được thêm;
- corpus RAG thay đổi;
- provider mô hình (model / 모델) thay đổi;
- attacker học cách thích nghi.

Do đó an toàn (safety / 안전) không kết thúc ở pre-release benchmark. Nó cần monitoring và regression evaluation liên tục.

> **Chuyển mạch:** Trong **Nền tảng an toàn AI**, **Defense in độ sâu (depth / 깊이)** tiếp nhận điểm tựa từ **Phân phối (distribution / 분포) shift** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fail-safe và fail-closed** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Defense in độ sâu (depth / 깊이)

Không nên dựa vào một lớp duy nhất:

```text
hành vi mô hình
+ kiểm tra input
+ quyền hạn
+ sandbox
+ schema công cụ
+ verifier
+ human approval
+ monitoring
+ incident response
```

Mỗi lớp giảm một loại thất bại (failure / 실패) khác nhau. Nếu một lớp bị bypass, các lớp sau vẫn phải giới hạn hậu quả.

> **Chuyển mạch:** Ở chặng này của **Nền tảng an toàn AI**, **Fail-safe và fail-closed** tiếp nhận điểm tựa từ **Defense in độ sâu (depth / 깊이)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Human factors** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fail-safe và fail-closed

Với hành động rủi ro cao:

```text
không xác minh được
→ không thực thi
```

là lựa chọn hợp lý. Nhưng fail-closed làm giảm availability. Use trường hợp (case / 사례) rủi ro thấp có thể chọn degraded fallback thay vì chặn toàn bộ.

Không có chính sách fail-open/fail-closed đúng cho mọi hệ thống; lựa chọn phải gắn với impact.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng an toàn AI**, **Human factors** tiếp nhận điểm tựa từ **Fail-safe và fail-closed** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Evaluation cho an toàn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Human factors

Đầu ra (output / 출력) trôi chảy có thể tạo **thiên lệch tự động hóa (automation bias)**: người dùng tin kết quả hơn mức bằng chứng (evidence / 증거) cho phép.

An toàn (safety / 안전) kỹ thuật (engineering / 엔지니어링) phải xem cả giao diện và quy trình:

- nguồn có được hiển thị không;
- bất định (uncertainty / 불확실성) có được truyền đạt không;
- approval có hiển thị hành động (action / 동작) thật không;
- người rà soát (review / 검토) có đủ ngữ cảnh (context / 맥락) không;
- warning có bị bỏ qua vì xuất hiện quá nhiều không.

> **Chuyển mạch:** Trong **Nền tảng an toàn AI**, **Evaluation cho an toàn** tiếp nhận điểm tựa từ **Human factors** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Red teaming** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Evaluation cho an toàn

Bộ kiểm thử (test / 테스트) nên gồm:

```text
known harmful scenarios
misuse / abuse
prompt injection
edge cases
long-horizon agent behavior
tool permission failures
recovery / fallback
multilingual/domain slices
```

Không có finite bộ kiểm thử (test suite / 테스트 스위트) nào chứng minh an toàn tuyệt đối. Mục tiêu là tăng coverage và bằng chứng (evidence / 증거) theo rủi ro (risk / 위험) mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Nền tảng an toàn AI**, **Red teaming** tiếp nhận điểm tựa từ **Evaluation cho an toàn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình triển khai môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Red teaming

Red teaming chủ động tìm thất bại (failure / 실패) thay vì chờ môi trường vận hành (production / 운영 환경) phát hiện. Kết quả red nhóm (team / 팀) có giá trị khi được chuyển thành:

```text
failure taxonomy
→ architecture fix
→ regression test
→ release gate
→ monitoring signal
```

Chỉ lưu “prompt đã jailbreak được” mà không thay đổi điều khiển (control / 제어) thì chưa hoàn thành vòng học.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng an toàn AI**, **Mô hình triển khai môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **Red teaming** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình triển khai môi trường vận hành (production / 운영 환경)

Một hệ thống rủi ro vừa/cao có thể theo luồng (flow / 흐름):

```text
request
→ authentication
→ input validation
→ model/retrieval/tool reasoning
→ policy + authorization
→ verifier
→ approval nếu cần
→ execution
→ outcome verification
→ durable state
→ audit / monitoring
```

Mỗi bước nên có đơn vị sở hữu (owner / 오너), hành vi khi thất bại (failure behavior / 실패 동작) và dấu vết (trace / 추적) rõ ràng.

> **Chuyển mạch:** Trong **Nền tảng an toàn AI**, **Sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **Mô hình triển khai môi trường vận hành (production / 운영 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dạng thất bại (failure mode / 실패 모드) thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự đánh đổi (trade-off / 트레이드오프)

An toàn (safety / 안전) điều khiển (control / 제어) thường đánh đổi:

- độ trễ (latency / 지연 시간);
- chi phí (cost / 비용);
- autonomy;
- tỷ lệ tự động hóa;
- false positive refusal;
- nhà phát triển (developer / 개발자) velocity.

Mục tiêu không phải tối đa mọi điều khiển (control / 제어), mà là chọn điều khiển (control / 제어) tương ứng rủi ro (risk / 위험) lớp (class / 클래스) và khả năng phục hồi.

> **Chuyển mạch:** Ở chặng này của **Nền tảng an toàn AI**, **Dạng thất bại (failure mode / 실패 모드) thường gặp** tiếp nhận điểm tựa từ **Sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dạng thất bại (failure mode / 실패 모드) thường gặp

**Safe mô hình (model / 모델), unsafe ứng dụng (application / 애플리케이션).** công cụ (tool / 도구) permission quá rộng hoặc UI khiến người dùng (user / 사용자) overtrust.

**Benchmark an toàn (safety / 안전) overfitting.** Tốt trên kiểm thử (test / 테스트) set nhưng yếu với ngôn ngữ hoặc attack mới.

**Fallback không được kiểm thử (test / 테스트).** Chỉ tồn tại trong diagram.

**Approval sau side tác động (effect / 효과).** Human rà soát (review / 검토) đến quá muộn.

**Monitoring chỉ đo HTTP 200.** Không phát hiện silent chất lượng (quality / 품질)/an toàn (safety / 안전) degradation.

**Không có kill switch.** Không thể vô hiệu hóa năng lực (capability / 역량) nhanh khi sự cố (incident / 인시던트) xảy ra.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng an toàn AI**, **Mô hình tư duy** gom các mảnh từ **Dạng thất bại (failure mode / 실패 모드) thường gặp** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> **An toàn AI = nhận diện mối nguy → giới hạn năng lực (capability / 역량) → kiểm chứng hành vi → giới hạn hậu quả → quan sát môi trường vận hành (production / 운영 환경) → phục hồi khi thất bại.**

> **Chuyển mạch:** Trong **Nền tảng an toàn AI**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Mô hình an toàn = ứng dụng an toàn”

Không. Permission, retrieval, công cụ (tool / 도구), UI và workflow có thể làm ứng dụng nguy hiểm dù mô hình (model / 모델) tương đối tốt.

### “bảo mật (security / 보안) và an toàn (safety / 안전) là một”

Không. bảo mật (security / 보안) tập trung vào khai thác có chủ đích; an toàn (safety / 안전) bao gồm cả lỗi không có attacker.

### “Một benchmark đủ chứng minh an toàn”

Không. an toàn (safety / 안전) phụ thuộc ngữ cảnh (context / 맥락), phân phối (distribution / 분포), công cụ (tool / 도구) và triển khai (deployment / 배포).

> **Chuyển mạch:** Ở chặng này của **Nền tảng an toàn AI**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Căn chỉnh AI](./01_alignment_and_objective_specification.md), [Prompt Injection](./03_prompt_injection_and_jailbreaks.md), [Adversarial ML](./04_adversarial_machine_learning.md), [Reliability](../18_evaluation_reliability_interpretability/07_reliability_engineering.md), [Reliable Agent Design](../10_agents_and_ai_systems/10_reliable_agent_design.md), [AI System Design](../15_ai_engineering/10_ai_system_design.md) và [Incident Response](../16_mlops_and_llmops/09_incident_response_and_lifecycle.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
