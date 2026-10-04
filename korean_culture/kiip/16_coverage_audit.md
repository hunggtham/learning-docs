# 16. Coverage Audit — KIIP 한국사회 이해

> **Audit date:** `2026-10-04`  
> **Canonical basic syllabus:** [`00_official_textbook_map.md`](00_official_textbook_map.md)  
> **Canonical 귀화용 심화 syllabus:** [`18_귀화용_심화_official_map.md`](18_귀화용_심화_official_map.md)

File này trả lời ba câu hỏi:

1. official lesson nào có owner?
2. phần nào từng thiếu/nhạt và đã được vá ở đâu?
3. fact nào phải version hóa vì luật/policy/thống kê thay đổi?

---

# 1. Correction quan trọng sau khi đối chiếu giáo trình chính thức

Mapping cũ trong library từng ghi:

```text
법 30~37
역사 38~44
지리 45~50
```

Đây là **off-by-one error**.

Mapping chính thức hiện dùng:

```text
사회1 1~8
사회2 9~12
문화 13~19
정치 20~24
경제 25~29
법 30~36
역사 37~43
지리 44~50
```

Lesson titles đầy đủ và owner nằm ở `00_official_textbook_map.md`.

---

# 2. Basic 50-lesson coverage

| Domain | Official lessons | Main owner | Status |
|---|---:|---|---|
| 사회1 | 1~8 | `01_사회.md` + file 19 | ✅ 8/8 |
| 사회2 | 9~12 | `02_교육.md` | ✅ 4/4 |
| 문화 | 13~19 | `03_문화.md` + file 19 | ✅ 7/7 |
| 정치 | 20~24 | `04_정치.md` + file 19 | ✅ 5/5 |
| 경제 | 25~29 | `05_경제.md` | ✅ 5/5 |
| 법 | 30~36 | `06_법.md` + file 19 | ✅ 7/7 |
| 역사 | 37~43 | `07_역사.md` + file 19 | ✅ 7/7 |
| 지리 | 44~50 | `08_지리.md` + file 19 | ✅ 7/7 |

**Total:** `50/50 official basic lessons have an owner`.

Điều này nghĩa là coverage map không còn syllabus gap rõ ràng. Nó **không** nghĩa người học đã master 50 bài.

---

# 3. Gaps phát hiện trong đợt audit và cách xử lý

## 제5과 한국의 대중매체

Gap cũ: chỉ có digital-life note, chưa giải thích `언론·여론·대중매체` như một social institution.

Fix: [`19_official_basic_gap_supplement.md`](19_official_basic_gap_supplement.md).

## 제19과 한국의 전통 가치와 연고

Gap cũ: có `효·공동체` nhưng thiếu `혈연·지연·학연·연고주의`.

Fix: file 19.

## 제23과 한국의 정치과정

Gap cũ: có election/local participation nhưng thiếu flow `여론·언론·정당·시민단체 → 정책`.

Fix: file 19 + `04_정치.md`.

## 제24과 한국의 국제관계

Gap lớn: politics chapter trước audit không có owner rõ cho international relations.

Fix: file 19, gồm `분단·한국전쟁·정전·주변4국·외교`.

## 제35과 권리 침해에 대한 구제와 보호

Gap cũ: có tên 기관 nhưng chưa dạy cách chọn remedy.

Fix: file 19 — `경찰·노동기관·인권위·법률구조공단·권익위·법원` theo loại vấn đề.

## 제36과 준법의 중요성

Gap cũ: `준법` xuất hiện rải rác, chưa giải thích relation với `법치주의`.

Fix: file 19.

## 제40과 지폐 속 위인들

Gap cũ: figure table chưa bảo đảm banknote association.

Fix:

- `1천원 이황`
- `5천원 이이`
- `1만원 세종대왕`
- `5만원 신사임당`.

## 제48~50과

Gap cũ: geography chủ yếu là region recognition, thiếu ba bài cuối chính thức:

- 관광명소·축제;
- 지역사회 기관;
- 지역문제 해결·주민 참여.

Fix: file 19.

---

# 4. Core chapters được tăng độ sâu

| File | Trạng thái sau review | Nội dung chính được cải thiện |
|---|---|---|
| `01_사회.md` | ✅ deepened | family, population change, housing, welfare, healthcare, foreigner support, multicultural society |
| `02_교육.md` | ✅ baseline+ | childcare, school, education fever/admissions, lifelong learning |
| `03_문화.md` | ✅ deepened | rites, `회갑/환갑`, holidays, food, hanok, religion, Hallyu |
| `04_정치.md` | ✅ deepened | constitution, sovereignty, separation of powers, institutions, elections, local autonomy, democratization |
| `05_경제.md` | ✅ baseline+ | growth, market, consumer, finance, employment/fraud |
| `06_법.md` | ✅ deepened/current | civil/criminal/admin, residence/nationality, family/property/labor, 2026 justice structure |
| `07_역사.md` | ✅ deepened | causal timeline, figures, heritage, independence, modern state, democratization |
| `08_지리.md` | ✅ baseline+ + supplement | physical/regions + official final lessons via file 19 |

