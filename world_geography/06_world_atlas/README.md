# World Atlas — Application Layer của Knowledge Library

## Atlas không phải mục tiêu coverage theo số file

World Atlas dùng quốc gia, vùng lãnh thổ và các không gian địa lý như **case study** để áp dụng kiến thức core. Nó không phải bảng tra “thủ đô–dân số–GDP”, cũng không phải dự án tạo một file cho mọi mã chỉ để đạt 100% file coverage.

Danh sách toàn cầu được giữ ở [Global inventory](./01_global_inventory.md). Inventory có thể đầy đủ mà profile học tập vẫn có tính chọn lọc.

## Ba loại nội dung phải phân biệt

**Inventory entry** chỉ đảm bảo một không gian không bị bỏ khỏi danh mục.

**Reference stub** là ghi chú ngắn từ các batch cũ. Nó có thể hữu ích để định vị nhưng **không được tính là chapter hoàn chỉnh** và không nằm trong learning route.

**Learning profile** là tài liệu độc lập có causal reasoning và cross-link với core. Chỉ loại này được xem là nội dung Atlas đã hoàn thiện.

Xem trạng thái: [Coverage status](./03_coverage_status.md).

## Khi nào một country đáng có profile riêng?

Tạo hoặc giữ profile riêng khi territory cung cấp case học đáng giá: cấu trúc địa hình–khí hậu đặc biệt, demographic transition, global production network, major port/corridor, resource system, chokepoint, megadelta, landlocked dependency, city-state, archipelago hoặc liên hệ trực tiếp với Korea–Vietnam.

Nếu kiến thức chỉ lặp lại chapter vùng và không có cơ chế riêng đáng học, nên gộp vào regional/comparative chapter thay vì duy trì skeleton.

## Phương pháp đọc profile

Bắt đầu bằng thesis không gian. Sau đó theo causal chain:

**physical base → climate/water → settlement/population → production → transport/network → external dependencies → hazard/risk → transformation**.

Mục tiêu là có thể giải thích vì sao pattern xuất hiện, không phải nhớ danh sách fact.

## Nội dung bền vững trước snapshot

Atlas ưu tiên địa hình, lưu vực, climate regime, network structure, urban hierarchy và corridor. Dân số, GDP, trade share, government hoặc current dispute thay đổi nhanh chỉ nên đưa vào khi có mục đích phân tích, kèm thời điểm và nguồn.

Với vấn đề chính trị/biên giới, cấu trúc file không phải tuyên bố về chủ quyền. Xem [Methodology](./00_methodology_and_coverage.md).

## Vai trò của Korea và Vietnam trong route

Vì library phục vụ việc học có liên hệ trực tiếp với Korea và Vietnam, East Asia và Southeast Asia là application priority. Các profile Korea–Vietnam–China–Japan và các node ASEAN quan trọng nên được nâng sâu trước khi mở rộng long tail.

Country profile phải quay lại core chapter như population, migration, industry, trade, hydrology hoặc climate. Nếu profile có thể đọc mà không cần core, nó dễ biến thành encyclopedic fact sheet thay vì knowledge graph.

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

Atlas được đọc **sau** [Learning Route](../LEARNING_ROUTE.md), không phải trước.