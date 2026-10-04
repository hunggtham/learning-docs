# 00. Bản đồ phạm vi KIIP — 시험 범위와 전략

> File này trả lời ba câu hỏi trước khi học: **thi cái gì, tài liệu nào là nguồn chuẩn, và phải học đến mức nào**.

---

# 1. KIIP nằm ở đâu trong chương trình?

`사회통합프로그램(KIIP)` gồm hai khối lớn:

```text
한국어와 한국문화
└─ 0~4단계

한국사회 이해
└─ 5단계
```

Theo 안내 hiện hành của 법무부:

- mục tiêu `영주`: 한국사회 이해 70시간;
- mục tiêu `국적/귀화`: 한국사회 이해 100시간.

Do đó repository này tập trung vào **5단계 한국사회 이해**, không thay thế toàn bộ giáo trình tiếng Hàn 0~4단계.

---

# 2. Hai lớp phạm vi: 기본 và 심화

## 공통 / 기본

Đây là backbone 50 bài mà cả người ôn 영주용 lẫn 귀화용 đều cần nắm:

```text
사회 1~8
교육 9~12
문화 13~19
정치 20~24
경제 25~29
법 30~37
역사 38~44
지리 45~50
```

Bản `한국사회 이해 : 기본` được xác minh trong audit 2026-10 là **12판 (2025)**.

## 귀화용 심화

Người hướng tới 국적/귀화 phải học thêm lớp kiến thức về:

- `대한민국의 국민`;
- `국민의 권리`;
- `국민의 의무`;
- `국민을 위한 복지`;
- `대한민국 정부수립` và tiến trình 헌정·민주주의;
- `헌법적 가치`, 국가 공동체, an ninh/thống nhất ở mức giáo trình yêu cầu.

Bản `한국사회 이해 : 심화` được xác minh trong audit là **10판 (2024)**.

Repository không tạo hai cây note trùng nhau. Phần chung học một lần; nội dung 심화 được gắn đúng domain.

---

# 3. Cách đọc tag

- `공통`: nội dung cơ bản dùng cho 영주용 và là nền cho 귀화용.
- `귀화용 심화`: phần cần mở rộng cho quốc tịch/귀화.
- `현재 확인`: dữ liệu, luật, policy, cơ cấu hoặc format đánh giá có thể đổi.

Ví dụ:

```text
국회의원 임기 4년
→ structural fact, tương đối ổn định

예금자보호한도
→ policy/amount, phải 현재 확인

외국인의 지방선거 선거권 조건
→ legal condition, phải 현재 확인
```

---

# 4. Source hierarchy — học theo nguồn nào?

Ưu tiên:

1. giáo trình/공지 chính thức áp dụng cho thời điểm kỳ thi;
2. 법무부, 사회통합정보망(Socinet), KIIP 평가;
3. cơ quan chuyên ngành chính thức;
4. textbook edition gần nhất đã xác minh;
5. 8 PDF study summary người dùng cung cấp;
6. note tổng hợp của repository;
7. community/blog/prep material.

Chi tiết provenance: [`SOURCES.md`](SOURCES.md).

Điều này giải quyết một vấn đề thực tế: **textbook và note cũ có thể vẫn đúng về concept nhưng sai về số liệu hiện hành**.

---

# 5. Phạm vi 50 bài — không chỉ tên chapter

Dùng [`17_complete_exam_coverage_map.md`](17_complete_exam_coverage_map.md) làm “contract học tập”.

Với mỗi bài, bạn phải biết:

```text
정의      nó là gì?
이유      tại sao tồn tại?
구별      khác gì với concept gần nó?
적용      áp dụng trong đời sống Hàn thế nào?
시험출력  nếu đề đổi câu chữ, mình vẫn trả lời được không?
```

Nếu chỉ nhớ một keyword nhưng không giải thích được, concept đó chưa hoàn thành.

---

# 6. Phần 심화 được gộp vào đâu?

| Trục 심화 | File chính |
|---|---|
| 대한민국의 국민 | `01_사회.md`, `06_법.md`, `17_complete_exam_coverage_map.md` |
| 국민의 기본권 | `04_정치.md`, `06_법.md` |
| 국민의 의무 | `04_정치.md`, `06_법.md` |
| 국민을 위한 복지 | `01_사회.md` |
| 헌법·삼권분립·국가기관 | `04_정치.md` |
| 정부수립·한국전쟁·민주화 | `04_정치.md`, `07_역사.md` |
| 국가상징 | `01_사회.md`, `10_작문_구술.md` |
| 국가안보·통일·헌법적 가치 | `17_complete_exam_coverage_map.md` + 심화 source |

Điểm khác giữa 기본 và 심화 không phải chỉ “thêm vài câu khó”. Ở 심화, bạn phải giải thích sâu hơn về **công dân, quyền-nghĩa vụ và trật tự hiến pháp**.

---

# 7. Format đánh giá — học theo kỹ năng, không đóng đinh vào một notice cũ

Một thông báo chính thức của 법무부 về `귀화용 종합평가` công bố cấu trúc 100 điểm gồm:

- 객관식;
- 작문형;
- 구술형;
- tổng cộng 45문 / 70분 trong format được công bố ở notice đó;
- 합격 기준 60점 이상 trong notice tương ứng.

Tuy nhiên **format kỳ thi là dữ liệu vận hành có thể được thay đổi bằng 공지 mới**. Vì vậy trước kỳ thi, kiểm tra Socinet/KIIP 평가 thay vì coi số câu/thời gian cũ là bất biến.

