# Source map — 증권투자기초 sách 1

Nguồn chính: `증권투자기초/raw_md/sach1.md`.

Các số trang dưới đây là số trang in được nhận diện trong mục lục; `Page N` là
marker OCR tương ứng và cần kiểm tra lại khi OCR làm lệch số trang. Source map
này dùng để kiểm tra độ phủ, không phải nội dung học thay thế.

## Bản đồ cấp sách

| Khối | Phạm vi trong nguồn | Nội dung | Trạng thái |
|---|---:|---|---|
| 제1장 금융시장과 증권시장 | trang in 13–205 (+ tổng kết 206–210, bài tập 211–231) | thị trường tài chính/chứng khoán, công cụ, cấu trúc thị trường, tổ chức, IPO–listing, giao dịch, phái sinh chỉ số, thuế, M&A | đã viết và audit coverage/prose; số liệu pháp lý là snapshot |
| 제2장 집합투자 | trang in 234–351 | khái niệm đầu tư tập thể, cấu trúc/quy mô quỹ, loại quỹ, quản lý và thuế | đã viết và audit coverage/prose; số liệu pháp lý/thuế là snapshot |

## 제1장 — source map

| Section nguồn | Trang in theo mục lục | Vai trò trong mạch học | Output |
|---|---:|---|---|
| 제1절 금융시장과 증권시장 | 13–20 | đặt hệ thống: dòng tiền, trung gian, thị trường sơ cấp/thứ cấp | [đã viết](./book1/01-financial-markets-and-securities.md) |
| 제2절 증권의 종류와 의의 | 20–34 | chuyển từ hệ thống sang quyền tài chính và các loại chứng khoán | [đã viết](./book1/02-securities-types-and-meaning.md) |
| 제3절 증권시장의 의의와 구조 | 34–47 | làm rõ cấu trúc và cơ chế vận hành của thị trường chứng khoán | [đã viết](./book1/03-securities-market-structure.md) |
| 제4절 증권 관련 기관 | 47–61 | xác định các tổ chức giám sát, vận hành và trung gian | [đã viết](./book1/04-securities-institutions.md) |
| 제5절 기업공개 및 상장제도 | 61–90 | nối huy động vốn doanh nghiệp với IPO, tăng vốn và niêm yết | [đã viết](./book1/05-ipo-and-listing.md) |
| 제6절 주식유통시장제도 | 90–163 | đi từ lệnh/giao dịch/thanh toán đến công bố thông tin và KOSDAQ | [đã viết](./book1/06-stock-market-trading.md) |
| 제7절 주가지수선물·옵션시장 | 164–184 | áp dụng cơ chế phái sinh vào chỉ số và cổ phiếu | [đã viết](./book1/07-index-futures-options.md) |
| 제8절 증권 관련 세제 | 184–197 | đặt lợi suất và giao dịch trong lớp thuế liên quan | [đã viết](./book1/08-securities-tax.md) |
| 제9절 기업인수합병(M&A)제도 | 198–205 | khép chương bằng thay đổi quyền kiểm soát và tái cấu trúc doanh nghiệp | [đã viết](./book1/09-ma.md) |

## 제2장 — source map

| Section nguồn | Trang in theo mục lục | Vai trò trong mạch học | Output |
|---|---:|---|---|
| 제1절 집합투자의 개념 | 236–242 | vì sao gom vốn và ủy thác quản lý tạo thành một cấu trúc riêng | [đã viết](./book1/10-collective-investment-concepts.md) |
| 제2절 펀드의 구조 | 242–263 | ai góp vốn, ai quản lý, ai lưu ký và tiền đi qua hệ thống thế nào | [đã viết ở mức cơ chế](./book1/11-fund-structure.md) |
| 제3절 펀드의 종류 | 263–314 | phân loại theo tài sản, cấu trúc, chiến lược, khu vực và dạng đặc thù | [đã viết ở mức cơ chế](./book1/12-fund-types.md) |
| 제4절 펀드 관리 | 314–351 | quy trình đầu tư, đánh giá phù hợp và thuế/quản lý | [đã viết ở mức cơ chế](./book1/13-fund-management.md) |

