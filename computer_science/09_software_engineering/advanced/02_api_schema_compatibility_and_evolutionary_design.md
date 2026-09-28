# API/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) và evolutionary thiết kế (design / 설계)

> **Mạch đọc:** Đặt **API/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) và evolutionary thiết kế (design / 설계)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **tính tương thích (compatibility / 호환성) có hướng** sang **Additive thay đổi (change / 변경) thường an toàn hơn destructive thay đổi (change / 변경)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Một API môi trường vận hành (production / 운영 환경) hiếm khi có thời điểm tất cả producers và consumers upgrade cùng lúc. Trong rolling triển khai (deployment / 배포), mobile app, bên ngoài (external / 외부) tích hợp (integration / 통합) hoặc sự kiện (event / 이벤트) stream, nhiều versions phải cùng tồn tại. Vì vậy tính tương thích (compatibility / 호환성) không phải polish; nó là điều kiện để hệ thống **evolve without coordinated stop-the-world upgrade**.

## Tính tương thích (compatibility / 호환성) có hướng

**Backward tính tương thích (compatibility / 호환성)** thường nghĩa bên tiêu thụ (consumer / 소비자) mới vẫn hiểu dữ liệu (data / 데이터)/yêu cầu (request / 요청) cũ hoặc API mới không phá máy khách (client / 클라이언트) cũ, tùy ngữ cảnh (context / 맥락). **Forward tính tương thích (compatibility / 호환성)** nói thành phần cũ có thể chịu được dữ liệu (data / 데이터) từ phiên bản (version / 버전) mới ở mức thiết kế cho phép.

Vì thuật ngữ dễ gây nhầm, kỹ thuật (engineering / 엔지니어링) document nên viết rõ producer phiên bản (version / 버전) nào nói chuyện với bên tiêu thụ (consumer / 소비자) phiên bản (version / 버전) nào thay vì chỉ ghi “backward compatible”.


> **Chuyển mạch:** Từ **tính tương thích (compatibility / 호환성) có hướng**, ta sang **Additive thay đổi (change / 변경) thường an toàn hơn destructive thay đổi (change / 변경)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Additive thay đổi (change / 변경) thường an toàn hơn destructive thay đổi (change / 변경)

Thêm optional trường dữ liệu (field / 필드) thường dễ tương thích hơn rename/remove trường dữ liệu (field / 필드). Nhưng “optional” phải có ngữ nghĩa (semantic / 의미적) default rõ. Nếu bên tiêu thụ (consumer / 소비자) cũ bỏ qua trường dữ liệu (field / 필드) mới nhưng trường dữ liệu (field / 필드) đó thay đổi meaning của yêu cầu (request / 요청), wire format vẫn parse được nhưng nghiệp vụ (business / 비즈니스) tính tương thích (compatibility / 호환성) đã hỏng.

Tính tương thích (compatibility / 호환성) có ít nhất ba tầng: **syntactic**, **ngữ nghĩa (semantic / 의미적)**, **operational**.


> **Chuyển mạch:** Từ **Additive thay đổi (change / 변경) thường an toàn hơn destructive thay đổi (change / 변경)**, ta sang **Tolerant reader có giới hạn** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tolerant reader có giới hạn

Bên tiêu thụ (consumer / 소비자) nên bỏ qua unknown fields khi giao thức (protocol / 프로토콜) cho phép để producer có thể mở rộng. Nhưng quá tolerant với malformed/ambiguous dữ liệu (data / 데이터) có thể che bug hoặc bảo mật (security / 보안) issue.

Robustness không có nghĩa accept mọi thứ; đặc tả hợp đồng (contract / 계약) phải xác định extension points nào được phép và bất biến (invariant / 불변식) nào phải reject.


> **Chuyển mạch:** Từ **Tolerant reader có giới hạn**, ta sang **Enum là một tính tương thích (compatibility / 호환성) trap** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Enum là một tính tương thích (compatibility / 호환성) trap

Producer thêm enum giá trị (value / 값) mới có thể làm bên tiêu thụ (consumer / 소비자) cũ crash nếu mã (code / 코드) giả định exhaustive set cố định. Với công khai (public / 공개)/sự kiện (event / 이벤트) contracts, bên tiêu thụ (consumer / 소비자) cần chiến lược (strategy / 전략) cho unknown giá trị (value / 값): map `UNKNOWN`, preserve raw giá trị (value / 값) hoặc thất bại (fail / 실패) theo chính sách (policy / 정책) có chủ đích.

Trình biên dịch (compiler / 컴파일러) exhaustiveness rất hữu ích trong mã (code / 코드) nội bộ nhưng ranh giới (boundary / 경계) evolving cần thiết kế riêng.


> **Chuyển mạch:** Từ **Enum là một tính tương thích (compatibility / 호환성) trap**, ta sang **cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) evolution** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) evolution

Rename column trực tiếp có thể phá old ứng dụng (application / 애플리케이션) instances trong rolling deploy. mẫu (pattern / 패턴) an toàn hơn thường là **expand → migrate → đặc tả hợp đồng (contract / 계약)**: thêm biểu diễn (representation / 표현) mới tương thích, deploy mã (code / 코드) có thể đọc/ghi theo chuyển tiếp (transition / 전이), backfill dữ liệu (data / 데이터), chuyển traffic, rồi chỉ xóa trường dữ liệu (field / 필드) cũ khi không còn bên tiêu thụ (consumer / 소비자).

