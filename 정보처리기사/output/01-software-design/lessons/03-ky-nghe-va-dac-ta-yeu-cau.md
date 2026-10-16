# 요구공학 및 요구사항 분석·검증 (Kỹ nghệ và Đặc tả yêu cầu phần mềm)

## 학습 목표 (Mục tiêu)
- Nắm vững quy trình phân tích hiện trạng hệ thống (`현행 시스템 분석`) và hạ tầng vận hành: phân biệt máy chủ Web, WAS, DB và 3 kiến trúc lưu trữ dữ liệu chuyên dụng (`DAS, NAS, SAN`).
- Hiểu sâu sắc bản chất của Kỹ nghệ yêu cầu (`요구공학 - Requirements Engineering`): phân biệt 4 pha của Phát triển yêu cầu (도출 $\rightarrow$ 분석 $\rightarrow$ 명세 $\rightarrow$ 확인) và Quản lý yêu cầu (`요구사항 관리`) qua ma trận truy vết RTM.
- Phân biệt tuyệt đối giữa Yêu cầu chức năng (`기능 요구사항`) và Yêu cầu phi chức năng (`비기능 요구사항`) trong các tình huống đề thi trắc nghiệm.
- Làm chủ bộ công cụ phân tích có cấu trúc: Biểu đồ luồng dữ liệu (`자료 흐름도 - DFD`), Từ điển dữ liệu (`자료 사전 - DD`), và Đặc tả tiến trình sơ cấp (`소단위 명세서 - Mini-spec`).
- Phân biệt Kỹ thuật đặc tả hình thức toán học (`정형 명세 - Z, VDM, Petri-net`) với Phi hình thức (`비정형 명세 - FSM, State Chart`); hiểu rõ các công cụ hỗ trợ máy tính `CASE` và `SADT`.
- Phân biệt bản chất giữa Xác minh (`검증 - Verification`) và Xác nhận (`확인 - Validation`), cùng 3 kỹ thuật thẩm tra yêu cầu kinh điển: Duyệt đồng nghiệp (`동료검토`), Duyệt tài liệu (`워크스루`), và Thẩm tra chính thức (`인스펙션`).

## 핵심 키워드 (Từ khóa)
- 현행 시스템 분석 (Phân tích hệ thống hiện tại / Current System Analysis / DAS, NAS, SAN)
- 요구공학 (Kỹ nghệ yêu cầu / Requirements Engineering / 개발 vs 관리)
- 기능 요구사항 vs 비기능 요구사항 (Functional vs Non-functional Requirements)
- 요구사항 도출 기법 (Thu thập yêu cầu: 인터뷰, 브레인스토밍, 델파이 기법 - Delphi Method)
- 자료 흐름도 (Data Flow Diagram - DFD / 버블 차트 / Yourdon vs Gane-Sarson)
- 자료 사전 (Data Dictionary - DD: `=`, `+`, `{}`, `[]`, `()`, `**`)
- 소단위 명세서 (Mini-spec / Process Specification / 원시 프로세스 / 구조적 언어)
- 정형 명세 vs 비정형 명세 (Formal vs Informal Specification / Z, VDM, Petri-net)
- 검증 vs 확인 (Verification vs Validation / Product Right vs Right Product)
- 인스펙션 vs 워크스루 (Inspection vs Walkthrough / FTR - 정형 기술 검토)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Tiếp nối từ các phương pháp luận vòng đời [01-sdlc-va-cac-mo-hinh-vong-doi.md](01-sdlc-va-cac-mo-hinh-vong-doi.md) và [02-phuong-phap-luan-agile-scrum-xp.md](02-phuong-phap-luan-agile-scrum-xp.md), bất kỳ dự án phần mềm nào muốn thành công đều phải bắt đầu từ việc làm rõ: Hệ thống hiện tại đang có gì và Người dùng thực sự cần hệ thống mới giải quyết vấn đề gì.
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết toàn bộ chu trình kỹ nghệ để chuyển hóa các mong muốn mơ hồ, rời rạc của khách hàng thành một bộ Tài liệu đặc tả yêu cầu phần mềm (`SRS - Software Requirements Specification`) có cấu trúc chuẩn xác, có thể đo lường và thẩm định được, làm đầu vào duy nhất cho khâu thiết kế kiến trúc.
- **Dùng đi đâu (Forward Handoff):** Sau khi yêu cầu được phân tích và chốt đường cơ sở (Baseline), bước tiếp theo là mô hình hóa các yêu cầu đó thành các sơ đồ hướng đối tượng chuẩn quốc tế. Toàn bộ kết quả phân tích yêu cầu sẽ được chuyển giao sang [04-mo-hinh-hoa-uml-va-bieu-do.md](04-mo-hinh-hoa-uml-va-bieu-do.md) để biểu diễn bằng ngôn ngữ UML.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nắm vững: các ký hiệu toán tử trong Từ điển dữ liệu DD; sự khác biệt cốt lõi giữa Functional (làm gì) và Non-functional (chất lượng/ràng buộc); câu hỏi kinh điển tiếng Anh phân biệt Verification vs Validation; và bảng phân biệt Inspection vs Walkthrough.
- Đọc TẦNG B để hiểu sâu cấu trúc hạ tầng lưu trữ DAS/NAS/SAN, cơ chế vận hành của phương pháp chuyên gia Delphi, và cách kiểm tra tính khả thi của yêu cầu (Mini-Trace Checklist).

