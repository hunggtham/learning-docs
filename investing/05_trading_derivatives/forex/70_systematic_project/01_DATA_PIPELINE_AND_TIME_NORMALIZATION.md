# 01 — Dữ liệu (data / 데이터) Chuỗi xử lý (pipeline / 파이프라인) và Thời gian (time / 시간) Normalization cho Systematic FX

Một backtest FX có thể sai ngay từ tầng dữ liệu dù chiến lược (strategy / 전략) mã (code / 코드) hoàn toàn đúng. Các lỗi phổ biến nhất không nằm ở machine học tập (learning / 학습) hay indicator, mà ở những chi tiết rất “nhàm chán”: candle được cắt theo timezone nào, timestamp là sự kiện (event / 이벤트) thời gian (time / 시간) hay receive thời gian (time / 시간), bid/ask có bị trộn với mid không, DST có dịch session hay không, macro giá trị (value / 값) là bản công bố ban đầu hay bản revised nhiều tháng sau.

Mục tiêu của mô-đun (module / 모듈) này là biến dữ liệu (data / 데이터) thành một **point-in-time research dataset** có thể kiểm tra (audit / 감사).

## 1. Bắt đầu bằng dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약)

Trước khi tải dữ liệu (data / 데이터), định nghĩa từng dataset dùng để trả lời câu hỏi gì.

Ví dụ FX quote dataset:

```text
Dataset: fx_quote
Purpose: reconstruct executable market state
Granularity: tick or sampled quote
Required fields:
- instrument
- bid
- ask
- event_timestamp_utc
- receive_timestamp_utc if available
- source
- quality_flag
```

Một OHLC dataset tối thiểu:

```text
instrument
bar_open_timestamp_utc
bar_close_timestamp_utc
open_bid / high_bid / low_bid / close_bid
open_ask / high_ask / low_ask / close_ask
volume_or_tick_count if meaningful
source
```

Nếu chỉ có mid OHLC, phải ghi rõ limitation.

## 2. Sự kiện (event / 이벤트) thời gian (time / 시간) và receive thời gian (time / 시간)

**Sự kiện (event / 이벤트) thời gian (time / 시간)** là lúc thị trường/dữ liệu (data / 데이터) nguồn (source / 소스) nói sự kiện (event / 이벤트) xảy ra.

**Receive thời gian (time / 시간)** là lúc hệ thống (system / 시스템) của bạn nhận được sự kiện (event / 이벤트).

Trong live hệ thống (system / 시스템):

```text
market event happens
→ vendor processes
→ network transmits
→ your system receives
```

Nếu backtest dùng sự kiện (event / 이벤트) thời gian (time / 시간) nhưng live hệ thống (system / 시스템) chỉ có dữ liệu (data / 데이터) sau độ trễ (latency / 지연 시간), kết quả (result / 결과) có thể optimistic.

Với low-frequency daily chiến lược (strategy / 전략), độ trễ (latency / 지연 시간) vài giây có thể không đáng kể. Với event-driven chiến lược (strategy / 전략), nó có thể quyết định toàn bộ edge.

## 3. UTC làm chuẩn gốc (canonical / 정본) timeline

Research lưu trữ (storage / 저장소) nên chuẩn hóa timestamp về UTC.

Display tầng (layer / 계층) có thể convert sang:

```text
New York
London
Seoul
Tokyo
```

Nhưng nội bộ (internal / 내부) joins nên dựa trên chuẩn gốc (canonical / 정본) timezone để tránh ambiguity.

Không lưu cục bộ (local / 로컬) datetime không timezone như:

```text
2026-03-08 02:30
```

vì DST có thể làm thời điểm đó không tồn tại hoặc xuất hiện hai lần tùy jurisdiction.

## 4. DST là lỗi research thật

Một quy tắc (rule / 규칙) như:

```text
Trade London open at 08:00
```

không thể encode đơn giản bằng `08:00 UTC` quanh năm.

