# Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**. Route đi từ device/OEM/OS matrix → localization, resource và plural → battery/network/privacy → release readiness, rollback và observability → risk-based production testing.

Một Android app có thể compile, pass đơn vị (unit / 단위) kiểm thử (test / 테스트) và chạy tốt trên điện thoại nhà phát triển (developer / 개발자) nhưng vẫn thất bại môi trường vận hành (production / 운영 환경) vì khác OS phiên bản (version / 버전), OEM, locale, font quy mô (scale / 규모), mạng (network / 네트워크) điều kiện (condition / 조건), screen kích thước (size / 크기), battery chính sách (policy / 정책) hoặc di chuyển (migration / 마이그레이션) đường dẫn (path / 경로). chất lượng (quality / 품질) kỹ thuật (engineering / 엔지니어링) mobile vì vậy không chỉ là “kiểm thử (test / 테스트) nhiều hơn”; nó là xây **rủi ro (risk / 위험) ma trận (matrix / 행렬)** phản ánh môi trường thật.

Chapter này là lớp kiểm tra cuối của toàn bộ Kotlin + Android Master Notes. Mục tiêu là biết một tính năng (feature / 기능) “ready for môi trường vận hành (production / 운영 환경)” nghĩa là gì ngoài happy đường dẫn (path / 경로).

# 1. Android là một nền tảng (platform / 플랫폼) ma trận (matrix / 행렬)

Môi trường vận hành (production / 운영 환경) Android tồn tại trên nhiều chiều:

```text
OS version
× target SDK behavior
× OEM implementation
× RAM/CPU class
× screen/window size
× locale/font scale/RTL
× network quality
× permission state
× battery state
× account/data history
× app upgrade path
```

Bạn không thể kiểm thử (test / 테스트) Cartesian sản phẩm (product / 제품) đầy đủ. Vì vậy cần chọn ma trận (matrix / 행렬) theo **rủi ro (risk / 위험)**.

# 2. Risk-based thiết bị (device / 장치) ma trận (matrix / 행렬)

Một ma trận (matrix / 행렬) tối thiểu thường nên có:

| Nhóm | Mục đích |
|---|---|
| min/near-min API | tính tương thích (compatibility / 호환성) cũ |
| latest stable API | hành vi (behavior / 동작) mới |
| target-SDK di chuyển (migration / 마이그레이션) API | chính sách (policy / 정책)/permission mới |
| low/mid/high thiết bị (device / 장치) | hiệu năng (performance / 성능)/bộ nhớ (memory / 메모리) |
| Samsung/điểm ảnh (pixel / 픽셀) + OEM quan trọng | vendor difference |
| small phone | compact bố cục (layout / 레이아웃) |
| large/tablet/foldable nếu hỗ trợ (support / 지원) | adaptive UI |

Nếu app phụ thuộc BLE/camera/NFC, thêm vật lý (physical / 물리적) hardware representative thay vì chỉ emulator.

# 3. kiểm thử (test / 테스트) upgrade đường dẫn (path / 경로), không chỉ fresh install

Fresh install bỏ qua một lớp bug lớn: lược đồ (schema / 스키마) cũ, SharedPreferences cũ, đơn vị từ (token / 토큰) cũ, cached tệp (file / 파일) cũ, notification channel cũ và dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션).

Bản phát hành (release / 릴리스) kiểm thử (test / 테스트) nên có:

```text
version N production data
→ install N+1
→ migrate
→ launch critical flow
→ background/restore
→ rollback strategy nếu có
```

Room di chuyển (migration / 마이그레이션) phải kiểm thử (test / 테스트) từ các lược đồ (schema / 스키마) phiên bản (version / 버전) thực tế còn người dùng (user / 사용자) ngoài môi trường vận hành (production / 운영 환경), không chỉ previous phiên bản (version / 버전) gần nhất nếu người dùng (user / 사용자) có thể skip nhiều bản phát hành (release / 릴리스).

# 4. Downgrade và quay lui (rollback / 롤백) tính tương thích (compatibility / 호환성)

Play quay lui (rollback / 롤백) không phải lúc nào tương đương cài APK cũ đơn giản; máy chủ (server / 서버)/API/lược đồ (schema / 스키마) có thể đã thay đổi.

Khi staged rollout phiên bản (version / 버전) N+1 ghi dữ liệu (data / 데이터) format mà N không đọc được, quay lui (rollback / 롤백) app nhị phân (binary / 이진) có thể làm người dùng (user / 사용자) crash.

