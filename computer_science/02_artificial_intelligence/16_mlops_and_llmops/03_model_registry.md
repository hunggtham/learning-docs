# Sổ đăng ký Mô hình và Thăng cấp Artifact

**Sổ đăng ký mô hình (Model Registry / 모델 레지스트리)** là nơi quản lý artifact mô hình cùng metadata và trạng thái vòng đời. Registry không chỉ là nơi lưu trữ. Nó trả lời mô hình nào là ứng viên, mô hình nào đã được kiểm định, mô hình nào đang chạy production và vì sao một artifact được thăng cấp.

## Artifact và Bản ghi Registry

Artifact có thể gồm các file:

```text
trọng số
cấu hình
tokenizer
preprocessor
ánh xạ nhãn
```

Bản ghi registry bổ sung metadata:

```text
mô hình / phiên bản
lần huấn luyện
SHA của mã nguồn
lineage dữ liệu
chỉ số
báo cáo đánh giá
người phụ trách
trạng thái phê duyệt
lịch sử triển khai
```

## Trạng thái vòng đời

Một luồng phổ biến:

```text
ứng viên
→ đã kiểm định
→ staging
→ production
→ ngừng khuyến nghị sử dụng
→ lưu trữ
```

Tên trạng thái có thể khác nhau giữa các tổ chức nhưng chuyển trạng thái nên được định nghĩa tường minh.

## Cổng thăng cấp

Việc thăng cấp (promotion) không nên chỉ dựa vào một chỉ số “cao hơn”. Cổng kiểm soát có thể kiểm tra:

- chỉ số của tác vụ;
- chỉ số theo subgroup;
- calibration;
- độ trễ và chi phí;
- độ bền vững trước nhiễu (robustness);
- kiểm thử an toàn;
- khả năng tương thích schema;
- phê duyệt pháp lý hoặc quản trị.

## Champion–Challenger

Mô hình production hiện tại là **champion**; ứng viên mới là **challenger**. Nên so sánh trên bộ đánh giá cố định và dữ liệu shadow/canary trước khi thay thế.

Mẫu này tránh tình trạng “checkpoint mới nhất tự động thắng”.

## Tách Registry khỏi Triển khai

Trạng thái registry kiểu `production-approved` không nhất thiết nghĩa artifact đã được triển khai ở mọi vùng. Nền tảng triển khai đọc artifact đã được phê duyệt rồi rollout theo từng môi trường.

Tách phê duyệt khỏi thực thi giúp rollback và audit rõ hơn.

## Artifact phải bất biến

Một phiên bản đã được đăng ký nên bất biến. Nếu cần sửa, tạo phiên bản mới.

Artifact có thể thay đổi làm lineage mất ý nghĩa.

## Khả năng tương thích

Registry nên lưu signature:

```text
schema đầu vào
schema đầu ra
đặc trưng bắt buộc
phiên bản tokenizer / preprocessor
dependency runtime
```

Cổng triển khai có thể phát hiện môi trường phục vụ không tương thích trước khi lỗi runtime xảy ra.

## Registry cho ứng dụng LLM

Với LLM được cung cấp qua dịch vụ (hosted LLM), artifact không nhất thiết là trọng số. Có thể cần registry cho toàn bộ **gói hành vi của ứng dụng (application bundle)**:

```text
model ID / version
system prompt
prompt template
cấu hình retrieval
mô hình embedding
reranker
schema của tool
graph của agent
chính sách an toàn
```

Phiên bản hành vi phải bao phủ toàn bộ bundle này.

## Rollback

Registry cần biết bản phát hành tốt gần nhất (previous known-good release). Rollback phải khôi phục cả cấu hình và dependency dữ liệu tương thích, không chỉ trọng số mô hình.

## Dấu vết kiểm toán

Ai đã thăng cấp? Khi nào? Dựa trên bằng chứng gì? Có ngoại lệ nào được phê duyệt?

Dấu vết kiểm toán (audit trail) hữu ích cho debugging và governance.

## Registry không nhất thiết chứa trực tiếp Binary lớn

Binary lớn thường nằm trong object storage; registry giữ reference và metadata. Về mặt khái niệm:

```text
Metadata registry → URI / hash của artifact bất biến
```

## Mô hình tư duy

```text
Thí nghiệm tạo artifact
Registry gán danh tính + bằng chứng + trạng thái vòng đời
Triển khai sử dụng artifact đã được phê duyệt
```

## Những nhầm lẫn thường gặp

### “Registry chỉ là thư mục model/”

Không. Thư mục không thể hiện tốt vòng đời, lineage và phê duyệt.

### “Production tag có thể đổi tùy ý mà không cần lịch sử”

Alias có thể thay đổi được, nhưng phiên bản bất biến phía dưới và lịch sử phải được giữ lại.

### “Dùng hosted API thì không cần registry”

Không. Hành vi của ứng dụng vẫn phụ thuộc mô hình, prompt và bundle cấu hình cần versioning.

## Liên kết kiến thức

Xem [Experiment Tracking](./01_experiment_tracking_and_reproducibility.md), [Data & Model Versioning](./02_data_and_model_versioning.md), [CI/CD/CT](./04_ci_cd_ct_for_ai.md) và [AI System Design](../15_ai_engineering/10_ai_system_design.md).