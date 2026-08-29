# Study Plan Import - H2 2026

Generated files:
- `study_plan_2026_06_23_to_2026_12_31.json`: JSON payload with `tasks`, `goals`, `resources`.
- `study_plan_2026_06_23_to_2026_12_31_supabase.sql`: Supabase SQL insert script.
- `study_plan_2026_06_23_to_2026_12_31.xlsx`: readable Excel workbook.

## Date range
2026-06-23 to 2026-12-31

## SQL import steps
1. Open Supabase Dashboard.
2. Go to **Authentication > Users** and copy your `user_id`.
3. Open `study_plan_2026_06_23_to_2026_12_31_supabase.sql`.
4. Replace `PUT-YOUR-USER-ID-HERE` with your UUID.
5. Run the script in **SQL Editor**.

The script deletes previous rows from the same batch before inserting:
- `tasks.note LIKE '%batch_id=study-plan-h2-2026-v1%'`
- `goals.title LIKE '[H2-2026]%'`

## Important assumptions
- SQLD exam fixed: 2026-08-22.
- 정보처리기사 필기: registration around 2026-07-20, exact exam date must be updated after registration.
- 정보처리기사 실기: registration around 2026-09-21 only if 필기 is passed.
- TOPIK exam fixed: 2026-07-05.
- KIIP 심화: planned in August, no exact date provided.
- IELTS class: Tue and Fri late evening.
- Mon/Wed/Thu available 21:00-00:00.
- Weekend available from 11:00/12:00 onward.

## Recommended workflow
- Import the SQL once.
- In the app, update task `status` daily.
- After 2026-07-20, update actual 정보처리기사 필기 exam date.
- After SQLD/정보처리기사 results, convert conditional tasks if needed.
