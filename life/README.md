# Life Knowledge Library — Kiến thức đời sống

> **Mạch đọc:** README này là owner của **Life Knowledge Library**. Route đi từ đối tượng đời sống → nguyên liệu/cấu tạo → cơ chế tạo ra khác biệt → cách đọc thông tin và trade-off → ứng dụng thực tế; mỗi nhánh bên dưới có chapter nền tảng và lớp case/decision để áp dụng mental model đó.

Thư viện này giải thích những đối tượng rất thường gặp trong đời sống nhưng dễ bị hiểu theo tên gọi, thương hiệu hoặc tiếp thị hơn là theo bản chất. Mục tiêu là để người đọc hiểu **nó giải quyết vấn đề gì, được tạo ra hoặc vận hành như thế nào, vì sao có các loại khác nhau, thông số hay nhãn nào thực sự có ý nghĩa, cách sử dụng/bảo dưỡng thay đổi kết quả ra sao, và kiến thức đó được dùng thế nào khi so sánh sản phẩm**.

Nội dung kế thừa [`prompt/COMMON_PROMPT.md`](../prompt/COMMON_PROMPT.md): ưu tiên mô hình tư duy, cơ chế, nguyên lý nền tảng và mạch giải thích liên tục; thuật ngữ chuyên môn được giải thích bằng tiếng Việt kèm từ khóa tiếng Anh/Hàn khi phù hợp.

---

## Life sở hữu phạm vi nào?

`life/` không phải thư mục chứa “mọi thứ ngoài đời”. Nó là **everyday object & consumer literacy**: những đồ vật, sản phẩm, vật liệu và hệ thống nhỏ mà một cá nhân trực tiếp sử dụng, bảo quản, bảo dưỡng, so sánh hoặc mua sắm.

Mental model chung:

```text
problem / use case (nhu cầu & ràng buộc)
→ material / ingredient (nguyên liệu / vật liệu cấu thành)
→ construction / production (quy trình sản xuất / chế tạo)
→ mechanism (cơ chế vận hành / chuyển hóa)
→ classification axes (các trục phân loại độc lập)
→ specs / labels (thông số kỹ thuật & nhãn mác)
→ trade-offs (các điểm đánh đổi kỹ thuật)
→ use / maintenance (sử dụng & bảo dưỡng đúng cách)
→ failure / degradation (suy thoái & chế độ hỏng hóc)
→ comparison / ownership (so sánh lựa chọn & tổng chi phí sở hữu)
```

Ranh giới (boundary) quan trọng với các domain khác:
- Hệ thống hạ tầng xã hội quy mô lớn (lưới điện, mạng lưới cấp thoát nước, logistics) → [`How Things Work`](how_things_work/README.md) khi domain đó canonical.
- Khả năng chi trả, quản lý nợ, ngân sách, bảo hiểm hộ gia đình → `Personal Finance`.
- Phương pháp lập luận, đánh giá bằng chứng, tư duy xác suất và ra quyết định → `Thinking Toolkit`.
- Lý thuyết khoa học hình thức sâu → [`Physics`](../physics/README.md), [`Chemistry`](../chemistry/README.md), [`Biology`](../biology/README.md), [`Electrical Engineering`](../electrical_engineering/README.md).
- Quy trình pháp lý và thủ tục hành chính chuyên biệt cho người nước ngoài tại Hàn Quốc → [`Korea Law, Civic & Everyday Life`](../korea_law_civic_life/README.md).

---

## Mục lục canonical

Đây là bản đồ owner của domain; hãy chọn nhánh theo câu hỏi đời sống rồi đi theo route cơ chế của nhánh đó trước khi so sánh thương hiệu, giá hoặc lời khuyên cộng đồng.

```text
Life
├── Food & Drinks (Đồ uống & Văn hóa thưởng thức: Bia & Whisky)
├── Vehicles & Cars (Phương tiện & Xe hơi: Nền tảng + 13 bài chuyên sâu)
├── Consumer Knowledge & Literacy (Đọc sản phẩm bằng cơ chế, vật liệu, độ bền & TCO)
├── Home (Hệ thống nhà ở, điện, nước, nhiệt và vi khí hậu)
├── Digital Life (Thiết bị, tài khoản, dữ liệu, bảo mật và quyền riêng tư)
├── Everyday Law (Quy tắc pháp lý đời sống, hợp đồng, chứng cứ và cơ quan)
├── Safety & First Aid (An toàn hiện trường, sơ cấp cứu và phòng ngừa tai nạn)
├── Communication (Giao tiếp, truyền tải bối cảnh, xử lý xung đột và đàm phán)
└── How Things Work (Ranh giới hệ thống, cơ chế, phản hồi và cách kiểm tra)
```

Các nhánh được ánh xạ vào filesystem như sau:

- [Food & Drinks](food_drink/README.md): nguyên liệu → lên men/chưng cất/lưu trữ → hệ phân loại → nhãn mác và cảm nhận; gồm tầng tổng quan liên ngành ([01](food_drink/01_style_process_and_tasting.md), [02](food_drink/02_regulation_comparison_and_serving.md), [03](food_drink/03_beer_whisky_comparison_lab.md)) cùng hai chuỗi chuyên sâu về [Whisky](food_drink/whisky/00_whisky_foundations.md) (00–04) và [Bia](food_drink/beer/00_beer_foundations.md) (00–02).
- [Vehicles & Cars](vehicles/cars/README.md): năng lượng → động cơ → mô-men → hệ dẫn động → lốp xe → an toàn ADAS, chẩn đoán bảo dưỡng và chi phí sở hữu; kết nối giữa [tầng nền tảng](vehicles/cars/README.md#tang-1-nen-tang-he-thong--tong-quan-van-hanh) (00–03) và [13 bài học cơ chế chuyên sâu](vehicles/cars/README.md#tang-2-chuyen-sau-co-che--chi-tiet-phan-he) (01–13).
- [Consumer Knowledge](consumer_knowledge/README.md) & [Consumer Literacy](consumer_literacy/README.md): chức năng → cấu tạo/vật liệu → chất lượng → độ bền/bảo hành → tổng chi phí và trade-off; là khung tư duy dùng lại cho mọi sản phẩm tiêu dùng.
- [Home](home/README.md): không gian ở → hệ thống điện/nước/nhiệt/không khí → bảo trì phòng ngừa → an toàn và chi phí vận hành.
- [Digital Life](digital_life/README.md): thiết bị → tài khoản → dữ liệu → mạng → riêng tư, bảo mật, sao lưu và chú ý số.
- [Everyday Law](everyday_law/README.md): sự kiện → quan hệ pháp luật → quy tắc → chứng cứ → cơ quan tiếp nhận, thời hạn và cách bảo vệ quyền lợi.
- [Safety & First Aid](safety_first_aid/README.md): phòng ngừa rủi ro → nhận diện hiện trường → bảo vệ bản thân và nạn nhân → gọi trợ giúp → sơ cứu trong giới hạn an toàn.
- [Communication](communication/README.md): ý định → bối cảnh chung → lựa chọn kênh → phản hồi → hóa giải hiểu nhầm và xử lý xung đột.
- [How Things Work](how_things_work/README.md): hiện tượng đời sống → ranh giới hệ thống → đầu vào/trạng thái → cơ chế → phản hồi/thất bại → cách kiểm chứng thực tế.

---

## Nguyên tắc của domain

Life Knowledge không phải catalog sản phẩm và cũng không phải bộ mẹo mua hàng. Một khái niệm chỉ thực sự được hiểu khi người đọc có thể giải thích được **vì sao** hai sản phẩm thuộc hai loại khác nhau, sự khác biệt đó đến từ đâu, nó tạo ra hệ quả gì và khi nào sự khác biệt ấy thực sự quan trọng.

Vì vậy các chapter ưu tiên đường đi:

```text
nguồn gốc / vấn đề thực tế
→ cấu tạo hoặc nguyên liệu
→ cơ chế vận hành
→ trục phân loại độc lập
→ thuộc tính đo lường được
→ thuộc tính cảm nhận được
→ sử dụng / bảo dưỡng / suy thoái
→ ứng dụng thực tế & so sánh lựa chọn
```

Thương hiệu và model cụ thể chỉ xuất hiện khi chúng giúp làm rõ một cơ chế, một trục phân loại hoặc một điểm đánh đổi; không dùng danh sách thương hiệu để thay cho kiến thức.

---

## Điều phối và Kiểm toán (Coordination & Audit)

- [`CONCEPTUAL_DEPENDENCIES.md`](CONCEPTUAL_DEPENDENCIES.md) — các khái niệm và mô hình tư duy được sử dụng xuyên suốt giữa nhiều nhóm sản phẩm.
- [`COVERAGE.md`](COVERAGE.md) — bản đồ bao phủ canonical, đối chiếu owner, chapter hiện có và câu hỏi mở rộng kế tiếp.
- [`SOURCES.md`](SOURCES.md) — danh mục nguồn tài liệu chính thức, phiên bản và giới hạn áp dụng.
- [`COVERAGE_AUDIT.md`](COVERAGE_AUDIT.md) — kiểm toán độ sâu của các module: phần nào đã đạt độ sâu cần thiết, phần nào đang triển khai hoặc thuộc domain khác.

Mục tiêu dài hạn không phải là bao phủ mọi đồ vật trên thế giới, mà là xây dựng một hệ thống mô hình tư duy đủ sắc bén để khi người học gặp một sản phẩm mới chưa từng học, họ vẫn biết **phải đặt những câu hỏi nào để hiểu rõ bản chất của nó**.

> **Bàn giao:** Khi bắt đầu một nhánh, hãy quay lại route của chính nhánh đó để biết prerequisite, trục phân loại và điểm dừng; không suy ra chất lượng tổng thể từ một nhãn hiệu hoặc một con số đơn lẻ.
