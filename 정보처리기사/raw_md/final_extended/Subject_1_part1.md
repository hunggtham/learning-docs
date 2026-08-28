# 1과목: 소프트웨어 설계 (Phần 1: Thiết kế phần mềm)

## 1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)

### 001. 소프트웨어 공학의 기본 원칙 (Nguyên tắc cơ bản của kỹ nghệ phần mềm)
- 현대적인 프로그래밍 기술을 계속적으로 적용해야 한다. (Phải liên tục áp dụng các kỹ thuật lập trình hiện đại.)
- 개발된 소프트웨어의 품질이 유지되도록 지속적으로 검증해야 한다. (Phải liên tục xác minh để duy trì chất lượng phần mềm đã phát triển.)
- 소프트웨어 개발 관련 사항 및 결과에 대한 명확한 기록을 유지해야 한다. (Phải lưu giữ hồ sơ rõ ràng về các vấn đề và kết quả liên quan đến phát triển phần mềm.)
- **Ví dụ (Example):** Áp dụng CI/CD (Continuous Integration/Continuous Deployment) để liên tục kiểm thử (검증) phần mềm mỗi khi có code mới.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **HKK** (Hiện - Kiểm - Ký): **Hãy Kiểm Kê** (Kỹ thuật hiện đại - Kiểm chứng - Ghi chép).

### 002. 폭포수 모형 (Waterfall Model / Mô hình thác nước)
- 이전 단계로 돌아갈 수 없다는 전제하에 각 단계를 확실히 매듭짓고 다음 단계를 진행하는 개발 방법론이다. (Là phương pháp phát triển với tiền đề không thể quay lại giai đoạn trước, hoàn thành dứt điểm từng giai đoạn rồi mới tiến sang giai đoạn tiếp theo.)
- 보헴이 제시한 고전적 생명 주기 모형이다. (Là mô hình vòng đời cổ điển do Boehm đề xuất.)
- 요구사항을 반영하기 어렵다. (Khó phản ánh/thay đổi yêu cầu.)
- **Ví dụ (Example):** Xây dựng một ngôi nhà, bạn không thể xây mái nhà khi chưa làm xong móng. (Phải theo tuần tự).
- 💡 **Mẹo ghi nhớ (Mnemonic):** Nước chảy từ trên xuống, không chảy ngược lại (이전 단계로 돌아갈 수 없음).

### 003. 나선형 모형 (Spiral Model / Mô hình xoắn ốc)
- 나선을 따라 돌듯이 점진적으로 완벽한 최종 소프트웨어를 개발하는 것이다. (Phát triển phần mềm cuối cùng hoàn hảo một cách tuần tự giống như quay theo hình xoắn ốc.)
- '계획 수립 → 위험 분석 → 개발 및 검증 → 고객 평가' 과정이 반복적으로 수행된다. (Quá trình 'Lập kế hoạch → Phân tích rủi ro → Phát triển & Kiểm chứng → Khách hàng đánh giá' được lặp đi lặp lại.)
- **Ví dụ (Example):** Phát triển một game lớn, ban đầu làm bản demo (1 vòng xoắn), đánh giá rủi ro, rồi mới phát triển thêm tính năng (vòng xoắn tiếp theo).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KNKK** (Kế - Nguy - Khai - Khách): **Kế Nguy Khách Khóc** (Lập KH - Rủi ro - Phát triển - Khách hàng).

