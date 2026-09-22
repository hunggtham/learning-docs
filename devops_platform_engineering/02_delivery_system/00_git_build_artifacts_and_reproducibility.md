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

## 11. Reproducible build khác hermetic build

Hai khái niệm liên quan nhưng không giống nhau. Build tái lập được (reproducible build) nhấn mạnh cùng input cho output tương đương theo contract. Build kín (hermetic build) nhấn mạnh quá trình build chỉ được phép thấy những input đã khai báo, thay vì vô tình đọc tool, file, network hoặc package state từ môi trường host.

Một build có thể cho kết quả giống nhau nhiều lần trong cùng runner nhưng vẫn không hermetic nếu nó âm thầm dùng JDK cài sẵn trong máy. Ngày runner được nâng cấp, output hoặc behavior có thể đổi. Ngược lại, build hermetic nhưng artifact chứa timestamp ngẫu nhiên có thể chưa bit-for-bit reproducible.

Mental model tốt là khai báo **input closure**: source, dependency, toolchain, build rule và dữ liệu nào thực sự ảnh hưởng output. Càng ít input ẩn, debugging và provenance càng đáng tin.

## 12. Reproducible không đồng nghĩa trusted

Một attacker kiểm soát build script hoàn toàn có thể tạo malware theo cách rất reproducible. Vì vậy correctness và trust là hai trục khác nhau. Reproducibility giúp biết cùng input tạo cùng output; provenance/attestation giúp biết input và builder nào đã được dùng; authorization/policy quyết định có tin builder và source đó hay không.

Chuỗi reasoning nên là:

```text
identity của source/change
→ identity và isolation của builder
→ declared inputs
→ artifact digest
→ provenance/attestation
→ policy cho phép promotion/deploy hay không
```

Nếu chỉ scan artifact cuối cùng mà không kiểm soát builder, một compromised runner có thể chèn code sau test. Nếu chỉ tin builder nhưng dependency không pin, build vẫn có input ngoài dự kiến.

## 13. Cache là trust boundary, không chỉ performance feature

Shared cache có thể làm tăng tốc đáng kể, nhưng nếu key collision hoặc writer không đáng tin có thể ghi output độc hại vào cache, job khác sẽ consume mà không chạy lại bước tạo output. Với cache chứa package, compiled object hoặc Docker layer, cần biết ai được ghi, key có bao phủ input quan trọng không và cache có được phân tách theo trust level hay repository hay không.

Pull request từ fork/untrusted source đặc biệt cần cẩn thận. Một pattern an toàn là cho job không tin cậy đọc cache phù hợp nhưng không ghi vào cache dùng bởi trusted release job, hoặc dùng namespace/cache key tách biệt. Chi tiết phụ thuộc CI system nhưng invariant không đổi: **output từ trust domain thấp không được trở thành input ngầm của trust domain cao**.

## 14. Attestation là statement có subject và predicate

Attestation có thể hiểu đơn giản là một statement được một identity ký/xác nhận về một subject. Subject thường là artifact digest; predicate có thể mô tả provenance, test result hoặc policy fact. Điều quan trọng là không đánh đồng “có signature” với “nội dung statement đúng và đủ”.

Verifier phải kiểm tra ít nhất: subject có đúng digest đang deploy không; signer/builder có nằm trong trust policy không; statement type có đúng điều đang cần chứng minh không; và identity/key có còn hợp lệ theo lifecycle hiện tại không.

Nhờ đó promotion có thể chuyển từ “pipeline trước đã xanh” sang một contract machine-verifiable: artifact D chỉ được vào production nếu có provenance từ trusted builder, source revision được review theo policy và các verification cần thiết gắn đúng với D.

## 15. Build metadata phải sống cùng artifact identity

Log CI thường bị retention ngắn hoặc khó tìm. Metadata quan trọng cho production không nên chỉ nằm trong một pipeline run URL. Artifact catalog/registry nên cho phép lần từ digest tới source revision, builder, SBOM, provenance và release history.

Điều này đặc biệt hữu ích trong incident hoặc vulnerability response. Khi có CVE mới, câu hỏi không còn là “repo nào có dependency này?” mà là “artifact nào đang hoặc từng chạy production chứa component bị ảnh hưởng, được build từ revision nào, và có replacement nào đã verify?”.

## 16. Senior note: promotion là chuyển trust, không phải copy bytes

Khi artifact D đi từ staging sang production, bytes không nên đổi. Thứ thay đổi là **mức evidence và authorization** gắn với D. Staging có thể chứng minh integration behavior; canary production thêm evidence từ traffic thật; approval nếu cần xác nhận risk/business decision.

Nhìn như vậy giúp tránh anti-pattern “rebuild cho production để sạch hơn”. Rebuild tạo subject mới và reset một phần evidence. Một delivery system mạnh giữ artifact identity ổn định rồi tích lũy evidence quanh identity đó.