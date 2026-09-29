# Bộ tối ưu dựa trên chi phí, ước lượng số dòng và thống kê

> **Mạch đọc:** Đặt **Bộ tối ưu dựa trên chi phí, ước lượng số dòng và thống kê** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Không gian kế hoạch tăng rất nhanh** sang **Số lượng bản ghi là biến trung tâm**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


SQL mô tả **cần lấy kết quả gì**, không bắt buộc hệ quản trị phải thực hiện **bằng cách nào**. Cùng một truy vấn có thể nối bảng theo nhiều thứ tự, dùng quét chỉ mục hoặc quét tuần tự, dùng băm (hash / 해시) phép nối (join / 조인) hoặc nested-loop phép nối (join / 조인). **Bộ tối ưu dựa trên chi phí (Cost-Based Optimizer — CBO / 비용 기반 옵티마이저)** tìm kế hoạch có chi phí ước lượng thấp dựa trên thống kê và mô hình chi phí.

## Không gian kế hoạch tăng rất nhanh

Khi số bảng tăng, số thứ tự nối tăng theo kiểu tổ hợp. Bộ tối ưu không thể thử mọi kế hoạch cho truy vấn lớn, nên phải dùng quy hoạch động, kinh nghiệm tìm kiếm hoặc cắt tỉa không gian phương án.

Vì vậy tối ưu truy vấn bản thân cũng là một bài toán tìm kiếm thuật toán dưới giới hạn thời gian.


> **Chuyển mạch:** Từ **Không gian kế hoạch tăng rất nhanh**, ta sang **Số lượng bản ghi là biến trung tâm** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Số lượng bản ghi là biến trung tâm

Nếu bộ tối ưu nghĩ một điều kiện lọc trả 10 dòng nhưng thực tế trả 10 triệu, nhiều quyết định phía sau có thể sai. Nested-loop phép nối (join / 조인) hợp lý khi phía ngoài nhỏ có thể trở thành thảm họa khi phía ngoài rất lớn.

**Ước lượng số lượng bản ghi (cardinality estimation)** cố dự đoán số dòng sau quét, lọc hoặc nối. Thống kê thường gồm tổng số dòng, số giá trị khác nhau, histogram, tỷ lệ `NULL` và thông tin tương quan.


> **Chuyển mạch:** Từ **Số lượng bản ghi là biến trung tâm**, ta sang **Giả định độc lập** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Giả định độc lập

Một nguồn sai số phổ biến là giả định các điều kiện độc lập. Nếu `city='Seoul'` và `country='KR'` có tương quan mạnh, nhân hai độ chọn lọc như thể độc lập sẽ làm ước lượng quá thấp hoặc quá cao.

Thống kê nhiều cột giúp giảm vấn đề nhưng không thể nắm mọi phụ thuộc trong dữ liệu.


> **Chuyển mạch:** Từ **Giả định độc lập**, ta sang **Mô hình chi phí** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình chi phí

“chi phí (cost / 비용)” trong bộ tối ưu thường không phải số mili-giây chính xác. Nó là mô hình tương đối kết hợp chi phí I/O, CPU, truy cập ngẫu nhiên/tuần tự và đôi khi cả mức song song. Phần cứng mới, trạng thái bộ nhớ đệm (cache / 캐시) hoặc lưu trữ đám mây có thể khiến các hằng số mặc định lệch khỏi thực tế.

Bộ tối ưu chỉ cần mô hình đủ tốt để xếp hạng các kế hoạch, không cần dự đoán chính xác tuyệt đối độ trễ.


> **Chuyển mạch:** Từ **Mô hình chi phí**, ta sang **Khả năng tận dụng chỉ mục** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Khả năng tận dụng chỉ mục

Một điều kiện **có khả năng tìm kiếm bằng chỉ mục (SARGable)** cho phép hệ quản trị biến nó thành điều kiện truy cập phù hợp. Hàm bao quanh cột đã đánh chỉ mục, ép kiểu ngầm hoặc biểu thức phức tạp có thể làm chỉ mục khó sử dụng tùy DBMS.

Hiểu SARGability hữu ích hơn việc học thuộc mẹo “hãy đánh chỉ mục (index / 인덱스) cột này”, vì nó giải thích đường truy cập nào thật sự tồn tại trong không gian kế hoạch.


> **Chuyển mạch:** Từ **Khả năng tận dụng chỉ mục**, ta sang **Độ nhạy với tham số** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Độ nhạy với tham số

Prepared statement có tham số với phân bố dữ liệu lệch có thể cần kế hoạch khác nhau cho các giá trị khác nhau. Kế hoạch tối ưu cho giá trị hiếm không nhất thiết phù hợp với giá trị xuất hiện rất nhiều.

Các DBMS xử lý bằng kế hoạch chung/riêng, bind peeking hoặc cơ chế thích nghi khác nhau. Đây là một nguồn của hiện tượng “cùng câu SQL nhưng lúc nhanh lúc chậm”.


> **Chuyển mạch:** Từ **Độ nhạy với tham số**, ta sang **Thống kê cũ** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Thống kê cũ

Phân bố dữ liệu thay đổi nhưng thống kê chưa cập nhật sẽ làm bộ ước lượng sai. Cơ chế tự động phân tích giúp giảm vấn đề, nhưng bảng rất lớn, dữ liệu thay đổi nhanh và cột có tương quan vẫn cần chẩn đoán.

Khi đọc kế hoạch thực thi, nên so số dòng ước lượng với số dòng thực tế ở từng toán tử. Sai lệch xuất hiện sớm thường lan truyền xuống phần còn lại của kế hoạch.


> **Chuyển mạch:** Từ **Thống kê cũ**, ta sang **Bộ tối ưu và thiết kế chỉ mục** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bộ tối ưu và thiết kế chỉ mục

Chỉ mục không chỉ giảm chi phí tra cứu; nó thay đổi không gian kế hoạch, thứ tự dữ liệu và các phương án nối. Thứ tự cột trong chỉ mục ghép nên phản ánh kiểu truy cập, độ chọn lọc và yêu cầu sắp xếp, thay vì áp dụng máy móc quy tắc “cột chọn lọc nhất luôn đứng trước”.


> **Chuyển mạch:** Từ **Bộ tối ưu và thiết kế chỉ mục**, ta sang **Mô hình tư duy** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy

> Bộ tối ưu truy vấn là một bộ lập kế hoạch ra quyết định dưới điều kiện không chắc chắn. Thống kê là dữ liệu quan sát, ước lượng cardinality là niềm tin về kích thước trung gian, mô hình chi phí là cách đánh giá phương án và kế hoạch thực thi là hành động được chọn. Khi kế hoạch xấu, hãy tìm xem ước lượng sai ở đâu trước khi ép hint.

> **Bàn giao:** Sau **Mô hình tư duy**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 mvcc visibility wal and recovery internals](./00_mvcc_visibility_wal_and_recovery_internals.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
