# Life Knowledge Library — Kiến thức đời sống

> **Mạch đọc:** README này là owner của **Life Knowledge Library**. Route đi từ đối tượng đời sống → nguyên liệu/cấu tạo → cơ chế tạo ra khác biệt → cách đọc thông tin và trade-off → ứng dụng thực tế; mỗi nhánh bên dưới có chapter nền tảng và lớp case/decision để áp dụng mental model đó.

Thư viện này giải thích những đối tượng rất thường gặp trong đời sống nhưng dễ bị hiểu theo tên gọi, thương hiệu hoặc marketing hơn là theo bản chất. Mục tiêu là để người đọc hiểu **nó là gì, được tạo ra hoặc vận hành như thế nào, vì sao có các loại khác nhau, thông số hay nhãn nào thực sự có ý nghĩa, và kiến thức đó được dùng thế nào trong đời sống**.

Nội dung kế thừa [`prompt/COMMON_PROMPT.md`](../prompt/COMMON_PROMPT.md): ưu tiên mô hình tư duy, cơ chế, nguyên lý nền tảng và mạch giải thích liên tục; thuật ngữ chuyên môn được giải thích bằng tiếng Việt kèm từ khóa tiếng Anh/Hàn khi phù hợp.

> **Chuyển mạch:** Contract chung yêu cầu đi từ câu hỏi đến cơ chế và giới hạn; các README nhánh dưới đây áp dụng cùng contract đó cho một nhóm đối tượng cụ thể.

## Mục lục canonical

Đây là bản đồ owner của domain; hãy chọn nhánh theo câu hỏi đời sống rồi đi theo route cơ chế của nhánh đó trước khi so sánh thương hiệu, giá hoặc lời khuyên cộng đồng.

```text
Life
├── Food & Drinks
├── Cars
├── Consumer Knowledge
├── Home
├── Digital Life
├── Everyday Law
├── Safety & First Aid
├── Communication
└── How Things Work
```

Các nhánh được ánh xạ vào filesystem như sau:

- [Food & Drinks](food_drink/README.md): nguyên liệu → lên men/chưng cất/lưu trữ → phong cách → nhãn và cảm nhận; hiện có beer và whisky.
- [Cars](vehicles/cars/README.md): năng lượng → power unit → mô-men → drivetrain → mặt đường → an toàn, thông số và chi phí sở hữu.
- [Consumer Knowledge](consumer_knowledge/README.md): chức năng → cấu tạo/vật liệu → chất lượng → độ bền/bảo hành → tổng chi phí và trade-off.
- [Home](home/README.md): không gian ở → hệ thống điện/nước/nhiệt/không khí → bảo trì → an toàn và chi phí vận hành.
- [Digital Life](digital_life/README.md): thiết bị → tài khoản → dữ liệu → mạng → riêng tư, bảo mật, sao lưu và chú ý.
- [Everyday Law](everyday_law/README.md): sự kiện → quan hệ → quy tắc → chứng cứ → cơ quan, thời hạn và cách phản đối; vấn đề Hàn Quốc chuyên biệt nối sang [Korea Law, Civic & Everyday Life](../korea_law_civic_life/README.md).
- [Safety & First Aid](safety_first_aid/README.md): phòng ngừa → nhận diện nguy hiểm → bảo vệ hiện trường → gọi trợ giúp → sơ cứu trong giới hạn an toàn.
- [Communication](communication/README.md): ý định → bối cảnh chung → kênh → phản hồi → sửa hiểu nhầm và xử lý xung đột.
- [How Things Work](how_things_work/README.md): hiện tượng → ranh giới hệ thống → đầu vào/trạng thái → cơ chế → phản hồi/thất bại → cách kiểm tra.

> **Chuyển mạch:** Mỗi nhánh dưới đây đã có owner, chapter nền tảng và case/decision layer; các module theo model, jurisdiction hoặc sản phẩm cụ thể được mở rộng mà không thay đổi canonical map.

## Canonical map và nguồn

Để kiểm tra độ đầy đủ và freshness, dùng [COVERAGE](COVERAGE.md) cho route/chapter/owner và [SOURCES](SOURCES.md) cho nguồn chính thức, ngày kiểm tra và giới hạn sử dụng. COVERAGE trả lời “học phần nào trước”, còn SOURCES trả lời “claim nào cần xác minh ở đâu”.

## Nguyên tắc của domain

Life Knowledge không phải catalog sản phẩm và cũng không phải bộ mẹo mua hàng. Một khái niệm chỉ thực sự được hiểu khi người đọc có thể giải thích được **vì sao** hai sản phẩm thuộc hai loại khác nhau, sự khác biệt đó đến từ đâu, nó tạo ra hệ quả gì và khi nào sự khác biệt ấy thực sự quan trọng.

Vì vậy các chapter sẽ ưu tiên đường đi `nguồn gốc/vấn đề → cấu tạo hoặc nguyên liệu → cơ chế → phân loại → thuộc tính cảm nhận được → cách đọc thông tin → ứng dụng thực tế`, rồi mới đi tới thương hiệu hoặc ví dụ cụ thể khi chúng giúp làm rõ bản chất.

> **Bàn giao:** Khi bắt đầu một nhánh, hãy quay lại route của chính nhánh đó để biết prerequisite, trục phân loại và điểm dừng; không suy ra chất lượng tổng thể từ một nhãn hoặc một con số đơn lẻ.
