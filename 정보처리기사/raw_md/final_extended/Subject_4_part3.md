## 인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)
### TẦNG A – NOTE NÉN (ÔN / ĐI THI)
- **개념 (Khái niệm)**: 소스 코드를 컴파일하지 않고 인터프리터(Interpreter)가 한 줄씩 즉시 해석하여 실행하는 프로그래밍 언어. (Ngôn ngữ lập trình dịch và thực thi từng dòng mã nguồn trực tiếp mà không cần biên dịch toàn bộ.)
- **핵심 키워드 (Từ khóa)**: 자바 스크립트 (JavaScript), PHP, 파이썬 (Python), 쉘 스크립트 (Shell script).
- **시험 포인트 (Điểm thi)**: 클라이언트용(Client-side: JS)과 서버용(Server-side: ASP, JSP, PHP) 스크립트 언어를 구분하는 것이 단골 문제. (Phân biệt ngôn ngữ cho Client và Server là câu hỏi thường gặp.)
- **한 문장 설명 (Tóm tắt)**: 컴파일 과정이 없어 실행 속도가 빠르고 수정이 용이하여 웹 개발 및 시스템 관리에 널리 사용됨. (Tốc độ khởi động nhanh và dễ sửa đổi vì không cần biên dịch, phổ biến trong web và quản trị hệ thống.)

### TẦNG B – NOTE 보충 (HIỂU SÂU)
- **자바 스크립트 (JavaScript)**: 웹 브라우저 내에서 동작하며 입력 사항 확인 등 클라이언트 측 제어에 사용. (Chạy trên trình duyệt, kiểm soát phía client như xác thực đầu vào.)
- **PHP**: 서버용 스크립트로 C, Java와 문법이 유사. (Script cho server, cú pháp giống C/Java.)
- **파이썬 (Python)**: 객체지향 지원, 문법이 간단하여 배우기 쉽고 플랫폼 독립적인 대화형 언어. (Hỗ trợ OOP, cú pháp đơn giản, độc lập nền tảng, có tính tương tác.)
- **쉘 스크립트 (Shell Script)**: 유닉스/리눅스의 쉘 명령어를 조합한 관리용. (Kết hợp lệnh shell Linux/Unix để quản trị.)
- **ASP / JSP**: 서버 측 동적 페이지 생성 언어 (ASP의 마이크로소프트, JSP의 자바 기반). (ASP của MS, JSP của Java.)
- **예시 (Ví dụ)**: 브라우저에서 버튼을 누르면 즉시 알림창이 뜨는 JS 코드는 컴파일 없이 바로 실행됨. (Mã JS hiển thị thông báo khi bấm nút trên trình duyệt chạy ngay mà không cần biên dịch.)
- 💡 **Mẹo ghi nhớ**: JS là Client, còn lại PPP (PHP, JSP, ASP) đa số là Server.

## 284 & 294. 구역성 (Locality / Tính cục bộ)
### TẦNG A – NOTE NÉN (ÔN / ĐI THI)
- **개념 (Khái niệm)**: 프로세스가 실행되는 동안 주기억장치(Main memory)의 특정 영역만을 집중적으로 참조하는 성질. (Tính chất mà quá trình chỉ tham chiếu tập trung vào một số trang nhất định của bộ nhớ chính khi thực thi.)
- **핵심 키워드 (Từ khóa)**: 시간 구역성 (Temporal locality), 공간 구역성 (Spatial locality), 집중 참조 (Concentrated reference).
- **시험 포인트 (Điểm thi)**: 시간 구역성(Loop, Stack)과 공간 구역성(Array)의 구체적인 사례를 구분하는 것. (Phân biệt ví dụ của cục bộ thời gian và cục bộ không gian.)
- **한 문장 설명 (Tóm tắt)**: 스래싱(Thrashing) 방지를 위한 핵심 이론. (Lý thuyết cốt lõi để ngăn chặn hiện tượng Thrashing.)

