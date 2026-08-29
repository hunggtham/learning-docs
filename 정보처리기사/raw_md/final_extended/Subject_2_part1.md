# 2과목: 소프트웨어 개발 (Software Development)

## 1. 자료 구조의 분류 (Classification of Data Structures)
* **선형 구조 (Linear Structure)**: 배열(Array), 선형 리스트(Linear List), 스택(Stack), 큐(Queue), 데크(Deque)
* **비선형 구조 (Non-linear Structure)**: 트리(Tree), 그래프(Graph)
* **방향/무방향 그래프의 최대 간선 수 (Maximum edges in graphs)**:
  * 무방향 그래프 (Undirected Graph): n(n-1)/2
  * 방향 그래프 (Directed Graph): n(n-1)
* **Vietnamese**:
  * Cấu trúc tuyến tính: Mảng, danh sách tuyến tính, ngăn xếp, hàng đợi, hàng đợi hai đầu.
  * Cấu trúc phi tuyến: Cây, Đồ thị.
  * Số cạnh tối đa: Đồ thị vô hướng là n(n-1)/2, có hướng là n(n-1).
* **Example**: 노드가 4개인 무방향 그래프의 최대 간선 수는 4(4-1)/2 = 6개입니다. (Với đồ thị vô hướng có 4 đỉnh, số cạnh tối đa là 6).
* 💡 **Mẹo ghi nhớ**: Tuyến tính (Linear) là một đường thẳng (Mảng, Stack, Queue). Phi tuyến là rẽ nhánh (Cây, Đồ thị).

## 2. 스택 (Stack) 및 응용 (Applications)
* 리스트의 한쪽 끝으로만 자료의 삽입, 삭제 작업이 이루어지는 자료 구조.
* 가장 나중에 삽입된 자료가 가장 먼저 삭제되는 후입선출(**LIFO**, Last-In First-Out) 방식.
* **응용 분야 (Applications)**: 인터럽트 처리 (Interrupt handling), 수식 계산 및 표기법 (Expression evaluation), 서브루틴 호출 및 복귀 주소 저장 (Subroutine calls).
* **삽입/삭제 (Push/Pop)**: `PUSH`는 자료 입력, `POP`은 자료 출력.
* **Vietnamese**:
  * Stack là cấu trúc dữ liệu LIFO, thêm/xóa dữ liệu ở một đầu.
  * Ứng dụng: Xử lý ngắt, tính toán biểu thức, lưu địa chỉ khi gọi hàm.
* **Example**: 브라우저의 '뒤로 가기' 버튼은 스택 구조를 사용합니다. (Nút "Back" trên trình duyệt sử dụng cấu trúc stack).
* 💡 **Mẹo ghi nhớ**: LIFO - Vào sau ra trước, giống như xếp đĩa, lấy đĩa trên cùng ra trước.

## 3. 트리 (Tree)
* 정점(Node)과 선분(Branch)을 이용하여 사이클을 이루지 않도록 구성한 그래프의 특수한 형태.
* **디그리 (Degree, 차수)**: 각 노드에서 뻗어 나온 가지의 수.
* **단말 노드 (Terminal Node) = 잎 노드 (Leaf Node)**: 자식이 하나도 없는 노드, 즉 디그리가 0인 노드.
* **Vietnamese**:
  * Cây là đồ thị đặc biệt không có chu trình.
  * Bậc (Degree): Số nhánh của một nút con.
  * Nút lá (Leaf): Nút không có con (bậc = 0).
* **Example**: 폴더 구조에서 하위 폴더가 없는 폴더가 단말 노드입니다. (Trong cấu trúc thư mục, thư mục không chứa thư mục con là nút lá).
* 💡 **Mẹo ghi nhớ**: Degree là số con trực tiếp. Leaf là chiếc lá ở cuối cành không mọc thêm được nữa.

## 4. 이진 트리의 운행법 (Binary Tree Traversal)
* **Preorder (전위)**: Root → Left → Right
* **Inorder (중위)**: Left → Root → Right
* **Postorder (후위)**: Left → Right → Root
* **Vietnamese**:
  * Preorder: Gốc -> Trái -> Phải.
  * Inorder: Trái -> Gốc -> Phải.
  * Postorder: Trái -> Phải -> Gốc.
* **Example**: 수식 `A + B`를 전위 표기하면 `+ A B`, 중위 표기하면 `A + B`, 후위 표기하면 `A B +`가 됩니다.
* 💡 **Mẹo ghi nhớ**: Tiền/Trung/Hậu tố chỉ vị trí của Root (Gốc) so với Trái/Phải.

## 5. 수식의 표기법 변환 (Expression Notation Conversion)
* **Infix → Prefix**: 연산자를 피연산자 두 개의 **앞(왼쪽)**으로 이동.
* **Infix → Postfix**: 연산자를 피연산자 두 개의 **뒤(오른쪽)**로 이동.
* **Postfix → Infix**: 연산자를 피연산자 두 개의 **가운데**로 이동.
* **Vietnamese**: Chuyển đổi biểu thức Infix sang Prefix (đưa toán tử ra trước) và Postfix (đưa toán tử ra sau).
* **Example**: Infix `A/B` -> Postfix `A B /` -> Prefix `/ A B`.
* 💡 **Mẹo ghi nhớ**: Prefix (Pre = trước), Postfix (Post = sau).

## 6. 정렬 알고리즘 (Sorting Algorithms)
* **삽입 정렬 (Insertion Sort)**: 두 번째 값부터 시작해 앞의 값들과 비교하여 알맞은 위치에 삽입.
* **선택 정렬 (Selection Sort)**: 가장 작은 값을 선택해 첫 번째와 교환, 그 다음 작은 값을 두 번째와 교환하는 방식.
* **버블 정렬 (Bubble Sort)**: 인접한 두 값을 비교하여 큰 값을 뒤로 보내는 과정을 반복.
* **Vietnamese**:
  * Insertion: Chèn phần tử vào đúng vị trí của dãy đã sắp xếp.
  * Selection: Chọn phần tử nhỏ nhất đưa lên đầu.
  * Bubble: Nổi bọt, so sánh 2 phần tử kề nhau, lớn hơn thì đổi chỗ.
* **Example**: `8, 5, 6` 버블 정렬 1회전: 5, 8, 6 -> 5, 6, 8. (Bubble sort đổi chỗ 8 và 5, rồi 8 và 6).
* 💡 **Mẹo ghi nhớ**: Insertion: bốc bài và chèn. Selection: tìm người lùn nhất xếp hàng. Bubble: bong bóng lớn nổi lên cuối cùng.

## 7. 이분 검색 (Binary Search)
* 검색할 데이터가 정렬되어 있어야 함.
* 비교 횟수를 거듭할 때마다 검색 대상이 반(절반)으로 줄어듦.
* 탐색 효율이 좋고 시간이 적게 소요됨. 중간 레코드 번호(M) = (F+L)/2.
* **Vietnamese**: Tìm kiếm nhị phân. Dữ liệu phải được sắp xếp trước. Mỗi lần chia đôi không gian tìm kiếm.
* **Example**: 사전에서 단어를 찾을 때 책을 반으로 계속 쪼개며 찾는 방식입니다.
* 💡 **Mẹo ghi nhớ**: Binary = chia đôi (phải sắp xếp trước!).

## 8. 주요 해싱 함수 (Hashing Functions)
* **제산법 (Division)**: 키 값을 소수(Prime)로 나눈 나머지를 주소로 사용.
* **제곱법 (Mid-Square)**: 키 값을 제곱한 후 중간 부분의 값을 주소로 사용.
* **폴딩법 (Folding)**: 키 값을 여러 부분으로 나눈 후 더하거나 XOR한 값을 주소로 사용.
* **숫자 분석법 (Digit Analysis)**: 숫자의 분포를 분석해 고른 자리를 주소로 사용.
* **Vietnamese**: Các hàm băm (Hashing) giúp ánh xạ khóa (key) thành địa chỉ. Division (chia lấy dư), Mid-Square (bình phương lấy giữa), Folding (gấp/cộng các phần), Digit Analysis (phân tích chữ số).
* **Example**: 제산법으로 키 10을 해시 테이블 크기 7(소수)로 나누면 나머지 3이 주소가 됩니다.
* 💡 **Mẹo ghi nhớ**: Division = Chia lấy dư, Square = Bình phương, Fold = Gấp lại.

