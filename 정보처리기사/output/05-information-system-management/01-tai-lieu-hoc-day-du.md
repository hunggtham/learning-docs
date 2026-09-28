# Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)

## 학습 목표 (Mục tiêu học tập)

- 시험에서 사용하는 한국어 용어를 영어와 베트남어 뜻까지 함께 인식한다.
- 각 개념을 정의 → 구성요소/절차 → 비교 포인트 → 예시 순서로 설명할 수 있다.
- 앞에서 배운 개념과 뒤의 심화 개념을 연결하여 문제의 조건을 빠르게 해석한다.

## 권장 학습 순서 (Lộ trình đề xuất)

1. 먼저 이 문서의 각 `##` 단원을 순서대로 읽는다.
2. 단원마다 **핵심 키워드**를 소리 내어 읽고, 한국어 원문과 베트남어 설명을 함께 확인한다.
3. 마지막에 `복습 체크리스트`를 점검한 뒤, 세부 lesson 파일에서 헷갈리는 부분을 다시 본다.

> **Nguồn:** tổng hợp từ các Markdown đã generate trong `raw_md/final`, được đối chiếu với các nguồn `raw` và `raw_md` cùng môn. Nội dung gốc được giữ lại; chỉ chuẩn hoá cấu trúc bài học.

> **Quy ước đọc:** thuật ngữ được ưu tiên theo mẫu `한국어 (English) (Tiếng Việt)`. Mỗi ý tiếng Hàn có phần giải thích Việt ngữ liền kề hoặc ngay sau đó; khi gặp từ kỹ thuật trong ngoặc, hãy xem đó là nghĩa cần nhớ khi làm đề.

> **Cách học:** học theo thứ tự các mục; với mỗi mục, xác định khái niệm → cơ chế/quy tắc → ví dụ → mẹo nhớ. Các mục lặp lại ở phần “심화” (nâng cao) dùng để nối kiến thức trước đó với dạng câu hỏi sâu hơn.

> **Mạch nối:** Mỗi mục trong guide phải được đọc như một bước của cùng một chuỗi suy luận. Hãy dùng phần cuối của mục trước để đặt câu hỏi cho mục sau, rồi quay lại checklist để kiểm tra khái niệm vừa được mở rộng; không coi mỗi heading là một ghi chú tách rời.

---

## 1. 소프트웨어 개발 방법론 및 프레임워크 (Phương pháp luận & Framework phát triển PM)

### 1.1 구조적 방법론 (Structured Methodology)
- 정형화된 분석 절차에 따라 사용자 요구사항을 파악하여 문서화하는 **처리(Process) 중심**의 방법론이다.
- 복잡한 문제를 다루기 위해 **분할과 정복 (Divide and Conquer)** 원리를 적용한다.
- **Tiếng Việt:** Là phương pháp luận trung tâm vào xử lý (Process), lập tài liệu yêu cầu người dùng theo quy trình phân tích chuẩn. Áp dụng nguyên lý chia để trị (Divide and Conquer) cho các vấn đề phức tạp.
- **Example:**
  - *KR:* 큰 시스템을 여러 개의 작은 모듈로 나누어 개발.
  - *VN:* Chia một hệ thống lớn thành nhiều mô-đun (module / 모듈) nhỏ để phát triển.

### 1.2 정보공학 방법론 (Information Engineering Methodology)
- 정보 시스템의 개발을 위해 정형화된 기법들을 상호 연관성 있게 통합 및 적용하는 **자료(Data) 중심**의 방법론이다.
- 데이터베이스 설계를 위한 데이터 모델링으로 **개체 관계도 (ERD; Entity Relationship Diagram)**를 사용한다.
- **Tiếng Việt:** Phương pháp luận trung tâm vào dữ liệu (data / 데이터), tích hợp các kỹ thuật chuẩn hóa để phát triển hệ thống. Sử dụng sơ đồ thực thể liên kết (ERD) cho mô hình hóa dữ liệu.
- **Example:**
  - *KR:* 고객과 주문의 관계를 ERD로 모델링하여 시스템 구축.
  - *VN:* Mô hình hóa mối quan hệ giữa Khách hàng và Đơn hàng bằng ERD để xây dựng hệ thống.

### 1.3 컴포넌트 기반(CBD) 방법론 (Component-Based Development)
- 기존의 시스템이나 소프트웨어를 구성하는 **컴포넌트를 조합**하여 하나의 새로운 애플리케이션을 만드는 방법론이다.
- 분석 단계에서 사용자 요구사항 정의서가 산출된다.
- **Tiếng Việt:** Phương pháp luận tạo ứng dụng mới bằng cách kết hợp các thành phần (component / 컴포넌트) có sẵn. Tài liệu định nghĩa yêu cầu được tạo ra ở bước phân tích.
- **Example:**
  - *KR:* 결제 컴포넌트와 장바구니 컴포넌트를 조립하여 쇼핑몰 구축.
  - *VN:* Lắp ráp thành phần (component / 컴포넌트) thanh toán và thành phần (component / 컴포넌트) giỏ hàng để tạo trang thương mại điện tử.
- 💡 **Mẹo ghi nhớ:** CBD = "Lego" (lắp ráp các mảnh ghép có sẵn).

### 1.4 소프트웨어 개발 프레임워크 (Software Development Framework)
- 공통적으로 사용되는 구성 요소와 아키텍처를 일반화하여 제공해주는 반제품 형태의 소프트웨어 시스템.
- 사업자 종속성이 해소되며, 객체들의 제어를 프레임워크에 넘김으로써 생산성을 향상시킨다.
- **Tiếng Việt:** Hệ thống phần mềm dạng bán thành phẩm cung cấp các thành phần và kiến trúc chung. Giải quyết sự phụ thuộc vào nhà cung cấp và tăng năng suất.
- **Example:**
  - *KR:* Spring 프레임워크를 사용하여 Java 웹 애플리케이션을 빠르게 개발.
  - *VN:* Sử dụng Spring khung phần mềm (framework / 프레임워크) để phát triển nhanh ứng dụng web Java.

---

> **Mạch chuyển:** Từ **1. 소프트웨어 개발 방법론 및 프레임워크 (Phương pháp luận & Framework phát triển PM)**, chuyển sang **소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)

### 1. 테일러링 (Tailoring)
프로젝트 특성에 맞게 개발 방법론의 절차나 기법을 수정 및 보완하는 작업.
- **내부적 기준**: 목표 환경, 요구사항, 프로젝트 규모, 보유 기술.
- **외부적 기준**: 법적 제약사항, 표준 품질 기준.

### 2. 소프트웨어 개발 프레임워크 (Framework)
공통 사용되는 구성 요소와 아키텍처를 일반화하여 제공하는 반제품 형태의 시스템. (예외 처리, 트랜잭션, DB 연동 등 기본 기능 제공).
- **종류**: 스프링(Spring - Java용), 닷넷(.NET - Windows용), 전자정부 프레임워크(공공부문 지원).

---

> **Mạch chuyển:** Từ **소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)**, chuyển sang **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 프레임워크 특징 및 SW 신기술 (Framework & SW Tech)

### 1. 프레임워크의 특성 (Characteristics of Framework)
- **모듈화 (Modularity)**: 캡슐화로 모듈화를 강화하여 변경 영향을 최소화.
- **재사용성 (Reusability)**: 재사용 가능한 모듈 제공으로 생산성 향상.
- **확장성 (Extensibility)**: 다형성을 통한 인터페이스 확장.
- **제어의 역흐름 (Inversion of Control)**: 개발자가 아닌 프레임워크가 객체들을 제어하고 통제.

### 2. SDE (Software-Defined Everything)
하드웨어 자원을 가상화하여 소프트웨어만으로 제어 및 관리하는 기술.
- **SDN**: 소프트웨어 정의 네트워킹 (네트워크 가상화)
- **SDDC**: 소프트웨어 정의 데이터 센터 (데이터 센터 전체 가상화)
- **SDS**: 소프트웨어 정의 스토리지 (스토리지 가상화)

### 3. 주요 SW 및 관련 용어
- **SOA (Service Oriented Architecture)**: 서비스나 컴포넌트 중심으로 구축하는 아키텍처.
- **디지털 트윈 (Digital Twin)**: 물리적 자산을 소프트웨어로 가상화(복제)하여 효율성을 높이는 기술.
- **텐서플로 (TensorFlow)**: 구글이 만든 딥러닝/데이터 흐름용 오픈소스 라이브러리.
- **도커 (Docker)**: 컨테이너(Container) 기술을 자동화하는 오픈소스 프로젝트.

---

> **Mạch chuyển:** Từ **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)**, chuyển sang **5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크

---

> **Mạch chuyển:** Từ **5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크**, chuyển sang **336. 소프트웨어 개발 프레임워크 (Software Development Framework)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 336. 소프트웨어 개발 프레임워크 (Software Development Framework)
- **개념**: 개발에 공통 사용되는 구조를 제공하여 생산성을 높이는 기반.
- **특성**: 모듈화, 재사용성, 확장성, **제어의 역흐름(IoC)**.
- **Tiếng Việt**: Nền tảng cấu trúc sẵn giúp tăng năng suất (như Spring, .NET). Đặc tính: mô-đun (module / 모듈) hóa, Tái sử dụng, Mở rộng, Đảo ngược luồng điều khiển (IoC).

### 자주 혼동하는 판별 포인트

- COCOMO의 고전 유형은 **Organic / Semi-Detached / Embedded**이며 Sequential은 유형명이 아니다.
- RIP는 거리 벡터 방식이고 최대 15홉을 사용한다. OSPF는 링크 상태 방식, BGP는 AS 간 경로 제어다.
- AES·DES·SEED는 대칭키, RSA는 공개키 알고리즘이다. 해시(MD5/SHA 계열)는 암·복호화 키를 교환하는 알고리즘이 아니라 일방향 요약 함수다.
- Chinese Wall은 이해상충 방지, Bell-LaPadula는 기밀성, Biba는 무결성 중심 모델이다.

---

> **Mạch chuyển:** Từ **336. 소프트웨어 개발 프레임워크 (Software Development Framework)**, chuyển sang **3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)

### 3.1 소프트웨어 프로젝트 관리 (Software Project Management)
- 주어진 기간 내에 최소의 비용으로 사용자를 만족시키는 시스템을 개발하기 위한 전반적인 활동.
- **Tiếng Việt:** Hoạt động tổng thể để phát triển hệ thống làm hài lòng người dùng với chi phí tối thiểu trong thời gian quy định.

### 3.2 하향식/상향식 비용 산정 (Cost Estimation)
#### LOC 기법 (Lines of Code)
- 각 기능의 원시 코드 라인 수의 비관치, 낙관치, 기대치를 측정하여 예측.
- **공식 (Formulas):**
  - 노력(인월, Person-Month) = 개발 기간 × 투입 인원 = LOC / 1인당 월평균 생산 코드 라인 수
  - 개발 비용 = 노력(인월) × 단위 비용
  - 개발 기간 = 노력(인월) / 투입 인원
  - 생산성 = LOC / 노력(인월)
- **Tiếng Việt:** Ước tính dựa trên số dòng mã (code / 코드). Tính toán Nỗ lực (Person-Month) = Số dòng mã (code / 코드) / Số dòng mã (code / 코드) 1 người viết trong 1 tháng.

#### 수학적 산정 기법 (Mathematical Models)
- **COCOMO 모형:** 원시 프로그램의 규모(LOC)와 개발 유형에 의한 비용 산정. 고전 COCOMO의 경계는 조직형 `≤ 50 KDSI`, 반분리형 `> 50 ~ 300 KDSI`, 내장형 `> 300 KDSI`로 겹치지 않게 해석한다.
- **Putnam 모형:** 생명 주기 동안 사용될 노력의 분포를 가정 (Rayleigh-Norden 곡선 기초). **SLIM** 도구 사용.
- **기능 점수 (FP) 모형:** 기능적 요구사항을 점수화. 가중치 증대 요인: 자료 입력, 정보 출력, 명령어(질의), 데이터 파일, 외부 루틴 인터페이스.
- **Tiếng Việt:**
  - COCOMO: Dựa vào số dòng mã (code / 코드) (LOC). Gồm Organic (nhỏ), Semi-Detached (vừa), Embedded (lớn).
  - Putnam: Dựa trên đường cong Rayleigh-Norden (Công cụ: SLIM).
  - FP (Function Point): Dựa trên tính năng.

### 3.3 일정 관리 (Schedule Management)
- **PERT (프로그램 평가 및 검토 기술):** 낙관, 가능, 비관적인 경우로 나누어 종료 시기를 결정. 결정 경로와 임계 경로를 알 수 있음.
- **CPM (임계 경로 기법):** 임계 경로는 프로젝트에서 가장 긴(최장) 경로를 의미한다.
- **간트 차트 (Gantt Chart):** 작업 일정을 막대 도표로 표시 (수평 막대 길이는 기간).
- **Tiếng Việt:**
  - PERT: Dựa trên thời gian lạc quan, bi quan, khả thi.
  - đường găng (critical path / 임계 경로): Đường dài nhất trong sơ đồ mạng.
  - Biểu đồ Gantt: Thể hiện tiến độ bằng thanh ngang.

### 3.4 위험 관리 및 테일러링 (Risk Management & Tailoring)
- **위험 관리 (Risk Analysis):** 돌발 상황(위험)을 미리 예상하고 적절한 대책을 수립.
- **방법론 테일러링 (Tailoring):** 프로젝트 상황에 맞게 방법론 절차나 기법을 수정/보완.
  - 내부적 기준: 목표 환경, 요구사항, 프로젝트 규모, 보유 기술.
  - 외부적 기준: 법적 제약사항(Compliance), 표준 품질 기준.
