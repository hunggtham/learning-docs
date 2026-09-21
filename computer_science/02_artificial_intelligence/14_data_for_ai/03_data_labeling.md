# Gán nhãn Dữ liệu

**Gán nhãn dữ liệu (data labeling / 데이터 라벨링)** biến các raw example thành supervision signal mà mô hình dùng để tối ưu. Label không tự nhiên xuất hiện từ thực tế rồi rơi thẳng vào dataset; nó thường được tạo bởi rule, human judgment, downstream outcome hoặc một model khác. Vì vậy label luôn có ngữ nghĩa, độ bất định và một quy trình tạo phía sau.

## Ground Truth không phải lúc nào cũng Tuyệt đối

Một số label gần như deterministic:

```text
invoice total = numeric field chính xác
object class = catalog ID đã biết
```

Nhưng nhiều label mang tính chủ quan hoặc latent:

```text
toxicity
sentiment
medical diagnosis
fraud intent
helpfulness
image quality
```

Trong những trường hợp này, disagreement giữa annotator có thể phản ánh ambiguity thật của task chứ không đơn giản là ai đó “gán nhãn sai”.

## Định nghĩa Label

Trước khi annotation, cần có specification rõ:

- label đại diện cho điều gì;
- ranh giới positive/negative;
- edge case;
- lựa chọn unknown hoặc abstain;
- temporal cutoff;
- quy tắc multi-label;
- example và counterexample.

Nếu guideline mơ hồ, mô hình sẽ học chính sự không nhất quán đó.

## Label dựa trên Outcome

Label có thể đến từ một sự kiện xảy ra trong tương lai:

```text
customer churn trong 30 ngày
transaction trở thành chargeback
loan default trong 12 tháng
```

Cần định nghĩa **cửa sổ quan sát (observation window)** và thời điểm label đủ trưởng thành. Nếu tạo training set quá sớm, nhiều sample chưa kịp phát sinh outcome sẽ bị gán false negative.

## Proxy Label

Khi mục tiêu thật khó đo trực tiếp, ta thường dùng proxy:

```text
click → interest
watch time → satisfaction
manual review result → fraud truth
```

Rủi ro cốt lõi là **proxy mismatch**. Mô hình tối ưu proxy được đưa vào dữ liệu, không tự hiểu concept thật mà designer mong muốn.

## Human Annotation

Một human-labeling pipeline đáng tin cần ít nhất:

```text
instruction
training / calibration
annotation UI
quality check
adjudication
feedback loop
```

UX của tool ảnh hưởng trực tiếp tới label quality. Nếu giao diện crop mất context hoặc ẩn metadata cần thiết, annotator không thể đưa ra label chính xác dù guideline tốt.

## Mức độ Đồng thuận giữa Annotator

Agreement đo mức độ nhất quán giữa người gán nhãn. Percent agreement đơn giản có thể trông cao giả tạo khi một class chiếm đa số.

Với hai annotator, **Cohen’s kappa** có thể dùng:

\[
\kappa=\frac{p_o-p_e}{1-p_e}
\]

Trong đó `p_o` là agreement quan sát được và `p_e` là agreement kỳ vọng do ngẫu nhiên.

Agreement thấp có thể báo hiệu guideline chưa rõ hoặc task vốn có tính chủ quan cao.

## Majority Vote

Khi có nhiều label cho cùng sample, majority vote là cách tổng hợp đơn giản nhưng nó làm mất uncertainty và mặc định mọi annotator đáng tin như nhau.

Các lựa chọn khác gồm:

- weighted annotator;
- probabilistic label model;
- adjudicator;
- soft target distribution.

## Soft Label

Nếu 7/10 annotator chọn A và 3/10 chọn B, có thể giữ target distribution:

\[
y=[0.7,0.3]
\]

thay vì ép thành hard label `[1,0]`.

Soft label giữ lại thông tin về ambiguity và disagreement tốt hơn trong những task có nhiều interpretation hợp lý.

## Expert Label và Crowd Label

Các domain như radiology hoặc legal review thường cần expert knowledge. Crowd labeling rẻ hơn nhưng có thể thiếu competence chuyên ngành.

Một pipeline lai có thể để crowd xử lý case dễ, còn expert adjudicate những case khó hoặc disagreement cao.

## Annotation Bias

Annotator mang theo background văn hóa, kiến thức và prior riêng. Người thiết kế guideline cũng encode value và assumption vào định nghĩa label.

Diverse annotator pool cùng subgroup analysis giúp phát hiện những vùng disagreement có hệ thống thay vì chỉ nhìn overall agreement.

## Blind Annotation

Nếu annotator nhìn thấy model prediction trước khi label, **anchoring bias** có thể xảy ra.

Khi xây independent gold data, UI nên cân nhắc ẩn model output để human judgment không bị kéo theo dự đoán hiện tại của hệ thống.

## Active Learning

Trong **học chủ động (active learning)**, model chọn những sample bất định hoặc có giá trị thông tin cao để đưa cho con người label.

Cách này có thể giảm chi phí annotation, nhưng tập sample được chọn lại phụ thuộc chính model hiện tại. Vì vậy vẫn nên giữ một phần random audit hoặc exploration để không bỏ sót systematic blind spot.

