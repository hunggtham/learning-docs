# Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. lược đồ (schema / 스키마) là đặc tả hợp đồng (contract / 계약) chứ không chỉ cấu trúc (structure / 구조)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Backward và forward tính tương thích (compatibility / 호환성)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Hệ thống môi trường vận hành (production / 운영 환경) hiếm khi nâng cấp toàn bộ thành phần cùng lúc. Trong vài phút, vài giờ hoặc nhiều tuần, máy khách (client / 클라이언트) cũ có thể nói chuyện với máy chủ (server / 서버) mới; producer mới gửi dữ liệu cho bên tiêu thụ (consumer / 소비자) cũ; cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) mới phục vụ ứng dụng (application / 애플리케이션) instance chưa restart. Vì vậy **tính tương thích (compatibility / 호환성)** không phải vấn đề phụ của triển khai (deployment / 배포) mà là thuộc tính tính đúng đắn (correctness / 정확성) của hệ thống đang tiến hóa.

Chapter này nối dữ liệu (data / 데이터) modeling, API thiết kế (design / 설계), sự kiện (event / 이벤트) streaming và phân tán (distributed / 분산) triển khai (deployment / 배포). Câu hỏi trung tâm là: **làm thế nào thay đổi biểu diễn (representation / 표현) mà các thành phần đang chạy ở nhiều phiên bản (version / 버전) vẫn hiểu nhau đủ đúng?**

## 1. lược đồ (schema / 스키마) là đặc tả hợp đồng (contract / 계약) chứ không chỉ cấu trúc (structure / 구조)

Một trường dữ liệu (field / 필드) `status` trong JSON không chỉ là chuỗi. bên tiêu thụ (consumer / 소비자) có thể giả định tập giá trị, nullability, ý nghĩa thời gian hoặc quan hệ với trường dữ liệu (field / 필드) khác.

```json
{
  "orderId": "A-100",
  "status": "PAID"
}
```

Nếu producer thêm `PARTIALLY_REFUNDED`, cú pháp (syntax / 문법) vẫn hợp lệ nhưng bên tiêu thụ (consumer / 소비자) dùng exhaustive switch cũ có thể crash hoặc xử lý sai.

Do đó lược đồ (schema / 스키마) có hai lớp: biểu diễn (representation / 표현) đặc tả hợp đồng (contract / 계약) và ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약).

