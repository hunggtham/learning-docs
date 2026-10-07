# 정보처리기사 필기 2026 — Deep-Dive nhánh học (track / 트랙)

Thư mục này là lớp học **sau Master Guide**. Master Guide kiểm tra coverage toàn cục; các tệp (file / 파일) ở đây tăng độ sâu từng môn tới mức có thể tự giải scenario, tính tay, dấu vết (trace / 추적) mã (code / 코드)/SQL, đọc đúng thuật ngữ tiếng Hàn và phân biệt các đáp án rất gần nhau.

## Luồng học

1. Đọc [`../00-2026-written-exam-master-guide.md`](../00-2026-written-exam-master-guide.md) để biết toàn bộ phạm vi.
2. Học 5 deep-dive theo môn, không bỏ qua phần procedural lập luận (reasoning / 추론).
3. Đọc [Cross-Subject Connection Map](07-cross-subject-connection-map.md) để nối yêu cầu (requirement / 요구사항) → thiết kế (design / 설계) → mã (code / 코드) → DB → OS/mạng (network / 네트워크) → thao tác (operation / 연산)/bảo mật (security / 보안).
4. Làm toàn bộ [Procedural Workbook](08-procedural-workbook.md) bằng tay; không tính là hoàn thành nếu chỉ đọc lời giải.
5. Học [High-Risk Confusion Atlas](11-high-risk-confusion-atlas.md) để khóa ranh giới giữa các cặp khái niệm dễ bị nhầm.
6. Làm [Advanced Scenario Labs](12-advanced-scenario-labs.md) để luyện nguyên nhân gốc (root cause / 근본 원인), tầng (layer / 계층)/phạm vi (scope / 범위) và sự đánh đổi (trade-off / 트레이드오프).
7. Dùng [Korean Term Bridge](13-korean-term-bridge.md) cho các concept đã hiểu bằng English/Vietnamese nhưng chưa nhận ra wording tiếng Hàn.
8. Đọc [Edge-Case Coverage Supplement](15-edge-case-coverage-supplement.md) để bù các chi tiết có độ salience thấp nhưng vẫn nằm trong 21 chapter.
9. Với điểm chưa chắc, dùng [Error Remediation Map](14-error-remediation-map.md) để phân loại lỗi và quay lại đúng tệp (file / 파일) cần sửa.
10. Một lỗi chỉ được đóng khi đạt `Explain → Distinguish → Reproduce → Transfer`, không lặp lại một bộ câu cố định chỉ để tăng cảm giác quen.

## 5 môn

1. [Môn 1 — 소프트웨어 설계: Deep Dive](01-software-design-depth.md)
2. [Môn 2 — 소프트웨어 개발: Deep Dive](02-software-development-depth.md)
3. [Môn 3 — 데이터베이스 구축: Deep Dive](03-database-construction-depth.md)
4. [Môn 4 — 프로그래밍 언어 활용: Deep Dive](04-programming-language-depth.md)
5. [Môn 5 — 정보시스템 구축 관리: Deep Dive](05-information-system-management-depth.md)

## Practice + tích hợp (integration / 통합) + remediation tầng (layer / 계층)

6. [Cross-Subject Connection Map — nối kiến thức giữa 5 môn](07-cross-subject-connection-map.md)
7. [Procedural Workbook — 35 bài tính/tracing/SQL/OS/network/security](08-procedural-workbook.md)
8. [High-Risk Confusion Atlas — 50+ cặp/nhóm dễ nhầm](11-high-risk-confusion-atlas.md)
9. [Advanced Scenario Labs — 25 lab + 3 mega-lab](12-advanced-scenario-labs.md)
10. [Korean Term Bridge — Korean → English → Vietnamese → mechanism](13-korean-term-bridge.md)
11. [Error Remediation Map — biến lỗi thành đường sửa cụ thể](14-error-remediation-map.md)
12. [Edge-Case Coverage Supplement — 120 điểm nhỏ dễ bỏ sót](15-edge-case-coverage-supplement.md)

## Cách dùng với các lesson cũ

Không đọc tuần tự hàng trăm lesson cũ trước. Khi deep-dive, kiểm tra (audit / 감사) hoặc remediation map phát hiện một phần chưa hiểu, mở lesson tương ứng trong folder môn để đào sâu. Các lesson cũ là **tham chiếu (reference / 참조) tầng (layer / 계층)**, không phải lộ trình học (learning path / 학습 경로) chính.

## Lỗi (error / 오류) mô hình (model / 모델)

Mọi lỗi trong scenario hoặc procedural lab nên được gán một primary mã (code / 코드):

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
**ứng dụng (application / 애플리케이션):** làm được một câu scenario/tính/mã (code / 코드)/SQL liên quan mà không nhìn đáp án.

Một lỗi chỉ được coi là “đã sửa” khi đạt thêm:

**Reproduction:** làm lại procedure/scenario không nhìn lời giải.
**Transfer:** làm đúng một câu mới với wording hoặc số liệu khác.

Toàn bộ nhánh học (track / 트랙) chỉ được coi là `ready` khi:

- 21 chapter đều đạt `Explain + Distinguish + Solve`;
- Edge-Case Supplement được đối chiếu đủ với các chapter sở hữu;
- 50+ confusion pairs cốt lõi không còn phụ thuộc vào từ khóa (keyword / 키워드) đơn lẻ;
- Procedural Workbook không còn dạng bài “biết lý thuyết nhưng không tự tính/dấu vết (trace / 추적) được”;
- Advanced Scenario Labs trung bình đạt ít nhất mức 3/4 theo rubric trong tệp (file / 파일);
- Korean terms quan trọng map được `Korean → English concept → mechanism`;
- mọi lỗi COV/CON/PRO/LAY/TERM quan trọng đã đi qua remediation và transfer kiểm thử (test / 테스트).
