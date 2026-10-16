# FOREIGN CERT BILINGUAL PROMPT — Tiêu chuẩn tài liệu chứng chỉ thi bằng tiếng Hàn / tiếng Anh

Áp dụng prompt này kết hợp với `prompt/COMMON_PROMPT.md` và `AGENTS.md` cho toàn bộ tài liệu ôn thi các chứng chỉ quốc tế / chuyên môn có ngôn ngữ đề thi là **tiếng Hàn** (như 정보처리기사, 컴퓨터활용능력 1급/2급, SQLD/SQLP, 한국사...) hoặc **tiếng Anh** (như AWS, CKA, PMP, CFA, CompTIA...).

Mục tiêu cốt lõi: Đảm bảo người học khi vào phòng thi **nhận diện tức thì thuật ngữ và mẫu câu đề thi gốc (Hàn/Anh)**, đồng thời **hiểu sâu sắc bản chất kỹ thuật qua phần giải thích tiếng Việt song song**.

---

## 1. Nguyên tắc song ngữ song song (Bilingual Pairing)

### 1.1. Thứ tự ưu tiên ngôn ngữ
1. **Ngôn ngữ gốc của kỳ thi (Korean hoặc English) đi TRƯỚC**:
   - Dùng chính xác văn phong, cụm từ ra đề của cơ quan khảo thí (KORCHAM, Kdata, HRDK, AWS, PMI...).
   - Đưa ra định nghĩa nén, câu chốt lý thuyết, hoặc mệnh đề điều kiện bằng ngôn ngữ thi thật.
2. **Giải thích kỹ thuật tiếng Việt đi NGAY SAU**:
   - Giải thích bản chất cơ chế, lý do vì sao đúng/sai, trường hợp biên (edge cases) và mẹo phân biệt.
   - Viết tự nhiên, chính xác về mặt kỹ thuật, không dịch thô (word-by-word) làm méo mó tư duy kỹ thuật.

### 1.2. Mẫu định dạng chuẩn (Canonical Patterns)

- **Thuật ngữ & Từ khóa (Keywords):**
  - Mẫu thi tiếng Hàn: `한국어 (English/Acronym) — Giải thích kỹ thuật tiếng Việt`
    *Ví dụ:* `참조무결성 (Referential Integrity) — Ràng buộc toàn vẹn tham chiếu: Giá trị khóa ngoại phải tồn tại ở khóa chính hoặc mang giá trị NULL.`
  - Mẫu thi tiếng Anh: `English (Korean nếu có) — Giải thích kỹ thuật tiếng Việt`
    *Ví dụ:* `Deadlock (교착 상태) — Trạng thái khóa chết: Hai hay nhiều tiến trình chờ đợi tài nguyên do nhau nắm giữ vô hạn định.`

- **Khái niệm & Điểm thi trọng tâm (Core Exam Principles):**
  - Trình bày một câu/đoạn ngắn bằng tiếng Hàn (hoặc tiếng Anh) mang đúng văn phong câu hỏi thi.
  - Ngay bên dưới là phân tích chi tiết bằng tiếng Việt:
    ```markdown
    - **핵심 원리 (Nguyên tắc cốt lõi):**
      - [Hàn/Anh]: `외래키(FK) 값은 참조하는 테이블의 기본키(PK) 값과 일치하거나 NULL이어야 한다.`
      - [Tiếng Việt]: Khóa ngoại không bao giờ được phép trỏ tới một bản ghi không tồn tại trong bảng cha. Khi xóa dữ liệu ở bảng cha có ràng buộc `RESTRICT`, thao tác sẽ bị chặn đứng; nếu chọn `CASCADE`, dữ liệu con sẽ bị xóa theo.
    ```

### 1.3. Những điều tuyệt đối cấm về ngôn ngữ
- **Cấm đơn ngữ hóa hoàn toàn**: Không viết 100% tiếng Việt mà bỏ sót thuật ngữ gốc (khiến người học đi thi không đọc hiểu đề). Không để 100% tiếng Hàn/Anh đơn ngữ không có giải thích tiếng Việt.
- **Cấm tự dịch tên hàm, API, cú pháp, mã lệnh**: Tên hàm Excel (`VLOOKUP`, `INDEX`, `MATCH`), lệnh SQL (`SELECT`, `JOIN`, `GROUP BY`), phương thức code, khóa bảo mật phải giữ nguyên 100%.