---

## 요구공학 및 요구사항 분석·검증

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Phân tích hiện trạng hệ thống và Hạ tầng vận hành

##### A. Phân tích hiện trạng hệ thống (현행 시스템 분석)
- **Mục đích:** Xác định rõ kiến trúc subsystem, luồng dữ liệu liên kết, hệ điều hành (OS), hệ quản trị cơ sở dữ liệu (DBMS), mạng (Network) và các ràng buộc bản quyền phần mềm hiện có trước khi xây dựng hệ thống mới.
- **Phân loại nghiệp vụ:**
  - `기간 업무 (Core Business / Nghiệp vụ cốt lõi)`: Các nghiệp vụ sống còn mang lại doanh thu hoặc chức năng chính của tổ chức (ví dụ: giao dịch tài khoản trong ngân hàng, xử lý đơn hàng).
  - `지원 업무 (Support Business / Nghiệp vụ hỗ trợ)`: Các nghiệp vụ hành chính, nhân sự, kế toán nội bộ phục vụ cho nghiệp vụ cốt lõi.
- **Chỉ số hiệu năng nền tảng (Platform Performance):**
  - `처리량 (Throughput - Xuyên suất)`: Số lượng giao dịch hoặc tác vụ được xử lý thành công trong một đơn vị thời gian (tính bằng TPS, RPM).
  - `응답 시간 (Response Time - Thời gian phản hồi)`: Khoảng thời gian từ khi người dùng gửi yêu cầu đến khi nhận được phản hồi đầu tiên.
  - `경과 시간 (Turnaround Time - Thời gian quay vòng)`: Tổng thời gian từ lúc gửi lệnh đến khi hoàn thành xử lý toàn bộ tác vụ.
  - `가용성 (Availability - Tính sẵn sàng)`: Tỷ lệ phần trăm thời gian hệ thống hoạt động ổn định và sẵn sàng phục vụ mà không bị gián đoạn (ví dụ: 99.99%).

##### B. Phân biệt 3 kiến trúc lưu trữ dữ liệu (Storage Architecture)

| Kiến trúc lưu trữ | Phương thức kết nối vật lý | Giao thức / Đặc tính kỹ thuật | Ưu nhược điểm & Ứng dụng |
|:---|:---|:---|:---|
| **DAS (Direct Attached Storage)** | Cáp chuyên dụng (SATA, SAS, SCSI) gắn **trực tiếp vào máy chủ** | Không qua mạng mạng LAN | Tốc độ cao, giá rẻ, dễ cài đặt; nhưng khó chia sẻ dữ liệu giữa nhiều máy chủ khác nhau |
| **NAS (Network Attached Storage)** | Kết nối qua hạ tầng mạng **Ethernet LAN** hiện có | Giao thức chia sẻ file: **NFS (Linux), CIFS/SMB (Windows)** | Dễ chia sẻ file cho nhiều máy tính; nhưng băng thông bị nghẽn do cạnh tranh lưu lượng mạng LAN |
| **SAN (Storage Area Network)** | Kết nối qua **mạng cáp quang chuyên dụng riêng biệt (Fiber Channel)** | Xử lý dữ liệu dạng khối (Block-level), switch quang chuyên dụng | Tốc độ truyền tải siêu cao, độ trễ cực thấp, bảo mật tối ưu; phù hợp CSDL lớn ngân hàng; chi phí rất đắt |

---

