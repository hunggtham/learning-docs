# 컴퓨터활용능력 2급 — Bản đồ học tập (Study Map)

Tài liệu này là lộ trình học tập chuẩn (canonical learning route) cho kỳ thi **컴퓨터활용능력 2급** theo tiêu chuẩn xuất đề **2024–2026 출제기준**. Lộ trình được thiết kế theo nguyên tắc: hiểu sâu bản chất khái niệm ở phần lý thuyết (필기), sau đó chuyển hóa trực tiếp thành phản xạ thao tác trên phần mềm Excel ở phần thực hành (실기).

## Cấu trúc kỳ thi 2급

| Phân loại | Môn thi | Hình thức | Thời gian |
|---|---|---|---:|
| **필기 (Lý thuyết)** | 컴퓨터 일반 + 스프레드시트 일반 | Trắc nghiệm 40 câu | 40 phút |
| **실기 (Thực hành)** | 스프레드시트 실무 (Excel) | Thao tác trên máy tính | 40 phút |

**Tiêu chuẩn đạt điểm đỗ (합격 기준):**
- **필기:** Từng môn đạt từ 40 điểm trở lên (không bị điểm liệt) và điểm trung bình cộng 2 môn đạt từ 60/100 trở lên.
- **실기:** Đạt từ 70/100 điểm trở lên (bài thi chấm tự động bằng phần mềm, có nhiều mục 0 điểm tuyệt đối nếu sai quy cách).

Môi trường thi chuẩn áp dụng năm 2026: **Windows 10** và **Microsoft Office LTSC 2021** (giao diện tiếng Hàn).

## 1. 필기 (Lý thuyết trắc nghiệm)

Trang mục lục: [필기 Index](./필기/README.md)

1. [01 — 컴퓨터 일반](./필기/01-컴퓨터-일반.md): Cấu trúc máy tính, hệ điều hành Windows 10, CPU/bộ nhớ, mạng Internet, đa phương tiện và an toàn thông tin.
2. [02 — 스프레드시트 일반](./필기/02-스프레드시트-일반.md): Khái niệm bảng tính, địa chỉ ô (tương đối/tuyệt đối/hỗn hợp), công thức & hàm, định dạng, sắp xếp, lọc, PivotTable, biểu đồ và Macro.
3. [90 — 필기 문제풀이 전략](./필기/90-필기-문제풀이-전략.md): Chiến lược phân bổ 40 phút, sơ đồ cây quyết định chọn hàm, nhận diện bẫy so sánh và phương pháp loại trừ phương án sai.

Mục tiêu học lý thuyết không phải là học vẹt từng câu chữ, mà là nắm rõ các cặp đối chiếu (A vs B) và hiểu mục đích vận hành của từng tính năng.

## 2. 실기 (Thực hành Excel)

Trang mục lục: [실기 Index](./실기/README.md)

1. [01 — 기본작업](./실기/01-기본작업.md): Nhập liệu, định dạng ô, điều kiện định dạng, bộ lọc dữ liệu cơ bản.
2. [02 — 계산작업](./실기/02-계산작업.md): Nền tảng công thức, địa chỉ tham chiếu, các hàm thống kê, toán học, tra cứu và logic cơ bản.
3. [03 — 분석작업](./실기/03-분석작업.md): Sắp xếp, Subtotal (부분합), Consolidate (통합), Goal Seek (목표값 찾기), Data Table (데이터 표), Scenario (시나리오) và PivotTable.
4. [04 — 기타작업](./실기/04-기타작업.md): Hiệu chỉnh biểu đồ (Chart) và ghi nhận Macro gắn nút bấm.
5. [05 — 계산작업 공식 함수 인벤토리 및 중첩 패턴](./실기/05-함수-인벤토리-및-공식-패턴.md): Cẩm nang 7 nhóm hàm chính thức và 6 mẫu công thức lồng ghép kinh điển chiếm 40 điểm thi.
6. [06 — 분석·기타작업 세부수행 및 감점방지 매뉴얼](./실기/06-분석-기타작업-세부수행-및-감점방지.md): Quy trình thao tác chuẩn từng bước và kỹ thuật chống điểm 0 cho phần phân tích (20 điểm) và bổ trợ (20 điểm).
7. [07 — 기본작업 심화 — 서식·필터·외부데이터](./실기/07-기본작업-심화-서식-필터-외부데이터.md): Định dạng tùy chỉnh nâng cao (Custom Number Format), công thức điều kiện toàn dòng và bộ lọc nâng cao (Advanced Filter).
8. [90 — 실전 모의고사](./실기/90-실전-모의고사.md): Trình tự giải đề 40 phút, xử lý khi gặp sự cố và bảng kiểm tra soát lỗi trước khi nộp bài.

Mục tiêu thực hành là chuyển đổi đề bài dạng văn bản thành chuỗi thao tác chính xác: **Vùng chọn mục tiêu (Target Range) → Lệnh thao tác (Operation) → Ràng buộc điều kiện (Condition) → Kết quả mong muốn (Output)**.

## Mối liên kết giữa lý thuyết và thực hành

| Khái niệm ở phần 필기 | Chuyển hóa thành thao tác ở phần 실기 |
|---|---|
| Cell / Range / Data Types | Thao tác nhập liệu và định dạng ở 기본작업 (01, 07) |
| Cell References / Built-in Functions | Xây dựng công thức và lồng hàm ở 계산작업 (02, 05) |
| What-If Analysis / Pivot Table | Phân tích số liệu và lập báo cáo ở 분석작업 (03, 06) |
| Chart Elements / Macro Recording | Trực quan hóa và tự động hóa thao tác ở 기타작업 (04, 06) |

## Quản lý phiên bản tiêu chuẩn đề thi

Phòng Thương mại và Công nghiệp Hàn Quốc (KORCHAM) đã công bố tiêu chuẩn đề thi giai đoạn 2027–2029 áp dụng từ ngày 01/01/2027. Chi tiết khác biệt và kế hoạch cập nhật được theo dõi riêng tại [EXAM_VERSION_NOTES.md](../EXAM_VERSION_NOTES.md).
