# 컴퓨터활용능력 1급 실기 — Cẩm nang Chiến lược & Bản đồ Thực hành

Kỳ thi thực hành **컴퓨터활용능력 1급 (Tin học văn phòng Hàn Quốc - Cấp độ 1)** do Phòng Thương mại và Công nghiệp Hàn Quốc (KCCI - 대한상공회의소) chủ trì là kỳ thi kỹ năng số chuyên sâu bậc cao, được mệnh danh là một trong những chứng chỉ thực hành có tính sàng lọc khắt khe nhất trong hệ thống chứng chỉ kỹ thuật quốc gia Hàn Quốc.

Tài liệu này đóng vai trò là kim chỉ nam điều phối lộ trình học tập, cấu trúc barem điểm thi chính thức, phương pháp chấm tự động và ma trận liên kết hệ thống tài liệu thực hành 1급 theo chuẩn khảo thí hiện hành.

---

## 1. Tổng quan kỳ thi thực hành 1급 (Exam Overview)

Kỳ thi thực hành 1급 không kiểm tra đơn lẻ một ứng dụng mà đòi hỏi năng lực vận hành đồng thời hai hệ thống phần mềm nghiệp vụ văn phòng cốt lõi: bảng tính nâng cao và quản trị cơ sở dữ liệu quan hệ.

```
┌────────────────────────────────────────────────────────────────────────┐
│                   TỔNG THỜI GIAN THỰC HÀNH: 90 PHÚT                    │
├───────────────────────────────────┬────────────────────────────────────┤
│ MÔN 1: 스프레드시트 실무 (Excel)     │ MÔN 2: 데이터베이스 실무 (Access)     │
│ Thời gian: 45 phút                │ Thời gian: 45 phút                 │
│ Điểm tối đa: 100 điểm             │ Điểm tối đa: 100 điểm              │
└───────────────────────────────────┴────────────────────────────────────┘
                  [Giải lao chuyển đề: 5 – 10 phút]
```

### Tiêu chuẩn công nhận đỗ (합격 기준)

* **Điều kiện tiên quyết:** Thí sinh bắt buộc phải đạt **tối thiểu 70/100 điểm ở CẢ HAI MÔN THI**.
* **Nguyên tắc loại trừ tuyệt đối (과락):** 
  * Nếu môn Excel đạt 100 điểm tuyệt đối nhưng môn Access chỉ đạt 69 điểm, kết quả chung cuộc vẫn là **Không đạt (불합격)**.
  * Không áp dụng cơ chế bù điểm trung bình cộng giữa hai môn.
  * Không bảo lưu kết quả từng môn thực hành. Nếu trượt, thí sinh phải đăng ký thi lại toàn bộ cả 2 môn trong kỳ thi tiếp theo.
* **Cơ chế chấm điểm tự động (채점 프로그램):** Toàn bộ bài làm của thí sinh được quét bằng hệ thống chấm tự động của KCCI. Hệ thống này kiểm tra chính xác từng thuộc tính ô tính, tên trường, cú pháp công thức, thuộc tính form/report và quan hệ dữ liệu. Nhiều hạng mục lớn áp dụng nguyên tắc nhị phân (chỉ có điểm tối đa hoặc 0 điểm, không có điểm thành phần nếu sai phạm quy cách).

---

## 2. Barem điểm chi tiết chính thức (Detailed Scoring Breakdown)

### Môn 1: 스프레드시트 실무 (Microsoft Excel — 45 phút / 100 điểm)

