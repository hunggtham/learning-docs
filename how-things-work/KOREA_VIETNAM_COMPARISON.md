# Korea ↔ Vietnam — cùng một chức năng, khác cách tổ chức hệ thống

Tài liệu này là lớp so sánh ngang của `how-things-work/`. Mục tiêu không phải xếp hạng hai nước mà là thấy rằng cùng một nhu cầu — truyền dữ liệu, cấp điện, thanh toán, vận chuyển, đi metro, xử lý rác hay vận hành một tòa nhà — có thể được giải bằng **topology tổ chức (organizational topology / 조직 토폴로지)** khác nhau.

Không nên đọc bảng dưới đây như số liệu thị phần cố định. Đây là bản đồ actor và cơ chế ở snapshot 2026-09-30; khi dùng cho quyết định pháp lý, đầu tư hoặc vận hành phải kiểm tra nguồn chính thức mới nhất.

## 1. Bản đồ so sánh nhanh — 22 hệ thống

| Hệ thống | Hàn Quốc | Việt Nam | Khác biệt đáng học |
|---|---|---|---|
| Internet | Hạ tầng băng rộng mật độ cao, ISP/mobile operators lớn, peering/CDN/data center phát triển sâu | Backbone và access mở rộng nhanh, nhiều tuyến quốc tế/submarine dependency quan trọng, mobile Internet có vai trò lớn | Cùng TCP/IP nhưng topology, international capacity và failure domain khác nhau |
| Electricity grid | KPX vận hành power market + system operation; KEPCO giữ vai trò lớn ở transmission/distribution/retail | NSMO vận hành hệ thống điện và thị trường; EVN cùng các đơn vị thành viên vẫn là actor hạ tầng rất lớn | Tách rõ market operator, grid owner/operator và retailer; không đồng nhất “công ty điện” với toàn hệ thống |
| Water supply | Hệ thống đô thị trưởng thành, nhiều local utilities và K-water ở các lớp phù hợp | Utility theo địa phương, hạ tầng đô thị mở rộng nhanh và chênh lệch vùng đáng kể | Water system mang tính địa phương hơn electricity/telecom |
| Sewage | Coverage/treatment đô thị trưởng thành, resource recovery ngày càng quan trọng | Capacity xử lý tăng nhưng collection/treatment coverage và đô thị hóa tạo pressure lớn | Có sewer pipe chưa có nghĩa toàn bộ wastewater đã được xử lý đến cùng chuẩn |
| Waste/recycling | Source separation, food-waste stream và volume-based fees đã institutionalized lâu | Phân loại tại nguồn và formal treatment đang mở rộng; organic share lớn và landfill vẫn quan trọng ở nhiều nơi | Recycling phụ thuộc cả collection, sorting, treatment và material market; không chỉ hành vi household |
| Construction/buildings | High-rise/apartment stock trưởng thành; focus mạnh vào safety, retrofit, green building và aging assets | High-rise/industrial stock tăng nhanh; challenge là construction quality, utility integration, fire/safety và long-term FM | Hàn thường tối ưu/retrofit mature stock; Việt Nam vừa xây mới nhanh vừa chuẩn hóa vận hành |
| Fuel/oil supply | Import-dependent nhưng có refinery, strategic stockpile và commercial storage/oil-hub infrastructure lớn | Domestic refining + imports + nationwide distribution; policy 2026 tiếp tục chú trọng supply diversification/reserves | Cùng chịu global oil/FX shock nhưng inventory/refining/distribution topology khác nhau |
| Banking | BOK-Wire+ ở lớp large-value final settlement; KFTC vận hành nhiều retail systems | SBV là central-bank layer; NAPAS có vai trò lớn ở switching/clearing retail | UX chuyển khoản tức thời khác với thời điểm interbank obligation được final-settled |
| Card/payment | Card/VAN/PG là topology đặc trưng; card usage trưởng thành | Card + NAPAS + mobile banking + VietQR/account-to-account cùng phát triển mạnh | “Thanh toán QR” và “thanh toán thẻ” có thể giống UX nhưng đi trên payment rail khác nhau |
| Stock market | KRX + KSD/depository infrastructure; standard stock settlement T+2 | HOSE/HNX/VNX structure + VSDC clearing/depository; listed stocks settle T+2 | Matching chỉ là execution layer; post-trade infrastructure mới đưa cash/securities tới final state |
| Shipping | Busan là hub container/transshipment lớn, kết nối manufacturing-export network | Hải Phòng/Lạch Huyện và Cái Mép–Thị Vải là gateway quan trọng, cùng mạng cảng trải dài | Geography làm Vietnam có cấu trúc Bắc–Nam dài; Korea tập trung mạnh quanh industrial/port clusters |
| Postal/parcel | Dense automated parcel/post network, apartment-heavy last mile, mature sorting | E-commerce parcel network mở rộng nhanh; motorbike last mile, COD và long north–south linehaul quan trọng | Parcel flow cần address + tracking + sortation + financial reconciliation; không chỉ “giao hàng” |
| Supermarket | Convenience store, hypermarket và e-commerce integration trưởng thành | Modern trade tăng cùng traditional trade và e-commerce | Retail system phải giải khác nhau về last-mile, store density và payment behavior |
| Public transport | Seoul/metro areas có dense rail + bus network và mature integrated fare/transfer rules | Hà Nội/TP.HCM đang chuyển từ từng tuyến metro sang network với feeder/cashless integration | Korea tối ưu dense network; Vietnam phải build network effect, transfer và first/last-mile đồng thời |
| Road traffic | Mature expressway/ITS + Hi-Pass ecosystem; dense traffic monitoring | Expressway network mở rộng rất nhanh; ETC/ITS rollout đi song hành với new corridors | Korea thiên optimization/maintenance; Vietnam vừa build physical road vừa hoàn thiện digital/control layer |
| Airlines | Network carrier + LCC ecosystem trưởng thành; Korean Air–Asiana đang trong integration plan 2026 | Vietnam Airlines, Vietjet và các hãng khác tạo cấu trúc network/LCC hỗn hợp | Airline economics phụ thuộc fleet, slot, network connectivity và airport constraints hơn chỉ số lượng hãng |
| Airports | Incheon có operator riêng; KAC vận hành phần lớn mạng sân bay còn lại | ACV vận hành phần lớn commercial airport network; Long Thành làm thay đổi topology tương lai | Airport operator ≠ airline ≠ ATC authority |
| GPS/GNSS | Dùng multi-GNSS toàn cầu; KASS cung cấp SBAS augmentation cho use cases phù hợp | Dùng multi-GNSS toàn cầu; geospatial/augmentation infrastructure phát triển theo nhu cầu | Hai nước không cần sở hữu GPS constellation để dùng positioning; receiver phụ thuộc global constellations |
| Satellites | EO/meteorological/research satellite ecosystem và ground/data infrastructure trưởng thành hơn | Domestic program đang tăng, đồng thời dùng mạnh international EO partnerships; LOTUSat là capability-building path | Space value chain là spacecraft + ground + processing + application; owning a satellite chỉ là một phần |
| Mobile networks | SKT, KT, LG U+ tạo 3-MNO structure lớn; 5G deployment trưởng thành | Viettel, VNPT/VinaPhone, MobiFone là MNO chính; 5G rollout đang mở rộng | Spectrum, RAN density, backhaul và core architecture quyết định experience, không chỉ logo “5G” |
| Semiconductors | Global-strength memory manufacturing và supply-chain depth; Samsung/SK hynix là actors lớn | Assembly/test, electronics manufacturing và design capability tăng; national strategy đặt mục tiêu mở rộng sâu hơn | Korea mạnh ở capital-intensive manufacturing; Vietnam đang xây depth qua FDI + domestic capability + workforce |
| Cloud | Global hyperscalers + domestic Naver/KT/NHN ecosystem; CSAP tạo public-sector boundary quan trọng | Global services + Viettel/VNPT/FPT và domestic data centers; sovereign/national data infrastructure tăng | Cloud market chịu ràng buộc bởi power, fiber, compliance và enterprise procurement, không chỉ compute price |

