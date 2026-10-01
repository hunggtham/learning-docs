# Giao diện (interface / 인터페이스) thiết kế (design / 설계), khả năng tiếp cận (accessibility / 접근성) và usability

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Giao diện (interface / 인터페이스) thiết kế (design / 설계), khả năng tiếp cận (accessibility / 접근성) và usability**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Usability theo tác vụ (task / 작업) và người dùng (user / 사용자)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Thông tin (information / 정보) kiến trúc (architecture / 아키텍처)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Usability không phải cảm giác chủ quan hoàn toàn. Ta có thể quan sát tác vụ (task / 작업) completion, lỗi (error / 오류) tỷ lệ (rate / 비율), thời gian (time / 시간), learnability và satisfaction. khả năng tiếp cận (accessibility / 접근성) mở rộng câu hỏi: giao diện (interface / 인터페이스) có usable với người có năng lực giác quan, vận động, nhận thức và thiết bị khác nhau hay không?

## Usability theo tác vụ (task / 작업) và người dùng (user / 사용자)

Một giao diện (interface / 인터페이스) nhanh cho expert operator có thể khó cho novice. Command line hiệu quả cho repetitive automation nhưng không discoverable như GUI.

Vì vậy “dễ dùng” luôn cần ngữ cảnh (context / 맥락): ai, làm tác vụ (task / 작업) gì, tần suất nào, lỗi (error / 오류) chi phí (cost / 비용) bao nhiêu.

> **Chuyển mạch:** Trong **Giao diện (interface / 인터페이스) thiết kế (design / 설계), khả năng tiếp cận (accessibility / 접근성) và usability**, **Thông tin (information / 정보) kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **Usability theo tác vụ (task / 작업) và người dùng (user / 사용자)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Visual hierarchy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thông tin (information / 정보) kiến trúc (architecture / 아키텍처)

Điều hướng (navigation / 내비게이션) tốt phản ánh cách users phân loại goals, không nhất thiết cách cơ sở dữ liệu (database / 데이터베이스) tables hoặc organization departments được chia.

Card sorting, cây (tree / 트리) testing và tìm kiếm (search / 검색) logs có thể giúp kiểm mô hình (model / 모델) categories.

> **Chuyển mạch:** Ở chặng này của **Giao diện (interface / 인터페이스) thiết kế (design / 설계), khả năng tiếp cận (accessibility / 접근성) và usability**, **Visual hierarchy** tiếp nhận điểm tựa từ **Thông tin (information / 정보) kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Form thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Visual hierarchy

Kích thước (size / 크기), spacing, position, contrast và grouping hướng attention. Gestalt principles như proximity/similarity giúp người dùng (user / 사용자) nhận groups mà không cần border mọi thứ.

Visual hierarchy không chỉ aesthetic; nó encode priority và relationship.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Giao diện (interface / 인터페이스) thiết kế (design / 설계), khả năng tiếp cận (accessibility / 접근성) và usability**, **Form thiết kế (design / 설계)** tiếp nhận điểm tựa từ **Visual hierarchy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khả năng tiếp cận (accessibility / 접근성) không phải add-on cuối dự án** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Form thiết kế (design / 설계)

Forms cần labels rõ, đầu vào (input / 입력) các ràng buộc (constraints / 제약조건들), lỗi (error / 오류) message gần trường dữ liệu (field / 필드) và preserve entered dữ liệu (data / 데이터) khi kiểm tra hợp lệ (validation / 검증) thất bại (fail / 실패).

Kiểm tra hợp lệ (validation / 검증) sớm giúp phản hồi (feedback / 피드백) nhưng server-side kiểm tra hợp lệ (validation / 검증) vẫn bắt buộc vì máy khách (client / 클라이언트) không trusted.

Good lỗi (error / 오류) message nói điều gì sai và cách sửa, không chỉ “Invalid đầu vào (input / 입력)”.

> **Chuyển mạch:** Trong **Giao diện (interface / 인터페이스) thiết kế (design / 설계), khả năng tiếp cận (accessibility / 접근성) và usability**, **Khả năng tiếp cận (accessibility / 접근성) không phải add-on cuối dự án** tiếp nhận điểm tựa từ **Form thiết kế (design / 설계)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Keyboard và focus** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khả năng tiếp cận (accessibility / 접근성) không phải add-on cuối dự án

Ngữ nghĩa (semantic / 의미적) HTML, keyboard điều hướng (navigation / 내비게이션), focus thứ tự (order / 순서), văn bản (text / 텍스트) alternatives, contrast và scalable văn bản (text / 텍스트) ảnh hưởng kiến trúc (architecture / 아키텍처)/thành phần (component / 컴포넌트) thiết kế (design / 설계) từ đầu.

Screen reader dựa cây khả năng tiếp cận (accessibility tree / 접근성 트리)/ngữ nghĩa (semantics / 의미론), không “nhìn điểm ảnh (pixel / 픽셀)” như người sighted.

> **Chuyển mạch:** Ở chặng này của **Giao diện (interface / 인터페이스) thiết kế (design / 설계), khả năng tiếp cận (accessibility / 접근성) và usability**, **Keyboard và focus** tiếp nhận điểm tựa từ **Khả năng tiếp cận (accessibility / 접근성) không phải add-on cuối dự án** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Color** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Keyboard và focus

Interactive controls phải reachable bằng keyboard nếu use trường hợp (case / 사례)/nền tảng (platform / 플랫폼) yêu cầu. Focus indicator cho biết hiện tại (current / 현재) mục tiêu (target / 대상); modal phải quản lý focus entry/trap/return hợp lý.

