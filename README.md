# Learning Docs

Kho tài liệu học được tổ chức theo từng chủ đề. Mỗi bộ có nguồn gốc (`raw`/`raw_md`), script generate và thư mục `output` đã chuẩn hóa để học.

## Bộ tài liệu

Phần này là bản đồ của toàn bộ kho học tập. Hãy chọn một bộ theo mục tiêu, rồi đi vào tài liệu liên quan để theo dõi mạch khái niệm → cơ chế → ví dụ → ôn tập.

- [정보처리기사](정보처리기사/output/README.md): 5 môn, tài liệu Hàn–Anh–Việt, sắp xếp theo mạch kiến thức.
- [SQLD](sql/output/README.md): mô hình dữ liệu và SQL cơ bản/nâng cao, có ví dụ truy vấn và quy tắc dễ nhầm.
- [Mathematics Master Knowledge Book](mathematics/README.md): 87 chủ đề Toán theo conceptual dependency và first-principles, có glossary Việt–Anh–Hàn, knowledge connections và coverage audit; bao phủ thêm analysis, tensor/autodiff, stochastic processes, Bayesian inference và dynamic programming/control.
- [Physics Knowledge Library](physics/README.md): thư viện Vật lý theo conceptual dependency từ phép đo, cơ học, sóng, chất lưu, nhiệt, điện từ và quang học đến tương đối tính, lượng tử, nguyên tử–hạt nhân, vật chất ngưng tụ, điện tử và vật lý thiên văn; có knowledge connections và depth/coverage audit.
- [Biology Knowledge Library](biology/README.md): thư viện Sinh học tổ chức theo conceptual boundary từ hóa học của sự sống, tế bào, di truyền, tiến hóa và vi sinh vật đến sinh lý cơ thể, sinh thái, công nghệ sinh học, bioinformatics và systems biology; dùng thuật ngữ Việt–Anh–Hàn, mental model, mathematical connections và coverage audit.
- [Computer Science Knowledge Library](computer_science/README.md): namespace Computer Science; phần **Basic/Foundation** gồm 100 topic chapters được đặt tại `computer_science/basic/`, còn các library chuyên sâu như Data Structures & Algorithms được tách riêng để không trộn foundation với advanced knowledge.
- [JavaScript Knowledge Library](10_frontend/javascript/javascript_beginner_rebuilt.md): lộ trình JavaScript Vietnamese-first từ [Beginner](10_frontend/javascript/javascript_beginner_rebuilt.md) → [Intermediate](10_frontend/javascript/javascript_intermediate.md) → [Senior](10_frontend/javascript/javascript_senior.md) → [Master](10_frontend/javascript/javascript_master_supplement_detailed.md), tập trung execution model, scope/closure, `this`/prototype, Promise/event loop, browser runtime, modern-vs-legacy evolution, memory/performance, security và production engineering.
- [Korean History Master Knowledge Book](korean_history/README.md): lịch sử bán đảo Triều Tiên từ tiền sử đến Hàn Quốc đương đại, kèm social/economic/technology history và quy ước tên Việt–Hàn–Anh.
- [Korean Culture Master Knowledge Book](korean_culture/README.md): văn hóa Hàn Quốc theo lịch sử, quan hệ, gia đình, giáo dục, công sở, ẩm thực, nghệ thuật, vùng miền, Hallyu và xã hội hiện đại; bên trong có [`korean_culture/kiip/`](korean_culture/kiip/README.md) làm lớp ôn KIIP `한국사회 이해`, tổng hợp `공통` và đánh dấu trực tiếp các phần `귀화용 심화` thay vì tách hai bộ note.
- [Korea Law, Civic & Everyday Life Knowledge Library](korea_law_civic_life/README.md): hệ thống pháp luật, cơ cấu công quyền và các quy trình đời sống tại Hàn Quốc cho người nước ngoài; bao phủ lao động, nhà ở, thuế, `4대보험`, tài chính, xuất nhập cảnh, `민원` và kỹ năng tự tra nguồn chính thức.
- [Native Mobile Development](11_native/00_INDEX.md): lộ trình Swift/iOS và Kotlin/Android từ Beginner → Intermediate → Advanced/Senior → Master, gồm cả modern stack, legacy interoperability và production engineering.
- [Investing Knowledge Library](investing/README.md): thư viện đầu tư hoàn chỉnh theo 6 domain chính — Foundations, Asset Classes, Company Analysis, Economics, Trading & Derivatives, Korea & Vietnam Markets — cộng glossary/quy chuẩn nghiên cứu, Advanced Labs, [Advanced Depth Path](investing/ADVANCED_DEPTH_PATH.md), [Advanced Practice Workbook](investing/ADVANCED_PRACTICE_WORKBOOK.md) và capstone tích hợp từ thesis → mô hình → định giá → vị thế → thực thi → review.
- [Study Planner](planner/study-planner/README.md): ứng dụng lập kế hoạch học tập đồng bộ Supabase.
- [Study Library](learning-library/README.md): trình đọc Markdown/PDF tĩnh cho GitHub Pages.

## Quy ước biên soạn

Các quy ước dưới đây giải thích cách đọc, cách cập nhật và cách phân biệt nguồn thô với bản học đã được chuẩn hóa.

- Giữ thuật ngữ gốc để đối chiếu đề thi, kèm English và nghĩa tiếng Việt khi có thể.
- Trình bày theo thứ tự: khái niệm → cơ chế/quy tắc → so sánh → ví dụ → ôn tập.
- Không sửa nguồn thô; mọi bản học được tạo lại bằng script tương ứng trong `scripts/`.

## Lecture contract cho tài liệu học

Mọi chapter hoặc section đang dạy kiến thức phải được viết như một buổi giảng ngắn cho người mới, không chỉ như danh sách header và ghi chú. Mỗi khối cần có:

1. **Định vị:** người học cần biết gì trước, câu hỏi hiện tại là gì và phần này nối với phần trước ở đâu.
2. **Giải thích có liên kết:** đi từ đối tượng/mục tiêu → cơ chế hoặc ràng buộc → hệ quả; bullet, bảng, công thức và ví dụ phải được dẫn vào và tổng hợp lại bằng prose.
3. **Chốt và bàn giao:** nêu mental model hoặc boundary vừa hình thành, điểm dễ nhầm nếu có, rồi nói rõ phần kế tiếp sẽ dùng, mở rộng hay đối chiếu điều gì.

Không được đạt contract bằng cách lặp một câu wrapper quanh mọi header. Header chỉ là nhãn điều hướng; câu hỏi, quan hệ giữa các ý và kết luận phải được viết theo nội dung thật của topic. Glossary, index, atlas profile và bảng tra cứu thuần tham chiếu có thể ngắn hơn, nhưng phải chỉ rõ cách dùng và đường quay lại phần giảng giải.

Contract chi tiết và các prompt sinh/QA nằm tại [`prompt/COMMON_PROMPT.md`](prompt/COMMON_PROMPT.md). Các corpus có generator phải sửa source hoặc generator rồi tái sinh và audit, không sửa tay từng output.
