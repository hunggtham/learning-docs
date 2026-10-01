# Hóa học và Khoa học máy tính — phân tử như dữ liệu và hệ mô phỏng

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Hóa học và Khoa học máy tính — phân tử như dữ liệu và hệ mô phỏng**. Route đi từ graph/SMILES và chuẩn hóa dữ liệu → tìm kiếm cấu trúc con → mô phỏng lượng tử/động lực học → pipeline tính toán và reproducibility, để mỗi kết quả máy tính giữ được ý nghĩa hóa học và provenance.

> Hóa học ngày càng phụ thuộc vào tính toán vì không gian phân tử, mạng phản ứng và trạng thái lượng tử quá lớn để xử lý hoàn toàn bằng suy luận thủ công. Khoa học máy tính cung cấp cách biểu diễn, tìm kiếm, mô phỏng và tự động hóa; Hóa học cung cấp các ràng buộc miền để những phép tính đó vẫn có ý nghĩa vật lý.

## Biểu diễn phân tử

Một phân tử có thể được biểu diễn như một **đồ thị (graph / 그래프)**: nguyên tử là nút, liên kết là cạnh. Tuy nhiên đồ thị hóa học cần thêm nhiều thuộc tính như nguyên tố, điện tích, bậc liên kết, tính thơm và thông tin lập thể.

`SMILES` mã hóa cấu trúc phân tử thành chuỗi ký tự, còn `InChI` hướng tới biểu diễn định danh chuẩn hóa. Việc chuẩn hóa không hề đơn giản vì cùng một đồ thị có thể được duyệt theo nhiều thứ tự và sinh ra nhiều chuỗi khác nhau nếu không có quy tắc chuẩn.

Đây là lý do biểu diễn phân tử là bài toán khoa học máy tính thật sự, không chỉ là đổi hình vẽ thành văn bản.

> **Chuyển mạch:** Trong **Hóa học và Khoa học máy tính — phân tử như dữ liệu và hệ mô phỏng**, **Tìm kiếm cấu trúc con** tiếp nhận điểm tựa từ **Biểu diễn phân tử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hóa học tính toán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tìm kiếm cấu trúc con

Cơ sở dữ liệu hóa học sử dụng thuật toán đồ thị để tìm motif hoặc cấu trúc con. Tuy nhiên tìm khớp đồ thị chính xác có thể tốn chi phí tính toán, nên hệ thống thường dùng **dấu vân tay phân tử (molecular fingerprint)** để mã hóa đặc trưng cấu trúc thành véc-tơ (vector / 벡터) hoặc chuỗi bit.

Các fingerprint giúp tìm tương đồng rất nhanh, nhưng độ tương đồng phụ thuộc cách biểu diễn. Hai phân tử có fingerprint gần nhau không đảm bảo có cùng hoạt tính sinh học hoặc cùng cơ chế phản ứng.

> **Chuyển mạch:** Ở chặng này của **Hóa học và Khoa học máy tính — phân tử như dữ liệu và hệ mô phỏng**, **Hóa học tính toán** tiếp nhận điểm tựa từ **Tìm kiếm cấu trúc con** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Động học số** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hóa học tính toán

Hóa học lượng tử tìm nghiệm gần đúng cho phương trình Schrödinger điện tử. Các phương pháp như Hartree–Fock, hậu Hartree–Fock và lý thuyết phiếm hàm mật độ (**Density Functional Theory, DFT**) đánh đổi giữa độ chính xác và chi phí tính toán.

**Động lực học phân tử (molecular dynamics)** mô phỏng quỹ đạo nguyên tử theo thời gian dựa trên trường lực hoặc tính toán cấu trúc điện tử. Nó cho phép nghiên cứu chuyển động, khuếch tán, gấp cuộn và dao động thay vì chỉ nhìn một cấu trúc tĩnh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hóa học và Khoa học máy tính — phân tử như dữ liệu và hệ mô phỏng**, **Động học số** tiếp nhận điểm tựa từ **Hóa học tính toán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hóa tin học** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Động học số

Một mạng phản ứng có thể được chuyển thành hệ phương trình vi phân thường:

\[
\frac{d\mathbf c}{dt}=\mathbf f(\mathbf c,T)
\]

