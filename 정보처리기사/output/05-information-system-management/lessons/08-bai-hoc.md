# 소프트웨어 비용 산정 기법 (Software Cost Estimation)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **소프트웨어 비용 산정 기법 (Software Cost Estimation)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

소프트웨어, 비용, 산정, 기법

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 소프트웨어 비용 산정 기법 (Software Cost Estimation)

### 1. LOC (Line Of Code) 기법
- 원시 코드(Source Code) 라인 수의 낙관치, 비관치, 기대치를 측정해 예측치를 구하여 비용을 산정.
- **공식**:
  - 노력(인월, Man-Month) = `LOC / 1인당 월평균 생산 코드 라인 수` = `개발 기간 × 투입 인원`
  - 개발 비용 = `노력(인월) × 단위 비용(월평균 인건비)`

### 2. 수학적 산정 기법
과거의 프로젝트 데이터를 기반으로 한 상향식 비용 산정 모델입니다.
- **COCOMO 모형 (Boehm 제안)**: LOC 기반 산정. 고전 COCOMO의 경계는 다음처럼 겹치지 않게 해석한다.
  1. **조직형 (Organic)**: `≤ 50 KDSI` (중소 규모 업무용).
  2. **반분리형 (Semi-Detached)**: `> 50 ~ 300 KDSI` (컴파일러, 유틸리티).
  3. **내장형 (Embedded)**: `> 300 KDSI` (초대형 운영체제, 미사일 제어).
- **Putnam 모형 (생명 주기 예측 모형)**: 시간에 따른 **Rayleigh-Norden 곡선**의 노력 분포도를 기초로 산정.
- **FP (Function Point, 기능 점수) 모형**: 알브레히트(Albrecht) 제안. 기능 요인(입력, 출력, 사용자 질의, 데이터 파일, 외부 인터페이스)별로 가중치를 부여해 산정.

> **Vietnamese Explanation**:
> - **LOC**: Tính chi phí dựa trên số dòng code.
> - **COCOMO**: Phân loại theo độ lớn dự án (Organic: nhỏ, Semi: vừa, Embedded: lớn).
> - **Putnam**: Dựa trên đường cong phân bố nỗ lực theo thời gian Rayleigh-Norden.
> - **FP (Function Point)**: Dựa trên số lượng chức năng phần mềm mang lại cho người dùng.

💡 **Mẹo ghi nhớ (Mnemonics):**
- FP의 5가지 요인: **I.O.Q.F.I** (Input, Output, inQuiry, File, Interface).
