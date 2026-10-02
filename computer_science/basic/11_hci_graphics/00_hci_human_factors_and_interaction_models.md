# Human-Computer tương tác (interaction / 상호작용), human factors và tương tác (interaction / 상호작용) các mô hình (models / 모델들)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Human-computer interaction, human factors và interaction models**. Route đi từ user-in-system → mental models/affordance → feedback/gulf of execution → attention/Fitts/Hick → slips, mistakes và direct manipulation, để thiết kế bám vào hành vi thật.

Human-Computer tương tác (interaction / 상호작용) nghiên cứu cách con người hiểu, điều khiển và hình thành mô hình tư duy (mental model / 사고 모델) về computer các hệ thống (systems / 시스템들). Một giao diện (interface / 인터페이스) technically correct vẫn có thể gây lỗi nếu người dùng (user / 사용자) không biết hệ thống (system / 시스템) trạng thái (state / 상태), hành động (action / 동작) consequences hoặc khôi phục (recovery / 복구) đường dẫn (path / 경로).

## Người dùng (user / 사용자) là một phần của hệ thống (system / 시스템)

Trong interactive software, đầu ra (output / 출력) không kết thúc computation; nó thay đổi perception của người dùng (user / 사용자), người dùng (user / 사용자) chọn hành động (action / 동작) mới rồi hệ thống (system / 시스템) tiếp tục. Đây là vòng phản hồi (feedback loop / 피드백 루프).

Vì vậy usability bug có thể trở thành tính đúng đắn (correctness / 정확성)/an toàn (safety / 안전) bug. Nếu banking UI làm người dùng (user / 사용자) nhầm beneficiary hoặc medical UI che warning quan trọng, bài toán (problem / 문제) không còn là “mỹ thuật”.

> **Chuyển mạch:** Trong **Human-Computer tương tác (interaction / 상호작용), human factors và tương tác (interaction / 상호작용) các mô hình (models / 모델들)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Người dùng (user / 사용자) là một phần của hệ thống (system / 시스템)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Affordance và signifier** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Người dùng (user / 사용자) xây mô hình tư duy (mental model / 사고 모델) từ labels, bố cục (layout / 레이아웃), phản hồi (feedback / 피드백) và prior experience. giao diện (interface / 인터페이스) dễ dùng khi mô hình (model / 모델) người dùng (user / 사용자) hình thành gần với hành vi (behavior / 동작) thực đủ để dự đoán kết quả actions.

Nếu button “Save” đôi lúc lưu cloud, đôi lúc cục bộ (local / 로컬) draft, mô hình tư duy (mental model / 사고 모델) không ổn định. Consistency giảm học tập (learning / 학습) chi phí (cost / 비용) vì cùng cue → cùng expectation.

> **Chuyển mạch:** Ở chặng này của **Human-Computer tương tác (interaction / 상호작용), human factors và tương tác (interaction / 상호작용) các mô hình (models / 모델들)**, **Affordance và signifier** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Phản hồi (feedback / 피드백)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Affordance và signifier

Affordance là hành động (action / 동작) possibilities của đối tượng (object / 객체); signifier là cue cho người dùng (user / 사용자) biết hành động (action / 동작) đó có thể thực hiện.

Một icon không label có thể có affordance click nhưng signifier meaning kém. HCI quan tâm cả khả năng thao tác lẫn khả năng nhận biết.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Human-Computer tương tác (interaction / 상호작용), human factors và tương tác (interaction / 상호작용) các mô hình (models / 모델들)**, **Phản hồi (feedback / 피드백)** tiếp nhận điểm tựa từ **Affordance và signifier** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gulf of thực thi (execution / 실행) và evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phản hồi (feedback / 피드백)

Hành động (action / 동작) cần phản hồi (feedback / 피드백) tương xứng độ trễ (latency / 지연 시간). Nếu save mất 2 giây nhưng UI im lặng, người dùng (user / 사용자) có thể click lại và tạo duplicate.

Loading indicator, disabled button hoặc optimistic UI là các strategies khác nhau. phản hồi (feedback / 피드백) phải phản ánh bất định (uncertainty / 불확실성)/trạng thái (state / 상태) thật, không chỉ animation.

> **Chuyển mạch:** Trong **Human-Computer tương tác (interaction / 상호작용), human factors và tương tác (interaction / 상호작용) các mô hình (models / 모델들)**, **Gulf of thực thi (execution / 실행) và evaluation** tiếp nhận điểm tựa từ **Phản hồi (feedback / 피드백)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Human attention và working bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gulf of thực thi (execution / 실행) và evaluation

Gulf of thực thi (execution / 실행) là khoảng cách giữa goal người dùng (user / 사용자) và actions giao diện (interface / 인터페이스) cung cấp. Gulf of evaluation là khoảng cách giữa hệ thống (system / 시스템) trạng thái (state / 상태) và khả năng người dùng (user / 사용자) hiểu trạng thái (state / 상태) đó.

Good thiết kế (design / 설계) giảm cả hai: hành động (action / 동작) discoverable, kết quả (result / 결과) interpretable.

> **Chuyển mạch:** Ở chặng này của **Human-Computer tương tác (interaction / 상호작용), human factors và tương tác (interaction / 상호작용) các mô hình (models / 모델들)**, **Human attention và working bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Gulf of thực thi (execution / 실행) và evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fitts's Law** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Human attention và working bộ nhớ (memory / 메모리)