Nếu tốc độ các phản ứng khác nhau qua nhiều bậc độ lớn, hệ trở thành bài toán **cứng (stiff system)** và cần bộ giải số chuyên dụng.

Cơ chế cháy, hóa học khí quyển và chuyển hóa sinh học có thể chứa từ hàng trăm tới hàng nghìn phản ứng, nên mô phỏng số là cách duy nhất thực tế để theo dõi toàn mạng.

> **Chuyển mạch:** Trong **Hóa học và Khoa học máy tính — phân tử như dữ liệu và hệ mô phỏng**, **Hóa tin học** tiếp nhận điểm tựa từ **Động học số** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Máy học** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hóa tin học

**Hóa tin học (cheminformatics)** kết nối cấu trúc, tính chất, phản ứng và dữ liệu phổ trong cơ sở dữ liệu có thể truy vấn.

Những bài toán tưởng như thuần phần mềm như loại bản ghi trùng, chuẩn hóa tautomer, xử lý điện tích, lập thể hay ánh xạ nguyên tử trong phản ứng đều cần hiểu hóa học miền. Làm sạch dữ liệu hóa học vì vậy là một dạng kỹ thuật dữ liệu có tri thức chuyên ngành.

> **Chuyển mạch:** Ở chặng này của **Hóa học và Khoa học máy tính — phân tử như dữ liệu và hệ mô phỏng**, **Máy học** tiếp nhận điểm tựa từ **Hóa tin học** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tự động hóa phòng thí nghiệm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Máy học

Mô hình máy học có thể dự đoán độ tan, độc tính, phổ, hiệu suất phản ứng, tương tác protein–ligand hoặc tính chất vật liệu.

**Mạng nơ-ron đồ thị (Graph Neural network, GNN)** phù hợp tự nhiên với cấu trúc phân tử dạng đồ thị. Mô hình Transformer có thể làm việc với `SMILES`, chuỗi phản ứng hoặc mô tả văn bản.

Tuy nhiên hiệu năng luôn phụ thuộc độ lệch dữ liệu, phạm vi miền và độ đúng vật lý. Dự đoán thống kê không thay thế kiểm chứng thực nghiệm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hóa học và Khoa học máy tính — phân tử như dữ liệu và hệ mô phỏng**, **Tự động hóa phòng thí nghiệm** tiếp nhận điểm tựa từ **Máy học** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khả năng tái lập** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tự động hóa phòng thí nghiệm

Robot tổng hợp, bộ lấy mẫu tự động và hệ thống quản lý thông tin phòng thí nghiệm (**Laboratory information Management system, LIMS**) giúp biến thí nghiệm thành dòng dữ liệu có cấu trúc.

Trong **hệ vòng kín (closed-loop system)**, thuật toán đề xuất điều kiện tiếp theo, robot thực hiện thí nghiệm, thiết bị đo kết quả rồi dữ liệu quay lại mô hình để quyết định bước kế tiếp.

Đây là điểm giao giữa phần mềm, điều khiển, tối ưu hóa và Hóa học thực nghiệm.

> **Chuyển mạch:** Trong **Hóa học và Khoa học máy tính — phân tử như dữ liệu và hệ mô phỏng**, **Khả năng tái lập** tiếp nhận điểm tựa từ **Tự động hóa phòng thí nghiệm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khả năng tái lập

Mã nguồn có kiểm soát phiên bản, môi trường phần mềm được cố định, kiểm thử đơn vị, dữ liệu máy đọc được và lưu đầy đủ tham số mô phỏng quan trọng với Hóa học tính toán không kém sổ tay phòng thí nghiệm trong Hóa học thực nghiệm.

Một kết quả không thể tái tạo khi thiếu phiên bản phần mềm, bộ tham số hoặc dữ liệu đầu vào thì vẫn là kết quả khó kiểm chứng, dù thuật toán có phức tạp đến đâu.

> **Chuyển mạch:** Ở chặng này của **Hóa học và Khoa học máy tính — phân tử như dữ liệu và hệ mô phỏng**, **Mô hình tư duy** gom các mảnh từ **Khả năng tái lập** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

Khoa học máy tính cung cấp cho Hóa học **biểu diễn, tìm kiếm, mô phỏng và tự động hóa**. Hóa học cung cấp các định luật, ràng buộc và ngữ nghĩa giúp những phép tính đó không trở thành thao tác dữ liệu thuần túy.

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