### 004. 애자일 모형의 주요 방법론 (Các phương pháp luận chính của mô hình Agile)
- 스크럼 (Scrum
- XP (eXtreme Programming)
- 기능 중심 개발 (FDD; Feature Driven Development)
- 칸반 (Kanban)
- Lean
- **Ví dụ (Example):** Các công ty startup thường dùng Scrum để phát triển nhanh một ứng dụng, chia thành các Sprint ngắn 2 tuần.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **SXFKL** (Scrum, XP, FDD, Kanban, Lean): **Sợ Xấu Phải Kiêng Luôn**.

### 005. 애자일 개발 4가지 핵심 가치 (4 Giá trị cốt lõi của phát triển Agile)
- 프로세스와 도구보다는 개인과 상호작용에 더 가치를 둔다. (Coi trọng cá nhân và sự tương tác hơn là quy trình và công cụ.)
- 방대한 문서보다는 실행되는 SW에 더 가치를 둔다. (Coi trọng phần mềm chạy được hơn là tài liệu đồ sộ.)
- 계약 협상보다는 고객과 협업에 더 가치를 둔다. (Coi trọng sự cộng tác với khách hàng hơn là đàm phán hợp đồng.)
- 계획을 따르기 보다는 변화에 반응하는 것에 더 가치를 둔다. (Coi trọng việc phản hồi với sự thay đổi hơn là bám sát kế hoạch.)
- **Ví dụ (Example):** Thay vì viết tài liệu 100 trang cho khách, nhóm Agile sẽ đưa cho khách một bản demo chạy được (실행되는 SW) để lấy ý kiến ngay.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CTKB** (Cá - Thực - Khách - Biến): **Cá Thực Khó Bắt** (Cá nhân - Thực thi - Khách hàng - Biến đổi).

### 006. XP의 핵심 가치 (Giá trị cốt lõi của XP - eXtreme Programming)
- 의사소통 (Communication - Giao tiếp)
- 단순성 (Simplicity - Sự đơn giản)
- 용기 (Courage - Dũng cảm)
- 존중 (Respect - Tôn trọng)
- 피드백 (Feedback - Phản hồi)
- **Ví dụ (Example):** Developer có 'dũng cảm' (용기) để xóa những đoạn code cũ không cần thiết và viết lại cho 'đơn giản' (단순성).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **YĐDTP** (Ý - Đơn - Dũng - Tôn - Phản): **Ý Định Dũng Tướng Phàm**.

## 2. 요구사항 개발 (Phát triển Yêu cầu)

### 007. 주요 비기능 요구사항 (Các yêu cầu phi chức năng chính / Non-functional Requirements)
- 성능 요구사항 (Yêu cầu hiệu năng)
- 보안 요구사항 (Yêu cầu bảo mật)
- 품질 요구사항 (Yêu cầu chất lượng)
- 제약사항 (Ràng buộc)
- 인터페이스 요구사항 (Yêu cầu giao diện)
- **Ví dụ (Example):** Chức năng đăng nhập là yêu cầu chức năng. Nhưng "Đăng nhập phải hoàn tất dưới 1 giây" là yêu cầu phi chức năng (hiệu năng - 성능).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **HBCRG** (Hiệu - Bảo - Chất - Ràng - Giao): **Học Bài Chăm Rồi Giỏi**.

### 008. 요구사항 개발 프로세스 (Quy trình phát triển yêu cầu)
- 도출 (Elicitation - Khám phá/Rút ra) → 분석 (Analysis - Phân tích) → 명세 (Specification - Đặc tả) → 확인 (Validation - Xác nhận)
- **Ví dụ (Example):** Phỏng vấn user (도출), lọc ra các yêu cầu hợp lý (분석), viết tài liệu SRS (명세), nhờ user ký duyệt (확인).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **ĐPMX** (Đồ - Phân - Minh - Xác): **Đi Phượt Một Xe**.

### 009. 요구사항 분석 (Phân tích yêu cầu / Requirements Analysis)
- 개발 대상에 대한 사용자의 요구사항을 이해하고 문서화(명세화)하는 활동을 의미한다. (Hoạt động hiểu và tài liệu hóa (đặc tả) yêu cầu của người dùng về đối tượng cần phát triển.)
- 소프트웨어 개발의 실제적인 첫 단계이다. (Là bước thực tế đầu tiên của phát triển phần mềm.)
- 사용자 요구의 타당성을 조사하고 비용과 일정에 대한 제약을 설정한다. (Khảo sát tính hợp lý của yêu cầu người dùng và thiết lập các ràng buộc về chi phí, lịch trình.)
- 사용자의 요구를 정확하게 추출하여 목표를 정하고, 해결 방식을 결정한다. (Trích xuất chính xác yêu cầu của người dùng để đặt mục tiêu và quyết định cách giải quyết.)
- **Ví dụ (Example):** Khách hàng muốn "App chạy nhanh". Phân tích viên sẽ dịch thành "Thời gian phản hồi < 2s" và xem xét chi phí server có đủ đáp ứng không (비용/일정 제약).

### 010. 자료 흐름도 (DFD - Data Flow Diagram) 의 구성 요소
- 프로세스 (Process - Quy trình): Hình tròn / Hình bầu dục. (Ví dụ: 물품 확인 - Kiểm tra hàng hóa)
- 자료 흐름 (Data Flow - Luồng dữ liệu): Mũi tên. (Ví dụ: 물품 코드 - Mã hàng hóa)
- 자료 저장소 (Data Store - Kho lưu trữ dữ liệu): Hai đường thẳng song song. (Ví dụ: 물품대장 - Sổ hàng hóa)
- 단말 (Terminator - Điểm cuối/Tác nhân ngoài): Hình chữ nhật. (Ví dụ: 공장 - Nhà máy)
- 💡 **Mẹo ghi nhớ (Mnemonic):** **PFST** (Process, Flow, Store, Terminator): **Phải Phạt Sợ Tội**.

### 011. 자료 사전 (Data Dictionary) 의 표기 기호
- `=`: 정의 (Định nghĩa - is composed of)
- `+`: 연결 (Kết nối/Và - and)
- `( )`: 생략 (Có thể bỏ qua/Tùy chọn - optional)
- `[ | ]`: 선택 (Lựa chọn [hoặc] - choose only one)
- `{ }`: 반복 (Lặp lại - iteration)
- `* *`: 설명 (Giải thích/Chú thích - comment)
- **Ví dụ (Example):** `Customer_Name = First_Name + (Middle_Name) + Last_Name`. Middle_Name nằm trong `( )` nghĩa là có thể không có (생략).
- 💡 **Mẹo ghi nhớ (Mnemonic):** `{ }` giống như vòng lặp trong code, nên là lặp lại (반복). `* *` giống comment `/* */` trong code.

### 012. HIPO (Hierarchy plus Input-Process-Output)
- 하향식 소프트웨어 개발을 위한 문서화 도구이다. (Là công cụ tài liệu hóa cho phát triển phần mềm theo hướng từ trên xuống - Top-down.)
- 기호, 도표 등을 사용하므로 보기 쉽고 이해하기도 쉽다. (Sử dụng ký hiệu, biểu đồ nên dễ nhìn và dễ hiểu.)
- 기능과 자료의 의존 관계를 동시에 표현할 수 있다. (Có thể biểu diễn đồng thời mối quan hệ phụ thuộc giữa chức năng và dữ liệu.)
- **Ví dụ (Example):** Vẽ một sơ đồ cây bắt đầu từ Hệ thống chính (Quản lý trường học) rẽ nhánh xuống các chức năng con (Quản lý điểm, Quản lý sinh viên).

## 3. 모델링 및 UML (Mô hình hóa và UML)

### 013. UML (Unified Modeling Language)
- 시스템 개발자와 고객 또는 개발자 상호 간의 의사소통이 원활하게 이루어지도록 표준화한 대표적인 객체지향 모델링 언어이다. (Là ngôn ngữ mô hình hóa hướng đối tượng tiêu biểu được chuẩn hóa để việc giao tiếp giữa nhà phát triển hệ thống và khách hàng, hoặc giữa các nhà phát triển với nhau diễn ra suôn sẻ.)
- 구성 요소 (Components): 사물 (Things - Sự vật), 관계 (Relationships - Mối quan hệ), 다이어그램 (Diagram - Biểu đồ).
- **Ví dụ (Example):** Khi xây nhà cần bản vẽ thiết kế (Blueprint). Khi làm phần mềm, dùng UML làm bản vẽ thiết kế chung để ai cũng hiểu.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **SQĐ** (Sự - Quan - Đa): **Sợ Quá Đi** (Sự vật - Quan hệ - Đa biểu đồ).

### 014. UML의 주요 관계 (Các mối quan hệ chính trong UML)
- 일반화 (Generalization) 관계: 하나의 사물이 다른 사물에 비해 더 일반적인지 구체적인지를 표현. (Thể hiện một sự vật là tổng quát hay cụ thể hơn sự vật khác - kế thừa).
- 의존 (Dependency) 관계: 필요에 의해 서로에게 영향을 주는 짧은 시간 동안만 연관을 유지하는 관계를 표현. (Thể hiện mối quan hệ phụ thuộc ngắn hạn, ảnh hưởng lẫn nhau khi cần thiết).
- 실체화 (Realization) 관계: 사물이 할 수 있거나 해야 하는 기능으로 서로를 그룹화 할 수 있는 관계를 표현. (Thể hiện mối quan hệ hiện thực hóa chức năng mà sự vật có thể/phải làm - interface).
- **Ví dụ (Example):** Động vật -> Chó, Mèo là mối quan hệ '일반화' (Generalization).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **NYT** (Nhất - Ý - Thực): **Như Ý Thật** (Nhất quát - Ý tồn - Thực thể).

### 015. 구조적(Structural) 다이어그램의 종류 (Các loại biểu đồ cấu trúc - Tĩnh)
- 클래스 다이어그램 (Class Diagram)
- 객체 다이어그램 (Object Diagram)
- 컴포넌트 다이어그램 (Component Diagram)
- 배치 다이어그램 (Deployment Diagram)
- 복합체 구조 다이어그램 (Composite Structure Diagram)
- 패키지 다이어그램 (Package Diagram)
- **Ví dụ (Example):** Class Diagram thể hiện cấu trúc tĩnh của hệ thống, giống như sơ đồ tổ chức của một công ty.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **LĐCBPG** (Lớp - Đối - Com - Bố - Phức - Gói): **Làm Được Có Bữa Phải Giỏi**. Các biểu đồ này thể hiện cấu trúc "Tĩnh" (정적).

### 016. 행위(Behavioral) 다이어그램의 종류 (Các loại biểu đồ hành vi - Động)
- 유스케이스 다이어그램 (Use Case Diagram)
- 순차 다이어그램 (Sequence Diagram)
- 커뮤니케이션 다이어그램 (Communication Diagram)
- 상태 다이어그램 (State Diagram)
- 활동 다이어그램 (Activity Diagram)
- 상호작용 개요 다이어그램 (Interaction Overview Diagram)
- 타이밍 다이어그램 (Timing Diagram)
- **Ví dụ (Example):** Sequence Diagram thể hiện trình tự thời gian gửi tin nhắn (메시지) giữa các đối tượng (hành vi động).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **UTCTHTT** (Use - Trình - Com - Trạng - Hoạt - Tương - Time): **Uống Trà Chiều Thấy Hay Thật Tuyệt**. Các biểu đồ này thể hiện đặc tính "Động" (동적).

### 017. 스테레오 타입 (Stereotype)
- UML에서 표현하는 기본 기능 외에 추가적인 기능을 표현하기 위해 사용한다. (Dùng để biểu diễn các chức năng bổ sung ngoài chức năng cơ bản trong UML.)
- 길러멧(Guilemet)이라고 부르는 겹화살괄호(`<< >>`) 사이에 표현할 형태를 기술한다. (Viết hình thái muốn biểu diễn giữa cặp dấu ngoặc nhọn kép `<< >>` gọi là Guilemet.)
- **Ví dụ (Example):** `<<include>>` hoặc `<<extend>>` trong Use Case Diagram.

### 018. 유스케이스 다이어그램 - 액터(Actor) (Biểu đồ Use Case - Tác nhân)
- 시스템과 상호작용을 하는 모든 외부 요소로, 사람이나 외부 시스템을 의미한다. (Là tất cả các yếu tố bên ngoài tương tác với hệ thống, có nghĩa là con người hoặc hệ thống bên ngoài.)
- 주액터 (Primary Actor): 시스템을 사용함으로써 이득을 얻는 대상으로, 주로 사람이 해당함. (Đối tượng nhận được lợi ích khi dùng hệ thống, chủ yếu là con người - ví dụ: Khách hàng.)
- 부액터 (Secondary Actor): 주액터의 목적 달성을 위해 시스템에 서비스를 제공하는 외부 시스템으로, 조직이나 기관 등이 될 수 있음. (Hệ thống bên ngoài cung cấp dịch vụ cho hệ thống để đạt mục đích của Primary Actor - ví dụ: Cổng thanh toán ngân hàng.)

### 019. 순차(Sequence) 다이어그램의 구성 요소 (Thành phần của biểu đồ Sequence)
- 액터 (Actor - Tác nhân)
- 객체 (Object - Đối tượng)
- 생명선 (Lifeline - Đường đời)
- 실행 상자 (Active Box - Hộp thực thi)
- 메시지 (Message - Thông điệp)
- **Ví dụ (Example):** Khi user (Actor) ấn nút mua hàng, một mũi tên (Message) sẽ được gửi đến Giỏ hàng (Object). Đường nét đứt sổ dọc xuống từ Giỏ hàng là 생명선 (Lifeline).

## 4. 사용자 인터페이스 (Giao diện người dùng - UI)

### 020. 사용자 인터페이스의 특징 (Đặc điểm của giao diện người dùng)
- 사용자의 편리성과 가독성을 높여준다. (Tăng tính tiện lợi và khả năng đọc cho người dùng.)
- 작업 시간을 단축시킨다. (Rút ngắn thời gian làm việc.)
- 업무에 대한 이해도를 높여준다. (Tăng cường sự hiểu biết về công việc.)
- 사용자 중심으로 설계되어 있다. (Được thiết kế lấy người dùng làm trung tâm.)

### 021. 사용자 인터페이스의 구분 (Phân loại giao diện người dùng)
- CLI (Command Line Interface): 명령과 출력이 텍스트 형태로 이뤄지는 인터페이스 (Giao diện mà lệnh và đầu ra đều dưới dạng văn bản - VD: CMD, Terminal).
- GUI (Graphical User Interface): 아이콘이나 메뉴를 마우스로 선택하여 작업을 수행하는 그래픽 환경의 인터페이스 (Giao diện môi trường đồ họa, dùng chuột chọn icon/menu - VD: Windows, MacOS).
- NUI (Natural User Interface): 사용자의 말이나 행동으로 기기를 조작하는 인터페이스 (Giao diện thao tác thiết bị bằng lời nói hoặc hành động của người dùng - VD: Siri, Kinect).

### 022. 사용자 인터페이스의 기본 원칙 (Nguyên tắc cơ bản của UI)
- 직관성 (Tính trực quan): 누구나 쉽게 이해하고 사용할 수 있어야 한다. (Bất kỳ ai cũng có thể dễ dàng hiểu và sử dụng.)
- 유효성 (Tính hữu hiệu): 사용자의 목적을 정확하고 완벽하게 달성해야 한다. (Phải đạt được mục đích của người dùng một cách chính xác và hoàn hảo.)
- 학습성 (Tính học hỏi): 누구나 쉽게 배우고 익힐 수 있어야 한다. (Bất kỳ ai cũng có thể dễ dàng học và làm quen.)
- 유연성 (Tính linh hoạt): 요구사항을 최대한 수용하며, 실수를 방지. (Tính linh hoạt, tối đa hóa việc đáp ứng yêu cầu người dùng).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **THHN** (Trực - Hữu - Học - Nhu): **Trực Học Hằng Ngày**.

### 023. 목업 (Mockup)
- 와이어프레임보다 좀 더 실제 화면과 유사하게 만든 정적인 형태의 모형이다. (Là mô hình dạng tĩnh, được làm giống với màn hình thực tế hơn so với Wireframe.)
- 시각적으로만 구성 요소를 배치하는 것으로 실제로 구현되지는 않는다. (Chỉ bố trí các thành phần về mặt thị giác chứ thực tế không hoạt động/code chưa chạy.)
- **Ví dụ (Example):** Dùng Figma vẽ ra một màn hình app đẹp long lanh, nhưng bấm vào các nút không có phản hồi logic gì, đó là Mockup.

## 5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)

### 024. ISO/IEC 9126의 품질 특성 (Đặc tính chất lượng theo ISO/IEC 9126)
- 기능성 (Functionality): 요구사항을 정확하게 만족하는 기능을 제공하는지 여부를 나타냄. (Cung cấp chức năng thỏa mãn chính xác các yêu cầu không.)
- 신뢰성 (Reliability): 요구된 기능을 오류 없이 수행할 수 있는 정도를 나타냄. (Mức độ thực hiện chức năng yêu cầu mà không có lỗi.)
- 사용성 (Usability): 사용자가 쉽게 배우고 사용할 수 있는 정도를 나타냄. (Mức độ người dùng dễ dàng học và sử dụng.)
- 이식성 (Portability): 다른 환경에서도 얼마나 쉽게 적용할 수 있는지 정도를 나타냄. (Mức độ dễ dàng áp dụng trong các môi trường khác nhau.)
- **Ví dụ (Example):** App đang chạy trên Android, mang sang iOS chạy vẫn tốt mà không cần sửa nhiều -> Tính 이식성 (Portability) cao.

### 025. 소프트웨어 아키텍처의 설계 과정 (Quá trình thiết kế Kiến trúc phần mềm)
- 설계 목표 설정 (Thiết lập mục tiêu thiết kế) → 시스템 타입 결정 (Quyết định loại hệ thống) → 아키텍처 패턴 적용 (Áp dụng pattern kiến trúc) → 서브시스템 구체화 (Cụ thể hóa hệ thống con) → 검토 (Xem xét/Đánh giá).

### 026. 모듈화 (Modularization / Mô-đun hóa)
- 기능의 분리가 가능하여 인터페이스가 단순해진다. (Có thể phân tách các chức năng nên giao diện trở nên đơn giản.)
- 프로그램의 효율적인 관리가 가능하다. (Có thể quản lý chương trình một cách hiệu quả.)
- 오류의 파급 효과를 최소화할 수 있다. (Có thể giảm thiểu tác động lan truyền của lỗi.)
- 모듈의 크기를 너무 작게 나누면 개수가 많아져 모듈간의 통합 비용이 많이 들고, 너무 크게 나누면 개수가 적어 통합 비용은 적게 들지만 모듈 하나의 개발 비용이 많이 든다. (Nếu chia module quá nhỏ, số lượng nhiều, chi phí tích hợp sẽ cao. Nếu chia quá lớn, chi phí tích hợp ít nhưng chi phí phát triển 1 module lại cao.)
- **Ví dụ (Example):** Thay vì viết toàn bộ chức năng vào 1 file code, ta chia ra `login.py`, `payment.py`. Lỗi ở payment không làm sập login (giảm thiểu 파급 효과).

### 027. 추상화의 유형 (Các loại trừu tượng hóa)
- 과정 추상화 (Trừu tượng hóa quá trình)
- 데이터(자료) 추상화 (Trừu tượng hóa dữ liệu)
- 제어 추상화 (Trừu tượng hóa điều khiển)

### 028. 정보 은닉 (Information Hiding / Che giấu thông tin)
- 한 모듈 내부에 포함된 절차와 자료들의 정보가 감추어져 다른 모듈이 접근하거나 변경하지 못하도록 하는 기법이다. (Kỹ thuật che giấu thông tin về thủ tục và dữ liệu bên trong một module để các module khác không thể truy cập hoặc sửa đổi.)
- 모듈을 독립적으로 수행할 수 있다. (Có thể thực thi module một cách độc lập.)
- 수정, 시험, 유지보수가 용이하다. (Dễ dàng sửa đổi, kiểm thử, bảo trì.)
- 정보 은닉을 표기할 때 private의 의미는 은닉이다. (Khi ký hiệu che giấu thông tin, 'private' mang ý nghĩa là che giấu.)
- **Ví dụ (Example):** Trong OOP, khai báo các biến là `private` và chỉ cho phép truy cập qua `getter/setter`.

### 029. 파이프 - 필터 패턴 (Pipe-Filter Pattern)
- 시스템의 처리 결과물을 파이프를 통해 전달받아 처리한 후 그 결과물을 다시 파이프를 통해 다음 시스템으로 넘겨주는 패턴이다. (Pattern nhận kết quả xử lý qua Pipe, xử lý (Filter) rồi lại chuyển kết quả đó qua Pipe cho hệ thống tiếp theo.)
- 데이터 변환으로 인한 오버헤드가 발생한다. (Phát sinh overhead do chuyển đổi dữ liệu.)
- **Ví dụ (Example):** Câu lệnh trong Linux: `ls | grep "txt" | sort`. Ký tự `|` chính là Pipe, còn `grep`, `sort` là các Filter.

### 030. MVC (Model-View-Controller) 패턴
- 모델 (Model): 서브시스템의 핵심 기능과 데이터를 보관함. (Lưu trữ chức năng cốt lõi và dữ liệu - Logic nghiệp vụ.)
- 뷰 (View): 사용자에게 정보를 표시함. (Hiển thị thông tin cho người dùng - UI.)
- 컨트롤러 (Controller): 사용자로부터 입력된 변경 요청을 처리하기 위해 모델에게 명령을 보냄. (Xử lý yêu cầu thay đổi từ người dùng và gửi lệnh cho Model.)

### 039. 모듈 (Module)
- 모듈화를 통해 분리된 시스템의 각 기능들이다. (Là các chức năng của hệ thống được tách ra thông qua quá trình module hóa.)
- 단독으로 컴파일이 가능하다. (Có thể biên dịch độc lập.)
- 재사용 할 수 있다. (Có thể tái sử dụng.)
- 다른 모듈에서의 접근이 가능하다. (Các module khác có thể truy cập được.)

### 040 & 041. 결합도 (Coupling) 의 종류와 정도 (Các loại Độ kết dính / Mức độ từ Yếu → Mạnh)
- *Kết dính càng YẾU (약함) càng TỐT, càng MẠNH (강함) càng XẤU.*
- **자료 (Data) 결합도 (Yếu nhất - Tốt nhất):** 모듈 간의 인터페이스가 자료 요소로만 구성될 때. (Chỉ truyền dữ liệu đơn giản giữa các module).
- **스탬프 (Stamp) 결합도:** 배열이나 레코드 등의 자료 구조가 전달될 때. (Truyền cấu trúc dữ liệu như mảng, bản ghi).
- **제어 (Control) 결합도:** 제어 신호를 이용하여 통신하거나 제어 요소를 전달. (Truyền cờ điều khiển - control flag/signal).
- **외부 (External) 결합도:** 데이터(변수)를 외부의 다른 모듈에서 참조할 때. (Tham chiếu biến toàn cục bên ngoài).
- **공통 (Common) 결합도:** 공유되는 공통 데이터 영역을 여러 모듈이 사용할 때. (Nhiều module cùng dùng chung một vùng dữ liệu chung - global data).
- **내용 (Content) 결합도 (Mạnh nhất - Xấu nhất):** 한 모듈이 다른 모듈의 내부 기능 및 그 내부 자료를 직접 참조하거나 수정. (Module này trực tiếp can thiệp nội bộ module kia).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TSCNCN** (Tư - Stamp - Chế - Ngoại - Công - Nội): **Tính Sao Cho Nhẹ Cả Người**. (Từ Tốt nhất -> Xấu nhất).

### 043. 주요 응집도 (Cohesion)
- *Độ gắn kết nội bộ. Gắn kết càng MẠNH càng TỐT.*
- **기능적 (Functional) 응집도 (Mạnh nhất - Tốt nhất):** Tất cả các yếu tố bên trong đều hướng tới giải quyết một chức năng duy nhất.
- **순차적 (Sequential) 응집도:** Kết quả đầu ra của hoạt động này là đầu vào của hoạt động kia.
- **통신적 (Communication) 응집도:** Các hoạt động cùng sử dụng chung một dữ liệu đầu vào/ra.
- **절차적 (Procedural) 응집도:** 모듈 안의 구성 요소들이 그 기능을 순차적으로 수행할 경우. (Thực hiện tuần tự theo quy trình nhưng có thể không cùng dữ liệu).
- **시간적 (Temporal) 응집도:** 특정 시간에 처리되는 몇 개의 기능을 모아 하나의 모듈로 작성. (Nhóm các chức năng cần thực hiện cùng một thời điểm, ví dụ: Module khởi tạo hệ thống).
- **논리적 (Logical) 응집도:** Các chức năng có cùng logic được nhóm lại.
- **우연적 (Coincidental) 응집도 (Yếu nhất - Xấu nhất):** 각 구성 요소들이 서로 관련 없는 요소로만 구성된 경우. (Nhóm các thành phần chẳng liên quan gì với nhau).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KTTTTLN** (Kỳ - Thuận - Thông - Tiết - Thời - Luận - Ngẫu): **Không Thể Tin Thằng Trẻ Làm Ngốc**. (Từ Tốt nhất -> Xấu nhất).

### 044. 팬인(Fan-In) / 팬아웃(Fan-Out)
- 팬인 (Fan-In): 어떤 모듈을 제어(호출)하는 모듈의 수. (Số lượng các module gọi/điều khiển module đó -> Mũi tên TRỎ VÀO nó).
- 팬아웃 (Fan-Out): 어떤 모듈에 의해 제어(호출)되는 모듈의 수. (Số lượng các module mà module đó gọi/điều khiển -> Mũi tên TRỎ RA từ nó).
- **Nguyên tắc thiết kế tốt:** Fan-In phải CAO (được dùng lại nhiều), Fan-Out phải THẤP (ít phụ thuộc vào nhiều thằng khác).

## 6. 객체지향 (Hướng Đối Tượng - OOP)

### 031. 메시지 (Message)
- 객체에게 어떤 행위를 하도록 지시하는 명령 또는 요구사항이다. (Là lệnh hoặc yêu cầu chỉ thị cho đối tượng thực hiện một hành vi nào đó.)
- 객체들 간에 상호 작용을 하는 데 사용되는 수단이다. (Là phương tiện dùng để tương tác giữa các đối tượng.)

### 032. 클래스 (Class)
- 공통된 속성과 연산(행위)을 갖는 객체의 집합이다. (Là tập hợp các đối tượng có chung thuộc tính và phép toán (hành vi).)
- 클래스에 속한 각각의 객체를 인스턴스(Instance)라 한다. (Mỗi đối tượng thuộc một class được gọi là Thực thể - Instance).
- 객체지향 프로그램에서 데이터를 추상화하는 단위이다. (Là đơn vị trừu tượng hóa dữ liệu trong lập trình OOP.)

### 033. 캡슐화 (Encapsulation / Đóng gói)
- 데이터와 데이터를 처리하는 함수를 하나로 묶는 것을 의미한다. (Việc bó buộc dữ liệu và hàm xử lý dữ liệu đó thành một khối.)
- 외부 모듈의 변경으로 인한 파급 효과가 적다. (Giảm thiểu hiệu ứng lan truyền khi module bên ngoài thay đổi.)
- 인터페이스가 단순화된다. (Giao diện trở nên đơn giản.)
- 재사용이 용이하다. (Dễ dàng tái sử dụng.)
- **Ví dụ (Example):** Một viên thuốc nhộng (capsule) chứa nhiều bột thuốc bên trong, người dùng chỉ việc uống viên nhộng mà không cần biết tỷ lệ bột bên trong.

### 034. 상속 (Inheritance / Kế thừa)
- 상위 클래스(부모 클래스)의 모든 속성과 연산을 하위 클래스(자식 클래스)가 물려받는 것이다. (Lớp con kế thừa toàn bộ thuộc tính và phương thức của lớp cha.)

### 035. 다형성 (Polymorphism / Đa hình)
- 오버로딩 (Overloading - Nạp chồng): 메소드의 이름은 같지만 인수를 받는 자료형과 개수를 달리하여 여러 기능을 정의할 수 있음. (Cùng tên hàm nhưng khác kiểu/số lượng tham số -> Định nghĩa nhiều chức năng).
- 오버라이딩 (Overriding - Ghi đè): 메소드의 이름은 같지만 메소드 안의 실행 코드를 달리하여 자식 클래스에서 재정의해서 사용할 수 있음. (Cùng tên hàm, định nghĩa lại nội dung code ở lớp con).
- **Ví dụ (Example):** Hàm `add(int a, int b)` và `add(float a, float b)` là Overloading. Lớp Mèo `speak()` kêu Meo, lớp Chó `speak()` kêu Gâu là Overriding.

### 036. 객체지향 분석 방법론 - Coad와 Yourdon 방법
- E-R 다이어그램을 사용하여 객체의 행위를 모델링 한다. (Sử dụng biểu đồ E-R để mô hình hóa hành vi đối tượng.)
- 객체 식별, 구조 식별, 주제 정의, 속성과 인스턴스 연결 정의, 연산과 메시지 연결 정의 등의 과정으로 구성하는 기법이다. (Quy trình gồm: Nhận diện đối tượng, Nhận diện cấu trúc, Định nghĩa chủ đề, Định nghĩa thuộc tính/liên kết instance, Định nghĩa phép toán/thông điệp).

### 037. 럼바우(Rumbaugh)의 분석 기법 (Kỹ thuật phân tích của Rumbaugh)
- 객체(Object) 모델링: 정보 모델링이라고도 하며, 객체들 간의 관계를 규정하여 객체 다이어그램으로 표시하는 것. (Mô hình hóa đối tượng/thông tin: Xác định mối quan hệ giữa các đối tượng và hiển thị bằng Object Diagram).
- 동적(Dynamic) 모델링: 상태 다이어그램을 이용하여 객체들 간의 동적인 행위를 표현하는 모델링. (Mô hình hóa động: Thể hiện hành vi động giữa các đối tượng bằng State Diagram).
- 기능(Functional) 모델링: 자료 흐름도를 이용하여 자료 흐름을 표현한 모델링. (Mô hình hóa chức năng: Thể hiện luồng dữ liệu bằng DFD - Data Flow Diagram).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KĐC** (Khách - Động - Cơ): **Không Đợi Chờ** (Khách thể - Động lực - Cơ năng). (O-D-F)

### 038. 객체지향 설계 원칙 (SOLID 원칙) (Các nguyên tắc thiết kế OOP)
- 단일 책임 원칙 (SRP - Single Responsibility Principle): 객체는 단 하나의 책임만 가져야 한다는 원칙. (Mỗi đối tượng chỉ có MỘT trách nhiệm duy nhất.)
- 개방-폐쇄 원칙 (OCP - Open-Closed Principle): 기존의 코드를 변경하지 않고 기능을 추가할 수 있도록 설계해야 한다는 원칙. (Mở cho việc mở rộng, Đóng cho việc sửa đổi.)
- 리스코프 치환 원칙 (LSP - Liskov Substitution Principle): 자식 클래스는 최소한 자신의 부모 클래스에서 가능한 행위는 수행할 수 있어야 한다는 설계 원칙. (Lớp con có thể thay thế hoàn toàn lớp cha mà không làm hỏng logic.)
- 인터페이스 분리 원칙 (ISP - Interface Segregation Principle): 자신이 사용하지 않는 인터페이스와 의존 관계를 맺거나 영향을 받지 않아야 한다는 원칙. (Nên tách nhỏ Interface, không ép client implement những phương thức không dùng tới.)
- 의존 역전 원칙 (DIP - Dependency Inversion Principle): 추상성이 낮은 클래스보다 추상성이 높은 클래스와 의존 관계를 맺어야 한다는 원칙. (Module cấp cao không nên phụ thuộc module cấp thấp, cả 2 nên phụ thuộc vào abstraction/interface.)
- 💡 **Mẹo ghi nhớ (Mnemonic):** Tên các chữ cái đầu tiếng Anh tạo thành chữ **S-O-L-I-D**.


## 7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)

### NS 차트 (Nassi-Shneiderman Chart)
- 논리의 기술에 중점을 둔 도형을 이용한 표현 방법이다. (Là phương pháp biểu diễn bằng hình khối, trọng tâm vào việc mô tả logic.)
- 연속, 선택 및 다중 선택, 반복 등의 제어 논리 구조를 표현한다. (Thể hiện cấu trúc logic điều khiển như tuần tự, lựa chọn (if-else), đa lựa chọn (switch), lặp lại (while/for).)
- GOTO나 화살표를 사용하지 않는다. (Không sử dụng lệnh GOTO hay mũi tên.)
- 시각적으로 명확히 식별하는 데 적합하다. (Thích hợp để nhận diện rõ ràng về mặt thị giác.)
- 이해하기 쉽고, 코드 변환이 용이하다. (Dễ hiểu và dễ chuyển đổi thành code.)
- **Ví dụ (Example):** Dùng các khối hình chữ nhật xếp chồng lên nhau để biểu diễn một hàm tính toán thay vì dùng sơ đồ khối (Flowchart) có mũi tên rườm rà.

### 재사용 (Reuse / Tái sử dụng)
- 이미 개발된 기능을 새로운 시스템이나 기능 개발에 사용할 수 있는 정도를 의미한다. (Mức độ có thể sử dụng lại các chức năng đã phát triển cho hệ thống hoặc chức năng mới.)
- 재사용 규모에 따른 분류: 함수와 객체, 컴포넌트, 애플리케이션. (Phân loại theo quy mô: Hàm/Đối tượng, Component, Ứng dụng).

### 효과적인 모듈 설계 방안 (Phương án thiết kế module hiệu quả)
- 결합도는 줄이고 응집도는 높인다. (Giảm độ kết dính (Coupling) và tăng độ gắn kết (Cohesion).)
- 복잡도와 중복성을 줄인다. (Giảm độ phức tạp và sự trùng lặp.)
- 일관성을 유지시킨다. (Duy trì tính nhất quán.)
- 모듈의 기능은 지나치게 제한적이어서는 안 된다. (Chức năng của module không nên quá hạn hẹp.)
- 유지보수가 용이해야 한다. (Phải dễ dàng bảo trì.)
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CUTK** (Cao Ứng - Thấp Kết): **Cứ Ứng Thật Kỹ** -> 응집도 높게(Cohesion High), 결합도 낮게(Coupling Low).

### 주요 코드 (Các loại Code cơ bản)
- 순차 코드 (Sequence Code): 일정 기준에 따라서 차례로 일련번호를 부여하는 방법. (Gắn số thứ tự liên tiếp theo một tiêu chuẩn định sẵn - VD: 001, 002, 003).
- 표의 숫자 코드 (Significant Digit Code): 코드화 대상 항목의 중량, 면적, 용량 등의 물리적 수치를 적용시키는 방법. (Sử dụng trực tiếp các chỉ số vật lý như trọng lượng, kích thước vào mã - VD: Tivi 50 inch thì mã là TV-50).

## 8. 디자인 패턴 (Design Patterns)

### 디자인 패턴 (Design Pattern) 개요
- 세부적인 구현 방안을 설계할 때 참조할 수 있는 전형적인 해결 방식 또는 예제를 의미한다. (Là những phương pháp giải quyết hoặc ví dụ điển hình có thể tham khảo khi thiết계 chi tiết phương án triển khai.)
- 3가지 유형 (3 Loại chính): 생성 패턴 (Creational), 구조 패턴 (Structural), 행위 패턴 (Behavioral).

### 생성 패턴 (Creational Pattern / Mẫu khởi tạo) - 5 loại
- 객체 생성과 관련된 패턴. (Liên quan đến việc tạo đối tượng.)
- **빌더 (Builder):** 작게 분리된 인스턴스를 건축하듯이 조합하여 객체를 생성함. (Tạo đối tượng bằng cách lắp ráp các phần nhỏ như xây nhà.)
- **팩토리 메소드 (Factory Method):** 객체 생성을 서브 클래스에서 처리하도록 분리하여 캡슐화한 패턴으로, 가상 생성자(Virtual Constructor) 패턴이라고도 함. (Giao việc tạo đối tượng cho lớp con, còn gọi là Virtual Constructor).
- **프로토타입 (Prototype):** 원본 객체를 복제하는 방법으로 객체를 생성함. (Tạo đối tượng bằng cách copy/clone từ đối tượng gốc).
- **싱글톤 (Singleton):** 생성된 객체를 여러 프로세스가 동시에 참조할 수는 없음 (하나의 객체만 생성). (Đảm bảo chỉ có 1 instance duy nhất được tạo ra).
- **추상 팩토리 (Abstract Factory):** 서로 연관·의존하는 객체들의 그룹으로 생성하여 추상적으로 표현함. (Tạo ra một nhóm các đối tượng có liên quan với nhau thông qua interface).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **BFPSA** (Build - Fact - Pro - Sing - Ab): **Bạn Phải Phạt Sợ Ai**.

### 구조 패턴 (Structural Pattern / Mẫu cấu trúc) - 7 loại
- 클래스나 객체를 조합해 더 큰 구조를 만드는 패턴. (Kết hợp lớp/đối tượng thành cấu trúc lớn hơn).
- **어댑터 (Adapter):** 인터페이스를 다른 클래스가 재사용할 수 있도록 변환함. (Biến đổi interface để lớp khác dùng được, giống như cục sạc chuyển đổi điện).
- **브리지 (Bridge):** 서로가 독립적으로 확장할 수 있도록 구성함. (Tách phần trừu tượng và phần thực thi để cả 2 có thể phát triển độc lập).
- **컴포지트 (Composite):** 복합 객체와 단일 객체를 구분 없이 다루고자 할 때 사용함. (Xử lý đối tượng đơn lẻ và đối tượng phức hợp (nhóm) theo cùng một cách, cấu trúc cây).
- **데코레이터 (Decorator):** 부가적인 기능을 추가하기 위해 다른 객체들을 덧붙이는 방식으로 구현함. (Gắn thêm tính năng mới vào đối tượng có sẵn giống như trang trí).
- **퍼싸드 (Facade):** 복잡한 서브 클래스들을 피해 더 상위에 인터페이스를 구성함. (Tạo một interface cấp cao đơn giản để che giấu hệ thống con phức tạp bên dưới).
- **플라이웨이트 (Flyweight):** 가능한 한 인스턴스를 공유해서 사용함으로써 메모리를 절약하는 패턴. (Chia sẻ instance để tiết kiệm bộ nhớ, tái sử dụng những gì giống nhau).
- **프록시 (Proxy):** 접근이 어려운 객체와 여기에 연결하려는 객체 사이에서 인터페이스 역할을 수행하는 패턴. (Người đại diện, đứng giữa kiểm soát truy cập vào đối tượng thực).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **ABCDFFP** (Ad - Bri - Com - Dec - Fac - Fly - Pro): **Anh Bán Cơm Đĩa Phải Phạt Phi**.

### 행위 패턴 (Behavioral Pattern / Mẫu hành vi) - 11 loại
- 객체 간의 상호작용이나 책임 분배에 대한 패턴. (Giao tiếp và phân bổ trách nhiệm giữa các đối tượng).
- **책임 연쇄 (Chain of Responsibility):** 요청을 한 객체가 처리하지 못하면 다음 객체로 넘어가는 형태. (Xử lý dây chuyền, ai làm được thì làm, không thì chuyển người tiếp theo).
- **커맨드 (Command):** 재이용하거나 취소할 수 있도록 요청에 필요한 정보를 저장함. (Đóng gói yêu cầu thành đối tượng, dễ dàng undo/redo).
- **인터프리터 (Interpreter):** 언어에 문법 표현을 정의함. (Định nghĩa ngữ pháp cho ngôn ngữ).
- **반복자 (Iterator):** 접근이 잦은 객체에 대해 동일한 인터페이스를 사용하도록 함. (Duyệt qua các phần tử của tập hợp mà không cần biết cấu trúc bên trong).
- **중재자 (Mediator):** 복잡한 상호 작용을 캡슐화하여 객체로 정의함. (Làm trung gian liên lạc giữa các đối tượng để giảm sự phụ thuộc chéo).
- **메멘토 (Memento):** 객체를 해당 시점의 상태로 돌릴 수 있는 기능을 제공, C + Z와 같은 되돌리기 기능을 개발할 때 주로 이용함. (Lưu trạng thái để khôi phục/Undo).
- **옵서버 (Observer):** 객체에 상속되어 있는 다른 객체들에게 변화된 상태를 전달함. (Một đối tượng thay đổi trạng thái, các đối tượng đăng ký theo dõi sẽ được thông báo - VD: Đăng ký kênh YouTube).
- **상태 (State):** 객체의 상태에 따라 동일한 동작을 다르게 처리해야 할 때 사용함. (Thay đổi hành vi khi trạng thái đối tượng thay đổi).
- **전략 (Strategy):** 동일한 계열의 알고리즘들을 상호 교환할 수 있게 정의함. (Đóng gói thuật toán để có thể thay đổi linh hoạt lúc runtime).
- **템플릿 메소드 (Template Method):** 하위 클래스에서 세부 처리를 구체화함. (Lớp cha định nghĩa khung thuật toán, lớp con implement chi tiết).
- **방문자 (Visitor):** 처리 기능을 분리하여 별도의 클래스로 구성함. (Tách logic xử lý khỏi cấu trúc dữ liệu, đối tượng Visitor đi "thăm" các phần tử để xử lý).

## 9. 요구사항 및 시스템 파악 (Yêu cầu & Phân tích Hệ thống)

### 요구사항 검증 방법 (Phương pháp xác minh yêu cầu)
- **동료검토 (Peer Review):** 작성자가 명세서 내용을 직접 설명하면서 결함을 발견함. (Tác giả trực tiếp giải thích tài liệu để đồng nghiệp tìm lỗi - Phi chính thức).
- **워크스루 (Walk Through):** 미리 배포한 명세서를 사전 검토한 후 결함을 발견함. (Phát tài liệu trước, sau đó họp để tìm lỗi - Phi chính thức).
- **인스펙션 (Inspection):** 작성자를 제외한 다른 검토 전문가들이 결함을 발견함. (Các chuyên gia khác (không phải tác giả) kiểm tra chặt chẽ để tìm lỗi - **Chính thức**).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **PWI** (Peer - Walk - Inspect): **Phát Web In**. Inspection là khắt khe và chính thức nhất (공식적).

### 미들웨어 (Middleware)
- 분산 컴퓨팅 환경에서 서로 다른 기종 간을 연결한다. (Kết nối các nền tảng khác nhau trong môi trường điện toán phân tán).
- 운영체제와 응용 프로그램 사이에서 다양한 서비스를 제공한다. (Cung cấp các dịch vụ nằm giữa HĐH và Ứng dụng).
- 위치 투명성을 제공한다. (Cung cấp tính trong suốt về vị trí - User không cần biết server nằm đâu).
- 사용자가 미들웨어의 내부 동작을 확인하려면 별도의 응용 소프트웨어를 사용해야 한다.
- **종류 (Phân loại):** DB, RPC (Remote Procedure Call), MOM (Message Oriented Middleware), TP-Monitor (Transaction Processing Monitor), ORB (Object Request Broker), WAS (Web Application Server).

### 스크럼(Scrum) 상세 (Chi tiết về Scrum)
- **제품 책임자 (PO; Product Owner):** 요구사항을 작성하고 우선순위를 결정하는 주체. (Người đại diện khách hàng, tạo và quản lý thứ tự ưu tiên của Product Backlog).
- **스크럼 마스터 (SM; Scrum Master):** 스크럼 회의를 주관하고 장애 요소를 해결하는 가이드. (Người hướng dẫn, giải quyết khó khăn cho team, không phải là sếp quản lý).
- **개발팀 (Development Team):** 디자이너, 테스터 등 개발에 참여하는 모든 인원 (7~8명). (Nhóm đa chức năng trực tiếp làm ra sản phẩm).
- **제품 백로그 (Product Backlog):** 모든 요구사항(User Story) 목록. (Danh sách tổng tổng hợp mọi yêu cầu của sản phẩm).
- **스프린트 (Sprint):** 2~4주 주기의 실제 개발 과정. (Vòng lặp phát triển kéo dài 2-4 tuần).
- **일일 스크럼 (Daily Scrum):** 매일 15분, 서서 진행, 소멸 차트(Burn-down Chart) 사용. (Họp đứng 15 phút mỗi ngày cập nhật tiến độ, dùng Burn-down Chart).
- **스프린트 검토/회고 (Sprint Review/Retrospective):** 검토는 제품 시연, 회고는 프로세스 cải tiến. (Review = Demo sản phẩm; Retrospective = Rút kinh nghiệm quy trình).

### XP 주요 실천 방법 (Các kỹ thuật thực hành của XP)
- **짝 프로그래밍 (Pair Programming):** 2 người cùng code trên 1 máy tính.
- **공동 코드 소유 (Collective Ownership):** Code là của chung, ai cũng có quyền sửa.
- **테스트 주도 개발 (TDD - Test-Driven Development):** Viết Test case trước, viết Code sau.
- **전체 팀 (Whole Team):** Khách hàng và team phát triển làm việc cùng nhau như 1 đội.
- **계속적인 통합 (Continuous Integration):** Tích hợp code liên tục (CI) ngay khi xong 1 task.
- **리팩토링 (Refactoring):** Cải thiện cấu trúc code mà không đổi chức năng bên ngoài.
- **소규모 릴리즈 (Small Releases):** Cập nhật/Phát hành các phiên bản nhỏ liên tục.

### 현행 시스템 파악 (Phân tích hệ thống hiện tại)
- 1단계: 시스템 구성, 기능, 인터페이스 파악. (Bước 1: Nắm bắt Cấu trúc, Chức năng, Interface).
- 2단계: 아키텍처 및 소프트웨어 구성 파악. (Bước 2: Nắm bắt Kiến trúc và Phần mềm).
- 3단계: 하드웨어 및 네트워크 구성 파악. (Bước 3: Nắm bắt Phần cứng và Mạng).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KGI -> AS -> HN** (Kéo Ghế In -> Áo Sơ -> Hát Nhép) -> Giống như quy trình từ phần mềm đến phần cứng.

### 운영체제 (OS - Operating System)
- 컴퓨터 시스템의 자원들을 효율적으로 관리하며, 환경을 제공하는 소프트웨어이다. (Là phần mềm quản lý tài nguyên máy tính hiệu quả và cung cấp môi trường chạy ứng dụng).
- 고려사항 (Các yếu tố cần cân nhắc khi chọn): 가용성 (Tính sẵn sàng), 성능 (Hiệu năng), 기술 지원 (Hỗ trợ kỹ thuật), 주변 기기 (Thiết bị ngoại vi), 구축 비용 (Chi phí).

### 데이터베이스 관리 시스템 (DBMS)
- 사용자와 데이터베이스 사이에서 정보를 생성하고 관리해 주는 소프트웨어이다. (Phần mềm nằm giữa User và Database để quản lý dữ liệu - giải quyết vấn đề trùng lặp và phụ thuộc).
- 고려사항: 가용성, 성능, 기술 지원, 상호 호환성 (Tính tương thích), 구축 비용.


## 10. 요구사항 심화 (Yêu cầu chuyên sâu)

### 요구사항의 유형 (Các loại yêu cầu)
- **기능 요구사항 (Functional Requirements):** 시스템이 무엇을 하는지, 어떤 기능을 하는지에 대한 사항. (Hệ thống làm gì, chức năng nào. Ví dụ: Phải có nút Lưu, phải tính toán được thuế).
- **비기능 요구사항 (Non-functional Requirements):** 성능 (Hiệu năng), 인터페이스 (Giao diện), 데이터 (Dữ liệu), 테스트 (Kiểm thử), 보안 (Bảo mật), 품질 (Chất lượng), 제약사항 (Ràng buộc), 프로젝트 관리/지원 (Quản lý dự án/Hỗ trợ). (Là các yêu cầu không trực tiếp là chức năng nhưng quyết định chất lượng hệ thống).
- **Ví dụ (Example):** Chức năng giỏ hàng là "기능" (Chức năng). Nhưng giỏ hàng phải load trong 0.5 giây là "성능" (Hiệu năng - Phi chức năng).

### 요구사항 도출 (Requirement Elicitation / Thu thập yêu cầu)
- 기법 (Kỹ thuật): 청취와 인터뷰 (Lắng nghe & Phỏng vấn), 설문 (Khảo sát), 브레인스토밍 (Brainstorming), 워크샵 (Workshop), 프로토타이핑 (Prototyping), 유스케이스 (Use Case).

### 요구사항 명세 기법 (Kỹ thuật Đặc tả yêu cầu)
- **정형 명세 기법 (Formal Specification):** 수학적 기호, 정형화된 표기법 사용 (Dùng ký hiệu toán học). 정확하고 간결, 일관성 있음, 하지만 표기법이 어려워 사용자가 이해하기 어려움. (Chính xác, nhất quán nhưng khó hiểu với user). 종류: VDM, Z, Petri-net, CSP.
- **비정형 명세 기법 (Informal Specification):** 일반 명사, 동사 등의 자연어를 기반으로 서술 또는 다이어그램 작성. (Dùng ngôn ngữ tự nhiên/biểu đồ). 의사소통이 용이하지만 작성자에 따라 해석이 달라질 수 있음. (Dễ giao tiếp nhưng dễ gây hiểu nhầm). 종류: FSM, Decision Table, ER모델링, State Chart.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CTPT** (Chính-Toán-Phi-Tự) -> **Chăm Toán Phải Tốt** -> 정형 = 수학적 (Chính thức = Toán học), 비정형 = 자연어 (Phi chính thức = Tự nhiên).

### 요구사항 분석을 위한 CASE 도구 (Công cụ CASE tự động hóa phân tích)
- **SADT:** SoftTech사 개발, 구조적 분석 및 설계 도구. (Công cụ phân tích cấu trúc của SoftTech).
- **SREM (RSL/REVS):** TRW사 개발, 실시간 처리 소프트웨어 요구사항 기술. (Công cụ cho hệ thống thời gian thực, dùng RSL và REVS).
- **PSL/PSA:** 미시간 대학 개발. (Phát triển bởi ĐH Michigan).
- **TAGS:** 개발 주기 전 과정에 이용할 수 있는 통합 자동화 도구. (Công cụ tích hợp toàn bộ vòng đời).

## 11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)

### 웹 애플리케이션 서버 (WAS - Web Application Server)
- 동적인 콘텐츠를 처리하기 위해 사용되는 미들웨어. (Middleware xử lý các nội dung web động thay vì web tĩnh).
- 종류: Tomcat, GlassFish, JBoss, Jetty, JEUS, Resin, WebLogic, WebSphere.

### 자료 흐름도 (DFD) 표기법 차이 (Khác biệt ký hiệu DFD)
- **Yourdon/DeMarco:** 프로세스를 원(원형)으로 표시. (Process là hình tròn).
- **Gane/Sarson:** 프로세스를 둥근 사각형으로 표시. (Process là hình chữ nhật bo góc).

### HIPO Chart의 종류 (Các loại biểu đồ HIPO)
- **가시적 도표 (Visual Table of Contents):** 시스템의 전체적인 기능과 흐름을 보여주는 계층(Tree) 구조도. (Cấu trúc cây tổng thể).
- **총체적 도표 (Overview Diagram):** 입력, 처리, 출력에 대한 전반적인 정보를 제공. (Cung cấp thông tin tổng quan I-P-O).
- **세부적 도표 (Detail Diagram):** 기본 요소들을 상세히 기술하는 도표. (Mô tả chi tiết các yếu tố cơ bản).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **GTT** (Gia - Tổng - Tế): **Giữ Trật Tự**.

### 클래스 다이어그램 심화 (Class Diagram chi tiết)
- **클래스 (Class):** 3개의 구획으로 나뉨 (Chia làm 3 phần). 이름 (Tên class), 속성 (Attribute/Biến), 오퍼레이션 (Operation/Hàm, Phương thức).
- **관계 (Relationships) 심화:**
  - **연관 (Association):** 2개 이상의 사물이 서로 관련되어 있음 (Mũi tên ngang).
  - **집합 (Aggregation):** 하나의 사물이 다른 사물에 포함되어 있는 관계 (Hình thoi rỗng). (Ví dụ: Máy tính và Chuột - Mất máy tính chuột vẫn tồn tại).
  - **포함 (Composition):** 집합 관계의 특수한 형태, 포함하는 사물의 변화가 포함되는 사물에게 영향을 미치는 관계 (Hình thoi đặc). (Ví dụ: Tòa nhà và Căn phòng - Phá tòa nhà thì phòng cũng mất).

### 스테레오 타입 (Stereotype) 추가
- `<<include>>`: 연결된 다른 UML 요소에 대해 포함 관계. (Quan hệ Bắt buộc phải có - Bắt buộc thực hiện Use case kia).
- `<<extend>>`: 확장 관계. (Quan hệ Tùy chọn/Mở rộng - Có thể thực hiện hoặc không).
- `<<interface>>`: 인터페이스 정의. (Định nghĩa Interface).
- `<<exception>>`: 예외 정의. (Định nghĩa Ngoại lệ).
- `<<constructor>>`: 생성자 역할. (Đóng vai trò Hàm khởi tạo).

### 순차 다이어그램 심화 (Sequence Diagram chi tiết)
- **생명선 (Lifeline):** 객체가 메모리에 존재하는 기간 (Đường nét đứt sổ dọc xuống).
- **실행 상자 (Active Box):** 객체가 메시지를 주고받으며 구동되고 있음을 표현 (Hình chữ nhật nằm trên đường sinh mệnh).

### 사용자 인터페이스(UI) 특성 (Đặc tính của UI)
- 소프트웨어 영역 중 변경이 가장 많이 발생한다. (Là phần thường xuyên bị thay đổi nhất trong phần mềm).
- 최소한의 노력으로 원하는 결과를 얻을 수 있게 한다. (Giúp user đạt kết quả mong muốn với nỗ lực ít nhất).

## 12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)

### 사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)
- **VUI (Voice User Interface):** 사람의 음성으로 기기를 조작하는 인터페이스. (Giao diện điều khiển bằng giọng nói - VD: Bixby, Alexa).
- **OUI (Organic User Interface):** 모든 사물과 사용자 간의 상호작용을 위한 인터페이스 (사물 인터넷, VR, AR, MR 등). (Giao diện hữu cơ, tương tác vật lý/thực tế ảo).

### 사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)
- **사용자 중심 (User-centric):** 실사용자에 대한 이해가 바탕이 되어야 함. (Dựa trên sự hiểu biết về người dùng thực tế).
- **사용성 (Usability):** 설계 시 가장 우선적으로 고려해야 함. (Ưu tiên hàng đầu khi thiết kế - dễ hiểu, dễ dùng).
- **심미성 (Aesthetics):** 디자인적으로 완성도 높게 그래픽 요소 배치. (Bố trí đồ họa thẩm mỹ cao).
- **오류 발생 해결 (Error Recovery):** 오류 발생 시 쉽게 인지하고 해결할 수 있도록 설계. (Giúp user dễ nhận biết và khắc phục lỗi).

### UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)
- **와이어프레임 (Wireframe):** 개략적인 레이아웃이나 뼈대 설계 (손그림, 스케치). (Khung xương, layout sơ lược).
- **목업 (Mockup):** 실제 화면과 유사하게 만든 정적인 형태의 모형. (Mô hình tĩnh giống thật nhưng không chạy được logic).
- **스토리보드 (Storyboard):** 와이어프레임 + 콘텐츠 설명 + 페이지 이동 흐름. 디자이너/개발자의 최종 참고 문서. (Tài liệu chi tiết nhất gồm wireframe + mô tả nội dung + luồng di chuyển).
- **프로토타입 (Prototype):** 인터랙션을 적용하여 실제 구현된 것처럼 테스트 가능한 동적인 모형. (Mô hình động có tương tác, test thử được).
- **유스케이스 (Use Case):** 사용자 측면의 요구사항 기술. (Mô tả yêu cầu chức năng từ góc nhìn người dùng).

### UI 주요 요소 (Các thành phần UI)
- **체크 박스 (Check Box):** 1개 이상의 값을 선택할 수 있는 버튼. (Chọn nhiều - Multiple choice).
- **라디오 버튼 (Radio Button):** 여러 항목 중 하나만 선택할 수 있는 버튼. (Chọn 1 - Single choice).
- **텍스트 박스 (Text Box):** 데이터를 입력/수정하는 상자. (Hộp nhập văn bản).
- **콤보 상자 (Combo Box):** 목록에서 선택하거나 새로 입력할 수 있는 상자. (Dropdown list có thể gõ thêm text).
- **목록 상자 (List Box):** 목록만 표시하고 새로 입력할 수는 없는 상자. (Chỉ chọn từ list có sẵn, không được gõ).

### 상위 설계와 하위 설계 (Thiết kế bậc cao và Bậc thấp)
- **상위 설계 (High-level Design):** 아키텍처 설계, 예비 설계. 대상: 시스템 전체 구조 (DB, Interface). (Thiết kế tổng thể, kiến trúc).
- **하위 설계 (Low-level Design):** 모듈 설계, 상세 설계. 대상: 시스템 내부 구조, 컴포넌트, 알고리즘. (Thiết kế chi tiết module, thuật toán).

### 소프트웨어 아키텍처 품질 속성 (Thuộc tính chất lượng Kiến trúc)
- **시스템 측면 (Hệ thống):** 성능, 보안, 가용성, 기능성. (Hiệu năng, bảo mật...).
- **비즈니스 측면 (Kinh doanh):** 시장 적시성 (Time-to-market), 비용과 혜택. (Thời điểm tung ra thị trường, chi phí).
- **아키텍처 측면 (Kiến trúc):** 개념적 무결성, 정확성, 완결성. (Tính toàn vẹn, chính xác).

### 협약(Contract)에 의한 설계 (Thiết kế theo hợp đồng)
- 컴포넌트의 정확한 인터페이스를 명세하는 방법. (Đặc tả chính xác interface của component).
- **선행 조건 (Precondition):** 오퍼레이션이 호출되기 전에 참이 되어야 할 조건. (Điều kiện bắt buộc trước khi chạy hàm).
- **결과 조건 (Postcondition):** 오퍼레이션이 수행된 후 만족되어야 할 조건. (Điều kiện phải đạt sau khi chạy hàm).
- **불변 조건 (Invariant):** 오퍼레이션이 실행되는 동안 항상 만족되어야 할 조건. (Điều kiện luôn đúng trong suốt quá trình chạy).

## 13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)

### ISO/IEC 9126 하위 품질 특성 (Đặc tính con của ISO/IEC 9126)
- *Đây là phần rất hay thi, cần ghi nhớ chi tiết.*
- **기능성 (Functionality):** 적절성 (Suitability), 정밀성 (Accuracy), 상호 운용성 (Interoperability), 보안성 (Security), 준수성 (Compliance).
- **신뢰성 (Reliability):** 성숙성 (Maturity), 고장 허용성 (Fault Tolerance), 회복성 (Recoverability).
- **사용성 (Usability):** 이해성 (Understandability), 학습성 (Learnability), 운용성 (Operability), 친밀성 (Attractiveness).
- **효율성 (Efficiency):** 시간 효율성 (Time Behaviour), 자원 효율성 (Resource Behaviour).
- **유지 보수성 (Maintainability):** 분석성 (Analyzability), 변경성 (Changeability), 안정성 (Stability), 시험성 (Testability).
- **이식성 (Portability):** 적용성 (Adaptability), 설치성 (Installability), 대체성 (Replaceability), 공존성 (Co-existence).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KTSHDD** (Kỳ - Tín - Sử - Hiệu - Duy - Di): **Không Tin Sẽ Hư Dần Dần** (Tên 6 đặc tính chính).
  - 유지 보수성: **분변안시** (Phân - Biến - An - Thử).

### 관련 품질 표준 (Các tiêu chuẩn ISO khác)
- **ISO/IEC 25010:** 2011년 9126을 개정한 최신 표준. (Bản cập nhật của 9126).
- **ISO/IEC 12119:** 테스트 절차를 포함한 품질 표준. (Bao gồm quy trình test).
- **ISO/IEC 14598:** 평가자별 제품 평가 활동 규정. (Quy định hoạt động đánh giá).

### 기타 아키텍처 패턴 (Các mẫu kiến trúc bổ sung)
- **마스터-슬레이브 패턴 (Master-Slave):** 마스터가 작업을 분할하고 슬레이브가 처리 결과를 돌려주는 패턴 (장애 허용 시스템, 병렬 컴퓨팅). (Master chia việc, Slave làm rồi trả kết quả -> Hệ thống tính toán song song).
- **브로커 패턴 (Broker):** 사용자가 요청하면 브로커가 적합한 컴포넌트를 연결해 줌 (분산 환경). (Môi giới kết nối User với Component phù hợp -> Hệ thống phân tán).
- **피어-투-피어 패턴 (Peer-To-Peer / P2P):** 각 피어가 클라이언트도 되고 서버도 됨. (Mỗi node vừa là Client vừa là Server).
- **이벤트-버스 패턴 (Event-Bus):** 소스가 이벤트를 발행(Publish)하면 리스너가 구독(Subscribe)하여 처리. (Mô hình Pub/Sub).
- **블랙보드 패턴 (Blackboard):** 모든 컴포넌트가 공유 데이터 저장소(블랙보드)에 접근 (음성 인식, 신호 해석). (Bảng đen dùng chung, các AI agents tự do truy cập -> Nhận diện giọng nói, xử lý tín hiệu).

## 14. 객체지향 심화 (OOP chuyên sâu)

### 다형성 (Polymorphism) 추가 설명
- **오버로딩 (Overloading):** 인수를 받는 자료형과 개수를 달리하여 여러 기능을 정의. (Cùng tên hàm, khác tham số).
- **오버라이딩 (Overriding / 메소드 재정의):** 상위 클래스의 메소드 안의 코드를 자식 클래스에서 재정의. (Lớp con định nghĩa lại hàm của lớp cha).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **Over-load** = Chở thêm đồ (Thêm tham số). **Over-ride** = Lái đè lên vết xe cũ (Ghi đè nội dung hàm).

## 15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)

### 객체지향 분석 방법론 종류 (Các phương pháp phân tích OOP)
- **Rumbaugh (럼바우):** 객체(Object), 동적(Dynamic), 기능(Functional) 모델로 나누어 분석. (Chia làm 3 mô hình).
- **Booch (부치):** 미시적(Micro) 개발과 거시적(Macro) 개발 프로세스 모두 사용. (Dùng cả quy trình vĩ mô và vi mô).
- **Jacobson (제이콥슨):** Use Case(유스케이스)를 강조. (Nhấn mạnh vào Use Case).
- **Coad와 Yourdon:** E-R 다이어그램 사용. (Dùng sơ đồ ER).
- **Wirfs-Brock:** 분석과 설계 간 구분이 없고 연속적으로 수행. (Không phân biệt rõ phân tích và thiết kế, làm liên tục).
- 💡 **Mẹo ghi nhớ (Mnemonic):** R-O, B-M, J-U, C-E, W-L -> **Ra Ôm Bạn Mới, Giữ Út, Cho Em Vui Lây** (Rumbaugh-Object, Booch-Micro, Jacobson-Use case, Coad-ER, Wirfs-Liên tục).

### 공통 모듈 명세 기법 (Kỹ thuật đặc tả Module chung)
- **정확성 (Correctness):** 기능이 필요하다는 것을 알 수 있도록 정확히 작성. (Chính xác, biết rõ cần thiết).
- **명확성 (Clarity):** 중의적으로 해석되지 않도록 명확하게. (Rõ ràng, không hiểu 2 nghĩa).
- **완전성 (Completeness):** 구현에 필요한 모든 것을 기술. (Đầy đủ mọi thứ cần thiết).
- **일관성 (Consistency):** 기능들 간 상호 충돌이 발생하지 않도록. (Nhất quán, không xung đột).
- **추적성 (Traceability):** 요구사항 출처, 관련 시스템 등 관계 파악. (Có thể truy xuất nguồn gốc).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CMHNT** (Chính - Minh - Hoàn - Nhất - Truy): **Chỉ Mong Học Nhất Trường**.

### 코드(Code)의 주요 기능 (Chức năng chính của Code)
- 식별 기능 (Nhận diện), 분류 기능 (Phân loại), 배열 기능 (Sắp xếp), 표준화 기능 (Chuẩn hóa), 간소화 기능 (Đơn giản hóa).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TPBTG** (Thức - Phân - Bài - Tiêu - Giản): **Thích Phá Bài Thì Giảm**.

### 코드의 종류 심화 (Các loại Code chi tiết)
- **순차 코드 (Sequence Code):** 1, 2, 3... (Theo thứ tự).
- **블록 코드 (Block Code):** 공통성 있는 것끼리 블록으로 구분 (1000~1100: Phòng Nhân sự, 1101~1200: Phòng IT).
- **10진 코드 (Decimal Code):** 0~9 분할 반복 (Ví dụ: Mã phân loại sách thư viện Dewey).
- **그룹 분류 코드 (Group Classification):** 대/중/소 분류 (1-01-001).
- **연상 코드 (Mnemonic Code):** 명칭/약호와 관계있는 문자/숫자 (TV-40). (Gợi nhớ).
- **표의 숫자 코드 (Significant Digit):** 물리적 수치 적용 (120-720).
- **합성 코드 (Combined Code):** 2개 이상 코드 조합 (KE-711).

## 16. 디자인 패턴 심화 (Design Patterns chuyên sâu)

### 디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)
- **장점 (Ưu điểm):** 범용적 코딩 스타일(구조 파악 용이), 생산성 향상, 개발 시간/비용 절약, 의사소통 원활, 유연한 대처 가능. (Dễ đọc code, tăng năng suất, tiết kiệm chi phí, dễ giao tiếp, dễ đối phó thay đổi).
- **단점 (Nhược điểm):** 초기 투자 비용 부담, 다른 기반(비객체지향)에는 부적합. (Tốn kém thời gian học ban đầu, không hợp cho mô hình không hướng đối tượng).

### 디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)
- *(Tham khảo lại Mục 8 để biết tên gọi, dưới đây là các đặc điểm từ khóa thường ra thi)*
- **생성 패턴 (5개):**
  - **Abstract Factory:** 인터페이스를 통해 구체적인 클래스에 의존하지 않고 객체 생성. (Tạo đối tượng qua Interface mà không phụ thuộc Class cụ thể).
  - **Builder:** 생성 과정과 표현 방법을 분리. (Tách rời quá trình tạo và cách biểu diễn).
  - **Factory Method:** 상위 클래스는 인터페이스만 정의, 실제 생성은 서브 클래스가. (Lớp cha định nghĩa Interface, lớp con thực sự tạo).
  - **Prototype:** 비용이 큰 경우 복제하여 생성. (Clone khi chi phí tạo mới quá lớn).
  - **Singleton:** 인스턴스가 하나뿐임을 보장. (Đảm bảo chỉ có 1 instance).
- **구조 패턴 (7개):**
  - **Adapter:** 호환성이 없는 클래스들의 인터페이스 변환. (Chuyển đổi interface không tương thích).
  - **Bridge:** 기능(추상층)과 구현(구현부)을 분리. (Tách rời chức năng và phần thực thi).
  - **Composite:** 트리 구조로 구성. (Cấu trúc cây).
  - **Decorator:** 능동적으로 기능들을 확장(덧붙임). (Chủ động mở rộng/thêm tính năng).
  - **Facade:** 통합 인터페이스 제공(Wrapper 객체). (Cung cấp interface tổng hợp).
  - **Flyweight:** 다수의 유사 객체 공유 (메모리 절약). (Chia sẻ nhiều đối tượng giống nhau để tiết kiệm RAM).
  - **Proxy:** 네트워크 연결, 메모리 대용량 객체 접근 등 (인터페이스 역할). (Làm đại diện kết nối mạng, tải đối tượng lớn).

## 17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)

### 요구사항 검증 방법 추가 (Các phương pháp kiểm chứng yêu cầu bổ sung)
- **요구사항 검토 (Requirements Review):** 동료검토, 워크스루, 인스펙션. (Review thủ công bởi người).
- **프로토타이핑 (Prototyping):** 견본품을 만들어 최종 결과물을 예측. (Làm bản nháp/prototype để dự đoán kết quả).
- **테스트 설계 (Test Design):** 요구사항이 현실적으로 테스트 가능한지 검토 (Test Case 생성). (Tạo Test Case để xem yêu cầu có khả thi không).
- **CASE 도구 활용 (CASE Tools):** 일관성 분석(Consistency Analysis)을 통해 요구사항 변경사항 추적 및 분석. (Dùng tool để phân tích tính nhất quán).

### 시스템 연계 기술 (Các công nghệ liên kết hệ thống)
- **DB Link:** DB에서 제공하는 DB Link 객체를 이용. (Dùng trực tiếp link kết nối của DB).
- **API / Open API:** 송신 시스템의 DB에서 데이터를 읽어와 제공하는 프로그램. (Giao diện lập trình ứng dụng mở).
- **연계 솔루션:** EAI 서버와 송·수신 시스템에 설치되는 클라이언트(Client)를 이용. (Giải pháp dùng EAI Server).
- **Socket:** 통신을 위한 소켓을 생성하여 포트를 할당하고 클라이언트와 연결. (Tạo socket và cấp phát port để giao tiếp mạng).
- **Web Service:** WSDL, UDDI, SOAP 프로토콜을 이용. (Dịch vụ web dùng chuẩn SOAP/WSDL).

### 연계 매커니즘 구성요소 (Thành phần cơ chế liên kết)
- **송신 시스템 (Sender System):** 데이터를 전송 형식에 맞게 변환하여 송신. (Hệ thống gửi, chuyển đổi dữ liệu ra định dạng chuẩn).
- **수신 시스템 (Receiver System):** 수신한 데이터를 시스템에 맞게 변환하여 반영. (Hệ thống nhận, chuyển đổi dữ liệu chuẩn vào DB).
- **연계 서버 (Integration Server):** 송수신 현황을 모니터링. (Server trung gian giám sát quá trình truyền dữ liệu).

### 미들웨어(Middleware) 상세 (Chi tiết Middleware)
- 운영체제와 응용 프로그램 사이에서 다양한 서비스를 제공.
- **DB (DataBase):** 2-Tier 아키텍처에 주로 사용, 클라이언트와 원격 DB를 연결. (Kết nối Client-DB).
- **RPC (Remote Procedure Call):** 원격 프로시저를 로컬 프로시저처럼 호출. (Gọi hàm từ xa như gọi hàm cục bộ).
- **MOM (Message Oriented Middleware):** 비동기형 메시지 전달 (이기종 분산 데이터 시스템). (Truyền tin nhắn bất đồng bộ).
- **TP-Monitor (Transaction Processing Monitor):** 온라인 트랜잭션 처리 및 감시 (항공기/철도 예약). (Quản lý giao dịch online tốc độ cao).
- **ORB (Object Request Broker):** CORBA 표준 스펙을 구현한 객체 지향 미들웨어. (Middleware hướng đối tượng chuẩn CORBA).
- **WAS (Web Application Server):** 동적인 콘텐츠를 처리하는 미들웨어. (Xử lý web động).

---

# 3과목: 데이터베이스 (Phần 3: Cơ sở dữ liệu)
*(Lưu ý: Tùy theo chương trình, Database có thể thuộc Subject 1 hoặc 3. Dưới đây là kiến thức cốt lõi về DB)*

## 1. 데이터베이스 기본 (Cơ bản về Cơ sở dữ liệu)

### 정보 시스템과 자료 (Hệ thống thông tin và Dữ liệu)
- **자료 (Data):** 가공되지 않은 단순한 사실이나 결과값. (Dữ liệu thô, chưa qua xử lý. VD: Con số 30, 40).
- **정보 (Information):** 의사 결정에 도움을 줄 수 있는 유용한 형태로, 자료를 가공해서 얻는 결과물. (Thông tin đã xử lý hữu ích. VD: Nhiệt độ trung bình là 35 độ).
- **데이터웨어 하우스 (DataWarehouse):** 의사 결정 지원 시스템을 지원하는 주체적, 통합적, 시간적 데이터의 집합체. (Kho dữ liệu khổng lồ hợp nhất từ nhiều nguồn để phân tích ra quyết định).

### 데이터베이스의 4가지 정의 (4 Định nghĩa của Database)
- **통합된 데이터 (Integrated Data):** 자료의 중복을 배제한 데이터의 모임. (Dữ liệu hợp nhất, loại bỏ trùng lặp).
- **저장된 데이터 (Stored Data):** 컴퓨터가 접근할 수 있는 저장 매체에 저장된 자료. (Dữ liệu được lưu trữ trên máy tính).
- **운영 데이터 (Operational Data):** 조직의 업무를 수행하는 데 반드시 필요한 자료. (Dữ liệu hoạt động thiết yếu của tổ chức).
- **공용 데이터 (Shared Data):** 여러 응용 시스템들이 공동으로 소유하고 유지하는 자료. (Dữ liệu dùng chung).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TTVC** (Thống - Trữ - Vận - Công): **Tin Tưởng Vào Con**.

### 데이터베이스의 4가지 특징 (4 Đặc điểm của Database)
- **실시간 접근성 (Real Time Accessibility):** 수시적이고 비정형적인 질의에 대하여 실시간 응답. (Truy cập và phản hồi theo thời gian thực).
- **계속적인 변화 (Continuous Evolution):** 삽입, 삭제, 갱신으로 항상 최신의 데이터를 유지. (Liên tục thay đổi/cập nhật để giữ dữ liệu mới nhất).
- **동시 공유 (Concurrent Sharing):** 여러 사용자가 동시에 자기가 원하는 데이터를 이용. (Nhiều người dùng chung một lúc).
- **내용에 의한 참조 (Content Reference):** 주소나 위치가 아닌 데이터 '내용(값)'으로 데이터를 찾음. (Tham chiếu bằng Nội dung thay vì Địa chỉ vật lý).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TKĐN** (Thực - Kế - Đồng - Nội): **Thích Kể Đủ Nghe**.

### 기존 파일 처리 방식의 문제점 (Vấn đề của Hệ thống File cũ)
- **종속성 (Dependency):** 응용 프로그램과 데이터 파일이 상호 의존적. (Chương trình phụ thuộc chặt vào cấu trúc file, file đổi thì code phải đổi).
- **중복성 (Redundancy):** 동일한 데이터의 반복. 이로 인해 일관성, 보안성, 경제성, 무결성이 떨어짐. (Trùng lặp dữ liệu gây tốn dung lượng, khó bảo mật, mất tính nhất quán).

### DBMS의 정의와 필수 기능 3가지 (Định nghĩa & 3 Chức năng cốt lõi của DBMS)
- DBMS: 사용자와 DB 사이에서 정보를 생성하고 관리하는 소프트웨어. (Phần mềm quản lý DB).
- **정의 (Definition):** 데이터의 형(Type)과 구조, 제약조건 명시. (Định nghĩa cấu trúc, kiểu dữ liệu, ràng buộc).
- **조작 (Manipulation):** 데이터 검색, 갱신, 삽입, 삭제 등을 처리. (Thao tác dữ liệu: Thêm, sửa, xóa, tìm kiếm).
- **제어 (Control):** 무결성 유지, 보안, 권한 검사, 병행 제어(Concurrency Control). (Kiểm soát: bảo mật, tính toàn vẹn, xử lý đồng thời).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **ĐTK** (Định - Thao - Kiểm / Def-Man-Con): **Đợi Tý Không**.

### 논리적/물리적 독립성 (Tính độc lập dữ liệu)
- **논리적 독립성 (Logical Independence):** 데이터의 논리적 구조를 변경하더라도 응용 프로그램은 변경되지 않음. (Đổi cấu trúc bảng nhưng code app không cần đổi).
- **물리적 독립성 (Physical Independence):** 디스크 등 물리적 구조를 변경하더라도 응용 프로그램에는 영향을 주지 않음. (Thay ổ cứng, đổi chỗ lưu trữ không ảnh hưởng đến app).

## 2. 스키마와 데이터베이스 언어 (Schema & Ngôn ngữ DB)

### 스키마(Schema)의 정의와 3계층 (Schema & 3 Mức)
- **스키마:** 데이터베이스의 구조와 제약조건에 관한 전반적인 명세 (데이터 사전에 저장, 메타 데이터라고도 함). (Đặc tả tổng thể về cấu trúc và ràng buộc của DB - Meta-data).
- **외부 스키마 (External Schema / Subschema / User View):** 사용자나 프로그래머 개인의 입장에서 필요로 하는 논리적 구조. (Góc nhìn của Từng người dùng/Ứng dụng).
- **개념 스키마 (Conceptual Schema / Overall View):** 조직 전체의 통합된 논리적 구조. 보안 및 무결성 규칙 정의 (보통 스키마라 하면 개념 스키마를 의미). (Góc nhìn Tổng thể của toàn tổ chức, do DBA quản lý).
- **내부 스키마 (Internal Schema):** 물리적 저장장치의 입장에서 본 데이터베이스 구조 (실제 저장 방법). (Góc nhìn Vật lý, cách lưu trữ trên đĩa cứng).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **NKN** (Ngoại - Khái - Nội): **Người Khác Nhìn**.

### 데이터베이스 언어 (Database Languages)
- **DDL (Data Definition Language - 데이터 정의어):** DB 구조, 데이터 형식을 정의/수정. (Dùng để định nghĩa/tạo/sửa cấu trúc bảng).
- **DML (Data Manipulation Language - 데이터 조작어):** 데이터를 실질적으로 처리(검색, 삽입, 삭제, 갱신). (Dùng để thao tác dữ liệu: SELECT, INSERT, UPDATE, DELETE).
- **DCL (Data Control Language - 데이터 제어어):** 무결성, 보안, 권한 제어, 회복, 병행수행 제어. (Dùng để kiểm soát quyền và bảo mật: GRANT, REVOKE).

### 데이터베이스 사용자 (Các loại người dùng DB)
- **DBA (DataBase Administrator):** DB 구성 요소 결정, 스키마 정의, 보안/권한 정책 수립, 시스템 감시 등 모든 관리와 운영 책임. (Quản trị viên DB, có quyền cao nhất).
- **응용 프로그래머 (Application Programmer):** DML을 삽입하여 프로그램을 작성하는 전문가. (Lập trình viên viết ứng dụng kết nối DB).
- **일반 사용자 (End User):** 질의어(SQL)나 응용 프로그램을 사용하여 DB에 접근하는 사람. (Người dùng cuối).

### 데이터 모델의 종류 (Các mức độ Mô hình dữ liệu)
- **개념적 데이터 모델 (Conceptual Data Model):** 현실 세계를 추상적 개념으로 표현. (Mô hình khái niệm, dùng hình vẽ ERD để con người dễ hiểu).
- **논리적 데이터 모델 (Logical Data Model):** 컴퓨터가 이해하고 처리할 수 있는 구조로 변환 (관계, 계층, 네트워크 모델). (Mô hình logic, cấu trúc bảng/dữ liệu cho máy tính).

## 3. 데이터 모델링 (Mô hình hóa dữ liệu)

### 데이터 모델 표시 3요소 (3 Yếu tố của Mô hình dữ liệu)
- **구조 (Structure):** 개체 타입 간의 관계로 데이터 구조 및 정적 성질 표현. (Cấu trúc tĩnh của dữ liệu).
- **연산 (Operation):** 실제 데이터를 처리하는 방법. (Các phép toán xử lý dữ liệu).
- **제약조건 (Constraint):** 실제 데이터의 논리적인 제약조건. (Các điều kiện ràng buộc dữ liệu).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CTC** (Cấu - Toán - Chế): **Cứ Thế Chơi**.

### 데이터 모델의 구성 요소 (Thành phần mô hình)
- **개체 (Entity):** 파일 시스템의 레코드에 대응. 사람이 생각하는 개념이나 정보 단위. (Thực thể - tương đương 1 dòng / bản ghi dữ liệu).
- **속성 (Attribute):** 데이터의 가장 작은 논리적 단위 (필드). (Thuộc tính - tương đương 1 cột).
- **관계 (Relationship):** 개체 간의 관계 또는 속성 간의 관계. (Mối quan hệ).

### 개체-관계 모델 (E-R Model)과 다이어그램
- 1976년 Peter Chen 제안. 특정 DBMS를 고려하지 않고 개념적으로 표현. (Do Peter Chen đề xuất, biểu diễn khái niệm, không phụ thuộc hệ quản trị DB nào).
- **E-R 다이어그램 기호 (Ký hiệu E-R):**
  - **사각형 (Hình chữ nhật):** 개체 (Entity).
  - **마름모 (Hình thoi):** 관계 (Relationship).
  - **타원 (Hình elip):** 속성 (Attribute).
  - **밑줄 타원 (Elip gạch chân):** 기본키 속성 (Primary Key).
  - **복수 타원 (Elip kép):** 복합 속성 (Composite Attribute - Ví dụ: Họ tên gồm Họ và Tên).
  - **선 (Đường thẳng):** 개체와 속성 연결 (Link).

### 주요 데이터 모델 종류 (Các loại mô hình DB)
- **관계형 (Relational):** 표(Table) 형태. 1:1, 1:N, M:N 표현. 기본키/외래키 사용. (Dạng bảng, dùng PK/FK để liên kết).
- **계층형 (Hierarchical):** 트리(Tree) 형태. 1:N만 가능. 부모-자식 관계. 사이클 불가. 삭제 시 연쇄 삭제(Triggered Delete). 대표: IMS. (Dạng cây, 1 cha nhiều con, xóa cha thì mất con).
- **망형 (Network):** 그래프(Graph) 형태. N:M 가능. Owner-Member 관계. 대표: DBTG, TOTAL. (Dạng lưới, 1 con nhiều cha).

### 데이터베이스 설계 순서 (Quy trình thiết kế DB)
- **요구 분석 (Phân tích yêu cầu):** 요구 조건 명세서 작성. (Viết đặc tả).
- **개념적 설계 (Thiết kế khái niệm):** 개념 스키마, E-R 다이어그램 작성. (Vẽ ERD).
- **논리적 설계 (Thiết kế logic):** 목표 DBMS에 맞는 논리적 스키마/테이블 설계, 트랜잭션 인터페이스 설계. (Thiết kế bảng).
- **물리적 설계 (Thiết kế vật리):** 디스크에 저장될 물리적 구조(저장 레코드, 인덱스, 접근 경로) 설계. 성능 고려. (Thiết kế lưu trữ ổ đĩa, index, tối ưu hiệu năng).
- **구현 (Triển khai):** DDL로 DB 생성. (Code SQL tạo DB).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **YKLVC** (Yêu - Khái - Logic - Vật - Cụ): **Yêu Không Lo Về Cửa**.

## 4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)

### 릴레이션 (Relation / Table) 구성 요소
- **튜플 (Tuple):** 행(Row), 레코드(Record). 
  - 튜플의 수 = **카디널리티 (Cardinality)** = 기수. (Số lượng dòng).
- **속성 (Attribute):** 열(Column), 필드(Field).
  - 속성의 수 = **디그리 (Degree)** = 차수. (Số lượng cột).
- **도메인 (Domain):** 하나의 속성이 취할 수 있는 같은 타입의 원자값들의 집합. (Tập hợp các giá trị hợp lệ của 1 cột. VD: Cột 'Giới tính' có Domain là 'Nam' và 'Nữ').
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TCTD** (Tuple-Card, Thuộc-Deg): **Tính Cẩn Thận Đi** -> Tuple đi với Cardinality, Cột(속성) đi với Degree.

### 릴레이션의 4가지 특징 (4 Đặc trưng của Bảng quan hệ)
- 튜플의 유일성: 한 릴레이션에 포함된 튜플들은 모두 상이하다. (Không có 2 dòng nào hoàn toàn giống nhau).
- 튜플의 무순서: 튜플 사이에는 순서가 없다. (Thứ tự các dòng không quan trọng).
- 속성의 무순서: 속성들 간의 순서는 중요하지 않다. (Thứ tự các cột không quan trọng).
- 속성값의 원자성: 속성은 더 이상 쪼갤 수 없는 원자값만 저장한다. (Giá trị mỗi ô phải là nguyên tử, không chứa mảng hay list).

### 키(Key)의 종류 (Các loại Khóa)
- **후보키 (Candidate Key):** 튜플을 유일하게 식별하기 위해 사용하는 속성. **유일성**과 **최소성**을 모두 만족해야 함. (Khóa ứng viên: Duy nhất và Ít thuộc tính nhất).
- **기본키 (Primary Key - PK):** 후보키 중에서 선택한 주키. NULL 값을 가질 수 없고 중복 불가. (Khóa chính: Chọn từ Candidate Key, cấm NULL).
- **대체키 (Alternate Key):** 후보키가 둘 이상일 때 기본키를 제외한 나머지 후보키. (Khóa thay thế: Khóa ứng viên không được chọn làm PK).
- **슈퍼키 (Super Key):** 튜플을 구별할 수 있는 속성들의 집합. 유일성은 만족하지만, 최소성은 만족하지 않음. (Siêu khóa: Gom nhiều cột lại để phân biệt, dư thừa cột cũng không sao).
- **외래키 (Foreign Key - FK):** 참조되는 릴레이션의 기본키와 대응되는 속성. (Khóa ngoại: Dùng để liên kết 2 bảng).

### 무결성 (Integrity / Tính toàn vẹn) 제약조건
- **개체 무결성 (Entity Integrity):** 기본키는 NULL이나 중복값을 가질 수 없다. (PK không được NULL hoặc trùng lặp).
- **참조 무결성 (Referential Integrity):** 외래키 값은 NULL이거나 참조 릴레이션의 기본키 값과 동일해야 한다. (FK phải có giá trị tồn tại trong PK bảng mẹ, hoặc NULL).
- **도메인 무결성 (Domain Integrity):** 특정 속성의 값이 그 속성이 정의된 도메인에 속한 값이어야 한다. (Giá trị phải nằm trong khoảng/định dạng hợp lệ).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TTD** (Thực - Tham - Domain): **Thích Thì Dùng**.

## 5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)

### 관계대수와 관계해석 (Đại số quan hệ & Giải tích quan hệ)
- **관계대수 (Relational Algebra):** 절차적 언어 (Procedural). 원하는 정보와 그 정보를 **어떻게** 유도하는지 기술. (Ngôn ngữ thủ tục: Chỉ ra 'Cái gì' và 'Làm thế nào').
- **관계해석 (Relational Calculus):** 비절차적 언어 (Non-procedural). 원하는 정보가 **무엇**인지 만을 정의. (Ngôn ngữ phi thủ tục: Chỉ ra 'Cái gì').

### 순수 관계 연산자 4가지 (4 Phép toán quan hệ thuần túy)
- **Select (σ / 시그마):** 조건을 만족하는 행(튜플)을 구하는 수평 연산. (Chọn ra các hàng thỏa mãn điều kiện).
- **Project (π / 파이):** 제시된 열(속성)만을 추출하는 수직 연산. (Chọn ra các cột cần thiết).
- **Join (▷◁):** 공통 속성을 중심으로 2개의 릴레이션을 하나로 합침. (Kết nối 2 bảng).
- **Division (÷):** R의 속성이 S의 속성값을 모두 가진 튜플에서 S가 가진 속성을 제외하고 구하는 연산. (Phép chia: Lấy ra các giá trị của bảng R có mặt đầy đủ trong bảng S).

### 이상(Anomaly) 현상 (Hiện tượng Dị thường dữ liệu)
- 정규화를 거치지 않아 데이터가 중복될 때 발생하는 예기치 못한 현상. (Lỗi xảy ra do dữ liệu trùng lặp khi chưa chuẩn hóa).
- **삽입 이상 (Insertion):** 원하지 않는 값까지 억지로 삽입해야 하는 현상. (Khi thêm dữ liệu phải thêm cả dữ liệu không mong muốn do bắt buộc).
- **삭제 이상 (Deletion):** 한 튜플을 삭제할 때 의도와 상관없는 값까지 연쇄 삭제되는 현상. (Xóa 1 thông tin kéo theo mất luôn thông tin khác).
- **갱신 이상 (Update):** 일부 정보만 갱신되어 정보의 모순이 생기는 현상. (Cập nhật thiếu sót gây ra mâu thuẫn dữ liệu).

### 정규화(Normalization) 과정과 암기법 (Quy trình chuẩn hóa)
- 잘못 설계된 스키마를 쪼개어 바람직하게 만드는 논리적 설계 단계. (Chia nhỏ bảng để tối ưu dữ liệu).
- **1NF:** 도메인이 원자값 (Mỗi ô chỉ có 1 giá trị duy nhất).
- **2NF:** 부분적 함수 종속 제거 (Loại bỏ phụ thuộc hàm từng phần).
- **3NF:** 이행적 함수 종속 제거 (Loại bỏ phụ thuộc hàm bắc cầu A->B->C).
- **BCNF:** 결정자이면서 후보키가 아닌 것 제거 (Mọi yếu tố quyết định đều phải là khóa ứng viên).
- **4NF:** 다치 종속 제거 (Loại bỏ phụ thuộc đa trị).
- **5NF:** 조인 종속성 이용 (Dùng phụ thuộc Join).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **DBIGDJ** (Do-Bu-I-Gyul-Da-Jo): **Đi Bộ Ít Giúp Đỡ Jo** -> Do (Domain), Bu (부분), I (이행), Gyul (결정자), Da (다치), Jo (조인).

## 6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)

### SQL의 3가지 분류 (Phân loại câu lệnh SQL)
- **DDL (데이터 정의어):** `CREATE`, `ALTER`, `DROP`.
- **DML (데이터 조작어):** `SELECT`, `INSERT`, `DELETE`, `UPDATE`.
- **DCL (데이터 제어어):** `COMMIT` (Lưu vĩnh viễn), `ROLLBACK` (Hoàn tác), `GRANT` (Cấp quyền), `REVOKE` (Thu hồi quyền).

### SELECT 명령어 구조 (Cấu trúc lệnh SELECT)
- `SELECT` [DISTINCT] 속성명 `FROM` 테이블명 `WHERE` 조건 `GROUP BY` 속성 `HAVING` 그룹조건 `ORDER BY` 속성 [ASC|DESC]
- 그룹 함수: COUNT (Số lượng), MAX (Lớn nhất), MIN (Nhỏ nhất), SUM (Tổng), AVG (Trung bình).

### 삽입 / 삭제 / 갱신 문법 (Cú pháp Thêm, Xóa, Sửa)
- **INSERT:** `INSERT INTO` 테이블명(속성) `VALUES` (데이터);
- **DELETE:** `DELETE FROM` 테이블명 `WHERE` 조건; (Lưu ý: DROP là xóa bảng, DELETE là xóa dòng).
- **UPDATE:** `UPDATE` 테이블명 `SET` 속성=데이터 `WHERE` 조건;

### 뷰 (View)의 특징 (Đặc điểm của View)
- 기본 테이블에서 유도된 가상 테이블 (Bảng ảo). 물리적으로 존재하지 않음.
- 필요한 데이터만 보여줘서 자동 보안 제공.
- 뷰의 정의를 `ALTER`로 변경할 수 없으며 (삭제 후 다시 생성해야 함), 인덱스를 가질 수 없음. (Không thể sửa định nghĩa, không có index).
- 생성: `CREATE VIEW`, 삭제: `DROP VIEW 뷰이름 CASCADE` (xóa tất cả liên quan) / `RESTRICT` (nếu đang bị dùng thì cấm xóa).

### 내장 SQL과 시스템 카탈로그 (Embedded SQL & System Catalog)
- **내장 SQL (Embedded SQL):** 응용 프로그램 코드 내에 삽입된 SQL. 수행 결과로 단 하나의 튜플만 반환됨. (SQL nhúng trong code như Java/C, chỉ trả về 1 dòng 1 lúc).
- **시스템 카탈로그 (System Catalog = Data Dictionary):** 스키마, 권한 등 메타 데이터(Meta-Data)를 저장하는 시스템 DB. (Từ điển dữ liệu chứa thông tin cấu trúc DB). 
- 시스템이 자동으로 갱신하며, 사용자는 SELECT로 검색할 수 있지만 갱신(UPDATE/INSERT)은 불가. (Chỉ được xem, không được tự ý sửa).

### 트랜잭션(Transaction)의 정의와 4가지 특성 (Định nghĩa & 4 Đặc tính ACID)
- 데이터베이스 상태를 변환시키는 하나의 논리적 단위 (복구 및 병행 수행의 단위). (Đơn vị công việc logic, ví dụ: 1 giao dịch chuyển tiền).
- **Atomicity (원자성):** 모두 반영되거나 아예 반영되지 않아야 함 (All or Nothing). (Thành công toàn bộ hoặc không có gì).
- **Consistency (일관성):** 트랜잭션 성공 완료 후 항상 일관성 있는 상태 유지. (Kết thúc giao dịch dữ liệu phải đúng đắn, không vi phạm ràng buộc).
- **Isolation (독립성, 격리성):** 실행 중에 다른 트랜잭션이 끼어들 수 없음. (Giao dịch đang chạy thì giao dịch khác không được can thiệp vào giữa chừng).
- **Durability (영속성, 지속성):** 완료된 결과는 영구적으로 반영되어야 함. (Giao dịch xong thì kết quả phải lưu vĩnh viễn dù cúp điện).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **ACID** (Atomicity, Consistency, Isolation, Durability) hoặc **NNĐT** (Nguyên - Nhất - Độc - Trì): **Người Ngoan Đáng Thương**.