- **Tiếng Việt:** Quản lý rủi ro (lên phương án phòng ngừa) và Cắt may phương pháp (Tailoring) - điều chỉnh quy trình phát triển cho phù hợp với đặc thù dự án.

---

> **Mạch chuyển:** Từ **3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)**, chuyển sang **프로젝트 일정 관리 (Project Schedule Management)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 프로젝트 일정 관리 (Project Schedule Management)

### 1. PERT (Program Evaluation and Review Technique)
과거 경험이 없어 예측이 어려운 프로젝트에 사용. 각 작업별로 낙관치, 기대치, 비관치를 나누어 종료 시기를 계산합니다.
- `예측치 = (비관치 + 4*기대치 + 낙관치) / 6`

### 2. CPM (Critical Path Method, 임계 경로 기법)
작업 사이의 의존 관계를 노드와 간선으로 구성. 네트워크에서 최장 경로가 **임계 경로(Critical Path)**가 됩니다.

### 3. 간트 차트 (Gantt Chart, 시간선 차트)
각 작업의 시작과 종료를 막대 도표로 표시하는 일정표. 적응성이 약하지만 이정표와 작업 기간을 한눈에 파악하기 쉽습니다.

---

> **Mạch chuyển:** Từ **프로젝트 일정 관리 (Project Schedule Management)**, chuyển sang **소프트웨어 비용 산정 기법 (Software Cost Estimation)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

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
> - **LOC**: Tính chi phí dựa trên số dòng mã (code / 코드).
> - **COCOMO**: Phân loại theo độ lớn dự án (Organic: nhỏ, Semi: vừa, Embedded: lớn).
> - **Putnam**: Dựa trên đường cong phân bố nỗ lực theo thời gian Rayleigh-Norden.
> - **FP (Function Point)**: Dựa trên số lượng chức năng phần mềm mang lại cho người dùng.

💡 **Mẹo ghi nhớ (Mnemonics):**
- FP의 5가지 요인: **I.O.Q.F.I** (Input, Output, inQuiry, File, Interface).

---

> **Mạch chuyển:** Từ **소프트웨어 비용 산정 기법 (Software Cost Estimation)**, chuyển sang **323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)
- **개념**: 통계 공식을 활용한 비용 예측 기법 (Dự toán chi phí dựa trên công thức toán học).
- **종류**:
  - **COCOMO**: LOC(라인 수) 기반 (Dựa vào số dòng code).
  - **Putnam**: 시간에 따른 인력 분포 곡선(Rayleigh-Norden) 활용 (Dựa vào đường cong phân bổ nhân lực).
  - **FP (Function Point)**: 입력, 출력, 인터페이스 등 기능적 요인 기반 (Dựa vào điểm chức năng).

---

> **Mạch chuyển:** Từ **323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)**, chuyển sang **4. 프로세스 품질 표준 (Tiêu chuẩn chất lượng quy trình)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 4. 프로세스 품질 표준 (Tiêu chuẩn chất lượng quy trình)

### 4.1 ISO/IEC 12207
- **기본 생명 주기:** 획득, 공급, 개발, 운영, 유지보수.
- **지원 생명 주기:** 품질 보증, 검증, 확인, 문서화, 형상 관리 등.
- **조직 생명 주기:** 관리, 기반 구조, 훈련, 개선.
- **Tiếng Việt:** Tiêu chuẩn vòng đời phần mềm gồm: Cơ bản, Hỗ trợ, Tổ chức.

### 4.2 CMMI 성숙도 5단계 (CMMI Maturity Levels)
1. **초기 (Initial):** 프로세스 없음.
2. **관리 (Managed):** 프로젝트 단위 관리.
3. **정의 (Defined):** 조직 차원 표준화.
4. **정량적 관리 (Quantitatively Managed):** 통계적 측정.
5. **최적화 (Optimizing):** 지속적 개선.
- **Tiếng Việt:** 5 cấp độ trưởng thành: Khởi tạo -> Được quản lý -> Được định nghĩa -> Quản lý định lượng -> Tối ưu hóa.
- 💡 **Mẹo ghi nhớ:** I - M - D - Q - O.

### 4.3 SPICE (ISO/IEC 15504)
- 소프트웨어 프로세스 평가 및 개선 국제 표준.
- **수행 능력 6단계 (Capability Levels):**
  - 0: 불완전 (Incomplete)
  - 1: 수행 (Performed)
  - 2: 관리 (Managed)
  - 3: 확립 (Established)
  - 4: 예측 (Predictable)
  - 5: 최적화 (Optimizing)
- **Tiếng Việt:** Đánh giá năng lực quy trình phần mềm từ Cấp 0 (Chưa hoàn chỉnh) đến Cấp 5 (Tối ưu hóa).

---

> **Mạch chuyển:** Từ **4. 프로세스 품질 표준 (Tiêu chuẩn chất lượng quy trình)**, chuyển sang **소프트웨어 프로세스 품질 및 성숙도 표준 (Quality & Maturity Standards)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 소프트웨어 프로세스 품질 및 성숙도 표준 (Quality & Maturity Standards)

### 1. ISO/IEC 12207
표준 소프트웨어 생명 주기 프로세스. 3가지(기본, 지원, 조직 프로세스)로 분류.

### 2. CMMI (Capability Maturity Model Integration)
조직의 성숙도를 평가하는 모델 (5단계).
- **초기(Initial) -> 관리(Managed) -> 정의(Defined) -> 정량적 관리(Quantitatively Managed) -> 최적화(Optimizing)**

### 3. SPICE (ISO/IEC 15504)
프로세스 수행 능력 단계를 평가 (6단계).
- **불완전(Incomplete) -> 수행(Performed) -> 관리(Managed) -> 확립(Established) -> 예측(Predictable) -> 최적화(Optimizing)**

> **Vietnamese Explanation**:
> Các tiêu chuẩn như CMMI và SPICE dùng để đánh giá xem một công ty phần mềm làm việc chuyên nghiệp đến đâu. CMMI có 5 cấp độ (từ lộn xộn đến tối ưu hóa liên tục), còn SPICE có 6 cấp độ.

---

> **Mạch chuyển:** Từ **소프트웨어 프로세스 품질 및 성숙도 표준 (Quality & Maturity Standards)**, chuyển sang **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)

### 1.1 데이터 통신 및 주요 발전
- **데이터 통신:** 컴퓨터와 통신기기 사이에서 디지털(0과 1) 정보를 송수신. (데이터 통신 = 데이터 전송 기술 + 데이터 처리 기술).
- **정보 통신:** 전기 통신 + 컴퓨터 (정보 처리). 통신의 3요소: 정보원, 수신원, 전송 매체.
- **주요 시스템:**
  - `SAGE`: 최초의 데이터 통신 시스템.
  - `SABRE`: 최초 상업용.
  - `ARPANET`: 인터넷의 효시.
  - `ALOHA`: 최초 무선 패킷 교환.
- **Tiếng Việt:** Truyền thông dữ liệu truyền thông tin số (0, 1). 3 yếu tố: Nguồn, Đích, Môi trường truyền. ARPANET là tiền thân của Internet.

### 1.2 통신 회선 및 매체 (Transmission Media)
- **꼬임선 (Twisted Pair):** 저렴하고 설치 간편, 간섭에 취약.
- **동축 케이블 (Coaxial Cable):** 대역폭이 넓고 누화 적음, 중계기 필요.
- **광섬유 케이블 (Optical Fiber):** 빛의 반사 원리. 가장 빠르고 대역폭 큼. 도청 어려워 보안성 우수. 무유도, 무누화.
- **마이크로파/위성 통신:** 장거리 대용량 통신. 다중 접속 방식: FDMA(주파수), TDMA(시간), CDMA(코드).
- **Tiếng Việt:**
  - Twisted Pair: Rẻ, dễ nhiễu.
  - Coaxial: Băng thông rộng, ít nhiễu.
  - Optical Fiber: Cáp quang (phản xạ ánh sáng), siêu tốc, siêu bảo mật.
  - Vệ tinh: Phân chia theo Tần số (FDMA), Thời gian (TDMA), Mã (CDMA).

### 1.3 통신 제어장치 (CCU) & 전처리기 (FEP)
- **CCU:** 데이터 신호의 직·병렬 변환 등 전반적인 제어.
- **FEP (Front-End Processor):** 호스트와 단말기 사이에 위치해 통신 제어를 전담하여 메인 컴퓨터의 부하를 줄임.
- **Tiếng Việt:** CCU điều khiển truyền tải. FEP xử lý tiền kỳ để giảm tải cho máy chủ (Host).

---

> **Mạch chuyển:** Từ **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)**, chuyển sang **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)

### 2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)
- **방향에 따른 분류:** 단방향 (Simplex), 반이중 (Half-Duplex, 무전기), 전이중 (Full-Duplex, 전화).
- **비동기식 (Asynchronous):** 문자마다 Start Bit / Stop Bit를 붙여 전송. 저속 단거리, 오버헤드 큼.
- **동기식 (Synchronous):** 프레임(블록) 단위로 일시에 전송. 속도 빠르고 효율 좋음. 비트/블록 동기 방식.
- **Tiếng Việt:**
  - Đơn công (Simplex), Bán song công (Half-Duplex), Song công toàn phần (Full-Duplex).
  - Bất đồng bộ: Dùng Start/Stop bit (overhead cao). Đồng bộ: Truyền theo khối (block / 블록) (nhanh, hiệu quả).

### 2.2 신호 변환 장치 (MODEM & DSU)
- **모뎀 (MODEM):** 디지털 ↔ 아날로그 변환.
- **DSU (Digital Service Unit):** 디지털 ↔ 디지털 (단극성 ↔ 양극성 변환). 디지털 전용선에 사용.
- **Tiếng Việt:** MODEM (Chuyển đổi Số <-> Tương tự). DSU (Chuyển đổi Số <-> Số).
- 💡 **Mẹo ghi nhớ:** MO-Dem = MOdulation - DEModulation. D-SU = Digital - Digital.

### 2.3 디지털 변조 (Digital Modulation - Keying)
- **ASK (진폭 편이):** 진폭 변화.
- **FSK (주파수 편이):** 주파수 변화 (1,200bps 이하).
- **PSK (위상 편이):** 위상 변화 (중/고속 모뎀).
- **QAM (직교 진폭 변조):** 진폭과 위상 동시 변화 (고속, 9,600bps 표준).
- **Tiếng Việt:** Điều chế tín hiệu số sang tương tự: ASK (Biên độ), FSK (Tần số), PSK (Pha), QAM (Biên độ + Pha kết hợp cho tốc độ cao).

### 2.4 PCM (Pulse Code Modulation)
- 아날로그 데이터를 디지털 신호로 변환. CODEC 이용.
- **과정:** 표본화(Sampling) → 양자화(Quantizing) → 부호화(Encoding) → 복호화(Decoding) → 여파화(Filtering).
- **표본화 (Sampling):** 횟수 = 2 × 최고 주파수.
- **Tiếng Việt:** Biến đổi Tương tự -> Số (dùng CODEC). Quá trình: Lấy mẫu -> Lượng tử hóa -> Mã hóa.
- 💡 **Mẹo ghi nhớ:** Mẫu Lượng Mã Giải Lọc (Lấy mẫu -> Lượng tử hóa -> Mã hóa -> Giải mã -> Lọc).

---

> **Mạch chuyển:** Từ **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)**, chuyển sang **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)

### 3.1 다중화기 (Multiplexer)
- 여러 단말기가 하나의 통신 회선을 공유.
- **FDM (주파수 분할 다중화):** 주파수를 분할. 보호 대역(Guard Band) 필요(대역폭 낭비). 아날로그, 비동기식.
- **TDM (시분할 다중화):** 시간을 분할(Time Slot). 동기식/디지털.
  - **STDM (동기식):** 데이터 유무 상관없이 고정 시간 폭 할당 (효율 낮음).
  - **ATDM (비동기식/통계적):** 데이터가 있는 단말에만 시간 할당 (효율 높음).
- **역 다중화기 (Inverse MUX):** 하나의 고속 채널을 2개의 저속 채널로 분할.
- **집중화기 (Concentrator):** 회선이 부족할 때 동적으로 할당(버퍼 필요). (입력 > 출력 회선).
- **Tiếng Việt:**
  - FDM: Chia tần số (cần khoảng vệ bảo vệ Guard Band).
  - TDM: Chia thời gian. (STDM: Cố định, ATDM: Động/Thống kê).
  - Concentrator: Gom kênh, cần bộ đệm, số đầu vào > đầu ra.

### 3.2 통신 속도 (Speed Metrics)
- **변조 속도 (Baud):** 1초 동안 신호 변화 횟수. (Baud = Bps / 상태 변화 수).
- **신호 속도 (Bps):** 1초 동안 전송 비트 수.
- **상태 변화 수:** Mono(1), Di(2), Tri(3), Quad(4) bit.
- **Tiếng Việt:** Baud: Số lần đổi trạng thái/s. Bps: Số bit/s.

### 3.3 전송 제어 (Transmission Control)
- **5단계 절차:** 회선 접속 → 링크 설정 → 메시지 전송 → 링크 해제 → 회선 절단.
- **전송 제어 문자:**
  - `SYN`: 동기화
  - `SOH`/`STX`/`ETX`/`ETB`/`EOT`: 헤더, 텍스트(본문), 블록, 전송 종료
  - `ENQ`: 링크 설정 요구
  - `DLE`: 데이터 링크 이스케이프 (투과성 확보)
  - `ACK`/`NAK`: 긍정/부정 응답
