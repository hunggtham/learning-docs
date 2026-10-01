# AI kỹ thuật (engineering / 엔지니어링)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **AI kỹ thuật (engineering / 엔지니어링)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Mô hình không đồng nghĩa sản phẩm** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Huấn luyện Offline và phục vụ Online** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Kỹ thuật AI (AI Engineering / AI 엔지니어링)** là lĩnh vực biến mô hình (model / 모델), dữ liệu và các thành phần AI thành một hệ thống có thể vận hành ổn định, nhanh, có chi phí kiểm soát được, quan sát được (observable) và bảo trì được trong môi trường vận hành (production / 운영 환경). Chất lượng mô hình chỉ là một thành phần; trải nghiệm người dùng và độ tin cậy của hệ thống còn phụ thuộc toàn bộ chuỗi xử lý (pipeline / 파이프라인) xung quanh.

```text
Dữ liệu / yêu cầu
→ tiền xử lý / truy xuất
→ suy luận của mô hình
→ hậu xử lý / chính sách
→ phản hồi / hành động
→ ghi log / phản hồi học tập
```

## Mô hình không đồng nghĩa sản phẩm

Một mô hình có điểm benchmark cao vẫn có thể tạo ra sản phẩm kém nếu:

- độ trễ (latency / 지연 시간) quá cao;
- ngữ cảnh hoặc truy xuất sai;
- hết thời gian chờ (timeout / 타임아웃) xảy ra thường xuyên;
- chi phí trên mỗi yêu cầu không bền vững;
- lược đồ (schema / 스키마) đầu ra không ổn định;
- triển khai (deployment / 배포) thiếu cơ chế dự phòng (fallback);
- vi phạm quyền riêng tư hoặc bảo mật.

Kỹ thuật AI tối ưu **toàn bộ hệ thống end-to-end**, không chỉ chỉ số (metric / 지표) của mô hình.

> **Chuyển mạch:** Trong **AI kỹ thuật (engineering / 엔지니어링)**, **Huấn luyện Offline và phục vụ Online** tiếp nhận điểm tựa từ **Mô hình không đồng nghĩa sản phẩm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Các thành phần của hệ thống AI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Huấn luyện Offline và phục vụ Online

Huấn luyện (training / 학습) thường tối ưu thông lượng (throughput / 처리량) trên batch lớn và có thể chạy nhiều giờ hoặc nhiều ngày. Phục vụ suy luận (serving) thường cần độ trễ thấp, traffic biến động và yêu cầu availability nghiêm ngặt.

Cùng một mô hình nhưng các ràng buộc thời gian chạy (runtime / 런타임) có thể hoàn toàn khác nhau.

> **Chuyển mạch:** Ở chặng này của **AI kỹ thuật (engineering / 엔지니어링)**, **Các thành phần của hệ thống AI** tiếp nhận điểm tựa từ **Huấn luyện Offline và phục vụ Online** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Contract-First suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các thành phần của hệ thống AI

Một kiến trúc điển hình:

```text
API Gateway
→ kiểm tra yêu cầu
→ đặc trưng / ngữ cảnh / truy xuất
→ bộ định tuyến mô hình (model router)
→ dịch vụ suy luận
→ kiểm tra đầu ra / guardrail
→ cache / lưu trữ
→ quan sát hệ thống (observability)
```

Hệ thống tác nhân (agent / 에이전트) hoặc RAG còn bổ sung công cụ (tool / 도구), kho trạng thái (state store), tìm kiếm véc-tơ (vector / 벡터) và orchestration.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **AI kỹ thuật (engineering / 엔지니어링)**, **Contract-First suy luận (inference / 추론)** tiếp nhận điểm tựa từ **Các thành phần của hệ thống AI** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lớp xác định và lớp xác suất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Contract-First suy luận (inference / 추론)

Mô hình môi trường vận hành (production / 운영 환경) nên có hợp đồng đầu vào (input / 입력)/đầu ra (output / 출력) rõ ràng:

```json
{
  "model_version": "fraud-v12",
  "input": {"transaction_id":"...", "features": {...}},
  "output": {"score":0.87, "decision":"review"}
}
```

Kiểm tra lược đồ (schema / 스키마) giúp tránh trường hợp hệ thống âm thầm chấp nhận dữ liệu sai định dạng.