## 9. 스키마 3계층 (Three-Schema Architecture)
* **외부 스키마 (External Schema)**: 사용자나 프로그래머 입장에서 필요한 논리적 구조.
* **개념 스키마 (Conceptual Schema)**: 전체적인 논리적 구조, 개체 간 관계/제약조건, 보안/무결성 규칙.
* **내부 스키마 (Internal Schema)**: 물리적 저장장치 입장에서 본 구조 (레코드 형식, 물리적 순서).
* **Vietnamese**:
  * External: Góc nhìn của người dùng (User view).
  * Conceptual: Cấu trúc logic tổng thể, quan hệ, bảo mật.
  * Internal: Cấu trúc lưu trữ vật lý.
* **Example**: DB의 전체 테이블 구조는 개념 스키마, 사용자가 보는 뷰(View)는 외부 스키마, 파일 저장 방식은 내부 스키마.
* 💡 **Mẹo ghi nhớ**: Ngoài (Người dùng) - Giữa/Khái niệm (Tổng thể logic) - Trong (Lưu trữ vật lý).

## 10. 빌드 자동화 도구 (Build Automation Tools)
* **Ant**: 아파치 소프트웨어 재단에서 개발.
* **Maven**: Ant의 대안.
* **Jenkins**: JAVA 기반의 오픈 소스 빌드 자동화 도구.
* **Gradle**: Groovy 기반의 오픈 소스 빌드 자동화 도구.
* **Vietnamese**: Các công cụ tự động hóa quá trình build phần mềm (biên dịch, đóng gói).
* **Example**: 개발자가 코드를 수정하면 Jenkins가 자동으로 빌드와 테스트를 실행합니다.
* 💡 **Mẹo ghi nhớ**: AMJG (Ant, Maven, Jenkins, Gradle).

## 11. DRM (디지털 저작권 관리, Digital Rights Management)
* **구성 요소 (Components)**: 클리어링 하우스 (Clearing House - 권한/결제 관리), 콘텐츠 제공자 (Contents Provider), 패키저 (Packager - 암호화), 콘텐츠 분배자 (Distributor), DRM 컨트롤러 (Controller - 이용 권한 통제).
* **기술 요소 (Technologies)**: 암호화 및 키 관리, 식별체계 표현, 라이선스 발급, 정책 관리, 크랙 방지.
* **Vietnamese**: Quản lý bản quyền kỹ thuật số. Clearing House xử lý thanh toán/cấp phép. Packager mã hóa nội dung.
* **Example**: 넷플릭스 영상이 녹화가 안 되거나 불법 복제가 안 되는 것이 DRM 기술 덕분입니다.
* 💡 **Mẹo ghi nhớ**: Clearing House = Ngân hàng/Trung tâm kiểm duyệt. Packager = Người đóng gói/Mã hóa.

## 12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)
* **패키징 (Packaging)**: 모듈별 실행 파일들을 묶어 배포용 설치 파일을 만드는 것. 사용자 중심으로 진행하며 보안(암호화, DRM 연동) 고려.
* **설치 매뉴얼 (Installation Manual)**: 사용자를 기준으로 작성. 기본 사항, 소프트웨어 개요, 설치 파일, 프로그램 삭제 등 포함.
* **Vietnamese**:
  * Packaging: Đóng gói các file thực thi thành file cài đặt (hướng đến người dùng cuối).
  * Manual: Tài liệu hướng dẫn cài đặt viết cho người dùng, bao gồm cách cài và gỡ.
* **Example**: `.exe` 설치 파일을 만들고, "다음, 다음, 완료"를 설명하는 설명서를 작성하는 과정입니다.

## 13. 형상 관리 (SCM - Software Configuration Management)
* 변경 사항을 관리하기 위해 개발된 일련의 활동. 목적: 개발 비용 감소, 방해 요인 최소화.
* **도구 (Tools)**: Git, CVS, Subversion(SVN).
* **주요 기능 (Key Functions)**:
  * **Check-Out**: 저장소에서 파일을 받아옴.
  * **Check-In**: 수정을 완료한 후 저장소에 새로운 버전으로 갱신.
  * **Commit**: 갱신 시 충돌을 알리고 수정한 후 완료함.
* **Vietnamese**: Quản lý cấu hình phần mềm (quản lý thay đổi/version).
  * Check-out: Lấy file về.
  * Check-in: Lưu file lên.
  * Commit: Lưu thay đổi (xử lý xung đột nếu có).
* **Example**: Git에서 코드를 가져오는 것이 Checkout, 수정 후 서버에 올리는 것이 Commit/Check-in입니다.
* 💡 **Mẹo ghi nhớ**: In = vào kho, Out = ra khỏi kho.

## 14. 파레토 법칙 (Pareto Principle)
* 소프트웨어 테스트에서 오류의 80%는 전체 모듈의 20% 내에서 발견된다는 법칙.
* **Vietnamese**: Nguyên lý 80/20. 80% lỗi nằm trong 20% module cốt lõi.
* **Example**: 시스템에 10개의 모듈이 있다면, 대부분의 버그는 핵심 모듈 2개에 몰려있습니다.
* 💡 **Mẹo ghi nhớ**: Pareto = 80/20.

## 15. 화이트박스 vs 블랙박스 테스트 (White-box vs Black-box Testing)
* **화이트박스 테스트**: 원시 코드를 오픈시킨 상태에서 논리적 경로(제어 구조)를 테스트.
  * **종류**: 기초 경로 검사 (Base Path), 제어 구조 검사 (조건, 루프, 데이터 흐름).
* **블랙박스 테스트**: 기능이 제대로 작동하는지 외부에서 테스트 (내부 구조 안 봄).
  * **종류**: 동치 분할 (Equivalence Partitioning), 경계값 분석 (Boundary Value), 원인-효과 그래프 (Cause-Effect), 오류 예측 (Error Guessing), 비교 검사 (Comparison).
* **Vietnamese**:
  * White-box: Nhìn thấy code bên trong (kiểm tra đường dẫn, vòng lặp).
  * Black-box: Không nhìn thấy code, chỉ kiểm tra đầu vào/đầu ra (kiểm tra tính năng).
* **Example**: 화이트박스는 코드의 `if-else` 모든 경로를 실행해보는 것이고, 블랙박스는 로그인 창에 ID/PW를 넣어보는 것입니다.
* 💡 **Mẹo ghi nhớ**: White = Nhìn xuyên thấu (Code). Black = Hộp đen không thấy ruột (Chức năng).

## 16. 소프트웨어 테스트 단계 (Software Testing Phases)
* **단위 테스트 (Unit Test)**: 코딩 직후 최소 단위인 모듈/컴포넌트 테스트. (알고리즘 오류, 탈출구 없는 반복문 등 발견).
* **통합 테스트 (Integration Test)**:
  * 하향식 (Top-down): 상위에서 하위로 (스텁/Stub 사용).
  * 상향식 (Bottom-up): 하위에서 상위로 (드라이버/Driver 사용).
* **인수 테스트 (Acceptance Test)**: 사용자가 시스템을 수락하기 전 수행.
  * **알파 테스트**: 개발자 앞에서 사용자가 수행.
  * **베타 테스트 (Field Testing)**: 최종 사용자가 실제 환경에서 여러 사용자 앞에서 수행.
* **Vietnamese**:
  * Unit Test: Kiểm thử từng module nhỏ (tìm lỗi thuật toán, lặp vô hạn).
  * Integration Test: Kiểm thử tích hợp. Top-down (từ trên xuống), Bottom-up (từ dưới lên).
  * Acceptance Test: Kiểm thử chấp nhận. Alpha (cùng dev), Beta (không có dev, real-world).
* **Example**: 게임 개발 후 회사 내부에서 해보는 것이 알파 테스트, 유저들에게 먼저 공개하는 것이 오픈 베타 테스트입니다.
* 💡 **Mẹo ghi nhớ**: Alpha = có người tạo ra (Dev) giám sát. Beta = thả ra tự nhiên cho User.

## 17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)
* **테스트 오라클 (Test Oracle)**: 테스트 결과가 참인지 판단하기 위해 사전에 정의된 참 값을 대입하여 비교. (참, 샘플링, 추정, 일관성 검사 오라클).
* **테스트 드라이버 (Test Driver)**: (상향식 테스트에서) 하위 모듈을 호출하고 매개 변수를 전달하여 결과를 도출하는 도구. (가짜 메인 프로그램).
* **Vietnamese**:
  * Test Oracle: Cơ chế/Nguồn chân lý để xác định kết quả đúng hay sai.
  * Test Driver: Chương trình giả lập gọi module con (dùng trong Bottom-up).
