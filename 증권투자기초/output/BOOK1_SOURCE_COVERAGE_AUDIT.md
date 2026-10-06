# Book 1 — Source Coverage Audit

## Kết luận pass audit

Audit này đối chiếu toàn bộ `증권투자기초/raw_md/sach1.md` với các tài liệu
canonical trong `output/book1/`. Source đã được đọc theo các vùng Page 1–168 của
Markdown OCR; nội dung giáo trình tương ứng khoảng trang in 13–351.

**Kết luận hiện tại: `PASS CÓ ĐIỀU KIỆN — semantic coverage đã được rebuild; các
con số pháp lý vẫn là snapshot nguồn.** Các lesson đã được bổ sung bảng, điều
kiện, công thức, ví dụ và checkpoint hiểu bài; `90-review-and-source-trace.md`
đã nối các dải câu hỏi nguồn với lesson đích. Các ngưỡng hiện hành chưa được
thay thế im lặng: chúng được đánh dấu là historical/source rule để tránh biến
giáo trình cũ thành tư vấn pháp lý hiện tại.

Pass này xác nhận coverage của nội dung học và provenance, không xác nhận luật
2026. `raw_md/sach1.md` không bị sửa.

## Owner và ranh giới

| Phạm vi | Owner | Vai trò |
|---|---|---|
| Book 1 theo section | [`book1/00-book1-index.md`](./book1/00-book1-index.md) và các file `01`–`13` | bản học canonical theo mạch giáo trình |
| Ôn tập/source trace | [`book1/90-review-and-source-trace.md`](./book1/90-review-and-source-trace.md) | review và provenance, không thay lesson |
| Source map | [`BOOK1_SOURCE_MAP.md`](./BOOK1_SOURCE_MAP.md) | section/trang/provenance |
| Investing chuyên sâu | `investing/` | owner canonical; Book 1 cross-link thay vì duplicate |
| Authority | `raw_md/sach1.md` và ảnh `raw/sach1/` | source/provenance |

## Source inventory

### Chương 1 — 금융시장과 증권시장

`금융시장` và phân loại trực tiếp/gián tiếp, ngắn hạn/vốn, các loại tổ chức tài
chính; `증권` và `금융투자상품`, 투자성, chứng khoán/phái sinh, bảng tỷ lệ tổn
thất; các nhóm chứng khoán, cổ phiếu, trái phiếu và công cụ lai; nghĩa rộng/hẹp
của `증권시장`; phát hành/lưu thông, chức năng kinh tế, issuer/investor/
underwriter, 공모/사모, trực tiếp/gián tiếp, 총액인수/잔액인수/모집주선; cơ quan
quản lý/vận hành, sáu loại `금융투자업`, 인가/등록, 업무단위 và vốn tối thiểu;
IPO, tăng vốn, niêm yết và công thức; lệnh, khớp lệnh, settlement, disclosure,
KOSDAQ/KONEX/K-OTC/NXT; futures/options/ELW và metrics; thuế; M&A, LBO, chào mua,
báo cáo sở hữu, treasury stock, proxy và phân loại thương vụ.

### Chương 2 — 집합투자

Định nghĩa `집합투자` và `집합투자기구`; cấu trúc pháp lý, chủ thể, public/private,
NAV/기준가격, chi phí, kỳ hạn, 가입/환매/연기, open/closed; phân loại quỹ theo
tài sản, cấu trúc, chiến lược, khu vực và quỹ đặc thù; REIT, special assets,
derivative funds, fund-of-funds, master-feeder, multiple class, umbrella, wrap,
ETF, infrastructure, PE, hedge; suitability/risk profile, prospectus, asset
report, chọn quỹ, return/risk/benchmark/beta/Sharpe, tái cân bằng và thuế.

## Coverage matrix

`FULL` chỉ dùng khi người học có thể hiểu semantic unit mà không cần quay lại
source. Nhắc tên thuật ngữ hoặc một bullet không được tính là `FULL`.

| Source | Semantic unit | Type | Current target | Status | Action |
|---|---|---|---|---|---|
| Ch1 §1 p13–16 | 정의/chức năng `금융시장` | definition/mechanism | `01` §§1,6–8 | FULL | keep |
| Ch1 §1 p14–16 | `직접금융` vs `간접금융` | comparison | `01` §§2,7 | FULL | keep |
| Ch1 §1 p14–16 | `단기금융시장` vs `자본시장` | classification | `01` §2 | FULL | marker thời hạn và boundary |
| Ch1 §1 p16–18 | bảng phân loại tổ chức tài chính | table/classification | `01` §4, §10 | FULL | bảng nhóm và ví dụ |
| Ch1 §2 p19–20 | nghĩa rộng/hẹp của `증권시장` | definition | `03` §1, §8 | FULL | điều kiện tổ chức/thời gian/địa điểm |
| Ch1 §2 p19–20 | phát hành vs lưu thông | mechanism | `01` §5; `03` §§2,5 | FULL | cross-link |
| Ch1 §2 p19–20 | 5 chức năng kinh tế | mechanism | `03` §3 | FULL | keep |
| Ch1 §2 p37–39 | `자본집중`, `최초 소유분산`, `경제조정` | mechanism | `03` §4, §7 | FULL | map từng chức năng vào flow |
| Ch1 §2 p40–44 | issuer/investor/underwriter, 간사단/인수단/청약단 | roles/process | `03` §4.1–4.2 | FULL | thêm ví dụ trách nhiệm |
| Ch1 §2 p41–43 | 공모/사모 và ngưỡng source | rule/comparison | `03` §4.3 | FULL | logic và snapshot threshold |
| Ch1 §2 p42–44 | 총액인수/잔액인수/모집주선 | process/risk allocation | `03` §4.4 | FULL | worked example |
| Ch1 §2 p45–47 | sơ đồ KRX–broker–KSD–investor | diagram | `03` §5; `04` §§2,6 | FULL | redraw flow |
| Ch1 §2 p21–23 | `금융투자상품`, 투자성 và ngoại lệ | legal definition | `02` §§1,7 | FULL | điều kiện/exception |
| Ch1 §2 p22–23 | bảng tỷ lệ tổn thất và sản phẩm | table/classification | `02` §2 | FULL | giữ bảng và giải thích |
| Ch1 §2 p23–25 | `증권`, `투자계약증권`, `파생결합증권` | legal definition | `02` §§2–3,7–8 | FULL | taxonomy/điều kiện |
| Ch1 §2 p25 | phân nhỏ vốn, marketability, risk-return | mechanism | `02` §4 | FULL | keep |
| Ch1 §2 p26–30 | các loại cổ phiếu và ưu đãi | classification/rights | `02` §5 | FULL | quyền tham gia/tích lũy |
| Ch1 §2 p30–34 | các loại trái phiếu | classification/cash flow | `02` §6 | FULL | quyền/điều kiện từng loại |
| Ch1 §3 p34–44 | cấu trúc thị trường và issuance | process/mechanism | `03` §§2–4 | FULL | keep |
| Ch1 §4 p47–55 | cơ quan KOFIA/KRX/KSD/Koscom | institution/roles | `04` §§1–2 | FULL | nhiệm vụ theo source |
| Ch1 §4 p54–56 | 6 loại `금융투자업` | legal classification | `04` §§3,11 | FULL | own/other account, advice/discretion |
| Ch1 §4 p56–59 | 인가 vs 등록, investor/product risk | legal mechanism | `04` §§4,11 | FULL | decision tree |
| Ch1 §4 p57–59 | 업무단위, product/investor unit, vốn tối thiểu | table/threshold | `04` §11 | FULL | bảng snapshot |
| Ch1 §4 p59–61 | 지급결제, 겸영, 부수업무 | legal process | `04` §§5,12 | FULL | điều kiện và 7-day notice |
| Ch1 §5 p61–66 | IPO purpose và 신주모집/구주매출/hybrid | definition/process | `05` §§1–3,9 | FULL | dòng tiền và tỷ lệ source |
| Ch1 §5 p63–66 | mệnh giá/thị giá và method | classification/formula | `05` §§5,10 | FULL | công thức và biến |
| Ch1 §5 p67–74 | 유상/무상/포괄/병행 증자 | classification/legal | `05` §5 | FULL | quyền mua và hệ quả |
| Ch1 §5 p64–90 | công thức phát hành và listing requirements | formula/process | `05` §§6–14 | FULL | SOURCE_AMBIGUITY: công thức 1차 phát hành/OCR và ngưỡng lịch sử được ghi rõ, không dùng như current rule |
| Ch1 §6 p90–99 | phương thức giao dịch, ưu tiên, single/multiple price | mechanism/rule | `06` §§2–3 | FULL | verify source terms |
| Ch1 §6 p96–100 | giờ giao dịch, giới hạn giá, settlement | table/rule | `06` §§4–5,12 | FULL | bảng snapshot |
| Ch1 §6 p98–100 | 자기주식 trading limits | legal rule | `06` §15 | FULL | owner và giới hạn riêng |
| Ch1 §6 p101–105 | 관리종목, 상장폐지, 정리매매, short-term overheating | legal process | `06` §§7,11,16 | FULL | flow + criteria table |
| Ch1 §6 p106–115 | order types, IOC/FOK, off-hours, Sidecar | mechanism/rule | `06` §§6–7 | FULL | condition table |
| Ch1 §6 p116–121 | disclosure requirements | legal mechanism | `06` §9 | FULL | requirements and limits |
| Ch1 §6 p122–163 | KOSDAQ/KONEX/K-OTC/NXT | market rules | `06` §§10–17 | FULL | tiêu chí venue, giao dịch và giới hạn lịch sử đã có; current rule vẫn phải tra riêng |
| Ch1 §7 p164–183 | futures/options/ELW/stock derivatives | instrument/formula | `07` §§1–9 | FULL | formulas, variables, worked examples |
| Ch1 §8 p184–198 | dividend/interest/transaction/capital-increase tax | tax rule | `08` §§1–12 | FULL | base, timing, withholding, exceptions |
| Ch1 §9 p198–205 | M&A types, payment, combination | classification | `09` §§1–2,5–6,9 | FULL | full source taxonomy |
| Ch1 §9 p199–205 | 공개매수/reporting/treasury/proxy | legal process | `09` §§3,10 | FULL | threshold/deadline snapshot explicitly labelled |
| Ch1 review p211–232 | chapter 1 true/false and MCQ knowledge | exercise mapping | `90` | FULL | range-to-lesson mapping |
| Ch2 §1 p234–242 | 집합투자 definition and boundaries | legal definition | `10` §§1,9 | FULL | statutory conditions |
| Ch2 §2 p242–248 | legal forms and participants | legal structure | `11` §§1–2 | FULL | forms/duties và separation of roles |
| Ch2 §2 p248–250 | NAV/base price/unit math | formula/example | `11` §5 | FULL | calculation and unit logic |
| Ch2 §2 p249–250 | fees, TER, performance fee | cost/table | `11` §§6–7,9 | FULL | TER/class table |
| Ch2 §2 p250–253 | maturity, suitability, adequacy, explanation, unfair solicitation | legal process | `11` §§7–8 | FULL | decision flow |
| Ch2 §2 p255–262 | pricing timing, 가입/환매/연기, open/closed | rule/table/process | `11` §§4,8,10 | FULL | timing tables and exceptions |
| Ch2 §3 p263–293 | target-asset classification, REIT, special/mixed/derivative | classification/diagram | `12` §§1–9,14–15 | FULL | percentages and flows |
| Ch2 §3 p294–298 | fund-of-funds/master-feeder/class/umbrella/wrap | structure/comparison | `12` §10,14 | FULL | limits, layers and cost effects |
| Ch2 §3 p299–313 | active/passive/ETF/region/infrastructure/PE/hedge | strategy/classification | `12` §§11–13 | FULL | source distinctions |
| Ch2 §4 p314–319 | risk profile, time horizon, 5 levels, allocation | process/table | `13` §§1–2,8 | FULL | profile matrix |
| Ch2 §4 p320–322 | prospectus, simplified prospectus, asset report | document/process | `13` §§3,11 | FULL | source field checklist |
| Ch2 §4 p323–326 | fund selection/category/return/risk | process/formula | `13` §4 | FULL | apple-to-apple and category return |
| Ch2 §4 p326–327 | standard deviation, beta, benchmark excess | metric/formula | `13` §§4–5,9 | FULL | variables and ambiguity note |
| Ch2 §4 p333–334 | fund taxation | tax rule | `13` §§0,6 | FULL | SOURCE STATE/CURRENT STATE tách rõ; mức thuế textbook không được dùng thay luật 2026 |
| Ch2 review p341–351 | 30 questions, answer explanations, Sharpe formula | exercise/formula | `90`, `13` | FULL | range mapping and worked example |

## Summary

| Status | Count |
|---|---:|
| FULL | 55 |
| PARTIAL | 0 |
| MISSING | 0 |
| N/A_NON_LEARNING_CONTENT | 0 in matrix |

Matrix total: **55 semantic units**. `PARTIAL = 0`, `MISSING = 0`. Các giới hạn
không thể khẳng định như current 2026 được ghi trong `SOURCE_AMBIGUITY` và
`Time-sensitive items`, nhưng knowledge-bearing content của source đã có đích
giải thích trong learning docs.

## Tables, figures and formulas

| Object group | Current handling | Result |
|---|---|---|
| Hình 1-1 financial-market classification | prose/tree in `01` | FULL |
| Table I-1 institution classification | source table in `01` §10 | FULL |
| Table 1-2 loss ratio/product classification | tree/table in `02` | FULL |
| bond/stock classification tables | prose/bullets in `02` | FULL |
| Hình 1-2 secondary-market structure | flow in `03`/`04` | FULL |
| Tables I-3/I-4 authorization/concurrent business | snapshot tables in `04` §§11–12 | FULL |
| IPO/listing/increase-capital tables/formulas | formulas/checklist in `05` §§9–14 | FULL — SOURCE_AMBIGUITY/OCR and historical thresholds explicitly flagged |
| Table I-7 trading hours/limits/circuit breakers | snapshot table in `06` §12 | FULL |
| management/listing/KOSDAQ/K-OTC/NXT tables | market comparison/checklists in `06` §§7,13–18 | FULL — historical criteria and venue relationships reconstructed |
| ELW/futures/options metrics | formulas/payoff/hedge table in `07` §§7–9 | FULL |
| NAV/pricing/redemption timing tables | timing/fee/class tables in `11` §§9–10 | FULL |
| TER/class/fund classification tables | tables in `11` §§9–9.1 and `12` §14 | FULL |
| REIT/special-assets flow diagrams | flow and thresholds in `12` §§7–9,14–15 | FULL |
| risk-profile/prospectus/asset-report tables | profile/metric/evidence tables in `13` §§8–15 | FULL |
| Sharpe formula and source explanations | worked formula in `13` §9 and `90` | FULL |

## Time-sensitive items

Until checked against FSC/FSS/KRX/KSD/NTS/Korean law or another official source
with a date, the following remain `Historical/source rule`: institution mandates
and composition; capital requirements; IPO/listing thresholds; trading hours,
price limits, circuit breakers, Sidecar, settlement and NXT; KOSDAQ/KONEX/K-OTC
eligibility and benefits; dividend/transaction/fund tax; fund cutoffs, fees and
redemption timing. Current law must be added as a separate `Current rule / 2026
update`, never silently replace textbook content.

## SOURCE_AMBIGUITY register

| Marker | Ambiguity | Handling |
|---|---|---|
| Page 3 | Vietnamese editorial prose already embedded in raw Markdown | treat as existing annotation, not Korean source knowledge |
| Pages 7–10 | OCR errors: `제1자`, `금융시작`, `증권시작`, `유통시자`, broken tables/order | verify against page images before exact extraction |
| Pages 62–65 | OCR marker/page-number jump around IPO/trading | map by printed page and image |
| Pages 73–81 | split historical listing/delisting tables | reconstruct only with image evidence |
| Pages 108–118 | chapter 2 paragraphs/timing tables wrap across pages | join by printed page before rewriting |
| Pages 151–155 | summary material interleaves with prior source sections | use as review evidence, not a second owner |
| Pages 162–166 | answer keys/formula subscripts are OCR-fragile | verify answer mapping from source images |

## Reverse-audit sau khi rebuild

1. Mỗi section 01–13 có checkpoint `Kiểm tra hiểu`; section 90 có checkpoint
   mapping bài tập và đường truy nguyên.
2. Các bảng/công thức chính đã có bản tái dựng hoặc ghi chú OCR/historical:
   nghiệp vụ và vốn, IPO/quyền mua, trading–settlement, cổ phiếu quỹ,
   futures/options/ELW, thuế, M&A, NAV/pricing, phí/quỹ và risk metrics.
3. Reverse audit đã nối source → lesson → câu hỏi ôn; hiện không còn hàng
   `PARTIAL` hoặc `MISSING`. Những điểm còn nhãn `SOURCE_AMBIGUITY` chỉ là
   giới hạn của OCR hoặc snapshot lịch sử, không phải khoảng trống nội dung.
4. Kiểm tra kỹ thuật cuối: `git diff --check`, link nội bộ, raw source bất biến và
   không có marker xung đột.

**Acceptance: PASS CÓ ĐIỀU KIỆN — nội dung học và coverage đạt; current-law
verification vẫn là bước riêng nếu cần dùng cho giao dịch thực tế.**
