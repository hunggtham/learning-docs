# 컴퓨터활용능력 (1급 & 2급) — Coverage Audit

> **Mục đích:** Đảm bảo toàn bộ phạm vi xuất đề (출제기준 2024–2026) của kỳ thi Quốc gia Tin học văn phòng KCCI (대한상공회의소) được giảng dạy đầy đủ và chuyên sâu, phân biệt rõ ràng giữa "tệp tài liệu tồn tại" và "nội dung bao phủ 100% syllabus".
> **Phiên bản chuẩn khảo thí:** 2024–2026 출제기준 / Windows 10 & Microsoft Office LTSC 2021 (giao diện tiếng Hàn).
> **Trạng thái quy ước:** FULL (Bao phủ 100%) / PARTIAL (Bao phủ một phần) / MISSING (Chưa có) / VERIFY_OFFICIAL (Theo dõi chuẩn mới).

---

## 1. Cấu trúc tổng thể kỳ thi Quốc gia

| Cấp độ | Phân loại | Môn thi | Trạng thái | Owner chính |
|---|---|---|:---:|---|
| **1급 (Cấp độ 1)** | **필기 (Lý thuyết)** | 1과목: 컴퓨터 일반 (Tin học & Hệ thống) | **FULL** | `1급/필기/01-컴퓨터-일반.md` |
| | | 2과목: 스프레드시트 일반 (Bảng tính Excel) | **FULL** | `1급/필기/02-스프레드시트-일반.md` |
| | | 3과목: 데이터베이스 일반 (CSDL quan hệ Access) | **FULL** | `1급/필기/03-데이터베이스-일반.md` |
| | | 문제풀이 전략 (Chiến lược 60p & chống 과락) | **FULL** | `1급/필기/90-필기-문제풀이-전략.md` |
| | **실기 (Thực hành)** | 과목 1: 스프레드시트 실무 (Excel nâng cao) | **FULL** | `1급/실기/01~05-스프레드시트-*.md` |
| | | 과목 2: 데이터베이스 실무 (Access CSDL) | **FULL** | `1급/실기/06~10-데이터베이스-*.md` |
| | | 실전 모의고사 및 오류 복구 전략 (90p kép) | **FULL** | `1급/실기/90-실전-모의고사-및-오류-복구-전략.md` |
| **2급 (Cấp độ 2)** | **필기 (Lý thuyết)** | 1과목: 컴퓨터 일반 + 2과목: 스프레드시트 일반 | **FULL** | `2급/필기/` (01, 02, 90) |
| | **실기 (Thực hành)** | 스프레드시트 실무 (Excel tiêu chuẩn 100đ) | **FULL** | `2급/실기/` (01~07, 90) |
| **Chung** | **Ranh giới phiên bản** | 2027–2029 출제기준 개편 대비 | **PARTIAL** | `EXAM_VERSION_NOTES.md` |

---

## 2. Chi tiết độ phủ 1급 (Cấp độ 1 — Chuyên gia)

### 2.1 1급 필기 (Lý thuyết trắc nghiệm 3 môn — 60 câu / 60 phút)

