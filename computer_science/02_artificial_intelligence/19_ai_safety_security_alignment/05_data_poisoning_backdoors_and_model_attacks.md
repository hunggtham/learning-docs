# Đầu độc dữ liệu, cửa hậu và tấn công mô hình

Bảo mật AI không chỉ bắt đầu ở thời điểm suy luận. Nếu attacker can thiệp vào dữ liệu huấn luyện, nhãn, checkpoint, adapter hoặc pipeline build, hệ thống có thể bị compromise từ trước khi triển khai. **Đầu độc dữ liệu (data poisoning / 데이터 포이즈닝)** làm quá trình học hấp thụ hành vi sai hoặc có chủ đích. **Cửa hậu (backdoor / trojan)** tạo một điều kiện kích hoạt đặc biệt khiến mô hình hành xử khác thường trong một số trường hợp hiếm.

## Kiến thức cần có trước

Nên đọc [Data for AI](../14_data_for_ai/README.md), [Data Governance](../14_data_for_ai/08_data_governance.md), [Training Pipeline](../15_ai_engineering/01_training_pipeline.md), [Model Registry](../16_mlops_and_llmops/03_model_registry.md) và [Adversarial Machine Learning](./04_adversarial_machine_learning.md).

## Bề mặt tấn công của quá trình huấn luyện

Một pipeline huấn luyện có thể lấy dữ liệu từ:

```text
web công khai
nội dung do người dùng tạo
nhãn do con người gán
dataset của bên thứ ba
dữ liệu tổng hợp
feedback từ production
checkpoint đã huấn luyện trước
adapter / LoRA
```

Mỗi nguồn có mức độ tin cậy và provenance khác nhau. Khi các nguồn này được trộn vào cùng một training corpus mà không giữ metadata, việc điều tra nguồn gốc hành vi xấu về sau trở nên rất khó.

## Hai mục tiêu lớn của poisoning

**Poisoning phá tính sẵn sàng (availability poisoning)** làm chất lượng tổng thể của mô hình giảm rõ rệt.

**Poisoning phá tính toàn vẹn (integrity poisoning)** cố giữ metric tổng thể gần bình thường nhưng làm sai một hành vi, một lớp, một input hoặc một nhóm trường hợp cụ thể.

Dạng thứ hai nguy hiểm hơn trong production vì benchmark aggregate có thể vẫn tốt.

## Trực giác cơ chế

Huấn luyện tối ưu objective trên dữ liệu quan sát. Nếu một phần dữ liệu bị thay đổi có hệ thống, gradient tổng hợp cũng đổi theo. Với tập huấn luyện `D` và tập poison `P`, objective có thể hình dung như:

\[
L(\theta)=\frac{1}{|D\cup P|}
\sum_{(x,y)\in D\cup P}L(f_\theta(x),y)
\]

Nếu `P` được thiết kế để tạo gradient có ảnh hưởng lớn tới một vùng hành vi cụ thể, số mẫu poison không nhất thiết phải chiếm tỷ lệ lớn mới gây tác động. Vì vậy trực giác “dataset lớn sẽ tự pha loãng poison” không phải bảo đảm an toàn.

## Poisoning nhãn

**Poisoning nhãn (label poisoning)** thay đổi hoặc thao túng quá trình gán nhãn. Lỗi không nhất thiết đến từ attacker; bug trong pipeline label hoặc policy gán nhãn sai cũng có thể tạo hậu quả tương tự.

Các biện pháp production gồm:

- lưu provenance của nhãn;
- đo agreement giữa annotator;
- phát hiện thay đổi label distribution;
- review các nhóm nhãn bất thường;
- giữ một tập validation có nguồn kiểm soát chặt.

## Clean-label poisoning

Trong **clean-label poisoning**, input vẫn trông hợp lệ và nhãn cũng có vẻ đúng với con người, nhưng sample được chọn hoặc biến đổi để làm biên quyết định dịch theo hướng bất lợi. Điều này nhắc rằng “label đúng” không đồng nghĩa “sample vô hại”.

## Cửa hậu và trigger