Custom clickable `div` thường thiếu keyboard ngữ nghĩa (semantics / 의미론) và accessible role nếu nhà phát triển (developer / 개발자) không thêm đúng hành vi (behavior / 동작).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Giao diện (interface / 인터페이스) thiết kế (design / 설계), khả năng tiếp cận (accessibility / 접근성) và usability**, **Color** tiếp nhận điểm tựa từ **Keyboard và focus** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Responsive thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Color

Không nên dùng color là channel duy nhất truyền trạng thái vì color-vision differences và monochrome/high-contrast modes.

Lỗi (error / 오류) có thể dùng icon/văn bản (text / 텍스트) + color. Contrast cần đủ theo khả năng tiếp cận (accessibility / 접근성) guidelines tương ứng, nhưng chính xác (exact / 정확한) threshold phụ thuộc tiêu chuẩn (standard / 표준)/ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Trong **Giao diện (interface / 인터페이스) thiết kế (design / 설계), khả năng tiếp cận (accessibility / 접근성) và usability**, **Responsive thiết kế (design / 설계)** tiếp nhận điểm tựa từ **Color** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Người dùng (user / 사용자) testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Responsive thiết kế (design / 설계)

Responsive không chỉ shrink desktop UI. Small touch screen có mục tiêu (target / 대상) kích thước (size / 크기), thumb reach, virtual keyboard và mạng (network / 네트워크) các ràng buộc (constraints / 제약조건들) khác.

Bố cục (layout / 레이아웃)/content priority có thể cần thay đổi, không chỉ CSS scaling.

> **Chuyển mạch:** Ở chặng này của **Giao diện (interface / 인터페이스) thiết kế (design / 설계), khả năng tiếp cận (accessibility / 접근성) và usability**, **Người dùng (user / 사용자) testing** tiếp nhận điểm tựa từ **Responsive thiết kế (design / 설계)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **A/B testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Người dùng (user / 사용자) testing

Quan sát representative users làm representative tasks phát hiện mismatches mà nhóm (team / 팀) quen sản phẩm không thấy.

5 users không phải magic number cho mọi research. cỡ mẫu (sample size / 표본 크기) phụ thuộc goal, variability và statistical vs qualitative phương thức (method / 메서드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Giao diện (interface / 인터페이스) thiết kế (design / 설계), khả năng tiếp cận (accessibility / 접근성) và usability**, **A/B testing** tiếp nhận điểm tựa từ **Người dùng (user / 사용자) testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dark patterns** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## A/B testing

A/B kiểm thử (test / 테스트) đo nhân quả (causal / 인과적) tác động (effect / 효과) của giao diện (interface / 인터페이스) variant nếu randomization/metrics đúng. Nhưng cục bộ (local / 로컬) chỉ số (metric / 지표) tăng có thể hại long-term kết quả (outcome / 결과).

Ví dụ tăng notification clicks không đồng nghĩa tăng người dùng (user / 사용자) well-being. chỉ số (metric / 지표) cần guardrails.

> **Chuyển mạch:** Trong **Giao diện (interface / 인터페이스) thiết kế (design / 설계), khả năng tiếp cận (accessibility / 접근성) và usability**, **Dark patterns** tiếp nhận điểm tựa từ **A/B testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dark patterns

Dark mẫu (pattern / 패턴) dùng asymmetry/confusion để steer người dùng (user / 사용자) chống lợi ích/preferences của họ, như khó cancel hơn subscribe hoặc hidden fees.

Đây là intersection HCI và ethics: thiết kế (design / 설계) effectiveness không tự đồng nghĩa thiết kế (design / 설계) responsibility.

> **Chuyển mạch:** Ở chặng này của **Giao diện (interface / 인터페이스) thiết kế (design / 설계), khả năng tiếp cận (accessibility / 접근성) và usability**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Dark patterns** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“khả năng tiếp cận (accessibility / 접근성) chỉ dành cho một nhóm nhỏ.”** Temporary injury, aging, bright sunlight, one-handed use và poor mạng (network / 네트워크) tạo situational khả năng tiếp cận (accessibility / 접근성) needs rộng.

**“ngữ nghĩa (semantic / 의미적) HTML chỉ tốt cho SEO.”** Nó hỗ trợ khả năng tiếp cận (accessibility / 접근성), trình duyệt (browser / 브라우저) hành vi (behavior / 동작) và maintainability.

**“A/B kiểm thử (test / 테스트) thắng nghĩa thiết kế (design / 설계) tốt hơn.”** Chỉ với chỉ số (metric / 지표)/horizon/population đã chọn; cần interpret broader effects.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Giao diện (interface / 인터페이스) thiết kế (design / 설계), khả năng tiếp cận (accessibility / 접근성) và usability**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> giao diện (interface / 인터페이스) là một information-and-action kiến trúc (architecture / 아키텍처). khả năng tiếp cận (accessibility / 접근성) tốt làm ngữ nghĩa (semantics / 의미론)/actions survive across different bodies, devices và assistive technologies.

> **Chuyển mạch:** Trong **Giao diện (interface / 인터페이스) thiết kế (design / 설계), khả năng tiếp cận (accessibility / 접근성) và usability**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc [HCI/human factors](./00_hci_human_factors_and_interaction_models.md), [web security](../07_security_reliability/06_web_application_security.md) và [computing ethics](../12_society_ethics_profession/00_computing_ethics_privacy_and_professional_responsibility.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