| Khu vực kiến thức KCCI | Nội dung bao phủ chi tiết | Trạng thái | Tài liệu phụ trách |
|---|---|:---:|---|
| **Kiến trúc phần cứng CPU** | ALU, CU, Registers (PC, IR, MAR, MBR, AC, PSW), Chu kỳ lệnh (Fetch, Decode, Execute, Interrupt), Pipelining, Superscalar, RISC vs CISC. | FULL | `1급/필기/01-컴퓨터-일반.md` |
| **Phân cấp bộ nhớ & Bộ nhớ ảo** | Cache L1/L2/L3, Ánh xạ cache (Direct, Associative, Set-Associative), Hit ratio, Paging vs Segmentation, Hiện tượng Thrashing & Working Set. | FULL | `1급/필기/01-컴퓨터-일반.md` |
| **Hệ thống Bus & Lưu trữ** | Data Bus, Address Bus, Control Bus, Mảng đĩa RAID 0 (Striping), RAID 1 (Mirroring), RAID 5 (Parity striping). | FULL | `1급/필기/01-컴퓨터-일반.md` |
| **Hệ điều hành Windows 10/11** | Cấu trúc Registry 5 nhánh chính (HKCR, HKCU, HKLM, HKU, HKCC), Event Viewer, Task Manager, Device Manager, Chế độ Safe Mode. | FULL | `1급/필기/01-컴퓨터-일반.md` |
| **Mạng & Giao thức truyền thông** | Mô hình OSI 7 tầng vs TCP/IP 4 tầng, Địa chỉ IPv4 (Phân lớp, Subnet Mask, Tính Subnet ID/Broadcast) và IPv6 (128-bit, Unicast/Multicast/Anycast), Các giao thức TCP, UDP, ARP, ICMP, DNS, DHCP. | FULL | `1급/필기/01-컴퓨터-일반.md` |
| **An toàn thông tin & Mật mã** | Mã hóa đối xứng (AES, DES, SEED) vs Bất đối xứng (RSA, ECC), Chữ ký số & Hạ tầng khóa công khai PKI, Tường lửa, IDS/IPS, Các dạng mã độc và tấn công (DoS/DDoS, Pharming, Phishing, Ransomware). | FULL | `1급/필기/01-컴퓨터-일반.md` |
| **Excel lý thuyết nâng cao** | Chuỗi định dạng số tùy chỉnh 4 phần (`양수;음수;0;텍스트`, ký hiệu `#`, `0`, `?`, `@`, `*`), Các mã lỗi Excel (`#DIV/0!`, `#N/A`, `#NAME?`, `#NUM!`, `#REF!`, `#VALUE!`, `#NULL!`). | FULL | `1급/필기/02-스프레드시트-일반.md` |
| **Công thức mảng & Hàm nâng cao** | Bản chất toán học ma trận và tổ hợp phím `{=...}`, Phép nhân AND và phép cộng OR mảng, Hàm tài chính (`PMT`, `PV`, `FV`, `RATE`, `NPER`), Hàm tra cứu ma trận (`INDEX`, `MATCH`, `OFFSET`). | FULL | `1급/필기/02-스프레드시트-일반.md` |
| **Phân tích What-If & Lập trình VBA** | Calculated Field vs Calculated Item trong Pivot Table, Solver (`해 찾기`), Goal Seek, Cú pháp VBA (Biến, Kiểu dữ liệu, If/Else, Select Case, For Next, Do While), Mô hình đối tượng DOM Excel. | FULL | `1급/필기/02-스프레드시트-일반.md` |
| **CSDL quan hệ RDBMS** | Quan hệ (Relation), Bản ghi (Tuple/Hàng), Trường (Attribute/Cột), Miền (Domain), Bản số (Cardinality) vs Bậc (Degree). Phân loại Siêu khóa, Khóa ứng viên, Khóa chính, Khóa ngoại. | FULL | `1급/필기/03-데이터베이스-일반.md` |
| **Toàn vẹn & Chuẩn hóa dữ liệu** | Toàn vẹn thực thể (개체 무결성), Toàn vẹn tham chiếu (참조 무결성), Đại số quan hệ (Chọn, Chiếu, Join, Chia), Các bất thường Anomaly (Chèn, Xóa, Cập nhật), Quy trình chuẩn hóa 1NF $\to$ 2NF $\to$ 3NF $\to$ BCNF. | FULL | `1급/필기/03-데이터베이스-일반.md` |
| **Ngôn ngữ SQL & Đối tượng Access** | Cú pháp SQL đầy đủ (DDL: `CREATE`/`ALTER`/`DROP`; DML: `SELECT`-`FROM`-`WHERE`-`GROUP BY`-`HAVING`-`ORDER BY`, `INSERT`, `UPDATE`, `DELETE`), Field Properties Access, Cấu trúc Form/Report, Hàm miền `DLookup`, DoCmd. | FULL | `1급/필기/03-데이터베이스-일반.md` |
| **Chiến lược giải đề 필기 1급** | Barem điểm đỗ và phòng tránh điểm liệt (과락 $\ge 8$ câu/môn, tổng $\ge 36$ câu), Sơ đồ phân bổ 60 phút thực chiến, 10 dạng bẫy trắc nghiệm kinh điển và kỹ thuật loại trừ logic. | FULL | `1급/필기/90-필기-문제풀이-전략.md` |

