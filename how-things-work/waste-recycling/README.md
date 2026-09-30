# Waste & Recycling — rác đi đâu sau khi rời khỏi nhà?

Bỏ rác vào thùng chỉ là lúc người dùng rời khỏi hệ thống. Từ đó bắt đầu một chuỗi collection → transfer → sorting → treatment → recycling/incineration/landfill. Chất lượng của hệ thống không chỉ phụ thuộc “người dân có phân loại hay không”, mà còn phụ thuộc route collection, contamination, sorting technology, thị trường vật liệu tái chế và khả năng xử lý phần residual.

## 1. Waste không phải một loại vật chất duy nhất

Household waste thường cần tách tối thiểu theo function:

```text
food / organic waste
recyclables
  ├─ paper
  ├─ glass
  ├─ metals
  └─ plastics
residual mixed waste
bulky waste
hazardous / special waste
```

Mỗi stream có downstream khác nhau. Trộn sai làm giảm recovery và tăng chi phí.

## 2. Flow end-to-end

```text
household / business
      ↓ source separation
collection vehicle
      ↓
transfer station / direct haul
      ↓
sorting / treatment facility
      ↓
├─ recyclable material → reprocessor → manufacturing
├─ organics → compost / feed / anaerobic digestion / other treatment
├─ combustible residual → incineration / energy recovery
└─ residual ash/nonrecoverable → landfill
```

Một city không thể “recycle 100%” chỉ bằng sorting. Recycling cần buyer/process technology và material quality đủ cao.

## 3. Source separation tại sao quan trọng?

Nếu food waste dính vào paper/plastic, contamination tăng. Nếu glass vỡ trộn với film plastic, sorting khó hơn.

```text
better separation at source
        ↓
cleaner material stream
        ↓
lower sorting loss
        ↓
higher-value recycling output
```

Nhưng nếu rule quá phức tạp, compliance có thể giảm. System design phải cân bằng precision và usability.

## 4. Collection là routing problem

Waste trucks có capacity hữu hạn. Operator phải tối ưu:

- collection frequency;
- vehicle route;
- bin capacity;
- narrow streets / apartment loading areas;
- worker safety;
- odor/leakage constraints;
- transfer distance.

```text
many small collection points
        ↓
truck route
        ↓
transfer station
        ↓ larger haul
regional treatment facility
```

Transfer station tồn tại vì không hiệu quả nếu mọi collection truck phải chạy xa tới landfill/incinerator.

## 5. Material Recovery Facility hoạt động thế nào?

**Cơ sở phân loại vật liệu tái chế (Material Recovery Facility, MRF / 재활용 선별시설)** có thể kết hợp:

```text
bag opening / screening
        ↓
size separation
        ↓
magnet → ferrous metal
        ↓
eddy current → aluminum/non-ferrous
        ↓
optical/NIR sorting → plastic types
        ↓
manual quality control
        ↓
baling
```

Output là bale/material fraction, không phải ngay lập tức thành chai mới. Nó còn phải đi tới reprocessor.

## 6. Recycling economics: “có thể tái chế” khác “được tái chế”

Material technically recyclable nhưng economics có thể xấu nếu:

- collection cost cao;
- contamination lớn;
- polymer/material mix khó tách;
- virgin material rẻ;
- buyer ở xa;
- quality output thấp.

Do đó policy có thể dùng deposit, producer responsibility hoặc mandated separation để thay incentive.

## 7. Food waste là một system riêng

Food waste có độ ẩm cao nên landfill/incineration behavior khác dry waste. Nó có thể được:

- xử lý thành feed/compost tùy quality/rules;
- anaerobic digestion tạo biogas;
- dewatered và xử lý theo route khác.

Điểm quan trọng là **organic contamination**. Một chiếc túi nhựa, kim loại hoặc hóa chất lẫn vào food stream có thể làm downstream khó hơn.

## 8. Hàn Quốc: source separation và food-waste stream rất rõ

Hàn Quốc có lịch sử lâu về volume-based waste fees và phân loại riêng food waste/recyclables. Ở nhiều apartment complexes, resident phải bỏ từng stream tại collection area; food-waste systems có thể dùng dedicated bins/RFID-based charging tùy địa phương.

Ministry of Environment statistics cho thấy food waste vẫn là một stream lớn nhưng được theo dõi riêng với recyclable resources và volume-based general waste. Đây là dấu hiệu institutional: waste được quản lý theo material stream chứ không chỉ “một xe rác”.

```text
household
├─ recyclables → separated collection
├─ food waste → dedicated treatment stream
└─ volume-rate bag residual → incineration / disposal stream
```

Incineration và energy recovery có vai trò lớn hơn tại vùng đô thị dày đặc nơi land scarcity cao.

## 9. Việt Nam: collection đang chuyển dần từ mixed waste sang source separation

