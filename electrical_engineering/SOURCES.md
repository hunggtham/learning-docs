# Electrical Engineering — source ledger và version/currentness boundary

> **Owner:** `electrical_engineering/` (canonical engineering content). Ledger này tách invariant vật lý khỏi standard, datasheet và behavior của từng implementation.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| EE-IEEE-01 | IEEE Standards Association | standards cho điện, signal, communication, safety và embedded interfaces | https://standards.ieee.org/ | standard/edition phải ghi theo claim; portal kiểm tra 2026-10-09 | Không dùng landing page làm bằng chứng; ghi mã standard, edition, scope và normative status | communications/control/embedded |
| EE-IEC-01 | International Electrotechnical Commission | international standards, symbols, safety và electrotechnical terminology | https://www.iec.ch/standards | catalogue portal; edition riêng | Standard có thể paywalled/đổi edition; ghi mã/edition và không sao chép normative text nếu chưa có quyền | circuits/power/safety |
| EE-NIST-01 | National Institute of Standards and Technology | measurement, calibration, cybersecurity và technical reference cho hệ thống điện tử | https://www.nist.gov/publications | publication/version riêng; portal kiểm tra 2026-10-09 | Ghi publication number, revision và measurement conditions; không biến guideline thành law/standard bắt buộc | measurement/embedded/security |
| EE-ARM-01 | Arm Developer | ISA, architecture, memory model và processor implementation contract | https://developer.arm.com/documentation | architecture/profile/revision phải ghi | Không suy behavior của mọi MCU từ một chip; ghi architecture, core, vendor và errata khi cần | embedded/hardware–software |
| EE-TI-01 | Texas Instruments technical documentation | datasheet, reference design, electrical limits và application behavior của component cụ thể | https://www.ti.com/lit/ | datasheet revision/date bắt buộc | Absolute maximum, typical và guaranteed specs phải tách; không dùng vendor datasheet làm invariant toàn ngành | analog/power/electronics |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| EE-SAFETY-01 | `NEEDS_SOURCE` | Voltage/current/thermal/safety limit cần standard hoặc datasheet cụ thể, topology và điều kiện đo; không dùng con số nhớ từ một board. | Owner circuits/power chapter |
| EE-IMPLEMENTATION-01 | `REVIEW_REQUIRED` | Claim “mạch luôn ổn định”, “MCU hỗ trợ” hoặc “protocol đảm bảo” phải ghi operating range, revision, load và failure mode. | Owner relevant track + lab reviewer |
| EE-MEASUREMENT-01 | `NEEDS_SOURCE` | Measurement result phải ghi instrument, bandwidth, probe/loading, calibration, sampling và uncertainty. | Owner signals/measurement |
| EE-STANDARD-01 | `REVIEW_REQUIRED` | Tóm tắt standard phải giữ scope và normative/non-normative boundary; không dùng blog/vendor summary thay bản standard. | Owner standards-facing chapter |

## Quy trình refresh

1. Gắn source ID và mã edition/revision ngay tại lab/chapter khi claim phụ thuộc standard, component hoặc silicon.
2. Tách mô hình lý thuyết, nominal behavior, guaranteed limit, typical value và measured result.
3. Khi datasheet/errata/standard đổi, đánh dấu affected chapter và chạy lại lab; không chỉ cập nhật link.
4. Với safety-critical claim, thiếu authority hoặc điều kiện đo thì giữ `NEEDS_SOURCE`.
