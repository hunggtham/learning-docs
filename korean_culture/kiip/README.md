# KIIP — 한국사회 이해 Exam Library

Bộ tài liệu này dùng cho `한국사회이해 5단계`, với mục tiêu **đọc để hiểu hệ thống xã hội Hàn Quốc, sau đó mới nén thành fact để thi**. Nó không phải một bộ flashcard kéo dài.

## Phạm vi

Theo cấu trúc KIIP hiện hành:

- `영주용`: `한국사회이해 기본과정 70시간`;
- `귀화용`: tổng `100시간`, gồm phần 심화 bổ sung.

Trong repository không tách hai cây tài liệu trùng nhau. Mỗi chapter dùng tag:

- `공통`: nền cơ bản;
- `귀화용 심화`: cần học sâu hơn cho mục tiêu 국적/귀화;
- `현재 확인`: fact có thể đổi theo luật/chính sách/thống kê.

> **Nguyên tắc:** structure và mechanism nằm trong chapter; fact có thể đổi được version hóa tại `00_current_facts_and_corrections.md`.

---

# 1. Start here — hiểu phạm vi trước khi học

1. [`00_exam_scope_and_strategy.md`](00_exam_scope_and_strategy.md) — exam map, cách học nhiều vòng và tiêu chuẩn mastery.
2. [`00_current_facts_and_corrections.md`](00_current_facts_and_corrections.md) — các fact đã thay đổi hoặc phải kiểm tra trước kỳ thi.

Đừng bắt đầu bằng mock nếu chưa biết coverage. KIIP có cả written và oral, nên “nhìn đáp án thấy quen” chưa đủ.

---

# 2. Core curriculum — 8 lĩnh vực / 50 bài

| Domain | Bài | File | Mental model chính |
|---|---:|---|---|
| 사회 | 1~8 | [`01_사회.md`](01_사회.md) | gia đình → việc làm → nhà ở → phúc lợi → đời sống người nước ngoài |
| 교육 | 9~12 | [`02_교육.md`](02_교육.md) | childcare → trường phổ thông → đại học → lifelong learning |
| 문화 | 13~19 | [`03_문화.md`](03_문화.md) | giá trị → nghi lễ vòng đời → lễ tết → ăn ở → tôn giáo → 한류 |
| 정치 | 20~24 | [`04_정치.md`](04_정치.md) | 헌법 → 국민주권 → 삼권분립 → 선거 → 지방자치 → 민주화 |
| 경제 | 25~29 | [`05_경제.md`](05_경제.md) | thị trường → tăng trưởng → tiêu dùng → tài chính → việc làm |
| 법 | 30~37 | [`06_법.md`](06_법.md) | quyền/nghĩa vụ → cư trú → gia đình → hợp đồng → tội phạm → tư pháp |
| 역사 | 38~44 | [`07_역사.md`](07_역사.md) | chronology → nhân vật → di sản → độc lập → nhà nước hiện đại → dân chủ hóa |
| 지리 | 45~50 | [`08_지리.md`](08_지리.md) | tự nhiên → 수도권 → vùng → association lịch sử/văn hóa |

### Backbone

```text
사회 1~8
  ↓
교육 9~12
  ↓
문화 13~19
  ↓
정치 20~24
  ↓
경제 25~29
  ↓
법 30~37
  ↓
역사 38~44
  ↓
지리 45~50
```

Không nhất thiết học theo thứ tự này nếu đang vá lỗ hổng, nhưng lần đọc đầu nên đi đủ 8 domain để không bỏ vùng kiến thức.

---

# 3. Coverage gate — kiểm tra xem đã thực sự “đủ” chưa

Sau khi đọc 01~08, dùng:

[`17_complete_exam_coverage_checklist.md`](17_complete_exam_coverage_checklist.md)

File 17 là **master checklist** cho toàn bộ phần ôn: core 50 bài, 귀화용 심화, current facts và output skills.

Một topic chỉ đánh dấu hoàn thành khi bạn đạt:

```text
Recognition
   ↓
Recall
   ↓
Contrast
   ↓
Explanation in Korean
```

Ví dụ bạn thuộc `대통령 5년 단임` nhưng không giải thích được `단임` khác hệ thống tái cử như thế nào thì mới ở tầng recall, chưa phải explanation.

---

# 4. Compression — số, cơ quan và cặp dễ nhầm

[`09_high_yield_numbers_institutions.md`](09_high_yield_numbers_institutions.md)

Dùng sau khi đã hiểu chapter. Không đảo quy trình thành “học 100 con số trước rồi cố đoán ý nghĩa”.

Đặc biệt current facts như:

- `예금자보호한도`
- `법정 최고금리`
- cơ cấu hình sự sau `2026-10-02`
- statistic theo năm

phải quay lại `00_current_facts_and_corrections.md`.

---

# 5. Active recall — tự nhớ không nhìn note

[`14_active_recall_bank.md`](14_active_recall_bank.md)

Mục tiêu của recall không phải score đẹp ngay lần đầu mà là tìm **false familiarity**: những topic nhìn thì quen nhưng không tự nói được.

Nếu sai một câu, quay về owner chapter thay vì chỉ học đáp án câu đó.

---

# 6. 작문·구술 — biến knowledge thành output

[`10_작문_구술.md`](10_작문_구술.md)

종합평가 baseline chính thức không chỉ có 객관식; còn có `작문형` và `구술시험`. Vì vậy mỗi domain phải có ít nhất vài concept bạn nói được bằng câu hoàn chỉnh.

Pattern nói an toàn:

`결론 → 이유 → 짧은 예시`.

Ví dụ:

**Q. 삼권분립이 왜 필요합니까?**  
`국가 권력이 한 곳에 집중되는 것을 막고 서로 견제와 균형을 이루기 위해서입니다.`

---

# 7. Mock và question pattern

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
vá owner chapter
  ↓
mock 02
```

Không chỉ ghi “sai câu 17”; phải biết **vì sao sai**.

---

# 8. Deep context — khi summary chưa đủ để hiểu

[`12_cross_reference_master_books.md`](12_cross_reference_master_books.md)

KIIP chapter trả lời: **để thi cần hiểu và nói được gì?**  
Các master book ở `korean_culture/` và `korean_history/` trả lời: **vì sao hệ thống/sự kiện đó hình thành sâu hơn?**

Ví dụ:

- `5·18`, `6월 민주항쟁` → đọc sâu ở `korean_history/`;
- `전세`, gia đình, chaebol, xã hội hiện đại → chapter chuyên sâu ở `korean_culture/`;
- nhưng sau khi hiểu sâu phải quay lại KIIP để giữ phạm vi thi.

---

# 9. Quality control

[`16_coverage_audit.md`](16_coverage_audit.md) giữ audit theo domain và current-version risks.

Một concept trong KIIP nên có tối thiểu:

1. thuật ngữ tiếng Hàn;
2. nghĩa tiếng Việt dễ hiểu;
3. bản chất/tại sao tồn tại;
4. relation với concept gần;
5. cặp dễ nhầm nếu có;
6. recall/output question;
7. current correction nếu fact có thể đổi.

---

# 10. Lộ trình ôn hoàn chỉnh

```text
00 scope
   ↓
01~08 core chapters
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
00 current facts lần cuối trước kỳ thi
```

### Exit criteria

Bạn sẵn sàng hơn khi có thể:

- nhìn một concept và giải thích bản chất, không chỉ dịch từ;
- phân biệt các cặp bẫy trong 10 giây;
- tự kể chronology lịch sử/chính trị không nhìn note;
- trả lời ngắn bằng Korean cho các câu `왜? 어떻게? 차이가 무엇입니까?`;
- nhận ra fact nào là current-version risk và không học cứng từ PDF cũ.

> **Điểm chốt:** “đủ nội dung” được bảo đảm bằng coverage 01~08 + `귀화용 심화` + file 17; “đủ khả năng thi” chỉ đạt khi coverage đó đi qua recall, 작문·구술 và mock.