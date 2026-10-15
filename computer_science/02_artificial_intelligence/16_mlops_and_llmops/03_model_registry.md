# Sổ đăng ký Mô hình và Thăng cấp sản phẩm tạo ra (artifact / 산출물)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Model registry và artifact promotion**. Route đi từ immutable artifact → metadata/lineage → validation gates → lifecycle stages → deployment/rollback, để registry là điểm kiểm soát release chứ không chỉ là kho file.

**Sổ đăng ký mô hình (Model Registry / 모델 레지스트리)** là nơi quản lý sản phẩm tạo ra (artifact / 산출물) mô hình cùng siêu dữ liệu (metadata / 메타데이터) và trạng thái vòng đời. Registry không chỉ là nơi lưu trữ. Nó trả lời mô hình nào là ứng viên, mô hình nào đã được kiểm định, mô hình nào đang chạy môi trường vận hành (production / 운영 환경) và vì sao một sản phẩm tạo ra (artifact / 산출물) được thăng cấp.

## Sản phẩm tạo ra (artifact / 산출물) và Bản ghi Registry

Sản phẩm tạo ra (artifact / 산출물) có thể gồm các tệp (file / 파일):

```text
trọng số
cấu hình
tokenizer
preprocessor
ánh xạ nhãn
```

Bản ghi registry bổ sung siêu dữ liệu (metadata / 메타데이터):

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

Các trường này tạo nền cho việc theo dõi vòng đời: cùng một artifact phải cho biết nó đang ở trạng thái nào và đã vượt qua bằng chứng nào. Vì vậy, bước tiếp theo là làm rõ các trạng thái trước khi bàn đến điều kiện thăng cấp.

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

Trạng thái chỉ là nhãn mô tả; quyết định chuyển trạng thái cần một cổng thăng cấp với tiêu chí có thể kiểm tra. Sau khi xác định các tiêu chí đó, ta có thể so sánh ứng viên mới với mô hình đang phục vụ.

## Cổng thăng cấp

Việc thăng cấp (promotion) không nên chỉ dựa vào một chỉ số “cao hơn”. Cổng kiểm soát có thể kiểm tra:

- chỉ số của tác vụ;
- chỉ số theo subgroup;
- calibration;
- độ trễ và chi phí;
- độ bền vững trước nhiễu (robustness);
- kiểm thử an toàn;
- khả năng tương thích lược đồ (schema / 스키마);
- phê duyệt pháp lý hoặc quản trị.

So sánh champion–challenger giúp cổng thăng cấp dựa trên bằng chứng thay vì chỉ dựa vào số phiên bản mới nhất. Tuy nhiên, phê duyệt một artifact chưa đồng nghĩa đã triển khai nó ở mọi môi trường.

## Champion–Challenger

Mô hình môi trường vận hành (production / 운영 환경) hiện tại là **champion**; ứng viên mới là **challenger**. Nên so sánh trên bộ đánh giá cố định và dữ liệu shadow/canary trước khi thay thế.

Mẫu này tránh tình trạng “checkpoint mới nhất tự động thắng”.

Việc tách phê duyệt khỏi rollout làm rõ ai quyết định và môi trường nào đã nhận artifact. Để lịch sử đó còn đáng tin, chính artifact được tham chiếu phải giữ nguyên sau khi đăng ký.

## Tách Registry khỏi Triển khai

Trạng thái registry kiểu `production-approved` không nhất thiết nghĩa sản phẩm tạo ra (artifact / 산출물) đã được triển khai ở mọi vùng. Nền tảng triển khai đọc sản phẩm tạo ra (artifact / 산출물) đã được phê duyệt rồi rollout theo từng môi trường.

Tách phê duyệt khỏi thực thi giúp quay lui (rollback / 롤백) và kiểm tra (audit / 감사) rõ hơn.

Tính bất biến bảo vệ lineage, nhưng chưa đủ để bảo đảm artifact có thể chạy ở nơi nhận nó. Registry vì thế cũng cần lưu chữ ký tương thích của đầu vào, đầu ra và môi trường.

## Sản phẩm tạo ra (artifact / 산출물) phải bất biến

Một phiên bản đã được đăng ký nên bất biến. Nếu cần sửa, tạo phiên bản mới.

Sản phẩm tạo ra (artifact / 산출물) có thể thay đổi làm lineage mất ý nghĩa.

