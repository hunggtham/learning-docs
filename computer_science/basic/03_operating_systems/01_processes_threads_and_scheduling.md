# Tiến trình, luồng và lập lịch

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Processes, threads và scheduling**. Route đi từ address space/process → thread/context switch → scheduling/queues → latency, fairness và throughput, để hành vi ứng dụng được nối với cách CPU phân phối thời gian.

Một máy có thể đồng thời chạy trình duyệt, cơ sở dữ liệu, IDE và hàng trăm dịch vụ dù số lõi CPU hữu hạn. Hệ điều hành tạo cảm giác mọi thứ cùng chạy bằng cách chia sẻ thời gian thực thi giữa nhiều công việc. Để suy luận đúng, cần tách **tiến trình (process / 프로세스)** — ranh giới cô lập và chứa tài nguyên — khỏi **luồng (thread)** — dòng thực thi có thể được bộ lập lịch phân CPU.

## Tiến trình

Một tiến trình (process / 프로세스) thường có không gian địa chỉ ảo, các handle hoặc tệp (file / 파일) descriptor đang mở, danh tính bảo mật và một hoặc nhiều luồng. Hai tiến trình mặc định không thể đọc trực tiếp bộ nhớ của nhau vì ánh xạ trang và quyền bảo vệ khác nhau.

Cách tạo tiến trình phụ thuộc hệ điều hành. Trên Unix, `fork()` về mặt khái niệm tạo tiến trình con từ tiến trình cha và thường tận dụng sao chép khi ghi (copy-on-write / 쓰기 시 복사); `exec()` thay ảnh tiến trình hiện tại bằng chương trình mới. Windows dùng nhóm API khác. Môi trường lập trình cấp cao có thể che đi nhiều chi tiết này.

> **Chuyển mạch:** Trong **Tiến trình, luồng và lập lịch**, **Luồng** tiếp nhận điểm tựa từ **Tiến trình** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuyển ngữ cảnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Luồng

Luồng (thread / 스레드) là một ngữ cảnh thực thi gồm bộ đếm lệnh, thanh ghi, ngăn xếp (stack / 스택) và trạng thái lập lịch. Các luồng trong cùng tiến trình dùng chung vùng nhớ động (heap / 힙), không gian địa chỉ và nhiều tài nguyên khác.

Chia sẻ làm giao tiếp rẻ hơn nhưng tạo nguy cơ tranh chấp dữ liệu (data race). Tiến trình cô lập tốt hơn nhưng giao tiếp liên tiến trình (IPC) thường cần thêm chi phí sao chép, truyền thông hoặc tuần tự hóa. Đây là sự đánh đổi giữa cô lập và chia sẻ.

> **Chuyển mạch:** Ở chặng này của **Tiến trình, luồng và lập lịch**, **Chuyển ngữ cảnh** tiếp nhận điểm tựa từ **Luồng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ lập lịch đang tối ưu điều gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuyển ngữ cảnh

Bộ lập lịch chuyển CPU từ công việc A sang B bằng cách lưu và khôi phục ngữ cảnh thực thi, đồng thời cập nhật trạng thái không gian địa chỉ khi cần. Chi phí không chỉ là vài thao tác lưu thanh ghi; tính cục bộ của bộ nhớ đệm (cache / 캐시) và TLB cũng có thể bị ảnh hưởng.

Vì vậy “thêm luồng để chạy nhanh hơn” có giới hạn. Quá nhiều luồng sẵn sàng chạy làm tăng số lần chuyển ngữ cảnh, tranh chấp bộ nhớ đệm (cache / 캐시) và chi phí lập lịch.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình, luồng và lập lịch**, **Bộ lập lịch đang tối ưu điều gì?** tiếp nhận điểm tựa từ **Chuyển ngữ cảnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Công việc nặng CPU và công việc nặng I/O** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ lập lịch đang tối ưu điều gì?

**Lập lịch (scheduling / 스케줄링)** phải cân bằng thông lượng, độ trễ, khả năng phản hồi, tính công bằng và mức ưu tiên. Tải xử lý theo lô muốn thông lượng cao; giao diện tương tác muốn phản hồi nhanh; hệ thống thời gian thực cần bảo đảm thời hạn.

Các thuật toán giáo khoa như FCFS, SJF, Round Robin và Priority Scheduling giúp hiểu các chiều đánh đổi. Bộ lập lịch thực tế như Linux CFS hoặc các cơ chế thuộc họ EEVDF phức tạp hơn và có thể thay đổi theo phiên bản kernel.

> **Chuyển mạch:** Trong **Tiến trình, luồng và lập lịch**, **Công việc nặng CPU và công việc nặng I/O** tiếp nhận điểm tựa từ **Bộ lập lịch đang tối ưu điều gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Luồng người dùng, luồng kernel và môi trường thực thi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Công việc nặng CPU và công việc nặng I/O

Công việc **nặng CPU (CPU-bound)** dành phần lớn thời gian để tính toán và thường luôn ở trạng thái có thể chạy. Công việc **nặng I/O (I/O-bound)** chạy trong thời gian ngắn rồi ngủ để chờ đĩa, mạng hoặc thiết bị khác.

Khi một công việc bị chặn để chờ I/O, bộ lập lịch có thể đưa công việc khác lên CPU. Vì vậy đồng thời (concurrency) có thể tăng thông lượng cho tải nặng I/O ngay cả khi máy chỉ có ít lõi: lúc A chờ mạng, B có thể dùng CPU.

