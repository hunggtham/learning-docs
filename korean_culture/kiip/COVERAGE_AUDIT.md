# KIIP / 한국사회 이해 — điểm vào kiểm toán phạm vi

**Ngày rà soát:** 2026-09-29  
**Root chuẩn gốc:** `korean_culture/kiip/`

Bản kiểm toán chi tiết về coverage kỳ thi đã tồn tại tại:

- [`16_coverage_audit.md`](./16_coverage_audit.md)

Tệp root này chỉ tạo **điểm vào governance ổn định** cho tooling cấp repository.

## Hợp đồng cấp root

KIIP sở hữu lớp ôn thi: ghi nhớ đúng facts, phân biệt khái niệm dễ nhầm, luyện viết/nói và luyện đề. Nó không thay thế các thư viện sâu hơn về Korean Culture, Korean History hoặc Korea Law/Civic Life.

Các nhãn phạm vi phải giữ rõ:

- `공통` — nền dùng chung;
- `귀화용 심화` — phần mở rộng cho mục tiêu nhập quốc tịch;
- `현재 확인` — fact, luật hoặc chính sách có thể thay đổi và cần kiểm lại nguồn hiện hành.

Workflow bền vững là:

```text
phạm vi thi
→ correction cho facts hiện hành
→ 8 lĩnh vực / 50 bài
→ cặp dễ nhầm và high-yield facts
→ active recall
→ viết / nói
→ mock exam
→ review pattern sai
→ kiểm lại coverage và current facts
```

Các con số pháp luật, chính trị, kinh tế hiện hành phải được coi là **facts cần rà soát theo thời điểm**, không phải chân lý cố định; khi cần, chúng phải dẫn về nguồn chính thức hiện tại.

## Quy tắc review và bàn giao

Khi coverage kỳ thi, high-yield gap hoặc trạng thái xác minh fact thay đổi, cập nhật [`16_coverage_audit.md`](./16_coverage_audit.md). Chỉ sửa tệp root này khi owner hoặc vị trí audit chi tiết thay đổi.

Khi người học cần hiểu sâu “vì sao” thay vì chỉ nhớ để thi, bàn giao sang [Korean Culture](../README.md), [Korean History](../../korean_history/README.md) hoặc [Korea Law/Civic Life](../../korea_law_civic_life/README.md) tùy chủ đề.