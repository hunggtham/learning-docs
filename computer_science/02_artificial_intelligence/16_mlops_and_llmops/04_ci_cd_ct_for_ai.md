# CI/CD/CT cho Hệ thống AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **CI/CD/CT cho Hệ thống AI**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tích hợp liên tục** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Kiểm tra dữ liệu** để đối chiếu nhận định với dữ liệu và nguồn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

> **Chuyển mạch:** Trong **CI/CD/CT cho Hệ thống AI**, **Tích hợp liên tục** nêu điều cần giải thích; **Kiểm tra dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Smoke kiểm thử (test / 테스트) cho Huấn luyện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **CI/CD/CT cho Hệ thống AI**, **Kiểm tra dữ liệu** nêu điều cần giải thích; **Smoke kiểm thử (test / 테스트) cho Huấn luyện** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Phân phối liên tục và Triển khai liên tục** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Smoke kiểm thử (test / 테스트) cho Huấn luyện

Không cần huấn luyện toàn bộ mô hình trong CI. Có thể chạy trên tập con nhỏ để xác nhận chuỗi xử lý (pipeline / 파이프라인) thực thi end-to-end, mất mát (loss / 손실) hữu hạn và sản phẩm tạo ra (artifact / 산출물) có thể được tải lại.

Huấn luyện đầy đủ thường chạy ở một job điều phối riêng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CI/CD/CT cho Hệ thống AI**, **Phân phối liên tục và Triển khai liên tục** tiếp nhận điểm tựa từ **Smoke kiểm thử (test / 테스트) cho Huấn luyện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cổng cho Triển khai Mô hình** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân phối liên tục và Triển khai liên tục

**Continuous Delivery** đảm bảo ứng viên luôn ở trạng thái có thể triển khai nhưng việc thăng cấp lên môi trường vận hành (production / 운영 환경) vẫn cần phê duyệt.

**Continuous triển khai (deployment / 배포)** tự động đưa thay đổi đã vượt qua gate vào môi trường vận hành (production / 운영 환경).

Với AI có rủi ro cao, delivery kết hợp phê duyệt có kiểm soát thường phù hợp hơn triển khai hoàn toàn tự động.

> **Chuyển mạch:** Trong **CI/CD/CT cho Hệ thống AI**, **Cổng cho Triển khai Mô hình** tiếp nhận điểm tựa từ **Phân phối liên tục và Triển khai liên tục** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Huấn luyện liên tục** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **CI/CD/CT cho Hệ thống AI**, **Huấn luyện liên tục** tiếp nhận điểm tựa từ **Cổng cho Triển khai Mô hình** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trigger Huấn luyện lại và Trigger Triển khai lại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CI/CD/CT cho Hệ thống AI**, **Trigger Huấn luyện lại và Trigger Triển khai lại** tiếp nhận điểm tựa từ **Huấn luyện liên tục** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quay lui (rollback / 롤백)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trigger Huấn luyện lại và Trigger Triển khai lại

Có thể huấn luyện lại nhưng không triển khai nếu mô hình mới không tốt hơn. Ngược lại có thể triển khai lại cùng mô hình vì hạ tầng hoặc thời gian chạy (runtime / 런타임) được vá mà không cần huấn luyện lại.

Tách hai khái niệm này làm vòng đời rõ hơn.

> **Chuyển mạch:** Trong **CI/CD/CT cho Hệ thống AI**, **Quay lui (rollback / 롤백)** tiếp nhận điểm tựa từ **Trigger Huấn luyện lại và Trigger Triển khai lại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Triển khai Canary** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quay lui (rollback / 롤백)

Quay lui (rollback / 롤백) cần khôi phục bộ mô hình, tokenizer/preprocessor, prompt và cấu hình tương thích. Nếu cơ sở dữ liệu (database / 데이터베이스) hoặc chỉ mục (index / 인덱스) lược đồ (schema / 스키마) đã migrate theo cách không tương thích, chỉ quay lui (rollback / 롤백) mô hình có thể vẫn thất bại.