`baseline+` nghĩa là core chapter đã đủ backbone nhưng chưa nhất thiết đồng nhất style tuyệt đối với các chapter được rewrite sâu.

---

# 5. 귀화용 심화 — 20/20 official lessons

Canonical owner: [`18_귀화용_심화_official_map.md`](18_귀화용_심화_official_map.md).

## 1편 대한민국의 국민 — 4과

- 정체성과 헌법
- 국민의 권리
- 국민의 의무
- 국민을 위한 복지

✅ covered.

## 2편 대한민국의 역사와 발전 — 4과

- 대한민국 정부 수립
- 6·25 전쟁과 남북 관계
- 민주주의의 발전
- 사회 변동

✅ covered.

## 3편 대한민국의 정치와 외교 — 4과

- 정치 과정과 시민 참여
- 선거와 정당
- 외교와 국제관계
- 남북통일을 위한 노력

✅ previously under-covered; now expanded in file 18/19.

## 4편 대한민국의 경제 — 4과

- 한국의 경제체제
- 금융과 자산 관리
- 기업과 근로자
- 국민경제와 국제거래

✅ previously under-specified; now expanded in file 18.

## 5편 대한민국의 법질서 — 4과

- 가족 문제와 법
- 재산 문제와 법
- 직장생활과 법
- 범죄와 법

✅ covered through file 18 + `06_법.md`.

**Total:** `20/20 심화 lessons have an owner and output question`.

---

# 6. Exam-output coverage

Owner: [`10_작문_구술.md`](10_작문_구술.md).

Layer hiện có:

- writing structure;
- safe connectors;
- definition/reason/comparison/order/history/orientation schemas;
- 50 core oral questions;
- 10 귀화 심화 questions;
- self-rating `0~3`;
- practice loop.

Coverage rule:

`multiple-choice recognition alone ≠ exam readiness`.

---

# 7. Current-version risks

Owner: [`00_current_facts_and_corrections.md`](00_current_facts_and_corrections.md).

## Financial/policy

- `예금자보호한도`
- `법정 최고금리`
- minimum wage/year-specific amounts
- benefit amounts.

## Statistics

- `1인 가구 비율`
- population
- religion share
- education statistics.

## Immigration/nationality

- visa requirements;
- reporting deadlines;
- detailed naturalization conditions.

## Election/politics

- detailed foreign-resident voting eligibility;
- election dates;
- current party landscape;
- current government organization if reorganized.

## International relations

- trade ranking;
- current inter-Korean conditions;
- current diplomatic disputes/policy positions.

## Criminal justice — major 2026 correction

From `2026-10-02`:

`검찰청` as the old organization is no longer the current simple owner for prosecution/investigation.

Current exam mental model:

`수사기관(경찰·중대범죄수사청 등) → 공소청 → 법원`.

Always distinguish:

`수사 ↔ 기소/공소 ↔ 재판`.

---

# 8. Exam-format risk

Baseline official material describes:

- `필기 40문 / 60분 / 75점`
- `객관식 36문`
- `작문형 4문`
- `구술 5문 / 10분 / 25점`
- total `45문 / 70분 / 100점`
- baseline pass `60점 이상`.

But 운영/평가 details can be revised. Before each exam verify `kiiptest.org`/Socinet.

---

# 9. Layer architecture after audit

```text
Official basic syllabus  → 00_official_textbook_map
Official advanced map    → 18_귀화용_심화_official_map
Concept understanding    → 01~08
Basic gaps               → 19_official_basic_gap_supplement
Current verification     → 00_current_facts_and_corrections
Global mastery gate      → 17_complete_exam_coverage_checklist
Compression              → 09_high_yield_numbers_institutions
Active recall            → 14_active_recall_bank
Output                   → 10_작문_구술
Question traps           → 13_exam_question_patterns
Mock                     → 11_mock_01, 15_mock_02
Deep context             → 12_cross_reference_master_books
Quality audit            → 16_coverage_audit
```

---

# 10. Quality invariant

Một concept được coi là properly documented khi có:

1. Korean term;
2. Vietnamese explanation;
3. underlying purpose/mechanism;
4. relation với concept gần;
5. contrast/trap;
6. recall/output question;
7. current correction nếu cần;
8. official lesson owner.

Không cần copy toàn bộ textbook hoặc master history vào KIIP. Mục tiêu là **self-contained enough to understand and pass, nhưng vẫn có canonical scope**.

---

# 11. Audit conclusion

Sau đợt review `2026-10-04`:

- **basic:** `50/50` official lessons have coverage owner;
- **귀화용 심화:** `20/20` official lessons have coverage owner;
- các gap lớn trước đây (`대중매체`, `연고`, `정치과정`, `국제관계`, remedies, 준법, banknote figures, final geography lessons) đã được bổ sung;
- chapter high-risk (`사회·정치·법·역사`) đã được rewrite sâu;
- current-law layer đã sửa thay đổi hình sự 2026;
- output layer có writing/oral practice;
- remaining risk chủ yếu là **future policy/current-fact changes và learner mastery**, không phải một syllabus hole đã biết.

Final loop:

`00 official map → 01~08 + 19 → (귀화: 18) → 17 → 14 → 10 → mock → 00 current facts`.