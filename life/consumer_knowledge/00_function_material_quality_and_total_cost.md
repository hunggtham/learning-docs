# Từ chức năng đến tổng chi phí: cách đọc một sản phẩm

> **Mạch đọc:** [Consumer Knowledge README](README.md) đặt chapter này làm điểm vào cho nhánh tiêu dùng. Ta đi từ nhu cầu và chức năng → cấu tạo/vật liệu → thông số và bằng chứng → độ bền, bảo hành, sửa chữa → khấu hao và tổng chi phí, để câu hỏi “có đáng mua không?” được trả lời trong đúng bối cảnh sử dụng.

## 1. Đừng bắt đầu bằng giá hoặc thương hiệu

Hai sản phẩm chỉ so sánh được khi chúng giải quyết cùng một nhu cầu trong những điều kiện tương tự. Một chiếc xe, máy lọc không khí và đôi giày không có cùng tiêu chí tối ưu; ngay cả hai sản phẩm cùng tên loại cũng có thể khác vì tải, môi trường và tuổi thọ kỳ vọng khác nhau.

Hãy viết nhu cầu thành một câu có điều kiện: **ai dùng, dùng để làm gì, bao nhiêu lần, trong môi trường nào, và điều gì không được phép hỏng**. Câu đó tạo ra chức năng cần kiểm tra và loại bằng chứng cần tìm.

> **Chuyển mạch:** Khi nhu cầu đã rõ, chức năng cho biết kết quả cần có; để biết sản phẩm đạt kết quả bằng cách nào, ta phải nhìn vào cấu tạo và vật liệu chứ không chỉ đọc claim.

## 2. Cấu tạo tạo ra thuộc tính

Vật liệu không tự động đồng nghĩa với chất lượng. Cùng một vật liệu có thể cho kết quả khác do độ dày, xử lý bề mặt, mối nối, dung sai, thiết kế tản nhiệt hoặc cách sản xuất. Vì vậy nên hỏi ba câu: bộ phận nào chịu tải, cơ chế nào tạo ra hiệu năng, và điểm nào sẽ xuống cấp trước?

Một thông số chỉ có nghĩa khi gắn với phép đo và điều kiện đo. `IP rating`, công suất, dung lượng pin, độ phân giải hay tải trọng đều mô tả một thuộc tính trong phạm vi nhất định; không được kéo nó thành kết luận rằng sản phẩm “tốt toàn diện”.

> **Chuyển mạch:** Cấu tạo giải thích vì sao một thuộc tính xuất hiện, còn thông số định lượng mức thuộc tính đó; [01. Reading specs, claims and evidence](01_reading_specs_claims_and_evidence.md) sẽ kiểm tra con số có bằng chứng và giới hạn nào.

## 3. Đọc thông số như một giả thuyết cần kiểm tra

Đọc bảng thông số theo thứ tự:

```text
đại lượng được đo
→ đơn vị và điều kiện đo
→ sai số/phạm vi áp dụng
→ so sánh với nhu cầu
→ chi phí để duy trì thuộc tính
```

Nếu một claim không nói điều kiện đo, hãy coi nó là tín hiệu marketing cần xác minh thêm. Review người dùng hữu ích để phát hiện failure mode và trải nghiệm, nhưng không thay thế thử nghiệm có phương pháp hoặc tài liệu owner.

> **Chuyển mạch:** Bằng chứng giúp ước lượng hiệu năng lúc mới dùng; quyết định dài hạn còn phụ thuộc độ bền, bảo hành, sửa chữa và khả năng thay thế.

## 4. Chất lượng là quan hệ giữa hiệu năng và thời gian

Độ bền không chỉ là “dùng được bao lâu”. Nó bao gồm tốc độ suy giảm, cách phát hiện hỏng, khả năng sửa, giá linh kiện, thời gian chờ và việc sản phẩm còn an toàn khi xuống cấp hay không. Bảo hành là cam kết xử lý trong điều kiện nhất định, không phải bảo đảm mọi hỏng hóc đều được miễn phí.

Khi so sánh, hãy tách `reliability` (xác suất không hỏng trong một khoảng thời gian), `maintainability` (dễ bảo trì/sửa) và `safety` (hỏng thì hậu quả nghiêm trọng đến đâu). Ba thuộc tính này có thể trade-off với nhau.

> **Chuyển mạch:** Độ bền và bảo hành biến hiệu năng thành dòng chi phí theo thời gian; vì vậy giá mua ban đầu chưa phải tổng chi phí sở hữu.

## 5. Tổng chi phí sở hữu và quyết định

Một mô hình đơn giản:

```text
TCO = giá mua
    + vật tư/năng lượng
    + bảo trì và sửa chữa
    + phí dịch vụ/phụ kiện
    − giá trị còn lại
```

Đây là khung suy nghĩ, không phải công thức cố định cho mọi sản phẩm. Nếu độ không chắc chắn lớn, hãy ghi thành khoảng và chỉ ra biến nào nhạy nhất. Sản phẩm rẻ hơn có thể có chi phí vận hành hoặc thay thế cao hơn; sản phẩm đắt hơn chỉ đáng chọn khi lợi ích đó liên quan trực tiếp đến nhu cầu.

> **Bàn giao:** Giữ mental model `nhu cầu → cơ chế → thông số → độ bền → TCO`; áp dụng nó vào [Cars](../vehicles/cars/README.md), [Food & Drinks](../food_drink/README.md) hoặc chapter tiêu dùng cụ thể mà không biến một con số thành phán quyết tổng thể.
