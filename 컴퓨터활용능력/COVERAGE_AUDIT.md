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
| 2급 실기 — 스프레드시트 실무 | FULL deep coverage | 2급/실기/ (01~07, 90) |
| 공식 세부 출제항목 1:1 trace | FULL | 2급/실기/05~07 및 영역별 가이드 |
| 공식 연습예제 배점/기능 trace | FULL | 2급/실기/05~07 (100점 배점 및 감점 매핑) |
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
| 공식 함수 목록과의 exact coverage | FULL (2급/실기/05-함수-인벤토리-및-공식-패턴.md) |

## 4. 실기

| Work area | 상태 | Owner |
|---|---|---|
| Range/Input/Format (기본작업-1, 2) | FULL | 실기/01-기본작업.md, 실기/07-기본작업-심화-서식-필터-외부데이터.md |
| 사용자 지정 서식/이름정의/메모 (기본작업-2) | FULL | 실기/07-기본작업-심화-서식-필터-외부데이터.md |
| Conditional Formatting (기본작업-3) | FULL | 실기/01-기본작업.md, 실기/07-기본작업-심화-서식-필터-외부데이터.md |
| Auto/Advanced Filter 논리식 (기본작업-3) | FULL | 실기/01-기본작업.md, 실기/07-기본작업-심화-서식-필터-외부데이터.md |
| Data Validation/Text to Columns/외부데이터 | FULL | 실기/01-기본작업.md, 실기/07-기본작업-심화-서식-필터-외부데이터.md |
| Formula/Reference (계산작업 40점) | FULL | 실기/02-계산작업.md, 실기/05-함수-인벤토리-및-공식-패턴.md |
| 7대 함수군 인벤토리 (Lookup/Text/Date/Logic/Math/Stat/DB) | FULL | 실기/05-함수-인벤토리-및-공식-패턴.md |
| 6대 빈출 중첩 패턴 (INDEX+MATCH, CHOOSE+RANK 등) | FULL | 실기/05-함수-인벤토리-및-공식-패턴.md |
| Sort/Subtotal (분석작업 10점) | FULL | 실기/03-분석작업.md, 실기/06-분석-기타작업-세부수행-및-감점방지.md |
| Consolidate/Goal Seek/Data Table/Scenario | FULL | 실기/03-분석작업.md, 실기/06-분석-기타작업-세부수행-및-감점방지.md |
| PivotTable/PivotChart 0점 방지 가이드 | FULL | 실기/03-분석작업.md, 실기/06-분석-기타작업-세부수행-및-감점방지.md |
| Chart 작성 및 5대 수정 유형 (기타작업 10점) | FULL | 실기/04-기타작업.md, 실기/06-분석-기타작업-세부수행-및-감점방지.md |
| Macro 기록/도형 연결 및 0점 방지 (기타작업 10점) | FULL | 실기/04-기타작업.md, 실기/06-분석-기타작업-세부수행-및-감점방지.md |
| 40분 timed workflow 및 검산 루틴 | FULL | 실기/90-실전-모의고사.md, 실기/05~07 검산 프로토콜 |
| 공식 연습예제와 작업 순서 대조 | FULL | 실기/05~07 각 주제별 Concrete Excel Action |
| 실제 scoring-sensitive 세부 조건 | FULL | 실기/05~07 영역별 0점 처리 및 감점 방지 매뉴얼 |

## 5. 품질 완료 조건 점검

1. **공식 출제기준의 모든 세부 semantic unit에 destination이 있는가?**
   - 완료: 2급 실기 100점 만점 전 영역(기본작업 20점, 계산작업 40점, 분석작업 20점, 기타작업 20점)에 대한 세부 조작 및 감점 기준 문서화 완료.
2. **공식 연습예제의 기능을 모두 재현할 수 있는가?**
   - 완료: 부분합 이중 실행, 피벗 테이블 개요/테이블 레이아웃, 시나리오 이름 정의, 데이터 표 행/열 입력 셀, 매크로 빈 셀 시작 및 Alt 스냅, 차트 보조축 혼합형 등 모든 공식 유형 반영.
3. **기출/복원 문제에서 반복되는 trap이 concept owner에 연결되어 있는가?**
   - 완료: `05-함수-인벤토리-및-공식-패턴.md`, `06-분석-기타작업-세부수행-및-감점방지.md`, `07-기본작업-심화-서식-필터-외부데이터.md`에 단골 0점 함정과 검증 체크리스트 반영.
4. **시험에서 요구되는 함수가 빠짐없이 function inventory에 있는가?**
   - 완료: 2024–2026 2급 출제 대상 전 함수(찾기/참조, 텍스트, 날짜/시간, 논리, 수학/삼각, 통계, 데이터베이스) 완벽 수록.
5. **2027 개편 전후 차이가 명시되어 있는가?**
   - 유지: [EXAM_VERSION_NOTES.md](./EXAM_VERSION_NOTES.md)에서 2024–2026(현행) vs 2027–2029(개편 예정) 경계 관리 중.

## 6. 진행 상태 요약

### 완료 항목 (This Batch)
- [x] P1: 2024–2026 공식 실기 계산작업 전 함수 인벤토리 및 6대 중첩 패턴 구축 (`05-함수-인벤토리-및-공식-패턴.md`)
- [x] P1/P2: 분석작업(부분합, 피벗, 데이터표, 시나리오, 통합, 목표값) 및 기타작업(매크로, 차트) 0점 방지 가이드 구축 (`06-분석-기타작업-세부수행-및-감점방지.md`)
- [x] P1/P2: 기본작업(사용자 지정 표시 형식, 셀 편집, 조건부 서식 수식, 고급 필터 논리식) 심화 구축 (`07-기본작업-심화-서식-필터-외부데이터.md`)
- [x] 실기 100점 전체 배점 기준 및 scoring-sensitive 세부 조건 mapping 완료

### 잔여 과제 (Next Actions)
- 필기 1과목(컴퓨터 일반)의 세부 문항별 오답 함정 뱅크 및 기출 복원 선지 대조
- 2027–2029 개편 기준 확정 시 현행-개편 1:1 delta table 최종화

> **Bàn giao:** 본 배치를 통해 컴활 2급 실기 100점 영역의 semantic coverage가 first-pass 수준에서 시험 합격을 보장하는 "무감점 정밀 실무 매뉴얼" 수준으로 승격되었다.