Việt Nam vẫn có tỷ lệ organic/food waste cao trong municipal solid waste. Năm 2026, các chương trình môi trường tiếp tục nhấn mạnh phân loại tại nguồn, giảm food waste và tăng recycling/circular economy.

Challenge lớn không chỉ là ban hành rule, mà là giữ stream đã phân loại **không bị trộn lại downstream**. Nếu household tách ba nhóm nhưng collection vehicle/facility lại nhập chung, incentive của người dân sẽ mất.

```text
source separation rule
        ↓
separate collection logistics
        ↓
separate treatment capacity
        ↓
recycling/organic markets
```

Bốn lớp phải phát triển cùng nhau.

## 10. Korea ↔ Vietnam

| Lớp | Hàn Quốc | Việt Nam |
|---|---|---|
| Household separation | Mature, detailed streams common | Đang mở rộng/chuẩn hóa separation at source |
| Food waste | Dedicated collection/treatment widely institutionalized | Organic share lớn; dedicated treatment capacity đang mở rộng |
| Urban disposal | Incineration/recovery important due land constraints | Landfill vẫn quan trọng ở nhiều nơi; treatment mix đang thay đổi |
| Recycling | Formal collection/sorting + producer systems mature | Formal + informal recovery coexist; formalization/infrastructure expanding |
| Core challenge | contamination, disposal capacity, circularity | collection consistency, treatment capacity, landfill dependence, market infrastructure |

Không nên hiểu “informal recycling” chỉ là kém phát triển. Informal collectors có thể recover material rất hiệu quả về market incentive, nhưng system-level traceability, worker safety và treatment of low-value residuals vẫn là vấn đề khác.

## 11. Incineration và waste-to-energy

Incinerator giảm waste volume và có thể recover heat/electricity, nhưng không làm vật chất biến mất.

```text
waste
 ↓ combustion
heat → steam → electricity/heat
 ↓
flue gas treatment
 ↓
bottom ash + fly ash
 ↓
further treatment / disposal / recovery
```

Air pollution control là subsystem quan trọng. Ash vẫn cần xử lý; hazardous fly ash không thể coi như ordinary soil.

## 12. Landfill là engineered system

Sanitary landfill cần:

- liner;
- leachate collection;
- gas collection;
- daily cover;
- drainage;
- groundwater monitoring.

```text
waste body
├─ landfill gas → capture / flare / energy
└─ leachate → collection → wastewater treatment
```

Vì vậy landfill nối trực tiếp với [water/sewage](../sewage/README.md).

## 13. Extended Producer Responsibility

**Trách nhiệm mở rộng của nhà sản xuất (Extended Producer Responsibility, EPR / 생산자책임재활용제도)** chuyển một phần cost/end-of-life responsibility về producer/importer.

Economic logic:

```text
producer chooses packaging/material
          ↓
producer faces end-of-life obligation/cost
          ↓
incentive to improve recyclability / collection funding
```

Implementation details khác theo quốc gia và loại product; phần này chỉ giữ mechanism.

## 14. Failure propagation

### Collection strike / fleet failure
Waste tích ở source → odor/pest/public-space problem.

### Incinerator outage
Residual stream phải chuyển sang facility khác/landfill → transport distance/cost tăng.

### Recycling market collapse
Bales không có buyer → inventory tại MRF tăng → material có thể bị downgraded/disposed.

### Heavy rain/flood
Open dumps/poorly controlled sites có thể gây leachate/runoff vào water system.

### Electricity outage
Conveyors, compactors, treatment plants và wastewater subsystems chịu ảnh hưởng.

## 15. Finality trong waste system

“Truck đã lấy rác” chưa phải final state.

```text
collected
  ↓
accepted at facility
  ↓
sorted / treated
  ↓
material sold/reprocessed OR residual disposed
  ↓
final environmental containment / product substitution
```

Recycling claim chỉ có ý nghĩa mạnh khi material thật sự trở thành feedstock cho production, không chỉ khi nó được bỏ vào recycling bin.

## Đọc tiếp

- [Sewage](../sewage/README.md): leachate/wastewater boundary.
- [Electricity grid](../electricity-grid/README.md): waste-to-energy và plant resilience.
- [Shipping logistics](../shipping-logistics/README.md): recovered material movement.
- [Supermarkets](../supermarkets/README.md): packaging và food waste upstream.

Mental model:

```text
Waste management
= source separation
+ collection routing
+ transfer
+ sorting
+ treatment
+ material market
+ residual disposal
```

## Nguồn chính thức tham chiếu

- Korea Ministry of Environment — National Waste Statistical Survey / waste policy: https://me.go.kr/eng/
- Vietnam Government / Ministry of Agriculture and Environment — municipal solid-waste and food-waste policy updates: https://baochinhphu.vn/ ; https://mae.gov.vn/
