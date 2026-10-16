# 컴퓨터활용능력 1급 — Bản đồ Học tập Toàn diện (Comprehensive Study Map)

Kỳ thi **컴퓨터활용능력 1급 (Tin học văn phòng Hàn Quốc - Cấp độ 1)** do Phòng Thương mại và Công nghiệp Hàn Quốc (KCCI - 대한상공회의소) tổ chức là chứng chỉ kỹ thuật quốc gia chuyên sâu, đánh giá năng lực tích hợp nâng cao về bảng tính điện tử (Spreadsheet) và quản trị cơ sở dữ liệu quan hệ (Relational Database Management System).

Tài liệu này là cổng điều phối trung tâm (Canonical Entrypoint), thiết lập bức tranh toàn cảnh, so sánh chiến lược giữa 1급 và 2급, cùng hệ thống liên kết đồng bộ đến toàn bộ 16 modules tài liệu học tập của Cấp độ 1.

---

## 1. Cấu trúc tổng quan kỳ thi 1급

Kỳ thi bao gồm hai giai đoạn kiểm tra độc lập:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   GIAI ĐOẠN 1: 필기 (LÝ THUYẾT TRẮC NGHIỆM)             │
├────────────────────────────────────────────────────────────────────────┤
│ • 1과목: 컴퓨터 일반 (Tin học đại cương & Windows 10) — 20 câu          │
│ • 2과목: 스프레드시트 일반 (Bảng tính điện tử Excel) — 20 câu           │
│ • 3과목: 데이터베이스 일반 (Cơ sở dữ liệu Access) — 20 câu             │
│ ──> Tổng: 60 câu / 60 phút.                                            │
│ ──> Tiêu chuẩn đỗ: Mỗi môn >= 40 điểm (tránh liệt) và ĐTB >= 60/100.   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ (Đỗ Lý thuyết mới được thi Thực hành)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                   GIAI ĐOẠN 2: 실기 (THỰC HÀNH MÁY TÍNH)               │
├───────────────────────────────────┬────────────────────────────────────┤
│ MÔN 1: 스프레드시트 실무 (Excel)     │ MÔN 2: 데이터베이스 실무 (Access)     │
│ • Thời gian: 45 phút              │ • Thời gian: 45 phút               │
│ • Điểm tối đa: 100 điểm           │ • Điểm tối đa: 100 điểm            │
├───────────────────────────────────┴────────────────────────────────────┤
│ ──> Tổng thời gian: 90 phút (có nghỉ chuyển đề giữa 2 môn).             │
│ ──> TIÊU CHUẨN ĐỖ CHÍNH THỨC: CẢ 2 MÔN BẮT BUỘC ĐẠT TỪ 70 ĐIỂM TRỞ LÊN.│
│ ──> Quy tắc 과락: Chỉ cần 1 môn dưới 70 điểm là TRƯỢT TOÀN BỘ.         │
└────────────────────────────────────────────────────────────────────────┘
```

* **Môi trường khảo thí chuẩn hóa năm 2026:** Hệ điều hành **Windows 10** và bộ phần mềm văn phòng **Microsoft Office LTSC 2021** (ngôn ngữ giao diện tiếng Hàn).

---

## 2. So sánh chuyên sâu: 1급 vs 2급 (Deep Comparison)

Sự khác biệt giữa 1급 và 2급 không chỉ nằm ở số lượng môn thi mà phản ánh bước nhảy vọt về tư duy xử lý dữ liệu và độ khó thực chiến.

| Tiêu chí so sánh | 컴퓨터활용능력 2급 (Cấp độ 2) | 컴퓨터활용능력 1급 (Cấp độ 1) | Phân tích bản chất kỹ thuật & Độ khó |
|---|---|---|---|
| **Phạm vi môn thi Lý thuyết (필기)** | 2 môn (40 câu / 40 phút): • 컴퓨터 일반; • 스프레드시트 일반 | 3 môn (60 câu / 60 phút): • 컴퓨터 일반; • 스프레드시트 일반; • **데이터베이스 일반** | 1급 mở rộng thêm toàn bộ lý thuyết CSDL quan hệ: Mô hình thực thể ERD, Chuẩn hóa dữ liệu (1NF/2NF/3NF), Khóa chính/Khóa ngoại, Ngôn ngữ truy vấn SQL và Đại số quan hệ. |
| **Phạm vi môn thi Thực hành (실기)** | 1 môn duy nhất (40 phút): • 스프레드시트 실무 (Excel) | 2 môn độc lập (90 phút): • 스프레드시트 실무 (Excel - 45p); • **데이터베이스 실무 (Access - 45p)** | 1급 bắt buộc thao tác hoàn thiện hệ thống trên Microsoft Access: Xây dựng cấu trúc bảng, liên kết quan hệ 1-Nhiều, thiết kế Form, xuất Báo cáo Report và viết Truy vấn Query phức hợp. |
| **Độ phức tạp tính toán Excel** | • Sử dụng hàm đơn và hàm lồng ghép căn bản. • Không có công thức mảng. • Hàm tài chính và tra cứu giới hạn ở dạng cơ sở. | • **Công thức mảng nâng cao (배열 수식)** chiếm 12–18 điểm: Yêu cầu xử lý mảng logic đa điều kiện (`Ctrl+Shift+Enter`). • Tra cứu dữ liệu ma trận động (`INDEX+MATCH`, `OFFSET`). • Xử lý lỗi chuyên sâu. | 1급 đòi hỏi khả năng trừu tượng hóa mảng 2 chiều và tư duy tính toán theo khối dữ liệu thay vì thao tác trên từng ô đơn lẻ. |
| **Mức độ Tự động hóa & Lập trình** | • Chỉ dừng ở mức **Ghi nhận Macro (Macro Recording)** bằng thao tác chuột và gán vào nút bấm/hình vẽ. • Không yêu cầu viết mã lệnh. | • **Lập trình trực tiếp bằng ngôn ngữ VBA (Visual Basic for Applications)**: — 1. Viết hàm tự định nghĩa (`Public Function fn...`). — 2. Lập trình sự kiện Form (`UserForm.Show`, `RowSource`). — 3. Ghi dữ liệu tự động xuống bảng tính bằng `Cells(i, j)`. | 1급 đòi hỏi thí sinh phải nắm vững cú pháp lập trình cơ bản, biến số, cấu trúc rẽ nhánh (`If/Else`, `Select Case`) và mô hình đối tượng (DOM) của Excel. |
| **Độ phức tạp Phân tích số liệu** | • Pivot Table cơ bản (chỉ kéo thả và thiết lập hiển thị đơn giản). • Các công cụ giả lập dữ liệu độc lập. | • Pivot Table ở mức chuyên gia: Nguồn dữ liệu từ CSDL ngoài, tạo trường tính toán (Calculated Field), định dạng số qua Value Field Settings. • **Chấm nhị phân 0 điểm tuyệt đối nếu sai sót nhỏ.** | Khả năng kiểm soát chi tiết và chống sai sót ở 1급 khắt khe hơn gấp nhiều lần. |
| **Tỷ lệ đỗ thực tế (합격률)** | • Lý thuyết: ~50%; • Thực hành: **~40% – 50%** | • Lý thuyết: ~30% – 35%; • Thực hành: **~10% – 15%** | Thực hành 1급 được mệnh danh là một trong những kỳ thi có tỷ lệ trượt cao nhất Hàn Quốc do yêu cầu vượt qua cả 2 môn thực hành cùng lúc với ngưỡng điểm 70. |
| **Giá trị chứng chỉ & Ưu tiên tuyển dụng** | • Điểm cộng công chức cấp cơ sở. • Tín chỉ học tập: 6 tín chỉ. • Phù hợp cho nhân viên hành chính văn phòng căn bản. | • **Cộng điểm tối đa (lên tới 1%) trong kỳ thi công chức Hàn Quốc (7급, 9급 공무원 가산점).**; • Ưu tiên hàng đầu vòng hồ sơ NCS tại các Doanh nghiệp Nhà nước (공기업: KEPCO, Korail, K-water, LH...). • Điểm cộng tuyển dụng tại các Tập đoàn hàng đầu (Samsung, LG, SK, Hyundai) và Ngân hàng thương mại. • Chuyển đổi **14 tín chỉ** trong hệ thống Ngân hàng tín chỉ (학점은행제). • Điều kiện tốt nghiệp bắt buộc tại các trường đại học top đầu (SKY, Sungkyunkwan...). | Chứng chỉ 1급 là bảo chứng thép cho năng lực xử lý dữ liệu và tự động hóa công việc văn phòng chuyên nghiệp tại Hàn Quốc. |

---

## 3. Cây thư mục và Danh mục điều hướng toàn diện (Directory Tree & Index)

Hệ thống tài liệu **컴퓨터활용능력 1급** được cấu trúc thành hai phân khu độc lập: 4 modules Lý thuyết (`필기/`) và 11 modules Thực hành (`실기/`).

```
컴퓨터활용능력/1급/
├── README.md                                                  <── [Trang chủ Study Map hiện tại]
├── 필기/                                                      <── [Phân khu Lý thuyết trắc nghiệm]
│   ├── README.md                                              <── Mục lục & Bản đồ lý thuyết
│   ├── 01-컴퓨터-일반.md                                        <── Tin học đại cương & Windows 10
│   ├── 02-스프레드시트-일반.md                                   <── Bảng tính Excel đại cương
│   ├── 03-데이터베이스-일반.md                                   <── CSDL quan hệ & Access đại cương
│   └── 90-필기-문제풀이-전략.md                                  <── Chiến lược giải đề trắc nghiệm 60 phút
└── 실기/                                                      <── [Phân khu Thực hành máy tính]
    ├── README.md                                              <── Cẩm nang chiến lược & Barem điểm KCCI
    ├── 01-스프레드시트-기본작업.md                                  <── Excel: Lọc nâng cao, Định dạng điều kiện, In
    ├── 02-스프레드시트-계산작업-배열수식.md                           <── Excel: Cơ chế & Cấu trúc công thức mảng
    ├── 03-스프레드시트-계산작업-사용자정의함수-및-고급함수.md           <── Excel: Hàm VBA Function & Hàm nâng cao
    ├── 04-스프레드시트-분석작업.md                                  <── Excel: Pivot Table & Công cụ phân tích
    ├── 05-스프레드시트-기타작업-차트-및-프로시저.md                   <── Excel: Sửa biểu đồ & Lập trình Form VBA
    ├── 06-데이터베이스-DB구축.md                                  <── Access: Thiết kế Bảng & Quan hệ dữ liệu
    ├── 07-데이터베이스-화면구현-폼.md                                <── Access: Thiết kế Biểu mẫu Form & Subform
    ├── 08-데이터베이스-조회출력-보고서.md                             <── Access: Thiết kế Báo cáo Report & Lệnh xuất
    ├── 09-데이터베이스-처리구현-쿼리.md                               <── Access: Xây dựng các loại truy vấn Query
    ├── 10-데이터베이스-프로시저-및-이벤트.md                         <── Access & VBA: DoCmd, Filter, RecordsetClone
    └── 90-실전-모의고사-및-오류-복구-전략.md                     <── Chiến lược thực chiến 90 phút & Chống điểm 0
