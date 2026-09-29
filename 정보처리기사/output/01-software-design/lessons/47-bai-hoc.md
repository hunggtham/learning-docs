# 4. 운영 환경 구축 고려사항 (Operation Environment Considerations)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **4. 운영 환경 구축 고려사항 (Operation Environment Considerations)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **4. 운영 환경 구축 고려사항 (Operation Environment Considerations)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **6. 구조적 분석 도구 (Structured Analysis Tools)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

운영, 환경, 구축, 고려사항

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **2. 스크럼 및 XP 추가 개념 (Advanced Scrum & XP)**에서 만든 기준을 이어받아 **4. 운영 환경 구축 고려사항 (Operation Environment Considerations)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 4. 운영 환경 구축 고려사항 (Operation Environment Considerations)

Sau khi đã đặt nền bằng **2. 스크럼 및 XP 추가 개념 (Advanced Scrum & XP)**, ta chuyển sang **4. 운영 환경 구축 고려사항 (Operation Environment Considerations)**. Đây là mắt xích 47/55 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **4. 운영 환경 구축 고려사항 (Operation Environment Considerations)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **WAS (Web Application Server)**, **오픈 소스 (Open Source)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **운영체제 (OS)** & **DBMS**: 가용성 (Availability), 성능 (Performance), 기술 지원 (Tech Support), 구축 비용 (Cost). 
  - OS có thêm: 주변 기기 (Thiết bị ngoại vi).
  - DBMS có thêm: 상호 호환성 (Khả năng tương thích - JDBC/ODBC).
- **WAS (Web Application Server)**: Xử lý nội dung động. Có thêm **가비지 컬렉션 (GC - Dọn rác)**.
- **오픈 소스 (Open Source)**: Cần chú ý 라이선스 (Bản quyền), 사용자 수 (Số lượng người dùng), 기술의 지속 가능성 (Khả năng duy trì công nghệ).

Ta có thể khép mục **4. 운영 환경 구축 고려사항 (Operation Environment Considerations)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **6. 구조적 분석 도구 (Structured Analysis Tools)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.