# DevOps và Platform Engineering: từ vấn đề delivery đến operating model

## 1. Vấn đề gốc không phải thiếu công cụ

Một sản phẩm phần mềm tạo giá trị khi thay đổi có thể đi từ ý tưởng đến người dùng thật. Trong một hệ thống nhỏ, cùng một người có thể viết code, chạy test, copy file lên server và tự xem log. Khi hệ thống lớn hơn, chuỗi đó bị chia cho nhiều người, nhiều môi trường và nhiều quyền hạn. Từ đây xuất hiện một vấn đề hệ thống: mỗi handoff làm tăng thời gian chờ, mất ngữ cảnh và khả năng xảy ra sai khác.

DevOps tồn tại để xử lý chính vấn đề này. DevOps không phải vị trí “người biết Jenkins và Docker”, cũng không phải việc chuyển toàn bộ nhiệm vụ vận hành sang developer. Bản chất của nó là tối ưu hệ thống tạo và vận hành phần mềm sao cho **flow nhanh, feedback sớm và ownership không bị đứt đoạn**.

Hãy hình dung một thay đổi rất nhỏ: sửa timeout từ 2 giây lên 3 giây. Nếu phải mở ticket cho team build, chờ team infra tạo package, chờ team operation triển khai thủ công, rồi khi lỗi không ai biết cấu hình nào đang chạy, thì độ khó không nằm trong dòng code. Độ khó nằm trong delivery system.

## 2. Flow, feedback và learning loop

Luồng giá trị (value stream / 가치 흐름) là đường đi từ nhu cầu đến kết quả production. Một flow tốt giảm ba loại thời gian khác nhau. Thứ nhất là thời gian thực sự làm việc. Thứ hai là thời gian chờ giữa các bước. Thứ ba là thời gian sửa lại vì lỗi chỉ được phát hiện quá muộn.

Automation chủ yếu làm giảm thời gian thao tác và biến quy trình thành repeatable. Continuous Integration làm feedback về integration xuất hiện sớm. Continuous Delivery làm trạng thái “có thể phát hành” trở thành trạng thái bình thường. Observability rút ngắn feedback sau khi thay đổi chạm production. Postmortem biến failure thành input cho thiết kế tiếp theo.

Mental model quan trọng là một vòng kín:

```text
change → verify → package → release → observe → learn
   ↑                                      ↓
   └────────────── improve ───────────────┘
```

Nếu chỉ có automation từ trái sang phải mà không có evidence quay ngược lại, tổ chức có pipeline nhưng chưa có learning loop.

## 3. Ownership và ranh giới trách nhiệm

Ownership không có nghĩa mỗi developer phải trực 24/7 cho mọi thành phần. Nó có nghĩa team tạo ra một capability phải nhìn thấy hậu quả vận hành đủ rõ để thiết kế tốt hơn. Khi người viết code không bao giờ thấy latency, saturation, deployment failure hoặc incident pattern, feedback bị cắt. Khi operator chỉ nhận artifact cuối cùng mà không biết intent của thay đổi, ngữ cảnh cũng bị cắt.

Một operating model tốt phải làm rõ ít nhất ba lớp trách nhiệm. Application team sở hữu behavior của application và cách application dùng platform. Platform team sở hữu các capability dùng chung và trải nghiệm sử dụng chúng. Một số nhóm chuyên môn như security, network hoặc database có thể cung cấp policy, expertise và shared service nhưng không nên trở thành queue bắt buộc cho mọi thay đổi thông thường.

Điểm khó là tìm abstraction boundary. Nếu platform giấu quá nhiều, developer không hiểu failure. Nếu platform lộ mọi chi tiết Kubernetes/cloud, cognitive load lại quay về từng team. Platform Engineering xuất hiện để thiết kế ranh giới này có chủ đích.

## 4. Platform Engineering giải quyết cognitive load

Khi mỗi team tự dựng CI, logging, ingress, secrets, cluster policy và Terraform theo cách riêng, tổ chức có autonomy nhưng phải trả chi phí lặp lại khổng lồ. Nhiều lỗi production không đến từ business logic mà đến từ việc mỗi team phải trở thành chuyên gia ở hàng chục subsystem.

Nền tảng nội bộ (internal developer platform / 내부 개발자 플랫폼) gom các capability lặp lại thành product dùng cho developer. “Product” ở đây quan trọng: platform phải có user, use case, interface, compatibility contract, support model và feedback. Một repository chứa vài template chưa tự động trở thành platform.

Đường đi chuẩn (golden path) là một con đường đã được tối ưu cho use case phổ biến. Ví dụ, service HTTP tiêu chuẩn có thể nhận sẵn pipeline, image build, deployment manifest, health check, metrics, secret injection và dashboard. Golden path không nên là “golden cage”. Team phải có escape hatch khi requirement thật sự khác, nhưng sự khác biệt phải explicit và có owner.

