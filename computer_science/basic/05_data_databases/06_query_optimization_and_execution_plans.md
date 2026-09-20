# Tối ưu truy vấn và kế hoạch thực thi

Hai câu SQL có thể trả cùng kết quả nhưng thời gian chạy chênh nhau hàng nghìn lần. **Bộ tối ưu truy vấn (query optimizer / 옵티마이저)** của cơ sở dữ liệu phải tìm một kế hoạch thực thi vật lý có chi phí ước lượng thấp trong một không gian phương án rất lớn. Đây là nơi thuật toán, thống kê, lưu trữ, cache CPU và đại số quan hệ gặp nhau.

## Từ câu SQL đến kế hoạch vật lý

Luồng xử lý khái quát:

```text
phân tích SQL
→ liên kết tên và kiểu dữ liệu
→ tạo kế hoạch logic
→ biến đổi biểu thức logic
→ liệt kê các phương án vật lý
→ ước lượng chi phí
→ chọn kế hoạch
→ thực thi các toán tử
```

Bộ tối ưu không “hiểu ý nghĩa nghiệp vụ”. Nó dựa vào lược đồ, ràng buộc, số liệu thống kê và mô hình chi phí.

## Ước lượng số lượng bản ghi là trung tâm của mô hình chi phí

Nếu bộ tối ưu dự đoán một điều kiện lọc chỉ trả 10 dòng nhưng thực tế trả 10 triệu dòng, thứ tự nối bảng và thuật toán nối có thể trở nên hoàn toàn không phù hợp.

Số liệu thống kê thường gồm số dòng, số giá trị khác nhau, biểu đồ phân bố (histogram), tỷ lệ `NULL` và đôi khi có thống kê mở rộng cho nhiều cột.

Giả định các cột độc lập thường sai. `city='Seoul'` và `country='KR'` có tương quan mạnh; nếu nhân độ chọn lọc của hai điều kiện như thể chúng độc lập, hệ thống có thể ước lượng quá thấp hoặc quá cao.

## Số phương án thứ tự nối tăng rất nhanh

Khi có nhiều bảng, số thứ tự nối có thể tăng bùng nổ. Tìm kiếm toàn bộ nhanh chóng trở nên không khả thi, nên bộ tối ưu thường dùng quy hoạch động cho tập nối nhỏ, kết hợp với kinh nghiệm (heuristic) hoặc giới hạn không gian tìm kiếm.

Tính kết hợp của phép nối cho phép `(A join B) join C` và `A join (B join C)` tương đương với phép nối trong (inner join) khi các điều kiện phù hợp, nhờ đó tạo không gian cho tối ưu. Phép nối ngoài, phụ thuộc `LATERAL` và hàm có hành vi thay đổi theo lần gọi làm giảm mức tự do này.

## Các toán tử thực thi vật lý

**Nested-loop join** phù hợp khi phía ngoài nhỏ và phía trong có chỉ mục chọn lọc tốt. **Hash join** thường hiệu quả cho phép nối bằng khi phía dựng bảng băm vừa với bộ nhớ. **Sort-merge join** hữu ích khi dữ liệu đầu vào đã có thứ tự hoặc kết quả sắp xếp còn được dùng ở bước sau.

Quét tuần tự (sequential scan) có thể nhanh hơn quét chỉ mục khi truy vấn cần phần lớn bảng, vì chi phí truy cập trang ngẫu nhiên và tra cứu chỉ mục có thể lớn hơn lợi ích của chỉ mục.

Không có toán tử “tốt nhất” cho mọi trường hợp; lựa chọn phụ thuộc số lượng bản ghi, thứ tự dữ liệu, bộ nhớ và đặc tính thiết bị lưu trữ.

## Điều kiện có thể tận dụng chỉ mục

Một điều kiện **có khả năng tìm kiếm bằng chỉ mục (SARGable)** cho phép cơ sở dữ liệu sử dụng đường truy cập chỉ mục hiệu quả hơn. Ví dụ `WHERE created_at >= ?` thường thuận lợi hơn `WHERE function(created_at) = ?` nếu hệ quản trị không có chỉ mục biểu thức tương ứng.

