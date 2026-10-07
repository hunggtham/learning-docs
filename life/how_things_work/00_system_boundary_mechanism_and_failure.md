# Ranh giới hệ thống, cơ chế và failure mode

> **Mạch đọc:** [How Things Work README](README.md) dùng chapter này làm khung phân tích xuyên các nhánh Life. Ta đi từ hiện tượng → ranh giới hệ thống → input/state/output → cơ chế và ràng buộc → phản hồi, failure mode và cách kiểm tra.

## 1. Bắt đầu bằng hiện tượng có thể quan sát

Một câu hỏi tốt mô tả điều xảy ra và điều kiện xảy ra: “pin tụt nhanh khi dùng định vị”, “phòng ẩm sau khi tắm”, “bia cùng tên có vị khác”, hoặc “tin nhắn bị hiểu sai”. Tránh bắt đầu bằng nhãn nguyên nhân như “do app lỗi” hay “do máy kém”.

Hiện tượng là output cần giải thích; nó chưa cho biết ranh giới hệ thống hoặc biến ẩn. Hãy ghi cái thay đổi, cái giữ nguyên và dữ kiện nào có thể quan sát lại.

> **Chuyển mạch:** Khi hiện tượng đã cụ thể, ta chọn ranh giới để biết cái gì nằm trong hệ thống và cái gì là môi trường tác động.

## 2. Ranh giới và luồng vào–ra

Mọi mô hình đều bỏ qua một phần thế giới. Với xe, ranh giới có thể gồm power unit đến lốp; với đời sống số, gồm thiết bị, tài khoản, mạng và dịch vụ; với nhà, gồm vỏ công trình và hệ thống kỹ thuật.

Ghi `input → state → process → output` và thêm thời gian, năng lượng, thông tin hoặc vật chất đi qua. Nếu output không khớp, hãy hỏi input nào đổi, state nào bị giữ sai hoặc process nào có giới hạn.

> **Chuyển mạch:** Ranh giới cho biết thành phần; cơ chế giải thích quan hệ giữa chúng và dự đoán output khi điều kiện thay đổi.

## 3. Cơ chế, ràng buộc và phản hồi

Một cơ chế không chỉ là chuỗi bước; nó phải nói biến nào tác động biến nào, qua quan hệ gì và trong điều kiện nào. Ràng buộc như nhiệt, ma sát, băng thông, vật liệu, chú ý hoặc quy định làm giới hạn kết quả.

Phản hồi làm output quay lại tác động input hoặc state. Phản hồi dương có thể khuếch đại thay đổi; phản hồi âm có thể ổn định hệ thống. Nhận ra vòng phản hồi giúp giải thích vì sao một lỗi nhỏ trở thành cascade hoặc vì sao hệ thống tự cân bằng.

> **Chuyển mạch:** Mô hình chỉ hữu ích nếu nói được lúc nào nó hỏng; failure mode và phép kiểm tra biến lời giải thích thành kiến thức có thể dùng.

## 4. Kiểm tra và giới hạn

Tách prediction khỏi story. Viết một dự đoán có thể quan sát, thay đổi một biến khi an toàn, ghi kết quả và nêu điều kiện khiến phép thử không kết luận được. Không biến tương quan thành cơ chế nhân quả chỉ vì hai hiện tượng xuất hiện cùng lúc.

How Things Work không thay thế owner chuyên môn. Nó nối [Cars](../vehicles/cars/README.md), [Home](../home/README.md), [Digital Life](../digital_life/README.md) và các nhánh khác bằng cùng một khung, nhưng claim chi tiết vẫn phải quay về chapter của domain đó.

> **Bàn giao:** Giữ invariant `hiện tượng → boundary → input/state → mechanism → constraint/feedback → test`; dùng nó để mở chapter mới hoặc phát hiện khi một lời giải thích đời thường còn thiếu biến quan trọng.