---

### 2.2 1급 실기 (Thực hành máy tính 2 môn — 90 phút = 45p Excel + 45p Access)

| Phần thi | Tên nghiệp vụ KCCI | Nội dung bao phủ chi tiết | Trọng số | Trạng thái | Tài liệu phụ trách |
|---|---|---|:---:|:---:|---|
| **Excel 1** | **기본작업** (Thao tác cơ bản) | • Lọc nâng cao (고급필터): Biểu thức logic công thức bắt đầu `=`, cố định cột `$A4`, kết hợp AND/OR/YEAR/AVERAGE.<br>• Định dạng có điều kiện (조건부 서식): Công thức định dạng toàn dòng, khóa cột tuyệt đối.<br>• Bố cục trang in & Bảo vệ sheet: Lặp lại dòng tiêu đề khi in, khóa ô và ẩn công thức. | 30 điểm | **FULL** | `1급/실기/01-스프레드시트-기본작업.md` |
| **Excel 2** | **계산작업** (배열수식) | 5 cấu trúc công thức mảng chuẩn KCCI: SUM(IF), SUM(*), COUNT(IF), AVERAGE(IF) (chống bẫy số 0), MAX/LARGE(IF), INDEX+MATCH mảng đa điều kiện, kết thúc bằng `Ctrl+Shift+Enter`. | 24 điểm | **FULL** | `1급/실기/02-스프레드시트-계산작업-배열수식.md` |
| **Excel 2** | **계산작업** (사용자정의함수) | Lập trình hàm VBA tự định nghĩa trong Standard Module (`Public Function fn...`), rẽ nhánh If/ElseIf, Select Case; Nhóm hàm tài chính PMT/FV/PV; Nhóm hàm tra cứu và thời gian. | 6 điểm | **FULL** | `1급/실기/03-스프레드시트-계산작업-사용자정의함수-및-고급함수.md` |
| **Excel 3** | **분석작업** (Pivot Table & Công cụ) | Quy trình chống điểm 0 của Pivot Table (nguồn dữ liệu ngoài `.accdb`, Grouping ngày/số, Calculated Field, định dạng số qua Value Field Settings); Bảng dữ liệu Data Table 2 biến, Scenario Manager, Consolidate, Subtotal. | 20 điểm | **FULL** | `1급/실기/04-스프레드시트-분석작업.md` |
| **Excel 4** | **기타작업** (Biểu đồ & VBA) | 5 dạng hiệu chỉnh biểu đồ chuẩn (Combo Chart trục phụ, chuỗi dữ liệu, nhãn, khoảng cách); Lập trình sự kiện UserForm VBA (Nạp form `.Show`, khởi tạo `.RowSource`, ghi dòng cuối `Cells(i, col)`, đóng `Unload Me`). | 20 điểm | **FULL** | `1급/실기/05-스프레드시트-기타작업-차트-및-프로시저.md` |
| **Access 1** | **DB구축** (Thiết kế bảng & Quan hệ) | Khóa chính đơn/kép, Field Properties (Field Size, Format, Input Mask 3 phần, Default Value, Validation Rule & Text, Required, Indexed); Thiết lập quan hệ 1-Nhiều với Toàn vẹn tham chiếu, Cascade Update/Delete; Lookup Field ComboBox. | 30 điểm | **FULL** | `1급/실기/06-데이터베이스-DB구축.md` |
| **Access 2** | **화면구현** (Giao diện Form) | Thuộc tính Form (RecordSource, Default View, ScrollBars, Modal, Popup); Thuộc tính Control (ControlSource, RowSource); Hàm miền tính toán (`DLookup`, `DSum`, `DAvg`, `DCount`); Nhúng Subform đồng bộ khóa liên kết. | 25 điểm | **FULL** | `1급/실기/07-데이터베이스-화면구현-폼.md` |
| **Access 3** | **조회출력** (Báo cáo Report) | Cấu trúc 5 Section Report, Gom nhóm & Sắp xếp, Thuộc tính Force New Page, Keep Together; Đánh số thứ tự liên tục Running Sum (Over Group vs Over All); Ẩn giá trị trùng lặp (Hide Duplicates); Đánh số trang động và hàm tính tổng nhóm/báo cáo. | 25 điểm | **FULL** | `1급/실기/08-데이터베이스-조회출력-보고서.md` |
| **Access 4** | **처리구현** (Truy vấn Query) | Kỹ thuật xây dựng Select Query với Criteria phức tạp, Trường tính toán (IIF, Switch, Format), Totals Query; Parameter Query; Crosstab Query (Row Heading, Column Heading, Value); Action Query (Update, Append, Delete, Make Table); Unmatched Query. | 20 điểm | **FULL** | `1급/실기/09-데이터베이스-처리구현-쿼리.md` |
| **Access 4** | **프로시저 및 이벤트** (Macro & VBA) | Macro nhúng & độc lập (OpenForm, OpenReport, Requery, ApplyFilter); Lập trình sự kiện VBA: Bộ lọc `Me.Filter`, Định vị bản ghi `Me.RecordsetClone.FindFirst` & Bookmark, Thực thi SQL `DoCmd.RunSQL`, Cập nhật dữ liệu `Me.Requery`. | 10-15đ | **FULL** | `1급/실기/10-데이터베이스-프로시저-및-이벤트.md` |
| **Chiến lược** | **실전 모의고사 및 오류 복구** | Chiến lược phân bổ thời gian 45 phút Excel + 45 phút Access; Thứ tự làm bài tối ưu; Bảng nhận diện và xử lý các lỗi chí mạng 0 điểm tuyệt đối; Checklist 5 phút cuối giờ đối soát an toàn. | 200 điểm | **FULL** | `1급/실기/90-실전-모의고사-및-오류-복구-전략.md` |