## Weak Supervision

**Weak supervision** tạo label từ heuristic, rule hoặc knowledge source thay vì human annotation trực tiếp, ví dụ:

```text
keyword rule
regex
existing classifier
business rule
```

Nhiều labeling function có nhiễu có thể được kết hợp bằng probabilistic model. Cách này scale tốt nhưng vẫn kế thừa bias của rule.

## Pseudo-Labeling

Một mô hình được train trên labeled data có thể dự đoán unlabeled data, sau đó dùng các prediction có confidence cao làm **pseudo-label**.

Rủi ro chính là self-reinforcing error: model sai ở đâu có thể tiếp tục tạo thêm data sai cùng hướng. Thresholding, teacher model và consistency method giúp giảm nhưng không loại bỏ hoàn toàn vấn đề này.

## Label do LLM tạo

LLM có thể gán nhãn text hoặc image ở quy mô lớn, nhưng nên xem nó như một **annotator có nhiễu**, không phải oracle.

Cần:

- benchmark với human gold set;
- kiểm tra subgroup bias;
- lưu model version và prompt version;
- tránh vòng lặp nơi cùng một model family vừa tạo label vừa tự đánh giá label đó.

## Label Leakage

Quy trình annotation có thể vô tình dùng thông tin không có sẵn tại thời điểm inference.

Ví dụ analyst nhìn thấy chargeback cuối cùng rồi dùng thông tin đó để gán nhãn “suspicious at transaction time”. Training label lúc này chứa future information.

Câu hỏi quan trọng là:

> **Annotator được phép biết những gì tương ứng với prediction time?**

## Label Noise

Random noise đối xứng và class-dependent noise ảnh hưởng learning algorithm khác nhau. Deep neural network có khả năng cuối cùng memorize cả label sai nếu train đủ lâu.

Early stopping, robust loss, sample reweighting hoặc relabeling có thể giúp, nhưng tốt nhất vẫn là sửa source process nếu có thể.

## Positive–Unlabeled Learning

Đôi khi ta chỉ biết chắc một số positive, còn phần unlabeled chứa cả negative thật lẫn positive chưa được phát hiện.

Nếu coi toàn bộ unlabeled là negative, dataset sẽ bị bias. **Positive–Unlabeled learning (PU learning)** mô hình hóa trường hợp này rõ hơn.

## Multi-Label Annotation

Một object hoặc document có thể thuộc nhiều class cùng lúc. Annotation UI nên cho phép chọn tất cả label phù hợp thay vì ép thành một class duy nhất nếu semantics thực sự là multi-label.

## Hierarchical Label

Taxonomy có thể có cấu trúc phân cấp:

```text
vehicle
├── car
└── truck
```

Annotator đôi khi chỉ chắc chắn ở parent level. Hệ thống nên lưu đúng granularity đó thay vì bắt buộc đoán xuống leaf class.

## Span, Box và Mask Label

Label có cấu trúc còn có vấn đề alignment và geometry. Bounding box “tight” hay “loose”, text-span boundary hoặc segmentation contour đều cần guideline rõ.

Nếu policy annotation không nhất quán, model sẽ học một target geometry không ổn định.

## Versioning cho Label

Taxonomy có thể thay đổi theo thời gian:

```text
v1: fraud / not fraud
v2: account takeover / card theft / friendly fraud / clean
```

Dataset và model lịch sử phải biết label schema version nào đã được dùng. Thay đổi taxonomy đôi khi đòi hỏi relabeling chứ không chỉ rename field.

## Gold Set

Nên duy trì một **gold set** chất lượng cao được review kỹ, tách khỏi annotation thông thường.

Không nên liên tục tune guideline và model trực tiếp theo hidden test examples cho tới khi test set trở thành training signal gián tiếp.

## Annotation QA

Một số kỹ thuật QA gồm:

- hidden known-answer task;
- overlap giữa nhiều annotator;
- consistency check;
- constraint loại impossible label;
- review sample disagreement cao;
- drift monitoring theo thời gian.

## Chi phí và Chất lượng

Annotation budget nên tập trung vào vùng bất định, hiếm hoặc có impact cao.

Một triệu weak label có thể kém giá trị hơn 50 nghìn label nhất quán và đúng domain nếu mục tiêu là production reliability.

## Mô hình tư duy

> **Label là phép đo của target concept, không phải chính concept đó. Chất lượng mô hình bị giới hạn bởi cách target được operationalize và đo lường.**

## Những nhầm lẫn thường gặp

### “Human label chính là ground truth”

Không. Human có thể disagreement, thiếu context hoặc làm theo guideline bị lỗi.

### “Majority vote luôn tạo ra truth”

Không. Nó có thể xóa mất interpretation thiểu số nhưng hợp lệ.

### “LLM label là cách scale miễn phí”

Không. Nó chỉ chuyển annotation error sang model bias và prompt bias, nên vẫn cần validation.

## Liên kết kiến thức

Gán nhãn dữ liệu nối Measurement Theory, HCI, Statistics, Weak Supervision và Evaluation.

Xem tiếp: [Chất lượng Dữ liệu](./04_data_quality.md).