- **Tiếng Việt:** Các ký tự điều khiển: SYN (Đồng bộ), STX (Bắt đầu văn bản), ETX (Kết thúc văn bản), ACK (Xác nhận), NAK (Từ chối).

### 3.4 HDLC 프로토콜 (High-level Data Link Control)
- **비트(Bit) 위주**의 프로토콜. 전이중/반이중 지원, 동기식 전송.
- **비트 투과성 (Bit Stuffing):** 연속된 '1'이 5개면 강제로 '0' 추가 (플래그 `01111110`과 구분).
- **프레임 종류:**
  - **I (정보):** 데이터 전달 (0으로 시작).
  - **S (감독):** 오류/흐름 제어 (10).
  - **U (비번호):** 링크 모드 설정 (11).
- **전송 모드:** NRM (정규), ARM (비동기), ABM (비동기 균형 - 전이중 P2P).
- **Tiếng Việt:** HDLC là giao thức truyền theo bit. Dùng "Bit Stuffing" để chèn bit '0' sau 5 bit '1' liên tiếp. 3 loại Frame: I (Thông tin), S (Giám sát), U (Không số).

---

> **Mạch chuyển:** Từ **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)**, chuyển sang **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)

### 4.1 오류 발생 원인 및 제어 (Error Causes & Control)
- **원인:** 감쇠, 지연 왜곡, 상호 변조, 누화 잡음, 충격성 잡음(디지털 통신 주요인).
- **FEC (순방향 오류 수정):** 여분 비트를 함께 보내 수신 측이 재전송 없이 오류를 검출·수정 (해밍 코드 등). 오버헤드가 크고 역채널이 필요 없다.
- **BEC/ARQ (역방향 오류 제어):** 수신 측이 오류를 검출한 뒤 송신 측에 재전송을 요청한다. CRC·패리티는 주로 검출에 사용되고, Stop-and-Wait·Go-Back-N·Selective Repeat가 대표적인 ARQ 방식이다.
- **Tiếng Việt:**
  - FEC: Tự sửa lỗi (vd: Hamming Code).
  - BEC: Yêu cầu gửi lại (vd: CRC, Parity).

### 4.2 ARQ (자동 반복 요청) 및 오류 검출 방식
- **ARQ 종류:**
  - **Stop-and-Wait:** 한 블록 보내고 기다림.
  - **Go-Back-N:** 오류 발생 지점부터 *모두* 재전송.
  - **Selective Repeat:** 오류 발생 블록*만* 재전송 (버퍼 필요, 복잡).
  - **Adaptive:** 채널 상태에 따라 동적 변경.
- **오류 검출 및 수정:**
  - **패리티 (Parity):** 1비트 검출, 짝수오류 검출 불가.
  - **CRC:** 다항식 기반, 집단 오류 검출 특화 (HDLC 사용).
  - **해밍 코드 (Hamming Code):** 1비트 *수정* 가능. `2^n` 번째 자리에 비트 삽입.
- **Tiếng Việt:**
  - Go-Back-N: Gửi lại từ lỗi. Selective Repeat: Chỉ gửi lại gói lỗi.
  - CRC: Kiểm tra đa thức (phổ biến nhất). Hamming mã (code / 코드): Sửa được lỗi 1 bit.

### 4.3 교환 방식 (Switching Methods)
- **회선 교환 (Circuit Switching):** 물리적 전용선 할당. 고정 대역, 연속적 데이터 전송. (접속 지연 O, 전송 지연 X). 전화망.
- **축적 교환 (Store-and-Forward):** 데이터를 저장했다가 경로를 찾아 전송.
  - **메시지 교환 (Message Switching):** 전체 메시지 전송. 지연 매우 긺.
  - **패킷 교환 (Packet Switching):** 패킷 단위로 잘라서 전송 (다음 파트에서 상세 서술).
- **Tiếng Việt:**
  - Circuit Switching (Chuyển mạch kênh): Tạo đường truyền vật lý (Điện thoại).
  - Message Switching (Chuyển mạch thông điệp): Lưu rồi chuyển toàn bộ.

### 4.4 패킷 교환 방식 및 네트워크 기능 (Packet Switching & Network Functions)
- **가상 회선 (Virtual Circuit):** 패킷 교환 전에 논리적인 가상 회선을 설정. 전송 순서가 보장되며 신뢰성이 높음. (호 설정 → 데이터 전송 → 호 해제).
- **데이터그램 (Datagram):** 연결 경로 설정 없이 각 패킷이 독립적으로 운반됨. 패킷마다 경로가 다르고 순서가 다를 수 있음. 짧은 데이터 전송에 적합.
- **패킷 교환망의 기능:** 패킷 다중화, 논리 채널 설정, 경로 제어, 순서 제어, 트래픽 제어, 오류 제어.
- **Tiếng Việt:**
  - Virtual Circuit: Tạo đường dẫn ảo trước khi truyền (thứ tự được đảm bảo).
  - Datagram: Truyền độc lập không cần tạo đường dẫn (thứ tự có thể thay đổi).

### 4.5 트래픽 제어 및 라우팅 심화 (Traffic Control & Routing)
- **경로 설정 방식 (Routing Strategies):**
  - **고정 경로 (Static):** 미리 정해진 경로 사용.
  - **적응 경로 (Adaptive):** 트래픽 상황에 따라 동적 변경.
  - **범람 (Flooding):** 모든 경로로 패킷 복사 전송 (네트워크 정보 불필요).
  - **임의 경로 (Random):** 인접 교환기 중 임의 선택.
- **폭주(혼잡) 제어 (Congestion Control):** 오버플로를 방지하기 위해 네트워크 내 패킷 수 조절.
- **Tiếng Việt:** Routing có Static (Tĩnh), Adaptive (Động), Flooding (Tràn ngập). Congestion điều khiển (control / 제어) giúp chống quá tải mạng.

---

> **Mạch chuyển:** Từ **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)**, chuyển sang **⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## ⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)

---

> **Mạch chuyển:** Từ **⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)**, chuyển sang **2. 자원 처리 오류 (Resource Handling Errors)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 2. 자원 처리 오류 (Resource Handling Errors)
- **부적절한 자원 해제 (Improper Resource Release)**: 힙 메모리나 소켓을 사용 후 반환(close)하지 않아 자원 고갈 발생. (Không giải phóng bộ nhớ, kết nối sau khi dùng xong).
- **해제된 자원 사용 (Use After Free)**: 반환된 메모리를 다시 참조하여 오작동 유발. (Dùng lại vùng nhớ đã được giải phóng).
- **초기화되지 않은 변수 사용 (Uninitialized Variable)**: 변수 선언 후 값을 넣지 않고 사용하여 이전 쓰레기 값이 노출됨. (Dùng biến chưa khởi tạo giá trị).

---

> **Mạch chuyển:** Từ **2. 자원 처리 오류 (Resource Handling Errors)**, chuyển sang **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)

### 5.1 신기술 동향 (New Technologies)
- **SDN (Software Defined Networking):** 네트워크를 가상화하여 소프트웨어로 제어/관리.
- **SDS (Software-Defined Storage):** 물리적 스토리지를 가상화하여 하나처럼 관리.
- **SDDC (Software Defined Data Center):** 데이터 센터의 모든 자원을 가상화하여 소프트웨어 조작만으로 자동 제어.
- **클라우드 기반 HSM:** 클라우드 기반 암호화 키 생성/처리 하드웨어 보안기기.
- **파스-타 (PaaS-TA):** 개발 환경을 제공하는 개방형 클라우드 플랫폼.
- **징 (Zing):** 10cm 이내에서 3.5Gbps 속도의 초고속 근접무선통신.
- **스마트 그리드 (Smart Grid):** 전력선을 기반으로 효율적 에너지 관리 통합 시스템.
- **SSO (Single Sign On):** 한 번 로그인으로 여러 사이트 이용.
- **메시 네트워크 (Mesh Network):** 여러 디바이스를 그물망처럼 유기적으로 연결.
- **피코넷 (PICONET):** 블루투스/UWB 기술로 형성하는 독립적 무선망.
- **Tiếng Việt:**
  - SDN/SDS/SDDC: Ảo hóa và điều khiển mạng/lưu trữ/trung tâm dữ liệu bằng phần mềm.
  - PaaS-TA: Nền tảng cloud mở của Hàn Quốc.
  - SSO: Đăng nhập một lần.
  - Zing: Giao tiếp không dây tầm cực gần, tốc độ cao.

### 5.2 LAN 표준 및 위상 (LAN Standards & Topology)
- **CSMA/CD:** IEEE 802.3 유선 LAN 매체 접속 제어 방식 (충돌 감지).
- **CSMA/CA:** 무선 랜(WLAN) 데이터 전송 시 충돌을 피하기 위해 일정 시간 기다림 (충돌 회피).
- **WPA (Wi-Fi Protected Access):** 무선 랜 인증/암호화 표준.
- **802.11e:** QoS 기능 지원을 위해 MAC 계층 수정.
- **버스형 (Bus Topology):** 한 통신 회선에 여러 단말장치 연결.
- **VLAN (Virtual LAN):** 물리적 배치와 무관하게 논리적으로 네트워크 분리.
- **WDM (Wavelength Division Multiplexing):** 파장이 다른 광선을 이용해 동시 통신 (광다중화).
- **Tiếng Việt:**
  - CSMA/CD: Phát hiện xung đột (Mạng có dây).
  - CSMA/CA: Tránh xung đột (Mạng không dây).
  - VLAN: Mạng LAN ảo, phân chia lô-gic (logic / 논리) không phụ thuộc vật lý.

### 5.3 라우팅 프로토콜 및 흐름 제어 (Routing Protocols & Flow Control)
- **ARP (Address Resolution Protocol):** IP 주소를 MAC 주소로 변환.
- **RIP (Routing Information Protocol):** 거리 벡터 라우팅 (최대 홉 15 제한).
- **OSPF (Open Shortest Path First):** 링크 상태 기반 최단 경로 라우팅 (대규모 망).
- **흐름 제어 - 정지-대기 (Stop-and-Wait):** 수신 측의 ACK(확인 신호)를 받은 후 다음 패킷 전송.
- **Tiếng Việt:**
  - ARP: IP -> MAC.
  - RIP: Dựa trên số Hop (tối đa 15).
  - OSPF: Dựa trên trạng thái Link, tìm đường ngắn nhất.
  - Stop-and-Wait: Chờ phản hồi (ACK) rồi mới gửi tiếp.

---

> **Mạch chuyển:** Từ **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)**, chuyển sang **5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)

### 5.1 LAN 및 매체 접근 제어 (LAN & MAC)
- **LAN (Local Area Network):** 단일 기관 소유, 고속 전송, 오류율 낮음.
- **IEEE 802 주요 규격:**
  - `802.1` (전체 구성), `802.2` (LLC), `802.3` (CSMA/CD), `802.4` (토큰 버스), `802.5` (토큰 링), `802.11` (무선 LAN).
- **CSMA/CD (Carrier Sense Multiple Access/Collision Detection):** 채널 사용권 경쟁. 충돌 감지.
  - 규격 명칭 (예: `10 BASE T` - 10Mbps, 베이스밴드, 꼬임선).
  - **이더넷 (Ethernet):** CSMA/CD 방식을 사용하는 LAN.
- **Tiếng Việt:** Mạng LAN cục bộ. IEEE 802.3 là tiêu chuẩn CSMA/CD (Ethernet - phát hiện xung đột).

### 5.2 기타 통신망 (VAN, ISDN)
- **VAN (부가 가치 통신망):** 공중 통신망을 임대해 정보 가공/변환 등 부가 가치를 첨가해 서비스 제공.
- **ISDN (종합 정보 통신망):** 음성/문자/영상을 디지털 방식으로 종합 제공.
- **Tiếng Việt:**
  - VAN: Mạng giá trị gia tăng (thuê đường truyền, thêm dịch vụ).
  - ISDN: Mạng số đa dịch vụ tích hợp.

### 5.3 인터넷 주소 체계 (IP Addresses)
- **IPv4:** 32비트 (8비트 × 4부분). 클래스 A~E (A: 대형 ~ C: 소규모망, D: 멀티캐스트).
- **IPv6:** 128비트 (16비트 × 8부분, 16진수, 콜론 `:` 구분)로 주소 공간을 확장한다. 기본 헤더는 단순화되고 브로드캐스트 대신 멀티캐스트·애니캐스트를 사용한다.
- **IPv4 → IPv6 전환 전략:** 듀얼 스택(Dual Stack), 터널링(Tunneling), 헤더/전송/응용 게이트웨이 변환(Translation).
- **DNS (Domain Name System):** 문자 도메인 네임을 IP 주소로 변환.
- **Tiếng Việt:** IPv4 (32 bit, Class A-E). IPv6 (128 bit, giải quyết cạn kiệt IP). DNS dịch tên miền sang IP.
- 💡 **Mẹo ghi nhớ:** Chuyển đổi IPv4/IPv6: "Dual - Tunnel - Translate".

### 5.4 네트워크 관련 장비 (Network Devices)
- **허브 (Hub):** 물리 계층, 포트 통합 관리 및 리피터 역할.
- **리피터 (Repeater):** 물리 계층, 신호 재생 및 증폭.
- **브리지 (Bridge):** 데이터 링크 계층, LAN-LAN 연결.
- **라우터 (Router):** 네트워크 계층, 경로 선택(Routing) 및 서로 다른 망 연결.
- **게이트웨이 (Gateway):** 전 계층(주로 상위), 프로토콜이 전혀 다른 네트워크 연결.
- **Tiếng Việt:**
  - L1: Hub, Repeater (Khuếch đại tín hiệu).
  - L2: cầu nối (bridge / 브리지) (Nối LAN).
  - L3: Router (Định tuyến).
  - L4-L7: Gateway (Nối mạng khác giao thức).

