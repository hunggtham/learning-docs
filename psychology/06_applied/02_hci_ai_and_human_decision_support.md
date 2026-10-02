# HCI, AI và hỗ trợ ra quyết định của con người

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **HCI, AI và hỗ trợ ra quyết định của con người**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Working bộ nhớ (memory / 메모리) là tài nguyên hữu hạn** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Cognitive tải (load / 로드) không phải cứ “ít element” là tốt** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối HCI với AI và human decision support, để thiết kế hỗ trợ con người mà không che khuất uncertainty hay quyền quyết định.

Khi xây phần mềm, ta không chỉ thiết kế giao diện. Ta đang thiết kế một **môi trường nhận thức (cognitive environment)**: hệ thống quyết định thông tin nào nổi bật, lúc nào người dùng bị ngắt quãng, lỗi (error / 오류) được trình bày ra sao, lựa chọn mặc định là gì và người dùng phải nhớ bao nhiêu thứ trong đầu.

Vì vậy, HCI (Human–Computer Interaction / tương tác người–máy) là điểm gặp tự nhiên giữa psychology, khoa học máy tính (computer science / 컴퓨터 과학) và thiết kế (design / 설계).

## Working bộ nhớ (memory / 메모리) là tài nguyên hữu hạn

Nếu UI yêu cầu người dùng nhớ ID từ màn hình trước, đối chiếu nhiều trường dữ liệu (field / 필드) và giữ quy tắc (rule / 규칙) nghiệp vụ trong đầu, ta đã chuyển chi phí (cost / 비용) từ hệ thống (system / 시스템) sang working bộ nhớ (memory / 메모리) của người dùng (user / 사용자).

Một nguyên tắc hữu ích là **recognition over recall**: khi có thể, hãy để hệ thống (system / 시스템) hiển thị option/ngữ cảnh (context / 맥락) thay vì bắt người dùng (user / 사용자) nhớ chính xác.

Ví dụ:

- dropdown có label rõ tốt hơn bắt nhớ mã (code / 코드);
- inline kiểm tra hợp lệ (validation / 검증) tốt hơn báo lỗi tổng quát ở cuối form;
- breadcrumb tốt hơn bắt người dùng (user / 사용자) nhớ mình đang ở tầng điều hướng (navigation / 내비게이션) nào.

Xem thêm: [[../02_learning_and_cognition/01_memory]], [[../02_learning_and_cognition/10_cognitive_offloading_external_memory_and_extended_cognition]].

> **Chuyển mạch:** Trong **HCI, AI và hỗ trợ ra quyết định của con người**, **Cognitive tải (load / 로드) không phải cứ “ít element” là tốt** tiếp nhận điểm tựa từ **Working bộ nhớ (memory / 메모리) là tài nguyên hữu hạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Attention là hệ thống cạnh tranh ưu tiên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cognitive tải (load / 로드) không phải cứ “ít element” là tốt

Tải nhận thức (cognitive load) phụ thuộc vào tác vụ (task / 작업), expertise và thông tin (information / 정보) cấu trúc (structure / 구조). Một screen nhiều thông tin nhưng được chunk tốt có thể dễ hơn screen tối giản buộc người dùng (user / 사용자) mở nhiều popup.

Đặc biệt với enterprise software, mục tiêu không phải “trông tối giản” mà là **giảm unnecessary mental transformation**.

> **Chuyển mạch:** Ở chặng này của **HCI, AI và hỗ trợ ra quyết định của con người**, **Attention là hệ thống cạnh tranh ưu tiên** tiếp nhận điểm tựa từ **Cognitive tải (load / 로드) không phải cứ “ít element” là tốt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lỗi (error / 오류) là tương tác (interaction / 상호작용) giữa người và hệ thống (system / 시스템)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Attention là hệ thống cạnh tranh ưu tiên

Notification, animation, color contrast và motion đều cạnh tranh attention. Nếu mọi thứ đều nổi bật thì không còn hierarchy.

UI nên dùng salience tương ứng với quyết định (decision / 결정) importance. Một destructive hành động (action / 동작) cần nổi bật theo cách khác một informational badge.

Attention capture cũng có chi phí (cost / 비용) sau khi interruption kết thúc: người dùng phải tái dựng tác vụ (task / 작업) trạng thái (state / 상태). Với nhà phát triển (developer / 개발자) hoặc analyst, frequent ngữ cảnh (context / 맥락) switching có thể gây mất nhiều thời gian hơn bản thân interruption.

Xem thêm: [[../01_brain_and_mind/07_attention_consciousness_and_awareness]], [[./00_work_organization_and_leadership]].

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HCI, AI và hỗ trợ ra quyết định của con người**, **Lỗi (error / 오류) là tương tác (interaction / 상호작용) giữa người và hệ thống (system / 시스템)** tiếp nhận điểm tựa từ **Attention là hệ thống cạnh tranh ưu tiên** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델) và hệ thống (system / 시스템) mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lỗi (error / 오류) là tương tác (interaction / 상호작용) giữa người và hệ thống (system / 시스템)

