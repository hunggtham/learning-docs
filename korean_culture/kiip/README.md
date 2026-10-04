# KIIP — 한국사회 이해 Exam Library

Bộ tài liệu này dùng cho `한국사회이해 5단계`, với mục tiêu **đọc để hiểu hệ thống xã hội Hàn Quốc, sau đó mới nén thành fact để thi**. Nó không phải một bộ flashcard kéo dài.

## Phạm vi chính thức

Theo cấu trúc KIIP hiện hành:

- `영주용`: `한국사회이해 기본과정 70시간`;
- `귀화용`: tổng `100시간`, gồm phần 심화 bổ sung.

Để tránh nhầm syllabus, repository có hai canonical map:

1. [`00_official_textbook_map.md`](00_official_textbook_map.md) — **50 bài 기본 chính thức, 제1과~제50과**.
2. [`18_귀화용_심화_official_map.md`](18_귀화용_심화_official_map.md) — **20 bài 심화 chính thức** cho mục tiêu 국적/귀화.

> **Quy tắc:** nếu lesson numbering trong một chapter cũ mâu thuẫn với canonical map, dùng `00_official_textbook_map.md`. Structure và mechanism nằm trong chapter; fact có thể đổi được version hóa tại `00_current_facts_and_corrections.md`.

---

# 1. Start here — hiểu phạm vi trước khi học

1. [`00_official_textbook_map.md`](00_official_textbook_map.md) — exact 50-lesson syllabus.
2. [`00_exam_scope_and_strategy.md`](00_exam_scope_and_strategy.md) — exam map, cách học nhiều vòng và tiêu chuẩn mastery.
3. [`00_current_facts_and_corrections.md`](00_current_facts_and_corrections.md) — fact đã thay đổi hoặc phải kiểm tra trước kỳ thi.

Đừng bắt đầu bằng mock nếu chưa biết coverage. KIIP có cả written và oral, nên “nhìn đáp án thấy quen” chưa đủ.

---

# 2. Core curriculum — 8 lĩnh vực / 50 bài

| Domain | Bài chính thức | File | Mental model chính |
|---|---:|---|---|
| 사회1 | 1~8 | [`01_사회.md`](01_사회.md) | biểu tượng → gia đình → việc làm → giao thông/truyền thông → welfare → đô thị/nông thôn → dân số |
| 사회2 | 9~12 | [`02_교육.md`](02_교육.md) | childcare → trường phổ thông → 교육열 → community/lifelong learning |
| 문화 | 13~19 | [`03_문화.md`](03_문화.md) | 의식주 → lễ tết → tôn giáo → housing culture → 의례 → popular culture → 가치/연고 |
| 정치 | 20~24 | [`04_정치.md`](04_정치.md) | 민주주의 → 정치제도 → 정부형태 → 정치과정 → 국제관계 |
| 경제 | 25~29 | [`05_경제.md`](05_경제.md) | tăng trưởng → global economy → finance → market → employment |
| 법 | **30~36** | [`06_법.md`](06_법.md) | quyền/nghĩa vụ → quốc tịch → hiến pháp → law enforcement → 생활법률 → remedies → 준법 |
| 역사 | **37~43** | [`07_역사.md`](07_역사.md) | ancient → medieval/modern → figures → culture/art → heritage |
| 지리 | **44~50** | [`08_지리.md`](08_지리.md) | vị trí/khí hậu/địa hình → 수도권/regions → tourism/festivals → community institutions → local problem solving |

### Backbone chính xác

```text
사회1 1~8
  ↓
사회2 9~12
  ↓
문화 13~19
  ↓
정치 20~24
  ↓
경제 25~29
  ↓
법 30~36
  ↓
역사 37~43
  ↓
지리 44~50
```

Một số file được tổ chức theo concept thay vì đúng thứ tự textbook. Vì vậy, **lesson map quyết định coverage, chapter quyết định cách hiểu**.

---

# 3. Official basic gaps — những bài trước đây bị bỏ/nhạt

Sau khi đối chiếu trực tiếp với TOC chính thức, library cũ còn yếu ở:

- `제5과 한국의 대중매체`;
- `제19과 한국의 전통 가치와 연고`;
- `제23과 한국의 정치과정`;
- `제24과 한국의 국제관계`;
- `제35과 권리 침해에 대한 구제와 보호`;
- `제36과 준법의 중요성`;
- `제40과 지폐 속 위인들` 일부;
- `제48~50과` 관광·지역사회 기관·지역문제 해결.

Các gap này được vá tại:

[`19_official_basic_gap_supplement.md`](19_official_basic_gap_supplement.md)

Đây không phải “tài liệu phụ tùy chọn”; cho tới khi các section đó được merge hoàn toàn vào owner chapter, nó là **exam-critical**.

---

# 4. 귀화용 심화 — 20 bài riêng

Nếu mục tiêu là `귀화용 종합평가`, basic 50 bài chưa đủ.

Dùng:

[`18_귀화용_심화_official_map.md`](18_귀화용_심화_official_map.md)

Nó kiểm tra đủ 5 phần:

```text
대한민국의 국민
   ↓
대한민국의 역사와 발전
   ↓
대한민국의 정치와 외교
   ↓
대한민국의 경제
   ↓
대한민국의 법질서
```

Các gap 심화 quan trọng được bổ sung trực tiếp trong file 18, đặc biệt:

- `정당·시민참여`;
- `외교·국제관계`;
- `남북통일 노력`;
- `경제체제`;
- `금융과 자산관리`;
- `기업과 근로자`;
- `국민경제와 국제거래`;
- `가족·재산·직장·범죄와 법`.

