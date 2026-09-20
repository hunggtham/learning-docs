# Thiết kế giao diện, khả năng tiếp cận và tính dễ sử dụng

Tính dễ sử dụng (usability) không hoàn toàn là cảm giác chủ quan. Ta có thể quan sát tỷ lệ hoàn thành nhiệm vụ, tỷ lệ lỗi, thời gian thực hiện, khả năng học và mức hài lòng. **Khả năng tiếp cận (accessibility / 접근성)** mở rộng câu hỏi: giao diện có thể sử dụng được với người có khả năng giác quan, vận động, nhận thức và thiết bị khác nhau hay không?

## Tính dễ sử dụng phụ thuộc người dùng và nhiệm vụ

Một giao diện rất nhanh với người vận hành có kinh nghiệm có thể khó hiểu với người mới. Dòng lệnh (command line) hiệu quả cho tự động hóa lặp lại nhưng khó tự khám phá hơn giao diện đồ họa.

Vì vậy “dễ dùng” luôn cần ngữ cảnh: ai đang sử dụng, làm nhiệm vụ gì, tần suất bao nhiêu và chi phí của sai sót lớn đến mức nào.

## Kiến trúc thông tin

Điều hướng tốt phản ánh cách người dùng phân loại mục tiêu, không nhất thiết phản ánh cấu trúc bảng cơ sở dữ liệu hoặc sơ đồ phòng ban của tổ chức.

Các phương pháp như phân loại thẻ (card sorting), kiểm thử cây điều hướng và phân tích nhật ký tìm kiếm giúp kiểm tra xem mô hình phân nhóm của sản phẩm có khớp với cách người dùng suy nghĩ hay không.

## Thứ bậc thị giác

Kích thước, khoảng cách, vị trí, độ tương phản và cách nhóm hướng sự chú ý. Các nguyên lý Gestalt như gần nhau và tương đồng giúp người dùng nhận ra nhóm mà không cần vẽ khung quanh mọi thành phần.

**Thứ bậc thị giác (visual hierarchy)** không chỉ là thẩm mỹ; nó mã hóa mức ưu tiên và quan hệ giữa thông tin.

## Thiết kế biểu mẫu

Biểu mẫu cần nhãn rõ ràng, ràng buộc đầu vào dễ hiểu, thông báo lỗi gần trường liên quan và giữ dữ liệu người dùng đã nhập khi kiểm tra thất bại.

Kiểm tra sớm ở phía máy khách giúp phản hồi nhanh, nhưng kiểm tra phía máy chủ vẫn bắt buộc vì không thể tin cậy dữ liệu từ client. Thông báo lỗi tốt nói rõ điều gì sai và cách sửa, thay vì chỉ hiển thị “Invalid input”.

## Khả năng tiếp cận không phải phần thêm vào cuối dự án

HTML có ngữ nghĩa, điều hướng bằng bàn phím, thứ tự focus, văn bản thay thế, độ tương phản và khả năng phóng to chữ ảnh hưởng kiến trúc thành phần ngay từ đầu.

Trình đọc màn hình (screen reader) dựa vào cây accessibility và ngữ nghĩa, chứ không “nhìn pixel” như người có thị lực bình thường.

## Bàn phím và focus

Các điều khiển tương tác phải có thể tiếp cận bằng bàn phím khi nền tảng và trường hợp sử dụng yêu cầu. Chỉ báo focus cho biết phần tử đang nhận thao tác; hộp thoại modal phải quản lý việc đưa focus vào, giữ focus bên trong khi cần và trả focus về vị trí hợp lý sau khi đóng.

Một `div` tự chế để bấm thường thiếu ngữ nghĩa bàn phím và vai trò accessibility nếu lập trình viên không bổ sung đầy đủ hành vi tương ứng.

## Màu sắc

Không nên dùng màu làm kênh duy nhất để truyền trạng thái vì người dùng có khả năng nhận màu khác nhau, và hệ thống có thể chạy ở chế độ đơn sắc hoặc tương phản cao.

Trạng thái lỗi có thể kết hợp biểu tượng, văn bản và màu. Độ tương phản cần đáp ứng hướng dẫn accessibility tương ứng; ngưỡng cụ thể phụ thuộc tiêu chuẩn và ngữ cảnh.

## Thiết kế đáp ứng

**Thiết kế đáp ứng (responsive design)** không chỉ là thu nhỏ giao diện desktop. Màn hình cảm ứng nhỏ có kích thước vùng chạm, tầm với ngón tay, bàn phím ảo và điều kiện mạng khác.

Vì vậy bố cục và mức ưu tiên nội dung đôi khi phải thay đổi, chứ không chỉ co giãn bằng CSS.

## Kiểm thử với người dùng

Quan sát người dùng đại diện thực hiện các nhiệm vụ đại diện giúp phát hiện khoảng cách giữa mô hình của đội phát triển và cách người dùng thật sự hiểu sản phẩm.

“5 người dùng” không phải con số thần kỳ cho mọi nghiên cứu. Cỡ mẫu phụ thuộc mục tiêu, độ biến thiên và việc phương pháp là định tính hay cần suy luận thống kê.

## Thử nghiệm A/B

Thử nghiệm A/B có thể đo ảnh hưởng nhân quả của một biến thể giao diện nếu việc ngẫu nhiên hóa và chỉ số được thiết kế đúng. Tuy nhiên một chỉ số cục bộ tăng không có nghĩa kết quả dài hạn tốt hơn.

Ví dụ tăng số lần bấm thông báo không đồng nghĩa tăng lợi ích cho người dùng. Vì vậy chỉ số chính cần đi cùng các chỉ số bảo vệ (guardrail metric).

## Mẫu thiết kế thao túng

**Mẫu tối (dark pattern)** dùng sự bất cân xứng hoặc gây nhầm lẫn để hướng người dùng làm điều trái với lợi ích hoặc mong muốn của họ, chẳng hạn hủy đăng ký khó hơn đăng ký hoặc che phí bổ sung.

Đây là điểm giao giữa HCI và đạo đức: thiết kế có hiệu quả trong việc thúc đẩy hành vi không tự động đồng nghĩa với thiết kế có trách nhiệm.

## Những hiểu nhầm thường gặp

**“Accessibility chỉ dành cho một nhóm nhỏ.”** Không đúng. Chấn thương tạm thời, tuổi tác, ánh sáng mạnh, sử dụng một tay và mạng kém đều tạo ra nhu cầu tiếp cận theo tình huống.

**“HTML có ngữ nghĩa chỉ tốt cho SEO.”** Không đúng. Nó hỗ trợ accessibility, hành vi trình duyệt và khả năng bảo trì.

**“Biến thể thắng A/B test nghĩa thiết kế tốt hơn.”** Chỉ đúng đối với chỉ số, khoảng thời gian và nhóm người dùng đã chọn; vẫn phải xem ảnh hưởng rộng hơn.

## Mô hình tư duy

> Giao diện là một **kiến trúc thông tin và hành động**. Khả năng tiếp cận tốt giúp ý nghĩa và hành động vẫn tồn tại khi người dùng có cơ thể, thiết bị và công nghệ hỗ trợ khác nhau.

## Kết nối

Đọc [HCI và yếu tố con người](./00_hci_human_factors_and_interaction_models.md), [bảo mật web](../07_security_reliability/06_web_application_security.md) và [đạo đức máy tính](../12_society_ethics_profession/00_computing_ethics_privacy_and_professional_responsibility.md).