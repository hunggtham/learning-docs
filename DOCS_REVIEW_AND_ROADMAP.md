# BÁO CÁO TOÀN DIỆN VỀ HỆ THỐNG TÀI LIỆU (DOCS AUDIT & ENHANCEMENT ROADMAP)

> **Ngày thực hiện:** 16/10/2026
> **Phạm vi khảo sát:** Toàn bộ 42 chuyên mục tài liệu (2,485+ tài liệu Markdown) trong kho tri thức `00.my-learning`.
> **Mục tiêu:** Đánh giá hiện trạng chi tiết, chỉ rõ các lỗi kỹ thuật và ngữ nghĩa, định hình tiêu chuẩn cần áp dụng và vạch ra lộ trình nâng cấp bài bản.

---

## I. TỔNG QUAN HIỆN TRẠNG TOÀN KHO TÀI LIỆU

### 1. Bảng phân bố tài liệu theo nhóm chuyên đề

| Nhóm chuyên đề | Số chuyên mục | Số lượng file Markdown | Trạng thái kỹ thuật & chất lượng | Mức độ ưu tiên nâng cấp |
| :--- | :---: | :---: | :--- | :---: |
| **1. Chứng chỉ chuyên môn (Certifications)** | 6 | 363 files | 2 môn đạt chuẩn tuyệt đối (정보처리기사, SQLD); 4 môn cần chuẩn hóa (Comhwal, PMP, Chứng khoán, Kế toán). | **ƯU TIÊN 1 (Khẩn cấp)** |
| **2. Khoa học máy tính & Kỹ thuật (CS & Engineering)** | 7 | 817 files | 75.5% (461/610 file CS) dính boilerplate nối mạch tự sinh; dịch máy cơ học nhiều từ ngữ. | **ƯU TIÊN 2 (Cao)** |
| **3. Hàn Quốc học, Hội nhập & Pháp luật** | 5 | 251 files | Nhiều bài kinh tế dính boilerplate (58/63 file); cần đồng bộ song ngữ thực chiến. | **ƯU TIÊN 3 (Trung bình)** |
| **4. Khoa học cơ bản (Math, Physics, Chem, Bio)** | 4 | 343 files | Trên 93% file dính boilerplate chuyển mạch; thiếu ví dụ bài toán thực tế. | **ƯU TIÊN 4 (Trung bình)** |
| **5. Khoa học xã hội, Nhân văn & Lịch sử** | 8 | 708 files | Chứa nhiều bài viết tổng quan; cần rà soát tính mạch lạc và liên kết tri thức. | **ƯU TIÊN 5 (Kế hoạch)** |

---

## II. ĐÁNH GIÁ CHI TIẾT THEO TỪNG LĨNH VỰC & NHỮNG ĐIỂM CẦN APPLY

### 1. NHÓM CHỨNG CHỈ (CERTIFICATIONS) — TRỌNG TÂM HÀNG ĐẦU

#### A. Đã đạt chuẩn Vàng (Gold Standard):
1. **정보처리기사 (Kỹ sư Xử lý Thông tin Hàn Quốc - 84 bài học):**
   - Đạt **100% Quality Audit Pass (84/84)** theo `scripts/run_quality_audit.py`.
   - Cấu trúc 7 phần chuẩn mực: `학습 목표`, `핵심 키워드`, `선행·연결 개념`, `읽는 방법`, `TẦNG A (Ghi chú nén)`, `TẦNG B (Hiểu sâu)`, `복습 체크리스트`.
   - Song ngữ đầy đủ: `Thuật ngữ Hangul / Tiếng Anh / Tiếng Việt`, biểu đồ ASCII, công thức và code trace chi tiết.
2. **SQLD (SQL Developer - K-Data 2024 개정판 - 19 bài học):**
   - Đạt **100% Audit Pass (19/19)** theo `sql/scripts/audit_sqld_learning_output.py`.
   - Đầy đủ 2024 revision: PIVOT/UNPIVOT, 5 hàm REGEXP, Window frames, Hierarchical queries, Surrogate key evaluation.
   - Mỗi bài học đều có chuyên mục **Cạm bẫy thi cử trọng điểm (출제 함정 & 오답 노트)** và **3-4 câu trắc nghiệm thi thử mô phỏng có giải thích chi tiết**.