> **Chuyển mạch:** Trong **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **2. Backward và forward tính tương thích (compatibility / 호환성)** tiếp nhận điểm tựa từ **1. lược đồ (schema / 스키마) là đặc tả hợp đồng (contract / 계약) chứ không chỉ cấu trúc (structure / 구조)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Additive thay đổi (change / 변경) thường an toàn hơn destructive thay đổi (change / 변경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Backward và forward tính tương thích (compatibility / 호환성)

**Tương thích ngược (backward compatibility)** thường nghĩa reader mới đọc được dữ liệu do writer cũ tạo. **Tương thích xuôi (forward compatibility)** nghĩa reader cũ vẫn xử lý được dữ liệu writer mới trong phạm vi thiết kế.

Trong rolling triển khai (deployment / 배포), thường cần cả hai theo một khoảng thời gian vì phiên bản (version / 버전) cũ và mới cùng tồn tại.

Không nên dùng hai thuật ngữ này mà không nói rõ ai là reader, ai là writer; documentation giữa các hệ sinh thái đôi khi dùng góc nhìn khác nhau.

> **Chuyển mạch:** Ở chặng này của **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **3. Additive thay đổi (change / 변경) thường an toàn hơn destructive thay đổi (change / 변경)** tiếp nhận điểm tựa từ **2. Backward và forward tính tương thích (compatibility / 호환성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Tolerant reader và giới hạn của nó** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Additive thay đổi (change / 변경) thường an toàn hơn destructive thay đổi (change / 변경)

Thêm optional trường dữ liệu (field / 필드) thường dễ tương thích nếu reader cũ bỏ qua trường dữ liệu (field / 필드) lạ:

```json
{
  "orderId": "A-100",
  "status": "PAID",
  "paymentMethod": "CARD"
}
```

Nhưng “thêm trường dữ liệu (field / 필드)” không tự động an toàn. Nếu trường dữ liệu (field / 필드) mới thay đổi interpretation của trường dữ liệu (field / 필드) cũ, ngữ nghĩa (semantic / 의미적) tính tương thích (compatibility / 호환성) vẫn có thể vỡ.

Rename thường thực chất là `add new → dual support → migrate → remove old`, không phải đổi tên nguyên tử.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **3. Additive thay đổi (change / 변경) thường an toàn hơn destructive thay đổi (change / 변경)** đã nêu tiêu chí phân biệt, còn **4. Tolerant reader và giới hạn của nó** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **5. Enum là điểm tính tương thích (compatibility / 호환성) dễ vỡ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Tolerant reader và giới hạn của nó

Tolerant reader bỏ qua thông tin không hiểu, giúp evolution. Nhưng quá tolerant có thể che lỗi. Nếu security-sensitive trường dữ liệu (field / 필드) bị bỏ qua, hệ thống có thể chấp nhận message mà đáng ra phải reject.

Vì vậy tolerance phải có ranh giới (boundary / 경계): unknown siêu dữ liệu (metadata / 메타데이터) có thể bỏ qua, nhưng unknown authorization chế độ (mode / 모드) có thể phải thất bại (fail / 실패) closed.

> **Chuyển mạch:** Trong **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **4. Tolerant reader và giới hạn của nó** đã nêu tiêu chí phân biệt, còn **5. Enum là điểm tính tương thích (compatibility / 호환성) dễ vỡ** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **6. nhị phân (binary / 이진) protocols và trường dữ liệu (field / 필드) định danh (identity / 식별자)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Enum là điểm tính tương thích (compatibility / 호환성) dễ vỡ

Nhà phát triển (developer / 개발자) thường xem enum là closed set:

```text
PENDING | PAID | CANCELLED
```

Phân tán (distributed / 분산) giao thức (protocol / 프로토콜) nên cân nhắc khả năng writer mới thêm giá trị. bên tiêu thụ (consumer / 소비자) cũ cần chiến lược như `UNKNOWN`, fallback an toàn hoặc tường minh (explicit / 명시적) rejection.

Đây là sự đánh đổi (trade-off / 트레이드오프) giữa evolvability và khả năng phát hiện dữ liệu bất thường.

> **Chuyển mạch:** Ở chặng này của **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **5. Enum là điểm tính tương thích (compatibility / 호환성) dễ vỡ** nêu điều cần giải thích; **6. nhị phân (binary / 이진) protocols và trường dữ liệu (field / 필드) định danh (identity / 식별자)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) trong rolling triển khai (deployment / 배포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. nhị phân (binary / 이진) protocols và trường dữ liệu (field / 필드) định danh (identity / 식별자)

Các serialization hệ thống (system / 시스템) như giao thức (protocol / 프로토콜) Buffers không chỉ dựa vào tên trường dữ liệu (field / 필드) mà dùng numeric trường dữ liệu (field / 필드) identifier trên wire. Nếu tái sử dụng identifier đã xóa cho nghĩa mới, dữ liệu cũ có thể bị giải mã thành ý nghĩa sai.

Điểm sâu ở đây là **wire định danh (identity / 식별자) phải ổn định lâu hơn source-code name**. Rename nguồn (source / 소스) trường dữ liệu (field / 필드) có thể an toàn trong khi reuse wire tag có thể nguy hiểm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **6. nhị phân (binary / 이진) protocols và trường dữ liệu (field / 필드) định danh (identity / 식별자)** nêu điều cần giải thích; **7. cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) trong rolling triển khai (deployment / 배포)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. Dual ghi (write / 쓰기) và consistency rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) trong rolling triển khai (deployment / 배포)

Giả sử cần đổi `full_name` thành `display_name`. Nếu di chuyển (migration / 마이그레이션) rename column trước khi ứng dụng (application / 애플리케이션) cũ dừng, instance cũ có thể lỗi.

Mẫu (pattern / 패턴) **expand–migrate–đặc tả hợp đồng (contract / 계약)** giải quyết bằng các giai đoạn:

```text
expand: thêm representation mới nhưng giữ cũ
migrate: code/data chuyển dần
contract: xóa representation cũ khi không còn reader/writer phụ thuộc
```

Điều này biến di chuyển (migration / 마이그레이션) từ một mutation lớn thành giao thức (protocol / 프로토콜) giữa các phiên bản (version / 버전).

> **Chuyển mạch:** Trong **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **7. cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) trong rolling triển khai (deployment / 배포)** nêu điều cần giải thích; **8. Dual ghi (write / 쓰기) và consistency rủi ro (risk / 위험)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. Backfill là tải công việc (workload / 워크로드) môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Dual ghi (write / 쓰기) và consistency rủi ro (risk / 위험)

Trong giai đoạn chuyển tiếp, ứng dụng (application / 애플리케이션) đôi khi ghi cả column cũ và mới. Hai ghi (write / 쓰기) có thể lệch nếu không nằm trong cùng giao dịch (transaction / 트랜잭션) hoặc lô-gic (logic / 논리) ánh xạ (mapping / 매핑) thay đổi.

Nếu dual ghi (write / 쓰기) sang hai dịch vụ (service / 서비스)/cơ sở dữ liệu (database / 데이터베이스) độc lập, ta quay lại phân tán (distributed / 분산) dual-write bài toán (problem / 문제). Khi đó outbox/event-driven di chuyển (migration / 마이그레이션) có thể phù hợp hơn.

Xem [distributed transactions](../../05_data_databases/advanced/07_distributed_transactions_2pc_consensus_sagas_and_outbox.md).

> **Chuyển mạch:** Ở chặng này của **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **9. Backfill là tải công việc (workload / 워크로드) môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **8. Dual ghi (write / 쓰기) và consistency rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. sự kiện (event / 이벤트) lược đồ (schema / 스키마) khó xóa hơn cơ sở dữ liệu (database / 데이터베이스) column** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Backfill là tải công việc (workload / 워크로드) môi trường vận hành (production / 운영 환경)

Backfill hàng triệu row không chỉ là dữ liệu (data / 데이터) script. Nó cạnh tranh I/O, buffer pool, WAL bandwidth, replica lag và khóa (lock / 잠금) với traffic thật.

Một di chuyển (migration / 마이그레이션) logically correct vẫn có thể gây outage vì tài nguyên (resource / 자원) saturation. Vì vậy cần batch, tỷ lệ (rate / 비율) limit, checkpoint, thử lại (retry / 재시도) và khả năng quan sát (observability / 관측 가능성).

Đây là liên kết (connection / 연결) trực tiếp giữa lược đồ (schema / 스키마) evolution và sức chứa (capacity / 용량) planning.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **9. Backfill là tải công việc (workload / 워크로드) môi trường vận hành (production / 운영 환경)** nêu điều cần giải thích; **10. sự kiện (event / 이벤트) lược đồ (schema / 스키마) khó xóa hơn cơ sở dữ liệu (database / 데이터베이스) column** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. API versioning không phải lựa chọn đầu tiên cho mọi thay đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. sự kiện (event / 이벤트) lược đồ (schema / 스키마) khó xóa hơn cơ sở dữ liệu (database / 데이터베이스) column

Cơ sở dữ liệu (database / 데이터베이스) row có thể được di chuyển (migration / 마이그레이션) tại chỗ. sự kiện (event / 이벤트) log có thể giữ message nhiều năm và được replay. bên tiêu thụ (consumer / 소비자) mới phải đối mặt historical lược đồ (schema / 스키마).

Nếu stream được dùng cho replay, tính tương thích (compatibility / 호환성) horizon gần bằng retention horizon, không chỉ triển khai (deployment / 배포) cửa sổ (window / 윈도우).

Lược đồ (schema / 스키마) registry giúp kiểm tra structural tính tương thích (compatibility / 호환성), nhưng không chứng minh ngữ nghĩa (semantic / 의미적) tính tương thích (compatibility / 호환성).