```

---

### Danh mục chi tiết các Modules học tập

#### Phân khu Lý thuyết: `필기/` (4 modules)

1. [필기 README](./필기/README.md): Lộ trình ôn tập 3 môn lý thuyết, phương pháp học theo bảng đối chiếu khái niệm.
2. [01 — 컴퓨터 일반](./필기/01-컴퓨터-일반.md): Cấu trúc phần cứng máy tính, hệ điều hành Windows 10, quản lý bộ nhớ, truyền thông mạng, giao thức Internet và an toàn bảo mật thông tin.
3. [02 — 스프레드시트 일반](./필기/02-스프레드시트-일반.md): Nguyên lý hoạt động của bảng tính, hệ thống hàm dựng sẵn, biểu đồ phân tích, in ấn và cơ chế vận hành macro tự động.
4. [03 — 데이터베이스 일반](./필기/03-데이터베이스-일반.md): Mô hình CSDL quan hệ, chuẩn hóa bảng dữ liệu, ràng buộc toàn vẹn tham chiếu, ngôn ngữ SQL (DDL, DML, DCL) và đại số quan hệ.
5. [90 — 필기 문제풀이 전략](./필기/90-필기-문제풀이-전략.md): Kỹ thuật phân bổ 60 phút, phương pháp loại trừ phương án nhiễu và nhận diện 10 dạng bẫy trắc nghiệm kinh điển.

#### Phân khu Thực hành: `실기/` (11 modules)

1. [실기 README](./실기/README.md): Bản đồ thực hành tổng quan, cấu trúc barem điểm chi tiết và ma trận yêu cầu của KCCI.
2. [01 — 기본작업 (Excel)](./실기/01-스프레드시트-기본작업.md): Kỹ thuật lập vùng điều kiện logic cho Lọc nâng cao (Advanced Filter), công thức định dạng có điều kiện toàn dòng với khóa cột tuyệt đối (`$`), căn lề trang in và bảo vệ sheet (30 điểm).
3. [02 — 계산작업: 함수 및 배열수식 (Excel)](./실기/02-스프레드시트-계산작업-배열수식.md): Cơ chế thực thi công thức mảng (Array Formula) với `Ctrl+Shift+Enter`, các mẫu mảng tính tổng/đếm/trung bình có điều kiện và hàm tra cứu đa chiều (24 điểm).
4. [03 — 계산작업: 사용자 정의 함수 및 고급 함수 (Excel)](./실기/03-스프레드시트-계산작업-사용자정의함수-및-고급함수.md): Hướng dẫn viết hàm tự tạo trong VBA Module với cấu trúc rẽ nhánh `If/ElseIf/Select Case` (6 điểm tuyệt đối).
5. [04 — 분석작업 (Excel)](./실기/04-스프레드시트-분석작업.md): Quy trình thao tác không điểm chết cho Pivot Table (chống mất 10 điểm), kỹ thuật lập Data Table 2 biến, Scenario, Consolidate và Subtotal (20 điểm).
6. [05 — 기타작업: 차트 및 프로시저 (Excel)](./실기/05-스프레드시트-기타작업-차트-및-프로시저.md): 5 dạng bài hiệu chỉnh biểu đồ chuẩn và quy trình lập trình Form VBA mở/khởi tạo/đóng biểu mẫu và ghi dữ liệu (20 điểm).
7. [06 — DB구축 (Access)](./실기/06-데이터베이스-DB구축.md): Thiết lập thuộc tính bảng, Validation Rule, Input Mask, định dạng hiển thị, khóa chính và thiết lập toàn vẹn quan hệ dữ liệu 1-Nhiều (30 điểm).
8. [07 — 화면구현 (폼 - Access)](./실기/07-데이터베이스-화면구현-폼.md): Thiết lập thuộc tính Form, điều khiển nguồn dữ liệu, nhúng Subform đồng bộ trường liên kết và định dạng điều kiện biểu mẫu (25 điểm).
9. [08 — 조회 및 출력 (보고서 - Access)](./실기/08-데이터베이스-조회출력-보고서.md): Thiết kế Báo cáo Report chuẩn, nhóm và sắp xếp, tính tổng tích lũy (Running Sum), đánh số trang động và hàm miền thống kê (`DLookup`, `DSum`) (25 điểm).
10. [09 — 처리구현 (쿼리 - Access)](./실기/09-데이터베이스-처리구현-쿼리.md): Kỹ thuật xây dựng Select Query, Parameter Query, Crosstab Query, Action Query (Update, Delete, Append, Make Table) và Unmatched Query (20 điểm).
11. [10 — 고급 프로시저 및 이벤트 (Access/Excel)](./실기/10-데이터베이스-프로시저-및-이벤트.md): Làm chủ đối tượng DoCmd, kỹ thuật lọc dữ liệu `Me.Filter`, tìm kiếm `RecordsetClone` và các hàm thông báo hộp thoại.
12. [90 — 실전 모의고사 및 오류 복구 전략](./실기/90-실전-모의고사-및-오류-복구-전략.md): Chiến lược phân bổ thời gian 45 phút cho từng môn, bảng phục hồi lỗi chí mạng 0 điểm và checklist 5 phút đối soát an toàn trước khi nộp bài.

---

## 4. Lộ trình chiến lược ôn thi đề xuất (Strategic Roadmap)

### Lộ trình 1: Nâng cấp từ 2급 lên 1급 (Thời gian ước tính: 4 – 6 tuần)
* **Tuần 1:** Bổ sung môn lý thuyết thứ 3 (데이터베이스 일반) và ôn tập lại kiến thức mạng/phần cứng; luyện giải đề trắc nghiệm thi đỗ 필기.
* **Tuần 2:** Nâng cấp kỹ năng Excel: Làm chủ toàn bộ công thức mảng (`02`), viết hàm tự tạo VBA (`03`) và quy trình chống điểm 0 của Pivot Table (`04`).
* **Tuần 3:** Học mới hoàn toàn Access: Nắm chắc thiết kế Bảng & Quan hệ (`06`), biểu mẫu Form (`07`) và Báo cáo Report (`08`).
* **Tuần 4:** Chinh phục các loại Truy vấn Query (`09`) và Lập trình sự kiện DoCmd (`10`).
* **Tuần 5 – 6:** Luyện giải đề thi thực chiến theo giới hạn 45 phút từng môn, áp dụng nghiêm ngặt cẩm nang [90 — 실전 모의고사 및 오류 복구 전략](./실기/90-실전-모의고사-및-오류-복구-전략.md).

### Lộ trình 2: Bắt đầu trực tiếp từ 1급 (Thời gian ước tính: 8 – 10 tuần)
* Xây dựng nền tảng lý thuyết song song với việc thao tác thực tế trên phần mềm. Không học lý thuyết suông dạng học vẹt câu chữ mà mở trực tiếp Excel và Access tiếng Hàn để đối chiếu từng tính năng.
* Tuân thủ triết lý đào tạo của repository: **Khái niệm (Concept) → Cơ chế vận hành (Mechanism) → So sánh & Bẫy đề thi (Comparison/Trap) → Thao tác thực tế (Action) → Quy trình đối soát (Verification)**.