> **Chuyển mạch:** Trong **AI kỹ thuật (engineering / 엔지니어링)**, **Lớp xác định và lớp xác suất** tiếp nhận điểm tựa từ **Contract-First suy luận (inference / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **AI đồng bộ và bất đồng bộ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lớp xác định và lớp xác suất

Một kiến trúc đáng tin cậy thường có dạng:

```text
Kiểm tra có tính xác định
→ mô hình xác suất
→ chính sách / ràng buộc có tính xác định
```

Ví dụ mô hình trả về xác suất gian lận; nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) quyết định threshold và luồng approval.

> **Chuyển mạch:** Ở chặng này của **AI kỹ thuật (engineering / 엔지니어링)**, **AI đồng bộ và bất đồng bộ** tiếp nhận điểm tựa từ **Lớp xác định và lớp xác suất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Định tuyến mô hình** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## AI đồng bộ và bất đồng bộ

Chat hoặc tìm kiếm (search / 검색) tương tác thường cần phản hồi đồng bộ (synchronous). Phân tích tài liệu lớn, xử lý video hoặc tạo embedding theo lô thường phù hợp với job bất đồng bộ (asynchronous).

Không nên ép tác vụ dài chạy trọn trong một HTTP yêu cầu (request / 요청) duy nhất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **AI kỹ thuật (engineering / 엔지니어링)**, **Định tuyến mô hình** tiếp nhận điểm tựa từ **AI đồng bộ và bất đồng bộ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cơ chế dự phòng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Định tuyến mô hình

Các loại tác vụ (task / 작업) khác nhau có thể dùng các mô hình khác nhau:

```text
mô hình nhỏ, rẻ → classification / extraction
mô hình lớn → reasoning khó
embedding model → retrieval
vision model → image
```

Bộ định tuyến (router) có thể dựa trên loại tác vụ (task / 작업), confidence, độ trễ (latency / 지연 시간) ngân sách (budget / 예산) hoặc chi phí (cost / 비용) ngân sách (budget / 예산).

> **Chuyển mạch:** Trong **AI kỹ thuật (engineering / 엔지니어링)**, **Định tuyến mô hình** xác định đầu vào; **Cơ chế dự phòng** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Độ tin cậy và khả năng từ chối trả lời** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cơ chế dự phòng

Hệ thống AI môi trường vận hành (production / 운영 환경) nên định nghĩa rõ đường đi khi lỗi xảy ra:

- mô hình hoặc provider thứ hai;
- fallback dựa trên quy tắc (rule / 규칙);
- kết quả đã bộ nhớ đệm (cache / 캐시);
- human rà soát (review / 검토);
- phản hồi giảm cấp có kiểm soát (graceful degradation).

Fallback không nên âm thầm thay đổi ngữ nghĩa (semantics / 의미론) của tác vụ.

> **Chuyển mạch:** Ở chặng này của **AI kỹ thuật (engineering / 엔지니어링)**, **Cơ chế dự phòng** xác định đầu vào; **Độ tin cậy và khả năng từ chối trả lời** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mặt phẳng dữ liệu (data plane / 데이터 플레인) và điều khiển (control / 제어) Plane** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ tin cậy và khả năng từ chối trả lời

Với classification, hệ thống có thể từ chối quyết định khi bất định (uncertainty / 불확실성) cao. Với Generative AI, confidence khó đo hơn; nên dựa vào bằng chứng được grounding, validator và kiểm tra đặc thù theo tác vụ (task / 작업) thay vì chỉ dùng xác suất đơn vị từ (token / 토큰) thô.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **AI kỹ thuật (engineering / 엔지니어링)**, **Độ tin cậy và khả năng từ chối trả lời** nêu điều cần giải thích; **Mặt phẳng dữ liệu (data plane / 데이터 플레인) và điều khiển (control / 제어) Plane** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình (model / 모델) sản phẩm tạo ra (artifact / 산출물)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mặt phẳng dữ liệu (data plane / 데이터 플레인) và điều khiển (control / 제어) Plane

**mặt phẳng dữ liệu (data plane / 데이터 플레인)** xử lý yêu cầu (request / 요청) và suy luận (inference / 추론) của người dùng.

