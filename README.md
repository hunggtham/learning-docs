# Learning Docs

Kho tài liệu học được tổ chức theo từng chủ đề. Mỗi bộ có nguồn gốc (`raw`/`raw_md`), script generate và thư mục `output` đã chuẩn hóa để học.

## Bộ tài liệu

- [정보처리기사](정보처리기사/output/README.md): 5 môn, tài liệu Hàn–Anh–Việt, sắp xếp theo mạch kiến thức.
- [SQLD](sql/output/README.md): mô hình dữ liệu và SQL cơ bản/nâng cao, có ví dụ truy vấn và quy tắc dễ nhầm.
- [Mathematics Master Knowledge Book](mathematics/README.md): 87 chủ đề Toán theo conceptual dependency và first-principles, có glossary Việt–Anh–Hàn, knowledge connections và coverage audit; bao phủ thêm analysis, tensor/autodiff, stochastic processes, Bayesian inference và dynamic programming/control.
- [Physics Knowledge Library](physics/README.md): thư viện Vật lý theo conceptual dependency từ phép đo, cơ học, sóng, chất lưu, nhiệt, điện từ và quang học đến tương đối tính, lượng tử, nguyên tử–hạt nhân, vật chất ngưng tụ, điện tử và vật lý thiên văn; có knowledge connections và depth/coverage audit.
- [Biology Knowledge Library](biology/README.md): thư viện Sinh học tổ chức theo conceptual boundary từ hóa học của sự sống, tế bào, di truyền, tiến hóa và vi sinh vật đến sinh lý cơ thể, sinh thái, công nghệ sinh học, bioinformatics và systems biology; dùng thuật ngữ Việt–Anh–Hàn, mental model, mathematical connections và coverage audit.
- [Computer Science Knowledge Library](computer_science/README.md): namespace Computer Science; phần **Basic/Foundation** gồm 100 topic chapters được đặt tại `computer_science/basic/`, còn các library chuyên sâu như Data Structures & Algorithms được tách riêng để không trộn foundation với advanced knowledge.
- [Korean History Master Knowledge Book](korean_history/README.md): lịch sử bán đảo Triều Tiên từ tiền sử đến Hàn Quốc đương đại, kèm social/economic/technology history và quy ước tên Việt–Hàn–Anh.
- [Korean Culture Master Knowledge Book](korean_culture/README.md): văn hóa Hàn Quốc theo lịch sử, quan hệ, gia đình, giáo dục, công sở, ẩm thực, nghệ thuật, vùng miền, Hallyu và xã hội hiện đại; bên trong có [`korean_culture/kiip/`](korean_culture/kiip/README.md) làm lớp ôn KIIP `한국사회 이해`, tổng hợp `공통` và đánh dấu trực tiếp các phần `귀화용 심화` thay vì tách hai bộ note.
- [Native Mobile Development](11_native/00_INDEX.md): lộ trình Swift/iOS và Kotlin/Android từ Beginner → Intermediate → Advanced/Senior → Master, gồm cả modern stack, legacy interoperability và production engineering.
- [Investing Knowledge Library](investing/README.md): thư viện đầu tư hoàn chỉnh theo 6 domain chính — Foundations, Asset Classes, Company Analysis, Economics, Trading & Derivatives, Korea & Vietnam Markets — cộng glossary/quy chuẩn nghiên cứu, Advanced Labs, [Advanced Depth Path](investing/ADVANCED_DEPTH_PATH.md), [Advanced Practice Workbook](investing/ADVANCED_PRACTICE_WORKBOOK.md) và capstone tích hợp từ thesis → mô hình → định giá → vị thế → thực thi → review.
- [Study Planner](planner/study-planner/README.md): ứng dụng lập kế hoạch học tập đồng bộ Supabase.
- [Study Library](learning-library/README.md): trình đọc Markdown/PDF tĩnh cho GitHub Pages.

## Quy ước biên soạn

- Giữ thuật ngữ gốc để đối chiếu đề thi, kèm English và nghĩa tiếng Việt khi có thể.
- Trình bày theo thứ tự: khái niệm → cơ chế/quy tắc → so sánh → ví dụ → ôn tập.
- Không sửa nguồn thô; mọi bản học được tạo lại bằng script tương ứng trong `scripts/`.
