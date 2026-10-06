# 199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối testing strategies với level, oracle, risk và feedback, để chiến lược kiểm thử phân bổ bằng chứng theo mục tiêu.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **200. 유지보수 (Maintenance / Bảo trì phần mềm)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

검사, 전략

> **Nối mạch:** Ở chặng này của **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)**에서 만든 기준을 이어받아 **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)**, **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)

Ở bước 61/91, **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)** xuất hiện như phần tiếp nối của **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **단위 검사 (Unit Testing)**, **하향식 통합 검사 (Top-Down Integration)**, **상향식 통합 검사 (Bottom-Up Integration)**, **검증(확인) 검사 (Validation Testing)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **단위 검사 (Unit Testing)**: 코딩 후 최소 단위인 '모듈' 초점 검사 (화이트 박스 기법).
- **하향식 통합 검사 (Top-Down Integration)**: 상위 모듈 -> 하위 모듈 방향. 임시 시험용 모듈인 **스터브(Stub)** 필요.
- **상향식 통합 검사 (Bottom-Up Integration)**: 하위 모듈 -> 상위 모듈 방향. 제어 모듈과 종속 모듈 그룹인 **클러스터(Cluster)**와 드라이버(Driver) 필요. (Stub 불필요).
- **검증(확인) 검사 (Validation Testing)**: 요구사항 충족 여부 확인 (블랙 박스 기법).
  - **알파 검사 (Alpha Test)**: **개발자 환경(장소)**에서 사용자가 테스트 (통제된 환경).
  - **베타 검사 (Beta Test)**: **실제 사용자 환경**에서 여러 사용자가 테스트 (개발자 통제 없음).
- **시스템 검사 (System Test)**: 전체 시스템(하드웨어 포함)에서 완벽히 수행되는지 검사. (복구/보안/강도/성능 검사).

**Giải thích (Vietnamese):**
- Kiểm thử tích hợp từ trên xuống (Top-down) cần làm các module giả (Stub) để thay thế cho module con chưa code xong. Từ dưới lên (Bottom-up) cần nhóm (Cluster/Driver) để gọi module con.
- Alpha Test: Bạn mời khách hàng đến công ty bạn ngồi test app trước mặt bạn.
- Beta Test: Bạn tung app lên store cho người dùng tải về dùng thử và báo lỗi (bạn không ngồi cạnh họ).

**💡 Mẹo ghi nhớ (Mnemonics):**
**하스 상드** (Hạ - Stub, Thượng - Driver): **하**향식 = **스**터브(Stub). **상**향식 = 드라이버(Driver)/클러스터(Cluster).

---

Như vậy, **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **200. 유지보수 (Maintenance / Bảo trì phần mềm)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
