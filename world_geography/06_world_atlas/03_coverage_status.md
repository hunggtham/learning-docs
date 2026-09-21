# Coverage Status — World Atlas

## Coverage phải tách inventory khỏi learning content

Atlas hiện có **inventory rộng** dựa trên UN M49 và nhiều file country/area được tạo trong các batch trước. Từ audit này, sự tồn tại của một file **không còn được tính là nội dung hoàn thành**.

Có ba lớp coverage khác nhau:

**Inventory coverage** nghĩa tên/mã country-or-area đã có trong index để không bỏ sót không gian thống kê. Lớp này có thể hoàn chỉnh mà không cần tạo hàng trăm chapter.

**Reference stub** là file ngắn giúp định vị hoặc ghi mental model sơ bộ. Nó không phải learning chapter và không được tính vào completion metric.

**Learning profile** là chapter có causal chain đầy đủ: physical base → climate/water → population/urban → economy → networks → hazards/constraints → misconceptions → mental model → cross-links. Chỉ lớp này mới được tính là nội dung Atlas hoàn chỉnh.

## Trạng thái hiện tại

**Inventory coverage:** rộng và về cơ bản đã bao phủ Africa, Americas, Asia, Europe, Oceania và Antarctica theo baseline M49 đã dùng trong project.

**Learning-profile coverage:** **chưa hoàn chỉnh toàn cầu**. Một số profile lớn đã được depth-pass, đặc biệt nhóm Africa trong các commit gần đây; nhiều file Asia/Europe/Americas/Oceania vẫn ở mức compact hoặc reference-only và phải re-audit trước khi được gắn nhãn hoàn chỉnh.

**Legacy short profiles:** còn tồn tại từ giai đoạn chạy coverage. Chúng được xem là transitional reference files, không nằm trong learning route và là ứng viên để **nâng sâu, gộp vào subregion chapter hoặc xóa** khi cleanup Atlas. Không tiếp tục tạo thêm file kiểu này.

## Quy tắc từ thời điểm audit

Không tạo profile mới chỉ để “đủ quốc gia”. Global inventory chịu trách nhiệm completeness của danh sách; profile folder là **curated learning layer**.

Một file template chưa có giải thích cơ chế không được tính là completed. Số heading hoặc số dòng cũng không đủ; mỗi section phải trả lời “vì sao / bằng cơ chế nào / giới hạn gì”.

Nếu một country/territory không có đủ giá trị học độc lập, kiến thức của nó nên nằm trong chapter tiểu vùng hoặc comparative chapter thay vì giữ một skeleton riêng.

## Priority learning profiles

Atlas ưu tiên nơi có giá trị cao đối với route Korea–Vietnam, kinh tế thế giới, lịch sử mạng thương mại và các hệ thống địa lý lớn.

Nhóm Đông Á/Đông Nam Á nên ưu tiên **Republic of Korea, Viet Nam, China, Japan, DPR Korea, Taiwan (supplemental geographic case), Singapore, Indonesia, Malaysia, Thailand và Philippines**.

Nhóm global economy nên ưu tiên **United States, India, Germany, France, United Kingdom, Netherlands, Australia** cùng các case có vai trò lớn trong manufacturing, finance, ports hoặc commodity networks.

Nhóm energy/chokepoint nên chọn profile theo giá trị cơ chế như **Saudi Arabia, Iran, Türkiye, United Arab Emirates, Egypt, Panama** và các corridor/gateway liên quan, nhưng nội dung địa chính trị theo thời điểm phải kiểm tra nguồn cập nhật và giữ wording trung tính.

Các profile Africa đã được depth-pass vẫn được giữ vì chúng cung cấp case tốt về Sahel, Nile, Congo Basin, Great Rift, landlocked corridors, resource belts và urbanization.

## Không dùng Atlas để thay core

Nếu một concept như demographic transition, monsoon, plate tectonics, agglomeration hay chokepoint chưa hiểu, phải quay lại core chapter. Country profile chỉ minh họa sự kết hợp của nhiều cơ chế ở một place cụ thể.

## Definition of Done cho một Learning Profile

Một profile đủ chuẩn khi:

1. Có thesis không gian rõ: “territory này được tổ chức bởi những cấu trúc nào?”.
2. Giải thích physical base và climate/water bằng cơ chế, không chỉ liệt kê núi–sông.
3. Giải thích population/urban pattern bằng accessibility, history và network.
4. Giải thích production zones, corridor và external dependency.
5. Tách hazard, exposure và vulnerability.
6. Có ít nhất một phần misconception/limitation.
7. Có mental model cô đọng nhưng không thay cho phần giải thích.
8. Có relative links về prerequisite core và region chapter.
9. Tránh số liệu nhanh lỗi thời nếu không có năm/nguồn.
10. Có đủ chiều sâu để đọc độc lập; template/skeleton không đạt điều kiện này.

## Cleanup queue

Khi quay lại Atlas, ưu tiên re-audit theo subregion. File reference-only sẽ nhận một trong ba quyết định: **promote** thành learning profile, **merge** vào regional/comparative chapter, hoặc **remove** nếu không tạo giá trị ngoài inventory.

Metric quan trọng từ đây là **số profile có giá trị học và chất lượng cross-link**, không phải tổng số `.md`.