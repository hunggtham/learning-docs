# Hóa học và Trí tuệ nhân tạo — dự đoán trong không gian hóa học

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Hóa học và Trí tuệ nhân tạo — dự đoán trong không gian hóa học**. Route đi từ biểu diễn phân tử/dataset → descriptor và mô hình dự đoán → xác thực ngoài mẫu → dự đoán tính chất/phản ứng → uncertainty và domain shift, để AI hỗ trợ suy luận hóa học chứ không thay thế bằng chứng thực nghiệm.

> Trí tuệ nhân tạo (**Artificial Intelligence, AI**) hữu ích trong Hóa học vì số phân tử, vật liệu và điều kiện phản ứng khả dĩ lớn hơn rất nhiều so với khả năng tổng hợp, đo đạc hoặc tính toán lượng tử trực tiếp. Mô hình AI có thể đóng vai trò bộ xấp xỉ, bộ xếp hạng và công cụ định hướng tìm kiếm, nhưng kết quả chỉ có ý nghĩa khi đi kèm ràng buộc hóa học, đánh giá độ không đảm bảo và kiểm chứng thực nghiệm.

## Dự đoán tính chất từ cấu trúc

Một bài toán phổ biến là nhận đầu vào dưới dạng cấu trúc phân tử rồi dự đoán một tính chất như độ tan, `logP`, `pKa`, phổ, độc tính, năng lượng hoặc các đại lượng thu được từ tính toán lượng tử.

Để máy học có thể xử lý phân tử, cấu trúc hóa học phải được chuyển thành biểu diễn số. Cách cổ điển dùng descriptor và fingerprint được thiết kế bằng tay; cách hiện đại có thể học trực tiếp **biểu diễn đồ thị (graph embedding)** hoặc biểu diễn hình học ba chiều từ tọa độ nguyên tử.

Điểm quan trọng là mô hình không “nhìn thấy phân tử” theo cách nhà hóa học nhìn cấu trúc Lewis. Nó chỉ nhận một biểu diễn, vì vậy giới hạn của biểu diễn sẽ trở thành giới hạn của mô hình.

> **Chuyển mạch:** Structure-to-property prediction tạo feature space; reaction prediction mở rộng sang transformation space, còn molecular generation phải giữ chemical validity và uncertainty thay vì chỉ tối ưu score.

## Dự đoán phản ứng

AI có thể dự đoán sản phẩm từ chất phản ứng và thuốc thử, đề xuất điều kiện phản ứng hoặc giải bài toán **phân tích ngược tổng hợp (retrosynthesis)** để tìm đường tổng hợp một phân tử mục tiêu.

Tuy nhiên độ chính xác cao trên bộ dữ liệu chuẩn không đồng nghĩa mô hình đã hiểu cơ chế. Nếu dữ liệu chứa nhiều mẫu phản ứng lặp lại, mô hình có thể học rất tốt quy luật thống kê của dữ liệu mà vẫn yếu khi gặp hóa học mới, chất nền hiếm hoặc cơ chế ngoài miền huấn luyện.

Vì vậy cần tách hai câu hỏi: mô hình dự đoán đúng đến mức nào, và nó có đang suy luận theo các ràng buộc hóa học hợp lý hay chỉ nhận diện mẫu quen thuộc?

> **Chuyển mạch:** Ở chặng này của **Hóa học và Trí tuệ nhân tạo — dự đoán trong không gian hóa học**, **Hóa học sinh phân tử** tiếp nhận điểm tựa từ **Dự đoán phản ứng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cấu trúc protein và phức phân tử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hóa học sinh phân tử

**Mô hình sinh (generative model)** có thể đề xuất phân tử mới thỏa các tính chất mục tiêu. Nhưng thiết kế phân tử thực tế luôn là bài toán nhiều mục tiêu: hoạt tính, độ chọn lọc, độ tan, độc tính, độ ổn định, khả năng tổng hợp, chi phí và ràng buộc sở hữu trí tuệ có thể xung đột nhau.

Do đó phân tử được sinh ra chỉ là giả thuyết. Nó vẫn cần kiểm tra hóa trị, điện tích, độ bền, khả năng tổng hợp, độ mới và cuối cùng là xác nhận thực nghiệm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hóa học và Trí tuệ nhân tạo — dự đoán trong không gian hóa học**, **Cấu trúc protein và phức phân tử** tiếp nhận điểm tựa từ **Hóa học sinh phân tử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khám phá vật liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấu trúc protein và phức phân tử

Học sâu (**deep learning**) có thể suy ra cấu trúc protein hoặc phức từ trình tự, thông tin tiến hóa và dữ liệu cấu trúc. Điều này rút ngắn mạnh giai đoạn tạo giả thuyết trong sinh học cấu trúc và phát triển thuốc.