## 5. Guardrail khác gate

Cổng kiểm soát (gate) thường chặn flow và đòi một phê duyệt thủ công trước khi tiếp tục. Hàng rào an toàn (guardrail) cố gắng encode policy ngay trong hệ thống để lựa chọn không an toàn khó xảy ra từ đầu.

Ví dụ, thay vì yêu cầu security team đọc từng Kubernetes manifest để xem container có chạy root hay không, platform có thể cung cấp default an toàn, policy-as-code và feedback ngay trong pull request. Gate vẫn cần ở một số thay đổi có rủi ro cao, nhưng nếu mọi thay đổi đều cần gate thì platform đang biến chuyên gia thành bottleneck.

## 6. Automation không đồng nghĩa với safety

Một quy trình sai được tự động hóa chỉ giúp sai nhanh hơn. Safety đến từ invariant và feedback. Ví dụ, “mọi môi trường chạy cùng một artifact đã được định danh bằng digest” là invariant. “Deployment chỉ tiếp tục khi health signal nằm trong ngưỡng” là một invariant khác. Pipeline, registry và controller chỉ là mechanism thực thi các invariant đó.

Khi thiết kế automation, hãy hỏi: state nào đang thay đổi; nguồn sự thật (source of truth) là gì; ai có quyền thay đổi; thay đổi có idempotent không; có thể preview không; failure giữa chừng để lại state gì; rollback thật sự là đảo code, đảo config, đảo schema hay chuyển traffic; và evidence nào chứng minh hệ thống đã đạt trạng thái mong muốn.

## 7. Một ví dụ xuyên suốt

Giả sử team cần tạo dịch vụ `orders-api`. Cách tool-centric sẽ bắt đầu bằng câu hỏi dùng GitHub Actions hay Jenkins, Docker hay Buildpacks, EKS hay GKE. Cách reasoning-centric bắt đầu từ contract.

Source change phải review được. Build phải tái tạo được và tạo artifact bất biến. Artifact phải có provenance đủ để biết commit nào sinh ra nó. Môi trường không được build lại artifact khác. Deployment phải giới hạn blast radius. Service phải xuất telemetry đủ để xác định user impact. Secrets không được bake vào image. Dependency failure phải quan sát được. Recovery phải có cả rollback path và data compatibility path.

Sau khi những invariant này rõ, lựa chọn tool mới có ý nghĩa. Hai tổ chức có thể dùng tool khác nhau nhưng cùng operating model. Ngược lại, hai team cùng dùng Kubernetes vẫn có maturity khác nhau rất lớn nếu một team hiểu control loop còn team kia chỉ copy YAML.

## 8. Senior note: tối ưu toàn hệ thống, không tối ưu cục bộ

Một pipeline chạy nhanh hơn không có giá trị nếu nó đẩy lỗi sang production. Một security gate bắt được nhiều lỗi không có giá trị nếu mỗi release phải chờ ba ngày và team bắt đầu bypass quy trình. Một platform che hết Kubernetes không có giá trị nếu khi incident xảy ra không ai biết workload thực sự được schedule và network như thế nào.

Đây là tư duy tối ưu hệ thống (systems optimization): local metric phải phục vụ outcome toàn chuỗi. Khi một bước trở nên nhanh hơn nhưng queue ở bước sau dài hơn, throughput toàn hệ thống không tăng. Khi abstraction giảm cognitive load lúc bình thường nhưng làm mất khả năng chẩn đoán lúc bất thường, abstraction chưa hoàn thiện.

## 9. Kết nối với canonical Computer Science

Operating model này dựa trên nhiều cơ chế không nên duplicate trong library. Process, syscall và isolation xem tại [Operating Systems foundation](../../computer_science/basic/03_operating_systems/00_kernel_syscalls_and_os_abstractions.md). Container internals xem [namespaces, cgroups, capabilities và seccomp](../../computer_science/03_operating_systems/advanced/06_containers_namespaces_cgroups_capabilities_and_seccomp.md). Distributed failure semantics xem [Networks & Distributed Systems advanced](../../computer_science/06_networks_distributed_systems/advanced/README.md). Deployment strategy ở mức software engineering xem [deployment safety](../../computer_science/09_software_engineering/advanced/05_deployment_safety_canary_blue_green_flags_and_rollback.md).

Các chapter tiếp theo dùng những nền đó để xây delivery system và platform ở cấp production.

## 10. Flow phải được nhìn bằng queue, WIP và batch size

