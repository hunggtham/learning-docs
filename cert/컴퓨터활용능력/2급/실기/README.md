# 컴퓨터활용능력 2급 실기 — Mục lục & Lộ trình thực hành Excel

Phần thi thực hành (실기) là môn **스프레드시트 실무 (Thực hành bảng tính Excel)** với thời gian làm bài **40 phút**. Thang điểm tối đa là **100 điểm**, điểm đỗ yêu cầu đạt từ **70 điểm trở lên**. Bài thi được chấm điểm tự động bằng phần mềm, trong đó nhiều nội dung áp dụng quy tắc chấm nhị phân (chỉ có trọn vẹn điểm hoặc 0 điểm).

Tài liệu này được sắp xếp theo cấu trúc đề thi thực tế và cẩm nang thao tác chuẩn xác, giúp người học vừa nắm vững bản chất kỹ thuật vừa tuyệt đối tránh các lỗi thao tác dẫn đến bị trừ điểm.

## Lộ trình học tập (Learning Path)

### 01 — 기본작업 (Thao tác cơ bản & định dạng)
[01-기본작업.md](./01-기본작업.md)
- Nhập liệu và quy tắc chọn vùng dữ liệu (Range selection)
- Định dạng hiển thị ô và số liệu (Cell / Number format)
- Định dạng có điều kiện cơ bản (Conditional Formatting)
- Lọc tự động và Lọc nâng cao cơ bản (Auto / Advanced Filter)
- Kiểm soát hợp lệ dữ liệu (Data Validation) và Tách văn bản (Text to Columns)
- Nhập dữ liệu ngoài (External Data) và Dán đặc biệt (Paste Special)

