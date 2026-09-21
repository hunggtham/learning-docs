# Đạo đức máy tính, quyền riêng tư và trách nhiệm nghề nghiệp

Phần mềm thay đổi điều con người có thể biết, có thể làm và có thể kiểm soát. Vì vậy kỹ sư không chỉ chịu trách nhiệm “viết mã đúng đặc tả”; còn phải xem ai bị ảnh hưởng, loại thiệt hại nào có thể xảy ra và dữ liệu hoặc quyền đồng thuận nào đang được sử dụng. Đạo đức (ethics) không thay thế pháp luật, nhưng pháp luật cũng không bao phủ mọi quyết định có trách nhiệm.

## Quyết định kỹ thuật luôn chứa giả định về giá trị

Chọn mặc định công khai hay riêng tư, giữ dữ liệu 30 ngày hay vô thời hạn, thông báo theo cơ chế tự chọn tham gia hay mặc định tham gia đều định hướng hành vi và phân phối rủi ro khác nhau.

Một thiết kế có vẻ trung lập về kỹ thuật vẫn có thể chứa các động cơ và giả định ảnh hưởng trực tiếp tới người dùng.

## Quyền riêng tư không chỉ là giữ bí mật

**Quyền riêng tư (privacy)** liên quan tới quyền kiểm soát và ngữ cảnh của thông tin cá nhân: thu thập dữ liệu nào, cho mục đích gì, ai được truy cập, giữ bao lâu và kết hợp với nguồn nào.

Một thông tin riêng lẻ có thể không bí mật, nhưng khi tổng hợp nhiều nguồn hoặc tái định danh, hệ thống có thể tạo ra rủi ro mới mà từng mẩu dữ liệu riêng không có.

## Tối thiểu hóa dữ liệu

**Tối thiểu hóa dữ liệu (data minimization)** nghĩa là chỉ thu thập lượng dữ liệu thực sự cần thiết. Điều này giảm thiệt hại khi xảy ra rò rỉ và giảm gánh nặng quản trị. Lý do “có thể hữu ích trong tương lai” không tự động biện minh cho việc thu thập vô thời hạn.

Tối thiểu hóa cũng là nguyên tắc bảo mật: dữ liệu không tồn tại trong hệ thống thì không thể bị rò rỉ từ chính hệ thống đó.

## Đồng thuận

**Đồng thuận (consent)** có ý nghĩa khi người dùng được cung cấp đủ thông tin, lựa chọn đủ cụ thể và có mức tự nguyện hợp lý. Mẫu thiết kế thao túng hoặc tình huống “chấp nhận tất cả hoặc không được dùng dịch vụ” có thể biến consent thành thủ tục hơn là lựa chọn thật sự.

Kỹ thuật phải bảo đảm lựa chọn của người dùng được thực thi trong luồng dữ liệu thật, không chỉ tồn tại dưới dạng một ô chọn trên giao diện.

## Giới hạn mục đích

Dữ liệu được thu để chống gian lận không tự động phù hợp cho quảng cáo không liên quan. Tái sử dụng cho mục đích khác làm thay đổi rủi ro và ngữ cảnh, và có thể cần cơ sở hoặc sự đồng thuận mới tùy chính sách và pháp luật.

Theo dõi nguồn gốc dữ liệu (data lineage) giúp biết hệ thống phía sau đang sử dụng tập dữ liệu nào cho mục đích nào.

## Trách nhiệm nghề nghiệp

Kỹ sư có trách nhiệm báo cáo rủi ro nghiêm trọng, không làm sai lệch kết quả kiểm thử và không che giấu lỗi an toàn hoặc bảo mật đã biết.

Trong hệ thống có mức ảnh hưởng cao, áp lực tiến độ không xóa nghĩa vụ nâng cấp cảnh báo khi có bằng chứng về rủi ro. Bộ quy tắc đạo đức của các tổ chức nghề nghiệp cung cấp khung tham khảo nhưng không tự động giải mọi xung đột.

## Công nghệ có thể được dùng cho nhiều mục đích

Mã hóa, nhận diện khuôn mặt, nghiên cứu lỗ hổng và AI tạo sinh đều có thể đem lại lợi ích đồng thời bị lạm dụng. Phân tích có trách nhiệm cần xem các cách lạm dụng có khả năng xảy ra, cơ chế kiểm soát truy cập, giám sát và chiến lược công bố.

Không thể ngăn mọi hành vi lạm dụng, nhưng quan điểm “công cụ trung lập nên không cần suy nghĩ về hậu quả” là không đủ.

## Báo cáo và nâng cấp cảnh báo

Khi nguy cơ hoặc vi phạm nghiêm trọng bị bỏ qua, có thể cần dùng các kênh nội bộ, đạo đức, tuân thủ hoặc pháp lý. Việc tố giác ra bên ngoài phụ thuộc pháp luật, bằng chứng và rủi ro cụ thể; đây không phải vấn đề chỉ có thể giải bằng kỹ thuật.

Một điểm quan trọng với kỹ sư là quy trình tổ chức cũng là cơ chế an toàn, tương tự code review nhưng áp dụng cho rủi ro xã hội và nghề nghiệp.

## Những hiểu nhầm thường gặp

**“Nếu hợp pháp thì chắc chắn có đạo đức.”** Không đúng. Pháp luật đặt ra giới hạn và nghĩa vụ tối thiểu nhưng có thể đi sau công nghệ hoặc vẫn cho phép những lựa chọn gây hại.

**“Quyền riêng tư chỉ là mã hóa cơ sở dữ liệu.”** Không đúng. Mã hóa chỉ là một biện pháp; việc thu thập, truy cập, lưu giữ và mục đích sử dụng vẫn quyết định rủi ro.

**“Kỹ sư không quyết định sản phẩm nên không có trách nhiệm.”** Không đúng. Kỹ sư thường hiểu chi tiết triển khai và rủi ro mà người khác không thấy, nên có vai trò truyền đạt hệ quả và cảnh báo.

## Mô hình tư duy

> Điện toán có trách nhiệm không chỉ hỏi “hệ thống có hoạt động không?” mà còn hỏi “hệ thống hoạt động cho ai, sử dụng dữ liệu và quyền lực nào, và ai phải chịu chi phí khi các giả định sai?”.

## Kết nối

Đọc [nguyên tắc bảo mật](../07_security_reliability/00_threat_models_and_security_principles.md), [HCI và mẫu thiết kế thao túng](../11_hci_graphics/01_interface_design_accessibility_and_usability.md), [đánh giá AI](../10_ai_foundations/04_ai_evaluation_data_and_responsibility.md) và [quản trị dữ liệu](./01_data_governance_bias_and_algorithmic_impact.md).