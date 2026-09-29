# 04. Caching và vô hiệu hóa (invalidation / 무효화)

> **Mạch đọc:** Đặt **04. Caching và vô hiệu hóa (invalidation / 무효화)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **mẫu (pattern / 패턴)** sang **Stampede và consistency**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Bộ nhớ đệm (cache / 캐시) là một bản sao có thời hạn, không phải nguồn chuẩn (source of truth / 정본). Thiết kế bộ nhớ đệm (cache / 캐시) bắt
đầu bằng câu hỏi: dữ liệu nào được phép stale, trong bao lâu, ai sở hữu key, và
thất bại (failure / 실패) khi bộ nhớ đệm (cache / 캐시) mất là gì.

## Mẫu (pattern / 패턴)
Phần “Mẫu (pattern / 패턴)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- **Cache-aside**: đọc bộ nhớ đệm (cache / 캐시), miss thì đọc nguồn (source / 소스) rồi populate; dễ áp dụng nhưng
  có stampede và cửa sổ stale.
- **Write-through**: ghi qua bộ nhớ đệm (cache / 캐시) và nguồn (source / 소스) theo một luồng (flow / 흐름); đơn giản cho reader
  nhưng cần xử lý partial thất bại (failure / 실패).
- **Write-behind**: bộ nhớ đệm (cache / 캐시) nhận ghi trước; chỉ dùng khi chấp nhận durability
  bất đồng bộ và có hàng đợi (queue / 큐)/khôi phục (recovery / 복구) rõ ràng.
- **Refresh-ahead**: làm mới trước expiry cho hot key; cần giới hạn chi phí.

TTL là an toàn (safety / 안전) net, không phải vô hiệu hóa (invalidation / 무효화) chiến lược (strategy / 전략). Khi mutation thành công,
invalidate các key liên quan hoặc dùng versioned key. vô hiệu hóa (invalidation / 무효화) phải bao phủ
mọi biểu diễn (representation / 표현): detail, danh sách (list / 목록), aggregate và permission-sensitive view.


> **Chuyển mạch:** Từ **mẫu (pattern / 패턴)**, ta sang **Stampede và consistency** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Stampede và consistency

Dùng single-flight/lease, jitter TTL, stale-while-revalidate hoặc giới hạn
tính đồng thời (concurrency / 동시성) để tránh hàng nghìn yêu cầu (request / 요청) cùng rebuild một key. Không bộ nhớ đệm (cache / 캐시) dữ liệu
phụ thuộc định danh (identity / 식별자) bằng key thiếu tenant/người dùng (user / 사용자). Nếu consistency quan trọng hơn
độ trễ (latency / 지연 시간), đọc nguồn (source / 소스) sau ghi (write / 쓰기) hoặc đính kèm phiên bản (version / 버전) để máy khách (client / 클라이언트) phát hiện stale.


> **Chuyển mạch:** Từ **Stampede và consistency**, ta sang **Chỉ số cần theo dõi** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Chỉ số cần theo dõi

Hit ratio một mình không đủ: theo dõi stale-read tỷ lệ (rate / 비율), eviction, kích thước (size / 크기), độ trễ (latency / 지연 시간),
origin tải (load / 로드), lỗi (error / 오류)/fallback và hot-key skew. bộ nhớ đệm (cache / 캐시) outage phải degrade có chủ ý
(slower origin, partial response hoặc fail fast), không tạo thử lại (retry / 재시도) storm.


> **Chuyển mạch:** Từ **Chỉ số cần theo dõi**, ta sang **Đào sâu: consistency ngân sách (budget / 예산)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Đào sâu: consistency ngân sách (budget / 예산)

Đặt một `staleness budget` cho từng loại dữ liệu thay vì nói bộ nhớ đệm (cache / 캐시) “nhanh hơn”.
Profile công khai có thể chấp nhận stale 60 giây; quyền truy cập không được đọc
bộ nhớ đệm (cache / 캐시) quá cũ sau revoke. ngân sách (budget / 예산) quyết định TTL, vô hiệu hóa (invalidation / 무효화), read-after-write
đường dẫn (path / 경로) và alert threshold.

Key thiết kế (design / 설계) là một phần của lược đồ (schema / 스키마). Key phải chứa mọi dimension làm thay đổi
biểu diễn (representation / 표현) (tenant, locale, permission scope, version). không gian tên (namespace / 네임스페이스) và phiên bản (version / 버전)
giúp đổi serialization mà không phải scan/xóa toàn bộ bộ nhớ đệm (cache / 캐시). Khi vô hiệu hóa (invalidation / 무효화)
không chắc chắn, versioned key + TTL ngắn an toàn hơn một lệnh delete tưởng đã
bao phủ tất cả variant.

Ba thất bại (failure / 실패) mẫu (pattern / 패턴) cần tách: **stampede** (rebuild đồng thời, dùng lease),
**avalanche** (nhiều key hết hạn cùng lúc, dùng jitter), và **penetration** (key
không tồn tại bị hỏi liên tục, dùng negative cache TTL ngắn). kiểm thử (test / 테스트) cả bộ nhớ đệm (cache / 캐시)
outage và origin lỗi (error / 오류) trong lúc refresh để không ghi đè giá trị tốt bằng lỗi (error / 오류).

> **Bàn giao:** Sau **Đào sâu: consistency ngân sách (budget / 예산)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 backend request lifecycle](./00_backend_request_lifecycle.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
