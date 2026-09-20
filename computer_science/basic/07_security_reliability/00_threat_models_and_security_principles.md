# Mô hình đe dọa và các nguyên tắc bảo mật

Bảo mật (security / 보안) không bắt đầu từ mã hóa. Nó bắt đầu bằng câu hỏi: **ta đang bảo vệ tài sản nào, khỏi tác nhân nào, qua bề mặt tấn công nào và thuộc tính nào phải được giữ vững?** Nếu không có **mô hình đe dọa (threat model)**, từ “an toàn” quá mơ hồ để kiểm chứng.

## Các thuộc tính bảo mật

Bộ ba CIA là mô hình tư duy cổ điển. **Tính bí mật (Confidentiality)** ngăn người không có quyền đọc dữ liệu; **tính toàn vẹn (Integrity)** ngăn hoặc giúp phát hiện sửa đổi trái phép; **tính sẵn sàng (Availability)** giữ dịch vụ và tài nguyên có thể sử dụng khi cần.

Ngoài ra còn có tính xác thực, khả năng quy trách nhiệm và kiểm toán, chống chối bỏ trong ngữ cảnh phù hợp, quyền riêng tư và an toàn vận hành. Một hệ thống giữ bí mật rất tốt nhưng thường xuyên không phục vụ được người dùng vẫn không đáp ứng đầy đủ mục tiêu bảo mật.

## Mô hình đe dọa

Mô hình đe dọa xác định tài sản cần bảo vệ, ranh giới tin cậy, tác nhân và năng lực của họ, điểm đi vào hệ thống và các tình huống lạm dụng. Kẻ tấn công từ Internet khác người nội bộ ác ý; một tiến trình ứng dụng đã bị chiếm quyền khác kẻ có quyền truy cập vật lý; bot cơ hội khác đối thủ có nguồn lực lớn.

Một biện pháp kiểm soát chỉ có ý nghĩa khi đặt trong mối quan hệ với mối đe dọa. Mã hóa ổ đĩa bảo vệ laptop bị đánh cắp khi đang tắt, nhưng không ngăn phần mềm độc hại đọc dữ liệu đã giải mã khi người dùng đang đăng nhập.

## Ranh giới tin cậy

**Ranh giới tin cậy (trust boundary)** là nơi dữ liệu hoặc quyền điều khiển đi từ một ngữ cảnh có giả định tin cậy này sang ngữ cảnh khác: trình duyệt → máy chủ, dữ liệu người dùng → SQL, ứng dụng → kernel, dịch vụ A → dịch vụ B, tenant → nền tảng dùng chung.

Mỗi ranh giới cần kiểm tra dữ liệu, xác thực và phân quyền theo mức rủi ro. Không nên mặc định “mạng nội bộ” là hoàn toàn đáng tin vì một dịch vụ nội bộ bị xâm nhập có thể trở thành bàn đạp sang thành phần khác.

## Nguyên tắc đặc quyền tối thiểu

**Đặc quyền tối thiểu (principle of least privilege)** yêu cầu mỗi danh tính hoặc tiến trình chỉ có quyền cần thiết, trong phạm vi và khoảng thời gian cần thiết. Tài khoản ứng dụng của cơ sở dữ liệu không nên có quyền `DROP` toàn bộ schema nếu chỉ cần CRUD trên vài bảng; container không nên chạy đặc quyền cao nếu không cần; token API chỉ đọc không nên có quyền quản trị.

Giảm quyền giúp thu hẹp phạm vi thiệt hại (blast radius) nhưng làm quản lý phức tạp hơn. Thiết kế tốt dùng vai trò, phạm vi và capability để quyền vừa đủ mà không biến hệ thống thành mê cung permission.

## Phòng thủ nhiều lớp

Không biện pháp nào hoàn hảo. TLS, xác thực, phân quyền, kiểm tra đầu vào, sandbox, giám sát và sao lưu bảo vệ các kiểu lỗi khác nhau. Các lớp nên có mức độc lập tương đối; ba biện pháp cùng phụ thuộc một secret duy nhất không tạo ra ba lớp bảo vệ thật sự độc lập.