London cục bộ (local / 로컬) thời gian (time / 시간) thay đổi theo daylight-saving regime.

Chuỗi xử lý (pipeline / 파이프라인) nên:

```text
Store event in UTC
Keep exchange/financial-centre timezone metadata
Derive session label from timezone-aware calendar
```

Không hard-code session bằng một constant UTC hour nếu chiến lược (strategy / 전략) tồn tại nhiều năm.

## 5. Nghiệp vụ (business / 비즈니스) calendar

FX gần như 24/5 nhưng không có nghĩa mỗi giờ giống nhau.

Calendar tầng (layer / 계층) nên biết:

```text
weekend close/reopen
bank holidays
major financial-centre holidays
year-end abnormal liquidity
DST transitions
value-date holidays
```

Nếu mô hình (model / 모델) roll/financing, holiday calendar còn ảnh hưởng number of days charged.

## 6. Instrument master

Không hard-code pip kích thước (size / 크기) và đặc tả hợp đồng (contract / 계약) kích thước (size / 크기) trong chiến lược (strategy / 전략).

Tạo instrument master:

```text
instrument_id
base_currency
quote_currency
pip_size
price_precision
contract_size_if_applicable
asset_type
trading_timezone_reference
rollover_rule_reference
source
valid_from
valid_to
```

`valid_from`/`valid_to` quan trọng vì specification có thể thay đổi.

## 7. Symbol normalization

Vendor A có thể dùng:

```text
EURUSD
```

Vendor B:

```text
EUR/USD
```

Broker C:

```text
EURUSD.r
```

Không phép nối (join / 조인) raw ticker trực tiếp.

Dùng chuẩn gốc (canonical / 정본) instrument ID:

```text
FX_EUR_USD_SPOT
```

và ánh xạ (mapping / 매핑) bảng (table / 테이블) versioned theo nguồn (source / 소스).

## 8. Bid/ask trước mid

Nếu có bid/ask, lưu cả hai.

Mid:

```text
mid = (bid + ask) / 2
```

có thể derive sau.

Nếu chỉ lưu mid, bạn mất ability reconstruct:

```text
spread
entry side
exit side
stop trigger side
liquidity stress proxy
```

Do đó raw tầng (layer / 계층) nên giữ highest-fidelity dữ liệu (data / 데이터) available.

## 9. Spread sanity checks

Kiểm tra hợp lệ (validation / 검증) rules:

```text
ask >= bid
spread >= 0
price > 0
spread < extreme threshold unless flagged
```

Không auto-delete extreme spreads. Chúng có thể là real stress sự kiện (event / 이벤트).

Thay vì delete:

```text
quality_flag = OUTLIER_SPREAD
```

rồi rà soát (review / 검토) nguồn (source / 소스)/sự kiện (event / 이벤트) ngữ cảnh (context / 맥락).

## 10. Duplicate events

Dữ liệu (data / 데이터) vendor có thể gửi duplicate tick.

Dedup key có thể dựa trên:

```text
source
instrument
source_sequence_id
```

Nếu không có chuỗi (sequence / 시퀀스) ID, timestamp+price dedup có thể accidentally remove legitimate repeated quotes.

Phải hiểu vendor ngữ nghĩa (semantics / 의미론) trước khi dedup.

## 11. Missing intervals

Một missing bar có thể đến từ:

```text
market closed
vendor outage
network issue
illiquid instrument
pipeline failure
```

Không fill tất cả missing bars bằng previous close.

Phân biệt:

```text
EXPECTED_CLOSED
NO_TRADE
DATA_MISSING
UNKNOWN
```

Nếu fill-forward cần cho mô hình (model / 모델), retain flag để tính năng (feature / 기능) biết giá trị (value / 값) không phải observed trade.

## 12. Bar construction

Nếu bản dựng (build / 빌드) candles từ ticks, định nghĩa:

```text
bar boundary
included timestamps
bid/ask/mid source
first/last event rule
empty-bar policy
```

Ví dụ 1-minute bar `[10:00:00, 10:01:00)` khác bar `(10:00:00, 10:01:00]` ở sự kiện (event / 이벤트) ranh giới (boundary / 경계).

Hai backtest khác nhau có thể diverge từ detail này.

## 13. Tick volume không phải toàn cục (global / 전역) FX volume

Retail vendor tick count hoặc broker volume chỉ reflect nguồn (source / 소스) đó.

Do not label trường dữ liệu (field / 필드) simply `volume` unless ngữ nghĩa (semantics / 의미론) are clear.

Prefer:

```text
source_tick_count
broker_reported_volume
exchange_futures_volume
```

Mỗi loại có thông tin (information / 정보) content khác nhau.

## 14. Futures dữ liệu (data / 데이터) vs OTC spot

Currency futures có centralized exchange volume/thứ tự (order / 순서) book, nhưng không phải toàn bộ toàn cục (global / 전역) FX thị trường (market / 시장).

Nếu dùng futures as proxy:

```text
spot_pair
futures_contract
expiry
roll rule
basis
trading hours
```

phải tường minh (explicit / 명시적).

Không phép nối (join / 조인) futures price vào spot chiến lược (strategy / 전략) mà bỏ basis/maturity differences.

## 15. Macro bản phát hành (release / 릴리스) dataset

Một macro bảng (table / 테이블) nên có nhiều timestamps:

```text
indicator_id
reference_period
release_timestamp_utc
value_first_release
consensus_if_available
previous_value_as_known_then
revision_timestamp
revised_value
source
```

Điều quan trọng là `value_first_release` và `previous_value_as_known_then`.

## 16. Revised dữ liệu (data / 데이터) leakage

Nếu backtest 2018 CPI chiến lược (strategy / 전략) dùng 2026 cơ sở dữ liệu (database / 데이터베이스) export với historical series đã revised, mô hình (model / 모델) có thể thấy thông tin (information / 정보) chưa tồn tại lúc đó.

Need vintage lưu trữ (storage / 저장소):

```text
What did the researcher know
at timestamp T?
```

Point-in-time truy vấn (query / 쿼리) phải answer được câu đó.

## 17. Consensus is also timestamped dữ liệu (data / 데이터)

Consensus forecast thay đổi tới gần bản phát hành (release / 릴리스).

Một chiến lược (strategy / 전략) dùng surprise:

```text
actual - consensus
```

phải define consensus snapshot:

```text
24h before?
1h before?
latest available before release?
```

Không dùng final consensus compiled after sự kiện (event / 이벤트).

## 18. Central-bank quyết định (decision / 결정) siêu dữ liệu (metadata / 메타데이터)

Một chính sách (policy / 정책) sự kiện (event / 이벤트) bảng (table / 테이블) có thể lưu:

```text
meeting_date
announcement_timestamp
policy_rate_before
policy_rate_after
expected_change_before_event
guidance_label or structured fields
press_conference_timestamp
```

Nếu chiến lược (strategy / 전략) reacts to statement vs press conference, timestamps phải tách riêng.

## 19. News văn bản (text / 텍스트) and point-in-time availability

Nếu dùng NLP/news:

```text
article_published_at
article_first_seen_at
article_updated_at
source
version
```

Không dùng updated article văn bản (text / 텍스트) như thể phiên bản (version / 버전) đó tồn tại ngay khi headline đầu tiên phát hành.

## 20. Dữ liệu (data / 데이터) lineage

Mỗi transformed dataset nên biết nguồn (source / 소스) parents.

Example:

```text
fx_1m_features_v3
← fx_quotes_vendorA_v7
← session_calendar_v2
← instrument_master_v4
```

Lineage giúp gỡ lỗi (debug / 디버그) khi kết quả (result / 결과) thay đổi sau dữ liệu (data / 데이터) cập nhật (update / 업데이트).

