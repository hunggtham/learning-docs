# 098 & 기타 협업 도구 (Build Tools & Collaboration Tools)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **098 & 기타 협업 도구 (Build Tools & Collaboration Tools)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **098 & 기타 협업 도구 (Build Tools & Collaboration Tools)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **104-1 ~ 108: 소프트웨어 매뉴얼 (Software Manuals)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

기타, 협업, 도구

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)**에서 만든 기준을 이어받아 **098 & 기타 협업 도구 (Build Tools & Collaboration Tools)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 098 & 기타 협업 도구 (Build Tools & Collaboration Tools)

Sau khi đã đặt nền bằng **097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)**, ta chuyển sang **098 & 기타 협업 도구 (Build Tools & Collaboration Tools)**. Đây là mắt xích 92/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **098 & 기타 협업 도구 (Build Tools & Collaboration Tools)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **빌드 도구 (Build Tool)**. Hãy xác định **빌드 도구 (Build Tool)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 빌드 도구 (Build Tool)

Phần nguồn của **빌드 도구 (Build Tool)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 소스 코드를 실행할 수 있는 제품으로 변환(빌드)하는 과정을 자동화. (Công cụ tự động biên dịch và gom file code lại thành file chạy `.exe`, `.apk`...).
- **Ant:** Cổ điển, dùng cho Java, của Apache.
- **Maven:** Nâng cấp của Ant, quản lý thư viện (Dependencies) tự động.
- **Gradle:** Hiện đại nhất, lai giữa Ant và Maven, dùng nhiều cho Android.

Các bullet của **빌드 도구 (Build Tool)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **빌드 도구 (Build Tool)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **기타 협업 도구 (Groupware / Collaboration Tools)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **기타 협업 도구 (Groupware / Collaboration Tools)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 기타 협업 도구 (Groupware / Collaboration Tools)

Các ý ngay dưới **기타 협업 도구 (Groupware / Collaboration Tools)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **프로젝트 및 일정 관리 (Quản lý dự án):** Jira (지라), Trello, Google Calendar.
- **메신저 (Giao tiếp):** Slack, Jandi.
- **디자인 (Thiết kế UI -> Code):** Zeplin, Sketch.
- **기타:** Evernote (Ghi chú), Swagger (Tài liệu API tự động), GitHub (Lưu source code).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Jira = Quản lý công việc (Ticket). Slack = Chat. Zeplin = Thiết kế. Swagger = Viết Document cho API. Gradle = Build Android.

---

Với **기타 협업 도구 (Groupware / Collaboration Tools)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **기타 협업 도구 (Groupware / Collaboration Tools)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **098 & 기타 협업 도구 (Build Tools & Collaboration Tools)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **104-1 ~ 108: 소프트웨어 매뉴얼 (Software Manuals)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.