---

> **Mạch chuyển:** Từ **5. 네트워크 통신망 및 주소 체계 (Mạng lưới & Hệ thống Địa chỉ)**, chuyển sang **네트워크 구조 및 기술 (Network Structures & Technologies)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 네트워크 구조 및 기술 (Network Structures & Technologies)

### 1. 네트워크 설치 구조 (Network Topologies)
- **성형 (Star, 중앙 집중형)**: 중앙 컴퓨터를 중심으로 단말기가 연결 (Point-to-Point).
- **링형 (Ring, 루프형)**: 이웃하는 장치끼리 연결. 단방향 시 하나만 고장나도 전체 마비.
- **버스형 (Bus)**: 한 개의 통신 회선에 여러 장치 연결 (단말기 추가/제거 용이).
- **계층형 (Tree, 분산형)**: 중앙에서 중간 단말장치로 다시 분기되는 형태.
- **망형 (Mesh)**: 모든 지점을 연결. 통신량이 많을 때 유리하며 회선이 가장 많이 필요함 (`n(n-1)/2` 개).

### 2. 근거리 통신망 (LAN) 표준 및 기술
- **IEEE 802 규격**: 802.3(CSMA/CD), 802.4(토큰 버스), 802.5(토큰 링), 802.11(무선 LAN).
- **VLAN**: 물리적 배치와 상관없이 논리적으로 분리하는 기술.
- **CSMA/CA**: 무선 LAN(802.11)에서 매체가 비어있음을 확인 후 충돌 회피(Avoidance)를 위해 기다렸다가 전송하는 방식.

### 3. 경로 제어 (Routing) 및 흐름 제어 (Flow Control)
- **IGP (내부 게이트웨이 프로토콜)**: AS 내에서 사용. **RIP**(거리 벡터, 최대 15홉 제한)와 **OSPF**(링크 상태, 대규모 망)가 있음.
- **EGP / BGP**: AS(자율 시스템) 간의 라우팅 프로토콜.
- **흐름 제어**: **정지-대기(Stop-and-Wait)** (수신 확인 후 다음 패킷 전송) / **슬라이딩 윈도우(Sliding Window)** (수신 확인 없이 윈도우 크기만큼 연속 전송).

💡 **Mẹo ghi nhớ (Mnemonics):**
- **RIP**: 15 Hops max (Dùng cho mạng nhỏ).
- **OSPF**: Link trạng thái (state / 상태) (Dùng cho mạng lớn).
- **CSMA/CD**: Mạng LAN có dây (Collision Detection).
- **CSMA/CA**: Mạng không dây (Collision Avoidance).

---

> **Mạch chuyển:** Từ **네트워크 구조 및 기술 (Network Structures & Technologies)**, chuyển sang **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 네트워크 및 정보 침해 공격 (Network & Info Security Attacks)

### 1. 네트워크 공격
- **DDoS (분산 서비스 거부 공격)**: 여러 대의 PC(Agent/Zombie)를 이용해 특정 서버에 대량의 트래픽을 보내 마비시킴. (툴: Trin00, TFN, TFN2K, Stacheldraht).
- **스머핑 (SMURFING)**: IP/ICMP 특성을 악용해 한 사이트에 엄청난 데이터를 집중시키는 공격.
- **세션 하이재킹 (Session Hijacking)**: 클라이언트 세션을 가로채어 정상적인 사용자인 척하는 공격.
- **스위치 재밍 (Switch Jamming)**: 위조된 MAC 주소를 대량으로 보내 스위치를 더미 허브처럼 작동하게 만듦.

### 2. 블루투스 공격
- **블루버그 (BlueBug)**: 원격 조종 및 통화 감청.
- **블루스나프 (BlueSnarf)**: 장비 파일에 접근해 정보 탈취.
- **블루재킹 (BlueJacking)**: 스팸 메시지를 익명으로 퍼뜨림.

### 3. 시스템 및 소프트웨어 공격
- **제로 데이 공격 (Zero Day Attack)**: 보안 취약점이 공표되기 전, 혹은 패치가 나오기 전에 신속하게 이루어지는 공격.
- **랜섬웨어 (Ransomware)**: 파일을 암호화하고 돈(Ransom)을 요구하는 악성 프로그램.
- **백도어 (Back Door)**: 관리자 편의를 위해 만들어 놓은 비밀 통로를 악용.

💡 **Mẹo ghi nhớ (Mnemonics):**
- **BlueSnarf**: Sniff (Đánh hơi/Trộm thông tin).
- **BlueBug**: Bug (Cài bọ/Nghe lén).
- **BlueJacking**: Hijack (Chặn tin/Gửi tin nhắn rác).

---

> **Mạch chuyển:** Từ **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)**, chuyển sang **네트워크 보안 기술 (Network Security Tech)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 네트워크 보안 기술 (Network Security Tech)
- **VPN (가상 사설 통신망)**: 공중 네트워크를 전용 회선처럼 사용할 수 있게 해주는 암호화 보안 솔루션.
- **SSH (시큐어 셸)**: 원격 로그인, 파일 복사 등을 안전하게 수행하는 프로토콜 (포트 22번 사용, 데이터 암호화 지원).

---

> **Mạch chuyển:** Từ **네트워크 보안 기술 (Network Security Tech)**, chuyển sang **6. 통신 프로토콜 (Giao thức Truyền thông)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 6. 통신 프로토콜 (Giao thức Truyền thông)

### 6.1 통신 프로토콜 3요소 (Protocol 3 Elements)
- **구문 (Syntax):** 데이터 형식, 코딩.
- **의미 (Semantics):** 제어 정보 및 오류 관리.
- **시간 (Timing):** 속도 조절, 동기화.
- **Tiếng Việt:** 3 yếu tố của giao thức: cú pháp (syntax / 문법), ngữ nghĩa (semantics / 의미론), Thời gian (Timing).

### 6.2 OSI 7계층 (OSI 7 Layers)
1. **물리 계층 (Physical):** 기계/전기적 특성 (RS-232C, 리피터).
2. **데이터 링크 계층 (Data Link):** 인접 시스템 간 신뢰성 보장, 오류/흐름 제어 (HDLC, LLC).
3. **네트워크 계층 (Network):** 경로 설정(Routing), 데이터 교환 (IP, X.25, 라우터).
4. **전송 계층 (Transport):** 종단 간(End-to-End) 투명한 데이터 전송 (TCP, UDP).
5. **세션 계층 (Session):** 대화 제어 및 동기점(체크점) 관리.
6. **표현 계층 (Presentation):** 데이터 포맷 변환, 암호화, 압축.
7. **응용 계층 (Application):** 사용자에게 네트워크 서비스 제공.
- **Tiếng Việt:** Mô hình OSI 7 lớp: Vật lý -> Liên kết dữ liệu -> Mạng -> Giao vận -> Phiên -> Trình diễn -> Ứng dụng.
- 💡 **Mẹo ghi nhớ:** Vật Liên Mạng Giao Phiên Trình Ứng (Vật lý -> Liên kết dữ liệu -> Mạng -> Giao vận -> Phiên -> Trình diễn -> Ứng dụng).

### 6.3 주요 네트워크 프로토콜
- **X.25:** 패킷 교환망 프로토콜 (물리 - 프레임 - 패킷 계층). LAPB 사용.
- **TCP/IP:**
  - **응용 계층:** FTP, SMTP, HTTP, DNS 등.
  - **전송 계층:**
    - **TCP:** 연결형, 신뢰성 보장, 순서/흐름 제어, 스트림 전송.
    - **UDP:** 비연결형, 빠른 전송.
  - **인터넷 계층:**
    - **IP:** 비연결형(데이터그램), 경로 선택(Routing).
    - **ICMP:** IP 오류 처리 및 제어 메시지.
    - **ARP:** IP → MAC / **RARP:** MAC → IP.
  - **네트워크 액세스 계층:** 이더넷, X.25, RS-232C.
- **Tiếng Việt:**
  - TCP: Tin cậy, hướng kết nối. UDP: Nhanh, không kết nối.
  - IP: Định tuyến. ICMP: Báo lỗi mạng. ARP: Đổi IP sang MAC.

---

> **Mạch chuyển:** Từ **6. 통신 프로토콜 (Giao thức Truyền thông)**, chuyển sang **기본 프로토콜 (Basic Protocols)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 기본 프로토콜 (Basic Protocols)
* **ARP**: 호스트의 IP 주소(논리 주소)를 호스트와 연결된 네트워크 접속장치의 물리적 주소(MAC Address)로 변환함.
  * *Tiếng Việt*: Chuyển đổi địa chỉ IP (địa chỉ logic) của máy chủ thành địa chỉ vật lý (MAC Address) của thiết bị kết nối mạng.
  * *Ví dụ (Example)*: 컴퓨터가 IP 192.168.1.5의 MAC 주소를 찾을 때 ARP를 사용합니다. (Máy tính sử dụng ARP để tìm địa chỉ MAC của IP 192.168.1.5)
  * 💡 *Mnemonic*: **A**ddress **R**esolution (IP -> MAC)
* **RARP**: 물리적 주소를 IP 주소(논리 주소)로 변환함.
  * *Tiếng Việt*: Chuyển đổi địa chỉ vật lý thành địa chỉ IP (địa chỉ logic).
  * 💡 *Mnemonic*: **R**everse ARP (MAC -> IP)
* **RTCP**: 실시간 전송 프로토콜(RTP)이 안정되게 기능을 유지하도록 데이터 전송을 모니터링하고 최소한의 제어와 인증 기능을 제공함.
  * *Tiếng Việt*: Giám sát truyền dữ liệu và cung cấp chức năng điều khiển, xác thực tối thiểu để duy trì ổn định RTP.
* **WAP**: 이동 단말이나 PDA 등 소형 무선 단말기에서 인터넷을 이용할 수 있도록 해주는 프로토콜.
  * *Tiếng Việt*: Giao thức cho phép sử dụng internet trên các thiết bị không dây nhỏ như điện thoại di động, PDA.
* **PPP**: 주로 두 개의 라우터를 접속할 때 사용되며, 오류 검출 기능만 제공됨.
  * *Tiếng Việt*: Chủ yếu dùng để kết nối 2 router, chỉ cung cấp chức năng phát hiện lỗi (không phục hồi/điều khiển luồng).
* **UDP (User Datagram Protocol)**: 데이터 전송 전에는 연결을 설정하지 않는 비연결형 서비스. 오버헤드가 적고 실시간 전송에 유리.
  * *Tiếng Việt*: Dịch vụ không kết nối (không thiết lập kết nối trước khi truyền). Ít overhead, thuận lợi cho truyền thời gian thực (tốc độ quan trọng hơn độ tin cậy).
  * *Ví dụ*: 실시간 스트리밍(Video streaming)에 주로 사용됩니다. (Thường dùng cho phát video trực tiếp).

---

---

> **Mạch chuyển:** Từ **기본 프로토콜 (Basic Protocols)**, chuyển sang **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)

### 7.1 회복 및 동시성 제어 (Recovery & Concurrency)
- **회복 (Recovery):** 장애 발생 시 손상 이전의 정상 상태로 복구.
- **즉각 갱신 기법 (Immediate Update):** 트랜잭션 부분 완료 전이라도 즉시 DB에 반영. 갱신 내용은 **Log에 보관**하여 회복에 대비.
- **로킹 단위 (Locking Granularity):** 병행제어에서 한꺼번에 로킹하는 객체 크기.
  - **단위가 크면:** 로크 수가 작아 관리하기 쉽지만 병행성 저하.
  - **단위가 작으면:** 로크 수가 많아 관리 복잡/오버헤드 증가, 하지만 병행성 상승.
- **타임 스탬프 순서 (Time Stamp Ordering):** 직렬성 순서를 결정하기 위해 트랜잭션 처리 순서를 미리 선택.
- **Tiếng Việt:**
  - Immediate cập nhật (update / 업데이트): Cập nhật ngay lập tức (dùng Log để phục hồi).
  - Locking Granularity: Kích thước khóa. Khóa lớn -> dễ quản lý, đồng thời thấp. Khóa nhỏ -> khó quản lý, đồng thời cao.

### 7.2 교착상태 (Deadlock)
- **발생 4가지 조건:** 상호 배제(Mutual Exclusion), 점유와 대기(Hold and Wait), 비선점(Non-preemption), 환형 대기(Circular Wait).
- **회피 기법 (Avoidance):** 교착상태 가능성을 피해 나가는 방법. 주로 **은행원 알고리즘 (Banker's Algorithm, E. J. Dijkstra)** 사용.
- **Tiếng Việt:** 4 điều kiện Deadlock: Loại trừ lẫn nhau, Giữ & Chờ, Không trưng dụng, Chờ vòng tròn. Tránh Deadlock dùng Thuật toán Nhà băng.
- 💡 **Mẹo ghi nhớ:** Điều kiện Deadlock: Độc Giữ Không Vòng (Độc quyền, Giữ và chờ, Không ưu tiên, Vòng tròn).

---

> **Mạch chuyển:** Từ **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)**, chuyển sang **데이터베이스 신기술 (DB New Technologies)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 데이터베이스 신기술 (DB New Technologies)

