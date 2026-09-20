# Knowledge Library — Địa lý thế giới

Bộ tài liệu này được tổ chức theo **khái niệm (concept) → kiến thức phụ thuộc (dependency) → mối quan hệ (relationship)**, không chia theo các mức cơ bản–trung cấp–nâng cao (Beginner/Intermediate/Advanced). Mục tiêu là học Địa lý như một hệ thống giải thích **vì sao thế giới có hình dạng, khí hậu, dân cư, thành phố, biên giới, mạng lưới kinh tế và các vùng địa lý như hiện nay**, thay vì ghi nhớ danh sách địa danh.

> **Mô hình tư duy (mental model) trung tâm:** Địa lý nghiên cứu *vị trí* (where), *phân bố* (distribution), *quan hệ không gian* (spatial relationship), *quá trình* (process) và *quy mô* (scale). Một hiện tượng chỉ thật sự được hiểu khi ta biết nó xảy ra ở đâu, vì sao ở đó, lan truyền theo cơ chế nào và thay đổi thế nào khi đổi quy mô phân tích.

## Cách dùng thư viện

Nên đọc `00_foundations` trước để hiểu tư duy không gian, hệ tọa độ, bản đồ và dữ liệu địa lý. Sau đó có thể đi sang `01_physical_geography` để hiểu nền tảng vật lý của Trái Đất, hoặc `02_human_geography` để hiểu dân số, đô thị, kinh tế và chính trị. `03_regions` dùng các nguyên lý trước đó để đọc từng vùng của thế giới. `04_global_systems` tập trung vào các hệ thống xuyên biên giới. `90_connections` nối Địa lý với Toán học, thống kê (statistics), công nghệ thông tin (IT), GIS, dữ liệu (Data), kinh tế học và các mô hình tư duy tổng hợp.

Quy ước liên kết chéo dùng đường dẫn Markdown tương đối, ví dụ: [Bản đồ và phép chiếu](./00_foundations/03_cartography_projections_scale.md).

## Sơ đồ quan hệ kiến thức

```mermaid
graph TD
  A[Tư duy địa lý] --> B[Trái Đất như một hệ thống]
  A --> C[Tọa độ và thời gian]
  C --> D[Bản đồ và phép chiếu]
  D --> E[GIS và viễn thám]
  B --> F[Kiến tạo mảng]
  B --> G[Khí quyển và khí hậu]
  B --> H[Thủy văn và đại dương]
  F --> I[Địa mạo]
  G --> J[Quần xã và hệ sinh thái]
  H --> J
  A --> K[Dân số và di cư]
  K --> L[Đô thị hóa]
  A --> M[Địa lý chính trị và kinh tế]
  F --> N[Địa lý vùng]
  G --> N
  M --> N
  N --> O[Các hệ thống toàn cầu]
  E --> P[Địa lý + IT/Data]
```

## Cấu trúc

```text
world_geography/
├── 00_foundations/
├── 01_physical_geography/
├── 02_human_geography/
├── 03_regions/
├── 04_global_systems/
└── 90_connections/
```

Bộ tài liệu ưu tiên kiến thức tương đối bền vững. Với số liệu dân số, GDP, khí hậu cực trị hoặc biên giới đang tranh chấp, hãy coi số cụ thể là dữ liệu theo thời điểm và kiểm tra nguồn cập nhật khi cần ra quyết định thực tế.
