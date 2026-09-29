# Đo lường (measurement / 측정), Statistics và Replication

> **Mạch đọc:** Đọc **đo lường (measurement / 측정), Statistics và Replication** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Từ dữ liệu (data / 데이터) đến claim** sang **độ sâu (depth / 깊이) pass: đo lường (measurement / 측정) như một lập luận, không phải con số**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Đo lường (measurement / 측정) không phải cửa sổ trong suốt vào reality. Construct phải được operationalize; instrument có resolution, calibration, noise và độ lệch (bias / 편향); observed score thường là tín hiệu (signal / 신호) cộng lỗi (error / 오류). Vì vậy, một kết quả có ý nghĩa thống kê không tự cho biết tác động (effect / 효과) lớn, ổn định hay quan trọng về thực tế.

## Từ dữ liệu (data / 데이터) đến claim
Phần “Từ dữ liệu (data / 데이터) đến claim” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
construct → operational measure → sampling/design
→ estimate + uncertainty → interpretation → transportability
```

Replication kiểm tra độ ổn định của finding dưới mẫu (sample / 표본), operator, instrument hoặc ngữ cảnh (context / 맥락) khác. Replication thất bại không tự chứng minh original là false; có thể tác động (effect / 효과) phụ thuộc ngữ cảnh (context / 맥락), power thấp hoặc giao thức (protocol / 프로토콜) khác. Ngược lại, một replication thành công cũng chưa xác nhận nhân quả (causal / 인과적) story nếu thiết kế chỉ lặp lại association.

Open dữ liệu (data / 데이터), preregistration, multiverse phân tích (analysis / 분석) và meta-analysis giúp giảm researcher degrees of freedom, nhưng không loại bỏ judgment. Philosophy of science ở đây gặp statistics: calibration của claim phải tương xứng với chuỗi xử lý (pipeline / 파이프라인) tạo ra dữ liệu (data / 데이터).


> **Chuyển mạch:** Từ **Từ dữ liệu (data / 데이터) đến claim**, ta sang **độ sâu (depth / 깊이) pass: đo lường (measurement / 측정) như một lập luận, không phải con số** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Độ sâu (depth / 깊이) pass: đo lường (measurement / 측정) như một lập luận, không phải con số

### Question và definitions

Đo lường (measurement / 측정) hỏi construct nào được đại diện, bằng instrument nào, trong population nào và với lỗi (error / 오류) mô hình (model / 모델) nào. độ tin cậy (reliability / 신뢰성) (ổn định) khác validity (đo đúng construct); statistical significance khác practical importance; replication khác independent nhân quả (causal / 인과적) confirmation.

### Strongest argument và premises

Một claim đo lường mạnh cần chuỗi (chain / 사슬): construct → operationalization → calibration → sampling/thiết kế (design / 설계) → estimate + bất định (uncertainty / 불확실성) → transportability. Preregistration làm rõ quyết định (decision / 결정) trước khi thấy kết quả; replication kiểm tra robustness dưới operator, mẫu (sample / 표본) và ngữ cảnh (context / 맥락) khác. Nhưng mỗi bước vẫn có mô hình (model / 모델) choice và missingness cần công khai.

### Objection, reply và rival position

Objection: reproducibility crisis chứng minh statistics không đáng tin. Reply: nó cho thấy claim phải được phân tầng theo giao thức (protocol / 프로토콜), power, selection và đo lường (measurement / 측정) invariance; không phải mọi finding đều false. Bayesian và frequentist tools có thể trả lời câu hỏi khác nhau, nhưng cả hai đều cần prior/giả định (assumption / 가정) và calibration. Meta-analysis không tự chữa publication độ lệch (bias / 편향).

### Empirical ranh giới (boundary / 경계) và implication

Đo lường (measurement / 측정) cần sensitivity phân tích (analysis / 분석), negative controls, adversarial replication và ghi rõ ranh giới (boundary / 경계) population. Khi chỉ số (metric / 지표) trở thành mục tiêu (target / 대상), Goodhart phản hồi (feedback / 피드백) có thể làm construct biến dạng. Implication: report tác động (effect / 효과) kích thước (size / 크기), bất định (uncertainty / 불확실성), missing dữ liệu (data / 데이터), quyết định (decision / 결정) threshold và dạng thất bại (failure mode / 실패 모드); không dùng một p-value để thay thế lập luận về cơ chế (mechanism / 메커니즘) hay chính sách (policy / 정책) giá trị (value / 값).

> **Bàn giao:** Sau **Empirical ranh giới (boundary / 경계) và implication**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 models explanation and causality](./00_models_explanation_and_causality.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
