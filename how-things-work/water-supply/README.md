# Water Supply — nước máy được tạo và phân phối như thế nào?

Mở vòi nước trông đơn giản hơn bật Internet, nhưng phía sau cũng là một hệ thống mạng. Khác Internet, thứ đi trong mạng là khối lượng nước có trọng lượng, chịu áp lực, bị rò rỉ và có thể suy giảm chất lượng nếu residence time quá dài hoặc đường ống gặp sự cố.

## 1. Từ nguồn nước tới căn hộ

Một hệ thống cấp nước đô thị điển hình:

```text
River / reservoir / groundwater
        ↓
Intake
        ↓
Coagulation + flocculation
        ↓
Sedimentation
        ↓
Filtration
        ↓
Disinfection / advanced treatment
        ↓
Clear-water reservoir
        ↓
Pumping + distribution reservoir
        ↓
Transmission mains
        ↓
Distribution pipes
        ↓
Building tank / booster pump
        ↓
Meter → tap
```

Keo tụ và tạo bông (coagulation/flocculation / 응집) làm các hạt nhỏ kết lại để có thể lắng; bể lắng loại phần lớn cặn; lọc giữ phần hạt còn lại; khử trùng (disinfection / 소독) giảm rủi ro vi sinh. Hệ thống hiện đại có thể thêm ozone, than hoạt tính hoặc màng tùy chất lượng nguồn nước.

Điều khó không kết thúc ở nhà máy. Nước sau xử lý phải đi qua hàng chục đến hàng trăm kilomet ống với áp lực đủ nhưng không quá cao, tránh contamination, kiểm soát leak và duy trì residual disinfectant phù hợp.

## 2. Hàn Quốc: ví dụ Seoul Arisu

Seoul Water công bố chuỗi xử lý Arisu gồm intake từ Han River, receiving well, mixing, flocculation, sedimentation, filtration, ozone, granular activated carbon, clean-water reservoir và distribution reservoir. Đây là ví dụ tốt để thấy xử lý nước không chỉ là “lọc rồi cho chlorine”.

Ở quy mô quốc gia, Hàn Quốc có K-water và nhiều đơn vị cấp nước địa phương. Cấu trúc vì vậy không phải một công ty duy nhất bán nước cho cả nước: nguồn nước lớn, đập, hệ thống vùng và utility đô thị có thể do các tổ chức khác nhau sở hữu hoặc vận hành.

## 3. Việt Nam: hệ thống theo địa phương và vùng cấp nước

Việt Nam cũng tổ chức cấp nước qua các đơn vị cấp nước theo tỉnh/thành và khu vực, dưới khung pháp lý quốc gia. Văn bản hợp nhất 51/VBHN-BXD năm 2026 tiếp tục điều chỉnh sản xuất, cung cấp và tiêu thụ nước sạch. Khác biệt thực tế lớn nằm ở tốc độ đô thị hóa, độ đồng đều của mạng ống và mức thất thoát nước giữa các địa phương.

Một thành phố có nhà máy xử lý tốt vẫn có thể gặp vấn đề nếu mạng cũ rò rỉ, áp lực không ổn định, nguồn nước bị ô nhiễm hoặc dự phòng nguồn kém. Vì vậy chất lượng utility phải nhìn cả **source → treatment → network → building**.

## 4. Hàn Quốc ↔ Việt Nam: cùng cơ chế, khác bài toán vận hành

| Lớp | Hàn Quốc | Việt Nam |
|---|---|---|
| Nguồn | Nhiều hệ thống sông/hồ và hạ tầng vùng đã đầu tư lâu dài | Nguồn mặt và nước ngầm tùy vùng; đô thị hóa làm nhu cầu và áp lực nguồn thay đổi nhanh |
| Treatment | Advanced treatment phổ biến tại các đô thị lớn; monitoring dày | Công nghệ đa dạng theo utility; các đô thị lớn có nhà máy quy mô lớn, nhưng mức đồng đều giữa địa phương khác nhau |
| Distribution | Mạng đô thị trưởng thành, quản trị áp lực và chất lượng chi tiết | Mở rộng nhanh; non-revenue water và mạng cũ là bài toán quan trọng ở nhiều nơi |
| Governance | K-water + local utilities | Khung quốc gia + utility/đơn vị cấp nước địa phương |

## 5. Tại sao vẫn có bồn nước trên mái?

Nếu utility cung cấp áp lực trực tiếp ổn định, nước có thể tới từng tầng qua hệ thống booster. Nhưng nhiều tòa nhà dùng bể ngầm, bể mái hoặc booster pump để tách biến động của mạng công cộng khỏi nhu cầu nội bộ. Điều này tạo thêm một boundary: utility có thể giao nước đạt chuẩn tới đồng hồ, nhưng chất lượng tại vòi còn phụ thuộc vệ sinh bể và plumbing của tòa nhà.

## 6. Hai chỉ số dễ bị bỏ qua

**Thất thoát nước (non-revenue water, NRW / 무수수량)** là phần nước đã sản xuất nhưng không tạo doanh thu vì rò rỉ, sai số meter hoặc thất thoát thương mại. **Áp lực mạng (network pressure / 관망 압력)** quá thấp gây thiếu nước; quá cao tăng leak và burst. Do đó utility không chỉ tối đa hóa lượng nước sản xuất mà phải tối ưu toàn mạng.

Chapter tiếp theo [sewage](../sewage/README.md) bắt đầu đúng tại điểm nước rời khỏi vòi và trở thành nước thải.

## Nguồn chính thức tham chiếu

- Seoul Water — Arisu Production and Supply: https://arisu.seoul.go.kr/eng/sub?menukey=8006
- Chính phủ Việt Nam — Văn bản hợp nhất 51/VBHN-BXD (2026) về sản xuất, cung cấp và tiêu thụ nước sạch: https://chinhphu.vn/?docid=218531&pageid=27160
