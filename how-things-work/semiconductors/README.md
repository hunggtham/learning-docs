# Semiconductors — một con chip đi từ ý tưởng tới thiết bị như thế nào?

“Công ty bán dẫn” có thể là công ty thiết kế không có fab, foundry chỉ sản xuất wafer, memory IDM tự thiết kế–sản xuất, equipment supplier hoặc packaging/test house. Nếu gom tất cả thành một ngành duy nhất, ta sẽ không hiểu vì sao Hàn Quốc mạnh ở một số lớp và Việt Nam đang xây năng lực ở những lớp khác.

## 1. Value chain từ specification tới finished chip

```text
System requirement
      ↓
Architecture
      ↓
Logic / circuit design
      ↓
Verification
      ↓
Physical design
      ↓ tape-out
Mask generation
      ↓
Wafer fabrication
      ↓
Wafer test
      ↓
Dicing
      ↓
Packaging / advanced packaging
      ↓
Final test
      ↓
Module / board / device
```

Phía sau flow này còn có EDA software, IP cores, silicon wafers, photoresist, specialty gases, lithography, etch/deposition/metrology equipment và ultra-clean utilities. Một fab không thể hoạt động chỉ với “máy in chip”.

## 2. Fabless, foundry và IDM

**Công ty thiết kế không sở hữu fab (fabless / 팹리스)** tập trung design và outsource manufacturing. **Xưởng đúc bán dẫn (foundry / 파운드리)** sản xuất wafer theo design của customer. **Nhà sản xuất thiết bị tích hợp (Integrated Device Manufacturer, IDM / 종합반도체기업)** sở hữu nhiều phần từ design tới manufacturing.

```text
Fabless: design ─────────────→ foundry → package/test
IDM:     design → own fab → own/partner package/test
```

Business model quyết định capex và risk. Leading-edge fab cần investment khổng lồ và utilization cao; fabless tránh fab capex nhưng phụ thuộc external capacity.

## 3. Wafer fabrication thực sự là lặp hàng trăm bước

Simplified transistor flow:

```text
Silicon wafer
→ oxidation / deposition
→ photoresist coating
→ lithography exposure
→ develop
→ etch / implant
→ strip / clean
→ repeat many times
→ metal interconnect layers
```

**Quang khắc (lithography / 노광)** chuyển pattern từ mask lên photoresist; **khắc (etch / 식각)** loại material chọn lọc; **lắng đọng (deposition / 증착)** thêm lớp vật liệu; **implantation** đưa dopant vào silicon. Modern chips cần rất nhiều cycle với overlay/alignment cực nhỏ.

Yield là biến số kinh tế sống còn. Nếu wafer có 600 dies nhưng chỉ 300 good dies, cost per good die gần gấp đôi so với yield cao hơn, trước cả packaging.

## 4. Memory và logic khác nhau

DRAM/NAND memory tối ưu density, process repeatability và cost/bit. Logic chip như CPU/GPU/mobile SoC tối ưu complex computation và interconnect. Hàn Quốc đặc biệt mạnh ở memory qua Samsung Electronics và SK hynix; Samsung còn tham gia foundry/logic.

AI boom làm High Bandwidth Memory (HBM / 고대역폭메모리) trở nên quan trọng. HBM không đơn giản là “DRAM nhanh hơn”: nhiều memory dies được stack và kết nối bằng TSV/advanced packaging để cung cấp bandwidth rất cao gần accelerator.

## 5. Advanced packaging biến back-end thành strategic layer

Trước đây packaging thường bị coi là bước “đóng vỏ” cuối. Chiplet và AI accelerators khiến packaging trở thành system architecture:

```text
Compute die + HBM stacks + interposer
        ↓
advanced package
        ↓
short high-bandwidth connections
```

Thermal, power delivery, interconnect density và package yield quyết định system performance. Việc Hàn Quốc năm 2026 tiếp tục có chương trình xây hạ tầng advanced packaging phản ánh thay đổi này.

## 6. Hàn Quốc: ecosystem từ memory tới equipment/materials

Hàn Quốc có hai global memory leaders Samsung Electronics và SK hynix, cùng foundry, display/electronics demand, equipment/material suppliers và advanced packaging ecosystem. Semiconductor exports có ảnh hưởng lớn tới industrial cycle và trade của quốc gia.

Điểm mạnh không chỉ là một vài mega-fab. Cluster economics đến từ supplier proximity, engineering labor, utilities, R&D, customers và repeated learning. Một fab mới cần ultrapure water, stable electricity, specialty chemicals, waste treatment và logistics — kết nối trực tiếp với các chapter electricity/water của library.