#### 2. Kỹ nghệ yêu cầu (Requirements Engineering — 요구공학)
Kỹ nghệ yêu cầu là phân ngành kỹ thuật phần mềm chịu trách nhiệm quản lý toàn bộ chu trình sống của yêu cầu, gồm 2 mảng lớn: **요구사항 개발 (Phát triển yêu cầu)** và **요구사항 관리 (Quản lý yêu cầu)**.

##### A. 4 Giai đoạn phát triển yêu cầu (요구사항 개발 프로세스)
$$\text{도출 (Elicitation)} \rightarrow \text{분석 (Analysis)} \rightarrow \text{명세 (Specification)} \rightarrow \text{확인 및 검증 (Validation)}$$

1. **도출 (Elicitation — Thu thập/Khai thác yêu cầu):**
   - Lắng nghe và trích xuất mong muốn của các bên liên quan (Stakeholders).
   - **Các kỹ thuật thu thập chính:**
     - `인터뷰 (Interview)`: Phỏng vấn trực tiếp 1-1 với người dùng và chuyên gia nghiệp vụ.
     - `브레인스토밍 (Brainstorming - Công não)`: Thảo luận nhóm tự do, tuân thủ nghiêm ngặt nguyên tắc **Cấm chỉ trích (비판 금지)** để khuyến khích sinh ra tối đa ý tưởng mới.
     - `델파이 기법 (Delphi Method)`: Kỹ thuật thu thập ý kiến chuyên gia thông qua các bảng hỏi **hoàn toàn ẩn danh (익명성)** qua nhiều vòng lặp, tổng hợp ý kiến để đạt được sự đồng thuận khách quan, triệt tiêu ảnh hưởng của người có uy thế lớn.
     - `워크숍 (JAD / Joint Application Design)`: Hội thảo tập trung giữa người dùng, nhà quản lý và lập trình viên.
2. **분석 (Analysis — Phân tích yêu cầu):**
   - Sàng lọc, phát hiện mâu thuẫn, phân tích tính khả thi về kỹ thuật/ngân sách và xác định thứ tự ưu tiên.
3. **명세 (Specification — Đặc tả yêu cầu):**
   - Biểu diễn các yêu cầu thành tài liệu chuẩn hóa hoặc mô hình kỹ thuật mà các bên có thể hiểu và kiểm tra được. Kết quả đầu ra là **Tài liệu đặc tả yêu cầu phần mềm (`SRS - Software Requirements Specification`)**.
4. **확인 및 검증 (Validation — Xác nhận và Thẩm định):**
   - Rà soát để đảm bảo tài liệu SRS phản ánh chính xác nhu cầu của khách hàng và tuân thủ các chuẩn kỹ thuật trước khi làm căn cứ ký kết đường cơ sở (`베이스라인 - Baseline`).

##### B. Quản lý yêu cầu (요구사항 관리)
- Chịu trách nhiệm theo dõi và kiểm soát các thay đổi đối với đường cơ sở yêu cầu trong suốt dự án.
- Sử dụng **요구사항 추적표 (RTM - Requirements Traceability Matrix)** để ánh xạ 1-1 từ yêu cầu ban đầu $\rightarrow$ thiết kế $\rightarrow$ mã nguồn $\rightarrow$ các kịch bản kiểm thử (Test Case).

---

#### 3. Phân loại yêu cầu: Chức năng vs Phi chức năng
- **핵심 원리 (Nguyên tắc cốt lõi):**
  - **기능 요구사항 (Functional Requirements — Yêu cầu chức năng):**
    - [Hàn/Anh]: `시스템이 무엇을 해야 하는지(What), 시스템의 기능, 입출력, 연산 등 시스템이 제공해야 하는 본연의 기능을 명세한 것이다.`
    - [Tiếng Việt]: Mô tả hệ thống **PHẢI LÀM GÌ**; xác định các chức năng nghiệp vụ cụ thể, dữ liệu đầu vào, quy trình tính toán biến đổi, và dữ liệu đầu ra mà hệ thống cung cấp cho người dùng.
    - *Ví dụ:* "Khách hàng có thể tra cứu số dư tài khoản", "Hệ thống tự động tính lãi suất tiết kiệm cuối tháng và gửi thông báo".
  - **비기능 요구사항 (Non-functional Requirements — Yêu cầu phi chức năng):**
    - [Hàn/Anh]: `시스템이 어떻게 동작해야 하는지(How), 성능, 보안, 신뢰성, 품질, 제약조건 등 시스템이 갖추어야 할 품질 속성과 제약사항을 명세한 것이다.`
    - [Tiếng Việt]: Mô tả hệ thống **PHẢI ĐẠT ĐƯỢC CHẤT LƯỢNG NHƯ THẾ NÀO** hoặc **BỊ RÀNG BUỘC BỞI ĐIỀU KIỆN GÌ**; bao gồm hiệu năng, tính bảo mật, độ tin cậy, tính tương thích, giao diện, tiêu chuẩn công nghệ và quy định pháp lý.
    - *Ví dụ:* "Thời gian phản hồi khi bấm nút thanh toán phải dưới 2 giây", "Dữ liệu mật khẩu người dùng bắt buộc phải mã hóa bằng thuật toán SHA-256", "Hệ thống phải hoạt động 24/7 với độ sẵn sàng đạt 99.9%".

