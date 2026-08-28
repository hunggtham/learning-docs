
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

