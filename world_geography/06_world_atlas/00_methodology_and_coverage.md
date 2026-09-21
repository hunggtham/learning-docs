# Phương pháp, tên gọi và phạm vi của World Atlas

## Inventory và learning profile là hai bài toán khác nhau

Cụm “mọi quốc gia và vùng lãnh thổ” có nhiều lớp thống kê và pháp lý. Để inventory không tùy ý, project dùng **UN M49** làm baseline cho danh mục `countries or areas`, với ISO 3166 làm tham chiếu bổ trợ khi phù hợp.

Việc một entry nằm trong inventory không buộc phải có một chapter riêng. Inventory giải quyết **completeness của danh sách**; learning profile giải quyết **giá trị giáo dục**.

## Cấu trúc file không phải tuyên bố chủ quyền

Nếu một không gian được phân tích riêng, điều đó chỉ có nghĩa nó hữu ích cho địa lý. Folder, tên file và mã không được dùng như kết luận về chủ quyền, tính chính danh hoặc đường biên.

Với khu vực có cách phân loại khác nhau giữa hệ thống quốc tế, profile phải ghi provenance và tách: hệ phân loại thống kê, tình trạng/quan điểm theo nguồn và cấu trúc địa lý đang phân tích. Không suy ý định chính trị từ bản đồ.

## Không tạo stub để chạy coverage

Một template có vài câu không phải profile. Từ audit này, quy tắc là:

- không auto-generate country files từ inventory;
- không đánh dấu completed chỉ vì file tồn tại;
- không dùng số line/heading như metric chất lượng;
- không copy cùng một đoạn cho hàng chục country rồi đổi tên;
- nếu case không có đủ giá trị độc lập, gộp vào regional/comparative chapter.

Các stub legacy từ batch trước chỉ là transitional reference và sẽ được promote/merge/remove khi Atlas được cleanup.

## Bốn trạng thái nội dung

**Inventory only:** chỉ có entry trong danh mục.

**Reference:** có ghi chú ngắn để định vị nhưng chưa đủ làm bài học.

**Learning profile:** có causal chain hoàn chỉnh, misconception, mental model và cross-link.

**Deep comparative profile:** ngoài learning profile còn so sánh cơ chế với nơi khác, giải thích network dependency và nối nhiều domain core.

Chỉ hai trạng thái cuối được tính vào educational coverage.

## Profile phải có thesis, không chỉ template

Mỗi profile nên trả lời một câu thesis, ví dụ: “địa lý của nơi này được tổ chức bởi một megadelta + export corridor + monsoon regime” hoặc “mountain water tower + landlocked trade dependence”.

Các section sau phải chứng minh thesis. Nếu heading đầy đủ nhưng nội dung chỉ lặp fact, profile vẫn chưa đạt.

## Nội dung bền vững và dữ liệu theo thời điểm

Ưu tiên vị trí, relief, basin, climate regime, population pattern, urban hierarchy, production belt, port/corridor và hazard mechanism.

Population/GDP/trade share, current government, ranking và event thay đổi nhanh chỉ thêm khi phục vụ một luận điểm, phải ghi năm và source. Không biến profile thành snapshot dễ lỗi thời.

## Political geography và boundary provenance

M49 là hệ thống thống kê; việc dùng M49 không đồng nghĩa Atlas tự đưa ra phán quyết pháp lý. Khi cần mô tả boundary hoặc maritime claim, phải dùng nguồn có thẩm quyền phù hợp, ghi thời điểm và thể hiện bất định/tranh chấp bằng wording trung tính.

Bản đồ boundary cũng là data product: cần biết source, version và rule biểu diễn.

## Tên file và mã

Nếu có ISO alpha-3, file có thể dùng dạng `KOR_republic_of_korea.md`, `VNM_viet_nam.md`. Mã giúp link ổn định hơn tên hiển thị, nhưng mã không phải bản chất địa lý của territory.

## Profile priority

Thứ tự ưu tiên không dựa trên diện tích hoặc “quan trọng hơn” theo giá trị chính trị. Nó dựa trên **learning leverage**: nơi nào giúp hiểu nhiều concept, có liên hệ Korea–Vietnam hoặc có vai trò rõ trong economy/history/network geography thì được làm sâu trước.

Nhóm đầu gồm East Asia, Southeast Asia, major global economies, chokepoint/corridor cases, megadeltas, landlocked states, city-states, archipelagos và resource-system cases.

## Definition of Done

Một profile chỉ được gắn `Learning profile` khi người đọc có thể trả lời:

- physical structure tạo constraint/opportunity gì;
- climate/water được tạo bởi cơ chế nào;
- population/urban pattern vì sao nằm ở đó;
- production và network có hình dạng nào;
- external dependency và chokepoint nào quan trọng;
- hazard biến thành risk qua exposure/vulnerability ra sao;
- claim nào chỉ là model hoặc có limitation;
- profile nối với prerequisite core files nào.

Nếu chưa trả lời được, nó vẫn là reference, không phải completed content.