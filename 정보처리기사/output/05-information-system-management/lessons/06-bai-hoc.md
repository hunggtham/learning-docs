# 3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)

## 3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)

### 3.1 소프트웨어 프로젝트 관리 (Software Project Management)
Phần “3.1 소프트웨어 프로젝트 관리 (Software Project Management)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 주어진 기간 내에 최소의 비용으로 사용자를 만족시키는 시스템을 개발하기 위한 전반적인 활동.
- **Tiếng Việt:** Hoạt động tổng thể để phát triển hệ thống làm hài lòng người dùng với chi phí tối thiểu trong thời gian quy định.

### 3.2 하향식/상향식 비용 산정 (Cost Estimation)
#### LOC 기법 (Lines of Code)
Phần “LOC 기법 (Lines of Code)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 각 기능의 원시 코드 라인 수의 비관치, 낙관치, 기대치를 측정하여 예측.
- **공식 (Formulas):**
  - 노력(인월, Person-Month) = 개발 기간 × 투입 인원 = LOC / 1인당 월평균 생산 코드 라인 수
  - 개발 비용 = 노력(인월) × 단위 비용
  - 개발 기간 = 노력(인월) / 투입 인원
  - 생산성 = LOC / 노력(인월)
- **Tiếng Việt:** Ước tính dựa trên số dòng code. Tính toán Nỗ lực (Person-Month) = Số dòng code / Số dòng code 1 người viết trong 1 tháng.

#### 수학적 산정 기법 (Mathematical Models)
Phần “수학적 산정 기법 (Mathematical Models)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **COCOMO 모형:** 원시 프로그램의 규모(LOC)와 개발 유형에 의한 비용 산정. 고전 COCOMO의 경계는 조직형 `≤ 50 KDSI`, 반분리형 `> 50 ~ 300 KDSI`, 내장형 `> 300 KDSI`로 겹치지 않게 해석한다.
- **Putnam 모형:** 생명 주기 동안 사용될 노력의 분포를 가정 (Rayleigh-Norden 곡선 기초). **SLIM** 도구 사용.
- **기능 점수 (FP) 모형:** 기능적 요구사항을 점수화. 가중치 증대 요인: 자료 입력, 정보 출력, 명령어(질의), 데이터 파일, 외부 루틴 인터페이스.
- **Tiếng Việt:**
  - COCOMO: Dựa vào số dòng code (LOC). Gồm Organic (nhỏ), Semi-Detached (vừa), Embedded (lớn).
  - Putnam: Dựa trên đường cong Rayleigh-Norden (Công cụ: SLIM).
  - FP (Function Point): Dựa trên tính năng.

### 3.3 일정 관리 (Schedule Management)
Phần “3.3 일정 관리 (Schedule Management)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **PERT (프로그램 평가 및 검토 기술):** 낙관, 가능, 비관적인 경우로 나누어 종료 시기를 결정. 결정 경로와 임계 경로를 알 수 있음.
- **CPM (임계 경로 기법):** 임계 경로는 프로젝트에서 가장 긴(최장) 경로를 의미한다.
- **간트 차트 (Gantt Chart):** 작업 일정을 막대 도표로 표시 (수평 막대 길이는 기간).
- **Tiếng Việt:**
  - PERT: Dựa trên thời gian lạc quan, bi quan, khả thi.
  - Đường găng (Critical Path): Đường dài nhất trong sơ đồ mạng.
  - Biểu đồ Gantt: Thể hiện tiến độ bằng thanh ngang.

### 3.4 위험 관리 및 테일러링 (Risk Management & Tailoring)
Phần “3.4 위험 관리 및 테일러링 (Risk Management & Tailoring)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **위험 관리 (Risk Analysis):** 돌발 상황(위험)을 미리 예상하고 적절한 대책을 수립.
- **방법론 테일러링 (Tailoring):** 프로젝트 상황에 맞게 방법론 절차나 기법을 수정/보완.
  - 내부적 기준: 목표 환경, 요구사항, 프로젝트 규모, 보유 기술.
  - 외부적 기준: 법적 제약사항(Compliance), 표준 품질 기준.
- **Tiếng Việt:** Quản lý rủi ro (lên phương án phòng ngừa) và Cắt may phương pháp (Tailoring) - điều chỉnh quy trình phát triển cho phù hợp với đặc thù dự án.
