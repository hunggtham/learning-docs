# Economics — source ledger và data/forecast currentness boundary

> **Owner:** `economics/` (canonical economics content). Ledger này định tuyến theory, official statistics, empirical papers và forecast; model assumptions phải được ghi riêng.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| ECO-WB-01 | World Bank Open Data | macro/development indicators, poverty, trade và labor data | https://data.worldbank.org/ | indicator/period/revision phải ghi; portal kiểm tra 2026-10-09 | Definition, country coverage, base year và revision cần ghi; indicator không tự là causal proof | macro/development |
| ECO-IMF-01 | IMF Data | national accounts, balance of payments, fiscal/monetary và WEO datasets | https://data.imf.org/ | dataset/vintage/release phải ghi | Forecast và historical estimate phải tách; ghi vintage, assumptions và revision | macro/forecast |
| ECO-OECD-01 | OECD Data | comparative labor, productivity, education, tax và social indicators | https://data.oecd.org/ | indicator/methodology/period phải ghi | Cross-country comparability phụ thuộc definition/method; không bỏ qua metadata | applied/comparative economics |
| ECO-FRED-01 | Federal Reserve Bank of St. Louis — FRED | U.S. time series and metadata | https://fred.stlouisfed.org/ | series ID/release date phải ghi | FRED may revise series; ghi observation date, release/vintage và geography | macro/time series |
| ECO-NBER-01 | National Bureau of Economic Research | working papers and empirical research | https://www.nber.org/papers | working-paper date/version/DOI phải ghi | Working paper không đồng nghĩa peer-reviewed consensus; ghi identification/design/limitations | econometrics/applied |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| ECO-CAUSAL-01 | `REVIEW_REQUIRED` | Causal claim phải nêu identification/design, confounders, population, time window và uncertainty; correlation/forecast không đủ. | Owner econometrics/applied |
| ECO-DATA-01 | `NEEDS_SOURCE` | GDP, inflation, unemployment, trade, inequality và poverty claim phải ghi series, definition, base year, vintage và period. | Owner relevant chapter |
| ECO-FORECAST-01 | `REVIEW_REQUIRED` | Forecast cần model/provider/vintage/assumptions; không viết forecast như observed fact. | Owner macro/forecast |
| ECO-POLICY-01 | `NEEDS_SOURCE` | Tax, interest rate, regulation, subsidy và current policy cần authority đúng jurisdiction và effective date. | Owner applied/policy |

## Quy trình refresh

1. Ghi dataset/series ID, metadata, period, vintage/revision và ngày tải cho mọi số liệu.
2. Tách theory/model assumption, observed data, estimate, forecast và author inference.
3. Khi provider revise series hoặc forecast vintage, cập nhật bảng/claim và mở review cho affected prose.
4. Structural audit không xác nhận economic data còn current hoặc causal interpretation đúng.
