# Coverage Audit — World History

## Kết luận hiện tại

`world_history/` đã có **breadth tốt**: đủ 17 giai đoạn theo chuỗi người dùng yêu cầu, có phương pháp, glossary và cross-link với Geography/Korean History/Culture. Depth pass này đã làm dày 14 canonical chapters trọng tâm (Agricultural Revolution → post-1991) bằng initial conditions, actors, institutions, material constraints, mechanism, event sequence, competing interpretations, consequences và path dependence. Mục tiêu là chapter đọc độc lập ở mức **advanced foundation**; đây vẫn không phải chuyên khảo theo từng vùng, nguồn hay tranh luận sử học.

Đây là baseline đủ chắc để chuyển từ “lấp khoảng trống” sang **depth có chọn lọc**. Vòng đánh giá này đã bổ sung case studies liên vùng, transition matrix và source workbench; ưu tiên kế tiếp là gắn các case đó vào bibliography cụ thể và các chapter chuyên đề, không sinh thêm hàng loạt file timeline.

## Ma trận chất lượng

| Tiêu chí | Trạng thái | Ghi chú |
| --- | --- | --- |
| Period coverage | Mạnh | 17 giai đoạn từ origins đến post-Cold War |
| Causal spine | Mạnh | Mỗi chapter có technology/resources/institutions/trade/warfare/demography/ideas và depth sequence |
| Regional balance | Khá–mạnh | Đã thêm case West Africa, South/Southeast Asia, East Asia, Mesoamerica/Andes và các basin/biển; cần depth chapter riêng nếu chọn ưu tiên |
| Material systems | Mạnh | Food, land, energy, metals, shipping, finance và ecological externality đã có causal treatment |
| Institutions | Mạnh | State, empire, law, religion, company, party, alliance đã được đặt vào chuỗi |
| Social distribution | Khá–mạnh | Có coercion, slavery, gender, class, migration và winner–loser; cần case study tiếng nói bị trị |
| Demography/disease | Khá–mạnh | Có disease, migration, displacement và uncertainty; cần time series chọn lọc |
| Warfare/logistics | Mạnh | Từ raid đến total war/proxy war, có supply, debt, food, energy và alliance logistics |
| Ideas/legitimacy | Mạnh | Không tách ideas khỏi institutions và material base |
| Evidence/source practice | Mạnh | Mỗi chapter ghi loại evidence, archive bias và limitation; `22_source_workbench` chuẩn hoá cách kiểm tra và `23_annotated_bibliography` cung cấp reading map có giới hạn rõ |
| Cross-links | Mạnh | Index, methods và link sang Geography/Korea đã có |
| Study usability | Mạnh | README, dependency graph, learning route, audit, glossary, case studies và transition matrix đã có |

## Ranh giới cần giữ

```text
world_history/      = causal comparison xuyên vùng và thời gian
korean_history/     = lịch sử bán đảo Triều Tiên chuyên sâu
world_geography/    = spatial/physical/resource constraints và networks
korean_culture/     = institutions, practices và everyday meanings
investing/economics = market, finance, risk và allocation tools
```

Khi một chapter mới cần mô tả địa hình, không duplicate toàn bộ Geography; khi cần niên đại Hàn Quốc, link sang Korean History; khi cần mô hình kinh tế, giữ phần lịch sử ở đây và trỏ sang Economics.

## Ưu tiên nâng cấp

### P0 — giữ nhất quán

- Mỗi chapter mới phải có ít nhất một causal chain, một boundary/limitation và một transition.
- Dùng cùng vocabulary cho `stock`, `flow`, `capacity`, `extraction`, `legitimacy`, `chokepoint`, `agency`.
- Ghi rõ khi periodization là quy ước phân tích chứ không phải ranh giới tự nhiên.

### P1 — tăng chiều sâu có chọn lọc (đã thực hiện vòng này)

- Đã deepen trực tiếp 14 canonical files, không tạo thêm breadth/chapter timeline.
- Đã làm rõ coal–steam–factory–empire, colonial extraction, debt/borders/mass politics và logistics trong các chapter tương ứng.
- Bước tiếp theo là gắn từng case trong `20_comparative_case_studies.md` với source cụ thể, dataset và tranh luận học thuật; đây là refinement, không phải mở folder mới.

### P2 — mở rộng sau khi P1 ổn định

- Thêm các module theo vùng: West Africa, South Asia, Southeast Asia, Mesoamerica/Andes, East Asia.
- Tạo timeline tra cứu nhanh chỉ sau khi causal chapters đủ sâu.
- Bổ sung bibliography có chú thích ngắn: nguồn sơ cấp, textbook, monograph và dataset.

## Definition of done cho một depth pass

Một chapter chỉ được xem là đã nâng cấp khi có:

1. ít nhất hai scale (local/regional/global) được phân biệt;
2. một bảng hoặc sơ đồ stock/flow;
3. một ví dụ về distribution/winner–loser;
4. một counterfactual có giới hạn;
5. tối thiểu hai loại evidence và ghi rõ uncertainty;
6. link trước–sau và link sang domain liên quan;
7. một đoạn “khi mô hình không áp dụng”.

Depth pass bổ sung thêm một quality sequence bắt buộc cho các chapter canonical:

```text
initial conditions → actors → institutions/material constraints
→ mechanism → event sequence → competing interpretations
→ consequences → long-run path dependence
```
