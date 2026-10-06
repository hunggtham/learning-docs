# 7. 공통 모듈 (Common Module)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **7. 공통 모듈 (Common Module)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối common module với reuse, interface, cohesion và dependency, để dùng chung không tạo coupling ẩn.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **7. 공통 모듈 (Common Module)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **7. 공통 모듈 (Common Module)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **9. 효과적인 모듈 설계 방안 (Effective Module Design)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **7. 공통 모듈 (Common Module)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

공통, 모듈

> **Nối mạch:** Ở chặng này của **7. 공통 모듈 (Common Module)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **2. 모듈 (Module) & 독립성 (Independence)**에서 만든 기준을 이어받아 **7. 공통 모듈 (Common Module)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **7. 공통 모듈 (Common Module)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **7. 공통 모듈 (Common Module)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **7. 공통 모듈 (Common Module)**, **7. 공통 모듈 (Common Module)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 7. 공통 모듈 (Common Module)

Sau khi đã đặt nền bằng **2. 모듈 (Module) & 독립성 (Independence)**, ta chuyển sang **7. 공통 모듈 (Common Module)**. Đây là mắt xích 32/69 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **7. 공통 모듈 (Common Module)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 여러 프로그램에서 공통적으로 사용할 수 있는 모듈 (Module dùng chung cho nhiều chương trình, ví dụ: Đăng nhập, tính toán).

*   **명세 기법 5가지 (5 nguyên tắc viết đặc tả module):**
    1.  **정확성 (Correctness):** 정확히 작성 (Chính xác).
    2.  **명확성 (Clarity):** 중의적이지 않게 (Rõ ràng, không mơ hồ).
    3.  **완전성 (Completeness):** 모든 것을 빠짐없이 (Đầy đủ).
    4.  **일관성 (Consistency):** 상호 충돌 없게 (Nhất quán).
    5.  **추적성 (Traceability):** 출처, 관계 추적 가능 (Có thể truy xuất nguồn gốc).
💡 **Mẹo ghi nhớ:** C-M-H-N-T (Chính-Rõ-Đủ-Nhất-Truy) -> **Chỉ Mong Học Nhất Trường**

---

Ta có thể khép mục **7. 공통 모듈 (Common Module)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **9. 효과적인 모듈 설계 방안 (Effective Module Design)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **7. 공통 모듈 (Common Module)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
