# CI/CD/CT cho Hệ thống AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **CI/CD/CT cho hệ thống AI**. Route đi từ code/data checks → training validation → model packaging → continuous deployment/testing → production guardrails, để automation kiểm tra cả phần mềm lẫn hành vi model.

Trong phần mềm truyền thống, **CI/CD** chủ yếu kiểm tra mã nguồn và triển khai ứng dụng. Hệ thống AI cần thêm kiểm tra cho dữ liệu, sản phẩm tạo ra (artifact / 산출물) mô hình và hành vi. Vì vậy MLOps thường nói tới **CI/CD/CT**: tích hợp liên tục (Continuous Integration), phân phối/triển khai liên tục (Continuous Delivery/Deployment) và huấn luyện liên tục (Continuous Training).

## Tích hợp liên tục

CI cho AI nên kiểm nhiều lớp:

```text
unit test cho mã nguồn
kiểm tra schema / hợp đồng dữ liệu
kiểm tra phép biến đổi đặc trưng
smoke test cho huấn luyện
kiểm tra serialization / load
kiểm tra signature của mô hình
kiểm tra hợp lý của đánh giá
kiểm tra bảo mật / static analysis
```

Một chuỗi xử lý (pipeline / 파이프라인) có thể thất bại dù mã nguồn biên dịch bình thường nếu lược đồ (schema / 스키마) upstream thay đổi hoặc phân phối đặc trưng bất thường.

Các kiểm tra mã nguồn chỉ là lớp đầu tiên; với AI, tính hợp lệ của dữ liệu cũng quyết định pipeline có đáng tin hay không. Vì vậy, bước kế tiếp là kiểm tra các đặc tính có thể làm thay đổi đầu vào huấn luyện.

## Kiểm tra dữ liệu

Ví dụ:

- tỷ lệ null;
- khoảng giá trị;
- vocabulary của category;
- tỷ lệ bản ghi trùng;
- độ mới;
- tính đúng theo thời điểm (point-in-time correctness);
- khả năng sẵn có của nhãn.

Kiểm tra dữ liệu không chứng minh dữ liệu “đúng hoàn toàn”, nhưng giúp chặn nhiều thất bại (failure / 실패) phổ biến trước khi huấn luyện.

Kiểm tra dữ liệu giúp chặn lỗi sớm nhưng không thay thế việc chạy thử toàn bộ chuỗi xử lý. Một smoke test nhỏ là cách rẻ để xác nhận pipeline vẫn thực thi và tạo ra artifact có thể dùng được.

## Smoke kiểm thử (test / 테스트) cho Huấn luyện

Không cần huấn luyện toàn bộ mô hình trong CI. Có thể chạy trên tập con nhỏ để xác nhận chuỗi xử lý (pipeline / 파이프라인) thực thi end-to-end, mất mát (loss / 손실) hữu hạn và sản phẩm tạo ra (artifact / 산출물) có thể được tải lại.

Huấn luyện đầy đủ thường chạy ở một job điều phối riêng.

Smoke test xác nhận khả năng chạy; delivery và deployment quyết định cách đưa artifact đã xác nhận qua các môi trường. Trước khi tự động hóa bước đó, cần nêu rõ cổng chất lượng và quyền phê duyệt.

## Phân phối liên tục và Triển khai liên tục

**Continuous Delivery** đảm bảo ứng viên luôn ở trạng thái có thể triển khai nhưng việc thăng cấp lên môi trường vận hành (production / 운영 환경) vẫn cần phê duyệt.

**Continuous triển khai (deployment / 배포)** tự động đưa thay đổi đã vượt qua gate vào môi trường vận hành (production / 운영 환경).

Với AI có rủi ro cao, delivery kết hợp phê duyệt có kiểm soát thường phù hợp hơn triển khai hoàn toàn tự động.

Các gate biến yêu cầu triển khai thành quyết định có thể kiểm tra, còn huấn luyện liên tục tạo ra các ứng viên mới. Hai vòng này cần nối với nhau nhưng không được coi là cùng một quyết định.

## Cổng cho Triển khai Mô hình

Ứng viên có thể cần vượt qua:

```text
cổng chất lượng offline
bộ regression test
cổng độ trễ / chi phí
cổng fairness / safety
cổng tương thích
cổng shadow / canary
```

Ngưỡng của gate nên được phiên bản (version / 버전) hóa và có thể rà soát (review / 검토).

CT có thể tạo ra một artifact mới sau mỗi trigger, nhưng artifact đó vẫn phải đi qua đánh giá và phê duyệt. Vì thế cần phân biệt rõ điều gì kích hoạt huấn luyện lại và điều gì kích hoạt rollout.

## Huấn luyện liên tục

CT có thể tự động hoặc bán tự động kích hoạt huấn luyện lại khi:

- tới lịch;
- đã có đủ nhãn mới;
- drift vượt ngưỡng;
- mùa vụ kinh doanh thay đổi;
- nguồn dữ liệu được cập nhật.

Nhưng huấn luyện lại không đồng nghĩa tự động thăng cấp.

```text
kích hoạt huấn luyện
→ đánh giá
→ đăng ký ứng viên
→ so sánh với champion
→ phê duyệt / thăng cấp
```

Hai trigger tách biệt giúp tránh huấn luyện lại ngoài ý muốn hoặc triển khai một artifact chưa được đánh giá. Khi rollout không đạt yêu cầu, quy trình cần có đường quay về bản phát hành tương thích trước đó.

## Trigger Huấn luyện lại và Trigger Triển khai lại

Có thể huấn luyện lại nhưng không triển khai nếu mô hình mới không tốt hơn. Ngược lại có thể triển khai lại cùng mô hình vì hạ tầng hoặc thời gian chạy (runtime / 런타임) được vá mà không cần huấn luyện lại.

