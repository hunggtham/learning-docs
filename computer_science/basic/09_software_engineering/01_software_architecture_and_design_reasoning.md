# Kiến trúc phần mềm và tư duy thiết kế

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Kiến trúc phần mềm và tư duy thiết kế**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Kiến trúc là tập hợp các quyết định có hệ quả lớn** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Thuộc tính chất lượng định hình kiến trúc** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Kiến trúc không phải một sơ đồ hộp đẹp mắt. Nó là tập hợp những quyết định khó thay đổi về ranh giới, quyền sở hữu dữ liệu, giao tiếp, triển khai và các thuộc tính chất lượng. Thiết kế tốt bắt đầu từ các lực tác động và ràng buộc thật sự, không bắt đầu từ tên của một mẫu thiết kế.

## Kiến trúc là tập hợp các quyết định có hệ quả lớn

Quyết định “dùng PostgreSQL” thường có phạm vi ảnh hưởng khác hẳn việc đặt tên một trường là `createdAt`. **Quyết định kiến trúc (architecture decision)** thường tác động tới nhiều mô-đun (module / 모듈) hoặc nhóm và có chi phí di chuyển cao nếu đổi sau này.

Vì vậy **bản ghi quyết định kiến trúc (architecture decision record — ADR)** nên ghi bối cảnh, các phương án, quyết định cuối cùng và hệ quả. Mục tiêu không phải tăng thủ tục mà là giữ lại lý do để người bảo trì tương lai hiểu vì sao hệ thống có hình dạng hiện tại.

> **Chuyển mạch:** Trong **Kiến trúc phần mềm và tư duy thiết kế**, **Thuộc tính chất lượng định hình kiến trúc** tiếp nhận điểm tựa từ **Kiến trúc là tập hợp các quyết định có hệ quả lớn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mức liên kết và độ kết dính** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thuộc tính chất lượng định hình kiến trúc

Tính sẵn sàng, độ trễ, bảo mật, khả năng thay đổi, khả năng mở rộng và chi phí thường xung đột nhau.

Ví dụ, sao chép đồng bộ có thể tăng độ bền và mức nhất quán nhưng làm tăng độ trễ ghi và có thể giảm khả năng phục vụ khi replica không sẵn sàng. Vì vậy một kiến trúc chỉ có ý nghĩa khi gắn với thứ tự ưu tiên của các thuộc tính chất lượng.

> **Chuyển mạch:** Ở chặng này của **Kiến trúc phần mềm và tư duy thiết kế**, sau nội dung của **Thuộc tính chất lượng định hình kiến trúc**, **Mức liên kết và độ kết dính** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Che giấu thông tin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mức liên kết và độ kết dính

**Độ kết dính (cohesion)** cao nghĩa là hành vi và dữ liệu thường thay đổi cùng nhau được đặt gần nhau. **Mức liên kết (coupling)** thấp nghĩa là ít giả định phải truyền xuyên qua các ranh giới.

Coupling có nhiều dạng: lúc biên dịch, lúc chạy, qua lược đồ dữ liệu, qua thời gian và qua tổ chức. Hai dịch vụ không import mã của nhau nhưng luôn phải phát hành cùng một cửa sổ triển khai vẫn đang bị liên kết chặt.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc phần mềm và tư duy thiết kế**, **Che giấu thông tin** tiếp nhận điểm tựa từ **Mức liên kết và độ kết dính** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiến trúc phân lớp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Che giấu thông tin

Một mô-đun (module / 모듈) nên che quyết định dễ thay đổi phía sau giao diện ổn định. Ví dụ mô-đun (module / 모듈) lưu trữ có thể cung cấp `saveOrder()` thay vì buộc mọi nơi gọi phụ thuộc trực tiếp vào cấu trúc bảng nếu cấu trúc đó có khả năng thay đổi.

**Che giấu thông tin (information hiding)** giúp thu hẹp phạm vi ảnh hưởng của thay đổi.

> **Chuyển mạch:** Trong **Kiến trúc phần mềm và tư duy thiết kế**, **Kiến trúc phân lớp** tiếp nhận điểm tựa từ **Che giấu thông tin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trực giác của kiến trúc lục giác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiến trúc phân lớp

Kiến trúc phân lớp tạo hướng phụ thuộc, chẳng hạn giao diện → ứng dụng → miền nghiệp vụ → hạ tầng tùy phong cách thiết kế. Phân lớp giúp tách trách nhiệm nhưng quá nhiều lớp có thể tạo mã trung chuyển không mang giá trị.

Lớp là công cụ kiểm soát phụ thuộc, không phải quy tắc bắt mọi yêu cầu đi qua một số lượng lớp (class / 클래스) cố định.

> **Chuyển mạch:** Ở chặng này của **Kiến trúc phần mềm và tư duy thiết kế**, **Trực giác của kiến trúc lục giác** tiếp nhận điểm tựa từ **Kiến trúc phân lớp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu kiến trúc luôn phụ thuộc bối cảnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trực giác của kiến trúc lục giác

Trong **kiến trúc lục giác (hexagonal architecture / ports and adapters)**, lô-gic (logic / 논리) miền phụ thuộc vào các cổng trừu tượng; cơ sở dữ liệu, giao diện hoặc message broker bên ngoài đóng vai trò adapter. Mục tiêu là quy tắc nghiệp vụ không bị gắn cứng vào khung phần mềm (framework / 프레임워크) hoặc hạ tầng cụ thể.