## 2. Pattern 1 — Hàn Quốc thường tối ưu “mật độ/maturity”, Việt Nam thường đồng thời tối ưu “mở rộng/integration”

Seoul metropolitan area có mật độ dân số, fiber, transit, payments, retail và enterprise IT rất cao. Khi infrastructure đã dày, bài toán chuyển từ “có hạ tầng hay chưa” sang **capacity, efficiency, resilience, asset renewal và modernization**.

Việt Nam có hai cực đô thị lớn cùng mạng thành phố/tỉnh trải dài, tốc độ đô thị hóa và nhu cầu digital service tăng nhanh. Vì vậy nhiều hệ thống vừa phải vận hành legacy assets vừa mở mới capacity.

Ví dụ public transport:

```text
Seoul
many interconnected lines + buses
        ↓
frequency / crowding / asset renewal / reliability optimization

Hanoi / HCMC
few operating rail corridors + rapidly expanding plans
        ↓
network build-out + feeder + fare integration + behavior shift
```

Ví dụ road:

```text
Korea
mature expressways
        ↓
ITS optimization + maintenance + congestion management

Vietnam
new expressway corridors
        ↓
physical completion + ETC + ITS + operations standardization
```

Đây là simplification để hình dung, không phải mô tả mọi địa phương.

## 3. Pattern 2 — actor visible nhất chưa chắc vận hành mọi layer

Một lỗi tư duy thường gặp là lấy thương hiệu visible nhất làm đại diện cho toàn system.

