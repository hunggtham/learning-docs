# 컴퓨터활용능력 — Root Entrypoint

`컴퓨터활용능력/` là canonical root dự kiến cho tài liệu học chứng chỉ **컴퓨터활용능력 (Computer Proficiency / Computer Utilization Ability)**. Giai đoạn đầu chỉ dựng cấu trúc và mục lục cho **2급**; chưa viết lesson chi tiết.

## Phạm vi hiện tại

- Track ưu tiên: **컴퓨터활용능력 2급**
- 필기: `컴퓨터 일반` + `스프레드시트 일반`
- 실기: `스프레드시트 실무`
- Chuẩn thi hiện hành: 2024–2026
- Chuẩn 2027–2029 đã được công bố và áp dụng từ 2027-01-01; chênh lệch version sẽ được quản lý riêng tại [EXAM_VERSION_NOTES.md](./EXAM_VERSION_NOTES.md).

## Cấu trúc dự kiến

```text
컴퓨터활용능력/
├── README.md
├── EXAM_VERSION_NOTES.md
└── 2급/
    ├── README.md
    ├── 필기/
    │   ├── README.md
    │   ├── 01-컴퓨터-일반.md
    │   ├── 02-스프레드시트-일반.md
    │   └── 90-필기-문제풀이-전략.md
    └── 실기/
        ├── README.md
        ├── 01-기본작업.md
        ├── 02-계산작업.md
        ├── 03-분석작업.md
        ├── 04-기타작업.md
        └── 90-실전-모의고사.md
```

## Mạch học

1. [2급 overview](./2급/README.md)
2. [필기 index](./2급/필기/README.md)
3. [실기 index](./2급/실기/README.md)
4. Sau khi skeleton được xác nhận mới bắt đầu viết lesson chi tiết theo `prompt/COMMON_PROMPT.md`.

> Trạng thái: **structure-first / planned**. Các file con hiện chỉ giữ scope, TOC và dependency để tránh generate nội dung trước khi chốt kiến trúc.
