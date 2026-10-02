# Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Inference pipeline**. Route đi từ training/serving parity → request validation → preprocessing/model execution → postprocessing → observability and fallback, để đường đi của request giữ cùng semantics với lúc train.

**chuỗi xử lý (pipeline / 파이프라인) suy luận (inference pipeline / 추론 파이프라인)** biến một yêu cầu môi trường vận hành (production / 운영 환경) thành đầu vào (input / 입력) phù hợp với mô hình, thực thi mô hình, sau đó biến raw đầu ra (output / 출력) thành quyết định hoặc phản hồi có thể sử dụng. Độ đúng phụ thuộc toàn bộ đường đi, không chỉ forward pass.

```text
request
→ kiểm tra
→ lấy feature / context
→ tiền xử lý / tokenize
→ model inference
→ decode / hậu xử lý
→ policy / validation
→ response
```

## Tính nhất quán giữa huấn luyện (training / 학습) và Serving

Cùng một phép biến đổi về mặt ngữ nghĩa (semantics / 의미론) nên được dùng online giống như khi huấn luyện (training / 학습). Các dạng skew phổ biến gồm:

- normalization constant khác nhau;
- category ánh xạ (mapping / 매핑) không khớp;
- tokenizer phiên bản (version / 버전) khác;
- timezone hoặc cửa sổ (window / 윈도우) khác;
- quy tắc resize/crop ảnh khác.

