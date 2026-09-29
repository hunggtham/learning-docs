# 1. 소프트웨어 아키텍처 (Software Architecture)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **1. 소프트웨어 아키텍처 (Software Architecture)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **1. 소프트웨어 아키텍처 (Software Architecture)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **6. 객체지향 (Hướng Đối Tượng - OOP)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

소프트웨어, 아키텍처

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)**에서 만든 기준을 이어받아 **1. 소프트웨어 아키텍처 (Software Architecture)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 1. 소프트웨어 아키텍처 (Software Architecture)

Từ **13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)**, ta đã có điểm tựa để bước vào **1. 소프트웨어 아키텍처 (Software Architecture)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 24/55 trước khi đi vào chi tiết.

Để đọc **1. 소프트웨어 아키텍처 (Software Architecture)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **상위 설계 (High-level)**, **하위 설계 (Low-level)**, **아키텍처 패턴 (Architecture Patterns)**, **레이어 패턴 (Layers)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **상위 설계 (High-level)**: 아키텍처 (Architecture), 자료구조 (Data Structure), 인터페이스 (Interface).
- **하위 설계 (Low-level)**: 모듈 (Module), 프로시저 (Procedure).
- **아키텍처 패턴 (Architecture Patterns)**:
  - **레이어 패턴 (Layers)**: Chia thành các tầng (OSI 7 layer).
  - **클라이언트-서버 패턴 (Client-Server)**: Máy khách - Máy chủ.
  - **파이프-필터 패턴 (Pipe-Filter)**: Dữ liệu qua các bộ lọc liên tiếp (Ví dụ: Unix shell).
  - **MVC 패턴**: Model (Dữ liệu), View (Giao diện), Controller (Điều khiển).
  - **브로커 패턴 (Broker)**: Có môi giới ở giữa.
  - **마스터-슬레이브 (Master-Slave)**: Một chủ, nhiều tớ (Hệ thống thời gian thực).

Điểm chốt của **1. 소프트웨어 아키텍처 (Software Architecture)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **6. 객체지향 (Hướng Đối Tượng - OOP)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.