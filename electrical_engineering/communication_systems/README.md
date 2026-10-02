# Communication các hệ thống (systems / 시스템들) — Hệ thống thông tin

> **Mạch đọc:** README này là owner của **Communication các hệ thống (systems / 시스템들) — Hệ thống thông tin**. Route đi từ thông tin, bandwidth và channel → signal/modulation/coding → antennas, networks và synchronization → measurement, reliability và power → applications, để mỗi chapter trả lời một phần của bài toán truyền tin.

Communication các hệ thống (systems / 시스템들) thiết kế đường đi của thông tin (information / 정보) qua channel có bandwidth, noise, interference, delay và giới hạn công suất. Mục tiêu không chỉ là “truyền được” mà là định lượng sự đánh đổi (trade-off / 트레이드오프) độ tin cậy (reliability / 신뢰성), tỷ lệ (rate / 비율), độ trễ (latency / 지연 시간) và năng lượng (energy / 에너지).

## Cốt lõi (core / 핵심) tuyến (route / 경로)

```text
baseband → modulation → channel/noise → synchronization → coding → link budget → protocol boundary
```

> **Chuyển mạch:** **Cốt lõi tuyến** cho biết thứ tự từ tín hiệu đến kênh và mã hóa; **Cốt lõi chapter** giải thích từng cơ chế, còn **Cần nắm** chốt các đại lượng phải kiểm tra.

## Cốt lõi (core / 핵심) chapter

- [Modulation, channel and coding](00_modulation_channel_coding.md) — I/Q, link ngân sách (budget / 예산), noise, synchronization, BER/FER và độ tin cậy (reliability / 신뢰성) sự đánh đổi (trade-off / 트레이드오프).
- [Information budget and synchronization](01_information_budget_and_synchronization.md) — Shannon/Nyquist, QAM, EVM, coding overhead và goodput.

> **Chuyển mạch:** Sau khi nắm cơ chế và đại lượng, **Cầu nối** đưa chúng vào bài toán budget, đồng bộ và failure mode của một đường truyền thực.

## Cần nắm

- amplitude/phase/frequency modulation và I/Q biểu diễn (representation / 표현);
- bandwidth, SNR, đường dẫn (path / 경로) mất mát (loss / 손실), fading và interference;
- matched filter, timing/carrier khôi phục (recovery / 복구) và packet framing;
- nguồn (source / 소스)/channel coding, BER/FER, interleaving và retransmission;
- antenna/link ngân sách (budget / 예산) ở mức hệ thống, không lặp lại electromagnetic derivation.

> **Chuyển mạch:** **Cầu nối** khép README bằng cách gắn khái niệm với trade-off thông lượng, nhiễu, latency và độ tin cậy; đó là điểm quay lại khi mở chapter chi tiết.

## Cầu nối (bridge / 브리지)

Đi từ [signals and systems](../signals_and_systems/README.md), rồi nối sang Khoa học máy tính (computer science / 컴퓨터 과학) networking khi vấn đề chuyển từ vật lý (physical / 물리적)/link ngân sách (budget / 예산) sang packet, routing hoặc phân tán (distributed / 분산) giao thức (protocol / 프로토콜).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