### 1. 빅데이터 및 분석 기술
- **하둡 (Hadoop)**: 대용량 데이터를 병렬로 처리하기 위한 자바 소프트웨어 프레임워크 (오픈소스).
- **맵리듀스 (MapReduce)**: 하둡 기반 분산 처리 프로그래밍 모델 (Map으로 분류, Reduce로 추출).
- **데이터 마이닝 (Data Mining)**: 대량의 데이터에서 패턴을 규명하여 유용한 정보를 추출하는 기법.
- **OLAP**: 다차원 데이터로부터 통계적 요약 정보를 분석하여 의사결정에 활용. (연산: Roll-up, Drill-down, Pivoting 등).

---

> **Mạch chuyển:** Từ **데이터베이스 신기술 (DB New Technologies)**, chuyển sang **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)

### 8.1 보안 기본 요소 및 프레임워크
- **보안 3대 요소 (CIA Triad):**
  - **기밀성 (Confidentiality):** 인가된 사용자에게만 접근 허용.
  - **무결성 (Integrity):** 인가된 사용자만 수정 가능.
  - **가용성 (Availability):** 인가받은 사용자는 언제라도 사용 가능.
- **Seven Touchpoints:** 소프트웨어 보안 모범사례를 SDLC(소프트웨어 생명주기)에 통합.
- **OWASP:** 웹 보안 취약점을 연구하는 비영리 단체.
- **관리적/물리적/기술적 보안:**
  - 관리적 (정책, 교육), 물리적 (출입 통제, 재해 복구), 기술적 (사용자 인증, 접근 제어).
- **Tiếng Việt:** 3 yếu tố bảo mật CIA: Tính bảo mật, Tính toàn vẹn, Tính sẵn sàng.

### 8.2 시스템 보안 기술
- **TCP 래퍼 (TCP Wrapper):** 외부 접속 인가 여부를 점검하여 허용/거부하는 도구.
- **Secure OS:** 보안 기능을 갖춘 커널을 이식하여 시스템 자원 보호.
- **침입 탐지 시스템 (IDS):** 실시간으로 비정상적 사용 탐지 (오용 탐지: 패턴 기반, 이상 탐지: 평균 상태 기준).
- **고가용성 솔루션 (HACMP):** 장애 발생 시 즉시 다른 시스템으로 대체 가능하게 하는 환경.
- **인증 (Authentication):** 지식 기반(패스워드), 소유 기반(스마트카드), 행위 기반(서명).
- **커널 로그:**
  - `wtmp`: 성공한 로그인/로그아웃.
  - `utmp`: 현재 로그인 상태.
  - `btmp`: 실패한 로그인.
  - `lastlog`: 마지막 성공 로그인.
- **Tiếng Việt:** Secure OS, IDS (phát hiện xâm nhập), HACMP (giải pháp độ sẵn sàng cao). Phân loại log kernel (wtmp, utmp, v.v.).

---

> **Mạch chuyển:** Từ **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)**, chuyển sang **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)

### 10.1 웹 및 애플리케이션 취약점
- **SQL 삽입 (SQL Injection):** SQL을 삽입하여 DB 유출/변조 및 인증 우회.
- **크로스사이트 스크립팅 (XSS):** 악의적인 스크립트를 삽입하여 방문자 정보 탈취.
- **경로 조작 및 자원 삽입:** 데이터 입출력 경로 조작으로 자원 삭제/수정.
- **메모리 버퍼 오버플로:** 메모리 범위를 넘어선 위치에서 쓰기 시도. 방어 기술로 **스택 가드(Stack Guard)** 사용.
- **하드코드된 비밀번호:** 소스코드 내부에 비밀번호를 직접 입력하는 취약점.
- **Tiếng Việt:** Các lỗ hổng web: SQL Injection (chèn lệnh SQL), XSS (chèn script độc hại), Buffer Overflow (tràn bộ đệm - phòng bằng Stack Guard).

### 10.2 네트워크 및 분산 서비스 거부 공격 (DoS/DDoS)
- **세션 하이재킹 (Session Hijacking):** 클라이언트의 세션 정보를 가로채는 공격.
- **DDoS 공격:** 여러 분산된 지점에서 한 곳을 공격. (툴: Trin00, TFN, TFN2K, Stacheldraht).
- **Ping of Death:** 허용 범위 이상의 큰 ICMP 패킷을 전송해 마비시킴.
- **Ping Flood:** 많은 ICMP 메시지를 보내 응답으로 자원 고갈시킴.
- **스머핑 (SMURFING):** IP/ICMP 특성을 악용해 한 사이트에 집중적으로 데이터 보냄.
- **DPI (Deep Packet Inspection):** 전 계층의 프로토콜과 패킷 내부를 파악해 침입 탐지.
- **Tiếng Việt:**
  - DDoS: Tấn công từ chối dịch vụ phân tán.
  - Ping of Death: Gửi gói ICMP quá lớn.
  - SMURFING: Gửi lượng lớn dữ liệu tập trung.

### 10.3 시스템 해킹 및 악성코드
- **백도어 (Back Door):** 보안을 제거하고 만들어 놓은 비밀 통로 (탐지: 무결성 검사, 열린 포트 등).
- **키로거 공격 (Key Logger):** 키보드 움직임을 탐지해 개인정보 탈취.
- **랜섬웨어 (Ransomware):** 문서 암호화 후 돈(Ransom)을 요구.
- **웜 (Worm):** 네트워크를 통해 스스로 전파·복제되는 악성 코드로, 숙주 파일에 기생해야 하는 바이러스와 구분한다.
- **허니팟 (Honeypot):** 비정상 접근 탐지를 위해 의도적으로 설치한 시스템 (미끼).
- **피싱 (Phishing):** 공공/금융 기관을 사칭해 개인정보 탈취.
- **Tiếng Việt:** Backdoor (Cửa hậu), Key Logger (Ghi thao tác bàn phím), Ransomware (Mã độc tống tiền), Worm (Giun máy tính - tự nhân bản), Honeypot (Hệ thống mồi nhử).

### 10.4 기타 네트워크 공격
- **스위치 재밍 (Switch Jamming):** 위조된 MAC 주소를 흘려보내 스위치를 더미 허브로 작동하게 만듦.
- **블루투스 관련 공격:**
  - **블루버그 (BlueBug):** 취약한 연결 관리 악용.
  - **블루스나프 (BlueSnarf):** 취약점 활용해 파일 접근.
  - **블루프린팅 (BluePrinting):** 공격 대상 장비 검색.
  - **블루재킹 (BlueJacking):** 익명으로 스팸 메시지 퍼뜨림.
- **Tiếng Việt:** Tấn công Switch Jamming (biến Switch thành Hub) và các tấn công Bluetooth (BlueBug, BlueSnarf, BlueJacking).
- 💡 **Mẹo ghi nhớ:** Blue**Jacking** = **Spam message**. Blue**Snarf** = **Snatch files** (cướp file).

---

> **Mạch chuyển:** Từ **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)**, chuyển sang **정보 보안 및 하드웨어 신기술 (Security & HW Tech)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 정보 보안 및 하드웨어 신기술 (Security & HW Tech)

### 1. 보안 용어 및 Secure OS
- **BaaS (Blockchain as a Service)**: 클라우드 기반 블록체인 개발 환경 제공.
- **OWASP**: 웹 취약점을 연구하는 비영리 단체 (10대 취약점 발표).
- **허니팟 (Honeypot)**: 침입자를 속여 정보를 수집하기 위해 설치해 둔 시스템 (미끼).
- **Secure OS**: 기존 OS에 보안 기능 커널을 이식한 운영체제. 암호적, 논리적, 시간적, 물리적 분리 방법을 통해 보호하며 식별, 인증, 접근통제(MAC, DAC) 기능을 제공합니다.

### 2. 하드웨어 신기술
- **HA (High Availability, 고가용성)**: 장애 발생 시 즉시 다른 시스템으로 대체 가능한 이중화 환경.
- **RAID**: 여러 개의 하드디스크에 데이터를 분산 저장하여 속도와 안정성을 향상시키는 기술.
- **트러스트존 (TrustZone)**: 프로세서 내에 일반 구역과 보안 구역을 분할하는 ARM의 하드웨어 보안 기술.

---

> **Mạch chuyển:** Từ **정보 보안 및 하드웨어 신기술 (Security & HW Tech)**, chuyển sang **소프트웨어 보안 (Software Security)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 소프트웨어 보안 (Software Security)

### 1. 보안 3대 요소 (CIA Triad)
- **기밀성 (Confidentiality)**: 인가된 사용자만 접근 가능 (암호화).
- **무결성 (Integrity)**: 인가된 사용자만 수정 가능 (변조 방지).
- **가용성 (Availability)**: 인가된 사용자는 언제든 사용 가능.
- 기타: 인증(Authentication), 부인 방지(Non-Repudiation).

### 2. Secure SDLC
보안상 안전한 SW 개발을 위해 SDLC(생명주기)에 보안 활동을 추가한 것.
- **방법론**: CLASP(초기 단계 중심), SDL(MS사 개발), Seven Touchpoints(각 단계별 모범사례 적용).

### 3. 주요 보안 약점 및 방어
- **SQL 삽입 (SQL Injection)**: 입력 폼에 SQL 명령어를 넣어 DB를 조작. (방어: 입력값 필터링 및 매개변수화).
- **XSS (크로스사이트 스크립팅)**: 웹페이지에 악성 스크립트를 삽입해 사용자 정보 탈취. (방어: `<, >, &` 등 특수문자 치환).
- **메모리 버퍼 오버플로**: 할당된 메모리 범위를 넘어서 기록하여 오동작 유발.
  - **스택 가드 (Stack Guard)**: 복귀 주소와 변수 사이에 특정 값을 넣어 오버플로를 탐지하는 기술.
- **접근 지정자 (Access Modifier)**: `Public`(모두 접근), `Protected`(패키지+상속), `Default`(같은 패키지), `Private`(클래스 내부만).

💡 **Mẹo ghi nhớ (Mnemonics):**
- 보안 3요소: **C.I.A** (Confidentiality - Integrity - Availability).
- 접근 한정자: **P.P.D.P** (Public - Protected - Default - Private).

---

> **Mạch chuyển:** Từ **소프트웨어 보안 (Software Security)**, chuyển sang **인증 및 보안 체계 (Authentication & Security System)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 인증 및 보안 체계 (Authentication & Security System)

### 1. 인증 수단 4가지
- **지식 기반 (Something You Know)**: 패스워드, PIN (머릿속 기억).
- **소유 기반 (Something You Have)**: 신분증, 스마트카드, OTP.
- **생체 기반 (Something You Are)**: 지문, 홍채, 정맥 인식.
- **위치 기반 (Somewhere You Are)**: 접속 IP 위치, GPS.

### 2. 보안 체계 3영역
- **관리적 보안**: 정보보호 정책, 조직, 교육 등 사람 중심.
- **물리적 보안**: 출입 통제, 전산실 관리 등 물리적 보호.
- **기술적 보안**: 사용자 인증, 암호화, 접근 제어 등 IT 기술 보호.

---

> **Mạch chuyển:** Từ **인증 및 보안 체계 (Authentication & Security System)**, chuyển sang **소프트웨어 개발 보안 관련 법규** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 소프트웨어 개발 보안 관련 법규
- **개인정보 보호법**: 개인정보 처리 및 보호에 관한 전반적 사항.
- **정보통신망법**: 정보통신망을 통한 개인정보 수집/이용 보호.
- **신용정보법**: 개인의 신용정보 취급 보호.
- **위치정보법**: 개인 위치정보 수집 및 제공 보호.

---

> **Mạch chuyển:** Từ **소프트웨어 개발 보안 관련 법규**, chuyển sang **⦁ 보안 취약점 및 보안 기능 (Lỗ hổng bảo mật & Chức năng bảo mật)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## ⦁ 보안 취약점 및 보안 기능 (Lỗ hổng bảo mật & Chức năng bảo mật)

---

> **Mạch chuyển:** Từ **⦁ 보안 취약점 및 보안 기능 (Lỗ hổng bảo mật & Chức năng bảo mật)**, chuyển sang **4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)
- **적절한 인증 없이 중요기능 허용 (Missing Authentication)**: 중대한 기능에 재인증이 없음. (Không yêu cầu xác thực lại khi làm việc quan trọng).
- **중요정보 평문 저장 및 전송 (Plaintext Storage/Transmission)**: 패스워드를 암호화 없이 저장/전송. (Lưu hoặc truyền mật khẩu không mã hóa).
- **하드코드된 비밀번호 (Hardcoded Password)**: 소스코드에 비밀번호를 직접 작성. (Ghi cứng mật khẩu trong source code).
- **오류 메시지 통한 정보 노출 (Information Exposure Through Error Message)**: 시스템 내부 구조나 파일 경로가 오류 메시지에 포함되어 노출됨. (Thông báo lỗi làm lộ đường dẫn nội mục hệ thống).
- **예시 (Example)**:
  - (KR) DB 연결 실패 시 "gốc (root / 루트) 계정 연결 실패" 같은 메시지를 띄우지 않고 "일시적인 오류입니다"로 대체.
  - (VN) Thay vì hiện lỗi "Không kết nối được tài khoản gốc (root / 루트)", chỉ hiển thị "Lỗi hệ thống tạm thời".

---

---

> **Mạch chuyển:** Từ **4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)**, chuyển sang **9. 암호화 기술 (Công nghệ Mã hóa)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 9. 암호화 기술 (Công nghệ Mã hóa)

### 9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)
- **개인키(대칭키) 암호화 (Private/Symmetric Key):**
  - **동일한 키**로 암호화/복호화. 속도가 빠름. 암호화 키 개수: n(n-1)/2.
  - 종류:
    - **블록 암호화:** DES, SEED, AES, ARIA, IDEA
    - **스트림 암호화:** LFSR, RC4