Tách hai khái niệm này làm vòng đời rõ hơn.

Rollback bảo vệ người dùng khi phiên bản mới có vấn đề, nhưng vẫn cần quan sát phiên bản mới trong phạm vi nhỏ trước khi mở rộng. Canary cung cấp một cơ chế kiểm chứng như vậy.

## Quay lui (rollback / 롤백)

Quay lui (rollback / 롤백) cần khôi phục bộ mô hình, tokenizer/preprocessor, prompt và cấu hình tương thích. Nếu cơ sở dữ liệu (database / 데이터베이스) hoặc chỉ mục (index / 인덱스) lược đồ (schema / 스키마) đã migrate theo cách không tương thích, chỉ quay lui (rollback / 롤백) mô hình có thể vẫn thất bại.

Canary cho phép phiên bản mới ảnh hưởng một phần traffic và có thể quay lui nhanh. Nếu muốn quan sát mà không ảnh hưởng đầu ra người dùng, ta dùng shadow deployment.

## Triển khai Canary

Chỉ chuyển một tỷ lệ traffic tới ứng viên rồi theo dõi chỉ số hệ thống và chỉ số chất lượng/kinh doanh.

Canary cần chú ý thiên lệch lựa chọn (selection bias): tập traffic phải đủ đại diện hoặc kết quả phải được diễn giải đúng.

Shadow giữ đầu ra của ứng viên ngoài luồng người dùng, nên phù hợp để đo hành vi trên traffic thật trước khi quyết định. Với LLM, phép đo đó cần mở rộng từ độ trễ sang chất lượng và an toàn của đầu ra.

## Triển khai Shadow

Ứng viên nhận bản sao yêu cầu (request / 요청) nhưng đầu ra (output / 출력) không ảnh hưởng người dùng. Cách này hữu ích để đo độ trễ và hành vi trên traffic thật.

Shadow có thể gần như nhân đôi chi phí suy luận và vẫn phải tuân thủ kiểm soát quyền riêng tư.

LLM đưa thêm prompt, retrieval và tool vào bề mặt thay đổi, nên bộ kiểm thử phải bao quát cả hành vi. Những thành phần này cũng cần được versioning và review như mã nguồn.

## CI/CD cho LLM

Ứng dụng LLM có thể thay đổi prompt, retrieval, công cụ (tool / 도구) hoặc mô hình (model / 모델) provider. CI nên có bộ kiểm thử hành vi (behavioral test set) cho:

```text
độ đúng của câu trả lời
mức hỗ trợ của citation
độ tuân thủ JSON / schema
lựa chọn tool
trường hợp từ chối / bảo mật
trường hợp prompt injection
chi phí / độ trễ
```

So sánh chuỗi chính xác thường quá giòn với đầu ra (output / 출력) sinh nội dung; nên dùng kiểm tra có cấu trúc hoặc đánh giá bằng verifier khi phù hợp.

Versioning pipeline giúp xem diff và tái lập một lần chạy, nhưng pipeline vẫn hoạt động trong các môi trường chứa secret và quyền khác nhau. Vì vậy, kiểm soát secret phải là một phần của cùng hợp đồng triển khai.

## Chuỗi xử lý (pipeline / 파이프라인) như Mã nguồn

Chuỗi xử lý (pipeline / 파이프라인) huấn luyện và triển khai nên được phiên bản (version / 버전) hóa như mã nguồn để có thể rà soát (review / 검토) diff, tái lập và quay lui (rollback / 롤백).

Cấu hình chỉ tồn tại trong UI thủ công dễ tạo trạng thái ẩn khó truy vết.

Tách secret và môi trường làm giảm nguy cơ lộ credential và giúp mỗi bước được cấp đúng quyền. Các phần trên có thể được cô đọng thành ba vai trò: kiểm tra, tạo artifact và đưa artifact đi qua môi trường.

## Secret và Môi trường

Log của huấn luyện (training / 학습) hoặc CI không được làm lộ API key, credential hoặc dữ liệu nhạy cảm. Quyền giữa dev, staging và môi trường vận hành (production / 운영 환경) nên được tách rõ.

Sơ đồ này tách CI, CT và CD theo việc chúng chứng minh, tạo ra và phân phối điều gì. Các hiểu lầm sau thường xuất hiện khi ba vai trò bị gộp thành một nút “tự động triển khai”.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
CI → chứng minh thay đổi nhất quán nội bộ
CT → tạo artifact đã học mới
CD → đưa artifact đã được phê duyệt qua các môi trường một cách an toàn
```

Các ví dụ trên cho thấy tự động hóa chỉ đáng tin khi mỗi gate, artifact và môi trường đều có bằng chứng tương ứng. Các liên kết dưới đây nối mạch CI/CD/CT với registry, monitoring, drift và LLMOps.

## Những nhầm lẫn thường gặp

### “Continuous huấn luyện (training / 학습) nghĩa là luôn huấn luyện mô hình mới nhất”

Không. Tần suất huấn luyện phải dựa trên dữ liệu, giá trị và chi phí, không phải chỉ vì có thể tự động hóa.

### “Vượt benchmark offline thì nên tự động triển khai”

Không. Phân phối môi trường vận hành (production / 운영 환경) và ràng buộc hệ thống có thể khác.

### “CI của LLM chỉ cần kiểm tra cú pháp prompt”

Không. Regression về hành vi, bảo mật và retrieval mới là phần khó.


## Liên kết kiến thức

Xem [Model Registry](./03_model_registry.md), [Monitoring](./06_monitoring_and_observability.md), [Drift](./07_drift_and_retraining.md), [LLMOps](./08_llmops.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
