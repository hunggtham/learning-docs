# World Atlas — Quốc gia, vùng lãnh thổ và các không gian địa lý của thế giới

Atlas này không được thiết kế như bảng tra “thủ đô – diện tích – dân số”. Mỗi hồ sơ phải giải thích **vì sao không gian đó có cấu trúc như hiện nay** bằng cách nối địa hình, khí hậu, nước, dân cư, mạng đô thị, kinh tế, giao thông, rủi ro và vị trí khu vực.

Một quốc gia có thể thay đổi chính phủ hoặc số liệu GDP trong vài năm, nhưng nhiều ràng buộc địa lý tồn tại hàng thập kỷ đến hàng triệu năm: không giáp biển, nằm trên cung núi lửa, kiểm soát một eo biển, có đồng bằng châu thổ, phụ thuộc một lưu vực hay có mạng đô thị dọc bờ biển. Atlas ưu tiên những cấu trúc bền vững này.

## Chuẩn coverage

Inventory chính dùng **UN M49 — Standard country or area codes for statistical use**. M49 bao gồm “countries or areas” và chia mỗi mục vào một vùng thống kê. Việc dùng phân loại này nhằm có một baseline nhất quán; nó **không được hiểu là phán quyết của tài liệu về chủ quyền, đường biên hay tính hợp pháp chính trị**.

Bên cạnh M49, atlas có thể tạo **hồ sơ địa lý bổ sung** cho những không gian thường cần phân tích riêng trong bản đồ, thống kê hoặc kinh tế nhưng M49 không tách thành mục chính. Những file như vậy phải ghi rõ lý do tồn tại và hệ phân loại nguồn đang dùng.

Xem chi tiết: [Phương pháp và coverage](./00_methodology_and_coverage.md).

## Cấu trúc

```text
06_world_atlas/
├── 00_methodology_and_coverage.md
├── 01_global_inventory.md
├── 02_profile_template.md
├── africa/
├── americas/
├── asia/
├── europe/
├── oceania/
├── antarctica/
└── supplemental/
```

Các folder châu lục chứa README inventory trước; hồ sơ chi tiết được thêm theo từng tiểu vùng. Khi một profile hoàn thiện, nó phải đủ sâu để người đọc hiểu khu vực mà không cần chỉ dựa vào chapter vùng tổng quát.

## Cách đọc một hồ sơ

Hãy bắt đầu bằng **khung không gian**: giáp đâu, mở ra biển nào, địa hình nào chia cắt bên trong. Sau đó đọc **khung vật lý**: kiến tạo, khí hậu, lưu vực, tài nguyên và hiểm họa. Tiếp theo là **khung con người**: dân cư nằm ở đâu và vì sao, đô thị nào là nút chính, kinh tế bám theo hành lang nào. Cuối cùng đọc **mạng bên ngoài**: cảng, tuyến thương mại, biên giới, phụ thuộc năng lượng–lương thực–nước và rủi ro truyền qua mạng.

Mục tiêu cuối cùng không phải nhớ từng fact, mà có thể nhìn bản đồ trống và suy ra: **“nếu địa hình, khí hậu và vị trí như vậy, những mẫu dân cư–kinh tế nào có khả năng xuất hiện?”**