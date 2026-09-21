# Coverage Status — World Atlas

## Coverage phải tách inventory khỏi learning content

Sự tồn tại của `.md` file không đồng nghĩa nội dung hoàn thành. Atlas dùng bốn trạng thái:

- **Inventory**: có tên/mã trong index.
- **Planned**: đáng viết nhưng chưa có full learning content.
- **Reference**: compact legacy note, không tính completion.
- **Learning profile**: đạt Definition of Done và dùng được như chapter ứng dụng.

## Inventory coverage

Inventory toàn cầu đã rộng theo baseline M49 sử dụng trong project. Không cần sinh thêm file để chứng minh completeness của danh sách.

## High-value learning profiles hiện tại

Nhóm ưu tiên Korea–Vietnam / East Asia:

**Republic of Korea, Viet Nam, China, Japan**.

Nhóm vừa được promote trong batch hiện tại:

**Singapore, Indonesia, India**.

Nhóm global economy đã có profile sâu:

**United States, Germany, France, United Kingdom, Italy, Netherlands**.

Một số Africa profile đã qua depth pass và giữ giá trị case study, nhưng toàn bộ Africa Atlas chưa được gắn nhãn “completed”; cần QA từng file theo cùng standard.

## Planned priority — không tạo skeleton trước

Các candidates tiếp theo nếu quay lại Atlas:

**Brazil, Australia, Malaysia, Thailand, Philippines**, sau đó mới cân nhắc Saudi Arabia, Iran, Türkiye, UAE, Egypt, Panama hoặc profile khác dựa trên learning value.

Planned nghĩa là **không cần file mới** nếu file chưa tồn tại; nếu đã có reference file thì giữ status reference/planned cho tới khi được promote.

## Legacy short profiles

Các file 3–25 dòng từ giai đoạn coverage được xem là transitional references. Chúng không nằm trong learning route và không được tính completed.

Mỗi file sau audit sẽ nhận một trong ba quyết định:

**promote** → viết full learning profile;

**merge** → đưa insight vào region/comparative chapter;

**remove** → xóa file nếu không tạo learning value ngoài inventory.

## Completion metric

Không dùng số `.md`.

Theo dõi:

- số core/region chapters đạt depth standard;
- số Atlas learning profiles có causal reasoning;
- chất lượng relative links/prerequisites;
- mức trùng lặp giữa region và country;
- số legacy skeleton được classify/cleanup.

## Profile quality gate

Learning profile phải giải thích:

**relief/tectonics/climate/water → resources → settlement/population → production/economy → transport/corridors → urban hierarchy → trade/external dependency → society/institution → hazards → regional role**.

Nếu chỉ có capital, climate, population và vài bullet economy thì vẫn là Reference.

## Current direction

Core và Regional Geography đang có priority cao hơn Atlas long tail. Atlas chỉ được mở rộng khi profile có giá trị học rõ hoặc liên hệ mạnh với Korea, Vietnam, global economy, resources, trade hay geopolitics.

Xem [Atlas README](./README.md) và [Core Coverage Audit](../CORE_COVERAGE_AUDIT.md).