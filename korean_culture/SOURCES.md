# Korean Culture — source ledger và currentness boundary

> **Owner:** `korean_culture/` cho nội dung văn hóa canonical; `korean_culture/kiip/SOURCES.md` giữ provenance riêng của syllabus/ôn thi KIIP.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| KOR-CULT-UNESCO-01 | UNESCO Intangible Cultural Heritage | trạng thái ghi danh và mô tả khung di sản phi vật thể Hàn Quốc | https://ich.unesco.org/en/state/republic-of-korea-KR?info=elements-on-the-lists | danh sách truy cập 2026-10-09 | Ghi danh UNESCO không đồng nghĩa toàn bộ thực hành hiện nay giống mô tả; phải tách registry, lịch sử và thực hành sống | văn hóa truyền thống/di sản |
| KOR-CULT-KHA-01 | Korea Heritage Agency (국가유산진흥원) | cơ quan/tổ chức hoạt động bảo tồn và truyền bá di sản | https://www.kh.or.kr/ | cổng được UNESCO xác nhận; kiểm tra 2026-10-09 | Không dùng cho claim về toàn bộ xã hội hoặc ý nghĩa đương đại nếu thiếu nghiên cứu cụ thể | chapter di sản và thực hành |
| KOR-CULT-KOSTAT-01 | Statistics Korea (KOSTAT) | số liệu dân số, hộ gia đình, xã hội và kinh tế Hàn Quốc | https://kostat.go.kr/eng/index.do | cổng truy cập 2026-10-09; mỗi bảng có kỳ riêng | Mọi số liệu phải ghi bảng, kỳ, định nghĩa và ngày tải; không dùng headline thay cho bảng gốc | chapter xã hội/nhân khẩu |
| KOR-CULT-MOJ-01 | Ministry of Justice / Immigration Service | chương trình và chính sách hội nhập khi claim thuộc KIIP/immigration | https://www.moj.go.kr/moj/369/subview.do | cổng được ghi trong KIIP ledger; refresh mỗi kỳ thông báo | Không suy ra quy tắc thi, visa hoặc quyền cư trú từ chapter văn hóa; xem ledger KIIP/korea law | `korean_culture/kiip/` |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| KOR-CULT-GENERAL-01 | `NEEDS_SOURCE` | Không viết “người Hàn luôn…”/“văn hóa Hàn là…” như quy luật phổ quát; cần survey, ethnography hoặc source lịch sử cụ thể và ghi population/context. | Owner chapter tương ứng |
| KOR-CULT-STAT-01 | `NEEDS_SOURCE` | Claim về thái độ, hành vi, thế hệ, vùng hoặc xu hướng hiện tại phải có dataset/survey với năm và mẫu; không dùng giai thoại. | Owner chapter xã hội |
| KOR-CULT-TRANSLATION-01 | `REVIEW_REQUIRED` | Dịch thuật ngữ văn hóa phải giữ nguyên sắc thái và phạm vi, không dùng bản dịch tiện tay như định nghĩa chính thức. | Owner prose + Korean reviewer |

## Quy trình refresh

1. Ghi source ID và context ngay tại chapter khi claim không phải kiến thức nền.
2. Với statistic/policy, ghi `as-of`, kỳ dữ liệu hoặc ngày hiệu lực.
3. Tách mô tả lịch sử, registry chính thức, thực hành đương đại và diễn giải của tác giả; không trộn thành một fact duy nhất.