- **공개키(비대칭키) 암호화 (Public/Asymmetric Key):**
  - 암호화(공개키), 복호화(비밀키/개인키). 키 개수: **2n**.
  - 대표 알고리즘: **RSA** (소인수분해 기반).
- **Tiếng Việt:**
  - Khóa cá nhân (Đối xứng): Cùng 1 khóa, nhanh. (DES, AES, ARIA).
  - Khóa công khai (Bất đối xứng): 2 khóa (Public để mã hóa, Private để giải mã), an toàn nhưng chậm. (RSA).

### 9.2 해시 및 기타 암호화 요소
- **해시 (Hash):** 임의의 길이를 고정된 길이로 변환. 복호화가 불가한 **일방향 함수**. (종류: SHA, MD4, MD5 등).
- **솔트 (Salt):** 암호화 전 원문에 무작위 값을 덧붙이는 과정. (패스워드 보안 강화용).
- **Tiếng Việt:** băm (hash / 해시) là hàm một chiều không thể giải mã (SHA, MD5). Salt là thêm chuỗi ngẫu nhiên trước khi mã hóa để chống tấn công từ điển.

---

> **Mạch chuyển:** Từ **9. 암호화 기술 (Công nghệ Mã hóa)**, chuyển sang **암호화 기법 (Encryption Techniques)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 암호화 기법 (Encryption Techniques)

### 1. 개인키 (대칭키) 암호화 (Private Key / Symmetric Key)
- 암호화와 복호화에 **동일한 키(비밀키)**를 사용합니다.
- 장점: 속도가 빠름 / 단점: 키 분배가 어렵고 키 개수가 많아짐.
- 필요한 키의 개수: `n(n-1) / 2`
- **종류**: DES, 3DES, AES, SEED(국내), ARIA(국내).

### 2. 공개키 (비대칭키) 암호화 (Public Key / Asymmetric Key)
- 암호화할 때는 공개키(Public Key), 복호화할 때는 비밀키(Private Key)를 사용합니다.
- 장점: 키 분배 용이, 키 개수 적음 / 단점: 암복호화 속도가 느림.
- 필요한 키의 개수: `2n`
- **종류**: RSA.

### 3. 해시(Hash)와 솔트(Salt)
- **해시 (Hash)**: 임의의 길이 데이터를 고정된 길이의 값으로 변환하는 일방향 함수다. 무결성 검증에 사용하며, 패스워드는 전용 password hashing/KDF와 salt를 사용해야 한다. 해시는 암호화처럼 복호화하지 않는다 (예: SHA-256, MD5).
- **솔트 (Salt)**: 암호화 전 원문에 덧붙이는 무작위 값. 동일한 패스워드라도 솔트가 다르면 해시값이 달라져 레인보우 테이블 공격을 방어합니다.

> **Vietnamese Explanation**:
> **Mã hóa đối xứng (Private Key)**: Dùng chung 1 chìa khóa để khóa và mở (nhanh nhưng khó chia sẻ chìa khóa an toàn).
> **Mã hóa bất đối xứng (Public Key)**: Dùng khóa công khai để khóa, khóa bí mật để mở (chậm hơn nhưng an toàn).
> **băm (hash / 해시)** là mã hóa 1 chiều (không dịch ngược được). **Salt (Muối)** là thêm chuỗi ngẫu nhiên vào mật khẩu trước khi băm để tăng độ khó.

---

> **Mạch chuyển:** Từ **암호화 기법 (Encryption Techniques)**, chuyển sang **1. 암호화 기본 개념 (Concepts)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 1. 암호화 기본 개념 (Concepts)
- **평문 (Plain)**: Bản rõ (chưa mã hoá)
- **암호문 (Cipher)**: Bản mã (đã mã hoá)
- **치환 암호 (Substitution Cipher)**: 문자를 다른 문자로 대체 (Mã hoá thay thế, vd: A -> C).
- **전치 암호 (Transposition Cipher)**: 문자의 위치를 바꿈 (Mã hoá hoán vị, vd: ABC -> BCA).

---

> **Mạch chuyển:** Từ **1. 암호화 기본 개념 (Concepts)**, chuyển sang **2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)

### 2.1 소프트웨어 재사용 (Software Reuse)
- **이점 (Benefits):** 개발 시간과 비용 단축, 품질 향상, 생산성 향상, 시스템 명세/설계/코드 등 문서 공유.
- **방법 (Methods):**
  - **합성 중심 (Composition-based):** 전자 칩 같은 소프트웨어 부품(모듈)을 만들어 끼워 맞추는 방법.
  - **생성 중심 (Generation-based):** 추상화 형태로 쓰여진 명세를 구체화하여 프로그램을 만드는 방법.
- **Tiếng Việt:** Tái sử dụng phần mềm giúp giảm thời gian/chi phí, tăng chất lượng.
  - Tổng hợp: lắp ráp các mô-đun (module / 모듈) (như chip).
  - Khởi tạo: tạo chương trình từ đặc tả trừu tượng.
- **Example:**
  - *KR:* 이전에 만든 로그인 모듈을 새 프로젝트에 그대로 재사용.
  - *VN:* Tái sử dụng nguyên bản mô-đun (module / 모듈) đăng nhập đã làm trước đó cho dự án mới.

### 2.2 소프트웨어 재공학 (Software Reengineering)
- 기존 소프트웨어의 데이터와 기능을 변경 및 개선하여 유지보수성과 품질을 높이는 기법.
- **이점 (Benefits):** 위험 부담 감소, 개발 시간/비용 단축, 시스템 명세 오류 억제.
- **주요 활동 (Activities):**
  - **분석 (Analysis):** 명세서 확인 및 재공학 대상 선정.
  - **재구성 (Restructuring):** 코드 재구성하여 구조 향상.
  - **역공학 (Reverse Engineering):** 기존 소프트웨어를 분석하여 설계 정보를 재발견하는 활동.
  - **이식 (Migration):** 다른 운영체제나 하드웨어 환경으로 변환.
- **Tiếng Việt:** Tái thiết kế phần mềm cũ để dễ bảo trì. Các hoạt động chính: Phân tích, Tái cấu trúc, Dịch ngược (Reverse Engineering), và di chuyển (migration / 마이그레이션).
- 💡 **Mẹo ghi nhớ:** Các bước Reengineering: "Phân Tích -> Tái Cấu Trúc -> Dịch Ngược -> Di Chuyển".

### 2.3 trường hợp (case / 사례) (Computer Aided Software Engineering)
- 소프트웨어 개발 과정 전체 또는 일부를 자동화하는 전용 도구.
- **원천 기술 (Core Technologies):** 구조적 기법, 프로토타이핑, 자동 프로그래밍, 정보 저장소, 분산처리.
- **주요 기능 (Major Functions):** 생명 주기 전 단계 연결, 다양한 모델 지원, 그래픽 지원, 자료 흐름도 작성, 모순 검사 등.
- **Tiếng Việt:** Công cụ tự động hóa toàn bộ hoặc một phần quá trình phát triển phần mềm. Hỗ trợ đồ họa, vẽ sơ đồ, kiểm tra lỗi.
- **Example:**
  - *KR:* UML 설계 도구를 사용하여 코드를 자동 생성.
  - *VN:* Sử dụng công cụ thiết kế UML để tự động sinh mã (code / 코드).

---

> **Mạch chuyển:** Từ **2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)**, chuyển sang **6. IT 신기술 및 소프트웨어 (Công nghệ IT mới & Phần mềm)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 6. IT 신기술 및 소프트웨어 (Công nghệ IT mới & Phần mềm)

### 6.1 최신 IT 기술 동향
- **도커 (Docker):** 컨테이너 기술을 자동화하여 쉽게 사용할 수 있게 하는 오픈소스 프로젝트.
- **매시업 (Mashup):** 웹에서 제공하는 정보/서비스를 융합하여 새로운 서비스를 만드는 기술.
- **디지털 트윈 (Digital Twin):** 현실 속 사물을 소프트웨어로 가상화한 모델.
- **서비스형 블록체인 (BaaS):** 블록체인 앱 개발 환경을 클라우드 기반으로 제공.
- **스크래피 (Scrapy):** Python 기반의 대규모 웹 크롤링 프레임워크.
- **텐서플로 (TensorFlow):** 구글의 기계학습/데이터 흐름 프로그래밍용 오픈소스 라이브러리.
- **앤 스크린 (N-Screen):** 여러(N개) 단말기에서 동일한 콘텐츠를 자유롭게 이용.
- **Tiếng Việt:**
  - Docker: Nền tảng bộ chứa (container / 컨테이너) hóa mã nguồn mở.
  - Mashup: Kết hợp các API/dịch vụ web để tạo dịch vụ mới.
  - Digital Twin: Bản sao kỹ thuật số của thế giới thực.
  - N-Screen: Xem một nội dung trên nhiều thiết bị.

### 6.2 데이터 분석 및 분산 처리
- **하둡 (Hadoop):** 오픈소스 기반 분산 컴퓨팅 플랫폼. 대용량 데이터 전송에 **스쿱(Sqoop)** 사용.
- **맵리듀스 (MapReduce):** 대용량 데이터를 분산 처리하기 위한 프로그래밍 모델.
- **데이터 마이닝 (Data Mining):** 대량의 데이터에서 유용한 정보를 발견하는 기법.
- **OLAP (Online Analytical Processing):** 다차원 데이터에서 통계적 요약 정보를 분석하여 의사결정에 활용. (연산: Roll-up, Drill-down, Pivoting, Slicing, Dicing 등).
- **Tiếng Việt:**
  - Hadoop: Nền tảng điện toán phân tán (dùng Sqoop kết nối RDB).
  - MapReduce: Mô hình lập trình xử lý phân tán.
  - dữ liệu (data / 데이터) Mining: Khai phá dữ liệu.
  - OLAP: Xử lý phân tích đa chiều trực tuyến.

### 6.3 시스템 아키텍처 및 프로그래밍 요소
- **SOA (Service Oriented Architecture) 기반 계층:** 표현(Presentation) → 업무 프로세스 → 서비스 중간 → 애플리케이션 → 데이터 저장.
- **접근 지정자 (Access Modifiers):** 외부로부터의 접근을 제한 (Public, Protected, Default, Private).
- **Tiếng Việt:** Kiến trúc hướng dịch vụ (SOA) và các chỉ định truy cập trong lập trình hướng đối tượng (OOP).

---

> **Mạch chuyển:** Từ **6. IT 신기술 및 소프트웨어 (Công nghệ IT mới & Phần mềm)**, chuyển sang **11. 보충 및 심화 내용 (Bổ sung & Nâng cao)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 11. 보충 및 심화 내용 (Bổ sung & Nâng cao)

### 11.1 소프트웨어 프레임워크 및 개발 심화
- **프레임워크의 특성 (Framework Characteristics):**
  - **모듈화 (Modularity):** 캡슐화를 통해 변경의 영향을 최소화하고 품질 향상.
  - **재사용성 (Reusability):** 재사용 가능한 모듈 제공 (생산성 향상).
  - **확장성 (Extensibility):** 다형성을 통한 인터페이스 확장.
  - **제어의 역흐름 (Inversion of Control):** 객체 제어 권한을 프레임워크에 넘김.
- **프레임워크 종류 (Framework Types):**
  - **스프링 (Spring):** 자바 플랫폼을 위한 경량형 오픈소스 프레임워크.
  - **전자정부 (e-Government):** 공공부문 정보화 사업을 지원하는 프레임워크.
  - **닷넷 (.NET):** 마이크로소프트의 Windows 개발 및 실행 환경.
- **Tiếng Việt:** Đặc điểm của khung phần mềm (framework / 프레임워크): Mô-đun hóa, Tái sử dụng, Khả năng mở rộng, và Đảo ngược quyền điều khiển (IoC - Inversion of Control). Các loại: Spring (Java), e-Government (Hàn Quốc), .NET (Microsoft).

### 11.2 네트워크 구조 및 표준 심화
- **네트워크 토폴로지 (Network Topology):**
  - **성형 (Star):** 중앙 컴퓨터를 중심으로 연결 (포인트 투 포인트).
  - **링형 (Ring):** 이웃하는 단말끼리 원형으로 연결.
  - **버스형 (Bus):** 하나의 통신 회선에 여러 단말 연결 (신뢰성 높음).
  - **망형 (Mesh):** 모든 지점을 서로 연결. 회선 수 = `n(n-1)/2`.
- **IEEE 802 표준 규격:**
  - `802.3`: CSMA/CD (유선 LAN)
  - `802.11`: 무선 LAN (WLAN)
    - `802.11a/g`: 54Mbps
    - `802.11i`: 보안 표준 (WPA/WPA2)
    - `802.11n`: 2.4GHz/5GHz 듀얼 대역, 최고 600Mbps
- **경로 제어 프로토콜 (Routing Protocols):**
  - **IGP (내부):** AS 내부 라우팅 (RIP, OSPF)
  - **EGP (외부):** AS 간의 라우팅
  - **BGP (Border Gateway Protocol):** EGP 단점 보완. 변화된 정보만 교환.
- **흐름 제어 (Flow Control):**
  - **정지-대기 (Stop-and-Wait):** ACK를 받은 후 다음 패킷 전송.
  - **슬라이딩 윈도우 (Sliding Window):** ACK 없이도 미리 정해진 윈도우 크기(Window Size)만큼 연속 전송.
