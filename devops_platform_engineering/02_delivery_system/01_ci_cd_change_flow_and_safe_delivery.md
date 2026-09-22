# CI/CD: biến thay đổi thành flow có bằng chứng

## 1. Continuous Integration là giảm integration risk

Continuous Integration (CI / 지속적 통합) không đồng nghĩa với “có server chạy test”. Bản chất là tích hợp thay đổi nhỏ vào nhánh chính thường xuyên và nhận feedback tự động đủ nhanh để lỗi integration không tích tụ.

Nếu branch sống hai tuần rồi mới merge nhưng có Jenkins chạy mỗi commit, hệ thống có automation nhưng feedback integration vẫn muộn. Nếu test mất sáu giờ và thường flaky, developer có xu hướng bỏ qua signal. Do đó CI là thiết kế feedback loop, không chỉ YAML pipeline.

## 2. Pipeline phải trả lời câu hỏi theo tầng

Một pipeline tốt tổ chức check từ rẻ/nhanh đến đắt/chậm, nhưng không biến pipeline thành một chuỗi tuần tự dài vô lý. Lint/static check cho feedback nhanh. Unit test kiểm tra logic cục bộ. Integration/contract test kiểm tra boundary. Security/supply-chain checks xác minh policy. Build tạo artifact. Một số stage có thể chạy song song nếu dependency cho phép.

Điểm quan trọng là mỗi stage phải có failure semantics rõ. “Pipeline đỏ” nhưng không biết check nào đáng tin, ai sở hữu, có retry được không sẽ tạo alert fatigue giống production monitoring.

## 3. Flaky test là reliability debt

Test lúc pass lúc fail mà source không đổi làm pipeline mất vai trò oracle. Team bắt đầu rerun đến khi xanh và CI trở thành nghi thức. Flaky test cần được đo, quarantine có kiểm soát và sửa có owner. Không nên giữ build đỏ vô hạn, nhưng cũng không được coi rerun là remediation.

Một senior practice là theo dõi false positive/false negative của validation system. Pipeline cũng là production system phục vụ developer; nó có SLO về thời gian, availability và signal quality.

## 4. Continuous Delivery khác Continuous Deployment

Continuous Delivery nghĩa mainline luôn ở trạng thái có thể phát hành thông qua process tự động đáng tin. Continuous Deployment đi thêm một bước: thay đổi đạt policy sẽ tự động vào production mà không cần quyết định thủ công cho từng release.

Tổ chức có thể chọn delivery mà không deployment tự động vì regulation hoặc risk model. Điều quan trọng là approval nếu có phải nằm đúng nơi: xác nhận business/risk decision, không phải bù cho pipeline thiếu test.

## 5. Environment promotion

Một anti-pattern là mỗi môi trường build lại source. Confidence tốt hơn khi build một lần và promote cùng artifact. Environment khác nhau chủ yếu qua config, credential, capacity và external integration.

Promotion cần evidence. Ví dụ artifact A qua integration test, deploy staging, chạy smoke/e2e, rồi mới đủ điều kiện production. Evidence có thể được lưu cùng release metadata. Khi production incident, ta cần biết chính xác artifact, config, migration và deployment event nào vừa xảy ra.

## 6. Deployment không kết thúc khi API trả thành công

Một deployment command thành công chỉ chứng minh control plane chấp nhận desired state. Safe delivery cần xác minh actual behavior sau rollout. Có thể workload chưa ready, traffic error tăng hoặc dependency saturation xuất hiện sau vài phút.

Deployment verification nên dùng production signal liên quan user impact. Canary, blue-green, rolling update và feature flag là các mechanism giảm blast radius. Theory và trade-off đã có canonical chapter [deployment safety, canary, blue-green, flags và rollback](../../computer_science/09_software_engineering/advanced/05_deployment_safety_canary_blue_green_flags_and_rollback.md).

DevOps layer phải nối mechanism đó vào pipeline/controller để promotion dựa trên evidence chứ không dựa vào “deploy command exited 0”.

## 7. Rollback không luôn là inverse

Nếu release chỉ thay stateless code tương thích, rollback image có thể dễ. Nhưng nếu release đã migrate database schema, publish event theo schema mới hoặc gọi external side effect, rollback code có thể làm tình hình tệ hơn.

Safe change cần backward/forward compatibility. Database migration thường nên theo expand-and-contract: thêm capability tương thích trước, chuyển traffic/code, sau đó mới bỏ cấu trúc cũ khi chắc chắn không còn consumer. Khi state đã biến đổi không thể đảo, roll-forward có thể an toàn hơn rollback.

## 8. Feature flag tách deploy khỏi release

Deploy là đưa code vào environment. Release là làm behavior mới có hiệu lực với user. Feature flag cho phép hai thời điểm khác nhau. Điều này giảm blast radius và cho progressive exposure, nhưng flag tạo state và complexity riêng.

Flag cần owner, expiry và cleanup. Flag tồn tại nhiều tháng có thể tạo combinatorial behavior mà test không bao phủ. Platform nên hỗ trợ lifecycle chứ không chỉ cung cấp SDK.

## 9. Change metadata là telemetry

Mỗi deployment nên phát event có service, artifact version, commit, environment, actor/automation, thời gian và result. Khi dashboard latency tăng lúc 14:03, operator phải dễ overlay deployment event để thấy correlation. Không có change telemetry, investigation thường bắt đầu bằng câu “có ai vừa deploy gì không?”.

## 10. Pipeline security boundary

CI thường có quyền đọc source, token registry, cloud credential hoặc deploy permission. Vì vậy runner và workflow là security boundary. Pull request từ code chưa tin cậy không nên tự động nhận production secret. Dependency action/plugin phải được pin và kiểm soát. Least privilege nên áp dụng cho job identity theo stage.

## 11. Ví dụ reasoning một release

Giả sử `orders-api` thay logic tính phí. CI xác minh unit/contract test rồi build image digest D. D được scan và publish một lần. Staging deploy D với config staging. Smoke test và contract với dependency pass. Production rollout bắt đầu 5% traffic, theo dõi error rate, latency và business invariant. Nếu signal xấu, controller dừng promotion; rollback hoặc disable feature tùy state compatibility.

Điểm cốt lõi không nằm ở Jenkins/GitHub Actions/Argo Rollouts. Nó nằm ở identity của artifact, staged evidence, blast-radius control và recovery path.

## 12. Senior note: tối ưu lead time bằng giảm queue, không bỏ evidence

Khi pipeline chậm, phản xạ nguy hiểm là bỏ test. Trước tiên tìm critical path: setup dependency, duplicate build, serialized job, scarce runner, flaky rerun hay test suite không partition. Tối ưu feedback time bằng cache đúng, parallelism, test selection và architecture tốt hơn.

Delivery performance cao và reliability không phải hai mục tiêu đối nghịch nếu hệ thống được thiết kế để thay đổi nhỏ, feedback nhanh và rollback/risk boundary rõ.