**Mặt phẳng điều khiển (control plane)** quản lý mô hình (model / 모델) phiên bản (version / 버전), rollout, cấu hình (configuration / 구성), routing, chính sách (policy / 정책) và monitoring.

Tách hai lớp này giúp triển khai (deployment / 배포) và quay lui (rollback / 롤백) an toàn hơn.

> **Chuyển mạch:** Trong **AI kỹ thuật (engineering / 엔지니어링)**, **Mặt phẳng dữ liệu (data plane / 데이터 플레인) và điều khiển (control / 제어) Plane** nêu điều cần giải thích; **Mô hình (model / 모델) sản phẩm tạo ra (artifact / 산출물)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Bản dựng (build / 빌드) có khả năng tái lập** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình (model / 모델) sản phẩm tạo ra (artifact / 산출물)

Sản phẩm tạo ra (artifact / 산출물) dùng để triển khai không chỉ gồm weights:

```text
weights
architecture / config
tokenizer / preprocessor
feature schema
label mapping
runtime dependencies
quantization config
model card / version metadata
```

Sai tokenizer có thể phá hỏng toàn bộ triển khai (deployment / 배포) LLM dù weights hoàn toàn đúng.

> **Chuyển mạch:** Ở chặng này của **AI kỹ thuật (engineering / 엔지니어링)**, **Bản dựng (build / 빌드) có khả năng tái lập** tiếp nhận điểm tựa từ **Mô hình (model / 모델) sản phẩm tạo ra (artifact / 산출물)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **API và Backpressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bản dựng (build / 빌드) có khả năng tái lập

Phiên bản (version / 버전) của bộ chứa (container / 컨테이너) và môi trường nên được cố định đủ chặt để thời gian chạy (runtime / 런타임) có thể tái lập. Khả năng tương thích giữa GPU driver và thư viện (library / 라이브러리) cũng là một phần của tính tương thích (compatibility / 호환성) của sản phẩm tạo ra (artifact / 산출물).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **AI kỹ thuật (engineering / 엔지니어링)**, **API và Backpressure** tiếp nhận điểm tựa từ **Bản dựng (build / 빌드) có khả năng tái lập** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SLO** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## API và Backpressure

Suy luận (inference / 추론) API cần có:

- giới hạn kích thước yêu cầu (request / 요청);
- hết thời gian chờ (timeout / 타임아웃);
- giới hạn hàng đợi (queue / 큐);
- tỷ lệ (rate / 비율) limiting;
- cancellation;
- backpressure.

Hàng đợi (queue / 큐) không giới hạn chỉ che giấu tình trạng quá tải cho đến khi độ trễ (latency / 지연 시간) tăng đột biến.

> **Chuyển mạch:** Trong **AI kỹ thuật (engineering / 엔지니어링)**, **SLO** tiếp nhận điểm tựa từ **API và Backpressure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chất lượng AI phụ thuộc ngữ cảnh hệ thống** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SLO

Cần định nghĩa **mục tiêu mức dịch vụ (Service-Level Objective — SLO)** như:

```text
availability
p50 / p95 / p99 latency
error rate
quality metric
cost per request
freshness
```

Chất lượng (quality / 품질) SLO thường khó đo hơn độ trễ (latency / 지연 시간) SLO vì label có thể đến trễ.

> **Chuyển mạch:** Ở chặng này của **AI kỹ thuật (engineering / 엔지니어링)**, **Chất lượng AI phụ thuộc ngữ cảnh hệ thống** tiếp nhận điểm tựa từ **SLO** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính nhất quán giữa Offline và Online** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chất lượng AI phụ thuộc ngữ cảnh hệ thống

Độ đúng end-to-end phụ thuộc vào nhiều thành phần:

\[
P(system\ success)=f(data,retrieval,model,policy,tools,environment)
\]

Cải thiện mô hình 2% có thể ít giá trị hơn việc sửa lỗi retrieval recall hoặc lỗi lược đồ (schema / 스키마).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **AI kỹ thuật (engineering / 엔지니어링)**, **Tính nhất quán giữa Offline và Online** tiếp nhận điểm tựa từ **Chất lượng AI phụ thuộc ngữ cảnh hệ thống** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Shadow triển khai (deployment / 배포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính nhất quán giữa Offline và Online

Lô-gic (logic / 논리) tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링), tokenization và preprocessing nên được chia sẻ hoặc phiên bản (version / 버전) hóa giữa huấn luyện (training / 학습) và serving. **Training-serving skew** có thể tạo lỗi âm thầm rất khó phát hiện.

