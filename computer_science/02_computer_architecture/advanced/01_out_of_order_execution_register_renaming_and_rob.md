# Out-of-order execution, register renaming và reorder buffer

Một CPU hiện đại hiếm khi thực thi instruction đúng từng bước theo thứ tự source code. Nếu instruction thứ hai phải chờ dữ liệu từ RAM nhưng instruction thứ ba và thứ tư đã có đủ operand, việc để toàn bộ pipeline đứng yên sẽ lãng phí execution units. **Out-of-order execution (OoO / 비순차 실행)** giải quyết vấn đề đó bằng cách cho phép CPU thực thi các micro-operation đã sẵn sàng trước, nhưng vẫn cố gắng làm cho chương trình quan sát kết quả như thể instruction đã hoàn thành theo đúng thứ tự kiến trúc.

Điểm quan trọng là phân biệt **execution order** với **architectural order**. CPU có thể tính toán bên trong theo một thứ tự khác, nhưng trạng thái mà software nhìn thấy — register, exception, memory ordering theo ISA — phải tuân thủ contract của kiến trúc.

## Từ instruction đến micro-operation

Instruction trong ISA như x86 `ADD`, `LOAD` hay `CALL` là contract giữa software và processor. Bên trong CPU, instruction có thể được decode thành một hoặc nhiều **micro-operations (µops)** nhỏ hơn. Front-end fetch và decode tạo ra dòng µop; back-end quyết định µop nào có thể issue tới integer ALU, floating-point unit, load/store unit hoặc vector unit.

Nếu một µop cần kết quả chưa có, nó phải chờ. Nhưng dependency của một µop không nhất thiết ngăn các µop độc lập phía sau chạy. Đây là nguồn instruction-level parallelism mà OoO engine khai thác.

## Data dependency thật và dependency giả

Giả sử chương trình có logic:

```text
R1 = R2 + R3
R4 = R1 * R5
R1 = R6 + R7
```

Instruction thứ hai có **RAW dependency — Read After Write** thật với instruction đầu vì nó cần giá trị mới của `R1`. Nhưng instruction thứ ba chỉ tái sử dụng tên architectural register `R1`; nó không phụ thuộc vào giá trị cũ. Nếu CPU coi tên register vật lý và architectural register là một, việc tái sử dụng tên này tạo **WAR/WAW dependency** giả.

**Register renaming (레지스터 리네이밍)** ánh xạ architectural registers sang một tập physical registers lớn hơn. Hai phiên bản khác nhau của `R1` có thể tồn tại đồng thời trong hai physical register khác nhau. Nhờ đó CPU loại bỏ false dependency và mở rộng cửa sổ instruction có thể chạy song song.

## Reservation station và wakeup/select

Sau rename, µop đi vào các cấu trúc chờ execution. Một entry thường giữ operation, source operands hoặc tag của physical register đang chờ, cùng destination tag. Khi producer hoàn thành, dependent µops được đánh thức. Scheduler chọn các µop đã ready và gửi chúng tới execution ports phù hợp.

Đây không phải một queue FIFO đơn giản. Scheduler phải giải bài toán wakeup/select rất nhanh trong mỗi cycle, nên kích thước scheduling window, số execution ports và wiring đều ảnh hưởng trực tiếp tới clock frequency, area và power.

## Reorder Buffer giữ precise architectural state

Nếu execution được phép chạy lung tung, CPU vẫn phải xử lý exception chính xác. Giả sử instruction cũ hơn gây page fault nhưng vài instruction trẻ hơn đã tính xong. Software không được nhìn thấy một trạng thái nửa trước-nửa sau tùy tiện.

**Reorder Buffer (ROB / 재정렬 버퍼)** theo dõi các instruction theo program order. Execution có thể hoàn thành out-of-order, nhưng **retirement/commit** thường diễn ra in-order. Chỉ khi instruction ở đầu ROB đã hoàn tất hợp lệ thì kết quả architectural của nó mới được commit.

Cơ chế này tạo **precise exception**: khi fault xảy ra, processor có thể bỏ các instruction trẻ hơn và trình bày trạng thái tương ứng với điểm chính xác trong instruction stream.

## Load/store làm OoO khó hơn register operation

Register dependency có thể nhận diện từ operand, nhưng hai memory operation có thể alias dù address chưa được tính xong. CPU vì thế cần **Load/Store Queue (LSQ)** và memory disambiguation.

Nếu một load trẻ hơn được cho chạy trước một store cũ hơn mà sau đó phát hiện cả hai trỏ cùng address, CPU phải replay hoặc squash phần computation phụ thuộc. Predictor tốt giúp tăng parallelism; predictor sai tạo penalty.

Store thường chưa được phép trở thành globally visible ngay khi execution unit tính xong. Store buffer giữ chúng cho đến khi ordering và retirement conditions cho phép. Điều này liên hệ trực tiếp với memory consistency model của chapter trước.

## Speculation và rollback

OoO execution gần như luôn đi cùng speculation. CPU dự đoán branch, memory dependency hoặc target để tiếp tục giữ pipeline bận. Nếu dự đoán đúng, latency bị che giấu. Nếu sai, speculative work phải bị loại bỏ và pipeline khôi phục từ checkpoint phù hợp.

Vì vậy performance không chỉ phụ thuộc IPC lý tưởng mà còn phụ thuộc kích thước ROB, scheduler window, branch accuracy, cache miss latency và khả năng tìm independent work trong cửa sổ hiện tại.

## Ví dụ reasoning về performance

Một backend service có hot loop thực hiện nhiều phép tính độc lập có thể tận dụng OoO tốt. Ngược lại, pointer chasing kiểu `node = node.next` tạo dependency chain: address của load tiếp theo chỉ biết sau khi load hiện tại hoàn thành. Dù CPU có nhiều ALU, nó không thể tạo parallelism từ một chuỗi dependency nối tiếp như vậy.

Đây là lý do hai thuật toán cùng Big-O có thể khác performance đáng kể. Data layout tốt không chỉ giúp cache locality mà còn có thể tạo nhiều independent memory operations hơn cho OoO engine.

## Trade-off kiến trúc

ROB lớn và scheduler rộng giúp che latency tốt hơn nhưng tốn transistor, năng lượng và wiring. Nhiều execution ports tăng throughput nhưng làm rename/scheduling/bypass network phức tạp hơn. Mobile CPU, server CPU và high-performance desktop CPU vì thế chọn điểm cân bằng khác nhau giữa power, area, latency và throughput.

## Mental model

> Out-of-order CPU là một hệ thống speculative data-flow nằm phía sau một contract in-order. Rename loại bỏ dependency giả, scheduler tìm work đã ready, ROB bảo toàn thứ tự architectural, còn rollback biến speculation sai thành trạng thái không được software quan sát.

Khi phân tích performance, đừng chỉ hỏi “CPU bao nhiêu GHz?”. Hãy hỏi dependency chain dài bao nhiêu, instruction window có đủ work độc lập không, cache miss có thể được overlap không, và speculation có thường xuyên bị phá bỏ hay không.