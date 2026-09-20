# Computing ethics, privacy và professional responsibility

Software changes what people can know, do and control. Vì vậy engineer không chỉ chịu trách nhiệm “code đúng spec”; cần xem ai bị ảnh hưởng, harm nào có thể xảy ra và quyền/consent nào đang được dùng. Ethics không thay law, nhưng law cũng không bao phủ mọi responsible decision.

## Technical decision có value assumptions

Chọn default public/private, data retention 30 ngày hay vô hạn, notification opt-in hay opt-out đều steer behavior và distribute risk.

Một design có thể technically neutral-looking nhưng embed incentives/assumptions.

## Privacy không chỉ là secrecy

Privacy liên quan control/context của personal information: data nào được thu, mục đích gì, ai truy cập, giữ bao lâu, combine với nguồn nào.

Information có thể không secret nhưng aggregation/re-identification tạo harm mới.

## Data minimization

Thu thập ít data cần thiết giảm breach impact và governance burden. “Có thể hữu ích sau này” không luôn là justification tốt cho indefinite collection.

Minimization cũng là security principle: data không tồn tại thì không thể leak từ system đó.

## Consent

Consent có ý nghĩa khi informed, specific và reasonably voluntary. Dark patterns hoặc take-it-or-leave-it contexts có thể làm consent formality hơn là meaningful choice.

Engineering cần làm preference enforceable trong actual data flows, không chỉ checkbox UI.

## Purpose limitation

Data collected cho fraud prevention không tự động appropriate cho unrelated advertising. Repurposing thay risk/context và có thể cần new justification/consent tùy policy/law.

Data lineage giúp biết downstream systems đang dùng dataset nào cho purpose nào.

## Professional responsibility

Engineer có duty báo risk nghiêm trọng, không falsify test results và không hide known safety/security defects.

Trong high-stakes systems, pressure deadline không loại obligation escalate evidence.

Codes of ethics từ professional organizations cung cấp frameworks nhưng không tự giải mọi conflict.

## Dual use

Technology như encryption, facial recognition, vulnerability research và generative AI có beneficial + harmful uses. Responsible analysis xem plausible misuse, access controls, monitoring và publication strategy.

Không phải mọi misuse có thể prevent, nhưng “tool neutral nên không cần nghĩ” là insufficient.

## Whistleblowing và escalation

Khi harm/rule violation nghiêm trọng bị ignore, internal escalation, ethics/compliance/legal channels có thể cần dùng. External whistleblowing phụ thuộc jurisdiction, evidence và risk; đây không phải topic chỉ technical.

Điểm CS nền tảng: organization process là một safety control, giống code review nhưng cho societal risk.

## Common Misconceptions

**“Nếu hợp pháp thì chắc chắn ethical.”** Law đặt minimum/constraints nhưng có thể lag technology hoặc cho phép choices vẫn gây harm.

**“Privacy = encrypt database.”** Encryption chỉ một control; collection, access, retention và purpose vẫn matter.

**“Engineer không quyết product nên không có responsibility.”** Engineers biết implementation/risk details và có role communicate consequences.

## Mental Model

> Responsible computing hỏi không chỉ “system có hoạt động không?” mà “hoạt động cho ai, với dữ liệu/quyền lực nào, và ai chịu cost khi assumptions sai?”

## Kết nối

Đọc [security principles](../07_security_reliability/00_threat_models_and_security_principles.md), [HCI/dark patterns](../11_hci_graphics/01_interface_design_accessibility_and_usability.md), [AI evaluation](../10_ai_foundations/04_ai_evaluation_data_and_responsibility.md) và [data governance](./01_data_governance_bias_and_algorithmic_impact.md).