* **Example**: 테스트 오라클은 정답지 역할을 합니다.
* 💡 **Mẹo ghi nhớ**: Oracle = Nhà tiên tri/Chân lý. Driver = Người lái xe (Gọi cấp dưới).

## 18. 최악의 시간 복잡도 (Worst-case Time Complexity)
* **O(1)**: 입력값 크기에 관계 없이 일정. (스택 삽입/삭제).
* **O(n log n)**: n log n번 수행. (힙 정렬, 병합 정렬).
* **Vietnamese**: Độ phức tạp thời gian. O(1) là hằng số, O(n log n) cho Heap/Merge sort.
* **Example**: 데이터가 아무리 많아도 스택의 최상단에 값을 넣는 것은 1번의 연산만 필요하므로 O(1)입니다.

## 19. 클린 코드 작성 원칙 (Clean Code Principles)
* **가독성 (Readability)**: 누구든지 코드를 쉽게 읽을 수 있도록 작성.
* **단순성 (Simplicity)**: 코드를 간단하게 작성.
* **Vietnamese**: Nguyên tắc viết code sạch. Dễ đọc, đơn giản.
* **Example**: 변수 이름을 `a` 대신 `userCount`로 짓는 것이 가독성을 높이는 것입니다.



## 20. 하향식 통합 테스트와 테스트 스텁 (Top-down Integration Test & Test Stub)
* **테스트 스텁 (Test Stub)**: 상향식에서 드라이버를 쓰듯, 하향식 통합 테스트에서는 '스텁(Stub)'이라는 가짜 하위 모듈을 사용.
* 의존성 배제 및 중복성 최소화.
* 일시적으로 필요한 조건만을 가지고 있는 시험용 모듈.
* **Vietnamese**: Test Stub là module giả lập cấp dưới, dùng trong kiểm thử tích hợp từ trên xuống (Top-down).
* **Example**: 로그인 기능을 먼저 테스트하기 위해, DB 연결 모듈 대신 무조건 "성공"을 반환하는 스텁을 만듭니다.
* 💡 **Mẹo ghi nhớ**: Top-down dùng Stub (T-S), Bottom-up dùng Driver (B-D).

## 21. 외계인 코드 (Alien Code)
* 아주 오래되거나 참고문서/개발자가 없어 유지보수 작업이 어려운 코드.
* **Vietnamese**: Alien Code là mã nguồn quá cũ, không có tài liệu hoặc người phát triển gốc, rất khó bảo trì.
* **Example**: 20년 전에 퇴사한 직원이 주석 없이 짠 코드가 외계인 코드입니다.
* 💡 **Mẹo ghi nhớ**: Alien = Người ngoài hành tinh, đọc không hiểu gì cả.

## 22. 정적 분석 도구 (Static Analysis Tools)
* 코드를 실행하지 않고(하드웨어/소프트웨어적으로) 소스 코드 품질을 분석하는 도구.
* **종류**: pmd, checkstyle, cppcheck 등.
* **Vietnamese**: Công cụ phân tích tĩnh, phân tích source code mà không cần chạy chương trình.
* **Example**: 코딩 표준을 잘 지켰는지 검사하는 Checkstyle.

## 23. EAI 구축 유형 (Enterprise Application Integration Types)
* **Point-to-Point**: 애플리케이션을 1:1로 직접 연결.
* **Hub & Spoke**: 단일 접점인 허브 시스템을 통해 데이터를 전송하는 중앙 집중형 방식.
* **Message Bus (ESB 방식)**: 애플리케이션 사이에 미들웨어를 두어 처리하는 방식.
* **Hybrid**: Hub & Spoke와 Message Bus의 혼합 방식.
* **Vietnamese**: Các kiểu kiến trúc tích hợp hệ thống (EAI).
  * Point-to-Point: Nối 1-1.
  * Hub & Spoke: Tập trung qua 1 Hub trung tâm.
  * Message Bus: Dùng middleware (trục thông điệp).
  * Hybrid: Lai giữa Hub & Spoke và Message Bus.
* **Example**: 여러 부서의 시스템을 가운데 중앙 서버 하나(Hub)를 통해 연결하는 방식이 Hub & Spoke입니다.
* 💡 **Mẹo ghi nhớ**: Hub là cái trục xe đạp (trung tâm), Spoke là nan hoa (tỏa ra xung quanh).

## 24. 인터페이스 보안 - 네트워크 영역 (Interface Security - Network Area)
* 네트워크 트래픽에 대한 암호화 설정.
* **방식**: IPSec, SSL, S-HTTP 등.
* **Vietnamese**: Bảo mật giao diện vùng mạng (mã hóa lưu lượng). Dùng IPSec, SSL, S-HTTP.
* **Example**: 웹사이트 주소가 `https://`로 시작하면 SSL이 적용된 것입니다.

## 25. 트립와이어 (tripwire)
* 크래커가 침입하여 백도어를 만들어 놓거나, 설정 파일을 변경했을 때 분석하는 데이터 무결성 검사 도구.
* **Vietnamese**: Công cụ kiểm tra tính toàn vẹn dữ liệu, phát hiện backdoor hoặc thay đổi file cấu hình.
* 💡 **Mẹo ghi nhớ**: Tripwire = Dây bẫy, chạm vào là báo động.

## 26. 인터페이스 구현 검증 도구 (Interface Verification Tools)
* **xUnit**: 다양한 언어에 적용되는 단위 테스트 프레임워크 (JUnit, CppUnit, NUnit).
* **STAF**: 서비스 호출 및 컴포넌트 재사용 등 다양한 환경 지원.
* **FitNesse**: 웹 기반 테스트 케이스 설계, 실행, 결과 확인.
* **NTAF**: FitNesse와 STAF의 장점을 통합한 NHN(Naver)의 테스트 자동화 프레임워크.
* **watir**: Ruby 기반 웹 애플리케이션 테스트 프레임워크.
* **Vietnamese**: Các công cụ kiểm thử giao diện. xUnit (kiểm thử đơn vị), STAF, FitNesse (Web), NTAF (Naver), watir (Ruby).
* 💡 **Mẹo ghi nhớ**: xUnit là phổ biến nhất cho Unit Test. NTAF có chữ N (Naver).

## 27. JSON 및 AJAX (JSON & AJAX)
* **JSON (JavaScript Object Notation)**: 속성-값 쌍(Attribute-Value Pairs)으로 이루어진 데이터 객체를 전달하기 위한 개방형 표준 포맷. 사람이 읽기 쉬움.
* **AJAX (Asynchronous JavaScript and XML)**: 자바스크립트를 이용한 비동기 통신 기술. 클라이언트-서버 간 XML(또는 JSON) 데이터를 교환 및 제어.
* **Vietnamese**:
  * JSON: Định dạng dữ liệu dạng Key-Value dễ đọc.
  * AJAX: Công nghệ giao tiếp bất đồng bộ, tải dữ liệu mà không cần tải lại toàn bộ trang.
* **Example**: 좋아요 버튼을 눌렀을 때 페이지 이동 없이 하트가 채워지는 것이 AJAX 기술입니다.

## 28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)
* 앞서 배운 선형 리스트는 두 가지로 나뉩니다.
* **연속 리스트 (Contiguous List - 예: 배열)**:
  * 연속되는 기억장소에 저장. 기억장소 이용 효율 밀도가 1(가장 좋음).
  * 중간에 데이터를 삽입/삭제 시 자료의 이동이 필요(오버헤드 발생).
* **연결 리스트 (Linked List)**:
  * 임의의 기억공간에 저장하며, 포인터(링크)를 이용해 서로 연결.
  * 노드의 삽입/삭제가 용이. 순차 리스트에 비해 기억 공간 이용 효율은 낮고, 포인터를 찾는 시간 때문에 접근 속도가 느림.
  * 중간 노드가 끊어지면 다음 노드를 찾기 힘듦.
* **오버플로/언더플로 (Overflow/Underflow)**: 스택/리스트가 꽉 찬 상태에서 삽입하면 Overflow, 빈 상태에서 삭제하면 Underflow 발생.
* **Vietnamese**:
  * Contiguous List (Mảng): Dữ liệu lưu liên tiếp. Chèn/Xóa chậm do phải dịch chuyển dữ liệu. Mật độ = 1.
  * Linked List (Danh sách liên kết): Dữ liệu lưu rải rác, nối bằng pointer. Chèn/Xóa nhanh, nhưng truy cập chậm.
