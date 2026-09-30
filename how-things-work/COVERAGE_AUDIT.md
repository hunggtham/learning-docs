# How Things Work — Coverage & Depth Audit

> Audit date: 2026-09-30. Mục tiêu của audit là giữ library có chiều sâu và đường đọc rõ, không tăng số file chỉ để tăng coverage.

## 1. Coverage hiện tại — 22 systems

| Topic | End-to-end | Korea ↔ Vietnam | Failure/bottleneck | Cross-links | Case integration | Status |
|---|---:|---:|---:|---:|---:|---|
| Internet | ✓ | ✓ | ✓ | ✓ | ✓ | Core complete |
| Electricity grid | ✓ | ✓ | ✓ | ✓ | ✓ | Core complete |
| Water supply | ✓ | ✓ | ✓ | ✓ | ✓ | Core complete |
| Sewage | ✓ | ✓ | ✓ | ✓ | ✓ | Core complete |
| Banking system | ✓ | ✓ | ✓ | ✓ | ✓ | Core complete |
| Credit-card network | ✓ | ✓ | ✓ | ✓ | ✓ | Core complete |
| Stock market | ✓ | ✓ | ✓ | ✓ | ✓ | Core complete + settlement case |
| Shipping logistics | ✓ | ✓ | ✓ | ✓ | ✓ | Core complete |
| Supermarkets | ✓ | ✓ | ✓ | ✓ | ✓ | Core complete |
| Airlines | ✓ | ✓ | ✓ | ✓ | ✓ | Core complete |
| Airports | ✓ | ✓ | ✓ | ✓ | ✓ | Core complete |
| GPS/GNSS | ✓ | ✓ | ✓ | ✓ | ✓ | Core complete |
| Satellites | ✓ | ✓ | ✓ | ✓ | ✓ | Core complete + EO pipeline case |
| Mobile networks | ✓ | ✓ | ✓ | ✓ | ✓ | Core complete |
| Semiconductors | ✓ | ✓ | ✓ | ✓ | ✓ | Core complete |
| Cloud computing | ✓ | ✓ | ✓ | ✓ | ✓ | Core complete |
| Public transport | ✓ | ✓ | ✓ | ✓ | ✓ | Phase 2 core complete |
| Road traffic | ✓ | ✓ | ✓ | ✓ | ✓ | Phase 2 core complete |
| Waste/recycling | ✓ | ✓ | ✓ | ✓ | ✓ | Phase 2 core complete |
| Postal/parcel | ✓ | ✓ | ✓ | ✓ | ✓ | Phase 2 core complete |
| Fuel/oil supply | ✓ | ✓ | ✓ | ✓ | ✓ | Phase 2 core complete |
| Construction/buildings | ✓ | ✓ | ✓ | ✓ | ✓ | Phase 2 core complete |

`Core complete` nghĩa chapter đã đủ để người đọc hiểu flow chính mà không cần Google chỉ để biết “hệ thống chạy ra sao”. Nó không có nghĩa bao phủ mọi standard, luật, actor hay edge case.

## 2. Lớp tích hợp hiện tại

### System map

[`SYSTEM_MAP.md`](./SYSTEM_MAP.md) nối 22 topic bằng energy, information, money, physical flow và waste/return flow; đồng thời chỉ ra buffer, feedback loop và common-mode dependency.

### Korea ↔ Vietnam comparison

[`KOREA_VIETNAM_COMPARISON.md`](./KOREA_VIETNAM_COMPARISON.md) dùng cùng các trục actor, operator, market, finality, buffer, bottleneck và global dependency để tránh kiểu so sánh rời rạc.

### Integrated cases

Hiện có 9 case:

1. convenience store payment → inventory → restock;
2. e-commerce Korea → Vietnam;
3. Seoul → Hanoi flight;
4. power outage cascade;
5. semiconductor Korea → Vietnam electronics chain;
6. buy one stock Korea ↔ Vietnam → T+2 settlement;
7. Earth-observation satellite → processed data/application;
8. high-rise apartment utility boundary;
9. urban commute Seoul ↔ Hà Nội ↔ TP.HCM.

Các case hiện bao phủ commerce, financial settlement, urban mobility, aviation, infrastructure dependency, built environment, Earth observation và industrial supply chain.

## 3. Phase 2 đã hoàn tất

Backlog Phase 2 trước đó:

```text
01 public-transport       ✓
02 road-traffic           ✓
03 waste-recycling        ✓
04 postal-parcel          ✓
05 fuel-oil-supply        ✓
06 construction-buildings ✓
```