> **Chuyển mạch:** Trong **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **10. sự kiện (event / 이벤트) lược đồ (schema / 스키마) khó xóa hơn cơ sở dữ liệu (database / 데이터베이스) column** nêu điều cần giải thích; **11. API versioning không phải lựa chọn đầu tiên cho mọi thay đổi** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. năng lực (capability / 역량) negotiation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. API versioning không phải lựa chọn đầu tiên cho mọi thay đổi

Tạo `/v2` cho mỗi thay đổi nhỏ tạo nhiều phiên bản (version / 버전) phải duy trì. Additive evolution thường tốt hơn khi ngữ nghĩa (semantics / 의미론) cốt lõi không đổi.

Phiên bản (version / 버전) mới hợp lý khi đặc tả hợp đồng (contract / 계약) thực sự thay đổi theo cách không thể diễn đạt tương thích, ví dụ meaning của tài nguyên (resource / 자원) hoặc workflow thay đổi lớn.

Versioning không xóa di chuyển (migration / 마이그레이션); nó chuyển di chuyển (migration / 마이그레이션) sang máy khách (client / 클라이언트) ecosystem.

> **Chuyển mạch:** Ở chặng này của **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **12. năng lực (capability / 역량) negotiation** tiếp nhận điểm tựa từ **11. API versioning không phải lựa chọn đầu tiên cho mọi thay đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. ngữ nghĩa (semantic / 의미적) versioning và phân tán (distributed / 분산) reality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. năng lực (capability / 역량) negotiation

Một số giao thức (protocol / 프로토콜) cho phép hai phía thương lượng năng lực (capability / 역량) thay vì suy luận từ phiên bản (version / 버전) number:

```text
client supports: compression=A,B; feature=X
server supports: compression=B,C; feature=X,Y
intersection: compression=B; feature=X
```

Năng lực (capability / 역량) negotiation hữu ích khi tính năng (feature / 기능) evolution không tuyến tính. Nhưng giao thức (protocol / 프로토콜) handshake và fallback trở nên phức tạp hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **13. ngữ nghĩa (semantic / 의미적) versioning và phân tán (distributed / 분산) reality** tiếp nhận điểm tựa từ **12. năng lực (capability / 역량) negotiation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Consumer-driven đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. ngữ nghĩa (semantic / 의미적) versioning và phân tán (distributed / 분산) reality

`major.minor.patch` là communication convention, không phải proof về tính tương thích (compatibility / 호환성). Một “minor” bản phát hành (release / 릴리스) vẫn có thể phá bên tiêu thụ (consumer / 소비자) nếu hành vi (behavior / 동작) undocumented đã trở thành phụ thuộc (dependency / 의존성) thực tế.

Đặc tả hợp đồng (contract / 계약) tests và traffic bằng chứng (evidence / 증거) quan trọng hơn label phiên bản (version / 버전).

> **Chuyển mạch:** Trong **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **14. Consumer-driven đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **13. ngữ nghĩa (semantic / 의미적) versioning và phân tán (distributed / 분산) reality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Unknown fields, defaults và dữ liệu bị mất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Consumer-driven đặc tả hợp đồng (contract / 계약)

Provider không luôn biết bên tiêu thụ (consumer / 소비자) đang dựa vào trường dữ liệu (field / 필드) nào. Consumer-driven đặc tả hợp đồng (contract / 계약) ghi lại expectation của bên tiêu thụ (consumer / 소비자) và kiểm tra provider thay đổi (change / 변경) trước triển khai (deployment / 배포).

Nhưng kiểm thử (test / 테스트) chỉ phản ánh bên tiêu thụ (consumer / 소비자) đã đăng ký. Shadow bên tiêu thụ (consumer / 소비자), ad-hoc analytics hoặc bên ngoài (external / 외부) tích hợp (integration / 통합) vẫn có thể tồn tại. quản trị (governance / 거버넌스) và khả năng quan sát (observability / 관측 가능성) vẫn cần thiết.

> **Chuyển mạch:** Ở chặng này của **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **14. Consumer-driven đặc tả hợp đồng (contract / 계약)** nêu điều cần giải thích; **15. Unknown fields, defaults và dữ liệu bị mất** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Unknown fields, defaults và dữ liệu bị mất

