# Inventory toàn cầu

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Inventory toàn cầu**. Route đi từ chuẩn M49 và coverage theo từng châu lục → country/area entries → tiểu vùng và mã đặc biệt → kiểm tra liên kết, để inventory nối bản đồ hành chính với cấu trúc atlas.

Inventory atlas được chia theo các vùng thống kê M49 để bảo đảm mỗi **country or area** có một vị trí trong hệ thống. Danh sách chi tiết nằm trong README của từng châu lục và tiểu vùng.

## Châu Phi

Xem [Africa inventory](./africa/README.md): Bắc Phi, Đông Phi, Trung Phi, Nam Phi và Tây Phi; bao gồm cả các area có mã riêng như Western Sahara, Mayotte, Réunion, Saint Helena và British Indian Ocean Territory theo M49.

> **Nối mạch:** **Châu Phi** mở inventory bằng các dải Sahara–savanna–rừng và bờ biển; **Châu Mỹ** tiếp theo chuyển sang hai đại dương, Andes và các lưu vực lớn nhưng giữ cùng logic mã hóa. **Châu Á** sau đó mở mạng lục địa–biển có mật độ entry cao hơn.

## Châu Mỹ

Xem [Americas inventory](./americas/README.md): Caribbean, Central America, South America và Northern America. M49 dùng “North America” như một continental grouping rộng hơn gồm Northern America + Caribbean + Central America; vì vậy Mexico nằm trong Central America của M49 dù trong nhiều cách dùng địa lý–văn hóa nó được thảo luận cùng Bắc Mỹ.

> **Nối mạch:** **Châu Mỹ** cho thấy inventory phải giữ cả lục địa, đảo và territory; **Châu Á** tiếp theo dùng cùng schema cho các subregion từ Central Asia tới Southeast Asia. **Châu Âu** sau đó chuyển sang các nhóm nhỏ hơn nhưng không đổi owner logic.

## Châu Á

Xem [Asia inventory](./asia/README.md): Central Asia, Eastern Asia, South-eastern Asia, Southern Asia và Western Asia. Hong Kong SAR và Macao SAR là các area riêng trong inventory M49. Taiwan được xử lý thêm trong `supplemental` theo chính sách (policy / 정책) của atlas.

> **Nối mạch:** **Châu Á** mở rộng quy mô và độ đa dạng của inventory; **Châu Âu** tiếp theo gom các subregion quanh các biển và corridor lục địa. **Châu Đại Dương** sau đó chuyển trọng tâm sang đảo, atoll và khoảng cách biển.

## Châu Âu

Xem [Europe inventory](./europe/README.md): Eastern, Northern, Southern và Western Europe; bao gồm các area như Åland Islands, Faroe Islands, Guernsey, Jersey, Isle of Man, Gibraltar và Svalbard and Jan Mayen.

> **Nối mạch:** **Châu Âu** khép các nhóm lục địa–biển dày entry; **Châu Đại Dương** tiếp theo phải đọc theo khoảng cách, cung đảo và territory. **Nam Cực** sau đó đưa inventory sang một entry không phải quốc gia.

## Châu Đại Dương

Xem [Oceania inventory](./oceania/README.md): Australia and New Zealand, Melanesia, Micronesia và Polynesia. Khu vực này có nhiều đảo/vùng lãnh thổ diện tích đất nhỏ nhưng không gian biển và vai trò mạng lớn.

> **Nối mạch:** **Châu Đại Dương** cho thấy boundary và owner phải xử lý territory đảo; **Nam Cực** tiếp theo áp dụng nguyên tắc đó cho một lục địa nghiên cứu không có quốc gia chủ quyền. **Hồ sơ bổ sung** sau đó giữ các entry cần caveat riêng.

## Nam Cực

Xem [Antarctica](./antarctica/README.md). Antarctica xuất hiện như một area trong M49 nhưng không được xử lý giống một quốc gia; profile tập trung địa lý vật lý, khoa học, logistics và chế độ sử dụng không gian.

> **Nối mạch:** **Hồ sơ bổ sung** khép inventory bằng các trường hợp cần chính sách tên gọi hoặc phân loại riêng; toàn bộ danh mục vẫn quay về owner và source canonical của từng vùng.

## Hồ sơ bổ sung

Folder [supplemental](./supplemental/README.md) dành cho những không gian cần một chapter độc lập để học địa lý nhưng không xuất hiện như country/area chính trong baseline M49. Việc đưa vào đây không phải đánh giá về chủ quyền.

> **Bàn giao:** Sau **Hồ sơ bổ sung**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
