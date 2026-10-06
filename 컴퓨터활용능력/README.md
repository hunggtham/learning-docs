# 컴퓨터활용능력 — Root Entrypoint

컴퓨터활용능력은 대한상공회의소가 시행하는 국가기술자격이며, 이 library는 현재 **2급**을 우선 canonical track으로 구축한다.

## 현재 구현 범위

### 2급 필기

- [컴퓨터 일반](./2급/필기/01-컴퓨터-일반.md)
- [스프레드시트 일반](./2급/필기/02-스프레드시트-일반.md)
- [필기 문제풀이 전략](./2급/필기/90-필기-문제풀이-전략.md)

### 2급 실기

- [기본작업](./2급/실기/01-기본작업.md)
- [계산작업](./2급/실기/02-계산작업.md)
- [분석작업](./2급/실기/03-분석작업.md)
- [기타작업](./2급/실기/04-기타작업.md)
- [실전 모의고사](./2급/실기/90-실전-모의고사.md)

## 시험 baseline

2026년 준비 기준:

- 필기: 컴퓨터 일반 + 스프레드시트 일반
- 실기: 스프레드시트 실무
- 필기: 객관식 40문항 / 40분
- 실기: 컴퓨터 작업형 / 40분
- 필기 합격: 각 과목 40점 이상 + 평균 60점 이상
- 실기 합격: 70점 이상
- 운영체제 baseline: Windows 10
- Office baseline: Microsoft Office LTSC 2021

대한상공회의소는 **2027–2029 출제기준**을 공지했으며 적용 시점은 2027-01-01이다. Version 경계는 [EXAM_VERSION_NOTES.md](./EXAM_VERSION_NOTES.md)에서 관리한다.

## 편집 원칙

이 library는 단순 요약본이 아니라 다음 순서로 만든다.

**concept → mechanism → 비교/함정 → 실제 Excel action → timed practice**

한국어 시험 용어를 유지하고, Vietnamese explanation과 English keyword를 함께 사용한다.

## 품질 상태

현재 2급의 **first-pass learning path는 작성 완료**했다. 다만 “완전한 시험 coverage”라고 선언하지 않는다.

다음 검증 단계:

1. 2024–2026 공식 출제기준 semantic inventory
2. 공식 실기 연습예제 대조
3. 함수/기능 누락 audit
4. 기출·복원 문제로 trap coverage 보강
5. 2027–2029 현행-개편 대조표 기반 delta 반영

상세 상태는 [COVERAGE_AUDIT.md](./COVERAGE_AUDIT.md)에서 추적한다.

## Entrypoint

→ [컴퓨터활용능력 2급 Study Map](./2급/README.md)

> **Bàn giao:** first-pass 문서를 읽는 것만으로 끝내지 않고, coverage audit 후 실제 Excel 반복 훈련과 timed mock을 붙여 “이해 → 수행 → 합격 안정성”으로 완성한다.