## 21. Raw / clean / tính năng (feature / 기능) layers

Một cấu trúc đơn giản:

```text
raw/
clean/
features/
research_snapshots/
```

`raw` immutable nếu có thể.

`clean` apply documented kiểm tra hợp lệ (validation / 검증)/correction.

`features` derived variables.

`research_snapshots` freeze chính xác (exact / 정확한) inputs used in a published experiment.

## 22. Never silently overwrite historical dữ liệu (data / 데이터)

Nếu vendor correction arrives:

```text
create new dataset version
```

Không silently replace old tệp (file / 파일) rồi để old backtest trở nên unreproducible.

## 23. Hashing and versioning

Một run siêu dữ liệu (metadata / 메타데이터) có thể lưu:

```text
data_version
file_hash
config_hash
code_commit
```

Nếu raw dataset rất lớn, băm (hash / 해시) manifest thay vì mỗi row.

Mục tiêu là detect đầu vào (input / 입력) changes.

## 24. Currency conversion dữ liệu (data / 데이터)

P/L reporting cần FX conversion.

Nếu account currency USD nhưng trade EUR/GBP:

```text
P/L initially in GBP
→ need GBP/USD conversion
```

Backtest phải dùng conversion tỷ lệ (rate / 비율) available at that timestamp, không hiện tại (current / 현재) tỷ lệ (rate / 비율).

## 25. Triangular consistency checks

Ví dụ:

```text
EUR/USD × USD/JPY ≈ EUR/JPY
```

Difference vượt threshold có thể báo:

```text
stale quote
source mismatch
wrong timestamp alignment
```

Nhưng bid/ask và độ trễ (latency / 지연 시간) làm chính xác (exact / 정확한) equality không expected.

## 26. Corporate actions analogy does not apply directly

FX spot không có stock split/dividend adjustment giống equity.

Nhưng có instrument-specific changes:

```text
currency redenomination
peg/regime change
vendor symbol change
contract specification change
```

Chuỗi xử lý (pipeline / 파이프라인) vẫn cần historical siêu dữ liệu (metadata / 메타데이터).

## 27. Price sanity by return

Compute log return:

```text
r_t = ln(P_t / P_{t-1})
```

Flag extreme values based on broad threshold.

Nhưng không auto-remove 2015 CHF-like jump chỉ vì z-score huge.

Extreme return may be most important observation in rủi ro (risk / 위험) research.

## 28. Cross-source comparison

Nếu có hai vendors:

```text
compare mid
compare spread
compare timestamps
```

Persistent divergence can reveal ánh xạ (mapping / 매핑)/timezone bài toán (problem / 문제).

Occasional micro-difference may be normal OTC fragmentation.

## 29. Dữ liệu (data / 데이터) chất lượng (quality / 품질) report

Mỗi ingest batch nên produce:

```text
rows
start/end timestamp
missing intervals
negative/zero prices
crossed markets
spread percentiles
extreme returns
duplicate count
timezone anomalies
```

Chất lượng (quality / 품질) report should be stored with dataset phiên bản (version / 버전).

## 30. Lược đồ (schema / 스키마) evolution

Nếu thêm trường dữ liệu (field / 필드) mới:

```text
schema_version++
```

Downstream mã (code / 코드) must know whether trường dữ liệu (field / 필드) exists historically.

Do not infer missing trường dữ liệu (field / 필드) ngữ nghĩa (semantics / 의미론) silently.

## 31. Tính năng (feature / 기능) causality

Mỗi tính năng (feature / 기능) cần answer:

```text
What raw data does it use?
What timestamps are included?
Could any input occur after decision time?
```

Example bad rolling mean:

```text
centered rolling window
```

because it uses future observations.

Use trailing cửa sổ (window / 윈도우) unless chiến lược (strategy / 전략) genuinely has future dữ liệu (data / 데이터)—which it cannot.