- **Tiếng Việt:**
  - Topology mạng: Star, Ring, Bus, Mesh (Số đường truyền = n(n-1)/2).
  - IEEE 802.11: Tiêu chuẩn mạng không dây (Wi-Fi).
  - luồng (flow / 흐름) điều khiển (control / 제어): Sliding cửa sổ (window / 윈도우) truyền liên tục dựa vào kích thước cửa sổ mà không cần chờ ACK cho từng gói.

### 11.3 데이터베이스 동시성 및 교착상태 심화
- **교착상태 해결 방법 (Deadlock Handling):**
  - **예방 (Prevention):** 발생 4조건(상호배제, 점유대기, 비선점, 환형대기) 중 하나를 부정 (자원 낭비 심함).
  - **회피 (Avoidance):** 가능성을 피함 (**은행원 알고리즘**).
  - **발견 (Detection):** 교착상태가 발생했는지 점검.
  - **회복 (Recovery):** 프로세스 종료 또는 자원 선점.
- **회복 기법 (Recovery):**
  - **연기 갱신 기법 (Deferred Update):** 트랜잭션 부분 완료 전까지 실제 DB 반영을 연기하고 Log에 기록 (Redo만 가능).
  - **즉각 갱신 기법 (Immediate Update):** 즉시 반영. 장애 시 Undo, Redo 모두 사용 가능.
  - **그림자 페이지 대체 기법 (Shadow Paging):** 그림자 페이지 보관 (Log, Undo, Redo 불필요).
  - **검사점 기법 (Check Point):** 검사점부터 회복하여 시간 절약.
- **Tiếng Việt:** Xử lý Deadlock: Phòng ngừa (Prevention) -> Tránh (Avoidance - Thuật toán Banker) -> Phát hiện (Detection) -> Phục hồi (Recovery). Phục hồi DB bằng Log, Shadow Paging, Check điểm (point / 지점).

### 11.4 암호화 및 해시 알고리즘 심화
- **암호화 키 개수 (Key Count):**
  - **개인키(대칭키):** `n(n-1)/2` 개
  - **공개키(비대칭키):** `2n` 개
- **블록 암호화 알고리즘 (Block Ciphers):**
  - **SEED:** 한국인터넷진흥원(KISA) 개발 (128/256bit).
  - **ARIA:** 국가정보원 및 산학연 협회 개발 (128/192/256bit).
  - **DES:** 미국 NBS 발표, 64bit 블록 / 56bit 키 (3DES로 강화됨).
  - **AES:** DES 한계 극복, NIST 발표 (128/192/256bit).
- **해시 함수 종류 (Hash Functions):**
  - **SHA 시리즈:** 미국 NSA 설계, NIST 발표.
  - **MD5:** R. Rivest 고안 (128bit 키).
  - **N-NASH, SNEFRU.**
- **Tiếng Việt:** Thuật toán mã hóa Hàn Quốc: SEED, ARIA. Thuật toán quốc tế: DES, AES, RSA. Số lượng khóa đối xứng = n(n-1)/2. Số lượng khóa bất đối xứng = 2n.

### 11.5 기타 보안 및 공격 기법 심화
- **Secure SDLC 방법론:**
  - **CLASP:** 활동 중심, 역할 기반 (초기 단계 보안 강화).
  - **MS SDL:** 마이크로소프트의 나선형 모델 기반 방법론.
  - **Seven Touchpoints:** 모범사례를 SDLC에 통합 (위험 분석 및 테스트).
- **추가 웹 보안 약점 (Additional Web Vulnerabilities):**
  - **운영체제 명령어 삽입:** 외부 입력으로 시스템 명령어 실행 유도.
  - **위험한 파일 업로드:** 스크립트 파일 업로드로 시스템 제어.
  - **신뢰되지 않는 URL 주소로 자동접속 연결 (Open Redirect):** 피싱 사이트로 유도.
- **분산 서비스 공격용 툴 (DDoS Tools):**
  - **Trin00:** UDP Flooding 주도.
  - **TFN / TFN2K:** UDP/TCP SYN, 스머핑 동시 수행.
  - **Stacheldraht:** 암호화된 통신 수행 및 자동 업데이트.
- **새로운 공격 기법 (New Attack Vectors):**
  - **제로 데이 공격 (Zero Day Attack):** 보안 취약점이 공표되기도 전에 이루어지는 신속한 공격.
  - **스미싱 (Smishing):** SMS를 이용한 개인정보 탈취.
  - **Evil Twin Attack:** 실제와 동일한 이름의 가짜 Wi-Fi(AP)를 송출해 정보 탈취.
- **Tiếng Việt:**
  - Zero Day Attack: Tấn công khai thác lỗ hổng trước khi có bản vá.
  - Smishing: Phishing qua tin nhắn SMS.
  - Evil Twin: Tấn công bằng trạm Wi-Fi giả mạo tên (SSID) giống hệt trạm thật.
  - DDoS Tools: Trin00, TFN, Stacheldraht (ẩn danh và mã hóa liên lạc).

---

> **Mạch chuyển:** Từ **11. 보충 및 심화 내용 (Bổ sung & Nâng cao)**, chuyển sang **001. 소프트웨어 생명 주기 (Software Life Cycle)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 001. 소프트웨어 생명 주기 (Software Life Cycle)
* **개념**: 소프트웨어를 개발하기 위해 정의하고 운용, 유지보수 등의 과정을 각 단계별로 나눈 것. (소프트웨어 수명 주기)
  * *Tiếng Việt*: Vòng đời phần mềm là việc chia quá trình từ định nghĩa, phát triển, vận hành đến bảo trì phần mềm thành các giai đoạn.
  * *Ví dụ*: 앱을 기획하고, 만들고, 출시 후 업데이트하는 전체 과정. (Toàn bộ quá trình từ lên kế hoạch, tạo, đến cập nhật app sau khi ra mắt).

---

---

> **Mạch chuyển:** Từ **001. 소프트웨어 생명 주기 (Software Life Cycle)**, chuyển sang **5과목 정보시스템 구축 관리 (Information System Construction Management)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 5과목 정보시스템 구축 관리 (Information System Construction Management)

### 소프트웨어 개발 방법론 (Software Development Methodologies)
- **구조적 방법론 (Structured)**: 처리(Process) 중심. 분할과 정복(Divide and Conquer) 원리 적용.
- **정보공학 방법론 (Information Engineering)**: 자료(Data) 중심. 대규모 정보 시스템 구축에 적합.
- **컴포넌트 기반 방법론 (CBD)**: 기존 컴포넌트를 조합하여 새로운 애플리케이션 생성. 재사용성(Reusability)과 확장성이 높고 유지보수 비용 최소화.

### 소프트웨어 재사용과 재공학 (Software Reuse & Reengineering)
- **소프트웨어 재사용 (Reuse)**: 이미 검증된 소프트웨어를 새로운 개발에 사용하여 개발 시간 및 비용 단축, 품질 향상.
- **소프트웨어 재공학 (Reengineering)**: 기존 시스템의 분석·재구성·역공학·이식 등을 통해 유지보수성과 수명을 개선하는 활동이다. 신규 기능 추가 자체와 동일한 개념은 아니다.

> **Vietnamese Explanation**:
> - **Methodologies**: Structured (Tập trung vào quá trình), thông tin (information / 정보) kỹ thuật (engineering / 엔지니어링) (Tập trung vào dữ liệu), CBD (Lắp ráp từ các linh kiện có sẵn).
> - **Reuse**: Dùng lại mã (code / 코드)/mô-đun (module / 모듈) cũ cho dự án mới để tiết kiệm chi phí.
> - **Reengineering**: Tái cấu trúc, cải tiến hệ thống cũ để dễ bảo trì và đáp ứng nhu cầu mới.

---

> **Mạch chuyển:** Từ **5과목 정보시스템 구축 관리 (Information System Construction Management)**, chuyển sang **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)

### 1. 재사용 방법 (Reuse Methods)
- **합성 중심 (Composition-Based)**: 소프트웨어 부품(블록)을 만들어 끼워 맞추어 완성시키는 방법. (블록 구성 방법)
- **생성 중심 (Generation-Based)**: 추상화 형태의 명세를 구체화하여 프로그램을 만드는 방법. (패턴 구성 방법)

### 2. 재공학 주요 활동 (Reengineering Activities)
기존 시스템을 개선하고 유지보수성을 높이는 활동입니다.
- **분석 (Analysis)**: 기존 명세서를 확인해 동작을 이해하고 대상을 선정.
- **재구성 (Restructuring)**: 외적인 동작은 유지하면서 코드 구조를 향상.
- **역공학 (Reverse Engineering)**: 기존 코드를 분석해 설계 정보나 구성 요소를 다시 추출(도출)해 내는 활동.
- **이식 (Migration)**: 다른 운영체제나 하드웨어 환경에서 사용할 수 있도록 변환.

---

> **Mạch chuyển:** Từ **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)**, chuyển sang **trường hợp (case / 사례) (Computer Aided Software Engineering)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## Trường hợp (case / 사례) (Computer Aided Software Engineering)
- 소프트웨어 개발 생명 주기(요구 분석, 설계, 구현, 검사 등) 전체 또는 일부를 **컴퓨터와 전용 도구를 사용해 자동화**하는 기법.
- 개발의 표준화를 지향하며 생산성 및 품질을 향상시킵니다.

---

> **Mạch chuyển:** Từ **trường hợp (case / 사례) (Computer Aided Software Engineering)**, chuyển sang **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)

### 1. 회복 기법 (Recovery)
장애 발생 시 데이터베이스를 정상 상태로 복구합니다.
- **연기 갱신 (Deferred Update)**: 트랜잭션이 완료될 때까지 DB 갱신을 연기하고 로그(Log)에 보관. 실패 시 무시하면 됨. (Redo만 가능).
- **즉각 갱신 (Immediate Update)**: 즉시 DB에 갱신하고 로그에 보관. 실패 시 취소(Undo)와 재실행(Redo) 모두 사용.
- **그림자 페이지 (Shadow Paging)**: 복사본(그림자) 페이지를 보관해두고, 실패 시 대체하는 방식 (로그 불필요).
- **검사점 (Check Point)**: 특정 단계에 검사점을 찍어 장애 시 그 시점부터 회복(시간 절약).

### 2. 병행 제어 기법 (Concurrency Control)
다중 트랜잭션 실행 시 DB의 일관성이 파괴되지 않도록 제어합니다.
- **로킹 (Locking)**: 데이터 엑세스 전에 khóa (lock / 잠금)을 요청하는 기법. (로킹 단위: DB, 파일, 레코드 등 한꺼번에 잠그는 크기).
- **타임 스탬프 순서 (Time Stamp Ordering)**: 트랜잭션 실행 전 시간표(Time Stamp)를 부여해 그 순서대로 처리 (교착상태 미발생).
- **다중 버전 기법**: 갱신될 때마다 새로운 버전(Version)을 부여해 관리.

> **Vietnamese Explanation**:
> **khôi phục (recovery / 복구) (Phục hồi DB)** có Deferred (chờ xong mới cập nhật - chỉ Redo), Immediate (cập nhật ngay - cần cả Undo và Redo).
> **tính đồng thời (concurrency / 동시성) điều khiển (control / 제어) (Kiểm soát đồng thời)** dùng Locking (khóa dữ liệu khi đang dùng) hoặc thời gian (time / 시간) Stamp (cấp tem thời gian để xếp hàng trước sau) tránh việc 2 giao dịch cùng sửa 1 dữ liệu gây lỗi.

---

> **Mạch chuyển:** Từ **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)**, chuyển sang **교착상태 (Dead Lock)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 교착상태 (Dead Lock)
둘 이상의 프로세스가 자원을 점유한 상태에서 서로 다른 프로세스의 자원을 무한정 기다리는 현상.

### 1. 교착상태 발생의 4가지 필요충분조건
모두 충족해야 교착상태가 발생합니다.
- **상호 배제 (Mutual Exclusion)**: 한 번에 한 프로세스만 자원 사용.
- **점유와 대기 (Hold and Wait)**: 자원을 점유한 채로 다른 자원을 대기.
- **비선점 (Non-preemption)**: 할당된 자원을 강제로 빼앗을 수 없음.
- **환형 대기 (Circular Wait)**: 대기하는 프로세스들이 원형(Cycle)을 이룸.