---

# 5. Coverage gate — kiểm tra xem đã thực sự “đủ” chưa

Sau khi đọc core + supplement, dùng:

[`17_complete_exam_coverage_checklist.md`](17_complete_exam_coverage_checklist.md)

Một topic chỉ đánh dấu hoàn thành khi đạt:

```text
Recognition
   ↓
Recall
   ↓
Contrast
   ↓
Explanation in Korean
```

Ví dụ bạn thuộc `대통령 5년 단임` nhưng không giải thích được `단임` nghĩa gì và vì sao khác hệ thống tái cử thì mới ở tầng recall, chưa phải explanation.

---

# 6. Compression — số, cơ quan và cặp dễ nhầm

[`09_high_yield_numbers_institutions.md`](09_high_yield_numbers_institutions.md)

Dùng sau khi đã hiểu chapter. Không đảo quy trình thành “học 100 con số trước rồi cố đoán ý nghĩa”.

Đặc biệt current facts như:

- `예금자보호한도`;
- `법정 최고금리`;
- cơ cấu hình sự sau `2026-10-02`;
- statistic theo năm;
- current foreign-policy/election detail

phải quay lại `00_current_facts_and_corrections.md`.

---

# 7. Active recall — tự nhớ không nhìn note

[`14_active_recall_bank.md`](14_active_recall_bank.md)

Mục tiêu của recall không phải score đẹp ngay lần đầu mà là tìm **false familiarity**: những topic nhìn thì quen nhưng không tự nói được.

Nếu sai một câu, quay về owner chapter hoặc official supplement thay vì chỉ học đáp án câu đó.

---

# 8. 작문·구술 — biến knowledge thành output

[`10_작문_구술.md`](10_작문_구술.md)

종합평가 baseline chính thức không chỉ có 객관식; còn có `작문형` và `구술시험`. Vì vậy mỗi domain phải có concept bạn nói được bằng câu hoàn chỉnh.

Pattern nói an toàn:

`결론 → 이유 → 짧은 예시`.

Ví dụ:

**Q. 삼권분립이 왜 필요합니까?**  
`국가 권력이 한 곳에 집중되는 것을 막고 서로 견제와 균형을 이루기 위해서입니다.`

---

# 9. Mock và question pattern

- [`11_mock_01.md`](11_mock_01.md)
- [`13_exam_question_patterns.md`](13_exam_question_patterns.md)
- [`15_mock_02.md`](15_mock_02.md)

Thứ tự đề xuất:

```text
mock 01
  ↓
phân loại lỗi: knowledge / confusion / Korean / time
  ↓
13_exam_question_patterns
  ↓
vá owner chapter / file 19 / file 18
  ↓
mock 02
```

Không chỉ ghi “sai câu 17”; phải biết **vì sao sai**.

---

# 10. Deep context — khi summary chưa đủ để hiểu

[`12_cross_reference_master_books.md`](12_cross_reference_master_books.md)

KIIP chapter trả lời: **để thi cần hiểu và nói được gì?**  
Các master book ở `korean_culture/` và `korean_history/` trả lời: **vì sao hệ thống/sự kiện đó hình thành sâu hơn?**

Ví dụ:

- `5·18`, `6월 민주항쟁` → đọc sâu ở `korean_history/`;
- `전세`, family, chaebol, housing → chapter chuyên sâu ở `korean_culture/`;
- nhưng sau khi hiểu sâu phải quay lại KIIP map để giữ phạm vi thi.

---

# 11. Quality control

[`16_coverage_audit.md`](16_coverage_audit.md) giữ audit theo official lesson map và current-version risks.

Một concept trong KIIP nên có tối thiểu:

1. thuật ngữ tiếng Hàn;
2. nghĩa tiếng Việt dễ hiểu;
3. bản chất/tại sao tồn tại;
4. relation với concept gần;
5. cặp dễ nhầm nếu có;
6. recall/output question;
7. current correction nếu fact có thể đổi;
8. owner trong official map.

---

# 12. Lộ trình ôn hoàn chỉnh

## 영주용

```text
00 official map
   ↓
01~08 core chapters
   ↓
19 official-basic gap supplement
   ↓
17 complete coverage checklist
   ↓
09 high-yield numbers/institutions
   ↓
14 active recall
   ↓
10 작문·구술
   ↓
11 mock 01
   ↓
13 question patterns + vá lỗi
   ↓
15 mock 02
   ↓
00 current facts lần cuối
```

## 귀화용 심화

```text
영주용 flow hoàn tất
   ↓
18 귀화용 심화 20과
   ↓
심화 20-question gate
   ↓
10 작문·구술의 귀화 질문
   ↓
mock + current facts
```

### Exit criteria

Bạn sẵn sàng hơn khi có thể:

- tick đủ **50/50 basic lessons** theo file 00;
- nếu thi 귀화, tick đủ **20/20 심화 lessons** theo file 18;
- phân biệt các cặp bẫy trong 10 giây;
- kể chronology lịch sử/chính trị không nhìn note;
- trả lời ngắn bằng Korean cho câu `왜? 어떻게? 차이가 무엇입니까?`;
- nhận ra fact nào là current-version risk và không học cứng từ PDF cũ.

> **Điểm chốt:** “đủ nội dung” = official map basic + 심화 map + gap supplement; “đủ khả năng thi” = coverage đó đi qua recall, 작문·구술 và mock.