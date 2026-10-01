# Computing ethics, privacy và professional responsibility

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Computing ethics, privacy và professional responsibility**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Technical quyết định (decision / 결정) có giá trị (value / 값) các giả định (assumptions / 가정들)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Privacy không chỉ là secrecy** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Software changes what people can know, do and điều khiển (control / 제어). Vì vậy engineer không chỉ chịu trách nhiệm “mã (code / 코드) đúng spec”; cần xem ai bị ảnh hưởng, harm nào có thể xảy ra và quyền/consent nào đang được dùng. Ethics không thay law, nhưng law cũng không bao phủ mọi responsible quyết định (decision / 결정).

## Technical quyết định (decision / 결정) có giá trị (value / 값) các giả định (assumptions / 가정들)

Chọn default công khai (public / 공개)/private, dữ liệu (data / 데이터) retention 30 ngày hay vô hạn, notification opt-in hay opt-out đều steer hành vi (behavior / 동작) và distribute rủi ro (risk / 위험).

Một thiết kế (design / 설계) có thể technically neutral-looking nhưng embed incentives/các giả định (assumptions / 가정들).

> **Chuyển mạch:** Technical decisions embed value assumptions; privacy rộng hơn secrecy vì liên quan quyền kiểm soát và context, nên data minimization là nguyên tắc thiết kế tiếp theo.

## Privacy không chỉ là secrecy

Privacy liên quan điều khiển (control / 제어)/ngữ cảnh (context / 맥락) của personal thông tin (information / 정보): dữ liệu (data / 데이터) nào được thu, mục đích gì, ai truy cập, giữ bao lâu, combine với nguồn nào.

Thông tin (information / 정보) có thể không secret nhưng aggregation/re-identification tạo harm mới.

> **Chuyển mạch:** Ở chặng này của **Computing ethics, privacy và professional responsibility**, **Privacy không chỉ là secrecy** nêu điều cần giải thích; **Dữ liệu (data / 데이터) minimization** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Consent** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) minimization

Thu thập ít dữ liệu (data / 데이터) cần thiết giảm breach impact và quản trị (governance / 거버넌스) burden. “Có thể hữu ích sau này” không luôn là justification tốt cho indefinite collection.

Minimization cũng là bảo mật (security / 보안) principle: dữ liệu (data / 데이터) không tồn tại thì không thể leak từ hệ thống (system / 시스템) đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Computing ethics, privacy và professional responsibility**, **Dữ liệu (data / 데이터) minimization** nêu điều cần giải thích; **Consent** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Purpose limitation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Consent

Consent có ý nghĩa khi informed, specific và reasonably voluntary. Dark patterns hoặc take-it-or-leave-it contexts có thể làm consent formality hơn là meaningful choice.

Kỹ thuật (engineering / 엔지니어링) cần làm preference enforceable trong actual dữ liệu (data / 데이터) flows, không chỉ checkbox UI.

> **Chuyển mạch:** Trong **Computing ethics, privacy và professional responsibility**, **Consent** đã nêu tiêu chí phân biệt, còn **Purpose limitation** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Professional responsibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Purpose limitation

Dữ liệu (data / 데이터) collected cho fraud prevention không tự động appropriate cho unrelated advertising. Repurposing thay rủi ro (risk / 위험)/ngữ cảnh (context / 맥락) và có thể cần new justification/consent tùy chính sách (policy / 정책)/law.

Dữ liệu (data / 데이터) lineage giúp biết downstream các hệ thống (systems / 시스템들) đang dùng dataset nào cho purpose nào.

> **Chuyển mạch:** Ở chặng này của **Computing ethics, privacy và professional responsibility**, **Purpose limitation** đã nêu tiêu chí phân biệt, còn **Professional responsibility** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Dual use** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Professional responsibility

Engineer có duty báo rủi ro (risk / 위험) nghiêm trọng, không falsify kiểm thử (test / 테스트) results và không hide known an toàn (safety / 안전)/bảo mật (security / 보안) defects.

Trong high-stakes các hệ thống (systems / 시스템들), pressure deadline không loại obligation escalate bằng chứng (evidence / 증거).

Codes of ethics từ professional organizations cung cấp frameworks nhưng không tự giải mọi xung đột (conflict / 충돌).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Computing ethics, privacy và professional responsibility**, **Dual use** tiếp nhận điểm tựa từ **Professional responsibility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Whistleblowing và escalation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dual use

Technology như encryption, facial recognition, vulnerability research và generative AI có beneficial + harmful uses. Responsible phân tích (analysis / 분석) xem plausible misuse, truy cập (access / 접근) controls, monitoring và publication chiến lược (strategy / 전략).

Không phải mọi misuse có thể prevent, nhưng “công cụ (tool / 도구) neutral nên không cần nghĩ” là insufficient.

> **Chuyển mạch:** Trong **Computing ethics, privacy và professional responsibility**, **Whistleblowing và escalation** tiếp nhận điểm tựa từ **Dual use** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Whistleblowing và escalation

Khi harm/quy tắc (rule / 규칙) violation nghiêm trọng bị ignore, nội bộ (internal / 내부) escalation, ethics/compliance/legal channels có thể cần dùng. bên ngoài (external / 외부) whistleblowing phụ thuộc jurisdiction, bằng chứng (evidence / 증거) và rủi ro (risk / 위험); đây không phải topic chỉ technical.

Điểm CS nền tảng: organization tiến trình (process / 프로세스) là một an toàn (safety / 안전) điều khiển (control / 제어), giống rà soát mã (code review / 코드 리뷰) nhưng cho societal rủi ro (risk / 위험).

> **Chuyển mạch:** Ở chặng này của **Computing ethics, privacy và professional responsibility**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Whistleblowing và escalation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Nếu hợp pháp thì chắc chắn ethical.”** Law đặt minimum/các ràng buộc (constraints / 제약조건들) nhưng có thể lag technology hoặc cho phép choices vẫn gây harm.

**“Privacy = encrypt cơ sở dữ liệu (database / 데이터베이스).”** Encryption chỉ một điều khiển (control / 제어); collection, truy cập (access / 접근), retention và purpose vẫn matter.

**“Engineer không quyết sản phẩm (product / 제품) nên không có responsibility.”** Engineers biết hiện thực (implementation / 구현)/rủi ro (risk / 위험) details và có role communicate consequences.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Computing ethics, privacy và professional responsibility**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Responsible computing hỏi không chỉ “hệ thống (system / 시스템) có hoạt động không?” mà “hoạt động cho ai, với dữ liệu/quyền lực nào, và ai chịu chi phí (cost / 비용) khi các giả định (assumptions / 가정들) sai?”

> **Chuyển mạch:** Trong **Computing ethics, privacy và professional responsibility**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc [security principles](../07_security_reliability/00_threat_models_and_security_principles.md), [HCI/dark patterns](../11_hci_graphics/01_interface_design_accessibility_and_usability.md), [AI evaluation](../10_ai_foundations/04_ai_evaluation_data_and_responsibility.md) và [data governance](./01_data_governance_bias_and_algorithmic_impact.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