Signature giúp phát hiện lỗi tích hợp trước khi rollout. Với ứng dụng LLM, phần cần versioning còn rộng hơn trọng số mô hình, nên registry phải mô tả cả gói hành vi.

## Khả năng tương thích

Registry nên lưu signature:

```text
schema đầu vào
schema đầu ra
đặc trưng bắt buộc
phiên bản tokenizer / preprocessor
dependency runtime
```

Cổng triển khai có thể phát hiện môi trường phục vụ không tương thích trước khi lỗi thời gian chạy (runtime / 런타임) xảy ra.

Khi toàn bộ bundle được định danh cùng nhau, việc khôi phục một bản phát hành không còn phụ thuộc riêng vào model ID. Phần tiếp theo tập trung vào cách chọn và phục hồi bản phát hành tốt gần nhất.

## Registry cho ứng dụng LLM

Với LLM được cung cấp qua dịch vụ (hosted LLM), sản phẩm tạo ra (artifact / 산출물) không nhất thiết là trọng số. Có thể cần registry cho toàn bộ **gói hành vi của ứng dụng (application bundle)**:

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

Rollback chỉ đáng tin khi bản phát hành trước và các phụ thuộc đi kèm đã được ghi nhận đầy đủ. Do đó, mỗi lần quay lui cũng cần để lại dấu vết để người khác có thể giải thích quyết định.

## Quay lui (rollback / 롤백)

Registry cần biết bản phát hành tốt gần nhất (previous known-good release). quay lui (rollback / 롤백) phải khôi phục cả cấu hình và phụ thuộc (dependency / 의존성) dữ liệu tương thích, không chỉ trọng số mô hình.

Audit trail liên kết quyết định với artifact, người phê duyệt và bằng chứng cụ thể. Registry có thể làm việc đó mà không cần tự mình chứa toàn bộ nhị phân lớn.

## Dấu vết kiểm toán

Ai đã thăng cấp? Khi nào? Dựa trên bằng chứng gì? Có ngoại lệ nào được phê duyệt?

Dấu vết kiểm toán (audit trail) hữu ích cho debugging và quản trị (governance / 거버넌스).

Tham chiếu URI và hash cho phép kho lưu trữ đảm nhiệm dữ liệu lớn, còn registry giữ danh tính và bằng chứng. Từ các mảnh này, ta có thể tóm tắt registry như một điểm kiểm soát của vòng đời phát hành.

## Registry không nhất thiết chứa trực tiếp nhị phân (binary / 이진) lớn

Nhị phân (binary / 이진) lớn thường nằm trong đối tượng (object / 객체) lưu trữ (storage / 저장소); registry giữ tham chiếu (reference / 참조) và siêu dữ liệu (metadata / 메타데이터). Về mặt khái niệm:

```text
Metadata registry → URI / hash của artifact bất biến
```

Sơ đồ trên nhấn mạnh rằng registry nối thí nghiệm, bằng chứng và triển khai; nó không chỉ là thư mục lưu file. Ba hiểu lầm sau thường xuất hiện khi một trong các mối nối đó bị bỏ qua.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Thí nghiệm tạo artifact
Registry gán danh tính + bằng chứng + trạng thái vòng đời
Triển khai sử dụng artifact đã được phê duyệt
```

Các ví dụ này cùng nhắc lại một nguyên tắc: tên nhãn có thể thay đổi, nhưng phiên bản, bằng chứng và lịch sử phải truy nguyên được. Các liên kết dưới đây mở rộng nguyên tắc đó sang tracking, versioning và pipeline.

## Những nhầm lẫn thường gặp

### “Registry chỉ là thư mục mô hình (model / 모델)/”

Không. Thư mục không thể hiện tốt vòng đời, lineage và phê duyệt.

### “môi trường vận hành (production / 운영 환경) tag có thể đổi tùy ý mà không cần lịch sử”

Alias có thể thay đổi được, nhưng phiên bản bất biến phía dưới và lịch sử phải được giữ lại.

### “Dùng hosted API thì không cần registry”

Không. Hành vi của ứng dụng vẫn phụ thuộc mô hình, prompt và bundle cấu hình cần versioning.


## Liên kết kiến thức

Xem [Experiment Tracking](./01_experiment_tracking_and_reproducibility.md), [Data & Model Versioning](./02_data_and_model_versioning.md), [CI/CD/CT](./04_ci_cd_ct_for_ai.md) và [AI System Design](../15_ai_engineering/10_ai_system_design.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