---

## 2. Quy tắc chuyển mạch & câu nối sư phạm (Pedagogical Transitions)

Mỗi file tài liệu và từng phần lớn (`##`, `###`) phải giữ được mạch tư duy học tập liên tục, tuân thủ nghiêm ngặt mô hình 3 vế:

1. **Từ đâu (Origin / Prerequisite):**
   - Chỉ rõ kiến thức nền tảng, bài học trước, hoặc điều kiện tiền đề vừa học.
2. **Đang giải quyết gì (Current Problem):**
   - Đặt vấn đề kỹ thuật hoặc câu hỏi trọng tâm mà phần hiện tại sẽ giải quyết (tại sao phải cần cơ chế này? đề thi thường bẫy điểm nào?).
3. **Dùng đi đâu (Forward Handoff):**
   - Bàn giao kết quả phân tích sang bài học kế tiếp theo quan hệ logic: `kế thừa`, `mở rộng`, `đối chiếu`, `áp dụng thực hành` hoặc `nguyên nhân – hệ quả`.

### ⚠️ Nghiêm cấm câu nối rỗng (Boilerplate Prohibition)
Tuyệt đối không chèn các câu khuôn mẫu vô nghĩa như:
- ❌ *"Phần này nối khái niệm vừa học với..., giúp người mới hiểu mục đích..."* (Khuôn mẫu sáo rỗng lặp lại).
- ❌ *"Xem tiếp phần sau"*, *"Dưới đây là chi tiết"*, *"Ta chuyển sang mục kế tiếp"*.
- ✅ Mỗi câu nối phải chứa thuật ngữ và quan hệ kỹ thuật thực tế của chính chủ đề đó.

---

## 3. Khả năng hiển thị tối ưu trên thiết bị di động (Mobile-Friendly Tables & Layout)

Tài liệu học tập thường xuyên được người học ôn luyện trên điện thoại di động (smartphone/tablet).

### 3.1. Hướng dẫn thiết kế bảng Markdown
- **Giới hạn số cột**: Bảng Markdown trên mobile chỉ hiển thị tốt với tối đa **3 đến 4 cột**.
- **Nội dung ô súc tích**: Tránh nhồi nhét cả một đoạn văn dài vào một ô trong bảng.
- **Phương án thay thế cho bảng rộng (> 4 cột)**:
  - Tách thành các danh sách bullet có cấu trúc rõ ràng hoặc định dạng Card.
  - Sử dụng các khối `###` hoặc `####` con cho từng đối tượng so sánh.
  - Ví dụ chuyển đổi:
    ```markdown
    #### 1. Trạng thái A (상태 A)
    - **Ý nghĩa (의미):** ...
    - **Điều kiện kích hoạt (발생 조건):** ...
    - **Bẫy đề thi (시험 함정):** ...
    ```

---

## 4. Kiểm chứng kỹ thuật & Tuân thủ AGENTS.md

- **Không bịa đặt (Zero Hallucination):** Mọi công thức, trọng số điểm, phiên bản phần mềm (ví dụ Excel 2021 LTSC cho 컴활), bẫy trắc nghiệm phải đối chiếu với công bố chính thức của cơ quan khảo thí. Nếu chưa xác minh, đánh dấu `UNVERIFIED` hoặc `NEEDS_SOURCE`.
- **Cấm công cụ tự động sinh văn phong (No Automation Prose Injection):** Không dùng script Python, JS, regex để tự động chèn câu chuyển tiếp, mở đầu, kết luận hàng loạt.
- **Không chèn câu hỏi thi trắc nghiệm vào canonical docs:** Tuân thủ `COMMON_PROMPT.md`, tài liệu học chuẩn (canonical) tập trung vào bản chất kiến thức và chiến lược giải quyết vấn đề, không chèn các khối quiz/mock test ngắn làm rác kho tri thức.