Human lỗi (error / 오류) thường bị giải thích bằng “người dùng (user / 사용자) bất cẩn”. Human factors đặt câu hỏi khác: **hệ thống (system / 시스템) đã tạo điều kiện gì khiến lỗi (error / 오류) dễ xảy ra?**

Có thể phân biệt:

- slip: intention đúng nhưng hành động (action / 동작) sai;
- mistake: mô hình (model / 모델)/quyết định (decision / 결정) sai;
- chế độ (mode / 모드) lỗi (error / 오류): người dùng (user / 사용자) nghĩ hệ thống (system / 시스템) đang ở trạng thái (state / 상태) khác;
- confirmation lỗi (error / 오류): phản hồi (feedback / 피드백) không đủ để người dùng (user / 사용자) nhận ra hành động (action / 동작) đã xảy ra.

Thiết kế tốt không chỉ prevent lỗi (error / 오류) mà còn hỗ trợ **khôi phục (recovery / 복구)**: undo, clear status, reversible hành động (action / 동작) và meaningful lỗi (error / 오류) message.

> **Chuyển mạch:** Trong **HCI, AI và hỗ trợ ra quyết định của con người**, **Mô hình tư duy (mental model / 사고 모델) và hệ thống (system / 시스템) mô hình (model / 모델)** gom các mảnh từ **Lỗi (error / 오류) là tương tác (interaction / 상호작용) giữa người và hệ thống (system / 시스템)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Affordance và phản hồi (feedback / 피드백)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델) và hệ thống (system / 시스템) mô hình (model / 모델)

Người dùng không nhìn thấy cơ sở dữ liệu (database / 데이터베이스), máy trạng thái (state machine / 상태 머신) hay backend workflow. Họ xây một **mô hình tư duy (mental model / 사고 모델)** dựa trên những gì UI cho thấy.

Nếu UI hiển thị một button “Save” nhưng thực tế hành động (action / 동작) chỉ lưu draft cục bộ (local / 로컬), mô hình tư duy (mental model / 사고 모델) sẽ sai. Bug usability đôi khi không nằm ở chức năng mà nằm ở ánh xạ (mapping / 매핑) giữa giao diện (interface / 인터페이스) và underlying trạng thái (state / 상태).

