# Đầu độc dữ liệu, cửa hậu và tấn công mô hình

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Kiến thức cần có trước** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Bề mặt tấn công của quá trình huấn luyện** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Bảo mật AI không chỉ bắt đầu ở thời điểm suy luận. Nếu attacker can thiệp vào dữ liệu huấn luyện, nhãn, checkpoint, adapter hoặc chuỗi xử lý (pipeline / 파이프라인) bản dựng (build / 빌드), hệ thống có thể bị compromise từ trước khi triển khai. **Đầu độc dữ liệu (data poisoning / 데이터 포이즈닝)** làm quá trình học hấp thụ hành vi sai hoặc có chủ đích. **Cửa hậu (backdoor / trojan)** tạo một điều kiện kích hoạt đặc biệt khiến mô hình hành xử khác thường trong một số trường hợp hiếm.

## Kiến thức cần có trước

Nên đọc [Data for AI](../14_data_for_ai/README.md), [Data Governance](../14_data_for_ai/08_data_governance.md), [Training Pipeline](../15_ai_engineering/01_training_pipeline.md), [Model Registry](../16_mlops_and_llmops/03_model_registry.md) và [Adversarial Machine Learning](./04_adversarial_machine_learning.md).

> **Chuyển mạch:** Trong **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Bề mặt tấn công của quá trình huấn luyện** tiếp nhận điểm tựa từ **Kiến thức cần có trước** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hai mục tiêu lớn của poisoning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bề mặt tấn công của quá trình huấn luyện

Một chuỗi xử lý (pipeline / 파이프라인) huấn luyện có thể lấy dữ liệu từ:

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

Mỗi nguồn có mức độ tin cậy và provenance khác nhau. Khi các nguồn này được trộn vào cùng một huấn luyện (training / 학습) corpus mà không giữ siêu dữ liệu (metadata / 메타데이터), việc điều tra nguồn gốc hành vi xấu về sau trở nên rất khó.

> **Chuyển mạch:** Ở chặng này của **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Hai mục tiêu lớn của poisoning** tiếp nhận điểm tựa từ **Bề mặt tấn công của quá trình huấn luyện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trực giác cơ chế** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hai mục tiêu lớn của poisoning

**Poisoning phá tính sẵn sàng (availability poisoning)** làm chất lượng tổng thể của mô hình giảm rõ rệt.

**Poisoning phá tính toàn vẹn (integrity poisoning)** cố giữ chỉ số (metric / 지표) tổng thể gần bình thường nhưng làm sai một hành vi, một lớp, một đầu vào (input / 입력) hoặc một nhóm trường hợp cụ thể.

Dạng thứ hai nguy hiểm hơn trong môi trường vận hành (production / 운영 환경) vì benchmark aggregate có thể vẫn tốt.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Hai mục tiêu lớn của poisoning** xác định đầu vào; **Trực giác cơ chế** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Poisoning nhãn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trực giác cơ chế

Huấn luyện tối ưu mục tiêu (objective / 목표) trên dữ liệu quan sát. Nếu một phần dữ liệu bị thay đổi có hệ thống, độ dốc (gradient / 기울기) tổng hợp cũng đổi theo. Với tập huấn luyện `D` và tập poison `P`, mục tiêu (objective / 목표) có thể hình dung như:

\[
L(\theta)=\frac{1}{|D\cup P|}
\sum_{(x,y)\in D\cup P}L(f_\theta(x),y)
\]

Nếu `P` được thiết kế để tạo độ dốc (gradient / 기울기) có ảnh hưởng lớn tới một vùng hành vi cụ thể, số mẫu poison không nhất thiết phải chiếm tỷ lệ lớn mới gây tác động. Vì vậy trực giác “dataset lớn sẽ tự pha loãng poison” không phải bảo đảm an toàn.

> **Chuyển mạch:** Trong **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Trực giác cơ chế** xác định đầu vào; **Poisoning nhãn** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Clean-label poisoning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Poisoning nhãn

**Poisoning nhãn (label poisoning)** thay đổi hoặc thao túng quá trình gán nhãn. Lỗi không nhất thiết đến từ attacker; bug trong chuỗi xử lý (pipeline / 파이프라인) label hoặc chính sách (policy / 정책) gán nhãn sai cũng có thể tạo hậu quả tương tự.

Các biện pháp môi trường vận hành (production / 운영 환경) gồm:

- lưu provenance của nhãn;
- đo agreement giữa annotator;
- phát hiện thay đổi label phân phối (distribution / 분포);
- rà soát (review / 검토) các nhóm nhãn bất thường;
- giữ một tập kiểm tra hợp lệ (validation / 검증) có nguồn kiểm soát chặt.

> **Chuyển mạch:** Ở chặng này của **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Poisoning nhãn** cho ta quy tắc; **Clean-label poisoning** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cửa hậu và trigger** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Clean-label poisoning

Trong **clean-label poisoning**, đầu vào (input / 입력) vẫn trông hợp lệ và nhãn cũng có vẻ đúng với con người, nhưng mẫu (sample / 표본) được chọn hoặc biến đổi để làm biên quyết định dịch theo hướng bất lợi. Điều này nhắc rằng “label đúng” không đồng nghĩa “mẫu (sample / 표본) vô hại”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Clean-label poisoning** cho ta quy tắc; **Cửa hậu và trigger** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cửa hậu đi vào hệ thống bằng cách nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cửa hậu và trigger

Một backdoor thường có hành vi (behavior / 동작) kiểu:

```text
input bình thường
→ mô hình hoạt động đúng

input + điều kiện kích hoạt hiếm
→ mô hình trả kết quả do attacker mong muốn
```

Trigger có thể là mẫu (pattern / 패턴) thị giác, đơn vị từ (token / 토큰), siêu dữ liệu (metadata / 메타데이터), thuộc tính ngữ cảnh hoặc một tổ hợp tính năng (feature / 기능) hiếm. Vì hành vi bình thường vẫn tốt nên benchmark tiêu chuẩn có thể bỏ sót.

> **Chuyển mạch:** Trong **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Cửa hậu đi vào hệ thống bằng cách nào?** tiếp nhận điểm tựa từ **Cửa hậu và trigger** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rủi ro từ checkpoint và serialization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Rủi ro từ checkpoint và serialization** tiếp nhận điểm tựa từ **Cửa hậu đi vào hệ thống bằng cách nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rủi ro từ adapter và mô hình (model / 모델) merging** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rủi ro từ checkpoint và serialization

Tệp (file / 파일) mô hình không nên được mặc định xem như “dữ liệu thụ động”. Một số định dạng serialization hoặc custom loading đường dẫn (path / 경로) có thể thực thi mã (code / 코드). Ngay cả khi định dạng an toàn về mã (code / 코드) thực thi (execution / 실행), trọng số vẫn có thể chứa hành vi đã bị cài backdoor.

Môi trường vận hành (production / 운영 환경) chuỗi xử lý (pipeline / 파이프라인) nên:

```text
xác minh nguồn
kiểm tra digest/signature
tránh custom code không cần thiết
load trong sandbox khi nguồn chưa tin cậy
chạy behavioral/security regression trước khi promote
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Rủi ro từ adapter và mô hình (model / 모델) merging** tiếp nhận điểm tựa từ **Rủi ro từ checkpoint và serialization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Synthetic dữ liệu (data / 데이터) và phản hồi (feedback / 피드백) poisoning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rủi ro từ adapter và mô hình (model / 모델) merging

Adapter, LoRA hoặc checkpoint merge có thể thay đổi hành vi (behavior / 동작) sâu dù kích thước sản phẩm tạo ra (artifact / 산출물) nhỏ. Vì vậy adapter phải được xem như sản phẩm tạo ra (artifact / 산출물) có quyền thay đổi hệ thống, không phải “tệp (file / 파일) phụ” vô hại.

Mọi adapter cần định danh (identity / 식별자), provenance, evaluation và approval giống mô hình (model / 모델) sản phẩm tạo ra (artifact / 산출물) chính.

> **Chuyển mạch:** Trong **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Rủi ro từ adapter và mô hình (model / 모델) merging** nêu điều cần giải thích; **Synthetic dữ liệu (data / 데이터) và phản hồi (feedback / 피드백) poisoning** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Làm sạch dữ liệu không đủ để bảo đảm an toàn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Synthetic dữ liệu (data / 데이터) và phản hồi (feedback / 피드백) poisoning

Nếu synthetic dữ liệu (data / 데이터) được sinh từ một mô hình (model / 모델) đã có độ lệch (bias / 편향) hoặc compromise rồi quay lại làm dữ liệu huấn luyện (training data / 학습 데이터), lỗi có thể tự khuếch đại. Tương tự, môi trường vận hành (production / 운영 환경) phản hồi (feedback / 피드백) có thể bị thao túng bằng hành vi phối hợp, spam rating hoặc tạo nhiều tương tác giả.

Không nên đưa phản hồi (feedback / 피드백) trực tiếp vào continuous huấn luyện (training / 학습) nếu chưa qua trust weighting, anomaly detection, delayed kiểm tra hợp lệ (validation / 검증) hoặc sampling rà soát (review / 검토).

> **Chuyển mạch:** Ở chặng này của **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Synthetic dữ liệu (data / 데이터) và phản hồi (feedback / 피드백) poisoning** nêu điều cần giải thích; **Làm sạch dữ liệu không đủ để bảo đảm an toàn** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Tập kiểm tra hợp lệ (validation / 검증) có provenance tin cậy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Làm sạch dữ liệu không đủ để bảo đảm an toàn

Các phép kiểm như duplicate, outlier, nguồn (source / 소스) reputation, label inconsistency và anomalous cluster có ích nhưng không thể chứng minh mọi poison đã được loại bỏ. Attack có thể được thiết kế để trông giống phân phối bình thường.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Làm sạch dữ liệu không đủ để bảo đảm an toàn** nêu điều cần giải thích; **Tập kiểm tra hợp lệ (validation / 검증) có provenance tin cậy** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Phân tích ảnh hưởng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tập kiểm tra hợp lệ (validation / 검증) có provenance tin cậy

Một tập kiểm tra hợp lệ (validation / 검증) nhỏ nhưng được kiểm soát tốt có thể đóng vai trò anchor. Nó giúp phát hiện candidate mô hình (model / 모델) có hành vi (behavior / 동작) khác thường so với known-good mô hình (model / 모델).

Tuy nhiên nếu attacker cũng có thể thao túng kiểm tra hợp lệ (validation / 검증) set thì lớp này mất giá trị. Vì vậy quyền ghi vào evaluation assets cũng là một ranh giới bảo mật (security boundary / 보안 경계).

> **Chuyển mạch:** Trong **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Phân tích ảnh hưởng** tiếp nhận điểm tựa từ **Tập kiểm tra hợp lệ (validation / 검증) có provenance tin cậy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phát hiện backdoor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân tích ảnh hưởng

Các kỹ thuật **phân tích ảnh hưởng (influence analysis)** cố ước lượng mẫu (sample / 표본) huấn luyện nào góp phần nhiều vào một prediction hoặc hành vi (behavior / 동작) đáng ngờ. Chúng hữu ích cho forensic investigation nhưng thường đắt và chỉ gần đúng với mô hình lớn.

Không nên coi influence score như bằng chứng tuyệt đối về nguyên nhân.

> **Chuyển mạch:** Ở chặng này của **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Phát hiện backdoor** tiếp nhận điểm tựa từ **Phân tích ảnh hưởng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình triển khai an toàn hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phát hiện backdoor

Có thể kiểm tra:

- activation bất thường;
- sensitivity với mẫu (pattern / 패턴) hiếm;
- thay đổi hành vi (behavior / 동작) theo trigger candidate;
- regression trên tập red-team;
- khác biệt giữa mô hình (model / 모델)/adapter lineage.

Không có một detector duy nhất bao phủ mọi backdoor. False positive và false negative đều cần được xem xét.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Mô hình triển khai an toàn hơn** tiếp nhận điểm tựa từ **Phát hiện backdoor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quyền tối thiểu trong huấn luyện (training / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình triển khai an toàn hơn

Một training-to-production luồng (flow / 흐름) nên có dạng:

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

Điểm quan trọng là mỗi mũi tên phải có lineage để truy ngược khi sự cố (incident / 인시던트) xảy ra.

> **Chuyển mạch:** Trong **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Quyền tối thiểu trong huấn luyện (training / 학습)** tiếp nhận điểm tựa từ **Mô hình triển khai an toàn hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dạng thất bại (failure mode / 실패 모드) ở môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quyền tối thiểu trong huấn luyện (training / 학습)

Huấn luyện (training / 학습) job thường chỉ cần đọc dataset và ghi sản phẩm tạo ra (artifact / 산출물). Nó không nên mặc định có quyền quản trị môi trường vận hành (production / 운영 환경) cơ sở dữ liệu (database / 데이터베이스), registry hoặc secret rộng hơn mức cần thiết.

**Nguyên tắc quyền tối thiểu (least privilege)** giảm blast radius nếu notebook, phụ thuộc (dependency / 의존성) hoặc worker bị compromise.

> **Chuyển mạch:** Ở chặng này của **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Dạng thất bại (failure mode / 실패 모드) ở môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **Quyền tối thiểu trong huấn luyện (training / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ứng phó sự cố** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dạng thất bại (failure mode / 실패 모드) ở môi trường vận hành (production / 운영 환경)

**Poisoning không làm chỉ số (metric / 지표) aggregate giảm.** Hành vi xấu chỉ xuất hiện ở slice hiếm.

**kiểm tra hợp lệ (validation / 검증) dùng cùng nguồn với huấn luyện (training / 학습).** Một nguồn lỗi có thể làm cả train và kiểm tra hợp lệ (validation / 검증) cùng sai.

**Không có lineage.** Khi phát hiện issue không biết mô hình (model / 모델) nào dùng dataset hoặc adapter bị ảnh hưởng.

**sản phẩm tạo ra (artifact / 산출물) mutable.** Tag cũ bị ghi đè khiến quay lui (rollback / 롤백) không còn xác định.

**vòng phản hồi (feedback loop / 피드백 루프) tự động.** Bad đầu ra (output / 출력) tạo bad phản hồi (feedback / 피드백) rồi lại quay vào huấn luyện (training / 학습).

**Adapter được trust quá mức.** Một LoRA nhỏ được promote mà không qua bảo mật (security / 보안) regression.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Ứng phó sự cố** tiếp nhận điểm tựa từ **Dạng thất bại (failure mode / 실패 모드) ở môi trường vận hành (production / 운영 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Với hệ thống có nhiều tenant hoặc công cụ (tool / 도구) quyền cao, có thể cần đồng thời thu hồi credential hoặc vô hiệu hóa workflow liên quan.

> **Chuyển mạch:** Trong **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **Ứng phó sự cố** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự đánh đổi (trade-off / 트레이드오프)

Kiểm soát provenance, immutable artifacts và bảo mật (security / 보안) evaluation làm chuỗi xử lý (pipeline / 파이프라인) chậm hơn và tăng lưu trữ (storage / 저장소)/compute chi phí (cost / 비용). Nhưng bỏ các lớp này khiến sự cố khó điều tra và khôi phục (recovery / 복구) đắt hơn nhiều.

Mức độ kiểm soát nên tỷ lệ với impact: mô hình (model / 모델) thử nghiệm nội bộ có thể dùng gate nhẹ hơn hệ thống tài chính, danh tính hoặc tác nhân (agent / 에이전트) có side tác động (effect / 효과).

> **Chuyển mạch:** Ở chặng này của **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Mô hình tư duy** gom các mảnh từ **Sự đánh đổi (trade-off / 트레이드오프)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> **Nếu dữ liệu, nhãn hoặc sản phẩm tạo ra (artifact / 산출물) đầu vào không đáng tin, hành vi đã học cũng là một phần của chuỗi cung ứng cần được bảo vệ.**

Bảo mật (security / 보안) của mô hình (model / 모델) bắt đầu từ nguồn dữ liệu và chuỗi xử lý (pipeline / 파이프라인) tạo ra mô hình (model / 모델), không chỉ từ endpoint suy luận (inference / 추론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Dataset lớn tự động pha loãng poison”

Không. Targeted poisoning hoặc backdoor có thể tạo tác động lớn trên một vùng hành vi nhỏ.

### “Checkpoint nổi tiếng thì mặc định an toàn”

Không. Popularity không phải cryptographic provenance và không chứng minh absence of backdoor.

### “kiểm tra hợp lệ (validation / 검증) accuracy cao thì không có backdoor”

Không. Backdoor có thể được thiết kế để giữ hành vi (behavior / 동작) bình thường gần như không đổi.

### “Fine-tune nhỏ không thể phá an toàn (safety / 안전) của cơ sở (base / 기반) mô hình (model / 모델)”

Không. Adaptation nhỏ vẫn có thể thay đổi hành vi (behavior / 동작) hoặc làm mất một số guardrail đã học.

> **Chuyển mạch:** Trong **Đầu độc dữ liệu, cửa hậu và tấn công mô hình**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Nên đọc cùng [Data Governance](../14_data_for_ai/08_data_governance.md), [Model Registry](../16_mlops_and_llmops/03_model_registry.md), [CI/CD/CT](../16_mlops_and_llmops/04_ci_cd_ct_for_ai.md), [Adversarial ML](./04_adversarial_machine_learning.md), [Supply-Chain Security](./07_model_and_supply_chain_security.md) và [Incident Response](../16_mlops_and_llmops/09_incident_response_and_lifecycle.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