Một delivery system có thể rất tự động nhưng vẫn chậm vì thay đổi nằm chờ trong queue. Để hiểu flow, cần tách **lead time** — thời gian từ lúc nhu cầu/thay đổi bắt đầu đến lúc tạo giá trị — khỏi **processing time** — thời gian hệ thống thực sự đang xử lý thay đổi. Khoảng cách giữa hai con số thường chính là queue, handoff, chờ review, chờ environment hoặc chờ approval.

Công việc đang dở (work in progress — WIP) càng lớn thì càng nhiều thay đổi phải chia sẻ attention, runner, reviewer và môi trường. Một quan hệ quan trọng từ lý thuyết hàng đợi là: khi throughput tương đối ổn định, WIP tăng sẽ kéo thời gian hoàn thành trung bình tăng. Vì vậy cách cải thiện flow thường không phải “bắt mọi người làm nhanh hơn”, mà là giảm batch size, giới hạn WIP và làm feedback xuất hiện trước khi một thay đổi tích tụ thêm dependency.

Hãy so hai release. Release A chứa 40 thay đổi và mất hai tuần để test; khi lỗi xảy ra phải tìm trong một batch lớn. Release B gồm nhiều thay đổi nhỏ, mỗi thay đổi đi qua pipeline trong vài chục phút. Cùng một tổng khối lượng code nhưng release B có search space nhỏ hơn, rollback/roll-forward dễ hơn và feedback quay về author khi context còn mới. Đây là lý do batch size là một biến reliability chứ không chỉ là biến tốc độ.

## 11. Metric delivery là sensor, không phải mục tiêu để game

Các metric như lead time, deployment frequency, tỷ lệ thay đổi gây lỗi và thời gian phục hồi hữu ích vì chúng quan sát các phần khác nhau của flow. Nhưng chúng chỉ là sensor. Nếu ép “deployment frequency phải tăng” mà team chia một thay đổi nguy hiểm thành nhiều deploy phụ thuộc lẫn nhau, số đẹp hơn nhưng system risk có thể tăng. Nếu định nghĩa “failure” quá hẹp để giảm change failure rate, metric mất giá trị.

Cách dùng đúng là nhìn metric theo causal question. Lead time tăng vì review queue hay vì test chậm? Tỷ lệ release lỗi tăng ở một service hay toàn platform? Recovery chậm vì detection muộn, access khó, rollback không tương thích hay operator thiếu runbook? Metric chỉ hữu ích khi dẫn tới một hypothesis có thể kiểm tra và một thay đổi hệ thống cụ thể.

## 12. Socio-technical system: kiến trúc và tổ chức phản hồi lẫn nhau

Delivery system không chỉ gồm code và tool. Quyền hạn, ownership, cấu trúc team và incentive quyết định automation được dùng ra sao. Một team có quyền deploy nhưng không có quyền xem production telemetry vẫn chưa thật sự sở hữu outcome. Một platform team bị đo bằng số ticket đóng có thể vô tình tối ưu việc xử lý ticket thay vì xóa nhu cầu ticket.

Khi một bước luôn tạo bottleneck, đừng chỉ hỏi tool nào chậm. Hãy hỏi tại sao quyết định đó phải đi qua boundary hiện tại, information nào chỉ một nhóm đang giữ, risk nào đang được gate thủ công thay vì encode thành guardrail, và liệu interface giữa các team có thể trở thành contract kỹ thuật ổn định hay không.

Đây là điểm Platform Engineering nối với organizational design: mục tiêu không phải xóa mọi specialization mà là biến giao tiếp lặp lại thành capability có contract, để chuyên gia tập trung vào exception và evolution thay vì trở thành queue cho common path.

## 13. Bottleneck quyết định throughput toàn hệ thống

Một hệ thống delivery có nhiều bước nhưng throughput dài hạn thường bị giới hạn bởi constraint hẹp nhất. Nếu build mất 5 phút nhưng security review phải chờ hai ngày, tối ưu build xuống 3 phút gần như không thay đổi lead time. Nếu reviewer là bottleneck, tăng số pull request mở đồng thời còn có thể làm queue dài hơn.

Điều này dẫn tới một discipline quan trọng: trước khi tối ưu, xác định **constraint hiện tại** bằng evidence. Queue nào tăng dần? Resource hoặc role nào luôn bận? Bước nào tạo waiting time lớn nhất? Khi constraint được cải thiện, bottleneck có thể chuyển sang bước khác; tối ưu hệ thống là quá trình lặp, không phải một dự án “tăng tốc pipeline” một lần.

Local utilization 100% không luôn tốt. Một reviewer hoặc môi trường test chạy kín 100% thời gian thường đồng nghĩa queue phía trước không có slack để hấp thụ biến động. Hệ thống flow-sensitive cần một mức capacity headroom để urgent work và variation không biến thành waiting time phi tuyến.