### TẦNG B – NOTE 보충 (HIỂU SÂU)
- **시간 구역성 (Temporal locality)**: 한 번 참조된 페이지는 가까운 시간 내에 다시 참조될 가능성이 높음. (Trang vừa dùng sẽ có khả năng cao được dùng lại sớm. Ví dụ: Vòng lặp/Loop, Ngăn xếp/Stack, Biến đếm.)
- **공간 구역성 (Spatial locality)**: 특정 페이지가 참조되면 인근 위치의 페이지가 계속 참조될 가능성이 높음. (Trang vừa dùng thì các trang liền kề nó dễ được gọi theo. Ví dụ: Mảng/Array, duyệt tuần tự.)
- **예시 (Ví dụ)**: 배열 `A[0]`부터 `A[100]`까지 순서대로 읽는 것은 공간 구역성이고, `for`문 안에서 변수 `i`를 계속 증가시키며 쓰는 것은 시간 구역성. (Đọc mảng theo thứ tự là cục bộ không gian; dùng biến i nhiều lần trong vòng lặp là cục bộ thời gian.)
- 💡 **Mẹo ghi nhớ**: **T**emporal = **T**ime (Lặp lại nhiều lần/Loop), **S**patial = **S**pace (Gần nhau/Array).

## 285 & 295. 워킹 셋 (Working Set / Tập làm việc)
### TẦNG A – NOTE NÉN (ÔN / ĐI THI)
- **개념 (Khái niệm)**: 프로세스가 원활한 수행을 위해 일정 시간 동안 집중적으로 참조하는 페이지들의 집합. (Tập hợp các trang mà tiến trình tham chiếu tập trung trong một khoảng thời gian để chạy mượt mà.)
- **핵심 키워드 (Từ khóa)**: 데닝 (Denning), Locality 활용 (Ứng dụng Locality), 페이지 부재 감소 (Giảm Page Fault), 동적 변경 (Thay đổi động).
- **시험 포인트 (Điểm thi)**: 자주 참조되는 워킹 셋을 주기억장치에 상주시킴으로써 시스템을 안정화(스래싱 방지)한다는 점. (Giữ Working Set trong bộ nhớ chính giúp hệ thống ổn định và tránh Thrashing.)

### TẦNG B – NOTE 보충 (HIỂU SÂU)
- 데닝(Denning)이 제안한 모델로, 프로그램의 국부성(Locality)을 이용. (Mô hình do Denning đề xuất dựa trên tính cục bộ.)
- 시간에 따라 참조하는 페이지가 달라지므로 지속적으로 (동적으로) 변경됨. (Thay đổi động theo thời gian.)
- **예시 (Ví dụ)**: 당신이 시험 공부를 할 때 지금 당장 책상 위에 꺼내놓은 책과 필기구들이 '워킹 셋'입니다. 과목이 바뀌면 책상 위 물건(워킹 셋)도 바뀝니다. (Những cuốn sách và bút bạn đang để trên bàn học ngay lúc này chính là 'Working Set'. Khi chuyển môn, đồ trên bàn cũng thay đổi.)
- 💡 **Mẹo ghi nhớ**: Working Set = Những món đồ đang "Working" (Đang dùng) phải để sẵn trên bàn (Memory).

## 287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)
### TẦNG A – NOTE NÉN (ÔN / ĐI THI)
- **개념 (Khái niệm)**: 커널(Kernel), 쉘(Shell), 유틸리티(Utility)의 계층적 구조. (Cấu trúc phân tầng gồm Kernel, Shell và Utility.)
- **핵심 키워드 (Từ khóa)**: 커널(Kernel - Hạt nhân), 쉘(Shell - Vỏ), 명령어 해석기 (Trình thông dịch lệnh).
- **시험 포인트 (Điểm thi)**: 커널(핵심 및 상주)과 쉘(명령어 해석기 및 인터페이스)의 역할을 명확히 구분. (Phân biệt vai trò của Kernel và Shell.)

### TẦNG B – NOTE 보충 (HIỂU SÂU)
- **커널 (Kernel)**: 하드웨어를 직접 관리, 프로세스/메모리/파일 관리. 주기억장치에 상주. (Quản lý trực tiếp phần cứng, tiến trình, bộ nhớ. Nằm thường trực trong RAM.)
- **쉘 (Shell)**: 사용자의 명령을 인식하여 수행하는 명령어 해석기 (인터페이스). (Trình biên dịch lệnh, nhận lệnh từ người dùng và gọi chương trình.)
- **유틸리티 (Utility)**: 에디터, 컴파일러 등 응용 프로그램. (Các chương trình ứng dụng như trình soạn thảo, biên dịch.)
- **예시 (Ví dụ)**: 식당에서 사용자가 주문(명령)을 하면 종업원(Shell)이 이를 받아 주방장(Kernel)에게 전달하여 요리(하드웨어 제어)를 하는 구조. (Khách hàng gọi món (Lệnh) -> Phục vụ bàn (Shell) -> Đầu bếp (Kernel) xử lý nấu nướng.)
- 💡 **Mẹo ghi nhớ**: Kernel là **Lõi** (Hardware), Shell là **Vỏ** (Giao tiếp người dùng).

