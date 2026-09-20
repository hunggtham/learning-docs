# Modular monolith vs services: boundary economics và migration

“Monolith hay microservices?” thường bị biến thành câu hỏi công nghệ, trong khi vấn đề thật là **boundary economics**: boundary nào cần enforce, team nào sở hữu state, change nào thường đi cùng nhau, failure nào cần cô lập và organization có đủ năng lực vận hành distributed system hay không.

## Monolith không đồng nghĩa spaghetti

Một **modular monolith** deploy như một application nhưng bên trong có module boundaries rõ, dependency direction và ownership contract. Module có thể có API nội bộ và không cho code khác truy cập trực tiếp implementation/data của nó.

Nếu boundary logic không tồn tại trong monolith, tách process thường chỉ biến coupling trong memory thành coupling qua network.

## Service boundary có chi phí cố định

Khi module trở thành service, function call biến thành network call. Ta nhận thêm serialization, timeout, retry, authentication, observability, deployment, version compatibility và partial failure.

Đổi lại có thể nhận independent deployment, resource scaling, fault isolation và team autonomy. Service chỉ đáng giá khi lợi ích boundary vượt distributed-systems tax.

## Data ownership là boundary mạnh hơn endpoint

Hai services dùng chung database schema và sửa trực tiếp table của nhau vẫn coupled mạnh dù có hai deployment. Một service boundary trưởng thành thường đi cùng **data ownership**: service khác tương tác qua contract thay vì bypass owner.

Điều này không bắt buộc “mỗi service một database server”; điểm quan trọng là quyền thay đổi schema/data thuộc một owner và access path được kiểm soát.

## Transaction trở thành workflow

Trong monolith + single database, nhiều invariant có thể nằm trong ACID transaction. Sau khi tách service, transaction xuyên boundary trở nên đắt hoặc không khả dụng. Business operation phải được modeling thành workflow với message, retry, idempotency và compensation.

Đây là lý do decomposition không chỉ là cắt package thành REST APIs. Transaction boundary thay đổi semantics của hệ thống.

## Coupling có nhiều chiều

Services có thể loosely coupled về code nhưng tightly coupled về deployment nếu mọi release phải phối hợp. Có thể độc lập deployment nhưng coupled về runtime nếu synchronous call chain dài. Có thể tách runtime nhưng coupled về data schema.

Đánh giá boundary cần nhìn **change coupling, temporal coupling, data coupling và organizational coupling**.

## Khi modular monolith có lợi

Team nhỏ, domain còn thay đổi nhanh, transaction cross-domain nhiều và operational platform chưa trưởng thành thường hưởng lợi từ modular monolith. Debugging local đơn giản, refactor cross-module rẻ hơn và consistency dễ giữ.

Điều kiện là architecture phải thực sự enforce module boundaries; nếu không, technical debt tích tụ và extraction sau này khó hơn.

## Khi service extraction có tín hiệu tốt

Một module có scaling profile khác biệt, security boundary riêng, release cadence độc lập hoặc team ownership ổn định có thể là candidate tốt. Hot path cần resource đặc biệt cũng có thể justify extraction.

“Codebase lớn” một mình chưa đủ; repository có thể lớn nhưng module boundaries vẫn quản lý tốt.

## Migration theo seam

Extraction an toàn thường bắt đầu từ seam rõ: define interface, ngăn direct database access, đưa dependency qua abstraction, quan sát traffic, sau đó mới move implementation ra process riêng.

Pattern strangler cho phép route từng capability sang service mới thay vì rewrite toàn hệ thống. Branch-by-abstraction giúp code cũ và mới cùng tồn tại trong migration mà không cần long-lived branch khổng lồ.

## Reverse migration cũng hợp lệ

Nếu service boundary tạo nhiều operational cost nhưng không mang autonomy/isolation thực, merge services trở lại modular monolith có thể là quyết định đúng. Architecture evolution không phải con đường một chiều từ monolith → microservices.

## Mental model

> Process boundary là công cụ kinh tế-kỹ thuật. Modular monolith tối ưu local reasoning và transaction simplicity; services mua autonomy/isolation bằng distributed complexity. Boundary tốt là nơi ownership, change pattern, data và failure semantics cùng có lý do tách — không phải nơi sơ đồ trông đẹp.