#### B. Những phần cần APPLY & NÂNG CẤP NGAY:
1. **Vấn đề tổ chức thư mục `cert/`:**
   - **Hiện trạng:** Hiện tại thư mục `cert/` chỉ chứa duy nhất `컴퓨터활용능력`. Trong khi đó, `정보처리기사`, `sql`, `pmp`, `증권투자기초` đang nằm phân tán ở thư mục gốc (root directory).
   - **Cần Apply:**
     - Tái cấu trúc hoặc thiết lập Symlink/Route chuẩn để quy hoạch toàn bộ các chứng chỉ vào không gian chung `cert/`:
       * `cert/정보처리기사/`
       * `cert/sqld/` (hoặc giữ `sql/` và tạo symlink vào `cert/sqld`)
       * `cert/컴퓨터활용능력/` (1급, 2급)
       * `cert/pmp/`
       * `cert/증권투자기초/`
2. **컴퓨터활용능력 (Tin học văn phòng 1급 & 2급 - 35 files):**
   - **Hiện trạng:** Nội dung bài học rất tốt, đã có song ngữ Hàn - Việt và hình minh họa ASCII. Tuy nhiên:
     * Có tới **19 file chứa thẻ HTML `<br>`** bên trong bảng Markdown (gây vỡ hiển thị trên thiết bị di động và vi phạm quy chuẩn kiểm định CI).
     * Chưa được chuẩn hóa sang cấu trúc 7 phần thống nhất của nhóm chứng chỉ.
   - **Cần Apply:**
     - Chạy script chuẩn hóa xóa sạch thẻ `<br>`, chuyển thành định dạng danh sách gạch đầu dòng hoặc tách dòng sạch trong Markdown.
     - Đồng bộ cấu trúc chuẩn đề thi KCCI (대한상공회의소).
3. **PMP (Project Management Professional - 25 files):**
   - **Hiện trạng:**
     * Chứa nhiều đoạn **dịch cơ học từng chữ (mechanical literal translation)** gây tối nghĩa, ví dụ: `"lần ghi nhận (commit / 커밋) vào một solution"`, `"đơn vị từ (token)"`.
     * Toàn bộ 17 bài học chính đều chứa các khối boilerplate tự sinh mẫu: `> **Nối mạch:** [Bài toán A] nối từ [Khái niệm B] sang [Khái niệm C], vì cơ chế trước tạo đầu vào cho bước sau.` lặp đi lặp lại một cách máy móc.
   - **Cần Apply:**
     - Xóa bỏ toàn bộ các khối boilerplate nối mạch tự sinh mẫu.
     - Viết lại câu văn chuyển mạch tự nhiên, diễn đạt rõ ràng tư duy quản trị dự án theo chuẩn PMBOK 7 & Agile Practice Guide.
     - Tăng cường các kịch bản tình huống thực tế (Scenario-based situational questions) vốn chiếm 80% đề thi PMP.
4. **증권투자기초 & Kế toán tài chính (66 files):**
   - **Hiện trạng:** Đang ở dạng tài liệu thô (raw book chapters), nhiều bài viết còn là bản dịch thô chưa có cấu trúc học tập và bài tập rèn luyện.
   - **Cần Apply:** Xây dựng khung bài giảng chuẩn hóa cho chứng chỉ Đầu tư Chứng khoán Hàn Quốc (증권투자권유대행인 / 투자자산운용사).

---

### 2. NHÓM KHOA HỌC MÁY TÍNH & KỸ THUẬT PHẦN MỀM (CS, DATA, DEVOPS, LINUX)

