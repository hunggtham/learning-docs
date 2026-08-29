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