> **Chuyển mạch:** Trong **AI kỹ thuật (engineering / 엔지니어링)**, **Shadow triển khai (deployment / 배포)** tiếp nhận điểm tựa từ **Tính nhất quán giữa Offline và Online** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Canary bản phát hành (release / 릴리스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Shadow triển khai (deployment / 배포)

Mô hình mới nhận bản sao của môi trường vận hành (production / 운영 환경) traffic nhưng đầu ra (output / 출력) chưa được dùng để ra quyết định. Nhờ đó có thể so sánh chất lượng và độ trễ (latency / 지연 시간) trước khi chuyển traffic thật.

> **Chuyển mạch:** Ở chặng này của **AI kỹ thuật (engineering / 엔지니어링)**, **Canary bản phát hành (release / 릴리스)** tiếp nhận điểm tựa từ **Shadow triển khai (deployment / 배포)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **A/B Testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Canary bản phát hành (release / 릴리스)

Chỉ tuyến (route / 경로) một tỷ lệ traffic nhỏ sang mô hình mới, theo dõi các chỉ số rồi tăng dần nếu ổn định. Cần định nghĩa trigger quay lui (rollback / 롤백) rõ ràng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **AI kỹ thuật (engineering / 엔지니어링)**, **A/B Testing** tiếp nhận điểm tựa từ **Canary bản phát hành (release / 릴리스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Versioning cho mô hình và cấu hình** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## A/B Testing

A/B testing nên đo cả kết quả (outcome / 결과) của người dùng hoặc nghiệp vụ (business / 비즈니스), không chỉ offline chỉ số (metric / 지표). Guardrail cần bao gồm độ trễ (latency / 지연 시간), an toàn (safety / 안전) và chi phí (cost / 비용).

> **Chuyển mạch:** Trong **AI kỹ thuật (engineering / 엔지니어링)**, **Versioning cho mô hình và cấu hình** tiếp nhận điểm tựa từ **A/B Testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khả năng quan sát (observability / 관측 가능성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Versioning cho mô hình và cấu hình

Mọi prediction và log nên truy vết được tới mô hình (model / 모델)/cấu hình (config / 설정) phiên bản (version / 버전) chính xác. Với ứng dụng LLM, nên ghi thêm phiên bản (version / 버전) của prompt/template, retrieval cấu hình (config / 설정) và công cụ (tool / 도구) khi cần.

> **Chuyển mạch:** Ở chặng này của **AI kỹ thuật (engineering / 엔지니어링)**, **Khả năng quan sát (observability / 관측 가능성)** tiếp nhận điểm tựa từ **Versioning cho mô hình và cấu hình** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dạng thất bại (failure mode / 실패 모드) đặc thù của AI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khả năng quan sát (observability / 관측 가능성)

Cần dấu vết (trace / 추적) một yêu cầu (request / 요청) xuyên suốt các thành phần:

```text
request
→ latency của feature / retrieval
→ latency của model
→ token usage
→ tool call
→ output validation
```

Chỉ số (metric / 지표) không đi cùng dấu vết (trace / 추적) khiến việc tìm nguyên nhân gốc (root cause / 근본 원인) trở nên khó khăn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **AI kỹ thuật (engineering / 엔지니어링)**, **Dạng thất bại (failure mode / 실패 모드) đặc thù của AI** tiếp nhận điểm tựa từ **Khả năng quan sát (observability / 관측 가능성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chi phí là một ràng buộc kiến trúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dạng thất bại (failure mode / 실패 모드) đặc thù của AI

Phần này kiểm tra ranh giới và failure mode của cơ chế vừa học. Hãy dùng nó để biết khi nào mô hình còn đúng, khi nào cần đổi chiến lược và bằng chứng nào phải thu thập.

- distribution shift;
- model unavailable;
- tokenizer mismatch;
- GPU OOM;
- ngữ cảnh (context / 맥락) overflow;
- structured đầu ra (output / 출력) bị hallucination;
- embedding hoặc chỉ mục (index / 인덱스) cũ;
- công cụ (tool / 도구) lời gọi (call / 호출) không hợp lệ;
- batch hàng đợi (queue / 큐) bị bão hòa.

> **Chuyển mạch:** Trong **AI kỹ thuật (engineering / 엔지니어링)**, **Chi phí là một ràng buộc kiến trúc** tiếp nhận điểm tựa từ **Dạng thất bại (failure mode / 실패 모드) đặc thù của AI** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Human-in-the-Loop** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí là một ràng buộc kiến trúc

Tổng chi phí gồm:

```text
compute inference
retrieval / storage
network
model API token
human review
training / retraining
idle capacity
```

Mô hình rẻ nhất trên mỗi đơn vị từ (token / 토큰) chưa chắc tạo ra tác vụ (task / 작업) hoàn thành rẻ nhất nếu tỷ lệ thử lại (retry / 재시도) hoặc thất bại (failure / 실패) cao.

> **Chuyển mạch:** Ở chặng này của **AI kỹ thuật (engineering / 엔지니어링)**, **Human-in-the-Loop** tiếp nhận điểm tựa từ **Chi phí là một ràng buộc kiến trúc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bản dựng (build / 빌드) hay Buy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Human-in-the-Loop

Human rà soát (review / 검토) nên được thiết kế thành workflow có hàng đợi (queue / 큐), ngữ cảnh (context / 맥락) và escalation rõ ràng, không phải biện pháp chữa cháy thủ công. Nếu quản trị (governance / 거버넌스) cho phép, các nhãn rà soát (review / 검토) có thể trở thành dữ liệu cải thiện hệ thống về sau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **AI kỹ thuật (engineering / 엔지니어링)**, **Bản dựng (build / 빌드) hay Buy** tiếp nhận điểm tựa từ **Human-in-the-Loop** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bản dựng (build / 빌드) hay Buy

Dùng bên ngoài (external / 외부) mô hình (model / 모델) API giúp triển khai nhanh và giảm gánh nặng hạ tầng; self-hosting cho nhiều quyền kiểm soát hơn và có thể rẻ hơn ở quy mô lớn, nhưng tăng chi phí vận hành.

Quyết định phụ thuộc vào:

- volume;
- privacy;
- độ trễ (latency / 지연 시간);
- mô hình (model / 모델) customization;
- năng lực phần cứng;
- rủi ro phụ thuộc provider.

> **Chuyển mạch:** Trong **AI kỹ thuật (engineering / 엔지니어링)**, **Mô hình tư duy** gom các mảnh từ **Bản dựng (build / 빌드) hay Buy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> **Kỹ thuật AI là Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) trong một hệ thống có thành phần xác suất và hành vi phụ thuộc dữ liệu.**

Mô hình không phải toàn bộ hệ thống; hệ thống phải giới hạn, vận hành và quan sát mô hình.

> **Chuyển mạch:** Ở chặng này của **AI kỹ thuật (engineering / 엔지니어링)**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “môi trường vận hành (production / 운영 환경) AI chỉ là deploy một mô hình (model / 모델) endpoint”

Không. Hệ thống thực tế còn cần dữ liệu, routing, kiểm tra hợp lệ (validation / 검증), khả năng quan sát (observability / 관측 가능성) và vòng đời (lifecycle / 생명주기) management.

### “Mô hình benchmark cao nhất luôn là lựa chọn môi trường vận hành (production / 운영 환경) tốt nhất”

Không. độ trễ (latency / 지연 시간), chi phí (cost / 비용) và độ tin cậy (reliability / 신뢰성) có thể quan trọng hơn.

### “suy luận (inference / 추론) chạy được trên máy cục bộ (local / 로컬) nghĩa là serving đã giải quyết xong”

Không. tính đồng thời (concurrency / 동시성), bộ nhớ (memory / 메모리), queueing và các lỗi vận hành chỉ bộc lộ rõ khi có tải thật.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **AI kỹ thuật (engineering / 엔지니어링)**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Kỹ thuật AI kết nối [Kiến trúc hệ thống AI](../00_foundations/04_ai_system_architecture.md), dữ liệu (data / 데이터), tác nhân (agent / 에이전트)/RAG và Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학).

Xem tiếp: [Training Pipeline](./01_training_pipeline.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
