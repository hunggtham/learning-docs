# World Atlas — Application Layer của Knowledge Library

## Atlas không phải dự án 100% country-file coverage

World Atlas dùng quốc gia, vùng lãnh thổ và các không gian địa lý như **case study** để áp dụng core Geography. Nó không phải bảng tra “thủ đô–dân số–GDP” và không tạo một file ngắn cho mỗi mã chỉ để đủ danh sách.

Danh sách toàn cầu được giữ ở [Global inventory](./01_global_inventory.md). Inventory có thể rộng trong khi learning-profile layer vẫn được curated.

## Bốn trạng thái nội dung

**Inventory**: chỉ có tên/mã trong index; không có learning chapter riêng cũng hoàn toàn chấp nhận được.

**Planned**: được đánh dấu là đáng có profile sau này nhưng chưa đủ nội dung. Planned không được tính completion.

**Reference**: file ngắn từ batch cũ có một số orientation/mental model. Nó có thể hỗ trợ navigation nhưng không phải chapter học hoàn chỉnh.

**Learning profile**: chapter đủ sâu, có causal reasoning và cross-link với core. Chỉ trạng thái này được tính là completed Atlas learning content.

Xem [Coverage Status](./03_coverage_status.md).

## Khi nào một country đáng có profile riêng?

Profile riêng chỉ có giá trị khi territory tạo một case học rõ, ví dụ:

- liên hệ trực tiếp Korea–Vietnam;
- major economy hoặc manufacturing/value-chain node;
- major port, chokepoint hoặc transport corridor;
- resource/energy system có ảnh hưởng vượt biên giới;
- megadelta, landlocked dependency, archipelago hoặc city-state;
- physical–human relationship đặc biệt giúp transfer mental model sang nơi khác.

Nếu kiến thức chỉ lặp region chapter và không có mechanism riêng đáng học, nên giữ ở inventory hoặc gộp vào comparative/subregional chapter.

## Causal chain bắt buộc

Learning profile không được viết như encyclopedia rời rạc. Cấu trúc giải thích phải làm rõ:

**physical geography → climate/water → resources → settlement/population → economy/production → transport/network → society/institutions → regional/global role → hazards/transformation**.

Không cần mỗi profile có đúng cùng số heading, nhưng phải cho thấy các lớp ảnh hưởng nhau như thế nào.

## Priority hiện tại

### Tier 1 — trực tiếp với learning route

**Republic of Korea, Viet Nam, China, Japan**.

Đây là các case chính để nối East Asia/Southeast Asia với demographic transition, manufacturing GVC, maritime trade, urban concentration, resource dependency và climate/water risk.

### Tier 2 — global economy

**United States** và các major European economies đã được depth-pass như **Germany, France, United Kingdom, Italy, Netherlands**.

Các profile này có giá trị vì market scale, industrial/service networks, ports, finance, energy transition và global value chains.

### Tier 3 — trade/resource/geopolitical mechanisms

Ưu tiên có chọn lọc các case như India, Singapore, Indonesia, Malaysia, Thailand, Philippines, Saudi Arabia, Iran, Türkiye, United Arab Emirates, Egypt, Panama, Brazil, Australia hoặc các nơi khác nếu có mechanism đủ mạnh.

Tier 3 là roadmap, không phải yêu cầu tạo ngay tất cả profile.

## Nội dung bền vững trước snapshot

Atlas ưu tiên địa hình, lưu vực, climate regime, urban hierarchy, resource/value chain, port/corridor và regional role. Population, GDP, trade share, government hoặc current dispute thay đổi nhanh chỉ nên thêm khi có mục đích phân tích, kèm thời điểm và nguồn.

Với vấn đề chính trị/biên giới, cấu trúc file không phải tuyên bố về chủ quyền. Xem [Methodology](./00_methodology_and_coverage.md).

## Cấu trúc

```text
06_world_atlas/
├── 00_methodology_and_coverage.md
├── 01_global_inventory.md
├── 02_profile_template.md
├── 03_coverage_status.md
├── africa/
├── americas/
├── asia/
├── europe/
├── oceania/
├── antarctica/
└── supplemental/
```

Các folder địa lý có thể chứa cả learning profile và legacy reference file. **Folder presence không biểu thị completion**.

## Quy tắc cleanup

Khi audit một subregion, mỗi legacy short file phải nhận một quyết định:

**promote** → viết thành learning profile;

**merge** → chuyển kiến thức có giá trị vào regional/comparative chapter;

**reference/planned** → giữ để navigation nhưng không tính completed;

**remove** → xóa nếu không còn giá trị ngoài inventory.

Không tạo thêm legacy stub mới.

## Cách dùng Atlas khi học

Atlas được đọc **sau** [Learning Route](../LEARNING_ROUTE.md). Trước khi mở profile, hãy tự dự đoán physical constraint, water/resource, settlement, production corridor và external dependency. Sau đó dùng profile để kiểm tra reasoning.

Nếu không thể giải thích concept như monsoon, agglomeration, demographic transition hay chokepoint, quay lại core chapter thay vì tìm thêm country fact.