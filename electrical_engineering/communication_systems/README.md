# Communication các hệ thống (systems / 시스템들) — Hệ thống thông tin

> **Mạch đọc:** Đọc **Communication các hệ thống (systems / 시스템들) — Hệ thống thông tin** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **cốt lõi (core / 핵심) tuyến (route / 경로)** sang **cốt lõi (core / 핵심) chapter**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Communication các hệ thống (systems / 시스템들) thiết kế đường đi của thông tin (information / 정보) qua channel có bandwidth, noise, interference, delay và giới hạn công suất. Mục tiêu không chỉ là “truyền được” mà là định lượng sự đánh đổi (trade-off / 트레이드오프) độ tin cậy (reliability / 신뢰성), tỷ lệ (rate / 비율), độ trễ (latency / 지연 시간) và năng lượng (energy / 에너지).

## Cốt lõi (core / 핵심) tuyến (route / 경로)

```text
baseband → modulation → channel/noise → synchronization → coding → link budget → protocol boundary
```


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) tuyến (route / 경로)**, ta sang **cốt lõi (core / 핵심) chapter** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cốt lõi (core / 핵심) chapter

- [Modulation, channel and coding](00_modulation_channel_coding.md) — I/Q, link ngân sách (budget / 예산), noise, synchronization, BER/FER và độ tin cậy (reliability / 신뢰성) sự đánh đổi (trade-off / 트레이드오프).
- [Information budget and synchronization](01_information_budget_and_synchronization.md) — Shannon/Nyquist, QAM, EVM, coding overhead và goodput.


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) chapter**, ta sang **Cần nắm** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cần nắm

- amplitude/phase/frequency modulation và I/Q biểu diễn (representation / 표현);
- bandwidth, SNR, đường dẫn (path / 경로) mất mát (loss / 손실), fading và interference;
- matched filter, timing/carrier khôi phục (recovery / 복구) và packet framing;
- nguồn (source / 소스)/channel coding, BER/FER, interleaving và retransmission;
- antenna/link ngân sách (budget / 예산) ở mức hệ thống, không lặp lại electromagnetic derivation.


> **Chuyển mạch:** Từ **Cần nắm**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi từ [signals and systems](../signals_and_systems/README.md), rồi nối sang Khoa học máy tính (computer science / 컴퓨터 과학) networking khi vấn đề chuyển từ vật lý (physical / 물리적)/link ngân sách (budget / 예산) sang packet, routing hoặc phân tán (distributed / 분산) giao thức (protocol / 프로토콜).

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 modulation channel coding](./00_modulation_channel_coding.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