## 14. Feedback delay có thể làm control decision sai dù signal đúng

Feedback không chỉ cần chính xác mà còn phải đủ sớm. Nếu một deployment lỗi sau 30 phút nhưng team deploy 20 release khác trong khoảng đó, khi alert xuất hiện search space đã lớn. Nếu cost report chỉ đến cuối tháng, feedback quá trễ để developer liên hệ với change cụ thể.

Một loop có delay dài dễ bị over-correction. Team thấy queue dài nên tăng concurrency; vài phút sau downstream quá tải, lại giảm mạnh; rồi khi backlog giảm thì capacity dư thừa. Cùng pattern xuất hiện ở autoscaling, approval queue và incident response.

Vì vậy khi thiết kế feedback loop phải hỏi bốn thứ: sensor đo gì, delay bao lâu, actuator thay state nào và action có effect sau bao lâu. “Có metric” không đủ nếu delay lớn hơn tốc độ hệ thống thay đổi.

## 15. Queue discipline là policy, không chỉ implementation detail

Khi capacity hữu hạn, thứ tự xử lý work trở thành quyết định sản phẩm/vận hành. FIFO đơn giản và công bằng theo thời gian, nhưng incident fix hoặc security patch critical có thể cần priority. Nếu mọi team đánh request của mình là urgent, priority queue mất nghĩa và normal work bị starvation.

Expedite lane nên có entry criterion rõ, giới hạn WIP và audit. Mục tiêu là giữ khả năng phản ứng với work thật sự khẩn cấp mà không biến hệ thống thành “ai kêu to hơn được làm trước”.

Điều này áp dụng từ ticket/review queue đến CI runner, deploy queue và platform provisioning. Queue semantics là một phần operating model vì nó quyết định latency dưới contention.

## 16. Handoff làm mất information, không chỉ thêm waiting time

Mỗi handoff giữa team hoặc tool có thể làm mất intent. Developer nói “cần DB để xử lý order” nhưng ticket chỉ còn “tạo PostgreSQL 4 CPU”; operator thấy resource request nhưng không biết RPO, connection pattern hay criticality. Khi incident xảy ra, context business ban đầu đã biến mất.

Một interface tốt phải giữ lại information cần cho quyết định downstream dưới dạng contract hoặc metadata: owner, criticality, SLO, data class, artifact/config identity và reason của exception. Đây là lý do platform API có giá trị hơn chỉ tự động hóa thao tác: nó chuẩn hóa **semantic handoff**.

Giảm handoff không nghĩa xóa mọi team boundary. Nó nghĩa giữ intent machine-readable đủ để boundary không biến thành mất ngữ cảnh rồi hỏi lại bằng ticket/chat.

## 17. Toil là công việc lặp lại thiếu giá trị bền vững, nhưng không phải mọi manual work đều xấu

Toil thường là thao tác thủ công lặp lại, có tính operational, tăng gần tuyến tính theo quy mô và không tạo cải thiện lâu dài: tạo namespace bằng tay, rotate cùng loại secret cho hàng trăm service, copy deployment status vào ticket. Những việc này là ứng viên tốt cho automation hoặc self-service.

Nhưng automation có fixed cost và maintenance cost. Một thao tác hiếm, rủi ro cao, thay đổi liên tục có thể chưa đáng encode thành platform feature. Tự động hóa quá sớm còn khóa assumption chưa hiểu rõ vào code và mở blast radius mới.

Một cách reasoning tốt là xem frequency, volume, error probability, waiting time, cognitive load và cost nếu automation sai. Mục tiêu không phải “zero manual operation”; mục tiêu là con người tập trung vào decision cần judgment còn common path trở nên repeatable.

## 18. Senior walkthrough: tăng utilization làm lead time tệ hơn

Giả sử một organization có hai shared staging environment và muốn “tận dụng tài nguyên tốt hơn”, nên scheduler luôn giữ cả hai environment bận. Khi một release critical cần test, nó phải chờ các job dài hiện tại kết thúc. Team bắt đầu gộp nhiều change vào mỗi lượt staging để “đỡ phải chờ”, batch size tăng; khi test fail, search space lớn và lượt retry tiếp tục chiếm environment lâu hơn.

Tối ưu utilization cục bộ đã tạo feedback xấu: utilization cao → queue dài → batch lớn → failure/rework lớn → queue càng dài. Fix có thể là giữ reserve capacity cho high-priority flow, giới hạn job duration, tạo ephemeral environment hoặc giảm setup cost để capacity co giãn được.

Bài học là delivery system nên tối ưu **flow và outcome**, không tối đa hóa việc mọi resource luôn bận.