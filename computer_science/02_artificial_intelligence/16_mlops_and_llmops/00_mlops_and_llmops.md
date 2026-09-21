# MLOps và LLMOps là gì?

**Vận hành học máy (Machine Learning Operations — MLOps / 머신러닝 운영)** là tập hợp thực hành, kiến trúc và quy trình giúp hệ thống học máy (Machine Learning) có thể được phát triển, triển khai, quan sát, tái lập và cải tiến một cách có kiểm soát trong môi trường production. **LLMOps** mở rộng cùng bài toán quản lý vòng đời (lifecycle) sang mô hình ngôn ngữ lớn (Large Language Model — LLM), RAG, prompt, agent và pipeline đánh giá.

MLOps không đơn giản là “DevOps cộng thêm một tệp mô hình”. Hệ thống ML có thêm nhiều thành phần thay đổi theo thời gian mà phần mềm truyền thống ít gặp hơn: tập dữ liệu thay đổi, phân phối mục tiêu bị trôi (drift), quá trình huấn luyện không hoàn toàn xác định, dòng nguồn gốc của đặc trưng (feature lineage), chỉ số mô hình, metadata của thí nghiệm và quyết định huấn luyện lại.

## Vì sao DevOps chưa đủ?

Một dịch vụ web thường triển khai mã nguồn và cấu hình. Dịch vụ ML còn phụ thuộc vào:

```text
mã nguồn
+ snapshot dữ liệu
+ định nghĩa đặc trưng
+ kiến trúc mô hình
+ cấu hình huấn luyện
+ random seed
+ dependency
+ phần cứng / runtime
+ trọng số đã học
+ tập dữ liệu đánh giá
```

Nếu thiếu một thành phần, ta có thể không tái lập được mô hình dù mã nguồn giống hệt.

## Vòng đời ML

```text
định nghĩa bài toán
→ thu thập dữ liệu
→ kiểm tra dữ liệu
→ đặc trưng / biểu diễn
→ thí nghiệm
→ huấn luyện
→ đánh giá
→ đăng ký
→ phê duyệt
→ triển khai
→ giám sát
→ thu phản hồi
→ huấn luyện lại / rollback / ngừng sử dụng
```

MLOps quản lý các chuyển tiếp giữa những giai đoạn này.

## Vòng đời LLMOps

Ứng dụng LLM thường có thêm:

```text
mô hình nền / phiên bản API
system prompt
prompt template
chỉ mục truy xuất
mô hình embedding
reranker
chính sách ngữ cảnh
công cụ / hàm
workflow của agent
bộ đánh giá
chính sách an toàn
```

Chỉ cần thay đổi cách chia đoạn (chunking) hoặc system prompt cũng có thể làm hành vi thay đổi dù trọng số mô hình giữ nguyên.

## Khả năng tái lập

Mục tiêu không nhất thiết là kết quả giống hệt từng bit; nhiều lần huấn luyện phân tán vẫn có tính không xác định. Nhưng cần đủ metadata để trả lời:

```text
mô hình này được tạo từ đâu?
dùng dữ liệu nào?
commit mã nguồn nào?
cấu hình nào?
bộ đánh giá nào?
ai phê duyệt?
đang phục vụ ở đâu?
```

Đó là **dòng nguồn gốc (lineage / 계보)**.

## Theo dõi thí nghiệm

Theo dõi thí nghiệm (experiment tracking) không chỉ lưu chỉ số cuối cùng. Nên lưu tham số, phiên bản tập dữ liệu, SHA của mã nguồn, artifact, môi trường, phần cứng, random seed và kết quả đánh giá theo từng lát dữ liệu.

Nếu chỉ số tăng nhưng phiên bản dữ liệu cũng thay đổi, việc kết luận nguyên nhân cần thận trọng.

## Registry

Kho đăng ký mô hình (model registry) quản lý artifact, metadata và trạng thái vòng đời:

```text
ứng viên → đã kiểm định → staging → production → lưu trữ
```

Việc thăng cấp (promotion) nên dựa trên các cổng kiểm soát (gate) và bằng chứng rõ ràng, không dựa vào việc lập trình viên nhớ tên checkpoint.

## CI, CD và CT

- **CI**: kiểm tra mã nguồn, schema, test và hợp đồng dữ liệu.
- **CD**: triển khai mô hình hoặc ứng dụng một cách an toàn.
- **CT — Continuous Training**: huấn luyện lại theo lịch hoặc khi điều kiện phù hợp.

CT không có nghĩa tự động huấn luyện lại mỗi khi xuất hiện dữ liệu mới. Huấn luyện lại thiếu kiểm soát có thể khuếch đại nhãn xấu hoặc drift nếu không có cổng chất lượng.

## Giám sát

ML production phải theo dõi ít nhất hai lớp:

```text
sức khỏe hệ thống → độ trễ, lỗi, tài nguyên
sức khỏe mô hình   → phân phối đầu vào, dự đoán, calibration, chất lượng
```

Nhãn chất lượng thường đến trễ, nên có thể cần chỉ số thay thế (proxy metric), nhưng phải hiểu rõ giới hạn của chúng.

## Drift

Sự trôi dữ liệu (data drift) không tự động nghĩa mô hình đã hỏng; suy giảm hiệu năng mới trực tiếp liên quan tới chất lượng. Drift là tín hiệu để điều tra, không phải trigger để huấn luyện lại một cách mù quáng.

## Quản trị

Ai có quyền thăng cấp mô hình? Artifact nào được phép dùng? Tập dữ liệu có provenance và license không? Model card hoặc hồ sơ rủi ro được lưu ở đâu? Đây là **quản trị vận hành (operational governance)**, không phải giấy tờ tách rời khỏi engineering.

## Mức trưởng thành của MLOps

Một nhóm có thể phát triển theo lộ trình:

```text
notebook thủ công
→ huấn luyện bằng script
→ pipeline có version
→ registry + đánh giá tự động
→ triển khai có kiểm soát
→ observability + vòng phản hồi
→ vòng đời điều khiển bằng policy
```

Không cần xây nền tảng phức tạp ngay từ ngày đầu; nên giải quyết điểm đau thực tế trước.

## Tự xây hay dùng nền tảng có sẵn

Công cụ MLOps có thể hỗ trợ theo dõi, điều phối, registry và triển khai. Nhưng công cụ không tự định nghĩa hợp đồng dữ liệu, cổng chất lượng hoặc chính sách rollback cho tổ chức.

## Mô hình tư duy

```text
MLOps = làm cho hành vi đã học có thể truy vết, tái lập, triển khai và quản trị
LLMOps = MLOps + vòng đời của prompt / context / retrieval / tool / agent
```

## Những nhầm lẫn thường gặp

### “MLOps chỉ là Kubernetes cho ML”

Không. Kubernetes chỉ là một lựa chọn hạ tầng.

### “Có registry là đã làm MLOps”

Không. Registry không thay thế giám sát, lineage, test hay quy trình phát hành.

### “LLMOps chỉ là quản lý prompt”

Không. Hệ thống LLM còn có mô hình, truy xuất, công cụ, đánh giá, bảo mật, chi phí và trạng thái.

## Liên kết kiến thức

Nối trực tiếp [AI Engineering](../15_ai_engineering/README.md), [Data for AI](../14_data_for_ai/README.md), [RAG](../09_retrieval_and_rag/README.md) và [Agents](../10_agents_and_ai_systems/README.md).