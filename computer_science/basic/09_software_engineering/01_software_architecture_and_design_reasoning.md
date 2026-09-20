# Kiến trúc phần mềm và tư duy thiết kế

Kiến trúc không phải một sơ đồ hộp đẹp mắt. Nó là tập hợp những quyết định khó thay đổi về ranh giới, quyền sở hữu dữ liệu, giao tiếp, triển khai và các thuộc tính chất lượng. Thiết kế tốt bắt đầu từ các lực tác động và ràng buộc thật sự, không bắt đầu từ tên của một mẫu thiết kế.

## Kiến trúc là tập hợp các quyết định có hệ quả lớn

Quyết định “dùng PostgreSQL” thường có phạm vi ảnh hưởng khác hẳn việc đặt tên một trường là `createdAt`. **Quyết định kiến trúc (architecture decision)** thường tác động tới nhiều module hoặc nhóm và có chi phí di chuyển cao nếu đổi sau này.

Vì vậy **bản ghi quyết định kiến trúc (Architecture Decision Record — ADR)** nên ghi bối cảnh, các phương án, quyết định cuối cùng và hệ quả. Mục tiêu không phải tăng thủ tục mà là giữ lại lý do để người bảo trì tương lai hiểu vì sao hệ thống có hình dạng hiện tại.

## Thuộc tính chất lượng định hình kiến trúc

Tính sẵn sàng, độ trễ, bảo mật, khả năng thay đổi, khả năng mở rộng và chi phí thường xung đột nhau.

Ví dụ, sao chép đồng bộ có thể tăng độ bền và mức nhất quán nhưng làm tăng độ trễ ghi và có thể giảm khả năng phục vụ khi replica không sẵn sàng. Vì vậy một kiến trúc chỉ có ý nghĩa khi gắn với thứ tự ưu tiên của các thuộc tính chất lượng.

## Mức liên kết và độ kết dính

**Độ kết dính (cohesion)** cao nghĩa là hành vi và dữ liệu thường thay đổi cùng nhau được đặt gần nhau. **Mức liên kết (coupling)** thấp nghĩa là ít giả định phải truyền xuyên qua các ranh giới.

Coupling có nhiều dạng: lúc biên dịch, lúc chạy, qua lược đồ dữ liệu, qua thời gian và qua tổ chức. Hai dịch vụ không import mã của nhau nhưng luôn phải phát hành cùng một cửa sổ triển khai vẫn đang bị liên kết chặt.

## Che giấu thông tin

Một module nên che quyết định dễ thay đổi phía sau giao diện ổn định. Ví dụ module lưu trữ có thể cung cấp `saveOrder()` thay vì buộc mọi nơi gọi phụ thuộc trực tiếp vào cấu trúc bảng nếu cấu trúc đó có khả năng thay đổi.

**Che giấu thông tin (information hiding)** giúp thu hẹp phạm vi ảnh hưởng của thay đổi.

## Kiến trúc phân lớp

Kiến trúc phân lớp tạo hướng phụ thuộc, chẳng hạn giao diện → ứng dụng → miền nghiệp vụ → hạ tầng tùy phong cách thiết kế. Phân lớp giúp tách trách nhiệm nhưng quá nhiều lớp có thể tạo mã trung chuyển không mang giá trị.

Lớp là công cụ kiểm soát phụ thuộc, không phải quy tắc bắt mọi yêu cầu đi qua một số lượng class cố định.

## Trực giác của kiến trúc lục giác

Trong **kiến trúc lục giác (hexagonal architecture / ports and adapters)**, logic miền phụ thuộc vào các cổng trừu tượng; cơ sở dữ liệu, giao diện hoặc message broker bên ngoài đóng vai trò adapter. Mục tiêu là quy tắc nghiệp vụ không bị gắn cứng vào framework hoặc hạ tầng cụ thể.

Tuy nhiên nếu miền rất đơn giản, tạo interface ở mọi nơi có thể trở thành thiết kế quá mức. Chỉ nên dựng ranh giới khi nó thực sự bảo vệ phần có khả năng thay đổi hoặc cần cô lập.

## Mẫu kiến trúc luôn phụ thuộc bối cảnh

Monolith, microservices, event-driven, CQRS, layered hay pipes-and-filters không tạo thành một “thang trưởng thành”. Mỗi mẫu giải quyết một nhóm lực tác động và đồng thời tạo ra nghĩa vụ mới.

CQRS tách mô hình đọc và ghi khi nhu cầu hai phía khác nhau rõ rệt, nhưng làm đồng bộ và tiến hóa dữ liệu phức tạp hơn. Event sourcing hỗ trợ kiểm toán và phát lại lịch sử nhưng làm thay đổi schema và gỡ lỗi khó hơn.

## Quyền sở hữu dữ liệu

Ranh giới kiến trúc mạnh thường cần quyền sở hữu trạng thái rõ ràng. Nhiều dịch vụ cùng ghi trực tiếp vào một cơ sở dữ liệu dùng chung dễ tạo các bất biến ẩn mà không thành phần nào thật sự kiểm soát.

Quyền sở hữu không có nghĩa dữ liệu không được chia sẻ. Nó nghĩa một thành phần có thẩm quyền cập nhật và các thành phần khác truy cập qua hợp đồng hoặc bản sao phù hợp.

## Đảo ngược phụ thuộc

Chính sách cấp cao không nên phụ thuộc trực tiếp vào cách triển khai cấp thấp khi cần tách sự biến động hoặc giảm coupling. **Đảo ngược phụ thuộc (dependency inversion)** dùng interface hoặc abstraction để hướng phụ thuộc trong mã nguồn phục vụ tính ổn định.

Tuy nhiên một interface chỉ có đúng một triển khai và không bảo vệ phần dễ thay đổi không tự động tạo ra giá trị.

## Hàm kiểm tra sức khỏe kiến trúc

Ý định kiến trúc có thể suy giảm theo thời gian. Các kiểm tra tự động như quy tắc phụ thuộc, kiểm thử tương thích API, SLO độ trễ và quét chính sách bảo mật có thể đóng vai trò **hàm kiểm tra kiến trúc (architecture fitness function)** để phát hiện sự trôi khỏi thiết kế mong muốn.

Kiến trúc vì vậy không chỉ là thiết kế ban đầu; nó cần được kiểm chứng liên tục.

## Những hiểu nhầm thường gặp

**“Kiến trúc là chọn framework.”** Không đúng. Framework là một quyết định triển khai; kiến trúc rộng hơn, tập trung vào ranh giới và đánh đổi chất lượng.

**“Mẫu nổi tiếng nghĩa là best practice cho mọi nơi.”** Không đúng. Một mẫu chỉ phù hợp khi các lực tác động tương ứng thật sự tồn tại.

**“Clean Architecture càng nhiều lớp càng sạch.”** Không đúng. Tầng trung gian không có mục đích làm hệ thống khó hiểu hơn.

## Mô hình tư duy

> Kiến trúc là cách phân bố trách nhiệm và ràng buộc để những thay đổi hoặc lỗi quan trọng bị giới hạn trong các ranh giới hợp lý.

## Kết nối

Đọc cùng [phân rã hệ thống và ranh giới dịch vụ](../08_software_systems/07_system_decomposition_services_and_boundaries.md), [yêu cầu và đặc tả](./00_requirements_specification_and_engineering_process.md) và [bảo trì cùng nợ kỹ thuật](./04_maintenance_evolution_and_technical_debt.md).