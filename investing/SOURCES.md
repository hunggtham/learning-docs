# Investing — source ledger và currentness boundary

> **Owner:** `investing/` (nội dung học); người cập nhật phải ghi ngày kiểm tra trong ledger này.
> Đây là sổ provenance cho claim và dữ liệu, không phải khuyến nghị mua bán.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Nguyên tắc dùng nguồn

- Nguyên lý nền (risk, return, diversification, valuation mechanics) có thể giữ lâu hơn, nhưng ví dụ số liệu vẫn phải có kỳ tham chiếu.
- Quy định, thuế, giới hạn sở hữu, sản phẩm, chỉ số, phí, lãi suất, tỷ giá và dữ liệu thị trường là **time-sensitive**: phải trỏ tới nguồn của đúng thị trường và ghi `as-of`/ngày hiệu lực.
- Nguồn Hoa Kỳ không tự động chứng minh quy định Hàn Quốc hay Việt Nam. Khi lesson nói về hai thị trường này mà chưa có hồ sơ chính thức cụ thể, dùng `NEEDS_SOURCE` và không diễn đạt như quy tắc hiện hành.

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| INV-SEC-01 | U.S. Securities and Exchange Commission — Investor.gov | khái niệm đầu tư cơ bản, rủi ro, disclosure và EDGAR trong phạm vi Mỹ | https://www.investor.gov/introduction-investing | cổng truy cập kiểm tra 2026-10-09; trang có thể cập nhật | Không suy rộng sang luật/chế độ bảo vệ nhà đầu tư ngoài Mỹ; claim sản phẩm/quy định phải kiểm tra lại | `investing/01_foundations/`, `investing/03_company_analysis/` |
| INV-SEC-02 | SEC — Investor.gov | trách nhiệm và mục tiêu của cơ quan quản lý chứng khoán Mỹ | https://www.investor.gov/introduction-investing/investing-basics/role-sec | kiểm tra 2026-10-09 | Chỉ dùng để giải thích bối cảnh SEC; không dùng làm nguồn cho KRX/VN | `investing/04_economics/`, các lesson có phạm vi US |
| INV-FSC-01 | Financial Services Commission (Republic of Korea) | cơ cấu/mandate và thông báo chính sách tài chính Hàn Quốc | https://www.fsc.go.kr/eng/co000000 | kiểm tra 2026-10-09; thông báo thay đổi theo ngày | Claim policy, consumer protection, licensing và market stability phải dùng notice/luật cụ thể, không chỉ trang giới thiệu | `investing/06_markets_korea_vietnam/` |
| INV-KRX-01 | Korea Exchange (KRX) | cấu trúc thị trường, công cụ/chỉ số và dữ liệu KRX | https://global.krx.co.kr/ | kiểm tra 2026-10-09 | Giá, volume, index và trạng thái niêm yết là snapshot; phải lưu ngày/giờ và endpoint hoặc file dữ liệu | `investing/02_asset_classes/`, `investing/06_markets_korea_vietnam/` |
| INV-KRX-02 | KRX Data Marketplace | dữ liệu thị trường KRX | https://data.krx.co.kr/contents/MDC/MAIN/main.jspx | kiểm tra 2026-10-09 | Không coi số liệu live là facts bất biến; lesson phải ghi kỳ quan sát và timezone | `investing/06_markets_korea_vietnam/`, research workflow |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| INV-LOCAL-REG-01 | `NEEDS_SOURCE` | Chưa dùng các con số về thuế, room ngoại, phí giao dịch, giờ giao dịch hoặc điều kiện sản phẩm Hàn Quốc/Việt Nam như quy định hiện hành nếu chưa có luật/notice đúng jurisdiction và ngày hiệu lực. | Owner `investing/06_markets_korea_vietnam/`; bổ sung FSC/FSS/법령 hoặc cơ quan Việt Nam tương ứng |
| INV-MARKET-SNAPSHOT-01 | `NEEDS_SOURCE` | Mọi giá, lợi suất, tỷ giá, market cap và ranking phải là dữ liệu có `as-of`, không viết như facts hiện tại nếu không có snapshot. | Owner của từng research note; xác minh ngay trước khi dùng |
| INV-ADVICE-01 | `REVIEW_REQUIRED` | Nội dung giáo dục không phải tư vấn cá nhân; không suy ra phân bổ vốn, mục tiêu lợi nhuận hoặc suitability từ nguồn giáo khoa. | Owner `investing/`; review thủ công trước publication |

## Quy trình refresh

1. Trước khi phát hành lesson có policy/data, ghi source ID, jurisdiction, ngày hiệu lực/kỳ dữ liệu và đường dẫn cụ thể.
2. Khi source đổi hoặc URL hỏng, giữ snapshot cũ trong lịch sử, cập nhật ledger và đánh dấu các claim bị ảnh hưởng.
3. Audit cấu trúc/link không chứng minh số liệu còn đúng hoặc thesis còn phù hợp; cần review nội dung riêng.
