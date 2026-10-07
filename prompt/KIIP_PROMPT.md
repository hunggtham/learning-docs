# KIIP CONTENT PROMPT — 한국사회통합프로그램 Knowledge Foundation

Áp dụng prompt này cho toàn bộ tài liệu trong `korean_culture/kiip/`, đồng thời tuân thủ `prompt/COMMON_PROMPT.md`.

## 1. Mục tiêu

Xây KIIP thành một nền tảng kiến thức về xã hội Hàn Quốc có thể đọc như giáo trình độc lập, không phải bộ note học thuộc. Người học phải hiểu đủ sâu để vừa thi KIIP, vừa hiểu bối cảnh mà một người Hàn có giáo dục phổ thông thường liên tưởng khi gặp khái niệm đó.

Ưu tiên:

Understanding > Memorization  
Reasoning > Rule  
Mechanism > isolated fact  
Connection > isolated keyword  
Historical/social context > bare definition

## 2. Ngôn ngữ

- Khoảng 80% phần giải thích phải là tiếng Việt tự nhiên.
- Khoảng 15–20% là tiếng Hàn dành cho thuật ngữ gốc, tên người, tên cơ quan, sự kiện, địa danh, câu KIIP và cách diễn đạt người Hàn thực sự dùng.
- Tiếng Anh chỉ giữ khi chính thuật ngữ/tên riêng tiếng Anh có giá trị, ví dụ `Auld Lang Syne`. Không dùng tiếng Anh làm ngôn ngữ giải thích khi tiếng Việt diễn đạt được.
- Tuyệt đối không tạo câu lai kiểu `Mugunghwa appears in công cộng...`, `Why these biểu tượngs...`, `vớiout`, `thiết kếation`.
- Không dùng replace hàng loạt theo từ nếu có nguy cơ sửa một phần bên trong từ tiếng Anh hoặc phá ngữ pháp.
- Sau mỗi lần sửa phải đọc lại câu hoàn chỉnh, không chỉ kiểm tra keyword.

## 3. Kiến trúc canonical

`korean_culture/kiip/lessons/` là nguồn kiến thức canonical.

Mỗi `01과 → 50과` là một bài độc lập và phải đủ kiến thức để hiểu ngay tại chỗ. Các file tổng hợp, keyword, active recall, mock test và cross-reference chỉ được rút ra từ canonical lessons; không được chứa kiến thức nền quan trọng chỉ tồn tại ở file phụ.

Internal link là đường đọc sâu thêm, không phải điều kiện bắt buộc để hiểu bài hiện tại.

## 4. Vertical completeness — đào sâu từng concept

Khi đã nhắc đến một khái niệm, nhân vật, tổ chức, sự kiện hoặc biểu tượng quan trọng, không được bỏ nó ở mức một câu định nghĩa.

Tùy bản chất concept, phải giải thích đủ các lớp liên quan:

1. Nó là gì?
2. Nó xuất hiện để giải quyết vấn đề gì?
3. Ai/cơ quan nào liên quan?
4. Mốc thời gian nào quan trọng?
5. Bối cảnh lịch sử/xã hội lúc đó là gì?
6. Nó hình thành bằng quá trình nào?
7. Tại sao lại hình thành theo cách đó?
8. Nó thay đổi ra sao theo thời gian?
9. Có nhiều phiên bản/giai đoạn/cách hiểu hay không?
10. Có tranh luận hoặc attribution chưa chắc chắn không?
11. Địa vị pháp lý/chính thức khác gì tập quán xã hội?
12. Hiện nay nó được dùng/hiểu như thế nào?
13. Người Hàn thường liên tưởng gì khi nghe keyword này?
14. KIIP có thể hỏi phần nào?

Nếu không tồn tại câu trả lời đơn giản cho “ai chọn?”, “năm nào?”, “ai sáng tác?”, phải giải thích chính sự không chắc chắn đó. Không được bịa một người hoặc một mốc cho dễ học.

## 5. Horizontal completeness — concept neighborhood

Một concept không được đứng cô lập. Phải mở rộng các node xung quanh có giá trị kiến thức phổ thông.

Ví dụ:

`서울`
→ `수도`
→ `서울특별시`
→ `수도권`
→ lịch sử `한양`
→ `경복궁·창덕궁·종묘·광화문`
→ vai trò chính trị/kinh tế/văn hóa
→ quan hệ với `경기·인천`.

Với địa lý, ưu tiên mạng:

`지역 → 행정구역 → 위치/지형 → 역사 → 산업 → 도시 → 관광지 → 음식/특산물 → 문화 → người Hàn liên tưởng gì → vùng dễ nhầm/lân cận`.

Với lịch sử:

`bối cảnh trước → nguyên nhân → nhân vật/chủ thể → sự kiện → diễn biến → kết quả → hệ quả dài hạn → sự kiện tiếp theo`.

Với chính trị/pháp luật:

`vấn đề cần giải quyết → nguyên tắc → thiết chế → quyền hạn → giới hạn → kiểm soát quyền lực → ví dụ đời sống → ngoại lệ/current facts`.

Với kinh tế:

`nguyên nhân → cơ chế → chủ thể → dòng tiền/hàng hóa/quyền lợi → kết quả → tác dụng phụ → ví dụ Hàn Quốc`.

## 6. Cách viết

Viết như một giảng viên đang dẫn người học qua một chapter hoàn chỉnh.

Không viết kiểu glossary kéo dài:

`A = ...`  
`B = ...`  
`C = ...`

mà phải tạo reasoning chain.

Ví dụ không dừng ở:

`세종대왕 → 한글`.

Phải đi đến:

`한문 중심 문자생활의 한계 → 백성이 글을 쓰기 어려움 → 세종 → 1443 창제 → 1446 반포/해례 → 28자와 제자 원리 → 집현전의 역할 → 최만리의 반대 → 점진적 사회 확산 → 1894 국문 지위 강화 → 일제강점기의 언어 보존 → 현대 한국의 문화적 정체성`.

Không lạm dụng câu meta như “Nối mạch”, “Chuyển mạch”, “Ở chặng này”. Quan hệ phải xuất hiện tự nhiên trong nội dung.

## 7. Accuracy và current facts

- Ưu tiên nguồn chính thức của Hàn Quốc cho luật, thiết chế, biểu tượng quốc gia, lịch sử chính thức và số liệu hiện hành.
- Phân biệt rõ historical fact, disputed attribution, social convention và legal designation.
- Luật, ngưỡng tiền, điều kiện visa/phúc lợi, cơ cấu tổ chức và số liệu có thể thay đổi phải được coi là mutable facts.
- Không biến thông tin hiện hành thành chân lý vĩnh viễn.
- Khi cần, đồng bộ với `00_current_facts_and_corrections.md`.

## 8. KIIP exam layer

Mỗi bài phải có phần giúp chuyển kiến thức sâu thành output thi:

- keyword cần nhận diện;
- contrast dễ nhầm;
- câu hỏi KIIP có thể gặp;
- câu trả lời tiếng Hàn tự nhiên;
- follow-up question;
- lỗi trả lời thường gặp.

Câu trả lời thi có thể ngắn, nhưng tài liệu nền phía trước phải sâu.

## 9. Quality gate bắt buộc trước commit

Trước khi commit một lesson:

1. Đọc lại toàn bộ file như một bài viết, không chỉ grep keyword.
2. Tìm câu trộn Việt–Anh–Hàn bất thường.
3. Tìm từ bị hỏng do replace như `vớiout`, `thiết kếation`, hậu tố tiếng Anh gắn vào từ Việt/Hàn.
4. Kiểm tra mọi heading đều tự nhiên.
5. Kiểm tra mỗi concept quan trọng có vertical context.
6. Kiểm tra concept neighborhood đủ để không phải Google kiến thức nền.
7. Kiểm tra mốc thời gian, người, cơ quan và attribution.
8. Kiểm tra internal links nếu có.
9. Đảm bảo file phụ không sở hữu kiến thức nền mà canonical lesson chưa giải thích.
10. Chỉ đánh dấu hoàn thành khi người học có thể đọc lesson độc lập.

## 10. Definition of done

Một bài KIIP chỉ hoàn thành khi:

- người mới có thể đọc từ đầu và hiểu;
- người đã biết cơ bản vẫn học thêm được context và mechanism;
- người ôn KIIP có thể rút ra keyword/câu trả lời;
- không cần mở nguồn khác chỉ để hiểu prerequisite quan trọng;
- không có prose tiếng Anh không cần thiết;
- không có câu lai hoặc từ bị hỏng;
- các concept quan trọng được giải thích cả chiều sâu lẫn mạng liên hệ.

## Điều phối task mới

Trước mỗi task, đọc prompt/00_ORCHESTRATOR_PROMPT.md và task manifest. Với corpus có raw/source, chạy INGEST → PLAN → PILOT trước khi fan-out lesson. Dùng prompt/ACCEPTANCE_CONTRACT.md để tách content, evidence, Git và publication status.