## Mặc định an toàn

Cấu hình mặc định nên từ chối hoặc cấp quyền tối thiểu và yêu cầu bật tường minh cho quyền nguy hiểm. Đường xử lý lỗi không nên biến thành “dịch vụ xác thực timeout thì cho phép truy cập”. Một số hệ thống ưu tiên tính sẵn sàng có thể cố ý mở khi lỗi (fail-open), nhưng đó phải là quyết định đánh đổi rủi ro có chủ đích.

## Giảm bề mặt tấn công

Mỗi endpoint, bộ phân tích dữ liệu, dependency, cổng mở, đặc quyền và tính năng đều có thể trở thành **bề mặt tấn công (attack surface)**. Loại bỏ dịch vụ không dùng, giảm API công khai, cập nhật dependency và giới hạn đầu vào giúp giảm số trạng thái mà hệ thống phải bảo vệ.

Sự đơn giản có giá trị bảo mật vì càng ít trạng thái và tương tác thì càng dễ suy luận về hành vi.

## Kiểm tra quyền ở mọi đường truy cập

Nguyên tắc **kiểm tra đầy đủ (complete mediation)** yêu cầu phân quyền ở mọi lần truy cập tài nguyên được bảo vệ, không chỉ trên giao diện. Ẩn một nút không bảo vệ API phía máy chủ. Cache cũng phải giữ đúng ngữ nghĩa phân quyền; khóa cache thiếu thông tin tenant hoặc người dùng có thể làm rò rỉ dữ liệu giữa các đối tượng.

## Phân tách nhiệm vụ

Một hành động quan trọng có thể yêu cầu nhiều vai trò hoặc phê duyệt độc lập để giảm nguy cơ lạm dụng hoặc một tài khoản duy nhất bị chiếm quyền. Phê duyệt triển khai, quản lý khóa và quy trình tài chính thường dùng nguyên tắc này.

## Bảo mật, khả dụng và hiệu năng

Biện pháp bảo mật luôn có chi phí. MFA thêm thao tác; hàm dẫn xuất khóa mạnh tốn CPU; mã hóa thêm chi phí xử lý; thời hạn phiên quá ngắn làm người dùng phải xác thực lại nhiều hơn. Kỹ thuật tốt cần định lượng mối đe dọa và chi phí thay vì bỏ bảo mật hoặc tăng ma sát một cách cực đoan.

## Mô hình tư duy

> Bảo mật là **quản lý niềm tin trong môi trường có hành vi đối kháng**. Hãy bắt đầu từ tài sản → mối đe dọa → ranh giới → bất biến cần giữ → biện pháp kiểm soát → rủi ro còn lại, thay vì bắt đầu từ danh sách công nghệ.

## Những hiểu nhầm thường gặp

**“Dùng HTTPS là đủ an toàn.”** Không đúng. TLS bảo vệ kênh truyền nhưng không sửa lỗi phân quyền, injection hoặc endpoint đã bị xâm nhập.

**“Ở mạng nội bộ thì có thể tin cậy.”** Không đúng. Vị trí mạng chỉ là một tín hiệu; danh tính và phân quyền vẫn cần thiết.

**“Bảo mật là tính năng thêm vào cuối dự án.”** Không đúng. Mô hình dữ liệu, ranh giới đặc quyền và thiết kế giao thức quyết định nhiều thuộc tính bảo mật ngay từ đầu.

## Kết nối

Cô lập của hệ điều hành nằm ở [đặc quyền và ảo hóa](../03_operating_systems/05_privilege_isolation_and_virtualization.md). Cơ chế mật mã nằm ở [nền tảng mật mã học](./01_cryptography_foundations.md); danh tính và quyền truy cập ở [xác thực và phân quyền](./02_identity_authentication_and_authorization.md); lỗi triển khai ở [lỗ hổng phần mềm](./03_software_vulnerabilities.md).
