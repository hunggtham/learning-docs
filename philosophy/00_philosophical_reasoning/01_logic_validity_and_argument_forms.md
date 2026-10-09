# Lô-gic (logic / 논리), Validity và các dạng lập luận

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Lô-gic (logic / 논리), Validity và các dạng lập luận**. Route đi từ mệnh đề và cấu trúc → validity/soundness → deduction, induction và abduction → điều kiện phản ví dụ, để tách một suy luận hợp lệ khỏi tiền đề đúng hoặc kết luận đáng tin trong thực tế.

## Validity không phải truth

Một argument **hợp lệ (valid)** khi conclusion buộc phải đúng nếu tất cả premise đúng. Validity chỉ xét cấu trúc; soundness mới thêm yêu cầu premise đáng tin hoặc đúng.

```text
Nếu P thì Q.
P.
Vậy Q.                 modus ponens — valid

Nếu P thì Q.
Q.
Vậy P.                 affirming the consequent — invalid
```

Dạng thứ hai có thể cho conclusion đúng trong một trường hợp cụ thể, nhưng không được premise bảo đảm: Q có thể có nguyên nhân khác. Đây là lỗi thường gặp khi đọc correlation như causation.

> **Chuyển mạch:** Validity chỉ nói cấu trúc suy luận có bảo toàn kết luận hay không, không bảo đảm tiền đề đúng. Vì deduction, induction và abduction dựa trên những tiêu chuẩn khác nhau, phần kế tiếp sẽ so sánh phạm vi và điểm yếu của từng kiểu.

## Deduction, induction và abduction

- **Deduction** bảo toàn tính đúng theo cấu trúc: từ quy tắc (rule / 규칙) và trường hợp (case / 사례) suy ra consequence.
- **Induction** mở rộng từ observations hữu hạn sang mẫu (pattern / 패턴) tổng quát; conclusion có độ tin cậy chứ không certainty.
- **Abduction** chọn explanation tốt nhất cho bằng chứng (evidence / 증거) hiện có; “tốt nhất” cần nói rõ tiêu chuẩn như fit, simplicity, phạm vi (scope / 범위) và khả năng kiểm tra.

Không dạng nào tự giải quyết mọi vấn đề. Deduction có thể vận hành trên premise sai; induction nhạy với mẫu (sample / 표본) và cơ sở (base / 기반) tỷ lệ (rate / 비율); abduction có thể chọn explanation đẹp nhưng chưa đủ discriminating bằng chứng (evidence / 증거).

> **Chuyển mạch:** Deduction kiểm tra hệ quả theo cấu trúc, induction đánh giá mức khái quát từ mẫu hữu hạn, còn abduction so sánh các lời giải thích cạnh tranh. Trước khi phản biện, ta cần steelman lập luận đối phương và xác định đúng nghĩa vụ chứng minh thay vì công kích một phiên bản yếu hơn.

## Steelman và burden of proof

Trước khi phản biện, hãy viết phiên bản mạnh nhất của lập luận đối phương: định nghĩa rõ, bỏ straw man, tách claim chính khỏi ví dụ. Burden of proof thuộc về người đưa ra claim có nội dung, nhưng người phản đối một claim cũng cần chỉ ra counterexample hoặc premise bị lỗi — không thể chỉ nói “chưa chứng minh” cho mọi điều.

Xem thêm [Câu hỏi, khái niệm và lập luận](00_questions_concepts_and_arguments.md) và [Knowledge, justification và evidence](../01_epistemology/00_knowledge_justification_and_evidence.md).

> **Bàn giao:** Sau **Steelman và burden of proof**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