### 2. 교착상태 해결 방법
- **예방 (Prevention)**: 4가지 조건 중 하나를 제거 (자원 낭비가 가장 심함).
- **회피 (Avoidance)**: 발생 가능성을 인정하고 적절히 피해감 (**은행원 알고리즘 / Banker's Algorithm**).
- **발견 (Detection)**: 발생 여부를 점검 (자원 할당 그래프 등).
- **회복 (Recovery)**: 교착상태에 있는 프로세스를 종료하거나 자원을 선점하여 회복.

> **Vietnamese Explanation**:
> **Deadlock (Bế tắc)** giống như kẹt xe ở ngã tư, ai cũng chờ người kia nhường đường nên không ai đi được. Để giải quyết, phương pháp **Avoidance (Né tránh)** dùng thuật toán Banker (người giữ tiền) để đảm bảo luôn có đủ tài nguyên cấp phát một cách an toàn.

---

> **Mạch chuyển:** Từ **교착상태 (Dead Lock)**, chuyển sang **침입 탐지 시스템 (IDS; Intrusion Detection System)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 침입 탐지 시스템 (IDS; Intrusion Detection System)
컴퓨터 시스템의 비정상적인 사용, 오용, 남용 등을 실시간으로 탐지하는 시스템.
- **오용 탐지 (Misuse Detection)**: 미리 입력해 둔 공격 패턴 감지 (시그니처 기반).
- **이상 탐지 (Anomaly Detection)**: 평균적인 상태를 기준으로 비정상 행위 감지 (행위 기반).
- **종류**:
  - **HIDS (Host-Based)**: 내부 시스템 감시 (OSSEC 등).
  - **NIDS (Network-Based)**: 외부로부터의 네트워크 트래픽 감시 (Snort 등).

---

> **Mạch chuyển:** Từ **침입 탐지 시스템 (IDS; Intrusion Detection System)**, chuyển sang **리눅스의 커널 로그 (Linux Kernel Logs)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 리눅스의 커널 로그 (Linux Kernel Logs)
- `/var/log/wtmp`: 성공한 로그인/로그아웃 및 시스템 시작/종료 시간 기록.
- `/var/run/utmp`: 현재 로그인한 사용자의 상태 기록.
- `/var/log/btmp`: 실패한 로그인 기록.
- `/var/log/lastlog`: 마지막으로 성공한 로그인 기록.

---

> **Mạch chuyển:** Từ **리눅스의 커널 로그 (Linux Kernel Logs)**, chuyển sang **소프트웨어 생명주기 모델 (SDLC Models)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 소프트웨어 생명주기 모델 (SDLC Models)
- **폭포수 모델 (Waterfall)**: 각 단계를 명확히 마무리한 후 다음 단계로 넘어가는 선형 순차적 모델 (요구사항 변경 어려움).
- **프로토타입 모델 (Prototyping)**: 시제품(Prototype)을 만들어 최종 결과물을 예측.
- **나선형 모델 (Spiral)**: 점진적으로 개발하며 **위험 분석(Risk Analysis)** 기능을 추가한 대형 프로젝트용 모델.
- **V 모델 (V Model)**: 폭포수 모델에 테스트 단계를 세부적으로 추가하여 검증을 강화한 모델.

> **Vietnamese Explanation**:
> - **Waterfall (Thác nước)**: Làm xong bước này mới qua bước khác.
> - **Prototyping (Mẫu thử)**: Làm một bản nháp cho khách hàng xem trước.
> - **Spiral (Xoắn ốc)**: Làm từng phần và liên tục đánh giá rủi ro (Risk analysis).
> - **V mô hình (model / 모델) (Chữ V)**: Nhấn mạnh vào việc kiểm thử (Testing) ở mỗi giai đoạn tương ứng.

---

> **Mạch chuyển:** Từ **소프트웨어 생명주기 모델 (SDLC Models)**, chuyển sang **스토리지 시스템 (Storage Systems)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 스토리지 시스템 (Storage Systems)
대용량 데이터를 저장하기 위한 장치 구성 방식.
- **DAS (Direct Attached Storage)**: 서버와 스토리지를 전용 케이블로 **직접 연결**.
- **NAS (Network Attached Storage)**: 서버와 스토리지를 **네트워크(LAN)**로 연결.
- **SAN (Storage Area Network)**: 스토리지 전용 **광 채널 네트워크(FC-SAN)**를 별도로 구성하여 고속 전송.

💡 **Mẹo ghi nhớ (Mnemonics):**
- **DAS**: Direct (Cắm trực tiếp).
- **NAS**: mạng (network / 네트워크).
- **SAN**: Area mạng (network / 네트워크).

---

> **Mạch chuyển:** Từ **스토리지 시스템 (Storage Systems)**, chuyển sang **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)
- **개념**: 연속된 메모리 공간을 사용하는 프로그램에서 할당된 메모리의 범위를 넘어선 위치에서 자료를 읽거나 쓰려고 할 때 발생하는 취약점.
- **Tiếng Việt**: Lỗ hổng xảy ra khi chương trình ghi hoặc đọc dữ liệu vượt quá giới hạn vùng nhớ đã được cấp phát.
- **예시 (Example)**:
  - (KR) 10바이트 공간에 20바이트의 데이터를 입력하면 다른 메모리 영역을 침범함.
  - (VN) Nhập 20 byte dữ liệu vào mảng chỉ có kích thước 10 byte, làm ghi đè lên các vùng nhớ khác.
- **대책**: 버퍼의 크기를 적절히 설정.
- 💡 **Mẹo ghi nhớ**: Buffer Overflow = Bơm nước quá đầy làm tràn ly.

---

> **Mạch chuyển:** Từ **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)**, chuyển sang **2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)
- **개념**: 외부 입력값을 통해 시스템 명령어의 실행을 유도함으로써 권한을 탈취하거나 장애를 유발하는 취약점.
- **Tiếng Việt**: Chèn các lệnh hệ điều hành thông qua đầu vào của người dùng để thực thi trái phép trên máy chủ (server / 서버).
- **예시 (Example)**:
  - (KR) 웹 입력창에 `; rm -rf /` 와 같은 명령어를 삽입하여 서버 파일을 삭제.
  - (VN) Chèn lệnh `; rm -rf /` vào ô đầu vào (input / 입력) trên web để xoá tệp (file / 파일) trên máy chủ.
- **대책**: 외부 입력값을 검증 없이 내부 명령어로 사용하지 않음.

---

> **Mạch chuyển:** Từ **2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)**, chuyển sang **3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)
- **개념**: 로그인 세션이나 쿠키가 남아 있는 사용자의 브라우저가 공격자가 의도한 상태 변경 요청을 보내도록 유도하는 취약점.
- **Tiếng Việt**: Lợi dụng phiên đăng nhập (session) hợp lệ của người dùng để thực hiện các yêu cầu không mong muốn.
- **예시 (Example)**:
  - (KR) 로그인된 상태에서 공격자가 보낸 링크를 클릭하면 내 계정에서 몰래 송금이 됨.
  - (VN) Khi đang đăng nhập ngân hàng, lỡ click vào link của hacker thì bị tự động chuyển tiền.
- **대책**: CSRF 토큰과 SameSite 쿠키를 사용하고, 서버에서 Origin/Referer와 인증 상태를 검증한다. POST만으로는 충분하지 않다.
- 💡 **Mẹo ghi nhớ**: C-S-R-F = Cứ Sợ Rằng Fake (Sợ người dùng thật nhưng gửi request fake).

---

> **Mạch chuyển:** Từ **3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)**, chuyển sang **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)
- **개념**: 널 포인터(값이 없는 메모리 주소)가 가리키는 메모리에 값을 저장하거나 읽을 때 발생하는 오류.
- **Tiếng Việt**: Lỗi xảy ra khi cố gắng đọc/ghi dữ liệu thông qua con trỏ đang có giá trị Null.
- **예시 (Example)**:
  - (KR) 객체가 생성되지 않았는데 그 객체의 메서드를 호출하여 시스템이 다운됨.
  - (VN) Gọi hàm của một đối tượng chưa được khởi tạo (bằng Null), làm app bị crash.

---

> **Mạch chuyển:** Từ **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)**, chuyển sang **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)
- **개념**: 입력 길이·권한·오류 조건을 충분히 검증하지 않는 API를 사용하여 취약점을 만드는 것 (예: C언어의 `strcpy`, `strcat`).
- **Tiếng Việt**: Sử dụng các hàm không an toàn, dễ gây lỗi tràn bộ đệm (như `strcpy`).
- **예시 (Example)**:
  - (KR) 길이 제한이 없는 `strcpy()` 대신 입력 길이와 널 종료를 명시적으로 검증한다. `strncpy()`도 널 종료가 보장되지 않을 수 있으므로 무조건 안전한 대체재로 보지 않는다.
  - (VN) Dùng `strncpy()` (có giới hạn độ dài) thay cho `strcpy()` (copy không giới hạn).

---

---

> **Mạch chuyển:** Từ **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)**, chuyển sang **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)

---

> **Mạch chuyển:** Từ **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)**, chuyển sang **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)
- **대칭 키 (Symmetric Key)**: 암호화 키 = 복호화 키 (비밀 키).
  - 속도가 빠름, 키 관리가 어려움 (Nhanh nhưng khó quản lý phân phối key).
  - 종류 (Các loại): DES, AES, SEED, ARIA, IDEA (Block); RC4, LFSR (Stream).
- **비대칭 키 (Asymmetric Key)**: 암호화 키(공개 키) ≠ 복호화 키(개인 키).
  - 속도가 느림, 키 분배 및 관리가 쉬움 (Chậm nhưng dễ phân phối key, an toàn).
  - 종류 (Các loại): RSA, ECC, Diffie-Hellman.
- 💡 **Mẹo ghi nhớ**:
  - 대칭 (Đại xưng) = 비밀 (Bí mật chung) -> AES, DES.
  - 비대칭 (Bất đại xưng) = 공개 (Công khai 1 nửa) -> RSA.

---

# 107 서비스 공격 기법 (Service Attack Techniques / Kỹ thuật tấn công dịch vụ)

- **Backdoor (백도어)**: 시스템 인증 절차를 우회하여 몰래 접속하는 경로 (Cửa sau, lách xác thực).
- **Key Logger (키로거)**: 키보드 입력 움직임을 탐지하여 비밀번호 등을 탈취 (Ghi lại thao tác bàn phím).
- **Rootkit (루트킷)**: 시스템 침입 사실을 숨기고 관리자 권한을 유지하는 도구 모음 (Bộ công cụ che giấu xâm nhập và giữ quyền admin).
- **Phishing, Smishing, Qshing (피싱, 스미싱, 큐싱)**: 이메일(Phishing), 문자(Smishing), QR코드(Qshing)로 개인정보 탈취 (Lừa đảo lấy thông tin qua mail, SMS, mã QR).
- **Zombie PC & Botnet (좀비 PC & 봇넷)**: 악성 봇에 감염되어 해커(C&C서버)의 명령에 따라 DDoS 공격 등을 수행하는 PC 무리 (Máy tính bị nhiễm bot, bị điều khiển hàng loạt).
- **Ransomware (랜섬웨어)**: 파일을 암호화하고 돈을 요구하는 악성 프로그램 (Mã độc tống tiền).
- **Zero Day Attack (제로데이 공격)**: 취약점이 공표되기도 전에 이루어지는 공격 (Tấn công ngay khi lỗ hổng vừa được phát hiện, chưa có bản vá).
- **Sniffing (스니핑)**: 네트워크 패킷을 몰래 엿보며 정보 수집 (Nghe lén gói tin trên mạng).
- **Spoofing (스푸핑 - IP, ARP)**: 위조된 IP나 MAC 주소로 속여 인증을 통과하거나 패킷을 가로챔 (Giả mạo địa chỉ IP hoặc MAC).
- **Session Hijacking (세션 하이재킹)**: 이미 로그인된 세션 정보를 가로채어 권한 획득 (Cướp phiên đăng nhập).
- 💡 **Mẹo ghi nhớ**: Spoof = 속이다 (Fake/Giả mạo), Sniff = 킁킁거리다 (Nghe lén/Trộm xem).

---

---

> **Mạch chuyển:** Từ **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)**, chuyển sang **108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)

---

> **Mạch chuyển:** Từ **108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)**, chuyển sang **1. 인증 기술 (Authentication Types)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 1. 인증 기술 (Authentication Types)
- **지식 기반 (Knowledge)**: 알고 있는 것 (Mật khẩu, mã PIN).
- **소유 기반 (Possession)**: 가지고 있는 것 (Token, Smart Card, OTP).
- **생체 기반 (Biometric)**: 고유한 신체 특징 (Vân tay, mống mắt).
- **행위 기반 (Behavior)**: 행동 특징 (Chữ ký, dáng đi).

---

> **Mạch chuyển:** Từ **1. 인증 기술 (Authentication Types)**, chuyển sang **2. 접근 제어 정책 (Access Control Policies)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 2. 접근 제어 정책 (Access Control Policies)
- **DAC (임의적 접근 통제 / Discretionary)**: 신분(Identity) 기반. 데이터 소유자가 권한 부여.
- **MAC (강제적 접근 통제 / Mandatory)**: 보안등급(Label) 기반. 시스템 관리자가 강제로 권한 부여.
- **RBAC (역할 기반 접근 통제 / Role-Based)**: 역할(Role) 기반. 변경이 용이.
- 💡 **Mẹo ghi nhớ**: DAC = Danh tính, MAC = Mức độ bảo mật, RBAC = Role (Vai trò).

---

# 110 네트워크 보안 솔루션 (Network Security Solutions)
- **방화벽 (Firewall)**: 트래픽 접근 허용/차단 (Tường lửa cơ bản).
- **WAF (웹 방화벽)**: SQL 인젝션, XSS 등 웹 특화 공격 방어 (Tường lửa chuyên cho Web).
- **IDS (침입 탐지 시스템)**: 침입을 실시간으로 "탐지(Detect)" (Hệ thống phát hiện xâm nhập).
- **IPS (침입 방지 시스템)**: 유해 트래픽을 실시간으로 "차단(Prevent)" (Hệ thống ngăn chặn xâm nhập).
- **VPN (가상사설망)**: 공중망을 전용망처럼 안전하게 사용 (Mạng riêng ảo).

---

---

> **Mạch chuyển:** Từ **2. 접근 제어 정책 (Access Control Policies)**, chuyển sang **318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng phần mềm)** để mở rộng cùng một chuỗi khái niệm; hãy giữ lại tiêu chí phân biệt vừa học trước khi đọc mục mới.

---

## 318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng phần mềm)
- **개념**: 검증된 소프트웨어의 일부를 다시 사용 (Sử dụng lại các phần mềm đã được kiểm chứng để giảm chi phí, tăng chất lượng).
- **방법**:
  - **합성 중심 (Composition-Based)**: 블록 조립 (Lắp ráp các block như Lego).
  - **생성 중심 (Generation-Based)**: 추상적 명세로 코드 자동 생성 (Tự động sinh code từ bản đặc tả).
