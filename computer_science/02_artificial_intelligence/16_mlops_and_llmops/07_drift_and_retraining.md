# Drift, Thay đổi Phân phối và Huấn luyện lại

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Drift, distribution change và retraining**. Route đi từ covariate/label/concept drift → detection windows → impact on metrics → retraining trigger → validation and rollback, để cập nhật model dựa trên tác động chứ không chỉ biến động thống kê.

Một mô hình được huấn luyện trên phân phối lịch sử nhưng thế giới môi trường vận hành (production / 운영 환경) luôn thay đổi. **Độ trôi (drift / 드리프트)** mô tả sự thay đổi của quá trình tạo dữ liệu hoặc mối quan hệ giữa đầu vào và mục tiêu theo thời gian. Drift quan trọng vì chất lượng mô hình phụ thuộc vào các giả định về phân phối.

## Dữ liệu (data / 데이터) Drift

Nếu:

\[
P_{train}(X)\neq P_{prod}(X)
\]

thì phân phối đầu vào đã thay đổi.

Ví dụ: tỷ lệ thiết bị, ngôn ngữ hoặc phân phối số tiền giao dịch của khách hàng thay đổi.

Dữ liệu (data / 데이터) drift không tự động nghĩa dự đoán đã sai. Mô hình có thể vẫn khái quát hóa tốt.

Từ đây, cần phân biệt thay đổi nhãn và prior để biết cơ chế nào đang diễn ra.

## Label Shift hoặc Prior Shift

Tỷ lệ nền của lớp thay đổi:

\[
P_{train}(Y)\neq P_{prod}(Y)
\]

Ví dụ tỷ lệ gian lận tăng sau một chiến dịch tấn công.

Ngưỡng hoặc calibration có thể cần điều chỉnh ngay cả khi cấu trúc `P(Y|X)` vẫn tương đối ổn định.

So sánh tiếp với concept drift giúp tách thay đổi quan hệ khỏi thay đổi tỷ lệ lớp.

## Concept Drift

Mối quan hệ giữa đầu vào và mục tiêu thay đổi:

\[
P_{train}(Y|X)\neq P_{prod}(Y|X)
\]

Đây thường là dạng nguy hiểm nhất: mẫu (pattern / 패턴) từng có tính dự đoán không còn đúng.

Ví dụ kẻ gian thay đổi hành vi sau khi biết quy tắc (rule / 규칙) hoặc mô hình (model / 모델).

Covariate shift tập trung vào đầu vào, nên là bước kiểm tra tiếp theo khi phân loại drift.

## Covariate Shift

Thuật ngữ này thường dùng khi `P(X)` thay đổi nhưng giả định `P(Y|X)` vẫn ổn định. Trong một số điều kiện, reweighting có thể giúp.

Tuy nhiên cần kiểm chứng giả định thay vì chỉ gắn nhãn theo taxonomy.

Không phải biến động nào cũng là drift gây hại; mùa vụ cần được tách riêng trước khi chọn phản ứng.

## Thay đổi theo Mùa và Drift gây hại

Tính mùa vụ có thể dự đoán được và không nhất thiết là bất thường. Traffic bán lẻ cuối tuần khác ngày thường là bình thường.

Giám sát cần mốc tham chiếu phù hợp, ví dụ so sánh cùng thứ trong tuần hoặc cùng mùa thay vì một baseline tĩnh duy nhất.

Khi đã có giả thuyết về thay đổi, bước kế tiếp là chọn phương pháp phát hiện drift.

## Phát hiện Drift

Có thể dùng:

- Population Stability chỉ mục (index / 인덱스);
- KS kiểm thử (test / 테스트);
- Jensen–Shannon divergence;
- histogram theo đặc trưng;
- giám sát phân phối embedding;
- kiểm định hai mẫu bằng classifier.

Nhưng ý nghĩa thống kê không đồng nghĩa ý nghĩa kinh doanh, đặc biệt khi cỡ mẫu rất lớn.

Phát hiện ở đầu vào chưa cho biết dự đoán đã sai; prediction drift bổ sung góc nhìn từ đầu ra.

## Prediction Drift

Theo dõi phân phối của score hoặc đầu ra (output / 출력). Nếu xác suất dự đoán đột ngột thay đổi, nguyên nhân có thể là đầu vào (input / 입력) shift, thay đổi mô hình (model / 모델)/cấu hình (config / 설정) hoặc lỗi downstream.

Prediction drift là triệu chứng, không phải nguyên nhân gốc.

Để biết drift có tác động thực, cần theo dõi hiệu năng thay vì chỉ theo dõi phân phối.

## Hiệu năng (performance / 성능) Drift

Khi ground truth đến sau, có thể theo dõi trực tiếp:

```text
accuracy / F1 / AUC
calibration
hàm mất mát có tính tới chi phí
kết quả kinh doanh
```

Đây là bằng chứng mạnh hơn chỉ nhìn đầu vào (input / 입력) drift.

Vì nhãn thường đến trễ, pipeline cần cơ chế gắn nhãn và đánh giá hồi cứu.

## Nhãn đến trễ

Kết quả gian lận có thể chỉ biết sau nhiều tuần hoặc tháng. Vì vậy hệ thống cần phép nối (join / 조인) dự đoán với nhãn đến trễ bằng prediction ID và timestamp bất biến.

Nếu không lưu ngữ cảnh (context / 맥락) và phiên bản tại thời điểm dự đoán, đánh giá hồi cứu sẽ rất khó.