Tuy nhiên nếu miền rất đơn giản, tạo giao diện (interface / 인터페이스) ở mọi nơi có thể trở thành thiết kế quá mức. Chỉ nên dựng ranh giới khi nó thực sự bảo vệ phần có khả năng thay đổi hoặc cần cô lập.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc phần mềm và tư duy thiết kế**, **Mẫu kiến trúc luôn phụ thuộc bối cảnh** tiếp nhận điểm tựa từ **Trực giác của kiến trúc lục giác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quyền sở hữu dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu kiến trúc luôn phụ thuộc bối cảnh

Monolith, microservices, event-driven, CQRS, layered hay pipes-and-filters không tạo thành một “thang trưởng thành”. Mỗi mẫu giải quyết một nhóm lực tác động và đồng thời tạo ra nghĩa vụ mới.

CQRS tách mô hình đọc và ghi khi nhu cầu hai phía khác nhau rõ rệt, nhưng làm đồng bộ và tiến hóa dữ liệu phức tạp hơn. sự kiện (event / 이벤트) sourcing hỗ trợ kiểm toán và phát lại lịch sử nhưng làm thay đổi lược đồ (schema / 스키마) và gỡ lỗi khó hơn.

> **Chuyển mạch:** Trong **Kiến trúc phần mềm và tư duy thiết kế**, **Mẫu kiến trúc luôn phụ thuộc bối cảnh** nêu điều cần giải thích; **Quyền sở hữu dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Đảo ngược phụ thuộc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quyền sở hữu dữ liệu

Ranh giới kiến trúc mạnh thường cần quyền sở hữu trạng thái rõ ràng. Nhiều dịch vụ cùng ghi trực tiếp vào một cơ sở dữ liệu dùng chung dễ tạo các bất biến ẩn mà không thành phần nào thật sự kiểm soát.

Quyền sở hữu không có nghĩa dữ liệu không được chia sẻ. Nó nghĩa một thành phần có thẩm quyền cập nhật và các thành phần khác truy cập qua hợp đồng hoặc bản sao phù hợp.

> **Chuyển mạch:** Ở chặng này của **Kiến trúc phần mềm và tư duy thiết kế**, **Quyền sở hữu dữ liệu** nêu điều cần giải thích; **Đảo ngược phụ thuộc** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Hàm kiểm tra sức khỏe kiến trúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đảo ngược phụ thuộc

Chính sách cấp cao không nên phụ thuộc trực tiếp vào cách triển khai cấp thấp khi cần tách sự biến động hoặc giảm coupling. **Đảo ngược phụ thuộc (dependency inversion)** dùng giao diện (interface / 인터페이스) hoặc lớp trừu tượng (abstraction / 추상화) để hướng phụ thuộc trong mã nguồn phục vụ tính ổn định.

Tuy nhiên một giao diện (interface / 인터페이스) chỉ có đúng một triển khai và không bảo vệ phần dễ thay đổi không tự động tạo ra giá trị.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc phần mềm và tư duy thiết kế**, **Hàm kiểm tra sức khỏe kiến trúc** tiếp nhận điểm tựa từ **Đảo ngược phụ thuộc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những hiểu nhầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàm kiểm tra sức khỏe kiến trúc

Ý định kiến trúc có thể suy giảm theo thời gian. Các kiểm tra tự động như quy tắc phụ thuộc, kiểm thử tương thích API, SLO độ trễ và quét chính sách bảo mật có thể đóng vai trò **hàm kiểm tra kiến trúc (architecture fitness function)** để phát hiện sự trôi khỏi thiết kế mong muốn.

Kiến trúc vì vậy không chỉ là thiết kế ban đầu; nó cần được kiểm chứng liên tục.

> **Chuyển mạch:** Trong **Kiến trúc phần mềm và tư duy thiết kế**, **Hàm kiểm tra sức khỏe kiến trúc** đã nêu tiêu chí phân biệt, còn **Những hiểu nhầm thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu nhầm thường gặp

**“Kiến trúc là chọn khung phần mềm (framework / 프레임워크).”** Không đúng. khung phần mềm (framework / 프레임워크) là một quyết định triển khai; kiến trúc rộng hơn, tập trung vào ranh giới và đánh đổi chất lượng.

**“Mẫu nổi tiếng nghĩa là best practice cho mọi nơi.”** Không đúng. Một mẫu chỉ phù hợp khi các lực tác động tương ứng thật sự tồn tại.

**“Clean kiến trúc (architecture / 아키텍처) càng nhiều lớp càng sạch.”** Không đúng. Tầng trung gian không có mục đích làm hệ thống khó hiểu hơn.

> **Chuyển mạch:** Ở chặng này của **Kiến trúc phần mềm và tư duy thiết kế**, **Những hiểu nhầm thường gặp** đã nêu tiêu chí phân biệt, còn **Mô hình tư duy** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> Kiến trúc là cách phân bố trách nhiệm và ràng buộc để những thay đổi hoặc lỗi quan trọng bị giới hạn trong các ranh giới hợp lý.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc phần mềm và tư duy thiết kế**, **Kết nối** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc cùng [phân rã hệ thống và ranh giới dịch vụ](../08_software_systems/07_system_decomposition_services_and_boundaries.md), [yêu cầu và đặc tả](./00_requirements_specification_and_engineering_process.md) và [bảo trì cùng nợ kỹ thuật](./04_maintenance_evolution_and_technical_debt.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
