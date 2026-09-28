# Economics — Coverage Kiểm tra (audit / 감사)

## Kết luận hiện tại

Economics cốt lõi (core / 핵심) hiện đã hoàn chỉnh ở cấp chuẩn gốc (canonical / 정본) lộ trình học (learning path / 학습 경로): `00 Foundations`, `01 Microeconomics`, `02 Market Structure & Game Theory`, `03 Macroeconomics`, `04 Applied Economics`, `05 Econometrics` và `06 Economic History & Institutions` đều có trục học (learning spine / 학습 축), độ sâu (depth / 깊이) gate, bằng chứng (evidence / 증거) ranh giới (boundary / 경계) và cross-domain tích hợp (integration / 통합).

Điều này không có nghĩa mọi advanced subfield đã được viết. Nó nghĩa người đọc hiện có một tuyến (route / 경로) đầy đủ từ nguyên lý nền tảng (first principles / 제일 원리) → individual/firm choice → strategic markets → aggregate economy → nhân quả (causal / 인과적) empirical methods → applied fields → institutions/lịch sử (history / 이력) mà không cần nhảy ra ngoài chỉ để lấp các khái niệm cốt lõi (core / 핵심).

## Coverage ma trận (matrix / 행렬)

| Mô-đun (module / 모듈) | Trạng thái | Coverage hiện có | Advanced gaps chỉ mở khi cần |
|---|---|---|---|
| 00 Foundations | Chuẩn gốc (canonical / 정본) baseline | scarcity, opportunity chi phí (cost / 비용), marginal phân tích (analysis / 분석), incentives, equilibrium, PPF, efficiency/equity, positive/normative, comparative statics | bất định (uncertainty / 불확실성) formal hơn, behavioral/institutional foundations |
| 01 Microeconomics | **Cốt lõi (core / 핵심) complete** | bên tiêu thụ (consumer / 소비자)/producer; welfare; externality; công khai (public / 공개) goods/commons; thông tin (information / 정보) asymmetry/contracts | intertemporal choice, expected utility, general equilibrium |
| 02 Thị trường (market / 시장) Cấu trúc (structure / 구조) & Game Lý thuyết (theory / 이론) | **Cốt lõi (core / 핵심) complete** | monopoly/competition, oligopoly, Cournot/Bertrand, sequential/repeated games, entry/collusion, auctions/cơ chế (mechanism / 메커니즘) thiết kế (design / 설계) | động (dynamic / 동적) games, advanced cơ chế (mechanism / 메커니즘) thiết kế (design / 설계) |
| 03 Macroeconomics | **Cốt lõi (core / 핵심) complete** | đo lường (measurement / 측정); growth; labor/inflation; money/banking; monetary/fiscal chính sách (policy / 정책); nghiệp vụ (business / 비즈니스) cycles; open economy/crises | heterogeneous-agent macro, advanced DSGE/structural macro |
| 04 Applied Economics | **Cốt lõi (core / 핵심) complete** | labor; công khai (public / 공개); trade; development; industrial organization | environmental, health, education, urban/spatial if needed |
| 05 Econometrics | **Foundation complete** | đo lường (measurement / 측정)/estimands; OLS; experiments/selection; IV/RDD; panel/DiD; thời gian (time / 시간) series/macro identification; robustness/bên ngoài (external / 외부) validity | nhân quả (causal / 인과적) ML, structural estimation, duration/count/spatial methods |
| 06 Economic Lịch sử (history / 이력) & Institutions | **Cốt lõi (core / 핵심) complete** | thuộc tính (property / 속성)/contracts/trạng thái (state / 상태) sức chứa (capacity / 용량); money/finance/fiscal states; industrialization/globalization; crises/regimes/đường dẫn (path / 경로) dependence | deeper regional/period trường hợp (case / 사례) studies via cross-links, not duplicated chronology |

## 06 — Economic Lịch sử (history / 이력) & Institutions độ sâu (depth / 깊이) gate

Chuẩn gốc (canonical / 정본) chuỗi (sequence / 시퀀스):

```text
00 Institutions, Property Rights & State Capacity
01 Money, Finance & Fiscal States
02 Technology, Industrialization & Globalization
03 Crises, Regime Change & Path Dependence
```

Độ sâu (depth / 깊이) gate gồm:

- formal vs informal institutions; rules vs enforcement; thuộc tính (property / 속성)/đặc tả hợp đồng (contract / 계약) rights; fiscal/thông tin (information / 정보)/legal trạng thái (state / 상태) sức chứa (capacity / 용량); credible commitment; rent-seeking và political power;
- money/payment institutions, banking/clearing, công khai (public / 공개) debt, fiscal sức chứa (capacity / 용량), corporate forms, financial deepening, regulation và crisis hạ tầng (infrastructure / 인프라);
- Malthusian ràng buộc (constraint / 제약조건), năng lượng (energy / 에너지), general-purpose technologies, diffusion, factory/management organization, vận chuyển (transport / 전송), structural transformation, globalization, di chuyển (migration / 마이그레이션) và động (dynamic / 동적) comparative advantage;
- leverage/amplification, banking/sovereign/currency crises, chính sách (policy / 정책) regimes, reconstruction, Lucas critique, hysteresis, lock-in, multiple equilibria và historical identification.

Lịch sử (history / 이력) is used as a cơ chế (mechanism / 메커니즘) laboratory. Chronology, political actors and detailed sự kiện (event / 이벤트) chuỗi (sequence / 시퀀스) remain chuẩn gốc (canonical / 정본) in `world_history/` and `korean_history/`.

## Economics-wide bằng chứng (evidence / 증거) discipline

Giữ bốn rules:

```text
Model ≠ Evidence
Accounting Identity ≠ Causal Theory
Estimator ≠ Identification Strategy
Causal Estimate ≠ Policy Recommendation
```

Historical tầng (layer / 계층) thêm:

```text
Persistence ≠ Path Dependence
Formal Rule ≠ Effective Enforcement
```

Một historical association chỉ trở thành nhân quả (causal / 인과적) claim khi assignment/nguồn (source / 소스) of variation và alternative persistent channels được xử lý đủ rõ.

## Tích hợp (integration / 통합) rules

- **Lịch sử (history / 이력):** Economics cross-link chronology; không bản sao (copy / 복사) timeline.
- **Geography:** geography có thể là ràng buộc (constraint / 제약조건), treatment, confounder hoặc instrument; phải nêu cơ chế (mechanism / 메커니즘).
- **Psychology:** hành vi (behavior / 동작)/expectations/salience bổ sung rational baseline.
- **Investing:** thị trường (market / 시장)/asset interpretation giữ ở Investing; Economics giữ cơ chế (mechanism / 메커니즘) và bằng chứng (evidence / 증거) foundation.
- **Korea Nghiệp vụ (business / 비즈니스):** contemporary Korean institutional/company cases ở trường hợp (case / 사례) tầng (layer / 계층) riêng.
- **Khoa học máy tính (computer science / 컴퓨터 과학):** computational methods/platforms/auctions được cross-link khi relevant.

## Advanced expansion gate

Không tiếp tục mở Economics theo lô-gic (logic / 논리) “còn subfield là phải có folder”. Chỉ thêm advanced chapter khi ít nhất một điều kiện đúng:

1. existing chapter cần prerequisite đó để không giải thích nửa chừng;
2. một lĩnh vực (domain / 도메인) khác phụ thuộc trực tiếp vào nó;
3. topic tạo học tập (learning / 학습) giá trị (value / 값) khác biệt, không duplicate;
4. có thể viết đủ các giả định (assumptions / 가정들)/bằng chứng (evidence / 증거)/thất bại (failure / 실패) modes, không chỉ glossary.

Các ứng viên sau này: intertemporal choice/bất định (uncertainty / 불확실성), heterogeneous-agent macro, structural IO, nhân quả (causal / 인과적) ML, spatial/environmental/health economics.

## Repo-wide priority sau Economics

Sau độ sâu (depth / 깊이) pass này, Economics không còn là lĩnh vực (domain / 도메인) ưu tiên cần mở rộng tiếp ngay. Priority nên quay sang các vùng còn mỏng hơn:

```text
Research Methods
→ Sociology
→ Frontend canonical/root structure
→ repo-wide audit automation
```

Sau đó mới chạy cross-domain rà soát (review / 검토) để tìm gaps thật sự thay vì tiếp tục thêm files vào các thư viện (library / 라이브러리) đã đủ cốt lõi (core / 핵심).

## Completion criterion

Economics được đánh dấu **core-domain complete** khi:

- tất cả `00–06` có chuẩn gốc (canonical / 정본) tuyến (route / 경로);
- README + coverage kiểm tra (audit / 감사) + danh mục (catalog / 카탈로그) phản ánh nguồn chuẩn (source of truth / 정본);
- nội bộ (internal / 내부) boundaries với Investing/Lịch sử (history / 이력)/Korea/Geography rõ;
- lý thuyết (theory / 이론), bằng chứng (evidence / 증거) và normative conclusions được tách;
- applied chapters có estimand + identification;
- historical chapters có enforcement/power/persistence cơ chế (mechanism / 메커니즘).

Các tiêu chí trên hiện đã đạt sau độ sâu (depth / 깊이) pass này, subject to final danh mục (catalog / 카탈로그) synchronization on `main`.
