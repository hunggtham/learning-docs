# Lô-gic (logic / 논리), Validity và các dạng lập luận

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Lô-gic (logic / 논리), Validity và các dạng lập luận**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Validity không phải truth** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Deduction, induction và abduction** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

> **Chuyển mạch:** Validity nói về inference form, không bảo đảm premises true; deduction/induction/abduction vì vậy có standards khác nhau, cần steelman trước khi đặt burden of proof.

## Deduction, induction và abduction

- **Deduction** bảo toàn tính đúng theo cấu trúc: từ quy tắc (rule / 규칙) và trường hợp (case / 사례) suy ra consequence.
- **Induction** mở rộng từ observations hữu hạn sang mẫu (pattern / 패턴) tổng quát; conclusion có độ tin cậy chứ không certainty.
- **Abduction** chọn explanation tốt nhất cho bằng chứng (evidence / 증거) hiện có; “tốt nhất” cần nói rõ tiêu chuẩn như fit, simplicity, phạm vi (scope / 범위) và khả năng kiểm tra.

Không dạng nào tự giải quyết mọi vấn đề. Deduction có thể vận hành trên premise sai; induction nhạy với mẫu (sample / 표본) và cơ sở (base / 기반) tỷ lệ (rate / 비율); abduction có thể chọn explanation đẹp nhưng chưa đủ discriminating bằng chứng (evidence / 증거).

> **Chuyển mạch:** Ở chặng này của **Lô-gic (logic / 논리), Validity và các dạng lập luận**, **Steelman và burden of proof** tiếp nhận điểm tựa từ **Deduction, induction và abduction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Steelman và burden of proof

Trước khi phản biện, hãy viết phiên bản mạnh nhất của lập luận đối phương: định nghĩa rõ, bỏ straw man, tách claim chính khỏi ví dụ. Burden of proof thuộc về người đưa ra claim có nội dung, nhưng người phản đối một claim cũng cần chỉ ra counterexample hoặc premise bị lỗi — không thể chỉ nói “chưa chứng minh” cho mọi điều.

Xem thêm [Câu hỏi, khái niệm và lập luận](00_questions_concepts_and_arguments.md) và [Knowledge, justification và evidence](../01_epistemology/00_knowledge_justification_and_evidence.md).

> **Bàn giao:** Sau **Steelman và burden of proof**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
