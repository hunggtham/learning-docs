# AI Testing và Behavioral Evaluation

> **Mạch đọc:** Đặt **AI Testing và Behavioral Evaluation** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Pyramid mở rộng cho AI** sang **đơn vị (unit / 단위) Tests vẫn cần**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Traditional software testing kiểm tra deterministic contracts tương đối rõ. AI hệ thống (system / 시스템) lại có stochastic đầu ra (output / 출력), fuzzy tính đúng đắn (correctness / 정확성), learned hành vi (behavior / 동작) và distribution-dependent thất bại (failure / 실패). Vì vậy **AI testing** cần kết hợp đơn vị (unit / 단위)/tích hợp (integration / 통합) tests truyền thống với behavioral evaluation trên representative tasks.

## Pyramid mở rộng cho AI

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
unit tests
→ data/schema tests
→ component model tests
→ integration tests
→ behavioral evals
→ end-to-end scenario tests
→ online monitoring
```

Không tầng (layer / 계층) nào thay thế hoàn toàn tầng (layer / 계층) khác.

## Đơn vị (unit / 단위) Tests vẫn cần

Kiểm thử (test / 테스트) deterministic mã (code / 코드):

- preprocessing;
- tính năng (feature / 기능) calculations;
- parser;
- công cụ (tool / 도구) schemas;
- authorization;
- postprocessing;
- bộ nhớ đệm (cache / 캐시) keys;
- dữ liệu (data / 데이터) transforms.

Đừng dùng LLM judge để kiểm thử (test / 테스트) thứ có thể assert bằng mã (code / 코드).

## Dữ liệu (data / 데이터) Tests

Kiểm tra:

```text
schema
range
nulls
freshness
duplicates
point-in-time semantics
label consistency
```

Mô hình (model / 모델) tests vô nghĩa nếu đầu vào (input / 입력) chuỗi xử lý (pipeline / 파이프라인) sai.

## Behavioral Tests

Behavioral kiểm thử (test / 테스트) định nghĩa đầu vào (input / 입력) category + expected thuộc tính (property / 속성).

Ví dụ customer-support LLM:

```text
refund policy question → cite official policy
password request → do not reveal credentials
ambiguous request → ask clarification
unsupported claim → abstain / qualify
```

Expected hành vi (behavior / 동작) có thể là thuộc tính (property / 속성), không chính xác (exact / 정확한) string.

## Invariance Tests

Meaning-preserving transformation không nên đổi answer quá nhiều:

- paraphrase;
- harmless formatting;
- trường hợp (case / 사례) variation;
- irrelevant siêu dữ liệu (metadata / 메타데이터).

Nếu đầu ra (output / 출력) thay mạnh, expose brittleness.

## Directional Expectation Tests

Một tính năng (feature / 기능) tăng nên prediction move expected direction trong domain-specific trường hợp (case / 사례).

Không áp dụng nếu relationship not monotonic.

## Minimum Functionality Tests

Simple obvious cases mô hình (model / 모델) should pass. Nếu thất bại (fail / 실패) MFT, sophisticated benchmark score ít meaningful.

## Metamorphic Testing

Khi không có chính xác (exact / 정확한) oracle, define quan hệ (relation / 관계) giữa outputs under đầu vào (input / 입력) transformations.

Examples:

```text
shuffle irrelevant list order → same classification
add unrelated context → answer unchanged
translate round-trip → core meaning preserved
```

## Property-Based Testing

Generate many inputs satisfying các ràng buộc (constraints / 제약조건들) và kiểm thử (test / 테스트) invariants.

Useful for structured công cụ (tool / 도구) arguments, parsers and numeric các mô hình (models / 모델들).

## Golden kiểm thử (test / 테스트) Cases

Curated regression cases từ môi trường vận hành (production / 운영 환경) incidents nên trở thành permanent tests.

Each trường hợp (case / 사례) nên include:

- reason for inclusion;
- expected thuộc tính (property / 속성);
- severity;
- đơn vị sở hữu (owner / 오너)/lĩnh vực (domain / 도메인).

## Fuzzing

Generate malformed, extreme hoặc unexpected inputs để find crashes/lược đồ (schema / 스키마) errors/tài nguyên (resource / 자원) issues.

AI endpoints also need input-size/tài nguyên (resource / 자원) fuzzing to kiểm thử (test / 테스트) denial-of-service resistance.

## Stochastic Outputs

Generative mô hình (model / 모델) có variance. Tests có thể:

- fix temperature/seed when possible;
- run multiple samples;
- assert success tỷ lệ (rate / 비율) threshold;
- use deterministic validators.

Avoid flaky exact-string assertions.

## LLM Evaluation Oracle

Possible oracles:

```text
reference answer
executable test
schema validator
citation checker
retrieval evidence
human rubric
model-based judge
```

Prefer stronger deterministic/executable oracle when available.

## Mã (code / 코드) Generation Testing

Best evaluation often execute generated mã (code / 코드) against tests rather than judge văn bản (text / 텍스트) similarity.

Bảo mật (security / 보안) sandboxing required for untrusted mã (code / 코드).

## Công cụ (tool / 도구)/tác nhân (agent / 에이전트) Testing

Kiểm thử (test / 테스트) trajectory các ràng buộc (constraints / 제약조건들):

- allowed tools only;
- no duplicate side effects;
- correct thứ tự (order / 순서);
- stop điều kiện (condition / 조건);
- thử lại (retry / 재시도) bounds;
- trạng thái (state / 상태) persistence;
- quay lui (rollback / 롤백)/compensation.

Final answer alone may hide unsafe trajectory.

## RAG Testing

Separate tests:

```text
ingestion/parser
retrieval recall
reranking
context assembly
answer groundedness
citation correctness
```

End-to-end thất bại (failure / 실패) should be diagnosable to stage.

## Non-Functional Tests

AI môi trường vận hành (production / 운영 환경) also needs:

- độ trễ (latency / 지연 시간) kiểm thử tải (load test / 부하 테스트);
- bộ nhớ (memory / 메모리)/OOM kiểm thử (test / 테스트);
- tính đồng thời (concurrency / 동시성);
- chi phí (cost / 비용) ngân sách (budget / 예산);
- failover;
- cancellation;
- cold start.

## Tải (load / 로드) Testing

Traffic phân phối (distribution / 분포) should include prompt/đầu vào (input / 입력) length phân phối (distribution / 분포), not only QPS. LLM yêu cầu (request / 요청) chi phí (cost / 비용) varies strongly by tokens.

## Chaos Testing

Inject công cụ (tool / 도구)/API hết thời gian chờ (timeout / 타임아웃), retrieval outage, worker mất mát (loss / 손실) hoặc slow mô hình (model / 모델) to verify fallback/khôi phục (recovery / 복구).

## Regression Suite

Every major sự cố (incident / 인시던트)/bug should become regression kiểm thử (test / 테스트) if feasible. Suite grows from real failures, not only imagined happy paths.

## Kiểm thử (test / 테스트) dữ liệu (data / 데이터) Privacy

Do not bản sao (copy / 복사) raw môi trường vận hành (production / 운영 환경) sensitive dữ liệu (data / 데이터) into permanent kiểm thử (test / 테스트) fixtures without quản trị (governance / 거버넌스). Use redacted/synthetic representative cases when possible.

## Bản phát hành (release / 릴리스) Gate

Tests/evals can define blocking vs informational gates. High-severity an toàn (safety / 안전) regressions should khối (block / 블록) bản phát hành (release / 릴리스) even if average chất lượng (quality / 품질) improves.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Software tests validate code contracts.
AI behavioral tests validate learned/system behavior under representative situations.
```

## Dùng chung (common / 공통) Misconceptions

### “LLM đầu ra (output / 출력) nondeterministic nên không kiểm thử (test / 테스트) được”

Kiểm thử (test / 테스트) properties, validators and success probabilities.

### “Benchmark chính là bộ kiểm thử (test suite / 테스트 스위트)”

Benchmark thường không cover tích hợp (integration / 통합), permissions, độ trễ (latency / 지연 시간) hoặc known sản phẩm (product / 제품) thất bại (failure / 실패) modes.

### “đơn vị (unit / 단위) tests không quan trọng trong AI”

Deterministic hạ tầng (infrastructure / 인프라) bugs often cause more môi trường vận hành (production / 운영 환경) failures than mô hình (model / 모델) math.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [Metrics & Benchmarks](./01_metrics_benchmarks_and_test_design.md), [Robustness](./03_robustness_and_distribution_shift.md), [Red Teaming](./06_red_teaming_and_adversarial_evaluation.md), [CI/CD/CT](../16_mlops_and_llmops/04_ci_cd_ct_for_ai.md).
