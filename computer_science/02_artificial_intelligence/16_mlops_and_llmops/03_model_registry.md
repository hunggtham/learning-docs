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

> **Chuyển mạch:** Trong **Sổ đăng ký Mô hình và Thăng cấp sản phẩm tạo ra (artifact / 산출물)**, **Trạng thái vòng đời** tiếp nhận điểm tựa từ **Sản phẩm tạo ra (artifact / 산출물) và Bản ghi Registry** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cổng thăng cấp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Sổ đăng ký Mô hình và Thăng cấp sản phẩm tạo ra (artifact / 산출물)**, **Cổng thăng cấp** tiếp nhận điểm tựa từ **Trạng thái vòng đời** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Champion–Challenger** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sổ đăng ký Mô hình và Thăng cấp sản phẩm tạo ra (artifact / 산출물)**, **Champion–Challenger** tiếp nhận điểm tựa từ **Cổng thăng cấp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tách Registry khỏi Triển khai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Champion–Challenger

Mô hình môi trường vận hành (production / 운영 환경) hiện tại là **champion**; ứng viên mới là **challenger**. Nên so sánh trên bộ đánh giá cố định và dữ liệu shadow/canary trước khi thay thế.

Mẫu này tránh tình trạng “checkpoint mới nhất tự động thắng”.

> **Chuyển mạch:** Trong **Sổ đăng ký Mô hình và Thăng cấp sản phẩm tạo ra (artifact / 산출물)**, **Tách Registry khỏi Triển khai** tiếp nhận điểm tựa từ **Champion–Challenger** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sản phẩm tạo ra (artifact / 산출물) phải bất biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tách Registry khỏi Triển khai

Trạng thái registry kiểu `production-approved` không nhất thiết nghĩa sản phẩm tạo ra (artifact / 산출물) đã được triển khai ở mọi vùng. Nền tảng triển khai đọc sản phẩm tạo ra (artifact / 산출물) đã được phê duyệt rồi rollout theo từng môi trường.

Tách phê duyệt khỏi thực thi giúp quay lui (rollback / 롤백) và kiểm tra (audit / 감사) rõ hơn.

> **Chuyển mạch:** Ở chặng này của **Sổ đăng ký Mô hình và Thăng cấp sản phẩm tạo ra (artifact / 산출물)**, **Sản phẩm tạo ra (artifact / 산출물) phải bất biến** tiếp nhận điểm tựa từ **Tách Registry khỏi Triển khai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khả năng tương thích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sản phẩm tạo ra (artifact / 산출물) phải bất biến

Một phiên bản đã được đăng ký nên bất biến. Nếu cần sửa, tạo phiên bản mới.

Sản phẩm tạo ra (artifact / 산출물) có thể thay đổi làm lineage mất ý nghĩa.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sổ đăng ký Mô hình và Thăng cấp sản phẩm tạo ra (artifact / 산출물)**, **Khả năng tương thích** tiếp nhận điểm tựa từ **Sản phẩm tạo ra (artifact / 산출물) phải bất biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Registry cho ứng dụng LLM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Sổ đăng ký Mô hình và Thăng cấp sản phẩm tạo ra (artifact / 산출물)**, **Registry cho ứng dụng LLM** tiếp nhận điểm tựa từ **Khả năng tương thích** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quay lui (rollback / 롤백)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Sổ đăng ký Mô hình và Thăng cấp sản phẩm tạo ra (artifact / 산출물)**, **Quay lui (rollback / 롤백)** tiếp nhận điểm tựa từ **Registry cho ứng dụng LLM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dấu vết kiểm toán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quay lui (rollback / 롤백)

Registry cần biết bản phát hành tốt gần nhất (previous known-good release). quay lui (rollback / 롤백) phải khôi phục cả cấu hình và phụ thuộc (dependency / 의존성) dữ liệu tương thích, không chỉ trọng số mô hình.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sổ đăng ký Mô hình và Thăng cấp sản phẩm tạo ra (artifact / 산출물)**, **Dấu vết kiểm toán** tiếp nhận điểm tựa từ **Quay lui (rollback / 롤백)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Registry không nhất thiết chứa trực tiếp nhị phân (binary / 이진) lớn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dấu vết kiểm toán

Ai đã thăng cấp? Khi nào? Dựa trên bằng chứng gì? Có ngoại lệ nào được phê duyệt?

Dấu vết kiểm toán (audit trail) hữu ích cho debugging và quản trị (governance / 거버넌스).

> **Chuyển mạch:** Trong **Sổ đăng ký Mô hình và Thăng cấp sản phẩm tạo ra (artifact / 산출물)**, **Registry không nhất thiết chứa trực tiếp nhị phân (binary / 이진) lớn** tiếp nhận điểm tựa từ **Dấu vết kiểm toán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Registry không nhất thiết chứa trực tiếp nhị phân (binary / 이진) lớn

Nhị phân (binary / 이진) lớn thường nằm trong đối tượng (object / 객체) lưu trữ (storage / 저장소); registry giữ tham chiếu (reference / 참조) và siêu dữ liệu (metadata / 메타데이터). Về mặt khái niệm:

```text
Metadata registry → URI / hash của artifact bất biến
```

> **Chuyển mạch:** Ở chặng này của **Sổ đăng ký Mô hình và Thăng cấp sản phẩm tạo ra (artifact / 산출물)**, **Mô hình tư duy** gom các mảnh từ **Registry không nhất thiết chứa trực tiếp nhị phân (binary / 이진) lớn** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Thí nghiệm tạo artifact
Registry gán danh tính + bằng chứng + trạng thái vòng đời
Triển khai sử dụng artifact đã được phê duyệt
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sổ đăng ký Mô hình và Thăng cấp sản phẩm tạo ra (artifact / 산출물)**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Registry chỉ là thư mục mô hình (model / 모델)/”

Không. Thư mục không thể hiện tốt vòng đời, lineage và phê duyệt.

### “môi trường vận hành (production / 운영 환경) tag có thể đổi tùy ý mà không cần lịch sử”

Alias có thể thay đổi được, nhưng phiên bản bất biến phía dưới và lịch sử phải được giữ lại.

### “Dùng hosted API thì không cần registry”

Không. Hành vi của ứng dụng vẫn phụ thuộc mô hình, prompt và bundle cấu hình cần versioning.

> **Chuyển mạch:** Trong **Sổ đăng ký Mô hình và Thăng cấp sản phẩm tạo ra (artifact / 산출물)**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Experiment Tracking](./01_experiment_tracking_and_reproducibility.md), [Data & Model Versioning](./02_data_and_model_versioning.md), [CI/CD/CT](./04_ci_cd_ct_for_ai.md) và [AI System Design](../15_ai_engineering/10_ai_system_design.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
