# 5과목 정보시스템 구축 관리 (Môn 5: Quản lý xây dựng hệ thống thông tin)

## 1. 소프트웨어 개발 방법론 및 프레임워크 (Phương pháp luận & Framework phát triển PM)

### 1.1 구조적 방법론 (Structured Methodology)
- 정형화된 분석 절차에 따라 사용자 요구사항을 파악하여 문서화하는 **처리(Process) 중심**의 방법론이다.
- 복잡한 문제를 다루기 위해 **분할과 정복 (Divide and Conquer)** 원리를 적용한다.
- **Tiếng Việt:** Là phương pháp luận trung tâm vào xử lý (Process), lập tài liệu yêu cầu người dùng theo quy trình phân tích chuẩn. Áp dụng nguyên lý chia để trị (Divide and Conquer) cho các vấn đề phức tạp.
- **Example:**
  - *KR:* 큰 시스템을 여러 개의 작은 모듈로 나누어 개발.
  - *VN:* Chia một hệ thống lớn thành nhiều module nhỏ để phát triển.

### 1.2 정보공학 방법론 (Information Engineering Methodology)
- 정보 시스템의 개발을 위해 정형화된 기법들을 상호 연관성 있게 통합 및 적용하는 **자료(Data) 중심**의 방법론이다.
- 데이터베이스 설계를 위한 데이터 모델링으로 **개체 관계도 (ERD; Entity Relationship Diagram)**를 사용한다.
- **Tiếng Việt:** Phương pháp luận trung tâm vào dữ liệu (Data), tích hợp các kỹ thuật chuẩn hóa để phát triển hệ thống. Sử dụng sơ đồ thực thể liên kết (ERD) cho mô hình hóa dữ liệu.
- **Example:**
  - *KR:* 고객과 주문의 관계를 ERD로 모델링하여 시스템 구축.
  - *VN:* Mô hình hóa mối quan hệ giữa Khách hàng và Đơn hàng bằng ERD để xây dựng hệ thống.

### 1.3 컴포넌트 기반(CBD) 방법론 (Component-Based Development)
- 기존의 시스템이나 소프트웨어를 구성하는 **컴포넌트를 조합**하여 하나의 새로운 애플리케이션을 만드는 방법론이다.
- 분석 단계에서 사용자 요구사항 정의서가 산출된다.
- **Tiếng Việt:** Phương pháp luận tạo ứng dụng mới bằng cách kết hợp các thành phần (component) có sẵn. Tài liệu định nghĩa yêu cầu được tạo ra ở bước phân tích.
- **Example:**
  - *KR:* 결제 컴포넌트와 장바구니 컴포넌트를 조립하여 쇼핑몰 구축.
  - *VN:* Lắp ráp component thanh toán và component giỏ hàng để tạo trang thương mại điện tử.
- 💡 **Mẹo ghi nhớ:** CBD = "Lego" (lắp ráp các mảnh ghép có sẵn).

### 1.4 소프트웨어 개발 프레임워크 (Software Development Framework)
- 공통적으로 사용되는 구성 요소와 아키텍처를 일반화하여 제공해주는 반제품 형태의 소프트웨어 시스템.
- 사업자 종속성이 해소되며, 객체들의 제어를 프레임워크에 넘김으로써 생산성을 향상시킨다.
- **Tiếng Việt:** Hệ thống phần mềm dạng bán thành phẩm cung cấp các thành phần và kiến trúc chung. Giải quyết sự phụ thuộc vào nhà cung cấp và tăng năng suất.
- **Example:**
  - *KR:* Spring 프레임워크를 사용하여 Java 웹 애플리케이션을 빠르게 개발.
  - *VN:* Sử dụng Spring framework để phát triển nhanh ứng dụng web Java.

## 2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)

### 2.1 소프트웨어 재사용 (Software Reuse)
- **이점 (Benefits):** 개발 시간과 비용 단축, 품질 향상, 생산성 향상, 시스템 명세/설계/코드 등 문서 공유.
- **방법 (Methods):**
  - **합성 중심 (Composition-based):** 전자 칩 같은 소프트웨어 부품(모듈)을 만들어 끼워 맞추는 방법.
  - **생성 중심 (Generation-based):** 추상화 형태로 쓰여진 명세를 구체화하여 프로그램을 만드는 방법.
- **Tiếng Việt:** Tái sử dụng phần mềm giúp giảm thời gian/chi phí, tăng chất lượng. 
  - Tổng hợp: lắp ráp các module (như chip).
  - Khởi tạo: tạo chương trình từ đặc tả trừu tượng.
- **Example:**
  - *KR:* 이전에 만든 로그인 모듈을 새 프로젝트에 그대로 재사용.
  - *VN:* Tái sử dụng nguyên bản module đăng nhập đã làm trước đó cho dự án mới.

### 2.2 소프트웨어 재공학 (Software Reengineering)
- 기존 소프트웨어의 데이터와 기능을 변경 및 개선하여 유지보수성과 품질을 높이는 기법.
- **이점 (Benefits):** 위험 부담 감소, 개발 시간/비용 단축, 시스템 명세 오류 억제.
- **주요 활동 (Activities):**
  - **분석 (Analysis):** 명세서 확인 및 재공학 대상 선정.
  - **재구성 (Restructuring):** 코드 재구성하여 구조 향상.
  - **역공학 (Reverse Engineering):** 기존 소프트웨어를 분석하여 설계 정보를 재발견하는 활동.
  - **이식 (Migration):** 다른 운영체제나 하드웨어 환경으로 변환.
- **Tiếng Việt:** Tái thiết kế phần mềm cũ để dễ bảo trì. Các hoạt động chính: Phân tích, Tái cấu trúc, Dịch ngược (Reverse Engineering), và Di chuyển (Migration).
- 💡 **Mẹo ghi nhớ:** Các bước Reengineering: "Phân Tích -> Tái Cấu Trúc -> Dịch Ngược -> Di Chuyển".

### 2.3 CASE (Computer Aided Software Engineering)
- 소프트웨어 개발 과정 전체 또는 일부를 자동화하는 전용 도구.
- **원천 기술 (Core Technologies):** 구조적 기법, 프로토타이핑, 자동 프로그래밍, 정보 저장소, 분산처리.
- **주요 기능 (Major Functions):** 생명 주기 전 단계 연결, 다양한 모델 지원, 그래픽 지원, 자료 흐름도 작성, 모순 검사 등.
- **Tiếng Việt:** Công cụ tự động hóa toàn bộ hoặc một phần quá trình phát triển phần mềm. Hỗ trợ đồ họa, vẽ sơ đồ, kiểm tra lỗi.
- **Example:**
  - *KR:* UML 설계 도구를 사용하여 코드를 자동 생성.
  - *VN:* Sử dụng công cụ thiết kế UML để tự động sinh code.

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
- **Tiếng Việt:** Ước tính dựa trên số dòng code. Tính toán Nỗ lực (Person-Month) = Số dòng code / Số dòng code 1 người viết trong 1 tháng.

#### 수학적 산정 기법 (Mathematical Models)
- **COCOMO 모형:** 원시 프로그램의 규모(LOC)에 의한 산정.
  - 개발 유형: **조직형 (Organic, <50K)**, **반분리형 (Semi-Detached, <300K)**, **내장형 (Embedded, >300K)**.
- **Putnam 모형:** 생명 주기 동안 사용될 노력의 분포를 가정 (Rayleigh-Norden 곡선 기초). **SLIM** 도구 사용.
- **기능 점수 (FP) 모형:** 기능적 요구사항을 점수화. 가중치 증대 요인: 자료 입력, 정보 출력, 명령어(질의), 데이터 파일, 외부 루틴 인터페이스.
- **Tiếng Việt:** 
  - COCOMO: Dựa vào số dòng code (LOC). Gồm Organic (nhỏ), Semi-Detached (vừa), Embedded (lớn).
  - Putnam: Dựa trên đường cong Rayleigh-Norden (Công cụ: SLIM).
  - FP (Function Point): Dựa trên tính năng. 

### 3.3 일정 관리 (Schedule Management)
- **PERT (프로그램 평가 및 검토 기술):** 낙관, 가능, 비관적인 경우로 나누어 종료 시기를 결정. 결정 경로와 임계 경로를 알 수 있음.
- **CPM (임계 경로 기법):** 임계 경로는 프로젝트에서 가장 긴(최장) 경로를 의미한다.
- **간트 차트 (Gantt Chart):** 작업 일정을 막대 도표로 표시 (수평 막대 길이는 기간).
- **Tiếng Việt:** 
  - PERT: Dựa trên thời gian lạc quan, bi quan, khả thi.
  - Đường găng (Critical Path): Đường dài nhất trong sơ đồ mạng.
  - Biểu đồ Gantt: Thể hiện tiến độ bằng thanh ngang.

### 3.4 위험 관리 및 테일러링 (Risk Management & Tailoring)
- **위험 관리 (Risk Analysis):** 돌발 상황(위험)을 미리 예상하고 적절한 대책을 수립.
- **방법론 테일러링 (Tailoring):** 프로젝트 상황에 맞게 방법론 절차나 기법을 수정/보완.
  - 내부적 기준: 목표 환경, 요구사항, 프로젝트 규모, 보유 기술.
  - 외부적 기준: 법적 제약사항(Compliance), 표준 품질 기준.
- **Tiếng Việt:** Quản lý rủi ro (lên phương án phòng ngừa) và Cắt may phương pháp (Tailoring) - điều chỉnh quy trình phát triển cho phù hợp với đặc thù dự án.

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
  - VLAN: Mạng LAN ảo, phân chia logic không phụ thuộc vật lý.

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
  - Docker: Nền tảng container hóa mã nguồn mở.
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
  - Data Mining: Khai phá dữ liệu.
  - OLAP: Xử lý phân tích đa chiều trực tuyến.

### 6.3 시스템 아키텍처 및 프로그래밍 요소
- **SOA (Service Oriented Architecture) 기반 계층:** 표현(Presentation) → 업무 프로세스 → 서비스 중간 → 애플리케이션 → 데이터 저장.
- **접근 지정자 (Access Modifiers):** 외부로부터의 접근을 제한 (Public, Protected, Default, Private).
- **Tiếng Việt:** Kiến trúc hướng dịch vụ (SOA) và các chỉ định truy cập trong lập trình hướng đối tượng (OOP).

## 7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)

### 7.1 회복 및 동시성 제어 (Recovery & Concurrency)
- **회복 (Recovery):** 장애 발생 시 손상 이전의 정상 상태로 복구.
- **즉각 갱신 기법 (Immediate Update):** 트랜잭션 부분 완료 전이라도 즉시 DB에 반영. 갱신 내용은 **Log에 보관**하여 회복에 대비.
- **로킹 단위 (Locking Granularity):** 병행제어에서 한꺼번에 로킹하는 객체 크기.
  - **단위가 크면:** 로크 수가 작아 관리하기 쉽지만 병행성 저하.
  - **단위가 작으면:** 로크 수가 많아 관리 복잡/오버헤드 증가, 하지만 병행성 상승.
- **타임 스탬프 순서 (Time Stamp Ordering):** 직렬성 순서를 결정하기 위해 트랜잭션 처리 순서를 미리 선택.
- **Tiếng Việt:** 
  - Immediate Update: Cập nhật ngay lập tức (dùng Log để phục hồi).
  - Locking Granularity: Kích thước khóa. Khóa lớn -> dễ quản lý, đồng thời thấp. Khóa nhỏ -> khó quản lý, đồng thời cao.

