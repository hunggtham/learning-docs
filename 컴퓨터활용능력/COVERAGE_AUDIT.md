# 컴퓨터활용능력 2급 — Coverage Audit

> **목적:** “file이 존재한다”와 “시험 범위를 충분히 가르친다”를 구분한다.  
> **Baseline:** 2024–2026 출제기준 / 2026 시험 준비.  
> **Status vocabulary:** FULL / PARTIAL / MISSING / VERIFY_OFFICIAL.

## 1. 공식 시험 구조

| 항목 | 상태 | Owner |
|---|---|---|
| 2급 필기 — 컴퓨터 일반 | FULL first-pass | 2급/필기/01-컴퓨터-일반.md |
| 2급 필기 — 스프레드시트 일반 | FULL first-pass | 2급/필기/02-스프레드시트-일반.md |
| 2급 필기 문제풀이 workflow | FULL first-pass | 2급/필기/90-필기-문제풀이-전략.md |
| 2급 실기 — 스프레드시트 실무 | FULL first-pass route | 2급/실기/ |
| 공식 세부 출제항목 1:1 trace | VERIFY_OFFICIAL | 다음 audit |
| 공식 연습예제 배점/기능 trace | VERIFY_OFFICIAL | 다음 audit |
| 2027–2029 delta | PARTIAL | EXAM_VERSION_NOTES.md |

## 2. 필기 — 컴퓨터 일반

| Semantic area | 상태 |
|---|---|
| 컴퓨터 시스템 구조 | FULL |
| 운영체제 역할 | FULL |
| Windows 10 기본 요소 | FULL |
| 파일/폴더 | FULL |
| CPU/ALU/Control/Register | FULL |
| 기억장치 계층 | FULL |
| 데이터 표현 | FULL |
| 시스템/응용 소프트웨어 | FULL |
| LAN/WAN, Server/Client | FULL |
| IP/DNS/URL | FULL |
| HTTP/HTTPS/FTP/SMTP/POP3/IMAP | FULL |
| Browser cache/cookie | FULL |
| Email | FULL |
| Bitmap/Vector/Image formats | FULL |
| Audio/Video/Codec | FULL |
| Cloud/IoT/Wireless | FULL |
| CIA/Auth/AuthZ | FULL |
| Encryption/Hash/Signature | FULL |
| Malware/Firewall/Backup | FULL |
| 세부 공식 항목과의 1:1 mapping | VERIFY_OFFICIAL |

## 3. 필기 — 스프레드시트 일반

| Semantic area | 상태 |
|---|---|
| Workbook/Worksheet/Cell/Range | FULL |
| Data type/Input/AutoFill | FULL |
| Relative/Absolute/Mixed reference | FULL |
| Formula/Operator | FULL |
| Basic aggregate functions | FULL |
| IF/AND/OR | FULL |
| Conditional aggregate | FULL |
| Math/Statistics | FULL |
| Text/Date | FULL |
| Lookup | FULL |
| Database functions | FULL |
| Error values | FULL |
| Cell/Number format | FULL |
| Conditional Formatting | FULL |
| Data Validation | FULL |
| Sort/Filter/Advanced Filter | FULL |
| Subtotal/Consolidate | FULL |
| Goal Seek/Data Table/Scenario | FULL |
| PivotTable/PivotChart | FULL |
| Chart | FULL |
| Print | FULL |
| Macro concept | FULL |
| 공식 함수 목록과의 exact coverage | VERIFY_OFFICIAL |

## 4. 실기

| Work area | 상태 | Owner |
|---|---|---|
| Range/Input/Format | FULL first-pass | 실기/01-기본작업.md |
| Conditional Formatting | FULL first-pass | 실기/01-기본작업.md |
| Auto/Advanced Filter | FULL first-pass | 실기/01-기본작업.md |
| Data Validation/Text to Columns | FULL first-pass | 실기/01-기본작업.md |
| Formula/Reference | FULL first-pass | 실기/02-계산작업.md |
| IF/Logical | FULL first-pass | 실기/02-계산작업.md |
| Text/Date/Lookup/DB functions | FULL first-pass | 실기/02-계산작업.md |
| Sort/Subtotal | FULL first-pass | 실기/03-분석작업.md |
| Consolidate | FULL first-pass | 실기/03-분석작업.md |
| Goal Seek/Data Table/Scenario | FULL first-pass | 실기/03-분석작업.md |
| PivotTable/PivotChart | FULL first-pass | 실기/03-분석작업.md |
| Chart | FULL first-pass | 실기/04-기타작업.md |
| Macro | FULL first-pass | 실기/04-기타작업.md |
| 40분 timed workflow | FULL first-pass | 실기/90-실전-모의고사.md |
| 공식 연습예제와 작업 순서 대조 | VERIFY_OFFICIAL | 다음 audit |
| 실제 scoring-sensitive 세부 조건 | VERIFY_OFFICIAL | 다음 audit |

## 5. 아직 “완료”로 선언하지 않는 이유

First-pass 문서는 syllabus의 major concepts와 실기 workflow를 연결했지만, certification library의 Definition of Done은 더 엄격하다.

완료 조건:

1. 공식 출제기준의 모든 세부 semantic unit에 destination이 있어야 한다.
2. 공식 연습예제의 기능을 모두 재현할 수 있어야 한다.
3. 기출/복원 문제에서 반복되는 trap이 concept owner에 연결되어야 한다.
4. 시험에서 요구되는 함수가 빠짐없이 function inventory에 있어야 한다.
5. 2027 개편 전후 차이가 명시되어야 한다.

## 6. 다음 audit 순서

### P0

- 공식 2024–2026 출제기준 PDF를 semantic inventory로 변환
- 2급 세부 항목 → 현재 section mapping
- MISSING/PARTIAL 탐지

### P1

- 공식 실기 연습예제 대조
- 함수 inventory 생성
- chart/macro/analysis 세부 operation 보강

### P2

- 기출/복원 문제 기반 misconception/trap bank
- 2027–2029 delta table
- timed practice set 및 mock set 추가

> **Bàn giao:** 이 audit는 “많이 써 놓은 문서”를 “시험 범위를 검증한 문서”로 바꾸는 품질 gate다.
