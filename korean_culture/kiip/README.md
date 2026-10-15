# KIIP — 한국사회 이해 Exam Library

Bộ tài liệu này phục vụ ôn thi `한국사회이해 5단계` (Chương trình Hội nhập Xã hội Hàn Quốc — KIIP), với mục tiêu **đọc để hiểu bản chất và cơ chế của hệ thống xã hội Hàn Quốc, từ đó chuyển hóa thành năng lực thi cử vững chắc**.

## 1. Cấu trúc học tập và phạm vi chính thức

Theo quy định của Bộ Tư pháp Hàn Quốc (법무부):
- **영주용 (Thường trú):** 70 giờ chương trình cơ bản (기본과정);
- **귀화용 (Nhập tịch):** 100 giờ, gồm 70 giờ cơ bản cộng thêm 30 giờ nâng cao (심화과정).

Để đảm bảo học đúng trọng tâm và không bỏ sót nội dung, repository thiết lập hệ thống bản đồ và danh mục kiểm tra chuẩn:

1. [`00_official_textbook_map.md`](00_official_textbook_map.md) — **Bản đồ 50 bài học chính thức (제1과 ~ 제50과)** theo giáo trình chuẩn của Bộ Tư pháp, trỏ trực tiếp đến 50 bài học độc lập tại `lessons/`.
2. [`18_귀화용_심화_official_map.md`](18_귀화용_심화_official_map.md) — **Bản đồ 20 bài học nâng cao chính thức (심화 20과)** dành cho đối tượng thi nhập tịch (국적/귀화).
3. [`17_complete_exam_coverage_checklist.md`](17_complete_exam_coverage_checklist.md) — **Danh mục kiểm tra độ bao phủ toàn diện**, kiểm soát 4 tầng năng lực: Recognition (Nhận diện) → Recall (Tự nhớ) → Contrast (Phân biệt bẫy) → Explanation (Giải thích bằng tiếng Hàn).
4. [`19_official_basic_gap_supplement.md`](19_official_basic_gap_supplement.md) — **Tài liệu bổ sung các chủ đề cơ bản**, giải thích chi tiết các bài học còn thiếu hoặc mỏng trong tài liệu tóm tắt cũ.

---

## 2. 50 bài học chuẩn (Canonical Lessons)

50 bài học tại `lessons/01_...` đến `lessons/50_...` là nguồn kiến thức cốt lõi, giải thích cặn kẽ từng khái niệm và cơ chế:

| Lĩnh vực | Bài chính thức | Thư mục bài học | Trọng tâm nội dung |
|---|---:|---|---|
| 사회 1 | 1~8 | [`lessons/01_대한민국과_국가상징.md`](lessons/01_대한민국과_국가상징.md) ~ [`lessons/08_의료와_안전.md`](lessons/08_의료와_안전.md) | Quốc gia & biểu tượng, gia đình, nơi làm việc, giao thông & truyền thông, nhà ở, đô thị & nông thôn, phúc lợi xã hội, y tế & an toàn |
| 사회 2 | 9~12 | [`lessons/09_보육과_유아교육.md`](lessons/09_보육과_유아교육.md) ~ [`lessons/12_평생교육.md`](lessons/12_평생교육.md) | Chăm sóc & giáo dục mầm non, hệ thống trường học 6-3-3, nhiệt huyết giáo dục & đại học, giáo dục suốt đời |
| 문화 | 13~19 | [`lessons/13_전통가치와_공동체.md`](lessons/13_전통가치와_공동체.md) ~ [`lessons/19_여가문화와_워라밸.md`](lessons/19_여가문화와_워라밸.md) | Giá trị truyền thống, ẩm thực - trang phục - nhà ở, lễ nghi vòng đời, ngày lễ tết, tôn giáo, văn hóa đại chúng & Hallyu, văn hóa giải trí |
| 정치 | 20~24 | [`lessons/20_민주정치.md`](lessons/20_민주정치.md) ~ [`lessons/24_선거와_지방자치.md`](lessons/24_선거와_지방자치.md) | Nền chính trị dân chủ, Quốc hội, Chính phủ hành pháp, Tòa án & Tòa án Hiến pháp, Bầu cử & tự quản địa phương |
| 경제 | 25~29 | [`lessons/25_경제활동과_시장.md`](lessons/25_경제활동과_시장.md) ~ [`lessons/29_취업과_노동시장.md`](lessons/29_취업과_노동시장.md) | Hoạt động kinh tế & thị trường, tăng trưởng kinh tế Hàn Quốc, tiêu dùng & bảo vệ người tiêu dùng, tài chính, việc làm & thị trường lao động |
| 법 | 30~36 | [`lessons/30_왜_법이_필요한가.md`](lessons/30_왜_법이_필요한가.md) ~ [`lessons/37_생활안전과_법률지원.md`](lessons/37_생활안전과_법률지원.md) | Vai trò của pháp luật, xuất nhập cảnh & cư trú, quốc tịch & nhập tịch, luật gia đình, tài sản & hợp đồng, tố tụng hình sự, hỗ trợ pháp luật |
| 역사 | 37~43 | [`lessons/38_고조선과_고대국가.md`](lessons/38_고조선과_고대국가.md) ~ [`lessons/44_광복과_한국전쟁.md`](lessons/44_광복과_한국전쟁.md) | Cổ Triều Tiên & các quốc gia cổ đại, Tam quốc & Nam Bắc quốc, Goryeo, Joseon, Mở cảng & Đế quốc Đại Hàn, Kháng Nhật, Giải phóng & Chiến tranh Triều Tiên |
| 지리 | 44~50 | [`lessons/45_자연환경.md`](lessons/45_자연환경.md) ~ [`lessons/50_강원과_제주.md`](lessons/50_강원과_제주.md) | Vị trí - địa hình - khí hậu, Vùng thủ đô (Seoul - Gyeonggi - Incheon), Chungcheong, Jeolla & Honam, Gyeongsang & Yeongnam, Gangwon & Jeju |