Cấp cao (senior / 시니어) bản phát hành (release / 릴리스) thiết kế (design / 설계) hỏi trước:

```text
N+1 thay local schema thế nào?
server contract backward compatible bao lâu?
feature flag có disable behavior mới không?
rollback binary có đọc dữ liệu mới được không?
```

# Localization

## 5. String tài nguyên (resource / 자원), không hardcode UI văn bản (text / 텍스트)

User-facing string nên ở tài nguyên (resource / 자원) để localize, kiểm thử (test / 테스트) và thay đổi theo locale.

```xml
<string name="order_count">%1$d orders</string>
```

Nhưng plural phải dùng plural tài nguyên (resource / 자원) thay vì nối số + noun thủ công.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **5. String tài nguyên (resource / 자원), không hardcode UI văn bản (text / 텍스트)** nêu điều cần giải thích; **6. Plural** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. Format number/currency/date theo locale** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Plural

Ngôn ngữ không có cùng plural quy tắc (rule / 규칙). Dùng `<plurals>`/quantity string để khung phần mềm (framework / 프레임워크) chọn form.

Đừng giả định chỉ singular/plural kiểu English.

> **Chuyển mạch:** Plural và number/currency/date đều phụ thuộc locale; sau format, timezone phải được xử lý riêng để tránh biến instant thành local time sai.

## 7. Format number/currency/date theo locale

Không tự format:

```kotlin
"$price USD"
```

nếu UI cần locale-aware display. Dùng formatter thích hợp cho currency/number/date.

Lĩnh vực (domain / 도메인) giá trị (value / 값) giữ ngữ nghĩa (semantic / 의미적) chuẩn; formatting là presentation concern.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **8. thời gian (time / 시간) zone** tiếp nhận điểm tựa từ **7. Format number/currency/date theo locale** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Locale thay đổi (change / 변경) thời gian chạy (runtime / 런타임)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. thời gian (time / 시간) zone

Timestamp máy chủ (server / 서버) nên có ngữ nghĩa (semantic / 의미적) rõ: instant tuyệt đối hay cục bộ (local / 로컬) nghiệp vụ (business / 비즈니스) date/thời gian (time / 시간).

`2026-09-20 09:00` không đủ nếu không biết timezone/ngữ cảnh (context / 맥락).

Phân biệt:

```text
Instant → một thời điểm tuyệt đối
LocalDate → ngày lịch không timezone
LocalDateTime → local clock chưa gắn zone
ZonedDateTime → local time + zone
```

Mobile travel qua timezone dễ làm bug calendar/reminder nếu mô hình (model / 모델) sai từ đầu.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **9. Locale thay đổi (change / 변경) thời gian chạy (runtime / 런타임)** tiếp nhận điểm tựa từ **8. thời gian (time / 시간) zone** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Start/end thay left/right** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Locale thay đổi (change / 변경) thời gian chạy (runtime / 런타임)

Locale có thể đổi khi tiến trình (process / 프로세스)/app đang tồn tại. Đừng bộ nhớ đệm (cache / 캐시) formatted string toàn cục (global / 전역) vô hạn.

UI nên derive display văn bản (text / 텍스트) từ tài nguyên (resource / 자원)/formatter theo hiện tại (current / 현재) cấu hình (configuration / 구성).