Điều không đổi trong strategy của repository là bạn phải luyện đủ:

```text
객관식 recognition
+ contrast/trap
+ 작문 output
+ 구술 output
```

---

# 8. Bảy kiểu câu hỏi cần chuẩn bị

## ① 정의형 — định nghĩa

`지방자치란 무엇입니까?`

Cần trả lời: **nó là gì + mục đích**.

## ② 비교형 — so sánh

`전세와 월세의 차이`, `사회보험과 공공부조`, `대법원과 헌법재판소`.

Cần có ít nhất 2 trục phân biệt.

## ③ 기관형 — cơ quan

Tình huống → chọn đúng 기관/chức năng.

Ví dụ: 119, 112, 1345, 국회, 법원, 지방자치단체.

## ④ 순서형 — thứ tự

Lịch sử và 민주화:

`4·19 → 5·18 → 6월 민주항쟁`

hoặc chuỗi thời đại lịch sử.

## ⑤ 원인·결과형 — nguyên nhân/hệ quả

Tại sao cần 삼권분립? Vì sao 도시화 diễn ra? Vì sao 경제위기 ảnh hưởng việc làm?

## ⑥ 상황형 — tình huống đời sống

Hợp đồng thuê nhà, lao động, bệnh viện, lừa đảo tài chính, quyền lợi người tiêu dùng, visa.

## ⑦ 작문·구술형 — output

Không chỉ chọn đáp án. Phải tự tạo câu tiếng Hàn ngắn, đúng từ khóa.

---

# 9. Học theo 6 vòng

## Vòng 1 — Coverage

Đọc [`17_complete_exam_coverage_map.md`](17_complete_exam_coverage_map.md). Đánh dấu concept lạ.

## Vòng 2 — Understanding

Đọc `01~08` theo domain. Với phần chưa hiểu cơ chế, dùng master books qua [`12_cross_reference_master_books.md`](12_cross_reference_master_books.md).

## Vòng 3 — Contrast + numbers

Dùng [`09_high_yield_numbers_institutions.md`](09_high_yield_numbers_institutions.md).

Tập trung vào cặp dễ nhầm:

- 국회 ↔ 행정부;
- 대법원 ↔ 헌법재판소;
- 사회보험 ↔ 공공부조;
- 영주권 ↔ 국적;
- 어린이집 ↔ 유치원;
- 수시 ↔ 정시;
- 전세 ↔ 월세;
- 설날 ↔ 추석;
- 지역구 ↔ 비례대표.

## Vòng 4 — Active recall

Dùng [`14_active_recall_bank.md`](14_active_recall_bank.md). Không nhìn đáp án trước.

## Vòng 5 — Output

Dùng [`10_작문_구술.md`](10_작문_구술.md) và [`13_exam_question_patterns.md`](13_exam_question_patterns.md).

Mẫu nói hiệu quả:

```text
정의
→ 이유/특징
→ 예시
```

## Vòng 6 — Mock + error loop

Làm `11_mock_01.md` và `15_mock_02.md`.

Mỗi câu sai phải được phân loại:

- thiếu fact;
- nhầm concept;
- không hiểu Korean wording;
- nhầm cơ quan;
- nhầm timeline;
- fact đã stale.

Sau đó quay lại **concept gốc**, không học thuộc đáp án sai/đúng riêng lẻ.

---

# 10. Ba mức ghi nhớ

Một fact chỉ được coi là “đã học” khi đạt:

1. **Recognition** — nhìn thấy thì biết.
2. **Recall** — không nhìn note vẫn nhớ.
3. **Explanation** — nói được bằng một câu Hàn đơn giản.

Ví dụ `삼권분립`:

- recognition: 입법·행정·사법;
- recall: 국회–정부–법원;
- explanation: `국가 권력이 한 곳에 집중되지 않도록 권력을 나누는 원리입니다.`

Với 귀화용 심화, ưu tiên mức 3.

---

# 11. Dữ liệu có thể thay đổi

Không học cứng từ infographic/PDF cũ các nhóm:

- phúc lợi và trợ cấp;
- visa/quốc tịch/영주;
- luật lao động và mức tiền;
- bảo vệ tiền gửi, lãi suất/trần lãi;
- thống kê dân số/hộ gia đình/tôn giáo/giáo dục;
- quyền bầu cử có điều kiện;
- cơ cấu bộ/cơ quan công tố-tư pháp;
- format/lệ phí/lịch đánh giá.

Route toàn bộ qua [`00_current_facts_and_corrections.md`](00_current_facts_and_corrections.md).

---

# 12. Checklist cuối

Trước khi nói “đủ KIIP”, bạn phải có thể:

- [ ] giải thích toàn bộ checklist 50 bài trong file 17;
- [ ] hoàn thành 8 domain 01~08;
- [ ] nếu thi 귀화용, hoàn thành toàn bộ lớp 심화;
- [ ] thuộc high-yield numbers/institutions;
- [ ] làm recall không nhìn note;
- [ ] viết được câu ngắn;
- [ ] nói được câu trả lời 3 tầng definition → reason → example;
- [ ] làm ít nhất 2 mock và sửa lỗi theo concept;
- [ ] cập nhật current facts ngay trước kỳ thi.

> **Nguyên tắc:** mục tiêu không phải “nhìn câu này đã từng gặp”, mà là **dù đề đổi cách hỏi, vẫn nhận ra hệ thống phía sau và suy ra đáp án**.