# Từ source đến artifact: Git, build và tính tái lập

## 1. Source control là lịch sử thay đổi, không phải kho file

Git quan trọng với delivery vì nó tạo một graph các snapshot có identity. Commit hash cho phép gắn một thay đổi với review, test result, build artifact và deployment. Nếu production đang chạy nhưng không thể trả lời “commit nào sinh ra binary này?”, traceability đã bị đứt.

Branch strategy chỉ là một cơ chế quản lý concurrent change. Mục tiêu thật là giảm thời gian thay đổi sống ngoài nhánh chính và giảm batch size. Nhánh tồn tại quá lâu làm integration trở thành sự kiện lớn. Vì vậy trunk-based development thường phù hợp với continuous integration khi team có test và feature flag đủ tốt. Nhưng rule không phải “không được branch”; rule là integration phải thường xuyên và thay đổi phải nhỏ đủ để hiểu/rollback.

## 2. Build là hàm biến input thành output

Mental model đơn giản:

```text
artifact = build(source, dependencies, toolchain, configuration)
```

Nếu bất kỳ input nào bị ẩn hoặc mutable, cùng commit có thể tạo output khác nhau. Ví dụ dùng dependency `latest`, download script không pin checksum hoặc build dựa vào package registry state hiện tại. Khi đó commit hash không còn đủ để tái tạo artifact.

Tính tái lập (reproducibility) không nhất thiết đòi bit-for-bit identical cho mọi hệ sinh thái, nhưng phải có contract đủ mạnh: dependency version khóa, toolchain version xác định, build instruction versioned và environment-dependent value không được bake ngẫu nhiên vào artifact.

## 3. Artifact phải bất biến sau khi phát hành

Một anti-pattern phổ biến là dùng tag mutable như `app:latest` và push lại nội dung khác dưới cùng tag. Manifest nhìn không đổi nhưng workload mới có thể chạy bytes khác. Điều này phá audit và rollback.

Tag thuận tiện cho con người, digest/content identity thuận tiện cho machine invariant. Platform nên có cách promotion cùng một artifact digest từ test sang staging rồi production. Không build lại source ở mỗi môi trường, vì build lại có nghĩa đưa thêm biến số vào đúng lúc cần tăng confidence.

## 4. Configuration khác artifact

Không phải mọi thứ đều nên đóng vào image/package. Code và runtime dependency ổn định thuộc artifact. Environment-specific configuration, secret và endpoint thường nên được inject qua deployment/runtime interface. Ranh giới này cho phép cùng artifact chạy ở nhiều môi trường.

Tuy nhiên “externalize config” không có nghĩa config không cần versioning. Một incident do config change vẫn là change. Production cần biết code version và config version nào kết hợp tại thời điểm failure.

## 5. Dependency pinning và update strategy

Khóa dependency giúp reproducibility nhưng tạo trách nhiệm update. Nếu pin mãi, security patch và compatibility improvement không vào được. Nếu luôn lấy newest, build trở nên không deterministic. Hệ thống tốt tách hai hành vi: build thường dùng version đã pin; dependency update là một change explicit qua bot hoặc pull request, có test và review như code.

Với base container image cũng tương tự. `FROM ubuntu:latest` dễ dùng nhưng khó audit. Pin digest tăng tính xác định; đồng thời cần automation định kỳ mở update để base image không bị đóng băng.

## 6. Build cache: optimization có correctness contract

Cache build giảm thời gian nhưng cache key sai có thể tái sử dụng output cũ khi input đã đổi. Vì vậy cache không chỉ là performance feature; nó là correctness problem. Cache key phải đại diện mọi input ảnh hưởng output.

Ví dụ với Dockerfile, copy lockfile và cài dependency trước khi copy toàn source giúp cache dependency layer hiệu quả. Nhưng nếu build phụ thuộc file bị bỏ qua khỏi context hoặc environment variable không nằm trong key, cache có thể che lỗi. Khi nghi ngờ build inconsistency, thử clean build để phân biệt lỗi source với lỗi cache.

## 7. Provenance và software supply chain

Artifact production nên có metadata trả lời: source repository nào, commit nào, build workflow nào, builder identity nào, dependency nào và thời điểm nào. Provenance không tự động đảm bảo artifact an toàn; nó làm chuỗi bằng chứng có thể kiểm tra.

SBOM (Software Bill of Materials) mô tả component bên trong artifact. SBOM hữu ích khi một vulnerability mới xuất hiện: thay vì scan mọi source bằng phỏng đoán, có thể tìm artifact nào chứa version bị ảnh hưởng. Chapter security sẽ nối provenance, signing và policy thành supply-chain control.

## 8. Một pipeline build có contract rõ ràng

Một build pipeline tối thiểu nên tách verification và packaging. Verification chứng minh source change đạt rule. Packaging tạo artifact. Publish đưa artifact bất biến vào registry/repository. Metadata nối artifact với commit và build run.

Pseudo-flow:

```text
checkout exact commit
→ restore trusted cache
→ resolve pinned dependencies
→ compile/build
→ unit/static/security checks
→ package immutable artifact
→ generate metadata/SBOM
→ publish once
```

Không nhất thiết mọi check chạy trước packaging; tổ chức có thể tối ưu parallelism. Điều không nên mất là identity và promotion semantics.

## 9. Failure pattern

Nếu “staging chạy, production lỗi” dù code được cho là giống nhau, kiểm tra đầu tiên là artifact có thật sự giống nhau không. Nếu staging deploy bằng tag và production pull lại tag vài giờ sau, có thể bytes đã khác. Nếu artifact giống, so config, secret version, external dependency và data/schema compatibility.

Nếu “rebuild commit cũ nhưng artifact khác”, kiểm tra dependency lock, base image, package registry, build timestamp, generated code và toolchain. Đây là lý do reproducibility là prerequisite của debugging đáng tin cậy.

## 10. Invariant cần giữ

Một delivery system trưởng thành phải trả lời được: thay đổi nào sinh artifact; artifact nào được deploy; artifact có bất biến không; input build có được version hóa không; ai/automation nào tạo artifact; và cùng artifact có được promote xuyên môi trường không. Khi các câu trả lời này rõ, CI/CD phía sau mới có nền ổn định.