* 💡 **Mẹo ghi nhớ**: Array = Nhà chung cư sát vách. Linked List = Các nhà rải rác nhưng có bản đồ chỉ đường đến nhà tiếp theo.

## 29. 큐 (Queue)
* 삽입은 한쪽 끝에서, 삭제는 반대쪽 끝에서 이루어지는 자료 구조.
* 선입선출(**FIFO**, First-In First-Out) 방식.
* 시작과 끝을 표시하는 두 개의 포인터(Front, Rear)가 있음.
* **Vietnamese**: Hàng đợi FIFO (Vào trước ra trước). Dùng 2 con trỏ chỉ vị trí đầu và cuối.
* **Example**: 프린터의 인쇄 대기열이나 매표소 줄서기와 같습니다.
* 💡 **Mẹo ghi nhớ**: Queue = Xếp hàng.

## 30. 트리 구조 추가 용어 (Tree Terminology Additional)
* **자식 노드 (Son Node)**: 어떤 노드에 연결된 다음 레벨의 노드들.
* **부모 노드 (Parent Node)**: 어떤 노드에 연결된 이전 레벨의 노드.
* **형제 노드 (Sibling / Brother Node)**: 동일한 부모를 갖는 노드들.
* **트리의 디그리 (Degree of a Tree)**: 전체 노드들의 디그리(자식 수) 중에서 가장 큰 값.
* **Vietnamese**:
  * Son Node: Nút con.
  * Parent Node: Nút cha.
  * Sibling: Nút anh em (cùng cha).
  * Degree of Tree: Bậc lớn nhất trong tất cả các nút của cây.



## 31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)
* **퀵 정렬 (Quick Sort)**: 키를 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽 서브파일로 분해시키는 방식. 분할(Divide)과 정복(Conquer)을 통해 자료를 정렬. 
  * 평균 시간 복잡도: O(n log n), 최악: O(n^2).
* **2-Way 합병 정렬 (Merge Sort)**: 정렬되어 있는 두 개의 파일을 한 개의 파일로 합병하는 방식. 평균/최악 모두 O(n log n).
* **힙 정렬 (Heap Sort)**: 전이진 트리(Complete Binary Tree)를 이용한 정렬 방식. 평균/최악 모두 O(n log n).
* **Vietnamese**: Các thuật toán sắp xếp bổ sung:
  * Quick Sort: Chia để trị (Divide & Conquer), dùng chốt (pivot).
  * Merge Sort: Trộn 2 mảng đã sắp xếp.
  * Heap Sort: Dùng cây nhị phân hoàn chỉnh.
* **Example**: 퀵 정렬은 반장(기준)을 뽑아서 키 작은 사람은 왼쪽, 큰 사람은 오른쪽으로 세우는 방식입니다.
* 💡 **Mẹo ghi nhớ**: Quick = Nhanh nhưng rủi ro (worst case O(n^2)). Merge/Heap = Luôn ổn định O(n log n).

## 32. 추가 해싱 함수 (Additional Hashing Functions)
* **기수 변환법 (Radix)**: 키 숫자의 진수를 다른 진수로 변환.
* **대수적 코딩법 (Algebraic Coding)**: 다항식의 계수로 간주하여 나눈 나머지 사용.
* **무작위법 (Random)**: 난수를 발생시켜 홈 주소로 사용.
* **Vietnamese**: Các hàm băm khác: Cơ số (Radix), Đại số (Algebraic), Ngẫu nhiên (Random).

## 33. DBMS (데이터베이스 관리 시스템)
* 사용자와 데이터베이스 사이에서 정보를 생성하고 데이터베이스를 관리해 주는 소프트웨어.
* **필수 기능 3가지**:
  * **정의 기능 (Definition)**: 데이터 형, 구조, 제약조건 등 명시.
  * **조작 기능 (Manipulation)**: 데이터 검색, 갱신, 삽입, 삭제(인터페이스 제공).
  * **제어 기능 (Control)**: 데이터 무결성 유지, 보안, 정확성 제어.
* **장점**: 데이터 중복 최소화, 독립성 보장, 일관성/무결성/보안 유지, 실시간 처리.
* **단점**: 전문가 부족, 전산화 비용 증가, 과부하 발생 시 백업/회복 어려움, 시스템 복잡.
* **Vietnamese**: Hệ quản trị CSDL.
  * 3 chức năng: Định nghĩa (Cấu trúc), Thao tác (Thêm/Sửa/Xóa/Tìm), Điều khiển (Bảo mật, toàn vẹn).
  * Ưu điểm: Giảm trùng lặp, nhất quán. Nhược điểm: Tốn kém, phức tạp.
* **Example**: Oracle, MySQL 등이 대표적인 DBMS입니다.
* 💡 **Mẹo ghi nhớ**: Đ-T-Đ (Định nghĩa, Thao tác, Điều khiển) = D-M-C (Define, Manipulate, Control).

## 34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)
* **단위 모듈 (Unit Module)**: 한 가지 동작을 수행하는 기능 모듈 (독립적인 컴파일 가능).
* **IPC (프로세스 간 통신)**: 복수의 프로세스 간 통신을 구현하는 방법.
* **IPC 대표 메소드**:
  * **Shared Memory**: 다수 프로세스가 공유 가능한 메모리 구성.
  * **Socket**: 네트워크 소켓을 이용한 통신.
  * **Semaphores**: 공유 자원에 대한 접근 제어.
  * **Pipes & Named Pipes**: 선입선출(FIFO) 형태의 공유 메모리 사용.
  * **Message Queueing**: 메시지 전달 방식.
* **Vietnamese**: Giao tiếp giữa các tiến trình (IPC). Các phương thức: Bộ nhớ chia sẻ, Socket (mạng), Cờ hiệu (Semaphore), Ống dẫn (Pipes), Hàng đợi tin nhắn.
* **Example**: 두 개의 프로그램이 채팅을 주고받을 때 Socket이나 Message Queue를 사용합니다.
* 💡 **Mẹo ghi nhớ**: S-S-S-P-M (Shared memory, Socket, Semaphore, Pipe, Message Queue).

## 35. 테스트 케이스 (Test Case)
* 사용자의 요구사항을 정확하게 준수했는지 확인하기 위해 설계된 테스트 항목에 대한 명세서.
* **구성 요소 (ISO/IEC/IEEE 29119-3)**: 
  * 식별자, 테스트 항목, 입력 명세(Input), 출력 명세(Output/예상 결과), 환경 설정, 특수 절차 요구, 의존성 기술.
* **Vietnamese**: Kịch bản kiểm thử (Test Case). Bao gồm: ID, Môi trường, Đầu vào, Đầu ra mong đợi.
* **Example**: 로그인 기능을 위해 "ID: admin, PW: 1234를 넣었을 때 관리자 페이지로 넘어가는가?"를 문서화한 것입니다.

## 36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)
* **IDE**: 코딩, 디버그, 컴파일, 배포 등 모든 작업을 하나의 프로그램에서 처리.
  * **기능**: 코딩(Coding), 컴파일(Compile), 디버깅(Debugging), 배포(Deployment).
* **빌드 도구**: 소스 코드를 실행 가능한 제품 소프트웨어로 변환(Ant, Maven, Gradle).
* **Vietnamese**: Môi trường phát triển tích hợp (IDE - như Eclipse, VS Code). Chức năng: Code, Dịch, Gỡ lỗi, Triển khai.

## 37. 소프트웨어 패키징 고려사항 추가 (Packaging Considerations)
* 사용자의 시스템 최소 환경(OS, CPU, 메모리) 정의.
* UI(시각적 자료) 매뉴얼과 일치.
* 하드웨어와 함께 관리되도록 Managed Service 형태로 제공 고려.
* 제품 종류에 적합한 암호화 알고리즘 및 DRM 연동 고려.
* **Vietnamese**: Các lưu ý khi đóng gói phần mềm: Yêu cầu hệ thống tối thiểu, Giao diện (UI) khớp với hướng dẫn, Quản lý dịch vụ, Mã hóa/DRM.