---

#### 4. Kỹ thuật phân tích có cấu trúc (Structured Analysis Tools)

##### A. 자료 흐름도 (Data Flow Diagram - DFD / Bubble Chart)
- **Đặc trưng:** Biểu diễn trực quan luồng di chuyển và biến đổi của dữ liệu trong hệ thống; **chỉ tập trung vào dữ liệu đi đâu và được biến đổi thế nào**, tuyệt đối **không mô tả cấu trúc điều khiển rẽ nhánh hay lặp lại** như lưu đồ thuật toán (Flowchart).
- **4 thành phần cốt lõi của DFD:**

| Thành phần DFD | Ý nghĩa kỹ thuật | Ký hiệu Yourdon/DeMarco | Ký hiệu Gane/Sarson |
|:---|:---|:---:|:---:|
| **프로세스 (Process)** | Thao tác biến đổi dữ liệu đầu vào thành đầu ra | Hình tròn (Circle) | Hình chữ nhật bo góc |
| **자료 흐름 (Data Flow)** | Hướng di chuyển của dòng dữ liệu | Mũi tên có tên dữ liệu | Mũi tên có tên dữ liệu |
| **자료 저장소 (Data Store)** | Nơi lưu trữ dữ liệu tạm thời hoặc vĩnh viễn | Hai đường thẳng song song | Hình chữ nhật hở cạnh phải |
| **단말 (Terminator / External Entity)** | Thực thể bên ngoài cung cấp hoặc nhận dữ liệu | Hình chữ nhật (Rectangle) | Hình chữ nhật đổ bóng |

##### B. 자료 사전 (Data Dictionary - DD)
- **Định nghĩa:** Là "dữ liệu về dữ liệu" (`메타데이터 - Metadata`), mô tả chi tiết định dạng, cấu trúc và ý nghĩa của tất cả các luồng và kho dữ liệu xuất hiện trong DFD.
- **Bảng ký hiệu toán tử bất di bất dịch trong Đề thi:**

| Ký hiệu DD | Tên gọi chuẩn | Ý nghĩa kỹ thuật | Ví dụ minh họa |
|:---:|:---|:---|:---|
| `=` | 정의 (Definition) | Được định nghĩa là / Bao gồm | `Thẻ tín dụng = Số thẻ + Ngày hết hạn + Mã CVV` |
| `+` | 연결 (Concatenation) | Ghép nối / Và (AND) | `Họ tên = Họ + Tên đệm + Tên` |
| `{ }` | 반복 (Iteration) | Lặp lại $N$ lần ($N$ phần tử) | `Đơn hàng = Khách hàng + { Mặt hàng }` |
| `[ \| ]` | 선택 (Selection) | Lựa chọn một trong các phương án (OR) | `Giới tính = [ Nam \| Nữ \| Khác ]` |
| `( )` | 생략 (Option) | Có thể có hoặc không (Tùy chọn) | `Địa chỉ = Tỉnh/TP + Quận/Huyện + (Số nhà)` |
| `* *` | 설명 (Comment) | Chú thích / Diễn giải thêm | `* Điểm GPA từ 0.0 đến 4.0 *` |

##### C. 소단위 명세서 (Mini-spec / Process Specification)
- Sử dụng để mô tả chi tiết logic xử lý bên trong của các **tiến trình sơ cấp (`원시 프로세스 - Primitive Process`)** ở tầng thấp nhất của DFD (khi một hình tròn process không thể chia nhỏ thêm được nữa).
- Được viết bằng: Ngôn ngữ có cấu trúc (Structured Language), Bảng quyết định (Decision Table), hoặc Cây quyết định (Decision Tree).

---

#### 5. Kỹ thuật đặc tả yêu cầu và Công cụ CASE

##### A. Đặc tả hình thức vs Phi hình thức

