# 01 — Data Pipeline và Time Normalization cho Systematic FX

Một backtest FX có thể sai ngay từ tầng dữ liệu dù strategy code hoàn toàn đúng. Các lỗi phổ biến nhất không nằm ở machine learning hay indicator, mà ở những chi tiết rất “nhàm chán”: candle được cắt theo timezone nào, timestamp là event time hay receive time, bid/ask có bị trộn với mid không, DST có dịch session hay không, macro value là bản công bố ban đầu hay bản revised nhiều tháng sau.

Mục tiêu của module này là biến data thành một **point-in-time research dataset** có thể audit.

## 1. Bắt đầu bằng data contract

Trước khi tải data, định nghĩa từng dataset dùng để trả lời câu hỏi gì.

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

## 2. Event time và receive time

**Event time** là lúc thị trường/data source nói event xảy ra.

**Receive time** là lúc system của bạn nhận được event.

Trong live system:

```text
market event happens
→ vendor processes
→ network transmits
→ your system receives
```

Nếu backtest dùng event time nhưng live system chỉ có data sau latency, result có thể optimistic.

Với low-frequency daily strategy, latency vài giây có thể không đáng kể. Với event-driven strategy, nó có thể quyết định toàn bộ edge.

## 3. UTC làm canonical timeline

Research storage nên chuẩn hóa timestamp về UTC.

Display layer có thể convert sang:

```text
New York
London
Seoul
Tokyo
```

Nhưng internal joins nên dựa trên canonical timezone để tránh ambiguity.

Không lưu local datetime không timezone như:

```text
2026-03-08 02:30
```

vì DST có thể làm thời điểm đó không tồn tại hoặc xuất hiện hai lần tùy jurisdiction.

## 4. DST là lỗi research thật

Một rule như:

```text
Trade London open at 08:00
```

không thể encode đơn giản bằng `08:00 UTC` quanh năm.

London local time thay đổi theo daylight-saving regime.

Pipeline nên:

```text
Store event in UTC
Keep exchange/financial-centre timezone metadata
Derive session label from timezone-aware calendar
```

Không hard-code session bằng một constant UTC hour nếu strategy tồn tại nhiều năm.

## 5. Business calendar

FX gần như 24/5 nhưng không có nghĩa mỗi giờ giống nhau.

Calendar layer nên biết:

```text
weekend close/reopen
bank holidays
major financial-centre holidays
year-end abnormal liquidity
DST transitions
value-date holidays
```

Nếu model roll/financing, holiday calendar còn ảnh hưởng number of days charged.

## 6. Instrument master

Không hard-code pip size và contract size trong strategy.

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

Không join raw ticker trực tiếp.

Dùng canonical instrument ID:

```text
FX_EUR_USD_SPOT
```

và mapping table versioned theo source.

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

Do đó raw layer nên giữ highest-fidelity data available.

## 9. Spread sanity checks

Validation rules:

```text
ask >= bid
spread >= 0
price > 0
spread < extreme threshold unless flagged
```

Không auto-delete extreme spreads. Chúng có thể là real stress event.

Thay vì delete:

```text
quality_flag = OUTLIER_SPREAD
```

rồi review source/event context.

## 10. Duplicate events

Data vendor có thể gửi duplicate tick.

Dedup key có thể dựa trên:

```text
source
instrument
source_sequence_id
```

Nếu không có sequence ID, timestamp+price dedup có thể accidentally remove legitimate repeated quotes.

Phải hiểu vendor semantics trước khi dedup.

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

Nếu fill-forward cần cho model, retain flag để feature biết value không phải observed trade.

## 12. Bar construction

Nếu build candles từ ticks, định nghĩa:

```text
bar boundary
included timestamps
bid/ask/mid source
first/last event rule
empty-bar policy
```

Ví dụ 1-minute bar `[10:00:00, 10:01:00)` khác bar `(10:00:00, 10:01:00]` ở event boundary.

Hai backtest khác nhau có thể diverge từ detail này.

## 13. Tick volume không phải global FX volume

Retail vendor tick count hoặc broker volume chỉ reflect source đó.

Do not label field simply `volume` unless semantics are clear.

Prefer:

```text
source_tick_count
broker_reported_volume
exchange_futures_volume
```

Mỗi loại có information content khác nhau.

## 14. Futures data vs OTC spot

Currency futures có centralized exchange volume/order book, nhưng không phải toàn bộ global FX market.

Nếu dùng futures as proxy:

```text
spot_pair
futures_contract
expiry
roll rule
basis
trading hours
```

phải explicit.

Không join futures price vào spot strategy mà bỏ basis/maturity differences.

## 15. Macro release dataset

Một macro table nên có nhiều timestamps:

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

## 16. Revised data leakage

Nếu backtest 2018 CPI strategy dùng 2026 database export với historical series đã revised, model có thể thấy information chưa tồn tại lúc đó.

Need vintage storage:

```text
What did the researcher know
at timestamp T?
```