```text
Electricity Korea
KPX       → market/system operation
KEPCO     → major network/commercial roles
Generators→ physical generation
Regulator/government → rule/policy

Transport Seoul
city/policy layer
+ multiple rail operators
+ bus operators
+ T-money/fare infrastructure
+ road/traffic management
= one passenger-facing network
```

Tương tự tại Việt Nam:

```text
Electricity
NSMO      → system + market operation
EVN/group entities → major physical/network/commercial roles
Generators → supply
Government/regulator → policy/rules

Metro
city/transport authority
+ line operator
+ bus/feeder operators
+ fare/payment infrastructure
+ construction/project entities
= evolving network
```

Luôn hỏi: **ai sở hữu asset, ai vận hành real-time, ai đặt rule, ai giữ source of truth?** Bốn câu trả lời có thể là bốn tổ chức khác nhau.

## 4. Pattern 3 — digital và physical infrastructure không thể tách

Một cloud app vẫn cần:

```text
power
+ fiber
+ data center
+ spectrum
+ chips
+ cooling
+ physical maintenance
```

Một metro “physical” lại cần:

```text
traction power
+ signaling
+ telecom
+ fare/payment
+ cloud/IT
+ road/feeder access
```

Một building cần:

```text
city grid
+ water
+ sewer
+ telecom
+ road access
+ waste collection
```

Vì vậy system classification chỉ giúp học; ngoài đời boundaries luôn giao nhau.

## 5. Pattern 4 — toàn cầu hóa nằm bên trong hệ thống nội địa

- Internet phụ thuộc submarine cable, international transit, DNS/CDN và global cloud.
- Card payments có international schemes bên cạnh domestic rails.
- GNSS dùng GPS/Galileo/BeiDou/GLONASS.
- Fuel phụ thuộc global crude/product shipping, commodity prices và FX.
- Airlines phụ thuộc aircraft/engine OEM và global aviation rules.
- Semiconductor chain nối EDA/IP, tools, materials, fab, memory, packaging và electronics assembly ở nhiều nước.
- Container shipping nối domestic ports với carrier network toàn cầu.
- Satellite applications có thể dùng data-sharing quốc tế trước cả khi domestic spacecraft capability trưởng thành.

Do đó “thị trường Hàn” hay “thị trường Việt” thường là một node trong global system, không phải closed system.

## 6. Pattern 5 — bottleneck map quan trọng hơn asset count

```text
More power generation
!= enough electricity
if transmission is constrained

More metro kilometers
!= useful network
if transfers/feeder/frequency are weak

More expressway
!= reliable road system
if ITS/toll/incident response are weak

More recycling bins
!= more recycling
if sorting/material markets are weak

More refinery capacity
!= fuel security
if crude/shipping/storage/distribution are constrained

More cloud servers
!= more AI capacity
if GPU/power/cooling/network are constrained
```

So sánh Korea ↔ Vietnam tốt nhất ở **bottleneck map**, không chỉ số lượng asset.

## 7. Pattern 6 — buffer làm failure khác nhau về thời gian

Korea và Vietnam đều dùng buffer nhưng ở topology khác nhau:

- strategic/commercial fuel inventory;
- building water tanks;
- UPS/generators;
- cloud redundancy;
- road/transit alternate routes;
- warehouse/parcels backlog capacity.

Một upstream failure có thể chưa lập tức lộ ra vì downstream còn buffer. Khi buffer cạn, nhiều user có thể bị ảnh hưởng cùng lúc.

## 8. Template so sánh cho chapter tương lai

| Trục | Câu hỏi |
|---|---|
| User entrypoint | Người dùng chạm system ở đâu? |
| Physical layer | Asset thật nằm ở đâu? |
| Operator | Ai vận hành real-time? |
| Market layer | Ai mua/bán và price hình thành thế nào? |
| Rule/regulation | Ai định chuẩn/rule? |
| Settlement/source of truth | Khi nào state được coi là final? |
| Buffer | Inventory/redundancy nào trì hoãn failure? |
| Bottleneck | Constraint hiện tại là gì? |
| Failure propagation | Lỗi có lan sang system khác không? |
| Korea topology | Actor và topology chính ở Hàn? |
| Vietnam topology | Actor và topology chính ở Việt Nam? |
| Global dependency | Layer nào nằm ngoài hai nước? |

## Đọc tiếp

Đọc [`SYSTEM_MAP.md`](./SYSTEM_MAP.md) để xem dependency giữa 22 hệ thống, sau đó đọc [`case-studies/`](./case-studies/README.md) để thấy chúng tương tác trong tình huống cụ thể.

Các nguồn chính thức chuyên ngành được đặt ở cuối từng chapter; ưu tiên chapter tương ứng khi cần kiểm tra claim time-sensitive.