---

## 3. Tài liệu chiến lược và công cụ ôn tập

- [`00_exam_scope_and_strategy.md`](00_exam_scope_and_strategy.md) — Phương pháp học theo vòng, cách đối chiếu khái niệm và chuẩn mực hoàn thành.
- [`00_current_facts_and_corrections.md`](00_current_facts_and_corrections.md) — Bảng đối chiếu số liệu và pháp luật hiện hành (cải cách cơ cấu tố tụng hình sự 2026, hạn mức bảo hiểm tiền gửi 100 triệu won, lãi suất tối đa 20%, thống kê dân số và hộ gia đình).
- [`09_high_yield_numbers_institutions.md`](09_high_yield_numbers_institutions.md) — Nén các con số, cơ quan đầu mối và các cặp thuật ngữ dễ nhầm lẫn nhất.
- [`10_작문_구술.md`](10_작문_구술.md) — Khung luyện thi viết (작문형) và thi vấn đáp (구술시험) với các mẫu câu chuẩn theo văn phong Hàn Quốc.
- [`13_exam_question_patterns.md`](13_exam_question_patterns.md) — Phân tích dạng câu hỏi thường gặp, bẫy trắc nghiệm và chuỗi tư duy giải đề.
- [`12_cross_reference_master_books.md`](12_cross_reference_master_books.md) — Kết nối bài học KIIP với các chuyên khảo sâu trong `korean_culture/` và `korean_history/`.
- [`16_coverage_audit.md`](16_coverage_audit.md) — Báo cáo kiểm định chất lượng, rà soát tính nhất quán và độ bao phủ của toàn bộ tài liệu.
- [`SOURCES.md`](SOURCES.md) — Nguồn gốc tài liệu chính thức, thông tin khóa học và các cổng tra cứu của cơ quan nhà nước Hàn Quốc.

---

## 4. Lộ trình ôn tập khuyến nghị

```text
00_official_textbook_map.md (Xác định phạm vi 50 bài chuẩn)
   ↓
lessons/01_... đến lessons/50_... (Đọc hiểu bản chất từng bài)
   ↓
19_official_basic_gap_supplement.md (Bổ sung các chủ đề đặc thù)
   ↓
(Nếu thi 귀화) 18_귀화용_심화_official_map.md (20 bài nâng cao)
   ↓
17_complete_exam_coverage_checklist.md (Kiểm tra 4 tầng nhận thức)
   ↓
09_high_yield_numbers_institutions.md (Nén số liệu và cơ quan)
   ↓
10_작문_구술.md (Luyện đầu ra viết và nói)
   ↓
00_current_facts_and_corrections.md (Cập nhật quy định mới nhất)
```
