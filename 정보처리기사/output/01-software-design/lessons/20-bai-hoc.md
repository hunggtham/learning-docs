# 1. 사용자 인터페이스 (User Interface - UI)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **1. 사용자 인터페이스 (User Interface - UI)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối user interface với input, affordance, feedback và error recovery, để thao tác có thể hiểu và sửa.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **1. 사용자 인터페이스 (User Interface - UI)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **1. 사용자 인터페이스 (User Interface - UI)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **1. 사용자 인터페이스 (User Interface - UI)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

사용자, 인터페이스

> **Nối mạch:** Ở chặng này của **1. 사용자 인터페이스 (User Interface - UI)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **4. 사용자 인터페이스 (Giao diện người dùng - UI)**에서 만든 기준을 이어받아 **1. 사용자 인터페이스 (User Interface - UI)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **1. 사용자 인터페이스 (User Interface - UI)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **1. 사용자 인터페이스 (User Interface - UI)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **1. 사용자 인터페이스 (User Interface - UI)**, **1. 사용자 인터페이스 (User Interface - UI)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 1. 사용자 인터페이스 (User Interface - UI)

Sau khi đã đặt nền bằng **4. 사용자 인터페이스 (Giao diện người dùng - UI)**, ta chuyển sang **1. 사용자 인터페이스 (User Interface - UI)**. Đây là mắt xích 20/69 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **1. 사용자 인터페이스 (User Interface - UI)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **UI 유형 (UI Types)**, **모바일 제스처 (Mobile Gestures)**, **UI 기본 원칙 (4 Principles)**, **직관성 (Intuitiveness)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “1. 사용자 인터페이스 (User Interface - UI)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **UI 유형 (UI Types)**:
  - CLI (Dòng lệnh), GUI (Đồ họa), NUI (Cử chỉ tự nhiên như chạm, vuốt), OUI (Hữu cơ).
  - **모바일 제스처 (Mobile Gestures)**: Tap (Chạm), Double Tap, Drag (Kéo), Pan (Di chuyển liên tục), Press (Nhấn giữ), Flick (Vuốt nhanh), Pinch (Phóng to/thu nhỏ bằng 2 ngón).
- **UI 기본 원칙 (4 Principles)**:
  - **직관성 (Intuitiveness)**: Dễ hiểu, trực quan.
  - **유효성 (Effectiveness)**: Đạt được mục tiêu của người dùng một cách chính xác và đầy đủ.
  - **학습성 (Learnability)**: Dễ học.
  - **유연성 (Flexibility)**: Linh hoạt, giảm thiểu lỗi.
  - 💡 **Mẹo ghi nhớ**: T/H/H/N -> **Trực Học Hằng Ngày**
- **UI 설계 도구 (UI Design Tools)**:
  - **와이어프레임 (Wireframe)**: Khung xương (Tĩnh).
  - **목업 (Mockup)**: Thiết kế tĩnh, giống thật nhất.
  - **스토리보드 (Storyboard)**: Bản hướng dẫn chi tiết, có luồng di chuyển.
  - **프로토타입 (Prototype)**: Mô hình động, có thể tương tác.

---

Ta có thể khép mục **1. 사용자 인터페이스 (User Interface - UI)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **1. 사용자 인터페이스 (User Interface - UI)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
