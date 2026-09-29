# 1. 사용자 인터페이스 (User Interface - UI)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **1. 사용자 인터페이스 (User Interface - UI)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **1. 사용자 인터페이스 (User Interface - UI)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

사용자, 인터페이스

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **4. 사용자 인터페이스 (Giao diện người dùng - UI)**에서 만든 기준을 이어받아 **1. 사용자 인터페이스 (User Interface - UI)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 1. 사용자 인터페이스 (User Interface - UI)

Từ **4. 사용자 인터페이스 (Giao diện người dùng - UI)**, ta đã có điểm tựa để bước vào **1. 사용자 인터페이스 (User Interface - UI)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 18/55 trước khi đi vào chi tiết.

Để đọc **1. 사용자 인터페이스 (User Interface - UI)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **UI 유형 (UI Types)**, **모바일 제스처 (Mobile Gestures)**, **UI 기본 원칙 (4 Principles)**, **직관성 (Intuitiveness)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **UI 유형 (UI Types)**: 
  - CLI (Dòng lệnh), GUI (Đồ họa), NUI (Cử chỉ tự nhiên như chạm, vuốt), OUI (Hữu cơ).
  - **모바일 제스처 (Mobile Gestures)**: Tap (Chạm), Double Tap, Drag (Kéo), Pan (Di chuyển liên tục), Press (Nhấn giữ), Flick (Vuốt nhanh), Pinch (Phóng to/thu nhỏ bằng 2 ngón).
- **UI 기본 원칙 (4 Principles)**:
  - **직관성 (Intuitiveness)**: Dễ hiểu, trực quan.
  - **유효성 (Efficiency)**: Đạt được mục tiêu chính xác.
  - **학습성 (Learnability)**: Dễ học.
  - **유연성 (Flexibility)**: Linh hoạt, giảm thiểu lỗi.
  - 💡 **Mẹo ghi nhớ**: T/H/H/N -> **Trực Học Hằng Ngày**
- **UI 설계 도구 (UI Design Tools)**:
  - **와이어프레임 (Wireframe)**: Khung xương (Tĩnh).
  - **목업 (Mockup)**: Thiết kế tĩnh, giống thật nhất.
  - **스토리보드 (Storyboard)**: Bản hướng dẫn chi tiết, có luồng di chuyển.
  - **프로토타입 (Prototype)**: Mô hình động, có thể tương tác.

---
# Chapter 3. 애플리케이션 설계 (Application Design)

Điểm chốt của **1. 사용자 인터페이스 (User Interface - UI)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.