> **Chuyển mạch:** Ở chặng này của **CI/CD/CT cho Hệ thống AI**, **Triển khai Canary** tiếp nhận điểm tựa từ **Quay lui (rollback / 롤백)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Triển khai Shadow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Triển khai Canary

Chỉ chuyển một tỷ lệ traffic tới ứng viên rồi theo dõi chỉ số hệ thống và chỉ số chất lượng/kinh doanh.

Canary cần chú ý thiên lệch lựa chọn (selection bias): tập traffic phải đủ đại diện hoặc kết quả phải được diễn giải đúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CI/CD/CT cho Hệ thống AI**, **Triển khai Shadow** tiếp nhận điểm tựa từ **Triển khai Canary** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CI/CD cho LLM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Triển khai Shadow

Ứng viên nhận bản sao yêu cầu (request / 요청) nhưng đầu ra (output / 출력) không ảnh hưởng người dùng. Cách này hữu ích để đo độ trễ và hành vi trên traffic thật.

Shadow có thể gần như nhân đôi chi phí suy luận và vẫn phải tuân thủ kiểm soát quyền riêng tư.

> **Chuyển mạch:** Trong **CI/CD/CT cho Hệ thống AI**, **CI/CD cho LLM** tiếp nhận điểm tựa từ **Triển khai Shadow** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuỗi xử lý (pipeline / 파이프라인) như Mã nguồn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **CI/CD/CT cho Hệ thống AI**, **CI/CD cho LLM** nêu điều cần giải thích; **Chuỗi xử lý (pipeline / 파이프라인) như Mã nguồn** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Secret và Môi trường** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuỗi xử lý (pipeline / 파이프라인) như Mã nguồn

Chuỗi xử lý (pipeline / 파이프라인) huấn luyện và triển khai nên được phiên bản (version / 버전) hóa như mã nguồn để có thể rà soát (review / 검토) diff, tái lập và quay lui (rollback / 롤백).

Cấu hình chỉ tồn tại trong UI thủ công dễ tạo trạng thái ẩn khó truy vết.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CI/CD/CT cho Hệ thống AI**, **Chuỗi xử lý (pipeline / 파이프라인) như Mã nguồn** nêu điều cần giải thích; **Secret và Môi trường** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Secret và Môi trường

Log của huấn luyện (training / 학습) hoặc CI không được làm lộ API key, credential hoặc dữ liệu nhạy cảm. Quyền giữa dev, staging và môi trường vận hành (production / 운영 환경) nên được tách rõ.

> **Chuyển mạch:** Trong **CI/CD/CT cho Hệ thống AI**, **Mô hình tư duy** gom các mảnh từ **Secret và Môi trường** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
CI → chứng minh thay đổi nhất quán nội bộ
CT → tạo artifact đã học mới
CD → đưa artifact đã được phê duyệt qua các môi trường một cách an toàn
```

> **Chuyển mạch:** Ở chặng này của **CI/CD/CT cho Hệ thống AI**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Continuous huấn luyện (training / 학습) nghĩa là luôn huấn luyện mô hình mới nhất”

Không. Tần suất huấn luyện phải dựa trên dữ liệu, giá trị và chi phí, không phải chỉ vì có thể tự động hóa.

### “Vượt benchmark offline thì nên tự động triển khai”

Không. Phân phối môi trường vận hành (production / 운영 환경) và ràng buộc hệ thống có thể khác.

### “CI của LLM chỉ cần kiểm tra cú pháp prompt”

Không. Regression về hành vi, bảo mật và retrieval mới là phần khó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CI/CD/CT cho Hệ thống AI**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Model Registry](./03_model_registry.md), [Monitoring](./06_monitoring_and_observability.md), [Drift](./07_drift_and_retraining.md), [LLMOps](./08_llmops.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
