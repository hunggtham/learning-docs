# 정보처리기사 필기 2026 — Deep-Dive Track

Thư mục này là lớp học **sau Master Guide**. Master Guide kiểm tra coverage toàn cục; các file ở đây tăng độ sâu từng môn tới mức có thể tự giải scenario, tính tay, trace code/SQL, đọc đúng thuật ngữ tiếng Hàn và phân biệt các đáp án rất gần nhau.

## Luồng học

1. Đọc [`../00-2026-written-exam-master-guide.md`](../00-2026-written-exam-master-guide.md) để biết toàn bộ phạm vi.
2. Học 5 deep-dive theo môn, không bỏ qua phần procedural reasoning.
3. Làm [Mixed Exam Drills](06-mixed-exam-drills.md) để kiểm tra khả năng chuyển context giữa 5 môn.
4. Đọc [Cross-Subject Connection Map](07-cross-subject-connection-map.md) để nối requirement → design → code → DB → OS/network → operation/security.
5. Làm toàn bộ [Procedural Workbook](08-procedural-workbook.md) bằng tay; không tính là hoàn thành nếu chỉ đọc lời giải.
6. Học [High-Risk Confusion Atlas](11-high-risk-confusion-atlas.md) để khóa ranh giới giữa các cặp khái niệm dễ bị distractor lợi dụng.
7. Làm [Advanced Scenario Labs](12-advanced-scenario-labs.md) để luyện root cause, layer/scope và trade-off thay vì chọn keyword.
8. Dùng [Korean Term Bridge](13-korean-term-bridge.md) cho các concept đã hiểu bằng English/Vietnamese nhưng chưa nhận ra wording tiếng Hàn.
9. Dùng [Coverage Audit & Closed-Book Recall](10-coverage-audit-and-recall.md) để kiểm tra đủ `Explain + Distinguish + Solve` cho 21 chapter.
10. Làm [Full Mock Exam 100 Questions](09-full-mock-exam-100.md) trong một lượt và chấm riêng từng môn.
11. Với mọi câu sai, dùng [Error Remediation Map](14-error-remediation-map.md) để phân loại lỗi và quay lại đúng file/drill cần sửa.
12. Chỉ làm full mock tiếp theo khi lỗi cũ đạt `Explain → Distinguish → Reproduce → Transfer`, không làm đề liên tục chỉ để tăng cảm giác quen câu.

## 5 môn

1. [Môn 1 — 소프트웨어 설계: Deep Dive](01-software-design-depth.md)
2. [Môn 2 — 소프트웨어 개발: Deep Dive](02-software-development-depth.md)
3. [Môn 3 — 데이터베이스 구축: Deep Dive](03-database-construction-depth.md)
4. [Môn 4 — 프로그래밍 언어 활용: Deep Dive](04-programming-language-depth.md)
5. [Môn 5 — 정보시스템 구축 관리: Deep Dive](05-information-system-management-depth.md)

## Practice + integration + remediation layer

6. [Mixed Exam Drills — 40 câu luyện liên môn](06-mixed-exam-drills.md)
7. [Cross-Subject Connection Map — nối kiến thức giữa 5 môn](07-cross-subject-connection-map.md)
8. [Procedural Workbook — 35 bài tính/tracing/SQL/OS/network/security](08-procedural-workbook.md)
9. [Full Mock Exam — 100 câu, 20 câu/môn](09-full-mock-exam-100.md)
10. [Coverage Audit & Closed-Book Recall — audit 21 chapter](10-coverage-audit-and-recall.md)
11. [High-Risk Confusion Atlas — 50 cặp/nhóm dễ nhầm](11-high-risk-confusion-atlas.md)
12. [Advanced Scenario Labs — 25 lab + 3 mega-lab](12-advanced-scenario-labs.md)
13. [Korean Term Bridge — Korean → English → Vietnamese → mechanism](13-korean-term-bridge.md)
14. [Error Remediation Map — biến câu sai thành đường sửa cụ thể](14-error-remediation-map.md)

## Cách dùng với các lesson cũ

Không đọc tuần tự hàng trăm lesson cũ trước. Khi deep-dive, audit hoặc remediation map phát hiện một phần chưa hiểu, mở lesson tương ứng trong folder môn để đào sâu. Các lesson cũ là **reference layer**, không phải learning path chính.

## Error model

Mọi lỗi trong mock/mixed drill nên được gán một primary code:

```text
COV  = coverage hole
CON  = confusion giữa concept gần nhau
PRO  = procedural error
LAY  = đúng mechanism nhưng sai layer/scope
TERM = không nhận ra Korean terminology
READ = đọc sai polarity/wording
CAL  = arithmetic error
MEM  = nhớ đáp án nhưng không hiểu mechanism
```

Mục tiêu không phải giảm “số câu sai” bằng cách thuộc đáp án cũ, mà giảm **nguồn sinh lỗi**.

## Definition of Done

Một chủ đề chỉ được coi là “đã học” khi đạt đủ bốn điều kiện:

**Recognition:** nhìn thuật ngữ tiếng Hàn và biết nó nói về concept nào.  
**Explanation:** giải thích được bản chất bằng lời của mình.  
**Discrimination:** phân biệt được với 2–3 khái niệm gần nhất.  
**Application:** làm được một câu scenario/tính/code/SQL liên quan mà không nhìn đáp án.

Một lỗi chỉ được coi là “đã sửa” khi đạt thêm:

**Reproduction:** làm lại procedure/scenario không nhìn lời giải.  
**Transfer:** làm đúng một câu mới với wording hoặc số liệu khác.

Toàn bộ track chỉ được coi là `ready` khi:

- 21 chapter đều đạt `Explain + Distinguish + Solve`;
- 50 confusion pairs cốt lõi không còn phụ thuộc vào keyword đơn lẻ;
- Procedural Workbook không còn dạng bài “biết lý thuyết nhưng không tự tính/trace được”;
- Advanced Scenario Labs trung bình đạt ít nhất mức 3/4 theo rubric trong file;
- Korean terms quan trọng map được `Korean → English concept → mechanism`;
- Full Mock không có môn nào dưới 8/20;
- mọi lỗi COV/CON/PRO/LAY/TERM quan trọng đã đi qua remediation và transfer test.