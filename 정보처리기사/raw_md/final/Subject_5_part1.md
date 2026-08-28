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