## 292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)
### TẦNG A – NOTE NÉN (ÔN / ĐI THI)
- **개념 (Khái niệm)**: 주기억장치 빈 공간이 없을 때 어떤 페이지를 내보낼지 결정하는 기법. (Kỹ thuật chọn trang để loại bỏ khi bộ nhớ chính đã đầy để nhường chỗ cho trang mới.)
- **핵심 키워드 (Từ khóa)**: OPT, FIFO, LRU, LFU, NUR.
- **시험 포인트 (Điểm thi)**: 각 알고리즘별 교체 대상 선정 기준 묻는 문제. (Tiêu chí chọn trang của từng thuật toán.)

### TẦNG B – NOTE 보충 (HIỂU SÂU)
- **OPT (Optimal)**: 앞으로 가장 오랫동안 안 쓸 페이지 교체 (이론적 최고). (Thay trang sẽ lâu nhất không được dùng trong tương lai - Tốt nhất nhưng chỉ trên lý thuyết.)
- **FIFO (First-In First-Out)**: 들어온 지 가장 오래된 페이지 교체. (Thay trang vào bộ nhớ sớm nhất.)
- **LRU (Least Recently Used)**: 최근에 가장 오랫동안 안 쓴 페이지 교체. (Thay trang lâu nhất chưa được sử dụng tính từ hiện tại.)
- **LFU (Least Frequently Used)**: 참조 횟수가 가장 적은 페이지 교체. (Thay trang có số lần sử dụng ít nhất.)
- **NUR (Not Used Recently)**: 참조 비트와 변형 비트를 사용해 최근 미사용 페이지 교체. (Dùng bit tham chiếu và bit sửa đổi để loại trang không dùng gần đây.)
- **예시 (Ví dụ)**: 스마트폰에서 앱을 여러 개 켜다가 램이 부족해지면, 제일 먼저 켰던 앱(FIFO)을 끄거나 최근에 가장 안 본 앱(LRU)을 종료시킴. (Khi điện thoại đầy RAM, nó sẽ tắt app mở đầu tiên (FIFO) hoặc app lâu rồi chưa đụng tới (LRU).)
- 💡 **Mẹo ghi nhớ**: **R**ecently = Lâu không đụng (Thời gian), **F**requently = Ít dùng (Số lần). 

## 298. PCB (Process Control Block)
### TẦNG A – NOTE NÉN (ÔN / ĐI THI)
- **개념 (Khái niệm)**: 운영체제가 각 프로세스를 관리하기 위해 정보를 저장하는 데이터 구조. (Cấu trúc dữ liệu HĐH dùng để lưu thông tin quản lý từng tiến trình.)
- **핵심 키워드 (Từ khóa)**: 프로세스 상태 (Trạng thái tiến trình), 식별자 (PID), 우선순위 (Priority).
- **시험 포인트 (Điểm thi)**: 프로세스 생성 시 고유하게 생성되며, 종료 시 제거됨. (Được tạo ra duy nhất khi tiến trình bắt đầu và bị xóa khi kết thúc.)

### TẦNG B – NOTE 보충 (HIỂU SÂU)
- 현재 상태(준비/실행/대기), CPU 레지스터 정보, 자원 정보 포함. (Chứa trạng thái hiện tại, thanh ghi CPU, tài nguyên được cấp.)
- 문맥 교환(Context Switching) 시, 현재까지 진행 상황을 PCB에 저장. (Khi chuyển đổi ngữ cảnh, lưu tiến độ vào PCB để sau này chạy tiếp.)
- **예시 (Ví dụ)**: 병원에서 환자(프로세스)마다 차트(PCB)를 만들어 병력과 현재 상태를 기록하는 것과 같음. 퇴원하면 차트를 닫음. (Giống như Bệnh án (PCB) của từng bệnh nhân (Process), ghi lại tình trạng, xuất viện thì đóng hồ sơ.)
- 💡 **Mẹo ghi nhớ**: PCB giống như "Thẻ căn cước + Hồ sơ bệnh án" của một tiến trình.
