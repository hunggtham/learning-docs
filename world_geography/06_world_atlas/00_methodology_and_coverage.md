# Phương pháp, tên gọi và phạm vi của World Atlas

## Vì sao cần một chuẩn inventory?

Cụm từ “mọi quốc gia và vùng lãnh thổ” tưởng đơn giản nhưng trong dữ liệu thực tế có nhiều lớp: quốc gia thành viên Liên Hợp Quốc, quốc gia quan sát viên, lãnh thổ phụ thuộc, đặc khu, đảo xa, vùng có mã thống kê riêng và các không gian có tình trạng được mô tả khác nhau giữa hệ thống quốc tế.

Để tránh tự tạo một danh sách tùy ý, atlas dùng **UN M49** làm baseline. M49 được UN Statistics Division duy trì cho mục đích thống kê và liệt kê các “country or area”, kèm mã số M49 và phần lớn có ISO alpha-3. UN nhấn mạnh việc xếp một khu vực vào nhóm thống kê không hàm ý lập trường về tình trạng pháp lý, chính quyền hay ranh giới.

ISO 3166 được dùng bổ trợ vì tiêu chuẩn này định nghĩa mã cho **countries, dependencies and other areas of particular geopolitical interest**. Hai hệ có mục tiêu gần nhau nhưng không hoàn toàn giống nhau.

## Hồ sơ không phải tuyên bố chủ quyền

Folder và tên file chỉ là cấu trúc tri thức. Nếu một vùng được viết thành file riêng, điều đó có nghĩa **nó hữu ích khi phân tích địa lý độc lập**, không có nghĩa atlas tuyên bố nó là quốc gia có chủ quyền.

Ngược lại, nếu M49 gộp một khu vực trong mã thống kê khác, atlas vẫn có thể tạo profile bổ sung nếu cần để hiểu địa hình, dân cư, kinh tế hay mạng lưới của khu vực đó. Phần đầu file phải ghi rõ ngữ cảnh phân loại.

## Trường hợp M49 không tách riêng

UN M49 nêu rõ hai ví dụ thường gặp. Kosovo không xuất hiện như một mục chính trong M49; M49 mô tả nó trong bối cảnh Nghị quyết Hội đồng Bảo an 1244 (1999) và cho biết mã 412 có thể dùng cho mục đích thống kê nghiêm ngặt. Taiwan Province of China cũng không xuất hiện như một mục chính; M49 xem trong mã China 156 nhưng cho biết mã 158 có thể được dùng cho mục đích thống kê nghiêm ngặt.

Atlas vì mục tiêu học địa lý sẽ có thể duy trì profile bổ sung cho các không gian này, với wording trung tính và ghi rõ hệ phân loại. Cách làm tương tự được áp dụng nếu sau này gặp một khu vực có mã thực tế trong datasets nhưng không là mục M49 chính.

## Tên file và mã

Nếu có ISO alpha-3, file ưu tiên dạng:

```text
KOR_republic_of_korea.md
VNM_viet_nam.md
GRL_greenland.md
```

Mã giúp file ổn định ngay cả khi short name thay đổi. Tên hiển thị bên trong chapter dùng tiếng Việt trước, tên tiếng Anh/UN khi cần trong ngoặc.

## Nội dung bền vững và nội dung theo thời điểm

Atlas ưu tiên dữ kiện ít biến động: vị trí, địa hình, lưu vực, khí hậu nền, mô hình dân cư, mạng đô thị, cảng/hành lang và rủi ro tự nhiên. Số liệu dân số, GDP, chính quyền hiện tại, xếp hạng và số liệu thương mại thay đổi nhanh nên chỉ thêm khi có mục đích phân tích rõ, ghi năm và nguồn.

Một profile không nên trở thành “snapshot năm nay” nhanh lỗi thời.

## Chính trị và biên giới

Khi địa lý chính trị cần thiết, tài liệu mô tả **cấu trúc không gian và tình trạng theo nguồn**, không tự suy ý định, tính chính danh hay kết quả tương lai. Với tranh chấp, cần tách ba lớp: kiểm soát thực tế, yêu sách pháp lý/ngoại giao và cách nguồn dữ liệu phân loại.

Bản đồ có thể khác nhau vì dùng nguồn khác; đó là lý do provenance của boundary dataset là một phần của kiến thức GIS.

## Mức hoàn thiện của profile

Một profile được coi là “đã viết” khi có đủ các lớp: khung không gian; địa hình–kiến tạo; khí hậu–nước; sinh thái/tài nguyên khi có ý nghĩa; dân cư–đô thị; kinh tế không gian; mạng giao thông–liên kết; rủi ro; hiểu lầm phổ biến; mental model và cross-link.

Không tạo hàng trăm stub một đoạn chỉ để đủ số file. Inventory có thể hoàn chỉnh trước, nhưng profile phải được phát triển theo batch có chiều sâu.