- **Quy mô:** Hơn 800 bài học bao quát từ Hệ điều hành, Mạng, Kiến trúc máy tính, Cấu trúc dữ liệu & Giải thuật, AI/ML, DevOps đến Linux.
- **Vấn đề cốt lõi phát hiện qua Audit:**
  1. **Boilerplate chuyển mạch rác diện rộng:**
     - **461 / 610 file** trong `computer_science` (75.5%) chứa mẫu chuyển mạch tự sinh cũ (`> **Nối mạch:** ... nối từ ... sang ... vì cơ chế trước tạo đầu vào...`).
     - **59 / 63 file** trong `linux` (93.7%) dính boilerplate tương tự.
     - **20 / 24 file** trong `devops_platform_engineering` (83.3%) dính boilerplate.
  2. **Văn phong dịch chắp vá từ vựng (Word-substitution artifact):**
     - Rất nhiều câu văn xuất hiện dạng: `"ngăn xếp (stack / 스택) buffer overflow kinh điển có thể overwrite return siêu dữ liệu (metadata / 메타데이터)"`, `"bản địa (native / 네이티브) libraries"`, `"Same mẫu (pattern / 패턴) xuất hiện..."`.
     - Cách viết này cản trở mạch đọc của người học, tạo cảm giác như một bản chạy script regex thay từ thay vì một bài giảng chuyên gia.
- **Cần Apply:**
  - **Xóa bỏ triệt để các khối `> **Nối mạch:**` rỗng.** Chỉ giữ lại phần chuyển mạch thực chất nằm trong dòng chảy tự nhiên của văn bản.
  - **Biên tập lại câu chữ (Naturalization):** Đưa thuật ngữ chuyên ngành về dạng tự nhiên: dùng trực tiếp thuật ngữ tiếng Anh chuẩn công nghệ (Stack buffer overflow, Native library, Metadata, Design pattern) kèm chú thích tiếng Hàn/Việt ở phần từ khóa đầu bài, tránh chèn ngoặc đơn 3 thứ tiếng ở mọi danh từ trong bài.
  - Bổ sung sơ đồ ASCII và mã nguồn thực thi (C/Python/Go) cho các bài học kiến trúc và hệ thống.

---

### 3. NHÓM HÀN QUỐC HỌC, HỘI NHẬP & PHÁP LUẬT (KIIP, KINH TẾ, PHÁP LUẬT)

- **Quy mô:** 251 bài học hỗ trợ kỳ thi Hội nhập Xã hội (KIIP) và hiểu biết sâu về thể chế Hàn Quốc.
- **Hiện trạng:**
  - `korea_business_economy_knowledge_library`: **58 / 63 file (92%)** dính các đoạn template: `> **Chuyển mạch:** Đặt trong câu hỏi lớn của... [Khái niệm A] tiếp nhận điểm tựa từ [Khái niệm B] nhưng đổi góc nhìn sang câu hỏi của chính nó...`
  - `kiip`: Nội dung chuẩn kiến thức chương trình Hội nhập Xã hội cấp 4 và cấp 5, nhưng cần tăng cường thêm hệ thống câu hỏi trắc nghiệm ôn thi quốc tịch / thường trú nhân.
- **Cần Apply:**
  - Xóa bỏ boilerplate chuyển mạch mẫu ở 58 file kinh tế Hàn Quốc.
  - Bổ sung bảng đối chiếu song ngữ Hàn - Việt cho toàn bộ thuật ngữ kinh tế, luật pháp và cơ quan hành chính Hàn Quốc (ví dụ: 출입국·외국인청, 고용노동부, 대법원, 국민건강보험).
  - Tích hợp đề thi thử trắc nghiệm mô phỏng kỳ thi Đánh giá Tổng hợp (종합평가).

---

### 4. NHÓM KHOA HỌC CƠ BẢN & XÃ HỘI NHÂN VĂN (TOÁN, LÝ, HÓA, TRIẾT HỌC, TÂM LÝ)

- **Quy mô:** Hơn 1,000 bài học.
- **Hiện trạng:**
  - Tỷ lệ dính boilerplate template tự sinh cực kỳ cao: Toán (91.8%), Vật lý (98.9%), Hóa học (93.3%), Sinh học (97.2%), Tâm lý học (98.0%), Lịch sử thế giới (96.4%).
  - Các khối boilerplate này chiếm diện tích nhưng không mang lại giá trị tri thức cho người đọc.