Khi bằng chứng đủ mạnh, trigger retraining phải gắn với ngưỡng và hành động được định nghĩa trước.

## Trigger cho Huấn luyện lại

Huấn luyện lại có thể được kích hoạt bởi:

- lịch định kỳ;
- đủ dữ liệu có nhãn mới;
- suy giảm hiệu năng;
- nguồn dữ liệu thay đổi lớn;
- chính sách (policy / 정책) hoặc nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) thay đổi.

Một ngưỡng drift đơn lẻ hiếm khi nên kích hoạt tự động việc thăng cấp mô hình mới.

Trigger mới cho biết khi nào, còn cửa sổ retraining quyết định dữ liệu nào được dùng.

## Cửa sổ Huấn luyện lại

Nên huấn luyện trên toàn bộ lịch sử hay chỉ cửa sổ gần đây? Toàn bộ lịch sử ổn định hơn nhưng chứa mẫu (pattern / 패턴) cũ; cửa sổ gần đây thích nghi nhanh hơn nhưng phương sai cao và dễ quên trường hợp hiếm.

Có thể dùng lịch sử có trọng số hoặc phát lại dữ liệu phân tầng (stratified replay).

Cửa sổ mới phải được cân bằng với nguy cơ catastrophic forgetting.

## Catastrophic Forgetting trong Continual Setting

Cập nhật mô hình theo phân phối mới có thể làm giảm khả năng cũ. Đánh giá phải giữ bộ dữ liệu lịch sử ổn định và bộ regression cho long-tail.

Để tránh tự củng cố sai lệch, hệ thống cần vòng phản hồi được kiểm soát.

## Vòng phản hồi

Quyết định của mô hình ảnh hưởng nhãn tương lai. Ví dụ mô hình tín dụng chỉ phê duyệt một nhóm người dùng, nên nhãn hoàn trả chỉ được quan sát trên nhóm đã được phê duyệt.

Huấn luyện lại trực tiếp trên dữ liệu quan sát được có thể tạo thiên lệch lựa chọn.

Các nguyên tắc này đặc biệt quan trọng với LLM và RAG, nơi nhiều thành phần có thể drift.

## Drift trong LLM và RAG

Hệ thống LLM có thể drift do:

```text
provider cập nhật mô hình
prompt thay đổi
retrieval corpus thay đổi
mô hình embedding được cập nhật
index được rebuild
phân phối truy vấn người dùng thay đổi
hành vi API của tool thay đổi
```

Không phải trường hợp nào cũng cần huấn luyện lại mô hình; nhiều khi quay lui (rollback / 롤백) cấu hình hoặc chỉ mục (index / 인덱스) mới là phản ứng đúng.

Không phải mọi drift đều cần retrain; recalibration có thể là lựa chọn rẻ hơn.

## Recalibration và Huấn luyện lại

Nếu khả năng xếp hạng hoặc phân biệt vẫn tốt nhưng xác suất bị lệch, recalibration hoặc điều chỉnh threshold có thể rẻ hơn huấn luyện lại toàn bộ.

Nếu vẫn cần thay mô hình, champion–challenger giúp so sánh an toàn trước khi thăng cấp.

## Champion–Challenger sau Huấn luyện lại

Mô hình được huấn luyện lại trở thành challenger. Nên so với champion trên bộ đánh giá cố định, bộ đánh giá gần đây và môi trường vận hành (production / 운영 환경) shadow trước khi thăng cấp.

Mô hình cũ cũng cần lộ trình ngừng sử dụng, lưu trữ và khả năng quay lui.

## Ngừng sử dụng Mô hình

Vòng đời không chỉ có huấn luyện lại. Một mô hình có thể được retire khi use trường hợp (case / 사례) không còn, nguồn dữ liệu bị ngừng hoặc có giải pháp thay thế tốt hơn.

Sản phẩm tạo ra (artifact / 산출물) đã lưu trữ vẫn cần chính sách retention phù hợp với quản trị (governance / 거버넌스).

Các quyết định trên có thể gom thành một mô hình tư duy ngắn gọn.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Drift là bằng chứng rằng thế giới hoặc pipeline đã thay đổi.
Huấn luyện lại chỉ là một trong nhiều phản ứng có thể có.
```

Những nhầm lẫn sau đây kiểm tra xem mô hình đó có bị áp dụng quá đơn giản hay không.

## Những nhầm lẫn thường gặp

### “Phân phối đặc trưng thay đổi thì mô hình chắc chắn hỏng”

Không. Cần nối shift với hiệu năng tác vụ thực tế.

### “Huấn luyện lại thường xuyên luôn tốt”

Không. Dữ liệu mới có thể nhiễu hoặc thiên lệch, và huấn luyện cũng có chi phí/rủi ro.

### “Drift chỉ là vấn đề của tabular ML”

Không. LLM, RAG và tác nhân (agent / 에이전트) cũng drift qua người dùng, corpus, công cụ (tool / 도구) và phiên bản mô hình.

Phần liên kết kiến thức đặt chủ đề cạnh monitoring, evaluation và LLMOps.

## Liên kết kiến thức

Xem [Monitoring](./06_monitoring_and_observability.md), [Continuous Training](./04_ci_cd_ct_for_ai.md), [Dataset Bias](../14_data_for_ai/06_dataset_bias.md) và [Evaluation](../18_evaluation_reliability_interpretability/README.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
