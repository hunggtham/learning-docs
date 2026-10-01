# API/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) và evolutionary thiết kế (design / 설계)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **API/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) và evolutionary thiết kế (design / 설계)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tính tương thích (compatibility / 호환성) có hướng** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Additive thay đổi (change / 변경) thường an toàn hơn destructive thay đổi (change / 변경)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Một API môi trường vận hành (production / 운영 환경) hiếm khi có thời điểm tất cả producers và consumers upgrade cùng lúc. Trong rolling triển khai (deployment / 배포), mobile app, bên ngoài (external / 외부) tích hợp (integration / 통합) hoặc sự kiện (event / 이벤트) stream, nhiều versions phải cùng tồn tại. Vì vậy tính tương thích (compatibility / 호환성) không phải polish; nó là điều kiện để hệ thống **evolve without coordinated stop-the-world upgrade**.

## Tính tương thích (compatibility / 호환성) có hướng

**Backward tính tương thích (compatibility / 호환성)** thường nghĩa bên tiêu thụ (consumer / 소비자) mới vẫn hiểu dữ liệu (data / 데이터)/yêu cầu (request / 요청) cũ hoặc API mới không phá máy khách (client / 클라이언트) cũ, tùy ngữ cảnh (context / 맥락). **Forward tính tương thích (compatibility / 호환성)** nói thành phần cũ có thể chịu được dữ liệu (data / 데이터) từ phiên bản (version / 버전) mới ở mức thiết kế cho phép.

Vì thuật ngữ dễ gây nhầm, kỹ thuật (engineering / 엔지니어링) document nên viết rõ producer phiên bản (version / 버전) nào nói chuyện với bên tiêu thụ (consumer / 소비자) phiên bản (version / 버전) nào thay vì chỉ ghi “backward compatible”.

> **Chuyển mạch:** Trong **API/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) và evolutionary thiết kế (design / 설계)**, **Additive thay đổi (change / 변경) thường an toàn hơn destructive thay đổi (change / 변경)** tiếp nhận điểm tựa từ **Tính tương thích (compatibility / 호환성) có hướng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tolerant reader có giới hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Additive thay đổi (change / 변경) thường an toàn hơn destructive thay đổi (change / 변경)

Thêm optional trường dữ liệu (field / 필드) thường dễ tương thích hơn rename/remove trường dữ liệu (field / 필드). Nhưng “optional” phải có ngữ nghĩa (semantic / 의미적) default rõ. Nếu bên tiêu thụ (consumer / 소비자) cũ bỏ qua trường dữ liệu (field / 필드) mới nhưng trường dữ liệu (field / 필드) đó thay đổi meaning của yêu cầu (request / 요청), wire format vẫn parse được nhưng nghiệp vụ (business / 비즈니스) tính tương thích (compatibility / 호환성) đã hỏng.

Tính tương thích (compatibility / 호환성) có ít nhất ba tầng: **syntactic**, **ngữ nghĩa (semantic / 의미적)**, **operational**.

> **Chuyển mạch:** Ở chặng này của **API/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) và evolutionary thiết kế (design / 설계)**, **Additive thay đổi (change / 변경) thường an toàn hơn destructive thay đổi (change / 변경)** đã nêu tiêu chí phân biệt, còn **Tolerant reader có giới hạn** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Enum là một tính tương thích (compatibility / 호환성) trap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tolerant reader có giới hạn

Bên tiêu thụ (consumer / 소비자) nên bỏ qua unknown fields khi giao thức (protocol / 프로토콜) cho phép để producer có thể mở rộng. Nhưng quá tolerant với malformed/ambiguous dữ liệu (data / 데이터) có thể che bug hoặc bảo mật (security / 보안) issue.

Robustness không có nghĩa accept mọi thứ; đặc tả hợp đồng (contract / 계약) phải xác định extension points nào được phép và bất biến (invariant / 불변식) nào phải reject.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **API/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) và evolutionary thiết kế (design / 설계)**, **Tolerant reader có giới hạn** đã nêu tiêu chí phân biệt, còn **Enum là một tính tương thích (compatibility / 호환성) trap** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) evolution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Enum là một tính tương thích (compatibility / 호환성) trap

Producer thêm enum giá trị (value / 값) mới có thể làm bên tiêu thụ (consumer / 소비자) cũ crash nếu mã (code / 코드) giả định exhaustive set cố định. Với công khai (public / 공개)/sự kiện (event / 이벤트) contracts, bên tiêu thụ (consumer / 소비자) cần chiến lược (strategy / 전략) cho unknown giá trị (value / 값): map `UNKNOWN`, preserve raw giá trị (value / 값) hoặc thất bại (fail / 실패) theo chính sách (policy / 정책) có chủ đích.

Trình biên dịch (compiler / 컴파일러) exhaustiveness rất hữu ích trong mã (code / 코드) nội bộ nhưng ranh giới (boundary / 경계) evolving cần thiết kế riêng.

> **Chuyển mạch:** Trong **API/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) và evolutionary thiết kế (design / 설계)**, **Enum là một tính tương thích (compatibility / 호환성) trap** nêu điều cần giải thích; **Cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) evolution** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Sự kiện (event / 이벤트) lược đồ (schema / 스키마) khó hơn yêu cầu (request / 요청)/phản hồi (response / 응답)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) evolution