Một proxy đọc message mới bằng lược đồ (schema / 스키마) cũ rồi serialize lại có thể làm mất unknown trường dữ liệu (field / 필드) nếu serialization thư viện (library / 라이브러리) không preserve chúng. Đây là dạng thất bại (failure mode / 실패 모드) tinh vi: proxy “không thay đổi gì” về lô-gic (logic / 논리) nhưng làm hỏng forward tính tương thích (compatibility / 호환성).

Default giá trị (value / 값) cũng nguy hiểm. Missing trường dữ liệu (field / 필드) có thể có nghĩa “writer cũ không biết trường dữ liệu (field / 필드) này”, khác với writer mới chủ động gửi `false` hoặc `0`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **15. Unknown fields, defaults và dữ liệu bị mất** nêu điều cần giải thích; **16. tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **17. Failure-safe rollout** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)

Thay vì hỏi “API có backward compatible không?”, hãy lập ma trận (matrix / 행렬):

```text
writer old -> reader old
writer old -> reader new
writer new -> reader old
writer new -> reader new
historical replay -> reader current
```

Sau đó kiểm tra structural parsing, ngữ nghĩa (semantic / 의미적) interpretation và side tác động (effect / 효과) của từng ô.

> **Chuyển mạch:** Trong **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **17. Failure-safe rollout** tiếp nhận điểm tựa từ **16. tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Failure-safe rollout

Một rollout tốt cần khả năng dừng và quay lui (rollback / 롤백). Nhưng quay lui (rollback / 롤백) nhị phân (binary / 이진) không luôn quay lui (rollback / 롤백) dữ liệu (data / 데이터). Nếu phiên bản (version / 버전) mới đã ghi biểu diễn (representation / 표현) mà phiên bản (version / 버전) cũ không hiểu, quay ứng dụng (application / 애플리케이션) về phiên bản (version / 버전) cũ có thể thất bại.

Do đó di chuyển (migration / 마이그레이션) cần **quay lui (rollback / 롤백) tính tương thích (compatibility / 호환성)** trong khoảng quan trọng, hoặc forward-fix chiến lược (strategy / 전략) rõ ràng.

> **Chuyển mạch:** Ở chặng này của **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **17. Failure-safe rollout** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Thêm trường dữ liệu (field / 필드) luôn backward compatible.”** Chỉ đúng nếu parser và ngữ nghĩa (semantics / 의미론) của bên tiêu thụ (consumer / 소비자) cho phép.

**“lược đồ (schema / 스키마) registry đảm bảo hệ thống tương thích.”** Registry thường kiểm structural rules, không hiểu nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론).

**“cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) chạy một lần nên hiệu năng (performance / 성능) không quan trọng.”** di chuyển (migration / 마이그레이션) có thể là tải công việc (workload / 워크로드) lớn nhất hệ thống trong thời gian chạy.

**“quay lui (rollback / 롤백) ứng dụng (application / 애플리케이션) là đủ.”** dữ liệu (data / 데이터) được ghi bởi phiên bản (version / 버전) mới có thể làm phiên bản (version / 버전) cũ không chạy được.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến hóa lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và hợp đồng tương thích**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> lược đồ (schema / 스키마) evolution là một **phân tán (distributed / 분산) giao thức (protocol / 프로토콜) theo thời gian** giữa các writer và reader không đổi phiên bản (version / 버전) đồng thời.

Thiết kế thay đổi (change / 변경) bằng cách xác định ai đang đọc/ghi biểu diễn (representation / 표현) nào, overlap cửa sổ (window / 윈도우) dài bao lâu, historical dữ liệu (data / 데이터) có replay không, quay lui (rollback / 롤백) cần hiểu dữ liệu mới đến mức nào và di chuyển (migration / 마이그레이션) tiêu thụ tài nguyên gì.

Xem thêm: [Event streams](./04_event_streams_partitions_watermarks_replay_and_state.md), [Capacity planning](./01_capacity_planning_utilization_knee_and_admission_control.md), [Idempotency](./05_idempotency_and_deduplication_at_scale.md).

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