Một backdoor thường có behavior kiểu:

```text
input bình thường
→ mô hình hoạt động đúng

input + điều kiện kích hoạt hiếm
→ mô hình trả kết quả do attacker mong muốn
```

Trigger có thể là pattern thị giác, token, metadata, thuộc tính ngữ cảnh hoặc một tổ hợp feature hiếm. Vì hành vi bình thường vẫn tốt nên benchmark tiêu chuẩn có thể bỏ sót.

## Cửa hậu đi vào hệ thống bằng cách nào?

Nguồn thường gặp về mặt kiến trúc:

```text
dữ liệu training bị poison
checkpoint bên ngoài đã bị cài backdoor
adapter hoặc LoRA không đáng tin
code tiền xử lý bị sửa
pipeline build bị compromise
```

Do đó backdoor detection không chỉ là bài toán của mô hình; nó là bài toán supply-chain và lineage.

## Rủi ro từ checkpoint và serialization

File mô hình không nên được mặc định xem như “dữ liệu thụ động”. Một số định dạng serialization hoặc custom loading path có thể thực thi code. Ngay cả khi định dạng an toàn về code execution, trọng số vẫn có thể chứa hành vi đã bị cài backdoor.

Production pipeline nên:

```text
xác minh nguồn
kiểm tra digest/signature
tránh custom code không cần thiết
load trong sandbox khi nguồn chưa tin cậy
chạy behavioral/security regression trước khi promote
```

## Rủi ro từ adapter và model merging

Adapter, LoRA hoặc checkpoint merge có thể thay đổi behavior sâu dù kích thước artifact nhỏ. Vì vậy adapter phải được xem như artifact có quyền thay đổi hệ thống, không phải “file phụ” vô hại.

Mọi adapter cần identity, provenance, evaluation và approval giống model artifact chính.

## Synthetic data và feedback poisoning

Nếu synthetic data được sinh từ một model đã có bias hoặc compromise rồi quay lại làm training data, lỗi có thể tự khuếch đại. Tương tự, production feedback có thể bị thao túng bằng hành vi phối hợp, spam rating hoặc tạo nhiều tương tác giả.

Không nên đưa feedback trực tiếp vào continuous training nếu chưa qua trust weighting, anomaly detection, delayed validation hoặc sampling review.

## Làm sạch dữ liệu không đủ để bảo đảm an toàn

Các phép kiểm như duplicate, outlier, source reputation, label inconsistency và anomalous cluster có ích nhưng không thể chứng minh mọi poison đã được loại bỏ. Attack có thể được thiết kế để trông giống phân phối bình thường.

Vì vậy cần **phòng thủ theo nhiều lớp (defense in depth)**:

```text
provenance
→ data quality gate
→ trusted validation
→ lineage
→ behavior regression
→ controlled promotion
→ production monitoring
```

## Tập validation có provenance tin cậy

Một tập validation nhỏ nhưng được kiểm soát tốt có thể đóng vai trò anchor. Nó giúp phát hiện candidate model có behavior khác thường so với known-good model.

Tuy nhiên nếu attacker cũng có thể thao túng validation set thì lớp này mất giá trị. Vì vậy quyền ghi vào evaluation assets cũng là một security boundary.

## Phân tích ảnh hưởng

Các kỹ thuật **phân tích ảnh hưởng (influence analysis)** cố ước lượng sample huấn luyện nào góp phần nhiều vào một prediction hoặc behavior đáng ngờ. Chúng hữu ích cho forensic investigation nhưng thường đắt và chỉ gần đúng với mô hình lớn.

Không nên coi influence score như bằng chứng tuyệt đối về nguyên nhân.

## Phát hiện backdoor

Có thể kiểm tra:

- activation bất thường;
- sensitivity với pattern hiếm;
- thay đổi behavior theo trigger candidate;
- regression trên tập red-team;
- khác biệt giữa model/adapter lineage.

Không có một detector duy nhất bao phủ mọi backdoor. False positive và false negative đều cần được xem xét.

## Mô hình triển khai an toàn hơn

Một training-to-production flow nên có dạng:

```text
nguồn dữ liệu đã định danh
→ snapshot bất biến
→ validation + provenance check
→ training trong môi trường kiểm soát
→ artifact digest/signature
→ evaluation trên trusted set
→ security regression
→ registry
→ approval
→ canary/shadow
→ production monitoring
```

Điểm quan trọng là mỗi mũi tên phải có lineage để truy ngược khi incident xảy ra.

## Quyền tối thiểu trong training

Training job thường chỉ cần đọc dataset và ghi artifact. Nó không nên mặc định có quyền quản trị production database, registry hoặc secret rộng hơn mức cần thiết.

**Nguyên tắc quyền tối thiểu (least privilege)** giảm blast radius nếu notebook, dependency hoặc worker bị compromise.

## Failure mode ở production

**Poisoning không làm metric aggregate giảm.** Hành vi xấu chỉ xuất hiện ở slice hiếm.

**Validation dùng cùng nguồn với training.** Một nguồn lỗi có thể làm cả train và validation cùng sai.

**Không có lineage.** Khi phát hiện issue không biết model nào dùng dataset hoặc adapter bị ảnh hưởng.

**Artifact mutable.** Tag cũ bị ghi đè khiến rollback không còn xác định.

**Feedback loop tự động.** Bad output tạo bad feedback rồi lại quay vào training.

**Adapter được trust quá mức.** Một LoRA nhỏ được promote mà không qua security regression.

## Ứng phó sự cố

Khi nghi ngờ poisoning hoặc backdoor:

```text
1. dừng promotion và continuous training liên quan
2. cô lập nguồn dữ liệu/artifact đáng ngờ
3. xác định model bị ảnh hưởng qua lineage
4. rollback về known-good bundle
5. rebuild từ snapshot tin cậy
6. mở rộng regression suite cho failure vừa phát hiện
7. chỉ promote lại sau evaluation và security gate
```

Với hệ thống có nhiều tenant hoặc tool quyền cao, có thể cần đồng thời thu hồi credential hoặc vô hiệu hóa workflow liên quan.

## Trade-off

Kiểm soát provenance, immutable artifacts và security evaluation làm pipeline chậm hơn và tăng storage/compute cost. Nhưng bỏ các lớp này khiến sự cố khó điều tra và recovery đắt hơn nhiều.

Mức độ kiểm soát nên tỷ lệ với impact: model thử nghiệm nội bộ có thể dùng gate nhẹ hơn hệ thống tài chính, danh tính hoặc agent có side effect.

## Mô hình tư duy

> **Nếu dữ liệu, nhãn hoặc artifact đầu vào không đáng tin, hành vi đã học cũng là một phần của chuỗi cung ứng cần được bảo vệ.**

Security của model bắt đầu từ nguồn dữ liệu và pipeline tạo ra model, không chỉ từ endpoint inference.

## Những nhầm lẫn thường gặp

### “Dataset lớn tự động pha loãng poison”

Không. Targeted poisoning hoặc backdoor có thể tạo tác động lớn trên một vùng hành vi nhỏ.

### “Checkpoint nổi tiếng thì mặc định an toàn”

Không. Popularity không phải cryptographic provenance và không chứng minh absence of backdoor.

### “Validation accuracy cao thì không có backdoor”

Không. Backdoor có thể được thiết kế để giữ behavior bình thường gần như không đổi.

### “Fine-tune nhỏ không thể phá safety của base model”

Không. Adaptation nhỏ vẫn có thể thay đổi behavior hoặc làm mất một số guardrail đã học.

## Liên kết kiến thức

Nên đọc cùng [Data Governance](../14_data_for_ai/08_data_governance.md), [Model Registry](../16_mlops_and_llmops/03_model_registry.md), [CI/CD/CT](../16_mlops_and_llmops/04_ci_cd_ct_for_ai.md), [Adversarial ML](./04_adversarial_machine_learning.md), [Supply-Chain Security](./07_model_and_supply_chain_security.md) và [Incident Response](../16_mlops_and_llmops/09_incident_response_and_lifecycle.md).