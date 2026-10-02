# 15 — ML tính năng (feature / 기능) nền tảng (platform / 플랫폼) và point-in-time tính đúng đắn (correctness / 정확성)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **15 — ML tính năng (feature / 기능) nền tảng (platform / 플랫폼) và point-in-time tính đúng đắn (correctness / 정확성)**. Route đi từ feature time semantics → offline/online parity → point-in-time joins và leakage controls → registry, serving và monitoring → training/serving skew, để feature platform bảo vệ correctness thay vì chỉ cung cấp cột dữ liệu.

Tính năng (feature / 기능) nền tảng (platform / 플랫폼) nối kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) với huấn luyện (training / 학습) và serving. Rủi ro lớn nhất không phải tính năng (feature / 기능) thiếu đẹp, mà là **huấn luyện (training / 학습)/serving skew** và dữ liệu (data / 데이터) leakage do dùng thông tin của tương lai.

## 1. tính năng (feature / 기능) thời gian (time / 시간) ngữ nghĩa (semantics / 의미론)

Mỗi tính năng (feature / 기능) cần sự kiện (event / 이벤트) thời gian (time / 시간), availability thời gian (time / 시간) và thực thể (entity / 엔터티) key. huấn luyện (training / 학습) row tại prediction thời gian (time / 시간) T chỉ được dùng tính năng (feature / 기능) có `available_at <= T`, không chỉ `event_time <= T`.

```text
entity + prediction_time
→ latest feature version available before T
```

Dùng hiện tại (current / 현재) dimension cho historical huấn luyện (training / 학습) có thể đưa kết quả (outcome / 결과) tương lai vào đầu vào (input / 입력) mà không tạo exception.

> **Chuyển mạch:** Trong **15 — ML tính năng (feature / 기능) nền tảng (platform / 플랫폼) và point-in-time tính đúng đắn (correctness / 정확성)**, **2. Offline/online parity** tiếp nhận điểm tựa từ **1. tính năng (feature / 기능) thời gian (time / 시간) ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Freshness và missing tính năng (feature / 기능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Offline/online parity

Offline store tối ưu scan lịch sử; online store tối ưu điểm (point / 지점) lookup độ trễ (latency / 지연 시간). Cùng tính năng (feature / 기능) definition phải tạo giá trị tương đương, timezone/encoding/null chính sách (policy / 정책) giống nhau và phiên bản (version / 버전) được dấu vết (trace / 추적).

Dual-write có thể lệch khi một sink thành công còn sink kia thất bại (fail / 실패). sự kiện (event / 이벤트) log + deterministic projection thường dễ replay hơn hai writer độc lập.

> **Chuyển mạch:** Ở chặng này của **15 — ML tính năng (feature / 기능) nền tảng (platform / 플랫폼) và point-in-time tính đúng đắn (correctness / 정확성)**, **3. Freshness và missing tính năng (feature / 기능)** tiếp nhận điểm tựa từ **2. Offline/online parity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Backfill và leakage kiểm thử (test / 테스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Freshness và missing tính năng (feature / 기능)

Tính năng (feature / 기능) SLO cần freshness, completeness, availability và acceptable staleness. Missing giá trị (value / 값) phải phân biệt “chưa đến”, “không áp dụng”, “bị xóa” và “chuỗi xử lý (pipeline / 파이프라인) lỗi”. Default giá trị (value / 값) có thể che sự cố (incident / 인시던트) và làm mô hình (model / 모델) drift.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **15 — ML tính năng (feature / 기능) nền tảng (platform / 플랫폼) và point-in-time tính đúng đắn (correctness / 정확성)**, **4. Backfill và leakage kiểm thử (test / 테스트)** tiếp nhận điểm tựa từ **3. Freshness và missing tính năng (feature / 기능)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Deletion và lineage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Backfill và leakage kiểm thử (test / 테스트)

Backfill tính năng (feature / 기능) cần giữ snapshot/mã (code / 코드)/lược đồ (schema / 스키마) phiên bản (version / 버전), không rewrite huấn luyện (training / 학습) set mà không có provenance. kiểm thử (test / 테스트) leakage bằng cách dịch prediction cutoff, kiểm tra tính năng (feature / 기능) availability và chạy negative điều khiển (control / 제어) với trường dữ liệu (field / 필드) chỉ xuất hiện sau kết quả (outcome / 결과).

> **Chuyển mạch:** Trong **15 — ML tính năng (feature / 기능) nền tảng (platform / 플랫폼) và point-in-time tính đúng đắn (correctness / 정확성)**, **5. Deletion và lineage** tiếp nhận điểm tựa từ **4. Backfill và leakage kiểm thử (test / 테스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. bằng chứng (evidence / 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Deletion và lineage

Xóa một subject phải lan qua raw sự kiện (event / 이벤트), offline tính năng (feature / 기능), online key, huấn luyện (training / 학습) sản phẩm tạo ra (artifact / 산출물), bộ nhớ đệm (cache / 캐시) và exported mô hình (model / 모델) nếu chính sách (policy / 정책) yêu cầu. tính năng (feature / 기능) danh mục (catalog / 카탈로그) cần đơn vị sở hữu (owner / 오너), nguồn (source / 소스) columns, transformation, TTL, sensitivity và downstream mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **15 — ML tính năng (feature / 기능) nền tảng (platform / 플랫폼) và point-in-time tính đúng đắn (correctness / 정확성)**, **5. Deletion và lineage** nêu điều cần giải thích; **6. bằng chứng (evidence / 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 6. bằng chứng (evidence / 증거)

Theo dõi offline-online diff, tính năng (feature / 기능) freshness phân phối (distribution / 분포), missingness by thực thể (entity / 엔터티), point-in-time phép nối (join / 조인) violations, dữ liệu huấn luyện (training data / 학습 데이터) băm (hash / 해시), tính năng (feature / 기능) phiên bản (version / 버전) và mô hình (model / 모델) đầu vào (input / 입력) lược đồ (schema / 스키마). Chỉ mô hình (model / 모델) accuracy không chứng minh chuỗi xử lý (pipeline / 파이프라인) tính năng (feature / 기능) đúng.

Đọc tiếp: [05 — Modeling](../05_data_modeling_and_transformation/README.md), [10 — Serving](../10_serving_semantic_layer/README.md), [11 — Governance](../11_governance_lineage_security/README.md).

> **Bàn giao:** Sau **6. bằng chứng (evidence / 증거)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
