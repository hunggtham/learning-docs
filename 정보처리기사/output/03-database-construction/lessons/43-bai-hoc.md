# 183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối functional dependency với normalization và transitive dependency, để phát hiện dư thừa và bất nhất từ quy tắc phụ thuộc.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **186. 시스템 카탈로그 (System Catalog)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

함수적, 종속과, 이행적, 종속

> **Nối mạch:** Ở chặng này của **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **178. 관계해석 (Relational Calculus)**에서 만든 기준을 이어받아 **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)**, **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)

Ở bước 43/54, **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)** xuất hiện như phần tiếp nối của **178. 관계해석 (Relational Calculus)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **함수적 종속 (Functional Dependency):** X -> Y (X가 결정되면 Y가 결정됨).
- **이행적 종속 (Transitive Dependency):** A -> B, B -> C 일 때 A -> C 인 관계.
- **VI (Vietnamese) (Tiếng Việt):** Phụ thuộc hàm và Phụ thuộc bắc cầu.

Như vậy, **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **186. 시스템 카탈로그 (System Catalog)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