### 7.2 교착상태 (Deadlock)
- **발생 4가지 조건:** 상호 배제(Mutual Exclusion), 점유와 대기(Hold and Wait), 비선점(Non-preemption), 환형 대기(Circular Wait).
- **회피 기법 (Avoidance):** 교착상태 가능성을 피해 나가는 방법. 주로 **은행원 알고리즘 (Banker's Algorithm, E. J. Dijkstra)** 사용.
- **Tiếng Việt:** 4 điều kiện Deadlock: Loại trừ lẫn nhau, Giữ & Chờ, Không trưng dụng, Chờ vòng tròn. Tránh Deadlock dùng Thuật toán Nhà băng.
- 💡 **Mẹo ghi nhớ:** Điều kiện Deadlock: Độc Giữ Không Vòng (Độc quyền, Giữ và chờ, Không ưu tiên, Vòng tròn).

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
- **Tiếng Việt:** Hash là hàm một chiều không thể giải mã (SHA, MD5). Salt là thêm chuỗi ngẫu nhiên trước khi mã hóa để chống tấn công từ điển.

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
- **웜 (Worm):** 연속적으로 **자신을 복제**하여 시스템 부하 유발 (바이러스의 일종).
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
- **Tiếng Việt:** Đặc điểm của Framework: Mô-đun hóa, Tái sử dụng, Khả năng mở rộng, và Đảo ngược quyền điều khiển (IoC - Inversion of Control). Các loại: Spring (Java), e-Government (Hàn Quốc), .NET (Microsoft).

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
  - Flow Control: Sliding Window truyền liên tục dựa vào kích thước cửa sổ mà không cần chờ ACK cho từng gói.

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
- **Tiếng Việt:** Xử lý Deadlock: Phòng ngừa (Prevention) -> Tránh (Avoidance - Thuật toán Banker) -> Phát hiện (Detection) -> Phục hồi (Recovery). Phục hồi DB bằng Log, Shadow Paging, Check Point.

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

EOF
# 데이터 통신 및 통신 프로토콜 (Truyền thông Dữ liệu & Giao thức)

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

## 2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)

### 2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)
- **방향에 따른 분류:** 단방향 (Simplex), 반이중 (Half-Duplex, 무전기), 전이중 (Full-Duplex, 전화).
- **비동기식 (Asynchronous):** 문자마다 Start Bit / Stop Bit를 붙여 전송. 저속 단거리, 오버헤드 큼.
- **동기식 (Synchronous):** 프레임(블록) 단위로 일시에 전송. 속도 빠르고 효율 좋음. 비트/블록 동기 방식.
- **Tiếng Việt:** 
  - Đơn công (Simplex), Bán song công (Half-Duplex), Song công toàn phần (Full-Duplex).
  - Bất đồng bộ: Dùng Start/Stop bit (overhead cao). Đồng bộ: Truyền theo block (nhanh, hiệu quả).

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

## 4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)

### 4.1 오류 발생 원인 및 제어 (Error Causes & Control)
- **원인:** 감쇠, 지연 왜곡, 상호 변조, 누화 잡음, 충격성 잡음(디지털 통신 주요인).
- **FEC (순방향 오류 수정):** 수신 측에서 스스로 수정 (해밍 코드 등). 오버헤드 큼, 역채널 불필요.
- **BEC (역방향 오류 수정):** 오류 시 재전송(ARQ) 요구 (패리티, CRC 등).
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
  - CRC: Kiểm tra đa thức (phổ biến nhất). Hamming Code: Sửa được lỗi 1 bit.

### 4.3 교환 방식 (Switching Methods)
- **회선 교환 (Circuit Switching):** 물리적 전용선 할당. 고정 대역, 연속적 데이터 전송. (접속 지연 O, 전송 지연 X). 전화망.
- **축적 교환 (Store-and-Forward):** 데이터를 저장했다가 경로를 찾아 전송.
  - **메시지 교환 (Message Switching):** 전체 메시지 전송. 지연 매우 긺.
  - **패킷 교환 (Packet Switching):** 패킷 단위로 잘라서 전송 (다음 파트에서 상세 서술).
- **Tiếng Việt:** 
  - Circuit Switching (Chuyển mạch kênh): Tạo đường truyền vật lý (Điện thoại).
  - Message Switching (Chuyển mạch thông điệp): Lưu rồi chuyển toàn bộ.

EOF
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
- **Tiếng Việt:** Routing có Static (Tĩnh), Adaptive (Động), Flooding (Tràn ngập). Congestion Control giúp chống quá tải mạng.

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
- **IPv6:** 128비트 (16비트 × 8부분, 16진수, 콜론 `:` 구분). 주소 부족 문제 해결.
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
  - L2: Bridge (Nối LAN).
  - L3: Router (Định tuyến).
  - L4-L7: Gateway (Nối mạng khác giao thức).

## 6. 통신 프로토콜 (Giao thức Truyền thông)

### 6.1 통신 프로토콜 3요소 (Protocol 3 Elements)
- **구문 (Syntax):** 데이터 형식, 코딩.
- **의미 (Semantics):** 제어 정보 및 오류 관리.
- **시간 (Timing):** 속도 조절, 동기화.
- **Tiếng Việt:** 3 yếu tố của giao thức: Cú pháp (Syntax), Ngữ nghĩa (Semantics), Thời gian (Timing).

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


# 정보처리기사 (Information Processing Engineer) - Part 2

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

## 001. 소프트웨어 생명 주기 (Software Life Cycle)
* **개념**: 소프트웨어를 개발하기 위해 정의하고 운용, 유지보수 등의 과정을 각 단계별로 나눈 것. (소프트웨어 수명 주기)
  * *Tiếng Việt*: Vòng đời phần mềm là việc chia quá trình từ định nghĩa, phát triển, vận hành đến bảo trì phần mềm thành các giai đoạn.
  * *Ví dụ*: 앱을 기획하고, 만들고, 출시 후 업데이트하는 전체 과정. (Toàn bộ quá trình từ lên kế hoạch, tạo, đến cập nhật app sau khi ra mắt).

## 002. 소프트웨어 공학 (Software Engineering)
* **개념**: 소프트웨어의 위기를 극복하기 위한 방안으로 연구된 학문. 품질과 생산성 향상 목적.
  * *Tiếng Việt*: Ngành học nghiên cứu các phương án khắc phục "khủng hoảng phần mềm". Mục đích nâng cao chất lượng và năng suất.
* **기본 원칙**: 현대적 프로그래밍 기술 적용, 지속적 검증, 명확한 기록 유지.
  * *Tiếng Việt*: Áp dụng kỹ thuật lập trình hiện đại, xác minh liên tục, duy trì ghi chép (tài liệu) rõ ràng.

## 003. 폭포수 모형 (Waterfall Model)
* **개념**: 이전 단계로 돌아갈 수 없다는 전제하에 각 단계를 확실히 매듭짓고 다음 단계를 진행하는 고전적 모형. 선형 순차적.
  * *Tiếng Việt*: Mô hình thác nước - mô hình cổ điển, tuần tự tuyến tính. Hoàn thành dứt điểm một giai đoạn rồi mới sang giai đoạn tiếp theo, không thể quay lại.
  * *Ví dụ*: 건축에서 설계도가 완성된 후 시공을 시작하는 것과 같습니다. (Giống như trong xây dựng, hoàn thành bản thiết kế rồi mới bắt đầu thi công).
  * 💡 *Mnemonic*: 폭포수(Thác nước) - Nước chỉ chảy xuống, không chảy ngược (Không quay lại bước trước).

## 004. 나선형 모형 (Spiral Model / 점진적 모형)
* **개념**: 폭포수 모형과 프로토타입 모형의 장점에 **위험 분석(Risk Analysis)** 기능을 추가한 모형.
  * *Tiếng Việt*: Mô hình xoắn ốc kết hợp ưu điểm của mô hình thác nước và prototype, thêm chức năng **phân tích rủi ro**. Phát triển dần dần lặp đi lặp lại.
  * *단계 (Giai đoạn)*: 계획 수립 (Lên kế hoạch) -> 위험 분석 (Phân tích rủi ro) -> 개발 및 검증 (Phát triển & Kiểm chứng) -> 고객 평가 (Khách hàng đánh giá).
  * 💡 *Mnemonic*: **나**선형은 **위**험하다 -> 나선형 모형 = 위험 분석 (Spiral = Risk).

## 005. 애자일 모형 (Agile Model)
* **개념**: 고객의 요구사항 변화에 유연하게 대응할 수 있도록 일정한 주기를 반복하면서 개발과정을 진행 (민첩함).
  * *Tiếng Việt*: Mô hình linh hoạt. Tiến hành phát triển lặp đi lặp lại theo chu kỳ nhất định để phản ứng linh hoạt với sự thay đổi yêu cầu của khách hàng.
  * *Các phương pháp*: Scrum, XP, Kanban, Lean, Crystal, FDD, v.v.

## 006. 애자일 개발 4가지 핵심 가치 (4 Core Values of Agile)
1. 프로세스와 도구보다는 **개인과 상호작용** (Cá nhân và tương tác hơn là quy trình và công cụ).
2. 방대한 문서보다는 **실행되는 SW** (Phần mềm chạy được hơn là tài liệu đồ sộ).
3. 계약 협상보다는 **고객과 협업** (Cộng tác với khách hàng hơn là đàm phán hợp đồng).
4. 계획을 따르기 보다는 **변화에 반응** (Phản ứng với sự thay đổi hơn là bám sát kế hoạch).
  * 💡 *Mnemonic*: 개/실/고/변 (Cá nhân, Chạy được, Khách hàng, Thay đổi).

## 007. 스크럼 (Scrum)
* **개념**: 팀이 중심이 되어 개발의 효율성을 높이는 방법. 팀원 스스로 구성(self-organizing) 및 해결(cross-functional).
  * *Tiếng Việt*: Khung làm việc (framework) mà nhóm làm trung tâm để tăng hiệu quả phát triển. Tự tổ chức và làm việc chéo chức năng.
* **구성요소**:
  * **제품 책임자 (PO; Product Owner)**: 요구사항 작성, 우선순위 갱신. (Chủ sản phẩm: viết yêu cầu, cập nhật độ ưu tiên).
  * **스크럼 마스터 (SM; Scrum Master)**: 가이드 역할, 일일 회의 주관, 장애 요소 공론화. (Người điều phối: hướng dẫn, loại bỏ cản trở).
  * **개발팀 (DT; Development Team)**: PO와 SM을 제외한 모든 팀원 (디자이너, 테스터 등 포함). (Nhóm phát triển).

## 008. 스크럼 개발 프로세스 (Scrum Process)
* **제품 백로그 (Product Backlog)**: 요구사항 우선순위 목록. (Danh sách toàn bộ yêu cầu dự án).
* **스프린트 계획 회의 (Sprint Planning)**: 단기 일정 수립. (Lập kế hoạch cho Sprint).
* **스프린트 (Sprint)**: 2~4주 실제 개발 작업. (Chu kỳ phát triển thực tế, 2-4 tuần).
* **일일 스크럼 회의 (Daily Scrum)**: 매일 15분 진행 상황 점검 (서서 진행). (Họp đứng hàng ngày 15 phút).
* **스프린트 검토 회의 (Sprint Review)**: 고객 앞에서 테스팅/데모. (Đánh giá/Demo sản phẩm với khách hàng).
* **스프린트 회고 (Sprint Retrospective)**: 규칙 준수 여부, 개선점 확인. (Nhìn lại quá trình, rút kinh nghiệm).

## 009. XP (eXtreme Programming)
* **개념**: 고객의 참여와 개발 과정의 반복을 극대화하여 유연하게 대응. 짧고 반복적인 개발 주기, 단순한 설계.
  * *Tiếng Việt*: Lập trình cực hạn. Tối đa hóa sự tham gia của khách hàng và lặp lại quá trình phát triển. Chu kỳ ngắn, thiết kế đơn giản.
* **5가지 핵심 가치**: 의사소통 (Communication), 단순성 (Simplicity), 용기 (Courage), 존중 (Respect), 피드백 (Feedback).
  * 💡 *Mnemonic*: 의/단/용/존/피 (Giao tiếp, Đơn giản, Dũng cảm, Tôn trọng, Phản hồi).

## 010. XP의 주요 실천 방법 (XP Practices)
* **Pair Programming**: 짝 프로그래밍 (책임 공동 소유). (Lập trình theo cặp).
* **Collective Ownership**: 공동 코드 소유. (Sở hữu mã chung).
* **Test-Driven Development (TDD)**: 테스트 주도 개발 (코드 작성 전 테스트 케이스 먼저 작성). (Phát triển hướng kiểm thử - Viết test trước).
* **Whole Team**: 전체 팀 참여 (고객 포함). (Làm việc theo toàn đội).
* **Continuous Integration**: 계속적인 통합 (지속적 통합). (Tích hợp liên tục).
* **Refactoring**: 리팩토링 (기능 변경 없이 단순화, 유연성 강화). (Tái cấu trúc mã nguồn).
* **Small Releases**: 소규모 릴리즈. (Phát hành quy mô nhỏ).

## 011. 현행 시스템 파악 3단계 (Current System Analysis Steps)
* **1단계**: 시스템 구성 파악, 시스템 기능 파악, 시스템 인터페이스 파악. (Nắm bắt cấu trúc, chức năng, giao diện hệ thống).
* **2단계**: 아키텍처 구성 파악, 소프트웨어 구성 파악. (Nắm bắt kiến trúc, phần mềm).
* **3단계**: 하드웨어 구성 파악, 네트워크 구성 파악. (Nắm bắt phần cứng, mạng).

## 012. 운영체제 (OS, Operating System)
* **개념**: 컴퓨터 자원을 효율적으로 관리하고 사용자가 편리하게 사용할 수 있도록 환경을 제공하는 시스템 소프트웨어. (Windows, UNIX, Linux, iOS, Android 등).
  * *Tiếng Việt*: Hệ điều hành. Phần mềm hệ thống quản lý tài nguyên máy tính và cung cấp môi trường thuận tiện cho người dùng.
* **요구사항 식별 시 고려사항**: 가용성, 성능, 기술 지원, 주변 기기, 구축 비용. (Khả năng khả dụng, Hiệu suất, Hỗ trợ kỹ thuật, Thiết bị ngoại vi, Chi phí xây dựng).

## 013. 데이터베이스 관리 시스템 (DBMS)
* **개념**: 데이터 종속성과 중복성 문제를 해결하고, 데이터베이스를 관리해 주는 소프트웨어. (Oracle, MySQL, MongoDB 등).
  * *Tiếng Việt*: Hệ quản trị cơ sở dữ liệu. Giải quyết vấn đề phụ thuộc và trùng lặp dữ liệu.
* **고려사항**: 가용성, 성능, 기술 지원, 상호 호환성, 구축 비용. (Khả năng khả dụng, Hiệu suất, Hỗ trợ kỹ thuật, Khả năng tương thích, Chi phí).

## 014. 웹 애플리케이션 서버 (WAS)
* **개념**: 동적인 콘텐츠를 처리하기 위해 사용되는 미들웨어 (Tomcat, JEUS, WebLogic 등). 데이터베이스 서버와 주로 연동.
  * *Tiếng Việt*: Máy chủ ứng dụng web. Middleware dùng để xử lý nội dung động, thường kết nối với máy chủ cơ sở dữ liệu (Database server).
  * *Ví dụ*: 쇼핑몰에서 사용자마다 장바구니 내용이 다르게 보이게 처리하는 역할. (Xử lý giỏ hàng hiển thị khác nhau cho từng người dùng trên web e-commerce).

## 015. 요구사항 정의 (Requirements Definition)
* **기능 요구사항 (Functional)**: 시스템이 **무엇을 하는지**, 반드시 수행해야 하는 기능. (입력/출력, 데이터 저장/연산).
  * *Tiếng Việt*: Yêu cầu chức năng. Hệ thống phải "làm gì", các chức năng bắt buộc. (vd: Chức năng đăng nhập).
* **비기능 요구사항 (Non-functional)**: 장비 구성, **성능** (처리 속도), 인터페이스, 보안, 품질, 제약사항 등.
  * *Tiếng Việt*: Yêu cầu phi chức năng. Liên quan đến hiệu suất, bảo mật, chất lượng, ràng buộc... (vd: Hệ thống phải phản hồi trong 2 giây).

## 016. 요구사항 개발 프로세스 (Requirements Development Process)
* **순서**: 도출(Elicitation) -> 분석(Analysis) -> 명세(Specification) -> 확인(Validation).
  * *Tiếng Việt*: Rút trích/Thu thập -> Phân tích -> Đặc tả -> Xác nhận.
  * 💡 *Mnemonic*: 도/분/명/확 (Thu thập, Phân tích, Đặc tả, Xác nhận).
* **도출(수집)**: 인터뷰, 설문, 브레인스토밍, 프로토타이핑, 유스케이스 등으로 요구사항 식별. (Phỏng vấn, khảo sát, dùng mẫu thử... để xác định yêu cầu).



## 017. 요구사항 명세 기법 (Requirements Specification Techniques)
* **정형 명세 기법 (Formal)**: 수학적 기호와 정형화된 표기법 사용. 작성자에 관계없이 일관성 유지. 표기법이 어려움. (VDM, Z, Petri-net, CSP 등)
  * *Tiếng Việt*: Kỹ thuật đặc tả hình thức. Sử dụng ký hiệu toán học. Nhất quán cao nhưng khó hiểu.
* **비정형 명세 기법 (Informal)**: 자연어, 다이어그램 기반. 의사소통 용이. 작성자에 따라 해석이 다를 수 있음. (FSM, Decision Table, ER 모델링 등)
  * *Tiếng Việt*: Kỹ thuật đặc tả phi hình thức. Dựa trên ngôn ngữ tự nhiên và sơ đồ. Dễ hiểu, dễ giao tiếp nhưng thiếu nhất quán.
  * *Ví dụ*: "사용자는 비밀번호를 입력한다" (비정형) vs 수식 형태의 상태 전이 조건 (정형). (Dùng câu tự nhiên vs Dùng công thức).

## 018. 요구사항 분석의 개요 (Overview of Requirements Analysis)
* **개념**: 소프트웨어 개발의 실제적인 첫 단계로 요구사항을 이해하고 문서화(명세화)하는 활동.
  * *Tiếng Việt*: Bước đầu tiên thực tế của phát triển phần mềm, hiểu và tài liệu hóa (đặc tả) yêu cầu.
* **도구 (Tools)**: UML, 자료 흐름도(DFD), 자료 사전(DD), 소단위 명세서(Mini-Spec), 개체 관계도(ERD), 상태 전이도(STD) 등.

## 019. 자료 흐름도 (DFD; Data Flow Diagram)
* **개념**: 자료의 흐름 및 변환 과정과 기능을 도형 중심으로 기술하는 방법 (버블 차트라고도 함).
  * *Tiếng Việt*: Sơ đồ luồng dữ liệu. Mô tả quá trình biến đổi và luồng dữ liệu bằng hình khối (còn gọi là Bubble Chart).
* **구성요소 (Components)**:
  * **프로세스 (Process)**: 원 (O). 자료 처리 과정. (Xử lý dữ liệu).
  * **자료 흐름 (Data Flow)**: 화살표 (->). 자료의 이동. (Luồng di chuyển của dữ liệu).
  * **자료 저장소 (Data Store)**: 평행선 (=). 자료가 저장되는 곳 (DB/File). (Nơi lưu trữ dữ liệu).
  * **단말 (Terminator)**: 사각형 ([]). 시스템과 교신하는 외부 개체 (정보의 생산/소비). (Thực thể bên ngoài giao tiếp với hệ thống).

## 020. 자료 사전 (DD; Data Dictionary)
* **개념**: 자료 흐름도에 있는 자료를 더 자세히 정의하고 기록한 것 (메타 데이터).
  * *Tiếng Việt*: Từ điển dữ liệu. Định nghĩa chi tiết các dữ liệu trong DFD (metadata - dữ liệu của dữ liệu).
* **기호 (Symbols)**:
  * `=` : ~로 구성되어 있다 (is composed of) (Bao gồm)
  * `+` : 그리고 (and) (Và)
  * `( )` : 생략 가능 (optional) (Có thể bỏ qua)
  * `[ | ]` : 선택 (or) (Hoặc / Lựa chọn)
  * `{ }` : 반복 (iteration) (Lặp lại)
  * `* *` : 주석 (comment) (Chú thích)
  * 💡 *Mnemonic*: 괄호는 생략, 대괄호는 선택, 중괄호는 반복. (Ngoặc đơn: Bỏ qua, Ngoặc vuông: Chọn, Ngoặc nhọn: Lặp).

## 021. 요구사항 분석을 위한 CASE (자동화 도구) (CASE Tools for Req. Analysis)
* **SADT**: SoftTech사 개발. 구조적 분석 및 설계 도구. (Công cụ phân tích cấu trúc của SoftTech).
* **SREM (RSL/REVS)**: TRW사 개발. 실시간 처리 소프트웨어 시스템을 위한 도구. (Công cụ cho hệ thống xử lý thời gian thực).
* **PSL/PSA**: 미시간 대학 개발. (Đại học Michigan phát triển).
* **TAGS**: 시스템 공학 방법 응용을 위한 통합 자동화 도구. (Công cụ tự động hóa tích hợp).

## 022. HIPO (Hierarchy Input Process Output)
* **개념**: 시스템의 기능을 입력, 처리, 출력으로 나타내는 하향식 소프트웨어 개발을 위한 문서화 도구. 보기 쉽고 이해하기 쉬움.
  * *Tiếng Việt*: Công cụ tài liệu hóa cho phát triển phần mềm từ trên xuống, thể hiện chức năng qua Đầu vào (Input), Xử lý (Process), Đầu ra (Output). Dễ nhìn, dễ hiểu.
* **종류 (Types of HIPO Chart)**:
  * **가시적 도표 (Visual Table of Contents)**: 시스템 전체 기능과 흐름의 계층 구조도. (Cấu trúc phân cấp tổng thể).
  * **총체적 도표 (Overview Diagram)**: 입력, 처리, 출력 전반적 정보. (Tổng quan Input-Process-Output).
  * **세부적 도표 (Detail Diagram)**: 기본 요소를 상세히 기술. (Mô tả chi tiết các yếu tố).
  * 💡 *Mnemonic*: 가/총/세 (가시적, 총체적, 세부적). (Visual, Overview, Detail).

## 023. UML (Unified Modeling Language)의 개요
* **개념**: 의사소통이 원활하게 이루어지도록 표준화한 대표적인 객체지향 모델링 언어 (OMG에서 표준 지정).
  * *Tiếng Việt*: Ngôn ngữ mô hình hóa thống nhất (hướng đối tượng). Chuẩn hóa để giao tiếp giữa người phát triển và khách hàng.
* **구성요소**: 사물(Things), 관계(Relationships), 다이어그램(Diagram). (Sự vật, Mối quan hệ, Sơ đồ).

## 024. 관계 (Relationships in UML)
* **연관 관계 (Association)**: 2개 이상 사물이 서로 관련. (Liên kết).
* **집합 관계 (Aggregation)**: 하나의 사물이 다른 사물에 포함. (Tập hợp - độc lập).
* **포함 관계 (Composition)**: 포함하는 사물이 변화하면 포함되는 사물도 영향 받음. (Bao gồm - phụ thuộc chặt chẽ).
* **일반화 관계 (Generalization)**: 일반적(상위) - 구체적(하위) 관계 (상속). (Tổng quát hóa / Kế thừa).
* **의존 관계 (Dependency)**: 필요에 의해 짧은 시간 동안만 연관 유지 (매개 변수 사용 시). (Phụ thuộc).
* **실체화 관계 (Realization)**: 사물이 할 수 있는 기능(인터페이스)을 그룹화. (Hiện thực hóa).

## 025. 다이어그램 (Diagrams in UML)
* **구조적 다이어그램 (Structural - 정적 모델링)**:
  * **클래스(Class)**: 클래스 속성/메소드 관계.
  * **객체(Object)**: 인스턴스 관계.
  * **컴포넌트(Component)**: 구현 모듈 간 관계 (구현 단계).
  * **배치(Deployment)**: 물리적 요소 위치 (구현 단계).
  * **복합체 구조(Composite Structure)**: 복합 구조 내부.
  * **패키지(Package)**: 그룹화된 패키지 관계.
  * 💡 *Mnemonic 구조적*: 클/객/컴/배/복/패 (Class, Object, Component, Deployment, Composite, Package).
* **행위 다이어그램 (Behavioral - 동적 모델링)**:
  * **유스케이스(Use Case)**: 사용자 요구 분석.
  * **순차(Sequence)**: 시간 흐름에 따른 상호 작용 (메시지).
  * **커뮤니케이션(Communication)**: 순차 + 객체 간 연관.
  * **상태(State)**: 상태 변화 (객체지향 동적 모델링).
  * **활동(Activity)**: 객체의 처리 로직 흐름.
  * **상호작용 개요(Interaction Overview)**, **타이밍(Timing)**.
  * 💡 *Mnemonic 행위*: 유/순/커/상/활/상/타 (Use case, Sequence, Communication, State, Activity...).

## 026. 스테레오 타입 (Stereotype)
* **개념**: UML 기본 기능 외에 추가 기능 표현. 겹화살괄호 `<< >>` (길러멧) 사용.
  * *Tiếng Việt*: Mở rộng tính năng của UML. Dùng ký hiệu `<< >>`.
* **종류**: `<<include>>` (포함), `<<extend>>` (확장), `<<interface>>` (인터페이스), `<<exception>>` (예외), `<<constructor>>` (생성자).

## 027. 유스케이스 (Use Case) 다이어그램
* **개념**: 사용자의 관점에서 시스템의 기능을 표현한 것.
  * *Tiếng Việt*: Biểu diễn chức năng hệ thống từ góc nhìn người dùng (Use case diagram).
* **구성요소**: 시스템, 액터(주액터=사람, 부액터=외부시스템), 유스케이스, 관계(연관, 포함, 확장, 일반화).

## 028. 클래스 (Class) 다이어그램
* **개념**: 시스템을 구성하는 클래스와 속성, 오퍼레이션(메소드), 관계 등을 표현.
  * *Tiếng Việt*: Sơ đồ lớp. Thể hiện các lớp, thuộc tính, phương thức và mối quan hệ cấu thành hệ thống.

## 029. 순차 (Sequence) 다이어그램
* **개념**: 시간의 흐름에 따라 상호 작용하는 과정을 그림으로 표현.
  * *Tiếng Việt*: Sơ đồ tuần tự. Thể hiện quá trình tương tác theo dòng thời gian.
* **구성요소**: 액터 (Actor), 객체 (Object), 생명선 (Lifeline), 실행 상자 (Active Box), 메시지 (Message).

## 030. 사용자 인터페이스 (UI)의 특징
* **개념**: 사용자와 시스템 간의 상호작용. 사용자 만족도에 큰 영향. 오류 감소, 편리성 제공.
  * *Tiếng Việt*: Giao diện người dùng. Ảnh hưởng lớn đến sự hài lòng của người dùng. Giảm lỗi, tăng tiện lợi.

## 031. 사용자 인터페이스의 구분 (Types of UI)
* **CLI (Command Line Interface)**: 텍스트 형태 (명령어 입력). (Giao diện dòng lệnh).
* **GUI (Graphical User Interface)**: 아이콘, 마우스 조작. (Giao diện đồ họa).
* **NUI (Natural User Interface)**: 사용자의 말이나 행동. (Giao diện tự nhiên - hành động/giọng nói).
* **VUI (Voice User Interface)**: 음성 조작. (Giao diện giọng nói).
* **OUI (Organic User Interface)**: 사물 인터넷, VR, AR 등 하드웨어 기반 (유기적 인터페이스). (Giao diện hữu cơ).

## 034. 사용자 인터페이스 개발 시스템의 기능
* 입력 검증, 에러 처리/메시지 표시, 도움 및 프롬프트 제공.
  * *Tiếng Việt*: Chức năng hệ thống phát triển UI: Xác thực đầu vào, xử lý lỗi, cung cấp prompt trợ giúp.



## 032. 사용자 인터페이스의 기본 원칙 (UI Design Principles)
* **직관성 (Intuitiveness)**: 누구나 쉽게 이해하고 사용할 수 있어야 함. (Trực quan, dễ hiểu).
* **유효성 (Effectiveness)**: 사용자의 목적을 정확하고 완벽하게 달성. (Hiệu quả, đạt mục đích).
* **학습성 (Learnability)**: 누구나 쉽게 배우고 익힐 수 있어야 함. (Dễ học).
* **유연성 (Flexibility)**: 요구사항을 최대한 수용하고 실수를 최소화. (Linh hoạt).
  * 💡 *Mnemonic*: 직/유/학/유 (직관, 유효, 학습, 유연). (Trực quan, Hiệu quả, Dễ học, Linh hoạt).

## 033. 사용자 인터페이스의 설계 지침 (UI Design Guidelines)
* 사용자 중심, 사용성(Usability - 가장 우선 고려), 심미성, 오류 발생 해결 등.
  * *Tiếng Việt*: Hướng tới người dùng, Tính khả dụng (ưu tiên hàng đầu), Tính thẩm mỹ, Xử lý lỗi.

## 035. UI 설계 도구 (UI Design Tools)
* **와이어프레임 (Wireframe)**: 개략적인 레이아웃이나 UI 요소 뼈대 설계. (손그림, 스케치 등).
  * *Tiếng Việt*: Khung xương (Wireframe). Bố cục sơ lược, thiết kế khung giao diện (Vẽ tay, Sketch).
* **목업 (Mockup)**: 실제 화면과 유사하게 만든 정적인 형태의 모형. (파워 목업 등).
  * *Tiếng Việt*: Mô hình tĩnh (Mockup). Giống màn hình thực tế nhưng không tương tác được.
* **스토리보드 (Story Board)**: 와이어프레임 + 콘텐츠 설명 + 페이지 이동 흐름. (작업 지침서).
  * *Tiếng Việt*: Bảng phân cảnh. Wireframe + mô tả nội dung + luồng chuyển trang. (Tài liệu hướng dẫn công việc).
* **프로토타입 (Prototype)**: 인터랙션을 적용하여 실제 구현된 것처럼 테스트 가능한 동적인 모형.
  * *Tiếng Việt*: Mẫu thử (Prototype). Mô hình động, có thể tương tác nghiệm thu nghiệm như thật.
* **유스케이스 (Use Case)**: 사용자 측면에서의 요구사항 기술.

## 036. 품질 요구사항 (Quality Requirements)
* **ISO/IEC 9126**: 소프트웨어 품질 특성 및 평가 국제 표준. (Tiêu chuẩn quốc tế về chất lượng phần mềm).
* **품질 특성 6가지**:
  1. **기능성 (Functionality)**: 정확하게 만족하는 기능 제공. (Tính chức năng).
  2. **신뢰성 (Reliability)**: 오류 없이 수행. (성숙성, 고장 허용성, 회복성). (Tính tin cậy).
  3. **사용성 (Usability)**: 이해하고 사용하기 쉬운 정도. (이해성, 학습성, 운용성). (Tính khả dụng).
  4. **효율성 (Efficiency)**: 한정된 자원으로 빨리 처리. (시간/자원 효율성). (Tính hiệu quả).
  5. **유지 보수성 (Maintainability)**: 개선하거나 확장하기 쉬운 정도. (Tính bảo trì).
  6. **이식성 (Portability)**: 다른 환경에도 쉽게 적용. (Tính khả chuyển).
  * 💡 *Mnemonic*: 기/신/사/효/유/이 (기능, 신뢰, 사용, 효율, 유지, 이식).

## 037. UI 요소 (UI Elements)
* **체크 박스 (Check Box)**: 다중 선택. (Chọn nhiều).
* **라디오 버튼 (Radio Button)**: 단일 선택. (Chọn một).
* **텍스트 박스 (Text Box)**: 텍스트 입력. (Nhập văn bản).
* **콤보 상자 (Combo Box)**: 목록 표시 + 새로 입력 가능. (Danh sách thả xuống + có thể nhập).
* **목록 상자 (List Box)**: 목록 표시만 (입력 불가). (Chỉ chọn từ danh sách, không nhập được).

## 038. 상위 설계와 하위 설계 (High-level vs Low-level Design)
* **상위 설계 (High-level)**: 아키텍처 설계, 예비 설계. (전체 구조, DB, 인터페이스).
  * *Tiếng Việt*: Thiết kế cấp cao. Kiến trúc tổng thể, DB, giao diện.
* **하위 설계 (Low-level)**: 모듈 설계, 상세 설계. (내부 구조, 컴포넌트, 자료 구조, 알고리즘).
  * *Tiếng Việt*: Thiết kế cấp thấp. Thiết kế chi tiết, thuật toán, cấu trúc dữ liệu.

## 039. 소프트웨어 아키텍처 설계의 기본 원리 (Software Architecture Design Principles)
* **모듈화 (Modularity)**: 기능들을 모듈 단위로 나눔 (유지 관리 용이). (Mô-đun hóa).
* **추상화 (Abstraction)**: 포괄적 개념 설계 후 구체화 (과정, 데이터, 제어 추상화). (Trừu tượng hóa).
* **단계적 분해 (Stepwise Refinement)**: 상위 개념에서 하위 개념으로 구체화 (하향식). (Phân rã từng bước).
* **정보 은닉 (Information Hiding)**: 모듈 내부의 정보를 감추어 다른 모듈이 접근하지 못하게 함. (Che giấu thông tin).

## 040. 소프트웨어 아키텍처의 품질 속성 (Quality Attributes of Architecture)
* 시스템 측면, 비즈니스 측면, 아키텍처 측면으로 구분하여 품질 평가 요소 구체화. (Đánh giá chất lượng từ khía cạnh Hệ thống, Kinh doanh, Kiến trúc).

## 041. 소프트웨어 아키텍처의 설계 과정
* 설계 목표 설정 -> 시스템 타입 결정 -> 아키텍처 패턴 적용 -> 서브시스템 구체화 -> 검토.
  * *Tiếng Việt*: Đặt mục tiêu -> Quyết định loại hệ thống -> Áp dụng Pattern -> Cụ thể hóa subsystem -> Đánh giá.

## 042. 협약(Contract)에 의한 설계 (Design by Contract)
* **선행 조건 (Precondition)**: 오퍼레이션 호출 전 참이어야 할 조건. (Điều kiện tiên quyết).
* **결과 조건 (Postcondition)**: 수행 후 만족되어야 할 조건. (Điều kiện kết quả).
* **불변 조건 (Invariant)**: 실행되는 동안 항상 만족해야 할 조건. (Điều kiện bất biến).

## 043. 파이프 - 필터 패턴 (Pipe - Filter Pattern)
* **개념**: 데이터 스트림을 처리하는 필터(Filter) 컴포넌트들을 파이프(Pipe)로 연결. UNIX Shell이 대표적.
  * *Tiếng Việt*: Mẫu Pipe-Filter. Các bộ lọc xử lý luồng dữ liệu được nối bằng Pipe. Dễ mở rộng, tái sử dụng (VD: UNIX Shell).

## 044. 모델 - 뷰 - 컨트롤러 패턴 (MVC Pattern)
* **Model**: 핵심 기능, 데이터 보관. (Dữ liệu/Logic cốt lõi).
* **View**: 사용자에게 정보 표시. (Giao diện hiển thị).
* **Controller**: 사용자 입력 처리 및 Model 제어. (Xử lý yêu cầu, điều khiển Model).

## 045. 기타 패턴 (Other Architectural Patterns)
* **마스터-슬레이브 (Master-Slave)**: 작업 분할 후 결과 종합 (병렬 컴퓨팅).
* **브로커 (Broker)**: 사용자와 컴포넌트 연결 (분산 환경 시스템).
* **피어-투-피어 (P2P)**: 각 피어가 클라이언트 겸 서버.
* **이벤트-버스 (Event-Bus)**: 채널에 이벤트 발행(Publish), 리스너가 구독(Subscribe).
* **블랙보드 (Blackboard)**: 공유 데이터 저장소 기반 (음성 인식, 신호 해석).
* **인터프리터 (Interpreter)**: 프로그램 코드 해석 클래스 구성.

## 046. 객체 (Object)
* **데이터(속성, 상태, 변수)** + **함수(메소드, 동작, 연산)**로 구성된 소프트웨어 모듈 (캡슐화됨).
  * *Tiếng Việt*: Đối tượng. Bao gồm Dữ liệu (Thuộc tính) và Hàm (Phương thức) được đóng gói.

## 047. 클래스 (Class)
* 공통된 속성과 연산을 갖는 객체의 집합. 객체를 생성하는 '틀'.
  * *Tiếng Việt*: Lớp. Tập hợp các đối tượng có chung thuộc tính và phương thức. Là khuôn mẫu để tạo đối tượng (인스턴스화 - Khởi tạo).

## 048. 캡슐화 (Encapsulation)
* 데이터와 처리 함수를 하나로 묶고 외부 접근을 제한(정보 은닉). 결합도 감소, 재사용 용이.
  * *Tiếng Việt*: Đóng gói. Gộp dữ liệu và hàm xử lý, che giấu chi tiết. Giảm độ kết dính (Coupling), dễ tái sử dụng.

## 049. 상속 (Inheritance)
* 상위 클래스의 속성과 연산을 하위 클래스가 물려받음. 재사용성 증가.
  * *Tiếng Việt*: Kế thừa. Lớp con nhận các thuộc tính/phương thức từ lớp cha.

## 050. 다형성 (Polymorphism)
* 동일한 메시지에 대해 객체마다 고유한 방법으로 응답. (오버로딩, 오버라이딩).
  * *Tiếng Việt*: Đa hình. Cùng một thông điệp nhưng các đối tượng phản hồi theo cách riêng. (VD: Overloading, Overriding).

## 051. 연관성 (Relationship)
* **연관화 (Association)**: is member of (Cùng nhóm/liên quan).
* **분류화 (Classification)**: is instance of (Phân loại).
* **집단화 (Aggregation)**: is part of (Tập hợp thành lớp lớn).
* **일반화 (Generalization)**: is a (Tổng quát hóa / Kế thừa).
* **특수화/상세화 (Specialization)**: Cụ thể hóa (Ngược với 일반화).

## 052. 객체지향 분석의 방법론 (Object-Oriented Analysis Methodologies)
* **Rumbaugh (럼바우)**: 가장 일반적. 객체 모델(Object) -> 동적 모델(Dynamic) -> 기능 모델(Functional).
  * *Tiếng Việt*: Phương pháp Rumbaugh. Phân tích qua 3 mô hình: Đối tượng, Động, Chức năng.
* **Booch (부치)**: 미시적/거시적 프로세스 모두 사용.
* **Jacobson**: 유스케이스(Use Case) 강조.



## 052. 객체지향 분석의 방법론 (Object-Oriented Analysis Methodologies - Continued)
* **Coad와 Yourdon**: E-R 다이어그램을 사용하여 객체의 행위 모델링. (Sử dụng sơ đồ E-R).
* **Wirfs-Brock**: 분석과 설계 간 구분이 없고 연속적으로 수행. (Không phân biệt phân tích và thiết kế, thực hiện liên tục).

## 053. 럼바우(Rumbaugh)의 분석 기법 (OMT)
* **순서**: 객체 모델링 -> 동적 모델링 -> 기능 모델링 (객동기).
  * *Tiếng Việt*: Kỹ thuật phân tích Rumbaugh (OMT). Thứ tự: Mô hình hóa đối tượng -> động -> chức năng.
* **객체 모델링 (Object)**: 정보 모델링. 객체 다이어그램 사용 (속성, 연산 식별). (Mô hình hóa thông tin).
* **동적 모델링 (Dynamic)**: 상태 다이어그램 (시간 흐름에 따른 제어, 상호 작용). (Mô hình hóa động - State diagram).
* **기능 모델링 (Functional)**: 자료 흐름도(DFD) (자료 흐름 중심 처리 과정). (Mô hình hóa chức năng - DFD).

## 054. 객체지향 설계 원칙 (SOLID Principles)
* **S (SRP - 단일 책임 원칙)**: 단 하나의 책임만 가짐. (Nguyên tắc đơn trách nhiệm).
* **O (OCP - 개방-폐쇄 원칙)**: 확장에는 열려 있고(기능 추가), 수정(기존 코드 변경)에는 닫혀 있음. (Mở để mở rộng, Đóng để sửa đổi).
* **L (LSP - 리스코프 치환 원칙)**: 자식 클래스는 부모 클래스의 행위를 대체(수행)할 수 있어야 함. (Nguyên tắc thay thế Liskov).
* **I (ISP - 인터페이스 분리 원칙)**: 사용하지 않는 인터페이스와 의존 관계 맺지 않음. (Nguyên tắc phân tách giao diện).
* **D (DIP - 의존 역전 원칙)**: 추상성이 높은 클래스와 의존 관계를 맺음. (Nguyên tắc đảo ngược phụ thuộc).

## 055. 결합도 (Coupling) - 낮을수록 품질이 높음
* **개념**: 모듈 간에 상호 의존하는 정도 (Mức độ phụ thuộc giữa các mô-đun - Càng thấp càng tốt).
* **순서 (약함 -> 강함) (Tốt -> Xấu)**:
  * **자료 (Data)**: 자료 요소로만 구성.
  * **스탬프 (Stamp)**: 배열/레코드 등 자료 구조 전달.
  * **제어 (Control)**: 논리 흐름 제어를 위해 제어 신호 전달.
  * **외부 (External)**: 외부 모듈의 변수 참조.
  * **공통 (Common)**: 공통 데이터 영역 공유.
  * **내용 (Content)**: 다른 모듈 내부 자료/기능 직접 참조 및 수정.
  * 💡 *Mnemonic*: 자/스/제/외/공/내. (Data, Stamp, Control, External, Common, Content).

## 056. 응집도 (Cohesion) - 높을수록 품질이 높음
* **개념**: 모듈 내부 요소들이 서로 관련되어 있는 정도 (Mức độ gắn kết bên trong mô-đun - Càng cao càng tốt).
* **순서 (강함 -> 약함) (Tốt -> Xấu)**:
  * **기능적 (Functional)**: 모든 기능 요소가 단일 문제와 연관.
  * **순차적 (Sequential)**: 출력 데이터가 다음 활동의 입력 데이터로 사용.
  * **통신적/교환적 (Communication)**: 동일한 입력/출력 사용.
  * **절차적 (Procedural)**: 기능들을 순차적으로 수행.
  * **시간적 (Temporal)**: 특정 시간에 처리되는 기능들을 모음.
  * **논리적 (Logical)**: 유사한 성격/형태로 분류.
  * **우연적 (Coincidental)**: 서로 관련 없는 요소로 구성.
  * 💡 *Mnemonic*: 기/순/통/절/시/논/우.

## 057. 팬인(Fan-In) / 팬아웃(Fan-Out)
* **팬인 (Fan-In)**: 자신을 제어(호출)하는 모듈의 수. (Số lượng mô-đun gọi đến nó - Vào).
* **팬아웃 (Fan-Out)**: 자신이 제어(호출)하는 모듈의 수. (Số lượng mô-đun nó gọi - Ra).

## 058. N-S 차트 (Nassi-Schneiderman Chart)
* **개념**: 논리의 기술에 중점을 둔 도형 (박스 다이어그램).
  * *Tiếng Việt*: Biểu đồ Nassi-Schneiderman. Trọng tâm vào mô tả logic qua hình khối.
* **특징**: GOTO나 화살표 사용 안 함. 선택과 반복 시각적 표현. 임의 제어 전이 불가. (Không dùng GOTO/mũi tên, dễ nhìn nhưng khó vẽ tổng thể).

## 059. 공통 모듈 (Common Module)
* **개념**: 여러 프로그램에서 공통적으로 사용할 수 있는 모듈 (재사용).
* **명세 기법**: 정확성(Correctness), 명확성(Clarity), 완전성(Completeness), 일관성(Consistency), 추적성(Traceability).

## 060. 재사용 (Reuse)
* **개념**: 이미 개발된 기능을 파악, 재구성하여 새 시스템에 사용.
  * *Tiếng Việt*: Tái sử dụng. Sử dụng lại các chức năng đã phát triển (Hàm/Đối tượng -> Component -> Ứng dụng).
* **특징**: 외부 결합도는 낮고 응집도는 높아야 함.

## 061. 효과적인 모듈 설계 방안
* 결합도 줄이고 응집도 높임 (독립성과 재사용성 향상). 복잡도와 중복성 감소. 유지보수 용이. (Giảm Coupling, tăng Cohesion).

## 062. 코드(Code)의 개요
* **기능**: 식별(Identify), 분류(Classify), 배열(Arrange), 표준화(Standardize), 간소화(Simplify). (Chức năng của mã code: nhận dạng, phân loại, sắp xếp, chuẩn hóa, đơn giản hóa).

## 063. 코드의 종류 (Types of Codes)
* **순차 코드 (Sequence)**: 발생 순서대로 일련번호 부여 (1, 2, 3...). (Mã tuần tự).
* **블록 코드 (Block)**: 공통성 있는 것끼리 블록 구분 후 일련번호. (Mã khối).
* **10진 코드 (Decimal)**: 10진 분할 반복 (도서 분류). (Mã thập phân).
* **그룹 분류 코드 (Group Classification)**: 대/중/소분류 구분 후 일련번호. (Mã phân nhóm).
* **연상 코드 (Mnemonic)**: 명칭과 관계있는 문자/숫자 (TV-40). (Mã gợi nhớ).
* **표의 숫자 코드 (Significant Digit)**: 물리적 수치 적용 (120-720). (Mã chữ số có ý nghĩa).
* **합성 코드 (Combined)**: 2개 이상 조합. (Mã tổng hợp).

## 064. 디자인 패턴 (Design Pattern)의 개요
* **개념**: 세부적인 구현 방안 설계 시 참조할 수 있는 전형적인 해결 방식(예제). GoF 디자인 패턴(총 23개).
  * *Tiếng Việt*: Mẫu thiết kế. Giải pháp mẫu cho các vấn đề thường gặp trong thiết kế (GoF có 23 mẫu).
* **분류**: 생성(Creational - 5개), 구조(Structural - 7개), 행위(Behavioral - 11개).

## 065. 디자인 패턴 사용의 장·단점
* **장점**: 구조 파악 용이, 생산성 향상, 개발 시간/비용 절약(재사용), 의사소통 원활.
* **단점**: 초기 투자 비용 부담, 객체지향 기반에만 적합.

## 066. 생성 패턴 (Creational Pattern - 5종)
* 객체의 생성과 참조 과정을 캡슐화하여 유연성 제공. (Mẫu tạo lập - liên quan đến việc tạo đối tượng).
  * **추상 팩토리 (Abstract Factory)**: 연관된 객체 그룹 생성.
  * **빌더 (Builder)**: 조합하여 객체 생성 (건축하듯).
  * **팩토리 메소드 (Factory Method)**: 생성 처리를 서브 클래스로 분리 (Virtual Constructor).
  * **프로토타입 (Prototype)**: 원본 복제 방식.
  * **싱글톤 (Singleton)**: 인스턴스가 하나뿐임을 보장 (메모리 절약).
  * 💡 *Mnemonic*: 추/빌/팩/프/싱 (추상, 빌더, 팩토리, 프로토, 싱글).

## 067. 구조 패턴 (Structural Pattern - 7종)
* 클래스/객체를 조합하여 더 큰 구조 형성. (Mẫu cấu trúc).
  * **어댑터 (Adapter)**: 호환성 없는 인터페이스 변환.
  * **브리지 (Bridge)**: 기능과 구현을 분리(독립적 확장).
  * **컴포지트 (Composite)**: 객체들을 트리 구조로 구성 (단일 객체와 복합 객체 구분 없이 다룸).
  * **데코레이터 (Decorator)**: 객체 결합을 통해 기능 동적 확장.
  * **퍼싸드 (Facade)**: 상위에 인터페이스 구성 (복잡함 숨김, Wrapper 객체).
  * **플라이웨이트 (Flyweight)**: 다수 유사 객체 공유 (메모리 절약).
  * **프록시 (Proxy)**: 접근 어려운 객체의 인터페이스 역할 수행.
  * 💡 *Mnemonic*: 어/브/컴/데/퍼/플/프 (Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy).



## 068. 행위 패턴 (Behavioral Pattern - 11종)
* 객체들 간의 상호작용 및 책임 분배 방법 정의. (Mẫu hành vi - định nghĩa cách tương tác).
  * **책임 연쇄 (Chain of Responsibility)**: 한 객체가 처리 못하면 다음 객체로 넘김.
  * **커맨드 (Command)**: 요청을 캡슐화하여 재이용/취소 (명령어 추상화).
  * **인터프리터 (Interpreter)**: 문법 표현 정의 (SQL, 프로토콜).
  * **반복자 (Iterator)**: 내부 노출 없이 순차적으로 접근.
  * **중재자 (Mediator)**: 복잡한 상호작용을 중재자 객체로 캡슐화(결합도 감소).
  * **메멘토 (Memento)**: 특정 시점 상태 객체화 (되돌리기(Undo) 기능).
  * **옵서버 (Observer)**: 상태 변화 시 상속된 객체들에게 전달 (Publish-Subscribe).
  * **상태 (State)**: 상태에 따라 동일 동작을 다르게 처리.
  * **전략 (Strategy)**: 알고리즘을 캡슐화하여 클라이언트와 독립적으로 상호 교환 가능.
  * **템플릿 메소드 (Template Method)**: 상위 클래스에서 골격 정의, 하위에서 구체화.
  * **방문자 (Visitor)**: 처리 기능을 분리하여 각 클래스를 방문(Visit)하며 수행.
  * 💡 *Mnemonic*: 책/커/인/반/중/메/옵/상/전/템/방.

## 069. 요구사항 검증 방법 (Requirements Validation Methods)
* **요구사항 검토 (Requirements Review)**: 수작업으로 결함 검토.
  * **동료검토 (Peer Review)**: 작성자가 설명하고 동료가 결함 발견. (Kiểm tra chéo).
  * **워크스루 (Walk Through)**: 미리 배포하여 사전 검토 후 짧은 회의. (Kiểm tra từng bước).
  * **인스펙션 (Inspection)**: 작성자 제외한 전문가들이 검토. (Thanh tra bởi chuyên gia).
* **프로토타이핑 (Prototyping)**: 견본품(Prototype) 제작.
* **테스트 설계 (Test Design)**: 테스트 케이스(Test Case) 생성 가능 여부 검토.
* **CASE 도구 활용**: 일관성 분석(Consistency Analysis) 및 변경 추적.

## 070. 시스템 연계 기술 (System Integration Technology)
* **DB Link**: DB 제공 객체 이용. (Liên kết DB).
* **API/Open API**: DB에서 데이터를 읽어와 제공하는 프로그램. (Cung cấp hàm API).
* **연계 솔루션**: EAI 서버와 클라이언트 이용. (Sử dụng giải pháp liên kết EAI).
* **Socket**: 포트 할당하여 클라이언트와 직접 연결. (Giao tiếp Socket).
* **Web Service**: WSDL, UDDI, SOAP 프로토콜 이용. (Dịch vụ Web).

## 071. 연계 매커니즘 구성요소 (Integration Mechanism Components)
* **송신 시스템**: 데이터를 형식(xml, csv 등)에 맞게 변환하여 송신. (Hệ thống gửi).
* **수신 시스템**: 수신한 데이터를 처리할 수 있게 변환하여 반영. (Hệ thống nhận).
* **연계 서버**: 송수신 현황 모니터링 역할. (Máy chủ liên kết).

## 072. 미들웨어 (Middleware)
* **개념**: 운영체제/응용 프로그램 또는 클라이언트/서버 사이에서 서비스 제공. (Phần mềm trung gian).
* **종류**:
  * **DB**: 클라이언트에서 원격 DB 연결.
  * **RPC (Remote Procedure Call)**: 원격 프로시저를 로컬처럼 호출.
  * **MOM (Message Oriented Middleware)**: 비동기형 메시지 전달 (이기종 분산 시스템).
  * **TP-Monitor (Transaction Processing)**: 온라인 트랜잭션 처리/감시 (항공권 예약 등).
  * **ORB (Object Request Broker)**: 코바(CORBA) 표준 스펙 구현 객체지향 미들웨어.
  * **WAS (Web Application Server)**: 동적 콘텐츠 처리 (웹 환경).

---
# 2 과목 소프트웨어 개발 (Subject 2: Software Development)

## 073. 자료 구조의 분류 (Data Structure Classification)
* **선형 구조 (Linear)**: 배열(Array), 선형 리스트(연속/연결 리스트), 스택(Stack), 큐(Queue), 데크(Deque).
  * *Tiếng Việt*: Cấu trúc tuyến tính (Dữ liệu xếp thành 1 hàng).
* **비선형 구조 (Non-Linear)**: 트리(Tree), 그래프(Graph).
  * *Tiếng Việt*: Cấu trúc phi tuyến tính (Dữ liệu có nhiều nhánh).

## 074. 선형 리스트 (Linear List)
* **연속 리스트 (Contiguous List - 배열)**: 연속된 기억장소. 밀도 1. 삽입/삭제 시 자료 이동 필요.
  * *Tiếng Việt*: Danh sách liên tục (Mảng). Vị trí kề nhau. Xóa/chèn chậm do phải dời chỗ.
* **연결 리스트 (Linked List)**: 포인터(링크)로 연결. 임의 공간 저장. 삽입/삭제 용이. 접근 속도 느림.
  * *Tiếng Việt*: Danh sách liên kết. Các node trỏ vào nhau. Xóa/chèn nhanh nhưng tìm kiếm chậm.

## 075. 스택 (Stack)
* **개념**: 한쪽 끝에서만 삽입/삭제 (LIFO - 후입선출).
  * *Tiếng Việt*: Ngăn xếp (Vào sau ra trước).
* **응용 분야**: 함수 호출 순서 제어, 인터럽트 처리, 수식 계산/표기법, 부 프로그램 복귀주소 저장.
  * *Ví dụ*: 웹 브라우저의 '뒤로 가기' 버튼. (Nút Back của trình duyệt web).
* **오버플로(Overflow)**: 꽉 찬 상태에서 삽입 시 발생. / **언더플로(Underflow)**: 빈 상태에서 삭제 시 발생.

## 076. 큐 (Queue)
* **개념**: 한쪽에서는 삽입, 반대쪽에서는 삭제 (FIFO - 선입선출).
  * *Tiếng Việt*: Hàng đợi (Vào trước ra trước).
  * *Ví dụ*: 프린터 인쇄 대기열. (Danh sách chờ in của máy in).

## 077. 방향/무방향 그래프의 최대 간선 수 (Max Edges of Graph)
* 정점이 n개일 때:
  * **무방향 그래프 (Undirected)**: n(n-1) / 2
  * **방향 그래프 (Directed)**: n(n-1)

## 078. 트리의 개요 (Overview of Tree)
* **개념**: 사이클이 없는 특수한 형태의 그래프. (Đồ thị dạng cây không có chu trình).
* **용어**:
  * **근 노드 (Root)**: 최상위 노드.
  * **디그리 (Degree / 차수)**: 특정 노드에서 뻗어 나온 가지 수. 트리의 디그리는 전체 노드 중 최대 디그리.
  * **단말 노드 (Terminal/Leaf)**: 자식이 없는(디그리가 0인) 노드. (Nút lá).

## 079. 트리의 운행법 (Tree Traversal)
* **Preorder (전위)**: Root -> Left -> Right.
* **Inorder (중위)**: Left -> Root -> Right.
* **Postorder (후위)**: Left -> Right -> Root.
  * 💡 *Mnemonic*: Root의 위치에 따라 이름이 결정됨 (전위=앞, 중위=중간, 후위=뒤).

## 080. 수식의 표기법 (Expression Notation)
* **전위 (Prefix)**: 연산자 -> Left -> Right (예: +AB).
* **중위 (Infix)**: Left -> 연산자 -> Right (예: A+B).
* **후위 (Postfix)**: Left -> Right -> 연산자 (예: AB+).
* **변환 방법 (Infix -> Prefix/Postfix)**:
  1. 괄호로 모두 묶기. (Đóng ngoặc toàn bộ biểu thức).
  2. 연산자를 괄호 앞(Prefix)이나 뒤(Postfix)로 이동. (Di chuyển toán tử ra trước hoặc sau ngoặc).
  3. 괄호 제거. (Bỏ ngoặc).



## 081. 삽입 정렬 (Insertion Sort)
* **개념**: 두 번째 값부터 시작하여 앞의 정렬된 부분과 비교해 적절한 위치에 '삽입'하는 정렬.
  * *Tiếng Việt*: Sắp xếp chèn. Chọn phần tử và chèn vào vị trí đúng trong mảng con đã sắp xếp.

## 082. 선택 정렬 (Selection Sort)
* **개념**: 전체 데이터 중 가장 작은(또는 큰) 값을 선택하여 맨 앞의 데이터와 교환하는 방식.
  * *Tiếng Việt*: Sắp xếp chọn. Tìm phần tử nhỏ nhất và hoán đổi với phần tử ở vị trí đầu.

## 083. 버블 정렬 (Bubble Sort)
* **개념**: 인접한 두 값을 비교하여 크기가 순서대로 되어 있지 않으면 교환. (가장 큰 값이 뒤로 밀려남).
  * *Tiếng Việt*: Sắp xếp nổi bọt. So sánh và hoán đổi 2 phần tử kề nhau.

## 084. 퀵 정렬 (Quick Sort)
* **개념**: 기준값(Pivot)을 중심으로 작은 값은 왼쪽, 큰 값은 오른쪽 서브파일로 분할(Divide)하고 정복(Conquer)하는 방식.
  * *Tiếng Việt*: Sắp xếp nhanh. Chia để trị (Dùng Pivot).
* **시간 복잡도**: 평균 O(nlog₂n), 최악 O(n²).

## 085. 힙 정렬 (Heap Sort)
* **개념**: 전이진 트리(Complete Binary Tree)를 이용한 정렬 방식.
  * *Tiếng Việt*: Sắp xếp vun đống (Heap). Dùng cây nhị phân hoàn chỉnh.
* **시간 복잡도**: 평균, 최악 모두 O(nlog₂n).

## 086. 2-Way 합병 정렬 (Merge Sort)
* **개념**: 이미 정렬된 두 개의 파일을 한 개의 파일로 합병하는 정렬 방식.
  * *Tiếng Việt*: Sắp xếp trộn. Trộn 2 mảng đã sắp xếp thành 1.
* **시간 복잡도**: 평균, 최악 모두 O(nlog₂n).

## 087. 이분 검색 (Binary Search)
* **개념**: 전체 파일을 두 개의 서브파일로 분리해 가면서 검색. **반드시 순서화(정렬)된 파일**이어야 함.
  * *Tiếng Việt*: Tìm kiếm nhị phân. Chia đôi mảng để tìm. Bắt buộc mảng phải được sắp xếp trước.
* **공식**: 중간 레코드 번호 M = (F + L) / 2. (F: 첫번째, L: 마지막).

## 088. 해싱 함수 (Hashing Function)
* **종류**:
  * **제산법 (Division)**: 소수(Prime)로 나눈 나머지 사용.
  * **제곱법 (Mid-Square)**: 제곱한 후 중간 부분 값 사용.
  * **폴딩법 (Folding)**: 여러 부분으로 나눈 후 더하거나 XOR 처리.
  * **기수 변환법 (Radix)**: 진수 변환 후 자릿수 조절.
  * **대수적 코딩법 (Algebraic Coding)**: 다항식 나누기 이용.
  * **숫자 분석법 (Digit Analysis)**: 숫자 분포를 분석하여 고른 자리 택함.
  * **무작위법 (Random)**: 난수 발생.

## 089. DBMS (데이터베이스 관리 시스템)의 필수 기능
* **정의 기능 (Definition)**: 데이터 형, 구조, 제약 조건 등 명시. (Định nghĩa dữ liệu).
* **조작 기능 (Manipulation)**: 데이터 검색, 갱신, 삽입, 삭제. (Thao tác dữ liệu).
* **제어 기능 (Control)**: 데이터 무결성 유지, 보안, 병행 수행 제어. (Điều khiển, bảo mật).
  * 💡 *Mnemonic*: 정/조/제 (정의, 조작, 제어).

## 090. DBMS의 장·단점
* **장점**: 데이터 독립성 보장, 중복 최소화, 무결성/일관성 유지, 공동 이용, 보안 유지. (Độc lập, giảm trùng lặp, bảo toàn dữ liệu).
* **단점**: 전문가 부족, 전산화 비용 증가, 과부하(Overhead) 발생, 예비(Backup)/회복(Recovery) 어려움. (Tốn kém, quá tải, khó backup).

## 091. 스키마 (Schema)
* **개념**: 데이터베이스의 구조와 제약 조건에 대한 명세(Meta-Data). (Cấu trúc và ràng buộc của DB).
* **3계층 스키마**:
  * **외부 스키마 (External)**: 사용자나 응용 프로그래머 관점의 논리적 구조 (여러 개 존재). (Góc nhìn người dùng).
  * **개념 스키마 (Conceptual)**: 조직 전체의 통합된 논리적 구조 (단 1개 존재). (Cấu trúc logic toàn hệ thống).
  * **내부 스키마 (Internal)**: 물리적 저장장치 입장의 구조 (저장 데이터 항목 표현 방법). (Góc nhìn lưu trữ vật lý).
  * 💡 *Mnemonic*: 외/개/내.

## 092. 절차형 SQL의 테스트와 디버깅
* 디버깅(Debugging)을 통해 소스 코드 오류 추적 및 수정. (Tìm và sửa lỗi SQL).

## 093. 단위 모듈 (Unit Module)
* **개념**: 한 가지 동작을 수행하는 기능을 모듈로 구현 (독립적인 컴파일 가능). (Mô-đun đơn vị, thực hiện 1 chức năng).
* **구현 순서**: 단위 기능 명세서 작성 -> 입·출력 기능 구현 -> 알고리즘 구현.

## 094. IPC (Inter-Process Communication)
* **개념**: 프로세스 간 통신 방식. (Giao tiếp giữa các tiến trình).
* **대표 메소드**:
  * **Shared Memory**: 공유 가능한 메모리 구성. (Bộ nhớ chia sẻ).
  * **Socket**: 네트워크 소켓을 통한 통신. (Giao tiếp qua mạng).
  * **Semaphores**: 공유 자원 접근 제어. (Kiểm soát truy cập tài nguyên).
  * **Pipes & named Pipes**: FIFO 형태 메모리 공유 (한 프로세스만 접근 가능). (Đường ống).
  * **Message Queueing**: 메시지 전달 형태. (Hàng đợi tin nhắn).

## 095. 단위 모듈 테스트 (Unit Test)
* **개념**: 구현된 단위 모듈이 정해진 기능을 정확히 수행하는지 검증 (화이트박스/블랙박스 테스트 사용). (Kiểm thử mức mô-đun).
* **특징**: 시스템 수준 오류는 잡을 수 없음. 단독 실행 환경과 테스트 데이터 필요.

## 096. 테스트 케이스 (Test Case)
* **개념**: 소프트웨어가 요구사항을 준수했는지 확인하기 위한 명세서 (입력값, 실행 조건, 기대 결과 등). (Ca kiểm thử).
* **구성요소**: 식별자, 테스트 항목, 입력 명세, 출력 명세(예상 결과), 환경 설정, 특수 절차 요구, 의존성 기술.

## 097. 통합 개발 환경 (IDE; Integrated Development Environment)
* **개념**: 코딩, 컴파일, 디버깅, 배포 등 모든 작업을 하나의 프로그램에서 처리. (Môi trường phát triển tích hợp).
* **기능**:
  * **코딩 (Coding)**: 소스 코드 작성.
  * **컴파일 (Compile)**: 목적 프로그램(실행 가능 형태)으로 변환.
  * **디버깅 (Debugging)**: 오류(Bug) 수정.
  * **배포 (Deployment)**: 사용자에게 소프트웨어 전달.

## 098. 빌드 도구 (Build Tools)
* **개념**: 소스 코드를 실행 가능한 소프트웨어로 변환(컴파일 등)하는 작업을 수행하는 소프트웨어. (Công cụ build dự án).
* **종류**:
  * **Ant**: 아파치 재단 개발 (자바 공식 빌드 도구).
  * **Maven**: Ant의 대안 (아파치 재단).
  * **Gradle**: Ant와 Maven 보완 (공동 개발).



## 099. 소프트웨어 패키징 (Software Packaging)
* **개념**: 모듈별로 생성한 실행 파일들을 묶어 배포용 설치 파일을 만드는 것. 사용자 중심 진행.
  * *Tiếng Việt*: Đóng gói phần mềm. Tập hợp các file thực thi thành file cài đặt để phân phối (hướng tới người dùng).

## 100. 패키징 시 고려사항
* 최소 시스템 환경 정의, UI 매뉴얼 일치, 보안 및 암호화(DRM 연동), 사용자 편의성 등 고려. (Định nghĩa môi trường tối thiểu, bảo mật, mã hóa, tiện lợi).

## 101. 릴리즈 노트 (Release Note)
* **개념**: 고객과 공유하기 위한 문서로, 배포 정보, 개선 사항, 테스트 결과 등을 담음.
  * *Tiếng Việt*: Ghi chú phát hành. Tài liệu chia sẻ với khách hàng về tính năng mới, lỗi đã sửa.

## 102. 릴리즈 노트 초기 버전 작성 시 고려사항
* 정확/완전한 정보 기반, **현재 시제**로 개발팀에서 직접 작성.
* **구성요소**: 머리말, 개요, 목적, 문제 요약, 재현 항목, 수정 내용 등.

## 103. 디지털 저작권 관리 (DRM; Digital Right Management)
* **개념**: 저작권자가 배포한 디지털 콘텐츠가 의도한 용도로만 사용되도록 보호/관리하는 기술.
  * *Tiếng Việt*: Quản lý bản quyền kỹ thuật số (DRM). Ngăn chặn sao chép lậu.
* 클리어링 하우스(Clearing House)를 통해 라이선스 및 과금 처리.

## 104. 디지털 저작권 관리(DRM)의 구성 요소
* **클리어링 하우스 (Clearing House)**: 권한/라이선스 발급, 결제 관리. (Nơi cấp phép, thanh toán).
* **콘텐츠 제공자 / 분배자 / 소비자**: 저작권자 / 유통자 / 구매자.
* **패키저 (Packager)**: 콘텐츠 암호화 배포 프로그램. (Mã hóa, đóng gói).
* **DRM 컨트롤러 / 보안 컨테이너**: 이용 권한 통제 및 안전 유통 장치.

## 105. 디지털 저작권 관리(DRM)의 기술 요소
* 암호화, 키 관리, 식별 기술, 저작권 표현(Right Expression), 정책 관리, 크랙 방지(Tamper Resistance), 인증.

## 106 ~ 107. 소프트웨어 설치 매뉴얼 (Installation Manual)
* **개념**: 설치 과정 설명서. 예외 상황/오류 메시지를 별도로 분류하여 설명. (Tài liệu hướng dẫn cài đặt).
* **기본사항**: 개요, 관련 파일, 설치 아이콘, 삭제 방법(Uninstall) 등.

## 108. 소프트웨어 사용자 매뉴얼 (User Manual)
* **개념**: 사용 과정 설명서. 컴포넌트 단위 작성. 배포 후 패치/업그레이드를 위한 버전 관리 필수. (Tài liệu hướng dẫn sử dụng).

## 109. 소프트웨어 패키징의 형상 관리 (SCM; Software Configuration Management)
* **개념**: 소프트웨어 개발 및 유지보수 과정의 모든 '변경 사항'을 체계적으로 추적하고 통제하는 일련의 활동.
  * *Tiếng Việt*: Quản lý cấu hình phần mềm (SCM). Theo dõi và kiểm soát mọi thay đổi của phần mềm.
* **도구**: Git, CVS, Subversion(SVN) 등.

## 110. 형상 관리의 중요성
* 무절제한 변경 방지, 버그 추적 용이, 진행 정도 가시성(Visibility) 제공, 협업 개발 지원. (Ngăn thay đổi vô tội vạ, dễ dò bug, hỗ trợ làm việc nhóm).

## 111. 형상 관리 기능 (SCM Functions)
1. **형상 식별**: 관리 대상(이름/번호) 계층 구조 부여. (Nhận dạng cấu hình).
2. **버전 제어**: 다른 버전 생성 및 관리. (Kiểm soát phiên bản).
3. **형상 통제 (변경 관리)**: 변경 요구 검토 후 기준선(Baseline)에 반영. (Kiểm soát thay đổi).
4. **형상 감사**: 기준선 무결성 검증, 공식 승인. (Kiểm toán cấu hình).
5. **형상 기록 (상태 보고)**: 결과 기록 및 보고서 작성. (Ghi chép trạng thái).
  * 💡 *Mnemonic*: 식/제/통/감/기 (식별, 제어, 통제, 감사, 기록).

## 112. 소프트웨어 버전 등록 관련 주요 기능
* **저장소 (Repository)**: 최신 파일 및 변경 내역 저장소.
* **체크아웃 (Check-Out)**: 수정을 위해 저장소에서 파일 받아옴.
* **체크인 (Check-In)**: 수정 완료 후 저장소로 갱신 (새 버전).
* **커밋 (Commit)**: 충돌 시 해결 후 갱신 완료. (Lưu thay đổi).
* **동기화 (Update)**: 최신 버전으로 작업 공간 동기화.

## 113. 공유 폴더 방식 (Shared Folder)
* 버전 관리 자료가 로컬 공유 폴더에 저장. (SCCS, RCS, PVCS 등).

## 114. 클라이언트/서버 방식 (Client/Server)
* 중앙 서버에서 버전 관리 수행. (CVS, SVN 등). (Quản lý tập trung ở server).

## 115. 분산 저장소 방식 (Distributed Repository)
* 원격 저장소와 개발자 로컬 저장소 함께 사용. (Git, Mercurial, Bitkeeper 등). (Quản lý phân tán).

## 116. Subversion (SVN)
* **개념**: CVS 개선 (클라이언트/서버 구조). 아파치 재단 발표.
* **특징**: `trunk`(메인), `branches`(추가 작업). 커밋(Commit)마다 리비전 1씩 증가. 이름 변경/이동 가능.

## 117. Git (깃)
* **개념**: 리눅스 토발즈 개발. 분산 버전 관리 시스템. (Hệ thống quản lý phiên bản phân tán).
* **특징**: 지역(Local) + 원격(Remote) 저장소. 파일 변화를 **스냅샷(Snapshot)**으로 저장. 오프라인 작업 가능. 빠른 속도, 브랜치 테스팅.

## 118. 빌드 자동화 도구의 개념 (Build Automation Tools)
* **개념**: 컴파일, 테스트, 배포를 자동화. 지속적 통합(CI) 환경에 유용. (Tự động hóa build, test, deploy).
* **종류**: Ant, Maven, Gradle, Jenkins 등.

## 119. Jenkins (젠킨스)
* JAVA 기반 오픈 소스. 서버 기반 (서블릿 컨테이너 실행). 가장 대표적인 CI/CD 도구. (Công cụ CI/CD mã nguồn mở dựa trên Java).



## 120. Gradle
* **개념**: Groovy 기반 오픈 소스 빌드 자동화 도구. (Công cụ build tự động hóa dựa trên Groovy).
* **특징**: 안드로이드 앱 개발 환경에서 주로 사용. DSL 사용. 태스크(Task) 단위 실행. 빌드 캐시(속도 향상).

## 121. 애플리케이션 테스트의 개념
* **확인 (Validation)**: **사용자** 입장, 요구사항 맞게 구현되었는가. (Are we building the right product?).
* **검증 (Verification)**: **개발자** 입장, 명세서에 맞게 만들어졌는가. (Are we building the product right?).

## 122. 애플리케이션 테스트 관련 용어
* **결함 집중 (Defect Clustering)**: 소수의 특정 모듈에 결함 집중. (Lỗi thường tập trung ở vài mô-đun).
* **파레토 법칙 (Pareto Principle)**: 80% 오류는 20% 모듈에서 발견됨. (Quy tắc 80/20).
* **살충제 패러독스 (Pesticide Paradox)**: 동일 테스트 케이스 반복 시 더 이상 오류 발견 못함. (Nghịch lý thuốc trừ sâu).
* **오류-부재의 궤변 (Absence of Errors Fallacy)**: 결함이 없어도 요구사항을 못 맞추면 품질이 높지 않음. (Nguỵ biện không có lỗi).

## 123. 프로그램 실행 여부에 따른 테스트
* **정적 테스트**: 실행 안 함 (워크스루, 인스펙션 등). 초기 오류 발견. (Kiểm thử tĩnh - Không chạy code).
* **동적 테스트**: 프로그램 실행하여 오류 찾음 (블랙박스, 화이트박스). (Kiểm thử động).

## 124. 테스트 기반(Test Bases)에 따른 테스트
* **명세 기반**: 요구사항 명세서 기반 (동등 분할, 경계값 분석 등).
* **구조 기반**: 논리 흐름 파악 (구문, 결정, 조건 기반 등).
* **경험 기반**: 테스터 경험 기반 (에러 추정, 탐색적 테스팅). 시간 제약 시 효과적.

## 126. 목적에 따른 테스트 (Test by Purpose)
* **회복 (Recovery)**: 고의로 실패 유도 후 정상 복구되는지 확인. (Phục hồi).
* **안전 (Security)**: 불법 침입으로부터 보호 확인. (Bảo mật).
* **강도 (Stress)**: 과부하 시 정상 작동 확인. (Chịu tải).
* **성능 (Performance)**: 응답 시간, 처리량 등 효율성 진단. (Hiệu năng).
* **구조 (Structure)**: 내부 논리적 경로, 소스 코드 복잡도 평가. (Cấu trúc).
* **회귀 (Regression)**: 수정된 코드에 새로운 오류가 없는지 확인. (Hồi quy).
* **병행 (Parallel)**: 변경 전후 소프트웨어 동일 데이터 결과 비교. (Song song).

## 127. 화이트박스 테스트 (White Box Test)
* **개념**: 모듈의 '원시 코드'를 오픈하여 **모든 논리적 경로**를 테스트 (개발자 관점).
  * *Tiếng Việt*: Kiểm thử hộp trắng. Kiểm tra cấu trúc code bên trong, đường dẫn logic.
* 반복, 분기 등 제어 구조 경로 테스트. (Kiểm tra vòng lặp, rẽ nhánh).

## 128 ~ 129. 화이트박스 테스트 종류 및 검증 기준
* **종류**: 기초 경로 검사, 조건 검사, 루프 검사, 데이터 흐름 검사.
* **검증 기준 (Coverage)**:
  * **문장 (Statement)**: 모든 구문 1번 이상 수행.
  * **분기/결정 (Branch/Decision)**: 조건문 True/False 1번 이상 수행.
  * **조건 (Condition)**: 개별 조건식 True/False 1번 이상.
  * **분기/조건 (Branch/Condition)**: 분기와 조건 모두 만족.

## 130. 블랙박스 테스트 (Black Box Test)
* **개념**: 프로그램 구조 고려 없이 **기능(명세)** 입증 테스트. 테스트 과정 후반부 적용.
  * *Tiếng Việt*: Kiểm thử hộp đen. Chỉ quan tâm Input và Output, không cần biết code bên trong.

## 131. 블랙박스 테스트의 종류
* **동치 분할 검사 (Equivalence Partitioning)**: 타당/타당하지 않은 입력 자료를 균등하게 나누어 검사. (Phân vùng tương đương).
* **경계값 분석 (Boundary Value)**: 경계값에서 오류 확률이 높음을 이용. (Phân tích giá trị biên).
* **원인-효과 그래프 (Cause-Effect)**: 입력-출력 관계 분석. (Đồ thị nguyên nhân - kết quả).
* **오류 예측 (Error Guessing)**: 경험과 감각으로 예측. (Đoán lỗi).
* **비교 검사 (Comparison)**: 여러 버전에 동일 자료 주어 비교.

## 132. 개발 단계에 따른 테스트 (V-모델)
* **단위(Unit) -> 통합(Integration) -> 시스템(System) -> 인수(Acceptance)**.
  * *Tiếng Việt*: Mô hình V. Đơn vị -> Tích hợp -> Hệ thống -> Nghiệm thu.

## 133 ~ 135. 단계별 테스트
* **단위 테스트**: 모듈/컴포넌트 단위 (주로 화이트박스/구조 기반 테스트).
* **통합 테스트**: 모듈 결합 시 테스트. (점진적/비점진적).
* **시스템 테스트**: 실제 환경과 유사한 환경에서 기능/비기능 요구사항 테스트.

## 136. 인수 테스트 (Acceptance Test)
* **알파(Alpha) 테스트**: 통제된 환경(개발자 장소)에서 **사용자가** 테스트 (개발자 앞에서). (Kiểm thử Alpha: Tại cty phát triển).
* **베타(Beta) 테스트**: 실업무 환경에서 통제 없이 **사용자가 직접** 테스트 (필드 테스팅). (Kiểm thử Beta: Người dùng tự test ở môi trường thực tế).

## 137 ~ 139. 하향식 vs 상향식 통합 테스트
* **하향식 (Top-Down)**: 상위 -> 하위 모듈 방향. **스텁(Stub)** 이라는 가짜 하위 모듈 사용. 초기 시스템 구조 파악 가능.
  * *Tiếng Việt*: Tích hợp từ trên xuống. Dùng Stub (mô-đun giả).
* **상향식 (Bottom-Up)**: 하위 -> 상위 모듈 방향. 제어 모듈 역할을 하는 **드라이버(Driver)** 사용.
  * *Tiếng Việt*: Tích hợp từ dưới lên. Dùng Driver (mô-đun điều khiển giả).

## 140. 회귀 테스팅 (Regression Testing)
* 이미 테스트된 프로그램이 '변경'된 후, 새로운 결함(Side effect)이 생겼는지 확인하는 반복 테스트. 변경된 부분을 꼼꼼히 확인.

## 141. 애플리케이션 테스트 프로세스
* 계획 -> 분석/디자인 -> 케이스/시나리오 작성 -> 테스트 수행 -> 결과 평가/리포트 -> 결함 추적/관리.

## 142. 테스트 케이스 (Test Case)
* 입력값, 실행 조건, 기대 결과 명세서. 시스템 설계 단계에서 작성하는 것이 이상적. (Ca kiểm thử).



## 120. Gradle
* **개념**: Groovy 기반 오픈 소스 빌드 자동화 도구. (Công cụ build tự động hóa dựa trên Groovy).
* **특징**: 안드로이드 앱 개발 환경에서 주로 사용. DSL 사용. 태스크(Task) 단위 실행. 빌드 캐시(속도 향상).

## 121. 애플리케이션 테스트의 개념
* **확인 (Validation)**: **사용자** 입장, 요구사항 맞게 구현되었는가. (Are we building the right product?).
* **검증 (Verification)**: **개발자** 입장, 명세서에 맞게 만들어졌는가. (Are we building the product right?).

## 122. 애플리케이션 테스트 관련 용어
* **결함 집중 (Defect Clustering)**: 소수의 특정 모듈에 결함 집중. (Lỗi thường tập trung ở vài mô-đun).
* **파레토 법칙 (Pareto Principle)**: 80% 오류는 20% 모듈에서 발견됨. (Quy tắc 80/20).
* **살충제 패러독스 (Pesticide Paradox)**: 동일 테스트 케이스 반복 시 더 이상 오류 발견 못함. (Nghịch lý thuốc trừ sâu).
* **오류-부재의 궤변 (Absence of Errors Fallacy)**: 결함이 없어도 요구사항을 못 맞추면 품질이 높지 않음. (Nguỵ biện không có lỗi).

## 123. 프로그램 실행 여부에 따른 테스트
* **정적 테스트**: 실행 안 함 (워크스루, 인스펙션 등). 초기 오류 발견. (Kiểm thử tĩnh - Không chạy code).
* **동적 테스트**: 프로그램 실행하여 오류 찾음 (블랙박스, 화이트박스). (Kiểm thử động).

## 124. 테스트 기반(Test Bases)에 따른 테스트
* **명세 기반**: 요구사항 명세서 기반 (동등 분할, 경계값 분석 등).
* **구조 기반**: 논리 흐름 파악 (구문, 결정, 조건 기반 등).
* **경험 기반**: 테스터 경험 기반 (에러 추정, 탐색적 테스팅). 시간 제약 시 효과적.

## 126. 목적에 따른 테스트 (Test by Purpose)
* **회복 (Recovery)**: 고의로 실패 유도 후 정상 복구되는지 확인. (Phục hồi).
* **안전 (Security)**: 불법 침입으로부터 보호 확인. (Bảo mật).
* **강도 (Stress)**: 과부하 시 정상 작동 확인. (Chịu tải).
* **성능 (Performance)**: 응답 시간, 처리량 등 효율성 진단. (Hiệu năng).
* **구조 (Structure)**: 내부 논리적 경로, 소스 코드 복잡도 평가. (Cấu trúc).
* **회귀 (Regression)**: 수정된 코드에 새로운 오류가 없는지 확인. (Hồi quy).
* **병행 (Parallel)**: 변경 전후 소프트웨어 동일 데이터 결과 비교. (Song song).

## 127. 화이트박스 테스트 (White Box Test)
* **개념**: 모듈의 '원시 코드'를 오픈하여 **모든 논리적 경로**를 테스트 (개발자 관점).
  * *Tiếng Việt*: Kiểm thử hộp trắng. Kiểm tra cấu trúc code bên trong, đường dẫn logic.
* 반복, 분기 등 제어 구조 경로 테스트. (Kiểm tra vòng lặp, rẽ nhánh).

## 128 ~ 129. 화이트박스 테스트 종류 및 검증 기준
* **종류**: 기초 경로 검사, 조건 검사, 루프 검사, 데이터 흐름 검사.
* **검증 기준 (Coverage)**:
  * **문장 (Statement)**: 모든 구문 1번 이상 수행.
  * **분기/결정 (Branch/Decision)**: 조건문 True/False 1번 이상 수행.
  * **조건 (Condition)**: 개별 조건식 True/False 1번 이상.
  * **분기/조건 (Branch/Condition)**: 분기와 조건 모두 만족.

## 130. 블랙박스 테스트 (Black Box Test)
* **개념**: 프로그램 구조 고려 없이 **기능(명세)** 입증 테스트. 테스트 과정 후반부 적용.
  * *Tiếng Việt*: Kiểm thử hộp đen. Chỉ quan tâm Input và Output, không cần biết code bên trong.

## 131. 블랙박스 테스트의 종류
* **동치 분할 검사 (Equivalence Partitioning)**: 타당/타당하지 않은 입력 자료를 균등하게 나누어 검사. (Phân vùng tương đương).
* **경계값 분석 (Boundary Value)**: 경계값에서 오류 확률이 높음을 이용. (Phân tích giá trị biên).
* **원인-효과 그래프 (Cause-Effect)**: 입력-출력 관계 분석. (Đồ thị nguyên nhân - kết quả).
* **오류 예측 (Error Guessing)**: 경험과 감각으로 예측. (Đoán lỗi).
* **비교 검사 (Comparison)**: 여러 버전에 동일 자료 주어 비교.

## 132. 개발 단계에 따른 테스트 (V-모델)
* **단위(Unit) -> 통합(Integration) -> 시스템(System) -> 인수(Acceptance)**.
  * *Tiếng Việt*: Mô hình V. Đơn vị -> Tích hợp -> Hệ thống -> Nghiệm thu.

## 133 ~ 135. 단계별 테스트
* **단위 테스트**: 모듈/컴포넌트 단위 (주로 화이트박스/구조 기반 테스트).
* **통합 테스트**: 모듈 결합 시 테스트. (점진적/비점진적).
* **시스템 테스트**: 실제 환경과 유사한 환경에서 기능/비기능 요구사항 테스트.

## 136. 인수 테스트 (Acceptance Test)
* **알파(Alpha) 테스트**: 통제된 환경(개발자 장소)에서 **사용자가** 테스트 (개발자 앞에서). (Kiểm thử Alpha: Tại cty phát triển).
* **베타(Beta) 테스트**: 실업무 환경에서 통제 없이 **사용자가 직접** 테스트 (필드 테스팅). (Kiểm thử Beta: Người dùng tự test ở môi trường thực tế).

## 137 ~ 139. 하향식 vs 상향식 통합 테스트
* **하향식 (Top-Down)**: 상위 -> 하위 모듈 방향. **스텁(Stub)** 이라는 가짜 하위 모듈 사용. 초기 시스템 구조 파악 가능.
  * *Tiếng Việt*: Tích hợp từ trên xuống. Dùng Stub (mô-đun giả).
* **상향식 (Bottom-Up)**: 하위 -> 상위 모듈 방향. 제어 모듈 역할을 하는 **드라이버(Driver)** 사용.
  * *Tiếng Việt*: Tích hợp từ dưới lên. Dùng Driver (mô-đun điều khiển giả).

## 140. 회귀 테스팅 (Regression Testing)
* 이미 테스트된 프로그램이 '변경'된 후, 새로운 결함(Side effect)이 생겼는지 확인하는 반복 테스트. 변경된 부분을 꼼꼼히 확인.

## 141. 애플리케이션 테스트 프로세스
* 계획 -> 분석/디자인 -> 케이스/시나리오 작성 -> 테스트 수행 -> 결과 평가/리포트 -> 결함 추적/관리.

## 142. 테스트 케이스 (Test Case)
* 입력값, 실행 조건, 기대 결과 명세서. 시스템 설계 단계에서 작성하는 것이 이상적. (Ca kiểm thử).



## 120. Gradle
* **개념**: Groovy 기반 오픈 소스 빌드 자동화 도구. (Công cụ build tự động hóa dựa trên Groovy).
* **특징**: 안드로이드 앱 개발 환경에서 주로 사용. DSL 사용. 태스크(Task) 단위 실행. 빌드 캐시(속도 향상).

## 121. 애플리케이션 테스트의 개념
* **확인 (Validation)**: **사용자** 입장, 요구사항 맞게 구현되었는가. (Are we building the right product?).
* **검증 (Verification)**: **개발자** 입장, 명세서에 맞게 만들어졌는가. (Are we building the product right?).

## 122. 애플리케이션 테스트 관련 용어
* **결함 집중 (Defect Clustering)**: 소수의 특정 모듈에 결함 집중. (Lỗi thường tập trung ở vài mô-đun).
* **파레토 법칙 (Pareto Principle)**: 80% 오류는 20% 모듈에서 발견됨. (Quy tắc 80/20).
* **살충제 패러독스 (Pesticide Paradox)**: 동일 테스트 케이스 반복 시 더 이상 오류 발견 못함. (Nghịch lý thuốc trừ sâu).
* **오류-부재의 궤변 (Absence of Errors Fallacy)**: 결함이 없어도 요구사항을 못 맞추면 품질이 높지 않음. (Nguỵ biện không có lỗi).

## 123. 프로그램 실행 여부에 따른 테스트
* **정적 테스트**: 실행 안 함 (워크스루, 인스펙션 등). 초기 오류 발견. (Kiểm thử tĩnh - Không chạy code).
* **동적 테스트**: 프로그램 실행하여 오류 찾음 (블랙박스, 화이트박스). (Kiểm thử động).

## 124. 테스트 기반(Test Bases)에 따른 테스트
* **명세 기반**: 요구사항 명세서 기반 (동등 분할, 경계값 분석 등).
* **구조 기반**: 논리 흐름 파악 (구문, 결정, 조건 기반 등).
* **경험 기반**: 테스터 경험 기반 (에러 추정, 탐색적 테스팅). 시간 제약 시 효과적.

## 126. 목적에 따른 테스트 (Test by Purpose)
* **회복 (Recovery)**: 고의로 실패 유도 후 정상 복구되는지 확인. (Phục hồi).
* **안전 (Security)**: 불법 침입으로부터 보호 확인. (Bảo mật).
* **강도 (Stress)**: 과부하 시 정상 작동 확인. (Chịu tải).
* **성능 (Performance)**: 응답 시간, 처리량 등 효율성 진단. (Hiệu năng).
* **구조 (Structure)**: 내부 논리적 경로, 소스 코드 복잡도 평가. (Cấu trúc).
* **회귀 (Regression)**: 수정된 코드에 새로운 오류가 없는지 확인. (Hồi quy).
* **병행 (Parallel)**: 변경 전후 소프트웨어 동일 데이터 결과 비교. (Song song).

## 127. 화이트박스 테스트 (White Box Test)
* **개념**: 모듈의 '원시 코드'를 오픈하여 **모든 논리적 경로**를 테스트 (개발자 관점).
  * *Tiếng Việt*: Kiểm thử hộp trắng. Kiểm tra cấu trúc code bên trong, đường dẫn logic.
* 반복, 분기 등 제어 구조 경로 테스트. (Kiểm tra vòng lặp, rẽ nhánh).

## 128 ~ 129. 화이트박스 테스트 종류 및 검증 기준
* **종류**: 기초 경로 검사, 조건 검사, 루프 검사, 데이터 흐름 검사.
* **검증 기준 (Coverage)**:
  * **문장 (Statement)**: 모든 구문 1번 이상 수행.
  * **분기/결정 (Branch/Decision)**: 조건문 True/False 1번 이상 수행.
  * **조건 (Condition)**: 개별 조건식 True/False 1번 이상.
  * **분기/조건 (Branch/Condition)**: 분기와 조건 모두 만족.

## 130. 블랙박스 테스트 (Black Box Test)
* **개념**: 프로그램 구조 고려 없이 **기능(명세)** 입증 테스트. 테스트 과정 후반부 적용.
  * *Tiếng Việt*: Kiểm thử hộp đen. Chỉ quan tâm Input và Output, không cần biết code bên trong.

## 131. 블랙박스 테스트의 종류
* **동치 분할 검사 (Equivalence Partitioning)**: 타당/타당하지 않은 입력 자료를 균등하게 나누어 검사. (Phân vùng tương đương).
* **경계값 분석 (Boundary Value)**: 경계값에서 오류 확률이 높음을 이용. (Phân tích giá trị biên).
* **원인-효과 그래프 (Cause-Effect)**: 입력-출력 관계 분석. (Đồ thị nguyên nhân - kết quả).
* **오류 예측 (Error Guessing)**: 경험과 감각으로 예측. (Đoán lỗi).
* **비교 검사 (Comparison)**: 여러 버전에 동일 자료 주어 비교.

## 132. 개발 단계에 따른 테스트 (V-모델)
* **단위(Unit) -> 통합(Integration) -> 시스템(System) -> 인수(Acceptance)**.
  * *Tiếng Việt*: Mô hình V. Đơn vị -> Tích hợp -> Hệ thống -> Nghiệm thu.

## 133 ~ 135. 단계별 테스트
* **단위 테스트**: 모듈/컴포넌트 단위 (주로 화이트박스/구조 기반 테스트).
* **통합 테스트**: 모듈 결합 시 테스트. (점진적/비점진적).
* **시스템 테스트**: 실제 환경과 유사한 환경에서 기능/비기능 요구사항 테스트.

## 136. 인수 테스트 (Acceptance Test)
* **알파(Alpha) 테스트**: 통제된 환경(개발자 장소)에서 **사용자가** 테스트 (개발자 앞에서). (Kiểm thử Alpha: Tại cty phát triển).
* **베타(Beta) 테스트**: 실업무 환경에서 통제 없이 **사용자가 직접** 테스트 (필드 테스팅). (Kiểm thử Beta: Người dùng tự test ở môi trường thực tế).

## 137 ~ 139. 하향식 vs 상향식 통합 테스트
* **하향식 (Top-Down)**: 상위 -> 하위 모듈 방향. **스텁(Stub)** 이라는 가짜 하위 모듈 사용. 초기 시스템 구조 파악 가능.
  * *Tiếng Việt*: Tích hợp từ trên xuống. Dùng Stub (mô-đun giả).
* **상향식 (Bottom-Up)**: 하위 -> 상위 모듈 방향. 제어 모듈 역할을 하는 **드라이버(Driver)** 사용.
  * *Tiếng Việt*: Tích hợp từ dưới lên. Dùng Driver (mô-đun điều khiển giả).

## 140. 회귀 테스팅 (Regression Testing)
* 이미 테스트된 프로그램이 '변경'된 후, 새로운 결함(Side effect)이 생겼는지 확인하는 반복 테스트. 변경된 부분을 꼼꼼히 확인.

## 141. 애플리케이션 테스트 프로세스
* 계획 -> 분석/디자인 -> 케이스/시나리오 작성 -> 테스트 수행 -> 결과 평가/리포트 -> 결함 추적/관리.

## 142. 테스트 케이스 (Test Case)
* 입력값, 실행 조건, 기대 결과 명세서. 시스템 설계 단계에서 작성하는 것이 이상적. (Ca kiểm thử).




# 3과목: 데이터베이스 구축 / 소프트웨어 테스트 및 인터페이스 통합

## 핵심 144: 테스트 오라클 (Test Oracle)
테스트 결과가 올바른지 판단하기 위해 사전에 정의된 참 값을 대입하여 비교하는 기법 및 활동입니다.
- **Vietnamese**: Kỹ thuật và hoạt động so sánh kết quả kiểm thử với các giá trị chuẩn (true values) được định nghĩa từ trước để đánh giá xem kết quả kiểm thử có chính xác hay không.
- **Example**: 
  - (KR) 계산기 프로그램에서 '2+2'의 예상 결과인 '4'를 미리 정의해 두고 실제 결과와 비교합니다.
  - (VN) Trong chương trình máy tính, định nghĩa trước kết quả mong đợi của '2+2' là '4' và so sánh với kết quả thực tế.
- 💡 **Mẹo ghi nhớ (Mnemonics)**: Oracle (오라클) giống như nhà tiên tri, luôn biết trước "kết quả đúng" để chúng ta so sánh.

## 핵심 145: 테스트 오라클의 종류 (Types of Test Oracle)
1. **참 (True) 오라클**: 모든 테스트 케이스의 입력 값에 대해 기대하는 결과를 제공. 모든 오류 검출 가능. (Oracle thực - cung cấp kết quả mong đợi cho mọi input).
2. **샘플링 (Sampling) 오라클**: 특정한 몇몇 테스트 케이스의 입력 값들에 대해서만 기대하는 결과를 제공. (Oracle lấy mẫu - chỉ cung cấp kết quả cho một số input nhất định).
3. **추정 (Heuristic) 오라클**: 샘플링 오라클을 개선하여, 특정 입력값은 결과를 제공하고 나머지는 추정(Heuristic)으로 처리. (Oracle ước lượng - kết hợp lấy mẫu và ước lượng các kết quả còn lại).
4. **일관성 검사 (Consistent) 오라클**: 애플리케이션 변경 시, 변경 전후의 결과 값이 동일한지 확인. (Oracle kiểm tra tính nhất quán - kiểm tra sự giống nhau trước và sau khi thay đổi).
- 💡 **Mẹo ghi nhớ:** Thật Mẫu Ước Nhất (Thật - Lấy mẫu - Ước lượng - Nhất quán).

## 핵심 146: 테스트 자동화 도구 (Test Automation Tools)
사람이 반복적으로 수행하던 테스트 절차를 스크립트 형태로 구현하여 자동화하는 도구.
(Công cụ tự động hóa các quy trình kiểm thử lặp đi lặp lại bằng các script.)
- **정적 분석 도구 (Static Analysis Tools)**: 프로그램을 실행하지 않고 소스 코드를 분석. (Phân tích tĩnh: Không chạy chương trình, chỉ phân tích source code).
- **테스트 케이스 생성 도구 (Test Case Generation Tools)**: 자료 흐름도, 기능 테스트, 랜덤 테스트 등 테스트 케이스를 자동 생성. (Tự động tạo test case).
- **테스트 실행 도구 (Test Execution Tools)**: 스크립트 언어를 사용하여 테스트를 실행 (데이터 주도, 키워드 주도 방식). (Chạy test bằng script).
- **성능 테스트 도구 (Performance Test Tools)**: 가상의 사용자를 만들어 처리량, 응답 시간 등을 테스트. (Kiểm thử hiệu suất).
- **테스트 통제 도구 (Test Control Tools)**: 테스트 계획/관리, 결함 관리 등을 수행. (Kiểm soát, quản lý test và lỗi).
- **테스트 하네스 도구 (Test Harness Tools)**: 테스트 환경을 시뮬레이션하여 컴포넌트/모듈 테스트를 지원. (Môi trường test harness mô phỏng môi trường chạy).

## 핵심 147: 테스트 하네스(Test Harness)의 구성 요소
- **테스트 드라이버 (Test Driver)**: 하위 모듈을 호출하고 파라미터를 전달 (상향식). (Driver: gọi module con, truyền tham số).
- **테스트 스텁 (Test Stub)**: 제어 모듈이 호출하는 타 모듈의 기능을 단순히 수행하는 가짜 모듈 (하향식). (Stub: module giả lập các module bị gọi).
- **테스트 슈트 (Test Suites)**: 테스트 케이스의 집합. (Tập hợp các test case).
- **테스트 케이스 (Test Case)**: 입력 값, 실행 조건, 기대 결과 명세서. (Test case: điều kiện đầu vào, kết quả mong đợi).
- **테스트 스크립트 (Test Script)**: 테스트 실행 절차 명세서. (Kịch bản chạy test).
- **목 오브젝트 (Mock Object)**: 예정된 행위를 수행하는 가짜 객체. (Mock Object: đối tượng giả mạo trả về kết quả định trước).
- 💡 **Mẹo ghi nhớ:** D-S-S-C-S-M (Driver, Stub, Suite, Case, Script, Mock).

## 핵심 148: 결함 (Fault)
소프트웨어가 설계된 것과 다르게 동작하거나 다른 결과가 발생하는 것. (Lỗi/Khuyết tật: Phần mềm hoạt động hoặc cho ra kết quả khác với thiết kế ban đầu, kể cả việc không đáp ứng yêu cầu nghiệp vụ).

## 핵심 149: 애플리케이션 성능 분석 (Application Performance Analysis)
- **처리량 (Throughput)**: 일정 시간 내에 처리하는 일의 양. (Thông lượng: khối lượng công việc xử lý trong một thời gian).
- **응답 시간 (Response Time)**: 요청을 전달한 시간부터 응답이 도착할 때까지의 시간. (Thời gian phản hồi: Từ lúc gửi yêu cầu đến khi nhận phản hồi).
- **경과 시간 (Turn Around Time)**: 작업을 의뢰한 시간부터 처리가 완료될 때까지의 시간. (Thời gian hoàn thành: Từ lúc giao việc đến khi hoàn thành toàn bộ).
- **자원 사용률 (Resource Usage)**: CPU, 메모리 등의 자원 사용률. (Tỷ lệ sử dụng tài nguyên CPU, RAM...).

## 핵심 150: 빅오 표기법 (Big-O Notation)
알고리즘의 최악의 실행 시간을 표기하는 방법. (Ký hiệu Big-O: Biểu diễn thời gian chạy tệ nhất (worst-case) của thuật toán).
- **O(1)**: 입력값 관계없이 일정. (Hằng số - vd: Push/Pop trong Stack).
- **O(log2n)**: 단계가 조건에 의해 감소. (Logarit - vd: Tìm kiếm nhị phân).
- **O(n)**: 입력값과 1:1 비례. (Tuyến tính - vd: vòng lặp for cơ bản).
- **O(nlog2n)**: vd: 힙 정렬, 병합 정렬.
- **O(n²)**: 제곱 비례. (Bậc hai - vd: Sắp xếp chèn, nổi bọt, chọn).
- **O(2^n)**: 2의 제곱수. (Mũ - vd: Dãy Fibonacci).

## 핵심 151: 순환 복잡도 (Cyclomatic Complexity)
프로그램의 논리적 복잡도를 측정하는 척도. (Độ phức tạp Cyclomatic: đo lường độ phức tạp logic của chương trình dựa trên đồ thị luồng điều khiển).
- **계산법**: V(G) = E - N + 2 (E: 간선/화살표 수, N: 노드 수). (Công thức: Số cạnh - Số node + 2).

## 핵심 152: 소스 코드 최적화 (Source Code Optimization)
나쁜 코드(Bad Code)를 배제하고 클린 코드(Clean Code)로 작성하는 것.
- **클린 코드 (Clean Code)**: 이해하기 쉽고 명료한 코드. (Code sạch, dễ hiểu, dễ bảo trì).
- **스파게티 코드 (Spaghetti Code)**: 로직이 복잡하게 얽힌 코드. (Code rối rắm như mì spaghetti).
- **외계인 코드 (Alien Code)**: 오래되거나 문서가 없어 유지보수가 어려운 코드. (Code từ "người ngoài hành tinh", quá cũ và thiếu tài liệu).
- **작성 원칙**: 가독성 (Dễ đọc), 단순성 (Đơn giản), 의존성 배제 (Loại bỏ phụ thuộc), 중복성 최소화 (Giảm thiểu lặp lại), 추상화 (Trừu tượng hóa).

## 핵심 153: 소스 코드 품질 분석 도구
- **정적 분석 도구 (Static)**: 실행하지 않고 코딩 표준, 결함 분석 (pmd, cppcheck, SonarQube). (Không chạy code).
- **동적 분석 도구 (Dynamic)**: 실행하여 메모리 누수, 스레드 결함 분석 (Avalanche, Valgrind). (Chạy code để test rò rỉ bộ nhớ).

## 핵심 154, 155: EAI & ESB
- **EAI (Enterprise Application Integration)**: 기업 내 애플리케이션들을 연계/통합하는 솔루션. (Giải pháp tích hợp các ứng dụng trong doanh nghiệp).
  - 유형: Point-to-Point (1:1), Hub & Spoke (Trung tâm Hub), Message Bus (Qua Middleware Bus), Hybrid (Hỗn hợp).
- **ESB (Enterprise Service Bus)**: 애플리케이션 보다는 서비스 중심의 통합 (표준 기반 인터페이스). 결합도를 약하게 유지. (Tích hợp dựa trên Dịch vụ, kết nối lỏng lẻo Loosely Coupled).

## 핵심 156, 157, 158: 데이터 형식 및 통신 기술
- **JSON (JavaScript Object Notation)**: 속성-값 쌍(Attribute-Value)으로 이루어진 개방형 표준 포맷. AJAX에서 XML 대체. (Định dạng dữ liệu cặp key-value, nhẹ hơn XML).
- **XML (eXtensible Markup Language)**: 다목적 마크업 언어. 태그를 사용자 정의 가능. (Ngôn ngữ đánh dấu mở rộng, tự định nghĩa tag).
- **AJAX (Asynchronous JavaScript and XML)**: 비동기 통신 기술로 웹 페이지 전체 새로고침 없이 상호 작용 가능. (Công nghệ web giao tiếp bất đồng bộ, không cần reload cả trang).

## 핵심 159, 160: 인터페이스 보안 및 무결성
- **보안 영역**: 네트워크 (IPSec, SSL 적용), 애플리케이션 (코드 보안 취약점 보완), 데이터베이스 (접근 권한, 트리거 보안).
- **무결성 검사 도구 (Integrity Checker)**: 시스템 파일의 변경 유무를 확인. (Công cụ kiểm tra xem file hệ thống có bị thay đổi/hacker chỉnh sửa không). 예: Tripwire, AIDE.

## 핵심 161, 162: 검증 및 성능 관리
- **인터페이스 검증 도구**: xUnit (단위 테스트), STAF (분산 환경), FitNesse (웹 기반), Selenium (웹 브라우저 테스트).
- **APM (Application Performance Management)**: 애플리케이션 성능 관리/모니터링. 리소스 방식 (Nagios)과 엔드투엔드 방식 (제니퍼). (Quản lý và giám sát hiệu suất ứng dụng).

## 핵심 163: 데이터베이스 설계 순서 (Database Design Process)
1. **요구 조건 분석**: 요구 조건 명세서 작성. (Phân tích yêu cầu).
2. **개념적 설계**: E-R 모델, 개념 스키마. (Thiết kế khái niệm: vẽ E-R, Schema khái niệm).
3. **논리적 설계**: 목표 DBMS에 맞는 논리 스키마 설계, 정규화. (Thiết kế logic: chuẩn hóa, chuyển sang mô hình quan hệ).
4. **물리적 설계**: 물리적 구조 변환 (인덱스, 파티션 등). (Thiết kế vật lý: tạo cấu trúc lưu trữ thực tế).
5. **구현**: DDL로 데이터베이스 생성. (Triển khai: viết DDL tạo DB).
- 💡 **Mẹo ghi nhớ:** Yêu Khái Logic Vật Triển (Yêu cầu, Khái niệm, Logic, Vật lý, Triển khai).


## 핵심 164, 165, 166: 데이터베이스 설계 상세 단계
- **개념적 설계 (정보 모델링, Conceptual Design)**: 요구 분석 명세를 DBMS에 독립적인 E-R 다이어그램으로 작성. 트랜잭션 모델링 병행. (Thiết kế khái niệm: Không phụ thuộc DBMS, vẽ E-R, mô hình hóa giao dịch).
- **논리적 설계 (데이터 모델링, Logical Design)**: 물리적 저장장치에 맞게 특정 DBMS가 지원하는 논리적 자료 구조(테이블 등)로 변환(mapping). 트랜잭션 인터페이스 설계. (Thiết kế logic: Ánh xạ sang cấu trúc của DBMS cụ thể, thiết kế table).
- **물리적 설계 (데이터 구조화, Physical Design)**: 디스크 등 물리적 저장장치에 저장할 물리적 구조로 변환. 저장 레코드 양식, 순서, 액세스 경로 결정. (Thiết kế vật lý: Định dạng lưu trữ, tạo index, đường dẫn truy cập trên ổ cứng).

## 핵심 167: 데이터 모델 (Data Model)
- **구성 요소 (Components)**: 개체 (Entity - Thực thể), 속성 (Attribute - Thuộc tính), 관계 (Relationship - Mối quan hệ).
- **표시 요소 (Elements)**: 구조 (Structure - Cấu trúc), 연산 (Operation - Các thao tác xử lý), 제약 조건 (Constraint - Ràng buộc dữ liệu).

## 핵심 168, 169: E-R 모델의 개요 및 다이어그램 기호
- 1976년 피터 첸(Peter Chen) 제안. 개체, 속성, 관계로 개념적 표현. (Mô hình Thực thể - Liên kết).
- **기호 (Symbols)**:
  - **사각형 (Rectangle)**: 개체 타입 (Thực thể).
  - **마름모 (Diamond)**: 관계 타입 (Quan hệ).
  - **타원 (Ellipse)**: 속성 (Thuộc tính).
  - **이중 타원 (Double Ellipse)**: 다중값 속성 (Thuộc tính đa trị).
  - **밑줄 타원 (Underlined Ellipse)**: 기본키 속성 (Thuộc tính khóa chính).
  - **선 (Line)**: 연결 (Kết nối).

## 핵심 170, 171, 172: 관계형 데이터 모델 및 릴레이션 구조
- **관계형 데이터 모델 (Relational Data Model)**: 2차원 표(Table) 형태. 기본키와 외래키로 관계 표현. (Mô hình dữ liệu quan hệ dùng bảng).
- **릴레이션 구조 (Relation Structure)**:
  - **튜플 (Tuple)**: 표의 행(Row), 레코드(Record). 튜플의 수 = **카디널리티 (Cardinality)** 또는 기수, 대응수. (Tuple: hàng/record. Số tuple = Cardinality).
  - **속성 (Attribute)**: 표의 열(Column), 필드(Field). 속성의 수 = **디그리 (Degree)** 또는 차수. (Attribute: cột/trường. Số thuộc tính = Degree).
  - **도메인 (Domain)**: 하나의 속성이 가질 수 있는 원자값들의 집합. (Tập hợp các giá trị hợp lệ của một thuộc tính).
- **릴레이션의 특징 (Features)**: 튜플은 모두 상이함(중복 불가). 튜플 간 순서 없음. 시간에 따라 변함(동적). 속성 명은 유일, 속성 값은 중복 가능. 원자값만 저장. (Đặc điểm: Không có tuple trùng lặp, không phân biệt thứ tự tuple, thay đổi theo thời gian, chỉ chứa giá trị nguyên tử).
- 💡 **Mẹo ghi nhớ:** Tuple-Cardinality (Bản ghi - Số lượng), Thuộc tính-Degree (Cột - Bậc).

## 핵심 173: 키(Key)
- **후보키 (Candidate Key)**: 튜플을 유일하게 식별하는 속성. **유일성(Uniqueness)**과 **최소성(Minimality)** 만족. (Khóa ứng viên: đảm bảo tính duy nhất và tính tối thiểu).
- **기본키 (Primary Key)**: 후보키 중 선택된 주키. 중복값 및 NULL 값 불가. (Khóa chính: Không trùng, không được NULL).
- **대체키 (Alternate Key)**: 후보키 중 기본키를 제외한 나머지. 보조키. (Khóa thay thế).
- **슈퍼키 (Super Key)**: 유일성은 만족하지만 최소성은 만족하지 못하는 속성의 집합. (Siêu khóa: Duy nhất nhưng không tối thiểu, vd: Học bổng + Tên).
- **외래키 (Foreign Key)**: 다른 릴레이션의 기본키를 참조하는 속성. (Khóa ngoại).

## 핵심 174: 무결성 (Integrity)
- **개체 무결성 (Entity Integrity)**: 기본키는 NULL 값이나 중복값을 가질 수 없다. (Khóa chính không NULL, không trùng).
- **도메인 무결성 (Domain Integrity)**: 속성 값은 정의된 도메인에 속해야 한다. (Giá trị phải thuộc miền cho phép).
- **참조 무결성 (Referential Integrity)**: 외래키 값은 NULL이거나 참조 릴레이션의 기본키 값과 동일해야 한다. (Khóa ngoại phải khớp với khóa chính của bảng tham chiếu hoặc NULL).
- **사용자 정의 무결성 (User-Defined)**: 사용자가 정의한 제약조건 만족. (Ràng buộc do người dùng định nghĩa).

## 핵심 175, 176, 177: 관계대수 (Relational Algebra)
- 릴레이션을 처리하는 **절차적 언어 (Procedural Language)**. 연산의 순서를 명시함. (Đại số quan hệ: ngôn ngữ thủ tục, chỉ định rõ CÁCH lấy dữ liệu).
- **순수 관계 연산자 (Pure Relational Operators)**:
  - **Select (σ, 시그마)**: 수평 연산 (행/튜플 추출). (Chọn các hàng thỏa mãn điều kiện).
  - **Project (π, 파이)**: 수직 연산 (열/속성 추출). (Chiếu các cột được chỉ định).
  - **Join (⋈)**: 두 릴레이션을 공통 속성 기준으로 합침. (Kết nối 2 bảng).
  - **Division (÷)**: S의 속성값을 모두 가진 R의 튜플 반환. (Phép chia).
- **일반 집합 연산자 (Set Operators)**:
  - 합집합 (UNION, ∪), 교집합 (INTERSECTION, ∩), 차집합 (DIFFERENCE, -), 교차곱 (CARTESIAN PRODUCT, ×).

## 핵심 178: 관계해석 (Relational Calculus)
- **비절차적 언어 (Non-procedural Language)**. 원하는 정보가 무엇인지(What)만 정의함. E.F. Codd 제안. (Giải tích quan hệ: ngôn ngữ phi thủ tục).
- 관계대수와 기능 및 능력 면에서 동등함.
- 논리 기호: **∀ (전칭 정량자, For All)**, **∃ (존재 정량자, There Exists)**.

## 핵심 179, 180: 정규화 (Normalization)
- **정규화의 개요**: 잘못 설계된 스키마를 종속성 이론을 이용해 더 작은 속성 세트로 쪼개는(분해하는) 과정. 논리적 설계 단계에서 수행. (Chuẩn hóa: Phân rã bảng lớn thành các bảng nhỏ hơn dựa trên sự phụ thuộc hàm, thực hiện ở giai đoạn thiết kế logic).
- **목적**: 데이터 중복 배제, 이상(Anomaly) 발생 방지, 무결성 유지, 자료 저장 공간 최소화. (Mục đích: Loại bỏ trùng lặp, tránh dị thường, duy trì tính toàn vẹn).


## 핵심 181: 이상 (Anomaly)의 개념 및 종류
정규화를 거치지 않아 데이터가 불필요하게 중복되어 발생하는 문제. (Dị thường dữ liệu do chưa chuẩn hóa).
- **삽입 이상 (Insertion Anomaly)**: 데이터 삽입 시 의도치 않은 값들도 함께 삽입해야 하는 현상. (Lỗi khi thêm: bắt buộc phải thêm dữ liệu không liên quan).
- **삭제 이상 (Deletion Anomaly)**: 한 튜플 삭제 시 의도치 않은 값들까지 연쇄 삭제되는 현상. (Lỗi khi xóa: xóa một thông tin làm mất luôn thông tin khác).
- **갱신 이상 (Update Anomaly)**: 속성값 갱신 시 일부 튜플만 갱신되어 정보 모순이 생기는 현상. (Lỗi khi cập nhật: dữ liệu không đồng bộ, gây mâu thuẫn).

## 핵심 182, 183: 정규화 과정과 함수적 종속
- **함수적 종속 (Functional Dependency)**: X가 결정되면 Y가 결정되는 관계 (X -> Y). (Phụ thuộc hàm).
- **이행적 종속 (Transitive Dependency)**: A -> B, B -> C 이면 A -> C 인 관계. (Phụ thuộc bắc cầu).
- **정규화 단계 (Normalization Steps)**:
  - 1NF: 도메인이 원자값 (Miền giá trị nguyên tử).
  - 2NF: 부분적 함수 종속 제거 (Loại bỏ phụ thuộc hàm từng phần).
  - 3NF: 이행적 함수 종속 제거 (Loại bỏ phụ thuộc hàm bắc cầu).
  - BCNF: 결정자이면서 후보키가 아닌 것 제거 (Loại bỏ các khóa quyết định không phải là khóa ứng viên).
  - 4NF: 다치 종속 제거 (Loại bỏ phụ thuộc đa trị).
  - 5NF: 조인 종속성 이용 (Sử dụng phụ thuộc kết nối).
- 💡 **Mẹo ghi nhớ:** Miền Phần Cầu Khóa Đa Nối (Miền giá trị - Một phần - Bắc cầu - Khóa quyết định - Đa trị - Nối).

## 핵심 184, 185: 반정규화 (Denormalization)
- **개념**: 시스템 성능 향상, 운영 편의성을 위해 의도적으로 정규화 원칙을 위배하여 데이터를 통합/중복/분리하는 과정. (Khử chuẩn hóa: Cố tình phá vỡ chuẩn hóa để tăng hiệu suất truy vấn).
- **방법**: 테이블 통합, 테이블 분할(수직/수평), 중복 테이블 추가, 중복 속성 추가. (Gộp bảng, chia bảng, thêm bảng trùng, thêm thuộc tính trùng).

## 핵심 186: 시스템 카탈로그 (System Catalog)
- DBMS에서 지원하는 모든 객체(테이블, 뷰, 인덱스 등)에 대한 정의나 명세를 저장하는 시스템 테이블 (메타 데이터). 데이터 사전(Data Dictionary)이라고도 함. (Danh mục hệ thống: Lưu trữ siêu dữ liệu meta-data về các cấu trúc DB).
- 사용자는 SQL로 **검색만 가능**하며 갱신(INSERT, UPDATE 등)은 **불가**. (DBMS tự động cập nhật, người dùng chỉ được đọc).

## 핵심 187, 188, 189: 트랜잭션 (Transaction) 및 ACID 특성
- **개념**: 데이터베이스 상태를 변환시키는 논리적 작업 단위. (Giao dịch: Đơn vị công việc logic nhỏ nhất).
- **상태**: 활동 (Active) -> 부분 완료 (Partially Committed) -> 완료 (Committed) 또는 실패 (Failed) -> 철회 (Aborted/Rollback).
- **특성 (ACID)**:
  - **Atomicity (원자성)**: 모두 반영되거나(Commit) 전혀 반영되지 않아야 함(Rollback). (Nguyên tử: All or Nothing).
  - **Consistency (일관성)**: 실행 성공 시 항상 일관된 상태 유지. (Nhất quán: Trước và sau giao dịch dữ liệu phải hợp lệ).
  - **Isolation (독립성/격리성/순차성)**: 실행 중 다른 트랜잭션이 끼어들 수 없음. (Độc lập: Không bị ảnh hưởng bởi giao dịch khác đang chạy).
  - **Durability (영속성/지속성)**: 성공한 결과는 시스템 고장 시에도 영구 반영. (Bền vững: Dữ liệu đã lưu sẽ không mất).

## 핵심 190: CRUD 분석
데이터베이스 테이블에 변화를 주는 생성(Create), 읽기(Read), 갱신(Update), 삭제(Delete) 연산의 발생 횟수/주기를 분석하는 매트릭스. (Phân tích các thao tác Thêm, Đọc, Sửa, Xóa).

## 핵심 191, 192: 인덱스 (Index)
- **개념**: 레코드에 빠르게 접근하기 위한 <키 값, 포인터> 구조. 검색 속도를 높이지만 삽입/삭제 시 부하 발생. (Chỉ mục: Giống mục lục sách, giúp tìm kiếm nhanh).
- **종류**: 트리 기반 (B+ 트리), 비트맵, 함수 기반, 비트맵 조인, 도메인 인덱스.

## 핵심 193: 뷰 (View)
- **개념**: 하나 이상의 기본 테이블에서 유도된 **가상 테이블**. (View: Bảng ảo).
- **특징**: 물리적으로 존재하지 않음. 논리적 데이터 독립성 제공. 보안 측면에서 유리. 삽입/삭제/갱신 연산에 제약이 있음. 인덱스 불가. 정의 변경 불가.

## 핵심 194: 파티션 (Partition)
- **개념**: 대용량 테이블/인덱스를 작은 논리적 단위로 분할. (Phân vùng dữ liệu).
- **종류**: 범위(Range - vd: Tháng, Quý), 해시(Hash - băm ngẫu nhiên đều), 조합(Composite), 목록(List), 라운드 로빈(Round Robin).

## 핵심 195, 196, 197: 분산 데이터베이스 (Distributed Database)
- **개념**: 물리적으로 분산되어 있으나 논리적으로 하나의 시스템인 DB. (DB phân tán).
- **목표 (4대 투명성)**: 위치(Location), 중복(Replication), 병행(Concurrency), 장애(Failure) 투명성. (Mục tiêu: Trong suốt về vị trí, trùng lặp, đồng thời, lỗi - người dùng không cần biết chi tiết bên dưới).
- **장단점**: 신뢰성, 확장성 좋음. 설계 복잡, 비용 증가.

## 핵심 198: 암호화 (Encryption)
- **개인키 (Private/Secret Key)**: 대칭키 (Symmetric). 암호화와 복호화 키가 동일. (Khóa đối xứng: mã hóa và giải mã dùng chung 1 khóa, vd: DES).
- **공개키 (Public Key)**: 비대칭키 (Asymmetric). 암호화는 공개키, 복호화는 비밀키. (Khóa bất đối xứng: mã hóa bằng khóa công khai, giải mã bằng khóa bí mật, vd: RSA).

## 핵심 199: 접근통제 기술 (Access Control)
- **DAC (임의 접근통제, Discretionary)**: 데이터 소유자가 사용자 신원에 따라 권한 부여 (GRANT/REVOKE). (Kiểm soát tùy ý: Chủ sở hữu cấp quyền).
- **MAC (강제 접근통제, Mandatory)**: 시스템이 보안 등급에 따라 권한 부여. (Kiểm soát bắt buộc: Dựa trên cấp độ bảo mật của dữ liệu và người dùng).
- **RBAC (역할기반 접근통제, Role-Based)**: 중앙관리자가 역할에 따라 권한 부여. (Kiểm soát theo vai trò).


## 핵심 200: 보안 모델 (Security Models)
- **벨 라파듈라 모델 (Bell-LaPadula Model)**: 기밀성(Confidentiality) 보장. 군대 보안처럼 등급에 따라 읽기/쓰기 권한 제한. (Mô hình bảo mật tập trung vào tính bảo mật, cấp dưới không được đọc tài liệu cấp trên, cấp trên không được viết xuống cấp dưới).
- **비바 무결성 모델 (Biba Integrity Model)**: 무결성(Integrity) 보장. 벨 라파듈라 보완. 비인가자의 데이터 변형 방지. (Tập trung vào tính toàn vẹn dữ liệu).
- **클락-윌슨 모델 (Clark-Wilson Model)**: 상업용 무결성 모델. (Mô hình thương mại).
- **만리장성 모델 (Chinese Wall Model)**: 이해 충돌 관계에 있는 객체 간 정보 접근 통제. (Mô hình Vạn Lý Trường Thành: Ngăn chặn xung đột lợi ích).

## 핵심 201, 202, 203: 스토리지(Storage) 시스템
- **DAS (Direct Attached Storage)**: 서버에 전용 케이블로 직접 연결 (예: 외장하드). 빠르고 저렴하지만 공유 불가. (Kết nối trực tiếp, nhanh, rẻ nhưng không chia sẻ được).
- **NAS (Network Attached Storage)**: 네트워크(Ethernet)를 통해 연결. 파일 공유 가능, 유연성 우수. 접속 증가 시 성능 저하 가능. (Kết nối qua mạng cục bộ LAN, cho phép chia sẻ file).
- **SAN (Storage Area Network)**: 광 채널(FC) 스위치를 이용한 스토리지 전용 네트워크 구성. DAS의 속도 + NAS의 공유 장점. 비용이 비쌈. (Mạng lưu trữ chuyên dụng dùng cáp quang, nhanh, dễ mở rộng nhưng đắt tiền).

## 핵심 204, 205, 206: SQL 명령어 분류
- **DDL (데이터 정의어, Data Definition Language)**: 구조를 정의/변경/삭제. (Ngôn ngữ định nghĩa dữ liệu).
  - CREATE (생성), ALTER (변경), DROP (삭제).
- **DML (데이터 조작어, Data Manipulation Language)**: 데이터를 실질적으로 처리. (Ngôn ngữ thao tác dữ liệu).
  - SELECT (검색), INSERT (삽입), UPDATE (수정/갱신), DELETE (삭제).
- **DCL (데이터 제어어, Data Control Language)**: 보안, 무결성, 회복, 병행 제어, 권한. (Ngôn ngữ kiểm soát dữ liệu).
  - GRANT (권한 부여), REVOKE (권한 취소), COMMIT (저장/완료), ROLLBACK (복구).

## 핵심 207, 208, 209: DDL 상세 (CREATE, ALTER, DROP)
- **CREATE TABLE**: 테이블 생성. 제약조건(PRIMARY KEY, FOREIGN KEY 등) 설정 가능.
- **ALTER TABLE**: 
  - `ADD`: 열(속성) 추가. (Thêm cột).
  - `ALTER`: 열의 기본값(Default) 변경. (Đổi giá trị mặc định).
  - `DROP COLUMN`: 열 삭제. (Xóa cột).
- **DROP**: 개체 삭제.
  - `CASCADE`: 연관된(참조하는) 다른 개체도 함께 삭제. (Xóa theo dây chuyền).
  - `RESTRICT`: 참조 중이면 삭제를 취소. (Cấm xóa nếu đang bị tham chiếu).

## 핵심 210, 211: DCL 권한 제어 (GRANT, REVOKE)
- **GRANT**: 권한 부여. `WITH GRANT OPTION`은 부여받은 권한을 남에게 다시 줄 수 있게 함. (Cấp quyền).
- **REVOKE**: 권한 취소. `CASCADE`는 연쇄 취소. (Thu hồi quyền).
- **Example (KR/VN)**: 
  - `GRANT ALL ON 고객 TO NABI WITH GRANT OPTION;` (NABI에게 고객 테이블의 모든 권한과 부여 권한까지 줌 / Cấp mọi quyền trên bảng Khách Hàng cho NABI và cho phép NABI cấp quyền đó cho người khác).

## 핵심 212, 213: DCL 트랜잭션 제어 (COMMIT, ROLLBACK)
- **COMMIT**: 트랜잭션이 성공적으로 끝나면 변경 내용을 DB에 영구 반영 (일관성 유지). (Lưu thay đổi vĩnh viễn vào DB sau khi giao dịch thành công).
- **ROLLBACK**: 트랜잭션 실패 또는 진행 중 취소 시, 변경 내용을 취소하고 이전 상태로 복구. (Hoàn tác các thay đổi nếu giao dịch thất bại).

## 핵심 214, 215: DML 기본 문법 (INSERT, DELETE)
- **INSERT INTO**: 새로운 튜플(행) 삽입. (Thêm dòng mới).
  - 형식: `INSERT INTO 테이블명(속성명) VALUES (데이터);`
- **DELETE FROM**: 조건에 맞는 튜플 삭제. (Xóa dòng).
  - 형식: `DELETE FROM 테이블명 WHERE 조건;` (WHERE를 생략하면 모든 튜플이 삭제되나 테이블 구조는 남음).


## 핵심 216: DML 갱신문 (UPDATE)
- **UPDATE ~ SET**: 테이블에서 튜플의 내용을 변경. (Cập nhật dữ liệu).
  - 형식: `UPDATE 테이블명 SET 속성명=값 WHERE 조건;` (WHERE 생략 시 모든 튜플 변경).
  - Example (KR/VN): `UPDATE 사원 SET 기본급 = 기본급 + 5 WHERE 이름 = '황진이';` (황진이의 기본급 5만 원 인상 / Tăng lương cơ bản của Hwang Jin-yi lên 50,000 won).

## 핵심 217, 218, 221: DML 검색문 (SELECT) 및 구조
- **SELECT 절**: 
  - `DISTINCT`: 중복 튜플 제거 후 한 번만 검색. (Loại bỏ các dòng trùng lặp).
  - `AS`: 출력될 때 보여줄 제목(별칭) 지정. (Đặt bí danh cho cột).
- **FROM 절**: 검색 대상 테이블.
- **WHERE 절**: 검색 조건.
- **GROUP BY 절**: 특정 속성을 기준으로 그룹화. 그룹 함수와 함께 사용. (Gom nhóm dữ liệu).
- **HAVING 절**: GROUP BY로 그룹화된 결과에 대한 조건. (Điều kiện lọc sau khi gom nhóm).
- **ORDER BY 절**: 정렬. `ASC`(오름차순-기본값), `DESC`(내림차순). (Sắp xếp tăng/giảm dần).
- **WINDOW 함수**: `PARTITION BY`(적용 범위 지정)와 `ORDER BY`를 이용해 GROUP BY 없이 집계. (Hàm cửa sổ).

## 핵심 219: 조건 연산자 및 우선순위
- **비교 연산자**: `=`, `<>`(같지 않다), `>`, `<`, `>=`, `<=`.
- **논리 연산자**: `NOT`, `AND`, `OR`.
- **LIKE 연산자**: 패턴 검색. (Tìm kiếm theo mẫu).
  - `%`: 모든 문자 여러 개 (0개 이상). (Đại diện chuỗi ký tự bất kỳ).
  - `_`: 문자 딱 1개. (Đại diện 1 ký tự).
  - `#`: 숫자 딱 1개. (Đại diện 1 chữ số).
- **우선순위 (Priority)**: 산술 연산자 (+, -, *, /) > 관계 연산자 (비교) > 논리 연산자. (Toán học > So sánh > Logic).

## 핵심 220: 하위 질의 (Subquery)
- 조건절(WHERE) 안에 또 다른 SELECT문이 포함된 구조. 괄호로 묶어서 사용.
- (Câu truy vấn con nằm trong mệnh đề WHERE của truy vấn chính).
- `EXISTS` 연산자와 함께 사용되기도 함.

## 핵심 222: 그룹 함수 (Aggregate Functions)
- **종류**: 
  - `COUNT`: 개수 (Số lượng).
  - `SUM`: 합계 (Tổng).
  - `AVG`: 평균 (Trung bình).
  - `MAX` / `MIN`: 최대/최소 (Lớn nhất/Nhỏ nhất).
  - `STDDEV`: 표준편차 (Độ lệch chuẩn).
  - `VARIANCE`: 분산 (Phương sai).

## 핵심 223: 집합 연산자를 이용한 통합 질의 (Set Operators)
2개 이상의 SELECT 질의 결과를 통합. 컬럼의 개수와 데이터 타입이 같아야 함.
- **UNION**: 두 조회 결과를 통합 (중복 제거). (Hợp, bỏ trùng lặp).
- **UNION ALL**: 두 조회 결과를 통합 (중복 유지). (Hợp, giữ nguyên trùng lặp).
- **INTERSECT**: 공통된 행만 출력. (Giao, phần chung).
- **EXCEPT**: 첫 번째 결과에서 두 번째 결과를 뺀 나머지. (Hiệu, phần bù).

## 핵심 224: INNER JOIN (내부 조인)
- 가장 일반적인 조인 방식으로, 조인 조건을 만족하는 행들만 반환. (Lấy các dòng thỏa mãn điều kiện join ở cả 2 bảng).
- **EQUI JOIN** (등가 조인, =)과 **NON-EQUI JOIN** (비등가 조인)으로 나뉨.


## 핵심 225: 트리거 (Trigger)
- 데이터베이스에 삽입(Insert), 갱신(Update), 삭제(Delete) 이벤트가 발생할 때마다 **자동으로 수행**되는 절차형 SQL. (Trigger: Tự động kích hoạt khi có sự kiện Insert/Update/Delete).
- 무결성 유지, 로그 출력 등에 사용되며, 내부에 DCL(COMMIT, ROLLBACK 등)을 사용할 수 없다.

## 핵심 226, 227: DBMS 접속 기술 및 ORM
- **JDBC**: Java 언어로 DB에 접속하는 표준 API. (Kết nối DB bằng Java).
- **ODBC**: 개발 언어 관계없이 사용하는 개방형 표준 API. (Kết nối DB mã nguồn mở, không phụ thuộc ngôn ngữ).
- **MyBatis**: JDBC 코드를 단순화한 SQL Mapping 프레임워크. SQL과 XML을 분리. (Framework ánh xạ SQL, tách SQL ra file XML riêng).
- **ORM (Object-Relational Mapping)**: 객체지향 프로그래밍의 객체와 관계형 DB의 데이터를 매핑하는 기술. 독립적이며 재사용/유지보수 용이. (Ánh xạ Object và Bảng CSDL).

## 핵심 228: 쿼리 성능 최적화
- **RBO (Rule Based Optimizer)**: 규칙 기반 옵티마이저 (규칙 우선순위 기준). (Tối ưu hóa dựa trên quy tắc).
- **CBO (Cost Based Optimizer)**: 비용 기반 옵티마이저 (액세스 비용 산출). (Tối ưu hóa dựa trên chi phí/thống kê).

## 핵심 229, 230, 231: 데이터 전환 (ETL) 및 오류 정제
- **데이터 전환 (ETL)**: 기존 데이터를 추출(Extraction), 변환(Transformation), 적재(Loading)하는 과정 (Migration). (Chuyển đổi dữ liệu).
- **오류 상태**: 
  - `Open`: 보고만 된 상태 (Mới báo cáo).
  - `Assigned`: 개발자에게 할당된 상태 (Đã giao).
  - `Fixed`: 수정된 상태 (Đã sửa).
  - `Closed`: 재테스트 후 오류 없음 확인 (Đã đóng).
  - `Deferred`: 수정 연기 (Hoãn).
  - `Classified`: 오류가 아님으로 판명 (Không phải lỗi).

# 4과목: 프로그래밍 언어 활용

## 핵심 232: 배치 프로그램 (Batch Program)
사용자와 상호 작용 없이 일괄적으로 처리하는 프로그램. (Chương trình chạy lô/hàng loạt).
- 필수 요소: 대용량 데이터, 자동화, 견고성, 안정성/신뢰성, 성능.

## 핵심 233, 235: 데이터 타입 및 크기
- **C/C++**: `char`(1Byte), `int`(4Byte), `float`(4Byte), `double`(8Byte).
- **JAVA**: `byte`(1Byte), `boolean`(1Byte), `char`(2Byte), `short`(2Byte), `int`(4Byte), `long`(8Byte), `float`(4Byte), `double`(8Byte).

## 핵심 234: C언어 구조체 (Struct)
자료형이 다른 여러 변수를 묶어서 하나의 단위로 관리할 수 있는 자료형. (Struct: Nhóm các biến có kiểu dữ liệu khác nhau thành 1 khối).
- 형식: `struct 구조체명 { 자료형 변수명; ... }`

## 핵심 236: Python의 시퀀스 자료형
연속적으로 이어진 자료형. (Kiểu dữ liệu chuỗi/danh sách).
- **리스트 (List)**: 변경 가능(Mutable). (Danh sách có thể sửa).
- **튜플 (Tuple)**: 추가/삭제/변경 불가능(Immutable). (Danh sách cố định, không thể sửa).
- **range**: 연속된 숫자 생성. (Tạo dãy số).

## 핵심 237, 238: 변수명 작성 규칙 및 가비지 콜렉터
- **변수명 규칙**: 영문자, 숫자, `_` 사용 가능. 숫자로 시작 불가. 대소문자 구분. 예약어 사용 불가. (Quy tắc đặt tên biến).
- **헝가리안 표기법 (Hungarian Notation)**: 변수명에 데이터 타입을 명시하는 표기법 (예: `iCount` -> integer Count).
- **가비지 콜렉터 (Garbage Collector)**: 사용하지 않는 메모리를 자동으로 회수하여 재사용하게 하는 기능. (Bộ thu gom rác tự động giải phóng bộ nhớ).

## 핵심 239, 240: 산술 연산자와 관계 연산자
- **산술 연산자**: `+`, `-`, `*`, `/`, `%`(나머지). 
- **증감 연산자**: `++`, `--` (전치: 연산 전 증감, 후치: 연산 후 증감). (Tiền tố: Tăng/giảm trước, Hậu tố: Tăng/giảm sau).
- **관계 연산자**: `==`, `!=`, `>`, `>=`, `<`, `<=`. (C 거짓은 0, 참은 1 / 모든 0 외의 값은 참).


## 핵심 241, 242, 243, 244: 비트, 논리, 대입, 조건 연산자
- **비트 연산자 (Bitwise)**: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (Left Shift), `>>` (Right Shift). (Toán tử thao tác bit).
- **논리 연산자 (Logical)**: `!` (NOT), `&&` (AND), `||` (OR).
- **대입 연산자 (Assignment)**: `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `<<=` 등. 연산 후 결과를 대입. (Toán tử gán).
- **조건 연산자 (Ternary)**: `조건 ? 수식1 : 수식2;` (참이면 수식1, 거짓이면 수식2. / Toán tử 3 ngôi: Điều kiện ? Đúng : Sai).

## 핵심 245: 연산자 우선순위 (Operator Precedence)
- **우선순위 요약**: 단항 연산자 (`!`, `~`, `++`, `--`) > 산술 연산자 (`*`, `/`, `%` > `+`, `-`) > 시프트 (`<<`, `>>`) > 관계 연산자 (비교 `>` > `==`) > 비트 연산자 (`&` > `^` > `|`) > 논리 연산자 (`&&` > `||`) > 삼항 조건 (`?:`) > 대입 연산자 (`=`, `+=`).
- (Ưu tiên: Đơn ngôi > Toán học > Dịch bit > So sánh > Bitwise > Logic > 3 ngôi > Gán).

## 핵심 246, 247, 248: C언어 입출력 함수 (scanf, printf)
- **scanf()**: 표준 입력 함수. 변수의 주소 연산자(`&`)를 사용해야 함. (Hàm nhập: cần truyền địa chỉ biến với `&`).
  - 예: `scanf("%d", &a);`
- **printf()**: 표준 출력 함수. 변수의 주소 연산자 없이 값만 전달. (Hàm xuất).
- **서식 문자열 (Format String)**: `%d` (10진 정수), `%c` (문자 1개), `%s` (문자열), `%f` (실수).
  - 예: `%-8.2f` (전체 8자리, 소수점 아래 2자리, 왼쪽 정렬).

## 핵심 249: 주요 제어문자 (Escape Sequences)
- `
`: 줄 바꿈 (New line)
- `	`: 탭 띄우기 (Tab)
- ` `: 널 문자 (Null)
- `
`: 커서를 현재 줄 처음으로 이동 (Carriage return)

## 핵심 250: JAVA에서의 표준 출력
- `System.out.print()`: 형식 없이 그냥 출력. (In ra).
- `System.out.println()`: 출력 후 줄 바꿈(New Line) 추가. (In ra và xuống dòng).
- `System.out.printf()`: C언어의 `printf`와 같이 서식 문자열을 사용하여 출력. (In ra theo định dạng).
- 문자열 연결 시 `+` 연산자 사용 가능 (예: `"Hello " + "World"`).

## 핵심 251, 252: if문 (조건문)
- **단순 if문**: `if(조건) { 실행문 } else { 실행문 }` (Điều kiện rẽ nhánh đơn giản).
- **다중 if문**: `if(조건1) { } else if(조건2) { } else { }`. 중첩(Nested) 사용 가능. (Rẽ nhánh nhiều điều kiện).

## 핵심 253: switch문 (분기문)
- 특정 수식의 결과에 따라 여러 case로 분기. (Rẽ nhánh dựa trên giá trị cụ thể).
- 형식: `switch(수식) { case 상수: 실행문; break; default: 실행문; }`
- **특징**: 
  - `case` 레이블에는 상수(정수, 문자 등)만 가능하며 변수는 불가. (Case chỉ nhận hằng số).
  - `break`문 생략 시 하위의 모든 `case`문들이 순차적으로 모두 실행됨. (Nếu bỏ `break`, code sẽ chạy tuột xuống các case bên dưới).


## 핵심 254, 255, 256: 반복문 (for, while, do~while)
- **for문**: 정해진 횟수를 반복할 때 주로 사용. (Vòng lặp xác định số lần).
  - `for(초기식; 조건식; 증감식) { 실행문; }`
- **while문**: 조건이 참인 동안 무한 반복 가능. 조건이 거짓이면 한 번도 실행되지 않음. (Vòng lặp kiểm tra điều kiện trước).
  - `while(조건) { 실행문; }`
- **do~while문**: **무조건 한 번은 실행**한 후, 조건을 판단하여 반복 여부 결정. (Vòng lặp kiểm tra điều kiện sau, ít nhất chạy 1 lần).
  - `do { 실행문; } while(조건);`

## 핵심 257: 분기/제어 (break, continue)
- **break**: 자신이 속한 가장 가까운 반복문이나 switch문을 탈출. (Thoát khỏi vòng lặp hoặc switch).
- **continue**: 현재 반복의 나머지 부분을 건너뛰고, 다음 반복(조건식이나 증감식)으로 넘어감. 반복문에서만 사용 가능. (Bỏ qua phần còn lại của lần lặp này, chuyển sang lần lặp tiếp theo).

## 핵심 258, 259, 260: 배열 (Array)
- **개념**: 동일한 자료형의 여러 변수를 연속된 메모리 공간에 묶어서 하나의 이름으로 관리. (Mảng: Tập hợp các biến cùng kiểu).
- **특징**: 
  - C언어에서 인덱스(첨자)는 **0부터 시작**. (Chỉ số bắt đầu từ 0).
  - 1차원 배열: `int a[5];` (Mảng 1 chiều).
  - 2차원 배열: `int a[3][4];` (행(Row)과 열(Column)로 구성 / Mảng 2 chiều: Dòng và Cột).
- **초기화**: 
  - `int a[3] = {1, 2, 3};` 
  - 지정한 요소 개수보다 초기값이 적으면 나머지는 **0으로 채워짐**. (Nếu khai báo thiếu giá trị, các phần tử còn lại tự động bằng 0).

## 핵심 261: C언어의 문자열 배열
- C언어에는 문자열 전용 자료형(String)이 없어, `char` 배열이나 포인터를 사용. (C không có kiểu String, dùng mảng char).
- 배열 초기화 시 문자열을 큰따옴표로 묶어 할당하면, 끝에 **자동으로 널 문자(` `)가 삽입**됨. 따라서 크기 지정 시 글자 수 + 1 이상이어야 함. (Cuối chuỗi luôn tự động thêm ký tự NULL ` `).
  - 예: `char a[5] = "love";` ('l', 'o', 'v', 'e', ' ').

## 핵심 262: 포인터와 포인터 변수 (Pointer)
- **개념**: 변수의 **메모리 주소**를 저장하는 변수. 동적 메모리(Heap) 접근 시 활용. (Con trỏ: Biến lưu trữ địa chỉ bộ nhớ).
- **기호**: 
  - `*`: 포인터 선언 시 사용 (예: `int *p;`). 또는 포인터가 가리키는 주소의 **값(Value)**을 참조할 때 사용 (`*p = 10;`). (Dùng để khai báo con trỏ, hoặc lấy giá trị tại địa chỉ đó).
  - `&`: 특정 변수의 **주소(Address)**를 가져올 때 사용. (Dùng để lấy địa chỉ của biến).
- **Example (KR/VN)**: 
  - `int a = 50;` (변수 a 생성 및 50 저장 / Tạo biến a, gán 50).
  - `int *p = &a;` (포인터 p에 a의 주소 저장 / Con trỏ p lưu địa chỉ của a).
  - `*p = 70;` (p가 가리키는 곳(a)의 값을 70으로 변경 / Đổi giá trị tại địa chỉ p trỏ đến thành 70. Lúc này a = 70).
- 💡 **Mẹo ghi nhớ**: `&`(And)는 주소(Address), `*`(Star)는 값(Value)을 가리킨다고 기억하세요.



## 포인터와 배열 (Pointer and Array)
- **개념**: C언어에서 배열을 포인터(Pointer/Con trỏ) 변수에 저장한 후 포인터를 이용해 배열의 요소에 접근할 수 있습니다.
- **특징**:
  - 배열 위치를 나타내는 첨자를 생략하고 배열의 대표명만 지정하면 배열의 첫 번째 요소의 주소를 지정하는 것과 같습니다. (예: `b = a;` 는 `b = &a[0];` 와 동일)
  - 배열 요소에 대한 주소를 지정할 때는 일반 변수와 동일하게 `&` 연산자를 사용합니다.
  - 배열의 요소가 포인터인 포인터형 배열을 선언할 수 있습니다.
  - 포인터 값에 정수를 더하면, 포인터가 가리키는 자료형의 크기(예: 정수형은 4바이트)만큼 물리적 주소가 증가합니다. (예: `p+1`은 4바이트 뒤의 주소)

> **Vietnamese Explanation**: 
> Trong C, tên của mảng (array) chính là con trỏ (pointer) trỏ đến phần tử đầu tiên của mảng đó. Bạn có thể gán mảng cho một biến con trỏ, từ đó dùng con trỏ để truy cập các phần tử thay vì dùng chỉ số (index). Khi cộng 1 vào con trỏ, địa chỉ bộ nhớ sẽ tăng thêm số byte tương ứng với kiểu dữ liệu của nó (ví dụ int tăng 4 byte).

**예시 / Ví dụ:**
```c
int a[5] = {10, 11, 12, 13, 14};
int *p = a; // p trỏ tới a[0]
printf("%d", *(p+1)); // 출력/Output: 11
```

💡 **Mẹo ghi nhớ (Mnemonics):** 
**Tên mảng = Địa chỉ đầu**. Mảng không cần `&` khi trỏ vào, nhưng phần tử thì cần (ví dụ `&a[0]`).


## Python의 기본 문법 (Python Basic Syntax)
- **특징**:
  - 변수의 자료형(Data Type/Kiểu dữ liệu)에 대한 선언이 없습니다.
  - 문장의 끝을 의미하는 세미콜론(`;`)을 사용할 필요가 없습니다.
  - 변수에 연속하여 값을 저장하는 것이 가능합니다. (예: `x, y, z = 10, 20, 30`)
  - `if`나 `for`와 같이 코드 블록(Code Block/Khối lệnh)을 포함하는 명령문을 작성할 때, 콜론(`:`)과 여백(Indentation/Thụt lề)으로 구분합니다.
  - 여백은 일반적으로 4칸 또는 한 개의 탭(Tab)만큼 띄워야 하며, 같은 수준의 코드들은 반드시 동일한 여백을 가져야 합니다.

> **Vietnamese Explanation**: 
> Khác với C hay Java, Python không cần khai báo kiểu dữ liệu cho biến, không cần dấu chấm phẩy `;` ở cuối dòng. Python dùng khoảng trắng (thụt lề) để phân chia các khối lệnh thay vì dùng dấu ngoặc nhọn `{}`.

**예시 / Ví dụ:**
```python
x, y = 10, 20
if x < y:
    print("x is smaller") # Thụt lề 4 khoảng trắng
```

💡 **Mẹo ghi nhớ (Mnemonics):** 
**P.I.T** - **P**ython **I**ndents **T**hings (Python thụt lề mọi thứ).


## Python 데이터 입·출력 함수 (Python Input/Output Functions)

### 1. input( ) 함수
- Python의 표준 입력 함수로, 키보드로 입력받아 변수에 문자열(String) 형태로 저장합니다.
- **형식**: `변수 = input('출력문자')`

### 2. print( ) 함수
- **형식**: `print(출력값1, 출력값2, ..., sep='분리문자', end='종료문자')`
  - `sep`: 여러 값을 출력할 때 값 사이를 구분하는 문자 (기본값: 공백 한 칸)
  - `end`: 맨 마지막에 표시할 문자 (기본값: 줄 바꿈 `\n`)

> **Vietnamese Explanation**: 
> Hàm `input()` dùng để nhận dữ liệu nhập từ bàn phím (mặc định luôn là chuỗi string). Hàm `print()` dùng để in ra màn hình, có thể tùy chỉnh dấu ngăn cách giữa các giá trị `sep` và ký tự kết thúc `end`.

**예시 / Ví dụ:**
```python
print(82, 24, sep='-', end=',')
# 출력/Output: 82-24,
```


## 입력 값의 형변환 (Type Casting)
- `input()` 함수는 입력되는 값을 무조건 문자열(String)로 저장하므로, 숫자로 사용하기 위해서는 형(Type)을 변환해야 합니다.
- **변환할 데이터가 1개일 때**: `int()`, `float()` 사용
- **변환할 데이터가 2개 이상일 때**: `map()`과 `split()` 사용
  - 형식: `변수1, 변수2 = map(int, input().split())`

> **Vietnamese Explanation**: 
> Vì `input()` trả về chuỗi, bạn phải ép kiểu sang số thực (`float`) hoặc số nguyên (`int`). Để nhập nhiều số cùng lúc trên một dòng, dùng `split()` để tách chuỗi và `map()` để ép kiểu hàng loạt cho tất cả các phần tử.

**예시 / Ví dụ:**
```python
a, b = map(int, input("Nhập 2 số: ").split())
# Nếu nhập "10 20", a=10, b=20
```

💡 **Mẹo ghi nhớ (Mnemonics):** 
**M.I.S** - **M**ap **I**nt **S**plit để nhập nhiều số nguyên cùng lúc.


## Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)

### 1. 리스트 (List / Danh sách)
- C/Java의 배열(Array)과 달리 크기를 지정하지 않으며, 정수/실수/문자열 등 다양한 자료형을 섞어서 저장할 수 있습니다.
- 위치(Index)는 0부터 시작합니다.
- **형식**: `리스트명 = [값1, 값2, ...]` 또는 `list([값1, 값2, ...])`

### 2. 딕셔너리 (Dictionary / Từ điển)
- 연관된 값을 묶어서 저장하는 용도로, 인덱스 대신 사용자가 원하는 값을 키(Key)로 지정해 사용합니다. 키-값 쌍(Key-Value pairs) 형태로 저장합니다.
- **형식**: `딕셔너리명 = {키1:값1, 키2:값2, ...}` 또는 `dict(...)`

> **Vietnamese Explanation**: 
> List giống như Array nhưng linh hoạt hơn nhiều (có thể chứa nhiều kiểu dữ liệu cùng lúc, tự động thay đổi kích thước). Dictionary lưu dữ liệu theo dạng Cặp Chìa khóa - Giá trị (Key-Value), cho phép tra cứu nhanh theo Key.

**예시 / Ví dụ:**
```python
# List
my_list = [10, "mike", 23.45]
# Dictionary
my_dict = {"이름": "홍길동", "나이": 25}
my_dict["주소"] = "서울" # Thêm phần tử
```

💡 **Mẹo ghi nhớ (Mnemonics):** 
- **List**: Ngoặc vuông `[]` (Ví dụ: cái hộp hình vuông chứa đủ đồ).
- **Dict**: Ngoặc nhọn `{}` (Có dạng `Key: Value`).


## 슬라이스 (Slice)
- **개념**: 문자열이나 리스트와 같은 순차형 객체에서 일부를 잘라(Slicing) 반환하는 기능입니다.
- **형식**: `객체명[초기위치:최종위치:증가값]`
  - `초기위치`에서 `최종위치 - 1` 까지의 요소들을 가져옵니다.
  - 인수를 생략하면 전체를 의미하거나, 기본값(처음, 끝, 1씩 증가)이 적용됩니다.

> **Vietnamese Explanation**: 
> Slice (cắt lát) giúp lấy ra một phần của List hoặc String một cách dễ dàng. Nhớ là vị trí kết thúc không bao giờ được bao gồm (chỉ lấy đến `cuối - 1`).

**예시 / Ví dụ:**
```python
a = ['a', 'b', 'c', 'd', 'e']
print(a[1:3])    # ['b', 'c']
print(a[0:5:2])  # ['a', 'c', 'e'] (Lấy cách nhau 2 bước)
print(a[::-1])   # Lật ngược list (âm là đi lùi)
```


## Python 제어문 (Control Statements): if문, for문

### 1. if문 (if Statement / Câu lệnh điều kiện)
- **형식**:
  ```python
  if 조건:
      실행할 문장
  ```
- 조건 뒤에 콜론(`:`)을 붙이고, 실행할 문장은 반드시 여백(Indentation)을 주어야 합니다.

### 2. for문 (for Statement / Vòng lặp for)
- **형식 1 (range 이용)**:
  ```python
  for 변수 in range(초기값, 최종값, 증가값):
      실행할 문장
  ```
  - `최종값` - 1 까지 반복합니다.
- **형식 2 (리스트 이용)**:
  ```python
  for 변수 in 리스트:
      실행할 문장
  ```

> **Vietnamese Explanation**: 
> `if` dùng để rẽ nhánh điều kiện. `for` dùng để lặp. Hàm `range(start, end, step)` sinh ra một dãy số từ `start` tới `end-1` với khoảng cách là `step`.

**예시 / Ví dụ:**
```python
# Tính tổng các số từ 1 đến 4
sum = 0
for i in range(1, 5): 
    sum += i
print(sum) # Output: 10 (1+2+3+4)
```


## Python 클래스 (Class) - 기초 (Cơ bản)
- **정의 형식**:
  ```python
  class 클래스명:
      def 메소드명(self, 인수):
          실행할 문장
          return 값
  ```
- `def`는 메소드(Method/Phương thức)를 정의하는 예약어입니다.
- `self`는 메소드에서 자기 클래스에 속한 변수에 접근할 때 사용하는 명칭으로 첫 번째 인수로 반드시 작성합니다.

> **Vietnamese Explanation**: 
> Class là khuôn mẫu để tạo ra các đối tượng (Objects). Hàm định nghĩa bên trong class được gọi là method (phương thức) và luôn phải có tham số `self` đại diện cho chính đối tượng đó.

## Python 클래스와 함수 (Class and Functions)

### 1. 객체 생성 및 메소드 (Objects and Methods)
- **클래스 기반 객체 생성**: `변수명 = 클래스명()`
  - 예: `a = Cls()` (Cls 클래스의 객체 a를 생성)
  - 객체의 속성(변수)이나 메소드(함수)에 접근할 때는 마침표(`.`)를 사용합니다. (예: `a.x`, `a.chg()`)
- **함수 (클래스 없는 메소드)**: C언어의 함수처럼 클래스 없이 독립적으로 `def`를 이용해 메소드를 선언하고 사용할 수 있습니다.

> **Vietnamese Explanation**: 
> Bạn có thể tạo đối tượng (object) từ một class bằng cú pháp `tên_biến = TênClass()`. Để truy cập biến hay hàm bên trong, ta dùng dấu chấm `.`. Ngoài ra, Python cũng cho phép định nghĩa các hàm độc lập không cần nằm trong class bằng từ khóa `def`.

**예시 / Ví dụ:**
```python
# Hàm độc lập (Function)
def calc(x, y):
    return x * y

a = calc(3, 4) # a = 12
```


## Python 제어문: while문 (While Loop)
- **형식**:
  ```python
  while 조건:
      실행할 문장
  ```
- 조건이 참(True)인 동안 실행할 문장을 반복 수행합니다.

**예시 / Ví dụ:**
```python
i = 0
while i < 5:
    i += 1
```


## 프로그래밍 언어의 분류 (Classification of Programming Languages)

### 1. 절차적 프로그래밍 언어 (Procedural)
- **C**: UNIX의 일부를 구현한 언어. 시스템 프로그래밍에 적합하며 포인터(Pointer) 제공.
- **ALGOL**: 과학 기술 계산용. PASCAL과 C의 모체.
- **COBOL**: 사무 처리용. 영어 문장 형식 (4개의 DIVISION).
- **FORTRAN**: 수학과 공학 등 과학 기술 계산용.

### 2. 객체지향 프로그래밍 언어 (Object-Oriented)
- **JAVA**: 분산 네트워크 환경 적합, 멀티스레드(Multi-thread) 지원, 이식성 강함.
- **C++**: C언어에 객체지향 개념을 추가.
- **Smalltalk**: 1세대 순수 객체지향 언어로, 최초로 GUI를 제공.

### 3. 스크립트 언어 (Scripting)
- **클라이언트 측 (Client-side)**:
  - **JavaScript**: 웹 페이지 동작 제어.
  - **VBScript**: Microsoft 애플리케이션 제어 (Active X).
- **서버 측 (Server-side)**:
  - **ASP**: Microsoft 제작, Windows 전용.
  - **JSP**: Java 기반, 다양한 운영체제 지원.
  - **PHP**: C/Java와 유사한 문법, Linux/Unix/Windows 등 다양하게 지원.
- **기타**: Python(대화형 인터프리터, 플랫폼 독립적), Shell Script(유닉스/리눅스 명령어 조합).

### 4. 선언형 프로그래밍 언어 (Declarative)
- **HTML**: 하이퍼텍스트 웹 표준 문서 생성.
- **LISP**: 인공지능 분야. 연결 리스트(Linked List) 및 재귀(Recursion) 호출 사용.
- **PROLOG**: 논리학 기초, 인공지능 논리 추론.
- **XML**: HTML 단점 보완, 태그(Tag) 사용자 정의 가능.
- **Haskell**: 함수형 언어로 부작용(Side Effect)이 없음.

💡 **Mẹo ghi nhớ (Mnemonics):** 
- **C.A.C.F** = Các ngôn ngữ thủ tục (C, Algol, Cobol, Fortran).
- **J.A.P** = Các ngôn ngữ kịch bản Server-side (JSP, ASP, PHP).


## 라이브러리 및 예외 처리 (Libraries and Exception Handling)

### 1. 라이브러리 (Library)
- 자주 사용하는 함수나 데이터들을 미리 만들어 모아 놓은 집합체 (표준 라이브러리, 외부 라이브러리).
- **C언어 대표 표준 라이브러리**:
  - `stdio.h`: 입출력 (`printf`, `scanf`)
  - `math.h`: 수학 함수 (`sqrt`, `pow`)
  - `string.h`: 문자열 처리 (`strlen`, `strcpy`)
  - `stdlib.h`: 자료형 변환, 메모리 할당, 난수 (`atoi`, `malloc`, `rand`)
  - `time.h`: 시간 처리 (`time`)

### 2. 예외 처리 (Exception Handling)
- 프로그램의 정상적인 실행을 방해하는 조건이나 상태를 예외(Exception)라고 합니다.
- 예외 발생 시 비정상 종료를 막고 대비해 놓은 처리 루틴을 수행하는 것을 의미합니다.

> **Vietnamese Explanation**: 
> Thư viện (Library) là nơi chứa các hàm viết sẵn để bạn gọi ra dùng (ví dụ nhập xuất, toán học). Xử lý ngoại lệ (Exception Handling) là việc bắt các lỗi có thể xảy ra trong lúc chạy (như chia cho 0, mất kết nối) để chương trình không bị sập ngang.


## 운영체제 (OS: Operating System) 기초

### 1. 정의 및 목적
- 하드웨어를 제어하고 사용자가 편리하게 컴퓨터를 사용할 수 있도록 돕는 시스템 소프트웨어.
- **성능 평가 4가지 기준**:
  1. **처리 능력 (Throughput)**: 일정 시간 내에 시스템이 처리하는 일의 양. (높을수록 좋음)
  2. **반환 시간 (Turn Around Time)**: 작업 의뢰부터 완료될 때까지 걸린 시간. (짧을수록 좋음)
  3. **사용 가능도 (Availability)**: 시스템을 필요할 때 즉시 사용할 수 있는 정도. (높을수록 좋음)
  4. **신뢰도 (Reliability)**: 시스템이 문제를 정확하게 해결하는 정도. (높을수록 좋음)

### 2. 운영체제의 구성
- **제어 프로그램 (Control Program)**:
  - 감시 프로그램 (Supervisor): 자원 할당 및 작동 감시 (가장 핵심).
  - 작업 관리 (Job Management): 작업 순서 및 방법 관리.
  - 데이터 관리 (Data Management): 데이터/파일 처리 관리.
- **처리 프로그램 (Processing Program)**:
  - 언어 번역 프로그램 (컴파일러, 어셈블러 등).
  - 서비스 프로그램 (유틸리티 등).

💡 **Mẹo ghi nhớ (Mnemonics):** 
- **Hiệu suất OS**: T.T.A.R (Throughput - Turnaround - Availability - Reliability).
- **Chương trình điều khiển**: Giám sát (Supervisor) - Công việc (Job) - Dữ liệu (Data).


## Windows와 UNIX 운영체제 (Windows & UNIX)

### 1. Windows 주요 특징
- **GUI (Graphic User Interface)**: 마우스 기반 그래픽 환경.
- **선점형 멀티태스킹 (Preemptive Multi-Tasking)**: 응용 프로그램 문제 시 OS가 강제 종료시켜 자원 반환.
- **PnP (Plug and Play)**: 하드웨어 설치 시 OS가 자동 감지 및 환경 구성.
- **OLE (Object Linking and Embedding)**: 문자/그림 개체를 다른 문서에 연결하거나 삽입.
- **긴 파일명**: 최대 255자 지정 가능 (VFAT 이용).

### 2. UNIX 주요 특징
- 대화식 시분할 시스템 (Time Sharing System) 및 개방형 시스템 (Open System).
- 주로 **C언어**로 작성되어 이식성이 높고 파일 시스템은 트리(Tree) 구조를 가짐.
- **다중 사용자 (Multi-User)** 및 **다중 작업 (Multi-Tasking)** 지원.

### 3. 파일 디스크립터 (File Descriptor)
- 파일 제어 블록(FCB; File Control Block)이라고도 하며, 시스템(OS)이 필요로 하는 파일에 대한 정보를 가진 제어 블록.
- 파일마다 독립적으로 존재하며 보통 보조기억장치에 있다가 파일이 열릴(Open) 때 주기억장치로 옮겨집니다.

### 4. UNIX 시스템 구조: 커널 (Kernel)
- UNIX의 가장 **핵심적인 부분**. 프로그램과 하드웨어 간의 인터페이스 역할을 담당하며 프로세스, 메모리, 입출력 관리 등을 수행합니다.

> **Vietnamese Explanation**: 
> Windows nổi bật với giao diện chuột GUI, Plug and Play (cắm là chạy). UNIX là hệ điều hành mã nguồn mở, đa nhiệm, đa người dùng, chủ yếu viết bằng C. Trong UNIX, Kernel (nhân) là phần cốt lõi quản lý phần cứng và giao tiếp với phần mềm. File Descriptor lưu giữ thông tin quan trọng về các file đang được hệ thống quản lý.

## UNIX 주요 구성요소 (UNIX Components)

### 1. 쉘 (Shell)
- 사용자의 명령어를 인식하여 프로그램을 호출하고 명령을 수행하는 **명령어 해석기**입니다.
- 주기억장치에 상주하지 않고 명령어가 포함된 파일 형태로 존재합니다.
- 파이프라인 기능을 지원하며 입·출력 재지정(Redirection)이 가능합니다.
- 예: Bourne Shell, C Shell, Korn Shell 등

### 2. 유틸리티 프로그램 (Utility Program)
- 일반 사용자가 작성한 응용 프로그램을 처리하는 데 사용됩니다. (에디터, 컴파일러, 디버거 등)

> **Vietnamese Explanation**: 
> Shell trong UNIX đóng vai trò như người phiên dịch, nhận lệnh từ người dùng và giao cho hệ thống xử lý. Chương trình tiện ích (Utility) là các công cụ hỗ trợ người dùng như trình soạn thảo, trình biên dịch.


## 메모리 관리 (Memory Management)

### 1. 배치 전략 (Placement Strategy)
새로 반입되는 프로그램이나 데이터를 주기억장치의 어디에 위치시킬 것인지 결정합니다.
- **최초 적합 (First Fit)**: 빈 영역 중 첫 번째 분할 영역에 배치.
- **최적 적합 (Best Fit)**: 단편화(Fragmentation/Khoảng trống thừa)를 가장 작게 남기는 분할 영역에 배치.
- **최악 적합 (Worst Fit)**: 단편화를 가장 많이 남기는 분할 영역에 배치.

### 2. 가상기억장치 구현 기법 (Virtual Memory Techniques)
- **페이징(Paging) 기법**: 가상기억장치와 주기억장치를 **동일한 크기**로 나누어 적재. (프로그램 단위: 페이지, 주기억장치 단위: 페이지 프레임)
  - 외부 단편화는 발생하지 않으나, **내부 단편화**는 발생 가능.
- **세그먼테이션(Segmentation) 기법**: 프로그램을 배열이나 함수 등 **다양한 크기의 논리적인 단위(세그먼트)**로 나누어 적재.
  - 내부 단편화는 발생하지 않으나, **외부 단편화**는 발생 가능.

💡 **Mẹo ghi nhớ (Mnemonics):** 
- **Paging**: Bằng nhau (Page). Lỗi nội bộ (내부 단편화).
- **Segmentation**: Khác nhau (Theo logic). Lỗi bên ngoài (외부 단편화).


## 페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)

### 1. 페이지 교체 알고리즘 (Page Replacement Algorithms)
페이지 부재(Page Fault) 발생 시, 어떤 페이지 프레임을 교체할 것인지 결정합니다.
- **OPT (Optimal)**: 앞으로 가장 오랫동안 사용하지 않을 페이지 교체 (가장 효율적이나 미래 예측이 필요해 비현실적).
- **FIFO (First In First Out)**: 가장 먼저 들어와서 가장 오래 있었던 페이지 교체.
- **LRU (Least Recently Used)**: 최근에 가장 오랫동안 사용하지 않은 페이지 교체 (계수기나 스택 사용).
- **LFU (Least Frequently Used)**: 사용 빈도(횟수)가 가장 적은 페이지 교체.
- **NUR (Not Used Recently)**: LRU의 오버헤드를 줄이기 위해 참조 비트와 변형 비트를 사용하여 최근 사용 안 된 페이지 교체.
- **SCR (Second Chance Replacement)**: FIFO의 단점을 보완하여 자주 사용되는 페이지는 한 번 더 기회를 줌.

### 2. 페이지 크기 (Page Size)
- **크기가 작을 경우**: 페이지 단편화 감소, 워킹 셋 효율 증가, Locality 일치로 기억장치 효율 상승. 단, 페이지 맵 테이블 크기가 커지고 매핑 속도가 느려지며 디스크 입출력 횟수가 증가.
- **크기가 클 경우**: 페이지 맵 테이블 크기 감소, 매핑 속도 상승, 디스크 입출력 횟수 감소. 단, 불필요한 내용까지 적재될 수 있고 페이지 단편화가 증가.


## 프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)

### 1. Locality (국부성, 구역성)
프로세스 실행 중 일부 페이지만 집중적으로 참조하는 성질.
- **시간 구역성 (Temporal Locality)**: 하나의 페이지를 짧은 시간 동안 집중 참조 (반복문, 스택 등).
- **공간 구역성 (Spatial Locality)**: 특정 위치 주변의 페이지를 집중 참조 (배열, 순차적 코드 등).

### 2. 워킹 셋 (Working Set)
프로세스가 일정 시간 동안 자주 참조하는 페이지들의 집합. (시간에 따라 변함). 주기억장치에 상주시키면 페이지 부재 현상이 줄어듭니다.

### 3. 스래싱 (Thrashing)
프로세스 처리 시간보다 페이지 교체에 소요되는 시간이 더 많아져 시스템 성능이 급격히 저하되는 현상.
- **방지 방법**: 다중 프로그래밍 정도 조절, 페이지 부재 빈도 조절, 워킹 셋 유지 등.

> **Vietnamese Explanation**: 
> **Locality** là tính cục bộ (hay dùng lại chỗ vừa dùng). **Working Set** là tập hợp các trang bộ nhớ đang được dùng nhiều nhất, cần giữ lại ở RAM. **Thrashing** là hiện tượng "giậm chân tại chỗ", máy bận rộn tráo đổi dữ liệu với ổ cứng nhiều hơn là thực sự chạy chương trình, làm máy bị đơ.


## 프로세스와 스레드 (Process and Thread)

### 1. 프로세스 (Process)
- CPU에 의해 처리되는 실행 중인 프로그램 (작업/Job, 태스크/Task).
- **PCB(Process Control Block)**: 운영체제가 프로세스에 대한 중요한 정보를 저장하는 곳. (현재 상태, 포인터, 고유 식별자, 스케줄링 우선순위 등). 프로세스 생성 시 만들어지고 완료 시 제거됨.

### 2. 프로세스 상태 전이 (Process State Transition)
- **제출(Submit) -> 접수(Hold) -> 준비(Ready) -> 실행(Run) -> 대기(Wait/Block) -> 종료(Exit)**
- **주요 용어**:
  - **Dispatch (디스패치)**: 준비 상태 -> 실행 상태로 전이 (CPU 할당).
  - **Wake Up (웨이크 업)**: 입·출력 완료 후 대기 상태 -> 준비 상태로 전이.
  - **Spooling (스풀링)**: 디스크를 버퍼처럼 활용해 느린 입출력 장치와 CPU 간 속도 차이를 보완.

### 3. 스레드 (Thread)
- 프로세스 내에서의 작업 단위 (경량 프로세스/Light Weight Process).
- 동일 프로세스 환경에서 서로 독립적인 다중 수행이 가능하여 응답 시간을 단축하고 기억장소 낭비를 줄입니다.

> **Vietnamese Explanation**: 
> **Process** là một chương trình đang chạy. **Thread** là các luồng xử lý nhỏ nằm bên trong Process. Dùng nhiều thread giúp chương trình chạy nhanh hơn và chia sẻ bộ nhớ tốt hơn (ví dụ nhiều tab trên trình duyệt). **Dispatch** là hành động cấp CPU cho một tiến trình đang xếp hàng chờ.


## 주요 스케줄링 알고리즘 (Major Scheduling Algorithms)

### 1. FCFS (First Come First Service) / FIFO
준비 큐에 도착한 순서대로 CPU를 할당하는 기법 (선입선출). 구현은 가장 간단하나, 긴 작업이 먼저 오면 뒤의 짧은 작업이 오래 기다리게 됨.

### 2. SJF (Shortest Job First)
실행 시간이 가장 짧은 프로세스에게 먼저 CPU를 할당하는 기법. 가장 적은 평균 대기 시간을 제공하지만, 실행 시간이 긴 프로세스는 무한정 기다릴 수 있음.

### 3. HRN (Highest Response-ratio Next)
SJF의 단점(긴 작업 불리)을 보완하여 대기 시간과 실행 시간을 함께 고려함.
- **우선순위 계산식**: `(대기 시간 + 서비스 시간) / 서비스 시간`
- 결과값이 높은 것부터 우선순위를 부여함.

## UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)

### 1. 주요 환경 변수 (Environment Variables)
환경 변수를 사용할 때는 변수명 앞에 `$`를 붙입니다.
- `$HOME`: 사용자의 홈 디렉터리
- `$PWD`: 현재 작업하는 디렉터리
- `$PATH`: 실행 파일을 찾는 경로
- `$USER`: 사용자의 이름

### 2. 기본 명령어 (Basic Commands)
- `cat`: 파일 내용 화면 표시
- `chmod`: 파일 보호 모드 설정 (사용 허가 지정)
- `chown`: 파일 소유자 변경
- `cp`: 파일 복사 / `rm`: 파일 삭제
- `find`: 파일 검색
- `fork`: 새로운 프로세스 생성 (프로세스 복제)
- `fsck`: 파일 시스템 검사 및 보수
- `ls`: 현재 디렉터리 내 파일 목록 확인

> **Vietnamese Explanation**: 
> Biến môi trường trong UNIX/LINUX giúp hệ thống biết các cài đặt mặc định (như đường dẫn `$PATH`, thư mục chủ `$HOME`). Các lệnh cơ bản như `chmod` dùng để phân quyền file, `fork` để nhân bản tiến trình.


## IP 주소 및 서브네팅 (IP Address & Subnetting)

### 1. IPv4 주소 (Internet Protocol version 4)
- 8비트씩 4부분, 총 **32비트**로 구성됩니다.
- 네트워크 크기에 따라 A~E 클래스로 나뉩니다.
  - **A Class**: 국가/대형 망 (0~127)
  - **B Class**: 중대형 망 (128~191)
  - **C Class**: 소규모 망 (192~223)
  - **D Class**: 멀티캐스트용 (224~239)
  - **E Class**: 실험적 주소

### 2. 서브네팅 (Subnetting)
할당된 네트워크 주소를 다시 여러 개의 작은 네트워크로 나누어 사용하는 기법입니다. (서브넷 마스크 활용).

### 3. IPv6 주소 (Internet Protocol version 6)
- IPv4의 주소 부족 문제를 해결하기 위해 개발되었습니다.
- 16비트씩 8부분, 총 **128비트**로 구성되며 콜론(`:`)으로 구분합니다.
- 인증성, 기밀성, 무결성을 지원하여 보안이 뛰어나고, 주소 확장성과 호환성이 좋습니다.
- **주소 체계**:
  - **유니캐스트 (Unicast)**: 1 대 1 통신
  - **멀티캐스트 (Multicast)**: 1 대 다 통신
  - **애니캐스트 (Anycast)**: 1 대 1 통신 (가장 가까운 수신자에게 전송)

💡 **Mẹo ghi nhớ (Mnemonics):** 
- **IPv4**: 32-bit (4 x 8).
- **IPv6**: 128-bit (8 x 16), **U.M.A** (Unicast, Multicast, Anycast).


## OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)
국제표준화기구(ISO)에서 제안한 통신 규약으로, 하위 3계층과 상위 4계층으로 나뉩니다.
- **물리 계층 (Physical)**: 실제 접속, 기계적/전기적 특성 정의.
- **데이터 링크 계층 (Data Link)**: 인접 시스템 간 신뢰성 있는 전송, 흐름 제어, 오류 제어, 동기화.
- **네트워크 계층 (Network)**: 경로 설정(Routing), 트래픽 제어, 패킷 전송.
- **전송 계층 (Transport)**: 종단(End-to-End) 간 신뢰성 있는 데이터 전송, 연결 설정, 다중화.
- **세션 계층 (Session)**: 대화(회화) 제어, 동기 제어.
- **표현 계층 (Presentation)**: 데이터 형식 변환, 암호화, 압축.
- **응용 계층 (Application)**: 사용자에게 통신 서비스 제공.

> **Vietnamese Explanation**: 
> Mô hình OSI chia quá trình truyền mạng thành 7 lớp. 3 lớp dưới (Physical, Data Link, Network) lo việc truyền dẫn tín hiệu, tìm đường (routing). 4 lớp trên (Transport, Session, Presentation, Application) lo việc kiểm tra lỗi, mã hóa dữ liệu và giao tiếp với người dùng.


## 네트워크 관련 장비 (Network Equipment)
- **NIC (Network Interface Card)**: 컴퓨터와 네트워크 연결 (랜카드).
- **허브 (Hub)**: 여러 컴퓨터 연결 및 회선 통합 관리 (리피터 역할 포함).
- **리피터 (Repeater)**: 약해진 신호를 증폭/재생하여 다시 전송.
- **브리지 (Bridge)**: LAN과 LAN을 연결 (MAC 주소 기반).
- **스위치 (Switch)**: 브리지와 유사하나 하드웨어 기반으로 속도가 더 빠름.
- **라우터 (Router)**: 최적 경로(Routing) 선택, 서로 다른 네트워크 연결 (네트워크 계층).
- **게이트웨이 (Gateway)**: 프로토콜이 전혀 다른 네트워크들을 연결하는 출입구 역할 (전 계층).

💡 **Mẹo ghi nhớ (Mnemonics):** 
- **Repeater**: Tầng 1 (Khuếch đại tín hiệu).
- **Bridge/Switch**: Tầng 2 (Nối LAN).
- **Router**: Tầng 3 (Tìm đường IP).
- **Gateway**: Tầng 4-7 (Cổng nối các mạng khác biệt).


## 계층별 주요 프로토콜 (Major Protocols by Layer)

### 1. 응용 계층 (Application)
- **FTP**: 파일 전송 / **SMTP**: 이메일 송신 / **HTTP**: 웹 문서 송수신
- **TELNET**: 원격 접속 가상 터미널 / **DNS**: 도메인 네임을 IP 주소로 변환

### 2. 전송 계층 (Transport)
- **TCP**: 연결 지향, 양방향, 신뢰성 보장, 스트림 위주 전달, 흐름 및 순서 제어 기능 제공.
- **UDP**: 비연결형, 빠른 전송 속도 (실시간 전송 유리, 오버헤드 적음).

### 3. 인터넷 계층 (Internet / Network)
- **IP**: 데이터 주소 지정 및 경로 설정.
- **ICMP**: 제어 메시지 및 오류 처리 관리.
- **ARP**: IP 주소 -> MAC 주소 (물리적 주소)로 변환.
- **RARP**: MAC 주소 -> IP 주소로 변환.

### 4. 네트워크 액세스 계층 (Data Link & Physical)
- **Ethernet (IEEE 802.3)**, **HDLC**, **X.25**, **RS-232C** 등.


## 5과목 정보시스템 구축 관리 (Information System Construction Management)

### 소프트웨어 개발 방법론 (Software Development Methodologies)
- **구조적 방법론 (Structured)**: 처리(Process) 중심. 분할과 정복(Divide and Conquer) 원리 적용.
- **정보공학 방법론 (Information Engineering)**: 자료(Data) 중심. 대규모 정보 시스템 구축에 적합.
- **컴포넌트 기반 방법론 (CBD)**: 기존 컴포넌트를 조합하여 새로운 애플리케이션 생성. 재사용성(Reusability)과 확장성이 높고 유지보수 비용 최소화.

### 소프트웨어 재사용과 재공학 (Software Reuse & Reengineering)
- **소프트웨어 재사용 (Reuse)**: 이미 검증된 소프트웨어를 새로운 개발에 사용하여 개발 시간 및 비용 단축, 품질 향상.
- **소프트웨어 재공학 (Reengineering)**: 기존 시스템을 유지보수 관점에서 개조 및 개선하여 새로운 기능을 추가하고 성능을 높이는 기술 (예방 유지보수 측면).

> **Vietnamese Explanation**: 
> - **Methodologies**: Structured (Tập trung vào quá trình), Information Engineering (Tập trung vào dữ liệu), CBD (Lắp ráp từ các linh kiện có sẵn).
> - **Reuse**: Dùng lại code/module cũ cho dự án mới để tiết kiệm chi phí. 
> - **Reengineering**: Tái cấu trúc, cải tiến hệ thống cũ để dễ bảo trì và đáp ứng nhu cầu mới.

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


## CASE (Computer Aided Software Engineering)
- 소프트웨어 개발 생명 주기(요구 분석, 설계, 구현, 검사 등) 전체 또는 일부를 **컴퓨터와 전용 도구를 사용해 자동화**하는 기법.
- 개발의 표준화를 지향하며 생산성 및 품질을 향상시킵니다.


## 소프트웨어 비용 산정 기법 (Software Cost Estimation)

### 1. LOC (Line Of Code) 기법
- 원시 코드(Source Code) 라인 수의 낙관치, 비관치, 기대치를 측정해 예측치를 구하여 비용을 산정.
- **공식**:
  - 노력(인월, Man-Month) = `LOC / 1인당 월평균 생산 코드 라인 수` = `개발 기간 × 투입 인원`
  - 개발 비용 = `노력(인월) × 단위 비용(월평균 인건비)`

### 2. 수학적 산정 기법
과거의 프로젝트 데이터를 기반으로 한 상향식 비용 산정 모델입니다.
- **COCOMO 모형 (Boehm 제안)**: LOC 기반 산정. 소프트웨어 규모에 따라 3가지로 분류.
  1. **조직형 (Organic)**: 5만 라인 이하 (중소 규모 업무용).
  2. **반분리형 (Semi-Detached)**: 30만 라인 이하 (컴파일러, 유틸리티).
  3. **내장형 (Embedded)**: 30만 라인 이상 (초대형 운영체제, 미사일 제어).
- **Putnam 모형 (생명 주기 예측 모형)**: 시간에 따른 **Rayleigh-Norden 곡선**의 노력 분포도를 기초로 산정.
- **FP (Function Point, 기능 점수) 모형**: 알브레히트(Albrecht) 제안. 기능 요인(입력, 출력, 사용자 질의, 데이터 파일, 외부 인터페이스)별로 가중치를 부여해 산정.

> **Vietnamese Explanation**: 
> - **LOC**: Tính chi phí dựa trên số dòng code.
> - **COCOMO**: Phân loại theo độ lớn dự án (Organic: nhỏ, Semi: vừa, Embedded: lớn).
> - **Putnam**: Dựa trên đường cong phân bố nỗ lực theo thời gian Rayleigh-Norden.
> - **FP (Function Point)**: Dựa trên số lượng chức năng phần mềm mang lại cho người dùng.

💡 **Mẹo ghi nhớ (Mnemonics):** 
- FP의 5가지 요인: **I.O.Q.F.I** (Input, Output, inQuiry, File, Interface).


## 프로젝트 일정 관리 (Project Schedule Management)

### 1. PERT (Program Evaluation and Review Technique)
과거 경험이 없어 예측이 어려운 프로젝트에 사용. 각 작업별로 낙관치, 기대치, 비관치를 나누어 종료 시기를 계산합니다.
- `예측치 = (비관치 + 4*기대치 + 낙관치) / 6`

### 2. CPM (Critical Path Method, 임계 경로 기법)
작업 사이의 의존 관계를 노드와 간선으로 구성. 네트워크에서 최장 경로가 **임계 경로(Critical Path)**가 됩니다.

### 3. 간트 차트 (Gantt Chart, 시간선 차트)
각 작업의 시작과 종료를 막대 도표로 표시하는 일정표. 적응성이 약하지만 이정표와 작업 기간을 한눈에 파악하기 쉽습니다.


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


## 소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)

### 1. 테일러링 (Tailoring)
프로젝트 특성에 맞게 개발 방법론의 절차나 기법을 수정 및 보완하는 작업.
- **내부적 기준**: 목표 환경, 요구사항, 프로젝트 규모, 보유 기술.
- **외부적 기준**: 법적 제약사항, 표준 품질 기준.

### 2. 소프트웨어 개발 프레임워크 (Framework)
공통 사용되는 구성 요소와 아키텍처를 일반화하여 제공하는 반제품 형태의 시스템. (예외 처리, 트랜잭션, DB 연동 등 기본 기능 제공).
- **종류**: 스프링(Spring - Java용), 닷넷(.NET - Windows용), 전자정부 프레임워크(공공부문 지원).

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
- **OSPF**: Link State (Dùng cho mạng lớn).
- **CSMA/CD**: Mạng LAN có dây (Collision Detection).
- **CSMA/CA**: Mạng không dây (Collision Avoidance).


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


## 데이터베이스 신기술 (DB New Technologies)

### 1. 빅데이터 및 분석 기술
- **하둡 (Hadoop)**: 대용량 데이터를 병렬로 처리하기 위한 자바 소프트웨어 프레임워크 (오픈소스).
- **맵리듀스 (MapReduce)**: 하둡 기반 분산 처리 프로그래밍 모델 (Map으로 분류, Reduce로 추출).
- **데이터 마이닝 (Data Mining)**: 대량의 데이터에서 패턴을 규명하여 유용한 정보를 추출하는 기법.
- **OLAP**: 다차원 데이터로부터 통계적 요약 정보를 분석하여 의사결정에 활용. (연산: Roll-up, Drill-down, Pivoting 등).


## DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)

### 1. 회복 기법 (Recovery)
장애 발생 시 데이터베이스를 정상 상태로 복구합니다.
- **연기 갱신 (Deferred Update)**: 트랜잭션이 완료될 때까지 DB 갱신을 연기하고 로그(Log)에 보관. 실패 시 무시하면 됨. (Redo만 가능).
- **즉각 갱신 (Immediate Update)**: 즉시 DB에 갱신하고 로그에 보관. 실패 시 취소(Undo)와 재실행(Redo) 모두 사용.
- **그림자 페이지 (Shadow Paging)**: 복사본(그림자) 페이지를 보관해두고, 실패 시 대체하는 방식 (로그 불필요).
- **검사점 (Check Point)**: 특정 단계에 검사점을 찍어 장애 시 그 시점부터 회복(시간 절약).

### 2. 병행 제어 기법 (Concurrency Control)
다중 트랜잭션 실행 시 DB의 일관성이 파괴되지 않도록 제어합니다.
- **로킹 (Locking)**: 데이터 엑세스 전에 Lock(잠금)을 요청하는 기법. (로킹 단위: DB, 파일, 레코드 등 한꺼번에 잠그는 크기).
- **타임 스탬프 순서 (Time Stamp Ordering)**: 트랜잭션 실행 전 시간표(Time Stamp)를 부여해 그 순서대로 처리 (교착상태 미발생).
- **다중 버전 기법**: 갱신될 때마다 새로운 버전(Version)을 부여해 관리.

> **Vietnamese Explanation**: 
> **Recovery (Phục hồi DB)** có Deferred (chờ xong mới cập nhật - chỉ Redo), Immediate (cập nhật ngay - cần cả Undo và Redo).
> **Concurrency Control (Kiểm soát đồng thời)** dùng Locking (khóa dữ liệu khi đang dùng) hoặc Time Stamp (cấp tem thời gian để xếp hàng trước sau) tránh việc 2 giao dịch cùng sửa 1 dữ liệu gây lỗi.

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
- **해시 (Hash)**: 임의의 길이 데이터를 고정된 길이의 값으로 변환(단방향). 무결성 검증 및 패스워드 암호화에 사용 (예: SHA-256, MD5).
- **솔트 (Salt)**: 암호화 전 원문에 덧붙이는 무작위 값. 동일한 패스워드라도 솔트가 다르면 해시값이 달라져 레인보우 테이블 공격을 방어합니다.

> **Vietnamese Explanation**: 
> **Mã hóa đối xứng (Private Key)**: Dùng chung 1 chìa khóa để khóa và mở (nhanh nhưng khó chia sẻ chìa khóa an toàn).
> **Mã hóa bất đối xứng (Public Key)**: Dùng khóa công khai để khóa, khóa bí mật để mở (chậm hơn nhưng an toàn). 
> **Hash (Băm)** là mã hóa 1 chiều (không dịch ngược được). **Salt (Muối)** là thêm chuỗi ngẫu nhiên vào mật khẩu trước khi băm để tăng độ khó.


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

## 침입 탐지 시스템 (IDS; Intrusion Detection System)
컴퓨터 시스템의 비정상적인 사용, 오용, 남용 등을 실시간으로 탐지하는 시스템.
- **오용 탐지 (Misuse Detection)**: 미리 입력해 둔 공격 패턴 감지 (시그니처 기반).
- **이상 탐지 (Anomaly Detection)**: 평균적인 상태를 기준으로 비정상 행위 감지 (행위 기반).
- **종류**:
  - **HIDS (Host-Based)**: 내부 시스템 감시 (OSSEC 등).
  - **NIDS (Network-Based)**: 외부로부터의 네트워크 트래픽 감시 (Snort 등).

## 리눅스의 커널 로그 (Linux Kernel Logs)
- `/var/log/wtmp`: 성공한 로그인/로그아웃 및 시스템 시작/종료 시간 기록.
- `/var/run/utmp`: 현재 로그인한 사용자의 상태 기록.
- `/var/log/btmp`: 실패한 로그인 기록.
- `/var/log/lastlog`: 마지막으로 성공한 로그인 기록.


## 네트워크 보안 기술 (Network Security Tech)
- **VPN (가상 사설 통신망)**: 공중 네트워크를 전용 회선처럼 사용할 수 있게 해주는 암호화 보안 솔루션.
- **SSH (시큐어 셸)**: 원격 로그인, 파일 복사 등을 안전하게 수행하는 프로토콜 (포트 22번 사용, 데이터 암호화 지원).


## 소프트웨어 생명주기 모델 (SDLC Models)
- **폭포수 모델 (Waterfall)**: 각 단계를 명확히 마무리한 후 다음 단계로 넘어가는 선형 순차적 모델 (요구사항 변경 어려움).
- **프로토타입 모델 (Prototyping)**: 시제품(Prototype)을 만들어 최종 결과물을 예측.
- **나선형 모델 (Spiral)**: 점진적으로 개발하며 **위험 분석(Risk Analysis)** 기능을 추가한 대형 프로젝트용 모델.
- **V 모델 (V Model)**: 폭포수 모델에 테스트 단계를 세부적으로 추가하여 검증을 강화한 모델.

> **Vietnamese Explanation**: 
> - **Waterfall (Thác nước)**: Làm xong bước này mới qua bước khác. 
> - **Prototyping (Mẫu thử)**: Làm một bản nháp cho khách hàng xem trước.
> - **Spiral (Xoắn ốc)**: Làm từng phần và liên tục đánh giá rủi ro (Risk analysis).
> - **V Model (Chữ V)**: Nhấn mạnh vào việc kiểm thử (Testing) ở mỗi giai đoạn tương ứng.


## 스토리지 시스템 (Storage Systems)
대용량 데이터를 저장하기 위한 장치 구성 방식.
- **DAS (Direct Attached Storage)**: 서버와 스토리지를 전용 케이블로 **직접 연결**.
- **NAS (Network Attached Storage)**: 서버와 스토리지를 **네트워크(LAN)**로 연결.
- **SAN (Storage Area Network)**: 스토리지 전용 **광 채널 네트워크(FC-SAN)**를 별도로 구성하여 고속 전송.

💡 **Mẹo ghi nhớ (Mnemonics):** 
- **DAS**: Direct (Cắm trực tiếp).
- **NAS**: Network (Qua mạng LAN).
- **SAN**: Area Network (Mạng quang riêng tốc độ cao).


## 소프트웨어 개발 보안 관련 법규
- **개인정보 보호법**: 개인정보 처리 및 보호에 관한 전반적 사항.
- **정보통신망법**: 정보통신망을 통한 개인정보 수집/이용 보호.
- **신용정보법**: 개인의 신용정보 취급 보호.
- **위치정보법**: 개인 위치정보 수집 및 제공 보호.



# ⦁ 보안 취약점 및 보안 기능 (Lỗ hổng bảo mật & Chức năng bảo mật)

## 1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)
- **개념**: 연속된 메모리 공간을 사용하는 프로그램에서 할당된 메모리의 범위를 넘어선 위치에서 자료를 읽거나 쓰려고 할 때 발생하는 취약점.
- **Tiếng Việt**: Lỗ hổng xảy ra khi chương trình ghi hoặc đọc dữ liệu vượt quá giới hạn vùng nhớ đã được cấp phát.
- **예시 (Example)**: 
  - (KR) 10바이트 공간에 20바이트의 데이터를 입력하면 다른 메모리 영역을 침범함.
  - (VN) Nhập 20 byte dữ liệu vào mảng chỉ có kích thước 10 byte, làm ghi đè lên các vùng nhớ khác.
- **대책**: 버퍼의 크기를 적절히 설정.
- 💡 **Mẹo ghi nhớ**: Buffer Overflow = Bơm nước quá đầy làm tràn ly.

## 2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)
- **개념**: 외부 입력값을 통해 시스템 명령어의 실행을 유도함으로써 권한을 탈취하거나 장애를 유발하는 취약점.
- **Tiếng Việt**: Chèn các lệnh hệ điều hành thông qua đầu vào của người dùng để thực thi trái phép trên server.
- **예시 (Example)**: 
  - (KR) 웹 입력창에 `; rm -rf /` 와 같은 명령어를 삽입하여 서버 파일을 삭제.
  - (VN) Chèn lệnh `; rm -rf /` vào ô input trên web để xoá file trên máy chủ.
- **대책**: 외부 입력값을 검증 없이 내부 명령어로 사용하지 않음.

## 3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)
- **개념**: 사용자가 자신의 의지와 무관하게 공격자가 의도한 행위를 특정 웹사이트에 요청하게 하는 취약점.
- **Tiếng Việt**: Lợi dụng phiên đăng nhập (session) hợp lệ của người dùng để thực hiện các yêu cầu không mong muốn.
- **예시 (Example)**: 
  - (KR) 로그인된 상태에서 공격자가 보낸 링크를 클릭하면 내 계정에서 몰래 송금이 됨.
  - (VN) Khi đang đăng nhập ngân hàng, lỡ click vào link của hacker thì bị tự động chuyển tiền.
- **대책**: GET 방식 대신 POST 방식 사용, CSRF 토큰 사용.
- 💡 **Mẹo ghi nhớ**: C-S-R-F = Cứ Sợ Rằng Fake (Sợ người dùng thật nhưng gửi request fake).

## 4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)
- **적절한 인증 없이 중요기능 허용 (Missing Authentication)**: 중대한 기능에 재인증이 없음. (Không yêu cầu xác thực lại khi làm việc quan trọng).
- **중요정보 평문 저장 및 전송 (Plaintext Storage/Transmission)**: 패스워드를 암호화 없이 저장/전송. (Lưu hoặc truyền mật khẩu không mã hóa).
- **하드코드된 비밀번호 (Hardcoded Password)**: 소스코드에 비밀번호를 직접 작성. (Ghi cứng mật khẩu trong source code).
- **오류 메시지 통한 정보 노출 (Information Exposure Through Error Message)**: 시스템 내부 구조나 파일 경로가 오류 메시지에 포함되어 노출됨. (Thông báo lỗi làm lộ đường dẫn nội mục hệ thống).
- **예시 (Example)**: 
  - (KR) DB 연결 실패 시 "root 계정 연결 실패" 같은 메시지를 띄우지 않고 "일시적인 오류입니다"로 대체.
  - (VN) Thay vì hiện lỗi "Không kết nối được tài khoản root", chỉ hiển thị "Lỗi hệ thống tạm thời".

---

# ⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)

## 1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)
- **개념**: 널 포인터(값이 없는 메모리 주소)가 가리키는 메모리에 값을 저장하거나 읽을 때 발생하는 오류.
- **Tiếng Việt**: Lỗi xảy ra khi cố gắng đọc/ghi dữ liệu thông qua con trỏ đang có giá trị Null.
- **예시 (Example)**: 
  - (KR) 객체가 생성되지 않았는데 그 객체의 메서드를 호출하여 시스템이 다운됨.
  - (VN) Gọi hàm của một đối tượng chưa được khởi tạo (bằng Null), làm app bị crash.

## 2. 자원 처리 오류 (Resource Handling Errors)
- **부적절한 자원 해제 (Improper Resource Release)**: 힙 메모리나 소켓을 사용 후 반환(close)하지 않아 자원 고갈 발생. (Không giải phóng bộ nhớ, kết nối sau khi dùng xong).
- **해제된 자원 사용 (Use After Free)**: 반환된 메모리를 다시 참조하여 오작동 유발. (Dùng lại vùng nhớ đã được giải phóng).
- **초기화되지 않은 변수 사용 (Uninitialized Variable)**: 변수 선언 후 값을 넣지 않고 사용하여 이전 쓰레기 값이 노출됨. (Dùng biến chưa khởi tạo giá trị).

## 3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)
- **개념**: 보안 문제로 금지된 함수 (예: C언어의 `strcpy`, `strcat`) 사용.
- **Tiếng Việt**: Sử dụng các hàm không an toàn, dễ gây lỗi tràn bộ đệm (như `strcpy`).
- **예시 (Example)**: 
  - (KR) 길이 제한이 없는 `strcpy()` 대신 길이를 지정하는 `strncpy()` 사용.
  - (VN) Dùng `strncpy()` (có giới hạn độ dài) thay cho `strcpy()` (copy không giới hạn).

---

# 106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)

## 1. 암호화 기본 개념 (Concepts)
- **평문 (Plain)**: Bản rõ (chưa mã hoá)
- **암호문 (Cipher)**: Bản mã (đã mã hoá)
- **치환 암호 (Substitution Cipher)**: 문자를 다른 문자로 대체 (Mã hoá thay thế, vd: A -> C).
- **전치 암호 (Transposition Cipher)**: 문자의 위치를 바꿈 (Mã hoá hoán vị, vd: ABC -> BCA).

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

# 108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)

## 1. 인증 기술 (Authentication Types)
- **지식 기반 (Knowledge)**: 알고 있는 것 (Mật khẩu, mã PIN).
- **소유 기반 (Possession)**: 가지고 있는 것 (Token, Smart Card, OTP).
- **생체 기반 (Biometric)**: 고유한 신체 특징 (Vân tay, mống mắt).
- **행위 기반 (Behavior)**: 행동 특징 (Chữ ký, dáng đi).

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

# 5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크

## 318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng phần mềm)
- **개념**: 검증된 소프트웨어의 일부를 다시 사용 (Sử dụng lại các phần mềm đã được kiểm chứng để giảm chi phí, tăng chất lượng).
- **방법**: 
  - **합성 중심 (Composition-Based)**: 블록 조립 (Lắp ráp các block như Lego).
  - **생성 중심 (Generation-Based)**: 추상적 명세로 코드 자동 생성 (Tự động sinh code từ bản đặc tả).

## 323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)
- **개념**: 통계 공식을 활용한 비용 예측 기법 (Dự toán chi phí dựa trên công thức toán học).
- **종류**:
  - **COCOMO**: LOC(라인 수) 기반 (Dựa vào số dòng code).
  - **Putnam**: 시간에 따른 인력 분포 곡선(Rayleigh-Norden) 활용 (Dựa vào đường cong phân bổ nhân lực).
  - **FP (Function Point)**: 입력, 출력, 인터페이스 등 기능적 요인 기반 (Dựa vào điểm chức năng).

## 336. 소프트웨어 개발 프레임워크 (Software Development Framework)
- **개념**: 개발에 공통 사용되는 구조를 제공하여 생산성을 높이는 기반.
- **특성**: 모듈화, 재사용성, 확장성, **제어의 역흐름(IoC)**.
- **Tiếng Việt**: Nền tảng cấu trúc sẵn giúp tăng năng suất (như Spring, .NET). Đặc tính: Module hóa, Tái sử dụng, Mở rộng, Đảo ngược luồng điều khiển (IoC).