## 7. Việt Nam: design + assembly/test là base thực tế, fab là mục tiêu dài hơn

Việt Nam đã có semiconductor design activity và significant assembly/packaging/test investment từ các multinational và domestic teams. Chính phủ ban hành Quyết định 1018/QĐ-TTg ngày 21/09/2024 về chiến lược semiconductor tới 2030, tầm nhìn 2050.

Điều quan trọng khi đọc strategy: các con số như “số doanh nghiệp design”, “fab” hoặc packaging plants trong mốc 2030 là **mục tiêu chính sách**, không phải current installed capacity. Không nên biến target thành fact hiện tại.

Với manufacturing ecosystem electronics lớn, Việt Nam có lợi thế để mở rộng OSAT/packaging, test, design services và supplier base. Nhưng wafer fab đòi hỏi capital, water/power quality, technology transfer, equipment access, process know-how và volume economics ở một cấp độ khác.

## 8. Hàn Quốc ↔ Việt Nam

| Value-chain layer | Hàn Quốc | Việt Nam |
|---|---|---|
| Memory | Global-scale leadership | Chủ yếu downstream/use/assembly ecosystem, chưa có memory wafer-fab scale tương đương |
| Logic/foundry | Samsung + fabless ecosystem và suppliers | Design capability tăng; fabless/design centers mở rộng |
| Wafer fab | Large domestic fabrication base | Domestic wafer-fab capability còn hạn chế; strategy đặt mục tiêu phát triển |
| Packaging/test | Mature, advanced packaging ngày càng strategic | Một trong các lớp có existing FDI base và room mở rộng lớn |
| Equipment/material | Deep domestic supplier ecosystem nhưng vẫn phụ thuộc global chain ở critical tools/materials | Emerging supporting industry, phụ thuộc nhập khẩu nhiều equipment/material |
| Talent | Large experienced engineering pool | Talent expansion là policy priority; training pipeline đang được mở rộng |

Đây là so sánh vị trí value chain, không phải bảng xếp hạng “nước nào tốt hơn”. Một layer lower-capex có thể là bước tích lũy process knowledge trước khi đi sâu upstream.

## 9. Vì sao fab cần nhiều nước và điện?

Ultra-pure water làm sạch wafer giữa nhiều process steps; contamination rất nhỏ cũng làm defect. Equipment, cleanroom HVAC, vacuum pumps và chillers dùng lượng điện lớn và cần power quality/reliability cao. Vì vậy semiconductor cluster là khách hàng chiến lược của [electricity grid](../electricity-grid/README.md) và [water supply](../water-supply/README.md).

## 10. Tại sao node “3 nm” không đủ để so chip?

Process-node label ngày nay không phải một kích thước vật lý duy nhất có thể so trực tiếp giữa mọi foundry. Performance phụ thuộc transistor architecture, density, library, power, design, package và workload. Chip ở older node vẫn tối ưu cho analog, power, automotive, RF hoặc cost-sensitive uses.

Do đó “càng nm nhỏ càng tốt” là mental model sai khi áp cho toàn semiconductor market.

## 11. Supply-chain shock lan ra sao?

```text
Fab/tool/material constraint
→ fewer wafers
→ component shortage
→ module shortage
→ electronics/automotive production delay
→ inventory hoarding
→ price distortion
→ later inventory correction
```

Bullwhip effect khiến shortage có thể chuyển thành glut sau khi mọi tầng cùng over-order. Đây là lý do semiconductor cycle vừa mang tính technology vừa mang tính inventory/finance.

Mental model:

```text
Chip value
= architecture
+ design
+ process
+ yield
+ package
+ software ecosystem
+ supply-chain execution
```

[`../../investing/`](../../investing/README.md) sở hữu company/cycle analysis; chapter này chỉ xây manufacturing mental model. Đọc [cloud-computing](../cloud-computing/README.md) để thấy chips được gom thành data-center compute, và [mobile-networks](../mobile-networks/README.md) cho modem/RF/base-station demand.

## Nguồn chính thức tham chiếu

- Korea Ministry of Trade, Industry and Energy — 2026 advanced semiconductor packaging infrastructure program: https://motie.go.kr/kor/article/ATCLc01b2801b/70880/view
- Government of Vietnam — Decision 1018/QĐ-TTg Semiconductor Strategy: https://vanban.chinhphu.vn/?docid=211240&pageid=27160
- SEMI — semiconductor manufacturing ecosystem: https://www.semi.org/
