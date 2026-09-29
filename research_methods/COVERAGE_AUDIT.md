# Research Methods — Coverage Kiểm tra (audit / 감사)

## Kết luận hiện tại

Research Methods đã có cốt lõi (core / 핵심) chuẩn gốc (canonical / 정본) tuyến (route / 경로) đủ để phục vụ các lĩnh vực (domain / 도메인) khác mà không duplicate Econometrics. Five cốt lõi (core / 핵심) modules hiện cover research thiết kế (design / 설계), đo lường (measurement / 측정)/sampling, qualitative methods, bằng chứng (evidence / 증거) synthesis, mixed methods/ethics/reproducibility.

Lĩnh vực (domain / 도메인) này được xem là **cốt lõi (core / 핵심) complete ở foundation mức (level / 수준)**. Advanced methods chỉ nên mở khi một lĩnh vực (domain / 도메인) cụ thể cần, ví dụ advanced psychometrics, mạng (network / 네트워크) phân tích (analysis / 분석), text-as-data, spatial methods hoặc hiện thực (implementation / 구현) science.

## Coverage ma trận (matrix / 행렬)

| Mô-đun (module / 모듈) | Trạng thái | Coverage |
|---|---|---|
| 00 Research Questions, Lý thuyết (theory / 이론) & Thiết kế (design / 설계) | Cốt lõi (core / 핵심) complete | question types, concepts, lý thuyết (theory / 이론), hypotheses, mechanisms, rival explanations, phạm vi (scope / 범위), trường hợp (case / 사례)/longitudinal/comparative/experimental thiết kế (design / 설계), validity |
| 01 Đo lường (measurement / 측정), Sampling & Survey Thiết kế (design / 설계) | Cốt lõi (core / 핵심) complete | độ tin cậy (reliability / 신뢰성)/validity, invariance, scales, survey wording/chế độ (mode / 모드), sampling frames, xác suất (probability / 확률)/nonprobability sampling, weighting, nonresponse, dữ liệu (data / 데이터) chất lượng (quality / 품질) |
| 02 Qualitative Methods | Cốt lõi (core / 핵심) complete | interviews, observation, ethnography, purposive sampling, coding, thematic/content/discourse phân tích (analysis / 분석), tiến trình (process / 프로세스) tracing, reflexivity, triangulation |
| 03 Systematic Reviews & Bằng chứng (evidence / 증거) Synthesis | Cốt lõi (core / 핵심) complete | protocols, searches, screening, extraction, rủi ro (risk / 위험) of độ lệch (bias / 편향), meta-analysis, heterogeneity, publication độ lệch (bias / 편향), qualitative synthesis, certainty |
| 04 Mixed Methods, Ethics, Reproducibility & Open Science | Cốt lõi (core / 핵심) complete | convergent/sequential/embedded designs, ethics/privacy, preregistration, reproducibility, replication, dữ liệu (data / 데이터)/mã (code / 코드) sharing, AI-assisted research boundaries |

## Lĩnh vực (domain / 도메인) ranh giới (boundary / 경계)

### Econometrics

`economics/05_econometrics/` owns estimator-level detail and quantitative nhân quả (causal / 인과적)/statistical identification. Research Methods should cross-link rather than repeat OLS, IV, RDD, DiD, panel or time-series derivations.

### Philosophy

Philosophy owns epistemology and philosophy-of-science foundations. Research Methods operationalizes those ideas into study thiết kế (design / 설계), bằng chứng (evidence / 증거) and reporting.

### Psychology / Sociology / Lịch sử (history / 이력) / Nghiệp vụ (business / 비즈니스) / Kỹ thuật (engineering / 엔지니어링)

These domains should keep domain-specific đo lường (measurement / 측정) and cases, while generic sampling, survey, interview, systematic-review and reproducibility principles remain chuẩn gốc (canonical / 정본) here.

## Quality gates

Every research sản phẩm tạo ra (artifact / 산출물) should make tường minh (explicit / 명시적):

```text
question + claim type
scope / population / case boundary
construct + measurement
sampling / case-selection logic
evidence provenance
design / analysis method
validity threats / rival explanations
ethics / privacy
uncertainty / external validity
reproducibility / audit trail
```

## Anti-patterns

Do not treat:

```text
large sample = representative
reliability = validity
statistical significance = causal evidence
participant explanation = causal proof
many papers = strong evidence
reproducibility = correctness
ethics approval = complete ethical reasoning
```

## Advanced expansion gate

Only add a new methodology chapter when:

1. it is reused across multiple domains;
2. hiện tại (current / 현재) chapters cannot explain it without becoming bloated;
3. it has distinct inferential các giả định (assumptions / 가정들)/thất bại (failure / 실패) modes;
4. there is enough độ sâu (depth / 깊이) to teach cơ chế (mechanism / 메커니즘), not glossary.

Potential advanced modules: psychometrics/latent variables, mạng (network / 네트워크) methods, text-as-data/content computation, spatial research methods, hiện thực (implementation / 구현)/tiến trình (process / 프로세스) evaluation.

## Next repo-wide priority

After Research Methods, the next content gap identified by the repository kiểm tra (audit / 감사) is **Sociology**. Sociology should reuse this thư viện (library / 라이브러리) for thiết kế (design / 설계)/đo lường (measurement / 측정) and Psychology/Economics for individual/economic mechanisms rather than duplicate them.
