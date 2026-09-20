# 16. Coverage Audit — KIIP 한국사회 이해

Mục tiêu của file này là kiểm tra **đã cover gì, phần nào là source, phần nào là current verification, phần nào cần học sâu**. Nó không phải một chapter để học thuộc.

## 1. Coverage theo 8 PDF

| Domain | Bài | File | Nội dung chính đã cover | Trạng thái |
|---|---:|---|---|---|
| 사회 | 1~8 | `01_사회.md` | 국가상징, 가족, 직장, 주거, 도시·농촌, 교통·통신, 사회보험, 외국인 지원·안전 | ✅ core covered |
| 교육 | 9~12 | `02_교육.md` | 임신·보육, 어린이집/유치원, 6-3-3, 초·중·고, 외국인 학생, 수시/정시, 고등교육, 평생교육 | ✅ expanded |
| 문화 | 13~19 | `03_문화.md` | 효·예절·공동체, 통과의례, 설날/추석, 음식, 한복/한옥, 종교, 한류·여가 | ✅ expanded |
| 정치 | 20~24 | `04_정치.md` | 국민주권, 민주화, 삼권분립, 국회·행정부·사법부, 선거, 지방자치 | ✅ core + 귀화 심화 |
| 경제 | 25~29 | `05_경제.md` | 경제활동, 성장, 소비자, 금융기관, 금융사기, 취업 | ✅ expanded |
| 법 | 30~37 | `06_법.md` | 법 목적, 외국인 권리·의무, 입국·체류, 국적·귀화, 가족법, 금전·부동산, 범죄·기관 | ✅ core + corrections |
| 역사 | 38~44 | `07_역사.md` | 고조선, 삼국·남북국, 고려, 조선, 일제강점·독립운동, 문화유산, 광복 이후 | ✅ core + cross-reference |
| 지리 | 45~50 | `08_지리.md` | 사계절, 지형, 수도권, 충청, 전라, 경상, 강원, 제주, 사투리 | ✅ expanded |

## 2. 귀화용 심화 đã được gộp ở đâu

Không có folder riêng cho 귀화. Nội dung bổ sung được đặt theo concept:

| Concept | Vị trí |
|---|---|
| 국민·영주권·국적 | `01_사회.md`, `06_법.md` |
| 복지국가·사회보험/공공부조 | `01_사회.md` |
| 기본권 | `04_정치.md`, `06_법.md` |
| 국민의 의무 | `04_정치.md`, `06_법.md` |
| 헌법·국가·정부 | `04_정치.md` |
| 정부수립·한국전쟁·민주화 | `04_정치.md`, `07_역사.md` |
| 국가상징 설명·구술 | `01_사회.md`, `10_작문_구술.md` |

## 3. Current-version risks

Các nhóm không được học cứng từ infographic cũ:

- `예금자보호한도`
- `법정 최고금리`
- tỷ lệ `1인 가구`
- dân số Seoul
- tỷ lệ tôn giáo
- tỷ lệ vào đại học, số du học sinh
- trợ cấp sinh con/chăm trẻ
- chi tiết visa/quốc tịch
- chi tiết quy định election cho từng loại đối tượng
- format kỳ thi nếu có notice mới

Tất cả được route qua `00_current_facts_and_corrections.md`.

## 4. Layer học tập đã có

```text
Source understanding   → 01~08
Current verification   → 00_current_facts_and_corrections
High-yield compression → 09
Output practice        → 10
Mock                   → 11, 15
Deep context           → 12
Question patterns      → 13
Active recall          → 14
Coverage control       → 16
```

Như vậy bộ KIIP hiện không chỉ có summary mà đã có **input → recall → output → test → audit loop**.

## 5. Những gì cố ý không duplicate

Không copy toàn bộ lịch sử Hàn Quốc vào `07_역사.md`; phần sâu nằm trong `korean_history/`.

Không copy toàn bộ văn hóa Hàn Quốc vào KIIP; phần sâu nằm ở chapter cha `korean_culture/`.

Không tạo lại cùng nội dung cho `영주용` và `귀화용`; dùng tag.

Không đưa mọi current law vào từng chapter; dùng một correction layer để tránh nhiều bản copy mâu thuẫn.

## 6. Tiêu chí “hoàn thiện” cho từng concept

Một concept được coi là đủ khi có:

1. tên tiếng Hàn;
2. nghĩa tiếng Việt dễ hiểu;
3. quan hệ với concept gần nó;
4. bẫy dễ nhầm nếu có;
5. ít nhất một câu hỏi recall hoặc mock;
6. current correction nếu fact có thể đổi;
7. cross-reference sang Master Book nếu cần hiểu sâu.

Các domain hiện đã đạt baseline này cho phần lõi. Những lần update tiếp theo nên ưu tiên **thêm câu hỏi và sửa theo giáo trình/공지 mới**, thay vì tạo lại cây thư mục mới.