Điểm quan trọng là sáu topic không chỉ được thêm folder; chúng đã được nối vào README, `SYSTEM_MAP.md`, `KOREA_VIETNAM_COMPARISON.md` và case studies.

## 4. Depth gap cũ đã được xử lý

### Stock market

Đã thêm [`case-studies/06_BUY_ONE_STOCK_KOREA_VIETNAM.md`](./case-studies/06_BUY_ONE_STOCK_KOREA_VIETNAM.md) để đi từ broker app → matching → clearing → depository → T+2 settlement.

### Satellites

Đã thêm [`case-studies/07_EARTH_OBSERVATION_DATA_PIPELINE.md`](./case-studies/07_EARTH_OBSERVATION_DATA_PIPELINE.md) để đi từ tasking → acquisition → ground station → image processing → GIS/AI → decision.

### Water/sewage/building boundary

Đã thêm [`case-studies/08_HIGH_RISE_APARTMENT_UTILITIES.md`](./case-studies/08_HIGH_RISE_APARTMENT_UTILITIES.md), làm rõ city utility boundary với tank/pump/transformer/risers/internal drainage của building.

## 5. Candidate Phase 3 — chỉ mở nếu tiếp tục có giá trị hệ thống

### Healthcare delivery system

```text
patient
→ appointment/triage
→ clinic/hospital
→ lab/imaging
→ pharmacy
→ insurance/payment
→ medical record
```

Rất hữu ích khi so Korea ↔ Vietnam, nhưng cần source y tế/pháp lý chặt hơn và boundary rõ với personal health docs.

### Insurance system

```text
risk pool
→ premium
→ underwriting
→ policy
→ claim
→ loss assessment
→ payout
→ reinsurance
```

Nối personal finance, banking, healthcare, cars và disasters.

### Food supply / agriculture

```text
farm
→ aggregation
→ cold chain
→ wholesale market
→ processing
→ retailer
→ consumer
```

Nối supermarket, logistics, water, fuel, weather/satellite và waste.

### Emergency response

```text
incident
→ emergency call
→ dispatch
→ police/fire/ambulance
→ routing
→ hospital/incident command
```

Nối mobile network, GPS, road traffic, healthcare, buildings và disaster response.

### Education system

```text
student
→ school/university
→ curriculum/assessment
→ admissions/credentials
→ finance/government
→ labor market
```

Có giá trị so sánh xã hội Hàn–Việt nhưng có overlap với sociology/policy, nên cần ownership boundary tốt.

### Natural gas / district heating

Có thể tách khỏi `fuel-oil-supply` nếu depth đủ lớn: LNG import → terminal → regasification → pipeline → city gas/power/industry; Korea có district-heating/city-gas context đáng học, Việt Nam có LNG/power infrastructure đang mở rộng.

## 6. Chưa nên thêm chỉ để tăng số topic

Không nên tạo chapter riêng cho mọi consumer product. Một topic chỉ đáng thành system chapter nếu có:

- multi-actor flow;
- physical/data/control layers;
- meaningful finality/state;
- bottlenecks/failure propagation;
- Korea ↔ Vietnam topology đủ khác để học được điều gì đó;
- cross-links mạnh với library hiện tại.

Nếu thiếu các điều kiện này, nội dung phù hợp hơn với `life/` hoặc domain chuyên môn khác.

## 7. Quality checklist cho chapter mới

Một chapter chỉ được coi là đủ khi trả lời được:

```text
What enters the system?
What exits?
Which actors own vs operate each layer?
Where is state stored?
What is the control plane?
What is the physical/data plane?
When is the process final?
What buffers delay failure?
Where are bottlenecks?
How can failures propagate?
How does Korea organize it?
How does Vietnam organize it?
Which canonical docs own deeper theory?
```

Nếu chỉ trả lời “nó là gì” và liệt kê thành phần, chapter chưa đạt mục tiêu library.

## 8. Trạng thái trước merge

`docs/how-things-work-korea-vietnam` vẫn là feature branch. Trước merge vào `main` cần:

1. kiểm tra toàn bộ internal links;
2. kiểm tra URL nguồn chính thức;
3. rà claim time-sensitive theo snapshot 2026-09-30;
4. thêm `how-things-work` vào `CATALOG.md` và root `README.md` khi quyết định canonical hóa;
5. kiểm tra site navigation/indexing của `learning-library/` nếu pipeline không tự discover folder mới;
6. review diff cuối và merge/squash theo branch workflow.

Audit này là checklist integration, không phải lý do giữ branch tồn tại lâu sau khi merge.