## 38. 릴리즈 노트 (Release Note)
* 소프트웨어 배포(릴리즈) 정보를 최종 사용자와 공유하기 위한 문서 (초기/추가 배포 시 제공).
* 개발팀에서 직접 현재 시제로 정확한 완전한 정보를 기반으로 작성.
* **항목**: 머릿말(Header), 개요, 목적, 문제 요약, 재현 항목, 수정/개선 내용, 사용자 영향도, SW 지원 영향도, 면책 조항 등.
* **Vietnamese**: Ghi chú phát hành. Chia sẻ thông tin cập nhật, lỗi đã sửa cho người dùng.
* **Example**: 앱스토어에서 앱 업데이트 시 적혀있는 "새로운 기능 및 버그 수정" 목록이 릴리즈 노트입니다.
* 💡 **Mẹo ghi nhớ**: Release Note = Nhật ký cập nhật phần mềm.

## 39. DRM 패키징 과정 상세 (DRM Packaging Process)
* 디지털 콘텐츠 배포 시, 아날로그는 디지털로 변환 후 패키저가 패키징.
* 용량이 작으면 실시간 패키징, 크면 미리 패키징 후 배포.
* 암호화된 저작권자 전자서명 포함, 라이선스는 클리어링 하우스에 등록.
* **Vietnamese**: Quy trình đóng gói DRM. Nội dung nhỏ thì đóng gói realtime, lớn thì đóng gói trước. Giấy phép lưu tại Clearing House.



## 40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)
* **형상 관리 (SCM)**: 소프트웨어 개발 과정에서 변경 사항을 관리하는 일련의 활동.
  * **기능**: 형상 식별, 버전 제어, 형상 통제(변경 관리), 형상 감사, 형상 기록.
* **버전 관리 방식 3가지**:
  1. **공유 폴더 방식 (Shared Folder)**: 로컬 공유 폴더에 저장. (SCCS, RCS 등).
  2. **클라이언트/서버 방식 (C/S)**: 중앙 서버에 저장하여 관리. (CVS, SVN 등). 
     * **SVN (Subversion)**: `trunk`에서 주로 개발, `branches`에서 추가 작업 후 병합(merge). 커밋 시 리비전(Revision) 1씩 증가.
  3. **분산 저장소 방식 (Distributed)**: 로컬 저장소와 원격 저장소에 함께 저장. (Git 등).
     * **Git**: 로컬에서 버전 관리가 가능해 빠르고 네트워크 문제 시에도 작업 가능. 스냅샷(Snapshot)으로 파일 변화를 저장.
* **주요 기능**: Repository, Import, Check-Out(가져오기), Check-In/Commit(반영), Update(동기화).
* **Vietnamese**: Quản lý cấu hình (SCM) và các cách quản lý phiên bản.
  * Shared Folder: Lưu ở thư mục chung.
  * C/S: Lưu ở server trung tâm (SVN).
  * Distributed: Lưu phân tán cả local và server (Git). Git dùng Snapshot để lưu thay đổi.
* **Example**: 회사에서 SVN을 쓰면 중앙 서버가 죽었을 때 작업을 올릴 수 없지만, Git을 쓰면 내 PC(Local)에 저장해뒀다가 서버가 복구되면 올릴 수 있습니다.

## 41. 빌드 자동화 도구 심화: Jenkins vs Gradle
* **Jenkins**: JAVA 기반 오픈 소스. 친숙한 Web GUI 제공. 분산 빌드/테스트 가능.
* **Gradle**: Groovy 기반 오픈 소스. 안드로이드 앱 개발 환경에서 주로 사용. DSL을 스크립트 언어로 사용하며 태스크(Task) 단위로 실행. 빌드 캐시(Build Cache)로 속도 향상.
* **Vietnamese**: Jenkins (dựa trên Java, có Web GUI dễ dùng) và Gradle (dựa trên Groovy, dùng nhiều trong Android, tăng tốc bằng Build Cache).
* 💡 **Mẹo ghi nhớ**: Jenkins = Java, Gradle = Groovy (Android).

## 42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)
* **결함 집중 (Defect Clustering) & 파레토 법칙**: 오류의 80%는 20%의 모듈에 집중됨.
* **살충제 패러독스 (Pesticide Paradox)**: 동일한 테스트 케이스로 반복 테스트하면 더 이상 새로운 결함을 찾을 수 없음. 주기적인 테스트 케이스 개선 필요.
* **오류-부재의 궤변 (Absence of Errors Fallacy)**: 결함이 0이더라도 사용자의 요구사항을 만족시키지 못하면 품질이 높다고 할 수 없음.
* **확인 (Validation)** vs **검증 (Verification)**:
  * 확인(Validation): **사용자** 입장에서 요구사항에 맞는지 테스트.
  * 검증(Verification): **개발자** 입장에서 명세서(스펙)에 맞는지 테스트.
* **Vietnamese**: Nguyên lý kiểm thử:
  * Pesticide Paradox (Nghịch lý thuốc trừ sâu): Dùng mãi 1 kịch bản thì không bắt được lỗi mới.
  * Absence of Errors Fallacy: Không có lỗi không có nghĩa là phần mềm tốt nếu sai yêu cầu của khách hàng.
  * Validation: Đúng yêu cầu người dùng (Build the right product). Verification: Làm đúng kỹ thuật/tài liệu (Build the product right).
* **Example**: 로그인 버튼을 예쁘게 만들었지만(결함 없음), 고객이 원한 건 지문 인식 로그인이라면 이는 '오류-부재의 궤변'입니다.

## 43. 테스트 분류 방식 (Test Classification)
* **실행 여부에 따른 분류**:
  * **정적 테스트 (Static)**: 프로그램 실행 없이 분석. (워크스루, 인스펙션, 코드 검사).
  * **동적 테스트 (Dynamic)**: 프로그램을 직접 실행하며 테스트. (블랙박스, 화이트박스).
* **기반(Bases)에 따른 분류**:
  * **명세 기반 (Specification)**: 요구사항 명세서를 빠짐없이 테스트. (동등 분할, 경계값).
  * **구조 기반 (Structure)**: 내부 논리 흐름(코드)에 따라 테스트. (구문, 결정, 조건 기반).
  * **경험 기반 (Experience)**: 테스터의 경험 직관에 의존. (에러 추정, 탐색적 테스팅).
* **목적에 따른 분류**:
  * **회복 (Recovery)**: 일부러 실패하게 한 후 복구되는지 확인.
  * **안전 (Security)**: 불법 침입으로부터 보호 확인.
  * **강도 (Stress)**: 과부하(Overload) 상태에서 정상 동작하는지.
  * **성능 (Performance)**: 응답 시간, 처리량 등 효율성 진단.
  * **회귀 (Regression)**: 코드를 수정한 후 **새로운 결함**이 발생하지 않았는지 확인.
  * **병행 (Parallel)**: 변경된 시스템과 기존 시스템에 동일 데이터 입력 후 결과 비교.
* **Vietnamese**: Phân loại kiểm thử.
  * Theo thực thi: Tĩnh (không chạy code - Review) và Động (chạy code).
  * Theo cơ sở: Dựa trên Đặc tả (Spec), Cấu trúc (Code), Kinh nghiệm.
  * Theo mục đích: Phục hồi (Recovery), Áp lực (Stress - quá tải), Hồi quy (Regression - test lại sau khi sửa code), Song song (Parallel).
* **Example**: 버그를 고치고 나서 다른 곳에 문제가 안 생겼는지 다시 테스트하는 것이 '회귀 테스트'입니다. (Kiểm tra lại sau khi sửa lỗi là Regression Test).



## 44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)
* **문장(구문) 검증 기준 (Statement Coverage)**: 소스 코드의 **모든 구문**이 한 번 이상 수행되도록 설계.
* **결정/분기 검증 기준 (Decision/Branch Coverage)**: 모든 조건문에 대해 조건이 **True인 경우와 False인 경우**가 한 번 이상 수행되도록 설계.
* **조건 검증 기준 (Condition Coverage)**: 조건문에 포함된 **개별 조건식**의 결과가 T/F 한 번 이상 수행되도록 설계.
* **분기/조건 기준 (Branch/Condition Coverage)**: 위 두 가지를 모두 만족하는 설계.
* **Vietnamese**: Các tiêu chí độ phủ (Coverage) trong kiểm thử hộp trắng: Bao phủ cú pháp (Statement), Bao phủ nhánh/quyết định (Branch - lệnh IF chạy cả T/F), Bao phủ điều kiện (Condition - từng điều kiện nhỏ chạy cả T/F), Bao phủ nhánh/điều kiện.
* 💡 **Mẹo ghi nhớ**: Statement = Dòng code. Branch = Ngã rẽ (IF). Condition = Điều kiện nhỏ trong IF.