| Tiêu chí | 정형 명세 기법 (Formal Specification) | 비정형 명세 기법 (Informal Specification) |
|:---|:---|:---|
| **Công cụ diễn đạt** | Ký hiệu toán học, đại số hình thức, logic vị từ | Ngôn ngữ tự nhiên (Hàn/Việt/Anh), sơ đồ trực quan |
| **Ngôn ngữ tiêu biểu** | **Z, VDM, Petri-net, CSP, Larch** | FSM (Máy trạng thái hữu hạn), State Chart, Use Case |
| **Ưu điểm** | Tính chính xác tuyệt đối, không nhập nhằng, có thể kiểm chứng toán học | Dễ viết, dễ đọc, khách hàng phổ thông dễ tiếp cận |
| **Nhược điểm** | Rất khó hiểu, đòi hỏi kiến thức toán chuyên sâu | Dễ phát sinh hiểu lầm do tính đa nghĩa của từ ngữ |

##### B. Công cụ CASE và Phương pháp SADT
- **CASE (Computer-Aided Software Engineering):** Bộ công cụ phần mềm tự động hóa hỗ trợ toàn diện các pha trong vòng đời SDLC (vẽ biểu đồ, sinh mã nguồn, tự động kiểm tra tính nhất quán).
- **SADT (Structured Analysis and Design Technique):** Do hãng SoftTech phát triển, sử dụng các khối biểu đồ chức năng và dữ liệu phân cấp (`블록 차트`) để phân tích hệ thống lớn.

---

#### 6. Thẩm định yêu cầu và Kỹ thuật đánh giá FTR (Formal Technical Review)

##### A. Phân biệt cốt lõi: 검증 (Verification) vs 확인 (Validation)
- **핵심 원리 (Nguyên tắc cốt lõi):**
  - **검증 (Verification — Xác minh):**
    - [Hàn/Anh]: `개발자의 관점에서 "우리가 제품을 올바르게 만들고 있는가?(Are we building the product right?)"를 확인하는 것으로, 규격과 설계서에 맞게 구현되었는지를 점검한다.`
    - [Tiếng Việt]: Đứng từ góc độ của **nhà phát triển**, kiểm tra xem "Chúng ta có đang xây dựng sản phẩm **đúng theo đặc tả kỹ thuật** không?". Mục tiêu là đảm bảo không vi phạm quy chuẩn thiết kế và tài liệu SRS.
  - **확인 (Validation — Xác nhận):**
    - [Hàn/Anh]: `사용자의 관점에서 "우리가 올바른 제품을 만들고 있는가?(Are we building the right product?)"를 확인하는 것으로, 사용자의 실제 요구사항에 부합하는지를 점검한다.`
    - [Tiếng Việt]: Đứng từ góc độ của **người dùng cuối**, kiểm tra xem "Chúng ta có đang xây dựng **đúng sản phẩm mà khách hàng cần** không?". Mục tiêu là đảm bảo sản phẩm giải quyết đúng bài toán nghiệp vụ thực tế.

##### B. 3 Kỹ thuật thẩm tra yêu cầu trong FTR (Formal Technical Review)
1. **동료 검토 (Peer Review — Duyệt đồng nghiệp):** Tác giả tài liệu yêu cầu trực tiếp giải thích nội dung cho 1 đến 2 đồng nghiệp nghe để phát hiện các lỗi sơ đẳng trong thời gian ngắn.
2. **워크스루 (Walkthrough — Duyệt tài liệu có chuẩn bị):** Buổi rà soát **không chính thức (비공식적)**. Tài liệu được gửi trước cho nhóm rà soát nghiên cứu, sau đó tác giả dẫn dắt cả nhóm đi qua từng phần nhằm mục đích tìm kiếm lỗi, chia sẻ tri thức và thu thập phản hồi cải tiến.
3. **인스펙션 (Inspection — Thẩm tra chính thức):**
   - Là hình thức rà soát **chính thức và nghiêm ngặt nhất (공식적 검토)** do một nhóm chuyên gia độc lập tiến hành.
   - **Tác giả không được làm chủ tọa**. Buổi họp do người điều phối độc lập (`주임 검토자 - Moderator`) chủ trì, có người đọc (`Reader`), người ghi chép lỗi (`Recorder`).
   - Sử dụng danh sách kiểm tra chuẩn hóa (`체크리스트 - Checklist`) để phát hiện và thống kê các khiếm khuyết phần mềm.

