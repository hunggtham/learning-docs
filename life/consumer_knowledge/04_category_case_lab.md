# Case lab: so sánh một category mà không biến thành bảng xếp hạng

> **Mạch đọc:** [03. Category comparison workbook](03_category_comparison_workbook.md) đã đặt decision boundary và evidence matrix. Lab này cung cấp output tối thiểu để xuất bản một so sánh có thể kiểm tra.

## Hồ sơ case

Ghi rõ người dùng, nhiệm vụ, môi trường, ngân sách, thời gian sở hữu, failure không chấp nhận và ba tiêu chí ưu tiên. Chọn tối đa ba sản phẩm đại diện với phiên bản xác định.

Hồ sơ này tạo boundary cho phép so sánh; từ đó ma trận phải cho thấy claim nào đang được kiểm tra, chứ không chỉ gom thông số của các sản phẩm vào một bảng.

## Ma trận và sensitivity

Mỗi claim cần nguồn/điều kiện. Chạy ít nhất hai scenario và thay đổi biến nhạy nhất. Nếu kết luận đảo, trình bày hai điều kiện thay vì lấy trung bình để che bất định.

Sensitivity là bước nối giữa evidence và quyết định: nó cho biết kết luận phụ thuộc vào biến nào. Chỉ khi đã thấy điểm đảo chiều, ta mới có thể viết output mà không biến bất định thành một thứ hạng giả.

## Output

Hãy ghi năm đầu ra dưới đây theo cùng một lập luận: boundary đặt câu hỏi, evidence cho biết vì sao tin, còn TCO và ngày rà soát giữ kết luận trong đúng điều kiện.

1. câu hỏi và boundary;
2. bảng claim–evidence–limit;
3. TCO khoảng và biến nhạy;
4. lựa chọn theo scenario;
5. dữ liệu cần cập nhật và ngày rà soát.

Năm đầu ra phải đọc như một lập luận có điều kiện: boundary nói câu hỏi, evidence nói vì sao tin, TCO nói chi phí theo thời gian, còn ngày rà soát nói khi nào kết luận mất hiệu lực.

> **Bàn giao:** Case lab là format xuất bản; không ghi “tốt nhất” nếu không nêu người dùng, điều kiện, nguồn và thời điểm.