Point-in-time query phải answer được câu đó.

## 17. Consensus is also timestamped data

Consensus forecast thay đổi tới gần release.

Một strategy dùng surprise:

```text
actual - consensus
```

phải define consensus snapshot:

```text
24h before?
1h before?
latest available before release?
```

Không dùng final consensus compiled after event.

## 18. Central-bank decision metadata

Một policy event table có thể lưu:

```text
meeting_date
announcement_timestamp
policy_rate_before
policy_rate_after
expected_change_before_event
guidance_label or structured fields
press_conference_timestamp
```

Nếu strategy reacts to statement vs press conference, timestamps phải tách riêng.

## 19. News text and point-in-time availability

Nếu dùng NLP/news:

```text
article_published_at
article_first_seen_at
article_updated_at
source
version
```

Không dùng updated article text như thể version đó tồn tại ngay khi headline đầu tiên phát hành.

## 20. Data lineage

Mỗi transformed dataset nên biết source parents.

Example:

```text
fx_1m_features_v3
← fx_quotes_vendorA_v7
← session_calendar_v2
← instrument_master_v4
```

Lineage giúp debug khi result thay đổi sau data update.

## 21. Raw / clean / feature layers

Một cấu trúc đơn giản:

```text
raw/
clean/
features/
research_snapshots/
```

`raw` immutable nếu có thể.

`clean` apply documented validation/correction.

`features` derived variables.

`research_snapshots` freeze exact inputs used in a published experiment.

## 22. Never silently overwrite historical data

Nếu vendor correction arrives:

```text
create new dataset version
```

Không silently replace old file rồi để old backtest trở nên unreproducible.

## 23. Hashing and versioning

Một run metadata có thể lưu:

```text
data_version
file_hash
config_hash
code_commit
```

Nếu raw dataset rất lớn, hash manifest thay vì mỗi row.

Mục tiêu là detect input changes.

## 24. Currency conversion data

P/L reporting cần FX conversion.

Nếu account currency USD nhưng trade EUR/GBP:

```text
P/L initially in GBP
→ need GBP/USD conversion
```

Backtest phải dùng conversion rate available at that timestamp, không current rate.

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

Nhưng bid/ask và latency làm exact equality không expected.

## 26. Corporate actions analogy does not apply directly

FX spot không có stock split/dividend adjustment giống equity.

Nhưng có instrument-specific changes:

```text
currency redenomination
peg/regime change
vendor symbol change
contract specification change
```

Pipeline vẫn cần historical metadata.

## 27. Price sanity by return

Compute log return:

```text
r_t = ln(P_t / P_{t-1})
```

Flag extreme values based on broad threshold.

Nhưng không auto-remove 2015 CHF-like jump chỉ vì z-score huge.

Extreme return may be most important observation in risk research.

## 28. Cross-source comparison

Nếu có hai vendors:

```text
compare mid
compare spread
compare timestamps
```

Persistent divergence can reveal mapping/timezone problem.

Occasional micro-difference may be normal OTC fragmentation.

## 29. Data quality report

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

Quality report should be stored with dataset version.

## 30. Schema evolution

Nếu thêm field mới:

```text
schema_version++
```

Downstream code must know whether field exists historically.

Do not infer missing field semantics silently.

## 31. Feature causality

Mỗi feature cần answer:

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

Use trailing window unless strategy genuinely has future data—which it cannot.

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

Future scheduled calendar is known, but **future outcome** is not.

Distinguish known schedule from unknown result.

## 34. Data split must preserve time

Do not random-shuffle time series observations before train/test split if dependence matters.

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

Do not keep mutating dataset until result becomes attractive.

## 36. Minimal data manifest

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

## 37. Example relational schema

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

## 38. SQL-style point-in-time join

Conceptual logic:

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

## 39. Reproducibility test

A successful pipeline passes:

```text
same code version
+ same config
+ same data snapshot
→ same feature rows
```

If output changes nondeterministically, fix before interpreting backtest.

## 40. Failure injection

Test pipeline with:

```text
missing hour
DST transition
duplicate ticks
negative spread bug
macro revision
vendor outage
symbol rename
```

System should fail loudly or flag degraded data, not silently continue.

## 41. Data quality vs strategy quality

If strategy stops working after correcting a timezone bug, strategy was not robust evidence.

Never preserve wrong data behavior just because equity curve looked better.

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

Module complete when a reviewer can answer:

```text
What did the strategy know at each decision timestamp?
Which price side was available?
How were sessions defined?
How were revisions handled?
Can the exact dataset be reconstructed?
```

Nếu một câu trả lời vẫn là “probably”, pipeline chưa đủ chuẩn cho serious research.

## Đọc tiếp

→ [02 — Backtest Engine và Execution Model](./02_BACKTEST_ENGINE_AND_EXECUTION_MODEL.md)

Liên quan:

- [10 — Backtesting and point-in-time FX data](../10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
- [05 — Execution, brokers, costs and risk](../05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