- **Cần Apply:**
  - Làm sạch tự động 100% boilerplate chuyển mạch rác trên toàn bộ các thư mục này.
  - Bảo tồn nguyên vẹn các công thức toán học, định lý, phản ứng hóa học và dẫn chứng lịch sử.
  - Định dạng lại các công thức KaTeX chuẩn: hiển thị khối công thức toán bằng `$$...$$` và công thức nội dòng bằng `$...$`.

---

## III. 5 NGUYÊN TẮC TIÊU CHUẨN CẦN APPLY TOÀN HỆ THỐNG

### Tiêu chuẩn 1: Cấu trúc Tài liệu Phân tầng (Tiered Document Architecture)
- **Đối với nhóm Chứng chỉ (Certs):** Bắt buộc tuân thủ chuẩn 7 phần:
  1. `## 1. Mục tiêu học tập (학습 목표)`
  2. `## 2. Thuật ngữ cốt lõi (핵심 키워드)`
  3. `## 3. Khung kiến thức tiên quyết & liên kết (선행·연결 개념)`
  4. `## 4. Hướng dẫn học theo mục tiêu (읽는 방법)`
  5. `## 5. TẦNG A: Cốt lõi thi cử & Bản đồ khái niệm (핵심 개념 & 시험 출제 포인트)`
  6. `## 6. TẦNG B: Phân tích chuyên sâu & Bản chất kỹ thuật (심층 분석 & 기술적 본질)`
  7. `## 7. Checklist ôn tập nhanh & Câu hỏi thi thử (복습 체크리스트 & 실전 기출 문제)`
- **Đối với nhóm Thư viện Tri thức (Knowledge Libraries):** Bắt buộc có phần tóm tắt cốt lõi, cơ chế giải thích nguyên lý vận hành, sơ đồ trực quan và ứng dụng thực tế.

### Tiêu chuẩn 2: Văn phong Chuyên gia & Tự nhiên hóa Ngôn ngữ (Natural Phrasing)
- Tuyệt đối chấm dứt việc thay thế từ ngữ máy móc (ví dụ: không viết `"Same mẫu (pattern / 패턴)"`, `"lần ghi nhận (commit)"`, `"đơn vị từ (token)"`).
- Diễn đạt trôi chảy bằng tiếng Việt chuyên ngành công nghệ / tài chính; thuật ngữ giữ nguyên tiếng Anh chuẩn quốc tế hoặc song ngữ Anh - Hàn - Việt trong bảng thuật ngữ chuyên biệt ở đầu hoặc cuối bài.

### Tiêu chuẩn 3: Không rác Chuyển mạch (Zero Automated Boilerplate)
- Cấm hoàn toàn các đoạn văn mẫu sinh tự động:
  - `> **Chuyển mạch:** ... tiếp nhận điểm tựa từ ... nhưng đổi góc nhìn sang câu hỏi của chính nó...`
  - `> **Nối mạch:** ... nối từ ... sang ..., vì cơ chế trước tạo đầu vào cho bước sau.`
  - `Ta vừa chốt ... bằng các điều kiện... Bây giờ ta đi vào nội dung...`
- Sự chuyển tiếp giữa các phần phải đến từ logic thực sự của nội dung kiến thức.

### Tiêu chuẩn 4: Chuẩn hóa Markdown & Tương thích Di động (Clean Markdown & Mobile-Friendly)
- Không sử dụng thẻ `<br>` hoặc `<mark>` bên trong các ô bảng Markdown.
- Không để khoảng trắng thừa cuối dòng (trailing whitespace = 0) để vượt qua `git diff --check`.
- Tất cả liên kết nội bộ phải tồn tại thực tế trên đĩa (0 broken links).

### Tiêu chuẩn 5: Quy hoạch Thư mục Tập trung (Centralized Directory Structure)
- Tập trung toàn bộ tài liệu ôn thi chứng chỉ vào thư mục `cert/`:
  - `cert/정보처리기사/`
  - `cert/sqld/`
  - `cert/컴퓨터활용능력/`
  - `cert/pmp/`
  - `cert/증권투자기초/`