Tuy vậy protein thật tồn tại dưới dạng một tập hợp cấu dạng động, có thể phụ thuộc ligand, màng, pH, ion kim loại và môi trường tế bào. Một cấu trúc dự đoán tốt vẫn không thay thế hoàn toàn động lực học phân tử và dữ liệu thực nghiệm.

> **Chuyển mạch:** Trong **Hóa học và Trí tuệ nhân tạo — dự đoán trong không gian hóa học**, **Khám phá vật liệu** tiếp nhận điểm tựa từ **Cấu trúc protein và phức phân tử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Giải thích phổ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khám phá vật liệu

AI có thể sàng lọc thành phần, cấu trúc tinh thể hoặc bề mặt xúc tác để tìm vật liệu pin, chất bán dẫn, chất xúc tác và vật liệu hấp phụ.

Một hướng quan trọng là dùng **mô hình thay thế (surrogate model)** để xấp xỉ những phép tính đắt như lý thuyết phiếm hàm mật độ (**Density Functional Theory, DFT**). Thay vì chạy DFT cho hàng triệu ứng viên, ta tính chính xác một tập nhỏ rồi huấn luyện mô hình để ưu tiên những ứng viên hứa hẹn nhất.

**Học chủ động (active learning)** mở rộng ý tưởng này bằng cách cho hệ thống tự chọn thí nghiệm hoặc phép tính tiếp theo sao cho thu được nhiều thông tin nhất.

> **Chuyển mạch:** Ở chặng này của **Hóa học và Trí tuệ nhân tạo — dự đoán trong không gian hóa học**, **Giải thích phổ** tiếp nhận điểm tựa từ **Khám phá vật liệu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ không đảm bảo và dữ liệu ngoài miền** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Giải thích phổ

Mô hình học máy có thể hỗ trợ nhận dạng hoặc giải thích phổ IR, NMR và khối phổ. Một số hệ dùng mô hình hoàn toàn dựa trên dữ liệu; các hệ mạnh hơn thường kết hợp mô phỏng vật lý với phần hiệu chỉnh học từ dữ liệu.

Cách kết hợp này hữu ích vì định luật vật lý giúp giới hạn không gian lời giải, còn dữ liệu giúp bù các xấp xỉ chưa hoàn hảo của mô hình lý thuyết.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hóa học và Trí tuệ nhân tạo — dự đoán trong không gian hóa học**, **Giải thích phổ** nêu điều cần giải thích; **Độ không đảm bảo và dữ liệu ngoài miền** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình có thông tin vật lý** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ không đảm bảo và dữ liệu ngoài miền

Không gian hóa học rất không đồng nhất. Một mô hình huấn luyện chủ yếu trên các phân tử hữu cơ giống thuốc có thể hoạt động kém với hợp chất cơ kim, trạng thái điện tích bất thường hoặc vật liệu vô cơ.

Đây là bài toán **ngoài miền phân bố (out-of-distribution, OOD)**. Vì vậy một dự đoán tốt phải đi kèm phạm vi áp dụng, chỉ báo độ không đảm bảo và kiểm chứng trên dữ liệu thật sự độc lập.

Mô hình không biết mình không biết là một rủi ro lớn hơn mô hình có sai số trung bình hơi cao nhưng biết báo độ không chắc chắn.

> **Chuyển mạch:** Trong **Hóa học và Trí tuệ nhân tạo — dự đoán trong không gian hóa học**, **Độ không đảm bảo và dữ liệu ngoài miền** nêu điều cần giải thích; **Mô hình có thông tin vật lý** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình có thông tin vật lý

Các mô hình **có thông tin vật lý (physics-informed)** đưa trực tiếp các ràng buộc như tính đối xứng, bảo toàn, tính tương đương quay–tịnh tiến hoặc cấu trúc năng lượng vào kiến trúc mô hình.

Điều này giúp giảm lượng dữ liệu cần thiết và hạn chế các dự đoán vi phạm vật lý. Với dữ liệu phân tử ba chiều, các mạng có tính tương đương hình học (**equivariant networks**) đặc biệt hữu ích vì kết quả vật lý không nên thay đổi tùy cách xoay hệ tọa độ.

> **Chuyển mạch:** Ở chặng này của **Hóa học và Trí tuệ nhân tạo — dự đoán trong không gian hóa học**, **Mô hình tư duy** gom các mảnh từ **Mô hình có thông tin vật lý** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

AI trong Hóa học nên được xem như **một bản đồ học từ dữ liệu trên không gian hóa học**, không phải sự thay thế cho định luật hóa học. Bản đồ đó chỉ đáng tin khi vùng cần dự đoán có đủ bằng chứng huấn luyện, biểu diễn phù hợp và các ràng buộc vật lý–hóa học được tôn trọng.

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