### 02 — 계산작업 (Cơ chế tính toán & các hàm nền tảng)
[02-계산작업.md](./02-계산작업.md)
- Cơ chế tham chiếu tương đối, tuyệt đối và hỗn hợp khi sao chép công thức
- Nhóm hàm logic: IF, lồng ghép AND / OR
- Nhóm hàm thống kê có điều kiện: COUNTIF, SUMIF
- Nhóm hàm toán học và thống kê: ROUND, INT, MOD, AVERAGE, MAX, MIN
- Nhóm hàm xử lý chuỗi và ngày tháng: LEFT, RIGHT, MID, YEAR, MONTH, DAY
- Nhóm hàm tra cứu cơ bản: VLOOKUP, HLOOKUP
- Nhóm hàm cơ sở dữ liệu: DSUM, DAVERAGE, DCOUNT
- Kỹ thuật truy vết và khắc phục lỗi công thức (#N/A, #VALUE!, #REF!)

### 03 — 분석작업 (Phân tích dữ liệu & tổng hợp nghiệp vụ)
[03-분석작업.md](./03-분석작업.md)
- Sắp xếp dữ liệu đơn cấp và đa cấp (Sort)
- Tính tổng con theo nhóm (Subtotal - 부분합)
- Hợp nhất dữ liệu từ nhiều bảng (Consolidate - 통합)
- Tìm giá trị mục tiêu (Goal Seek - 목표값 찾기)
- Bảng giả lập dữ liệu 1 biến và 2 biến (Data Table - 데이터 표)
- Quản lý kịch bản phân tích (Scenario - 시나리오)
- Báo cáo tổng hợp động (PivotTable & PivotChart)

### 04 — 기타작업 (Biểu đồ & Tự động hóa)
[04-기타작업.md](./04-기타작업.md)
- Xác định đúng vùng nguồn dữ liệu, chuỗi dữ liệu (Series) và trục danh mục (Category)
- Hiệu chỉnh các thành phần biểu đồ: Tiêu đề, nhãn số liệu, đường lưới, định dạng trục
- Quy trình ghi nhận Macro (Macro recording) và nguyên tắc chọn ô trống trước khi ghi
- Chạy Macro và gán macro vào nút bấm (Form Control Button) hoặc hình vẽ (Shape)

### 05 — 계산작업 공식 함수 인벤토리 및 중첩 패턴 (Chuyên sâu tính toán 40 điểm)
[05-함수-인벤토리-및-공식-패턴.md](./05-함수-인벤토리-및-공식-패턴.md)
- Toàn bộ danh mục 7 nhóm hàm chính thức theo tiêu chuẩn 2024–2026 (Tra cứu, Chuỗi, Ngày giờ, Logic, Toán học, Thống kê, Cơ sở dữ liệu)
- 6 mẫu công thức lồng ghép kinh điển trong đề thi (`INDEX+MATCH`, `VLOOKUP+LEFT`, `CHOOSE+RANK.EQ`, `IFERROR+VLOOKUP/INDEX`, `SUMIFS`, `TEXT+REPT`)
- Kỹ thuật hoàn thành trọn vẹn 40 điểm tính toán và quy trình đối soát công thức trong 15 giây

### 06 — 분석·기타작업 세부수행 및 감점방지 매뉴얼 (Chuyên sâu phân tích & bổ trợ 40 điểm)
[06-분석-기타작업-세부수행-및-감점방지.md](./06-분석-기타작업-세부수행-및-감점방지.md)
- Quy trình chống điểm 0 ở phần Subtotal: Bắt buộc sắp xếp trước, hủy chọn thay thế giá trị cũ khi chạy Subtotal lần hai
- Quy tắc giữ trọn 10 điểm Pivot Table: Vị trí ô bắt đầu, bố cục Outline/Tabular, định dạng số qua Value Field Settings
- Cơ chế gán ô công thức góc trái trên trong Data Table 2 biến
- Đặt tên ô trước khi lập báo cáo tóm tắt kịch bản (Scenario)
- Kỹ thuật ghi Macro bắt đầu từ ô trống và nhấn giữ phím `Alt` khi vẽ nút bấm
- 5 dạng bài hiệu chỉnh biểu đồ: Trục phụ kết hợp đường gập khúc, nhãn đơn lẻ, bước nhảy trục, liên kết tiêu đề với ô tính

### 07 — 기본작업 심화 — 서식·필터·외부데이터 (Chuyên sâu thao tác cơ bản 20 điểm)
[07-기본작업-심화-서식-필터-외부데이터.md](./07-기본작업-심화-서식-필터-외부데이터.md)
- Cấu trúc 4 vùng của mã định dạng tùy chỉnh (Custom Number Format), kỹ thuật rút gọn đơn vị nghìn và định dạng thứ ngày (`aaa`/`aaaa`)
- Phân biệt gộp ô (Merge & Center) và căn giữa qua vùng chọn (Center Across Selection)
- Quản lý tên ô (Name Manager với `Ctrl+F3`) và định dạng tự động co giãn kích thước chú thích (Comment Note)
- Công thức định dạng có điều kiện toàn dòng với tham chiếu hỗn hợp khóa cột (`=$C3>=80`)
- Phân biệt điều kiện trực tiếp (Direct Criteria) và điều kiện công thức logic (Formula Criteria) trong Lọc nâng cao

### 90 — 실전 모의고사 (Quy trình làm bài & giải đề)
[90-실전-모의고사.md](./90-실전-모의고사.md)
- Quy trình phân bổ thời gian 40 phút và thứ tự giải bài tối ưu
- Kỹ năng phân tích 4 thành phần trong câu hỏi đề thi (Target → Operation → Condition → Output)
- Xử lý tình huống khi gặp sự cố công thức hoặc nhầm lẫn thao tác
- Trình tự kiểm tra soát lỗi trước khi kết thúc bài thi

## Trọng số điểm và mối quan hệ phụ thuộc

```
[Phần cơ bản 20 điểm] Độ chính xác vùng chọn & định dạng (01, 07)
  └──> [Phần tính toán 40 điểm] Khóa địa chỉ tham chiếu & cú pháp lồng hàm (02, 05)
        └──> [Phần phân tích 20 điểm] Trình tự thao tác & chống điểm 0 (03, 06)
              └──> [Phần bổ trợ 20 điểm] Biểu đồ & tự động hóa Macro (04, 06)
                    └──> [Tích hợp] Luyện tập thực chiến 40 phút (90)
```