## Checkpoint hiện tại

- Đã đọc mục lục và phần mở đầu của `sach1.md`.
- Đã đối chiếu mẫu các trang OCR 13–20 với ảnh `raw/sach1/013.jpg`, `014.jpg`,
  `016.jpg`, `018.jpg`–`020.jpg`; đồng thời đối chiếu các điểm chính của section 2
  với ảnh `021.jpg`–`026.jpg`, `030.jpg` và `034.jpg`, và section 3 với ảnh
  `035.jpg`, `036.jpg`, `038.jpg`, `040.jpg`, `042.jpg`, `044.jpg`–`047.jpg`, và
  section 4 với ảnh `048.jpg`, `049.jpg`, `051.jpg`, `054.jpg`, `055.jpg`,
  `058.jpg`, `060.jpg`–`061.jpg`.
- Section 5 đã đối chiếu ảnh `raw/sach1/062.jpg`–`087.jpg` cho các mạch IPO,
  tăng vốn, niêm yết và bước đầu của tạm dừng/hủy niêm yết. OCR trong
  `raw_md/sach1.md` bị lệch từ marker Page 65 (nội dung OCR nhảy sang trang in
  93), nên ảnh được dùng để xác định thứ tự; các ngưỡng pháp lý vẫn chỉ là
  snapshot và chưa được xác minh hiện hành.
- Đã đối chiếu ảnh `raw/sach1/091.jpg`–`099.jpg` cho phần đầu của section 6:
  thị trường lưu thông, loại giao dịch, nguyên tắc khớp lệnh, giới hạn giá,
  ngắt mạch và thanh toán. Các mốc giờ, chu kỳ thanh toán và tỷ lệ trong ảnh
  được giữ như bối cảnh lịch sử, không được trình bày như quy định hiện hành.
- Đã đối chiếu tiếp ảnh `raw/sach1/102.jpg`–`134.jpg` cho lệnh giao dịch,
  quản lý cổ phiếu, cơ chế giảm tốc, giám sát thị trường, công bố thông tin và
  phần mở đầu KOSDAQ. Các tiêu chuẩn, lợi ích thuế, đơn vị yết giá và lịch xử
  lý hồ sơ trong các bảng này vẫn là số liệu theo thời kỳ.
- Đã đối chiếu ảnh `raw/sach1/135.jpg`–`164.jpg` cho phần còn lại của KOSDAQ,
  cơ chế quản lý/rút niêm yết, KONEX, NXT và K-OTC. Các mốc vận hành, ngưỡng,
  ưu đãi và điều kiện tham gia được giữ ở dạng logic/khái niệm vì chúng là
  snapshot theo thời kỳ.
- Đã đối chiếu ảnh `raw/sach1/165.jpg`–`184.jpg` cho section 7: KOSPI200,
  hợp đồng tương lai và spread, quyền chọn chỉ số, ELW/chứng quyền và hợp đồng
  tương lai/quyền chọn cổ phiếu. Công thức được giữ để học cơ chế; giờ giao dịch,
  bước giá, hệ số và ngưỡng đều được đánh dấu là snapshot.
- Đã đối chiếu ảnh `raw/sach1/185.jpg`–`198.jpg` cho section 8 về cổ tức,
  cổ tức được coi như phát sinh, thuế giao dịch, thời điểm thu nhập và tăng vốn;
  các tỷ lệ thuế/ngoại lệ chỉ được giữ như bối cảnh của ấn bản nguồn.