Working bộ nhớ (memory / 메모리) hữu hạn. giao diện (interface / 인터페이스) buộc nhớ mã từ màn hình trước hoặc compare nhiều values không visible tăng cognitive tải (load / 로드).

Recognition thường dễ hơn recall. Dropdown/lịch sử (history / 이력)/autocomplete có thể giảm need nhớ chính xác.

Nhưng quá nhiều choices visible lại tăng visual/tìm kiếm (search / 검색) tải (load / 로드); thiết kế (design / 설계) phải balance.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Human-Computer tương tác (interaction / 상호작용), human factors và tương tác (interaction / 상호작용) các mô hình (models / 모델들)**, **Fitts's Law** tiếp nhận điểm tựa từ **Human attention và working bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hick–Hyman intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fitts's Law

Fitts's Law mô hình thời gian trỏ tới mục tiêu (target / 대상) phụ thuộc distance và mục tiêu (target / 대상) kích thước (size / 크기) gần theo:

\[
T = a + b\log_2(1 + D/W)
\]

với `D` là khoảng cách và `W` effective mục tiêu (target / 대상) width.

Insight: mục tiêu (target / 대상) quan trọng nên đủ lớn và placement thuận tiện. Screen edges/corners có effective targeting advantage trong pointer interfaces vì cursor không overshoot ranh giới (boundary / 경계).

> **Chuyển mạch:** Trong **Human-Computer tương tác (interaction / 상호작용), human factors và tương tác (interaction / 상호작용) các mô hình (models / 모델들)**, **Hick–Hyman intuition** tiếp nhận điểm tựa từ **Fitts's Law** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Errors: slips và mistakes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hick–Hyman intuition

Quyết định (decision / 결정) thời gian (time / 시간) thường tăng khi number/bất định (uncertainty / 불확실성) của choices tăng. Nhưng không có nghĩa luôn giảm menu items; grouping, hierarchy và familiarity thay đổi effective quyết định (decision / 결정) độ phức tạp (complexity / 복잡도).

> **Chuyển mạch:** Ở chặng này của **Human-Computer tương tác (interaction / 상호작용), human factors và tương tác (interaction / 상호작용) các mô hình (models / 모델들)**, **Errors: slips và mistakes** tiếp nhận điểm tựa từ **Hick–Hyman intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Direct manipulation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Errors: slips và mistakes

Slip xảy ra khi goal đúng nhưng hành động (action / 동작) sai, như click nhầm delete. Mistake xảy ra khi mô hình tư duy (mental model / 사고 모델)/goal selection sai.

Prevention khác nhau: slip giảm bằng spacing, undo, confirmation cho irreversible hành động (action / 동작); mistake giảm bằng clearer mô hình (model / 모델), explanation và các ràng buộc (constraints / 제약조건들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Human-Computer tương tác (interaction / 상호작용), human factors và tương tác (interaction / 상호작용) các mô hình (models / 모델들)**, **Direct manipulation** tiếp nhận điểm tựa từ **Errors: slips và mistakes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Direct manipulation

Dragging đối tượng (object / 객체), resizing visual item và immediate phản hồi (feedback / 피드백) tạo cảm giác thao tác trực tiếp trên lĩnh vực (domain / 도메인) đối tượng (object / 객체). Nó mạnh cho spatial tasks nhưng không luôn phù hợp automation/batch operations.

Command interfaces có học tập (learning / 학습) chi phí (cost / 비용) cao hơn nhưng composability/efficiency tốt cho experts. UI thiết kế (design / 설계) phải xem người dùng (user / 사용자)/tác vụ (task / 작업) phân phối (distribution / 분포).

> **Chuyển mạch:** Trong **Human-Computer tương tác (interaction / 상호작용), human factors và tương tác (interaction / 상호작용) các mô hình (models / 모델들)**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Direct manipulation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“UX là làm giao diện đẹp.”** HCI quan tâm cognition, lỗi (error / 오류), learnability, efficiency và phản hồi (feedback / 피드백), không chỉ aesthetics.

**“người dùng (user / 사용자) lỗi (error / 오류) là lỗi người dùng (user / 사용자).”** Repeated predictable lỗi (error / 오류) mẫu (pattern / 패턴) thường cho thấy hệ thống (system / 시스템) thiết kế (design / 설계) không phù hợp human các ràng buộc (constraints / 제약조건들).

**“Ít click hơn luôn tốt.”** Một click nguy hiểm/khó hiểu có thể tệ hơn luồng (flow / 흐름) nhiều bước nhưng rõ ràng.

> **Chuyển mạch:** Ở chặng này của **Human-Computer tương tác (interaction / 상호작용), human factors và tương tác (interaction / 상호작용) các mô hình (models / 모델들)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Interactive hệ thống (system / 시스템) là closed vòng phản hồi (feedback loop / 피드백 루프) giữa machine trạng thái (state / 상태) và human perception/hành động (action / 동작). thiết kế (design / 설계) tốt làm trạng thái (state / 상태), available actions và consequences legible.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Human-Computer tương tác (interaction / 상호작용), human factors và tương tác (interaction / 상호작용) các mô hình (models / 모델들)**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc [interface/accessibility/usability](./01_interface_design_accessibility_and_usability.md), [requirements](../09_software_engineering/00_requirements_specification_and_engineering_process.md) và [AI human-in-the-loop](../10_ai_foundations/04_ai_evaluation_data_and_responsibility.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