## 45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계
개발 단계와 테스트 단계를 짝지어 놓은 모델.
1. **단위 테스트 (Unit Test)** - *구현(Code)* 단계와 짝. 모듈/컴포넌트 초점 (주로 구조 기반/화이트박스).
2. **통합 테스트 (Integration Test)** - *설계(Design)* 단계와 짝. 모듈들을 결합하여 테스트.
   * **하향식 (Top-down)**: 스텁(Stub) 사용. 깊이/넓이 우선. 테스트 초기부터 시스템 구조 파악 가능.
   * **상향식 (Bottom-up)**: 드라이버(Driver)와 클러스터(Cluster) 사용.
3. **시스템 테스트 (System Test)** - *분석(Specification)* 단계와 짝. 실제 환경과 유사하게 구성, 기능적/비기능적 요구사항 점검.
4. **인수 테스트 (Acceptance Test)** - *요구사항(Requirements)* 단계와 짝. 사용자가 직접 테스트. (알파/베타 테스트).
* **Vietnamese**: Mô hình chữ V (V-Model). Code <-> Unit, Design <-> Integration, Analysis <-> System, Requirements <-> Acceptance.
* **Example**: 코드 짠 사람이 직접 해보는 건 단위 테스트, 고객이 요구사항대로 됐는지 최종 확인하는 건 인수 테스트입니다.

## 46. 애플리케이션 테스트 프로세스 (Test Process)
* **순서**: 계획(Plan) → 분석 및 디자인(Analysis & Design) → 케이스 및 시나리오 작성 → 수행(Execution) → 결과 평가 및 리포팅 → 결함 추적 및 관리.
* **결함 (Fault/Defect)**: 설계와 다르게 동작하거나 예상 결과와 일치하지 않는 부분.
* **Vietnamese**: Quy trình kiểm thử: Lập kế hoạch -> Phân tích -> Viết kịch bản -> Chạy -> Đánh giá -> Theo dõi lỗi (Defect Tracking). Lỗi (Defect) là sự sai lệch giữa kết quả thực tế và mong đợi.

## 47. 테스트 오라클의 종류 (Types of Test Oracles)
* **참(True) 오라클**: 모든 입력값에 대해 결과를 제공 (모든 오류 검출).
* **샘플링(Sampling) 오라클**: 특정한 몇몇 입력값에 대해서만 결과 제공.
* **추정(Heuristic) 오라클**: 샘플링 + 나머지 값들은 추정(직관)으로 처리.
* **일관성 검사(Consistent) 오라클**: 변경 전후의 결과값이 동일한지 확인.
* **Vietnamese**: Các loại Test Oracle: Chân lý (True - biết hết kết quả), Lấy mẫu (Sampling - biết vài cái), Ước lượng (Heuristic - kết hợp lấy mẫu và đoán), Nhất quán (Consistent - trước sau như một).

## 48. 테스트 자동화 도구 (Test Automation Tools)
* **정적 분석 도구**: 실행 없이 코드 표준/스타일/복잡도 검사.
* **테스트 케이스 생성 도구**: 자료 흐름도, 기능 테스트, 도메인 분석, 랜덤 등으로 TC 자동 생성.
* **테스트 실행 도구**: 데이터 주도(Data-driven) 및 키워드 주도(Keyword-driven) 스크립트 실행.
* **성능 테스트 도구**: 가상의 사용자를 만들어 부하를 줌.
* **테스트 통제 도구**: 테스트 계획, 형상 관리, 결함 관리.
* **테스트 하네스 도구**: 테스트 환경 시뮬레이션.
* **Vietnamese**: Các công cụ tự động hóa kiểm thử: Phân tích tĩnh, Tạo TC, Chạy TC, Đo hiệu năng, Quản lý, Test Harness (Môi trường giả lập).

## 49. 테스트 하네스 구성 요소 (Test Harness Components)
* **드라이버(Driver)**: 하위 모듈 호출 (상향식).
* **스텁(Stub)**: 가짜 하위 모듈 (하향식).
* **슈트(Suites)**: 테스트 케이스의 집합.
* **케이스(Case)**: 입력 값, 실행 조건, 기대 결과 명세.
* **스크립트(Script)**: 테스트 실행 절차 명세(자동화).
* **목 오브젝트(Mock Object)**: 조건부 입력에 따라 상황에 맞는 행위를 수행하는 가짜 객체.
* **Vietnamese**: Thành phần của Test Harness: Driver (gọi cấp dưới), Stub (giả cấp dưới), Suites (tập hợp TC), Case (kịch bản), Script (mã chạy tự động), Mock Object (đối tượng giả).

## 50. 애플리케이션 성능 측정 지표 (Performance Metrics)
* **처리량 (Throughput)**: 일정 시간 내 처리하는 일의 양.
* **응답 시간 (Response Time)**: 요청을 전달한 후 '응답이 도착할 때'까지 걸린 시간.
* **경과 시간 (Turn Around Time)**: 작업을 의뢰한 후 '처리가 완료될 때'까지 걸린 시간.
* **자원 사용률 (Resource Usage)**: CPU, 메모리, 네트워크 등의 자원 사용량.
* **Vietnamese**: Các chỉ số hiệu năng: Thông lượng (Throughput), Thời gian phản hồi (Response), Thời gian hoàn thành (Turn Around), Mức sử dụng tài nguyên (Resource Usage).
* **Example**: 식당에서 주문하고 물이 나오는 시간(응답 시간), 음식을 다 먹고 나오는 시간(경과 시간).
* 💡 **Mẹo ghi nhớ**: Response = Phản hồi đầu tiên. Turn Around = Hoàn thành toàn bộ.

## 51. 빅오 표기법 (Big-O Notation) 심화
* **O(1)**: 스택 삽입/삭제.
* **O(log_2 n)**: 이진 트리, 이진 검색 (단계가 절반씩 줄어듦).
* **O(n)**: 1중 for문.
* **O(n log_2 n)**: 힙 정렬, 2-Way 합병 정렬.
* **O(n^2)**: 삽입, 선택, 버블, 퀵 정렬(최악). 2중 for문.
* **O(2^n)**: 피보나치 수열.
* **Vietnamese**: Độ phức tạp thuật toán Big-O. O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n).