Nên dùng chung thư viện (library / 라이브러리)/sản phẩm tạo ra (artifact / 산출물) hoặc sinh transform từ một specification duy nhất.

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Kiểm tra yêu cầu (request / 요청)** tiếp nhận điểm tựa từ **Tính nhất quán giữa huấn luyện (training / 학습) và Serving** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Truy xuất tính năng (feature / 기능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểm tra yêu cầu (request / 요청)

Trước khi đưa dữ liệu vào mô hình cần kiểm tra:

- lược đồ (schema / 스키마) và kiểu (type / 타입);
- trường dữ liệu (field / 필드) bắt buộc;
- giới hạn kích thước;
- enum hợp lệ;
- authentication;
- các ràng buộc nội dung.

Nên reject yêu cầu (request / 요청) sai càng sớm càng tốt thay vì để tensor/thời gian chạy (runtime / 런타임) phát sinh lỗi khó hiểu ở phía sau.

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Truy xuất tính năng (feature / 기능)** tiếp nhận điểm tựa từ **Kiểm tra yêu cầu (request / 요청)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tiền xử lý** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Truy xuất tính năng (feature / 기능)

Tính năng (feature / 기능) online cần đúng theo thời điểm, đủ mới và có độ trễ thấp. tính năng (feature / 기능) dịch vụ (service / 서비스) có thể lấy dữ liệu từ bộ nhớ đệm (cache / 캐시), KV store hoặc cơ sở dữ liệu (database / 데이터베이스).

Khi hết thời gian chờ (timeout / 타임아웃), hệ thống phải định nghĩa rõ sẽ:

- thất bại (fail / 실패);
- dùng giá trị mặc định;
- dùng stale bộ nhớ đệm (cache / 캐시);
- tuyến (route / 경로) sang fallback mô hình (model / 모델).

Giá trị mặc định có thể làm chất lượng giảm âm thầm, vì vậy cần log rõ khi fallback xảy ra.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Tiền xử lý** tiếp nhận điểm tựa từ **Truy xuất tính năng (feature / 기능)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Động (dynamic / 동적) Shape** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tiền xử lý

Các tác vụ thường gồm:

```text
chuẩn hóa giá trị số
mã hóa category
tokenize text
resize / normalize image
resample audio
tạo tensor đầu vào cho model
```

Với mô hình nhẹ, preprocessing độ trễ (latency / 지연 시간) đôi khi còn lớn hơn thời gian chạy mô hình (model / 모델).

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Động (dynamic / 동적) Shape** tiếp nhận điểm tựa từ **Tiền xử lý** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Suy luận sinh nội dung** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Động (dynamic / 동적) Shape

Chuỗi (sequence / 시퀀스) hoặc ảnh (image / 이미지) có kích thước khác nhau làm batching và bộ nhớ (memory / 메모리) khó tối ưu. Padding tất cả về item lớn nhất gây lãng phí compute.

Có thể nhóm yêu cầu (request / 요청) theo length/shape để tăng hiệu quả.

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Suy luận sinh nội dung** tiếp nhận điểm tựa từ **Động (dynamic / 동적) Shape** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Decoding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Suy luận sinh nội dung

LLM suy luận (inference / 추론) thường có hai giai đoạn:

1. **prefill**: xử lý đầu vào (input / 입력)/ngữ cảnh (context / 맥락) và tạo KV bộ nhớ đệm (cache / 캐시);
2. **decode**: sinh đơn vị từ (token / 토큰) theo kiểu autoregressive, từng bước một.

Prompt dài làm prefill đắt hơn; đầu ra (output / 출력) dài làm decode đắt hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Decoding** tiếp nhận điểm tựa từ **Suy luận sinh nội dung** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Structured đầu ra (output / 출력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Decoding

Các tham số thường gặp:

- greedy;
- temperature;
- top-k;
- top-p;
- beam tìm kiếm (search / 검색);
- stop chuỗi (sequence / 시퀀스);
- max đơn vị từ (token / 토큰).

Chúng là một phần của hành vi sản phẩm, vì vậy cần được phiên bản (version / 버전) hóa và theo dõi.

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Structured đầu ra (output / 출력)** tiếp nhận điểm tựa từ **Decoding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hậu xử lý** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Structured đầu ra (output / 출력)

Nếu downstream cần JSON hoặc hàm (function / 함수) lời gọi (call / 호출), đầu ra (output / 출력) phải được kiểm theo lược đồ (schema / 스키마). Constrained decoding có thể giảm lỗi cú pháp nhưng không thay thế ngữ nghĩa (semantic / 의미적) kiểm tra hợp lệ (validation / 검증).

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Hậu xử lý** tiếp nhận điểm tựa từ **Structured đầu ra (output / 출력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngân sách hết thời gian chờ (timeout / 타임아웃)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hậu xử lý

Ví dụ:

- classification threshold;
- NMS cho đối tượng (object / 객체) detection;
- detokenization;
- confidence calibration;
- nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙);
- redaction;
- đơn vị (unit / 단위) conversion.

Hậu xử lý là một phần của hợp đồng giữa mô hình và hệ thống, không phải bước trang trí.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Ngân sách hết thời gian chờ (timeout / 타임아웃)** tiếp nhận điểm tựa từ **Hậu xử lý** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thử lại (retry / 재시도)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngân sách hết thời gian chờ (timeout / 타임아웃)

Có thể chia deadline end-to-end như:

```text
feature 30 ms
model 100 ms
postprocess 10 ms
network margin 20 ms
```

Nếu mô hình (model / 모델) dùng hết toàn bộ deadline, downstream không còn khoảng trống để phục hồi hoặc fallback.

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Thử lại (retry / 재시도)** tiếp nhận điểm tựa từ **Ngân sách hết thời gian chờ (timeout / 타임아웃)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Admission điều khiển (control / 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thử lại (retry / 재시도)

Thử lại (retry / 재시도) suy luận (inference / 추론) thường an toàn khi chỉ đọc, nhưng yêu cầu (request / 요청) lặp lại vẫn tiêu tốn sức chứa (capacity / 용량) và có thể khuếch đại outage. Chỉ nên thử lại (retry / 재시도) lỗi transient, kèm deadline và backoff.

Với tác nhân (agent / 에이전트) hoặc công cụ (tool / 도구) có side tác động (effect / 효과), thử lại (retry / 재시도) cần idempotency.

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Admission điều khiển (control / 제어)** tiếp nhận điểm tựa từ **Thử lại (retry / 재시도)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Streaming đầu ra (output / 출력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Admission điều khiển (control / 제어)

Khi hệ thống quá tải, nên từ chối hoặc trì hoãn yêu cầu (request / 요청) ưu tiên thấp thay vì cho hàng đợi (queue / 큐) dài vô hạn. Tail độ trễ (latency / 지연 시간) thường quan trọng hơn average độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Streaming đầu ra (output / 출력)** tiếp nhận điểm tựa từ **Admission điều khiển (control / 제어)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cancellation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Streaming đầu ra (output / 출력)

LLM hoặc TTS có thể stream đầu ra (output / 출력) từng phần. Streaming cải thiện cảm nhận **time-to-first-output**, nhưng làm moderation và quay lui (rollback / 롤백) khó hơn vì người dùng đã thấy đơn vị từ (token / 토큰) trước khi toàn bộ phản hồi được validate.

Guardrail cần được thiết kế phù hợp với đặc điểm này.

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Cancellation** tiếp nhận điểm tựa từ **Streaming đầu ra (output / 출력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuỗi xử lý (pipeline / 파이프라인) nhiều mô hình** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cancellation

Nếu người dùng ngắt kết nối, nên dừng generation để giải phóng GPU nếu thời gian chạy (runtime / 런타임) hỗ trợ. Nếu không, hệ thống vẫn tiếp tục sinh đơn vị từ (token / 토큰) không ai sử dụng.

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Cancellation** xác định đầu vào; **Chuỗi xử lý (pipeline / 파이프라인) nhiều mô hình** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Cascade** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuỗi xử lý (pipeline / 파이프라인) nhiều mô hình

Ví dụ RAG:

```text
embed query
→ retrieve
→ rerank
→ generate
→ cite / validate
```

Độ trễ (latency / 지연 시간) end-to-end là tổng hoặc kết quả kết hợp của nhiều stage. Cần tối ưu toàn bộ đồ thị (graph / 그래프) thay vì chỉ một mô hình.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Chuỗi xử lý (pipeline / 파이프라인) nhiều mô hình** xác định đầu vào; **Cascade** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Batching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cascade

Có thể dùng mô hình rẻ trước, chỉ gọi mô hình đắt cho trường hợp (case / 사례) khó:

```text
small classifier
→ nếu confidence cao: kết thúc
→ nếu không: route sang large model
```

Cascade có thể giảm chi phí (cost / 비용) trung bình nếu routing đủ đáng tin.

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Batching** tiếp nhận điểm tựa từ **Cascade** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **KV bộ nhớ đệm (cache / 캐시)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Batching

Scheduler online có thể gom nhiều yêu cầu (request / 요청) thành batch GPU để tăng thông lượng (throughput / 처리량). Nhưng chờ đủ batch lại làm độ trễ (latency / 지연 시간) tăng. động (dynamic / 동적) hoặc continuous batching giúp cân bằng hai mục tiêu này.

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **KV bộ nhớ đệm (cache / 캐시)** tiếp nhận điểm tựa từ **Batching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Prefix Caching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## KV bộ nhớ đệm (cache / 캐시)

Autoregressive Transformer lưu key/giá trị (value / 값) tensor của đơn vị từ (token / 토큰) trước đó để không phải tính lại toàn bộ lịch sử (history / 이력) ở mỗi đơn vị từ (token / 토큰) đầu ra (output / 출력).

Bộ nhớ (memory / 메모리) xấp xỉ tăng theo:

```text
batch × sequence length × layers × hidden/head dimensions
```

Trong LLM serving, KV bộ nhớ đệm (cache / 캐시) thường giới hạn tính đồng thời (concurrency / 동시성) mạnh hơn bản thân weights.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Prefix Caching** tiếp nhận điểm tựa từ **KV bộ nhớ đệm (cache / 캐시)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiểm tra đầu ra (output / 출력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Prefix Caching

Nếu nhiều yêu cầu (request / 요청) dùng chung hệ thống (system / 시스템) prefix hoặc document dài giống nhau, có thể bộ nhớ đệm (cache / 캐시) kết quả prefill/KV để giảm compute, với điều kiện prefix và mô hình (model / 모델) cấu hình (config / 설정) phải khớp chính xác và dữ liệu được cô lập đúng theo privacy phạm vi (scope / 범위).

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Kiểm tra đầu ra (output / 출력)** tiếp nhận điểm tựa từ **Prefix Caching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Logging** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểm tra đầu ra (output / 출력)

Với ứng dụng rủi ro cao:

```text
model output
→ deterministic rule
→ external verification
→ human review khi cần
```

Không nên cho generative đầu ra (output / 출력) trực tiếp thay đổi trọng yếu (critical / 중요) hệ thống (system / 시스템) mà không qua kiểm tra hợp lệ (validation / 검증).

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Logging** tiếp nhận điểm tựa từ **Kiểm tra đầu ra (output / 출력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Logging

Nên ghi lại một cách an toàn:

- mô hình (model / 모델)/cấu hình (config / 설정) phiên bản (version / 버전);
- độ trễ (latency / 지연 시간) theo từng thành phần;
- đầu vào (input / 입력) shape hoặc đơn vị từ (token / 토큰) count;
- đầu ra (output / 출력) length;
- lỗi (error / 오류) và fallback;
- chất lượng (quality / 품질) phản hồi (feedback / 피드백).

Không nên log raw secret hoặc PII theo mặc định.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Mô hình tư duy** gom các mảnh từ **Logging** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> **suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인) là một đồ thị (graph / 그래프) biến đổi có deadline độ trễ (latency / 지연 시간), trong đó ngữ nghĩa (semantics / 의미론) phải khớp với huấn luyện (training / 학습) và mọi dạng thất bại (failure mode / 실패 모드) quan trọng phải được định nghĩa rõ.**

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “suy luận (inference / 추론) độ trễ (latency / 지연 시간) chính là thời gian forward của mô hình (model / 모델)”

Không. tính năng (feature / 기능) fetch, tokenization, hàng đợi (queue / 큐), mạng (network / 네트워크) và postprocess đều đóng góp độ trễ (latency / 지연 시간).

### “Streaming làm mô hình (model / 모델) chạy nhanh hơn”

Không nhất thiết. Streaming chủ yếu làm người dùng thấy đầu ra (output / 출력) sớm hơn; tổng compute có thể không đổi.

### “thử lại (retry / 재시도) luôn làm độ tin cậy (reliability / 신뢰성) tốt hơn”

Không. Khi hệ thống quá tải, thử lại (retry / 재시도) storm có thể khiến outage nặng hơn.

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인)**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Suy luận (inference / 추론) chuỗi xử lý (pipeline / 파이프라인) dẫn trực tiếp tới kiến trúc serving và sự đánh đổi (trade-off / 트레이드오프) giữa batch với online suy luận (inference / 추론).

Xem tiếp: [Model Serving](./03_model_serving.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
