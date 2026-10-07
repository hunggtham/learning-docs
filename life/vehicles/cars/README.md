# Cars Knowledge Library — Hiểu xe hơi như một hệ thống

> **Mạch đọc:** [Life README](../../README.md) đặt Cars trong nhánh đời sống theo cơ chế. Route đi từ bài toán chuyển động và năng lượng → power unit → truyền mô-men, lốp và mặt đường → steering/suspension/brakes/body → thông số, bảo dưỡng và tổng chi phí sở hữu, để tên gọi xe được đọc như kết quả của kiến trúc chứ không phải danh sách model.

Lộ trình hiện tại:

1. [`00_powertrain_motion_foundations.md`](00_powertrain_motion_foundations.md) — năng lượng, mô-men, lực tại lốp và giới hạn chuyển động.
2. [`01_ice_ev_hybrid_and_thermal.md`](01_ice_ev_hybrid_and_thermal.md) — ICE, EV, hybrid và giới hạn nhiệt.
3. [`02_transmission_tires_safety_and_ownership.md`](02_transmission_tires_safety_and_ownership.md) — transmission, lốp, safety và TCO.
4. [`03_vehicle_specification_case_lab.md`](03_vehicle_specification_case_lab.md) — case lab đọc specification khi chọn xe cho một profile sử dụng.

Xe hơi dễ bị học ngược: người ta biết tên hãng, model, mã động cơ hoặc horsepower trước khi hiểu chiếc xe phải giải quyết những bài toán vật lý nào. Nhánh này đi theo chiều ngược lại: bắt đầu từ **lực cần để xe chuyển động**, nguồn năng lượng tạo lực đó và con đường truyền lực tới mặt đường.

## 1. Một chiếc xe phải làm được những gì?

Ở mức cơ bản, xe phải lưu trữ hoặc nhận năng lượng, biến năng lượng thành chuyển động, truyền lực tới bánh xe, thay đổi hướng, giảm tốc, hấp thụ dao động từ mặt đường và bảo vệ người/người dùng cùng hàng hóa. Vì thế một chiếc xe có thể được nhìn thành nhiều hệ thống liên kết:

```text
Energy source
    ↓
Power unit
    ↓
Drivetrain
    ↓
Wheels / tires
    ↓
Road

Song song:
steering + suspension + brakes + chassis/body + electronics + thermal management
```

Cách nhìn này giúp tránh nhầm giữa các thuật ngữ thường được đặt cạnh nhau nhưng thực ra trả lời câu hỏi khác nhau.

Từ sơ đồ đó, câu hỏi đầu tiên cần tách là nguồn năng lượng và cách nó biến thành mô-men; chỉ sau khi có lớp này mới nên so horsepower, kiểu thân xe hay tên hệ truyền động.

## 2. ICE, Hybrid, PHEV và EV khác nhau ở đâu?

Xe động cơ đốt trong (internal combustion engine vehicle, ICE / 내연기관 자동차) lưu năng lượng chủ yếu dưới dạng nhiên liệu hóa học. Động cơ đốt nhiên liệu, tạo chuyển động quay rồi hệ truyền động đưa mô-men tới bánh xe.

Xe điện chạy pin (battery electric vehicle, BEV / 배터리 전기자동차) lưu năng lượng trong pin và dùng động cơ điện để tạo mô-men. Nó không chỉ là “xe xăng bỏ động cơ rồi gắn motor”: đặc tính của motor điện, pin, inverter, quản lý nhiệt và khả năng tái tạo năng lượng khi giảm tốc làm kiến trúc vận hành khác đáng kể.

Xe lai (hybrid electric vehicle, HEV / 하이브리드 자동차) kết hợp động cơ đốt trong với hệ điện để phân chia công việc theo điều kiện vận hành. Xe lai sạc ngoài (plug-in hybrid electric vehicle, PHEV / 플러그인 하이브리드 자동차) bổ sung khả năng nạp điện từ nguồn ngoài và thường có khả năng chạy điện đáng kể hơn HEV thông thường.

Điểm cần giữ lại không phải bốn chữ viết tắt mà là câu hỏi: **năng lượng nằm ở đâu, thiết bị nào biến nó thành mô-men và hệ thống quyết định dùng nguồn nào khi xe vận hành?**

> **Chuyển mạch:** Kiến trúc nguồn năng lượng cho biết xe tạo mô-men ra sao; để hiểu cảm giác vận hành, cần tách mô-men khỏi công suất và xem chúng thay đổi thế nào theo vòng tua.

## 3. Horsepower và torque không phải hai cách nói cùng một thứ

Mô-men xoắn (torque / 토크) mô tả xu hướng của lực làm vật quay. Công suất (power / 출력) mô tả tốc độ thực hiện công. Trong hệ quay, công suất liên hệ với mô-men và tốc độ quay; vì vậy nói một động cơ có mô-men lớn nhưng không xét vùng vòng tua chưa đủ để suy ra toàn bộ khả năng tăng tốc.

Mã lực (horsepower / 마력) là một đơn vị thường dùng để biểu diễn công suất. Nó không phải một “lực kéo” độc lập nằm trong động cơ.

