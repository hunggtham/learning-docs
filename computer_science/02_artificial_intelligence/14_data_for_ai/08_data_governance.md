# Quản trị Dữ liệu cho AI

**Quản trị dữ liệu (data governance / 데이터 거버넌스)** là hệ thống policy, ownership, metadata, access control và lifecycle management giúp tổ chức biết dữ liệu nào đang tồn tại, ai chịu trách nhiệm, dữ liệu được phép dùng cho mục đích gì và model nào đang phụ thuộc vào nó.

Governance không phải paperwork tách rời engineering. Khi AI dùng dữ liệu để train hoặc deploy, quản trị dữ liệu trở thành một phần trực tiếp của reliability, security và compliance.

## Ownership

Mỗi critical dataset hoặc source nên có owner rõ ràng, ví dụ:

```text
business / domain owner
technical data owner
data steward / quality owner
security / privacy contact
```

Nếu không ai chịu trách nhiệm cho semantics, feature definition và data contract rất dễ drift âm thầm theo thời gian.

## Data Catalog

**Danh mục dữ liệu (data catalog)** lưu metadata như:

- tên và mô tả dataset;
- schema;
- owner;
- source;
- freshness;
- lineage;
- privacy classification;
- permitted use;
- quality status;
- retention policy.

Catalog chỉ có giá trị khi metadata được duy trì và có thể tìm kiếm, không phải một tài liệu tĩnh bị bỏ quên.

## Data Lineage

Lineage có thể biểu diễn thành graph:

```text
source table / file
→ ETL / feature job
→ training snapshot
→ model version
→ deployment
```

Khi một field nguồn bị lỗi, lineage giúp trả lời model, experiment hoặc service nào bị ảnh hưởng.

## Access Control

Nguyên tắc **least privilege** cũng áp dụng cho dữ liệu:

```text
ai được đọc raw PII?
ai được export dữ liệu?
ai được train model?
ai được xem label nhạy cảm?
```

Role-based hoặc attribute-based access nên được enforce ở storage/service layer, không chỉ dựa trên quy ước xã hội hoặc prompt.

## Purpose Limitation

Dữ liệu được thu thập cho một mục đích không tự động trở nên hợp lệ cho mọi mục đích khác.

Governance cần ghi rõ permitted processing purpose và restriction. AI experimentation cũng phải tuân thủ cùng constraint như production.

## Phân loại Dữ liệu

Một số nhóm thường gặp:

```text
public
internal
confidential
personal data
sensitive personal data
secret / credential
regulated-domain data
```

Classification này quyết định encryption, retention, access và sharing policy.

## Encryption

Dữ liệu nên được bảo vệ:

- khi lưu trữ (at rest);
- khi truyền (in transit);
- bằng key management phù hợp;
- cùng access logging.

Encryption không ngăn được misuse bởi một user đã được cấp quyền; authorization và audit vẫn cần thiết.

## Retention và Deletion

Retention cần gắn với mục đích rõ ràng. Training snapshot thường muốn immutable để reproducibility, trong khi privacy hoặc compliance có thể yêu cầu deletion.

Model lifecycle vì vậy cần strategy cho data removal và retraining khi cần.

Xóa raw record không tự động xóa ảnh hưởng của record đó khỏi một model đã train.

## Provenance

Với dữ liệu bên ngoài, nên lưu:

- source URL hoặc provider;
- ngày thu thập;
- license và terms;
- transformation đã áp dụng;
- consent hoặc legal basis khi liên quan.

Trong thời đại foundation model, provenance ngày càng quan trọng cho copyright, trust và contamination analysis.

## Versioning cho Dataset

Một dataset version nên xác định được chính xác nội dung và processing configuration, không chỉ một nhãn semantic version chung chung.

Ví dụ:

```text
dataset_v42
manifest hash
source snapshot id
transform commit
label schema version
```

## Reproducibility

Để tái tạo một model, code là chưa đủ. Cần ít nhất:

```text
training data version
feature code
label version
random seed
model config
software environment
```

Governance cung cấp phần “data side” của reproducibility chain.

## Data Contract

Producer và consumer nên thống nhất schema, semantics, SLA và quy trình thay đổi.

Breaking change phải kích hoạt migration rõ ràng thay vì âm thầm làm downstream pipeline suy giảm.

## Privacy Impact

Trước khi dùng dữ liệu nhạy cảm, nên hỏi:

- feature này có thật sự cần thiết không?
- aggregate hoặc pseudonymized form có đủ không?
- có thể xử lý cục bộ thay vì gửi ra ngoài không?
- retention bao lâu?
- có cross-border transfer không?
- user có kỳ vọng dữ liệu được dùng theo cách này không?

Data minimization vừa giảm risk vừa giảm cơ hội để model học shortcut không mong muốn.

## Pseudonymization và Anonymization

Thay tên bằng ID là **pseudonymization**, không phải true anonymization.

Re-identification vẫn có thể xảy ra thông qua linkage hoặc auxiliary data. Dataset high-dimensional đặc biệt khó anonymize mà vẫn giữ utility cao.

## Differential Privacy

**Differential Privacy (DP)** cung cấp một bound toán học lên ảnh hưởng của từng record.

Một mechanism `M` là `(ε,δ)`-DP nếu với hai neighboring dataset `D` và `D'`:

\[
P(M(D)\in S)\le e^\epsilon P(M(D')\in S)+\delta
\]

`ε` nhỏ hơn thường nghĩa privacy mạnh hơn nhưng có thể làm utility giảm do cần thêm noise.

DP là một privacy mechanism toán học, không thay thế access control, encryption hoặc security operation.

## Data Residency

Một số tổ chức yêu cầu dữ liệu phải ở lại trong country hoặc region cụ thể.

Khi đó lựa chọn cloud, model provider và cross-region processing trở thành architecture constraint, không chỉ là quyết định hạ tầng.

## Dữ liệu từ Vendor

Dataset hoặc API bên thứ ba cần được đánh giá về:

- quyền sử dụng theo license;
- collection method;
- data quality;
- privacy commitment;
- retention;
- quyền dùng để train model;
- điều khoản thay đổi hoặc chấm dứt dịch vụ.

## Audit Log

Nên ghi lại ai đã access, export hoặc modify dataset nhạy cảm.

Audit log bản thân cũng là dữ liệu nhạy cảm và cần mức độ integrity phù hợp để có giá trị trong điều tra.

## Ứng phó Data Incident

Nếu dataset bị leak hoặc corrupt, quy trình có thể gồm:

1. cô lập access;
2. xác định data và model bị ảnh hưởng;
3. dùng lineage để tìm downstream artifact;
4. invalidate hoặc retrain khi cần;
5. bảo toàn evidence;
6. cập nhật control và regression test.

## Governance cho RAG

RAG index có thể ingest document với ACL khác nhau.

Retrieval phải enforce permission **trước khi** chunk đi vào model context. Không nên retrieve secret data rồi yêu cầu model “đừng tiết lộ”.

## Governance cho Agent Memory

Persistent memory có thể trở thành một data store mới. Nó cần retention, deletion, user scope, provenance và access control giống các database khác.

## Governance cho Synthetic Data

Nên lưu generator, model version, prompt version và source dataset đã dùng để tạo synthetic data.

Synthetic output không tự động xóa bỏ licensing hoặc privacy obligation của source ban đầu.

## Governance không đồng nghĩa Bureaucracy

Governance kém tạo ra nhiều manual gate nhưng không giảm risk.

Governance tốt chuyển policy thành metadata có thể đọc bằng máy, automated check và ownership rõ ràng.

## Tài liệu hóa Dataset

Một artifact hữu ích có thể là **Dataset Card**:

```text
- mục đích
- target population
- cách thu thập
- quy trình gán nhãn
- limitation đã biết
- sensitive field
- license
- recommended use
- prohibited use
```

## Mô hình tư duy

> **Data governance biến những file dữ liệu vô danh thành asset có owner, provenance, permission và lifecycle rõ ràng.**

## Những nhầm lẫn thường gặp

### “Governance chỉ quan trọng với công ty bị regulated”

Không. Ngay cả hệ thống nhỏ cũng cần lineage và ownership để debug và tái tạo kết quả.

### “Dataset đã anonymized thì an toàn mãi mãi”

Không. Re-identification risk thay đổi khi xuất hiện thêm auxiliary data hoặc kỹ thuật mới.

### “Search engine của RAG truy cập được document thì model cũng được phép đọc”

Không. User-level authorization vẫn phải được enforce riêng.

## Liên kết kiến thức

Data governance nối Security, Privacy, MLOps, AI Safety và Organizational Process. Đây là phần kết thúc Data layer và chuẩn bị cho AI Engineering, nơi model và data trở thành các production service.