Mỗi bước phải quay lui (rollback / 롤백) được trong phạm vi hợp lý. di chuyển (migration / 마이그레이션) lược đồ (schema / 스키마) và ứng dụng (application / 애플리케이션) triển khai (deployment / 배포) là một giao thức (protocol / 프로토콜) nhiều phiên bản (version / 버전).


> **Chuyển mạch:** Từ **cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) evolution**, ta sang **sự kiện (event / 이벤트) lược đồ (schema / 스키마) khó hơn yêu cầu (request / 요청)/phản hồi (response / 응답)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Sự kiện (event / 이벤트) lược đồ (schema / 스키마) khó hơn yêu cầu (request / 요청)/phản hồi (response / 응답)

Sự kiện (event / 이벤트) có thể được lưu và replay nhiều tháng sau. bên tiêu thụ (consumer / 소비자) mới có thể đọc sự kiện (event / 이벤트) rất cũ; bên tiêu thụ (consumer / 소비자) cũ có thể vẫn chạy khi producer mới publish. lược đồ (schema / 스키마) registry/versioning giúp quản lý cấu trúc (structure / 구조) nhưng không tự đảm bảo ngữ nghĩa (semantic / 의미적) tính tương thích (compatibility / 호환성).

Nếu trường dữ liệu (field / 필드) `amount` đổi từ gross sang net mà vẫn cùng tên/kiểu (type / 타입), lược đồ (schema / 스키마) checker có thể không phát hiện breaking ngữ nghĩa (semantic / 의미적) thay đổi (change / 변경).


> **Chuyển mạch:** Từ **sự kiện (event / 이벤트) lược đồ (schema / 스키마) khó hơn yêu cầu (request / 요청)/phản hồi (response / 응답)**, ta sang **Consumer-driven đặc tả hợp đồng (contract / 계약)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Consumer-driven đặc tả hợp đồng (contract / 계약)

Provider không phải lúc nào biết bên tiêu thụ (consumer / 소비자) phụ thuộc vào hành vi (behavior / 동작) nào. đặc tả hợp đồng (contract / 계약) testing có thể capture expectations quan trọng từ consumers và chạy chúng trước khi provider bản phát hành (release / 릴리스).

Tuy nhiên kiểm thử (test / 테스트) không thay thế phiên bản (version / 버전) chính sách (policy / 정책). Nếu hàng trăm bên tiêu thụ (consumer / 소비자) contracts encode accidental hành vi (behavior / 동작), provider có thể bị đóng băng. đặc tả hợp đồng (contract / 계약) cần tập trung vào supported hành vi (behavior / 동작).


> **Chuyển mạch:** Từ **Consumer-driven đặc tả hợp đồng (contract / 계약)**, ta sang **Versioning endpoint không giải quyết mọi thứ** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Versioning endpoint không giải quyết mọi thứ

`/v1` và `/v2` cho phép breaking thay đổi (change / 변경) rõ ràng nhưng tạo chi phí (cost / 비용) duy trì hai các hệ thống (systems / 시스템들). Nếu mọi thay đổi nhỏ đều tạo phiên bản (version / 버전) mới, di chuyển (migration / 마이그레이션) debt tăng nhanh. Additive evolution trong cùng major phiên bản (version / 버전) thường rẻ hơn; major phiên bản (version / 버전) dành cho ngữ nghĩa (semantic / 의미적) break thực sự.


> **Chuyển mạch:** Từ **Versioning endpoint không giải quyết mọi thứ**, ta sang **Deprecation là vòng đời (lifecycle / 생명주기)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Deprecation là vòng đời (lifecycle / 생명주기)

Một trường dữ liệu (field / 필드)/API không biến mất chỉ vì documentation ghi deprecated. Cần telemetry biết bên tiêu thụ (consumer / 소비자) nào còn dùng, communication, deadline, di chuyển (migration / 마이그레이션) đường dẫn (path / 경로) và enforcement. Unknown consumers là lý do khả năng quan sát (observability / 관측 가능성) tại ranh giới (boundary / 경계) rất quan trọng.


> **Chuyển mạch:** Từ **Deprecation là vòng đời (lifecycle / 생명주기)**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> API evolution là phân tán (distributed / 분산) di chuyển (migration / 마이그레이션) qua thời gian. Một thay đổi (change / 변경) an toàn phải xét old/new producer × old/new bên tiêu thụ (consumer / 소비자), không chỉ compile phiên bản (version / 버전) hiện tại. Expand trước, migrate usage, quan sát, rồi đặc tả hợp đồng (contract / 계약). tính tương thích (compatibility / 호환성) tốt giảm nhu cầu coordinated bản phát hành (release / 릴리스) và làm kiến trúc (architecture / 아키텍처) có khả năng thay đổi lâu dài.

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 architecture decisions evolution and socio technical constraints](./00_architecture_decisions_evolution_and_socio_technical_constraints.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