Hộp số còn thay đổi quan hệ giữa tốc độ quay và mô-men truyền tới bánh xe. Do đó muốn hiểu cảm giác tăng tốc phải nhìn cả đường cong công suất/mô-men, tỷ số truyền, khối lượng xe, độ bám lốp và điều kiện vận hành chứ không chỉ so hai con số quảng cáo.

> **Chuyển mạch:** Công suất và mô-men chỉ mô tả nguồn lực; drivetrain quyết định lực đó được phân phối tới cầu nào và biến thành traction trên mặt đường ra sao.

## 4. FWD, RWD, AWD và 4WD nói về nơi lực được đưa tới

Dẫn động cầu trước (front-wheel drive, FWD / 전륜구동) đưa lực chủ yếu tới bánh trước; dẫn động cầu sau (rear-wheel drive, RWD / 후륜구동) đưa lực tới bánh sau. Dẫn động bốn bánh toàn thời gian hoặc có khả năng phân phối lực giữa hai cầu thường được gọi bằng các hệ thuật ngữ AWD/4WD, nhưng kiến trúc thực tế khác nhau theo hệ thống và nhà sản xuất.

Điều quan trọng là drivetrain không tự tạo thêm năng lượng. Nó **phân phối và biến đổi cách mô-men từ nguồn động lực đến mặt đường**. Điều này ảnh hưởng traction, packaging, hiệu suất, khối lượng và đặc tính điều khiển của xe.

> **Chuyển mạch:** Nơi truyền lực giải thích một phần khả năng bám và điều khiển, nhưng không mô tả hình thái không gian; sedan, hatchback, SUV và coupe là một trục kiến trúc khác.

## 5. Sedan, hatchback, SUV và coupe chủ yếu nói về kiến trúc thân xe

Những từ này không phải cấp độ “tốt hơn/xấu hơn”. Chúng mô tả cách bố trí thân xe và không gian theo các truyền thống thiết kế khác nhau. Một SUV có thể dùng FWD hoặc AWD; một sedan có thể dùng động cơ xăng, hybrid hoặc điện. Vì vậy không nên trộn `SUV`, `AWD` và `Hybrid` thành các lựa chọn trên cùng một trục.

Đây chính là pattern đã thấy ở whisky: nhiều nhãn trên sản phẩm thuộc **những chiều phân loại khác nhau**.

> **Chuyển mạch:** Khi đã tách drivetrain khỏi thân xe, người học có thể đọc toàn bộ hệ thống theo thứ tự từ năng lượng tới an toàn, rồi mới dùng specification hoặc thương hiệu để so sánh.

## 6. Bản đồ học xe hơi

Từ nền tảng này, nhánh Cars sẽ phát triển theo mạch:

`năng lượng → động cơ/motor → công suất & mô-men → transmission → drivetrain → tire/traction → steering/suspension → brake → chassis/body → safety → electronics → thông số & trải nghiệm → bảo dưỡng → kinh tế sở hữu`

Sau phần hệ thống cơ khí sẽ là các chapter thực dụng: cách đọc specification, vì sao dung tích động cơ không trực tiếp quyết định sức mạnh, turbocharger hoạt động thế nào, CVT/DCT/automatic khác nhau ra sao, lốp ảnh hưởng xe mạnh đến mức nào, và cuối cùng là tổng chi phí sở hữu (total cost of ownership, TCO / 총소유비용), khấu hao (depreciation / 감가상각) và cách đánh giá xe mới/xe cũ.

Các chapter nền tảng đã được nối vào route: [00. Powertrain and motion](00_powertrain_motion_foundations.md) đặt invariant lực–mô-men, [01. ICE, EV, hybrid and thermal](01_ice_ev_hybrid_and_thermal.md) đối chiếu đường năng lượng, [02. Transmission, tires, safety and ownership](02_transmission_tires_safety_and_ownership.md) đưa lực tới lốp và TCO, còn [03. Vehicle specification case lab](03_vehicle_specification_case_lab.md) áp dụng route vào quyết định.

> **Bàn giao:** Giữ mental model `năng lượng → mô-men → truyền lực → tiếp xúc mặt đường → điều khiển và bảo vệ`; các module turbo, CVT/DCT hoặc model cụ thể chỉ là mở rộng khi có specification, thị trường và điều kiện đo rõ.

## Đọc tiếp

Bước tiếp theo trong route hiện có là [01. ICE, EV, hybrid and thermal](01_ice_ev_hybrid_and_thermal.md): chapter này giải thích nguồn động lực và giới hạn nhiệt trước khi mở rộng sang displacement, cylinder layout, turbocharger, battery hoặc charging. Nhánh điện dùng cùng câu hỏi năng lượng–mô-men để đối chiếu motor với ICE, không tạo một mental model tách rời.

> **Bàn giao:** Bước kế tiếp là chapter về nguồn động lực; hãy dùng route này làm owner map và không kết luận chất lượng xe chỉ từ horsepower, kiểu thân xe hoặc một nhãn truyền động.