Bản chất là khi biến đổi trực tiếp cột trong điều kiện, thứ tự khóa của chỉ mục có thể không còn được sử dụng trực tiếp.

## Chỉ mục bao phủ và quét chỉ mục không cần đọc bảng

Nếu chỉ mục chứa đủ các cột mà truy vấn cần, hệ thống có thể tránh quay lại bảng cho nhiều dòng. **Chỉ mục bao phủ (covering index)** vì vậy có thể thay đổi đáng kể kiểu I/O.

Tuy nhiên chỉ mục rộng tốn thêm dung lượng và làm tăng khuếch đại ghi (write amplification). Mỗi lần `INSERT` hoặc `UPDATE` phải duy trì các chỉ mục liên quan, nên tối ưu đọc luôn có chi phí ở phía ghi.

## Sắp xếp, tràn ra đĩa và hạn mức bộ nhớ

Các toán tử sắp xếp hoặc băm cần bộ nhớ. Nếu tập dữ liệu vượt phần bộ nhớ được cấp, hệ thống phải **tràn (spill)** dữ liệu ra vùng lưu trữ tạm và độ trễ có thể tăng mạnh.

Một truy vấn đột nhiên chậm khi dữ liệu vượt ngưỡng bộ nhớ là ví dụ về thay đổi pha: kế hoạch logic không đổi nhưng hành vi vật lý thay đổi vì giới hạn tài nguyên.

## EXPLAIN là bằng chứng, không phải phần trang trí

Kế hoạch thực thi cho thấy cây toán tử, số dòng và chi phí ước lượng; ở chế độ `ANALYZE`, nhiều hệ quản trị còn cho biết số dòng và thời gian thực tế.

Một quy trình gỡ lỗi tốt là tìm nơi số liệu ước lượng lệch xa thực tế, sau đó xem đường truy cập, thứ tự nối, điều kiện lọc, sắp xếp và hiện tượng spill trước khi quyết định thêm chỉ mục, viết lại SQL hoặc cập nhật thống kê.

Không nên tối ưu chỉ bằng cách nhìn câu SQL và đoán.

## Độ nhạy với tham số

Một truy vấn chuẩn bị sẵn có thể nhận các giá trị tham số có độ chọn lọc rất khác nhau. Kế hoạch tốt cho giá trị phổ biến có thể rất tệ cho giá trị hiếm và ngược lại. Các DBMS có cơ chế khác nhau như `parameter sniffing`, kế hoạch chung/kế hoạch riêng hoặc kế hoạch thích nghi để xử lý vấn đề này.

Điều đó cho thấy “một truy vấn luôn có một kế hoạch tối ưu duy nhất” không đúng khi tham số và phân bố dữ liệu thay đổi.

## Những hiểu nhầm thường gặp

**“Có chỉ mục thì cơ sở dữ liệu chắc chắn sẽ dùng.”** Không đúng. Bộ tối ưu có thể đúng khi chọn quét bảng nếu tổng chi phí thấp hơn.

**“Cost trong EXPLAIN là mili-giây.”** Thường không đúng. Đây thường là đơn vị chi phí nội bộ, không phải thời gian thực trực tiếp.

**“Viết lại SQL trông đẹp hơn thì chắc chắn nhanh hơn.”** Không đúng. Bộ tối ưu có thể chuẩn hóa nhiều cách viết thành cùng một kế hoạch; cần kiểm tra kế hoạch và số liệu thực tế.

## Mô hình tư duy

> Tối ưu truy vấn là bài toán tìm kiếm dưới điều kiện không chắc chắn: bộ tối ưu dùng thống kê để dự đoán số lượng bản ghi, rồi chọn các toán tử có mô hình chi phí phù hợp. Ước lượng sai thường kéo theo kế hoạch sai.

## Kết nối

Đọc cùng [ngữ nghĩa SQL](./05_relational_algebra_and_sql_semantics.md), [chỉ mục và thực thi truy vấn](./03_indexes_and_query_execution.md), [phần cứng lưu trữ](../02_computer_architecture/06_storage_hardware_ssd_disks_and_persistence.md) và [hiệu năng hệ thống phần mềm](../08_software_systems/02_performance_capacity_and_scalability.md).