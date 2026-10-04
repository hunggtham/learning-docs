# Sources & Provenance — KIIP / 한국사회 이해

Mục đích của file này là tách rõ:

1. giáo trình KIIP;
2. nguồn chính thức hiện hành cho luật/policy/kỳ thi;
3. PDF study summaries;
4. note tự biên soạn trong repository.

---

# 1. Official textbook baseline

## 한국사회 이해 : 기본

Đã xác minh trong audit 2026-10:

- 기획: `법무부 출입국·외국인정책본부`
- 판: **12판**
- 발행: **2025**
- ISBN: `9791186140291`

50 bài:

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

## 한국사회 이해 : 심화

- 판: **10판**
- 발행: **2024**

20 bài được chia thành:

```text
대한민국의 국민        1~4
대한민국의 역사와 발전  5~8
대한민국의 정치와 외교  9~12
대한민국의 경제        13~16
대한민국의 법질서      17~20
```

Repository không sao chép nguyên văn sách có bản quyền; nội dung được diễn giải lại để học.

Coverage:

- [`17_complete_exam_coverage_map.md`](17_complete_exam_coverage_map.md)
- [`18_귀화용_심화_20과.md`](18_귀화용_심화_20과.md)

---

# 2. KIIP official/current references

- 법무부 사회통합프로그램  
  https://www.moj.go.kr/immigration/1571/subview.do
- 사회통합정보망  
  https://www.socinet.go.kr/
- KIIP 평가  
  https://www.kiiptest.org/
- 중앙선거관리위원회  
  https://www.nec.go.kr/
- 대한민국 국회  
  https://www.assembly.go.kr/

Dùng cho:

- course structure/hours
- evaluation notices
- registration
- current institutions
- election rules

---

# 3. Program facts verified

법무부 hiện mô tả:

- `한국어와 한국문화`: 0~4단계
- `한국사회 이해`: 5단계
- 영주 mục tiêu: **70시간**
- 국적 mục tiêu: **100시간**

Socinet vận hành riêng `영주용 종합평가` và `귀화용 종합평가`.

Format đánh giá có thể thay đổi theo notice, vì vậy trước kỳ thi luôn kiểm tra Socinet/KIIP 평가 thay vì học từ screenshot cũ.

---

# 4. Current law — 2026 형사사법 개편

Các giáo trình cũ có thể dùng `경찰·검찰·법원` như mô hình đơn giản. Nhưng từ **2026-10-02** cơ cấu đã thay đổi.

Nguồn pháp lý chính thức:

- 국가법령정보센터 — `검찰청법` 폐지 / `공소청법` 시행  
  https://www.law.go.kr/lsRvsDocListP.do?chrClsCd=010202&lsId=001286&lsRvsGubun=all

- 국가법령정보센터 — `중대범죄수사청 조직 및 운영에 관한 법률`  
  https://www.law.go.kr/LSW/lsInfoP.do?efYd=20261002&lsiSeq=290127

Current mental model:

```text
수사
├─ 경찰 등 사법경찰
└─ 중대범죄수사청 (법률상 중대범죄)

기소·공소유지
└─ 공소청

재판
└─ 법원
```

Đã phản ánh vào:

- [`00_current_facts_and_corrections.md`](00_current_facts_and_corrections.md)
- [`06_법.md`](06_법.md)
- [`09_high_yield_numbers_institutions.md`](09_high_yield_numbers_institutions.md)

---

# 5. Other official sources

## 금융

금융위원회 — 예금보호한도 `1억원`  
https://www.fsc.go.kr/no010101/85200

## 최고금리

법무부 — 법정 최고금리 `20%`  
https://www.moj.go.kr/bbs/moj/182/545579/artclView.do

## 체류·출입국

HiKorea / `1345`를 사용해 current 체류 rules 확인.

---

# 6. Uploaded KIIP study summaries

Bản đầu của repo được dựng một phần từ:

- `KIIP 5 CHƯƠNG 1 XÃ HỘI.pdf`
- `KIIP 5 - CHƯƠNG 2 GIÁO DỤC.pdf`
- `KII5 - CHƯƠNG 3 VĂN HÓA.pdf`
- `CHƯƠNG 4 chính trị.pdf`
- `CHƯƠNG 5 kinh tế.pdf`
- `KIIP 5 - CHƯƠNG 6.pdf`
- `KIIP 5 - CHƯƠNG 7 LỊCH SỬ.pdf`
- `KIIP 5 - CHƯƠNG 8 (ĐỊA LÝ).pdf`

Chúng hữu ích để ôn nhưng **không đứng trên giáo trình/law/official notice hiện hành**.

---

# 7. Source hierarchy

Khi có conflict:

```text
1. current law / official notice áp dụng đúng thời điểm
2. 법무부·사회통합정보망·KIIP 평가
3. giáo trình KIIP hiện hành
4. cơ quan chuyên ngành chính thức
5. PDF study summaries
6. repository notes
7. community/blog/commercial prep
```

Cần phân biệt:

- câu hỏi về **교재 내용** → hiểu textbook đang kiểm tra concept gì;
- câu hỏi về **현재 제도** → ưu tiên law/official current source.

---

# 8. Current-fact policy

Các nhóm phải có timestamp hoặc route qua [`00_current_facts_and_corrections.md`](00_current_facts_and_corrections.md):

- finance limits/rates
- 최저임금 và labor details
- population/religion/education statistics
- welfare benefits
- visa/nationality/residency
- foreigner voting eligibility
- ministry/prosecution/judicial structure
- housing protection rules
- KIIP format/fee/schedule

---

# 9. Mock/recall provenance

Các câu trong mock, recall bank và oral bank là **câu luyện tập tự biên soạn**, trừ khi được ghi rõ là official sample. Không mô tả chúng như đề thi thật bị leak.
