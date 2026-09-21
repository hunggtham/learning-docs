# Version hóa Dữ liệu và Mô hình

Một hệ thống ML chỉ có thể tái lập tốt khi **dữ liệu, mã nguồn và artifact mô hình đều có danh tính rõ ràng**. Git quản lý mã nguồn rất tốt, nhưng tập dữ liệu lớn, bảng có thể thay đổi và đặc trưng được sinh tự động cần cơ chế versioning và lineage riêng.

## Phiên bản dữ liệu là gì?

Một phiên bản dữ liệu có thể được biểu diễn bằng:

```text
file bất biến + checksum
snapshot của kho dữ liệu theo thời điểm
truy vấn + phiên bản bảng nguồn
snapshot bảng Delta/Iceberg
manifest của các object ID
```

Điểm cốt lõi là phải xác định lại chính xác tập dữ liệu huấn luyện hoặc đánh giá đã được dùng.

## Dữ liệu có thể thay đổi nguy hiểm ở đâu?

Nếu truy vấn `SELECT * FROM transactions` hôm nay và một tháng sau trả về nội dung khác nhau thì cùng mã nguồn/cấu hình vẫn tạo ra hai run không còn so sánh trực tiếp được.

Cần snapshot hoặc manifest theo thời điểm (point-in-time manifest) để đóng băng danh tính dữ liệu.

## Dòng nguồn gốc của tập dữ liệu

Lineage cần trả lời được:

```text
nguồn thô nào?
phép biến đổi nào?
bộ lọc nào?
phiên bản logic gán nhãn nào?
mã nguồn đặc trưng nào?
tập dữ liệu đầu ra nào?
mô hình nào dùng tập dữ liệu đó?
```

Lineage hai chiều hỗ trợ phân tích ảnh hưởng (impact analysis): nếu một bảng nguồn thay đổi, những mô hình nào sẽ bị ảnh hưởng?

## Version hóa Schema

Sự tiến hóa schema cần hợp đồng rõ. Đổi tên cột, đổi đơn vị hoặc đổi semantics có thể không gây lỗi cú pháp nhưng vẫn phá mô hình một cách âm thầm.

Nên theo dõi cả metadata ngữ nghĩa như đơn vị, múi giờ, encoding và khoảng giá trị hợp lệ.

## Version hóa đặc trưng

Một định nghĩa đặc trưng (feature definition) thực chất gồm mã nguồn, dependency dữ liệu và semantics theo thời gian.

Ví dụ `avg_spend_30d` phải xác định rõ cửa sổ thời gian, múi giờ, loại giao dịch bị loại và thời điểm cutoff.

Tính nhất quán giữa huấn luyện và phục vụ yêu cầu logic đặc trưng online tương thích với định nghĩa offline.

## Phiên bản Artifact của mô hình

Phiên bản mô hình không chỉ là trọng số. Gói artifact nên gắn cùng:

```text
trọng số
cấu hình kiến trúc
tokenizer / preprocessor
ánh xạ nhãn
yêu cầu runtime
signature / schema đầu vào
training run ID
báo cáo đánh giá
```

Với ứng dụng LLM hoặc RAG còn cần phiên bản prompt và cấu hình truy xuất.

## Phiên bản ngữ nghĩa và ID bất biến

Hash bất biến hoặc run ID phù hợp cho truy vết. Phiên bản phát hành dễ đọc phù hợp cho giao tiếp giữa con người.

Có thể dùng cả hai:

```text
release: fraud-model-3.2
artifact sha: abc123...
```

## Checksum dữ liệu

Checksum phát hiện thay đổi ở mức byte nhưng không cho biết hai tập dữ liệu có tương đương về ngữ nghĩa hay không. Pipeline dữ liệu cần cả hash lẫn metadata.

## Tập dữ liệu lớn

Không nên sao chép toàn bộ tập dữ liệu cho mỗi thí nghiệm nếu chi phí lưu trữ quá lớn. Snapshot, manifest hoặc lưu trữ theo nội dung (content-addressed storage) có thể tái sử dụng các block không đổi.

## Quyền riêng tư và xóa dữ liệu

Versioning không có nghĩa giữ mọi dữ liệu vĩnh viễn. Yêu cầu xóa vì quyền riêng tư và chính sách lưu giữ phải được truyền qua snapshot, cache và lineage huấn luyện.

Trong một số trường hợp cần biết mô hình nào từng huấn luyện từ dữ liệu phải xóa để đánh giá việc huấn luyện lại hoặc biện pháp khắc phục.

## Đồ thị Mô hình–Dữ liệu

Một mô hình tư duy hữu ích:

```text
Dữ liệu nguồn
   ↓
Phiên bản tập dữ liệu
   ↓
Phiên bản đặc trưng
   ↓
Lần huấn luyện
   ↓
Artifact mô hình
   ↓
Đánh giá
   ↓
Triển khai
```

Mỗi cạnh trong graph cần metadata có thể truy vết.

## Những nhầm lẫn thường gặp

### “Git LFS là đủ cho version hóa dữ liệu”

Có thể đủ với tập dữ liệu nhỏ và ít thay đổi, nhưng snapshot kho dữ liệu hoặc lineage quy mô lớn cần abstraction khác.

### “Phiên bản mô hình chỉ là tên checkpoint”

Không. Tokenizer, schema và cấu hình cũng là một phần của mô hình có thể thực thi.

### “Càng nhiều snapshot càng tốt”

Không. Chi phí lưu trữ, thời hạn lưu giữ và ràng buộc quyền riêng tư cần được cân bằng.

## Liên kết kiến thức

Xem [Experiment Tracking](./01_experiment_tracking_and_reproducibility.md), [Data Governance](../14_data_for_ai/08_data_governance.md), [Model Registry](./03_model_registry.md).