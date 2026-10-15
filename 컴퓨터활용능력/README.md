# 컴퓨터활용능력 (Tin học văn phòng Hàn Quốc) — Root Entrypoint

컴퓨터활용능력 (Chứng chỉ Tin học văn phòng) là kỳ thi kỹ năng quốc gia do Phòng Thương mại và Công nghiệp Hàn Quốc (KORCHAM - 대한상공회의소) chủ trì. Thư viện này thiết lập lộ trình chuẩn hóa (canonical track) cho **컴퓨터활용능력 2급 (Cấp độ 2)**, bao quát đầy đủ cả lý thuyết (필기) và thực hành thao tác bảng tính (실기).

## Cấu trúc nội dung

### 2급 필기 (Lý thuyết trắc nghiệm)

- [01 — 컴퓨터 일반 (Tin học đại cương / Windows 10)](./2급/필기/01-컴퓨터-일반.md)
- [02 — 스프레드시트 일반 (Bảng tính đại cương / Excel)](./2급/필기/02-스프레드시트-일반.md)
- [90 — 필기 문제풀이 전략 (Chiến lược giải đề & phân loại bẫy)](./2급/필기/90-필기-문제풀이-전략.md)

### 2급 실기 (Thực hành bảng tính Excel)

- [01 — 기본작업 (Thao tác cơ bản & định dạng dữ liệu)](./2급/실기/01-기본작업.md)
- [02 — 계산작업 (Cơ chế công thức & hàm tính toán cốt lõi)](./2급/실기/02-계산작업.md)
- [03 — 분석작업 (Phân tích dữ liệu & tổng hợp nghiệp vụ)](./2급/실기/03-분석작업.md)
- [04 — 기타작업 (Biểu đồ Chart & Tự động hóa Macro)](./2급/실기/04-기타작업.md)
- [05 — 계산작업 공식 함수 인벤토리 및 중첩 패턴 (Tra cứu hàm & mẫu lồng ghép nâng cao)](./2급/실기/05-함수-인벤토리-및-공식-패턴.md)
- [06 — 분석·기타작업 세부수행 및 감점방지 매뉴얼 (Quy trình thao tác & phòng tránh điểm 0)](./2급/실기/06-분석-기타작업-세부수행-및-감점방지.md)
- [07 — 기본작업 심화 — 서식·필터·외부데이터 (Định dạng nâng cao, bộ lọc & nhập dữ liệu ngoài)](./2급/실기/07-기본작업-심화-서식-필터-외부데이터.md)
- [90 — 실전 모의고사 (Quy trình làm bài 40 phút & kiểm tra đối soát)](./2급/실기/90-실전-모의고사.md)

## Chuẩn môi trường thi (Exam Baseline)

Tiêu chuẩn chuẩn bị thi năm 2026:

- **필기 (Lý thuyết):** 컴퓨터 일반 (20 câu) + 스프레드시트 일반 (20 câu) — Trắc nghiệm 40 câu / 40 phút.
  - Điểm đỗ: Từng môn từ 40 điểm trở lên (tránh liệt) và điểm trung bình đạt từ 60/100 trở lên.
- **실기 (Thực hành):** 스프레드시트 실무 (Thao tác trực tiếp trên máy tính) / 40 phút.
  - Điểm đỗ: Đạt từ 70/100 điểm trở lên.
- **Hệ điều hành chuẩn (OS):** Windows 10.
- **Bộ phần mềm văn phòng chuẩn (Office):** Microsoft Office LTSC 2021 (giao diện tiếng Hàn).

KORCHAM đã công bố tiêu chuẩn đề thi mới cho giai đoạn **2027–2029** (áp dụng từ 01/01/2027). Toàn bộ ranh giới phiên bản và lộ trình chuyển đổi được quản lý độc lập tại [EXAM_VERSION_NOTES.md](./EXAM_VERSION_NOTES.md).

## Phương pháp biên soạn

Thư viện được xây dựng theo chuỗi nhận thức:

**Khái niệm (Concept) → Cơ chế vận hành (Mechanism) → So sánh & bẫy đề thi (Comparison/Trap) → Thao tác Excel thực tế (Action) → Quy trình đối soát (Verification)**

Tất cả thuật ngữ giao diện và đề thi tiếng Hàn được giữ nguyên vẹn để người học tra cứu chính xác khi thao tác trên phần mềm Excel tiếng Hàn, đồng thời đi kèm diễn giải tiếng Việt tự nhiên và từ khóa tiếng Anh tương ứng.

## Trạng thái chất lượng

Toàn bộ 100 điểm của bài thi thực hành 2급 đã được xây dựng hoàn chỉnh với các cẩm nang thao tác chi tiết (modules 05–07) cùng quy trình phòng ngừa trừ điểm:
1. Đầy đủ danh mục hàm và mẫu công thức lồng ghép theo tiêu chuẩn 2024–2026 (`05`).
2. Quy trình thao tác không điểm chết cho phần phân tích (Pivot Table, Subtotal, Scenario, Data Table, Consolidate, Goal Seek) và phần bổ trợ (Macro, Chart) (`06`).
3. Kỹ thuật định dạng có điều kiện, lọc nâng cao theo biểu thức logic và định dạng tùy chỉnh (`07`).
4. Theo dõi chi tiết độ bao phủ đề thi tại [COVERAGE_AUDIT.md](./COVERAGE_AUDIT.md).

## Điểm vào học tập (Entrypoint)

→ [컴퓨터활용능력 2급 Study Map](./2급/README.md)