- Đã đối chiếu ảnh `raw/sach1/199.jpg`–`206.jpg` cho section 9 về định nghĩa,
  lợi ích/rủi ro, loại hình M&A, chào mua công khai, báo cáo sở hữu lớn, cổ phiếu
  quỹ và ủy quyền biểu quyết. Đã đối chiếu thêm `207.jpg`–`211.jpg` cho sơ đồ
  tổng kết, bảng so sánh và tài liệu tham khảo; `212.jpg`–`232.jpg` là bài tập tự
  kiểm tra chương 1, được dùng để rà coverage khái niệm chứ không chép nguyên văn.
- Đã bắt đầu chương 2 bằng ảnh `raw/sach1/235.jpg`–`242.jpg` cho phần định hướng,
  khái niệm đầu tư tập thể, hình thức pháp lý và tài sản mục tiêu; tiếp tục đối
  chiếu `243.jpg`–`257.jpg` cho cấu trúc chủ thể, NAV, chi phí, kỳ hạn, suitability,
  pricing và phí phân phối; tiếp tục đối chiếu `258.jpg`–`282.jpg` cho mua lại,
  quỹ mở/đóng và các loại quỹ theo tài sản/phong cách; tiếp tục đối chiếu
  `283.jpg`–`314.jpg` cho quỹ bất động sản, REIT, tài sản đặc biệt, phái sinh,
  fund-of-funds, quỹ nhiều lớp, ETF, quỹ quốc tế, hạ tầng, private equity và
  hedge fund. Đã đối chiếu tiếp `315.jpg`–`334.jpg` cho khẩu vị rủi ro, danh mục,
  tài liệu quỹ, quy trình chọn, đo lợi nhuận/rủi ro, xếp hạng, tái cân bằng và
  thuế; ảnh `335.jpg`–`352.jpg` là phần tổng kết và bài tập tự kiểm tra. Không
  chép nguyên bộ câu hỏi vào bản học; chỉ giữ các điểm dễ nhầm và công thức cần
  nhớ.
- Đã giữ các lỗi/điểm cần xác minh về tên pháp lý hoặc số liệu hiện hành ngoài
  phạm vi bản học đầu tiên; chưa tự cập nhật luật/thị trường từ nguồn web.
- Không sửa `raw_md`.

## Audit độ phủ và tính toàn vẹn

### Trạng thái raw image sau cleanup

Các ảnh JPG đánh số trong `raw/sach1/001.jpg`–`354.jpg` đã được dọn khỏi
repository vì không còn là artifact cần phát hành. Các số trang/ảnh được nhắc
trong checkpoint bên trên chỉ là provenance của lần đối chiếu trước cleanup,
không phải link tới file ảnh còn tồn tại. Bản OCR và output học canonical vẫn là
nguồn đọc chính; không phục hồi ảnh chỉ vì source map còn ghi số trang.

| Hạng mục | Bằng chứng hiện tại | Kết quả |
|---|---|---|
| Phạm vi nguồn | mục lục `sach1.md` và ảnh 013–352 | bao phủ 제1장 và 제2장 của sách 1; ảnh bìa/phân cách không tính là nội dung |
| Section map | 9 section của 제1장 + 4 section của 제2장 | đủ 13 section, mỗi section có output và khoảng trang/ảnh |
| Phần tổng kết/bài tập | ảnh 207–232 và 335–352 | đã ghi vào source map; chỉ giữ ghi chú/điểm dễ nhầm, không chép nguyên bộ câu hỏi |
| Liên kết canonical | 13 liên kết output trong source map | đường dẫn tệp tồn tại trong worktree |
| Văn phong | rà các cụm boilerplate và câu phụ thuộc “theo sách” | đã giảm source-wrapper language; phần truy nguyên giữ provenance riêng |
| Tính nguyên vẹn nguồn | `git status --short -- raw_md raw` | không có thay đổi trên `raw_md` hoặc ảnh nguồn |
| Định dạng | `git diff --check` | đạt |

Các tỷ lệ, mốc giờ, điều kiện gia nhập, thuế và tên cơ quan trong bản học được
giữ như bối cảnh của ấn bản nguồn. Chúng không được coi là quy định hiện hành nếu
chưa tra cứu văn bản cập nhật riêng.
