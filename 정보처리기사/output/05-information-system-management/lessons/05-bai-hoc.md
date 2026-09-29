# 336. 소프트웨어 개발 프레임워크 (Software Development Framework)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **336. 소프트웨어 개발 프레임워크 (Software Development Framework)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **336. 소프트웨어 개발 프레임워크 (Software Development Framework)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

소프트웨어, 개발, 프레임워크

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크**에서 만든 기준을 이어받아 **336. 소프트웨어 개발 프레임워크 (Software Development Framework)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **336. 소프트웨어 개발 프레임워크 (Software Development Framework)** và nối nó với **3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 336. 소프트웨어 개발 프레임워크 (Software Development Framework)

Sau khi đã đặt nền bằng **5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크**, ta chuyển sang **336. 소프트웨어 개발 프레임워크 (Software Development Framework)**. Đây là mắt xích 5/61 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **336. 소프트웨어 개발 프레임워크 (Software Development Framework)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **개념**, **특성**, **Tiếng Việt** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **개념**: 개발에 공통 사용되는 구조를 제공하여 생산성을 높이는 기반.
- **특성**: 모듈화, 재사용성, 확장성, **제어의 역흐름(IoC)**.
- **Tiếng Việt**: Nền tảng cấu trúc sẵn giúp tăng năng suất (như Spring, .NET). Đặc tính: Module hóa, Tái sử dụng, Mở rộng, Đảo ngược luồng điều khiển (IoC).

Ta bắt đầu phần nội dung bằng **자주 혼동하는 판별 포인트**. Hãy xác định **자주 혼동하는 판별 포인트** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 자주 혼동하는 판별 포인트

Phần nguồn của **자주 혼동하는 판별 포인트** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- COCOMO의 고전 유형은 **Organic / Semi-Detached / Embedded**이며 Sequential은 유형명이 아니다.
- RIP는 거리 벡터 방식이고 최대 15홉을 사용한다. OSPF는 링크 상태 방식, BGP는 AS 간 경로 제어다.
- AES·DES·SEED는 대칭키, RSA는 공개키 알고리즘이다. 해시(MD5/SHA 계열)는 암·복호화 키를 교환하는 알고리즘이 아니라 일방향 요약 함수다.
- Chinese Wall은 이해상충 방지, Bell-LaPadula는 기밀성, Biba는 무결성 중심 모델이다.

Các bullet của **자주 혼동하는 판별 포인트** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **자주 혼동하는 판별 포인트**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **336. 소프트웨어 개발 프레임워크 (Software Development Framework)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.