# Thiết kế giao diện, khả năng tiếp cận và tính dễ sử dụng

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Interface design, accessibility và usability**. Route đi từ task/user goals → information architecture/form design → accessibility semantics → keyboard/focus/color/responsive → user testing/A-B/dark patterns, để UX quality được kiểm tra thay vì đoán.

Tính dễ sử dụng (usability) không hoàn toàn là cảm giác chủ quan. Ta có thể quan sát tỷ lệ hoàn thành nhiệm vụ, tỷ lệ lỗi, thời gian thực hiện, khả năng học và mức hài lòng. **khả năng tiếp cận (accessibility / 접근성)** mở rộng câu hỏi: giao diện có thể sử dụng được với người có khả năng giác quan, vận động, nhận thức và thiết bị khác nhau hay không?

## Tính dễ sử dụng phụ thuộc người dùng và nhiệm vụ

Một giao diện rất nhanh với người vận hành có kinh nghiệm có thể khó hiểu với người mới. Dòng lệnh (command line) hiệu quả cho tự động hóa lặp lại nhưng khó tự khám phá hơn giao diện đồ họa.

Vì vậy “dễ dùng” luôn cần ngữ cảnh: ai đang sử dụng, làm nhiệm vụ gì, tần suất bao nhiêu và chi phí của sai sót lớn đến mức nào.

> **Chuyển mạch:** Trong **Thiết kế giao diện, khả năng tiếp cận và tính dễ sử dụng**, **Kiến trúc thông tin** tiếp nhận điểm tựa từ **Tính dễ sử dụng phụ thuộc người dùng và nhiệm vụ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thứ bậc thị giác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiến trúc thông tin

Điều hướng tốt phản ánh cách người dùng phân loại mục tiêu, không nhất thiết phản ánh cấu trúc bảng cơ sở dữ liệu hoặc sơ đồ phòng ban của tổ chức.

Các phương pháp như phân loại thẻ (card sorting), kiểm thử cây điều hướng và phân tích nhật ký tìm kiếm giúp kiểm tra xem mô hình phân nhóm của sản phẩm có khớp với cách người dùng suy nghĩ hay không.

> **Chuyển mạch:** Ở chặng này của **Thiết kế giao diện, khả năng tiếp cận và tính dễ sử dụng**, **Thứ bậc thị giác** tiếp nhận điểm tựa từ **Kiến trúc thông tin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thiết kế biểu mẫu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thứ bậc thị giác

Kích thước, khoảng cách, vị trí, độ tương phản và cách nhóm hướng sự chú ý. Các nguyên lý Gestalt như gần nhau và tương đồng giúp người dùng nhận ra nhóm mà không cần vẽ khung quanh mọi thành phần.

**Thứ bậc thị giác (visual hierarchy)** không chỉ là thẩm mỹ; nó mã hóa mức ưu tiên và quan hệ giữa thông tin.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết kế giao diện, khả năng tiếp cận và tính dễ sử dụng**, **Thiết kế biểu mẫu** tiếp nhận điểm tựa từ **Thứ bậc thị giác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khả năng tiếp cận không phải phần thêm vào cuối dự án** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thiết kế biểu mẫu

Biểu mẫu cần nhãn rõ ràng, ràng buộc đầu vào dễ hiểu, thông báo lỗi gần trường liên quan và giữ dữ liệu người dùng đã nhập khi kiểm tra thất bại.

Kiểm tra sớm ở phía máy khách giúp phản hồi nhanh, nhưng kiểm tra phía máy chủ vẫn bắt buộc vì không thể tin cậy dữ liệu từ máy khách (client / 클라이언트). Thông báo lỗi tốt nói rõ điều gì sai và cách sửa, thay vì chỉ hiển thị “Invalid đầu vào (input / 입력)”.

> **Chuyển mạch:** Trong **Thiết kế giao diện, khả năng tiếp cận và tính dễ sử dụng**, **Khả năng tiếp cận không phải phần thêm vào cuối dự án** tiếp nhận điểm tựa từ **Thiết kế biểu mẫu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bàn phím và focus** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khả năng tiếp cận không phải phần thêm vào cuối dự án

HTML có ngữ nghĩa, điều hướng bằng bàn phím, thứ tự focus, văn bản thay thế, độ tương phản và khả năng phóng to chữ ảnh hưởng kiến trúc thành phần ngay từ đầu.

Trình đọc màn hình (screen reader) dựa vào cây khả năng tiếp cận (accessibility / 접근성) và ngữ nghĩa, chứ không “nhìn điểm ảnh (pixel / 픽셀)” như người có thị lực bình thường.

> **Chuyển mạch:** Ở chặng này của **Thiết kế giao diện, khả năng tiếp cận và tính dễ sử dụng**, **Bàn phím và focus** tiếp nhận điểm tựa từ **Khả năng tiếp cận không phải phần thêm vào cuối dự án** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Màu sắc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bàn phím và focus

Các điều khiển tương tác phải có thể tiếp cận bằng bàn phím khi nền tảng và trường hợp sử dụng yêu cầu. Chỉ báo focus cho biết phần tử đang nhận thao tác; hộp thoại modal phải quản lý việc đưa focus vào, giữ focus bên trong khi cần và trả focus về vị trí hợp lý sau khi đóng.

Một `div` tự chế để bấm thường thiếu ngữ nghĩa bàn phím và vai trò khả năng tiếp cận (accessibility / 접근성) nếu lập trình viên không bổ sung đầy đủ hành vi tương ứng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết kế giao diện, khả năng tiếp cận và tính dễ sử dụng**, **Màu sắc** tiếp nhận điểm tựa từ **Bàn phím và focus** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thiết kế đáp ứng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Màu sắc