## 52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)
* **소스 코드 최적화**: 배제해야 할 '나쁜 코드(Bad Code - 스파게티 코드, 외계인 코드)'와 작성해야 할 '클린 코드(Clean Code - 가독성, 단순성, 의존성 배제, 중복성 최소화, 추상화)'가 있음.
* **순환 복잡도 (McCabe's Cyclomatic Complexity)**: 프로그램 논리의 복잡도를 측정.
  * 계산 방법: `V(G) = 화살표 수(E) - 노드 수(N) + 2` 또는 제어 흐름도의 닫힌 영역 수 + 1.
* **소스 코드 품질 분석 도구 심화**:
  * **정적 분석 도구**: pmd, cppcheck, SonarQube, checkstyle, ccm.
  * **동적 분석 도구**: Avalanche, Valgrind (메모리 누수, 스레드 결함 발견).
* **Vietnamese**: Tối ưu mã nguồn & Độ phức tạp Cyclomatic (McCabe). 
  * Clean code > Bad code (Spaghetti/Alien).
  * V(G) = Cạnh(E) - Đỉnh(N) + 2. Số V(G) chính là số lượng test case cơ bản cần thiết.
  * Công cụ tĩnh (không chạy code): SonarQube. Động (chạy code tìm rò rỉ bộ nhớ): Valgrind.

## 53. EAI와 ESB 심화 (EAI vs ESB)
* **EAI**: 기업 내 애플리케이션들을 연동하는 솔루션 (Point-to-Point, Hub&Spoke, Message Bus, Hybrid).
* **ESB (Enterprise Service Bus)**: 애플리케이션 간 표준 기반 인터페이스 제공. 애플리케이션 통합보다는 **서비스 중심 통합** 지향. 결합도(Coupling)를 **약하게(Loosely)** 유지.
* **Vietnamese**: So sánh EAI và ESB. EAI tập trung tích hợp ứng dụng, ESB tập trung tích hợp dịch vụ (Service-oriented) với độ kết dính lỏng lẻo (Loosely coupled) dùng tiêu chuẩn chung.

## 54. XML 및 데이터 무결성 검사 도구 (XML & Integrity Check Tools)
* **XML (eXtensible Markup Language)**: HTML의 비호환성과 SGML의 복잡성을 해결하기 위해 만든 다목적 마크업 언어.
* **인터페이스 보안 - 네트워크 영역 (IPSec)**: 네트워크 계층에서 IP 패킷 단위의 데이터 변조 방지 (양방향 암호화 지원).
* **데이터 무결성 검사 도구**: 시스템 파일 변경 유무 확인 (해시 함수 이용). 백도어 탐지.
  * **종류**: Tripwire, AIDE, Samhain, Claymore, Slipwire, Fcheck.
* **Vietnamese**: XML khắc phục nhược điểm của HTML/SGML. Công cụ kiểm tra tính toàn vẹn dữ liệu (phát hiện backdoor/thay đổi file) dùng hàm Hash: Tripwire, AIDE.

## 55. APM (애플리케이션 성능 관리/모니터링)
* 애플리케이션의 성능 관리를 위해 자원 현황, 트랜잭션 등을 모니터링.
* **리소스 방식**: Nagios, Zabbix, Cacti.
* **엔드투엔드(End-to-End) 방식**: VisualVM, 제니퍼(Jennifer), 스카우터(Scouter).
* **Vietnamese**: Công cụ giám sát hiệu năng (APM). Có 2 loại: Theo dõi tài nguyên (Nagios) và Từ đầu đến cuối (VisualVM, Scouter).

---
*(이하 전자계산기 구조 파트 - Computer Architecture)*

## 56. 불 대수(Boolean Algebra)의 기본 공식
* **교환법칙**: A+B = B+A, A·B = B·A
* **결합법칙**: A+(B+C) = (A+B)+C, A·(B·C) = (A·B)·C
* **분배법칙**: A·(B+C) = A·B + A·C, A+B·C = (A+B)·(A+C)
* **멱등법칙**: A+A = A, A·A = A
* **보수법칙**: A+A' = 1, A·A' = 0
* **항등법칙**: A+0 = A, A+1 = 1, A·0 = 0, A·1 = A
* **드모르간 법칙 (De Morgan)**: (A+B)' = A'·B', (A·B)' = A'+B'
* **복원법칙**: (A')' = A
* **Vietnamese**: Các định lý đại số Boolean cơ bản (Giao hoán, Kết hợp, Phân phối, Lũy đẳng, Bù, Đồng nhất, De Morgan).
* **Example**: 드모르간 법칙은 괄호 전체의 부정을 풀 때, 각 변수를 부정하고 가운데 연산자(AND/OR)를 뒤집는 것입니다. (De Morgan: Phủ định của một tổng bằng tích các phủ định).

## 57. 카르노 맵 (Karnaugh Map)
* 설계된 논리식을 도표로 표현하여 간소화하는 방법.
* 1이 입력된 이웃 칸을 $2^n$개(1, 2, 4, 8...)씩 최대 크기로 묶어 간소화.
* 0과 1 모두 포함되는 변수는 상쇄되어 무시됨.
* **Vietnamese**: Bìa Karnaugh. Phương pháp rút gọn hàm Boolean bằng bảng. Nhóm các số 1 kề nhau theo lũy thừa của 2 (1, 2, 4, 8).

## 58. 기본 논리 게이트 (Logic Gates)
* **AND (·)**: 둘 다 1일 때만 1.
* **OR (+)**: 하나라도 1이면 1.
* **NOT (')**: 0이면 1, 1이면 0 반전.
* **NAND**: AND의 부정. 둘 다 1일 때만 0.
* **NOR**: OR의 부정. 둘 다 0일 때만 1.
* **XOR (⊕)**: Exclusive OR. 입력이 서로 다를 때만 1. $A⊕B = A'B + AB'$
* **XNOR (⊙)**: XOR의 부정. 입력이 서로 같을 때만 1. $A⊙B = A'B' + AB$
* **Vietnamese**: Các cổng logic cơ bản. AND (nhân), OR (cộng), NOT (phủ định), XOR (khác nhau thì 1, giống nhau thì 0).

## 59. 반가산기와 전가산기 (Half Adder & Full Adder)
* **반가산기 (HA - Half Adder)**: 1Bit 2진수 2개(A, B)를 더하는 회로.
  * **Sum (합)** = A ⊕ B (XOR 게이트)
  * **Carry (자리올림)** = A · B (AND 게이트)
* **전가산기 (FA - Full Adder)**: 하위 자리에서 올라온 자리올림 수(C_i)를 포함해 3개의 1Bit를 더하는 회로.
  * **Sum** = A ⊕ B ⊕ C_i
  * **Carry** = (A ⊕ B)·C_i + A·B
* **Vietnamese**: Bộ bán cộng (HA) cộng 2 bit. Bộ toàn cộng (FA) cộng 3 bit (gồm cả bit nhớ từ phép cộng trước).
* **Example**: 1+1을 하면 Sum은 0, Carry는 1이 발생합니다. (1+1 = 10 trong hệ nhị phân).
* 💡 **Mẹo ghi nhớ**: Bán cộng (Half Adder) có Sum là XOR, Carry là AND. (HA = XOR + AND).



## 60. 디코더와 플립플롭 (Decoder & Flip-Flop)
* **디코더 (Decoder, 해독기)**: n Bit의 코드를 받아 $2^n$개의 출력으로 번역하는 회로. 주로 명령어 해독에 사용되며 AND 게이트로 구성.
* **플립플롭 (Flip-Flop)**: 1Bit를 기억하는 메모리 소자 (2진 셀). 전원이 공급되는 한 상태 유지.
  * **RS**: 기본 플립플롭.
  * **JK**: RS에서 S=1, R=1일 때 동작 불능 상태를 해결. (둘 다 1이면 보수 출력).
  * **D (Data)**: RS의 R에 인버터를 달아 입력선을 1개로 만듦. 입력값을 그대로 저장.
  * **T (Toggle)**: JK의 두 입력을 묶은 일치 플립플롭. 1이 입력될 때마다 상태가 반전(Toggle).
  * **마스터-슬레이브**: 레이스 현상(Race condition)을 없애기 위해 2개의 플립플롭을 직렬 연결.
* **Vietnamese**: Bộ giải mã (Decoder) chuyển n bit thành $2^n$ đầu ra. Flip-Flop là mạch nhớ 1 bit.
  * RS: Cơ bản.
  * JK: Tốt nhất, khắc phục lỗi 1-1 của RS.
  * D: Lưu dữ liệu (Data).
  * T: Lật trạng thái (Toggle).
* **Example**: 토글(T) 플립플롭은 스위치를 누를 때마다 켜짐/꺼짐이 반복되는 볼펜 스위치와 같습니다.

## 61. 자료 구성의 단위 (Data Units)
* **비트 (Bit)**: 최소 단위 (0 또는 1).
* **니블 (Nibble)**: 4 Bits. (16진수 1자리 표현).
* **바이트 (Byte)**: 8 Bits. 문자 표현의 최소 단위, 주소 지정의 단위.
* **워드 (Word)**: CPU가 한 번에 처리할 수 있는 명령 단위. (Half=2B, Full=4B, Double=8B).
* **필드 (Field)**: 의미 있는 정보의 최소 단위.
* **레코드 (Record)**: 논리 레코드(일반적인 레코드).
* **블록 (Block)**: 물리 레코드(Physical Record). 입출력 단위.
* **파일 (File) -> 데이터베이스 (DB)**.
* **Vietnamese**: Đơn vị dữ liệu: Bit < Nibble (4 bit) < Byte (8 bit) < Word < Field (Trường) < Record (Bản ghi) < Block (Khối) < File < DB.
* 💡 **Mẹo ghi nhớ**: Bi-Ni-By-Wo-Fi-Re-Blo-Fi-DB.

## 62. 진법 변환과 보수 (Radix Conversion & Complements)
* **진법 변환**: 10진수를 다른 진수로 바꿀 때는 정수부는 나누고, 소수부는 곱함. 2진수 3자리는 8진수 1자리, 2진수 4자리는 16진수 1자리.
* **보수 (Complement)**: 뺄셈을 덧셈 회로(가산기)로 처리하기 위해 사용.
* **표현 범위 (n 비트)**:
  * **부호화 절대치 / 1의 보수**: $-2^{n-1}+1$ ~ $2^{n-1}-1$ (0이 +0, -0 두 개 존재).
  * **2의 보수**: $-2^{n-1}$ ~ $2^{n-1}-1$ (음수를 하나 더 표현 가능, 0은 하나뿐이라 연산이 간단).
* **Vietnamese**: Đổi cơ số và Số bù (Complement). Máy tính dùng số bù để làm phép trừ thông qua phép cộng. Số bù 2 (2's complement) phổ biến nhất vì chỉ có một số 0 và biểu diễn thêm được 1 số âm.

## 63. 자료 표현 방식 및 코드 (Data Representation & Codes)
* **고정 소수점 (정수 연산)**: 속도는 빠르나 표현 범위가 작음. 맨 앞 1비트는 부호비트(0:양수, 1:음수).
* **부동 소수점 (실수 연산)**: 부호(Sign), 지수부(Exponent), 가수부(Mantissa)로 구성. 정규화 과정이 필요하며 연산이 느리나 아주 큰/작은 수 표현 가능.
* **BCD 코드**: 8421 코드, 10진수 1자리를 2진수 4비트로 표현.
* **Excess-3 (3초과 코드)**: BCD + 3. 자보수(Self-complement) 코드.
* **Gray 코드 (그레이 코드)**: 1비트만 변화시켜 다음 수치로 증가 (오류 적음, A/D 변환기에 사용). 2진수와 XOR 연산으로 상호 변환.
* **패리티 검사 코드**: 1비트의 오류만 **검출** (교정 불가). Odd(홀수)/Even(짝수) 패리티.
* **해밍 코드 (Hamming Code)**: 오류를 **검출하고 교정(1Bit)**까지 가능한 코드. 패리티 비트는 $2^n$ 번째 자리(1, 2, 4, 8...)에 위치.
* **Vietnamese**: 
  * Dấu phẩy động (Floating point): Gồm Dấu, Số mũ, Phần định trị. Rộng nhưng chậm.
  * Mã Gray: Thay đổi 1 bit mỗi lần (dùng trong chuyển đổi A/D).
  * Mã Hamming: Có khả năng tự sửa lỗi 1 bit (Error Correction Code).
* **Example**: 패리티 코드는 "여기에 에러가 있다!"고 알려주기만 하지만, 해밍 코드는 "여기에 에러가 있으니 고쳤어!"라고 해줍니다.

## 64. 중앙처리장치(CPU)의 구성 요소 (CPU Components)
* **제어장치 (Control Unit)**: 명령어를 해독하여 제어 신호를 보냄.
  * 구성: 명령 레지스터(IR), 명령 해독기(Decoder), 부호기(Encoder), 제어 주소/버퍼 레지스터(CAR/CBR), 제어 기억장치, 순차 카운터(PC).
* **연산장치 (ALU)**: 실제 연산을 수행.
  * 구성: 가산기(Adder), 누산기(AC - 연산 중간결과 임시저장), 보수기(Complementer), 상태/플래그 레지스터, 이동(Shift) 레지스터.
* **레지스터 (Register)**: CPU 내부의 임시 기억장치. 메모리 중 가장 속도가 빠름 (플립플롭으로 구성).
* **Vietnamese**: Thành phần CPU:
  * Control Unit (Điều khiển): Giải mã lệnh và ra lệnh.
  * ALU (Tính toán): Tính toán thực tế. Chứa Accumulator (Lưu kết quả tạm thời).
  * Register (Thanh ghi): Bộ nhớ trong CPU, nhanh nhất.
* 💡 **Mẹo ghi nhớ**: Thanh ghi lũy kế (Accumulator) thuộc ALU. Thanh ghi lệnh (IR) thuộc Bộ điều khiển (CU).



## 65. 주요 레지스터와 버스 (Registers & Bus)
* **주요 레지스터**:
  * **PC (프로그램 카운터)**: '다음'에 실행할 명령어의 번지 기억.
  * **IR (명령 레지스터)**: '현재' 실행 중인 명령어 기억.
  * **AC (누산기)**: 연산 결과를 일시적으로 저장.
  * **MAR (메모리 주소 레지스터)**: 출입할 메모리의 주소 기억.
  * **MBR (메모리 버퍼 레지스터)**: 메모리를 오가는 데이터 임시 저장.
  * **상태 레지스터 (PSWR)**: 오버플로, 부호, 인터럽트 등 CPU 상태 저장.
* **버스 (Bus)**: 정보를 교환하는 전송선.
  * **주소 버스 (단방향)**: 위치 지정.
  * **데이터 버스 (양방향)**: 실제 데이터 전송.
  * **제어 버스 (양방향)**: 제어 신호 전송.
* **Vietnamese**: Các thanh ghi (Register) chính: PC (chứa địa chỉ lệnh tiếp theo), IR (chứa lệnh hiện tại), AC (Accumulator - chứa kết quả tính toán). Bus: Address (1 chiều), Data (2 chiều), Control (2 chiều).

## 66. 명령어 형식과 주소지정방식 (Instruction Format & Addressing Modes)
* **명령어의 구성**: 연산자부(OP-Code) + 주소부(Operand).
  * **0 번지**: 스택(Stack) 머신 사용. (역폴리쉬 표기법).
  * **1 번지**: 누산기(AC) 사용.
  * **2 번지**: 가장 널리 사용. 연산 후 원래 자료(Operand 1)가 파괴됨.
  * **3 번지**: 원래 자료를 파괴하지 않으나 명령어 길이가 긺.
* **주소지정방식 (Addressing Modes)**:
  * **암시적 (Implied)**: 데이터 위치 묵시적 지정 (스택/누산기).
  * **즉시적 (Immediate)**: 명령어 자체에 실제 데이터가 있음 (가장 빠름).
  * **직접 (Direct)**: 주소부에 실제 데이터의 유효 주소가 있음 (메모리 1번 접근).
  * **간접 (Indirect)**: 주소부가 가리키는 곳에 유효 주소가 있음 (메모리 2번 이상 접근).
  * **계산에 의한 방식**: 주소부 + 특정 레지스터 값 (상대 주소, 베이스 레지스터, 인덱스 레지스터).
* **Vietnamese**: Các loại địa chỉ lệnh: 0-address (dùng Stack), 1-address (dùng AC), 2-address (ghi đè kết quả lên toán hạng đầu). Các chế độ định địa chỉ: Im Implied (Ngầm định), Immediate (Tức thì - nhanh nhất vì chứa luôn dữ liệu), Direct (Trực tiếp), Indirect (Gián tiếp - cần truy cập bộ nhớ >=2 lần).

## 67. 주요 마이크로 연산 (Micro Operations)
* **논리적 Shift**: 빈자리에 무조건 0 채움.
* **산술적 Shift**: 부호는 유지하고 빈자리를 채움 (곱하기/나누기 연산).
  * 왼쪽(Left): 원래 자료 x 2. 오른쪽(Right): 원래 자료 / 2.
* **마스킹 (Masking) 연산**: AND 연산을 사용하여 특정 비트를 삭제(Clear).
* **선택적 세트 (Selective Set)**: OR 연산을 사용하여 특정 비트를 1로 세트.
* **Vietnamese**: Phép dịch bit (Shift): Dịch logic (điền 0) và Dịch số học (giữ nguyên dấu, Left = nhân 2, Right = chia 2). Masking (xóa bit bằng AND), Selective Set (bật bit 1 bằng OR).
* **Example**: 2진수 0010 (2)를 왼쪽으로 1칸 산술 Shift 하면 0100 (4)가 됩니다.

## 68. 메이저 스테이트와 제어 사이클 (Major States)
CPU가 명령을 수행하기 위해 거치는 4가지 상태.
1. **인출 (Fetch)**: 메모리에서 명령어를 가져와 IR에 넣음. 해독 후 주소지정방식(모드 비트)에 따라 다음 상태 결정.
   * 모드 0 (직접) -> Execute / 모드 1 (간접) -> Indirect.
2. **간접 (Indirect)**: 메모리에서 유효 주소를 계산하기 위해 한 번 더 접근.
3. **실행 (Execute)**: 명령을 실제 수행.
4. **인터럽트 (Interrupt)**: 예상치 못한 이벤트 발생 시 현재 상태(PC)를 0번지에 저장하고 처리 루틴으로 이동.
* **Vietnamese**: 4 trạng thái hoạt động chính của CPU: Fetch (Nạp lệnh vào IR), Indirect (Tìm địa chỉ thật nếu là định địa chỉ gián tiếp), Execute (Thực thi), Interrupt (Ngắt - cất PC hiện tại đi và xử lý lỗi/sự kiện).