> **Chuyển mạch:** Ở chặng này của **HCI, AI và hỗ trợ ra quyết định của con người**, **Affordance và phản hồi (feedback / 피드백)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델) và hệ thống (system / 시스템) mô hình (model / 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Default và choice kiến trúc (architecture / 아키텍처)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Affordance và phản hồi (feedback / 피드백)

**Affordance** liên quan tới việc đối tượng (object / 객체) gợi ý hành động (action / 동작) nào có thể thực hiện. Trong digital UI, nhiều affordance là learned convention: button trông có thể click, link có style nhất quán.

**phản hồi (feedback / 피드백)** trả lời “hành động (action / 동작) vừa rồi có tác dụng gì?”. độ trễ (latency / 지연 시간) không có phản hồi (feedback / 피드백) khiến người dùng (user / 사용자) click lặp, submit nhiều lần hoặc nghĩ hệ thống (system / 시스템) treo.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HCI, AI và hỗ trợ ra quyết định của con người**, **Default và choice kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **Affordance và phản hồi (feedback / 피드백)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **AI thay đổi vai trò của giao diện (interface / 인터페이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Default và choice kiến trúc (architecture / 아키텍처)

Default có influence mạnh vì giảm effort và đôi khi được hiểu như recommendation. Vì vậy default không trung tính hoàn toàn.

Trong enterprise workflow, default có thể tăng efficiency nhưng cũng tạo automation-like độ lệch (bias / 편향): người dùng (user / 사용자) ít xem lại trường dữ liệu (field / 필드) đã được hệ thống (system / 시스템) prefill.

Xem thêm: [[../02_learning_and_cognition/08_decision_under_risk_uncertainty_and_ambiguity]], [[../02_learning_and_cognition/02_thinking_language_and_decision]].

> **Chuyển mạch:** Trong **HCI, AI và hỗ trợ ra quyết định của con người**, **AI thay đổi vai trò của giao diện (interface / 인터페이스)** tiếp nhận điểm tựa từ **Default và choice kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Explainability không tự động tạo trust tốt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## AI thay đổi vai trò của giao diện (interface / 인터페이스)

Với AI hệ thống (system / 시스템), người dùng (user / 사용자) không chỉ thao tác button; họ phải đánh giá đầu ra (output / 출력) có đáng tin hay không. Đây là vấn đề **calibration**, không phải chỉ UX.

Hai dạng thất bại (failure mode / 실패 모드) đối lập:

- **automation độ lệch (bias / 편향)**: tin đầu ra (output / 출력) quá mức vì “máy đã tính”;
- **thuật toán (algorithm / 알고리즘) aversion**: mất trust hoàn toàn sau một lỗi dù hệ thống (system / 시스템) trung bình vẫn hữu ích.

Mục tiêu là **sự phụ thuộc phù hợp (appropriate reliance)**: dùng AI khi comparative advantage của nó cao và kiểm tra mạnh hơn khi bất định (uncertainty / 불확실성)/rủi ro (risk / 위험) cao.

> **Chuyển mạch:** Ở chặng này của **HCI, AI và hỗ trợ ra quyết định của con người**, **Explainability không tự động tạo trust tốt** tiếp nhận điểm tựa từ **AI thay đổi vai trò của giao diện (interface / 인터페이스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Xác minh (verification / 확인) debt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Explainability không tự động tạo trust tốt

Một explanation trông hợp lý có thể làm người dùng (user / 사용자) overtrust hệ thống (system / 시스템) ngay cả khi explanation không phản ánh actual computation. Vì vậy cần phân biệt:

- explanation để giúp debugging;
- explanation để hỗ trợ (support / 지원) quyết định (decision / 결정);
- confidence/bất định (uncertainty / 불확실성) communication;
- provenance/nguồn (source / 소스) visibility.

“AI giải thích được” không đồng nghĩa “AI đúng”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HCI, AI và hỗ trợ ra quyết định của con người**, **Xác minh (verification / 확인) debt** tiếp nhận điểm tựa từ **Explainability không tự động tạo trust tốt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cognitive offloading: AI là công cụ hay phần thay thế kỹ năng?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xác minh (verification / 확인) debt

Khi AI giúp tạo mã (code / 코드), văn bản (text / 텍스트) hoặc phân tích (analysis / 분석) rất nhanh, đầu ra (output / 출력) volume có thể tăng nhanh hơn sức chứa (capacity / 용량) để rà soát (review / 검토). Khoảng chênh này có thể gọi là **nợ kiểm chứng (verification debt)**.

Ví dụ nhà phát triển (developer / 개발자) generate 500 dòng mã (code / 코드) trong vài phút nhưng không hiểu bất biến (invariant / 불변식), phụ thuộc (dependency / 의존성) và dạng thất bại (failure mode / 실패 모드). Productivity tức thời tăng nhưng future debugging chi phí (cost / 비용) cũng tăng.

Cách giảm xác minh (verification / 확인) debt:

- chia generation thành đơn vị (unit / 단위) nhỏ;
- yêu cầu kiểm thử (test / 테스트)/giả định (assumption / 가정) rõ;
- rà soát (review / 검토) diff thay vì chỉ nhìn final đầu ra (output / 출력);
- tự giải thích lại lô-gic (logic / 논리);
- giữ human checkpoint cho high-risk hành động (action / 동작).

> **Chuyển mạch:** Trong **HCI, AI và hỗ trợ ra quyết định của con người**, **Cognitive offloading: AI là công cụ hay phần thay thế kỹ năng?** tiếp nhận điểm tựa từ **Xác minh (verification / 확인) debt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Human-in-the-loop thực sự nghĩa gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cognitive offloading: AI là công cụ hay phần thay thế kỹ năng?

Cognitive offloading có thể hữu ích. Calculator giúp ta không cần giữ arithmetic intermediate trạng thái (state / 상태); IDE autocomplete giảm recall burden; AI có thể giảm tìm kiếm (search / 검색)/synthesis chi phí (cost / 비용).

Vấn đề xuất hiện khi **hiệu năng (performance / 성능) goal** và **học tập (learning / 학습) goal** bị nhầm.

Nếu mục tiêu là ship một tác vụ (task / 작업) đã hiểu rõ, offloading có thể tốt. Nếu mục tiêu là học Java Streams, để AI viết toàn bộ chuỗi xử lý (pipeline / 파이프라인) mà không reconstruct lô-gic (logic / 논리) có thể làm giảm encoding và retrieval practice.

Mô hình tư duy (mental model / 사고 모델):

> Offload lưu trữ (storage / 저장소)/computation khi phù hợp, nhưng đừng offload phần lập luận (reasoning / 추론) mà bạn đang cố học.

> **Chuyển mạch:** Ở chặng này của **HCI, AI và hỗ trợ ra quyết định của con người**, **Human-in-the-loop thực sự nghĩa gì?** tiếp nhận điểm tựa từ **Cognitive offloading: AI là công cụ hay phần thay thế kỹ năng?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **AI anthropomorphism** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Human-in-the-loop thực sự nghĩa gì?

Chỉ có một người bấm “Approve” cuối chuỗi xử lý (pipeline / 파이프라인) không đảm bảo meaningful oversight. Human-in-the-loop cần:

- người rà soát (review / 검토) có đủ thông tin (information / 정보);
- có authority để reject;
- tải công việc (workload / 워크로드) không quá lớn;
- thất bại (failure / 실패) consequence được hiểu;
- hệ thống (system / 시스템) không tạo pressure khiến approve trở thành default.

Nếu 99.9% suggestion đúng, vigilance của reviewer có thể giảm; đây là automation complacency bài toán (problem / 문제).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HCI, AI và hỗ trợ ra quyết định của con người**, **AI anthropomorphism** tiếp nhận điểm tựa từ **Human-in-the-loop thực sự nghĩa gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ví dụ: AI mã (code / 코드) assistant** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## AI anthropomorphism

Ngôn ngữ tự nhiên khiến con người dễ gán intention, understanding hoặc confidence cho mô hình (model / 모델). Một câu trả lời trôi chảy có thể tạo **fluency heuristic**: dễ đọc → có vẻ đúng.

Cần tách:

- linguistic fluency;
- factual accuracy;
- lập luận (reasoning / 추론) validity;
- nguồn (source / 소스) chất lượng (quality / 품질);
- bất định (uncertainty / 불확실성).

Xem thêm: [[../90_connections/02_human_ai_collaboration_trust_and_cognitive_offloading]], [[./17_misinformation_belief_revision_and_inoculation]].

> **Chuyển mạch:** Trong **HCI, AI và hỗ trợ ra quyết định của con người**, **AI anthropomorphism** cho ta quy tắc; **Ví dụ: AI mã (code / 코드) assistant** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ: AI mã (code / 코드) assistant

Một workflow tốt hơn “prompt rồi bản sao (copy / 복사)”:

```text
1. Người dùng xác định requirement và invariant.
2. AI đề xuất implementation nhỏ.
3. Người dùng đọc diff và giải thích logic.
4. Test tự động kiểm tra behavior.
5. Người dùng review edge case/security.
6. Chỉ sau đó mới mở rộng sang phần tiếp theo.
```

Ở đây AI làm giảm môi trường vận hành (production / 운영 환경) chi phí (cost / 비용) nhưng human vẫn giữ mô hình (model / 모델) của hệ thống (system / 시스템).

> **Chuyển mạch:** Ở chặng này của **HCI, AI và hỗ trợ ra quyết định của con người**, **Ví dụ: AI mã (code / 코드) assistant** cho ta quy tắc; **Dùng chung (common / 공통) Misconceptions** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“UX chỉ là làm đẹp.”** UX bao gồm cognitive tải (load / 로드), lỗi (error / 오류), quyết định (decision / 결정), điều hướng (navigation / 내비게이션), khả năng tiếp cận (accessibility / 접근성) và phản hồi (feedback / 피드백).

**“AI càng chính xác thì con người càng ít cần rà soát (review / 검토).”** rà soát (review / 검토) chiến lược (strategy / 전략) phụ thuộc cả accuracy, bất định (uncertainty / 불확실성), consequence và detectability của lỗi (error / 오류).

**“Có confidence score là giải quyết trust.”** người dùng (user / 사용자) cần hiểu score đại diện gì và có calibrated hay không.

**“Dùng AI sẽ chắc chắn làm con người ngu đi.”** Quá đơn giản. kết quả (outcome / 결과) phụ thuộc phần nào được offload, tác vụ (task / 작업) goal và cách người dùng vẫn thực hành retrieval/lập luận (reasoning / 추론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HCI, AI và hỗ trợ ra quyết định của con người**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Connections** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Một interactive hệ thống (system / 시스템) tốt không cố làm người dùng (user / 사용자) “ghi nhớ cách dùng”. Nó **phân bố cognition** hợp lý giữa người, giao diện (interface / 인터페이스), automation và môi trường (environment / 환경).

Câu hỏi thiết kế trung tâm:

> Phần nào con người nên quyết định, phần nào máy nên tính, và thông tin nào cần hiện ra để hai bên phối hợp đúng?

> **Chuyển mạch:** Trong **HCI, AI và hỗ trợ ra quyết định của con người**, **Connections** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Connections

Xem thêm:

- [[../02_learning_and_cognition/01_memory]];
- [[../02_learning_and_cognition/04_cognitive_biases_and_metacognition]];
- [[../02_learning_and_cognition/08_decision_under_risk_uncertainty_and_ambiguity]];
- [[../02_learning_and_cognition/10_cognitive_offloading_external_memory_and_extended_cognition]];
- [[../90_connections/02_human_ai_collaboration_trust_and_cognitive_offloading]];
- [[../90_connections/03_risk_uncertainty_and_science_communication]].

> **Bàn giao:** Sau **Connections**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