#### 7. Bẫy đề thi trắc nghiệm thường gặp (주의/함정)
- **Bẫy 1 (Phân loại chức năng vs phi chức năng):** Đề thi trắc nghiệm thường đưa ra một phát biểu về hiệu năng (Response time) hoặc bảo mật (Mã hóa SSL) và hỏi có phải Yêu cầu chức năng không $\rightarrow$ **SAI**. Mọi chỉ số về tốc độ, bảo mật, thời gian hoạt động, môi trường chạy đều là **비기능 요구사항 (Yêu cầu phi chức năng)**.
- **Bẫy 2 (Ký hiệu DFD):** DFD **hoàn toàn không có ký hiệu rẽ nhánh điều kiện (IF-ELSE) hay vòng lặp**. Nếu đề thi hỏi *"DFD có biểu diễn luồng điều khiển logic của thuật toán không?"* $\rightarrow$ **Hoàn toàn KHÔNG (제어 흐름 표현 불가)**.
- **Bẫy 3 (Verification vs Validation):** Nhớ mẹo tiếng Anh:
  - *"Building the product right?"* (Đúng quy trình/đặc tả) $\rightarrow$ **Verification (검증)**.
  - *"Building the right product?"* (Đúng sản phẩm khách cần) $\rightarrow$ **Validation (확인)**.
- **Bẫy 4 (Walkthrough vs Inspection):**
  - Rà soát không chính thức, tác giả chủ trì $\rightarrow$ **워크스루 (Walkthrough)**.
  - Rà soát chính thức, dùng Checklist, Moderator độc lập chủ trì $\rightarrow$ **인스펙션 (Inspection)**.

- **한 문장 설명 (Câu chốt ghi nhớ):** "Hiện trạng khảo sát hạ tầng, Kỹ nghệ yêu cầu chia chức năng với phi chức năng; DFD chuyển dữ liệu, DD giải nghĩa ký hiệu; Verification soi đặc tả, Validation chiều lòng người dùng".

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Cơ chế vận hành của Kỹ thuật Delphi trong thu thập yêu cầu
- Trong các dự án phát triển phần mềm mang tính đột phá (ví dụ: áp dụng AI vào chẩn đoán y tế), các bên liên quan thường bất đồng quan điểm dữ dội và những người có chức vụ cao thường chi phối buổi họp.
- Phương pháp Delphi triệt tiêu rủi ro này qua 4 bước:
  1. Người điều phối gửi bảng câu hỏi mở về tính năng và rủi ro cho nhóm chuyên gia ẩn danh (các chuyên gia không biết danh tính của nhau).
  2. Các chuyên gia trả lời độc lập và gửi lại cho người điều phối.
  3. Người điều phối thống kê kết quả, giấu tên người phát biểu, tóm tắt các điểm đồng thuận và các quan điểm trái chiều, rồi gửi lại bảng câu hỏi vòng 2 cho toàn bộ chuyên gia.
  4. Các chuyên gia đọc lại lập luận của đồng nghiệp, suy ngẫm và điều chỉnh câu trả lời của mình. Quá trình này lặp lại 3-4 vòng cho đến khi dải ý kiến hội tụ về một phương án thống nhất cao.

#### 2. Quy trình thẩm định yêu cầu thu nhỏ (Mini-Trace Checklist)
Khi cầm trên tay tài liệu đặc tả SRS, kỹ sư kiểm tra tính đạt chuẩn qua 5 tiêu chí vàng:
1. **완전성 (Completeness - Tính đầy đủ):** Đã đặc tả đủ mọi trường hợp nhập liệu hợp lệ và không hợp lệ (Error handling) chưa?
2. **일관성 (Consistency - Tính nhất quán):** Có mục nào ở chương 2 định nghĩa thuật ngữ trái ngược với chương 5 không?
3. **명확성 (Unambiguity - Tính rõ ràng):** Có dùng các từ ngữ mơ hồ như "hệ thống phải chạy nhanh", "giao diện phải đẹp mắt" không? (Phải lượng hóa thành giây, pixel).
4. **검증 가능성 (Verifiability - Tính kiểm chứng được):** Có thể viết được bài test để kiểm tra xem yêu cầu này pass hay fail không?
5. **추적성 (Traceability - Tính truy xuất được):** Mỗi dòng yêu cầu có mã định danh duy nhất (ID) để nối sang tài liệu thiết kế và Test Case không?

#### 3. Sơ đồ đối chiếu trực quan 4 ký hiệu DFD (DeMarco vs Gane/Sarson)