# RTL

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **10. Start/end thay left/right** tiếp nhận điểm tựa từ **9. Locale thay đổi (change / 변경) thời gian chạy (runtime / 런타임)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. BiDi văn bản (text / 텍스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Start/end thay left/right

Bố cục (layout / 레이아웃) direction phải hỗ trợ (support / 지원) RTL khi app localize Arabic/Hebrew. Dùng start/end cho alignment/margin khi ngữ nghĩa (semantic / 의미적) directional.

Icon có direction như arrow/back có thể cần auto-mirror.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **11. BiDi văn bản (text / 텍스트)** tiếp nhận điểm tựa từ **10. Start/end thay left/right** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Large văn bản (text / 텍스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. BiDi văn bản (text / 텍스트)

Mixed Latin/Arabic/number/URL có thể kết xuất (render / 렌더링) direction khó. Không tự đảo string. Dùng nền tảng (platform / 플랫폼) văn bản (text / 텍스트) handling và kiểm thử (test / 테스트) real locale.

# Font scaling và khả năng tiếp cận (accessibility / 접근성)

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **12. Large văn bản (text / 텍스트)** tiếp nhận điểm tựa từ **11. BiDi văn bản (text / 텍스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Screen reader** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Large văn bản (text / 텍스트)

Người dùng (user / 사용자) có thể tăng font quy mô (scale / 규모). Fixed-height bộ chứa (container / 컨테이너) dễ cắt văn bản (text / 텍스트).

Đừng thiết kế (design / 설계) button/card theo một screenshot kích thước (size / 크기) duy nhất. Cho văn bản (text / 텍스트) wrap hoặc bố cục (layout / 레이아웃) adapt.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **13. Screen reader** tiếp nhận điểm tựa từ **12. Large văn bản (text / 텍스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Color/contrast** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Screen reader

Trọng yếu (critical / 중요) luồng (flow / 흐름) phải kiểm thử (test / 테스트) manual với TalkBack ít nhất theo bản phát hành (release / 릴리스) cadence phù hợp. ngữ nghĩa (semantics / 의미론) automated kiểm thử (test / 테스트) giúp nhưng không thay trải nghiệm nghe thật.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **13. Screen reader** đã nêu tiêu chí phân biệt, còn **14. Color/contrast** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **15. Wakeup chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Color/contrast

Không truyền trạng thái chỉ bằng màu. lỗi (error / 오류)/success/selected nên có văn bản (text / 텍스트)/icon/ngữ nghĩa (semantic / 의미적) trạng thái (state / 상태).

Dark chế độ (mode / 모드) và động (dynamic / 동적) color có thể thay contrast; custom color cần kiểm thử (test / 테스트) cả theme.

# Battery và background chất lượng (quality / 품질)

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **14. Color/contrast** đã nêu tiêu chí phân biệt, còn **15. Wakeup chi phí (cost / 비용)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **16. Batch thay polling khi có thể** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Wakeup chi phí (cost / 비용)

Mỗi periodic tác vụ (task / 작업), location cập nhật (update / 업데이트), sensor listener, BLE scan và mạng (network / 네트워크) poll có battery chi phí (cost / 비용). Một app có nhiều nhóm (team / 팀) dễ tạo “death by a thousand timers”.

Background công việc (work / 작업) cần inventory tập trung:

```text
job name
owner
frequency
constraints
network cost
battery reason
user-visible benefit
```

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **16. Batch thay polling khi có thể** tiếp nhận điểm tựa từ **15. Wakeup chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Doze/App Standby** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Batch thay polling khi có thể

Nếu backend hỗ trợ push/stream/sự kiện (event / 이벤트), không nhất thiết poll 5 phút. Nếu công việc (work / 작업) không cần chính xác (exact / 정확한) thời gian (time / 시간), để WorkManager/hệ thống (system / 시스템) batch giúp battery.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **17. Doze/App Standby** tiếp nhận điểm tựa từ **16. Batch thay polling khi có thể** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. kiểm thử (test / 테스트) slow mạng (network / 네트워크)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Doze/App Standby

Background thực thi (execution / 실행) có thể bị delay khi thiết bị (device / 장치) idle. lô-gic nghiệp vụ (business logic / 비즈니스 로직) không nên assume periodic worker chạy chính xác từng phút.

Nếu sản phẩm (product / 제품) yêu cầu hard realtime, cần kiến trúc (architecture / 아키텍처)/máy chủ (server / 서버) push/user-visible foreground hành vi (behavior / 동작) phù hợp hơn.

# Mạng (network / 네트워크) chất lượng (quality / 품질)

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **18. kiểm thử (test / 테스트) slow mạng (network / 네트워크)** tiếp nhận điểm tựa từ **17. Doze/App Standby** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. thử lại (retry / 재시도) storm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. kiểm thử (test / 테스트) slow mạng (network / 네트워크)

Wi-Fi văn phòng che giấu race/loading bug. kiểm thử (test / 테스트) độ trễ (latency / 지연 시간) cao, packet mất mát (loss / 손실), offline giữa yêu cầu (request / 요청), reconnect và máy chủ (server / 서버) hết thời gian chờ (timeout / 타임아웃).

UI cần distinguish loading initial và refreshing existing content.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **19. thử lại (retry / 재시도) storm** tiếp nhận điểm tựa từ **18. kiểm thử (test / 테스트) slow mạng (network / 네트워크)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Payload kích thước (size / 크기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. thử lại (retry / 재시도) storm

Nếu 1 triệu thiết bị (device / 장치) cùng thử lại (retry / 재시도) ngay sau backend outage, exponential backoff + jitter giúp tránh thundering herd.

Thử lại (retry / 재시도) chính sách (policy / 정책) là distributed-system concern.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **20. Payload kích thước (size / 크기)** tiếp nhận điểm tựa từ **19. thử lại (retry / 재시도) storm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Low-memory thiết bị (device / 장치)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Payload kích thước (size / 크기)

Mobile mạng (network / 네트워크) đắt và không ổn định. Đặc tả API (API contract / API 계약) cần pagination, compression, selective fields/caching khi dataset lớn.

Đừng download full lịch sử (history / 이력) mỗi app launch.

# Bộ nhớ (memory / 메모리)/CPU chất lượng (quality / 품질)

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **21. Low-memory thiết bị (device / 장치)** tiếp nhận điểm tựa từ **20. Payload kích thước (size / 크기)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Thermal throttling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Low-memory thiết bị (device / 장치)

Kiểm thử (test / 테스트) thiết bị (device / 장치) RAM thấp giúp phát hiện bitmap bộ nhớ đệm (cache / 캐시), giant danh sách (list / 목록), WebView/media bộ nhớ (memory / 메모리) và startup overhead.

Background tiến trình (process / 프로세스) có thể bị kill thường xuyên hơn, làm trạng thái (state / 상태) restoration bug lộ ra.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **22. Thermal throttling** tiếp nhận điểm tựa từ **21. Low-memory thiết bị (device / 장치)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Không giả định mọi OEM giống điểm ảnh (pixel / 픽셀)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Thermal throttling

CPU benchmark kéo dài có thể khác khi thiết bị (device / 장치) nóng. Heavy camera/ML/video tính năng (feature / 기능) nên kiểm thử (test / 테스트) thermal/battery thực tế chứ không chỉ một run ngắn.

# OEM fragmentation

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **23. Không giả định mọi OEM giống điểm ảnh (pixel / 픽셀)** tiếp nhận điểm tựa từ **22. Thermal throttling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. gỡ lỗi (debug / 디버그) tính năng (feature / 기능) không lọt môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Không giả định mọi OEM giống điểm ảnh (pixel / 픽셀)

Một số OEM có aggressive battery/background management, camera/Bluetooth ngăn xếp (stack / 스택) khác hoặc permission UI khác.

Không viết mã (code / 코드) “detect Samsung rồi hack” ngay từ đầu. Trước tiên dựa API công khai (public API / 공개 API); chỉ có workaround khi có bằng chứng (evidence / 증거), isolate workaround và document phạm vi (scope / 범위)/phiên bản (version / 버전).

# Bảo mật (security / 보안) chất lượng (quality / 품질)

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **24. gỡ lỗi (debug / 디버그) tính năng (feature / 기능) không lọt môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **23. Không giả định mọi OEM giống điểm ảnh (pixel / 픽셀)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Log redaction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. gỡ lỗi (debug / 디버그) tính năng (feature / 기능) không lọt môi trường vận hành (production / 운영 환경)

Bản phát hành (release / 릴리스) bản dựng (build / 빌드) phải kiểm tra:

```text
no debug endpoint
no trust-all certificate
no verbose sensitive logging
no test account secret
no WebView debugging ngoài ý muốn
no backup exposure ngoài policy
```

Bản dựng (build / 빌드) variant/cấu hình (configuration / 구성) nên khiến insecure gỡ lỗi (debug / 디버그) hành vi (behavior / 동작) khó lọt bản phát hành (release / 릴리스).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **25. Log redaction** tiếp nhận điểm tựa từ **24. gỡ lỗi (debug / 디버그) tính năng (feature / 기능) không lọt môi trường vận hành (production / 운영 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Screenshot/screen recording sensitivity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Log redaction

Đơn vị từ (token / 토큰), password, full card/account identifier, sensitive PII không nên log. Structured logging nên redaction từ nguồn (source / 소스) thay vì hy vọng dashboard filter sau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **26. Screenshot/screen recording sensitivity** tiếp nhận điểm tựa từ **25. Log redaction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. dữ liệu (data / 데이터) inventory** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Screenshot/screen recording sensitivity

Một số screen như credential/payment/health có thể cần `FLAG_SECURE` hoặc chính sách (policy / 정책) tương đương tùy yêu cầu (requirement / 요구사항). Nhưng đừng bật toàn app nếu làm hỏng legitimate người dùng (user / 사용자) workflow không cần thiết.

# Privacy chất lượng (quality / 품질)

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **26. Screenshot/screen recording sensitivity** nêu điều cần giải thích; **27. dữ liệu (data / 데이터) inventory** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **28. dữ liệu (data / 데이터) minimization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. dữ liệu (data / 데이터) inventory

Trước bản phát hành (release / 릴리스), biết app thu dữ liệu gì:

```text
field/event
purpose
storage location
retention
third-party recipient
user control
```

Nếu nhóm (team / 팀) không biết sự kiện (event / 이벤트) analytics chứa gì, rất khó đảm bảo privacy hoặc dữ liệu (data / 데이터) an toàn (safety / 안전) declaration đúng.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **27. dữ liệu (data / 데이터) inventory** nêu điều cần giải thích; **28. dữ liệu (data / 데이터) minimization** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **29. Analytics khác telemetry độ tin cậy (reliability / 신뢰성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. dữ liệu (data / 데이터) minimization

Không gửi raw GPS/contacts/thiết bị (device / 장치) identifier nếu nghiệp vụ (business / 비즈니스) chỉ cần derived region/count.

Privacy tốt thường bắt đầu bằng **không thu dữ liệu không cần**.

# Analytics và khả năng quan sát (observability / 관측 가능성)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **28. dữ liệu (data / 데이터) minimization** nêu điều cần giải thích; **29. Analytics khác telemetry độ tin cậy (reliability / 신뢰성)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **30. sự kiện (event / 이벤트) lược đồ (schema / 스키마) versioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Analytics khác telemetry độ tin cậy (reliability / 신뢰성)

Sản phẩm (product / 제품) analytics trả lời người dùng (user / 사용자) làm gì. Operational telemetry trả lời app có khỏe không.

Đừng dùng sự kiện (event / 이벤트) analytics như crash/dấu vết (trace / 추적) hệ thống (system / 시스템) thay thế.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **30. sự kiện (event / 이벤트) lược đồ (schema / 스키마) versioning** tiếp nhận điểm tựa từ **29. Analytics khác telemetry độ tin cậy (reliability / 신뢰성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Crash-free không đủ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. sự kiện (event / 이벤트) lược đồ (schema / 스키마) versioning

Analytics sự kiện (event / 이벤트) là đặc tả hợp đồng (contract / 계약) với dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인). Rename trường dữ liệu (field / 필드) tùy tiện phá dashboard/experiment.

```text
checkout_started.v1
checkout_completed.v1
```

không nhất thiết phải phiên bản (version / 버전) trong tên, nhưng cần quản trị (governance / 거버넌스)/lược đồ (schema / 스키마) đặc tả hợp đồng (contract / 계약) rõ.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **31. Crash-free không đủ** tiếp nhận điểm tựa từ **30. sự kiện (event / 이벤트) lược đồ (schema / 스키마) versioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Flag là di chuyển (migration / 마이그레이션) công cụ (tool / 도구), không phải rác vĩnh viễn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Crash-free không đủ

App không crash vẫn có thể slow, ANR, login vòng lặp (loop / 루프) hoặc sync thất bại (fail / 실패) silent. Monitor thêm ANR, startup, jank, mạng (network / 네트워크) lỗi (error / 오류), sync backlog và nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) quan trọng.

# Cờ tính năng (feature flag / 기능 플래그)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **32. Flag là di chuyển (migration / 마이그레이션) công cụ (tool / 도구), không phải rác vĩnh viễn** tiếp nhận điểm tựa từ **31. Crash-free không đủ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Server-driven flag và offline** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Flag là di chuyển (migration / 마이그레이션) công cụ (tool / 도구), không phải rác vĩnh viễn

Cờ tính năng (feature flag / 기능 플래그) giúp rollout/kill-switch. Nhưng flag cũ tạo combinatorial độ phức tạp (complexity / 복잡도).

Mỗi flag cần đơn vị sở hữu (owner / 오너), default, expiry/removal plan.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **33. Server-driven flag và offline** tiếp nhận điểm tựa từ **32. Flag là di chuyển (migration / 마이그레이션) công cụ (tool / 도구), không phải rác vĩnh viễn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. cổng chất lượng (quality gate / 품질 게이트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Server-driven flag và offline

App offline cần default/cached flag hành vi (behavior / 동작). Không để app startup khối (block / 블록) vô hạn chờ cấu hình (config / 설정) remote.

# Bản phát hành (release / 릴리스) chuỗi xử lý (pipeline / 파이프라인)

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **34. cổng chất lượng (quality gate / 품질 게이트)** tiếp nhận điểm tựa từ **33. Server-driven flag và offline** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Signed sản phẩm tạo ra (artifact / 산출물) là immutable đầu ra (output / 출력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. cổng chất lượng (quality gate / 품질 게이트)

Một chuỗi xử lý (pipeline / 파이프라인) môi trường vận hành (production / 운영 환경) có thể gồm:

```text
compile
→ unit test
→ lint/static analysis
→ integration test
→ instrumentation smoke
→ assemble/sign
→ artifact scan
→ internal track
→ staged rollout
→ monitor
→ expand / pause / rollback
```

Không phải nhóm (team / 팀) nào cần mọi gate trên mỗi PR; phân lớp theo chi phí (cost / 비용) và rủi ro (risk / 위험).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **35. Signed sản phẩm tạo ra (artifact / 산출물) là immutable đầu ra (output / 출력)** tiếp nhận điểm tựa từ **34. cổng chất lượng (quality gate / 품질 게이트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. phiên bản (version / 버전) mã (code / 코드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Signed sản phẩm tạo ra (artifact / 산출물) là immutable đầu ra (output / 출력)

Sản phẩm tạo ra (artifact / 산출물) đã QA/rà soát (review / 검토) nên chính là sản phẩm tạo ra (artifact / 산출물) được promote. Tránh rebuild khác cấu hình (config / 설정) giữa staging và môi trường vận hành (production / 운영 환경) nếu không cần, vì bạn mất traceability.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **36. phiên bản (version / 버전) mã (code / 코드)** tiếp nhận điểm tựa từ **35. Signed sản phẩm tạo ra (artifact / 산출물) là immutable đầu ra (output / 출력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. AAB và động (dynamic / 동적) delivery** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. phiên bản (version / 버전) mã (code / 코드)

`versionCode` phải tăng để Play cập nhật (update / 업데이트). `versionName` là display phiên bản (version / 버전). bản dựng (build / 빌드) siêu dữ liệu (metadata / 메타데이터)/lần ghi nhận (commit / 커밋) SHA nên được dấu vết (trace / 추적) trong khả năng quan sát (observability / 관측 가능성) để biết crash đến từ sản phẩm tạo ra (artifact / 산출물) nào.

# Play/App phân phối (distribution / 분포) awareness

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **37. AAB và động (dynamic / 동적) delivery** tiếp nhận điểm tựa từ **36. phiên bản (version / 버전) mã (code / 코드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. mục tiêu (target / 대상) API deadline** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. AAB và động (dynamic / 동적) delivery

Android App Bundle cho Play generate APK tối ưu theo thiết bị (device / 장치). Nếu app dùng động (dynamic / 동적) tính năng (feature / 기능)/mô-đun (module / 모듈)/tài nguyên (resource / 자원) delivery, kiểm thử (test / 테스트) install/cập nhật (update / 업데이트) đường dẫn (path / 경로) thực tế trên phân phối (distribution / 분포) nhánh học (track / 트랙) chứ không chỉ cục bộ (local / 로컬) APK.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **38. mục tiêu (target / 대상) API deadline** tiếp nhận điểm tựa từ **37. AAB và động (dynamic / 동적) delivery** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Auto Backup không phải luôn desirable cho mọi dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. mục tiêu (target / 대상) API deadline

Google Play thay đổi mục tiêu (target / 대상) API yêu cầu (requirement / 요구사항) theo thời gian. bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링) phải có cadence upgrade trước deadline, không đợi tuần cuối mới nâng mục tiêu (target / 대상) và xử lý tất cả hành vi (behavior / 동작) thay đổi (change / 변경) cùng lúc.

# Backup và restore

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **38. mục tiêu (target / 대상) API deadline** nêu điều cần giải thích; **39. Auto Backup không phải luôn desirable cho mọi dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **40. Restore phiên bản (version / 버전) mismatch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Auto Backup không phải luôn desirable cho mọi dữ liệu (data / 데이터)

Đơn vị từ (token / 토큰)/secret/device-bound credential có thể không nên restore sang thiết bị (device / 장치) mới. cơ sở dữ liệu (database / 데이터베이스)/người dùng (user / 사용자) preference khác có thể benefit từ backup.

Rà soát (review / 검토) backup quy tắc (rule / 규칙) theo dữ liệu (data / 데이터) sensitivity và máy chủ (server / 서버) rehydration năng lực (capability / 역량).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **39. Auto Backup không phải luôn desirable cho mọi dữ liệu (data / 데이터)** nêu điều cần giải thích; **40. Restore phiên bản (version / 버전) mismatch** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **41. Production-like trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Restore phiên bản (version / 버전) mismatch

Backup từ app phiên bản (version / 버전) cũ có thể được restore vào phiên bản (version / 버전) mới. Persistence tầng (layer / 계층) phải xử lý lược đồ (schema / 스키마)/dữ liệu (data / 데이터) phiên bản (version / 버전) đúng.

# Kiểm thử (test / 테스트) account và seed dữ liệu (data / 데이터)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **41. Production-like trạng thái (state / 상태)** tiếp nhận điểm tựa từ **40. Restore phiên bản (version / 버전) mismatch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. Mobile sự cố (incident / 인시던트) khác máy chủ (server / 서버) sự cố (incident / 인시던트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Production-like trạng thái (state / 상태)

QA cần account/dữ liệu (data / 데이터) mô phỏng:

```text
new user
heavy user
expired session
offline pending mutations
legacy schema data
restricted entitlement
large dataset
```

Happy-path empty account không phát hiện nhiều bug môi trường vận hành (production / 운영 환경).

# Sự cố (incident / 인시던트) readiness

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **42. Mobile sự cố (incident / 인시던트) khác máy chủ (server / 서버) sự cố (incident / 인시던트)** tiếp nhận điểm tựa từ **41. Production-like trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Diagnose theo phiên bản (version / 버전)/thiết bị (device / 장치) cohort** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. Mobile sự cố (incident / 인시던트) khác máy chủ (server / 서버) sự cố (incident / 인시던트)

Máy chủ (server / 서버) fix có thể deploy phút. Mobile nhị phân (binary / 이진) đã nằm trên hàng triệu thiết bị (device / 장치) không cập nhật (update / 업데이트) ngay.

Do đó cần:

```text
server backward compatibility
feature kill switch
config fallback
staged rollout
old-client support window
```

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **43. Diagnose theo phiên bản (version / 버전)/thiết bị (device / 장치) cohort** tiếp nhận điểm tựa từ **42. Mobile sự cố (incident / 인시던트) khác máy chủ (server / 서버) sự cố (incident / 인시던트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. tính năng (feature / 기능) complete không chỉ UI xong** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Diagnose theo phiên bản (version / 버전)/thiết bị (device / 장치) cohort

Khi crash tăng, breakdown theo app phiên bản (version / 버전), OS, OEM/thiết bị (device / 장치) mô hình (model / 모델), locale, cờ tính năng (feature flag / 기능 플래그) cohort và rollout percentage giúp tìm regression nhanh.

# Definition of Done môi trường vận hành (production / 운영 환경)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **44. tính năng (feature / 기능) complete không chỉ UI xong** tiếp nhận điểm tựa từ **43. Diagnose theo phiên bản (version / 버전)/thiết bị (device / 장치) cohort** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. chất lượng (quality / 품질) là kiến trúc (architecture / 아키텍처) thuộc tính (property / 속성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. tính năng (feature / 기능) complete không chỉ UI xong

Một tính năng (feature / 기능) quan trọng chỉ nên xem production-ready khi đã trả lời:

```text
state restore thế nào?
offline thế nào?
permission denied thế nào?
loading/error/retry thế nào?
accessibility thế nào?
locale/large font/RTL thế nào?
small/large window thế nào?
analytics/telemetry gì?
data sensitive gì?
test migration gì?
rollback thế nào?
```

Không phải mọi tính năng (feature / 기능) cần cùng mức rigor; payment/auth/sync cần sâu hơn tooltip đơn giản. Nhưng câu hỏi phải được cân nhắc.

# Cấp cao (senior / 시니어) Notes

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **45. chất lượng (quality / 품질) là kiến trúc (architecture / 아키텍처) thuộc tính (property / 속성)** tiếp nhận điểm tựa từ **44. tính năng (feature / 기능) complete không chỉ UI xong** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **46. ma trận (matrix / 행렬) phải dựa telemetry** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. chất lượng (quality / 품질) là kiến trúc (architecture / 아키텍처) thuộc tính (property / 속성)

Nếu mã (code / 코드) không có clear nguồn chuẩn (source of truth / 정본), không thể kiểm thử (test / 테스트) offline đúng. Nếu điều hướng (navigation / 내비게이션) truyền giant đối tượng (object / 객체), tiến trình (process / 프로세스) restore khó. Nếu networking không typed lỗi (error / 오류), UI khôi phục (recovery / 복구) mơ hồ. QA không thể “kiểm thử (test / 테스트) ra” một kiến trúc (architecture / 아키텍처) thiếu khôi phục (recovery / 복구) đường dẫn (path / 경로).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **46. ma trận (matrix / 행렬) phải dựa telemetry** tiếp nhận điểm tựa từ **45. chất lượng (quality / 품질) là kiến trúc (architecture / 아키텍처) thuộc tính (property / 속성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **47. Backward tính tương thích (compatibility / 호환성) là mobile superpower** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. ma trận (matrix / 행렬) phải dựa telemetry

Sau môi trường vận hành (production / 운영 환경), dùng crash/thiết bị (device / 장치)/OS/người dùng (user / 사용자) phân phối (distribution / 분포) để cập nhật kiểm thử (test / 테스트) ma trận (matrix / 행렬). Nếu 40% người dùng (user / 사용자) dùng một OEM cụ thể, thiết bị (device / 장치) đó quan trọng hơn một flagship hiếm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **47. Backward tính tương thích (compatibility / 호환성) là mobile superpower** tiếp nhận điểm tựa từ **46. ma trận (matrix / 행렬) phải dựa telemetry** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **48. Không tối ưu chỉ số (metric / 지표) đơn lẻ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. Backward tính tương thích (compatibility / 호환성) là mobile superpower

Máy chủ (server / 서버)/API có khả năng phục vụ nhiều app phiên bản (version / 버전) giúp rollout an toàn, sự cố (incident / 인시던트) khôi phục (recovery / 복구) nhanh và người dùng (user / 사용자) không bị bắt cập nhật (update / 업데이트) ngay.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 13 — môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질): thiết bị (device / 장치) ma trận (matrix / 행렬), Localization, Battery, Privacy và bản phát hành (release / 릴리스) Readiness**, **48. Không tối ưu chỉ số (metric / 지표) đơn lẻ** tiếp nhận điểm tựa từ **47. Backward tính tương thích (compatibility / 호환성) là mobile superpower** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 48. Không tối ưu chỉ số (metric / 지표) đơn lẻ

Giảm startup bằng lazy quá mức có thể làm first tương tác (interaction / 상호작용) lag. Giảm mạng (network / 네트워크) yêu cầu (request / 요청) bằng bộ nhớ đệm (cache / 캐시) quá lâu có thể stale. Giảm permission prompt bằng broad permission xin một lần có thể tệ privacy. Tối ưu luôn dựa người dùng (user / 사용자) journey và hệ thống (system / 시스템) sự đánh đổi (trade-off / 트레이드오프).

# Release-readiness checklist rút gọn

Trước bản phát hành (release / 릴리스) lớn, rà soát (review / 검토) theo nhóm: tính tương thích (compatibility / 호환성)/phiên bản (version / 버전); persistence/di chuyển (migration / 마이그레이션); permission/năng lực (capability / 역량); vòng đời (lifecycle / 생명주기)/tiến trình (process / 프로세스) death; offline/mạng (network / 네트워크); localization/RTL/font quy mô (scale / 규모); khả năng tiếp cận (accessibility / 접근성); adaptive UI; bộ nhớ (memory / 메모리)/hiệu năng (performance / 성능)/battery; bảo mật (security / 보안)/privacy; analytics/khả năng quan sát (observability / 관측 가능성); CI/signing/sản phẩm tạo ra (artifact / 산출물); staged rollout/quay lui (rollback / 롤백).

Checklist không thay lập luận (reasoning / 추론). Nếu một mục “N/A”, nhóm (team / 팀) nên biết vì sao N/A.

# Kết thúc chapter

Sau chapter này, bạn nên có khả năng xây thiết bị (device / 장치)/kiểm thử (test / 테스트) ma trận (matrix / 행렬) theo rủi ro (risk / 위험); kiểm thử (test / 테스트) upgrade thay vì chỉ fresh install; phân biệt localization, timezone và RTL concern; đưa font scaling/khả năng tiếp cận (accessibility / 접근성) vào tính đúng đắn (correctness / 정확성); đánh giá battery/background công việc (work / 작업); kiểm thử (test / 테스트) slow/offline mạng (network / 네트워크); theo dõi OEM/low-memory hành vi (behavior / 동작); quản privacy/dữ liệu (data / 데이터) inventory; thiết kế cờ tính năng (feature flag / 기능 플래그)/rollout; và định nghĩa production-ready tính năng (feature / 기능) dựa trên khôi phục (recovery / 복구), tính tương thích (compatibility / 호환성) và khả năng quan sát (observability / 관측 가능성) chứ không chỉ screenshot đúng thiết kế.

> **Bàn giao:** Sau **48. Không tối ưu chỉ số (metric / 지표) đơn lẻ**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
