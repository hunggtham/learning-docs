# 1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối SDLC với phases, deliverables, feedback và governance, để vòng đời được quản lý qua bằng chứng từng chặng.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

소프트웨어, 생명, 주기

> **Nối mạch:** Ở chặng này của **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **소프트웨어 생명 주기 및 개발 방법론 (SDLC & Methodologies)**에서 만든 기준을 이어받아 **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)**, **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)

Sau khi đã đặt nền bằng **소프트웨어 생명 주기 및 개발 방법론 (SDLC & Methodologies)**, ta chuyển sang **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)**. Đây là mắt xích 2/69 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)** như một bài học cho người mới, hãy giữ câu hỏi: **một dự án đi qua những giai đoạn nào, mỗi mô hình phân bổ công việc và rủi ro ra sao?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **개념**, **폭포수 모형 (Waterfall Model)**, **나선형 모형 (Spiral Model)**, **프로토타입 모형 (Prototype Model)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: Toàn bộ quá trình phát triển (Yêu cầu -> Thiết kế -> Code -> Test -> Bảo trì). Là tiêu chuẩn để quản lý dự án, chi phí, nhân lực.
- **폭포수 모형 (Waterfall Model)**:
  - Tuần tự (선형 순차적). Xong bước này mới qua bước khác. Không quay lại được.
  - Phù hợp dự án có yêu cầu rõ ràng, hệ thống nhà nước/ngân hàng. Tài liệu là trọng tâm.
- **나선형 모형 (Spiral Model)**:
  - Do Boehm đề xuất. Trọng tâm: Phân tích rủi ro (위험 분석).
  - Chu trình: Kế hoạch (계획) -> Phân tích rủi ro (위험) -> Phát triển (개발) -> Đánh giá (평가).
  - Phù hợp dự án lớn, rủi ro cao.
- **프로토타입 모형 (Prototype Model)**:
  - Làm bản nháp (시제품) trước khi phát triển thật. Phù hợp khi yêu cầu chưa rõ ràng.
- **V-모형 (V-Model)**:
  - Mỗi bước phát triển tương ứng với một bước Test (Ánh xạ Dev-Test). Yêu cầu chất lượng cực cao (Y tế, Hàng không).

Ta có thể khép mục **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