| Phần thi | Tên nghiệp vụ tiếng Hàn | Điểm số | Số lượng câu | Quy cách chấm điểm & Bản chất kỹ thuật |
|---|---|:---:|:---:|---|
| **기본작업** | Thao tác cơ bản & Bố cục dữ liệu | **30 điểm** | 3 – 4 câu | • **고급필터 (Lọc nâng cao - 5đ):** Thiết lập vùng điều kiện logic bằng công thức (`AND`, `OR`, mảng so sánh), trích xuất chính xác danh sách cột theo yêu cầu.<br>• **조건부 서식 (Định dạng có điều kiện - 5đ):** Công thức logic khóa cột tuyệt đối (`=$A3...`), chọn vùng dữ liệu không chứa dòng tiêu đề.<br>• **페이지 레이아웃 & 시트 보호 (Bố cục trang & Bảo vệ sheet - 5đ):** Lặp lại dòng tiêu đề khi in, căn giữa trang ngang/dọc, khóa ô chỉ định và bảo vệ bảng tính.<br>• **외부 데이터 / 텍스트 나누기 (Dữ liệu ngoài / Tách chuỗi - 15đ):** Nhập file dữ liệu ngoài (`.txt`, `.csv`, `.accdb`), phân định dấu phân cách hoặc độ rộng cố định. |
| **계산작업** | Cơ chế tính toán & Công thức mảng | **30 điểm** | 5 câu x 6đ | • **일반 함수 (Hàm nâng cao - 1~2 câu):** Lồng ghép tra cứu đa tầng (`INDEX`, `MATCH`, `OFFSET`, `VLOOKUP`, `XLOOKUP`), hàm tài chính, ngày giờ.<br>• **배열 수식 (Công thức mảng - 2~3 câu):** Xử lý mảng đa điều kiện kết hợp `SUM`, `AVERAGE`, `COUNT`, `LARGE`, `MAX`, `IF` kết thúc bằng `Ctrl+Shift+Enter`.<br>• **사용자 정의 함수 (Hàm tự định nghĩa - 1 câu):** Lập trình VBA `Public Function fn...()` xử lý rẽ nhánh `If ~ ElseIf ~ End If` hoặc `Select Case`. |
| **분석작업** | Phân tích nghiệp vụ & Báo cáo động | **20 điểm** | 2 câu x 10đ | • **피벗 테이블 보고서 (Pivot Table - 10đ):** Nguồn dữ liệu ngoài/bảng, nhóm dữ liệu, trường tính toán (Calculated Field), định dạng hiển thị số qua Value Field Settings. **Lưu ý chí mạng: Không có điểm bộ phận, sai bất kỳ chi tiết nào tính 0 điểm toàn phần!**<br>• **기타 분석작업 (Công cụ phân tích khác - 10đ):** Sắp xếp & Subtotal (부분합), Bảng dữ liệu (데이터 표), Quản lý kịch bản (시나리오), Hợp nhất dữ liệu (데이터 통합), Tìm mục tiêu (목표값 찾기) hoặc Kiểm tra tính hợp lệ dữ liệu (유효성 검사). |
| **기타작업** | Trực quan hóa & Tự động hóa VBA | **20 điểm** | 2 phần lớn | • **차트 수정 (Hiệu chỉnh biểu đồ - 10đ):** 5 tiểu mục nhỏ (2đ/câu), thay đổi loại biểu đồ, trục phụ (보조축), nhãn dữ liệu, tiêu đề liên kết ô, định dạng trục số liệu.<br>• **기타작업-2 프로그래밍 (VBA Form & Bảng tính - 10~15đ):** 3 tiểu mục (5đ/câu):<br>1. Nút mở Form (`Form.Show`) và sự kiện `UserForm_Initialize` nạp dữ liệu (`RowSource`, `AddItem`).<br>2. Ghi dữ liệu từ Form xuống hàng trống tiếp theo của bảng tính (`Cells(i, j)`).<br>3. Nút đóng Form (`Unload Me`) và thông báo hoàn tất (`MsgBox`). |

---

### Môn 2: 데이터베이스 실무 (Microsoft Access — 45 phút / 100 điểm)