---

## 3. Độ phủ 2급 (Cấp độ 2 — Tiêu chuẩn)

| Phân khu | Nội dung | Trạng thái | Owner |
|---|---|:---:|---|
| **2급 필기** | Tin học đại cương + Bảng tính Excel căn bản + Chiến lược giải đề 40 phút | **FULL** | `2급/필기/` (01, 02, 90) |
| **2급 실기** | Thao tác cơ bản, định dạng hiển thị, lọc cơ sở | **FULL** | `2급/실기/01-기본작업.md`, `07-기본작업-심화-서식-필터-외부데이터.md` |
| **2급 실기** | Tính toán bảng tính (40 điểm): 7 đại nhóm hàm & 6 mẫu công thức lồng ghép | **FULL** | `2급/실기/02-계산작업.md`, `05-함수-인벤토리-및-공식-패턴.md` |
| **2급 실기** | Phân tích nghiệp vụ (20 điểm): Pivot Table, Subtotal, Scenario, Data Table | **FULL** | `2급/실기/03-분석작업.md`, `06-분석-기타작업-세부수행-및-감점방지.md` |
| **2급 실기** | Bổ trợ & Tự động hóa (20 điểm): Biểu đồ Chart & Ghi nhận Macro | **FULL** | `2급/실기/04-기타작업.md`, `06-분석-기타작업-세부수행-및-감점방지.md` |
| **2급 실기** | Quy trình phòng chống điểm 0 và làm bài thực chiến 40 phút | **FULL** | `2급/실기/90-실전-모의고사.md` |

---

## 4. Tiêu chí nghiệm thu chất lượng (Quality Acceptance)

1. **Tính đầy đủ theo 출제기준 KCCI:** Đạt 100% độ phủ syllabus cho cả 1급 và 2급.
2. **Tuân thủ AGENTS.md & COMMON_PROMPT.md:**
   - 0 boilerplate rỗng ("Mở đầu", "Bàn giao", "Chuyển mạch").
   - 0 câu hỏi kiểm tra / quiz trắc nghiệm trong learning docs.
   - 100% thuật ngữ tiếng Hàn KCCI chính xác đi kèm diễn giải tiếng Việt tự nhiên và cú pháp Office 2021 LTSC.
3. **Tính liên kết nội bộ:** Toàn bộ liên kết Markdown cục bộ trỏ đúng tệp thực tế trên đĩa, vượt qua kiểm định `repo_audit.py`.
