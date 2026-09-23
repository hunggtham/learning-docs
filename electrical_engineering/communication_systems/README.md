# Communication Systems — Hệ thống thông tin

Communication systems thiết kế đường đi của information qua channel có bandwidth, noise, interference, delay và giới hạn công suất. Mục tiêu không chỉ là “truyền được” mà là định lượng trade-off reliability, rate, latency và energy.

## Core route

```text
baseband → modulation → channel/noise → synchronization → coding → link budget → protocol boundary
```

## Core chapter

- [Modulation, channel and coding](00_modulation_channel_coding.md) — I/Q, link budget, noise, synchronization, BER/FER và reliability trade-off.
- [Information budget and synchronization](01_information_budget_and_synchronization.md) — Shannon/Nyquist, QAM, EVM, coding overhead và goodput.

## Cần nắm

- amplitude/phase/frequency modulation và I/Q representation;
- bandwidth, SNR, path loss, fading và interference;
- matched filter, timing/carrier recovery và packet framing;
- source/channel coding, BER/FER, interleaving và retransmission;
- antenna/link budget ở mức hệ thống, không lặp lại electromagnetic derivation.

## Bridge

Đi từ [signals and systems](../signals_and_systems/README.md), rồi nối sang Computer Science networking khi vấn đề chuyển từ physical/link budget sang packet, routing hoặc distributed protocol.