##### A. Bảng sơ đồ ASCII so sánh ký hiệu Yourdon/DeMarco vs Gane/Sarson
```
┌─────────────────┬───────────────────────────────┬───────────────────────────────┐
│ Thành phần DFD  │ Yourdon & DeMarco (Cổ điển)   │ Gane & Sarson (Hiện đại)      │
├─────────────────┼───────────────────────────────┼───────────────────────────────┤
│ 1. 프로세스      │          ,--------.           │     ┌───────────────────┐     │
│    (Process)    │        /   1.0    \         │     │ 1.0               │     │
│                 │       | 주문 접수  |         │     ├───────────────────┤     │
│                 │        \          /         │     │     주문 접수     │     │
│                 │          `--------'         │     └───────────────────┘     │
│                 │        [Hình tròn]          │   [Chữ nhật bo tròn góc]      │
├─────────────────┼───────────────────────────────┼───────────────────────────────┤
│ 2. 자료 흐름     │          주문 요청            │          주문 요청            │
│    (Data Flow)  │   ─────────────────────►      │   ─────────────────────►      │
│                 │      [Mũi tên có tên]         │      [Mũi tên có tên]         │
├─────────────────┼───────────────────────────────┼───────────────────────────────┤
│ 3. 자료 저장소    │   ═════════════════════════   │     ┌───┬───────────────      │
│   (Data Store)  │          D1 고객 정보          │     │D1 │   고객 정보         │
│                 │   ═════════════════════════   │     └───┴───────────────      │
│                 │   [Hai đường song song]       │   [Chữ nhật hở cạnh phải]     │
├─────────────────┼───────────────────────────────┼───────────────────────────────┤
│ 4. 단말         │     ┌───────────────────┐     │     ┌───────────────────┐     │
│   (Terminator/  │     │                   │     │     │                   ││    │
│    External)    │     │      고객         │     │     │      고객         ││    │
│                 │     │                   │     │     │                   ││    │
│                 │     └───────────────────┘     │     └───────────────────┘│    │
│                 │      [Hình chữ nhật]          │   [Chữ nhật đổ bóng 3D] │    │
└─────────────────┴───────────────────────────────┴───────────────────────────────┘
```

##### B. Quy tắc bảo toàn dữ liệu và 3 lỗi vi phạm kinh điển (Data Conservation Flaws)
Trong phân tích DFD, dữ liệu không thể tự sinh ra hoặc biến mất. Mọi luồng dữ liệu vào phải được xử lý để sinh ra dữ liệu ra tương xứng:
1. **블랙홀 (Black Hole - Hố đen):**
   - **Hiện tượng:** Một Process chỉ có các luồng dữ liệu đi vào (`Input`) mà hoàn toàn không có bất kỳ luồng dữ liệu nào đi ra (`Output`).
   - **Bản chất lỗi:** Dữ liệu bị đưa vào và "biến mất" mà không phục vụ mục đích xử lý nào.
2. **미라클 / 화이트홀 (Miracle / White Hole - Điều kỳ diệu):**
   - **Hiện tượng:** Một Process tự phát sinh ra các luồng dữ liệu đi ra (`Output`) mà không hề có bất kỳ luồng dữ liệu nào đi vào (`Input`).
   - **Bản chất lỗi:** Không có nguyên liệu đầu vào nhưng lại đòi hỏi sản phẩm đầu ra (vi phạm định luật bảo toàn).
3. **그레이홀 (Grey Hole - Hố xám):**
   - **Hiện tượng:** Process có cả luồng vào và luồng ra, nhưng luồng vào không đủ thông tin hoặc không liên quan ngữ nghĩa để tạo ra luồng ra (ví dụ: Đầu vào là `Mã nhân viên`, đầu ra là `Báo cáo doanh số bán hàng quý`).

##### C. Các kết nối bất hợp lệ bị cấm trong DFD
- ❌ **External Entity $\longleftrightarrow$ External Entity:** Hai thực thể ngoài không bao giờ nối trực tiếp với nhau (hệ thống không quản lý giao tiếp ngoài biên).
- ❌ **External Entity $\longleftrightarrow$ Data Store:** Thực thể bên ngoài không được phép đọc/ghi trực tiếp vào CSDL mà bắt buộc phải thông qua một Process trung gian.
- ❌ **Data Store $\longleftrightarrow$ Data Store:** Dữ liệu không thể tự nhảy từ bảng này sang bảng khác mà phải có Process đọc từ kho A, biến đổi và lưu sang kho B.

---

#### 4. Phân tích chuyên sâu Từ điển dữ liệu (Data Dictionary - DD)

##### A. Bảng tổng hợp 6 ký hiệu toán tử chuẩn trong đề thi
Từ điển dữ liệu (`자료 사전 - DD`) đóng vai trò là "siêu dữ liệu" (`메타데이터 - Meta-data`), định nghĩa cấu trúc chi tiết của mọi luồng dữ liệu xuất hiện trong DFD:

| Ký hiệu toán tử | Tên tiếng Hàn & Anh | Ý nghĩa cú pháp kỹ thuật | Quy tắc logic tương đương |
|:---:|:---|:---|:---|
| `=` | `정의 (Definition)` | Được định nghĩa là / Bao gồm các thành phần | Phép gán cấu trúc (`is composed of`) |
| `+` | `연결 (Concatenation)` | Ghép nối tuần tự các phần tử dữ liệu | Phép logic `AND` (bắt buộc cùng xuất hiện) |
| `( )` | `생략 (Optional)` | Thành phần tùy chọn, có thể có hoặc vắng mặt | Tương đương lực lượng $0 \le n \le 1$ |
| `{ }` | `반복 (Iteration)` | Thành phần lặp lại nhiều lần ($m\{...\}n$) | Vòng lặp từ $m$ đến $n$ lần (mặc định: $0 \le n \le \infty$) |
| `[ \| ]` | `선택 (Selection)` | Lựa chọn duy nhất một trong các nhánh | Phép logic `OR` (các phương án ngăn cách bằng `\|`) |
| `* *` | `설명 / 주석 (Comment)` | Lời ghi chú kỹ thuật, diễn giải bổ sung | Không ảnh hưởng đến cấu trúc trường dữ liệu |

##### B. Ví dụ giải phẫu một cấu trúc dữ liệu thực tế
Xét mô hình đặc tả đơn đặt hàng thương mại điện tử bằng Data Dictionary:
```text
주문서 = 주문번호 + 주문일자 + 고객정보 + 1{주문항목}N + (할인쿠폰코드) + 결제수단 + *배송메모*
```
Phân rã chi tiết từng thành phần:
- `고객정보 = 고객ID + 고객성명 + 연락처 + (배송지주소)`: Một khách hàng gồm ID, họ tên, số điện thoại bắt buộc (`+`), địa chỉ có thể chưa nhập (`()`).
- `주문항목 = 상품코드 + 상품명 + 수량 + 단가 + 금액`: Mỗi mặt hàng gồm mã, tên, số lượng, giá và tổng tiền.
- `1{주문항목}N`: Một đơn hàng phải có tối thiểu 1 mặt hàng và tối đa $N$ mặt hàng (thể hiện giới hạn lặp $m$ và $n$).
- `(할인쿠폰코드)`: Khách hàng có thể áp dụng mã giảm giá hoặc không áp dụng.
- `결제수단 = [ 신용카드 | 계좌이체 | 가상계좌 | 간편결제 ]`: Người dùng bắt buộc phải chọn chính xác 1 trong 4 hình thức thanh toán (`[]`).
- `*배송메모*`: Lời chú thích hướng dẫn giao hàng dành riêng cho shipper, là trường văn bản chú giải (`**`).

---

### 복습 체크리스트
- [ ] Phân biệt được 3 kiến trúc lưu trữ DAS (gắn trực tiếp), NAS (qua mạng LAN), SAN (mạng cáp quang chuyên dụng).
- [ ] Nhớ chu trình 4 bước phát triển yêu cầu: 도출 (Elicitation) $\rightarrow$ 분석 (Analysis) $\rightarrow$ 명세 (Specification) $\rightarrow$ 확인 (Validation).
- [ ] Phân biệt được bản chất của 기능 요구사항 (hệ thống làm gì) và 비기능 요구사항 (chất lượng, hiệu năng, bảo mật, ràng buộc).
- [ ] Vẽ và gọi tên đúng 4 thành phần của DFD (Process, Data Flow, Data Store, Terminator) và nhớ DFD không mô tả luồng điều khiển.
- [ ] Thuộc lòng ý nghĩa 6 ký hiệu trong Từ điển dữ liệu DD: `=`, `+`, `{}`, `[]`, `()`, `**`.
- [ ] Phân biệt được Z, VDM, Petri-net là 정형 명세 (Toán học hình thức).
- [ ] Trả lời chuẩn xác câu hỏi tiếng Anh: Verification ("product right?") vs Validation ("right product?").
- [ ] Phân biệt rõ sự khác nhau giữa 워크스루 (không chính thức) và 인스펙션 (chính thức, dùng Checklist, Moderator chủ trì).
