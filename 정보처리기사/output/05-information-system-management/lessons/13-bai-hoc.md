# 8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

정보, 보안, 일반, 시스템

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)**에서 만든 기준을 이어받아 **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)

Ở bước 13/18, **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)** xuất hiện như phần tiếp nối của **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **8.1 보안 기본 요소 및 프레임워크** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **8.1 보안 기본 요소 및 프레임워크** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 8.1 보안 기본 요소 및 프레임워크

Bây giờ ta đi vào nội dung của **8.1 보안 기본 요소 및 프레임워크**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **보안 3대 요소 (CIA Triad):**
  - **기밀성 (Confidentiality):** 인가된 사용자에게만 접근 허용.
  - **무결성 (Integrity):** 인가된 사용자만 수정 가능.
  - **가용성 (Availability):** 인가받은 사용자는 언제라도 사용 가능.
- **Seven Touchpoints:** 소프트웨어 보안 모범사례를 SDLC(소프트웨어 생명주기)에 통합.
- **OWASP:** 웹 보안 취약점을 연구하는 비영리 단체.
- **관리적/물리적/기술적 보안:**
  - 관리적 (정책, 교육), 물리적 (출입 통제, 재해 복구), 기술적 (사용자 인증, 접근 제어).
- **Tiếng Việt:** 3 yếu tố bảo mật CIA: Tính bảo mật, Tính toàn vẹn, Tính sẵn sàng.

Các bullet của **8.1 보안 기본 요소 및 프레임워크** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **8.1 보안 기본 요소 및 프레임워크** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **8.2 시스템 보안 기술** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **8.2 시스템 보안 기술**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 8.2 시스템 보안 기술

Phần nguồn của **8.2 시스템 보안 기술** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

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

Các bullet của **8.2 시스템 보안 기술** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **8.2 시스템 보안 기술** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.