> **Chuyển mạch:** Ở chặng này của **Tiến trình, luồng và lập lịch**, **Luồng người dùng, luồng kernel và môi trường thực thi** tiếp nhận điểm tựa từ **Công việc nặng CPU và công việc nặng I/O** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhóm luồng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Luồng người dùng, luồng kernel và môi trường thực thi

Có nhiều mô hình ánh xạ giữa công việc của ngôn ngữ lập trình và luồng hệ điều hành: 1:1, nhiều-một hoặc nhiều-nhiều. Luồng Java truyền thống thường ánh xạ 1:1; virtual luồng thực thi (thread / 스레드) của Java ghép nhiều continuation nhẹ lên các luồng mang (carrier thread). Goroutine của Go được bộ lập lịch của thời gian chạy (runtime / 런타임) ghép theo mô hình M:N. JavaScript bất đồng bộ thường dựa trên vòng lặp sự kiện (event loop / 이벤트 루프) và các tác vụ.

Vì vậy khi nói “luồng thực thi (thread / 스레드)”, cần xác định đang nói về luồng hệ điều hành, luồng ngôn ngữ, virtual luồng thực thi (thread / 스레드) hay tác vụ/coroutine.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình, luồng và lập lịch**, **Nhóm luồng** tiếp nhận điểm tựa từ **Luồng người dùng, luồng kernel và môi trường thực thi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đảo ngược ưu tiên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhóm luồng

Tạo số luồng không giới hạn dễ làm cạn bộ nhớ và gây quá tải bộ lập lịch. **Nhóm luồng (thread pool)** giới hạn số worker và đưa công việc vào hàng đợi. Tuy nhiên một pool cố định vẫn có thể bế tắc hoặc bỏ đói công việc nếu các tác vụ bị chặn trong khi chờ tác vụ khác cũng phải chạy trên chính pool đó.

Kích thước pool phải phù hợp loại tải. Công việc nặng CPU thường cần mức song song gần số lõi; công việc nặng I/O có thể chịu mức đồng thời cao hơn, nhưng giới hạn của cơ sở dữ liệu, mạng và dịch vụ bên ngoài vẫn quyết định ngưỡng thực tế.

> **Chuyển mạch:** Trong **Tiến trình, luồng và lập lịch**, **Đảo ngược ưu tiên** tiếp nhận điểm tựa từ **Nhóm luồng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trực giác từ định luật Little** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đảo ngược ưu tiên

Một luồng ưu tiên cao có thể phải chờ khóa do luồng ưu tiên thấp giữ, trong khi các tác vụ ưu tiên trung bình liên tục giành CPU trước luồng đang giữ khóa. Hiện tượng này gọi là **đảo ngược ưu tiên (priority inversion)**. Kế thừa ưu tiên (priority inheritance) là một cơ chế giảm vấn đề.

Điều này cho thấy lập lịch và đồng bộ không phải hai chủ đề độc lập.

> **Chuyển mạch:** Ở chặng này của **Tiến trình, luồng và lập lịch**, **Trực giác từ định luật Little** tiếp nhận điểm tựa từ **Đảo ngược ưu tiên** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trực giác từ định luật Little

Trong một hệ thống ổn định:

\[
L = \lambda W
\]

Trong đó `L` là số phần tử trung bình đang ở trong hệ thống, `λ` là tốc độ đến và `W` là thời gian trung bình mỗi phần tử ở lại. Nếu độ trễ yêu cầu tăng trong khi tốc độ đến không đổi, số yêu cầu đang xử lý đồng thời cũng tăng. Vì vậy lập lịch và hàng đợi nối trực tiếp với kỹ thuật hiệu năng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình, luồng và lập lịch**, **Mô hình tư duy** gom các mảnh từ **Trực giác từ định luật Little** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu nhầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> **Tiến trình bảo vệ ranh giới; luồng mang dòng thực thi; bộ lập lịch phân phối thời gian CPU.** Đồng thời cho phép các công việc chồng lấp thời gian chờ; song song (parallelism) cần nhiều tài nguyên thực thi vật lý thật sự.

> **Chuyển mạch:** Trong **Tiến trình, luồng và lập lịch**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những hiểu nhầm thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu nhầm thường gặp

**“Một tiến trình bằng một luồng.”** Không đúng. Một tiến trình có thể có nhiều luồng.

**“Càng nhiều luồng càng nhanh.”** Không đúng. CPU bão hòa, khóa, bộ nhớ đệm (cache / 캐시) và chuyển ngữ cảnh có thể làm hệ thống chậm hơn.

**“Luồng bị chặn vẫn dùng CPU như vòng lặp bận.”** Thường không đúng. Tác vụ bị chặn thường không ở trạng thái có thể chạy, nên bộ lập lịch có thể giao CPU cho tác vụ khác.

> **Chuyển mạch:** Ở chặng này của **Tiến trình, luồng và lập lịch**, **Những hiểu nhầm thường gặp** đã nêu tiêu chí phân biệt, còn **Kết nối** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Phần cứng nhiều lõi được giải thích ở [kiến trúc song song](../02_computer_architecture/05_parallel_computer_architecture.md). Chia sẻ trạng thái dẫn tới [đồng thời và đồng bộ](./02_concurrency_synchronization_and_deadlock.md). Các mô hình thời gian chạy (runtime / 런타임) được nối ở [mô hình thực thi của ngôn ngữ](../04_programming_languages/00_language_semantics_and_execution_models.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