Không nên dùng màu làm kênh duy nhất để truyền trạng thái vì người dùng có khả năng nhận màu khác nhau, và hệ thống có thể chạy ở chế độ đơn sắc hoặc tương phản cao.

Trạng thái lỗi có thể kết hợp biểu tượng, văn bản và màu. Độ tương phản cần đáp ứng hướng dẫn khả năng tiếp cận (accessibility / 접근성) tương ứng; ngưỡng cụ thể phụ thuộc tiêu chuẩn và ngữ cảnh.

> **Chuyển mạch:** Trong **Thiết kế giao diện, khả năng tiếp cận và tính dễ sử dụng**, **Thiết kế đáp ứng** tiếp nhận điểm tựa từ **Màu sắc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiểm thử với người dùng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thiết kế đáp ứng

**Thiết kế đáp ứng (responsive design)** không chỉ là thu nhỏ giao diện desktop. Màn hình cảm ứng nhỏ có kích thước vùng chạm, tầm với ngón tay, bàn phím ảo và điều kiện mạng khác.

Vì vậy bố cục và mức ưu tiên nội dung đôi khi phải thay đổi, chứ không chỉ co giãn bằng CSS.

> **Chuyển mạch:** Ở chặng này của **Thiết kế giao diện, khả năng tiếp cận và tính dễ sử dụng**, **Kiểm thử với người dùng** tiếp nhận điểm tựa từ **Thiết kế đáp ứng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thử nghiệm A/B** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểm thử với người dùng

Quan sát người dùng đại diện thực hiện các nhiệm vụ đại diện giúp phát hiện khoảng cách giữa mô hình của đội phát triển và cách người dùng thật sự hiểu sản phẩm.

“5 người dùng” không phải con số thần kỳ cho mọi nghiên cứu. Cỡ mẫu phụ thuộc mục tiêu, độ biến thiên và việc phương pháp là định tính hay cần suy luận thống kê.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết kế giao diện, khả năng tiếp cận và tính dễ sử dụng**, **Thử nghiệm A/B** tiếp nhận điểm tựa từ **Kiểm thử với người dùng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu thiết kế thao túng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thử nghiệm A/B

Thử nghiệm A/B có thể đo ảnh hưởng nhân quả của một biến thể giao diện nếu việc ngẫu nhiên hóa và chỉ số được thiết kế đúng. Tuy nhiên một chỉ số cục bộ tăng không có nghĩa kết quả dài hạn tốt hơn.

Ví dụ tăng số lần bấm thông báo không đồng nghĩa tăng lợi ích cho người dùng. Vì vậy chỉ số chính cần đi cùng các chỉ số bảo vệ (guardrail metric).

> **Chuyển mạch:** Trong **Thiết kế giao diện, khả năng tiếp cận và tính dễ sử dụng**, **Mẫu thiết kế thao túng** tiếp nhận điểm tựa từ **Thử nghiệm A/B** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những hiểu nhầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu thiết kế thao túng

**Mẫu tối (dark pattern)** dùng sự bất cân xứng hoặc gây nhầm lẫn để hướng người dùng làm điều trái với lợi ích hoặc mong muốn của họ, chẳng hạn hủy đăng ký khó hơn đăng ký hoặc che phí bổ sung.

Đây là điểm giao giữa HCI và đạo đức: thiết kế có hiệu quả trong việc thúc đẩy hành vi không tự động đồng nghĩa với thiết kế có trách nhiệm.

> **Chuyển mạch:** Ở chặng này của **Thiết kế giao diện, khả năng tiếp cận và tính dễ sử dụng**, **Mẫu thiết kế thao túng** đã nêu tiêu chí phân biệt, còn **Những hiểu nhầm thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu nhầm thường gặp

**“khả năng tiếp cận (accessibility / 접근성) chỉ dành cho một nhóm nhỏ.”** Không đúng. Chấn thương tạm thời, tuổi tác, ánh sáng mạnh, sử dụng một tay và mạng kém đều tạo ra nhu cầu tiếp cận theo tình huống.

**“HTML có ngữ nghĩa chỉ tốt cho SEO.”** Không đúng. Nó hỗ trợ khả năng tiếp cận (accessibility / 접근성), hành vi trình duyệt và khả năng bảo trì.

**“Biến thể thắng A/B kiểm thử (test / 테스트) nghĩa thiết kế tốt hơn.”** Chỉ đúng đối với chỉ số, khoảng thời gian và nhóm người dùng đã chọn; vẫn phải xem ảnh hưởng rộng hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết kế giao diện, khả năng tiếp cận và tính dễ sử dụng**, **Những hiểu nhầm thường gặp** đã nêu tiêu chí phân biệt, còn **Mô hình tư duy** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> Giao diện là một **kiến trúc thông tin và hành động**. Khả năng tiếp cận tốt giúp ý nghĩa và hành động vẫn tồn tại khi người dùng có cơ thể, thiết bị và công nghệ hỗ trợ khác nhau.

> **Chuyển mạch:** Trong **Thiết kế giao diện, khả năng tiếp cận và tính dễ sử dụng**, **Kết nối** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc [HCI và yếu tố con người](./00_hci_human_factors_and_interaction_models.md), [bảo mật web](../07_security_reliability/06_web_application_security.md) và [đạo đức máy tính](../12_society_ethics_profession/00_computing_ethics_privacy_and_professional_responsibility.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
