# Life — Canonical Coverage Map

> **Mạch đọc:** [README](README.md) là owner cấp domain; file này trả lời câu hỏi “mỗi nhánh đã có mental model và chapter nào, còn thiếu phần nào?”. Đọc theo cột route để thấy prerequisite và điểm bàn giao, không coi bảng là nội dung thay thế chapter.

## Trạng thái route

Bảng này đối chiếu owner, chapter đã có và câu hỏi kế tiếp; hãy đọc cột cuối như backlog có giới hạn, không như claim rằng mọi chapter kế tiếp đã hoàn thành.

| Nhánh | Owner | Chapter hiện có | Câu hỏi kế tiếp |
|---|---|---|---|
| Food & Drinks | [`food_drink/README.md`](food_drink/README.md) | Tầng tổng quan (01–03); Whisky chuyên sâu (00–04); Bia chuyên sâu (00–02) | route nền tảng và chuyên sâu đã đủ; mở rộng wine/coffee khi có nhu cầu |
| Cars | [`vehicles/cars/README.md`](vehicles/cars/README.md) | Tầng nền tảng (00–03); Tầng chuyên sâu 13 bài (01–13: ICE, EV/HEV, hộp số, dẫn động, lốp, phanh, lái/treo, turbo, nhiệt, ADAS, spec, chẩn đoán, TCO) | route 2 tầng hoàn chỉnh; thêm diagnostic casebook khi cần |
| Consumer Knowledge & Literacy | [`consumer_knowledge/README.md`](consumer_knowledge/README.md) & [`consumer_literacy/README.md`](consumer_literacy/README.md) | Function/material/TCO (00–04); Specs/materials/reliability/lifecycle (00–03) | backbone dùng lại cho toàn domain; thêm case study khi có bằng chứng |
| Home | [`home/README.md`](home/README.md) | Systems; thermal/air/moisture; electricity/water; maintenance cases; room system case lab | thêm case nhà ở theo điều kiện địa phương khi cần |
| Digital Life | [`digital_life/README.md`](digital_life/README.md) | Devices/data; security/privacy; backup/exit; messaging/smart home; service case lab | service-specific modules cần ghi phiên bản và ngày kiểm tra |
| Everyday Law | [`everyday_law/README.md`](everyday_law/README.md) | Event/rule/evidence; contracts; jurisdiction/deadlines; home/work/digital; jurisdiction case lab | module theo jurisdiction chỉ thêm cùng nguồn hiện hành |
| Safety & First Aid | [`safety_first_aid/README.md`](safety_first_aid/README.md) | Scene assessment; acute examples; prevention; training boundaries; scenario drill case lab | diễn tập địa phương cần xác minh đường cấp cứu và huấn luyện |
| Communication | [`communication/README.md`](communication/README.md) | Shared context; messages/meetings; conflict/repair; online/negotiation; workplace/family/online case lab | thêm case theo quan hệ/kênh khi có mục tiêu rõ |
| How Things Work | [`how_things_work/README.md`](how_things_work/README.md) | Boundary/mechanism; energy/feedback; evidence/test; cross-domain labs; system case template | các phép đo sâu hơn là lớp mở rộng, không phải owner còn thiếu |

Các chapter hiện tại tạo thành lớp canonical nền tảng và ứng dụng dùng chung cho cả chín nhánh. Cột “Câu hỏi kế tiếp” chỉ nêu lớp mở rộng có owner; nó không phải claim rằng mọi category, model, dịch vụ hay jurisdiction cụ thể đã được viết hoặc có thể dùng thay tư vấn chuyên môn.

> **Bàn giao:** Khi thêm chapter, cập nhật cả README của nhánh và bảng này; chapter mới phải nối vào route trước/sau, có nguồn hoặc giới hạn phù hợp và không duplicate owner của nhánh khác.