---

## IV. LỘ TRÌNH THỰC HIỆN NÂNG CẤP (ACTIONABLE ROADMAP)

```
[Phase 1: Chuẩn hóa nhóm Cert & Xử lý Comhwal]
  │── Di chuyển / Quy hoạch chứng chỉ vào cert/
  │── Dọn sạch 19 file có thẻ <br> trong 컴퓨터활용능력
  └── Kiểm tra liên kết và build thư viện
         ▼
[Phase 2: Quét sạch Boilerplate rác trên toàn bộ Thư viện]
  │── Làm sạch 461 file Computer Science
  │── Làm sạch 58 file Kinh tế Hàn Quốc
  └── Làm sạch các môn Toán, Lý, Hóa, Tâm lý, Lịch sử (>600 files)
         ▼
[Phase 3: Tự nhiên hóa Văn phong & Nâng cấp Kỹ thuật PMP]
  │── Biên tập lại câu văn chắp vá, dịch cơ học trong PMP và CS
  └── Bổ sung bài tập tình huống thực chiến cho PMP
         ▼
[Phase 4: Chuẩn hóa Chứng khoán & Kế toán Hàn Quốc]
  │── Biên soạn lại 증권투자기초 từ raw notes thành các bài học chuẩn hóa
  └── Xây dựng bộ câu hỏi ôn thi chứng chỉ tài chính
         ▼
[Phase 5: Thiết lập Hệ thống Kiểm toán CI Tự động Toàn diện]
  │── Mở rộng scripts/run_quality_audit.py bao phủ toàn bộ kho tài liệu
  └── Tự động hóa kiểm tra Zero Boilerplate & Clean Markdown trên GitHub Actions
```

### Kế hoạch hành động cụ thể cho từng Phase:

1. **Giai đoạn 1: Tập trung hoàn thiện toàn bộ nhóm Cert (Thời gian dự kiến: 1-2 đợt làm việc)**
   - Tổ chức lại thư mục `cert/` thống nhất.
   - Xóa bỏ toàn bộ thẻ `<br>` trong `cert/컴퓨터활용능력/` và kiểm tra lại `git diff --check`.
   - Bổ sung cấu trúc thi cử và bộ câu hỏi trắc nghiệm cho Comhwal 1급 & 2급.

2. **Giai đoạn 2: Chiến dịch "Dọn sạch Boilerplate" (Zero-Boilerplate Campaign)**
   - Sử dụng script python thông minh bóc tách và loại bỏ an toàn các khối `> **Chuyển mạch:**` và `> **Nối mạch:**` rỗng mà không làm mất nội dung kiến thức cốt lõi.
   - Đo lường và kiểm toán sự thay đổi: đảm bảo 100% nội dung học tập được bảo toàn nguyên vẹn.

3. **Giai đoạn 3: Tinh chỉnh văn phong & Nâng cấp chuyên sâu PMP**
   - Viết lại các thuật ngữ dịch máy bị lỗi trong PMP.
   - Thêm phần cạm bẫy thi cử PMBOK 7 và Agile Practice Guide.

---

## V. KẾT LUẬN & ĐỀ XUẤT HÀNH ĐỘNG TIẾP THEO

Kho tài liệu `00.my-learning` đang sở hữu khối lượng tri thức đồ sộ và chất lượng rất cao ở các phần trọng điểm đã nâng cấp (`정보처리기사` và `SQLD`). Việc áp dụng các chuẩn mực trên sẽ đưa toàn bộ kho tài liệu lên cùng một đẳng cấp: **Chuyên nghiệp, Không rác template, Tự nhiên trong diễn đạt và Tối ưu tối đa cho người học thi chứng chỉ cũng như tra cứu chuyên sâu.**

**Đề xuất hành động ngay:**
Bạn có muốn tôi tiến hành ngay **Phase 1** (Quy hoạch thư mục `cert/`, làm sạch 19 file có thẻ `<br>` trong `컴퓨터활용능력` và nâng cấp chuẩn hóa chứng chỉ này) không?