## 32. Session features

Examples:

```text
is_asia_session
is_london_session
is_london_ny_overlap
minutes_since_session_open
```

Derive from timezone-aware calendar, not fixed UTC across years.

## 33. Event-distance features

Useful point-in-time features:

```text
minutes_to_next_known_central_bank_event
minutes_since_last_macro_release
```

Future scheduled calendar is known, but **future kết quả (outcome / 결과)** is not.

Distinguish known schedule from unknown kết quả (result / 결과).

## 34. Dữ liệu (data / 데이터) split must preserve thời gian (time / 시간)

Do not random-shuffle thời gian (time / 시간) series observations before train/kiểm thử (test / 테스트) split if dependence matters.

Basic:

```text
train < validation < test chronologically
```

Advanced methodology may use purging/embargo around overlapping labels.

## 35. Snapshot before experiment

Before serious backtest:

```text
freeze data version
freeze feature config
freeze universe
freeze split dates
```

Then run.

Do not keep mutating dataset until kết quả (result / 결과) becomes attractive.

## 36. Minimal dữ liệu (data / 데이터) manifest

`data_manifest.md` should include:

```text
Dataset name
Source
License/access note
Coverage period
Frequency
Timezone
Bid/ask/mid semantics
Known gaps
Revision policy
Version/hash
Used by which strategy
```

## 37. Example relational lược đồ (schema / 스키마)

```text
instrument_master
fx_quote
fx_bar
macro_release
central_bank_event
calendar_session
financing_rate
experiment_run
```

Keys should prefer stable IDs over vendor labels.

## 38. SQL-style point-in-time phép nối (join / 조인)

Conceptual lô-gic (logic / 논리):

```text
for each decision_timestamp T:
    use latest record
    whose information_available_timestamp <= T
```

Not:

```text
join on reference_month
and accidentally pull revised future value
```

## 39. Reproducibility kiểm thử (test / 테스트)

A successful chuỗi xử lý (pipeline / 파이프라인) passes:

```text
same code version
+ same config
+ same data snapshot
→ same feature rows
```

If đầu ra (output / 출력) changes nondeterministically, fix before interpreting backtest.

## 40. Thất bại (failure / 실패) injection

Kiểm thử (test / 테스트) chuỗi xử lý (pipeline / 파이프라인) with:

```text
missing hour
DST transition
duplicate ticks
negative spread bug
macro revision
vendor outage
symbol rename
```

Hệ thống (system / 시스템) should thất bại (fail / 실패) loudly or flag degraded dữ liệu (data / 데이터), not silently continue.

## 41. Dữ liệu (data / 데이터) chất lượng (quality / 품질) vs chiến lược (strategy / 전략) chất lượng (quality / 품질)

If chiến lược (strategy / 전략) stops working after correcting a timezone bug, chiến lược (strategy / 전략) was not robust bằng chứng (evidence / 증거).

Never preserve wrong dữ liệu (data / 데이터) hành vi (behavior / 동작) just because equity curve looked better.

## 42. Deliverables

Create:

```text
schema.md
data_manifest.md
calendar_spec.md
instrument_master_spec.md
validation_rules.md
data_quality_report.md
point_in_time_join_spec.md
```

## 43. Completion criteria

Mô-đun (module / 모듈) complete when a reviewer can answer:

```text
What did the strategy know at each decision timestamp?
Which price side was available?
How were sessions defined?
How were revisions handled?
Can the exact dataset be reconstructed?
```

Nếu một câu trả lời vẫn là “probably”, chuỗi xử lý (pipeline / 파이프라인) chưa đủ chuẩn cho serious research.

## Đọc tiếp

→ [02 — Backtest Engine và Execution Model](./02_BACKTEST_ENGINE_AND_EXECUTION_MODEL.md)

Liên quan:

- [10 — Backtesting and point-in-time FX data](../10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
- [05 — Execution, brokers, costs and risk](../05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