Rename column trực tiếp có thể phá old ứng dụng (application / 애플리케이션) instances trong rolling deploy. mẫu (pattern / 패턴) an toàn hơn thường là **expand → migrate → đặc tả hợp đồng (contract / 계약)**: thêm biểu diễn (representation / 표현) mới tương thích, deploy mã (code / 코드) có thể đọc/ghi theo chuyển tiếp (transition / 전이), backfill dữ liệu (data / 데이터), chuyển traffic, rồi chỉ xóa trường dữ liệu (field / 필드) cũ khi không còn bên tiêu thụ (consumer / 소비자).

Mỗi bước phải quay lui (rollback / 롤백) được trong phạm vi hợp lý. di chuyển (migration / 마이그레이션) lược đồ (schema / 스키마) và ứng dụng (application / 애플리케이션) triển khai (deployment / 배포) là một giao thức (protocol / 프로토콜) nhiều phiên bản (version / 버전).

> **Chuyển mạch:** Ở chặng này của **API/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) và evolutionary thiết kế (design / 설계)**, **Cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) evolution** nêu điều cần giải thích; **Sự kiện (event / 이벤트) lược đồ (schema / 스키마) khó hơn yêu cầu (request / 요청)/phản hồi (response / 응답)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Consumer-driven đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự kiện (event / 이벤트) lược đồ (schema / 스키마) khó hơn yêu cầu (request / 요청)/phản hồi (response / 응답)

Sự kiện (event / 이벤트) có thể được lưu và replay nhiều tháng sau. bên tiêu thụ (consumer / 소비자) mới có thể đọc sự kiện (event / 이벤트) rất cũ; bên tiêu thụ (consumer / 소비자) cũ có thể vẫn chạy khi producer mới publish. lược đồ (schema / 스키마) registry/versioning giúp quản lý cấu trúc (structure / 구조) nhưng không tự đảm bảo ngữ nghĩa (semantic / 의미적) tính tương thích (compatibility / 호환성).

Nếu trường dữ liệu (field / 필드) `amount` đổi từ gross sang net mà vẫn cùng tên/kiểu (type / 타입), lược đồ (schema / 스키마) checker có thể không phát hiện breaking ngữ nghĩa (semantic / 의미적) thay đổi (change / 변경).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **API/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) và evolutionary thiết kế (design / 설계)**, **Consumer-driven đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **Sự kiện (event / 이벤트) lược đồ (schema / 스키마) khó hơn yêu cầu (request / 요청)/phản hồi (response / 응답)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Versioning endpoint không giải quyết mọi thứ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Consumer-driven đặc tả hợp đồng (contract / 계약)

Provider không phải lúc nào biết bên tiêu thụ (consumer / 소비자) phụ thuộc vào hành vi (behavior / 동작) nào. đặc tả hợp đồng (contract / 계약) testing có thể capture expectations quan trọng từ consumers và chạy chúng trước khi provider bản phát hành (release / 릴리스).

Tuy nhiên kiểm thử (test / 테스트) không thay thế phiên bản (version / 버전) chính sách (policy / 정책). Nếu hàng trăm bên tiêu thụ (consumer / 소비자) contracts encode accidental hành vi (behavior / 동작), provider có thể bị đóng băng. đặc tả hợp đồng (contract / 계약) cần tập trung vào supported hành vi (behavior / 동작).

> **Chuyển mạch:** Trong **API/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) và evolutionary thiết kế (design / 설계)**, **Versioning endpoint không giải quyết mọi thứ** tiếp nhận điểm tựa từ **Consumer-driven đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deprecation là vòng đời (lifecycle / 생명주기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Versioning endpoint không giải quyết mọi thứ

`/v1` và `/v2` cho phép breaking thay đổi (change / 변경) rõ ràng nhưng tạo chi phí (cost / 비용) duy trì hai các hệ thống (systems / 시스템들). Nếu mọi thay đổi nhỏ đều tạo phiên bản (version / 버전) mới, di chuyển (migration / 마이그레이션) debt tăng nhanh. Additive evolution trong cùng major phiên bản (version / 버전) thường rẻ hơn; major phiên bản (version / 버전) dành cho ngữ nghĩa (semantic / 의미적) break thực sự.

> **Chuyển mạch:** Ở chặng này của **API/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) và evolutionary thiết kế (design / 설계)**, **Versioning endpoint không giải quyết mọi thứ** xác định đầu vào; **Deprecation là vòng đời (lifecycle / 생명주기)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deprecation là vòng đời (lifecycle / 생명주기)

Một trường dữ liệu (field / 필드)/API không biến mất chỉ vì documentation ghi deprecated. Cần telemetry biết bên tiêu thụ (consumer / 소비자) nào còn dùng, communication, deadline, di chuyển (migration / 마이그레이션) đường dẫn (path / 경로) và enforcement. Unknown consumers là lý do khả năng quan sát (observability / 관측 가능성) tại ranh giới (boundary / 경계) rất quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **API/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) và evolutionary thiết kế (design / 설계)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Deprecation là vòng đời (lifecycle / 생명주기)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> API evolution là phân tán (distributed / 분산) di chuyển (migration / 마이그레이션) qua thời gian. Một thay đổi (change / 변경) an toàn phải xét old/new producer × old/new bên tiêu thụ (consumer / 소비자), không chỉ compile phiên bản (version / 버전) hiện tại. Expand trước, migrate usage, quan sát, rồi đặc tả hợp đồng (contract / 계약). tính tương thích (compatibility / 호환성) tốt giảm nhu cầu coordinated bản phát hành (release / 릴리스) và làm kiến trúc (architecture / 아키텍처) có khả năng thay đổi lâu dài.

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