| Phần thi | Tên nghiệp vụ tiếng Hàn | Điểm số | Số lượng câu | Quy cách chấm điểm & Bản chất kỹ thuật |
|---|---|:---:|:---:|---|
| **DB구축** | Xây dựng cấu trúc Cơ sở dữ liệu | **30 điểm** | 3 phần | • **테이블 완성 (Hoàn thiện bảng - 20đ):** 5 tiểu mục (4đ/câu). Thiết lập Khóa chính (Primary Key), Kiểu dữ liệu (Data Type), Kích thước trường (Field Size), Quy tắc hợp lệ (Validation Rule), Thông báo lỗi (Validation Text), Mặt nạ nhập liệu (Input Mask), Định dạng hiển thị (Format), Giá trị mặc định (Default Value), Bắt buộc nhập (Required), Cho phép rỗng (Allow Zero Length), Trường tra cứu (Lookup Field Wizard).<br>• **관계 설정 (Thiết lập quan hệ - 5đ):** Liên kết bảng 1-Nhiều, áp dụng Ràng buộc toàn vẹn tham chiếu (참조 무결성 유지), Cập nhật liên hoàn (관련 필드 모두 업데이트), Xóa liên hoàn (관련 레코드 모두 삭제).<br>• **외부 데이터 가져오기 / 연결 (Dữ liệu ngoài - 5đ):** Nhập khẩu bảng từ Excel, Text hoặc Access ngoài vào bảng mới hoặc nối vào bảng hiện có. |
| **화면구현** | Thiết kế giao diện biểu mẫu (Form) | **25 điểm** | 2 – 3 phần | • **폼 완성 (Hoàn thiện Form - 15đ):** 5 tiểu mục (3đ/câu). Gán nguồn dữ liệu (`RecordSource`), điều khiển nguồn ô (`ControlSource`), chặn cuộn/di chuyển (`ScrollBars`, `NavigationButtons`, `RecordSelectors`), định dạng tự động giãn (`CanGrow`), sắp xếp thứ tự tab (`TabOrder`).<br>• **하위 폼 (Subform - 5đ):** Nhúng biểu mẫu con vào biểu mẫu chính, đồng bộ liên kết trường khóa chính - khóa ngoại (`LinkMasterFields`, `LinkChildFields`).<br>• **조건부 서식 / 컨트롤 제어 (Định dạng điều kiện / Nút lệnh - 5đ):** Đổi màu điều khiển theo điều kiện dữ liệu hoặc thiết lập thuộc tính điều khiển qua sự kiện. |
| **조회 및 출력** | Báo cáo in ấn & Truy vấn hiển thị | **25 điểm** | 2 phần | • **보고서 완성 (Hoàn thiện Report - 15đ):** 5 tiểu mục (3đ/câu). Sắp xếp và nhóm dữ liệu (정렬 및 그룹화), Bật/Tắt đầu trang & chân trang nhóm (Group Header/Footer), Tính tổng tích lũy (누적 합계 - Running Sum), Đánh số trang động (`[Page] & "/" & [Pages]`), Tính toán tổng hợp qua hàm miền (`DLookup`, `DSum`, `DCount`, `Sum`).<br>• **조회 / 출력 이벤트 프로시저 (Thủ tục sự kiện - 10đ):** Viết mã VBA cho nút in/mở: `DoCmd.OpenReport "보고서명", acViewPreview, , "조건식"` hoặc gán bộ lọc Form: `Me.Filter = "필드명 = " & txt조회`, `Me.FilterOn = True`, phương thức `Me.RecordsetClone.FindFirst`. |
| **처리구현** | Xử lý nghiệp vụ & Truy vấn dữ liệu | **20 điểm** | 3 – 4 câu | • **쿼리 작성 (Tạo truy vấn Query - 15~20đ):** 3-4 câu truy vấn phức hợp (4~7đ/câu):<br>1. Truy vấn chọn lọc có điều kiện (Select Query).<br>2. Truy vấn tham số nhận giá trị từ bàn phím hoặc Form (Parameter Query).<br>3. Truy vấn tổng hợp dữ liệu ma trận 2 chiều (Crosstab Query).<br>4. Truy vấn hành động làm thay đổi dữ liệu bảng (Action Query: Update, Delete, Append, Make Table).<br>5. Truy vấn tìm bản ghi không khớp (Unmatched Query bằng Not In hoặc Not Exists / Left Join).<br>• **이벤트 프로시저 / 매크로 (Thủ tục xử lý - 0~5đ):** Thi hành truy vấn cập nhật tự động `DoCmd.RunSQL`, làm mới dữ liệu `Me.Requery`. |

---

## 3. Bản đồ học tập & Ánh xạ tài liệu 1급 실기 (Learning Roadmap)

Hệ thống tài liệu thực hành 1급 bao gồm 10 chuyên đề thực chiến chuyên sâu và 1 cẩm nang giải đề tổng lực, phân bổ chính xác theo trọng số điểm bài thi:

| Mã số | Tên chuyên đề & Liên kết | Phạm vi nghiệp vụ | Trọng số đề thi | Mức độ ưu tiên |
|:---:|---|---|:---:|:---:|
| `01` | [01 — 기본작업](./01-스프레드시트-기본작업.md) | Excel: Lọc nâng cao logic, định dạng có điều kiện toàn dòng, bố cục trang in, bảo vệ sheet, nhập dữ liệu ngoài | 30 điểm Excel | **Bắt buộc trọn điểm (30/30)** |
| `02` | [02 — 계산작업: 함수 및 배열수식](./02-스프레드시트-계산작업-배열수식.md) | Excel: Hàm tra cứu nâng cao (`INDEX`, `MATCH`, `OFFSET`), kỹ thuật xây dựng công thức mảng đa điều kiện | 24 điểm Excel | **Trọng tâm phân loại (18-24đ)** |
| `03` | [03 — 계산작업: 사용자 정의 함수 및 고급 함수](./03-스프레드시트-계산작업-사용자정의함수-및-고급함수.md) | Excel: Lập trình hàm VBA tự tạo (`Public Function`), hàm tài chính, xử lý chuỗi và ngày giờ | 6 điểm Excel | **Lấy trọn 6 điểm dễ nhất** |
| `04` | [04 — 분석작업](./04-스프레드시트-분석작업.md) | Excel: Quy trình thao tác chống điểm 0 của Pivot Table, Data Table 2 biến, Scenario, Consolidate, Subtotal | 20 điểm Excel | **Bắt buộc trọn điểm (20/20)** |
| `05` | [05 — 기타작업: 차트 및 프로시저](./05-스프레드시트-기타작업-차트-및-프로시저.md) | Excel: 5 dạng hiệu chỉnh biểu đồ chuẩn, lập trình Form VBA (mở/khởi tạo form, ghi dữ liệu ô tính, đóng form) | 20 điểm Excel | **Mục tiêu đạt từ 15/20** |
| `06` | [06 — DB구축](./06-데이터베이스-DB구축.md) | Access: Thiết kế bảng, kiểu dữ liệu, Input Mask, Validation Rule, Khóa chính, Ràng buộc quan hệ dữ liệu 1-Nhiều | 30 điểm Access | **Bắt buộc trọn điểm (30/30)** |
| `07` | [07 — 화면구현 (폼)](./07-데이터베이스-화면구현-폼.md) | Access: Thuộc tính Form chính, gán RecordSource, nhúng Subform đồng bộ khóa liên kết, định dạng điều kiện trên Form | 25 điểm Access | **Mục tiêu đạt từ 20-25đ** |
| `08` | [08 — 조회 및 출력 (보고서)](./08-데이터베이스-조회출력-보고서.md) | Access: Thiết kế Báo cáo Report, nhóm/sắp xếp, tổng lũy kế (Running Sum), số trang động, hàm miền thống kê | 25 điểm Access | **Mục tiêu đạt từ 20-25đ** |
| `09` | [09 — 처리구현 (쿼리)](./09-데이터베이스-처리구현-쿼리.md) | Access: Kỹ thuật xây dựng Select, Parameter, Crosstab, Action Query (Update, Delete, Append, Make Table), Unmatched Query | 20 điểm Access | **Trọng tâm kỹ thuật (15-20đ)** |
| `10` | [10 — 고급 프로시저 및 이벤트](./10-데이터베이스-프로시저-및-이벤트.md) | Access & Excel: Đối tượng DoCmd, kỹ thuật lọc `Me.Filter`, tìm kiếm `RecordsetClone`, tự động hóa Macro | Tích hợp | **Chốt chặn điểm cao** |
| `90` | [90 — 실전 모의고사 및 오류 복구 전략](./90-실전-모의고사-및-오류-복구-전략.md) | Chiến lược phân bổ thời gian 45 phút từng môn, bảng xử lý lỗi chí mạng 0 điểm và checklist 5 phút trước khi nộp bài | 200 điểm tổng | **Kim chỉ nam phòng thi** |

---

## 4. Chiến lược tổng lực vượt ngưỡng 70 điểm kép

Muốn chinh phục chứng chỉ 1급, người học không thể áp dụng phương pháp "làm bài tuần tự từ trên xuống dưới" thông thường mà phải xây dựng tư duy phân bổ nguồn lực có tính toán.

### Kịch bản phân bổ điểm an toàn (Safety Margin Blueprint)

```
MÔN EXCEL (Mục tiêu: 80 – 85 điểm)
  [기본작업] 30/30 điểm  ──> Tuyệt đối không để mất điểm
  [분석작업] 20/20 điểm  ──> Tuân thủ quy trình kiểm soát Pivot Table
  [기타작업] 15/20 điểm  ──> Trọn 10đ biểu đồ + 5đ mở/đóng Form (bỏ qua VBA nhập liệu nếu thiếu giờ)
  [계산작업] 18~24/30 điểm ──> Trọn 6đ hàm tự tạo VBA + giải đúng 2 đến 3 câu mảng/hàm thường

MÔN ACCESS (Mục tiêu: 80 – 85 điểm)
  [DB구축]   30/30 điểm  ──> Nền tảng cốt lõi, bắt buộc trọn vẹn
  [화면구현] 20~25/25 điểm ──> Hoàn thiện thuộc tính Form & Subform
  [조회출력] 20~25/25 điểm ──> Hoàn thiện Report & lệnh mở báo cáo
  [처리구현] 12~16/20 điểm ──> Giải đúng 2 đến 3 câu Query căn bản
```

### Nguyên tắc sống còn trong phòng thi

1. **Phần mềm chấm điểm không có cảm xúc:** Bất kỳ thao tác dư thừa nào làm sai cấu trúc bảng tính hoặc làm đổi tên trường CSDL đều bị trừ điểm tối đa. Làm đúng và đủ theo từng câu chữ của đề bài, không tự ý sáng tạo hay thêm định dạng ngoài yêu cầu.
2. **Kỷ luật thời gian nghiêm ngặt:** Nếu một câu tính toán mảng trong Excel hoặc một câu truy vấn Crosstab trong Access vượt quá 3 phút mà chưa tìm ra hướng giải, lập tức đánh dấu bỏ qua để chuyển sang câu tiếp theo. 
3. **Thứ tự thao tác mang tính quyết định:** Trình tự làm bài tối ưu và các kỹ thuật đối soát chi tiết được đúc kết toàn diện tại chuyên mục [90 — 실전 모의고사 및 오류 복구 전략](./90-실전-모의고사-및-오류-복구-전략.md).
