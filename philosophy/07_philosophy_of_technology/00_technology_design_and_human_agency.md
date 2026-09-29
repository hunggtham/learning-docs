# Technology, thiết kế (design / 설계) và Human Agency

> **Mạch đọc:** Đọc **Technology, thiết kế (design / 설계) và Human Agency** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Các câu hỏi kiểm tra** sang **trường hợp (case / 사례): recommendation hệ thống (system / 시스템)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Technology không chỉ là vật thể trung tính nằm ngoài xã hội. Thiết kế quyết định affordance, default, visibility, chi phí (cost / 비용) of hành động (action / 동작) và ai có quyền sửa hệ thống. Tuy vậy, nói “technology tự quyết định mọi thứ” cũng sai: institutions, users, incentives và regulation cùng định hình kết quả (outcome / 결과).

## Các câu hỏi kiểm tra

1. Hệ thống làm cho hành động nào dễ hoặc khó hơn?
2. dữ liệu (data / 데이터), classification và chỉ số (metric / 지표) đại diện cho ai, bỏ sót ai?
3. Ai chịu benefit, rủi ro (risk / 위험), lỗi (error / 오류) và chi phí giám sát?
4. Automation thay thế tác vụ (task / 작업) hay chuyển quyền quyết định sang một actor khó thấy?
5. Có appeal, contestability, reversibility và human accountability không?

Trong AI, accuracy không đủ để quyết định triển khai (deployment / 배포). Cần xem mục tiêu (objective / 목표), proxy, phân phối (distribution / 분포) shift, bất định (uncertainty / 불확실성), human oversight và giá trị (value / 값) sự đánh đổi (trade-off / 트레이드오프). “Human in the vòng lặp (loop / 루프)” chỉ có ý nghĩa nếu con người có thông tin, quyền can thiệp và thời gian để thực sự sửa quyết định.

Liên hệ với [Computer Science](../../computer_science/README.md), [AI](../../computer_science/02_artificial_intelligence/README.md) và [Psychology về human–AI collaboration](../../psychology/90_connections/02_human_ai_collaboration_trust_and_cognitive_offloading.md).


> **Chuyển mạch:** Từ **Các câu hỏi kiểm tra**, ta sang **trường hợp (case / 사례): recommendation hệ thống (system / 시스템)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trường hợp (case / 사례): recommendation hệ thống (system / 시스템)

Một recommender tối ưu watch thời gian (time / 시간) có thể làm tăng engagement nhưng thay đổi attention, exposure diversity và beliefs. Để đánh giá, không chỉ hỏi mô hình (model / 모델) có accurate không; cần hỏi mục tiêu (objective / 목표), vòng phản hồi (feedback loop / 피드백 루프), population-level externality, người dùng (user / 사용자) understanding, opt-out, vulnerable users và khả năng kiểm tra (audit / 감사). Nếu người dùng thích nội dung do hệ thống liên tục cho xem, preference quan sát được vừa là đầu vào (input / 입력) vừa là sản phẩm của thiết kế (design / 설계).


> **Chuyển mạch:** Từ **trường hợp (case / 사례): recommendation hệ thống (system / 시스템)**, ta sang **Agency dưới automation** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Agency dưới automation

Human agency không chỉ là còn một nút “approve”. Người duyệt cần thấy bất định (uncertainty / 불확실성), alternatives, reason codes và có quyền override mà không bị penalty ngầm. Nếu tải công việc (workload / 워크로드) khiến mọi người rubber-stamp đầu ra (output / 출력), oversight trên giấy trở thành automation độ lệch (bias / 편향). Thiết kế có trách nhiệm phải phân bổ cả quyền quyết định, năng lực hiểu và nghĩa vụ giải trình.


> **Chuyển mạch:** Từ **Agency dưới automation**, ta sang **độ sâu (depth / 깊이) pass: technology, agency và quyền lực được vật chất hóa** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Độ sâu (depth / 깊이) pass: technology, agency và quyền lực được vật chất hóa

### Question và definitions

Technology vừa là sản phẩm tạo ra (artifact / 산출물), practice, hạ tầng (infrastructure / 인프라) và institution. Agency không chỉ là “có nút override”; nó cần thông tin (information / 정보), competence, thời gian (time / 시간), alternative và freedom from retaliation. thiết kế (design / 설계) làm một số hành động (action / 동작) rẻ/dễ, một số hành động (action / 동작) đắt/khó, qua đó phân bổ power trước cả khi có chính sách (policy / 정책).

### Strongest argument và premises

Technological mediation argument nói sản phẩm tạo ra (artifact / 산출물) hình thành perception và habit; social-shaping rival nhấn mạnh procurement, labor, law và người dùng (user / 사용자) adaptation. Một claim về độ lệch (bias / 편향) cần nêu construct, population, chỉ số (metric / 지표), baseline và vòng phản hồi (feedback loop / 피드백 루프). Accuracy chỉ là một thuộc tính (property / 속성); legitimacy còn cần purpose, contestability, privacy, an toàn (safety / 안전) và phân phối (distribution / 분포) of lỗi (error / 오류).

### Objection, reply và primary-source ngữ cảnh (context / 맥락)

Objection với “technology is political” là thiết kế không tự quyết định kết quả (outcome / 결과): cùng công cụ (tool / 도구) có thể có quản trị (governance / 거버넌스) khác. Reply: non-determinism không có nghĩa neutrality; defaults và hạ tầng (infrastructure / 인프라) tạo switching chi phí (cost / 비용) và đường dẫn (path / 경로) dependence. Primary-source ngữ cảnh (context / 맥락) từ Winner và STS tradition hữu ích để đặt câu hỏi về built-in politics, nhưng phải kiểm tra bằng triển khai (deployment / 배포) bằng chứng (evidence / 증거) chứ không coi lý thuyết (theory / 이론) là trường hợp (case / 사례).

### Empirical ranh giới (boundary / 경계) và implication

Kiểm tra (audit / 감사) cần kiểm thử (test / 테스트) phân phối (distribution / 분포) shift, human tải công việc (workload / 워크로드), automation độ lệch (bias / 편향), opt-out, appeal và second-order effects. “Human in the vòng lặp (loop / 루프)” chỉ có nghĩa khi override thực tế, reason mã (code / 코드) và liability rõ. Implication: deploy theo staged/reversible đường dẫn (path / 경로), log decisions, cho phép independent kiểm tra (audit / 감사) và thiết kế exit; agency cần được đo trong ngữ cảnh (context / 맥락) chứ không suy ra từ giao diện.

> **Bàn giao:** Sau **Empirical ranh giới (boundary / 경계) và implication**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 technology ethics data and automation](./01_technology_ethics_data_and_automation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
