# Phát triển ứng dụng bản địa — kiểm toán phạm vi

> **Mạch đọc:** Đọc audit này sau [README](./README.md) và [00_INDEX](./00_INDEX.md). README là điểm vào ổn định, `00_INDEX.md` giữ bản đồ học chi tiết; audit này chỉ trả lời **hai track Swift/iOS và Kotlin/Android đã phủ tới đâu, phần nào thuộc owner khác và thông tin nào phải kiểm lại theo phiên bản nền tảng**.

**Ngày rà soát:** 2026-09-29. `main` là nguồn chuẩn (source of truth / 정본) sau khi thay đổi được merge.

## 1. Phạm vi sở hữu

`11_native/` sở hữu kiến thức phát triển ứng dụng di động bản địa (native mobile development / 네이티브 모바일 개발) theo hai đường:

```text
Native Mobile
├── Swift / iOS
└── Kotlin / Android
```

Mỗi đường đi từ ngôn ngữ và nền tảng tới concurrency, persistence, networking, architecture, security, performance, testing, build/release và production engineering.

Các cơ chế tổng quát không nên copy lại nếu đã có owner rõ: thuật toán/hệ điều hành/mạng/database thuộc `computer_science/`; API/backend contract thuộc `10_backend/`; CI/CD, observability và platform operations thuộc `devops_platform_engineering/`.

## 2. Coverage hiện đã mạnh

Swift/iOS và Kotlin/Android đều đã có learning spine từ nền tảng tới production. Các vùng quan trọng như lifecycle, state ownership, concurrency, persistence, networking, offline/sync, security, performance, testing và release/rollback đều đã có chỗ trong cấu trúc hiện tại.

Điểm cần giữ là: framework/API chỉ là cách hiện thực. Một chapter đủ sâu phải làm rõ **vòng đời nền tảng (platform lifecycle / 플랫폼 수명주기)**, **quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **ranh giới đồng thời (concurrency boundary / 동시성 경계)**, **failure của lưu trữ/mạng**, **ranh giới bảo mật**, **chi phí tài nguyên/hiệu năng** và **đường release/recovery**.

Nếu chapter chỉ ghi “dùng API X” nhưng không giải thích state, lifecycle hoặc failure, nó chưa đạt chuẩn common prompt.

## 3. Thông tin nhạy theo phiên bản

Xcode, Swift, iOS SDK, Kotlin, Android Studio, AGP, Android API level và store policy đều có thể thay đổi. Những claim này phải có ngày kiểm tra và ưu tiên nguồn chính thức.

Cần tách rõ hai lớp:

```text
cơ chế bền tương đối
→ lifecycle / state / concurrency / persistence / networking

fact theo phiên bản
→ API availability / toolchain / store rule / SDK behavior
```

Không biến default hoặc policy hiện tại thành “kiến thức vĩnh viễn”.

## 4. Khoảng trống ưu tiên

Hiện chưa có gap P0/P1 ở learning spine. Giá trị tiếp theo nằm ở case tích hợp:

- **offline conflict → sync → recovery** giữa client và backend, để nối state local với server authority;
- production incident về memory/performance/battery/network degradation, để người học dùng telemetry thay vì đoán;
- platform migration case khi Swift/Kotlin/SDK thay đổi behavior hoặc failure mode;
- cross-platform comparison chỉ ở mức boundary, không biến Native thành catalog framework đa nền tảng.

Các case này quan trọng vì production failure thường cắt qua nhiều chapter cùng lúc; thêm một API chapter riêng lẻ không giúp luyện reasoning xuyên boundary.

## 5. Quy trình review

Khi sửa domain:

1. kiểm `README.md` và `00_INDEX.md` vẫn định tuyến đúng hai track;
2. giữ learning spine từ foundation tới master nhưng giải thích theo mechanism, không theo API list;
3. với version/store policy, ghi ngày kiểm tra và nguồn chính thức;
4. kiểm handoff sang Computer Science, Backend và DevOps;
5. chỉ thay trạng thái coverage khi có chapter/case cụ thể làm bằng chứng.

## 6. Kết luận và bàn giao

Coverage của cả Swift/iOS và Kotlin/Android hiện **mạnh**; chưa cần mở thêm track. Vòng tiếp theo nên ưu tiên end-to-end failure/recovery và migration cases.

Bắt đầu học tại [README](./README.md), dùng [00_INDEX](./00_INDEX.md) để chọn track. Khi vấn đề chuyển sang server contract hoặc production platform, bàn giao lần lượt sang [Backend](../10_backend/README.md) và [DevOps / Platform Engineering](../devops_platform_engineering/README.md).